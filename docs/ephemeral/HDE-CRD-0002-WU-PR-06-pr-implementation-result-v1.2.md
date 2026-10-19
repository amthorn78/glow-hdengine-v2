---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.2"
record_kind: PR-35 checkpoint for the second corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.1.md (v1.1, PR-35 checkpoint; blob 8d103888fc24; 18,917 bytes; sha256 1d8604bfd2f2e45a9e1b5d05a1f5a33a330ff3b3b31376442e7a6a2792156861); docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; blob b506bff32c5c). Both preserved unchanged
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
commits_this_phase: 2894628 (CX6-1) and 7303b26 (result v1.1), pushed; 302ab958fac9afc7bce328d6626c2d2c97e43535 (CX6-2 and CX6-3; parent 7303b26); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T15:15Z
next_step: push 302ab95 and this record; reply to and resolve the CX6-2 and CX6-3 threads; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.2 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `7303b26`, the head that carried the CX6-1 correction, raised two more P2 findings on the same install-step substitute, CX6-2 and CX6-3. Both are corrected by `302ab95`, together with their common root cause, and verified locally (§3 to §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Location | Finding | Classification | Disposition |
| :- | :- | :- | :- | :- | :- | :- |
| CX6-1 | Codex review 5571963225, thread `PRRT_kwDOP103ks6t7foX`, P2 | `d2ed4fc` | `_install_check` | presence-only check accepts a version outside the step's specifiers | substantive, in scope | fixed in `2894628` (result v1.1 §4); reply r4314994045; thread resolved |
| CX6-2 | Codex review 5573092833 (on `7303b26`), comment r4315034591, P2 | `7303b26` | `tools/ci/prepush_check.py` 991 (`_install_check`) | `psycopg[binary]>=3.1,<3.3` is reduced to `psycopg`; with `psycopg-binary` absent the substitute still reports the install as satisfied, though CI would install it; "preserve requested extras and validate their applicable `Requires-Dist` dependencies" | Substantive, in scope. Path traced: requirements.txt's `psycopg[binary]`; `_parse_requirement` discarded the extras; a caller who installed `psycopg` without the extra gets a green step 05 and db/release lanes on another dependency set. Reproduced (§5 item 7, case 2) | fixed in `302ab95` (§3) |
| CX6-3 | Codex review 5573092833, comment r4315034601, P2 | `7303b26` | `tools/ci/prepush_check.py` 1063 (`_resolution`) | a candidate that changes a `[project.scripts]` target replays through the console-script wrapper installed from the old target, because the install step is excluded; the compat lane runs `hdctl` from `PATH` | Substantive, in scope. Path traced: `_resolution` checks only that the target's module resolves inside the copy; the wrapper imports the installed entry point's `module:attr`. Reproduced (§5 item 7, case 3) | fixed in `302ab95` (§3) |
| — | Codex security review | — | — | not part of the chain (PF10 addendum 2.3) | not applicable | none needed |
| — | Human review | — | — | none requested or present | — | — |

**Root cause shared by CX6-1 to CX6-3.** The substitute for the excluded install step stood for "the caller's environment already has CI's install" (instruction ID-8) but checked it piecemeal: presence first, then versions, while extras, transitive requirements and the editable project's own metadata stayed unchecked. `302ab95` makes the substitute check the one condition that matters, that CI's install step would change nothing (§3, IF-35-3).

## 3. Correction CX6-2 and CX6-3 (`302ab95`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `122e12c94625`; 1,515 lines; +256/−53 on `7303b26`) | **Closure.** `_install_check` collects the step's requirements (literal words, `-r` files with nested `-r` followed and line continuations joined, the `-e` project's name and its candidate `[project].dependencies`) and `_unmet_requirements` follows their closure through each installed distribution's `Requires-Dist`, for the extras requested of it (CX6-2), with PEP 508 markers evaluated for the replay's interpreter, checking every version clause. **Editable project.** The installed project's version and its `console_scripts` and `gui_scripts` entry points must equal the candidate's `pyproject.toml` (CX6-3). **Parsing.** PEP 508 requirements (extras, parenthesized clauses, markers) and PEP 440 clauses including pre-, post- and dev-release versions, `===`, `~=` and wildcards. Marker comparisons follow the forms on which current and older `packaging` agree: version operators on `python_version`, `python_full_version`, `implementation_version` and `platform_release`; `==`, `!=`, `in` and `not in` on the others. **Fail closed.** Another pip option, a URL requirement, a local-version clause, a legacy dotted marker name, an undefined marker comparison, a requirements-file option other than `-r`, an editable project without a static version, or a command other than one `python -m pip install` raise `ValueError`, reported as `TOOLING cannot read the install step's inputs`. An unmet requirement is reported with what requires it, for example `psycopg-binary (not installed; required by psycopg)`. Standard library only (`platform` added to the imports) |
| `tests/tools/test_prepush_check.py` (blob `6417cb1b87ae`; 677 lines; +95/−18) | `test_install_substitute_follows_extras_dependencies_and_the_editable_project`: a synthetic site directory of `.dist-info` entries and a candidate copy; the broken site yields exactly four unmet lines (a transitive version, a missing extra dependency, the project's version and its console-script target) while a marker-excluded requirement stays out; the fixed site yields none; a pip option, a non-pip command and a requirements-file option are refused. `test_version_clauses_and_markers_follow_pep_440_and_508` (replaces CX6-1's clause table): pre-release, post-release, wildcard, epoch and `===` clauses, parenthesized and extras requirements, markers with extras, parentheses, `in` and name normalization, and the refused and undefined forms. The CX6-1 parametrized case keeps its five cases with the new wording. The owner test goes from 27 to 28 cases |

## 4. CI on `7303b26`

Run 39268868152 (job 118115568797) started on `7303b26` at 14:25:53Z. It became stale when the re-review at 14:29:34Z found CX6-2 and CX6-3. Cancellation was attempted through the GitHub Actions interface and refused (`403 Resource not accessible by integration`). The run was not waited on and is not a gate. It completed on its own with conclusion `success` (check suite completed by 14:43:09Z); that result covers `7303b26` only, whose code CX6-2 and CX6-3 change.

## 5. Local validation of `302ab95`

Environment as result v1.1 §5: closed rails, the vendor, database and GitHub keys unset, CPython 3.12.3 venv with CI's install (`-e` re-pointed at the clone `cand` at `302ab95`), `ruby` 3.3.6, `bash`, `curl`; three fresh scratch clones detached at `302ab95` (`cand` replay only, `cand2` short checks, `sweep`); `PYTHONPATH` the clone under test; exit statuses the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 28 passed in 38.6 s (concurrent with items 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..302ab95`, `pull_request` | exit 0; `reason=selected_lanes;paths=5;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls, each in a throwaway clone at `302ab95`, one guard disabled and committed there | NC-11 (version clauses not checked): the version-outside-specifier case and the site case fail (2 failed). NC-12 (unsupported forms accepted): the unsupported-form case and the clause-and-marker case fail (2 failed). NC-13 (requested extras ignored): the site case fails. NC-14 (entry points not compared): the site case fails. NC-15 (installed `Requires-Dist` not followed): the site case fails |
| 6 | Cross-checks against `packaging` (scratch only, not deliverables), loaded by path from `cand2` | `packaging` 26.3: the marker environment equals `default_environment()` for every key; every `Requires-Dist` line of the 28 installed distributions (15 declare any) parses to the same name, extras and clauses, and its marker evaluates the same for `""` and every declared extra; 20 synthetic markers; 26 versions × 19 specifiers with pre-release, post-release, `===`, `~=`, wildcard and epoch forms: 1,890 comparisons, 0 disagreements (`platform_machine === "x86_64"` raises in both). pip 24.0's vendored `packaging` 21.3 on the same real markers: 892 evaluations, 0 disagreements |
| 7 | The real `ci.yml` install step through `_install_check` | (1) the CI venv: no unmet requirement; (2) the same metadata with `psycopg_binary-*.dist-info` removed (CX6-2): exactly `psycopg-binary (not installed; required by psycopg)`; (3) a candidate `pyproject.toml` whose `hdctl` target is `engine.cli.entry:main` (CX6-3): exactly `glow-hdengine console_scripts {'hdctl': 'engine.cli.main:cli'} (the candidate declares {'hdctl': 'engine.cli.entry:main'})`; (4) `_substitute` on the real step: `success` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 14:43:39Z to 15:15:04Z (concurrent with item 9); classify `reason=selected_lanes;paths=5`, all seven lanes; every one of the 16 steps SUCCESS; step 05 (install substitute): "the environment already satisfies every requirement the step names, their dependencies and extras, and the editable project's version and entry points"; changed tests 166 targets, 3,914 passed (result v1.0's 3,907 plus the 7 net new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,879.7 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, HEAD and git metadata)`. `cand` before and after: `head=302ab95…`, `status_lines=0`, `git_metadata_digest=6a5bf6f790615db219a822ea9c834135d0a59cd7e0cdbfcaeffb564e0b2f5141`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,214 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,562.1 s (14:43:40Z to 15:09:44Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.0's 5,207 plus the 7 net new cases; the skips, xfails and warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 | This phase's commits go to the pull request's branch `claude/youthful-gauss-d9e0ab`, not the session's default branch `claude/wizardly-gates-m8at0w` | one branch and one pull request per plan cycle (GCF-17); result v1.1 §6 | remote head read back after each push |
| IF-35-2 | Corrections use a standard-library PEP 440/508 subset that fails closed, not the `packaging` library | instruction §7 "No new dependency"; plan PD-8; result v1.1 §6 | §5 items 1, 5 and 6 |
| IF-35-3 | The install-step substitute checks that CI's install would change nothing: the requirement closure through installed metadata, extras and markers included, and the editable project's version and entry points; unverifiable forms fail closed. This goes beyond the two findings' literal asks (transitive dependencies, nested `-r`, the project's version, refused pip options) | Three findings in two review rounds came from one root cause, a partial check of instruction ID-8's prerequisite "the caller's environment must already have CI's install". Without the substitute's honest outcome the replay's final audit is not honest (plan PD-8). The change stays inside `tools/ci/prepush_check.py` and its owner test, adds no dependency and changes no CI behaviour | §5 items 1 and 5 to 9 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.1 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 14:25:44 | push 1 of PR-35: `d2ed4fc..7303b26`, fast-forward, no force, to `claude/youthful-gauss-d9e0ab` | `git rev-parse origin/claude/youthful-gauss-d9e0ab` = `7303b26…` |
| 14:25:56 | reply r4314994045 on `PRRT_kwDOP103ks6t7foX` (CX6-1), then thread resolved | GitHub |
| 14:25:53 | CI run 39268868152 on `7303b26` started | check run 118115568797 |
| 14:25:54 to 14:29:34 | Codex code review on `7303b26` (trigger "New commits"): review 5573092833, findings CX6-2 and CX6-3 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 14:26:23 | safety-net check-in scheduled for 15:17Z (`trig_012Wk8tfu4nzgSrS6zYVvYZu`), for undelivered events only | it creates no session |
| after 14:29:38 | cancel of run 39268868152 attempted: `403 Resource not accessible by integration` | §4 |
| 14:42:50 | local commit `302ab95` (unpushed) | §3 |
| 14:43:39 to 15:15:04 | local validation of `302ab95`, all passed | §5 |
| after this record | push 2 of PR-35: `302ab95` and the commit adding this record, fast-forward onto `7303b26`, no force | read back in the next record |
| next | reply on the CX6-2 and CX6-3 threads naming `302ab95`, and resolve them; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35 | pending |
| Result v1.1 §8's extras and nested `-r` item | — | closed by `302ab95` |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands (result v1.1 §7) |
| WU-DOC-01 usage note; OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

Read on `main` at `0442d23` (`docs/pfcanon/` unchanged since `5e62a65`; this branch changes no canon).

| Topic | Sources and sections |
| :- | :- |
| Phase authority, review chain, merge boundary | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (all sections, including "Review-first and action-efficient execution" items 6 and 7 on stale CI); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 |
| Review chain overlay | PF10-HDE-Build-Notes v13.6.1 addendum 2.3 (Rules 1 to 5) |
| Tooling vs behavior | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5: an unmet or unverifiable install prerequisite is a tooling failure |
| In-flight scope | instruction v1.0 ID-8 (the excluded install step and its prerequisite), ID-9, ID-12, §6, §7 "No new dependency"; plan v1.0 §5.7, PD-8, §6.1, §13 RK-5, §17 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
