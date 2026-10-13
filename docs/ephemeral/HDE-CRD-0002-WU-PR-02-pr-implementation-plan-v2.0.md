---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-02-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v2.0.md
artifact_version: "2.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 2, the corrective re-plan after PR-40 REJECT (PR-20 "Re-plan entry", reject_replan)
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 91831e94c1c5; the plan of cycle 1, Proceeded once and spent; landed as amthorn78/glow-hdengine-v2#634, squash 1d2c834) with its companion docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff (blob 242eff5f7c8e). Both are preserved unchanged. This v2.0 does not restate v1.0's scope; that scope is landed history
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_WORK_UNIT_LINEAGE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v1.0.md (PR-40, decision REJECT; finding LR-1; bounded correction §8; blob d2336fb0e952; 40,880 bytes; landed on main at ef3972b, amthorn78/glow-hdengine-v2#635)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob b98bf846287d; unchanged)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE) — lineage only
cycle_1_records: PR-30 result docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md (v1.0, PR_CANDIDATE_PUBLISHED; blob 5942994df870); PR-35 result docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.4.md (v1.4, MERGE_PENDING, historical pre-merge evidence; blob 934b7f415bb2); PR-35 checkpoints v1.1 to v1.3 beside it
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10)
applicable_pf10_overlays: PF10 addendum 2.3 (reviewer chain without the Codex security review). Addendum 2.1 governs §20 only. Addendum 2.2 is scoped to WU-PR-01; its B-8 fact (the contract-inventory test file needs `ruby` on PATH) is used in §8 and §14 as a fact about the file this correction changes, not as an overlay on this unit. Addendum 2.4 is a WU-PR-01 record
effective_baseline: approved base + applicable PF10 overlays = the base above + PF10 addendum 2.3 (reviewer chain), with lineage review v1.0 §8 binding the corrective scope (it extends instruction §6 by one test file as a non-material correction under instruction §14)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5, effective 2026.10.13; blob c98831e8112d; 50,181 bytes; sha256 fb2899266ec3635e7c734a880136fcfdd4cc5ebc5e2a340ae51cd7e33dca54d2; read in full by this session; one unlettered document; addenda 2.1, 2.2, 2.3, 2.4; unchanged on main since cc3dc33)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md § 2.3 (record docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md); § 2.1 governs §20 only
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (the new dedicated WU-PR-02 PR engineering session for plan cycle 2, created by Nathan / Product Owner)
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); authoring session https://claude.ai/code/session_014BSjYENRE9rSuw6D7QZs8A
author: dedicated HDE-CRD-0002 WU-PR-02 PR engineering session (PR-20, plan cycle 2)
return_owner: the continuing whole-change HDE-CRD-0002 Implementation Agent (PR-40 after the corrective merge; RS-20 for any rescope)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1 (as recorded by the lineage review)
created_at: 2026-10-13T22:16:16Z
repository_baseline: origin/main ef3972b5e3a0cfe4aefc46774f24f2fb9b487afa (tree ae16a16d93ce; #635). git diff 1d2c834..ef3972b outside docs/ephemeral/ is empty, so every code fact the lineage review measured at 1d2c834 holds here
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner, docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md); no new entry (§16)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-02 — Detailed PR Implementation Plan v2.0 (corrective, plan cycle 2)

## 1. State and authority

**AWAITING_PO_PROCEED.** Held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.7.7).

This is the complete, executable corrective plan for WU-PR-02. It plans exactly the bounded correction of lineage review v1.0 §8, and nothing else:
1. make `tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent` pass on `main` again, keeping its intent, with a test-only change (LR-1);
2. confirm by a full sweep at the corrective head that no other regression exists;
3. write a new PR result record under `docs/ephemeral/`.

The change was prototyped on `main` `ef3972b` and verified: it fails before and passes after, a negative control shows the test still detects a broken supersession filter, and every validation the lineage review requires passes on the prototype (§4.3).

Authority:
- The cycle-1 Proceed (for plan v1.0) is spent. It is not reused. #634 is landed history: it is never resumed, reused or pushed to, and nothing is reverted (PR-20 "Re-plan entry"; lineage review §8).
- Only Nathan's `PR Implementation Proceed` (PR-30) for exactly `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v2.0.md` (v2.0) authorizes implementation. Only Nathan merges.
- This plan authorizes no implementation, merge, publication, Ops, QA, acceptance or closure. It changes no canon and creates no PF10 addendum.

## 2. Identity and lineage

| Field | Value |
| :- | :- |
| `CHANGE_CLASS` / `CHANGE_ID` | `CRD` / `HDE-CRD-0002` |
| `WORK_UNIT_ID` | `WU-PR-02`: evidence tooling; Distillation; S06, S11, S12, S13, S22 |
| Entry | PR-40 `PR_WORK_UNIT_LINEAGE_REVIEW` v1.0, decision `REJECT`, finding LR-1, bounded correction §8 |
| `PR_INSTRUCTION_ID` | instruction v1.0, unchanged. Its §6 bounds and §7 exclusions govern, extended by lineage review §8 by exactly one test file |
| `IMPLEMENTATION_PLAN_ID` / `PLAN_REVIEW_ID` | Plan v1.1 + review v1.1 (Isis, IA-30 `INITIAL_APPROVE`) |
| `SPECIFICATION_ID` | Specification v1.1 approved (Thoth) |
| Overlays | addendum 2.3 (reviewer chain) |
| Plan cycle 1 | instruction v1.0 → plan v1.0 → Proceed → PR-30 result v1.0 → PR-35 results v1.1 to v1.4 → #634 merged (squash `1d2c834`) → PR-40 lineage review v1.0 `REJECT` (#635, `ef3972b`) |
| Plan cycle 2 | this plan v2.0 → Proceed → PR-30 result v2.0 → PR-35 results v2.1 onward → merge → PR-40 |
| Dependency state | ready. The lineage review is on `main` (#635 merged 2026-10-13T21:53:03Z). No open pull request exists on the repository; no WU-PR-02 v2 plan or result exists (§4.1) |

## 3. Sources read

**Read in full by this session:**
- lineage review v1.0;
- instruction v1.0;
- PR-30 result v1.0 and PR-35 result v1.4;
- PF10 v13.5.5 (Front Matter, Precedence §1 to §9, Template, Addendum Index, addenda 2.1 to 2.4);
- PR-20 — Create Detailed PR Implementation Plan — 100926.1 (Notion);
- the corrective-plan precedent `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v2.0.md` (format and versioning only).

**Read in the sections cited:**
- plan v1.0: front matter, section headings, §15 decisions PD-1 to PD-11 (to avoid identifier collision and to confirm that §8.1 to §8.5 placed no case in the contract-inventory file);
- Implementation Plan v1.1 §7 WU-PR-02 block (purpose, deliverables, acceptance (1) to (5), "Risks and recovery: Mirror consumers rejecting added fields (run every read-only validator)");
- Specification v1.1 row S03 ("recorded failures and collection errors are fixed or retired with their files");
- `tools/evidence/update_evidence_index.py`: lines 28–29 (`ROOT`, `HUMAN_INDEX`), 56–89 (`CURRENT_RELEASE_CAPTURE_PATHS`, the label pattern), 1101–1108 (`EPIC034_PR04_SUPERSEDED_INDEX_KEYS`), 3818–3930 (`_current_release_label`, `_strip_current_release_label`, `_retained_release_labels`, `_recorded_capture_digests`, `_current_release_labels`, `_apply_current_release_label`), 4050–4145 (`_load_human_index`);
- `tests/evidence/test_hdapi_v2_contract_inventory.py`: lines 1–16 (imports), 570–605 (the sibling PR-02 and PR-03 supersession tests), 1267–1278 (the LR-1 test);
- `tests/evidence/test_evidence_index_missing_state.py` lines 1125–1220 (the landed label tests, including the `_current_release_label` stub at line 1138);
- `ci/checks/classify_ci_changes.py` registrations of the contract-inventory file; `.github/workflows/ci.yml` lines 60–135 and 220–320 (classifier, changed-test, evidence, qa and release steps).

**Not re-read; carried from the lineage review:** results v1.1 to v1.3, the Implementation Audit, the Plan review and the attribution evidence of #634. No decision here rests on them.

## 4. Repository baseline (verified at `ef3972b`)

### 4.1 Observed Evidence Snapshot (CA vetted)

| Command | Output |
| :- | :- |
| `git log --oneline -1 origin/main` | `ef3972b docs(ephemeral): HDE-CRD-0002 WU-PR-02 PR work-unit lineage review v1.0 (PR-40, REJECT) (#635)` |
| `git diff --stat 1d2c834 ef3972b -- . ':!docs/ephemeral'` | empty (exit 0) |
| `grep -n "_current_release_label\|def _load_human_index" tools/evidence/update_evidence_index.py` | `3818:def _current_release_label() -> str:`; `3889:def _current_release_labels(...)` (calls it at 3897); `4050:def _load_human_index()`; its return at 4089–4145 is `_apply_current_release_label(_dedupe_entries([...]), _current_release_labels(release_labels))` |
| `sed -n 3818,3840p` of the updater | `manifest_path = ROOT / "catalog/manifest.json"`; `if manifest_only_problems(manifest_path): raise SystemExit("CURRENT_RELEASE_LABEL_MANIFEST_INVALID")`, then canonical-bytes and version checks with the same refusal |
| `grep -rn "_current_release_label" tests/` | `tests/evidence/test_evidence_index_missing_state.py:1138: writer._current_release_label = lambda: {NEXT_RELEASE_LABEL!r}` (the landed release-label test stubs the same seam), plus strip-helper uses; no use in the contract-inventory file |
| `sed -n 1267,1279p tests/evidence/test_hdapi_v2_contract_inventory.py` | the LR-1 test: writes two stale rows to `tmp_path/INDEX.json`, monkeypatches `indexer.ROOT` to `tmp_path` and `indexer.HUMAN_INDEX`, calls `indexer._load_human_index()`, asserts no `EPIC034_PR04_SUPERSEDED_INDEX_KEYS` row remains |
| `git grep -l update_evidence_index ef3972b -- tests/` (excluding `.md`) | 24 test files (listed in §10 step 5) |
| GitHub open pull requests on `amthorn78/glow-hdengine-v2` (GitHub API, read 2026-10-13 during this session) | none |
| `ls docs/ephemeral \| grep -E 'WU-PR-02-pr-implementation-(plan\|result)-v2'` | none before this plan; v2.0 of the result is a new file |
| `ls docs/changes/` | `AUDIT_RESULTS.json`, `AUDIT_SUMMARY.md` (no `GCFPE_PROMPT_PROVENANCE.md`) |

**What the code does at `ef3972b`.** `_load_human_index()` always ends in `_current_release_labels(...)`, which calls `_current_release_label()` first. That function validates `ROOT / "catalog/manifest.json"` with `manifest_only_problems` and raises `SystemExit("CURRENT_RELEASE_LABEL_MANIFEST_INVALID")` when it is absent or invalid (CX-3). The LR-1 test points `ROOT` at an empty `tmp_path`, so the call exits before the supersession assertion is reached. The supersession filter itself (lines 4076–4077) is untouched by #634.

### 4.2 Reproduction (this session)

Environment E-CI: `/usr/bin/python3.12 -m venv`, CPython 3.12.3, CI's install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e <clone>`); readiness `python -m pip install -r requirements-dev.txt` exit 0, then `python -m pytest --version` → `pytest 8.4.2`; `ruby 3.3.6` on `PATH`. Every run under `env -i` closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH` = the worktree, no credential variable set), in detached worktrees of a scratch clone, never in the repository checkout.

| Commit | LR-1 test alone | Detail |
| :- | :- | :- |
| `0cd7b84` (base of #634) | **1 passed** (exit 0) | — |
| `1d2c834` (merge of #634) | **1 failed** (exit 1) | `SystemExit: CURRENT_RELEASE_LABEL_MANIFEST_INVALID` at `tools/evidence/update_evidence_index.py:3826` |
| `ef3972b` (`main`) | **1 failed** (exit 1) | same |

`c27c5e8` (PR-30's head) is not in this clone (squash-merged branch); the lineage review records its failure. This matches the lineage review §5 row "LR-1 test alone".

### 4.3 Prototype (this session; scratch only, never pushed)

A detached worktree of `ef3972b` got the §6.1 edit, committed locally as `3952915` (`39529159d8b40319aa01b8f64c7e23d591c30109`; tree `40a67926031f`). Environment as §4.2.

| # | Check | Result |
| :- | :- | :- |
| P-1 | The LR-1 test alone on `3952915` | 1 passed (exit 0) |
| P-2 | Negative control: in a scratch worktree of `3952915`, the two lines that exclude `EPIC034_PR04_SUPERSEDED_INDEX_KEYS` in `_load_human_index` removed | the corrected test **fails** (`AssertionError: assert not ({…} & {…EPIC034_PR04…})`, 1 failed, exit 1). The test still detects a broken supersession filter. Worktree restored; clean |
| P-3 | Refusal unchanged | `git diff ef3972b 3952915 -- tools/ ci/ .github/ catalog/` empty; `test_release_label_refuses_a_manifest_that_fails_full_validation` (write and `--check` modes refuse `CURRENT_RELEASE_LABEL_MANIFEST_INVALID`; in `tests/evidence/test_evidence_index_missing_state.py`) passes in P-8 and P-10 |
| P-4 | Classifier CLI `--base ef3972b5e3a0… --head 39529159d8b4… --event-name pull_request` (full SHAs) | exit 0; `reason=selected_lanes`; `path_count=1`; `lanes=evidence`; product, compat, db, rails, qa, release `false`; `needs_python=true`; `changed_tests=true`; 2 targets: `tests/evidence/test_hdapi_v2_contract_inventory.py`, `tests/evidence/test_http_reader_ci_ownership.py` |
| P-5 | `python3 ci/checks/check_agents_md_citations.py`; `bash ci/checks/check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK`, exit 0 |
| P-6 | `git diff --check`; diff size | exit 0; 1 file, 4 insertions, 0 deletions |
| P-7 | Changed-test step exactly as `ci.yml` runs it (detached worktree, the 2 targets of P-4, one `python -m pytest -q -p no:cacheprovider --` process) | **304 passed** in 125.36 s, exit 0; `git diff --exit-code` 0; `git status --short --untracked-files=all` empty; no tracked file newer than a marker touched before the run |
| P-8 | Evidence lane as `ci.yml` runs it: `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`, plus `check_lf_endings.py`; then the six evidence-lane test files | each check exit 0: `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh` (invoked directly, as `ci.yml` does; it is a Python script with a `.sh` name, and a first invocation through `bash` by this session's harness returned 2 with a shell syntax error, an operator error, not a result), `check_final_lf.sh`, `check_lf_endings.py`. The six test files: **130 passed** in 604.45 s, exit 0 (the lineage review's count at `1d2c834` is 130). `git diff --exit-code` 0; status empty |
| P-9 | Release-lane set: `release_id_recompute.py --check-manifest-only`; the four release-lane test files in a detached worktree | `release_id_recompute.py --check-manifest-only` exit 0; the four test files **79 passed** in 2.88 s, exit 0 (lineage review at `1d2c834`: 79); `git diff --exit-code` 0; status empty |
| P-10 | Every test file that imports or runs the updater (24 files, §10 step 5), one pytest process, detached worktree | **1,406 passed** in 846.80 s (24 files), exit 0; `git diff --exit-code` 0; status empty |
| P-11 | Updater written twice in a detached worktree of `3952915` | exit 0, 0; `git diff --exit-code` 0 after each; status empty (fixed point) |
| P-12 | Governed byte identity: `git diff --quiet ef3972b 3952915 -- docs/evidence artifacts/evidence_index.jsonl artifacts/evidence_index.jsonl.sha256 audit/gates/topology catalog tools ci .github` | exit 0 (no difference) |
| P-13 | Full sweep, `python -m pytest -q -p no:cacheprovider -rfE tests/`, detached worktree | **4,529 passed, 3 skipped, 2 xfailed**, 0 failed, in 1,102.22 s, exit 0 (run 2026-10-13T21:57:41Z–22:16:05Z); `git diff --exit-code` 0; status empty. Against the lineage review's sweep at `1d2c834` (1 failed, 4,528 passed, 3 skipped, 2 xfailed), the only difference is the LR-1 test, now passing. The 3 skips and 2 xfails are pre-existing and unchanged in count |

## 5. Scope

**In scope (the whole corrective scope; lineage review §8):**

| Item | Path | Bound |
| :- | :- | :- |
| C-1 (LR-1) | `tests/evidence/test_hdapi_v2_contract_inventory.py` | four added lines inside `test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent` (§6.1). Test-only. No other line of the file changes. The file is bound by lineage review §8 item 1 ("Locus: the test file (test-only). That file is not among instruction §6's paths; this review binds it") |
| C-2 | `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v2.0.md` (new) | the PR-30 result record of plan cycle 2 (lineage review §8 item 3; §12) |

**Out of scope (unchanged and not touched):**
- `tools/evidence/update_evidence_index.py` and every other `tools/**`, `scripts/**` and `ci/**` file, `.github/workflows/ci.yml`, every release member, `catalog/manifest.json`, every governed artifact (Index, Mirror, checksums, path proofs, orientation), `AGENTS.md`, `README.md` and `docs/pfcanon/`. A test-only correction keeps the test's intent (§6.2), so lineage review §8's conditional permission for an updater change does not arise;
- the classifier: no owner registration is added (PD-13, §15); the classifier already runs the corrected file when it changes (P-4);
- the CX-2 residual (accepted by the Product Owner), LR-O1, LR-O2 and LR-O3 (to later instructions by the IA), and the carried observations (§17);
- the historical records: plan v1.0 and its prototype diff, results v1.0 to v1.4, the lineage review and #634's description stay as they are;
- WU-PR-03 and later units. The WU-PR-03 instruction is issued only after WU-PR-02 is accepted (lineage review §8 "Next unit").

No rescope is needed. The correction is the one lineage review §8 binds, and it is "not material … It touches no acceptance intent, protected boundary, dependency or other unit's scope" (lineage review §7 LR-1). No boundary finding exists (PR-20 Execute 6).

## 6. Design

### 6.1 C-1: stub the release-label seam in the LR-1 test

In `tests/evidence/test_hdapi_v2_contract_inventory.py`, inside `test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent` (lines 1267–1278 at `ef3972b`), insert four lines immediately after `monkeypatch.setattr(indexer, "HUMAN_INDEX", human_index)` and before `rows = indexer._load_human_index()`, at the function's indentation:

```python
    # tmp_path has no catalog/manifest.json, from which the updater derives the
    # release label (and refuses without one); this test concerns supersession.
    label = "current-release capture: release 0.0.0, release_id " + "0" * 64
    monkeypatch.setattr(indexer, "_current_release_label", lambda: label)
```

The complete function afterwards, as prototyped (`3952915`):

```python
def test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    stale_rows = [
        {"artifact_key": "hdapi_v2.adapter_boundary_proof", "discovered_physical_path": "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log"},
        {"artifact_key": "epic034.pr04.boundary_check", "discovered_physical_path": "audit/qa/hde-epic034/pr-04/boundary_check.log"},
    ]
    human_index = tmp_path / "INDEX.json"
    human_index.write_text(json.dumps(stale_rows) + "\n", encoding="utf-8")
    monkeypatch.setattr(indexer, "ROOT", tmp_path)
    monkeypatch.setattr(indexer, "HUMAN_INDEX", human_index)
    # tmp_path has no catalog/manifest.json, from which the updater derives the
    # release label (and refuses without one); this test concerns supersession.
    label = "current-release capture: release 0.0.0, release_id " + "0" * 64
    monkeypatch.setattr(indexer, "_current_release_label", lambda: label)
    rows = indexer._load_human_index()
    row_keys = {(row["artifact_key"], row["discovered_physical_path"]) for row in rows}
    assert not row_keys & indexer.EPIC034_PR04_SUPERSEDED_INDEX_KEYS
```

Why each element is there:
- **The seam.** `_current_release_label()` is the only function that reads the manifest on this path (§4.1). `_current_release_labels` looks it up as a module global at call time, so `monkeypatch.setattr` reaches it, and pytest restores the original after the test. Everything else in `_load_human_index` runs unchanged under the temporary root, including the label application to roster paths.
- **The landed precedent.** The updater's own label test stubs the same function the same way (`test_evidence_index_missing_state.py` line 1138, `writer._current_release_label = lambda: …`), so this is the established test seam, not a new one.
- **A well-formed label.** The stub returns a string that matches `_CURRENT_RELEASE_LABEL_RE` (release token without whitespace, comma or semicolon; 64 hex digits), so it behaves as a real label wherever the updater applies or strips it. The values `0.0.0` and 64 zeros name no real release.
- **A local, not a module constant.** The label stays inside the one function, so no other line of the 4,424-line file changes.
- **The comment.** It states why the stub exists, so a later reader does not take it for a weakening of the refusal.
- **Nothing else moves.** `ROOT` still points at `tmp_path`, so the test still runs with every EPIC034 PR-04 output absent, which is its intent; the assertion is unchanged.

### 6.2 Why a test-only correction keeps the intent (lineage review §8 item 1)

| Lineage review constraint | How C-1 meets it | Proof |
| :- | :- | :- |
| "Make … pass on `main` again, keeping its intent: superseded EPIC034 PR-04 rows are removed when their outputs are absent" | the temporary root (outputs absent) and the assertion are unchanged | P-1 passes; P-2 shows the test fails when the supersession filter is broken |
| "Do not weaken the landed behavior. The updater still refuses an invalid or absent manifest (CX-3), and the label semantics (CX-1, IF-7) are unchanged" | no non-test file changes; the stub exists only inside this one test | P-3 (empty diff over `tools/`, `ci/`, `.github/`, `catalog/`; the refusal test passes); P-11 and P-12 (no updater output change) |
| "Locus: the test file (test-only)" | one file, four added lines | P-6 |
| "A change to `tools/evidence/update_evidence_index.py` is allowed only if the plan shows that a test-only correction cannot keep the test's intent" | a test-only correction keeps it, so no updater change is planned | P-1, P-2 |

**Alternatives considered and rejected (PD-12):**
- *Copy a valid `catalog/manifest.json` and its 45 members into `tmp_path`.* It would satisfy `manifest_only_problems`, but it couples a supersession test to the release roster and its bytes (the test would break at every re-cut), and it places release files under a root the test means to keep empty. Rejected.
- *Drop the `ROOT` monkeypatch.* The real root holds `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`, so the test would no longer run with the outputs absent, which is its stated intent. Rejected.
- *Make the updater tolerate an absent manifest (skip labels).* It weakens CX-3 and changes IF-7 semantics, which lineage review §8 forbids. Rejected.
- *Stub `_current_release_labels` (plural) to return `{}`.* It would also work, but it skips the label application path that the real updater runs. Stubbing the single manifest-reading function keeps more of the real code path under test. Not chosen.

## 7. Change set

| Path | Change |
| :- | :- |
| `tests/evidence/test_hdapi_v2_contract_inventory.py` | +4 lines in one function (§6.1; prototype: 1 file, 4 insertions, 0 deletions) |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v2.0.md` | new; the PR-30 result record of cycle 2 (§12) |

Nothing else changes. `git diff --name-only <base>..<head>` lists exactly these two paths, plus the later PR-35 result records under `docs/ephemeral/`. No governed artifact is regenerated, because no updater output changes (P-11, P-12).

## 8. Implementation sequence (PR-30)

PR-30 executes this after Nathan's Proceed for exactly this plan (v2.0).

1. **Recover before creating anything.**
   - Inspect local roots, worktrees, branches, open PRs and `docs/ephemeral/` for cycle-2 WU-PR-02 work (`*-WU-PR-02-pr-implementation-result-v2*`, a branch or PR carrying the §6.1 lines). Resume the most advanced consistent state.
   - Fetch `main` and record the base SHA. If `main` has moved past `ef3972b`, run `git diff ef3972b <base> -- tests/evidence/test_hdapi_v2_contract_inventory.py tools/evidence/update_evidence_index.py ci/checks/classify_ci_changes.py`. If it is not empty, re-locate the insertion point and the label seam and repeat P-1, P-2 and P-4 before continuing. A changed label mechanism is a finding to resolve before continuing, never a reason to edit the updater.
   - Never reuse #634, its branch `claude/intelligent-cannon-32u7tl`, or the cycle-1 Proceed. Publish from a branch that holds only the new work on top of the current `main`.
2. **Environment.** E-CI as §4.2: Python 3.12 with CI's install; pytest readiness (`python -m pip install -r requirements-dev.txt`, then `python -m pytest --version`, per `AGENTS.md`); closed rails under `env -i`; `ruby` on `PATH` with `ruby --version` recorded, because the changed-test step runs the contract-inventory file (PF10 addendum 2.2, B-8). The Debian rehearsal environment (E-DEB) is not needed: nothing touches `tools/evidence/build_release_attestation.py` or `tools/evidence/regenerate_identity_closure.py`.
3. **Before.** Run the LR-1 test alone at the base: expect 1 failed with `CURRENT_RELEASE_LABEL_MANIFEST_INVALID` (§4.2). Record it.
4. **C-1.** Insert the §6.1 lines exactly as written. Run the LR-1 test alone: expect 1 passed.
5. **Negative control.** In a scratch worktree of the candidate, remove the two lines of `_load_human_index` that exclude `EPIC034_PR04_SUPERSEDED_INDEX_KEYS`; confirm that the corrected test fails. Discard the worktree; the updater in the candidate is untouched.
6. **Local validation** (§10), on the commit candidate's tree, in detached worktrees.
7. **One coherent commit** carrying C-1. Push and open the PR with the `.github/pull_request_template.md` headings and the `AGENTS.md` content rules (§11).
8. **C-2.** Write result v2.0 (§12), then commit, push and read it back. Return `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

Restart rules: any change after step 6 repeats step 6. A base change that touches the test file, the updater or the classifier repeats steps 1 to 6.

## 9. Requirement → change → test map

| Obligation | Change | Proof (local, PR-30) | Proof (hosted, PR-35) |
| :- | :- | :- | :- |
| LR-1; lineage review §8 item 1 | C-1 | before/after (§8 steps 3 and 4: fails at the base, passes at the candidate); negative control (§8 step 5) | the changed-test step runs the file (P-4: 2 targets) |
| S03 outcome held across units (Specification S03 "recorded failures … are fixed"; lineage review §6 "NOT MET" row) | C-1 | the full `tests/` sweep at the candidate has no failure (§10 step 9) | the changed-test step; the evidence lane |
| Plan v1.1 §7 WU-PR-02 risk "Mirror consumers rejecting added fields" | C-1 | every updater-consuming test file passes (§10 step 5; LR-O2) | — |
| Lineage review §8 validation: "The corrected test fails at `1d2c834` and passes at the corrective head" | C-1 | §8 steps 3 and 4 (the base `ef3972b` has the same code as `1d2c834`, §4.1) | — |
| Lineage review §8 validation: "Every test file that imports or runs `update_evidence_index.py` passes …, or the full `tests/` sweep does" | none needed | both are run (§10 steps 5 and 9) | — |
| Lineage review §8 validation: "The evidence and release lane sets pass" | none needed | §10 steps 6 and 7 | evidence lane (selected, P-4); release lane not selected by the classifier for a test-only change (P-4) |
| Lineage review §8 validation: "The Index, Mirror and governed companions stay byte-identical" | none | §10 step 8 | evidence lane `--check` validators |
| CX-3 refusal and CX-1/IF-7 label semantics unchanged | none | `git diff <base>..<candidate> -- tools/ ci/ .github/ catalog/` empty; `test_release_label_refuses_a_manifest_that_fails_full_validation` passes (evidence lane set) | evidence lane |
| WU-PR-02 acceptance (1) to (5) and contracts D-1 to D-5 | unchanged | no non-test file changes; the lineage review's MET rows stand (lineage review §6) | — |
| C-5 / D-5: no member change | none | `python scripts/release_id_recompute.py --check-manifest-only` exit 0 | — |

## 10. Validation plan (PR-30, local)

All checks run on the commit candidate's tree, under §8 step 2's environment, in detached worktrees with `PYTHONPATH` set to the worktree. A failure is a finding to fix, never to skip, deselect, mark `xfail` or quarantine.

1. `python3 ci/checks/check_agents_md_citations.py` and `bash ci/checks/check_env_pins.sh`: exit 0.
2. The LR-1 test alone: 1 failed at the base, 1 passed at the candidate (§8 steps 3 and 4). Negative control (§8 step 5).
3. Classifier CLI dry run `--base <base SHA> --head <candidate SHA> --event-name pull_request` with full SHAs, `--github-output` and `--changed-tests-output` to files outside the tree. Expect exit 0, `lanes=evidence`, `changed_tests=true`, and the 2 targets of P-4.
4. The changed-test step exactly as `ci.yml` runs it, on the step-3 targets: one `python -m pytest -q -p no:cacheprovider -- <targets>` process. Expect the P-7 count (304 passed). Afterwards `git diff --exit-code` 0, an empty `git status --short --untracked-files=all`, and no tracked file newer than a marker touched before the run (the prototype run P-7 touched no tracked file, so OBS-4's 11 same-byte rewrites did not occur with these targets; any rewrite PR-30 observes is recorded).
5. Every test file that imports or runs the updater (LR-O2), in one pytest process: `tests/config/test_config_artifacts.py`, `tests/config/test_typed_bundles.py`, `tests/evidence/test_engine_core_evidence.py`, `tests/evidence/test_evidence_index_env.py`, `tests/evidence/test_evidence_index_missing_state.py`, `tests/evidence/test_evidence_index_snapshot.py`, `tests/evidence/test_evidence_index_token_sets.py`, `tests/evidence/test_evidence_skeleton.py`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/evidence/test_hdapi_v2_contract_inventory.py`, `tests/evidence/test_hde_epic037_v2_adapter.py`, `tests/evidence/test_internal_version_manifest_captures.py`, `tests/evidence/test_machine_mirror_self_proof.py`, `tests/evidence/test_orientation_demo.py`, `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/evidence/test_release_attestation.py`, `tests/evidence/test_release_manifest_content_binding.py`, `tests/ops/test_evidence_index.py`, `tests/qa/test_epic020_qa_docs.py`, `tests/qa/test_epic024_bootstrap_status.py`, `tests/qa/test_generate_epic_close_pack.py`, `tests/qa/test_viability_generator_wrappers.py`, `tests/transport/test_internal_version_contract.py`, `tests/unit/test_check_agents_md_citations.py`. PR-30 re-derives the list with `git grep -l update_evidence_index <candidate> -- tests/` (excluding `.md`) and records any difference. Expect 0 failed and a clean tree (prototype P-10: 1,406 passed).
6. The evidence lane as `ci.yml` runs it: the seven read-only checks plus `python tools/evidence/check_lf_endings.py`, each exit 0, with the `ci/checks/*.sh` files invoked directly by path as `ci.yml` does (`check_mirror_schema.sh` is a Python script; P-8); then the six evidence-lane test files. Expect the P-8 count and a clean tree.
7. The release-lane set: `python scripts/release_id_recompute.py --check-manifest-only` exit 0; the four release-lane test files (`tests/runtime/test_identity.py`, `tests/evidence/test_release_attestation.py`, `tests/evidence/test_release_manifest_content_binding.py`, `tests/evidence/test_sanity_pipeline.py`) in a detached worktree. Expect the P-9 count and a clean tree. The attestation build is not required: the release lane is not selected (P-4) and no release input changes; PR-30 may run it and records what it ran.
8. Governed byte identity: the updater written twice in a detached worktree, `git diff --exit-code` 0 after each; and `git diff --quiet <base> <candidate> -- docs/evidence artifacts/evidence_index.jsonl artifacts/evidence_index.jsonl.sha256 audit/gates/topology catalog tools ci .github` exit 0.
9. The full sweep: `python -m pytest -q -p no:cacheprovider -rfE tests/` in a detached worktree. Expect 0 failed and a clean tree (prototype P-13: 4,529 passed, 3 skipped, 2 xfailed). This is the confirmation lineage review §8 item 2 requires ("The corrective plan's own sweep confirms that at its head").
10. `git diff --check`: exit 0. `git diff --name-only <base>..<candidate>` lists only the test file.

The product, compat, db, rails and qa lane emulations are not needed locally: the classifier selects none of them (P-4), and steps 5 and 9 run every one of their test files that the change could affect. PR-30 records the qa-lane file `tests/qa/test_generate_epic_close_pack.py` result from step 5 (OBS-17).

## 11. PR split, merge dependencies and pull request description

- **One PR**, from a branch whose only commits are this cycle's, carrying C-1 in one commit and then C-2, plus the PR-35 records. It is a new PR. #634 is not reopened.
- **Upstream merge dependency:** this plan's own PR must be merged to `main` before PR-30 runs, so that PR-30 reads it from `main`. #635 is merged.
- **Downstream:** the correction lands before WU-PR-03 and before WU-PR-07 (lineage review §8 "Merge order"). PR-40 reviews the corrected lineage (#634 and this PR) after Nathan merges. The WU-PR-03 instruction (PR-10) follows only on ACCEPT.
- **CI cost:** the evidence lane and a two-file changed-test step (P-4). This follows from the classifier's own rules for the test file and is the smallest correct lane (Plan Templates, "CI lane classification and automated budget-control discipline"). The result record under `docs/ephemeral/` selects no lane.
- **PR description** (`AGENTS.md` "PR descriptions"):
  - **Why:** lineage review v1.0 finding LR-1 and its §8 correction, quoted.
  - **What changed:** grouped by path, as §7.
  - **Checks run:** each check with its counts, the before/after and the negative control included.
  - **Not in this PR:** the CX-2 residual (Product Owner accepted), LR-O1 to LR-O3 (IA, later instructions), the classifier (PD-13), the carried observations with their owners; WU-PR-03.
  - **What merging does:** the corrected test becomes current on `main`. For the record under `docs/ephemeral/`, "Merging preserves the record and approves nothing (D21-C)". It establishes no QA, acceptance or closure. Merge-order dependency: before WU-PR-03 and WU-PR-07.
  - It must not restate #634's claims as this PR's, and it says that #634's description is unchanged.

## 12. Acceptance and evidence obligations (result record v2.0)

Result v2.0 contains:
- the recovery performed and the base SHA;
- the implemented change (the commit, its tree, and the diff naming only the test file);
- the before/after of the LR-1 test and the negative control;
- every §10 check actually run, with its result and counts, the `ruby` version and the environment;
- the canon-conflict register as §16 states it;
- the nonclaims: CI green is not QA; no PF09 mapping; no QA artifact; no updater, governed-artifact or member change; WU-PR-02 is not accepted by this record.

QA evidence and `audit/qa/hde-crd-0002/` are out of scope (instruction §7). No new evidence family is produced.

## 13. Security and migration constraints

- **Migration:** none. No data, schema, catalog, member or governed-artifact change. Rollback is Nathan's revert of the squash commit, which removes only the four test lines and the record.
- **Security:** the change is test-only. It stubs one function inside one test and touches no refusal in product or tool code; the updater's manifest refusal (CX-3) is unchanged and still tested. Instruction §11's obligations (exact-source attestation, clean child environment, `--no-index`, `--require-clean`, root-bound probe, `crd_id` validator) are untouched. No secret, token or key value appears in the test, the logs or the records; the stub label is a fixed public string.
- **Reviewer chain (addendum 2.3):** the Codex code review is read and resolved by PR-35. No Codex security review is requested or waited on, and its absence is not a gap.

## 14. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| R-1 | `main` moves and changes the label seam or the test | §8 step 1 re-check; repeat P-1, P-2, P-4 |
| R-2 | A reviewer reads the stub as weakening the refusal | §6.2 table: the refusal is unchanged and still tested by the updater's own test; PR-35 replies with that evidence |
| R-3 | A reviewer asks for a classifier owner registration or an updater change | outside lineage review §8 ("The classifier, unless an owner registration is stated as a finding"; updater change only if test-only fails). PR-35 replies that it is outside the bounded correction and routes it to the whole-change IA (LR-O2 owner); it is not added |
| R-4 | Hosted `ruby` absent on the runner | the contract-inventory file fails, never skips (addendum 2.2, B-8); PR-35 records it; OBS-12 stays with the Product Owner. WU-PR-01 cycle 2 showed `ruby` present on `ubuntu-24.04` (addendum 2.4) |
| R-5 | Another hidden updater consumer fails | §10 steps 5 and 9 cover every consumer and every test file; a failure is a finding for this PR only if C-1 caused it, otherwise it is routed to the IA |
| R-6 | OBS-17: intermittent failure of `tests/qa/test_generate_epic_close_pack.py` | the qa lane is not selected (P-4); locally it runs in §10 steps 5 and 9; a failure is recorded as OBS-17, never fixed here |

Recovery:
- an interruption resumes in the same phase session from its last saved artifact;
- an ordinary defect in this plan returns to this PR-20 context, and a correction is a complete successor version (v2.1);
- a boundary found in PR-30 or PR-35 goes through RS-20 with `PR_RETURN_PHASE` recorded;
- abort is only Nathan's manual PR-50 instruction.

## 15. Decisions taken in this plan (within approved scope)

Numbered after plan v1.0's PD-1 to PD-11 so no identifier is reused.

| ID | Decision | Why |
| :- | :- | :- |
| PD-12 | Test-only correction: stub `_current_release_label` inside the LR-1 test (§6.1); the alternatives in §6.2 rejected | lineage review §8 item 1 prefers a test-only change and allows an updater change only if test-only cannot keep the intent; it can (P-1, P-2). The seam is the one the landed label test already stubs |
| PD-13 | No classifier owner registration for the contract-inventory file under the updater | lineage review §8 places the classifier outside the correction unless stated as a finding; LR-O2 assigns the consumer-run duty to later instructions, not to a registration. A change to the file already selects it (P-4). Not a finding |
| PD-14 | Version the cycle-2 plan and records as v2.x (plan v2.0, result v2.0, PR-35 results v2.1 onward) | keeps cycle 2's artifacts distinct from cycle 1's v1.x records, all of which are landed history; same convention as WU-PR-01 cycle 2 |
| PD-15 | Run both the consumer set and the full sweep locally; the attestation build optional | lineage review §8 accepts either; both are cheap enough (§20 surface advice) and the sweep is what §8 item 2 names |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER`, carried:

| ID | Classification | Status | Decision owner | Effect on this plan |
| :- | :- | :- | :- | :- |
| CR-1 | CANON_RECONCILIATION | APPROVED_AS_CHANGED | Thoth | none |
| CR-2 | CANON_RECONCILIATION | APPROVED_AS_CHANGED | Thoth | none |
| CR-3 | CANON_RECONCILIATION | APPROVED_AS_CHANGED | Thoth | none |
| CR-4 | CANON_RECONCILIATION | APPROVED | Nathan / Product Owner (`docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2) | none (WU-PR-01 only) |
| CR-5 | CANON_RECONCILIATION | APPROVED_AS_CHANGED | Nathan / Product Owner (same record §3) | this PR carries no canon change |

**No new conflict.** LR-1 is an implementation defect, not a canon conflict (lineage review §9). The correction changes one test and adds one record. Searched for this plan: `git grep` of `docs/pfcanon/` on `main` for `re-plan`, `replan`, `reject_replan` and `lineage review`. The hits are a PF06 Extended Moon Loop replanning line (QA-lane scope), a PF19 QA-remediation line, PF20 and PF30.1 historical records, PF23 and PF27 lines on other subjects, and PF10 addenda 2.3 and 2.4. None governs this correction beyond what §1 and §13 apply. PF10 v13.5.5 is otherwise silent on it ("Silence rule").

## 17. Observations and carried items (not in this PR)

Unchanged from lineage review v1.0 §7, each with its owner:
- **CX-2 residual / LR-O1:** accepted by the Product Owner; the IA carries it into the WU-PR-03, WU-PR-04, WU-PR-05 and WU-PR-08 instructions and to WU-DOC-01 with OBS-W2-1.
- **LR-O2:** classifier coverage of updater consumers → IA; later updater-changing instructions (WU-PR-07) require a run of every consuming test file. This plan applies that rule to itself (§10 step 5).
- **LR-O3:** updater runs before the cut, label timing and stale labels → IA, in the WU-PR-03 instruction.
- **OBS-W2-1, OBS-W2-2:** doc-delta candidates → WU-DOC-01.
- **OBS-W2-3:** other ambient probes → observation only.
- **OBS-17:** `tests/qa/test_generate_epic_close_pack.py` → QA tool and test owner, through the IA; Product Owner to route.
- **O-6:** hosted `ruby` version unprinted → IA. It becomes applicable here, because this PR selects the contract-inventory file (P-4). PR-35 records the version if the job log shows it.
- **AQ-1:** gates WU-PR-07 only. **PF10 addendum 2.2's downstream items:** the WU-PR-03 and WU-PR-06 instructions.

## 18. PR-30 and PR-35 ownership

- **PR-30** (after Nathan's Proceed for this v2.0, in a dedicated session):
  - recovers before creating any vehicle (§8 step 1);
  - implements only C-1 and C-2;
  - records the before/after and the negative control, and tests locally under §10;
  - forms one coherent commit for C-1 and publishes the initial candidate on a new PR;
  - writes, pushes and reads back result v2.0;
  - returns `PR_CANDIDATE_PUBLISHED` with a handoff to PR-35 in PR-35's own dedicated session.

  PR-30 owns neither review correction nor CI readiness.
- **PR-35** (its own dedicated session):
  - retrieves and resolves the Codex code review findings (addendum 2.3), retests locally and pushes coherent corrections within §5;
  - uses CI economically: known findings first, no `[skip ci]` without Nathan's direct authorization;
  - verifies current-head CI (the evidence lane and the changed-test step as classified, and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), remote-head identity and mergeability;
  - records each run on its heads with its actual conclusion, and the hosted `ruby` version if the log shows it (O-6);
  - writes its records as results v2.1 onward;
  - returns `MERGE_PENDING — Ready to merge` without merging.

  No CI waiver exists for HDE-CRD-0002.
- **Merge:** Nathan merges, manually. Afterwards, PR-40 by the whole-change IA reviews the corrected WU-PR-02 lineage (#634 then this PR).

## 19. Session identity and recovery envelope

```yaml
paused_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (corrective planning complete; held for Proceed)
phase: PR-20 re-plan after PR-40 REJECT; no PR_RETURN_PHASE (no cycle-2 Proceed, vehicle or PR exists)
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner); authoring session https://claude.ai/code/session_014BSjYENRE9rSuw6D7QZs8A
base_identity: Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0; PF10 v13.5.5; overlay addendum 2.3 (reviewer chain)
entry_identity: lineage review v1.0 (REJECT, LR-1, §8)
checkpoint_identity: this artifact (v2.0, AWAITING_PO_PROCEED); cycle-1 plan v1.0 and its prototype diff preserved
completed_work: input reads, baseline verification, LR-1 reproduction at 0cd7b84, 1d2c834 and ef3972b, C-1 prototype with negative control, classifier dry run, changed-test step, evidence and release lane sets, updater-consumer set, updater fixed point, full sweep
pending_decision: Nathan's PR Implementation Proceed for exactly this plan (v2.0)
resume: on Proceed, PR-30 (§8)
scratch_state: TRANSIENT_SCRATCH only (prototype commit 3952915, worktrees and venv in the session scratchpad); this plan is self-sufficient without them
```

## 20. TypeSafe reading for the receiving session (PR-30, cycle 2)

PF10 addendum 2.1 governs. The reading is reported as the skill printed it. No agent recommendation is given beside it.

Action sent (v6): "Implement, as a new dedicated PR session after the Product Owner's Proceed, a corrective detailed plan for an already merged evidence-tooling work unit whose independent lineage review rejected it for one regression: add a prototyped 4-line monkeypatch to one existing test in a 4,400-line test file so that it again passes without the release manifest its temporary root lacks, with no change to the 5,000-line evidence-index updater or any other tool, and write a new result record, following a complete task list; then run the local validation (a reproduction before and after, a negative control, the 24 test files that use the updater, the evidence and release lane sets, and a full sweep of about 4,500 tests taking about 25 minutes, all in detached worktrees with a clean-tree check) and publish one pull request of two files. No live provider call occurs; code review, a review-and-CI phase, the Product Owner's manual merge and another lineage review follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 1.95 (confidence 0.83); rung probabilities low 0.00, medium 0.15, high 0.75, extra high 0.10, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.03, Opus 5.5 0.97 (confidence 0.94). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.15, Opus 5.5 at high 0.73, Opus 5.5 at extra high 0.10, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.02, Fable 5.1 at extra high 0.00, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-13T22:00:03Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T22:00:03Z; HTTP 200 in 0.66 s; 4323 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none.
- **One send**, taken before this artifact was saved. The Notion row was not written (this executing-flow session writes nothing to Notion).
- **Nathan's pick for PR-30:** not stated.
- **Nathan's pick for this PR-20 session:** not stated. The lineage review's reading for PR-20 was Opus 5.5 at high (lineage review §12).

**Surface advice (facts, not a model recommendation):**
- PR-30 runs as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt and GitHub access for PR creation.
- It needs Python 3.12 with CI's install (package-index access to build it) and `ruby` on `PATH`; the cloud container provides `/usr/bin/python3.12` and `ruby` 3.3.6. It needs no Debian rehearsal, no live vendor, production or database access, and the closed rails strip every credential.
- Durations measured here: the full sweep about 18 minutes (with two other runs sharing 4 cores); the updater-consumer set about 14 minutes; the changed-test step about 2 minutes; the evidence lane test set about 10 minutes; everything else seconds.
- Prerequisite: the pull request carrying this plan is merged to `main` first.

## 21. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / PR-20 / WU-PR-02 / plan 2 (v2.0; re-plan after PR-40 REJECT) |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1 (approved by review v1.1) |
| instruction | `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md`, v1.0 |
| entry | `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v1.0.md` (REJECT) |
| overlays | PF10 addendum 2.3 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md`) |
| work unit / requirements | WU-PR-02; S06, S11, S12, S13, S22 (LR-1 correction; S03 outcome held) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (fetched 2026-10-13; page state as of 2026-10-12T02:29:47Z) |
| role/stage | dedicated WU-PR-02 PR engineering session / PR-20 (re-plan entry) |
| capture time | 2026-10-13T22:16:16Z |
| execution identity | https://claude.ai/code/session_014BSjYENRE9rSuw6D7QZs8A |
| inherited prompt uses | PR-10 instruction 1 (instruction §20); PR-20 plan 1 (plan v1.0 §22); PR-30 implementation 1 (result v1.0 §10); PR-35 review resolution 1 (result v1.4 §10); PR-40 lineage review 1 (lineage review §13) |
| repository persistence | PENDING / NON_GATING: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` does not exist at `ef3972b`. Recorded here only; owner of any later installation: GCFPE-MGMT-10 and the Product Owner |

## Canon relied on

Read on `main` at `ef3972b`. `docs/pfcanon/` is unchanged since `cc3dc33`.

- **PF10-HDE-Build-Notes v13.5.5**, read in full.
  - Addendum 2.3 Rules 2 and 3 set the reviewer chain (§13, §18).
  - Addendum 2.2's B-8 fact (`ruby` for the contract-inventory file) is used in §8 and §14; addendum 2.4 records `ruby` present on the hosted runner for WU-PR-01.
  - Addendum 2.1 governs §20.
  - The "Silence rule" returns everything else to permanent canon.
- **PF04-Canon-HDE-Governance v2.8.7**, read for these sections:
  - §9.1.1 "Change authority and exact-artifact lineage": the dedicated PR session authors the detailed per-PR plan; the Product Owner's `PR Implementation Proceed` is its approval; a plan's existence alone does not authorize implementation; PR merges remain Product Owner actions; a revision supplies a complete replacement and preserves the prior artifact.
  - §9.1.2 "Canon precedence and persistent sources": canon on `main`; in-flight documents and reviews govern within their scope (the lineage review's §8 bounds this plan).
  - §9.7.7 "Plan approval gate": the `ASK OK? — PR IMPLEMENTATION PLAN` hold; no plan-local token; no proof by intent (§4 carries the measured proofs); negative audit proof is valid proof (P-3, P-12).
- **PF27-Canon-Plan-Templates v2.0.5**, read for these sections:
  - "Repository loci and file minting": §4.1's CA-vetted snapshot; the minted result file named exactly (§7).
  - "CI lane classification and automated budget-control discipline": the smallest correct lane, chosen by the classifier; no invented YAML (§11).
- **Operative documentation:** `AGENTS.md`:
  - canon-first and read-only canon rules;
  - closed rails and pytest readiness;
  - sole Index/Mirror writer and no hand edits (no governed artifact changes here; P-11, P-12);
  - "Evidence attribution, currentness and distinct decisions" (record actual results; the tested state is the prototype commit, not the later PR head);
  - PR description headings;
  - "Code review scope — CI-exempt paths" (`docs/ephemeral/` is out of automated review scope).
- **In-flight documents:** listed in §3. The lineage review's own "Canon relied on" (PF04 §9.1.1 and §9.1.2; PF10 addenda 2.3 and 2.4; PF12 §6.2, §8.3, §8.17) stands for the finding this plan corrects; PF12 was not re-read here because the correction touches no schema, label or identity rule.

## Checks run by this session

| Check | Result |
| :- | :- |
| `origin/main` after #635 | `ef3972b`; #635 merged; working branch reset to it |
| `git diff --stat 1d2c834 ef3972b -- . ':!docs/ephemeral'` | empty |
| Label seam and loader loci (§4.1) | as quoted |
| Open pull requests; branches | none open; no corrective branch |
| Reproduction at `0cd7b84`, `1d2c834`, `ef3972b` | §4.2 |
| Prototype P-1 to P-13 | §4.3 |
| TypeSafe reading (§20) | HTTP 200; Opus 5.5 at high |

Not executed by this session: hosted CI, the Codex code review, the product, compat, db, rails and qa lane emulations, the release attestation build and the Debian rehearsal. These belong to PR-30, PR-35 and hosted CI, or are not needed (§10).

---

**State:** `AWAITING_PO_PROCEED`, held at `ASK OK? — PR IMPLEMENTATION PLAN`. This is the WU-PR-02 corrective detailed PR implementation plan v2.0, complete and executable within the approved base plus PF10 addendum 2.3 and the bounded correction of lineage review v1.0 §8. Nathan's `PR Implementation Proceed` for exactly this plan path and version authorizes PR-30. Nothing else does.
