---
artifact_type: REALITY_AUDIT
artifact_version: "1.0"
logical_id: HDE-EPIC041-QA10-REALITY-AUDIT
REALITY_AUDIT_ID: docs/ephemeral/HDE-EPIC041-QA10-reality-audit-v1.0.md
state: COMPLETE
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
predecessor: none (first QA-10 result for HDE-EPIC041; no prior readiness, audit or triage record exists)
companion_artifacts:
  CHANGE_AUDIT_TRIAGE_ID: docs/ephemeral/HDE-EPIC041-QA10-change-audit-triage-v1.0.md
  QA_READINESS_ID: docs/ephemeral/HDE-EPIC041-QA10-qa-readiness-v1.0.md
producer: Isis, the continuing Lead Developer and whole-change readiness decision owner for HDE-EPIC041 (role continuity per D27; this session's platform identity is not directly known to it and is not invented). Earlier Isis sessions of this change, as provenance only: Isis-55 https://claude.ai/code/session_01Q789u1otbrFy2ZhqojikVt (Specification v1.0); Isis-56 https://claude.ai/code/session_01Q789u35D8uKpsTHJ67oMCz (Specification v1.1; IA-30 reviews v1.0 and v1.1)
prompt: QA-10 — Audit Implementation and Establish QA Readiness — 102726.1 (https://app.notion.com/p/4064590a05eb8161b170fbb23f7aeb28; page state 2026-10-27T13:07:31.843Z, read in full)
r1_row: GCF-20 (GCF-20.PF23 fresh audit and historical comparison; this artifact)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
ecosystem_release: GCFPE-20261027.1 / 102726.1 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261027.1 / 102726.1", exactly 56 members, read 2026-10-29; QA-10 and QA-20 102726.1 are members of the HDE QA hub)
repository: amthorn78/glow-hdengine-v2
repository_head_audited: 6a0f55f07607ddfea5590ed8ee080764e029b31a (origin/main after `git fetch origin main`; subject "cline skills"; parent 3a3d3f66, the #802 merge)
pf23_comparison_pin: 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b (the commit PF23 v1.2.3 audits)
audited_at: 2026-10-29T03:50Z to 2026-10-29T04:06Z (UTC)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.3.md (741 lines, 102,755 bytes, sha256 6fa054b1e51cf76fd795e460cec039a51caf99cec16fe1521f0a00febff15f3c; read in full, ending at the authored `<eof>`; provenance, not a gate)
pf10_addenda_applicable: "2.2 (planning documents and PF-Canon versions are never inputs; applies to what may depend on this record); 2.3 and 2.4 (the WU-PR-01 and WU-PR-02 lineage records; their deferred obligations are reconciled in §12); 2.1 (S19) not engaged"
pf10_addendum_output: NOT_PRODUCED_BY_QA-10
canon_conflict_register: CCR-1 to CCR-4 carried unchanged; CCR-5 (close-stage ordering) PROPOSED by the triage (#28), carried here (§12.5)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-QA10-20261029
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    requirements: R-01 to R-04; AC-01 to AC-05; work units WU-PR-01, WU-PR-02, WU-PR-03
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: QA-10 — 102726.1 (https://app.notion.com/p/4064590a05eb8161b170fbb23f7aeb28), revision as of 2026-10-27T13:07:31.843Z
    role_stage: continuing Isis / GCF-20 (QA-10)
    captured_at: 2026-10-29
    runtime_identity: not directly known (D27)
    inherited_usage: HDE-EPIC041-DOC20-WU-PR-03-20261029
    repository_persistence: PENDING (docs/changes/ holds only AUDIT_RESULTS.json and AUDIT_SUMMARY.md; no GCFPE_PROMPT_PROVENANCE.md; owner GCFPE management; non-gating)
---

# HDE-EPIC041 — Reality Audit v1.0 (QA-10)

**Status: COMPLETE.** This is the fresh factual audit of the delivered HDE-EPIC041 change on `main` at `6a0f55f0`, in the thirteen-section form of Reality Audits (PF23 §1), followed by the dated comparison with PF23's historical observations (§12.3). It records what exists, what differs from the stated comparison frame and what could not be established. Normative compliance, dispositions and owners are in the separate Change Audit Triage; the readiness decision is in the separate QA Readiness record. Neither substitutes for this audit, and this audit makes no readiness decision.

How to read it:

* `E-nnn` is evidence: a path and line, or a command and its result. `N-nnn` is a negative claim; §13 holds each one's pattern, tool, case, scope and zero-hit result.
* `QA10-OBS-nn` is an observation of this audit (§12.1). `H-…` rows compare PF23's observations (§12.3).
* "Local probe" means a read-only run in a throwaway clone of `6a0f55f0` at `/tmp/qa10/clone`, under `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, Python 3.11.17, no package installed. It is not CI, not QA and not governed evidence. After every probe the clone's `git status --porcelain --untracked-files=all` was empty.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `6a0f55f0`; this branch changes nothing there. `git log` shows the last `docs/pfcanon/` change is `4fcb3c76` (HDE Build Notes v13.9.3). Terms searched (`grep -n -i` over `docs/pfcanon/*.md` and `docs/ephemeral/HDE-EPIC041-*`): reality audit, PF23, QA-10, readiness, integrated readiness, historical comparison, drift, chart loader, `engine/charts`, `charts/loader`, SEPA006, purity, governed evidence, required governed evidence, completion standard, doc delta, drainage ordering, open-rails, production-functional.

| Title (file) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| Reality Audits (`PF23-Canon-Reality-Audits-v1.2.3.md`) | Front matter and "Intent & scope"; §1 to §12.3 (the method, the thirteen sections, the coverage table, the observation and historical tables); the §12.4 header and its result legend; §13 header and format; Evidence-list format; Provenance | The audit method and section structure; the historical comparison set and statuses (§12.3). Its "PO-only, at epic closure" intent is the historical actor statement that HDE Governance §9.1.5 and Glow QA Guide §3.1.1 replace for Epic/CRD readiness (scoped override, below) |
| HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`) | §9.1.5 "Integrated readiness, remediation and closure" (whole); §2.0.18 "QA Acceptance Tokens & PF23 scope" including "PF23 consult scope", "Drift assessment trigger", "Drift assessment protocol (stub)" and "PF23 audit observation classification" | QA-10's outputs and readiness table; PF23 observations are dated snapshots; drift stubs (§12.1) |
| Glow QA Guide (`PF19-Canon-Glow-QA-Guide-v3.0.7.md`) | "Reality Audits, readiness and QA acceptance (titles-only)"; §3.1 "Intent" and "Workflow placement"; §3.1.1, §3.1.2, §3.1.3; §3.2 "Checklist" (evidence capture and same-PR Index/Mirror parity) | Output purposes; current facts need current evidence; evidence-indexing posture (§9) |
| Change Process Guide (`PF06-Canon-Change-Process-Guide-v2.5.5.md`) | §2.2 "Audit (the executing agent)", including "Negative or no-hit audit proof" and "Findings → Doc Delta Map"; §3.5.2.8 "Post-QA documentation drainage ordering (normative)" | Negative-proof rule (§13); doc-delta homes and drainage timing (§12.1) |
| HDE Build Checklist — Separation (`PF09.3-…-v1.1.8.md`) | §0.6 "Completion Standard"; Task HDE-SEPA006 and Subtasks .1 to .3 | The comparison frame for §4, §5, §9 to §12 |
| HDE Architecture (`PF02-…-v2.4.7.md`) | §1.1 "Single homes": "Purity rule", "BodyGraph seam carve-out", "Non-BodyGraph chart loader classification [Required-Now]"; the `adapter/` single-home lines | Purity predicate; the canon sentence §12 compares with the removed module |
| HDE Mechanics Guide (`PF14-…-v3.5.9.md`) | §1.1 "BodyGraph and loader seam posture" and its remediation paragraph; line 5697 (HDE-EPIC030 review record) | Remediation predicate; the canon sentences §12 compares |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.3.md`, the current controlled PF10) | Whole file | 2.2 R-1 and R-2 bound what may depend on this record; 2.3 and 2.4 deferred obligations (§12.2); 2.1 not engaged (no vendor, route, evidence-tool or gate surface in the change) |
| HDE State of the Repository (`PF31-Reference-…-v0.1.md`) | §2.2 | Reference context compared in §12 (reference class, not authority) |
| AGENTS.md | Canon-first rule; closed rails; truncation guardrail; QA output placement; "HDE-EPIC041 current posture"; governed-evidence rules | Probe posture; the posture lines compared in §12 |
| In-flight documents (current versions) | Specification v1.1 (whole); review v1.1 (whole, §5 CCR); Implementation Audit v1.0 (whole); Plan v1.1 (whole); Plan review v1.1 (whole) and review v1.0 N-4; every WU-PR-01 to WU-PR-03 instruction, PR plan, final result and lineage review (whole); DOC-20 completion v1.0 (whole) | Comparison frame, approved objectives, delivery lineage |

Scoped override: Reality Audits' intent statement places audits with the Product Owner at epic closure. For Epic/CRD readiness, HDE Governance §9.1.5 and Glow QA Guide §3.1.1 assign the fresh audit and historical comparison to continuing Isis in QA-10; HDE Governance §2.0.18 records that this bounded correction does not harmonize PF23 policy generally. This audit applies the PF23 method and the §9.1.5 actor and timing. Silence: none decisive for this audit.

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Audit Snapshot Metadata

| Field | Value |
| :- | :- |
| Scope | HDE-EPIC041 (EPIC), "Separation Pass 4": PF09.3 Task HDE-SEPA006 and Subtasks .1 to .3, as approved in Specification v1.1 (R-01 to R-04, AC-01 to AC-05) and delivered under Plan v1.1 (WU-PR-01 → WU-PR-02 → WU-PR-03; no Ops unit) |
| Approved lineage | Specification `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md` (blob a41b10b58ce9, 51,861 bytes), approved by `docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md` (CF-E-30 INITIAL_APPROVE, ASK OK); Audit `docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md` (blob 9decb6085a64); Plan `docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md` (blob 2ff65a377ae3, 37,557 bytes), approved by `docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md` (IA-30 INITIAL_APPROVE, ASK OK.) |
| Delivery lineage | WU-PR-01 #791 squash `e72c9bac` (lineage review ACCEPT, blob 20e9d51c481d); WU-PR-02 #796 squash `9843934f` (ACCEPT, blob 2d93a6fd866e); WU-PR-03 #800 squash `634be154` (ACCEPT, blob d48393be1b84); DOC-20 COMPLETE (`docs/ephemeral/HDE-EPIC041-WU-PR-03-documentation-completion-v1.0.md`, blob da78b7a9d260), landed by #802 as `3a3d3f66` |
| Absence states | No Ops task, execution result or receipt (Plan v1.1 §6); no approved amendment; no remediation lineage; no prior readiness, audit or triage record (searched: `git ls-tree -r --name-only HEAD docs/ephemeral` lists 36 HDE-EPIC041 files, none a QA-10 record; Notion search "HDE-EPIC041" returned no QA-10 record) |
| Repository and commit | `amthorn78/glow-hdengine-v2` at `6a0f55f07607ddfea5590ed8ee080764e029b31a` (E-001) |
| Observation | 2026-10-29T03:50Z to 04:06Z |
| Inspection method | A full-history local clone (`/workspace/glow-hdengine-v2`, unshallowed by `git fetch --unshallow`, detached at `origin/main`, working tree clean) for static reads, `git grep`, `git log`, `git diff`, `git show`; a throwaway clone for local probes (header). No dependency was installed: QA-10's boundary forbids it. Probes therefore use only the standard library and the repository's own modules |
| Tools | git 2.43.0; Python 3.11.17 (CI uses 3.12); no pytest |
| Environment | Session shell: `APP_ENV`, `DATABASE_URL`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `ENGINE_ENV`, `SAFE_MODE`, `ALLOW_NETWORK` all UNSET (checked by name). Probes set closed rails explicitly through `env -i` |
| Hosted CI | Not read directly: the unauthenticated GitHub API answered HTTP 403 (rate limit) and no GitHub credential is configured. Hosted results cited here are the ones the accepted lineage reviews recorded |
| Producer and version | Continuing Isis role; this audit v1.0 |

**Coverage.** A section is COMPLETE when every unit of its stated population was read in full. "Carried" means the unit is byte-identical to PF23's pin `0adce9d` (`git diff` empty), so PF23's content-based facts about it still hold and it was not re-read.

| § | Population | Status |
| :- | :- | :- |
| 1 | Pin, tools, environment names, canon identities, lineage files | COMPLETE |
| 2 | All 6,109 tracked entries (root inventory); the complete name-status delta `0adce9d..6a0f55f0` outside the four planning prefixes (47 paths) | COMPLETE |
| 3 | `pyproject.toml`, requirements, `Procfile`, release manifest and admission constants | COMPLETE (all carried: byte-identical to the pin) |
| 4 | The change's Engine population: `engine/charts/pure.py`, the removed `engine/charts/loader.py` (blob 8ea4dce2 read at `b29ca84`), `engine/util/input_validators.py`; the other Engine modules | COMPLETE for the change population; the remaining 100 Engine files carried (no `engine/` path other than `engine/charts/` changed since the pin) |
| 5 | `adapter/chart_orchestration.py`, `adapter/__init__.py`, `adapter/no_io_guard.py`; the three app factories and route registrations | COMPLETE for the change population; factories and routes carried (unchanged) |
| 6 | Emitters and serializers | Carried; the change adds no emitter or public serialization (§6) |
| 7 | `engine/cli/main.py` and the console script | Carried; no CLI surface added (§7) |
| 8 | Provider, vendor, resolver and DB modules | Carried; the change removed one provider-resolution import and added no acquisition (§8) |
| 9 | Index, Mirror, sentinel, path validators, release manifest, change evidence homes, the architecture snapshot, `artifacts/logs/loader_call.jsonl`, `artifacts/compat/*` | COMPLETE, with three validators not runnable here (§9) |
| 10 | The change's tests (five new or migrated files and two migrated loader tests), CI registration, `pytest.ini`, `ci.yml`, the classifier's change surface | COMPLETE for the change population; hosted CI read through recorded evidence only |
| 11 | PF23's 14 flow families plus the change's chart-orchestration flow | COMPLETE (the new flow traced hop by hop; the 14 families classified by file delta) |
| 12 | Observations; every RA-20261026 row of PF23 §12.1.A (32) and every row of PF23 §12.3 (43); the three AGENTS.md drift rows of §12.1.B | COMPLETE for those populations; §12.1.B canon-claim rows and §12.4 item rows not re-compared row by row (bounded in §12.3) |
| 13 | Every N- id in this file | COMPLETE |

**Limitations.**

* No route, database or vendor probe was made. Runtime, deployed and production state are Unknown.
* No dependency was installed, so modules that import `jsonschema`, Flask or psycopg could not be imported locally. Affected: the C-1 generator run (exit 1 `ModuleNotFoundError: jsonschema` instead of its exit 2, E-030), `update_evidence_index.py --check`, `orientation_demo.py --check` and `release_id_recompute.py --check-manifest-only` (E-041). For these, the audit relies on the recorded hosted CI and lineage-review evidence and on byte identity of the code since that evidence was taken (E-031).
* Hosted CI was not read (above). The state of the push run on `6a0f55f0` is Unknown; §10 records what the classifier does on that push when run as `ci.yml` runs it.
* The local Python is 3.11, not CI's 3.12. The probed code uses no 3.12-only feature (`datetime.UTC` exists from 3.11).

## 2. Top-level Repo Map

* E-001 `git rev-parse HEAD` → `6a0f55f07607ddfea5590ed8ee080764e029b31a`; `git rev-parse origin/main` (after `git fetch origin main`, which advanced `3a3d3f6..6a0f55f`) → the same; `git status --porcelain` → empty.
* E-002 Recent `main` history (`git log --format='%h %an %aI %s'`): `6a0f55f0` amthorn78 2026-10-29T02:35:05Z "cline skills" (direct commit; parent `3a3d3f66`); `3a3d3f66` #802 (DOC-20 record); `f56322a0` #801 (WU-PR-03 lineage review); `634be154` #800 (WU-PR-03); `9843934f` #796 (WU-PR-02); `e72c9bac` #791 (WU-PR-01); `e121e354` #792 (close-pack writer correction, HDE Build Notes 2.2); `7983b252` #767 (HDE-CRD-0002 documentation deltas).
* E-003 6,109 tracked entries: 5,972 mode `100644`, 135 `100755`, 2 symlinks `120000`, no gitlinks (`git ls-tree -r HEAD | awk '{print $1}' | sort | uniq -c`). PF23 recorded 8,374 at the pin.
* E-004 41 root directories, tracked files each: `.audit_src/` 485, `.backup_epic004/` 6, `.claude/` 9, `.devcontainer/` 3, `.github/` 3, `.vscode/` 1, `_arch/` 147, `_archive/` 29, `adapter/` 18, `artifacts/` 1026, `audit/` 3196, `catalog/` 25, `ci/` 14, **`cline_skills/` 9 (new)**, `codex/` 37, `config/` 2, `dev/` 2, `docs/` 287, `engine/` 102, `errors/` 10, `fixtures/` 17, `freeze/` 1, `goldens/` 26, `handoff/` 49, `internal/` 5, `math/` 1, `migrations/` 3, `narratives/` 10, `notes/` 21, `parity/` 17, `presenter/` 4, `proofs/` 6, `release/` 1, `reports/` 2, `scan_reports/` 2, `schemas/` 47, `scripts/` 66, `sql/` 1, `tests/` 260, `tools/` 100, `validation/` 2. Against the pin: `adapter/` 17 → 18, `docs/` 2,567 → 287, `tests/` 255 → 260, `cline_skills/` added; every other directory has its pin count.
* E-005 57 root files, the same names PF23 recorded (project documents `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md`; build and run files; the EPIC023 step reports; the scratch and zero-byte files `Run`, `assert`, `import`, `temp_run.*`, `big.json`, `patch.diff`, `manifest_pre.sha256`, `manifest_post.sha256` and others).
* E-006 `docs/` holds 18 directories and 53 root files. By directory: `acceptance` 2, `adr` 5, `architecture` 2, `changes` 2, `contracts` 2, `crd` 3, `design` 8, `ephemeral` 37, `evidence` 9, `graph` 59, `ops` 1, `pfcanon` 34, `plans` 8, `prompt_ecosystem_management` 33, `qa` 2, `run` 6, `schemas` 20, `server` 1. `docs/ephemeral/` holds the 36 HDE-EPIC041 records and `PF10-build-notes-addendum-planning-documents-and-pf-versions-never-inputs-v1.0.md`; commit `de27c356` (2026-10-28, "Archived /docs/ephemeral to Google Drive") deleted the earlier records.
* E-007 Name-status delta `git diff --name-status 0adce9d HEAD` outside `docs/ephemeral/`, `docs/graph/`, `docs/pfcanon/`, `docs/prompt_ecosystem_management/` (47 lines): M `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`; A `adapter/chart_orchestration.py`; M `artifacts/evidence_index.jsonl` and its `.path_proof.txt`, `.sha256`, `.sha256.path_proof.txt`; M `audit/HDE-CRD-0002_MANIFEST.json`, `…_MANIFEST.json.path_proof.txt`, `…_close_candidate_source.json`, `…_close_report.md`, `…_close_report.md.path_proof.txt`; M `ci/checks/classify_ci_changes.py`; A nine `cline_skills/*.skill`; M `docs/ADAPTER_009.md`, `docs/EVIDENCE_INDEX.md`, `docs/INDEX.md`, `docs/adr/hde/close_pack_writer_adr.md`, `docs/contracts/reader_v2_public_bytes.md`; D `engine/charts/loader.py`; A `engine/charts/pure.py`; M `schemas/close_candidate_source.v2.json`, `scripts/make_compat_determinism_artifacts.py`; A `tests/adapter/test_chart_orchestration.py`, `tests/charts/test_chart_loader_import_guard.py`, `tests/charts/test_chart_pure_interface.py`, `tests/charts/test_chart_pure_purity.py`, `tests/scripts/test_make_compat_determinism_artifacts.py`; M `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/loader/test_load_chart_fixture_only.py`, `tests/loader/test_loader_logs_keys_only.py`, `tests/qa/test_generate_epic_close_pack.py`, `tests/retired_tests.md`, `tests/tools/test_prepush_check.py`, `tools/ci/prepush_check.py`, `tools/qa/generate_epic_close_pack.py`. Attribution (`git log 0adce9d..HEAD -- <paths>`): HDE-EPIC041 is #791, #796 and #800; #767 and #792 are HDE-CRD-0002 follow-ups; `6a0f55f0` adds `cline_skills/`.
* E-008 `cline_skills/` holds nine files, each beginning with the ZIP signature `PK\x03\x04` (`git show 6a0f55f:<f> | head -c 4 | od -c`): `change-flow.skill` 538,904 bytes, `flowmaster-validate.skill` 721,634, `glow-graph-contract.skill` 58,987, `glow-hde-pr-development.skill` 26,085, `glow-merged-change-attribution-lock.skill` 65,594, `glow-workspace-currency.skill` 13,536, `glow-write-boundary.skill` 4,199, `session-branch-flowmaster.skill` 13,020, `typesafe-scoring.skill` 15,894.
* E-009 744 tracked `.py` files; `tests/` has 260 tracked files, 220 of them `test_*.py`.
* The change's discovered homes: code `adapter/chart_orchestration.py`, `engine/charts/pure.py`, `scripts/make_compat_determinism_artifacts.py`; tests `tests/charts/`, `tests/adapter/test_chart_orchestration.py`, `tests/loader/test_load_chart_fixture_only.py`, `tests/loader/test_loader_logs_keys_only.py`, `tests/scripts/test_make_compat_determinism_artifacts.py`, `tests/retired_tests.md`; CI `ci/checks/classify_ci_changes.py`; documentation `CHANGELOG.md`, `ARCHITECTURE.md`, `AGENTS.md`; tracked data it touches or must not touch `artifacts/constants/iso_3166_1_alpha2.json`, `artifacts/constants/iana_tz_list.json`, `artifacts/logs/loader_call.jsonl`, `artifacts/compat/*`.

## 3. Packaging and Entrypoints

* E-010 `pyproject.toml`, `requirements.txt`, `requirements-dev.txt` and `Procfile` are byte-identical to the pin (`git diff --quiet 0adce9d HEAD -- <f>`), so PF23's facts hold: one console script, `hdctl = "engine.cli.main:cli"` (PF23 N-12-907), runtime requirements `psycopg[binary]`, `Flask<3.0`, `gunicorn<22`, `jsonschema==4.23.0`, and the `Procfile` gunicorn command on `adapter.factory:create_app()`.
* E-011 Release admission: `catalog/manifest.json` version `1.3.0`, 45 `files`, 5,881 bytes, SHA-256 prefix `77204764c225b645`; no member path contains `chart`, `input_validators` or `make_compat` (json parse). `engine/config/registry_loader.py:398` reads `ADMITTED_RELEASE_VERSION = "1.3.0"`. `git diff --stat b29ca84 HEAD -- catalog/ engine/config/registry_loader.py` is empty, so the change altered no release member or admission constant.
* The change adds no entrypoint: `adapter/chart_orchestration.py` defines no `__main__` block, no Flask app, route or blueprint (N-005), and is imported by no app factory, the CLI, the compat module or the BodyGraph modules (N-004). Its only non-test caller is the C-1 script (E-021).

## 4. Engine Modules

* E-012 `git ls-tree -r HEAD engine/charts/` → `engine/charts/pure.py` only (blob `6b7d10ca559c`, SHA-256 `07b179b4…c744e`, 101 lines). `engine/charts/` has no `__init__.py`; it is a namespace package, as the removed loader's directory was. `engine/__init__.py` is 0 bytes.
* E-013 `engine/charts/pure.py:9-11` imports exactly `re`, `unicodedata` and `typing`. It defines `ChartInputError` (`:16`; `code`, `message`, `details`), `BirthInputs` (`:24`, a NamedTuple), `_parse_date` (`:36`, local calendar arithmetic, comment "without strptime's locale and TZ reads"), `_parse_time` (`:50`), `validate_birth_inputs(birthdate, birthtime, place, tz, *, iso_codes, iana_zones)` (`:61`) and `normalize_chart(obj)` (`:91`). Check order date, time, place, tz presence, tz value (`:71-87`); every refusal is `ChartInputError("READER_INVALID_INPUT", <message>, {"field": <date|time|place|tz>})` (`:32-33`).
* E-014 Local probe of the delivered purity checks (`tests/charts/test_chart_pure_purity.py`, loaded without pytest), 2026-10-29T03:55:58Z: `violations(engine/charts/pure.py) = []`; `test_pure_module_has_no_forbidden_dependency_or_call` PASS; `test_checker_flags_planted_violations` PASS; `test_fresh_import_and_calls_have_no_external_side_effects` PASS (a cold import loads none of `random`, `secrets`, `uuid`, `socket`, `subprocess`, `logging`, `datetime`, `time`, `json`, `pathlib`, `engine.util.input_validators` and others; then import and calls under 31 patched time, randomness, environment, filesystem, logging, socket and subprocess entry points); `test_harness_flags_a_planted_side_effect` PASS; `test_harness_flags_a_planted_operational_import` PASS.
* E-015 The removed loader, read at `b29ca84` (`git show b29ca84:engine/charts/loader.py`, blob `8ea4dce2602d`, 173 lines; SHA-256 of the bytes `7c95be40…9685`): mixed validation (via `engine.util.input_validators`), `SAFE_MODE` read (`:54`), wall clock (`:49`), `perf_counter` (`:95`, `:168`), `ensure_cid` (`:97`), a JSONL append to `artifacts/logs/loader_call.jsonl` relative to the working directory (`:69-73`), a `resolve_provider` import (`:20-23`), `_call_legacy` with the `{"gates": [1, 2, 3]}` fallback (`:76-82`) and the kwargs-form recursion (`:160-164`).
* E-016 `engine/util/input_validators.py` (unchanged since `b29ca84`, E-032): imports `secrets` at module level (`:7`); `_ISO_PATH` and `_IANA_PATH` are relative `Path`s (`:12-13`) read by `parse_place_city_cc` (`:46`) and `parse_tz_iana` (`:54`); `parse_date_yyyy_mm_dd` calls `datetime.strptime` (`:25`); `ensure_cid` (`:60-70`) never raises and synthesizes with `secrets.token_hex(8)`. Its callers outside tests are `adapter/chart_orchestration.py` (for `ensure_cid` only) and `engine/providers/vendor_http_hdapi.py` (Audit O-17; not re-traced).
* E-017 `engine.compat.compute` defines no `compat_public` (N-006); its file is byte-identical to the pin.
* No other `engine/` path changed since the pin (E-007), so PF23's §4 facts about the other Engine modules are carried (§12.3).

## 5. Adapter / HTTP Surfaces

* E-018 `adapter/chart_orchestration.py` (blob `f8163fad5f61`, SHA-256 `9426b91f…4302`, 113 lines). Imports (`:11-21`): `datetime`, `json`, `logging`, `os`, `re`, `time`, `pathlib.Path`, `typing`; `from engine.charts.pure import normalize_chart, validate_birth_inputs`; `from engine.util.input_validators import ensure_cid`. `_ROOT = Path(__file__).resolve().parents[1]` (`:24`) anchors `_ISO_PATH` and `_IANA_PATH` (`:25-26`). `load_chart(*args, **kwargs)` (`:70`): `perf_counter` start (`:78`); `safe_mode = str(_os.getenv("SAFE_MODE", "0")).strip() == "1"` (`:79`); `cid = ensure_cid(kwargs.get("correlation_id"))` (`:80`); routing (`:83-92`): the positional predicate `_birth_args` (`:38-44`), a first positional string not shaped `YYYY-MM-DD` → `TypeError`, the three birth keywords through the same predicate, else `TypeError("Invalid arguments to load_chart")`; validation with the two pinned lists as `frozenset`s (`:93-98`); `normalize_chart(_fixture_chart())` (`:99`); a `finally` block that builds one line with keys `ts, route, provider, source, status, duration_ms, safe_mode, correlation_id` (`:103-112`; `route` `loader.load_chart`, `provider` `fixtures`, `source` `default`) and passes it to `_emit` (`:113`), which calls `log_sink` or the module logger and swallows any exception (`:59-67`).
* E-019 Local probe of the entry (`/tmp/qa10/probe_orch.py`), 2026-10-29T03:56:27Z, with an injected sink unless stated:
  * positional form → the fixture chart, one line, `status` `ok`; canonical bytes `{"authority":"","centers":[],"channels_short":[],"gates":[1,2,3],"meta":{"provider":"fixtures","source":"default"},"profile":"","type":""}` plus LF (`engine.serializer.canon.sercanon`);
  * keyword form with C-1's literals (`1990-05-04`, `14:22`, `Austin, US`, `Europe/Amsterdam`) → the fixture chart, one line;
  * no arguments, `("user-abc",)`, keyword `birthdate="user-abc"`, `("1990-01-01",)`, `(42,)` → each `TypeError: Invalid arguments to load_chart`, one line, `status` `error`;
  * invalid date, time, place, tz absent, tz invalid → `ChartInputError`, `READER_INVALID_INPUT`, `details.field` `date`, `time`, `place`, `tz`, `tz`, messages `invalid date`, `invalid time`, `invalid place`, `tz required on internal path`, `invalid tz`, one line each;
  * the line's keys in order `ts, route, provider, source, status, duration_ms, safe_mode, correlation_id`; values `loader.load_chart`, `fixtures`, `default`, `int`, `True` (under `SAFE_MODE=1`); none of `birthdate`, `birthtime`, `place`, `Amsterdam`, `NL`, `1990-01-01`, `12:34`, `Europe/Amsterdam` in the line once `ts` is removed;
  * an absent correlation id → synthesized, matching `^CID-[a-f0-9]{16}$`;
  * from an empty foreign working directory → the same chart and the same `place` refusal; the directory stayed empty;
  * with no sink → exactly one record on logger `adapter.chart_orchestration`; a raising sink → the call still returns the chart;
  * `NoIoGuard` around three calls → `attempts == 0`;
  * mutating a returned chart leaves the next call's chart unchanged.
* E-020 `adapter/__init__.py` is one comment line, `# adapter package`.
* The three app factories (`adapter/factory.py`, `adapter/http_reader.py`, `adapter/wsgi.py`) and `engine/http/compat_handler.py` are byte-identical to the pin; the route population PF23 recorded is carried. The new module registers no route (N-005) and no factory imports it (N-004).

## 6. Presenter / Emitter

* The change adds no emitter, presenter or public serializer. The entry's only serialization is the keys-only log line (`json.dumps(..., separators=(",", ":"), ensure_ascii=False)`, E-018), an operational log, not a public payload. The returned chart dict is not serialized by the entry; its canonical bytes under `sercanon` are recorded in E-019.
* Every presenter and emitter module PF23 names is byte-identical to the pin (E-007 lists no `presenter/` or `engine/presenter/` path); PF23's §6 facts are carried.

## 7. CLI Surfaces

* `engine/cli/main.py` is byte-identical to the pin; the subcommands `showcompat`, `aux-preview`, `bg:resolve`, `dev:sampler` and the stdout guards PF23 recorded are carried. No CLI file imports the chart entry or the pure module (N-004). The change adds no CLI option.
* The C-1 script is not a console script; it is run as `python scripts/make_compat_determinism_artifacts.py` (§11, F15).

## 8. Vendor Seam & BodyGraph Storage

* The changed boundary performs no vendor or database acquisition. The entry's "acquisition" is the in-process fixture literal `_fixture_chart()` (E-018); it imports no resolver, provider, vendor, HTTP client or DB module (E-018 import list).
* Removing `engine/charts/loader.py` removed its `engine.config.provider_loader.resolve_provider` import and its resolver-unavailable fallback (E-015). `engine/config/provider_loader.py`, `engine/providers/*`, `engine/provider/*`, `engine/bodygraph/*` and `engine/db/*` are unchanged since `b29ca84` (E-032) and since the pin (E-007); PF23's §8 facts are carried.
* No configuration name is read by the entry other than `SAFE_MODE`, and only for the log field (E-018 `:79`). No secret value was inspected by this audit.

## 9. Evidence, Indices, Catalogs

* E-021 Change evidence homes on `main`: `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` each have 0 rows naming `EPIC041` or `epic041` (`grep -c`); `audit/qa/` and `audit/docdeltas/` hold no `hde-epic041` entry (`ls | grep -i 041` → nothing); no `audit/EPIC-041_*` close-pack file exists. The Specification §10 close-pack and doc-delta paths are expected-at-close locations, not existing files.
* E-022 `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` are byte-identical to the pin. `artifacts/evidence_index.jsonl` and its three companions changed only in `e121e354` (#792), the HDE-CRD-0002 close-pack republication (`git log 0adce9d..HEAD -- artifacts/evidence_index.jsonl`).
* E-023 Local validator probes at `6a0f55f0`, 2026-10-29T04:04Z: `tools/evidence/validate_evidence_paths.py` rc 0; `ci/checks/check_mirror_schema.sh` rc 0; `ci/checks/check_evidence_index_hash.sh` rc 0; `tools/evidence/check_lf_endings.py` rc 0; `ci/checks/check_agents_md_citations.py` rc 0 `AGENTS_MD_CITATIONS_OK`; `ci/checks/check_direct_db_contract.py` rc 0 `DIRECT_DB_CONTRACT_OK`.
* E-024 Not runnable here (limitation): `tools/evidence/update_evidence_index.py --check`, `tools/evidence/orientation_demo.py --check` and `scripts/release_id_recompute.py --check-manifest-only` each exit 1 with `ModuleNotFoundError: No module named 'jsonschema'`. This is an environment gap, not a repository result.
* E-025 `tools/evidence/generate_architecture_snapshot.py --check` → rc 1, `STALE:artifacts/architecture/architecture_snapshot.keys_only.json`. The snapshot (last changed `dbd7487d`, 2026-08-02) names `engine/charts/loader.py` once (`grep -c` 1) and names neither `adapter/chart_orchestration.py` nor `engine/charts/pure.py` (`grep -c` 0). Its directory is a classifier historical prefix.
* E-026 `artifacts/logs/loader_call.jsonl` blob `925569528ffc` (the blob the Audit and the WU-PR-02 review recorded), last changed by `c6fdc913` (2026-05-01); no live tracked writer of it remains (N-002).
* E-027 `artifacts/compat/AB.json` and `BA.json` blob `7fe71f996dc6`, `identity_hash.txt` blob `7e6176a2886e`, unchanged since `c6fdc913` and since `b29ca84`.
* E-028 `catalog/manifest.json.path_proof.txt` records `size_bytes: 1981` and `sha256: dbf89997…`; the manifest is 5,881 bytes with SHA-256 `77204764…`; neither the Human Index nor the Mirror names that path proof (`grep -c` 0 and 0). All three are unchanged since the pin (PF23 RA-20261026-10, §12.3).

## 10. Tests, QA Harness, CI/Checks

* E-029 The change's tests at `6a0f55f0`: `tests/charts/test_chart_pure_purity.py` (5 tests), `tests/charts/test_chart_pure_interface.py` (8 cases: 1 + 5 parametrized + 1 + 1), `tests/adapter/test_chart_orchestration.py` (20 cases: the entry's contract, E-019's behaviors as literal assertions), `tests/charts/test_chart_loader_import_guard.py` (4 tests), `tests/scripts/test_make_compat_determinism_artifacts.py` (1 test), and the migrated `tests/loader/test_load_chart_fixture_only.py` (2) and `tests/loader/test_loader_logs_keys_only.py` (1; `ts` pinned to its shape and removed before the substring check, `:51-54`). Retained coverage named by PF09.3 (`tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode`, `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on`) is unchanged.
* E-030 Local probe of the import guard (`tests/charts/test_chart_loader_import_guard.py`, loaded without pytest), 2026-10-29: all four tests PASS; `git ls-files -z -- '*.py' ':(exclude)docs/ephemeral/' ':(exclude)docs/pfcanon/'` lists 744 files, of which 518 are scanned after the classifier's `_HISTORICAL_PREFIXES` (`.audit_src/`, `_archive/`, `_backup_`, `artifacts/architecture/`, `artifacts/epic020/`, `audit/history/`, `audit/historical/`, `audit/ops/`) and the guard's own file are skipped. The C-1 script could not be run locally: exit 1, `ModuleNotFoundError: No module named 'jsonschema'` (limitation).
* E-031 Recorded hosted CI (from the accepted lineage reviews, not re-read): #791 exact head `815fd5b2` run 40723983402 `success`, all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; #796 exact head `8200d1fb` run 40774524113 `success`, all seven lanes; #800 exact head `88d4a311` run 40801978516 `success`, `documentation_only`. Post-merge push runs: 40735776026 on `e72c9bac` `success` (WU-PR-02 instruction §1); 40777435776 on `9843934f` `success` (WU-PR-03 instruction §1); 40802629588 on `634be154` `success` (WU-PR-03 lineage review §3). The generator test, the guard, the purity and orchestration tests ran in those exact-head runs.
* E-032 Byte identity since the accepted code: `git diff --stat 9843934f HEAD -- . ':(exclude)docs/ephemeral' ':(exclude)AGENTS.md' ':(exclude)ARCHITECTURE.md' ':(exclude)CHANGELOG.md' ':(exclude)cline_skills'` lists only HDE Build Notes (v13.9.2 → v13.9.3). `git diff --stat b29ca84 HEAD -- .audit_src _archive _arch handoff artifacts/architecture artifacts/logs/loader_call.jsonl engine/util engine/config/provider_loader.py engine/providers engine/provider` is empty.
* E-033 CI registration (`ci/checks/classify_ci_changes.py:610-623`): `engine/charts/pure.py` → the purity, interface and orchestration tests; `adapter/chart_orchestration.py` → the orchestration tests; `engine/charts/loader.py` → the import guard; `scripts/make_compat_determinism_artifacts.py` → the generator test. Neither `pytest.ini` nor the classifier names the retired characterization file (`grep -c characterization` 0 and 0). `pytest.ini` and `.github/workflows/ci.yml` are byte-identical to the pin.
* E-034 `tests/retired_tests.md:8` is the row for `tests/adapter/test_chart_orchestration_characterization.py` (retired 2026-10-28; replacing coverage `tests/adapter/test_chart_orchestration.py`). `tests/retired_tests.md:58` is byte-identical to line 57 at `b29ca84` (SHA-256 of the line, prefix `f3ada82b4af2863b`, both).
* E-035 Classifier on the current head's push, run as `.github/workflows/ci.yml:65-70` runs it (`BASE_SHA` = `github.event.pull_request.base.sha || github.event.before`): `python3 ci/checks/classify_ci_changes.py --base 3a3d3f66… --head 6a0f55f0… --event-name push …` → exit 2, `CI_CHANGE_CLASSIFIER_ERROR:CI_CHANGE_SURFACE_UNCLASSIFIED:cline_skills/change-flow.skill`. The same error stops `--base b29ca84… --head 6a0f55f0… --event-name pull_request`. The workflow's push `paths` filter includes `'**'` and excludes only the eight `docs/` prefixes (`ci.yml:18-32`), so a push run on `6a0f55f0` starts and reaches that step. Its actual hosted outcome is Unknown (not read).
* The QA harness (`tools/qa/qa_harness.py`, `tools/qa/epic021_qa.py`) is byte-identical to the pin; no HDE-EPIC041 QA has run (E-021). Inspection here is not a claim that any test ran or passed beyond the local probes stated.

## 11. Flows & Call Chains

| # | Flow (PF23 family or new) | Status at `6a0f55f0` | Evidence |
| :- | :- | :- | :- |
| F1 | Reader HTTP v1/v2 and dev `GET /reader` | Present; entry and hop files unchanged since the pin; not touched by the change | E-007; N-004 |
| F2 | Compat HTTP `/api/compat/v1` | Present; unchanged | E-007 |
| F3 | `hdctl showcompat` | Present; unchanged | E-007, §7 |
| F4 | Aux preview | Present; unchanged | E-007 |
| F5 | Dev sampler | Present; unchanged | E-007 |
| F6 | `hdctl bg:resolve` | Present; unchanged | E-007, §8 |
| F7 | Configured-v2 mapped cache | Present; unchanged | E-007 |
| F8 | Evidence update (`tools/evidence/update_evidence_index.py`) | Present; tool unchanged; Mirror bytes changed by #792 only (E-022) | E-022, E-023 |
| F9 | Golden comparison | Present; unchanged | E-007 |
| F10 | Gate readiness | Present; unchanged | E-007 |
| F11 | QA harness recording | Present; unchanged | §10 |
| F12 | Close pack `--write` / `--check` | Present; changed by #792 (HDE-CRD-0002 follow-up; HDE Build Notes 2.2), not by HDE-EPIC041; not re-traced here | E-007 |
| F13 | Release cut and runtime identity | Present; unchanged | E-011 |
| F14 | Every other route, hook, subcommand and launcher | Present; no route registration, hook or launcher changed (the only new `adapter/` file registers none, N-005) | E-007, N-005 |
| F15 (new) | Chart orchestration | Present; traced below | E-018, E-019, E-021 |

**F15 hops.** Callers → entry → pure module, each read in full:

1. C-1 `scripts/make_compat_determinism_artifacts.py:9` `from adapter.chart_orchestration import load_chart`; `main()` (`:14-19`) first resolves `engine.compat.compute.compat_public`, which does not exist (N-006), prints `compat_public not implemented` to stderr and exits 2, before the `load_chart(**a)` calls at `:25`. Its writes (`artifacts/compat/identity_hash.txt`, `:47-48`) are therefore unreachable on `main`.
2. C-2 `tests/loader/test_load_chart_fixture_only.py:4-5` and C-3 `tests/loader/test_loader_logs_keys_only.py:4` call the entry with an injected sink.
3. The new tests call the entry and the pure module directly (E-029).
4. Entry `adapter/chart_orchestration.py::load_chart` → `ensure_cid` (`engine/util/input_validators.py:60`) → pinned-list reads anchored at `_ROOT` (`:31-35`, `:96-97`) → `engine.charts.pure.validate_birth_inputs` (`pure.py:61`) → `normalize_chart` (`pure.py:91`) on `_fixture_chart()` → one log line through `_emit` to the sink or logger. No write to the filesystem occurs on any path (E-019).
5. No production entry reaches F15 (N-004). It is reached only by the C-1 script and tests.

## 12. Drift and Reality vs Expectations

### 12.1 This audit's observations

Each row is an independently verifiable fact with both sides. Status: Aligned, Partial, Drift or Not established. A drift stub follows HDE Governance §2.0.18 (source claim, conflicting repository fact, surface, tentative bucket). An observation is not by itself a defect or a gate; the triage decides each one.

| Id | Observation | Compared with | Status | Evidence | Drift stub |
| :- | :- | :- | :- | :- | :- |
| QA10-OBS-01 | `adapter/chart_orchestration.py` is the one place on the chart path that reads `SAFE_MODE`, both clocks and the correlation id, reads the pinned lists (anchored at the repository root), acquires the fixture chart and emits one keys-only log line; it registers no route and writes no file | Specification R-01/AC-01; Plan v1.1 §5.1, I-2, §5.3; PF09.3 Task "Implementation / integration boundary" | Aligned | E-018, E-019, N-004, N-005 | — |
| QA10-OBS-02 | `engine/charts/pure.py` imports only `re`, `unicodedata` and `typing`; the delivered purity checks pass in a fresh local run, and their negative self-tests fail planted violations | Specification R-02/AC-02; Plan I-1; HDE Architecture §1.1 Purity rule | Aligned | E-013, E-014 | — |
| QA10-OBS-03 | `engine/charts/` holds only `pure.py`; no tracked Python file outside the classifier's historical prefixes and the two planning trees imports `engine.charts.loader` or references `_call_legacy`; the inventory pattern of Plan v1.1 §6 matches 69 files, 25 live and 44 under historical captures, each with a disposition (§12.4); the legacy signature raises `TypeError`; no shim | Specification R-03/AC-03; Plan WU-PR-02 Scope; D-1 | Aligned | E-012, E-019, E-030, N-001, N-003 | — |
| QA10-OBS-04 | Today's entry and the removed loader (blob `8ea4dce2`) return equal results and equal typed-error `code`, `details.field` and message on 13 call shapes (valid and invalid, positional and keyword); `artifacts/compat/*` bytes, `artifacts/logs/loader_call.jsonl` and release membership are unchanged; the fallback is gone; no tracked file changed after the probes | Specification AC-05; Plan I-3, I-4, I-5 | Aligned | E-036, E-011, E-026, E-027, N-002 | — |
| QA10-OBS-05 | The boundary checks of R-04 exist, are registered as owner tests, and passed in each work unit's exact-head hosted CI; AC-04's record fields are in the PR records. No independent QA of HDE-EPIC041 has run | Specification R-04/AC-04, §9 ("Live QA is required for eventual close") | Aligned (implementation); QA owed | E-029, E-031, E-033, E-021 | — |
| QA10-OBS-06 | The C-1 script imports the entry and still exits 2 before its chart call; local reproduction needs the repository's requirements, which this audit may not install | Specification R-03 (generator migrated; behavior preserved); Plan I-4; Audit ED-07 | Aligned (on recorded CI and PR-40 evidence for identical code) | E-030, E-031, E-032, N-006 | — |
| QA10-OBS-07 | No production entry point, CLI path or vendor path reaches the entry or the pure module; the changed boundary performs no vendor or DB acquisition | Specification §4 items 3 and 4 (binding conditions); Audit §6 | Aligned: neither binding condition is met at `6a0f55f0` | N-004, E-018, §8 | — |
| QA10-OBS-08 | HDE Architecture §1.1 says "The checked-in loader remains current repository reality until separately remediated"; the module is removed | HDE Architecture §1.1 vs repository | Drift | E-012, N-003 | Source claim: "The checked-in loader remains current repository reality until separately remediated" (PF02 §1.1) · Conflicting repository fact: `engine/charts/` holds only `pure.py`; the loader was removed by #796 (E-012) · Surface: `engine/charts/`, `adapter/chart_orchestration.py` · bucket (tentative): necessary reality shift |
| QA10-OBS-09 | HDE Mechanics Guide §1.1 says "The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift"; that responsibility now sits in `adapter/chart_orchestration.py` and `engine/charts/pure.py` | HDE Mechanics Guide §1.1 vs repository | Drift | E-012, E-018 | Source claim: "The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift" (PF14 §1.1) · Conflicting repository fact: the module is removed; the responsibility is split between the Adapter entry and the pure module (E-012, E-018) · Surface: chart path · bucket (tentative): necessary reality shift |
| QA10-OBS-10 | HDE State of the Repository §2.2 says the loader "still mixes input normalization with environment inspection, clocks, provider orchestration, and filesystem logging" | PF31 §2.2 (reference) vs repository | Drift | E-012 | Source claim: "The non-BodyGraph loader under `engine/charts/loader.py` still mixes…" (PF31 §2.2) · Conflicting repository fact: removed (E-012) · Surface: `engine/charts/` · bucket (tentative): necessary reality shift |
| QA10-OBS-11 | PF09.3 records Task HDE-SEPA006 and Subtasks .1 to .3 as **Not done**, and its Task notes describe the loader defect as current; the implementation they describe is delivered and accepted, and QA, acceptance and closure have not occurred | PF09.3 vs repository and delivery lineage | Partial (status drainage is post-closure; §0.6 completion predicates not all met) | E-012, E-021, E-031 | — |
| QA10-OBS-12 | No governed evidence family exists for HDE-EPIC041: no Index or Mirror row, no `audit/qa/hde-epic041/`, no doc-delta file, no close pack. The approved Plan planned none for the PR units. PF09.3 requires "required governed evidence … indexed through the existing authorized writer" and lists governed evidence among its §0.6 completion predicates | PF09.3 Task deliverables, Subtask .3, §0.6; Specification §8, §9, §10; Plan §10; review v1.0 N-4 | Not established (owed by the QA and close stages) | E-021 | — |
| QA10-OBS-13 | `6a0f55f0` adds nine `cline_skills/*.skill` ZIP archives at a new root; the classifier, run as `ci.yml` runs it for that push, exits 2 with `CI_CHANGE_SURFACE_UNCLASSIFIED:cline_skills/change-flow.skill`. Not part of HDE-EPIC041 | CI classifier contract vs repository | Drift | E-008, E-035 | Source claim: every changed path must classify (classifier `:1934`, `CI_CHANGE_SURFACE_UNCLASSIFIED`) · Conflicting repository fact: nine `cline_skills/` paths do not (E-035) · Surface: `cline_skills/`, `ci/checks/classify_ci_changes.py` · bucket (tentative): not assigned (outside the change) |
| QA10-OBS-14 | The register binds the GCFPE operating procedure to `docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.1.0-20261027.md`; that path is not on `main` (deleted by `de27c356`). The register states the procedure restates no rule | GCFPE register binding vs repository | Drift (non-decisive) | E-006, N-007 | — |
| QA10-OBS-15 | `engine/compat/compute.py` has no `compat_public`, so the canon-named compat-determinism generator still cannot complete (Audit FND-005) | HDE Governance GATE:CORE-DET, D.1, D.3 (as the Audit cited) vs repository | Drift (persistent; out of scope) | N-006, E-017 | — |
| QA10-OBS-16 | `engine/util/input_validators.py` still reads its pinned lists relative to the working directory and its date parser uses `strptime` (TZ read on first call) for its other caller (Audit FND-006; WU-PR-01 OBS-1) | — (implementation observation) | Persistent; out of scope | E-016 | — |
| QA10-OBS-17 | The architecture snapshot is stale, names the removed loader and names neither new module (Audit FND-007) | HDE Schemas and Artifacts evidence-family currency (as the Audit cited) | Persistent; out of scope | E-025 | — |
| QA10-OBS-18 | `CHANGELOG.md` lines 3-19, `ARCHITECTURE.md` lines 13 and 16 and `AGENTS.md` lines 129-134 describe the delivered boundary; each statement this audit checked matches the code (entry, pure module, removal, `TypeError`, generator exit 2, retired test, unchanged log file, unchanged release) | DOC-20 COMPLETE; WU-PR-03 measures | Aligned | E-012, E-018, E-019, E-026, E-034, N-001 | — |

### 12.2 HDE Build Notes 2.3 and 2.4: deferred obligations at this head

| Item (addendum) | State at `6a0f55f0` | Evidence |
| :- | :- | :- |
| OBS-4, clock-dependent C-3 (2.3) | Resolved by WU-PR-02: `ts` pinned and removed before the substring check | E-029 |
| AUD-CORR-1, "pure" helper statement (2.3) | Resolved in code: `pure.py` imports nothing from `input_validators` | E-013 |
| OBS-1, `parse_date_yyyy_mm_dd` reads TZ (2.3) | Persistent, out of scope (QA10-OBS-16) | E-016 |
| 2.2 bearing on WU-PR-02, WU-PR-03 and CL-05 (2.3, 2.4) | WU-PR-02 and WU-PR-03 conform (guard pathspec exclusions; no planning path or PF version in code or the new text); CL-05 not reached | E-030; QA10-OBS-18 |
| DELTA-001, DELTA-002 (2.4) | Carried as non-mandatory candidates in #800's description; canon unchanged (QA10-OBS-08, -09) | §12.1 |
| SWEEP-1 (2.4) | Holds: the only live documents naming the module are the three that state it is removed | E-007; §12.4 |
| OBS-6, OBS-7, OBS-8 (2.4) | Unchanged repository and environment facts | — |
| FND-005, FND-006, FND-007 (2.4) | Persistent (QA10-OBS-15 to -17) | — |

### 12.3 Historical comparison with PF23 (dated)

**Comparison set.** Every RA-20261026 row of PF23 v1.2.3 §12.1.A (32 rows) and every row of PF23 §12.3 (18 RA and 25 FND ids, 43 rows), plus the three AGENTS.md drift rows of §12.1.B. PF23's pin is `0adce9d` (2026-10-26). **Method.** For each row, the paths in its cited E- and N- evidence were extracted from PF23's Evidence list and §13 and checked against `git diff --no-renames --name-only 0adce9d 6a0f55f0` (script `/tmp/qa10/hist/compare.py`, local scratch; `--no-renames` so that a renamed canon file counts as changed). A row whose cited paths are all byte-identical is **Persistent (carried)**: its content-based fact still holds by identity and was not re-read. A row with a changed path, a hosted or runtime subject, or no path was re-checked directly. Statuses: New, Persistent, Resolved, Changed, Unverifiable.

| PF23 id | PF23 observation (short) | PF23 status | Now | Evidence for the disposition |
| :- | :- | :- | :- | :- |
| RA-20261026-08 | `engine/charts/loader.py` reads `SAFE_MODE`, times calls, imports `resolve_provider`, appends `loader_call.jsonl`, returns `{"gates":[1,2,3]}` on the legacy path | Aligned (with PF31 §2.2) | **Resolved** | E-012; N-003. The module is removed; PF31 §2.2's claim is now drift (QA10-OBS-10) |
| FND-022 | `engine/charts/loader.py` environment reads, timing, provider resolution and file logging | Persistent | **Resolved** | Same as RA-20261026-08 |
| RA-20261026-06 | No hosted run for the audited commit; latest `main` run failed at `1fb4731`; 19 earlier pushes succeeded | Drift | **Changed** | E-031: the post-merge push runs of #791, #796 and #800 succeeded; E-035: the push run on `6a0f55f0` is expected to stop at classification; its hosted outcome Unknown |
| FND-018 | Hosted CI outcomes | Changed | **Changed** | As RA-20261026-06 |
| RA-20261026-10 | `catalog/manifest.json.path_proof.txt` records a different size and digest; not indexed | Drift | Persistent | E-028 (re-checked: the Mirror changed in #792 but still does not name it) |
| RA-20261026-14 | The classifier maps `dev/reader_harness/app.py` to `product`; nothing tracked there | Drift | Persistent | Re-checked: `classify_ci_changes.py:274` still maps it; `git ls-files -- dev/reader_harness` → 0 |
| RA-20261026-15 | `_HISTORICAL_BACKUP_PATHS` omits `scripts/hdctl.clean.py` | Partial | Persistent | Re-checked: `:328` defines the set; `grep -c hdctl.clean` → 0 |
| RA-20261026-32 | `qa_harness.py` roll-ups differ on empty input vs AGENTS.md's "no absent … becomes a PASS" | Partial | Persistent | Re-checked: the AGENTS.md sentence remains (`:48`); `tools/qa/qa_harness.py` unchanged |
| RA-08 | 189 test files not named by a lane or roster; whole-suite failures | Changed | Changed | E-009: `tests/` 260 files, 220 `test_*.py` (PF23: 255 and 215); no suite run here |
| RA-09 | Security review did not cover implementation deltas in four units | Unverifiable | Unverifiable | No new evidence; the HDE-EPIC041 units recorded "security review not required" (lineage reviews §3) |
| RA-10 | Live Gate readiness never observed; open-rails QA step owed | Reserved for QA | Unverifiable | No DB probe allowed (§1) |
| RA-13 | `check_mirror_schema.sh` is Python; AGENTS.md has no bash invocation | Resolved | Persistent (resolved state holds) | Re-checked: AGENTS.md changed but `grep -c -E '(bash\|sh) +ci/checks/check_mirror_schema' AGENTS.md` → 0; E-023 the check runs by path, rc 0 |
| RA-17 | PF10's Addendum Index equals its body and ends with `<eof>` | Resolved | Persistent (resolved state holds) | PF10 v13.9.3: 4 index lines (`^\* 2\.`), 4 body headings (`^## 2\.`), last line `\<eof\>` |
| RA-18 | Canon drainage of C040-05 to -08 pending | Changed | Changed | PF10 v13.9.3 names no `C040` (0 hits); AGENTS.md:140 states C040-06 to -08 are drained; the drained permanent text was not re-verified here |
| FND-009 | Producer/evidence root counts | Changed | Changed | E-004: `docs` 287, `audit` 3196, `tests` 260, `engine` 102, `adapter` 18; new `cline_skills/` |
| FND-016 | Final operative documentation present | Persistent (presence only) | Persistent | `docs/ADAPTER_009.md`, `docs/acceptance/http_transport_evidence.md`, `docs/qa_harness_pattern.md` present; AGENTS.md and `docs/ADAPTER_009.md` changed (#767, #800) |
| FND-017 | `docs/ADAPTER_009.md` retained `body_not_allowed` | Resolved | Persistent (resolved state holds) | Re-checked after #767 changed the file: `grep -c body_not_allowed docs/ADAPTER_009.md` → 0 |
| FND-008 | Exact lowercase root names | Persistent | Persistent | `git ls-tree -d --name-only HEAD \| grep -c '[A-Z]'` → 0 (`cline_skills/` is lowercase) |
| FND-012 | `assert` and `import` are zero-byte tracked files | Persistent | Persistent | `git cat-file -s` → 0 for `assert`, `import`, `Run`, `temp_run.err`, `temp_run.out` |
| FND-019 | Permanent PF19 current-source wording ("A changed, different or unavailable SHA alone must never block progression") | Resolved | Persistent (resolved state holds) | Re-checked: PF19 was renamed v3.0.6 → v3.0.7; the sentence is present once in v3.0.7 (line 4262) |
| FND-020 | `docs/changes/GCFPE_PROMPT_PROVENANCE.md` not found | Persistent | Persistent | N-008 |
| FND-004 | Index and Mirror bind artifacts across several roots | Persistent | Persistent | E-022 (Index unchanged; Mirror republished by #792) |
| P-A-013 (§12.1.B) | Non-PF10 PF documents cite PF10 by section or version | Drift | Persistent | Re-checked: e.g. PF04 v2.8.8 10 lines, PF27 v2.0.6 6, PF19 v3.0.7 4, PF06 v2.5.5 4 match `PF10 (§\|addendum\|v1[0-9])\|PF10-HDE-Build-Notes-v` |
| P-A-094 (§12.1.B) | AGENTS.md says PF10 records an HDE-CRD-0001 plan-wide CI override; PF10 has none | Drift | Persistent | Re-checked: AGENTS.md:111 keeps the sentence; PF10 v13.9.3 has 0 `HDE-CRD-0001` and 0 `plan-wide` |
| P-A-196 (§12.1.B) | AGENTS.md names `unsupported_runtime_nonclaim`; runtime has none | Drift | Persistent | Re-checked: AGENTS.md:185 keeps it; `git grep -l unsupported_runtime_nonclaim HEAD -- engine adapter presenter` → 0 |
| RA-20261026-01 to -05, -07, -09, -11 to -13, -16 to -31 (26 rows) | Engine, Reader, compat, packaging, server-config, runner, admission-docstring, purity-closure, threshold, vendor, sampler, catalog-gate, cache-header, version-schema, orientation-comment observations | Aligned / Partial / Drift as recorded | Persistent (carried) | Every cited path byte-identical to the pin (compare.py: 0 changed paths per row) |
| RA-01 to -07, RA-11, RA-12, RA-14 to -16 (12 rows) | Catalog/roster, Reader, validators, wheel, factories 404, dev gate, showcompat help, bg:resolve LF guard, ci.yml filters, endpoint catalog, serializer hazards, root hygiene | As recorded | Persistent (carried) | Every cited path byte-identical to the pin (0 changed paths per row); `ci.yml` unchanged |
| FND-001 to -003, -005 to -007, -010, -011, -013 to -015, -021, -023 to -025 (15 rows) | Presenter split, compat blueprint, `hdctl`, purity boundaries, vendor transport, direct DB, catalog symlink, Procfile, duplicate ids, helper presence, `compute_core` reach, CRD-0001 root, showcompat stdout, catalog rows | As recorded | Persistent (carried) | Every cited path byte-identical to the pin (0 changed paths per row) |

**Counts.** 78 PF23 rows compared (32 + 43 + 3): Resolved 2 (RA-20261026-08, FND-022); Changed 5 (RA-20261026-06, FND-018, RA-08, RA-18, FND-009); Persistent 69 (16 re-checked directly, 53 carried by byte identity); Unverifiable 2 (RA-09, RA-10). New: QA10-OBS-01 to -18 (18 rows of §12.1), of which -15 to -17 restate Audit findings FND-005 to FND-007 at this head.

**Not re-compared row by row (stated, not dropped).** PF23 §12.1.B's 2,316 canon-claim comparisons (PF02, PF05, PF10, PF12, PF14) were made against canon versions that have since been replaced (PF10 v13.8.6 → v13.9.3; PF02, PF05, PF12, PF14 each revised); re-comparing every canon claim is outside this change's audit scope. The canon sentences that bear on this change are compared in §12.1 (QA10-OBS-08 to -11). PF23 §12.4's 120 rows compare PF23 v1.2.2's items; their subjects are covered by the §12.3 RA/FND rows above and by the file delta (E-007).

### 12.4 Inventory and dispositions (Plan v1.1 §6 search at this head)

Search: `git grep -l -I -E 'engine\.charts|engine/charts|charts\.loader|load_chart\b|loader_call|LoaderInputError|_call_legacy' HEAD -- . ':(exclude)docs/pfcanon' ':(exclude)docs/ephemeral'` → 69 files. Against the WU-PR-02 squash `9843934f` (66 files), the difference is exactly `AGENTS.md`, `ARCHITECTURE.md` and `CHANGELOG.md` (WU-PR-03).

| Members | Disposition |
| :- | :- |
| `adapter/chart_orchestration.py` | The Adapter-owned entry (QA10-OBS-01) |
| `scripts/make_compat_determinism_artifacts.py` | C-1, migrated (QA10-OBS-06) |
| `tests/loader/test_load_chart_fixture_only.py`, `tests/loader/test_loader_logs_keys_only.py` | C-2, C-3, migrated in place |
| `tests/adapter/test_chart_orchestration.py`, `tests/charts/test_chart_pure_interface.py`, `tests/charts/test_chart_pure_purity.py`, `tests/charts/test_chart_loader_import_guard.py` | The change's boundary checks (the guard and purity test hold the module name only as planted or self-test text) |
| `ci/checks/classify_ci_changes.py` | Owner mappings, including the removed path's (E-033) |
| `tests/retired_tests.md` | Rows 8 and 58 (E-034) |
| `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md` | WU-PR-03 text stating the removal and naming the new homes (QA10-OBS-18) |
| `adapter/http_reader.py` | Name collision only (`_safe_load_chart` reads a fixture file; no loader import) |
| `artifacts/logs/loader_call.jsonl` | Tracked historical log; unchanged (E-026) |
| `artifacts/epic004/guards/forbidden_serializers.txt`, `artifacts/math/_manifest_files.txt`, `artifacts/qa/a7_presence.rg.txt`, `artifacts/qa/evidence_presence.rg.txt`, `audit/inventory_epic007.json`, `codex/out/008.evidence_inventory.json`, `manifest_pre.sha256`, `manifest_post.sha256`, `notes/dev-sampler/grep_reader_start_gunicorn.txt`, `notes/dev-sampler/grep_reader_start_http_reader.txt` | Historical captures and inventories naming the loader as text; unchanged |
| 44 files under `.audit_src/`, `_archive/`, `_arch/`, `handoff/`, `artifacts/architecture/` | Historical captures; unchanged (E-032) |

### 12.5 CANON_CONFLICT_REGISTER (CCR-1 to CCR-4 carried unchanged; CCR-5 proposed)

| ID | Classification | Status and reviewer | State at this audit |
| :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION (acceptance map for tokenless work) | APPROVED, Thoth, CF-E-30 review v1.1 (Ruling R-A); confirmed by Isis IA-30 v1.1 | Unchanged; a close-pack matter for CL-05. Drainage: Product Owner |
| CCR-2 | CANON_RECONCILIATION (Business Case content lists) | APPROVED, Thoth, review v1.1 | Unchanged; no effect |
| CCR-3 | CANON_RECONCILIATION (S19 vendor decisions) | APPROVED as conditional, Thoth, review v1.1 | Not triggered at this head (QA10-OBS-07) |
| CCR-4 | CANON_RECONCILIATION (cited Build Notes loader record) | APPROVED, Thoth, review v1.1 | Unchanged; no effect |
| CCR-5 | CANON_RECONCILIATION (when the close pack is written relative to the closure decision: HDE Build Notes §2.2 R-3 against Change Process Guide §3.5.1, Glow QA Guide §3.1.3 and Plan Templates §3B) | PROPOSED by QA-10 in the Change Audit Triage v1.0 (#28; full entry in its §6); not yet reviewed; decision owner Product Owner; meanwhile R-3 governs as written (PF10 precedence) | A canon-text conflict, not a repository observation; bears on CL-05 only |

QA10-OBS-08 to -11 are drift that canon itself anticipated ("until separately remediated"; "not a claim that relocation, caller migration or removal has occurred"), not a conflict between canon and an approved base, and add no entry. HDE Build Notes 2.2 to 2.4 conflict with neither approved base; CCR-5 is a conflict between canon documents.

## 13. Negative-Claim Proof Appendix

Each command ran from the repository root of the local clone at `6a0f55f0`, 2026-10-29.

| Id | Claim | Pattern | Tool | Case | Scope | Result | Zero-hit reading |
| :- | :- | :- | :- | :- | :- | :- | :- |
| N-001 | No tracked Python file outside the classifier's historical prefixes and the two planning trees imports `engine.charts.loader` (any import or dynamic-string form) or references `_call_legacy` | AST forms of `tests/charts/test_chart_loader_import_guard.py::findings` (18 planted forms recognized) | the guard's own `scan`, run without pytest (E-030) | exact | the 518 scanned files of `git ls-files -z -- '*.py' ':(exclude)docs/ephemeral/' ':(exclude)docs/pfcanon/'` minus `_HISTORICAL_PREFIXES` and the guard file | `hits == {}` | 0 findings in 518 files |
| N-002 | No live tracked writer of `loader_call.jsonl` remains | `loader_call` | `git grep -l -I` | sensitive | tracked `*.py *.sh *.yml *.yaml *.toml *.cfg *.ini` | 2 files, both under `.audit_src/` (`.audit_src/engine/charts/loader.py`, `.audit_src/tests/loader/test_loader_logs_keys_only.py`), a historical prefix; across all tracked files outside the historical prefixes and planning trees the 11 matching files are `CHANGELOG.md:15` (states no supported run writes it), inventories and captures, and `tests/retired_tests.md` rows | 0 live code files |
| N-003 | `engine/charts/loader.py` does not exist and is not tracked | exact path | `git ls-tree -r HEAD engine/charts/`; `test -e` (guard test) | exact | `engine/charts/` | only `engine/charts/pure.py` | 0 hits for the loader path |
| N-004 | No production entry point, CLI, compat or BodyGraph module imports the entry or the pure module | `chart_orchestration\|engine\.charts` | `git grep -l -E` | sensitive | `adapter/factory.py adapter/wsgi.py adapter/http_reader.py adapter/app.py engine/cli/ engine/compat/ engine/bodygraph/ Procfile pyproject.toml` at HEAD | `0` files | 0 hits |
| N-005 | The entry registers no route and imports no web framework | `route(\|Blueprint\|register_blueprint\|flask` | `grep -c` | sensitive | `adapter/chart_orchestration.py` | `0` | 0 hits |
| N-006 | `engine/` defines or names no `compat_public` | `compat_public` | `git grep -c HEAD -- engine/` | sensitive | all tracked files under `engine/` | 0 files with a match | 0 hits |
| N-007 | The GCFPE operating procedure v5.1.0 is not tracked on `main` | `Operating-Procedure` | `git ls-tree -r --name-only HEAD \| grep -i` | insensitive | whole index | matches only `docs/prompt_ecosystem_management/operating-procedures/…` (other documents); the v5.1.0 path is absent; `git log -1 -- <path>` → `de27c356` | 0 hits for the bound path |
| N-008 | `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is not tracked | exact path | `git ls-files -- <path> \| wc -l` | exact | exact path | `0` | 0 hits |
| N-009 | Neither `pytest.ini` nor the classifier names the retired characterization file | `characterization` | `grep -c` | sensitive | `pytest.ini`, `ci/checks/classify_ci_changes.py` | `0`, `0` | 0 hits |
| N-010 | No release member is a chart, validator or generator path | `chart\|input_validators\|make_compat` in `files[].path` | `python3` json parse | sensitive | `catalog/manifest.json` (45 entries) | `[]` | 0 hits |

## Evidence added by local probe

* E-036 Independent re-characterization (`/tmp/qa10/probe_char.py`), 2026-10-29T03:56:56Z: the removed loader loaded from `git show b29ca84:engine/charts/loader.py` (written outside the checkout to `/tmp/qa10/oldloader/old_chart_loader.py`, SHA-256 `7c95be40…9685`), its log write redirected to a temporary directory by replacing its `_Path`, run with the clone root as working directory, against today's `adapter.chart_orchestration.load_chart` with a discarding sink, on 13 shapes: the four valid ones (positional; C-1's two keyword inputs; another positional), five invalid fields, a fourth positional argument, a keyword-form invalid place, no arguments and date-only. Result: `shapes 13 differences 0` (typed errors compared by `code`, `details`, `message`; class names differ by design: `LoaderInputError` → `ChartInputError`). The old loader wrote 16 lines to the temporary log for 13 calls: its three keyword-form calls each wrote two (Audit O-07), which the entry does not reproduce (one line per call, E-019).

## Nonclaims

This audit records repository facts. It is not QA, a QA verdict, readiness, acceptance, Ops, deployment, release, PF09 or board movement, a canon change, a PF10 addendum, PF23 publication or closure. Local probes are observations, not CI, QA or governed evidence. It edits no approved artifact and no file outside `docs/ephemeral/`. Merging it preserves the record and approves nothing (D21-C).
