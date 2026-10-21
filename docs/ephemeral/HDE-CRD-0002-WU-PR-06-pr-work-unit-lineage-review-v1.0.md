---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-06-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: ACCEPT
progression: TERMINAL_PRODUCT_OWNER_RETURN (the next ordered unit, WU-PR-07, cannot start its PR-10 until the Product Owner supplies its business case under PF10 addendum 2.11; §8)
predecessor: none (the first PR-40 review of WU-PR-06)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-06
work_unit_title: "Read-only pre-push and pre-plan check (PR; Distillation; S20)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob f3a6a8855ec0; landed by #658 as 1993d07)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0.md (v1.0; Proceeded; spent; blob 2848847e8bee; landed by #659 as 0442d23) with companion docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0-prototype.diff (blob 04af32e1e3da)
PR_30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED; blob b506bff32c5c)
PR_35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.25.md (MERGE_PENDING; historical pre-merge evidence; blob 38a3a46b3bc6). It supersedes v1.24 (MERGE_PENDING; blob 398e52bd9f05) as the MERGE_PENDING result. Checkpoints v1.1 to v1.23 are part of the same lineage
PR_REFS: amthorn78/glow-hdengine-v2#660 (the only pull request of this work unit; merged as b963ed4)
entry_event: MERGE_OBSERVED for #660, delivered to the subscribed PR-35 session and pasted by Nathan (merged 2026-10-20T11:39:12Z as squash commit b963ed4; this handoff voids the conditional PR-40 block returned with MERGE_PENDING). The merge and the handoff's facts were verified independently (§3, §4)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role; session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (author of the WU-PR-06 instruction; not an author of the plan, code, results or postmortem reviewed here)
pr_sessions: PR-20, PR-30 and the postmortem https://claude.ai/code/session_01NZEtMVb5HR3XYEmJ6W5cb6; PR-35 https://claude.ai/code/session_01SVmct81WDzDqX36ZasAijn
approved_lineage: Specification docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3); Implementation Audit docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0; blob b39ac9f276db); Implementation Plan docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44); Plan review docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE; blob 0cc0276524b2)
overlays: PF10 addenda 2.2, 2.3, 2.4, 2.5, 2.9, 2.10 (the unit's effective baseline, as the instruction applies them); 2.11 (adopted during PR-35 and current on main since the merge; it reserves WU-PR-06's disposition to the Product Owner and gates WU-PR-07's PR-10); none created for this unit
product_owner_decisions_in_lineage: PO-35-1 to PO-35-3 (results v1.7 and v1.8 §2a), PO-35-4 and PO-35-5 (result v1.22 §2a), PO-35-6 (result v1.24 §2a); the canon commit direction of 2026-10-20T10:44:07Z (result v1.25 §2); postmortem decisions D-2 to D-5 (postmortem v1.1 §17). D-1, WU-PR-06's fate, is recorded there as open
postmortem: docs/ephemeral/HDE-CRD-0002-WU-PR-06-postmortem-v1.1.md (v1.1; blob 738bb5232b22; landed by #661), with v1.0 (blob 4510ca5c829c) preserved
return_owner: the same continuing whole-change HDE-CRD-0002 Implementation Agent; for this result's pending decisions, Nathan / Product Owner (§8)
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state as of 2026-10-12T02:29:38.234Z; read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-20T12:19:08Z
repository_state_reviewed: origin/main fc51620c275bd50c38406382b1326e143b2adb61 (tree 273a5d869290), which is b963ed4 (#660; tree eed8783e764c) plus #661 (AGENTS.md rule D-4 and the postmortem). No commit after fc51620 at review time
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.2.md (v13.6.2; blob fa450ba8e99a; 232,936 bytes; sha256 f1a65911ab3d80fe017765698e2ee4360171adac45114855905e20170365f875; landed on main by #660's b0e2299, the Product Owner's file byte for byte). Read in this invocation: the complete v13.6.1 → v13.6.2 diff (the version lines, one index line and addendum 2.11; nothing else changed) and addendum 2.11 in full. Addenda 2.1 to 2.5 and 2.10 were read in full by this session at PR-10 for this unit (instruction front matter) and are byte-unchanged; a search of the whole file for WU-PR-06, S20, pre-push, PR-40 and WU-PR-07 finds items only in 2.2, 2.5, 2.9, 2.10 and 2.11
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§9)
next_prompt: none (terminal Product Owner return; §8)
---

# HDE-CRD-0002 WU-PR-06 — PR work-unit lineage review v1.0 (PR-40, #660)

## 1. Decision

**ACCEPT.** WU-PR-06 is delivered, with sufficient attributable evidence, by its one pull request, #660.
- **The tool.** `tools/ci/prepush_check.py` gives one read-only command with the five reports the instruction requires: `lanes`, `membership`, `build-notes`, `sweep` and `replay`. Each report ran on merged `main` in this review and left the checkout unchanged (§5).
- **Owner test and registration.** `tests/tools/test_prepush_check.py` has 137 cases, and all passed on `main`. The 29-line fail-closed `tools/ci/` registration in `ci/checks/classify_ci_changes.py` landed byte for byte as plan v1.0 §4.4 states.
- **Design change during PR-35.** The landed design is plan v1.0 as changed by the Product Owner's in-flight decision PO-35-4 (IF-35-23):
  - the replay runs only the `ci.yml` with the pinned SHA-256;
  - the install step is a stated precondition, checked for presence only;
  - `lanes` and `membership` run the classifier only in a throwaway copy.
- **Code review.** All 51 Codex findings are disposed and all 51 threads resolved. The one P1 (CX6-15, caller secrets reaching child processes) was fixed under PO-35-3. The three declines rest on Product Owner rulings (PO-35-1, PO-35-5, PO-35-6). The reviews of the final heads `bd2dc3a` and `daa2845` had no findings.
- **CI.** Hosted CI passed on the merged head `daa2845` across all seven lanes, with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. It passed again on `main` for the merge commit `b963ed4` (§4).

**What ACCEPT is not.**
- It is a delivery verdict against the approved scope.
- It is not the Product Owner's disposition of WU-PR-06 under PF10 addendum 2.11. Addendum 2.11 reserves that disposition to him, and postmortem v1.1 §17 records it (D-1) as open. The merge settles only that #660 was not closed unmerged.
- It is not QA, acceptance of HDE-CRD-0002, Ops, deployment, release activation, PF09 or PF30 movement, or closure.
- The tool's green is not CI's green and not QA, and its output is not governed evidence.

**Progression.** Plan v1.1 §7 orders WU-PR-07 next. Addendum 2.11 requires WU-PR-07's business case from the Product Owner before its PR-10. So this result returns to Nathan for that decision (§8) and emits no continuation handoff.

## 2. Inputs read

- **In full, in this invocation:**
  - the PR-40 prompt;
  - plan v1.0 (all sections, "Canon relied on" and "Checks run");
  - results v1.0, v1.22, v1.23, v1.24 and v1.25;
  - postmortem v1.1, which contains v1.0's text unchanged as §1 to §16;
  - PF10 addendum 2.11 and the v13.6.1 → v13.6.2 diff;
  - the `AGENTS.md` change of #661;
  - the landed `tools/ci/prepush_check.py`, all 1,755 lines;
  - the classifier diff of #660, and the owner test's case list.
- **Results v1.1 to v1.21, in full, by a read-only worker of this session.**
  - **What it produced.** A ledger of every record's commits, findings CX6-1 to CX6-45, the decisions PO-35-1 to PO-35-3 quoted verbatim, the in-flight decisions IF-35-1 to IF-35-22, CI runs, validations, open items and inconsistencies.
  - **Its own checks.** It verified every predecessor blob, byte count and sha256 those records cite against the stored files, and every commit SHA, blob, line count and +/− count against git.
  - **This review's spot checks.** I checked its CX6-7 entry against result v1.5 §2. I checked its open items against the later records and against GitHub (§4).
- **Authored by this IA and re-read for the decisions that depend on it:** instruction v1.0 §4, ID-1 to ID-12, §6, §7, §8, §10, §11, §12, §14 and §15.
- **Approved lineage, for the sections this unit binds:**
  - the Specification's S20 row, the constraints "Duplication" and "Uncovered tests", and the Exclusions;
  - Plan v1.1 §5 IF-9 and §7 (the order paragraph, and the WU-PR-06, WU-PR-07, WU-PR-08, WU-DOC-01 and WU-OPS-01 blocks);
  - Audit §6 S20 and §7.1 EC-9, as the instruction quotes them;
  - the IA-30 review v1.1, which has no note for this unit.
- **Remote evidence, each read whole by a programmatic scan where it came back as one long line:**
  - #660's metadata;
  - the 51 review threads (137,983 characters, `hasNextPage: false`);
  - the 75 formal reviews;
  - the two PR comments;
  - the check runs on `daa2845`;
  - job 118587679773's log (73,339 characters, 911 lines; the API's `original_length` 911);
  - the 26 workflow runs on the branch;
  - the `main` runs after the merge.

## 3. Merge state and landed lineage

| Item | Fact |
| :- | :- |
| Pull request | #660, "HDE-CRD-0002 WU-PR-06 (S20): read-only pre-push and pre-plan check (PR-30)". GitHub: `merged: true`, `merged_at` 2026-10-20T11:39:12Z, `merged_by` amthorn78, base `main` `0442d23`, head `claude/youthful-gauss-d9e0ab` `daa2845dc3a36cccd537fb410a575f7e24809b71`, 52 commits, 30 files, +7,050/−3 |
| Merge commit | `b963ed4dfd8d600f6980752b3bc05229ac9b8eb6`, a squash with one parent, `0442d23` (#659), committed by GitHub. Its tree `eed8783e764c` equals the tree of the PR head `daa2845`. So the landed bytes are the reviewed head's bytes |
| Base currency | `b963ed4`'s parent is `0442d23`, the PR's base. No commit landed on `main` between #659 and #660 |
| Code candidate | `7b9e95f` (CX6-50). Every later commit changes only `docs/ephemeral/` or, for `b0e2299`, `docs/pfcanon/`. `git diff 7b9e95f b963ed4` over `tools/`, `ci/`, `tests/`, `.github/`, `pyproject.toml`, `requirements*.txt` and `pytest.ini` is empty |
| Landed code blobs | `tools/ci/prepush_check.py` `4dc098566620` (1,755 lines); `tests/tools/test_prepush_check.py` `8d2c0be36e2e` (1,070 lines); `ci/checks/classify_ci_changes.py` `10a7155f3df2` (2,086 lines; +29, equal to plan v1.0 §4.4's blob) |
| Commits not adopted | `c912b04` (PO-35-4) and `2f9106d` (PO-35-6). Neither object exists in the session's repository or in the scratch clone checked (`git cat-file -e` fails in both) |
| Commit-subject labels | four pushed subjects say "(S21)": `e4cda7d`, `d01599c`, `5280748`, `657c22b`. They now sit in `b963ed4`'s squash message. Result v1.22 §1 corrects them: the requirement is S20. History is not rewritten, and nothing depends on a subject |

**Attribution.**

| Change | Attribution |
| :- | :- |
| `tools/ci/prepush_check.py` (new), `tests/tools/test_prepush_check.py` (new), `ci/checks/classify_ci_changes.py` (+29) | WU-PR-06, by the ordered lineage `d9a0858` (PR-30) → PR-35 corrections → `7b9e95f`, squashed into `b963ed4` |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.0.md` to `v1.25.md` (26 records) | WU-PR-06's records. Merging preserves them and approves nothing |
| `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md` → `v13.6.2.md` (`b0e2299`, rename at 89%, +118/−3) | **Not WU-PR-06 scope.** It is the Product Owner's canon replacement, committed to #660 at his direction (result v1.25 §2) as his file, byte for byte. It is current canon on `main` from the merge |
| `fc51620` (#661, merged 2026-10-20T11:39:30Z): `AGENTS.md` +3 (the real-input review rule, decision D-4) and the postmortem v1.0 and v1.1 | **Later divergence**, not attributable to WU-PR-06's delivery. It changes the code-review rule for later pull requests. It touches none of the unit's paths |

No generated evidence, governed artifact, release member, manifest or workflow changed in #660. `catalog/manifest.json` and `release_id` `77204764…` are unchanged.

## 4. Reviews, checks and corrected-change coverage

| Item | Fact |
| :- | :- |
| Codex reviews | 24 reviews with findings, one per reviewed head, from `d2ed4fc` to `6999f90` (the last one at 09:58:11Z). The bot's summary comment 6267808148 reads `code_review: {commit_sha: daa2845dc3a3…, has_any_findings: null, has_unresolved_findings: null, status: completed}`, "Code Review — Completed 2026-10-20T10:56:01Z — `daa2845`". No review object exists on `bd2dc3a`, `b0e2299` or `daa2845`: the reviews of the final heads had no findings. 51 further `COMMENTED` reviews carry the PR-35 session's thread replies. There is no human review, and no `APPROVED` or `CHANGES_REQUESTED` |
| Codex security review | not part of the chain (PF10 addendum 2.3). The summary's `security_review` is null |
| Review threads | 51, all resolved; 34 outdated. On every thread the first comment is the Codex bot's and the last is the PR-35 session's reply. All 51 are on `tools/ci/prepush_check.py`. Severity: 50 P2 and 1 P1 |
| Finding dispositions | 47 fixed, 1 resolved by the pin (CX6-47), 3 declined as stated limits: CX6-12 (PO-35-1), CX6-49 (under PO-35-5) and CX6-51 (PO-35-6). The P1, CX6-15, was fixed in `78b5172`: an allowlisted child environment and a stated trust boundary (PO-35-3), with no network sandbox. No P1 or security finding was declined. CX6-7 was dispositioned in `d9171d1` by failing closed instead of the change the finding asked for (IF-35-6). That code was removed by `30158af` (PO-35-4), so nothing of it is open (§7) |
| Corrected-change coverage | The last code change, `7b9e95f`, was reviewed at `6999f90` (same code tree), where it drew CX6-51, declined under PO-35-6. It was then re-reviewed clean at `bd2dc3a` and `daa2845`. The PF10 commit is Markdown under a CI-exempt prefix, outside code-review scope under `AGENTS.md` |
| Hosted CI on the merged head | Run 39410766706, job 118587679773, `success`, 10:50:36Z to 11:11:55Z.<br>**Set-up:** runner image `ubuntu-24.04` 20261012.334.1; Python 3.12.15; checkout `ref: daa2845dc3a3…`.<br>**Classifier:** `BASE_SHA 0442d23`, `HEAD_SHA daa2845`, `reason=selected_lanes;paths=31`, all seven lanes; `AGENTS_MD_CITATIONS_OK`; `[env-pins] OK`.<br>**Results:** changed tests 4,023 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db `DIRECT_DB_CONTRACT_OK`, 269 passed; rails 120, 113, `RAILS_GATE_EVIDENCE_OK` 155, `RAILS_JOB_DEFINITIONS_OK` 138; evidence 130; qa 488; release 79 passed, with the attestation built and verified.<br>**Final audit:** every outcome `success`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| CI history on the branch | 26 runs, run numbers 3750 to 3775: 25 `success` and 1 `failure`. The failure is run 39345008218 on `7a3b7b2`, in `tests/qa/test_generate_epic_close_pack.py::test_manifest_reader_rejects_new_report_with_old_manifest`. That test is outside the change set; PR comment 6280395750 records it; it did not recur on the 13 later heads. Run 39282295924 on `b7bc20b`, whose conclusion no record states, is `success` by the API |
| `main` after the merge | Push run 39416482387 (run 3778), job 118606644602, on `b963ed4`: `success`, 11:39:15Z to 12:00:42Z. Its log was read whole (73,295 characters, 911 lines; `original_length` 911).<br>**Set-up:** image `ubuntu-24.04` 20261018.339.1; checkout `ref: b963ed4dfd8d…`.<br>**Classifier:** `CI_CHANGE_CLASSIFICATION:event=push;reason=selected_lanes;paths=31;lanes=product,compat,db,rails,evidence,qa,release`.<br>**Results:** changed tests 4,023; product 77; compat 119/3/2; db `DIRECT_DB_CONTRACT_OK`, 269; rails 120, 113, `RAILS_GATE_EVIDENCE_OK` 155, `RAILS_JOB_DEFINITIONS_OK` 138; evidence 130; qa 488; release 79 with the attestation; every step `success`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.<br>The push run on `fc51620` (#661, run 39416516689) concluded `success` in 11 s. It is not this unit's |
| Mergeability | `clean` on `bd2dc3a` (result v1.25 §3), with base `0442d23` current. GitHub merged the PR with no intervening base change |
| Waivers | none exists or was used. No `[skip ci]`, re-run or cancellation (results v1.1 to v1.25 ledgers) |

## 5. This review's independent checks on merged `main` (`fc51620`)

**Environment.**
- **Copies.** Two fresh scratch clones of the session's checkout (`--no-hardlinks`), detached at `fc51620`. `m2` held the short reports and tests; `m` held the replay. The session's own checkout was only read.
- **Interpreter.** A CPython 3.12.3 venv with CI's install; pytest 8.4.2.
- **Tools.** `ruby` 3.3.6, `bash`, `curl`, git 2.43.0.
- **Rails.** Closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`). The vendor, database and GitHub keys and `ENGINE_ENV` were unset.
- **Exit codes** were captured from the producer's own status.
- **State digest.** A scratch digest per clone: `HEAD`, `git status --porcelain=v1 -z --untracked-files=all --ignored`, and every file under `.git` by `lstat` identity, by content outside `objects/`, and every directory by name.

| # | Check | Result |
| -: | :- | :- |
| 1 | `--help` | exit 0 (0.1 s) |
| 2 | `lanes --base 0442d23… --head b963ed4…` | exit 0 (8.4 s). `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=31;lanes=product,compat,db,rails,evidence,qa,release`, 166 targets, "classified in a throwaway copy at b963ed4…". The classifier CLI run directly on the same refs gives the same line; its eleven `--github-output` records and 166 targets are identical (`diff` empty) |
| 3 | `lanes --path tools/ci/prepush_check.py --path docs/ephemeral/example.md` | exit 0 (5.6 s); `reason=selected_lanes;paths=2;lanes=product`; one target |
| 4 | `lanes --path tools/ci/prepush_check.py --path ci/checks/unregistered_example.py` | exit 1 (5.8 s); `FAILURE CI_CHANGE_CLASSIFIER_ERROR:CI_CHANGE_SURFACE_UNCLASSIFIED:ci/checks/unregistered_example.py` |
| 5 | `membership --path engine/core/core.py --path tools/ci/prepush_check.py` | exit 0 (6.2 s). `admitted release version=1.3.0 roster=45 release_id=77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e head=fc51620… (read in a throwaway copy)`. `member engine/core/core.py`, `not-member tools/ci/prepush_check.py`, and the information-only refresh note |
| 6 | `build-notes` | exit 0 (1.0 s); `path=docs/pfcanon/PF10-HDE-Build-Notes-v13.6.2.md bytes=232936 sha256=f1a65911…f875`. The pattern resolution found the renamed file with no change to the tool (instruction ID-6) |
| 7 | `sweep` at the head | exit 0 (6.4 s); `tracked_test_files=215 pytest_command_tokens=39 workflow_tests_tokens=39 full_validation_targets=166 uncovered=0` |
| 8 | `sweep --head a429c7c --no-run` | exit 1 (6.7 s); `tracked_test_files=278 … full_validation_targets=94 uncovered=135`; "run: not executed (--no-run)". The 135 paths equal the WU-PR-01 list file for file (`diff` empty apart from the reference file's header line) |
| 9 | State of `m2` around items 1 to 8 | identical before and after: `head=fc51620…`, status empty, git metadata digest `f09a9e2e…25c7`. Every report printed "repository unchanged (tree, ignored files, directories, HEAD and git metadata)" and the nonclaim line |
| 10 | Owner test (`PYTHONPATH` the clone, `-p no:cacheprovider`) | **137 passed in 130.7 s**, exit 0 |
| 11 | Pin files and neighbours, one at a time | `test_rails_ci_workflow_integration.py` 138, `test_http_reader_ci_ownership.py` 4, `test_architecture_snapshot.py` 5, `test_epic020_bundle_tool.py` 6, `test_check_agents_md_citations.py` 57 passed; each exit 0 |
| 12 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC`, exit 0 |
| 13 | State of `m2` after items 10 to 12 | changed: an ignored `.pytest_cache/` appeared and the git metadata digest moved. These were this review's own `pytest` runs in the checkout, not the tool's. It is the hazard the tool avoids by running tests only in copies (instruction §5.7) |
| 14 | `replay --full` from `m`, 11:50:10Z to 12:14:58Z | **Exit 0.**<ul><li>**Inputs:** `event=pull_request base=fc51620… head=fc51620… (full validation)`; interpreter 3.12.3, `workflow_python=3.12`.</li><li>**Pin:** `workflow .github/workflows/ci.yml sha256=d02021f3… (the modelled one)`.</li><li>**Environment:** job env `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `resolves hdctl (<venv>/bin/hdctl) -> engine.cli.main: <copy>/engine/cli/main.py`.</li><li>**Steps:** all 16 `SUCCESS`; steps 1, 4 and 5 excluded and substituted, the install step by the presence check.</li><li>**Lanes:** changed tests 4,023 passed (all 166 full-validation targets); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, with the attestation built and verified from the replay's `RUNNER_TEMP`.</li><li>**Final audit:** `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.</li><li>**Time:** step time 1,476.0 s.</li><li>**Read-only result:** "copy after replay: clean"; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`.</li><li>**Scratch check of `m`:** identical before and after (`head=fc51620…`, status empty, digest `edd8150e…ee0a`); no temporary directory left.</li><li>**Comparison:** every lane count equals hosted CI on `daa2845` and on `b963ed4` (§4).</li></ul> |

## 6. Requirement coverage across the work unit

| Requirement or obligation | Delivered by | Evidence | State |
| :- | :- | :- | :- |
| S20 "one read-only command" (Plan acceptance (1) and (3); IF-9 "writes only under a temporary directory; asserts a clean tree before and after"; ID-2, ID-3) | `main`, `repository_state`, `make_copy`, the one temporary directory chosen before creation (refused inside the repository) | `test_reports_on_a_clone_of_the_repository_are_read_only`, `test_repository_state_covers_ignored_files`, the dirty-tree and temp-inside cases; §5 items 9 and 14 | met |
| `lanes` equals the classifier, both modes, refusals included (ID-4) | `_lanes_for_refs` runs the head's classifier CLI in a copy; `classify_given_paths` runs its functions in a child inside a copy | `test_lanes_equals_the_classifier_for_refs_and_for_given_paths`; §5 items 2 to 4 | met |
| `membership` matches `ADMITTED_RELEASE_ROSTER` (ID-5) | `admitted_release` by AST in the copy; paths normalized by the classifier's `_normalized_path` | owner test's 45-path case; §5 item 5 | met |
| `build-notes` resolves exactly one PF10 and prints its SHA-256 (ID-6) | `report_build_notes` by pattern from `HEAD`'s tree | the zero, one and two-file cases; §5 item 6 (v13.6.2 after the rename) | met |
| `sweep`: the binding coverage definition; 135 at `a429c7c`, 0 at the head; a non-empty set fails; run in a throwaway copy (ID-7; G-2; addendum 2.2's `ruby`) | `compute_coverage` in a child against the copy's own classifier; the tool preflight (CX6-17) | `test_coverage_matches_the_binding_definition_and_the_guard_on_the_repository`, the synthetic sweep case; §5 items 7 and 8 | met |
| `replay`: every step of the `test` job executed or excluded with a reason; the pin; the interpreter rule; resolution of `hdctl` (ID-8; G-3; OBS-W5-5) | `REPLAY_INVENTORY`, `REPLAY_WORKFLOW_SHA256` (`d02021f3…`), `replay_steps`, the substitutes, `_resolution` | `test_replay_inventory_pins_every_step_of_the_ci_test_job` (with the SHA pin), the synthetic replays, the interpreter case; §5 item 14 | met, with G-3 widened by IF-35-23 (§7 LR6-O5) |
| Closed rails, no network, keys-only output (ID-9; C2) | `child_environment`: only `HOME`, `LOGNAME`, `PATH`, `SHELL`, `TERM`, `USER` inherited; closed rails set; no `pip`, `fetch` or network import | `test_child_environment_is_closed_rails_without_keys`, `test_tool_installs_no_hook_fetches_nothing_and_opens_no_network`; CX6-15's fix | met; children are not sandboxed (stated limit, PO-35-3) |
| Registration and owner test (ID-10; G-4) | `_CI_TOOL_PREFIX`, `_CI_TOOL_LANES`, `_CI_TOOL_TEST_OWNERS`, `_ci_tool_owner_targets` | blob equal to plan §4.4; owner test a full-validation target; 137 passed (§5 item 10); hosted CI ran it | met |
| Carried classifier gaps (ID-11) | not fixed; surfaced: `lanes` shows the classifier's selection, `replay --full` runs every full-validation target | §5 item 14 | carried to the Product Owner (§7) |
| In-flight corrections outside the change set (ID-12) | none: no path outside plan §6.1 changed | §3 attribution | met |
| Plan acceptance (4) "Lanes green (full validation, classifier changed)" | hosted CI on the merged head | §4 | met |
| Evidence obligation "PR result record with one captured run" | result v1.0 §6 at `d9a0858`; re-runs of each report at `30158af` and `7b9e95f` (results v1.22 §5 and v1.23 §5); this review's runs on `main` | §5 | met (LR6-O9) |
| Exclusions: no hook, no SessionStart hook, no `.claude/` change, no new dependency, no workflow change, no release or evidence change, no `README.md`/`AGENTS.md`/`CHANGELOG.md` edit | §3 attribution: #660 changes none of these paths | `git diff --name-status 0442d23 b963ed4` | met |
| Security (instruction §11) | read-only by construction; allowlisted children; argument vectors; paths validated by the classifier | §4 dispositions; §5 | met |
| Documentation obligation | none in this unit; the usage note is WU-DOC-01's (G-1) | — | carried (LR6-O7) |
| Migration and rollback | none; rollback is Nathan's revert of `b963ed4` | — | as instruction §11 |

## 7. Findings

No defect is open against the approved scope. The observations below have owners. None reopens the delivered state.

| ID | Observation | Owner and route |
| :- | :- | :- |
| LR6-O1 | **WU-PR-06's disposition (postmortem D-1) is open.** Addendum 2.11 states: "Its disposition is the Product Owner's decision and is not made by this addendum". It names options A (merge and attach a measure), B (close #660 unmerged and remove S20 through a Specification delta) and C (strip the replay). The merge rules out closing #660 unmerged and C. Two things remain undecided:<ul><li>whether A's measure applies: "each later unit's PR-40 records any hosted CI failure a local replay would have caught; if none is recorded by HDE-CRD-0002's QA-10 the replay is removed in a later change";</li><li>whether S20 is removed by a later Specification delta.</li></ul>No record states that decision (repository and Notion searched). This review does not apply the measure, and it does not decide | Product Owner (§8) |
| LR6-O2 | **Addendum 2.11's rule cross-references are misnumbered, now on `main`.** Postmortem v1.1 §18 lists eleven references that use the postmortem's R-numbers. Example: rule 7's "on a real input (rule 3)" points at the gates rule, not rule 4's definition of a real input. The landed file is the Product Owner's upload byte for byte, uncorrected. This review reads each reference by the rule its text describes. No decision here depends on the numbering | Product Owner (PF10 is his to correct; §8) |
| LR6-O3 | **No business case, ceiling or measure exists for WU-PR-06**: none was set (NOT PRODUCED). Addendum 2.11's deferred obligation would have PR-40 record "the unit's actual cost against its ceiling and whether its measure was met"; it is unperformed (GCFPE Modification Backlog MB-019). The actual cost, for the record:<ul><li>26 completed Codex reviews, 24 of them with findings;</li><li>51 findings (50 P2, 1 P1);</li><li>26 hosted CI runs (25 success, 1 failure), 494.3 minutes of run wall time;</li><li>52 commits; 26 result records;</li><li>PR open to merge 22.65 h;</li><li>three sessions (PR-20/PR-30, PR-35, this PR-40) plus the postmortem;</li><li>tool 1,229 → 2,132 (peak) → 1,755 lines; owner test 552 → 1,229 → 1,070 lines, 21 → 141 → 137 cases</li></ul> | Product Owner (the measure, under LR6-O1); GCFPE-MGMT-10 (MB-019) |
| LR6-O4 | **Hardening that the pin makes unreachable stays in the tool.** The YAML-subset and expression rules added for class B findings (IF-35-15 to IF-35-22) now read only the pinned file. The pin refuses every other `ci.yml` before parsing (`report_replay`). They show no wrong result on a real input, and addendum 2.11 rule 6's "pins the exact input it supports and refuses any other" is met by the pin. Removing them would be a simplification, not a fix. Also outstanding: result v1.24 §9's design candidate, shared lane scripts that both `ci.yml` and the tool call | Product Owner, as later-change candidates |
| LR6-O5 | **Contract G-3 is wider than the instruction stated.** Any change to `ci.yml`, not only a step added, renamed or removed, now fails the owner test, and the replay refuses until the PR updates `REPLAY_WORKFLOW_SHA256` (IF-35-23 (a), PO-35-4). Hosted CI is unaffected. No planned unit edits `ci.yml` | any later pull request that edits `ci.yml`; WU-DOC-01's usage note (G-1) |
| LR6-O6 | **The owner test takes about 130 s, against plan §5.10's 25 to 32 s for the PR-30 test.** Each `lanes` and `membership` run copies the head (IF-35-23 (c)). CI runs it only as a changed-test target or a full-validation target | recorded; no gate |
| LR6-O7 | **Stated limits for the usage note (G-1):**<ul><li>the replay runs only the pinned `ci.yml`;</li><li>the install step is checked for presence only;</li><li>runner defaults are not given to scripts a step calls (CX6-12, CX6-49);</li><li>directories under `.git` are compared by name (CX6-51);</li><li>concurrent git activity in the checkout fails the read-only check (IF-35-24);</li><li>children are not sandboxed (CX6-15, PO-35-3);</li><li>a shallow source makes copies hold ref-reachable history only (F-3);</li><li>the environment prerequisites: CI's install, Python 3.12, `ruby`, `bash`, `curl`</li></ul> | WU-DOC-01 |
| LR6-O8 | **OBS-17 recurred once on this PR**: the intermittent `test_manifest_reader_rejects_new_report_with_old_manifest` failure on `7a3b7b2`, mechanism not established. It did not recur on any later head, and the qa lane and the replay passed (§4, §5) | QA tool and test owner, through this IA; Product Owner to route (unchanged) |
| LR6-O9 | **The final code's re-runs lacked two captured runs**: results v1.22 and v1.23 re-ran each report at `30158af` and `7b9e95f` but recorded neither a `replay --full` nor a refused-path `lanes` run. This review ran both on merged `main` (§5 items 4 and 14), so the obligation is met on the landed code | none |
| LR6-O10 | **Record consistency.** The worker's ledger found these inconsistencies in results v1.1 to v1.21. None changes the delivered state:<ul><li>the "(S21)" subjects, corrected in v1.22;</li><li>a wider paraphrase of PO-35-2 in v1.7 §1 than its question; PO-35-5 replaced PO-35-2;</li><li>v1.6 ruling out running the build backend and v1.12 then running it; that code was removed by `30158af`;</li><li>CX6-7's "dispositioned" status dropped from later cumulative rows; its fail-closed code was removed by `30158af`;</li><li>the reuse of the ID IF-35-7 across v1.5 and v1.6;</li><li>one thread reply's step count, corrected in v1.14;</li><li>`created_at` values a minute or more after their pushes in v1.14 to v1.19;</li><li>v1.12's sweep run without the scratch `XDG_STATE_HOME` and `PYTHONPATH`, self-reported and repeated in v1.13</li></ul> | none (history preserved) |
| LR6-O11 | **O-6 stands.** The hosted `ruby` version is still unprinted; the image was `ubuntu-24.04` 20261012.334.1 at `daa2845`. Addendum 2.2's note on Ubuntu 26.04 stands | as addendum 2.2 |

**Carried items from instruction §15, with their state after this unit:**
- **Applied in the tool:** F-5 (the classifier applies WU-PR-05's registration, and `lanes` reports it); C-3 and LR O-1 (the binding definition with the token-set pin); C-4 (the inventory, now also the SHA pin); C-6 (the registration shape).
- **Carried to the Product Owner as later classifier change candidates:** OBS-P4-1 and OBS-P3-5. They are surfaced and not fixed; `replay --full` runs the tests they leave out.
- **O-14:** does not reproduce; nothing owed.
- **Handled:** the `ruby` requirement (tooling failure if missing); OBS-W5-5 (the replay puts the copy first on `PYTHONPATH` and prints where `hdctl` resolves); OBS-W5-3 and S19-R04 (the replay runs only `ci.yml` text, in a copy); OBS-P4-2 and OBS-P4-7 (children get `APP_ENV=dev` and no `ENGINE_ENV`); OBS-4 and OBS-14 (tests run only in copies).
- **Unchanged:** `release_id` `77204764…` with 45 members; AQ-1 (WU-PR-07 only); the other items of instruction §15, with their owners.

## 8. Next approved Plan stage: Product Owner return

- **The next ordered unit.** Implementation Plan v1.1 §7: "Order of landing on `main`: WU-PR-01 → … → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 → QA-10 readiness". WU-PR-07's block: "Dependencies and order. Seventh; after WU-PR-02 (updater model)". WU-PR-02 is accepted (addendum 2.5), and no `HDE-CRD-0002-WU-PR-07-*` file exists on `main`.
- **Why it cannot start.** Addendum 2.11 is current canon on `main`, and its rules "apply immediately to the remaining HDE-CRD-0002 units".
  - It requires that WU-PR-07 "needs a rule 1 business case before its PR-10, weighed against cheaper options such as a canon change to the close-report requirement or keeping exceptional closure".
  - It assigns "the business-case and real-input work for WU-PR-07 and WU-PR-08 before their PR-10" to the Product Owner.
  - Its gates rule: "PR-10 carries both [business case and ceiling] into the instruction".
  - No WU-PR-07 business case exists: the repository's `docs/ephemeral/` and `docs/prompt_ecosystem_management/` were searched, and Notion was searched.
  - So PR-10 for WU-PR-07 cannot run.
  - PR-40 says: "If the next ordered unit's dependencies are unmet …, preserve the existing ACCEPT and return the exact pending decision to its owner. Do not select a convenient later unit or invent an order." WU-PR-08 follows WU-PR-07 and has its own 2.11 prerequisite; WU-DOC-01 and WU-OPS-01 follow WU-PR-08.
- **This result is therefore terminal** for this invocation, with no continuation handoff.

**Decisions returned to Nathan / Product Owner:**
1. **WU-PR-07's business case**, under addendum 2.11 rule 1: beneficiary, evidence, benefit, measure, and cost ceiling in sessions and elapsed days. Alternatively, one of the cheaper options 2.11 names:
   - a canon change to the close-report requirement;
   - keeping exceptional closure.

   Either alternative changes S21's scope and so goes through its native owner (a Specification delta for S21). AQ-1 (the S21 ADR) stays as Plan v1.1 §13 states, decided before WU-PR-07 merges.
2. **The rest of D-1 (LR6-O1):**
   - whether option A's measure applies to the remaining units' PR-40 reviews, with its stop date at QA-10;
   - or whether S20 is to be removed by a Specification delta.
3. **Addendum 2.11's cross-references (LR6-O2):** whether to issue a corrected PF10.
4. **Already recorded by 2.11, before WU-PR-08's PR-10:** the S01 real-input fact (the Railway build command and deploy trigger).
5. **Merge this review's pull request.** It carries this record only.

**Resume point.** When the Product Owner supplies WU-PR-07's business case, the next stage is WU-PR-07 through PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), by this whole-change Implementation Agent, with this review and the business case as inputs. If he decides another route, that route applies.

## 9. CANON_CONFLICT_REGISTER

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

**No new conflict.**
- **Addendum 2.11.** It governs over earlier canon for its scope by its own terms ("Where this addendum conflicts with earlier PF-Canon or with an in-flight change document, this addendum governs"), so no entry is needed.
- **WU-PR-06 itself.** 2.11 applies to "units of in-flight changes not yet at PR-10". WU-PR-06 was past PR-10, so 2.11 reserves its disposition to the Product Owner and does not invalidate the approved base.
- **PO-35-4.** The Product Owner ruled it an in-flight design decision and not a rescope (instruction §9.1 and §14). The approved base is unchanged.
- **LR6-O2** is an internal numbering error in one PF10 addendum, with its meaning recoverable from each rule's text. It is not a conflict between sources, and drainage stays with the Product Owner.

## 10. NOT PRODUCED, NOT EXECUTED and pending values

- **NOT PRODUCED:**
  - a business case, ceiling or measure for WU-PR-06 or WU-PR-07;
  - the Product Owner's D-1 disposition record;
  - a PF10 addendum by this review;
  - any QA, Ops, acceptance or closure artifact;
  - a continuation handoff (terminal result).
- **NOT EXECUTED by this review:**
  - the attribution-lock collector;
  - a full `tests/` sweep: the replay's full validation and hosted CI cover the lanes;
  - the 70 negative controls;
  - any live vendor, production or database call.
- **Pending:**
  - the Product Owner decisions of §8;
  - the merge of this review's pull request;
  - persistence of prompt-use provenance (§12).

## 11. TypeSafe reading and surface advice

**TypeSafe: not read.** This result is a terminal return to the Product Owner. There is no receiving session whose work could be scored, and the next runnable stage depends on his decision (§8). A reading belongs to the record that hands off WU-PR-07's PR-10 once that stage is runnable.

**Surface advice:** none for a receiving session. For the record:
- Re-running this review's checks needs Python 3.12 with CI's install, `ruby`, `bash`, `curl`, closed rails with the keys unset, and throwaway clones.
- On four CPUs here, the owner test took about 2 minutes and a `replay --full` about 25 minutes (§5).

**Session and model.** Nathan has not stated the model and setting for this session; none is recorded.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-06 / PR-40 / lineage review 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-06 (S20) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state as of 2026-10-12T02:29:38.234Z) |
| role/stage | continuing whole-change IA, read-only PR-40 role |
| capture time | 2026-10-20T12:19:08Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | instruction v1.0 (§20); plan v1.0 (§20); results v1.0 (§16) and v1.24 (§10) |
| pull request | amthorn78/glow-hdengine-v2#660 (`b963ed4`) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); recorded here only |

## Canon relied on

Read on `main` at `fc51620`. `docs/pfcanon/` was last changed by `b963ed4` (#660's PF10 replacement), and every other PF file is unchanged since 2026-10-09.

| Decision topic | Sources and sections |
| :- | :- |
| Review authority, entry and result | PR-40 — Review PR Work-Unit Lineage — 100926.1, read in full: "Product Owner merge action" (entry on `MERGE_OBSERVED`), "Read-only review boundary", "Execute", "Required result", "Resolve the next approved Plan stage" (unmet next-unit dependency: preserve ACCEPT, return the pending decision to its owner), "Terminal operator return and receiver compatibility", "Accepted-final lineage protection". HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (Proceed per detailed PR plan; merges are Product Owner actions) and §9.1.2 (canon on `main`; in-flight documents govern within their scope) |
| Business case, real inputs, finding disposition, WU-PR-06's disposition, the WU-PR-07 gate | PF10-HDE-Build-Notes v13.6.2 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.6.2.md`), addendum 2.11, in full: rules 1 to 8, "Scope and supersession", "Epic, task, and status effects", "Deferred obligations and unresolved work". HDE Governance §9.7.7 "Business Case section required (Epic Specifications)" (the Epic-only rule 2.11 extends; searched) |
| Review chain and code-review scope | addendum 2.3 (Rules 1 to 5: the Codex code review read and resolved; no Codex security review); `AGENTS.md` "Code review guidelines" (with the real-input rule D-4 added by #661, which governs later reviews) and "Code review scope" (Markdown and CI-exempt prefixes) |
| Non-mutation, rails and failure classes | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 "Tooling vs behavior failures", §2.2.6 "Rails posture in CI (default CLOSED)", §2.2.11 ("A non-writing check MUST NOT mutate the repository or external state"), as instruction §4.1 C1 to C3 map them |
| CI scope and tooling | Change Process Guide (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md`) §0.2; Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "CI lane classification and automated budget-control discipline" and "Repository loci and file minting" (non-governed tooling output) |
| Carried items and overlays | addenda 2.2 ("Affected surfaces": the coverage definition contracted to WU-PR-06 and the `ruby` requirement), 2.4, 2.5, 2.9 (OBS-P4-1), 2.10 ("Carried into the WU-PR-06 instruction") |
| In-flight documents | Specification v1.1 (S20, constraints "Duplication" and "Uncovered tests", Exclusions); Plan v1.1 §5 IF-9, §7 (order and the WU-PR-06 to WU-OPS-01 blocks), §13 AQ-1; review v1.1; Audit §6 S20, §7.1 EC-9; instruction v1.0; plan v1.0 and its companion diff; results v1.0 to v1.25 with PO-35-1 to PO-35-6; postmortem v1.1 (§13, §14, §17, §18) |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Evidence attribution, currentness and distinct decisions"; "PR descriptions"; "Truncation/retrieval-failure guardrail" (the job log and thread listing read whole; exit codes from the producer's own status) |

Silence: canon defines no lineage-review predicate beyond the PR-40 prompt and HDE Governance §9.1, and no rule on pre-push tools or git hooks beyond the Specification's Exclusions. Canon states no business-case content for WU-PR-07 (searched: `docs/pfcanon/` for "business case", "WU-PR-07", "real input"); addendum 2.11 assigns it to the Product Owner.
