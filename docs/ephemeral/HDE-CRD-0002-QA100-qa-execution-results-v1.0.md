---
artifact_type: QA_EXECUTION_RESULTS
artifact_id: HDE-CRD-0002-QA100-QA-EXECUTION-RESULTS
artifact_version: "1.0"
predecessor: none (the first QA-100 result for HDE-CRD-0002)
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
stage: QA-100 — Execute Bounded QA Task — 100926.1
state: RESULTS_RETURNED_TO_QA110
author: the QA-100 executor the Product Owner chose by issuing the QA-100 handoff to this session; Claude Code CLI agent (model Claude Opus 5.5, claude-opus-5-5); not Kronos
role_session_ref: Claude Code local CLI session abab87ae-fdb9-4eb6-b2b9-de5380cee6cb (id taken from the session scratchpad path; no claude.ai session URL is available to this session)
invocation_binding: CRD / HDE-CRD-0002 / QA-100 / QA_PLAN v1.2 checks 1 to 15 (tasks T01 to T15, attempt 1 each)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-100 — Execute Bounded QA Task — 100926.1 (https://app.notion.com/p/3f44590a05eb8182a201f0e177dad431; page state 2026-10-12T02:30:45.204Z; read in full at this invocation)
ecosystem_release: GCFPE-20261009.1 (100926.1)
task_collection: docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.0.md (QA_TASK_COLLECTION v1.0, TASK_READY; SHA-256 fd1eb20d2cfd3a1da9b776980eaa9fcd705273f8eba537d0472ec02e96a328ca, equal to the QA-90 checkpoint's pin)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; blob 66f6016cc75bd1ab4ff9730ea89e5e25c7ec629c, SHA-256 8068ea350a9239c83e692a552bac8d5561a914d8694835faf4d38e0ab69f64e9; both verified equal to the approved bytes, and check 1 verified the blob in the E-L clone)
approving_review: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.2.md (APPROVE; SHA-256 b33d38a25defc48348189b9846a4e8d4f476b72d566882c67414c9af323037ef)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE; SHA-256 d4f886b7b2272a1fb4c2e8b251d0f6e3d731cbbe18e2b7234cac179948080dad)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; the single PF10 file on main)
tested_source: 2e03a2686af87ab0607c6cfb9afb4ad79bcdb171 (tree af5293473238c17d72c7d73013493739b9f32750; origin/main at clone time, after amthorn78/glow-hdengine-v2#724 merged; code outside docs/ephemeral/ and docs/pfcanon/ identical to 0b15328d, check 1)
evidence_branch: qa/hde-crd-0002-evidence (commits e97c3bba58e4be35ca0251d361d3ee3c0bc39881 for checks 1 to 12, 14 and 15, and 3d8080472473ed20b306da6a83228e16c11f82cb for check 13, on parent 2e03a268; pushed)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/726 (open, not merged; carries the evidence and this record set)
related_pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/727 (open, not merged; the two Product Owner direction records of §8)
routing: QA-110 — Review QA Evidence and Route the Next Action — 100926.1, the continuing Kronos session
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-100 (QA-100 is not an addendum producer)
created_at: 2026-10-25T01:10:00Z
---

# HDE-CRD-0002 — QA-100 execution results v1.0: tasks T01 to T15 (QA Plan v1.2 checks 1 to 15), attempt 1

## 1. Result

| Field | Value |
| --- | --- |
| Collection executed | T01 to T15 of the QA-90 collection, all fifteen in caller order, each attempt 1. T01 was published before any other task. No task was skipped or narrowed |
| Result states | 14 × `COMPLETE`, 1 × `FAILED` (T13). No state is an acceptance or a QA PASS |
| Step-log statuses published | 14 × `PASS`; `qa-13-prepush-check` `FAIL_BEHAVIOR` |
| In-session Moon Loops | Two, each directed by the Product Owner in this session (§5): check 3 (E-D interpreter wiring; then `PASS`) and check 13 (`TMPDIR`; the venue cause was removed, `FAIL_BEHAVIOR` remains) |
| Publication | One `publish_crd_check_family` call per check through the §4.7 helper. After every call and on the committed state, all six read-only validators passed (§6) |
| Evidence storage | Committed and pushed on `qa/hde-crd-0002-evidence` under the Product Owner's evidence-persistence direction, used as Plan v1.2 §2's evidence-only commit grant (§8 PO-4). Pull request #726 |
| For Kronos at QA-110 | Check 13's `FAIL_BEHAVIOR` (S20 finding, §5.2); acceptance of both Moon Loops (§5); deviations D-01 to D-08 (§7) |

## 2. Identity, venue and environment

| Field | Value |
| --- | --- |
| Executor | Claude Code CLI agent, model Claude Opus 5.5, in the session above. Chosen by the Product Owner by issuing the QA-100 handoff to it. Execution authority only, not acceptance authority |
| Venue | The Product Owner's Linux workstation: Ubuntu 26.04.1 LTS, kernel 7.0.0-38-generic, 2 CPUs; `/tmp` is a tmpfs; `TMPDIR=/home/nathan/.tmp` (ext4) in the agent's shell |
| E-L | Full-history clone (plain `git clone`) detached at `2e03a268`. Venv from CPython 3.12.15, a uv-managed python-build-standalone build: this venue has no distribution Python 3.12, and its `/usr/bin/python3` is 3.14.4. CI's full install (`setuptools` 84.2.1, `pytest` 8.4.2, Flask 2.3.3). `ruby` 3.3.8, `bash` 5.3.9, `curl`, `git` 2.53.0. `XDG_STATE_HOME` an empty scratch directory |
| E-D (check 3) | Through the Moon Loop: a venv from uv-managed CPython 3.13.17 with a `.pth` path entry for `/usr/lib/python3/dist-packages`, so the venv imports Ubuntu's `python3-setuptools` 78.1.1-0.1build1 (distribution-patched) and `python3-wheel` 0.46.3. `_distutils_system_mod` is not importable (§5.1) |
| Evidence checkout | Separate full-history clone on `qa/hde-crd-0002-evidence`, from `origin/main` `2e03a268`; tests never ran there |
| Rails | Every check and every publication ran under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`, `PYTHONDONTWRITEBYTECODE=1`. Every `captured_env` carries the check shell's actual values |
| Presence | The venue's parent shell holds `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `DATABASE_URL`. Every check shell unset them (§4.3 step 6); check 1 step 4 shows all nine names `UNSET`. No value was read into evidence. Each body was scanned both from the check shell (§4.6 command) and against the parent shell's actual values (comparison only): `NO_HIT` every time |
| Network | Setup only: the clones, the pip installs and `uv python install 3.13`. No check made a network, vendor, database or production call |
| Times | Setup 2026-10-24T23:36:31Z to 23:37:00Z; T01 start 23:40:59Z; last publication 2026-10-25T00:58:28Z |

## 3. Task-to-result map

Every primary is at `audit/qa/hde-crd-0002/checks/<check_id>/primary.log` with its `.path_proof.txt`. Each primary's SHA-256 equals its path proof, its manifest status equals its header status, and both Index keys and both Mirror rows are present. For every check the Index keys are `audit.qa.hde_crd_0002.checks.<check_id>.primary.log` and `audit.qa.hde_crd_0002.qa_step_logs_manifest`.

| Task | `check_id` | State | Status | Bytes | SHA-256 | `timestamp_utc` | `exit_code` |
| :- | :- | :- | :- | -: | :- | :- | -: |
| T01 | `qa-01-preflight` | COMPLETE | PASS | 290,492 | `01df910157d7d96ec9d6b7cfeb18be22aa1c7f2f3d8b8e2437c77e1af80303e4` | 2026-10-24T23:41:30Z | 0 |
| T02 | `qa-02-ci-coverage` | COMPLETE | PASS | 7,990 | `bc52ae603d33932cc634751f267d7e21b3f1c8438a0deebe294cfb70c1359eac` | 2026-10-24T23:44:26Z | 0 |
| T03 | `qa-03-attestation-debian` | COMPLETE | PASS (Moon Loop) | 39,632 | `7dfc152a9f8e38450a1644437f692c6687998c30179b315834e0ffa854cf3094` | 2026-10-24T23:56:15Z | 0 |
| T04 | `qa-04-showcompat-help` | COMPLETE | PASS | 11,443 | `3e8b5c5d74f654c31400b4fb2e29d0784c192de744531ade671084d01a92ef5d` | 2026-10-24T23:46:35Z | 0 |
| T05 | `qa-05-aux-preview-band` | COMPLETE | PASS | 23,571 | `e06b99d39affdc48aac8674da54df21a9e64719bb5613a4f27b86c9139b7f8ee` | 2026-10-24T23:47:31Z | 0 |
| T06 | `qa-06-dev-harness-retired` | COMPLETE | PASS | 8,485 | `0fe1f4cb69ff89b8cdad5cbd03a5c2f957d471d15e2b9266f42b2a71aecfc5e2` | 2026-10-24T23:48:08Z | 0 |
| T07 | `qa-07-dev-reader-gate` | COMPLETE | PASS | 6,097 | `3da89797b92d68046be61c46a53c280d7e530dff5aea75ee0b3531c1709ae262` | 2026-10-24T23:57:35Z | 0 |
| T08 | `qa-08-release-evidence-tooling` | COMPLETE | PASS | 7,264 | `f1421a7e6412cedf3c7ea8031568e327eb17a0f266a8f9ea5a41538bc53ec5e3` | 2026-10-24T23:58:26Z | 0 |
| T09 | `qa-09-override-matrix` | COMPLETE | PASS | 14,878 | `fea39bb3ead43325c6607bfc770afad7afb93176335548c17c07eb4d419bc643` | 2026-10-24T23:59:03Z | 0 |
| T10 | `qa-10-endpoint-catalog` | COMPLETE | PASS | 7,209 | `34c747808926344b21553cb75ca6656880bf43d7c05133ba2198d67c1946f6da` | 2026-10-24T23:59:56Z | 0 |
| T11 | `qa-11-template-and-documents` | COMPLETE | PASS | 16,634 | `21c193380cf4accd181427dcb1047c220a7031cc448371dff88fe67db724c9d7` | 2026-10-25T00:00:51Z | 0 |
| T12 | `qa-12-security-review` | COMPLETE | PASS | 8,802 | `d7c986943c3f52a49a75d06a49d94de9c9dad984443a8958f20ccbb1dc610c08` | 2026-10-25T00:01:57Z | 0 |
| T13 | `qa-13-prepush-check` | FAILED | FAIL_BEHAVIOR (Moon Loop) | 35,842 | `71a0d11afff1b89a76a9c7624d0cfa93d22845f5714a3618a87c7967b9593ef7` | 2026-10-25T00:56:35Z | 4 |
| T14 | `qa-14-close-pack-writer` | COMPLETE | PASS | 7,998 | `d4d2f223c8b6e62f2df3e028b7633bab8f96e2508ffa4040b75ca7a3b9a23e7d` | 2026-10-25T00:23:16Z | 0 |
| T15 | `qa-15-s01-removal` | COMPLETE | PASS | 8,380 | `f4233b2f574828f5bbce3ff2c36f4935a81072af59784245257b527b1541d582` | 2026-10-25T00:23:59Z | 0 |

Manifest `audit/qa/hde-crd-0002/qa_step_logs_manifest.json`: 2,339 bytes, SHA-256 `ae34abc336da8b2323f756ffbe2202fe2a8f78615bfa781075e17460e3e064e9`. It lists the fifteen check IDs with the statuses above.

## 4. QA_EXECUTION_RESULT records

Every task ran its readiness reads (collection §4.5; check 1 is its own bootstrap) and found them `PASS`. The decisive observations are below; every command, exit code and output is in the primary.

### T01 `qa-01-preflight` — COMPLETE, `PASS`

| Item | Observed |
| :- | :- |
| Candidate | Tested commit `2e03a268`, shallow `false`, `7136040` resolves; the guard diff against `0b15328d` is empty |
| Manifest | SHA-256 `77204764…66c51e`; `1.3.0 2026-08-24T18:04:49Z 45`; `hdctl --version` exact |
| Tools and environment | Python 3.12.15, `pytest` 8.4.2, `ruby`, `bash`, `curl` and `git` present; `engine` inside the clone; the nine names `UNSET` |
| Validators | Six, each exit 0 |
| Step-0B | All twenty selectors collect exactly their Audit counts; five entrypoints exist; the three documents are tracked; the PF10 file is v13.7.8; the Plan blob is the approved one; both doc-delta surfaces are absent (asserted `ls -l` exit 2). BLOCKERS none, CAVEATS none: "no deltas" |
| Status | Empty |

Normalizations: NZ-01, and NZ-05 (steps 1, 6 and 7 in one asserting script, run after steps 2 to 5 so the status read is last).

### T02 `qa-02-ci-coverage` — COMPLETE, `PASS`

"3 passed"; "2 passed"; the ledger has 66 rows with no `BAD` line, and 0 ledger paths are still tracked. Hosted push run 39699657729 is cited, not re-run.

### T03 `qa-03-attestation-debian` — COMPLETE, `PASS` through a Moon Loop (§5.1)

Attempt 1, published first, was `TOOLING_BLOCKED`: no system interpreter in the venue met E-D. The decisive Moon Loop rerun 2 met every predicate:

| Step | Observed |
| :- | :- |
| 1 | `78.1.1 /usr/lib/python3/dist-packages/setuptools/__init__.py None` |
| 2 and 3 | Build and verify each exit 0 |
| 4 | `attestation.json` 28,163 bytes, SHA-256 `5fe81fd77dac66a47fdb464217026687497ba3549c3f4d40171015ff5b9d8ade`, `source_commit` `2e03a268`; `release_id` `77204764…66c51e`, `PASS`, `PR06R_B_FINAL_PASS`; compat line count 1 |
| 5 | "11 passed" |
| 6 | Build clone status empty |

Normalizations: NZ-01 and NZ-07.

### T04 `qa-04-showcompat-help` — COMPLETE, `PASS`

Both help commands exit 0 with empty stderr, and their stdouts are byte-identical (797 bytes). The S07 sentence occurs once. `check_cli_help.sh` exits 0; "2 passed". `COLUMNS` was unset (NZ-03).

### T05 `qa-05-aux-preview-band` — COMPLETE, `PASS`

`harmony` is `Cool`. Eight `aux-preview` commands exit 0 with empty stderr. For Open, Warm and Glow, the file form equals the flag form and differs from the no-band output; the no-band output equals `Cool`. "7 passed". The `cmp` comparisons ran in one asserting script (the NZ-05 pattern; D-03).

### T06 `qa-06-dev-harness-retired` — COMPLETE, `PASS`

Nothing is tracked under `dev/reader_harness` and `app.py` is absent. The `harness` counts are 0 and 0 (grep exit 1, asserted). "4 passed". NZ-05.

### T07 `qa-07-dev-reader-gate` — COMPLETE, `PASS`

"33 passed"; one match at `adapter/http_reader.py:389`.

### T08 `qa-08-release-evidence-tooling` — COMPLETE, `PASS`

"2 passed", "6 passed", "4 passed". Supporting count: 27 Mirror rows carry the current-release label.

### T09 `qa-09-override-matrix` — COMPLETE, `PASS`

"256 passed". Probes (a) and (b) exit 1 with `status` `error` and code `PROVIDER_REFUSED`, stderr empty. Probes (c), (d) and (e) exit 64 with empty stdout and one stderr line that does not contain the flag value. `XDG_STATE_HOME` and status are empty. NZ-05.

### T10 `qa-10-endpoint-catalog` — COMPLETE, `PASS`

"247 passed"; `generate_a7_transport_proofs.py --check` exits 0; the catalogs are equal; 18 records.

### T11 `qa-11-template-and-documents` — COMPLETE, `PASS`

Fourteen "contains" counts are each 1 or more, and the one "no" count is 0 (factory and dev runner, exit 1 asserted). The classifier prints `documentation_only`; `emit_public` returns `bytes`; the three factory names appear in `## Routing and mounts`. NZ-05.

### T12 `qa-12-security-review` — COMPLETE, `PASS`

`per-file rows 49`; `fixed rows 9 without disposition 0`; `routed rows 7 without disposition 0`; "268 passed". NZ-04.

### T13 `qa-13-prepush-check` — FAILED, `FAIL_BEHAVIOR` after a Moon Loop (§5.2)

On the decisive rerun, step 1's reports were all as predicated:

| Report | Observed |
| :- | :- |
| `lanes` | `reason=selected_lanes;paths=2;lanes=product,compat,release` |
| `membership` | Member and not-member lines as predicted |
| `build-notes` | Path and SHA-256 as predicted |
| `sweep` | `uncovered=0` |
| `replay` | Steps 01 to 16 `SUCCESS`; step 08 "4521 passed, 2 skipped" |
| All five | `status=PASS` |

Even so, the tool exited 4 with `PREPUSH_CHECK_READ_ONLY_VIOLATION`, and the `PREPUSH_CHECK_RESULT: PASS … repository unchanged` line is absent. Step 2 passed, step 3 "137 passed", step 4 empty. Check 13's own Outcomes line maps exit 4 to `FAIL_BEHAVIOR`.

### T14 `qa-14-close-pack-writer` — COMPLETE, `PASS`

"905 passed"; "4 passed". ADR line 3 begins as predicated, with the review reference `docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md`. The v2 schema exists.

### T15 `qa-15-s01-removal` — COMPLETE, `PASS`

Every count is 1. `git log 7136040^..HEAD -- pyproject.toml` prints nothing in a full-history clone. The Procfile starts `adapter.factory:create_app()`.

## 5. Moon Loops (Glow QA Guide §3.4.8; Plan Templates "Bounded step-level rerun posture")

Both loops were directed by the Product Owner in this session. Each changed only QA-created environment wiring outside every repository; no repository file, product code, test, generator, predicate or expected value changed. Kronos decides at QA-110 whether to accept each as a PASS-only Moon Loop deviation (T03), and how to classify T13's remaining failure.

### 5.1 Check 3 (T03)

- **Direction:** "We need to just run a moon loop and pass T03. I am not going to be blocked on a python version as long as the product functions".
- **Original attempt-1 receipt:**
  - Status `TOOLING_BLOCKED`: "No interpreter meets step 1 in this venue: /usr/bin/python3 (3.14.4) makes _distutils_system_mod importable; /usr/bin/python3.13, 3.12 and 3.11 are absent".
  - Published 2026-10-24T23:46:03Z, before any evidence grant, so it was never committed; the republication replaced it in the evidence checkout.
  - Its exact bytes are preserved in the repository at `docs/ephemeral/HDE-CRD-0002-QA100-t03-attempt1-primary-v1.0.log` (12,380 bytes, SHA-256 `f67c2274cb9288f464616b5db503846b36dacd6f245b03521af9b2e4872961e3`).
- **Remediation:**
  - E-D was rewired from uv-managed CPython 3.13.17 (no `_distutils_system_mod`) with a `.pth` path entry for `/usr/lib/python3/dist-packages`.
  - That gives the WU-PR-02 F-1 causal condition: a non-distribution interpreter importing Ubuntu's patched backend. The `install_layout` and `prefix_option` patch is present in this venue's `setuptools/command/install_lib.py` and `install_egg_info.py`.
- **Rerun 1 (QA environment defect):**
  - Builder import failed with `ModuleNotFoundError: No module named 'rpds.rpds'`. pip had treated the distribution's Python 3.14 C-extension `rpds` as satisfying the requirements.
  - Corrected with `pip install --ignore-installed`, so only `setuptools`, `pkg_resources` and `wheel` come from the distribution path.
  - Rerun 2 is decisive.
- **Fidelity:**
  - Step 1's two defining properties hold literally, and the builder's own probe judged the condition present (`build_backend_compat=distribution_install_layout`).
  - Departures from the Plan's literal construction ("`/usr/bin/python3 -m venv --system-site-packages`") and from WU-PR-02's E-DEB: interpreter build (uv CPython 3.13.17 rather than deadsnakes 3.13.16), the `.pth` path entry, `setuptools` 78.1.1 rather than 68.1.2, and `wheel` 0.46.3 rather than 0.42.0.

### 5.2 Check 13 (T13)

- **Direction:** "That means this environment needs a fix, so resolve it as a moon loop".
- **Attempt-1 failure signature** (kept in the same primary, 2026-10-25T00:02:22Z to 00:16:57Z):
  - Step 1 exit 4; `replay: status=FAIL` at step 08 with 2 failed and 4,521 passed, both failures in `tests/ops/test_hde_epic038_ops03.py`:
    - `::test_candidate_replacement_failure_is_persisted_before_cleanup`;
    - `::test_validator_rejects_authorized_candidate_symlink`, which raised `OSError: [Errno 18] Invalid cross-device link` between the tool's fixed `RUN_ROOT` `/tmp/hde-epic038-ops03` (tmpfs) and pytest's `tmp_path` under `TMPDIR=/home/nathan/.tmp` (ext4).
  - Replay steps 09 to 15 `SKIPPED`, step 16 `FAILURE`; stderr `PREPUSH_CHECK_READ_ONLY_VIOLATION`.
- **Remediation:**
  - `TMPDIR` was unset in the check shell, as on hosted CI, so Python's `tempfile` uses `/tmp`.
  - The two directories attempt 1's failed tests had left under `/tmp/hde-epic038-ops03` were listed and removed.
- **Result:**
  - The venue cause is removed: replay `status=PASS`, steps 01 to 16 `SUCCESS`.
  - The read-only violation recurred, so it does not come from the venue's `TMPDIR`. Status `FAIL_BEHAVIOR`; exit_code 4 (step 1, the decisive child).
- **Observation on the cause (executor's reading, not a predicate):**
  - In both runs no tracked, ignored or directory entry of the E-L clone changed. The only `.git` file whose mtime and ctime moved in the check window is `.git/objects/pack/pack-0702e37ebe0101b3b80d126c73ab6880b2aff2bc.pack`, last at 00:16:40Z and 00:56:17Z, both inside step 3; a step-1 change would have been overwritten by those.
  - `repository_state()` in `tools/ci/prepush_check.py` digests every `.git` file's lstat identity (mtime and ctime), objects included.
  - `make_copy()` clones every throwaway copy with `git clone --shared`.
  - An executor diagnostic in separate scratch repositories (git 2.53.0), outside the check, showed that `clone --shared` plus checkout leave the source pack untouched, but writing an object that already exists in the source pack from inside the copy updates the source pack's mtime. A replayed test that writes such an object trips the guard.
  - The Audit's preapproval run at `0b15328d` (Audit §7 item 9) reported "repository unchanged". Why that venue did not trip the guard is not established.
  - The PR35-C1 signature (a test in `tests/tools/test_prepush_check.py` failing on a maintenance race) does not apply: those tests passed in step 3 and in the replay.

## 6. Publication, indexing and receipt (collection §4.7, §4.11)

- One helper call per check, each printing `PUBLISHED <primary> <manifest>` with exit 0. The helper is collection §4.7 byte for byte (SHA-256 `8bfbde7cdddfa79cdcbc568096c1f4e8acff23e45c28ee665de12e8ba016b0ae`), run as `python -c "exec(open(...).read())" <spec>` from the evidence checkout (NZ-06).
  - Check 3 was published twice: attempt 1, then the Moon Loop result, merged by `check_id`.
  - There was no refused publication.
- After every call, from the evidence checkout, each exited 0:
  - `update_evidence_index.py --check`;
  - `orientation_demo.py --check`;
  - `validate_evidence_paths.py`;
  - `check_mirror_schema.sh`;
  - `check_lf_endings.py`;
  - `validate_crd_check_family(HDE-CRD-0002)`, which grew from 1 to 15 checks.
- Final receipt for this selection, on the committed state `3d808047` with status empty (2026-10-25T00:59:14Z): the five command-line validators each exit 0 with empty stderr, and `validate_crd_check_family` lists exactly the fifteen check IDs.
  - This is not Plan §5.6's final receipt, which follows check 21.
  - No primary claims a graph that includes itself.
- Changed paths, both commits together:
  - 32 files added under `audit/qa/hde-crd-0002/`: 15 primaries, 15 path proofs, and the manifest with its path proof;
  - the ten updater-owned graph files, modified by the writer only;
  - nothing else under the root (no sidecar, no `00_meta/`).
- The writer stamps `produced_at_utc: 2026-09-22T14:25:29Z` in the CRD path proofs. That is the writer's own value, recorded as observed and not judged here.
- Hosted CI: expected lanes `evidence` and `release` (Plan §5.6), with named risks FND-024 and IR-7. The result of #726 is pending; QA-110 reads it from GitHub.

## 7. Deviations and observations for QA-110

| ID | Item |
| :- | :- |
| D-01 | NZ-01 throughout: the scratch locations are under the session scratchpad (`/home/nathan/.tmp/claude-1000/-home-nathan-glow-hdengine-v2/abab87ae-fdb9-4eb6-b2b9-de5380cee6cb/scratchpad/hde-crd-0002-*`), not `/tmp` |
| D-02 | T01's order: steps 2 to 5 ran before the NZ-05 script (steps 1, 6, 7), so step 7's status read was last; `command` records the actual order. Every command is read-only |
| D-03 | T05: step 3's `cmp` comparisons ran in one asserting script (expected 0 for equal and 1 for differing pairs). The Plan's "every command exits 0" is read as the product commands. T05 is not among NZ-05's listed tasks; the same Plan §5.2 rule was applied |
| D-04 | T10 adds a supporting `git status --porcelain` after the generator's `--check` (recorded, not decisive). T13 records step 1's exit (4) as `exit_code`, the decisive child for the failed predicate |
| D-05 | T11's three factory names were resolved from the `## Routing and mounts` section itself: `adapter/factory.py::create_app`, `adapter/wsgi.py::create_app`, `adapter/http_reader.py::create_app`. Each was counted only within that section |
| D-06 | QA-glue corrections before publication, none changing an observed value: T02's step-4 citation row marked `RECORDED`, not `PASS`; T11's `emit_public` evaluator re-run because the first version over-required one matching line (`grep` also lists `emit_public_with_envelope`); T02's finalization time taken from the predicates file's write time, because the run shell did not persist it |
| D-07 | Body capture: lone CR bytes from git progress output in check 3's setup records were converted to LF, and the body notes it (Plan §5.3 rule 1) |
| D-08 | Each check's spec was scanned for secrets as well as its body (`NO_HIT`) |

## 8. Product Owner decisions in this session

| ID | Words (verbatim) | Effect |
| :- | :- | :- |
| PO-1 | "We need to just run a moon loop and pass T03. I am not going to be blocked on a python version as long as the product functions" | The check 3 Moon Loop (§5.1) |
| PO-2 | "Make a PO note which should be drained to canon: we should not be pinning tool versions. … Function matters, not tool versions." | `docs/ephemeral/HDE-CRD-0002-po-direction-tool-version-pinning-v1.0.md` (#727), `PENDING_DRAINAGE` |
| PO-3 | "That means this environment needs a fix, so resolve it as a moon loop" | The check 13 Moon Loop (§5.2) |
| PO-4 | "you never asked me where i wanted the evidence.QA  evidence needs to be PERSISTED in the repo, not kept in tmp. this needs to be re-litigated" | `docs/ephemeral/HDE-CRD-0002-po-direction-qa-evidence-persistence-v1.0.md` (#727). Used as the Plan v1.2 §2 evidence-only commit grant: the evidence was committed on `qa/hde-crd-0002-evidence` in #726 |
| PO-5 | Asked whether the evidence-persistence rule should also be drained to PF canon (options: 1 drain to canon, PF19 §3.4.3; 2 change level only), the Product Owner answered: "1 but just include this in your report, do NOT edit pfcanon" | **Decision: drain to canon.** Target: PF19-Canon-Glow-QA-Guide §3.4.3 (evidence layout), stating that published QA evidence is persisted in the repository. Owner and route: the Product Owner's canon drainage (an HDE Build Notes addendum by an authorized producer, or the Product Owner's own canon transfer). It supersedes the "OPEN" drainage line of that direction record's §5 (v1.0, unchanged). No PF canon file was edited |

## 9. Residual state, cleanup and resume point

- **Cleanup done (collection §4.9, 2026-10-25T01:00:31Z):** deleted the E-L clone, the E-L venv, the scratch `XDG_STATE_HOME` (0 files), the check-3 scratch (E-D venv, build clone, attestation output) and the check-5 scratch, plus the diagnostic repositories.
- **Kept until QA-110 has read this result:**
  - the evidence checkout (`…/scratchpad/hde-crd-0002-evidence`, clean at `3d808047`);
  - the QA working files (`…/scratchpad/hde-crd-0002-qa`: helper, specs, bodies, per-check parts, T03 attempt-1 parts, T13 attempt-1 outputs).
- **Outside the repository, not removed:** uv-managed CPython 3.13.17 in `/home/nathan/.local/share/uv/python/` (installed for the check 3 Moon Loop), and two directories left under `/tmp/hde-epic038-ops03/` by the repository's OPS03 tests during the check 13 rerun (`ops03-test-03c7fd6d9c364a7ebd4bc9b7`, `ops03-test-c9f3990f2f154f8f83394c7e`).
- **Resume point:** none for QA-100. Every selected task has a published, committed primary. The next action is Kronos's at QA-110, including any attempt 2 of check 13 (Plan §9).

## 10. Carried lineage and CANON_CONFLICT_REGISTER

- Plan v1.0 → `DENY` → v1.1 → `DENY` → v1.2 → `APPROVE` (QA-70 review v1.2) → QA-90 collection v1.0 (`TASK_READY`) → this QA-100 result. No earlier QA-100 result or QA-110 decision exists; every task is attempt 1.
- The CANON_CONFLICT_REGISTER is carried unchanged from Plan v1.2 §13 and collection §6:

  | Entry | Status |
  | :- | :- |
  | CR-1 to CR-3 | `APPROVED_AS_CHANGED` |
  | CR-4 | `APPROVED` |
  | CR-5 | `APPROVED_AS_CHANGED` |
  | CR-6 to CR-8 | `APPROVED`, alternative (a) |
  | CR-9 | `PROPOSED` (Isis, IA-30 boundary) |
  | CR-10 | `APPROVED`, alternative (a) |
  | CR-11 | `APPROVED_AS_CHANGED`, alternative (a); applied in check 1, which found no deltas |

  QA-100 proposes no new conflict. PO-2 and PO-4 meet canon that is silent on their subjects (each direction record §3 or §5).

## 11. TypeSafe reading for the receiving session (QA-110)

Action sent (v8.2): "Review a new, not yet reviewed QA execution result for one change request: 15 local checks already run against an approved QA plan and task list, each with a committed evidence log, manifest entry and index rows; for each check, decide whether the evidence is complete and its status stands, including two in-session environment workarounds the Product Owner directed (one rewired the interpreter for a build check, one changed the temp-directory setting) and one failure of a delivered developer tool to classify and route for repair. No live run against a provider occurs; the 15 checks are independent units that must each be checked; repair work and a final QA report follow."

- **TypeSafe: not read.** As printed by the script: "TypeSafe v8.2: not read (HTTP 403 after 2 attempt(s), sent 2026-10-25T00:59:28Z). Do not fill in a reading by hand." This local Claude Code venue does not attach the Glow app environment's credential, which the skill relies on.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "QA-110 HDE-CRD-0002 checks 1 to 15 evidence review".
- **Records:** the Notion row was not written.
- **Picks:**
  - This QA-100 session: the Product Owner set Opus 5.5 at extra high effort (`/model`, at session start). Its reading is in the collection §9 (Opus 5.5 at high, score 1.65).
  - QA-110: the pick is not stated.
- **Surface advice for QA-110:**
  - **Session:** the continuing Kronos session for HDE-CRD-0002 (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV), on `amthorn78/glow-hdengine-v2`.
  - **Reads:** this record; the fifteen primaries and the manifest on #726, or on `main` once merged; the T03 attempt-1 primary file; the two direction records on #727; Plan v1.2 §7 checks 3 and 13, §9 and §10; Glow QA Guide §3.4.8 and §10.6; Plan Templates "Exact status predicates", "Causal precedence" and "Bounded step-level rerun posture".
  - **Optional re-check:** the `--shared` freshening observation of §5.2 can be reproduced with two scratch git repositories in under a minute. Check 13's cause can be examined in `tools/ci/prepush_check.py` (`make_copy`, `repository_state`, `_metadata_digest`) without running the 24-minute replay.
  - **Access:** GitHub read for #726 and #727, including its hosted CI result. No production, vendor, Railway or database access.
  - **Writes:** its QA-110 decision record under `docs/ephemeral/`, by pull request.

## 12. Nonclaims

This result executes and publishes evidence only. It establishes no QA verdict, acceptance, closure, deployment, release activation or S-requirement, and it decides nothing about routed Product Owner items (FND-012, FND-028, FND-029, X-02, G-1). The pre-push tool's result is not CI's result. No product, test, generator or PF canon file was changed.

## Canon relied on

Read on `main` at `2e03a268`; this session's branches edit no `docs/pfcanon/` file.
- QA-100 — Execute Bounded QA Task — 100926.1 (page state 2026-10-12T02:30:45.204Z), read in full.
- PF19-Canon-Glow-QA-Guide v3.0.6:
  - §3.4.7 "Command formatting" and §3.4.8 "Rails posture for manual Live QA", each read in full, including Moon Loop, "Entrypoint existence preflight", "Execution-critical helper readiness", "Evidence posture for in-session remediation", the stop condition and "PO-approved Extended Moon Loop remediation";
  - §10.6 "Remediation QA evidence and review rules", read from its opening through "Evidence-package caveats and failure history".
- PF27-Canon-Plan-Templates v2.0.5: "Exact status predicates", "Causal precedence" and "Bounded step-level rerun posture", each read in full.
- PF04-Canon-HDE-Governance v2.8.7 §9.8.2 "Blocked-step minimum fields", read, for attempt 1 of check 3.
- PF06-Canon-Change-Process-Guide v2.5.4 §0.4 and §0.6.2 (the determinism-pin passages); PF29-Canon-HDE-Users-Guide v1.0.2 §3.1; PF07-Canon-Glow-Infrastructure v2.3.3 §2.2 and §10 (for PO-2).
- HDE Build Notes v13.7.8, the version in force, searched for Moon Loop, PR35-C1 (addendum 2.21's record, read) and tool versions.
- In-flight: the QA-90 collection v1.0 (read in full); Plan v1.2 (§0 to §9, §12 to §14, and checks 1 to 15, read in full); the QA-70 review v1.2 §7 and the cautions N-1, N-4, N-5, N-8 and N-101 of reviews v1.0 and v1.1; QA Audit v1.0 §7; WU-PR-02 implementation plan v1.0 (F-1, PD-1, E-DEB).

## Provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-100-20261024-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | QA Plan v1.2 checks 1 to 15; QA-90 tasks T01 to T15, attempt 1 each |
| prompt | QA-100 — Execute Bounded QA Task — 100926.1, page state of 2026-10-12T02:30:45.204Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | QA-100 executor (Product Owner's choice), `RESULTS_RETURNED_TO_QA110` |
| capture time | 2026-10-25T01:10:00Z |
| execution identity | Claude Code local CLI session abab87ae-fdb9-4eb6-b2b9-de5380cee6cb (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-90-20261024-01 and those it lists, each in its artifact |
| task/result mapping | T01 to T15 → `qa-01-preflight` to `qa-15-s01-removal` → §3 |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
