---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.19"
record_kind: PR-35 checkpoint for the nineteenth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.18.md (v1.18, PR-35 checkpoint; blob b8ae075c826f; 23,381 bytes; sha256 42f51df57c7b935fada13e288faa7804206d9a756e30a32e383ec2e885599084); v1.17 (blob 78cc146ad6e9), v1.16 (blob 0d7b2026f6b4), v1.15 (blob 08cf62c76359), v1.14 (blob 456818eb3364), v1.13 (blob 6bce49444702), v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b, 161941f, d1a8969, 0783969, 0575fb0, ef06f44, 7be75ef, ba65334, bb52426, a7f1fdc, e4cda7d and a062ff7, pushed; d01599c5cf84a245401d54b72f344de8fa622075 (CX6-40 and CX6-41; parent a062ff7); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T05:05Z
next_step: push d01599c and this record; answer the CX6-40 and CX6-41 threads naming d01599c and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---


# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.19 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `a062ff7` raised two P2 findings:

- CX6-40: a step id that repeats another is accepted, and the replay overwrites the first step's outcome and outputs.
- CX6-41: a tab in a line's indentation is normalised away, though YAML forbids it.

Under PO-35-2 both are fixed in `d01599c` (IF-35-20) and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-37 | Codex reviews 5571963225 to 5580246369 | `d2ed4fc` to `ba65334` | as results v1.1 to v1.17 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-38, CX6-39 | Codex review 5580468215 | `a7f1fdc` | as result v1.18 | fixed in `e4cda7d` (result v1.18); threads answered and resolved |
| CX6-40 | Codex review 5580742466 (on `a062ff7`), comment r4321446382, P2 | `a062ff7` | `tools/ci/prepush_check.py` 1266: "When a candidate adds `id: classify` to the checkout step while retaining the classifier step's existing ID, this validation accepts both and the replay simply overwrites `steps_context["classify"]` as execution proceeds"; "GitHub requires a step ID to be unique and rejects duplicate identifiers during template validation"; "validate uniqueness across all nonempty step IDs" | Confirmed at `a062ff7`: `id: classify` and `id: Classify` added to the checkout step were each accepted, beside the classifier's `classify`. The ids `1pins`, `env.pins`, `__env_pins` and `''` were accepted too. Fixed in `d01599c` (§3) |
| CX6-41 | same review, comment r4321446375, P2 | `a062ff7` | `tools/ci/prepush_check.py` 460: "When a candidate prefixes a top-level key such as `name:` or `on:` with a tab, `_indent` counts zero indentation and the later `strip()` removes the tab, so the current workflow still passes `replay_steps`"; "YAML explicitly forbids tabs in indentation"; "reject a tab occurring in a line's indentation rather than normalizing it away" | Confirmed at `a062ff7`: a tab before `name:` was accepted and all 16 steps read. A line of a tab alone inside a block scalar was read as an empty line. Other tab placements were already refused, though for other reasons (header drift, structure). Fixed in `d01599c` (§3, IF-35-20) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-40 and CX6-41 (`d01599c`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `35812f6095a8`; 2,114 lines; +25/−0 on `a062ff7`) | **CX6-40.** New `_STEP_ID_RE`. `replay_steps` collects every step's id. A repeated id is `REPLAY_INVENTORY_DRIFT` ("GitHub requires step ids to be unique"), and so are two ids that differ only in case. An id outside the form GitHub documents for job ids (a letter or `_`, then letters, digits, `-` or `_`), or one beginning with `__`, is drift too ("a form the replay does not model"). **CX6-41.** New `_spaces_only`, called on every line `_mapping` and `_sequence` read, blank and comment lines included. A tab in a line's leading whitespace fails closed, naming the line ("which YAML forbids"). In `_block`, a whitespace line containing a tab fails closed too: in YAML it ends the block rather than reading as an empty line. A tab after a block's indentation stays content, and a tab after a key's colon still separates its value, as in YAML |
| `tests/tools/test_prepush_check.py` (blob `e0899e416c14`; 1,208 lines; +26/−1) | The drift test gains four cases: `repeated-id` (`id: classify` on the checkout), `repeated-id-case` (`id: Classify`), `id-form` (`env.pins`) and `id-reserved` (`__env_pins`). New `test_tabs_in_indentation_are_refused_and_elsewhere_read_as_yaml_reads_them`. It refuses a tab before the top-level `name:`, before a nested key, before a sequence entry, before a block-scalar line, and on a blank line. It refuses a whitespace line with a tab inside a block. It reads a tab after the block indentation as content, and a tab after a colon as a separator. 131 cases (126 + 5) |

## 4. CI on `a062ff7`

Run 39369054806 (job 118452513678) on `a062ff7` ran from 04:20:31Z to 04:37:50Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 04:24:10Z with CX6-40 and CX6-41. It was not waited on and is not a gate; its result covers `a062ff7` only, whose code `d01599c` changes. The changed-tests failure of result v1.13 §4 did not recur.

## 5. Local validation of `d01599c`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `d01599c` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: items 1 and 2, the negative controls and item 9;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: the session checkout's owner-test runs before the commit (131 passed);
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 131 passed in 38.2 s, pytest exit 0 |
| 2 | Pin and neighbouring files (`cand2`), one at a time | `test_rails_ci_workflow_integration.py` 138, `test_http_reader_ci_ownership.py` 4, `test_architecture_snapshot.py` 5, `test_epic020_bundle_tool.py` 6 passed; each pytest exit 0 |
| 3 | Classifier `0442d23..d01599c`, `pull_request` | exit 0; `reason=selected_lanes;paths=22;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test and the close-pack test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…`; `sweep --no-run` at the head and at `a429c7c` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0; `lanes` exit 0, eleven output records, PASS, repository unchanged; `sweep --no-run` at the head `uncovered=0`, exit 0, and at `a429c7c` `uncovered=135`, exit 1, as in result v1.15 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `d01599c`, committed there (04:29:47Z to 05:01:55Z, two at a time) | All 75 fail as intended, each clone clean afterwards. NC-11 to NC-79 fail exactly the cases they failed at `e4cda7d` (result v1.18 §5 item 5). The six new controls: NC-80 (the indentation check removed) and NC-81 (the block's whitespace-with-tab check removed) each fail the tab test. NC-82 (the id form check removed) fails `id-form` and `id-reserved`. NC-83 (the `__` prefix accepted) fails `id-reserved`. NC-84 (the uniqueness check removed) fails `repeated-id` and `repeated-id-case`. NC-85 (ids compared with their case) fails `repeated-id-case` |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` (integ2 with the real-setuptools site, integ3, integ4) | output byte-identical to result v1.18's, all three, each exit 0. The real workflow has no tab, and its fourteen step ids are unique and of the modelled form. `cand2` clean |
| 7 | Premises at `a062ff7` (that head's tool, scratch only), and the fix (the tool at `d01599c`) | At `a062ff7`: each case of §2 as listed there; the real workflow 16 steps. Under the fix: both repeated ids are refused, naming the step that repeats `classify`. The four malformed ids are refused, while `env-pins` still reads. Each tab in indentation is refused, naming its line, and so is the tab-only line in a block. The tab after a block's indentation still reads as content, and the tab after a colon as a separator. The real workflow still 16 steps. Rounds 15, 17, 18 and 19's premise cases at `d01599c` give their earlier outputs. One case of round 16's (seven spaces and a tab before `run:`) was refused before as an unsupported structure and is now refused by the new check, as "a tab in the indentation of line 78" |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 04:29:47Z to 04:57:37Z (concurrent with items 5 and 9); classify `reason=selected_lanes;paths=22`, all seven lanes; every one of the 16 steps SUCCESS. Changed tests 4,017 passed (result v1.18's 4,012 plus the five new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,665.3 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=d01599c…`, `status_lines=0`, `git_metadata_digest=f6deb412eaa600503932d558519314b445c18b54395cb636ce5cde6bb74a6ddd`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,317 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,388.8 s (04:29:47Z to 04:53:08Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.18's 5,312 plus the five new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones. The `PytestWarning` about `/tmp/pytest-of-root` noted in result v1.18 did not recur |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-19 | as results v1.1 to v1.18 §6 | unchanged | as recorded there |
| IF-35-20 | Two choices. First, CX6-40 refuses more than repeated ids. GitHub's workflow-syntax page says only that a step id is "a unique identifier", so the replay accepts ids only in the form the page documents for job ids. It refuses ids beginning with `__` and ids that differ only in case, forms whose treatment by GitHub it does not model. Second, CX6-41 refuses every tab in leading whitespace, blank and comment lines included, rather than modelling where YAML allows one there. A tab after indentation is read as YAML reads it, as content in a block and as a separator after a colon. Consequence: a PR whose workflow uses such a form gets a TOOLING failure from the replay until the model covers it; hosted CI is unaffected | A repeated id lets the replay run a different steps context than CI, and an indentation tab lets it run a workflow GitHub never runs ("To maintain portability, tab characters must not be used in indentation", YAML 1.2.2 §6.1). The real workflow has no tab, and its fourteen step ids are unique, lowercase and of the documented form (§5 items 6 and 8), so the closed model costs nothing there. PO-35-2; plan §5.7 (the parser, "a strict subset fails closed on any construct it does not understand"; the inventory); contract G-3; PD-8 | §5 items 1, 5 (NC-80 to NC-85), 6, 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.18 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 04:20:23 | push 18 of PR-35: `a7f1fdc..a062ff7` (`e4cda7d`, the v1.18 record), fast-forward, no force | remote head `a062ff7…`; v1.18 read back from the remote: blob `b8ae075c826f`, 23,381 bytes, sha256 equal to the local file |
| 04:20:42, 04:20:47 | replies r4321430329 (CX6-38) and r4321430656 (CX6-39) naming `e4cda7d`; both threads resolved | GitHub, read back at about 05:05: both `is_resolved: true` |
| 04:20:54 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved to 05:10Z | it creates no session |
| 04:20:31 to 04:37:50 | CI run 39369054806 on `a062ff7`: success, stale | §4 |
| 04:20:54 to 04:24:10 | Codex code review on `a062ff7` (trigger "New commits"): review 5580742466, findings CX6-40 and CX6-41 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 04:29:40 | local commit `d01599c` | §3 |
| 04:29:47 to 05:01:55 | local validation of `d01599c`, all passed | §5 |
| after this record | push 19 of PR-35: `d01599c` and the commit adding this record, fast-forward onto `a062ff7`, no force | read back in the next record |
| next | answer the CX6-40 and CX6-41 threads naming `d01599c` and resolve them; move the safety-net check-in; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (result v1.13 §4; PR comment 6280395750) | PR-35 watches each new head's CI; the close-pack tool and test are outside this PR's change set | did not recur on `161941f`, `0783969`, `ef06f44`, `ba65334`, `a7f1fdc` or `a062ff7` (results v1.14 to v1.19 §4); intermittent, mechanism not established |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
| `GITHUB_OUTPUT` forms other than `NAME=VALUE`; YAML escape sequences, folding around more-indented lines, typed scalars other than `true`, `false` and decimal integers in `env` and `with`, tabs in leading whitespace, and the other unmodelled scalar, block and key forms; an install step other than one simple command; an excluded step with another condition; a workflow header other than `ci.yml`'s; comparisons needing GitHub's number conversion or non-ASCII case folding, and objects used as values; step ids outside the documented job-id form, beginning with `__`, or differing only in case | stated limits; TOOLING (IF-35-15 to IF-35-20) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (as result v1.10 §8); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

Read on `main` at `0442d23` (`docs/pfcanon/` unchanged since `5e62a65`; this branch changes no canon). For this round, `docs/pfcanon/` on `main` and plan v1.0 were searched again for the findings' terms (step id, unique identifier, tab, indentation). Neither holds anything on workflow step ids or YAML tabs; the governing text is plan v1.0 §5.7. External reference, not canon: GitHub's workflow-syntax page ("A unique identifier for the step"; the job-id form "must start with a letter or `_` and contain only alphanumeric characters, `-`, or `_`") and YAML 1.2.2 §6.1 (quoted in §6).

| Topic | Sources and sections |
| :- | :- |
| Phase authority, review chain, stale CI, merge boundary | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (all sections); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 |
| Review chain overlay | PF10-HDE-Build-Notes v13.6.1 addendum 2.3 (Rules 1 to 5) |
| Sweep tools | PF10-HDE-Build-Notes v13.6.1 addendum 2.2 ("WU-PR-06's sweep environment must provide ruby") |
| Tooling vs behavior | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 |
| Closed rails | Glow QA Guide §2.2.6 "Rails posture in CI (default CLOSED)" (read in full on `main`) |
| Generated metadata stays out of the tree (IF-35-14, carried) | HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §27.4 "Tracked evidence boundary and rollback" |
| In-flight scope | instruction v1.0 ID-2, ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.2, §5.7 (the parser, the inventory, "Conditions and expressions"), §5.8, PD-8, §6.1, §9, §13 RK-1, RK-3 and RK-5, §17; contract G-3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" and its corollary on exit statuses |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
