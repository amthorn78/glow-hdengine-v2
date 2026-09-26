# HDE-EPIC040-PR06b — PR-35 durable checkpoint v1.1 (Product Owner-directed PF10 push)

This is the recovery record for the PR06b work unit at the second PR-35 push. A resumed or uncertain entry to this PR-35 session re-reads this file, results v1.1 and v1.2, and ledger v1.2 before creating any work. It advances PR-35 checkpoint v1.0 (`docs/ephemeral/HDE-EPIC040-PR06b-pr35-checkpoint-v1.0.md`) and the PR-30 checkpoint; both are unchanged as issued.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08, alternative A), release re-cut to `1.3.0` |
| Session at checkpoint | the dedicated PR-35 session (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_01XyLNkn9Ab1sB7kCUCJvodt`), subscribed to PR #513 |
| Phase at checkpoint | PR-35. Result v1.2 is `MERGE_PENDING`, conditional on the final head (result v1.2 §1, *Final head*); result v1.1's outcome is superseded by v1.2 |
| Original Proceed | Nathan / Product Owner's PR-30 Proceed for exactly plan v1.0 (`1672b1a8…13c8b`) with instruction v1.0 (`d3d750cb…2696`). One Proceed covers PR-30 → PR-35; there is no second Proceed |
| Product Owner direction | "include this PF10 update in your PR, and remove the old version" (this session, 2026-09-26). It was applied as commit `f9a655236ee7d445b913854d7e85685be7e78888`: `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.6.md` added byte-for-byte (`cc20d134…`), and `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.5.md` removed. This is not a PR06b delivery (result v1.2 §2) |
| Workspace | `/home/user/glow-hdengine-v2` in this session's container (a fresh clone; the repository, branch, pull request and records establish continuity) |
| Branch | `claude/focused-heisenberg-91y3cn`. The harness branch `claude/wizardly-lamport-m1y87z` is absent on `origin` and was never committed to or pushed |
| Pull request | #513, open, not draft; the one work vehicle |
| Candidate code | the implementation commit `acae4c637e2ce8c9e987953bcbe284f7e03719c9`. PR-35 made no code, test, evidence or roster change. Every later commit changes only `docs/ephemeral/` (`85e702b3`, `e34541b0`, and the v1.2 records commit) or `docs/pfcanon/` (`f9a65523`) |
| Records commit | the commit adding result v1.2, ledger v1.2, this checkpoint and conditional PR-40 handoff v1.1, directly above `f9a65523`. Its SHA and the remote head after the push are recorded in the PR #513 body and the PR-35 return |
| Base | `origin/main` merge-base `d031f94a9cd0ef89f0fc50b37e86abe3cd90a643` |
| Release identity at checkpoint | `catalog/manifest.json` has 45 members, version `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z`; `release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`. `FROZEN_OPEN_ABBA_SHA256` is `c78740b3…`, unchanged by PR-35 |
| PF10 | On `main` until the merge: v13.3.5. After the merge: v13.3.6 (`cc20d134…`), where the PR06b overlay is §2.25. Recorded as provenance (result v1.2 §3) |
| Result / ledger / handoff | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.2.md` (with v1.1); `docs/ephemeral/HDE-EPIC040-PR06b-pr-remote-action-ledger-v1.2.md`; `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.1.md` (handoff v1.0 is void) |

## Review and CI state at checkpoint

| Item | State |
| --- | --- |
| CR-01 (Codex P1, `PRRT_kwDOP103ks6mSA83`) | answered in `discussion_r4111998120` and resolved (`is_resolved: true`); dispositioned out of scope (result v1.1 §§4–5; result v1.2 §3) |
| Codex Code Review | `acae4c6`: one finding (CR-01). `e34541b`: completed 16:33:59Z with no new review, thread or comment. The final head is read after the push |
| Security Review | completed on `acae4c6` with no finding. No code correction landed, so none is re-requested |
| CI | `85e702b3`: run `36254322410` `success`. `e34541b`: run `36255782232` `success`. Final head: read after the push, through the subscription |
| Mergeability | `clean` on `85e702b3`; the final head is read after the push |

## Next action on re-entry

1. Read back `git ls-remote origin refs/heads/claude/focused-heisenberg-91y3cn` and PR #513. Confirm the head is the v1.2 records commit and that nothing followed it.
2. Read the final head's `ci.yml` run in full, and any Codex review, thread or comment on it.
3. Confirm the PR #513 body names the final head, the PF10 operation, the CI run and the thread state. Rewrite it if not.
4. If all is clean, result v1.2's `MERGE_PENDING` stands: return it with conditional PR-40 handoff v1.1. If there is a finding or a failure, v1.2 no longer stands:
   - resolve it locally under closed rails;
   - issue result v1.3, ledger v1.3 and checkpoint v1.2 with one coherent push;
   - if a roster member's bytes change, re-cut through `scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` and restart plan §5.4 at step 2.
5. After Nathan's manual merge, if the subscription delivers it, return `MERGE_OBSERVED` with the PR-40 handoff.

## Constraints carried

- **Closed rails for every run:** `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, with `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL` and `GH_TOKEN` absent from the process environment.
- **Environment:** dependencies installed as `ci.yml` installs them; `python` on `PATH` carries pytest; `engine` resolves from the checkout being validated.
- **Scope:** plan §§4–6. `docs/pfcanon/**` changes only by the Product Owner's direct, specific instruction (the `AGENTS.md` PO-directed exception); nothing beyond the one directed operation. Governed evidence changes only through its owners.
- **Tests:** no test is skipped, disabled, quarantined or deselected. `tests/reader_v1/test_cli_proof.py` stays untouched (D-13).
- **Remote actions:** Codex is the only reviewer. Never merge, enable auto-merge, schedule a merge or use `[skip ci]`. Notion is read only. Records go under `docs/ephemeral/` only.
- **Result vocabulary:** `MERGE_PENDING | MERGE_OBSERVED | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.
