---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v2.0.md
artifact_version: "2.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 2, the corrective re-plan after PR-40 REJECT (PR-20 "Re-plan entry", reject_replan)
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1; blob dbb9a56a91dc; the plan of cycle 1, Proceeded once, landed as amthorn78/glow-hdengine-v2#627, squash 7136040). v1.1 and v1.0 are preserved unchanged. This v2.0 does not restate v1.1's scope; that scope is landed history
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
work_unit_title: CI coverage of every test file (PR; Distillation; S03, S04, S05)
PR_WORK_UNIT_LINEAGE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v1.0.md (PR-40, decision REJECT; finding LR-1; bounded correction §10; blob 2cfbb5ec33d8; 38,138 bytes; landed on main at dc701f2, amthorn78/glow-hdengine-v2#628)
PO_DISPOSITION_REF: docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md (CR-4 APPROVED, CR-5 APPROVED_AS_CHANGED; blob f24c4965ed88; landed with #628)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 24597a31fbb9; unchanged)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE) — lineage only
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0.md (RS-20, APPROVE; blob eccab2187769) — decided; nothing in this plan reopens it
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10)
applicable_pf10_overlays: PF10 addendum 2.2 (WU-PR-01 rescope; approved by RESCOPE_REVIEW_ID); PF10 addendum 2.3 (Codex security review deprecated) for the reviewer chain
effective_baseline: approved base + applicable PF10 overlays = the base above + PF10 addendum 2.2, with the reviewer chain read under PF10 addendum 2.3
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md (v13.5.4, effective 2026.10.13; blob f31b4e04adfd; 33,384 bytes; sha256 7e285dffb1dd7ab40fa685c8412c63e8784a43a1f38c1adace6816a23bbca881; read in full; one unlettered document; addenda 2.1, 2.2, 2.3)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md § 2.2 (record docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md); docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md § 2.3 (record docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md); § 2.1 governs §20 only
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (the new dedicated WU-PR-01 PR engineering session for plan cycle 2, created by Nathan / Product Owner)
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); authoring session https://claude.ai/code/session_012kGFYdD1BYJnXh3TagQetg
author: dedicated HDE-CRD-0002 WU-PR-01 PR engineering session (PR-20, plan cycle 2)
return_owner: the continuing whole-change HDE-CRD-0002 Implementation Agent (PR-40 after the corrective merge)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1 (as recorded by the lineage review, register read 2026-10-13)
created_at: 2026-10-13T13:11:01Z
repository_baseline: origin/main dc701f23c44f1537f7296d3a63cb2bbc5104462a (tree 88db3d09cb8b; #628). git diff 7136040..dc701f2 outside docs/ephemeral/ is empty, so every code fact the lineage review measured at 7136040 holds here
canon_conflict_register: CR-1, CR-2, CR-3 carried (APPROVED_AS_CHANGED); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED by the Product Owner (PO_DISPOSITION_REF); no new entry (§16)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-01 — Detailed PR Implementation Plan v2.0 (corrective, plan cycle 2)

## 1. State and authority

**AWAITING_PO_PROCEED.** Held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.7.7).

This is the complete, executable corrective plan for WU-PR-01. It plans exactly the bounded correction of lineage review v1.0 §10, and nothing else:
1. add the monkeypatched synthetic inactive-refusal test case that plan v1.1 §5.4, §5.5 and §8 committed to and that never landed (LR-1);
2. write a new PR result record that states the actual facts behind LR-2 and LR-3.

The test case was prototyped on `main` `dc701f2` and verified, with a negative control (§4.3).

Authority:
- The earlier Proceed (for plan v1.1) is spent. It is not reused, and #627 is landed history: it is never resumed, reused or pushed to (PR-20 "Re-plan entry").
- Only Nathan's `PR Implementation Proceed` (PR-30) for exactly `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v2.0.md` (v2.0) authorizes implementation. Only Nathan merges.
- This plan authorizes no implementation, merge, publication, Ops, QA, acceptance or closure. It changes no canon and creates no PF10 addendum.

## 2. Identity and lineage

| Field | Value |
| :- | :- |
| `CHANGE_CLASS` / `CHANGE_ID` | `CRD` / `HDE-CRD-0002` |
| `WORK_UNIT_ID` | `WU-PR-01`: CI coverage of every test file; Distillation; S03, S04, S05 |
| Entry | PR-40 `PR_WORK_UNIT_LINEAGE_REVIEW` v1.0, decision `REJECT`, finding LR-1, bounded correction §10 |
| `PR_INSTRUCTION_ID` | instruction v1.0, unchanged. Its §6 bounds and §7 exclusions govern, as extended by addendum 2.2 |
| `IMPLEMENTATION_PLAN_ID` / `PLAN_REVIEW_ID` | Plan v1.1 + review v1.1 (Isis, IA-30 `INITIAL_APPROVE`) |
| `SPECIFICATION_ID` | Specification v1.1 approved (Thoth, CF-C-30 `INITIAL_APPROVE`) |
| Overlays | addendum 2.2 (WU-PR-01 rescope); addendum 2.3 (reviewer chain without the Codex security review) |
| Plan cycle 1 | plan v1.0 (suspended at RS-20) → RS-20 review v1.0 `APPROVE` → plan v1.1 → Proceed → PR-30 result v1.0 → PR-35 results v1.1 to v1.15 → #627 merged (squash `7136040`) → PR-40 lineage review v1.0 `REJECT` → PO disposition of CR-4 and CR-5 |
| Plan cycle 2 | this plan v2.0 → Proceed → PR-30 result v2.0 → PR-35 → merge → PR-40 |
| Dependency state | ready. The lineage review and the disposition are on `main` (#628). No WU-PR-01 corrective branch, open PR or v2 record exists (§4.1) |

## 3. Sources read

**Read in full by this session:**
- the lineage review v1.0 and the PO disposition v1.0;
- instruction v1.0;
- plan v1.1;
- result v1.0 (PR-30) and result v1.15 (PR-35 final record);
- RS-20 review v1.0;
- PF10 v13.5.4 (Front Matter, Precedence §1 to §9, Template, Addendum Index, addenda 2.1, 2.2, 2.3);
- PR-20 — Create Detailed PR Implementation Plan — 100926.1 (Notion).

**Read in the sections cited:**
- Specification v1.1: Requirements rows S03, S04, S05; Exclusions; Constraints ("Uncovered tests");
- Implementation Plan v1.1: §7 common paragraph and WU-PR-01;
- result v1.5 §2 and result v1.9 §4 (the statements LR-3 corrects);
- the #627 description (GitHub API read; the statements LR-2 and LR-3 (a) concern).

**Not re-read; carried from the lineage review:** results v1.1 to v1.14 outside the sections above, the Implementation Audit and the Plan review. No decision here rests on them.

## 4. Repository baseline (verified at `dc701f2`)

### 4.1 Observed Evidence Snapshot (CA vetted)

| Command | Output |
| :- | :- |
| `git log --oneline -1 origin/main` | `dc701f2 docs(ephemeral): HDE-CRD-0002 WU-PR-01 PR work-unit lineage review v1.0 (PR-40, REJECT) and PO disposition of CR-4/CR-5 (#628)` |
| `git diff --stat 7136040 dc701f2 -- . ':!docs/ephemeral'` | empty |
| `grep -n -E '_FULL_VALIDATION_INACTIVE_TESTS\|CI_INACTIVE_TEST_REQUIRES_DISPOSITION' ci/checks/classify_ci_changes.py` | `152:_FULL_VALIDATION_INACTIVE_TESTS: set[str] = set()`; `1086: if target not in _FULL_VALIDATION_INACTIVE_TESTS`; `1532: if path in _FULL_VALIDATION_INACTIVE_TESTS:`; `1533: raise ValueError(f"CI_INACTIVE_TEST_REQUIRES_DISPOSITION:{path}")` |
| same pattern over `tests/evidence/test_rails_ci_workflow_integration.py` (2,118 lines) | `1109: inactive = classifier._FULL_VALIDATION_INACTIVE_TESTS`; `1152: for path in sorted(classifier._FULL_VALIDATION_INACTIVE_TESTS):`; `1154: ValueError, match="CI_INACTIVE_TEST_REQUIRES_DISPOSITION"` |
| `git log -S'CI_INACTIVE_TEST_REQUIRES_DISPOSITION' --oneline e3a5ed4..7136040 -- tests/` | no commit (exit 0) |
| `git grep` of the two identifiers outside `docs/`, the classifier and the integration file | no match |
| GitHub open pull requests on `amthorn78/glow-hdengine-v2` | none |
| `ls docs/ephemeral \| grep -E 'WU-PR-01-pr-implementation-(plan\|result)-v2'` | none; v2.0 of the plan and of the result are new files |
| `ls docs/changes/` | `AUDIT_RESULTS.json`, `AUDIT_SUMMARY.md` (no `GCFPE_PROMPT_PROVENANCE.md`) |

**What the code does at `dc701f2`.**
- `changed_test_targets` (`ci/checks/classify_ci_changes.py`, from line 1510) normalizes and sorts the paths. For each path, it first refuses a symlinked `tests/` path, then refuses a member of `_FULL_VALIDATION_INACTIVE_TESTS` (lines 1532–1533), before any lane or owner logic. The set is read from the module global at call time.
- The set is empty (line 152), so `test_full_validation_inputs_run_the_supplemental_behavioral_gap` (lines 1137–1156) loops over nothing at lines 1152–1156 and proves nothing about the refusal. That is LR-1.

### 4.2 LR-2 and LR-3 facts (re-read for this plan)

GitHub Actions run listing for branch `claude/elegant-mayer-y6ppap` (17 runs), read 2026-10-13:

| Head | Run | Conclusion | Created → updated (UTC) |
| :- | :- | :- | :- |
| `26140fe` | 38329588625 | cancelled | 00:55:00 → 00:58:52 |
| `68d9207` | 38329893033 | success | 00:58:46 → 01:15:36 |
| `e13516b` | 38331608172 | cancelled | 01:19:51 → 01:37:31 |
| `a7fb338` | 38332996216 | success | 01:37:16 → 01:56:28 |
| `218b65d` | 38335070763 | success | 02:03:26 → 02:22:09 |
| `bb0f85c` | 38336691078 | **success** | 02:23:57 → 02:35:56 |
| `4d8a047` | 38338530975 | success | 02:46:57 → 02:58:08 |
| `f134651` | 38342040842 | success | 03:30:34 → 03:45:33 |
| `a22be49` | 38343487439 | cancelled | 03:49:06 → 04:05:41 |
| `496e2c7` | 38344773095 | failure | 04:05:24 → 04:09:37 |
| `1fae26b` … `b6206fa` | 38346583864 to 38379706424 (7 runs) | success | 04:28:13 → 10:13:48 |

The statements to correct:
- **LR-2.** #627 "What changed": "`tests/evidence/test_rails_ci_workflow_integration.py`: new coverage, S04, S05 and inactive-refusal tests, plus the pin updates." Result v1.0 §4 records plan v1.1 §8 as "applied unchanged" and lists "`tests/evidence/test_rails_ci_workflow_integration.py` pins and new tests (plan §5.5)". No inactive-refusal test was added (§4.1, the `git log -S` row).
- **LR-3 (a).** Result v1.5 §2: "CI on `bb0f85c` | the run started by the fourth push. It is stale because R-9 requires a correction, and this push supersedes it (`cancel-in-progress` for pull requests)". In fact run 38336691078 completed **success** at 02:35:56Z, before the next run was created at 02:46:57Z. No later record states that outcome, and #627's "Hosted CI" list of passing heads omits `bb0f85c`.
- **LR-3 (b).** Result v1.9 §4: "identical code passed on `f134651` and every earlier head". The runs on `26140fe` and `e13516b` were cancelled and give no result for those heads. Every earlier run that completed (`68d9207`, `a7fb338`, `218b65d`, `bb0f85c`, `4d8a047`, `f134651`) concluded success.

### 4.3 Prototype (this session; scratch only, never pushed)

A throwaway clone of `main` at `dc701f2` got the §6.1 edit, committed locally as `9a45abc` (tree `7d1d3862dddd`). The checks ran with Python 3.12.3, CI's install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), pytest 8.4.2, `ruby` 3.3.6 on `PATH`, and `env -i` closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; every credential variable unset).

| # | Check | Result |
| :- | :- | :- |
| P-1 | The new case and `test_full_validation_inputs_run_the_supplemental_behavioral_gap` | 2 passed in 0.69 s |
| P-2 | Negative control: lines 1532–1533 removed from the classifier in a scratch worktree of `9a45abc` | the new case fails: `Failed: DID NOT RAISE <class 'ValueError'>` (1 failed) |
| P-3 | Without the monkeypatch, `changed_test_targets(ROOT, ("tests/synthetic/test_inactive_disposition_probe.py",))` | `()`, so the refusal in P-1 comes only from set membership |
| P-4 | Classifier CLI, `--base dc701f2… --head 9a45abc… --event-name pull_request` (full SHAs) | exit 0; `reason=selected_lanes`; `path_count=1`; seven lanes; `needs_python=true`; `changed_tests=true`; 163 targets, equal to `_full_validation_test_targets()` |
| P-5 | `python3 ci/checks/check_agents_md_citations.py`; `bash ci/checks/check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK`, exit 0 |
| P-6 | `git diff --check` over the prototype commit; diff size | exit 0; 1 file, 19 insertions, 0 deletions |
| P-7 | Changed-test step exactly as `ci.yml` runs it (detached worktree of `9a45abc`, the 163 targets from P-4, one pytest process, `PYTHONPATH` set to the worktree) | 3,264 passed in 480.24 s; exit 0; `git diff --exit-code` 0; `git status --short --untracked-files=all` empty. The tracked files newer than the pre-run marker are exactly OBS-4's 11 same-byte paths (9 under `artifacts/bodygraph/` and `schemas/bodygraph_source_invariance.*.v2.json`, plus `artifacts/release_id.txt` and `artifacts/release_pack_manifest.json`). The count equals the cycle-1 final count (lineage review V-2) because the integration file is not a changed-test target (P-8) |
| P-8 | Where the integration file runs: `_fixed_lane_test_provider("tests/evidence/test_rails_ci_workflow_integration.py")`; `grep` of `ci.yml` | `rails`; `ci.yml` line 219, `python -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py`, the last command of the rails-lane step. It is not among the 163 changed-test targets (0 matches in the P-4 list) |
| P-9 | Rails lane as `ci.yml` runs it, in the same worktree after P-7: `python ci/checks/run_rails_job_definitions.py` with the three job files, then the integration file | runner exit 0 (`RAILS_JOB_DEFINITIONS_OK`; 39 passed); integration file **138 passed** in 28.68 s, exit 0 (base `dc701f2`: 137 passed); `git diff --exit-code` 0; status empty; no tracked file newer than a marker touched before the step |
| P-10 | `python scripts/release_id_recompute.py --check-manifest-only` on `9a45abc` | exit 0 (C-5: no member change) |

## 5. Scope

**In scope (the whole corrective scope; lineage review §10):**

| Item | Path | Bound |
| :- | :- | :- |
| C-1 (LR-1) | `tests/evidence/test_rails_ci_workflow_integration.py` | one new test function (§6.1). Test-only. No other line of the file changes |
| C-2 (LR-2, LR-3) | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v2.0.md` (new) | the PR-30 result record of plan cycle 2, carrying the corrections of §6.2 |

Both paths are inside instruction v1.0 §6: the integration file is a bounded file ("pinned workflow and classifier expectations"), and the `docs/ephemeral/` PR result record is the evidence record.

**Out of scope (unchanged and not touched):**
- every other file. In particular `ci/checks/classify_ci_changes.py`, `.github/workflows/ci.yml`, `pytest.ini`, every `tools/**` and `scripts/**` file, every release member, every governed artifact, `AGENTS.md`, `README.md` and `docs/pfcanon/`;
- the historical records: plan v1.0 and v1.1, results v1.0 to v1.15, the lineage review and the #627 description stay as they are (lineage review §10 item 2);
- R-14: settled by CR-4 (PO-D4 confirmed; PO disposition §2);
- CR-5: settled by the Product Owner (PO disposition §3);
- the lineage review's O-1 to O-6 and every carried item (lineage review §6), which stay with their named owners (§17);
- WU-PR-02 and later units. The WU-PR-02 instruction is issued only after WU-PR-01 is accepted (lineage review §10).

No rescope is needed: the correction delivers what plan v1.1 already committed to, inside the approved base. No boundary finding exists (PR-20 Execute 6).

## 6. Design

### 6.1 C-1: the synthetic inactive-refusal case

Insert this function in `tests/evidence/test_rails_ci_workflow_integration.py` immediately after `test_full_validation_inputs_run_the_supplemental_behavioral_gap` (which ends at line 1156 at `dc701f2`) and before `test_every_current_governed_primary_selects_evidence`, with two blank lines on each side. The file already imports `re` and `pytest` and binds `classifier` and `ROOT`.

```python
def test_inactive_test_refusal_rejects_a_synthetic_inactive_path(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The inactive set is empty, so the loop above asserts nothing. A
    synthetic member proves that a direct change to an inactive test still
    fails closed, alone and beside a full-validation input."""

    synthetic = "tests/synthetic/test_inactive_disposition_probe.py"
    assert not (ROOT / synthetic).exists()
    assert synthetic not in classifier._FULL_VALIDATION_INACTIVE_TESTS
    monkeypatch.setattr(
        classifier, "_FULL_VALIDATION_INACTIVE_TESTS", {synthetic}
    )
    expected = f"^CI_INACTIVE_TEST_REQUIRES_DISPOSITION:{re.escape(synthetic)}$"
    for paths in ((synthetic,), ("requirements.txt", synthetic)):
        with pytest.raises(ValueError, match=expected):
            classifier.changed_test_targets(ROOT, paths)
```

Why each element is there:
- **Monkeypatch, not a real entry.** Re-adding a real file to the inactive set would change classifier behaviour and the roster pin (`configured == fixed | supplemental | inactive`). `monkeypatch.setattr` rebinds the module global for this test only. The refusal reads that global at call time (§4.1), so the patch reaches it, and pytest restores the empty set afterwards.
- **A synthetic path that does not exist.** It proves that membership alone triggers the refusal. P-3 shows that the same path is otherwise accepted with no target. The two precondition asserts keep the case honest if such a file or entry ever appears.
- **Exact message.** The anchored pattern pins both the code and the path, so a refusal for a different path or code fails the test.
- **Beside a full-validation input.** `requirements.txt` is a full-validation path that sorts first and runs the owner computation before the synthetic path is reached. The refusal must still win, as the classifier's fail-closed rule requires.
- **The existing loop stays.** Lines 1152–1156 remain unchanged. They still guard any real entry added to the set later, which the new case does not replace.

### 6.2 C-2: result record v2.0

PR-30 writes `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v2.0.md` (result `PR_CANDIDATE_PUBLISHED`). Besides the usual PR-30 content (§12), it carries a section "Corrections to the cycle-1 record" with the three corrections below. Each states the statement as recorded, where it is, and the actual fact with its evidence. The record says that the earlier records and #627's description are unchanged and remain historical statements, and that this record supersedes them only for the facts listed.

| ID | Recorded statement and location | Actual fact and evidence |
| :- | :- | :- |
| LR-2 | #627 "What changed": "new coverage, S04, S05 and inactive-refusal tests"; result v1.0 §4: plan v1.1 §8 "applied unchanged", "pins and new tests (plan §5.5)" | No inactive-refusal test was added in cycle 1. `git log -S'CI_INACTIVE_TEST_REQUIRES_DISPOSITION' e3a5ed4..7136040 -- tests/` returns no commit, and the existing loop iterates an empty set. Cycle 2 adds the case (this PR, C-1) |
| LR-3 (a) | result v1.5 §2: the run on `bb0f85c` "is stale … this push supersedes it (`cancel-in-progress`)" | run 38336691078 on `bb0f85c` completed **success** at 02:35:56Z, before the next run was created (38338530975, 02:46:57Z). It was not cancelled. #627's "Hosted CI" list of passing heads omits `bb0f85c` |
| LR-3 (b) | result v1.9 §4: the close-pack test's code "passed on `f134651` and every earlier head" | the runs on `26140fe` (38329588625) and `e13516b` (38331608172) were cancelled and give no result. Every earlier run that completed concluded success: `68d9207`, `a7fb338`, `218b65d`, `bb0f85c`, `4d8a047`, `f134651` |

PR-30 re-reads the run listing for `claude/elegant-mayer-y6ppap` from the GitHub Actions API before writing these rows and quotes the run IDs, heads, conclusions and times it reads. If any value differs from §4.2, it records the value it read and flags the difference in the record. It never copies §4.2 unverified.

No other content of the cycle-1 records is restated or corrected. A fact that is not in LR-2 or LR-3 is not part of this correction.

## 7. Change set

| Path | Change |
| :- | :- |
| `tests/evidence/test_rails_ci_workflow_integration.py` | +19 lines: the §6.1 function (prototype diff: 1 file, 19 insertions, 0 deletions) |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v2.0.md` | new; the PR-30 result record of cycle 2 (§6.2, §12) |

Nothing else changes. `git diff --name-only <base>..<head>` lists exactly these two paths, plus the later PR-35 result records under `docs/ephemeral/`.

## 8. Implementation sequence (PR-30)

PR-30 executes this after Nathan's Proceed for exactly this plan (v2.0), in a dedicated session.

1. **Recover before creating anything.**
   - Inspect local roots, worktrees, branches, open PRs and `docs/ephemeral/` for cycle-2 WU-PR-01 work (`*-pr-implementation-result-v2*`, a branch or PR carrying the §6.1 function). Resume the most advanced consistent state.
   - Fetch `main` and record the base SHA. If `main` has moved past `dc701f2`, check `git diff dc701f2 <base> -- tests/evidence/test_rails_ci_workflow_integration.py ci/checks/classify_ci_changes.py`. If it is not empty, re-locate the insertion point and the refusal lines and repeat P-1 to P-4 before continuing. A changed refusal mechanism is a finding to resolve before continuing, never a reason to edit the classifier.
   - Never reuse #627, its branch `claude/elegant-mayer-y6ppap`, or the cycle-1 Proceed. Create a new branch from the current `main`.
2. **Environment.** Python 3.12 with CI's install. Pytest readiness: `python -m pip install -r requirements-dev.txt`, then `python -m pytest --version` (`AGENTS.md`). Closed rails as in §4.3 (`env -i` is the proven method). `ruby` on `PATH` (`ruby --version` recorded), because the changed-test step runs the contract-inventory file (addendum 2.2, B-8).
3. **C-1.** Insert the §6.1 function exactly as written. Run P-1.
4. **Negative control.** In a scratch worktree, remove classifier lines 1532–1533 and confirm that the new case fails with `DID NOT RAISE`. Discard the worktree; the classifier in the candidate is untouched.
5. **Local validation** (§10), on the commit candidate's tree, in detached worktrees.
6. **One coherent commit** carrying C-1. Push to the new branch and open the PR with the `.github/pull_request_template.md` headings and the `AGENTS.md` content rules (§11).
7. **C-2.** Write result v2.0 (§6.2, §12), then commit, push and read it back. Return `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

Restart rules: any change after step 5 repeats step 5. A base change that touches the integration file or the classifier repeats steps 1 and 5.

## 9. Requirement → change → test map

| Obligation | Change | Proof (local, PR-30) | Proof (hosted, PR-35) |
| :- | :- | :- | :- |
| LR-1; plan v1.1 §5.4 "with a monkeypatched synthetic case so its pinned loop is not vacuous", §5.5, §8 | C-1 | P-1 (passes); P-2 negative control (fails without the refusal); P-3 (membership alone triggers it); P-9 (the integration file in its rails-lane shape: one more test than the base) | the rails lane runs the integration file (`ci.yml` line 219); the file is a fixed rails-lane test, not a changed-test target (P-8) |
| LR-2, LR-3 (record defects; `AGENTS.md` "Evidence attribution": record actual results, never relabel a run) | C-2 | the §6.2 rows, each with the re-read API values | — |
| S04 refusal family (C-6, fail-closed classification) unchanged | none (test-only) | `git diff <base>..<head> -- ci/` empty | — |
| Acceptance (1): zero uncovered | none needed; it holds and must stay true | `test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target` passes; no test file added or removed | rails lane |
| Acceptance (2): retained files pass with a clean tree | none needed | changed-test step in a detached worktree: `git diff --exit-code` 0, empty status, mtime clean apart from OBS-4's 11 same-byte paths (P-7) | changed-test step with its clean-tree assertion |
| Acceptance (3), (4) | unchanged | the S04 and S05 pinned tests pass in the integration file | rails lane |
| Acceptance (5): all seven lanes green on the exact head with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | the integration file is a full-validation path, so every lane runs (P-4) | P-4 | PR-35: exact-head CI |
| C-5: no member change | none | `python scripts/release_id_recompute.py --check-manifest-only` exit 0 | release lane |

## 10. Validation plan (PR-30, local)

All checks run on the commit candidate's tree, under §8 step 2's environment. A failure is a finding to fix, never to skip, deselect, mark `xfail` or quarantine.

1. `python3 ci/checks/check_agents_md_citations.py` and `bash ci/checks/check_env_pins.sh`: exit 0.
2. The integration file alone: all pass, and the count is one more than at the base (prototype: 138 against 137). PR-30 records both counts.
3. Negative control (§8 step 4).
4. The rails lane as `ci.yml` runs it, in a detached worktree of the candidate: `python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml`, then `python -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py`. Expect runner exit 0 and the step-2 count, then a clean diff, status and mtime check (prototype: P-9). This is the CI shape that runs C-1.
5. Classifier CLI dry run `--base <base SHA> --head <candidate SHA> --event-name pull_request` with full SHAs, `--github-output` and `--changed-tests-output` to files outside the tree. Expect exit 0, seven lanes, `changed_tests=true`, and targets equal to `_full_validation_test_targets()` (163 at `dc701f2`).
6. The changed-test step exactly as `ci.yml` runs it: a detached worktree, the target list from step 5, one `python -m pytest -q -p no:cacheprovider -- <targets>` process with `PYTHONPATH` set to the worktree. Afterwards: `git diff --exit-code` 0, an empty `git status --short --untracked-files=all`, and no tracked file newer than a marker touched before the run, apart from OBS-4's 11 same-byte paths. It does not run the integration file (P-8). It proves that acceptance (2) still holds on the candidate (prototype: P-7, 3,264 passed).
7. `python scripts/release_id_recompute.py --check-manifest-only`: exit 0. `git diff <base>..<candidate> --name-only` lists only the integration file.
8. `git diff --check`: exit 0.

The product, compat, db, evidence, qa and release lane emulations and the release attestation build are not needed locally. The change is one test function in a file only the rails lane runs (step 4), and hosted CI runs every lane on the exact head (acceptance (5)). PR-30 may run them if time allows and records what it ran.

## 11. PR split, merge dependencies and pull request description

- **One PR**, branched from the current `main`, carrying C-1 in one commit and then C-2, plus the PR-35 records. It is a new PR. #627 is not reopened.
- **Upstream merge dependency:** this plan's own PR must be merged to `main` before PR-30 runs, so that PR-30 reads it from `main`. #628 is merged.
- **Downstream:** PR-40 reviews the corrected lineage (#627 and this PR) after Nathan merges. The WU-PR-02 instruction (PR-10) follows only on ACCEPT. WU-PR-02 is otherwise dependency-ready (lineage review §10).
- **CI cost:** a full-validation change (all seven lanes, 163 changed-test targets). This follows from the classifier's rule for the integration file and is the smallest correct lane (Plan Templates, "CI lane classification and automated budget-control discipline").
- **PR description** (`AGENTS.md` "PR descriptions"):
  - **Why:** lineage review v1.0 finding LR-1 and its §10 correction, quoted.
  - **What changed:** grouped by path, as §7.
  - **Checks run:** each check with its counts.
  - **Not in this PR:** R-14 (CR-4), CR-5, O-1 to O-6 and the carried items with their owners; WU-PR-02.
  - **What merging does:** the synthetic refusal case becomes current on `main`. For the record under `docs/ephemeral/`, "Merging preserves the record and approves nothing (D21-C)". It establishes no QA, acceptance or closure.
  - It must not restate #627's claims as this PR's, and it says that #627's description is unchanged.

## 12. Acceptance and evidence obligations (result record v2.0)

Result v2.0 contains:
- the recovery performed and the base SHA;
- the implemented change (the commit, its tree, and the diff naming only the integration file);
- every §10 check actually run, with its result and counts, the negative control included;
- the `ruby` version used;
- the §6.2 corrections, with the API values re-read;
- the canon-conflict register as §16 states it;
- the nonclaims: CI green is not QA; no PF09 mapping; no QA artifact; WU-PR-01 is not accepted by this record.

QA evidence and `audit/qa/hde-crd-0002/` are out of scope (instruction §7).

## 13. Security and migration constraints

- **Migration:** none. No data, schema, catalog, member or governed-artifact change. Rollback is Nathan's revert of the squash commit, which removes only the test function and the record.
- **Security:** the change is test-only and only strengthens a fail-closed check. The classifier, the workflow (`permissions: contents: read`, exact-head checkout, closed rails, isolation) and every security obligation of instruction §11 are unchanged. No secret, token or key value appears in the test, the logs or the records.
- **Reviewer chain (addendum 2.3):** the Codex code review is read and resolved by PR-35. No Codex security review is requested or waited on, and its absence is not a gap.

## 14. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| R-1 | `main` moves and changes the refusal or the insertion point | §8 step 1 re-check; repeat P-1 to P-4 |
| R-2 | A reviewer asks for a broader inactive-set test, for example exclusion from `_full_validation_test_targets()` (line 1086) | Outside lineage review §10. PR-35 replies that it is outside the bounded correction and routes it to the whole-change IA; it is not added |
| R-3 | OBS-17: intermittent hosted failure of `tests/qa/test_generate_epic_close_pack.py` in the changed-test step | Not this PR's code. PR-35 handles it under its CI rules (one re-run at most when justified, otherwise a stated blocker). The test is never skipped |
| R-4 | Hosted `ruby` absent after `ubuntu-latest` moves to Ubuntu 26.04 | The contract-inventory file fails, never skips (B-8). PR-35 records it; OBS-12 stays with the Product Owner |
| R-5 | The record corrections misstate a run | §6.2 requires a fresh API read and quotes it |

Recovery:
- an interruption resumes in the same phase session from its last saved artifact;
- an ordinary defect in this plan returns to this PR-20 context, and a correction is a complete successor version (v2.1);
- a boundary found in PR-30 or PR-35 goes through RS-20 with `PR_RETURN_PHASE` recorded;
- abort is only Nathan's manual PR-50 instruction.

## 15. Decisions taken in this plan (within approved scope)

| ID | Decision | Why |
| :- | :- | :- |
| D-1 | Version the cycle-2 plan and records as v2.x (plan v2.0, result v2.0, PR-35 results v2.1 onward) | Keeps the corrective cycle's artifacts distinct from cycle 1's v1.x records, all of which are landed history |
| D-2 | A new test function; the existing loop is unchanged | Smallest change; the existing loop still guards a real entry added later |
| D-3 | A nonexistent synthetic path under `tests/` | Lineage review §10 names a synthetic path; nonexistence proves membership alone triggers the refusal (P-3) |
| D-4 | The second call mixes in `requirements.txt` | Shows that the refusal wins over full-validation owner computation in one change set, at no extra cost |
| D-5 | Locally, only the rails lane (§10 step 4) and the changed-test step (§10 step 6) are required; the other lane emulations and the attestation build are not | §10 closing paragraph |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER`, carried:

| ID | Classification | Status | Decision owner | Effect on this plan |
| :- | :- | :- | :- | :- |
| CR-1 | CANON_RECONCILIATION (PF30 record and "CRD Plan" wording versus HDE Governance §9.1.1) | APPROVED_AS_CHANGED | Thoth | none |
| CR-2 | CANON_RECONCILIATION (planned units in a Specification) | APPROVED_AS_CHANGED | Thoth | none |
| CR-3 | CANON_RECONCILIATION ("stable CRD ID recorded in PF30") | APPROVED_AS_CHANGED | Thoth | none |
| CR-4 | CANON_RECONCILIATION (PO-D4 versus the addendum 2.2 rescope-lane route) | APPROVED: PO-D4 confirmed for exactly R-14 ("I accept your recommendation for CR-4.") | Nathan / Product Owner (PO disposition §2) | R-14 stays an analyzer limit owned by the IA (OBS-16); outside this plan |
| CR-5 | CANON_RECONCILIATION (canon replacement inside an implementation PR) | APPROVED_AS_CHANGED ("For CR-5 I will reserve the right to assign such things as I see fit.") | Nathan / Product Owner (PO disposition §3) | this PR carries no canon change; any vehicle for one is the Product Owner's to assign |

**No new conflict.** This plan adds a test that plan v1.1 already committed to, and corrects records. Searched for this plan: `git grep` of `docs/pfcanon/` on `main` for `lineage review`, `re-plan`/`replan`, `inactive test`, `monkeypatch` and `vacuous`. The only hits are a PF06 Extended Moon Loop replanning rule (QA-lane scope; not applicable to a PR-40 re-plan), a PF19 QA-remediation line, PF01 mathematics, a PF14 viability line and historical PF23 and PF30.1 records. None governs this correction. PF10 v13.5.4 is silent on it beyond addenda 2.2 and 2.3 ("Silence rule").

## 17. Observations and carried items (not in this PR)

Unchanged from lineage review v1.0 §6, each with its owner:
- **O-1:** coverage-guard token scope → IA (WU-PR-06 instruction, C-3).
- **O-2:** retired generators' fail-closed tests; the `AGENTS.md` EPIC037 entrypoints → Product Owner and IA; WU-DOC-01.
- **O-3:** architecture snapshot `--check` STALE at base and head → Product Owner.
- **O-4:** stale references in `docs/RUN.md:9`, `docs/ADAPTER_009.md:115`, `README.md:218` → IA (WU-DOC-01 instruction).
- **O-5:** OBS-17, the intermittent close-pack test → QA tool and test owner, through the IA; Product Owner to route.
- **O-6:** unverified hosted behaviours (dot-prefixed `**` matching; docs-only PR starts no run; hosted ruby version) → IA, at the next relevant unit's CI. PR-35 of this cycle may observe the third from the job log, and records it if it does.
- **Carried owners** as lineage review §6 lists them: IA (OBS-16 (a) to (l), R-16, R-21, OBS-1, OBS-3 to OBS-5, OBS-7, OBS-9, OBS-13, OBS-14; WU-PR-03 baseline currency; WU-PR-06 ruby); WU-PR-04 owner (OBS-2, OBS-6); WU-DOC-01 (OBS-8; OBS-10 to the next editor); Product Owner (OBS-12, ruby on Ubuntu 26.04, HDE-SEPA006, another source of security review and HDE Governance §9.1.1 wording); GCFPE-MGMT-10 and the Product Owner (prompt and skill wording naming the Codex security review).

## 18. PR-30 and PR-35 ownership

- **PR-30** (after Nathan's Proceed for this v2.0, in a dedicated session):
  - recovers before creating any vehicle (§8 step 1);
  - implements only C-1 and C-2;
  - tests locally under §10;
  - forms one coherent commit for C-1 and publishes the initial candidate on a new branch and PR;
  - writes, pushes and reads back result v2.0;
  - returns `PR_CANDIDATE_PUBLISHED` with a handoff to PR-35 in PR-35's own dedicated session.

  PR-30 owns neither review correction nor CI readiness.
- **PR-35** (its own dedicated session):
  - retrieves and resolves the Codex code review findings (addendum 2.3), retests locally and pushes coherent corrections within §5;
  - uses CI economically: known findings first, no `[skip ci]` without Nathan's direct authorization;
  - verifies current-head CI (all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), remote-head identity and mergeability;
  - records each run on its heads with its actual conclusion (no relabelled or predicted outcome, which is the LR-3 class);
  - writes its records as results v2.1 onward;
  - returns `MERGE_PENDING — Ready to merge` without merging.

  No CI waiver exists for HDE-CRD-0002.
- **Merge:** Nathan merges, manually. Afterwards, PR-40 by the whole-change IA reviews the corrected WU-PR-01 lineage.

## 19. Session identity and recovery envelope

```yaml
paused_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (corrective planning complete; held for Proceed)
phase: PR-20 re-plan after PR-40 REJECT; no PR_RETURN_PHASE (no cycle-2 Proceed, vehicle or PR exists)
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner); authoring session https://claude.ai/code/session_012kGFYdD1BYJnXh3TagQetg
base_identity: Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0; PF10 v13.5.4; overlays addendum 2.2 and (reviewer chain) 2.3
entry_identity: lineage review v1.0 (REJECT, LR-1, §10); PO disposition of CR-4 and CR-5 v1.0
checkpoint_identity: this artifact (v2.0, AWAITING_PO_PROCEED); cycle-1 plans v1.0 and v1.1 preserved
completed_work: input reads, baseline verification, LR-2/LR-3 fact re-read from the Actions API, C-1 prototype with negative control, classifier dry run, changed-test step run, rails-lane run
pending_decision: Nathan's PR Implementation Proceed for exactly this plan (v2.0)
resume: on Proceed, PR-30 (§8)
scratch_state: TRANSIENT_SCRATCH only (prototype clone 9a45abc and venv in the session scratchpad); this plan is self-sufficient without them
```

## 20. TypeSafe reading for the receiving session (PR-30, cycle 2)

PF10 addendum 2.1 governs. The reading is reported as the skill printed it. No agent recommendation is given beside it.

Action sent (v6): "Implement, as a new dedicated PR session after the Product Owner's Proceed, a corrective detailed plan for an already merged CI-coverage work unit whose independent lineage review rejected it for one precise defect: add one prototyped, 19-line monkeypatched test case for one classifier refusal path to an existing 2,100-line test file, and write a new result record that corrects two record misstatements, with no production code, workflow or classifier change and a complete task list; then run the local validation (about 3,300 tests in one detached-worktree run plus a negative control) and publish one pull request of two files. No live provider call occurs; code review, a review-and-CI phase, the Product Owner's manual merge and another lineage review follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 1.63 (confidence 0.72); rung probabilities low 0.00, medium 0.39, high 0.58, extra high 0.03, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.99 (confidence 0.98). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.39, Opus 5.5 at high 0.57, Opus 5.5 at extra high 0.03, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.00, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Flags: boundary between medium and high. Sent 2026-10-13T13:00:14Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T13:00:14Z; HTTP 200 in 0.85 s; 4277 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between medium and high.
- **One send**, taken before this artifact was saved. The Notion row was not written (this executing-flow session writes nothing to Notion).
- **Nathan's pick for PR-30:** not stated.
- **Nathan's pick for this PR-20 session:** not stated. The lineage review's reading for PR-20 was Opus 5.5 at high (lineage review §11).

**Surface advice (facts, not a model recommendation):**
- PR-30 runs as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, on a new branch from `main`, with Notion read access and GitHub access (Actions run reads for §6.2; PR creation).
- It needs Python 3.12, CI's install and `ruby` on `PATH`. It needs no live vendor, production or database access, and the closed rails strip every credential.
- The changed-test step is the long check (P-7, about 8 minutes locally). The rails lane takes about 30 seconds, and everything else takes seconds.
- Prerequisite: the pull request carrying this plan is merged to `main` first.

## 21. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / PR-20 / WU-PR-01 / plan 3 (v2.0; re-plan after PR-40 REJECT) |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1 (approved by review v1.1) |
| instruction | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md`, v1.0 |
| entry | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v1.0.md` (REJECT) |
| overlays | PF10 addenda 2.2 and 2.3 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md`) |
| work unit / requirements | WU-PR-01; S03, S04, S05 (LR-1 correction) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (fetched 2026-10-13; page state as of 2026-10-12T02:29:47Z) |
| role/stage | dedicated WU-PR-01 PR engineering session / PR-20 (re-plan entry) |
| capture time | 2026-10-13T13:11:01Z |
| execution identity | https://claude.ai/code/session_012kGFYdD1BYJnXh3TagQetg |
| inherited prompt uses | IA-10, IA-40, IA-30, PR-10 (instruction v1.0 §20), PR-20 (plans v1.0 §22, v1.1 §22), RS-20 (review v1.0 §14), PR-30 (result v1.0 §13), PR-35 (results v1.1 to v1.15), PR-40 (lineage review v1.0 §12) |
| repository persistence | PENDING / NON_GATING: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` does not exist at `dc701f2`. Recorded here only; owner of any later installation: GCFPE-MGMT-10 and the Product Owner |

## Canon relied on

Read on `main` at `dc701f2`. `docs/pfcanon/` is unchanged since `7136040` (#627 carried PF10 v13.5.4).

- **PF10-HDE-Build-Notes v13.5.4**, read in full.
  - Addendum 2.2 sets the effective baseline (approved base plus 2.2) and the B-8 `ruby` requirement used in §8 and §14.
  - Addendum 2.3 Rules 2 and 3 set the reviewer chain (§13, §18).
  - Addendum 2.1 governs §20.
  - The "Silence rule" returns everything else to permanent canon.
- **PF04-Canon-HDE-Governance v2.8.7**, read in full for these sections:
  - §9.1.1 "Change authority and exact-artifact lineage": the dedicated PR session authors the detailed per-PR plan; the Product Owner's `PR Implementation Proceed` is its approval; a plan's existence alone does not authorize implementation.
  - §9.7.7 "Plan approval gate": the `ASK OK? — PR IMPLEMENTATION PLAN` hold; no plan-local token; no proof by intent; negative audit proof is valid proof (§4.1's `git log -S` row).
- **PF27-Canon-Plan-Templates v2.0.5**, read in full for these sections:
  - "Artifact execution boundary": an Implementation Plan is working direction.
  - "Repository loci and file minting": §4.1's CA-vetted snapshot; new-file absence proofs.
  - "CI lane classification and automated budget-control discipline": the smallest correct lane, chosen by the classifier; no invented YAML (§11).
- **PF06-Canon-Change-Process-Guide v2.5.4**: the replanning paragraph of the Extended Moon Loop section, read to confirm that it does not govern a PR-40 re-plan.
- **Operative documentation:** `AGENTS.md`:
  - canon-first and read-only canon rules;
  - closed rails and pytest readiness;
  - "Evidence attribution, currentness and distinct decisions" (record actual results; never relabel an earlier run; the basis of §6.2);
  - PR description headings;
  - "Code review scope — CI-exempt paths" (`docs/ephemeral/` is out of automated review scope).
- **In-flight documents:** listed in §3. The lineage review's own "Canon relied on" (PF04 §9.1.2 and §9.1.4, PF06 §0.2 to §0.4, PF19 §10.8) stands for the findings this plan corrects. It was not re-read here.

## Checks run by this session

| Check | Result |
| :- | :- |
| `origin/main` after #628 | `dc701f2`; #628 merged; branch reset to it |
| `git diff --stat 7136040 dc701f2 -- . ':!docs/ephemeral'` | empty |
| Inactive-set and refusal loci (§4.1) | as quoted |
| `git log -S'CI_INACTIVE_TEST_REQUIRES_DISPOSITION' e3a5ed4..7136040 -- tests/` | no commit |
| Actions run listing, branch `claude/elegant-mayer-y6ppap` | 17 runs; §4.2 table |
| #627 description (API read) | the LR-2 sentence and the LR-3 (a) omission confirmed |
| Open pull requests | none |
| Prototype P-1 to P-10 | §4.3 |
| TypeSafe reading (§20) | HTTP 200; Opus 5.5 at high |

Not executed by this session: hosted CI, the Codex code review, the fixed-lane emulations and the release attestation build. These belong to PR-30, PR-35 and hosted CI.

---

**State:** `AWAITING_PO_PROCEED`, held at `ASK OK? — PR IMPLEMENTATION PLAN`. This is the WU-PR-01 corrective detailed PR implementation plan v2.0, complete and executable within the approved base plus PF10 addendum 2.2. Nathan's `PR Implementation Proceed` for exactly this plan path and version authorizes PR-30. Nothing else does.
