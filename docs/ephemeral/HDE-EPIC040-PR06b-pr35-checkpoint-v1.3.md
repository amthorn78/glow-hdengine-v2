# HDE-EPIC040-PR06b — PR-35 durable checkpoint v1.3 (CR-02 records push)

This is the recovery record for the PR06b work unit at the fourth PR-35 push. A resumed or uncertain entry to this PR-35 session re-reads this file, results v1.1 to v1.4, and ledger v1.4 before creating any work. It advances PR-35 checkpoints v1.0 to v1.2 and the PR-30 checkpoint; all are unchanged as issued.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08, alternative A), release re-cut to `1.3.0` |
| Session at checkpoint | the dedicated PR-35 session (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_01XyLNkn9Ab1sB7kCUCJvodt`), subscribed to PR #513 |
| Phase at checkpoint | PR-35. Result v1.4 is `MERGE_PENDING`, conditional on the final head (result v1.4 §1, *Final head*); the outcomes of v1.1 to v1.3 are superseded by v1.4 |
| Original Proceed | Nathan / Product Owner's PR-30 Proceed for exactly plan v1.0 (`1672b1a8…13c8b`) with instruction v1.0 (`d3d750cb…2696`). One Proceed covers PR-30 → PR-35; there is no second Proceed |
| Product Owner direction | (1) "include this PF10 update in your PR, and remove the old version", applied as commit `f9a655236ee7d445b913854d7e85685be7e78888`: `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.6.md` added byte-for-byte (`cc20d134…`), and v13.3.5 removed (result v1.2 §2). (2) "A, remove the old PF10 versions too", applied as commit `43aa2d6b6d39c31291f1cc308f7b5756fade179f`: v13.3 to v13.3.4 removed (result v1.3 §2). Both were given in this session on 2026-09-26, and neither is a PR06b delivery |
| Workspace | `/home/user/glow-hdengine-v2` in this session's container (a fresh clone; the repository, branch, pull request and records establish continuity) |
| Branch | `claude/focused-heisenberg-91y3cn`. The harness branch `claude/wizardly-lamport-m1y87z` is absent on `origin` and was never committed to or pushed |
| Pull request | #513, open, not draft; the one work vehicle |
| Candidate code | the implementation commit `acae4c637e2ce8c9e987953bcbe284f7e03719c9`. PR-35 made no code, test, evidence or roster change. Every later commit changes only `docs/ephemeral/` (`85e702b3`, `e34541b0`, `20ca1c35`, `7309f2bf`, and the v1.4 records commit) or `docs/pfcanon/` (`f9a65523`, `43aa2d6b`) |
| Records commit | the commit adding result v1.4, ledger v1.4, this checkpoint and conditional PR-40 handoff v1.3, directly above `7309f2b`. Its SHA and the remote head after the push are recorded in the PR #513 body and the PR-35 return |
| Base | `origin/main` merge-base `d031f94a9cd0ef89f0fc50b37e86abe3cd90a643` |
| Release identity at checkpoint | `catalog/manifest.json` has 45 members, version `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z`; `release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`. `FROZEN_OPEN_ABBA_SHA256` is `c78740b3…`, unchanged by PR-35 |
| PF10 | On `main` until the merge: v13.3.5 (beside v13.3 to v13.3.4). After the merge: v13.3.6 (`cc20d134…`) is the only PF10 file, and the PR06b overlay is its §2.25. Recorded as provenance (result v1.2 §3) |
| Result / ledger / handoff | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.4.md` (with v1.1 to v1.3); `docs/ephemeral/HDE-EPIC040-PR06b-pr-remote-action-ledger-v1.4.md`; `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.3.md` (handoffs v1.0 to v1.2 are void) |

## Review and CI state at checkpoint

| Item | State |
| --- | --- |
| CR-01 (Codex P1, `PRRT_kwDOP103ks6mSA83`) | answered in `discussion_r4111998120` and resolved (`is_resolved: true`); dispositioned out of scope (result v1.1 §§4–5; result v1.2 §3) |
| CR-02 (Codex P1, `PRRT_kwDOP103ks6mSUll`) | dispositioned out of scope, in the same class as CR-01 (result v1.4 §§2–3). The reply and resolution follow the push. Later instances of the class are handled as result v1.4 §3 says |
| Codex Code Review | `acae4c6`: CR-01. `e34541b` (16:33:59Z) and `20ca1c3` (16:46:04Z): no new finding. `7309f2b` (16:53:40Z): CR-02. The final head is read after the push |
| Security Review | completed on `acae4c6` with no finding. No code correction landed, so none is re-requested |
| CI | `85e702b3`: run `36254322410` `success`. `e34541b`: run `36255782232` `success`. `20ca1c3`: run `36256453481` `cancelled` (superseded). `7309f2b`: run `36256852430`, superseded by this push while in progress. Final head: read after the push, through the subscription |
| Mergeability | `clean` on `85e702b3`; the final head is read after the push |

## Next action on re-entry

1. Read back `git ls-remote origin refs/heads/claude/focused-heisenberg-91y3cn` and PR #513. Confirm the head is the v1.4 records commit and that nothing followed it. Confirm the CR-02 reply and resolution exist, and post whichever is missing.
2. Read the final head's `ci.yml` run in full, and any Codex review, thread or comment on it.
3. Confirm the PR #513 body names the final head, both PF10 operations, the CI run and the thread state. Rewrite it if not.
4. If all is clean, result v1.4's `MERGE_PENDING` stands: return it with conditional PR-40 handoff v1.3. A later Codex finding of result v1.4 §3's class is handled as that section says. Any other finding or a failure means v1.4 no longer stands:
   - resolve it locally under closed rails;
   - issue result v1.5, ledger v1.5 and checkpoint v1.4 with one coherent push;
   - if a roster member's bytes change, re-cut through `scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` and restart plan §5.4 at step 2.
5. After Nathan's manual merge, if the subscription delivers it, return `MERGE_OBSERVED` with the PR-40 handoff.

## Constraints carried

- **Closed rails for every run:** `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, with `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL` and `GH_TOKEN` absent from the process environment.
- **Environment:** dependencies installed as `ci.yml` installs them; `python` on `PATH` carries pytest; `engine` resolves from the checkout being validated.
- **Scope:** plan §§4–6. `docs/pfcanon/**` changes only by the Product Owner's direct, specific instruction (the `AGENTS.md` PO-directed exception); nothing beyond the two directed operations. Governed evidence changes only through its owners.
- **Tests:** no test is skipped, disabled, quarantined or deselected. `tests/reader_v1/test_cli_proof.py` stays untouched (D-13).
- **Remote actions:** Codex is the only reviewer. Never merge, enable auto-merge, schedule a merge or use `[skip ci]`. Notion is read only. Records go under `docs/ephemeral/` only.
- **Result vocabulary:** `MERGE_PENDING | MERGE_OBSERVED | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.
