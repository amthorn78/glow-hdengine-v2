---
artifact_type: REMEDIATION_PROPOSAL
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001
artifact_version: "1.1"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: REMEDIATION_PENDING
approval_sentinel: "ASK OK?"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (FND-001; Reality Audit RA2-22; blob dac6d1a79de8). Unchanged; return owner Isis, QA-10 reassessment of S22
delivery_stage_evidence: finding F-1 in docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0.md §16, with its rehearsal §12 (PR-20, BLOCKED; blob 9009107b3be8; #710, squash f5c7c7f), and its companion docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0-prototype.diff (blob 2a2895a589fd)
originating_stage: QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, NOT_READY (docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md §5; blob f6d7ff018ce7); producer Isis
requirement: S22 (QA evidence admission), with S21's close-run tests and close-pack rows
predecessor: v1.0, docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.0.md (blob ee59f22c432a; sha256 d120223b8e9d5f51176228153a1debf8274f142cd780520cf7513c0a4d02b70d; #707)
predecessor_decision: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001 v1.0, APPROVE_AS_CHANGED with C-1, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md (Isis; blob e100bf4eba08; #708); addendum record docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (2.23; blob 248c17e7e513; not yet in the PF10 file, publication the Product Owner's)
work_unit_records_affected: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-instruction-v1.0.md (PR-10, INSTRUCTION_READY; blob d89d1dc9991b) and the PR-20 plan v1.0 above. No Proceed, branch or pull request exists for WU-REM-01
author: Thoth, Head of Development, continuing HDE-CRD-0002 remediation author (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum)
reviewer: Isis, continuing Lead Developer, ESC-40 — Review and Return Approved Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b)
prompt: ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9; page state as of 2026-10-12T02:29:51.552Z, fetched and read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
created_at: 2026-10-23T19:25:00Z
repository_head_read: origin/main f5c7c7f (#710 merged). Outside docs/ephemeral/, every byte equals 7d5a5aa, v1.0's reproduction head (git diff --stat 7d5a5aa f5c7c7f outside docs/ephemeral/ is empty)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md (454,052 bytes; sha256 2759c4da5e779970f144686c60f9683048583cd7ca50337026c1f8c7c548e167; last addendum in the file 2.22), with the 2.23 record
pf10_addendum: none (ESC-30 produces none)
PR_RETURN_PHASE: not applicable (WU-REM-01 has no Proceed and no pull request)
next_prompt: ESC-40 — Review and Return Approved Remediation — 100926.1
canon_conflict_register: CR-1 to CR-8 carried, decided; CR-9 carried PROPOSED, unaffected; CR-10 new, PROPOSED (§13)
---

# HDE-CRD-0002 — Remediation proposal for FND-001 (S22), v1.1

## 1. Result

**REMEDIATION_PENDING.** This is the complete successor to v1.0. It answers finding F-1, which WU-REM-01's PR-20 raised against the remedy Isis approved as changed.

- **F-1 is valid.** I reproduced it independently. Once HDE-CRD-0002's close pack is indexed, `tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity` fails: it rejects the `crd_id` key that the updater writes on the two close-pack rows. The approved remedy cannot fix this, because its limit is "No other file changes".
- **Diagnosis found a second defect with the same cause, F-2.** The QA harness (`tools/qa/qa_harness.py`) checks every Index and Mirror row against its own allowed-key set, and that set also lacks `crd_id`. With the close pack indexed:
  - Epic acceptance-map viability turns from PASS to FAIL_TOOLING for HDE-EPIC021, HDE-EPIC027, HDE-EPIC028 and HDE-EPIC029 ("Human Evidence Index row 567 has unknown fields: ['crd_id']");
  - the qa lane's `tests/qa/test_epic021_acceptance_alignment.py::test_current_acceptance_inputs_are_strictly_viable` fails.
  - The close-pack pull request would not show this. It selects only the evidence and release lanes, so it would land green and leave the qa lane red for the next pull request that selects it.
- **The common cause** is one canon duty that two validators miss. HDE Schemas and Artifacts §8.3 allows `crd_id` and requires that "every serializer or validator enforcing this allowed-key set MUST accept crd_id". The updater and `ci/checks/check_mirror_schema.sh` do; the skeleton test and the harness do not.
- **The successor remedy** widens WU-REM-01 from one file to three. It adds R-4, one line in the skeleton test, and R-5, two lines in the harness. It extends V-1, V-2, V-3 and V-5 to the qa lane. P-1, R-1 to R-3 with C-1, and V-4 stay as approved. I rehearsed the whole change in throwaway clones, and every lane passes (§5).
- **One canon question** is recorded as CR-10 (PROPOSED). §8.3 also asks these validators to refuse a row that carries both `epic_id` and `crd_id`. No such row can reach them, so the remedy adds no check for it (§6.3).

The remedy changes no Specification boundary and no product intent, so it is within remediation authority (§10). This proposal approves nothing and creates no addendum, Plan, instruction, Proceed or work vehicle. It awaits Isis's ESC-40 decision (`ASK OK?`).

## 2. What changed from v1.0, and decision history

### 2.1 Decision history

| When (UTC, 2026-10-23) | Record | Actor | Outcome |
| :- | :- | :- | :- |
| 16:23 | Proposal v1.0 (#707) | Thoth, ESC-30 | REMEDIATION_PENDING: P-1, P-2, R-1 to R-3, V-1 to V-5 |
| 16:40 | Remediation review v1.0 (#708) and the 2.23 record | Isis, ESC-40 | APPROVE_AS_CHANGED: C-1 adds the close candidate source to R-3 and V-3 |
| 16:50 | WU-REM-01 instruction v1.0 (#709) | whole-change IA, PR-10 | INSTRUCTION_READY |
| 18:20 | WU-REM-01 PR plan v1.0 (#710) | WU-REM-01 PR session, PR-20 | BLOCKED on F-1: V-3 fails; V-3′ (one added line) passes |
| 19:25 | This proposal v1.1 | Thoth, ESC-30 | REMEDIATION_PENDING: F-1 and F-2 |

### 2.2 Item by item

| Item | v1.0 as approved (review v1.0 §4; 2.23) | v1.1 | Why |
| :- | :- | :- | :- |
| P-1 | Acceptance (5) restated | **Unchanged** | It is met once R-4 lands (§5.5, M3) |
| P-2 | WU-REM-01, one file | **Amended** (§6.1): three files, purpose and business case extended | F-1, F-2 |
| R-1, R-2 | As approved | **Unchanged** | PR-20's prototype meets them (plan v1.0 §7) |
| R-3 with C-1 | As approved | **Unchanged**. C-1 was already applied to the approved overlay and is carried word for word | — |
| R-4 | — | **New**: the skeleton test accepts `crd_id` | F-1 |
| R-5 | — | **New**: the harness accepts `crd_id` on Index and Mirror rows | F-2 |
| Limit | "No other file changes" | **Replaced**: "No file outside the three named files changes" | F-1, F-2 |
| V-1 | Evidence lane, root absent | **Extended**: also the qa lane and CI's changed-test step | R-5 selects them |
| V-2 | Evidence and release lanes, QA family present | **Extended**: also the qa lane | Later pull requests run it over that state |
| V-3 with C-1 | Evidence lane, close stage present | **Extended**: also the qa and release lanes, and an Epic viability comparison | F-2 |
| V-4 | Planted Index row fails the R-1 test | **Unchanged** | — |
| V-5 | Hosted evidence lane green | **Extended**: every selected lane and the changed-test step | R-5 |
| Exclusions | "No runtime, updater, harness or governed-evidence change" | **Amended**: the harness change is R-5 only | F-2 |
| Business case | QA evidence and close-pack PRs pass the evidence lane | **Extended** (§6.5) | F-2 |

Text not listed here is carried from v1.0 and from review v1.0 §4 unchanged.

## 3. Finding validation

### 3.1 The originating finding (unchanged)

FND-001 stands as v1.0 §2 validated it:
- the approved objective is S22, Constraints "QA evidence admission", and the QA requirement;
- the observed cause is six tests in `tests/evidence/test_evidence_index_missing_state.py` that assume the real checkout holds no HDE-CRD-0002 root;
- the real input is this change's own QA evidence and the hosted CI runner;
- the return owner is Isis, for the QA-10 reassessment of S22 and its dependants.

PR-20 reproduced it again at 16ecf95 (plan v1.0 §12.3, R0: 2 failed, 4 errors). F-1 and F-2 are delivery-stage evidence against the approved remedy for it, not new originating findings.

### 3.2 F-1

| Field | Validated value |
| :- | :- |
| Raised by | WU-REM-01 PR-20 plan v1.0 §16, from its rehearsal V-3 (§12.3) |
| Approved objective affected | P-1's clause "the evidence-lane tests do not depend on whether the real checkout holds … its close pack"; V-3's pass condition; the business case's close-pack benefit |
| Expected | With the close stage indexed, the evidence lane passes |
| Observed by PR-20 | 1 failed, 133 passed: `test_mirror_schema_and_parity`, `AssertionError: assert {'crd_id'} == set()` at line 539. With `"crd_id"` added to the test's optional set (V-3′): 134 passed |
| Observed in this diagnosis | Reproduced on a fresh stand-in close stage at f5c7c7f (§5.2): the same assertion at line 539 |
| Real input | Yes. The close-pack rows are what `_crd_close_pack_entries` (`tools/evidence/update_evidence_index.py` line 4046) writes for HDE-CRD-0002's close pack, a planned deliverable (Plan v1.1 WU-PR-07 (a); addendum 2.11 rule 4(a)). The hosted runner runs the test (rule 4(b)) |
| Within R-1 to R-3? | No: the test is in another file |

### 3.3 F-2 (found in this diagnosis)

| Field | Validated value |
| :- | :- |
| Found by | This ESC-30, while checking which other validators of the Index and Mirror key set read the real checkout (§4.3) |
| Approved objectives affected | Specification v1.1 Constraints, "QA evidence admission": "preserves existing Epic and HDE-CRD-0001 inputs (HDE Schemas & Artifacts §8.17)"; S22's "existing Epic and HDE-CRD-0001 inputs still publish and validate"; the business case's close-pack benefit |
| Expected | Indexing HDE-CRD-0002's close pack leaves existing Epic validation and every CI lane as they were |
| Observed | With the close stage indexed: 4 Epic acceptance maps change from PASS to FAIL_TOOLING; 3 more that already fail gain a `crd_id` reason; the qa-lane test `test_current_acceptance_inputs_are_strictly_viable` fails. Without the close stage, all of these are as on `main` (§5.3, §5.4) |
| Real input | Yes. The close-pack rows are a planned deliverable (rule 4(a)). The qa lane runs the failing test on the hosted runner for any pull request that selects the qa lane (rule 4(b)). The harness's Epic viability is an existing interface, used by `tools/qa/epic021_qa.py` and by the Epic close-pack generators |
| Why CI would not catch it in time | The close-pack pull request selects only the evidence and release lanes (§5.6). The qa lane would first fail on a later, unrelated pull request |

## 4. Diagnosis

### 4.1 F-1, proven cause

`test_mirror_schema_and_parity` (`tests/evidence/test_evidence_skeleton.py` lines 511 to 594; blob 057b4ae973ba) reads the real checkout's `artifacts/evidence_index.jsonl`. For every row it asserts `key_set - (required_fields | optional_fields) == set()`, with `optional_fields = {"epic_id", "notes", "record_type", "schema_version", "tokens"}`. The two CRD close-pack rows carry `crd_id`. The file was last changed before any CRD admission (PR-20 plan v1.0 §4).

### 4.2 F-2, proven cause

`tools/qa/qa_harness.py` (blob 4484408aa713; not a release member) defines two allowed-key sets without `crd_id`:
- `_HUMAN_INDEX_OPTIONAL_FIELDS` (line 233), used by `_load_evidence_graph` (line 791) to reject any Human Index row with an unknown key (lines 855 to 864);
- `_MIRROR_OPTIONAL_FIELDS` (line 230), used by `_mirror_record_error` (line 660) for every Mirror row.

`_load_evidence_graph` validates the **whole** Index and Mirror, not only the rows an acceptance map cites. `_EvidenceGovernanceValidator` (line 1059) calls it for every acceptance-map reference that a PF04 §2.0 token requires to be governed (`evaluate_acceptance_map_viability`, line 3467). So one `crd_id` row anywhere in the Index fails the viability of every Epic map with such a reference. QA-family and close-run rows carry no `crd_id`; only the close-pack rows do. That is why S22's QA root alone breaks nothing (§5.3, state Q).

### 4.3 Common cause, and the inventory

HDE Schemas and Artifacts §8.3, "Allowed top-level keys and unknown-key rejection", lists `crd_id` among the optional metadata keys. It states: "Before the first affected CRD enters QA, the Machine Mirror schema and every serializer or validator enforcing this allowed-key set MUST accept crd_id, enforce the epic_id/crd_id mutual-exclusion rule, and preserve valid historical and active epic_id records". WU-PR-07 made the updater write `crd_id` on CRD close-pack rows (S21). Two validators of the key set were not brought along.

Every repository surface that rejects unknown Index or Mirror keys, by search (§4.6):

| Surface | Accepts `crd_id` | Refuses `epic_id` with `crd_id` | Runs in |
| :- | :- | :- | :- |
| `tools/evidence/update_evidence_index.py` (`_ALLOWED_INDEX_FIELDS`, line 3745; `_normalize_index_entry`, line 3782) | Yes | Yes ("Index entry carries both epic_id and crd_id"); pinned by `test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together` | The sole writer; the evidence lane |
| `ci/checks/check_mirror_schema.sh` (line 19; `EPIC_CRD_EXCLUSIVE`, line 107) | Yes | Yes | The evidence lane |
| `tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity` | **No (F-1)** | No | The evidence lane |
| `tools/qa/qa_harness.py` `_load_evidence_graph` and `_mirror_record_error` | **No (F-2)** | No | Epic viability; the qa lane |

### 4.4 Correction to v1.0

v1.0 §3.2 recorded the updater and the harness as "not the cause, proven", and §3.3 recorded no open hypothesis bearing on the remedy. Both statements were true of the state I tested, a QA root without a close stage. I proved the close stage by reading only and left its execution to V-3. That is how F-1 reached PR-20 and how F-2 went unseen. In this successor every close-stage claim is executed (§5).

### 4.5 Hypotheses still open

None that bears on the remedy.

### 4.6 How the surface was searched

- **Validators:** `grep` over `tools/`, `ci/`, `scripts/`, `engine/` and `tests/` for allowed-key sets that name `epic_id`, and for unknown-key, unknown-field, extra-key or `ALLOWED_KEYS` rejection. The Index and Mirror rejections found are the four rows above. Two more rejections are for vendor log records, not Index or Mirror rows (`tools/evidence/generate_rails_gate_evidence.py`, `tools/evidence/generate_epic031_pr02_log_posture.py`). Other files name `epic_id` only to write it or to compare its value.
- **Tests that read the real Index or Mirror:** 25 files name `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`, `_load_human_index`, `_load_evidence_graph` or `evaluate_acceptance_map_viability`. Six are the evidence lane's files and one, `tests/evidence/test_release_attestation.py`, is the release lane's; the lane runs cover them. I ran the other 18 in both states, with `tests/qa/test_tooling_bootstrap.py` added so the qa lane's seven files are complete: 19 files (§5.3).

## 5. Reproduction and rehearsal evidence

### 5.1 Method

- **Where:** a throwaway clone of `main` at f5c7c7f under `/tmp/claude-0/-home-user-glow-hdengine-v2/6f0d7b39-d09c-5539-b3ea-d705c7417465/scratchpad/esc30/clone`, with git worktrees beside it. The clone has no remote; nothing was pushed and nothing from it enters the repository. Every tree ended with an empty `git status --short --untracked-files=all`.
- **Interpreter and install:** CPython 3.12.3 with CI's install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`); pytest 8.4.2. `PYTHONPATH` named the tree under test, as `ci.yml` does for its isolated steps.
- **Rails:** `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. No vendor, database or GitHub value reached any process.
- **Lane commands:** the steps of `.github/workflows/ci.yml`, run as written:
  - "Verify closed deterministic environment";
  - "Run governed evidence integrity lane" (lines 221 to 240): 7 validators and 6 pytest files;
  - "Run approved generic QA subsystem lane in isolation" (lines 242 to 271), in a detached worktree of the head, with its two tree checks;
  - "Run affected behavioral tests in isolation" for the classifier's changed-test targets;
  - "Build and verify exact-source release attestation" (lines 273 to 343);
  - the final `git diff --check`, `git diff --exit-code` and clean-status checks.
- **Stand-ins:** produced only through the harness and the canonical updater, plus authored files; each states "ESC-30 F-1 rehearsal stand-in in a throwaway clone; not QA evidence, a close pack or a close candidate":
  - QA family: `writer.publish_crd_check_family(qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT), …)` with checks `qa-01-standin` and `qa-02-standin`, each a `qa.CheckResult` with status `PASS` from an executed `python -c "raise SystemExit(0)"`, then `qa.validate_crd_check_family`;
  - close candidate source: authored at `audit/HDE-CRD-0002_close_candidate_source.json`;
  - close pack: `audit/HDE-CRD-0002_close_report.md` and `audit/HDE-CRD-0002_MANIFEST.json`, authored, then indexed by the updater's write;
  - close-run family: `writer.publish_crd_close_run_family(config, …)` with checks `close-pack-check` and `evidence-index-check`, then the updater's `--check`.
- **Clone-local commits:**
  - `cf9fc08`: PR-20's prototype diff (R-1 to R-3 with C-1) on f5c7c7f; the file's blob becomes 8c368caf3b42, as plan v1.0 §8 states;
  - `798626c` (state **Q**): the stand-in QA family, 16 paths;
  - `a7b4b97` (state **C**): the close stage, 19 paths. The Index and the Mirror then hold 627 rows each, 7 of them HDE-CRD-0002's; 2 carry `crd_id`, the close report and the manifest;
  - `2a5921b` (state **M1**): `cf9fc08` plus R-4 and R-5, with no HDE-CRD-0002 root. Against f5c7c7f this is exactly the proposed change: 3 files, +60/−27;
  - `f98d7cc` (state **M2**): Q plus R-4 and R-5;
  - `11f842f` (state **M3**): C plus R-4 and R-5 (§6.2).

### 5.2 F-1 reproduced

On state C: `check_mirror_schema.sh` exit 0, and `test_mirror_schema_and_parity` **1 failed** at line 539, as PR-20 recorded.

### 5.3 Tests that read the real Index, with and without the close stage

The 19 files of §4.6, each run alone. State Q is the QA family only; state C adds the close stage. Neither has R-4 or R-5.

| File | Lane | Q | C |
| :- | :- | :- | :- |
| `tests/qa/test_epic021_acceptance_alignment.py` | qa | 3 passed | **1 failed**, 2 passed: `test_current_acceptance_inputs_are_strictly_viable`, "Human Evidence Index row 567 has unknown fields: ['crd_id']" |
| `tests/qa/test_generic_qa_harness.py` | qa | 167 passed | 167 passed |
| `tests/qa/test_qa_harness_followup.py` | qa | 114 passed | 114 passed |
| `tests/qa/test_epic021_harness_entrypoint.py` | qa | 33 passed | 33 passed |
| `tests/qa/test_tooling_bootstrap.py` | qa | 2 passed | 2 passed |
| `tests/qa/test_viability_generator_wrappers.py` | qa | 87 passed | 87 passed |
| `tests/qa/test_epic029_requalification.py` | qa | 82 passed | 82 passed |
| `tests/evidence/test_rails_ci_workflow_integration.py` | rails | 138 passed | 138 passed |
| `tests/qa/test_generate_epic_close_pack.py` | none | 905 passed | 905 passed |
| `tests/evidence/test_hdapi_v2_contract_inventory.py` | none | 9 failed, 291 passed | the same 9 failed, 291 passed (OBS-2) |
| 9 other files (`tests/config/test_registry_report_indexing.py`, `tests/evidence/test_d23_evidence_index_snapshot_contract.py`, `…/test_engine_core_evidence.py`, `…/test_epic024_evidence_path_binding_validation.py`, `…/test_epic030_pr05_category_framework_evidence.py`, `…/test_evidence_index_snapshot.py`, `…/test_sanity_evidence_index.py`, `…/test_v2_mapped_cache_evidence.py`, `tests/qa/test_epic023_acceptance_alignment.py`) | none | 48 passed | 48 passed |

The close stage changes one result, the qa-lane test. Each tree was clean afterwards.

### 5.4 Epic acceptance-map viability, by state

A read-only probe (scratchpad `scripts/viability_probe.py`) calls `qa_harness.evaluate_acceptance_map_viability(HarnessConfig(<epic>, <tree>))` for each of the 16 `docs/acceptance_map_epic0NN.json`. The call publishes nothing.

| State | PASS | FAIL_TOOLING | Results naming `crd_id` |
| :- | :- | :- | :- |
| Q | HDE-EPIC021, 027, 028, 029 | 017, 019, 020, 022, 023, 024, 030, 033, 034, 035, 036, 037 | 0 |
| C | none | all 16 | 7: 021, 022, 023, 024, 027, 028, 029 |
| M3 (C with R-4 and R-5) | 021, 027, 028, 029 | the same 12 as Q | 0 |

M3 equals Q on all 16 statuses. The 12 maps that already fail in Q do so for reasons unrelated to this change, and this change does not touch them.

### 5.5 The proposed change, rehearsed

| ID | State | Validators (7) | Evidence lane, 6 files | qa lane, 7 files | Changed-test step | Release lane | Tree after |
| :- | :- | :- | :- | :- | :- | :- | :- |
| M1 | `2a5921b`: the full change, root absent (V-1) | all exit 0 | **134 passed** (696.4 s) | **488 passed** (18.4 s); worktree diff and status clean | `tests/qa/test_qa_tool_ownership.py`: 146 passed; worktree clean | not selected | clean (`git diff --check`, `git diff --exit-code`, empty status) |
| M2 | `f98d7cc`: the full change with the QA family (V-2) | all exit 0 | **134 passed** (673.2 s) | **488 passed** (16.7 s); worktree diff and status clean | — | **pass**: manifest check exit 0; 79 release tests passed; attestation built (exit 0) and verified (exit 0); tree clean | clean |
| M3 | `11f842f`: the full change with the QA family and close stage (V-3) | all exit 0 | **134 passed** (704.2 s) | **488 passed** (15.7 s); worktree diff and status clean | — | **pass**: manifest check exit 0; 79 release tests passed; attestation built (exit 0) and verified (exit 0); tree clean | clean |

- **Epic viability on M2 and M3:** the probe of §5.4 gives the same 16 statuses as state Q, and no result names `crd_id`. This is V-3 (b) as §6.4 states it.
- **What a WU-REM-01 pull request would run:** M1 is its head (V-1). M2 and M3 are the states a later QA-evidence pull request and a later close-pack pull request leave on `main` (V-2, V-3).

### 5.6 Classification and pre-push check

| Run | Result |
| :- | :- |
| `ci/checks/classify_ci_changes.py` as `ci.yml` calls it, base f5c7c7f, head `2a5921b` (the full change), `pull_request` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=evidence,qa`; `changed_tests=true`; one target, `tests/qa/test_qa_tool_ownership.py` |
| The same, base f5c7c7f, head `cf9fc08` (R-1 to R-3 only) | `paths=1;lanes=evidence`; `changed_tests=false` |
| The same, base `798626c`, head `a7b4b97` (what a close-pack pull request changes) | `paths=19;lanes=evidence,release`; `changed_tests=false`. The qa lane is not selected |
| `python tools/ci/prepush_check.py --base f5c7c7f --head HEAD lanes build-notes` on `2a5921b` | PASS; PF10 `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md`, 454,052 bytes, sha256 2759c4da…; "repository unchanged"; exit 0 |
| `prepush_check.py … --path` for each of the three files `membership` | PASS; all three not-member; exit 0 |

### 5.7 Negative controls

Each was run on a worktree of the close-stage state and restored with `git checkout`:
- **F-1 without R-4:** fails (§5.2). **F-2 without R-5:** fails (§5.3, §5.4).
- **V-4** (the R-1 test against a planted Index row) is PR-20's and stands (plan v1.0 §12.4).
- **Rehearsed, not proposed:** a variant that also refuses a row with both `epic_id` and `crd_id` (two more lines, §6.3). Its checks fired when a Mirror row and an Index row each had `"epic_id":"HDE-EPIC040"` planted beside `crd_id`:
  - the skeleton test failed at the new assertion;
  - `_load_evidence_graph` returned FAIL_TOOLING, "Human Index record must not carry both epic_id and crd_id".
  - Its full lane run was stopped when I chose the smaller variant. It completed only the 7 validators, all exit 0.

## 6. Proposed bounded remediation

### 6.1 Overlay on the immutable Implementation Plan v1.1

| # | Plan v1.1 anchor | Overlay |
| :- | :- | :- |
| P-1 | §7 WU-PR-02, "Acceptance and verification" item (5), last clause | **Unchanged** from review v1.0 §4: "an absent admitted HDE-CRD-0002 root publishes nothing, proven in a copy of the checkout from which that root and its Index rows are removed; the evidence-lane tests do not depend on whether the real checkout holds the HDE-CRD-0002 QA root, its close-run family, its close pack or its close candidate source". WU-PR-02's accepted delivery is unchanged; the new proof is delivered by WU-REM-01 |
| P-2 | §7, the unit after WU-OPS-01 and before QA-10 readiness | **Amended.** It replaces review v1.0 §4's P-2 as a whole, below |

**P-2. WU-REM-01 — Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation).** The title is unchanged, so existing records still name the unit.
- **Purpose:** let HDE-CRD-0002's QA evidence and close pack land without breaking the evidence lane, and keep the qa lane and existing Epic acceptance-map viability unaffected once the close pack is on `main` (FND-001; F-1; F-2).
- **Bounded scope:** S22, and S21's close-run tests and close-pack rows. Three files:
  - `tests/evidence/test_evidence_index_missing_state.py` (R-1 to R-3);
  - `tests/evidence/test_evidence_skeleton.py` (R-4);
  - `tools/qa/qa_harness.py` (R-5).
- **Dependencies:** none on unmerged work; it lands before QA-20.
- **Acceptance:** V-1 to V-5 (§6.4).
- **Evidence obligations:** the PR result record with the V-2 and V-3 rehearsal outputs, V-3's viability comparison included; no governed evidence change.
- **Business case:** §6.5.
- **Nonclaims:** no HDE-CRD-0002 QA evidence, close pack or close candidate source is produced or committed.

The Specification is unchanged (§10).

### 6.2 Required behaviour (PR-20 designs the code)

| # | File | Required behaviour |
| :- | :- | :- |
| R-1 | `tests/evidence/test_evidence_index_missing_state.py` | Unchanged from review v1.0 §4 |
| R-2 | same | Unchanged from review v1.0 §4 |
| R-3 (with C-1) | same | Unchanged from review v1.0 §4: `close_repo` removes `audit/qa/hde-crd-0002/` (including `close/`), `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and `audit/HDE-CRD-0002_close_candidate_source.json`, with their path proofs and Index rows, from the copy, then regenerates and checks through the canonical updater. The four close-run tests keep their assertions |
| R-4 | `tests/evidence/test_evidence_skeleton.py` | `test_mirror_schema_and_parity` accepts `crd_id` as an optional top-level Mirror key, as HDE Schemas and Artifacts §8.3 lists it. Nothing else in that file changes |
| R-5 | `tools/qa/qa_harness.py` | The evidence-graph validation accepts `crd_id` as an optional key on Human Index rows and on Machine Mirror rows. Nothing else in the harness changes: the required keys, the other metadata checks, the strict Epic predicates and the refusal of CRD viability stay as they are (HDE Mechanics Guide §1.6.3, "Explicit legacy Epic compatibility") |

**Limit.** No file outside these three changes. A shared helper, if any, stays in the file that uses it.

**The rehearsed lines for R-4 and R-5** substantiate the size of the change; they are not a design. PR-20 may write them differently within R-4 and R-5. The excerpt below is from the rehearsed diff (scratchpad `out/minimal_candidate.diff`: 29 lines, 956 bytes, sha256 efce8ff7393f3b45ef3dbad07d5ea3e608208f25257def2235135f3985897991), with context lines trimmed, so it is not meant for `git apply`:

```diff
--- a/tests/evidence/test_evidence_skeleton.py
+++ b/tests/evidence/test_evidence_skeleton.py
@@ -524,6 +524,7 @@ def test_mirror_schema_and_parity():
     optional_fields = {
+        "crd_id",
         "epic_id",
--- a/tools/qa/qa_harness.py
+++ b/tools/qa/qa_harness.py
@@ -228,10 +228,11 @@ _MIRROR_REQUIRED_FIELDS = frozenset(
 _MIRROR_OPTIONAL_FIELDS = frozenset(
-    {"epic_id", "notes", "record_type", "schema_version", "tokens"}
+    {"crd_id", "epic_id", "notes", "record_type", "schema_version", "tokens"}
 )
 _HUMAN_INDEX_OPTIONAL_FIELDS = frozenset(
     {
+        "crd_id",
         "epic_id",
```

**No new committed test is required for R-4 or R-5.**
- R-4 is itself a test, and V-3 shows its effect.
- For R-5, V-3 shows the effect on the close-stage state. Once the close pack is on `main`, the qa lane's `test_current_acceptance_inputs_are_strictly_viable` exercises it on every qa-lane run.
- A further test is PR-20's design choice, made only for a condition these leave unprotected (addendum 2.11 rule 2).

### 6.3 Stated limit: a row with both `epic_id` and `crd_id`

R-4 and R-5 add no check for a row that carries both keys. No such row can reach either validator:
- the canonical updater, the sole writer, refuses it ("Index entry carries both epic_id and crd_id"), pinned by `test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together`;
- `ci/checks/check_mirror_schema.sh` rejects it (`EPIC_CRD_EXCLUSIVE`) on every evidence-lane run, so even a hand edit cannot pass the evidence lane.

Under addendum 2.11 rule 5, a check for it in these two validators would model a constructed input: "An input outside the real set gets one refusal or a stated limit, never a model of it". HDE Schemas and Artifacts §8.3 asks every validator of the key set to "enforce the epic_id/crd_id mutual-exclusion rule". CR-10 (§13) records that tension, with its proposed disposition, for Isis's decision. If Isis decides otherwise, the two lines are rehearsed (§5.7).

### 6.4 Verification

| # | Check | Pass condition |
| :- | :- | :- |
| V-1 | Local, on the PR head (root absent) | The 7 evidence-lane validators exit 0. The six evidence-lane pytest files pass with no fewer than 134 tests. The qa lane's seven files pass with its two tree checks. The changed-test targets the classifier selects pass in isolation (today `tests/qa/test_qa_tool_ownership.py`). All exactly as `ci.yml` runs them |
| V-2 | Rehearsal in a throwaway clone of the PR head, with a stand-in HDE-CRD-0002 QA family published by the harness and the canonical updater | The evidence, qa and release lanes pass, exactly as `ci.yml` runs them |
| V-3 (with C-1) | The V-2 clone, also holding a stand-in close-run family, the two close-pack files and the close candidate source, indexed by the canonical updater | (a) The evidence, qa and release lanes pass, exactly as `ci.yml` runs them. (b) For each `docs/acceptance_map_epic0NN.json`, `evaluate_acceptance_map_viability` returns the same status as in the V-2 state, and no result names `crd_id` |
| V-4 | Negative control | Unchanged: the R-1 test fails when an Index row under `audit/qa/hde-crd-0002/` is planted in its copy |
| V-5 | Hosted CI on the PR head | Every lane the classifier selects (today evidence and qa) and the changed-test step are green, and the run ends `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |

Nothing from a rehearsal clone is committed. The checks still cover the triage's required resolution evidence: (1) by R-1 to R-5 on `main` after merge, checked at PR-40; (2) by V-5; (3) by V-2 and V-3.

### 6.5 Business case (addendum 2.11 rule 1, as addendum 2.18 narrows it)

| Field | Content |
| :- | :- |
| Beneficiary | QA (Kronos) and the Product Owner: HDE-CRD-0002's QA evidence and close pack can be published through ordinary CI. Every later pull-request session that selects the qa lane: it is not failed by HDE-CRD-0002's close pack. Users of the harness's Epic acceptance-map viability (`tools/qa/epic021_qa.py` and the Epic close-pack generators): it keeps its results |
| Evidence | v1.0 §4 (six evidence-lane tests break with the root present). PR-20 plan v1.0 §12.3 (V-3: one more break with the close stage). §5.3 and §5.4 here (the qa-lane test and four Epic viabilities break with the close stage) |
| Benefit | QA-20 and QA-50 can proceed. The first QA-evidence pull request and the close-pack pull request are not blocked by the evidence lane. The close pack does not leave the qa lane red or Epic viability failing for later work |
| Measure | (1) Unchanged: the first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests. (2) New: the close-pack pull request passes the evidence lane, and the first qa-lane run on `main` after it passes, with no change to these three files. Neither is observable at WU-REM-01's PR-40; PR-40 records V-2 and V-3 as their proxy and the measure as "not yet measurable" (addendum 2.18 rule 5) |

There is no cost ceiling (addendum 2.18 rule 1). This is not CI or canon conformance for its own sake (rule 2): each added line answers an observed failure on a real input.

## 7. Affected surfaces

| Area | Effect |
| :- | :- |
| Requirements | S22 becomes achievable on the real root. S21's close-run tests stop depending on the real checkout, and its close-pack rows stop failing a validator. No other requirement is affected |
| Dependencies | QA-10 reassessment, QA-20 and QA-50 wait on WU-REM-01; so does the close-pack pull request at closure. The WU-REM-01 instruction v1.0 needs a new version (§11) |
| Tests | Two test files (R-1 to R-4). No new test file |
| Tooling | `tools/qa/qa_harness.py` (R-5). Not a release member; not runtime |
| Ops | None |
| Documentation | None. HDE Mechanics Guide §1.6.3 and HDE Schemas and Artifacts §8.3 already describe the intended behaviour |
| CI | WU-REM-01's pull request runs the evidence and qa lanes and the changed-test step (§5.6) |
| Release identity | Unchanged; no release member is touched (`membership`: all three not-member) |

## 8. Preserved bases, overlays and exclusions

- **Preserved unchanged:**
  - Specification v1.1-approved with Specification delta 01 (addendum 2.20);
  - Implementation Plan v1.1 and its review v1.1, with Plan delta 01 v1.1 (addendum 2.19);
  - the Implementation Audit v1.0;
  - every accepted work unit: WU-PR-02 stays accepted-final (addendum 2.5), and WU-PR-07 stays accepted (addendum 2.16). R-4 and R-5 are prospective work in WU-REM-01; they reopen neither unit;
  - review v1.0 and the 2.23 record, as issued.
- **Overlays:** if this is approved, P-1 as approved and the amended P-2, with R-1 to R-5 and V-1 to V-5 as stated here. They replace the overlay of review v1.0 §4 for WU-REM-01.
- **Exclusions:**
  - no runtime or updater change, and no harness change beyond R-5;
  - no regeneration or hand edit of governed evidence (Index, Mirror, sentinels, path proofs, orientation);
  - no new evidence family;
  - no HDE-CRD-0002 QA evidence, close pack or close candidate source produced or committed;
  - no Specification boundary or product-intent change;
  - no re-run of an accepted-final pull request;
  - the 12 Epic acceptance maps that already fail viability on `main` are not repaired (OBS-1).
- **Not in scope:** FND-024 (the PR35-C1 flake risk on QA-evidence pull requests) stays with its recorded owner.

## 9. Risks

| Risk | Treatment |
| :- | :- |
| R-5 widens what the harness accepts | Only `crd_id`, which canon allows, on Index and Mirror rows. Required keys and every other check stay. On `main` today no row carries `crd_id`, so R-5 changes no result until the close pack lands (§5.4, Q equals M3) |
| A row with both keys is accepted by the two validators | It cannot reach them (§6.3). The sole writer and the evidence lane's schema check refuse it |
| The fixtures strip more than intended | Unchanged from v1.0 §8: only named paths and their rows leave, the updater regenerates and checks, and V-4 keeps the absent-root property detectable |
| Lane time | R-4 and R-5 add no test. PR-20 measured R-1 to R-3 within noise (plan v1.0 §12.3). The qa lane, which WU-REM-01's pull request now also selects, took 16 to 19 s here (§5.5) |
| A later CRD repeats the defect | R-2 iterates `ADMITTED_CRD_QA`. R-4 and R-5 accept `crd_id` for any CRD |
| A Codex finding on a constructed input, for example the both-keys row | Addendum 2.11 rule 7: traced path and stated limit (§6.3) |

## 10. Authority: within remediation, not a Specification change

- **Product intent:** unchanged. S21 and S22 keep their intents. R-4 and R-5 serve S22's "existing Epic … inputs still publish and validate" and its Constraint "preserves existing Epic and HDE-CRD-0001 inputs".
- **Specification boundary:** unchanged.
  - No Specification exclusion names the QA harness.
  - The Specification's impact classes include "close-pack tooling and evidence-index tooling" among non-production-affecting surfaces.
  - Plan v1.1 WU-PR-07 (T5) already places a `tools/qa/qa_harness.py` change "inside S21's bound".
- **The approved remedy's exclusion** "No runtime, updater, harness or governed-evidence change" is an overlay term, not a Specification term. Changing it is Isis's ESC-40 decision, which is why this is ESC-30 → ESC-40 and not RS-20 (instruction v1.0 §14).
- **Materiality:** material under IA-30's definition as used for the remediation review (review v1.0 §2): it changes an approved work unit's scope and acceptance. It therefore qualifies for an addendum if approved.

### Alternatives considered

| Option | Assessment |
| :- | :- |
| (a) WU-REM-01 carries R-4 and R-5 (this proposal) | One vehicle and one lineage. The rehearsal already exercises the close stage. Both defects are closed before QA entry, as §8.3 asks |
| (b) R-4 in WU-REM-01; F-2 as a separate remedy before the close stage | A second full lineage (ESC-40, PR-10, PR-20, Proceed, PR-30, PR-35, PR-40) for two lines. Until then, §8.3's duty stays unmet in the harness. Not recommended |
| (c) Narrow V-3 and P-1, and defer both | Leaves the close-pack pull request failing the evidence lane. It fails the approved business case. Rejected |
| (d) The updater stops writing `crd_id` on close-pack rows | Reverses WU-PR-07's accepted design and changes the sole writer. The harness would still fail §8.3's duty. Rejected |

## 11. Delivery and return map

1. **ESC-40**, Isis: APPROVE, APPROVE_AS_CHANGED or DENY. A qualifying approval writes one HDE Build Notes addendum recording the amended overlay.
2. **PR-10** — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), by the whole-change Implementation Agent, for `WORK_UNIT_ID: WU-REM-01`. It issues the instruction v1.1 under the amended overlay. Instruction v1.0's §4 Limit, §6 bounded files and §7 exclusions no longer match the remedy, so PR-20 cannot plan against v1.0.
3. **PR-20**, in the same dedicated WU-REM-01 PR session (https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5): the successor plan. It reuses plan v1.0 §5 to §15 where they stay valid (plan v1.0 §1, "What is preserved").
4. **Then the ordinary unit lineage:** Product Owner Proceed → PR-30 → PR-35 → Nathan's merge → PR-40 lineage review.
5. **Return:** the same Isis, QA-10 reassessment of S22 and its dependants, after PR-40 ACCEPT.

`PR_RETURN_PHASE`: not applicable. WU-REM-01 has no Proceed and no pull request. The change goes back before PR-20 through a new instruction version, not through RS-40.

## 12. Unresolved items and owners

| Item | Owner |
| :- | :- |
| The ESC-40 decision on this proposal, including CR-10 | Isis |
| WU-REM-01 instruction v1.1 | Whole-change Implementation Agent (PR-10) |
| WU-REM-01's code design and successor plan | PR-20 in WU-REM-01's PR session |
| Publication into PF10 of 2.23 and of any addendum for this proposal | Product Owner |
| CR-9 (PROPOSED; WU-OPS-01 Plan-text conflict), unaffected | Isis (IA-30) |
| FND-024 (PR35-C1 flake risk on QA-evidence pull requests) | As recorded in the triage |
| The business-case measures (§6.5) | The first QA-evidence pull request, the close-pack pull request and the next qa-lane run, or the QA-10 reassessment |
| The QA-10 reassessment of S22 and its dependants | Isis, after WU-REM-01's PR-40 ACCEPT |
| The failing tests of `tests/evidence/test_hdapi_v2_contract_inventory.py` (OBS-2) | Not this change's. Reported for the Product Owner's triage |

## 13. Canon conflict register

**Carried unchanged** (readiness record §6; review v1.0 §7):
- CR-1, CR-2 and CR-3: APPROVED_AS_CHANGED (Thoth);
- CR-4: APPROVED, and CR-5: APPROVED_AS_CHANGED (Product Owner);
- CR-6: APPROVED, alternative (a) (Implementation Agent through RS-20);
- CR-7 and CR-8: APPROVED, alternative (a) each (Product Owner);
- CR-9: PROPOSED, not yet reviewed (Isis at IA-30), unaffected.

**New entry:**

| Field | Value |
| :- | :- |
| ID | CR-10 |
| Classification | CANON_RECONCILIATION: an earlier PF rule against a PF10 rule |
| Sources | HDE Schemas and Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`, blob 1542a8f78846) §8.3, "Allowed top-level keys and unknown-key rejection": "every serializer or validator enforcing this allowed-key set MUST accept crd_id, enforce the epic_id/crd_id mutual-exclusion rule, and preserve valid historical and active epic_id records". PF10-HDE-Build-Notes v13.7.5 addendum 2.11 rules 4 and 5, with 2.18 rule 6 keeping them: "An input constructed only to exercise code justifies no requirement, design element, test, fix or blocking finding. An input outside the real set gets one refusal or a stated limit, never a model of it" |
| Conflict | R-4 and R-5 make two validators of the key set accept `crd_id`. Read literally, §8.3 then requires each of them also to refuse a row with both keys. That row is not a real input to them: the sole writer refuses it and the evidence lane's schema check rejects it (§6.3). Rule 5 forbids a design element for it |
| Affected requirements | S21 and S22, through R-4 and R-5 |
| Alternatives | (a) Rule 5 governs, as PF10's precedence and 2.11's own scope ("Where this addendum conflicts with earlier PF-Canon …, this addendum governs") provide. The mutual-exclusion rule is enforced where a both-keys row can arise, at the writer and at the Mirror schema check. R-4 and R-5 accept `crd_id` only, with the stated limit of §6.3. (b) §8.3 read literally: each validator also refuses the row. Two more lines, rehearsed (§5.7) |
| Recommended disposition | (a) |
| Interim treatment | (a), as proposed in §6.3 |
| Unresolved risk | None on a real input |
| Permanent drainage target and owner | HDE Schemas and Artifacts §8.3: state that the mutual-exclusion rule is enforced by the canonical writer and the Machine Mirror schema check, and that other validators of the key set need only accept `crd_id`. Owner: the Product Owner, by a later HDE Build Notes addendum or permanent canon revision. Unperformed |
| Status | PROPOSED |
| Reviewer and reviewed artifact | Isis, ESC-40, on this proposal v1.1. Not yet reviewed |
| Decision time and rationale | — (unreviewed) |
| Original proposal and history | This proposal v1.1 (Thoth, ESC-30, 2026-10-23); first raised as an open choice in WU-REM-01 PR-20 plan v1.0 §16 ("Whether to include it is the proposal author's") |

## 14. Observations (no action in this remedy)

- **OBS-1, Epic viability already failing on `main`.** Without HDE-CRD-0002's close stage, 12 of 16 Epic acceptance maps already return FAIL_TOOLING through the harness (§5.4, Q). Their reasons do not involve `crd_id`, and this remedy neither causes nor repairs them.
- **OBS-2, a test file failing on `main`.** `tests/evidence/test_hdapi_v2_contract_inventory.py` has the same 9 failures in states Q and C, so they predate HDE-CRD-0002's evidence. No CI lane runs the file. `AGENTS.md` records that HDE-EPIC033 to HDE-EPIC037 evidence generators have stale `--check` results on `main`; I did not trace these 9 further.
- **OBS-3, the identifier collision.** As PR-20 noted (plan v1.0 §16, OBS-4), "FND-001" here is QA-10's finding (triage §3), not the WU-OPS-01 receipt's finding of addendum 2.22.

## 15. TypeSafe reading for the receiving session (ESC-40)

Action sent (v8.2): "Review, as the independent integrated-remediation reviewer, a successor remediation proposal that amends a remedy you approved once with one change: the planner's rehearsal showed the approved one-file test fix cannot meet its own acceptance, and the remediation author's diagnosis found a second, related defect, so the successor widens the work unit from one test file to three files (one line in a second evidence test and two lines in the QA harness's index-row key validation), with every check already rehearsed in throwaway clones and one proposed canon-conflict entry; decide approve, approve as changed or deny, and on approval write one standalone build-notes addendum and route to a re-issued work-unit instruction. It is a read-only review of Markdown records against canon and the repository: no code is written and no live run occurs; a re-issued instruction, a pull-request plan and implementation with their own reviews, and a readiness reassessment follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.27 (confidence 0.77); rung probabilities low 0.00, medium 0.04, high 0.66, extra high 0.28, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.97, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.96). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.013, Fable 5.1 at extra high 0.006, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.039, Opus 5.5 at high 0.640, Opus 5.5 at extra high 0.272, Opus 5.5 at max 0.010, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.007, Sonnet 5.5 at extra high 0.003, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-23T19:01:21Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-23T19:01:21Z; HTTP 200 in 0.56 s; 5540 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Records:** run once with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `review`, before this record was saved. The Notion row was not written (ESC-30 handoff rule; addendum 2.1). Nathan's pick for ESC-40 is not stated. Nathan's pick for this ESC-30 session is not stated; its reading is in PR-20 plan v1.0 §21.

**Surface advice:** run ESC-40 in the continuing Isis session for HDE-CRD-0002, or a top-level Claude Code cloud session Nathan creates for that role, on `amthorn78/glow-hdengine-v2` with Notion read access.
- **Reads:**
  - this proposal (§3 to §6, §10, §13); review v1.0 and the 2.23 record; PR-20 plan v1.0 §12 and §16;
  - `tests/evidence/test_evidence_skeleton.py` lines 511 to 545; `tools/qa/qa_harness.py` lines 219 to 260, 578 to 690, 791 to 960 and 1059 to 1160; `tests/qa/test_epic021_acceptance_alignment.py`; `ci/checks/check_mirror_schema.sh`;
  - `docs/pfcanon/`: HDE Schemas and Artifacts §8.3, HDE Mechanics Guide §1.6.3, and current PF10 (2.11, 2.18).
- **Re-running a rehearsal (optional):** a throwaway clone with CI's install, Python 3.12 and closed rails through `env -i`. The read-only viability probe and the single-test reproductions take under two minutes each. A full evidence-lane run took 12 minutes here and about 17 minutes in PR-20's session, on 4 CPUs; the qa lane about 20 s.
- **Writes:** only its review and any addendum, under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this proposal's pull request is merged first.

## 16. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | `GCFPE-USE-HDE-CRD-0002-ESC-30-20261023-FND-001-02` |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| requirement / work unit | S22, with S21's close-run tests and close-pack rows; WU-REM-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9 (page state as of 2026-10-12T02:29:51.552Z) |
| role/stage | continuing Thoth, ESC-30 (second proposal for FND-001) |
| capture time | 2026-10-23T19:25:00Z |
| execution identity | https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum |
| result | REMEDIATION_PENDING (proposal v1.1); next ESC-40 |
| inherited usage | proposal v1.0 (ESC-30, FND-001 proposal 1); review v1.0 (`GCFPE-USE-HDE-CRD-0002-ESC-40-20261023-FND-001-01`); instruction v1.0 (`GCFPE-USE-HDE-CRD-0002-PR-10-20261023-WU-REM-01-01`); plan v1.0 (`GCFPE-USE-HDE-CRD-0002-PR-20-20261023-WU-REM-01-01`) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); recorded here only |

## Canon relied on

Read on `main` at f5c7c7f (`docs/pfcanon/` last changed by 39122b7; PF10 v13.7.5). Each source maps to the decision topics it governs.

| Decision topic | Sources and sections |
| :- | :- |
| This prompt's contract: inputs, `AUTHORING_CONTEXT`, a successor after a decision, no product-intent change, no Plan, vehicle, Proceed or addendum, routing | ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, fetched and read in full in this invocation ("Required inputs", "Execute" 1 to 6, "Required result", "Result routing", "Carried conflict and decision lineage") |
| The approved remedy and what this successor amends | `docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md`, read in full (§2 to §7; §4 the overlay); the 2.23 record, read in full; proposal v1.0, read in full |
| The delivery-stage finding and the route for a change to the remedy | WU-REM-01 PR-20 plan v1.0, read in full (§1, §4, §5, §11, §12, §16, §20), with its prototype diff (`git apply --check` clean on f5c7c7f); WU-REM-01 instruction v1.0, read in full (§4 Limit, §6, §7, §14: "Changes to the approved remedy itself belong to Isis through ESC-30 and ESC-40, not to RS-20") |
| PF10 authority; business case; real inputs; finding disposition; no ceiling | PF10-HDE-Build-Notes v13.7.5: addendum 2.11 (rules 1 to 8, "Scope and supersession"), read in full in this invocation; addendum 2.18 ("Rule" 1 to 6, "Scope and supersession"), read in this invocation; its heading index 2.11 to 2.22 checked; 2.23 is not in the file (0 matches). Addenda 2.5 (WU-PR-02 accepted-final), 2.16 (WU-PR-07 accepted) and 2.19 and 2.20 (the deltas in force), as cited by the inputs |
| The Mirror and Index key set (F-1, F-2, CR-10) | HDE Schemas and Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.3, "Bundle-aware extension" and "Allowed top-level keys and unknown-key rejection", read in full |
| The harness's Epic viability and what it must preserve (F-2, R-5) | HDE Mechanics Guide (`PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §1.6.3 "Generic Epic/CRD QA harness (local records, governed publication, legacy viability)": "Identity and local recording", "Current-family validation and publication", "Explicit legacy Epic compatibility" ("Preserve the existing Epic logic and strict predicates") and "Closed-rails regression responsibilities" ("Preserve strict legacy Epic viability"), read |
| What viability gates | Glow QA Guide (`PF19-Canon-Glow-QA-Guide-v3.0.6.md`), "Acceptance-map / QA-plan viability check (names-only)", read in full (a FAIL_TOOLING viability report stops dependent Live QA) |
| The objective, its boundary and the harness's place in it | Specification v1.1-approved: S21 and S22 rows, "Exclusions", "Constraints" ("QA evidence admission"), the affected-surfaces line, the production-effect classes, CD-3; Implementation Plan v1.1 §7 WU-PR-07 (T5: a harness change "inside S21's bound") |
| Evidence writer and CI rules | `AGENTS.md`: canon-first rule; closed rails; pytest readiness; pre-push check; "Governed evidence rules" (sole writer; no hand-editing); QA output placement; "Code review guidelines" (real-input rule); "Evidence attribution, currentness and distinct decisions" |
| Repository facts | `tests/evidence/test_evidence_skeleton.py` lines 500 to 600; `tools/qa/qa_harness.py` lines 219 to 260, 578 to 700, 791 to 960, 1059 to 1160, 2522 to 2560, 2763 to 2940, 3467 to 3535 and 3914 to 3925; `tools/evidence/update_evidence_index.py` lines 3745 to 3790, 4040 to 4100 and 5166 to 5260; `ci/checks/check_mirror_schema.sh` lines 15 to 130; `tests/evidence/test_evidence_index_missing_state.py` lines 1238 to 1260; `tests/qa/test_epic021_acceptance_alignment.py` lines 95 to 112; `.github/workflows/ci.yml` lines 55 to 343; `catalog/manifest.json` member list (no `tools/qa/` member) |

Canon searched (`git grep -n -i` on `origin/main -- docs/pfcanon/`) for `crd_id` (with its escaped form `crd\_id`) and `viability`:
- `crd_id` appears in HDE Schemas and Artifacts §8.3 (read above), in HDE Mechanics Guide §1.6.3 (`HarnessConfig`, read above) and in an HDE CRD Records template heading, which does not bear on key sets.
- `viability` appears in HDE Governance, CLI/API/Vendor Ref, the Change Process Guide, the Build Checklists, HDE Schemas and Artifacts, HDE Mechanics Guide and the Glow QA Guide. The sections read above govern the harness's viability behaviour; the other hits name historical Epic viability logs.

ASK OK?
