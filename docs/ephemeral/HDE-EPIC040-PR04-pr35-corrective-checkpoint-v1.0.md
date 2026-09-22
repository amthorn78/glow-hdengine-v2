# HDE-EPIC040-PR04 — PR-35 corrective-push checkpoint v1.0

Durable checkpoint saved at the PR-35 coherent corrective publication, as the phase requires after every corrective push. It changes no result, authority or scope. The PR-30 result stands (`PR_CANDIDATE_PUBLISHED`); no PR-35 result is issued by this file.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR04 — Bounded application, identity and consumer integration |
| Phase | PR-35, after the one coherent corrective push; awaiting exact-head CI and current-head Codex reviews |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/peaceful-gauss-jhyezn` |
| Pull request | #467 (open, not draft, reused; base `main` `3b8084d09e974f15c2b71112e5a596af01b1a371`) |
| Original Proceed | PR-30 — PR Implementation Proceed — 091426.1 for plan v1.2 (`docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.2.md`, SHA-256 `dc005adc9ec0acd4541241f1893712d5c780f01632a09284aa6bd3d779779160`). PR-35 continues under it; no new Proceed |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md` (§2.15 present) |
| Implementation commit (PR-30) | `881cc2df6ca79ab8564bba9d9e20013807ecf077` (tree `475ba9b440fbcac6336e49cca2739097991dea88`) |
| PR-30 records commit / remote head at PR-30 publication | `e7c5323a6db0eb651db3bf81c90c40efd95d3f70` |
| PR-35 entry checkpoint commit | `73b9812ab09124333a313b2cbf1c638412d17468` (docs-only) |
| PR-35 corrective commit | `7b2bc5c95aa558961069a0a904ad7e4869a8469f` |
| PR-35 records commit | the commit adding this file and the result-record/ledger updates (a commit cannot embed its own SHA); the remote head read back after the push is recorded below |
| Remote head read back after the corrective push | `ed432acd50bcaf3dc39b089b9ddc83430f294923` (`git ls-remote`, equal to local `HEAD`) |
| Final branch head | This checkpoint was completed with that verbatim SHA in one follow-up docs-only commit, which becomes the final branch head. A commit cannot embed its own SHA, so that head is read back after its push and recorded in the PR #467 body and in ledger L-23 — the same convention the PR-30 records commit used. Because `pull_request` events evaluate `paths-ignore` against the whole PR diff, this push still runs CI, and `cancel-in-progress` supersedes the run on `ed432ac`, so exact-head CI evidence lands on the final head rather than on a superseded revision |

## What the corrective push contains

One coherent revision bundling the four CI changed-test failures with the Codex P1 finding, as the phase requires — not one push per finding.

| Item | Source | Disposition |
| --- | --- | --- |
| C-1 `tests/compat/test_abba_parity.py` | CI run 35741951421 | Converted to seam inputs; shape assertion re-bound to `schemas/magic10_compat_result_v1.schema.json` (result record §4 P-18) |
| C-2 `tests/compliance/test_logging_filter_keys_only_and_redactions.py` | same | `inject_seams` added (P-19) |
| C-3 / C-4 `tests/evidence/test_epic030_pr05_category_framework_evidence.py` | same | `mod.ROOT` monkeypatched with the other path constants (P-20) |
| Codex **P1** `adapter/http_reader.py` | Code Review on `73b9812` | Read bounded to the limit plus one byte; measured 5,000,102 → 32,769 bytes consumed; new regression test (P-21) |
| Codex **P2** `engine/compat/compute.py` packaging | Code Review on `73b9812` | Verified accurate; **not fixed here** — pre-existing, outside this PR's diff, unreachable in the CI and deployment shapes in use, and a distribution-surface change beyond the bounded work unit. Recorded as observation O-12 and answered on its thread |
| `catalog/manifest.json` | consequence of P-21 | Re-cut through its owner with the pinned arguments; `release_id` `5fd293bf…` → `a6db0106…`; canonical gate written once by its owner, Index/Mirror once by the sole updater |

## Verification carried into this checkpoint

All under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; full table in result record §8.1.

- CI changed-tests step reproduced exactly at the corrective head: **2397 passed** (was 2392 passed / 4 failed), `git diff --exit-code` 0, tree clean.
- Configured roster **1916 passed, 3 skipped** — identical to the PR-30 baseline.
- All seven lane equivalents green, including the accepted `RAILS_LANE:RELEASE_NOT_ADMITTED` and `RELEASE_LANE:RELEASE_NOT_ADMITTED` outcomes and the release receipt `{"code":"release_not_admitted","stage":"closure_write_and_check","returncode":3,"secret_values_recorded":false}` with the independent probe observing `INCOMPLETE_RELEASE_ROSTER`.
- The five pre-existing failures outside the CI lanes are unchanged; no test was skipped, disabled, quarantined or weakened.
- The container had no project dependencies at PR-35 entry; `requirements.txt`, `requirements-dev.txt`, `-e .` and a PyPI `setuptools` (84.0.0) were installed exactly as CI does before any figure above. The PyPI `setuptools` removes the PR-30 §9 limitation that had forced a separate venv for the attestation rehearsal.

## Still owed before `MERGE_PENDING`

1. Exact-head hosted CI: the changed-tests step plus all seven lanes on the corrective head.
2. Current-head Codex **code** review (the previous one was on `73b9812`).
3. Current-head Codex **security** review — the last completed one is on `e927ed0`, the PR-open head; request `@codex security review` once if it does not re-run for new commits.
4. Mergeability read back on the corrective head.

Nathan / Product Owner merges manually. Nothing in this phase enables, schedules or requests a merge.

## Constraints carried (unchanged)

Closed rails for every run; governed evidence only via owners (`update_evidence_index.py` sole index writer); `docs/pfcanon/` read-only; Google Drive is not a source or store; no test skipped, disabled, quarantined or weakened; no legacy success path; no admission bypass; no synthetic release fed to a governed gate or the attestation; `PR06R_B_FINAL_PASS` and `hde.release_attestation.v1` unchanged; PF12 wire values unchanged; Codex reviews only (never Claude Code Review); no merge, auto-merge or `[skip ci]` without Nathan's direct authorization; `rg` unavailable (use grep/find).
