---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.3.md
artifact_version: "1.3"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review correction and merge readiness); this record is the checkpoint for PR-35's third corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.2.md (v1.2, PR-35 checkpoint for the second corrective push; preserved unchanged). Lineage and facts recorded in v1.1 and v1.2 are not repeated here
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
entry_head_for_this_push: a7fb3387d84d3884d1c2e296015391fe2907548e (the v1.2 checkpoint commit; its parent ea4d72e is the second correction)
correction_commit: dd91ed37b185d1f604d232f824ce981bc4b69f10 ("fix(evidence,tests): strict presenter-bound helper shape; guard subscript lookups (#627 review)"; parent a7fb338; tree c8ba8215a8c46032e4e78bf348e424b8cd151b5c, the exact tree every §5 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.4.md
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.3 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The second corrective push (v1.2) was verified, and its two review threads were answered and resolved.

The Codex review of the resulting head `a7fb338` raised two new P2 findings:
- **R-4** was already corrected locally before the review arrived.
- **R-5** is corrected here.

PR-35's own adversarial probes found further gaps of the same family, one before that review arrived (R-3b) and three after it (R-6, §3). They are corrected too. One correction commit carries all of it, published by the push that carries this record.

Still open:
- CI on the head this push creates;
- the Codex review of that head;
- the Codex security review, still not produced (v1.2 §6);
- mergeability.

This record returns no PR-35 result. It claims no merge readiness, QA verdict, acceptance, PF09 movement or closure.

## 2. Second corrective push, verified

| Fact | Evidence |
| :- | :- |
| Push | `e13516b..a7fb338` at 01:37:10Z; `git ls-remote` = `a7fb3387d84d3884d1c2e296015391fe2907548e`; the PR read shows head `a7fb338`, 6 commits, 103 files, base `e3a5ed4`, `mergeable_state: clean` (read at 01:37:23Z, before the head's CI registered) |
| R-2, R-3 threads | replies r4253880791 and r4253881173 naming `ea4d72e`; threads `PRRT_kwDOP103ks6rrP8b` and `PRRT_kwDOP103ks6rrP8g` resolved (tool-confirmed) |
| Codex review of `a7fb338` | review 5497865720, `COMMENTED`, at 01:42:39Z; summary row "Code Review — Completed — `a7fb338` — New commits"; two inline findings, R-4 and R-5. No Security Review row |
| CI on `a7fb338` | run 38332996216, started 01:37:33Z. It is stale because R-5 requires a correction. It is not a gate and is not cancelled by hand; this push supersedes it (`cancel-in-progress` for pull requests) |
| CI on `e13516b` | run 38331608172, superseded by the second push |

## 3. Review matrix (this round)

| # | Reviewer / location | Revision | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-3b | PR-35's own probe (before review 5497865720), `tools/evidence/hdapi_v2_boundary_analyzer.py` | `a7fb338` | A same-module self-import replaces the helper: `import <module> as _self; _self._respond = _plain`. The base reports it; `a7fb338` does not | substantive in-scope correction (addendum 2.2: bypass detection is not weakened) | corrected (§4) |
| R-4 | Codex, review 5497865720, thread `PRRT_kwDOP103ks6rrc_Y` (r4253903970), `tests/arch/test_arch_guards.py` lines 44–46, P2 | `a7fb338` | "Detect registrations fetched from class dictionaries": `app.__class__.__dict__["register_blueprint"](app, bp)` is missed by the `ast` guard; the base text check caught it | substantive in-scope correction | corrected (§4); already in PR-35's local candidate before the review arrived |
| R-5 | Codex, review 5497865720, thread `PRRT_kwDOP103ks6rrc_U` (r4253903965), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 1941, P2 | `a7fb338` | "Reject conditional rebinding of presenter-derived aliases": `f = emit_fn; if condition: f = _plain; return Response(f(payload))` is accepted in a presenter-bound helper; the parent reports it | substantive in-scope correction (addendum 2.2: "a helper that emits through any other path" stays reported) | corrected (§4) |

**Verification by reproduction, base / `ea4d72e` / correction:**
- **R-3b.** Self-import (`import …` and `from … import … as _self`) with an attribute store: reported / not reported / reported.
- **R-4.** `app.__class__.__dict__["register_blueprint"](app, bp)` and `type(app).__dict__["add_url_rule"](app, "/x")`: base text check 1, previous `ast` guard 0, corrected guard 1.
- **R-5 and three siblings found by PR-35.** A one-sided alias overwrite (R-5), a one-sided body overwrite, `resp.data = b'raw'` and `resp.set_data(b'raw')`: reported / not reported / reported, each. A control with the production shape (one `body`, one `resp`, a header write) is reported at the base and accepted at `ea4d72e` and after the correction, as planned.
- **Production loci:** `['adapter/http_reader.py:reader_post']` / `[]` / `[]`.

- **R-6 (PR-35's own probe, after review 5497865720).** Three caller-side and module-binding gaps of the presenter-bound shape, each reported at the base and missed by `ea4d72e` and by the R-5 candidate:
  - the view alters the helper's result before returning it (`r = _respond(emit_fn); r.data = b'raw'; return r`), or returns it inside a tuple;
  - the bound argument is rebound on its way to the call: in the view (`if c: emit_fn = _plain`), by a view parameter shadowing it, or by a second binding in the factory;
  - an imported presenter name is rebound in the module (`emit_reader_public_bytes = _plain`), which turns the sanctioned default into a non-presenter.

  Each is reported / not reported / reported, base / `ea4d72e` / correction. Two controls are accepted at `ea4d72e` and after the correction: the view returning `_respond(emit_fn)` directly, and the view returning `_respond()` directly.

**Same shapes in an ordinary helper.** These use an imported presenter, not a bound parameter. The base itself does not report them: an alias overwritten in a branch, a body overwritten in a branch, and `resp.data` mutation. The general return proof is flow-insensitive, and the new shape inherited that. The correction does not change the general proof (IF-8, OBS-16).

## 4. Correction (one commit)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.**
- **Condition 7, widened (R-3b).** The helper's name may appear only as a bare-name callee. Any attribute access by that name, such as `_self._respond`, rejects the shape.
- **Condition 9, new (R-5 and siblings).** The new shape holds the helper body to a stricter, flow-independent standard than the general return proof:
  - a bound parameter is only ever called, never aliased or passed on;
  - every local name has exactly one binding site, counting assignments, augmented assignments, `for`, `with`, `except`, walrus, `del`, `match` captures, `def`, `class`, `import`, `global` and `nonlocal`;
  - no response content or status is replaced after construction: no store or delete of `.data`, `.response`, `.status` or `.status_code`, and no `.set_data` or `.set_json` call.
- **Condition 10, new (R-6).** The view must return the helper call directly (`return _respond(...)`). Assigning, mutating or wrapping the result rejects the shape.
- **Condition 11, new (R-6).** A bound argument that the caller proves (not a direct sanctioned reference) must not be bound anywhere in the view, its parameters included. It must have at most one binding site in each enclosing function's body; in the factory, that one site is the conditional default.
- **Condition 12, new (R-6).** Every name the proof trusts must have exactly one binding site in the module, its import. That covers the imported presenter callables and the presenter modules.
- **Dynamic access, widened.** The module-wide dynamic-access precondition (condition 8) also covers `.__setattr__` and `.__delattr__`.
- **What production uses.** The production Reader satisfies every condition:
  - `reader_post` returns `_production_reader_response(emit_fn)` directly and never binds `emit_fn`;
  - `get_reader_api_bp` binds `emit_fn` once (`emit_fn = emit_reader_public_bytes`);
  - `emit_public` and `emit_reader_public_bytes` are each bound once, by a top-level import;
  - the helper only calls `emit_fn`, binds each local once and writes only headers.

  Production loci stay `[]`.
- **Confinement.** The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `ea4d72e`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains seven shapes, so it now checks 18:
- `replaced_through_module_attribute`, `alias_overwritten_in_branch`, `body_overwritten_in_branch`, `response_data_replaced` and `presenter_name_rebound_at_module`;
- two view-level shapes, `view_mutates_result` and `view_rebinds_argument_in_branch`, built from the same template with a view body in place of `return {call}`.

Its docstring names them. It is still one test function, 189 functions and 300 collected items (B-4).

**`tests/arch/test_arch_guards.py` (R-4).**
- The registration guard also flags a string-keyed subscript lookup of a registration method, such as `__dict__["register_blueprint"]` or `vars(type(app))["add_url_rule"]`. The three `tools/evidence` analyzers keep those names only in dict, set and tuple literals, comparisons and keyword arguments, never as a subscript key or positional call argument (checked by `ast`), so they stay clean.
- A new test, `test_guard_patterns_flag_real_violations_not_mentions`, pins real versus false-positive samples for both guards in CI, including the unparsable-text fallback.

**`tests/epic003/test_legacy_imports_denied.py`.** A new test, `test_legacy_import_check_flags_statements_not_mentions`, pins the same for its import check.

## 5. Local validation of the correction

Common conditions are as v1.1 §6. The candidate tree is `c8ba8215a8c46032e4e78bf348e424b8cd151b5c`, run through a local candidate commit object `dec98b0` (never pushed). The correction commit `dd91ed3` has the same tree.

| # | Check | Result |
| :- | :- | :- |
| L-23 | All analyzer probes on the correction: the R-1 shapes, the related runtime-replacement shapes, the nine R-2 dynamic shapes, the R-3b self-import shapes, the R-5 family and the R-6 shapes (§3) | every shape the base reports and an earlier PR-35 head missed is reported again, including the module-level presenter-name rebinding first recorded as OBS-16 (a). The controls are accepted. The shapes left unreported are those the base does not report in their inline or ordinary-helper form, plus a factory called with a non-presenter emitter, which is single-module-invisible for inline code too (OBS-16) |
| L-24 | Production loci on the correction | `[]` |
| L-25 | The two analyzer tests and both guard files (including the two new guard tests) on the working tree | 8 passed |
| L-25b | R-6 probe, eight shapes, base / an intermediate candidate without conditions 10–12 (`02b5e00`) / correction | the six gap shapes: reported / not reported / reported; the two direct-return controls: reported / accepted / accepted; production loci: reported / `[]` / `[]` |
| L-26 | Negative control: the corrected negative test against the `ea4d72e` analyzer | 1 failed (`AssertionError: replaced_through_module_attribute`, the first new shape), as intended. The R-5 and R-6 shapes are each missed by `ea4d72e` in the probes (L-23, L-25b) |
| L-27 | Planted `app.__class__.__dict__["register_blueprint"](app, bp)` under `tools/`, correction / `ea4d72e` | `test_blueprints_only_in_adapter`: 1 failed / 1 passed. The correction catches what `ea4d72e` missed |
| L-28 | `ast` confinement: analyzer base → correction and `ea4d72e` → correction; test file `ea4d72e` → correction | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-29 | `git diff --cached --check` | exit 0 |
| L-30 | Classifier dry run, `--base e3a5ed4 --head dec98b0 --event-name pull_request` | exit 0; seven lanes; 103 paths; 163 targets, identical to v1.1's list |
| L-31 | Detached worktree of the candidate: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (103.4 s); 325 passed (53.0 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-32 | Changed-test step exactly as `ci.yml` runs it, 163 targets | 3,264 passed in 378.1 s (the 3,262 plus the two new guard tests); exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |

Intermediate candidates:
- `6e66d2f` (without the R-5 correction): its full run was stopped once R-5 arrived;
- `02b5e00` (without conditions 10–12): its full run completed with 3,264 passed, a clean tree and the 11 OBS-4 paths, but it is superseded.

Neither is relied on for the correction.

## 6. In-flight decisions (this round)

| ID | Decision | Why it is necessary for the approved scope | Tested |
| :- | :- | :- | :- |
| IF-7 | Close R-3b, found by PR-35's own probe, in the same push | Same family as R-1 and R-2; the base reports it; addendum 2.2 forbids weakening. Fixing it before a reviewer finds it saves a CI and review cycle | L-23, L-26 |
| IF-8 | Close R-5 with strict body conditions for the new shape only, not by making the general return proof flow-sensitive | Addendum 2.2 keeps "a helper that emits through any other path" reported, so the new shape must not inherit the general proof's flow-insensitivity. Changing the general proof would change verdicts for existing views and ordinary helpers, which B-3 does not authorize; the base's own limits there are recorded as OBS-16 | L-23, L-24, L-25 |
| IF-9 | Add one synthetic-sample test to each guard file | Without it, CI proves only that today's tree is clean, not that the guards still catch the violations PR-30's narrowing lost. Test-only, in files the PR already changed | L-25, L-31 |
| IF-10 | Close the R-6 caller-side and module-binding gaps (conditions 10–12) in the same push, without waiting for a reviewer to find them | Each is reported at the base, and the addendum forbids weakening. The rules stay single-module: they demand static, single binding of every name the proof trusts, and a direct return. The production Reader already has that shape | L-23, L-24, L-25b, L-31 |

## 7. PR_REMOTE_ACTION_LEDGER (this round)

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| 01:37:10 | Second corrective push | `e13516b..a7fb338`, verified (§2) | done |
| 01:37:20–01:37:25 | Replies on R-2 and R-3; both threads resolved | §2 | done |
| ~01:38–01:42 | R-3b probe and the R-4 guard extension, locally | §3 | done |
| 01:42:39 | Codex review of `a7fb338` read | review 5497865720; R-4, R-5 | read |
| ~01:43–01:52 | R-5 reproduction and correction | §5 | pass |
| ~01:52–02:05 | R-6 probe and correction; L-23 to L-31 on `dec98b0` | §5 | pass |
| 01:55:39–02:01:59 | Changed-test step, 163 targets | L-32 | 3,264 passed; clean |
| this push | Correction commit and this record's commit, one push | verified by `git ls-remote` and a PR read; recorded in the next version | pending verification |
| after the push | Replies on R-4 and R-5 naming the correction commit, then resolve both threads | GitHub | pending |

**Remaining useful local action:** none.

**Next evidence actions:**
- verify the push;
- reply on and resolve R-4 and R-5;
- read the Codex review of the new head;
- read CI on the new head;
- check mergeability;
- settle the security-review state (v1.2 §6).

## 8. Unresolved items and owners (additions to v1.1 §10 and v1.2 §9)

| Item | Owner |
| :- | :- |
| OBS-16, extended. Pre-existing analyzer properties, recorded and not changed:<br>(a) module-level rebinding of an imported presenter name: not detected at the base for views and ordinary helpers. The presenter-bound shape now rejects it (condition 12).<br>(d) a factory called with a non-presenter `emit_fn` (`get_bp(_plain)`): not detected, inline at the base or through the helper. The factory parameter is an injection point by design, and cross-module callers are invisible to single-module analysis.<br>(e) the general return proof for views and ordinary helpers is flow-insensitive: an alias or body overwritten in one branch, and `resp.data` or `set_data` mutation, are not reported at the base. The presenter-bound shape is held to conditions 9 and 10 instead | the whole-change IA (analyzer items). No HDE-CRD-0002 unit waits on it |
| Codex security review on #627 | PR-35 (v1.2 §6) |

## 9. Canon relied on (additions to v1.1 §11 and v1.2 §10)

No new source. This round relies on:
- PF10-HDE-Build-Notes v13.5.3, addendum 2.2: Approved delta (RP-1) item 2 ("a helper that emits through any other path … stay reported") and Binding requirements;
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14;
- PF02-Canon-HDE-Architecture v2.4.6 §2.1, already read in full for v1.2.

## 10. Recovery

If this session is interrupted:
- **This record was pushed:** re-enter PR-35 in its dedicated session from this file. Verify the remote head, then continue at §7's next evidence actions.
- **This record was not pushed:** the correction is on the local `claude/elegant-mayer-y6ppap`. Re-run L-31, then push the correction and this record together.

No second PR or branch is created.
