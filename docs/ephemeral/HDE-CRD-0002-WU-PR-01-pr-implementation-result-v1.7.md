---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.7.md
artifact_version: "1.7"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review correction and merge readiness); this record is the checkpoint for PR-35's seventh corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.6.md (v1.6, PR-35 checkpoint for the sixth corrective push; preserved unchanged). Lineage and facts recorded in v1.1 to v1.6 are not repeated here
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1)
PR_RETURN_PHASE: none (no rescope is open)
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1 (unchanged)
pf10_ref: as v1.6 (governing on main, v13.5.3; on this branch, v13.5.4 supplied by the Product Owner)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. No other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED)
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: f134651bb513689ff53633fadb53f2932f15e452 (the v1.6 checkpoint commit; its parent 731d970 is the sixth correction, whose parent 9954b11 is the PF10 commit)
correction_commit: 02dfdde498679effce85caa4b5af771d9661bca9 ("fix(evidence): helper presenter proof fails closed on Flask response-path registration"; parent f134651; tree 1c00d8f8bd2ee3289a9dc36f9d2fbfb695bf8e1e, the exact tree every §5 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.8.md
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.7 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The sixth corrective push (v1.6) was verified, and its two review threads were answered and resolved.

The Codex code review of the resulting head `f134651` raised one P2 finding in the analyzer, R-12: a per-request response callback registered inside the trusted helper. PR-35's probe found 15 further response-path shapes of the same kind (R-12b). One correction commit closes all of them (§4).

Still open:
- CI on the head this push creates;
- the Codex code review of that head;
- mergeability.

The Codex security review stays settled (v1.6 §3).

This record returns no PR-35 result. It claims no merge readiness, QA verdict, acceptance, PF09 movement or closure.

## 2. Sixth corrective push, verified

| Fact | Evidence |
| :- | :- |
| Push | `4d8a047..f134651` at 03:30:30Z. `git ls-remote` gave `f134651bb513689ff53633fadb53f2932f15e452`, and `main` was unchanged at `e3a5ed4`. A PR read gave head `f134651`, 109 changed files and `mergeable_state` `unstable` while CI ran |
| R-10, R-11 threads | replies r4254414499 and r4254415022 naming `731d970`; threads `PRRT_kwDOP103ks6rsOBr` and `PRRT_kwDOP103ks6rsOBu` resolved (tool-confirmed) |
| Codex code review of `f134651` | review 5498474376, `COMMENTED`, at 03:35:25Z. The summary row reads "Code Review — Completed — `f134651` — New commits". There is one inline finding, R-12 |
| CI on `f134651` | run 38342040842 (`pull_request`, run 3704), started at 03:30:34Z, completed **`success`** at 03:45:33Z. This is hosted evidence for the v1.6 correction and the PF10 commit. The head this push creates supersedes it |

## 3. Review matrix (this round)

| # | Reviewer / location | Revision | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-12 | Codex, review 5498474376, thread `PRRT_kwDOP103ks6rst6O` (r4254438388), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2254, P2 | `f134651` | "Reject nested per-request response callbacks": a helper that registers `@after_this_request` returning `Response(b"raw")` is accepted, and Flask serves the replacement. The parent reports the route | substantive in-scope correction (addendum 2.2: bypass detection is not weakened) | corrected (§4) |
| R-12b | PR-35's own probe (after review 5498474376), same file | `f134651` | 15 further shapes that the base reports and `f134651` accepts (L-67):<br>• `after_this_request` called directly, from a function the helper calls, through `flask.`, or under an alias;<br>• the request context's after-request list;<br>• an after-request hook or error handler registered by call, with a helper that can raise;<br>• the view map replaced;<br>• an `endpoint` registration;<br>• a `request_finished` receiver;<br>• `wsgi_app` middleware;<br>• a `process_response` override;<br>• a nested definition in the helper;<br>• a nested callback in the view or in a hand-off function | substantive in-scope correction | corrected (§4) |

## 4. Correction (one commit, `02dfdde`)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.** The presenter-bound helper shape additionally requires two things.

- **Nothing nested.** The helper, the view and a hand-off function define no nested function, class or lambda (`defines_nothing`). Nothing in those bodies can carry code that runs outside the returns the proof checks.
- **No response-path registration outside the analyzed decorators.** The module names none of the following (`touches_response_path`), whether as a name, an attribute, an import or a constant `getattr` name:
  - `after_this_request` and the request context's `_after_request_functions`;
  - `after_request_funcs`, `view_functions` and `error_handler_spec`;
  - `register_error_handler`;
  - `process_response`, `finalize_request`, `full_dispatch_request`, `handle_user_exception`, `handle_http_exception` and `handle_exception`;
  - `wsgi_app`;
  - `request_finished`.

  Nor does it use `after_request`, `after_app_request`, `errorhandler` or `app_errorhandler` other than as a decorator, which the analyzer proves as a hook. It calls and decorates with no `endpoint`.

**The boundary.** A `before_request` hook registered by call is outside the rule. It runs before every view alike, and the general return proof does not see it either. The production Reader's factory registers one this way: `state.app.before_request(_governed_405_for_unrouted_methods)` inside `bp.record(...)`, for unrouted methods only. This is recorded as OBS-16 (h).

**Production.** `adapter/http_reader.py` satisfies both new conditions:
- the helper, the view and `_error` define nothing nested;
- the module names none of the response-path names;
- its after-request and error-handler hooks are decorators: `@app.errorhandler(404)`, `@app.errorhandler(405)` and `@app.after_request`.

Production loci stay `[]`.

**Confinement.** The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `f134651`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains five shapes, so it checks 36:
- `registers_after_this_request_callback`, which is R-12 exactly;
- `calls_function_registering_callback`;
- `after_request_hook_registered_by_call`;
- `request_finished_receiver`;
- `nested_definition_in_helper`.

Its docstring names them. It is still one test function, 189 functions and 300 collected items (B-4).

## 5. Local validation of the correction

Common conditions are as v1.1 §6. The candidate is the correction commit `02dfdde` itself, tree `1c00d8f8bd2ee3289a9dc36f9d2fbfb695bf8e1e`.

| # | Check | Result |
| :- | :- | :- |
| L-67 | R-12 probe, 18 shapes, base / `f134651` / correction | 16 bypass shapes (R-12 and 15 siblings): reported / not reported / reported.<br>Two controls, a plain module and one with the production-like `bp.record` and call-form `before_request`: reported / accepted / accepted.<br>Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]` |
| L-68 | Every earlier probe (R-1 to R-11b, and the direct-return analogues) on the correction | identical output to `f134651` for every R-1 to R-9b probe; R-10/R-11 and patching/hand-off probes as v1.6 L-54/L-55; direct-return analogues as v1.6 L-57 |
| L-69 | The contract-inventory file and both guard files on the working tree | 306 passed |
| L-70 | Negative control: the corrected test file against the `f134651` analyzer, in a scratch export of `f134651` | negative test 1 failed (`AssertionError: registers_after_this_request_callback`, the first new shape), as intended; positive test passed |
| L-71 | `ast` confinement: analyzer base → correction and `f134651` → correction; test file `f134651` → correction | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-72 | `git diff --cached --check` | exit 0 |
| L-73 | Classifier dry run, `--base e3a5ed4 --head 02dfdde --event-name pull_request` | exit 0; seven lanes; 110 paths: v1.6's 108 plus v1.6 and the addendum record; 163 targets, identical to v1.1's list |
| L-74 | Detached worktree of `02dfdde`: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (90.0 s); 325 passed (35.5 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-75 | Changed-test step exactly as `ci.yml` runs it, 163 targets, on `02dfdde` | 3,264 passed in 308.7 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

## 6. In-flight decisions (this round)

| ID | Decision | Why it is necessary for the approved scope | Tested |
| :- | :- | :- | :- |
| IF-19 | Fail closed on nested definitions in the helper, the view and a hand-off function, and on Flask response-path registration outside the analyzed decorators | R-12 and its siblings are cases the base reports. Addendum 2.2 requires that they stay reported. The rule is confined to the new shape, and the production Reader satisfies it | L-67, L-69, L-70 |
| IF-20 | Leave call-form `before_request` outside the rule | It runs before every view alike and is outside the general return proof on `main`. The production Reader uses it for unrouted methods, so banning it would refuse the production shape without a change in what the view returns | L-67 (production-like control accepted) |

## 7. PR_REMOTE_ACTION_LEDGER (this round)

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| 03:30:30 | Sixth corrective push | `4d8a047..f134651`, verified (§2) | done |
| 03:30:41–03:30:50 | Replies on R-10 and R-11; both threads resolved | §2 | done |
| 03:35:25 | Codex code review of `f134651` read | review 5498474376; R-12 | read |
| ~03:36–03:47 | R-12 and R-12b reproduction; correction; L-67 to L-74 | §5 | pass |
| 03:45:33 | CI on `f134651` read | run 38342040842, `success` | read |
| 03:42:45–03:48:20 | Changed-test step, 163 targets | L-75 | 3,264 passed; clean |
| this push | Correction commit and this record's commit, one push | verified by `git ls-remote` and a PR read; recorded in the next version | pending verification |
| after the push | Reply on R-12 naming `02dfdde`, then resolve its thread | GitHub | pending |

**Remaining useful local action:** none.

**Next evidence actions:**
- verify the push;
- reply on and resolve R-12;
- read the Codex code review of the new head;
- read CI on the new head;
- check mergeability.

## 8. Unresolved items and owners (additions to earlier versions)

| Item | Owner |
| :- | :- |
| OBS-16 (h), new. The general return proof does not see two kinds of response path:<br>• a `before_request` hook registered by call, which can short-circuit any view, such as the production Reader's governed 405 for unrouted methods;<br>• a nested callback or registration inside a view's own body, which the parent accepts for a direct return.<br>The new shape now refuses the second, and the first is route-independent | the whole-change IA (analyzer items). No HDE-CRD-0002 unit waits on it |

## 9. Canon relied on (additions to earlier versions)

No new source:
- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (R-12, R-12b);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).

## 10. Recovery

If this session is interrupted:
- **This record was pushed:** re-enter PR-35 in its dedicated session from this file. Verify the remote head, then continue at §7's next evidence actions.
- **This record was not pushed:** the correction is on the local `claude/elegant-mayer-y6ppap`. Re-run L-74, then push the correction and this record together.

No second PR or branch is created.
