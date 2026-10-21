---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-05-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 1 (first plan for this work unit)
predecessor: none
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0-prototype.diff (the prototype's diff from 1e97ba9 for the 21 hand-edited paths of §8.1; owner-produced paths excluded; §4.4)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-05
work_unit_title: "Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation; S19)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob ee5acb997fcc; 87,354 bytes; landed by amthorn78/glow-hdengine-v2#654 at 1e97ba9)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — §6 S19 and Appendix B bind this unit
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10). None is rewritten
applicable_pf10_overlays: PF10 addendum 2.3 (reviewer chain without the Codex security review; Rule 3 names this recorded review as an unchanged security deliverable that adds no review tooling); 2.7 AD-4 (the four non-public-route gaps decided once, here) and AD-5 (refresh order and restart rules); 2.6 (22-path label roster; step 3b and its restart point); 2.5 (LR-O1 to LR-O3); 2.8 (the WU-PR-03 acceptance and its carried items); 2.9 (the WU-PR-04 acceptance, the refresh base 2f18a5eb… and its "Carried into the WU-PR-05 instruction" list). 2.1 governs §22 only. 2.2 (ruby) and 2.4 have no other item for this unit
effective_baseline: approved base + applicable PF10 overlays = the base above + addenda 2.3, 2.5, 2.6, 2.7 (AD-4, AD-5), 2.8 and 2.9, as instruction v1.0 applies them
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md (v13.6; blob f6f80d8779e8; 167,152 bytes; sha256 4ecdd9caf9dc172ecb07ab0c577b400ca7a96cc18cef4421448b99dd94fe28aa). Resolved afresh on main at 1e97ba9: the unique controlled PF10; unchanged since 86e002c (git diff 86e002c 1e97ba9 adds only the instruction)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md §2.3, §2.5, §2.6, §2.7, §2.8, §2.9; §2.1 for §22
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (the dedicated HDE-CRD-0002 WU-PR-05 PR engineering session, created by Nathan / Product Owner)
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); authoring session https://claude.ai/code/session_01FtgUXCdmFGLWASrRUWaDjc
author: dedicated HDE-CRD-0002 WU-PR-05 PR engineering session (PR-20)
return_owner: the continuing whole-change HDE-CRD-0002 Implementation Agent (PR-40 after the merge; RS-20 for any rescope; PR-10 for an instruction defect)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-18T19:29:00Z
repository_baseline: origin/main 1e97ba9b0c9f274192385068f0b71a0e7a904fa8 (tree d9bbd85515d1; #654). git diff 86e002c 1e97ba9 changes only the instruction under docs/ephemeral/, so every non-docs/ byte equals 86e002c and 5892538 (#651); all 49 review-path blobs equal instruction §5.1 (§4.1)
reviewed_head: 1e97ba9b0c9f274192385068f0b71a0e7a904fa8 (the merge of the instruction's pull request, as instruction ID-2 expects)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§18)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-05 — Detailed PR Implementation Plan v1.0

## 1. State and authority

**AWAITING_PO_PROCEED.** Held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.1.1).

This is the complete, executable plan for WU-PR-05 (S19). It contains:
- **the code security review itself**, performed read-only by this PR-20 session on `main` at `1e97ba9`, as instruction ID-2 assigns: the 49 per-file lines, the checklist, the findings table with dispositions, the named-input table, the observations and the PF27 route-policy statement (§5);
- **nine confirmed findings fixed here** (S19-F01 to S19-F09), each with its design, regression tests and a recorded negative control (§7, §4.3);
- **seven confirmed findings routed** with owner and reason (S19-R01 to S19-R07);
- the same-version release refresh at `1.3.0` that five member changes force, rehearsed twice byte-identically (§9);
- the S19 record PR-30 writes from §5 (§14).

Every fix was prototyped in a scratch worktree, the refresh rehearsed in two passes, the result swept in full and checked (§4.3, "Checks run by this session").

Authority:
- Only Nathan's `PR Implementation Proceed` (PR-30) for exactly `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md` (v1.0) authorizes implementation. Only Nathan merges.
- This plan authorizes no implementation, merge, publication, Ops, QA, acceptance or closure. It changes no canon and creates no PF10 addendum. The routed findings are not decided by this plan.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-05 (Plan v1.1 §7 "WU-PR-05 — Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation)") |
| Requirement | S19 (source 6(b), RA-09) |
| Binding IA decisions | instruction §4.2 ID-1 to ID-11 |
| Upstream units | WU-PR-01 (addendum 2.4), WU-PR-02 (2.5), WU-PR-03 (2.8), WU-PR-04 (2.9): all accepted |
| Refresh base | `release_id` `2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76` (addendum 2.9; manifest sha256 at `1e97ba9`); `FROZEN_OPEN_ABBA_SHA256` `9949ddf5fe7e5d329a6d9a49bea916a9ff369ba6dd058de18b7cf7df9556098f` |
| Downstream | WU-PR-08 cuts `1.4.0` from this unit's `release_id` (F-1); QA-10 and the QA Plan read the S19 record (F-2); the QA Plan, WU-PR-08 and WU-DOC-01 read the production route exposure (F-3); the Product Owner and named owners receive the routed findings (F-4); WU-PR-06 reads classifier registrations: none added (F-5) |
| Phase | Distillation |
| Live QA class | "inherits the class of each fixed surface" (Specification table; Plan §6): per fix in §5.4 |

## 3. Sources read

Read completely by this session:
- PR-20 — Create Detailed PR Implementation Plan — 100926.1 (Notion, page state 2026-10-12T02:29:47.327Z).
- PR instruction v1.0 (all 20 sections and "Canon relied on").
- PF10 v13.6: addenda 2.1, 2.3, 2.7 and 2.9 in full; 2.5, 2.6 and 2.8 for the refresh rules and carried items they hold, as instruction v1.0 states them.
- Specification v1.1: rows S02, S09, S10, S15, S19; Exclusions; Constraints (all, including "Security review", "Dev route", "Release members"); the Live QA class table.
- Plan v1.1 §3, §4, §7 (common paragraph, WU-PR-05 block), §10, §11 (R-5), §12 to §15; Audit §6 S19 and Appendix B.
- WU-PR-04 plan v1.0 (structure precedent; §6.13 refresh table) and result v1.0 §9 and §10.
- Canon on `main` (section list in "Canon relied on").
- Code read in full by this session: `adapter/factory.py`, `adapter/wsgi.py`, `adapter/http_reader.py`, `engine/http/compat_handler.py`, `engine/runtime/public.py`, `engine/emit_public.py`, `engine/config/__init__.py`, `presenter/reader_v1/emitter.py`, `engine/compat/error_tokens.py`, `engine/compat/errors.py` (context), `engine/bodygraph/mapped_cache.py`, `engine/bodygraph/ingest.py`; in the parts §5.6 names: `engine/bodygraph/resolver.py`, `engine/bodygraph/projection.py`, `engine/bodygraph/v2_adapter.py`, `engine/cli/main.py`, `engine/compat/compute.py`, `engine/bodygraph/vendor_client.py` (context), `adapter/env_guard.py` (context), `engine/narratives/composer.py` and `preview.py` (context).
- The other 31 review paths were read in full by four read-only worker sessions inside this session (§5.1 "Method"), and this session re-read the cited lines of every candidate it classifies.

## 4. Repository baseline (verified at `1e97ba9`)

### 4.1 Instruction facts re-verified

- `git diff --name-only 86e002c 1e97ba9` is the instruction alone.
- The 49 review paths and their blob IDs at `1e97ba9` equal instruction §5.1 exactly (programmatic comparison of all 49 rows).
- Manifest: `1.3.0`, `built_at_utc 2026-08-24T18:04:49Z`, 45 members, sha256 `2f18a5eb…`.
- The production-factory probe of instruction §5.3 reproduces at `1e97ba9` row for row (probe P-4, §4.2).
- `Procfile`: `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30` (instruction §5.3 quotes it without the interpreter prefix; same command).
- Baseline full `tests/` sweep at `1e97ba9` (this session): **4,918 passed, 3 skipped, 2 xfailed, 0 failed** (1,037.7 s; 17:05:59Z to 17:23:18Z), exit 0, then an empty `git status`. Equal to the WU-PR-04 lineage review's count on `5892538`.

### 4.2 Facts this session established (not in the instruction)

| ID | Fact | Effect on the plan |
| :- | :- | :- |
| P-1 | `POST /api/reader` (production factory, `APP_ENV=prod`) with a 32,768-byte body of `[` (inside the 32 KiB limit) answers **500 `text/html` with no `Cache-Control`**: `json.loads` raises `RecursionError`, which `_parse_reader_post_body`'s `except (UnicodeDecodeError, ValueError)` does not catch. Shallower nesting (100 to 5,000) answers the governed 422. The same holds for `{"a_id":` followed by 20,000 `[` | S19-F01 |
| P-2 | With `SAFE_MODE` unset (or `2`) and `ALLOW_NETWORK=1`, `resolve_bodygraph` treats the SAFE rail as open: in `APP_ENV=prod` without the flag it runs the override matrix and appends a `refused` event; with a valid flag it appends `allowed` then `failed`. The socket layer (`vendor_client.HdApiClient._default_request`, exact `SAFE_MODE == "0"` and `ALLOW_NETWORK == "1"`) refuses before any socket, so no I/O occurred (socket and DNS guarded in the probe). `ALLOW_NETWORK=true` with `SAFE_MODE=0` behaves the same way | S19-F05 |
| P-3 | One legacy-route `bg:resolve --source vendor --dry-run` (non-production, fake transport, sockets blocked) appended three lines to the **tracked** `artifacts/ingest/retry_trace.log` in the working tree: `ingest_vendor_bodygraph` defaults to the working-directory-relative `RETRY_LOG` and `SUCCESS_LOG`, and the production-override path passes `log_path=RETRY_LOG`. `tests/evidence/test_open_rails_abba_proof.py` names these files "governed logs" that a live run must leave unchanged | S19-F06 |
| P-4 | Production factory under `APP_ENV=prod`: instruction §5.3's table holds. The dev/admin gate passes ` dev`, `dev `, `Dev`, `DEV`, `test`, `TEST `, `local` (sampler reaches its 415) and refuses `prod`, `production`, `live`, `x`, empty and unset | S19-F02, S19-F03 |
| P-5 | `hdctl dev:sampler` passes its gate for `DEV`, `Dev` and `TEST` (reaches candidate validation) and refuses ` dev`, `dev `, `prod` and empty (`DEV_ADMIN_ONLY`): `_ensure_dev_admin_env` case-folds without trimming | S19-F02 |
| P-6 | `hdctl showcompat` with 30,000 `[` on stdin, as a pair file or as party files exits 1 with `CLI_UNEXPECTED:maximum recursion depth exceeded while decoding a JSON array from a unicode string`; an undecodable pair file gives `CLI_UNEXPECTED:'utf-8' codec can't decode byte 0xff in position 0: invalid start byte` | S19-F07 |
| P-7 | Gap 4: in `adapter/http_reader.py::create_app`, no `/internal/` response carries an `ETag` and `HEAD`/`OPTIONS /ops/writer/diagnostic` already set `Content-Length: 0`; the dead hook has no observable effect | named input 4 (§5.5) |
| P-8 | `adapter/wsgi.py`'s 405 (`DELETE /internal/version`, `PUT /aux/narrative`) carries no `Allow` | OBS-P3-3 (§5.5) |
| P-9 | `/aux/narrative` with CR/LF in `category`, `release_id`, `pack_sha`, `perspective`, `viewer_top`, or a 100,000-character category, answers 200 with no query value reflected in any header; `release_id` and `pack_sha` are hex-validated in `engine/narratives/composer.py` | no finding (§5.6 row 3) |
| P-10 | Production served set (`APP_ENV=prod`, `/static` excluded; a pair is a method a rule accepts): `adapter.factory` and `adapter.http_reader.create_app` 21 URL rules and 49 `(method, path)` pairs, `adapter.wsgi` 23 and 55, at `1e97ba9` and unchanged with D-1, which adds and removes no rule. Every pair requested under `APP_ENV=prod` on both: exactly the nine canon-retired pairs change their answer (to the governed `ERR_NOT_FOUND` 404, the bytes an unknown path gets), and `GET /internal/version`'s body carries the refreshed `release_id`; every dev-harness pair keeps its refusal bytes and every automatic `OPTIONS` answer keeps its status and `Allow` set (Flask orders `Allow` differently from run to run). Non-production postures are unchanged | F-3 contract |
| P-11 | `engine/bodygraph/resolver.py` has no module-level `Path` import; the former `RETRY_LOG` import becomes unused under S19-F06 and is removed | §7.6 |
| P-12 | The refresh changes 56 paths, two more than WU-PR-04's 54: `artifacts/core/purity/purity_report.json` and its path proof, because the purity report binds the source digest of `engine/config/registry_loader.py`, which S19-F08 changes. The purity rows stay unlabelled | §9 expected set |
| P-13 | Two governed static analyzers read the adapter's route and hook registrations and fail closed: the architecture snapshot (`tools/evidence/generate_architecture_snapshot.py`, proven by `tests/evidence/test_architecture_snapshot.py`) and the EPIC034 adapter-boundary analyzer (`tools/evidence/hdapi_v2_boundary_analyzer.py`, proven by `tests/evidence/test_hdapi_v2_contract_inventory.py`). The first F03 prototype (a `Blueprint` subclass whose setup state swapped views, registered by the three factories with `**options`) failed 12 of their tests in the full sweep: `super().add_url_rule(...)` is an unclassified route registration, `register_blueprint(..., **options)` leaves every route of the blueprint unproven, and a call-registered `before_request` hook is accepted only when each return is `None` or a direct presenter-backed helper call such as `_error(...)` (a wrapper helper, `_writer_error` or a raised `NotFound` is not). D-1 as planned (§7.3) passes both; their results equal the baseline's except source digests and line numbers | §7.3 shape; RK-8 |
| P-14 | Under D-1's production mount a doubled-slash spelling of a guarded path (`/ops//probe/env`) gets Werkzeug's 308 redirect to the canonical path, which then answers the governed 404 (`/dev//sampler/conjunction` then answers its 403); at `1e97ba9` the same redirect led to the 200 process probe. A trailing slash answers 404 directly | §7.3 limits |
| P-15 | Three CI guards bind every test module to the classifier's owner registries: `tests/evidence/test_http_reader_ci_ownership.py` (a test that imports `adapter.http_reader` must be registered in `_HTTP_READER_TEST_OWNERS`), and in `tests/evidence/test_rails_ci_workflow_integration.py` the coverage guard (every tracked test module reached) and the full-validation roster guard (every module under a configured pytest root in a fixed lane or the supplemental roster). Four new modules failed all three in `e3129b7`'s full sweep. Registering them changed four exact pins in that file: the selection of `adapter/http_reader.py`'s owners, the owners of `engine/config/registry_loader.py` (two pins) and of `tools/config/generate_config_artifacts.py`. Instruction ID-11 keeps every registry pin true | PD-13 |

### 4.3 Prototype (this session; scratch only, never pushed)

Copies used, all in the session scratchpad:
- the baseline worktree of `1e97ba9` (probes, the baseline sweep and the pre-existing-failure comparison; never edited);
- a prototype worktree of `1e97ba9` (edits; scratch commits on a detached head, never pushed). The final pair is `2280dea` (source) and `a2957ae` (convergence). Three earlier pairs (`771ea9b`/`574abeb`, `179bd4e`/`cd1a84e`, `e3129b7`/`a93c62b`) carried superseded designs (below) and are not evidence for this plan, except where a row names `e3129b7`, whose member bytes `2280dea` keeps;
- a sweep worktree of `a2957ae`;
- per-copy CPython 3.12.3 venvs with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .` of the copy under test), pytest 8.4.2, Flask 2.3.3; `ruby` 3.3.6 at `/usr/local/bin/ruby`, `bash`, `curl`.

Closed rails throughout: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; unset by name: `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `ENGINE_ENV`; `XDG_STATE_HOME` pointed at an empty scratch directory. Open-rails values appear only inside monkeypatched tests with fake clients and in the fixture-mode open-rails proof with keys absent.

**Design revisions during prototyping.**
1. The first S19-F03 prototype, a `Blueprint` subclass whose setup state swapped views, registered by the three factories with `**options`, failed 12 tests of the two governed analyzers in its full sweep (P-13).
2. The second, the registration-callback hook of §7.3 without its automatic-`OPTIONS` exemption, passed both analyzers. The served-set probe (P-10) then showed automatic `OPTIONS` on `/reader` and on the three conjunction paths turning from Flask's 200 into the refusal (400 or 403); the exemption restores it (PD-15).
3. The third (`e3129b7`) put the regression tests in four new modules. Its full sweep failed three CI coverage and ownership tests (P-15). Registering the modules would have changed four exact pins, so the tests moved into 13 existing owner modules (PD-13). The member bytes did not change.

Every result below is from the final pair unless it names `e3129b7`.

**Before the cut** (source `2280dea`): the affected directories (`tests/http`, `tests/adapter`, `tests/transport`, `tests/bodygraph`, `tests/cli`, `tests/scripts`, `tests/config`, `tests/compat`, `tests/reader_v1`, `tests/runtime`) and the two analyzer test files gave 2,497 passed, 3 skipped, 2 xfailed and 17 failed. Each failure is a refusal of the not-yet-cut manifest: admission's member-hash check, the Magic10 `ERR_M10_MANIFEST_MISMATCH` 503, the updater's `CURRENT_RELEASE_LABEL_MANIFEST_INVALID`, or a script whose run needs admission (`VERIFY.sh`'s Reader 200 check, the recompute write). They are the same 17 as on `e3129b7`, and all pass on the converged commit (full sweep). No existing assertion changed.

**New tests**: 267 cases, all named `test_s19_*`, added to the 13 existing modules of §8.1. All pass on the prototype, and the 915 tests of those modules pass.

**Negative controls**, each on the prototype with one fix disabled, run over the 267 `test_s19_*` cases of the 13 host modules (`-k s19`), then the file restored and its bytes re-checked:

| ID | Fix disabled | Result (of 267) |
| :- | :- | :- |
| NC-01 | S19-F01 Reader parse (`RecursionError` removed) | 12 failed, 255 passed |
| NC-02 | S19-F01 writer helper parse | 1 failed, 266 passed |
| NC-03 | S19-F01 compat parse | 1 failed, 266 passed |
| NC-04 | S19-F02 HTTP gate (strip and lower restored) | 24 failed, 243 passed |
| NC-05 | S19-F02 CLI gate (lower restored) | 4 failed, 263 passed |
| NC-06 | S19-F03 production mount (`bp.record(_mount_for_production)` removed) | 18 failed, 249 passed |
| NC-17 | S19-F03 retired path, method no rule names (the `MethodNotAllowed` clause removed) | 3 failed, 264 passed |
| NC-18 | S19-F03 automatic-`OPTIONS` exemption removed | 3 failed, 264 passed |
| NC-07 | S19-F04 bounded read (`get_data` restored) | 1 failed, 266 passed |
| NC-08 | S19-F05 resolver rails (truthy reading restored) | 30 failed, 237 passed |
| NC-09 | S19-F05 ingest rails | 9 failed, 258 passed |
| NC-10 | S19-F06 ingest log defaults (`RETRY_LOG`, `SUCCESS_LOG` restored) | 3 failed, 264 passed |
| NC-11 | S19-F06 override log path (`log_path=RETRY_LOG` and its import restored) | 1 failed, 266 passed |
| NC-12 | S19-F07 CLI JSON parse (`_parse_input`) | 2 failed, 265 passed |
| NC-13 | S19-F07 CLI catch-all (`CLI_UNEXPECTED:{exc}` restored) | 2 failed, 265 passed |
| NC-14 | S19-F08 loader path rule | 6 failed, 261 passed |
| NC-15 | S19-F08 cutter path rule | 6 failed, 261 passed |
| NC-16 | S19-F09 report-path rule | 1 failed, 266 passed |

**Refresh rehearsal** (§9) on `e3129b7`, whose member bytes `2280dea` keeps:
- Pass 1 (steps 2 to 10) ran 37 commands and pass 2 (steps 3 to 10) ran 34. Every command exited 0, and sanity gave `summary:PASS` both times.
- After each pass 56 paths differ from the source commit and no untracked file exists. They are the same 56 paths as §9 lists.
- The two `git diff HEAD` patches are byte-identical (SHA-256 `234f053fe646085af065cffa94a6d646f3008cfaaf69ffa8fb5d8933708a36d7`).
- That patch applied to `2280dea` gives `a2957ae`. A third pass (steps 3 to 10, 34 commands, all exit 0) on `a2957ae` changed no byte.
- Rehearsal `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`: 45 members, `1.3.0`, `built_at_utc` unchanged. The five manifest rows that change are the five members of §9.
- Rehearsal open-rails digest `e8a47d53b4d9a145ebfc95163a85252c15a4fbddb12dc9dea380662aaa1cb73c`, equal to the new `FROZEN_OPEN_ABBA_SHA256`.
- Both are rehearsal values only: PR-30's bytes fix the real ones (PD-14).
- Mirror: 620 rows. 27 carry the rehearsal `release_id` and none carries `2f18a5eb`; the two purity-report rows carry no `notes`.
- Step 11 sweep for `2f18a5eb|9949ddf5`, outside the excluded prefixes and in `docs/` outside `docs/ephemeral/` and `docs/pfcanon/`: no hit.

**Classifier** on the rehearsal candidate (`1e97ba9` → `a2957ae`, `pull_request`):
- `reason=selected_lanes`; 77 paths;
- lanes product, compat, db, rails, evidence and release; `qa=false`;
- `needs_python=true`, `changed_tests=true`; 39 changed-test targets.

Ten of the 13 host modules are changed-test targets. The other three are fixed-lane providers in lanes this change selects:
- `tests/bodygraph/test_ingest.py` runs in db;
- `tests/cli/test_cli_usage_and_errors.py` and `tests/http/test_compat_endpoint_contract.py` run in compat.

No path is unclassified, and no registration is needed (F-5: none).

The full sweep, the read-only checks and the attestation on the converged prototype are in "Checks run by this session".

### 4.4 Prototype diff (companion file)

`docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0-prototype.diff` is `git diff 1e97ba9 2280dea`: the 21 hand-edited paths of §8.1 (1,215 lines; SHA-256 `5081ded3b8ce1db03bae4e19075d55ca4a90f8369170fd5365f5bde7842d5cc5`). The manifest, the `FROZEN_OPEN_ABBA_SHA256` line and every regenerated governed artifact are excluded: PR-30 produces them with their owners. `git apply --check` succeeds on `1e97ba9`.

PR-30 may apply it as its starting point, but owns the implementation:
- it re-reads every hunk against this plan;
- it re-runs §12 on the real branch;
- where the diff and this plan differ, this plan governs, and the difference is a defect PR-30 corrects.

## 5. The S19 review (instruction ID-1 to ID-8)

This section is the review's content. PR-30 transcribes it into the S19 record (§14) and adds only the commit identities and run results that exist after implementation.

### 5.1 Scope, reviewed head and method

- **Paths.** The 49 paths Audit Appendix B names (its prose says 48; three sidecars are written as suffixes; ID-1, OBS-W5-1). Each has a per-file line (§5.6).
- **Bytes.** Current bytes on `main` at the reviewed head `1e97ba9b0c9f274192385068f0b71a0e7a904fa8`, including what PR06b, the four CI commits of 2026-09-27 and WU-PR-01 to WU-PR-04 changed in them (§5.6 "Later changes"; instruction §5.2). The blob of each path is in §5.6.
- **Context reads.** Tests, callers and callees outside the 49 are read as proof or context and get no per-file line (ID-1).
- **What counts.** A finding is a defect located in, or reached through, code of the 49 paths; its fix may change a path outside them (ID-1). `engine/bodygraph/vendor_audit.py` is context only (LR4-O4).
- **Method.** Manual review with repository tooling only: reading, `git`, `grep`, the Python standard library and the repository's own tests and tools, under closed rails, with probes in scratch copies (Flask test client; no live vendor, production or database call). No scanner, linter or analyzer was run, installed or added (Exclusions bullet 6; addendum 2.3 Rule 3).
  - This session read 18 of the 49 paths itself (§3).
  - Four read-only worker sessions, run inside this session under one written brief (the eight-item checklist, the confirmation rule of ID-4, read-only rules, own throwaway worktrees, no write-mode generator, never the EPIC030 generator), read the other 31 in full and reported per-file results with line citations. Every worktree they used ended with an empty `git status --short --untracked-files=all` and was removed.
  - This session re-read the cited lines of every candidate it classifies and ran its own probes for every finding fixed here.
- **Limits.** Static reading plus closed-rails probes: no deployed-service, live-vendor or database behavior is observed. Platform behavior outside the repository (GitHub path-filter limits, Railway configuration, branch protection) is not observable. Race conditions were reasoned from code, not run.

### 5.2 Severity scale (instruction ID-4)

| Level | Criterion |
| :- | :- |
| High | Exploitable now by an unauthenticated network client against the production application, with a secret, PII, write or vendor-call consequence |
| Medium | Reachable now on the production application by an unauthenticated client and violating a canon security or error-contract requirement, without a secret, PII, write or vendor consequence; or a production-mounted surface whose only control against such a consequence is a check that does not meet canon |
| Low | Reachable only by an operator, a CI job or a local user (CLI, tools, dev, test or local deployments), or only after a further misconfiguration; consequence limited to integrity of local or governed evidence, refusal-code accuracy or defence in depth |
| Informational | No reachable exposure found; a latent pattern, or a deviation from canon wording without effect |

### 5.3 Threat checklist

The eight items of Audit §6 S19, mapped to canon exactly as instruction §4.1 maps them: T1 input bounds and body limits; T2 path and file handling; T3 environment gating and rails; T4 secret and keys-only logging; T5 error disclosure; T6 injection into audit or log lines; T7 concurrency and atomic publication for the evidence writers; T8 dependency and subprocess use. Where canon is silent the line states the observed behavior and judges the risk; silence is not a finding by itself. For T7 canon names no general atomic-replace rule for evidence writers, so each writer's actual behavior is stated.

### 5.4 Findings

**Confirmed, fixed here** (instruction ID-5 (a) to (f) hold for each; designs in §7):

| ID | File and line at `1e97ba9` | Description | Item | Severity | Canon or requirement | Evidence | Live QA class (surface) |
| :- | :- | :- | :- | :- | :- | :- | :- |
| S19-F01 | `adapter/http_reader.py` 485–491 (`_parse_reader_post_body`), 175–178 (`_read_writer_json`); `engine/http/compat_handler.py` 132 (`post_json`) | A JSON body nested past the parser's recursion limit raises `RecursionError`, which no handler catches: the production `POST /api/reader` (unauthenticated) answers 500 `text/html` with no `no-store` and a logged traceback; the writer helper and compat `POST` do the same on their surfaces | T1, T5 | Medium | HDE-CLI-API-Vendor-Ref §5.2 item 1 (every governed HTTP error emits `error_v1`), §5.2.3 table (invalid JSON → `ERR_READER_INVALID_INPUT` 422), §8.1 | P-1; NC-01 to NC-03 | Functional-feature: the production application that serves Reader v1 and v2 |
| S19-F02 | `adapter/http_reader.py` 826–832 (`_dev_admin_gate`); `engine/cli/main.py` 832–835 (`_ensure_dev_admin_env`) | The dev/admin `APP_ENV` gates normalize: the HTTP gate trims and case-folds (admits ` dev`, `DEV`, `TEST `), the CLI gate case-folds (admits `DEV`, `Dev`, `TEST`). Named input gap 3 | T3 | Low | HDE Governance §2.0.10 `ENV_RAILS_POLICY_OK` and "Dev/admin APP_ENV gating" ("exactly"); HDE-CLI-API-Vendor-Ref §5.11.2 ("exactly one of dev, test, or local"), §5.12 | P-4, P-5; NC-04, NC-05 | Functional-feature: the production application (the routes are mounted there) and the operator CLI surface |
| S19-F03 | `adapter/factory.py` 13; `adapter/http_reader.py` 1176 and the routes at 606–678, 756–820, 987–1078, 1123–1168; `adapter/wsgi.py` 23 | The production application mounts the dev harness (`GET`/`HEAD /reader`, `POST /internal/dev/sampler`, the three `/dev/*/conjunction` routes) and the three canon-retired `/ops` routes. Today, unauthenticated: `/ops/probe/env` returns the process id, its start time, the `SAFE_MODE`, `ALLOW_NETWORK` and `APP_ENV` values and whether a probe token exists; the harness code (fixture reads, Engine evaluation, vendor acquisition under the production open rails, idempotence writes) is reachable code behind one request-time check that S19-F02 shows does not meet canon; the retired writer checks bearers against test-token environment values. Named inputs gaps 1 and 2 | T3, T5 | Medium | HDE Architecture §3.2 "A7 proof surface" ("Non-prod entries must be unreachable in production"), §3.3 "Gating & posture" ("Harness is dev-only; never mounted in production") and "Current repository discrepancy", §3.5 "Current repository discrepancy" (`RETIRED/NONCANONICAL`), §1.3 "No leakage across boundaries"; HDE-CLI-API-Vendor-Ref §5.4 "Gate" ("must not be mounted in production builds"), §5.12 ("MUST NOT be available in production"); HDE Users Guide §1.1 ("Do not use as an operator workflow"); HDE Governance `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`; addendum 2.7 AD-4 | P-4, P-10, P-14; NC-06, NC-17, NC-18 | Functional-feature: the production application |
| S19-F04 | `adapter/http_reader.py` 155 | The writer JSON helper reads the whole body before its 32 KiB check when `Content-Length` is absent (a chunked request; werkzeug returns the raw stream when `wsgi.input_terminated` is set, as gunicorn sets it). Reached by the dev sampler after its gate and the retired writer after authentication; after S19-F03 neither handler is reachable in production | T1 | Low | the writer limit (`ERR_WRITER_REQUEST_TOO_LARGE`, "request body exceeds 32 KiB"; HDE-CLI-API-Vendor-Ref §5.11.3 "writer JSON helpers") | test with a counting stream; NC-07 | Functional-feature: the production application module |
| S19-F05 | `engine/bodygraph/resolver.py` 126–133, 174–175, 923–925; `engine/bodygraph/ingest.py` 56–61, 144–145 | The resolver and the ingest read the rails leniently: `SAFE_MODE` closes only for `1`/`true`/`yes`/`on` (unset, empty, `2`, `false` count as open) and `ALLOW_NETWORK` opens for `true`/`yes`/`on`. The production-override matrix, its audit events and credential projection then run under rails canon treats as closed; only the socket layer's exact check prevents I/O | T3 | Low | HDE-CLI-API-Vendor-Ref §7.1.2 (two-gate rule: exactly `SAFE_MODE=0` and `ALLOW_NETWORK=1`), §7.1.3, §7.1.11d (rails first); HDE Governance §3.1 "SAFE rails default ON" | P-2; NC-08, NC-09 | Functional-feature with the mandatory live vendor call: vendor ingest through `hdctl bg:resolve --source vendor` (the S14 class) |
| S19-F06 | `engine/bodygraph/ingest.py` 50–52, 138–139; `engine/bodygraph/resolver.py` 446–451, 461 | Vendor runs append to the tracked governed files `artifacts/ingest/retry_trace.log` and `artifacts/ingest/ingest_success.log`, resolved against the working directory: the non-production legacy call uses the ingest defaults, the production-override path passes `log_path=RETRY_LOG` | T7, T2 | Low | `AGENTS.md` (governed evidence produced only by its owners; no hand edits); the repository's own posture (`tests/evidence/test_open_rails_abba_proof.py` treats them as governed logs a live run must not change); HDE Engine Epics Map lists them as EPIC-011 evidence | P-3; NC-10, NC-11 | Functional-feature with the mandatory live vendor call (vendor ingest) |
| S19-F07 | `engine/cli/main.py` 324–326 (catch-all), 220–223, 331–334, 883–886, 949–952 | An unexpected CLI failure writes `CLI_UNEXPECTED:<exception text>` to stderr; JSON nested past the recursion limit (stdin, pair file, party files, candidates, viewer preferences) and undecodable input reach it | T5, T1 | Low | HDE-CLI-API-Vendor-Ref §3.3 and §8.2 (one LF-terminated code token on stderr) | P-6; NC-12, NC-13 | Functional-feature: the operator CLI surface |
| S19-F08 | `engine/config/registry_loader.py` 1076–1079 (rule), 1083–1087 (messages); `scripts/cut_release_manifest.py` 61–71 (rule), 146, 168 (messages) | The manifest path rules admit control characters, NUL included, and a refused path can be echoed raw into a message or stderr line (line injection). Admission's exact roster check refuses such a path before any file is opened; `load_manifest` (used by `scripts/release_id_recompute.py`) and the cutter accept it | T2, T6 | Low | HDE Math Spec §5.4.3 ("no … NUL"); HDE Governance §7.1.4 (log-line determinism) | worker probe (in-memory `_parse_manifest`; cutter `--check` on a crafted manifest printed a forged line); NC-14, NC-15 | Loader: functional-feature (release admission in the production application); cutter: not production-affecting (release tooling) |
| S19-F09 | `tools/config/generate_config_artifacts.py` 322 vs `tools/config/artifacts.py` 471 | The golden-comparison `--report` refusal compares the report with the candidate root resolved through symlinks, while admission uses the lexical absolute path; a `<symlink>/..` candidate argument lets the report land inside the admitted root | T2 | Low | HDE Mechanics Guide §25.6 and HDE Users Guide §7.6 ("`--report` writes only … outside both repository and candidate root"); `AGENTS.md` "HDE-EPIC040 current posture" | worker probe at the validator; NC-16 | Not production-affecting (read-only repository tooling) |

**Confirmed, routed** (ID-5: at least one of (a) to (d) fails, or the item lies in a frozen family; the owner decides):

| ID | File and line | Description | Item | Severity | Owner | Reason |
| :- | :- | :- | :- | :- | :- | :- |
| S19-R01 (OBS-W4-1) | `engine/cli/main.py` 747–753, 788–799; `engine/bodygraph/resolver.py` 905–1021 | `hdctl showcompat --source vendor`, and conjunction mode with any source but `db` or `auto`, acquire from the vendor under open rails with no production override, audit event or production gate. Production rails are open by default (Glow Infrastructure §2.4), so any production shell reaches it | T3 | Low | Product Owner (owner of HDE-CLI-API-Vendor-Ref) | ID-5 (a) and ID-7: §7.1.11a scopes the override to `bg:resolve`; `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK` admits CLI runs under explicit open-rails profiles; a gate would set policy canon does not state. Decision needed: whether production showcompat and conjunction acquisition must meet a production gate |
| S19-R02 (OBS-W4-3) | `engine/bodygraph/resolver.py` 676–694 → `engine/bodygraph/vendor_client.py` 100–153 | Route selection reads any path segment, case-insensitively, as the version: a nonterminal `v2` selects `charts` with the Bearer key; an unversioned or `v3` base selects legacy `bodygraphs` with the `HD-Api-Key` credential projected; userinfo, query and fragment are not refused | T1, T3 | Low | Product Owner | ID-7: a §7.1.10 fix reverses the posture that tests pin (`tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py` line 118 asserts the legacy fallback for an unversioned and a `v3` base; `tests/bodygraph/test_bg_resolve_route_policy.py` line 86; `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` line 237), that the governed EPIC038 evidence predicate `explicit_legacy_fallback` records (`tools/evidence/generate_v2_mapped_cache_evidence.py` line 275) and that `AGENTS.md` "EPIC036 docs posture", HDE Mechanics Guide §1.1 and HDE Users Guide §11.3 state; the frozen EPIC036 and EPIC037 captures would contradict it. The fix needs the Product Owner's decision on retiring that posture, with evidence and test owners |
| S19-R03 | `engine/http/compat_handler.py` 130–173 | `POST /api/compat/v1` returns the internal numeric result with no authentication; canon describes the success body as "after the production-excluding environment gate and internal authentication". Production answers 404 through the compat guard; a reachable non-production deployment (Glow Infrastructure §2.2 Staging/QA) would serve stored-UID results unauthenticated | T3 | Low | Product Owner | ID-5 (a): canon names no compat authentication mechanism (credential, scope or registry), so a fix would set policy |
| S19-R04 | `tools/errors/generate_error_artifacts.py` 319–320; `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` 243; `tools/evidence/run_sanity_pipeline_gate.py` 106 | Governed owner tools without argument parsing act on any invocation, `--help` included: the error-artifact generator rewrites tracked files, the release member `errors/token_map/token_map.json` among them, with truncate-then-write; the EPIC030 generator rewrites three frozen logs with wall-clock times and a different category order (OBS-W5-3); the sanity gate runs the canonical write pipeline | T7 | Low | Product Owner | ID-5 (a) and (d): each fix changes an owner tool's invocation contract, which no canon rule sets; the EPIC030 family is frozen and its regeneration belongs to its owner. Operator and CI-runner reach only |
| S19-R05 | `tools/evidence/run_sanity_pipeline.py` 333, 347; `tools/evidence/build_release_attestation.py` 178–191, 603–617, 907–912 | Unrestricted or non-exclusive write targets: `--log-path` follows symlinks and can overwrite a governed file; the attestation builder accepts any existing empty output root, follows symlinks on later writes and, on failure, removes `evidence/` and bundle files it did not create (a concurrent run's bundle was destroyed in the worker's probe) | T2, T7 | Low | Product Owner (owner of HDE Schemas & Artifacts §6.2.1 and HDE Mechanics Guide §27.3) | ID-5 (a): canon accepts an empty existing destination; exclusivity and ownership rules for the output root are an owner contract decision. Operator only; CI uses a fresh `$RUNNER_TEMP` path |
| S19-R06 | `tools/cli/generate_showcompat_artifacts.py` 104–109 | The frozen-family generator runs the relative `scripts/hdctl.py` with no `cwd`: run from another directory, it executes that directory's file with the full environment | T8 | Low | Product Owner (owner of the frozen `artifacts/cli/**` family) | ID-5 (d): the tool belongs to a frozen family (instruction §6); its governed callers pass `cwd=ROOT` |
| S19-R07 | `tools/evidence/run_canonical_json_gate.py` 1205 | A failing target validation records `validation_error:<type>:<exception text>` in the governed check rows, absolute local paths included, and write mode publishes them | T5 | Low | Product Owner (owner of HDE Governance §6.3.2 diagnostics rules) | ID-5 (a): the content rule for gate diagnostics is the owner's; reached only by a failing operator or CI run |

Every confirmed finding has a disposition: fixed here with a regression test and a recorded negative control, or routed with an owner and a reason (acceptance (2)).

### 5.5 Named inputs (instruction ID-6 and ID-7)

| Input | Canon basis | Evidence | Classification (ID-4) | Disposition (ID-5) |
| :- | :- | :- | :- | :- |
| Gap 1 — production mount of the dev harness and the `POST /reader` stub | HDE Architecture §3.2, §3.3 and its "Current repository discrepancy"; HDE-CLI-API-Vendor-Ref §5.4 "Gate", §5.12 | P-4; instruction §5.3 | Confirmed, part of S19-F03 | Fixed here (D-1). The stub stays: HDE-CLI-API-Vendor-Ref §5.4 "Production mount" and HDE Users Guide §6.4 state it as the production refusal (PD-2) |
| Gap 2 — the three canon-retired `/ops` routes, mounted and ungated in production | HDE Architecture §3.5 "Current repository discrepancy"; HDE Users Guide §1.1 | P-4 (`/ops/probe/env` 200 with process and rails state) | Confirmed, part of S19-F03 | Fixed here: in a production-like posture answered as an unknown path (the governed 404) before any handler; code kept (removal stays with its canon owner) |
| Gap 3 — `_dev_admin_gate` normalizes | HDE Governance "Dev/admin APP_ENV gating"; HDE-CLI-API-Vendor-Ref §5.11.2 | P-4 | Confirmed, S19-F02 (with the CLI gate) | Fixed here: exact comparison; refusal matrix of instruction ID-6 |
| Gap 4 — `adapter/http_reader.py::create_app`'s after-request hook never matches (`getattr(resp, "request", None)` is `None`) | none (no canon names the hook) | P-7: no `/internal/` ETag and the diagnostic 204/405 already carry `Content-Length: 0` | Not confirmed as a security finding (no observable effect). Non-security defect: dead code | Observation O-01 (§5.7); not fixed here (ID-4) |
| OBS-P3-3 — `adapter/wsgi.py`'s 405 emits no `Allow` | none in canon for this factory (RFC 9110 requires `Allow` on a 405) | P-8 | Not confirmed: `adapter/wsgi.py` is not the production factory; no exposure | Observation O-02 |
| OBS-P3-14 — `python-dotenv` would let `Flask.run` read a local `.env` | addendum 2.7 AD-3 (the runner's run-call arguments) | absent from `requirements*.txt` and CI's install; no `.env` or `.flaskenv` tracked; present only in this container's system Python, not in the CI-equivalent venv | Not confirmed | none |
| OBS-P3-17 — root helpers run the production factory with the debugger and reloader | HDE Architecture §3.8.1 "Current repository discrepancy" | `run_flask.py`, `run_flask_dev.sh` (outside the 49) | The part reached through `adapter/factory.py` is gap 1, fixed by D-1 (under a production-like `APP_ENV` no harness handler is reachable there either); the helpers' own settings are out of scope | Out-of-scope observation X-02 (§5.8) |
| OBS-W4-1 | HDE-CLI-API-Vendor-Ref §7.1.11a; HDE Governance `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK` | §5.4 R01 | Confirmed (realistic exposure path under T3) | Routed: S19-R01 |
| OBS-W4-3 | HDE-CLI-API-Vendor-Ref §7.1.10 and §7.2.0 | §5.4 R02 | Confirmed (violates §7.1.10) | Routed: S19-R02 |

### 5.6 Per-file lines (49)

Columns: attribution (merged by; later changes as instruction §5.1 lists them); member of the release (M); items that apply; what was read; result. "n/a" items are stated in the line.

| # | Path (blob at `1e97ba9`) | Attribution; M | Items | Read | Result |
| :- | :- | :- | :- | :- | :- |
| 1 | `.github/workflows/ci.yml` (`3836bad11c39`) | #467; 398276b, 735af8a, #627; no | T6, T8; T2 ($RUNNER_TEMP paths only); T4 (no secret referenced); T1, T5, T7 n/a (orchestration) | whole file; the classifier; the pin test | No finding. `pull_request` (not `_target`); `contents: read`; `persist-credentials: false`; the only `${{ }}` inside `run:` is `github.event_name`; no cache; changed paths reach the shell only through a quoted array. Not confirmed: CI1 (GitHub path-filter limits), CI3 (actions pinned by tag; `setuptools`/`wheel` unpinned) — observations O-11, O-12 |
| 2 | `adapter/factory.py` (`618a624dc4d4`) | #508; #643; no | T3, T5; T1, T2, T4, T6–T8 n/a (registration and error handlers only) | whole file | S19-F03 (line 13, the mount; the fix lives in the blueprint and this file is unchanged). Error handlers emit the governed envelope (S02) |
| 3 | `adapter/http_reader.py` (`a26feb9b48f4`) | #467, #508; #643, #646; M | T1–T6; T7, T8 n/a (no evidence writer, no subprocess) | whole file | S19-F01 (485–491, 175–178), S19-F02 (826–832), S19-F03, S19-F04 (155). Not confirmed: `_safe_load_chart` (resolve then prefix check; both refusals map to `ERR_READER_INVALID_PATH`, no existence oracle; the `is_symlink()` after `resolve` is dead, O-03); `_require_admin_scope` compares test tokens with `==` (dev-only after S19-F03; O-04); conjunction errors echo `provider_details` such as `str(URLError)` (dev-only after S19-F03; no secret content; X-04); the aux route reflects no query value (P-9). Gap 4 hook (O-01) |
| 4 | `adapter/schemas/error_v1.schema.json` (`720aa6738466`) | #501; M | T1, T5; others n/a (static contract) | whole file; its consumers | No finding. `details: {}` accepts any object (SC1); no leak found through it; observation O-13 |
| 5 | `adapter/wsgi.py` (`52fd4aedf1a9`) | #508; no | T3, T5 | whole file | S19-F03 (line 23, same mount; file unchanged). OBS-P3-3 (O-02). HSTS header decision normalizes `APP_ENV`, which only widens a header; no finding |
| 6 | `catalog/manifest.json` (`80364154c776`) | #467, #501, #508; #513, #643, #646, #651; identity source | T2 | whole file; `git ls-files -s` modes | No finding. Canonical bytes; 45 safe repository-relative POSIX paths, all mode `100644`, hashes and sizes equal to disk |
| 7 | `ci/checks/classify_ci_changes.py` (`3be620cbac91`) | all four; e1bff8d, 398276b, 2876fa0, 735af8a, #627, #643, #651; no | T1, T2, T6, T8; T3–T5, T7 n/a | 1–340, 960–1140, 1522–2055 read; registry tables skimmed | No finding. `git diff -z` with list argv; strict UTF-8; NUL/CR/LF, absolute and `..` paths refused; unknown surfaces fail closed (exit 2); `$GITHUB_OUTPUT` gets fixed keys only. CI2 (workflow filter's governed exceptions hard-coded): observation O-14 |
| 8 | `ci/checks/run_rails_job_definitions.py` (`ce25809df3e7`) | #467; no | T4, T6, T8; T3 (exact rails values) | whole file; `ci/jobs/*.yml` | No finding. List argv matched against an allowlist; credential-bearing arguments refused. Not confirmed: RR1, children inherit names outside its 8-name strip list under open rails (no path to I/O or output found; CI sets none; O-15); RR2 `python` from `PATH` |
| 9 | `ci/jobs/rails_open_conformance.yml` (`b1d3f056b3e4`) | #467; no | T3, T8 | whole file | No finding. Open rails for two allowlisted commands; no credential keys |
| 10 | `engine/bodygraph/ingest.py` (`68fb7b4a7d0a`) | #467; no | T2, T3, T4, T6, T7 | whole file | S19-F05 (56–61, 144–145), S19-F06 (50–52, 138–139). Log lines are `json.dumps` (no injection); content keys-only (`user_id` is a UUID or a UUID5) |
| 11 | `engine/bodygraph/mapped_cache.py` (`8741137ba14a`) | #467; M | T1, T5; T3, T4 | whole file | No finding. Parameterized SQL with fixed table names; value-free typed errors; read-back parity |
| 12 | `engine/bodygraph/projection.py` (`e28c47d8ee02`) | #467; M | T1, T5 | validators and `project_bodygraph` | No finding. Exact key sets, typed refusals; recursion depth bounded by its callers' JSON parse (S19-F01 covers the parse) |
| 13 | `engine/bodygraph/resolver.py` (`c3550c066094`) | #467; #651; M | T1–T6 | `resolve_bodygraph`, `_resolve_vendor`, `_resolve_vendor_route`, `_resolve_vendor_v2_chart`, `_vendor_config_env`, `_classify_env_route_policy`, `_acquire_dry_run`, `_resolve_stored` (lines 126–490, 617–735, 905–1072); the WU-PR-04 override steps 4 to 7 and event calls (LR4-O4) | S19-F05, S19-F06; R01 (905–1021), R02 (676–694). The override code: no further finding (the WU-PR-04 chain reviewed `vendor_audit.py`; LR4-O4) |
| 14 | `engine/bodygraph/v2_adapter.py` (`447243305d5e`) | #467; M | T1, T4, T5 | `adapt_v2_chart_payload` and validators | No finding. Pure mapping; no raw payload retained; typed refusals |
| 15 | `engine/cli/main.py` (`7761834a6100`) | #467; #643, #651; M | T1–T6 | `cli`, the pre-scan (WU-PR-04), `bg_resolve`, showcompat sources, file loaders, `_ensure_dev_admin_env`, dev sampler | S19-F02 (832–835), S19-F07; R01. `--dump-reader` and `--dump-admin-dir` write operator-chosen paths (operator surface; no finding) |
| 16 | `engine/compat/compute.py` (`77e311800838`) | #467; M | T1, T3, T5 | header, `evaluate_pair`, conjunction carriers (1–68, 300–470) | No finding. Its `source_policy="vendor"` default is reached by R01's paths; admission per evaluation costs about 0.3 s (worker measure; availability observation O-16) |
| 17 | `engine/compat/error_tokens.py` (`32f013d484e6`) | #467; M | T5 | whole file | No finding. Static messages; value-free boundary errors. The alias `forbidden` maps to two tokens (O-05) |
| 18 | `engine/config/__init__.py` (`aef7a0206c09`) | #467; no | all n/a (re-exports; lazy import by fixed names) | whole file | No finding |
| 19 | `engine/config/registry_loader.py` (`d7e9496d96d0`) | #508; #513; M | T1, T2, T5, T6, T7 | whole file (worker); 1030–1110 (this session) | S19-F08 (1076–1087). Not confirmed: unbounded manifest read before its size check for an operator-chosen candidate root (RL3), schema recursion (RL2). No TOCTOU between hash and parse; no-follow descriptors; thread-safe (no shared mutable state) |
| 20 | `engine/emit_public.py` (`4fdcd8d94517`) | #467; #643; no | T5 | whole file | No finding |
| 21 | `engine/http/compat_handler.py` (`42d0e7f9bfc6`) | #467; M | T1, T3, T5 | whole file | S19-F01 (132); R03. The production guard follows HDE-CLI-API-Vendor-Ref §5.5 exactly (exact namespace; trimmed, case-folded production posture); no body limit on the dev-only route (not confirmed: no canon bound, loopback runner) |
| 22 | `engine/runtime/public.py` (`df33eab7d8f4`) | #467, #508; M | T5 | whole file | No finding. Bands-only projection with closed key sets |
| 23 | `errors/token_map/token_map.json` (`7a5b2df0125f`) | #467, #501; M | T5 | whole file; its producer | No finding. 30 static messages |
| 24 | `errors/token_map/token_map.json.path_proof.txt` (`30822f401b73`) | #467, #501; no | T7 (binding) | whole file; the updater's proof writer | No finding. Binds path, size 2,982 and sha256 `a218f515…`, both equal; written by the updater |
| 25 | `presenter/reader_v1/emitter.py` (`4a9f1bacbd72`) | #508; M | T5 | whole file | No finding. Exactly `{id, band}` items; duplicates refused |
| 26 | `schemas/reader.v1.schema.json` (`a91843f13c20`) | #501, #508; #513; M | T1, T5 | whole file | No finding. Closed objects; constant codes |
| 27 | `schemas/reader.v1.schema.json.sha256` (`e8ef6ca434c2`) | #501, #508; #513; no | T7 (binding) | whole file | No finding. Matches the schema bytes; validated by `tests/reader_v1/test_schema.py` |
| 28 | `schemas/reader.v2.schema.json` (`7803e9a63009`) | #508; M | T1, T5 | whole file | No finding. Exactly ten ordered items |
| 29 | `schemas/reader.v2.schema.json.sha256` (`0a39e26325c2`) | #508; no | T7 (binding) | whole file | No finding. Matches |
| 30 | `scripts/cut_release_manifest.py` (`f87ef35c396d`) | #501; no | T2, T3, T6, T7 | whole file | S19-F08 (61–71, 146, 168). Closed rails required; resolved paths stay inside the repository; standalone write is non-atomic (the coordinating owner publishes atomically; O-17) |
| 31 | `scripts/make_reader_v1_goldens.py` (`9bb05d6dc503`) | #508; #513; no | T2, T7 | whole file | No finding. Writes at import time to fixed paths (O-18) |
| 32 | `scripts/make_release_pack.sh` (`6ea1acf4ffc1`) | #508; no | T2, T6, T7 | whole file | No finding. Quoted heredoc. Its `artifacts/release_id.txt` (`8ca9ba71…`) is not the canonical `release_id` and `scripts/hd_cli.py` reads it (naming drift; O-19) |
| 33 | `tools/bodygraph/check_magic10_gate_readiness.py` (`50fbc78f77e0`) | #492; M | T1–T5, T7 | whole file | No finding. Refuses outside closed rails before any provider; writes nothing (no `--report` option); one fixed parameterized `SELECT`; selection file bounded to 1 MiB, symlink and FIFO refused. Not confirmed: it connects to `DATABASE_URL` under closed rails (by design, HDE Mechanics Guide §25.6), not in a read-only session (O-20) |
| 34 | `tools/cli/generate_cli_conformance_artifacts.py` (`54db49d57b0a`) | #467; no | T3, T4, T7, T8 | whole file | No finding. Children inherit the environment (closed rails, `APP_ENV=test`); captured outputs are tokens and help text; not confirmed as exposure (GCC1; O-15). `--check` read-only |
| 35 | `tools/cli/generate_showcompat_artifacts.py` (`9ef2f0b818e9`) | #467; no | T3, T4, T7, T8 | whole file | R06 (104–109). `--check` read-only |
| 36 | `tools/config/artifacts.py` (`c8b702fefaee`) | #492, #501; no | T1, T2, T3, T5, T7 | whole file | No finding of its own (S19-F09's admitted root is at 471). Goldens read bounded to 1 MiB with no-follow; the report's exception text could carry a host path (ART1, not confirmed; O-21) |
| 37 | `tools/config/generate_config_artifacts.py` (`402c60206398`) | #492, #501; no | T1, T2, T3, T5, T7 | whole file | S19-F09 (322). Not confirmed: re-check before the report write (GCA2), linked-worktree reading of "repository" (GCA3), case-insensitive file systems (GCA4); no-argument run writes three governed artifacts, as HDE Users Guide warns |
| 38 | `tools/errors/generate_error_artifacts.py` (`ea1e1110578e`) | #501; no | T3, T4, T7, T8 | whole file | R04 (319–320). Children inherit the environment under forced closed rails with the database forced unavailable (GEA2, not confirmed; O-15) |
| 39 | `tools/evidence/build_release_attestation.py` (`edcdd517aa87`) | #467; #634; no | T2, T4, T5, T7, T8 | whole file | R05. Holds as canon states: refusals before writes (symlinked root, inside the source, non-directory, non-empty); child environment allowlist (`PATH`, `TMPDIR`, closed rails, `HDE_*`); no shell; no raw subprocess output retained. Not confirmed: skip-worktree defeats the clean check (BRA3; deliberate operator act; O-22); `--source` other than the running checkout lets a failure receipt land in the running checkout (BRA2; O-22) |
| 40 | `tools/evidence/generate_a7_transport_proofs.py` (`b5f71b9c704d`) | #467, #508; #643, #646; no | T2, T3, T7 | whole file | No finding. `APP_ENV` restored in `finally`; write gated by `HDE_WRITE_A7_PROOFS=1`. The env-gate proof is fixed text from one `prod` probe (A7-1; evidence strength, O-23); twelve sequential writes, one through the tracked symlink `docs/ENDPOINTS_CATALOG.json` (by design) |
| 41 | `tools/evidence/generate_conjunction_writer_evidence.py` (`ad8d812ed29d`) | #508; no | T2, T3, T4, T7 | whole file | No finding. Refuses unless exactly closed rails; `DATABASE_URL` popped and restored; the lookup seam is app config only. `os.environ.setdefault("APP_ENV", "dev")` is not restored for a library caller (CONJ-1; O-24) |
| 42 | `tools/evidence/generate_determinism_gate_proofs.py` (`31df358af63a`) | #467; no | T3, T4, T7, T8 | whole file | No finding. Children forced to closed rails; outputs are hashes. Environment inheritance (DET-1, not confirmed; O-15) |
| 43 | `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` (`c2d199883a9e`) | #467; no | T2, T7, T8 | whole file (read only; never run) | R04 (243). Also: wall-clock `produced_at`; its binding log checks key presence, not hashes (OBS-W5-3) |
| 44 | `tools/evidence/generate_hde_epic037_v2_to_compat.py` (`b76746a132fa`) | #467; no | T2, T3, T4, T7 | whole file | No finding. Closed rails enforced before work; synthetic fixtures only. Its `--check` fails on `main` from code drift, not security (OBS-W5-4) |
| 45 | `tools/evidence/generate_open_rails_abba_proof.py` (`d5097d28e679`) | #467, #501, #508; #513, #643, #646, #651; no | T2, T3, T4, T7, T8 | whole file | No finding. Live mode needs `--live`, exact rails, `APP_ENV=dev`, the canonical base, a confirmed authorization and an unused receipt; fixture-mode children have vendor keys stripped and run local-only showcompat; outputs carry presence booleans and redacted bases. Not confirmed: exact-name environment denylist (ORA-2; O-15); `--check-current`, which CI's rails job runs, does not byte-compare the committed proof while the release is admitted (ORA-1; the updater's `--check` binds its bytes; evidence-currency observation O-25) |
| 46 | `tools/evidence/regenerate_identity_closure.py` (`c1a06abee562`) | #467; #634; no | T2, T3, T8 | whole file | No finding. The source-tree refusal rests on `HDE_ISOLATED_RELEASE_BUILD=1` plus a hidden flag (RIC1; defeatable only by a deliberate operator act; O-22) |
| 47 | `tools/evidence/run_canonical_json_gate.py` (`652029563561`) | #467, #501; no | T2, T5, T7 | whole file | R07 (1205). Primaries published atomically per file; rows are `json.dumps` |
| 48 | `tools/evidence/run_sanity_pipeline.py` (`853566a0e4f7`) | #467; no | T2, T7, T8 | whole file | R05 (333, 347). Pins enforced; child output captured, never printed; log lines built from constants |
| 49 | `tools/evidence/run_sanity_pipeline_gate.py` (`62fbf8f87b1f`) | #467; no | T2, T5, T8 | whole file | R04 (106). Re-prints the pipeline's own output on failure (RSG2; not confirmed) |

### 5.7 Not-confirmed items and non-security observations

Recorded, not fixed here (ID-4); owner the IA unless stated, who routes them:

| ID | Observation | Owner |
| :- | :- | :- |
| O-01 | Gap 4: `adapter/http_reader.py::create_app`'s after-request hook is dead (`resp.request` does not exist); no observable effect (P-7). Addendum 2.7 and the decision record say it "never fires"; the precise statement is that it runs and never matches | IA (a later unit; doc wording) |
| O-02 | OBS-P3-3: `adapter/wsgi.py`'s 405 has no `Allow` header (P-8) | IA |
| O-03 | `_safe_load_chart`'s `rp.is_symlink()` after `resolve(strict=True)` is always false | IA |
| O-04 | `_require_admin_scope` compares bearer tokens with `==`; after S19-F03 the route answers the governed 404 in production before its handler | IA |
| O-05 | The alias `forbidden` maps to both `ERR_READER_FORBIDDEN` and `ERR_WRITER_FORBIDDEN` | IA |
| O-11 to O-13 | CI1 (GitHub path-filter limits, platform behavior); CI3 (tag-pinned actions, unpinned `setuptools` and `wheel`, no hashes); SC1 (`error_v1.details` unconstrained) | Product Owner (CI and dependency policy; schema owner) |
| O-14 | CI2: the workflow's path filter hard-codes the governed exceptions under exempt prefixes; they agree with the Index today, with no test tying them | WU-PR-06 or a later CI unit |
| O-15 | Environment inheritance into child processes (RR1, DET-1, ORA-2, GCC1, GEA2, RIC2): no path from an inherited value to I/O or output was found | IA (defence-in-depth candidate) |
| O-16 | Admission runs on every evaluation (about 0.3 s, CPU-bound) under 2 workers × 4 threads | Product Owner (performance) |
| O-17, O-18 | Non-atomic standalone writes of the cutter and of the goldens script (import-time writes) | IA |
| O-19 | `scripts/make_release_pack.sh` writes a non-canonical `artifacts/release_id.txt` that `scripts/hd_cli.py` reads as a release identity | WU-PR-08 / WU-DOC-01 through the IA |
| O-20 | The gate-readiness tool's `SELECT` runs in an ordinary (not read-only) transaction | IA |
| O-21 | `tools/config/artifacts.py` puts exception text into its report | IA |
| O-22 | Attestation and closure guards defeatable only by deliberate operator acts (BRA2, BRA3, RIC1) | IA |
| O-23 | The env-gate proof is fixed text from one `prod` probe; the exact gate itself is proven by `tests/http/test_reader_a7_transport.py` | IA / QA Plan |
| O-24 | `generate_conjunction_writer_evidence.py` leaves `APP_ENV=dev` set in a library caller's process | IA |
| O-25 | ORA-1: CI's `--check-current` does not compare the committed open-rails proof with a rebuild while the release is admitted | IA |

### 5.8 Out-of-scope observations (instruction ID-8)

| ID | Observation | Owner |
| :- | :- | :- |
| X-01 | LR4-O1: `vendor_audit.append_event` creates missing intermediate directories with the default mode; the sink directory and file stay owner-only | IA (routes it at the WU-PR-05 PR-40 review) |
| X-02 | OBS-P3-17: `run_flask.py` and `run_flask_dev.sh` start the production factory with the debugger and reloader on (HDE Architecture §3.8.1 discrepancy). After D-1 no harness handler is reachable there under a production-like `APP_ENV` | Product Owner |
| X-03 | The same lenient rails reading as S19-F05 outside the 49: `engine/providers/vendor_http.py` (`_is_truthy` on `ALLOW_NETWORK`) and `scripts/bodygraph/run_refresh_worker.py` (`_truthy` on both rails) | IA (later change candidate) |
| X-04 | `engine/bodygraph/vendor_client.py` puts `str(exc)` of a network error into `PROVIDER_NETWORK_ERROR` details, which the dev conjunction routes echo; after S19-F03 their handlers are not reachable in production | IA |

### 5.9 Route-policy statement (Plan Templates "`bg:resolve --source vendor` route-policy posture")

The route policy is unchanged by this unit (S19-R02 is routed, not fixed):
- configured `v2` bases are v2 chart-backed (`charts`, the deterministic `ChartResult` adapter);
- every other base takes the explicit legacy BodyGraph fallback (`bodygraphs`), including the unversioned, nonterminal and `v3` bases of S19-R02.

S19-F05 changes only which rail values count as open; the route selected for open rails is the same. This unit claims no BodyGraph-resolution conformance beyond existing evidence, no broad HumanDesignAPI v2 platform conformance, no live route availability and no public Reader change.

## 6. Scope

In scope (instruction §6; Plan v1.1 §7 WU-PR-05 "Deliverables"):
- **Fixes** S19-F01 to S19-F09 at the paths §8.1 names, each with its regression tests.
- **Release:** the same-version refresh at `1.3.0` and every family it regenerates, by owners only (five members change).
- **Records:** the S19 record `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` and the PR result records under `docs/ephemeral/`.

Out of scope (instruction §7):
- no Reader or Aux contract, payload, route, flag or transport change, and no new public route. Refusing a non-public route in production is not a public change; the production Reader, Aux, `/internal/version`, `/ops/rails/refusal` and the `POST /reader` stub keep their bytes;
- no scanner, analyzer or dependency; no change to `requirements*.txt`, `pyproject.toml`, `pytest.ini` or `.github/workflows/ci.yml`;
- no version bump or admission-constant change;
- no canon edit, PF10 addendum, `schemas/` file, evidence family or acceptance token;
- no production gate on showcompat or conjunction (S19-R01); no route-policy change (S19-R02); no deletion of a canon-retired route's code;
- no live vendor, production or database call, no real credential, no production configuration change, no deployment;
- no `AGENTS.md`, `README.md`, `CHANGELOG.md`, `.env.example`, `docs/server/reader_v1.md` or `docs/CLI_commands.md` edit (no fix changes a behavior they state; §19);
- no skipped, disabled, `xfail` or quarantined test; no write-mode run of a frozen-family generator, the EPIC030 generator or the EPIC036/EPIC037 generators;
- the routed findings (S19-R01 to S19-R07) and the observations of §5.7 and §5.8.

## 7. Design

### 7.1 S19-F01 — nesting past the recursion limit

- `adapter/http_reader.py::_parse_reader_post_body`: the parse's `except` also catches `RecursionError` → `ERR_READER_INVALID_INPUT` 422, the standard four-key envelope, `no-store` (HDE-CLI-API-Vendor-Ref §5.2.3).
- `adapter/http_reader.py::_read_writer_json`: `except (json.JSONDecodeError, RecursionError)` → `ERR_WRITER_INVALID_JSON` 400.
- `engine/http/compat_handler.py::post_json`: `request.get_json(silent=True)` inside `try … except RecursionError` → the empty payload, which the existing checks refuse as `ERR_COMPAT_INVALID_JSON` 400.
- One comment each, citing the rule. No other handler changes.

### 7.2 S19-F02 — exact dev/admin gates

- HTTP: `_dev_admin_gate` returns `None` only for `os.environ.get("APP_ENV") in {"dev", "test", "local"}`; everything else, unset included, is the existing `ERR_WRITER_FORBIDDEN` 403.
- CLI: `_ensure_dev_admin_env` refuses `DEV_ADMIN_ONLY` unless `os.environ.get("APP_ENV") in ("dev", "test", "local")`.
- The refusal matrix of instruction ID-6 is the regression test for each gated route (the sampler, the three conjunction routes, `hdctl dev:sampler`): unset, empty, ` dev`, `dev `, `Dev`, `DEV`, `TEST `/`TEST`, `Local`, `prod`, `production`, `live`, `staging` refused; `dev`, `test`, `local` served.

### 7.3 S19-F03 — production mount of the dev/internal blueprint (D-1; instruction ID-6 and AD-4)

**One design, applied uniformly to every factory that mounts the blueprint.** The three factories are not edited: each already registers the dev/internal blueprint, and the blueprint carries the policy.
- `get_reader_bp` records `_mount_for_production` with `bp.record`. This is the registration callback the production Reader blueprint already uses for its unrouted-method 405 (`get_reader_api_bp`). Flask calls it once when an application registers the blueprint, so `adapter/factory.py`, `adapter/http_reader.py::create_app` and `adapter/wsgi.py::create_app` all get the same policy from the same code.
- The callback decides the posture with `_production_posture()`. `adapter.env_guard._compute_env_mode` takes a non-empty `APP_ENV`, trimmed and case-folded, else `ENGINE_ENV`, and resolves `prod`, `production` or `live` to production. This is HDE-CLI-API-Vendor-Ref §5.5's resolution, the one the compat guard already uses; its normalization only widens refusal, which addendum 2.7 AD-2 notes canon allows. In any other posture (dev, test, local, staging, empty or unset) the callback returns, and registration is exactly today's.
- In a production-like posture it installs one application-level `before_request` hook, `_refuse_in_production`. The hook answers before any handler of these routes runs:
  - **Canon-retired routes** → the governed `ERR_NOT_FOUND` 404 with `no-store`, the bytes and headers an unknown path gets in each factory (S02). This covers the endpoints of `/ops/db/unavailable`, `/ops/probe/env` and `/ops/writer/diagnostic` (`POST`, `HEAD`, `OPTIONS`), and any method no rule names on those paths.
  - **Automatic `OPTIONS`** → unchanged, because Flask's automatic answer runs no handler (PD-15).
  - **Dev-harness routes** → the canonical refusals:
    - `GET`/`HEAD /reader`: version validation, then `ERR_READER_FORBIDDEN` 403, byte for byte the handler's own refusal under `APP_ENV=prod`;
    - `POST /internal/dev/sampler` and the three `GET`/`HEAD /dev/*/conjunction` routes: `ERR_WRITER_FORBIDDEN` 403, byte for byte the dev/admin gate's refusal, with the same keys-only route label.

    The hook reads no request-time environment value, so no harness handler runs whatever `APP_ENV` says at request time.
  - **Every other request** → `None`, and routing proceeds unchanged.
- No rule is added or removed. The URL map, the endpoint names and every view function stay as they are; only the answers stated above change.

**Shape constrained by the governed analyzers** (P-13):
- The hook is registered by call with one name argument, and each of its returns is `None` or a direct `_error(...)` call. The EPIC034 adapter-boundary analyzer proves exactly that shape for a call-registered `before_request` hook, and the architecture-snapshot analyzer sees no new `add_url_rule` or `register_blueprint` call.
- The writer refusal therefore uses `_error("ERR_WRITER_FORBIDDEN", 403)`, whose bytes and headers equal `_writer_error`'s for this token; the tests compare full header sets.
- The retired answer returns `_error("ERR_NOT_FOUND", 404)` rather than raising `NotFound` (PD-16).
- A later change to the hook keeps this shape, or it is RK-8.

**Why refusals for the dev harness and not-found for the retired routes** (PD-1):
- Canon requires two things at once:
  - the harness is never mounted in production (HDE Architecture §3.3; HDE-CLI-API-Vendor-Ref §5.4, §5.12);
  - a request to these paths whose environment gate fails is refused with the writer-style `ERR_WRITER_FORBIDDEN` (§5.11.2, §5.12) or, for `/reader`, with `ERR_READER_FORBIDDEN` (S10).
- The hook meets both: no harness handler is reachable, and the canonical refusal bytes are unchanged, so S10's Live QA step and the env-gate proof stay valid.
- The canon-retired routes have no canonical refusal, so they answer exactly as a path no rule names. Their code stays; removal belongs to the canon owner.

**Limits, stated** (P-14). The rules stay in the URL map, so the router's own answers that come before the hook remain. No handler runs in either case:
- a doubled-slash spelling gets Werkzeug's 308 redirect to the canonical path, which then answers the refusal or the 404;
- the keys-only log line of a refused request names the matched blueprint.

**Routes canon adopts keep their posture** (instruction ID-6): `/api/reader` (all methods), `/aux/narrative` and `/api/aux/narrative`, `/internal/version`, `/ops/rails/refusal`, the compat namespace (its own production-excluding 404), and the unprefixed `POST /reader` 405 stub with `Allow: GET, HEAD` (PD-2).

**Dev use kept:** the canonical runner `python -m adapter.http_reader`, `scripts/dev_start_reader.sh`, `VERIFY.sh` and the tests run with dev, test or local values and get today's full mount. HDE Architecture §3.8.1's "exposes the same Reader and internal/dev sampler routes as the production adapter" is read as instruction ID-6 reads it: a duty of the dev server; it becomes a doc-delta candidate (§19).

**Proofs stay truthful:** `tools/evidence/generate_a7_transport_proofs.py` builds `adapter.http_reader.create_app()` under the closed-rails profile (`APP_ENV=dev`), so it gets the full mount and then observes the handler's request-time refusal under `APP_ENV=prod`, as today; `artifacts/proofs/endpoints_env_gate_proof.log` (`APP_ENV=prod`, `/reader_success_unreachable=true`) stays byte-identical and truthful. It observes the request-time gate of the dev-runner factory, not the production mount; the production mount is proven by the new tests.

**Catalog accounting:** the Endpoint Catalog and the route-enumeration test enumerate factories built under the test environment (non-production), whose served set is unchanged; no catalog record and no validator change (step 3b stays harmless).

**Production served set** (contract F-3; P-10): under a production-like posture each factory keeps its rules (`adapter.factory` and `adapter.http_reader.create_app` 21 rules and 49 `(method, path)` pairs, `adapter.wsgi` 23 and 55; `/static` excluded); the nine canon-retired pairs answer the governed 404, the dev-harness pairs that reach a handler answer their refusals (automatic `OPTIONS` stays), and nothing else changes.

### 7.4 S19-F04 — bounded writer read

`_read_writer_json` reads `request.stream.read(_MAX_WRITER_BYTES + 1)` instead of `request.get_data(cache=False)`, as `_parse_reader_post_body` already does, with the same comment. A body over 32 KiB, with or without `Content-Length`, is `ERR_WRITER_REQUEST_TOO_LARGE` 413 after at most 32,769 bytes are read.

### 7.5 S19-F05 — exact rails in the resolver and the ingest

- `engine/bodygraph/resolver.py`: `_truthy` is replaced by `_rail_value` (strip; `True`/`False` as `"1"`/`"0"`), `_safe_mode_closed(value)` (closed unless the value is exactly `"0"`) and `_network_allowed(value)` (open only for exactly `"1"`), used at the rails step of `resolve_bodygraph` and in `_acquire_dry_run`. This is the rule `vendor_client._rails_state_from_env` and `_default_request` already apply.
- `engine/bodygraph/ingest.py`: the same rule at its rails check (`_truthy` replaced by `_rail_value`).
- Effect: canonical values behave as today; an unset, empty or other `SAFE_MODE` refuses `PROVIDER_REFUSED` at the rails step, and an `ALLOW_NETWORK` other than `1` refuses `PROVIDER_NETWORK_BLOCKED` there, before environment classification, the override matrix, any audit event or any client construction (HDE-CLI-API-Vendor-Ref §7.1.11d).

### 7.6 S19-F06 — no ingest log in the checkout by default

- `engine/bodygraph/ingest.py`: `retry_log` and `success_log` default to `None`; `RETRY_LOG` and `SUCCESS_LOG` stay defined (tests import them).
- `engine/bodygraph/resolver.py`: the production-override client is built without `log_path`; the unused `RETRY_LOG` import is removed (P-11).
- A caller that wants a log names its path, as `tools/evidence/generate_open_rails_abba_proof.py` and the tests already do. A vendor run inside a checkout no longer changes `artifacts/ingest/**`.

### 7.7 S19-F07 — CLI stderr discipline

- The catch-all writes exactly `CLI_UNEXPECTED\n` (the token; no exception text).
- The four JSON parse sites (`_load_viewer_prefs`, `_parse_input`, `_load_candidates_from_path`, `_load_party_file`) also catch `RecursionError`, giving their existing tokens (`INVALID_VIEWER_PREFS`, `INVALID_JSON`, `INVALID_CANDIDATES_JSON`, `INVALID_JSON_<SIDE>`), exit 64 as today.

### 7.8 S19-F08 — manifest paths without control characters

- `engine/config/registry_loader.py::_parse_manifest`: the canonical-path rule also requires `path.isprintable()` (for an ASCII path this refuses NUL, CR, LF, TAB and DEL) → `INVALID_MANIFEST_PATH`. Messages that name a path come after this rule, so they name only printable paths.
- `scripts/cut_release_manifest.py::_path_unsafe`: the same condition → `release_manifest_entry_path_unsafe`, before any message names the row.

### 7.9 S19-F09 — report path against the admitted root

`_golden_report_destination` refuses a report inside any of: the candidate as given, resolved; the candidate's lexical absolute path (the root `compare_goldens` admits), resolved; the repository. One added tuple element and a comment.

## 8. Change set

### 8.1 Files edited by hand (the companion diff)

| Path | Change | Finding |
| :- | :- | :- |
| `adapter/http_reader.py` (member) | Reader and writer parse `except`; bounded writer read; exact `_dev_admin_gate`; `_PRODUCTION_DEV_WRITER_ROUTES`, `_PRODUCTION_RETIRED`, `_production_posture`, `_mount_for_production` with its hook `_refuse_in_production`; `get_reader_bp` records `_mount_for_production`; import of `_compute_env_mode` | F01, F02, F03, F04 |
| `engine/http/compat_handler.py` (member) | `RecursionError` around `get_json` | F01 |
| `engine/cli/main.py` (member) | exact `_ensure_dev_admin_env`; four parse sites; catch-all token | F02, F07 |
| `engine/bodygraph/resolver.py` (member) | `_rail_value`, `_safe_mode_closed`, `_network_allowed` replace `_truthy`; override client without `log_path`; `RETRY_LOG` import removed | F05, F06 |
| `engine/bodygraph/ingest.py` | exact rails; `None` log defaults | F05, F06 |
| `engine/config/registry_loader.py` (member) | `path.isprintable()` in the manifest path rule | F08 |
| `scripts/cut_release_manifest.py` | `name.isprintable()` in `_path_unsafe` | F08 |
| `tools/config/generate_config_artifacts.py` | the admitted root in the report refusal | F09 |
| `tests/http/test_reader_post_v1.py`, `tests/http/test_reader_post_v2.py` (6 + 6 cases) | the production Reader v1 and v2 in all three factories, two nesting shapes; import of `factory` and `wsgi` in the v1 module | F01 |
| `tests/transport/test_writers_errors_headers.py` (2) | the writer JSON helper's nesting refusal; its bounded read with a counting stream, no `Content-Length`, `wsgi.input_terminated` | F01, F04 |
| `tests/http/test_compat_endpoint_contract.py` (1) | compat `POST` nesting refusal, through `adapter.factory`. This module is an indirect owner of `adapter/http_reader.py` and still does not import `adapter.http_reader` (P-15) | F01 |
| `tests/http/test_dev_conjunction_http.py` (60) | the HTTP gate matrix over the sampler and the three conjunction routes: 12 refused values, 3 served | F02 |
| `tests/http/test_endpoint_catalog.py` (43) | for five postures and three factories: one hook installed; refusal status, bytes and full header set equal to the handler's own refusal; request-time `APP_ENV=dev` still refused. Also: automatic `OPTIONS` unchanged; retired routes answer exactly as an unknown path for six methods; adopted routes unchanged; non-production postures install no hook and keep every view; the posture rule (`_production_posture` imported) | F03 |
| `tests/bodygraph/test_resolver_vendor.py` (96) | resolver rail matrices (with and without the flag, `dev` and `prod`, I/O guards, no audit sink created); canonical values open; the compat acquisition; no ingest log under the working directory on the non-production and the production-override legacy paths | F05, F06 |
| `tests/bodygraph/test_ingest.py` (19) | ingest rail matrix; `None` log defaults | F05, F06 |
| `tests/cli/test_cli_usage_and_errors.py` (15) | `hdctl dev:sampler` gate matrix; the catch-all token; undecodable input | F02, F07 |
| `tests/cli/test_cli_file_inputs.py` (5) | nesting at stdin, pair file, party files, candidates, viewer preferences | F07 |
| `tests/config/test_manifest_schema.py` (7) | loader control-character rule; printable paths still named | F08 |
| `tests/scripts/test_cut_release_manifest.py` (6) | cutter control-character rule without echo | F08 |
| `tests/config/test_config_artifacts.py` (1) | report refusal against the lexically admitted root | F09 |

Every test addition is a delimited block headed `HDE-CRD-0002 WU-PR-05 (S19-Fnn)`, with module-private helpers prefixed `_s19`/`_S19`. Five import lines are widened, and no existing test or assertion changes. That is 651 added lines and 5 changed import lines (PD-13).

Lanes (classifier at `1e97ba9`): every path is classified and no registration is needed (F-5: none). Each host module is reached the way the rehearsal classifier showed (§4.3): ten as changed-test targets of their subjects, three in the fixed db or compat lane. All thirteen also run in full validation.

### 8.2 Written only by owners

`catalog/manifest.json` (cutter); `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py` (step 7); every family of §9; the Index, Mirror, sentinels and path proofs (updater only).

### 8.3 Expected unchanged (a change is a finding, §16 RK-6)

- `requirements*.txt`, `pyproject.toml`, `pytest.ini`, `.github/workflows/ci.yml`, `ci/checks/classify_ci_changes.py`, `tests/evidence/test_rails_ci_workflow_integration.py`;
- `adapter/factory.py`, `adapter/wsgi.py` (the factories register the blueprint as today; §7.3);
- `tools/evidence/generate_architecture_snapshot.py`, `tools/evidence/hdapi_v2_boundary_analyzer.py` and their tests (P-13; a failure is fixed in the hook's shape, never in an analyzer);
- `engine/bodygraph/vendor_client.py`, `engine/bodygraph/vendor_audit.py`, `engine/compat/**`, `engine/narratives/**`, `engine/presenter/**`, `presenter/**`;
- `run_flask.py`, `run_flask_dev.sh`, `FLASK_AUTO_RUN_GUIDE.md`, `scripts/dev_start_reader.sh`, `VERIFY.sh`;
- `engine/config/registry_loader.py`'s admission constants; `tools/evidence/update_evidence_index.py`; every existing test file other than the 13 hosts of §8.1, and in those every existing test and assertion;
- `ci/checks/classify_ci_changes.py` and every owner registry and pin in `tests/evidence/test_rails_ci_workflow_integration.py` and `tests/evidence/test_http_reader_ci_ownership.py` (P-15);
- every frozen family: `artifacts/vendor/**`, `artifacts/cli/**`, `artifacts/architecture/**`, `audit/ops/**`, `audit/qa/hde-epic0*/**`, `artifacts/ingest/**` and the EPIC022 release evidence; the Endpoint Catalog family;
- `AGENTS.md`, `README.md`, `CHANGELOG.md`, `.env.example`, `docs/server/reader_v1.md`, `docs/CLI_commands.md`, `docs/pfcanon/**`.

## 9. Release refresh and convergence (Plan v1.1 §10; addenda 2.6 and 2.7 AD-5; instruction §5.8)

Five members change: `adapter/http_reader.py`, `engine/http/compat_handler.py`, `engine/cli/main.py`, `engine/bodygraph/resolver.py`, `engine/config/registry_loader.py`. The refresh base is `2f18a5eb…` (addendum 2.9).

All steps run under closed rails, vendor and database keys unset, in the implementation branch's working tree after the member bytes are final and committed. Steps 3 to 10 run twice; the second pass must reproduce the first byte for byte. The `ci/checks/*.sh` scripts are invoked by path (WU-PR-04 F-2).

| Step | Commands (owner) | Notes |
| :- | :- | :- |
| 1 | member bytes final (one final LF) | no updater run from here to the cut (LR-O3 (a)) |
| 2 | `python scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; `python scripts/release_id_recompute.py --check-manifest-only`; the cutter again with `--check` | five manifest rows change; record the new `release_id` |
| 3 | admission one-liner (`load_active_mechanics_bundle()` → `release_id`, `len(manifest.files)`, `manifest.version`); `python tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>/golden_report.json` | expect the new `release_id`, 45, `1.3.0`; exit 0 |
| 3b | `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`; then `--check` | step-3b order (addenda 2.6, 2.7); harmless here: neither the catalog validator nor the A7 generator changes |
| 4 | `python tools/evidence/run_canonical_json_gate.py`; `--check-only` | |
| 5 | `python tools/evidence/update_evidence_index.py`; `--check` | first updater run after the cut |
| 6 | `python tools/config/generate_config_artifacts.py --publish-family`; updater `--check` | |
| 7 | A7 write and `--check`; `python tools/evidence/generate_determinism_gate_proofs.py`; `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_open_rails_abba_proof.py` (fixture mode, keys absent); set `FROZEN_OPEN_ABBA_SHA256` to `sha256sum audit/gates/determinism/open_rails_abba.json` by one anchored replacement; `python tools/evidence/generate_conjunction_writer_evidence.py`; `python tools/evidence/generate_engine_core_evidence.py` | the open-rails digest supersedes `9949ddf5…` |
| 8 | updater; `--check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/check_lf_endings.py`; `ci/checks/check_final_lf.sh`; `refresh_step_logs_manifest.py --check` | step-7 captures take the new label here (LR-O3 (b)) |
| 9 | `python tools/evidence/run_sanity_pipeline.py --log-path <outside>/sanity.log` (must end `summary:PASS`); the canonical run; `python tools/evidence/run_sanity_pipeline_gate.py`; updater `--check` | |
| 10 | `python tools/cli/generate_showcompat_artifacts.py --check`; `python tools/cli/generate_cli_conformance_artifacts.py --check`; `python tools/evidence/generate_rails_gate_evidence.py --check`; `python tools/evidence/generate_env_matrix_snapshot.py --check` | frozen families unchanged |
| 11 | `git grep -l -E '2f18a5eb|9949ddf5'` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256`, `manifest_post.sha256`; and in `docs/` outside `docs/ephemeral/` and `docs/pfcanon/` | expected: no hit; every hit is a defect to fix before publication. Also: the Mirror's 27 labelled rows carry the new `release_id`, none the old; the purity-report rows have no `notes` (LR-O3 (c); addendum 2.6) |
| 12 | §12's tests and lanes; the attestation build and verify | |

**Restart rules.** A member byte change after step 2 restarts at step 2. An evidence-primary change restarts at step 3b (addenda 2.6 and 2.7 AD-5).

**Expected changed set** (56 paths; observed in both rehearsal passes; PR-30 records its actual set):
- `catalog/manifest.json`;
- `tools/evidence/generate_open_rails_abba_proof.py` (`FROZEN_OPEN_ABBA_SHA256` only);
- 27 evidence primaries and their 27 path proofs:
  - **A7 success proofs:** `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}`;
  - **config:** `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log`;
  - **engine core:** `artifacts/core/{abba/ab_ba_parity,json_compare/core_result_json_compare,purity/purity_report,two_run/identity}.json` (the purity report binds the loader's digest; P-12);
  - **F07 writer:** `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}`;
  - **canonical JSON gate:** `audit/gates/canonical_json/{json_canon_compare,json_canonical_check}.log`, `audit/gates/json_gate/canonical/{json_gate_check_log,json_gate_compare_log}.ndjson`;
  - **determinism and parity:** `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}`, `audit/gates/parity/reader_cli/{ab,ba,summary}.json`;
  - **Index and Mirror:** `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`.

**Rewritten byte-identically** (not in the diff): the catalog family, `artifacts/proofs/endpoints_env_gate_proof.log`, `success_writers_errors.txt`, `artifacts/reader/endpoints_snapshot.json`, the canonical sanity log.

## 10. Implementation sequence (PR-30)

1. **Recover.** Inspect local roots, worktrees, branches, open PRs and `docs/ephemeral/HDE-CRD-0002-WU-PR-05-*` before creating anything (instruction §13).
2. **Branch** from current `main` (the session's designated branch).
3. **Head confirmation (ID-2).** Compare the 49 blob IDs at the branch base with §5.6. Review the changed hunks of any changed path and record them. A new confirmed finding there whose fix this plan does not cover is routed, or, if it must be fixed in this CRD, goes to RS-10 with `PR_RETURN_PHASE` (instruction §14). If `main` moved outside `docs/` since `1e97ba9`, re-run `git apply --check` of the companion diff and record any difference; a changed member or manifest on `main` is a new refresh base.
4. **Set up** Python 3.12 with CI's install and `-e .` of the worktree under test (OBS-W5-5), `ruby`, `bash`, `curl`; unset the vendor, database and GitHub keys; record versions.
5. **Apply §8.1** (the companion diff as a starting point) and re-read every hunk against §7.
6. **Pre-cut tests.** Run the 13 host modules, the affected directories of §4.3 and the two analyzer test files (P-13); the only expected failures before the cut are refusals of the not-yet-cut manifest (17 in the rehearsal, §4.3), and both analyzers must pass. Run NC-01 to NC-18 in a scratch copy; each must fail as §4.3 records.
7. **Source commit.** Freeze the member bytes and commit the source.
8. **Refresh.** Run §9 steps 2 to 11 and commit the convergence. Record each step's exit code, both passes, the byte-stability digest, the changed set and the sweep.
9. **Validate.** Run §12 in detached worktrees of the candidate commit.
10. **Record and publish.**
    - Write and read back the S19 record (§14) and the PR result record v1.0.
    - Commit coherently: source, convergence, records.
    - Push and open the PR with the template headings (§13).
    - Record `PR_CANDIDATE_PUBLISHED` and hand off to PR-35.

## 11. Requirement → change → test map

| Requirement / acceptance item | Change | Proof |
| :- | :- | :- |
| S19 review recorded / (1) | §5; the S19 record (§14) | 49 per-file lines with blob IDs; head confirmation (§10 step 3); PR-40 |
| S19 findings dispositioned / (2) | §7 (nine fixes); §5.4 routing lines | the 267 `test_s19_*` cases in the 13 host modules; NC-01 to NC-18; routing lines with owner, reason and evidence |
| Exclusion 6 / (3) | none (manual review) | the diff touches no `requirements*.txt`, `pyproject.toml` or workflow; no scanner was run (§5.1) |
| Lanes and release identity / (4) | §9 | admission at the head (`1.3.0`, 45, the refreshed `release_id`); second-pass byte identity; recompute exit 0; CI on the exact head with every selected lane green and `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| AD-4 (gaps 1 to 4) | §7.3, §7.2; §5.5 | `test_s19_production_mount_*`, `test_s19_every_other_posture_mounts_the_blueprint_unchanged` (`tests/http/test_endpoint_catalog.py`), `test_s19_dev_admin_gate_*` (`tests/http/test_dev_conjunction_http.py`); NC-04, NC-06, NC-17, NC-18; the served-set probe (P-10); gap 4 recorded (O-01) |
| CI coverage and ownership guards stay green with no registry change (P-15) | §8.1 test placement (PD-13) | `tests/evidence/test_rails_ci_workflow_integration.py` and `tests/evidence/test_http_reader_ci_ownership.py` in the full sweep; the classifier dry run (§12 item 1) |
| Governed analyzers stay green (P-13) | §7.3's hook shape | `tests/evidence/test_architecture_snapshot.py` and `tests/evidence/test_hdapi_v2_contract_inventory.py`, before the cut and in the full sweep |
| Live QA class per fix | §5.4 | the QA Plan's steps by class (F-2), not this unit |
| PF27 route-policy statement | §5.9 | unchanged posture; existing route-policy tests |

## 12. Validation plan (PR-30, local)

Every run that can write tracked files runs in a detached worktree and ends with `git diff --exit-code` and an empty `git status --short --untracked-files=all`:
1. **Classifier** dry run on the PR's changed paths: lanes and changed-test targets recorded (rehearsal: 77 paths, six lanes, 39 targets; the 13 host modules reached as §4.3 states).
2. **Changed-tests step** as CI runs it.
3. **Lanes** as `.github/workflows/ci.yml` writes them (product, compat, db, rails, evidence, release; qa if the classifier selects it), the release lane with the attestation build and verify into an external empty directory with `--require-clean`. The attestation is mandatory before publication: it is the only local run with the isolated child environment (OBS-P4-5).
4. **Full sweep** of `tests/` with `ruby`, `bash` and `curl` on `PATH` and `XDG_STATE_HOME` pointed at an empty scratch directory; counts recorded. The refresh rewrites the Index and Mirror, so this covers every updater consumer (LR-O2).
5. **The read-only checks of instruction §5.6** after the fixes: the ten evidence and release checks, the seven `--check`s, the five frozen-family checks, the three config and cutter checks, the sanity pipeline. Record the three pre-existing failures (`generate_hde_epic037_v2_to_compat.py --check`, `generate_hde_epic037_bg_resolve.py --check`, `generate_hde_epic036_bg_resolve_route_policy.py --check`) as pre-existing, never as passing.
6. **Convergence checks** of §9 steps 4 to 10 and the step-11 sweep.
7. **Negative controls** NC-01 to NC-18; each must fail.
8. **Probes** (instruction §10, gaps 1 to 3): the production-factory probe of instruction §5.3 repeated on the candidate, showing the dev-harness refusals unchanged in bytes, the retired routes 404 and the adopted routes unchanged; the served-set probe of P-10 (every pair under `APP_ENV=prod`; only the nine retired pairs and `/internal/version`'s body change); the same requests on the canonical runner under `APP_ENV=dev` unchanged; the gate value matrix.
9. **Hermeticity.** The 13 host modules pass with `APP_ENV` unset, and with `tests/adapter/test_jsonschema.py` first in the same process (OBS-P4-7).

Never run the EPIC030 generator in the repository tree (OBS-W5-3).

## 13. PR split, merge dependencies and pull request description

**No split: one PR for the whole unit** (Plan v1.1 §7). The member edits, the cut and the convergence must land together, so that admission and the updater hold at every commit of `main`; the S19 record lands with its fixes.

**Merge dependency:** none open. WU-PR-01 to WU-PR-04 have landed. WU-PR-06 and WU-PR-07 merge after this unit; WU-PR-08 depends on this unit's `release_id` (F-1).

**PR description:** the `.github/pull_request_template.md` headings with the `AGENTS.md` content rules:
- **Why:** S19 and instruction §4; addendum 2.7 AD-4.
- **What changed:** grouped by path.
- **Checks run:** each with its counts.
- **Not in this PR:** the routed findings and observations, with owners; the stale documents (§19).
- **What merging does:** what becomes current on `main` (the fixes, the refreshed `release_id`, the S19 record), and that it establishes no QA, acceptance or closure; the routed findings are not decided.

## 14. Acceptance and evidence obligations

**The S19 record** `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md`, written by PR-30 from §5 (instruction ID-2), one complete Markdown file:
- scope and reviewed head with the 49 blob IDs (§5.1, §5.6), and the head confirmation of §10 step 3;
- method and limits (§5.1; manual review with repository tooling; no scanner);
- the checklist (§5.3, with instruction §4.1's canon map);
- the severity scale (§5.2);
- the 49 per-file lines (§5.6);
- the findings table with the Plan's columns (id, file and line, description, severity, confirmed or not, disposition): a fixed-here disposition names the fix commit and its regression tests and negative control; a routed one names the owner, the reason and the evidence (§5.4);
- the named-input table (§5.5), the observations (§5.7) and the out-of-scope observations (§5.8);
- the PF27 route-policy statement (§5.9);
- the nonclaims (below).

Corrections before the merge amend the record in the PR; PR-35 lists each. Nothing changes it after the merge.

**The PR result record v1.0** (`docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.0.md`) names:
- the S19 record;
- each check actually run, with counts;
- the reviewed head and the head confirmation;
- each fix, its tests and its negative control;
- each routed finding and its owner (contract F-4);
- the `release_id` after the unit and every regenerated family, both passes, the byte-stability digest and the step-11 sweep (F-1);
- the production route exposure after the unit (F-3: §7.3's served set; how the dev, test and local runners still serve the dev routes; what the env-gate proof observes);
- the stale-document list (§19) and the classifier result (F-5: no registration);
- in-flight decisions (PR-30's own, or `NONE`);
- the nonclaims:
  - the review is implementation-side assurance, not QA and not acceptance (Plan);
  - no live run of any fixed surface;
  - no QA verdict, acceptance, Ops, deployment, PF09 movement or closure;
  - no conformance claim beyond the fixes made;
  - no canon edit; the routed items are not decided by this unit.

**Contract F-2 for QA-10 and the QA Plan:** the record path; each fix with its Live QA class and surface (§5.4); each routed finding with its owner.

## 15. Security and migration constraints

**Migration and rollback.** Migration: none (no data or schema change). Rollback: Nathan's revert of the squash commit, followed by a same-version manifest refresh (Plan v1.1 §7, §14).

**Security.**
- **Fixes only narrow exposure.** No rail opens, no write path opens, no surface gains vendor or database access. S19-F03 removes reachable code from the production application; S19-F05 refuses earlier; S19-F06 writes less.
- **Production bytes.** The production Reader and Aux, `/internal/version`, `/ops/rails/refusal`, the compat 404 and the `POST /reader` stub keep their bytes; the dev-harness paths keep their refusal bytes; only the three canon-retired routes change (to the governed 404) and the Reader's deep-nesting case (to the governed 422).
- **No secret** in a test, record, log or commit: fake keys are fixed non-secret strings; probes ran under closed rails; captured bodies show rails values as observed.
- **Keys-only statement** of every exposure; no exploit payload beyond what reproduces a defect under closed rails.
- **The refresh** opens no rail; the open-rails fixture proof runs with keys absent.

## 16. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| RK-1 | A test or tool builds a factory under a production-like `APP_ENV` and expects a harness handler | none found in the sweep; a new one is fixed only by its environment setup (instruction §6), otherwise RK-6 |
| RK-2 | A member byte change after the cut | restart at step 2 |
| RK-3 | A later Flask changes `Blueprint.record`, application `before_request` order or automatic `OPTIONS` | Flask is pinned `>=2.3,<3.0` (`requirements.txt`); the mount tests fail on any change of behavior |
| RK-4 | A frozen family changes | §12 items 5 and 6; any change is RK-6 |
| RK-5 | OBS-17: intermittent qa-lane failure of `tests/qa/test_generate_epic_close_pack.py` | recorded as OBS-17, never "fixed" here; the rehearsal classifier did not select the qa lane |
| RK-6 | A boundary trigger of instruction §14: a change outside §8, a governed output that cannot stay byte-identical, a reading that conflicts with canon, or a new finding at the head confirmation that must be fixed in this CRD | stop the affected work; `RESCOPE_REQUEST` through RS-20 (PR-30 records `PR_RETURN_PHASE`) |
| RK-7 | `ruby` absent on a runner | the contract-inventory test fails rather than skips; PR-35 records the hosted version if a log shows it (O-6) |
| RK-8 | A correction changes the hook's shape and a governed analyzer fails closed (P-13) | keep the shape of §7.3 (one name argument to `before_request`; each return `None` or a direct `_error(...)` call; no new `add_url_rule` or `register_blueprint` call); never edit an analyzer; a shape that cannot satisfy them is RK-6 |

**Recovery.** An interruption resumes in the same dedicated phase session from its last saved artifact. An ordinary defect in this plan returns to this PR-20 context as a new plan version. An instruction defect returns to the IA through PR-10. Abort is only Nathan's manual PR-50.

## 17. Decisions taken in this plan (instruction §9.2; within approved scope)

| ID | Decision | Basis |
| :- | :- | :- |
| PD-1 | **D-1 design:** in a production-like posture one application-level hook, installed by the blueprint's registration callback, answers the dev-harness routes with their canonical refusals and the canon-retired routes as an unknown path, before any of their handlers runs; one policy in the blueprint, the same in all three factories, no factory edited | AD-4 ("one factory-level design applied uniformly"); HDE Architecture §3.3; HDE-CLI-API-Vendor-Ref §5.4, §5.11.2, §5.12; §7.3 |
| PD-2 | The unprefixed `POST /reader` 405 stub stays in every posture, bytes unchanged | HDE-CLI-API-Vendor-Ref §5.4 "Production mount" and HDE Users Guide §6.4 state it as the production refusal; instruction ID-6 "Routes canon adopts keep their posture" |
| PD-3 | The production posture is HDE-CLI-API-Vendor-Ref §5.5's resolution (`_compute_env_mode`), evaluated when an application registers the blueprint (at creation, in every factory) | the canon rule the compat guard uses; normalization widens refusal only (addendum 2.7 AD-2); gunicorn builds the app in the deployed environment |
| PD-4 | The severity scale of §5.2 | instruction ID-4 |
| PD-5 | Each disposition of §5.4 | instruction ID-5 and ID-7 |
| PD-6 | S19-F01 covers the three parse sites in the two HTTP members; S19-F07 the CLI's | one defect class; the members change anyway |
| PD-7 | S19-F05 uses the socket layer's exact rule at the resolver and ingest rails steps | HDE-CLI-API-Vendor-Ref §7.1.2; consistency with `vendor_client` |
| PD-8 | S19-F06 changes the ingest defaults to `None` rather than adding a new log location | removes the write; sets no new location policy |
| PD-9 | S19-F08 refuses non-printable characters (NUL, CR, LF, TAB, DEL), stricter than canon's NUL | a sanitization ID-5 counts as engineering hardening |
| PD-10 | Routing rather than fixing for R04 to R07 | each fix changes an owner tool's contract or a frozen family's tool (ID-5 (a), (d)) |
| PD-11 | Gap 4 and OBS-P3-3 are observations, not fixed | instruction ID-4 (non-security defects are not fixed here) |
| PD-12 | No change to `docs/server/reader_v1.md` or `docs/CLI_commands.md` | no fix changes a behavior they state (§19) |
| PD-13 | Regression tests go in the existing modules that already own each fixed source (13 hosts; §8.1). There is no new test module and no classifier change | Instruction ID-10 requires every new test module to be reached without a `ci.yml` change. A new HTTP module must be registered in `_HTTP_READER_TEST_OWNERS`, whose selection is pinned exactly, as are the owners of `registry_loader` and `generate_config_artifacts` (P-15). ID-11 keeps every pin true. The hosts run whenever their subject changes, and the change runs no full validation |
| PD-14 | The rehearsal `release_id` and open-rails digest are not binding; PR-30 records its own | §4.3 |
| PD-15 | Flask's automatic `OPTIONS` answer on the dev-harness paths stays unchanged in production; the retired paths answer 404 for `OPTIONS` too | it runs no handler; canon states no `OPTIONS` rule for these paths (whole-PF05 search); the change stays limited to requests that reach a handler; NC-18 |
| PD-16 | The hook's writer refusal is `_error("ERR_WRITER_FORBIDDEN", 403)` and its retired answer `_error("ERR_NOT_FOUND", 404)` | equal bytes and headers to `_writer_error` and to each factory's 404 (tests compare full header sets); the shape the governed boundary analyzer proves (P-13) |

## 18. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | the IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict:
- D-1 meets HDE Architecture §3.3 ("never mounted": no harness handler is reachable in production) and HDE-CLI-API-Vendor-Ref §5.11.2 and §5.12 (the forbidden refusal) together, and keeps the stub HDE-CLI-API-Vendor-Ref §5.4 and HDE Users Guide §6.4 state (PD-1, PD-2).
- HDE Architecture §3.8.1 is read as instruction ID-6 reads it (a duty of the dev server).
- S19-F05 applies §7.1.2's exact two-gate rule.
- S19-R02 is routed, so no decision between HDE-CLI-API-Vendor-Ref §7.1.10 and the passages that describe the current posture is taken (instruction §16).

Coverage read for this plan: the canon of "Canon relied on" and whole-canon searches on `main` for the unprefixed `POST /reader` stub, the retired `/ops` routes, compat authentication, the `--report` rule, the ingest log paths and the dev/admin gating rule.

## 19. Stale documents and carried items (not in this PR)

**Stale passages** (a fix makes them stale and this unit may not change them; instruction §9.5):

| Document | Statement | Owner |
| :- | :- | :- |
| HDE Architecture §3.3 "Current repository discrepancy" | the selected factory registers the Reader blueprint without an environment-specific unmount | Product Owner (canon doc-delta) |
| HDE Architecture §3.5 "Current repository discrepancy" | the retired routes' "continued presence in the selected blueprint": the code stays, a production-like application answers them as unknown paths | Product Owner (canon doc-delta) |
| HDE Architecture §3.8.1 | "exposes the same Reader and internal/dev sampler routes as the production adapter" | Product Owner (canon doc-delta; instruction ID-6) |
| HDE Users Guide §1.1 "Checked-in retired/noncanonical route drift" | add that a production-like application answers them as unknown paths | Product Owner (canon doc-delta) |
| HDE Mechanics Guide §34 "Current repository posture" | the production mount of the dev routes | Product Owner (canon doc-delta) |
| addendum 2.7 AD-4 item 4 and the decision record | "never fires" for the hook that runs and never matches (O-01) | Product Owner (wording) |

`docs/server/reader_v1.md` (the `/reader` gate, unchanged) and `docs/CLI_commands.md` ("APP_ENV in `dev|test|local`", which the exact gate keeps true) need no change. Repository documents that describe the production route set or the root helpers belong to WU-DOC-01 through the IA.

**Carried** (instruction §15):
- OBS-W4-1 and OBS-W4-3 → S19-R01, S19-R02 (Product Owner).
- LR4-O1 → X-01 (IA); OBS-P3-17 → X-02 (Product Owner).
- OBS-P4-5 and OBS-P4-7 are hazards §12 handles; OBS-P4-2 likewise (closed-rails profile sets `APP_ENV`).
- OBS-17 is RK-5; O-6 is RK-7.
- LR-O1 to LR-O3 apply in §9; LR-O2 is not triggered (the updater does not change), but its consumers run in the full sweep.
- OBS-W5-1 to OBS-W5-5 are applied (§5.1, §5.6 rows 43 and 44, §10 step 4).
- OBS-W4-2, OBS-W4-4, OBS-P4-3, OBS-P4-4, OBS-P4-1, the WU-PR-08 and WU-DOC-01 items, LR3-O1, LR3-O5 and AQ-1 stay with their owners, unchanged.

## 20. PR-30 and PR-35 ownership

**PR-30** (after Nathan's Proceed for this exact plan), in the dedicated session:
- recovers existing work first and confirms the head (§10 steps 1 and 3);
- implements only §8.1 and produces governed evidence only through owners (§9, §8.2);
- tests locally (§12), the attestation and the negative controls included;
- writes and reads back the S19 record and the PR result record v1.0;
- commits coherently: source, convergence, records;
- opens the one PR, returns `PR_CANDIDATE_PUBLISHED` and hands off to PR-35 in its own dedicated session;
- does not own review correction, current-head CI readiness or merge.

**PR-35** (its own dedicated session, from PR-30's handoff):
- retrieves and resolves the Codex code review findings on the code (addendum 2.3: no Codex security review; the Codex code review excludes Markdown and `docs/ephemeral/`, so the record's independent check is the IA's PR-40);
- retests and pushes coherent corrections; any member change re-runs §9 from step 2, any evidence-primary change from step 3b, with the attestation again; corrections to the S19 record are listed in its result;
- uses CI economically and verifies current-head CI (every selected lane, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability;
- records OBS-17 and O-6 if they occur;
- returns `MERGE_PENDING` without merging. Nathan merges manually; PR-40 by the IA follows the merge and reviews the record against ID-1 to ID-8.

## 21. Session identity and recovery envelope

```yaml
change: HDE-CRD-0002 / WU-PR-05
phase: PR-20 complete; AWAITING_PO_PROCEED
plan: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md (v1.0)
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0-prototype.diff
instruction: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-instruction-v1.0.md (v1.0)
baseline_and_reviewed_head: origin/main 1e97ba9b0c9f274192385068f0b71a0e7a904fa8
refresh_base_release_id: 2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner)
authoring_session: https://claude.ai/code/session_01FtgUXCdmFGLWASrRUWaDjc
next: PR-30 on Nathan's Proceed for this exact plan
vehicle: none (no implementation branch, commit or PR exists for this unit's code)
resume_point: PR-30 §10 step 1
```

## 22. TypeSafe reading for the receiving session (PR-30, WU-PR-05, plan v1.0)

Action sent (v8.2): "Implement, in a new dedicated session after the Product Owner's Proceed, one work unit of an approved change from a new, not yet reviewed detailed plan whose fixes were already prototyped, rehearsed and fully tested by the planning session, following its ordered task list: nine small security fixes across about ten hand-edited source files (a production mount policy for non-public HTTP routes in the adapter's blueprint and three app factories, exact environment-value gates, JSON recursion and body-read bounds, exact vendor rails checks, no ingest logs written into the checkout, a single-token CLI error, two path-validation rules) with four new test files of about 570 lines, plus writing a long security-review record document from the plan; four release members change, so a same-version release manifest re-cut and a fixed governed-evidence convergence of about twelve owner-tool steps regenerating about 56 paths run in order, each proven byte-stable on a second pass, followed by negative controls, a full test sweep and an attestation build; then commit, open the pull request and hand off. No live vendor, production or database call; code review, review resolution and a lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.96 (confidence 0.72); rung probabilities low 0.00, medium 0.02, high 0.19, extra high 0.60, max 0.19, ultracode 0.00. Model probabilities Fable 5.1 0.03, Opus 5.5 0.96, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.95). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.006, Fable 5.1 at extra high 0.018, Fable 5.1 at max 0.006, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.019, Opus 5.5 at high 0.182, Opus 5.5 at extra high 0.576, Opus 5.5 at max 0.182, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.002, Sonnet 5.5 at extra high 0.006, Sonnet 5.5 at max 0.002, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-18T17:50:57Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-18T17:50:57Z; HTTP 200 in 0.58 s; 5582 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: none printed.
- **Which request.** The installed TypeSafe scoring skill's request v8.2 (`request-v8.2.json`, sha256 `62486fcc4357e5917c3e9ba3e1ba9e2709364f0338dde70d4a88b116022b22ec`) and `scripts/score_v8.py`, run once, before this record was saved.
- **Action-text discrepancies.** These were found after the reading. The reading is recorded as obtained and was not re-run, because PR-20 directs one run.
  - The text says "four release members change"; the plan changes five (§9).
  - The text places the mount policy "in the adapter's blueprint and three app factories", with "about ten hand-edited source files" and "four new test files of about 570 lines". After the design revisions of §4.3, the factories are not edited and no test file is new. The plan hand-edits eight source files and adds 651 test lines to 13 existing test files (§8.1).
  - Otherwise the work's kind, size and order are as the text states.
- **Records.** The Notion row was not written, as PR-20 directs. Nathan's pick for PR-30 is not stated. Nathan's pick for this PR-20 session is not stated; its reading is instruction §19.

**Surface advice:** run PR-30 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.** Python 3.12 with CI's install and `-e .` of the worktree under test (package-index access for `pip install`), plus `ruby`, `bash` and `curl` on `PATH`; all were present in this session's cloud container. Unset the vendor, database and GitHub keys the container sets. The container's system Python carries `python-dotenv`; use the venv.
- **Run times observed here.** A full `tests/` sweep about 17 to 28 minutes; one refresh pass about 3 minutes; an attestation build about 3 minutes.
- **Discipline.** Run the refresh in the implementation branch's working tree only after the member bytes are final, and every check that can write tracked files in a detached worktree. Run the attestation before publishing.
- **Access.** No live vendor, production or database access is needed.
- **Order.** This plan's pull request should be merged first.

## 23. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-05 / PR-20 / plan 1, version 1.0 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-05 (S19) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z) |
| role/stage | dedicated WU-PR-05 PR engineering session / PR-20 |
| capture time | 2026-10-18T19:29:00Z |
| execution identity | https://claude.ai/code/session_01FtgUXCdmFGLWASrRUWaDjc |
| inherited usage | PR-10 instruction 1 (instruction §20) and the earlier uses it names |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating; owner the Product Owner) |

## Canon precedence (Plan Templates, "Canon precedence for template use")

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## Canon relied on

Read on `main` at `1e97ba9` (`docs/pfcanon/` unchanged since `86e002c`).

| Topic | Sources and sections |
| :- | :- |
| Plan authority, hold and Proceed | PR-20 — Create Detailed PR Implementation Plan — 100926.1 (read in full); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 |
| Overlays | PF10-HDE-Build-Notes v13.6 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md`): addenda 2.1, 2.3, 2.7 and 2.9 in full; 2.5, 2.6, 2.8 for the refresh rules and carried items |
| Production mount and dev harness (S19-F02, S19-F03) | HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §1.3, §3.2 (including "Dev fixture surface" and "A7 proof surface"), §3.3 in full, §3.4, §3.5 in full, §3.8.1 in full, §7.1, §7.2; HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.4 in full, §5.5 in full, §5.6, §5.11 in full, §5.12 in full; HDE Governance §2.0.10 `ENV_RAILS_POLICY_OK` and `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`, "Dev/admin APP_ENV gating (dev/test/local only)"; HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`) §1.1 table, §6.4; Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §2.1–§2.2 environment list (Staging/QA) |
| Errors (S19-F01, S19-F07) | HDE-CLI-API-Vendor-Ref §5.2 (items 1–3 and the §5.2.3 table), §8.1 to §8.4 |
| Rails and vendor (S19-F05, S19-F06, R01, R02) | HDE-CLI-API-Vendor-Ref §7.1.1 to §7.1.6, §7.1.10 in full, §7.1.11 preamble; HDE Engine Epics Map (`docs/pfcanon/PF16-Canon-HD Engine Epics Map v2.3.8.md`) EPIC-011 evidence list |
| Manifest and report paths (S19-F08, S19-F09) | HDE Math Spec (`docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.8.md`) §5.4.3; HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §25.6; HDE Users Guide §7.6 |
| Checklist map | instruction §4.1 and its sources, as instruction §16 records them read |
| Route-policy statement | Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "`bg:resolve --source vendor` route-policy posture", "Canon precedence for template use" |
| Refresh | Implementation Plan v1.1 §10; WU-PR-04 plan v1.0 §6.13 and result v1.0 §9; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" |
| In-flight documents | Specification v1.1 (rows S02, S09, S10, S15, S19; Exclusions; Constraints; Live QA class table); Plan v1.1 §3, §4, §7, §10–§15; Audit §6 S19 and Appendix B; PR instruction v1.0 |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails and redaction; code-review scope; sole Index/Mirror writer; no hand edits; pytest readiness; PR descriptions; "HDE-EPIC040 current posture"; "EPIC036 docs posture"; truncation guardrail) |

## Checks run by this session

All checks ran in the session scratchpad, with the environment of §4.3. They used worktrees of `1e97ba9`, of the final scratch commits `2280dea` and `a2957ae`, and, where a row says so, of `e3129b7`; none was ever pushed. Every exit code below was captured from the producer itself.

| Check | Result |
| :- | :- |
| 49 blob IDs at `1e97ba9` against instruction §5.1 | all equal |
| Full `tests/` sweep at `1e97ba9` | 4,918 passed, 3 skipped, 2 xfailed, 0 failed (1,037.7 s), exit 0; clean tree |
| Probes P-1 to P-14 (§4.2) | as recorded; sockets and DNS guarded where a vendor path ran |
| Governed analyzers on `a2957ae` (P-13) | architecture snapshot `verdict` and `analyzer_verdict` `pass`, `unknown_count` 0. Boundary analyzer: no unresolved presenter route; every check true and equal to the baseline's. Its full result differs from the baseline's only in source digests and line numbers |
| Affected directories and the two analyzer test files on `2280dea`, before the cut | 2,497 passed, 3 skipped, 2 xfailed, 17 failed. Each failure is a refusal of the not-yet-cut manifest (§4.3); the same 17 as on `e3129b7` |
| The 13 host modules on `a2957ae` | 915 passed, of which the 267 `test_s19_*` cases are part. With `APP_ENV` unset: 915 passed, and 267 of 267 `test_s19_*`. With `tests/adapter/test_jsonschema.py` first: 918 passed and 2 xfailed (that file's) |
| Negative controls NC-01 to NC-18 on `a2957ae` | each fails as intended (§4.3); files restored byte for byte; clean tree |
| Refresh rehearsal | on `e3129b7`: pass 1 37 runs and pass 2 34 runs, all exit 0, byte-identical (`234f053f…`), 56 paths. On `a2957ae`: a third pass of 34 runs, all exit 0, changed no byte. Rehearsal `release_id` `77204764…`; labels and sweep as §4.3 |
| Full `tests/` sweep on `a93c62b` (the superseded third design; P-15) | 5,182 passed, 3 skipped, 2 xfailed, 3 failed: the coverage, roster and ownership guards of P-15, which led to PD-13 |
| Full `tests/` sweep on `a2957ae` | 5,185 passed, 3 skipped, 2 xfailed, 0 failed (1,030 s), exit 0; clean tree; `XDG_STATE_HOME` left empty. That is the baseline's 4,918 plus the 267 `test_s19_*` cases |
| Instruction §5.6 read-only checks on `a2957ae` | admission `77204764…`, 45, `1.3.0`. The ten evidence and release checks: 10 × exit 0. The seven `--check`s: 7 × exit 0. Frozen families (four `--check`s and `ci/checks/check_cli_help.sh`): 5 × exit 0. `generate_config_artifacts.py --check`, `--compare-goldens .` with `--report` outside the tree, and the cutter `--check`: 3 × exit 0 |
| Sanity pipeline on `a2957ae` (`--log-path` outside the tree) | exit 0; `summary:PASS`, `first_failed_stage:NONE` (40 s) |
| Pre-existing failures | `generate_hde_epic037_v2_to_compat.py --check`, `generate_hde_epic037_bg_resolve.py --check` and `generate_hde_epic036_bg_resolve_route_policy.py --check` each exit 1 on `a2957ae`. Each has byte-identical output and exit 1 on `1e97ba9`, so none is caused by this unit |
| Attestation on `a2957ae` (external empty directory, `--require-clean`, then `--verify`) | exit 0 and exit 0; `release_admission` `PR06R_B_FINAL_PASS`, `validation_result` `PASS`, `source_commit` `a2957ae97ffc971c36cc9a1ab3aa881ecead9f38`, `source_commit_exact` true (109 s) |
| Classifier on `1e97ba9` → `a2957ae` | 77 paths; six lanes; 39 targets; the 13 host modules reached (§4.3); no unclassified path |
| Companion diff | `git apply --check` on `1e97ba9`: ok |
| Worktree state after each run | empty `git status --short --untracked-files=all` |
| TypeSafe v8.2 | one send for PR-30, HTTP 200 (§22) |

Not executed:
- hosted CI;
- the PR-30 and PR-35 runs on the real branch;
- the lanes as separate commands (the full sweep and the checks above cover their tests).

No live vendor, production or database call was made.
