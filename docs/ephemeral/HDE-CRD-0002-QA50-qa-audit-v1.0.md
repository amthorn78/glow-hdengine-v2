---
artifact_type: QA_AUDIT
artifact_id: HDE-CRD-0002-QA50-QA-AUDIT
artifact_version: "1.0"
predecessor: none (the first QA Audit for HDE-CRD-0002)
state: AUDIT_COMPLETE
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Kronos, the QA authority for HDE-CRD-0002 (initial dedicated assignment; execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV, the session the Product Owner gave the QA-50 handoff to; it earlier served HDE-EPIC040 QA as Kronos-23)
session_disposition: Product Owner-selected context; no earlier Kronos work for HDE-CRD-0002 exists
context_conflict: none
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
prompt: QA-50 — Create Whole-Change QA Audit and Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb815d89d3e602973d83ad; page state 2026-10-12T02:30:48.299Z, read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
LIVE_QA_GUIDE_ID: docs/ephemeral/HDE-CRD-0002-QA20-live-qa-guide-v1.0.md (GUIDE_READY; #719, 0b15328d)
QA_READINESS_ID: docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.1.md (READY_FOR_QA)
REALITY_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-QA10-reality-audit-v1.1.md
CHANGE_AUDIT_TRIAGE_ID: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.1.md (40 findings)
companion_plan: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.0.md (QA_PLAN v1.0, PLAN_PENDING; holds the CANON_CONFLICT_REGISTER)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (519,440 bytes; sha256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; addenda 2.1 to 2.26)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-50
repository_head_read: origin/main 0b15328d585a764c124936b4524b766525daf1d9 (tree 9b58a6798409fddf4d51bdbf97926feb1f6f20ab)
created_at: 2026-10-24T02:27:05Z
---

# HDE-CRD-0002 — Whole-Change QA Audit v1.0 (QA-50, phase 1)

This Audit establishes what independent QA of HDE-CRD-0002 must prove, what the repository and environment actually support, and which gaps belong to which owner. It is the basis for QA Plan v1.0, written in the same invocation.
- **What it is not.** It executes no QA, makes no QA verdict, approves nothing, and decides no canon, scope or remedy. The throwaway-clone inspections in §7 are planning validation; none is QA evidence, and nothing from them was committed.
- **Result.** The change is testable as delivered. This Audit found no product defect. It records eleven planning findings (§8), one new proposed canon conflict (CR-11, carried in the Plan's register), and the design decisions the Guide left to QA-50 (G-1, IR-6, FND-004, FND-007, FND-011, FND-031, FND-032, FND-033).

## 1. Lineage and inputs

| Input | Identity and state | Read |
| :- | :- | :- |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (SPECIFICATION_APPROVED) with Specification delta 01 `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` (DELTA_APPROVE; HDE Build Notes addendum 2.20) | In full |
| Implementation Plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (approved by `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md`, INITIAL_APPROVE), with Plan delta 01 `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md` (DELTA_APPROVE; addendum 2.19) and the FND-001 overlay P-1 and amended P-2 (addenda 2.23, 2.24) | Plan §1 to §11 and §13 to §15 in full; delta 01 in full; overlays as addenda 2.23 to 2.25 state them |
| Readiness | QA readiness v1.1, Reality Audit v1.1, Change Audit Triage v1.1 | Readiness and triage in full; Reality Audit v1.1 in full |
| Live QA Guide | `docs/ephemeral/HDE-CRD-0002-QA20-live-qa-guide-v1.0.md` | In full |
| Accepted delivery | PR-40 lineage reviews of WU-PR-01 to WU-PR-08 and WU-DOC-01 (all ACCEPT); WU-REM-01 lineage review v1.0 (ACCEPT; #716, `3a5d846`); WU-DOC-01 documentation completion v1.1 (COMPLETE) | WU-REM-01 review and WU-DOC-01 completion in full; the others through addenda 2.4, 2.5, 2.8, 2.9, 2.10, 2.12, 2.16, 2.21 |
| S19 record | `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` | In full |
| Ops | `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-receipt-v1.0.md` (ACCEPT); evidence `audit/ops/hde-crd-0002/wu-ops-01/` (six files) | Receipt in full; evidence file list |
| Canon conflict register | CR-1 to CR-10, as the Guide §13 and readiness v1.1 §6 carry them | In full |
| Product Owner dispositions | AQ-1 (addenda 2.15, 2.17); Specification delta 01 scope decision; the deployment direction of 2026-10-21 (addendum 2.19); the no-ceiling rule (2.18). Pending: FND-028, FND-029 (S19-R01 to R07), the live vendor call's initiator and venue | As cited |

**Repository state.** `origin/main` is `0b15328d`. Outside `docs/ephemeral/` and `docs/pfcanon/`, `git diff 3a5d846 0b15328d` is empty, so the code on `main` is the WU-REM-01 merge's code, and its runtime code is the WU-OPS-01 candidate's (Guide §1). `audit/qa/hde-crd-0002/` does not exist (0 tracked files).

## 2. The candidate under test

| Fact | Value | Source |
| :- | :- | :- |
| Release | `1.3.0`, built `2026-08-24T18:04:49Z`, 45 members | `catalog/manifest.json`; addendum 2.20 (no version cut) |
| `release_id` | `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` | `sha256(catalog/manifest.json)` at `0b15328d`, recomputed here |
| Code identity | `0b15328d` code equals `3a5d846` outside `docs/ephemeral/` and `docs/pfcanon/` | `git diff --stat`, empty |
| Deployed identity | Production `GET /internal/version` reported the same `release_id` at 2026-10-23T13:30:06Z, one read | WU-OPS-01 receipt SC-1 |
| Deploy source | Commits landing on `main` deploy to the Railway service | Plan delta 01 P-9, P-18 (addendum 2.19) |
| `build_commit` | Fixed source value `9479d28`; it does not identify the deployment | Plan delta 01 P-9 |

A later QA run that finds `main` advanced keeps this candidate only if the code outside `docs/ephemeral/` and `docs/pfcanon/` is unchanged; otherwise the run stops at its preflight (Plan check 1).

## 3. Requirement and acceptance coverage

The criteria are the Specification's acceptance intents as delta 01 leaves them: S02 to S22 in scope, S01 removed. "Owed at QA" is what independent QA must still prove beyond implementation tests and hosted CI (Glow QA Guide §3.1: functional changes need runtime proof on the changed surface, or CI proof that executes it).

| Req | Delivered (Guide §2) | Owed at QA | Live QA class (Spec; PF19 §3.5.6 class) | Plan check |
| :- | :- | :- | :- | :- |
| S01 | Removed; not delivered (delta 01 C-1, C-6) | The removal and its stated limit hold (no version cut; README states the packaging limit); the close writer still reads S01 (G-1) | None (delta 01 C-12) | 15 |
| S02 | Governed 404/405 envelope on `adapter.factory` | Deployed-target probes | Functional-feature; class 1/2 | 17 |
| S03 to S05 | Coverage, ledger, owner refusal, filter equality | Repository checks | Not production-affecting | 2 |
| S06 | Debian setuptools shim in the wheel stage | The attestation builds under a distribution-patched setuptools on the candidate (FND-007, decided in §8) | Not production-affecting | 3 |
| S07 | Help summary names `magic10_compat_result.v1` | The exact summary on the operator CLI surface | Functional-feature (operator CLI); class 2 | 4 |
| S08 | `aux-preview --band` applies with `--pair-file` | The override on the operator CLI surface | Functional-feature (operator CLI); class 2 | 5 |
| S09 | Harness retired; `VERIFY.sh` exact `dev` | Repository checks | Not production-affecting | 6 |
| S10 | Exact `APP_ENV=dev` gate; production-posture refusal | Local gate matrix and runner profile; deployed refusal | Functional-feature; class 1/2 | 7, 18 |
| S11 to S13 | Drift test; labels; root-bound probe | Repository checks | Not production-affecting | 8 |
| S14 | `--allow-prod-vendor` per HDE CLI/API/Vendor Ref §7.1.11a to f | Local matrix tests; the mandatory human-initiated live vendor call | Functional-feature, mandatory vendor call; class 3 | 9, 20 |
| S15 | 18 catalog records; 53 pairs accounted | Repository checks | Catalog entries only | 10 |
| S16 to S18 | Template key; document statements | Mechanical document alignment | Not production-affecting | 11 |
| S19 | Record; 9 fixed, 7 routed | Record and 268 regression cases; F01 and F03 in the deployed target; F05 and F06 at the vendor call | Inherits per fix (S19 record §4) | 12, 18, 19, 20 |
| S20 | `tools/ci/prepush_check.py` with five reports | One run of every report, read-only | Not production-affecting | 13 |
| S21 | v2 close-pack writer; close-run family; ADR approved with changes | Repository checks; the real close is the business-case measure (after QA-120) | Not production-affecting | 14 |
| S22 | `ADMITTED_CRD_QA` admits `audit/qa/hde-crd-0002/` | The first real publication under the root, by this QA run; Epic and HDE-CRD-0001 inputs still validate | Not production-affecting | 21 |

**Production-affecting Live QA minimum** (Glow QA Guide §3.5.5; Change Process Guide §1.1.5A; Plan Templates "Open-Rails Live QA Requirement for production-affecting epics"): satisfied in the Plan by checks 17 to 19 (bounded open-rails live steps against the deployed service) and check 20 (one live vendor call under `SAFE_MODE=0`, `ALLOW_NETWORK=1`, synthetic data only). No S01 step or exemption is needed (delta 01 C-12).

## 4. Canon determinations the Plan applies

These are read from canon; none is put to the Product Owner as a question (Glow QA Guide §11.3; the HDE-EPIC040 planning-failure RCA v1.1 lessons C3 and D2).

| Topic | Determination | Canon |
| :- | :- | :- |
| Default rails | Closed: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, with `APP_ENV=dev` (the Development binding) | Plan Templates "Rails posture (explicit)" and "QA Rails — Open/Close (Final PR)"; Glow QA Guide §2.2.6, §2.3; Glow Infrastructure §2.4 "Development"; `AGENTS.md` closed-rails default |
| Production-target checks | The Production binding: `APP_ENV=prod`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, for that check only | Glow QA Guide §3.4.8 ("steps that touch production endpoints run with open rails"); Glow Infrastructure §2.4 "Production — Railway" |
| Rails changes | Only between checks; one rails pair per check; never a mixed pair | Plan Templates "Rails posture (explicit)"; HDE-EPIC040 RCA v1.1 §4 |
| Local test re-runs | Labelled "local/offline (no vendor)", PF19 class 2; never counted as live behaviour proof | Glow QA Guide §3.3, §3.4.8 |
| Vendor call | `hdctl bg:resolve --source vendor --dry-run` with the full synthetic birth tuple; `--upsert` forbidden | Glow QA Guide §3.3 (offline/local checks block, dry-run under open rails); HDE CLI/API/Vendor Ref §7.1.11d |
| Initiator | An authenticated human Product Owner, or a human operations executor the Product Owner delegates in the approved work item; not an AI agent | HDE CLI/API/Vendor Ref §7.1.11e; Specification constraint "Override initiator". The directed-agent rule of Glow QA Guide §3.5.7 neither implements nor waives this (§7.1.11 preamble) |
| Vendor configuration | From the environment only; `SET`/`UNSET`; a missing name means no call and `TOOLING_BLOCKED` | Glow QA Guide §3.5.7; Plan Templates "PO inputs needed" |
| Vendor evidence | Inside the vendor check's `primary.log` (request description, outputs, notes); no sidecars | Glow QA Guide §3.4.3 "KISS evidence posture", §3.5.7 (sidecar names are schematic; a mechanically generated note in `primary.log` suffices); HDE Mechanics Guide §1.6.3 (no arbitrary additional files) |
| HTTP readiness | A service readiness check precedes behaviour probes; an unreachable service is `TOOLING_BLOCKED`, not a behaviour failure | Glow QA Guide §3.5.10 |
| Header schema | `pf27.step_log_header.v2`, fourteen keys, written by the harness | Plan Templates "Step-log header schema expectations (required; v2)"; HDE Mechanics Guide §1.6.3 |
| Publication | `publish_crd_check_family` only; read-only validators afterwards | HDE Mechanics Guide §1.6.3; `AGENTS.md` evidence harness |
| Consumed Ops evidence | Pointed to from the consuming check's `primary.log`, not re-homed | Glow QA Guide §11.1; CR-9 interim treatment (a) |
| Plan format for the close | `### CHECK <n>` headings with the check ID in backticks, numbered 1 to N in order, each with a `Surface / D-goal mapping:` line before any level-1 to 3 heading | `tools/qa/generate_epic_close_pack.py` `QA_PLAN_CHECK_RE`, `QA_PLAN_SECTION_END_RE`, `QA_PLAN_MAPPING_RE`; addenda 2.16 (LR7-O4), 2.17 |

## 5. Repository and environment facts

All read on `main` at `0b15328d`.

**QA harness (`tools/qa/qa_harness.py`).**
- `HarnessConfig(crd_id="HDE-CRD-0002", repo_root=<checkout>)` sets the QA root `audit/qa/hde-crd-0002`; `CRD_RE` `HDE-CRD-[0-9]{4,}` (:23); check IDs `[a-z0-9][a-z0-9._-]*` (:24).
- `CheckResult` fields (:109-141): `check_id`, `status`, `status_reason`, `check_name`, `command` (one argv tuple or an ordered tuple of argv tuples), `command_provenance`, `exit_code`, `output`, `evidence_artifacts`, `intended_tokens`, `pf_refs`, `captured_env`.
- `captured_env` admits only `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV` (:45, :1426-1440). When it is empty, the harness copies those names from the *publishing* process (:1443-1446).
- `pf_refs` must match `PF[0-9]{2}(?:\.[0-9]+)?-(?:Canon|Reference)-[A-Za-z0-9][A-Za-z0-9-]*` exact titles (:26-28), so HDE Build Notes cannot appear there.
- PASS requires `exit_code` 0 when a command ran, an empty reason and evidence; every other status needs a reason (:1534-1543).
- `record_check_family` merges new results into the existing manifest by `check_id` (:2418-2522): checks may be published in batches.
- CRD records must be UTF-8 without BOM, with LF bytes only; a CR anywhere refuses (:1730-1736).
- `validate_crd_check_family` validates the flat manifest, each primary's header and the status agreement (:1763-1798).

**Canonical updater (`tools/evidence/update_evidence_index.py`).**
- `ADMITTED_CRD_QA` admits HDE-CRD-0001 and HDE-CRD-0002 with roots and key prefixes (:51-54).
- `publish_crd_check_family(config, results, *, captured_at_utc=None, coherence_verifier=None)` (:5166-5219): refuses an unadmitted ID or a foreign root; calls `ensure_determinism_env()`, so publication runs under closed rails; runs the updater's `--check` first; then records, converges and revalidates inside one `_WriteTransaction`.
- `_load_crd_qa_entries` (:3947-4005) admits only the manifest row, `checks/<id>/primary.log` rows and `close/<id>/primary.log` rows; any other row under the root is refused. Files under the root that carry no row are not loaded (HDE-CRD-0001 keeps an unindexed `00_meta/final-verification.log` on `main`).
- Index keys: `audit.qa.hde_crd_0002.qa_step_logs_manifest` and `audit.qa.hde_crd_0002.checks.<check_id>.primary.log` (:3933-3944).
- `publish_crd_close_run_family` (:5222-5291) is the post-verdict close-run writer; it is not used by QA.

**Close-pack writer (`tools/qa/generate_epic_close_pack.py`).**
- The QA plan must be the highest `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v<N>.<N>.md` (:2276-2279, :2750).
- `QA_PLAN_CHECK_RE` `^### CHECK ([0-9]+) \`([a-z0-9][a-z0-9._-]*)\`` (:2280); numbers must run 1, 2, 3 in order with unique IDs (:2439-2449).
- A check's section ends at the next level-1 to 3 heading (:2283); its first `Surface / D-goal mapping:` line names criteria, whole or as `A to B` ranges (:2284-2287, :2452-2477). A requirement ID followed by `-` (for example `S19-F01`) does not count as naming `S19` (`_token_occurs`, :2412-2419).
- Requirement IDs come from the highest `-specification-v<N>.<N>-approved.md` table rows (`CRD_REQUIREMENT_RE`, :2238; `_requirement_ids`, :2660): S01 to S22.
- The acceptance result enum is `MET` or `NOT_MET` (`schemas/close_candidate_source.v2.json`); SATISFIED needs every requirement ID `MET` and bound to a PASS check whose plan mapping names it (:2839-2868).

**Override path (`engine/cli/main.py`, `engine/bodygraph/resolver.py`, `engine/bodygraph/vendor_audit.py`).**
- `bg:resolve` takes `--user` (required), `--source`, `--upsert`, `--dry-run`, `--birthdate`, `--birthtime`, `--location`, `--allow-prod-vendor AUTHORIZATION_REF` (main.py:152-184); `--source vendor` needs the full birth tuple or exits 64 (:263-267).
- The vendor path applies rails, classification, the matrix, the pre-I/O `allowed` event, then route (resolver.py:227-331). The vendor environment overlays the process environment (:670-683).
- A v2 base selects `recommended_v2_chart`; with `--dry-run` there is no database access and one `charts` fetch; stdout carries the redacted request posture, the adapter status and the mapped `resolved` record, no raw vendor payload (:494-620).
- The sink is `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, else `$XDG_STATE_HOME/glow-hdengine/vendor_prod_override.jsonl`, else `~/.local/state/glow-hdengine/vendor_prod_override.jsonl`; a sink inside the repository refuses (vendor_audit.py:85-106). The actor is the effective-UID account name (:64-82).
- `--user` values that are not UUIDs map to a UUID5 (`engine/bodygraph/ingest.py` :36-47).
- The repository's override tests use the synthetic tuple `1990-01-01`, `12:34`, `Amsterdam, NL` (`tests/cli/test_bg_resolve.py`).

**Production app (`adapter/factory.py`, `adapter/http_reader.py`, `engine/http/compat_handler.py`).**
- 404 and 405 answer the governed `ERR_NOT_FOUND` envelope with `no-store` and no ETag; a 405 off the compat namespace carries a sorted `Allow` (factory.py:16-41).
- In a production posture, `_mount_for_production` refuses dev `/reader` (403 `ERR_READER_FORBIDDEN`, version check first), the dev writers (403 `ERR_WRITER_FORBIDDEN`) and the retired `/ops` routes (404) before any handler (http_reader.py:560-625). Every compat path answers 404 in production (compat_handler.py:108-120).

**Infrastructure** (Glow Infrastructure §2.2, §2.4, §2.6, §2.7): production service `glow-hdengine-v2` in Railway project `ample-illumination`, base URL `https://glow-hdengine-v2-production.up.railway.app`; Production binding `APP_ENV=prod`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, with `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL` set (PF07 records `HD_API_BASE_URL` as a v2 base). Any shell that reaches the base URL is a valid console for the CLI (§2.7).

## 6. Expected responses for the deployed probes

Computed with the Flask test client on `0b15328d`, `APP_ENV=prod` at registration (planning inspection, §7 item 5). The live service may differ only in router behaviour outside the app (IR-3).

| Probe | Status | Body (compact JSON, one LF) | Headers |
| :- | :- | :- | :- |
| `GET`, `POST`, `OPTIONS` on `/qa-hde-crd-0002-unknown`; `GET /api/qa-hde-crd-0002-unknown`; `GET /internal/qa-hde-crd-0002-unknown`; `GET /api/compat/v1` | 404 | `{"code":"ERR_NOT_FOUND","error":"not found","ok":false,"schema":"v1"}` | `application/json; charset=utf-8`; `Cache-Control: no-store`; no ETag |
| `HEAD /qa-hde-crd-0002-unknown` | 404 | empty | as above |
| `DELETE /internal/version` | 405 | the `ERR_NOT_FOUND` envelope | as above, plus `Allow: GET, HEAD, OPTIONS` |
| `GET /reader?v=1` | 403 | `{"code":"ERR_READER_FORBIDDEN","error":"reader endpoint disabled","ok":false,"schema":"v1"}` | as above |
| `HEAD /reader?v=1` | 403 | empty | as above |
| `POST /internal/dev/sampler`; `GET` on `/dev/sampler/conjunction`, `/dev/reader/conjunction`, `/dev/writer/conjunction` | 403 | `{"code":"ERR_WRITER_FORBIDDEN","error":"insufficient scope","ok":false,"schema":"v1"}` | as above |
| `GET /ops/probe/env`; `GET /ops/db/unavailable`; `POST /ops/writer/diagnostic` | 404 | the `ERR_NOT_FOUND` envelope | as above |
| `POST /api/reader?v=1` and `?v=2` with 32,768 bytes of `[` | 422 | `{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}` | as above |
| `GET /internal/version` | 200 | six keys, `release_id` the candidate's | `no-store`; no ETag |
| `OPTIONS /dev/sampler/conjunction` | 200, `text/html`, `Allow: GET, HEAD, OPTIONS` | empty | the router's automatic answer (LR5-O1; IR-3) |

## 7. Preapproval inspection ledger

Throwaway clones under this session's scratchpad, detached at `0b15328d`, with a CPython 3.12.3 venv holding CI's full install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; `pytest 8.4.2`). Every command ran under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1`, vendor and database keys unset, unless the row says otherwise. Nothing was committed or pushed; no vendor, production or database call was made. These rows validate the Plan's references and helper path (Glow QA Guide §3.4.8 "Entrypoint existence preflight" and "Execution-critical helper readiness"; §11.3 "Validated reference requirement"). They are not QA evidence.

| # | Command or probe | Result |
| :- | :- | :- |
| 1 | `tools/evidence/update_evidence_index.py --check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `check_lf_endings.py`; `scripts/release_id_recompute.py --check-manifest-only` | Each exit 0; tree clean afterwards (FND-033: with Flask installed, the two Flask-dependent validators run) |
| 2 | `pytest --collect-only -q` for every selector the Plan names | All resolve. Counts: check 2, three named nodes plus `-k qa_tool` 2; check 3, 11; check 4, 2; check 5, 7; check 6, 4; check 7, 27 plus 6 (the 33 of `tests/http/test_reader_a7_transport.py` and `tests/scripts/test_dev_start_reader.py -k "not verify"`); check 8, 2, 6, 4; check 9, 256; check 10, 247; check 12, 268; check 13, 137; check 14, 905 plus 4; check 21, 31, 1, 81. A first selector set placed `test_coverage_matches_the_binding_definition_and_the_guard_on_the_repository` in the wrong file and failed collection (exit 4); the Plan uses the corrected node in `tests/tools/test_prepush_check.py` |
| 3 | `hdctl --help`, `APP_ENV=dev` | Exit 0; the showcompat summary line present once |
| 4 | `hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json`; then `aux-preview` on that output | showcompat exit 0; every category band `Cool`. `aux-preview --pair-file <file> --category harmony --band Glow --show-narrative` equals the flag form `--category harmony --band Glow --perspective shared --show-narrative` and differs from the `Cool` output; with no `--band`, the output equals `Cool`'s. So the S08 predicate is observable on the operator CLI |
| 5 | Flask test client, `adapter.factory.create_app()` under `APP_ENV=prod` | The responses of §6 |
| 6 | Publication smoke in a second throwaway clone: two stand-in `CheckResult`s (one PASS from an executed `python -c "raise SystemExit(0)"` with an explicit open-rails `captured_env`, one `TOOLING_BLOCKED` with no command) published through `publish_crd_check_family`; then a third alone | Both publications succeeded; the manifest held all three checks (merge by `check_id`); the stored header carried the given open-rails `captured_env` though publication ran under closed rails. A fourth result whose `output` contained CR bytes was refused before any write ("CRD records require UTF-8 without BOM, and canonical LF bytes"), and the family stayed unchanged. Afterwards: `validate_crd_check_family` 3 checks; the five read-only validators each exit 0. The changed paths were the CRD root plus ten updater-owned graph files; `classify_paths` gave `evidence` and `release` |
| 7 | Interpreter facts | This container (Ubuntu 24.04) holds `/usr/lib/python3/dist-packages/setuptools` 68.1.2 (distribution-patched) with `_distutils_system_mod` not importable: the WU-PR-02 "E-DEB" condition is reproducible in an ordinary cloud container. `ruby`, `bash`, `curl`, `git` and `/usr/bin/python3.12` are present |
| 8 | Check 21's step-2 selectors, run in row 6's smoke clone with its stand-in `audit/qa/hde-crd-0002/` root (three stand-in checks) and updated graph present: `tests/evidence/test_evidence_index_missing_state.py -k crd`; `tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity`; `tests/qa/test_generic_qa_harness.py -k crd`; `tests/qa/test_epic021_acceptance_alignment.py::test_current_acceptance_inputs_are_strictly_viable` | 31 passed (about four minutes), 1 passed, 81 passed, 1 passed; the smoke clone's `git status` was the same before and after. A real root may present conditions a stand-in does not; check 21 is the proof |
| 10 | Check 9's CLI probes, `python -m engine.cli bg:resolve --user qa-hde-crd-0002-local1 --birthdate 1990-01-01 --birthtime 12:34 --location "Amsterdam, NL"` with: `--source vendor`; plus `--allow-prod-vendor HDE-CRD-0002/qa/qa-20-live-vendor-override`; plus `--allow-prod-vendor "bad ref"`; the flag twice; the flag with `--source db`. `XDG_STATE_HOME` an empty scratch directory; `APP_ENV=dev` | The first two exit 1 with a `status` `error` envelope, code `PROVIDER_REFUSED` ("Vendor source is refused under SAFE rails"), empty stderr. The other three exit 64 with empty stdout and one stderr line naming the rule, never the flag value. No file appeared under `XDG_STATE_HOME` |

## 8. Findings

None is a product defect. Each is a test, evidence or setup gap, a design point, or an authority boundary, with its owner.

| ID | Finding | Class | Treatment and owner |
| :- | :- | :- | :- |
| QA50-F01 | HTTP header captures carry CRLF; a `CheckResult` whose `output` holds a CR is refused at publication (§7 item 6) | Evidence-assembly gap | Plan rule: normalize CRLF to LF before assembling `output`, and record that normalization. Kronos (Plan) |
| QA50-F02 | `captured_env` defaults to the publishing process, and publication requires closed rails, so an open-rails step would be recorded with closed rails unless the step's own values are passed | Evidence-assembly gap | Plan rule: every `CheckResult` carries the step's actual six values explicitly. Kronos (Plan) |
| QA50-F03 | No test pins the full S07 summary sentence: `test_top_level_help_names_the_showcompat_stdout_contract` asserts the substring `magic10_compat_result.v1`, and `ci/checks/check_cli_help.sh` checks form only | Test gap, not a defect (the sentence is present, §7 item 3) | Check 4 asserts the exact sentence on the operator CLI output. A pinning test is a later-change candidate for the Product Owner |
| QA50-F04 | Plan Templates Step-0B requires the doc-delta pair `audit/docdeltas/<id>_doc_deltas.md` and `audit/qa/<id>/00_meta/doc_deltas.md`. The CRD publication interface cannot index a `00_meta/` file (HDE Mechanics Guide §1.6.3; §5 above), and Implementation Plan v1.1 WU-PR-07 has the close mutation set author `audit/docdeltas/hde-crd-0002_doc_deltas.md` at T1 | Canon tension | CR-11, `PROPOSED`, in the Plan's register. Interim: Step-0B content is carried in check 1's `primary.log`; QA writes neither file. Decision: Isis at QA-70 |
| QA50-F05 | G-1: the close writer needs an S01 `MET` row bound to a PASS check whose mapping names S01, yet S01 is removed | Close-stage design point | Check 15 proves the removal and its stated limit, and its mapping names S01 for that purpose only. Whether a `MET` row truthfully represents a removed requirement stays with the close mutation set and Isis, with the Product Owner if another route is needed. The Plan's mapping is not that decision |
| QA50-F06 | The live vendor call's initiator and venue are the Product Owner's choice, not yet stated; the code records the effective-UID account, not a person (IR-1, LR4-O2) | Authority boundary | The Plan defines two permitted venues and their evidence; QA-90 records the Product Owner's choice; the human initiator is attested in the evidence. Product Owner |
| QA50-F07 | FND-007: hosted CI never exercises the Debian path, and the only Debian proof is a pre-merge rehearsal on an earlier commit (WU-PR-02 plan v1.0 R-5, R-9) | Evidence gap | Decided: QA re-runs the build and verify on the candidate under a distribution-patched setuptools (check 3). The condition is available in an ordinary Ubuntu container (§7 item 7). Kronos |
| QA50-F08 | FND-004: S02's scope is "unknown non-compat paths" while its intent says "every 404" | Specification wording | Check 17 probes unknown paths at the root, under `/api/` and `/internal/`, all four methods at the root, a 405, and the production compat namespace. The Reader's unknown-person 404 is `ERR_M10_PERSON_UNRESOLVED` by canon (HDE CLI/API/Vendor Ref §5.2.3) and needs stored users that do not exist pre-App (Glow QA Guide §3.3); it is excluded |
| QA50-F09 | S20's acceptance intent names a `ci.yml` replay; FND-028 (removal of the replay report) is an open Product Owner decision | Scope boundary | Check 13 runs every report once as the delivered acceptance intent requires; it makes no recommendation on FND-028 |
| QA50-F10 | The first QA-evidence pull request selects the `evidence` and `release` lanes (§7 item 6); its hosted result is the remedy's measure (1) | Dependency | Recorded from GitHub by QA-110 and QA-120; not a check predicate. FND-024 (PR35-C1) and IR-7 stay named risks |
| QA50-F11 | Publication must run from the repository root of the evidence checkout, under closed rails, with Flask installed (the updater's `--check` imports it) | Setup requirement | Plan §5.4 "Publication procedure" |

**Integration risks IR-1 to IR-11 (Guide §9)** are each placed in the Plan: IR-1 (check 20 venue and attestation), IR-2 (no `showcompat --source vendor` in any production-like step), IR-3 (check 18 observation-only rows), IR-4 and IR-5 (no claim from the env guard or the dead hook), IR-6 (vendor evidence in `primary.log`), IR-7 and IR-8 (rerun classification and CI expectations), IR-9 (no Epic viability claim), IR-10 (no older generator run in write mode), IR-11 (G-1, check 15).

## 9. Data, permissions and safety

- **Data.** Synthetic only: the fixture charts `fixtures/charts/alice.json` and `fixtures/charts/bob.json`, the vendor tuple of §5, the QA user key `qa-hde-crd-0002-vendor1`, and non-existent request paths. No real person, user or production data.
- **Secrets.** Presence only (`SET`/`UNSET`); no value, raw header, token or vendor base URL value enters a log or record (`AGENTS.md` redaction rule; Glow QA Guide §3.5.7). Captured output is scanned before it enters evidence.
- **Production.** Read-only HTTP probes with fixed paths, each sent once, and one human-initiated dry-run vendor resolution. No deployment, configuration change, `--upsert`, database write, load or volume testing.
- **Repository.** Tests run only in throwaway clones (Specification constraint "Uncovered tests"; S19-R04). Evidence is written only by the canonical updater and lands by pull request; the Product Owner merges.

## 10. Planned versus delivered

No deviation affects testability. Recorded: S01 removed and the version cut withdrawn (delta 01; Plan delta 01); S10 narrowed to exact `dev` (CR-6, CR-8; addendum 2.7); S15 read under canon-retired exclusions (AD-1, CR-7); the deploy source is commits on `main` and the Ops task deploys nothing (P-9, P-18, P-19); WU-REM-01 added before QA-10 (addenda 2.23 to 2.25).

## 11. Open items and owners

| Item | Owner | State |
| :- | :- | :- |
| QA Plan v1.0 review | Isis (QA-70) | Next |
| CR-11 | Isis at QA-70 | PROPOSED |
| CR-9 | Isis (IA-30 boundary) | PROPOSED, unchanged |
| G-1 close representation of S01 | Close mutation set and Isis; Product Owner if a route beyond the writer is needed | Open |
| Venue and initiator for check 20 | Product Owner, recorded at QA-90 | Not stated |
| Evidence-only commit permission | Product Owner, at task execution | Requested in the Plan; not granted |
| FND-028, FND-029, FND-012, FND-022, FND-023, FND-034, FND-037, FND-038 | Product Owner | Pending, non-gating |
| QA50-F03 pinning test | Product Owner (later-change candidate) | Proposed |

## Canon relied on

Read on `main` at `0b15328d`.

| Topic | Sources and sections |
| :- | :- |
| Stage contract | QA-50 — Create Whole-Change QA Audit and Plan — 100926.1 (page state 2026-10-12T02:30:48.299Z), read in full |
| CRD QA applicability, roles, workflow | PF19-Canon-Glow-QA-Guide v3.0.6 §0.2 (read in full), §3.1, §3.1.1, §3.1.2, §3.1.3, §11.1 and §11.3 (read in full) |
| Rails, venue, vendor, Live QA classes | PF19 §2.3, §3.3, §3.4.8, §3.5.5, §3.5.6, §3.5.7, §3.5.10 (read in full) |
| Evidence layout and plan validity | PF19 §3.4.3 (with its path-grammar, migration and exception subsections), §3.4.4 to §3.4.7, §3.4.10, §3.4.11, §3.4.12 close-pack paragraphs, §3.4.13, §3.4.14, §4.4.1 to §4.4.7, §10.8 (read in full); §13.19 HDE-CRD-0001 record (read in full) |
| Plan template and header | PF27-Canon-Plan-Templates v2.0.5 "A) Glow Plan and Runbook Templates" §1 Live QA Plan from its front matter through "Check Blocks" and the CHECK template (lines 301 to 773, read in full) |
| CRD harness and publication | PF14-Canon-HDE-Mechanics-Guide v3.5.8 §1.6.3, lines 894 to 940 (read in full) |
| Override contract | PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11 to §7.1.11f (read in full) |
| Infrastructure | PF07-Canon-Glow-Infrastructure v2.3.3 §2.1, §2.2, §2.4, §2.5, §2.6, §2.7 (read in full) |
| Build Notes | PF10-HDE-Build-Notes v13.7.8: front matter and index; addenda 2.1, 2.2, 2.3, 2.7, 2.9 and 2.26 read in full; 2.10, 2.15, 2.16 and 2.17 read at their QA-relevant passages (Live QA classes, LR5-O1, LR7-O4, the close-run family, resolution A); 2.11 and 2.18 rules read |
| Approved scope | Specification v1.1-approved and delta 01; Implementation Plan v1.1 and Plan delta 01 v1.1 (as §1 states) |
| Precedent (not authority) | `docs/ephemeral/HDE-EPIC040-QA70-planning-failure-rca-v1.1.md` (read in full) |
| Repository rules | `AGENTS.md`: canon-first rule, closed rails, redaction rule, pytest readiness rule, pre-push check, QA output placement, governed evidence rules, evidence attribution, truncation guardrail, operating routes |

Searched (`git grep -n -i -E` on `origin/main -- docs/pfcanon/`): "Live QA", "Step-0B", "doc_deltas", "allow-prod-vendor", "7.1.11", "publish_crd_check_family", "Change-lane QA applicability". The governing hits are the sections above.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-50-20261024-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| unit | whole change; S01 (removed) and S02 to S22 |
| prompt | QA-50 — Create Whole-Change QA Audit and Plan — 100926.1, page state of 2026-10-12T02:30:48.299Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-50 phase 1 (QA_AUDIT) |
| capture time | 2026-10-24T02:27:05Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| earlier uses | QA-20 GCFPE-USE-HDE-CRD-0002-QA-20-20261024-01 (the Guide) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
