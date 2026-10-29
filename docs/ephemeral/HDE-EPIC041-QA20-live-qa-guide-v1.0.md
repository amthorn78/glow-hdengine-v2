---
artifact_type: LIVE_QA_GUIDE
artifact_version: "1.0"
logical_id: HDE-EPIC041-QA20-LIVE-QA-GUIDE
LIVE_QA_GUIDE_ID: docs/ephemeral/HDE-EPIC041-QA20-live-qa-guide-v1.0.md
state: GUIDE_READY
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
predecessor: none (first Live QA Guide for HDE-EPIC041; no prior Guide, partial Guide or BLOCKED result exists)
QA_READINESS_ID: docs/ephemeral/HDE-EPIC041-QA10-qa-readiness-v1.0.md (QA_READINESS v1.0, READY_FOR_QA)
REALITY_AUDIT_ID: docs/ephemeral/HDE-EPIC041-QA10-reality-audit-v1.0.md (REALITY_AUDIT v1.0, COMPLETE, of main 6a0f55f0)
CHANGE_AUDIT_TRIAGE_ID: docs/ephemeral/HDE-EPIC041-QA10-change-audit-triage-v1.0.md (CHANGE_AUDIT_TRIAGE v1.0, COMPLETE, 28 rows)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1, blob a41b10b58ce9)
SPECIFICATION_REVIEW_ID: docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md (CF-E-30 INITIAL_APPROVE, Thoth)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1, blob 2ff65a377ae3)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE, Isis)
delivery_lineage: "WU-PR-01 #791 squash e72c9bac, docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-lineage-review-v1.0.md ACCEPT; WU-PR-02 #796 squash 9843934f, docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-lineage-review-v1.0.md ACCEPT; WU-PR-03 #800 squash 634be154, docs/ephemeral/HDE-EPIC041-WU-PR-03-pr-lineage-review-v1.0.md ACCEPT"
DOCUMENTATION_COMPLETION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-03-documentation-completion-v1.0.md (DOC-20 COMPLETE)
ops_lineage: none (Plan v1.1 §6 declares no Ops unit)
approved_amendments: none
remediation_lineage: none
repository: amthorn78/glow-hdengine-v2
repository_head_read: ad537323e7a99e6768ae3e4b78f188a673ed4cf6 (origin/main; "HDE-EPIC041-QA10-records", direct commit by amthorn78 2026-10-29T04:38:31Z, sole parent 6a0f55f0; adds only the three QA-10 records)
producer: Isis, the continuing Lead Developer who established readiness for HDE-EPIC041 (role continuity per D27; this session's platform identity is not directly known to it and is not invented)
prompt: QA-20 — Create Live QA Guide — 102726.1 (https://app.notion.com/p/4064590a05eb810ca861ff615ddb7e79; page state 2026-10-27T13:14:52.288Z, read in full)
r1_row: GCF-20 (GCF-20.GUIDE)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
ecosystem_release: GCFPE-20261027.1 / 102726.1 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261027.1 / 102726.1", exactly 56 members; page state 2026-10-28T00:52:53Z, re-read for this Guide)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.3.md (741 lines, 102,755 bytes, sha256 6fa054b1e51cf76fd795e460cec039a51caf99cec16fe1521f0a00febff15f3c; read in full to the authored eof; provenance, not a gate)
pf10_addenda: "2.1 (S19 decisions): not engaged. 2.2 (planning documents and PF-Canon versions are never inputs; close-pack writer only at close): applies to every QA evidence artifact, Index/Mirror row, path proof and close pack (§7.5, §12). 2.3 and 2.4 (WU-PR-01 and WU-PR-02 lineage records): their deferred obligations are reconciled in the Reality Audit §12.2 and carried in §12"
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-20
canon_conflict_register: CCR-1 to CCR-4 carried unchanged; CCR-5 PROPOSED (QA-10 triage #28), carried unchanged and still unreviewed (§13)
next_stage: QA-50 — Create Whole-Change QA Audit and Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81dbb28ed028d68b8816), continuing Kronos
authored_at: 2026-10-29 (UTC)
typesafe_qa50: "TypeSafe v8.2: not read (HTTP 403 after 2 attempt(s), sent 2026-10-29T04:50:15Z)"
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-QA20-20261029
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    requirements: R-01 to R-04; AC-01 to AC-05; work units WU-PR-01, WU-PR-02, WU-PR-03
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: QA-20 — 102726.1 (https://app.notion.com/p/4064590a05eb810ca861ff615ddb7e79), revision as of 2026-10-27T13:14:52.288Z
    role_stage: continuing Isis / GCF-20.GUIDE (QA-20)
    captured_at: 2026-10-29
    runtime_identity: not directly known (D27)
    inherited_usage: HDE-EPIC041-QA10-20261029
    outcome: GUIDE_READY
    result_references: this Guide at the path above; its pull request and merge commit do not exist at writing and are recorded by the stage that reads them
    repository_persistence: PENDING (no docs/changes/GCFPE_PROMPT_PROVENANCE.md, Reality Audit N-008; owner GCFPE management; non-gating)
---

# HDE-EPIC041 — Live QA Guide v1.0 (QA-20): GUIDE_READY

## 0. What this Guide is

**GUIDE_READY.** This is the one live guide that turns the accepted QA-10 readiness package into the facts Kronos needs to audit and plan QA of HDE-EPIC041. GUIDE_READY is this author's completion state; it introduces no Guide approval and no `ASK OK?` gate (QA-20 "Required result and routing"; Glow QA Guide §3.1.1, §3.1.2).

* **It states** what was delivered, which acceptance obligations still need independent verification, the environment and rails it must run under, the integration risks, the evidence QA must produce and register, the limits, the permitted and forbidden actions, data handling, recovery expectations and the verification still owed.
* **It is not** Kronos's QA Audit, QA Plan, an executable task, an evidence review, a final QA Report or an RCA. It names no `check_id`, step order or command sequence as required; those belong to the QA Plan (Plan Templates §1 "Live QA Plan"; Glow QA Guide §3.4.14). It prescribes no result and does not limit what Kronos may audit in the actual system. Where it names a repository locus, the locus is copied from the Reality Audit, the in-flight records or canon; any observation made for this Guide is labelled "QA-20 observation" and is consult input for Kronos's own QA Audit (Change Process Guide §0.5.1, "QA-planning locus provenance lock").
* **It is not** QA, a QA verdict, QA execution, readiness, acceptance, a scope change, a repair, PF10 text, a canon change or closure.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `ad53732`. `git diff --stat 6a0f55f ad53732 -- . ':(exclude)docs/ephemeral'` is empty, so canon and code are byte-identical to what QA-10 read. This branch changes nothing under `docs/pfcanon/`. Terms searched (`grep -n -i` over `docs/pfcanon/*.md` and `docs/ephemeral/HDE-EPIC041-*`): Live QA Guide, QA Guide, QA-20, GUIDE_READY, Live QA Plan, step log, evidence index, update_evidence_index, admission, open rails, production-functional, vendor-focused, Step-0B, doc delta, D0 Discovery, QA RCA, close mutation set, functional proof, interactive-safe.

| Title (file) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| Glow QA Guide (`PF19-Canon-Glow-QA-Guide-v3.0.7.md`) | §2.3 "Rails & environment posture"; §3.1 "Intent" and "Workflow placement"; §3.1.1; §3.1.2; §3.1.3; §3.2 "Checklist"; §3.3 "Environment constraints — pre-App, no-user QA mode"; §3.4.1 to §3.4.14; §3.5.5 "PO Live QA sessions (vendor-first rails)"; §3.5.6 "Vendor vs non-vendor steps in Live QA plans"; §4.1 to §4.4.7, including "Interactive-shell safety (normative; operator-facing QA instructions)" | What the Guide is and is not (§0); rails and `captured_env` (§4); step classes (§5.4); evidence grammar, step logs, manifest, indexing and same-PR parity (§7); Moon Loop and non-QA-root routing (§11) |
| Plan Templates (`PF27-Canon-Plan-Templates-v2.0.6.md`) | "Purpose & scope", "Governed artifacts", "Artifact execution boundary", "Reality Audits historical-context boundary", "Portability and provenance", "Exact technical facts and secret safety", "Repository loci and file minting" (opening); §1 "Mandatory Step-0 artifacts" and "Step-0B — Doc Delta Capture"; "Runbook Check Matrix" rules, including "Functional proof requirement" | The Live QA Plan is Kronos's template, not this Guide's (§0); Step-0B (§7.3); functional proof check (§5.3) |
| Change Process Guide (`PF06-Canon-Change-Process-Guide-v2.5.5.md`) | §0.4.1 "Live QA discovery and RCA (execution requirements)", §0.4.1.1 to §0.4.1.3; §0.5.1 "Epic path normalization", including "Plan path provenance", "Plan locus validation labels", "Audit provenance in planning artifacts", "QA-planning locus provenance lock" and "Environment variable name governance"; §3.5.2.8 "Live QA via harness (required for epic closeout)", including "Post-QA documentation drainage ordering (normative)" | D0 Discovery and QA RCA & Doc Delta summary (§7.3); locus provenance (§0); harness, functional proof, evidence landing routes and CI entrypoint tests (§5.3, §7.4); drainage after QA (§12) |
| HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`) | §3.4 "Open rails (controlled)", including "Production-functional epic live-proof requirement" and "Other production-affecting scope"; §9.1.5 "Integrated readiness, remediation and closure" | Open-rails conditions (§5); QA-10 return and remediation (§11) |
| HDE Schemas and Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`) | §8.17 "Scope / root", "Current-state evidence", "Close-run family exception"; §8.17.1 "Root and step directories" | QA root layout; which artifacts are indexed is the QA Plan's to decide; no Epic close-run family (§7) |
| HDE Build Checklist — Separation (`PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md`) | Task HDE-SEPA006 and Subtasks .1 to .3 | Deliverables, required governed evidence and "required indexing through the existing governed writer" (§3, §7) |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.3.md`, the current controlled PF10) | Whole file | 2.2 R-1 to R-3 bind QA evidence, Index/Mirror rows, path proofs and the close pack (§7.5, §12); 2.3 and 2.4 deferred obligations (§12); 2.1 not engaged |
| Technical Writing Best Practices (`PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`) | §3 "Truth and source fidelity", "Canonical ownership", "Claim-state separation", "Structure and language"; §11; §12 "Task, plan, and execution-document writing", "Reports and retrospectives", "Runnable guides and usage documentation" | Source fidelity; observed versus required versus unknown; no invented locus |
| AGENTS.md | "HDE-EPIC041 current posture"; closed rails; pytest readiness rule; redaction rule; QA output placement; governed-evidence rules; "Evidence harness" roster line | Delivered posture (§2); environment (§4); data handling (§10); writer and validators (§7.4) |
| In-flight records (current versions) | The three QA-10 records (whole); Specification v1.1 and review v1.1 (whole); Plan v1.1 and review v1.1 (whole); the three lineage reviews (whole); DOC-20 v1.0 (whole) | Every obligation carried below |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

Scoped override: none new. QA-10's recorded override (HDE Governance §9.1.5 and Glow QA Guide §3.1.1 over the Reality Audits document's PO-at-closure intent) stands. Canon silence: none decisive.

## 1. Intake verification (QA-20 Execute step 1)

| Check | Result | Evidence |
| :- | :- | :- |
| QA_READINESS is `READY_FOR_QA` and complete, with its two companions | Yes | The three records, read end to end |
| Precondition: the three QA-10 records are on `main` | Yes. They landed by a direct commit, `ad53732`, by amthorn78 (2026-10-29T04:38:31Z), not by a squash of a pull request; the readiness record's working branch `docs/20261029-hde-epic041-qa10-readiness` is not on the remote. The Product Owner's direct-main route for `docs/ephemeral/` records is permitted (AGENTS.md "Operating routes and authority") | `git log -1 ad53732`; `git ls-remote origin` |
| Later material evidence since readiness | None. `git diff --name-status 6a0f55f ad53732` adds exactly the three QA-10 records under `docs/ephemeral/`; code, tests, CI, canon and governed evidence are byte-identical to the audited head | QA-20 observation |
| Approved bases, amendments, remediation | Unchanged: Specification v1.1 and Plan v1.1, no amendment, no remediation, no Ops | Readiness §2 |
| Product Owner dispositions | D-1 "Retire it" (2026-10-28); the 2026-10-28 direction recorded in HDE Build Notes 2.2. CCR-5 remains unruled (§13) | Readiness §2.4; triage §6 |
| Selected release and prompt identity | GCFPE-20261027.1 / 102726.1, 56 members; QA-20 and QA-50 at 102726.1 are members | Register, re-read |

**Readiness is not invalidated.** No new evidence shows a failed approved objective or a recoverable QA-10 evidence gap. One new QA-planning fact was found: the authorized evidence writer does not yet register any HDE-EPIC041 artifact (G-OBS-01, §7.4). It bears on how QA evidence gets indexed, which QA-10 already assigned to QA (QR-04); it is not an objective of the approved Specification (Specification §8: "a governed-evidence obligation, not a requirement") and it does not change readiness. The `BLOCKED` route to QA-10 is therefore not taken (§15).

## 2. Delivered behavior and interfaces

The delivered change, as the Reality Audit observed it at `6a0f55f0` (identical code at `ad53732`). Each line cites the Reality Audit's evidence id; Kronos re-verifies on the actual system.

### 2.1 The Adapter-owned chart entry (R-01)

* `adapter/chart_orchestration.py::load_chart(*args, **kwargs)` (E-018). It is the only place on the chart path that reads `SAFE_MODE` (for the log field only), both clocks and the correlation id, reads the two pinned lists anchored at the repository root, acquires the fixture chart and emits one keys-only log line (QA10-OBS-01).
* Accepted forms (E-018, E-019; Plan v1.1 §5.3):
  * positional: at least three positional strings, the first shaped `YYYY-MM-DD`, the second `HH:MM`;
  * keyword: `birthdate`, `birthtime`, `place`, optional `tz` (the form the compat-determinism generator uses).
  * `tz`, `correlation_id` and `log_sink` are read from keywords only; a fourth positional argument is ignored.
* Every other shape raises `TypeError("Invalid arguments to load_chart")`: no arguments, `("user-abc",)`, keyword `birthdate="user-abc"`, `("1990-01-01",)`, `(42,)` (E-019). **This is the one intended failure-behavior change** (Plan I-4; D-1); the removed loader raised `AttributeError` or returned fallback data for the legacy shapes.
* Log line: exactly one per call, on success and on error; keys in order `ts, route, provider, source, status, duration_ms, safe_mode, correlation_id`; fixed values `route` `loader.load_chart`, `provider` `fixtures`, `source` `default`; `status` `ok` or `error`; no birth input value in the line once `ts` is removed (E-018, E-019). `loader.load_chart` is a label, not a module (AGENTS.md).
* Correlation id: passed through when given; synthesized when absent, matching `^CID-[a-f0-9]{16}$` (E-019), through `engine.util.input_validators.ensure_cid` (E-016, E-018).
* Sink: `log_sink` callable, else the module logger `adapter.chart_orchestration`; a raising sink does not break the call; no file is written on any path (E-019).
* No route, Flask app, blueprint or `__main__` (N-005); no production entry, CLI, compat or BodyGraph module imports it (N-004); its only non-test caller is the generator (§2.3).

### 2.2 The pure Engine chart module (R-02)

* `engine/charts/pure.py`, 101 lines, imports exactly `re`, `unicodedata` and `typing` (E-012, E-013).
* `validate_birth_inputs(birthdate, birthtime, place, tz, *, iso_codes, iana_zones)` checks date, time, place, tz presence, tz value in that order; each refusal is `ChartInputError("READER_INVALID_INPUT", <message>, {"field": <date|time|place|tz>})` with messages `invalid date`, `invalid time`, `invalid place`, `tz required on internal path`, `invalid tz` (E-013, E-019).
* `normalize_chart(obj)` keeps the gates normalization; the fixture chart's canonical bytes are recorded in E-019.
* It imports nothing from `engine.util.input_validators` (AUD-CORR-1; E-013).

### 2.3 Removal, guard and migrated callers (R-03)

* `engine/charts/loader.py` is removed; `engine/charts/` holds only `pure.py`; no shim (E-012, N-003).
* `tests/charts/test_chart_loader_import_guard.py` fails if the module path or an import of it returns; it scans tracked `.py` files outside the classifier's historical prefixes and the two planning trees (518 files at `6a0f55f0`, 0 findings) (E-030, N-001). Stated limit: it does not recognize a module name assembled at run time or an attribute chain through a parent package; such a form would fail at import (triage #3).
* C-1 `scripts/make_compat_determinism_artifacts.py` imports the entry and exits 2 with `compat_public not implemented` before its chart call, writing nothing (F15 hop 1; N-006). Its compat computation is not restored (FND-005; QR-08).
* C-2 `tests/loader/test_load_chart_fixture_only.py` and C-3 `tests/loader/test_loader_logs_keys_only.py` call the entry with an injected sink (F15 hop 2; E-029).
* The supported-caller inventory at `6a0f55f0`: 69 files, 25 live and 44 under historical captures, each with a disposition (Reality Audit §12.4).

### 2.4 Boundary checks and preserved outputs (R-04, AC-05)

* The change's tests (E-029): `tests/charts/test_chart_pure_purity.py` (5), `tests/charts/test_chart_pure_interface.py` (8 cases), `tests/adapter/test_chart_orchestration.py` (20 cases), `tests/charts/test_chart_loader_import_guard.py` (4), `tests/scripts/test_make_compat_determinism_artifacts.py` (1), and the migrated C-2 (2) and C-3 (1). Retained coverage named by HDE Build Checklist — Separation: `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on`.
* CI owner registration (E-033): `engine/charts/pure.py` → purity, interface and orchestration tests; `adapter/chart_orchestration.py` → orchestration tests; `engine/charts/loader.py` → the guard; the generator → its test.
* Preserved and unchanged (E-036, E-026, E-027, E-011): 13 of 13 call shapes equal against the removed loader; `artifacts/compat/AB.json`, `BA.json`, `identity_hash.txt`; `artifacts/logs/loader_call.jsonl`; release `1.3.0`, 45 members, no chart path a member (N-010).

### 2.5 What did not change (scope boundary for QA)

No public route, flag, payload field, CLI command or option, provider contract, HTTP home or release member (Specification §4; Reality Audit §5 to §8, F1 to F14 unchanged). Reader, `hdctl showcompat` and Engine Core are untouched. No vendor or database acquisition exists on the changed path (§8 of the Reality Audit).

## 3. Acceptance obligations and objective coverage

QA-10 found every objective achieved at the implementation level and none failed; each still needs independent verification (Readiness §4; HDE Governance §9.1.5: "pre-QA absence establishes neither failure nor achievement"). The "existing evidence" column names what QA may bind instead of re-running; QA-50 decides, and a re-run of a closed-rails group CI already ran states the gap it closes (QA-50 Phase 2 step 2).

| Objective | What QA must independently establish | Existing evidence QA may bind | Owed at |
| :- | :- | :- | :- |
| R-01 / AC-01 | The entry owns every R-01 concern and no Engine chart code holds one; a supported path exists for each supported use; no acquisition, so the resolver clause is vacuous; behavior of §2.1 on the actual system under closed rails | E-018, E-019 (local probes, not QA); exact-head CI runs 40723983402 (#791) and 40774524113 (#796) (E-031) | QA execution (QR-01) |
| R-02 / AC-02 | Purity at import and in calls; the interface and side-effect account of §2.2 | E-013, E-014; the purity tests' negative self-tests (E-014) | QA execution (QR-01) |
| R-03 / AC-03 | Module absent, no importer, guard passes and fails a planted importer; every inventory member has a disposition; C-1 exits 2 with no file written from a temporary working directory, with the repository's requirements installed | E-012, E-030, N-001, §12.4; WU-PR-02 lineage review §3 (local run at `9843934f`) | QA execution (QR-01, QR-02) |
| R-04 / AC-04 | The boundary checks pass on the actual system, with commands, configuration, tested-source identity, results, actor, time and limitations recorded, and the required governed evidence indexed | E-029, E-031, E-033; the PR records | QA execution and indexing (QR-01, QR-04) |
| AC-05 | Caller output and failure behavior preserved; no fallback in the changed boundary; running the covering tests leaves `git status --porcelain` empty | E-036, E-019, E-026, E-027, E-011; clean trees recorded in the lineage reviews | QA execution (QR-01) |
| Specification §4 items 3 to 5 | The open-rails determination still holds on the actual system (§5) | QA10-OBS-07; N-004, E-018 | QA Audit and QA Plan (QR-03) |
| Specification §6 D4, §8 | Governed evidence produced by canonical tools and indexed by the authorized writer; tested-source identity distinct from evidence-storage commits | None exists (E-021) | QA Plan, execution, QA-110 (QR-04; G-OBS-01) |
| Specification §9 | "Live QA is required for eventual close of this Epic" | None | The whole QA chain (§5.3) |
| Specification §10 | Doc-delta surfaces at Step-0B; close pack at CL-05 | None (E-021; expected before QA) | Step-0B (QR-05); CL-05 (QR-09) |
| Specification §11 TI-01 to TI-07 | Each proved, carried, promoted or dropped by close | Readiness §4.4 | Final QA Report and closure; TI-07/CCR-1 at CL-05 |

Every in-scope criterion must be covered by at least one QA step, and every step must map to a criterion or an evidence-capture requirement (Glow QA Guide §3.4.14; Plan Templates "Runbook Check Matrix": no check "solely for good measure").

## 4. Environment and setup constraints

* **Target.** The repository itself, `amthorn78/glow-hdengine-v2`, on a current `main` that contains the delivered code (identical since `9843934f` outside documentation and planning paths, E-032). There is no deployed, production or vendor target for this change (N-004; §5).
* **Rails and pins.** Closed rails: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0` (AGENTS.md "Closed rails default"; Specification §9). Every primary log records `captured_env` with at least `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ` (Glow QA Guide §2.3). `APP_ENV=dev` is the value the QA-10 probes and the lineage reviews used. Do not mint any other environment variable name as an input or evidence key (Change Process Guide §0.5.1).
* **`SAFE_MODE` exception for one obligation.** The entry's `safe_mode` field must be observed for `SAFE_MODE` set to `1`, to `0` and unset (QR-01; Plan WU-PR-01 tests). That is an input to the function under test inside a closed-network run (`ALLOW_NETWORK=0`), not an opening of rails for an acquisition; the plan step states it explicitly and records the values it set.
* **Python and install.** CI uses Python 3.12 (`.github/workflows/ci.yml` line 85, QA-20 observation; Readiness QR-10). Pytest-dependent checks, the generator test and the evidence tools' `--check` modes need what CI installs: `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, then `python -m pytest --version` as readiness proof (AGENTS.md "Pytest readiness rule"). QA-10 could not run these without installing (E-024, E-030).
* **Clean environment.** The working container exports credentials; run checks under `env -i` with only the pins above set (OBS-2). Record secret-bearing names only as `SET` or `UNSET`.
* **Clone.** Use a full-history clone (OBS-5). The clone this Guide was written from is shallow (50 commits); facts needing deeper history come from the Reality Audit, which used an unshallowed clone.
* **Known local facts.** `scripts/scratch.py` is a tracked `.py` holding Markdown notes, which the guard searches as text (OBS-6); with the classifier changed in the same push, a deleted registered owner test reports `CI_FULL_VALIDATION_TEST_INVALID` before `CI_REGISTERED_OWNER_TEST_DELETED` (OBS-7); `ruby` is at `/usr/local/bin` and must be on an `env -i` `PATH` when a check needs it (OBS-8).
* **Venue.** Not material to any claim of this change; record venue as `NOT CLAIMED` unless the QA Plan makes it a proof axis with the four statements Change Process Guide §3.5.2.8 requires.
* **Hosted CI on `main`.** The push run on `6a0f55f0` is expected to stop at classification on `cline_skills/` (E-035); it is not an HDE-EPIC041 result (QR-07; Plan RK-06). A QA pull request classifies only its own changed paths. `ad53732` changes only `docs/ephemeral/`, which the workflow's push filter excludes. Neither hosted outcome was read here (no credential).

## 5. Rails posture and the open-rails binding conditions

### 5.1 Carried verbatim (Specification v1.1 §4; Plan v1.1 §11)

* **Item 3.** "*Binding condition.* If the Implementation Audit finds that any affected surface, including the new orchestration entry, is used to produce such a feature, or reaches vendor acquisition in a deployed or CLI path, the mandatory bounded live vendor test (synthetic data only, `SAFE_MODE=0`, `ALLOW_NETWORK=1`) applies to this Epic's QA Plan. No exemption or non-vendor substitute then applies. Closed-rails proof, static validation, repository inspection, generated evidence, an OPS observation or exemption language does not replace it."
* **Item 4.** "*Broader scope.* This Specification records no exemption from the broader production-affecting open-rails requirement. If the Implementation Audit finds the changed boundary can affect runtime compute, vendor ingest, database retrieval or production-used CLI/API behavior, the QA Plan must carry a bounded open-rails step or an exemption authorized and recorded under the Product Owner. Silence is not an exemption."
* **Item 5.** "*Authorization.* The row authorizes no live vendor or production database activity. Any live step needs separate, task-specific Product Owner authorization (§9)."

### 5.2 Determination carried

Neither item 3 nor item 4 is met at `6a0f55f0` (Implementation Audit §6; QA10-OBS-07): no production entry point, CLI path or vendor path reaches the entry or the pure module (N-004), and the changed boundary acquires nothing from a vendor or database (E-018). HDE Governance §3.4 "Production-functional epic live-proof requirement" and "Other production-affecting scope" therefore do not attach on this evidence. **If the QA Audit or any later stage finds new reach, both items re-attach**, and a live step then needs separate, task-specific Product Owner authorization; the Guide does not authorize one. CCR-3 (HDE Build Notes 2.1, vendor decisions) stays not triggered for the same reason.

### 5.3 What "Live QA is required for eventual close" means for this change

* Specification §9's requirement is met by the Live QA stage every Epic completes (Change Process Guide §3.5.2.8, §0.4.1): an approved QA Plan executed under closed rails, with governed evidence under the Epic QA root, a D0 Discovery artifact and a QA RCA & Doc Delta summary. It is not, on this evidence, an open-rails or production step.
* The change alters a functional seam, the adapter-to-engine chart path (Change Process Guide §3.5.2.8 lists "adapter-to-engine behavior"). The QA Plan therefore needs at least one functional proof check that exercises that runtime path and captures an observable result, not only static artifacts (Plan Templates "Functional proof requirement"; Glow QA Guide §3.1: "Functional changes require trustworthy runtime functional proof on the changed surface, or a CI-sourced proof that actually executes it").
* Every entrypoint command the QA Plan documents needs a CI test that runs it under the canonical pins (Change Process Guide §3.5.2.8, "Entrypoint regression test exists in CI"). The change's own tests and the generator test are CI-registered (E-033); a QA-created harness or new entrypoint is not, and a missing required entrypoint routes through the normal PR path before QA relies on it (Glow QA Guide §3.4.8).

### 5.4 Step classes (Glow QA Guide §3.5.6)

On current evidence every QA step for this change is class 2, internal functional and determinism, or an evidence-publication action. No class 3 vendor step attaches (§5.2), so there is no Product Owner Live QA vendor workload, and no class 1 production handshake (Step-0C applies only when a plan claims prod-like behavior). The QA Plan labels each step's class and records the Product Owner's chosen execution arrangement (D27); execution creates no acceptance authority.

## 6. Integration risks

| Id | Risk | Why it matters for QA | Source |
| :- | :- | :- | :- |
| IR-01 | The purity harness proves absence only for the entry points it patches | A side effect through an unpatched entry point is outside the delivered proof; QA decides whether its own check closes that gap | Triage #2 limits |
| IR-02 | The guard does not recognize run-time-assembled names or parent-package attribute chains | A negative guard result is bounded to the forms it recognizes; such a form would fail at import because the module is absent | Triage #3; WU-PR-02 lineage review §5 |
| IR-03 | C-1's exit 2 rests on `engine.compat.compute` lacking `compat_public` | If `compat_public` were restored, C-1 would proceed to its chart calls and its write of `artifacts/compat/identity_hash.txt` (F15 hop 1); restoring it is out of scope (FND-005) | Reality Audit §11; QR-08 |
| IR-04 | `ensure_cid` lives in `engine/util/input_validators.py`, whose module imports `secrets` and whose other helpers read files relative to the working directory | The entry uses `ensure_cid` only; the pure module imports nothing from that module. QA verifies the entry from a foreign working directory and does not test `input_validators`' other caller (FND-006) | E-016, E-018; QR-08 |
| IR-05 | The keys-only log line carries a clock-derived `ts` | A substring check that includes `ts` is clock-dependent (OBS-4, resolved in C-3 by removing `ts` before the check); QA checks follow the same rule | E-029; HDE Build Notes 2.3 |
| IR-06 | Canon still describes the removed loader as current | HDE Architecture §1.1, HDE Mechanics Guide §1.1 and HDE State of the Repository §2.2 are drift canon anticipated, not the delivered contract; test the delivered boundary (§2) and AGENTS.md "HDE-EPIC041 current posture" | QR-06; QA10-OBS-08 to -10 |
| IR-07 | Evidence publication needs a writer change outside the QA root | See G-OBS-01 (§7.4); unplanned, it leaves QA evidence unindexed and the PF09.3 indexing obligation unmet | §7.4 |
| IR-08 | `main` push CI is red for an unrelated cause | Not an HDE-EPIC041 result; read current-head CI of the QA pull request | QR-07 |
| IR-09 | Local Python differs from CI's 3.12 | Use CI's version and install for decisive runs | QR-10 |
| IR-10 | A run that writes a tracked file | Any tracked-file change after a covering test contradicts AC-05; preserve it as evidence (§11) | Specification AC-05; Plan I-5 |

## 7. Required evidence and indexing

Evidence publication and indexing are part of each QA step's instructions, not an optional add-on (QA-20 and QA-50 "Required QA evidence indexing"; HDE Build Checklist — Separation Task HDE-SEPA006 "Required governed evidence is indexed through the existing authorized writer"; Subtask .3 "required indexing through the existing governed writer"; Specification §8).

### 7.1 Evidence QA has to produce

* **Boundary evidence**: entry behavior of §2.1 and pure-module behavior of §2.2, positive and negative, including purity at import (R-01, R-02, R-04).
* **Caller-regression and migration evidence**: guard result and its negative probe, inventory dispositions, C-1 run (exit 2, stderr, no file), C-2 and C-3 results, retained-coverage tests (R-03, R-04).
* **Preservation evidence**: output and failure equality, compat bytes and the tracked log unchanged, release membership unchanged, clean tree after every covering run (AC-05).
* **Open-rails determination record**: the QA Audit's confirmation or revision of §5.2 (QR-03).
* **Execution deliverables**: a D0 Discovery artifact before behavior steps (Change Process Guide §0.4.1.1); Step-0B doc-delta capture (§7.3); a QA RCA & Doc Delta summary (Change Process Guide §0.4.1.2), either as a section of the close report or as `audit/EPIC-041_QA_RCA.md`, the canonical filename that section names. Because HDE Build Notes 2.2 R-3 places the close-pack write after the closure decision (CCR-5), the QA Plan states where the summary lives and when it is written.
* Each record carries the actual commands, configuration, tested-source identity, results, actor, time and limitations, and keeps tested-source identity distinct from the later evidence-storage commit and review-time HEAD (Specification AC-04, §8; AGENTS.md "Evidence attribution").

### 7.2 Canonical destinations (Glow QA Guide §3.4.3 grammar; HDE Schemas and Artifacts §8.17)

| Class | Destination | Notes |
| :- | :- | :- |
| Epic QA root | `audit/qa/hde-epic041/` | Lower-case; absent today (E-021). Created by the step that first produces evidence, not pre-created by a generic setup |
| Current-state manifest | `audit/qa/hde-epic041/qa_step_logs_manifest.json` and its `.path_proof.txt` | Keyed by `check_id`; each entry has `check_id`, `status`, full repository-relative `log_path` |
| Decisive receipt per check | `audit/qa/hde-epic041/checks/<check_id>/primary.log` and its `.path_proof.txt` | One per evidence-producing check; `check_id` values are Kronos's to resolve, lower-case ASCII; header contract `pf27.step_log_header.v2` (Plan Templates); statuses `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `PARKED` |
| Check-created outputs | `audit/qa/hde-epic041/checks/<check_id>/<explicit_filename>` | Named in the Plan, referenced by the primary log |
| Doc-delta pair | `audit/docdeltas/hde-epic041_doc_deltas.md` (draft) and `audit/qa/hde-epic041/00_meta/doc_deltas.md` (record) | Specification §10 |
| Authored QA Plan, Audit and reviews | `docs/ephemeral/` | Not execution evidence and never bound by any evidence artifact (HDE Build Notes 2.2 R-1) |
| Transient scratch | `/tmp` | Never indexed, mirrored, path-proofed or referenced as acceptance evidence (Glow QA Guide §3.4.8) |

No per-run, timestamped or "latest" roots (Glow QA Guide §3.4.3; Plan Templates "Artifact execution boundary"). No Epic close-run family is admitted (HDE Schemas and Artifacts §8.17).

### 7.3 Step-0B doc-delta capture (QR-05)

Mechanical, by commands, BLOCKERS and CAVEATS with stable ids, written to the pair in §7.2 and byte-identical at close; PF references by title; the preservation rule applies, and "no deltas" is not emitted while proof-bearing content exists (Plan Templates "Step-0B — Doc Delta Capture"). Content known now, carried as non-mandatory Product Owner-owned candidates:

* DELTA-001: HDE Architecture §1.1, "The checked-in loader remains current repository reality until separately remediated" (QA10-OBS-08; #800's description; HDE Build Notes 2.4).
* DELTA-002: HDE Mechanics Guide §1.1, "The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift" (QA10-OBS-09).
* DELTA-003 (candidate): HDE State of the Repository §2.2, the loader "still mixes input normalization with environment inspection, clocks, provider orchestration, and filesystem logging" (QA10-OBS-10; triage #10).

Drainage into canon happens only after every QA task is complete (Change Process Guide §3.5.2.8, "Post-QA documentation drainage ordering"). No QA step edits a PF document.

### 7.4 Writer, registration and read-only validation

* **Authorized writer.** `tools/evidence/update_evidence_index.py`, the sole active writer of `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, `audit/gates/topology/orientation_demo.txt` and proof companions (AGENTS.md "Evidence harness"). Never hand-edit any of them.
* **Registration set.** The Human Index, its hash sentinel, the Machine Mirror and its checksum, and path proofs, updated in the same pull request as the evidence they describe (Glow QA Guide §3.2 "Same-PR parity", §4.3). Which artifacts are indexed is the QA Plan's decision (HDE Schemas and Artifacts §8.17 "Scope / root").
* **Read-only validation.** `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, `ci/checks/check_mirror_schema.sh`, plus `tools/evidence/validate_evidence_paths.py`, `ci/checks/check_evidence_index_hash.sh` and `tools/evidence/check_lf_endings.py` (AGENTS.md; Reality Audit E-023, E-024). The first two need the CI install (§4).
* **G-OBS-01 — the writer registers no HDE-EPIC041 artifact today** (QA-20 observation at `ad53732`, read-only, consult input for the QA Audit):
  * `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` have no HDE-EPIC041 row (Reality Audit E-021).
  * The writer builds the Human Index from the rows already in `docs/evidence/INDEX.json` plus source-owned per-change lists (for example `EPIC039_QA_PRIMARY_ARTIFACTS` and `EPIC040_QA_PRIMARY_ARTIFACTS`) and the CRD admission table `ADMITTED_CRD_QA`, which HDE Schemas and Artifacts §8.17 names; it has no list or admission for HDE-EPIC041 and no generic discovery of an Epic QA root. Its `--epic-id` option acts only for `HDE-EPIC020`.
  * Consequence: indexing HDE-EPIC041 QA evidence through the canonical writer needs a change to the writer's source first. That is repository tooling outside the QA root, so it is not Moon Loop work; it routes through an approved work item (Glow QA Guide §3.4.8 "Non-QA-root remediation boundary"; Plan Templates "Non-QA-root remediation route"), and the evidence then lands in an evidence-only QA pull request that merges before the close pull request, or in the close mutation set (Change Process Guide §3.5.2.8, "Live QA evidence landing").
  * How earlier Epics' rows were introduced is not established here (history before `0838ba0` is not in this shallow clone).
  * Owner: Kronos plans the registration set, the routing and the dependency in QA-50; Isis reviews it at QA-70; the Product Owner chooses who executes it. QA-110 treats missing required indexing as incomplete work or a tooling outcome, never as behavioral PASS, and returns it to the writer's owner without rerunning valid QA solely to index it.
* **Proof returned to QA-110.** Per step: the evidence paths produced, the writer invocation and its output, the `--check` results, the Index/Mirror rows and path proofs for each registered artifact, manifest membership, and every gap with its owner.

### 7.5 Constraints from HDE Build Notes 2.2

No QA evidence artifact, manifest, Index or Mirror row, path proof or close pack reads, binds, hashes, resolves or requires a path under `docs/ephemeral/`, or pins a PF file name, version or digest; canon is cited by title (R-1, R-2). The close-pack writer runs only at close (R-3; CCR-5). A fact a later stage needs from this Guide or the QA Plan is recorded as text where that stage reads it.

## 8. Known limitations

* No runtime, deployed or production observation exists for this change, and none is needed on current evidence (§5.2).
* QA-10 ran no dependency-requiring check: the generator run and three evidence-tool `--check` runs were not reproduced (E-024, E-030); QR-02 and QR-04 carry them.
* Hosted CI for `6a0f55f0` and `ad53732` is unread here and in QA-10 (no credential).
* Local probes by QA-10 and the lineage reviewers are observations, not CI, QA or governed evidence.
* The purity harness and the guard have the bounded proofs of IR-01 and IR-02.
* This Guide's own repository reads were static, at `ad53732`; it ran no test.

## 9. Permitted and forbidden actions

| Permitted in QA | Forbidden in QA |
| :- | :- |
| Closed-rails runs of tracked, CI-registered tests and entrypoints on the actual repository | Any live vendor or production database call, or opening rails for an acquisition, without separate task-specific Product Owner authorization (§5.1 item 5) |
| Read-only repository inspection and `git` observation for attribution | Editing product code, tests, CI, tools, configuration, governed evidence outside the QA root or `docs/pfcanon/` as part of QA execution; such a change is routed remediation (§11) |
| QA-created evidence-capture files under `audit/qa/hde-epic041/`, named in the Plan | Hand-editing the Human Index, Mirror, sentinels, path proofs, manifests, close reports or acceptance maps |
| Publishing evidence only through `tools/evidence/update_evidence_index.py` | Restoring `engine/charts/loader.py`, adding a shim, or adding time, environment, filesystem, provider or logging access under `engine/charts/` (AGENTS.md) |
| Ephemeral `/tmp` helpers that are never evidence | New features, acceptance criteria, public contracts, tokens or evidence families; per-run or timestamped roots; minted environment variable names |
| Recording doc-delta candidates as non-mandatory and PO-owned | Requiring a PF document update, PF23 publication or PF10 edit as a QA deliverable (Glow QA Guide §3.4.10) |
| | Branch, commit, push, merge or other VCS mutation as a QA execution step; evidence lands by the separately authorized pull-request lane (Glow QA Guide §3.4.9) |
| | Treating C-1's exit 2 as a passing compat gate (AGENTS.md) |

Copy-paste instruction blocks in the QA Plan and tasks are interactive-safe: no shell-terminating control flow; a failing enforcement runs in a subshell and its status is captured, so evidence capture continues (Glow QA Guide §4.3, "Interactive-shell safety (normative; operator-facing QA instructions)").

## 10. Data handling

* Inputs are synthetic: the fixture chart literal and synthetic birth tuples such as C-1's (`1990-05-04`, `14:22`, `Austin, US`, `Europe/Amsterdam`) (E-019). No real person, user or production data.
* The keys-only log line must carry no birth input value; QA evidence that captures log lines keeps that property.
* No secret value is printed, logged or stored; environment probes record `SET` or `UNSET` only (AGENTS.md "Redaction rule"; Plan Templates "Exact technical facts and secret safety").
* No database, cache or vendor data is read or written (Plan v1.1 §9).

## 11. Recovery expectations

* **Clean tree.** After every covering run, `git status --porcelain --untracked-files=all` is empty outside the QA evidence paths the step names. An unexpected tracked-file change is AC-05 evidence: preserve the failure signature in the primary log; do not reset it away before it is captured.
* **Rerun.** One bounded ordinary rerun for a correctable execution or evidence fault under the unchanged approved Plan; the earlier receipt stays in the same evidence stream (QA-50 Phase 2 step 4; Plan Templates "Bounded step-level rerun posture").
* **Moon Loop.** Only for QA-created files under the QA root, minimal and recorded with changed paths and why (Glow QA Guide §3.4.8). A change to product code, tests, tools (including the evidence writer, G-OBS-01), governed evidence outside the QA root or a PF document is routed remediation, cited before any final PASS that depends on it.
* **Failures.** `FAIL_BEHAVIOR`, `FAIL_TOOLING` and `TOOLING_BLOCKED` stay distinct; a missing prerequisite is `TOOLING_BLOCKED`, not a behavior failure (Glow QA Guide §4.4.4, §4.4.5). A second failure or a behavior, scope or Plan change goes to escalation: Kronos's ESC-10 report, then Thoth's ESC-30 (HDE Governance §9.1.5).
* **Readiness invalidation.** A finding that shows a failed approved objective or invalidates the readiness basis returns to QA-10 (same Isis) with its evidence; accepted repair returns to its originating owner.
* **Interruption.** Cancellation is incomplete work, not a QA failure, and consumes no retry. An uncertain write is inspected before any retry.

## 12. Verification still owed and carried obligations

| Id | Obligation | Guide section | Owner and route |
| :- | :- | :- | :- |
| QR-01 | Independent runtime verification of R-01 to R-04 and AC-01 to AC-05 under closed rails | §2, §3 | Kronos (QA-50) → QA-70 → execution → QA-110 |
| QR-02 | C-1 exit 2, no file, temporary working directory, CI's install | §2.3, §3, §4 | Kronos |
| QR-03 | Items 3 to 5 verbatim; determination; re-attachment | §5 | Kronos (QA Audit); Product Owner for any live authorization |
| QR-04 | Governed QA evidence through the authorized writer, same-PR Index/Mirror parity, read-only validation; HDE Build Notes 2.2 R-1, R-2 | §7 | Kronos plans; QA-100 to QA-120 verify |
| G-OBS-01 | The writer needs an HDE-EPIC041 registration before indexing can succeed | §7.4 | Kronos (plan the routed work item and dependency); Isis (QA-70); Product Owner (arrangement) |
| QR-05 | Step-0B doc deltas DELTA-001 to DELTA-003; drainage after QA | §7.3 | Kronos; drainage Product Owner |
| QR-06 | Canon drift is not the contract | §6 IR-06 | Kronos |
| QR-07 | `main` push CI red at classification, not this change's | §4, §6 | Product Owner (classify, relocate or accept) |
| QR-08 | FND-005 to FND-007 out of scope | §2.3, §6 | CL-40 scan; Product Owner |
| QR-09 | Close mutation set at CL-05, including CCR-1's acceptance map and OBS-D1; ordering per CCR-5 | §7.1, §13 | CL-05; Product Owner (CCR-5 ruling before CL-05) |
| QR-10 | Environment facts | §4 | Kronos; QA executors |
| QR-11 | PF09.3 HDE-SEPA006 rows stay Not done until the authorized post-closure update; PF23 manual update non-gating | — | Product Owner |
| QR-12 | TI-02 (items 9 and 10); OBS-9; PR35-LINK; QA10-OBS-14; prompt-use persistence PENDING | — | Product Owner; CI tooling owner; GCFPE management |

Acceptance-map coordination (CCR-1, TI-07): the acceptance map and its viability log are close-pack baseline artifacts (Specification §10). If the QA Plan produces an acceptance-map viability check, it must be meaningful and not default-PASS (Change Process Guide §3.5.2.8); otherwise the QA Plan states that CL-05 owns it.

HDE Build Notes 2.3 and 2.4 deferred obligations: OBS-4, AUD-CORR-1 and the 2.2 bearing on WU-PR-02 and WU-PR-03 are met; OBS-1 and FND-005 to FND-007 persist out of scope; DELTA-001 and DELTA-002 are carried (Reality Audit §12.2).

## 13. CANON_CONFLICT_REGISTER (CCR-1 to CCR-4 carried unchanged; CCR-5 carried, PROPOSED)

| ID | Classification | Sources and clauses | Conflict | Affected | Decision or recommended disposition | Interim treatment | Drainage target and owner | Status | Reviewer, reviewed artifact, decision time |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION | Plan Templates Preflight B against HDE Governance §2.0.19 and HDE Schemas and Artifacts "legacy token compatibility shape" | Is an acceptance map required for tokenless work? | Specification §10; TI-07 | No operative conflict; the acceptance map is listed with no token roster (Ruling R-A) | Close-pack matter for CL-05 | Product Owner (possible canon change) | APPROVED | Thoth, CF-E-30 review v1.1 of Specification v1.1, 2026-10-28; confirmed by Isis, IA-30 review v1.1 |
| CCR-2 | CANON_RECONCILIATION | HDE Governance §9.7.7 against Plan Templates §2 | Business Case content lists differ | Specification §2 | Specification v1.1 satisfies both | None | None needed | APPROVED | Thoth, review v1.1, 2026-10-28 |
| CCR-3 | CANON_RECONCILIATION | HDE Build Notes 2.1 (vendor route selection, production vendor override) against the Specification's "adjacent" reading | Possible reach into the orchestration path | Specification TI-02 | Conditional: governs only if the entry performs resolver-selected vendor acquisition | Not triggered (§5.2) | Implementation Audit determined applicability | APPROVED as conditional | Thoth, review v1.1, 2026-10-28 |
| CCR-4 | CANON_RECONCILIATION | PF09.3 Task HDE-SEPA006 notes against the current HDE Build Notes | Cited loader record no longer in PF10 | Specification §5 | No conflict; PF09.3 states the defect in full | None | None | APPROVED | Thoth, review v1.1, 2026-10-28 |
| CCR-5 | CANON_RECONCILIATION | HDE Build Notes 2.2 R-3 first bullet against Change Process Guide §3.5.1 "Close-mutation-set stage", Glow QA Guide §3.1.3 and Plan Templates §3B "Entries and exit (normative)" | On the ordinary path R-3 requires the closure decision before the close-pack write; the three permanent documents place the close mutation set before the closure decision | Specification §10, §6 D5; Plan v1.1 DL-04; CL-05 | Alternatives (A) R-3 stands, (B) a correcting addendum restores the CL-05 entries and exit; recommended: an explicit Product Owner ruling before CL-05 runs | R-3 governs as written (HDE Build Notes "Precedence, versioning, and scope" §1); QA-20, QA-50 and QA execution unaffected | HDE Build Notes under (B), or the three permanent documents under (A); Product Owner | PROPOSED | Not yet reviewed; proposed by Isis, QA-10 triage v1.0 (full entry and history in its §6) |

This Guide adds no entry. G-OBS-01 is a repository-tooling fact, not a canon conflict: canon leaves the indexed set to the QA Plan and names the writer as the publication route.

## 14. Unresolved items and owners

1. **Manual prerequisite:** Nathan lands this Guide on `main`.
2. QA-50 QA Audit, then QA Plan, by Kronos (§16), including the routing of G-OBS-01.
3. QA-70 review by Isis; QA-80 revision by Kronos if denied.
4. QA task creation and execution under the Product Owner's chosen arrangement; Kronos's evidence review; final QA Report and separate RCA.
5. CCR-5 ruling by the Product Owner before CL-05; CL-05 close mutation set; Isis's closure decision; post-closure maintenance (QR-09, QR-11).

## 15. Result and routing

* **State: `GUIDE_READY`.** One complete `LIVE_QA_GUIDE` with `AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING`, the exact source, PF10, addendum, readiness, audit, triage and delivery lineage in the front matter, and the risks and unresolved items above.
* **Next:** QA-50 — Create Whole-Change QA Audit and Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81dbb28ed028d68b8816), continuing Kronos, expecting separate `QA_AUDIT` and `QA_PLAN` artifacts.
* **Route not taken:** `BLOCKED` → QA-10 (same Isis). No material readiness invalidation or recoverable QA-10 evidence gap was found (§1).
* PF10 addendum output: none; QA-20 is not an addendum producer.

## 16. TypeSafe reading and surface advice for QA-50

* **Method.** Installed TypeSafe scoring skill, request v8.2; script run once before this Guide was saved, session kind `authoring`, label "HDE-EPIC041 QA-50 QA Audit and Plan". No Notion row written (QA-20: "do not paste its line into the block or write its Notion row").
* **Action sent (v8.2).** "As the continuing independent QA authority, create one new whole-change QA Audit and then one new QA Plan for an approved Epic, from a new Live QA Guide and three readiness records (a reality audit, a change-audit triage and a ready-for-QA readiness record): the delivered change is a pure Python chart-validation module of about 100 lines, an Adapter-owned orchestration entry of about 110 lines, the removal of one legacy module with a repository-wide import guard, and three migrated callers, checked against four requirements and five acceptance criteria, and the Plan must cover about a dozen carried obligations including open-rails binding conditions, doc-delta capture and QA evidence publication through a canonical evidence writer that does not yet register this Epic's evidence. A written prompt with steps exists; no product code is changed; local closed-rails test runs may be used to audit; no live run against a provider occurs. A separate independent review of the QA Plan, then QA execution and evidence review, follow later in separate sessions."
* **Reading, as printed.** `TypeSafe v8.2: not read (HTTP 403 after 2 attempt(s), sent 2026-10-29T04:50:15Z). Do not fill in a reading by hand.` No cell, probabilities or flags exist to record. The script was not run again.
* **Picks.** Nathan has stated no model or setting for this QA-20 session or for QA-50; none is recorded.
* **Surface advice (QA-50).**
  * The continuing Kronos top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this Guide is on `main`.
  * Read access to `main`: this Guide, the three QA-10 records, the Specification and Plan with their v1.1 reviews, the three lineage reviews, the DOC-20 record, `docs/pfcanon/` (Glow QA Guide, Plan Templates, Change Process Guide, HDE Schemas and Artifacts, the current HDE Build Notes), the delivered code and tests, and `tools/evidence/update_evidence_index.py`.
  * The QA-50 Notion page, read-only.
  * For auditing by local runs: a closed-rails Python 3.12 environment with CI's install, under `env -i`, on a full-history clone (§4).
  * An authenticated GitHub read only if the QA Audit needs hosted CI facts beyond those recorded in the lineage reviews.
  * Write access to one branch and one pull request under `docs/ephemeral/`.
  * Not needed: product code changes, open rails, vendor, Railway, database or deployment access, or Notion writes.

## Nonclaims

This Guide is authored process material. It is not QA, QA execution, a QA verdict, a QA Audit, a QA Plan, readiness, acceptance of HDE-EPIC041, Ops, deployment, release, a canon change, a PF10 addendum, PF23 publication, PF09 or board movement, or closure. It edits no approved artifact and no file outside `docs/ephemeral/`. Merging it preserves the record and approves nothing (D21-C).
