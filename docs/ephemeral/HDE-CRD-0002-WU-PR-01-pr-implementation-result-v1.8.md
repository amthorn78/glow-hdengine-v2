---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.8.md
artifact_version: "1.8"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review correction and merge readiness); this record is the checkpoint for PR-35's eighth corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.7.md (v1.7, PR-35 checkpoint for the seventh corrective push; preserved unchanged). Lineage and facts recorded in v1.1 to v1.7 are not repeated here
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
entry_head_for_this_push: a22be49917fcc14b832bcad9f4527a7809496ad8 (the v1.7 checkpoint commit; its parent 02dfdde is the seventh correction)
correction_commit: 34dbc7059fffd8aeaad6c339de1044959e8b659e ("fix(evidence): helper presenter proof verifies the owner of the view's route decorators"; parent a22be49; tree 8cccb4db27eada26a206c8728f9aebeaab8fdb77, the exact tree every §5 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.9.md
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.8 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The seventh corrective push (v1.7) was verified, and its review thread was answered and resolved.

The Codex code review of the resulting head `a22be49` raised one P2 finding in the analyzer, R-13: the view-decorator condition trusted a decorator by its name suffix. PR-35's probe found seven further shapes of the same kind (R-13b). One correction commit closes all of them (§4).

Still open:
- CI on the head this push creates;
- the Codex code review of that head;
- mergeability.

The Codex security review stays settled (v1.6 §3).

This record returns no PR-35 result. It claims no merge readiness, QA verdict, acceptance, PF09 movement or closure.

## 2. Seventh corrective push, verified

| Fact | Evidence |
| :- | :- |
| Push | `f134651..a22be49` at 03:49:01Z. `git ls-remote` gave `a22be49917fcc14b832bcad9f4527a7809496ad8`, and `main` was unchanged at `e3a5ed4` |
| R-12 thread | reply r4254516219 naming `02dfdde`; thread `PRRT_kwDOP103ks6rst6O` resolved (tool-confirmed) |
| Codex code review of `a22be49` | review 5498603058, `COMMENTED`, at 03:53:26Z. The summary row reads "Code Review — Completed — `a22be49` — New commits". There is one inline finding, R-13 |
| CI on `a22be49` | run 38343487439 (`pull_request`, run 3705), started at 03:49:06Z, was still in progress at 04:04:45Z. It is stale because R-13 requires a correction, and this push supersedes it (`cancel-in-progress` for pull requests); it is not cancelled by hand. Run 38342040842 on `f134651` (success, v1.7 §2) is the latest completed hosted run on this PR |

## 3. Review matrix (this round)

| # | Reviewer / location | Revision | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-13 | Codex, review 5498603058, thread `PRRT_kwDOP103ks6rs9z1` (r4254541243), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2393, P2 | `a22be49` | "Verify route-decorator owners before trusting the view": with `@bp.route(...)` above `@evil.route(...)`, where `evil.route` wraps the view in `Response(b"raw")`, the route is accepted because the decorator name ends in `.route`. The parent reports it | substantive in-scope correction (addendum 2.2: bypass detection is not weakened) | corrected (§4) |
| R-13b | PR-35's own probe (after review 5498603058), same file | `a22be49` | seven further shapes that the base reports and `a22be49` accepts (L-76):<br>• a foreign `.route` decorator alone;<br>• a "blueprint" built by another constructor;<br>• a Blueprint subclass;<br>• the blueprint rebound in the factory;<br>• `Blueprint.route` patched;<br>• the blueprint's route method patched through an alias;<br>• the view binding the blueprint's name | substantive in-scope correction | corrected (§4) |

## 4. Correction (one commit, `34dbc70`)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.** The presenter-bound helper shape additionally requires three things.

- **Verified registrar (`is_route_registration`).** The view must carry route decorators. Each one is `<name>.route(...)`, or `.get`, `.post`, `.put`, `.patch` or `.delete`, and `<name>`:
  - is not bound in the view;
  - is bound exactly once in the nearest enclosing scope that binds it, the module included;
  - is bound by constructing an imported Flask app or Blueprint (`flask.Blueprint`, `flask.Flask`, `flask.blueprints.Blueprint` or `flask.app.Flask`), resolved through its import.
- **The view's name is used nowhere else** in the module. That rules out a second registration of the same function.
- **No route-registration method is patched.** No attribute store, attribute delete or constant `getattr` names `route`, `get`, `post`, `put`, `patch`, `delete` or `add_url_rule`.

A view registered only through `add_url_rule` or a class-based view, with no route decorator of its own, leaves the shape.

**Production.** `adapter/http_reader.py` satisfies all three:
- `reader_post` carries only `@bp.route("/reader", methods=["POST"], provide_automatic_options=False)`;
- `bp = Blueprint("reader_api", __name__)` is the single binding of `bp` at the top of `get_reader_api_bp`, with `Blueprint` from `from flask import …`;
- `reader_post` is named nowhere else;
- the module stores no route-method name.

Production loci stay `[]`.

**Confinement.** The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `a22be49`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains three shapes, so it checks 39:
- `foreign_route_decorator_under_blueprint_route`, which is R-13 exactly;
- `blueprint_from_foreign_constructor`;
- `registrar_route_method_patched`.

Its docstring names them. It is still one test function, 189 functions and 300 collected items (B-4).

## 5. Local validation of the correction

Common conditions are as v1.1 §6. The candidate is the correction commit `34dbc70` itself, tree `8cccb4db27eada26a206c8728f9aebeaab8fdb77`.

| # | Check | Result |
| :- | :- | :- |
| L-76 | R-13 probe, 10 shapes, base / `a22be49` / correction | 8 bypass shapes (R-13 and 7 siblings): reported / not reported / reported.<br>Two controls, a factory blueprint and a module-level `Flask` app: reported / accepted / accepted.<br>Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]` |
| L-77 | Every earlier probe (R-1 to R-12b, and the direct-return analogues) on the correction | identical output to `a22be49` for all 13 earlier probe scripts |
| L-78 | The contract-inventory file and both guard files on the working tree | 306 passed |
| L-79 | Negative control: the corrected test file against the `a22be49` analyzer, in a scratch export of `a22be49` | negative test 1 failed (`AssertionError: foreign_route_decorator_under_blueprint_route`, the first new shape), as intended; positive test passed |
| L-80 | `ast` confinement: analyzer base → correction and `a22be49` → correction; test file `a22be49` → correction | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-81 | `git diff --cached --check` | exit 0 |
| L-82 | Classifier dry run, `--base e3a5ed4 --head 34dbc70 --event-name pull_request` | exit 0; seven lanes; 111 paths: v1.7's 110 plus v1.7; 163 targets, identical to v1.1's list |
| L-83 | Detached worktree of `34dbc70`: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (87.9 s); 325 passed (36.2 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-84 | Changed-test step exactly as `ci.yml` runs it, 163 targets, on `34dbc70` | 3,264 passed in 313.4 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

## 6. In-flight decisions (this round)

| ID | Decision | Why it is necessary for the approved scope | Tested |
| :- | :- | :- | :- |
| IF-21 | Verify each view decorator's registrar as a Flask app or Blueprint the module constructs; require the view to be registered by its own decorators only; refuse patching of route-registration methods | R-13 and its siblings are cases the base reports. Addendum 2.2 requires that they stay reported. The rule is confined to the new shape, and the production Reader satisfies it | L-76, L-78, L-79 |

## 7. PR_REMOTE_ACTION_LEDGER (this round)

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| 03:49:01 | Seventh corrective push | `f134651..a22be49`, verified (§2) | done |
| 03:49:15 | Reply on R-12; thread resolved | §2 | done |
| 03:53:26 | Codex code review of `a22be49` read | review 5498603058; R-13 | read |
| ~03:54–04:05 | R-13 and R-13b reproduction; correction; L-76 to L-83 | §5 | pass |
| 03:58:51–04:04:05 | Changed-test step, 163 targets | L-84 | 3,264 passed; clean |
| this push | Correction commit and this record's commit, one push | verified by `git ls-remote` and a PR read; recorded in the next version | pending verification |
| after the push | Reply on R-13 naming `34dbc70`, then resolve its thread | GitHub | pending |

**Remaining useful local action:** none.

**Next evidence actions:**
- verify the push;
- reply on and resolve R-13;
- read the Codex code review of the new head;
- read CI on the new head;
- check mergeability.

## 8. Unresolved items and owners (additions to earlier versions)

| Item | Owner |
| :- | :- |
| OBS-16 (i), new. The general analyzer identifies routes by decorator and `add_url_rule` name suffixes without verifying the registrar object, for every shape it accepts. For example, the base accepts a direct view under `@app.route` and a foreign `@evil.route` that wraps it (checked). The new shape now verifies the registrar | the whole-change IA (analyzer items). No HDE-CRD-0002 unit waits on it |

## 9. Canon relied on (additions to earlier versions)

No new source:
- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (R-13, R-13b);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).

## 10. Recovery

If this session is interrupted:
- **This record was pushed:** re-enter PR-35 in its dedicated session from this file. Verify the remote head, then continue at §7's next evidence actions.
- **This record was not pushed:** the correction is on the local `claude/elegant-mayer-y6ppap`. Re-run L-83, then push the correction and this record together.

No second PR or branch is created.
