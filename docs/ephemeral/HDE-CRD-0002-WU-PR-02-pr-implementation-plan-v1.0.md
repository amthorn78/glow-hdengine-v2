---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-02-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
predecessor: none (first plan for WU-PR-02)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob b98bf846287d92f90b3389d56d498f12964a91a9; 42,058 bytes; landed on main at b996a20, amthorn78/glow-hdengine-v2#632)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b292777cc562b64bb983bdc4c55e3b)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276dbb06fa2222dfb9d7f5ecf05740f3c) — lineage only
REMEDIATION_REVIEW_ID: none
RESCOPE_REQUEST_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10)
applicable_pf10_overlays: PF10 addendum 2.3 (reviewer chain without the Codex security review); addendum 2.1 governs the TypeSafe reading (§21). Addenda 2.2 and 2.4 are WU-PR-01 records and change nothing in this unit
effective_baseline: approved base + applicable PF10 overlays = the base above + PF10 addendum 2.3
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5, effective 2026.10.13; blob c98831e8112da05bbcc9fae7316f64d1657824ff; 50,181 bytes; sha256 fb2899266ec3635e7c734a880136fcfdd4cc5ebc5e2a340ae51cd7e33dca54d2; read in full by this session; one unlettered document; active addenda 2.1, 2.2, 2.3, 2.4)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md § "2.3 Codex security review is deprecated: it is no longer a step of the HDE pull-request review chain" (its record: docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md, blob acd6a465af184508934e5946af5b68c9da865744); § "2.1 GCFPE model and reasoning-level guidance is the TypeSafe reading; no AI recommendation is given" for §21
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); authoring session https://claude.ai/code/session_01KTTzbrYjNwVoPN3AtpbN4a
author: dedicated HDE-CRD-0002 WU-PR-02 PR engineering session (PR-20)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1", 55 members; read 2026-10-13)
created_at: 2026-10-13T17:42:24Z
repository_baseline: origin/main b996a20470dff2dfc4b7f2f23124e345ed53d2e7 (tree 093ceddc09b1892577b6879045279f389e6392ab; "HDE-CRD-0002 WU-PR-02: PR work-unit instruction v1.0 (PR-10) (#632)"). git diff cc3dc33..b996a20 adds only the instruction file, so every §5 fact the instruction measured at cc3dc33 holds at b996a20 unless §4 below corrects it
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); carried unchanged; no new entry (§18)
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff (planning prototype, source and test files only; inference support, not implementation; §4.4)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-02 — Detailed PR Implementation Plan v1.0

## 1. State and authority

**AWAITING_PO_PROCEED.** Held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.7.7).

This is the complete, executable plan for WU-PR-02 within approved scope: the approved base plus PF10 addendum 2.3. Every planned source and test change was applied together in a throwaway clone of `b996a20`, the governed companions were regenerated there by the updater, and the result was validated (§4.3). The prototype is inference support; none of its bytes enter the repository through this plan except the companion diff named in the front matter, which is a planning record.

This plan does not:
- authorize implementation, a commit to any path outside `docs/ephemeral/`, a pull request for the code, a merge, Ops, QA, acceptance or closure. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for exactly this plan and version authorizes implementation, and only Nathan merges;
- change canon, create a PF10 addendum, or decide a canon conflict;
- carry unapproved scope. No boundary finding arose (§16).

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-02 (Plan v1.1 §7 "WU-PR-02 — Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation)") |
| Requirements | S06, S11, S12, S13, S22; CD-3 (resolved by S22) |
| Instruction | PR instruction v1.0 (front matter), INSTRUCTION_READY, issued by the whole-change IA (session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j) |
| Approved base | Specification v1.1 → Implementation Plan v1.1 + IA-30 review v1.1 |
| Overlays | PF10 addendum 2.3 (reviewer chain). Addendum 2.1 governs §21 only |
| Upstream unit | WU-PR-01, accepted (lineage review v2.0; PF10 addendum 2.4) |
| Phase / Live QA class | Distillation / not production-affecting (Plan v1.1 §6) |
| Dependency state | Ready (instruction §3): no code dependency on WU-PR-01; lands before WU-PR-07 and before any member-changing unit's convergence |
| Order | WU-PR-01 → **WU-PR-02** → WU-PR-03 → WU-PR-04 → WU-PR-05 → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 |

## 3. Sources

Every source below was read on `main` at `b996a20` (canon is unchanged since `cc3dc33`).

- **Instruction (sole substantive input):** read in full, all 19 sections.
- **PF10:** `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md` read in full (front matter rules 1–9, index, addenda 2.1–2.4). Applicable: 2.3 (Rules 2 and 3: the Codex code review stays; the Codex security review is not part of the chain and its absence is not a gap) and 2.1 (TypeSafe reading, §21). 2.2 and 2.4 are WU-PR-01 records; their downstream items belong to WU-PR-03 and WU-PR-06. PF10 is otherwise silent on S06, S11, S12, S13 and S22 (Silence rule), so permanent canon governs them.
- **Permanent canon:** HDE Schemas & Artifacts §8.3 (read in full, "Single home and path" to "Path-proof transcript schema") and §8.17 "Change-container identity (normative)" and "Path provenance (normative)"; HDE Governance §9.1.1, §9.1.2, §9.7.7; Plan Templates "Repository loci and file minting", "CI lane classification and automated budget-control discipline"; Change Process Guide §0.2 and §1.0.4. Section citations as in "Canon relied on".
- **In-flight documents:** Specification v1.1 requirement rows S06, S11, S12, S13, S22 (verified verbatim against the instruction §4) and Exclusions; Plan v1.1 §5 (IF-5, IF-7), §7 common paragraph and WU-PR-02 block (verified verbatim), §10 re-cut procedure, §11 risks; `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` §3.3, §5.4, §6.3, §6.4 (the measured re-cut set and the frozen families); the WU-PR-01 plan v1.1 (format).
- **Repository:** `AGENTS.md`; `.github/workflows/ci.yml` (lanes); `ci/checks/classify_ci_changes.py` (owners); the seven source and test files of §6 and their consumers named in §4.2.
- **Workflow:** PR-20 (above, read in full); PR-30 — PR Implementation Proceed — 100926.1 (read in full for the handoff contract); the GCFPE Membership and Release Register "Current selection" (read back).
- **Not present:** `docs/changes/GCFPE_PROMPT_PROVENANCE.md` does not exist; prompt-use provenance stays in §22 (pending, non-gating).

## 4. Repository baseline (re-verified at `b996a20`)

### 4.1 Facts confirmed

| Instruction fact | Re-measured at `b996a20` |
| :- | :- |
| §5.2 closure probe imports `engine.config.registry_loader` in-process; refusal true only for `INCOMPLETE_RELEASE_ROSTER` | confirmed (`release_not_admitted_observed`, lines 384–393; file 421 lines) |
| §5.3 nested `release_id` counts | `two_run/identity.json` 3, `abba/ab_ba_parity.json` 4, `json_compare/core_result_json_compare.json` 2, `purity/purity_report.json` 0; every value `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` = sha256 of `catalog/manifest.json` (release `1.3.0`) |
| §5.4 Mirror | 620 rows (Index 620); 0 rows carry a release field |
| §5.5 CRD constants, `_crd_qa_entry`, `_load_crd_qa_entries`, `publish_crd_check_family` refusal "admits only HDE-CRD-0001" | confirmed (updater 4,981 lines) |
| §5.5 `check_mirror_schema.sh` `OPTIONAL_KEYS` lacks `crd_id`; `KEYS_EXTRA` on extra keys | confirmed; the file is a Python 3 script with a `.sh` name (shebang `#!/usr/bin/env python3`), 243 lines |
| §5.6 none of the unit's files is a release member; release lane selected by the four tool paths | confirmed by the classifier dry run on the prototype (§4.3) |

### 4.2 Facts that extend or correct the instruction

- **F-1 (S06 root cause).** The failure is not in setuptools' own code path but in two Ubuntu patches of `python3-setuptools` 68.1.2-2ubuntu1.2: `setuptools/command/install_lib.py` and `install_egg_info.py` call `set_undefined_options('install', ('install_layout', 'install_layout'))` and `('prefix_option', 'prefix_option')`. Those two options exist on the distutils `install` command only when `_distutils_system_mod` is importable; that module ships in `libpython3.12-stdlib` (`/usr/lib/python3.12/_distutils_system_mod.py`) and is imported by `setuptools/_distutils/__init__.py`. The non-distribution interpreter `/usr/bin/python3` (CPython 3.13.16, package `python3.13` 3.13.16-1+noble1) has no `_distutils_system_mod`, so the patched `install_lib` raises `AttributeError: install_layout` and, once that is supplied, `AttributeError: prefix_option`.
- **F-2 (no upstream backend to seed).** The invoking environment holds no unpatched setuptools: the distribution's wheel `/usr/share/python-wheels/setuptools-68.1.2-py3-none-any.whl` carries the same `install_layout` patch in both files. The instruction's first example design (seed an upstream backend from the invoking environment) is therefore not available offline here; §5.1 uses the second family (make the patched backend build the ordinary layout).
- **F-3 (upstream also imports the hook).** Upstream setuptools 84.0.0 (the CI-like venv) still imports `_distutils_system_mod` from `setuptools/_distutils/__init__.py`. A shim placed on the path unconditionally would also act on hosted CI; §5.1 therefore applies it only when the importable setuptools is the distribution-patched one.
- **F-4 (S13 blocks S06 off CI).** With S06 fixed alone, the full builder in an environment that has no ambient `engine` (no `-e .`) fails at `closure_write_and_check`: the closure script runs with `sys.path[0]` = its own directory, so the in-process probe raises `ModuleNotFoundError: No module named 'engine'` (reproduced, §4.3 R-4). On CI the editable install masks the defect by importing `engine` from the source checkout, not from the isolated copy. S06's acceptance is therefore only demonstrable together with S13.
- **F-5 (S13 consumer outside §6).** `tests/evidence/test_sanity_pipeline.py::test_isolated_closure_refuses_with_the_distinct_code_before_any_producer` (release lane) monkeypatches `engine.config.registry_loader.load_active_mechanics_bundle` in-process and replaces `closure.subprocess.run` with a failure. A child-process probe (the instruction's example) would break this test, which is outside §6. §5.2 keeps the probe in-process and root-bound, so the test stays green unchanged.
- **F-6 (S12 interacts with three exact-row comparisons).** The updater compares retained Index rows by exact dict equality in `_catalog_validation_entries` (both from `_load_human_index` and from `publish_config_family`), in `_load_crd_qa_entries`, and for first-generation catalog rows in `_config_logical_delta`. A label stored in `notes` must be removed before those comparisons and re-derived afterwards (§5.4). Found by the prototype's first evidence-lane run: 21 config-family tests errored and 3 failed with `CONFIG_CATALOG_REGISTRATION_COLLISION`; after the strip, they pass (§4.3).
- **F-7 (a second allowed-key enforcer).** HDE Schemas & Artifacts §8.3 requires "every serializer or validator enforcing this allowed-key set" to accept `crd_id` and enforce the mutual exclusion before the first CRD enters QA. Besides `check_mirror_schema.sh` there is exactly one such enforcer: the updater's `_ALLOWED_INDEX_FIELDS` / `_normalize_index_entry`, which silently drops `crd_id` (inventory: every `tools/evidence`, `tools/qa`, `ci/checks` and `scripts` file naming `epic_id` was checked for an allowed-key set; `generate_epic031_pr02_log_posture.py`'s `ALLOWED_KEYS` governs log records, not the Mirror). It is in a §6 file and under the same S22 / ID-2 canon basis; §5.6 brings it into conformance (planning decision PD-7).
- **F-8 (two existing tests use HDE-CRD-0002 as the "unadmitted" example).** `test_crd_current_manifest_reconciles_supersession_without_history_conversion` creates `audit/qa/hde-crd-0002/unlisted.log` as a root with "no source-owned admission", and `test_crd_publication_refuses_foreign_scope_and_invalid_inputs` uses `HDE-CRD-0002` as the foreign ID. Once IF-5 admits HDE-CRD-0002 both would fail. Both live in the §6 test home; §6 switches their example to `HDE-CRD-0003` without changing their intent.
- **F-9 (CLI conformance and endpoint catalog are not current-release captures).** The instruction §5.4 cites `epic038.pr02.endpoint_catalog*` and the CLI conformance rows as examples of rows under origin labels. Neither is release-bound: the CLI conformance family (help and install captures, `artifacts/cli/{ab,ba,summary}.json`) is frozen under PR06b §6.4 ("--check" passes with no write on a re-cut), and the endpoint catalog, its audit mirror and their `.sha256` were byte-unchanged by the 1.3.0 re-cut (PR06b §6.3). §5.4 labels neither (planning decision PD-4).

- **F-10 (an existing invariant test pins "no manifest coupling").** `test_manifest_only_release_cut_stays_outside_the_evidence_graph` (§6 test home) cuts only `catalog/manifest.json` and then requires the whole evidence skeleton to be byte-unchanged and every read-only check to pass. With a manifest-derived label (IF-7, D-1: "derived at publication from the admitted manifest, so each later same-version refresh and the `1.4.0` cut relabel rows through the updater alone") the updater's `--check` reports the 28 rows stale until the updater runs. Canon does not state the invariant: HDE Schemas & Artifacts §6.2, §6.2.1 and §6.4 require the manifest to stay the sole release-identity input and outside the Index and Mirror, and both still hold (the label is derived from the manifest; no manifest row enters the graph; the Index and Mirror are not release members, so no cycle forms). The test is adapted, not removed (PD-10): the cutter still writes only the manifest and leaves the skeleton unchanged, the manifest never enters the graph, the historical proof is unchanged, and one updater run relabels exactly the 28 rows (all other row content identical after the label is stripped) before every check passes. Found by the consolidated run (§4.3 R-10).
- **F-11 (an existing config-family test pins the catalog rows' exact shape).** `test_config_family_publication_converges_and_preserves_unrelated_history` (§6 test home) requires each catalog-log Index row to equal its `CATALOG_VALIDATION_ENTRIES` constant. HDE Schemas & Artifacts §8.6.3.2 fixes those rows' retained metadata (`report`, `record_type: catalog_validation`, `schema_version: 1.0`, `epic_id: HDE-EPIC040`) and says "Preserve these artifact keys and existing metadata"; the label preserves every one of them and adds only `notes`. §6.2.1's "Configuration evidence and derived configuration bundles MUST NOT acquire incidental manifest digests, release IDs, or frozen-source identities merely because a release is cut" concerns the configuration evidence bytes and bundles; the two catalog logs already record the release by their owner's design (PR06b §5.4 step 6: "they carry `release_id`"), and the label is S12's purposeful provenance on the Mirror and Index row, which §6.2's identity table allows ("the owning capture's provenance; not another release-identity authority"). The registry report, bundles and thresholds are not labelled. The test is adapted (PD-11): the stripped row equals the constant and the label is present.

### 4.3 Planning rehearsal (inference support, not PR evidence)

Throwaway clone of `b996a20` under the session scratchpad; never the repository checkout. Two interpreters:

- **E-DEB (Debian-patched backend):** `/usr/bin/python3 -m venv --system-site-packages`, CPython 3.13.16; `setuptools` 68.1.2 and `wheel` 0.42.0 import from `/usr/lib/python3/dist-packages` (the Ubuntu-patched backend); `requirements.txt` and `requirements-dev.txt` installed; **no** `-e .`; `_distutils_system_mod` not importable.
- **E-CI (CI-like):** `/usr/bin/python3.12 -m venv`, CPython 3.12.3; `'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e <clone>` (setuptools 84.0.0, pytest 8.4.2).

Rails for every run: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL`, `GH_TOKEN` unset; builder runs under `env -i` with only the rails and `PATH`. No vendor, production or database call occurred.

| Run | What | Outcome |
| :- | :- | :- |
| R-1 | O-10 reproduction at `b996a20` (`git archive` export): the builder's own wheel command (`-m pip wheel --disable-pip-version-check --no-cache-dir --no-index --no-deps --no-build-isolation`) under `/usr/bin/python3` 3.13.16 with `env -i` rails | exit 1; `AttributeError: install_layout. Did you mean: 'install_platlib'?` from `/usr/lib/python3/dist-packages/setuptools/command/install_lib.py` line 17 (§5.1 of the instruction reproduced at this head) |
| R-2 | Same command with the §5.1 shim on `PYTHONPATH`; reference build by `/usr/bin/python3.12` (the distribution interpreter, no shim) | both exit 0; `glow_hdengine-0.0.0-py3-none-any.whl`; 129 entries each, identical names and per-entry SHA-256 (RECORD included); `entry_points.txt` `hdctl = engine.cli.main:cli`. A first shim with only `install_layout` failed on `AttributeError: prefix_option` (F-1) |
| R-3 | S06 "before": full builder at `b996a20`, clean clone, E-DEB, `--output <external empty> --require-clean` | exit 1; stderr `RELEASE_ATTESTATION_FAILED:isolated_package_install_failed`; `failure.json` = `{"code":"isolated_package_install_failed","returncode":1,"schema":"hde.release_attestation.failure.v1","secret_values_recorded":false,"stage":"build_package_wheel"}`; clone clean |
| R-4 | S06 alone (prototype commit 1), same method | exit 1, `{"code":"isolated_stage_failed",…,"stage":"closure_write_and_check"}`; cause reproduced separately: the probe raises `ModuleNotFoundError: No module named 'engine'` when run with the script's `sys.path` and no ambient `engine` (F-4) |
| R-5 | S06 + S13 (prototype commit 2), E-DEB, 16:49:16Z–16:51:44Z | build exit 0, `--verify --require-clean` exit 0; `build.log` carries `build_backend_compat=distribution_install_layout`; `attestation.json` 28,163 bytes, `release_id 52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, 174 files bound, 14 omitted (the counts PR06b recorded); clone clean |
| R-6 | Updater on S12 + S22 + validator (prototype commit 3) | write exit 0; `--check`, `orientation_demo.py --check`, `check_mirror_schema.sh`, `validate_evidence_paths.py`, `check_lf_endings.py`, `check_evidence_index_hash.sh` exit 0; 28 rows on 23 paths labelled in Index and Mirror; Index 163,015 → 166,507 bytes, Mirror 295,881 → 299,373 bytes; `orientation_demo.txt` unchanged; a second write leaves the diff byte-identical |
| R-7 | First lane run on commit 3 (detached worktree, E-CI) | env pins 0; evidence validators 0; **evidence tests 3 failed, 89 passed, 21 errors** (all config-family cases: `CONFIG_CATALOG_REGISTRATION_COLLISION`; F-6); release tests 64 passed; changed tests 196 passed; qa lane 488 passed; tree clean |
| R-8 | Tests added (commit 4) and the F-6 strip (commit 5), PD-7 (commit 6) | new S06/S11/S13 tests with the attestation, engine-core and sanity files: 70 passed; new S22/ID-2/S12 tests: 12 passed; PD-7 test and strip test: 2 passed; S13 negative control: the 4 S13 cases fail against the base probe |
| R-9 | Full builder on commit 4 in both environments | E-DEB build 0, verify 0, compat line present, 174 / 14; E-CI build 0, verify 0, no compat line, 174 / 14; both clones clean |
| R-10 | Consolidated validation on prototype commit 6 (`f64f1e8bcf9793e7e248f2aff02564b33d66f9f5`), E-CI, detached worktree, 17:09:39Z–17:31:20Z | env pins 0; `check_agents_md_citations.py` 0; `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`, `check_lf_endings.py`, `release_id_recompute.py --check-manifest-only` all 0; updater written twice, `git diff --exit-code` 0; classifier `lanes=evidence,release`, 15 paths, 5 changed-test targets; changed tests **198 passed**; evidence lane **2 failed, 124 passed** (F-10, F-11); config + engine-core files 165 passed; release lane tests **75 passed**; qa lane **488 passed**; tree clean. Attestation from a clean clone: E-DEB build 0, verify 0, compat line present, 28,163 bytes, SHA-256 `5bad80ed…`, `source_commit f64f1e8…`, `release_id 52be4558…`, PASS, `PR06R_B_FINAL_PASS`, 174 / 14; E-CI build 0, verify 0, no compat line, SHA-256 `5cd3344a…`, same identity and counts; both clones clean |
| R-11 | PD-10 and PD-11 applied (commit 7, `7fe9de6d5526fe1384ad97ddefcbbca7f690912d`; differs from commit 6 only in `tests/evidence/test_evidence_index_missing_state.py`, +15 / −2), E-CI, detached worktree | 17:26:36Z–17:41:55Z: evidence lane test set **126 passed** (the two F-10/F-11 tests included); `tests/config/test_config_artifacts.py`, `tests/evidence/test_engine_core_evidence.py` and the four release-lane test files **240 passed**; tree clean. The source and governed-companion bytes are those of commit 6, so R-10's validators, classifier, changed-test, qa-lane and attestation results carry over |

### 4.4 Prototype companion

`docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff` is the prototype's diff from `b996a20` restricted to the seven source and test files of §6 (governed companions excluded: PR-30 regenerates them with the updater). It is a planning record of a design that passed §4.3; PR-30 may apply it as its starting point, but owns the implementation, re-reads every hunk against this plan, and re-runs §11 on the real branch. Where the diff and this plan differ, this plan governs and the difference is a defect to correct in PR-30. Known differences: the two parametrized S06 and S13 tests in the diff lack the readable `ids=` that §8.1 and §8.2 require.

## 5. Design

### 5.1 S06 — wheel stage under a distribution-patched setuptools (`tools/evidence/build_release_attestation.py`)

**Decision PD-1.** When, and only when, the interpreter running the builder imports a distribution-patched setuptools and lacks the distribution's `_distutils_system_mod`, the wheel stage puts a builder-owned `_distutils_system_mod` module on the wheel child's `PYTHONPATH`. That module adds the two options the patch reads, `install_layout` and `prefix_option`, to the distutils `install` command with the neutral default `None`, which is the value under which the patched code takes its ordinary, non-Debian branch. The patched setuptools stays the build backend; nothing is downloaded, swapped or seeded.

Concrete shape (prototype, §4.4):

- New module-level `import importlib.util`.
- Constants `_DISTUTILS_SYSTEM_MOD = "_distutils_system_mod"`, `_DISTRIBUTION_LAYOUT_MARKER = "install_layout"`, and `_BUILD_BACKEND_COMPAT_SOURCE`, the module text: a subclass of `distutils.command.install.install` whose `initialize_options` calls the parent and sets `self.install_layout = None` and `self.prefix_option = None`, then `distutils.command.install.install = install`. A comment above the constants states the Debian/Ubuntu cause in two sentences.
- `_distribution_layout_compat_required() -> bool`: `False` when `importlib.util.find_spec("_distutils_system_mod")` is not `None` (the distribution interpreter supplies the options itself; never shadow it); otherwise locate the top-level `setuptools` spec without importing it (`find_spec("setuptools")`), read `<origin dir>/command/install_lib.py`, and return whether it contains `install_layout`. A missing setuptools or an unreadable file returns `False` (the build then fails exactly as today, with its existing receipt).
- `_wheel_build_env(install_root) -> tuple[dict[str, str], bool]`: returns `_clean_child_env()` and `False`, or writes `install_root / "build-backend-compat" / "_distutils_system_mod.py"` and returns `_clean_child_env()` plus `PYTHONPATH=<that directory>` and `True`.
- `_install_packaged_console_entrypoint` uses that environment for the `pip wheel` call only. The venv creation and `pip install` calls keep `_clean_child_env()` unchanged.
- Transcript: when applied, the wheel stage adds `build_backend_compat=distribution_install_layout` after `source=tracked_source_copy`. `stage=build_packaged_wheel` stays first. With the compat not applied (hosted CI), `build.log` is byte-identical to today's.

Guarantees kept (instruction §6, §11): `_clean_child_env` is unchanged and still excludes `PYTHONPATH` (its existing test stays as is); `_require_exact_source_copy`, the two exact copies, `--no-index`, `--no-deps`, `--no-build-isolation`, `--no-cache-dir`, the fixed-point stages, the output contract, `--require-clean` and the failure receipts are unchanged. The shim lives under the temporary isolated root, outside both source copies, so the exact-source snapshots are unaffected. It is written by the builder from a constant; nothing comes from the network or the caller's environment.

**Why this design.** F-2 rules out seeding an upstream backend offline; building the wheel without setuptools would re-implement a build backend; build isolation needs the network; retry-on-failure is nondeterministic. The gate in `_distribution_layout_compat_required` exists because of F-3. Equivalence: the wheel built by the 3.13 interpreter with the shim and the wheel built by the distribution's own Python 3.12 from the same source have identical member lists and per-member SHA-256 (129 of 129 entries, RECORD included; §4.3 R-2).

**Acceptance reading (instruction §10 (1)).** Before: the full builder at the PR base in E-DEB returns `isolated_package_install_failed` at `build_package_wheel`. After: the full builder at the PR head in E-DEB exits 0 with the patched backend and `--verify --require-clean` exits 0. Hosted CI's release lane still builds and verifies (PR-35).

### 5.2 S13 — root-bound closure admission probe (`tools/evidence/regenerate_identity_closure.py`)

**Decision PD-2.** The probe stays in-process (F-5) and is bound to the closure's own root:

- `_is_within_root(origin) -> bool`: the resolved file path lies under `ROOT.resolve()`.
- `_isolated_admission_owner()`: if `engine` is not yet imported and `sys.path[0]` is not `str(ROOT)`, insert `str(ROOT)` at `sys.path[0]` (a regular path entry first in `sys.path` precedes site-packages, `.pth` paths and the setuptools editable finder, which is appended to `sys.meta_path`); import `engine.config.registry_loader`; require that `engine`, `engine.config` and `engine.config.registry_loader` all have `__file__` inside `ROOT`; otherwise `raise SystemExit("IDENTITY_CLOSURE:ADMISSION_PROBE_NOT_ROOT_BOUND")`.
- `release_not_admitted_observed()` calls the owner through that module object (`loader.load_active_mechanics_bundle()`, `except loader.SchemaValidationError`), so in-process monkeypatches on the module still apply and the refusal semantics are unchanged: `True` only for `INCOMPLETE_RELEASE_ROSTER`.

Truthfulness (instruction §9.2): a missing ambient package is no longer a failure (the copy is first on the path); an ambient package from elsewhere never decides admission (either the copy wins, or, if `engine` was already imported from outside the root, the probe stops with an ordinary failure that is never the distinct exit code 3). The probe widens nothing.

Consumers kept: the closure step lists, `test_internal_version_manifest_captures.py`, `test_aux_preview_identity_parity.py`, the K-2 assertion at `test_release_attestation.py` lines 614–617, and `test_sanity_pipeline.py`'s in-process monkeypatch test (F-5), all unchanged and green in the prototype.

### 5.3 S11 — engine-core currency (`tests/evidence/test_engine_core_evidence.py`, test-only)

**Decision PD-3.** Add, after the path constants:
- `RELEASE_ID_CARRIERS = ("engine_core_two_run_logs", "engine_core_abba_logs", "engine_core_json_compare_logs")`;
- `_nested_release_ids(value)`: a recursive walk over dicts and lists collecting every value whose key is `release_id`;
- `_assert_payload_release_ids_are_admitted()`: reads `engine.runtime.identity.identity_meta()["release_id"]` at call time; each carrier payload has at least one `release_id` and every one equals the admitted value (message "… release_id drifted from the admitted release"); the purity report has none (its absence is asserted and recorded, not "fixed" — instruction §9.3).
- `test_core_evidence_binds_the_admitted_release_id` (positive) and `test_core_evidence_release_check_fails_when_the_admitted_release_id_differs` (monkeypatches `identity.identity_meta` to return `release_id = "0" * 64` and expects `AssertionError` matching "drifted from the admitted release").

`tools/evidence/generate_engine_core_evidence.py` and the four payloads are unchanged.

### 5.4 S12 — current-release labels in the Machine Mirror (`tools/evidence/update_evidence_index.py`)

**Encoding (ID-1), decision PD-4.** The label lives in `notes`, inside HDE Schemas & Artifacts §8.3's allowed key set. Exact text:

`current-release capture: release <version>, release_id <64 lowercase hex>`

appended to a row's existing notes with `"; "`, or as the whole of `notes` when the row has none. `artifact_key`, `epic_id`, `record_type`, `role`, `schema_version` and `tokens` are untouched, so origin identity and type labels stay (EC-5 "origin keys stay"); no new top-level key; no Mirror schema change; no schema companion; no canon edit. `notes` is the free-form, names-only commentary key; the label carries only a version name and a release digest, no secret or payload value.

Why `notes`, not `record_type`: 18 of the 28 rows already carry an origin `record_type` (for example `catalog_validation`, `writer_log`, `epic038_pr02_predicate_evidence`; 4 also carry origin `notes` and 16 an `epic_id`), and overwriting it would destroy a type label the updater's own reconcilers compare exactly (F-6). A suffix on `notes` is reversible by an exact pattern, which is what makes relabelling through the updater alone possible (D-1).

**Derivation.** `_current_release_label()` reads `ROOT/catalog/manifest.json`, requires its bytes to equal `engine.serializer.canon.sercanon(manifest, sort_keys=True)` and its `version` to be a string with no whitespace, comma or semicolon, and returns the text above with `release_id = sha256(manifest bytes)` (the `AGENTS.md` formula; for canonical bytes it equals the admitted `identity_meta()["release_id"]`). Any other state raises `SystemExit("CURRENT_RELEASE_LABEL_MANIFEST_INVALID")`. It is evaluated at every updater run, so a same-version refresh (WU-PR-03/04/05) or the `1.4.0` cut (WU-PR-08) relabels at step 5 of Plan §10 with no other change.

**Mechanics.**
- `_CURRENT_RELEASE_LABEL_RE = re.compile(r"(?:^|; )current-release capture: release [^\s,;]+, release_id [0-9a-f]{64}$")`; new module-level `import re`.
- `_strip_current_release_label(entry)`: removes the trailing label from `notes` (and the `notes` key if nothing remains); non-dict entries and rows without a label are returned unchanged.
- `_apply_current_release_label(entries)`: appends the label to every entry whose `discovered_physical_path` is in `CURRENT_RELEASE_CAPTURE_PATHS`.
- `_load_human_index()`: strips every retained row immediately after the strict load, before `_catalog_validation_entries` and `_load_crd_qa_entries`, and applies the label to the deduplicated result. Index and Mirror therefore carry identical notes (1:1 parity), and a stale label from an earlier release is replaced, never duplicated.
- `_catalog_validation_entries` compares `_strip_current_release_label(dict(row))` with the expected constant row (it is also called from `publish_config_family` on raw rows); `_config_logical_delta` compares stripped rows for first-generation catalog records (Index and Mirror). Existing-row drift detection is unchanged: a label changes only when the manifest changes, which happens at Plan §10 step 2 before the updater (step 5) and the config family (step 6).

**Family list, decision PD-4 (instruction §9.4; D-1).** Criterion: a tracked primary is a current-release capture when its bytes are produced from the admitted release by a current owner and changed with `release_id` in the measured 1.2.x → 1.3.0 re-cut (PR06b §3.3 and §6.3: 23 primaries, "the 25 path-proof siblings of the above" minus the Mirror and its checksum). `CURRENT_RELEASE_CAPTURE_PATHS` is that explicit set; no discovery:

| Owner family (Plan §10 step) | Paths | Rows |
| :- | :- | :- |
| Canonical JSON gate (4) | `audit/gates/canonical_json/json_canon_compare.log`, `audit/gates/canonical_json/json_canonical_check.log`, `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` | 6 (the two `.ndjson` files are registered under an HDE-EPIC024 key and an HDE-EPIC039 key each) |
| Config family (6) | `artifacts/catalog/catalog_schema_validation.log`, `artifacts/catalog/domain_closure_report.log` | 2 |
| A7 (7) | `artifacts/proofs/reader_success_get_head_304.json`, `success_304.txt`, `success_encoding_invariance.txt`, `success_get.txt`, `success_head.txt` | 8 |
| Determinism (7) | `audit/gates/parity/reader_cli/ab.json`, `ba.json`, `summary.json`, `audit/gates/determinism/abba.bytes`, `audit/gates/determinism/tworun_identity.sha256` | 5 |
| Open-rails fixture proof (7) | `audit/gates/determinism/open_rails_abba.json` | 1 |
| F07 writer (7) | `artifacts/writer/conjunction_write_readback.log`, `artifacts/writer/conjunction_writer_summary.json` | 2 |
| Engine-core (7b) | `artifacts/core/two_run/identity.json`, `abba/ab_ba_parity.json`, `json_compare/core_result_json_compare.json`, `purity/purity_report.json` | 4 |
| **Total** | **23 paths** | **28 rows** |

Not labelled, and why: the frozen families of PR06b §6.4 (`artifacts/cli/showcompat/*`, `artifacts/cli/{ab,ba,summary}.json`, help and install captures, `artifacts/identity/*`, `artifacts/math/*`, `artifacts/parity/two_run_identity.log`, `artifacts/bodygraph/release_bindings.json`, `artifacts/runtime/env_matrix.snapshot.json`, `artifacts/vendor/*`, `audit/ops/*`, EPIC032 router captures, the §2.21 captures) keep their capture-time labels; release-independent current files (the endpoint catalog and its mirror, `endpoints_snapshot.json`, `success_writers_errors.txt`, `json_gate_structured_record.json`, the registry report, config bundles and thresholds; F-9) carry no release binding; QA logs that quote a `release_id` (for example under `audit/qa/hde-epic040/`) are QA evidence of their own capture and are not current-release captures. `AGENTS.md` keeps the registry report free of release identity; this plan does not associate it with one.

**S12 invariant.** With the label, "a reader of the Mirror can tell a current-release capture from a frozen one without opening the file" (Audit §6 S12): current-release rows end with the label naming the release; no other row contains `current-release capture:`.

### 5.5 S22 — admitted-CRD table (IF-5) in the updater

**Decision PD-5.**
- Replace `CRD_QA_ID`, `CRD_QA_ROOT_REL`, `CRD_QA_KEY` (used only inside the updater; checked by search) with `ADMITTED_CRD_QA: Mapping[str, tuple[str, str]] = {"HDE-CRD-0001": ("audit/qa/hde-crd-0001", "audit.qa.hde_crd_0001"), "HDE-CRD-0002": ("audit/qa/hde-crd-0002", "audit.qa.hde_crd_0002")}`, with a comment that this is a source-owned admission table, not a check roster or discovery rule, and that another CRD needs its own row.
- `_crd_qa_entry(crd_id, check_id=None)` builds the existing row shape (`artifact_key`, `discovered_physical_path`, `role`) from the table.
- `_load_crd_qa_entries(retained)`: for each retained row, the set of admitted CRDs it claims by key prefix or by normalized path; no claim → unrelated (unchanged); more than one claim → `ValueError("CRD index row has foreign or contradictory key/path/metadata")`; one claim → the existing per-row checks against that CRD's root. Then, for each admitted ID in sorted order, an absent root with no retained rows publishes nothing; otherwise `qa_harness.validate_crd_check_family` and the rows are generated as today.
- `publish_crd_check_family`: refuses any config whose `crd_id` is not in the table with `ValueError("governed CRD publication admits only HDE-CRD-0001, HDE-CRD-0002; refused <ID>")`, and refuses a config whose `qa_root` differs from `ROOT / <admitted root>`. Everything else (repository-root check, outer transaction, prior-state `--check`, rollback) is unchanged. WU-PR-07 extends this table model and adds no second admission mechanism (D-2).
- HDE-CRD-0002 rows keep the existing CRD row shape; no `crd_id` is added to any row; HDE-CRD-0001 rows are not migrated; `audit/qa/hde-crd-0002/` is not created.

### 5.6 S22 / ID-2 — `crd_id` acceptance in both allowed-key enforcers

**Decision PD-6 (validator, `ci/checks/check_mirror_schema.sh`).** Add `"crd_id"` to `OPTIONAL_KEYS`; after the `KEYS_EXTRA` check, a record carrying both `epic_id` and `crd_id` prints `EPIC_CRD_EXCLUSIVE:<line>` to stderr and fails. Nothing else changes; every existing record still validates.

**Decision PD-7 (serializer, `_ALLOWED_INDEX_FIELDS` / `_normalize_index_entry`; F-7).** Add `"crd_id"` to `_ALLOWED_INDEX_FIELDS` and, before normalization, refuse an entry carrying both `epic_id` and `crd_id` with `ValueError("Index entry carries both epic_id and crd_id: <key>")`. No current row carries `crd_id`, so the Index and Mirror bytes do not change from this decision (prototype: `--check` exit 0 before and after). This is the same canon clause as ID-2 applied to the second enforcer that clause names; it adds no file to §6 and no row field. It is recorded for the IA's PR-40 review.


## 6. Change set

| Path | Change | Requirement |
| :- | :- | :- |
| `tools/evidence/build_release_attestation.py` | §5.1 (prototype +54 / −1 lines) | S06 |
| `tools/evidence/regenerate_identity_closure.py` | §5.2 (prototype +29 / −4) | S13 |
| `tools/evidence/update_evidence_index.py` | §5.4, §5.5, §5.6 PD-7, PD-9 (prototype +135 / −28) | S12, S22 |
| `ci/checks/check_mirror_schema.sh` | §5.6 PD-6 (prototype +5) | S22 / ID-2 |
| `tests/evidence/test_release_attestation.py` | §8.1, §8.2 | S06, S13 |
| `tests/evidence/test_engine_core_evidence.py` | §8.3 | S11 |
| `tests/evidence/test_evidence_index_missing_state.py` | §8.4, §8.5; F-8 switches `HDE-CRD-0002` to `HDE-CRD-0003` in two existing tests; F-10 and F-11 adapt two existing tests to the label (PD-10, PD-11) | S12, S22 |
| `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256` and their four `.path_proof.txt` companions | regenerated by the updater only (the 28 labelled rows) | S12 |
| `audit/gates/topology/orientation_demo.txt` | not expected to change (row counts are unchanged; prototype: unchanged); regenerated only by the updater if it does | — |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md` (PR-30) and its successors (PR-35) | PR result records | evidence obligation |

Unchanged, by design and by measurement in the prototype: `tools/evidence/generate_engine_core_evidence.py`, `tools/qa/qa_harness.py`, `ci/checks/classify_ci_changes.py` (no owner registration is needed: every new test lives in an already registered owner file; the classifier dry run reports no `CI_EVIDENCE_OWNER_TEST_MISSING`), `tests/evidence/test_sanity_pipeline.py`, `catalog/manifest.json`, every release member, every governed primary, `AGENTS.md`, `README.md`, `docs/EVIDENCE_INDEX.md`, `docs/pfcanon/**`.

## 7. Implementation sequence (PR-30, after the Product Owner's Proceed for this version)

C0 — **Recover first.** Inspect local roots, worktrees, branches, open PRs and `docs/ephemeral/HDE-CRD-0002-WU-PR-02-*` for existing WU-PR-02 work; resume the most advanced consistent state. Confirm `origin/main` still has `b996a20` as an ancestor and that `git diff b996a20 origin/main` touches none of the §6 paths, `catalog/manifest.json` or any §5.4 roster primary; if it does, re-measure §4 facts that depend on it and record the difference (a changed roster primary or manifest is not a finding by itself: the label derives from the manifest at run time).

C1 — **Environments.** E-CI and E-DEB exactly as §4.3. Readiness in E-CI: `python -m pip install -r requirements-dev.txt`, then `python -m pytest --version`. Record interpreter versions, setuptools origin and `importlib.util.find_spec("_distutils_system_mod")` for both.

C2 — **S06 "before".** From a clean clone detached at the PR base, in E-DEB: `env -i <rails> PATH=<E-DEB bin>:/usr/bin:/bin <E-DEB python> tools/evidence/build_release_attestation.py --output <external empty dir> --require-clean`; record exit 1, `RELEASE_ATTESTATION_FAILED:isolated_package_install_failed`, the receipt `{"code":"isolated_package_install_failed",…,"stage":"build_package_wheel"}` and a clean clone.

C3 — **Source edits** in this order: `regenerate_identity_closure.py` (§5.2), `build_release_attestation.py` (§5.1), `check_mirror_schema.sh` (§5.6), `update_evidence_index.py` (§5.5, §5.6 PD-7, then §5.4).

C4 — **Governed regeneration.** `python tools/evidence/update_evidence_index.py` (write), then a second write run (byte-stable), then every read-only validator (§11 step 4). Expected change: exactly the eight companions of §6, with 28 rows labelled in both the Index and the Mirror.

C5 — **Tests** (§8): add and adjust in the three test homes.

C6 — **Local validation** (§11). Fix and re-run until clean; never skip, deselect, `xfail` or quarantine a test.

C7 — **Commit.** One coherent commit with the source, test and governed-companion changes, message scope naming the work unit (for example `fix(evidence): HDE-CRD-0002 WU-PR-02 — attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (S06, S11, S12, S13, S22)`).

C8 — **S06 "after" and the release-lane rehearsal** on the committed head (§11 steps 9–10).

C9 — **Record and publish.** Write `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md` (§12), commit it, push, open one pull request with the `.github/pull_request_template.md` headings filled under `AGENTS.md` "PR descriptions", read the result back, and return `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

## 8. Test design

### 8.1 S06 (`tests/evidence/test_release_attestation.py`)

- `test_wheel_layout_compat_is_required_only_for_a_distribution_patched_backend` — parametrized over four cases with `builder.importlib.util.find_spec` monkeypatched and a fake `setuptools/command/install_lib.py` under `tmp_path`: system module present → `False`; absent + patched marker → `True`; absent + unpatched file → `False`; no setuptools → `False`. Use readable `ids=`.
- `test_wheel_build_env_adds_only_the_builder_owned_compat_path` — with a caller `PYTHONPATH` set: not required → env equals `_clean_child_env()` and no directory is created; required → env equals `_clean_child_env()` plus `PYTHONPATH` pointing at `build-backend-compat`, which holds only `_distutils_system_mod.py`, and the text compiles.
- `test_wheel_layout_compat_supplies_neutral_install_options` — a child `sys.executable -c` with the returned env imports setuptools and the shim, instantiates `distutils.command.install.install` and asserts `install_layout is None` and `prefix_option is None`.
- `test_wheel_stage_records_and_scopes_the_layout_compat` — fake `subprocess.run` as in the existing console-entrypoint test: only the wheel call carries `PYTHONPATH`; the transcript starts `stage=build_packaged_wheel`, `source=tracked_source_copy`, `build_backend_compat=distribution_install_layout`; `package_source` stays empty.
- Unchanged and still green: `test_child_environment_is_closed_and_drops_sensitive_values`, `test_isolated_console_entrypoint_is_installed_from_tracked_package`.

### 8.2 S13 (`tests/evidence/test_release_attestation.py`)

A stub isolated copy under `tmp_path`: the real `tools/evidence/regenerate_identity_closure.py` bytes plus a stub `engine/config/registry_loader.py` defining `SchemaValidationError(code)` and `load_active_mechanics_bundle` that either refuses with `INCOMPLETE_RELEASE_ROSTER` or admits.
- `test_closure_probe_follows_the_isolated_copy_with_no_ambient_engine` — `sys.executable -I -S <copy script> --in-place-isolated` from a neutral directory, env `PATH` and `HDE_ISOLATED_RELEASE_BUILD=1` only: no site-packages, no `PYTHONPATH`, no script directory, so no ambient `engine` is importable; exit 3 and stdout exactly `IDENTITY_CLOSURE:RELEASE_NOT_ADMITTED\n` (acceptance (2)).
- `test_closure_probe_ignores_a_different_ambient_engine` — two cases with an ambient stub package on `PYTHONPATH` that answers the opposite way (copy refuses / ambient admits → `True`; copy admits / ambient refuses → `False`), via `python -S -c` and `runpy.run_path`. Use readable `ids=`.
- `test_closure_probe_fails_closed_when_engine_was_imported_from_elsewhere` — the ambient `engine.config.registry_loader` imported first; nonzero exit and `IDENTITY_CLOSURE:ADMISSION_PROBE_NOT_ROOT_BOUND` on stderr.
- Negative control (recorded in the result): with the base probe restored, all four S13 cases fail; with the change, they pass.

### 8.3 S11 (`tests/evidence/test_engine_core_evidence.py`)

As §5.3: the positive test and the monkeypatched negative test (acceptance (3)).

### 8.4 S22 (`tests/evidence/test_evidence_index_missing_state.py`)

- F-8 edits: `audit/qa/hde-crd-0002` → `audit/qa/hde-crd-0003` (two lines) in `test_crd_current_manifest_reconciles_supersession_without_history_conversion`; `HDE-CRD-0002` → `HDE-CRD-0003` in `test_crd_publication_refuses_foreign_scope_and_invalid_inputs`.
- `test_admitted_crd_table_is_explicit_and_matches_the_harness_roots` — the table equals IF-5 exactly; each root equals `HarnessConfig(crd_id=…).qa_root`.
- `test_absent_admitted_crd_root_publishes_nothing` — on the real checkout, `audit/qa/hde-crd-0002/` is absent, `_load_crd_qa_entries([])` yields no HDE-CRD-0002 row and the Index has none.
- `test_crd_0002_fixture_root_publishes_beside_crd_0001` — in `crd_repo`, publish HDE-CRD-0002 then HDE-CRD-0001; both families validate; each has exactly its manifest and check rows in the existing shape (`artifact_key`, `discovered_physical_path`, `role`); no Mirror row under `audit/qa/hde-crd-*` carries `tokens`, `epic_id` or `crd_id`; `_checks` passes; republishing is byte-stable.
- `test_crd_publication_refuses_an_unadmitted_id_by_name` — HDE-CRD-0003 fails with "admits only HDE-CRD-0001, HDE-CRD-0002; refused HDE-CRD-0003" and the whole tree, metadata included, is unchanged.
- `test_crd_index_admission_rejects_cross_crd_rows` — a row whose key claims HDE-CRD-0002 and path HDE-CRD-0001, and the reverse, is refused before any write.
- Existing forgery, rollback and incoherent-prior-state cases stay unchanged and green.

### 8.5 ID-2 and S12 (`tests/evidence/test_evidence_index_missing_state.py`)

- `test_mirror_schema_accepts_crd_id_and_refuses_epic_and_crd_together` — a minimal synthetic Mirror (one record, its proof, a correct self-record and mirror proof) under `tmp_path`, run with `check_mirror_schema.sh` as cwd-relative validator: `crd_id` only → 0; `epic_id` only → 0; both → 1 with `EPIC_CRD_EXCLUSIVE`. The real Mirror still passes through `_checks` and the evidence lane.
- `test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together` — PD-7.
- `test_current_release_capture_rows_are_labeled_and_frozen_rows_are_not` — on the real Mirror and Index: every row for a roster path ends with the label computed from `catalog/manifest.json`; no other row contains `current-release capture:`; every roster path has at least one row; Index and Mirror notes agree; rows under `artifacts/identity/`, `artifacts/math/`, `artifacts/cli/showcompat/`, `artifacts/vendor/` and `audit/ops/` exist and carry no label (acceptance (4), "frozen families unchanged").
- `test_release_label_strip_preserves_origin_notes` — strip on origin + label, label only, and origin only.
- PD-10, `test_manifest_only_release_cut_stays_outside_the_evidence_graph`: keep every existing assertion up to the cut (manifest changed, historical proof unchanged, skeleton unchanged, no manifest row); replace the final `_checks` and skeleton-equality pair with: run the updater once; every Index row equals its pre-run row after `_strip_current_release_label`; every roster row ends with `current-release capture: release 1.0.1, release_id <sha256 of the cut manifest>`; still no `catalog/manifest.json` row; `_checks` passes; the historical proof is unchanged.
- PD-11, `test_config_family_publication_converges_and_preserves_unrelated_history`: `assert selected == [entry]` becomes the stripped comparison plus an assertion that the row's `notes` starts with `current-release capture: release `.
- `test_release_labels_follow_the_manifest_through_the_updater_alone` — in a repository copy, run the updater with `_current_release_label` replaced by a `9.9.9` / `b`×64 label: every labelled row ends with the new label exactly once; then the real updater restores `INDEX.json` byte for byte and `_checks` passes (D-1).

## 9. Requirement → change → test map

| Requirement / acceptance | Change | Proof |
| :- | :- | :- |
| S06 / (1) | §5.1 | C2 before receipt; §11 step 10 after (E-DEB build 0, verify 0); §8.1 four tests; hosted release lane (PR-35) |
| S13 / (2) | §5.2 | §8.2 four tests and their negative control; release lane tests; E-DEB full build (closure stages pass with no ambient `engine`) |
| S11 / (3) | §5.3 | §8.3 positive and monkeypatched negative |
| S12 / (4) | §5.4 | §8.5 label tests; regenerated Index/Mirror; `check_mirror_schema.sh`, `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_evidence_index_hash.sh` exit 0 |
| S22 / (5) | §5.5, §5.6 | §8.4 publication cases; §8.5 validator and normalizer cases |
| CD-3 | §5.5 | as S22 |
| Interface D-1 to D-5 | §10 | as listed there |

## 10. PR split, merge dependencies and downstream contracts

One pull request, one work unit, one coherent implementation commit plus the result record. No split: every change is small, they share the release and evidence lanes, and S06's acceptance needs S13 (F-4).

- **Merge order.** After WU-PR-01 (merged); before WU-PR-03 (whose same-version refresh will relabel through this model) and before WU-PR-07 (which extends the same updater). Nathan merges.
- **D-1 Label model before re-cuts** (WU-PR-03, -04, -05, -08): the label derives from `catalog/manifest.json` at every updater run, so Plan §10 step 5 relabels the 28 rows with no other change. The roster is the measured set of §5.4; if a later re-cut changes the bytes of a primary outside the roster, or leaves a roster primary byte-stable across a `release_id` change, that unit records it as a finding to the IA rather than editing the roster on its own.
- **D-2 CRD admission table** (WU-PR-07; QA-10): IF-5 table; unlisted IDs refused by name; an absent `audit/qa/hde-crd-0002/` publishes nothing; WU-PR-07 adds its close-run family to this model, not a second mechanism.
- **D-3 Validator conformance** (QA-10 and later QA evidence): `check_mirror_schema.sh` and the updater's normalizer accept `crd_id` with the mutual exclusion; HDE-CRD-0002 QA rows use the existing CRD row shape.
- **D-4 Attestation in the release lane** (every later unit): the release lane still builds and verifies on hosted CI (compat inactive there, `build.log` unchanged); the closure keeps its test selections.
- **D-5 No member change**: `catalog/manifest.json` and `release_id` untouched.

## 11. Validation plan (PR-30, local)

All under the §4.3 rails; every run that can write tracked files runs in a detached worktree or throwaway copy and ends with `git diff --exit-code` and an empty `git status --short --untracked-files=all` (OBS-4's 11 same-byte rewrites are the only accepted rewrite and leave no diff).

1. `ci/checks/check_env_pins.sh` exit 0; `python3 ci/checks/check_agents_md_citations.py` exit 0.
2. Readiness (C1) and the S06 "before" receipt (C2).
3. Updater write twice; the second leaves no diff.
4. Read-only validators, each exit 0: `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/refresh_step_logs_manifest.py --check`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_final_lf.sh`; `python tools/evidence/check_lf_endings.py`; `python scripts/release_id_recompute.py --check-manifest-only`.
5. Classifier dry run on the committed candidate: `python ci/checks/classify_ci_changes.py --base <full base SHA> --head <full head SHA> --event-name pull_request --github-output <file> --changed-tests-output <file>`; expected `lanes=evidence,release`, `changed_tests=true`, no unclassified path, no missing owner (prototype at `f64f1e8`: exactly this, 15 paths, five changed-test targets: `tests/config/test_config_artifacts.py`, `tests/evidence/test_aux_preview_identity_parity.py`, `tests/evidence/test_engine_core_evidence.py`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/evidence/test_internal_version_manifest_captures.py`).
6. Changed-test step as `ci.yml` runs it (detached worktree, `PYTHONPATH` = worktree) over the classifier's targets.
7. Evidence lane as `ci.yml` runs it: the step-4 validators plus `pytest` over `tests/evidence/test_evidence_index_missing_state.py`, `tests/evidence/test_evidence_skeleton.py`, `tests/evidence/test_machine_mirror_self_proof.py`, `tests/evidence/test_orientation_demo.py`, `tests/ops/test_evidence_index.py`, `tests/qa/test_epic020_qa_docs.py`; plus `tests/config/test_config_artifacts.py` (updater owner) and `tests/evidence/test_engine_core_evidence.py`.
8. Release lane tests in a detached worktree: `tests/runtime/test_identity.py`, `tests/evidence/test_release_attestation.py`, `tests/evidence/test_release_manifest_content_binding.py`, `tests/evidence/test_sanity_pipeline.py`.
9. Release lane build in E-CI from a clean clone of the committed head: `build_release_attestation.py --output <external empty dir> --require-clean` exit 0, then `--verify <dir> --require-clean` exit 0; `build.log` has no `build_backend_compat` line; clean tree.
10. S06 "after" in E-DEB from a clean clone of the committed head: build exit 0 with `build_backend_compat=distribution_install_layout` in `build.log`, `--verify --require-clean` exit 0, clean clone; record the attestation size, SHA-256, `source_commit`, `release_id`, bound and omitted file counts.
11. Prudence: the qa lane's seven test files in a detached worktree (`publish_crd_check_family` is used by the generic harness); a failure of `tests/qa/test_generate_epic_close_pack.py` is recorded as OBS-17 and not "fixed" here.
12. Negative controls: S13 tests against the base probe fail (§8.2); S11's negative test passes only because it expects the failure.

## 12. Acceptance and evidence obligations

The PR result record (`docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md`) records: every check run in §11 with counts and exit codes; the before/after O-10 receipts with E-DEB's exact description (interpreter, setuptools origin and package version, absence of `_distutils_system_mod`, no `-e .`); the S12 family list (§5.4 table) and encoding (PD-4) and the labelled-row count; the diff stat of the governed companions; the classifier output; the tested commit versus the later record commit; the In-flight decisions table; nonclaims. Evidence obligations (Plan): the PR result record and the regenerated governed companions in the PR; no new evidence family. Nonclaims: no QA evidence for HDE-CRD-0002 (admission readiness only), no QA verdict, acceptance, PF09/PF30 movement, deployment, canon change or closure; CI green is not QA.

## 13. Security and migration constraints

- **Security.** The attestation keeps its exact-source binding, clean child environment, `--no-index`, `--no-deps` and `--require-clean` refusal; the only addition to any child environment is `PYTHONPATH` naming a builder-written directory inside the temporary isolated root, for the wheel child only, and only when the distribution patch is detected; nothing comes from the network or from the caller's environment. The closure probe never lets code outside the isolated copy decide admission. The Mirror validator and the Index normalizer widen only to the canon-allowed `crd_id` and add the mutual-exclusion refusal. No secret, token or key value appears in tests, logs, labels or records; labels carry a version name and a digest only. PF10 addendum 2.3: the Codex code review is in the chain; no Codex security review is obtained or waited on.
- **Migration.** None: no data, schema, catalog or member change. Rollback is Nathan's revert of the squash commit, followed by the updater regenerating Index/Mirror from the reverted model (the labels disappear); no manifest refresh.

## 14. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| R-1 | A Mirror or Index consumer rejects or compares the new `notes` text (Plan v1.1 §11 "Mirror consumers rejecting added fields"). | F-6 found and fixed the three in-updater comparisons; §11 runs every read-only validator and the evidence, release, changed-test and qa lane sets. A failure outside §6 is routed (§16), not absorbed. |
| R-2 | The E-DEB rehearsal environment differs on PR-30's host (no `/usr/bin/python3` 3.13, or a different patched setuptools). | C1 records the environment; if no non-distribution interpreter importing a patched setuptools exists, record "S06 after not reproducible here" with the reason, keep the unit tests, and report it to Nathan as an access constraint; never claim the rehearsal. |
| R-3 | Hosted CI's runner (`ubuntu-latest`, `actions/setup-python`) changes setuptools so that the compat is detected there. | The gate reads the importable setuptools' own source; a detected patch on CI would add one transcript line and still build. PR-35 reads `build.log` facts from the lane if exposed; no action unless the lane fails. |
| R-4 | A concurrent change to `catalog/manifest.json` or a roster primary lands on `main` before merge. | The label is derived at run time; C0 re-checks; PR-35 merges `main` and reruns the updater if the Index changes. |
| R-5 | OBS-17 (`tests/qa/test_generate_epic_close_pack.py` intermittent on hosted qa lane). | The qa lane is not selected for this PR (classifier); if it runs and fails, record OBS-17; never patch it here. |

Recovery: interruption resumes in the same dedicated PR-30 session from its last saved artifact; inspect worktrees, branches, PRs and `docs/ephemeral/` first. A defect in this plan before Proceed returns to this PR-20 context for a v1.1 successor. Abort is only Nathan's manual PR-50 instruction.

## 15. In-flight planning decisions

| ID | Decision | Why it is within the approved scope | Proven by (prototype) |
| :- | :- | :- | :- |
| PD-1 | S06 compat shim, gated on the distribution patch | §9.1 leaves the design to PR-20; F-2, F-3 | wheel equivalence 129/129; E-DEB build and verify 0 (§4.3) |
| PD-2 | S13 in-process root-bound probe instead of a child process | §9.2; avoids a change to `test_sanity_pipeline.py` outside §6 (F-5) | 4 S13 tests pass, fail on the base probe; release tests green |
| PD-3 | S11 assertion and negative case, test-only | §9.3 | engine-core tests green |
| PD-4 | S12 label in `notes`; roster of 23 paths / 28 rows; CLI conformance and endpoint catalog excluded | ID-1 and §9.4 leave encoding and list to PR-20; F-9 | label tests; validators 0 |
| PD-5 | IF-5 table and claim model | IF-5 verbatim | S22 tests |
| PD-6 | Mirror validator `crd_id` + `EPIC_CRD_EXCLUSIVE` | ID-2 verbatim | validator tests |
| PD-7 | Index normalizer `crd_id` + mutual exclusion | PF12 §8.3 names every serializer or validator; same clause as ID-2; same §6 file; no row change (F-7) | normalizer test; `--check` unchanged |
| PD-8 | F-8 test example switch to HDE-CRD-0003 | required by IF-5 admitting HDE-CRD-0002; §6 test home | both tests green |
| PD-9 | Strip the label inside `_catalog_validation_entries` and `_config_logical_delta` | required for S12 to coexist with the config-family publisher (F-6) | 21 errors and 3 failures before, 0 after |
| PD-10 | Adapt the manifest-only-cut invariant test to "the cut writes only the manifest; the updater alone relabels" | D-1 requires manifest-derived labels; canon's release-identity rules (HDE Schemas & Artifacts §6.2, §6.2.1, §6.4) still hold; same §6 test home (F-10) | failed before the adaptation, passes after (§4.3 R-10, R-11) |
| PD-11 | Compare the catalog-log rows after stripping the label in the config-family convergence test | IF-7 and acceptance (4) include the two catalog logs (they carry `release_id`); HDE Schemas & Artifacts §8.6.3.2 metadata preserved (F-11) | as PD-10 |

## 16. Boundary findings and rescope

None. No change outside §6 is needed (F-5, F-6, F-10 and F-11 were resolved inside §6 files), no acceptance intent, protected boundary, schema, canon, dependency or other unit is affected, and the S12 invariant is met inside the allowed key set (ID-1). Expected triggers named in instruction §14 did not occur: S06 needs no network, no non-test change outside §6 and no weaker exact-source guarantee; `generate_engine_core_evidence.py`, `qa_harness.py` and the classifier stay unchanged. If PR-30 finds otherwise, it routes a `RESCOPE_REQUEST` to the IA through RS-20 with `PR_RETURN_PHASE`. PD-10 and PD-11 change what two existing tests expect; they are recorded as in-scope because the approved interface (IF-7 with D-1's derivation) requires the behaviour they now check and no canon clause is contradicted. If Nathan or the IA reads either as a protected boundary, the alternative is a rescope through RS-10/RS-20 before Proceed (for example, a label held as a constant that each re-cut unit updates, which keeps the manifest-only invariant but contradicts D-1's "through the updater alone").

## 17. Observations and doc-delta candidates

- **OBS-W2-1 (doc-delta candidate, HDE Schemas & Artifacts §8.3; owner the Product Owner, through WU-DOC-01 or a later canon drain).** The `notes` label convention for current-release captures (§5.4) is a local convention inside the allowed key set; canon may wish to name it. Not a conflict.
- **OBS-W2-2 (doc-delta candidate; owner WU-DOC-01).** Building the attestation off CI requires either a non-patched setuptools or the compat of §5.1; the operator note for local rehearsals can say that E-DEB-style environments are supported.
- **OBS-W2-3 (other probes; owner the IA).** `tools/evidence/run_sanity_pipeline.py` has its own `release_not_admitted_observed` and the release lane's inline probe in `ci.yml` imports `engine` from the ambient environment. They are outside S13's scope ("the closure admission probe") and outside §6; recorded only.
- **Carried:** OBS-17 (qa lane; QA tool and test owner through the IA); O-6 (not applicable: this PR does not select the contract-inventory file); OBS-4 (expected same-byte rewrites); AQ-1 (Nathan; gates WU-PR-07 only); WU-PR-03 and WU-PR-06 downstream items of PF10 addendum 2.2 (IA).

## 18. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried unchanged: CR-1, CR-2, CR-3 (CANON_RECONCILIATION) APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED (Product Owner; `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2); CR-5 APPROVED_AS_CHANGED (Product Owner; same record §3). None is touched by this unit. No new entry: PD-4, PD-6 and PD-7 apply HDE Schemas & Artifacts §8.3 as written; PD-10 and PD-11 rest on HDE Schemas & Artifacts §6.2, §6.2.1, §6.4 and §8.6.3.2 as read in F-10 and F-11, which they satisfy; the instruction's ID-1 and ID-2 rest on HDE Governance §9.1.2; no canon edit is planned. Coverage: §6.2 to §6.4, §8.3, §8.6.3.2 (catalog construction validation) and §8.17 read; PF10 read in full.

## 19. PR-30 and PR-35 ownership

- **PR-30** (this dedicated session, after Nathan's Proceed for exactly this plan v1.0): recovery (C0); implementation of §5 only; governed regeneration by the updater only; local validation (§11); one coherent commit; the result record; deliberate initial publication of one pull request; `PR_CANDIDATE_PUBLISHED` and a handoff to PR-35 in its own dedicated session. PR-30 does not resolve reviews, chase CI or claim merge readiness.
- **PR-35** (its own dedicated session, entered from PR-30's handoff): retrieves and resolves the Codex code review findings (PF10 addendum 2.3: no Codex security review); retests locally; pushes coherent corrections; uses CI economically (one push per coherent correction; no `[skip ci]` without Nathan's direct authorization); verifies the current-head CI, including the release lane's attestation build and verify and the evidence lane, with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; verifies mergeability; returns `MERGE_PENDING` without merging.
- **Merge:** Nathan only. **PR-40:** the IA reviews the landed lineage after the merge is observed or asserted.

## 20. Session identity and recovery envelope

| Field | Value |
| :- | :- |
| session_disposition | INITIAL_DEDICATED_ASSIGNMENT |
| role_session_ref | NOT_YET_ASSIGNED (Nathan assigns at launch); authoring session https://claude.ai/code/session_01KTTzbrYjNwVoPN3AtpbN4a |
| invocation_binding | CRD HDE-CRD-0002 / WU-PR-02 / instruction v1.0 / this plan v1.0 |
| context_conflict | none |
| Proceed | not yet given; required before C0 |
| Resume point | PR-30 C0 |
| Preserved attempts | none earlier; this is the first plan |

## 21. TypeSafe reading for the receiving session (PR-30, WU-PR-02)

Action sent (v6): "Implement, in a dedicated session after the Product Owner's Proceed, one work unit of an approved change from a detailed plan that already has an ordered task list and designs prototyped and tested in a throwaway copy: repair four release-evidence tools and add tests (a build-backend compatibility path in the 870-line release attestation builder for a distribution-patched setuptools; a root-bound admission probe in a 420-line closure script; a release-identity assertion with a negative case in an engine-core evidence test; release labels on 28 machine-mirror rows and a two-entry change-admission table in a 5,000-line evidence-index updater; one accepted key and one mutual-exclusion refusal in a mirror schema validator), about seven source and test files plus governed index and mirror companions regenerated only by their owner tool, then run the evidence and release test lanes locally, rehearse the attestation build in a Debian-patched environment, make one commit and open one pull request. No live vendor, production or database run; an automated code review, a separate review-resolution session and a lineage review follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.28 (confidence 0.65); rung probabilities low 0.00, medium 0.12, high 0.49, extra high 0.37, max 0.02, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.98 (confidence 0.96). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.12, Opus 5.5 at high 0.48, Opus 5.5 at extra high 0.36, Opus 5.5 at max 0.02, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.01, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Flags: boundary between extra high and high. Sent 2026-10-13T17:01:16Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T17:01:16Z; HTTP 200 in 0.71 s; 4351 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags printed by the script: boundary between extra high and high.

- **Notion row:** not written, as PR-20 directs.
- **Nathan's pick for PR-30:** not stated. **For this PR-20 session:** not stated (the reading for PR-20 is in the instruction §19).

**Surface advice:** run PR-30 in a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access. The cloud container provides both rehearsal environments of §4.3: `/usr/bin/python3` (CPython 3.13.16) importing Ubuntu's patched setuptools 68.1.2 for E-DEB, and `/usr/bin/python3.12` for E-CI; creating them needs package-index access for `pip install` of the repository requirements (not for the builder itself, which runs offline). No live vendor, production or database access is needed. The full validation (§11) took about 35 minutes of wall time in the prototype, most of it the evidence lane's repository-copy tests (about 12 minutes) and the two attestation builds (about 3 minutes each). This plan's pull request should be merged before PR-30 runs.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-02 / PR-20 / plan 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| work unit | WU-PR-02 (S06, S11, S12, S13, S22) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page last edited 2026-10-12T02:29:47Z) |
| role/stage | dedicated WU-PR-02 PR engineering session / PR-20 |
| capture time | 2026-10-13T17:42:24Z |
| execution identity | https://claude.ai/code/session_01KTTzbrYjNwVoPN3AtpbN4a |
| inherited usage | PR-10 instruction 1 (instruction §20) |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; pending, non-gating; owner: an authorized repository writer once installed) |

## Canon relied on

Read on `main` at `b996a20`:
- **Plan authority and content:** PR-20 — Create Detailed PR Implementation Plan — 100926.1 (read in full); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (Product Owner Proceed per PR), §9.1.2 (canon precedence over in-flight documents), §9.7.7 (Plan approval gate: the detailed PR Plan's hold); Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "Repository loci and file minting" and "CI lane classification and automated budget-control discipline"; Change Process Guide (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md`) §0.2 and §1.0.4.
- **S12, ID-2, PD-7:** HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.3 "Single home and path", "Format (canonical JSONL)", "Minimum record schema (reject unknown keys)", "Allowed top-level keys and unknown-key rejection", "Self-record semantics", "Field order and write discipline" (read in full).
- **S22:** HDE Schemas & Artifacts §8.17 "Change-container identity (normative)" and "Path provenance (normative)".
- **F-10, F-11, PD-10, PD-11:** HDE Schemas & Artifacts §6.2 "release_id computation" and its "Distinct source, capture, release, and evidence identities" table, §6.2.1 "External release attestation", §6.4 "Evidence and CI hooks", §8.6.3.2 "Catalog construction validation".
- **Review chain and reading:** PF10-HDE-Build-Notes v13.5.5 (read in full) addendum 2.3 Rules 2 and 3; addendum 2.1 Rules 2 to 4.
- **Operative documentation:** `AGENTS.md` (canon-first rule; sole Index/Mirror writer; governed evidence never hand-edited; release identity formula; closed rails; pytest readiness; PR descriptions; QA output placement).

## Checks run by this session

Run in the session scratchpad only (throwaway clones and worktrees; the repository checkout was never modified except to write this plan and its companion). Every result is in §4.3 (R-1 to R-11). Summary:

| Check | Where | Result |
| :- | :- | :- |
| O-10 wheel command, before | `b996a20` export, `/usr/bin/python3` 3.13.16 | exit 1, `AttributeError: install_layout` |
| Wheel with shim vs distribution 3.12 wheel | same export | both 0; 129/129 entries identical |
| Full builder, before | `b996a20`, E-DEB | exit 1, receipt `build_package_wheel` |
| Full builder, S06 only / S06+S13 | prototype commits 1 / 2, E-DEB | 1 at `closure_write_and_check` / 0 with verify 0 |
| Updater and read-only validators | commits 3 and 6 | all 0; 28 rows / 23 paths labelled; idempotent |
| Classifier dry run | `b996a20..f64f1e8` | `lanes=evidence,release`; 15 paths; 5 targets |
| Changed-test step | commit 6 | 198 passed |
| Evidence lane tests | commit 3 / commit 6 / commit 7 | 3 failed + 21 errors (F-6) / 2 failed (F-10, F-11) / **126 passed** |
| Config, engine-core and release-lane tests | commit 6 / commit 7 | 165 and 75 passed / **240 passed** |
| qa lane (prudence) | commits 3 and 6 | 488 passed each |
| S13 negative control | commit 4 tests against the base probe | 4 failed, as intended |
| Full attestation, both environments | commit 6 | E-DEB 0/0 with compat line; E-CI 0/0 without; 174 / 14 each; clones clean |
| Env pins; `AGENTS.md` citations | commit 6 | 0; 0 |
| TypeSafe v6 reading for PR-30 | `score.py` | HTTP 200; §21 |

Not run: hosted CI (no pull request carries the code yet); the Codex code review (PR-35); any vendor, production or database call.

---

**State:** `AWAITING_PO_PROCEED`, held at `ASK OK? — PR IMPLEMENTATION PLAN`. This is the WU-PR-02 detailed PR implementation plan v1.0, complete and executable within the approved base plus PF10 addendum 2.3. Nathan's `PR Implementation Proceed` for exactly this plan path and version authorizes PR-30. Nothing else does.
