# HDE-EPIC040-PR04 — PR-35 entry checkpoint v1.0 (session handoff)

Nonterminal interruption record. The Product Owner directed that PR-35 for this work unit be executed by a successor session because of context limits in the PR-30 session `PR04-HDE-EPIC040-1`. This file is the durable state at the handoff boundary; it changes no result, authority or scope. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED` (see `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-result-v1.0.md`, ledger `…-pr-remote-action-ledger-v1.0.md`, checkpoint `…-pr30-checkpoint-v1.0.md`).

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR04 — Bounded application, identity and consumer integration |
| Phase | PR-35 entered; no PR-35 result issued; no corrective push made |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/peaceful-gauss-jhyezn` |
| Pull request | #467 (open, not draft, base `main` at `3b8084d09e974f15c2b71112e5a596af01b1a371`) |
| Implementation commit / tree | `881cc2df6ca79ab8564bba9d9e20013807ecf077` / `475ba9b440fbcac6336e49cca2739097991dea88` |
| PR-30 records commit = remote head at PR-30 publication | `e7c5323a6db0eb651db3bf81c90c40efd95d3f70` (read back via `git ls-remote` and the PR head) |
| Original Proceed | PR-30 — PR Implementation Proceed — 091426.1 for plan v1.2 (`docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.2.md`, SHA-256 `dc005adc9ec0acd4541241f1893712d5c780f01632a09284aa6bd3d779779160`); implementation only; PR-35 continues under it, no new Proceed |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md` (§2.15 present) |
| Interrupted session's remote hooks | PR subscription and fallback check-in of session `PR04-HDE-EPIC040-1` released at handoff; the successor subscribes itself |

## Remote evidence read at handoff (2026-09-22, UTC)

- **CI run 35741951421** (`ci.yml`, run #3593, `pull_request`, head `e7c5323a`): job `test` **failed** at step "Run affected behavioral tests in isolation" (`4 failed, 2392 passed in 155.80s`); lanes product/compat/db/rails/evidence/qa/release were skipped as a consequence and the final step reported `APPLICABLE_CI_LANE_NOT_SUCCESSFUL` for changed-tests and each skipped lane. The changed-test step runs the classifier's 95 targets from a detached worktree with `PYTHONPATH` set to it, then requires `git diff --exit-code` and a clean tree.
- **Codex**: Code Review running on `e7c5323` since 14:40:36Z (no threads yet); Security Review completed only for `e927ed0` (PR-open head). A current-head security review is still owed.
- Combined commit status API returned 403 to the session's GitHub integration; use the Actions tools (run/job/logs) instead.

## The four failures, reproduced locally in a detached worktree (same command, closed rails)

| # | Test | Observed | Diagnosis (verified locally) |
| --- | --- | --- | --- |
| C-1 | `tests/compat/test_abba_parity.py::test_internal_compat_ab_ba_parity_is_canonical_bytes_identical` | 422 instead of 200 | The test posts legacy `{"person_uid": "alice"}` aliases to `/api/compat/v1`; the switched handler now refuses them per PF05 §5.2.3 with `ERR_M10_LEGACY_INPUT_UNSUPPORTED` ("legacy scoring input is unsupported"). The test was not among the plan's converted suites; it is an owner test of the changed handler (registered in `ci/checks/classify_ci_changes.py`). Smallest truthful fix: convert the test to seam inputs (complete fixture charts or canonical UUID identities, as `tests/http/test_compat_endpoint_contract.py` / `tests/support/pr04_fixtures.py` do), keeping its AB/BA byte-identity purpose. No handler change. |
| C-2 | `tests/compliance/test_logging_filter_keys_only_and_redactions.py::test_keys_only_log_and_redactions_and_echo_cid` | 503 instead of 200 | GET `/reader?v=1&a=fixtures/charts/alice.json&b=…` on the real app returns `ERR_M10_MANIFEST_MISMATCH` (503) because no admitted release exists (F01 posture). Every positive PR04 test injects the synthetic complete release via `tests.support.pr04_fixtures.inject_seams(monkeypatch, build_bundle(tmp), build_pack(tmp))`; this compliance test does not. Smallest truthful fix: add the seam injection to the test (its subject is the keys-only log line, not admission). No runtime change. |
| C-3 | `tests/evidence/test_epic030_pr05_category_framework_evidence.py::test_pr05_binding_passes_when_index_and_mirror_include_pr05_artifacts` | `ValueError` from `path.relative_to(ROOT)` | PR-30 moved the test root to `tmp_path` (outside the repository) but `_canonical_compare_line` in `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` renders paths relative to `ROOT`. The tests already monkeypatch every path constant; smallest truthful fix: also `monkeypatch.setattr(mod, "ROOT", test_root)` in both tests (ROOT is used only for those constants and the compare line). No generator change. |
| C-4 | `…::test_pr05_binding_fails_when_canonical_compare_fails` | same `ValueError` | same as C-3 |

These are test-side collisions inside the approved work unit, not a scope change (Product Owner direction: no atomic rescope for bounded in-unit collisions; record them in the result record §4 as P-18… and in the PR body).

## Required PR-35 sequence for the successor

1. Recover: read `AGENTS.md`, this file, the PR-30 result record, ledger and checkpoint; verify branch, remote head and PR #467 by read-back; subscribe to PR #467 activity.
2. Read all Codex code/security review content and thread state for the current head before pushing; resolve every substantive in-scope finding together with C-1…C-4 in one coherent corrective push.
3. Reproduce CI exactly: `git worktree add --detach <tmp> HEAD`; in it `export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<tmp>`; `python -m pytest -q -p no:cacheprovider -- $(cat <changed-test manifest>)` (manifest from `python ci/checks/classify_ci_changes.py --base <merge-base full SHA> --head <full SHA> --event-name pull_request --github-output <f> --changed-tests-output <manifest>`; both SHAs must be full hex); then `git diff --exit-code` and clean-tree check. Then rerun the lane equivalents listed in result record §8 and the read-only evidence checks.
4. If `adapter/http_reader.py` changes: `python scripts/cut_release_manifest.py --version 1.0.0 --built-at-utc 2025-12-26T00:00:00Z`, canonical gate write only if its bytes change, `python tools/evidence/update_evidence_index.py`, then read-only checks. Any other governed artifact changes only through its owner writer.
5. Update the result record (§4 corrections, §8 validation, §11 publication), the ledger (L-13 onward: remote head at PR-30 publication `e7c5323a…`, CI run 35741951421 failure, Codex state, corrective push) and a checkpoint; commit records with the corrective push (docs/ephemeral is CI-exempt); push once with `git push -u origin claude/peaceful-gauss-jhyezn`; read back remote head and PR; update the PR body's Publication section.
6. Verify exact-head CI (all seven lanes plus the accepted `RAILS_LANE:RELEASE_NOT_ADMITTED` and `RELEASE_LANE:RELEASE_NOT_ADMITTED` outcomes) and current-head Codex code and security review (request `@codex security review` once if it does not re-run for new commits); return `MERGE_PENDING` only when every predicate holds. Nathan merges manually.

## Constraints carried

Closed rails for every run; governed evidence only via owners (`update_evidence_index.py` sole index writer); `docs/pfcanon/` read-only; Google Drive is not a source or store; no test skipped, disabled, quarantined or weakened; no legacy success path; no admission bypass; no synthetic release fed to a governed gate or the attestation; `PR06R_B_FINAL_PASS` and `hde.release_attestation.v1` unchanged; Codex reviews only (never Claude Code Review); no merge, auto-merge or `[skip ci]` without Nathan's direct authorization; `rg` is unavailable (use grep/find); the container's system setuptools cannot run the attestation builder (use a fresh venv on a committed scratch snapshot).

## Other open items

- Observations O-03, O-06–O-11 in the result record are carried for their owners.
- `catalog/manifest.json` release_id `5fd293bf64f1196b8fba4e2856ed4cf2dcd9069d2a368a0fb6e331aafa16e360` binds the current `adapter/http_reader.py` bytes; recut if that file changes.
