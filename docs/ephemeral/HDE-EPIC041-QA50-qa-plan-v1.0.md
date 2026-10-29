---
artifact_type: QA_PLAN
artifact_version: "1.0"
logical_id: HDE-EPIC041-QA50-QA-PLAN
QA_PLAN_ID: docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md
state: PLAN_PENDING
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
QA_AUDIT_ID: docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE; the initial QA Audit for the epic and this Plan's locus provenance source)
predecessor: none (first QA Plan for HDE-EPIC041)
LIVE_QA_GUIDE_ID: docs/ephemeral/HDE-EPIC041-QA20-live-qa-guide-v1.0.md (LIVE_QA_GUIDE v1.0, GUIDE_READY)
QA_READINESS_ID: docs/ephemeral/HDE-EPIC041-QA10-qa-readiness-v1.0.md (READY_FOR_QA)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1, approved)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1, approved)
repository: amthorn78/glow-hdengine-v2
repository_head_read: 1e2ac50e88dd30253e3c96315fad0836d62ad79d (origin/main at authoring; provenance, not an execution predicate)
producer: Kronos, the continuing QA authority for HDE-EPIC041 (role continuity per D27)
prompt: QA-50 — Create Whole-Change QA Audit and Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81dbb28ed028d68b8816; page state 2026-10-27T13:08:15.848Z)
r1_row: GCF-21
ecosystem_release: GCFPE-20261027.1 / 102726.1
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.4.md (871 lines, sha256 b2142317093e9e89c69ee774aec61c518be3e9a8e0d7c71e2fbb21752f2ca091; provenance, not a gate)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-50
canon_conflict_register: section 21 of this Plan (CCR-1 to CCR-4 carried unchanged; CCR-5 carried, PROPOSED; CCR-6 PROPOSED by Kronos)
execution_arrangement: PENDING the Product Owner's choice (PI-01); this Plan names no executor
next_stage: QA-70 — Review Whole-Change QA Plan — 102726.1 (https://app.notion.com/p/4064590a05eb819ca94af85f1561b596), continuing Isis
authored_at: 2026-10-29 (UTC)
GCFPE_PROMPT_USES: "HDE-EPIC041-QA50-20261029 (full entry in the companion QA Audit front matter); outcome for this artifact: PLAN_PENDING; repository_persistence PENDING"
---

# HDE-EPIC041 — Live QA Plan v1.0 (QA-50): PLAN_PENDING

## 0. Front matter (Plan Templates §1)

Epic ID: HDE-EPIC041
Plan type: Live QA Plan / Runbook
Execution venue: Other: any Linux environment that meets the environment contract EC-1 to EC-5 (section 6.4); Codespaces, the canonical and preferred console, qualifies when it meets them
Approval sentinel: `ASK OK?`

Venue-specific claim: NOT CLAIMED

Why venue can affect the result: NOT APPLICABLE

Required venue evidence: NOT APPLICABLE

Effect of missing venue evidence: NOT APPLICABLE

Target environment: other: repository-local closed-rails execution on a full-history clone of `amthorn78/glow-hdengine-v2` at the execution source on `main`; no deployed, production or vendor target exists for this change (QA Audit section 9)
Plan revision: r1 (v1.0)
Date (UTC): 2026-10-29
Operators (names-only): PO, IA (Isis), QA agent (Kronos), executing agent (the Product Owner's choice)

"Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates."

No formally approved bounded Product Owner rescope applies to HDE-EPIC041.

### 0.1 Canon set (titles only; sections)

* HDE Build Notes
* PF04 — HDE-Governance, §3.4 "Open rails (controlled)"; §9.1.5 (integrated readiness, remediation and closure; escalation)
* PF06 — Change Process Guide, §0.4.1 (Discovery + QA RCA/Doc Delta); §0.7 (QA branches posture); §3.5.2.8 (Live QA via harness; functional proof; evidence landing; entrypoint regression tests in CI)
* HDE Build Checklist phase document: `PF09.3-Canon-HDE-Build-Checklist-Separation`, `Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction` and `Subtask HDE-SEPA006.3 — Boundary and behavior verification` (required indexing through the existing governed writer)
* PF12 — HDE Schemas & Artifacts, §8.17 "Scope / root" and "Current-state evidence" (the Plan decides which QA artifacts are indexed; no subdirectory enumeration)
* PF19 — Glow QA Guide, §2.3 (rails); §3.4.2, §3.4.3, §3.4.8, §3.4.9, §3.4.10 (tooling, evidence grammar, helper readiness, VCS boundary, plan lint); §4.4 (step logs); §9.2.13 "D0 discovery gate (non-token)"
* PF27 — Canon Plan Templates, §1 "Live QA Plan" (template obligations) and "Review guardrails"

PF20 is not used.

## 1. Scope statement

This plan evaluates the following in-scope surfaces and checks:

* **D0** — Discovery: execution source, rails, dependency and harness readiness, selector collection, `.gitignore` posture of the QA root, and the open-rails and caller-set precondition (check `d0-discovery`).
* **D1** — Adapter-owned chart entry `adapter/chart_orchestration.py` (R-01, AC-01; functional proof of the adapter-to-engine seam) (check `ac01-orchestration-entry`).
* **D2** — Pure Engine chart module `engine/charts/pure.py` (R-02, AC-02) (check `ac02-pure-module`).
* **D3** — Caller migration and retirement: removed `engine/charts/loader.py`, import guard, C-1 to C-3, PF09.3 retained coverage (R-03, AC-03, AC-05) (check `ac03-caller-migration`).
* **D4** — Boundary verification recorded as governed, indexed evidence (R-04, AC-04), the AC-05 tracked-file limb (check `ac05-tracked-files-unchanged`) and evidence integrity (check `qa-closeout-deliverables`), with publication through the authorized writer (section 13).
* **D5** — Doc-delta baseline of Specification §10 (check `step-0b-doc-delta-capture`).

This plan explicitly excludes:

* Any live vendor, production database, deployed-service, HTTP or CLI exercise (QA Audit section 9; no such surface is affected).
* Restoring the generator's compat computation, FND-005 to FND-007, Candidate CRD Items List items 9 and 10, and the `main` push CI classification (QR-07, QR-08).
* Re-running CI lanes, the full suite, or comparisons GitHub already records (bound in section 14).
* Canon wording that still calls the removed loader current: it is drift, recorded by Step-0B, not the contract (QR-06; AGENTS.md "HDE-EPIC041 current posture").
* The close pack, acceptance map and drain-targets file, which belong to CL-05 (section 18).
* PF document edits, PF10 drainage, PF09 status movement and PF23 updates; none is a deliverable or gate of this Plan.

## 2. PF10 overrides and conflicts

* HDE Build Notes (planning documents serve planning only) → no QA evidence artifact, manifest, path proof, Index or Mirror row reads, binds, hashes, resolves or requires a path under `docs/ephemeral/`; this Plan is cited in evidence by title only, and the Step-0B and closeout predicates reject `docs/ephemeral` and `docs/pfcanon` strings in the doc-delta pair → PF06 §0.4.1, §3.5.2.8; PF19 §3.4.3; PF12 §8.17.
* HDE Build Notes (PF-Canon is resolved by stable identity, never by version) → evidence cites PF documents by title; Step-0B resolves canon files at run time by versionless pattern and refuses a non-unique match → PF27 "Canon precedence for template use"; PF19 §4.4.5.
* HDE Build Notes (the close-pack writer runs only at close) → no QA step writes a close pack; the QA RCA & Doc Delta summary is rendered at CL-05 (section 18); CCR-5 governs ordering → PF06 §3.5.1; PF19 §3.1.3; PF27 §3B.

## 3. Open-Rails Live QA Requirement

Carried verbatim (Specification v1.1 §4; Plan v1.1 §11):

* **Item 3.** "*Binding condition.* If the Implementation Audit finds that any affected surface, including the new orchestration entry, is used to produce such a feature, or reaches vendor acquisition in a deployed or CLI path, the mandatory bounded live vendor test (synthetic data only, `SAFE_MODE=0`, `ALLOW_NETWORK=1`) applies to this Epic's QA Plan. No exemption or non-vendor substitute then applies. Closed-rails proof, static validation, repository inspection, generated evidence, an OPS observation or exemption language does not replace it."
* **Item 4.** "*Broader scope.* This Specification records no exemption from the broader production-affecting open-rails requirement. If the Implementation Audit finds the changed boundary can affect runtime compute, vendor ingest, database retrieval or production-used CLI/API behavior, the QA Plan must carry a bounded open-rails step or an exemption authorized and recorded under the Product Owner. Silence is not an exemption."
* **Item 5.** "*Authorization.* The row authorizes no live vendor or production database activity. Any live step needs separate, task-specific Product Owner authorization (§9)."

**Determination (QA Audit section 9): neither item 3 nor item 4 is met.** No production entry point (`Procfile` `web`, console script `hdctl`) imports or loads `adapter/chart_orchestration.py` or `engine/charts/pure.py`, and the entry acquires nothing from a vendor or database. The epic is outside the production-functional and the production-affecting scope of PF04 §3.4, so this Plan carries no open-rails step and needs no exemption; this is an affirmative determination, not silence. The Plan authorizes no live step. **Re-attachment:** check `d0-discovery` re-tests the caller set at the execution source; any difference blocks execution (`TOOLING_BLOCKED`) and returns the determination to Kronos, and a live step would then need separate, task-specific Product Owner authorization.

## 4. Reality Audits historical context

Not used. No PF23 Reality Audit is a dependency, check, deliverable or gate. The QA-10 Reality Audit record is cited only for evidence ids, as provenance.

## 5. Step classes and functional proof

Every check is class 2 (internal functional and determinism) or evidence capture and publication (Glow QA Guide §3.5.6); no class 1 or class 3 step exists. The functional seam this change alters is the adapter-to-engine chart path (PF06 §3.5.2.8); check `ac01-orchestration-entry` is its named functional proof check and exercises it at runtime through the harness, producing governed evidence. Checks `ac02-pure-module` and `ac03-caller-migration` add runtime proof for the pure module and for each migrated caller.

## 6. Environment and rails posture

### 6.1 Determinism pins (canonical pins only)

`LC_ALL=C`, `LANG=C`, `TZ=UTC` for every step. No other pin is added.

### 6.2 Rails posture

Default rails for every check: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`. No check changes rails. `test_safe_mode_field` in `tests/adapter/test_chart_orchestration.py` sets `SAFE_MODE` to `1`, to `0` and removes it inside its own process by `monkeypatch` to observe the entry's `safe_mode` log field; that is an input to the function under test inside a closed-network process, not a rails opening, and the process rails stay as above (QA Audit section 4.4).

### 6.3 VCS mutation and exact-source identity boundary

* This Plan instructs no branch creation, checkout, commit, push, merge, rebase or pull request as a QA execution step. Evidence lands through the separately authorized landing lane (section 13.3).
* Read-only `git` observations record the execution source; they are never a source-identity PASS predicate. The one `git diff` predicate (check `ac05-tracked-files-unchanged`) is the Specification's AC-05 behavior predicate, "running the covering tests leaves tracked files unchanged", and the same predicate CI enforces (ci.yml L129 to L130); it is not attribution.
* No step requires equality to a preplanned commit. D0 records the actual source (`git rev-parse HEAD`) and validates the required code posture through the caller-set precondition. The landing pull request records its base, reviewed head, exact-head CI and merge commit as they occur; the tested source stays distinct from the evidence-storage commit and review-time HEAD.

### 6.4 Environment contract (prerequisites, not QA steps)

* **EC-1.** A full-history clone of `amthorn78/glow-hdengine-v2` with `main` checked out at the execution source and a clean tracked tree, provided by the execution arrangement. The Plan does not instruct the checkout.
* **EC-2.** A Python 3.12 virtual environment at `/tmp/hde-epic041-qa/venv` (another `/tmp` path may be used; record it) with CI's install run **from the execution clone's root** (QA Audit section 4.1, IR-11): `/tmp/hde-epic041-qa/venv/bin/python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`. The install reaches the package index; that network use is dependency setup only.
* **EC-3.** A scratch home `/tmp/hde-epic041-qa/home` and the four script files of section 9.2 under `/tmp/hde-epic041-qa/`. Nothing under `/tmp` is evidence.
* **EC-4.** `bash`, `git`, `cmp`, `grep`, `cut`, `sort`, `date` and `sha256sum` on `/usr/bin:/bin`.
* **EC-5.** Every QA command runs from the execution clone's root behind the closed-environment prefix CS-ENV (section 9.1). Credentials present in the operator's shell are not passed.

## 7. PO inputs needed

* **PI-01 — Execution arrangement.** Executor, tools and venue for checks 1 to 7 and the publication steps (D27). The Plan names none and requires no particular session.
* **PI-02 — IDX-01 authorship and landing route.** Who authors the writer registration work item IDX-01 (section 13.1), and approval of landing route A (section 13.3) for it, or, if route A is declined, route C.
* **PI-03 — Landing lane authorization.** Who performs the branch, commit, push and pull request of the landing route. Nathan alone merges.
* **Secrets and vendor inputs.** None. `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `HDAPI_BASE_URL` are not required and not read; no check runs a vendor call. A missing required input at run time is `TOOLING_BLOCKED`; nothing is guessed.

## 8. Evidence posture and directory structure

### 8.1 Root, layout and header

* EPIC_QA_ROOT = `audit/qa/hde-epic041/` (Canon-defined grammar; QA-created). It is absent before execution (QA Audit section 5) and is created by check `d0-discovery`.
* Current-state, check-centric layout only: `audit/qa/hde-epic041/checks/<check_id>/primary.log` per check, the manifest `audit/qa/hde-epic041/qa_step_logs_manifest.json` with `audit/qa/hde-epic041/qa_step_logs_manifest.json.path_proof.txt`, and `audit/qa/hde-epic041/00_meta/doc_deltas.md`. No per-run, timestamped or latest root; no `run_id`.
* Every `primary.log` is written by `record_check` in `tools/qa/qa_harness.py` with a `pf27.step_log_header.v2` header (14 keys), statuses `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `PARKED`, `captured_env` with the six admitted keys, `intended_tokens` and `claimed_tokens` both `[]`. The manifest entry for each recorded check carries `check_id`, `log_path` and `status`; a `TOOLING_BLOCKED` check stays listed.

### 8.2 Pre-existing loci (Audit-proven) versus QA-run artifacts (QA-created)

Pre-existing loci this Plan uses, each copied verbatim from the QA Audit section 5 (L-01 to L-31): `adapter/chart_orchestration.py`, `engine/charts/pure.py`, `engine/charts/loader.py` (absent), `scripts/make_compat_determinism_artifacts.py`, the nine test selectors of L-05 to L-13, `tools/qa/qa_harness.py`, `tools/evidence/update_evidence_index.py`, `tools/evidence/orientation_demo.py`, `tools/evidence/validate_evidence_paths.py`, `tools/evidence/check_lf_endings.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh`, `ci/checks/classify_ci_changes.py`, the writer-owned files of L-23, `tests/ops/test_evidence_index.py`, `.github/workflows/ci.yml` and the canon patterns and text keys of L-29 and L-30. Presence gating applies only to these.

QA-run artifacts (all QA-created; NOT RUN until execution; none is a preflight requirement):

| Check | Files it creates (each gets a sibling `.path_proof.txt`) |
| :- | :- |
| `d0-discovery` | `audit/qa/hde-epic041/checks/d0-discovery/primary.log`, `audit/qa/hde-epic041/checks/d0-discovery/d0-env-rails.txt`, `audit/qa/hde-epic041/checks/d0-discovery/d0-entrypoint-preflight.txt`, `audit/qa/hde-epic041/checks/d0-discovery/d0-gitignore-audit-qa.txt`, `audit/qa/hde-epic041/checks/d0-discovery/d0-caller-set.txt`, `audit/qa/hde-epic041/qa_step_logs_manifest.json` |
| `step-0b-doc-delta-capture` | `audit/qa/hde-epic041/checks/step-0b-doc-delta-capture/primary.log`, `audit/docdeltas/hde-epic041_doc_deltas.md`, `audit/qa/hde-epic041/00_meta/doc_deltas.md` |
| `ac01-orchestration-entry` | `audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log` |
| `ac02-pure-module` | `audit/qa/hde-epic041/checks/ac02-pure-module/primary.log` |
| `ac03-caller-migration` | `audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log` |
| `ac05-tracked-files-unchanged` | `audit/qa/hde-epic041/checks/ac05-tracked-files-unchanged/primary.log` |
| `qa-closeout-deliverables` | `audit/qa/hde-epic041/checks/qa-closeout-deliverables/primary.log` |
| Conditional, only after a bounded rerun of a check (section 16.2); `<check_id>` is that check's id from the matrix | `audit/qa/hde-epic041/checks/<check_id>/tmp_attempt1_primary.log` and `audit/qa/hde-epic041/checks/<check_id>/tmp_attempt1_remediation_note.txt`; for check 1 also `tmp_attempt1_d0-env-rails.txt`, `tmp_attempt1_d0-entrypoint-preflight.txt`, `tmp_attempt1_d0-gitignore-audit-qa.txt` and `tmp_attempt1_d0-caller-set.txt` in the same directory. Example: `audit/qa/hde-epic041/checks/ac02-pure-module/tmp_attempt1_primary.log`. When the condition is unmet these files are not expected |

The manifest is rewritten by every check; its path proof is refreshed after every manifest update. All QA-created writes stay under `audit/**`.

### 8.3 Registration set (which artifacts are indexed; PF12 §8.17)

Every QA-run artifact above, and no other file, is indexed through the authorized writer, each row with `"epic_id": "HDE-EPIC041"`. Artifact keys:

* `epic041.qa_step_logs_manifest` → `audit/qa/hde-epic041/qa_step_logs_manifest.json`
* `epic041.doc_deltas` → `audit/docdeltas/hde-epic041_doc_deltas.md`
* Every other file under `audit/qa/hde-epic041/`: the key is its repository path with each `/` replaced by `.` and each `-` replaced by `_`, the convention of the HDE-EPIC040 rows in `tools/evidence/update_evidence_index.py`. The 12 unconditional keys are `audit.qa.hde_epic041.00_meta.doc_deltas.md`, `audit.qa.hde_epic041.checks.d0_discovery.primary.log`, `audit.qa.hde_epic041.checks.d0_discovery.d0_env_rails.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_entrypoint_preflight.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_gitignore_audit_qa.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_caller_set.txt`, `audit.qa.hde_epic041.checks.step_0b_doc_delta_capture.primary.log`, `audit.qa.hde_epic041.checks.ac01_orchestration_entry.primary.log`, `audit.qa.hde_epic041.checks.ac02_pure_module.primary.log`, `audit.qa.hde_epic041.checks.ac03_caller_migration.primary.log`, `audit.qa.hde_epic041.checks.ac05_tracked_files_unchanged.primary.log` and `audit.qa.hde_epic041.checks.qa_closeout_deliverables.primary.log`.

Path proofs are written at capture time by each check's publication step (snippet CS-3) so that `produced_at_utc` is the capture time; the writer keeps a matching proof. Transient scratch under `/tmp` is never registered; nothing else is registered.

## 9. Command snippets, scripts and preapproval smoke validation

Plans may define command snippets once and reference them by local id (Plan Templates "Command syntax latitude"); each primary log records the resolved command. Commands are intent carriers: an operator may normalize syntax in flight when proof target, check identity, rails, evidence identity and verdict meaning stay unchanged, and records the normalization (section 16.4).

### 9.1 Snippets

* **CS-ENV** (closed-environment prefix for every QA command): `env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`
* **CS-1** (run and record a pytest check through the tracked harness; arguments: check id, check name, extra evidence paths comma-separated or empty, then the pytest selectors and `-p no:cacheprovider`): `python -c "import dataclasses, sys; from tools.qa.qa_harness import HarnessConfig, record_check, run_pytest_check; c = HarnessConfig('HDE-EPIC041'); cid, name, extra = sys.argv[1:4]; r = run_pytest_check(c, cid, sys.argv[4:], check_name=name); r = dataclasses.replace(r, evidence_artifacts=tuple(x for x in extra.split(',') if x)) if extra else r; record_check(c, r); print('status=' + r.status.value, 'exit_code=' + str(r.exit_code))"`
* **CS-2** (run a check script with `bash -c` and record it through the tracked harness; arguments: check id, check name, the status for script exit 1, command provenance, extra evidence paths comma-separated or empty, script file; exit 0 records `PASS`, exit 1 the given status, exit 3 `TOOLING_BLOCKED`, any other exit `FAIL_TOOLING`; `status_reason` is the script's `REASON:` lines): `python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))"`
* **CS-3** (write capture-time path proofs with the writer's tracked `_refresh_path_proof` API, then verify them in check mode; arguments: the capture time, then the files): `python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"` followed by the files.
* **CS-4** (preserve attempt 1 before a bounded rerun of check X; run with `d` set to the check directory, for example `d=audit/qa/hde-epic041/checks/ac02-pure-module`): `for f in "$d"/*; do b=$(basename "$f"); case "$b" in tmp_attempt1_*|*.path_proof.txt) ;; *) cp -p "$f" "$d/tmp_attempt1_$b";; esac; done`
* **CS-5** (append one plan-versus-execution drift item to both doc-delta surfaces, then refresh both proofs with CS-3), for example: `printf '%s\n' '- DRIFT-001 (CAVEAT; drives decision: No): check ac02-pure-module was rerun once after attempt 1 was TOOLING_BLOCKED by a missing install; its executed commands are recorded in audit/qa/hde-epic041/checks/ac02-pure-module/primary.log.' | tee -a audit/docdeltas/hde-epic041_doc_deltas.md >> audit/qa/hde-epic041/00_meta/doc_deltas.md`

CS-1 to CS-3 invoke tracked, tested repository entrypoints through `python -c` (Glow QA Guide §3.4.8): `HarnessConfig`, `run_pytest_check`, `record_check`, `CheckResult` and `Status` from `tools/qa/qa_harness.py`, and `_refresh_path_proof` from `tools/evidence/update_evidence_index.py`, the form HDE-EPIC040's QA-70 decision C040-09 approved. Their CI entrypoint regression tests are `tests/qa/test_generic_qa_harness.py::test_pf27_header_and_manifest_replace_by_check_id`, `tests/qa/test_generic_qa_harness.py::test_same_interpreter_and_classification` and `tests/evidence/test_evidence_skeleton.py::test_refresh_path_proof_supports_staged_missing_artifact` (PF06 §3.5.2.8 "Entrypoint regression test exists in CI"). Every product-behavior predicate is decided by a tracked, CI-registered test; the scripts below decide only preflight, evidence assembly and the AC-05 tracked-file predicate.

### 9.2 Scripts (QA-created execution helpers under `/tmp`; never evidence)

The operator writes each script's lines, in order, each followed by one LF, to the named file, and confirms with `sha256sum` that the file matches the digest given before running it. The exact bytes run are recorded in the check's primary log (the `command` field), so the `/tmp` file is never referenced as evidence.

**Script SC-D0** (used by check `d0-discovery`): file `/tmp/hde-epic041-qa/d0-discovery.sh`, 24 lines, 5075 bytes, sha256 `00092b587aa0c12a32dd0b8c5053fe0de4656e27876c8c58c3dcd2a959be476a`. Lines, in order:

1. `set -u`
2. `d=audit/qa/hde-epic041/checks/d0-discovery`
3. `r=0`
4. `echo "QA root before this check:"; ls -la audit/qa/hde-epic041 2>&1 | head -n 40`
5. `echo "doc-delta draft before this check:"; ls -l audit/docdeltas/hde-epic041_doc_deltas.md 2>&1`
6. `mkdir -p "$d"`
7. `echo "execution_source: $(git rev-parse HEAD)"`
8. `echo "execution_source_commit: $(git log -1 --format='%cI %s')"`
9. `if git diff --quiet HEAD; then echo "tracked_tree_clean: yes"; else echo "tracked_tree_clean: no"; git diff --stat HEAD; echo "REASON: tracked files are modified before QA"; r=3; fi`
10. `echo "untracked at start (supplementary):"; git status --porcelain --untracked-files=all`
11. `{ echo "environment names:"; env | cut -d= -f1 | sort; echo "rails: SAFE_MODE=${SAFE_MODE-UNSET} ALLOW_NETWORK=${ALLOW_NETWORK-UNSET} APP_ENV=${APP_ENV-UNSET} LC_ALL=${LC_ALL-UNSET} LANG=${LANG-UNSET} TZ=${TZ-UNSET}"; python --version; python -m pip --version; python -m pip list --format=freeze; python -m pytest --version; } > "$d/d0-env-rails.txt" 2>&1 || { echo "REASON: pytest readiness failed"; r=3; }`
12. `{ ls -l tests/adapter/test_chart_orchestration.py tests/charts/test_chart_pure_purity.py tests/charts/test_chart_pure_interface.py tests/charts/test_chart_loader_import_guard.py tests/scripts/test_make_compat_determinism_artifacts.py tests/loader/test_load_chart_fixture_only.py tests/loader/test_loader_logs_keys_only.py tests/provider/test_vendor_and_prod_guard_min.py tests/provider/test_vendor_call_rails_and_config.py adapter/chart_orchestration.py engine/charts/pure.py scripts/make_compat_determinism_artifacts.py tools/qa/qa_harness.py tools/evidence/update_evidence_index.py tools/evidence/orientation_demo.py tools/evidence/validate_evidence_paths.py tools/evidence/check_lf_endings.py ci/checks/check_mirror_schema.sh ci/checks/check_evidence_index_hash.sh && python -c "from tools.qa.qa_harness import HarnessConfig, validate_check_id; c = HarnessConfig('HDE-EPIC041'); [validate_check_id(i) for i in ('d0-discovery', 'step-0b-doc-delta-capture', 'ac01-orchestration-entry', 'ac02-pure-module', 'ac03-caller-migration', 'ac05-tracked-files-unchanged', 'qa-closeout-deliverables')]; print('harness_registration: HDE-EPIC041 ->', c.qa_root.relative_to(c.repo_root))" && python -m pytest --collect-only -q -p no:cacheprovider tests/adapter/test_chart_orchestration.py tests/charts/test_chart_pure_purity.py tests/charts/test_chart_pure_interface.py tests/charts/test_chart_loader_import_guard.py tests/scripts/test_make_compat_determinism_artifacts.py tests/loader/test_load_chart_fixture_only.py tests/loader/test_loader_logs_keys_only.py tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on; } > "$d/d0-entrypoint-preflight.txt" 2>&1 || { echo "REASON: an entrypoint, the harness registration or selector collection failed"; r=3; }`
13. `grep -q -E '^43 tests collected' "$d/d0-entrypoint-preflight.txt" || { echo "REASON: selector collection is not exactly 43 tests"; r=3; }`
14. `{ git check-ignore -v --no-index audit/qa/hde-epic041/qa_step_logs_manifest.json audit/qa/hde-epic041/qa_step_logs_manifest.json.path_proof.txt audit/qa/hde-epic041/checks/d0-discovery/primary.log audit/qa/hde-epic041/checks/d0-discovery/primary.log.path_proof.txt audit/qa/hde-epic041/00_meta/doc_deltas.md audit/docdeltas/hde-epic041_doc_deltas.md; echo "check_ignore_exit_code: $?"; } > "$d/d0-gitignore-audit-qa.txt" 2>&1`
15. `grep -q '^check_ignore_exit_code: 1$' "$d/d0-gitignore-audit-qa.txt" || { echo "REASON: a QA evidence path is git-ignored or check-ignore failed"; r=3; }`
16. `exp=$(printf '%s\n' adapter/chart_orchestration.py ci/checks/classify_ci_changes.py engine/charts/pure.py scripts/make_compat_determinism_artifacts.py tests/adapter/test_chart_orchestration.py tests/charts/test_chart_loader_import_guard.py tests/charts/test_chart_pure_interface.py tests/charts/test_chart_pure_purity.py tests/loader/test_load_chart_fixture_only.py tests/loader/test_loader_logs_keys_only.py tests/scripts/test_make_compat_determinism_artifacts.py)`
17. `got=$(git grep -l -E 'chart_orchestration|engine\.charts' -- '*.py' ':(exclude)docs/ephemeral/' ':(exclude)docs/pfcanon/' ':(exclude).audit_src/')`
18. `{ echo "expected (QA Audit):"; printf '%s\n' "$exp"; echo "observed:"; printf '%s\n' "$got"; } > "$d/d0-caller-set.txt"`
19. `[ "$got" = "$exp" ] || { echo "REASON: the Python files naming the chart entry or the Engine chart package differ from the QA Audit set"; r=3; }`
20. `echo "writer registration lines for HDE-EPIC041 (supplementary):"; grep -c EPIC041_QA_PRIMARY_ARTIFACTS tools/evidence/update_evidence_index.py || true`
21. `echo "evidence graph baseline (supplementary):"; python tools/evidence/update_evidence_index.py --check; echo "writer_check_exit_code: $?"`
22. `echo "reachable surfaces: repository-local closed-rails execution only; no deployed service, HTTP route, CLI command, vendor or database is exercised"`
23. `for f in d0-env-rails.txt d0-entrypoint-preflight.txt d0-gitignore-audit-qa.txt d0-caller-set.txt; do echo "sidecar: $d/$f"; done`
24. `exit $r`

**Script SC-0B** (used by check `step-0b-doc-delta-capture`): file `/tmp/hde-epic041-qa/step-0b-doc-delta-capture.sh`, 23 lines, 2870 bytes, sha256 `ceffcbcd2c20c916af3ba58a6e3cf345ec521c685a54894f821b3dd4533c8003`. Lines, in order:

1. `set -u`
2. `for t in git grep cmp python; do command -v "$t" >/dev/null || { echo "REASON: $t is not on PATH"; exit 3; }; done`
3. `dd=audit/docdeltas/hde-epic041_doc_deltas.md`
4. `rec=audit/qa/hde-epic041/00_meta/doc_deltas.md`
5. `if [ -e "$dd" ] || [ -e "$rec" ]; then ls -l "$dd" "$rec" 2>&1; echo "REASON: a doc-delta surface already exists and is preserved unchanged"; exit 3; fi`
6. `python -c "import json, sys; m = json.load(open('audit/qa/hde-epic041/qa_step_logs_manifest.json')); sys.exit(0 if m.get('d0-discovery', {}).get('status') == 'PASS' else 3)" || { echo "REASON: d0-discovery is not recorded as PASS"; exit 3; }`
7. `set -- docs/pfcanon/PF02-Canon-HDE-Architecture-v*.md; [ $# -eq 1 ] && [ -f "$1" ] || { echo "REASON: HDE Architecture does not resolve to one controlled file"; exit 3; }; f1=$1`
8. `set -- docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v*.md; [ $# -eq 1 ] && [ -f "$1" ] || { echo "REASON: HDE Mechanics Guide does not resolve to one controlled file"; exit 3; }; f2=$1`
9. `set -- docs/pfcanon/PF31-Reference-HDE-State-of-the-Repository-v*.md; [ $# -eq 1 ] && [ -f "$1" ] || { echo "REASON: HDE State of the Repository does not resolve to one controlled file"; exit 3; }; f3=$1`
10. `k1='The checked-in loader remains current repository reality until separately remediated'`
11. `k2='The non-BodyGraph loader responsibility represented by'`
12. `k3='still mixes input normalization with environment inspection, clocks, provider orchestration, and filesystem logging'`
13. `item() { if grep -q -F "$3" "$4"; then printf '%s\n' "- $1 (CAVEAT; drives decision: No): $2 still contains the text \"$3\", which describes the removed chart loader as current. Drain target: $2, owner Product Owner, after all QA tasks are complete.$5"; else printf '%s\n' "- $1 (resolved at this source): $2 no longer contains the text \"$3\"; nothing remains to drain for this item."; fi; }`
14. `mkdir -p audit/docdeltas audit/qa/hde-epic041/00_meta`
15. `{ printf '%s\n' '# HDE-EPIC041 doc deltas (Step-0B)' '' 'Written by check step-0b-doc-delta-capture of the HDE-EPIC041 Live QA Plan v1.0. PF documents are named by title. Every item is a non-mandatory drain candidate owned by the Product Owner; none is a QA gate or a close blocker.' '' '## BLOCKERS' '' 'none' '' '## CAVEATS' ''; item DELTA-001 'HDE Architecture §1.1' "$k1" "$f1" ''; item DELTA-002 'HDE Mechanics Guide §1.1' "$k2" "$f2" ''; item DELTA-003 'HDE State of the Repository §2.2' "$k3" "$f3" ' This item is a candidate; HDE State of the Repository is a reference document.'; } > "$dd"`
16. `cp "$dd" "$rec"`
17. `cmp "$dd" "$rec" || { echo "REASON: the doc-delta pair differs"; exit 1; }`
18. `if grep -n -E 'docs/ephemeral|docs/pfcanon' "$dd"; then echo "REASON: the doc delta names a planning or canon path"; exit 1; fi`
19. `grep -q -E '^- DELTA-00[123] ' "$dd" || { echo "REASON: no doc-delta item was written"; exit 1; }`
20. `cat "$dd"`
21. `echo "written: $dd"`
22. `echo "written: $rec"`
23. `exit 0`

**Script SC-05** (used by check `ac05-tracked-files-unchanged`): file `/tmp/hde-epic041-qa/ac05-tracked-files-unchanged.sh`, 10 lines, 861 bytes, sha256 `139bd41ca5a91eca0557a6ae546ab9918429d138828e9268e99f7c62e74d772d`. Lines, in order:

1. `set -u`
2. `command -v git >/dev/null || { echo "REASON: git is not on PATH"; exit 3; }`
3. `git diff --exit-code --stat HEAD -- . ':(exclude)audit/qa/hde-epic041' ':(exclude)audit/docdeltas/hde-epic041_doc_deltas.md' ':(exclude)audit/docdeltas/hde-epic041_doc_deltas.md.path_proof.txt'`
4. `rc=$?`
5. `echo "tracked_diff_exit_code: $rc"`
6. `echo "untracked outside the QA evidence paths (supplementary, non-gating):"`
7. `git status --porcelain --untracked-files=all -- . ':(exclude)audit/qa/hde-epic041' ':(exclude)audit/docdeltas/hde-epic041_doc_deltas.md' ':(exclude)audit/docdeltas/hde-epic041_doc_deltas.md.path_proof.txt'`
8. `if [ "$rc" -eq 0 ]; then echo "tracked files unchanged after checks ac01, ac02 and ac03"; exit 0; fi`
9. `if [ "$rc" -eq 1 ]; then echo "REASON: tracked files changed after the covering test runs"; exit 1; fi`
10. `echo "REASON: git diff could not run (exit $rc)"; exit 3`

**Script SC-CL** (used by check `qa-closeout-deliverables`): file `/tmp/hde-epic041-qa/qa-closeout-deliverables.sh`, 8 lines, 1695 bytes, sha256 `d5420d277ab7cb840efc5cb4eb95d64806addb2398f4a8ce0772dc61ead95a45`. Lines, in order:

1. `set -u`
2. `python -c "import tools.evidence.update_evidence_index" || { echo "REASON: the evidence writer module does not import"; exit 3; }`
3. `python -c "import json, sys; m = json.load(open('audit/qa/hde-epic041/qa_step_logs_manifest.json')); need = ('d0-discovery', 'step-0b-doc-delta-capture', 'ac01-orchestration-entry', 'ac02-pure-module', 'ac03-caller-migration', 'ac05-tracked-files-unchanged'); [print('manifest:', k, m[k]['status'], m[k]['log_path']) for k in sorted(m)]; miss = [k for k in need if k not in m]; print('REASON: the manifest lacks ' + ' '.join(miss)) if miss else None; sys.exit(3 if miss else 0)" || exit $?`
4. `python -c "import datetime, json; import tools.evidence.update_evidence_index as u; m = json.load(open('audit/qa/hde-epic041/qa_step_logs_manifest.json')); t = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'); ps = sorted({a for e in m.values() for a in json.loads(open(e['log_path'], encoding='utf-8').readline())['evidence_artifacts']} | {'audit/qa/hde-epic041/qa_step_logs_manifest.json', 'audit/docdeltas/hde-epic041_doc_deltas.md', 'audit/qa/hde-epic041/00_meta/doc_deltas.md'}); [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; [print('proof valid:', p) for p in ps]" || { echo "REASON: a path proof is missing or does not match its file"; exit 1; }`
5. `cmp audit/docdeltas/hde-epic041_doc_deltas.md audit/qa/hde-epic041/00_meta/doc_deltas.md || { echo "REASON: the doc-delta pair differs"; exit 1; }`
6. `if grep -n -E 'docs/ephemeral|docs/pfcanon' audit/docdeltas/hde-epic041_doc_deltas.md; then echo "REASON: the doc delta names a planning or canon path"; exit 1; fi`
7. `echo "closeout predicates hold"`
8. `exit 0`

### 9.3 Interactive-shell safety

Every check runs inside a `bash -c` subprocess or a `python -c` process; no snippet uses shell-terminating control flow in the operator's shell, and a failing predicate is captured as a status, so evidence capture continues (Glow QA Guide §4.3).

### 9.4 Preapproval smoke validation (Glow QA Guide §3.4.8 "Execution-critical helper readiness")

Kronos validated the exact final snippets CS-1 to CS-5 and the four scripts above, extracted mechanically from this file, on 2026-10-29 in a throwaway full-history clone at `1e2ac50e88dd30253e3c96315fad0836d62ad79d`, working directory the clone root, Python 3.12.3 virtual environment with CI's install from that clone, under CS-ENV (with that environment's paths). Established: repository-root resolution (`HarnessConfig('HDE-EPIC041')` resolved the clone root); imports and argument parsing of all snippets; complete collection of the nine selectors (`43 tests collected`) and their import closure; runtime, development and test dependency readiness (`pytest 8.4.2`); pins (`captured_env` shows the six values); non-mutating startup (tracked tree unchanged). Result: each script file matched its digest; all seven checks recorded `PASS` in plan order; every path proof written by CS-3 verified; the worked rerun example of section 16.2 (CS-4, the note, CS-1 with the preserved files listed, CS-3) recorded `PASS` and CS-5 kept the pair byte-identical; `qa-closeout-deliverables` then verified all 16 proofs it covers. Negative rehearsals with the same scripts: a tracked modification before D0 recorded `TOOLING_BLOCKED` ("tracked files are modified before QA"); a tracked modification before the AC-05 check recorded `FAIL_BEHAVIOR` ("tracked files changed after the covering test runs"). A rehearsal of IDX-01 (16 rows built by the rule of section 8.3, including the two conditional rerun files) and IDX-RUN (section 13) took the Index from 653 to 669 rows; the six read-only validators exited 0 and the row confirmation command listed exactly those 16 rows (QA Audit section 10.4). Everything was discarded; the clone returned clean to `1e2ac50e`. This is preapproval smoke validation, not QA execution or evidence.

## 10. Mandatory Step-0 artifacts

* **Step-0A** is reserved for identifier compatibility; this Plan defines no Step-0A obligation.
* **Step-0B — Doc Delta Capture** is check `step-0b-doc-delta-capture` (section 12.2). It writes the two-surface pair: draft and staging surface `audit/docdeltas/hde-epic041_doc_deltas.md` (in-flight doc-delta evidence) and epic-scoped capture `audit/qa/hde-epic041/00_meta/doc_deltas.md` (authoritative record surface), byte-identical, generated by commands, BLOCKERS and CAVEATS separated with stable ids, PF documents named by title. It never overwrites an existing surface: if either exists it records `TOOLING_BLOCKED` and preserves it. "No deltas" is not emitted, because DELTA-001 to DELTA-003 are known. Plan-versus-execution drift found later (a normalized command, a rerun, a Moon Loop) is appended by CS-5, generated by command, before check 7; check 7 verifies the pair stays byte-identical and proofed.
* **Moon Loop clause (bounded).** Allowed only to correct QA-created surfaces under `audit/qa/hde-epic041/` or `audit/docdeltas/hde-epic041_doc_deltas.md`, or a transcription defect in a `/tmp` script, when the proof target, evidence identity, rails and acceptance meaning are unchanged; it is recorded through CS-4 and CS-5 with changed paths and why. A change to product code, tests, tools (including the evidence writer), governed artifacts outside the QA root or a PF document is not Moon Loop; it is routed remediation (PR, OPS, QA_PLAN_UPDATE or DOC_UPDATE) and is cited before any final PASS that depends on it. Stop and escalate when the correction is not minimal.
* **Step-0C** does not apply: no prod-like behavior is claimed.

## 11. Runbook Check Matrix

Commands are given in full in each check block (section 12); this matrix names them by snippet.

| check_id | check_name | D-goal | rails posture | commands (authorized executor) | expected result | primary evidence | deliverables | tokens (optional) | PF anchors |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| `d0-discovery` | D0 discovery | D0 | SAFE_MODE=1; ALLOW_NETWORK=0; APP_ENV=dev | CS-2 with SC-D0; CS-3 | PASS if every precondition holds; TOOLING_BLOCKED if any fails | `audit/qa/hde-epic041/checks/d0-discovery/primary.log` | primary, four sidecars, manifest, proofs | [INTENTIONALLY LEFT BLANK] | PF06 §0.4.1.1; PF19 §3.4.2, §9.2.13 |
| `step-0b-doc-delta-capture` | Step-0B doc delta capture | D5 | SAFE_MODE=1; ALLOW_NETWORK=0; APP_ENV=dev | CS-2 with SC-0B; CS-3 | PASS if the pair is written, identical and lists DELTA-001 to -003; FAIL_TOOLING if a generated-byte predicate fails; TOOLING_BLOCKED if a surface pre-exists, D0 is not PASS or canon does not resolve uniquely | `audit/qa/hde-epic041/checks/step-0b-doc-delta-capture/primary.log` | primary, doc-delta pair, proofs | [INTENTIONALLY LEFT BLANK] | PF27 "Step-0B — Doc Delta Capture" |
| `ac01-orchestration-entry` | Adapter-owned chart entry functional proof | D1, D4 | SAFE_MODE=1; ALLOW_NETWORK=0; APP_ENV=dev | CS-1 over L-05; CS-3 | PASS if pytest exits 0 (20 passed); FAIL_BEHAVIOR if a test fails; TOOLING_BLOCKED or FAIL_TOOLING per harness map | `audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log` | primary, proof | [INTENTIONALLY LEFT BLANK] | PF06 §3.5.2.8 functional proof; PF09.3 HDE-SEPA006.3 |
| `ac02-pure-module` | Pure Engine chart module purity and interface | D2, D4 | SAFE_MODE=1; ALLOW_NETWORK=0; APP_ENV=dev | CS-1 over L-06, L-07; CS-3 | PASS if pytest exits 0 (13 passed); otherwise per harness map | `audit/qa/hde-epic041/checks/ac02-pure-module/primary.log` | primary, proof | [INTENTIONALLY LEFT BLANK] | PF09.3 HDE-SEPA006.1, .3 |
| `ac03-caller-migration` | Caller migration, retirement guard and retained coverage | D3, D4 | SAFE_MODE=1; ALLOW_NETWORK=0; APP_ENV=dev | CS-1 over L-08 to L-13; CS-3 | PASS if pytest exits 0 (10 passed); otherwise per harness map | `audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log` | primary, proof | [INTENTIONALLY LEFT BLANK] | PF09.3 HDE-SEPA006.2, .3 |
| `ac05-tracked-files-unchanged` | Tracked files unchanged after the covering runs | D4 | SAFE_MODE=1; ALLOW_NETWORK=0; APP_ENV=dev | CS-2 with SC-05; CS-3 | PASS if no tracked file outside the QA evidence paths changed; FAIL_BEHAVIOR if one did; TOOLING_BLOCKED if git cannot run | `audit/qa/hde-epic041/checks/ac05-tracked-files-unchanged/primary.log` | primary, proof | [INTENTIONALLY LEFT BLANK] | PF09.3 HDE-SEPA006.3; PF19 §3.4.9; Specification AC-05 |
| `qa-closeout-deliverables` | QA closeout deliverables integrity | D4 | SAFE_MODE=1; ALLOW_NETWORK=0; APP_ENV=dev | CS-2 with SC-CL; CS-3 | PASS if the six earlier checks are recorded, every proof verifies and the pair is identical and path-free; FAIL_TOOLING if not; TOOLING_BLOCKED if a check is missing | `audit/qa/hde-epic041/checks/qa-closeout-deliverables/primary.log` | primary, proof | [INTENTIONALLY LEFT BLANK] | PF19 §3.4.3; PF27 "Close-out deliverables" |

Every row has a check block. No legacy acceptance token is in scope (Specification §8); every header records `intended_tokens: []` and `claimed_tokens: []`.

## 12. Check blocks

Common to every check: rails `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; pins `LC_ALL=C LANG=C TZ=UTC`; tokens `intended_tokens: []`, `claimed_tokens: []`; manifest `audit/qa/hde-epic041/qa_step_logs_manifest.json` (Canon-defined grammar; QA-created) and its proof `audit/qa/hde-epic041/qa_step_logs_manifest.json.path_proof.txt` (QA-created), refreshed by the check's CS-3 call; publication destination, writer and validation per section 13; proof returned to QA-110 per section 13.4. Each command below is preceded by CS-ENV and run from the execution clone's root.

### 12.1 CHECK 1 — `d0-discovery`: D0 discovery

* **Surface / D-goal mapping:** D0. Specification §9 (Discovery deliverable of the Live QA stage), §4 items 3 to 5 (precondition), AC-03 (governed current caller set), AC-04 (tested-source identity). Step class: evidence capture.
* **Rails and pins:** `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `LC_ALL=C LANG=C TZ=UTC`; no rails change.
* **PF anchors:** PF06-Canon-Change-Process-Guide §0.4.1.1; PF19-Canon-Glow-QA-Guide §3.4.2, §3.4.8 "Entrypoint existence preflight", §9.2.13 "D0 discovery gate (non-token)"; PF27-Canon-Plan-Templates "Dependency posture".
* **What it proves that bound CI and PR evidence do not:** CI produces no Discovery artifact, does not evaluate reach, and never records the QA execution source. This check records, as governed evidence at the exact source QA tests, the execution source, rails, dependency and harness readiness, collection of all 43 selected tests, the `.gitignore` posture of the QA evidence paths and the caller set, and blocks the run when the QA Audit's facts do not hold there.

**Intent.** Before any behavior check, establish that the run uses a clean tracked tree, closed rails, CI's dependencies, a working harness, the planned 43 tests, committable evidence paths and the caller set the open-rails determination rests on (QA Audit L-31).

**Discovery step.** This check is the discovery step. It records each resolved locus verbatim in its sidecars before any later check relies on it.

**Executor commands (CS-ENV prefix; repository root).**

1. Preflight: `sha256sum /tmp/hde-epic041-qa/d0-discovery.sh` prints `00092b587aa0c12a32dd0b8c5053fe0de4656e27876c8c58c3dcd2a959be476a`.
2. Run and record: `python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))" d0-discovery "D0 discovery" TOOLING_BLOCKED "HDE-EPIC041 QA Plan v1.0 script SC-D0 as written; run and recorded by snippet CS-2" audit/qa/hde-epic041/checks/d0-discovery/d0-env-rails.txt,audit/qa/hde-epic041/checks/d0-discovery/d0-entrypoint-preflight.txt,audit/qa/hde-epic041/checks/d0-discovery/d0-gitignore-audit-qa.txt,audit/qa/hde-epic041/checks/d0-discovery/d0-caller-set.txt /tmp/hde-epic041-qa/d0-discovery.sh`
3. Publish: `python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/d0-discovery/primary.log audit/qa/hde-epic041/checks/d0-discovery/d0-env-rails.txt audit/qa/hde-epic041/checks/d0-discovery/d0-entrypoint-preflight.txt audit/qa/hde-epic041/checks/d0-discovery/d0-gitignore-audit-qa.txt audit/qa/hde-epic041/checks/d0-discovery/d0-caller-set.txt audit/qa/hde-epic041/qa_step_logs_manifest.json`

**Dependency posture.**

* Dependencies required: EC-1 to EC-5; the virtual environment with CI's install; `tools/qa/qa_harness.py`; `git`, `bash`.
* Preflight commands: SC-D0 lines 11 to 13 (`python -m pytest --version` in line 11; `ls -l` of the 19 loci, the harness registration and `--collect-only` in line 12; the collection count in line 13).
* Helper and check registration preflight: `HarnessConfig('HDE-EPIC041')` and `validate_check_id` for all seven planned ids (SC-D0 line 12), captured in `d0-entrypoint-preflight.txt`; the `sha256sum` match of each script file before it runs.
* Registration failure posture: a missing entrypoint, failed registration or collection count other than 43 is `TOOLING_BLOCKED`. A missing tracked entrypoint is an implementation-readiness gap routed through the normal PR path, not Moon Loop.
* Non-QA-root refresh dependency: none for this check's PASS.
* Activation or installation remediation: rerun EC-2's install from the execution clone's root, then the bounded rerun (section 16.2).
* Per-step enforcement: this is the bootstrap step; later checks re-check readiness locally.
* Dependency evidence: `d0-env-rails.txt` and `d0-entrypoint-preflight.txt`.

**Expected result.**

* PASS if SC-D0 exits 0, which requires all of: `git diff --quiet HEAD` succeeds; `python -m pytest --version` succeeds; all 19 loci exist; the harness accepts `HDE-EPIC041` and the seven check ids; collection ends `43 tests collected`; `git check-ignore -v --no-index` exits 1 for the six listed evidence paths; the caller set equals QA Audit L-31 exactly. Supplementary and non-gating: QA root and doc-delta presence before the check, untracked files, the count of `EPIC041_QA_PRIMARY_ARTIFACTS` lines (0 until IDX-01), and the writer `--check` baseline.
* FAIL_BEHAVIOR: not applicable; D0 decides no product behavior.
* FAIL_TOOLING if CS-2 or `record_check` raises, or SC-D0 exits with a code other than 0, 1 or 3.
* TOOLING_BLOCKED if SC-D0 exits 1 or 3; `status_reason` lists every failing precondition. A caller-set difference is a plan-validity block that returns the open-rails determination to Kronos (section 3); it is not a behavior result. Every later check is then NOT RUN.

**Primary evidence artifact.** `audit/qa/hde-epic041/checks/d0-discovery/primary.log` (QA-created): header with the exact SC-D0 text as `command`, plus the transcript of source identity, preconditions and supplementary captures. The manifest `audit/qa/hde-epic041/qa_step_logs_manifest.json` and `audit/qa/hde-epic041/qa_step_logs_manifest.json.path_proof.txt` (Canon-defined; QA-created) record the check's entry.

**Deliverables (QA-created unless marked).**

* `audit/qa/hde-epic041/checks/d0-discovery/primary.log`, written by CS-2.
* `audit/qa/hde-epic041/checks/d0-discovery/d0-env-rails.txt`, written by SC-D0 line 11: environment names (no values), the six rail and pin values, Python, pip and pytest versions and `pip list --format=freeze`. Why: the D0 gate requires a named rails and dependency capture. Predicate: present, non-empty, names only.
* `audit/qa/hde-epic041/checks/d0-discovery/d0-entrypoint-preflight.txt`, written by SC-D0 line 12: `ls -l` of the loci, the harness registration line and the collection output. Why: entrypoint and harness health. Predicate: last line `43 tests collected` followed by the timing.
* `audit/qa/hde-epic041/checks/d0-discovery/d0-gitignore-audit-qa.txt`, written by SC-D0 line 14. Why: the D0 gate requires the `.gitignore` posture of the QA root. Predicate: contains `check_ignore_exit_code: 1`.
* `audit/qa/hde-epic041/checks/d0-discovery/d0-caller-set.txt`, written by SC-D0 line 18: expected and observed caller sets. Why: governed current caller set and the open-rails precondition. Predicate: both lists identical.
* `.path_proof.txt` of each of the five files above, and the manifest `audit/qa/hde-epic041/qa_step_logs_manifest.json` with `audit/qa/hde-epic041/qa_step_logs_manifest.json.path_proof.txt` (Canon-defined grammar), all written by step 3.

**Publication and indexing.** Outputs: the six files above with proofs. Registration keys: `audit.qa.hde_epic041.checks.d0_discovery.primary.log`, `audit.qa.hde_epic041.checks.d0_discovery.d0_env_rails.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_entrypoint_preflight.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_gitignore_audit_qa.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_caller_set.txt`, `epic041.qa_step_logs_manifest`. Writer: `tools/evidence/update_evidence_index.py` through IDX-RUN once IDX-01 lists them (section 13). Validation and proof returned: sections 13.2 and 13.4.

**Tokens.** `intended_tokens: []`; `claimed_tokens: []`.

### 12.2 CHECK 2 — `step-0b-doc-delta-capture`: Step-0B doc delta capture

* **Surface / D-goal mapping:** D5. Specification §10 doc-delta surfaces; QR-05; HDE Build Notes' WU-PR-01 and WU-PR-02 records (DELTA-001, -002) and QA-10 triage record (DELTA-003 candidate). Step class: evidence capture.
* **Rails and pins:** `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `LC_ALL=C LANG=C TZ=UTC`; no rails change.
* **PF anchors:** PF27-Canon-Plan-Templates "Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)"; PF06-Canon-Change-Process-Guide §3.5.2.8 "Post-QA documentation drainage ordering (normative)".
* **What it proves that bound CI and PR evidence do not:** no CI or PR record produces the Step-0B artifact or the Specification §10 surfaces. This check generates them mechanically from the canon text present at the execution source.

**Intent.** Record, by commands, the known canon-versus-repository mismatches as CAVEATS with stable ids (BLOCKERS: none at this point, because D0 passed), on the two-surface pair, byte-identical, without overwriting any existing surface.

**Discovery step.** Canon files are resolved at run time by versionless pattern (QA Audit L-29), refusing a non-unique match, with the text keys of L-30.

**Executor commands (CS-ENV prefix; repository root).**

1. Preflight: `sha256sum /tmp/hde-epic041-qa/step-0b-doc-delta-capture.sh` prints `ceffcbcd2c20c916af3ba58a6e3cf345ec521c685a54894f821b3dd4533c8003`.
2. Run and record: `python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))" step-0b-doc-delta-capture "Step-0B doc delta capture" FAIL_TOOLING "HDE-EPIC041 QA Plan v1.0 script SC-0B as written; run and recorded by snippet CS-2" audit/docdeltas/hde-epic041_doc_deltas.md,audit/qa/hde-epic041/00_meta/doc_deltas.md /tmp/hde-epic041-qa/step-0b-doc-delta-capture.sh`
3. Publish: `python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/step-0b-doc-delta-capture/primary.log audit/docdeltas/hde-epic041_doc_deltas.md audit/qa/hde-epic041/00_meta/doc_deltas.md audit/qa/hde-epic041/qa_step_logs_manifest.json`

**Dependency posture.** Dependencies: `git`, `grep`, `cmp`, `python`; the manifest from check 1. Step-local readiness: SC-0B line 2 (tools on PATH) and line 6 (D0 recorded `PASS`). Registration: the check id was preflighted by D0. Registration failure, missing tool or missing D0 `PASS`: `TOOLING_BLOCKED`. Non-QA-root refresh dependency: none for PASS. Remediation: environment repair, then the bounded rerun only if SC-0B wrote no surface (otherwise the surfaces are preserved and the run escalates). Dependency evidence: the primary log.

**Expected result.**

* PASS if SC-0B exits 0: neither surface existed before; D0 is `PASS`; each canon pattern resolved to one file; both surfaces were written; `cmp` finds them identical; neither names `docs/ephemeral` or `docs/pfcanon`; at least one `- DELTA-00` item is listed. Each item reads "CAVEAT; drives decision: No" when its canon text is still present, or "resolved at this source" when it is gone.
* FAIL_BEHAVIOR: not applicable.
* FAIL_TOOLING if SC-0B exits 1 (a generated-byte predicate fails: pair differs, a forbidden path string, no item) or exits other than 0, 1 or 3, or recording raises.
* TOOLING_BLOCKED if SC-0B exits 3: a surface already exists (preserved unchanged), D0 is not `PASS`, a tool is missing, or a canon pattern does not resolve to exactly one file.

**Primary evidence artifact.** `audit/qa/hde-epic041/checks/step-0b-doc-delta-capture/primary.log` (QA-created), whose body holds the written doc-delta text. The manifest and its proof record the check's entry.

**Deliverables (QA-created).**

* `audit/docdeltas/hde-epic041_doc_deltas.md` (draft and staging surface; Canon-defined name pattern) and `audit/qa/hde-epic041/00_meta/doc_deltas.md` (authoritative epic-scoped record), written by SC-0B lines 15 to 16. Why: PF27 Step-0B and Specification §10. Predicates: identical bytes; sections `## BLOCKERS` (`none`) and `## CAVEATS`; items DELTA-001 to DELTA-003; no `docs/ephemeral` or `docs/pfcanon` string; never `Doc Deltas: None` together with items. Later DRIFT items may be appended only by CS-5.
* Their `.path_proof.txt` files and the refreshed manifest proof, written by step 3.

**Publication and indexing.** Outputs: the primary and the pair, with proofs. Registration keys: `audit.qa.hde_epic041.checks.step_0b_doc_delta_capture.primary.log`, `epic041.doc_deltas`, `audit.qa.hde_epic041.00_meta.doc_deltas.md`. Writer, validation and proof returned: section 13.

**Tokens.** `intended_tokens: []`; `claimed_tokens: []`.

### 12.3 CHECK 3 — `ac01-orchestration-entry`: Adapter-owned chart entry functional proof

* **Surface / D-goal mapping:** D1, D4. R-01 / AC-01; R-04 / AC-04; AC-05 (the entry writes no file). Step class: 2 (internal functional and determinism).
* **Rails and pins:** `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `LC_ALL=C LANG=C TZ=UTC`; no rails change.
* **PF anchors:** PF06-Canon-Change-Process-Guide §3.5.2.8 "Functional proof requirement"; PF09.3-Canon-HDE-Build-Checklist-Separation HDE-SEPA006.1 and HDE-SEPA006.3; PF19-Canon-Glow-QA-Guide §3.4.8.
* **What it proves that bound CI and PR evidence do not:** BE-01 and BE-02 show these 20 tests passed at the PR heads in hosted logs. CI results are not governed evidence (PF06 §3.5.2.8: "CI tests MUST NOT be treated as a source of governed evidence"), never ran at the QA execution source, and record no QA actor or limitations. This check is the functional proof step PF06 requires for the changed adapter-to-engine seam: it exercises the runtime path through the harness and produces the governed, indexed receipt at the execution source.

**Intent.** Prove at runtime that the Adapter-owned entry owns the operational concerns and behaves as delivered under closed rails.

**What is exercised (titles only).** The positional and keyword call forms returning the fixture chart; a fresh dictionary per call; each invalid field raising the typed error with one error log line; absent and invalid `tz`; a fourth positional argument ignored; every other argument shape raising `TypeError("Invalid arguments to load_chart")` with one error line (the D-1 change); the `safe_mode` field for `SAFE_MODE` `1`, `0` and unset; correlation id passed through or synthesized as `CID-` plus 16 hex digits; a keys-only log line with no birth input once `ts` is removed; a raising sink not breaking the call; the default sink being the module logger and writing no file; validation independent of the working directory; no socket attempt.

**Discovery step.** Not needed: every selector is Audit-proven (QA Audit section 5) and was collected by D0.

**Executor commands (CS-ENV prefix; repository root).**

1. Run and record: `python -c "import dataclasses, sys; from tools.qa.qa_harness import HarnessConfig, record_check, run_pytest_check; c = HarnessConfig('HDE-EPIC041'); cid, name, extra = sys.argv[1:4]; r = run_pytest_check(c, cid, sys.argv[4:], check_name=name); r = dataclasses.replace(r, evidence_artifacts=tuple(x for x in extra.split(',') if x)) if extra else r; record_check(c, r); print('status=' + r.status.value, 'exit_code=' + str(r.exit_code))" ac01-orchestration-entry "Adapter-owned chart entry functional proof" "" tests/adapter/test_chart_orchestration.py -p no:cacheprovider`
2. Publish: `python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json`

**Dependency posture.** Dependencies: the virtual environment with CI's install; `tools/qa/qa_harness.py`; the selected test files. Step-local readiness: `run_pytest_check` runs `python -m pytest --version` before the tests and records both commands; it refuses an unsupported option or a missing selector file before running anything. Registration: the check id and the selectors were preflighted by D0. Failure of readiness or registration: `TOOLING_BLOCKED`. Non-QA-root refresh dependency: none for PASS. Remediation: environment repair, then the bounded rerun. Dependency evidence: the readiness command in the primary header's `command` field; a failed readiness is recorded as `TOOLING_BLOCKED` with its reason.

**Expected result** (the harness maps the pytest exit code; QA Audit section 10.5).

* PASS if the readiness command and the test command both exit 0; the body's summary is expected to read `20 passed`. A different count with exit 0 cannot arise from an unchanged source after D0's collection; QA-110 treats it as an evidence-identity defect, not PASS.
* FAIL_BEHAVIOR if pytest exits 1: a delivered test's predicate failed on the execution source.
* FAIL_TOOLING if pytest exits 2, 3, 4 or a negative code, or a launch raises.
* TOOLING_BLOCKED if readiness fails, a selector file is missing, an option is unsupported, or pytest exits 5 (no tests collected).

**Primary evidence artifact.** `audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log` (QA-created): header (exact readiness and test argv, `captured_env`, status, exit code) and the pytest transcript (platform, rootdir, configfile, per-file progress, summary). The manifest and its proof record the check's entry.

**Deliverables (QA-created).** `audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log` and `audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log.path_proof.txt`; the refreshed manifest and its proof. No other file.

**Publication and indexing.** Registration key: `audit.qa.hde_epic041.checks.ac01_orchestration_entry.primary.log`. Writer, validation and proof returned: section 13.

**Tokens.** `intended_tokens: []`; `claimed_tokens: []`.

### 12.4 CHECK 4 — `ac02-pure-module`: Pure Engine chart module purity and interface

* **Surface / D-goal mapping:** D2, D4. R-02 / AC-02; R-04 / AC-04. Step class: 2 (internal functional and determinism).
* **Rails and pins:** `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `LC_ALL=C LANG=C TZ=UTC`; no rails change.
* **PF anchors:** PF09.3-Canon-HDE-Build-Checklist-Separation HDE-SEPA006.1 and HDE-SEPA006.3; PF19-Canon-Glow-QA-Guide §3.4.8.
* **What it proves that bound CI and PR evidence do not:** BE-01 and BE-02 cover these 13 tests at the PR heads only, as non-governed hosted logs. This check records, as governed and indexed evidence at the execution source, the explicit interface and side-effect account (AC-02) including purity at import in a fresh interpreter, with its negative self-tests.

**Intent.** Prove that the Engine chart module takes explicit inputs and returns data with no listed side effect, including at import.

**What is exercised (titles only).** The AST deny-list over `engine/charts/pure.py` and its planted-violation self-test; a cold import loading no operational module, then import and calls with every time, randomness, environment, filesystem, logging, socket and subprocess entry point patched to fail, and the harness self-tests that a planted side effect and a planted operational import are caught; valid inputs returning parsed values; each invalid field raising `ChartInputError` with its field; the checks running in the removed loader's order; `normalize_chart` returning a copy of the fixture chart.

**Discovery step.** Not needed: every selector is Audit-proven (QA Audit section 5) and was collected by D0.

**Executor commands (CS-ENV prefix; repository root).**

1. Run and record: `python -c "import dataclasses, sys; from tools.qa.qa_harness import HarnessConfig, record_check, run_pytest_check; c = HarnessConfig('HDE-EPIC041'); cid, name, extra = sys.argv[1:4]; r = run_pytest_check(c, cid, sys.argv[4:], check_name=name); r = dataclasses.replace(r, evidence_artifacts=tuple(x for x in extra.split(',') if x)) if extra else r; record_check(c, r); print('status=' + r.status.value, 'exit_code=' + str(r.exit_code))" ac02-pure-module "Pure Engine chart module purity and interface" "" tests/charts/test_chart_pure_purity.py tests/charts/test_chart_pure_interface.py -p no:cacheprovider`
2. Publish: `python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/ac02-pure-module/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json`

**Dependency posture.** Dependencies: the virtual environment with CI's install; `tools/qa/qa_harness.py`; the selected test files. Step-local readiness: `run_pytest_check` runs `python -m pytest --version` before the tests and records both commands; it refuses an unsupported option or a missing selector file before running anything. Registration: the check id and the selectors were preflighted by D0. Failure of readiness or registration: `TOOLING_BLOCKED`. Non-QA-root refresh dependency: none for PASS. Remediation: environment repair, then the bounded rerun. Dependency evidence: the readiness command in the primary header's `command` field; a failed readiness is recorded as `TOOLING_BLOCKED` with its reason.

**Expected result** (the harness maps the pytest exit code; QA Audit section 10.5).

* PASS if the readiness command and the test command both exit 0; the body's summary is expected to read `13 passed`. A different count with exit 0 cannot arise from an unchanged source after D0's collection; QA-110 treats it as an evidence-identity defect, not PASS.
* FAIL_BEHAVIOR if pytest exits 1: a delivered test's predicate failed on the execution source.
* FAIL_TOOLING if pytest exits 2, 3, 4 or a negative code, or a launch raises.
* TOOLING_BLOCKED if readiness fails, a selector file is missing, an option is unsupported, or pytest exits 5 (no tests collected).

**Primary evidence artifact.** `audit/qa/hde-epic041/checks/ac02-pure-module/primary.log` (QA-created): header (exact readiness and test argv, `captured_env`, status, exit code) and the pytest transcript (platform, rootdir, configfile, per-file progress, summary). The manifest and its proof record the check's entry.

**Deliverables (QA-created).** `audit/qa/hde-epic041/checks/ac02-pure-module/primary.log` and `audit/qa/hde-epic041/checks/ac02-pure-module/primary.log.path_proof.txt`; the refreshed manifest and its proof. No other file.

**Publication and indexing.** Registration key: `audit.qa.hde_epic041.checks.ac02_pure_module.primary.log`. Writer, validation and proof returned: section 13.

**Tokens.** `intended_tokens: []`; `claimed_tokens: []`.

### 12.5 CHECK 5 — `ac03-caller-migration`: Caller migration, retirement guard and retained coverage

* **Surface / D-goal mapping:** D3, D4. R-03 / AC-03; R-01 / AC-01 (a supported path for each supported use); R-04 / AC-04; AC-05 (retained coverage; the generator writes nothing); QR-02. Step class: 2 (internal functional and determinism).
* **Rails and pins:** `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `LC_ALL=C LANG=C TZ=UTC`; no rails change.
* **PF anchors:** PF09.3-Canon-HDE-Build-Checklist-Separation HDE-SEPA006.2 and HDE-SEPA006.3 (retained coverage named in Task HDE-SEPA006 notes); PF19-Canon-Glow-QA-Guide §3.4.8.
* **What it proves that bound CI and PR evidence do not:** BE-02 covers these tests at `8200d1fb` only. CI reruns the guard only when its owner paths change, so no CI run has scanned the tracked tree of the QA execution source; this check does, and records the result as governed evidence. It also records C-1's exit 2 with nothing written under CI's install, which QA-10 could not reproduce (QR-02), and the PF09.3 retained coverage, as governed and indexed evidence.

**Intent.** Prove that the removed module stays absent with no tracked importer, that every migrated caller works through the new interfaces, and that the retained coverage still passes.

**What is exercised (titles only).** The guard scanning tracked Python files (with the three live callers among those scanned) and finding no importer or `_call_legacy` reference; `engine/charts/loader.py` absent and untracked; the guard's checker flagging every import form and ignoring non-imports; C-1 (`scripts/make_compat_determinism_artifacts.py`) run from a temporary working directory exiting 2 with stderr `compat_public not implemented` and writing nothing; C-2 requiring `tz` and returning the normalized chart, and raising the typed error without it; C-3 emitting a keys-only log line; the vendor provider refusing to construct under `SAFE_MODE=1` and the vendor HTTP provider refusing a call under `SAFE_MODE=1`.

**Discovery step.** Not needed: every selector is Audit-proven (QA Audit section 5) and was collected by D0.

**Executor commands (CS-ENV prefix; repository root).**

1. Run and record: `python -c "import dataclasses, sys; from tools.qa.qa_harness import HarnessConfig, record_check, run_pytest_check; c = HarnessConfig('HDE-EPIC041'); cid, name, extra = sys.argv[1:4]; r = run_pytest_check(c, cid, sys.argv[4:], check_name=name); r = dataclasses.replace(r, evidence_artifacts=tuple(x for x in extra.split(',') if x)) if extra else r; record_check(c, r); print('status=' + r.status.value, 'exit_code=' + str(r.exit_code))" ac03-caller-migration "Caller migration, retirement guard and retained coverage" "" tests/charts/test_chart_loader_import_guard.py tests/scripts/test_make_compat_determinism_artifacts.py tests/loader/test_load_chart_fixture_only.py tests/loader/test_loader_logs_keys_only.py tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on -p no:cacheprovider`
2. Publish: `python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json`

**Dependency posture.** Dependencies: the virtual environment with CI's install; `tools/qa/qa_harness.py`; the selected test files. Step-local readiness: `run_pytest_check` runs `python -m pytest --version` before the tests and records both commands; it refuses an unsupported option or a missing selector file before running anything. Registration: the check id and the selectors were preflighted by D0. Failure of readiness or registration: `TOOLING_BLOCKED`. Non-QA-root refresh dependency: none for PASS. Remediation: environment repair, then the bounded rerun. Dependency evidence: the readiness command in the primary header's `command` field; a failed readiness is recorded as `TOOLING_BLOCKED` with its reason.

**Expected result** (the harness maps the pytest exit code; QA Audit section 10.5).

* PASS if the readiness command and the test command both exit 0; the body's summary is expected to read `10 passed`. A different count with exit 0 cannot arise from an unchanged source after D0's collection; QA-110 treats it as an evidence-identity defect, not PASS.
* FAIL_BEHAVIOR if pytest exits 1: a delivered test's predicate failed on the execution source.
* FAIL_TOOLING if pytest exits 2, 3, 4 or a negative code, or a launch raises.
* TOOLING_BLOCKED if readiness fails, a selector file is missing, an option is unsupported, or pytest exits 5 (no tests collected).

**Primary evidence artifact.** `audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log` (QA-created): header (exact readiness and test argv, `captured_env`, status, exit code) and the pytest transcript (platform, rootdir, configfile, per-file progress, summary). The manifest and its proof record the check's entry.

**Deliverables (QA-created).** `audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log` and `audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log.path_proof.txt`; the refreshed manifest and its proof. No other file.

**Publication and indexing.** Registration key: `audit.qa.hde_epic041.checks.ac03_caller_migration.primary.log`. Writer, validation and proof returned: section 13.

**Tokens.** `intended_tokens: []`; `claimed_tokens: []`.

### 12.6 CHECK 6 — `ac05-tracked-files-unchanged`: Tracked files unchanged after the covering runs

* **Surface / D-goal mapping:** D4. AC-05 ("running the covering tests leaves tracked files unchanged"); R-01, R-03, R-04; IR-10. Step class: 2.
* **Rails and pins:** `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `LC_ALL=C LANG=C TZ=UTC`; no rails change.
* **PF anchors:** PF09.3-Canon-HDE-Build-Checklist-Separation HDE-SEPA006.3 ("preservation of governed outputs"); PF19-Canon-Glow-QA-Guide §3.4.9.
* **What it proves that bound CI and PR evidence do not:** CI's clean-tree gate (ci.yml L129 to L130) covered CI's own runs in a detached worktree at the PR heads. This check records, as governed evidence, that the QA runs of checks 3 to 5 in the execution clone left every tracked file unchanged.

**Intent.** Decide the AC-05 tracked-file limb for the QA runs of the covering tests. The predicate is the Specification's behavior predicate, not source attribution.

**Discovery step.** Not needed.

**Executor commands (CS-ENV prefix; repository root).**

1. Preflight: `sha256sum /tmp/hde-epic041-qa/ac05-tracked-files-unchanged.sh` prints `139bd41ca5a91eca0557a6ae546ab9918429d138828e9268e99f7c62e74d772d`.
2. Run and record: `python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))" ac05-tracked-files-unchanged "Tracked files unchanged after the covering runs" FAIL_BEHAVIOR "HDE-EPIC041 QA Plan v1.0 script SC-05 as written; run and recorded by snippet CS-2" "" /tmp/hde-epic041-qa/ac05-tracked-files-unchanged.sh`
3. Publish: `python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/ac05-tracked-files-unchanged/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json`

**Dependency posture.** Dependencies: `git`. Step-local readiness: SC-05 line 2. Registration: preflighted by D0. Missing `git` or a `git diff` error: `TOOLING_BLOCKED`. Non-QA-root refresh dependency: none. Dependency evidence: the primary log.

**Expected result.**

* PASS if `git diff --exit-code --stat HEAD`, excluding only `audit/qa/hde-epic041`, `audit/docdeltas/hde-epic041_doc_deltas.md` and its proof, exits 0. The untracked listing outside those paths is supplementary and non-gating, so ordinary working-tree noise cannot decide the result.
* FAIL_BEHAVIOR if that `git diff` exits 1: a tracked file changed after the covering runs. Preserve the tree as found; do not reset it before capture (section 17).
* FAIL_TOOLING if SC-05 exits other than 0, 1 or 3, or recording raises.
* TOOLING_BLOCKED if SC-05 exits 3 (`git` missing or `git diff` failed).

**Primary evidence artifact.** `audit/qa/hde-epic041/checks/ac05-tracked-files-unchanged/primary.log` (QA-created): the tracked diff exit code and the supplementary untracked listing. The manifest and its proof record the check's entry.

**Deliverables (QA-created).** The primary log and its proof; the refreshed manifest and its proof.

**Publication and indexing.** Registration key: `audit.qa.hde_epic041.checks.ac05_tracked_files_unchanged.primary.log`. Writer, validation and proof returned: section 13.

**Tokens.** `intended_tokens: []`; `claimed_tokens: []`.

### 12.7 CHECK 7 — `qa-closeout-deliverables`: QA closeout deliverables integrity

* **Surface / D-goal mapping:** D4. AC-04 (the recorded evidence is complete and coherent); Specification §8; QR-04. Step class: evidence capture.
* **Rails and pins:** `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `LC_ALL=C LANG=C TZ=UTC`; no rails change.
* **PF anchors:** PF19-Canon-Glow-QA-Guide §3.4.3 (manifest and primary-log path proofs), §4.4.3; PF27-Canon-Plan-Templates "Close-out deliverables" and "Step-0B — Doc Delta Capture".
* **What it proves that bound CI and PR evidence do not:** no CI or PR record covers QA-run artifacts. Before landing and indexing, this check verifies that the QA evidence family is complete (the six earlier checks are in the manifest), that every artifact each primary relies on and the manifest carry a valid capture-time path proof, and that the doc-delta pair is identical and names no planning or canon path, so that QA-110 and the writer receive a coherent family.

**Intent.** Verify the integrity of the QA evidence family; decide no product behavior.

**Discovery step.** Not needed; the manifest is the authoritative index (PF12 §8.17), and no subdirectory is enumerated.

**Executor commands (CS-ENV prefix; repository root).**

1. Preflight: `sha256sum /tmp/hde-epic041-qa/qa-closeout-deliverables.sh` prints `d5420d277ab7cb840efc5cb4eb95d64806addb2398f4a8ce0772dc61ead95a45`.
2. If any DRIFT item is owed (section 16.4), append it with CS-5 and refresh both doc-delta proofs with CS-3 first.
3. Run and record: `python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))" qa-closeout-deliverables "QA closeout deliverables integrity" FAIL_TOOLING "HDE-EPIC041 QA Plan v1.0 script SC-CL as written; run and recorded by snippet CS-2" "" /tmp/hde-epic041-qa/qa-closeout-deliverables.sh`
4. Publish: `python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/qa-closeout-deliverables/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json`

**Dependency posture.** Dependencies: `python` with the writer module importable, `cmp`, `grep`; the six earlier checks recorded. Step-local readiness: SC-CL line 2. Registration: preflighted by D0. Missing writer import: `TOOLING_BLOCKED`. Non-QA-root refresh dependency: none for PASS (indexing is section 13 and is not a predicate here). Dependency evidence: the primary log.

**Expected result.**

* PASS if SC-CL exits 0: the manifest holds the six earlier checks (any status); `_refresh_path_proof` in check mode (`check=True`) verifies every artifact listed in the earlier primaries' `evidence_artifacts`, the manifest and both doc-delta surfaces; `cmp` finds the pair identical; neither surface names `docs/ephemeral` or `docs/pfcanon`.
* FAIL_BEHAVIOR: not applicable.
* FAIL_TOOLING if SC-CL exits 1 (a proof is missing or stale, the pair differs, or a forbidden path string is present) or other than 0, 1 or 3, or recording raises. This is an evidence-assembly defect, correctable by Moon Loop within the QA root (section 10).
* TOOLING_BLOCKED if SC-CL exits 3 (a planned check has no manifest entry, or the writer module does not import).

**Primary evidence artifact.** `audit/qa/hde-epic041/checks/qa-closeout-deliverables/primary.log` (QA-created), listing each manifest entry and each verified proof. The manifest and its proof record the check's entry.

**Deliverables (QA-created).** The primary log and its proof; the refreshed manifest and its proof (the final manifest state of the run).

**Publication and indexing.** Registration key: `audit.qa.hde_epic041.checks.qa_closeout_deliverables.primary.log`. This check's own proof and the final manifest proof are verified by IDX-RUN's validators (section 13.2). Writer, validation and proof returned: section 13.

**Tokens.** `intended_tokens: []`; `claimed_tokens: []`.

## 13. Evidence publication, indexing and landing

Publication and indexing are part of every check: each check's CS-3 call publishes its own path proofs at capture time (sections 12.1 to 12.7), the registration set is fixed in section 8.3, and the indexing below is one shared batch action with the explicit per-check mapping of section 13.2.

### 13.1 IDX-01 — writer registration (routed work item; not QA execution)

* **Why.** QA Audit finding QA50-F02 (G-OBS-01): `tools/evidence/update_evidence_index.py` cannot index any HDE-EPIC041 artifact until its source lists them. That is a change to repository tooling outside the QA root, so it is routed remediation, not Moon Loop (Glow QA Guide §3.4.8 "Non-QA-root remediation boundary"), and it maps to PF09.3 HDE-SEPA006.3 ("required indexing through the existing governed writer").
* **Work item type.** PR. No lawful PR implementation author exists (WU-PR-01 to -03 are merged and accepted), so the Product Owner assigns the author and approves the route (PI-02). This Plan invents no PR, Proceed or author.
* **Required content (the registration set of section 8.3, nothing else).** An `EPIC041_QA_PRIMARY_ARTIFACTS` list in `tools/evidence/update_evidence_index.py` with one row per file the executed QA run actually produced (14 unconditional rows, plus any section 8.2 conditional files), each with `artifact_key`, `discovered_physical_path` and `"epic_id": "HDE-EPIC041"`, spliced after `*EPIC040_QA_PRIMARY_ARTIFACTS,`; and an owner test that fails when a listed row is absent from the regenerated Index, as `tests/ops/test_evidence_index.py` does for HDE-EPIC040. The PR author designs the code; this Plan fixes only the rows.
* **Ordering constraint.** A static list cannot merge before its files exist (`--check` reports `STALE`; QA Audit section 10.2). IDX-01 therefore lands with the evidence (route A) or, under route C, as a presence-gated, fail-closed registration merged before the evidence-only QA PR.
* **Completion predicate.** At the landing pull request's reviewed head, the Index holds exactly the registration-set rows for HDE-EPIC041, the read-only validators of section 13.2 exit 0, and the exact-head CI evidence lane passes. Other changes are limited to the writer's expected convergence (sentinels, Mirror self-record, orientation count and their proofs), classified as expected updater convergence. IDX-01's result is not a QA verdict.

### 13.2 IDX-RUN — the batch indexing action

Performed once, after check 7, in the working tree that holds the produced evidence and IDX-01's list (the landing branch under route A; the execution clone under route C):

* **Write.** `python tools/evidence/update_evidence_index.py` (write mode; it refuses unless the pins and closed rails hold).
* **Read-only validation**, each expected to exit 0: `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `ci/checks/check_mirror_schema.sh`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/check_lf_endings.py`. Never run `tools/evidence/orientation_demo.py` without `--check`.
* **Row confirmation.** `python -c "import json; rows = sorted((r['artifact_key'], r['discovered_physical_path']) for r in json.load(open('docs/evidence/INDEX.json')) if r.get('epic_id') == 'HDE-EPIC041'); [print(k, p) for k, p in rows]; print('rows:', len(rows))"` lists exactly the registration-set rows.
* **Per-check mapping** (files to keys as section 8.3): check 1 maps six files (primary, four sidecars, manifest); check 2 maps three (primary and the doc-delta pair); checks 3 to 7 map one primary each. Every row's proof is the capture-time proof written by that check's CS-3 call.
* **Dependency.** IDX-RUN needs IDX-01 present and every listed file present; without IDX-01 it is not run and indexing stays incomplete (section 13.4).

### 13.3 EL-01 — landing route

* **Planned route A.** One pull request from a branch named in the QA branch grammar of PF06 §0.7, `qa/hde-epic041-live-qa-evidence`, carrying: every QA-run artifact with its proof, exactly as produced (not regenerated); the IDX-01 change and its owner test; and IDX-RUN's regenerated `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, `audit/gates/topology/orientation_demo.txt` and their proofs. It keeps evidence and indices in one mutation set (PF06 §3.5.2.8). Because it also carries evidence tooling, which PF06 §0.7 does not list for an evidence-only QA PR, it needs the Product Owner's approval (PI-02; CCR-6); HDE-EPIC040 #559 is the precedent. Its body follows PF06 §4.5 and states the IDX-01 tooling change separately. It merges before any close pull request.
* **Route C, only if the Product Owner declines route A.** IDX-01 lands first as its own PR with a presence-gated, fail-closed registration; then an evidence-only QA PR from `qa/hde-epic041-live-qa-evidence` carries the evidence and IDX-RUN's outputs. A conditional rerun file (section 8.2) that the landed registration does not list needs an IDX-01 amendment through the same route before IDX-RUN.
* **Not planned.** Landing the evidence unindexed and indexing it later (route B) breaks the same-mutation-set parity rule.
* **Persistence.** Until the landing pull request carries them, the produced files stay unchanged in the execution clone; they are never left only in `/tmp`.
* **CI expectation** (QA Audit section 10; local reproduction, not hosted CI): the landing pull request classifies to the `evidence` and `release` lanes, plus `product` and the writer's changed owner tests when IDX-01 is included; no path is unclassified.

### 13.4 Proof returned to QA-110

QA-100 returns, per check: the produced paths and their proofs, the CS-3 output, manifest membership and status; and, for the batch: the IDX-RUN write output, each validator's exit code and output, the row confirmation output, the landing pull request number, reviewed head and exact-head CI run, and every gap with its owner. Missing indexing is incomplete work or a tooling outcome, never a behavioral PASS; QA-110 returns missing publication to the writer's owner without rerunning valid QA solely to index it.

## 14. Bound CI and PR evidence (not re-run)

| Id | Evidence | Binds | Gap the QA checks close |
| :- | :- | :- | :- |
| BE-01 | #791 exact-head CI run 40723983402 (`success`) on `815fd5b2` | R-01, R-02 tests passed at WU-PR-01's head | Governed, indexed receipt at the QA execution source |
| BE-02 | #796 exact-head CI run 40774524113 (`success`) on `8200d1fb`, the delivered code tree | All seven lanes, including the changed-tests lane for WU-PR-02's diff (guard, generator test, migrated callers), passed with a clean tree | As BE-01, plus actor and limitations in the record |
| BE-03 | GitHub diffs of #791, #796, #800 | Compat artifacts, `artifacts/logs/loader_call.jsonl`, `catalog/manifest.json` and `.audit_src/` historical captures unchanged | None needed; not re-run |
| BE-04 | WU-PR-02 lineage review focused run; Reality Audit E-036 equality against the removed loader | Preservation against code that can no longer run | None possible; bound |
| BE-05 | CI owner registration in `ci/checks/classify_ci_changes.py` | Regression selection for future changes | None needed |

## 15. Coverage map and out-of-scope items

| Criterion | Covered by | Notes |
| :- | :- | :- |
| R-01 / AC-01 | `ac01-orchestration-entry`; `ac03-caller-migration` (a supported path for each supported use: C-1 to C-3 through the entry); `d0-discovery` (no other caller; no acquisition, so the resolver clause is vacuous) | Functional proof check |
| R-02 / AC-02 | `ac02-pure-module` | Includes purity at import |
| R-03 / AC-03 | `ac03-caller-migration`; `d0-discovery` (governed caller set at the execution source) | Inventory dispositions: QA Audit sections 3 and 5; historical captures: BE-03 |
| R-04 / AC-04 | All seven checks (commands, configuration, tested source, results, time in the headers); actor and limitations in the QA-100 result and Final QA Report; indexing by IDX-01 and IDX-RUN | |
| AC-05 | `ac05-tracked-files-unchanged`; `ac03-caller-migration` (retained coverage; generator writes nothing); `ac01-orchestration-entry` (entry writes no file); BE-03, BE-04 | |
| Specification §4 items 3 to 5 | QA Audit section 9; `d0-discovery` precondition | |
| Specification §9 | Execution of this Plan, D0 and the summary of section 18 | |
| Specification §10 doc-delta surfaces | `step-0b-doc-delta-capture` | Close pack: CL-05 |

Every in-scope criterion is covered by at least one check, and every check maps to a criterion or an evidence-capture requirement.

**Out of scope, deferred or blocked (not checks):** live vendor or production steps (not required, section 3); the close pack, acceptance map, viability log and drain targets (CL-05; CCR-1, CCR-5); FND-005 to FND-007 and items 9 and 10 (Product Owner); `main` push CI (QR-07); PF09.3 status movement (post-closure, Product Owner); prompt-use repository persistence (GCFPE management). The bounded proof limits IR-01 and IR-02 (QA Audit QA50-F05, -F06) are reported, not checked.

## 16. Order, dependencies, rerun and escalation

### 16.1 Order and stop rules

1. `d0-discovery`. If it is not `PASS`, stop: no other check runs; the run returns `BLOCKED` with D0's receipt.
2. `step-0b-doc-delta-capture` (needs D0 `PASS`).
3. `ac01-orchestration-entry`, then 4. `ac02-pure-module`, then 5. `ac03-caller-migration` (each needs D0 `PASS`; independent of each other; a failure in one does not stop the others).
6. `ac05-tracked-files-unchanged` (after checks 3 to 5, whatever their status).
7. `qa-closeout-deliverables` (after checks 2 to 6 are recorded, whatever their status).
8. IDX-RUN, then EL-01 (section 13), when IDX-01 is available.

### 16.2 Bounded rerun (one per check)

* **Trigger.** An execution or evidence fault in check X under this unchanged Plan: `TOOLING_BLOCKED` or `FAIL_TOOLING` whose cause is outside the product (a missing install, a script transcription error, an interrupted write) and is corrected without changing proof target, scope, rails or predicates. `FAIL_BEHAVIOR` is never rerun; it goes to escalation.
* **Rails.** Unchanged.
* **Procedure.** Run CS-4 for X's directory; write X's remediation note (one line: what changed and why) to `tmp_attempt1_remediation_note.txt` in that directory; rerun X's command unchanged except that the extra-evidence argument lists every `tmp_attempt1_` file (for a CS-2 check, after its normal extra paths); run CS-3 on the new primary, every `tmp_attempt1_` file and the manifest; append a DRIFT item with CS-5 and refresh the pair's proofs. The rerun stays in X's directory and evidence family, and the first attempt stays preserved and registered (section 8.2).
* **Worked example (check 4, `ac02-pure-module`; each command behind CS-ENV where it runs Python).**
  1. `d=audit/qa/hde-epic041/checks/ac02-pure-module` and then CS-4.
  2. `printf '%s\n' 'attempt 1 was TOOLING_BLOCKED because the CI requirements were not installed; installed them from the execution clone root; nothing else changed' > audit/qa/hde-epic041/checks/ac02-pure-module/tmp_attempt1_remediation_note.txt`
  3. CS-1 with arguments `ac02-pure-module`, `Pure Engine chart module purity and interface`, `audit/qa/hde-epic041/checks/ac02-pure-module/tmp_attempt1_primary.log,audit/qa/hde-epic041/checks/ac02-pure-module/tmp_attempt1_remediation_note.txt`, `tests/charts/test_chart_pure_purity.py`, `tests/charts/test_chart_pure_interface.py`, `-p`, `no:cacheprovider`.
  4. CS-3 with files `audit/qa/hde-epic041/checks/ac02-pure-module/primary.log`, `audit/qa/hde-epic041/checks/ac02-pure-module/tmp_attempt1_primary.log`, `audit/qa/hde-epic041/checks/ac02-pure-module/tmp_attempt1_remediation_note.txt`, `audit/qa/hde-epic041/qa_step_logs_manifest.json`.
  5. CS-5 (its example item fits this case), then CS-3 with files `audit/docdeltas/hde-epic041_doc_deltas.md` and `audit/qa/hde-epic041/00_meta/doc_deltas.md`.
* **Limit.** One rerun. A second failure, any behavior failure, or a needed Plan, scope or rails change goes to escalation. Attempt lineage is never reset by renaming a check.

### 16.3 Escalation and returns

* `FAIL_BEHAVIOR`, a second failure, or an invalid Plan: QA-110 evidence review, then Kronos's ESC-10 report and Thoth's ESC-30 (HDE Governance §9.1.5).
* A D0 caller-set mismatch: Kronos re-determines section 3 (possible re-attachment of items 3 and 4) through QA-80.
* A finding that a readiness basis is invalid returns to QA-10 (Isis). Accepted repair returns to its originating owner.

### 16.4 Normalization and drift record

An executor who normalizes a command or script records the exact command run (the primary log does so), the reason in the command provenance argument of CS-2 (for example `HDE-EPIC041 QA Plan v1.0 script SC-05 normalized: quoting of line 3 corrected after transcription; run and recorded by snippet CS-2`) or in the QA-100 result for a CS-1 check, and a DRIFT item through CS-5. More than three plan-to-evidence structural mismatches in the run pause execution for systems RCA (Plan Templates QoS stop rule).

## 17. Cleanup and recovery

* No check writes outside `audit/qa/hde-epic041/`, `audit/docdeltas/hde-epic041_doc_deltas.md` and their proofs; `.pytest_cache` is disabled; `__pycache__` and `glow_hdengine.egg-info/` are git-ignored.
* A tracked-file change found by check 6 is preserved as AC-05 evidence; it is not reset before capture.
* `record_check` publishes atomically with rollback; after an interruption, read the manifest and resume from the first planned check without an entry. Cancellation is incomplete work, not a failure, and consumes no rerun. An uncertain write is inspected before any retry.
* `/tmp/hde-epic041-qa/` may be deleted after the landing pull request carries the evidence. Evidence files are never deleted or regenerated before landing.

## 18. Close-out deliverables

* **Discovery artifact.** `d0-discovery`'s primary log and its four sidecars, governed and indexed (PF06 §0.4.1.1; Glow QA Guide §9.2.13).
* **QA RCA & Doc Delta summary.** Location: a section of the epic close report `audit/EPIC-041_close_report.md`, rendered by the close-pack writer at CL-05 from summary lines that the Final QA Report (QA-120) records as text (HDE Build Notes: close pack only at close; CCR-5 decides the ordering). No QA step writes `audit/EPIC-041_QA_RCA.md`. Content, per PF06 §0.4.1.2 and Plan Templates "What QA RCA & Doc Delta summary means": what ran and what each outcome means; evidence pointers under `audit/qa/hde-epic041/`; Coverage vs QA Plan accounting in plan order with step ids 1 to 7, each Fully, Partially or Not evidenced, with every accepted deviation (rerun, normalization, Moon Loop) surfaced separately; doc deltas DELTA-001 to -003 mapped to PF titles, with drainage after all QA tasks and never a blocker; deferrals as deferrals; the source-of-truth posture; whether same-run runtime proof exists for D1 to D3; an explicit closeout-readiness recommendation; and repo-supported completion, canon-drain completion and formal close-pack completion kept as separate states.
* **Facts CL-05 needs, recorded as text by QA-120** (the close-pack writer reads the source, never this Plan): planned checks in order with their criteria: `d0-discovery` []; `step-0b-doc-delta-capture` []; `ac01-orchestration-entry` [R-01, R-04, AC-01, AC-04, AC-05]; `ac02-pure-module` [R-02, R-04, AC-02, AC-04]; `ac03-caller-migration` [R-01, R-03, R-04, AC-01, AC-03, AC-04, AC-05]; `ac05-tracked-files-unchanged` [R-01, R-03, R-04, AC-05]; `qa-closeout-deliverables` [R-04, AC-04].
* **Acceptance map.** This Plan produces no acceptance-map viability check; CL-05 owns the acceptance map (CCR-1, TI-07; QA Audit QA50-F10).

## 19. Final-report criteria (QA-110 and QA-120)

A QA PASS for HDE-EPIC041 is supportable only when all of these hold; otherwise the Final QA Report states the failed condition and its owner:

1. Checks 1 to 7 are recorded `PASS` in the manifest (a rerun `PASS` counts only with attempt 1 preserved and registered and the DRIFT item present), each primary carries the expected header and `exit_code` 0, and checks 3 to 5 report 20, 13 and 10 passed.
2. Every QA-run artifact is on `main` through EL-01, with its capture-time proof, and indexed: the row confirmation lists exactly the registration set, the six validators exit 0 at the landing pull request's reviewed head, and its exact-head CI passed.
3. The execution source recorded by D0, the landing pull request's base, reviewed head and merge commit, and review-time HEAD are recorded as distinct facts.
4. The open-rails determination still holds (D0 caller set equal), and no live step ran.
5. The doc-delta pair is byte-identical on `main` and lists DELTA-001 to -003 and every DRIFT item.
6. Limitations IR-01 and IR-02 and the bound evidence BE-01 to BE-05 are stated, with the TI-01 to TI-07 states of the readiness record.

A `FAIL_BEHAVIOR`, an unresolved `FAIL_TOOLING` or `TOOLING_BLOCKED`, missing evidence or missing indexing prevents a PASS; documentation drainage never does.

## 20. PF09 routing and later-drain statement

| Work item ID | PF09 disposition | Phased PF09 document | Task ID | Subtask ID | Exact source heading | Contribution | Status nonclaim |
| :- | :- | :- | :- | :- | :- | :- | :- |
| QA-CHK (checks 1 to 7) | in the current epic with exact phased PF09 task or subtask mapping | PF09.3-Canon-HDE-Build-Checklist-Separation | HDE-SEPA006 | HDE-SEPA006.3 | Subtask HDE-SEPA006.3 — Boundary and behavior verification | Independent verification and governed evidence of .1 and .2 | Moves no PF09 status |
| IDX-01 and IDX-RUN | in the current epic with exact phased PF09 task or subtask mapping | PF09.3-Canon-HDE-Build-Checklist-Separation | HDE-SEPA006 | HDE-SEPA006.3 | Subtask HDE-SEPA006.3 — Boundary and behavior verification | "required indexing through the existing governed writer" | Moves no PF09 status |
| EL-01 | in the current epic with exact phased PF09 task or subtask mapping | PF09.3-Canon-HDE-Build-Checklist-Separation | HDE-SEPA006 | HDE-SEPA006.3 | Subtask HDE-SEPA006.3 — Boundary and behavior verification | Persists the governed evidence | Moves no PF09 status |
| DD-DRAIN (DELTA-001 to -003) | documentation/status drainage only | N/A | N/A | None exists | N/A | Canon text drain after all QA tasks | Not a gate |
| CCR-6 canon reconciliation | documentation/status drainage only | N/A | N/A | None exists | N/A | Possible canon change to PF06 §0.7 and §3.5.2.8 | Not a gate |

**Later-drain PF-canon update statement (non-mandatory; Product Owner-owned).** After all QA tasks complete, and supported by checks 1 to 7 and the Step-0B record: HDE Architecture §1.1 "Non-BodyGraph chart loader classification" and HDE Mechanics Guide §1.1 "BodyGraph and loader seam posture" may replace the text that calls `engine/charts/loader.py` current with the delivered boundary (DELTA-001, -002); HDE State of the Repository §2.2 may record the delivered correction or retire the item (DELTA-003, candidate); PF09.3 Task HDE-SEPA006 and Subtasks .1 to .3 may move only through the authorized post-closure update; Change Process Guide §0.7 "QA branches posture" and §3.5.2.8 "Live QA evidence landing" may state how QA-root artifacts and their writer registration land (CCR-6). None of these is a deliverable, gate or condition of this Plan.

## 21. CANON_CONFLICT_REGISTER

| ID | Classification | Sources and clauses | Conflict | Affected | Alternatives and recommended disposition | Interim treatment and risk | Drainage target and owner | Status | Reviewer, reviewed artifact, decision time and rationale; history |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION | Plan Templates Preflight B against HDE Governance §2.0.19 and HDE Schemas and Artifacts "legacy token compatibility shape" | Is an acceptance map required for tokenless work? | Specification §10; TI-07 | No operative conflict; listed with no token roster (Ruling R-A) | Close-pack matter for CL-05 | Product Owner (possible canon change) | APPROVED | Thoth, CF-E-30 review v1.1 of Specification v1.1, 2026-10-28; confirmed by Isis, IA-30 review v1.1; carried unchanged |
| CCR-2 | CANON_RECONCILIATION | HDE Governance §9.7.7 against Plan Templates §2 | Business Case content lists differ | Specification §2 | Specification v1.1 satisfies both | None | None needed | APPROVED | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-3 | CANON_RECONCILIATION | HDE Build Notes (S19 vendor route selection, production vendor override) against the Specification's "adjacent" reading | Possible reach into the orchestration path | TI-02 | Conditional: governs only if the entry performs resolver-selected vendor acquisition | Not triggered (section 3) | Implementation Audit determined applicability | APPROVED as conditional | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-4 | CANON_RECONCILIATION | PF09.3 Task HDE-SEPA006 notes against the current HDE Build Notes | Cited loader record no longer in PF10 | Specification §5 | No conflict; PF09.3 states the defect in full | None | None | APPROVED | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-5 | CANON_RECONCILIATION | HDE Build Notes (close-pack writer only at close, first bullet) against Change Process Guide §3.5.1 "Close-mutation-set stage", Glow QA Guide §3.1.3 and Plan Templates §3B "Entries and exit (normative)" | The Build Notes rule puts the closure decision before the close-pack write; the three permanent documents put the close mutation set before the closure decision | Specification §10, §6 D5; Plan v1.1 DL-04; CL-05 | (A) the Build Notes rule stands; (B) a correcting addendum restores the CL-05 entries and exit; recommended: an explicit Product Owner ruling before CL-05 | The Build Notes rule governs as written; QA-50 and QA execution unaffected (no QA step writes a close pack) | HDE Build Notes under (B), or the three permanent documents under (A); Product Owner | PROPOSED | Not yet reviewed; proposed by Isis, QA-10 triage v1.0 (full entry and history in its §6); recorded in HDE Build Notes; carried unchanged |
| CCR-6 | CANON_RECONCILIATION | Change Process Guide §0.7 "QA branches posture" ("Allowed changes are limited to governed artifacts" of a listed set; no tooling) against Change Process Guide §3.5.2.8 "Live QA evidence landing" (QA step artifacts under the Epic QA root may land in an evidence-only QA PR with the Index and Mirror in the same mutation set), Glow QA Guide §3.4.3 and §3.4.8 (non-QA-root remediation is a routed work item), and PF09.3 HDE-SEPA006.3 (indexing through the existing writer) | §0.7's list names neither Epic QA-root artifacts nor the doc-delta pair, and no landing route covers evidence plus the writer registration it needs; the writer cannot index a static list before its files exist | QR-04; G-OBS-01; Specification §8, §6 D4; this Plan section 13 | (A) route A under an explicit Product Owner decision (HDE-EPIC040 D-3, where the same gap was logged as CC-3); (B) route C, a presence-gated writer registration first, then an evidence-only QA PR. Recommended: (A) for HDE-EPIC041, decided by the Product Owner before EL-01, with a later canon clarification of §0.7 | Route A pending PI-02; risk: evidence unindexed if neither is chosen (RK-QA-01) | Change Process Guide §0.7 and §3.5.2.8; Product Owner | PROPOSED | Not yet reviewed (Isis reviews this Plan's route at QA-70; the Product Owner decides the route and any canon change); proposed by Kronos, QA-50 QA Audit v1.0 finding QA50-F03 and this Plan v1.0, 2026-10-29; no prior history |

A proposal here is not approval. Decided entries are preserved; unreviewed fields stay unreviewed.

## 22. TypeSafe reading and surface advice for QA-70

* **Method.** The installed TypeSafe scoring skill, request v8.2; its script was run once, before this Plan was saved, with session kind `review` and label "HDE-EPIC041 QA-70 QA Plan review". No Notion row was written (QA-50: "do not paste its line into the block or write its Notion row").
* **Action sent (v8.2).** "As the independent reviewer, review for the first time one new whole-change Live QA Plan of seven checks, each to be reviewed (about 730 lines, with four embedded check scripts), and its new companion QA Audit (about 390 lines) for an approved Epic whose delivered change is a pure Python chart module of about 100 lines, an Adapter-owned orchestration entry of about 110 lines and a removed legacy module with an import guard and three migrated callers, judging them against canon plan templates, the delivered code and a canonical evidence writer that needs a separately routed registration change. A written plan with steps exists; no product code is changed and no live run against a provider occurs; QA task creation, QA execution and an independent evidence review follow later in separate sessions."
* **Reading, as printed.** `TypeSafe v8.2: not read (HTTP 403 after 2 attempt(s), sent 2026-10-29T06:35:41Z). Do not fill in a reading by hand.` No cell, probabilities or flags exist to record. The script was not run again.
* **Picks.** Nathan has stated no model or setting for this QA-50 session or for QA-70; none is recorded.
* **Surface advice (QA-70).**
  * The continuing Isis top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this Plan and its QA Audit are on `main`.
  * Read access to `main`: this Plan, the QA Audit, the Guide, the three QA-10 records, the Specification and Implementation Plan with their v1.1 reviews, the three lineage reviews, the DOC-20 record, `docs/pfcanon/` (Plan Templates, Glow QA Guide, Change Process Guide, HDE Schemas and Artifacts, HDE Governance, the Separation Build Checklist and the current HDE Build Notes), `tools/qa/qa_harness.py`, `tools/evidence/update_evidence_index.py`, `.github/workflows/ci.yml`, `ci/checks/classify_ci_changes.py` and the delivered code and tests.
  * The QA-70 Notion page, read-only.
  * Optional, to repeat section 9.4's smoke validation: a closed-rails Python 3.12 environment with CI's install from a full-history clone, run under `env -i`; any run stays in a throwaway clone.
  * An authenticated GitHub read only if the review needs hosted CI facts beyond those recorded here.
  * Write access to one branch and one pull request under `docs/ephemeral/`.
  * Not needed: product code changes, open rails, vendor, Railway, database or deployment access, evidence writes, or Notion writes.

## 23. Result and routing

* **State: `PLAN_PENDING`.** One complete `QA_PLAN` v1.0 and, separately, one complete `QA_AUDIT` v1.0 (`docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md`), both with `AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING`, saved and read back. Isis reviews this Plan independently at QA-70; Kronos does not approve it.
* **Next:** QA-70 — Review Whole-Change QA Plan — 102726.1 (https://app.notion.com/p/4064590a05eb819ca94af85f1561b596), continuing Isis.
* **Routes not taken:** `AUDIT_COMPLETE` → QA-60 (the Plan completed in this invocation); `BLOCKED` (no source, tool or authority gap prevented the Plan).
* **Unresolved items and owners:** PI-01, PI-02 and PI-03 (Product Owner); CCR-5 and CCR-6 (Product Owner; Isis reviews CCR-6's route effect at QA-70); QR-07 (Product Owner); prompt-use persistence (GCFPE management).
* PF10 addendum output: none; QA-50 is not an addendum producer.

## Nonclaims

This Plan is authored process material. It is not QA execution, a QA verdict, readiness, acceptance of HDE-EPIC041, an approval of itself, an execution task, Ops, deployment, release, a canon change, a PF10 addendum, PF23 publication, PF09 or board movement, or closure. Its smoke validation was preapproval readiness in a throwaway clone. It edits no file outside `docs/ephemeral/`. Merging it preserves the record and approves nothing (D21-C).

ASK OK?
