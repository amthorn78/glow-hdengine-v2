# HDE-EPIC040-PR06a — PR-30 durable checkpoint v1.0 (initial publication)

Recovery record for the PR06a work unit. A resumed or uncertain entry (the dedicated PR-35 session, or an RS-40 return) re-reads this file, the result record and the ledger before creating any work.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06a — Reader v2 full Magic-10 and deferred Reader work |
| Session at checkpoint | the dedicated PR06a PR-development session (PR-20 and PR-30 phases; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_01EBvvgYQTXQqvSpd2eHtK8V`); PR-35 runs in its own dedicated session |
| Phase at checkpoint | PR-30 complete: `PR_CANDIDATE_PUBLISHED`; next phase PR-35 |
| Original Proceed | Nathan / Product Owner's PR-30 invocation for exactly `HDE-EPIC040-PR06a-PR-IMPLEMENTATION-PLAN` v1.0 (SHA-256 `48cf4120e4613b4fde38ebe26c99186ead627808593540155eb79e576aaa9d68`) with `HDE-EPIC040-PR06a-PR-INSTRUCTION` v1.0 (`b6e1c663fe19a073e519ef57455701d1b437c0fb9c12d284b4b0d6fb83220fcb`); one Proceed for the whole PR-30 → PR-35 lifecycle; no second Proceed |
| Workspace | `/home/user/glow-hdengine-v2` (repository root; the same checkout that produced plan v1.0) |
| Branch | `claude/admiring-tesla-h3awg8` (operator-designated; restarted from `origin/main` `547dc5b` after PR #507 merged the plan; IF-07) |
| Pull request | #508 (`https://github.com/amthorn78/glow-hdengine-v2/pull/508`), created at PR-30 as the one work vehicle; not draft |
| Implementation head / tree | `402db7214ce79fea472f388c71f5e671a55b7cc8` / `25c64aaa1a056a5602f0e889cc4c89c6747ce9eb` (six commits: `894bb6f6…`, `e2bd0247…`, `0c092e6e…`, `2b11d8f6…`, `a3336ad2…`, `402db721…`) |
| Remote head after the implementation push | `402db7214ce79fea472f388c71f5e671a55b7cc8` (`git ls-remote`) |
| Records commit | the commit adding the result record, the ledger and this checkpoint; its SHA and the remote head after its push are recorded in the PR #508 body (a commit cannot embed its own SHA) |
| Base | `origin/main` merge-base `547dc5b1198811483bc5b93585731558cdc3dcba` |
| Plan / instruction | `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-plan-v1.0.md` / `docs/ephemeral/HDE-EPIC040-PR06a-pr-instruction-v1.0.md` (on PR #506's head `dd9b9a8e…` until it merges) |
| Overlay / decision | `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` (drained as PF10 §2.23); `docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md` |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md` (`0029e282…`; §§2.12, 2.16–2.18, 2.21, 2.23 applied) |
| Release identity at checkpoint | `catalog/manifest.json` 45 members, `1.2.0`, `2026-08-24T18:04:49Z`; `release_id 5866c800b6dfff437b0ba2bf2ee8e655bd5d61262e335ea50bcc2625e53a285f`; sanity log PASS model `88d787c11d58e3bd56e1d57008ef4cc2241510f9449c2fc9ce6eb1131ad3cdd7`; `FROZEN_OPEN_ABBA_SHA256` `0e8f8f1aa09cf49596550cbb61fcd8a919715f869a65bfd788c1f1b56d2852e6` |
| Result record | `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.0.md` |
| Ledger | `docs/ephemeral/HDE-EPIC040-PR06a-pr-remote-action-ledger-v1.0.md` |

## Constraints carried into PR-35

- Closed rails for every local run: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `GEO_API_KEY`, `DATABASE_URL` absent from the process environment (the container carries values; `env -u`); `python` on `PATH` must be the interpreter that carries pytest (the rails runner shells out to `python -m pytest`); the editable install must resolve `engine` from the checkout being validated.
- Scope stays plan §§4–6 (owned loci + the four classified coherence dependents of §14.3); `engine/compat/**`, `engine/bodygraph/**`, `engine/cli/main.py`, `engine/presenter/emitter.py`, `scripts/hd_cli.py`, the cutter, the attestation builder, the sanity pipeline, the updater, `.github/workflows/ci.yml`, `docs/pfcanon/**` and the frozen families stay untouched (plan §6.6).
- Any change to a roster member's bytes (`adapter/http_reader.py`, `engine/runtime/public.py`, `presenter/reader_v1/emitter.py`, `schemas/reader.v1.schema.json`, `schemas/reader.v2.schema.json`, `engine/config/registry_loader.py`, or any other of the 45) requires a re-cut through `python scripts/cut_release_manifest.py --version 1.2.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` and a restart of plan §5.9 at step 2, with the A7 owner's write before the updater when the catalog changes (IF-02) and the engine-core owner when `engine/config/registry_loader.py` changes (IF-05); any evidence primary restarts at step 5. Governed evidence only through its owners; nothing governed is hand-edited.
- No test skipped, disabled, quarantined or weakened; no expected value rewritten from actual output; `tests/reader_v1/test_cli_proof.py` stays untouched (D-18).
- Reviews come from Codex only; never install, trigger or rely on another reviewer product. Nathan merges; no auto-merge; `[skip ci]` only with Nathan's direct authorization for the identified push.
- Result vocabulary for PR-35: `MERGE_PENDING | MERGE_OBSERVED | RESCOPE_PENDING | RECOVERY_PENDING | REMOTE_EVIDENCE_PENDING | PRODUCT_OWNER_DECISION_REQUIRED`.
- Expected CI on this candidate: all seven lanes green (full validation: the candidate changes `ci/checks/classify_ci_changes.py`), `RAILS_JOB_DEFINITIONS_OK` (never `RAILS_LANE:RELEASE_NOT_ADMITTED`), a built and verified attestation in the release lane (never a `release_not_admitted` receipt), final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. Any `RELEASE_NOT_ADMITTED` outcome on this candidate is a defect.

## Unresolved items at checkpoint

- Codex code/security review of the pushed implementation head: unread (PR-35 entry action).
- Hosted CI for the pushed heads: unobserved (PR-35 entry action); local lane equivalents were all green at `402db7214ce79fea472f388c71f5e671a55b7cc8`.
- Mergeability of PR #508: read once at creation (ledger L-11); PR-35 re-reads it.
- Observations O-P06a-16 … O-P06a-21 in the result record (and O-P06a-01 … 15 in the plan) are carried for their owners, not for this PR.
