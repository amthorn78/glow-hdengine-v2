---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-08-PR-IMPLEMENTATION-PLAN
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
predecessor: none (first plan for WU-PR-08)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-08
work_unit_title: "Environment template and operator documentation (PR; Coagulation; S16, S17)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob e2c9f0ae1337; landed by #685 as 3715252)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1, approved; blob abffa2ccbd44), with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1, DELTA_APPROVE; blob 5103fe29d588), whose P-7 is this unit's block
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE); the delta's approval docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE), §6 S16 and S17
REMEDIATION_REVIEW_ID: none (no remediation lineage)
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md §2 (Product Owner OPTION 1, 2026-10-21); its "Cost ceiling" row is not in force (addendum 2.18)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + IA-30 review v1.1
effective_baseline: approved base + the Specification delta 01 addendum (record docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md) + the Plan delta 01 addendum 2.19 (record docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-PF10-build-notes-addendum-v1.0.md) + PF10 addenda 2.18, 2.11 (as 2.18 narrows it), 2.14, 2.7 to 2.10 at their WU-PR-08 items, 2.3 and 2.1
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md (blob afce167947cd; 374,434 bytes; sha256 eab61385a819c859e1cf2743a204b70813feef23c902f647b3a5d7141454114d; the only PF10 file on main at 3715252)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md §2.18, §2.14, §2.11, §2.10, §2.9, §2.8, §2.7, §2.3, §2.1; docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-PF10-build-notes-addendum-v1.0.md (2.19); docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md (the Specification delta 01 addendum, not present in PF10 v13.7.1; cited by title and record, as the instruction does)
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0-prototype.diff (git diff 3715252 → prototype head 62767d0; 3 files, +11/−10; 86 lines; 4,408 bytes; sha256 954a7881fbdcf688826bdf41f4da593fc7ea9430529709c1e37cfa3024745acb; `git apply --check` clean on 3715252)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: https://claude.ai/code/session_01QezXHuju1GXwpubx7zDvTA (the dedicated WU-PR-08 PR engineering session that Nathan created; PR-20 now, PR-30 after the Proceed)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z, fetched and read in full in this session)
repository_baseline: origin/main 3715252 (#685). Outside docs/ephemeral/, every byte equals 67adb68, the instruction's measured baseline (git diff --stat 67adb68 3715252 lists only the instruction file)
working_branch: claude/awesome-einstein-ig69r1, restarted from 3715252 after #685 merged (documents only)
created_at: 2026-10-21T22:14:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§19)
---

# HDE-CRD-0002 WU-PR-08 — PR Implementation Plan v1.0

## 1. Result

**AWAITING_PO_PROCEED for v1.0.** This is the complete plan for WU-PR-08 within the instruction's scope: S16, S17 and one classifier registration, nothing else. It makes the three choices the instruction leaves to PR-20 (§5), maps every corrected statement to the code it matches (§6), and records the prototype (§13). The prototype ran in throwaway clones and passed:
- the classifier, as `ci.yml` calls it, selected all seven lanes;
- `.env.example` alone classifies as `documentation_only`;
- admission reports `1.3.0`, 45 members and `release_id` `77204764…`, unchanged;
- the rails workflow test and the classifier-owned tests pass;
- a full local replay of `ci.yml` passed all 16 steps with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (§13.4).

PR-30 applies the companion diff, re-runs §12 and publishes one PR.

This plan authorizes nothing. Only the Product Owner's `PR Implementation Proceed` (PR-30) for exactly v1.0 authorizes implementation, and only the Product Owner merges.

## 2. Lineage and sources read in this session

- **Instruction** v1.0, read in full at 3715252 (blob e2c9f0ae, the blob #685 recorded). Its §5 baseline was re-measured (§4).
- **Plan delta 01 v1.1** §1 to §3 and P-7 in full (Purpose to Business case); the 2.19 addendum record's front matter, "Source and approval", "Approved decision" and its WU-PR-08 passages.
- **Specification delta 01 addendum record**, read in full (C-1 to C-14; WU-PR-08 covers S16 and S17 only).
- **Product Owner decision record** (WU-PR-08 scope), read in full (§2 business case; §4 unchanged items).
- **WU-PR-07 plan v1.1**, read in full as the structure precedent.
- **PF10 v13.7.1:** addenda 2.18, 2.11, 2.14, 2.3 and 2.1 in full; 2.7, 2.8, 2.9 and 2.10 at their WU-PR-08 passages.
- **Code read at 3715252:** `adapter/wsgi.py` in full; `adapter/app.py`; `adapter/env_guard.py` in full; `adapter/http_reader.py` `create_app` registrations and `__main__` (lines 1315 to 1325); `adapter/factory.py` (no readiness route); `Procfile`; `scripts/dev_start_reader.sh`; `ci/checks/classify_ci_changes.py` (the sets, `_lanes_for_path`, `classify_paths`); `tests/adapter/test_jsonschema.py` (readyz test); `tests/retired_tests.md` (the retired `tests/adapter/test_readyz.py` row); `docs/ENDPOINTS_CATALOG.json` (the readyz row).
- **Documents:** `.env.example` (bytes) and `docs/ADAPTER_009.md` (232 lines), each in full.

## 3. Business case (ID-1)

Carried, not re-decided. From the decision record §2, under addendum 2.18:
- **Beneficiary:** whoever configures an HD Engine environment from `.env.example` (S16), and operators and agents who use `docs/ADAPTER_009.md` for health checks and local access (S17).
- **Evidence:** re-measured at 3715252 (§4); unchanged.
- **Benefit:** an environment set up from the template is complete; a health check or local call built from the document hits a real route and port.
- **Measure:** `.env.example` has a `GEO_API_KEY` entry, and each statement S17 corrects matches the code on the merged head, checked by PR-40. §6 is the table PR-40 checks.
- **No cost ceiling** (2.18 rule 1). No record of this unit records spend against one (rule 5). Work returns to the Product Owner only where 2.11 rule 8, 2.14, or a material change sends it (rule 2).

How the plan serves it: the template gains the one key the vendor provider requires. The document's readiness section now says the route is on `adapter.wsgi` only and always answers 200, so nobody builds a health check against the production app or the dev Reader, where it is 404 (§13.3). The port lines give the address the runner actually binds.

## 4. Baseline re-check (instruction §9.4)

Measured at 3715252 in a throwaway clone, closed rails, CPython 3.12.3 (§13 environment).

| Fact | Instruction (67adb68) | Measured (3715252) |
| :- | :- | :- |
| Bytes outside `docs/ephemeral/` | — | identical to 67adb68 |
| `.env.example` | 3 lines, no `GEO_API_KEY` | same |
| `docs/ADAPTER_009.md` | 232 lines; ID-2 at lines 6, 22, 33, 46 to 51, 122, 138 | same |
| ID-8, `ENGINE_ENV=dev\|staging\|prod` | "line 55" | **line 54** (line 55 is "Optional fixed meta: …"). Out of bound either way; no effect |
| `classify_paths(['.env.example'])` | `CI_CHANGE_SURFACE_UNCLASSIFIED` | same |
| `prepush_check.py … lanes membership build-notes` (3 paths) | lanes FAIL (unclassified), membership PASS, PF10 eab61385… | same; exit 1; "repository unchanged" |
| Served rules, `APP_ENV=prod` | factory 21, http_reader 21, wsgi 23 | 22, 22 and 24 counting Flask's own `/static/<path:filename>`; **21, 21 and 23 without it**. Same route sets; `/internal/healthz` and `/internal/readyz` on `adapter.wsgi` only |
| Governed primaries | neither document in the 606 | same (606; neither) |
| Index and Mirror rows for either document | none | none |
| `adapter/http_reader.py` `__main__` | lines 1316 to 1324 | **lines 1315 to 1325**; content as quoted |
| Readers of `.env.example` | none | none: no `.py`, `.sh`, `.yml`, `.yaml`, `.toml`, `.json` or `Procfile` reference outside frozen capture records, and no dotenv loader. Capture records naming it (`artifacts/math/_manifest_files.txt`, root `manifest_pre.sha256` and `manifest_post.sha256`, `_arch/`, `handoff/`, `.audit_src/`) have no reader in code |
| Tests naming `_DOCUMENT_PATHS` or `_WORKFLOW_CONTROL_PATH_LANES` | none | none (`tests/`, `ci/`, `tools/`) |
| Release | `1.3.0`, 45 members, `release_id` 77204764… | same |
| `tests/evidence/test_rails_ci_workflow_integration.py` | 2 environmental failures in the rehearsal container | **138 passed** in this container on the prototype (§13.2); neither failure recurred, so no base comparison was needed |

No difference changes a planning decision.

## 5. Design decisions (instruction §9.1)

- **PD-1, the registration's form (ID-4).** Add `.env.example` to `_DOCUMENT_PATHS`, with a two-line comment stating why it is safe:
  - **Smallest existing mechanism.** `_DOCUMENT_PATHS` exists for tracked files no code reads (`LICENSE`, `AGENTS.md`, …). One entry; no new set, branch or rule.
  - **Nothing affected is classed as irrelevant** (Plan Templates, CI lane discipline). Nothing in the repository reads the template (§4), so a change to it alone can change no test outcome; `documentation_only` hides no affected change.
  - **Alternative rejected:** `_WORKFLOW_CONTROL_PATH_LANES` would run lanes on every later template edit while protecting nothing. That is CI for its own sake (2.11 rule 2) and the avoidable hosted execution Plan Templates rules out.
  - **Stated limit:** if a later change makes code read `.env.example`, that change runs its own lanes; a template-only edit after it would not. The comment records the precondition, so the change that adds a reader sees it.
- **PD-2, owner or pin test (ID-5): none.** No test enumerates `_DOCUMENT_PATHS` or `_WORKFLOW_CONTROL_PATH_LANES` at 3715252. No row is added to the classifier's scenario table: it would pin an example and protect no behavior.
- **PD-3, the corrected wording (ID-3).** As in §6: each statement says only what the code does, cites the app or runner, and adds no claim of its own.
- **PD-4, the override guard: left unstated (ID-3).** ID-3 lets PR-20 state the guard "only as far as it verifies how the guard is wired". Measured:
  - `adapter/wsgi.py` line 20 calls `validate_or_fail(app)`. The wrapper in `adapter/env_guard.py` (lines 82 to 104) maps a Flask app to `app.config`, not the process environment.
  - With `APP_ENV=prod FEATURE_TOGGLES=1`, `adapter.wsgi.create_app()` builds without raising, while `validate_or_fail(os.environ)` raises `CANON_TOGGLES_OVERRIDE_IN_PROD` (§13.3).
  - `adapter.factory`, the production app, does not call the guard.

  So the document gains no startup-guard statement. Line 22 says only what readyz does. The wiring is finding F-1 (§17), outside this unit's bound.
- **PD-5, template placement.** `GEO_API_KEY=changeme` is appended as line 4. Lines 1 to 3 are byte-unchanged, so acceptance (1) is checked by `git diff`. The value matches the file's other placeholders; no secret.

## 6. Statement map (instruction §9.5; the measure PR-40 checks)

Line numbers are at 3715252. The corrected text is the prototype's (§13).

| # | Line | Current text | Corrected text | Code it matches (3715252) |
| :- | :- | :- | :- | :- |
| R-1 | 6 | `- GET /internal/readyz — resolver + catalogs/freeze + smoke ≤800 ms; sets X-Toggles-SHA on success` | ``- GET /internal/readyz — always 200 `{"ok":true,"schema":"v1"}`; no dependency check, no smoke (see Readiness rules)`` | `adapter/wsgi.py` 47–51: the handler returns `emit_public({"ok": True, "schema": "v1"})`, status 200, with no branch |
| R-2 | 22 | `- prod overrides: if config/runtime_overrides.json exists, /internal/readyz returns 503 (OverridesNotAllowedInProd).` | `- prod overrides: /internal/readyz performs no override check; config/runtime_overrides.json does not change its response.` | `adapter/wsgi.py` 47–51 (no file or environment read); outside `_archive/` and `.audit_src/`, no `.py`, `.sh` or `.yml` names `OverridesNotAllowedInProd`, and the only one naming `runtime_overrides` is `tests/adapter/test_jsonschema.py` line 64, which deletes the file before calling readyz; measured: with the file present under `APP_ENV=prod`, 200 and the same body (§13.3) |
| R-3 | 33 | `- Readyz only: X-Toggles-SHA: <64-hex>` | `- /internal/readyz adds no header of its own (no X-Toggles-SHA).` | `adapter/wsgi.py` 27–39 and 47–51: readyz uses only `_apply_common_headers`; no live code sets `X-Toggles-SHA`; measured headers in §13.3 |
| R-4 | 46–51 | "200 iff: 1) resolve_toggles() … 2) catalogs/freeze/toggles load, 3) a single compute_pair smoke … Else 503 with typed code …" | Two lines: readyz "is registered only by `adapter.wsgi:create_app()`, exposed as `adapter.app:app` for `flask --app adapter.app run`. The production app (`adapter.factory:create_app()`, started by `Procfile`) and the dev Reader (`python -m adapter.http_reader`) do not register it and answer 404." / "It returns 200 with `{"ok":true,"schema":"v1"}` and the header set above, unconditionally. It checks no dependency, runs no smoke and performs no override check, so a 200 shows only that the process answers." | `adapter/wsgi.py` 11, 47–51; `adapter/app.py` 4–5; `adapter/factory.py` and `adapter/http_reader.py` `create_app` register no readyz (21 rules each, F-3); `Procfile` line 1; measured 404 on both, 200 on `adapter.app` (§13.3) |
| P-1 | 122 | `Bind target for captures: http://127.0.0.1:5000` | `Bind target for captures: http://127.0.0.1:8000 — the runner binds loopback (127.0.0.1) only, on `$PORT` when set (default 8000).` | `adapter/http_reader.py` 1315–1325: `run(host="127.0.0.1", port=int(os.environ.get("PORT", "8000")), …)`; `scripts/dev_start_reader.sh` 10, 23, 26; measured listener `127.0.0.1:8000`, and `8123` with `PORT=8123` (§13.3) |
| P-2 | 138 | `Bind: http://127.0.0.1:5000  ·  Env: … ·  Auto-reload: off` | `Bind: http://127.0.0.1:8000 (`$PORT` when set)  ·  Env: … ·  Auto-reload: off` (only the bind part changes) | as P-1 |

**Not changed, checked:** line 149, `--bind 0.0.0.0:$PORT`, matches `Procfile` (measured `0.0.0.0` listener under gunicorn, §13.3). Line 5 (healthz) and line 4 (the WSGI adapter's three routes) are true of `adapter.wsgi` and are neither readiness nor port statements.

**Canon agreement:**
- HDE Architecture §3.4 classes `/internal/readyz` as a "Future concept [Speculative]", records it as defined only in the alternate `adapter/wsgi.py` factory, and says static bytes do not establish "a truthful readiness predicate". R-1 to R-4 say the same and claim no predicate.
- The old `compute_pair` smoke would have breached §3.4's [Required-Now] boundary ("MUST NOT touch Engine Core").
- P-1 and P-2 follow the HDE Mechanics Guide §34 "Required local capture profile" (loopback, port `8000` by default, an explicit `PORT` overrides, "captures and examples MUST use the effective port").
- They also follow the Change Process Guide §0.6.1 access-address bullets (`127.0.0.1` with the correct port; the server bind not renamed).

## 7. Real-input set (instruction §9.2; addendum 2.11 rules 4 to 6)

- **The template:** the file on the PR head, and the one key `engine/providers/vendor_http_hdapi.py` line 67 requires. No loader is written or modelled.
- **The document:** every corrected statement cites code on `main` (§6) and was checked against the running app in the operator's shell (§13.3). No statement describes behavior that does not exist.
- **The classifier:** the PR's real three-path diff, classified as `ci.yml` calls it, and the hosted CI run.
- **Out of the set:** any future reader of `.env.example` (PD-1's stated limit) and any other runner. Neither is modelled; a review finding that needs one gets the traced path and the limit (2.11 rule 7; 2.14 for a P1).

## 8. Canon map (instruction §4.1)

| # | Requirement | Where the plan meets it |
| :- | :- | :- |
| C1 | `127.0.0.1` with the correct port; the server bind not renamed | P-1, P-2; line 149 unchanged |
| C2 | Business case, real inputs, no emulation, dispositions, repeated class | §3, §7, §20 (PR-35) |
| C3 | P1 findings | §20 (PR-35) |
| C4 | Codex code review in the chain; security review not | §15, §20 |
| C5 | One `test` job, seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | §12 item 6; §13.1; acceptance (5) at PR-35 |
| C6 | Release identity unchanged | §13.1 admission; acceptance (3) |
| C7 | Smallest repository-grounded CI design; nothing affected classed as irrelevant | PD-1 |
| — | Readiness probe status in canon (HDE Architecture §3.4) | §6 "Canon agreement" |
| — | Local capture profile (HDE Mechanics Guide §34) | P-1, P-2 |

## 9. Files and requirement-to-change/test map

| Path | Change (prototype) | Check |
| :- | :- | :- |
| `.env.example` | +1: `GEO_API_KEY=changeme` | `git diff` shows one added line and nothing else (acceptance 1) |
| `docs/ADAPTER_009.md` | +7/−10: R-1 to R-4, P-1, P-2 | §6 map, re-read on the PR head (acceptance 2) |
| `ci/checks/classify_ci_changes.py` | +3: PD-1 entry and comment | classifier on `.env.example` alone (acceptance 4); rails workflow test and classifier-owned tests; hosted lanes (acceptance 5) |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-08-*` | this plan, its diff, PR-30's result record | — |

No new test (Audit §6: "no test is proportionate"; PD-2).

| Requirement | Acceptance | Proof |
| :- | :- | :- |
| S16 | (1) | §13.1 diff; PR-40 reads the merged file |
| S17 readiness | (2) | §6 R-1 to R-4; §13.3 |
| S17 ports | (2) | §6 P-1, P-2; §13.3 |
| Registration | (4), (5) | §13.1; hosted CI at PR-35 |
| No member change | (3) | §13.1 admission and membership |

## 10. Implementation sequence for PR-30

1. **Recover before creating.** Inspect this session's checkout, branches, worktrees, open PRs and `docs/ephemeral/` for WU-PR-08 work. Expected: only this plan and its diff.
2. **Branch** from current `origin/main` on the session's designated branch. If `main` moved past 3715252 outside `docs/ephemeral/`, re-run §4 for the three paths and the code §6 cites first, and record any difference. A change to a cited line updates §6's text in the result record before applying.
3. **Apply** `docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0-prototype.diff` (`git apply --check`, then `git apply`). A hunk that fails is applied by hand to the same effect and recorded.
4. **Local checks** (§12 items 1 to 5) under closed rails, with the vendor, database and GitHub keys unset.
5. **Commit** once: `docs(adapter): correct ADAPTER_009 readiness and port statements; add GEO_API_KEY to .env.example and classify it (HDE-CRD-0002 WU-PR-08 S16 S17)`.
6. **Replay** `python tools/ci/prepush_check.py --base <base> --head HEAD --full replay` on the commit (§12 item 6).
7. **Publish** the PR. The description uses the `.github/pull_request_template.md` headings with the `AGENTS.md` content rules. It names the registration's reason (PD-1) and says the PR runs all seven lanes because it changes the classifier.
8. **Result record** `docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-result-v1.0.md`: `PR_CANDIDATE_PUBLISHED`, the §6 map against the published head, checks with counts, the classifier output for `.env.example` alone, admission's `release_id`, the replay line, nonclaims. Hand off to PR-35 in its own session.

**Integration seams:** the classifier's `_DOCUMENT_PATHS` lookup in `_lanes_for_path` (no code change there). The document and template have no code seam. **Order inside the commit:** none needed; one commit.

## 11. PR split and merge dependencies

- **One PR.** Three small files, one coherent change.
- **Before merge:** PR-35's `MERGE_PENDING`; the Product Owner merges.
- **Order:** after WU-PR-07 (accepted, addendum 2.16); before WU-DOC-01, which follows this unit's merge.
- **No release member changes** (§13.1), so no manifest refresh and no evidence regeneration (ID-6).

## 12. Validation PR-30 runs (PR-35 re-runs items 1 to 5 after any correction)

Environment: CPython 3.12 with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`), `ruby`, `bash`, `curl`, git; `env -i` closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`); vendor, database and GitHub keys unset; the editable install pointed at the checkout under test (OBS-W5-5).

1. `python3 ci/checks/classify_ci_changes.py --base <base SHA> --head <head SHA> --event-name pull_request --github-output <tmp> --changed-tests-output <tmp>`: exit 0, `reason=selected_lanes`, all seven lanes. Then `classify_paths(['.env.example'])`: `documentation_only`, no `CI_CHANGE_SURFACE_UNCLASSIFIED` (acceptance 4).
2. `python tools/ci/prepush_check.py --base <base> --head HEAD --path .env.example --path docs/ADAPTER_009.md --path ci/checks/classify_ci_changes.py lanes membership build-notes`: PASS; none a member.
3. Admission: `engine.config.registry_loader.load_active_mechanics_bundle()` succeeds; `1.3.0`, 45 members; `engine.runtime.identity._manifest_release_id()` equals the base's `77204764…` (acceptance 3); `python scripts/release_id_recompute.py --check-manifest-only` exit 0.
4. `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py` (138 expected), then the classifier-owned and readiness-adjacent set of §13.2 (791 passed, 2 xfailed expected).
5. The §6 map re-read against the head, and the §13.3 live probes repeated (dev Reader on 8000 and on an explicit `PORT`; `flask --app adapter.app run`; gunicorn with the `Procfile` arguments on a scratch port).
6. `prepush_check.py --base <base> --head HEAD --full replay` on the commit.

## 13. Prototype record

Throwaway clones under the session scratchpad, both at 3715252. The session checkout was not changed. The prototype was committed only in its clone (head 62767d0). Environment: CPython 3.12.3 venv with CI's install and the clone installed editable; git 2.43.0; Werkzeug 3.1.9; `env -i` closed rails as §12. Every clone ended with an empty `git status --short`.

### 13.1 Classifier, lanes, membership, admission

| Run | Result |
| :- | :- |
| Classifier as `ci.yml` calls it, base 3715252, head 62767d0, `pull_request` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=product,compat,db,rails,evidence,qa,release`; `needs_python=true`, `changed_tests=true`; 166 changed-test targets |
| `classify_paths` on `.env.example`; on `docs/ADAPTER_009.md`; on both | `documentation_only`, no lanes, each |
| `prepush_check.py … lanes membership build-notes` (3 paths) | PASS; lanes as above (166 targets); not-member ×3; PF10 v13.7.1 eab61385…; "repository unchanged"; exit 0 |
| Admission at 62767d0 | `load_active_mechanics_bundle()` ok; `1.3.0`, 45; `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e (= base) |
| `scripts/release_id_recompute.py --check-manifest-only` | exit 0 |
| Change set | 3 paths, +11/−10; nothing under `.github/`, `catalog/`, `engine/`, `docs/evidence/`, `artifacts/`, `audit/`, `requirements*`, `pyproject.toml` or `Procfile` |

### 13.2 Tests (on 62767d0)

| Run | Result | Time |
| :- | :- | :- |
| `tests/evidence/test_rails_ci_workflow_integration.py` | 138 passed, exit 0 | 21:38:52Z to 21:39:22Z (29.4 s) |
| `tests/evidence/test_http_reader_ci_ownership.py`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/qa/test_qa_tool_ownership.py`, `tests/tools/test_prepush_check.py`, `tests/config/test_config_artifacts.py`, `tests/bodygraph/test_check_magic10_gate_readiness.py` (every test file that names the classifier), with `tests/adapter/test_jsonschema.py` (readyz), `tests/http/test_endpoint_catalog.py` and `tests/scripts/test_dev_start_reader.py` | 791 passed, 2 xfailed (the two `/internal/version` cases marked `xfail` in `test_jsonschema.py`), exit 0 | 21:39:30Z to 21:42:34Z (183 s) |

### 13.3 Live probes (operator's shell, at 3715252; the document change does not affect them)

| Runner | Listener | `/internal/version` | `/internal/readyz` | `/internal/healthz` |
| :- | :- | :- | :- | :- |
| `python -m adapter.http_reader`, `PORT` unset | `127.0.0.1:8000` | 200 | 404 | 404 |
| `PORT=8123 scripts/dev_start_reader.sh` (banner "Binding port 8123 … (host=127.0.0.1)") | port 8123 | 200 | 404 | 404 |
| `flask --app adapter.app run` | "Running on http://127.0.0.1:5000" (Flask's default) | 200 | 200 | 200 |
| `APP_ENV=prod python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:8124 …` | `0.0.0.0:8124` | 200 | 404 | 404 |

- readyz on `adapter.app`: body `{"ok":true,"schema":"v1"}`. Headers: `Cache-Control: no-store`, the JSON content type, `X-Adapter-Version`, `X-Engine-Tag`, `X-Release-Id`, `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options`, `X-Correlation-Id`. No `X-Toggles-SHA`.
- Test client, `adapter.wsgi`, `APP_ENV=prod`, with `config/runtime_overrides.json` present: 200, same body, no `X-Toggles-SHA`, `Strict-Transport-Security` present. The file was removed afterwards; the clone was clean.
- Guard wiring (PD-4): `validate_or_fail(os.environ)` with `APP_ENV=prod FEATURE_TOGGLES=1` raises `CANON_TOGGLES_OVERRIDE_IN_PROD`; `adapter.wsgi.create_app()` in the same environment builds without raising; `APP_ENV` is not in `app.config`.

### 13.4 Full local replay

`python tools/ci/prepush_check.py --base 3715252 --head HEAD --full replay` on 62767d0, in the tool's own throwaway copy, 21:42:41Z to 22:12:01Z (step time 1,754.5 s):
- exit 0; `PREPUSH_CHECK_RESULT: PASS replay=PASS`; "copy after replay: clean"; "repository unchanged";
- `ci.yml` sha256 d02021f3… (the modelled one); `hdctl` resolves to the copy's `engine/cli/main.py`;
- all 16 steps SUCCESS (1, 4 and 5 excluded and substituted, as the tool states); `CI_APPLICABILITY_AND_EXACT_HEAD_OK`;
- changed tests 4,523 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79, with the attestation built and verified.

This is a local replay, not hosted CI; acceptance (5) is checked on the hosted run at PR-35.

## 14. Interface contracts (instruction §8)

- **WU-DOC-01** receives, through this IA's PR-40: ID-8's out-of-bound statements and the additions in §18; O-19's documentation side.
- **WU-OPS-01:** `release_id` is unchanged by this unit (§13.1).
- **QA-10:** S16 and S17 are not production-affecting.

## 15. Security and migration

- `.env.example` carries the placeholder `changeme`, never a key. No secret, token or key value is in any record, test or commit; this session's env probes recorded only SET or UNSET.
- Closed rails for every local run; the container's vendor, database and GitHub keys were kept out of every child by `env -i`.
- The Codex code review is in the chain; the Codex security review is not (addendum 2.3).
- **Migration:** none. **Rollback:** the Product Owner's revert of the squash commit; no member changes, so no refresh.

## 16. Risks and recovery

| Risk | Treatment |
| :- | :- |
| Misclassification: a later change makes code read `.env.example` | PD-1's comment records the precondition; that change runs its own lanes |
| The full seven-lane run exposes failures that are not this unit's | PR-35's base-red rule (P-7 Risks); the unit is not widened. Known hazards: OBS-P4-5 (no such test is added here) and OBS-P4-7 (`tests/adapter/test_jsonschema.py` calls readyz and leaks `ENGINE_ENV`) |
| Document drift: `main` moves under a cited line | §10 step 2 re-measures; §6 is re-checked on the head |
| A Codex finding on a constructed input | 2.11 rule 7 (traced path and stated limit); rule 8 after two same-class rounds; a P1 under 2.14 |
| Interruption | Resume in this session from the last saved artifact; prototypes only in throwaway clones |

## 17. Findings for the Product Owner (outside this unit's bound; not changed here)

- **F-1. The override guard as wired does not see the process environment.** `adapter/wsgi.py` calls `validate_or_fail(app)`. The wrapper maps the app to `app.config`, which holds no `APP_ENV`, so the guard computes `dev` and never refuses. The production app, `adapter.factory`, does not call it. Measured in §13.3. This unit changes no code (P-7 "Nothing else"; instruction §7), and the document now makes no claim about the guard (PD-4). Owner: the whole-change IA, through PR-40, as a later-change candidate for the Product Owner. Not a blocker for this unit.
- **F-2. Further stale statements in `docs/ADAPTER_009.md`, outside S17's bound** (added to ID-8's list for WU-DOC-01):
  - lines 124 to 130 and line 138's "Env:" part list a capture environment without `APP_ENV=dev`, `ALLOW_NETWORK=0`, `LC_ALL` or `LANG`, which the HDE Mechanics Guide §34 capture profile requires;
  - line 55's `TOGGLES_SHA`: no live code reads it;
  - line 29's `X-Release-Id: <release_id>`: `adapter.wsgi` sends its config default (`rel_dev`, observed in §13.3);
  - lines 7 and 21 ("prod requires Authorization: Bearer"): under gunicorn with `APP_ENV=prod` and no token configured, `/internal/version` answered 200 without one (observed once in §13.3; not investigated).

## 18. Carried items (instruction ID-7, ID-8 and §15)

| Item | Disposition |
| :- | :- |
| §9.1 choices | Made: PD-1, PD-2, PD-3 (with PD-4 and PD-5) |
| Loopback bind statements (2.7 to 2.9) | Met: P-1 states the loopback bind and the effective port; P-2 the address |
| OBS-P4-5 | Stated hazard (§16); no open-rails vendor-path test is added |
| O-19 | Not this unit: neither script changes; documentation to WU-DOC-01; any code change to the Product Owner |
| F-3 (route exposure) | Holds unchanged: 21 / 21 / 23 non-static rules (§4); no route changes; R-4 rests on it |
| Not carried | 2.10's `1.4.0` cut and 2.6's purity-report regeneration (Plan delta 01 K-1, K-2) |
| ID-8 out-of-bound statements | Recorded for WU-DOC-01 (lines 7 and 8 duplicate; line 20 "localhost"; line 54 `ENGINE_ENV`, cited as 55 in the instruction; lines 145 to 150 start line), with F-2's additions |
| OBS-P4-7 | A full-lane hazard (§16); a later unit through the IA |
| Business cases for WU-DOC-01 and WU-OPS-01; the deploy-source doc-delta; the Specification delta 01 addendum's PF10 number | The Product Owner, as carried |
| F-1, F-2 | New; the IA through PR-40 (§17) |

## 19. Canon-conflict register

Carried unchanged: CR-1, CR-2 and CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); CR-6 APPROVED (a) (IA through RS-20); CR-7 and CR-8 APPROVED (a) each (Product Owner). **No new conflict:**
- The instruction's two non-conflicts stand (the `127.0.0.1` convention vs the `0.0.0.0:$PORT` production bind; the stale readiness claims as documentation drift).
- HDE Architecture §3.4 does describe readyz semantics, but as a [Speculative] future concept, and records the current repository behavior as this plan's corrected text states it. So there is no conflict between canon and the corrected document.

## 20. PR-30 and PR-35 obligations

- **PR-30** (this session, after the Proceed for exactly v1.0):
  - recover existing work first;
  - implement only §9's three files from the companion diff;
  - run §12;
  - commit once, publish the PR and record the replay;
  - write the result record;
  - return `PR_CANDIDATE_PUBLISHED`, handing off to PR-35 in its own session.
  - It does not resolve reviews, wait for CI readiness or merge.
- **PR-35** (its own session):
  - retrieve the Codex code review findings and disposition them under 2.11 rule 7 and 2.14: a P1 on a real input is fixed; declining a P1 or a security finding goes to the Product Owner first; rule 8 after two same-class rounds;
  - push coherent corrections and re-run §12 items 1 to 5;
  - verify current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability; a failure also red on the base is handled as base-red;
  - return `MERGE_PENDING` without merging.
- **Nonclaims every record keeps:** no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release cut; no change to `/internal/readyz`'s behavior.

## 21. TypeSafe reading for the receiving session (PR-30, WU-PR-08, plan v1.0)

Action sent (v8.2): "Implement, in a dedicated session, one small work unit from a detailed PR plan that the Product Owner has proceeded: apply an already prototyped change of about 20 lines across three existing files (add one placeholder key to a three-line environment template, correct six readiness and port statements in one 230-line operator document, and add one entry to an existing set in a 2,100-line CI change classifier); a task list and a prototype diff exist; run the classifier, the release admission check, the unit's existing tests and a full local CI replay, then commit and open the pull request, which runs all seven CI lanes; no live provider call occurs; an automated code review, a separate merge-readiness session and a lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at medium.** Effort score 1.25 (confidence 0.84); rung probabilities low 0.01, medium 0.79, high 0.17, extra high 0.03, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.90, Sonnet 5.5 0.10, Haiku 5.5 0.00 (confidence 0.87). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.009, Opus 5.5 at medium 0.711, Opus 5.5 at high 0.153, Opus 5.5 at extra high 0.027, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.001, Sonnet 5.5 at medium 0.079, Sonnet 5.5 at high 0.017, Sonnet 5.5 at extra high 0.003, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-21T21:42:53Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-21T21:42:53Z; HTTP 200 in 0.67 s; 5496 input and 71 output tokens; jev-1.13.0. Rung by rule: medium (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Records.** Run once with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `implementation`, before this plan was saved. The Notion row was not written (PR-20 handoff rule; addendum 2.1). Nathan's pick for PR-30 is not stated; his pick for this PR-20 session is not stated (its reading is the instruction's §19).

**Surface advice:** PR-30 continues in this same top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with GitHub access for the PR. Its environment needs:
- CPython 3.12 with CI's install, which needs package-index access;
- `ruby`, `bash`, `curl` and git;
- closed rails through `env -i`, because this container sets vendor, database and GitHub keys;
- throwaway clones for the live probes.

Observed times: the classifier takes seconds, the rails test 30 s, the §13.2 set 3 minutes, and the full replay about 30 minutes; a hosted seven-lane run takes about 20 minutes. No live vendor, production or database access is needed. This plan's pull request should be merged first.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-08 / PR-20 / plan 1 (v1.0) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| work unit | WU-PR-08 (S16, S17) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z) |
| role/stage | dedicated WU-PR-08 PR engineering session / PR-20 |
| capture time | 2026-10-21T22:14:00Z |
| execution identity | https://claude.ai/code/session_01QezXHuju1GXwpubx7zDvTA |
| inherited usage | instruction v1.0 (PR-10, session_01U3QLYTkfUepeRbSGZNPj9N); the Plan delta 01 review v1.1 and the WU-PR-08 decision record (Isis, session_012tPq26JWVhCYZmcqTidpV2) |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at 3715252 (`docs/pfcanon/` last changed by 7b763db, PF10 v13.7.1).

| Topic | Sources and sections |
| :- | :- |
| Plan authority and content | PR-20 — Create Detailed PR Implementation Plan — 100926.1, read in full |
| Overlays | PF10-HDE-Build-Notes v13.7.1: 2.18 in full (no ceiling; WU-PR-08 effects); 2.11 in full (rules 1 to 8); 2.14 in full (P1); 2.3 in full (reviewer chain); 2.1 in full (TypeSafe reading); 2.7 ("Downstream", the WU-PR-08 bullet), 2.8 (the loopback carry), 2.9 (OBS-P4 table; carried-for-later bullet), 2.10 (LR5-O4; F-3; carried-for-later bullet), at those passages. The 2.19 record and the Specification delta 01 addendum record, as §2 states |
| Readiness probe | HDE Architecture (`PF02-Canon-HDE-Architecture-v2.4.6.md`) §3.4 "Internal ops signals", read in full; §3.3's closing discrepancy and routing passages read in passing |
| Local capture profile | HDE Mechanics Guide (`PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §34 "Dev HTTP Harness (single home)": the "Required local capture profile" paragraph and the bounded-context route table, read in full |
| Dev access address | Change Process Guide (`PF06-Canon-Change-Process-Guide-v2.5.4.md`) §0.6.1, the infra-fact and access-address bullets |
| Dev binding facts | Glow Infrastructure (`PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §2.4 "Env Deployment Inventory", read at the Development and QA lists (`PORT=8000`, `DEV_SAMPLER_URL=http://127.0.0.1:8000/…`, `GEO_API_KEY` among the keys), and §10.2 "Binding" (`Procfile` `0.0.0.0:$PORT`) |
| CI design | Plan Templates (`PF27-Canon-Plan-Templates-v2.0.5.md`) "CI lane classification and automated budget-control discipline", read in full |
| Operative documentation | `AGENTS.md`: canon-first rule; "HDE-EPIC039 current workflow posture"; "Release identity"; "HDE-EPIC040 current posture"; closed rails and redaction; "Code review guidelines"; "PR descriptions" |
| In-flight documents | the instruction v1.0 in full; Plan delta 01 v1.1 P-7 in full; the decision record in full; the two addendum records as §2 states |

Canon searched for `readyz`, `healthz` and the dev port: HDE Build Checklist Coagulation and HDE Mechanics Guide §32.3 "Health/ready & lifecycle" list `/readyz` as a probe concept; Reality Audits RA-14 records readyz as uncatalogued (since catalogued, `docs/ENDPOINTS_CATALOG.json`). Neither governs this document's wording.
