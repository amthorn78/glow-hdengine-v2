---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-03-PR-IMPLEMENTATION-RESULT
artifact_version: "2.0"
result_state: PR_CANDIDATE_PUBLISHED
phase: PR-30
plan_cycle: 2 (the corrective cycle; decision record and PF10 addendum 2.7)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; unchanged; overlaid by PF10 addenda 2.6 and 2.7 for the clauses they name)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md (v2.0; blob 1d6a92a483e2; landed by #645 as 2e08c5e); companion docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0-prototype.diff (blob 0a0c82a7efc1)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; not edited)
CORRECTIVE_DECISION_RECORD_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md (v1.0, COMPLETE; AD-1 to AD-6; CR-7 and CR-8 APPROVED)
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md (cycle 1, RS-20 APPROVE; carried through addendum 2.6)
REMEDIATION_REVIEW_ID: none
effective_baseline: approved base (Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0) + PF10 addenda 2.2, 2.3, 2.5, 2.6 and 2.7 (2.7 overlays 2.6 only where its "Overlaid base clauses" says so)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md (v13.5.8, effective 2026.10.14; blob 3c13456a576c; 103,474 bytes; sha256 94573d06200935fdd29c71b04bafd2035c69b9d0537d1e4f69d9e7f02fe27eb6; resolved afresh on main 18b3a16 and read: front matter §§1–9, cross-references, index, addenda 2.1, 2.2, 2.3, 2.5, 2.6 and 2.7 in full; 2.4 is a WU-PR-01 record). Provenance, not a gate
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md §2.2, §2.3, §2.5, §2.6, §2.7 (records docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md for 2.6 and docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-PF10-build-notes-addendum-v1.0.md for 2.7); §2.1 for §17
pf10_addendum_created: none (PR-30 is not a qualifying approval prompt)
proceed: Nathan / Product Owner, by pasting in this session, on 2026-10-14, the PR-30 invocation that names exactly docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md (version 2.0, state AWAITING_PO_PROCEED), with the prerequisite that #645 is merged (it is: 2e08c5e on main). The one Proceed for plan cycle 2; cycle 1's Proceed (plan v1.1) is spent and not reused
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-03 PR engineering session for plan cycle 2 (PR-30 phase), https://claude.ai/code/session_01Ea8P6Cr5BxJmYS7gBcpj11 (session_disposition INITIAL_DEDICATED_ASSIGNMENT; created by Nathan; the cycle-1 and PR-20 sessions were not reused)
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08Z; read in full); primary skill glow-hde-pr-development 1.4.0
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2 (cloud container)
repository_baseline: origin/main 18b3a162db9b73fe41856f91f46543610e11dbc7 (Product Owner commit "skills for cline" over #645 at 2e08c5e; §2)
branch: claude/affectionate-euler-i70chn (new for cycle 2; created at origin/main 18b3a16; only this cycle's commits)
pull_request: amthorn78/glow-hdengine-v2#646 (https://github.com/amthorn78/glow-hdengine-v2/pull/646; open, base main, not draft)
commits: 95ff2b8 (hand-edited source, §7.1); 006b43b (owner-produced re-cut and convergence; the tested code and evidence head, tree 8668a2d3b52a); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried; CR-7 and CR-8 APPROVED, alternative (a) each; no new entry (§15)
created_at: 2026-10-14T08:08:05Z
next_phase: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e), in its own dedicated session (session_disposition NEW_DEDICATED)
---

# HDE-CRD-0002 WU-PR-03 — PR Implementation Result v2.0 (PR-30, corrective cycle)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** The corrective delta of plan v2.0 is implemented, converged by the owners, locally validated (§9) and published as [amthorn78/glow-hdengine-v2#646](https://github.com/amthorn78/glow-hdengine-v2/pull/646):
- **AD-1:** the Endpoint Catalog drops the five records of the three canon-retired routes (23 → 18); the catalog owner's validator refuses them; the enumeration test gains exclusion class (d) and accounts for 53 served pairs as 18 + 35.
- **AD-2:** the dev `GET`/`HEAD /reader` gate compares `APP_ENV` exactly with `dev`.
- **AD-3:** `python -m adapter.http_reader` binds `127.0.0.1` with `debug`, `use_debugger` and `use_reloader` explicitly `False`; tests prove the run call and the absence of CORS headers; the start helper's banner names the host.
- **AD-5:** one same-version re-cut (`release_id` `d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7`, superseding `72fca4c3…`) and two byte-identical convergence passes.
- **AD-6:** the canon trace (§5) and the class-and-basis record in the enumeration test.

What #643 delivered stands; nothing of it is restated here as this cycle's work. PR-35 owns review retrieval and correction, hosted current-head CI and merge readiness. Nothing here is merged. Nothing here claims merge readiness, QA, acceptance or closure.

## 2. Recovery and base

| Check | Observation |
| :- | :- |
| Open pull requests | none (GitHub listing, state open, before any write) |
| Local root, worktrees, branches | one worktree, `/home/user/glow-hdengine-v2`, on `claude/affectionate-euler-i70chn` at `18b3a16` (= `origin/main`), clean; the branch did not exist on the remote |
| Remote branches | `claude/nifty-cray-w86vmp` (#643's, merged history; not reused), `claude/wizardly-edison-x05uwc`, `codex/exclude-markdown-code-review`, `docs/20261012-crd0002-specification`, `main`; none carries cycle-2 work |
| Cycle-2 artifacts on `main` | plan v2.0 and its companion diff only; no `HDE-CRD-0002-WU-PR-03-pr-implementation-result-v2*`, no cycle-2 commit or pull request |
| Prerequisite | #645 merged (`2e08c5e` on `main`) |
| Base | `origin/main` `18b3a162db9b73fe41856f91f46543610e11dbc7`. It moved past the plan's baseline `79eac95` by #645 (plan v2.0 and its diff, `docs/ephemeral/`) and `18b3a16` "skills for cline" (seven binary `.claude/skills/*.skill` files, Product Owner commit, 2026-10-14T07:29:15Z) |
| Plan §8 step 2 | `git diff 79eac95 18b3a16 -- adapter/ tools/evidence/generate_a7_transport_proofs.py tests/http/test_endpoint_catalog.py tests/http/test_reader_a7_transport.py tests/scripts/test_dev_start_reader.py scripts/dev_start_reader.sh docs/server/reader_v1.md catalog/manifest.json ci/checks/classify_ci_changes.py tools/evidence/update_evidence_index.py` is empty, so no re-measurement was required. F-15 was re-measured anyway at the candidate head (§6) |
| Companion diff | `git apply --check` on `18b3a16`: succeeds (7 files) |
| PF10 | `docs/pfcanon/` unchanged since `79eac95`; PF10 v13.5.8 blob `3c13456a576c`, the plan's |
| Action | work on the designated branch `claude/affectionate-euler-i70chn` from `18b3a16`; no other vehicle created |

## 3. Authority, Proceed and lineage

- **Proceed.** Nathan invoked PR-30 for exactly plan v2.0 (front matter). It is the one Proceed for plan cycle 2. PR-35 and any recovery continue under it without another Proceed.
- **Immutable base.** Specification v1.1; Implementation Plan v1.1 and its review v1.1; PR instruction v1.0. None is rewritten.
- **Overlays.** PF10 addendum 2.2 (ID-4 binding requirements); 2.3 (reviewer chain without the Codex security review); 2.5 (LR-O1 to LR-O3); 2.6 (start-helper propagation, 22-path roster, step 3b), overlaid by 2.7 for the start helper's banner line only; 2.7 (AD-1 to AD-6, the overlaid clauses and the binding requirements of this cycle).
- **Cycle 1 history.** #643 (squash `c98d41f`) is merged history; it was not resumed, reused or pushed to. Its open Codex threads `PRRT_kwDOP103ks6sJ4Y_` (catalogued retired routes) and `PRRT_kwDOP103ks6sJ4Y8` (normalizing gate) are resolved in substance by AD-1 and AD-2 here; nothing was posted on #643.

## 4. Implementation (commit `95ff2b8`)

**Starting point.** The companion diff was applied to `18b3a16` in two steps: first the hunks of `tests/http/test_reader_a7_transport.py` alone (for RC-1 "before"), then the other six files. Every hunk was re-read against plan v2.0 §6:
- `tools/evidence/generate_a7_transport_proofs.py` against §6.1 and PD-25: `CANON_RETIRED_PATHS` after the `AUX_PATH` line; exactly the five records removed; the other 18 keep their bytes and order; the pin after the "aliases only on the aux record" check, refusing a retired path as a record path or an alias with `canon-retired route must not be cataloged`.
- `tests/http/test_endpoint_catalog.py` against §6.2, PD-26 to PD-28: the import; `_CANON_RETIRED` and `_EXCLUSION_BASIS` with the plan's texts; class (d) with nine pairs and the two paths out of class (c); the four added assertions; the `/internal/healthz` retarget; the parametrized retired-pin test.
- `adapter/http_reader.py` against §6.3 (PD-29) and §6.4 (PD-31): `return os.environ.get("APP_ENV") == "dev"` with the plan's docstring; name, call site and `v`-first order unchanged; the `__main__` run call with `host="127.0.0.1"`, `port=int(os.environ.get("PORT", "8000"))`, `debug=False`, `use_debugger=False`, `use_reloader=False`; the module-level `app = create_app()` unchanged; one final LF.
- `tests/http/test_reader_a7_transport.py` against §6.3 (PD-30) and §6.4 (PD-32): served `["dev"]`; the 16-value refusal matrix; the runner-profile test via `runpy` on `http_reader.__name__` with `flask.Flask.run` recorded; the six-request CORS-absence test on `http_reader.create_app()`.
- `scripts/dev_start_reader.sh` (line 23 only), `tests/scripts/test_dev_start_reader.py` (one assertion) and `docs/server/reader_v1.md` (lines 17 and 19) against §6.4 and §6.6 (PD-33).

No difference between the diff and the plan was found; no hunk was changed.

**Hand-edited set** (`git show --stat 95ff2b8`: 7 files, 111 insertions, 29 deletions): `adapter/http_reader.py` (member), `docs/server/reader_v1.md`, `scripts/dev_start_reader.sh`, `tests/http/test_endpoint_catalog.py`, `tests/http/test_reader_a7_transport.py`, `tests/scripts/test_dev_start_reader.py`, `tools/evidence/generate_a7_transport_proofs.py`.

**Before and after, without admission** (plan §8 step 5; the file's seams avoid the admission dependency):

| Run | Result |
| :- | :- |
| RC-1 before: base `adapter/http_reader.py`, new tests only | 7 failed, 20 passed: the refusal cases ` dev`, `dev `, ` DEV `, `Dev`, `DEV` (served by the normalizing gate) and both runner-profile cases (`{'host': '0.0.0.0'} != {'host': '127.0.0.1'}`, flags absent). Exactly the plan's RC-1 set |
| After: §7.1 applied | 27 passed |
| RC-2 (optional; detached scratch worktree of `95ff2b8`, never committed): an after-request hook setting `Access-Control-Allow-Origin: *` injected into `create_app` | the 6 CORS-absence cases failed, 21 deselected; file restored; worktree removed |

## 5. Canon trace (AD-6), restated against the landed code

Plan v2.0 §17 restated at `006b43b`. No difference from the plan.

### 5.1 Decisions

| Decision | Canon relied on (document, section, bullet) | Landed code |
| :- | :- | :- |
| AD-1 | HDE Architecture §3.5 "Internal-ops identity and refusal (route-only)", "Current repository discrepancy" (the three routes "are `RETIRED/NONCANONICAL` as architecture and excluded from the Endpoint Catalog"; "No repository removal … or catalog mutation is claimed") and "Adopted routes" (`/internal/version`, `/ops/rails/refusal`) | `tools/evidence/generate_a7_transport_proofs.py` line 38 `CANON_RETIRED_PATHS`; five records removed; `/ops/rails/refusal` `GET` and `POST` stay catalogued; the routes stay mounted |
| AD-1 | HDE Users Guide §1.1 "Checked-in retired/noncanonical route drift (unsupported)" (the three rows; "do not define route bytes, promise removal, create a deprecation window, or imply compatibility support") | `tests/http/test_endpoint_catalog.py` lines 106–138: class (d) and its basis; no route removed |
| AD-1 | HDE Architecture §0 "Endpoint Catalog (single home; routing note)" (derived inventories "MUST NOT independently hard-code a second endpoint inventory") | the retired set has one home, the catalog owner; the test imports it (PD-25) |
| AD-1 | HDE Schemas & Artifacts §8.8 "Authoritative Endpoint Catalog file" ("public surfaces and key internal/ops/dev endpoints"; "correspond to real mounted routes"; closed class set; minimum fields) | no class or field change; the `catalogued − served` assertion kept |
| AD-1 | HDE-CLI-API-Vendor-Ref §5.6 "Endpoint Catalog (JSON success)" (none of the three routes in its table; the Aux record and `aliases`) | Aux record, `public_aux` and `aliases` unchanged |
| AD-1 | HDE Governance §9.1.2 "Canon precedence and persistent sources"; HDE Build Notes 2.7 AD-1 "S15 reading" | S15 read under canon; IF-6/EC-8 as overlaid |
| AD-2 | HDE-CLI-API-Vendor-Ref §5.4 "Route and gate (must)", bullet "Gate." ("The route **must** be gated by `APP_ENV=dev` …"); §5.6 `/reader` row ("explicit `APP_ENV=dev`") | `adapter/http_reader.py` line 378 `_reader_dev_env_explicit`: `os.environ.get("APP_ENV") == "dev"`; call site line 612, after the `v` check |
| AD-2 | HDE Schemas & Artifacts §8.8 "Reader surface routes and distinct contracts (normative)" ("explicitly gated by `APP_ENV=dev`"); HDE Mechanics Guide §34 route table `/reader?v=1` row and "Required local capture profile" ("Require the caller to supply `APP_ENV=dev`") | catalog `env_gate` `APP_ENV=dev` unchanged; `docs/server/reader_v1.md` line 17 |
| AD-2 (contrast) | HDE-CLI-API-Vendor-Ref §5.5 (normalization only where it widens refusal); HDE Governance "Dev/admin APP_ENV gating (dev/test/local only)" | `_dev_admin_gate` unchanged (AD-4, WU-PR-05) |
| AD-3 | HDE-CLI-API-Vendor-Ref §5.4 "Gate." ("bound only to a local interface (for example, `127.0.0.1`)"), "Documented local-style access (clarification)", "Rails closed." | `adapter/http_reader.py` lines 1239–1250: the run call; `docs/server/reader_v1.md` line 19 |
| AD-3 | HDE Mechanics Guide §34 "Required local capture profile" (bind `127.0.0.1`; port `8000` with explicit `PORT` override; "Disable CORS …"; "Set Flask `debug=False`, `use_debugger=False`, and `use_reloader=False` explicitly"), "Shared environments", "Current repository posture" | the run call; `test_dev_runner_binds_loopback_with_debugger_and_reloader_off`; `test_dev_runner_emits_no_cors_headers` (the test-backed disabled-CORS declaration) |
| AD-3 | HDE Build Checklist — Conjunction, Subtask HDE-CONJ001.1 "Dev-only posture" (loopback; CORS disabled; debug reloader off) | supporting canon, as the plan records |
| AD-3 (scope) | Glow Infrastructure §2.2 "Client access, service identity, and server bind are separate facts"; Plan Templates `127.0.0.1` template note | the production `Procfile` and `scripts/start_web.sh` binds untouched |
| AD-3 (unchanged) | HDE Architecture §3.8.1 "Repo-side start-helper posture"; HDE Mechanics Guide §5.6 "Dev Reader start helpers (APP_ENV propagation)" | `scripts/dev_start_reader.sh` changes only line 23 (banner); propagation unchanged |
| AD-4 | HDE Architecture §1.3, §3.2, §3.3, §3.5; HDE-CLI-API-Vendor-Ref §5.4 "Gate."; HDE Governance dev/admin gating; Specification S19 | not in this pull request; carried to WU-PR-05 (§11) |
| AD-5 | Implementation Plan v1.1 §10; HDE Build Notes 2.6 (step 3b; 22-path roster) and 2.7 AD-5; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" | §8 |
| AD-6 | `AGENTS.md` canon-first rule; HDE Governance §9.1.2 | this section; `_EXCLUSION_BASIS`; the enumeration test's basis assertion |

### 5.2 Routes the unit touches

| Route and methods | Posture at `006b43b` | Canon |
| :- | :- | :- |
| `GET`, `HEAD /reader` | served only for `APP_ENV` exactly `dev`; catalogued (`dev_harness`, `env_gate: APP_ENV=dev`, A7-eligible, the success designation) | HDE-CLI-API-Vendor-Ref §5.4 "Gate.", §5.6 `/reader` row; HDE Schemas & Artifacts §8.8 "Reader surface routes and distinct contracts" and the success-proof designation; HDE Mechanics Guide §34 route table |
| `OPTIONS /reader` | unchanged; class (c); no CORS headers (tested) | HDE Mechanics Guide §34 "Disable CORS"; ID-1 class (c) |
| `POST /reader` | unchanged; class (a) | HDE-CLI-API-Vendor-Ref §5.4 "Production mount" |
| `GET`, `HEAD`, `OPTIONS /ops/db/unavailable`; `GET`, `HEAD`, `OPTIONS /ops/probe/env`; `POST`, `HEAD`, `OPTIONS /ops/writer/diagnostic` | mounted and unchanged; not catalogued; class (d); the validator refuses a record for them | HDE Architecture §3.5 "Current repository discrepancy"; HDE Users Guide §1.1 |
| `GET`, `POST /ops/rails/refusal` | unchanged; catalogued | HDE Architecture §3.5 "Adopted routes" |
| the dev runner (`python -m adapter.http_reader`, started by `scripts/dev_start_reader.sh`) | binds `127.0.0.1` only; debugger and reloader off; no CORS headers | HDE-CLI-API-Vendor-Ref §5.4 "Gate."; HDE Mechanics Guide §34 "Required local capture profile"; HDE Build Checklist — Conjunction HDE-CONJ001.1 |
| every other served pair (14 other catalogued records; 26 class (a)–(c) exclusions) | unchanged | the class bases of plan §6.2; cycle 1's per-record readings |

Tally at `006b43b`: 53 served = 18 catalogued + 35 excluded (7 (a), 1 (b), 18 (c), 9 (d)).

## 6. AD-1 — catalog, exclusions, arithmetic, pin

- **Catalog diff (23 → 18).** Removed: `GET /ops/db/unavailable`, `GET /ops/probe/env`, `POST /ops/writer/diagnostic` (with `route_id` `ops.writer.diagnostic.v1`), `HEAD /ops/writer/diagnostic`, `OPTIONS /ops/writer/diagnostic`. Added: none. The 18 kept records are byte-equal and in their former order. `success_endpoints` `[GET /reader]` and `generated_at_utc` `2026-08-24T18:04:49Z` unchanged.
- **Mirror and symlink.** `docs/ENDPOINTS_CATALOG.json` `cmp`-equal to `artifacts/audit/ENDPOINTS_CATALOG.json`; the docs path stays a symlink (mode 120000, blob `5d041e91a8c0`, target `../artifacts/audit/ENDPOINTS_CATALOG.json`).
- **Served set at `006b43b`** (`url_map` of `adapter/factory.py`, `adapter/wsgi.py`, `adapter/http_reader.py::create_app`; `static` excluded): 53 distinct pairs. Uncatalogued and unexcluded: none. Stale exclusions: none. Catalogued but unmounted: none.
- **Exclusion table by class:** (a) governed refusal 7; (b) alias 1; (c) framework-implicit 18; (d) canon-retired 9 (`GET`, `HEAD`, `OPTIONS` of `/ops/db/unavailable` and `/ops/probe/env`; `HEAD`, `OPTIONS`, `POST` of `/ops/writer/diagnostic`). Total 35. Each class's basis is `_EXCLUSION_BASIS` data, asserted for every excluded pair.
- **Arithmetic at the head:** 18 catalogued + 35 excluded = 53 served, asserted by `len(served) == len(catalogued) + len(excluded)`.
- **Pin and tests.** `validate_catalog` refuses a canon-retired path as a record path or alias (`canon-retired route must not be cataloged`). `test_validator_refuses_a_record_for_a_canon_retired_route` (3 cases) and the retargeted `/internal/healthz` case pass (§9).

## 7. AD-2 and AD-3 results

- **AD-2.** Served value: exactly `dev` (`test_dev_reader_is_served_only_for_explicit_dev[dev]`: `GET` 200, `HEAD` 200 with no body). Refusal matrix, 16 values (unset, `""`, `"  "`, `" dev"`, `"dev "`, `" DEV "`, `"Dev"`, `"DEV"`, `"test"`, `"local"`, `"prod"`, `"production"`, `"live"`, `"staging"`, `"development"`, `"dev1"`): each 403 `ERR_READER_FORBIDDEN`, `no-store`, JSON, no ETag; `HEAD` 403 with no body; `v=2` answers 400 `ERR_READER_INVALID_VERSION` first. RC-1 before and after: §4.
- **AD-3, run call as the test observed it:** exactly one call, `{"host": "127.0.0.1", "port": 8000, "debug": False, "use_debugger": False, "use_reloader": False}` with `PORT` unset, and `port: 8123` with `PORT=8123`, on an app that serves `/reader`.
- **AD-3, CORS absence:** with `Origin: https://cross-origin.invalid`: `GET /reader` (dev) 200; `HEAD /reader` (dev) 200; preflight `OPTIONS /reader` with `Access-Control-Request-Method: GET` 200; `GET /reader` under `APP_ENV=prod` 403; `v=2` 400; `/no-such-route` 404. No response header name starts with `access-control-` on any of them.
- **AD-3, banner:** `[dev-start] Binding port ${PORT} via python -m adapter.http_reader (host=127.0.0.1)`; `git diff 18b3a16 006b43b -- scripts/dev_start_reader.sh` is exactly that line.
- **AD-3, loopback runs:** `tests/scripts/test_dev_start_reader.py` 10 passed in the changed-test step (with the new banner assertion) and again with `APP_ENV` unset in the informative run; its runner is reached on `127.0.0.1`; `VERIFY.sh` with `APP_ENV=dev` exit 0, 12 of 12 tokens `_OK` (`SERIALIZER_ONE_LF`, `PREIMAGE`, `TWO_RUN_IDENTITY`, `AB_BA`, `READER_200_STATUS`, `READER_200_HEADERS`, `READER_200_ETAG_PRESENT`, `READER_200_ETAG_MATCH`, `READER_304_STATUS`, `READER_304_EMPTY_BODY`, `READER_HEAD_CL_MATCH`, `ETAG_INVARIANCE`) against the loopback runner; clean tree; without `APP_ENV` exit 2; standard error `VERIFY_APP_ENV_NOT_DEV: run with APP_ENV=dev (effective: <UNSET>)`; standard output empty (0 bytes); clean tree (§9).

## 8. AD-5 — release refresh and convergence (commit `006b43b`)

**Setup.** The branch's working tree, after the member bytes were final and committed (`95ff2b8`); Python 3.12.3 venv with CI's install; closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH` the checkout). The container's environment sets `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL` and `GH_TOKEN` (names only); every run unset them, and `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY` and `GITHUB_TOKEN`. One script ran steps 2 to 10 (pass 1) and steps 3 to 10 (pass 2), stopping on any non-zero exit; `ci/checks/*.sh` were invoked by path (F-25).

| Step | Commands (owner) | Pass 1 | Pass 2 |
| :- | :- | :- | :- |
| 2 | `scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; `scripts/release_id_recompute.py --check-manifest-only`; the cutter with `--check` | 3 × exit 0. One manifest row changed: `adapter/http_reader.py`. `release_id` = manifest SHA-256 `d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7`, equal to the plan's rehearsal (the companion hunks were applied unchanged) | not run |
| 3 | admission one-liner; `tools/config/generate_config_artifacts.py --compare-goldens . --report <outside>` | `d84d99e1… 45 1.3.0`; exit 0 | same |
| 3b | `HDE_WRITE_A7_PROOFS=1 tools/evidence/generate_a7_transport_proofs.py`; `--check` | exit 0 | exit 0 |
| 4 | `tools/evidence/run_canonical_json_gate.py`; `--check-only` | exit 0 | exit 0 |
| 5 | `tools/evidence/update_evidence_index.py`; `--check` | exit 0 | exit 0 |
| 6 | `generate_config_artifacts.py --publish-family`; updater `--check` | exit 0 | exit 0 |
| 7 | A7 write and `--check`; `generate_determinism_gate_proofs.py`; `SAFE_MODE=0 ALLOW_NETWORK=1 generate_open_rails_abba_proof.py` (fixture mode, keys absent); `FROZEN_OPEN_ABBA_SHA256` set to `sha256sum audit/gates/determinism/open_rails_abba.json` by an anchored one-line replacement; `generate_conjunction_writer_evidence.py`; `generate_engine_core_evidence.py` | all exit 0; open-rails digest `06611525045515c29b7dc4dee50b9906dce8053726a642a5de9050ce5d01613c` (supersedes `64553c25…`; equal to the rehearsal) | all exit 0; same digest; constant unchanged |
| 8 | updater; `--check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `check_lf_endings.py`; `ci/checks/check_final_lf.sh`; `refresh_step_logs_manifest.py --check` | 9 × exit 0 | 9 × exit 0 |
| 9 | `run_sanity_pipeline.py --log-path <outside>` (ends `summary:PASS`); the canonical run; `run_sanity_pipeline_gate.py`; updater `--check` | 4 × exit 0; `summary:PASS` | same |
| 10 | `generate_showcompat_artifacts.py --check`; `generate_cli_conformance_artifacts.py --check`; `generate_rails_gate_evidence.py --check`; `generate_env_matrix_snapshot.py --check` | 4 × exit 0 (frozen families unchanged) | same |

**Byte stability.** Pass 1: 37 runs, all exit 0. Pass 2: 34 runs, all exit 0. After each pass 61 paths differed from `95ff2b8`, no untracked file existed, and `git diff HEAD` had SHA-256 `e15444b1ebb35afc36c6e4424e5f87accef7d97d934b16b097b26b4c36295927`; the two patches are `cmp`-identical. (The plan's rehearsal digest `a6fd148b…` was taken against `79eac95`; path proofs carry capture provenance, so the digest is a per-run identity, not a cross-run constant.)

**Changed set (61 paths, owner-produced):** `catalog/manifest.json`; `tools/evidence/generate_open_rails_abba_proof.py` (`FROZEN_OPEN_ABBA_SHA256` only); 29 evidence primaries with their 29 path proofs; `docs/ENDPOINTS_CATALOG.json.path_proof.txt`. The families are exactly plan §6.5's:
- Catalog: `artifacts/audit/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`, `docs/ENDPOINTS_CATALOG.json.sha256`.
- A7 success proofs: `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}`.
- Config: `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log`.
- Engine core: `artifacts/core/{abba/ab_ba_parity,json_compare/core_result_json_compare,two_run/identity}.json`.
- F07 writer: `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}`.
- Canonical JSON gate: `audit/gates/canonical_json/{json_canon_compare,json_canonical_check}.log`, `audit/gates/json_gate/canonical/{json_gate_check_log,json_gate_compare_log}.ndjson`.
- Determinism and parity: `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}`, `audit/gates/parity/reader_cli/{ab,ba,summary}.json`.
- Index and Mirror: `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`.

**Rewritten byte-identically** (not in the diff): `artifacts/proofs/endpoints_env_gate_proof.log` (still `APP_ENV=prod`, `/reader_success_unreachable=true`; F-21), `artifacts/proofs/success_writers_errors.txt`, `artifacts/reader/endpoints_snapshot.json`, `artifacts/core/purity/purity_report.json`, the canonical sanity log.

**Labels.** Mirror: 620 rows; 27 labelled rows (the 22 roster paths), all carrying `d84d99e1…`; the purity-report row has no `notes` (RP-3). The roster still holds 22 paths; the updater is unchanged.

**Stale-binding sweep (step 11).** `git grep -l -E '72fca4c3|64553c25'` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256`, `manifest_post.sha256`: no hit (exit 1). Informative: `docs/` outside `docs/ephemeral/` and `docs/pfcanon/` also has no hit; ten `docs/ephemeral/` records name them as history.

**New base.** `release_id` `d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7` is the refresh base for WU-PR-04 and WU-PR-05 (contract E-3); `72fca4c3…` is historical. Admission constants, version and the 22-path roster are unchanged.

## 9. Local validation (plan §10)

Environment: CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .`); readiness `python -m pytest --version` → `pytest 8.4.2`; `ruby 3.3.6 (2024-11-05 revision 75015d4c1f) [x86_64-linux]` at `/usr/local/bin/ruby`; `bash` and `curl` on `PATH`; closed rails as §8; each run in a detached worktree of `006b43b` with `PYTHONPATH` set to it, ending with `git diff --exit-code` and an empty `git status --short --untracked-files=all`. The full sweep ran in its own worktree concurrently with the lane replications in another.

| # | Check | Result |
| :- | :- | :- |
| 1 | Classifier dry run, `18b3a16` → `006b43b` (full SHAs), `pull_request` | exit 0; 68 paths; lanes `product,compat,db,evidence,release`; `rails=false`, `qa=false`; `changed_tests=true`; 20 targets, exactly the plan's (F-24) |
| — | `ci/checks/check_env_pins.sh`; `python3 ci/checks/check_agents_md_citations.py` | exit 0; exit 0 |
| 2 | Changed-test step (the 20 targets, one process) | 854 passed (147 s); clean tree. The 20 targets include `tests/evidence/test_hdapi_v2_contract_inventory.py` (300 cases, `ruby` on `PATH`), `tests/http/test_endpoint_catalog.py` (204), `tests/http/test_reader_a7_transport.py` (27) and `tests/scripts/test_dev_start_reader.py` (10) |
| 3 | Product lane: `generate_ordering_artifacts.py --check`; its four test paths (incl. `tests/evidence/test_architecture_snapshot.py`) | ordering `--check` exit 0; 77 passed; clean tree |
| 4 | Compat lane: `check_cli_help.sh`; serializer grep guard and emitter symbol proof (outputs outside the tree); ten test files | three checks exit 0; 103 passed, 3 skipped, 2 xfailed; clean tree |
| 5 | DB lane: `check_direct_db_contract.py`; seven test paths | exit 0; 249 passed; clean tree |
| 6 | Evidence lane: updater `--check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh` (by path), plus `check_lf_endings.py`; six test files | eight checks exit 0; 130 passed (564 s); clean tree |
| 7 | Release-lane: `release_id_recompute.py --check-manifest-only`; four test files | recompute exit 0; 79 passed; clean tree |
| 8 | Attestation `--output <external empty dir> --require-clean`, then `--verify` | build exit 0 (183 s), verify exit 0; `validation_result: PASS`, `release_admission: PR06R_B_FINAL_PASS`, `release_id` = `manifest_sha256` = `d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7`, `source_commit` `006b43b5c924820b5cd03dcf1ff32425c5ede9e4`, `source_commit_exact: true`; clean tree |
| 9 | `VERIFY.sh`, `APP_ENV=dev`, free `VERIFY_PORT` | exit 0, 12 of 12 tokens `_OK` (`SERIALIZER_ONE_LF`, `PREIMAGE`, `TWO_RUN_IDENTITY`, `AB_BA`, `READER_200_STATUS`, `READER_200_HEADERS`, `READER_200_ETAG_PRESENT`, `READER_200_ETAG_MATCH`, `READER_304_STATUS`, `READER_304_EMPTY_BODY`, `READER_HEAD_CL_MATCH`, `ETAG_INVARIANCE`) against the loopback runner; clean tree |
| 10 | `VERIFY.sh` without `APP_ENV` | exit 2; standard error `VERIFY_APP_ENV_NOT_DEV: run with APP_ENV=dev (effective: <UNSET>)`; standard output empty (0 bytes); clean tree |
| 10 (informative) | the 24 `_HTTP_READER_TEST_OWNERS` files plus `tests/scripts/test_dev_start_reader.py` and `tests/scripts/test_dev_sampler_healthcheck.py`, `APP_ENV` unset | 26 files, 804 passed (127 s); clean tree. No test depends on CI's `APP_ENV=dev` |
| 11 | Full sweep `python -m pytest -q -p no:cacheprovider tests` | 4,761 passed, 3 skipped, 2 xfailed, 0 failed (1,093 s); `git diff --exit-code` 0; no untracked file. The 3 skips (`tests/cli/test_showcompat_parity_and_identity.py` lines 108, 128, 150: "showcompat vendor calls require open rails") and 2 xfails (`tests/adapter/test_jsonschema.py::test_version_schema_ok_dev`, `::test_error_envelope_schema_on_unauthorized_prod`: "/internal/version untouched in PR scope") are pre-existing, in files this delta does not touch. Equal to the plan's rehearsal; cycle 1 had 4,747 passed with the same skips and xfails |
| 12 | Diff checks against `18b3a16` | outside `docs/ephemeral/`: exactly the 7 files of §7.1 and the 61 of §6.5 (68); `scripts/dev_start_reader.sh`: exactly the line-23 change; every plan §7.3 path: empty diff; `git diff --check`: exit 0 |
| — | Served-set enumeration at `006b43b` | 53 = 18 + 35 (§6) |
| — | Contract-inventory baseline (ID-4; F-23) | `tests/evidence/test_hdapi_v2_contract_inventory.py` passes with `ruby` in the changed-test step and the sweep; `tools/evidence/generate_hdapi_v2_contract_inventory.py` and `artifacts/vendor/hdapi_v2/**` unchanged |

Not selected and not run as lanes: rails and qa (F-24). Their test files ran in the sweep; `tests/qa/test_generate_epic_close_pack.py` passed (405 cases, in the sweep) (OBS-17). Not executed: hosted CI and the Codex code review (PR-35's); a second attestation build.

## 10. Requirement → proof (plan §9)

| Requirement / acceptance item (as overlaid) | Proof at PR-30 | Result |
| :- | :- | :- |
| S15 / (5) under classes (a)–(d) | enumeration test (18 + 35 = 53); retired-pin test (3); validator case; A7 `--check`; updater `--check`; catalog = mirror; `success_endpoints` unchanged | met locally (§6, §8, §9) |
| S10 / (2): exact `dev` | served test (1); refusal matrix (16); RC-1 before/after | met locally (§4, §7) |
| S10 / (2), last clause as 2.6 B-2 | `tests/scripts/test_dev_start_reader.py` | 10 passed in the changed-test step (with the new banner assertion) and again with `APP_ENV` unset in the informative run; its runner is reached on `127.0.0.1` |
| S09 / S10: the canonical runner meets the local capture profile | runner-profile test (2); CORS test (6); banner assertion; RC-1, RC-2; `VERIFY.sh` with `APP_ENV=dev` | met locally: runner-profile 2 and CORS 6 passed; banner assertion passed; RC-1 and RC-2 as §4; `VERIFY.sh` exit 0, 12 of 12 |
| AD-5 / (7) | admission `d84d99e1… 45 1.3.0`; two-pass digest; recompute; selected lanes replicated; attestation | met locally; hosted lanes are PR-35's |
| AD-6 | basis assertion; §5 | met |
| ID-4 (addendum 2.2) | contract-inventory test with `ruby` | met locally: 300 passed; baseline unchanged (F-23) |
| S02, S07, S18, ID-3, RP-1, RP-3 (delivered by #643) | the sweep; `check_cli_help.sh`; CLI conformance `--check`; `VERIFY.sh` | held: sweep 4,761 passed; `check_cli_help.sh` exit 0; CLI conformance `--check` exit 0 (both passes); `VERIFY.sh` exit 0 |

Hosted proof (the five lanes, the changed-test step and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) is PR-35's.

## 11. Stale documents, observations and carried items (not in this pull request)

Unchanged from plan v2.0 §18; this phase found nothing new.
- **Stale documents:** HDE Mechanics Guide §34 "Current repository posture" (bind, flags, CORS, `APP_ENV` default) and its `/api/reader?v=1` alias row; HDE Users Guide §4.1 (the `0.0.0.0` bind statement); HDE Schemas & Artifacts §8.8 population rule; HDE-CLI-API-Vendor-Ref §5.6 "Implementation and acceptance state"; HDE Architecture §3.4 (Product Owner, canon doc-deltas); `docs/RUN.md` line 5 (OBS-P3-12; WU-DOC-01); `scripts/qa/dev_sampler_healthcheck.py` line 129 comment (OBS-P3-13; the IA); `AGENTS.md` and `README.md` start command and bind (WU-DOC-01); cycle 1's list (result v1.0 §9).
- **Observations:** OBS-P3-12 to OBS-P3-17 as plan v2.0 §18 states them, owner the whole-change IA, who routes them.
- **Carried:** AD-4's four gaps to WU-PR-05 (S19) with OBS-P3-3; WU-PR-08's port and bind statements; the refresh base `d84d99e1…` for WU-PR-04, WU-PR-05 and WU-PR-08 with the 22-path roster and step 3b; WU-DOC-01's start command and bind; from cycle 1, OBS-P3-2, OBS-P3-5 to OBS-P3-11, OBS-W3-1 (now addressed for the bind by AD-3; the production mount is AD-4's), LR-O1 and LR-O3 (applied in §8), LR-O2 (not triggered; every updater consumer ran in the sweep), OBS-17, O-6, AQ-1 (WU-PR-07 only).

## 12. In-flight decisions

| ID | What changed | Why it was necessary | Tested by (outcome) |
| :- | :- | :- | :- |
| D-1 | Publication order. Plan §8 step 10 lists "write the result record v2.0, commit it, push, and open the pull request". The two code commits were pushed and the pull request opened first; this record, which names the pull request and the post-publication read-back, was then committed and pushed | The PR-30 prompt requires the record to hold the PR reference and the read-back, and allows PR and commit references only after they exist; the handoff may not carry the only copy of a fact. Same precedent as cycle 1 and WU-PR-02 cycle 2. Cost: the first hosted run is superseded by the record push (pull-request concurrency cancels it) | this record read back after the push (§13); remote head verified |

## 13. PR_REMOTE_ACTION_LEDGER

| Time (UTC, 2026-10-14) | Action | Evidence |
| :- | :- | :- |
| before any write | open-PR listing; remote branch listing | none open; `claude/affectionate-euler-i70chn` absent on the remote |
| 07:37:37, 07:44:08 | local commits `95ff2b8` (source) and `006b43b` (convergence) | §4, §8 |
| 07:44–08:05 | local validation (§9) | all pass |
| 08:07:04 | before the push: `origin/main` `18b3a16` (fetched), branch `claude/affectionate-euler-i70chn`, clean tree, outgoing `95ff2b8`, `006b43b`; `git push -u origin claude/affectionate-euler-i70chn` (new branch) | `git ls-remote` → `006b43b5c924820b5cd03dcf1ff32425c5ede9e4` |
| 08:07:49 | created amthorn78/glow-hdengine-v2#646 (base `main`, head `claude/affectionate-euler-i70chn`, not draft), description with the template headings | https://github.com/amthorn78/glow-hdengine-v2/pull/646; read back: open, not draft, not merged, head `006b43b5c924…`, base `18b3a162db9b…`, 2 commits, 68 files (+239/−157), `mergeable_state: clean` |
| after this record is written | record commit and push (`docs/ephemeral/` only) | read back below; the pushed head is verified by PR-35 at entry |
| — | Reviews read | none (PR-35's) |
| — | Hosted CI | not observed (PR-35's). The run started for `006b43b` is superseded by the record push; the workflow's pull-request concurrency cancels it (D-1). The record push also selects the five lanes, because the classifier compares base to head |
| — | Mergeability | `clean` at 08:07:49 for `006b43b`; PR-35 re-reads it on the current head |
| — | Remaining useful local action | none for PR-30 |
| — | Next evidence action | PR-35: subscribe to #646; read the Codex code review and the CI on the current head |

## 14. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex code review findings on the pull request (addendum 2.3: no Codex security review) | PR-35 | pending |
| Hosted CI on the current head: product, compat, db, evidence and release lanes, the changed-test step, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; O-6 (hosted `ruby` version) if the log shows it | PR-35 | pending |
| Mergeability and readiness (`MERGE_PENDING`) | PR-35 | pending |
| Restart rules for any correction | PR-35 | a member change re-runs plan §6.5 from step 2; an evidence-primary change from step 3b; steps 3b to 10 byte-stable on a second run |
| Merge | Nathan only | — |
| Lineage review across #643 and this pull request; WU-PR-03 acceptance | the whole-change IA (PR-40) | after the merge |
| AD-4's four gaps | WU-PR-05 (S19) through its instruction | carried |
| OBS-P3-12 to OBS-P3-17, the doc-delta candidates, WU-DOC-01 items | §11 owners | recorded |
| Persistence of prompt-use provenance | Product Owner (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) | pending, non-gating |

Constraints preserved throughout: closed rails; no live vendor, production or database call; no hand edit of a governed artifact; no skipped, deselected, `xfail`-marked or quarantined test; no canon edit; no Specification edit; no PF10 addendum; no route added, removed or re-gated other than the `/reader` comparison; no production-factory, public-contract, admission-constant or version change.

## 15. Canon-conflict register

`CANON_CONFLICT_REGISTER`:

| ID | Classification | Status | Decision owner | Record |
| :- | :- | :- | :- | :- |
| CR-1, CR-2, CR-3 | CANON_RECONCILIATION | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | CANON_RECONCILIATION | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | CANON_RECONCILIATION | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | CANON_RECONCILIATION | APPROVED, alternative (a) | the IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7 | CANON_RECONCILIATION (S15, IF-6/EC-8 vs HDE Architecture §3.5) | APPROVED, alternative (a): exclusion under canon | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7; applied by §6 |
| CR-8 | CANON_RECONCILIATION (instruction §9.2 vs explicit `APP_ENV=dev`) | APPROVED, alternative (a): exact comparison | same | same; applied by §7 |

No new conflict was found during implementation.

## 16. Nonclaims

- CI green, local or hosted, is not QA. No QA artifact was created; `audit/qa/hde-crd-0002/` is untouched.
- No route, production-factory or public-contract change. The three canon-retired routes stay mounted and behave as before; their production exposure is AD-4's (WU-PR-05).
- WU-PR-03 is not accepted by this record or by a merge; PR-40 decides across #643 and this pull request.
- No new evidence family; no deployment, Ops, PF09 or PF30 status movement, release activation or closure.
- #643's description and claims are unchanged and are not restated as this cycle's.

## 17. TypeSafe reading and surface advice for the receiving session (PR-35, WU-PR-03 corrective)

PF10 addendum 2.1 governs. Run once, before this record was saved, with the step label "PR-35 HDE-CRD-0002 WU-PR-03 corrective (plan v2.0)".

**Action sent (v6):** "Continue, in a new dedicated session, an already published and locally validated corrective pull request for one work unit of an approved change (seven hand-edited files, among them one release member, plus about sixty owner-regenerated evidence files from a same-version release re-cut): read the automated code review and any review threads on it for the first time, fix every in-scope finding locally, and, if a finding touches the release member or an evidence producer, re-run the fixed-order governed-evidence convergence of about thirty-five owner-tool runs and its byte-stability second pass before one coherent push; then verify that five CI lanes and the changed-test step pass on the exact current head, confirm mergeability, and write the phase result record and checkpoint. A complete task list exists; no live provider call occurs; the Product Owner's manual merge and an independent lineage review follow."

**The reading, as the skill printed it:**
- **TypeSafe v6: Opus 5.5, high.** Effort score 2.36 (confidence 0.73); rung probabilities low 0.00, medium 0.03, high 0.59, extra high 0.38, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.98 (confidence 0.96). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.03, Opus 5.5 at high 0.58, Opus 5.5 at extra high 0.37, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.01, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-14T07:45:34Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-14T07:45:34Z; HTTP 200 in 0.56 s; 4290 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none printed.

**Records:** the Notion row was not written, as PR-30 directs. Nathan's pick for PR-35: not stated. Nathan's pick for this PR-30 session: not stated (the reading for PR-30 is in plan v2.0 §21).

**Surface advice for PR-35** (execution surface only):
- **Session.** A new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt and GitHub access to the pull request; at entry it subscribes to the pull request's activity.
- **Environment, if a correction needs local re-runs.** Python 3.12 with CI's install (package-index access); `ruby` on `PATH` for the contract-inventory test; `bash` and `curl` for the start-helper owner test and `VERIFY.sh`. All were present in this session's container. The container sets `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL` and `GH_TOKEN`; unset them for every local run.
- **Run times observed in this phase** (the sweep ran concurrently with the lane replications, so both are slower than alone): full sweep about 18 minutes; evidence-lane tests about 9.5; changed-test step about 2.5; the two convergence passes about 2.5 each (149 and 150 s of step time); attestation build and verify about 3; the `APP_ENV`-unset owner set about 2.
- **Discipline.** Run any re-convergence in the branch's working tree only after member edits are committed; run every other check that can write tracked files in a detached worktree; invoke `ci/checks/*.sh` by path (F-25).
- **Access.** No live vendor, production or database access is needed.

## 18. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / PR-30 / result 2 (plan cycle 2), version 2.0 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18); corrective decisions AD-1 to AD-6 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08Z). Receiver contract read: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e (page state as of 2026-10-12T02:30:15Z) |
| role/stage | dedicated WU-PR-03 PR engineering session, plan cycle 2 / PR-30 |
| capture time | 2026-10-14T08:08:05Z |
| execution identity | https://claude.ai/code/session_01Ea8P6Cr5BxJmYS7gBcpj11 |
| inherited usage | PR-10 instruction 1 (instruction §20); PR-20 plans v1.0, v1.1 and v2.0 (plan v2.0 §22); RS-20 rescope reviews 1 and 2; PR-30 result 1 (result v1.0 §16); PR-35 result 1.1; the corrective decision record (§9) |
| pull request and commits | amthorn78/glow-hdengine-v2#646 (https://github.com/amthorn78/glow-hdengine-v2/pull/646; open, base main, not draft); `95ff2b8`, `006b43b`, and this record's commit |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating; owner the Product Owner) |

## 19. Next phase

PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e).
- **Session.** Its own new dedicated session (`session_disposition: NEW_DEDICATED`), entered from this phase's handoff, which Nathan pastes.
- **Continuity.** It continues amthorn78/glow-hdengine-v2#646 (https://github.com/amthorn78/glow-hdengine-v2/pull/646; open, base main, not draft) under the original Proceed for plan v2.0; it shares this phase's work unit, workspace, branch, pull request, instruction, plan, primary skill and recovery lineage.
- **Inputs:** this record; plan v2.0 and its companion diff; instruction v1.0; the corrective decision record v1.0; addendum records 2.6 and 2.7; the immutable Specification v1.1, Implementation Plan v1.1 and review v1.1; PF10 as resolved at entry.
- **Branch and head.** PR-35 verifies both at entry from the pull request.

## Canon relied on

Read on `main` at `18b3a16` (`docs/pfcanon/` unchanged since `79eac95`).

| Topic | Sources and sections |
| :- | :- |
| Phase authority, Proceed, results, handoff | PR-30 — PR Implementation Proceed — 100926.1 (read in full); PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (read in full, receiver contract); skill glow-hde-pr-development 1.4.0 |
| Overlays | PF10-HDE-Build-Notes v13.5.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md`): front matter §§1–9, cross-references, index, addenda 2.1, 2.2, 2.3, 2.5, 2.6, 2.7 (read in full) |
| AD-1 | HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §3.5 in full; HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`) §1.1 in full; the remaining AD-1 sources as plan v2.0 "Canon relied on" maps them, relied on through the plan's trace and not re-read here |
| AD-2, AD-3 | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.4 in full; HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §34 in full; the remaining sources as plan v2.0 maps them |
| AD-5 | Implementation Plan v1.1 §10; addenda 2.6 (RP-2, RP-3) and 2.7 AD-5; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" |
| AD-6 | `AGENTS.md` canon-first rule; plan v2.0 §17 |
| In-flight documents | plan v2.0 and its companion diff (in full); corrective decision record v1.0 (in full); PR instruction v1.0 (in full); result v1.0 (structure and §5) |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails; pytest readiness; sole Index/Mirror writer; no hand edits; Endpoint Catalog source of truth; PR descriptions; evidence attribution; truncation guardrail) |
