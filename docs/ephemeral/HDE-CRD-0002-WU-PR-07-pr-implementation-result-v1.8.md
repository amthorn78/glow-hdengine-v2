---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.8"
result: none (PR-35 checkpoint after the seventh corrective commit; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.7.md (preserved unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (on this branch; read as provenance; governing canon read from main)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
branch: claude/gallant-cerf-ysdde5
remote_head_before_push: abc02545b62db3a4b9545b9103b7207a4ebc996a
commits_in_this_push: ff0de6e (CX7-9 fix), 0fc625d (CX7-9 test correction), and this record
created_at: 2026-10-21T00:40:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.8 (PR-35 checkpoint)

## 1. State

Nonterminal.

- **Codex round 7** (review 5593304287, on `abc0254`) did not re-raise CX7-8, whose thread was resolved. It raised one P1, CX7-9, in the same class. The session asked the Product Owner one design question and got PO-35-5 (§2).
- **The fix** is `ff0de6e`, with a test correction in `0fc625d`. Both are pushed with this record.
- **Hosted CI is red on a third head**, `abc0254` (run 39518303974), with the same 7 tests as on `45e4cef` and `b0a7305` (§5).
- **Root cause now established (§5).** It corrects v1.7 §5, which left the access-time cause unknown. GitHub moved the `ubuntu-latest` label from `ubuntu-24.04` to `ubuntu-26.04` between the last passing run and the first failing one. Under 26.04's separate `strictatime` `/tmp`, `main`'s own code fails the same 7 tests. A re-run on `ubuntu-latest` therefore cannot pass.
- **Product Owner statement PO-35-6:** "I can rerun CI manually as needed". §8 records why a re-run cannot make this head's CI green, and the decision that remains.

## 2. Product Owner decision PO-35-5 (round 7)

The question put CX7-9 as found: the writer trusted each ledger entry's `PASS` without opening the `primary.log` it names. A tracked ledger saying `PASS` next to a missing or failing primary would still close `SATISFIED`. The canonical harness never writes such a pair; only a hand edit or a partial commit does.

The options offered:
- read the primaries (recommended);
- decline as non-real, which under addendum 2.14 needs the Product Owner's approval;
- rescope.

**Answer: "Read the primaries (Recommended)".** The option's text:
- for each ledger entry, the writer reads its `primary.log` from the tracked tree; it must be tracked, otherwise `QA_LEDGER_INVALID`;
- it parses the first-line PF27 v2 header and requires `check_id` and `status` to match the ledger, otherwise `QA_LEDGER_INVALID`;
- the primaries' digests go into the manifest inputs;
- the writer stays stdlib plus `jsonschema`.

## 3. Review findings (round 7)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-9 | Codex, `abc0254`, P1 (thread `PRRT_kwDOP103ks6ukn1h`, comment 4331617729) | `_require_v2_semantics` | The writer checked only the `log_path` string's shape and trusted the ledger's status, so `SATISFIED` could close over a missing primary or one that records a failure | The canonical harness writes the ledger and its primaries together and never writes a disagreeing pair. A disagreeing pair arises from a hand edit (forbidden for governed artifacts) or a partial commit. The Product Owner chose to fix it (PO-35-5) | Fixed in `ff0de6e` and `0fc625d` (PO-35-5) |

Answered by round 7 and resolved: CX7-8 (`PRRT_kwDOP103ks6ukJ80`). Rule 8: the class recurred again in round 7. Its answer is the Product Owner's decision PO-35-5.

## 4. Implementation (`ff0de6e`, `0fc625d`)

- **Writer** (`tools/qa/generate_epic_close_pack.py`):
  - New `_primary_identity`, which parses the first-line `pf27.step_log_header.v2` header.
  - After the semantic checks, for each ledger entry, `_load_model_v2`:
    - requires `log_path` in the tracked tree;
    - admits the primary as a causal input and captures it;
    - requires its header's `(check_id, status)` to equal the entry's. Otherwise `QA_LEDGER_INVALID`.
  - The primaries are captured with the other inputs. They render as `- QA primary: …` lines under "Source bindings", and appear in the manifest as `inputs.qa_primaries`.
- **Tests** (`tests/qa/test_generate_epic_close_pack.py`):
  - `test_v2_real_primaries_agree_with_their_real_ledgers`: the header of every primary named in the four tracked ledgers (HDE-CRD-0001, HDE-EPIC021, HDE-EPIC039, HDE-EPIC040) agrees with its ledger entry.
  - `test_v2_report_and_manifest_bind_each_qa_primary`.
  - `test_v2_qa_ledger_entries_must_agree_with_their_tracked_primaries`, with four cases: `primary_untracked`, `primary_status_disagrees`, `primary_not_pf27_v2` and `primary_check_id_disagrees`.
  - `0fc625d` makes the `primary_untracked` case also remove the primary's two now-empty directories. Without that, the fixture tree held an empty `audit/qa/hde-crd-0002/checks/` directory. The pre-fix writer then refused with `DIRTY_TREE` instead of reaching the ledger, so the case was not a behavioral control.
- **ADR** (`docs/adr/hde/close_pack_writer_adr.md`): item 4 and the QA-ledger stated limit now describe the primary check. The writer reads the header line only and does not judge the rest of a primary. The earlier "does not open the primaries" is removed.

## 5. Hosted CI on `abc0254`

| Run | Head | Result |
| :- | :- | :- |
| 39511628248 | `45e4cef` | failure: changed-tests step, 7 failed, 4,091 passed |
| 39514356279 | `b0a7305` | failure: changed-tests step, 7 failed, 4,102 passed |
| 39518303974 | `abc0254` | failure: changed-tests step, 7 failed, 4,117 passed, 2 skipped (428.32 s); every later lane skipped; final step `APPLICABLE_CI_LANE_NOT_SUCCESSFUL` |

The failed-job log (job 118955686701) was read through its short test summary. The 7 failures are the same tests as in v1.7 §5:
- `tests/evidence/test_v2_mapped_cache_evidence.py::test_write_failure_rolls_back_all_producer_owned_files`: `ValueError`, a `/tmp/pytest-of-runner/…` path "is not in the subpath of" `/home/runner/work/_temp/hde-changed-test-source`.
- `tests/evidence/test_v2_mapped_cache_evidence.py::test_command_fixed_point_check_nonmutation_and_no_repository_residue`: `OSError: [Errno 18] Invalid cross-device link` from `/home/runner/work/_temp/hde-epic038-pr05-*` into `/tmp/pytest-of-runner/…`.
- Five v1 tests in `tests/qa/test_generate_epic_close_pack.py`:
  - `test_complete_candidate_lifecycle_is_committable_exact_and_idempotent`;
  - `test_unrelated_clean_tracked_symlink_preserves_terminal_reachability`;
  - `test_both_staged_outputs_are_verified_before_any_canonical_install`;
  - `test_recovery_cleanup_refuses_git_identity_drift_before_mutation[same_tree_head]`;
  - `test_publication_failure_restores_previous_pair_and_leaves_no_temp_residue`.

  Each differs only at tuple index 5 of the test's `_metadata`, which is `st_atime_ns`. Mode, size, mtime, ctime and inode are equal.

None of the 7 is a v2 test or touches the CX7-9 code.

**Root cause (established; supersedes v1.7 §5's "not known").**

| Fact | Evidence |
| :- | :- |
| The runner image changed | The "Set up job" section was read from each of four complete job logs:<br>- Run 39490424564 (`0d50b06`, the last success; 917 lines): `Image: ubuntu-24.04`, `Version: 20261012.334.1`, runner 2.337.0.<br>- Runs 39511628248 (`45e4cef`), 39514356279 (`b0a7305`) and 39518303974 (`abc0254`), 1,332 to 1,333 lines each: `Image: ubuntu-26.04`, `Version: 20261012.163.1`, runner 2.338.0.<br>All four jobs ran on the label `ubuntu-latest`. The images of the six earlier passing runs were not read |
| On 26.04, `/tmp` and `$RUNNER_TEMP` are different filesystems | `Invalid cross-device link` from `/home/runner/work/_temp/…` into `/tmp/pytest-of-runner/…` |
| A separate `strictatime` tmpfs `/tmp` reproduces all 7 on `main` | Local tmpfs mounted `mode=1777,strictatime,nosuid,nodev`, used as pytest's `--basetemp`. On `origin/main` (`6f53552`), `tests/qa/test_generate_epic_close_pack.py` with `tests/evidence/test_v2_mapped_cache_evidence.py` gave 7 failed, 414 passed, 2 skipped: exactly the 7 hosted failures. On `0fc625d`, 4 of the 5 atime tests fail. `test_both_staged_outputs_are_verified_before_any_canonical_install` passed in that run |
| The writer does not move access times | Probe under the same mount, with metadata (mode, size, mtime, ctime, inode, atime) captured before `--check`, after `--check` and after `--write` on a committed pair: all equal. A following plain `read_bytes()` by the test moved the report's atime |
| The atime moves come from the tests' own reads between their two snapshots | Example: `test_complete_candidate_lifecycle_is_committable_exact_and_idempotent` calls `read_bytes()` after the second `--write` and before its `after` snapshot. Under `strictatime`, every read moves atime. On 24.04, `/tmp` shared a filesystem with `$RUNNER_TEMP`: the cross-device pair passed there. That its mount did not move an atime already later than mtime is inferred from those passes, not read |

Consequences:
- The failure is the base's under the new runner image, not this PR's change.
- Any run of these 7 tests on `ubuntu-latest` fails, whichever head it tests.
- A re-run lands on the same image.

**Observation for PF10's open item on ruby after the move to Ubuntu 26.04** (HDE Build Notes, WU-PR-01 overlay, "Unresolved obligations and owners", owner "PR-35 observation of hosted CI"). `tests/evidence/test_hdapi_v2_contract_inventory.py` needs ruby and is one of this PR's 166 changed-test targets. It did not fail on `ubuntu-26.04` 20261012.163.1 in any of the three runs, whose only failures are the 7 above. Without ruby on `PATH` its ruby-dependent cases fail rather than skip: this harness's own run of the 166 targets showed 9 such failures (v1.7 §6). So ruby was available on that image. The undeclared ruby dependency remains the documentation delta candidate for the Product Owner.

## 6. Local checks

Detached clones, closed rails, CPython 3.12.3, CI's install (as v1.1 §4).

| Check | Result |
| :- | :- |
| Negative control: the new test file against the pre-fix writer (`abc0254`), `-k primar` | 9 failed, 2 passed. The 9 failures are exactly the 9 new tests. The 2 passes are existing tests that match the selection through their parameters. Behavioral: in 4 cases the old writer writes (exit 0) over a primary that is missing, records `FAIL_BEHAVIOR`, carries a v1 header, or names another check. The other 5 fail on the new `_primary_identity` and on the bindings that are not yet rendered |
| `tests/qa/test_generate_epic_close_pack.py` on `0fc625d` | 517 passed, exit 0, 00:13:23 to 00:14:52; tree clean afterwards |
| `prepush_check.py --base abc0254 --head 0fc625d replay` | **PASS**, 00:15:15 to 00:27:23. Lanes `evidence,qa` (3 paths); `ci.yml` the pinned one (sha256 d02021f3…); step 08 changed tests 663 passed; step 13 evidence 134 passed; step 14 qa 488 passed; step 16 SUCCESS; copy clean; repository unchanged. Not CI's result. Here `/tmp` shares the checkout's filesystem, as it did on the 24.04 runner |

## 7. In-flight decisions

| Decision | Why | Tested by |
| :- | :- | :- |
| PO-35-5 implemented as stated (§2) | Product Owner decision | §6 |
| A primary is admitted and captured through the writer's existing causal-input path (`_require_admitted_causal_input`, `_capture_input`) | One input path; no second reader (addendum 2.11 rule 5) | 517 passed; no test aims a ledger entry at an updater output or the close-run family, because the pinned `log_path` shape already excludes both |
| The header comparison covers `check_id` and `status` only | The option's text; the ADR states it as a limit | the four `QA_LEDGER_INVALID` cases |
| `0fc625d` as a separate commit | `ff0de6e` was committed before the negative control showed the `primary_untracked` case was not behavioral | §6 |

## 8. Decision needed: hosted CI cannot pass on `ubuntu-latest`

PO-35-6 offered manual re-runs. A re-run cannot make this head green, because it runs on `ubuntu-26.04`, where `main` itself fails these 7 tests (§5). The skill's `MERGE_PENDING` predicate needs current-head CI to pass, or an actual scoped authorized waiver. The fix lies in `.github/workflows/ci.yml`, which instruction §6 keeps unchanged, so it is not WU-PR-07's to make. The options:

| Option | What it does | Cost |
| :- | :- | :- |
| A. Fix CI on `main`, outside WU-PR-07, then merge `main` into #668 | Pin the `test` job to `runs-on: ubuntu-24.04`, the image of the last run on which all 7 passed. Alternatively, export `TMPDIR="$RUNNER_TEMP/pytest-tmp"` in the changed-tests step. That addresses the cross-device pair as established; for the 5 atime tests it rests on `$RUNNER_TEMP`'s mount options, which are not known | One small change on `main`, by its owner and route; fixes every PR that runs these tests |
| B. Rescope WU-PR-07 to carry the same `ci.yml` change | As A, inside #668 | RS-20 review by the IA; the session ceiling is spent |
| C. A scoped Product Owner CI direction for these 7 tests on #668 | Records an authorized waiver. Under HDE Governance §9.1.4 the failed check stays failed and local validation still applies | `main` stays red for the next PR that runs these tests |

## 9. Spend against the ceiling (instruction ID-1)

- **Sessions:** 4 of 4.
- **Codex rounds:** 7 completed, plus two that failed on the usage limit.
- **Elapsed:** within 3 days, excluding Product Owner waits.

## 10. PR_REMOTE_ACTION_LEDGER (continues v1.7 §9)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 44 | 23:57 | Reply on CX7-8; push `b0a7305..abc0254` | pushed |
| 45 | 00:01 | Codex review 5593304287 on `abc0254` | CX7-9 (P1); CX7-8 answered |
| 46 | ~00:02 | Resolve CX7-8 thread | resolved |
| 47 | ~00:03 | Rule 8 question (CX7-9) | PO-35-5 |
| 48 | 23:57 to 00:05 | Hosted `test` on `abc0254` (run 39518303974, run 3789) | failure (§5) |
| 49 | 00:15 to 00:27 | Local fix and checks (§6) | pass |
| 50 | ~00:20 | Product Owner: "I can rerun CI manually as needed" (PO-35-6) | recorded; §8 |
| 51 | 00:20 to 00:35 | Root-cause checks: four job logs' runner images; `strictatime` reproduction on `main` and on `0fc625d`; writer atime probe | established (§5) |
| 52 | next | Reply on CX7-9; push `ff0de6e`, `0fc625d` and this record. The CX7-9 thread stays open until Codex's next review answers it | — |

## 11. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Hosted CI red on `ubuntu-latest` (§5, §8) | Product Owner | decision needed (A, B or C) |
| Codex review and hosted CI on the new head | PR-35 | after push |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent of #668's merge |
| Drainage named by addenda 2.13 to 2.15 | their owners | unperformed |

Nonclaims: no merge readiness, QA verdict, acceptance, Ops, deployment or closure.
