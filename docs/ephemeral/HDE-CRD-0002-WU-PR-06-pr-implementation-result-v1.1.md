---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.1"
record_kind: PR-35 checkpoint for the first corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; blob b506bff32c5c; 27,679 bytes; sha256 e4e37e317cba7b6eff6cffc315c6d52064b596583af5d5242a5b3040917aff37; read in full). Preserved unchanged; this v1.1 is its PR-35 successor in the same lineage
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-06
work_unit_title: "Read-only pre-push and pre-plan check (PR; Distillation; S20)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob f3a6a8855ec0; read in full)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0.md (v1.0; blob 2848847e8bee; read in full)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
REMEDIATION_REVIEW_ID: none
effective_baseline: unchanged from result v1.0 (approved base + PF10 addenda 2.2, 2.3, 2.4, 2.5, 2.9, 2.10)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md (v13.6.1; sha256 ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e; docs/pfcanon/ on origin/main 0442d23 last changed by 5e62a65; the unique controlled PF10). Provenance, not a gate
pf10_addendum_created: none (PR-35 is not an approval prompt)
proceed: the original Proceed of result v1.0 (Nathan's PR-30 invocation for plan v1.0). No other Proceed exists or is needed
session: the dedicated HDE-CRD-0002 WU-PR-06 PR-35 session (session_disposition NEW_DEDICATED), https://claude.ai/code/session_01SVmct81WDzDqX36ZasAijn, entered from result v1.0's handoff pasted by Nathan
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15.569Z; read in full); primary skill glow-hde-pr-development 1.4.0; support skill glow-write-boundary
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2 (cloud container)
pull_request: amthorn78/glow-hdengine-v2#660 (https://github.com/amthorn78/glow-hdengine-v2/pull/660), opened by PR-30 at 2026-10-19T13:00:14Z from branch claude/youthful-gauss-d9e0ab into main. Recorded here at PR-35 entry, because result v1.0 was pushed before the pull request existed
commits_this_phase: 28946280682174d394ceddcbbfadee451d3dac7c (correction CX6-1; parent d2ed4fc); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T14:25Z
next_step: push this record with 2894628; reply to and resolve the CX6-1 thread; read the Codex re-review and hosted CI of the new head over the active subscription; result v1.2
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.1 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex code review of [amthorn78/glow-hdengine-v2#660](https://github.com/amthorn78/glow-hdengine-v2/pull/660) raised one P2 finding, CX6-1: the replay's install-step substitute checked only that each named distribution was installed, not that its version satisfies the step's requirement specifiers. CX6-1 is corrected by `2894628` and verified locally (§4, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in v1.2.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Entry recovery (2026-10-19T13:36Z to 13:40Z)

| Check | Observation |
| :- | :- |
| Pull request | #660 open, not draft, not merged; head `claude/youthful-gauss-d9e0ab` at `d2ed4fc`; base `main` at `0442d23` = `origin/main`; 2 commits (`d9a0858`, `d2ed4fc`); 4 files (+2,068); `mergeable_state: clean` |
| Local and remote | Fresh container checkout on the session's default branch `claude/wizardly-gates-m8at0w` at `0442d23`, clean, no commits of its own. The pull request's branch existed on the remote; a tracking branch was created from it at `d2ed4fc`, clean |
| Artifact lineage | result v1.0 (PR-30) read in full; plan v1.0 read in full (§5.7 for the install substitute, §6 change set, §13 RK-5, §17 PR-35 duties); instruction v1.0 read in full (ID-8, ID-9, ID-12, §6, §7, §12, §14, §15); no PR-35 record for WU-PR-06 existed |
| Tree identity | `git diff --name-only d9a0858 d2ed4fc` adds only result v1.0 under `docs/ephemeral/`: the entry head's code tree is the one PR-30 validated |
| Earlier cycles | none: plan cycle 1 of WU-PR-06 |
| Subscription | active at entry for #660 (the tool result confirmed that this session receives its events) |
| Repository skills | `.claude/skills/steward/SKILL.md` and `.claude/skills/babysit/SKILL.md` are absent on the head branch |

## 3. Review matrix

| ID | Source | Head | Location | Finding | Classification | Disposition |
| :- | :- | :- | :- | :- | :- | :- |
| CX6-1 | Codex code review (`chatgpt-codex-connector[bot]`), review 5571963225, thread `PRRT_kwDOP103ks6t7foX` (comment r4314148300), P2 | `d2ed4fc` (summary comment 6267808148: code review on `d2ed4fc` completed, `has_unresolved_findings: true`) | `tools/ci/prepush_check.py` 965–966 (`_install_check`) | "this presence-only lookup accepts" a distribution installed at a version outside the workflow's constraints, for example pytest 9 under `requirements-dev.txt`'s `pytest<9.0`, "and substitutes the dependency-install step as successful"; the replay then runs against dependencies CI's install would replace | Substantive in-scope correction. Verified against the code: `_install_check` matched only a leading name and called `importlib.metadata.distribution(name)`; specifiers were discarded. Plan §5.7 and PD-8 state the substitute's purpose ("the final audit runs with honest outcomes", PD-8); a wrong-version environment defeats it, and ID-9/C3 class that state as a tooling failure | Fixed in `2894628` (§4); thread reply and resolution after the push (§7) |
| — | Codex security review | — | — | not part of the review chain (PF10 addendum 2.3) | not applicable | none needed |
| — | Human review | — | — | none requested or present | — | — |

## 4. Correction CX6-1 (`2894628`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `e25ecfa01d34`; 1,312 lines; +96/−13 on `d2ed4fc`) | `_install_check` parses each requirement the install step names (`-r` files read from the copy, literal words, the `-e` project's name) into a name, optional extras and comma-separated clauses, and checks the installed version against every clause. A standard-library PEP 440 matcher: `==`, `!=`, `<`, `<=`, `>`, `>=`, `~=` and `==`/`!=` with `.*`, on release versions; installed pre-, post-, dev- and local releases ordered as PEP 440 orders them, with the `<` pre-release and `>` post/local exclusions; an installed pre-release counts, as pip's own check of an installed distribution counts it. A marker, URL, `===`, a pre/post/dev/local/epoch clause, a trailing comma or an installed version that is not PEP 440 raises `ValueError`, which `_substitute` already reports as `TOOLING cannot read the install step's inputs` (fail closed). An unmet requirement is reported as `TOOLING the caller's environment does not satisfy the install step: <name> <installed> (needs <clauses>)` or `<name> (not installed)`. No dependency is added; the tool still imports only the standard library |
| `tests/tools/test_prepush_check.py` (blob `1077ee1207ec`; 600 lines; +48) | `test_install_substitute_requires_versions_the_specifiers_allow`, 5 parametrized cases built from the installed pytest version: satisfied, wildcard, version outside the specifier (the finding's case), missing distribution, unsupported form; `test_version_clauses_follow_pep_440`, a clause table (trailing zeros, local labels, pre-release at `<`, post and local at `>`, `~=`, wildcards, dev ordering, epochs) plus the refused forms. The owner test goes from 21 to 27 cases |

The commit was first made as `f13fc07` (unpushed). Its replay showed the step 05 detail repeating "at a version its specifiers allow" (once in the edited inventory reason, once in the success text); the reason string was restored to its v1.0 wording and the unpushed commit amended to `2894628` before any push. All validation in §5 ran on `2894628`.

## 5. Local validation of `2894628`

Closed rails throughout (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), with `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HD_GEOCODE_KEY`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `GH_TOKEN`, `GITHUB_TOKEN` and `ENGINE_ENV` unset (the container sets six of them). CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`; pytest 8.4.2; `-e` of the clone `cand`); `ruby` 3.3.6 at `/usr/local/bin/ruby`, `bash`, `curl`; git 2.43.0. Three scratch clones of the session's checkout, each detached at `2894628`: `cand` (replay only), `cand2` (short checks), `sweep`; `PYTHONPATH` the clone under test (OBS-W5-5). Exit statuses are the producer's own (`$?` of the unpiped command).

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py` (`cand2`) | 27 passed in 47.1 s (concurrent with the replay and the sweep), exit 0 |
| 2 | Pin and neighbouring files, one at a time (`cand2`) | `test_rails_ci_workflow_integration.py` 138, `test_http_reader_ci_ownership.py` 4, `test_architecture_snapshot.py` 5, `test_epic020_bundle_tool.py` 6 passed; each exit 0 |
| 3 | Classifier `0442d23..2894628`, `pull_request`, full SHAs | exit 0; `reason=selected_lanes;paths=4;lanes=product,compat,db,rails,evidence,qa,release`; `changed_tests=true`; 166 targets, `tests/tools/test_prepush_check.py` among them. (`d2ed4fc..2894628`: `paths=2;lanes=product,release`, 1 target) |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC`, exit 0 |
| 5 | Negative controls, each in a throwaway clone at `2894628` with the guard disabled and committed there | NC-11 (version check skipped, presence-only as before): `test_install_substitute_requires_versions_the_specifiers_allow[version-outside-specifier]` fails (1 failed, 26 passed). NC-12 (unsupported forms accepted): `[unsupported-form]` and `test_version_clauses_follow_pep_440` fail (2 failed, 25 passed) |
| 6 | PEP 440 cross-check (scratch only, not a deliverable): the tool's `_parse_requirement`, `_parse_version` and `_satisfies` against `packaging` 26.3 (`SpecifierSet.contains(..., prereleases=True)`; `Version` order of public versions), loaded by path from `cand2` | 57 versions × 34 specifiers plus 57 × 57 orderings: 5,187 comparisons, 0 mismatches; every refused form refused |
| 7 | `replay --base 0442d23…` from `cand` (all seven lanes: the classifier is in the pull request's diff) | exit 0; 13:50:46Z to 14:24:04Z (concurrent with item 8); classify `reason=selected_lanes;paths=4`, all seven lanes; every one of the 16 steps SUCCESS; step 05 (install substitute) "every named distribution is installed at a version its specifiers allow"; changed tests 166 targets, 3,913 passed (result v1.0's 3,907 plus the 6 new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,992.1 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, HEAD and git metadata)`. `cand` before and after: `head=2894628…`, `status_lines=0`, `git_metadata_digest=0fef8999512ae308731feb7d7dfd5aeec11a59e7bc7a19245ee26a25e160c8e6`, identical; no temporary directory left |
| 8 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,213 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,640.9 s (13:50:46Z to 14:18:10Z, concurrent with item 7); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.0's 5,207 plus the 6 new cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 | This phase's commits go to the pull request's branch `claude/youthful-gauss-d9e0ab`, not to the session's default branch `claude/wizardly-gates-m8at0w` | The handoff continues #660; the work unit keeps one branch and one pull request per plan cycle (GCF-17 continuity). Same decision as WU-PR-05 result v1.1 IF-35-1 | remote head read back after the push (§7) |
| IF-35-2 | CX6-1 is corrected with a standard-library PEP 440 subset that fails closed, not with the third-party `packaging` library | Instruction §7 "No new dependency" and plan PD-8's standard-library rule for the replay; no repository code imports `packaging`, which CI installs only as pytest's dependency. The subset covers every form the install step names today (`>=`, `<`, `==`, extras); any other form is a tooling failure rather than a silent pass | §5 items 1, 5 and 6 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.0 §10)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 13:00:14 | #660 opened by PR-30 from `claude/youthful-gauss-d9e0ab` | GitHub `created_at` |
| 13:00:22 to 13:21:45 | CI run 39256496826, job 118073002562, on `d2ed4fc`: `success` | check run; job log read in full (913 lines, the API's original length 913): classifier `BASE_SHA 0442d23`, `HEAD_SHA d2ed4fc`, `paths=4`, all seven lanes; changed tests 3,907 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 120, 113, 155 and 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. Runner image `ubuntu-24.04`, version `20261012.334.1`; `ruby`'s version is not printed (O-6 stands); hosted install pytest 8.4.2, psycopg 3.2.13 |
| 13:05:12 | Codex code review on `d2ed4fc`: review 5571963225, one P2 finding (CX6-1) | §3 |
| 13:37 | PR-35 entry: subscription confirmed; pull request, reviews, threads, summary comment, commits and check runs read | §2 |
| after entry | run 39256496826 treated as stale: the head it tested needs CX6-1. It had already completed; nothing to cancel | not a gate |
| 13:44:49 | local commit `f13fc07` (unpushed) | §4 |
| 13:45:39 to ~13:49 | replay of `f13fc07` started, stopped by SIGINT after step 07 (the tool removed its temporary directory; the clone stayed clean) | §4 |
| 13:49:55 | `f13fc07` amended locally to `2894628`, before any push | §4 |
| 13:50:46 to 14:24:04 | local validation of `2894628`, all passed | §5 |
| after this record | push 1 of PR-35: `2894628` and the commit adding this record, fast-forward onto `d2ed4fc`, no force | remote head read back in v1.2 |
| next | reply on thread `PRRT_kwDOP103ks6t7foX` naming `2894628`, and resolve it; read the Codex re-review and hosted CI of the new head | v1.2 |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or cancelled. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35 | pending (v1.2) |
| Extras: the substitute checks the named distribution's version, not the distributions an extra pulls in (`psycopg[binary]` → `psycopg-binary`); a nested `-r` or option line inside a requirements file is skipped, as in v1.0 | IA through PR-40, as a later candidate | recorded; not in CX6-1's scope (the finding names version specifiers) |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands: image recorded (§7), version not printed |
| WU-DOC-01 usage note; OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

Read on `main` at `0442d23` (`docs/pfcanon/` unchanged since `5e62a65`; this branch changes no canon).

| Topic | Sources and sections |
| :- | :- |
| Phase authority, review chain, merge boundary | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (all sections); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (PR implementation runs the normal code/security/review and evidence chain; one Proceed per detailed PR plan; merges are Product Owner actions) and §9.1.2 (canon on `main`; in-flight documents govern within their scope) |
| Review chain overlay | PF10-HDE-Build-Notes v13.6.1 addendum 2.3 (Rules 1 to 5: the Codex security review is not part of the chain; the Codex code review is read and resolved as before) |
| Tooling vs behavior | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 ("Import-time dependency failures are tooling, not behavior"): an unmet install requirement stays a tooling failure |
| In-flight scope | instruction v1.0 ID-8 (excluded install step; "the caller's environment must already have CI's install"), ID-9 (missing dependency is tooling), ID-12, §6, §7 "No new dependency", §12; plan v1.0 §5.7, PD-8, §6.1, §13 RK-5, §17 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" (exit codes from the producer's own status) |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
