---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.2.md
artifact_version: "1.2"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review correction and merge readiness); this record is the checkpoint for PR-35's second corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.1.md (v1.1, PR-35 checkpoint for the first corrective push; preserved unchanged). Lineage and facts recorded there are not repeated here
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1)
PR_RETURN_PHASE: none (no rescope is open)
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1 (unchanged from v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md (v13.5.3; blob a51bf40a4bcd2cc95653fb5c3e327bf61162aa52; read in full; unchanged)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. No other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED)
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: e13516b4ebd944900f02687500d1e6a324a3ff55 (the v1.1 checkpoint commit; its parent c5116f7 is the first correction)
correction_commit: ea4d72e614a63a98d821dccfcd626323623cd452 ("fix(evidence,tests): reject dynamic namespace access for presenter-bound helpers; AST guards (#627 review)"; parent e13516b; tree f8672952c5dd0b1b0e3594bf544599f43a405049, the exact tree every §5 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.3.md
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.2 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The first corrective push (v1.1) was verified, and its review thread was answered and resolved.

The Codex review of the resulting head `e13516b` raised two new P2 findings. Both are substantive and in scope, and both are corrected in one commit. That commit is published by the push that carries this record (§3–§5).

Still open:
- CI on the head this push creates;
- the Codex review of that head;
- the Codex security review, which has not run on #627 (§6);
- mergeability.

This record returns no PR-35 result. It claims no merge readiness, QA verdict, acceptance, PF09 movement or closure.

## 2. First corrective push, verified

| Fact | Evidence |
| :- | :- |
| Push | `68d9207..e13516b` to `claude/elegant-mayer-y6ppap` at 01:19:47Z; `git ls-remote` = `e13516b4ebd944900f02687500d1e6a324a3ff55`; the PR read shows head `e13516b`, 4 commits, 102 files, base `e3a5ed4` |
| R-1 thread `PRRT_kwDOP103ks6rq-UC` | reply r4253803611 naming `c5116f7`; thread resolved (the tool confirmed it; a later read shows `is_resolved: true`, `is_outdated: true`) |
| Security review request | comment 6135990857 `@codex security review` at 01:19:59Z (§6) |
| Codex review of `e13516b` | review 5497764776, `COMMENTED`, at 01:23:11Z; summary row "Code Review — Completed — `e13516b` — Manual request"; two inline findings, R-2 and R-3 |
| CI on `e13516b` | run 38331608172, started 01:19:54Z. It is stale because R-2 and R-3 require a correction. It is not a gate and is not cancelled by hand; this push supersedes it (`cancel-in-progress` for pull requests). It was still in progress at 01:34Z, when this record was written |

## 3. Review matrix (this round)

| # | Reviewer / location | Revision | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-2 | Codex, review 5497764776, thread `PRRT_kwDOP103ks6rrP8b` (r4253817828), `tools/evidence/hdapi_v2_boundary_analyzer.py` lines 2045–2050, P2 | `e13516b` | "Reject helpers replaced through dynamic global writes": a route that runs `globals()["_respond"] = lambda emit_fn: Response(b"raw")` before `return _respond(emit_fn)` is accepted, while the parent analyzer reported it | substantive in-scope correction (addendum 2.2 binding requirement "bypass detection is not weakened") | corrected (§4) |
| R-3 | Codex, review 5497764776, thread `PRRT_kwDOP103ks6rrP8g` (r4253817837), `tests/arch/test_arch_guards.py` line 39, P2 | `e13516b` | "Detect blueprint registrations invoked through aliases": `register = app.register_blueprint; register(bp)` outside `adapter/` passes the narrowed PR-30 regex, while the base guard caught it | substantive in-scope correction (a PR-30 test-only fix lost a real violation; PF02 HDE Architecture §2.1 makes `adapter/` the single HTTP home) | corrected (§4) |

**Verification by reproduction.**
- R-2. Nine probe shapes ran against base `e3a5ed4` / `c5116f7` / correction: an in-route `globals()` write (R-2's case), a module-level `globals()` write, `globals().update`, `vars()`, `setattr(sys.modules[__name__], …)`, `sys.modules[__name__].__dict__[…]`, `exec`, `importlib.import_module(__name__)._respond = …`, and a control with no dynamic access.
  - Every dynamic shape is reported at the base, not reported at `c5116f7`, and reported after the correction.
  - The control is reported at the base and accepted at `c5116f7` and after the correction, as planned.
  - Production loci are `['adapter/http_reader.py:reader_post']` at the base, and `[]` at `c5116f7` and after the correction.
- R-3. A synthetic sample matrix ran through the base regex, PR-30's regex and the corrected guard (§5 L-14). The base and the corrected guard detect the aliased registration; PR-30's regex does not.

## 4. Correction (one commit)

**R-2: `tools/evidence/hdapi_v2_boundary_analyzer.py`.** Inside `_adapter_routes_without_presenter` only, the presenter-bound helper shape gains a module-wide precondition, condition 8. The module has no dynamic namespace access:
- no name `globals`, `vars`, `locals`, `exec`, `eval`, `compile`, `setattr`, `delattr`, `__import__` or `__builtins__`;
- no `.__dict__` or `.__globals__`;
- no `sys.modules`, and no import of `builtins` or `importlib`.

This closes R-2's case and the other same-module ways to replace the helper or its defaults at run time. It only narrows the new shape. The production adapter loci use none of these, so production loci stay `[]`. The docstring states the condition. The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `c5116f7`, and every import node is identical (B-3, B-5).

**R-2 test: `tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains two shapes, `replaced_through_globals` and `replaced_through_module_setattr`, and its docstring names them. It is still one test function, 189 functions and 300 collected items (B-4).

**R-3, and the same root cause in the import guards: `tests/arch/test_arch_guards.py` and `tests/epic003/test_legacy_imports_denied.py`.** PR-30 removed each guard's false positives by narrowing a regex. Narrowing a regex also drops real violations. The guards now use `ast`:
- **Route registration** (`test_blueprints_only_in_adapter`) flags any use of `add_url_rule` or `register_blueprint`: a call, an alias such as `register = app.register_blueprint`, or a `getattr`, `attrgetter` or `methodcaller` lookup by name. A string that only mentions the name, as the three `tools/evidence` analyzers do, is not flagged.
- **Legacy imports** (`test_no_legacy_imports_in_active_code` and `test_legacy_imports_denied`) flag any absolute `import` or `from` of `core`, `server` or `adapters`. That includes compound lines such as `try: import core`, `x = 1; import adapters` and `import os, core`. A qualified current import such as `from engine.core import core` is not flagged.
- **Unparsable files** fall back to the base's unnarrowed textual patterns, so nothing the base caught there is lost. Two tracked files do not parse: `scripts/scratch.py` and its `.audit_src/` copy, which are Markdown notes.

The emitter check (`test_handlers_cli_use_single_emitter_path`) is unchanged. Its scope narrowing to `engine/http/` and `engine/cli/` is plan v1.1 §7 row 16's approved approach and drops no product home: the other `/cli/` trees are `tools/cli/` and `scripts/cli/`.

## 5. Local validation of the correction

Common conditions as v1.1 §6:
- Python 3.12.3 venv with CI's install; pytest 8.4.2; `ruby` 3.3.6;
- `env -i` closed rails, with every credential variable unset;
- candidate tree `f8672952c5dd0b1b0e3594bf544599f43a405049`, run through a local candidate commit object `905af16` (never pushed). The correction commit `ea4d72e` has the same tree.

| # | Check | Result |
| :- | :- | :- |
| L-13 | R-2 probe, 9 shapes, base / `c5116f7` / correction (§3) | every dynamic shape: reported / not reported / reported; control: reported / accepted / accepted; production loci: reported / `[]` / `[]` |
| L-14 | Guard sample matrix: base regex / PR-30 regex / corrected guard, 12 import and 9 registration samples | Real violations (detected by base / PR-30 / corrected): `try: import core`, `x = 1; import adapters`, `if True: from server import y`, unparsable `import core`, an aliased registration, `getattr(app, 'register_blueprint')`, `operator.methodcaller('add_url_rule', …)`: 1 / 0 / 1 each. `import os, core`: 0 / 0 / 1. The plain forms: 1 / 1 / 1. False positives (`from engine.core import core`, comment and string mentions, the analyzers' name sets and `endswith('.add_url_rule')`): the base flags them, the corrected guard flags none, PR-30 flags one (a commented-out call) |
| L-15 | Planted violations in throwaway worktrees (an aliased registration and `try: import core` under `tools/`; `x = 1; import server` under `engine/`), corrected candidate / `c5116f7` | 3 failed, 1 passed (the emitter test, untouched) / 4 passed. The corrected guards catch what PR-30's missed |
| L-16 | The two analyzer tests and the two guard files on the working tree | 6 passed |
| L-17 | Negative control: the corrected negative test against the `c5116f7` analyzer | 1 failed (`AssertionError: replaced_through_globals`), as intended |
| L-18 | `ast` confinement: analyzer base → correction and `c5116f7` → correction; test file `c5116f7` → correction | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-19 | `git diff --check` | exit 0 |
| L-20 | Classifier dry run, `--base e3a5ed4 --head 905af16 --event-name pull_request` | exit 0; `selected_lanes`; seven lanes; 102 paths; 163 targets, identical to v1.1's list |
| L-21 | Detached worktree of the candidate: `tests/evidence/test_hdapi_v2_contract_inventory.py` alone; pinned suites plus the ownership and architecture tests; the two guard files | 300 passed (95.9 s); 319 passed (48.1 s); 4 passed (3.9 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker; no `tmp_boundary_test/` |
| L-22 | Changed-test step exactly as `ci.yml` runs it, 163 targets | 3,262 passed in 376.3 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

## 6. Codex security review

| Fact | Evidence |
| :- | :- |
| At PR open | the Codex summary (comment 6135675652) has shown only a **Code Review** row since 00:55Z. No Security Review row has appeared on #627 |
| Request | comment 6135990857 `@codex security review`, once, at 01:19:59Z. Codex reacted 👀, then ran a **Code Review** with trigger "Manual request" (01:20:15Z–01:23:11Z). The summary still has no Security Review row |
| Precedent | on amthorn78/glow-hdengine-v2#501, the Security Review row came from "PR opened". A later `@codex security review` comment there was answered by a code-review comment ("Codex Review: Didn't find any major issues…") |
| State | Codex security review evidence for #627: **not produced** at record time. PR-35 does not request it again on this head, because the one request produced a code review. Whether it arrives, and what readiness does without it, is recorded in v1.3 |

## 7. In-flight decisions (this round)

| ID | Decision | Why it is necessary for the approved scope | Tested |
| :- | :- | :- | :- |
| IF-3 | R-2 is closed by a module-wide no-dynamic-namespace-access precondition, not by matching `globals()["_respond"]` alone | Repeated runtime-replacement findings (R-1, R-2) share one root cause: the new shape trusts the module's static text. Every same-module dynamic mechanism can replace the helper, so the precondition covers them all. It only narrows, and production uses none of them | L-13, L-16, L-17, L-21 |
| IF-4 | The legacy-import guards in both files move to `ast` with R-3's registration guard, although Codex flagged only the registration guard | Same root cause as R-3: PR-30's anchored regex drops real legacy imports on compound lines (L-14), which the base caught and PF02 HDE Architecture §2.1 forbids. Test-only, in files the PR already changed | L-14, L-15, L-21 |
| IF-5 | Unparsable files fall back to the base's unnarrowed textual patterns | Keeps the guards fail-closed for text `ast` cannot read (`scripts/scratch.py`), so nothing the base caught there is lost | L-14 (unparsable samples) |
| IF-6 | The emitter-scope narrowing is kept | It is plan v1.1 §7 row 16's approved approach and drops no product home (§4) | L-21 |

## 8. PR_REMOTE_ACTION_LEDGER (this round)

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| 01:19:47 | First corrective push | `68d9207..e13516b`, verified (§2) | done |
| 01:19:57 | Reply on R-1, then resolve its thread | r4253803611; `PRRT_kwDOP103ks6rq-UC` resolved | done |
| 01:19:59 | `@codex security review` | comment 6135990857 | produced a code review (§6) |
| 01:23:11 | Codex review of `e13516b` read | review 5497764776; R-2, R-3 | read |
| ~01:24–01:40 | R-2/R-3 reproduction, correction, L-13 to L-21 | §5 | pass |
| 01:29:32–01:35:50 | Changed-test step, 163 targets | L-22 | 3,262 passed; clean |
| this push | Correction commit and this record's commit, one push | verified by `git ls-remote` and a PR read; recorded in v1.3 | pending verification |
| after the push | Reply on R-2 and R-3 naming the correction commit, then resolve both threads | GitHub | pending |

**Remaining useful local action:** none.

**Next evidence actions:**
- verify the push;
- reply on and resolve R-2 and R-3;
- read the Codex review of the new head (re-review on new commits) and any security review;
- read CI on the new head;
- check mergeability.

## 9. Unresolved items and owners (additions to v1.1 §10)

| Item | Owner |
| :- | :- |
| Codex security review on #627 (§6) | PR-35 records it if it arrives; the readiness consequence is recorded in v1.3 |
| CI, the Codex review and mergeability on the new head | PR-35 |

## 10. Canon relied on (additions to v1.1 §11)

| Source | Sections read | Used for |
| :- | :- | :- |
| PF02-Canon-HDE-Architecture v2.4.6 | §2.1 "Components & responsibilities (single homes)", including "Deny-list (normative)": `core/`, `server/`, `adapters/` "MUST NOT exist or be imported on public paths … CI MUST fail on imports from these paths"; `adapter/` is the single HTTP home, and mounting stays adapter-owned | R-3 and IF-4: the guards must keep real violations failing |
| PF10-HDE-Build-Notes v13.5.3 | addendum 2.2, Approved delta (RP-1) item 2 and Binding requirements (read in full, as in v1.1) | R-2: bypass detection is not weakened; the correction stays in `_adapter_routes_without_presenter` |
| PF19-Canon-Glow-QA-Guide v3.0.6 | §13.14 | R-2: boundary proof is conservative and fails closed |
| In-flight documents | plan v1.1 §7 row 16 and plan v1.0 line 257 (the guard fix's approved approach); Implementation Plan v1.1 line 132 (reviewer chain: "Codex code review and security review on the PR") | IF-4, IF-6 and §6 |

## 11. Recovery

If this session is interrupted:
- **This record was pushed:** re-enter PR-35 in its dedicated session from this file. Verify the remote head, then continue at §8's next evidence actions.
- **This record was not pushed:** the correction is on the local `claude/elegant-mayer-y6ppap`. Re-run L-21, then push the correction and this record together.

No second PR or branch is created.
