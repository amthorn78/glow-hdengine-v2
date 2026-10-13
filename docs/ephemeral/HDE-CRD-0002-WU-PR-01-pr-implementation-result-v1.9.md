---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.9.md
artifact_version: "1.9"
artifact_state: PR-35 FINAL RECORD. The PR-35 result is MERGE_PENDING, returned only when the three predicates of §2 hold on the head that adds this file. A file cannot record the CI run or review of the commit that adds it; the PR-35 return message reports them
phase: PR-35 (review correction and merge readiness), final record
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.8.md (v1.8, PR-35 checkpoint for the eighth corrective push; preserved unchanged). v1.0 (PR-30) and v1.1 to v1.8 (PR-35) are preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1)
PR_RETURN_PHASE: none (no rescope is open)
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1 (unchanged)
pf10_ref: governing on main, docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md (v13.5.3). On this branch, docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md (v13.5.4), supplied by the Product Owner (v1.6 §4)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. No other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED)
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: 496e2c7dc5b864c68652974789130c9a194aa32d (the v1.8 checkpoint commit; its parent 34dbc70 is the eighth and last correction)
final_code_commit: 34dbc7059fffd8aeaad6c339de1044959e8b659e (tree 8cccb4db27eada26a206c8728f9aebeaab8fdb77). Every commit after it changes only docs/ephemeral/
record_commit: the commit that adds this file; its own identity is not written into itself
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.9 (PR-35 final record)

## 1. Result

**PR-35 result: `MERGE_PENDING` (Ready to merge), subject to §2.** The PR-35 return message reports §2's evidence for the head that carries this file. Only Nathan merges. No merge, auto-merge or scheduled merge was requested or performed.

This record establishes no QA verdict, acceptance, PF09 movement or closure. Merge readiness is not QA.

## 2. Merge-readiness predicates

| # | Predicate | State when this record was written |
| :- | :- | :- |
| P-1 | Every review thread is answered and resolved | met. 13 Codex findings over nine reviews, one thread each (R-1 to R-14; R-6 is PR-35's own), plus PR-35's own same-family findings, all answered; every thread resolved (§3) |
| P-2 | Hosted CI is green on the head, all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | the push that carries this file runs CI on the whole PR diff. On `496e2c7` one test outside this PR failed; that run is not green (§4). Checked on the new head by the PR-35 return |
| P-3 | The PR is mergeable against `main` | `main` is unchanged at `e3a5ed4`, and the branch contains it. Checked on the new head by the PR-35 return |

The Codex security review is not a predicate. The Product Owner waived it for #627 ("Waive it for #627") and then deprecated it. PF10 v13.5.4 addendum 2.3, carried on this branch, records the deprecation; the addendum record is `docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md` (v1.6 §3).

## 3. Review matrix (all rounds)

| # | Source and thread | Head reviewed | Finding (short) | Disposition | Correction / record |
| :- | :- | :- | :- | :- | :- |
| R-1 | Codex 5497631947, `PRRT_kwDOP103ks6rq-UC` | `26140fe` | decorated presenter-bound helper | corrected | `c5116f7` / v1.1 |
| R-2 | Codex 5497764776, `PRRT_kwDOP103ks6rrP8b` | `e13516b` | helper replaced through dynamic global writes | corrected | `ea4d72e` / v1.2 |
| R-3 | Codex 5497764776, `PRRT_kwDOP103ks6rrP8g` | `e13516b` | aliased blueprint registration missed by the guard | corrected | `ea4d72e` / v1.2 |
| R-3b | PR-35 probe | `a7fb338` | helper replaced through a same-module self-import | corrected | `dd91ed3` / v1.3 |
| R-4 | Codex 5497865720, `PRRT_kwDOP103ks6rrc_Y` | `a7fb338` | registration fetched from a class dictionary | corrected | `dd91ed3` / v1.3 |
| R-5 | Codex 5497865720, `PRRT_kwDOP103ks6rrc_U` | `a7fb338` | conditional rebinding of a presenter alias | corrected | `dd91ed3` / v1.3 |
| R-6 | PR-35 probe | `a7fb338` | caller-side and module-binding gaps | corrected | `dd91ed3` / v1.3 |
| R-7 | Codex 5497999066, `PRRT_kwDOP103ks6rruX1` | `218b65d` | registration name stored in a variable | corrected | `5c196ad` / v1.4 |
| R-8 | Codex 5497999066, `PRRT_kwDOP103ks6rruXz` | `218b65d` | indirect response-body mutation | corrected | `5c196ad` / v1.4 |
| R-9 | Codex 5498116305, `PRRT_kwDOP103ks6rr-XY` | `bb0f85c` | helper replaced through frame globals | corrected | `1d588de` / v1.5 |
| R-9b | PR-35 probe | `bb0f85c` | extra view or factory decorator | corrected | `1d588de` / v1.5 |
| R-10 | Codex 5498232695, `PRRT_kwDOP103ks6rsOBr` | `4d8a047` | response constructor accepted by local name | corrected | `731d970` / v1.6 |
| R-11 | Codex 5498232695, `PRRT_kwDOP103ks6rsOBu` | `4d8a047` | helper's implicit fall-through exit | corrected | `731d970` / v1.6 |
| R-11b | PR-35 probes | `4d8a047` | 26 identity, exit, patching and hand-off shapes | corrected | `731d970` / v1.6 |
| R-12 | Codex 5498474376, `PRRT_kwDOP103ks6rst6O` | `f134651` | `after_this_request` callback in the helper | corrected | `02dfdde` / v1.7 |
| R-12b | PR-35 probe | `f134651` | 15 Flask response-path and nested-definition shapes | corrected | `02dfdde` / v1.7 |
| R-13 | Codex 5498603058, `PRRT_kwDOP103ks6rs9z1` | `a22be49` | route decorator trusted by name suffix | corrected | `34dbc70` / v1.8 |
| R-13b | PR-35 probe | `a22be49` | 7 registrar shapes | corrected | `34dbc70` / v1.8 |
| R-14 | Codex 5498755857, `PRRT_kwDOP103ks6rtRd9` (r4254671771) | `496e2c7` | an imported function, in another module, called from the helper registers a raw callback | **recorded as a limit, no code change**, by Product Owner decision (§5) | this record |

All 13 Codex threads are resolved. R-14's thread holds the reproduction (r4254677258) and the Product Owner's decision (r4254715038).

**Verification behind the corrections.** Each corrected finding was handled the same way:
- reproduced at the base, at the head the review read, and on the correction;
- validated by the full changed-test step (3,264 passed each time from v1.3 on), the contract-inventory file (300) and the side suites (325);
- checked by a negative control against the previous head's analyzer, and by an `ast` confinement check: only `_adapter_routes_without_presenter` differs, no import line changes, and only the one negative test function changes. The test file keeps 189 functions and 300 collected items.

The final negative test checks 39 bypass shapes. The production Reader analyzes clean at every correction.

## 4. Hosted CI

| Head | Run | Conclusion |
| :- | :- | :- |
| `26140fe` to `bb0f85c` | v1.1 to v1.5 | as recorded there |
| `4d8a047` | 38338530975 | success |
| `f134651` | 38342040842 | success |
| `a22be49` | 38343487439 | superseded by the next push (`cancel-in-progress`); not cancelled by hand |
| `496e2c7` | 38344773095 | **failure**: 1 failed, 3,263 passed in the changed-tests step |
| this record's head | started by this push | reported in the PR-35 return |

**The failure on `496e2c7` is OBS-17, below.** It is not this PR's code:
- the failing test is `tests/qa/test_generate_epic_close_pack.py::test_manifest_reader_rejects_new_report_with_old_manifest`, whose final `--check` returned `CHECK_MODE_MUTATION`;
- neither that test nor `tools/qa/generate_epic_close_pack.py` differs from `main`;
- identical code passed on `f134651` and every earlier head, and in 16 local runs.

**Handling.**
- The PR comment (issuecomment 6138082089) names the check, the likely cause and a proposed patch.
- My request to re-run the failed job was refused (`403 Resource not accessible by integration`).
- The Product Owner chose to let the next push re-run CI. This push is that push.

**Hosted Ruby.** The runner image is ubuntu-24.04, image 20261004.327.1. Ruby is present there: the Ruby-dependent contract-inventory tests pass in hosted CI. The hosted Ruby version is not printed (OBS-12).

## 5. Decisions in this round

| ID | Decision | By | Basis |
| :- | :- | :- | :- |
| PO-D1 | Codex security review waived for #627 | Product Owner, "Waive it for #627" | v1.6 §3 |
| PO-D2 | Codex security review deprecated; PF10 addendum 2.3 | Product Owner | v1.6 §3, §4 |
| PO-D3 | PF10 v13.5.4 replaces v13.5.3 on this PR | Product Owner, "add this updated PF10 version to your current PR and remove the old one" | v1.6 §4 |
| PO-D4 | R-14 recorded as a limit with no code change. Later findings of the same cross-module kind are answered and recorded, not fixed in #627 | Product Owner, after the business impact of three options was set out: record as limit, allowlist production imports, or build cross-module analysis | this record §3 |
| PO-D5 | The CI failure on `496e2c7` is re-run by the next push | Product Owner | §4 |

**Why R-14 cannot be fixed within scope.** The production helper `_production_reader_response` itself calls imported project functions, `resolve_compat_chart` and `identity_meta`. It also calls module functions that call further imports. Refusing imported calls would report the production Reader again. Proving them free of response-path side effects needs cross-module analysis, which the analyzer does for no shape. On `main` the base already accepts the same call in a direct view (checked).

In-flight decisions IF-1 to IF-21 are recorded in v1.1 to v1.8 and are not repeated.

## 6. Unresolved items and owners (carried and new)

| Item | Owner |
| :- | :- |
| OBS-16 (a) to (i), limits of the analyzer's general return proof and route discovery, recorded in v1.1 to v1.8. (f) now also covers R-14: single-module analysis, including imported calls from the helper with response-path side effects | the whole-change IA (analyzer items). No HDE-CRD-0002 unit waits on them |
| OBS-17, new: an intermittent hosted failure of `tests/qa/test_generate_epic_close_pack.py`. Likely cause: git ≥ 2.47 starts automatic maintenance detached after `git commit`, and that background process reads a git control file while the tool's `--check` watches its atime. The proposed patch sets `maintenance.auto=false` and `gc.auto=0` in the test's `_init_repo` (issuecomment 6138082089). It is outside WU-PR-01's scope | QA tool / test owner, through the whole-change IA; Product Owner to route |
| Whether the review chain needs another source of security review; the wording of HDE Governance §9.1.1 (addendum 2.3) | the Product Owner |
| Wording of the GCFPE prompts and skills that name the Codex security review (addendum 2.3) | GCFPE-MGMT-10 and the Product Owner |
| OBS-12, the undeclared `ruby` dependency, and the other plan §17 items | as recorded in v1.0 and v1.1 |

## 7. TypeSafe reading for the PR-40 handoff

The `typesafe-scoring` script (request v6) was run once for the PR-40 session. The Notion row was not written, as the PR-35 handoff directs. The header line, verbatim:

> **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.87 (confidence 0.81); rung probabilities low 0.00, medium 0.02, high 0.17, extra high 0.74, max 0.06, ultracode 0.01. Model probabilities Fable 5.1 0.09, Opus 5.5 0.91 (confidence 0.82). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.02, Opus 5.5 at high 0.15, Opus 5.5 at extra high 0.67, Opus 5.5 at max 0.05, Opus 5.5 at ultracode 0.01, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.02, Fable 5.1 at extra high 0.07, Fable 5.1 at max 0.01, Fable 5.1 at ultracode 0.00. Sent 2026-10-13T04:25:49Z. Nathan picks the cell.

The action text sent was:

> Lineage review (PR-40) by the whole-change implementation architect of pull request #627 for HDE-CRD-0002 work unit WU-PR-01, which Codex code review has already reviewed over nine rounds: about 110 changed files, about 5,000 lines added and 6,400 deleted, spanning the CI workflow and change classifier, 66 retired test files with a ledger, 27 test fixes, a roughly 500-line evidence-analyzer addition confined to one function, a PF10 canon file update and eleven phase records, checked against the approved Specification, Implementation Plan and PR plan with the PR-40 prompt's task list. No live provider run occurs, and QA readiness and closure gates follow.

No agent recommendation of model or effort is given.

**Surface.** PR-40 runs in the continuing whole-change IA session for HDE-CRD-0002. The latest known is https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah; Nathan selects.

## 8. Canon relied on (additions to earlier versions)

- PF10-HDE-Build-Notes v13.5.3 (on `main`): addendum 2.2, Binding requirements (R-14 disposition).
- PF10-HDE-Build-Notes v13.5.4 (this branch): addendum 2.3 (security review not a predicate).
- PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (the PR implementation chain entry).
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed).
- AGENTS.md: the canon-first rule; "Operating routes and authority" (ordinary merges remain Product Owner manual actions); "PR descriptions"; "Evidence attribution, currentness and distinct decisions" (merge readiness, CI and QA are distinct states).
- In-flight: Implementation Plan v1.1 §7 (WU-PR-01, reviewer chain read under addendum 2.3); WU-PR-01 PR instruction v1.0 §12; detailed PR plan v1.1 §19; Specification v1.1, S03 to S05.

## 9. Recovery

If this session is interrupted:
- **This record was pushed:** read CI and the Codex code review on the head that adds it.
  - Both clean: the PR-35 result is `MERGE_PENDING`.
  - A new finding of the cross-module kind: record it under PO-D4.
  - Any other finding, or a failure in this PR's code: re-enter PR-35 and write v1.10.
- **This record was not pushed:** it is on the local `claude/elegant-mayer-y6ppap`. Push it alone.

No second PR or branch is created.
