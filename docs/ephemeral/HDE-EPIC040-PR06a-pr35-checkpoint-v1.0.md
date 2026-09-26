# HDE-EPIC040-PR06a — PR-35 durable checkpoint v1.0 (corrective and records push)

Recovery record for the PR06a work unit at the PR-35 push. A resumed or uncertain entry to this PR-35 session re-reads this file, result v1.1 and ledger v1.1 before creating any work. It advances the PR-30 checkpoint (`docs/ephemeral/HDE-EPIC040-PR06a-pr30-checkpoint-v1.0.md`, unchanged as issued).

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06a — Reader v2 full Magic-10 and deferred Reader work |
| Session at checkpoint | the dedicated PR-35 session (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_01QAme7bG6ZDJ5AEsYfRbLr9`) |
| Phase at checkpoint | PR-35; result v1.1 `MERGE_PENDING`, conditional on the records head (result v1.1 §1, *Final head*) |
| Original Proceed | Nathan / Product Owner's PR-30 Proceed for exactly plan v1.0 (`48cf4120…6aa9d68`) with instruction v1.0 (`b6e1c663…220fcb`); one Proceed for PR-30 → PR-35; no second Proceed |
| Workspace | `/home/user/glow-hdengine-v2` in this session's container (fresh clone; PR-30's container is not reachable, and the repository, branch, pull request and records establish continuity) |
| Branch | `claude/admiring-tesla-h3awg8`; the harness branch `claude/youthful-faraday-o3tsf8` is absent on `origin` and was never committed to or pushed |
| Pull request | #508, open, not draft; one work vehicle |
| Candidate code | `dc958ec568e55984d2c4a242cd4ff51726a132fb` (tree `0f29d0905e37036823877ec957d0ca3014131ab9`), one corrective commit above the PR-30 records head `b23c06f` |
| Records commit | the commit adding result v1.1, ledger v1.1, this checkpoint and the conditional PR-40 handoff v1.0, directly above `dc958ec`; its SHA and the remote head after its push are recorded in the PR #508 body and the PR-35 return |
| Base | `origin/main` merge-base `547dc5b1198811483bc5b93585731558cdc3dcba`; `main` at `cf9198d` (one unrelated `docs/ephemeral/` file) |
| Release identity at checkpoint | `catalog/manifest.json` 45 members, `1.2.0`, `2026-08-24T18:04:49Z`; `release_id 9f962ce338c448c7a2312f05695d5fdab12b01fbc1a67d490465d9fc87edab3f`; sanity log PASS model `88d787c1…`; `FROZEN_OPEN_ABBA_SHA256` `29223e6f8a30ed80f857a5ded666e13eab8b54440c14d068ac8c40330a1fdbda` |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md` (`0029e282…`), provenance |
| Result / ledger / handoff | `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.1.md`; `docs/ephemeral/HDE-EPIC040-PR06a-pr-remote-action-ledger-v1.1.md`; `docs/ephemeral/HDE-EPIC040-PR06a-conditional-PR40-handoff-v1.0.md` |

## Review and CI state at checkpoint

| Item | State |
| --- | --- |
| CR-01 (Codex P2, `PRRT_kwDOP103ks6mN-mX`) | fixed in `dc958ec` (IF-08); reply and resolution follow the push |
| CR-02 (Codex P1, `PRRT_kwDOP103ks6mOBEL`) | C040-08, out of scope, carried; reply and resolution as dispositioned follow the push |
| CR-03 (Codex P2, `PRRT_kwDOP103ks6mOBEM`) | pre-existing, out of scope, O-P06a-22; reply and resolution as dispositioned follow the push |
| Security Review | completed on `402db72` with no finding; one `@codex security review` request follows the push |
| CI on `b23c06f` | run `36220539219` `success` (diagnostic; superseded as a gate) |
| Local at `dc958ec` | every `ci.yml` step exit 0 on Python 3.12.3 (result v1.1 §7.2) |
| Records head | its CI run and Codex reviews are read after the push |

## Next action on re-entry

1. Read back `git ls-remote origin refs/heads/claude/admiring-tesla-h3awg8` and PR #508; confirm the head is the records commit and nothing followed it.
2. Confirm the three thread replies and resolutions and the security-review request exist (PR #508 body lists their ids); post whichever is missing.
3. Read the records head's `ci.yml` run in full and Codex's reviews of that head (reviews, threads, summary comment).
4. All clean: result v1.1's `MERGE_PENDING` stands; return it with the conditional PR-40 handoff v1.0. A finding or a failure: v1.1 no longer stands; resolve it locally under closed rails and issue result v1.2, ledger v1.2 and checkpoint v1.1 with one coherent corrective push. A change to any roster member's bytes needs a re-cut through `scripts/cut_release_manifest.py --version 1.2.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` and a restart of plan §5.9 at step 2, with the A7 owner before the updater and the engine-core owner after every re-cut (O-P06a-23).
5. After Nathan's manual merge, if the subscription delivers it: `MERGE_OBSERVED` with the PR-40 handoff.

## Constraints carried

Closed rails for every run (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, with `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `GEO_API_KEY`, `DATABASE_URL` and `DEV_SAMPLER_URL` absent from the process environment); dependencies as `ci.yml` installs them, with `python` on `PATH` the interpreter that carries pytest and the editable install resolving `engine` from the checkout being validated; `docs/pfcanon/**` read only; governed evidence only through its owners; no test skipped, disabled, quarantined or deselected; `tests/reader_v1/test_cli_proof.py` untouched (D-18); Codex is the only reviewer; never merge, enable auto-merge, schedule a merge or use `[skip ci]`; Notion read only; records under `docs/ephemeral/` only. Result vocabulary: `MERGE_PENDING | MERGE_OBSERVED | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.
