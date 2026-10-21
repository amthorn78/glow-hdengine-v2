---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.20"
record_kind: PR-35 checkpoint for the twentieth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.19.md (v1.19, PR-35 checkpoint; blob a694b81ce84a; 21,400 bytes; sha256 cbe118734a3da121f259e7cbdb5dcaeae608248d0adcfa91919e7c2ea52567c8); v1.18 (blob b8ae075c826f), v1.17 (blob 78cc146ad6e9), v1.16 (blob 0d7b2026f6b4), v1.15 (blob 08cf62c76359), v1.14 (blob 456818eb3364), v1.13 (blob 6bce49444702), v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b, 161941f, d1a8969, 0783969, 0575fb0, ef06f44, 7be75ef, ba65334, bb52426, a7f1fdc, e4cda7d, a062ff7, d01599c and 153b67b, pushed; 528074854aaf109421b480ec84b362149cfb7175 (CX6-42; parent 153b67b); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T05:50Z
next_step: push 5280748 and this record; answer the CX6-42 thread naming 5280748 and resolve it; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---



# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.20 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `153b67b` raised one P2 finding:

- CX6-42: a plain scalar beginning with `]`, `}` or `,` is read as a string, though YAML forbids those characters at the start of a plain scalar.

Under PO-35-2 it is fixed in `5280748` (IF-35-21) and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-39 | Codex reviews 5571963225 to 5580468215 | `d2ed4fc` to `a7f1fdc` | as results v1.1 to v1.18 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-40, CX6-41 | Codex review 5580742466 | `a062ff7` | as result v1.19 | fixed in `d01599c` (result v1.19); threads answered and resolved |
| CX6-42 | Codex review 5580987020 (on `153b67b`), comment r4321659209, P2 | `153b67b` | `tools/ci/prepush_check.py` 534: "Reject `]`, `}`, and `,` as initial plain-scalar characters here"; "adding `env: { HARMLESS: ] }` in block form to an executed step is accepted by `replay_steps` as the string `"]"`"; "These characters are forbidden at the start of a YAML plain scalar, so omitting them from this guard violates the replay parser's fail-closed contract" | Confirmed at `153b67b`: as an `env` value, `]`, `}`, `,x` and `] x` were each read as that string and all 16 steps read. So were `-`, `?` and `:` followed by a tab, which YAML also forbids at the start (only a non-space may follow them there). A `]` sequence entry in the header was read as text too, and refused only because the header pin saw a changed value. Fixed in `5280748` (§3, IF-35-21) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-42 (`5280748`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `b94000fc73be`; 2,116 lines; +8/−6 on `153b67b`) | `_plain`'s guard now applies YAML 1.2.2 §7.3.3's rule for a plain scalar's first character ("ns-plain-first"). A plain scalar may begin with any non-space character except an indicator. Of the indicators, only `-`, `?` and `:` may begin one, and only when a non-space character follows. The indicator set refused at the start gains `,`, `]` and `}`. `-`, `?` and `:` are refused there when nothing, a space or a tab follows, where before only a lone `-` or `?` or one followed by a space was. The refusal message says "flow indicators" for "flow collections". `-x`, `?x`, `:x` and `a,b`, `a]`, `x}` still read as plain text, as YAML reads them in block context. The rest of the guard (a mapping value inside the scalar, a trailing `:`, a comment cut) is unchanged |
| `tests/tools/test_prepush_check.py` (blob `cfc356cce360`; 1,212 lines; +5/−1) | `test_yaml_forms_the_parser_does_not_model_are_refused` gains eight values: `]`, `}`, `,x`, `] x`, `-\tx`, `?\tx`, `:\tx` and `? x`. `test_quoted_scalars_and_keys_are_read_as_yaml_reads_them` checks that `-x`, `?x`, `:x`, `a,b`, `a]` and `x}` read unchanged. 139 cases (131 + 8) |

## 4. CI on `153b67b`

Run 39372913207 (job 118464548608) on `153b67b` ran from 05:04:20Z to 05:21:04Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 05:09:29Z with CX6-42. It was not waited on and is not a gate; its result covers `153b67b` only, whose code `5280748` changes. The changed-tests failure of result v1.13 §4 did not recur.

## 5. Local validation of `5280748`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `5280748` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: items 1 and 2, the negative controls and item 9;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: the session checkout's owner-test run before the commit (139 passed);
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 139 passed in 41.2 s, pytest exit 0 |
| 2 | Pin and neighbouring files (`cand2`), one at a time | `test_rails_ci_workflow_integration.py` 138, `test_http_reader_ci_ownership.py` 4, `test_architecture_snapshot.py` 5, `test_epic020_bundle_tool.py` 6 passed; each pytest exit 0 |
| 3 | Classifier `0442d23..5280748`, `pull_request` | exit 0; `reason=selected_lanes;paths=23;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test and the close-pack test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…`; `sweep --no-run` at the head and at `a429c7c` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0; `lanes` exit 0, eleven output records, PASS, repository unchanged; `sweep --no-run` at the head `uncovered=0`, exit 0, and at `a429c7c` `uncovered=135`, exit 1, as in result v1.15 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `5280748`, committed there (05:11:59Z to 05:46:17Z, two at a time) | All 77 fail as intended, each clone clean afterwards. NC-11 to NC-85 fail exactly the cases they failed at `d01599c` (result v1.19 §5 item 5), with one explained difference. NC-47 (the whole guard removed) is retargeted to the rewritten guard line; it fails its earlier cases and the eight new values. The two new controls: NC-86 (the indicator set without `,`, `]` and `}`) fails `]`, `}`, `,x` and `] x`. NC-87 (the `-`, `?`, `:` rule as it was before) fails `-\tx`, `?\tx` and `:\tx` |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` (integ2 with the real-setuptools site, integ3, integ4) | output byte-identical to result v1.19's, all three, each exit 0. No plain scalar in the real workflow begins with an indicator. `cand2` clean |
| 7 | Premises at `153b67b` (that head's tool, scratch only), and the fix (the tool at `5280748`) | At `153b67b`: each case of §2 as listed there; the real workflow 16 steps. Under the fix: the seven forbidden starts are refused as an unsupported YAML value as `env` values, and the `]` sequence entry is refused the same way before the header is compared. `-x`, `?x`, `:x`, `a,b`, `a]` and `x}` still read unchanged. The real workflow still 16 steps. Rounds 17 to 20's premise cases at `5280748` give their earlier outputs. Round 15's three refused forms (`a: b`, `- x`, `# c`) are refused as before, with the message's "flow collections" now "flow indicators". Round 16's output differs only in the printed order of one `frozenset`, as in result v1.17 |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 05:11:59Z to 05:40:58Z (concurrent with items 5 and 9); classify `reason=selected_lanes;paths=23`, all seven lanes; every one of the 16 steps SUCCESS. Changed tests 4,025 passed (result v1.19's 4,017 plus the eight new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,732.7 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=5280748…`, `status_lines=0`, `git_metadata_digest=a8538c34b618a65e109e161b6d0002f8cf2c51018d5905ec550a9573a4443bc2`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,325 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,448.3 s (05:11:59Z to 05:36:22Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.19's 5,317 plus the eight new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-20 | as results v1.1 to v1.19 §6 | unchanged | as recorded there |
| IF-35-21 | CX6-42 is fixed by applying YAML's whole first-character rule for plain scalars, not only by adding the three characters named. The same rule also forbids `-`, `?` and `:` followed by a tab, and the earlier guard accepted those. Indicators after the first character stay plain text, as YAML reads them in block context. Consequence: a PR whose workflow writes such a form gets a TOOLING failure from the replay; hosted CI is unaffected, since GitHub rejects the same forms | A form the parser reads as text while GitHub's parser rejects it lets the replay run a workflow GitHub never runs. The real workflow begins no plain scalar with an indicator (§5 item 6), so the rule costs nothing there. PO-35-2; plan §5.7 (the parser, "a strict subset fails closed on any construct it does not understand"); PD-8 | §5 items 1, 5 (NC-47 retargeted; NC-86, NC-87), 6, 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.19 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 05:04:11 | push 19 of PR-35: `a062ff7..153b67b` (`d01599c`, the v1.19 record), fast-forward, no force | remote head `153b67b…`; v1.19 read back from the remote: blob `a694b81ce84a`, 21,400 bytes, sha256 equal to the local file |
| 05:04:20, 05:04:24 | replies r4321635238 (CX6-40) and r4321635557 (CX6-41) naming `d01599c`; both threads resolved | GitHub, read back at about 05:48: both `is_resolved: true` |
| 05:04:26 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved to 05:55Z | it creates no session |
| 05:04:20 to 05:21:04 | CI run 39372913207 on `153b67b`: success, stale | §4 |
| 05:04:40 to 05:09:29 | Codex code review on `153b67b` (trigger "New commits"): review 5580987020, finding CX6-42 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 05:11:57 | local commit `5280748` | §3 |
| 05:11:59 to 05:46:17 | local validation of `5280748`, all passed | §5 |
| after this record | push 20 of PR-35: `5280748` and the commit adding this record, fast-forward onto `153b67b`, no force | read back in the next record |
| next | answer the CX6-42 thread naming `5280748` and resolve it; move the safety-net check-in; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (result v1.13 §4; PR comment 6280395750) | PR-35 watches each new head's CI; the close-pack tool and test are outside this PR's change set | did not recur on `161941f`, `0783969`, `ef06f44`, `ba65334`, `a7f1fdc`, `a062ff7` or `153b67b` (results v1.14 to v1.20 §4); intermittent, mechanism not established |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
| `GITHUB_OUTPUT` forms other than `NAME=VALUE`; YAML escape sequences, folding around more-indented lines, typed scalars other than `true`, `false` and decimal integers in `env` and `with`, tabs in leading whitespace, plain scalars beginning with an indicator, and the other unmodelled scalar, block and key forms; an install step other than one simple command; an excluded step with another condition; a workflow header other than `ci.yml`'s; comparisons needing GitHub's number conversion or non-ASCII case folding, and objects used as values; step ids outside the documented job-id form, beginning with `__`, or differing only in case | stated limits; TOOLING (IF-35-15 to IF-35-21) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (as result v1.10 §8); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

Read on `main` at `0442d23` (`docs/pfcanon/` unchanged since `5e62a65`; this branch changes no canon). This round's subject, the YAML plain-scalar rule, falls under the same parser section already searched in results v1.18 and v1.19; canon holds nothing on YAML syntax, and the governing text is plan v1.0 §5.7. External reference, not canon: YAML 1.2.2 §7.3.3 "Plain Style", the source Codex cites.

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
