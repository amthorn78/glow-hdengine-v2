---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.6"
record_kind: PR-35 checkpoint for the sixth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.5.md (v1.5, PR-35 checkpoint; blob e4175f2a960d; 17,044 bytes; sha256 ae95af975d8ab9f032835e05056a812f17f48a5e56b6b363de7a30c2d5ec2fa8); v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1 and b5694ae, pushed; 1895e56a489ad150fc5a04436b555ee51c9baf9e (CX6-9, CX6-10 and CX6-11; parent b5694ae); 574bbd43fa57b1c50c6cc42082372f4fd6d9dff2 (owner-test fix found by negative control NC-30; parent 1895e56); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T18:48Z
next_step: push 1895e56, 574bbd4 and this record; answer and resolve the CX6-9, CX6-10 and CX6-11 threads; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.6 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `b5694ae` raised three P2 findings on the replay's substitutes: CX6-9 (action revisions), CX6-10 (runner environment variables) and CX6-11 (the build backend's hook target). They share one root cause with CX6-6 and CX6-8: where the replay stands in for something hosted CI provides, it accepted values it does not model. `1895e56` fixes that root cause: the replay now accepts exactly what it models and refuses everything else. `574bbd4` corrects one line of the owner test, found by negative control NC-30. Both are verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-6 | Codex reviews 5571963225, 5573092833, 5573797059, 5574347631; P2 | `d2ed4fc` to `b7bc20b` | install-step substitute (versions, extras, entry points, requires-python, extras whitespace); substituted checkout inputs | fixed in `2894628`, `302ab95`, `11d4aa5`, `c9d9196` (results v1.1 to v1.4); threads resolved |
| CX6-7, CX6-8 | Codex review 5574868136; P2 | `be4000b` | exclusive clause with a pre-release bound; the build system | dispositioned in `d9171d1` (result v1.5); replies r4316927481, r4316928123; threads resolved |
| CX6-9 | Codex review 5575476393 (on `b5694ae`), comment r4316977522, thread `PRRT_kwDOP103ks6uCQf0`, P2 | `b5694ae` | `tools/ci/prepush_check.py` 976: "splitting at `@` discards" a change of `actions/checkout@v4` or `actions/setup-python@v5` to "a nonexistent or behaviorally different revision", so the replay still substitutes success; "treat the supported revision as part of the modeled action identity" | Confirmed: at `b5694ae`, `replay_steps` accepted the real `ci.yml` with `actions/checkout@v5`. Fixed in `1895e56` (§3) |
| CX6-10 | same review, comment r4316977538, thread `PRRT_kwDOP103ks6uCQf_`, P2 | `b5694ae` | `tools/ci/prepush_check.py` 1417: a step changed to read `GITHUB_SHA`, `GITHUB_WORKSPACE` or `RUNNER_OS` "observes an absent or caller-inherited value rather than the value hosted CI provides"; "populate the supported runner environment consistently or reject run text that references unmodeled runner variables" | Confirmed: at `b5694ae`, `replay_steps` accepted the classify step with `--base "$GITHUB_SHA"`, and the replay's environment was built from the caller's whole environment, so the caller's own `GITHUB_*` values reached the steps. Fixed in `1895e56` by rejection, since values such as the run id and the merge ref cannot be known offline; the same root cause in expression contexts is fixed with it (§3, IF-35-8) |
| CX6-11 | same review, comment r4316977533, thread `PRRT_kwDOP103ks6uCQf8`, P2 | `b5694ae` | `tools/ci/prepush_check.py` 1320: an importable but invalid backend (`json`) or a missing object (`setuptools.build_meta:no_such_backend`) passes, since only the module before `:` is checked; "validate the complete backend target and required hooks, or refuse any backend identity not known to be equivalent" | Confirmed: at `b5694ae`, with the real install step and the CI venv, both forms reported no unmet requirement. Fixed in `1895e56` by the second option: the build system must be the one the replay models (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

## 3. Correction CX6-9, CX6-10 and CX6-11 (`1895e56`, `574bbd4`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `9103bdfb2c80`; 1,661 lines; +85/−35 on `b5694ae`) | **CX6-9.** `REPLAY_SUBSTITUTED_INPUTS` is keyed by the full `uses` string, revision included (`actions/checkout@v4`, `actions/setup-python@v5`). Any other revision is `REPLAY_INVENTORY_DRIFT`. **CX6-10.** `replay_steps` refuses, as `REPLAY_INVENTORY_DRIFT`, a step whose `run` text names a runner variable the replay does not model, and a step or job `env` that sets one. Runner variables are any `GITHUB_*`, `RUNNER_*` or `ACTIONS_*` name, `ImageOS`, `ImageVersion`, and setup-python's `pythonLocation` and `Python*_ROOT_DIR`. The modelled ones are those the replay sets (`GITHUB_ACTIONS`, `GITHUB_EVENT_NAME`, `GITHUB_OUTPUT`, `RUNNER_TEMP`) and those it removes, which stay absent as on a hosted runner (`REMOVED_ENV_KEYS`, for example `GITHUB_TOKEN`). Every inherited runner variable is removed from the replay's environment, so a script a step calls sees only the modelled ones and never the caller's. Expressions get the same rule: a `github` context path outside `REPLAY_GITHUB_PATHS` fails as tooling where its value is used, and so do `github.sha` and `github.event.before` on a `pull_request` event, where the merge commit and the payload's `before` are unknown offline; where `\|\|` discards them they are harmless. The unused `env` context is dropped, so `${{ env.* }}` is refused too. The contexts are built by `replay_contexts`. **CX6-11.** The editable project's `[build-system]` must equal `REPLAY_BUILD_SYSTEM`, `{build-backend: setuptools.build_meta, requires: [setuptools>=68, wheel]}`. setuptools provides PEP 660 hooks from release 64, so every release `setuptools>=68` admits has them. Another backend, a `module:object` target, other requirements, a `backend-path` or a missing key fails closed. The caller's environment must still satisfy the requirements and hold the backend's module |
| `tests/tools/test_prepush_check.py` (blob `8d4320925cde`; 753 lines; +47/−12) | Five new drift cases: `checkout-revision`, `setup-python-revision`, `runner-variable-in-run` (`$GITHUB_SHA` in run text), `runner-variable-step-env` (`RUNNER_OS` in a step env) and `runner-variable-job-env` (`GITHUB_WORKSPACE` in the job env). The expressions case checks `replay_contexts` for both events. On `pull_request`, the two `\|\|` forms of `ci.yml` still evaluate, while `github.sha`, `github.event.before == 'x'`, `github.run_id`, `github.workspace`, `github.event.pull_request.title` and `env.LC_ALL` are refused, including as a condition. On `push`, `github.sha` and `github.event.before` evaluate. The site case's candidate now declares the modelled build system. The broken site lacks `wheel` and setuptools' `build_meta` module; the fixed site holds both. `json`, `setuptools.build_meta:no_such_backend`, `setuptools>=40`, an added `backend-path`, and a missing `build-backend` or `requires` are each refused. The synthetic replay sets `GITHUB_SHA`, `RUNNER_OS` and `GITHUB_WORKSPACE` in the caller's environment, and a script that a step calls must see none of them. 39 cases (34 + 5) |
| `tests/tools/test_prepush_check.py` at `574bbd4` (blob `df40b5b56d02`; 753 lines; +1/−1 on `1895e56`) | The called script now starts with `set -e`. At `1895e56` its passing last line hid a failed first check, so NC-30 (inherited runner variables kept) still passed the owner test (§5 item 5). The tool is unchanged |

## 4. CI on `b5694ae`

Run 39296242182 (job 118209401467) on `b5694ae` ran from 17:41:13Z to 18:02:16Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 17:46:50Z with CX6-9 to CX6-11. It was not waited on and is not a gate. Its result covers `b5694ae` only, whose code `1895e56` changes. Cancellation was not attempted; it was refused through the same interface at result v1.2 §4.

## 5. Local validation of `1895e56` and `574bbd4`

Environment as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install and pip 24.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`. Fresh scratch clones replace the earlier ones: `cand` (replay), `cand2` (short checks) and `sweep`, detached at `1895e56`; `cand3` and one clone per negative control, detached at `574bbd4`. `PYTHONPATH` is the clone under test. Exit statuses are the producer's own. Tested states: items 2, 4, 6, 8 and 9 ran at `1895e56` only; `574bbd4` differs from it by the one owner-test line in §3; items 1, 3 and 5 ran at both.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test | `1895e56` (`cand2`): 39 passed in 39.6 s, exit 0. `574bbd4` (`cand3`): 39 passed in 45.0 s, exit 0. Both concurrent with items 8 and 9 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..1895e56` and `0442d23..574bbd4`, `pull_request` | each exit 0; `reason=selected_lanes;paths=9;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone, committed there | At `1895e56`, NC-11 to NC-29, NC-31 and NC-32 each failed as intended, and NC-30 (inherited runner variables kept) passed: the gap `574bbd4` closes. At `574bbd4`, all 22 fail as intended, each clone clean afterwards. NC-11 to NC-25 fail the same cases as at result v1.5 §5 item 5, with NC-23 to NC-25 retargeted to the new build-system code. NC-26 (revision ignored): `checkout-revision` and `setup-python-revision` fail. NC-27 (run text not scanned): `runner-variable-in-run` fails. NC-28 (step env keys not checked): `runner-variable-step-env` fails. NC-29 (job env keys not checked): `runner-variable-job-env` fails. NC-30 (inherited runner variables kept): both synthetic replay cases fail. NC-31 (`github` paths not restricted) and NC-32 (`github.sha` modelled on `pull_request`): the expressions case fails |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` | (1) the CI venv: no unmet requirement. (2) A metadata copy without `psycopg-binary`: exactly `psycopg-binary (not installed; required by psycopg)`. (3) An `hdctl` target change, (4) `requires-python = ">=3.13"` and (5) a `pytest11` entry point: exactly their lines as in result v1.3. (6) `setuptools.build_metaa`, (7) `json`, (8) `setuptools.build_meta:no_such_backend` and (9) `setuptools>=999` are each refused as "not the one the replay models". (6) and (9) were reported as unmet at result v1.5; they now fail closed earlier. (10) `_substitute` on the real step: `success`. (11) `replay_steps` on the real workflow: 16 steps. (12) `--base "$GITHUB_SHA"` in the classify step: `REPLAY_INVENTORY_DRIFT: step 'Classify affected CI lanes' names runner variables the replay does not model: GITHUB_SHA`. (13) `actions/checkout@v5`: `REPLAY_INVENTORY_DRIFT: … uses 'actions/checkout@v5', which the replay does not model`. (14) Every step-env expression in `ci.yml` evaluates under both events, the classify step's `BASE_SHA`/`HEAD_SHA` to the base and head. (15) `${{ github.sha }}` alone: refused on `pull_request`, the head on `push` |
| 7 | Earlier cross-checks (PEP 440/508 against `packaging` 26.3 and pip's vendored 21.3; the 3,136-case pip-rule grid) | not rerun: `1895e56` does not touch the version, clause, marker or closure code. `_Version`, `_parse_version`, `_clause`, `_parse_clauses`, `_parse_requirement`, `_parse_marker`, `_marker_environment`, `_marker_true`, `_satisfies` and `_unmet_requirements` are source-identical to `d9171d1` (compared by AST segment); the owner test's clause table passes |
| 8 | `replay --base 0442d23…` from `cand` (at `1895e56`) | exit 0; 18:01:33Z to 18:36:13Z (concurrent with item 9); classify `reason=selected_lanes;paths=9`, all seven lanes; every one of the 16 steps SUCCESS; step 05 "the environment already satisfies every requirement the step names, their dependencies and extras, and the editable project's build system, version and entry points"; changed tests 166 targets, 3,925 passed (result v1.5's 3,920 plus the 5 new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 2,074.4 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, HEAD and git metadata)`. `cand` before and after: `head=1895e56…`, `status_lines=0`, `git_metadata_digest=70c26fd8d9fb7ddf11c0398d907c39b22b696f0df7f8065de174794274f7c6f8`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`, at `1895e56`), `XDG_STATE_HOME` an empty scratch directory | **5,225 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,696.2 s (18:01:33Z to 18:30:00Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.5's 5,220 plus the 5 new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-6 | as results v1.1 to v1.5 §6 | unchanged | as recorded there |
| IF-35-7 | The build-system proxy of result v1.5 is narrowed: the `[build-system]` must equal the one modelled build system. The caller's environment is still the proxy for its requirements and backend module | CX6-11 showed that checking only a backend's module cannot establish the PEP 517/660 hooks. Verifying hooks would mean importing and running the candidate's backend, which the tool's read-only, offline posture rules out (instruction §7). Refusing any other identity is the fail-closed choice | §5 items 1, 5 (NC-23 to NC-25), 6 |
| IF-35-8 | Closed world for every substituted identity. The replay accepts exactly the action revisions, runner variables, `github` context paths and build system it models. Anything else is drift or a tooling failure, and inherited runner variables are removed. This goes beyond the findings' text in two places: expression contexts (`github.*` paths, plus `github.sha` and `github.event.before` on `pull_request`) and the removal of inherited runner variables | Ten of the eleven findings across six review rounds (all but CX6-7) had one root cause: a substitute that accepted something it does not model. Contract G-3 already makes drift in the step inventory force a tool update in the same PR. Extending that rule to the substituted identities closes the root cause, rather than one instance per round. Plan PD-8 requires the substitute's outcome to be honest. Consequence: a PR that changes an action revision, the `[build-system]` table, or a step's runner-variable use gets a TOOLING failure from the replay until the tool's tables are updated. Hosted CI is unaffected. Limit, stated in the code: scripts a step calls are not scanned; they see only the modelled variables | §5 items 1, 5 (NC-26 to NC-32), 6 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.5 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 17:41:06 | push 5 of PR-35: `be4000b..b5694ae` (`d9171d1` and the v1.5 record), fast-forward, no force | `git rev-parse origin/claude/youthful-gauss-d9e0ab` = `b5694ae…`; v1.5 read back |
| 17:41:36, 17:41:40 | replies r4316927481 (CX6-7) and r4316928123 (CX6-8); both threads resolved | GitHub |
| 17:41:58 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` scheduled for 18:32Z. At 18:06 it was moved to 19:35Z, after the round-7 push, rather than letting it fire mid-validation | it creates no session |
| 17:41:13 to 17:46:50 | Codex code review on `b5694ae` (trigger "New commits"): review 5575476393, findings CX6-9 to CX6-11 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 17:41:13 to 18:02:16 | CI run 39296242182 on `b5694ae`: success, stale | §4 |
| 18:00:35, 18:24:16 | local commits `1895e56` and, after NC-30, `574bbd4` | §3, §5 item 5 |
| 18:01:33 to 18:47:43 | local validation of `1895e56` and `574bbd4`, all passed | §5 |
| after this record | push 6 of PR-35: `1895e56`, `574bbd4` and the commit adding this record, fast-forward onto `b5694ae`, no force | read back in the next record |
| next | answer the CX6-9 to CX6-11 threads naming `1895e56`, and resolve them; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35 | pending |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment | stated limit; one modelled build system plus the fail-closed proxy (IF-35-7) | recorded |
| Scripts a step calls are not scanned for runner variables | stated limit (IF-35-8); they see only the modelled variables | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note: the replay needs a Linux machine. Ambiguous clauses, build requirements, an unmodelled build system and unmodelled runner variables are tooling failures. OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
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
| In-flight scope | instruction v1.0 ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.7, PD-8, §6.1, §13 RK-3 and RK-5, §17; contract G-3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
