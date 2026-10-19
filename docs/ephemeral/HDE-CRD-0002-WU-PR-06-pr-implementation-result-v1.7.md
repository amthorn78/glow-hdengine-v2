---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.7"
record_kind: PR-35 checkpoint for the seventh corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.6.md (v1.6, PR-35 checkpoint; blob 1d2c326dc483; 21,947 bytes; sha256 6687562605a752b333dbc9525c41d8ad9e80a8ae5420550f5aeed03840e3695a); v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4 and 36d292b, pushed; 2d567a364868189fa8c17217317fbd18ddd54ea4 (CX6-13 and CX6-14; parent 36d292b); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T19:46Z
next_step: push 2d567a3 and this record; answer the CX6-12, CX6-13 and CX6-14 threads and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.7 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `36d292b` raised three P2 findings: CX6-12 (runner variables read by scripts a step calls), CX6-13 (`persist-credentials` accepted with any value) and CX6-14 (the editable version compared without its local label). Nathan, the Product Owner, decided two things in this session (§2a): CX6-12 is declined, and every further Codex finding on this PR is to be fixed. `2d567a3` fixes CX6-13 and CX6-14 and is verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-8 | Codex reviews 5571963225 to 5574868136; P2 | `d2ed4fc` to `be4000b` | as results v1.1 to v1.5 | fixed or dispositioned in `2894628`, `302ab95`, `11d4aa5`, `c9d9196`, `d9171d1`; threads resolved |
| CX6-9 to CX6-11 | Codex review 5575476393; P2 | `b5694ae` | action revisions; runner variables; build backend | fixed in `1895e56` and `574bbd4` (result v1.6); replies r4317558294, r4317559149, r4317559674; threads resolved |
| CX6-12 | Codex review 5576227131 (on `36d292b`), comment r4317604555, P2 | `36d292b` | `tools/ci/prepush_check.py` 1467: inherited `GITHUB_*` and `RUNNER_*` values are removed, but `replay_steps` scans only `run:` text, so if "an existing invoked script such as `ci/checks/check_env_pins.sh`" were changed to read `GITHUB_SHA`, `GITHUB_WORKSPACE` or `RUNNER_OS`, "hosted CI supplies the variable while replay supplies an empty value"; "populate the modeled hosted values for child processes or otherwise fail closed on these transitive consumers" | **Declined by the Product Owner's decision PO-35-1 (§2a).** Path traced: no file that CI runs reads an unmodelled runner variable today (§5 item 6), so the divergence is hypothetical. Populating cannot be complete offline (the merge commit, the run id and the ref are unknown). Failing closed by scanning the tree would flag at least five unrelated tracked files today. The limit stays stated in the code (result v1.6 IF-35-8), and the tool's nonclaim covers it |
| CX6-13 | same review, comment r4317604565, P2 | `36d292b` | `tools/ci/prepush_check.py` 134: `persist-credentials` maps to `None`, so `true` is not drift; hosted checkout would then keep authentication for later commands, which the throwaway clone never has; "require the currently modeled `false` value" | Confirmed: at `36d292b`, the real `ci.yml` with `persist-credentials: true` was accepted. Fixed in `2d567a3` (§3) |
| CX6-14 | same review, comment r4317604543, P2 | `36d292b` | `tools/ci/prepush_check.py` 1391: `0.0.0+candidate` and an installed `0.0.0` share a `.key`, since `_parse_version` excludes the local label, so stale metadata is accepted that CI's editable install would update; "compare the complete normalized project versions, including local labels" | Confirmed: at `36d292b` the two keys compared equal. Fixed in `2d567a3` by comparing the two normalized version strings, which is stricter than the local label alone (IF-35-9) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

### 2a. Product Owner decisions in this session

| ID | Question put (verbatim) | Options offered | Decision |
| :- | :- | :- | :- |
| PO-35-1 | "Codex CX6-12 on PR #660: a script that a CI step calls (e.g. ci/checks/check_env_pins.sh) could read GITHUB_SHA, GITHUB_WORKSPACE or RUNNER_OS. Hosted CI supplies a value; the local replay now supplies nothing. No script CI runs today reads one. Exact values can't be known offline (merge commit, run id, ref), and a repo-wide scan would flag 5+ unrelated files today (VERIFY.sh's RUNNER_FAIL, the devcontainer script, OPS evidence, the owner test). How should I dispose of it?" | Decline, keep limit (recommended); Populate knowable values; Fail closed by tree scan | "Decline, keep limit (Recommended)" |
| PO-35-2 | "Each Codex round on this PR has found 2–3 new gaps in how faithfully the offline replay imitates the hosted runner (7 rounds, 14 findings so far). What rule should I apply to further findings of that kind on this PR?" | Fix if real and small (recommended); Fix every finding; Ask me each time | "Fix every finding" |

Both answers were given through the session's question tool before the local commit of 18:59:33Z. PO-35-2 governs every later round on this PR. Applying it, CX6-13 and CX6-14 are fixed.

## 3. Correction CX6-13 and CX6-14 (`2d567a3`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `75e63384cd5f`; 1,683 lines; +24/−2 on `36d292b`) | **CX6-13.** `REPLAY_SUBSTITUTED_INPUTS["actions/checkout@v4"]["persist-credentials"]` is now `"false"`, exactly and required. Any other value is `REPLAY_INVENTORY_DRIFT`. **CX6-14.** New `_normalized_version` returns a version's PEP 440 normal form: the epoch only if nonzero, release numbers as integers, `a`/`b`/`rc` with a number, `.postN`, `.devN`, and the local label lowercased, split at `.`, `-` or `_` and rejoined with `.`, with numeric segments as integers. The editable-project check compares the installed and the declared version as normalized strings, because CI's reinstall records the candidate's normalized string. `_parse_version` and `_Version` are unchanged |
| `tests/tools/test_prepush_check.py` (blob `06159a215dd8`; 767 lines; +15/−1) | A `checkout-credentials` drift case (`persist-credentials: true`). The site case also refuses candidate versions `0.2.0+candidate` and `0.2` against an installed `0.2.0`. A normalization table of twelve forms covers epochs, leading zeros, implicit and spelled post-releases, alternative pre-release spellings, implicit dev numbers and local labels. 40 cases (39 + 1) |

An intermediate local commit, `80c34b2` (18:59:33Z), compared PEP 440 keys plus the local label. Its integration check (§5 item 6, case D) showed that `0.0` against an installed `0.0.0` was still accepted, although CI's reinstall would record `0.0`. It was amended before any push into `2d567a3` (19:08:46Z). Its validation runs, started at 19:01Z, were stopped, and their temporary directories were removed. No result of theirs is cited.

## 4. CI on `36d292b`

Run 39305685720 (job 118242024630) on `36d292b` ran from 18:48:56Z to 19:10:00Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 18:54:02Z with CX6-12 to CX6-14. It was not waited on and is not a gate. Its result covers `36d292b` only, whose code `2d567a3` changes.

## 5. Local validation of `2d567a3`

Environment as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install and pip 24.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`. Clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `2d567a3` by fetch and checkout from the session's checkout. Before the runs, each had no untracked or ignored files and only its main worktree, once `cand2`'s ignored caches from the scratch integration scripts had been removed. `python -I` does not honour `PYTHONDONTWRITEBYTECODE`, so those scripts now run with `-B`. One fresh clone per negative control. `PYTHONPATH` is the clone under test. Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 40 passed in 43.6 s (concurrent with items 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..2d567a3`, `pull_request` | exit 0; `reason=selected_lanes;paths=10;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `2d567a3`, committed there | All 24 fail as intended, each clone clean afterwards. NC-11 to NC-32 fail exactly the cases they failed at `574bbd4` (result v1.6 §5 item 5). The one addition is NC-18 (unmodelled substituted inputs accepted), which now also fails the new `checkout-credentials` case, since that guard enforces CX6-13. NC-33 (`persist-credentials` back to any value): `checkout-credentials` fails. NC-34 (the editable version compared by PEP 440 key, as at `36d292b`): the site case fails |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2`; and the tree | (A) the CI venv: no unmet requirement. (B) `persist-credentials: true`: `REPLAY_INVENTORY_DRIFT: step 'Check out exact candidate head' has inputs the replay does not model: persist-credentials`. (C) `version = "0.0.0+candidate"`: exactly `glow-hdengine 0.0.0 (the candidate declares version 0.0.0+candidate)`. (D) `version = "0.0"`: exactly `glow-hdengine 0.0.0 (the candidate declares version 0.0)`. Result v1.6 §5 item 6's fifteen cases give the same results again. For CX6-12, every tracked file outside `docs/` was searched for runner-variable names. Among files that CI runs, the names that appear are modelled ones: in `ci/checks/classify_ci_changes.py` (`GITHUB_OUTPUT`, `RUNNER_TEMP`), in two evidence tests (`GITHUB_TOKEN`, `RUNNER_TEMP`), and in the owner test and the tool, where other names are test data and the scan's own patterns. The other hits, none run by CI, are `VERIFY.sh` and `.audit_src/VERIFY.sh` (their own `RUNNER_FAIL`), `.audit_src/n` and `.devcontainer/scripts/codespaces-extension-doctor.sh` (Codespaces names), three OPS evidence files and an OPS command list under `audit/ops/` |
| 7 | `_normalized_version` against `packaging` 26.3 and pip 24.0's vendored 21.3 (scratch only) | 19,800 generated versions: nine release forms × eleven pre-release × eight post-release × five dev × five local spellings. All are valid for `packaging`, and the three normal forms agree in every case, 0 mismatches. 22 edge and malformed forms: refused by all three, or normalized identically, 0 mismatches. The earlier PEP 440/508 cross-checks and the 3,136-case pip-rule grid are not rerun, since `_parse_version`, `_satisfies`, the requirement and marker parsers, and `_unmet_requirements` are unchanged |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 19:09:52Z to 19:45:14Z (concurrent with item 9); classify `reason=selected_lanes;paths=10`, all seven lanes; every one of the 16 steps SUCCESS; changed tests 166 targets, 3,926 passed (result v1.6's 3,925 plus the one new case); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 2,115.9 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, HEAD and git metadata)`. `cand` before and after: `head=2d567a3…`, `status_lines=0`, `git_metadata_digest=9648479b207387a9d1af7590849692c88176c794caa801a7c9f82c3535066e53`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,226 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,767.3 s (19:09:52Z to 19:39:22Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.6's 5,225 plus the one new owner-test case; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-8 | as results v1.1 to v1.6 §6 | unchanged | as recorded there |
| IF-35-9 | The editable version check compares normalized version strings, not PEP 440 equality plus the local label. So `0.2` against an installed `0.2.0` is reported too, although PEP 440 calls them equal | CX6-14's root cause is that the replay keeps installed metadata which CI's reinstall would rewrite. That metadata records the candidate's normalized string, and `importlib.metadata` consumers read the string, so only string equality guarantees that the reinstall changes nothing. This follows the finding's own words, "the complete normalized project versions" | §5 items 1, 5 (NC-34), 6 (C, D), 7 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.6 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 18:48:48 | push 6 of PR-35: `b5694ae..36d292b` (`1895e56`, `574bbd4`, the v1.6 record), fast-forward, no force | remote head `36d292b…`; v1.6 read back from the remote: blob `1d2c326dc483`, 21,947 bytes, sha256 equal to the local file |
| 18:49:07 to 18:49:16 | replies r4317558294 (CX6-9), r4317559149 (CX6-10) and r4317559674 (CX6-11); the three threads resolved | GitHub |
| 18:49:01 to 18:54:02 | Codex code review on `36d292b` (trigger "New commits"): review 5576227131, findings CX6-12 to CX6-14 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 18:48:56 to 19:10:00 | CI run 39305685720 on `36d292b`: success, stale | §4 |
| before 18:59:33 | PO-35-1 and PO-35-2 | §2a |
| 18:59:33, 19:08:46 | local commit `80c34b2`, amended before any push into `2d567a3` | §3 |
| 19:01 to 19:08 | validation runs of `80c34b2` started, then stopped; their two temporary directories removed | §3 |
| 19:12:42 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved from 19:35Z to 20:40Z, after the round-8 push; it carries the PO-35-2 rule | it creates no session |
| 19:09:52 to 19:45:14 | local validation of `2d567a3`, all passed | §5 |
| after this record | push 7 of PR-35: `2d567a3` and the commit adding this record, fast-forward onto `36d292b`, no force | read back in the next record |
| next | answer the CX6-12 thread with the decision and the traced path, and CX6-13 and CX6-14 naming `2d567a3`; resolve the three; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment | stated limit; one modelled build system plus the fail-closed proxy (IF-35-7) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (as result v1.6 §8); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
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
