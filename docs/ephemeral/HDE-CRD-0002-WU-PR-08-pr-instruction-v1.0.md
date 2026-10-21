---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-PR-08-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-08
work_unit_title: "Environment template and operator documentation (PR; Coagulation; S16, S17)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_overlays: (1) Specification delta 01 (DELTA_APPROVE), recorded by the Specification delta 01 addendum (record docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md); (2) Implementation Plan delta 01 v1.1 (DELTA_APPROVE), recorded by addendum 2.19 (record docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-PF10-build-notes-addendum-v1.0.md); its P-7 is this unit's block; (3) PF10 addendum 2.18, no cost ceiling; (4) PF10 addendum 2.11 rules 1 to 8 as 2.18 narrows them, and addendum 2.14 (P1 findings); (5) addenda 2.7, 2.8, 2.9 and 2.10 at their WU-PR-08 carried items; (6) addendum 2.3 (the Codex code review stays in the chain, the Codex security review does not); (7) addendum 2.1 (§19 only)
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (blob 9408d6ed091b), approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44), with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1; blob 5103fe29d588)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with the delta's approval docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE; blob 4801c7cc2c9d)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276db), §6 S16 and S17
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md §2 (Product Owner OPTION 1, 2026-10-21; blob efc220928f7c). Its "Cost ceiling" row is not in force (addendum 2.18)
predecessor_unit_acceptance: WU-PR-07 accepted by docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-work-unit-lineage-review-v1.0.md (ACCEPT on #668; addendum 2.16)
structure_precedent: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md (blob afce167947cd; 374,434 bytes; sha256 eab61385a819c859e1cf2743a204b70813feef23c902f647b3a5d7141454114d)
pf10_note: PF10 v13.7.1's last addendum is 2.18 (no cost ceiling). The Plan delta's addendum record is numbered 2.19; the Specification delta 01 addendum's record also calls itself 2.18 and is cited here by title and record. No instruction decision depends on either number
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state of 2026-10-12T02:29:33.739Z, read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-21T20:58:37Z
repository_baseline: origin/main 67adb68dcbf79928a2cb40e493cc288f272dd494 (#684). Every repository fact in §5 was measured at this head under closed rails, CPython 3.12.3
receiver: dedicated HDE-CRD-0002 WU-PR-08 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state of 2026-10-12T02:29:47.327Z, read at its Inputs and Execute sections in this invocation)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§16)
---

# HDE-CRD-0002 WU-PR-08 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete PR instruction for work unit WU-PR-08 of HDE-CRD-0002. The whole-change IA issues it from Implementation Plan v1.1 as amended by the approved Plan delta 01 v1.1, whose P-7 replaces the unit's block. A dedicated PR-20 session can plan the unit from this instruction and the linked repository and canon, without reconstructing upstream intent (§17).

The unit is small:
- one placeholder key in `.env.example` (S16);
- corrected readiness and port statements in `docs/ADAPTER_009.md` (S17);
- one classifier registration, so that CI accepts a change to `.env.example`.

The registration makes the pull request run all seven CI lanes.

It does not:
- author the per-file plan, the classifier registration's final form or the document's wording. Those are PR-20's (§9);
- authorize implementation, a commit, a pull request or a merge. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for the exact PR-20 plan authorizes implementation, and only Nathan merges;
- cut a release, change a release member or change a CI workflow;
- decide a canon, product or scope question, change canon or create a PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-08: Plan delta 01 v1.1 P-7, "WU-PR-08 — Environment template and operator documentation (PR; Coagulation)", replacing the Plan v1.1 §7 block of the same ID |
| Requirements | S16 (source 5(h)); S17 (source 5(i), O-P07-05) |
| Approved base | Specification v1.1 → Plan v1.1 + review v1.1 (refs above) |
| Overlays | Specification delta 01 and its addendum; Plan delta 01 v1.1 and its addendum 2.19; addenda 2.18, 2.11, 2.14, 2.7 to 2.10, 2.3 and 2.1, as the header names them |
| Upstream units | WU-PR-01 to WU-PR-07, all accepted |
| Phase | Coagulation (Specification delta 01, C-10: "Durable environment discipline: S16, S17"; completion boundary "S16 and S17 hold on `main`") |
| Live QA class | Not production-affecting (Specification table: "documentation and the environment template") |

## 3. Unit selection and dependency state

- **Plan approval.** Isis approved Plan v1.1 (review v1.1, INITIAL_APPROVE) and Plan delta 01 v1.1 (review v1.1 of the delta, DELTA_APPROVE).
- **Unit type.** PR unit.
- **Dependency state: ready.**
  - P-7: "Eighth code unit, after WU-PR-07; the order is kept." WU-PR-07 is accepted (lineage review v1.0 on #668; addendum 2.16).
  - The business case exists (decision record §2). Addendum 2.11 rule 3, as 2.18 narrows it, requires PR-10 to carry it into the instruction; there is no ceiling.
  - No `HDE-CRD-0002-WU-PR-08-*` file other than the decision record exists on `main`.
  - No QA Guide, QA Plan or Ops receipt is a prerequisite (Plan v1.1 §9 item 4).
- **Order.** WU-PR-07 → **WU-PR-08** → WU-DOC-01 → WU-OPS-01 → QA-10 readiness.
- **Downstream dependents.**
  - WU-DOC-01 follows this unit's merge. It owns the repository documents this unit does not touch (§7; ID-7).
  - WU-OPS-01 places the `main` head after WU-PR-08 and WU-DOC-01 merge, and proves it by `/internal/version`'s `release_id`. This unit changes no member, so that `release_id` is the one admission reports at this unit's base (§5.5).

## 4. Required behavior

**Acceptance intents**, verbatim from the approved Specification (unchanged by Specification delta 01):

| ID | Scope | Acceptance intent |
| :- | :- | :- |
| S16 | "Add `GEO_API_KEY` to the environment template" | "`.env.example` has a `GEO_API_KEY` entry" |
| S17 | "Correct the readiness and port statements in `docs/ADAPTER_009.md`" | "The readiness rules describe what `/internal/readyz` does, and the port statements are current" |

**Plan delta 01 v1.1 P-7** is binding as written: its Purpose, Bounded scope, Inputs, Deliverables (1) to (4) with "Repository facts for PR-20", Dependencies and order, Acceptance and verification (1) to (5), Evidence obligations, Risks and recovery, Nonclaims and Business case. PR-20 reads the block in full. Its Bounded scope is: "S16, S17, and one classifier registration that makes `.env.example` a classified change surface. Nothing else."

**Audit §6 S16 and S17** "Required behavior" are inputs:
- S16: "One `GEO_API_KEY=changeme` entry (placeholder value, no secret)."
- S17: "The readiness section states what `/internal/readyz` does and on which app it exists; the port statements name the current bindings and defaults. The default documented dev access host stays `127.0.0.1` with the correct port (Change Process Guide, dev access address convention)."

### 4.1 Requirements mapped to canon

| # | Requirement | Governing source (read for this instruction) |
| :- | :- | :- |
| C1 | The documented non-prod access host is `127.0.0.1` with the correct port; the convention never renames the server bind address or the production address | Change Process Guide §0.6.1, the client-access convention bullets ("the default documented client access host MUST be `127.0.0.1` with the correct port and endpoint path"; "It MUST NOT be used to rename or obscure … the server bind address") |
| C2 | Business case, real inputs, no emulation, finding disposition, repeated finding class | PF10 addendum 2.11 rules 1 to 8, with addendum 2.18 (no ceiling) |
| C3 | P1 findings | PF10 addendum 2.14 rules 1 to 6 (rule 5 withdrawn by 2.18) |
| C4 | Reviewer chain | PF10 addendum 2.3: the Codex code review is in the chain; the Codex security review is not |
| C5 | The one `test` job, seven change-aware lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | `AGENTS.md` "HDE-EPIC039 current workflow posture" |
| C6 | Release identity unchanged | `AGENTS.md` "Release identity" and "HDE-EPIC040 current posture"; Specification delta 01, C-5 and C-7 |
| C7 | Smallest repository-grounded CI design, chosen by the implementation task; nothing affected classified as irrelevant | Plan Templates, "CI lane classification and automated budget-control discipline" |

### 4.2 Binding IA decisions

- **ID-1, business case (addendum 2.11 rule 1, as 2.18 narrows it).** Carried verbatim from the decision record §2:
  - *Beneficiary:* "Whoever configures an HD Engine environment from `.env.example` (S16), and operators and agents who use `docs/ADAPTER_009.md` for health checks and local access (S17)".
  - *Evidence:* "`.env.example` holds only `HD_API_BASE_URL`, `HD_API_KEY` and `HD_API_SECRET`, while `engine/providers/vendor_http_hdapi.py` requires `GEO_API_KEY`." And for S17: "`docs/ADAPTER_009.md` lines 46–51 describe `/internal/readyz` as a resolver, catalog and `compute_pair` smoke returning a typed 503 on failure. `adapter/wsgi.py` lines 47–51 return `{"ok": true, "schema": "v1"}` with 200 unconditionally, and `adapter/factory.py`, the production app, registers no `/internal/readyz`. Lines 122 and 138 give `127.0.0.1:5000`, while the runners bind `$PORT` (default 8000)." This is re-measured at `67adb68` in §5.
  - *Benefit:* "An environment set up from the template is complete; a health check or local call built from the document hits a real route and port".
  - *Measure:* "`.env.example` has a `GEO_API_KEY` entry (S16's acceptance intent), and each statement S17 corrects matches the code on the merged head, checked in WU-PR-08's lineage review (PR-40)".
  - *No cost ceiling* (addendum 2.18 rule 1). No session records spend against a ceiling (rule 5). Work returns to the Product Owner only where another rule sends it (rule 2).
  - The registration is not CI work for its own sake (addendum 2.11 rule 2). Without it, CI refuses any pull request that changes `.env.example` (§5.4).
- **ID-2, the statements S17 corrects.** S17's scope is "the readiness and port statements" in the document. Its acceptance is that "the readiness rules describe what `/internal/readyz` does", and the measure is that "each statement S17 corrects matches the code". So every readiness statement and every port statement in the document is in scope, not only the "Readiness rules" section the Audit names. Measured at `67adb68` (§5.2), they are:
  - **readiness:** line 6 (overview: "resolver + catalogs/freeze + smoke ≤800 ms; sets X-Toggles-SHA on success"), line 22 ("if config/runtime_overrides.json exists, /internal/readyz returns 503 (OverridesNotAllowedInProd)"), line 33 ("Readyz only: X-Toggles-SHA: <64-hex>") and lines 46 to 51 ("Readiness rules");
  - **port:** lines 122 and 138 (`http://127.0.0.1:5000`). Line 149's production `--bind 0.0.0.0:$PORT` already matches `Procfile` and needs no change.

  PR-20 re-reads the document at its head and records the final list. A statement that is neither a readiness nor a port statement is out of scope (ID-7).
- **ID-3, what the corrected statements say.** Each corrected statement matches the code at the PR head (§5.3). PR-20 writes the wording. The content, as measured at `67adb68`:
  - **Readiness.** `/internal/readyz` exists only on `adapter.wsgi`'s app (exposed for `flask --app adapter.app run` by `adapter/app.py`, and used by tests). It returns 200 with `{"ok":true,"schema":"v1"}` and the common header set, with no dependency check, no smoke and no `X-Toggles-SHA` header. The production app (`adapter.factory:create_app()`, the `Procfile` app) and `adapter.http_reader.create_app` register no `/internal/readyz`.
  - **No readiness-time override check.** The readyz handler performs no runtime-overrides check. The production override refusal the document attributes to readyz is a startup environment guard (`adapter/env_guard.py` `validate_or_fail`, code `CANON_TOGGLES_OVERRIDE_IN_PROD`). PR-20 states it only as far as it verifies how the guard is wired, or leaves it unstated.
  - **Ports.** The canonical dev runner (`python -m adapter.http_reader`, started by `scripts/dev_start_reader.sh`) binds `127.0.0.1` on `$PORT`, default `8000`, with the debugger and reloader off. The documented dev access address is therefore `http://127.0.0.1:8000`, or `$PORT` where it is set (C1). Production binds `0.0.0.0:$PORT` (`Procfile`).
- **ID-4, the registration (P-7 deliverable 3).** PR-20 chooses and states the form, from the classifier's existing mechanisms (Plan Templates, C7). The repository facts are in P-7 and were re-measured in §5.4. The instruction does not choose.
- **ID-5, the owner or pin test (P-7 deliverable 4).** It applies only if a test enumerates the registry the registration changes. At `67adb68` no test enumerates `_DOCUMENT_PATHS` or `_WORKFLOW_CONTROL_PATH_LANES` (§5.4). PR-20 re-checks at its head and records the result. An example-based scenario table that pins chosen paths, such as `tests/evidence/test_rails_ci_workflow_integration.py` `test_change_classifier_selects_expected_execution_scenarios`, does not enumerate a registry, so the deliverable does not require a row there. A row added there would be a plan choice with its reason, not a deliverable.
- **ID-6, release identity.** No member changes (§5.5), so there is no manifest refresh, no evidence regeneration and no convergence. Acceptance (3) is checked by admission at the PR head.
- **ID-7, carried items** (P-7 Inputs). Each has a disposition PR-20 records:
  - **The loopback bind statements** (addenda 2.7, 2.8 and 2.9): "WU-PR-08's port and bind statements (S17) describe the loopback bind". They are met by ID-3's port content (`127.0.0.1`, the runner's loopback bind).
  - **OBS-P4-5**: the attestation's isolated child environment has no `APP_ENV`. A new open-rails vendor-path test that a rails job or a sanity-run test executes must set `APP_ENV` itself. This unit adds no such test, so it is a stated hazard for the full seven-lane run, not a deliverable.
  - **O-19** (S19 record): `scripts/make_release_pack.sh` writes a non-canonical `artifacts/release_id.txt` that `scripts/hd_cli.py` reads as a release identity. It is outside P-7's bound ("Nothing else"). This unit changes neither script. O-19 stays with WU-DOC-01, its other named recipient, for documentation. Any code change is a later-change candidate for the Product Owner.
  - **Contract F-3** (production route exposure, from WU-PR-05): `adapter.factory` and `adapter.http_reader.create_app` serve 21 rules, and `adapter.wsgi` 23 (§5.3). ID-3's readiness content rests on it. This unit changes no route, so F-3 holds unchanged.
  - **Not carried:** addendum 2.10's `1.4.0` cut (contract F-1) and addendum 2.6's purity-report regeneration, both superseded for this unit (Plan delta 01 K-1 and K-2).
- **ID-8, document statements outside the bound** (recorded, not changed):
  - line 7 and line 8 list `/internal/version` twice;
  - line 20 says "open on localhost", which conflicts with C1's `127.0.0.1` convention, but is an access statement, not a port statement;
  - line 55's `ENGINE_ENV=dev|staging|prod` (the Audit's doc-delta candidate);
  - lines 145 to 150 give a production start line with a dependency-install prefix that `Procfile` lacks.

  These go to WU-DOC-01's owner through this IA as stale-document candidates. They are not edited here.

## 5. Current repository and reference baseline (measured at `67adb68`)

### 5.1 Repository state

`origin/main` `67adb68dcbf79928a2cb40e493cc288f272dd494`. Since WU-PR-07's merge, `main` has changed only `docs/ephemeral/` records and PF10 (v13.7.1). No code, test, CI or document file of this unit changed (`git diff --stat 7b763db 67adb68`: only `docs/ephemeral/`).

### 5.2 Files of the unit

- **`.env.example`** (3 lines): `HD_API_BASE_URL=https://api.example.invalid`, `HD_API_KEY=changeme`, `HD_API_SECRET=changeme`. No `GEO_API_KEY`. Nothing on `main` reads the file: no `.py`, `.sh`, `.yml`, `.toml`, `.json`, `requirements*.txt` or `Procfile` reference, and no dotenv loader. The only test hit is the S16 literal in a fixture of `tests/qa/test_generate_epic_close_pack.py` (line 4338).
- **`docs/ADAPTER_009.md`** (232 lines). The statements in scope are those of ID-2. It is not a governed evidence primary: it appears in neither `docs/evidence/INDEX.json` nor `artifacts/evidence_index.jsonl`, has no path proof, and is not in the classifier's 606 governed primaries. Frozen snapshots and hash lists name it (`codex/out/docs_meta_index.json`, `audit/docs_snapshot/`, `manifest_pre.sha256`, `manifest_post.sha256`, `handoff/…`). They are capture-time records; they are not refreshed and nothing reads them as current.
- **`ci/checks/classify_ci_changes.py`** (2,089 lines): see §5.4.

### 5.3 Code the statements must match

- **`adapter/wsgi.py`:**
  - `create_app()` registers `GET /internal/healthz` and `GET /internal/readyz` (lines 41 to 51). Both return `emit_public({"ok": True, "schema": "v1"})`, 200, through `_apply_common_headers`.
  - That header set is `Cache-Control: no-store`, the content type, `X-Adapter-Version`, `X-Engine-Tag`, `X-Release-Id`, `X-Content-Type-Options`, `Referrer-Policy` and `X-Frame-Options`, plus `Strict-Transport-Security` when `APP_ENV` or `ENGINE_ENV` is production-like.
  - No `X-Toggles-SHA`.
  - `adapter/app.py` exposes this app "For `flask --app adapter.app run`".
- **Served rules under `APP_ENV=prod`, closed rails** (contract F-3, re-measured):
  - `adapter.factory`: 21 rules, `/internal/` rules `/internal/dev/sampler` and `/internal/version` only;
  - `adapter.http_reader.create_app`: the same 21;
  - `adapter.wsgi`: 23 rules, adding `/internal/healthz` and `/internal/readyz`.
- **`Procfile`:** `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30`.
- **`adapter/http_reader.py` `__main__`** (lines 1316 to 1324): `create_app().run(host="127.0.0.1", port=int(os.environ.get("PORT", "8000")), debug=False, use_debugger=False, use_reloader=False)`, commented "loopback only, debugger and reloader off".
- **`scripts/dev_start_reader.sh`:** sets `PORT` to `8000` by default and runs `python -m adapter.http_reader`, printing "host=127.0.0.1".
- **`adapter/env_guard.py`** `validate_or_fail`: in prod mode, forbids the known override keys with `CANON_TOGGLES_OVERRIDE_IN_PROD`. `adapter/wsgi.py` calls it at app creation, not in the readyz handler.
- **`engine/providers/vendor_http_hdapi.py`:** requires `HD_API_KEY` and `GEO_API_KEY` (line 67).

### 5.4 Classifier and lanes

- `classify_paths(['.env.example'])` raises `CI_CHANGE_SURFACE_UNCLASSIFIED:.env.example`.
- `python tools/ci/prepush_check.py --path .env.example --path docs/ADAPTER_009.md --path ci/checks/classify_ci_changes.py lanes membership build-notes` at `67adb68` reports:
  - `lanes: FAILURE CI_CHANGE_CLASSIFIER_ERROR:CI_CHANGE_SURFACE_UNCLASSIFIED:.env.example`;
  - membership PASS, all three paths not members;
  - build-notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md`, sha256 `eab61385…`;
  - "repository unchanged".
- `ci/checks/classify_ci_changes.py` is in `_FULL_VALIDATION_PATHS`, so changing it selects all seven lanes.
- Plan delta 01 P-7 records a throwaway-clone rehearsal at `a78b350`. These files are byte-identical at `67adb68`. Adding `.env.example` to `_DOCUMENT_PATHS` and changing the three files gave classifier exit 0, `reason=selected_lanes`, all seven lanes and 166 changed-test targets. `.env.example` alone classified as `documentation_only`. In the same rehearsal, `tests/evidence/test_rails_ci_workflow_integration.py` ran 136 passed and 2 failed. Both failures reproduce identically on the unchanged base in that container, so they are environmental:
  - `test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned`: a `pytest --collect-only` subprocess exits 2;
  - `test_open_rails_producer_check_mode_has_no_repo_residue`: `OPEN_RAILS_ABBA_PREDICATES_FAILED`.

  PR-20 re-runs them in its own environment.
- **Existing mechanisms:**
  - `_DOCUMENT_PATHS` (`LICENSE`, `AcceptanceMap.md`, `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`; `documentation_only`);
  - `_WORKFLOW_CONTROL_PATH_LANES` (a path-to-lanes map).

  No test under `tests/`, `ci/` or `tools/` names `_DOCUMENT_PATHS`.

### 5.5 Release membership

Admitted release `1.3.0`, roster 45, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`. None of the unit's three paths is a member.

## 6. Bounded files and components

| Path | Change | Bound |
| :- | :- | :- |
| `.env.example` | Add one `GEO_API_KEY` placeholder entry | Nothing else in the file changes (acceptance 1). No secret value |
| `docs/ADAPTER_009.md` | Correct the readiness and port statements of ID-2 | No other statement changes (ID-8) |
| `ci/checks/classify_ci_changes.py` | One registration that classifies `.env.example` | The smallest existing mechanism (ID-4); no other classifier change |
| An owner or pin test | Only if one enumerates the changed registry (ID-5) | None does at `67adb68` |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-08-*` | The PR session's own records (plan, result records) | — |

**Expected unchanged:**
- `.github/workflows/*`;
- every release member, including `catalog/manifest.json` and `engine/config/registry_loader.py`;
- every governed evidence artifact (Index, Mirror, path proofs, sentinels);
- `requirements*.txt`, `pyproject.toml` and `Procfile`;
- `scripts/make_release_pack.sh` and `scripts/hd_cli.py` (O-19);
- `README.md`, `AGENTS.md`, `CHANGELOG.md` and the other WU-DOC-01 documents;
- `docs/pfcanon/`.

## 7. Exclusions

- No release cut or manifest refresh (Specification delta 01, C-5); no admission-constant change.
- No CI workflow change (P-7 Nonclaims).
- No S01 work: packaging and wheel layout are removed (Specification delta 01, C-1 and C-6).
- No route, payload, flag or transport change; no change to `/internal/readyz`'s behavior. The document follows the code, not the reverse.
- No WU-DOC-01 document (ID-8), no O-19 code change (ID-7).
- No canon change, no PF10 addendum, no QA artifact, no Ops act, no deployment.

## 8. Interface contracts with other units

- **WU-DOC-01** receives ID-8's out-of-bound statements and O-19's documentation side through this IA's PR-40.
- **WU-OPS-01** relies on `release_id` being unchanged by this unit (ID-6).
- **QA-10** reads S16 and S17 as not production-affecting.

## 9. Disposition rules PR-20 must apply and record

1. **Choices left to PR-20,** each recorded with its reason:
   - the registration's form (ID-4);
   - whether any owner or pin test changes (ID-5);
   - the corrected wording of each ID-2 statement (ID-3).
2. **Real-input set** (addendum 2.11 rule 4): the inputs that matter are the three files at the PR head, the code of §5.3 and the hosted CI run. Every statement in the document cites something that exists on `main`. No test models an input that does not.
3. **Prototype** in a throwaway copy:
   - apply the three changes;
   - run the classifier as `ci.yml` calls it with full SHAs, and on `.env.example` alone;
   - run admission and `tools/ci/prepush_check.py lanes membership` for the three paths;
   - record each command, exit status and the copy's state before and after.
4. **Baseline re-check.** Re-measure §5.2 to §5.5 at the plan's head, and record any difference before planning edits.
5. **Statement map.** A table from each ID-2 statement to its corrected text and the code line it matches (§5.3). This is the measure PR-40 checks.
6. **Carried items.** Record ID-7's dispositions and ID-8's list.

## 10. Acceptance, tests and evidence

Acceptance is P-7's (1) to (5), verbatim:
1. "`.env.example` has a `GEO_API_KEY` entry and nothing else in it changed."
2. "The readiness section describes `/internal/readyz` as implemented and names the app that serves it. The port statements match the runner and Procfile bindings."
3. "Admission at the PR head reports `1.3.0`, 45 members and the base head's `release_id`, unchanged."
4. "At the PR head, the classifier run on `.env.example` alone returns a classification and no `CI_CHANGE_SURFACE_UNCLASSIFIED`."
5. "All seven lanes are green on the exact PR head, with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`."

Read with ID-2: acceptance (2) covers every readiness and port statement of ID-2, including lines 6, 22 and 33, not only the "Readiness rules" section.

**Tests.**
- No new test is required (Audit §6 S16 and S17: "no test is proportionate").
- The classifier's existing tests run in the full lane set.
- PR-20 runs `tests/evidence/test_rails_ci_workflow_integration.py` and the classifier-owned tests at its head. It records the two environmental failures of §5.4 if they recur, with their base comparison.

**Evidence.** The PR result record names:
- every check run, with its counts;
- the statement map (§9.5);
- the classifier output for `.env.example` alone;
- admission's `release_id`;
- the current-head CI run with all seven lanes.

## 11. Migration and security constraints

- **Migration:** none.
- **Rollback:** Nathan's revert of the squash commit. No member changes, so no refresh.
- **Security** (addendum 2.3: the Codex code review is in the chain, the Codex security review is not):
  - `.env.example` carries a placeholder (`changeme`, as the file's other keys do), never a real key;
  - no secret, token or key value in any record, test or commit (`AGENTS.md` redaction rule);
  - closed rails for every local run.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated PR session):
  - reads this instruction and its lineage, P-7 in full, the three files, §5.3's code and canon on `main`;
  - re-checks the baseline (§9.4) and prototypes (§9.3);
  - writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/` with the §9 records;
  - returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.
- **PR-30** (after Nathan's Proceed for that exact plan, against the business case):
  - recovers existing work first;
  - implements only the planned files;
  - runs the prototype checks on the real branch;
  - commits coherently;
  - publishes `PR_CANDIDATE_PUBLISHED`;
  - hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session):
  - retrieves and dispositions the Codex code review findings under addendum 2.11 rule 7 and addendum 2.14. A P1 on a real input is fixed; a decline of a P1 or a security finding goes to the Product Owner first;
  - applies rule 8 on a repeated finding class;
  - verifies current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability. A failure that is red on the base too is handled as base-red, not by widening the unit (P-7 Risks);
  - returns `MERGE_PENDING` without merging.
- **PR description:** the `.github/pull_request_template.md` headings, with the `AGENTS.md` content rules.
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage. It checks the measure, that each corrected statement matches the code on the merged head, and records whether it was met (addendum 2.18 rule 5). On ACCEPT it selects the next unit, WU-DOC-01 through DOC-10, whose business case the Product Owner states first.
- **Nonclaims** every record keeps: no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release cut.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect existing worktrees, branches, PRs and `docs/ephemeral/` before creating anything.
- **Prototype:** it runs only in throwaway copies. Discard and re-clone on failure.
- **An ordinary defect in this instruction** returns to this IA through PR-10. A corrected instruction is a new version.
- **Abort** is only Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material:** a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or scope or risk needing Product Owner direction. A planned approach found incomplete or inferior is not by itself material.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional support; RS-30 for revisions), and this IA reviews it through RS-20.
- **After Proceed:** PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Expected triggers:**
  - a needed change in an expected-unchanged path of §6, such as a workflow, a member, a WU-DOC-01 document or an O-19 script;
  - a finding that `/internal/readyz`'s behavior, rather than the document, should change;
  - rule 8's design question.
- **Not a trigger:** a §9.1 choice; adding the scenario-table row of ID-5 as a recorded plan choice.

## 15. Unresolved items, carried observations and owners

| Item | Owner | State |
| :- | :- | :- |
| The choices of §9.1 | PR-20 session | In the plan |
| Loopback bind statements (2.7 to 2.9) | this unit (ID-7) | Met by ID-3's port content |
| OBS-P4-5 | this unit, as a hazard (ID-7) | No test of that kind added |
| O-19 | WU-DOC-01 (documentation) through this IA; the Product Owner for any code change | Not this unit |
| F-3 | this unit (ID-7) | 21 / 21 / 23 rules; unchanged |
| ID-8's out-of-bound statements | WU-DOC-01 through this IA | Recorded |
| Business cases for WU-DOC-01 and WU-OPS-01 | Product Owner | Due before DOC-10 and OPS-10 |
| Glow Infrastructure doc-delta: the deploy source | Product Owner | Carried (Plan delta 01 P-18) |
| PF10 number of the Specification delta 01 addendum; addendum 2.11's cross-references | Product Owner | Carried |
| OBS-P4-7 (`ENGINE_ENV` leak in `tests/adapter/test_jsonschema.py`) | a later unit through this IA | A full-lane hazard here: that test calls `/internal/readyz` |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

**No new conflict.**
- C1's `127.0.0.1` convention and the production `0.0.0.0:$PORT` bind are consistent, because canon says the convention never renames the server bind.
- The document's stale readiness claims are documentation drift, not canon. No PF document specifies `/internal/readyz`'s rules. `docs/ENDPOINTS_CATALOG.json` and the A7 catalog row list `/internal/readyz` on `adapter.wsgi` as a readiness probe, which is consistent with §5.3.

**Coverage read for this instruction:**
- Change Process Guide §0.6.1 (the access-address and infra-fact bullets);
- PF10 addenda 2.18 and 2.19 (the Plan delta's addendum record) in full, 2.11 rules 1 to 8 in full, 2.14 rules 1 to 6 in full, 2.3 rules 1 to 5 in full, and 2.7, 2.8, 2.9 and 2.10 at their WU-PR-08 items;
- the Specification delta 01 addendum, from its record;
- Plan Templates "CI lane classification and automated budget-control discipline", read in full in this session;
- `AGENTS.md` "HDE-EPIC039 current workflow posture", "Release identity" and "HDE-EPIC040 current posture".

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Unit | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S16 "`.env.example` has a `GEO_API_KEY` entry" | one placeholder key the vendor provider requires | §6; §11 placeholder | WU-PR-08 | (1) | PR-30; PR-40 |
| S17 "readiness rules describe what `/internal/readyz` does" | every readiness statement matches the handler | ID-2; ID-3 | WU-PR-08 | (2) | PR-30; PR-40 (measure) |
| S17 "port statements are current" | the runner's and Procfile's binds; `127.0.0.1` client host | ID-3; C1 | WU-PR-08 | (2) | PR-30; PR-40 |
| P-7 "one classifier registration" | CI accepts a change to `.env.example`, smallest existing mechanism | ID-4; ID-5 | WU-PR-08 | (4), (5) | PR-20; CI |
| P-7 "No release member changes" | no refresh; `release_id` unchanged | ID-6 | WU-PR-08 | (3) | PR-30 |
| P-7 Inputs (2.7 to 2.10 items) | each carried item disposed | ID-7 | WU-PR-08 | — | PR-20; PR-40 |
| Decision record §2 measure | each corrected statement matches the code on the merged head | ID-1; §9.5 | WU-PR-08 | — | PR-40 |
| Addendum 2.18 | no ceiling, no spend recording | ID-1 | WU-PR-08 | — | all phases |
| Addenda 2.11 rules 4 to 8, 2.14 | real inputs; dispositions; P1 | §9.2; §12 | WU-PR-08 | — | PR-20 to PR-35 |

**Checks against the full PR-20 contract:**
- Its sole substantive input is `PR_INSTRUCTION_ID`.
- This instruction carries the Specification, delta, Audit, Plan, delta and review lineage; the PF10 path and overlays; the business case; the baseline, loci, exclusions, interfaces and dependencies; acceptance, evidence, migration and security; recovery, rescope, merge ownership and the return owner.
- PR-20 plans without mutating the repository. Its prototype runs in a throwaway copy, and it writes only its own artifacts.
- There are no numeric domains, sentinels or closed schemas in this unit. The classifier's lane flags are booleans selected by the classifier, and the instruction sets none.
- No decisive comparison fails. Every fact in §5 was measured at `67adb68` by this IA, except the rehearsal, which P-7 records at `a78b350` on byte-identical files.

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated top-level WU-PR-08 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Return to the IA:**
  - PR-40 lineage review after Nathan's merge;
  - rescope review through RS-20;
  - same-owner correction of this instruction through PR-10.

## 19. TypeSafe reading for the receiving session (PR-20, WU-PR-08)

Action sent (v8.2): "Write, in a new dedicated session, the first detailed PR implementation plan, not yet reviewed, for one small work unit of an approved change: add one placeholder key to a three-line environment template, correct about eight readiness and port statements in one 230-line operator document against code the instruction has already measured, and add one entry to an existing set in a 2,100-line CI change classifier so the template is a classified path, which makes the pull request run all seven CI lanes. A ready instruction lists the files, the measured facts, the acceptance criteria and the carried observations; the plan re-checks them at its head, prototypes the change in a throwaway copy and states the classifier registration's form. No live run against a provider occurs; a Product Owner Proceed, implementation, CI with an independent code review, and a lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.78 (confidence 0.79); rung probabilities low 0.01, medium 0.25, high 0.70, extra high 0.04, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.76, Sonnet 5.5 0.23, Haiku 5.5 0.00 (confidence 0.68). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.003, Fable 5.1 at high 0.007, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.008, Opus 5.5 at medium 0.190, Opus 5.5 at high 0.532, Opus 5.5 at extra high 0.030, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.002, Sonnet 5.5 at medium 0.058, Sonnet 5.5 at high 0.161, Sonnet 5.5 at extra high 0.009, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-21T20:54:51Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-21T20:54:51Z; HTTP 200 in 0.65 s; 5515 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Which request.** The installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records.** The Notion row was not written (PR-10 handoff rule). Nathan's pick for PR-20 is not stated. Nathan's pick for this PR-10 session is not stated; its reading is in the Plan delta 01 review v1.1 §7.

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment:**
  - Python 3.12 with CI's install (`pip install -r requirements-dev.txt` and `requirements.txt`), git and bash;
  - closed rails, with the vendor, database and GitHub keys the container sets left unset;
  - throwaway clones for the prototype.
- **Run times observed:** the classifier: a few seconds. `tests/evidence/test_rails_ci_workflow_integration.py`: about 30 s. A full hosted seven-lane run: about 20 minutes.
- **Access:** no live vendor, production or database access is needed.
- **Order:** this instruction's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-08 / PR-10 / instruction 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| work unit | WU-PR-08 (S16, S17) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state of 2026-10-12T02:29:33.739Z). Receiver contract read: PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state of 2026-10-12T02:29:47.327Z), Inputs and Execute |
| role/stage | continuing whole-change IA / PR-10 |
| capture time | 2026-10-21T20:58:37Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| inherited usage | the Plan delta 01 review v1.1 (Isis, https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok) and the WU-PR-08 decision record (Isis, https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2) |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `67adb68`. `docs/pfcanon/` was last changed by `7b763db` (PF10 v13.7.1); every other PF file is unchanged.

| Topic | Sources and sections |
| :- | :- |
| PR-10 operation, readiness and handoff | PR-10 — Create PR Work-Unit Instructions — 100926.1, read in full: "Execute" 1 to 8; "Semantic readiness before INSTRUCTION_READY"; "Required result"; "INSTRUCTION_READY → PR-20"; "Mandatory single-block handoff" |
| Receiver contract | PR-20 — Create Detailed PR Implementation Plan — 100926.1: "Inputs" (`PR_INSTRUCTION_ID` sole input) and "Execute" 1 to 10, read in full |
| Unit scope | Plan delta 01 v1.1 P-7 and its addendum record (2.19), read in full; the delta's approval review v1.1, read in full; Plan v1.1 §3, §7 common terms and §9, read in full for the delta work in this session |
| Requirements | Specification v1.1 S16 and S17 rows and the Live QA class table; Specification delta 01 C-1, C-5 to C-7 and C-10 (from its addendum record, read in full); Audit §6 S16 and S17, read in full |
| Business case | Decision record §1 to §3, read in full; PF10 addendum 2.18, read in full; addendum 2.11 rules 1 to 8, read in full |
| P1 and dispositions | PF10 addendum 2.14 rules 1 to 6, read in full |
| Reviewer chain | PF10 addendum 2.3 rules 1 to 5, read in full |
| Carried items | PF10 addenda 2.7 ("Affected surfaces", WU-PR-08 bullet), 2.8 (the loopback carry), 2.9 (the OBS-P4 table and the carried-for-later bullet), 2.10 (F-3 and the carried-for-later bullet), read at those passages; the S19 record's O-19 row; WU-PR-04 plan's OBS-P4-5 row; WU-PR-05 plan's F-3 definition |
| Dev access address | PF06-Canon-Change-Process-Guide v2.5.4 §0.6.1, the infra-fact and access-address bullets, read in full |
| CI design | PF27-Canon-Plan-Templates v2.0.5 "CI lane classification and automated budget-control discipline", read in full in this session |
| CI, release identity | `AGENTS.md` "HDE-EPIC039 current workflow posture", "Release identity", "HDE-EPIC040 current posture" |
| Authority, Proceed, merge | PF04-Canon-HDE-Governance v2.8.7 §9.1.1 and §9.1.2, as Plan v1.1 cites them; not re-read in this session |

**Repository read at `67adb68`:**
- `.env.example`;
- `docs/ADAPTER_009.md` lines 1 to 58 and 112 to 152;
- `adapter/wsgi.py` in full;
- `adapter/app.py`;
- `adapter/factory.py` (its routes);
- `adapter/http_reader.py` `__main__`;
- `scripts/dev_start_reader.sh`;
- `adapter/env_guard.py` `validate_or_fail`;
- `Procfile`;
- `ci/checks/classify_ci_changes.py` (the sets and `_lanes_for_path`);
- `tests/evidence/test_rails_ci_workflow_integration.py` (the scenario table);
- `tools/ci/prepush_check.py` (run);
- the served-rule sets of the three factories (run).
