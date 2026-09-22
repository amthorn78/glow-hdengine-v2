# HDE-EPIC040-PR04 — PR-30 durable checkpoint v1.0 (initial publication)

Recovery record for the one dedicated PR-development session. A resumed or uncertain entry re-reads this file, the result record and the ledger before creating any work.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR04 — Bounded application, identity and consumer integration |
| Session | `PR04-HDE-EPIC040-1` |
| Phase at checkpoint | PR-30 complete: `PR_CANDIDATE_PUBLISHED`; next phase PR-35 (same session) |
| Original Proceed | PR-30 Proceed for plan v1.2 (SHA-256 `dc005adc9ec0acd4541241f1893712d5c780f01632a09284aa6bd3d779779160`); implementation only |
| Workspace | `/home/user/glow-hdengine-v2` (repository root) |
| Branch | `claude/peaceful-gauss-jhyezn` |
| Pull request | #467 |
| Implementation commit / records commit | `881cc2df6ca79ab8564bba9d9e20013807ecf077` / the commit adding the result record, the ledger and this checkpoint (SHA recorded verbatim in the PR #467 body and in the ledger at PR-35 entry) |
| Remote head read back | `git ls-remote` after the single push of both commits; equals the records commit; recorded verbatim in the PR #467 body and in the ledger at PR-35 entry |
| Base | `origin/main` merge-base `3b8084d09e974f15c2b71112e5a596af01b1a371` |
| Plan / instruction | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.2.md` / `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md` |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md` (§2.15 present) |
| F01 / F02 | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` + addendum v1.0; `docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md` (Product Owner approval) |
| Result record | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-result-v1.0.md` |
| Ledger | `docs/ephemeral/HDE-EPIC040-PR04-pr-remote-action-ledger-v1.0.md` |

## Constraints carried into PR-35

- Closed rails for every local run: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` (+ `APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` in tests).
- Governed evidence only through its owners (`tools/evidence/update_evidence_index.py` is the sole index writer); `docs/pfcanon/` read-only; Google Drive is not a source or store.
- No test skipped, disabled, quarantined or weakened; no legacy success path; no admission bypass; no synthetic release fed to a governed gate or the attestation; `PR06R_B_FINAL_PASS` and `hde.release_attestation.v1` unchanged.
- Any corrective push that changes `adapter/http_reader.py` re-runs `python scripts/cut_release_manifest.py --version 1.0.0 --built-at-utc 2025-12-26T00:00:00Z`, the canonical gate write if its bytes change, and the updater; then the read-only checks.
- Reviews come from Codex only; never install, trigger or rely on another reviewer product. Nathan merges; no auto-merge; `[skip ci]` only with Nathan's direct authorization for the identified push.
- Result vocabulary for PR-35: `MERGE_PENDING | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.

## Unresolved items at checkpoint

- Codex code/security review of the pushed head: unread.
- Hosted CI for the pushed head: unobserved; the rails and release lanes are expected to end in the accepted `RELEASE_NOT_ADMITTED` outcomes.
- Observations O-03, O-06–O-10 in the result record are carried for their owners, not for this PR.
