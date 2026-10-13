---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-01-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: REJECT
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1; the object of the original Product Owner Proceed recorded in result v1.0; blob dbb9a56 at e3a5ed4 and at 7136040)
PR_30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.0.md (v1.0, PR_CANDIDATE_PUBLISHED)
PR_35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.15.md (v1.15, final record; MERGE_PENDING, historical pre-merge evidence; v1.1 to v1.14 are its preserved predecessors)
PR_REFS: amthorn78/glow-hdengine-v2#627 (the work unit's only pull request; merged)
entry_event: MERGE_OBSERVED, delivered by the PR-35 session in the pasted handoff (no saved MERGE_OBSERVED artifact exists; NOT PRODUCED). Merge verified independently below
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, in its read-only PR-40 lineage-review role, as instruction v1.0 §12 designates; this review in session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (selected by Nathan / Product Owner by pasting the handoff; the IA lineage's latest-known session in the handoff was https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah)
pr_30_session: https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8 (commits 26140fe, 68d9207)
pr_35_session: https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (the other 29 commits)
return_owner: the same continuing whole-change HDE-CRD-0002 Implementation Agent
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f)
prompt_release: GCFPE-20261009.1 / 100926.1 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1", exactly 55 members; read 2026-10-13)
created_at: 2026-10-13T12:44:32Z
repository_state_reviewed: origin/main 7136040821fe5deab5992a00ba8275644b1e7aca (tree 8b0cec5f4debea67ecc794d1014e9aab85cd01d4); no commit after it at review time
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md (v13.5.4; blob f31b4e04; sha256 7e285dffb1dd7ab40fa685c8412c63e8784a43a1f38c1adace6816a23bbca881; read in full; addenda 2.1, 2.2, 2.3)
pf10_addendum_paths: docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md (2.2); docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md (2.3)
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1, CR-2, CR-3 carried unchanged (APPROVED_AS_CHANGED); CR-4 and CR-5 recorded as PROPOSED, not yet reviewed (§9)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba), new dedicated WU-PR-01 session, corrective plan (§10)
---

# HDE-CRD-0002 WU-PR-01 — PR work-unit lineage review v1.0 (PR-40)

## 1. Decision

**REJECT.**

The landed work unit is delivered and independently re-verified in every respect but one:
- S03, S04 and S05 hold at `7136040`.
- Whole-change Plan acceptance (1) to (5) is met.
- Every addendum 2.2 bound holds.
- The landed delta reconciles exactly with the PR head.
- Hosted CI is green on the final head, and every Codex finding is dispositioned.

The one exception is a precise in-scope defect (LR-1). The Proceeded per-PR plan v1.1 commits to a monkeypatched synthetic inactive-refusal test case. It never landed, and the merged PR's description says it did. Under PR-40 "PRECISE IN-SCOPE DEFECT → re-plan", the route is a new per-PR plan for the same work unit through PR-20 (§10). The earlier Proceed is spent and is not reused.

What this decision is not:
- It is not an acceptance of WU-PR-01.
- It does not issue the WU-PR-02 instruction (§10).
- It establishes no QA verdict, acceptance, Ops, PF09/PF30 movement, release activation or closure.
- It changes no repository or PF content beyond this file.
- It creates no PF10 addendum.

## 2. Lineage

| Item | Identity |
| :- | :- |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (v1.1, SPECIFICATION_APPROVED, "ASK OK.") |
| Implementation Audit | `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md` (v1.0, AUDIT_COMPLETE) |
| Implementation Plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (v1.1) |
| Plan review | `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md` (IA-30 INITIAL_APPROVE, "ASK OK.") |
| PR instruction | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md` (PR-10, INSTRUCTION_READY) |
| Per-PR plans | v1.0 (lineage only); v1.1 (Proceeded) |
| Rescope | request v1.0; RS-20 review v1.0 (APPROVE); PF10 addendum 2.2 (record `docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md`) |
| Security-review deprecation | PF10 addendum 2.3 (record `docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md`), carried by #627 at the Product Owner's direction |
| Results | PR-30 v1.0; PR-35 v1.1 to v1.15 (v1.15 final) |
| Effective scope | approved base plus PF10 addendum 2.2; reviewer chain read under addendum 2.3 |

The work-unit input records (instruction, plans, rescope request and review, addendum 2.2 record) have identical blob IDs at the base `e3a5ed4` and at `7136040`. #627 did not change them.

## 3. Merge state and landed lineage

| Fact | Evidence |
| :- | :- |
| Merged | GitHub: `merged=true`, `merged_by amthorn78`, `merged_at 2026-10-13T11:12:51Z`, `merge_commit_sha 7136040821fe…` |
| Method | SQUASH. `7136040` has one parent, `e3a5ed4` (the PR base) |
| Head | `b6206faac1441c258bb741b82a6f81298ebdc8be`; `e3a5ed4` is its ancestor; 31 commits, no merge commits |
| Tree equality | `7136040^{tree}` = `b6206fa^{tree}` = `8b0cec5f4debea67ecc794d1014e9aab85cd01d4` |
| Later divergence | none: `origin/main` = `7136040`, 0 commits after it; post-merge push CI run 38388669208 on `7136040`: success |
| Commit order | PR-30: `26140fe` (implementation), `68d9207` (result v1.0). PR-35: 13 correction commits (`c5116f7`, `ea4d72e`, `dd91ed3`, `5c196ad`, `1d588de`, `731d970`, `02dfdde`, `34dbc70`, `175bc56`, `6e6fe7f`, `fe924d3`, `65ee506`, `97902d8`), one canon commit (`9954b11`, PF10 v13.5.4) and 15 record commits (results v1.1 to v1.15). Every cited commit/tree pair in the records matches git |
| Last code commit | `97902d8` (tree `9269d85`), the parent of `b6206fa`, which adds only result v1.15 |

### Merged-change attribution

Produced with the `glow-merged-change-attribution-lock` skill (revision 1.2.0, interface `GLOW-MERGED-CHANGE-ATTRIBUTION-082826.3`, `SHADOW_VALIDATION`), LOCAL_GIT mode, read-only invariant held.

| Field | Value |
| :- | :- |
| Comparison SHA | `7136040821fe5deab5992a00ba8275644b1e7aca` (`refs/remotes/origin/main` = HEAD) |
| Attributed change | amthorn78/glow-hdengine-v2#627 |
| Run key | `auto-d9ffc52bd3f31ed3fdab7388` |
| Reconciliation | **EXACT**: direct and landed binary deltas share SHA-256 `076cc6e7272726154788968512119ae75c185247e43c79121ff9151eebb2101a` |
| Landed delta | 118 files, +5,613/−6,391 with rename detection (119 paths without: 19 A, 67 D, 33 M) |
| Later committed / worktree divergence | none / none |
| Unproven items or stops | none; validator exit 0; final line `END MERGED CHANGE ATTRIBUTION: VALIDATED` |
| Shadow comparison with this review's native result | agrees: same merge, base, head, tree and absence of divergence |

**Attribution by content.**

| Class | Paths |
| :- | :- |
| WU-PR-01 deliverables (base scope) | `.github/workflows/ci.yml`; `ci/checks/classify_ci_changes.py`; `pytest.ini`; 66 deleted test files; `tests/retired_tests.md`; 28 modified test files (27 "retain + fix" rows plus `tests/evidence/test_rails_ci_workflow_integration.py`) |
| WU-PR-01 deliverables (addendum 2.2) | `tools/evidence/generate_hdapi_v2_contract_inventory.py`; `tools/evidence/hdapi_v2_boundary_analyzer.py` |
| Work-unit records | 16 result records (v1.0 to v1.15) |
| Product Owner-directed content outside the unit's deliverables | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md` → `v13.5.4` (R078; version, date, one index line, addendum 2.3) and the addendum 2.3 record (PO-D2, PO-D3; CR-5) |
| Unrelated or unattributable | none |

## 4. Reviews, checks and corrected-change coverage

**Codex code review.**
- 15 Codex reviews ran, the first on `26140fe` and the last on `b98f315`.
- They opened 21 threads (R-1 to R-22; R-6 is PR-35's own and has no thread). All 21 are resolved, and each carries a reply naming its correction commit or its Product Owner decision.
- 18 findings were corrected. Three are recorded as limits: R-14 (PO-D4), R-16 (PO-D6) and R-21 (PO-D7).
- PR-35's same-family findings (R-3b, R-6, R-9b, R-11b, R-12b, R-13b, R-15b, R-18b, R-19b, R-20b, R-22b) map to their correction commits.
- The final Codex code review, on `b6206fa`, completed at 09:59:19Z with no findings: the bot reacted +1 at 09:59:22Z. `b6206fa` adds only a record over `97902d8`, so the last corrected code is covered by that review.

**Codex security review.**
- Requested once (comment 6135990857, 01:19:59Z) and never produced.
- PO-D1 ("Waive it for #627") waived it for #627, and PF10 addendum 2.3, now on `main`, deprecates it.
- Under addendum 2.3 Rule 2, its absence is not a gap, finding or blocker for this lineage review. Instruction §11's security constraints still apply and are checked in §5.

**Hosted CI.**
- 17 runs on the branch. Each head, run ID and conclusion matches the records, except the record statements in LR-3.
- Final head `b6206fa`, check `test`, run 38379706424: **success**. It checked out `b6206fa` and ran all seven lanes (product 77; compat 102 passed, 3 skipped, 2 xfailed; db 249; rails 137; evidence 113; qa 488; release 64 plus attestation). The changed-test step passed 3,264 tests. `CI_APPLICABILITY_AND_EXACT_HEAD_OK` is at job-log line 880.
- One failure: run 38344773095 on `496e2c7`. It failed `tests/qa/test_generate_epic_close_pack.py::test_manifest_reader_rejects_new_report_with_old_manifest` (`CHECK_MODE_MUTATION`). That test and its tool are byte-identical to `main` (OBS-17). The run was never re-run (run_attempt 1), and the next push passed.
- No CI waiver exists or was needed. `main` has no required status checks.

**Merge readiness (v1.9 §2 predicates on `b6206fa`).** All three held:
- P-1: 21/21 threads resolved.
- P-2: current-head CI success with the marker.
- P-3: mergeable and clean per the API at 10:14Z, and the merge landed with tree equal to the head tree.

**Independent validation by this review.**
- Tested state: `7136040`, tree `8b0cec5f`.
- Environment: a scratch clone with Python 3.12.3 and CI's install (`requirements.txt`, `requirements-dev.txt`, `-e .`); ruby 3.3.6; closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, vendor, geocode and database keys unset).
- The main checkout was not executed in, and stayed unchanged.

| # | Check | Result |
| :- | :- | :- |
| V-1 | Classifier, `e3a5ed4`→`7136040`, pull_request and push | exit 0; 119 paths; seven lanes; 163 targets (identical for both events) |
| V-2 | Changed-test step exactly as `ci.yml` runs it | 3,264 passed, 0 failed/skipped/xfailed, 316.69 s, exit 0; `git diff --exit-code` 0; status empty; the 11 same-byte rewrites of OBS-4 only |
| V-3 | Default `pytest.ini` testpaths | 2,551 passed, 3 skipped (showcompat vendor calls need open rails), 276.47 s, exit 0, clean |
| V-4 | `python3 ci/checks/check_agents_md_citations.py`; `ci/checks/check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK` exit 0; `[env-pins] OK` exit 0 |
| V-5 | `tests/qa/test_generate_epic_close_pack.py`, three runs | 405 passed each time (local git 2.43.0, so OBS-17's suspected git ≥ 2.47 cause is not exercised) |
| V-6 | Integration, architecture guards, legacy imports, contract inventory | 137, 4, 2 and 300 passed |
| V-7 | Instruction §5.1 coverage computation | head: 212 tracked, 49 lane-reached, 163 full-validation targets, **0 uncovered**; base: 278, 94 targets, 135 uncovered (equal to the plan's 135 rows) |
| V-8 | S05 filter equivalence | both `ci.yml` filters equal the list derived from `_DOCUMENTATION_PREFIXES` and `docs/evidence/INDEX.json`; 7,966 tracked paths and 91 synthetic paths, 0 mismatches |
| V-9 | S04 refusal | head: unregistered `tools/qa/` `.py`, `.sh`, `.sql`, `.SH`, `.SQL` refused with `CI_QA_OWNER_TEST_MISSING`; base: `.sh`, `.sql`, `.SH`, `.SQL` passed |
| V-10 | Addendum 2.2 bounds | generator: only `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` data changed (21 records, equal to what the stated rule derives; no `reader_v1_post`); analyzer: only `_adapter_routes_without_presenter` changed; import nodes identical in both tools; governed-path diff empty; production loci clean at head (base reports `adapter/http_reader.py:reader_post`); the negative test's 46 shapes and 21 further base-reported probes stay reported, except the R-14/R-21 helper class (LR-4) |

## 5. Requirement and obligation coverage

| Obligation (source) | Status | Evidence |
| :- | :- | :- |
| S03 "No test file runs in no CI lane; each retirement has a recorded reason; recorded failures and collection errors are fixed or retired" (Specification) | MET | V-7; 66 deleted = 66 plan retire rows = 66 ledger rows (path, reason, date 2026-10-13, replacing coverage); 69 retained files registered and passing (V-2, V-3) |
| S04 (Specification) | MET | V-9; unit test in `tests/evidence/test_rails_ci_workflow_integration.py` |
| S05 (Specification; EC-1) | MET | V-8; docs-only dry run gives `documentation_only`, no lane; governed primaries keep the evidence lane |
| Acceptance (1) to (5) (whole-change Plan v1.1 §7; instruction §10) | MET | (1) V-7 and ledger; (2) hosted changed-test step in a detached worktree with clean diff and status, plus V-2; (3) V-9; (4) V-8; (5) run 38379706424 |
| Deliverables (instruction §6; plan v1.1 §8) | MET except one | every path present; **the plan v1.1 §5.4/§5.5/§8 synthetic inactive-refusal case is missing (LR-1)** |
| Interface contracts C-1 to C-6 (instruction §8) | MET | C-1 `tests/bodygraph/test_resolver_vendor.py` and C-2 `tests/adapter/test_gate_auth.py` retained and registered; C-3 definition unchanged (O-1); C-4 lane names and steps unchanged; C-5 no member change, manifest `1.3.0`, `release_id_recompute.py --check-manifest-only` exit 0; C-6 S04 rule mirrors the bodygraph rule |
| Disposition rules §9.1 to §9.9 (instruction) | MET | one disposition per file; N2 criterion stated and applied; 14 legacy-import files retired; tracked-write fixes; consumers kept (`test_internal_version_manifest_captures.py`, `test_aux_preview_identity_parity.py`, `test_resolver_vendor.py`); inactive set resolved; 22 undiagnosed failures diagnosed in plan v1.1 (F-5, row 76); RP-2 loader retirement ledgered honestly |
| Exclusions (instruction §7) | MET, with one Product Owner-directed variance | no member, `scripts/**`, `ci/jobs/*`, governed-artifact, QA-artifact, `AGENTS.md` or `README.md` change; `tools/**` limited to the two addendum 2.2 files; no skip, xfail or quarantine added in any retained file (one `pytest.skip` call removed, in `tests/adapter/test_env_guard_import_purity.py`); "no canon edit": PF10 v13.5.4 carried at PO direction (CR-5) |
| Addendum 2.2 binding requirements (B-1 to B-14) | MET, with LR-4 | V-10; ruby needed and present (hosted presence inferred from the passing file; version not printed) |
| Security (instruction §11; addendum 2.3 Rule 3) | MET | `permissions: contents: read`, exact-head checkout, isolation unchanged; no governed primary or path proof skipped; S04 only narrows; every retired security-relevant test names a replacing test or a reason; no credential value in the added lines |
| Migration and rollback (instruction §11) | MET, with CR-5 note | no data, schema or member change; reverting `7136040` would also remove PF10 v13.5.4 and addendum 2.3 |
| Evidence obligations (whole-change Plan; plan v1.1 §13) | MET | result v1.0: inventory 135/130 → 0, the 135-row table, checks with counts, lane counts, ruby version, RP-1/RP-2 evidence, nonclaims; sweep summary by reference to plan §4.2 (base content-identical) |
| Documentation obligations | none for this unit | `AGENTS.md`/`README.md` belong to WU-DOC-01 (O-4) |
| Engineering, review, CI and merge (instruction §12; read under addendum 2.3) | MET | two dedicated sessions; Codex code review resolved; current-head CI green; Nathan merged |
| PR description (AGENTS.md; instruction §12) | template headings and nonclaims present; **one false claim (LR-2)** | |
| Recovery (instruction §13) | none open | no interruption state; `PR_RETURN_PHASE: none` throughout |
| Nonclaims (Plan; instruction) | MET | no QA, PF09 or acceptance claim in the records or PR body |

## 6. Findings

| ID | Finding | Severity | Requirement | Evidence | Owner and route |
| :- | :- | :- | :- | :- | :- |
| LR-1 | The planned monkeypatched synthetic inactive-refusal test case was never added. The refusal `CI_INACTIVE_TEST_REQUIRES_DISPOSITION` (`ci/checks/classify_ci_changes.py` line 1533) is now untested | Precise in-scope defect; not material to acceptance (1) to (5); **basis of REJECT** | Plan v1.1 §5.4 last bullet ("the `CI_INACTIVE_TEST_REQUIRES_DISPOSITION` mechanism stays, with a monkeypatched synthetic case so its pinned loop is not vacuous"), §5.5 ("Inactive refusal case: §5.4"), §8 (the integration file's change set includes "inactive-refusal tests") | `tests/evidence/test_rails_ci_workflow_integration.py` lines 1152–1156 loop over `classifier._FULL_VALIDATION_INACTIVE_TESTS`, which is `set()` (classifier line 152), so the loop asserts nothing. `git log -S'CI_INACTIVE_TEST_REQUIRES_DISPOSITION' e3a5ed4..b6206fa -- tests/` returns no commit. No PO decision or record sets the case aside. Confirmed by two independent adversarial verifiers and by this reviewer | PR-20 (new dedicated WU-PR-01 session), corrective plan, then Product Owner Proceed, PR-30, PR-35, PR-40 (§10) |
| LR-2 | The PR record states the missing test exists | PR-lineage defect (record) | AGENTS.md "Evidence attribution": record actual results | PR #627 body, "What changed": "new coverage, S04, S05 and inactive-refusal tests"; result v1.0 §4 records plan v1.1 §8 as applied | Corrected by a new result record in the corrective unit; historical records stay unchanged |
| LR-3 | Two CI statements in the PR-35 records do not match hosted CI | PR-lineage defect (record); no conclusion changes | AGENTS.md "Evidence attribution": never relabel a run | (a) Result v1.5 §2 calls run 38336691078 on `bb0f85c` stale and about to be cancelled by `cancel-in-progress`. It had completed **success** at 02:35:56Z, before the next push. No later record states the outcome, and the PR body's "passed" list omits `bb0f85c`. (b) Result v1.9 §4 says the close-pack code "passed on f134651 and every earlier head", but the runs on `26140fe` and `e13516b` were cancelled | Corrected by the same new result record |
| LR-4 | R-14, a helper shape the base analyzer reports and the merged analyzer accepts, was settled as a limit by PO-D4 without the rescope lane that addendum 2.2's Binding requirements name, and that option was not offered. PO-D4 carries no verbatim Product Owner wording | Procedural; not a defect in the landed code against the Proceeded plan | PF10 addendum 2.2 "Approved delta" item 2 and "Binding requirements" ("If the analyzer change cannot be made without weakening bypass detection, that is a new finding to the Implementation Agent through the rescope lane") | Probes: R-14 and R-21 helper shapes are reported at the base and accepted at the head. Their direct-view analogues are accepted at both, and the base also reports the sanctioned production helper, so the base's report comes from not following the parameter, not from detecting the mechanism. Plan v1.1 §5.8.2 proves helper returns as direct views are proven. For R-21 the rescope lane was offered and declined (PO-D7, question answered 09:29:54Z); for R-14 it was not (referral 04:16:46Z, decision posted 04:24:35Z) | CR-4: Nathan / Product Owner confirms PO-D4 as his bounded decision for exactly R-14, or routes R-14 to the rescope lane. Not part of the LR-1 correction |
| LR-5 | PF10 v13.5.4 was carried inside an implementation PR | Variance directed by the Product Owner; not a WU-PR-01 deliverable | PF06 §0.2 ("Coding agents and Implementation Agents MAY NOT directly modify PF-Canon documents as part of implementation PR work"); instruction §1 and §7 ("no canon edit"); Plan v1.1 §7 nonclaim "no canon change" | PO-D3 ("add this updated PF10 version to your current PR and remove the old one", result v1.6 §4) gives exact authority for this document and action under PF04 §9.1.2 and AGENTS.md. Only `9954b11` touches `docs/pfcanon/`; bytes match the stated sha256. Reverting `7136040` would also remove addendum 2.3 | CR-5: Product Owner |

**Observations** (facts to carry; no WU-PR-01 obligation is unmet):

| ID | Observation | Owner |
| :- | :- | :- |
| O-1 | The coverage guard `test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target` scans every `tests/` token anywhere in `ci.yml`, a wider set than §5.1's "token in a `python -m pytest` command" wording. Today both sets are the same 39 tokens | IA: state the definition in the WU-PR-06 instruction (C-3) |
| O-2 | Retired `tests/evidence/test_hdapi_v2_live_conformance.py` and `test_hde_epic037_field_sufficiency.py` also tested their historical generators' fail-closed paths. Those generators now have no test, but an edit to them still fails classification (`CI_EVIDENCE_OWNER_TEST_MISSING`). `AGENTS.md` still names the EPIC037 generators as validation entrypoints | Product Owner and IA, awareness; WU-DOC-01 for operative wording |
| O-3 | `tools/evidence/generate_architecture_snapshot.py --check` reports STALE at both base and head, with identical differences that do not involve either addendum 2.2 tool. It predates this PR, and no CI step runs it | Product Owner, for the canonical writer's owner |
| O-4 | OBS-11's stale references are still present: `docs/RUN.md:9` and `docs/ADAPTER_009.md:115` (`tests/test_sercanon.py`), and `README.md:218` (`tests/qa/test_epic022_acceptance_scaffold.py`). The first two files are outside WU-DOC-01's planned bounded scope | IA: carry into the WU-DOC-01 instruction, naming both paths |
| O-5 | OBS-17: intermittent hosted failure of the close-pack test, with a proposed test-side patch in the PR conversation. It can fail later units' CI | QA tool and test owner, through the IA; Product Owner to route |
| O-6 | Unverified hosted behaviours: whether `**` in `on.paths` matches dot-prefixed paths (`.github/`, `.claude/`, `.gitignore`); that a documentation-only PR starts no hosted run; the hosted ruby version (not printed in the log) | IA, observed at the next relevant unit's CI |

**Carried items and owners** (from the records, unchanged by this review):
- **Whole-change IA:** OBS-16 (a) to (l), R-16, R-21, OBS-1, OBS-3, OBS-4, OBS-5, OBS-7, OBS-9, OBS-13 and OBS-14. Also WU-PR-03 baseline currency for the contract-inventory generator and the WU-PR-06 sweep's ruby requirement (addendum 2.2 "Downstream work").
- **WU-PR-04 owner:** OBS-2 and OBS-6.
- **WU-DOC-01:** OBS-8. OBS-10 goes to whichever unit next edits the source.
- **Product Owner:** OBS-12, and ruby after the move to Ubuntu 26.04. HDE-SEPA006 (the legacy chart-loader defect). Whether the review chain needs another source of security review, and HDE Governance §9.1.1 wording (addendum 2.3).
- **GCFPE-MGMT-10 and the Product Owner:** GCFPE prompt and skill wording that still names the Codex security review.

## 7. Truthful NOT PRODUCED, NOT EXECUTED and pending values

- **NOT PRODUCED**:
  - a saved PR-35 `MERGE_OBSERVED` artifact (the event is in the handoff only);
  - any QA, Ops, acceptance or closure artifact (outside PR-40);
  - a PF10 addendum (PR-40 is not a qualifying prompt).
- **NOT EXECUTED**:
  - the Codex security review (deprecated, addendum 2.3);
  - a hosted reproduction of OBS-17;
  - individual one-file runs of each retained file at the final head. All 69 retained files ran as part of V-2 and of hosted run 38379706424, and PR-30's single-file runs cover identical bytes for the 66 files unchanged after `26140fe`.
- **UNVERIFIED**:
  - the Product Owner's own wording for PO-D4 and PO-D5 (LR-4);
  - that the committed PF10 bytes are the exact file the Product Owner supplied (only agent records assert it; sha256 matches the recorded value);
  - O-6.
- **Pending**:
  - CR-4 and CR-5 (Product Owner);
  - the corrective unit (§10).
- **Prompt-use provenance**: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent. Usage is kept in §12 of this artifact; repository persistence is pending its authorized installation and is not gating.
- **Scratch side effects**: ignored-only files (`.pytest_cache/`) in the scratch clone; none in the repository checkout.

## 8. Product Owner decisions in the lineage

| ID | Decision | Product Owner wording in the records | Status in this review |
| :- | :- | :- | :- |
| PO-D1 | Codex security review waived for #627 | "Waive it for #627" (v1.6 §3; PF10 v13.5.4 addendum 2.3) | carried |
| PO-D2 | Codex security review deprecated; addendum 2.3 | quoted in addendum 2.3 "Source and authority" | carried; in force on `main` |
| PO-D3 | PF10 v13.5.4 replaces v13.5.3 on #627 | "add this updated PF10 version to your current PR and remove the old one" (v1.6 §4) | carried; CR-5 |
| PO-D4 | R-14 recorded as a limit | none verbatim; options offered: limit, allowlist, cross-module analysis | **confirmation pending (CR-4)** |
| PO-D5 | CI failure on `496e2c7` re-run by the next push | none verbatim | carried; consistent with run_attempt 1 |
| PO-D6 | R-16 recorded as a limit | answer to the question at 09:29:54Z, "Record as a limit (Recommended)" | carried |
| PO-D7 | R-21 recorded as a limit; the rescope lane was offered and declined | as PO-D6 | carried |

## 9. CANON_CONFLICT_REGISTER

Carried unchanged from the Specification, Plan and instruction: **CR-1**, **CR-2**, **CR-3** (CANON_RECONCILIATION; APPROVED_AS_CHANGED by Thoth; interim treatments as recorded in instruction v1.0 §16). None is touched by this work unit.

The PR-35 records (v1.1 to v1.15) do not restate the register. This review restates it and records two evidenced candidates. It decides neither; the review fields below stay unreviewed until the native owner decides.

**CR-4. PO-D4 versus the addendum 2.2 rescope-lane route.**
- **Classification:** CANON_RECONCILIATION.
- **Conflicting sources:** PF10-HDE-Build-Notes v13.5.4 addendum 2.2, "Approved delta (RP-1)" item 2 and "Binding requirements" (route a weakening to the Implementation Agent through the rescope lane). Against it, PO-D4 (result v1.9 §5), an in-session Product Owner decision recorded without verbatim wording.
- **Statement:** a case the addendum routes to the rescope lane was closed by a recorded Product Owner decision instead.
- **Affected requirement:** S03 via addendum 2.2 (no-weakening bound).
- **Alternatives:**
  - (a) Product Owner confirms PO-D4 as a bounded Product Owner decision for exactly R-14 (AGENTS.md: a formally approved bounded Product Owner rescope supersedes for the exact decision it adjudicates);
  - (b) R-14 enters the rescope lane (RS-10/RS-20) as a merged-but-unaccepted finding.
- **Recommended disposition:** (a). Reasons: the direct-view analogue is unreported at the base; PO-D7 made the same choice for the same class with the lane offered; and the plan's helper proof equals the view proof.
- **Interim treatment:** the landed analyzer stands; R-14 stays an IA-owned analyzer limit (OBS-16).
- **Unresolved risk:** the authority for PO-D4 is agent-recorded only.
- **Drainage target and owner:** Product Owner; PF10 if a later addendum is wanted.
- **Status:** PROPOSED.
- **Reviewer/session, reviewed artifact, decision time, rationale:** not yet reviewed.

**CR-5. Canon replacement inside an implementation PR.**
- **Classification:** CANON_RECONCILIATION.
- **Conflicting sources:** PF06-Canon-Change-Process-Guide v2.5.4 §0.2 ("Coding agents and Implementation Agents MAY NOT directly modify PF-Canon documents as part of implementation PR work"). Against it: PF04-Canon-HDE-Governance v2.8.7 §9.1.2 ("agents may edit PF canon only under the Product Owner's exact authority for the identified document and action"), the `AGENTS.md` canon read-only rule, and PO-D3.
- **Statement:** PO-supplied PF10 bytes were committed by the PR-35 agent within the WU-PR-01 implementation PR. PF04 and `AGENTS.md` permit that under exact Product Owner authority; PF06 §0.2 forbids canon edits in implementation PR work without an exception.
- **Affected requirements:** none of S03 to S05. It affects the rollback coupling of `7136040`.
- **Alternatives:**
  - (a) PF04 §9.1.2 exact Product Owner authority governs, and the landed change stands;
  - (b) such replacements go in a separate PR or direct-main change.
- **Recommended disposition:** (a) for this case. For later units, state the preferred vehicle.
- **Interim treatment:** PF10 v13.5.4 is the controlled PF10 on `main`.
- **Unresolved risk:** a revert of `7136040` would also remove addendum 2.3.
- **Drainage target and owner:** Product Owner.
- **Status:** PROPOSED.
- **Reviewer/session, reviewed artifact, decision time, rationale:** not yet reviewed.

## 10. Route and next stage

**REJECT → PR-20 — Create Detailed PR Implementation Plan — 100926.1**, for the same `WORK_UNIT_ID` WU-PR-01, in a new dedicated top-level session that Nathan creates. The plan then goes through its own Product Owner Proceed, PR-30, PR-35 and PR-40. The earlier Proceed is spent and is never reused. #627's merge and review evidence are preserved and not reopened.

**Bounded correction** (the whole corrective scope; the effective baseline remains the approved base plus PF10 addendum 2.2, with the reviewer chain read under addendum 2.3):
1. `tests/evidence/test_rails_ci_workflow_integration.py`: add the monkeypatched synthetic inactive-path case that plan v1.1 §5.4 commits to. It sets a synthetic path into `classifier._FULL_VALIDATION_INACTIVE_TESTS` and asserts that `classifier.changed_test_targets` refuses it with `CI_INACTIVE_TEST_REQUIRES_DISPOSITION`. Test-only; no classifier, workflow, tool or production change.
2. A new PR result record under `docs/ephemeral/` that states the actual facts behind LR-2 and LR-3. Historical records and #627's description stay unchanged.

**Outside the correction:**
- R-14 (CR-4, Product Owner).
- CR-5 (Product Owner).
- O-1 to O-6 and the carried items, which stay with their owners.

The corrective PR changes a full-validation path, so every lane runs.

**Next unit.** WU-PR-02's instruction is not issued by this review. Instruction v1.0 §12 issues it "on ACCEPT", and PR-40 selects a next unit only after a complete accepted delivery. WU-PR-02 is otherwise dependency-ready: whole-change Plan §7 says "Second; no code dependency on WU-PR-01", no overlay adds a prerequisite, and no WU-PR-02 instruction exists. It becomes the next stage (PR-10) when the corrected WU-PR-01 lineage is accepted.

## 11. TypeSafe reading for the receiving session (PR-20, WU-PR-01 corrective plan)

Action sent (v6): "Write, in a new dedicated session, a corrective detailed PR implementation plan for an already merged CI-coverage work unit whose independent lineage review rejected it for one precise defect: a planned monkeypatched test case for one classifier refusal path was never added, and the merged PR's description claims it exists. The plan covers adding that one test-only case to an existing 2,100-line test file and a new result record that corrects two record misstatements, with no production code, workflow or classifier change; it goes to the Product Owner for Proceed, then implementation, code review and another lineage review. No live run occurs."

- **TypeSafe v6: Opus 5.5, high.**
  - Effort score 1.79 (confidence 0.83).
  - Rung probabilities: low 0.01, medium 0.22, high 0.75, extra high 0.02, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.99 (confidence 0.98).
  - Twelve cells, computed from the two answers: Opus 5.5 at low 0.01, at medium 0.22, at high 0.74, at extra high 0.02, at max 0.00, at ultracode 0.00; Fable 5.1 at low 0.00, at medium 0.00, at high 0.01, at extra high 0.00, at max 0.00, at ultracode 0.00.
  - Sent 2026-10-13T12:44:27Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T12:44:27Z; HTTP 200 in 0.69 s; 4241 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (Fable 5.1 only when P(most capable) is 0.5 or more). Flags printed by the script: none.
- **Notion row:** not written, as PR-40 directs.
- **Nathan's pick for PR-20:** not stated.
- **Nathan's pick for this PR-40 session:** not stated. The handoff's reading for PR-40 was Opus 5.5, extra high, recorded in result v1.9 §7.

**Surface advice.** Run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access.
- Reads: this review, instruction v1.0, plan v1.1 (§5.4, §5.5, §8), result v1.0 and v1.15, `ci/checks/classify_ci_changes.py` and `tests/evidence/test_rails_ci_workflow_integration.py` on `main`.
- Writes: only its plan under `docs/ephemeral/`.
- Test run: closed rails with Python 3.12, CI's install and ruby on PATH, in a throwaway copy, if it prototypes the case.
- No live vendor, production or database access.
- This review's pull request should be merged to `main` first.

## Canon relied on

Read on `main` at `7136040` (`docs/pfcanon/` changed only by the PF10 rename in #627). Each decision topic maps to the sections below.

**Review authority, decision values and routes:**
- PR-40 — Review PR Work-Unit Lineage — 100926.1 (read in full);
- PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (PR implementation authority; normal code/security/review and evidence chain; Product Owner merges);
- PF04 §9.1.2 (canon precedence; in-flight reviews and Product Owner dispositions govern within scope);
- PF04 §9.1.4 (tested state versus later commits);
- PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use" and "Source-bound review authority and exact-fix limits".

**Merge evidence, lineage and CI scope (§3, §4):**
- PF06-Canon-Change-Process-Guide v2.5.4 §0.2 (traceability through base, head and merge; the Product Owner squashes; a valid reduced lane set from the classifier is sufficient CI scope), §0.3, §0.4, §4.2 to §4.4;
- PF27 "CI lane classification and automated budget-control discipline";
- PF04 §4.3 and §4.3.9;
- PF19-Canon-Glow-QA-Guide v3.0.6 §10.8 "Commit progression and substantive review", "Claim separation, CI and integrity".

**Requirement coverage (§5):**
- the Specification's S03, S04, S05 rows and the "Uncovered tests" constraint;
- whole-change Plan v1.1 §7 WU-PR-01 and the common paragraph;
- instruction v1.0 (all sections);
- plan v1.1 §4 to §8, §13, §17 to §19;
- permanent canon has no test-retirement rule. PF10 addendum 2.2 RP-2, S03 and the instruction govern it (searched: PF04, PF06, PF19, PF23, PF27).

**Addendum 2.2 bounds (V-10; LR-4; CR-4):**
- PF10-HDE-Build-Notes v13.5.4 addendum 2.2 in full;
- RS-20 review v1.0 §6 (B-1 to B-14);
- the addendum 2.2 record.

**Security review (§4; LR-1 scope):**
- PF10 v13.5.4 addendum 2.3 in full. Rule 2 names "a lineage review"; Rule 3 keeps the Codex code review and every other security obligation.
- Permanent canon names no Codex security review (searched).

**Canon edit in the PR (LR-5; CR-5):**
- PF06 §0.2 (implementation agents may not modify PF-Canon in implementation PR work);
- PF04 §9.1.2 (exact Product Owner authority);
- `AGENTS.md` "PF canon is read-only unless the prompt explicitly directs a change".

**PF10 authority and silence:**
- PF10 v13.5.4 read in full: Front Matter, Precedence §1 to §9, Template, Addendum Index, addenda 2.1, 2.2, 2.3;
- addendum 2.1 governs §11 only;
- PF10 is silent on PR-40's decision values.

**Operative documentation:** `AGENTS.md`, including:
- canon-first rule;
- closed rails;
- pytest readiness;
- evidence attribution;
- PR descriptions;
- code-review scope;
- truncation guardrail.

**In-flight documents read in full:**
- instruction v1.0;
- per-PR plan v1.1;
- results v1.0, v1.9 and v1.15;
- the addendum 2.2 and 2.3 records;
- Plan review v1.1.

**In-flight documents read in the sections cited:**
- results v1.1 to v1.8 and v1.10 to v1.14;
- rescope request and review v1.0;
- Specification v1.1;
- Audit v1.0 (§3, §5.2, §5.3, §5.7, S03 to S05, Appendix A);
- whole-change Plan v1.1 (§3, §4, §7, §9 to §11, §13).

**Not read; no decision rests on them:** PF01, PF02, PF14 (no product behavior in scope); PF20 and PF23 (historical only).

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-01 / PR-40 / lineage review 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| work unit | WU-PR-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f |
| role/stage | whole-change IA / PR-40 lineage review |
| capture time | 2026-10-13T12:44:32Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| repository persistence | recorded here only (installed writer absent; pending, non-gating) |

**Decision: REJECT.**
