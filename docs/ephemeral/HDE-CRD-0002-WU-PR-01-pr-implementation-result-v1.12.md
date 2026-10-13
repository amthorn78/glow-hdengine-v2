---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.12.md
artifact_version: "1.12"
artifact_state: PR-35 FINAL RECORD, superseding v1.11 as the final record. The PR-35 result is MERGE_PENDING, returned only when v1.9 §2's three predicates hold on the head that adds this file and R-16 is settled (v1.11 §2). A file cannot record the CI run or review of the commit that adds it; the PR-35 return message reports them
phase: PR-35 (review correction and merge readiness), final record
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.11.md (v1.11; preserved unchanged). Everything in v1.9 to v1.11 stands except what §1 to §5 below add or replace
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
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED). The worker process restarted during this round as well; the committed correction and the completed validation logs survived, and nothing was redone from memory
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: d7a4d74e80ab783c9a940b158f73adec6f5bf27d (the v1.11 record commit)
final_code_commit: fe924d39bd1c9f0b28bb77ad526017396508b3f0 ("fix(evidence): helper presenter proof requires header-only after_request hooks in the module"; parent d7a4d74; tree 0514810956b61b3a432347a27d900c5638430e7c, the exact tree every §3 check ran on)
record_commit: the commit that adds this file; its own identity is not written into itself
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.12 (PR-35 final record)

## 1. Result

**PR-35 result: `MERGE_PENDING` (Ready to merge), subject to v1.9 §2's predicates on this record's head and to R-16's settlement.** The PR-35 return message reports the evidence. Only Nathan merges. This record establishes no QA verdict, acceptance, PF09 movement or closure.

## 2. Twelfth review round: R-18

**Verification of v1.11's push.**
- The push was `2aad4c5..d7a4d74` at 05:20:54Z. `git ls-remote` gave `d7a4d74e80ab783c9a940b158f73adec6f5bf27d`, and `main` was unchanged at `e3a5ed4`.
- R-17's thread `PRRT_kwDOP103ks6rtqz4` was answered (r4255001503) and resolved.
- CI on `d7a4d74`, run 38350926146, completed **`success`** at 05:39:23Z.
- R-16 (`PRRT_kwDOP103ks6rtqz7`) still waits on the Product Owner's decision, PO-D6.

**Codex code review of `d7a4d74`.** Review 5499154338 at 05:24:40Z raised one P2 finding:

| # | Source and thread | Head reviewed | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-18 | Codex 5499154338, `PRRT_kwDOP103ks6ruHOl` (r4255021453), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2247 | `d7a4d74` | "Reject in-place mutation in decorated after-request hooks": an `@bp.after_request` hook that runs `resp.response.clear(); resp.response.append(b"raw")` and returns `resp` is accepted. The general proof's after-request check sees only attribute stores and `set_data`/`set_json`. The parent reports the route | substantive in-scope correction (addendum 2.2). It is a same-module case | corrected (§3) |
| R-18b | PR-35's own probe | `d7a4d74` | 5 siblings that the base reports and `d7a4d74` accepts:<br>• `getattr(resp, "response")`;<br>• `resp.stream.write`;<br>• an alias then a mutation;<br>• the response passed to a mutating helper;<br>• a `direct_passthrough` store.<br>A `status_code` store was already reported | corrected (§3) | |

## 3. Correction (one commit, `fe924d3`)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.** The presenter-bound shape now requires every decorated after-request hook in the module to leave the body alone (`after_hook_is_header_only`):
- the hook defines nothing nested;
- its response parameter is never rebound;
- the parameter is used only to read a body-free attribute (`headers`, `status_code`, `status`, `mimetype`, `content_type`, `content_length`, `request`) or a constant `getattr` of one, to reach `.headers`, to be returned, or to go to a statement call of a header-only helper.

The check runs once, with the call-registered before-request hooks, when the shape is first tried. Its cache is renamed `registered_hooks_proven`.

**Production.** `adapter/http_reader.py`'s `_strip_etag_on_internal(resp)` satisfies the rule, and production loci stay `[]`. It reads `getattr(resp, "request", None)` and `resp.status_code`, edits `resp.headers`, and returns `resp`.

**Confinement.** The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `d7a4d74`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains `after_request_hook_rewrites_body`, which is R-18 exactly, so it checks 43 shapes. It is still one test function, 189 functions and 300 collected items (B-4).

**Local validation (common conditions as v1.1 §6).**

| # | Check | Result |
| :- | :- | :- |
| L-103 | R-18 probe, 8 shapes, base / `d7a4d74` / correction | 7 mutation shapes: reported / 6 not reported (the `status_code` store already reported) / all reported. Production-like hook control: reported / accepted / accepted. Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]` |
| L-104 | All 16 earlier probe scripts (R-1 to R-17, direct-return analogues) | identical output to `d7a4d74` |
| L-105 | The contract-inventory file and both guard files on the working tree | 306 passed |
| L-106 | Negative control: the corrected test file against the `d7a4d74` analyzer, in a scratch export | negative test 1 failed (`AssertionError: after_request_hook_rewrites_body`), as intended; positive test passed |
| L-107 | `ast` confinement, base → correction and `d7a4d74` → correction; test file | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-108 | `git diff --cached --check` | exit 0 |
| L-109 | Classifier dry run, `--base e3a5ed4 --head fe924d3 --event-name pull_request` | exit 0; seven lanes; 115 paths; 163 targets, identical to v1.1's list |
| L-110 | Detached worktree of `fe924d3`: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (105.0 s); 325 passed (42.1 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-111 | Changed-test step exactly as `ci.yml` runs it, 163 targets, on `fe924d3` (05:44:24–05:51:01) | 3,264 passed in 362.8 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

## 4. Hosted CI (additions)

| Head | Run | Conclusion |
| :- | :- | :- |
| `d7a4d74` | 38350926146 | **success** at 05:39:23Z. The code tree tested was `a8c23a4`, before the R-18 correction |
| this record's head | started by this push | reported in the PR-35 return |

## 5. Decisions and owners (additions)

| ID | Decision | Basis |
| :- | :- | :- |
| IF-24 | For the presenter-bound shape, every decorated after-request hook in the module must be header-only | R-18 is a same-module case the base reports (addendum 2.2). The general proof's own after-request check is unchanged for every other shape, and is added to OBS-16 as (j) |
| PO-D6 (still pending) | R-16 | as v1.11 §5 |

**OBS-16 (j), new.** For every shape but the presenter-bound one, the general return proof's after-request check (`response_param_content_status_safe`) misses in-place mutation through `.response` and similar attributes. The owner is the whole-change IA (analyzer items).

The TypeSafe reading for the PR-40 handoff stays the one in v1.9 §7, for the reasons in v1.10 §5. With R-18 the review ran twelve rounds, and the PR has 116 changed paths.

## 6. Canon relied on (additions)

No new source:
- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (R-18);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).

## 7. Recovery

As v1.9 §9. The local `fe924d3` and this record are pushed together. R-16 waits on the Product Owner's decision.
