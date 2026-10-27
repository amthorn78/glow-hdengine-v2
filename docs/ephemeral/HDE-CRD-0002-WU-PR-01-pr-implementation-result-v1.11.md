---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.11.md
artifact_version: "1.11"
artifact_state: PR-35 FINAL RECORD, superseding v1.10 as the final record. The PR-35 result is MERGE_PENDING, returned only when v1.9 §2's three predicates hold on the head that adds this file and R-16 is settled (§2). A file cannot record the CI run or review of the commit that adds it; the PR-35 return message reports them
phase: PR-35 (review correction and merge readiness), final record
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.10.md (v1.10; preserved unchanged). Everything in v1.9 and v1.10 stands except what §1 to §5 below add or replace
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
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED). The session's worker process restarted once during this round; the local branch, the committed correction and the completed validation logs survived, and nothing was redone from memory
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: 2aad4c567a1af819d35696b5afeecdfd9786df1a (the v1.10 record commit)
final_code_commit: 6e6fe7f5410ecd1c8629c9337032a4d3d5f2b19c ("fix(evidence): a call-registered before_request hook may not be a generator"; parent 2aad4c5; tree a8c23a4d14261f91e691610841e1b3dff3f297b0, the exact tree every §3 check ran on)
record_commit: the commit that adds this file; its own identity is not written into itself
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.11 (PR-35 final record)

## 1. Result

**PR-35 result: `MERGE_PENDING` (Ready to merge), subject to v1.9 §2's predicates on this record's head and to R-16's settlement (§2).** The PR-35 return message reports the evidence. Only Nathan merges. This record establishes no QA verdict, acceptance, PF09 movement or closure.

## 2. Eleventh review round: R-16 and R-17

**Verification of v1.10's push.**
- The push was `1fae26b..2aad4c5` at 04:45:20Z. `git ls-remote` gave `2aad4c567a1af819d35696b5afeecdfd9786df1a`, and `main` was unchanged at `e3a5ed4`.
- R-15's thread `PRRT_kwDOP103ks6rtdYV` was answered (r4254818272) and resolved.
- CI on `2aad4c5`, run 38347985687, completed **`success`** at 05:04:38Z.

**Codex code review of `2aad4c5`.** Review 5498939871 at 04:49:24Z raised two P2 findings:

| # | Source and thread | Head reviewed | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-16 | Codex 5498939871, `PRRT_kwDOP103ks6rtqz7` (r4254837644), `tests/arch/test_arch_guards.py` line 70 | `2aad4c5` | "Reject dynamically resolved registration methods": `method = "register_" + "blueprint"; getattr(app, method)(bp)` outside `adapter/` is not flagged by `has_route_registration()` | **not a weakening by this PR.** The guard on `main` is a text search for `add_url_rule\|register_blueprint`, and it misses the same source (checked) | answered (r4254876245). Referred to the Product Owner: record it as a pre-existing limit, or fold constant string expressions in the guard. The thread stays open until decided |
| R-17 | Codex 5498939871, `PRRT_kwDOP103ks6rtqz4` (r4254837639), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2261 | `2aad4c5` | "Reject generator before-request hooks": a call-registered hook containing `yield` returns a generator, which Flask serves instead of the view. The hook was accepted as proven. The parent reports the route | substantive in-scope correction (addendum 2.2) | corrected (§3) |

**Why the options for R-16 have costs.**
- Failing closed on every non-constant `getattr`-family target would flag 11 current files outside `adapter/` whose dynamic lookups are not registrations. Among them are `engine/cli/main.py`, `engine/config/__init__.py` and `tools/qa/qa_harness.py`.
- Folding constant string expressions would close the reported form. A name built from variables would still pass, as it does on `main`.

## 3. Correction (one commit, `6e6fe7f`)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.** `before_hook_is_proven` also refuses a hook whose own body contains `yield`, `yield from` or `await`. The production Reader's hook has none, and production loci stay `[]`.

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains `before_request_hook_generator`, so it checks 42 shapes. It is still one test function, 189 functions and 300 collected items (B-4).

**Local validation (common conditions as v1.1 §6).**

| # | Check | Result |
| :- | :- | :- |
| L-94 | R-17 probe, 4 shapes, base / `2aad4c5` / correction | 3 generator shapes (`yield`, `yield from`, a conditional `yield`): reported / not reported / reported. Control hook returning `None`: reported / accepted / accepted. Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]` |
| L-95 | All 15 earlier probe scripts (R-1 to R-15b, direct-return analogues) | identical output to `2aad4c5` |
| L-96 | The contract-inventory file and both guard files on the working tree | 306 passed |
| L-97 | Negative control: the corrected test file against the `2aad4c5` analyzer, in a scratch export | negative test 1 failed (`AssertionError: before_request_hook_generator`), as intended; positive test passed |
| L-98 | `ast` confinement, base → correction and `2aad4c5` → correction; test file | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-99 | `git diff --cached --check` | exit 0 |
| L-100 | Classifier dry run, `--base e3a5ed4 --head 6e6fe7f --event-name pull_request` | exit 0; seven lanes; 114 paths; 163 targets, identical to v1.1's list |
| L-101 | Detached worktree of `6e6fe7f`: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (99.4 s); 325 passed (38.9 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-102 | Changed-test step exactly as `ci.yml` runs it, 163 targets, on `6e6fe7f` (04:53:55–04:59:58) | 3,264 passed in 331.3 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

## 4. Hosted CI (additions to v1.9 §4 and v1.10 §4)

| Head | Run | Conclusion |
| :- | :- | :- |
| `2aad4c5` | 38347985687 | **success** at 05:04:38Z. The code tree tested was `fbd377f`, before the R-17 correction |
| this record's head | started by this push | reported in the PR-35 return |

## 5. Decisions and owners (additions)

| ID | Decision | Basis |
| :- | :- | :- |
| IF-23 | A call-registered before-request hook must also be neither a generator nor contain `await` | R-17 is a same-module case the base reports (addendum 2.2) |
| PO-D6 (pending) | R-16: record as a pre-existing limit of the text-based guard, or fold constant string expressions | Referred to the Product Owner. The case is not reported on `main` either, so addendum 2.2's "stay reported" requirement does not bind it |

The TypeSafe reading for the PR-40 handoff stays the one in v1.9 §7, for the reasons in v1.10 §5. With R-16 and R-17 the review ran eleven rounds, and the PR has 115 changed paths.

## 6. Canon relied on (additions)

No new source:
- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (R-16 classification, R-17);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).

## 7. Recovery

As v1.9 §9. The local `6e6fe7f` and this record are pushed together. R-16 waits on the Product Owner's decision; a folding change, if chosen, is its own validated commit.
