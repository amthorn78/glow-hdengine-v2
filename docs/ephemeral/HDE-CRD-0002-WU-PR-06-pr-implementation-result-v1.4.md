---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.4"
record_kind: PR-35 checkpoint for the fourth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.3.md (v1.3, PR-35 checkpoint; blob 980eed838fd4; 14,745 bytes; sha256 94e4045ca08ac36e17ec8ecee10a88a287e0559f80ae149735893e216ec1a81b); v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-06
work_unit_title: "Read-only pre-push and pre-plan check (PR; Distillation; S20)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob f3a6a8855ec0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0.md (v1.0; blob 2848847e8bee)
effective_baseline: unchanged from result v1.0 (approved base + PF10 addenda 2.2, 2.3, 2.4, 2.5, 2.9, 2.10)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md (v13.6.1; sha256 ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e; unchanged on origin/main 0442d23). Provenance, not a gate
pf10_addendum_created: none
proceed: the original Proceed of result v1.0. No other Proceed exists or is needed
session: the dedicated HDE-CRD-0002 WU-PR-06 PR-35 session, https://claude.ai/code/session_01SVmct81WDzDqX36ZasAijn
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e); primary skill glow-hde-pr-development 1.4.0; support skill glow-write-boundary
pull_request: amthorn78/glow-hdengine-v2#660 (https://github.com/amthorn78/glow-hdengine-v2/pull/660), branch claude/youthful-gauss-d9e0ab into main
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5 and b7bc20b, pushed; c9d91961151a9398ad5d2c7a4b2fd829b91fa5e9 (CX6-5 and CX6-6; parent b7bc20b); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T16:47Z
next_step: push c9d9196 and this record; reply to and resolve the CX6-5 and CX6-6 threads; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.4 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `b7bc20b` raised two P2 findings: CX6-5, on the extras parser, and CX6-6, on the checkout substitute. Both are corrected by `c9d9196`, with CX6-6's root cause, and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 | Codex review 5571963225, thread `PRRT_kwDOP103ks6t7foX`, P2 | `d2ed4fc` | presence-only install check ignores version specifiers | fixed in `2894628` (result v1.1); resolved |
| CX6-2 | review 5573092833, thread `PRRT_kwDOP103ks6t9otV`, P2 | `7303b26` | requirement extras dropped | fixed in `302ab95` (result v1.2); resolved |
| CX6-3 | review 5573092833, thread `PRRT_kwDOP103ks6t9otb`, P2 | `7303b26` | installed console-script wrappers not compared | fixed in `302ab95` (result v1.2); resolved |
| CX6-4 | review 5573797059, thread `PRRT_kwDOP103ks6t--QV`, P2 | `76483d7` | candidate `requires-python` not checked | fixed in `11d4aa5` (result v1.3); reply r4316014604; resolved |
| CX6-5 | review 5574347631 (on `b7bc20b`), comment r4316055412, P2 | `b7bc20b` | `tools/ci/prepush_check.py` 1036: `alpha[fast, slow]>=1` stores the second extra as `" slow"`, so a dependency guarded by `extra == "slow"` is never checked and the substitute can pass | Substantive, in scope; a real defect in `302ab95`'s parser (`_canonical` keeps the leading space). The real requirement files have no space in their extras, which is why §5 item 6's real-metadata cross-check did not show it. Fixed in `c9d9196` (§3) |
| CX6-6 | review 5574347631, comment r4316055421, P2 | `b7bc20b` | `tools/ci/prepush_check.py` 1389: a candidate that changes the checkout step's `with:` inputs (`ref`, submodules, sparse checkout) is still accepted, and the substitute treats a clone of the head as equivalent, so the replay can test another tree | Substantive, in scope. Path traced: `replay_steps` checked step names, keys and `uses:`/`run:` only, and `_substitute` returns success for any checkout. Reproduced with `b7bc20b`'s own `replay_steps` on the real `ci.yml`: a `sparse-checkout` input and a removed `ref` were both accepted (and its parser returned `{'fast', ' slow'}` for CX6-5's example). Fixed in `c9d9196` (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

**Root cause of CX6-6.** The replay stands in for three things it does not run: the checkout action, the Python set-up action and the hosted runner. Like the install step before them (CX6-1 to CX6-4), each substitution accepted inputs it does not model, and the jobs-only parser skipped workflow-level keys. `c9d9196` makes each substitution accept only what it reproduces (§3, IF-35-5).

## 3. Correction CX6-5 and CX6-6 (`c9d9196`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `2fac2e342428`; 1,561 lines; +30/−1 on `b7bc20b`) | **CX6-5.** Each extra is stripped before canonicalizing. **CX6-6 and its root cause.** `replay_steps` refuses as `REPLAY_INVENTORY_DRIFT`, a tooling failure: a `uses:` step whose action is not one the replay substitutes; any input of `actions/checkout` other than `fetch-depth` (required, exactly `0`), `ref` (required, exactly the head expression `${{ github.event.pull_request.head.sha \|\| github.sha }}`) and `persist-credentials` (any value); any input of `actions/setup-python` other than `python-version`; a `runs-on` that is not an `ubuntu-` runner; and any workflow-level key other than `name`, `run-name`, `on`, `permissions`, `concurrency` and `jobs` (a workflow-level `env:` or `defaults:` would otherwise be skipped). `report_replay` refuses, as tooling, to replay on a machine that is not Linux. The supported inputs are one table, `REPLAY_SUBSTITUTED_INPUTS`, beside the inventory; a later workflow change that adds an input must update it in the same pull request, as for a step (contract G-3) |
| `tests/tools/test_prepush_check.py` (blob `5fc5fc000b17`; 702 lines; +16/−4) | Six more drift cases on the real `ci.yml`: a changed checkout `ref`, an added `submodules`, `fetch-depth: 1`, an added set-up input, a `macos-latest` runner and a workflow-level `env:`. The synthetic replay workflow's checkout step carries the real inputs. The site case requests `alpha[fast, slow]` with `zeta; extra == "slow"`, and a missing `zeta` is now reported; the clause table checks `alpha[ Fast , slow_path ]`. The owner test goes from 28 to 34 cases |

## 4. CI on `b7bc20b`

Run 39282295924 (job 118158804432) started on `b7bc20b` at 16:01:48Z. It became stale when the re-review completed at 16:06:19Z with CX6-5 and CX6-6. It is not waited on and is not a gate, and cancellation was not attempted (refused through the same interface at result v1.2 §4).

## 5. Local validation of `c9d9196`

Environment as result v1.1 §5 (closed rails, keys unset, CPython 3.12.3 venv with CI's install, `-e` re-pointed at the clone `cand` at `c9d9196`, `ruby` 3.3.6, `bash`, `curl`); three fresh scratch clones detached at `c9d9196`; `PYTHONPATH` the clone under test; exit statuses the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 34 passed in 44.5 s (concurrent with items 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..c9d9196`, `pull_request` | exit 0; `reason=selected_lanes;paths=7;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls, each in a throwaway clone at `c9d9196`, one guard disabled and committed there | NC-11 to NC-17 as before, each failing as intended. NC-18 (substituted inputs not checked): the four checkout and set-up drift cases fail. NC-19 (extras not stripped): the site case and the clause-and-marker case fail. NC-20 (workflow-level keys not checked): the workflow-env case fails. NC-21 (runner not checked): the runner case fails |
| 6 | Cross-checks against `packaging` (scratch only), loaded by path from `cand2` | `packaging` 26.3: 1,890 comparisons, 0 disagreements (`platform_machine === "x86_64"` raises in both); pip's vendored `packaging` 21.3: 892 real marker evaluations, 0 disagreements; extras of `alpha[fast, slow]>=1` and `alpha[ Fast , slow_path ]>=1` equal `packaging`'s canonicalized extras |
| 7 | The real `ci.yml` through the substitutes | install step cases (1) to (5) as result v1.3 §5 item 7, unchanged; the real `ci.yml` passes `replay_steps`; with a `sparse-checkout` input added, `REPLAY_INVENTORY_DRIFT: … inputs the replay does not model: sparse-checkout`; with the `ref` line removed, the same drift naming `ref` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 16:13:31Z to 16:47:29Z (concurrent with item 9); classify `reason=selected_lanes;paths=7`, all seven lanes; every one of the 16 steps SUCCESS; changed tests 166 targets, 3,920 passed (result v1.0's 3,907 plus the 13 net new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 2,029.9 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, HEAD and git metadata)`. `cand` before and after: `head=c9d9196…`, `status_lines=0`, `git_metadata_digest=8716137f699eeb9ec765df6a2895ac964a4272ed9ef7375ff245e32d0367049c`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,220 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,683.4 s (16:13:31Z to 16:41:37Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.0's 5,207 plus the 13 net new cases; the skips, xfails and warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 | This phase's commits go to the pull request's branch `claude/youthful-gauss-d9e0ab` | one branch and one pull request per plan cycle (GCF-17); result v1.1 §6 | remote head read back after each push |
| IF-35-2 | Standard-library PEP 440/508 subset that fails closed, not `packaging` | instruction §7 "No new dependency"; plan PD-8 | §5 items 1, 5, 6 |
| IF-35-3 | The install-step substitute checks that CI's install would change nothing | result v1.2 §6 | results v1.2 and v1.3 §5 |
| IF-35-4 | Every entry-point group of the editable project is compared | result v1.3 §6 | result v1.3 §5 |
| IF-35-5 | Beyond CX6-6's literal ask (checkout inputs), the set-up action's inputs, the runner and the workflow-level keys are also limited to what the replay reproduces, and a non-Linux machine is refused | The replay's honest final audit (plan PD-8) needs every substitution honest; instruction ID-8 already makes an unsupported construct a tooling failure, and these four are the remaining places where the replay accepted a construct it does not reproduce. About twenty lines; no CI behaviour changes; the real `ci.yml` passes unchanged | §5 items 1, 5 (NC-18, NC-20, NC-21), 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.3 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 16:01:38 | push 3 of PR-35: `76483d7..b7bc20b`, fast-forward, no force | `git rev-parse origin/claude/youthful-gauss-d9e0ab` = `b7bc20b…` |
| 16:01:51 | reply r4316014604 on `PRRT_kwDOP103ks6t--QV` (CX6-4); thread resolved | GitHub |
| 16:01:51 to 16:06:19 | Codex code review on `b7bc20b` (trigger "New commits"): review 5574347631, findings CX6-5 and CX6-6 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 16:12:38 | local commit `c9d9196` (unpushed) | §3 |
| 16:13:31 to 16:47:29 | local validation of `c9d9196`, all passed | §5 |
| after this record | push 4 of PR-35: `c9d9196` and the commit adding this record, fast-forward onto `b7bc20b`, no force | read back in the next record |
| next | reply on the CX6-5 and CX6-6 threads naming `c9d9196`, and resolve them; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35 | pending |
| The install step's isolated build environment | stated limit of the tool (result v1.3 §2) | not verifiable offline |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (now also: the replay needs a Linux machine); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

Read on `main` at `0442d23` (`docs/pfcanon/` unchanged since `5e62a65`; this branch changes no canon).

| Topic | Sources and sections |
| :- | :- |
| Phase authority, review chain, stale CI, merge boundary | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (all sections); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 |
| Review chain overlay | PF10-HDE-Build-Notes v13.6.1 addendum 2.3 (Rules 1 to 5) |
| Tooling vs behavior | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 |
| In-flight scope | instruction v1.0 ID-8 (inventory, exclusions, conditions, environment, interpreter), ID-9, ID-12, §6, §7, §8 G-3; plan v1.0 §5.7, PD-8, §6.1, §13 RK-1 and RK-5, §17 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
