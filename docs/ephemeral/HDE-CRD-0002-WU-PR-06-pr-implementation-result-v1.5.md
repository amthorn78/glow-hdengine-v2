---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.5"
record_kind: PR-35 checkpoint for the fifth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.4.md (v1.4, PR-35 checkpoint; blob 5b31c53c5309; 15,678 bytes; sha256 bc7b04df41de5d9311b86150f2fe8c079993c017ca7003cd5cbdf3b355619dc3); v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196 and be4000b, pushed; d9171d1b229eaa52b81bf11720cf4c4f8f561c4c (CX6-7 and CX6-8; parent be4000b); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T17:40Z
next_step: push d9171d1 and this record; answer and resolve the CX6-7 and CX6-8 threads; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.5 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `be4000b` raised two P2 findings on the install-step substitute: CX6-7 (an exclusive clause with a pre-release bound) and CX6-8 (the build system). Both are dispositioned by `d9171d1` and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-4 | Codex reviews 5571963225, 5573092833, 5573797059; P2 | `d2ed4fc` to `76483d7` | install-step substitute: versions, extras, entry points, requires-python | fixed in `2894628`, `302ab95`, `11d4aa5` (results v1.1 to v1.3); threads resolved |
| CX6-5, CX6-6 | Codex review 5574347631; threads `PRRT_kwDOP103ks6uAEwV`, `PRRT_kwDOP103ks6uAEwc`; P2 | `b7bc20b` | extras whitespace; substituted checkout inputs | fixed in `c9d9196` (result v1.4); replies r4316437996, r4316438808; threads resolved |
| CX6-7 | Codex review 5574868136 (on `be4000b`), comment r4316483301, P2 | `be4000b` | `tools/ci/prepush_check.py` 1180: with `pkg>1.0rc1` and an installed `pkg==1.0.post1`, "PEP 440 considers the installed version satisfactory", but the substitute rejects every same-release post-release when the bound is not a post-release, "a dependency change that pip would not make" | Partly confirmed. Measured (§5 item 6): every pip release up to 25.3 (vendored `packaging` 21.3, 24.1, 24.2, 25.0) rejects it, as the substitute did; pip 26.2.1 (vendored `packaging` 26.2) and `packaging` 26.3 accept it. Which pip CI runs is not recorded in its log, so neither answer is knowable offline. Disposition in `d9171d1`: where the two rules agree the substitute returns their answer; where they disagree it raises `AmbiguousClause`, a tooling failure naming the clause, instead of asserting either (§3) |
| CX6-8 | Codex review 5574868136, comment r4316483295, P2 | `be4000b` | `tools/ci/prepush_check.py` 1260: a candidate that changes `[build-system].build-backend` to an unimportable backend, or adds an unsatisfied build requirement, replays green while CI's `pip install -e .` fails; "validate the build system or fail closed instead of excluding it" | Substantive, in scope. `11d4aa5` had stated the isolated build environment as an offline limit; the finding shows a fail-closed proxy exists. Fixed in `d9171d1` (§3). Reproduced with the real step: a typo'd backend and `setuptools>=999` (§5 item 7) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

## 3. Correction CX6-7 and CX6-8 (`d9171d1`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `a88f12dd7e7e`; 1,611 lines; +57/−7 on `be4000b`) | **CX6-7.** `_satisfies` computes, for `<V` and `>V`, both pip's rule up to 25.x (exclude every pre-, post- or local release of V's release) and pip 26's rule (exclude only V's own family); equal results are returned, a disagreement raises `AmbiguousClause` (a `ValueError`, so the substitute reports it as a tooling failure; marker evaluation re-raises it rather than reading it as "not a version"). **CX6-8.** The editable project must declare a `[build-system]` with a `requires` list and a `build-backend`, and no `backend-path` (an in-tree backend), or the substitute fails closed. Its build requirements join the requirement closure, attributed to "`<project>`'s build-system", and its backend module must be locatable on the path by `importlib.machinery.PathFinder` without being imported or run. The `_install_check` docstring states the remaining limit: pip's isolated build environment is fetched from the package index, and these checks are its fail-closed proxy |
| `tests/tools/test_prepush_check.py` (blob `36975b3ff619`; 718 lines; +16) | The clause table asserts `AmbiguousClause` for four disagreeing forms (`1.0.post1` against `>1.0rc1`, `1.0rc1` against `<1.0.post1`, `1.0+local` against `>1.0rc1`, `1.0.post1` against `>1.0.dev1`); the agreeing forms keep their answers. The site case's candidate declares `[build-system] requires = ["buildreq>=1"]` and `build-backend = "fakebackend"`: the broken site now also reports `buildreq (not installed; required by proj's build-system)` and `proj build-backend fakebackend (not importable)`; the fixed site holds both; a project without `build-backend` and one without `requires` are refused. Still 34 cases |

## 4. CI on `be4000b`

Run 39288634263 (job 118183158615) on `be4000b`, 16:48:41Z to 17:01:13Z, completed on its own with conclusion `success`. It became stale when the re-review completed at 16:53:26Z with CX6-7 and CX6-8; it was not waited on and is not a gate, and its result covers `be4000b` only, whose code `d9171d1` changes. Cancellation was not attempted (refused through the same interface at result v1.2 §4).

## 5. Local validation of `d9171d1`

Environment as result v1.1 §5 (closed rails, keys unset, CPython 3.12.3 venv with CI's install and pip 24.0, `-e` re-pointed at the clone `cand` at `d9171d1`, `ruby` 3.3.6, `bash`, `curl`); three fresh scratch clones detached at `d9171d1`; `PYTHONPATH` the clone under test; exit statuses the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 34 passed in 43.5 s (concurrent with items 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..d9171d1`, `pull_request` | exit 0; `reason=selected_lanes;paths=8;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls, each in a throwaway clone at `d9171d1`, one guard disabled and committed there | NC-11 to NC-21 as result v1.4 §5 item 5, each failing as intended again. NC-22 (`AmbiguousClause` never raised): the clause-and-marker case fails. NC-23 (backend not located): the site case fails. NC-24 (build requirements not added to the closure): the site case fails. NC-25 (`[build-system]` shape not checked): the site case fails |
| 6 | pip's own clause decisions (scratch only; downloaded wheels used as data, never installed) | `pip index versions pip`: newest 26.2.1. Vendored `packaging`: pip 24.0 → 21.3, pip 24.2 → 24.1, pip 25.0 → 24.2, pip 25.2 and 25.3 → 25.0, pip 26.2.1 → 26.2. `>1.0rc1` against `1.0.post1`: False under 21.3, 24.1, 24.2 and 25.0; True under 26.2 and 26.3. Grid of `<V` and `>V` over same-release versions (two epochs, thirteen pre/post/dev tails, with and without local labels; 3,136 cases) against `packaging` 25.0 (pip 25.3) and 26.3, and again against 24.1 (pip 24.2): in every case the tool returns the shared answer where the two agree (2,876) and raises `AmbiguousClause` where they disagree (260); 0 mismatches. The earlier cross-checks still hold: `packaging` 26.3, 1,890 comparisons, 0 disagreements (`platform_machine === "x86_64"` raises in both); pip's vendored 21.3, 892 real marker evaluations, 0 disagreements |
| 7 | The real `ci.yml` install step through `_install_check` | (1) the CI venv: no unmet requirement; (2) a metadata copy without `psycopg-binary` (with a stub `setuptools.build_meta` module): exactly `psycopg-binary (not installed; required by psycopg)`; (3) `hdctl` target changed, (4) `requires-python = ">=3.13"`, (5) a `pytest11` entry point: exactly their lines as in result v1.3; (6) `build-backend = "setuptools.build_metaa"` (CX6-8): exactly `glow-hdengine build-backend setuptools.build_metaa (not importable)`; (7) `requires = ["setuptools>=999", "wheel"]` (CX6-8): exactly `setuptools 84.0.0 (needs >=999; required by glow-hdengine's build-system)`; (8) `_substitute` on the real step: `success` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 17:06:37Z to 17:40:06Z (concurrent with item 9); classify `reason=selected_lanes;paths=8`, all seven lanes; every one of the 16 steps SUCCESS; changed tests 166 targets, 3,920 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 2,002.8 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, HEAD and git metadata)`. `cand` before and after: `head=d9171d1…`, `status_lines=0`, `git_metadata_digest=65aae059febb9847005ab9214a33332f00879fc00779ba199f80d5fd27722fa7`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,220 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,697.3 s (17:06:38Z to 17:34:57Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Equal to result v1.4's count (the case count is unchanged) |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-5 | as results v1.1 to v1.4 §6 | unchanged | as recorded there |
| IF-35-6 | For an exclusive clause whose result depends on the pip release, the substitute fails closed (`AmbiguousClause`) instead of adopting either rule | CX6-7's premise holds for pip 26 and not for pip up to 25.3, and CI's pip release is not observable offline (its install log names no pip version). Instruction ID-9 makes a prerequisite the replay cannot establish a tooling failure, and plan PD-8 needs the substitute's outcome to be honest; asserting either rule would be a guess | §5 items 1, 5 (NC-22), 6 |
| IF-35-7 | The build-system check uses the caller's environment as a proxy: build requirements must be satisfied there and the backend module locatable there | pip builds in an isolated environment from the package index, which an offline replay cannot reproduce (instruction §7 "Network"). The proxy fails closed: a candidate whose build would break in CI fails here, and a candidate that needs a build requirement the caller lacks is a tooling failure the caller can fix by installing it | §5 items 1, 5 (NC-23 to NC-25), 7 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.4 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 16:48:12 | push 4 of PR-35: `b7bc20b..be4000b`, fast-forward, no force | `git rev-parse origin/claude/youthful-gauss-d9e0ab` = `be4000b…` |
| 16:48:31, 16:48:35 | replies r4316437996 (CX6-5) and r4316438808 (CX6-6); both threads resolved | GitHub |
| 16:48:56 | safety-net check-in scheduled for 17:39Z (`trig_01W6riki7o7tmt5WFCjrPpWF`); the 16:11Z one fired at 16:13Z (state had advanced) | it creates no session |
| 16:48:30 to 16:53:26 | Codex code review on `be4000b` (trigger "New commits"): review 5574868136, findings CX6-7 and CX6-8 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| ~16:55 to 17:00 | pip wheels 24.2, 25.0, 25.2, 25.3 and 26.2.1 downloaded into the scratch directory as data for §5 item 6 | scratch only; not installed; no repository effect |
| 17:04:47, 17:05:45 | local commit `8f4195a`, amended before any push to `d9171d1` (the `requires` list check) | §3 |
| 17:06:37 to 17:40:06 | local validation of `d9171d1`, all passed | §5 |
| after this record | push 5 of PR-35: `d9171d1` and the commit adding this record, fast-forward onto `be4000b`, no force | read back in the next record |
| next | answer the CX6-7 and CX6-8 threads naming `d9171d1`, and resolve them; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35 | pending |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment | stated limit; fail-closed proxy (IF-35-7) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (the replay needs a Linux machine; ambiguous clauses and build requirements are tooling failures); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
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
| In-flight scope | instruction v1.0 ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.7, PD-8, §6.1, §13 RK-3 and RK-5, §17 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
