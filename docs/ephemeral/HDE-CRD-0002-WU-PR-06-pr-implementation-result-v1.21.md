---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.21"
record_kind: PR-35 checkpoint for the twenty-first corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.20.md (v1.20, PR-35 checkpoint; blob 5df92bdae297; 19,523 bytes; sha256 80aabd287fdc218314a5811ea534d565c4193c170ae36f6e67358ae72ccd1cb0); v1.19 (blob a694b81ce84a), v1.18 (blob b8ae075c826f), v1.17 (blob 78cc146ad6e9), v1.16 (blob 0d7b2026f6b4), v1.15 (blob 08cf62c76359), v1.14 (blob 456818eb3364), v1.13 (blob 6bce49444702), v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b, 161941f, d1a8969, 0783969, 0575fb0, ef06f44, 7be75ef, ba65334, bb52426, a7f1fdc, e4cda7d, a062ff7, d01599c, 153b67b, 5280748 and 9fc2b10, pushed; 657c22b119eb1a9168b1969f2801f8f03ba22fd6 (CX6-43 to CX6-45; parent 9fc2b10); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T06:40Z
next_step: push 657c22b and this record; answer the CX6-43 to CX6-45 threads naming 657c22b and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---




# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.21 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `9fc2b10` raised three P2 findings:

- CX6-43: the git metadata digest reads only files and symlinks, so an empty directory created under `.git` leaves the snapshot unchanged.
- CX6-44: a plain scalar holding a colon followed by a tab is read as text, though YAML rejects it.
- CX6-45: a sequence entry indented differently from its siblings joins the same list, though YAML rejects the collection.

Under PO-35-2 all three are fixed in `657c22b` (IF-35-22) and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-41 | Codex reviews 5571963225 to 5580742466 | `d2ed4fc` to `a062ff7` | as results v1.1 to v1.19 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-42 | Codex review 5580987020 | `153b67b` | as result v1.20 | fixed in `5280748` (result v1.20); thread answered and resolved |
| CX6-43 | Codex review 5581255096 (on `9fc2b10`), comment r4321888263, P2 | `9fc2b10` | `tools/ci/prepush_check.py` 312: "When a report or imported candidate module creates or removes an empty directory under the repository's Git directory, this digest ignores it because it visits only files and symlinks, while `_directory_entries` deliberately excludes `.git`"; "include Git metadata directory identities in the snapshot" | Confirmed at `9fc2b10`: in a scratch repository, creating `.git/empty-dir` or `.git/refs/empty` left `repository_state` equal to the state before. Fixed in `657c22b` (§3) |
| CX6-44 | same review, comment r4321888289, P2 | `9fc2b10` | `tools/ci/prepush_check.py` 537: "When a plain scalar contains a colon followed by a tab, such as an unused step environment value `HARMLESS: foo:\tbar`, this guard accepts it because it checks only `": "`"; "reject a colon followed by any YAML separation whitespace" | Confirmed at `9fc2b10`: `BASE_SHA: foo:\tbar` was read as that text, all 16 steps read. Fixed in `657c22b` (§3) |
| CX6-45 | same review, comment r4321888279, P2 | `9fc2b10` | `tools/ci/prepush_check.py` 635: "indenting only the second `on.pull_request.paths` entry by two extra spaces leaves the parsed header identical and `replay_steps` accepts it, while YAML rejects the malformed block collection"; "record the first item indentation and require every sibling to match it" | Confirmed at `9fc2b10`: the second `pull_request` path indented two spaces more, and the first indented two spaces more than the second, were each accepted, all 16 steps read. Fixed in `657c22b` (§3, IF-35-22) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-43 to CX6-45 (`657c22b`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `c9b2ba69b50b`; 2,132 lines; +19/−3 on `9fc2b10`) | **CX6-43.** `_metadata_digest` now walks every entry under each git directory. A directory's name enters the digest with a trailing `/`; files and symlinks are digested as before (bytes, and names and sizes under `objects/`). An empty directory created or removed under `.git` therefore changes the metadata part of `RepositoryState`. **CX6-44.** In `_plain`'s guard, the test for a mapping value inside a scalar is now a colon followed by a space or a tab (`re.search(r":[ \t]", value)`), where it was a colon and a space only. A colon followed by another character still reads as text (`foo:bar`). **CX6-45.** `_sequence` records its first entry's indentation and refuses an entry at any other ("indented differently from its sequence's first entry"), as `_mapping` already does for keys |
| `tests/tools/test_prepush_check.py` (blob `3e2f4ddec06d`; 1,229 lines; +19/−2) | `test_repository_state_covers_ignored_files` creates `.git/refs/empty`. It checks that the metadata changes while the status stays empty, and that removing the directory restores the metadata. `test_yaml_forms_the_parser_does_not_model_are_refused` gains `foo:\tbar`. `test_quoted_scalars_and_keys_are_read_as_yaml_reads_them` checks that `foo:bar` reads unchanged. New `test_sequence_entries_share_one_indentation`, with the two misindented `paths` lists of §2. 141 cases (139 + 2) |

## 4. CI on `9fc2b10`

Run 39377041715 (job 118477403367) on `9fc2b10` ran from 05:50:29Z to 06:09:56Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 05:54:26Z with CX6-43 to CX6-45. It was not waited on and is not a gate; its result covers `9fc2b10` only, whose code `657c22b` changes. The changed-tests failure of result v1.13 §4 did not recur.

## 5. Local validation of `657c22b`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `657c22b` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: items 1 and 2, the negative controls and item 9;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: the session checkout's owner-test run before the commit (141 passed);
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 141 passed in 49.4 s, pytest exit 0 |
| 2 | Pin and neighbouring files (`cand2`), one at a time | `test_rails_ci_workflow_integration.py` 138, `test_http_reader_ci_ownership.py` 4, `test_architecture_snapshot.py` 5, `test_epic020_bundle_tool.py` 6 passed; each pytest exit 0 |
| 3 | Classifier `0442d23..657c22b`, `pull_request` | exit 0; `reason=selected_lanes;paths=24;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test and the close-pack test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…`; `sweep --no-run` at the head and at `a429c7c` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0; `lanes` exit 0, eleven output records, PASS, repository unchanged; `sweep --no-run` at the head `uncovered=0`, exit 0, and at `a429c7c` `uncovered=135`, exit 1, as in result v1.15 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `657c22b`, committed there (05:58:14Z to 06:35:18Z, two at a time) | All 80 fail as intended, each clone clean afterwards. NC-11 to NC-87 fail the cases they failed at `5280748` (result v1.20 §5 item 5), with three explained differences. NC-47 (the whole guard removed) is retargeted to the rewritten guard line and also fails `foo:\tbar`. NC-63 (the guard's second line removed) is retargeted the same way and also fails `foo:\tbar`, which that line now refuses. NC-87 (the `-`, `?`, `:` rule as it was before) no longer fails `:\tx`, because the new colon-and-tab test also refuses it; it still fails `-\tx` and `?\tx`. The three new controls: NC-88 (metadata directories skipped) fails the repository-state test. NC-89 (a colon and a space only) fails `foo:\tbar`. NC-90 (the sequence indentation check removed) fails the new sequence test |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` (integ2 with the real-setuptools site, integ3, integ4) | output byte-identical to result v1.20's, all three, each exit 0. The real workflow's sequences each keep one indentation, and no plain scalar in it holds a colon before whitespace. `cand2` clean |
| 7 | Premises at `9fc2b10` (that head's tool, scratch only), and the fix (the tool at `657c22b`) | At `9fc2b10`: each case of §2 as listed there; the real workflow 16 steps. Under the fix: both metadata directories change the state, and removing them restores it. `foo:\tbar` is refused, while `foo:bar` and `url:x` still read. Both misindented `paths` lists are refused, naming line 7. The real workflow still 16 steps. Rounds 15 to 21's premise cases at `657c22b` give their earlier outputs |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 05:58:14Z to 06:28:17Z (concurrent with items 5 and 9); classify `reason=selected_lanes;paths=24`, all seven lanes; every one of the 16 steps SUCCESS. Changed tests 4,027 passed (result v1.20's 4,025 plus the two new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,797.3 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`, now with metadata directories in the comparison. `cand` before and after: `head=657c22b…`, `status_lines=0`, `git_metadata_digest=a17751d28bda6b01ce627993b19875452b7547605ee379f81ef9d74974a22a68`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,327 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,483.2 s (05:58:14Z to 06:23:13Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.20's 5,325 plus the two new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-21 | as results v1.1 to v1.20 §6 | unchanged | as recorded there |
| IF-35-22 | Two choices. First, CX6-43 adds metadata directories by name, not by `lstat` identity (mode, mtime and ctime), as the working-tree directories are. Any entry created and removed in a git directory changes that directory's mtime, so an `lstat` comparison would fail on a transient entry that leaves nothing behind. A name catches what the finding describes, a directory created or left behind, and the metadata's files are already compared by content. Second, CX6-45 requires one indentation for all entries of a sequence, as `_mapping` does for keys, rather than modelling the forms YAML gives such lines (a continuation of the previous plain scalar, or an error). Consequence: such a workflow gets a TOOLING failure from the replay; hosted CI is unaffected | The tool's read-only claim covers the git metadata, so a directory it creates there must not pass unseen. A list that the replay reads as identical to GitHub's while GitHub rejects it lets the replay run a workflow GitHub never runs. The real workflow's sequences each keep one indentation, and its metadata is unchanged by every report (§5 items 6 and 8). This extends plan §5.2's digest, "every file under the git dir and the common dir by content, plus names and sizes under `objects/`", to directory names. PO-35-2; plan §5.2 ("The tool's own assertion"), §5.7 (the parser, "a strict subset fails closed on any construct it does not understand"); PD-8 | §5 items 1, 5 (NC-47 and NC-63 retargeted; NC-88 to NC-90), 6, 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.20 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 05:50:19 | push 20 of PR-35: `153b67b..9fc2b10` (`5280748`, the v1.20 record), fast-forward, no force | remote head `9fc2b10…`; v1.20 read back from the remote: blob `5df92bdae297`, 19,523 bytes, sha256 equal to the local file |
| about 05:50:30 | first reply to CX6-42: the call failed with a connection error ("upstream connect error or disconnect/reset before headers"); the thread resolve sent with it succeeded | the thread read back with no reply, so nothing was posted |
| 05:50:33 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved to 06:40Z | it creates no session |
| 05:52:50 | reply r4321880383 (CX6-42) naming `5280748`, sent again once the thread showed none | GitHub, read back at about 06:36: the reply present, `is_resolved: true` |
| 05:50:29 to 06:09:56 | CI run 39377041715 on `9fc2b10`: success, stale | §4 |
| 05:50:40 to 05:54:26 | Codex code review on `9fc2b10` (trigger "New commits"): review 5581255096, findings CX6-43 to CX6-45 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 05:58:13 | local commit `657c22b` | §3 |
| 05:58:14 to 06:35:18 | local validation of `657c22b`, all passed | §5 |
| after this record | push 21 of PR-35: `657c22b` and the commit adding this record, fast-forward onto `9fc2b10`, no force | read back in the next record |
| next | answer the CX6-43 to CX6-45 threads naming `657c22b` and resolve them; move the safety-net check-in; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (result v1.13 §4; PR comment 6280395750) | PR-35 watches each new head's CI; the close-pack tool and test are outside this PR's change set | did not recur on `161941f`, `0783969`, `ef06f44`, `ba65334`, `a7f1fdc`, `a062ff7`, `153b67b` or `9fc2b10` (results v1.14 to v1.21 §4); intermittent, mechanism not established |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
| Metadata directories are compared by name; a change to a git directory's mode alone is not seen, as a file's mode alone is not (IF-35-22) | stated limit | recorded |
| `GITHUB_OUTPUT` forms other than `NAME=VALUE`; YAML escape sequences, folding around more-indented lines, typed scalars other than `true`, `false` and decimal integers in `env` and `with`, tabs in leading whitespace, plain scalars beginning with an indicator or holding a colon before whitespace, sequence entries at different indentations, and the other unmodelled scalar, block and key forms; an install step other than one simple command; an excluded step with another condition; a workflow header other than `ci.yml`'s; comparisons needing GitHub's number conversion or non-ASCII case folding, and objects used as values; step ids outside the documented job-id form, beginning with `__`, or differing only in case | stated limits; TOOLING (IF-35-15 to IF-35-22) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (as result v1.10 §8); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

Read on `main` at `0442d23` (`docs/pfcanon/` unchanged since `5e62a65`; this branch changes no canon). This round's subjects are the parser (a colon before a tab; sequence indentation), searched in results v1.18 to v1.20, and the read-only snapshot. For the snapshot, `docs/pfcanon/` on `main` and plan v1.0 were searched for "git metadata", "read-only" and "repository unchanged". Canon holds nothing on either (its "read-only" hits concern Reality Audit checks and evidence tools). The governing text is plan v1.0 §5.7 for the parser and §5.2 for the read-only contract, whose "tool's own assertion" defines the metadata digest as "every file under the git dir and the common dir by content, plus names and sizes under `objects/`". External reference, not canon: YAML 1.2.2 §7.3.3 and §8.2.1 "Block Sequences".

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
