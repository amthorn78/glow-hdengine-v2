# HDE-EPIC040-PR06b — PR-30 durable checkpoint v1.0 (initial publication)

Recovery record for the PR06b work unit. A resumed or uncertain entry (the dedicated PR-35 session, or an RS-40 return) re-reads this file, the result record and the ledger before creating any work.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08, alternative A), release re-cut to `1.3.0` |
| Session at checkpoint | the dedicated PR06b PR-development session (PR-20 and PR-30 phases; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_018Zth7shEF7GFWMU8jgFUjZ`); PR-35 runs in its own dedicated session |
| Phase at checkpoint | PR-30 complete: `PR_CANDIDATE_PUBLISHED`; next phase PR-35 |
| Original Proceed | Nathan / Product Owner's PR-30 invocation (the pasted PR-30 handoff, 2026-09-26) for exactly `HDE-EPIC040-PR06b-PR-IMPLEMENTATION-PLAN` v1.0 (SHA-256 `1672b1a86315063d04a3d649ed1b929ea85fdab9b51896af82ba7ed7bba13c8b`) with `HDE-EPIC040-PR06b-PR-INSTRUCTION` v1.0 (`d3d750cb51bd02c6fbbc38a5bfc8dd24d6b0f51398b450976a7629b643fb2696`); one Proceed for the whole PR-30 → PR-35 lifecycle; no second Proceed |
| Workspace | `/home/user/glow-hdengine-v2` (repository root; the same checkout that produced plan v1.0) |
| Branch | `claude/focused-heisenberg-91y3cn` (operator-designated; restarted from `origin/main` `d031f94` after PR #512 merged the plan; IF-01) |
| Pull request | #513 (`https://github.com/amthorn78/glow-hdengine-v2/pull/513`), created at PR-30 as the one work vehicle; not draft |
| Implementation head / tree | `acae4c637e2ce8c9e987953bcbe284f7e03719c9` / `9b3fbee142b02dcce285731f55f7bbe38c5b5232` (one commit above the base) |
| Remote head after the implementation push | `acae4c637e2ce8c9e987953bcbe284f7e03719c9` (`git ls-remote`) |
| Records commit | the commit adding the result record, the ledger and this checkpoint; its SHA and the remote head after its push are recorded in the pull request body (a commit cannot embed its own SHA) |
| Base | `origin/main` merge-base `d031f94a9cd0ef89f0fc50b37e86abe3cd90a643` |
| Plan / instruction | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` / `docs/ephemeral/HDE-EPIC040-PR06b-pr-instruction-v1.0.md` (both on `main`) |
| Overlay / decision | `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md` (drained as PF10 §2.24); `docs/ephemeral/HDE-EPIC040-PR06b-rescope-decision-v1.0.md` |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.5.md` (`7010511c…`; §§2.12, 2.21, 2.23, 2.24 applied) |
| Release identity at checkpoint | `catalog/manifest.json` 45 members, `1.3.0`, `2026-08-24T18:04:49Z`; `release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`; sanity log PASS model `88d787c11d58e3bd56e1d57008ef4cc2241510f9449c2fc9ce6eb1131ad3cdd7` (unchanged); `FROZEN_OPEN_ABBA_SHA256` `c78740b3f9d45472e67c3bdeef4ade9e4a9c74fc3e6b11bc2f29d1a90a323348`; v1 schema `42bd46c41e6ddf00d647c4a81ee3e797e07d50c4c8d18b58d07565e7301b6370`; g06 `c5eb83aec246444fe5d207f14e089b28d2cafc35c5d84ff49bc719b01c37b27a` |
| Result record | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.0.md` |
| Ledger | `docs/ephemeral/HDE-EPIC040-PR06b-pr-remote-action-ledger-v1.0.md` |

## Constraints carried into PR-35

- Closed rails for every local run: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL`, `GH_TOKEN` absent from the process environment (the container carries values for several; unset them); `python` on `PATH` must be the interpreter that carries pytest (the rails runner shells out to `python -m pytest`); the editable install must resolve `engine` from the checkout being validated.
- Scope stays plan §§4–6 (owned loci plus the one classified coherence dependent of plan §14.3, `tools/evidence/generate_open_rails_abba_proof.py`); `adapter/**`, `engine/compat/**`, both emitters, `engine/runtime/**`, `schemas/reader.v2.schema.json`, `errors/token_map/token_map.json`, `ci/checks/**`, `.github/workflows/ci.yml`, the cutter, the attestation builder, the sanity pipeline, the updater, `docs/pfcanon/**` and the frozen families stay untouched (plan §6.6).
- Any change to a roster member's bytes (`schemas/reader.v1.schema.json`, `engine/config/registry_loader.py`, or any other of the 45) requires a re-cut through `python scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` and a restart of plan §5.4 at step 4, with the engine-core owner whenever `engine/config/registry_loader.py` changes (plan §5.4 step 7b) and `FROZEN_OPEN_ABBA_SHA256` refreshed after the open-rails proof; any evidence primary restarts at step 5. Governed evidence only through its owners; nothing governed is hand-edited.
- No test skipped, disabled, quarantined or weakened; no expected value rewritten from actual output; `tests/reader_v1/test_cli_proof.py` stays untouched (plan D-13).
- Reviews come from Codex only; never install, trigger or rely on another reviewer product. Nathan merges; no auto-merge; `[skip ci]` only with Nathan's direct authorization for the identified push.
- Result vocabulary for PR-35: `MERGE_PENDING | MERGE_OBSERVED | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.
- Expected CI on this candidate: lanes `product`, `compat`, `evidence`, `release` plus the changed-test isolation step (the candidate does not change the classifier, so `db`, `rails` and `qa` are not selected); a built and verified attestation in the release lane (never a `release_not_admitted` receipt); final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. Any `RELEASE_NOT_ADMITTED` outcome on this candidate is a defect.

## Unresolved items at checkpoint

- Codex code/security review of the pushed implementation head: unread (PR-35 entry action).
- Hosted CI for the pushed heads: unobserved (PR-35 entry action); local lane equivalents were all green at `acae4c637e2ce8c9e987953bcbe284f7e03719c9`.
- Mergeability of the pull request: read once at creation (ledger L-11); PR-35 re-reads it.
- Observations O-P06b-13 and O-P06b-14 in the result record (and O-P06b-01 … 12 in the plan) are carried for their owners, not for this PR.
