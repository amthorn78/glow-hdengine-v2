---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.1.md
artifact_version: "1.1"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review correction and merge readiness); this record is the checkpoint for PR-35's first corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; blob 3bfe71d7f69778131f86db46418955914f243681). Preserved unchanged; this v1.1 is its PR-35 successor in the same lineage
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
work_unit_title: CI coverage of every test file (PR; Distillation; S03, S04, S05)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1; blob dbb9a56a91dc10eefd32a8cdf66abf20535564a4)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0.md (RS-20, APPROVE)
REMEDIATION_REVIEW_ID: none
PR_RETURN_PHASE: none (no rescope is open)
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md (v13.5.3; blob a51bf40a4bcd2cc95653fb5c3e327bf61162aa52; sha256 bcb0b438585c99a3a7333f2766a3c960cd381571f449a38eca6c75464c100c7d; read in full by this PR-35 session; unchanged on main e3a5ed4 and on the branch)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md § 2.2 (controlled PF10); record docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0 (Nathan's PR-30 invocation for plan v1.1). PR-35 continues under it; no other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2; session_disposition NEW_DEDICATED (top-level session Nathan created)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15Z; read in full)
primary_skill: glow-hde-pr-development (revision 1.4.0)
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, not draft, base main e3a5ed4)
entry_head: 68d92075031edf105ffe4f4024482c0dd736e8a9 (PR-30 result commit; parent 26140fee1a7c169694bf4d46bc436bd5495fde91)
correction_commit: c5116f7c225828a5d59d272267fc4d2fc580ed30 ("fix(evidence): reject decorated or re-referenced presenter-bound helpers (#627 review)"; parent 68d9207; tree 1b0818d73de28b9134dbe9e72530286dcd10d302, the exact tree every §6 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.2.md (PR-35, written after the remote evidence below arrives)
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.1 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** PR-35 entered from PR-30's `PR_CANDIDATE_PUBLISHED` handoff. It read every review, thread, comment and check on amthorn78/glow-hdengine-v2#627. One substantive in-scope Codex finding was found and corrected locally, tested, and is published by the push that carries this record (§4–§6).

What is still open, and why this record is not a result:
- the CI run on the head this push creates;
- the Codex code re-review of that head, and the Codex security review, which has never run on #627 (§3);
- mergeability on that head.

What this record does not do:
- It returns no PR-35 result, claims no merge readiness, and requests no Proceed.
- It claims no QA verdict, acceptance, PF09 movement or closure. CI green is not QA.

## 2. Continuity (GCF-17, nine fields)

| Field | Value |
| :- | :- |
| `WORK_UNIT_ID` | `WU-PR-01` |
| Original Product Owner Proceed | Nathan's PR-30 invocation for plan v1.1 (v1.0 front matter `proceed`) |
| Workspace/worktree | the repository checkout `/home/user/glow-hdengine-v2`, in a fresh container for this session. Validation used detached worktrees of the same repository in the session scratchpad |
| Branch | `claude/elegant-mayer-y6ppap`, #627's head. A local branch of that name was created to track `origin/claude/elegant-mayer-y6ppap` at `68d9207` |
| Pull request | amthorn78/glow-hdengine-v2#627 |
| PR instruction | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md` |
| Detailed PR plan | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md` |
| Primary skill authority | `glow-hde-pr-development` 1.4.0 |
| Recovery/artifact lineage | instruction v1.0 → plan v1.0 → rescope request v1.0 → RS-20 review v1.0 + PF10 addendum 2.2 → plan v1.1 → result v1.0 (PR-30) → this result v1.1 (PR-35 checkpoint) |

**Session branch note.** The harness assigned this session the branch `claude/pr-35-review-merge-ready-k9z7uh`, cut from `main` `e3a5ed4`. It carries no work-unit commit, and nothing is pushed to it. PR-35 publishes only to #627's head branch, because Nathan's handoff directs this session to continue #627, and the continuity list allows one branch and one pull request per plan cycle.

## 3. Entry recovery and review reads (2026-10-13, 01:00–01:02Z)

| Read | Evidence | State at read |
| :- | :- | :- |
| Local checkout | one root; worktree clean on `claude/pr-35-review-merge-ready-k9z7uh` at `e3a5ed4` | no uncommitted work |
| PR | #627 open, not draft, head `68d9207`, base `e3a5ed4`, 101 files, 2 commits, `mergeable_state: unstable` (CI pending) | matches v1.0 §9 |
| Remote branch | `origin/claude/elegant-mayer-y6ppap` = `68d9207`; `26140fe` is its parent | matches v1.0 |
| `docs/ephemeral/` | result v1.0 is present on the branch, with no later PR-35 record | nothing to resume |
| Reviews | one, Codex `chatgpt-codex-connector[bot]`, review 5497631947, `COMMENTED`, on `26140fe`, at 00:58:48Z | one inline finding |
| Review threads | one: `PRRT_kwDOP103ks6rq-UC`, unresolved, not outdated (§4) | open |
| Issue comments | one: the Codex review summary, comment 6135675652. It shows **Code Review: Completed** on `26140fe` (trigger "PR opened"), and **no Security Review row** | security review never run |
| Check runs on `68d9207` | `test` (run 38329893033, job 115077054926), in progress | not a gate once this push supersedes it |
| Subscription | `subscribe_pr_activity` for #627 confirmed by the tool result: this session receives #627's events | active |

The Codex security review is required by plan v1.1 §19 and instruction §12. In this repository it is requested by a PR comment `@codex security review`, as amthorn78/glow-hdengine-v2#501 shows. PR-35 requests it once, on the head this push creates (§9).

## 4. Review matrix

| # | Reviewer / location | Revision | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-1 | Codex, review 5497631947, thread `PRRT_kwDOP103ks6rq-UC` (comment r4253702154), `tools/evidence/hdapi_v2_boundary_analyzer.py` lines 2039–2040, P2 | `26140fe` | "Reject decorators on presenter-proven helpers." A decorated helper whose wrapper returns raw bytes is accepted by the new presenter-bound shape, while the parent revision reported the route | substantive in-scope correction | corrected (§5); reply and thread resolution follow the push |

**Verification of R-1, by reproduction:**
- The fixture was `_PRESENTER_HELPER_MODULE` (plan v1.1 §5.8.3) with `@_raw` on `_respond`, where `_raw`'s wrapper returns `Response(b'raw', status=200)`.
- Base `e3a5ed4`: the decorated sanctioned-default shape and the decorated bound-value shape are both reported (`…:reader_post`).
- Entry head `68d9207`: neither is reported (`[]`). This is a regression against addendum 2.2's binding requirement that "bypass detection is not weakened" and that every case reported today stays reported.
- The correction stays inside B-3's confinement (`_adapter_routes_without_presenter` and its private helpers), so it is in-scope repair, not rescope. PF19 Glow QA Guide §13.14 requires a boundary proof to be "conservative and fail closed".

## 5. Correction (one commit)

**`tools/evidence/hdapi_v2_boundary_analyzer.py`.** Only `presenter_bound_helper_key`, the private helper nested in `_adapter_routes_without_presenter`, changes. It adds two acceptance conditions to the five of plan v1.1 §5.8.2:
1. **6.** The helper is undecorated: `fn.decorator_list` is empty. This is the analyzer's existing rule for `add_url_rule` views (`_local_view_binding_proof`).
2. **7.** The helper's name appears in the module only as the callee of a call. Any other reference rejects the shape, such as `_respond.__defaults__ = …`, `setattr(_respond, …)` or `x = _respond`.

Both conditions only narrow what the new shape accepts. The docstring states them. The diff is 11 lines in the tool (blob `23cee18` → `898fafe`).

**`tests/evidence/test_hdapi_v2_contract_inventory.py`.** The negative test `test_epic034_adapter_boundary_rejects_module_helper_without_presenter_provenance` gains three shapes. Each must be reported for `reader_post` and must make `build_adapter_boundary_proof` raise `ADAPTER_BOUNDARY_CHECK_FAILED:…no_presenter_bypass`:
- `decorated_sanctioned_default` (R-1's case);
- `decorated_bound_value`;
- `defaults_replaced`: `_respond.__defaults__ = (_plain,)`.

The docstring lists them. It is still one test function, so the file collects 300 items (B-4; plan D-7). The diff is 8 lines (blob `fd81458` → `5673ff8`).

**Unchanged:**
- every other function of both tools, and every import line, so B-5's import-symbol keys hold;
- the generator, and every governed artifact;
- the positive test and every other test function;
- every other file of the PR.

## 6. Local validation of the correction

Common conditions:
- the candidate tree is `1b0818d73de28b9134dbe9e72530286dcd10d302`, run through a local candidate commit object `4b8e296` (never pushed). The correction commit `c5116f7` has the same tree;
- Python 3.12.3 venv with CI's install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`);
- pytest 8.4.2 (readiness: `python -m pip install -r requirements-dev.txt`, then `python -m pytest --version`);
- `ruby` 3.3.6 (`/usr/local/bin/ruby`);
- `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, so every credential variable was unset.

| # | Check | Result |
| :- | :- | :- |
| L-1 | R-1 reproduction script, base / entry head / correction | decorated default: reported / not reported / reported. Decorated bound value: reported / not reported / reported. Undecorated control: reported / not reported / not reported, as planned |
| L-2 | Related runtime-replacement probe, base / entry head / correction | `__defaults__` replaced on the helper: reported / not reported / reported. Module-level rebinding of the imported presenter name with the helper default: reported / not reported / not reported. The base treats the inline equivalent the same way (OBS-16) |
| L-3 | Production loci, `_adapter_routes_without_presenter(ADAPTER_BOUNDARY_ADAPTER_LOCI)` on the correction | `[]`, as plan v1.1 §5.8.2 requires |
| L-4 | The two new test functions on the correction | 2 passed |
| L-5 | Negative control: the corrected test file against the entry-head analyzer | 1 failed (`AssertionError: decorated_sanctioned_default`, `[] == ['…:reader_post']`), as intended |
| L-6 | `ast` confinement, analyzer base → correction and entry head → correction | only `_adapter_routes_without_presenter` differs; import nodes identical in all three |
| L-7 | `ast`, test file entry head → correction | only the negative test function differs; 189 test functions |
| L-8 | `git diff --check` | exit 0 |
| L-9 | `tests/evidence/test_hdapi_v2_contract_inventory.py` alone, detached worktree of the candidate | 300 passed in 98.2 s; `git diff --exit-code` 0; status empty; no tracked file newer than the marker; no `tmp_boundary_test/` |
| L-10 | Pinned suites plus the ownership and architecture tests (`test_rails_ci_workflow_integration.py`, `tests/qa/test_qa_tool_ownership.py`, `test_http_reader_ci_ownership.py`, `test_evidence_tool_ownership.py`, `test_architecture_snapshot.py`), same worktree | 319 passed in 39.0 s; clean; no tracked file newer than the marker |
| L-11 | Classifier dry run, `--base e3a5ed4 --head 4b8e296 --event-name pull_request` | exit 0; `selected_lanes`; seven lanes; `needs_python=true`; `changed_tests=true`; 101 paths; 163 targets |
| L-12 | Changed-test step exactly as `ci.yml` runs it: detached worktree of the candidate, the 163 targets, one pytest process | 3,262 passed in 370.1 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows the same 11 tracked files rewritten with identical bytes as plan v1.1 §4.3 and result v1.0: 9 paths from `tests/evidence/test_bodygraph_policy_proofs.py` and 2 from `tests/reader_v1/test_release_pack.py` (OBS-4) |

The other lanes were not re-run locally. Only the analyzer and its owner test changed, and hosted CI on the entry head ran every lane on the rest of the same tree (§7).

## 7. CI

| Run | Head | State at record time | Gate? |
| :- | :- | :- | :- |
| 38329893033 (`pull_request`), job 115077054926 | `68d9207` (entry head) | completed, `success`, 00:58:54Z–01:15:35Z. Classification: seven lanes, 101 paths. Changed-test step 3,262 passed; product 77; compat 102 passed, 3 skipped, 2 xfailed; db 249; rails 137 (`RAILS_GATE_EVIDENCE_OK`, `RAILS_JOB_DEFINITIONS_OK`); evidence 113; qa 488; release 64 plus the attestation build and verify; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (job log line 880) | No. R-1 made that head stale, so the run is not a gate for the new head. It is evidence for the parts of the tree the correction does not touch. It finished before the push, so nothing was cancelled |
| next run | the head this push creates | not started at record time | yes, recorded in v1.2 |

**Hosted `ruby` (B-8).**
- Runner image `ubuntu-24.04`, version `20261004.327.1`, from the job log.
- `ruby` is present on the hosted runner: `tests/evidence/test_hdapi_v2_contract_inventory.py` ran in the changed-test step, and the step passed. That file fails without `ruby` (9 failures, B-8).
- The job log does not print the `ruby` version. For this image version, the runner-image readme lists Ruby 3.2.3 (plan v1.1 §3, §5.8.5). That figure is carried from the readme, not observed in the run.
- Whether the November 2026 move of `ubuntu-latest` to Ubuntu 26.04 keeps Ruby remains unknown (OBS-12, Product Owner).

No `[skip ci]` or other suppression is used.

## 8. In-flight decisions

| ID | Decision | Why it is necessary for the approved scope | Tested |
| :- | :- | :- | :- |
| IF-1 | Beyond R-1's decorator case, reject a presenter-bound helper that is referenced other than as a call's callee | The new shape reads the helper's parameter defaults from its definition. Replacing them after definition (`__defaults__`) is a bypass the base reports and the entry head did not, so addendum 2.2's "bypass detection is not weakened" requires it. It narrows acceptance only, and production calls `_production_reader_response` only as a callee | L-2, L-3, L-4, L-9 (`defaults_replaced` shape) |
| IF-2 | Do not change the analyzer for module-level rebinding of an imported presenter name, for decorated ordinary helpers, or for a mutated factory default | Those are pre-existing properties of the analyzer's notion of a sanctioned presenter callable, which the base applies to the inline-equivalent code too (L-2). Changing them would change verdicts for existing shapes, which B-3 does not authorize. Recorded as OBS-16 | L-2 |

## 9. PR_REMOTE_ACTION_LEDGER

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| 01:00–01:02 | PR, review, thread, comment, check and commit reads | §3 | done |
| ~01:01 | Subscribe to #627 activity | tool result confirms delivery to this session | active |
| ~01:02–01:08 | R-1 reproduction, related probe, correction, L-4 and L-5 | L-1, L-2, L-4, L-5 | done |
| 01:09:42–01:15:53 | Changed-test step, 163 targets | L-12 | 3,262 passed; clean |
| ~01:10–01:16 | Remaining local checks | L-3, L-6 to L-11 | pass |
| 01:15:35 | CI run 38329893033 on `68d9207` completed | §7 | `success`; not a gate for the new head |
| this push | Correction commit and this record's commit, one push to `claude/elegant-mayer-y6ppap` | verified by `git ls-remote` and a PR read after the push; recorded in v1.2 | pending verification |
| after the push | Reply on thread `PRRT_kwDOP103ks6rq-UC` naming the correction commit, then resolve it | GitHub | pending |
| after the push | Comment `@codex security review` once | GitHub | pending |

**Remaining useful local action:** none.

**Next evidence actions:**
- verify the push;
- reply on R-1 and resolve its thread;
- request the security review;
- read the Codex code re-review (amthorn78/glow-hdengine-v2#501 shows a re-review triggered by new commits), the security review, and CI on the new head;
- check mergeability.

## 10. Constraints, unresolved items and owners

| Item | Owner |
| :- | :- |
| CI on the new head: all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | PR-35 |
| Codex code re-review and Codex security review on the new head | PR-35 |
| Mergeability on the new head | PR-35 |
| OBS-16 (new). Three pre-existing analyzer properties, found while verifying R-1 and not changed (IF-2): (a) a module-level rebinding of an imported sanctioned presenter name (for example `emit_reader_public_bytes = _plain`) is not detected; (b) decorators on an ordinary helper are not considered by `function_returns_presenter`; (c) a mutated factory `__defaults__` is not detected | the whole-change IA (analyzer items, as plan v1.1 OBS-13 and OBS-14). No HDE-CRD-0002 unit waits on it |
| OBS-12: `ruby` is an undeclared dependency of the generator | Product Owner (documentation delta candidate); hosted observation in §7 |
| Legacy chart-loader defect (HDE-SEPA006) | Product Owner |
| Plan v1.1 §17 observations OBS-1 to OBS-15 | the owners named there |
| Merge | Nathan only |

## 11. Canon relied on

Read on `main` at `e3a5ed4`. `docs/pfcanon/` is identical on the branch, so there is no unmerged canon proposal.

| Source | Sections read | Used for |
| :- | :- | :- |
| PF10-HDE-Build-Notes v13.5.3 | in full (§0 precedence and silence rules; addenda 2.1 and 2.2) | Addendum 2.2 "Approved delta (RP-1)" item 2 and "Binding requirements" govern R-1's disposition and the correction's confinement (§4, §5, §8). Addendum 2.1 governs TypeSafe reading duties, none of which falls in this checkpoint. PF10 is otherwise silent on PR-35 review handling, so permanent canon and the in-flight documents govern |
| PF19-Canon-Glow-QA-Guide v3.0.6 | §13.14 (HDE-EPIC034 QA learnings: "Boundary proof must be conservative and fail closed") | that a proof passing while missing a presenter bypass is a proof-model failure (§4) |
| PF06-Canon-Change-Process-Guide v2.5.4 | §2.3 (Code Review (the executing agent)) and §1.0.6 (QA, closeout, and PF30 result update), read | §2.3: the correction adds no public interface, changes no public payload and uses no time or RNG source. §1.0.6: "CI success alone is not QA acceptance" (§1 nonclaims) |
| PF04-Canon-HDE-Governance v2.8.7 | §9.1.1 (Change authority and exact-artifact lineage), read in full | PR implementation stays with the dedicated PR session under the normal code, security, review and evidence chain; Nathan's `PR Implementation Proceed` is the only Product Owner runtime approval; merges are Product Owner actions |
| Search terms on `main` `docs/pfcanon/` | `codex`, `security review`, `code review`, `merge readiness`, `ready to merge`, `presenter bypass`, `no_presenter_bypass` | no other governing section found for PR-35 review handling |
| In-flight documents | instruction v1.0 §10–§15; plan v1.1 front matter, §1–§3, §5.8.2–§5.8.7, §13–§20; RS-20 review v1.0 as restated by addendum 2.2; result v1.0 in full | scope, B-3/B-4/B-5, PR-35 duties (plan §19; instruction §12), and the observation routes (plan §17) |
| Operative documentation | `AGENTS.md`: closed rails, pytest readiness, no hand-edited governed artifacts, PR description rules, evidence attribution, and the code-review scope exclusions | how the work is done and recorded |
| Prompt and skill | PR-35 (100926.1, in full); `glow-hde-pr-development` 1.4.0 | phase duties |

## 12. Recovery

If this session is interrupted:
- **This record was pushed:** re-enter PR-35 in its dedicated session from this file. Verify the remote head, then continue at §9's next evidence actions.
- **This record was not pushed:** the correction is local and uncommitted, or committed but unpushed, on `claude/elegant-mayer-y6ppap`. Recover the local branch, re-run L-9 and L-10, and push the correction and this record together.

Nothing is re-run that this record shows complete. No second PR or branch is created.
