---
artifact_type: PR_INSTRUCTION
artifact_version: "1.0"
logical_id: HDE-EPIC041-WU-PR-03-PR-INSTRUCTION
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-03-pr-instruction-v1.0.md
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-03
DOCUMENTATION_UNIT_ID: WU-PR-03
work_unit_title: "WU-PR-03 — Final repository documentation (GCF-19)"
state: INSTRUCTION_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
producer: the whole-change Implementation Agent for HDE-EPIC041 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj)
prompt: DOC-10 — Create Final Repository Documentation PR Instructions — 102726.1 (https://app.notion.com/p/4064590a05eb81b3a8b5dad3b0c20ed1; page state 2026-10-27T13:19:44.974Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1
SPECIFICATION_REF: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md, CF-E-30 INITIAL_APPROVE)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; corrected by AUD-CORR-1 in the WU-PR-01 lineage review §10)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1; blob 2ff65a377ae392396b32707313399fab3bf154e9)
PLAN_REVIEW_REF: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE)
DEPENDENCY_REFS:
  - docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-lineage-review-v1.0.md (PR-40 ACCEPT of WU-PR-01, amthorn78/glow-hdengine-v2#791, squash e72c9bac; review landed by #793)
  - docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-lineage-review-v1.0.md (PR-40 ACCEPT of WU-PR-02, amthorn78/glow-hdengine-v2#796, squash 9843934f; review landed by #797 as e29a0ade)
DELIVERY_LINEAGE:
  - WU-PR-01: instruction docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-instruction-v1.0.md; plan docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0.md; results v1.0 to v1.5 (final docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-result-v1.5.md)
  - WU-PR-02: instruction docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-instruction-v1.0.md; plan docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0.md; results v1.0 and v1.1 (final docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-result-v1.1.md)
ops_lineage: none (Plan v1.1 §6 declares no Ops unit)
prior_instruction_lineage: none (first instruction for WU-PR-03)
immutable_approved_bases: Specification v1.1 (Thoth); Implementation Plan v1.1 (Isis)
pf10_path: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.3.md (741 lines, 102,755 bytes, sha256 6fa054b1e51cf76fd795e460cec039a51caf99cec16fe1521f0a00febff15f3c; landed on main by 4fcb3c76; read for this instruction as the v13.9.2 text read in full earlier plus the 4fcb3c76 diff read line by line, which adds only addendum 2.4 and its index line; addenda 2.2, 2.3 and 2.4 read in full; provenance, not a gate)
pf10_addenda_applicable: "HDE Build Notes addendum 2.2 (R-1 and R-2 bound what the documentation may cite; R-3 is not engaged); addendum 2.3 (WU-PR-01 record; its 2.2 bearing names WU-PR-03); addendum 2.4 (WU-PR-02 record; its deferred-obligations table names DELTA-001, DELTA-002, SWEEP-1 and the 2.2 bearing for this unit). Addendum 2.1 (S19) is not engaged"
effective_baseline: "approved base + applicable PF10 overlays (addenda 2.2, 2.3 and 2.4 for their scope)"
repository_baseline: origin/main 4fcb3c760ec79d4fadd5cab7f35cde420c265218 (code and repository documentation identical to 9843934f, the WU-PR-02 squash; e29a0ade and 4fcb3c76 change only docs/ephemeral/ and docs/pfcanon/)
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner assigns the dedicated WU-PR-03 PR session at launch)
return_owner: the whole-change IA for HDE-EPIC041, through PR-40 lineage review and then DOC-20 completion verification; rescope through RS-20
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9)
authored_at: 2026-10-28 (UTC)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-DOC10-WU-PR-03-20261028
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    work_unit: WU-PR-03 (documentation of R-01 to R-04 as delivered; AC-01 to AC-05 recorded, not re-proved)
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: DOC-10 — 102726.1 (https://app.notion.com/p/4064590a05eb81b3a8b5dad3b0c20ed1), revision as of 2026-10-27T13:19:44.974Z
    role_stage: whole-change IA / GCF-19 (final repository documentation instruction)
    captured_at: 2026-10-28
    runtime_identity: https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj
    inherited_usage: HDE-EPIC041-PR40-WU-PR-02-20261028
    repository_persistence: PENDING (no docs/changes/GCFPE_PROMPT_PROVENANCE.md; owner GCFPE management; non-gating)
---

# HDE-EPIC041 WU-PR-03 — Final repository documentation PR instruction v1.0 (DOC-10): INSTRUCTION_READY

**State: INSTRUCTION_READY.** This is the one final repository-documentation PR instruction for HDE-EPIC041. It authorizes nothing: only the Product Owner's `PR Implementation Proceed` (PR-30) for an exact PR-20 plan version authorizes implementation, and only the Product Owner merges.

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` `4fcb3c76`. This branch changes nothing under `docs/pfcanon/`. Terms searched: final repository documentation, documentation unit, DOC-10, DOC-20, GCF-19, CHANGELOG, README, AGENTS.md, docs sweep, Doc-Delta, doc delta candidate, drift note, copy/paste command, planning document, PF version, chart loader, `engine/charts`, HDE-SEPA006.

| Title (file) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.3.md`, the current controlled PF10) | v13.9.2 read in full earlier for this Epic; the `4fcb3c76` diff (v13.9.2 → v13.9.3) read line by line: it adds addendum 2.4 and its index line, nothing else. Addenda 2.2, 2.3 and 2.4 read in full | §3.5 (R-1, R-2 citation rules); §3.4 and §12 (2.4's deferred obligations: DELTA-001, DELTA-002, SWEEP-1, the 2.2 bearing); 2.1 not engaged |
| Change Process Guide (`PF06-…-v2.5.5.md`) | §3.5.3 "Repo docs sweep (major epics)" in full; the docs-only rules before and after "Copy/paste command safety (docs-only and discovery PRs)", including "Repo-doc and docs-only changes must be evidence-backed", "Additional docs-only constraints", "Interactive-terminal safety", the CI-traceable command rules and "Decision-bounded placement"; §3.5.2.8 "Live QA via harness", its paragraph "Post-QA documentation drainage ordering (normative)" | §3.3 sweep scope and claim grounding; §3.5 command safety, evidence-type distinction, docs-only scope validation; §6 checks; §12 OBS-D1 (close-PR sweep timing) |
| HDE Governance (`PF04-…-v2.8.8.md`) | §9.1.4 "QA/Ops execution sources and substantive currentness"; §9.1.5 "Integrated readiness, remediation and closure" (QA-10 follows final repository-documentation completion); §9.2 "What requires a Doc-Delta"; §9.3 opening (Change Log entries are for normative changes); the planning-artifact rules on documentation drainage, "Doc deltas capture" notes and canon drift ("Plans MAY include a 'Doc deltas capture'…", "Coding agents and implementation agents MAY NOT directly modify PF-Canon…"); §9.7.7 business case and stop rule | §2; §3.4 (Doc-Delta candidates are non-mandatory, carried as drift notes, never a gate); §3.5 (no canon edit); §7; §10 lane |
| HDE Architecture (`PF02-…-v2.4.7.md`) | §1.1 "Single homes", "Non-BodyGraph chart loader classification" | §3.4 DELTA-001 target |
| HDE Mechanics Guide (`PF14-…-v3.5.9.md`) | §1.1 "BodyGraph and loader seam posture" and the remediation paragraph | §3.4 DELTA-002 target |
| HDE Build Checklist — Separation (`PF09.3-…-v1.1.8.md`) | Task HDE-SEPA006; Subtasks .1 to .3 | §3.1 (what was delivered, by subtask); §3.5 no PF09 movement claim |
| HDE CRD Records (`PF30.1-…-v0.9.2.md`) | The HDE-CRD-0002 record's "Phase blocks" section, including its paragraph on WU-DOC-01 | §10: a final documentation unit has its own lineage review and completion verification |
| Specification v1.1, Implementation Audit v1.0, Plan v1.1 and review v1.1 (in-flight) | Spec §5 (R-01 to R-04, AC-01 to AC-05), §10 (doc-delta surfaces), §11 TI-03; Audit O-20, §9 (DELTA-001, DELTA-002); Plan §6 WU-PR-03 (business case, scope, dependencies, acceptance), §8 DL-03, §10; review v1.1 business-case row for WU-PR-03 | §2 to §7 |
| WU-PR-01 and WU-PR-02 lineage reviews, instructions, plans and final results (in-flight) | Whole documents | §1; §3.1 delivered facts |
| DOC-10 and PR-40 prompts (Notion) | Whole pages | Procedure, required inputs, lane, result routing |

The search found no canon that forbids a pre-QA final documentation pass or that requires this unit to write a Doc-Delta file. Change Process Guide §3.5.3 adds a separate close-PR sweep for major Epics; §12 OBS-D1 records how this instruction treats it.

## 1. Selection and dependency evidence

* **Unit.** WU-PR-03, "Final repository documentation (GCF-19)", Plan v1.1 §6. It is the last unit in the Plan's order WU-PR-01 → WU-PR-02 → WU-PR-03. The Plan declares no Ops unit.
* **Dependency: "WU-PR-02 merged and accepted."**
  * #796 merged 2026-10-28T22:06:58Z as squash `9843934f`; accepted by the WU-PR-02 lineage review (landed by #797 as `e29a0ade`).
  * #791 merged as `e72c9bac`; accepted by the WU-PR-01 lineage review.
  * The post-merge `main` push run on `9843934f` (run 40777435776) concluded `success` at 22:19:37Z. The WU-PR-02 review recorded it as in progress; this is its final state.
* **Delivered state read, not assumed.** The code at `4fcb3c76` was read for §3.1: `adapter/chart_orchestration.py`, `engine/charts/pure.py`, `git ls-tree engine/charts/`, the guard and generator tests, `scripts/make_compat_determinism_artifacts.py`, `tests/retired_tests.md`.
* **No prior WU-PR-03 instruction exists.** No remediation lineage applies.

## 2. Business case (as Plan v1.1 states it)

* **Beneficiary:** the delivery team and the QA lane.
* **Evidence:**
  * HDE-EPIC040's QA Step-0B doc-delta record (`audit/docdeltas/hde-epic040_doc_deltas.md`, DD-05, DD-10, DD-11) found repository documentation that contradicted code, and QA had to carry it as caveats.
  * O-11 shows canon-named tooling that had silently stopped working for five weeks.
* **Benefit:** QA-10 and later sessions read a repository record that matches the delivered boundary, so they do not plan against a removed module.
* **Measure:**
  * A `CHANGELOG.md` "Unreleased — HDE-EPIC041" section names WU-PR-01 and WU-PR-02 and their nonclaims (O-20 convention).
  * A `git grep` sweep at the PR head finds no live repository document outside `docs/pfcanon/`, `docs/ephemeral/` and the historical prefixes describing `engine/charts/loader.py` as current.
* **Stop rule** (HDE Governance §9.7.7): "A work unit whose business case is met stops; further work on it needs a new business case."

The second measure already holds at the baseline (SWEEP-1, §3.3). The PR must keep it holding and record the search at its head.

## 3. Documentation obligations

### 3.1 Delivered state the documentation describes (observed at `4fcb3c76`)

Each fact is observed in the merged code, not taken from a PR description. PR-20 re-reads each one before it is written into a document.

| ID | Fact | Source (repository) | Unit and PR |
| :- | :- | :- | :- |
| F-1 | `adapter/chart_orchestration.py::load_chart` is the chart entry. Two call forms: `load_chart(birthdate, birthtime, place, *, tz=None, correlation_id=None, log_sink=None)` and `load_chart(*, birthdate, birthtime, place, tz=None, correlation_id=None, log_sink=None)`. Any other shape raises `TypeError("Invalid arguments to load_chart")` | The function and its docstring | WU-PR-01, #791 |
| F-2 | The entry owns the `SAFE_MODE` read for the log field, both clocks, the correlation id (`ensure_cid`), the pinned ISO-3166 and IANA list reads anchored at the repository root, the fixture chart, and one keys-only log line per call (`ts`, `route`, `provider`, `source`, `status`, `duration_ms`, `safe_mode`, `correlation_id`; `route` is `loader.load_chart`, `provider` is `fixtures`). The line goes to `log_sink` when given, otherwise to a module logger. It registers no route and writes no file | Module docstring; `_emit`; the `finally` block | WU-PR-01, #791 |
| F-3 | `engine/charts/pure.py` holds `validate_birth_inputs(birthdate, birthtime, place, tz, *, iso_codes, iana_zones)`, `normalize_chart(obj)` and `ChartInputError` (`code`, `message`, `details`; code `READER_INVALID_INPUT`, `details.field` one of `date`, `time`, `place`, `tz`). It does no time, randomness, environment, network, provider, logging or filesystem access, at import or in a call | Module docstring and definitions; `tests/charts/test_chart_pure_purity.py` | WU-PR-01, #791 |
| F-4 | `engine/charts/loader.py` is removed, with its legacy `load_chart(user_id)` signature, `_call_legacy`, its `resolve_provider` import and its resolver-unavailable fallback. No shim. `engine/charts/` holds only `pure.py` | `git ls-tree origin/main engine/charts/` | WU-PR-02, #796 (Product Owner decision D-1) |
| F-5 | `tests/charts/test_chart_loader_import_guard.py` fails if any tracked Python file outside the classifier's historical prefixes, `docs/ephemeral/` and `docs/pfcanon/` imports `engine.charts.loader` or references `_call_legacy`, or if the module path exists | The test | WU-PR-02, #796 |
| F-6 | `scripts/make_compat_determinism_artifacts.py` imports `adapter.chart_orchestration.load_chart`. It still exits 2 with `compat_public not implemented` before its chart call and writes nothing; `tests/scripts/test_make_compat_determinism_artifacts.py` pins that. Its compat computation is not restored (FND-005) | The script and its test | WU-PR-02, #796 |
| F-7 | No supported run of the chart path writes `artifacts/logs/loader_call.jsonl`. The tracked file is unchanged history | F-2, F-4; the file's blob is unchanged | WU-PR-01 and WU-PR-02 |
| F-8 | `tests/adapter/test_chart_orchestration_characterization.py` is retired, with a `tests/retired_tests.md` row naming its replacing coverage | `tests/retired_tests.md` | WU-PR-02, #796 |
| F-9 | No release member, route, flag, CLI option, schema, governed evidence family or public byte changed. Admission stays `1.3.0`, 45 members, `release_id` `77204764…` | The lineage reviews; `prepush_check.py membership` | WU-PR-01, WU-PR-02 |

### 3.2 Required change: the CHANGELOG section

* Insert one section at the top of `CHANGELOG.md`, directly below `# CHANGELOG`, in the file's convention (Audit O-20; the HDE-CRD-0002 and HDE-EPIC040 sections are the pattern): a heading line `Unreleased — HDE-EPIC041: …(final repository documentation, WU-PR-03)`, then `### Added` and `### Changed / Fixed`.
* It names WU-PR-01 (#791) and WU-PR-02 (#796) and what each delivered, from F-1 to F-9 only.
* It states the one intended failure-behavior change: argument shapes the legacy signature took now raise `TypeError` (D-1).
* It states what is not delivered: the generator's compat computation (FND-005), the `input_validators` working-directory and `TZ` reads (FND-006) and the stale architecture snapshot (FND-007).
* It ends with the nonclaims: no QA verdict, acceptance, Ops, deployment, release change, PF09 or board movement, canon drainage or closure.
* It names this documentation pass's own changed files, as the HDE-CRD-0002 section does.
* No earlier CHANGELOG section is edited. Older sections are history.

### 3.3 Sweep: scope, result at the baseline, and the candidates PR-20 decides

* **Scope.** `README.md`, `AGENTS.md`, `ARCHITECTURE.md` and every non-canon file under `docs/` (Change Process Guide §3.5.3 lists README, CHANGELOG, AGENTS and non-pfcanon `docs/**`). Excluded: `docs/pfcanon/`, `docs/ephemeral/`, the classifier's historical prefixes and `_HISTORICAL_PATHS`, governed evidence and close packs (written only by their canonical tools), and frozen captures under `artifacts/` and `audit/`.
* **Search (the measure).** `git grep -n -I -E 'engine\.charts|engine/charts|charts\.loader|load_chart\b|loader_call|LoaderInputError|_call_legacy|chart_orchestration|make_compat_determinism_artifacts' <head> -- <scope>`, with a disposition per match. **At `4fcb3c76` it finds no file in scope.** The matches outside scope are frozen captures and inventories (H-3), `tests/retired_tests.md` rows (history) and two HDE-CRD-0002 close-pack records that name HDE-SEPA006 as a deferred decision: `audit/HDE-CRD-0002_close_report.md` and `audit/docdeltas/hde-crd-0002_drain_targets.md`. Those two are governed close-mutation-set outputs of a closed change and must not be edited.
* **Candidates (statements in scope that the delivered boundary makes incomplete).** None describes the loader. PR-20 decides each one, with its basis, and drafts the exact text if it decides to change it:

  | ID | Statement at `4fcb3c76` | Why it is a candidate | Decision rule |
  | :- | :- | :- | :- |
  | C-A | `ARCHITECTURE.md` "Single homes (authoritative)": `adapter/` is "dev runner & route registration (the only app home)"; the `engine/` list names no chart module. The file says it "is kept in sync at the end of every epic" | `adapter/` now also holds the non-HTTP chart orchestration entry (F-1, F-2), and the pure chart module is a new Engine home (F-3) | Change it if a reader would otherwise place chart operational concerns in `engine/` or miss the entry. Add only F-1 to F-4 facts. Do not touch "Architecture capture (every epic)", which is a close-time obligation (§12) |
  | C-B | `docs/INDEX.md` heading "HD Engine Repo Docs — Index (HDE-EPIC040 current)" and its per-Epic orientation sections | Each recent Epic added an orientation section; HDE-CRD-0002 did not change the heading | Change it only if the PR-20 plan shows the heading would mislead a reader about current state. If changed, add a short HDE-EPIC041 orientation pointing to the CHANGELOG section and the delivered paths, with no claim beyond F-1 to F-9 |
  | C-C | `AGENTS.md`: no HDE-EPIC041 posture section | Plan v1.1 §6: "An AGENTS.md posture line for HDE-EPIC041 is added only if the per-PR plan shows a reader needs it, under the Doc agents rule" | Add one only if an agent would otherwise act wrongly: for example, by restoring a loader, writing chart I/O in `engine/`, or treating the generator as working. It must pass `ci/checks/check_agents_md_citations.py` (no PF document other than PF10, and PF10 by title only) |

  Any other stale statement PR-20 finds in scope is handled by the same rule, and recorded.

* **Scope interpretation (IN-1).** Plan v1.1 §6 lists "README.md, AGENTS.md or non-canon docs/". `ARCHITECTURE.md` is the same kind of top-level non-canon repository document, and Change Process Guide §3.5.3 covers top-level non-canonical repo docs. Including it serves the Plan's stated benefit and changes no Epic-level commitment, so it is not a material change as DOC-10 defines one. The same rule applies to it: only a statement made stale or incomplete by the delivered boundary is changed.

### 3.4 Doc-Delta candidates (non-mandatory; carried in the PR description)

* **DELTA-001.** HDE Architecture §1.1, "Non-BodyGraph chart loader classification": "The checked-in loader remains current repository reality until separately remediated". The loader is removed (F-4).
* **DELTA-002.** HDE Mechanics Guide §1.1, "BodyGraph and loader seam posture": "The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift". The responsibility now sits in `adapter/chart_orchestration.py` (F-1, F-2).
* **Treatment.**
  * Carry both in the PR description as drift notes / Doc-Delta candidates, as HDE Governance requires of an implementing agent that finds canon drift. They are not written to any canon file, to `audit/docdeltas/` or to any governed surface.
  * They are non-mandatory. Their presence or absence is not an acceptance condition, a measure or a gate (HDE Governance, planning-artifact rules; Change Process Guide §3.5.2.8, "Post-QA documentation drainage ordering").
  * Drainage is the canon owner's work after QA.
  * The Doc-Delta surfaces declared in Specification §10 (`audit/docdeltas/hde-epic041_doc_deltas.md`, `audit/qa/hde-epic041/00_meta/doc_deltas.md`) belong to QA Step-0B. This unit does not create them.
* **Not a normative change.** WU-PR-03 changes no math, public contract, emitter, schema, transport, rails, security or logging rule. HDE Governance §9.2 requires no Doc-Delta for it, and §9.3's Change Log is not touched.

### 3.5 Rules for every sentence this unit writes

* **Ground each claim.** Every command, path, module, function, flag, environment variable, token or behavior named must be verified against the repository at the PR head, PF10 or PF-Canon (Change Process Guide §3.5.3; "Repo-doc and docs-only changes must be evidence-backed"). The PR-20 plan records the proof for each non-obvious claim: a repo path and line, a test, or "Not verified", which is then not written as fact.
* **Distinguish evidence types.** Do not present PR-slice results, local checks or lineage reviews as QA, Live QA, close-pack evidence, canon drainage or closure (Change Process Guide §3.5.3).
* **Commands.** Add a command block only if it is needed. Each one is run as written, is CI-traceable, does not close the operator's shell and is not epic-specific by default (Change Process Guide, "Copy/paste command safety").
* **Planning documents and canon versions** (HDE Build Notes addendum 2.2, R-1 and R-2):
  * a document may cite a `docs/ephemeral/` record only as a prose reference, and nothing may depend on it;
  * prefer citing the merged PRs (#791, #796) and repository paths;
  * cite PF-Canon by title and section, never by file name, version or digest;
  * cite HDE Build Notes by title alone, with no addendum number.
* **AGENTS.md** names no PF document other than PF10, and PF10 by title only (the CI step "Check AGENTS.md cites no project documents").
* **No canon edit** and no edit to governed evidence, close packs, acceptance maps, Index/Mirror rows, path proofs or frozen captures.
* **No code, test, schema, CI or configuration change.** If the sweep finds a code defect, it is recorded for its owner, not fixed here.

## 4. Requirement-to-documentation map

| Approved requirement / criterion | Attributable delivered evidence | Documentation change | Validation | Owner |
| :- | :- | :- | :- | :- |
| R-01 / AC-01: one Adapter-owned orchestration entry | F-1, F-2; #791; WU-PR-01 review §4; WU-PR-02 review §4 (I-2) | CHANGELOG "Added" (the entry and what it owns); C-A if changed | Each statement checked against `adapter/chart_orchestration.py` at the head | PR-30 writes; PR-35 corrects; PR-40 reviews |
| R-02 / AC-02: pure Engine chart interface | F-3; #791; WU-PR-01 review §4 (I-1, F-1 fix) | CHANGELOG "Added" (the pure module and its interface); C-A if changed | Checked against `engine/charts/pure.py` | As above |
| R-03 / AC-03: callers migrated; legacy path removed | F-4, F-6, F-8; #796; WU-PR-02 review §4 | CHANGELOG "Changed / Fixed" (removal, D-1 `TypeError` behavior, generator import, retired test) | `git ls-tree` of `engine/charts/`; the script's import line | As above |
| R-04 / AC-04: automated boundary checks; reconciliation | F-5; the purity and orchestration tests; WU-PR-02 review §4 (reconciliation) | CHANGELOG names the guard and the purity tests as what now catches a regression | The test files exist at the head | As above |
| AC-05: outputs preserved, no fallback, clean tree | F-6, F-7, F-9 | CHANGELOG states that outputs, public bytes and release membership are unchanged and the fallback is gone | `prepush_check.py membership`; compat blobs unchanged | As above |
| Plan v1.1 WU-PR-03 measure 2; Spec TI-03 ("documentation-referenced commands") | SWEEP-1: no in-scope document names the loader or the generator | The sweep record in the PR description, with the search, its head SHA and the disposition per match | §6 item 3 | PR-30; PR-40 re-runs it |
| Addendum 2.4 deferred obligations (DELTA-001, DELTA-002, SWEEP-1, 2.2 bearing) | §3.3, §3.4, §3.5 | PR description notes; citation rules | PR-40 | PR-30 |

Not documented by this unit, because nothing in scope describes it: public routes, CLI options, configuration keys, environment variables, migrations, operations and security behavior. None changed (F-9). HDE-EPIC041 has no Ops unit and no external setup.

## 5. Repository baseline, bounded files and exclusions

* **Baseline.** `main` `4fcb3c76`. Outside `docs/ephemeral/` and `docs/pfcanon/` it equals `9843934f`.
* **Must change:** `CHANGELOG.md` (§3.2).
* **May change, only under §3.3's decision rule:** `ARCHITECTURE.md`, `docs/INDEX.md`, `AGENTS.md`, and any other in-scope statement the sweep finds stale.
* **Must not change:**
  * any code, test, script, schema, workflow, CI check or classifier file;
  * `pytest.ini`, `catalog/`, `engine/config/registry_loader.py`;
  * `docs/pfcanon/` and every other CI-exempt planning prefix except this unit's own records under `docs/ephemeral/`;
  * `audit/`, `artifacts/`, `docs/evidence/`, `docs/ENDPOINTS_CATALOG.json` and every governed or frozen artifact;
  * `tests/retired_tests.md`;
  * earlier CHANGELOG sections.
* **Exclusions:** FND-005 to FND-007 (owners: the CL-40 scan and the Product Owner); canon drainage; the Doc-Delta surfaces of Specification §10 (QA Step-0B); the close pack, the close-PR sweep and the architecture capture (CL-05, §12 OBS-D1); QA-10.

## 6. Validation and evidence obligations

All local checks run under closed rails through `env -i` (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`), on the commit to be published. Each is read-only.

1. **Docs-only scope.** `git diff --name-status <base>..HEAD` lists only the files §5 permits (Change Process Guide: docs-only scope validation proves code, tests, schemas, generated evidence, governed indices and PF-Canon were not changed).
2. **Classifier, as `ci.yml` calls it.** `python3 ci/checks/classify_ci_changes.py --base <base SHA> --head <head SHA> --event-name pull_request --github-output <tmp> --changed-tests-output <tmp>` → exit 0. Expected: `reason=documentation_only`, no lanes, because `CHANGELOG.md`, `README.md`, `AGENTS.md`, `ARCHITECTURE.md` and `*.md` map to no lane. Record the actual output.
3. **Sweep at the head.** §3.3's search and scope, with a disposition per match → no in-scope document describes `engine/charts/loader.py` as current.
4. **AGENTS.md citations.** `python3 ci/checks/check_agents_md_citations.py` → `AGENTS_MD_CITATIONS_OK`, exit 0.
5. **Direct-DB contract scan.** `python ci/checks/check_direct_db_contract.py` → `DIRECT_DB_CONTRACT_OK`, exit 0. It scans active repository prose, and the `db` lane that runs it is not selected for a documentation-only change.
6. **Membership and HDE Build Notes.** `python tools/ci/prepush_check.py --path <each changed path> membership build-notes` → every path `not-member`, PASS.
7. **Claim grounding.** For each new or changed sentence, the plan's proof note (§3.5) is checked against the head.
8. **Commands.** Each command block added is run as written, from a clean shell, and its result recorded. If none is added, say so.
9. **Clean tree.** `git status --porcelain --untracked-files=all` is empty after the checks.

**Hosted CI.** The `test` job runs on the PR because its paths are outside the workflow's excluded prefixes. It must be green on the exact head: classification `documentation_only`, the AGENTS.md citation step, and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. No CI waiver exists for HDE-EPIC041.

**AC-04-style record in the PR description ("Checks run").** Commands, configuration, tested-source SHA, results, actor, UTC time window and limitations. A docs-only PR states which claims were verified by a run and which by diff and code reading (Change Process Guide, "Additional docs-only constraints").

**Governed evidence.** None. No path in scope is an Index or Mirror member, a release member or a governed family.

## 7. Acceptance

* The business-case measure (§2) holds at the PR head and is recorded.
* §6 items 1 to 9 pass, and exact-head hosted CI is green.
* Every statement written traces to F-1 to F-9, the PR refs or a cited canon title (§3.5).
* PR-40 lineage review after Nathan's merge, then DOC-20 completion verification. ACCEPT and COMPLETE are their decisions, not this instruction's.

## 8. Environment, CI and access facts

* CPython 3.12 with CI's install is enough for items 2, 5 and 6. Items 1, 3, 4 and 9 need only `git` and `python3`.
* The container exports credentials; use `env -i`. The clone may be shallow; fetch full history before diffing (WU-PR-01 OBS-2, OBS-5).
* `tools/ci/prepush_check.py` resolves the current HDE Build Notes by identity at run time; on `4fcb3c76` that is the v13.9.3 file. Do not pin that name in any document (R-2).
* No open rails, vendor, Railway, database, deployment or Notion writes.

## 9. Security, privacy and recovery

* **Security and privacy.** Documentation must not include secrets, credential values, base URLs, tokens or a birth input. Environment probes are recorded as SET/UNSET. Nothing here changes a guard or a route.
* **Recovery.** Revert the PR. An interrupted PR-30 resumes from its last saved record. A repairable defect in this instruction returns to DOC-10 in the IA session. A material change, as DOC-10 defines it, goes to one `RESCOPE_REQUEST` from the PR author through RS-10 to RS-20, with the exact `PR_RETURN_PHASE`.

## 10. Ownership, lane and merge

* **Lane:**
  * PR-20 plans in the dedicated WU-PR-03 session, ending `ASK OK? — PR IMPLEMENTATION PLAN`;
  * the Product Owner's Proceed for that exact plan version;
  * PR-30 implements, runs §6 and publishes one PR;
  * PR-35 runs review and CI convergence in its own dedicated session and returns `MERGE_PENDING`;
  * Nathan merges manually;
  * PR-40 runs the read-only lineage review, entered on `MERGE_OBSERVED` or, only where none was returned for that merge, on Nathan's merge assertion;
  * DOC-20 verifies documentation completion.
* **Then QA-10.** QA-10 follows DOC-20, under HDE Governance §9.1.5: QA-10 follows "accepted PR/Ops delivery and final repository-documentation completion".
* **Reviews.** The Codex code review runs on the PR. Under the repository instructions it excludes Markdown, so a change made only of Markdown files may have no files in its scope. Findings, if any, are handled by PR-35 under the Change Process Guide's real-input rule.
* **Merges.** No agent merges or enables automatic merge.

## 11. CANON_CONFLICT_REGISTER (carried)

| ID | Classification | Status and reviewer | Treatment in WU-PR-03 |
| :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION (acceptance map for tokenless work) | APPROVED, Thoth, CF-E-30 review v1.1 (Ruling R-A); confirmed by Isis IA-30 v1.1 | None; a close-pack matter for CL-05. Drainage: Product Owner |
| CCR-2 | CANON_RECONCILIATION (Business Case content lists) | APPROVED, Thoth, review v1.1 | None |
| CCR-3 | CANON_RECONCILIATION (S19 vendor decisions) | APPROVED as conditional, Thoth, review v1.1 | Not triggered: no vendor, route, evidence tool or gate row |
| CCR-4 | CANON_RECONCILIATION (cited Build Notes loader record) | APPROVED, Thoth, review v1.1 | None |

No new entry. The canon search found no conflict for this unit's scope. OBS-D1 (§12) records two timing rules that apply at different stages; both can be met, so it is not a conflict.

## 12. Carried items, not-produced artifacts and owners

| ID | Item | Owner and use |
| :- | :- | :- |
| OBS-D1 | Change Process Guide §3.5.3 puts a repo docs sweep for major Epics in the close PR, beside the close pack. HDE Governance §9.1.5 and Plan v1.1 (GCF-19) put final repository documentation before QA-10. WU-PR-03 is the pre-QA pass. It does not claim to be, or to replace, any close-PR sweep. `ARCHITECTURE.md` "Architecture capture (every epic)" is also a close-time step | CL-05 decides at close whether §3.5.3 applies and what remains |
| DELTA-001, DELTA-002 | §3.4 | Canon owner after QA; this unit carries them as candidates |
| SWEEP-1 | §3.3: no in-scope document names the loader at `4fcb3c76` | PR-30 records the search at its head |
| FND-005, FND-006, FND-007 | The generator's compat repair; `input_validators` CWD and `TZ` reads; the stale architecture snapshot | CL-40 scan and the Product Owner |
| OBS-6, OBS-7, OBS-8 | `scripts/scratch.py` holds Markdown; classifier error order; `ruby` path | As the WU-PR-02 review records |
| Review v1.0 N-4 | Carried from Plan review | QA-10 |
| TI-07 / CCR-1; TI-02; Candidate CRD Items 9 and 10 | As the Plan records | Product Owner; CL-05 |
| Not produced | PR-20 plan, Proceed, PR, CI result, PR-35, PR-40 and DOC-20 records | Their owners, in the lane order |
| Usage persistence | Pending (front matter) | GCFPE management |

## 13. Real inputs of each component

| Component | Real inputs | Outside the real set |
| :- | :- | :- |
| `CHANGELOG.md` section | F-1 to F-9 at the PR head; the merged PR numbers | A planning document as a dependency (R-1); a PF file name or version (R-2) |
| Sweep record | The tracked files in scope at the PR head | Untracked or generated files; frozen captures (named, not edited) |
| Candidate edits C-A to C-C | The current text of each file and F-1 to F-9 | Claims about later units, QA, release or closure |
| PR description notes | §3.4 text; the checks of §6 | Canon edits; governed-surface writes |

## 14. TypeSafe reading and surface advice for PR-20 (WU-PR-03)

* **Method.**
  * Installed TypeSafe scoring skill, request v8.2.
  * Script run once, session kind `authoring`, label "HDE-EPIC041 PR-20 WU-PR-03 per-PR plan".
  * No Notion row written: this is an executing-flow session, and DOC-10 writes only under `docs/ephemeral/`.
* **Action sent (v8.2).** "Create a new detailed per-PR implementation plan for the third and last PR work unit of an approved Epic, a documentation-only unit, from one new documentation PR instruction of about 25 KB: add one CHANGELOG section naming the two delivered units, their merged pull requests and their nonclaims; decide, with a stated basis, whether each of three candidate statements in top-level and docs/ repository documentation needs an update to match a delivered boundary (one removed Python module, one new orchestration entry, one pure module), and draft the exact text; ground every claim in the merged code; carry two non-mandatory Doc-Delta candidate notes for the PR description; and record the CI classification (documentation only) and the read-only checks to run. A written prompt with steps exists; the planning session changes no repository code, and no tests beyond read-only checks run and no live run against a provider occurs. The Product Owner's Proceed, implementation, independent PR review, a lineage review and a documentation-completion verification follow later in separate sessions."
* **Reading, as printed.** **TypeSafe v8.2: Sonnet 5.5 at high.** Effort score 1.86 (confidence 0.87); rung probabilities low 0.01, medium 0.15, high 0.82, extra high 0.02, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.48, Sonnet 5.5 0.52, Haiku 5.5 0.00 (confidence 0.36). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.005, Opus 5.5 at medium 0.072, Opus 5.5 at high 0.394, Opus 5.5 at extra high 0.010, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.005, Sonnet 5.5 at medium 0.078, Sonnet 5.5 at high 0.426, Sonnet 5.5 at extra high 0.010, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T23:53:57Z. Nathan picks the cell.
* **Flags.** "model near tie between Sonnet 5.5 and Opus 5.5", as printed.
* **Detail.** Not retained. This session displayed only the reading's first lines, and the script was not re-run, because the skill allows one run.
* **Picks.** Nathan has stated no pick for PR-20 (WU-PR-03) and none for this DOC-10 session (its reading is the WU-PR-02 lineage review §13). None is recorded.
* **Surface advice (PR-20, WU-PR-03).**
  * Run it in a new dedicated top-level Claude Code cloud session for the WU-PR-03 PR role on `amthorn78/glow-hdengine-v2`, started after this instruction's pull request merges. The same session then receives PR-30 after Nathan's Proceed. PR-35 runs in its own session.
  * Read access is needed to `main`: this instruction and its referenced artifacts; `docs/pfcanon/`; the delivered code of §3.1; and the documentation homes in §3.3.
  * A local closed-rails Python 3.12 environment with CI's install, run through `env -i` on a full-history clone, is needed for the classifier, citation, contract and pre-push checks.
  * Write access is needed to one branch and one pull request under `docs/ephemeral/` for the plan.
  * Not needed: code or test changes, open rails, or vendor, Railway, database or Notion writes.

## 15. Nonclaims

This instruction is not Product Owner implementation approval. It is not a PR-20 plan, Proceed, implementation, CI result, QA, Ops, acceptance, PF09 or board movement, canon change, PF10 addendum or closure. It does not decide C-A to C-C; PR-20 does, under §3.3. Nothing outside `docs/ephemeral/` is changed by its pull request. Merging it preserves the record and approves nothing (D21-C).
