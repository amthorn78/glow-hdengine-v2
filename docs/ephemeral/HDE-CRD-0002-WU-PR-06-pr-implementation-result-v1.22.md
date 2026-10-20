---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.22"
record_kind: PR-35 checkpoint for the twenty-second corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.21.md (v1.21, PR-35 checkpoint; blob 7a495445b837; 22,524 bytes; sha256 251b55df9ff600075a61879ee96d58de5240126bebe8d4fd8dc2de24806b7ec9); v1.20 (blob 5df92bdae297), v1.19 (blob a694b81ce84a), v1.18 (blob b8ae075c826f), v1.17 (blob 78cc146ad6e9), v1.16 (blob 0d7b2026f6b4), v1.15 (blob 08cf62c76359), v1.14 (blob 456818eb3364), v1.13 (blob 6bce49444702), v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-06
work_unit_title: "Read-only pre-push and pre-plan check (PR; Distillation; S20)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob f3a6a8855ec0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0.md (v1.0; blob 2848847e8bee)
effective_baseline: unchanged from result v1.0 (approved base + PF10 addenda 2.2, 2.3, 2.4, 2.5, 2.9, 2.10)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md (v13.6.1; sha256 ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e; unchanged on origin/main 0442d23). Provenance, not a gate
pf10_addendum_created: none
proceed: the original Proceed of result v1.0. No other Proceed exists or is needed; PO-35-4 is an in-flight design decision, not a rescope (§2a)
session: the dedicated HDE-CRD-0002 WU-PR-06 PR-35 session, https://claude.ai/code/session_01SVmct81WDzDqX36ZasAijn
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e); primary skill glow-hde-pr-development 1.4.0; support skill glow-write-boundary
pull_request: amthorn78/glow-hdengine-v2#660 (https://github.com/amthorn78/glow-hdengine-v2/pull/660), branch claude/youthful-gauss-d9e0ab into main
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b, 161941f, d1a8969, 0783969, 0575fb0, ef06f44, 7be75ef, ba65334, bb52426, a7f1fdc, e4cda7d, a062ff7, d01599c, 153b67b, 5280748, 9fc2b10, 657c22b and fffd679, pushed; 30158afda0a2b91c1530e5c1874835529b7b6fbb (PO-35-4, CX6-46, CX6-48; parent fffd679); the record commit that adds this file (docs/ephemeral/ only). c912b04 was committed locally, never pushed, and is superseded by 30158af (§7)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T09:15Z
next_step: push 30158af and this record once; answer the CX6-46 to CX6-48 threads naming 30158af and resolve them; re-arm the safety-net check-in; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---




# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.22 (PR-35 checkpoint)

## 1. State

**Correction first.** The subjects of four pushed commits, `e4cda7d`, `d01599c`, `5280748` and `657c22b`, read "(S21)". The requirement is S20, as the work unit's title states. Their bodies, the code and the records carry S20, and nothing else depends on a subject. History is not rewritten. `30158af` and later commits use S20. The unpushed `c912b04` had the same error.

**PR-35 checkpoint, non-terminal.** The Codex re-review of `fffd679` raised three P2 findings, CX6-46 to CX6-48 (§2). Before acting on them, I put the length of the review loop and then the replay's design to Nathan. He decided two things (§2a):
- PO-35-4 narrows the replay, as an in-flight design change.
- PO-35-5 replaces PO-35-2 as the rule for findings.

`30158af` implements PO-35-4 and folds in what still applies of the unpushed `c912b04`:
- CX6-46 and CX6-48 are fixed.
- CX6-47 needs no parser change: the replay now refuses every `ci.yml` but the pinned one before reading it.

The change is verified locally (§5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-42 | Codex reviews 5571963225 to 5580987020 | `d2ed4fc` to `153b67b` | as results v1.1 to v1.20 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-43 to CX6-45 | Codex review 5581255096 | `9fc2b10` | as result v1.21 | fixed in `657c22b` (result v1.21); replies r4322142031, r4322142323 and r4322142671; threads resolved |
| CX6-46 | Codex review 5581590543 (on `fffd679`), comment r4322172632, P2 | `fffd679` | `tools/ci/prepush_check.py` 325: "if a report or imported candidate overwrites an existing loose object with different bytes of the same length, this branch produces the same digest because it records only the object's path and size"; "include each object's lstat identity or content in the snapshot" | Confirmed at `fffd679`: in a scratch repository, an unreachable loose object overwritten with different bytes of the same length left `repository_state` equal. A breach of the read-only guarantee, so fixed under PO-35-5, in `30158af` (§3) |
| CX6-47 | same review, comment r4322172639, P2 | `fffd679` | `tools/ci/prepush_check.py` 538: "When a candidate workflow contains a forbidden control character only in a comment, such as `name: ci # \x01`, this strips the comment before validating the scalar, so the parsed workflow still matches the pinned header and replay can PASS"; "validate the full input's permitted character set before discarding comments" | Confirmed at `fffd679`: `name: ci # ` followed by U+0001, U+007F, U+0085, U+2028 or U+000C was read, all 16 steps. Addressed by PO-35-4 (a) in `30158af`: the replay now hashes the head's `ci.yml` and refuses any text but the pinned one before parsing. At `30158af`, that workflow committed in a scratch clone got `TOOLING_FAILURE REPLAY_INVENTORY_DRIFT` in 4 s, with no step run (§5 item 7). The real `ci.yml` holds none of these characters. `c912b04`'s character check is not kept |
| CX6-48 | same review, comment r4322172627, P2 | `fffd679` | `tools/ci/prepush_check.py` 387–388: "when a report or imported classifier rewrites an existing tracked regular file with identical bytes, `git status` remains empty, while this state records identities only for ignored files and directories"; "include lstat identities for tracked files as well" | Confirmed at `fffd679`: a tracked file rewritten with its own bytes left `repository_state` equal. A breach of the read-only guarantee, so fixed under PO-35-5, in `30158af` (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

## 2a. Product Owner decisions PO-35-4 and PO-35-5

PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a.

**The questions as put.**
- **07:06Z.** After Nathan asked why the phase was taking so long, I reported the loop: 23 rounds, 48 findings, new ones in every round. I asked "which rule applies to further Codex findings on PR #660?", with three options:
  1. keep "fix every finding";
  2. a bounded rule (recommended);
  3. stop after this round.
- **Nathan, during that turn:** "It's not about declining findings, it's about possible problems with the whole architecture of the WU. If there's so many views, then it makes me feel like there's a larger flaw."
- **07:12Z.** I answered that the flaw is in the replay's design. The counts by part of the tool:

  | Part | Findings |
  | :- | -: |
  | `replay` | 41 |
  | the read-only snapshot | 6 |
  | `sweep` | 1 |
  | `lanes`, `membership`, `build-notes` | 0 |

  The replay rebuilds slices of GitHub's YAML reading, its workflow rules and expressions, the runner and `pip` in plain Python, and plan PD-8 promised to fail closed on any difference, so there is no last finding. I asked "how should the replay work?", with three options:
  1. keep hardening;
  2. narrow the replay (recommended): (a) a stored fingerprint of `ci.yml`, (b) the install step as a stated precondition, (c) no report running repository code against the checkout;
  3. take the replay out of this unit.

  I said that options 2 and 3 depart from the instruction and would go to the Implementation Agent as a rescope request, and that I was holding `c912b04` unpushed meanwhile.

**Nathan's decision, 07:22:18Z, verbatim:**

> Product Owner decisions for PR #660 (WU-PR-06, PR-35):
>
> PO-35-4 — replay design: option 2, as an in-flight design change, not a rescope (instruction v1.0 §9.1 leaves the parser and the copy mechanism to the plan; §14 says such a choice is not a rescope trigger; ID-8 already makes the install step a precondition; no later planned unit edits ci.yml). Record it as an in-flight decision, as PO-35-3 was.
>  (a) The replay runs only a ci.yml whose SHA-256 equals the value the tool stores. The owner test pins it, so a PR that edits ci.yml updates it in the same PR.
>  (b) The install step is a stated precondition: check that each distribution the step names is installed, and report what is missing as TOOLING. Drop the build-system, [tool.setuptools] and editable-metadata modelling, so WU-PR-08's pyproject.toml change cannot break the replay.
>  (c) No report runs repository code in the caller's checkout: lanes and membership work from a throwaway copy. Keep the snapshot as a safety check.
>
> PO-35-5 — replaces PO-35-2 for the rest of this PR: fix a Codex finding when it shows a wrong result or a crash on the repository's real ci.yml, real install step or real tree, or a breach of the read-only or no-secrets guarantees. Otherwise reply on the thread with the path you traced and the stated limit, and resolve it. Ask me only before declining a P1 or a security finding.
>
> Do not push c912b04 on its own. Fold whatever of it still applies into the option 2 change, validate as before, and push once.

His ruling settles that PO-35-4 is not a rescope. My statement at 07:12Z that it would need one is withdrawn. It is recorded as IF-35-23 (§6).

## 3. Change (`30158af`)

Both paths are in plan §6.1. No path outside the change set moves (instruction ID-12 not engaged), and `ci.yml` is unchanged.

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `690cd2bd4171`; 1,755 lines, from 2,132 at `fffd679`; +177/−554) | **(a) The pin.** `REPLAY_WORKFLOW_SHA256 = "d02021f3…b6ab9b"`, the SHA-256 of the real `ci.yml`, as instruction §5.2 measured it at `5e62a65`. `report_replay` reads the copy's `ci.yml` bytes and refuses any other digest with TOOLING `REPLAY_INVENTORY_DRIFT`, before the parser sees the text. It then prints `workflow .github/workflows/ci.yml sha256=… (the modelled one)`. The parser, the inventory and the expression evaluator are unchanged; in a replay they now only ever read the pinned file. **(b) The install precondition.** `_install_check` replaces the install modelling. The step must still be one simple `python -m pip install` or `pip install` command, and must name something. The check collects every distribution the step names: the words on its command line, the requirements in its `-r` files (nested `-r` followed, any other option refused) and the editable project by its `[project].name`. It reports any that `importlib.metadata` does not find as "TOOLING the caller's environment lacks distributions the install step names: …". A requirement's extras, version clauses and marker are not read; a URL, a path or another form fails closed. Removed: the modelled build system and `[tool.setuptools]` configuration, the PEP 440 version and PEP 508 marker evaluation, the dependency walk, the module-location and configuration checks and the editable-metadata comparison, with their constants and regular expressions. **(c) Throwaway copies.** `lanes` in both modes and `membership` now make a copy of the head (`lanes-copy`, `membership-copy`). They run the classifier there, in a child process whose working directory is the copy (`in_copy`, which calls the tool's own `normalized_paths` or `classify_given_paths` and reads their JSON answer). `membership` reads the admitted release from the copy and prints the head it read. Ref-mode `lanes` checks that the base is available to the copy, then always runs the head's classifier CLI there. The tool's own process no longer imports any repository module. **Folded from `c912b04`.** Each object under `objects/` enters the metadata digest by its `lstat` identity (mode, size, `mtime_ns`, `ctime_ns`), not its size alone (CX6-46). Every tracked file's `lstat` identity is a new `tracked` part of `RepositoryState`, sharing `_lstat_entries` with the ignored files (CX6-48). Not kept: `c912b04`'s check for characters YAML forbids (CX6-47), which the pin makes unreachable on any other workflow. The module docstring, which `--help` prints, states the pin, the presence-only precondition and the copies |
| `tests/tools/test_prepush_check.py` (blob `7a2eb7605aad`; 1,065 lines, from 1,229; +109/−273) | The inventory test asserts that the real `ci.yml`'s SHA-256 equals the pin. The synthetic replay tests first check that the real tool refuses the synthetic workflow (`REPLAY_INVENTORY_DRIFT`, no step line). They then run a copy of the tool that carries that workflow's digest (`_pinned_tool`). New: `test_install_substitute_checks_only_that_each_named_distribution_is_installed`, `test_the_real_install_step_names_only_installed_distributions` and `test_lanes_and_membership_run_the_classifier_only_in_a_throwaway_copy`. The last plants a write in a clone's classifier and checks three runs: `lanes --full`, `lanes --path` and `membership --path` each exit 0, the checkout is untouched, and the planted write lands in `lanes-copy`. `test_repository_state_covers_ignored_files` gains the same-bytes rewrite of a tracked file and the same-length overwrite of an unreachable object. The missing-inputs test expects "failed in the throwaway copy". Removed: the three install-modelling tests (the PEP 440 and 508 cases, the extras, dependencies and editable project, and the specifier cases) with their fixtures. 137 cases (141 at `fffd679`) |

## 4. CI on `fffd679`

- **Run.** Run 39381502111 (job 118491414225) on `fffd679` was created at 06:37:54Z. The job ran from 06:37:57Z to 06:58:37Z and completed on its own with conclusion `success`.
- **Stale.** It became stale at 06:42:51Z, when review 5581590543 posted CX6-46 to CX6-48. It was not waited on and is not a gate. Its result covers `fffd679` only, whose tool `30158af` replaces.
- **Changed-tests failure.** The failure of result v1.13 §4 did not recur.

## 5. Local validation of `30158af`

The environment is as result v1.1 §5:
- closed rails with the keys unset;
- a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`;
- `ruby` 3.3.6, `bash` and `curl`.

**Clones.** `cand` (replay), `cand2` (short checks) and `sweep` were moved to `30158af` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control.

**How each check reaches the code under test.**
- `PYTHONPATH` set to the clone: items 1 and 2, the negative controls and item 9.
- The replay's own `PYTHONPATH`, set to its copy: item 8.
- The working directory, which `python -m pytest` puts first on `sys.path`: the session checkout's owner-test run before the commit (137 passed in 129.2 s).
- The tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 137 passed in 149.9 s, pytest exit 0 (§6, IF-35-23, on the duration) |
| 2 | Pin and neighbouring files (`cand2`), one at a time | `test_rails_ci_workflow_integration.py` 138, `test_http_reader_ci_ownership.py` 4, `test_architecture_snapshot.py` 5, `test_epic020_bundle_tool.py` 6 passed; each pytest exit 0 |
| 3 | Classifier `0442d23..30158af`, `pull_request` | exit 0; `reason=selected_lanes;paths=25;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test and the close-pack test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…`; `lanes --path tools/ci/prepush_check.py`; `membership --path tools/ci/prepush_check.py --path engine/core/core.py`; `build-notes`; `sweep --no-run` at the head and at `a429c7c` | `AGENTS_MD_CITATIONS_OK`, exit 0. `[env-pins] OK: …`, exit 0. `--help` exit 0, naming `REPLAY_WORKFLOW_SHA256`. `lanes` exit 0, eleven output records, "classified in a throwaway copy at 30158af…", PASS. `lanes --path` exit 0, `lanes=product`, PASS. `membership` exit 0: `not-member tools/ci/prepush_check.py`, `member engine/core/core.py`, PASS. `build-notes` exit 0: PF10 v13.6.1, 208,266 bytes, sha256 `ca2d91c5…`. Each `lanes` and `membership` run ended "repository unchanged". `sweep --no-run` at the head `uncovered=0`, exit 0, and at `a429c7c` `uncovered=135`, exit 1, as in result v1.15 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `30158af` and committed there (07:41:08Z to 09:12:25Z, two at a time) | All 70 fail as intended, each clone clean afterwards. The 60 kept from round 22 fail exactly the cases they failed at `657c22b` (result v1.21 §5 item 5). Retired: the 20 controls of the install modelling (NC-11 to NC-17, NC-19, NC-22 to NC-25, NC-34, NC-43, NC-48, NC-51 to NC-54, NC-68), whose guarded code is removed; NC-93 and NC-94 belonged to `c912b04`'s character check, which is not kept. New: NC-91 (tracked identities left out) and NC-92 (objects by name and size only) fail the repository-state test. NC-95 (the pin check removed) fails both synthetic replay cases. NC-96 to NC-99 (the presence check, the editable project's name, the `-r` names, the requirement form) fail the new install test. NC-100 to NC-102 (ref-mode `lanes`, given-path `lanes` and `membership` each run in the checkout) fail the copy test |
| 6 | The real `ci.yml`, install step and environment through the tool at `cand2` (integ5) | exit 0. The real `ci.yml`'s SHA-256 equals the pin. 16 steps, `python-version` 3.12, `runs-on: ubuntu-latest`. The install step `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` names `Flask`, `glow-hdengine`, `gunicorn`, `jsonschema`, `psycopg`, `pytest`, `pytest-cov`, `pytest-mock`, `setuptools` and `wheel`. All ten are installed in the venv, and all ten are reported missing against an empty site. The substitute returns success. `cand2` clean. integ2 to integ4 are retired; they exercised the install modelling `30158af` removes |
| 7 | Premises at `fffd679` (that head's tool, scratch only), and the change (the tool at `30158af`) | **(a)** At `fffd679` the tool has no pin, and an edited workflow is read (16 steps). At `30158af` the pin equals the real workflow's digest and not the edited one's. A scratch clone at `30158af` with `# ` and U+0001 added to `ci.yml`'s first line got `TOOLING_FAILURE REPLAY_INVENTORY_DRIFT` from `replay` in 4 s, with no step run and the clone clean (CX6-47). **(b)** At `fffd679` the install check refuses a changed `[tool.setuptools]` packages list ("configuration the replay does not model"); at `30158af` it reports nothing missing. **(c)** With a classifier that writes a file beside itself when it loads, at `fffd679`: `lanes --path`, `membership --path` and `lanes --full` each exit 4 (read-only violation), with the write in the checkout. At `30158af` each exits 0 and the checkout is untouched. **CX6-46 and CX6-48:** at `fffd679` both states compare equal; at `30158af` both differ. **Earlier rounds:** rounds 15 to 23's premise scripts give their round-23 outputs, with two expected exceptions. Round 16's requirement cases call the removed requirement parser. Round 23's character cases are read by the parser alone, which the pin now guards |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 07:41:08Z to 08:16:24Z (concurrent with items 5 and 9). `workflow .github/workflows/ci.yml sha256=d02021f3… (the modelled one)`; classify `reason=selected_lanes;paths=25`, all seven lanes. Every one of the 16 steps SUCCESS; the install step's substitute reads "every distribution the step names is installed". Changed tests 4,023 passed (result v1.21's 4,027 less the four removed owner-test cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`. `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 2,108.8 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`, with tracked files and objects now compared by identity. `cand` before and after, by the scratch digest of result v1.1 §5: `head=30158af…`, `status_lines=0`, `git_metadata_digest=3e8fbb68d53a55cc4d4fa787ab66a8c40baadd114cf5d24cbf6875079ab85eb2`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,323 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,785.2 s (07:41:08Z to 08:11:14Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.21's 5,327 less the four removed owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-22 | as results v1.1 to v1.21 §6. IF-35-7, IF-35-12 and IF-35-14, the install modelling, are superseded by IF-35-23 (b). IF-35-15 to IF-35-22's parser rules stay, now reached only by the pinned file | unchanged | as recorded there |
| IF-35-23 | PO-35-4, as §3 implements it. **(a)** The pin is the SHA-256 of `ci.yml`'s raw bytes, checked before parsing. The parser is kept, because the inventory, conditions and expressions still read the pinned file. Consequence: contract G-3 (instruction §8) widens from "a step added, renamed or removed" to any change to `ci.yml`. Such a PR fails the owner test and gets TOOLING from the replay until it updates the pin; hosted CI is unaffected. **(b)** Presence is checked by distribution name, through `importlib.metadata` on the tool's interpreter's `sys.path`. This is plan §5.7's original rule for the install step, before IF-35-7, IF-35-12 and IF-35-14 added the modelling. Consequence: a wrong version, a missing dependency or stale editable metadata in the caller's environment is no longer caught before the steps run. It shows, if at all, as a step's own failure. A `pyproject.toml` change other than to `[project].name` (WU-PR-08) cannot fail the replay. **(c)** The classifier runs in a child process inside a copy of the head, which calls the tool's own functions and answers in JSON. That keeps one code path for both `lanes` modes and `membership`, and leaves nothing of the repository's in the tool's process. Plan §5.2 ("membership and given-path lanes read the checkout") and §5.3 and §5.4 (the checkout's classifier, loaded by path) change accordingly. Consequence: each `lanes` or `membership` run now costs a copy of the head. The owner test, which runs them many times, went from 49.4 s for 141 cases at `657c22b` to 129.2 to 149.9 s for 137 cases (§5 item 1). In a profiling run (159.0 s), three cases took 146.4 s: `test_lanes_equals_the_classifier_for_refs_and_for_given_paths` 73.5 s, `test_lanes_and_membership_run_the_classifier_only_in_a_throwaway_copy` 46.9 s and `test_reports_on_a_clone_of_the_repository_are_read_only` 26.0 s. Each of their runs copies the head's 8,068 tracked files. Plan §5.10's "25 to 32 s" was for 21 cases at PR-30. CI runs the owner test as a changed-test target when the tool or the test changes, and as a full-validation target. **The snapshot** is kept as a safety check, as directed. It now also compares tracked files and objects by `lstat` identity (CX6-46, CX6-48); directories under `.git` stay compared by name (IF-35-22) | PO-35-4 directs the design; PO-35-5 makes CX6-46 and CX6-48 fixes, since both breach the read-only guarantee. Instruction ID-8 makes CI's install a precondition ("the caller's environment must already have CI's install"). §9.1 leaves the replay parser and the copy mechanism to the plan, and §14 says such a choice is not a rescope trigger | §5 items 1, 4, 5 (the 22 controls whose guarded code is removed are retired; NC-91, NC-92 and NC-95 to NC-102 are new), 6, 7, 8, 9 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.21 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| about 06:37:50 | push 21 of PR-35: `9fc2b10..fffd679` (`657c22b`, the v1.21 record), fast-forward, no force | remote head `fffd679…`; v1.21 read back from the remote: blob `7a495445b837`, 22,524 bytes, sha256 equal to the local file |
| 06:37:55 to 06:38:02 | replies to CX6-43, CX6-44 and CX6-45 naming `657c22b`: r4322142031, r4322142323, r4322142671 | GitHub ids returned |
| 06:38:03 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved to 07:28Z | it creates no session |
| 06:38:08 to 06:38:10 | CX6-43 to CX6-45 threads resolved | "is now resolved", each |
| 06:37:57 to 06:58:37 | CI run 39381502111 on `fffd679`: success, stale | §4 |
| to 06:42:51 | Codex code review on `fffd679`: review 5581590543, findings CX6-46 to CX6-48 | three unresolved threads, `PRRT_kwDOP103ks6uOXrG`, `…rL`, `…rD` |
| 06:43:52 | the three premises confirmed at `fffd679`, scratch only | §2 |
| 06:47:50 | local commit `c912b04`: CX6-46 to CX6-48 as first fixed, CX6-47 by a character check | its validation started at 06:48:14 (owner test 149 passed; replay PASS; sweep 5,335 passed) and is not evidence for `30158af` |
| 07:06:17, 07:12:01 | the two questions of §2a | conversation |
| 07:22:18 | PO-35-4 and PO-35-5 | §2a, verbatim |
| 07:29:01 | the safety-net check-in fired, its text still naming PO-35-2 | read; acted on by re-arming after push 22 |
| 07:40:55 | local commit `30158af` (parent `fffd679`); `c912b04` not pushed, per "Do not push c912b04 on its own" | §3 |
| 07:41:08 to 09:12:25 | local validation of `30158af`, all passed | §5 |
| after this record | push 22 of PR-35: `30158af` and the commit adding this record, fast-forward onto `fffd679`, no force | read back in the next record |
| next | answer the CX6-46 to CX6-48 threads naming `30158af` and resolve them; re-arm the check-in with PO-35-4 and PO-35-5; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-5 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (result v1.13 §4; PR comment 6280395750) | PR-35 watches each new head's CI; the close-pack tool and test are outside this PR's change set | did not recur on `161941f`, `0783969`, `ef06f44`, `ba65334`, `a7f1fdc`, `a062ff7`, `153b67b`, `9fc2b10` or `fffd679` (results v1.14 to v1.22 §4); intermittent, mechanism not established |
| The replay runs only the `ci.yml` whose SHA-256 is `REPLAY_WORKFLOW_SHA256`. A PR that changes `ci.yml` in any way updates the pin, and the model if needed, in the same PR (G-3 as widened, IF-35-23) | the PR that edits `ci.yml`; WU-DOC-01's usage note (G-1) | stated limit |
| The install step is checked for presence only. Versions, extras, markers, dependencies, the build system and the editable project's metadata are the caller's to match (IF-35-23) | stated limit, as instruction ID-8 | recorded |
| The parser's unmodelled YAML and expression forms (IF-35-15 to IF-35-22) | stated limit. The pinned file uses none of them, and any other workflow is refused first | recorded |
| Children are not network- or file-system-sandboxed (CX6-15). `lanes` and `membership` now also run the classifier in a child, in a copy | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| Directories under `.git` are compared by name; a change to such a directory's mode alone is not seen (IF-35-22). Files and objects are compared by content or `lstat` identity | stated limit | recorded |
| CI's pip release, and the install step's isolated build environment (results v1.21 §8 and earlier) | moot: IF-35-23 (b) no longer models either | closed |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (as result v1.10 §8, plus the pin rule and the presence-only precondition); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

**Searches.** Canon was read on `main` at `0442d23`; `docs/pfcanon/` is unchanged since `5e62a65`, and this branch changes no canon. This round's subjects are a stored workflow digest, the install step as a precondition, and running repository code only in a copy. I searched `docs/pfcanon/` on `main` for "throwaway", "pre-push", "prepush", "pre-plan", "replay", "precondition", "fingerprint", "pinned workflow", a `ci.yml` digest, "WU-PR-06" and "S20".
- Canon holds nothing on the tool's design. The hits concern chart and composite fingerprints (PF01), the DDL fingerprint and replayable command transcripts (PF04), and PF10's WU-PR-06 entries: addendum 2.2's ruby requirement, which `sweep` still checks, and the plan-stage lines.
- The governing text is instruction v1.0: ID-8, §8 contracts G-1 and G-3, §9.1 and §14. It is applied through PO-35-4 and PO-35-5 and plan v1.0 §5.2 to §5.4, §5.7, §5.10 and PD-8.

| Topic | Sources and sections |
| :- | :- |
| Phase authority, review chain, stale CI, merge boundary | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (all sections); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 |
| Review chain overlay | PF10-HDE-Build-Notes v13.6.1 addendum 2.3 (Rules 1 to 5) |
| Sweep tools | PF10-HDE-Build-Notes v13.6.1 addendum 2.2 ("WU-PR-06's sweep environment must provide ruby") |
| Tooling vs behavior | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 |
| Closed rails | Glow QA Guide §2.2.6 "Rails posture in CI (default CLOSED)" |
| In-flight scope and the design change | instruction v1.0 ID-2, ID-8, ID-9, ID-12, §6, §7 ("Dependencies"), §8, §9.1, §14; plan v1.0 §5.2, §5.3, §5.4, §5.7, §5.10, PD-8, §6.1, §13; PO-35-4 and PO-35-5 (§2a) |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" and its corollary on exit statuses |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
