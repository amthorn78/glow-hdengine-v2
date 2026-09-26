# HDE-EPIC040-PR06b — PR Implementation Result v1.1 (PR-35)

| Field | Value |
| --- | --- |
| Artifact | `PR_IMPLEMENTATION_RESULT` — `HDE-EPIC040-PR06b-PR-IMPLEMENTATION-RESULT` v1.1, the PR-35 phase record. It continues v1.0 (PR-30, `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.0.md`). v1.0 is unchanged as issued and remains the implementation record: scope, planning decisions, in-flight decisions IF-01 and IF-02, and PR-30 local validation |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08, alternative A) with a release re-cut to `1.3.0` (overlay PF10 §2.24) |
| Change | `EPIC / HDE-EPIC040`; `HDE-EPIC040-SPECIFICATION` v1.1 (`SPECIFICATION_APPROVED`); PR06b rescope decision v1.0 |
| Producer | the dedicated PR-35 session for HDE-EPIC040-PR06b (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06b / PR-35`; `context_conflict: NONE`; runtime `https://claude.ai/code/session_01XyLNkn9Ab1sB7kCUCJvodt`); `EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION` |
| Result | `MERGE_PENDING` — Ready to merge, on the condition under *Final head* (§1) |
| Prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1 (`https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`; page as of 2026-09-24T15:48:24.405Z; parent `HDE IA — GCFPE-20260914.1 — 091426.1`; Notion read only). Primary skill: `glow-hde-pr-development` 1.3.1 |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/focused-heisenberg-91y3cn` (the PR-30 branch, continued) |
| Pull request | [#513](https://github.com/amthorn78/glow-hdengine-v2/pull/513), the one work vehicle, reused |
| Base | merge-base `d031f94a9cd0ef89f0fc50b37e86abe3cd90a643`; `origin/main` is still `d031f94` (re-read with `git ls-remote` during PR-35) |
| Commits | PR-30: `acae4c637e2ce8c9e987953bcbe284f7e03719c9` (implementation, tree `9b3fbee142b02dcce285731f55f7bbe38c5b5232`) and `85e702b3259f4a549adc69d2f68fa36ddaefda57` (PR-30 records, tree `db6ecacba80f6c47569cb8862e71814552f5b91d`). PR-35 made no code commit. Records: the commit that adds this file, ledger v1.1, the PR-35 checkpoint v1.0 and the conditional PR-40 handoff v1.0. A commit cannot embed its own SHA, so the records commit's SHA and the remote head after its push are recorded in the PR #513 body and the PR-35 return |
| Recorded by | the dedicated PR-35 session, 2026-09-26 (UTC); entry at 16:10Z |

## 1. Outcome

**`MERGE_PENDING` — Ready to merge,** on the condition under *Final head*. This record is historical pre-merge evidence. It does not claim the PR is merged. It is not a QA verdict, acceptance, release activation, PF09 movement, OPS01 attestation, C040-08 drainage, deployment or closure. Nathan / Product Owner merges manually as a separate action. Nothing here enables, schedules or requests a merge.

- **Reviews.** Codex's Security Review of the implementation head `acae4c6` completed with no finding. Codex's Code Review of the same head raised one finding:
  - **CR-01** (P1, "Keep the EPIC038 fixture proof frozen") on the `FROZEN_OPEN_ABBA_SHA256` refresh in `tools/evidence/generate_open_rails_abba_proof.py`.
  - Disposition: **not changed; out of scope for this work unit** (§4). The refresh is the plan-named coherence dependent (plan D-06, F-13, §6.2, §14.3). The IA's instruction requires it (§§5.3, 6). The repository treats the file as a current release-bound derivative. PR06 and PR06a each landed the same refresh. Both lineage reviews accepted the ABBA proof tool as a coherence dependent: PR06's in PF10 §2.22, and PR06a's in its own review record.
  - Both fixes the finding proposes fail tests or evidence checks on this head (§5).
  - The finding's valid residue is the family's fixed EPIC038-era labels. They pre-date this PR, are byte-identical on `main`, and go to their owner as O-P06b-15.
  - The thread is answered and resolved after the records push, so the reply can cite this record. Resolved means dispositioned for this PR, not fixed.
- **Correction.** None. No code, test, evidence or roster byte changed in PR-35. The candidate's code tree is the PR-30 implementation tree: `git diff --stat acae4c6 85e702b3` names only the three PR-30 records under `docs/ephemeral/`.
- **CI.** Run `36254322410` on head `85e702b3` concluded `success`, 16:07:33Z–16:19:50Z (§8). This run was a live gate, not a stale one, because no correction was needed. Selected lanes: product, compat, evidence and release, including the strict attestation build and verify. The run ended with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. PR #513 read `mergeable_state: clean` afterwards.
- **Local.** On Python 3.12.3 at `85e702b3`, every command in §7 exited 0. That covers the changed-test isolation (667 passed), the open-rails proof owner's checks, and every evidence and release read-only check.
- **Final head.** This record's commit adds only `docs/ephemeral/` records above `85e702b3`. The pushed head's exact-head CI is read after the push and recorded in the PR #513 body and the PR-35 return. That run covers the same four lanes on the same code tree. The return states `MERGE_PENDING` only if all of these hold:
  - that CI run is green;
  - the CR-01 thread is answered and resolved;
  - no new review finding or unresolved thread exists;
  - the PR stays open and mergeable.

  Otherwise this result no longer stands and a later version replaces it.

## 2. Authority, identity and controlling sources

| Source | Exact identity | Repository path |
| --- | --- | --- |
| Product Owner Proceed | The original PR-30 Proceed for exactly `HDE-EPIC040-PR06b-PR-IMPLEMENTATION-PLAN` v1.0 and `HDE-EPIC040-PR06b-PR-INSTRUCTION` v1.0 (result v1.0 §2). It covers PR-30 and PR-35 of this one work unit. No second Proceed exists, was requested or was needed | result v1.0 §2 |
| PR-35 invocation | Nathan's pasted PR-30 handoff naming this prompt, PR #513 and the input artifacts (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06b / PR-35`; `context_conflict: NONE`) | this session |
| Detailed PR plan | v1.0, SHA-256 `1672b1a86315063d04a3d649ed1b929ea85fdab9b51896af82ba7ed7bba13c8b` (108,802 bytes), read completely | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` |
| PR instruction | v1.0, SHA-256 `d3d750cb51bd02c6fbbc38a5bfc8dd24d6b0f51398b450976a7629b643fb2696` (9,611 bytes), read completely | `docs/ephemeral/HDE-EPIC040-PR06b-pr-instruction-v1.0.md` |
| Overlay and decision | addendum v1.0 `63d0bdcee8d4295738bb6a05a5a93c72951a871532e12d53b7e3a449fcca14a3` (drained as PF10 §2.24); rescope decision v1.0 `cebbe8ec34a91a39d9eec4692fcc8e1832b28d37cfada523638e25ee1a62140c`; both read completely | `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md`, `docs/ephemeral/HDE-EPIC040-PR06b-rescope-decision-v1.0.md` |
| PR-30 result, ledger, checkpoint | result v1.0 `2ade07f61048c230720b260b460208b95d89945dce601915754472e4a6f0ab72` (38,223 bytes); ledger v1.0 `4f9fe9a0b8a39ca0bb7651629ed3174b5508df1631d3ef14a6329c2bec28a1e7` (7,010 bytes); checkpoint v1.0 `f445cb33c794c186903ba0bf260eb67ea86cdfb9b27a9087fd80a9fcf2f09d87` (6,404 bytes). Each was read completely from the PR head; none was edited | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.0.md`, `…-pr-remote-action-ledger-v1.0.md`, `…-pr30-checkpoint-v1.0.md` |
| Immutable approved base | as plan v1.0 §2.1: Specification v1.1 (`43e1b182…`), Implementation Audit v2.0 (`9b0d8edb…`), Implementation Plan v2.1 (`10732f93…`), Plan Review v2.1 (`47f73e62…`), and the accepted PR01–PR06a. Digests verified at their paths | plan §2.1 paths |
| Current PF10 read | PF10 — HDE Build Notes v13.3.5, 274,422 bytes, SHA-256 `7010511cf61d1e6e84ce1e528f03027058df64eb0be2a6163cd89c7bf27efbae`. It is the latest base version; front-matter rule 6 says older base versions are not to be read, and v13.3 to v13.3.4 were not read. Read directly: front-matter lines 1–130 (purpose, authority, scope, lettered sets, supersession, the current-version and live-content rules), and §§2.15, 2.21, 2.22 and 2.24 in full. The complete file was also swept by a read-only worker for every passage on this finding (§5.4). Provenance, not a gate | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.5.md` |
| Repository instructions | `AGENTS.md` (`94c38926…`, 50,015 bytes) was applied, in particular: the closed rails, governed-evidence sole writers, the release-identity section, the Historical EPIC038 posture (lines 114–117, which the finding cites), the code-review scope, and the PR-description contract | `AGENTS.md` |

Nothing was opened from Google Drive, and no DOC or DOCX was used. Notion was read only: the PR-35 page, and the PR-40 page to confirm its identity for the handoff. `docs/pfcanon/` was read only.

## 3. Recovery and continuity at entry

- **Container.** The container was a fresh clone at `d031f94` (16:09:58Z). The harness created a local branch `claude/wizardly-lamport-m1y87z` at `d031f94`. That branch is absent on `origin` (`git ls-remote`) and was never committed to or pushed. The PR-30 container is not reachable; the repository, branch, pull request and records establish continuity.
- **Fetch and checkout.** `git fetch origin main claude/focused-heisenberg-91y3cn` read `origin/main` at `d031f94` (the PR base) and the PR head at `85e702b3`. `git checkout -B claude/focused-heisenberg-91y3cn origin/claude/focused-heisenberg-91y3cn` ran at 16:10:59Z. The tree was clean, and the only worktree was the checkout.
- **Continuity (the nine GCF-17 fields).** Every field has the same value in PR-30 and PR-35:
  - `WORK_UNIT_ID`;
  - the original Proceed;
  - workspace `/home/user/glow-hdengine-v2`;
  - branch `claude/focused-heisenberg-91y3cn`;
  - PR #513;
  - instruction v1.0;
  - plan v1.0;
  - primary skill `glow-hde-pr-development`;
  - artifact lineage: the PR-30 records at `85e702b3`, read back.

  Nothing was duplicated, replaced or transferred. No second branch or pull request was created.
- **PR state at entry.** Open, not draft, head `85e702b3`, base `main` `d031f94`, 2 commits, 68 files (+501/−127), `mergeable_state: unstable` because CI was still running.
- **Subscription.** `subscribe_pr_activity` for `amthorn78/glow-hdengine-v2#513` returned "Subscribed to activity on amthorn78/glow-hdengine-v2#513 … will now be delivered into this conversation". The subscription is active for this session.

## 4. Review findings and dispositions

Read at 16:11Z: every review, review thread, issue comment and check run on PR #513. There is no human review, no requested change and no other thread.

| ID | Reviewer / surface | Revision | Location | Finding | Disposition | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| CR-01 | `chatgpt-codex-connector[bot]`, Code Review `5326503158` (`COMMENTED`, 16:09:40Z); thread `PRRT_kwDOP103ks6mSA83` (`discussion_r4111930454`), P1, unresolved and not outdated at entry | `acae4c637e` | `tools/evidence/generate_open_rails_abba_proof.py:57` | Refreshing `FROZEN_OPEN_ABBA_SHA256` "blesses" the 1.3.0 regeneration as the frozen HDE-EPIC038 primary. The JSON still says `hde_epic038_pr03_open_rails_abba_proof` / `2026-07-14`, which misattributes a September run and turns retained evidence into a current-release derivative. Proposed fix: keep the original artifact and digest frozen and publish any current-release proof under a current evidence identity. Cites `AGENTS.md` L114–L117 | **Not changed — out of scope for PR06b.** The refresh is approved scope. Both proposed fixes fail tests or evidence checks on this head. The labels are pre-existing and go to O-P06b-15 | §5 |
| — | Codex Security Review | `acae4c6` | — | Completed 2026-09-26T16:09:18Z with no finding. The summary comment's metadata reads `codex-security-review:v1 … "status":"completed"`, and no security thread or comment exists | Clean | issue comment `5847734093` |
| — | Codex Review Summary | `acae4c6` | — | Code Review completed 16:09:42Z (one finding, CR-01); Security Review completed 16:09:18Z | Read | issue comment `5847734093` |

No new review was requested. The records commits change only `docs/ephemeral/`, which `AGENTS.md` puts outside CI and outside automated-review scope. Outside `docs/ephemeral/`, the code tree is identical to the reviewed `acae4c6`. PR-35 made no code correction, so plan §17.1's "Security Review on the corrected head where a correction lands" does not apply.

## 5. Evidence for the CR-01 disposition

### 5.1 What the repository says the file is

- **A release-bound derivative, not retained frozen evidence.**
  - `tools/evidence/regenerate_identity_closure.py` has a closure step `fixture_open_rails_abba`: write with `generate_open_rails_abba_proof.py`, then check with `--check`.
  - `audit/gates/determinism/open_rails_abba.json` and its `.path_proof.txt` are members of `DECLARED_PRODUCER_OUTPUTS` and `ATTESTATION_GENERATED_OUTPUTS` (checked by executing the module).
  - The strict attestation regenerates that set for the admitted release and binds it. This is the `AGENTS.md` release-identity model (line 109): "Current release-bound derivatives are generated only with `python tools/evidence/build_release_attestation.py --output <external-empty-directory> --require-clean`", and the closure is internal to its isolated copy.
- **Approved scope.**
  - The plan puts the file in the owner-regenerated set (§6.3), not in the frozen families (§6.4).
  - The plan names the constant refresh as the one coherence dependent (F-13, §6.2, §14.3, D-06). It records the consequence of omitting it (R-03: the test file, sanity stage 06 and the rails lane go red).
  - The IA's instruction directs convergence "including … the open-rails ABBA proof" (§5.3). It admits frozen-digest constants in proof tools as coherence dependents following the PR06a precedent (§6).
  - PF10 §2.24 item 3 requires evidence to converge through its owning writers.
- **Precedent.**
  - The constant was introduced by PR04 (`cd6f9e6`, `cfae96f8…`).
  - PR06 refreshed it (`f7484d0`, → `3e78fcdb…`; PR06 result v1.0 IF-01, reasoned as keeping the inert non-admitted branch truthful).
  - PR06a refreshed it (`d79cfc1`, → `29223e6f…`; D-12).
  - This PR refreshes it (`acae4c6`, → `c78740b3…`).
  - PF10 §2.22 (PR06 accepted final, L2315) lists "the ABBA proof tool" among the accepted coherence dependents.
  - PR06a's accepted-final lineage review (`docs/ephemeral/HDE-EPIC040-PR06a-pr-work-unit-lineage-review-v1.0.md`, line 70) says the same of `generate_open_rails_abba_proof.py`. PF10 itself records the tool change, not the constant's values; those come from `git log -G` and the PR06 / PR06a result records.
- **PF10 §2.24's owned loci.** They do not list the ABBA proof tool. §2.24 L2517 sends "a file that items 1–3 genuinely require but that falls outside these loci" to the rescope route. PF10 §2.23 L2421 carried the same clause for PR06a, and PR06a's lineage review accepted this exact tool change as a coherence dependent under it. The IA's instruction §6 applies that reading to PR06b ("Coherence dependents that the re-cut forces, such as frozen-digest constants in proof tools, follow the PR06a precedent and must be named in the plan"), and plan §14.3 names the tool accordingly. PF10 §2.15 L1713 also classes changes that "validate against an existing frozen capture" as "ordinary necessary dependents of the approved work unit". PR-35 applies the approved plan's classification and does not reopen it. The PR-40 conformance check sees the same record.
- **PF10 §2.15.** The constant is read only by `validate_frozen_fixture_primary()`, on the non-admitted branch. That branch "self-extinguishes" once a release is admitted, and PR06's lineage review records it as "no longer taken". Keeping the constant equal to the committed primary keeps that inert branch truthful: it reports `RELEASE_NOT_ADMITTED`, exit 3, never `FROZEN_PRIMARY_DRIFT`.
- **`AGENTS.md` L114–L117.** These lines cover HDE-EPIC038's "frozen architecture and OPS packets" and say "historical captures are not current runtime identity inputs". The fixture proof is neither an architecture nor an OPS packet. Runtime identity reads only `catalog/manifest.json`.
- **§2.21 frozen captures.** Instruction §8 says they are not re-identified. They are `artifacts/cli/showcompat/{args,stdout}.json` and `artifacts/cli/{ab,ba}.json` (`_CAPTURE_IDENTITY_SOURCES`), not this file. They are unchanged.

### 5.2 Measured on `85e702b3` (Python 3.12.3, closed rails, vendor and DB keys absent, detached worktrees)

| Case | Command | Outcome |
| --- | --- | --- |
| Baseline (the candidate) | `python -m pytest -q -p no:cacheprovider tests/evidence/test_open_rails_abba_proof.py` | `78 passed`, exit 0 |
| Baseline | `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_open_rails_abba_proof.py --check` (fixture mode) | `{"path": "audit/gates/determinism/open_rails_abba.json", "result": "pass", "status": "OK", "top_level_pass": true}`, exit 0: the committed primary equals the owner's output for the admitted `1.3.0` release |
| Baseline | `… --check-current` (open rails, as `ci/jobs/rails_open_conformance.yml` runs it) | same line, exit 0 |
| Baseline | `sha256sum` of the primary vs the constant | both `c78740b3f9d45472e67c3bdeef4ade9e4a9c74fc3e6b11bc2f29d1a90a323348` |
| A — revert only the constant to `main`'s `29223e6f…` | the test file | `2 failed, 76 passed`. The two failures are `test_check_current_ends_not_admitted_with_distinct_code_and_frozen_primary_check` and `test_fixture_generation_and_check_refuse_without_writing_when_not_admitted`: `FROZEN_PRIMARY_DRIFT:audit/gates/determinism/open_rails_abba.json` instead of exit 3. The file is one of this PR's 14 changed-test targets, it runs in the rails job, and sanity stage 06 runs that job |
| B — revert the constant and the primary to `main`'s bytes | the test file; the owner's `--check`; `update_evidence_index.py --check` | `78 passed`; `DRIFT:audit/gates/determinism/open_rails_abba.json`, exit 1; exit 1 (`PROOF_SHA:audit/gates/determinism/open_rails_abba.json.path_proof.txt`). The committed evidence would no longer be the owner's output, and the attestation closure would regenerate different bytes |
| Diff of the primary, `main` → head | field-wise JSON comparison | Only `hashes.*` (8 Reader/CLI envelope digests) and `idempotence_hashes.{ab,ba}.{stored,recomputed}` (4) differ, because the Reader envelope carries the admitted `release_id`. `artifact_kind` (`hde_epic038_pr03_open_rails_abba_proof`), `generated_at_utc` (`2026-07-14T00:00:00Z`), `outcome` (`EVALUATED`), the predicates and `top_level_pass` (`true`) are identical |

The variant worktree was discarded. The checkout was never modified.

### 5.3 Why this is not an in-scope correction and not a rescope

- The finding's proposed state ("keep the original artifact and digest frozen") contradicts the producer's admitted-path contract and the approved convergence obligation. §5.2 measures this.
- The finding's alternative, a current-release proof under a new evidence identity, needs a new evidence family or producer redesign. That means changing the producer's labels and the Mirror row identity, possibly adding a second primary with its own Index/Mirror rows, and changing the tests and the sanity and rails wiring. All of that is outside PR06b's owned loci. Plan §6.6 keeps the updater, the identity closure, the attestation builder and `ci/jobs/*.yml` untouched, and plan §6.2 admits exactly one coherence dependent. The change is neither obvious nor necessary to deliver the approved scope, which is delivered.
- The approved work unit continues lawfully without it, so there is no material boundary and no `RESCOPE_REQUEST`. Under the decision rule, it is recorded as a candidate for its owner (O-P06b-15).

### 5.4 PF10 completeness sweep

A read-only worker read all 2,557 lines of PF10 v13.3.5 in ten chunks, looking for every passage on the open-rails proof, frozen captures, release-bound derivatives, evidence labels and PR-35 review handling. The lines this record cites (L1372, L1671, L1679, L1713, L2080, L2213, L2262, L2308, L2315, L2421 and L2517) were re-read directly.

- PF10 never names `FROZEN_OPEN_ABBA_SHA256`, `audit/gates/determinism/open_rails_abba.json`, "frozen primary", `FROZEN_PRIMARY_DRIFT` or HDE-EPIC038. It neither calls the file a frozen EPIC038 primary nor forbids the refresh.
- Its frozen-capture protections are each scoped to their own addendum:
  - §2.10: PR02 only.
  - §2.15: the non-admitted interval ("Frozen captures remain frozen", L1671). It names the tool as the discrimination locus (L1679), and its non-admitted branch "self-extinguishes after PR06 admits the roster" (§2.19, L2080).
  - §2.21: the canonical-JSON gate's capture identity sources. Re-identifying those captures is "a Product Owner capture-contract decision" (L2262).
- No addendum asks for a new evidence identity or family for this file. Several prohibit new evidence families within their own scope.
- The sweep changes no disposition. It surfaced the §2.24 loci wording treated in §5.1 and the PF10 form items in O-P06b-16.

## 6. In-flight decisions

`NONE`. PR-35 took no decision that changed code, tests, evidence, scope or approach. CR-01 is a review disposition (§4), not an in-flight decision.

## 7. Local validation at the current head (PR-35)

Environment: a Python 3.12.3 virtualenv under the session scratchpad with CI's install set (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`). `python -m pytest --version` → `pytest 8.4.2`, and the venv's `python` was first on `PATH`. Every command ran in a detached worktree of `85e702b3`, with `PYTHONPATH` on it; `engine` resolved from the worktree (verified). Rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL` and `GH_TOKEN` were unset (count of set keys: 0). `ci/checks/check_env_pins.sh` → `[env-pins] OK`. The only open-rails commands were the fixture-mode proof checks of §5.2; no vendor call and no database connection occurred.

| Check | Command → outcome |
| --- | --- |
| Classifier (as `ci.yml`) | `python ci/checks/classify_ci_changes.py --base d031f94a… --head 85e702b3… --event-name pull_request …` → exit 0. Output: `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=68;lanes=product,compat,evidence,release`, with `db`, `rails` and `qa` false and `changed_tests=true`. The 14 changed-test targets are the same set PR-30 recorded |
| Changed-test isolation | the 14 targets in the detached worktree → `667 passed in 73.34s`, exit 0; `git diff --exit-code` 0; no untracked file |
| Open-rails proof owner | §5.2 baseline rows: 78 passed; `--check` 0; `--check-current` 0 |
| Evidence read-only | `update_evidence_index.py --check` 0; `orientation_demo.py --check` 0; `refresh_step_logs_manifest.py --check` 0; `ci/checks/check_evidence_index_hash.sh` 0; `validate_evidence_paths.py` 0; `ci/checks/check_mirror_schema.sh` 0; `ci/checks/check_final_lf.sh` 0; `run_canonical_json_gate.py --check-only` 0. `check_mirror_schema.sh` is a Python script with a `.sh` name. It was executed directly, as `ci.yml` runs it, and exited 0. An earlier invocation through `bash` exited 2 with a shell syntax error; that was this session's invocation error, not a repository defect |
| Release read-only | `scripts/release_id_recompute.py --check-manifest-only` 0; `load_active_mechanics_bundle()` → `AdmittedMechanicsBundle 1.3.0`, 45, `release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`, equal to `sha256(catalog/manifest.json)` and to `identity_meta()["release_id"]` |
| Tree | `git status --short --untracked-files=all` empty after every run |

Not re-run locally in PR-35, and why: the full product, compat, evidence and release pytest sets and the attestation build. Hosted CI ran them on this exact head on Python 3.12 (§8), and PR-30 ran them at the identical code tree `acae4c6` (result v1.0 §7). The db, rails and qa prudence lanes are unselected here; PR-30 ran them.

## 8. Hosted CI on the candidate head

| Item | Value |
| --- | --- |
| Run | `36254322410` (workflow `ci`, event `pull_request`, attempt 1, head `85e702b3259f4a549adc69d2f68fa36ddaefda57`), job `test` `108438124785`, 16:07:33Z–16:19:50Z, conclusion **`success`**; Python 3.12.14 |
| Classification | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=68;lanes=product,compat,evidence,release` |
| Changed tests (detached worktree at `85e702b3`) | `667 passed in 83.17s` |
| product | `20 passed in 10.40s` |
| compat | `102 passed, 3 skipped, 2 xfailed in 8.92s` |
| db / rails / qa | `skipped` (not selected), and the final check requires `skipped` for an unselected lane |
| evidence | `111 passed in 468.77s` |
| release | detached worktree at `85e702b3`: `64 passed in 1.93s`; the strict attestation build and `--verify` both completed (`…/hde-release-attestation/attestation.json` printed twice; step `success`). The non-admitted receipt branch `RELEASE_LANE:RELEASE_NOT_ADMITTED` was not taken: the string appears only in the step's printed script, never as output |
| Final marker | `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (16:19:49Z); `git diff --check`, `git diff --exit-code` and the clean-status assertion passed |
| Stale status | not stale. No review finding required a code correction, so this run gated the candidate code tree; it was neither cancelled nor re-run |
| Mergeability after the run | `mergeable_state: clean`, head `85e702b3`, base `d031f94` |

The log was read through the API: the job-log tail, then the complete run-log archive downloaded to the scratchpad and searched. The attestation's `release_admission` value is not printed by the lane. PR-30 observed `PR06R_B_FINAL_PASS` for the identical code tree (result v1.0 §7.6).

## 9. Merge-readiness predicates

| Predicate | State | Evidence |
| --- | --- | --- |
| Approved implementation scope complete | true | result v1.0 §1 (CC-1 to CC-5 on `acae4c6`); CC-6 and CC-8 by run `36254322410`. CC-7 by §4: the Security Review is clean, and the Code Review's one finding (CR-01) is dispositioned out of scope with evidence, its thread resolved after the push. CC-9 by this record's nonclaims |
| Required local checks pass on the candidate | true | result v1.0 §7 (`acae4c6`, Python 3.11.15); §7 here (`85e702b3`, Python 3.12.3) |
| Intended commits pushed; PR reflects the exact remote head | true for `85e702b3`; for the records head, established after the push | *Final head* |
| Code and security findings resolved; no required thread unresolved | Security: clean. CR-01: dispositioned with evidence; the thread reply and resolution follow the push | §4, §5; *Final head* |
| Required CI passes on the current candidate | true for `85e702b3`; for the records head, read after the push | §8; *Final head* |
| No unresolved material rescope, dependency or repository-state conflict | true | no material boundary (§5.3); base unchanged; `mergeable_state: clean` |
| Result, ledger, checkpoint and handoff saved and read back | true locally before the push; remote read-back after the push | this file; `docs/ephemeral/HDE-EPIC040-PR06b-pr-remote-action-ledger-v1.1.md`; `docs/ephemeral/HDE-EPIC040-PR06b-pr35-checkpoint-v1.0.md`; `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.0.md` |

## 10. Limitations

- The records head's CI, the CR-01 thread reply and resolution, and the remote read-back of the records commit happen after this record is committed. They are recorded in the PR #513 body and the PR-35 return (*Final head*).
- Local runs used Python 3.12.3; CI used 3.12.14.
- The attestation's `release_admission` value on the hosted run is inferred from the step's success and is not printed by the lane (§8).
- `tests/reader_v1/test_cli_proof.py` keeps its pre-existing failure (O-P06a-03). It was not run in PR-35 and is in no lane.
- No live vendor or database action occurred. The only open-rails runs were the fixture-mode checks of §5.2.
- PF10 v13.3.5 was read directly for front-matter lines 1–130 and §§2.15, 2.21, 2.22 and 2.24. The rest of the file was read by a read-only worker (§5.4), and the lines this record cites were re-verified directly.

## 11. Observations (non-gating, carried for their owners)

| ID | Observation | Owner |
| --- | --- | --- |
| O-P06b-15 | The open-rails fixture proof is regenerated by its owner at every re-cut, and its digest binds the admitted `release_id` (§5.2). Its self-description is still fixed EPIC038-era text: `artifact_kind` `hde_epic038_pr03_open_rails_abba_proof` and `generated_at_utc` `2026-07-14T00:00:00Z` (producer constants `PRODUCED_AT` and the `artifact_kind` literal); the Mirror row's `artifact_key` `epic038.pr03.open_rails_abba`, `epic_id` `HDE-EPIC038`, `record_type` `epic038_pr03_open_rails_abba_proof` and `produced_at_utc` `2026-07-14T00:00:00Z`; and the constant's comment "Frozen capture-time primary (HDE-EPIC038 PR-03)". That text describes the family's origin, not the current regeneration. This is the valid residue of Codex CR-01. It pre-dates this PR (the same text on `main` since PR06) and needs a producer / evidence-family decision: re-identify the family or its capture-time fields, and/or derive the non-admitted binding from tracked or Mirror bytes instead of a source constant (O-P06-17, O-P06a-11). Not decided here | open-rails proof owner; evidence updater owner for the Mirror row fields |
| O-P06b-16 | PF10 v13.3.5 form, observed during the sweep (the stored file is complete: 274,422 bytes, `7010511c…`). (a) L1372, the §2.11 prompt-use record, ends mid-word in the stored bytes: "Repository provenance persistence remains p". (b) §2.24's heading is H1 (`# 2.24 …`, L2486) with H2 subsections, where §2.8 (L943, L945) requires one H2 heading with H3 or deeper subordinates. Neither affects this unit | Nathan / PF10 drain owner |
| carried | O-P06b-01 to O-P06b-14 (plan §13.2, result v1.0 §10); CR-03 / O-P06a-22, O-12, O-P06a-03, O-P06a-11, O-P06a-12, O-P06a-23, O-P06-17 | their recorded owners |

## 12. `CANON_CONFLICT_REGISTER`

C040-01 to C040-08 are carried unchanged from plan v1.0 §13.1 and result v1.0 §11. C040-08 (`CANON_RECONCILIATION`, `APPROVED` alternative A, PF10 §2.24) is the conflict this candidate implements. Its PF01 §2.3 / PF04 §8.1.2 drainage stays with their maintainers and is non-gating. PR-35 opened, reopened, relabeled or decided no entry. CR-01 is not a register entry.

## 13. Remote actions

`docs/ephemeral/HDE-EPIC040-PR06b-pr-remote-action-ledger-v1.1.md` holds every PR-35 remote read and action with its evidence. PR-35 made one push (the records commit), one thread reply, one thread resolution and one PR-body update. It made no merge, no auto-merge, no `[skip ci]`, no force-push, no rebase, no review request, no Claude Code Review installation or trigger, no CI cancellation or re-run, no Notion write, no `docs/pfcanon/` write and no second branch or PR.

## 14. Prompt-use provenance

`GCFPE_PROMPT_USES`: `GCFPE-USE-HDE-EPIC040-PR-35-20260926-PR06b-01` (this PR-35 phase). Carried: `GCFPE-USE-HDE-EPIC040-PR-30-20260926-PR06b-01` (result v1.0 §13), `GCFPE-USE-HDE-EPIC040-PR-20-20260926-PR06b-01` (plan §16), `GCFPE-USE-HDE-EPIC040-PR-10-20260926-PR06b-01` (instruction §13), `GCFPE-USE-HDE-EPIC040-RS-20-20260926-PR06b-01` (decision §7).

- Prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1, `https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204` (page as of 2026-09-24T15:48:24.405Z; Notion read only). Destination confirmed by fetch: PR-40 — Review PR Work-Unit Lineage — 091426.1, `https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634?pvs=204` (page as of 2026-09-24T15:49:45.516Z).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members.
- Change / unit: HDE-EPIC040 / HDE-EPIC040-PR06b; Specification v1.1; instruction v1.0; plan v1.0.
- Role / stage: dedicated PR06b PR-35 session / PR-35.
- Execution identity: harness session `https://claude.ai/code/session_01XyLNkn9Ab1sB7kCUCJvodt`.
- Repository persistence: `PENDING / NON_GATING` (no installed provenance procedure); owner: the authorized repository writer once a procedure is installed.

## 15. Continuation

- `MERGE_PENDING` on the *Final head* condition. Nathan merges manually. This session stays subscribed to PR #513 and does not poll.
- When the subscription delivers the merge of PR #513, the return is `MERGE_OBSERVED` with the paste-ready PR-40 handoff. Otherwise the conditional block `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.0.md` applies. It is usable only after Nathan's manual merge and only where no `MERGE_OBSERVED` result was returned for that merge. Once either has been pasted, the other is void.
- **What merging does** (plan §15). The corrected Reader v1 schema, the real g06 error golden, the regenerated release-pack outputs and the 45-member `1.3.0` release (`release_id 52be4558…`) with its converged evidence become current on `main`. The corrected schema's error branch admits exactly the 17 governed envelopes the v1 routes emit, requires `schema` and removes `retry_after_ms`. Reader v1 and v2 response bytes do not change. It establishes none of: QA verdict, acceptance, PF09 movement, OPS01's final external attestation, C040-08 drainage into PF01 §2.3 / PF04 §8.1.2, C040-07 drainage, deployment, activation, Epic closure. PR07 must follow PR06b, and OPS01 verifies the `1.3.0` release.
