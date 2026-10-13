---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.10.md
artifact_version: "1.10"
artifact_state: PR-35 FINAL RECORD, superseding v1.9 as the final record. The PR-35 result is MERGE_PENDING, returned only when v1.9 §2's three predicates hold on the head that adds this file. A file cannot record the CI run or review of the commit that adds it; the PR-35 return message reports them
phase: PR-35 (review correction and merge readiness), final record
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.9.md (v1.9, the earlier final record; preserved unchanged). Everything in v1.9 stands except what §1 to §5 below add or replace
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
entry_head_for_this_push: 1fae26bf77e56643dc06443bb2b46947a6aac086 (the v1.9 record commit)
final_code_commit: 175bc5663c362db9b40f53bd04428fe51b333a9a ("fix(evidence): helper presenter proof accepts a call-registered before_request hook only when proven"; parent 1fae26b; tree fbd377f9dc973bc38109ea14dfb4acaa3205db26, the exact tree every §3 check ran on)
record_commit: the commit that adds this file; its own identity is not written into itself
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.10 (PR-35 final record)

## 1. Result

**PR-35 result: `MERGE_PENDING` (Ready to merge), subject to v1.9 §2's predicates on this record's head.** The PR-35 return message reports the evidence. Only Nathan merges. This record establishes no QA verdict, acceptance, PF09 movement or closure.

## 2. Tenth review round: R-15

**Verification of v1.9's push.**
- The push was `496e2c7..1fae26b` at 04:28:08Z. `git ls-remote` gave `1fae26bf77e56643dc06443bb2b46947a6aac086`, and `main` was unchanged at `e3a5ed4`.
- R-14's thread `PRRT_kwDOP103ks6rtRd9` carries the reproduction (r4254677258) and the Product Owner's decision (r4254715038), and it is resolved.

**Codex code review of `1fae26b`.** Review 5498842070 at 04:31:43Z raised one P2 finding:

| # | Source and thread | Head reviewed | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-15 | Codex 5498842070, `PRRT_kwDOP103ks6rtdYV` (r4254749534), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2207 | `1fae26b` | "Reject registered before-request response hooks": v1.7's IF-20 left every call-registered `before_request` hook outside the response-path rule. So `bp.before_request(_raw)` serving `Response(b"raw")` was accepted, while the parent reports the route | substantive in-scope correction. It is a same-module case, not the cross-module kind PO-D4 covers | corrected (§3); IF-20 is replaced by IF-22 |
| R-15b | PR-35's own probe | `1fae26b` | 7 siblings that the base reports and `1fae26b` accepts:<br>• an app-level hook;<br>• `before_app_request`;<br>• a hook registered inside `bp.record(...)`;<br>• a lambda hook;<br>• `before_request_funcs`;<br>• an aliased `before_request`;<br>• a hook whose name is also used as a value | corrected (§3) | |

## 3. Correction (one commit, `175bc56`)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.**

**Before-request hooks registered by call.** `<registrar>.before_request(<name>)` and `.before_app_request(<name>)` are accepted only when `<name>` is a function of this module that the general return proof proves as a before-request hook (`before_hook_is_proven`). The function must:
- be undecorated and not async;
- be bound once and define nothing nested;
- be named only as that argument or as a callee;
- have each return either `None` or presenter-backed.

Any other call form fails closed: a lambda, a keyword, more than one argument, or an aliased `before_request`. `before_request_funcs` and `preprocess_request` join the response-path names. The check runs once, when the shape is first tried (`module_alters_response_path()`).

**Production.** `adapter/http_reader.py` registers `_governed_405_for_unrouted_methods` by call, inside `bp.record(_refuse_unrouted_methods)`. That hook returns `None` or `_reader_method_not_allowed("POST")`, which builds `Response(emit_public(error_envelope(...)), status=405)`. The hook is proven, so production loci stay `[]`.

**Confinement.** The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `1fae26b`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains two shapes, so it checks 41:
- `before_request_hook_registered_by_call`, which is R-15 exactly;
- `before_request_hook_lambda`.

It is still one test function, 189 functions and 300 collected items (B-4).

**Local validation (common conditions as v1.1 §6).**

| # | Check | Result |
| :- | :- | :- |
| L-85 | R-15 probe, 10 shapes, base / `1fae26b` / correction | 8 bypass shapes: reported / not reported / reported. Two production-like controls (a `record` hook returning `None`, and one returning a presenter-built 405): reported / accepted / accepted. Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]` |
| L-86 | All 14 earlier probe scripts (R-1 to R-13b, direct-return analogues) | identical output to `1fae26b` |
| L-87 | The contract-inventory file and both guard files on the working tree | 306 passed |
| L-88 | Negative control: the corrected test file against the `1fae26b` analyzer, in a scratch export | negative test 1 failed (`AssertionError: before_request_hook_registered_by_call`), as intended; positive test passed |
| L-89 | `ast` confinement, base → correction and `1fae26b` → correction; test file | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-90 | `git diff --cached --check` | exit 0 |
| L-91 | Classifier dry run, `--base e3a5ed4 --head 175bc56 --event-name pull_request` | exit 0; seven lanes; 113 paths; 163 targets, identical to v1.1's list |
| L-92 | Detached worktree of `175bc56`: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (105.6 s); 325 passed (41.1 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-93 | Changed-test step exactly as `ci.yml` runs it, 163 targets, on `175bc56` | 3,264 passed in 342.5 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

## 4. Hosted CI (additions to v1.9 §4)

| Head | Run | Conclusion |
| :- | :- | :- |
| `1fae26b` | 38346583864 | **success** at 04:42:59Z. All seven lanes succeeded, and the log ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. The changed-tests step, which includes the close-pack test that failed on `496e2c7`, passed (OBS-17: intermittent). The code tree tested was `8cccb4d`, before the R-15 correction |
| this record's head | started by this push | reported in the PR-35 return |

## 5. Decisions and owners (additions to v1.9 §5 and §6)

| ID | Decision | Basis |
| :- | :- | :- |
| IF-22 | Replace IF-20. A call-registered `before_request` hook is accepted only when it is proven as a before-request hook; otherwise the shape fails closed | R-15 is a same-module case the base reports. The production hook is proven, so the narrower rule keeps production clean without the blanket exclusion |

OBS-16 (h) is narrowed accordingly. The general return proof still does not see hooks registered by call for direct views, but the new shape now proves them.

The TypeSafe reading for the PR-40 handoff stays the one in v1.9 §7. Its action text says the PR was reviewed over nine rounds; with R-15 it was ten, and the PR now has 113 changed paths, still "about 110". The PR-35 handoff allows one reading per handoff, so it is not re-run.

## 6. Canon relied on (additions)

No new source:
- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (R-15);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).

## 7. Recovery

As v1.9 §9. The local `175bc56` and this record are pushed together.
