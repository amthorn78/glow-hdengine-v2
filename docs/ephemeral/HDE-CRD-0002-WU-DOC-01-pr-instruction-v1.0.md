---
artifact_type: PR_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-DOC-01-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
DOCUMENTATION_UNIT_ID: WU-DOC-01
work_unit_title: "Final repository documentation (DOC; after WU-PR-08)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_overlays: (1) Specification delta 01 (DELTA_APPROVE), PF10 addendum 2.20; (2) Implementation Plan delta 01 v1.1 (DELTA_APPROVE), PF10 addendum 2.19, whose P-8 sets this unit's bounded scope and whose summary drops the dedicated-environment install note; (3) PF10 addendum 2.21, which routes the stale-document list (LR8-F2, LR8-O1 and the earlier carried items) to this unit; (4) PF10 addendum 2.17, which this unit's writer usage note reads with the S21 ADR
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (blob 9408d6ed091b), approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md (blob 5a6cecc86f60)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44) §7 WU-DOC-01, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1; blob 5103fe29d588) P-8
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE; blob 4801c7cc2c9d)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276db)
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md §2 (Product Owner adoption, 2026-10-22; blob 28b3deb24cb9; landed by #689)
predecessor_unit_acceptance: WU-PR-08 accepted by docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-work-unit-lineage-review-v1.0.md (ACCEPT on #687; blob 0d841d3fd24e; PF10 addendum 2.21)
prior_instruction_lineage: none for WU-DOC-01 (first instruction). Structure precedent: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-instruction-v1.0.md
ops_evidence: none exists. WU-OPS-01 follows this unit in the Plan order and needs its own business case before OPS-10
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (blob 1343ae09018e; 433,368 bytes; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff)
pf10_addendum_created: none (DOC-10 is not an addendum producer)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
prompt: DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb81ce99b1d2ade30c572f; page state of 2026-10-12T02:29:24.131Z, read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-22T01:14:05Z
repository_baseline: origin/main 6f2478febc1355010de3ecc27b06c7fce4ce4df1 (#689). Every repository fact in §5 and §6 was measured at this head under closed rails (env -i; SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC), CPython 3.12.3
receiver: dedicated HDE-CRD-0002 WU-DOC-01 PR engineering session (initial dedicated assignment; created by Nathan / Product Owner)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state of 2026-10-12T02:29:47.327Z; Inputs and Execute read in this invocation)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§16)
---

# HDE-CRD-0002 WU-DOC-01 — Final repository documentation PR instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one PR instruction for HDE-CRD-0002's final repository-documentation unit, WU-DOC-01. A dedicated PR-20 session can plan the unit from this instruction and the linked repository and canon.

- **The work:** bring eleven repository Markdown documents to the delivered state of HDE-CRD-0002. That is 36 items, listed in §6, each with its current statement, the measured fact and its source.
- **What it does not do:** it changes no code, test, workflow, schema, canon, governed evidence or release member.
- **CI:** every path in scope is classified `documentation_only`. The hosted `test` job starts, runs no lane and ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. So the tests that read these documents run only locally (§10).

This instruction is not the documentation. It authorizes no implementation, publication, merge, QA, Ops, acceptance or closure.

## 2. Identity and lineage

| Field | Value |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Unit | WU-DOC-01, Plan v1.1 §7 "Final repository documentation (DOC; after WU-PR-08)" |
| Bounded scope (P-8, verbatim) | `README.md` (pre-push check usage; close-pack writer capability; test guidance); `CHANGELOG.md`; `AGENTS.md` operative passages (HDE-EPIC039 workflow posture → the extended close-pack capability and schema v2; HDE-EPIC040 current posture → release `1.3.0`, refreshed in place with no version cut, and its current `release_id`; the CI-exempt paths note verified against the workflow; pytest guidance); `docs/EVIDENCE_INDEX.md` (CRD admission, Mirror labels, close-run family); `docs/CLI_commands.md` final pass; `docs/server/reader_v1.md` (not-found limitation line removed). No canon, no generated evidence, no governed artifact by hand. |
| Routed items | The stale-document list that PF10 addendum 2.21 routes here ("The stale-document list (LR8-F2, LR8-O1 and the earlier carried items) goes to WU-DOC-01"), resolved in §6. The business case record §2 names them as covered ("as the DOC-10 instruction resolves them") |
| Acceptance (Plan v1.1 §7, unchanged by P-8) | "Each statement traces to a merged unit; `tests/unit/test_check_agents_md_citations.py` passes; DOC-20 verifies completion." |
| Nonclaims (Plan v1.1 §7) | "Documentation completion establishes no QA, acceptance or closure." |
| Business case | Beneficiary: agents and operators who take repository workflow from `AGENTS.md` and `README.md`. Measure: "Each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20". No ceiling (addendum 2.18) |
| Merged units documented | WU-PR-01 #627, #630; WU-PR-02 #634, #637; WU-PR-03 #643, #646; WU-PR-04 #651; WU-PR-05 #656; WU-PR-06 #660; WU-PR-07 #668; WU-PR-08 #687. Each was accepted by its PR-40 lineage review (addenda 2.4, 2.5, 2.8, 2.9, 2.10, 2.12, 2.16, 2.21) |

## 3. Unit selection and dependency state

- **Order** (Plan v1.1 §7 as delta 01 keeps it): WU-PR-08 → **WU-DOC-01** → WU-OPS-01 → QA-10.
- **Dependency** "Ninth; after WU-PR-08 merges": met. #687 merged as `1a4c8ab`, and the lineage review accepted it.
- **Business-case prerequisite** (addendum 2.18, "Epic, task, and status effects"): met by the disposition record (#689, `6f2478f`).
- **Stage:** a final documentation unit with no instruction goes to DOC-10, and DOC-10 hands off to PR-20.
- **This is the only documentation unit** (Plan v1.1 §8 "Final repository documentation work": "WU-DOC-01 (§7) is the only documentation unit").
- **No Ops evidence exists**, and none is needed: WU-OPS-01 follows this unit, and §7 excludes Ops facts from its documents.

## 4. Requirement-to-documentation mapping

Every approved requirement, mapped to its delivered evidence and the documentation change it needs. "No change" means the delivered documentation is already current at the baseline, or the requirement has no operative-document obligation.

| Req. | Delivered by (merged) | Delivered fact (observed at `6f2478f`) | Documentation change (§6 item) |
| :- | :- | :- | :- |
| S01 | removed (Specification delta 01) | not delivered; the wheel still omits members, and README states it (line 132) | none. The README limitation stays accurate. No dedicated-environment install note (P-8; addendum 2.19) |
| S02 | WU-PR-03 #643 | every app factory answers an unknown path with the JSON `ERR_NOT_FOUND` envelope (probed: `adapter.factory`, `adapter.http_reader` and `adapter.wsgi`, `GET /api/reader/missing` → 404 `application/json`) | K-1 (`docs/contracts/reader_v2_public_bytes.md` line 19); V-1 (`docs/server/reader_v1.md`, confirm only); CH-1 |
| S03, S04, S05 | WU-PR-01 #627, #630 | every tracked test file reaches a lane, or is retired in `tests/retired_tests.md`; the workflow's skip list matches the classifier's prefixes | R-4 (test guidance, including line 218); U-2; F-1; CH-1 |
| S06 | WU-PR-02 #634, #637 | the attestation builder works under a distribution-patched setuptools (WU-PR-02 plan v1.0 PD-1) | R-7 (OBS-W2-2); CH-1 |
| S07 | WU-PR-03 #643 | `hdctl --help` describes showcompat's `magic10_compat_result.v1` output | L-1 (CLI final pass); CH-1 |
| S08 | WU-PR-04 #651 | `aux-preview --band` applies to pair-file input | L-1; CH-1 |
| S09 | WU-PR-03 #643 | `dev/reader_harness/app.py` retired (deleted in `c98d41f`) | CH-1 (records the retirement; the historical CHANGELOG entry at line 333 is left as history); P-1 (A7 crib) |
| S10 | WU-PR-03 #643, #646 | dev `GET /reader` is served only when `APP_ENV` is exactly `dev` (addendum 2.7 AD-2); the runner binds `127.0.0.1` on `$PORT`, default 8000 (`adapter/http_reader.py:1319-1320`; AD-3) | R-5; A-5; U-1; D-5; CH-1 |
| S11, S12, S13 | WU-PR-02 #634, #637 | the engine-core currency test checks `release_id`; current-release captures carry a release label in Mirror `notes` (IF-7, `CURRENT_RELEASE_CAPTURE_PATHS`); the admission probe is isolated | E-2 (Mirror labels; OBS-W2-1); CH-1 |
| S14 | WU-PR-04 #651 | `--allow-prod-vendor` per HDE-CLI-API-Vendor-Ref §7.1.11; vendor resolution needs a recognized `APP_ENV`, or `ENGINE_ENV` when `APP_ENV` is blank (`docs/CLI_commands.md` line 21 already states it) | L-1; X-1 (runnable `bg:resolve --source vendor` commands state an explicit recognized `APP_ENV`); CH-1 |
| S15 | WU-PR-03 #643, #646 | the Endpoint Catalog matches the served routes; three canon-retired routes stay mounted but uncatalogued (addendum 2.7 AD-1) | CH-1 |
| S16, S17 | WU-PR-08 #687 | `.env.example` has `GEO_API_KEY`; `docs/ADAPTER_009.md` readiness and port statements are corrected | D-1 to D-8 (LR8-F2, outside S17's bound); CH-1 |
| S18 | WU-PR-03 #643 | `docs/ADAPTER_009.md` states `invalid_json` for a compat GET with a body | CH-1 |
| S19 | WU-PR-05 #656 | `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` recorded; its fixes landed or routed | R-6 (O-19's documentation side); CH-1 |
| S20 | WU-PR-06 #660 | `tools/ci/prepush_check.py`, with five read-only reports (help measured, §5.3) | R-2 (usage note, G-1); A-7; CH-1 |
| S21 | WU-PR-07 #668 | `schemas/close_candidate_source.v2.json` and `tools/qa/generate_epic_close_pack.py` for Epic and CRD identities; the close-run family; ADR `docs/adr/hde/close_pack_writer_adr.md` (blob fcaa9da66fb7) | R-3 (H-4); A-1; E-3; Q-1; CH-1 |
| S22 | WU-PR-02 #634, #637 | `ADMITTED_CRD_QA` in `tools/evidence/update_evidence_index.py` admits HDE-CRD-0001 and HDE-CRD-0002 | E-1; Q-1; CH-1 |
| Release (delta 01) | WU-PR-03, WU-PR-04, WU-PR-05 refreshes | `1.3.0`, 45 members, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (computed from `catalog/manifest.json`; matches the `membership` report) | R-1; A-2; CH-1 |

## 5. Current repository and reference baseline (measured at `6f2478f`)

### 5.1 Repository state

- `origin/main` is `6f2478f` (#689). The branch `docs/20261022-hde-crd-0002-wu-doc-01-instruction` carries only this instruction.
- No §6 document, and not `docs/INDEX.md`, changed between `1a4c8ab` (#687's merge) and `6f2478f` (`git diff --stat` is empty).

### 5.2 The documents

| Document | Lines | Governed? | Release member? | Read by tests or tools |
| :- | -: | :- | :- | :- |
| `README.md` | 222 | no Index/Mirror row, no path proof | no | `ci/checks/classify_ci_changes.py`, `tests/bodygraph/test_check_magic10_gate_readiness.py`, `tests/evidence/test_rails_ci_workflow_integration.py`, `tools/bodygraph/check_magic10_gate_readiness.py` |
| `AGENTS.md` | 222 | no | no | `ci/checks/check_agents_md_citations.py`, `ci/checks/check_direct_db_contract.py`, `ci/checks/classify_ci_changes.py` |
| `CHANGELOG.md` | 518 | no | no | `ci/checks/check_direct_db_contract.py`, `ci/checks/classify_ci_changes.py` |
| `docs/EVIDENCE_INDEX.md` | 447 | no | no | `tests/unit/test_check_direct_db_contract.py` |
| `docs/CLI_commands.md` | 84 | no | no | `tests/cli/test_cli_usage_and_errors.py` |
| `docs/server/reader_v1.md` | 225 | no | no | none found |
| `docs/RUN.md` | 102 | no | no | `tests/unit/test_check_direct_db_contract.py` |
| `docs/ADAPTER_009.md` | 229 | no | no | `tests/qa/test_generate_epic_close_pack.py` |
| `docs/qa_harness_pattern.md` | 112 | no | no | none found |
| `docs/contracts/reader_v2_public_bytes.md` | 66 | no | no | none found |
| `docs/acceptance/reader_a7_crib.md` | 21 | no | no | `tests/qa/test_generate_epic_close_pack.py` |

"Read by" comes from `git grep` over `tests/`, `ci/` and `tools/`. PR-20 confirms each consumer's assertion, because a reworded line can break one. `docs/INDEX.md` enters only through item X-1.

### 5.3 Delivered tools (help and behaviour measured)

- **`python tools/ci/prepush_check.py --help`**, exit 0:
  - reports `lanes`, `membership`, `build-notes`, `sweep`, `replay` and `all`;
  - options `--base` (default `origin/main`), `--head` (default `HEAD`), `--event {pull_request,push}`, `--path` (repeatable), `--full` and `--no-run`;
  - the help states its own limits: refuses a dirty tree; committed revisions only; no network; children not sandboxed; its green is not CI's green and not QA; its output is not governed evidence.
- **`lanes` on the eleven documents:** `reason=documentation_only`, all seven lanes false. `membership`: all eleven are not members of `1.3.0` (45 members). `build-notes`: `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md`, sha256 `8ac97232…6d37ff`.
- **`python tools/qa/generate_epic_close_pack.py`:** usage `--source SOURCE (--write | --check)`, and it refuses without `--source`.
- **The close-pack schemas:** `schemas/close_candidate_source.v2.json` and `schemas/epic_close_candidate_source.v1.json` both exist.
- **The updater:** `ADMITTED_CRD_QA = {HDE-CRD-0001: (audit/qa/hde-crd-0001, audit.qa.hde_crd_0001), HDE-CRD-0002: (audit/qa/hde-crd-0002, audit.qa.hde_crd_0002)}` (`tools/evidence/update_evidence_index.py:51-54`). It also has `CURRENT_RELEASE_CAPTURE_PATHS` (IF-7, from line 62) and `publish_crd_close_run_family` (line 5222).
- **The A7 proof writer** is `tools/evidence/generate_a7_transport_proofs.py`:
  - writing needs `HDE_WRITE_A7_PROOFS=1` (line 176); `--check` exists;
  - `PROOFS` (line 31) lists `endpoints_env_gate_proof.log`, `success_get.txt`, `success_head.txt`, `success_304.txt`, `success_writers_errors.txt`, `success_encoding_invariance.txt` and `reader_success_get_head_304.json`;
  - its test is `tests/transport/test_a7_transport_proofs.py`, which asserts that `artifacts/proofs/encoding_invariance.txt` is absent;
  - `tests/http/test_reader_a7_transport.py` does not read `HDE_WRITE_A7_PROOFS`.
- **`/internal/version`** (`adapter/http_reader.py:1175`):
  - no authorization check;
  - an `X-Identity-Override` header returns 400;
  - `Cache-Control: no-store` and no ETag.
- **Other runtime facts:**
  - no source under `adapter/` or `engine/` reads `ENGINE_SERVICE_TOKEN` or `TOGGLES_SHA`;
  - `X-Release-Id` is set only by `adapter/wsgi.py`, whose `RELEASE_ID` defaults to `rel_dev` (lines 15 and 32);
  - `ENGINE_ENV` is read only as a fallback when `APP_ENV` is blank (`adapter/wsgi.py:36`, `adapter/env_guard.py:46`, `engine/bodygraph/resolver.py`).
- **`Procfile`:** `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30`.

### 5.4 CI path for this unit

- **The workflow filter** (`.github/workflows/ci.yml`, `pull_request.paths`) includes `**`, excludes the eight storage prefixes, and re-includes `**.path_proof.txt`, `docs/run/EPIC011_TEST_IDENTITIES.md` and `docs/run/PROD_ENDPOINTS.json`. A change to any §6 document therefore starts the `test` job.
- **What the job then does:**
  - the classifier gives `documentation_only` (`ci/checks/classify_ci_changes.py:1908`);
  - `needs_python=false`, so setup, install and pytest are skipped;
  - the job checks the clean tree and prints `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (`ci.yml:420`).
- **The `lanes` report's note** says "reason=documentation_only means the workflow's path filter starts no hosted run". That is not true for these paths (DOC10-O1, §15).
- **Codex code review:** `AGENTS.md` "Code review guidelines" exclude Markdown. A change made only of Markdown files outside the storage prefixes is outside Codex's review scope, so no Codex finding is expected. Codex security review is deprecated (addendum 2.3).

### 5.5 Local baseline of the document-reading tests

Run at `6f2478f` with a venv holding `requirements.txt` and `requirements-dev.txt` but not `-e .`. The run used `env -i PATH=/usr/bin:/bin HOME=/tmp`, closed rails.

The tests run:
- `tests/unit/test_check_agents_md_citations.py`;
- `tests/unit/test_check_direct_db_contract.py`;
- `tests/bodygraph/test_check_magic10_gate_readiness.py`;
- `tests/evidence/test_rails_ci_workflow_integration.py`;
- `tests/cli/test_cli_usage_and_errors.py`;
- `tests/qa/test_generate_epic_close_pack.py`.

Results:
- **1,243 passed, 5 failed.**
- All five failures are in `tests/cli/test_cli_usage_and_errors.py`. Each is `FileNotFoundError: 'hdctl'`, because the console script exists only after CI's `-e .` install.
- `tests/unit/test_check_agents_md_citations.py` alone: **57 passed**.

These five failures are environmental (DOC10-F2), not baseline defects. PR-30 runs the set with CI's full install (§10).

## 6. Bounded documents and items

Line numbers are at `6f2478f`. "Fact" is what this IA measured (§5), unless it is marked "PR-20 measures". **Required change** states what the text must say, not its wording; PR-20 drafts the exact text.

### 6.1 `README.md`

| ID | Line | Current statement | Fact and source | Required change |
| :- | -: | :- | :- | :- |
| R-1 | 13 | release `1.3.0`, `release_id` `52be4558…` | current `release_id` `77204764c225…c51e`; the release is refreshed in place with no version cut (LR3-O4; F-10; P-8) | the current `release_id` and "refreshed in place". The surrounding HDE-EPIC040 context stays |
| R-2 | new | the README has no pre-push check | §5.3; G-1; LR6-O5; LR6-O7 | a usage note for `tools/ci/prepush_check.py`, covering: <br>• the reports and options; <br>• that it is read-only and acts on committed revisions; <br>• the limits LR6-O7 lists: the replay runs only the pinned `ci.yml`; the install step is checked for presence only; runner defaults are not given to scripts; directories under `.git` are compared by name; concurrent git activity fails the read-only check; children are not sandboxed; a shallow source holds ref-reachable history only; it needs CI's install, Python 3.12, `ruby`, `bash` and `curl`; <br>• LR6-O5: any `ci.yml` change needs `REPLAY_WORKFLOW_SHA256` updated, or the replay refuses; <br>• the nonclaim: its result is not CI's result, not QA and not governed evidence. <br>It does not repeat DOC10-O1's note |
| R-3 | 25 (and the HDE-EPIC039 block) | "The epic-agnostic closeout-candidate capability is defined by `schemas/epic_close_candidate_source.v1.json`, …" | v2 delivered (S21; H-4) | the line stays the HDE-EPIC039 record. A current statement adds the writer's usage and posture (H-4): <br>• the v2 schema `schemas/close_candidate_source.v2.json`; <br>• Epic and CRD identities; <br>• the outputs `audit/EPIC-<NNN>_close_report.md` and `_MANIFEST.json` and the CRD equivalents (PR-20 measures their names); <br>• the writer's nonclaims, as the WU-PR-07 PR result record states them; <br>• the ADR's stated limits, read with PF10 addendum 2.17 (resolution A on TOOLING_BLOCKED under a closure override; resolution B: v2 supports only the ADR-status form of a tracked issue). <br>No statement may present v1 as the only schema |
| R-4 | 102, 213, 218 and "Testing (minimal)" | line 102: the A7 proof gate "defined in `tests/http/test_reader_a7_transport.py`"; line 218: `tests/qa/test_epic022_acceptance_scaffold.py` | the writer is `tools/evidence/generate_a7_transport_proofs.py` (§5.3); the scaffold test was retired (`tests/retired_tests.md` line 63; O-4); every test file reaches a lane or is retired (S03) | line 102: name the writer, its `HDE_WRITE_A7_PROOFS=1` write gate and `--check`. Line 218: remove the retired test. Add one statement of the S03 rule and the retirement register's path. Line 213 stays (the file exists and tests the transport) |
| R-5 | 159 | "Dev Reader helper (`scripts/dev_start_reader.sh`) remains available …; APP_ENV gating applies." | start command `APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC PORT=8000 scripts/dev_start_reader.sh` (as `docs/CLI_commands.md` line 78 states); `GET /reader` needs `APP_ENV` exactly `dev`; the runner binds `127.0.0.1` on `$PORT`, default 8000 (OBS-P3-8; AD-2; AD-3) | state the start command and the loopback bind |
| R-6 | "Release identity" (lines 128 to 137) | no statement about `artifacts/release_id.txt` | `scripts/make_release_pack.sh` writes `artifacts/release_id.txt` (`8ca9ba71…`), which `scripts/hd_cli.py` reads; it is not the canonical `release_id` (O-19; LR8-O1) | one sentence: that file is not the release identity; the identity is `sha256(canonical_bytes(catalog/manifest.json))`. The code change is the Product Owner's (§15) |
| R-7 | 135 (attestation) | no statement about building off CI | the wheel stage supplies a builder-owned compatibility module under a distribution-patched setuptools (S06; WU-PR-02 plan v1.0 PD-1; PR-20 measures the behaviour at `tools/evidence/build_release_attestation.py`) | one sentence: building the attestation off CI is supported under a distribution-patched setuptools (OBS-W2-2) |
| R-8 | 132 | the wheel omits 16 of 45 members | unchanged (S01 removed) | **no change**; no dedicated-environment install note (P-8) |

### 6.2 `AGENTS.md` (operative passages only)

| ID | Line | Current statement | Fact and source | Required change |
| :- | -: | :- | :- | :- |
| A-1 | 137 | "Generic closeout-candidate capability is defined by `schemas/epic_close_candidate_source.v1.json` and `tools/qa/generate_epic_close_pack.py` …" | as R-3 | add schema v2 and CRD identity. The HDE-EPIC039 nonclaims and the v1 statement stay as history (P-8: "the extended close-pack capability and schema v2") |
| A-2 | 125, 130 | "`catalog/manifest.json` version `1.3.0`, 45 members"; "OPS01 verifies the `1.3.0` release separately" | as R-1 | add "refreshed in place with no version cut" and the current `release_id` (P-8). Line 130's HDE-EPIC040 nonclaim stays |
| A-3 | 65 to 75 | "… a path under any of them returns no lanes at all, whatever its suffix — a `.py` file there is exempt too." | the classifier adds the `evidence` lane to an Evidence-Index-governed path under these prefixes (`classify_ci_changes.py:1897-1899`; measured: `docs/run/PROD_ENDPOINTS.json` and `docs/run/EPIC011_TEST_IDENTITIES.md` → `evidence`). The workflow filter re-includes those two files and `**.path_proof.txt` (§5.4) (DOC10-F1) | correct the factual description of the classifier and workflow, verified against both. **The review-scope rule is the Product Owner's direction of 2026-09-21 and is not changed.** If the correction would change which paths that rule exempts, PR-20 asks the Product Owner instead of editing (§9.2) |
| A-4 | 55 | "always install dev test dependencies … `python -m pip install -r requirements-dev.txt` …, then run `python -m pytest --version`" | CI installs `'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` (`ci.yml` lines 86-94); without `-e .` there is no `hdctl` script, and five tests fail (§5.5; DOC10-F2) | state CI's install, keeping the readiness proof |
| A-5 | 45 | "maintain the dev Reader helper (`scripts/dev_start_reader.sh`) …" | as R-5 (OBS-P3-8) | state the start command with `APP_ENV=dev` and the loopback bind |
| A-6 | 169 | "Repo-supported EPIC037 validation references are evidence/gate entrypoints only: `tools/evidence/generate_hde_epic037_field_sufficiency.py`, …" | the five generators exist; their tests were retired in WU-PR-01 (`tests/retired_tests.md` lines 44 and 49; O-2); an edit to them still fails classification with `CI_EVIDENCE_OWNER_TEST_MISSING` | state the measured posture of each generator. PR-20 runs each listed `--check` at its head under closed rails and records the exit code and output. Name none as a current validation entrypoint unless its `--check` passes |
| A-7 | "Operating workflow" | no mention of the pre-push check | §5.3 | one line naming `python tools/ci/prepush_check.py` for lanes, membership and replay before pushing, pointing to R-2's note (the business case's benefit) |

`AGENTS.md` beyond A-1 to A-7 is unchanged: the Code review guidelines, the canon-first and PF10 rules, the Product Owner direction paragraphs, the roster, the posture records and the Local Codex recovery note. The WU-PR-07 PR implementation plan v1.1 §18 noted "Product Owner instruction needed to edit `AGENTS.md`". The approved P-8 scope names these passages, and the Product Owner's Proceed on the exact PR-20 plan is that instruction for the planned edits only (§9.2).

### 6.3 `CHANGELOG.md`

| ID | Line | Required change |
| :- | -: | :- |
| CH-1 | top | One new entry, "Unreleased — HDE-CRD-0002", with the existing Added / Changed / Fixed form. Each bullet names its requirement and merged PR (§4). It records the harness retirement (S09) and the `1.3.0` refresh in place. It closes with the nonclaims: no QA verdict, acceptance, Ops, deployment, activation, PF09 or PF30 movement, or closure. The historical entries, including line 333's 2025-10-16 harness note, stay as history |

### 6.4 `docs/EVIDENCE_INDEX.md`

| ID | Required change | Fact and source |
| :- | :- | :- |
| E-1 | CRD admission: the source-owned `ADMITTED_CRD_QA` table admits HDE-CRD-0001 and HDE-CRD-0002 with their QA roots and key prefixes. Another CRD needs its own row; this is not discovery | §5.3; S22 |
| E-2 | Mirror labels: a current-release capture in `CURRENT_RELEASE_CAPTURE_PATHS` carries the release label in `notes` only when its owner regenerated it; a release change alone never relabels; frozen families keep their labels; **the label is not proof that an owner ran** | updater lines 56-62; S12; OBS-W2-1; CX-2 residual LR-O1 (WU-PR-02 lineage review v1.0) |
| E-3 | Close-run family: the post-verdict close-run family of an admitted CRD, published by `publish_crd_close_run_family`, with its membership rule. PR-20 measures the root path and members | updater lines 4008-4042 and 5222; S21; PF10 addendum 2.15 |

### 6.5 `docs/CLI_commands.md`, `docs/server/reader_v1.md`, `docs/qa_harness_pattern.md`

| ID | Document | Required change |
| :- | :- | :- |
| L-1 | `docs/CLI_commands.md` | Final pass. PR-20 compares every statement with `hdctl --help` and each subcommand's help at its head (closed rails, CI's install) and lists each mismatch. Known delivered changes: S07, S08, S14 and the dev harness (S09, S10). Line 78's start command is already current |
| V-1 | `docs/server/reader_v1.md` | P-8's "not-found limitation line removed": no such line exists at `6f2478f`. Line 20 states the delivered behaviour, landed by #643. **No change expected**; PR-20 confirms it and records it |
| Q-1 | `docs/qa_harness_pattern.md` | Line 79 says the "supported governed identity is **only `HDE-CRD-0001`**", and the page names only `publish_crd_check_family` (WU-PR-07 plan v1.1 §18). Change: CRD admission per E-1; add `publish_crd_close_run_family` (E-3). The rest of the page stays |

### 6.6 Routed stale documents (PF10 addendum 2.21)

| ID | Document:line | Current statement | Fact | Required change |
| :- | :- | :- | :- | :- |
| U-1 | `docs/RUN.md:5` | the runner "binds `0.0.0.0` on `PORT` (default `8000`)" | binds `127.0.0.1` (§4 S10) (OBS-P3-12) | the loopback bind |
| U-2 | `docs/RUN.md:9` | `pytest -q tests/test_sercanon.py` | retired; the retained test is `tests/infra/test_sercanon_bytes.py` (`tests/retired_tests.md` line 70; O-4) | the retained test |
| X-1 | `docs/RUN.md:65-66`; any other runnable `bg:resolve --source vendor` command in README, AGENTS.md, `docs/CLI_commands.md`, `docs/EVIDENCE_INDEX.md` or `docs/INDEX.md` | a command without an explicit `APP_ENV` | S14: vendor resolution needs a recognized `APP_ENV` (WU-PR-04 plan v1.0 §17) | PR-20 classifies each hit as a runnable command or a historical description. Measured hits: `AGENTS.md` 166, 173, 181; `CHANGELOG.md` 40, 51, 67; `README.md` 60, 70; `docs/CLI_commands.md` 51, 52; `docs/EVIDENCE_INDEX.md` 74; `docs/INDEX.md` 32, 35; `docs/RUN.md` 65, 66. Only runnable commands gain an explicit recognized `APP_ENV`; historical descriptions stay |
| D-1 | `docs/ADAPTER_009.md:7-8` | `/internal/version` listed twice, once "(prod requires Authorization: Bearer)" | one route; no authorization check (§5.3) | one line, with no Bearer claim |
| D-2 | `:20-21` | "dev/staging: open on localhost; bearer optional"; "prod: … requires Authorization: Bearer <ENGINE_SERVICE_TOKEN>" | no source reads `ENGINE_SERVICE_TOKEN`; no auth check; the documented client host is `127.0.0.1` | state the measured behaviour; remove the Bearer requirement |
| D-3 | `:44` | the EPIC-005 Bearer note | as D-2 | reconcile with D-2 |
| D-4 | `:51-52` | "ENGINE_ENV=dev\|staging\|prod (default dev), ENGINE_SERVICE_TOKEN (prod only)"; "Optional fixed meta: … RELEASE_ID, TOGGLES_SHA" | `ENGINE_ENV` is only the fallback when `APP_ENV` is blank; `ENGINE_SERVICE_TOKEN` and `TOGGLES_SHA` are unread; `RELEASE_ID` feeds only `adapter/wsgi.py`'s header and logging | state what is read and by which app |
| D-5 | `:119-135` | the capture environment: `PYTHONHASHSEED=0 PYTHONUTF8=1 TZ=UTC SAFE_MODE=1` | `/reader` needs `APP_ENV=dev`; closed rails also pin `ALLOW_NETWORK=0 LC_ALL=C LANG=C` | add `APP_ENV=dev` and the full closed-rails tuple. The S17 bind statements (lines 119 and 135) stay |
| D-6 | `:29` and the header block | `X-Release-Id: <release_id>` | `adapter/wsgi.py` sets it from `RELEASE_ID`, default `rel_dev`; it is not the canonical `release_id` | state the source and the default |
| D-7 | `:141-147` | "Use the exact start line that shipped in EPIC-005", with a `pip install` prefix | the repository's start line is the `Procfile` line (§5.3); deploys come from commits on `main` (P-9; addendum 2.19) | state the `Procfile` line as the repository's start command. Claim nothing about the live service's settings (§7) |
| D-8 | `:112` | `pytest -q tests/test_sercanon.py` | as U-2 (O-4) | the retained test |
| K-1 | `docs/contracts/reader_v2_public_bytes.md:19` | "Known limitation: a path that no route serves … receives the framework's HTML 404 …" | removed by S02 (§4) (F-8) | replace with the delivered behaviour, matching `docs/server/reader_v1.md` line 20 |
| P-1 | `docs/acceptance/reader_a7_crib.md:15-19` | proof writer "`tests/http/test_reader_a7_transport.py`"; file `encoding_invariance.txt` | writer and proof list as §5.3; `encoding_invariance.txt` is asserted absent | name the writer, its write gate and `--check`, and the current proof files |
| F-1 | `tests/fixtures/g05_*`, `g08_*`, `*__admin.json`, `tests/goldens/*` (OBS-8) | orphaned fixtures | test-data files, not documentation | **not this unit.** Routed to the Product Owner as a later cleanup candidate (§15) |

**Count:** 36 items:
- 33 changes. Four of them have a size PR-20 measures and records: X-1's runnable commands, L-1's mismatches, A-6's generators and E-3's members.
- 2 no-change confirmations: R-8 and V-1.
- 1 routed exclusion: F-1.

## 7. Exclusions

- **No canon edit.** Nothing in `docs/pfcanon/` changes. The canon doc-deltas that the lineage reviews named stay with the Product Owner (§15). Examples: HDE Mechanics Guide §34 "Current repository posture"; HDE Users Guide §4.1; HDE Schemas & Artifacts §8.3 and §8.8; HDE-CLI-API-Vendor-Ref §5.6 and §7.1.11; Glow Infrastructure §8; the S21 drainage targets.
- **Nothing generated or governed is edited by hand:** no Index/Mirror row, path proof, hash sentinel, manifest, close report, acceptance map, orientation output, `docs/ENDPOINTS_CATALOG.json` or `artifacts/`. No write-producing generator runs. The A7 writer, the updater and the EPIC037 generators run only with `--check`.
- **No code, test, fixture, workflow, schema, script or release member** changes. That covers `scripts/make_release_pack.sh`, `scripts/hd_cli.py`, `tools/ci/prepush_check.py` (DOC10-O1), `scripts/qa/dev_sampler_healthcheck.py` (OBS-P3-13) and `tests/tools/test_prepush_check.py` (PR35-C1).
- **Not edited:** the S21 ADR, whose revision needs the Product Owner's instruction (addendum 2.17), and historical entries and posture records, which stay as history.
- **No Ops fact.** No statement about the live service's start command, build command, deploy trigger or settings. Deploys come from commits on `main`, and WU-OPS-01 proves the deployment by `release_id` (addendum 2.19).
- **No other documents** outside §6. A newly found stale statement elsewhere is recorded and routed, not edited (§9.3).
- **No claims** of QA, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.

## 8. Interface contracts with other units

| Contract | Counterpart | Content |
| :- | :- | :- |
| G-1 (WU-PR-06) | the pre-push check | R-2 states LR6-O5 and LR6-O7's limits exactly. The usage note claims nothing beyond the tool's own help |
| H-4 (WU-PR-07) | the close-pack writer | the v2 schema, both identities, the outputs and the nonclaims, as the PR result record states them, read with the ADR and addendum 2.17 (R-3, A-1) |
| IF-4, IF-5, IF-7 (WU-PR-02, WU-PR-07) | the updater | E-1 to E-3 describe the updater at the PR head |
| DOC-20 | completion verification | DOC-20 checks the measure: each changed statement matches merged `main` |
| WU-OPS-01 | Ops | no document states Ops facts (§7) |

## 9. Disposition rules PR-20 must apply and record

### 9.1 Plan choices (PR-20's, recorded)

- the placement and wording of each change;
- whether R-2's note sits in README "Quickstart" or in its own section;
- CHANGELOG bullet grouping;
- one PR, unless PR-20 shows a reason to split. One PR is expected.

### 9.2 Product Owner questions (asked, not decided by PR-20)

- **A-3:** if the factual correction would change the set of paths that the 2026-09-21 review-scope rule exempts.
- **Any `AGENTS.md` change beyond A-1 to A-7.**
- **A-6:** whether to keep the EPIC037 generators listed when some `--check` fails.

The Proceed on a plan that names the exact `AGENTS.md` edits is the Product Owner's instruction for those edits.

### 9.3 Baseline re-check

- PR-20 re-measures every §5 and §6 fact at its own head and records each difference.
- A statement found already current is recorded as "no change".
- A new stale statement inside the §6 documents and within an item's subject is added and recorded. A stale statement outside them is routed, not edited.

### 9.4 Prototype

- PR-20 drafts the full text and applies it in a throwaway copy.
- In that copy it runs the §10 test set and the `lanes` report, and records the results.

### 9.5 Measure

- The plan lists every changed statement with the code, help output or record that proves it at the head.
- That list is what DOC-20 verifies.

## 10. Acceptance, tests and evidence

1. **Traceability:** each changed statement names a merged unit or a measured fact (Plan v1.1 §7; §4).
2. **`tests/unit/test_check_agents_md_citations.py` passes** (Plan v1.1 §7). It runs locally, because CI selects no lane (§5.4).
3. **The document-reading tests of §5.5 pass** on the PR head with CI's full install, including `-e .`. Run that install in a throwaway copy or a dedicated environment, not the checkout, so egg-info does not dirty the tree. The baseline's five `hdctl` failures must not recur under that install. PR-30 runs the set before publication; PR-35 runs it on the final head.
4. **`python tools/ci/prepush_check.py lanes membership build-notes`** on the PR head: `documentation_only`, no member changed, PF10 path and hash recorded.
5. **Hosted CI on the final head:** the `test` job succeeds and ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
6. **No path outside the planned list changes** (`git diff --name-status` against the base).
7. **Evidence:** the PR result records under `docs/ephemeral/` hold the statement-to-proof list (§9.5), the test counts, the `lanes` output and the CI run identity. The PR creates no evidence family and no QA artifact.

## 11. Security limits

- No secret, token, key value or base URL in any document. Environment names appear as names, or as SET/UNSET (`AGENTS.md` redaction rule).
- The `/internal/version` statements (D-1 to D-4) describe the measured behaviour only. They do not propose an authorization design. If PR-20 judges the missing authorization a security concern, it records it and routes it to the Product Owner. It is not fixed or decided in this unit.
- Closed rails for every local run. No live vendor, production or database access.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated session) reads:
  - this instruction and its lineage;
  - P-8 and addendum 2.21's routing;
  - the §6 documents in full;
  - §5's code and tools at its head;
  - canon on `main`.

  It then re-checks the baseline (§9.3), prototypes (§9.4), writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/`, and returns `AWAITING_PO_PROCEED`.
- **PR-30** (after Nathan's Proceed for that exact plan):
  - recovers existing work first;
  - edits only the planned documents;
  - runs §10 items 2 to 4 and 6;
  - commits coherently and publishes `PR_CANDIDATE_PUBLISHED`;
  - hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session):
  - retrieves review threads. Codex is not expected to report, because the change is all Markdown (§5.4). A human or other review comment is dispositioned under addendum 2.11 rule 7 and addendum 2.14;
  - re-runs §10 items 2 and 3 on the final head;
  - verifies item 5 and mergeability;
  - returns `MERGE_PENDING` without merging.
- **PR description:** the `.github/pull_request_template.md` headings, filled under the `AGENTS.md` content rules.
- **Merge:** Nathan merges manually.
- **PR-40:** this IA reviews the landed lineage, entered on `MERGE_OBSERVED` or, only where none was returned, on Nathan's merge assertion.
- **DOC-20:** verifies completion against the measure. Then WU-OPS-01's business case is due before OPS-10.
- **Nonclaims:** every record keeps the §7 nonclaims.

## 13. Recovery

- **Interruption:** resume from the phase's last saved artifact. Inspect branches, PRs and `docs/ephemeral/` before creating anything.
- **Prototype:** runs only in throwaway copies.
- **An instruction defect** returns to this IA through DOC-10. A corrected instruction is a new version.
- **Abort** is only Nathan's manual PR-50.

## 14. Rescope behavior

- **Material** means a change to an approved acceptance intent, a protected boundary, several units' scope, an accepted dependency, or scope or risk that needs Product Owner direction.
- **Before Proceed**, the PR-20 author owns a rescope proposal (RS-10; RS-30 for revisions), and this IA reviews it through RS-20. After Proceed, PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Expected triggers:**
  - a needed change in code, a test, a workflow, canon or a governed artifact;
  - a documentation fix that needs a behaviour change, such as `/internal/version` authorization;
  - A-3 changing the review-scope rule.
- **Not a trigger:** a §9.1 choice, or a stale statement found inside a §6 document within an item's subject.

## 15. Unresolved items, carried observations and owners

| Item | Owner | State |
| :- | :- | :- |
| DOC10-F1: `AGENTS.md`'s CI-exempt note omits the governed-path `evidence` lane and the workflow's re-includes | this unit (A-3) | to correct the description; the rule is unchanged |
| DOC10-F2: `AGENTS.md`'s pytest guidance omits CI's `-e .` | this unit (A-4) | — |
| DOC10-O1: `tools/ci/prepush_check.py` `lanes` note "documentation_only means the workflow's path filter starts no hosted run" is wrong for paths the filter includes | Product Owner (later change candidate; code) | observation |
| O-19 code: `scripts/make_release_pack.sh` and `scripts/hd_cli.py` | Product Owner | documentation side in R-6 |
| OBS-8: orphaned fixtures (F-1) | Product Owner (later cleanup) | routed |
| OBS-P3-13: `scripts/qa/dev_sampler_healthcheck.py:129` comment | this IA (QA tool owner) | not this unit |
| PR35-C1, LR8-F1 | Product Owner (addendum 2.21) | carried |
| Canon doc-deltas (§7 list) | Product Owner | carried |
| The S21 ADR revision (addendum 2.17 drainage) | Product Owner's instruction | carried |
| `/internal/version` authorization, if raised (§11) | Product Owner | conditional |
| WU-OPS-01 business case | Product Owner | due before OPS-10 |
| The §9.1 choices | PR-20 session | in the plan |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | IA through RS-20 | WU-PR-01 rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | addendum 2.7 |

**No new conflict.** The routed stale statements are repository-documentation drift, not canon conflicts:
- The canon passages that still state the old posture are doc-delta candidates the Product Owner owns. For example, HDE Mechanics Guide §34 "Current repository posture" still states the `0.0.0.0` bind. Canon governs canon, and repository documents follow the delivered code.
- PF03-Reference-Technical-Writing-Best-Practices "Canonical ownership" says a durable cross-document reference names its target by title, without a version number. The repository documents already cite PF documents by title (README line 3). New text keeps that.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Acceptance | Stage |
| :- | :- | :- | :- | :- |
| P-8 bounded scope | the six documents and their named passages | §6.1 to §6.5 | §10 (1), (2) | PR-20 to PR-35; DOC-20 |
| Addendum 2.21 "stale-document list … goes to WU-DOC-01" | the routed items | §6.6 | §10 (1) | PR-20; DOC-20 |
| Plan v1.1 §7 "Each statement traces to a merged unit" | statement-level traceability | §4; §9.5 | §10 (1) | PR-40; DOC-20 |
| Plan v1.1 §7 "`test_check_agents_md_citations.py` passes" | the `AGENTS.md` citation checker accepts the edited file | §10 (2), run locally | §10 (2) | PR-30; PR-35 |
| Business case measure | each changed statement matches merged `main` | §9.5 list | — | DOC-20 |
| Addendum 2.19 summary "drops the dedicated-environment install note" | no install note | R-8 | — | PR-20 |
| "No canon, no generated evidence, no governed artifact by hand" | the exclusions | §7 | §10 (6) | all phases |

**Checks against PR-20's input contract.** Its sole substantive input is `PR_INSTRUCTION_ID`, and this instruction carries:
- the Specification, delta, Audit, Plan, delta and review lineage;
- PF10 and the overlays;
- the business case;
- the baseline, documents, items, exclusions, interfaces and dependencies;
- acceptance, evidence, security, recovery, rescope, merge ownership and the return owner.

PR-20 plans without mutating the repository, beyond its own artifacts. There is no numeric domain, sentinel or closed schema in this unit. No decisive comparison fails: every fact in §5 and §6 was measured at `6f2478f` by this IA, except those marked "PR-20 measures".

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated top-level WU-DOC-01 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Returns to this IA:**
  - PR-40 after Nathan's merge, then DOC-20;
  - RS-20 for a rescope;
  - DOC-10 for an instruction defect.

## 19. TypeSafe reading for the receiving session (PR-20, WU-DOC-01)

Action sent (v8.2): "Write, in a new dedicated session, the first detailed PR implementation plan, not yet reviewed, for the final repository-documentation work unit of an approved change: correct or add about thirty statements across eleven Markdown documents (README, CHANGELOG, the agent-instructions file's operative passages, an evidence-index guide, a CLI reference, a runbook, an operator document, a harness guide, a contract page and an acceptance crib) so each matches the delivered code, including usage notes for a read-only pre-push check and a close-pack writer. A ready instruction lists each statement, the measured fact and the code that proves it; the plan re-measures each at its head against code and tool help, drafts the exact replacement text, and names the local tests that read these documents, because CI runs no test lane for a documentation-only change. No code changes and no live run occur; a Product Owner Proceed, implementation, CI, a lineage review and a completion verification follow."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 1.98 (confidence 0.87). Rung probabilities: low 0.01, medium 0.09, high 0.82, extra high 0.08, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.00, Opus 5.5 0.89, Sonnet 5.5 0.11, Haiku 5.5 0.00 (confidence 0.85).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.009, Opus 5.5 at medium 0.080, Opus 5.5 at high 0.730, Opus 5.5 at extra high 0.071, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.001, Sonnet 5.5 at medium 0.010, Sonnet 5.5 at high 0.090, Sonnet 5.5 at extra high 0.009, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Sent 2026-10-22T01:13:55Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T01:13:55Z; HTTP 200 in 0.63 s; 5540 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:**
  - The Notion row was not written.
  - Nathan's pick for PR-20 is not stated.
  - Nathan's pick for this DOC-10 session is not stated. Its reading is in the disposition record §5.

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment:**
  - Python 3.12 with CI's full install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), done in a throwaway copy or a dedicated environment so egg-info does not dirty the checkout;
  - git, bash and `ruby` for the pre-push check;
  - closed rails, with the vendor, database and GitHub keys the container sets left unset.
- **Run times observed:**
  - the §5.5 test set: about 76 s;
  - each `prepush_check.py` report: about 3 s.
- **Access:** no live vendor, production or database access is needed.
- **Order:** this instruction's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / DOC-10 / instruction 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| unit | WU-DOC-01 (S02 to S22 documentation; §4) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb81ce99b1d2ade30c572f (page state of 2026-10-12T02:29:24.131Z). Receiver contract read: PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state of 2026-10-12T02:29:47.327Z), Inputs and Execute |
| role/stage | continuing whole-change IA / DOC-10 |
| capture time | 2026-10-22T01:14:05Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| inherited usage | the disposition record (this session) |
| repository persistence | recorded here only. The installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`; persistence is pending and non-gating |

## Canon relied on

Read on `main` at `6f2478f`. PF10 is v13.7.4 (path and hash in the front matter).

| Topic | Sources and sections |
| :- | :- |
| DOC-10 operation and routing | DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, read in full: "Execute" 1 to 6; "Required result"; "Result routing"; "Runtime artifacts, readback, and handoff" |
| Receiver contract | PR-20 — Create Detailed PR Implementation Plan — 100926.1: "Inputs" and "Execute", read in this invocation |
| Unit scope | Implementation Plan v1.1 §7 WU-DOC-01, §6, §8 and §11; Plan delta 01 v1.1 P-6, P-8, P-13 and its §4 summary; PF10 addendum 2.19 (the P-8 text and "WU-DOC-01: drops the dedicated-environment install note") |
| Routed items | PF10 addendum 2.21 (the stale-document list; LR8-F2; LR8-O1), read in full; addenda 2.8 (LR3-O4; harness references), 2.10 (F-3, O-19 carry), 2.12 (LR6-O5, LR6-O7, G-1) and 2.16 (stale-document list) at those passages; the WU-PR-01 to WU-PR-08 lineage reviews at their WU-DOC-01 rows; WU-PR-03 plan v2.0 §18; WU-PR-04 plan v1.0 §17; WU-PR-07 plan v1.1 §18; WU-PR-02 plan v1.0 OBS-W2-1 and OBS-W2-2 |
| Writer usage note | PF10 addendum 2.17, read in full ("Deferred obligations": "WU-DOC-01's usage note for the writer (contract H-4) reads the ADR together with this addendum"); WU-PR-07 instruction v1.0 H-4 row |
| Business case; no ceiling | Disposition record §2; PF10 addendum 2.18 "Epic, task, and status effects"; addendum 2.11 rules 1 to 3 (from the disposition work in this session) |
| Dispositions and P1 | PF10 addendum 2.11 rule 7 and addendum 2.14, as the WU-PR-08 instruction applied them in this session |
| Reviewer chain | PF10 addendum 2.3; `AGENTS.md` "Code review guidelines" (the Markdown exclusion) |
| QA entry ordering | PF19-Canon-Glow-QA-Guide §3.1 "Intent" ("Complete and accept the required implementation PRs, applicable Ops and final repository-documentation PR before whole-change QA entry. Repository documentation delivery is distinct from later permanent PF drainage") |
| Source fidelity and citation form | PF03-Reference-Technical-Writing-Best-Practices "Truth and source fidelity" and "Canonical ownership", read in full |
| Doc-Delta discipline | PF04-Canon-HDE-Governance "Doc-Delta discipline" (normative edits need a Doc-Delta; stylistic or non-functional rewording does not); this unit makes no normative edit |
| Repository rules | `AGENTS.md`: canon-first rule; "Code review guidelines"; "Operating workflow" (pytest readiness; redaction; docs-only PR posture; PR descriptions); "Doc agents" roster line; "HDE-EPIC039 current workflow posture"; "HDE-EPIC040 current posture"; "Release identity" |
