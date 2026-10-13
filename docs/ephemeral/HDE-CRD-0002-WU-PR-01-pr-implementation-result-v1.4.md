---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.4.md
artifact_version: "1.4"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review correction and merge readiness); this record is the checkpoint for PR-35's fourth corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.3.md (v1.3, PR-35 checkpoint for the third corrective push; preserved unchanged). Lineage and facts recorded in v1.1 to v1.3 are not repeated here
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
entry_head_for_this_push: 218b65d03e5dc5b550fd9933720705ea5daee120 (the v1.3 checkpoint commit; its parent dd91ed3 is the third correction)
correction_commit: 5c196ad32685eb2de11d846a3b08440ef8d585d0 ("fix(evidence,tests): fail-closed presenter-derived value flow; guard stored names and exec text (#627 review)"; parent 218b65d; tree e645350cc8d12f395d466f78ab006a3eee513c3e, the exact tree every §5 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.5.md
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.4 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The third corrective push (v1.3) was verified, and its two review threads were answered and resolved.

The Codex review of the resulting head `218b65d` raised two new P2 findings, R-7 and R-8. Both are corrected in one commit, published by the push that carries this record.

Both findings showed the same root cause in the two checks. Each enumerated forbidden forms: guard mentions in the case of R-7, response mutations in the case of R-8. A blacklist like that has no end. This round therefore makes each check fail closed with an allowlist (§4).

Still open:
- CI on the head this push creates;
- the Codex review of that head;
- the Codex security review, still not produced (v1.2 §6);
- mergeability.

This record returns no PR-35 result. It claims no merge readiness, QA verdict, acceptance, PF09 movement or closure.

## 2. Third corrective push, verified

| Fact | Evidence |
| :- | :- |
| Push | `a7fb338..218b65d` at 02:03:22Z; `git ls-remote` = `218b65d03e5dc5b550fd9933720705ea5daee120`; `main` unchanged at `e3a5ed4` |
| R-4, R-5 threads | replies r4253998789 and r4253998491 naming `dd91ed3`; threads `PRRT_kwDOP103ks6rrc_Y` and `PRRT_kwDOP103ks6rrc_U` resolved (tool-confirmed) |
| Codex review of `218b65d` | review 5497999066, `COMMENTED`, at 02:08:28Z; summary row "Code Review — Completed — `218b65d` — New commits"; two inline findings, R-7 and R-8. No Security Review row |
| CI on `a7fb338` | run 38332996216 completed **`success`** at 01:56:25Z (every step, including the seven lanes and the applicability step), before the third push. It is hosted evidence for the v1.2 correction; the head has since moved |
| CI on `e13516b` | run 38331608172 `cancelled` at 01:37:31Z by the second push (`cancel-in-progress`) |
| CI on `218b65d` | run 38335070763, started 02:03:26Z, still in progress at record time. It is stale because R-7 and R-8 require a correction. It is not a gate and is not cancelled by hand; this push supersedes it |

## 3. Review matrix (this round)

| # | Reviewer / location | Revision | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-7 | Codex, review 5497999066, thread `PRRT_kwDOP103ks6rruX1` (r4254019706), `tests/arch/test_arch_guards.py` lines 47–50, P2 | `218b65d` | "Resolve constant registration names stored in variables": `method = "register_blueprint"; getattr(app, method)(bp)` passes the `ast` guard; the base text check caught it | substantive in-scope correction (PF02 HDE Architecture §2.1: `adapter/` is the single HTTP home) | corrected (§4) |
| R-8 | Codex, review 5497999066, thread `PRRT_kwDOP103ks6rruXz` (r4254019704), `tools/evidence/hdapi_v2_boundary_analyzer.py` lines 2152–2155, P2 | `218b65d` | "Reject indirect response-body mutation in presenter helpers": `resp.response.clear(); resp.response.append(b"raw")` in a presenter-bound helper is accepted; the parent reports it | substantive in-scope correction (addendum 2.2: "a helper that emits through any other path" stays reported) | corrected (§4) |

**Verification by reproduction, base / `218b65d` / correction:**
- **R-8 and siblings.** `resp.response.clear()` / `.append()` (R-8), `resp.response[0] = b'raw'`, an alias copy then mutated (`r2 = resp; r2.response.clear()`), `resp` passed to a module helper that clears the body, `resp` passed to an unproven callable (`print(resp)`), `resp.stream.write(b'raw')`, and a wrapper around the derived response (`return _wrap(Response(emit_fn(...)))`). Each is reported / not reported / reported.
- **Controls.** The production-like control is accepted at `218b65d` and after the correction: one `body`, one `resp`, a statement call of a header-only helper, and a `Content-Length` header write.
- **Production loci.** `['adapter/http_reader.py:reader_post']` / `[]` / `[]`.
- **R-7.** Planted in throwaway worktrees: `method = "register_blueprint"; getattr(app, method)(bp)` and `exec("import core")` under `tools/`. With the corrected guards, both guard tests fail (2 failed). With `218b65d`'s guards, 4 passed: both are missed.

## 4. Correction (one commit)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only. Condition 13 (R-8 and the class) fails closed on how presenter-derived values are used.**

A presenter-derived value is any of:
- a call of a bound parameter;
- a response constructed in the helper (`Response`, `make_response`, with the constructor's name bound once, by its import);
- a local holding one of those.

It may only:
- feed a response constructor or `len()` (a builtin not rebound in the module);
- be assigned once to a single local name, from a call only, never name to name;
- reach `.headers`;
- be returned, alone or as the first element of a returned tuple;
- be passed, in a statement call whose result is discarded, to a module-level helper whose matching parameter is never rebound and is used only for `.headers` and `return`. That helper is itself held to the identity rules: undecorated, bound once, and referenced only as a bare callee.

Any other use rejects the shape. That covers attribute access other than `.headers` (`.response`, `.data`, `.stream`, `.__dict__` …), subscripts, aliasing, wrapping, containers, `yield` and calls of unproven callables.

The production Reader satisfies it, so production loci stay `[]`:
- `body = emit_fn(...)`, then `Response(body, status=200)` and `len(body)`;
- `resp` goes to `_set_reader_200_headers(resp)`, which only writes `resp.headers[...]` and returns `resp`, as a statement call;
- then `resp.headers.pop(...)`, `resp.headers["Content-Length"] = …` and `return resp, 200`.

The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `218b65d`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains two shapes, `response_body_mutated_in_place` and `response_passed_to_mutating_helper`, so it checks 20. Its docstring names them. It is still one test function, 189 functions and 300 collected items (B-4).

**`tests/arch/test_arch_guards.py` (R-7, and the same root cause in the import guard).**
- **Registration guard.** Outside three named static analyzers, any string naming a registration method fails the guard, because a stored name can be looked up at run time. The named analyzers are `tools/evidence/generate_architecture_snapshot.py`, `generate_hdapi_v2_contract_inventory.py` and `hdapi_v2_boundary_analyzer.py`. An `ast` scan shows they are the only files outside `adapter/` that hold such strings (4, 55 and 74 constants). Inside them the names are data, but attribute use, subscript lookups and `getattr`-family lookups still fail. Comments are not code. Text that is not Python keeps the base pattern.
- **Legacy-import guard.** A string holding import text (for `exec`), and a dynamic import of a legacy root (`__import__`, `import_module`), also count. An `ast` scan finds no such string in the tree.
- **Synthetic test.** It is extended with the new real and data samples. Run against `218b65d`'s guard functions, it fails, as intended.

**`tests/epic003/test_legacy_imports_denied.py`.** The same string and dynamic-import rule as the legacy-import guard above, with its synthetic test extended.

## 5. Local validation of the correction

Common conditions are as v1.1 §6. The candidate tree is `e645350cc8d12f395d466f78ab006a3eee513c3e`, run through a local candidate commit object `d8bc30c` (never pushed). The correction commit `5c196ad` has the same tree.

| # | Check | Result |
| :- | :- | :- |
| L-33 | R-8 probe, nine shapes, base / `218b65d` / correction (§3) | the seven gap shapes and the wrapper: reported / not reported / reported; the production-like control: reported / accepted / accepted; production loci: reported / `[]` / `[]` |
| L-34 | Every earlier probe (R-1 to R-6) re-run on the correction | unchanged from v1.3 L-23 and L-25b: each gap shape is reported, the controls are accepted, and production loci are `[]` |
| L-35 | The two analyzer tests and both guard files on the working tree | 8 passed |
| L-36 | Negative control: the corrected negative test against the `218b65d` analyzer | 1 failed (`AssertionError: response_body_mutated_in_place`), as intended |
| L-37 | Negative control: the extended guard synthetic test grafted onto `218b65d`'s guard functions | 1 failed, as intended |
| L-38 | Planted violations (R-7 stored name; `exec("import core")`), on `c755195`, whose guard files are identical to the candidate's (`git diff c755195 d8bc30c` changes one line of the contract-inventory test only) / `218b65d` | 2 failed, 2 passed / 4 passed |
| L-39 | `ast` confinement: analyzer base → correction and `218b65d` → correction; test file `218b65d` → correction | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-40 | `git diff --cached --check` | exit 0 |
| L-41 | Classifier dry run, `--base e3a5ed4 --head d8bc30c --event-name pull_request` | exit 0; seven lanes; 104 paths; 163 targets, identical to v1.1's list |
| L-42 | Detached worktree of the candidate: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (101.0 s); 325 passed (58.3 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-43 | Changed-test step exactly as `ci.yml` runs it, 163 targets | 3,264 passed in 381.6 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

One intermediate candidate, `c755195`, is relied on only for the guard result of L-38. It came before one test shape was corrected. That shape, `response_passed_to_other_function`, passed `resp` to `_plain`. `_plain` never uses its parameter, so the call was not a bypass, and the analyzer rightly accepted it. It was replaced by `response_passed_to_mutating_helper`.

## 6. In-flight decisions (this round)

| ID | Decision | Why it is necessary for the approved scope | Tested |
| :- | :- | :- | :- |
| IF-11 | Close R-8 with a fail-closed allowlist of presenter-derived value uses, not another forbidden form | Four rounds showed a blacklist cannot be completed: decorators, namespace writes, one-sided overwrites and now in-place mutation. An allowlist that the production Reader already meets closes the class while still accepting production. It only narrows the new shape | L-33, L-34, L-35, L-36, L-42 |
| IF-12 | The registration guard fails closed on any registration-name string outside three named static analyzers | Whether a string is a mention or a use cannot be decided statically. Failing closed with named, reviewable exceptions keeps the guard at least as strict as the base for executable content. The base also flagged comments; comments are not code, so they stay clean | L-37, L-38, L-42 |
| IF-13 | The legacy-import guards also flag import text in strings and dynamic imports of a legacy root | Same root cause: `exec("import core")` was caught by the base text check and missed by the `ast` guard. No current file holds such a string, so nothing new fails | L-37, L-38, L-42 |

## 7. PR_REMOTE_ACTION_LEDGER (this round)

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| 02:03:22 | Third corrective push | `a7fb338..218b65d`, verified (§2) | done |
| 02:03:35–02:03:39 | Replies on R-4 and R-5; both threads resolved | §2 | done |
| 02:08:28 | Codex review of `218b65d` read | review 5497999066; R-7, R-8 | read |
| ~02:09–02:25 | R-7/R-8 reproduction, correction, L-33 to L-42 | §5 | pass |
| 02:16:08–02:22:31 | Changed-test step, 163 targets | L-43 | 3,264 passed; clean |
| this push | Correction commit and this record's commit, one push | verified by `git ls-remote` and a PR read; recorded in the next version | pending verification |
| after the push | Replies on R-7 and R-8 naming the correction commit, then resolve both threads | GitHub | pending |

**Remaining useful local action:** none.

**Next evidence actions:**
- verify the push;
- reply on and resolve R-7 and R-8;
- read the Codex review of the new head;
- read CI on the new head;
- check mergeability;
- settle the security-review state (v1.2 §6).

## 8. Canon relied on (additions to v1.1 §11, v1.2 §10 and v1.3 §9)

No new source:
- PF10-HDE-Build-Notes v13.5.3, addendum 2.2: Approved delta (RP-1) item 2 and Binding requirements (R-8);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed);
- PF02-Canon-HDE-Architecture v2.4.6 §2.1, the Deny-list and the single HTTP home (R-7, IF-12, IF-13).

## 9. Recovery

If this session is interrupted:
- **This record was pushed:** re-enter PR-35 in its dedicated session from this file. Verify the remote head, then continue at §7's next evidence actions.
- **This record was not pushed:** the correction is on the local `claude/elegant-mayer-y6ppap`. Re-run L-42, then push the correction and this record together.

No second PR or branch is created.
