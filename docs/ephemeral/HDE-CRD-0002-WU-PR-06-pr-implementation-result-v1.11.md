---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.11"
record_kind: PR-35 checkpoint for the eleventh corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.10.md (v1.10, PR-35 checkpoint; blob 7ba2d03ad6a5; 19,533 bytes; sha256 79ae79d7b67afe81872c583ae072fb841478f6ebb83d88da568eca37f83cdd65); v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54 and 14a5858, pushed; 7fc63d63f69fe82897247c64cc9da66a7174925c (CX6-25 to CX6-27; parent 14a5858); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T23:10Z
next_step: push 7fc63d6 and this record; answer the CX6-25 to CX6-27 threads naming 7fc63d6 and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.11 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `14a5858` raised three P2 findings:

- CX6-25: a second workflow job is ignored.
- CX6-26: a structured env value is accepted.
- CX6-27: `project = []` raises a `TypeError` that escapes the post-run read-only check.

Under PO-35-2 all three are fixed in `7fc63d6`, with their root-cause siblings (IF-35-13), and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-20 | Codex reviews 5571963225 to 5577595526 | `d2ed4fc` to `89e0828` | as results v1.1 to v1.9 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-21 to CX6-24 | Codex review 5578082885; P2 | `2c6dd5c` | runner label; executed step without `run:`; editable metadata; `TMPDIR` inside the checkout | fixed in `3601f54` (result v1.10); replies r4319455386, r4319455698, r4319456456, r4319456940; threads resolved |
| CX6-25 | Codex review 5578496092 (on `14a5858`), comment r4319487957, P2 | `14a5858` | `tools/ci/prepush_check.py` 1069: "an added job whose command exits nonzero is ignored while the replay can report PASS even though hosted CI fails"; "Require the parsed job set to be exactly `{test}` or replay every job" | Confirmed: at `14a5858`, the real `ci.yml` with a second job `other` was accepted. Fixed in `7fc63d6` (§3) |
| CX6-26 | same review, comment r4319487964, P2 | `14a5858` | `tools/ci/prepush_check.py` 1098: "a mapping-valued or sequence-valued environment entry, such as `BASE_SHA: {nested: invalid}`", is stringified, although GitHub Actions rejects it; "require every environment key and value to have the scalar shape supported by the workflow schema" | Confirmed, in two forms: at `14a5858`, a block-nested `BASE_SHA` was accepted as a mapping, and the finding's own flow form `{nested: invalid}` was accepted as the literal string `'{nested: invalid}'`, because the YAML subset parser does not model flow collections. Fixed in `7fc63d6` for both (§3, IF-35-13) |
| CX6-27 | same review, comment r4319487973, P2 | `14a5858` | `tools/ci/prepush_check.py` 1521: with `project = []`, formatting the error "indexes the list as `project['name']`", and the `TypeError` "escapes both `_substitute` and `main`, producing a traceback and skipping the post-run repository-state comparison"; "validate the table shape before reading its name" | Confirmed: at `14a5858`, `_substitute` on the real install step with `project = []` raised `TypeError: list indices must be integers or slices, not str`. Fixed in `7fc63d6` (§3, IF-35-13) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-25, CX6-26 and CX6-27 (`7fc63d6`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `d05aafb9e6fa`; 1,838 lines; +23/−8 on `14a5858`) | **CX6-25.** The workflow's job set must be exactly `{test}`, or it is `REPLAY_INVENTORY_DRIFT`. **CX6-26.** Each step's `name`, `id`, `if`, `uses`, `shell` and `run` must be a string, and its `env` and `with` mappings of strings, or it is `REPLAY_INVENTORY_DRIFT`. `parse_jobs` refuses a job `env` value that is not a string ("unsupported shape"). `_plain` now refuses an unquoted value that begins with a flow-collection, anchor, alias, tag, block-scalar or other YAML indicator (`{ [ & * ! \| > % @` and a backtick, or `?`): the parser would read it as a literal string where GitHub's parser reads YAML. **CX6-27.** `_install_check` reads `[project]` with `.get`, refuses a value that is not a table ("has no [project] table"), and its two messages read the name with `.get`. `_substitute` also reports a `TypeError` as a tooling failure. `main` now catches every exception a report raises (`except Exception`), so the post-run read-only comparison is always reached, as its comment already stated |
| `tests/tools/test_prepush_check.py` (blob `a275e80a171f`; 921 lines; +45/−1) | Three drift cases: `second-job`, `structured-env-value` (block-nested `BASE_SHA`) and `step-if-not-a-string` (a block-nested `if`). `test_a_step_that_is_not_a_mapping_is_refused` also refuses a block-nested job `env` value. New `test_yaml_forms_the_parser_does_not_model_are_refused`, with seven parameters: `{nested: invalid}`, `[a, b]`, `&anchor x`, `*alias`, `!tag x`, `\|+`, `>2`. New `test_an_unexpected_report_exception_still_reaches_the_read_only_check`: a report replaced by one raising `TypeError` gives exit 1, `TOOLING_FAILURE TypeError: boom` and `repository unchanged`. The site case refuses a `project = []` with "no [project] table", and `_substitute` reports it as tooling. 60 cases (49 + 11) |

## 4. CI on `14a5858`

Run 39334149978 (job 118339303216) on `14a5858` ran from 22:19:45Z to 22:39:16Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 22:24:30Z with CX6-25 to CX6-27. It was not waited on and is not a gate. Its result covers `14a5858` only, whose code `7fc63d6` changes.

## 5. Local validation of `7fc63d6`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install and pip 24.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `7fc63d6` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. `PYTHONPATH` is the clone under test. Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 60 passed in 39.3 s (concurrent with items 5, 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..7fc63d6`, `pull_request` | exit 0; `reason=selected_lanes;paths=14;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `7fc63d6`, committed there | All 40 fail as intended, each clone clean afterwards. NC-11 to NC-44 fail exactly the cases they failed at `3601f54` (result v1.10 §5 item 5), with NC-38 and NC-39 retargeted to the rewritten lines. The one difference is NC-38 (the `env`/`with` shape check disabled), which now also fails `structured-env-value`. NC-45 (the job-set check removed): `second-job` fails. NC-46 (the string check on step keys removed): `step-if-not-a-string` fails. NC-47 (the parser's indicator refusal removed): all seven YAML-form cases fail. NC-48 (the `[project]` table check removed): the site case fails. NC-49 (`main` back to the five exception types): the unexpected-exception case fails. NC-50 (the job `env` value check removed): `test_a_step_that_is_not_a_mapping_is_refused` fails |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` | result v1.10 §5 item 6's cases, including (E) to (M): output byte-identical to that round's. The real `ci.yml` parses with all 16 steps under the stricter parser, and the sweep's coverage still computes from it |
| 7 | Premises at `14a5858` (that head's tool, scratch only) | CX6-25: a second job accepted. CX6-26: a block-nested `BASE_SHA` accepted as `{'nested': 'invalid'}`, and `{nested: invalid}` accepted as the string `'{nested: invalid}'`. CX6-27: `_substitute` with `project = []` raised `TypeError` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 22:32:06Z to 23:04:03Z (concurrent with item 9); classify `reason=selected_lanes;paths=14`, all seven lanes; every one of the 16 steps SUCCESS; changed tests 166 targets, 3,946 passed (result v1.10's 3,935 plus the eleven new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,911.0 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=7fc63d6…`, `status_lines=0`, `git_metadata_digest=07558194a5011d525155de5d804f3e850e913a3740327381609b7ce065074c01`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,246 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,584.9 s (22:32:06Z to 22:58:38Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.10's 5,235 plus the eleven new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-12 | as results v1.1 to v1.10 §6 | unchanged | as recorded there |
| IF-35-13 | Three fixes beyond the findings' literal text. First, the value-shape rule covers every step key, not only `env` values: `name`, `id`, `if`, `uses`, `shell`, `run`, and `with` values. Second, the YAML subset parser fails closed on YAML forms it does not model, instead of reading them as strings. Third, `main` catches every exception a report raises, not only `TypeError` | Each is CX6-26's or CX6-27's root cause in a sibling place. CX6-26's own example, `{nested: invalid}`, would have stayed a string had only mapping values been checked. CX6-27's escape skipped the read-only comparison, which every report must reach, and `main`'s comment already promised that "whatever a report raised". PO-35-2; plan §5.2 (read-only by construction) | §5 items 1, 5 (NC-38, NC-39, NC-45 to NC-50), 6, 7 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.10 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 22:19:37 | push 10 of PR-35: `2c6dd5c..14a5858` (`3601f54`, the v1.10 record), fast-forward, no force | remote head `14a5858…`; v1.10 read back from the remote: blob `7ba2d03ad6a5`, 19,533 bytes, sha256 equal to the local file |
| 22:19:49 to 22:20:01 | replies r4319455386 (CX6-21), r4319455698 (CX6-22), r4319456456 (CX6-23) and r4319456940 (CX6-24); the four threads resolved | GitHub |
| 22:20:17 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` re-armed for 23:10Z after push 10 | it creates no session |
| 22:19:56 to 22:24:30 | Codex code review on `14a5858` (trigger "New commits"): review 5578496092, findings CX6-25 to CX6-27 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 22:19:45 to 22:39:16 | CI run 39334149978 on `14a5858`: success, stale | §4 |
| 22:28:28 to 22:30:04 | local commit `679019b`, amended before any push to `4f75d00` (the `step-if-not-a-string` case, added because no test covered the new string rule for step keys) and then to `7fc63d6` (the commit message naming that case) | §3 |
| 22:31:41 | the check-in moved from 23:10Z to 23:55Z, after the round-12 push | it creates no session |
| 22:32:06 to 23:09:40 | local validation of `7fc63d6`, all passed | §5 |
| after this record | push 11 of PR-35: `7fc63d6` and the commit adding this record, fast-forward onto `14a5858`, no force | read back in the next record |
| next | answer the CX6-25 to CX6-27 threads naming `7fc63d6` and resolve them; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment | stated limit; the modelled build system and configuration plus the fail-closed proxy (IF-35-7, IF-35-12) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (as result v1.10 §8); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

Read on `main` at `0442d23` (`docs/pfcanon/` unchanged since `5e62a65`; this branch changes no canon).

| Topic | Sources and sections |
| :- | :- |
| Phase authority, review chain, stale CI, merge boundary | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (all sections); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 |
| Review chain overlay | PF10-HDE-Build-Notes v13.6.1 addendum 2.3 (Rules 1 to 5) |
| Sweep tools | PF10-HDE-Build-Notes v13.6.1 addendum 2.2 ("WU-PR-06's sweep environment must provide ruby") |
| Tooling vs behavior | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 |
| Closed rails | Glow QA Guide §2.2.6 "Rails posture in CI (default CLOSED)" (read in full on `main`) |
| In-flight scope | instruction v1.0 ID-2, ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.2, §5.7, §5.8, PD-8, §6.1, §13 RK-3 and RK-5, §17; contract G-3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
