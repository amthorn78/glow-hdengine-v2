---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.6.md
artifact_version: "1.6"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review correction and merge readiness); this record is the checkpoint for PR-35's sixth corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.5.md (v1.5, PR-35 checkpoint for the fifth corrective push; preserved unchanged). Lineage and facts recorded in v1.1 to v1.5 are not repeated here
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1)
PR_RETURN_PHASE: none (no rescope is open)
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1 (unchanged)
pf10_ref: governing on main, docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md (v13.5.3; blob a51bf40a4bcd2cc95653fb5c3e327bf61162aa52; read in full). On this branch, docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md (v13.5.4; blob f31b4e04adfd41b2a3b58e95e2dad482004ce063; read in full), supplied by the Product Owner, replaces it (§4)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. No other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED)
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: 4d8a047951056b0be1433382ab78878c8d755591 (the v1.5 checkpoint commit; its parent 1d588de is the fifth correction)
pf10_commit: 9954b118df7abea2c679e233f66e3eed2f9118e2 ("docs(pfcanon): PF10 Build Notes v13.5.4 replaces v13.5.3"; parent 4d8a047)
correction_commit: 731d97097ac0d900312d47ac93f17184e3ddadd3 ("fix(evidence): helper presenter proof resolves response constructors and proves every exit"; parent 9954b11; tree 6172a230841d62c44a53c2c65deee90361b5a977, the exact tree every §6 check ran on, through the earlier commit object 7db5c7e, which has the same tree and parent and was never pushed. Only the commit message was corrected: ten shapes, not eleven)
checkpoint_commit: the commit that adds this file and the deprecation addendum record; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.7.md
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.6 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The fifth corrective push (v1.5) was verified. Its review thread was answered and resolved, and its hosted CI run succeeded.

The Codex review of the resulting head `4d8a047` raised two P2 findings in the analyzer:
- **R-10:** a response constructor accepted by its local name;
- **R-11:** a helper's implicit fall-through exit.

PR-35's own probes found 26 further shapes that the base reports and `4d8a047` accepts (R-11b). One correction commit closes all of them (§5).

The Codex security review is settled. The Product Owner waived it for #627, then deprecated it (§3).

The push that carries this record also carries two other items:
- PF10 v13.5.4 replacing v13.5.3, at the Product Owner's direction (§4);
- the deprecation addendum record.

Still open:
- CI on the head this push creates;
- the Codex code review of that head;
- mergeability.

This record returns no PR-35 result. It claims no merge readiness, QA verdict, acceptance, PF09 movement or closure.

## 2. Fifth corrective push, verified

| Fact | Evidence |
| :- | :- |
| Push | `bb0f85c..4d8a047`, before 02:46:57Z, when the CI run it started was created. The remote branch read `4d8a047951056b0be1433382ab78878c8d755591`, and `main` was unchanged at `e3a5ed4` |
| R-9 thread | reply r4254199332 naming `1d588de`; thread `PRRT_kwDOP103ks6rr-XY` resolved (`is_resolved: true` on read-back) |
| Codex review of `4d8a047` | review 5498232695, `COMMENTED`, at 02:53:09Z. The summary row reads "Code Review — Completed — `4d8a047` — New commits". There are two inline findings, R-10 and R-11, and no Security Review row |
| CI on `4d8a047` | run 38338530975 (`pull_request`, run 3703) completed **`success`** at 02:58:08Z. This is hosted evidence for the v1.5 correction. The head this push creates supersedes it |

## 3. Codex security review: waived for #627, then deprecated

| Step | Record |
| :- | :- |
| Question | PR-35 asked the Product Owner how to treat the security review that Implementation Plan v1.1 §7 names in the reviewer chain and that never ran on #627 (v1.2 §6) |
| Decision for #627 | The Product Owner answered "Waive it for #627" |
| Deprecation | The Product Owner then directed: "This feature (security review) is no longer available. We will need to deprecate it. You may create a PF10 build notes addendum to specify its deprecation." |
| Addendum record | `docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md`, addendum 2.3, committed by this push |
| Canon | The Product Owner supplied PF10 v13.5.4 with addendum 2.3. It is committed unchanged in `9954b11`. Its 2.3 section matches the record's page-ready text once Markdown formatting is normalized (§6, L-66) |

**Effect for #627.** The Codex security review is not obtained or waited on, and its absence is not a gap or blocker. This follows from the Product Owner's direct decisions, and from PF10 addendum 2.3 once #627 merges. The Codex code review is unaffected and remains in the chain.

The v1.2 §6 item is closed. It moves no other security obligation of HDE-CRD-0002, including S19 under WU-PR-05.

## 4. PF10 v13.5.4 on this PR (Product Owner direction)

**Direction.** The Product Owner directed: "add this updated PF10 version to your current PR and remove the old one". This is explicit direction for that particular file under AGENTS.md "PF canon is read-only unless the prompt explicitly directs a change".

**Commit `9954b11`:**
- It renames `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md` to `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md`, with the supplied bytes. A `cmp` with the upload is identical: 33,384 bytes, sha256 `7e285dffb1dd7ab40fa685c8412c63e8784a43a1f38c1adace6816a23bbca881`.
- Against v13.5.3, the file changes only:
  - the version and effective date;
  - one index line for 2.3;
  - addendum 2.3 itself.
- No other PF file changes. No repository code or test names the PF10 file. `ci/checks/check_agents_md_citations.py` excludes PF10 stems.
- `docs/pfcanon/` is a CI-exempt prefix, so the file adds no lane.
- The file keeps v13.5.3's conventions: Markdown hard line breaks as trailing double spaces (77 such lines in v13.5.3, 93 in v13.5.4), and a final `\<eof\>` with no final newline. It is not reformatted.

**Governing version.** Until #627 merges, PF10 v13.5.3 on `main` remains governing canon, and this branch's file is an unmerged proposal (AGENTS.md canon-first rule). Addendum 2.2, which governs WU-PR-01, has the same text in both versions. Its bytes differ only by one newline at the boundary with the new 2.3 section (12,570 and 12,569 bytes).

## 5. Review matrix (this round)

| # | Reviewer / location | Revision | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-10 | Codex, review 5498232695, thread `PRRT_kwDOP103ks6rsOBr` (r4254228722), `tools/evidence/hdapi_v2_boundary_analyzer.py` line 2198, P2 | `4d8a047` | "Require a genuine response constructor": with `from flask import redirect as Response`, `Response(emit_fn(...))` is accepted by its local name. The parent reports the route | substantive in-scope correction (addendum 2.2: bypass detection is not weakened) | corrected (§5.1) |
| R-11 | Codex, review 5498232695, thread `PRRT_kwDOP103ks6rsOBu` (r4254228726), same file, line 2419, P2 | `4d8a047` | "Prove every helper control-flow exit": `if enabled: return Response(emit_fn(...))` with an implicit fall-through is accepted. The parent reports the route | substantive in-scope correction | corrected (§5.1) |
| R-11b | PR-35's own probes (after review 5498232695), same file | `4d8a047` | 26 further shapes that the base reports and `4d8a047` accepts (L-54, L-55), in five groups:<br>• a constructor alias through `make_response` or a module alias;<br>• relative, star and dotted presenter imports;<br>• a call-chain default;<br>• bare-return, generator, async and view fall-through exits;<br>• the response class or a presenter module patched in the module, directly, through an alias, `type()`, `mro()`, `getattr` or `response_class`, and returns handed off to a function that aliases its constructor, alters or hands on its response, is decorated, falls through or is rebound | substantive in-scope correction | corrected (§5.1) |

### 5.1 Correction (one commit, `731d970`)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`, inside `_adapter_routes_without_presenter` only.** The presenter-bound helper shape additionally requires five things.

- **Exact constructors (R-10).** Every response construction in the helper resolves through its import to a Flask or Werkzeug `Response` class:
  - accepted: `flask.Response`, `flask.wrappers.Response`, `werkzeug.Response`, `werkzeug.wrappers.Response` and `werkzeug.wrappers.response.Response`;
  - refused: the local name alone, `make_response`, local subclasses, and anything the general proof treats as a constructor that does not resolve.
- **Every exit returns a value (R-11).** The helper and the view are neither async nor generators. No `return` in their own bodies lacks a value, and each body ends in a `return`. With that, the general proof's check of each explicit return covers every exit but an exception.
- **Hand-off returns.** A helper return that calls another function must reach a function that is:
  - an undecorated module-level function of this module, named only as a callee;
  - one that returns a value on every exit;
  - held to the same body rules;
  - one that hands off no further.

  The body rules are now shared:
  - single binding sites;
  - no content or status replacement;
  - exact constructors;
  - the presenter-derived value-flow allowlist, where sanctioned presenter calls now also count as derived.
- **Exact imports.**
  - A relative or star import leaves the module out of the shape.
  - Each trusted presenter name must be bound by an import that binds what the analyzer's alias says. `import a.b` binds `a`, not `a.b`.
  - Presenter values and defaults must be plain name chains.
- **No same-module patching of what is trusted.**
  - An object that holds a response class, or a module hosting one or hosting a trusted presenter, is only called, subclassed, annotated or read through. That covers any chain ending in `Response` or `response_class`, or resolving to such a class, such a module or a module above one.
  - No attribute store, attribute delete or `getattr` names a trusted presenter or response name.
  - `type()`, `mro()` and typing introspection join the reflection precondition.

**Production.** `adapter/http_reader.py` satisfies every new condition:
- `_production_reader_response` ends in `return resp, 200` and builds `Response(body, status=200)` from `from flask import Response`.
- Its one hand-off, `return _error(...)`, reaches `_error`, which ends in `return resp, code`. `_error` builds `Response(body_bytes, …)` from `emit_public(envelope)` and writes only `resp.headers`.
- The module's attribute stores (`g._log_override`, `self.token`, `self.status`, `resp.content_length` and the like) name no trusted name.
- It uses `Response` only as a callee, a class base and in annotations.

Production loci stay `[]`.

**Confinement.** The `ast` comparison shows only `_adapter_routes_without_presenter` differs from the base and from `4d8a047`, and every import node is identical (B-3, B-5).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The one negative test gains ten shapes, so it checks 31:
- `falls_through_conditionally`;
- `returns_without_value`;
- `generator_helper`;
- `response_class_patched`;
- `response_class_patched_through_type`;
- `presenter_module_patched`;
- `star_import`;
- `hands_off_to_mutating_function`;
- `view_falls_through_conditionally`;
- `constructor_is_another_callable`, which is R-10 exactly.

Its docstring names them. It is still one test function, 189 functions and 300 collected items (B-4).

Correction to v1.5 §4: an `ast` count of the test at `4d8a047` gives 21 shapes, not the 22 v1.5 states.

## 6. Local validation of the correction

Common conditions are as v1.1 §6. The candidate tree is `6172a230841d62c44a53c2c65deee90361b5a977`. The checks ran through the commit object `7db5c7e`, never pushed. The correction commit `731d970` has the same tree and parent.

| # | Check | Result |
| :- | :- | :- |
| L-54 | R-10/R-11 probe, 16 shapes, base / `4d8a047` / correction | 15 bypass shapes (R-10, R-11 and 13 siblings): reported / not reported / reported. Control: reported / accepted / accepted. Production loci: `['adapter/http_reader.py:reader_post']` / `[]` / `[]` |
| L-55 | Patching and hand-off probe, 18 shapes, base / `4d8a047` / correction | 14 bypass shapes: all reported at the base and after the correction; 13 not reported at `4d8a047`. The one reported there, a hand-off to a raw `Response(b'raw')`, is rejected by the general proof.<br>Controls: an exact hand-off and a `werkzeug.wrappers` module constructor are accepted after the correction.<br>Two controls stay reported after the correction, both fail-closed: a body bound inside `try` (the general proof collects no binding inside `try`, unchanged), and a hand-off target also used as a value, refused by design |
| L-56 | Every earlier probe (R-1 to R-9b) on the correction | unchanged from v1.5 L-44 to L-46 |
| L-57 | Direct-return analogues under the general proof, base / correction: aliased constructor, fall-through, patched class | not reported / not reported. The general proof is unchanged; see OBS-16 (g) |
| L-58 | The contract-inventory file and both guard files on the working tree | 306 passed |
| L-59 | Negative control: the corrected test file against the `4d8a047` analyzer, in a scratch export of `4d8a047` | negative test 1 failed (`AssertionError: falls_through_conditionally`, the first new shape), as intended; positive test passed |
| L-60 | `ast` confinement: analyzer base → correction and `4d8a047` → correction; test file `4d8a047` → correction | only `_adapter_routes_without_presenter` differs; import nodes identical; only the negative test function differs; 189 test functions |
| L-61 | `git diff --check 9954b11 7db5c7e -- tools tests` (tree `6172a23`) | exit 0. Over `9954b11` itself, `--check` reports only the supplied PF10 file's Markdown hard-break spaces, kept byte-exact (§4) |
| L-62 | Classifier dry run, `--base e3a5ed4 --head 7db5c7e --event-name pull_request` (tree `6172a23`) | exit 0; seven lanes; 108 paths: 105 plus v1.5 and the PF10 delete and add; 163 targets, identical to v1.1's list |
| L-63 | Detached worktree of `7db5c7e`: the contract-inventory file alone; pinned suites, ownership, architecture and both guard files | 300 passed (87.4 s); 325 passed (34.8 s); `git diff --exit-code` 0; status empty; no tracked file newer than the marker |
| L-64 | Changed-test step exactly as `ci.yml` runs it, 163 targets, on `7db5c7e` | 3,264 passed in 305.5 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 same-byte paths as v1.1 L-12 (OBS-4) |
| L-65 | `cmp` of the committed PF10 v13.5.4 with the supplied upload | identical; 33,384 bytes; sha256 `7e285dff…bbca881` |
| L-66 | Addendum record's page-ready text against PF10 v13.5.4 §2.3, after normalizing links, escapes, emphasis, code marks and table rules | identical (40 lines each) |

## 7. In-flight decisions (this round)

| ID | Decision | Why it is necessary for the approved scope | Tested |
| :- | :- | :- | :- |
| IF-16 | Resolve constructors through their imports, and require every exit of the helper and the view to return a value | R-10 and R-11 are cases the base reports. Addendum 2.2 requires that they stay reported. Both rules are confined to the new shape | L-54, L-58, L-59 |
| IF-17 | Close in the same push the 26 sibling shapes PR-35 found (R-11b): exact imports, hand-off returns, same-module patching | Every one is a case the base reports and `4d8a047` accepts. Closing the group before a reviewer finds each member saves review and CI cycles, as IF-15 did | L-54, L-55 |
| IF-18 | Carry PF10 v13.5.4 in #627 as its own commit | The Product Owner's explicit direction (§4). Kept separate from the correction so that the canon change and the code change review independently | L-65 |

## 8. PR_REMOTE_ACTION_LEDGER (this round)

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| before 02:46:57 | Fifth corrective push | `bb0f85c..4d8a047`, verified (§2) | done |
| 02:47:03 | Reply on R-9; thread resolved | §2 | done |
| 02:53:09 | Codex review of `4d8a047` read | review 5498232695; R-10, R-11 | read |
| 02:58:08 | CI on `4d8a047` read | run 38338530975, `success` | read |
| ~02:56–03:28 | R-10, R-11 and R-11b reproduction; correction; L-54 to L-63, L-65, L-66 | §6 | pass |
| 03:22:13–03:27:20 | Changed-test step, 163 targets | L-64 | 3,264 passed; clean |
| this push | `9954b11`, `731d970` and this record's commit, one push | verified by `git ls-remote` and a PR read; recorded in the next version | pending verification |
| after the push | Replies on R-10 and R-11 naming `731d970`, then resolve both threads | GitHub | pending |

**Remaining useful local action:** none.

**Next evidence actions:**
- verify the push;
- reply on and resolve R-10 and R-11;
- read the Codex code review of the new head;
- read CI on the new head;
- check mergeability.

## 9. Unresolved items and owners (additions to earlier versions)

| Item | Owner |
| :- | :- |
| OBS-16 (g), new. The general return proof, unchanged, accepts three things in a direct view return on `main` (L-57):<br>• a constructor by its local name;<br>• an explicit return with a fall-through exit;<br>• a response class patched in the module.<br>It also binds no name inside `try`. The new shape is held to exact rules, but the general proof's behavior for every other shape is the same as the base's. Objects reached through project modules, or through Flask and Werkzeug APIs that hand back a class under another name, are outside single-module analysis, as OBS-16 (f) records | the whole-change IA (analyzer items). No HDE-CRD-0002 unit waits on it |
| Whether the HDE pull-request review chain needs another source of security review, including the wording of HDE Governance §9.1.1's chain entry (addendum 2.3) | the Product Owner |
| Wording of the GCFPE prompts and skills that name the Codex security review (addendum 2.3) | GCFPE-MGMT-10 and the Product Owner |

## 10. Canon relied on (additions to earlier versions)

- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (R-10, R-11, R-11b).
- PF10-HDE-Build-Notes v13.5.4 (this branch), read in full: addendum 2.3, and addendum 2.2 unchanged.
- PF06-Canon-Change-Process-Guide v2.5.4 §0.1A, and PF03-Reference-Technical-Writing-Best-Practices v1.8.8 "Output" (addendum form).
- PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (the PR implementation chain entry, not reworded).
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).
- AGENTS.md: the canon-first rule (governing canon is `main`'s), and "PF canon is read-only unless the prompt explicitly directs a change".
- In-flight: Implementation Plan v1.1 §7 (reviewer chain, WU-PR-05); WU-PR-01 PR instruction v1.0 §12; detailed PR plan v1.1 §19; Specification v1.1, S19 and RD-1.

## 11. Recovery

If this session is interrupted:
- **This record was pushed:** re-enter PR-35 in its dedicated session from this file. Verify the remote head, then continue at §8's next evidence actions.
- **This record was not pushed:** `9954b11` and `731d970` are on the local `claude/elegant-mayer-y6ppap`. Re-run L-63, then push them with this record and the addendum record.

No second PR or branch is created.
