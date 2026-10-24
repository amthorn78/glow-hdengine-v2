---
artifact_type: QA_PLAN
artifact_id: HDE-CRD-0002-QA50-QA-PLAN
artifact_version: "1.0"
predecessor: none (the first QA Plan for HDE-CRD-0002)
state: PLAN_PENDING
approval_sentinel: "ASK OK?"
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
plan_type: Whole-change QA Plan and Live QA runbook
author: Kronos, the QA authority for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
reviewer: Isis, continuing Lead Developer, through QA-70 — Review Whole-Change QA Plan — 100926.1
prompt: QA-50 — Create Whole-Change QA Audit and Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb815d89d3e602973d83ad; page state 2026-10-12T02:30:48.299Z)
prompt_release: GCFPE-20261009.1 / 100926.1
QA_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE; same invocation)
LIVE_QA_GUIDE_ID: docs/ephemeral/HDE-CRD-0002-QA20-live-qa-guide-v1.0.md
QA_READINESS_ID: docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.1.md (READY_FOR_QA)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md, with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE; addendum 2.20)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (DELTA_APPROVE; addendum 2.19) and the FND-001 overlay (addenda 2.23, 2.24)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (sha256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-50
repository_head_read: origin/main 0b15328d585a764c124936b4524b766525daf1d9
canon_conflict_register: CR-1 to CR-10 carried; CR-11 PROPOSED (§13)
created_at: 2026-10-24T02:36:06Z
next_prompt: QA-70 — Review Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf), continuing Isis
---

# HDE-CRD-0002 — Whole-Change QA Plan v1.0 (QA-50, phase 2)

**State: `PLAN_PENDING`.** This Plan awaits Isis's QA-70 review. It authorizes no execution until approved, and approval of it is not a QA result. It is built on the QA Audit v1.0 (`docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md`), whose §5 to §7 hold the repository facts and the preapproval inspection ledger that back every path, test node and expected value named here (Glow QA Guide §11.3, "Validated reference requirement").

## 0. Runbook header (Plan Templates, Live QA Plan front matter)

| Field | Value |
| :- | :- |
| Change ID | HDE-CRD-0002 |
| Plan type | Live QA Plan / Runbook, whole change |
| Execution venue | Not fixed by this Plan. Four environment classes (§3.2) bind each check; the Product Owner chooses executor, tools and venue within them (§2) |
| Venue-specific claim | Check 20 only: the vendor call's actor principal and its audit sink depend on the venue (§3.2, E-V) |
| Why venue can affect the result | The override records the effective-UID account of the shell that runs it (IR-1); an ephemeral host does not keep the sink |
| Required venue evidence | Check 20's preflight rows P1 to P5 |
| Effect of missing venue evidence | Check 20 is `TOOLING_BLOCKED`; no vendor call runs |
| Target environment | Local/offline for checks 1 to 15 and 21; the Railway production service for checks 16 to 19; a production-like CLI environment for check 20 |
| Plan revision | r1 |
| Date (UTC) | 2026-10-24 |
| Operators (names-only) | Product Owner; authorized execution operator or session; Kronos (evidence review) |

Canon precedence (Plan Templates, "Canon precedence for template use"): applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

**Canon set** (titles only): HDE Build Notes; HDE-Governance §9.1.1, §9.8; Change Process Guide §0.4.1, §1.1.5A; HDE-CLI-API-Vendor-Ref §5.2, §5.4, §5.5, §5.6, §5.11, §5.12, §7.1.11 to §7.1.11f; HDE-Schemas & Artifacts §8.3, §8.17; HDE-Mechanics Guide §1.6.3; Glow Infrastructure §2.2, §2.4, §2.6, §2.7; Glow QA Guide §0.2, §2.3, §3.3, §3.4.3 to §3.4.14, §3.5.5 to §3.5.7, §3.5.10, §4.4, §10.6, §10.8, §11.1, §11.3; Plan Templates "A) Glow Plan and Runbook Templates" §1. PF09 mapping: none (Specification, "No PF09 mapping of this work").

**PF10 overrides.**
- Addendum 2.20 (Specification delta 01) → S01 removed, release kept at `1.3.0` → this Plan proves the removal (check 15), not delivery.
- Addendum 2.19 (Plan delta 01) → deployment is by commits landing on `main`; WU-OPS-01 deploys nothing → QA performs no deployment and judges the deployed candidate by `release_id` alone.
- Addendum 2.17 resolution A and 2.16 LR7-O4 → the close writer's pinned plan and report forms → this file's name, `### CHECK` headings and mapping lines (§7).
- Addendum 2.11 rules 4 to 6 (real inputs; no emulation) → every probe input here is one a user, operator or attacker can supply through an exposed interface, or a tracked fixture; no external system is emulated.
- Addendum 2.1 → §15's TypeSafe reading.

## 1. Scope

**In scope.** The twenty-one acceptance intents S02 to S22 of the approved Specification, as delta 01 leaves them, plus a removal check for S01 (§7 check 15; G-1). Requirement-to-check coverage is in §10.

**Excluded** (Specification Exclusions and "Not reopened"; Guide §10):
- live Gate readiness and live Reader success (HDE-COAG003.8, .9), and the Reader's unknown-person 404 (needs stored users that do not exist pre-App; Glow QA Guide §3.3; FND-004);
- `hdctl showcompat --source vendor` or conjunction vendor acquisition in any production-like step (S19-R01 is routed to the Product Owner; IR-2);
- any `--upsert`, production database write, mapped-cache persistence, deployment, configuration change, load, stress or volume testing;
- historical Epic acceptance-map viability as an objective (FND-038; IR-9), and the older vendor evidence generators in write mode (IR-10);
- re-running the full CI matrix: hosted CI ran it on the tested code (push run 39699657729 on `1a4c8ab`, all seven lanes; push run 40043995165 on `3a5d846`, evidence and qa), and the Plan cites it rather than replicating closed-rails surfaces (Glow QA Guide §3.4.8).

## 2. Candidate and execution arrangement

**Candidate.** `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (release `1.3.0`, 45 members). Tested source: the commit on `main` at execution whose code outside `docs/ephemeral/` and `docs/pfcanon/` equals `0b15328d`'s (that code equals `3a5d846`'s; Audit §2). Check 1 records the exact commit and enforces this guard.

**Execution arrangement.** The Product Owner has not stated a choice at QA-50. QA-90 records the Product Owner's choice of executor, tools and venue for each task. This Plan requires no executor name, platform or session identity, and does not bar Kronos from executing if the Product Owner chooses it. Two limits bind every arrangement:
- **Check 20's vendor commands** are initiated by an authenticated human: the Product Owner, or a human operations executor the Product Owner delegates by name in the approved QA-90 task (HDE CLI/API/Vendor Ref §7.1.11e; Specification constraint "Override initiator"). An agent may prepare the command text and assemble the evidence afterwards; it does not run steps V1 and V2.
- **Execution authority is not acceptance authority.** Evidence returns to Kronos (QA-110); Isis keeps closure.

**Evidence-only commit permission (requested; bounded; effective only when the Product Owner grants it at task execution).** If granted, the executor may commit and push only: `audit/qa/hde-crd-0002/**`; the ten updater-owned graph files `docs/evidence/INDEX.json`, `docs/evidence/INDEX.json.path_proof.txt`, `docs/evidence/INDEX.sha256`, `docs/evidence/INDEX.sha256.path_proof.txt`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.path_proof.txt`, `artifacts/evidence_index.jsonl.sha256`, `artifacts/evidence_index.jsonl.sha256.path_proof.txt`, `audit/gates/topology/orientation_demo.txt`, `audit/gates/topology/orientation_demo.txt.path_proof.txt`; and its own QA-100 result record under `docs/ephemeral/`. On one evidence branch, through a pull request. No other path, no merge, no force-push. Without the grant, the Product Owner commits.

## 3. Environment and rails posture

### 3.1 Determinism pins and rails

- **Pins** when producing governed bytes: `LC_ALL=C`, `LANG=C`, `TZ=UTC` (Plan Templates "Determinism pins"). No other pin is required. `PYTHONDONTWRITEBYTECODE=1` is set for local runs as hygiene only.
- **Default rails** for this runbook: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev` (the Development binding, Glow Infrastructure §2.4; Glow QA Guide §2.2.6).
- **Rails change by check** (one pair per check; changes only between checks; never a mixed pair):

| Checks | Rails | Why | Evidence it produces |
| :- | :- | :- | :- |
| 1 to 15, 21 | Default (closed; `APP_ENV=dev`) | Local/offline proof of repository behaviour (Glow QA Guide §3.3, §3.4.8) | `primary.log` per check |
| 16 to 19 | Production binding: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=prod` | Steps that touch production endpoints run with open rails (Glow QA Guide §3.4.8); the binding is PF07's Production row. Only `curl` runs; no product code runs on the client | Deployed-target transcripts |
| 20 | Production binding, as above | The mandatory live vendor call (Glow QA Guide §3.5.5; Plan Templates "Open-Rails Live QA Requirement") | The vendor transcript and audit events |

After check 20 the operator restores the default rails before any other check. **Publication** of every check, including 16 to 20, runs under the default closed rails (the updater requires them); each `CheckResult` carries the step's own rails explicitly (§5.3).

### 3.2 Environment classes

| Class | Definition | Used by |
| :- | :- | :- |
| E-L (local/offline) | A throwaway clone of `amthorn78/glow-hdengine-v2` detached at the tested source, never the evidence checkout; CPython 3.12 with CI's full install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` from the clone, then `python -m pytest --version`); `ruby`, `bash`, `curl`, `git` on `PATH`; default rails; `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DATABASE_URL`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and `ENGINE_ENV` unset; `XDG_STATE_HOME` pointed at an empty scratch directory outside the clone, for example `/tmp/hde-crd-0002-xdg-state` (Guide §6 hazard; the delivered sink reads it) | 1 to 15, 21 |
| E-D (Debian backend) | E-L plus a second venv made with `/usr/bin/python3 -m venv --system-site-packages /tmp/hde-crd-0002-qa03/venv` (outside every repository), whose `setuptools` imports from `/usr/lib/python3/dist-packages` and in which `_distutils_system_mod` is not importable, holding `-r requirements.txt -r requirements-dev.txt` and no `-e .` (the WU-PR-02 "E-DEB" condition; Audit §7 item 7) | 3 |
| E-P (production client) | Any shell with HTTPS egress to `https://glow-hdengine-v2-production.up.railway.app` (Glow Infrastructure §2.2, §2.7) and `curl`; Production binding recorded | 16 to 19 |
| E-V (vendor venue; the Product Owner chooses one) | **V-A, operator console:** the Product Owner's own shell (local terminal or Codespace) holding a clean clone at the tested source with CI's full install, whose environment already holds `HD_API_KEY`, `GEO_API_KEY` and `HD_API_BASE_URL`; the step's Production binding set for check 20 only. **V-B, production service shell:** a shell attached to the Railway service `glow-hdengine-v2` (project `ample-illumination`, environment `production`), which inherits the production bindings. Either way no vendor value is typed, pasted or put on an argument list | 20 |

**Hazards** (Guide §6): an editable install mapped to another checkout runs the wrong code (OBS-W5-5; check 1 guards it); six route-policy tests need `APP_ENV` set (OBS-P4-2; default rails set it); `tests/adapter/test_jsonschema.py` leaks `ENGINE_ENV` when first (OBS-P4-7; no selector here includes it); tests never run in the evidence checkout.

## 4. Product Owner inputs needed (names only)

- `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` (or `HDAPI_BASE_URL` only when the canonical name is absent; a conflict refuses), held by the E-V environment. Recorded `SET`/`UNSET` only. A missing name means no vendor call and check 20 `TOOLING_BLOCKED` (Plan Templates "PO inputs needed").
- The E-V venue choice (V-A or V-B) and the human initiator, recorded in the QA-90 task.
- The evidence-only commit grant (§2), or the Product Owner's own commit.
- No auth header input: `/internal/version` needs none (Plan Templates Step-0C).

## 5. Evidence and indexing

### 5.1 Layout

- Root: `audit/qa/hde-crd-0002/`; manifest `audit/qa/hde-crd-0002/qa_step_logs_manifest.json`; one primary per check at `audit/qa/hde-crd-0002/checks/` plus the check ID plus `/primary.log`, for example `audit/qa/hde-crd-0002/checks/qa-01-preflight/primary.log` (Glow QA Guide §0.2, §3.4.3, §4.4; HDE-Schemas & Artifacts §8.17). Lower-case directories.
- **Nothing else** is written under the root: no sidecars, no `00_meta/` file, no `results/` (the updater refuses any other indexed row under the root, and present-but-unindexed vendor evidence is a QA failure; Glow QA Guide §3.5.7; IR-6). Every request description, output, note and consumed-evidence pointer goes into the check's `primary.log` body. Plan Templates Step-0B content is carried in check 1's primary (CR-11, interim).
- Scratch files (pair files, attestation output, header captures) stay outside the repository and are not evidence; the primary records what the predicate needs (bytes, digests, counts).

### 5.2 Step-log header

`pf27.step_log_header.v2` with its fourteen keys, rendered by `tools.qa.qa_harness` (Plan Templates "Step-log header schema expectations (required; v2)"). `intended_tokens` and `claimed_tokens` are `[]` (no token use). `pf_refs` hold exact in-document PF titles from this set: `PF19-Canon-Glow-QA-Guide`, `PF27-Canon-Plan-Templates`, `PF05-Canon-HDE-CLI-API-Vendor-Ref`, `PF12-Canon-HDE-Schemas-and-Artifacts`, `PF14-Canon-HDE-Mechanics-Guide`, `PF07-Canon-Glow-Infrastructure`, `PF06-Canon-Change-Process-Guide`, `PF04-Canon-HDE-Governance` (HDE Build Notes cannot appear there; the body cites it by title).

**`command` and `exit_code`.** `command` holds the argv of each command the check executed, in order. When the Plan expects every child to exit 0, `exit_code` is the last decisive child's actual status. When the Plan expects a non-zero child exit (checks 6, 9, 11 and 20), the operator runs the sequence as one `bash -c` invocation that asserts each child's expected status, records that single invocation as `command`, and reports its actual exit status; each child's actual exit code and output appear in the body (Glow QA Guide §4.4.5: preserve negative child outcomes inside a passing outer predicate). `command_provenance` names this Plan's check, the QA-90 task and any in-flight syntax normalization (Glow QA Guide §3.4.7).

**Body.** In this order: `=== CONTEXT ===` (tested commit and tree, environment class, interpreter, rails, presence table, actor, time); `=== COMMANDS ===` (each child command, its exit code, stdout and stderr, separated); `=== PREDICATES ===` (each predicate with its observed value and PASS/FAIL); `=== NOTES ===` (normalizations, observations, nonclaims).

### 5.3 Evidence-assembly rules (from Audit findings QA50-F01, F02)

1. **LF only.** Normalize every captured CRLF to LF (HTTP headers in particular) before it enters `output`, and record "CRLF normalized to LF" in the notes. A CR byte makes publication refuse.
2. **Explicit rails.** Every `CheckResult.captured_env` carries the step's actual `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, captured when the step ran. The harness would otherwise copy the publishing process's closed rails.
3. **Secret scan.** Before assembly, scan all captured text for the values of the vendor and database variables held by the step's environment (comparison only; print `HIT` or `NO_HIT`, never a value) and for raw `Authorization`, `HD-Api-Key` or `HD-Geocode-Key` values. A hit quarantines the capture outside the repository and makes the check `FAIL_TOOLING` (Glow QA Guide §3.3, §3.5.7).
4. **Presence only.** Environment names are recorded `SET`/`UNSET`; `HD_API_BASE_URL` included (`AGENTS.md` redaction rule).

### 5.4 Publication procedure (all checks)

- **Evidence checkout.** A clean clone of `main` at or after the tested source (code identical), on one evidence branch, with CPython 3.12 and CI's full install (Flask is needed by the updater's `--check`; FND-033). Tests never run here.
- **Writer.** `tools.evidence.update_evidence_index.publish_crd_check_family(config, results, *, captured_at_utc=None, coherence_verifier=None)` with `tools.qa.qa_harness.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=pathlib.Path.cwd())`, invoked through `python -c` from the evidence checkout's root (so `pathlib.Path.cwd()` is that root) under the default closed rails (Plan Templates "Embedded harness checks"; HDE Mechanics Guide §1.6.3). The Audit §7 item 6 smoke-validated this path. QA-90 authors the exact invocation from it.
- **One call per check**, with `captured_at_utc` the check's own finalization time (the harness stamps one time per call). The call merges the result into the manifest by `check_id`; it runs the updater's `--check` first and refuses an incoherent prior graph.
- **After each call**, read-only validation from the evidence checkout root: `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/validate_evidence_paths.py`; `python ci/checks/check_mirror_schema.sh` (a Python script despite its suffix; CI runs it directly); `python tools/evidence/check_lf_endings.py`; and `tools.qa.qa_harness.validate_crd_check_family(config)`. The QA-100 result records each exit status and output.
- **A refused publication** (for example a CR byte or an invalid field) changes nothing (Audit §7 item 6). The operator corrects the assembly and publishes again from the same preserved transcript. That is not a rerun of the check. A second refusal of the same check goes to Kronos.
- **Never** hand-edit the manifest, a primary, a path proof, the Index, the Mirror, a sentinel or the orientation output; never run the updater in write mode separately.

### 5.5 Per-check registration map

For every check below, the registration set is (shown for check 1; every other check substitutes its own check ID): `audit/qa/hde-crd-0002/checks/qa-01-preflight/primary.log` and its `primary.log.path_proof.txt`; its manifest entry (`check_id`, `log_path`, `status`) in `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` and that file's `.path_proof.txt`; the Index rows `audit.qa.hde_crd_0002.checks.qa-01-preflight.primary.log` and `audit.qa.hde_crd_0002.qa_step_logs_manifest` in `docs/evidence/INDEX.json` with their Mirror rows in `artifacts/evidence_index.jsonl`; and the updater-owned companions of §2. Writer: `publish_crd_check_family`. Validation: §5.4.

| # | check_id | Publication dependency | Proof returned to QA-110 |
| :- | :- | :- | :- |
| 1 | `qa-01-preflight` | none; first publication creates the root | For every check: the primary's path, size and SHA-256; its manifest entry; the two Index keys present; the path proofs validating; §5.4's six results; the evidence commit and pull request; the attempt number |
| 2 to 15 | `qa-02-ci-coverage` to `qa-15-s01-removal` | check 1 published | as above |
| 16 to 19 | `qa-16-deployed-identity` to `qa-19-deployed-reader-input` | check 1 published | as above |
| 20 | `qa-20-live-vendor-override` | check 1 published | as above, plus the venue class and initiator attestation as recorded |
| 21 | `qa-21-evidence-admission` | checks 1 to 20 all published (any status) | as above, plus the final receipt of §5.6 |

### 5.6 Landing and final receipt

- Evidence lands by pull request (`AGENTS.md`); the Product Owner merges. Expected CI selection for such a pull request: lanes `evidence` and `release` (Audit §7 item 6). Its hosted result is the FND-001 remedy's measure (1); QA-110 reads it from GitHub and QA-120 reports it. It is not a check predicate.
- **Final receipt.** After check 21 is published, the operator re-runs §5.4's six validators and records them, with `validate_crd_check_family` listing all twenty-one checks, in the QA-100 result record. No primary claims the graph that includes itself (HDE Mechanics Guide §1.6.3, "must not claim a future final graph").
- **CI risks named in advance:** FND-024 (PR35-C1, git auto-maintenance race in `tests/tools/test_prepush_check.py`) and IR-7 (`test_manifest_reader_rejects_new_report_with_old_manifest`). A red run is classified from its log before any re-run; a re-run follows only the repository's CI rules.

## 6. Runbook check matrix

| # | check_id | Requirement(s) | Class (PF19 §3.5.6) | Rails | Env | Primary evidence |
| :- | :- | :- | :- | :- | :- | :- |
| 1 | `qa-01-preflight` | none (Step-0) | 2, pre-flight | default | E-L | `audit/qa/hde-crd-0002/checks/qa-01-preflight/primary.log` |
| 2 | `qa-02-ci-coverage` | S03, S04, S05 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-02-ci-coverage/primary.log` |
| 3 | `qa-03-attestation-debian` | S06 | 2, local/offline | default | E-D | `audit/qa/hde-crd-0002/checks/qa-03-attestation-debian/primary.log` |
| 4 | `qa-04-showcompat-help` | S07 | 2, operator CLI, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-04-showcompat-help/primary.log` |
| 5 | `qa-05-aux-preview-band` | S08 | 2, operator CLI, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-05-aux-preview-band/primary.log` |
| 6 | `qa-06-dev-harness-retired` | S09 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-06-dev-harness-retired/primary.log` |
| 7 | `qa-07-dev-reader-gate` | S10 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-07-dev-reader-gate/primary.log` |
| 8 | `qa-08-release-evidence-tooling` | S11, S12, S13 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-08-release-evidence-tooling/primary.log` |
| 9 | `qa-09-override-matrix` | S14 | 2, operator CLI, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-09-override-matrix/primary.log` |
| 10 | `qa-10-endpoint-catalog` | S15 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-10-endpoint-catalog/primary.log` |
| 11 | `qa-11-template-and-documents` | S16, S17, S18 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-11-template-and-documents/primary.log` |
| 12 | `qa-12-security-review` | S19 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-12-security-review/primary.log` |
| 13 | `qa-13-prepush-check` | S20 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log` |
| 14 | `qa-14-close-pack-writer` | S21 | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-14-close-pack-writer/primary.log` |
| 15 | `qa-15-s01-removal` | S01 (removed) | 2, local/offline | default | E-L | `audit/qa/hde-crd-0002/checks/qa-15-s01-removal/primary.log` |
| 16 | `qa-16-deployed-identity` | none (Step-0C; FND-032; FND-031) | 1, pre-flight / internal | Production | E-P | `audit/qa/hde-crd-0002/checks/qa-16-deployed-identity/primary.log` |
| 17 | `qa-17-deployed-not-found` | S02 | 1/2, internal (deployed) | Production | E-P | `audit/qa/hde-crd-0002/checks/qa-17-deployed-not-found/primary.log` |
| 18 | `qa-18-deployed-dev-surfaces` | S10, S19 | 1/2, internal (deployed) | Production | E-P | `audit/qa/hde-crd-0002/checks/qa-18-deployed-dev-surfaces/primary.log` |
| 19 | `qa-19-deployed-reader-input` | S19 | 1/2, internal (deployed) | Production | E-P | `audit/qa/hde-crd-0002/checks/qa-19-deployed-reader-input/primary.log` |
| 20 | `qa-20-live-vendor-override` | S14, S19 | **3, vendor; the Product Owner's Live QA workload** | Production | E-V | `audit/qa/hde-crd-0002/checks/qa-20-live-vendor-override/primary.log` |
| 21 | `qa-21-evidence-admission` | S22 | 2, local/offline | default | E-L and the evidence checkout | `audit/qa/hde-crd-0002/checks/qa-21-evidence-admission/primary.log` |

Checks 1 to 19 and 21 are "Pre-flight / internal" or local/offline, "Handled by QA/infra outside PO's Live QA time" (Glow QA Guide §3.5.6). Only check 20 is the Product Owner's Live QA workload. Tokens: none.

## 7. Check blocks

Every block's rails, environment and publication follow §3 to §5 unless it says otherwise. Every deliverable listed is required to exist after the check runs; nothing else under the root is created.

### CHECK 1 `qa-01-preflight` — Candidate, environment and Step-0B preflight
Surface / D-goal mapping: none; Plan Templates Step-0 (candidate identity, environment readiness, Step-0B doc-delta capture), on which every later check depends
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev · Pins: LC_ALL=C LANG=C TZ=UTC · Env: E-L
PF anchors: Plan Templates, Step-0B; Glow QA Guide §3.4.8 (entrypoint existence), §3.4.14, §10.8

**Covers:** the candidate guard (§2), OBS-W5-5, FND-033, Step-0B (CR-11 interim), the PF10 version in force.
**Actions** (each recorded with exit code and output):
1. `git rev-parse HEAD` and `git rev-parse HEAD^{tree}` in the clone; `git diff --stat 0b15328d585a764c124936b4524b766525daf1d9 HEAD -- . ':!docs/ephemeral' ':!docs/pfcanon'`.
2. `sha256sum catalog/manifest.json`; the manifest's `version`, `built_at_utc` and file count; `hdctl --version`.
3. `python --version`; `python -m pytest --version`; `ruby --version`; `bash --version`; `curl --version`; `git --version`; `python -c "import engine; print(engine.__file__)"`.
4. Presence of every name E-L must leave unset (`SET`/`UNSET`).
5. The first five read-only validators of §5.4 (the command-line ones) in the clone, plus `python scripts/release_id_recompute.py --check-manifest-only`.
6. Step-0B: `python -m pytest -p no:cacheprovider --collect-only -q` for every selector of checks 2 to 14 and 21; `test -e` for every entrypoint they name (`tools/ci/prepush_check.py`, `tools/evidence/build_release_attestation.py`, `tools/evidence/generate_a7_transport_proofs.py`, `ci/checks/check_cli_help.sh`, `scripts/release_id_recompute.py`); `ls docs/pfcanon | grep PF10` and its SHA-256; the QA Plan version in use is the approved one. Output the BLOCKER and CAVEAT list with stable IDs, or "no deltas".
7. `git status --porcelain` at the end.

**PASS predicate:** step 1 diff empty; manifest SHA-256 = `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, version `1.3.0`, built `2026-08-24T18:04:49Z`, 45 files, and `hdctl --version` prints exactly `hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e)` (observed at `0b15328d` under the default rails); Python 3.12.x, pytest present, `ruby`, `bash`, `curl`, `git` present; `engine` resolves inside the clone; every name in step 4 `UNSET`; every validator exits 0; every selector collects at least the Audit §7 item 2 count; Step-0B has no BLOCKER; status empty.
**Outcomes:** a missing tool or install, or an unexpected validator crash → `TOOLING_BLOCKED` or `FAIL_TOOLING` with the cause; a non-empty step 1 diff or a different `release_id` → `TOOLING_BLOCKED` ("candidate changed"), stop the run and route to Kronos; a Step-0B BLOCKER (a missing entrypoint or selector) → `TOOLING_BLOCKED`, stop and route to Kronos (Plan validity; Glow QA Guide §3.4.8). Never `FAIL_BEHAVIOR`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-01-preflight/primary.log`.
**Nonclaims:** environment readiness only.

### CHECK 2 `qa-02-ci-coverage` — Every test in a lane, owner refusal, filter equality
Surface / D-goal mapping: S03, S04, S05
Rails: default · Env: E-L · PF anchors: Glow QA Guide §3.4.8, §3.4.14

**Actions:**
1. `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py::test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target tests/evidence/test_rails_ci_workflow_integration.py::test_workflow_path_filter_skips_exactly_the_classifier_no_lane_documentation_paths tests/tools/test_prepush_check.py::test_coverage_matches_the_binding_definition_and_the_guard_on_the_repository` (S03, S05).
2. `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py -k qa_tool` (S04).
3. The `tests/retired_tests.md` ledger, from the clone root: `` awk -F' [|] ' '/^[|] `tests\//{n++; if ($2 ~ /^ *$/ || $3 !~ /^20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/) print "BAD", $1} END{print n" rows"}' tests/retired_tests.md `` (row count, and any row lacking a reason or an ISO date), then `` git ls-files -- $(grep -o '^| `tests/[^`]*`' tests/retired_tests.md | tr -d '|` ') | wc -l `` (ledger paths still tracked).
4. Cite, without re-running, hosted push run 39699657729 on `1a4c8ab` (all seven lanes `success`, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; Audit E-003 of the Reality Audit).

**PASS predicate:** step 1 "3 passed"; step 2 "2 passed"; step 3 prints no `BAD` line, then `66 rows` (the count at `0b15328d`), and the tracked count is `0`; exit 0 each.
**Outcomes:** a test failure → `FAIL_BEHAVIOR` with the failing node; a collection or environment error → `FAIL_TOOLING`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-02-ci-coverage/primary.log`.

### CHECK 3 `qa-03-attestation-debian` — Attestation builds under a distribution-patched setuptools
Surface / D-goal mapping: S06
Rails: default (the builder's own child environment allowlist applies) · Env: E-D · PF anchors: HDE-Schemas & Artifacts §6.2.1; HDE-Mechanics Guide §27.3

**Decision on FND-007:** re-run on the candidate. Hosted CI never exercises the Debian path, and the only Debian proof is a pre-merge rehearsal on an earlier commit.
**Actions:**
1. `/tmp/hde-crd-0002-qa03/venv/bin/python -c "import setuptools, importlib.util; print(setuptools.__version__, setuptools.__file__, importlib.util.find_spec('_distutils_system_mod'))"`.
2. From a second fresh clone detached at the tested source, with the E-D venv at `/tmp/hde-crd-0002-qa03/venv` and `/tmp/hde-crd-0002-qa03/out` absent or empty (both outside every repository): `env -i LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PATH=/tmp/hde-crd-0002-qa03/venv/bin:/usr/bin:/bin /tmp/hde-crd-0002-qa03/venv/bin/python tools/evidence/build_release_attestation.py --output /tmp/hde-crd-0002-qa03/out --require-clean`. If the venue needs other locations, the operator substitutes them throughout this check and records the substitution.
3. `env -i LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PATH=/tmp/hde-crd-0002-qa03/venv/bin:/usr/bin:/bin /tmp/hde-crd-0002-qa03/venv/bin/python tools/evidence/build_release_attestation.py --verify /tmp/hde-crd-0002-qa03/out --require-clean`.
4. From the output directory: `attestation.json` size and SHA-256, its `release_id`, `validation_result` and `release_admission`; `grep -c build_backend_compat=distribution_install_layout build.log`.
5. In the E-L venv: `python -m pytest -q -p no:cacheprovider tests/evidence/test_release_attestation.py -k "layout_compat or wheel_build_env"`.
6. `git status --porcelain` in the build clone.

**PASS predicate:** step 1 shows a `setuptools` path under `/usr/lib/python3/dist-packages` and `None` for the spec; steps 2 and 3 exit 0; `release_id` = the candidate's, `validation_result` `PASS`, `release_admission` `PR06R_B_FINAL_PASS`, the compat line count 1; step 5 "11 passed"; status empty.
**Outcomes:** no interpreter meets step 1 in the venue → `TOOLING_BLOCKED` (the Debian condition is unavailable; no claim). The build fails `isolated_package_install_failed` under the patched backend → `FAIL_BEHAVIOR`. Any other build failure → classify from the receipt (`failure.json`), `FAIL_TOOLING` unless it is product behaviour.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-03-attestation-debian/primary.log` (no attestation file is copied into the repository).
**Nonclaims:** no release cut, activation or deployment (`AGENTS.md` "Release identity").

### CHECK 4 `qa-04-showcompat-help` — The showcompat help summary on the operator CLI
Surface / D-goal mapping: S07
Rails: default · Env: E-L · PF anchors: HDE-CLI-API-Vendor-Ref §3.3; Glow QA Guide §3.3 (local/offline label)

**Actions:**
1. `hdctl --help` (the venv's console script) and `python -m engine.cli --help`; capture stdout and stderr separately.
2. `bash ci/checks/check_cli_help.sh`.
3. `python -m pytest -q -p no:cacheprovider tests/cli/test_cli_install_help.py::test_hdctl_and_module_help tests/cli/test_cli_usage_and_errors.py::test_top_level_help_names_the_showcompat_stdout_contract`.

**PASS predicate:** step 1 exits 0 with empty stderr; the two stdouts are byte-identical; with every run of whitespace collapsed to one space, the text contains exactly once `Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader` (the full sentence, QA50-F03); step 2 exits 0; step 3 "2 passed".
**Outcomes:** sentence absent or altered → `FAIL_BEHAVIOR`; tooling failure → `FAIL_TOOLING`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-04-showcompat-help/primary.log`.

### CHECK 5 `qa-05-aux-preview-band` — `--band` applies to pair-file input
Surface / D-goal mapping: S08
Rails: default · Env: E-L · PF anchors: HDE-CLI-API-Vendor-Ref §4.5; Glow QA Guide §3.3 ("Aux narratives come from compat JSON")

**Input:** a pair file produced offline from the tracked fixtures (a real `showcompat` output, labelled local/offline).
**Actions:**
1. `mkdir -p /tmp/hde-crd-0002-qa05 && hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json > /tmp/hde-crd-0002-qa05/pair.json` (a scratch file outside the clone); record its SHA-256 and each category's band (`harmony` is `Cool` at `0b15328d`).
2. For each band B in `Open`, `Warm`, `Glow` (three runs, each with the band written out): `hdctl aux-preview --pair-file /tmp/hde-crd-0002-qa05/pair.json --category harmony --band Open --show-narrative` and `hdctl aux-preview --category harmony --band Open --perspective shared --show-narrative`, then the same pair with `Warm`, then with `Glow`.
3. `hdctl aux-preview --pair-file /tmp/hde-crd-0002-qa05/pair.json --category harmony --show-narrative` and `hdctl aux-preview --category harmony --band Cool --perspective shared --show-narrative`.
4. `python -m pytest -q -p no:cacheprovider tests/cli/test_aux_preview.py -k pair_file`.

**PASS predicate:** every command exits 0 with empty stderr; for each B the two step-2 outputs are byte-identical and differ from the step-3 output; the two step-3 outputs are byte-identical (the file's band applies without `--band`); step 4 "7 passed". If the file's `harmony` band is not `Cool` at the tested source, the operator uses the three bands that differ from it and records the substitution.
**Outcomes:** override not applied → `FAIL_BEHAVIOR`; fixture or tool failure → `FAIL_TOOLING`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-05-aux-preview-band/primary.log` (narrative text is public Aux output and may be recorded).

### CHECK 6 `qa-06-dev-harness-retired` — Dev Reader harness retired; `VERIFY.sh` uses the canonical runner
Surface / D-goal mapping: S09
Rails: default · Env: E-L · PF anchors: HDE-CLI-API-Vendor-Ref §5.4; HDE-Mechanics Guide §34

**Actions:**
1. `git ls-files dev/reader_harness`; `test ! -e dev/reader_harness/app.py`.
2. `grep -c -i harness VERIFY.sh docs/acceptance/reader_a7_crib.md` (count 0 expected; grep exits 1, asserted inside the `bash -c` wrapper of §5.2).
3. `python -m pytest -q -p no:cacheprovider tests/scripts/test_dev_start_reader.py -k verify`.

**PASS predicate:** step 1 prints nothing and the file is absent; step 2 counts 0 and 0; step 3 "4 passed" (the script passes against the canonical runner with exact `dev` and refuses otherwise, `VERIFY_APP_ENV_NOT_DEV`).
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-06-dev-harness-retired/primary.log`.

### CHECK 7 `qa-07-dev-reader-gate` — Exact `dev` gate and canonical runner profile
Surface / D-goal mapping: S10
Rails: default · Env: E-L · PF anchors: HDE-CLI-API-Vendor-Ref §5.4, §5.6; HDE Build Notes 2.7 AD-2, AD-3

**Actions:**
1. `python -m pytest -q -p no:cacheprovider tests/http/test_reader_a7_transport.py tests/scripts/test_dev_start_reader.py -k "not verify"`.
2. `grep -n 'os.environ.get("APP_ENV") == "dev"' adapter/http_reader.py` (static supporting read).

**PASS predicate:** step 1 "33 passed" (the 16-value refusal matrix with exact `dev` serving, loopback bind, no CORS header, start-helper propagation); step 2 one match.
**Treatment of O-23:** the governed env-gate proof is fixed text from one `prod` probe; it is not decisive here. The decisive proof is step 1 locally and check 18 in the deployed target.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-07-dev-reader-gate/primary.log`.

### CHECK 8 `qa-08-release-evidence-tooling` — Drift test, release labels, root-bound closure probe
Surface / D-goal mapping: S11, S12, S13
Rails: default · Env: E-L · PF anchors: HDE-Schemas & Artifacts §8.3; HDE-Mechanics Guide §27.3

**Actions:**
1. `python -m pytest -q -p no:cacheprovider tests/evidence/test_engine_core_evidence.py -k release_id` (S11).
2. `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_index_missing_state.py -k "release_label or release_capture or capture_rows or capture_labels"` (S12).
3. `python -m pytest -q -p no:cacheprovider tests/evidence/test_release_attestation.py -k closure_probe` (S13).
4. Supporting read: the count of Mirror rows in `artifacts/evidence_index.jsonl` whose notes carry `current-release capture: release 1.3.0, release_id 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (27 at `0b15328d`).

**PASS predicate:** steps 1 to 3 "2 passed", "6 passed", "4 passed"; step 4 recorded (not decisive).
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-08-release-evidence-tooling/primary.log`.

### CHECK 9 `qa-09-override-matrix` — Override matrix, order and refusals, local
Surface / D-goal mapping: S14
Rails: default · Env: E-L, with `XDG_STATE_HOME` an empty scratch directory · PF anchors: HDE-CLI-API-Vendor-Ref §7.1.11a to §7.1.11f

**Actions:**
1. `python -m pytest -q -p no:cacheprovider tests/bodygraph/test_vendor_prod_override.py tests/cli/test_bg_resolve.py tests/bodygraph/test_resolver_vendor.py`.
2. CLI probes on the operator CLI under the default rails, inside one asserting `bash -c` (§5.2):
   - (a) `hdctl bg:resolve --user qa-hde-crd-0002-local1 --source vendor --birthdate 1990-01-01 --birthtime 12:34 --location "Amsterdam, NL"`;
   - (b) the same with `--allow-prod-vendor HDE-CRD-0002/qa/qa-20-live-vendor-override`;
   - (c) `--allow-prod-vendor "bad ref"` (a space, outside the allow-list);
   - (d) the flag twice;
   - (e) the flag with `--source db`.
3. After the probes: `find "$XDG_STATE_HOME" -type f` (E-L's empty scratch directory, for example `/tmp/hde-crd-0002-xdg-state`) and `git status --porcelain`.

**PASS predicate** (observed at `0b15328d`, Audit §7 item 10): step 1 "256 passed"; (a) and (b) exit 1 with a `status` `error` envelope and code `PROVIDER_REFUSED` (closed rails refuse first, matrix row 1); (c), (d) and (e) exit 64 with empty stdout and one stderr line that does not contain the flag value; step 3 finds no file (no audit event under closed rails) and an empty status.
**Outcomes:** any rail or matrix deviation → `FAIL_BEHAVIOR`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-09-override-matrix/primary.log`.
**Nonclaims:** no vendor I/O; the live behaviour is check 20.

### CHECK 10 `qa-10-endpoint-catalog` — Every served pair catalogued or excluded with a reason
Surface / D-goal mapping: S15
Rails: default · Env: E-L · PF anchors: HDE-CLI-API-Vendor-Ref §5.6; HDE-Schemas & Artifacts §8.8; HDE Build Notes 2.7 AD-1

**Actions:**
1. `python -m pytest -q -p no:cacheprovider tests/http/test_endpoint_catalog.py`.
2. `python tools/evidence/generate_a7_transport_proofs.py --check`.
3. `cmp docs/ENDPOINTS_CATALOG.json artifacts/audit/ENDPOINTS_CATALOG.json`; the catalog's record count.

**PASS predicate:** step 1 "247 passed"; step 2 exit 0; step 3 equal, 18 records.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-10-endpoint-catalog/primary.log`.
**Nonclaims:** catalog membership proves no reachability (HDE-CLI-API-Vendor-Ref §5.6).

### CHECK 11 `qa-11-template-and-documents` — Environment template and operator documents match the code
Surface / D-goal mapping: S16, S17, S18
Rails: default · Env: E-L · PF anchors: Glow QA Guide §3.4.12 (doc-alignment steps are mechanical)

**Actions** (mechanical `grep -c -F` counts and `python -c` classifier call; non-zero grep exits asserted in the wrapper):
1. S16: `.env.example` contains the line `GEO_API_KEY=changeme`; `python -c "from ci.checks import classify_ci_changes as c; print(c.classify_paths(['.env.example']).reason)"` prints `documentation_only`.
2. S17: `docs/ADAPTER_009.md` contains `GET /internal/readyz — always 200` and `/internal/readyz is registered only by`; `adapter/wsgi.py` contains `@app.get("/internal/readyz")` and `adapter/factory.py` and `adapter/http_reader.py` contain no `readyz`; `docs/ADAPTER_009.md` contains `Bind target for captures: http://127.0.0.1:8000` and the `Procfile` command after `web: ` byte for byte; `adapter/http_reader.py` contains `host="127.0.0.1"`.
3. S18: `docs/ADAPTER_009.md` contains `built from the \`invalid_json\` alias (emitted \`code\`: \`ERR_COMPAT_INVALID_JSON\`)`; `engine/http/compat_handler.py` contains `error_envelope("invalid_json")`; `ARCHITECTURE.md` contains `emit_public(envelope, *, sort_keys=True) -> bytes` and `## Routing and mounts` with the three factories named; `engine/presenter/emitter.py` defines `emit_public` returning `bytes`.

**PASS predicate:** every "contains" count is 1 or more and every "no" count is 0; step 1 prints `documentation_only`.
**Outcomes:** a statement absent or contradicted by the code → `FAIL_BEHAVIOR` (S16 to S18 acceptance is the documents' accuracy).
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-11-template-and-documents/primary.log`.
**Nonclaims:** FND-017 and FND-018's other stale lines are outside S17 and S18 and stay with the Product Owner.

### CHECK 12 `qa-12-security-review` — The S19 record and its fixes' regression tests
Surface / D-goal mapping: S19
Rails: default · Env: E-L · PF anchors: HDE Build Notes 2.3 rule 3, 2.10

**Actions:**
1. In the clone, from `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md`: the count of §6 per-file rows (49), of S19-F rows in §4's fixed table (9) and of S19-R rows in its routed table (7), each with a disposition.
2. `python -m pytest -q -p no:cacheprovider tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/transport/test_writers_errors_headers.py tests/http/test_compat_endpoint_contract.py tests/http/test_dev_conjunction_http.py tests/cli/test_cli_usage_and_errors.py tests/http/test_endpoint_catalog.py tests/bodygraph/test_resolver_vendor.py tests/bodygraph/test_ingest.py tests/cli/test_cli_file_inputs.py tests/config/test_manifest_schema.py tests/scripts/test_cut_release_manifest.py tests/config/test_config_artifacts.py -k s19`.

**PASS predicate:** step 1 counts 49, 9 and 7, every confirmed finding fixed or routed with owner and reason; step 2 "268 passed".
**Deployed classes:** S19-F01 and S19-F03 are proven in the deployed target by checks 19 and 18; S19-F05 and S19-F06 at the vendor call, check 20; S19-F02, F04, F07, F08 (loader) and F09 by step 2 locally. F08's loader effect in production is not exercised live (no Reader evaluation runs pre-App); this is a stated nonclaim.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-12-security-review/primary.log`.
**Nonclaims:** S19-R01 to R07 stay undecided with the Product Owner (FND-029).

### CHECK 13 `qa-13-prepush-check` — One read-only command with all five reports
Surface / D-goal mapping: S20
Rails: default (the tool runs its children under closed rails) · Env: E-L (a clean clone; `ruby`, `bash`, `curl` on `PATH`) · PF anchors: `AGENTS.md` "Pre-push check"

**Actions:**
1. The one command with all five reports: `python tools/ci/prepush_check.py --full --path engine/cli/main.py --path docs/ADAPTER_009.md lanes membership build-notes sweep replay` (given paths drive `lanes` and `membership`; `--full` makes `replay` the classifier's full validation).
2. `python tools/ci/prepush_check.py --path docs/ADAPTER_009.md lanes` (a documentation-only path alone).
3. `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py`.
4. `git status --porcelain`.

**PASS predicate:**
- Step 1 exits 0 and prints:
  - `lanes: classification reason=selected_lanes;paths=2;lanes=product,compat,release`;
  - `membership: member engine/cli/main.py` and `membership: not-member docs/ADAPTER_009.md`;
  - `build-notes: path=docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md` with `sha256=42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b` (or the single PF10 file then on `main`, recorded as a CAVEAT);
  - `uncovered=0` in the `sweep` report;
  - `status=PASS` for each of the five reports;
  - a final `PREPUSH_CHECK_RESULT: PASS` line that reports the repository unchanged.
- Step 2 prints `lanes: classification reason=documentation_only;paths=1;lanes=none` and exits 0.
- Step 3 "137 passed"; step 4 empty.

Every line above was observed at `0b15328d` (Audit §7 item 9); step 1 took about 24 minutes there, most of it `replay`.
**Outcomes:** a step 2 failure whose signature is the recorded git auto-maintenance race (PR35-C1, FND-024) is an execution fault eligible for §9's one rerun; any other failure → `FAIL_BEHAVIOR`. Exit 4 (repository changed) → `FAIL_BEHAVIOR`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log`.
**Nonclaims:** the tool's result is not CI's result (README "Pre-push check"); FND-028 (removing `replay`) stays the Product Owner's decision.

### CHECK 14 `qa-14-close-pack-writer` — The v2 close-pack writer, the close-run home and the ADR
Surface / D-goal mapping: S21
Rails: default · Env: E-L · PF anchors: Change Process Guide §3.5.2; HDE-Schemas & Artifacts §1.2; HDE Build Notes 2.15, 2.17

**Actions:**
1. `python -m pytest -q -p no:cacheprovider tests/qa/test_generate_epic_close_pack.py`.
2. `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_index_missing_state.py -k close`.
3. `sed -n 3p docs/adr/hde/close_pack_writer_adr.md`; `test -f schemas/close_candidate_source.v2.json`.

**PASS predicate:** step 1 "905 passed"; step 2 "4 passed"; step 3 prints `Status: Approved with changes by the Product Owner on 2026-10-20 (AQ-1; HDE Build Notes addendum 2.15;` followed by the review reference, and the schema exists.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-14-close-pack-writer/primary.log`.
**Nonclaims:** no close pack or candidate source is produced; the business-case measure is the real close (after QA-120). FND-020 (the ADR's superseded clause) stays with the Product Owner.

### CHECK 15 `qa-15-s01-removal` — S01 is removed as approved and its stated limit holds
Surface / D-goal mapping: S01 (removed by Specification delta 01; this check proves the removal and its stated limit, not delivery)
Rails: default · Env: E-L · PF anchors: HDE Build Notes 2.19, 2.20

**Purpose (G-1; QA50-F05):** the close writer reads S01 from the approved base. This check gives the close owners a truthful, evidenced basis for representing S01; it decides nothing about that representation.
**Actions:**
1. `grep -c '^decision: DELTA_APPROVE' docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`; `grep -c '^## 2.20 HDE-CRD-0002: Specification delta 01 is approved' docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md` (or the PF10 file in force, recorded).
2. No version cut: `grep -c '^ADMITTED_RELEASE_VERSION = "1.3.0"' engine/config/registry_loader.py`; `grep -c '^ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"' engine/config/registry_loader.py`; the manifest version (check 1).
3. Not delivered: `git log --oneline 7136040^..HEAD -- pyproject.toml` prints nothing (no packaging change in this change).
4. Stated limit and basis: `grep -c 'omits 16 of the 45' README.md`; the `Procfile` starts `adapter.factory:create_app()` from the checkout.

**PASS predicate:** every count is 1 and step 3 prints nothing.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-15-s01-removal/primary.log`.
**Nonclaims:** a regular wheel install outside a source checkout still does not admit the release (delta 01 C-6; FND-026).

### CHECK 16 `qa-16-deployed-identity` — Service readiness and the deployed candidate's identity
Surface / D-goal mapping: none; Glow QA Guide §3.5.2 Step 0 and §3.5.10 readiness, FND-032 re-read, and the WU-OPS-01 evidence consumed by reference (FND-031)
Rails: SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod (Production binding, recorded) · Env: E-P · PF anchors: Glow Infrastructure §2.2; HDE-Governance §10.5; Glow QA Guide §11.1

**Actions** (each request sent once; no auth header; headers and body captured separately, §5.3):
1. `mkdir -p /tmp/hde-crd-0002-qa16 && curl -sS -D /tmp/hde-crd-0002-qa16/get.hdr -o /tmp/hde-crd-0002-qa16/get.body -w '%{http_code}' https://glow-hdengine-v2-production.up.railway.app/internal/version` (scratch outside every repository; the operator may use another scratch directory and records it).
2. `curl -sS -I -D /tmp/hde-crd-0002-qa16/head.hdr -o /dev/null -w '%{http_code}' https://glow-hdengine-v2-production.up.railway.app/internal/version` (HEAD; curl reads headers only).
3. In the evidence checkout or a clone: `sha256sum -c SHA256SUMS.attempt1` in `audit/ops/hde-crd-0002/wu-ops-01/`; read `result.attempt1.txt` and `identity_reads.attempt1.tsv`.

**PASS predicate:** steps 1 and 2 return 200 with `Cache-Control: no-store`, no `ETag`, `application/json`; the body has exactly the keys `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`, with `release_id` = `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (judged on the GET body); step 3 "5 of 5 OK", result `PASS`, identity class `MATCH` with the same `release_id`.
**Outcomes:** the service is unreachable or not HTTP/1.x → `TOOLING_BLOCKED` (checks 17 to 19 then do not start; Glow QA Guide §3.5.10). A different `release_id` → `TOOLING_BLOCKED` ("deployed candidate differs"); route to the Product Owner (deployment and rollback are the Product Owner's; Plan delta 01 P-9). `build_commit` is recorded and never judged.
**Consumed Ops evidence:** the body lists the six `audit/ops/hde-crd-0002/wu-ops-01/` paths with their SHA-256 values, and `evidence_artifacts` names them, so this primary and its path proof point to them without re-homing (Glow QA Guide §11.1; CR-9 interim (a)).
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-16-deployed-identity/primary.log`.

### CHECK 17 `qa-17-deployed-not-found` — Unknown paths answer the governed envelope in the deployed service
Surface / D-goal mapping: S02
Rails: Production binding · Env: E-P · PF anchors: HDE-CLI-API-Vendor-Ref §5.2, §5.5 · Depends on: check 16 PASS

**FND-004 statement:** this check exercises unknown non-compat paths at the root, under `/api/` and `/internal/`, each method at the root, one 405, and the production compat namespace. It excludes the Reader's unknown-person 404 (§1).
**Requests** (eight, each once, base `https://glow-hdengine-v2-production.up.railway.app`): `GET`, `HEAD`, `POST` (body `{}`), `OPTIONS` on `/qa-hde-crd-0002-unknown`; `GET /api/qa-hde-crd-0002-unknown`; `GET /internal/qa-hde-crd-0002-unknown`; `GET /api/compat/v1`; `DELETE /internal/version`.
**PASS predicate** (Audit §6): each answers 404, except `DELETE /internal/version` 405 with `Allow: GET, HEAD, OPTIONS`; every answer has `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store` and no `ETag`; every body except HEAD's is exactly `{"code":"ERR_NOT_FOUND","error":"not found","ok":false,"schema":"v1"}` plus one LF; HEAD's is empty; no answer is `text/html`.
**Outcomes:** a reachable answer that contradicts a predicate → `FAIL_BEHAVIOR`; transport failure → `TOOLING_BLOCKED`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-17-deployed-not-found/primary.log`.

### CHECK 18 `qa-18-deployed-dev-surfaces` — Dev and retired routes refuse in the deployed service
Surface / D-goal mapping: S10, S19 (fix S19-F03, the production posture)
Rails: Production binding · Env: E-P · PF anchors: HDE-CLI-API-Vendor-Ref §5.4, §5.11.2, §5.12; HDE Architecture §3.3, §3.5 · Depends on: check 16 PASS

**Requests** (nine decisive, each once): `GET /reader?v=1`; `HEAD /reader?v=1`; `POST /internal/dev/sampler` (body `{}`); `GET /dev/sampler/conjunction`; `GET /dev/reader/conjunction`; `GET /dev/writer/conjunction`; `GET /ops/probe/env`; `GET /ops/db/unavailable`; `POST /ops/writer/diagnostic` (body `{}`). Observation only (IR-3; LR5-O1): `OPTIONS /dev/sampler/conjunction` and `GET //reader?v=1`.
**PASS predicate** (Audit §6): `/reader` GET and HEAD 403, the GET body `{"code":"ERR_READER_FORBIDDEN","error":"reader endpoint disabled","ok":false,"schema":"v1"}` plus LF, HEAD empty; the sampler and the three conjunction routes 403 with `{"code":"ERR_WRITER_FORBIDDEN","error":"insufficient scope","ok":false,"schema":"v1"}` plus LF; the three retired routes 404 with the `ERR_NOT_FOUND` envelope; all `application/json; charset=utf-8`, `no-store`, no `ETag`. The two observation rows are recorded with status, `Allow` and `Location` headers and carry no predicate: a 200 with `Allow` to `OPTIONS`, or a 404 or 308 to the doubled slash, is the router's answer (LR5-O1), not a defect on its own.
**Outcomes:** a 200 or a handler response on a decisive request → `FAIL_BEHAVIOR`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-18-deployed-dev-surfaces/primary.log`.
**Nonclaims:** no claim from the env guard (IR-4) or the dead `after_request` hook (IR-5).

### CHECK 19 `qa-19-deployed-reader-input` — Deeply nested JSON is a typed 422 in the deployed Reader
Surface / D-goal mapping: S19 (fix S19-F01)
Rails: Production binding · Env: E-P · PF anchors: HDE-CLI-API-Vendor-Ref §5.2.3, §8.1 · Depends on: check 16 PASS

**Input** (attacker-suppliable through the public route, so real under HDE Build Notes 2.11 rule 4(c)): 32,768 bytes of `[`; and `{"a_id":` followed by 20,000 bytes of `[`. Both are inside the 32 KiB limit and fail at parsing, before any lookup.
**Requests** (three, each once, `Content-Type: application/json; charset=utf-8`): `POST /api/reader?v=1` with the first body; `POST /api/reader?v=2` with the first body; `POST /api/reader?v=1` with the second.
**PASS predicate:** each answers 422, `application/json; charset=utf-8`, `no-store`, no `ETag`, body exactly `{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}` plus LF. A 500 or `text/html` fails.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-19-deployed-reader-input/primary.log` (request bodies recorded by length and SHA-256, not inline).

### CHECK 20 `qa-20-live-vendor-override` — The mandatory live vendor call through the production override
Surface / D-goal mapping: S14 (the production override, human-initiated, with its audit events); S19 (fixes S19-F05 strict rails and S19-F06 no tracked log write, at the vendor path)
Rails: SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod for this check only, then restore the default · Pins: LC_ALL=C LANG=C TZ=UTC · Env: E-V (V-A or V-B, the Product Owner's choice) · PF anchors: HDE-CLI-API-Vendor-Ref §7.1.11 to §7.1.11f; Glow QA Guide §3.3, §3.5.5, §3.5.7; Plan Templates "Open-Rails Live QA Requirement for production-affecting epics"

**What it proves:** in a production-like environment with both rails open, `hdctl bg:resolve --source vendor` refuses without the flag, and with a valid authorization reference makes one bounded admin vendor request whose pre-I/O `allowed` event and post-I/O state event are durable and keys-only.
**Initiator:** the authenticated human Product Owner, or the human operations executor the Product Owner names in the QA-90 task. That person types and runs steps V1 and V2.
**Authorization reference:** `HDE-CRD-0002/qa/qa-20-live-vendor-override` (it names this approved work item; it is not a credential; it matches `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$`).
**Synthetic inputs:** `--user qa-hde-crd-0002-vendor1`, `--birthdate 1990-01-01`, `--birthtime 12:34`, `--location "Amsterdam, NL"` (the synthetic tuple of the repository's override tests; no real person).
**Request limit and stop checks:** at most one allowed invocation (V2) per attempt; V1 makes no vendor request; no `--upsert`; no other vendor command (no `showcompat --source vendor`; IR-2); no retry beyond the client's own policy. Stop before V2 if any preflight row or V1 fails. Stop after V2 whatever its result.

**Preflight** (no vendor I/O):
- P1 candidate. V-A: `git rev-parse HEAD` passes check 1's guard, `git status --porcelain` is empty, `hdctl --version` prints the line check 1 pins (it contains the candidate `release_id`), and `engine` resolves inside the clone. V-B: check 16 PASS in the same session window, and `python -m engine.cli --version` in the service shell contains the candidate `release_id`.
- P2 presence: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` `SET`; `HDAPI_BASE_URL` `UNSET`, or `SET` and equal to the canonical value (compared without printing); `ENGINE_ENV` `UNSET` or a production-like value; `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and `DATABASE_URL` presence recorded.
- P3 rails: exactly `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=prod`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
- P4 sink: the sink path the delivered code will use (from `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, else `XDG_STATE_HOME`, else `~/.local/state/glow-hdengine/vendor_prod_override.jsonl`), confirmed outside any repository checkout, and its current line count (0 when absent).
- P5 actor: `python -c "import os, pwd; print(pwd.getpwuid(os.geteuid()).pw_name)"` prints a non-empty account name. The initiator's attestation line names their role and states that they ran V1 and V2 themselves (IR-1: the account is not proof of a person; the attestation is).

**Steps:**
- V1: `hdctl bg:resolve --user qa-hde-crd-0002-vendor1 --source vendor --dry-run --birthdate 1990-01-01 --birthtime 12:34 --location "Amsterdam, NL"` (V-B: `python -m engine.cli` in place of `hdctl`).
- V2: the same command with `--allow-prod-vendor HDE-CRD-0002/qa/qa-20-live-vendor-override`.
- After: the sink's new lines (all lines after P4's count); V-A `git status --porcelain`; the §5.3 secret scan over stdout, stderr and the new sink lines.

**PASS predicate:**
- V1 exits 1; stdout is a `status` `error` envelope with code `PROVIDER_PROD_OVERRIDE_REQUIRED` and `error.details.outbound_attempted` `false`; stderr empty; exactly one new sink line: event `vendor_prod_override`, outcome `refused`, `error_code` `PROVIDER_PROD_OVERRIDE_REQUIRED`, `authorization_ref` `null`, `outbound_attempted` `false`.
- V2 exits 0; stdout `status` `ok`; `resolver.route_policy.route_family` `recommended_v2_chart` and `resource_path` `charts`; `adapter.status` `mapped` with `payload_family` `ChartResult`; `cache.payload_posture` `adapter_mapped_no_raw_vendor_payload`; `ingest.rows_written` 0; the request posture lists `Authorization: Bearer <redacted>` and `HD-Geocode-Key: <redacted>` and no `HD-Api-Key`.
- Exactly two further sink lines with one shared `correlation_id`: first outcome `allowed` (`authorization_ref` the reference, `outbound_attempted` `false`, `route_family` `null`), then outcome `completed` (`outbound_attempted` `true`, `route_family` `recommended_v2_chart`, `resource_path` `charts`, `error_code` `null`).
- Every new sink line has the sixteen keys of HDE-CLI-API-Vendor-Ref §7.1.11f (with `route_family` and `resource_path` counted as two), `actor_principal` equal to P5's account, and no user key, birth data, location, URL, header, key or raw provider text.
- V-A: `git status --porcelain` empty (S19-F06: no tracked ingest log written). V-B: not applicable, recorded with the reason.
- Secret scan `NO_HIT`.

**Outcomes and classification** (Glow QA Guide §3.5.7):
- A missing name in P2, a failing P1 or P3, an unwritable sink or unresolved actor (`PROVIDER_AUDIT_UNAVAILABLE`, zero I/O; Plan R-3) → `TOOLING_BLOCKED`.
- V1 deviates → `FAIL_BEHAVIOR`; V2 is not run.
- V2 fails with a provider-side code → classify as credential, configuration, account or tier, endpoint unavailability, rate limit or outage (`TOOLING_BLOCKED`); request-shaping or response-mapping → `FAIL_BEHAVIOR` only with proof (a wrong auth-header family is request-shaping or setup).
- An event predicate violated → `FAIL_BEHAVIOR`.
- A secret hit → `FAIL_TOOLING` and quarantine.

**Evidence** (all in the primary; no sidecar; IR-6): venue class and initiator attestation; P1 to P5; the argv of V1 and V2 (no secret on an argument list); their stdout (canonical JSON; the mapped record of the synthetic input, no raw vendor payload), stderr and exit codes; the three new sink lines verbatim (keys-only by contract); the secret-scan result; the classification; the nonclaims. `captured_env` is the Production binding as set. V-B outputs are copied by the initiator from the service shell, CRLF normalized.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-20-live-vendor-override/primary.log`.
**Nonclaims:** V-A is a CLI-local call in a production-like environment, not deployed-service validation; no broad HumanDesignAPI v2 conformance, mapped-cache write, database write, deployment, QA PASS for the change or closure (Glow QA Guide §3.5.5).

### CHECK 21 `qa-21-evidence-admission` — The first real HDE-CRD-0002 publication validates; existing inputs still validate
Surface / D-goal mapping: S22
Rails: default · Env: the evidence checkout (validation only) and an E-L copy of it (tests) · PF anchors: HDE-Schemas & Artifacts §8.17; HDE-Mechanics Guide §1.6.3 · Depends on: checks 1 to 20 published (any status)

**Actions:**
1. In the evidence checkout, from its root: `validate_crd_check_family(HarnessConfig(crd_id="HDE-CRD-0002", repo_root=pathlib.Path.cwd()))` and the same with `crd_id="HDE-CRD-0001"`; §5.4's five read-only validators; read the Index for the key `audit.qa.hde_crd_0002.qa_step_logs_manifest` and for the twenty keys `audit.qa.hde_crd_0002.checks.qa-01-preflight.primary.log` to `audit.qa.hde_crd_0002.checks.qa-20-live-vendor-override.primary.log` (one per check ID of §6).
2. In a throwaway copy of the evidence checkout with its published files (tests never run in the evidence checkout): `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_index_missing_state.py -k crd tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity tests/qa/test_generic_qa_harness.py -k crd tests/qa/test_epic021_acceptance_alignment.py::test_current_acceptance_inputs_are_strictly_viable` (run as separate invocations where `-k` scopes differ).

**PASS predicate:** HDE-CRD-0002 validates with exactly the twenty IDs of checks 1 to 20, each manifest status equal to its header; HDE-CRD-0001 validates with its ten checks; the five validators exit 0; all twenty-one Index keys are present; step 2 "31 passed", "1 passed", "81 passed", "1 passed" with the real root present (Audit §7 item 8 observed these counts with a stand-in root; the first selector takes about four minutes).
**Outcomes:** a validator or test failure caused by the published family → `FAIL_BEHAVIOR` against S22 (route to Kronos, then the S22 owner); an assembly fault → `FAIL_TOOLING`.
**Deliverables:** `audit/qa/hde-crd-0002/checks/qa-21-evidence-admission/primary.log`. After it is published, §5.6's final receipt.
**Nonclaims:** the remedy's measure (1) is the evidence pull request's hosted result, read by QA-110; measure (2) belongs to the close-pack pull request.

## 8. Dependencies and order

- Check 1 precedes every check. Checks 2 to 15 are independent of one another.
- Check 16 PASS precedes checks 17 to 19, and check 20 under V-B. Check 20 under V-A needs check 1.
- Check 21 runs last, after checks 1 to 20 are each published (any status).
- The Product Owner selects tasks and their grouping at QA-90; this Plan sets no batch. A task may hold several checks, but each check is published by its own call (§5.4).

## 9. Rerun, escalation, recovery and cleanup

- **One bounded ordinary-lane rerun per check**, under this unchanged Plan, for an execution or evidence fault (`FAIL_TOOLING`, or `TOOLING_BLOCKED` from a transient or environmental cause), with the same `check_id`, rails, environment class and deliverable. The rerun's primary opens its notes with the first attempt's failure signature and a one-line remediation note (what changed and why); the first attempt's published primary, if any, remains in git history; QA-100 records both attempts (Plan Templates "Bounded step-level rerun posture"). Renaming a check does not reset attempts.
- **Check 20's rerun** is allowed only when attempt 1 made no outbound request (V2 never ran or refused before I/O), or V2 failed with a provider-side class (outage, rate limit, credential or configuration presence). The total stays at most two allowed invocations.
- **Escalation:** a second failure of the same check, any `FAIL_BEHAVIOR`, or a needed change of scope, target, rails, evidence or predicate goes to Kronos at QA-110, then through the remediation route of Glow QA Guide §10.6 or the Plan's owner (QA-80). Product code, tests, generators and governed artifacts outside the QA root are never changed in QA (Glow QA Guide §3.4.8 Moon Loop boundary); Moon Loop applies only to QA-created assembly under the QA root.
- **Recovery:** a refused publication changes nothing (§5.4). An interrupted run resumes at the first check without a published primary. If a deployed probe leaves the service in doubt, the only Ops action is WU-OPS-01's rollback intent (redeploy the previous commit), and it is the Product Owner's.
- **Cleanup:** delete throwaway clones, venvs, scratch pair files, the attestation output directory and the scratch `XDG_STATE_HOME`. Under V-A, the sink file keeps its three events (append-only by design); under V-B it lives on the service host. Restore the default rails after check 20.

## 10. Coverage

| Req | Checks (PASS needed) | Proof class |
| :- | :- | :- |
| S01 | 15 | Removal as approved (G-1) |
| S02 | 17 | Deployed target |
| S03, S04, S05 | 2 | Local/offline, with hosted CI cited |
| S06 | 3 | Local/offline, Debian backend |
| S07 | 4 | Operator CLI, local/offline |
| S08 | 5 | Operator CLI, local/offline |
| S09 | 6 | Local/offline |
| S10 | 7, 18 | Local matrix and deployed refusal |
| S11, S12, S13 | 8 | Local/offline |
| S14 | 9, 20 | Local matrix and the live vendor call |
| S15 | 10 | Local/offline |
| S16, S17, S18 | 11 | Mechanical document alignment |
| S19 | 12, 18, 19, 20 | Record and tests; F03, F01 deployed; F05, F06 live |
| S20 | 13 | Local/offline |
| S21 | 14 | Local/offline |
| S22 | 21 | The real publication and validation |

**Risks and obligations:** IR-1 (check 20 P5 and attestation), IR-2 (§1; check 20 limit), IR-3 (check 18 observation rows), IR-4 and IR-5 (check 18 nonclaims), IR-6 (§5.1; check 20 evidence), IR-7 and FND-024 (§5.6; check 13), IR-8 (no selector here includes `tests/evidence/test_hdapi_v2_contract_inventory.py`; a full-validation run would), IR-9 (§1), IR-10 (§1), IR-11 and FND-030 (check 15; §7 format), FND-004 (check 17), FND-007 (check 3), FND-011 (check 20), FND-031 (check 16), FND-032 (check 16), FND-033 (§3.2, §5.4), O-23 (check 7), LR4-O2 (check 20).

## 11. Final-report criteria (QA-120)

- **Form:** `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v` plus a two-part version plus `.md`, for example `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md`, with front matter `artifact_type: QA_REPORT`, `change_id: HDE-CRD-0002` and `verdict:` followed by the actual verdict (for example `verdict: PASS`), and a separate RCA (Glow QA Guide §3.1.2).
- **`verdict: PASS` only when:** all twenty-one checks are `PASS` in `audit/qa/hde-crd-0002/qa_step_logs_manifest.json`; each requirement S02 to S22 has a `PASS` check whose mapping names it (§10); S01 is reported as removed by Specification delta 01, with check 15's PASS as the removal evidence; the Live QA minimum holds (checks 17 to 19 and 20 `PASS`); check 21 and §5.6's final receipt show the published family coherent. A `TOOLING_BLOCKED` check leaves its criterion unproven and the verdict not `PASS`; any closure override is a close-stage decision, not QA's.
- **The report states:** the tested commit and tree; each check's status, attempts, environment class and rails; every normalization and deviation; the venue and initiator of check 20; the evidence commit and pull request with its hosted CI result (measure (1)); the dispositions of IR-1 to IR-11 and of FND-004, 007, 011, 024, 030, 031, 032 and 033; CR-11's decision; the nonclaims of §12.

## 12. Nonclaims

This Plan, its approval and a passing run establish none of: acceptance of HDE-CRD-0002, closure, a close pack, PF09 or PF30 movement, deployment, release activation, broad HumanDesignAPI v2 conformance, mapped-cache persistence, live Reader success or Gate readiness, canon drainage, or a decision on any routed Product Owner item (FND-012, FND-028, FND-029, X-02, the legacy chart-loader defect).

## 13. CANON_CONFLICT_REGISTER

**Carried entries** (unchanged; full fields in their records):

| ID | Classification | Statement | Status | Decision owner, time | Record |
| :- | :- | :- | :- | :- | :- |
| CR-1 | CANON_RECONCILIATION | Canon disagrees on whether a CRD needs a PF30 record and a "CRD Plan" | APPROVED_AS_CHANGED | Thoth, 2026-10-12 | Specification v1.1-approved "Canon conflict register" |
| CR-2 | CANON_RECONCILIATION | Plan Templates §2A asks a Specification for planned units HDE Governance §9.1.1 forbids | APPROVED_AS_CHANGED | Thoth, 2026-10-12 | same |
| CR-3 | CANON_RECONCILIATION | Three passages point to a PF30 record that will not exist (CRD identity) | APPROVED_AS_CHANGED | Thoth, 2026-10-12 | same |
| CR-4 | CANON_RECONCILIATION | PO-D4 versus the addendum 2.2 rescope route, for R-14 only | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | CANON_RECONCILIATION | Canon replacement inside an implementation PR; the vehicle is assigned case by case | APPROVED_AS_CHANGED | Product Owner | same §3 |
| CR-6 | CANON_RECONCILIATION | The dev Reader start helper's default versus canon | APPROVED, alternative (a) | Implementation Agent through RS-20 | HDE Build Notes 2.6 |
| CR-7 | CANON_RECONCILIATION | S15 and IF-6 catalogued routes HDE Architecture §3.5 excludes | APPROVED, alternative (a) | Product Owner, 2026-10-14 | HDE Build Notes 2.7 |
| CR-8 | CANON_RECONCILIATION | A normalizing dev gate versus explicit `APP_ENV=dev` | APPROVED, alternative (a) | Product Owner, 2026-10-14 | HDE Build Notes 2.7 |
| CR-9 | CANON_RECONCILIATION | Plan delta 01 P-9 asks for path proofs under the WU-OPS-01 root, which no canonical writer covers | PROPOSED, not yet reviewed; interim (a): the consuming QA check carries the path proof (applied by check 16) | Isis, at the IA-30 boundary | `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md` §13 |
| CR-10 | CANON_RECONCILIATION | The Index and Mirror key set gains `crd_id` (two validators) | APPROVED, alternative (a); applied | Isis, ESC-40, 2026-10-23T20:15:00Z | remediation review v1.1 §4; HDE Build Notes 2.24 |

**CR-11 (new; `PROPOSED`).**
- **Classification:** CANON_RECONCILIATION.
- **Sources:**
  - Plan Templates v2.0.5, "Mandatory Step-0 artifacts", Step-0B: "Doc-delta surfaces (required; two-surface pair)", the draft `audit/docdeltas/<epic-id>_doc_deltas.md` and the capture `audit/qa/<epic-id>/00_meta/doc_deltas.md`, "MUST be generated by commands".
  - HDE-Mechanics Guide v3.5.8 §1.6.3: CRD publication "neither repairs unrelated historical evidence implicitly nor permits arbitrary additional-file or index-metadata injection"; the updater indexes only the manifest and `checks/` and `close/` primaries under a CRD root (`_load_crd_qa_entries`).
  - Glow QA Guide v3.0.6 §3.5.7 and §3.4.3: evidence present but not indexed is a QA failure; outputs are minimized to the primary and the manifest.
  - Implementation Plan v1.1 §7 WU-PR-07 "Terminal-state reachability" (a) and T1: the close mutation set authors `audit/docdeltas/hde-crd-0002_doc_deltas.md` as a causal input of the close pack.
- **Statement:** for a CRD, Step-0B's 00_meta capture cannot be indexed by the governed writer, and its draft surface is a close-stage causal input another owner authors.
- **Affected requirements:** none of S01 to S22 directly; the QA run's Step-0B obligation and the close's doc-delta ledger.
- **Alternatives:** (a) carry Step-0B's BLOCKERS and CAVEATS in check 1's primary (indexed), report them in QA-120, and leave `audit/docdeltas/hde-crd-0002_doc_deltas.md` to the close mutation set at T1, which consumes them; (b) write `00_meta/doc_deltas.md` unindexed (rejected: present but unindexed evidence; the HDE-CRD-0001 `00_meta/final-verification.log` precedent is an unindexed final receipt, not a Step-0B surface); (c) extend the updater's CRD admission to `00_meta/` (a code change outside QA).
- **Recommended disposition and interim treatment:** (a), applied by this Plan pending the decision.
- **Unresolved risk:** if (a) is rejected, the Plan gains a Step-0B surface through QA-80 before execution; no executed evidence is affected yet.
- **Drainage target and owner:** Plan Templates Step-0B (CRD applicability) and HDE-Mechanics Guide §1.6.3; the Product Owner.
- **Status and history:** `PROPOSED` by Kronos in this Plan v1.0 (2026-10-24); reviewer Isis at QA-70; unreviewed fields: all decision fields.

## 14. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Review of this Plan | Isis, QA-70 | Next |
| CR-11 | Isis, QA-70 | PROPOSED |
| CR-9 | Isis, IA-30 boundary | PROPOSED, unchanged |
| Executor arrangement; check 20 venue and initiator; evidence-only commit grant | Product Owner, recorded at QA-90 | Not stated |
| G-1: the close representation of S01 | Close mutation set and Isis; Product Owner if a route beyond the writer is needed | Open; check 15 supplies the evidence |
| QA50-F03 pinning test for the S07 sentence | Product Owner (later-change candidate) | Proposed |
| FND-012, FND-022, FND-023, FND-028, FND-029, FND-034, FND-037, FND-038; documentation deltas FND-017 to FND-021, FND-040 | Product Owner | Pending, non-gating |

## 15. TypeSafe reading for the receiving session (QA-70)

Action sent (v8.2): "As the independent lead-developer reviewer for one change, review one new, never-reviewed whole-change QA plan of 21 separately verifiable checks (about 630 lines) and its companion QA audit (about 260 lines) against the canon, the approved specification's 22 requirements, a Live QA guide and the delivered code, and record a review with findings and a disposition. Each check's commands, pass predicates, evidence indexing and requirement mapping must be checked individually, including a few probes of the deployed service, one mandatory human-initiated live vendor call and one proposed canon conflict that needs a decision. It is a Markdown record only: no task list exists yet, no live run against a provider occurs here, and QA task creation, execution and an independent evidence review follow."

The reading as printed by the script:

- **TypeSafe v8.2: Fable 5.1 at max.** Effort score 3.58 (confidence 0.69); rung probabilities low 0.00, medium 0.01, high 0.09, extra high 0.23, max 0.65, ultracode 0.02. Model probabilities Fable 5.1 0.52, Opus 5.5 0.46, Sonnet 5.5 0.02, Haiku 5.5 0.00 (confidence 0.36). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.005, Fable 5.1 at high 0.047, Fable 5.1 at extra high 0.120, Fable 5.1 at max 0.338, Fable 5.1 at ultracode 0.010, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.005, Opus 5.5 at high 0.041, Opus 5.5 at extra high 0.106, Opus 5.5 at max 0.299, Opus 5.5 at ultracode 0.009, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.002, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.013, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between extra high and max; model near tie between Fable 5.1 and Opus 5.5. Sent 2026-10-24T02:45:51Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-24T02:45:51Z; HTTP 200 in 0.58 s; 5503 input and 71 output tokens; jev-1.13.0. Rung by rule: max (nearest to the score, halves up); model by rule: Fable 5.1 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between extra high and max; model near tie between Fable 5.1 and Opus 5.5.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "QA-70 HDE-CRD-0002 QA Plan v1.0 review", before this Plan was saved.
- **Records:** the Notion row was not written.
- **Picks:** Nathan's pick for QA-70 is not stated. Nathan's pick for this QA-50 session is not stated; its reading is in the Live QA Guide v1.0 §15 (Opus 5.5 at extra high, score 2.93).

**Surface advice:** run QA-70 in the continuing Isis session for HDE-CRD-0002 (Isis-53, https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok), as the QA-50 contract routes it, on `amthorn78/glow-hdengine-v2`. If that session cannot be continued, Nathan creates a top-level Claude Code cloud session for the Isis role on the same repository, and the review records that.
- **Reads:** Notion read access for the QA-70 prompt; this Plan, the QA Audit v1.0, the Live QA Guide v1.0, the three QA-10 v1.1 records, the Specification v1.1-approved with delta 01, Implementation Plan v1.1 with Plan delta 01 v1.1, the S19 record, the WU-OPS-01 receipt and the WU-REM-01 lineage review; `docs/pfcanon/` on `main` (PF10 v13.7.8, the Glow QA Guide, Plan Templates, HDE-Mechanics Guide, HDE-CLI-API-Vendor-Ref). It may re-check `tools/qa/generate_epic_close_pack.py`, `tools/qa/qa_harness.py` and `tools/evidence/update_evidence_index.py`, and collect the Plan's selectors locally under closed rails.
- **No access needed:** production, the vendor, Railway or the database; no publication through the evidence writer.
- **Writes:** only its review record (and any handoff) under `docs/ephemeral/`, by pull request.
- **Order:** this Plan's pull request merged first, so the review reads the Plan from `main`.

## Canon relied on

As recorded in the QA Audit v1.0 "Canon relied on" (same invocation, `main` at `0b15328d`), which lists every section read. This Plan additionally applies, read in full: Plan Templates v2.0.5 "Runbook Check Matrix", "Check Blocks", "Embedded harness checks", "Canon check clarifications" and the CHECK template with its vendor-dependent step rules (lines 698 to 773); Glow QA Guide v3.0.6 §3.4.10 (plan validity lint and syntax normalization) and §3.5.10; HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11d and §7.1.11f for check 20; Glow Infrastructure v2.3.3 §2.4 for the rails bindings; HDE Build Notes v13.7.8 addenda 2.9 (S14 black-box behaviour; LR4-O2), 2.10 (S19 classes; LR5-O1), 2.15 to 2.17 (close formats), 2.19, 2.20 and 2.26.

In-flight documents: the Live QA Guide v1.0; QA readiness v1.1; Reality Audit v1.1; Change Audit Triage v1.1; Specification v1.1-approved and delta 01; Implementation Plan v1.1 and Plan delta 01 v1.1; the S19 record; the WU-REM-01 lineage review; the WU-OPS-01 receipt; the WU-DOC-01 completion v1.1, all read as the Audit §1 states.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-50-20261024-01 (the same use as the Audit) |
| change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| unit | whole change; S01 (removed) and S02 to S22; checks 1 to 21 |
| prompt | QA-50 — Create Whole-Change QA Audit and Plan — 100926.1, page state of 2026-10-12T02:30:48.299Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-50 phase 2 (QA_PLAN) |
| capture time | 2026-10-24T02:36:06Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |
