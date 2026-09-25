# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.1 (round 2)

Durable checkpoint saved with PR-35's second coherent corrective push and before the wait for remote-only evidence on the pushed head. It continues `docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md`, which is unchanged as issued. It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 2: a second coherent corrective revision, committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 round 1: corrective `2dad33c889260ab13f1de8aa8e0f81c972e1b067` and records `d677f5d6fd8885267c5cff4fad3949591de3e68f` (the remote head after the round-1 push). PR-35 round 2: corrective `ab5e6e7e23787bff59138468d989dadfd89ee40e` (tree `19717ee07580f090cc2b2b569d33792112490bcf`), and records = the commit adding this file and ledger v1.2. A commit cannot embed its own SHA: the records commit and the remote head read back after this push are recorded in the PR #492 body and in the next record |

## What happened after the round-1 push (2026-09-24, UTC)

- **Round-1 push.** `229d1f7..d677f5d` at 23:27:15Z, read back with `git ls-remote` and the PR API. Both round-1 Codex threads were answered (`discussion_r4099495949`, `discussion_r4099496201`) and resolved, and the PR description was updated.
- **CI on `d677f5d`.** `ci.yml` run `36072806572` (#3617), job `107877415216`, 23:27:21Z–23:37:21Z, conclusion `success`. It became stale as merge evidence at 23:31:07Z, when the round-2 findings arrived.
  - Cancellation was attempted through the Actions API and refused: `403 Resource not accessible by integration`. The run was left running, not waited on, and not treated as a gate.
  - Its success confirms that hosted CI agrees with the local lane equivalents for the round-1 code.
- **Codex on `d677f5d`.** Code Review `5311455402` (`COMMENTED`, 23:31:06Z, trigger "New commits") raised three P2 findings. The Security Review is still the PR-open one on `96b54dd`.
- **Fallback check-in.** A self check-in (`send_later`, trigger `trig_01PvS7o5YWsKiDKg4MFmGf2o`) was scheduled for 2026-09-25T00:01:00Z in case webhook events were late. It fired at 2026-09-25T00:02:09Z (`run_once_fired`), while round-2 validation was still running.

## Round-2 findings and dispositions

| ID | Source | Finding | Verification at `d677f5d` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-03 | Codex P2, comment `4099515019`, `tools/config/artifacts.py:328` | The collection's identity metadata (`source`, identity constants) is checked only for non-empty strings; it is never compared or consumed, so an altered collection reports `ok: true` | `source.sha256` = `"0"*64` with `constants.uuid_1` = `"arbitrary"` → exit 0, `ok: true`. Same result for `constants.synthetic_projection_fields.profile`, G002's `realizable_chart_claim`, G003's stated `inputs.operation`, and an unknown key in a G008 party | **Fixed in `ab5e6e7`** (IF-03, IF-04). Identity and annotations are pinned by `GOLDEN_ANNOTATION_SHA256`. Every input is consumed or closed |
| CR-04 | Codex P2, comment `4099515032`, `tools/config/artifacts.py:375` | `_golden_admit` catches only `SchemaValidationError`; other `RegistryConfigError` subclasses escape: exit 1, traceback | A synthetic root whose manifest lists `adapter/http_reader.py` twice → exit 1, `DuplicateIdError` | **Fixed in `ab5e6e7`.** Catches the `RegistryConfigError` base (Schema, DuplicateId, UnknownId, AliasPolicy), so the result is `CANDIDATE_ADMISSION_REFUSED:<code>` at exit 5. The loader already wraps its own I/O and schema-reference failures into `SchemaValidationError` |
| CR-05 | Codex P2, comment `4099515026`, `tools/config/artifacts.py:353` | An object or array provenance tag makes `set(provenance)` raise `TypeError`: exit 1 | `input_provenance: [{"x": 1}]` → exit 1, `TypeError: unhashable type: 'dict'` | **Fixed in `ab5e6e7`.** Tags must be strings before they are deduplicated, so the result is `GOLDENS_INVALID` at exit 5 |
| SR-03 | PR-35's own review of the diff; the same class as CR-04/CR-05 | A goldens document nested beyond the parser's recursion limit raises `RecursionError`. Separately, `_golden_diff` ran in the per-case `else:` branch, outside the per-case containment | 100,000-deep nesting → exit 1, `RecursionError` | **Fixed in `ab5e6e7`.** Deep nesting is `GOLDENS_INVALID`; a comparison that raises is that case's mismatch |

All are ordinary in-scope corrections to PR05's own new code; no rescope. CR-04 is a gap in PR-35's own round-1 review: the round-1 check searched only for plain `RegistryConfigError` raises, not its subclasses. This round mapped the whole exception hierarchy and every field the runners leave unconsumed.

**In-flight decision IF-03.** The collection's identity and annotations are pinned by one digest, not by field-by-field constants. The digest covers `schema`, `source`, `constants`, and each case's `title`, `case_type`, `kind`, `realizable_chart_claim`, `input_provenance` and `notes`. It is `GOLDEN_ANNOTATION_SHA256` = `c9ce74c3d055826235d16b26de4dbac31644d1a995c73c6844447c9b6e846a8a`: the SHA-256 of `sercanon` of that projection of the committed fixture, 5,320 bytes. It implements plan §5.1's closed schema (exact `source` and `constants`, PF01's per-case realizability claims) without copying PF01 prose into code. A change to the fixture's annotations must update the pin in the same commit, and `test_annotation_digest_pins_the_committed_transcription` fails until it does.

**In-flight decision IF-04.** Every input is consumed or closed:
- **Nested objects are closed:** party `{gates, person_uid}`, pair `{a, b, pair_id}`, adverse `{adverse_id, field, party, value}`, scenario `{owners, scenario_id}`, weighted channel `{channel_id, weight}`, and channel-state row `{channel_id, owner, state}`.
- **G003's stated definition is checked:** its `operation` and `channels` must equal the candidate's definition.
- **G005 pair ids are positional labels:** `pair_1`, `pair_2`, and so on.

A violation is that case's mismatch. The plan-required input alterations still yield their exact mismatches: plan §8.1 item 3, and `g008_identity_flip` unchanged.

## Corrective revision `ab5e6e7` (2 files, +187/−30)

| Path | Change |
| --- | --- |
| `tools/config/artifacts.py` | CR-03 (IF-03, IF-04), CR-04, CR-05, SR-03 |
| `tests/config/test_config_artifacts.py` | 27 items. 25 fail at `d677f5d`; the other 2 are regression guards for hashable non-string tags, which were already refused. The items: `test_unconsumed_or_unknown_input_fields_are_mismatches` (10); `test_annotation_digest_pins_the_committed_transcription` (1); `test_altered_identity_or_annotations_refuse` (10, including Codex's exact `source.sha256` + `uuid_1` example); `test_non_string_provenance_refuses` (4); `test_deeply_nested_goldens_refuse` (1); `test_every_registry_admission_error_is_a_refusal` (1) |

Untouched, as in round 1: everything plan §6.5 lists, including `ci/**`, the golden fixture, `tests/config/helpers.py`, the readiness tool, every F01-enumerated file and all governed evidence.

## Local validation at `ab5e6e7`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `ab5e6e7`.

| Check | Result |
| --- | --- |
| The 27 new test items | pass at `ab5e6e7`. 25 fail at `d677f5d` (the test file copied into a throwaway worktree); the other 2 are guards |
| Owner modules | 135 passed |
| Plan §10.2 focused and guard suites | 1,137 passed |
| Classifier dry-run (`--base 25b2c87… --head ab5e6e7… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 14 paths, 90 changed-test targets (the same 90 as round 1) |
| Changed-test isolation (detached worktree) | 2,433 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to round 1 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,023 passed, 3 skipped, diff 0, tree clean |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `ab5e6e7` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions. The known pre-existing failures are present on both sides |
| Comparator CLI | synthetic complete-release root: exit 0, all eight cases `match`, two runs byte-identical and byte-identical to the report at `229d1f7` for the same root (1,210 bytes, SHA-256 `77208a05b85e50363f15798c398ea5a692996d0151fb5a11ec65fe92d6c60300`; the report names the candidate root, so its size depends on that path). Repository root: exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` |
| Admission fuzz (scratchpad diagnostic, CR-04's class) | Every JSON roster member and the manifest of a synthetic complete-release root were mutated with type-confused values: `null`, `[]`, `{}`, `"x"`, `1`, `[null]`, `{"x": null}`, and key deletion. The six registry and mechanics catalog documents (`catalog/channels_v1.json`, `gates_v1.json`, `magic10.json`, `magic10_caps.json`, `magic10_seeds.json`, `magic10_mechanics_v1.json`), `math/thresholds.json` and the manifest were mutated to depth 2 (up to eight keys per object and the first element of each array); the other thirteen members were mutated to depth 1. After each member mutation the manifest was re-cut to bind it (a mutated manifest was used as written), and `_golden_admit` was called. 1,161 attempts: 238 admitted and 923 refused with a typed `CANDIDATE_ADMISSION_REFUSED:<code>` (18 distinct codes); no other exception escaped |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-2 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the three round-2 Codex threads with the pushed fix, and resolve them.
3. Exact-head CI on the pushed head, with all seven lanes, the accepted `RELEASE_NOT_ADMITTED` lane outcomes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
4. The Codex code review auto-triggered on the pushed head. Once it completes, one bare `@codex security review` request, as checkpoint v1.0 planned.
5. Then the final records and `MERGE_PENDING`, only if every predicate holds on one unchanged head. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
