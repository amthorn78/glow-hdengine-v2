---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-03-PR-IMPLEMENTATION-RESULT
artifact_version: "1.1"
result_state: RESCOPE_PENDING
phase: PR-35 (review resolution and merge readiness); this record is the checkpoint at the rescope boundary and for PR-35's first corrective push
PR_RETURN_PHASE: PR-35
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; preserved unchanged)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; overlaid by addendum 2.6 for the clauses rescope review v1.0 §7.1 B-2 names)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (v1.1, Proceeded)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md (v1.0, RS-20, APPROVE; B-1 to B-12)
RESCOPE_REQUEST_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0.md (v1.0, RESCOPE_REQUEST_PENDING_REVIEW; RP-4, RP-5); companion docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0-prototype.diff
REMEDIATION_REVIEW_ID: none
effective_baseline: approved base (Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0) + PF10 addenda 2.2, 2.3, 2.5 + addendum 2.6 (record docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md on main 1735d94 (blob 9c5468fb69e4; sha256 8663ab94289adae0…; read in full by this session, 501 lines to <eof>); the pull request carries the Product Owner-directed docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md (sha256 dfb4478c88d712a9205b0d0907c77212eb5de9a86334d9f0235c7d0cb5748123; unmerged), which adds §2.6 only. Provenance, not a gate
proceed: Nathan / Product Owner's original PR-30 — PR Implementation Proceed — 100926.1 for exactly plan v1.1 (result v1.0 front matter). PR-35 continues under it; no other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-03 PR-35 session, https://claude.ai/code/session_0136SjBtuTJwoEpceUd46T6C; session_disposition NEW_DEDICATED (top-level session Nathan created from PR-30's handoff); role_session_ref NOT_YET_ASSIGNED (Nathan assigns)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15Z; read in full); primary skill glow-hde-pr-development 1.4.0
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2 (cloud container)
pull_request: amthorn78/glow-hdengine-v2#643 (open, not draft, base main 1735d94; head branch claude/nifty-cray-w86vmp)
pr_subscription: active (subscribe_pr_activity confirmed delivery of #643 events to this session at entry)
commits_this_phase: 3a1b0a7 (Codex P2 correction); the record commit that adds this file, the rescope request and its companion (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-6 carried unchanged; CR-7 and CR-8 PROPOSED by the rescope request (§7 there)
created_at: 2026-10-14T04:05:00Z
next_phase: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c) in the continuing whole-change IA session
---

# HDE-CRD-0002 WU-PR-03 — PR Implementation Result v1.1 (PR-35, RESCOPE_PENDING)

## 1. Result

**RESCOPE_PENDING.** The Codex code review of [amthorn78/glow-hdengine-v2#643](https://github.com/amthorn78/glow-hdengine-v2/pull/643) raised three findings:
- **F1 (P2, aliases off the Aux record):** an ordinary in-scope correction. Fixed in `3a1b0a7`, locally validated (§5) and pushed with this record.
- **F2 (P1, exact `APP_ENV=dev`):** contradicts the IA's binding instruction §9.2 and rescope review v1.0 B-6. Routed to RS-20 as RP-5.
- **F3 (P1, retired diagnostic routes in the catalog):** HDE Architecture §3.5 excludes the three routes from the Endpoint Catalog; instruction ID-1 and §14 name this exact case as an RS-20 boundary finding. Routed to RS-20 as RP-4.

The rescope request is `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0.md`. Only the work F2 and F3 affect is stopped. The pull request is not merge-ready: two Codex threads stay open pending the IA's decision. Nothing is merged; no QA, acceptance or closure is claimed.

## 2. Entry and recovery

| Check | Observation |
| :- | :- |
| Handoff | PR-30's `NEXT_PROMPT_HANDOFF` pasted by Nathan: PR-35, `session_disposition: NEW_DEDICATED`, #643, the ten inputs; all present at their paths |
| Pull request | #643 open, not draft, base `main` `1735d94`, head `claude/nifty-cray-w86vmp` at `b178f03` (= result v1.0's record commit); 6 commits, 84 files; `mergeable_state: unstable` (checks pending at entry) |
| Local root | one worktree `/home/user/glow-hdengine-v2`, clean, on the harness-designated branch `claude/pr-35-merge-readiness-lf9t2g` at `1735d94` (= `main`; no commits of its own; remote branch also `1735d94`) |
| Continuity (GCF-17) | same `WORK_UNIT_ID`, original Proceed, workspace, branch (`claude/nifty-cray-w86vmp`), pull request, instruction v1.0, plan v1.1, primary skill and lineage (result v1.0 → this v1.1) as PR-30 |
| Vehicle decision IF-35-1 | The session's harness named `claude/pr-35-merge-readiness-lf9t2g`; the pull request's head is `claude/nifty-cray-w86vmp`. PR-35 continues the existing pull request (Nathan's handoff: "continuing the existing pull request"), and GCF-17 allows one branch per plan cycle, so PR-35 checked out `origin/claude/nifty-cray-w86vmp` and pushes there, as the WU-PR-01 and WU-PR-02 PR-35 sessions pushed to their PR heads (WU-PR-02 result v1.1 §2). The designated branch is left untouched |
| Subscription | `subscribe_pr_activity` on #643: confirmed |
| Prompt | PR-35 — 100926.1 read in full from Notion; RS-20 — 100926.1 read in full (receiver contract) |

## 3. Review matrix

Reviews read: Codex code review `5512796236` on `2d26e2b` (03:42:31Z) and `5512813453` on `b178f03` (03:45:27Z), both `COMMENTED`; summary comment `6160341482` ("Code Review Completed" on `b178f03`, trigger "New commits"). No security review exists (deprecated, addendum 2.3). No human review.

| ID | Thread / comment | Location, head | Finding | Classification | Disposition |
| :- | :- | :- | :- | :- | :- |
| F1 | `PRRT_kwDOP103ks6sJ2D_` / 4266534756 (P2) | `tools/evidence/generate_a7_transport_proofs.py` L88, `2d26e2b` | `aliases` were rejected only off `public_aux` records, so a second record reclassified `public_aux` could carry an alias | substantive, in scope (S15 validator; plan §6.5 "the Aux record is pinned by path"; the test is named "…rejects aliases off the Aux record…") | fixed in `3a1b0a7` (D-4); thread answered and resolved after the push |
| F2 | `PRRT_kwDOP103ks6sJ4Y8` / 4266550065 (P1) | `adapter/http_reader.py` L383–384, `b178f03` | the gate trims and case-folds, so ` DEV ` and `Dev` serve; canon reads "explicit `APP_ENV=dev`" | material for this session: the current behavior is the IA's binding §9.2 rule, held by B-6, on a protected security gate | RP-5 to RS-20; thread answered, left open |
| F3 | `PRRT_kwDOP103ks6sJ4Y_` / 4266550069 (P1) | `tools/evidence/generate_a7_transport_proofs.py` L54, `b178f03` | five catalog rows publish `/ops/db/unavailable`, `/ops/probe/env`, `/ops/writer/diagnostic`, which HDE Architecture §3.5 marks `RETIRED/NONCANONICAL` and excludes from the Endpoint Catalog | material: changes IF-6, EC-8, ID-1's binding reading and acceptance (5)'s reading; instruction ID-1 and §14 route it to RS-20 | RP-4 to RS-20; thread answered, left open |

Canon verification for F2 and F3 is in the rescope request §2 to §4.

## 4. Correction (commit `3a1b0a7`)

- `tools/evidence/generate_a7_transport_proofs.py` line 88: `if any('aliases' in e for e in cat['endpoints'] if e['path']!=AUX_PATH)` replaces the `classification!='public_aux'` test. With the existing Aux pin (exactly one `/aux/narrative` record, `public_aux`, `aliases == ["/api/aux/narrative"]`), aliases can appear only on the Aux record.
- `tests/http/test_endpoint_catalog.py::test_validator_rejects_aliases_off_the_aux_record_and_alias_collisions` gains the reviewer's case: `GET /ops/rails/refusal` reclassified `public_aux` with `aliases: ["/x"]` is refused. The row is one canon adopts (HDE Architecture §3.5), so the case does not depend on RP-4.
- `public_aux` itself is not restricted to the Aux path, so `tests/transport/test_a7_transport_proofs.py::test_all_canon_valid_classifications_accepted` (PD-22) is unchanged.
- No release member, catalog byte, governed artifact or other file changes (§5).

## 5. Local validation (on `3a1b0a7`)

**Environment.** `/usr/bin/python3.12 -m venv` in the session scratchpad, CPython 3.12.3, `pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; readiness `python -m pytest --version` → `pytest 8.4.2`. `ruby` 3.3.6, `bash`, `curl` 8.5.0 on `PATH`. Rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, geocode, database and `GH_TOKEN` variables unset. Every write-capable run used a fresh detached worktree of `3a1b0a7` and ended with `git diff --exit-code` 0 and an empty `git status --short --untracked-files=all`.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/http/test_endpoint_catalog.py`, `tests/transport/test_a7_transport_proofs.py` | 227 passed |
| 2 | Red/green: the amended test against the pre-fix validator (`b178f03`'s generator) | 1 failed (the new case is accepted by the old validator); against the fix, passed |
| 3 | Plan §6.10 step 3b byte stability: `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`, then `--check` | both exit 0; zero tracked changes (catalog, sidecars, snapshot and the seven A7 proofs byte-identical) |
| 4 | Evidence validators: `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh`, `check_lf_endings.py`, `ci/checks/check_final_lf.sh`, `refresh_step_logs_manifest.py --check`, `run_canonical_json_gate.py --check-only` | all exit 0; clean tree |
| 5 | Classifier, whole PR (`--base 1735d94 --head 3a1b0a7 --event-name pull_request`) | `reason=selected_lanes`; all seven lanes; `needs_python`, `changed_tests` true; 85 paths; 164 changed-test targets (as PR-30) |
| 6 | Classifier, this correction only (`--base b178f03 --head 3a1b0a7`) | product, compat, evidence, release; 2 paths; 3 targets: `tests/evidence/test_http_reader_ci_ownership.py`, `tests/http/test_endpoint_catalog.py`, `tests/transport/test_a7_transport_proofs.py` |
| 7 | Release lane: `git diff --exit-code`; `release_id_recompute.py --check-manifest-only`; `build_release_attestation.py --output <external empty dir> --require-clean`; `--verify` | all exit 0: `validation_result: PASS`, `release_admission: PR06R_B_FINAL_PASS`, `release_id` = `manifest_sha256` = `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f` (unchanged), `source_commit` `3a1b0a72b5b865c394615464f32f9c0e0ac87feb`, `source_commit_exact: true`; clean tree |
| 8 | Changed-test step for this correction: the 3 targets of item 6, as CI runs them | 231 passed; clean tree |
| 9 | Evidence-lane tests (`.github/workflows/ci.yml` evidence step's six test paths) | 130 passed (480 s); clean tree |
| 10 | Full `tests/` sweep: `python -m pytest -q -p no:cacheprovider tests`, `PYTHONPATH` the worktree, `ruby`, `bash` and `curl` on `PATH` | **4,747 passed, 3 skipped, 2 xfailed, 0 failed** (5 warnings; 929 s); exit 0; `git diff --exit-code` 0; empty status. Same counts as PR-30's sweep on `7f6da26` (the new case is inside an existing test) |

Not rerun here: plan §6.10's convergence (no member or evidence primary changed: item 3) and `VERIFY.sh` (untouched).

## 6. Hosted CI

| Run / job | Head | Result | Status as a gate |
| :- | :- | :- | :- |
| 38507655612 / 115669136207 | `b178f03` (PR-30 record head) | success, 03:44:16Z–03:59:27Z; changed tests and all seven lanes success; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; hosted Python 3.12.15; qa lane success (OBS-17 did not occur) | stale: `b178f03` is known to need correction (F1). Not cancelled (it completed before any push). Evidence only. O-6: the hosted `ruby` version was not read from the log |
| (next) | the head this record's push creates | pending at record time | read by the PR-35 continuation; this record does not claim it |

## 7. Rescope

`docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0.md` (RP-4, RP-5; `PR_RETURN_PHASE: PR-35`) carries the evidence, alternatives, prototypes, impact and proposed CR-7 and CR-8. Recommended: RP-4 (a) catalog-only exclusion with ID-1 class (d) (2 hand-edited files, 11 owner-produced files; convergence from step 3b); RP-5 (a) exact comparison (release member: re-cut and full convergence from step 2). If both are approved, one convergence from step 2 covers both.

## 8. In-flight decisions

| ID | What changed | Why it was necessary | Tested by (outcome) |
| :- | :- | :- | :- |
| D-4 | `validate_catalog` keys the "aliases only on the Aux record" rule on the record's path (`AUX_PATH`) instead of its class; the validator test gains the reviewer's case | Codex F1: the class-based rule let a second `public_aux` record carry an alias, which the test's name, plan §6.5 ("pinned by path") and HDE-CLI-API-Vendor-Ref §5.6's single Aux record do not allow. Fail-closed validator hardening inside the S15 deliverable; no acceptance, interface or catalog byte changes | §5 items 1 to 4 and 7 (227 passed; red on the old validator; A7 write byte-identical; validators exit 0; attestation PASS); §5 items 8 to 10 (231, 130 and 4,747 passed, 0 failed) |
| IF-35-1 | PR-35 works on and pushes to the pull request's head branch `claude/nifty-cray-w86vmp`, not the harness-designated `claude/pr-35-merge-readiness-lf9t2g` | GCF-17: one branch and one pull request per plan cycle; Nathan's handoff continues #643 | remote head read back after the push (§9) |

## 9. PR_REMOTE_ACTION_LEDGER

| Time (UTC, 2026-10-14) | Action | Evidence |
| :- | :- | :- |
| ~03:47 | Entry reads: #643 state, reviews, review threads, comments, check runs | §2, §3; remote head `b178f03` |
| ~03:47 | `subscribe_pr_activity` #643 | confirmed |
| ~03:49 | Remote branch fetch | `origin/claude/nifty-cray-w86vmp` = `b178f03`; checked out locally |
| 03:44–03:59 | Hosted CI run 38507655612 on `b178f03` (started by PR-30's push) | success; stale as a gate; not cancelled |
| ~03:55 | Local commit `3a1b0a7` (F1) | §4 |
| 03:53–04:12 | Local validation (sweep about 03:53:46–04:09:16, 930 s) | §5 |
| 03:56:00 | TypeSafe reading for RS-20 | §11 |
| after this record is written | one push of `3a1b0a7` and the record commit to `claude/nifty-cray-w86vmp` (no `[skip ci]`) | the pushed head is read back with `git ls-remote` and named in the session's final reply; RS-40 / PR-35 verifies it at entry |
| after the push | Replies on F1 (resolved), F2 and F3 (open, routed) | the thread replies |
| — | Hosted CI and Codex review on the pushed head | not observed by this record; the subscription stays active |
| — | Mergeability | `unstable` at entry (checks pending); not merge-ready (F2, F3 open) |
| — | Remaining useful local action | none until RS-20 decides |
| — | Next evidence action | RS-20 decision; then RS-40 (APPROVE) or PR-35 (IN_SCOPE_REPAIR / REJECT) applies it, converges, pushes and reads CI and review on that head |

## 10. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| RP-4, RP-5 decision; CR-7, CR-8 | the whole-change IA (RS-20) | pending |
| Applying the decision; convergence from step 2 or 3b per plan §6.10 restart rules; second byte-stable pass; local validation; one push; hosted CI; Codex review; thread resolution; PR description update; `MERGE_PENDING` | PR-35 (through RS-40 on APPROVE) | pending |
| Hosted CI and Codex review on the head this record's push creates | PR-35 continuation | pending |
| Merge | Nathan only | — |
| Lineage review | the whole-change IA (PR-40) | after the merge |
| OBS-P3-1 to OBS-P3-11, doc-delta candidates, WU-DOC-01 items, OBS-17, O-6, AQ-1 (result v1.0 §9) | as named there | carried unchanged |
| Prompt-use provenance persistence | Product Owner (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent) | pending, non-gating |

Constraints preserved: closed rails; no live vendor, production or database call; no hand edit of a governed artifact; no skipped, disabled, `xfail` or quarantined test; no canon edit; no route added or removed; no member or admission-constant change in this phase.

## 11. TypeSafe reading and surface advice for the receiving session (RS-20, WU-PR-03 PR-35 rescope request v1.0)

**Action sent (v6):** "Review, as the whole-change implementation agent, a new bounded rescope request raised during review correction of one open pull request of an approved change, not yet reviewed, with two items: whether five endpoint-catalog rows for three diagnostic routes that canon marks retired and excluded from the catalog must leave the catalog (with a new reasoned exclusion class in the route-enumeration test and a validator pin), and whether the dev-only reader route's environment gate should compare the value exactly instead of trimming and case-folding it as the instruction directed; read the governing canon sections and the approved specification, plan and instruction, decide each item (approve, in-scope repair, reject, revision or specification change) and record the decision and any build-notes addendum. No code is written or run; the pull request session resumes the implementation, and CI and an independent lineage review follow."

**The reading, as the skill printed it:**

### RS-20 WU-PR-03 rescope review (RP-4, RP-5)
- **TypeSafe v6: Opus 5.5, high.** Effort score 2.21 (confidence 0.80); rung probabilities low 0.00, medium 0.05, high 0.70, extra high 0.25, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.07, Opus 5.5 0.93 (confidence 0.86). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.05, Opus 5.5 at high 0.65, Opus 5.5 at extra high 0.23, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.05, Fable 5.1 at extra high 0.02, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-14T03:56:00Z. Nathan picks the cell.

**Detail:** v6 sent 2026-10-14T03:56:00Z; HTTP 200 in 0.55 s; 4289 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none printed.

**Records:** Notion row not written, as PR-35 directs. Nathan's pick for RS-20: not stated. Nathan's pick for this PR-35 session: not stated (reading in result v1.0 §15).

**Surface advice for RS-20:**
- **Session.** The continuing whole-change IA context, as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` with Notion read access for the prompt and GitHub read access to #643 (its three Codex threads).
- **Reading.** The request reads from #643's head branch (it is not on `main` until the merge); canon is read on `main`. The canon passages are short: HDE Architecture §3.5, HDE Users Guide §1.1, HDE-CLI-API-Vendor-Ref §5.4 and §5.6, HDE Schemas & Artifacts §8.8, HDE Mechanics Guide §34, HDE Governance §4.1.4 "Dev/admin APP_ENV gating".
- **Reproduction, if wanted.** `git apply` of the companion diff on a scratch worktree of the PR head, a Python 3.12 environment with CI's install (package-index access), `ruby`, closed rails; RP-4's catalog effect needs `HDE_WRITE_A7_PROOFS=1` and the updater; RP-5's effect needs the same-version re-cut first (the member change makes admission refuse until then). No live vendor, production or database access.
- **Writes.** The review, any addendum and the handoff under `docs/ephemeral/`.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / PR-35 / result 1, version 1.1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e (page state 2026-10-12T02:30:15Z). Receiver contract read: RS-20 — Review Bounded Work-Unit Rescope — 100926.1, https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c (page state 2026-10-12T02:29:57Z) |
| role/stage | dedicated WU-PR-03 PR-35 session / review resolution |
| capture time | 2026-10-14T04:05:00Z |
| execution identity | https://claude.ai/code/session_0136SjBtuTJwoEpceUd46T6C |
| inherited usage | PR-30 result v1.0 §16 and the entries it inherits |
| pull request and commits | #643; `3a1b0a7` and this record's commit |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; pending, non-gating; owner the Product Owner) |

## Canon relied on

Canon read on `main` at `1735d94` (`docs/pfcanon/` unchanged since `ad11821`); the branch's PF10 v13.5.7 is the Product Owner's directed, unmerged change.

| Topic | Sources and sections |
| :- | :- |
| Phase authority, results, rescope routing, handoff | PR-35 — 100926.1 (read in full); RS-20 — 100926.1 (receiver contract, read in full); skill `glow-hde-pr-development` 1.4.0; instruction v1.0 §13 and §14 |
| Review chain | PF10 HDE Build Notes v13.5.6 addendum 2.3 (Rules 2 and 3: the Codex code review is read and resolved; no security review) |
| F1 (D-4) | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.6 (one canonical Aux record; `aliases` "reachable spellings of the same contract"); plan v1.1 §6.5 and PD-22; instruction ID-1 "Classes" |
| F2 (RP-5), F3 (RP-4) | as mapped in the rescope request "Canon relied on" |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md` read in full (precedence §1–§9; addenda 2.1–2.5); addendum record 2.6; silent on F1 to F3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails; pytest readiness; no hand edits; evidence attribution; QA output placement |

Read-back: this file, the rescope request and its companion are read back completely after commit and push; their identities, paths, versions, states and next consumer are confirmed in the session's final reply.
