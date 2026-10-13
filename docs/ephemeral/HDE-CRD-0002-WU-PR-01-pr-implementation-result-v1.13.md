---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.13.md
artifact_version: "1.13"
artifact_state: PR-35 FINAL RECORD, superseding v1.12 as the final record. The PR-35 result is MERGE_PENDING, returned only when v1.9 §2's three predicates hold on the head that adds this file and R-16 is settled (v1.11 §2). A file cannot record the CI run or review of the commit that adds it; the PR-35 return message reports them
phase: PR-35 (review correction and merge readiness), final record
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.12.md (v1.12; preserved unchanged). Everything in v1.9 to v1.12 stands except what §1 to §5 below add or replace
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1)
PR_RETURN_PHASE: none (no rescope is open)
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1 (unchanged)
pf10_ref: as v1.9
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. No other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED). The worker process restarted at the start of this round; the branch, the probe scripts and the earlier logs survived, and nothing was redone from memory
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: 6cf498bbc9c459d07116d80ad3a219fc12224d9b (the v1.12 record commit)
final_code_commit: 65ee506fd3da966435b62e21ef1b113886b04c00 ("fix(evidence): helper presenter proof fails closed on HTTP-exception exits and unverified hook decorators"; parent 6cf498b; tree 58a334c15934faa6c93545eccb1fd7a583ebb9d6, the exact tree every §3 check ran on)
record_commit: the commit that adds this file; its own identity is not written into itself
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.13 (PR-35 final record)

## 1. Result

**PR-35 result: `MERGE_PENDING` (Ready to merge), subject to v1.9 §2's predicates on this record's head and to R-16's settlement.** The PR-35 return message reports the evidence. Only Nathan merges. This record establishes no QA verdict, acceptance, PF09 movement or closure.

## 2. Thirteenth review round: R-19 and R-20

**Verification of v1.12's push.**
- The push was `d7a4d74..6cf498b` at 06:24:36Z. `git ls-remote` gave `6cf498bbc9c459d07116d80ad3a219fc12224d9b`, and `main` was unchanged at `e3a5ed4`.
- R-18's thread `PRRT_kwDOP103ks6ruHOl` was answered (r4255384814) and resolved.
- CI on `6cf498b`, run 38356536341, completed **`success`** at 06:43:18Z.
- R-16 (`PRRT_kwDOP103ks6rtqz7`) still waits on the Product Owner's decision, PO-D6.

**Codex code review of `6cf498b`.** Review 5499637189 at 06:31:34Z raised two P2 findings:

| # | Source and thread | Head reviewed | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-19 | Codex 5499637189, `PRRT_kwDOP103ks6rvHyN` (r4255434900), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2143 | `6cf498b` | "Reject HTTP-exception exits in presenter-bound views": a view that calls `abort(403)` or raises a Werkzeug `HTTPException` before `return _respond(emit_fn)` is accepted, although Flask serves Werkzeug's own error page. The parent reports the route | substantive in-scope correction (addendum 2.2). It is a same-module case | corrected (§3) |
| R-19b | PR-35's own probe | `6cf498b` | The general proof spots `abort` only by name suffix, and both `abort` and `raise` only in the body of a function it proves. A direct `abort(403)`, a direct `raise Forbidden()` and an aliased exception class raised in the view were therefore already reported at `6cf498b`. These forms, which the base reports, were accepted:<br>• `abort` imported under another name (`from flask import abort as deny`);<br>• `abort` aliased at module level;<br>• a view, a helper or a before-request hook that calls a module function that aborts;<br>• `request.routing_exception` passed on and re-raised | corrected (§3) | |
| R-20 | Codex 5499637189, `PRRT_kwDOP103ks6rvHyW` (r4255434910), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2321 | `6cf498b` | "Verify decorators that wrap after-request hooks": an `@bp.after_request` hook with an inner decorator that replaces it with a wrapper returning `Response(b"raw")` is accepted, because the hook checks read the original body while Flask registers the wrapper. The parent reports the route | substantive in-scope correction (addendum 2.2). It is a same-module case | corrected (§3) |
| R-20b | PR-35's own probe | `6cf498b` | Siblings that the base reports and `6cf498b` accepts:<br>• an inner decorator on a before-request hook;<br>• an after-request or error-handler hook registered on an object that is not a Flask app or Blueprint;<br>• a hook whose registrar name is rebound;<br>• an app-wide `before_app_request` or `after_app_request` hook on a Blueprint under a non-public prefix (`/internal`). The hook map skips such a hook, so neither hook check saw it | corrected (§3) | |

## 3. Correction (one commit, `65ee506`)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.** The presenter-bound shape now also requires two things.

**No HTTP-exception exit anywhere in the module (`raises_http_exception`).**
- Nothing is named `abort` or `Aborter`, whether by import, name, attribute or constant `getattr`.
- A name the module imports from Werkzeug, other than an exact response class, is used only as the class `isinstance()` tests or an `except` clause catches.
- `routing_exception` is read only as the object `isinstance()` tests.
- No `raise` reaches its exception through a Flask or Werkzeug import.

The rule is module-wide, so it covers the view, the helper, delegates, hooks and every module function they call, and it needs no call graph. A module that only imports `abort` falls outside the shape and is reported, as on the base.

**Every decorated hook is the analyzed hook (`is_hook_registration`).**
- Every function with a hook decorator (`after_request`, `after_app_request`, `before_request`, `before_app_request`, `errorhandler`, `app_errorhandler`) must be one the hook map analyzes.
- It carries exactly one decorator: its registration as `<name>.<hook>` (or `<name>.errorhandler(<key>)`, `<name>.app_errorhandler(<key>)`).
- `<name>` must be a registrar (`is_registrar`): not bound in the hook, and bound exactly once, in the nearest enclosing scope that binds it, by constructing an imported Flask app or Blueprint.
- `is_route_registration` now shares `is_registrar`; its behavior is unchanged (L-114).

The check runs once with the other hook checks, when the shape is first tried.

**Production.** `adapter/http_reader.py` satisfies both rules, and production loci stay `[]`.
- It imports nothing named `abort`.
- It uses `MethodNotAllowed`, its only Werkzeug name, only in `isinstance(request.routing_exception, MethodNotAllowed)`.
- Its three decorated hooks in `create_app` (`@app.errorhandler(404)`, `@app.errorhandler(405)`, `@app.after_request`) each carry one decorator on `app = Flask(__name__)`.

**Confinement.** The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `6cf498b`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains two shapes, so it checks 45:
- `view_aborts_through_alias`, a view that aborts through `abort` imported under another name (R-19);
- `after_request_hook_with_inner_decorator`, which is R-20 exactly.

It is still one test function, 189 functions and 300 collected items (B-4).

**Local validation (common conditions as v1.1 §6).**

| # | Check | Result |
| :- | :- | :- |
| L-112 | R-19/R-20 probe, 10 bypass shapes, base / `6cf498b` / correction | reported / 6 not reported, 4 reported / all reported. Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]`. This probe's two controls import `abort` and `Forbidden` into every shape, so the correction reports them by design; L-113 carries the controls |
| L-113 | Sibling probe, 15 bypass shapes and 2 controls, base / `6cf498b` / correction | 15 bypass shapes: reported / 7 not reported, 8 reported / all reported. Controls (a production-like module with a call-registered 405 hook testing `routing_exception`, an `app` after-request hook and error handler; and a Blueprint with decorated after-request, before-request and error-handler hooks): reported / accepted / accepted |
| L-114 | All 17 earlier probe scripts (R-1 to R-18, direct-return analogues) | identical output to `6cf498b`, fixture paths aside |
| L-115 | The contract-inventory file and both guard files on the working tree; collection | 306 passed; 300 items collected |
| L-116 | Negative control: the corrected test file against the `6cf498b` analyzer, in a scratch export | negative test failed (`AssertionError: view_aborts_through_alias`), as intended; positive test passed. With that shape removed, it failed on `after_request_hook_with_inner_decorator`, so each new shape fails on its own |
| L-117 | `ast` confinement, base → correction and `6cf498b` → correction; test file | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-118 | `git diff --check` on the correction before commit | exit 0 |
| L-119 | Classifier dry run, `--base e3a5ed4 --head 65ee506 --event-name pull_request` | exit 0; seven lanes; 116 paths; 163 targets, identical to v1.1's list |
| L-120 | Detached worktree of `65ee506`: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (111.6 s); 325 passed (45.0 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-121 | OBS-16 (k) probe: a direct view that calls a module function raising `ValueError`, calls a module function that aborts, or reads `request.get_json()`; base / correction | not reported / not reported, all three |
| L-122 | Changed-test step exactly as `ci.yml` runs it, 163 targets, on `65ee506` (06:51:24–06:57:59) | 3,264 passed in 359.4 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

## 4. Hosted CI (additions)

| Head | Run | Conclusion |
| :- | :- | :- |
| `6cf498b` | 38356536341 | **success** at 06:43:18Z. The code tree tested was `0514810`, before the R-19 and R-20 correction |
| this record's head | started by this push | reported in the PR-35 return |

## 5. Decisions and owners (additions)

| ID | Decision | Basis |
| :- | :- | :- |
| IF-25 | For the presenter-bound shape, the module may contain no HTTP-exception exit (§3) | R-19 is a same-module case the base reports (addendum 2.2). A module-wide rule covers every function on the request path without a call graph |
| IF-26 | For the presenter-bound shape, every hook-decorated function must be analyzed by the hook map and carry exactly one decorator, its registration on a registrar | R-20 is a same-module case the base reports (addendum 2.2) |
| PO-D6 (still pending) | R-16 | as v1.11 §5 |

**OBS-16 (k), new.** The presenter-bound shape cannot prove that no other exception escapes:
- An exception that is not an HTTP exception, raised by the module or by imported code, becomes Flask's own 500 page.
- An HTTP exception raised inside imported code is also unseen. Examples are `request.get_json()` raising `BadRequest`, and an `abort` in another module (the cross-module kind PO-D4 records as a limit).

Direct views have these limits on `main`. They also miss a same-module `abort` reached through a called function, which the presenter-bound shape now rejects (L-121). The production Reader's helper catches its own failure types and returns presenter-built errors. The owner is the whole-change IA (analyzer items).

The TypeSafe reading for the PR-40 handoff stays the one in v1.9 §7, for the reasons in v1.10 §5. With R-19 and R-20 the review ran thirteen rounds, and the PR has 117 changed paths.

## 6. Canon relied on (additions)

No new source:
- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (R-19, R-20);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).

## 7. Recovery

As v1.9 §9. The local `65ee506` and this record are pushed together. R-16 waits on the Product Owner's decision.
