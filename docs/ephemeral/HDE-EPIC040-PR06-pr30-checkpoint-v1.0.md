# HDE-EPIC040-PR06 — PR-30 durable checkpoint v1.0 (initial publication)

Recovery record for the PR06 work unit. A resumed or uncertain entry (the dedicated PR-35 session, or an RS-40 return) re-reads this file, the result record and the ledger before creating any work.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06 — Complete release admission and evidence convergence |
| Session at checkpoint | the dedicated PR06 PR-development session (PR-20 and PR-30 phases; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_01S3w2LDoDhi5GKMfuLRKkdx`); PR-35 runs in its own dedicated session |
| Phase at checkpoint | PR-30 complete: `PR_CANDIDATE_PUBLISHED`; next phase PR-35 |
| Original Proceed | Nathan / Product Owner's PR-30 invocation for exactly `HDE-EPIC040-PR06-PR-IMPLEMENTATION-PLAN` v1.1 (SHA-256 `8df055a33bed5e4b1289b4e8791708e0cb9dc399d3f10fd35cc87c469e447e74`) with `HDE-EPIC040-PR06-PR-INSTRUCTION` v1.0 (`20517abce769c3d241f944f8bde252434c4c59c4dade2c246c68224af469a684`); one Proceed for the whole PR-30 → PR-35 lifecycle; no second Proceed |
| Workspace | `/home/user/glow-hdengine-v2` (repository root; the same checkout that produced plan v1.0, finding F01 and plan v1.1) |
| Branch | `claude/gallant-wright-2f83bd` (operator-designated; first commit = plan v1.1 `92b4a3804ae3ec91c7d2bb988c030db898da0a89`) |
| Pull request | #501 (`https://github.com/amthorn78/glow-hdengine-v2/pull/501`), opened at PR-20 for plan v1.1 and reused at PR-30 as the one work vehicle; not draft |
| Implementation commit / tree | `abcb74a97821828f9603c05f9a8848ef6f4ddb4b` / `7b93607babb51864916894e816f9e44bf9a054df` |
| Remote head after the implementation push | `abcb74a97821828f9603c05f9a8848ef6f4ddb4b` (`git ls-remote`) |
| Records commit | the commit adding the result record, the ledger and this checkpoint; its SHA and the remote head after its push are recorded verbatim in the PR #501 body (a commit cannot embed its own SHA) |
| Base | `origin/main` merge-base `bce4c269989257f3a8d977da2a4a75fdbd2e8a61` |
| Plan / instruction | `docs/ephemeral/HDE-EPIC040-PR06-pr-implementation-plan-v1.1.md` / `docs/ephemeral/HDE-EPIC040-PR06-pr-instruction-v1.0.md` |
| F01 decision | `docs/ephemeral/HDE-EPIC040-PR06-F01-rescope-review-v1.0.md` (`APPROVE`, alternative A; conditions §4); drained as PF10 §2.21 |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.2.md` (`35fab8e9…5ce`; §§2.12, 2.15, 2.21 applied) |
| Release identity at checkpoint | `catalog/manifest.json` 44 members, `1.1.0`, `2026-08-24T18:04:49Z`; `release_id 988ed2a7c597631efc30662cfab1b16763d087434a64eb588985abed12d72f0e`; sanity log PASS model `88d787c11d58e3bd56e1d57008ef4cc2241510f9449c2fc9ce6eb1131ad3cdd7` |
| Result record | `docs/ephemeral/HDE-EPIC040-PR06-pr-implementation-result-v1.0.md` |
| Ledger | `docs/ephemeral/HDE-EPIC040-PR06-pr-remote-action-ledger-v1.0.md` |

## Constraints carried into PR-35

- Closed rails for every local run: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; dependencies as `ci.yml` installs them; the editable install must resolve `engine` from the checkout being validated; `setuptools >= 75` for the attestation's `pip wheel --no-build-isolation` (plan §10.1).
- Scope stays plan §§4–6 plus the PF10 §2.21 loci (the gate and its test home): `engine/**`, `.github/workflows/ci.yml`, `ci/jobs/**`, `tools/evidence/regenerate_identity_closure.py`, `tools/evidence/build_release_attestation.py`, `tools/evidence/run_sanity_pipeline*.py`, `tools/cli/generate_*`, the frozen captures and their digests, `artifacts/identity/*`, `schemas/hde_release_attestation*.json`, `docs/pfcanon/**` stay untouched; the 26 gate targets and six set rules stay untouched; no capture is re-identified (alternative B stays with PR07 / the Product Owner).
- Any change to a roster member's bytes (a review correction included) requires a re-cut through the cutter (`--roster-from-admission`) and a restart of the convergence at plan §5.7 step 4; any change to an evidence primary restarts at step 5; the sanity log's PASS model must be re-bound through plan §5.8 if it changes. Governed evidence only through its owners; nothing governed is hand-edited.
- No test skipped, disabled, quarantined or weakened; every F01 branch keeps its patched-provider coverage; no expected value is ever rewritten from actual output.
- Reviews come from Codex only; never install, trigger or rely on another reviewer product. Nathan merges; no auto-merge; `[skip ci]` only with Nathan's direct authorization for the identified push.
- Result vocabulary for PR-35: `MERGE_PENDING | MERGE_OBSERVED | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.
- Expected CI on this candidate: all seven lanes green (full validation), `RAILS_JOB_DEFINITIONS_OK` (never `RAILS_LANE:RELEASE_NOT_ADMITTED`), a built and verified attestation in the release lane (never a `release_not_admitted` receipt), final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. Any `RELEASE_NOT_ADMITTED` outcome on this candidate is a defect, not the interval.

## Unresolved items at checkpoint

- Codex code/security review of the pushed implementation head: unread (PR-35 entry action).
- Hosted CI for the pushed head: unobserved (PR-35 entry action); local lane equivalents were all green at `abcb74a97821828f9603c05f9a8848ef6f4ddb4b`.
- Mergeability of PR #501 after the implementation push: read once at publication (§12 of the result record); PR-35 re-reads it.
- Observations O-P06-16 … O-P06-20 in the result record (and O-P06-01 … 15 in the plan) are carried for their owners, not for this PR.
