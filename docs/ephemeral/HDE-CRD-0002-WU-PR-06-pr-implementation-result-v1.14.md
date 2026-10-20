---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.14"
record_kind: PR-35 checkpoint for the fourteenth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.13.md (v1.13, PR-35 checkpoint; blob 6bce49444702; 20,789 bytes; sha256 f5d814d1ad8006483431411e0b979537f7911bcd40de440273563e13a0cafdfd); v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b and 161941f, pushed; d1a89698953deddae9d2ea8964d52dd2f959ebca (CX6-30 and CX6-31; parent 161941f); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T01:32Z
next_step: push d1a8969 and this record; answer the CX6-30 and CX6-31 threads naming d1a8969 and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.14 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `161941f` raised two P2 findings:

- CX6-30: the install substitute accepts a step with an extra command on its own line.
- CX6-31: the workflow parser keeps the escape sequences of a double-quoted scalar.

Under PO-35-2 both are fixed in `d1a8969`, with sibling gaps in the same parser (IF-35-16), and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-28 | Codex reviews 5571963225 to 5578877595 | `d2ed4fc` to `efff0bb` | as results v1.1 to v1.12 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-29 | Codex review 5579226115; P2 | `7a3b7b2` | malformed `GITHUB_OUTPUT` records | fixed in `55a973b` (result v1.13); reply r4320350931; thread resolved |
| CX6-30 | Codex review 5579511731 (on `161941f`), comment r4320373714, P2 | `161941f` | `tools/ci/prepush_check.py` 1601: when the install step "appends another newline-separated command whose words are also installed distribution names", for example `python -m pip install pytest` followed by `pytest`, "`shlex.split` flattens both lines" and the substitute "substitutes the entire step without executing it"; "validate that the step contains exactly one pip invocation" | Confirmed at `161941f` with the real environment: `python -m pip install pytest` and `pytest` on the next line returned no unmet item. The other shell forms tried there (`;`, `&&`, `\|`, `$( )`, a backtick, `"$HOME"`, `>`, `#`) were refused only because the requirement parser did not recognize them. Fixed in `d1a8969` (§3) |
| CX6-31 | same review, comment r4320373705, P2 | `161941f` | `tools/ci/prepush_check.py` 447: for `run: "echo replay_pass\nexit 1"`, "`_plain` removes the quotes but leaves the escape sequence intact, so replay executes one successful `echo` command while hosted Actions parses `\n` as a line feed and executes the failing `exit 1`"; "either decode them or reject this scalar form" | Confirmed at `161941f`: the value read as `echo replay_pass\nexit 1` with the backslash kept. Fixed in `d1a8969` by refusing escapes, with the sibling scalar and key gaps confirmed alongside it (§3, IF-35-16) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-30 and CX6-31 (`d1a8969`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `2990ee3a611a`; 1,977 lines; +62/−12 on `161941f`) | **CX6-30.** New `_simple_command`, used by `_install_check` in place of `shlex.split`. The install step's text must be one bash simple command: no line break anywhere; outside quotes none of `; & \| < > ( )`, a backtick, `$ * ? [ ] { } ~ ! #` or a backslash; inside double quotes no `$`, backtick or backslash; no unterminated quote. Anything else is refused, before any requirement is read. **CX6-31.** `_plain` reads a single-quoted scalar only when it closes on its line, optionally followed by a comment, and decodes `''`. It reads a double-quoted scalar only when it closes on its line and holds no backslash: escape sequences are not modelled. A quoted scalar followed by a comment is now read without its quotes. A plain scalar is cut at a comment after any whitespace, not only a space. It is refused when it starts with `#` or is a sequence entry (`- …`), or when it holds `: ` or ends with `:`. **Keys.** `_mapping` requires each key to be a plain word (`[A-Za-z0-9_.-]+`) followed by `: `, a tab or the line end, and refuses a key repeated in one mapping |
| `tests/tools/test_prepush_check.py` (blob `fcbb99c30863`; 1,055 lines; +24/−1) | `test_yaml_forms_the_parser_does_not_model_are_refused` gains six parameters: `"echo replay_pass\nexit 1"`, `"unterminated`, `'a' b`, `a: b`, `- x`, `# c`. New `test_quoted_scalars_and_keys_are_read_as_yaml_reads_them`: a double-quoted and a single-quoted scalar with a trailing comment, a plain scalar with a tab before its comment, and a repeated `run:`, `run:` without a space and a quoted key, each refused. New `test_the_install_substitute_stands_in_for_one_simple_command_only`, eleven parameters: a second line, `;`, `&&`, `\|`, `$( )`, a backtick, `"$HOME"`, `>`, `#`, a backslash-newline continuation, an unterminated quote. 89 cases (71 + 18) |

## 4. CI on `161941f`

Run 39349630263 (job 118390495252) on `161941f` ran from 00:46:34Z to 01:08:14Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 00:51:02Z with CX6-30 and CX6-31. It was not waited on and is not a gate; its result covers `161941f` only, whose code `d1a8969` changes.

It does answer result v1.13 §4. The changed-tests failure on `7a3b7b2` did not recur. A `success` conclusion requires the changed-tests step to succeed, so `test_manifest_reader_rejects_new_report_with_old_manifest` passed in this run. The test and `tools/qa/generate_epic_close_pack.py` are byte-identical between `7a3b7b2` and `161941f`, since neither is in this PR's change set. That one failure stays recorded as intermittent, outside this PR, with its mechanism not established, as PR comment 6280395750 states.

## 5. Local validation of `d1a8969`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `d1a8969` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: item 1, the negative controls and item 9;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: item 2, in the session checkout at `d1a8969`;
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 89 passed in 42.4 s (concurrent with item 8), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..d1a8969`, `pull_request` | exit 0; `reason=selected_lanes;paths=17;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0; `lanes` exit 0, eleven output records, `PREPUSH_CHECK_RESULT: PASS lanes=PASS; repository unchanged (…)` |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `d1a8969`, committed there (00:58:08Z to 01:28:21Z, two at a time) | All 54 fail as intended, each clone clean afterwards. NC-11 to NC-46 and NC-48 to NC-58 fail exactly the cases they failed at `55a973b` (result v1.13 §5 item 5). NC-47 is retargeted to the rewritten indicator condition (now `if False`). It fails its seven earlier YAML-form cases and the three new plain ones, `a: b`, `- x` and `# c`; the quoted forms are refused before that condition. The six new controls: NC-59 (`shlex.split` in place of `_simple_command`) fails all eleven simple-command cases. NC-60 (backslashes accepted in double-quoted scalars) fails `"echo replay_pass\nexit 1"`. NC-61 (repeated keys accepted), NC-62 (the key form unchecked) and NC-64 (comments cut only after a space) each fail `test_quoted_scalars_and_keys_are_read_as_yaml_reads_them`. NC-63 (`: ` allowed in plain scalars) fails `a: b` |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` (integ2 with the real-setuptools site, integ3, integ4) | output byte-identical to result v1.13's, all three: the real workflow parses under the stricter parser, and the real install step is one simple command. A survey of the real `ci.yml`'s `jobs:` block found every key a plain word, double-quoted values only `"1"` and `"0"`, one single-quoted value `'3.12'`, and no plain value holding `: ` or starting with `#`. `cand2` clean |
| 7 | Premises at `161941f` (that head's tool, scratch only), and the fix (the tool at `d1a8969`) | At `161941f`: the install step with `pytest` on a second line returned `[]`. `BASE_SHA: "echo replay_pass\nexit 1"` read as `echo replay_pass\nexit 1`, with the backslash kept. `"x" # comment` read as `"x"`, with the quotes kept. `"unterminated`, `'a' b`, `a: b`, `- x` and `# c` were each accepted as strings. A repeated `run:` key gave the second value, and `run:python3 …` was read as a `run` key. Under the fix, every one of these is refused, with the line break, the operator or the form named. The real install step still returns `[]` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 00:57:32Z to 01:30:41Z (concurrent with items 1, 5 and 9); the real workflow read by the stricter parser, and the install step accepted as one simple command; classify `reason=selected_lanes;paths=17`, all seven lanes; every one of the 16 steps SUCCESS. Changed tests 166 targets, 3,975 passed (result v1.13's 3,957 plus the eighteen new cases), the close-pack test among them; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,984.2 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=d1a8969…`, `status_lines=0`, `git_metadata_digest=be9159ec985d6c21b2d2b93e5ecf7c6e26e1339ba5d649e5ddbddc8e0919ca62`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,275 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,638.3 s (00:57:32Z to 01:25:00Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.13's 5,257 plus the eighteen new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-15 | as results v1.1 to v1.13 §6 | unchanged | as recorded there |
| IF-35-16 | Three choices beyond the findings' literal text. First, CX6-30 is fixed by requiring one simple command, which also refuses operators, expansions, globs and comments, not only a second line. Before, those were refused only by accident, by the requirement parser. Second, CX6-31 is fixed by refusing escape sequences in double-quoted scalars rather than decoding them. Third, the sibling scalar and key gaps of the same parser fail closed too: a quoted scalar followed by a comment (now read correctly), unterminated or trailing quotes, a plain value holding `: ` or starting with `- ` or `#`, a key that is not a plain word followed by `: `, and a repeated key. Consequence: a PR that writes one of those forms gets a TOOLING failure from the replay until the parser models it; hosted CI is unaffected | The real workflow uses none of those forms (§5 item 6), so refusing them costs nothing, while decoding YAML escapes or modelling bash syntax would be code no step needs. Each sibling is the same root cause as CX6-31: the parser reading a form it does not model as a string. The repeated key matters because GitHub rejects such a workflow, while the parser took the last value. PO-35-2; plan §5.7 (the YAML subset, PD-8) | §5 items 1, 5 (NC-47 retargeted, NC-59 to NC-64), 6, 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.13 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 00:46:23 | push 13 of PR-35: `7a3b7b2..161941f` (`55a973b`, the v1.13 record), fast-forward, no force | remote head `161941f…`; v1.13 read back from the remote: blob `6bce49444702`, 20,789 bytes, sha256 equal to the local file |
| 00:46:38 | reply r4320350931 (CX6-29); the thread resolved | GitHub. Correction: the reply says the replay's "16 steps now go through the new parser". Only its 13 executed steps do; checkout, Python set-up and install are substituted. Result v1.13 §5 item 8 states it correctly |
| 00:47:02 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved to 01:40Z | it creates no session |
| 00:46:37 to 00:51:02 | Codex code review on `161941f` (trigger "New commits"): review 5579511731, findings CX6-30 and CX6-31 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 00:46:34 to 01:08:14 | CI run 39349630263 on `161941f`: success, stale; the changed-tests failure of `7a3b7b2` did not recur | §4 |
| 00:57:18 | local commit `d1a8969` | §3 |
| 00:57:32 to 01:30:41 | local validation of `d1a8969`, all passed | §5 |
| after this record | push 14 of PR-35: `d1a8969` and the commit adding this record, fast-forward onto `161941f`, no force | read back in the next record |
| next | answer the CX6-30 and CX6-31 threads naming `d1a8969` and resolve them; move the safety-net check-in if needed; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (result v1.13 §4; PR comment 6280395750) | PR-35 watches each new head's CI; the close-pack tool and test are outside this PR's change set | did not recur on `161941f` (§4); intermittent, mechanism not established |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
| `GITHUB_OUTPUT` forms other than `NAME=VALUE`; YAML escape sequences and the other unmodelled scalar and key forms; an install step other than one simple command | stated limits; TOOLING (IF-35-15, IF-35-16) | recorded |
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
