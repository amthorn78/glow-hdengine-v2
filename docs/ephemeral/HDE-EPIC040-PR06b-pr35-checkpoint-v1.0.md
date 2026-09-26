# HDE-EPIC040-PR06b — PR-35 durable checkpoint v1.0 (records push)

This is the recovery record for the PR06b work unit at the PR-35 records push. A resumed or uncertain entry to this PR-35 session re-reads this file, result v1.1 and ledger v1.1 before creating any work. It advances the PR-30 checkpoint (`docs/ephemeral/HDE-EPIC040-PR06b-pr30-checkpoint-v1.0.md`, unchanged as issued).

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08, alternative A), release re-cut to `1.3.0` |
| Session at checkpoint | the dedicated PR-35 session (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_01XyLNkn9Ab1sB7kCUCJvodt`), subscribed to PR #513 |
| Phase at checkpoint | PR-35; result v1.1 is `MERGE_PENDING`, conditional on the records head (result v1.1 §1, *Final head*) |
| Original Proceed | Nathan / Product Owner's PR-30 Proceed for exactly plan v1.0 (`1672b1a8…13c8b`) with instruction v1.0 (`d3d750cb…2696`). One Proceed covers PR-30 → PR-35; there is no second Proceed |
| Workspace | `/home/user/glow-hdengine-v2` in this session's container. It is a fresh clone: PR-30's container is not reachable, and the repository, branch, pull request and records establish continuity |
| Branch | `claude/focused-heisenberg-91y3cn`. The harness branch `claude/wizardly-lamport-m1y87z` is absent on `origin` and was never committed to or pushed |
| Pull request | #513, open, not draft; the one work vehicle |
| Candidate code | the implementation commit `acae4c637e2ce8c9e987953bcbe284f7e03719c9` (tree `9b3fbee1…`). PR-35 made no code commit. The PR-30 records head `85e702b3259f4a549adc69d2f68fa36ddaefda57` differs from it only by three `docs/ephemeral/` files |
| Records commit | the commit adding result v1.1, ledger v1.1, this checkpoint and the conditional PR-40 handoff v1.0, directly above `85e702b3`. Its SHA and the remote head after its push are recorded in the PR #513 body and the PR-35 return |
| Base | `origin/main` merge-base `d031f94a9cd0ef89f0fc50b37e86abe3cd90a643`, unchanged |
| Release identity at checkpoint | `catalog/manifest.json` has 45 members, version `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z`; `release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`. `FROZEN_OPEN_ABBA_SHA256` is `c78740b3f9d45472e67c3bdeef4ade9e4a9c74fc3e6b11bc2f29d1a90a323348`, unchanged by PR-35 |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.5.md` (`7010511c…`), recorded as provenance |
| Result / ledger / handoff | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.1.md`; `docs/ephemeral/HDE-EPIC040-PR06b-pr-remote-action-ledger-v1.1.md`; `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.0.md` |

## Review and CI state at checkpoint

| Item | State |
| --- | --- |
| CR-01 (Codex P1, `PRRT_kwDOP103ks6mSA83`) | Not changed, out of scope, with evidence (result v1.1 §§4–5). O-P06b-15 goes to the open-rails proof owner. The reply and resolution follow the push |
| Security Review | completed on `acae4c6` with no finding. No correction landed, so none is re-requested |
| CI on `85e702b3` | run `36254322410` `success`, with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| Mergeability | `mergeable_state: clean` on `85e702b3` |
| Local at `85e702b3` | every result v1.1 §7 command exit 0 on Python 3.12.3 |
| Records head | its CI run is read after the push, through the subscription |

## Next action on re-entry

1. Read back `git ls-remote origin refs/heads/claude/focused-heisenberg-91y3cn` and PR #513. Confirm the head is the records commit and that nothing followed it.
2. Confirm the CR-01 thread reply and its resolution exist (the PR #513 body names them). Post whichever is missing.
3. Read the records head's `ci.yml` run in full, and any new Codex review, thread or comment.
4. If all is clean, result v1.1's `MERGE_PENDING` stands: return it with the conditional PR-40 handoff v1.0. If there is a finding or a failure, v1.1 no longer stands:
   - resolve it locally under closed rails;
   - issue result v1.2, ledger v1.2 and checkpoint v1.1 with one coherent corrective push;
   - if any roster member's bytes change, re-cut through `scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` and restart plan §5.4 at step 2, running the engine-core owner after every re-cut (O-P06a-23) and refreshing `FROZEN_OPEN_ABBA_SHA256` after the open-rails proof.
5. After Nathan's manual merge, if the subscription delivers it, return `MERGE_OBSERVED` with the PR-40 handoff.

## Constraints carried

- **Closed rails for every run:** `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, with `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL` and `GH_TOKEN` absent from the process environment.
- **Environment:** dependencies installed as `ci.yml` installs them; `python` on `PATH` is the interpreter that carries pytest; the editable install or `PYTHONPATH` resolves `engine` from the checkout being validated.
- **Scope:** plan §§4–6. `docs/pfcanon/**` is read only. Governed evidence changes only through its owners.
- **Tests:** no test is skipped, disabled, quarantined or deselected. `tests/reader_v1/test_cli_proof.py` stays untouched (D-13).
- **Remote actions:** Codex is the only reviewer. Never merge, enable auto-merge, schedule a merge or use `[skip ci]`. Notion is read only. Records go under `docs/ephemeral/` only.
- **Result vocabulary:** `MERGE_PENDING | MERGE_OBSERVED | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.
