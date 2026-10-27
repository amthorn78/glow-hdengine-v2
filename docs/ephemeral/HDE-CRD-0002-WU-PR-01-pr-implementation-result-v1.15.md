---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.15.md
artifact_version: "1.15"
artifact_state: PR-35 FINAL RECORD, superseding v1.14 as the final record. The PR-35 result is MERGE_PENDING, returned only when v1.9 §2's three predicates hold on the head that adds this file. A file cannot record the CI run or review of the commit that adds it; the PR-35 return message reports them
phase: PR-35 (review correction and merge readiness), final record
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.14.md (v1.14; preserved unchanged). Everything in v1.9 to v1.14 stands except what §1 to §5 below add or replace
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
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED)
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: b98f3151ac1f1c3571101bf77f8841ebd280410f (the v1.14 record commit)
final_code_commit: 97902d8fa6c72e36ba87cbe4c889a99799691bcf ("fix(evidence): helper presenter proof holds request hooks to the helper's body rules"; parent b98f315; tree 9269d85ea7b184d632ca2e4361b63c60c8fec8ee, the exact tree every §3 check ran on)
record_commit: the commit that adds this file; its own identity is not written into itself
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.15 (PR-35 final record)

## 1. Result

**PR-35 result: `MERGE_PENDING` (Ready to merge), subject to v1.9 §2's predicates on this record's head.** The PR-35 return message reports the evidence. Only Nathan merges. This record establishes no QA verdict, acceptance, PF09 movement or closure.

## 2. Fifteenth review round: R-22

**Verification of v1.14's push.**
- The push was `fb95d25..b98f315` at 09:31:06Z. `git ls-remote` gave `b98f3151ac1f1c3571101bf77f8841ebd280410f`, and `main` was unchanged at `e3a5ed4`.
- R-16's thread `PRRT_kwDOP103ks6rtqz7` was answered with PO-D6 (r4256970529) and resolved. R-21's thread `PRRT_kwDOP103ks6rvtTl` was answered with PO-D7 (r4256970952) and resolved.
- CI on `b98f315`, run 38376894574, completed **`success`** at 09:43:40Z.
- The PR description was updated to the state of v1.14. A read-back of the live body matched the source byte for byte (11,555 bytes).

**Codex code review of `b98f315`.** Review 5501613372 at 09:39:53Z raised one P2 finding:

| # | Source and thread | Head reviewed | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-22 | Codex 5501613372, `PRRT_kwDOP103ks6rzD4U` (r4257051096), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2327 | `b98f315` | "Reject conditional rebinding in registered request hooks": a call-registered `before_request` hook that runs `body = emit_public(...); if SAFE_MODE: body = b"raw"; return body` is accepted, because the general return proof reads assignments without flow. Flask serves the hook's bytes instead of the view's. The parent reports the route | substantive in-scope correction (addendum 2.2). It is a same-module case in this PR's own hook acceptance, not the exception kind PO-D7 covers | corrected (§3) |
| R-22b | PR-35's own probe | `b98f315` | Siblings that the base reports and `b98f315` accepts:<br>• the rebound value returned inside `Response(...)`;<br>• an alias of the presenter bytes rebound in a branch;<br>• a hook returning a module function whose own body rebinds in a branch;<br>• a decorated `before_request` hook that rebinds;<br>• a decorated `after_request` hook that returns a new response from a rebound value | corrected (§3) | |

## 3. Correction (one commit, `97902d8`)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.** The presenter-bound shape now requires every before- and after-request hook in the module, decorated or registered by call, to pass `hook_body_is_exact`:
- the hook keeps the helper's body rules (`own_body_is_exact`). Each local name has one binding site, so the general proof's flow-independent reading of assignments holds. The hook also defines nothing nested, replaces no response content or status, builds responses only with an exact response class, and uses presenter-derived values only as the helper may;
- a return that hands off satisfies `delegate_is_exact`: the callee is an undecorated module-level function, named only as a callee, that returns a value on every exit, keeps the same body rules and hands off no further.

The check runs once, with the other hook checks, when the shape is first tried.

**Error handlers are not held to these rules.** They run only when the request fails. PO-D7 and IF-25 cover the exception paths, and the general proof still checks each handler's own returns, as on `main`. The production error handlers in `create_app` return a function nested in `create_app`, which `delegate_is_exact` refuses. That is OBS-16 (l), below.

**Production.** `adapter/http_reader.py` satisfies the rule, and production loci stay `[]`.
- `_governed_405_for_unrouted_methods`, registered by call inside `bp.record(...)`, binds nothing. It returns `None` or hands off to `_reader_method_not_allowed("POST")`. That module-level function binds `body` and `resp` once each and returns `resp`. It is named only as a callee at its three call sites.
- `_strip_etag_on_internal`, the `@app.after_request` hook, binds `req` and `req_path` once each and returns `resp`.

**Confinement.** The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `b98f315`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains `before_request_hook_rebinds_body_in_branch` (R-22), so it checks 46 shapes. It is still one test function, 189 functions and 300 collected items (B-4).

**Local validation (common conditions as v1.1 §6).**

| # | Check | Result |
| :- | :- | :- |
| L-124 | R-22 probe (`probe_round19.py`), 6 bypass shapes and 2 controls, base / `b98f315` / correction | 6 bypass shapes (Codex's exact `return body` form, the five R-22b forms): reported / not reported / reported. Controls (a production-like module with a call-registered 405 hook handing off to an exact function, and a Blueprint with decorated before- and after-request hooks): reported / accepted / accepted. Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]` |
| L-125 | All 21 earlier probe scripts (R-1 to R-21, direct-return analogues, the OBS-16 (k) probe) | identical output to `b98f315`, fixture paths aside |
| L-126 | The contract-inventory file and both guard files on the working tree; collection | 306 passed; 300 items collected |
| L-127 | Negative control: the corrected test file against the `b98f315` analyzer, in a scratch export | negative test failed (`AssertionError: before_request_hook_rebinds_body_in_branch`), as intended; positive test passed |
| L-128 | `ast` confinement, base → correction and `b98f315` → correction; test file | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-129 | `git diff --check` on the correction before commit | exit 0 |
| L-130 | Classifier dry run, `--base e3a5ed4 --head 97902d8 --event-name pull_request` | exit 0; seven lanes; 118 paths; 163 targets, identical to v1.1's list |
| L-131 | Detached worktree of `97902d8`: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (103.8 s); 325 passed (42.4 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-132 | Changed-test step exactly as `ci.yml` runs it, 163 targets, on `97902d8` (09:47:58–09:54:25) | 3,264 passed in 351.6 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

## 4. Hosted CI (additions)

| Head | Run | Conclusion |
| :- | :- | :- |
| `b98f315` | 38376894574 | **success** at 09:43:40Z. The code tree tested was `58a334c`, before the R-22 correction |
| this record's head | started by this push | reported in the PR-35 return |

## 5. Decisions and owners (additions)

| ID | Decision | Basis |
| :- | :- | :- |
| IF-27 | For the presenter-bound shape, every before- and after-request hook in the module must keep the helper's body rules, and a hand-off from it must be exact (`hook_body_is_exact`) | R-22 is a same-module case the base reports (addendum 2.2) |

**OBS-16 (l), new.** An error handler's own returns are checked only by the general return proof, which reads assignments without flow, as it does next to a direct view on `main`. Error handlers run only when the request fails. The owner is the whole-change IA (analyzer items).

Over fifteen Codex reviews, the PR received twenty-one Codex findings (R-1 to R-22; R-6 is PR-35's own).
- Eighteen are corrected.
- R-14 (PO-D4), R-16 (PO-D6) and R-21 (PO-D7) are recorded as limits by Product Owner decision.

The TypeSafe reading for the PR-40 handoff stays the one in v1.9 §7, for the reasons in v1.10 §5. With R-22 the review ran fifteen rounds, and the PR has 119 changed paths.

## 6. Canon relied on (additions)

No new source:
- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (R-22);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).

## 7. Recovery

As v1.9 §9. The local `97902d8` and this record are pushed together.
