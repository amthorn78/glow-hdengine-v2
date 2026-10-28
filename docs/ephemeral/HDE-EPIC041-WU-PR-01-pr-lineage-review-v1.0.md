---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_version: "1.0"
logical_id: HDE-EPIC041-WU-PR-01-PR-WORK-UNIT-LINEAGE-REVIEW
decision: ACCEPT
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-instruction-v1.0.md (v1.0; blob 455874034a8a627b1b2706c8193bb4c35dc010f7)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0.md (v1.0, with its companion docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0-prototype.diff)
PR30_RESULT_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED)
PR35_RESULT_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-result-v1.5.md (MERGE_PENDING on 2992cd07; historical pre-merge evidence; predecessors v1.1 to v1.4 read in full)
PR_REFS: [amthorn78/glow-hdengine-v2#791]
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1, approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE)
entry: MERGE_OBSERVED for #791 (Nathan's manual merge, 2026-10-28T17:26:38Z), as the pasted handoff states; the earlier conditional PR-40 block is void. Merged state verified independently (§2)
reviewer: the designated PR reviewer for WU-PR-01, run in the whole-change IA context for HDE-EPIC041 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj). This context authored the Audit, Plan and PR instruction. It authored none of the PR-20 plan, the code, the tests or the PR-30/PR-35 results
pr_sessions: PR-20/PR-30 https://claude.ai/code/session_01Q789tyc3umMjXiHB1aoXAR; PR-35 https://claude.ai/code/session_01Q789tzt85iauNogD8xS2zg
prompt: PR-40 — Review PR Work-Unit Lineage — 102726.1 (https://app.notion.com/p/4064590a05eb81479a74fa542b90cadb; page state 2026-10-27T13:18:21.343Z, read in full)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
ecosystem_release: GCFPE-20261027.1 / 102726.1
repository_head_reviewed: origin/main e72c9bac88ce96f5b974b461600ab146a6076c30 (the squash merge of #791; nothing after it)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.1.md (574 lines, 48,634 bytes, sha256 300e19679173c7dbf3c077be8edc12f90e9890b89d590426e5ca2b0d55870e68; read in full; provenance)
pf10_addendum_created: none (PR-40 is not an addendum producer)
return_owner: the whole-change IA for HDE-EPIC041 (Plan progress)
reviewed_at: 2026-10-28 (UTC)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-PR40-WU-PR-01-20261028
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    work_unit: WU-PR-01
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: PR-40 — 102726.1 (https://app.notion.com/p/4064590a05eb81479a74fa542b90cadb), revision as of 2026-10-27T13:18:21.343Z
    role_stage: designated PR reviewer / GCF-17.LINEAGE
    captured_at: 2026-10-28
    runtime_identity: https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj
    inherited_usage: HDE-EPIC041-PR10-WU-PR-01-20261028; HDE-EPIC041-PR20-WU-PR-01-20261028; HDE-EPIC041-PR30-WU-PR-01-20261028; HDE-EPIC041-PR35-WU-PR-01-20261028
    result_references: "#791; squash e72c9bac; final reviewed head 815fd5b2"
    repository_persistence: PENDING (no docs/changes/GCFPE_PROMPT_PROVENANCE.md; owner GCFPE management; non-gating)
---

# HDE-EPIC041 WU-PR-01 — PR work-unit lineage review v1.0 (PR-40): ACCEPT

## 1. Decision

**ACCEPT.** WU-PR-01 is delivered completely, and the delivery is attributable to its ordered lineage, which is the one PR, amthorn78/glow-hdengine-v2#791.

* #791 is merged. Its squash commit `e72c9bac` has the same tree as the final reviewed and CI-verified head `815fd5b2` (§2, §3).
* Every obligation of the PR instruction is met by the landed code and tests (§4).
* Every review finding is resolved. There is no open P1 (§5).
* The three changes made after the plan's companion diff are in-scope corrections recorded by PR-35. Each is evidenced (§6).
* The business-case measure is met (§7). Under HDE Governance §9.7.7 the work unit stops.

ACCEPT is not QA, Ops, release, acceptance of the Epic or closure. It returns WU-PR-01 to the whole-change IA for Plan progress (§11).

## 2. Merge state and PR evidence

| Item | Evidence |
| :- | :- |
| PR | #791, `state: closed`, `merged: true`, `merged_at` 2026-10-28T17:26:38Z, `merged_by` amthorn78 (GitHub) |
| Base | `main` `e121e354060afe3007a84d82b61b073df1da666b` (#792) |
| Final reviewed head | `815fd5b2eb9bc04d35bf33096a0e16b93a1ea85f` (the v1.5 record's commit, on `2992cd07`) |
| Landing | squash commit `e72c9bac88ce96f5b974b461600ab146a6076c30`, sole parent `e121e354` |
| Trees | `e72c9bac^{tree}` = `815fd5b2^{tree}` = `b09e6d643d6ecf46dcc6e95a3bb053c859b0adac` |
| Later divergence on `main` | none: `origin/main` = `e72c9bac` at review time |
| PR commits, in order | `2f7657c6` (implementation, PR-30); `c6e50a98` (result v1.0); `e6797eab` (merge of `main` after #792); `b399cfd0` (ID-35-1 test fix); `1b273594` (v1.1); `8b556e94` (v1.2); `b4f897d5` (v1.3); `72d40b5f` (ID-35-4 purity fix for F-1); `2992cd07` (v1.4); `815fd5b2` (v1.5) |
| Merge-order dependency | #792 merged first (12:23:16Z) and was merged into the branch (`e6797eab`), as the Product Owner directed |

## 3. Reviews and CI

* **Codex code review.** Run on every head that carried new commits. The latest summary (comment 6461664951) reads `code_review {commit_sha: 815fd5b2…, has_any_findings: false, has_unresolved_findings: false, status: completed}`, completed 2026-10-28T16:15:35Z. One finding was raised on the whole PR, F-1 (P2, on `b4f897d5`). It was fixed in `72d40b5f`, the reply names the commit, and thread `PRRT_kwDOP103ks6xMqM-` is resolved and outdated. The stalled automatic run on `8b556e94` was re-run at the Product Owner's choice (PO-35-1). That run had no findings.
* **Security review.** Not run. Neither the instruction nor the repository instructions require one for this change, which adds no route, credential, flag, network or environment gate. No security finding exists.
* **Exact-head CI on `815fd5b2`.** Check run 122942172254 (run 40723983402), `test`, `success`, 16:14:27Z to 16:33:34Z. All seven lanes ran, and the log ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. No waiver was used, and none exists for HDE-EPIC041.
* **Post-merge `main` push run on `e72c9bac`.** Run 40735776026 was in progress at review time. Steps 1 to 13 had succeeded: checkout, classification, install, isolated changed tests, and the product, compatibility, database and rails lanes. The evidence lane was running. It tests the same tree as `815fd5b2`. Its final state is recorded in §12 as it stood when this record was committed. It is not an acceptance predicate, because the pre-merge exact-head run on the identical tree passed.
* **Local corroboration by this reviewer** (closed rails through `env -i`, `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`, CPython 3.13.17 scratch venv with CI's install, on `e72c9bac`, 2026-10-28T17:36:19Z to 17:36:23Z):
  * `pytest tests/charts tests/adapter/test_chart_orchestration.py tests/adapter/test_chart_orchestration_characterization.py tests/loader tests/core/test_engine_core_purity.py`: 63 passed, and `git status --porcelain --untracked-files=all` was empty.
  * Classifier, read-only: both new modules map to their owner tests, and all four new test files are full-validation targets.
  * `catalog/manifest.json`: 45 members, neither new module among them.

  This is not CI, QA or governed evidence.

## 4. Requirement coverage across the complete work unit

| Instruction obligation | Landed evidence | Result |
| :- | :- | :- |
| §3.1 boundary: an Adapter-owned non-HTTP entry owns the `SAFE_MODE` read, both clocks, the correlation id, the repository-root-anchored pinned-list reads, fixture acquisition and the keys-only log line; it calls the pure interface | `adapter/chart_orchestration.py`: `os.getenv("SAFE_MODE")`, `time.perf_counter`, `datetime.now(UTC)`, `ensure_cid`, `_ROOT = Path(__file__).resolve().parents[1]`, `_fixture_chart`, `_emit`; calls `validate_birth_inputs` and `normalize_chart`. No route, no file write | Met (AC-01 for this unit) |
| §3.2 I-1, purity of the Engine module, including at import | `engine/charts/pure.py` imports only `re`, `unicodedata` and `typing`. `tests/charts/test_chart_pure_purity.py` has an AST deny-list (now forbidding every import from `input_validators`), a cold-import check and a patched re-import with calls, plus three negative self-tests. `engine/__init__.py` is empty | Met (AC-02). It reuses neither `input_validators` helper, which I-1 permits ("may") |
| I-2 | The R-01 concerns occur only in the entry for chart loading (code read) | Met |
| I-3, no acquisition, provider contract, fallback, route, flag, CLI option or release-member change | Landed name-status lists no such path. Neither module imports a resolver, provider, vendor, HTTP or CLI module. Membership is unchanged | Met; CCR-3 not triggered |
| I-4, outputs and failures preserved; legacy-routed shapes raise `TypeError` | Characterization test: 13 supported-path shapes equal today's loader in result, `code`, `details.field`, message and log fields other than `ts` and `duration_ms`. Literal-value tests of the fixture dict and its canonical bytes, and of each code, field and message. The `TypeError` test covers no arguments, legacy positional, legacy keyword and date-only | Met |
| I-5, clean tree | The CI clean-tree step passed on `815fd5b2`. Local run clean (§3) | Met (AC-05 for this unit) |
| I-6, historical captures, `loader_call.jsonl` and `retired_tests.md` row 57 unchanged | Not in the landed name-status | Met |
| §3.3 argument contract | `_birth_args` and the routing order match §3.3. Keyword-only `tz`, `correlation_id` and `log_sink`. A fourth positional argument is ignored (tested). One line per call (asserted on every `_call`) | Met |
| §3.3 log line keys, order and values; `safe_mode` reading; default sink is a logger with no file; a raising sink never breaks the call | `test_log_line_is_keys_only`, `test_safe_mode_field`, `test_default_sink_is_the_module_logger_and_writes_no_file`, `test_a_raising_sink_does_not_break_the_call` | Met |
| §3.3 pure interface: typed error, check order, messages, `normalize_chart` | `tests/charts/test_chart_pure_interface.py`; characterization `test_normalize_chart_matches_todays_normalizer` | Met |
| §3.4 real inputs | The plan's §6 table. Pinned-list absence is the stated limit, with no fallback | Met |
| §4 bounded files; must-not-change list | 7 code and test paths plus 6 records. Nothing under `engine/charts/loader.py`, `scripts/`, `tests/loader/`, `engine/util/`, `engine/config/`, `engine/provider*/`, `catalog/`, governed evidence or `docs/pfcanon/`. `pytest.ini` unchanged: the owner mappings put the tests in full validation (plan PD-4; verified §3) | Met |
| §5 tests and evidence; AC-04 record | Result v1.0 §4, v1.1 §4 and v1.4 §4: commands, configuration, tested-source SHAs, counts, actor, times and limitations | Met (AC-04 interface part) |
| §6 acceptance: exact-head CI green, no waiver | §3 | Met |
| §7 CI facts: full-validation cost; one coherent push | One implementation push. The corrections were pushed coherently, each after local items 1 to 5 | Met |
| §8 recovery and rescope | No `RESCOPE_REQUEST` was needed. In-scope repairs were made in place | Met |
| §9 ownership: PR-30 publication, then PR-35 in its own session; no agent merge | Two sessions as recorded; Nathan merged | Met |
| §10 CANON_CONFLICT_REGISTER carried | Carried unchanged through the plan and v1.0 to v1.5 | Met (§9 here) |
| HDE Build Notes, addendum on planning documents and PF-Canon versions (R-1, R-2) | No landed code or test reads, binds or resolves a path under `docs/ephemeral/` or `docs/pfcanon/`, or pins a PF file name or version (code read; PR-35 v1.1 diff search) | Conforms |

Documentation: none was due in this unit (plan §8 Doc-Delta row). DELTA-001 and DELTA-002 drain after WU-PR-02, and WU-PR-03 carries them.

## 5. Findings and their dispositions

| ID | Source | Disposition | State |
| :- | :- | :- | :- |
| F-1 (P2) | Codex on `b4f897d5`: importing `engine.charts.pure` loaded `random` and `secrets` through `engine.util.input_validators` | Fixed in `72d40b5f` (local `_parse_time`, cold-import check, AST rule, planted-import self-test). The reply names the commit | Resolved; Codex found nothing on the two later heads |
| OBS-3 | Plan §16: base-red close-pack test | Fixed on `main` by #792 and merged into the branch | Closed |

No P1 at any priority was raised. No finding was declined.

## 6. Delivered code against the plan's companion diff

These three changes are attributable to PR-35. None changes scope.

| ID | Change | Basis | Evidence |
| :- | :- | :- | :- |
| `e6797eab` | Merge of `main` after #792 | Plan §19 OBS-3 rule; Product Owner direction | Not in the landed delta: the squash's base is `e121e354`, which already contains #792 |
| ID-35-1, `b399cfd0` | `test_log_line_is_keys_only` no longer checks the clock-derived `ts` for the birth-input substring `12:34` | A real-input defect (the runner's clock) in this PR's own test | Pinned-clock reproduction in v1.1 §5 |
| ID-35-4, `72d40b5f` | `pure.py` uses a local `_parse_time` rather than importing `parse_time_hh_mm`; purity harness strengthened | F-1, a guarantee breach (I-1, AC-02, HDE Architecture §1.1) on a real input. The plan's PD-5 had reused the helper, which I-1 permitted but did not require | No difference from `parse_time_hh_mm` over 579,212 probes; the new tests fail on the old `pure.py`; characterization against today's loader passes |

## 7. Business-case measure (instruction §2)

**Met.**

* The AC-02 purity and import-side-effect tests pass. Each negative self-test fails its planted violation: planted imports and calls, a planted environment read, a planted `import secrets`.
* The orchestration tests pass with an injected sink and from a temporary CWD, and `test_no_socket_attempts` asserts `NoIoGuard.attempts == 0`.
* `git status --porcelain` is empty after the runs: the CI clean-tree step and this reviewer's local run.

The benefit about the tracked file is not claimed here. As the instruction states, it is realized only when WU-PR-02 migrates the callers and removes the loader. WU-PR-01 stops.

## 8. Merged-change attribution

This section uses the `glow-merged-change-attribution-lock` skill (1.2.0, interface `GLOW-MERGED-CHANGE-ATTRIBUTION-082826.3`, `SHADOW_VALIDATION`), in local Git mode.

* **Comparison.** The comparison ref is `origin/main`, pinned to `e72c9bac88ce96f5b974b461600ab146a6076c30`. The attributed change is `amthorn78/glow-hdengine-v2#791`, squash `e72c9bac` with pre-stage `e121e354`. The direct delta (base `e121e354` to head `815fd5b2`) and the landed delta (`e121e354` to `e72c9bac`) have the same SHA-256 `245fbb552bc7f2b98bda78c023c740a6a0319c8729b424741ebc3af8b5f95330`. Reconciliation: **EXACT**.
* **Landed paths (13).**
  * `adapter/chart_orchestration.py` (A);
  * `ci/checks/classify_ci_changes.py` (M);
  * `engine/charts/pure.py` (A);
  * the four test files (A);
  * the six result records v1.0 to v1.5 under `docs/ephemeral/` (A).
* **Divergence.**
  * Later committed divergence: none (an empty delta from `e72c9bac` to the comparison SHA).
  * Worktree-only divergence: none (empty staged, unstaged and untracked deltas).
  * Interstage divergence: none.
* **Validator.** The attribution artifact validated (`status: PASS`, `eligible_as_validated_evidence: true`). Evidence-manifest SHA-256: `3826c67645ba88d495bd1d377425fc7bdd04885e0eff6bcbd3f64a9d663c2de8`.
* **Unproven items.** None.
* **Shadow comparison.** The native review (§2: tree identity, parent topology, PR metadata) agrees with the skill's result. There is no discrepancy.
* **Retention.** The artifact was task-scoped and is discarded after this review. It is not retained as a separate record.
* **Separation.** The merge of `main` (`e6797eab`) and #792's content are not attributable to WU-PR-01, and the squash delta excludes them.

## 9. CANON_CONFLICT_REGISTER (carried unchanged)

| ID | Status | Treatment at this review |
| :- | :- | :- |
| CCR-1 (acceptance map for tokenless work) | APPROVED, Thoth, CF-E-30 review v1.1 (Ruling R-A) | A close-pack matter for CL-05 |
| CCR-2 (Business Case content lists) | APPROVED, Thoth, review v1.1 | None |
| CCR-3 (S19 vendor decisions) | APPROVED as conditional, Thoth, review v1.1 | Not triggered by the landed code (§4, I-3) |
| CCR-4 (cited Build Notes loader record) | APPROVED, Thoth, review v1.1 | None |

No new entry. The new HDE Build Notes addendum on planning documents and PF-Canon versions is current canon, not a conflict with the approved bases. Neither the Specification nor the Plan requires code to read a planning document or a versioned PF file. Its bearing on later units is recorded in §10.

## 10. Observations carried to the IA for the next stage

Not one of these is a defect in WU-PR-01.

| ID | Observation | Owner and use |
| :- | :- | :- |
| OBS-4 | `tests/loader/test_loader_logs_keys_only.py::test_loader_emits_keys_only_log` fails whenever it runs while the UTC clock reads `12:34` (PR-35 v1.1 §7). It can turn a full-validation pull request red about 84 seconds a day | WU-PR-02's instruction: C-3's migrated test must not carry the clock defect, and the test is removed or replaced with the loader |
| OBS-1 | `engine.util.input_validators.parse_date_yyyy_mm_dd` reads `TZ` through `time.tzset()` on its first call in a process (plan §16) | Context for FND-006; no WU-PR-02 change |
| AUD-CORR-1 | Audit v1.0 §4 R-02 (mitigation) and Plan v1.1 I-1 name `parse_date_yyyy_mm_dd` and `parse_time_hh_mm` as pure helpers. Importing their module loads `secrets` and seeds `random` (F-1), and the date helper reads `TZ` (OBS-1). The landed code relies on neither. Issued versions are not edited; this record corrects the statement for later stages | The IA. WU-PR-02's instruction must not tell a caller to import `engine.util.input_validators` into a pure path |
| PF10-2.2 | HDE Build Notes now forbids code, tests, tools, CI, governed evidence and close packs from reading, binding or resolving a path under `docs/ephemeral/`, or pinning a PF file name or version (R-1, R-2). The close-pack writer runs only at close (R-3). It was read in full as v13.9.1 | WU-PR-02's instruction: the repository-wide import guard must not read `docs/ephemeral/` or `docs/pfcanon/`. No test may depend on a planning document. WU-PR-03 and CL-05 apply R-1 to R-3 |
| OBS-2, OBS-5 | Local-environment facts: the container exports credentials, so use `env -i`; the clone is shallow; the canon hook writes `.git/` during `replay` | Later sessions' surface advice |

## 11. Next approved Plan stage

* **Selected unit.** `WU-PR-02` — "Caller migration, legacy retirement and boundary reconciliation (HDE-SEPA006.2; reconciliation part of .3)", Plan v1.1 §6.
* **Dependency.** "WU-PR-01 merged to `main` and accepted by its PR-40 lineage review." Merged: §2. Accepted: this record.
* **Per-PR plan base.** WU-PR-02's per-PR plan is formed against a `main` that contains WU-PR-01, here `e72c9bac` or later.
* **Lane.** An ordinary PR unit, so it goes to PR-10 — Create PR Work-Unit Instructions — 102726.1, run by the whole-change IA.
* **Not reached.** WU-PR-03 depends on WU-PR-02 merged and accepted. QA-10 follows all three units.

## 12. Post-merge `main` run (as recorded at commit time)

* Run 40735776026 (`ci`, push, job 122983777462), on `e72c9bac`.
* Read at about 17:40Z, before this record was committed: **in progress**.
  * Steps 1 to 13 had concluded `success`: checkout of `e72c9bac`, classification, the AGENTS.md citation check, install, pytest readiness, the closed-environment check, isolated changed tests (17:27:24Z to 17:33:53Z), and the product, compatibility, database and rails lanes.
  * Step 14, the evidence lane, was running. Steps 15 to 17 (QA lane, release attestation, final applicability check) were pending.
* Its final conclusion is not recorded here and is not claimed. It does not bear on ACCEPT: the exact-head run on `815fd5b2`, whose tree is the same, passed every step (§3).
* If it ends red, the cause is a fact for its owner under the CI-red rules. It does not reopen this review unless it shows a defect in WU-PR-01's code.

## 13. TypeSafe reading and surface advice for PR-10 (WU-PR-02)

* **Method.**
  * Installed TypeSafe scoring skill, request v8.2.
  * Script run once, session kind `authoring`, label "HDE-EPIC041 PR-10 WU-PR-02 PR instruction".
  * No Notion row written: this is an executing-flow session, and PR-40 writes only under `docs/ephemeral/`.
* **Action sent (v8.2).** "Create a new PR work-unit instruction for the second of three planned PR work units in one approved whole-change Implementation Plan, after the first unit was merged and accepted: migrating three callers (one script and two tests) of one legacy Python module of about 170 lines to the new interfaces, removing that module, adding a repository-wide import guard and a retired-test record, and updating CI test registrations, from the approved Plan's scope, invariants and test list plus four carried observations from the first unit. A written prompt with steps exists; no code is changed and no live run against a provider occurs. A per-PR plan, the Product Owner's Proceed, implementation and independent PR reviews follow later in separate sessions."
* **Reading, as printed.** **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.70 (confidence 0.67); rung probabilities low 0.05, medium 0.29, high 0.57, extra high 0.08, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.76, Sonnet 5.5 0.21, Haiku 5.5 0.02 (confidence 0.68). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.001, Fable 5.1 at medium 0.003, Fable 5.1 at high 0.006, Fable 5.1 at extra high 0.001, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.038, Opus 5.5 at medium 0.220, Opus 5.5 at high 0.433, Opus 5.5 at extra high 0.061, Opus 5.5 at max 0.008, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.011, Sonnet 5.5 at medium 0.061, Sonnet 5.5 at high 0.120, Sonnet 5.5 at extra high 0.017, Sonnet 5.5 at max 0.002, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.006, Haiku 5.5 at high 0.011, Haiku 5.5 at extra high 0.002, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T17:37:22Z. Nathan picks the cell.
* **Flags.** None printed.
* **Picks.** Nathan has stated no pick for PR-10 (WU-PR-02) and none for this PR-40 session. PR-35 v1.5 §7 keeps the reading for this PR-40 session. None is recorded.
* **Surface advice (PR-10, WU-PR-02).**
  * Run it in the whole-change IA role's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this review's pull request merges.
  * Read access is needed to `main`:
    * this review;
    * Plan v1.1 and its review;
    * the Audit and Specification v1.1;
    * the WU-PR-01 instruction and results;
    * `docs/pfcanon/`, including HDE Build Notes;
    * the code WU-PR-02 touches (`engine/charts/loader.py`, `scripts/make_compat_determinism_artifacts.py`, `tests/loader/`, `tests/retired_tests.md`, `pytest.ini`, `ci/checks/classify_ci_changes.py`, `adapter/chart_orchestration.py`, `engine/charts/pure.py`, the four WU-PR-01 test files).
  * Write access is needed to one branch and one pull request under `docs/ephemeral/`.
  * Not needed: code changes, test runs, open rails, or vendor, Railway, database or Notion writes.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` `e72c9bac`. Since the instruction (`23324960`), the only `docs/pfcanon/` change is HDE Build Notes v13.9 replaced by v13.9.1 (#792). This branch changes nothing under `docs/pfcanon/`.

| Title (file) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.1.md`, the current controlled PF10) | Whole file, 574 lines. The base sections and the S19 addendum equal v13.9, which was read in full for the Audit, and the v13.9.1 diff was read line by line. The new addendum "Planning documents and PF-Canon versions are never inputs; the close-pack writer runs only at close" was read in full | §4 last row (the landed code conforms to R-1 and R-2); §10 PF10-2.2. The S19 addendum does not apply (CCR-3, §9) |
| HDE Architecture (`PF02-…-v2.4.7.md`) | §1.1 "Single homes" (Purity rule; Non-BodyGraph chart loader classification; `adapter/`) | §4 I-1 and §3.1; F-1's guarantee |
| HDE Mechanics Guide (`PF14-…-v3.5.9.md`) | §1.1 "BodyGraph and loader seam posture" and the paragraph that follows it | §4 I-3: no fallback, no Engine I/O exception, no second resolver |
| HDE Governance (`PF04-…-v2.8.8.md`) | §9.7.7 "Business case for every requirement and work unit"; §9.1.1 | §7 measure and stop rule; author and reviewer lineage |
| HDE Build Checklist — Separation (`PF09.3-…-v1.1.8.md`) | Task HDE-SEPA006; Subtasks .1 and .3 | Scope delivered by this unit; ".1 before .2" (§11) |
| Change Process Guide (`PF06-…-v2.5.5.md`) | "PR review finding disposition (every pull request; real inputs only)" | §5: F-1 fixed as a real-input guarantee breach; ID-35-1 a real-input test defect |
| Plan Templates (`PF27-…-v2.0.6.md`) | "Review guardrails" (finding disposition, P1, repeated class); "Canon precedence for template use" | §5; precedence rule below |
| Specification v1.1, Implementation Audit v1.0, Plan v1.1 and review v1.1 (in-flight) | R-01, R-02, R-04, AC-01, AC-02, AC-04, AC-05; Audit §4, §5, §8; Plan §5, §6, §7, §10, §11; review v1.1 §4 | §4 coverage; §10 AUD-CORR-1; §11 next unit |
| WU-PR-01 instruction, plan v1.0, results v1.0 to v1.5 (in-flight) | Whole documents | §2 to §7 |
| PR-40 — Review PR Work-Unit Lineage — 102726.1 (Notion) | Whole page | Procedure, decision vocabulary, next-stage resolution |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## Nonclaims

This review accepts WU-PR-01's delivery only. It is not a merge or merge request. It is not QA, Ops, deployment or release, and it does not accept HDE-EPIC041. It is not PF09 or board movement, a canon change, a PF10 addendum, or closure. It does not authorize WU-PR-02's implementation, which needs its own instruction, plan and Proceed. It does not edit any reviewed artifact. Merging this file preserves the record and approves nothing (D21-C).
