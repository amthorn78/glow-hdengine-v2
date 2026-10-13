---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.5.md
artifact_version: "1.5"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review correction and merge readiness); this record is the checkpoint for PR-35's fifth corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.4.md (v1.4, PR-35 checkpoint for the fourth corrective push; preserved unchanged). Lineage and facts recorded in v1.1 to v1.4 are not repeated here
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1)
PR_RETURN_PHASE: none (no rescope is open)
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1 (unchanged)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md (v13.5.3; blob a51bf40a4bcd2cc95653fb5c3e327bf61162aa52; read in full; unchanged)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. No other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED)
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: bb0f85c661b15d328a19f42037b647a502227754 (the v1.4 checkpoint commit; its parent 5c196ad is the fourth correction)
correction_commit: 1d588ded251a3d40c5c65555818e52f647412550 ("fix(evidence): fail-closed reflection precondition and view decorators for presenter-bound helpers (#627 review)"; parent bb0f85c; tree 0e817d088c35fcc8e545d4e8d0f17782bbb14d3f, the exact tree every §5 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.6.md
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.5 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The fourth corrective push (v1.4) was verified, and its two review threads were answered and resolved.

The Codex review of the resulting head `bb0f85c` raised one P2 finding, R-9, in the analyzer. It raised none in the guards, whose fail-closed rewrite in v1.4 held.

R-9 is the fifth helper-replacement variant. The module-level dynamic-access check was still a list of forbidden names. This round replaces it with a fail-closed reflection precondition (§4). PR-35's own probe also found a view-decorator gap (R-9b), corrected in the same commit. That commit is published by the push that carries this record.

Still open:
- CI on the head this push creates;
- the Codex review of that head;
- the Codex security review, still not produced (v1.2 §6);
- mergeability.

This record returns no PR-35 result. It claims no merge readiness, QA verdict, acceptance, PF09 movement or closure.

## 2. Fourth corrective push, verified

| Fact | Evidence |
| :- | :- |
| Push | `218b65d..bb0f85c` at 02:23:54Z; `git ls-remote` = `bb0f85c661b15d328a19f42037b647a502227754`; `main` unchanged at `e3a5ed4` |
| R-7, R-8 threads | replies r4254090395 and r4254090001 naming `5c196ad`; threads `PRRT_kwDOP103ks6rruX1` and `PRRT_kwDOP103ks6rruXz` resolved (tool-confirmed) |
| Codex review of `bb0f85c` | review 5498116305, `COMMENTED`, at 02:31:40Z; summary row "Code Review — Completed — `bb0f85c` — New commits"; one inline finding, R-9. No Security Review row |
| CI on `218b65d` | run 38335070763 completed **`success`** at 02:22:09Z, before the fourth push. It is hosted evidence for the v1.3 correction |
| CI on `bb0f85c` | the run started by the fourth push. It is stale because R-9 requires a correction, and this push supersedes it (`cancel-in-progress` for pull requests); it is not cancelled by hand |

## 3. Review matrix (this round)

| # | Reviewer / location | Revision | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-9 | Codex, review 5498116305, thread `PRRT_kwDOP103ks6rr-XY` (r4254124579), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 1873, P2 | `bb0f85c` | "Reject helper replacement through frame globals": a route that runs `inspect.currentframe().f_globals["_respond"] = _raw` before `return _respond(emit_fn)` is accepted; the parent reports it | substantive in-scope correction (addendum 2.2: bypass detection is not weakened) | corrected (§4) |
| R-9b | PR-35's own probe (after review 5498116305), same file | `bb0f85c` | A non-route decorator on the view (`@_raw_wrap` under `@bp.route`), or a decorated factory, replaces what Flask serves; the shape is accepted. The base reports both | substantive in-scope correction | corrected (§4) |

**Verification by reproduction, base / `bb0f85c` / correction:**
- **R-9 and siblings.** Each is reported / not reported / reported:
  - `inspect.currentframe().f_globals[...]` (R-9);
  - `sys._getframe().f_globals[...]`;
  - a generator frame (`g.gi_frame.f_globals`);
  - `getattr(f, "__globals__")`;
  - `getattr` with a variable attribute name;
  - `import types`, `import gc`;
  - the `__loader__` name.

  A traceback frame (`e.__traceback__.tb_frame.f_globals`) is reported at all three. At `bb0f85c` that is for a different reason: the probe's view contains a `raise`, which the existing return proof rejects. After the correction, the precondition alone also rejects it (`__traceback__` and `tb_frame`).
- **R-9b.** A view with an extra decorator, and a decorated factory: reported / not reported / reported.
- **Controls.** A control module with none of these is reported at the base and accepted at `bb0f85c` and after the correction. Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]`.
- **Earlier probes.** Every R-1 to R-8 probe gives the same results as v1.4 L-33/L-34.

## 4. Correction (one commit)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.**
- **Condition 8, replaced by a fail-closed reflection precondition (R-9).** The presenter-bound shape is accepted only in a module that is reflection-free:
  - **Imports.** Every import's root is in an allowlist: the project packages (`adapter`, `engine`, `presenter`), `flask`, `werkzeug`, and the plain modules production uses (`__future__`, `collections`, `datetime`, `hashlib`, `json`, `os`, `pathlib`, `threading`, `typing`). Relative imports count as project imports.
  - **Attributes.** No dunder attribute other than `__init__`. No frame, generator, coroutine or traceback attribute (`f_globals`, `f_locals`, `f_back`, `f_builtins`, `f_code`, `f_trace`, `gi_frame`, `gi_code`, `cr_frame`, `cr_code`, `ag_frame`, `ag_code`, `tb_frame`, `tb_next`).
  - **Names.** No reflective builtin (`globals`, `vars`, `locals`, `exec`, `eval`, `compile`, `setattr`, `delattr`, `__import__`, `breakpoint`). No dunder name other than `__name__` and `__file__`.
  - **`getattr`/`hasattr`.** Only with a constant ordinary attribute name: not dunder, and not a frame attribute.

  The production `adapter/http_reader.py` satisfies it:
  - its imports are project packages, `flask`, `werkzeug` and the listed plain modules;
  - its only dunder attribute is `__init__`, and its only dunder name is `__name__`;
  - it calls `getattr` only as `getattr(exc, "code", None)`, `getattr(resp, "request", None)` and `getattr(req, "path", "")`.
- **Condition 14, new (R-9b).** The view carries only its route decorators (`.route`, `.get`, `.post`, `.put`, `.patch`, `.delete`), and every enclosing function in its chain is undecorated. Production `reader_post` has only `@bp.route`, and `get_reader_api_bp` is undecorated.
- **Production and confinement.** Production loci stay `[]`. The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `bb0f85c`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains two shapes, `view_wrapped_by_extra_decorator` and `replaced_through_frame_globals`, so it checks 22. Its docstring names them. It is still one test function, 189 functions and 300 collected items (B-4).

## 5. Local validation of the correction

Common conditions are as v1.1 §6. The candidate tree is `0e817d088c35fcc8e545d4e8d0f17782bbb14d3f`, run through a local candidate commit object `51f19c7` (never pushed). The correction commit `1d588de` has the same tree.

| # | Check | Result |
| :- | :- | :- |
| L-44 | R-9 probe, ten shapes, base / `bb0f85c` / correction (§3) | as §3; production loci reported / `[]` / `[]` |
| L-45 | R-9b probe, three shapes, base / `bb0f85c` / correction | view decorator and decorated factory: reported / not reported / reported; control: reported / accepted / accepted |
| L-46 | Every earlier probe (R-1 to R-8) on the correction | unchanged from v1.4 L-33/L-34 |
| L-47 | The two analyzer tests and both guard files on the working tree | 8 passed |
| L-48 | Negative control: the corrected negative test against the `bb0f85c` analyzer | 1 failed (`AssertionError: view_wrapped_by_extra_decorator`, the first new shape), as intended |
| L-49 | `ast` confinement: analyzer base → correction and `bb0f85c` → correction; test file `bb0f85c` → correction | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-50 | `git diff --cached --check` | exit 0 |
| L-51 | Classifier dry run, `--base e3a5ed4 --head 51f19c7 --event-name pull_request` | exit 0; seven lanes; 105 paths; 163 targets, identical to v1.1's list |
| L-52 | Detached worktree of the candidate: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (91.8 s); 325 passed (39.7 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-53 | Changed-test step exactly as `ci.yml` runs it, 163 targets | 3,264 passed in 349.2 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

One intermediate candidate, `3b363a4` (with R-9's correction but without R-9b), passed its side checks (300 and 325 passed, clean). Its full run was stopped when R-9b was found, so it is not relied on.

## 6. In-flight decisions (this round)

| ID | Decision | Why it is necessary for the approved scope | Tested |
| :- | :- | :- | :- |
| IF-14 | Replace the forbidden-name dynamic-access check with a fail-closed reflection precondition (import allowlist, dunder and frame attributes, reflective builtins, constant-name `getattr`) | Five runtime-replacement variants (R-1, R-2, R-3b, R-9 and its siblings) show that single forbidden names cannot cover every introspection path. A module with no reflection capability cannot rewrite its own namespace from inside. The allowlist is calibrated to what production actually uses, so production still passes | L-44, L-46, L-47, L-52 |
| IF-15 | Close R-9b (view and factory decorators) in the same push | Same family; the base reports it; adding it before a reviewer finds it saves a CI and review cycle | L-45, L-48 |

**Remaining limit (recorded, not changed).** Single-module analysis cannot see another module patching this one, for example `http_reader._respond = …` from `wsgi.py`. Nor can it see a project module that hands this one a reflective helper. The base analyzer has the same limit for every shape it accepts, and it is added to OBS-16 as (f).

## 7. PR_REMOTE_ACTION_LEDGER (this round)

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| 02:23:54 | Fourth corrective push | `218b65d..bb0f85c`, verified (§2) | done |
| 02:24:05–02:24:10 | Replies on R-7 and R-8; both threads resolved | §2 | done |
| 02:31:40 | Codex review of `bb0f85c` read | review 5498116305; R-9 | read |
| ~02:32–02:45 | R-9 and R-9b reproduction, correction, L-44 to L-52 | §5 | pass |
| 02:39:54–02:45:45 | Changed-test step, 163 targets | L-53 | 3,264 passed; clean |
| this push | Correction commit and this record's commit, one push | verified by `git ls-remote` and a PR read; recorded in the next version | pending verification |
| after the push | Reply on R-9 naming the correction commit, then resolve its thread | GitHub | pending |

**Remaining useful local action:** none.

**Next evidence actions:**
- verify the push;
- reply on and resolve R-9;
- read the Codex review of the new head;
- read CI on the new head;
- check mergeability;
- settle the security-review state (v1.2 §6).

## 8. Unresolved items and owners (additions to earlier versions)

| Item | Owner |
| :- | :- |
| OBS-16 (f), new: cross-module patching and reflective helpers supplied by other project modules are invisible to single-module analysis, for every shape the analyzer accepts | the whole-change IA (analyzer items). No HDE-CRD-0002 unit waits on it |
| Codex security review on #627 | PR-35 (v1.2 §6) |

## 9. Canon relied on (additions to earlier versions)

No new source:
- PF10-HDE-Build-Notes v13.5.3, addendum 2.2, Binding requirements (R-9, R-9b);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).

## 10. Recovery

If this session is interrupted:
- **This record was pushed:** re-enter PR-35 in its dedicated session from this file. Verify the remote head, then continue at §7's next evidence actions.
- **This record was not pushed:** the correction is on the local `claude/elegant-mayer-y6ppap`. Re-run L-52, then push the correction and this record together.

No second PR or branch is created.
