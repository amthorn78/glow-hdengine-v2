---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.3"
record_kind: PR-35 checkpoint for the third corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.2.md (v1.2, PR-35 checkpoint; blob c0be05f3f13a; 17,954 bytes; sha256 a8d92a49a2b564d14ab7b063013842ed119a37af7f631f4cc22108ba5054cd3f); v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95 and 76483d7, pushed; 11d4aa5350c4827dca4cb48acf26fb88937ba12d (CX6-4; parent 76483d7); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T16:01Z
next_step: push 11d4aa5 and this record; reply to and resolve the CX6-4 thread; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.3 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `76483d7` raised one P2 finding, CX6-4, on the editable project in the same install-step substitute. It is corrected by `11d4aa5`, together with the one remaining sibling gap of the same kind (entry-point groups other than scripts), and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 | Codex review 5571963225, thread `PRRT_kwDOP103ks6t7foX`, P2 | `d2ed4fc` | presence-only install check ignores version specifiers | fixed in `2894628` (result v1.1); thread resolved |
| CX6-2 | Codex review 5573092833, thread `PRRT_kwDOP103ks6t9otV`, P2 | `7303b26` | requirement extras dropped (`psycopg[binary]`) | fixed in `302ab95` (result v1.2); reply r4315534890; thread resolved |
| CX6-3 | Codex review 5573092833, thread `PRRT_kwDOP103ks6t9otb`, P2 | `7303b26` | installed console-script wrappers not compared with the candidate | fixed in `302ab95` (result v1.2); reply r4315535502; thread resolved |
| CX6-4 | Codex review 5573797059 (on `76483d7`), comment r4315592526, P2 | `76483d7` | `tools/ci/prepush_check.py` 1231: a candidate whose `requires-python` excludes the workflow's Python fails CI's `pip install -e .`, but the substitute never reads it, so an already-installed project lets the replay pass a candidate CI cannot install | Substantive, in scope. Path traced: `_install_check` read the candidate's name, version, dependencies and scripts only. Reproduced with the real step and a candidate declaring `requires-python = ">=3.13"` (§5 item 7, case 4). Fixed in `11d4aa5` (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

**Fixed point of the root cause.** `pip install -e .` rebuilds the editable project from the candidate: its name, version, dependencies, `requires-python` and every entry-point group. After `11d4aa5` the substitute checks each of them against the candidate. Pip's isolated build environment, fetched from the package index, is the one input of the install step an offline check cannot verify. The tool states that limit (docstring of `_install_check`), and its nonclaim, "the tool's green is not CI's green", covers it.

## 3. Correction CX6-4 (`11d4aa5`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `d6f9a5fd396a`; 1,532 lines; +38/−21 on `76483d7`) | The editable project's `requires-python` is parsed as PEP 440 clauses and checked against `platform.python_version()`, the replay's interpreter (CX6-4); an unparseable value fails closed. The entry-point comparison covers every group the candidate declares (`scripts`, `gui-scripts` and `[project.entry-points.*]`) or the installed metadata holds, because pip regenerates them all; a mismatch names the group, the installed entries and the candidate's. The clause loop is factored out of `_parse_requirement` into `_parse_clauses` for reuse; the parsing behaviour is unchanged (§5 item 6). The docstring of `_install_check` states the build-environment limit |
| `tests/tools/test_prepush_check.py` (blob `7675821dec7f`; 690 lines; +14/−1) | The synthetic site case's candidate declares `requires-python` and a `pytest11` group; the broken site now yields five unmet lines (the new one: `proj pytest11 {} (the candidate declares {'plug': 'proj.plug'})`); a `requires-python = "<3"` candidate yields exactly the requires-python line; an unparseable `requires-python` is refused. Still 28 cases |

## 4. CI on `76483d7`

Run 39276419131 (job 118141763778) started on `76483d7` at 15:15:49Z. It became stale when the re-review completed at 15:21:18Z with CX6-4. It was not waited on and is not a gate. Cancellation was not attempted again (the same interface refused it at result v1.2 §4). It completed on its own with conclusion `success` (read at 16:01Z); that result covers `76483d7` only, whose code CX6-4 changes.

## 5. Local validation of `11d4aa5`

Environment as result v1.1 §5 (closed rails, keys unset, CPython 3.12.3 venv with CI's install, `-e` re-pointed at the clone `cand` at `11d4aa5`, `ruby` 3.3.6, `bash`, `curl`); three fresh scratch clones detached at `11d4aa5`; `PYTHONPATH` the clone under test; exit statuses the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 28 passed in 39.1 s (concurrent with items 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..11d4aa5`, `pull_request` | exit 0; `reason=selected_lanes;paths=6;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls, each in a throwaway clone at `11d4aa5`, one guard disabled and committed there | NC-11 to NC-15 as result v1.2 §5 item 5, each failing as intended again (NC-12 adapted to the factored parser). NC-16 (requires-python not checked): the site case fails. NC-17 (only script groups compared): the site case fails |
| 6 | Cross-checks against `packaging` (scratch only), loaded by path from `cand2` | unchanged from result v1.2 §5 item 6: `packaging` 26.3, 1,890 comparisons, 0 disagreements (`platform_machine === "x86_64"` raises in both); pip's vendored `packaging` 21.3, 892 real marker evaluations, 0 disagreements |
| 7 | The real `ci.yml` install step through `_install_check` | (1) the CI venv: no unmet requirement; (2) `psycopg-binary` removed: exactly `psycopg-binary (not installed; required by psycopg)`; (3) `hdctl` target changed: exactly the `console_scripts` mismatch line; (4) a candidate with `requires-python = ">=3.13"` (CX6-4): exactly `glow-hdengine requires-python >=3.13 (the interpreter is 3.12.3)`; (5) a candidate adding `[project.entry-points.pytest11] hde = "engine.plugin"`: exactly `glow-hdengine pytest11 {} (the candidate declares {'hde': 'engine.plugin'})`; (6) `_substitute` on the real step: `success` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 15:27:15Z to 16:01:05Z (concurrent with item 9); classify `reason=selected_lanes;paths=6`, all seven lanes; every one of the 16 steps SUCCESS, step 05 the substitute's success; changed tests 166 targets, 3,914 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 2,025.1 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, HEAD and git metadata)`. `cand` before and after: `head=11d4aa5…`, `status_lines=0`, `git_metadata_digest=7cb5ce2eaf227bf8a61711e3d2cd86426a3f90bedf05d8561e48be1a8dcd2be4`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,214 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,588.9 s (15:27:15Z to 15:53:46Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Equal to result v1.2's count (the case count is unchanged) |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 | This phase's commits go to the pull request's branch `claude/youthful-gauss-d9e0ab` | one branch and one pull request per plan cycle (GCF-17); result v1.1 §6 | remote head read back after each push |
| IF-35-2 | Standard-library PEP 440/508 subset that fails closed, not `packaging` | instruction §7 "No new dependency"; plan PD-8; result v1.1 §6 | §5 items 1, 5, 6 |
| IF-35-3 | The substitute checks that CI's install would change nothing | result v1.2 §6 | result v1.2 §5 |
| IF-35-4 | Beyond CX6-4's literal ask, every entry-point group of the editable project is compared, not only scripts | Same reinstall, same root cause as CX6-3: a candidate that adds or changes, for example, a pytest plugin entry point would otherwise replay with the stale plugin set while CI registers the new one. About ten lines inside the same comparison; no other path changes | §5 items 1, 5 (NC-17), 7 (case 5), 8, 9 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.2 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 15:15:41 | push 2 of PR-35: `7303b26..76483d7`, fast-forward, no force | `git rev-parse origin/claude/youthful-gauss-d9e0ab` = `76483d7…` |
| 15:15:49 | CI run 39276419131 on `76483d7` started | check run 118141763778 |
| 15:15:57, 15:16:00 | replies r4315534890 (CX6-2) and r4315535502 (CX6-3); both threads resolved | GitHub |
| 15:15:51 to 15:21:18 | Codex code review on `76483d7` (trigger "New commits"): review 5573797059, finding CX6-4 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 15:20:03 | the 15:17Z safety-net check-in fired: review and CI still running; re-armed for 16:11Z (`trig_01VQRjrP6m1GBA1snBgnfMYd`) | it creates no session |
| 15:26:28 | local commit `11d4aa5` (unpushed) | §3 |
| 15:27:15 to 16:01:05 | local validation of `11d4aa5`, all passed | §5 |
| after this record | push 3 of PR-35: `11d4aa5` and the commit adding this record, fast-forward onto `76483d7`, no force | read back in the next record |
| next | reply on the CX6-4 thread naming `11d4aa5`, and resolve it; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35 | pending |
| The install step's isolated build environment (build requirements fetched from the package index) | stated limit of the tool; no owner action | not verifiable offline; covered by the nonclaim |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note; OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
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
| In-flight scope | instruction v1.0 ID-8, ID-9, ID-12, §6, §7 "No new dependency" and "Network"; plan v1.0 §5.7, PD-8, §6.1, §13 RK-5, §17 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
