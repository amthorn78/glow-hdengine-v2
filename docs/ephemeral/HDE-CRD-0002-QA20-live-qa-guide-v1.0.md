---
artifact_type: LIVE_QA_GUIDE
artifact_id: HDE-CRD-0002-LIVE-QA-GUIDE
artifact_version: "1.0"
predecessor: none (the first Live QA Guide for HDE-CRD-0002)
state: GUIDE_READY
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Isis, continuing Lead Developer and whole-change readiness decision owner (Isis-53; https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok), the same session that issued QA-10 readiness v1.0 and v1.1
session_disposition: continuing Isis context, selected by the Product Owner's handoff
invocation_binding: CRD HDE-CRD-0002, QA-20 for the whole change, from QA_READINESS v1.1 (READY_FOR_QA); manual prerequisite #718 merged (verified as 2ff696b on main)
context_conflict: none
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
prompt: QA-20 — Create Live QA Guide — 100926.1 (https://app.notion.com/p/3f44590a05eb81289c7be77f66bac909; page state 2026-10-12T02:30:15.395Z, read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
QA_READINESS_ID: docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.1.md (READY_FOR_QA; blob 4338797f9bea)
REALITY_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-QA10-reality-audit-v1.1.md
CHANGE_AUDIT_TRIAGE_ID: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.1.md (40 findings; PF10_ADDENDUM_OUTPUT NOT_PRODUCED_BY_QA-10; blob 4f222c660dbb)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md, with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE; addendum 2.20)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (DELTA_APPROVE; addendum 2.19) and the FND-001 overlay P-1 and amended P-2 (addenda 2.23, 2.24)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (INITIAL_APPROVE), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (DELTA_APPROVE)
DOCUMENTATION_COMPLETION_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-documentation-completion-v1.1.md (COMPLETE)
OPS_TASK_RECEIPT: docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-receipt-v1.0.md (ACCEPT); evidence audit/ops/hde-crd-0002/wu-ops-01/
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (519,440 bytes; sha256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; addenda 2.1 to 2.26; read in full)
repository_baseline: origin/main 8908e1d (code identical to 3a5d846, the WU-REM-01 merge; runtime code identical to 45f045b, the WU-OPS-01 candidate)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-20
next_prompt: QA-50 — Create Whole-Change QA Audit and Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb815d89d3e602973d83ad), continuing Kronos
created_at: 2026-10-24T01:45:00Z
---

# HDE-CRD-0002 — Live QA Guide v1.0 (QA-20)

This Guide tells Kronos what HDE-CRD-0002 delivered, what independent QA must establish, and the constraints QA works under.
- **What it is not.** It is not the QA Audit, the QA Plan, a QA task, an evidence review or a report. It pre-approves no result and adds no approval gate.
- **What Kronos keeps.** Kronos audits the actual system and may find things this Guide does not name. Where this Guide describes a step, it states an obligation or a constraint, not a design; the QA Plan designs every step.

## 1. Readiness still holds

| Check | Result |
| :- | :- |
| Commits since the readiness inspection (`82b860c`) | `2ff696b` (#718, the three QA-10 v1.1 records, `docs/ephemeral/` only) and `8908e1d` (PF10 v13.7.7 → v13.7.8). `git diff --stat 82b860c 8908e1d` outside `docs/ephemeral/` and `docs/pfcanon/` is empty |
| PF10 v13.7.8 | Adds only addendum 2.26, which records QA-10 v1.1 (READY_FOR_QA; 40 findings; no new conflict). It states no objective failure and no new gate. Addenda 2.23 to 2.25 are byte-identical to v13.7.7 |
| Deployed runtime | `git diff --stat 45f045b 8908e1d` outside `docs/ephemeral/` and `docs/pfcanon/` touches only the six WU-OPS-01 evidence files, two test files and `tools/qa/qa_harness.py`. None is a release member or a runtime module, so the candidate WU-OPS-01 read (`release_id` `77204764…`, 2026-10-23T13:30:06Z) is still the runtime code on `main` |
| New evidence during this Guide | One close-stage design point (G-1, §8) and two QA-evidence integration facts (§7). None demonstrates a failed objective or invalidates readiness, so there is no return to QA-10 |

## 2. What was delivered

Twenty-one requirements are in scope. S01 is removed by Specification delta 01 and is not delivered. Release 1.3.0, 45 members, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (refreshed in place at the same version; no version cut).

| Req | Unit | Delivered behaviour on `main` | Source |
| :- | :- | :- | :- |
| S02 | WU-PR-03 | Unknown paths on the production app (`adapter.factory`, the `Procfile` app) and on `adapter.http_reader.create_app` answer 404 `ERR_NOT_FOUND` through `emit_public`, `Cache-Control: no-store`, no ETag, JSON; 405 the same envelope with an `Allow` header. Compat shaping and the production Reader's governed 405 are unchanged | Audit E-216 to E-221; IF-11 |
| S03 to S05 | WU-PR-01 | Every tracked test file runs in a CI lane or a full-validation target (215 files, 0 uncovered); 66 retirements in `tests/retired_tests.md`, each with a reason; unregistered `tools/qa/` `.py`/`.sh`/`.sql` sources fail classification; the workflow path filter equals the classifier's eight documentation prefixes | E-119 to E-134 |
| S06 | WU-PR-02 | The release-attestation builder's wheel stage detects distribution-patched setuptools and injects a scoped shim | E-315 to E-318 |
| S07 | WU-PR-03 | `hdctl --help` describes showcompat as "Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader" | E-256 |
| S08 | WU-PR-04 | `hdctl aux-preview --pair-file … --band B` emits band B; without `--band`, the file's band | E-266 |
| S09 | WU-PR-03 | The dev Reader harness is retired; `VERIFY.sh` uses the canonical runner and refuses unless `APP_ENV` is exactly `dev` (`VERIFY_APP_ENV_NOT_DEV`, exit 2) | E-104; addendum 2.6 |
| S10 | WU-PR-03, WU-PR-05 | Dev `GET`/`HEAD /reader` served only when `APP_ENV` is exactly `dev`; every other value, unset and empty refuse 403 `ERR_READER_FORBIDDEN`. In a production posture (`prod`, `production`, `live`, case-insensitive; or `ENGINE_ENV=prod` with `APP_ENV` empty) a registration-time hook also refuses the dev harness routes before their handlers | E-226, E-227, E-238; addenda 2.7 AD-2, 2.10 |
| S11 to S13 | WU-PR-02 | Engine-core evidence test fails on `release_id` drift; 22 current-release capture paths carry manifest-derived labels; the closure probe is root-bound | E-319 to E-325 |
| S14 | WU-PR-04 | `hdctl bg:resolve --source vendor --allow-prod-vendor <AUTHORIZATION_REF>`: HDE CLI/API/Vendor Ref §7.1.11a to §7.1.11f, read-only in production (every write refuses `PROVIDER_WRITE_UNSUPPORTED`), a 16-key `vendor_prod_override.v1` audit event durable before I/O | E-275 to E-288; IF-1, IF-2; addendum 2.9 |
| S15 | WU-PR-03 | The Endpoint Catalog has 18 records; 53 served pairs = 18 records + 35 reasoned exclusions; canon-retired `/ops` routes are excluded and refused by the validator | E-246; addendum 2.7 AD-1 |
| S16, S17 | WU-PR-08 | `.env.example` has `GEO_API_KEY=changeme` and is a classified surface; `docs/ADAPTER_009.md` readiness and port statements match the code | addendum 2.21 |
| S18 | WU-PR-03 | `docs/ADAPTER_009.md` says `invalid_json` for compat GET with a body; `ARCHITECTURE.md` states the emitter return types and the mounts | E-418 to E-423 |
| S19 | WU-PR-05 | The S19 record (`docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md`): nine findings fixed (S19-F01 to F09), seven routed to the Product Owner (S19-R01 to R07) | addendum 2.10 |
| S20 | WU-PR-06 | `tools/ci/prepush_check.py` with `lanes`, `membership`, `build-notes`, `sweep`, `replay`; read-only; replay pinned to the current `ci.yml` SHA-256 | addendum 2.12 |
| S21 | WU-PR-07 | The v2 close-pack writer (`tools/qa/generate_epic_close_pack.py`, `schemas/close_candidate_source.v2.json`) for Epic and CRD identities; the post-verdict close-run family `audit/qa/<crd>/close/<check_id>/primary.log`; the ADR approved with changes (AQ-1) | addenda 2.15, 2.16, 2.17 |
| S22 | WU-PR-02, WU-REM-01 | The canonical updater admits `audit/qa/hde-crd-0002/` (`ADMITTED_CRD_QA`); the evidence-lane tests no longer depend on whether that root, its close-run family, the close pack or the candidate source exist; the skeleton test and the QA harness accept `crd_id` | E-326, E-347 to E-352; addenda 2.23 to 2.25 |

## 3. Acceptance obligations and objective coverage

The criteria are the Specification's acceptance intents, as Specification delta 01 leaves them. Live QA class is the Specification's ("Production-affecting Live QA minimum" table) and Plan v1.1 §6; PF19 class is Glow QA Guide §3.5.6 (1 ops/identity, 2 internal functional/determinism, 3 vendor).

| Req | What QA establishes | Live QA class | Already evidenced (not re-proof) | Owed at QA |
| :- | :- | :- | :- | :- |
| S02 | Unknown paths on the deployed production app answer the governed envelope with `no-store`, never Flask HTML. Which 404s the live step exercises is the QA Plan's to state (FND-004: the production Reader's unknown person is a canon-defined `ERR_M10_PERSON_UNRESOLVED` 404, a different envelope) | Functional-feature; PF19 class 1/2 deployed check | Test client and tests (`tests/http/test_endpoint_catalog.py`); hosted CI | Deployed-target live step |
| S03 to S05 | Coverage, retirement ledger, owner refusal, filter equality | Not production-affecting | Hosted CI; PR-40 reviews; Audit N-106 to N-109 | Repository checks only |
| S06 | The attestation builds under Debian-patched setuptools | Not production-affecting | WU-PR-02 local rehearsal (exit 1 before, 0 after); hosted CI uses setup-python, so it does not exercise the Debian path | Whether to re-run the Debian reproduction is the QA Plan's (FND-007) |
| S07 | `hdctl --help` text | Functional-feature (operator CLI); PF19 class 2 | `ci/checks/check_cli_help.sh`; tests | A live step on the operator CLI surface the QA Plan names |
| S08 | `--band` applies with `--pair-file` | Functional-feature (operator CLI); PF19 class 2 | 9 tests; negative control NC-D | A live step on the operator CLI surface |
| S09 | Harness retired; `VERIFY.sh` behaviour | Not production-affecting | Tests; PR-40 checks 11, 12 | Repository checks only |
| S10 | Dev `/reader` refused in the deployed production target; exact `dev` gate | Functional-feature; PF19 class 1/2 deployed check | 16-value matrix tests; env-gate proof (fixed text from one `prod` probe, O-23) | Deployed-target refusal step; O-23 asks the QA Plan to treat the env-gate proof's evidence strength |
| S11 to S13 | Drift test, labels, root-bound probe | Not production-affecting | Tests; Audit E-319 to E-325 | Repository checks only |
| S14 | The production override behaves as §7.1.11a to f in the real production-like environment, including the authorized initiator and the audit event | Functional-feature; **mandatory live vendor call**; PF19 class 3 | Matrix tests M-1 to M-8, O-1 to O-7; black-box probes against a discard port (addendum 2.9) | The live vendor call (§5.1); the initiator and actor posture of the chosen venue (FND-011; LR4-O2) |
| S15 | Catalog entries only; no route removed | Catalog entries only | Enumeration test; catalog validator | Repository checks only |
| S16, S17, S18 | Template key; document statements | Not production-affecting | Addendum 2.21 statement map; Audit E-401 to E-423 | Repository checks only |
| S19 | The record exists and each fixed surface behaves at its class (S19 record §4 "Live QA class") | Inherits: F01 to F07 and the F08 loader are functional-feature; F05 and F06 fall in the S14 vendor class; the F08 cutter and F09 are not production-affecting | 268 `test_s19_*` cases; negative controls NC-01 to NC-18; PR-40 Flask test-client probes | Deployed-target steps for F01 and F03 at least; LR5-O1 observation (§9) |
| S20 | One read-only command with five reports | Not production-affecting | PR-40 runs on merged `main`, including `replay --full` | Repository checks only |
| S21 | The writer, close-run home and ADR | Not production-affecting | 905 writer tests; PR-40's two terminal-state rehearsals | The real close (after QA-120) is the business-case measure; §8 lists the formats QA artifacts must take |
| S22 | The canonical updater publishes and validates HDE-CRD-0002 QA evidence; Epic and HDE-CRD-0001 inputs still publish and validate | Not production-affecting | Hosted CI on `3a5d846`; PR-30 V-2 and PR-40 V-3 rehearsals | The first real publication under `audit/qa/hde-crd-0002/` (remedy measure (1)); measure (2) at the close-pack PR and the next qa-lane run |

**Production-affecting Live QA minimum** (Glow QA Guide §3.5.5; Change Process Guide §1.1.5A; Specification "Canon, QA & Build Notes posture"):
- The QA Plan includes at least one bounded open-rails live step in the deployed target.
- It includes a live vendor call under `SAFE_MODE=0`, `ALLOW_NETWORK=1`, with synthetic data only. One call satisfies the functional-feature class; inclusion of S02, S07, S08, S10 and S14 adds no second mandatory call.
- Closed-rails tests, fixtures, mocks, generated evidence, Index refreshes, the WU-OPS-01 identity read and a deployed-service check alone do not satisfy the vendor minimum.
- No S01 step or exemption is needed (Specification delta 01, C-12).

## 4. Delivered interfaces QA relies on

| Interface | Exact shape on `main` |
| :- | :- |
| Override flag (IF-1) | `--allow-prod-vendor <AUTHORIZATION_REF>`, only with `bg:resolve --source vendor`; value `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$`. Malformed, duplicated, inapplicable or after `--`: usage error, exit 64, value not echoed |
| Environment classification | `APP_ENV` canonical, `ENGINE_ENV` only when `APP_ENV` is blank; production-like `{prod, production, live}`, non-production `{dev, test, local, stage, staging}`; unknown, absent or conflicting → `PROVIDER_CONFIG_INVALID` before I/O |
| Matrix outcomes (exit 1, `outbound_attempted: false`) | closed SAFE rail → `PROVIDER_REFUSED`; network closed → `PROVIDER_NETWORK_BLOCKED`; production without the flag → `PROVIDER_PROD_OVERRIDE_REQUIRED`; non-production with the flag → `PROVIDER_PROD_OVERRIDE_INVALID`; actor or sink unavailable → `PROVIDER_AUDIT_UNAVAILABLE`; any write in production → `PROVIDER_WRITE_UNSUPPORTED` |
| Audit event (IF-2) | `engine/bodygraph/vendor_audit.py`: schema `vendor_prod_override.v1`, event `vendor_prod_override`, 16 keys; sink `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, else `$XDG_STATE_HOME/glow-hdengine/vendor_prod_override.jsonl`, else `~/.local/state/glow-hdengine/vendor_prod_override.jsonl`; a sink inside the repository or a relative sink refuses; append-only, `0600`, fsync of file and directories; actor = the effective-UID account name from the user database, never an environment value; an allowed call writes an `allowed` event before I/O and a state event (`completed` or `failed`) after it under the same `correlation_id` |
| Vendor configuration | `HD_API_BASE_URL` (canonical; `HDAPI_BASE_URL` only when it is absent; a conflict is `PROVIDER_CONFIG_INVALID`), `HD_API_KEY`, `GEO_API_KEY`. The base URL owns the vendor version; a v2 base selects the `charts` resource (`route_family` `recommended_v2_chart`) |
| Production posture (S19-F03) | Under `APP_ENV` production-like at registration: dev `/reader` 403 `ERR_READER_FORBIDDEN`; `POST /internal/dev/sampler` and `/dev/*/conjunction` 403 `ERR_WRITER_FORBIDDEN`; `/ops/probe/env`, `/ops/db/unavailable`, `/ops/writer/diagnostic` 404 `ERR_NOT_FOUND`; all `no-store` |
| Reader parse depth (S19-F01) | `POST /api/reader` with JSON nested past the parser's recursion limit → 422 `ERR_READER_INVALID_INPUT`, `no-store`; body limit 32 KiB |
| Deployed identity | `GET /internal/version` (and `HEAD`), `no-store`, no ETag; keys `engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id`. Only `release_id` identifies the deployment: `build_commit` is a fixed source value (`"9479d28"`, `engine/runtime/identity.py`) (addendum 2.19 P-9) |
| QA evidence writer | `tools.evidence.update_evidence_index.publish_crd_check_family(config, results, *, captured_at_utc=None, coherence_verifier=None)` with `tools.qa.qa_harness.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=<checkout>)` and `CheckResult` records. A Python API, not a CLI (HDE Mechanics Guide §1.6.3) |

## 5. Required live steps set by canon and approved decisions

### 5.1 The mandatory live vendor call (S14)

- **Command family.** `hdctl bg:resolve --source vendor --allow-prod-vendor <AUTHORIZATION_REF>` in a production-like environment with both rails open. The QA Plan designs the exact command, inputs and expectations.
- **Initiator.** An authenticated human Product Owner, or a human operations executor the Product Owner explicitly delegates in the referenced approved work item (Specification constraint "Override initiator"; HDE CLI/API/Vendor Ref §7.1.11e). An AI agent, CI job, application request or unauthenticated shell cannot self-authorize. Glow QA Guide §3.5.7's directed-agent rule does not waive this: §7.1.11's preamble says the directed-agent vendor rule neither implements nor waives the override contract.
- **Actor posture.** The actor is the effective-UID account. In a cloud container it resolves to `root` (LR4-O2). Whether the chosen venue yields a stable authenticated human principal is the QA Plan's question (Plan R-3; FND-011).
- **`AUTHORIZATION_REF`.** It names the approved work item or recorded Product Owner delegation, and never a token or secret.
- **Read-only.** The flag authorizes one bounded admin vendor HTTP opportunity. It does not authorize `--upsert`, any production database write or expanded retries. A production dry run that contacts the vendor still requires the flag (§7.1.11d).
- **Data.** Synthetic birth inputs only; no real person, user or production data.
- **Audit sink.** It must be outside the repository. The event is keys-only, so its fields may enter QA evidence (§7). The sink on an ephemeral host does not survive the host; the QA Plan states where the event is captured.
- **Vendor values.** They come from the environment only. Record `SET`/`UNSET`; never ask the Product Owner to type or paste a value (Glow QA Guide §3.5.7). A missing variable means no vendor call: `TOOLING_BLOCKED`, not a behaviour failure.
- **Bounds.** A defined request limit and stop checks; no load, stress or volume testing.
- **What it proves.** Only what it exercises: not full vendor conformance, QA PASS, deployment or closure.

### 5.2 Deployed-target steps (non-vendor)

- **Target.** The Railway production service, base URL `https://glow-hdengine-v2-production.up.railway.app` (Glow Infrastructure §2.2; WU-OPS-01 receipt). Production bindings are `APP_ENV=prod`, `SAFE_MODE=0`, `ALLOW_NETWORK=1` (§2.4; seven names recorded `SET` on 2026-10-23).
- **Owed:**
  - S02's unknown-path envelope;
  - S10's `/reader` refusal;
  - S19-F01's deep-JSON 422 and S19-F03's production posture;
  - a re-read of `/internal/version` against `release_id` `77204764…` (FND-032).
- **Classes.** These are PF19 class 1 or 2 deployed checks. Under Glow QA Guide §3.5.6 they are labelled pre-flight or internal and are not the Product Owner's Live QA workload; the vendor step is.
- **Deployment.** Deploys come from commits landing on `main` (Product Owner direction of 2026-10-21; addendum 2.19). QA performs no deployment and no configuration change.

### 5.3 Ops evidence QA consumes

`audit/ops/hde-crd-0002/wu-ops-01/` holds six files with a SHA-256 ledger and no path proof or Index row (CR-9, interim treatment (a)). When a QA check consumes it, that check's `primary.log` and its sibling path proof point to it rather than re-homing it (Glow QA Guide §11.1; FND-031). The Ops read is Ops evidence; it is not QA evidence unless the QA Plan defines how it feeds a check (§3.5.7).

## 6. Environment and setup

- **Interpreter and install.** Python 3.12, as CI uses. CI's full install, `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, then `python -m pytest --version`. Two read-only validators import Flask and fail without it (FND-025, FND-033).
- **Tools.** `ruby` (the HDAPI v2 contract-inventory test needs it and never skips; addendum 2.2), `bash`, `curl`, `git`.
- **Rails.** The default is closed: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1`. Open rails only for the step that needs them, recorded in that step's evidence.
- **Hazards:**
  - an editable install mapped to another checkout makes `hdctl` subprocess tests run the wrong code (OBS-W5-5);
  - six route-policy tests need `APP_ENV` set (OBS-P4-2);
  - `tests/adapter/test_jsonschema.py` leaks `ENGINE_ENV` when it runs first (OBS-P4-7);
  - point `XDG_STATE_HOME` at an empty scratch directory for local runs so no audit sink lands in a real state directory;
  - leave vendor, database and GitHub keys unset outside the vendor step.
- **Where tests run.** In a throwaway clone, never the working tree: uncovered or owner tools can rewrite tracked evidence (Specification constraint "Uncovered tests"; S19-R04).
- **Database.** `DATABASE_URL` is the only DB surface. Retired bridge keys are refused, including when empty.

## 7. Required evidence and indexing

- **Root.** `audit/qa/hde-crd-0002/` (Glow QA Guide "Change-lane QA applicability"; Plan invariant 6). Lower-case directories. No QA output in the repository root.
- **What the updater indexes under the root.** Exactly `qa_step_logs_manifest.json`, `checks/<check_id>/primary.log` and, after the verdict, `close/<check_id>/primary.log`, each with its path proof. `_load_crd_qa_entries` refuses any other row under the root ("CRD index key/path relationship is malformed").
- **Consequence.** Glow QA Guide §3.5.7's vendor sidecars (`vendor_request.txt`, `vendor_run1.json` and the like) cannot be indexed under the CRD root by the governed writer. §3.5.7 also treats vendor evidence that is present but not indexed as a QA failure. So the QA Plan either carries the vendor step's request description, outputs and notes in the check's `primary.log` (a `CheckResult`'s `command`, `output`, `captured_env` and `evidence_artifacts`), or routes the gap to its owner. QA-20 does not decide the design (IR-6).
- **Publication.** Only through `publish_crd_check_family`. It requires a coherent graph first (it runs the updater's `--check`), merges results into the existing manifest by `check_id`, and runs inside one recoverable transaction. Never hand-edit the Index, Mirror, sentinels, path proofs or orientation output.
- **Check IDs.** Lower-case, matching `[a-z0-9][a-z0-9._-]*`.
- **Statuses.** `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `PARKED`. An unavailable prerequisite is never `PASS`.
- **Read-only validation after publication:**
  - `tools/evidence/update_evidence_index.py --check`;
  - `tools/evidence/orientation_demo.py --check`;
  - `tools/evidence/validate_evidence_paths.py`;
  - `ci/checks/check_mirror_schema.sh`;
  - `tools/evidence/check_lf_endings.py`;
  - `tools.qa.qa_harness.validate_crd_check_family(config)`.
- **Each step records** the tested commit, interpreter, rails and environment (secrets as `SET`/`UNSET`), command, exit code taken from the producer's own status, outputs or digests, actor, time and limitations (AGENTS.md "Evidence attribution, currentness and distinct decisions"; the exit-status corollary of the truncation guardrail).
- **Landing.** QA evidence lands by pull request. Such a PR selects the evidence and release lanes (PR-40 of WU-REM-01, §8.1). The first such PR is the remedy's measure (1).

## 8. Close-stage formats the QA artifacts must take

The S21 writer reads QA artifacts by pinned names and forms (FND-030; LR7-O4; addendum 2.17). An artifact in another form cannot support an ordinary close on the first attempt.

| Artifact | Pinned form |
| :- | :- |
| QA plan | `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v<N>.<N>.md`; checks as `### CHECK <n>` headings, each followed by its check ID in backticks, in plan order (`QA_PLAN_CHECK_RE`); each check with a `Surface / D-goal mapping:` line naming the criteria it proves (`A to B` names a range) |
| QA report | `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v<N>.<N>.md`; front matter `artifact_type: QA_REPORT`, `change_id: HDE-CRD-0002`, `verdict` |
| QA ledger | `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` in the harness's own bytes; each primary's header agrees with it |
| SATISFIED | Needs the report's `verdict: PASS`. Every planned check must be `PASS`, or `TOOLING_BLOCKED` named once by a closure-override gap (addendum 2.17 resolution A). Every requirement ID needs a `MET` row bound to a `PASS` check whose plan mapping names it |

**G-1 (close-stage design point; for Kronos and the close owners).** The writer takes the requirement IDs from the change's highest `-specification-v<N>.<N>-approved.md` file: `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, whose table still has the S01 row (`CRD_REQUIREMENT_RE`; `_requirement_ids`). Specification delta 01 is a separate file the writer does not read.
- **The effect.** A SATISFIED close of HDE-CRD-0002 needs an S01 `MET` row bound to a `PASS` check whose plan mapping names S01. Yet S01 is removed and not delivered.
- **What is already decided.** The writer renders the criterion ID, result and the row's `limitation` text; it does not copy criterion text ("criterion text is not copied"). How the plan maps S01 is a QA-50 design point (FND-030).
- **What is not decided.** Whether a `MET` row for a removed requirement is a truthful representation, or whether the close needs another route, is not decided here. Owners: Kronos (QA-50 mapping), then the close mutation set and Isis at closure, with the Product Owner if a route beyond the writer's pinned forms is needed.
- **Why it is not a readiness failure.** It does not block QA execution, and the writer behaves as AQ-1 C-2 approved.

## 9. Integration risks

| ID | Risk | Why it matters | Source |
| :- | :- | :- | :- |
| IR-1 | The override's actor in a container or shared shell is an account (`root`), not a person | The initiator rule is a human; code cannot tell a human from an agent | LR4-O2; FND-011 |
| IR-2 | Production rails are open by default, and `hdctl showcompat --source vendor` and conjunction acquisition have no production override gate | A showcompat vendor step in a production shell reaches the vendor without the S14 gate or audit event. It is not the S14 proof | S19-R01; FND-012 (Product Owner) |
| IR-3 | Router-level answers come before the production hook: automatic `OPTIONS` on dev-harness paths returns 200 with `Allow`; a doubled-slash path gets 308 to the canonical path, which then refuses | Canon is silent on `OPTIONS` and redirects for these paths; a live probe seeing them is not a defect on its own | LR5-O1 (Product Owner doc-delta candidate) |
| IR-4 | The env guard reads `app.config`, not the process environment, and `adapter.factory` does not call it | Do not claim the guard's protection from a live probe | LR8-F1; FND-023 |
| IR-5 | `adapter.http_reader.create_app`'s after-request hook runs and its branches never match | Do not rely on it in a dev-runner probe | AD-4 item 4; LR3-O2; FND-022 |
| IR-6 | The CRD index admits only primaries and the manifest under the root | Vendor sidecars cannot be indexed (§7) | `update_evidence_index.py` `_load_crd_qa_entries` |
| IR-7 | Intermittent hosted test failures: `tests/tools/test_prepush_check.py` (git auto-maintenance race) and `test_manifest_reader_rejects_new_report_with_old_manifest` (mechanism unknown) | A QA-evidence or close PR may see an unrelated red; classify before rerunning | PR35-C1 (FND-024); OBS-17, LR6-O8, LR7-O13 |
| IR-8 | `tests/evidence/test_hdapi_v2_contract_inventory.py` failed 9 tests in one local environment; hosted CI last ran it green | A full-validation run includes it; a QA-evidence PR does not | OBS-2; FND-037 |
| IR-9 | 12 of 16 Epic acceptance maps are `FAIL_TOOLING` through the harness on `main` | Not an HDE-CRD-0002 objective; do not read it as an S22 regression | OBS-1; FND-038 |
| IR-10 | Older vendor evidence generators (`generate_hde_epic036_bg_resolve_route_policy.py`, `generate_hde_epic037_*`) fail `--check` on `main` | They are not validation entrypoints for this change; never run them in write mode | AGENTS.md "EPIC037 docs posture"; OBS-P4-3 |
| IR-11 | The writer requires the removed S01 among its requirement IDs | Close-stage design point | G-1 (§8) |

## 10. Known limitations and baseline

- **Packaging.** S01 is not delivered: a regular wheel install outside a source checkout does not admit the release. The packaging covers 29 of 45 members (stated limit, FND-026). Production starts from the checkout.
- **Debian proof.** S06's Debian proof is a local rehearsal (FND-007).
- **Fixed `build_commit`.** It is a fixed value; deployment is judged by `release_id` alone.
- **The WU-OPS-01 read.** It is one read from the executor's network at 2026-10-23T13:30:06Z; variable presence only, not value correctness.
- **Routed findings, open with the Product Owner:**
  - S19-R01 to R07 (FND-029);
  - X-02;
  - the option A stop-rule decision on the replay report (FND-028);
  - the legacy chart-loader defect (addendum 2.2, HDE-SEPA006).
- **Documentation deltas outstanding** (not QA defects):
  - FND-017 to FND-020;
  - FND-040, HDE Mechanics Guide §1.6.3 still naming only HDE-CRD-0001;
  - HDE CLI/API/Vendor Ref §7.1.11's "Required-Now implementation gap (DD-04; held)" paragraph, stale since S14 landed (Specification "Affected canon and intended drainage targets").
- **Not reopened by the Specification** (no QA obligation): live Gate readiness and live Reader success (HDE-COAG003.8, .9), RA-11, RA-15, RA-16, O-OPS01-02 and the others in its "Not reopened" list.
- **HDAPI v2.** No broad HDAPI v2 runtime conformance is claimed. Non-dry-run v2 mapped-cache writes remain unproven (Glow QA Guide §3.5.7).

## 11. Permitted and forbidden actions; data handling

| Permitted | Forbidden |
| :- | :- |
| Tests, CLI runs, local servers and read-only tools under closed rails, in throwaway clones | Editing product code, tests, schemas, catalog, manifest, workflows or governed evidence; a release cut |
| The bounded live vendor call of §5.1, Product Owner-authorized, human-initiated, synthetic data, request-limited | `--upsert`, any production database write, backfill or migration; load, stress or volume testing |
| Read-only GET/HEAD/POST probes of the deployed service with synthetic or non-existent identifiers | Real person, user or production data in any request; a live Reader success claim |
| QA records under `audit/qa/hde-crd-0002/`, published by the canonical writer, landed by pull request | Hand-written Index, Mirror, path proof, manifest or orientation bytes; files in the repository root |
| Reading production variable names as `SET`/`UNSET` | Recording any secret, token, key, raw header value or vendor base URL value; asking the Product Owner to paste one |
| Consuming WU-OPS-01 evidence by reference | Deployment, production configuration change, PF-canon or PF10 edits, merges |

**Data handling:**
- Keys-only logs.
- Scan captured output for secrets before it enters evidence.
- Vendor responses: no raw payload persistence beyond what the governing contract allows (mapped, no raw vendor payload).
- The audit event's fields are keys-only by design. Copy them, not the host's other state.

## 12. Recovery expectations and failure classification

- **Behaviour contradiction.** `FAIL_BEHAVIOR` with evidence. An objective failure goes to its owner route through QA review and escalation; it is not fixed in QA.
- **Tooling or environment failure.** `FAIL_TOOLING` or `TOOLING_BLOCKED`. One bounded ordinary-lane rerun applies under an unchanged valid Plan (QA-50 "Execute" phase 2 item 4); never edit product files to pass.
- **Open-rails failure.** Classify it before acting: credential, configuration, vendor account or tier, endpoint unavailability, vendor contract mismatch, request-shaping, response-mapping, infrastructure, rate-limit, outage, product defect or QA expectation mismatch (Glow QA Guide §3.5.7). A wrong auth-header family is a request-shaping or setup failure.
- **Missing prerequisite.** A missing vendor or database prerequisite leaves the step blocked, never passed.
- **Unindexed evidence.** Missing indexing is incomplete work for the authorized writer. It is not a reason to rerun valid QA (QA-50 "Required QA evidence indexing").
- **Rollback.** If a live step leaves the deployed service in doubt, the only Ops action available is the WU-OPS-01 rollback intent (redeploy the previously deployed commit), and that action is the Product Owner's.

## 13. PF10 lineage and canon-conflict register

- **PF10.** `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md`, read in full.
- **Addenda that bear on QA:**
  - 2.1 (TypeSafe readings);
  - 2.2 (ruby dependency);
  - 2.3 (no Codex security review in the chain);
  - 2.7 AD-1 to AD-5 (catalog, exact gate, runner profile);
  - 2.9 (S14, LR4-O2);
  - 2.10 (S19 and LR5-O1);
  - 2.11 as narrowed by 2.18 (business case and real inputs; no ceiling);
  - 2.13 (closeout-validation install; T7);
  - 2.14 (P1 rule);
  - 2.15 and 2.17 (ADR, close-run family, SATISFIED rule);
  - 2.16 (LR7-O4);
  - 2.19 and 2.20 (deltas; deploy source; `build_commit`);
  - 2.21 (PR35-C1, LR8-F1);
  - 2.22 (WU-OPS-01);
  - 2.23 to 2.25 (FND-001 remedy);
  - 2.26 (QA-10 v1.1).
- **Register.** `CANON_CONFLICT_REGISTER`, carried unchanged from QA readiness v1.1 §6:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `…-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same §3 |
| CR-6 | APPROVED, alternative (a) | IA through RS-20 | addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner, 2026-10-14 | addendum 2.7 |
| CR-9 | PROPOSED, not yet reviewed | Isis, at IA-30; not a QA-20 decision | `…-WU-OPS-01-ops-task-v1.0.md` §13; interim treatment (a) |
| CR-10 | APPROVED, alternative (a); applied | Isis, ESC-40 | remediation review v1.1 §4; addendum 2.24 |

**No new conflict.**
- G-1 is a close-stage design point, not a conflict: the writer applies AQ-1 C-2 as approved, and Specification delta 01 is approved.
- IR-6 is a gap between Glow QA Guide §3.5.7's schematic sidecars and the CRD publication interface (HDE Mechanics Guide §1.6.3, which does not permit arbitrary additional files). The QA Plan resolves it within the primary log or routes it.

## 14. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| QA Audit and QA Plan | Kronos (QA-50); Isis reviews (QA-70) | Next |
| Kronos session for HDE-CRD-0002 | Product Owner | `NOT_YET_ASSIGNED`: no Kronos session for this change is on record (Kronos-23's session served HDE-EPIC040) |
| The live vendor call's initiator and venue | Product Owner, through the QA Plan | Pending |
| G-1 (S01 at the close) | Kronos for the mapping; the close mutation set and Isis at closure; Product Owner if a route beyond the writer is needed | Open |
| IR-6 (vendor sidecars) | Kronos (QA Plan design) | Open |
| CR-9 | Isis, IA-30 | PROPOSED |
| FND-028, FND-029, FND-012, FND-022, FND-023, FND-034, FND-037, FND-038 | Product Owner | Pending, non-gating |
| Documentation and canon drainage (FND-017 to FND-021, FND-040, CR-10, §7.1.11 status paragraph) | Product Owner | Unperformed, non-gating |
| Remedy measures (1) and (2) | The first QA-evidence PR; the close-pack PR and the next qa-lane run on `main` | Not yet measurable |
| Closeout-validation job's first hosted run (T7) | The close mutation set; the Product Owner dispatches | Due at the close |

## 15. TypeSafe reading for the receiving session (QA-50)

Action sent (v8.2): "As the independent QA authority for one change, author one new whole-change QA audit and then one new QA plan for 21 in-scope requirements delivered by eleven accepted work units, from a Live QA guide, three readiness records and the approved specification and plan; the plan defines a few dozen QA checks, each separately verifiable, including a few bounded probes of the deployed service and one mandatory human-initiated live vendor call, with evidence publication through the repository's canonical evidence writer. It is a Markdown record only: no task list exists yet, no live run against a provider occurs here, and an independent plan review follows."

- **TypeSafe v8.2: Opus 5.5 at extra high.**
  - Effort score 2.93 (confidence 0.38). Rung probabilities: low 0.00, medium 0.01, high 0.36, extra high 0.34, max 0.29, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.29, Opus 5.5 0.42, Sonnet 5.5 0.29, Haiku 5.5 0.00 (confidence 0.23).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.003, Fable 5.1 at high 0.104, Fable 5.1 at extra high 0.099, Fable 5.1 at max 0.084, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.004, Opus 5.5 at high 0.151, Opus 5.5 at extra high 0.143, Opus 5.5 at max 0.122, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.003, Sonnet 5.5 at high 0.104, Sonnet 5.5 at extra high 0.099, Sonnet 5.5 at max 0.084, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - **Flags: boundary between extra high and high; model near tie between Opus 5.5 and Fable 5.1.**
  - Sent 2026-10-24T01:39:49Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-24T01:39:49Z; HTTP 200 in 0.63 s; 5466 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review`, before this Guide was saved.
- **Records:** the Notion row was not written.
- **Picks:** Nathan's pick for QA-50 is not stated. Nathan's pick for this QA-20 session is not stated; its reading is in QA readiness v1.1 §8 (Sonnet 5.5 at high, score 1.92).

**Surface advice:** run QA-50 as a top-level Claude Code cloud session that Nathan creates for Kronos on `amthorn78/glow-hdengine-v2`. No Kronos session for HDE-CRD-0002 exists yet.
- **Reads:** Notion read access for the QA-50 prompt; this Guide, the three QA-10 v1.1 records, the Specification and Plan with their overlays, PF10 v13.7.8 and the Glow QA Guide in `docs/pfcanon/`; the S19 record; the delivered loci named in §4.
- **Optional checks while auditing:** a throwaway clone with CI's full install on Python 3.12, `ruby`, `bash` and `curl`, under closed rails.
- **Writes:** only the QA Audit and QA Plan under `docs/ephemeral/`, through their own pull request. The QA Plan follows §8's pinned path.
- **Not needed:** production, vendor, Railway and database access belong to QA execution, not to the Audit and Plan.
- **Order:** this Guide's pull request is merged first.

## Canon relied on

Read on `main` at `8908e1d`.

| Decision topic | Sources and sections |
| :- | :- |
| Guide operation, contents, states and routing | QA-20 — Create Live QA Guide — 100926.1 (page state 2026-10-12T02:30:15.395Z), read in full: "Required QA evidence indexing", "Required inputs", "Controlled PFCanon, immutable base, and PF10 overlays", "Execute" 1 to 5, "Required result and routing", "Runtime artifact and handoff contract" |
| Receiver intake | QA-50 — Create Whole-Change QA Audit and Plan — 100926.1 (page state 2026-10-12T02:30:48.299Z), read in full: "Required inputs", "QA authorship and Product Owner execution choice", "QA operation semantics and evidence", "Execute" |
| Workflow placement; CRD applicability; roles | PF19-Canon-Glow-QA-Guide v3.0.6 §0.2 "Change-lane QA applicability" (read in full), §3.1, §3.1.1, §3.1.2, §11.1 (read in full); PF04-Canon-HDE-Governance v2.8.7 §9.1.1 authority table (row "Whole-change readiness and Live QA Guide": continuing Isis) and §9.1.5 readiness table, read; PF14-Canon-HDE-Mechanics-Guide v3.5.8 "Objective-first Live QA Plans (directive posture)" bullet 4 (Live QA Guides belong to the post-implementation QA workflow), read |
| Step rails | PF04-Canon-HDE-Governance v2.8.7 §9.8.1 "Scope" (the rails apply to any document that defines stepwise QA execution, Live QA Guides included) and §9.8.2 (deliverables per step), read. This Guide defines no executable step; the QA Plan does, and these rails bind it |
| Live QA classes, minimum, vendor evidence | PF19-Canon-Glow-QA-Guide v3.0.6 §3.5.5, §3.5.6, §3.5.7 (read in full); PF06-Canon-Change-Process-Guide v2.5.4 §1.1.5A (read in full) |
| Production override contract | PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11 to §7.1.11f (read in full) |
| CRD publication interface | PF14-Canon-HDE-Mechanics-Guide v3.5.8 §1.6.3, lines 894-926 (read in full in the QA-10 reassessment, unchanged since); `tools/evidence/update_evidence_index.py` `_load_crd_qa_entries` and `publish_crd_check_family`, `tools/qa/qa_harness.py` `CheckResult`, `record_check_family`, `validate_crd_check_family`, read as repository fact |
| Close-stage forms | PF10 addenda 2.15, 2.16 (LR7-O4), 2.17; `tools/qa/generate_epic_close_pack.py` (`APPROVED_SPECIFICATION_RE`, `_requirement_ids`, the SATISFIED checks, the acceptance rendering), read as repository fact |
| Build Notes | PF10-HDE-Build-Notes v13.7.8, read in full (front matter, index, addenda 2.1 to 2.26) |
| Approved scope and objectives | Specification v1.1-approved: Requirements, Exclusions, Constraints, Phase blocks, "Canon, QA & Build Notes posture" (read in full); Specification delta 01 (read in full); Implementation Plan v1.1 §3 to §15 (read); Plan delta 01 v1.1 P-1 to P-20 (as addendum 2.19 reproduces them) |
| Fixed surfaces' classes | `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` §4 (read in full) and §7 row O-23 |
| Evidence and redaction rules | AGENTS.md "Governed evidence rules", "Redaction rule", "QA output placement", "Pytest readiness rule", "Evidence attribution, currentness and distinct decisions", the truncation guardrail, "EPIC037 docs posture" |
| Infrastructure facts | PF07-Canon-Glow-Infrastructure v2.3.3 §2.2 and §2.4, as the WU-OPS-01 receipt and addendum 2.22 cite them (base URL and bindings), not re-read here |

Searched (`git grep -l -i -E` on `origin/main -- docs/pfcanon/`):
- "Live QA Guide" hits PF04, PF10, PF14, PF19 and PF20;
- "QA-20" hits PF04, PF10 and PF19;
- "Live QA minimum" and "functional-feature" hit PF10 and PF19;
- "Change-lane QA applicability" hits PF19;
- "1.1.5A" hits PF06;
- "7.1.11" hits PF05 and PF10.

The governing hits are the sections above. PF20's hit (an EPIC021 Live QA guide rule) is historical reference only. Canon names no format for a Live QA Guide beyond the QA-20 prompt; the HDE-EPIC040 Guide (`docs/ephemeral/HDE-EPIC040-QA20-live-qa-guide-v1.0.md`) was read as precedent only.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-20-20261024-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| unit | whole change; S02 to S22 |
| prompt | QA-20 — Create Live QA Guide — 100926.1, page state of 2026-10-12T02:30:15.395Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | continuing Isis, QA-20 |
| capture time | 2026-10-24T01:45:00Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-10-20261023-01 (v1.0); GCFPE-USE-HDE-CRD-0002-QA-10-20261024-02 (v1.1) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |
