---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.15"
record_kind: PR-35 checkpoint for the fifteenth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.14.md (v1.14, PR-35 checkpoint; blob 456818eb3364; 21,007 bytes; sha256 9ef3df4ceba7271508c27c32b5cc0f1a8592afb9e9db8fff70b65be4b203fd6d); v1.13 (blob 6bce49444702), v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b, 161941f, d1a8969 and 0783969, pushed; 0575fb0937b83c6930260d76e9deb2f83941d4de (CX6-32 to CX6-34; parent 0783969); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T02:17Z
next_step: push 0575fb0 and this record; answer the CX6-32 to CX6-34 threads naming 0575fb0 and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.15 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `0783969` raised three P2 findings:

- CX6-32: a repeated top-level workflow key is accepted, and only the first `jobs:` block is read.
- CX6-33: a folded block scalar joins a more-indented line to its neighbours, where YAML keeps their line breaks.
- CX6-34: a malformed extras list such as `pip[,]` is accepted.

Under PO-35-2 all three are fixed in `0575fb0`, with a sibling block-scalar gap (IF-35-17), and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-29 | Codex reviews 5571963225 to 5579226115 | `d2ed4fc` to `7a3b7b2` | as results v1.1 to v1.13 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-30 and CX6-31 | Codex review 5579511731; P2 | `161941f` | extra command in the install step; double-quoted escapes | fixed in `d1a8969` (result v1.14); replies r4320584920 and r4320585324; threads resolved |
| CX6-32 | Codex review 5579783963 (on `0783969`), comment r4320606696, P2 | `0783969` | `tools/ci/prepush_check.py` 1127: "When a candidate repeats a top-level key—for example, by appending a second `name:` or `jobs:` mapping—collecting keys in a set hides the duplicate, and `parse_jobs` reads only the first `jobs:` block"; "parse the complete top-level mapping and reject duplicates just as the nested parser already does" | Confirmed at `0783969`: a second `name:` was accepted, and with a second `jobs:` block appended the replay read the first one. Fixed in `0575fb0` (§3) |
| CX6-33 | same review, comment r4320606682, P2 | `0783969` | `tools/ci/prepush_check.py` 500: for a folded block "followed by `echo replay_pass` and a more-indented `exit 1`, this joins both lines with spaces and replay executes one successful `echo` command", while "YAML preserves line breaks around more-indented content"; "implement the folded-block rules or reject this form" | Confirmed at `0783969`: the block read as `echo replay_pass   exit 1`. A sibling was confirmed in the same function: a literal-block line less indented than the block's first line lost characters, `echo b` becoming `ho b`. Fixed in `0575fb0` by refusing both forms (§3, IF-35-17) |
| CX6-34 | same review, comment r4320606690, P2 | `0783969` | `tools/ci/prepush_check.py` 1309: "When `requirements-dev.txt` contains a malformed requirement such as `pip[,]` or `pip[foo,]`, filtering empty elements makes it indistinguishable from a valid installed requirement"; "validate the original extras-list grammar before discarding empty components" | Confirmed at `0783969`: `pip[,]`, `pip[foo,]`, `pip[,foo]` and `pip[foo,,bar]` were accepted, and so was `pip[-x]`, whose extra is not a PEP 508 identifier. Fixed in `0575fb0` (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-32 to CX6-34 (`0575fb0`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `05506b1e2fe4`; 1,988 lines; +22/−11 on `0783969`) | **CX6-32.** New `parse_workflow` reads the whole workflow document as one mapping with the same parser, so the repeated-key refusal of result v1.14 now covers the top level too. `replay_steps` takes the top-level keys from it, in place of the line-start regular expression and its set. `parse_jobs` takes `jobs` from it, in place of the first `jobs:` line, so the sweep's coverage reads the same jobs as the replay. **CX6-33.** `_block` refuses a folded-block line that starts with a space or a tab after the block's indentation: YAML keeps the line breaks around it, which is not modelled. **Sibling.** `_block` refuses, in any block scalar, a line less indented than the block's first line. **CX6-34.** `_parse_requirement` splits a nonempty extras list at commas and requires each element to be a PEP 508 identifier; `[]` and `[ ]` stay valid |
| `tests/tools/test_prepush_check.py` (blob `8f8029e72496`; 1,087 lines; +33/−1) | New `test_the_whole_workflow_is_one_mapping_without_repeated_keys`: a second top-level `name:`, and a second `jobs:` block, are each refused by the replay, and the second `jobs:` block by the sweep's coverage reader (`pytest_command_tokens`). New `test_block_scalars_are_read_as_yaml_reads_them_or_refused`, through `replay_steps`: a folded block with an empty line reads as `echo a echo b\necho c`; a literal block keeps a more-indented line; a folded more-indented line and a literal less-indented line are refused. The PEP 440/508 test gains `alpha[ ]` (no extras) and refuses `x[,]`, `x[a,]`, `x[,a]`, `x[a,,b]` and `x[-a]`. 91 cases (89 + 2) |

## 4. CI on `0783969`

Run 39353894415 (job 118404163140) on `0783969` ran from 01:31:25Z to 01:52:29Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 01:35:31Z with CX6-32 to CX6-34. It was not waited on and is not a gate; its result covers `0783969` only, whose code `0575fb0` changes. The changed-tests failure of result v1.13 §4 did not recur here either.

## 5. Local validation of `0575fb0`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `0575fb0` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: item 1, the negative controls and item 9;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: item 2, in the session checkout at `0575fb0`;
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 91 passed in 42.5 s, exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..0575fb0`, `pull_request` | exit 0; `reason=selected_lanes;paths=18;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…`; `sweep --no-run` at the head and at `a429c7c` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0; `lanes` exit 0, eleven output records, PASS, repository unchanged. Both `sweep --no-run` runs read `ci.yml` through the whole-document parse. At the head: `uncovered=0`, exit 0. At `a429c7c`: `uncovered=135`, exit 1, as the report fails by design when files are uncovered; this is the count result v1.0 recorded against WU-PR-01 instruction §5.1 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `0575fb0`, committed there (01:42:10Z to 02:14:20Z, two at a time) | All 58 fail as intended, each clone clean afterwards. NC-11 to NC-60 and NC-62 to NC-64 fail exactly the cases they failed at `d1a8969` (result v1.14 §5 item 5). NC-12 (an unsupported requirement read as a bare name) and NC-19 (extras not stripped) are retargeted to the rewritten lines and still fail those cases. NC-61 (repeated keys accepted) now also fails the whole-document test, since the top level goes through the same check. The four new controls: NC-65 (`parse_jobs` reading only the first `jobs:` block) fails the whole-document test at its sweep-coverage assertion. NC-66 (more-indented folded lines accepted) and NC-67 (less-indented block lines accepted) each fail the block-scalar test. NC-68 (the extras identifier check removed) fails the PEP 440/508 test |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` (integ2 with the real-setuptools site, integ3, integ4) | output byte-identical to result v1.14's, all three: the real workflow parses as one document with all 16 steps; `cand2` clean |
| 7 | Premises at `0783969` (that head's tool, scratch only), and the fix (the tool at `0575fb0`) | At `0783969`: the real workflow 16 steps; a second top-level `name:` accepted; with a second `jobs:` block the replay read the first; the folded more-indented block read as `echo replay_pass   exit 1`; the less-indented literal line read as `ho b`; `pip[,]`, `pip[foo,]`, `pip[,foo]`, `pip[foo,,bar]` and `pip[-x]` accepted. Under the fix: 16 steps; each of those refused, naming the repeated key and its line, the more- or less-indented line, or the requirement; `pip[ foo , bar ]` and `pip[]` still read. A tab in the indentation was already refused at `0783969` and still is. Round 15's premise cases (result v1.14 §5 item 7) give the same output at `0575fb0` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 01:41:40Z to 02:15:00Z (concurrent with items 5 and 9); the workflow read as one document; classify `reason=selected_lanes;paths=18`, all seven lanes; every one of the 16 steps SUCCESS. Changed tests 166 targets, 3,977 passed (result v1.14's 3,975 plus the two new cases), the close-pack test among them; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,994.2 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=0575fb0…`, `status_lines=0`, `git_metadata_digest=92ff4c8a4c42e5a66b17e0c9d232cc997fcb3378baacb4ef6b2938272da87138`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,277 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,625.6 s (01:41:40Z to 02:09:01Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.14's 5,275 plus the two new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-16 | as results v1.1 to v1.14 §6 | unchanged | as recorded there |
| IF-35-17 | Three choices. First, CX6-32 is fixed by parsing the whole document with the same parser, not by a separate duplicate check on top-level lines, and the sweep's coverage reader uses that parse too. Second, CX6-33 is fixed by refusing a more-indented folded line rather than implementing YAML's folding rules. Third, a sibling in the same function, a block line less indented than the block's first line, is refused: it lost characters silently. Consequence: a PR that writes these forms gets a TOOLING failure from the replay until the parser models them; hosted CI is unaffected | One parse gives one answer for the replay and the sweep, and covers every level. The real workflow parses as one document (§5 items 4, 6). Its one folded block (the install step) has no more-indented line, so refusing the form costs nothing, while the folding rules would be code no step needs. The less-indented line is invalid YAML, which GitHub rejects. PO-35-2; plan §5.7 (the YAML subset, PD-8) | §5 items 1, 4, 5 (NC-12 and NC-19 retargeted, NC-65 to NC-68), 6, 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.14 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 01:31:14 | push 14 of PR-35: `161941f..0783969` (`d1a8969`, the v1.14 record), fast-forward, no force | remote head `0783969…`; v1.14 read back from the remote: blob `456818eb3364`, 21,007 bytes, sha256 equal to the local file |
| 01:31:29 and 01:31:33 | replies r4320584920 (CX6-30) and r4320585324 (CX6-31); both threads resolved | GitHub |
| 01:31:44 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved to 02:25Z | it creates no session |
| 01:31:29 to 01:35:31 | Codex code review on `0783969` (trigger "New commits"): review 5579783963, findings CX6-32 to CX6-34 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 01:31:25 to 01:52:29 | CI run 39353894415 on `0783969`: success, stale | §4 |
| 01:39:05 to 01:41:29 | local commit `9dfd8b3`, amended before any push to `0575fb0`. Planning NC-65 showed that no test made the sweep's coverage reader refuse a second `jobs:` block: `replay_steps` refuses one on its own. So that assertion was added. The replay and sweep already started on `9dfd8b3` were stopped and their temporary directory removed; neither result is used | §3 |
| 01:41:40 to 02:15:00 | local validation of `0575fb0`, all passed | §5 |
| after this record | push 15 of PR-35: `0575fb0` and the commit adding this record, fast-forward onto `0783969`, no force | read back in the next record |
| next | answer the CX6-32 to CX6-34 threads naming `0575fb0` and resolve them; move the safety-net check-in if needed; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (result v1.13 §4; PR comment 6280395750) | PR-35 watches each new head's CI; the close-pack tool and test are outside this PR's change set | did not recur on `161941f` or `0783969` (result v1.14 §4, §4 here); intermittent, mechanism not established |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
| `GITHUB_OUTPUT` forms other than `NAME=VALUE`; YAML escape sequences, folding around more-indented lines and the other unmodelled scalar, block and key forms; an install step other than one simple command | stated limits; TOOLING (IF-35-15 to IF-35-17) | recorded |
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
| Generated metadata stays out of the tree (IF-35-14, carried) | HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §27.4 "Tracked evidence boundary and rollback" |
| In-flight scope | instruction v1.0 ID-2, ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.2, §5.7, §5.8, PD-8, §6.1, §9, §13 RK-3 and RK-5, §17; contract G-3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
