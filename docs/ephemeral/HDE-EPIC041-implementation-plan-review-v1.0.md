---
artifact_type: IMPLEMENTATION_PLAN_REVIEW
artifact_version: "1.0"
logical_id: HDE-EPIC041-IMPLEMENTATION-PLAN-REVIEW
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
review_mode: INITIAL_PLAN_REVIEW
decision: INITIAL_DENY
decision_sentinel: REVISE AND RESUBMIT
reviewed_artifact: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.0.md
reviewed_artifact_version: "1.0"
reviewed_artifact_state: PLAN_PENDING, "ASK OK?" (unchanged by this review)
reviewed_artifact_identity: 31,508 bytes on main at ad662f7 (merged by amthorn78/glow-hdengine-v2#785)
implementation_audit: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE, 46,755 bytes; #785)
approved_specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; git blob a41b10b58ce9ff26b7999ce33eca5787e9800b28)
thoth_decision: docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md (CF-E-30, INITIAL_APPROVE, ASK OK; CANON_CONFLICT_REGISTER CCR-1 to CCR-4)
plan_author: the whole-change Implementation Agent for HDE-EPIC041 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj)
reviewer: Isis, the continuing Lead Developer role for HDE-EPIC041 (Isis-56; https://claude.ai/code/session_01Q789u35D8uKpsTHJ67oMCz). Isis authored the Specification v1.1 and did not author the Audit or the Plan
prompt: IA-30 — Review Whole-Change Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81ebb110fb0202874d8c; page state 2026-10-27T13:21:07.780Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1 (selected by the GCFPE Membership and Release Register, "Current selection", read 2026-10-28)
repository_head_read: origin/main ad662f7b263648fe41ebc11085f8fe31565c89e0
reviewed_at: 2026-10-28
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.md (searched by term; silent on this change)
pf10_addendum: NONE (INITIAL_DENY produces no PF10 addendum)
next_prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 102726.1
next_actor: the same whole-change Implementation Agent for HDE-EPIC041 (PREAPPROVAL_PLAN_REVISION)
---

# HDE-EPIC041 — Implementation Plan review (IA-30): INITIAL_DENY

## 1. Decision

**INITIAL_DENY** of `docs/ephemeral/HDE-EPIC041-implementation-plan-v1.0.md` v1.0. **REVISE AND RESUBMIT.**

The Plan is close to approvable. Its scope, work-unit order, D-1 handling, business cases and conflict-register treatment are sound (§4). Three defects block approval. Each changes execution or a quoted obligation:

* **F-1.** §11 labels Specification §4 items 3 and 4 as "preserved verbatim", but it drops sentences from both. The dropped text says that closed-rails proof cannot replace the live vendor test, and that the Specification records no exemption. Both the Specification and Ruling R-B require downstream Plans to preserve the two items.
* **F-2.** The orchestration entry's argument contract (§5.3) says other shapes raise `TypeError` "as today". That is not true for the shapes that today route to the legacy signature. The contract also accepts a positional `tz`, which today's code ignores. I-4 and the WU-PR-01 characterization test therefore cannot be carried out as written.
* **F-3.** WU-PR-01's characterization test imports today's loader. The Plan does not say how the test runs without writing the tracked log (I-5) or failing outside the repository root (O-06). It also does not say what happens to the test in WU-PR-02, where the module removal and the new import guard would break it.

Five more redlines would not block on their own, but the replacement applies them (§3.2). The Plan stays `PLAN_PENDING`. This decision produces no PF10 addendum. It authorizes no PR Instruction, per-PR Plan, Proceed, implementation, QA, Ops, PF09 movement or closure. The Plan returns to its same IA author through IA-40.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `ad662f7`. `git diff --stat b29ca84 ad662f7` changes only the Audit and Plan under `docs/ephemeral/`, so canon is byte-identical to what the Audit and Plan read. This branch changes nothing under `docs/pfcanon/`.

Search terms used: implementation plan, work unit, business case, General Implementation Plan, phased accountability, machine header, characterization, open-rails, production-functional, preserve items 3 and 4, review stability, severity mapping, template hygiene, chart loader, `SEPA006`, Doc-Delta, repo docs sweep, GCF-19, retired tests.

| Document (title; file read) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`) | §9.7.7 "Plan approval gate", whole section: "Business case for every requirement and work unit", "Template adherence is structural only", "Template-hygiene materiality rule", "Severity mapping and review burden", "Truth/proof blockers only", "Implementation Plan review boundary", "Plans are approval artifacts, not execution artifacts", "Accountability for task-like future work" | The work-unit business-case gate (§4.2); severity of F-1 to F-3 and of RL-4 to RL-8; why RL-7 is not a blocker |
| HDE Governance | §9.1.1 "Change authority and exact-artifact lineage" | IA authors and Isis reviews; a revision is a complete replacement returned to the same reviewer; the IP is concrete but creates no actual PR |
| Plan Templates (`PF27-Canon-Plan-Templates-v2.0.6.md`) | §12 "General Implementation Plan (Template)", whole section; "Canon precedence for template use"; "Review stability and no-moving-target discipline" | Structural check (§4.1); RL-7; full-gate first pass and blocker provenance (§3) |
| Change Process Guide (`PF06-Canon-Change-Process-Guide-v2.5.5.md`) | §3 "Implementation Plan", §3.1 to §3.4; §0 PR-route Doc-Delta rule (line 72); §3.5.3 "Repo docs sweep (major epics)" | Machine header (§4.1); WU-PR-03 Doc-Delta notes |
| HDE Build Checklist — Separation (`PF09.3-…-v1.1.8.md`) | Task HDE-SEPA006 and Subtasks .1 to .3 (lines 1280 to 1379) | Sequencing (.1 before .2; verification with both; .3 reconciles); deliverables and evidence; RL-7 rows |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.md`, the current controlled PF10) | Searched by term: chart loader, `engine/charts`, `get_chart`, `SEPA006`, implementation plan, work unit, business case. No match | Silent on every topic decided here, so permanent canon governs. No applicable active addendum (Audit §1.3, confirmed) |
| Specification v1.1 (approved, in-flight) | Whole document, in particular §3, §4 items 3 and 4 and "Implementation preservation", §8, §11 | F-1; RL-1 text; requirement coverage (§4.3) |
| Review v1.1 (CF-E-30, in-flight) | Whole document | CANON_CONFLICT_REGISTER CCR-1 to CCR-4 (§4.4) |
| Review v1.0 (CF-E-30, in-flight) | §4.3 Ruling R-B | F-1: "Downstream artifacts must preserve items 3 and 4" |
| Implementation Audit v1.0 (in-flight) | Whole document | Facts the Plan relies on; D-1 (§8.1 Q-01); ED-01 to ED-10 |
| Glow HDE Canonical Change Flow R1 oracle (`flowmaster-validate` reference `glow-hde-canonical-change-flow-r1-20261027.json`) | Rows GCF-19 and GCF-20 | WU-PR-03 is flow-required (`STOP_DOCS_PR_NOT_PLANNED`) |
| GCFPE Membership and Release Register (Notion) | "Current selection — GCFPE-20261027.1 / 102726.1" only; its historical sections were not read | IA-30 102726.1 is selected |
| IA-40 — Prepare or Revise Whole-Change Implementation Plan — 102726.1 (Notion, page state 2026-10-27T13:16:58.421Z) | Whole page | The exact-redline boundary each redline in §3 meets |
| AGENTS.md | Canon-first rule; closed rails; pytest readiness; pre-push check | Review procedure |

Scoped overrides: none. No PF10 addendum and no Product Owner rescope governs any topic decided here.

Silence: canon is silent on one question this review touches. It does not say whether this change's implementation evidence must be a governed, indexed family. That question is reported as N-4, not resolved.

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 2. Verification performed by Isis

Static reads only, on `main` `ad662f7`. Nothing was executed except `git`, `grep` and the GitHub run listing.

| Plan or Audit claim | Check | Result |
| :- | :- | :- |
| §5.3 "as today" for the argument shapes | Read `engine/charts/loader.py` lines 85 to 166 | Not true. Today, a first positional string that is not shaped `YYYY-MM-DD` goes to the legacy path (lines 153 to 158), not to `TypeError`. A keyword-form `birthdate` that is not so shaped recurses into the legacy path (line 162). `tz` is read only from keywords (line 115), so a fourth positional argument is ignored and gives "tz required on internal path". This supports F-2 |
| WU-PR-01's characterization test can run cleanly | The loader's log write (lines 69 to 73) is relative to CWD. `input_validators.py` reads `artifacts/constants/*.json` relative to CWD (lines 12, 13, 46, 53). C-2 and C-3 redirect with `monkeypatch.setattr(L, "_Path", …)` | The test needs the repository root plus the `_Path` redirection. The Plan states neither (F-3) |
| WU-PR-02's guard and the characterization test | `git grep` for importers of `engine.charts.loader` in `*.py` | Live importers are C-1, C-2 and C-3 only; all others are under `.audit_src/`. A WU-PR-01 characterization test would be a fourth importer, and the WU-PR-02 guard would fail on it (F-3) |
| Purity pattern in `tests/core/test_engine_core_purity.py` | Read | The AST deny-list checks a module's own imports and calls. An import of `engine.util.input_validators` would pass it, although that module holds file reads and `secrets` (RL-5) |
| `adapter/no_io_guard.py` usable in tests | Read | `NoIoGuard` is a context manager counting `connect`, `connect_ex` and `getaddrinfo` attempts. Usable as planned |
| `tests/retired_tests.md` row 57 | `grep -n` | Line 57 is the retired legacy test. Removed test files are recorded there by convention (RL-3) |
| `.audit_src/` and `_arch/` .py importers | `git grep` | No importer outside `.audit_src/` and the three live callers |
| `engine/charts/` contents | `ls` | `loader.py` only; no `__init__.py` |
| WU-PR-03 evidence | `audit/docdeltas/hde-epic040_doc_deltas.md` DD-05, DD-10, DD-11 | Present as cited: repository documentation that contradicted code, carried as QA caveats |
| TI-02 / RK-06 `main` CI | `ci` push runs on `main` | The latest run, #3858 on `7983b252` (2026-10-27), concluded `success`. #3855 on `1fb4731b` failed. Later `main` commits are documentation-only and started no run |
| Release selection | Register "Current selection" | GCFPE-20261027.1 / 102726.1, 56 members; IA-30 and IA-40 sit in the 102726.1 IA hub |

## 3. Findings and exact redlines

Severity follows HDE Governance §9.7.7, "Severity mapping and review burden". This is the first review of this Plan line, so every finding's provenance class is **Introduced by current revision** (Plan Templates, "Review stability and no-moving-target discipline"). The full gate set was applied to the full Plan.

Each redline gives the target, the anchor (unique in v1.0), the operation, the complete text, the reason and the linked edits. IA applies all eight to one complete replacement, v1.1, and preserves all other content. Quoted anchors are exact substrings of v1.0. "Linked edits" are the only other changes each redline authorizes.

### 3.1 Blocking

#### F-1 / RL-1: Specification §4 items 3 and 4 not preserved (Blocker)

* **Material harm.** These are statements of obligation that the Specification requires every derived Plan to preserve ("Implementation preservation"; Ruling R-B). v1.0 calls its text "verbatim" but drops the sentences that make the live vendor test non-substitutable, and the sentence recording no exemption. A QA Plan built from this Plan could then treat closed-rails proof as a substitute if the conditions re-attach.
* **Target and anchor.** Plan v1.0 §11, the two bullets beginning `  * **Item 3.**` and `  * **Item 4.**`.
* **Operation.** Replace both bullets.
* **Replacement:**

  ```text
    * **Item 3.** "*Binding condition.* If the Implementation Audit finds that any affected surface, including the new orchestration entry, is used to produce such a feature, or reaches vendor acquisition in a deployed or CLI path, the mandatory bounded live vendor test (synthetic data only, `SAFE_MODE=0`, `ALLOW_NETWORK=1`) applies to this Epic's QA Plan. No exemption or non-vendor substitute then applies. Closed-rails proof, static validation, repository inspection, generated evidence, an OPS observation or exemption language does not replace it."
    * **Item 4.** "*Broader scope.* This Specification records no exemption from the broader production-affecting open-rails requirement. If the Implementation Audit finds the changed boundary can affect runtime compute, vendor ingest, database retrieval or production-used CLI/API behavior, the QA Plan must carry a bounded open-rails step or an exemption authorized and recorded under the Product Owner. Silence is not an exemption."
  ```

* **Linked edits.** None. The lead-in sentence and the **Audit determination** bullet stay as they are.

#### F-2 / RL-2: Orchestration entry argument contract (Blocker)

* **Material harm.** Execution ambiguity, plus a false "as today". After D-1, the shapes that today reach the legacy path must go somewhere. v1.0 neither says where nor admits that their failure behavior changes. It also silently starts accepting a positional `tz`. I-4 ("keep today's values") and the WU-PR-01 characterization test cannot be satisfied or verified for those inputs. A PR session would have to choose, which an approved IP exists to prevent.
* **Target and anchor.** Plan v1.0 §5.3 **Orchestration entry**, the three sub-bullets beginning `* Signature:`, `* It accepts the positional form` and `* Any other argument shape raises`. In each fenced replacement below, indentation is shown relative to the fence, so a list line keeps the nesting level of the line it replaces or follows.
* **Operation.** Replace those three sub-bullets.
* **Replacement:**

  ```text
    * Signature: `load_chart(*args, **kwargs) -> dict`. `tz`, `correlation_id` and `log_sink` are read from the keyword arguments only, as today; a positional argument after the third is ignored, as today.
    * It accepts exactly the two call forms today's supported path accepts, with today's routing:
      * positional: at least three positional strings, the first matching `^\d{4}-\d{2}-\d{2}$` and the second matching `^\d{2}:\d{2}$`;
      * keyword: `birthdate`, `birthtime` and `place` keywords, with optional `tz`, routed as the positional form (the form C-1 uses).
    * Every other argument shape raises `TypeError("Invalid arguments to load_chart")`. That includes the shapes today's code routes to the legacy signature: a first positional string not shaped `YYYY-MM-DD`, and a keyword-form `birthdate` not so shaped. Today those raise `AttributeError` or return fallback data. D-1 retires that path, so this is the one intended change of failure behavior (I-4). The WU-PR-02 PR records it.
  ```

* **Linked edits:**
  1. §5.2 **I-4**: replace the sub-bullet "error `code` and `details.field` keep today's values;" with "error `code`, `details.field` and message keep today's values for every shape today's supported path accepts; the legacy-routed shapes of §5.3 raise `TypeError`, the one intended change;".
  2. WU-PR-01 **Tests and evidence**, orchestration tests: replace the sub-bullet "a bad argument shape → `TypeError`;" with "a bad argument shape, including each legacy-routed shape of §5.3 and a call with no arguments → `TypeError`;".

#### F-3 / RL-3: Characterization test procedure and lifecycle (Blocker)

* **Material harm.**
  * Run from the repository root without redirection, today's loader appends to the tracked `artifacts/logs/loader_call.jsonl`. That repeats E-2 in the work unit meant to end it, and breaks I-5.
  * Run from a temporary CWD, today's validators misreport a valid place (O-06), so the "equal results" proof fails.
  * In WU-PR-02, the same test would become a fourth importer of the removed module. It would then fail both on import and against WU-PR-02's own guard, and WU-PR-02's bounded scope does not cover removing it. That would force a rescope mid-delivery.
* **Target and anchors.** Plan v1.0 §6:
  * (a) WU-PR-01 **Tests and evidence**, the bullet beginning `* A characterization test proving`;
  * (b) the WU-PR-01 orchestration-tests sub-bullet `* a run from a temporary CWD validates the same as a run from the root.`;
  * (c) WU-PR-02 **Scope**, the bullet ending `No shim is kept.`;
  * (d) WU-PR-02 **Tests and evidence**, the guard sub-bullet `* a negative self-test on a synthetic source.`
* **Operations and text:**
  * (a) **Replace** the bullet with:

    ```text
    * A characterization test, in a test file of its own, proving that the new entry and today's `engine/charts/loader.load_chart` return equal results, and equal error `code`, `details.field` and message values, on the same inputs, for every call shape today's supported path accepts (§5.3), valid and invalid. It runs from the repository root, which today's validators need (O-06), with today's loader's log write redirected to a temporary directory by patching `engine.charts.loader._Path`, as C-2 and C-3 do today, so `git status --porcelain` stays empty (I-5). The old module still exists in this work unit, so this proves I-4 before removal.
    ```

  * (b) **Insert after** that sub-bullet:

    ```text
        * the fixture chart dict of O-03, and each `code`, `details.field` and message of §5.3, asserted as literal values, so they stay asserted after WU-PR-02 removes the old module.
    ```

  * (c) **Insert after** the bullet:

    ```text
      * Delete WU-PR-01's characterization test file in the same commit as `engine/charts/loader.py`. Record its removal as a new row in `tests/retired_tests.md` (reason: it compared the new entry with the removed module; replacing coverage: the WU-PR-01 orchestration tests that assert the literal values). Remove it from `pytest.ini` `testpaths` and the classifier roster where WU-PR-01 registered it. Row 57 is unchanged (I-6).
    ```

  * (d) **Insert after** the sub-bullet:

    ```text
        * the guard excludes only its own source file and the synthetic source of its negative self-test.
    ```

* **Linked edits.** None beyond (a) to (d). §5.2 I-6 stays as written: a new row leaves row 57 unchanged.

### 3.2 Non-blocking; the replacement applies them

#### RL-4: WU-PR-01 business-case Benefit overstates what the work unit delivers (Caveat)

* **Risk and safe default.** WU-PR-01 changes no caller, so on its own a run of today's loader can still write the tracked file. If PR-40 accepted WU-PR-01 against this Benefit, it would be accepting a benefit the work unit does not deliver. The safe default is that WU-PR-02 delivers that benefit. The business case itself is valid (§4.2).
* **Target and anchor.** WU-PR-01 **Business case**, the sub-bullet beginning `  * *Benefit:* chart validation becomes`.
* **Operation.** Replace the sub-bullet.
* **Replacement:**

  ```text
    * *Benefit:* chart validation exists as deterministic data-in/data-out code that tests can run from any CWD without touching the repository, and logging and file reads have one Adapter owner that writes no file by default. This work unit adds the interfaces and changes no caller, so on its own it does not stop a run of today's loader from writing the tracked file. That benefit is realized when WU-PR-02 migrates the callers and removes the loader.
  ```

* **Linked edits.** None.

#### RL-5: I-1 purity predicate is broader than its check (Caveat)

* **Risk and safe default.** The Audit's R-02 mitigation allows reusing the pure helpers of `engine.util.input_validators`. Read literally, I-1 forbids importing that module, because it also holds file reads and `secrets`. The deny-list pattern checks only direct imports. The safe default is the fresh-interpreter test, which does catch any read.
* **Target and anchor.** §5.2, the bullet beginning `* **I-1.**`.
* **Operation.** Replace the bullet.
* **Replacement:**

  ```text
  * **I-1.** The Engine chart module reads no time, randomness, environment, network, provider, logging or filesystem state, and writes none, at import or in any call; importing it has no side effect (R-02, AC-02). It may reuse the pure helpers `parse_date_yyyy_mm_dd` and `parse_time_hh_mm` of `engine.util.input_validators` (Audit §4, R-02), and calls no other function of that module. `_load_list`, `parse_place_city_cc`, `parse_tz_iana` and `ensure_cid` read files or randomness. The AST deny-list checks the module's own imports and calls. The fresh-interpreter test patches the time, randomness, environment, filesystem and socket entry points, and proves that none is reached at import or during validation and normalization.
  ```

* **Linked edits.** None.

#### RL-6: "a recorded valid waiver" names no waiver authority (Caveat)

* **Risk and safe default.** No CI waiver exists for HDE-EPIC041. The hosted-CI override in AGENTS.md is HDE-CRD-0001's. The wording invites a PR session to record one. RK-06 is the safe default.
* **Target and anchor.** WU-PR-01 **Acceptance and evidence**, the sub-bullet containing `green, or a recorded valid waiver`.
* **Operation.** Replace the sub-bullet.
* **Replacement:**

  ```text
    * Exact-head hosted CI `test` green. No CI waiver exists for HDE-EPIC041; a red result caused outside this change is handled under RK-06 and is not green.
  ```

* **Linked edits.** None. WU-PR-02's "Exact-head CI as WU-PR-01" then inherits the new text.

#### RL-7: HDE phased accountability table absent (Suggestion)

* **Not a blocker.** The PF09 mapping is present in substance: §1, §3, the work-unit headings and the §2 nonclaim. So the template-hygiene materiality rule applies.
* **Target and anchor.** §7, directly after the table row beginning `| D5 close baseline |`.
* **Operation.** Insert.
* **Text:**

  ```text

  **HDE phased accountability** (Plan Templates §12):

  | Work item ID | PF09 disposition | Phased PF09 document | Task ID | Subtask ID | Exact source heading | Contribution | Status nonclaim |
  | :- | :- | :- | :- | :- | :- | :- | :- |
  | W-SEPA006 | in the current epic | HDE Build Checklist — Separation (PF09.3, v1.1.8) | HDE-SEPA006 | HDE-SEPA006.1 to .3 (rows below) | Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction | advances (WU-PR-01 to WU-PR-03) | This plan does not itself move PF09 status. |
  | W-SEPA006.1 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.1 | Subtask HDE-SEPA006.1 — Adapter-owned acquisition and pure Engine normalization | advances (WU-PR-01) | This plan does not itself move PF09 status. |
  | W-SEPA006.2 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.2 | Subtask HDE-SEPA006.2 — Supported caller migration | advances (WU-PR-02) | This plan does not itself move PF09 status. |
  | W-SEPA006.3 | in the current epic | PF09.3 v1.1.8 | HDE-SEPA006 | HDE-SEPA006.3 | Subtask HDE-SEPA006.3 — Boundary and behavior verification | advances (WU-PR-01 interface checks; WU-PR-02 migration checks and reconciliation) | This plan does not itself move PF09 status. |
  ```

* **Linked edits.** None.

#### RL-8: WU-PR-02 tells the PR session to consult the Audit for its search (Suggestion)

* **Not a blocker.** The Audit is an in-flight governed input that PR-10 also receives. Embedding the scope and pattern makes the work unit self-contained.
* **Target and anchor.** WU-PR-02 **Scope**, the sub-bullet containing `Re-run the Audit §5.2 inventory search`.
* **Operation.** Replace the sub-bullet.
* **Replacement:**

  ```text
    * Re-run the inventory search at the PR head and record its result in the PR. Scope: all tracked files except `docs/pfcanon/` and `docs/ephemeral/`. Pattern: `engine\.charts|engine/charts|charts\.loader|load_chart\b|loader_call|LoaderInputError|_call_legacy` (Audit §5.2).
  ```

* **Linked edits.** None.

### 3.3 Nits and notes (not redlines; IA need not apply them)

* **N-1 (Nit).** Plan Templates §12 fields shown by content rather than by label:
  * "Non-goals" (folded into **Out of scope**);
  * "Contradictions or partial findings" and "Repository-dependent nonclaims" (§4);
  * the "Work-slice and dependency map" table (§6 carries each dependency with its producer and output).

  Change Process Guide §3.1's `context_header` and `codex_inputs` keys are absent from §14. The per-PR plan and PR Instruction carry those inputs. None of these creates ambiguity.
* **N-2 (Nit).** WU-PR-03's second evidence item, O-11, is about tooling that stopped working, not about documentation. The business case stands on DD-05, DD-10 and DD-11.
* **N-3 (Note).** TI-02 / RK-06: the latest `ci` push run on `main` (#3858, `7983b252`, 2026-10-27) succeeded. The OBS-17 failure at `1fb4731b` is not the current state. RK-06 is unchanged.
* **N-4 (Note; canon silence).** PF09.3 Subtask HDE-SEPA006.3 and Specification §8 require "required governed evidence" to be indexed through the authorized writer. Plan §10 plans no governed family and gives no basis for that determination. Canon, as searched, does not say whether this change's implementation evidence must be governed. The Plan's conditional rule (index only through the updater, if a changed path triggers a family) is a safe default. The question goes to QA-10 readiness, not to this revision.

## 4. Accepted

### 4.1 Structure

The Plan follows the Plan Templates §12 required structure, apart from the items in RL-7 and N-1:

* identity;
* purpose, scope, exclusions and nonclaims;
* governing-source map, citing HDE Build Notes by title only;
* observed reality;
* work units with dependencies;
* lane separation;
* the conditional fields;
* deliverables;
* validation intent;
* open-decision routing ("None");
* the approval block with `ASK OK?`.

The canon precedence rule is present. The §14 machine header follows Change Process Guide §3.1, with `acceptance_tokens: []` and the template's two close-pack files.

### 4.2 Work-unit business cases (the IA-30 gate)

| Work unit | Beneficiary | Evidence | Benefit | Measure | Result |
| :- | :- | :- | :- | :- | :- |
| WU-PR-01 | Delivery team | O-08 (three committed mutations of the tracked log); O-06 / X-3 (valid place misreported outside the root) | Risk and time: deterministic, CWD-independent validation; one Adapter owner of logging and files | Purity tests with negative self-tests; orchestration tests from a temporary CWD with zero sockets; clean tree | **Passes.** Observed incidents, not conformance to canon. RL-4 corrects the attribution of one benefit limb |
| WU-PR-02 | Delivery team | E-1 / O-04 / X-2; E-3; O-05; O-11 | The broken path is closed, not hidden; no supported caller depends on Engine I/O; a reintroduced importer fails CI | Module absent; guard with a negative self-test; C-1 behavior; compat bytes; retained coverage; clean tree | **Passes** |
| WU-PR-03 | Delivery team; QA lane | HDE-EPIC040 DD-05, DD-10, DD-11: repository documentation contradicted code and QA carried caveats (verified) | QA reads a record that matches the delivered boundary | CHANGELOG section; sweep finds no live document describing the loader as current | **Passes.** Rests on observed incidents, not "records for their own sake". It is also flow-required: GCF-19, `STOP_DOCS_PR_NOT_PLANNED` |

No work unit states a cost ceiling. None rests on conformance to canon, or on "could prevent" without an observed incident.

### 4.3 Coverage, architecture, sequencing and lanes

* **Requirements.** R-01 to R-04 and AC-01 to AC-05 each map to a work unit (§7). Specification §6 D1 to D5 map as stated.
* **D-1.** "Retire it" is applied (ED-06; WU-PR-02). TI-06 is moot.
* **Order.** WU-PR-01 → WU-PR-02 → WU-PR-03 follows PF09.3's ".1 before .2", "develop verification with both" and ".3 reconciles". Putting migration and removal together in WU-PR-02 is correct (RK-02).
* **Architecture.** I-2, I-3, I-5 and I-6, the pure interface shape, ED-01 to ED-10 and the target boundary are accepted. That includes repository-root anchoring of the pinned lists (ED-03) and the default `logging` sink with no default file write (ED-04).
* **Lanes and status.**
  * No Ops unit.
  * No live proof attached, on the Audit's §6 basis. The re-attachment rule is kept.
  * QA follows all three units, and QA steps are not a PR prerequisite.
  * No release-member change, confirmed per PR by the membership check.
  * Rollback is by revert.
* **External-system emulation.** No acceptance criterion emulates a vendor service or the hosted CI runner. `NoIoGuard` counts real socket calls and stubs no external system.

### 4.4 Canon conflict register

* **CCR-1 (acceptance map).** Unchanged. It is a close-pack matter for CL-05 (Ruling R-A).
* **CCR-2 and CCR-4.** No effect on the Plan.
* **CCR-3.** Not triggered. I-3 forbids the acquisition that would trigger it. Each PR re-checks it.

## 5. Next state, TypeSafe reading and surface advice

* **Next state.**
  * The Plan stays `PLAN_PENDING` at v1.0.
  * IA-40 (PREAPPROVAL_PLAN_REVISION) produces v1.1, `PLAN_PENDING_REVISED`, `ASK OK?`, with an item-by-item application report. It returns both to this reviewer at IA-30, in INITIAL_PLAN_REVIEW.
  * A redline IA finds ambiguous returns as `REDLINE_INCOMPLETE`, without inference.
  * The Audit v1.0 is unchanged and is not reviewed for approval here.
* **Open items and owners.** None blocks the revision.
  * TI-07 / CCR-1: Product Owner, as a possible canon change.
  * TI-02, items 9 and 10: Product Owner.
  * FND-005 to FND-007: the CL-40 scan and the Product Owner.
  * N-4: QA-10.
* **TypeSafe reading for IA-40.**
  * Method: installed scoring skill, request v8.2, script run once, session kind `authoring`, label "HDE-EPIC041 IA-40 Implementation Plan revision".
  * No Notion row was written. This is an executing-flow session, and IA-30 writes only under `docs/ephemeral/`.
  * Action sent (v8.2): "Revise one pending whole-change Implementation Plan of about 31 KB that was reviewed once and denied, by applying eight exact reviewer redlines into one complete replacement version: three blocking ones rewrite the open-rails quotation, the orchestration entry's argument contract and a characterization test's lifecycle across two of its three PR work units, and five are small business-case, invariant, CI-wording, accountability-table and search-pattern changes. A written prompt with steps exists; no code, test or canon change and no live run against a provider occurs. The replacement returns to the same independent reviewer for a second review."
  * As printed: **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.81 (confidence 0.83); rung probabilities low 0.00, medium 0.22, high 0.75, extra high 0.03, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.97, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.96). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.213, Opus 5.5 at high 0.728, Opus 5.5 at extra high 0.029, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.007, Sonnet 5.5 at high 0.022, Sonnet 5.5 at extra high 0.001, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T03:57:31Z. Nathan picks the cell.
  * Flags: none printed.
  * Picks: Nathan has stated no pick for IA-40 and none for this IA-30 session, so none is recorded.
* **Surface advice (IA-40).**
  * Run it in the same whole-change IA role's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this review's pull request merges.
  * Needs:
    * read access to `main`, including `docs/pfcanon/`, the Plan v1.0, this review, the Audit v1.0 and Specification v1.1;
    * the IA-40 Notion page;
    * write access to one branch and one pull request under `docs/ephemeral/`.
  * Each redline's anchor is a unique substring of Plan v1.0, so the edits can be applied and checked mechanically.
  * Not needed: code changes, test runs, open rails, or vendor, Railway, database or Notion writes.

## 6. Nonclaims

This review establishes none of the following:

* approval of any Plan version;
* a PR Instruction, per-PR Plan, Proceed, PR or merge authority;
* implementation, CI, QA, Ops or acceptance;
* PF09 or board movement;
* a canon change, a PF10 addendum or closure.

It does not edit the reviewed Plan or the Audit. Merging this file preserves the record and approves nothing (D21-C).
