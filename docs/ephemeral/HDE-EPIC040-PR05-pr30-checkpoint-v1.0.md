# HDE-EPIC040-PR05 — PR-30 durable checkpoint v1.0 (initial publication)

Recovery record for the PR05 work unit. A resumed or uncertain entry (the dedicated PR-35 session, or an RS-40 return) re-reads this file, the result record and the ledger before creating any work.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Session at checkpoint | the dedicated PR05 PR-development session (PR-20 and PR-30 phases; `role_session_ref: NOT_YET_ASSIGNED`); PR-35 runs in its own dedicated session |
| Phase at checkpoint | PR-30 complete: `PR_CANDIDATE_PUBLISHED`; next phase PR-35 |
| Original Proceed | Nathan / Product Owner's PR-30 invocation for exactly `HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN` v1.0 (SHA-256 `d50a6f1f8215124ee04fbce00538480352cf2513159b8df5030956b565675709`) with `HDE-EPIC040-PR05-PR-INSTRUCTION` v1.0 (`adb01ad8c0db18a9a8e45f6bfb183c15046aebd250a5dcbd509aa6d96f5d6ce7`); one Proceed for the whole PR-30 → PR-35 lifecycle; no second Proceed |
| Workspace | `/home/user/glow-hdengine-v2` (repository root; the same checkout that produced the plan) |
| Branch | `claude/beautiful-ritchie-6uvevf` |
| Pull request | #492 (`https://github.com/amthorn78/glow-hdengine-v2/pull/492`), opened by PR-30, not draft |
| Implementation commit / tree | `96b54dd870c6abe855af55140e13094ef896bbb6` / `c6d2238d2ff757626c6c1aee4d75c72adcd544c7` |
| Remote head after the implementation push | `96b54dd870c6abe855af55140e13094ef896bbb6` (`git ls-remote`) |
| Records commit | the commit adding the result record, the ledger and this checkpoint; its SHA and the remote head after its push are recorded verbatim in the PR #492 body (a commit cannot embed its own SHA) |
| Base | `origin/main` merge-base `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Plan / instruction | `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-plan-v1.0.md` / `docs/ephemeral/HDE-EPIC040-PR05-pr-instruction-v1.0.md` |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.md` (`d79e4110…6f91`; §2.15 PR04-F01 covers PR05) |
| Result record | `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md` |
| Ledger | `docs/ephemeral/HDE-EPIC040-PR05-pr-remote-action-ledger-v1.0.md` |

## Constraints carried into PR-35

- Closed rails for every local run: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; dependencies as `ci.yml` installs them.
- Scope stays plan §§4–6: only the nine owned/dependent paths; `engine/**`, `catalog/**` (incl. `catalog/manifest.json`), `schemas/**`, `migrations/**`, `adapter/**`, `presenter/**`, `goldens/**`, `.github/workflows/ci.yml`, `ci/jobs/**`, `tools/evidence/**`, the F01-enumerated files and `docs/pfcanon/**` stay untouched; no synthetic release reaches a governed gate or the attestation; no `PR06R_B_FINAL_PASS`; neither new tool exits `3`.
- Governed evidence only through its owners; nothing governed is hand-edited; no evidence writer runs for this unit (plan §6.3).
- No test skipped, disabled, quarantined or weakened; no expected golden value ever rewritten from actual output (plan §12 recovery rule).
- `tests/evidence/test_rails_ci_workflow_integration.py` pins the config-writer owner tuples and the configured-root roster — the reason for IF-01; a corrective push must keep the comparator tests inside `tests/config/test_config_artifacts.py` or route a change to that guard through its owner.
- Reviews come from Codex only; never install, trigger or rely on another reviewer product. Nathan merges; no auto-merge; `[skip ci]` only with Nathan's direct authorization for the identified push.
- Result vocabulary for PR-35: `MERGE_PENDING | MERGE_OBSERVED | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.
- Expected accepted CI outcomes on this candidate: `RAILS_LANE:RELEASE_NOT_ADMITTED`, `RELEASE_LANE:RELEASE_NOT_ADMITTED` (PF10 §2.15), final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

## Unresolved items at checkpoint

- Codex code/security review of the pushed head: unread (PR-35 entry action).
- Hosted CI for the pushed head: unobserved (PR-35 entry action); local lane equivalents were all green at `96b54dd8`.
- Mergeability of PR #492: unread.
- Observations O-09–O-12 in the result record are carried for their owners, not for this PR.
