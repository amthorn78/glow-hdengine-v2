---
artifact_type: IMPLEMENTATION_PLAN
artifact_version: "1.1"
logical_id: HDE-EPIC041-IMPLEMENTATION-PLAN
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
state: PLAN_PENDING_REVISED
approval_sentinel: ASK OK?
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
author: whole-change Implementation Agent for HDE-EPIC041 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj)
reviewer: the continuing Isis role, at IA-30 — Review Whole-Change Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81ebb110fb0202874d8c); session to be chosen by the receiving side
prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81a5a137f6912fba26b9; page state 2026-10-27T13:16:58.421Z, read in full); v1.0 was formed under IA-10 — Create Whole-Change Implementation Audit and Plan — 102726.1 (https://app.notion.com/p/4064590a05eb813281cbc25f2f30db13)
authoring_mode: PREAPPROVAL_PLAN_REVISION
r1_row: GCF-12 (this revision of the GCF-10 Plan)
supersedes: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.0.md (v1.0, PLAN_PENDING, denied; preserved unchanged)
review_ref: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.0.md (IA-30 INITIAL_DENY, redlines RL-1 to RL-8; merged by amthorn78/glow-hdengine-v2#786 as 81d6124f)
application_report: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1-application-report.md
ecosystem_release: GCFPE-20261027.1 / 102726.1
approved_specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; git blob a41b10b58ce9ff26b7999ce33eca5787e9800b28)
thoth_decision: docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md (CF-E-30 INITIAL_APPROVE; review v1.0 Rulings R-A to R-C in force)
implementation_audit: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE)
pf10_resolved: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.md (read in full)
pf10_addenda_applicable: NONE
base_and_overlays: "approved base (Specification v1.1) + applicable PF10 overlays (NONE)"
product_owner_decisions: D-1 = retire the legacy signature (Nathan / Product Owner, 2026-10-28, Audit §8.1 Q-01)
repository_head_planned_against: origin/main b29ca84a5c134fe7f54fd21cba955b0dab64c0ea (v1.0); origin/main 81d6124f (v1.1; canon byte-identical, `git diff --stat b29ca84 81d6124f -- docs/pfcanon/` empty)
authored_at: 2026-10-28 (UTC; v1.0 and v1.1)
---

# HDE-EPIC041 — Whole-Change Implementation Plan v1.1 (GCF-10, revised under GCF-12)

Format: Plan Templates §12 "General Implementation Plan (Template)". No more specific Plan Templates template controls a change-wide Implementation Plan. Process sequencing comes from Change Process Guide §3 and the selected 102726.1 Change Flow.

This is the pending revised Plan v1.1: the complete replacement of the denied v1.0, applying Isis's IA-30 review v1.0 redlines RL-1 to RL-8 (application report: `docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1-application-report.md`). It is pending and unapproved. It performs no work. It authorizes no PR, Proceed, Ops, QA, PF09 movement or closure. Merging it preserves the record and approves nothing (D21-C).

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Plan identity and revision

* **Plan identity:** HDE-EPIC041-IMPLEMENTATION-PLAN.
* **Plan type:** General Implementation Plan (change-wide).
* **Revision:** 1.1, the pre-approval revision of v1.0 (IA-30 review v1.0, INITIAL_DENY).
* **Date (UTC):** 2026-10-28.
* **Prepared by:** the whole-change IA for HDE-EPIC041.
* **Applicable identity:** Epic HDE-EPIC041; PF09.3 Task HDE-SEPA006 and Subtasks .1 to .3.

## 2. Purpose, scope, exclusions and nonclaims

* **Purpose.** Deliver Specification v1.1 R-01 to R-04 and AC-01 to AC-05.
  * Chart acquisition orchestration moves to one Adapter-owned entry.
  * Engine keeps only pure chart validation and normalization.
  * Every supported caller is migrated.
  * The legacy signature and the mixed module are retired, under D-1.
  * The boundary is proved by automated checks.
* **In scope.** Exactly HDE-SEPA006 and .1 to .3, as the Specification states them.
* **Out of scope.** The non-goals in Specification §2.1, and everything in §2.2:
  * no scoring algorithm;
  * no Magic10 delivery;
  * no new provider contract;
  * no fallback data;
  * no Engine I/O carve-out;
  * no production operation, and no live vendor or production database activity;
  * no provenance helper.

  Also out of scope:
  * restoring the compat-determinism generator's computation (Audit FND-005);
  * `engine/util/input_validators.py` for its other caller (FND-006);
  * the stale architecture snapshot (FND-007);
  * Candidate CRD Items List items 9 and 10.
* **Current implementation claims.** Only what the Audit observed on `main` `b29ca84`.
* **Nonclaims.** No implementation, CI result, Ops, QA verdict, acceptance, deployment, release, PF09 movement, board change, canon change or closure.

## 3. Governing-source map

| Topic | Source title | Locator | Constraint on this Plan |
| :- | :- | :- | :- |
| Scope, sequencing, owners | HDE Build Checklist — Separation | Task HDE-SEPA006; Subtasks .1 to .3 | .1 before .2; verification developed with both; .3 reconciles |
| Ownership and purity | HDE Architecture | §1.1 "Single homes": Purity rule; Non-BodyGraph chart loader classification; `adapter/` | Engine module pure; operational concerns Adapter-owned |
| Remediation posture | HDE Mechanics Guide | §1.1 "BodyGraph and loader seam posture" and the paragraph that follows | Migrate active callers including the generator; preserve canonical outputs; no fallback, no Engine I/O exception, no second resolver |
| Business cases | HDE Governance; Plan Templates | §9.7.7 "Business case for every requirement and work unit"; §2 "Requirement and work-unit business case" | One per work unit (§6); IA-30 checks them; PR-10 carries them |
| Change authority | HDE Governance | §9.1.1 | Same IA; Isis reviews; Proceed per PR plan |
| Plan and audit process | Change Process Guide | §2.2; §3; §0 PR-route Doc-Delta rule | PR includes code, Doc-Delta notes and governed companions where triggered |
| Evidence writers | HDE Schemas and Artifacts | Evidence Index single homes | Any governed artifact goes through `tools/evidence/update_evidence_index.py` |
| Build Notes | HDE Build Notes | (title only) | Silent on this change; the S19 decisions do not apply (Audit §1.3) |
| Repository rules | AGENTS.md | Closed rails; pytest readiness; pre-push check; QA output placement; Doc agents | Each PR session follows them |

## 4. Observed repository reality and validated loci

* **Pinned identity.** `main` `b29ca84`. Each per-PR plan re-verifies at its own base.
* **Validated existing loci** (Audit §3, §5):
  * `engine/charts/loader.py`;
  * `scripts/make_compat_determinism_artifacts.py`;
  * `tests/loader/test_load_chart_fixture_only.py`;
  * `tests/loader/test_loader_logs_keys_only.py`;
  * `pytest.ini`;
  * `ci/checks/classify_ci_changes.py`;
  * `artifacts/logs/loader_call.jsonl`;
  * `artifacts/compat/AB.json`, `BA.json`, `identity_hash.txt`;
  * `tests/core/test_engine_core_purity.py` (the pattern to follow);
  * `adapter/no_io_guard.py`;
  * `engine/util/input_validators.py`.
* **New loci.** Unknown pending per-PR planning: one Adapter module under `adapter/`, one pure module under `engine/charts/`, and their tests. Their names are fixed by the per-PR plan (PR-20), not here.
* **Observed state.**
  * The supported path acquires nothing; it returns a fixed fixture literal (O-03).
  * The legacy path is broken (O-04).
  * The validators read files relative to CWD (O-06).
  * The generator exits 2 before the load (O-11).
  * No CI owner mapping exists (O-13).
  * No production reach (O-09, O-10).
* **Unknown or not-found posture.** Bounded by the Audit's §5.2 search scope. Each PR re-runs that search at its head.

## 5. Architecture, invariants, interfaces and data shapes

### 5.1 Target boundary

```text
caller (script C-1, tests C-2/C-3)
  -> Adapter chart orchestration entry          [adapter/, non-HTTP, not a release member]
       reads: SAFE_MODE (log field only), wall clock, perf clock
       owns : correlation id (ensure_cid), pinned-list file reads (repository-root anchored),
              fixture-chart acquisition, keys-only log line to an injectable sink
       calls: Engine pure chart interface
  -> Engine pure chart interface                [engine/charts/, pure]
       validate(birth inputs, iso_codes, iana_zones) -> validated request | typed error
       normalize_chart(dict) -> dict
```

### 5.2 Invariants

* **I-1.** The Engine chart module reads no time, randomness, environment, network, provider, logging or filesystem state, and writes none, at import or in any call; importing it has no side effect (R-02, AC-02). It may reuse the pure helpers `parse_date_yyyy_mm_dd` and `parse_time_hh_mm` of `engine.util.input_validators` (Audit §4, R-02), and calls no other function of that module. `_load_list`, `parse_place_city_cc`, `parse_tz_iana` and `ensure_cid` read files or randomness. The AST deny-list checks the module's own imports and calls. The fresh-interpreter test patches the time, randomness, environment, filesystem and socket entry points, and proves that none is reached at import or during validation and normalization.
* **I-2.** The orchestration entry is the only place where the R-01 concerns occur for chart loading (AC-01).
* **I-3.** No vendor or DB acquisition, provider contract, fallback data, route, flag, CLI option or release-member change is introduced (Specification §2.1, §4; Audit ED-10). Adding any of them stops the work unit and returns it to this IA through rescope.
* **I-4.** Governed caller output and failure behavior are preserved (R-03, AC-05):
  * the fixture chart dict is byte-identical in canonical serialization;
  * error `code`, `details.field` and message keep today's values for every shape today's supported path accepts; the legacy-routed shapes of §5.3 raise `TypeError`, the one intended change;
  * C-1 exits 2 with `compat_public not implemented` and writes nothing;
  * `artifacts/compat/*` bytes are unchanged.
* **I-5.** Running any covering test leaves `git status --porcelain` empty (AC-05).
* **I-6.** Historical captures under `.audit_src/`, `_archive/`, `_arch/`, `handoff/` and `artifacts/architecture/` are unchanged. So are `artifacts/logs/loader_call.jsonl` and `tests/retired_tests.md` row 57 (R-03; Audit ED-04, ED-09).

### 5.3 Interfaces

These are the shapes. The per-PR plan fixes names and paths.

* **Orchestration entry.**
  * Signature: `load_chart(*args, **kwargs) -> dict`. `tz`, `correlation_id` and `log_sink` are read from the keyword arguments only, as today; a positional argument after the third is ignored, as today.
  * It accepts exactly the two call forms today's supported path accepts, with today's routing:
    * positional: at least three positional strings, the first matching `^\d{4}-\d{2}-\d{2}$` and the second matching `^\d{2}:\d{2}$`;
    * keyword: `birthdate`, `birthtime` and `place` keywords, with optional `tz`, routed as the positional form (the form C-1 uses).
  * Every other argument shape raises `TypeError("Invalid arguments to load_chart")`. That includes the shapes today's code routes to the legacy signature: a first positional string not shaped `YYYY-MM-DD`, and a keyword-form `birthdate` not so shaped. Today those raise `AttributeError` or return fallback data. D-1 retires that path, so this is the one intended change of failure behavior (I-4). The WU-PR-02 PR records it.
  * It emits exactly one keys-only log line per call, on success and on error.
  * The line's keys and values are `ts`, `route`, `provider`, `source`, `status`, `duration_ms`, `safe_mode` and `correlation_id`, with `route="loader.load_chart"`, `provider="fixtures"` and `source="default"`.
  * `log_sink` is a callable that takes the line. If it is `None`, the line goes to a module `logging` logger. The entry never writes a file by default (Audit ED-04).
  * A failing sink never breaks the call, as today.
* **Pure interface.**
  * A validation function takes the four birth fields plus explicit `iso_codes` and `iana_zones` collections. It returns the validated values or raises the typed error.
  * The typed error keeps `code`, `message` and `details`. Its values are `READER_INVALID_INPUT`, the field (`date`, `time`, `place` or `tz`) and today's messages (`invalid date`, `invalid time`, `invalid place`, `tz required on internal path`, `invalid tz`).
  * `normalize_chart(obj)` keeps today's gates normalization.
* **Data shape.** The fixture chart is the O-03 literal, unchanged.

## 6. Work units

No Ops work unit exists. The Specification §6 declares none and the Audit found no external action. The work units run strictly in the order WU-PR-01 → WU-PR-02 → WU-PR-03.

### WU-PR-01 — Adapter orchestration entry and pure Engine chart interface (HDE-SEPA006.1; interface part of .3)

* **Business case.**
  * *Beneficiary:* the delivery team.
  * *Evidence:*
    * O-08: committed runs appended to the tracked `artifacts/logs/loader_call.jsonl` three times (`39a5a33a`, `f3e1f9a1` "HDE-EPIC030 QA PASS 1", `c6fdc913` "HDE-EPIC030 QA PASS 2").
    * O-06 / X-3: chart validation misreports a valid place as invalid when run outside the repository root.
    * E-4 / O-02 locate the concerns.
  * *Benefit:* chart validation exists as deterministic data-in/data-out code that tests can run from any CWD without touching the repository, and logging and file reads have one Adapter owner that writes no file by default. This work unit adds the interfaces and changes no caller, so on its own it does not stop a run of today's loader from writing the tracked file. That benefit is realized when WU-PR-02 migrates the callers and removes the loader.
  * *Measure:*
    * The AC-02 purity and import-side-effect tests pass, and their negative self-test fails a planted violation.
    * The orchestration tests pass with an injected sink, from a temporary CWD, with zero socket attempts.
    * `git status --porcelain` is empty after the run.
* **Scope.**
  * Add the pure Engine chart module and the Adapter orchestration entry of §5.
  * Add their tests.
  * Add owner-test mappings for both new modules in `ci/checks/classify_ci_changes.py`, and register the new tests where CI selection requires it (`pytest.ini` `testpaths` and the classifier roster, as the per-PR plan determines).
  * Do not change `engine/charts/loader.py` or any caller.
* **Tests and evidence.**
  * AST deny-list and fresh-interpreter side-effect tests for the pure module, after `tests/core/test_engine_core_purity.py`, with a negative self-test.
  * Orchestration tests:
    * `SAFE_MODE` set to `1`, to `0` and unset → the `safe_mode` field;
    * a valid correlation id passed through; an absent or invalid one synthesized, matching `^CID-[a-f0-9]{16}$`;
    * keys-only content, with no input value in the line;
    * each invalid field → `READER_INVALID_INPUT` and that field;
    * `tz` absent → field `tz`;
    * a bad argument shape, including each legacy-routed shape of §5.3 and a call with no arguments → `TypeError`;
    * one line per call, on success and on error;
    * a raising sink does not break the call;
    * `NoIoGuard` attempts equal 0;
    * a run from a temporary CWD validates the same as a run from the root.
    * the fixture chart dict of O-03, and each `code`, `details.field` and message of §5.3, asserted as literal values, so they stay asserted after WU-PR-02 removes the old module.
  * A characterization test, in a test file of its own, proving that the new entry and today's `engine/charts/loader.load_chart` return equal results, and equal error `code`, `details.field` and message values, on the same inputs, for every call shape today's supported path accepts (§5.3), valid and invalid. It runs from the repository root, which today's validators need (O-06), with today's loader's log write redirected to a temporary directory by patching `engine.charts.loader._Path`, as C-2 and C-3 do today, so `git status --porcelain` stays empty (I-5). The old module still exists in this work unit, so this proves I-4 before removal.
* **Dependencies.** None. It is first.
* **Owners.**
  * Nathan creates the dedicated PR-30 session and runs PR Implementation Proceed against its per-PR plan.
  * The PR-30 and PR-35 phase sessions deliver under `glow-hde-pr-development`.
  * Nathan merges.
  * PR-40 accepts the landed lineage.
* **Acceptance and evidence.**
  * AC-01 (entry exists and owns the concerns).
  * AC-02.
  * AC-04 (interface-level checks, with commands, configuration, tested-source SHA, results, actor, time and limitations in the PR record).
  * AC-05 (output equality; tracked files unchanged).
  * Exact-head hosted CI `test` green. No CI waiver exists for HDE-EPIC041; a red result caused outside this change is handled under RK-06 and is not green.
* **Environment.**
  * Local closed rails per AGENTS.md: the pytest readiness install, then `python tools/ci/prepush_check.py lanes build-notes` and `--path <path> membership` for each changed path.
  * Hosted CI `test` job.
  * No open rails, vendor, DB, Railway or production access.
* **Recovery and rollback.**
  * The change is additive and nothing imports the new modules yet, so reverting the PR restores `main`.
  * Interrupted work resumes in the same work unit (RS-40 or PR-30 recovery).
  * An out-of-scope need is returned to this IA as a `RESCOPE_REQUEST` (RS-20).

### WU-PR-02 — Caller migration, legacy retirement and boundary reconciliation (HDE-SEPA006.2; reconciliation part of .3)

* **Business case.**
  * *Beneficiary:* the delivery team.
  * *Evidence:*
    * E-1 / O-04 / X-2: the legacy signature fails for every resolvable provider and carries fallback data.
    * E-3: its only caller was retired to hide the defect, not fix it.
    * O-05: a legacy call writes `artifacts/provider/decision.txt`.
    * O-11: the canon-named generator still imports the mixed module on every run.
  * *Benefit:* the broken path is closed rather than hidden, and no supported caller depends on Engine code with operational side effects. A regression that re-introduces an importer fails CI rather than surfacing later the way E-2 did.
  * *Measure:*
    * `engine/charts/loader.py` is absent.
    * The repository-wide import guard passes and fails on a planted importer.
    * C-1 still exits 2 with its stderr from a temporary CWD and writes nothing.
    * `artifacts/compat/*` bytes are unchanged.
    * The retained-coverage tests named in PF09.3 pass.
    * `git status --porcelain` is empty after the covering tests.
* **Scope.**
  * Migrate C-1, C-2 and C-3 (Audit §5.1) to the WU-PR-01 interfaces:
    * C-1: only its import and chart call change (Audit ED-07);
    * C-2 and C-3: they drop the `_Path` monkeypatch and use the injected sink and the pure interface.
  * Remove `engine/charts/loader.py`, including the legacy signature, `_call_legacy`, the `resolve_provider` import and the fallback (D-1; Audit ED-06). No shim is kept.
  * Delete WU-PR-01's characterization test file in the same commit as `engine/charts/loader.py`. Record its removal as a new row in `tests/retired_tests.md` (reason: it compared the new entry with the removed module; replacing coverage: the WU-PR-01 orchestration tests that assert the literal values). Remove it from `pytest.ini` `testpaths` and the classifier roster where WU-PR-01 registered it. Row 57 is unchanged (I-6).
  * Update `pytest.ini` `testpaths` and the classifier roster for any renamed or moved test.
  * Add owner mappings for `scripts/make_compat_determinism_artifacts.py` and for any changed product path that lacks one (O-13).
  * Re-run the inventory search at the PR head and record its result in the PR. Scope: all tracked files except `docs/pfcanon/` and `docs/ephemeral/`. Pattern: `engine\.charts|engine/charts|charts\.loader|load_chart\b|loader_call|LoaderInputError|_call_legacy` (Audit §5.2).
* **Tests and evidence.**
  * A repository-wide guard test:
    * no tracked Python file outside the classifier's historical prefixes imports `engine.charts.loader` or references `_call_legacy`;
    * the module path does not exist;
    * a negative self-test on a synthetic source.
    * the guard excludes only its own source file and the synthetic source of its negative self-test.
  * A generator behavior test: run C-1 in a temporary CWD; assert exit 2, the stderr text and no files created.
  * A compat-bytes check: `git diff --exit-code -- artifacts/compat/`.
  * The two retained-coverage tests named in PF09.3.
  * The reconciliation of R-01 to R-03 in the PR record:
    * the inventory with a disposition per member;
    * every R-01 concern located in the Adapter module;
    * no compatibility surface retained, so TI-06 is moot.
* **Dependencies.**
  * WU-PR-01 merged to `main` and accepted by its PR-40 lineage review.
  * The WU-PR-02 per-PR plan is formed against a `main` that contains WU-PR-01.
* **Owners.** As WU-PR-01, with its own dedicated PR sessions and its own Proceed.
* **Acceptance and evidence.**
  * AC-01 (no R-01 concern left under `engine/charts/`).
  * AC-03.
  * AC-04 (migration-level checks and the reconciliation).
  * AC-05.
  * Exact-head CI as WU-PR-01.
* **Environment.** As WU-PR-01.
* **Recovery and rollback.** Revert the PR to restore the module and the callers. No data or release state is involved. Rescope as WU-PR-01.

### WU-PR-03 — Final repository documentation (GCF-19)

* **Business case.**
  * *Beneficiary:* the delivery team and the QA lane.
  * *Evidence:*
    * HDE-EPIC040's QA Step-0B doc-delta record (`audit/docdeltas/hde-epic040_doc_deltas.md`, DD-05, DD-10, DD-11) found repository documentation that contradicted code, and QA had to carry it as caveats.
    * O-11 shows canon-named tooling that had silently stopped working for five weeks.
  * *Benefit:* QA-10 and later sessions read a repository record that matches the delivered boundary, so they do not plan against a removed module.
  * *Measure:*
    * A `CHANGELOG.md` "Unreleased — HDE-EPIC041" section names WU-PR-01 and WU-PR-02 and their nonclaims (O-20 convention).
    * A `git grep` sweep at the PR head finds no live repository document outside `docs/pfcanon/`, `docs/ephemeral/` and the historical prefixes describing `engine/charts/loader.py` as current.
* **Scope.**
  * The CHANGELOG section.
  * Any `README.md`, `AGENTS.md` or non-canon `docs/` statement the sweep finds stale. The Audit found none naming the loader. An AGENTS.md posture line for HDE-EPIC041 is added only if the per-PR plan shows a reader needs it, under the Doc agents rule.
  * Doc-Delta notes for the drainage targets DELTA-001 and DELTA-002 (Audit §9), carried in the PR description. They are not written to any canon file.
  * No `docs/pfcanon/` edit. No hand-edited governed evidence. No `audit/docdeltas/` file: that file is QA Step-0B's, as in HDE-EPIC040.
* **Dependencies.** WU-PR-02 merged and accepted. Initial delivery of WU-PR-03 completes before QA readiness (GCF-19).
* **Owners.** As WU-PR-01.
* **Acceptance and evidence.** The measure above. CI as applicable: the classifier selects lanes for `CHANGELOG.md` and docs paths, and the per-PR plan records them.
* **Environment.** Local and hosted CI only.
* **Recovery and rollback.** Revert the PR.

## 7. Requirement traceability

| Req / AC | WU-PR-01 | WU-PR-02 | WU-PR-03 | Audit basis |
| :- | :- | :- | :- | :- |
| R-01 / AC-01 | Entry and ownership | No concern left in Engine | — | §4 R-01; O-02, O-03 |
| R-02 / AC-02 | Pure module and checks | — | — | §4 R-02; O-06, O-16 |
| R-03 / AC-03 | — | Migration, retirement, guard | CHANGELOG record | §4 R-03; §5; D-1 |
| R-04 / AC-04 | Interface checks | Migration checks and reconciliation | — | §4 R-04 |
| AC-05 | Output equality; clean tree | Script, compat bytes, retained coverage; clean tree | — | O-08, O-11, O-12, O-19 |
| D1 to D4 (Specification §6) | D1, D2, D4 part | D3, D4 part | — | — |
| D5 close baseline | — | — | — | CL-05 at close (§10) |

**HDE phased accountability** (Plan Templates §12):

| Work item ID | PF09 disposition | Phased PF09 document | Task ID | Subtask ID | Exact source heading | Contribution | Status nonclaim |
| :- | :- | :- | :- | :- | :- | :- | :- |
| W-SEPA006 | in the current epic | HDE Build Checklist — Separation (PF09.3, v1.1.8) | HDE-SEPA006 | HDE-SEPA006.1 to .3 (rows below) | Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction | advances (WU-PR-01 to WU-PR-03) | This plan does not itself move PF09 status. |
| W-SEPA006.1 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.1 | Subtask HDE-SEPA006.1 — Adapter-owned acquisition and pure Engine normalization | advances (WU-PR-01) | This plan does not itself move PF09 status. |
| W-SEPA006.2 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.2 | Subtask HDE-SEPA006.2 — Supported caller migration | advances (WU-PR-02) | This plan does not itself move PF09 status. |
| W-SEPA006.3 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.3 | Subtask HDE-SEPA006.3 — Boundary and behavior verification | advances (WU-PR-01 interface checks; WU-PR-02 migration checks and reconciliation) | This plan does not itself move PF09 status. |

## 8. Lane separation and authorization

* **PR implementation.** Three work units, each with:
  * one per-PR plan, created with PR-20 in the PR-30 session;
  * one Proceed;
  * one branch and one PR;
  * PR-30 publication, then PR-35 correction and merge readiness in their own dedicated sessions;
  * Nathan's merge;
  * PR-40 lineage acceptance.

  Each PR is reviewable on its own and reversible by revert.
* **Ops.** None.
* **QA planning.** After all three work units are accepted:
  * QA-10 readiness, by the continuing Isis role;
  * QA-20 Guide;
  * QA-50 QA Audit and QA Plan, by Kronos;
  * QA-70 review.

  This Plan names no QA steps and adds no QA Guide or QA Plan as a PR prerequisite.
* **QA execution.** Under the arrangement the Product Owner chooses. This Plan issues no QA verdict.

## 9. Data, privacy, security, migration, rollout and rollback

* **Data and persistence.** Not applicable. No database, cache or vendor data is read or written (I-3).
* **Privacy and sensitive data.** The keys-only log line carries no birth input (ED-04). WU-PR-01 tests assert this.
* **Security and authorization.** No route, credential, flag or environment gate is added. The orchestration performs no network I/O (`NoIoGuard`).
* **Migration and compatibility.** No data migration. In-repository callers move (R-03). Callers' outputs and failures are preserved (I-4).
* **Rollout or release posture.**
  * No release cut and no change to `catalog/manifest.json` or `ADMITTED_RELEASE_*`, because no touched path is a member (O-10).
  * Each PR confirms this with `python tools/ci/prepush_check.py --path <path> membership`.
* **Rollback or safe refusal.** Revert the work unit's PR (§6).

## 10. Deliverables and completion predicates

| ID | Output | Lane | Completion predicate | Evidence pointer | Nonclaim |
| :- | :- | :- | :- | :- | :- |
| DL-01 | Pure Engine chart module and Adapter orchestration entry, with tests | PR (WU-PR-01) | PR-40 accepts the merged lineage | PR record, exact-head CI | Not QA, not acceptance of the Epic |
| DL-02 | Migrated callers; loader removed; guard and reconciliation | PR (WU-PR-02) | Same | Same | Same |
| DL-03 | CHANGELOG section and swept repository docs | PR (WU-PR-03) | Same | Same | No canon drainage |
| DL-04 | Close pack per Specification §10 | CL-05 (GCF-24.CLOSE), after a QA PASS | CL-05 close PR merged | Close report, manifest | Not part of this Plan's work units |

Governed evidence:

* None of DL-01 to DL-03 is planned to create or change a governed evidence family.
* If a per-PR plan finds that a changed path triggers one (for example an indexed artifact), it publishes it only through `tools/evidence/update_evidence_index.py` and the canonical generators. It then runs the read-only checks AGENTS.md names: `update_evidence_index.py --check`, `orientation_demo.py --check` and `ci/checks/check_mirror_schema.sh`.
* Tested-source identity stays distinct from any later evidence-storage commit and from review-time HEAD (Specification §8).

## 11. Validation and test intent

* **Static and unit:** the purity AST test with a negative self-test; orchestration unit tests; the repository-wide import guard.
* **Integration or contract:**
  * C-1 run as a subprocess from a temporary CWD;
  * characterization of the new entry against the old loader (WU-PR-01);
  * compat bytes unchanged;
  * retained-coverage tests.
* **Open-rails or external validation.** None planned. Specification §4 items 3 and 4 are preserved verbatim for the QA Plan owner:
  * **Item 3.** "*Binding condition.* If the Implementation Audit finds that any affected surface, including the new orchestration entry, is used to produce such a feature, or reaches vendor acquisition in a deployed or CLI path, the mandatory bounded live vendor test (synthetic data only, `SAFE_MODE=0`, `ALLOW_NETWORK=1`) applies to this Epic's QA Plan. No exemption or non-vendor substitute then applies. Closed-rails proof, static validation, repository inspection, generated evidence, an OPS observation or exemption language does not replace it."
  * **Item 4.** "*Broader scope.* This Specification records no exemption from the broader production-affecting open-rails requirement. If the Implementation Audit finds the changed boundary can affect runtime compute, vendor ingest, database retrieval or production-used CLI/API behavior, the QA Plan must carry a bounded open-rails step or an exemption authorized and recorded under the Product Owner. Silence is not an exemption."
  * **Audit determination.** Neither condition is met (Audit §6). If any later stage finds new reach, they re-attach.
* **Evidence identity and owner.** Each PR session records the commands, configuration, tested-source SHA, results, actor, time and limitations (AC-04).
* **Failure classification.** Behavior contradiction, tooling failure and an unavailable prerequisite are kept distinct, as AGENTS.md's QA status set requires.
* **Unexecuted-result nonclaim.** No test, QA, deployment or runtime result is claimed here.
* **Domain-correctness proof map.** Not applicable. No Human Design mechanics or compatibility computation changes.

## 12. Risks, exclusions and conflict-register treatment

| ID | Risk | Mitigation | Owner |
| :- | :- | :- | :- |
| RK-01 | A changed path fails CI classification (`CI_PRODUCT_OWNER_TEST_MISSING`) | Owner mappings in the same PR (O-13); pre-push `lanes` check | PR session |
| RK-02 | Removal before migration turns C-1's exit 2 into an `ImportError` | Migration and removal in one work unit (WU-PR-02) | PR session |
| RK-03 | Log contract drift | Keys and values pinned by WU-PR-01 tests; one line per call | PR session |
| RK-04 | A purity test that cannot fail | Negative self-tests required | PR session; PR-35 review |
| RK-05 | Scope creep into acquisition, provider contracts or the generator's compat repair | I-3; rescope to this IA | PR session; this IA |
| RK-06 | `main` CI is red for an unrelated cause (TI-02) | Each PR reads current-head CI and follows the CI-red rules; an unrelated failure is not this change's | PR session |

* **Conflict register.**
  * CCR-1 (acceptance map): unchanged; a close-pack matter for CL-05 (Ruling R-A).
  * CCR-2 and CCR-4: no effect.
  * CCR-3: not triggered (Audit §7). I-3 keeps it that way.
* **Exclusions.** §2.

## 13. Open-decision routing and unresolved items

* **D-1.** Decided: retire (Audit §8.1).
* **Open decisions:** none.
* **Unresolved items carried, not blocking:**
  * TI-07 / CCR-1: Product Owner, as a possible canon change.
  * TI-02, items 9 and 10: Product Owner.
  * FND-005 to FND-007: the CL-40 scan and the Product Owner.

## 14. Change Process Guide §3.1 machine header

```json
{
  "type": "IMPLEMENTATION_PLAN",
  "epic_id": "HDE-EPIC041",
  "crd_link": "not_applicable (Epic lane)",
  "digest": "Three ordered PR work units deliver HDE-SEPA006: WU-PR-01 adds a pure Engine chart interface and an Adapter-owned orchestration entry with purity, rails, correlation, keys-only logging and failure tests; WU-PR-02 migrates the three supported callers, retires the legacy signature (D-1) and removes engine/charts/loader.py with a repository-wide import guard and preserved outputs; WU-PR-03 records the delivered boundary in repository documentation. No Ops, no live proof, no release change.",
  "assumptions": [
    "No path touched is a release member (Audit O-10); re-verified per PR",
    "No production entry point loads the loader (Audit O-09); re-verified per PR"
  ],
  "code_capsules_finalized": [],
  "mutation_expectations": {
    "authorized_route": "PR",
    "template_required": true,
    "acceptance_criteria": ["AC-01", "AC-02", "AC-03", "AC-04", "AC-05"],
    "evidence_requirements": ["Specification v1.1 §8; this Plan §10 and §11"],
    "acceptance_tokens": [],
    "close_pack_files": ["audit/EPIC-041_close_report.md", "audit/EPIC-041_MANIFEST.json"]
  }
}
```

## 15. TypeSafe reading and surface advice for IA-30

* **Method.**
  * Installed TypeSafe scoring skill, request v8.2.
  * Script run once, session kind `review`, label "HDE-EPIC041 IA-30 Implementation Plan re-review".
  * No Notion row written: this is an executing-flow session, and IA-40 writes only under `docs/ephemeral/`.
* **Action sent (v8.2).** "Re-review one revised pending whole-change Implementation Plan of about 36 KB that was reviewed once and denied, checking against an item-by-item application report that eight exact redlines the reviewer wrote were applied: three blocking ones rewrite the open-rails quotation, the orchestration entry's argument contract and a characterization test's lifecycle across two of its three PR work units, and five are small business-case, invariant, CI-wording, accountability-table and search-pattern changes; the reviewer approves or returns exact redlines. A written prompt with steps exists; no code, test or canon change and no live run against a provider occurs. Per-PR plans, implementation and independent PR reviews follow later in separate sessions."
* **Reading, as printed.** **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.95 (confidence 0.89); rung probabilities low 0.00, medium 0.11, high 0.83, extra high 0.06, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 1.00, Sonnet 5.5 0.00, Haiku 5.5 0.00 (confidence 1.00). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.110, Opus 5.5 at high 0.830, Opus 5.5 at extra high 0.060, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T04:11:04Z. Nathan picks the cell.
* **Flags.** None printed.
* **Earlier readings.** v1.0 §15 keeps the reading for the first IA-30 review. Review v1.0 §5 keeps the reading for this IA-40 session.
* **Picks.** Nathan has stated no pick for the IA-30 re-review and none for this IA-40 session, so none is recorded.
* **Surface advice (IA-30).**
  * Run it in the continuing Isis role's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this Plan's pull request merges.
  * Read access is needed to `main`, including `docs/pfcanon/`, the Specification v1.1, review v1.1, this Plan v1.1, its application report, Plan v1.0, the IA-30 review v1.0 and the Audit.
  * A diff of v1.0 against v1.1 is the fastest check of the application; the report lists every change no redline states.
  * The IA-30 Notion page is needed.
  * Write access is needed to one branch and one pull request under `docs/ephemeral/`.
  * The Audit's §5.2 search and its X-1 to X-6 runs are repeatable locally under closed rails if the reviewer wants to check a fact.
  * Not needed: code changes, open rails, or vendor, Railway, database or Notion writes.

## 16. Approval

* **Approval sentinel:** `ASK OK?`
* **Approval state:** Pending.
* **Approval authority:** the continuing Isis role at IA-30 (GCF-11).
* **Approved scope or rejection basis:** not yet decided.

Approval of this Plan establishes no implementation, QA, Ops, deployment, release, acceptance, PF09 drainage, board or closure state, and gives no PR Proceed.

## 17. Nonclaims

This Plan claims no implementation, CI result, QA verdict, Ops, acceptance, PF09 or board movement, canon change, PF10 addendum, deployment or closure. It edits no approved artifact and no file outside `docs/ephemeral/`.
