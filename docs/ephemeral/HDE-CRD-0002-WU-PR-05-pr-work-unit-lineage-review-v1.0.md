---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-05-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: ACCEPT
predecessor: none (the first PR-40 review of WU-PR-05)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-05
work_unit_title: "Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation; S19)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob ee5acb997fcc; landed by #654 as 1e97ba9)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md (v1.0; Proceeded; spent; blob 54809ffbaf34; landed by #655 as 8170cd8) with companion docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0-prototype.diff (blob a73ef64f9d1f)
S19_RECORD: docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md (v1.0, RECORDED; blob 016e74e557ee; 52,542 bytes; landed by #656)
PR_30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED; blob 20b170490447)
PR_35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.2.md (MERGE_PENDING; historical pre-merge evidence; blob c6643708a3af), with its checkpoint docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.1.md (blob 2a1aebbc4c13)
PR_REFS: amthorn78/glow-hdengine-v2#656 (the only pull request of this work unit; merged as 822ce15)
entry_event: Nathan's manual-merge assertion for #656, given in the PR-40 fallback handoff because no MERGE_OBSERVED result was returned for this merge (NOT PRODUCED). The handoff also stated that CI run 39169173040 and the Codex code review on f7d610e completed clean after result v1.2 was saved. The merge and both facts were verified independently (§3, §4)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role; session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (author of the WU-PR-05 instruction; not an author of the plan, code, S19 record or results reviewed here)
pr_sessions: PR-20 and PR-30 https://claude.ai/code/session_01FtgUXCdmFGLWASrRUWaDjc; PR-35 https://claude.ai/code/session_01UxcGLTM7Z2RFQLHeg8szTB
approved_lineage: Specification docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1); Implementation Audit docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0); Implementation Plan docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1); Plan review docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
overlays: PF10 addenda 2.3 (review chain), 2.5 (LR-O1 to LR-O3), 2.6 (22-path roster; step 3b), 2.7 AD-4 (the four non-public-route gaps decided in S19) and AD-5 (refresh base and restart rules), 2.8 and 2.9 (WU-PR-03 and WU-PR-04 acceptances and their carried items); none created for this unit
return_owner: the same continuing whole-change HDE-CRD-0002 Implementation Agent
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state as of 2026-10-12T02:29:38.234Z; read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-18T22:39:08Z
repository_state_reviewed: origin/main 822ce15 (tree 3f265d762110); no commit after it at review time
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md (v13.6; blob f6f80d8779e8; 167,152 bytes; sha256 4ecdd9caf9dc172ecb07ab0c577b400ca7a96cc18cef4421448b99dd94fe28aa; docs/pfcanon/ unchanged since 86e002c). This IA session read it at PR-10 for this unit: the complete v13.5.9→v13.6 diff, addenda 2.9, 2.7 and 2.3 in full, with 2.6, 2.5's retained decisions and 2.8 read earlier the same day and byte-unchanged (instruction front matter). The file is byte-unchanged since (same blob and SHA-256), so this review relies on that reading
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1 to CR-8 carried; no new entry (§9)
next_prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), for WU-PR-06
---

# HDE-CRD-0002 WU-PR-05 — PR work-unit lineage review v1.0 (PR-40, #656)

## 1. Decision

**ACCEPT.** WU-PR-05 is delivered, with sufficient attributable evidence, by its one pull request, #656.
- **S19 record.** `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` covers the 49 paths of Audit Appendix B. Each path has a per-file line, and each line's blob equals the path's blob at the reviewed head `1e97ba9` (§5 item 10). The record contains:
  - the threat checklist and the severity scale;
  - nine confirmed findings fixed here (S19-F01 to S19-F09; two Medium, seven Low);
  - seven confirmed findings routed to the Product Owner with reasons (S19-R01 to S19-R07);
  - the named inputs of instruction ID-6 and ID-7;
  - the out-of-scope observations of ID-8;
  - the route-policy statement.
- **Fixes.** Each fix has `test_s19_*` regression tests in the module that owns its source: 267 at PR-30, plus one for CX5-1. Each also has a negative control. The fixes land exactly as the Proceeded plan's companion diff states.
- **Release refresh.** The same-version refresh at `1.3.0` gives `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (45 members). Admission accepts it on merged `main`.
- **Code review.** The one Codex finding (CX5-1, P2, the S9 ingest runner's logs) was corrected before the merge and re-reviewed clean.
- **CI and this review's checks.** Hosted CI passed on the final head across all seven lanes. This review's runs on merged `main` confirm the landed state (§5).

ACCEPT is this review's lineage result only. It is not QA, acceptance of HDE-CRD-0002, Ops, deployment, release activation, PF09 or PF30 movement, or closure. Each fixed surface's Live QA class (S19 record §4) belongs to the QA Plan.

## 2. Inputs read

- **In full, in this invocation:**
  - the PR-40 prompt;
  - plan v1.0 (all sections, "Canon relied on" and "Checks run");
  - the S19 record v1.0;
  - results v1.0, v1.1 and v1.2.
- **Authored by this IA and re-read for the decisions that depend on it:** instruction v1.0: §4 ID-1 to ID-11, §6, §8, §10, §14 and §15.
- **Companion diff.** Compared with the landed source commit `d0f25b6` (§3).
- **Approved lineage, re-read where a decision depends on it:**
  - Specification v1.1: S19, Exclusions bullet 6;
  - Implementation Plan v1.1: §7, "Common to every PR unit", the WU-PR-05 and WU-PR-06 blocks; §9; §10; R-5;
  - Audit §6 S19 and Appendix B (path list compared with the record, §5 item 10).
- **GitHub, read directly:**
  - #656 metadata, its seven commits and its single check run;
  - the final head's job log, read whole by a programmatic scan. It has 913 lines; the saved copy is 73,675 bytes with SHA-256 `20046b03…`. It begins with the runner start and ends after the post-job cleanup, and its line count equals the API's `original_length`, so it is not truncated;
  - the one review thread, both formal reviews and the Codex summary comment.
- **Code on `main`, read:**
  - the landed diffs of the eight hand-edited sources and of `scripts/ingest/run_vendor_ingest.py` and `ci/checks/classify_ci_changes.py`;
  - `adapter/http_reader.py`'s production mount (`_production_posture`, `_mount_for_production`, `_refuse_in_production`) and `_dev_admin_gate`;
  - the added test cases' names and hosts.

## 3. Merge state and landed lineage

| Item | Fact |
| :- | :- |
| Pull request | #656, merged=true, merged by amthorn78 at 2026-10-18T22:13:49Z. Base `main` `8170cd8eb36b`; head branch `ccr-ee766f88-s47rkh` at `f7d610e6740b`. 7 commits; 83 files (+1,796/−151) |
| Commits, in order | PR-30: `d0f25b6` source, 21 hand-edited paths; `176de33` owner-produced re-cut and convergence, 56 paths; `173bf97` S19 record; `faf7b2b` result v1.0. PR-35: `ef3cda5` CX5-1 correction, 3 paths; `c60ba38` result v1.1; `f7d610e` result v1.2. Each commit has one parent, the previous commit; `d0f25b6`'s parent is `8170cd8` |
| Squash | `822ce15`, one parent `8170cd8` (the pull request's base). `822ce15^{tree}`, `f7d610e^{tree}` and `3f265d762110` are equal. `git diff 8170cd8 f7d610e` and `git diff 8170cd8 822ce15` have the same SHA-256 (`642c8abe…`) |
| Changed set | 83 paths: 4 added (the S19 record and results v1.0 to v1.2), 79 modified. The 79 modified paths are exactly: <br>• the 21 paths of plan §8.1 (eight sources, 13 existing test hosts); <br>• the 56 owner-produced paths of plan §9 (the manifest, the file holding `FROZEN_OPEN_ABBA_SHA256`, evidence primaries with the Index and Mirror, and their path proofs); <br>• the two PR-35 paths of IF-35-2 and IF-35-3 (`scripts/ingest/run_vendor_ingest.py`, `ci/checks/classify_ci_changes.py`). `tests/bodygraph/test_ingest.py`, the third path of `ef3cda5`, is already among the 21 |
| Source versus the plan's companion diff | `d0f25b6`'s diff from `8170cd8` equals the companion diff byte for byte (SHA-256 `5081ded3…`). No in-flight decision at PR-30 (result v1.0 §11: NONE) |
| Release refresh | `catalog/manifest.json` re-cut at `1.3.0`, `2026-08-24T18:04:49Z`, with `--roster-from-admission`: `release_id` `2f18a5eb…` → `77204764…`. `FROZEN_OPEN_ABBA_SHA256` changes in one line, `9949ddf5…` → `e8a47d53b4d9a145ebfc95163a85252c15a4fbddb12dc9dea380662aaa1cb73c`. The 56-path set equals plan §9's list. The admission constants are unchanged |
| Plan §8.3 expected-unchanged paths | The changed set meets the §8.3 list and the frozen families only at `ci/checks/classify_ci_changes.py` (IF-35-3; LR5-O2 in §7). All other listed paths have an empty diff, including:<br>• `adapter/factory.py`, `adapter/wsgi.py`;<br>• `engine/bodygraph/vendor_client.py`, `engine/bodygraph/vendor_audit.py`, `engine/compat/**`;<br>• `.github/workflows/ci.yml`, `requirements*.txt`, `pyproject.toml`;<br>• `tools/evidence/update_evidence_index.py`;<br>• `artifacts/vendor/**`, `artifacts/cli/**`, `artifacts/architecture/**`, `artifacts/ingest/**`, `audit/ops/**`, `audit/qa/hde-epic0*/**`;<br>• `docs/pfcanon/**`, `AGENTS.md`, `README.md` |
| Interstage commits since the WU-PR-04 merge (`5892538`) | `dd9ac32` (#652, WU-PR-04 lineage review), `86e002c` (#653, PF10 v13.5.9 → v13.6, Product Owner), `1e97ba9` (#654, this unit's instruction), `8170cd8` (#655, its plan and companion diff). They change `docs/ephemeral/` and `docs/pfcanon/` only; none is attributable to the code delivery |
| Later divergence | none: `origin/main` is `822ce15` at review time |

**Attribution.** The landed delta is exactly #656's direct delta: a single-parent squash on the pull request's base, with equal trees and equal diff digests. The glow-merged-change-attribution-lock collector was not run (NOT EXECUTED), because native attribution meets its EXACT condition for a squash. No item is unproven.

## 4. Reviews, checks and corrected-change coverage

| Item | Fact |
| :- | :- |
| Codex code review, `173bf97` (pull request opened) | Review 5564835342 (submitted 20:37:48Z, on commit `173bf973f529`) raised one P2 finding, CX5-1, in thread `PRRT_kwDOP103ks6tuRXl` (`engine/bodygraph/ingest.py` lines 138–139, comment r4308637602): "Pass explicit log paths from the ingest evidence runner". S19-F06's `None` log defaults meant `scripts/ingest/run_vendor_ingest.py` no longer recreated the S9 logs it deletes, yet it still wrote its acceptance file and returned 0 |
| CX5-1 disposition | Corrected by `ef3cda5` (IF-35-2, IF-35-3): the runner passes `retry_log=RETRY_LOG` and `success_log=SUCCESS_LOG`, and S19-F06's `None` defaults stay. Regression test `test_s19_vendor_ingest_runner_passes_its_own_logs` fails with the change reverted, both in PR-35's run and in this review's (§5 item 7). The finding was answered in reply r4308800873 (21:20:51Z), and the thread is resolved. Neither the runner nor the classifier is a release member, and the evidence `--check` modes pass on the merged tree (§5 item 2), so no re-cut or convergence was needed |
| Codex code review, `c60ba38` and `f7d610e` ("New commits") | The re-review of `c60ba38` completed with no findings (result v1.2 §1). The Codex summary comment (issuecomment-6254839442, updated in place) records the latest code review as "Completed 2026-10-18T21:48:27.707412Z — `f7d610e` — New commits", with `has_any_findings: false` and `has_unresolved_findings: false`. This confirms the handoff's statement. No thread is open |
| Codex security review | Not part of the chain (PF10 addendum 2.3); not a gap. The summary comment's `security_review` fields are null. S19 itself is the unit's recorded security review (addendum 2.3 Rule 3) |
| Human reviews | None requested or present. The second formal review (5565017649, on `c60ba38`) only contains PR-35's thread reply |
| Hosted CI, final head `f7d610e` | Run 39169173040, job 117798448239, check `test`: success, 21:44:36Z to 22:05:31Z. <br>• **Setup:** checkout `ref: f7d610e6740bde65b1ddd87c625d2cbd523b613a` with `BASE_SHA` `8170cd8…`; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=83;lanes=product,compat,db,rails,evidence,qa,release`; `AGENTS_MD_CITATIONS_OK`. <br>• **Changed-test step:** 3,914 passed. <br>• **Lanes:** product 77; compat 119 passed, 3 skipped, 2 xfailed; db `DIRECT_DB_CONTRACT_OK` then 269; rails 120, 113, `RAILS_GATE_EVIDENCE_OK`, 155, `RAILS_JOB_DEFINITIONS_OK`, then the pin file 138; evidence 130; qa 488; release, in a worktree at `f7d610e6`, 79 passed, then the attestation built and verified. <br>• **Final audit:** every lane flag `true` with outcome `success`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` printed; no `##[error]` line. <br>• **Runner:** ubuntu-24.04 image 20261012.334.1, Python 3.12.15. <br>This confirms the handoff's statement |
| Earlier hosted runs | 39164247973 (job 117783823120) on `faf7b2b`: success, but stale once CX5-1 was known. 39167420087 on `c60ba38`: success with the same lane counts (result v1.2 §2). Neither is a gate |
| Corrected-change coverage | The reviewed and CI-tested head `f7d610e` has the merged tree. After `ef3cda5`, the only commits (`c60ba38`, `f7d610e`) add records under `docs/ephemeral/`, so the code tree PR-35 validated locally (`ef3cda5`, result v1.1 §5: full sweep 5,186 passed; all seven lanes; attestation) equals the merged code tree. The correction got both validation and review coverage, as `AGENTS.md` "Evidence attribution, currentness and distinct decisions" requires |
| Waivers | None exists or was used for HDE-CRD-0002 |
| OBS-17 and O-6 | OBS-17 did not occur: the qa lane ran, with 488 passed. O-6: `ruby` is present on the hosted runner. The contract-inventory test, which fails without `ruby` and never skips (addendum 2.2), is among the changed-test step's targets (§5 item 11), and that step passed with no failure or skip. The `ruby` version is still unprinted |

## 5. This review's independent checks on the merged `main` (`822ce15`)

**Environment.**
- Three detached worktrees of `822ce15` in a scratch clone: one for the sweep, one for the checks, one for the probes and controls.
- CPython 3.12.3 with CI's install. The scratch venv's editable install maps to the scratch clone's own checkout, which was set to `822ce15` first, so `hdctl` subprocess tests ran the code under test (OBS-W5-5).
- pytest 8.4.2; `ruby` at `/usr/local/bin/ruby`; `bash` and `curl`.
- Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`.
- Unset: `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and `ENGINE_ENV`.
- `XDG_STATE_HOME` pointed at an empty scratch directory, so a stray default-sink write would be visible.
- Every worktree ended with an empty `git status --short --untracked-files=all`.

1. **Admission:**
   - `load_active_mechanics_bundle()` → `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, 45 files, `1.3.0`, `2026-08-24T18:04:49Z`;
   - manifest SHA-256 equal to the `release_id`.
2. **Read-only evidence, release and frozen-family checks**, 25 × exit 0:
   - `scripts/release_id_recompute.py --check-manifest-only`;
   - `update_evidence_index.py --check`;
   - `orientation_demo.py --check`;
   - `validate_evidence_paths.py`;
   - `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh`, `ci/checks/check_final_lf.sh` and `ci/checks/check_cli_help.sh` (each by path);
   - `check_lf_endings.py`;
   - `refresh_step_logs_manifest.py --check`;
   - `run_canonical_json_gate.py --check-only`;
   - `generate_a7_transport_proofs.py --check`;
   - `generate_v2_mapped_cache_evidence.py --check` (`V2_MAPPED_CACHE_EVIDENCE_OK`);
   - `generate_bodygraph_policy_proofs.py --check`;
   - `tools/errors/generate_error_artifacts.py --check`;
   - `generate_conjunction_writer_evidence.py --check`;
   - `generate_determinism_gate_proofs.py --check`;
   - `generate_open_rails_abba_proof.py --check` (`audit/gates/determinism/open_rails_abba.json`, `pass`);
   - `tools/cli/generate_showcompat_artifacts.py --check`, `generate_cli_conformance_artifacts.py --check`;
   - `generate_rails_gate_evidence.py --check` (`RAILS_GATE_EVIDENCE_OK`), `generate_env_matrix_snapshot.py --check`;
   - `tools/config/generate_config_artifacts.py --check`;
   - `generate_config_artifacts.py --compare-goldens . --report <scratch>` (8 cases, 0 mismatches, `ok: true`, candidate `77204764…`);
   - `scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission --check`.
3. **Pre-existing failures** (instruction §5.6; plan F-5; OBS-P4-3). These three checks exit 1, and their output is byte-identical to the instruction's baseline run on `86e002c`:
   - `generate_hde_epic037_v2_to_compat.py --check`;
   - `generate_hde_epic037_bg_resolve.py --check`;
   - `generate_hde_epic036_bg_resolve_route_policy.py --check`.

   They were not caused by this unit, and none was run in write mode.
4. **Sanity pipeline** (`run_sanity_pipeline.py --log-path <scratch>`): exit 0, `first_failed_stage:NONE`, `summary:PASS`, 37 s.
5. **Release attestation:**
   - built with `build_release_attestation.py --output <empty scratch directory> --require-clean` (108 s) and checked with `--verify`;
   - `release_admission` `PR06R_B_FINAL_PASS`, `validation_result` `PASS`, `release_id` `77204764…`, `source_commit` `822ce15cb157…`, `source_commit_exact` true.
6. **Stale-binding sweep and labels.**
   - `git grep -l -E '2f18a5eb|9949ddf5'` outside `docs/`, `.audit_src/`, `handoff/` and `manifest_*.sha256`: no hit. In `docs/` outside `docs/ephemeral/` and `docs/pfcanon/`: no hit.
   - Mirror: 620 rows; 27 carry `77204764…` and none carries `2f18a5eb…`; the two purity-report rows carry no `notes`.
   - `artifacts/ingest/**` holds only its existing tracked files; no audit sink file is tracked.
7. **Targeted tests and negative controls.**
   - **Scope:** the 13 host modules; `-k s19` selects 268 cases.
   - **Baseline:** 268 passed. The whole host set gave 916 passed. With `APP_ENV` unset it also gave 916 passed. With `tests/adapter/test_jsonschema.py` first in the same process it gave 919 passed and 2 xfailed (OBS-P4-7 holds).
   - **Neutral controls:** a trailing comment appended to each of `adapter/http_reader.py`, `engine/bodygraph/resolver.py`, `engine/bodygraph/ingest.py`, `engine/config/registry_loader.py` and `scripts/ingest/run_vendor_ingest.py` gave 268 passed each time.
   - **Negative controls:** each one disables a single guard in a scratch worktree, and the file is then restored byte for byte.

   | ID | Guard disabled | Result of 268 | Plan v1.0 (of 267) |
   | :- | :- | :- | :- |
   | NC-01 | S19-F01 `RecursionError` in the Reader parse | 12 failed, 256 passed | 12 failed |
   | NC-04 | S19-F02 exact HTTP gate (strip and lower restored) | 24 failed, 244 passed | 24 failed |
   | NC-06 | S19-F03 `bp.record(_mount_for_production)` removed | 18 failed, 250 passed | 18 failed |
   | NC-08 | S19-F05 resolver rail (truthy reading restored) | 30 failed, 238 passed | 30 failed |
   | NC-10 | S19-F06 ingest log defaults (`RETRY_LOG`, `SUCCESS_LOG` restored) | 3 failed, 265 passed | 3 failed |
   | NC-14 | S19-F08 loader `isprintable()` rule | 6 failed, 262 passed | 6 failed |
   | CX5-1 | the runner's two explicit log arguments removed | 1 failed, 267 passed | (PR-35: 1 failed) |

   Every control fails as intended, with the plan's counts. The other fixes (S19-F04, S19-F07, S19-F09) rest on the plan's NC-02, NC-03, NC-05, NC-07, NC-09, NC-11 to NC-13 and NC-15 to NC-18, which PR-30 ran twice (S19 record §10), and on their passing tests here.
8. **Black-box HTTP probes** with the Flask test client on `822ce15`. No server was bound and no network was used.
   - **Production posture** (`APP_ENV=prod` at registration):
     - `GET` and `HEAD /reader?v=1`: 403 `ERR_READER_FORBIDDEN`, `no-store`;
     - `POST /internal/dev/sampler`, `GET /dev/sampler/conjunction` and `GET /dev/writer/conjunction`: 403 `ERR_WRITER_FORBIDDEN`, `no-store`. The answers are the same with request-time `APP_ENV=dev`, because the posture is fixed at registration;
     - `/ops/probe/env` for `GET`, `HEAD`, `OPTIONS`, `POST` and `PUT`, `GET /ops/db/unavailable`, and `POST` and `OPTIONS /ops/writer/diagnostic`: 404 `ERR_NOT_FOUND`, `no-store`, the same answer as an unknown path;
     - `POST /reader`: 405, `Allow: GET, HEAD`;
     - `/ops/rails/refusal`: 503 `ERR_WRITER_RAILS_CLOSED`;
     - `/internal/version`: 200.
   - **Router answers before the hook** (plan PD-15, P-14; LR5-O1):
     - automatic `OPTIONS` on `/reader` and `/dev/sampler/conjunction`: 200 with an `Allow` header and no handler run;
     - `GET /ops//probe/env`: 308 to the canonical path, which then answers 404.
   - **Hooks and served set:** a production posture adds exactly one `before_request` hook in each factory. Rules and pairs are the same in both postures: `adapter.factory` and `adapter.http_reader.create_app` have 21 rules and 49 pairs, and `adapter.wsgi` has 23 and 55 (`/static` excluded; pairs counted as methods per rule, as plan P-10 counts them). These numbers equal plan P-10 and result v1.0 §5 (LR5-O3).
   - **Posture classification:** `APP_ENV` values `PROD`, ` prod `, `production`, `live` and `Live`, and `ENGINE_ENV=prod` with `APP_ENV` empty, each install the hook.
   - **Gate matrix** (`POST /internal/dev/sampler` on the dev runner, `APP_ENV` set per request, JSON sent without the `charset` parameter): only exactly `dev`, `test` and `local` pass the gate. Those requests then stop at the next check, the media type, with 415. `DEV`, ` dev`, `dev `, `Dev`, `TEST `, `prod`, empty and `staging` get 403 from the gate.
   - **Parse depth:** a `POST /api/reader` body of 32,000 unclosed `[` makes the JSON parser raise `RecursionError` (checked separately). It gets 422 `ERR_READER_INVALID_INPUT` with `no-store`, as does a body of `{"a_id":` followed by 20,000 `[`. NC-01 proves that the S19-F01 guard is what turns this into 422.
   - **Dev runner** (`adapter.http_reader.create_app` under `APP_ENV=dev`): `/ops/probe/env` 200 and the sampler 200; the full mount is unchanged.
9. **Full `tests/` sweep.**
   - **Command:** `python -m pytest -q -p no:cacheprovider tests/`, with `XDG_STATE_HOME` pointed at an empty scratch directory.
   - **Result:** **5,186 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings (1,011 s; 22:19:25Z to 22:36:18Z); pytest exit 0.
   - **Afterwards:** `git status` and `git diff` empty; no file under the scratch `XDG_STATE_HOME`.
   - **Comparison:** the count equals PR-35's on `ef3cda5` (result v1.1 §5), which is PR-30's 5,185 plus CX5-1's case. The skips and xfails are the pre-existing ones. The warnings are the pre-existing `datetime.utcnow()` deprecation in `engine/ops/http_log.py`.
10. **S19 record coverage.**
    - The record's §6 table has 49 rows. Each row's path and blob equal the path's blob at the reviewed head `1e97ba9` (49 of 49).
    - The path set equals Audit Appendix B: 46 full paths plus the three sidecars Appendix B writes as suffixes (`errors/token_map/token_map.json.path_proof.txt`, `schemas/reader.v1.schema.json.sha256`, `schemas/reader.v2.schema.json.sha256`).
11. **Classifier dry run** on `8170cd8..822ce15` (`classify_ci_changes.py --event-name pull_request`): 83 paths, all seven lanes, `reason=selected_lanes`, 166 changed-test targets; the same classification as the hosted run.
12. **Not run here** (NOT EXECUTED):
    - a re-convergence (the `--check` modes in item 2 verify the converged state);
    - the seven CI lanes in sequence (hosted CI ran them on the identical tree, and PR-35 ran them on `ef3cda5`);
    - the attribution-lock collector (§3);
    - any live vendor, production or database call.

## 6. Requirement coverage across the work unit

| Requirement and acceptance (Plan v1.1 §7 WU-PR-05; instruction §10) | State | Evidence |
| :- | :- | :- |
| (1) The record covers all the paths with a per-file review line, even when no finding | MET: 49 lines, one per Appendix B path (the Plan's "48" is Appendix B's prose count; OBS-W5-1), with blobs equal at the reviewed head | §5 item 10; S19 record §1, §6 |
| (2) Every confirmed finding has a merged fix with a regression test, or a routing line with owner and reason | MET: S19-F01 to S19-F09 fixed in `d0f25b6`, with 267 `test_s19_*` cases in the 13 owning modules and negative controls NC-01 to NC-18; S19-R01 to S19-R07 routed to the Product Owner with reasons; CX5-1 fixed with its own regression test | S19 record §4, §10; §5 items 7 and 9; NC table |
| (3) No new review tooling or dependency (Exclusions bullet 6; addendum 2.3 Rule 3) | MET: no scanner, linter or analyzer; `requirements*.txt`, `pyproject.toml` and `ci.yml` unchanged | §3 (expected-unchanged); S19 record §1 "Method" |
| (4) Lanes green; when a member changed, admission and convergence as WU-PR-03 (7) | MET: five members changed (`adapter/http_reader.py`, `engine/http/compat_handler.py`, `engine/cli/main.py`, `engine/bodygraph/resolver.py`, `engine/config/registry_loader.py`); same-version re-cut with `--roster-from-admission`; convergence (result v1.0 §6: two byte-identical passes, 56 paths; step 3b; LR-O1 to LR-O3 applied); admission `77204764… 45 1.3.0`; all `--check` modes pass; hosted CI all seven lanes on the final head | §3; §4; §5 items 1 to 6 |
| Instruction ID-1 (scope and coverage statement; LR4-O4; OBS-W5-1) | MET: the 49 paths; context reads stated; `engine/bodygraph/vendor_audit.py` context only | S19 record §1 |
| ID-2 (when the review runs, its head and its record) | MET: reviewed head `1e97ba9`; plan v1.0 §5.1 to §5.9 transcribed unchanged into the record; PR-30's head confirmation at `8170cd8` (the 49 blobs equal row for row) | S19 record §1, §10; result v1.0 §2 |
| ID-3 (per-file line contents) | MET: attribution, membership, items, what was read, result | S19 record §6 |
| ID-4, ID-5 (classification, severity and disposition rules) | MET: severity scale; the confirmation rule; each routed row names the failing condition of ID-5 (a) to (d) | S19 record §2, §4 |
| ID-6 (AD-4's four gaps; OBS-P3-3, OBS-P3-14, OBS-P3-17; LR3-O2's wording) | MET: gaps 1 to 3 confirmed and fixed (S19-F03, S19-F02); gap 4 not confirmed as a security finding, with the precise wording ("runs and never matches") as O-01; OBS-P3-3 → O-02; OBS-P3-14 not confirmed; OBS-P3-17 → gap 1 for the reachable part and X-02 for the helpers | S19 record §5, §7, §8; §5 item 8 |
| ID-7 (OBS-W4-1, OBS-W4-3; route-policy statement) | MET: S19-R01 and S19-R02 routed with reasons; the route policy is stated unchanged | S19 record §4, §5, §9 |
| ID-8 (out-of-scope observations) | MET: X-01 to X-04 with owners | S19 record §8; §7 below |
| ID-9 (release identity and the refresh) | MET: refresh base `2f18a5eb…` (addendum 2.9); 22-path roster labels; step 3b; the new `release_id` recorded for WU-PR-08 | §3; §5 items 1, 2 and 6; result v1.0 §6 |
| ID-10 (tests and the test environment) | MET: 34 `test_s19_*` functions in the 13 owning modules, with no new module. The only removed test lines are five imports, each replaced by a wider import, so no assertion is removed or weakened. No skip, `xfail` or `importorskip` is added. The EPIC030 generator was never run (OBS-W5-3) | `git diff 8170cd8 822ce15 -- tests/`, read here; result v1.0 §4, §7; S19 record §10; §5 items 7 and 9 |
| ID-11 (classification consequences) | MET: PR-30 added no registration. PR-35 added one owner registration for an existing unregistered path its correction touched (IF-35-3; LR5-O2); every pin still holds | §3; §4; §5 item 11 |
| Production route exposure after the unit (contract F-3) | MET as recorded: the probes in §5 item 8 reproduce result v1.0 §5 | §5 item 8 |
| Evidence obligations (Plan; instruction §10) | MET: the result records name every check with counts, the new `release_id`, the refreshed families, the routed findings with owners, F-5, the stale-document list and the nonclaims; no live call; no sink in the repository | results v1.0 to v1.2; §5 item 6 |
| Security (instruction §11) | MET: <br>• fixes only narrow exposure: no rail opens, no write path opens, and no surface gains vendor or database access (the changed set touches neither the vendor client nor the database code); <br>• refusals use the governed envelopes with `no-store`; <br>• S19-F07 writes one code token instead of exception text, and S19-F08 refuses control characters before a path can be echoed; <br>• the records state exposures in keys-only terms | S19 record §4, §10; §3; §5 item 8 |
| Migration and recovery | none needed; rollback is a revert of `822ce15` with a same-version refresh (Plan v1.1 §7 "Common to every PR unit"); no recovery item open | — |
| PR description | MET: the template headings with checks and counts; updated for CX5-1 | #656 body |

## 7. Findings

**No finding against the landed work.** CX5-1 was found and closed before the merge (§4).

Observations (not defects of the unit), with owners:

| ID | Observation | Owner |
| :- | :- | :- |
| LR5-O1 | **D-1's stated limits.** In a production-like posture the dev-harness and retired rules stay in the URL map. The router's own answers therefore still come before the hook: <br>• automatic `OPTIONS` answers 200 with an `Allow` header on the dev-harness paths (the retired paths answer 404); <br>• a doubled-slash spelling gets a 308 to the canonical path, which then refuses. <br>No handler runs in either case. Plan v1.0 decided and recorded this (PD-1, PD-15, P-14), and the Product Owner's Proceed approved that plan. Canon says the dev conjunction routes "MUST NOT be available in production" and that requests that fail env-gating are forbidden with `ERR_WRITER_FORBIDDEN` (HDE-CLI-API-Vendor-Ref §5.12; §5.11.2 for the sampler); every request that reaches a handler gets exactly that. Canon states no `OPTIONS` or redirect rule for these paths | Product Owner, as a canon doc-delta candidate (whether "not available" also covers router-level `OPTIONS` and redirect answers); the QA Plan, through the IA, for the S19-F03 Live QA observation (contract F-3) |
| LR5-O2 | **PR-35's correction reached two paths outside plan v1.0 §8.** `scripts/ingest/run_vendor_ingest.py` is outside §8.1 and §8.2, and `ci/checks/classify_ci_changes.py` is in §8.3's expected-unchanged list. Plan RK-6 names "a change outside §8" as a rescope trigger. PR-35 recorded in-flight decisions IF-35-2 and IF-35-3 with reasons instead. This review accepts that course: <br>• the instruction's triggers are not met. §14 names a change in §6's expected-unchanged list, which contains neither path. §6 bounds the classifier to "the smallest registration a new path needs (ID-11)". The runner is an existing unregistered path, a case the instruction did not foresee, and the entry added is the smallest that classifies it, reusing an already-registered owner; <br>• the change is not material under §14's definition; <br>• it corrects this unit's own S19-F06 fix in two lines plus one owner entry, keeps F06's defaults, and has a regression test, a negative control, local validation and a clean Codex re-review (§4; `AGENTS.md` "ordinary in-scope commit progression … a material correction needs its applicable validation/review coverage") | IA lesson: later instructions state how a PR-35 correction of the unit's own fix that reaches a path outside the plan's change set is recorded |
| LR5-O3 | **Pair counts.** The records count pairs as methods per rule: 49, and 55 for `adapter.wsgi`. Distinct `(method, path)` pairs number 47 and 53, because four paths carry more than one rule (`/reader`, `/api/reader`, `/api/compat/v1`, `/ops/writer/diagnostic`) and two methods repeat across those rules. Both counts are the same in the production and dev postures on `822ce15`, so the served set is unchanged under either count | none; no correction needed |
| LR5-O4 | **Routing of the S19 record's IA-owned items** (the IA routes them, record §7 and §8). No remaining planned unit covers these paths. Routed to the Product Owner as later change candidates, unless a later plan takes them: <br>• X-01 (= LR4-O1), routed at this review as instruction v1.0 ID-8 directs; X-03; X-04; <br>• O-01's dead hook code (its wording is a canon doc-delta candidate in PF10 addendum 2.7); <br>• O-02 to O-05, O-15, O-17, O-18, O-20 to O-22, O-24 and O-25. <br>Carried to the named instructions: O-14 to WU-PR-06 (§8); O-19 to WU-PR-08 and WU-DOC-01; O-23 to the QA Plan through QA-10. O-11 to O-13 and O-16 stay with the Product Owner, as the record names. The record has no O-06 to O-10 (a numbering gap; no row is missing from its sources) | Product Owner; the named instructions |
| LR5-O5 | **Test-environment hazards met by this review:** <br>• OBS-W5-5 held: `hdctl` subprocess tests use the installed package, so the editable install's checkout was set to the commit under test before the sweep; <br>• OBS-P4-7 held: `tests/adapter/test_jsonschema.py` changes the host-set result when it runs first; <br>• OBS-W5-3 and S19-R04: owner tools that act on any invocation were not run outside their `--check` modes | WU-PR-06 instruction (the `sweep` and `replay` reports run tests and tool commands, §8) |

**Routed findings, unchanged and undecided here:**
- S19-R01 (OBS-W4-1) to S19-R07 belong to the Product Owner (S19 record §4).
- X-02 (OBS-P3-17) belongs to the Product Owner.
- The stale canon passages of result v1.0 §10 are canon doc-delta candidates for the Product Owner: HDE Architecture §3.3, §3.5 and §3.8.1; HDE Users Guide §1.1; HDE Mechanics Guide §34; and the "never fires" wording of addendum 2.7 AD-4 item 4.

**Carried observations, unchanged:**
- OBS-P4-1: WU-PR-06 or a later classifier unit.
- OBS-P4-2 and OBS-P4-7: a later unit through the IA.
- OBS-P4-3 and OBS-P4-4: Product Owner.
- OBS-P4-5: the WU-PR-08 instruction.
- OBS-P3-5: WU-PR-06.
- LR4-O2: the QA Plan, through the IA.
- LR4-O3: applied. This unit's instruction ran every check it listed, and the three known failures were marked as such.
- OBS-W4-2 and OBS-W4-4: Product Owner.
- LR3-O1, LR3-O4, LR3-O5: their owners.
- OBS-17: did not occur on #656.
- O-6: `ruby` present, version unprinted.
- AQ-1: WU-PR-07 only.

## 8. Next approved Plan stage

**WU-PR-06 — Read-only pre-push and pre-plan check (PR; Distillation; S20), through PR-10 — Create PR Work-Unit Instructions — 100926.1, by the whole-change Implementation Agent.**
- **Basis:**
  - Implementation Plan v1.1 §7 orders WU-PR-01 → … → WU-PR-05 → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01;
  - WU-PR-06's block states "Dependencies and order. Sixth; after WU-PR-01 (lane lists and sweep definition final)";
  - Specification v1.1's Distillation row states "S20 follows S03 to S05"; S03 to S05 are WU-PR-01's, and WU-PR-01 is accepted (addendum 2.4). WU-PR-05, the unit before WU-PR-06 in the merge order, is accepted by this review;
  - WU-PR-06 is an ordinary PR unit, so PR-10 is the destination;
  - no `HDE-CRD-0002-WU-PR-06-*` file exists on `main`.
- **Carried into the WU-PR-06 instruction by its author:**
  - **F-5:** this unit's one classifier registration, `"scripts/ingest/run_vendor_ingest.py": ("tests/bodygraph/test_ingest.py",)` in `_PRODUCT_TEST_OWNER_PATHS` (IF-35-3).
  - **O-14 (CI2):** the workflow's path filter hard-codes the governed exceptions under exempt prefixes, and no test ties them. The record names "WU-PR-06 or a later CI unit"; the instruction decides this within S20's bounds or routes it.
  - **OBS-P4-1:** the classifier gap for the override tests.
  - **OBS-P3-5:** a `VERIFY.sh`-only change selects `product` but not the owner test that runs it.
  - **The `ruby` requirement** (addendum 2.2 "Affected surfaces": "The WU-PR-06 instruction carries the ruby requirement of the sweep environment", and "The coverage definition contracted to WU-PR-06 is unchanged"; O-6): the `sweep` and `replay` reports run the contract-inventory test, which needs `ruby` on `PATH`.
  - **Test-environment hazards for `sweep` and `replay`:**
    - OBS-W5-5: install the worktree under test;
    - OBS-W5-3 and S19-R04: owner tools that act on any invocation, `--help` included, and the EPIC030 generator that rewrites tracked files;
    - OBS-P4-2 and OBS-P4-7: the ambient-`APP_ENV` route-policy tests and the `ENGINE_ENV` leak.
  - **The current `release_id`** `77204764…` with the 45-member roster, for the `membership` report.
  - **The current PF10 file** `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md`, for the `build-notes` report, which resolves one file and prints its SHA-256.
- **Carried for later instructions:**
  - **WU-PR-08 (S17)** cuts `1.4.0` from `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (contract F-1), with OBS-P4-5, O-19 and the production route exposure (F-3).
  - **WU-DOC-01** receives F-3, O-19 and the repository documents named in earlier reviews.
  - **The QA Plan, through QA-10,** reads the S19 record (F-2), each fix's Live QA class, LR5-O1 and O-23.

## 9. CANON_CONFLICT_REGISTER

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict. The unit applies the canon the S19 record cites, together with AD-4. Its readings stay within canon and are recorded in plan v1.0 §17 (PD-1 to PD-16) and §18, and in S19 record §4 and §5:
- D-1's one production hook;
- the exact gate;
- the strict rails;
- the routed findings whose fixes would set policy canon does not state.

LR5-O1 is a canon doc-delta candidate, not a conflict: the delivered behavior meets the refusal rule canon states, and canon is silent on `OPTIONS` and redirects. Drainage stays with the Product Owner, unperformed.

## 10. NOT PRODUCED, NOT EXECUTED and pending values

- **NOT PRODUCED:**
  - a `MERGE_OBSERVED` result for #656 (the entry is Nathan's assertion);
  - any QA, Ops, acceptance or closure artifact;
  - a PF10 addendum by this review.
- **NOT EXECUTED by this review:**
  - the attribution-lock collector;
  - a re-convergence;
  - the seven CI lanes in sequence;
  - any live vendor, production or database call;
  - any server bind (the probes used the Flask test client).
- **Pending:** none for WU-PR-05. The routed findings and later-change candidates are with their owners (§7).

## 11. TypeSafe reading and surface advice for the receiving session (PR-10, WU-PR-06)

Action sent (v8.2): "Write, as the continuing whole-change implementation agent, a new PR work-unit instruction, not yet reviewed, for the sixth unit of an approved change: one new read-only pre-push and pre-plan command-line tool with five sub-reports (CI lane classification for given paths, release membership, the current build-notes file and its hash, an uncovered-test sweep run in a throwaway copy, and a replay of every CI workflow lane step in a throwaway worktree), its new owner test and one classifier registration. It must re-measure the current repository baseline (the lane classifier, the CI workflow's lane steps, the test inventory and the release roster), map the governing canon, and carry about eight named inputs and test-environment hazards from accepted units; a task list exists (the approved plan's unit block), no code is written and no live provider call occurs, and a detailed plan, a Product Owner Proceed, implementation and independent reviews follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.17 (confidence 0.55); rung probabilities low 0.06, medium 0.12, high 0.46, extra high 0.30, max 0.05, ultracode 0.01. Model probabilities Fable 5.1 0.12, Opus 5.5 0.70, Sonnet 5.5 0.17, Haiku 5.5 0.01 (confidence 0.60). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.007, Fable 5.1 at medium 0.014, Fable 5.1 at high 0.055, Fable 5.1 at extra high 0.036, Fable 5.1 at max 0.006, Fable 5.1 at ultracode 0.001, Opus 5.5 at low 0.042, Opus 5.5 at medium 0.084, Opus 5.5 at high 0.322, Opus 5.5 at extra high 0.210, Opus 5.5 at max 0.035, Opus 5.5 at ultracode 0.007, Sonnet 5.5 at low 0.010, Sonnet 5.5 at medium 0.020, Sonnet 5.5 at high 0.078, Sonnet 5.5 at extra high 0.051, Sonnet 5.5 at max 0.009, Sonnet 5.5 at ultracode 0.002, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.001, Haiku 5.5 at high 0.005, Haiku 5.5 at extra high 0.003, Haiku 5.5 at max 0.001, Haiku 5.5 at ultracode 0.000. Flags: boundary between extra high and high. Sent 2026-10-18T22:29:21Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-18T22:29:21Z; HTTP 200 in 0.56 s; 5536 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between extra high and high.
- **Which request.** The installed skill's request v8.2 (`request-v8.2.json`, sha256 `62486fcc…`), run once with session kind `planning`.
- **Records.** No Notion row was written, as PR-40 directs. Nathan's pick for PR-10 (WU-PR-06) is not stated. Nathan's pick for this PR-40 session is not stated; its reading is result v1.2 §8.

**Surface advice:**
- **Session:** the whole-change Implementation Agent's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **What it reads:**
  - `docs/pfcanon/` on `main`;
  - the HDE-CRD-0002 records: Audit §5.2, §5.3 and §6 S20, the Plan's WU-PR-06 block, and this review's §8;
  - `ci/checks/classify_ci_changes.py`, `.github/workflows/ci.yml` and the release roster in `engine/config/registry_loader.py`.
- **Environment:** re-measuring the baseline means running the classifier, the lane steps and a full sweep. That needs:
  - Python 3.12 with CI's install, plus `ruby`, `bash` and `curl`;
  - closed rails, in scratch worktrees, with the worktree under test installed (OBS-W5-5);
  - the vendor, database and GitHub keys the container sets left unset.

  On four CPUs a full sweep takes about 17 minutes.
- **Access:** no live vendor, production or database access is needed.
- **Writes:** only the instruction, under `docs/ephemeral/`. This review's pull request should be merged first.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-05 / PR-40 / lineage review 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-05 (S19) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state as of 2026-10-12T02:29:38.234Z). Receiver contract: PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state as of 2026-10-12T02:29:33.739Z, read in full by this session at PR-10 for WU-PR-05) |
| role/stage | continuing whole-change IA, read-only PR-40 role |
| capture time | 2026-10-18T22:39:08Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | instruction v1.0 (§20); plan v1.0; results v1.0 (§17), v1.1 and v1.2 (§10) |
| pull request | amthorn78/glow-hdengine-v2#656 (`822ce15`) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); recorded here only |

## Canon relied on

Read on `main` at `822ce15` (`docs/pfcanon/` unchanged since `86e002c`).

| Decision topic | Sources and sections |
| :- | :- |
| Review authority, entry and result | PR-40 — Review PR Work-Unit Lineage — 100926.1, read in full: "Product Owner merge action" (fallback entry on Nathan's assertion), "Read-only review boundary", "Execute", "Required result", "Resolve the next approved Plan stage", "Rescope authorship, independent review and return" (non-PR findings return to the Product Owner without a lawful PR author). PR-10 — Create PR Work-Unit Instructions — 100926.1 (receiver contract). HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`): §9.1.1 (Proceed approves the exact detailed plan; implementation runs the normal code, security and review chain; merges are Product Owner actions) and §9.1.2 (canon on `main`; in-flight documents govern within their scope) |
| S19 coverage and the fixed surfaces | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`): §5.4 (dev harness routing and guard), §5.5 (compat v1), §5.11.2 (route, method and the exact `APP_ENV` gate; `ERR_WRITER_FORBIDDEN`), §5.12 (dev conjunction routes "MUST NOT be available in production"; the env-gating refusal; read in full for LR5-O1), §7.1.2 (two-gate rule), §7.1.10 (endpoint policy; S19-R02), §8.1 (typed public error object). HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`): §3.3, §3.5, §3.8.1 (the AD-4 gaps and their "Current repository discrepancy" passages) |
| Review chain | PF10-HDE-Build-Notes v13.6 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md`), addendum 2.3 (Rules 1–5: the Codex code review read and resolved; no Codex security review; Rule 3, S19 adds no review tooling) |
| AD-4 and the refresh | addendum 2.7 (AD-4: the four non-public-route gaps decided in S19, "one factory-level design applied uniformly"; AD-5: refresh base and restart rules); addendum 2.6 (RP-2 step 3b; RP-3 22-path roster); addendum 2.5 (LR-O1 to LR-O3); Implementation Plan v1.1 §10; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" |
| Carried items and next stage | addendum 2.2 "Affected surfaces" ("Dependencies": the coverage definition contracted to WU-PR-06 is unchanged; "Downstream work": the WU-PR-06 instruction carries the ruby requirement of the sweep environment); addenda 2.8 and 2.9 ("Carried into the WU-PR-05 instruction"; "Carried for later instructions"); Implementation Plan v1.1 §7 (order; "Common to every PR unit"; WU-PR-05 and WU-PR-06 blocks), §9; Specification v1.1 S19 and S20 |
| PR-35's out-of-plan correction (LR5-O2) | instruction v1.0 §6 (bounded files; expected unchanged), §14 (materiality; expected triggers), ID-11; plan v1.0 §8.3 and RK-6; `AGENTS.md` "Evidence attribution, currentness and distinct decisions" (in-scope progression; a material correction needs validation and review coverage) |
| TypeSafe reading | addendum 2.1; the typesafe-scoring skill (request v8.2) |
| In-flight documents | Specification v1.1 (S19, Exclusions bullet 6); Plan v1.1 §7, §9, §10, R-5; review v1.1; Audit §6 S19 and Appendix B; instruction v1.0; plan v1.0 and its companion diff; S19 record v1.0; results v1.0 to v1.2 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; sole Index/Mirror writer; no hand edits of governed artifacts; pytest readiness; the truncation guardrail, applied to the job log in §2 and to the exit codes in §5, each captured from the producer's own status |

Silence: no canon section defines a lineage-review predicate beyond the PR-40 prompt and HDE Governance §9.1. Canon states no `OPTIONS` or redirect rule for the dev-only and retired paths (HDE-CLI-API-Vendor-Ref searched in full by plan v1.0 PD-15; §5.4, §5.11.2 and §5.12 re-read here); see LR5-O1.
