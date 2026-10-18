---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-03-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: ACCEPT
predecessor: none (the first PR-40 review of WU-PR-03; by the Product Owner's direction of 2026-10-14 no separate review of #643 alone ran first — corrective decision record §5)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
work_unit_title: "Public, dev and CLI surfaces (PR; Conjunction; S02, S07, S09, S10, S15, S18)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 74e8f158b48d; overlaid by PF10 addenda 2.6 and 2.7 for the clauses they name)
PR_IMPLEMENTATION_PLAN_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (Proceeded; spent; blob 1e18046e5bd4); cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md (the corrective plan; Proceeded; blob 1d6a92a483e2) with companion docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0-prototype.diff
PR_30_RESULT_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED; blob fdc2f792315f); cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v2.0.md (PR_CANDIDATE_PUBLISHED; blob 5d8a84c7ab00)
PR_35_RESULT_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.1.md (RESCOPE_PENDING; historical; blob b72e57020353); cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v2.1.md (MERGE_PENDING; historical pre-merge evidence; blob ebc70d08ff98)
PR_REFS: amthorn78/glow-hdengine-v2#643 (cycle 1, merged as c98d41f) → amthorn78/glow-hdengine-v2#646 (cycle 2, corrective, merged as 2f3db0a)
entry_event: MERGE_OBSERVED for #646 (merged 2026-10-18T08:34:34Z as 2f3db0a), delivered by the cycle-2 PR-35 session in the pasted handoff; no saved MERGE_OBSERVED artifact exists (NOT PRODUCED); the merge was verified independently (§3). The earlier conditional PR-40 block issued with MERGE_PENDING is void
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role; session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (author of the WU-PR-03 instruction, both WU-PR-03 RS-20 reviews and the corrective decision record; not an author of any plan, code or result reviewed here)
pr_sessions: cycle 1 PR-20 and PR-30 https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ, PR-35 https://claude.ai/code/session_0136SjBtuTJwoEpceUd46T6C; cycle 2 PR-20 https://claude.ai/code/session_0186RTKAbX7HsgFuEgBB1fE8, PR-30 https://claude.ai/code/session_01Ea8P6Cr5BxJmYS7gBcpj11, PR-35 https://claude.ai/code/session_018Drji3J6yxg8KcP1JvgHrY
approved_lineage: Specification docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1); Implementation Audit docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0); Implementation Plan docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1); Plan review docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
overlays_and_decisions: rescope review v1.0 (docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md; RS-20 APPROVE) → PF10 addendum 2.6; PR-35 rescope review v1.0 (docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-review-v1.0.md; SPECIFICATION_CHANGE_REQUIRED) → corrective decision record v1.0 (docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md; Product Owner-directed) → PF10 addendum 2.7
return_owner: the same continuing whole-change HDE-CRD-0002 Implementation Agent
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state as of 2026-10-12T02:29:38.234Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-18T09:02:00Z
repository_state_reviewed: origin/main 2f3db0a (tree 9cce0dc250b4); no commit after it at review time
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md (v13.5.8; blob 3c13456a576c; 103,474 bytes; sha256 94573d06200935fdd29c71b04bafd2035c69b9d0537d1e4f69d9e7f02fe27eb6; front matter, index and addenda 2.6 and 2.7 read in full; 2.1 to 2.5 as read for the earlier reviews of this change)
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1 to CR-8 carried; no new entry (§9)
next_prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), for WU-PR-04
---

# HDE-CRD-0002 WU-PR-03 — PR work-unit lineage review v1.0 (PR-40, across #643 and #646)

## 1. Decision

**ACCEPT.** WU-PR-03 is delivered with sufficient attributable evidence across its ordered lineage, #643 then #646.
- #643 (cycle 1) delivered S02, S07, S09, S10, S15 and S18, the instruction's ID-3 and ID-4, and the addendum 2.6 rescope (RP-1 start-helper propagation; RP-3 label roster; RP-2 convergence order).
- It merged with two open Codex P1 findings: catalogued canon-retired routes, and a normalizing `/reader` gate.
- The Product Owner directed a corrective cycle with its architecture decided in advance (addendum 2.7). #646 (cycle 2) delivered AD-1, AD-2, AD-3, AD-5 and AD-6 exactly as bound, and closes both findings in substance.
- This review's own runs on the merged `main` confirm the landed state (§5). Both final heads passed hosted CI on their classified lanes. Nothing in the unit's scope remains unresolved.

ACCEPT is this review's lineage result only. It is not QA, acceptance of HDE-CRD-0002, Ops, deployment, release activation, PF09 or PF30 movement, or closure.

## 2. Inputs read

- **In full:**
  - this prompt;
  - the instruction v1.0;
  - plan v2.0 (all 22 sections, its "Canon relied on" and "Checks run");
  - results v2.0 and v2.1;
  - addendum 2.7 as published in PF10 v13.5.8, compared with its record.
- **Read for the earlier stages of this change, and re-checked here where a decision depends on them:**
  - plan v1.1 and result v1.0 (structure, §4 to §8 and §7 acceptance table, read again here);
  - result v1.1 (§1, §3, §6);
  - the PR-35 rescope request and review;
  - the rescope review v1.0;
  - the corrective decision record;
  - Implementation Plan v1.1 §7 (WU-PR-03 and WU-PR-04 blocks, read again here);
  - Specification v1.1 (rows S02 to S19, Exclusions and Live QA classes).
- **GitHub, read directly:**
  - #643, #646 and #647 metadata;
  - #646's commits;
  - check runs of both final heads, with their job logs read in full by a programmatic scan (#643: 901 lines; #646: 748 lines; neither truncated);
  - review threads, formal reviews and issue comments on #643 and #646.

## 3. Merge state and landed lineage

| PR | State | Head | Base | Landed as | Tree check |
| :- | :- | :- | :- | :- | :- |
| #643 (cycle 1) | merged 2026-10-14T04:41:15Z by amthorn78; 8 commits; 87 files | `dc45a35` | `1735d94` | squash `c98d41f` (one parent, `1735d94`) | `c98d41f^{tree}` = `dc45a35^{tree}` = `1a888b8fc355` |
| #646 (cycle 2) | merged 2026-10-18T08:34:34Z by amthorn78; 4 commits (`95ff2b8` source, `006b43b` convergence, `d995b9a` result v2.0, `c81594f` result v2.1); 70 files | `c81594f` | `18b3a16` | squash `2f3db0a` (one parent, `e7d0e33`) | `git diff e7d0e33 2f3db0a` is byte-identical to `git diff 18b3a16 c81594f` (same SHA-256); 70 files, +791/−157 |

**Attribution.**
- **#643's landed delta** is its head tree on `1735d94`.
- **#646's landed delta** equals its direct delta. On `main`, `2f3db0a` differs from `c81594f` only by #647's nine files.
- **Interstage commits** between the two squashes, none attributable to WU-PR-03 and none touching code, tools, tests, CI, catalog or governed evidence:

  | Commit | What it changed |
  | :- | :- |
  | `41069c2` (#644) | the PR-35 rescope review, the corrective decision record, the 2.7 record and the handoff (`docs/ephemeral/`) |
  | `79eac95` | PF10 v13.5.7 → v13.5.8, Product Owner commit (`docs/pfcanon/`) |
  | `2e08c5e` (#645) | plan v2.0 and its diff (`docs/ephemeral/`) |
  | `18b3a16` | seven `.claude/skills/*.skill` packages, Product Owner commit |
  | `e7d0e33` (#647) | TypeSafe v8 and hd-v3 pre-registration (`docs/ephemeral/typesafe-ladder/`) |

  The union of their paths outside `docs/ephemeral/`, `docs/pfcanon/` and `.claude/skills/` is empty.
- **Later divergence:** none. `2f3db0a` is the head of `main` at review time.
- **#646's changed set** is exactly the plan's: outside `docs/ephemeral/`, 68 paths (the 7 hand-edited paths of plan v2.0 §7.1 and the 61 owner-produced paths of §6.5), plus results v2.0 and v2.1. Every plan §7.3 expected-unchanged path has an empty diff. `scripts/dev_start_reader.sh` changes by one line.
- **Attribution aid not used.** The `glow-merged-change-attribution-lock` collector was not run (NOT EXECUTED). Attribution is native: single-parent squashes, equal head and landing trees for #643, equal landed and direct deltas for #646, and classified interstage commits. No item is unproven.

## 4. Reviews, checks and corrected-change coverage

**#643 (cycle 1, final head `dc45a35`).**
- **Hosted CI.** Run 38510408095, job 115677365542: success, 04:15:01Z–04:35:53Z. The log shows `HEAD is now at dc45a359`, classification `paths=88; lanes=product,compat,db,rails,evidence,qa,release`, then:

  | Step | Result |
  | :- | :- |
  | changed-test step | 3,483 passed |
  | product | 77 passed |
  | compat | 103 passed, 3 skipped, 2 xfailed |
  | db | 249 passed |
  | rails | 4 + 113 + 39 + 138 passed |
  | evidence | 130 passed |
  | qa | 488 passed |
  | release | 79 passed |

  It printed `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **Codex code review:**
  - F1 (P2, `PRRT_kwDOP103ks6sJ2D_`, aliases off the Aux record): fixed in `3a1b0a7`, answered and resolved.
  - F2 (P1, `PRRT_kwDOP103ks6sJ4Y8`, normalizing gate) and F3 (P1, `PRRT_kwDOP103ks6sJ4Y_`, catalogued retired routes): answered and routed to RS-20 (RP-5, RP-4); still open on the merged pull request.
  - Summary comment 6160341482 records the last review "Completed 2026-10-14T04:19:25Z — `dc45a35`" with no further thread.
- No formal human review.

**#646 (cycle 2, final head `c81594f`).**
- **Hosted CI.** Run 38555971758, job 115825063304: success, 11:21:19Z–11:33:20Z (on 2026-10-14). The log shows `HEAD is now at c81594fa`, `HEAD_SHA: c81594fa7ff40d3a74614024c82189b80f7f44bb`, classification `paths=70; lanes=product,compat,db,evidence,release`, then:

  | Step | Result |
  | :- | :- |
  | changed-test step | 854 passed |
  | product | 77 passed |
  | compat | 103 passed, 3 skipped, 2 xfailed |
  | db | 249 passed |
  | evidence | 130 passed |
  | release | 79 passed, then the attestation built to `/home/runner/work/_temp/hde-release-attestation/attestation.json` |

  It printed `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **Lanes not selected.** Rails and qa were not selected, because the classifier does not change in this cycle (plan v2.0 F-24). Their test files pass in the full sweeps (§5; result v2.0 §9).
- **Codex code review.** Summary comment 6163861217 records "Completed 2026-10-14T11:23:42Z — `c81594f`". There are 0 review threads and 0 formal reviews. The Codex security review is not part of the chain (addendum 2.3) and is not a gap.
- **Corrected-change coverage.** The reviewed head `c81594f` is the merged code tree. PR-35's `MERGE_PENDING` (result v2.1, on `d995b9a`) is historical pre-merge evidence. The record head `c81594f` that followed carries the green run and review above.

**Waivers.** No CI waiver exists or was used for HDE-CRD-0002.

## 5. This review's independent checks on the merged `main` (`2f3db0a`)

All runs are in detached worktrees of `2f3db0a` in a scratch clone, under:
- CPython 3.12.3 with CI's install (pytest 8.4.2);
- `ruby` at `/usr/local/bin/ruby`, `bash` and `curl`;
- closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`);
- `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL` and `GH_TOKEN` unset.

Each worktree ended with an empty `git status --short --untracked-files=all`.

| # | Check | Result |
| :- | :- | :- |
| 1 | Admission one-liner; `sha256sum catalog/manifest.json` | `d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7 45 1.3.0`; manifest SHA-256 equal |
| 2 | `release_id_recompute.py --check-manifest-only`; `update_evidence_index.py --check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `check_lf_endings.py`; `ci/checks/check_final_lf.sh`; `refresh_step_logs_manifest.py --check`; `run_canonical_json_gate.py --check-only`; `generate_a7_transport_proofs.py --check` | 11 × exit 0 |
| 3 | Frozen families: `generate_showcompat_artifacts.py --check`, `generate_cli_conformance_artifacts.py --check`, `generate_rails_gate_evidence.py --check`, `generate_env_matrix_snapshot.py --check`; `ci/checks/check_cli_help.sh` | 5 × exit 0 |
| 4 | Endpoint Catalog | 18 records; none for `/ops/db/unavailable`, `/ops/probe/env` or `/ops/writer/diagnostic` (path or alias); `docs/ENDPOINTS_CATALOG.json` a symlink `cmp`-equal to `artifacts/audit/ENDPOINTS_CATALOG.json`; both `.sha256` sidecars verify; `success_endpoints` `[GET /reader]` |
| 5 | Served set (`url_map` of `adapter/factory.py`, `adapter/http_reader.py::create_app`, `adapter/wsgi.py`) | 53 distinct pairs; all 18 catalogued pairs are served; the 9 canon-retired pairs are served and uncatalogued |
| 6 | Gate and runner code | `_reader_dev_env_explicit` returns `os.environ.get("APP_ENV") == "dev"`; `__main__` runs `create_app().run(host="127.0.0.1", port=int(os.environ.get("PORT", "8000")), debug=False, use_debugger=False, use_reloader=False)`; the start helper's banner reads `(host=127.0.0.1)` and is its only changed line in cycle 2 |
| 7 | Targeted tests: `tests/http/test_reader_a7_transport.py`, `tests/http/test_endpoint_catalog.py`, `tests/scripts/test_dev_start_reader.py`, `tests/cli/test_cli_usage_and_errors.py` | 248 passed |
| 8 | Negative control NC-1: the normalizing gate (`strip().lower() == "dev"`) restored | 5 failed (` dev`, `dev `, ` DEV `, `Dev`, `DEV`), 22 passed; file restored |
| 9 | Negative control NC-2: the run call's host set to `0.0.0.0` | the 2 runner-profile cases failed; file restored |
| 10 | Negative control NC-3: a copy of the `/ops/rails/refusal` record re-pathed to `/ops/probe/env` and appended to `catalog_obj()` | `validate_catalog` raised `canon-retired route must not be cataloged` |
| 11 | `VERIFY.sh` with `APP_ENV=dev`, `VERIFY_PORT=8471` | exit 0; 12 of 12 tokens `_OK` (`SERIALIZER_ONE_LF`, `PREIMAGE`, `TWO_RUN_IDENTITY`, `AB_BA`, `READER_200_STATUS`, `READER_200_HEADERS`, `READER_200_ETAG_PRESENT`, `READER_200_ETAG_MATCH`, `READER_304_STATUS`, `READER_304_EMPTY_BODY`, `READER_HEAD_CL_MATCH`, `ETAG_INVARIANCE`); 0 `_FAIL` |
| 12 | `VERIFY.sh` with `APP_ENV` unset | exit 2; standard error `VERIFY_APP_ENV_NOT_DEV: run with APP_ENV=dev (effective: <UNSET>)`; standard output 0 bytes |
| 13 | Label roster and Mirror | roster 22 paths, without the purity report; Mirror 620 rows; 27 labelled rows, all ending with `d84d99e1…`; the purity-report row has no `notes` |
| 14 | Stale-binding sweep: `git grep` for `72fca4c341d8` outside `docs/`; for `52be45584acb` outside `docs/`, `audit/qa/hde-epic040/`, `audit/ops/hde-epic040/`, `.audit_src/`, `handoff/`, `manifest_*.sha256` | `72fca4c3`: no hit. `52be4558`: `README.md` only (line 13; WU-DOC-01, known) |
| 15 | Harness references: `git grep -l reader_harness` outside `docs/pfcanon/`, `docs/ephemeral/` and the historical prefixes of instruction §5.4 | `CHANGELOG.md` (WU-DOC-01) and `ci/checks/classify_ci_changes.py` (the ID-3 keys): the two exceptions result v1.0 §7 records. The other hits are in §5.4's historical prefixes (`audit/docs_snapshot*`, `codex/out/`, `notes/`, `artifacts/epic004/`, `artifacts/math/_manifest_files.txt`, `audit/inventory_epic007.json`, `manifest_*.sha256`) |
| 16 | Document statements (S18, S07, S10) | `docs/ADAPTER_009.md` line 174 names the `invalid_json` alias and `ERR_COMPAT_INVALID_JSON`; `ARCHITECTURE.md` lines 9 and 24 state `emit_public` and `emit_compact_json`'s real return types, and its "Routing and mounts" section states the three factories' mounts; `engine/cli/main.py` line 79 names `magic10_compat_result.v1`; `docs/server/reader_v1.md` line 17 says "exactly `dev` (no trimming or case-folding)" and line 19 states the loopback bind |
| 17 | Full `tests/` sweep (`python -m pytest -q -p no:cacheprovider tests/`), in its own worktree, 08:38:39Z–09:00:18Z | 4,761 passed, 3 skipped, 2 xfailed, 0 failed (1,295 s); pytest exit 0; empty `git status` and `git diff` afterwards. Equal to PR-30's count on `006b43b` (result v2.0 §9 item 11). The skips and xfails are the pre-existing ones result v2.0 names. Every updater consumer, and the rails- and qa-lane test files, ran in it |

## 6. Requirement coverage across the work unit

| Requirement / acceptance item (as overlaid by 2.6 and 2.7) | Delivered by | Evidence | State |
| :- | :- | :- | :- |
| S02 / (1): unknown paths on the production and `http_reader` factories answer the governed envelope for GET, HEAD, POST and OPTIONS; compat and `api_bp` unchanged | #643 | result v1.0 §7 (180-case matrix; 405 `Allow`; regressions); `tests/http/test_endpoint_catalog.py` in §5 item 7 and the sweeps; both hosted runs | MET |
| S10 / (2), first part: `GET`/`HEAD /reader` served only for `APP_ENV` exactly `dev`; 403 `ERR_READER_FORBIDDEN` for unset, empty, ` dev`, `dev `, `Dev`, `DEV`, `test`, `local`, `prod`, `production`, `live` and arbitrary values | #643 (gate), #646 (AD-2 exactness) | §5 items 6, 7 and 8 (NC-1); result v2.0 §7 (16-value matrix); RC-1 before and after | MET |
| S10 / (2), last clause (2.6 B-2): the start helper propagates `APP_ENV`; `APP_ENV=dev` serves; unset or empty refuses | #643; banner #646 | `tests/scripts/test_dev_start_reader.py` (§5 item 7); `VERIFY.sh` (§5 items 11 and 12) | MET |
| S09 / S10 (2.7 AD-3): the canonical runner binds loopback with the debugger and reloader off and emits no CORS headers | #646 | §5 items 6 and 9 (NC-2); the runner-profile and CORS-absence tests in §5 item 7; result v2.0 RC-2 | MET |
| S07 / (3): `hdctl --help` names `magic10_compat_result.v1`; `check_cli_help.sh` exit 0; CLI conformance `--check` exit 0 | #643 | §5 items 3 and 16 | MET |
| S09 / (4): harness removed; `VERIFY.sh` runs against the canonical runner; no active reference | #643 | `dev/reader_harness/` absent; §5 items 11, 12 and 15 | MET |
| S15 / (5), read under classes (a) to (d) (2.7 AD-1; EC-8 as overlaid): every served pair has one record or one reasoned exclusion; validator accepts the model and refuses a retired record; catalog = mirror; `success_endpoints` unchanged | #643 (rows, Aux record, validator), #646 (AD-1) | §5 items 2, 4, 5, 7 and 10 (NC-3); result v2.0 §6 (53 = 18 + 35: (a) 7, (b) 1, (c) 18, (d) 9) | MET |
| S18 / (6): the documents state `invalid_json`, the emitter's real return type and the production mounts | #643 | §5 item 16 | MET |
| (7): admission `1.3.0`, 45 members, refreshed `release_id`; convergence byte-stable; recompute exit 0; lanes green | #643 (refresh `72fca4c3…`), #646 (AD-5 refresh `d84d99e1…`) | §5 items 1 to 3; result v2.0 §8 (two passes, identical `git diff` digest `e15444b1…`); both hosted runs green on their applicable lanes (§4) | MET |
| ID-3 classifier registration (`VERIFY.sh`, `dev/reader_harness/*`, the start-helper owner test) | #643 | result v1.0 §8; cycle-1 run selected all seven lanes; §5 item 15 | MET |
| ID-4 contract-inventory baseline (addendum 2.2) | #643; unchanged in #646 (F-23) | `tests/evidence/test_hdapi_v2_contract_inventory.py` in both hosted changed-test steps and the sweeps (`ruby` present) | MET |
| RP-1 propagation; RP-3 22-path roster; RP-2 step 3b (addendum 2.6) | #643; applied again in #646 | §5 items 7, 12 and 13; results v1.0 §5 and v2.0 §8 | MET |
| AD-6 canon trace | #646 | plan v2.0 §17; result v2.0 §5; `_EXCLUSION_BASIS` asserted for every excluded pair | MET |
| Evidence obligations (instruction §10; plan v2.0 §12) | results v1.0 and v2.0 | refreshed `release_id`, regenerated families, catalog diff, the S10 matrix, `VERIFY.sh`, the ID-1 exclusion table, the ID-3 keys, the ID-4 diff, stale documents, nonclaims | MET |
| Security (instruction §11; plan v2.0 §13): exposure only narrows; names-only catalog; no secret in tests, logs or records | both | the gate refuses more values; the runner binds loopback; no route opened; Codex review with no open finding on the final code | MET |
| Migration and recovery | both | none needed; no recovery item open | MET |

**AD-4 is outside the unit by decision.** It covers the dev-harness routes mounted in production, the retired `/ops` routes ungated in production, `_dev_admin_gate` normalization and the after-request hook. #646 left them unchanged as bound, and they are carried to WU-PR-05 (§8).

## 7. Findings

**No finding against the landed work.** #643's open P1 threads are closed in substance by #646:
- `PRRT_kwDOP103ks6sJ4Y8` by AD-2 (§5 items 6 and 8);
- `PRRT_kwDOP103ks6sJ4Y_` by AD-1 (§5 items 4, 5 and 10).

They remain marked unresolved on the merged #643 as merged evidence. Resolving them on GitHub is the Product Owner's choice and is not a gate.

Observations (not defects of the unit), with owners:

| ID | Observation | Owner |
| :- | :- | :- |
| LR3-O1 | **PF10 rendering.** PF10 v13.5.8 publishes addendum 2.7 without code spans. The values ` dev` and `dev ` lose their spaces, so AD-2 "Refused" and the binding requirement read "That includes dev, dev , Dev, DEV …", as if `dev` itself were refused. The `docs/ephemeral/` record, plan v2.0, the code and the tests are unambiguous and correct. A future PF10 revision may restore code formatting for those values | Product Owner (PF10 publication) |
| LR3-O2 | **Wording of AD-4 item 4.** The decision record and 2.7 say `create_app`'s after-request hook "never fires". In fact it runs on every response and its two branches never match (plan v2.0 F-26, OBS-P3-15). The WU-PR-05 instruction states it precisely | this IA (WU-PR-05 instruction) |
| LR3-O3 | Plan v2.0 §11 says record commits under `docs/ephemeral/` "select no lane". They do: the classifier compares base to head (result v2.1 §6; result v2.0 D-1). No effect on delivery | this IA (lesson; no action) |
| LR3-O4 | `README.md` line 13 still names `release_id` `52be4558…`, now superseded twice; the current value is `d84d99e1…` | WU-DOC-01, through this IA |
| LR3-O5 | O-6: the hosted `ruby` version is still unprinted. The contract-inventory test passed in both hosted changed-test steps | this IA (recorded; no action) |

Carried observations, unchanged:
- OBS-P3-1 to OBS-P3-17 with the owners results v1.0 §9 and v2.0 §11 name;
- OBS-W3-1 (bind addressed by AD-3; the production mount is AD-4's);
- OBS-RS2-1 (`_dev_admin_gate`, part of AD-4);
- OBS-17 (the qa-lane test passed in every run seen);
- LR-O1 to LR-O3 (applied in both refreshes);
- AQ-1 (WU-PR-07 only);
- the canon doc-delta candidates of addendum 2.7 and plan v2.0 §18 (Product Owner).

## 8. Next approved Plan stage

**WU-PR-04 — Provider gate and Aux preview (PR; Fermentation), through PR-10 — Create PR Work-Unit Instructions — 100926.1, by the whole-change Implementation Agent.**
- **Basis:**
  - Implementation Plan v1.1 §7 orders the units WU-PR-01 → WU-PR-02 → WU-PR-03 → WU-PR-04 → …;
  - WU-PR-04's block states "Dependencies and order. Fourth; after WU-PR-01 and WU-PR-03";
  - WU-PR-01 is accepted (addendum 2.4); WU-PR-02 is accepted (addendum 2.5); WU-PR-03 is accepted by this review;
  - WU-PR-04 is an ordinary PR unit, so PR-10 is the destination;
  - no `HDE-CRD-0002-WU-PR-04-*` file exists on `main`.
- **Carried into the WU-PR-04 instruction by its author:**
  - the refresh base `release_id` `d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7`;
  - the 22-path label roster, the convergence order with step 3b, and LR-O1 to LR-O3;
  - OBS-17 as a qa-lane risk;
  - O-6.
- **Carried for later instructions:**
  - WU-PR-05 receives AD-4's four gaps with OBS-P3-3, OBS-P3-14, OBS-P3-17 and LR3-O2's wording;
  - WU-PR-08 (S17) receives the loopback bind statements;
  - WU-DOC-01 receives the start command and bind, OBS-P3-12 and LR3-O4.

## 9. CANON_CONFLICT_REGISTER

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 (start-helper default versus canon) | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6; applied by #643 |
| CR-7 (S15 and IF-6/EC-8 versus HDE Architecture §3.5) | APPROVED, alternative (a): exclusion under canon | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7; applied by #646 |
| CR-8 (instruction §9.2 versus explicit `APP_ENV=dev`) | APPROVED, alternative (a): exact comparison | same | same; applied by #646 |

No new conflict. Drainage stays with the Product Owner: for CR-7, HDE Schemas & Artifacts §8.8 and HDE-CLI-API-Vendor-Ref §5.6; plus the canon doc-delta candidates.

## 10. NOT PRODUCED, NOT EXECUTED and pending values

- **NOT PRODUCED:** a saved `MERGE_OBSERVED` artifact for #646; any QA, Ops, acceptance or closure artifact; a PF10 addendum by this review.
- **NOT EXECUTED by this review:**
  - the attribution-lock collector (attribution is native, §3);
  - a second release attestation build (CI built it on `c81594f`; PR-30 built and verified it on `006b43b`);
  - the lane replications as separate commands (the sweep covers their test files; §5 items 2 and 3 cover their checks);
  - a re-convergence (the `--check` modes in §5 item 2 verify the converged state).
- **Pending:** none for WU-PR-03.

## 11. TypeSafe reading and surface advice for the receiving session (PR-10, WU-PR-04)

Action sent (v6): "Write, as the continuing whole-change implementation agent, a new PR work-unit instruction, not yet reviewed, for the fourth unit of an approved CRD Implementation Plan: a production vendor-override CLI flag with an eight-row environment matrix, a seven-step evaluation order and an append-only audit record, plus a band-flag fix, across two release members and one new module, with a same-version release re-cut. It must re-measure the current repository baseline, carry forward about twenty decisions and observations from three accepted units (a new release refresh base, the evidence-updater label roster, a fixed convergence order, and canon gaps routed to later units), map every governing canon passage to the unit's surfaces bullet by bullet, and set binding disposition rules for the planning session. A task list exists (the approved plan's unit block); no code is written and no live provider call occurs; a detailed plan, a Product Owner Proceed, implementation and independent reviews follow."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.71 (confidence 0.70).
  - Rung probabilities: low 0.00, medium 0.01, high 0.35, extra high 0.56, max 0.08, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.10, Opus 5.5 0.90 (confidence 0.80).
  - Twelve cells, computed from the two answers:
    - Opus 5.5 at low 0.00, Opus 5.5 at medium 0.01, Opus 5.5 at high 0.32, Opus 5.5 at extra high 0.50, Opus 5.5 at max 0.07, Opus 5.5 at ultracode 0.00;
    - Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.03, Fable 5.1 at extra high 0.06, Fable 5.1 at max 0.01, Fable 5.1 at ultracode 0.00.
  - Sent 2026-10-18T08:41:24Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-18T08:41:24Z; HTTP 200 in 0.66 s; 4304 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up). Model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none printed.
- **Which request.** v6 is the request in force; the v8 pre-registration (#647) is not yet accepted.
- No Notion row was written. **Nathan's pick for PR-10 (WU-PR-04):** not stated. **Nathan's pick for this PR-40 session:** not stated (its reading is result v2.1 §9).

**Surface advice:**
- **Session:** the whole-change Implementation Agent's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **What it reads:**
  - `docs/pfcanon/`, with HDE-CLI-API-Vendor-Ref §7.1.11a to §7.1.11f in full for the vendor override;
  - the HDE-CRD-0002 records on `main`;
  - WU-PR-04's surfaces: `engine/cli/main.py`, `engine/bodygraph/resolver.py`, the vendor client, `tests/cli/test_bg_resolve.py`, `tests/cli/test_aux_preview.py`, `tests/bodygraph/test_resolver_vendor.py`, `docs/CLI_commands.md` and the classifier.
- **Environment:** re-measuring the baseline or rehearsing the re-cut needs Python 3.12 with CI's install, `ruby`, `bash` and `curl`, closed rails and a scratch worktree. No live vendor, production or database access is needed.
- **Writes:** only its instruction, under `docs/ephemeral/`. This review's pull request should be merged first.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / PR-40 / lineage review 1 (across plan cycles 1 and 2) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state as of 2026-10-12T02:29:38.234Z). Receiver contract read: PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state as of 2026-10-12T02:29:33.739Z) |
| role/stage | continuing whole-change IA, read-only PR-40 role |
| capture time | 2026-10-18T09:02:00Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | instruction v1.0 (§20); plans v1.0, v1.1 and v2.0; RS-20 reviews 1 and 2; the corrective decision record (§9); results v1.0, v1.1, v2.0 and v2.1 |
| pull requests | amthorn78/glow-hdengine-v2#643 (`c98d41f`), amthorn78/glow-hdengine-v2#646 (`2f3db0a`) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); recorded here only |

## Canon relied on

Read on `main` at `2f3db0a`. `docs/pfcanon/` changed since the corrective decisions only by `79eac95` (PF10 v13.5.7 → v13.5.8).

| Decision topic | Sources and sections | Effect |
| :- | :- | :- |
| Review procedure, entry, verdicts, next stage, handoff | PR-40 — Review PR Work-Unit Lineage — 100926.1 (read in full); PR-10 — Create PR Work-Unit Instructions — 100926.1 (receiver contract, revision confirmed); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (Proceed per detailed PR plan; merges are Product Owner actions) and §9.1.2 (canon on `main`; in-flight documents and Product Owner dispositions govern within their scope) | §1, §3, §8 |
| Overlays applied by the unit | PF10-HDE-Build-Notes v13.5.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md`): front matter rules, index, addendum 2.6 (RP-1, RP-2, RP-3 and B-1 to B-12) and addendum 2.7 (AD-1 to AD-6, overlaid clauses, binding requirements), read in full; 2.2 (ID-4), 2.3 (review chain without the security review), 2.5 (LR-O1 to LR-O3) as read for the earlier reviews | §6 coverage; §4 review chain; LR3-O1 |
| AD-1 / S15 | HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §3.5 "Current repository discrepancy" and "Adopted routes"; HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`) §1.1 retired-route table; HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.8; HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.6 (all read in full for the corrective decisions; the passages relied on re-checked against the landed catalog here) | §5 items 4, 5 and 10 |
| AD-2 / S10 | HDE-CLI-API-Vendor-Ref §5.4 "Gate."; §5.6 `/reader` row; HDE Schemas & Artifacts §8.8 "Reader surface routes and distinct contracts (normative)"; HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §34 route table | §5 items 6 and 8 |
| AD-3 / S09, S10 | HDE-CLI-API-Vendor-Ref §5.4 "Gate." (local interface); HDE Mechanics Guide §34 "Required local capture profile"; HDE Architecture §3.8.1 "Repo-side start-helper posture" and HDE Mechanics Guide §5.6 start-helper paragraph (propagation unchanged) | §5 items 6, 9, 11 and 12 |
| AD-4 (outside the unit) | HDE Architecture §1.3, §3.2, §3.3, §3.5; HDE-CLI-API-Vendor-Ref §5.4; HDE Governance "Dev/admin APP_ENV gating"; Specification S19 | §6 note; §8 carried |
| AD-5 / (7) | Implementation Plan v1.1 §10; addendum 2.6 (step 3b; roster) and 2.7 AD-5; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" | §5 items 1 to 3, 13 and 14 |
| CI and review scope | `AGENTS.md` "HDE-EPIC039 current workflow posture" (the `test` job, seven lanes, exact-head marker), "Code review guidelines", "Evidence attribution, currentness and distinct decisions", "Truncation/retrieval-failure guardrail" | §4 (logs read whole; lanes as classified) |
| In-flight records | Specification v1.1 (S02 to S19; Exclusions; Live QA classes); Implementation Plan v1.1 §7 (WU-PR-03, WU-PR-04, order); instruction v1.0 (in full); plan v2.0 (in full); results v2.0 and v2.1 (in full); result v1.0 §4 to §8; corrective decision record; rescope reviews | §2 |
| Silence | No canon section defines a lineage-review predicate beyond the PR-40 prompt and HDE Governance §9.1; the Glow QA Guide and HDE Phased Epics hits on "acceptance" concern QA and historical acceptance, not this review | — |
