# HDE-EPIC040-PR06a — PR Implementation Result v1.0 (PR-30)

| Field | Value |
| --- | --- |
| Artifact | `PR_IMPLEMENTATION_RESULT` — `HDE-EPIC040-PR06a-PR-IMPLEMENTATION-RESULT` v1.0, the PR-30 phase record (implementation, local verification, initial publication) |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06a — Reader v2 full Magic-10 and deferred Reader work (overlay PF10 §2.23, C040-07) |
| Change | `EPIC / HDE-EPIC040`; `HDE-EPIC040-SPECIFICATION` v1.1 (`SPECIFICATION_APPROVED`); PR06a rescope decision v1.0 |
| Producer | the dedicated HDE-EPIC040-PR06a PR-development session (PR-20 and PR-30 phases; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_01EBvvgYQTXQqvSpd2eHtK8V`); `EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION` |
| Result | `PR_CANDIDATE_PUBLISHED` — one coherent, locally tested candidate deliberately published as pull request #508 |
| Prompt | PR-30 — PR Implementation Proceed — 091426.1 (`https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`; Notion read only) |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/admiring-tesla-h3awg8` (operator-designated) |
| Pull request | [#508](https://github.com/amthorn78/glow-hdengine-v2/pull/508), the one work vehicle, created at PR-30 (no open PR existed for this work unit or branch before it; the only open PR was #506, the instruction record) |
| Base | `origin/main` merge-base `547dc5b1198811483bc5b93585731558cdc3dcba` (= `main` at planning time, re-fetched before the push: unchanged) |
| Implementation head / tree | `402db7214ce79fea472f388c71f5e671a55b7cc8` / `25c64aaa1a056a5602f0e889cc4c89c6747ce9eb` (six commits above the base, 128 files, +1,891/−465) |
| Records commit | the commit adding this record, the ledger and the PR-30 checkpoint; a commit cannot embed its own SHA, so its SHA and the remote head after its push are recorded in the PR #508 body and in the ledger's final row |
| Recorded by | the dedicated PR06a session, 2026-09-26 (UTC); implementation ran 2026-09-26 between roughly 04:10Z and 05:14Z after the Proceed |

## 1. Outcome

**`PR_CANDIDATE_PUBLISHED`.** The approved PR06a scope (plan v1.0 §§4–6, overlay PF10 §2.23) is implemented on one branch, locally verified per plan §10 with the vendor and DB keys absent, and published as one pull request. This record is historical PR-30 evidence: it claims no review outcome, no hosted-CI outcome, no QA verdict, no acceptance, no PF09 movement, no OPS01 attestation, no C040-07 canon drainage, no deployment, no activation and no closure. PR-35 (own dedicated session) owns review retrieval, corrections, current-head CI and merge readiness; Nathan merges.

- **Scope.** Every completion condition of plan §4.2 is met on the implementation head: Reader v2 at `POST /api/reader?v=2` (ten `{id, band}` items in the canonical governed order, `[]` when ineligible, `reader_version "v2"`, same preimage/AB-BA/two-run rules); Reader v1 byte-for-byte unchanged (pinned to a pre-change golden); the production Reader mounted under `/api` by every app factory with governed 405s elsewhere; the Reader v1 schema conformed (F05) and the Reader v2 schema added as the 45th release member; goldens through their writer; the production-row endpoint catalog through the A7 owner; F07 dev conjunction evidence as a closed-rails deterministic capture with the admitted identity; the release re-cut to `1.2.0` / 45 members with every governed family converged by its owner and byte-stable on a second run.
- **Local validation.** Every lane of `.github/workflows/ci.yml`, the changed-test isolation step, the candidate-wide roster and the attestation rehearsal were run at the implementation head (§7). One failure remains and is pre-existing on `main` (`tests/reader_v1/test_cli_proof.py`, plan D-18).
- **In-flight decisions.** Seven (§6): one plan text defect (a token message), one convergence-order adjustment, three test repairs the plan's inventory did not anticipate, one governed evidence family (engine-core) that binds a changed member's digest, and the work-vehicle decision. None is material; no rescope was raised.
- **Not done, by rule.** No merge, auto-merge, `[skip ci]`, second PR or branch, Notion write, `docs/pfcanon/` write, Claude Code Review installation or trigger.

## 2. Authority, identity and controlling sources

| Source | Exact identity | Repository path |
| --- | --- | --- |
| Product Owner Proceed | Nathan's pasted PR-30 invocation: "This invocation is the Product Owner's Proceed for exactly HDE-EPIC040-PR06a-PR-IMPLEMENTATION-PLAN v1.0 and HDE-EPIC040-PR06a-PR-INSTRUCTION v1.0" (`session_disposition: RETAIN_EXISTING`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06a / PR-30`; `context_conflict: NONE`). One Proceed for the PR-30 → PR-35 lifecycle; no second Proceed | pasted invocation (this session) |
| Detailed PR plan | v1.0, SHA-256 `48cf4120e4613b4fde38ebe26c99186ead627808593540155eb79e576aaa9d68` (124,954 bytes; on `main` via PR #507, squash-merged as `547dc5b`) | `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-plan-v1.0.md` |
| PR instruction | v1.0, SHA-256 `b6e1c663fe19a073e519ef57455701d1b437c0fb9c12d284b4b0d6fb83220fcb` (12,599 bytes); still only on PR #506's head `dd9b9a8e9549bb10b742a9123305f00f73b9a969` (open, unmerged at publication) | `docs/ephemeral/HDE-EPIC040-PR06a-pr-instruction-v1.0.md` (PR #506) |
| PF10 overlay (addendum) | v1.0, SHA-256 `a69e2205de410bf6332bb558f3ee0110e3524b7143a84591bbed18ff476528e9`; drained as PF10 §2.23 (C040-07, NEW_CANON, approved) | `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` |
| Rescope decision | v1.0, SHA-256 `0c3d4ad718cbed410f1d248fcea5f1772b140bd06bc2866bc0ecc4257a7e8a55` | `docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md` |
| Current PF10 read | PF10 — HDE Build Notes v13.3.4, SHA-256 `0029e2827904f6b798f6367f54a8d134bb55d170a412cc544b1555594c4e4f29` (the unique current Markdown under `docs/pfcanon/`; applied §§2.12, 2.16–2.18, 2.21, 2.23) | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md` |
| Immutable approved base | as plan v1.0 §2.1 (Specification v1.1, Implementation Audit v2.0, Implementation Plan v2.1, Plan Review v2.1, accepted PR01–PR06) | plan §2.1 paths |

No Google Doc, DOC, DOCX or Drive copy was opened. Notion was read only (the PR-30 prompt at invocation; the PR-35 page identity resolved by search for the handoff). `docs/pfcanon/` was read only.

## 3. Recovery and baseline before any work vehicle was created

- **Workspace.** `/home/user/glow-hdengine-v2`, the same checkout that produced plan v1.0. Scratch clones from planning (`rehearsal`, `rehearsal2`, `rehearsal3` under the session scratchpad, never pushed) were inspected and left untouched; nothing from them was copied except the rehearsed v2 schema draft, re-canonicalized and corrected (IF-01).
- **Prior work of this plan cycle.** None: no implementation commit, worktree, PR or `docs/ephemeral/` PR06a result/ledger/checkpoint existed. PR #507 (the plan) was squash-merged as `547dc5b` and is landed history; PR #506 (the instruction) is open and is not an implementation vehicle.
- **Work vehicle (IF-07).** The operator-designated branch `claude/admiring-tesla-h3awg8` existed on `origin` at `c4ddf4d643e908f24399fdaaaeff8c24480e3899` — exactly the plan commit that PR #507 merged (its tree equals `main`'s tree). Per the harness rule for a merged designated branch, the branch was restarted from `origin/main` (`git checkout -B claude/admiring-tesla-h3awg8 origin/main`) and, at publication, pushed with `--force-with-lease` against that exact remote SHA, replacing only already-merged history. One branch, one PR (#508).
- **Environment.** Python 3.11.15 virtualenv with `pip install -e .` bound to this checkout (CI uses 3.12); `python -m pytest --version` → pytest 8.4.2; every command under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` with `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `GEO_API_KEY` and `DATABASE_URL` removed from the process environment (`env -u` / `unset`; the container carries values for four of them). No vendor call and no database connection occurred in PR-30.
- **Baseline re-verified.** `origin/main` = `547dc5b` (unchanged from planning through publication); manifest 44 rows / `1.1.0` / `release_id 988ed2a7c597631efc30662cfab1b16763d087434a64eb588985abed12d72f0e`; the pre-change dev `GET /reader` bytes for `fixtures/charts/{alice,bob}.json` under a fixed synthetic identity were captured from a detached worktree at `547dc5b` and pinned as a golden in `tests/http/test_reader_post_v1.py`.

## 4. Implemented scope (plan §§5–6; checkpoints C1–C5)

### 4.1 Commit series (one branch, in plan §9 order)

| Commit | Committed (UTC) | Subject |
| --- | --- | --- |
| `894bb6f68e7b28fca7c9027bafbb5f68251a5b93` | 2026-09-26T04:32:25+00:00 | feat(reader): Reader v2 full Magic-10 on POST /api/reader; production route under /api (HDE-EPIC040-PR06a C1) |
| `e2bd02470a1a3ff6cb5ec71cec8988d0a189d5c4` | 2026-09-26T04:32:25+00:00 | feat(schemas): Reader v1 F05 conformance and new Reader v2 schema; goldens through their writer (HDE-EPIC040-PR06a C2) |
| `0c092e6eb1509183c262f3e812fab74c5312a503` | 2026-09-26T04:35:46+00:00 | feat(evidence): production Reader catalog row and closed-rails F07 dev conjunction evidence owners (HDE-EPIC040-PR06a C3) |
| `2b11d8f691a9c70c96109ffecf9b50646691f4ed` | 2026-09-26T04:38:13+00:00 | ci(classifier): register PR06a paths; pin the 45-member 1.2.0 release identity in tests (HDE-EPIC040-PR06a C4) |
| `a3336ad20b712e7ec14fc709b6c01f6d2ff7e086` | 2026-09-26T04:43:50+00:00 | release: cut 1.2.0 (45 members) and converge governed evidence through their owners (HDE-EPIC040-PR06a C5) |
| `402db7214ce79fea472f388c71f5e671a55b7cc8` | 2026-09-26T05:00:02+00:00 | fix(evidence,tests): regenerate engine-core evidence via its owner; repair tests invalidated by the F05 schema and the re-cut (HDE-EPIC040-PR06a C5b) |

### 4.2 Owned and dependent code, schemas, goldens and tests

| Path | What changed | Plan |
| --- | --- | --- |
| `adapter/http_reader.py` | `_select_reader_version(allowed)` over `request.args.getlist("v")` (exactly one value in `allowed`, else `ERR_READER_INVALID_VERSION` 400 before any body read or lookup); `_evaluate_reader_pair` → `(eligible, bands, release_id)` with `bands` the ordered `(category_id, band)` rows of the validated result (first row must be `harmony`, else `CompatBoundaryError("result_schema")`); shared `_production_reader_response(emit_fn)`; `get_reader_api_bp` / `api_bp` (`Blueprint("reader_api")`: `POST /reader`, method-catch `GET, HEAD, OPTIONS, PUT, PATCH, DELETE` → governed 405 `Allow: POST`); unprefixed `POST /reader` → governed 405 `Allow: GET, HEAD`; dev `GET /reader` accepts `v=1` only; `_error` and `_reader_method_not_allowed` at module level; `_dev_conjunction_local_lookup()` reads `current_app.config["DEV_CONJUNCTION_LOCAL_LOOKUP"]` (callable or `None`) inside `_emit_conjunction_response`; `create_app` mounts `api_bp` at `/api` | §§5.1–5.3, 5.8 |
| `adapter/factory.py`, `adapter/wsgi.py` | `app.register_blueprint(api_bp, url_prefix="/api")` next to the existing registration | §5.2 |
| `engine/runtime/public.py` | `emit_reader_public_envelope(..., reader_version="v1", categories=None)`; `_v1_categories` (unchanged bytes); `_v2_categories` (accepts `(id, band)` pairs or `{id, band}` items; ids must equal `FROZEN_MAGIC10_ORDER`; bands in the enum; ineligible must be empty → `[]`); `emit_reader_public_bytes` forwards both keywords | §5.3 |
| `presenter/reader_v1/emitter.py` | `_clean_category` (exactly `{id, band}`, `prompt` refused, D-05); v1 set semantics kept; `_ordered_categories_v2` (ten in canonical order, never sorted; `[]` when ineligible); `_build_preimage_v2`; shared `_emit`; `emit_reader_v2` | §5.3 |
| `schemas/reader.v1.schema.json` + `.sha256` | canonical bytes (1,690 B); `category_id` enum `["harmony"]`; category `{id, band}` closed; `$defs.success` closed with the eligible/categories coupling; `$defs.error` semantics unchanged; root `oneOf [success, error]`; sidecar in `sha256sum` format | §5.4 |
| `schemas/reader.v2.schema.json` + `.sha256` | new, canonical bytes (4,271 B), draft 2020-12, `$id https://example.org/schemas/reader.v2.schema.json`; `prefixItems` of the ten ids in canonical order, `items: false`, `minItems`/`maxItems` 10; error branch of the twelve exact token/message pairs bound to `ERROR_TOKEN_MAP` (IF-01) | §5.5 |
| `scripts/make_reader_v1_goldens.py`; `goldens/reader/v1/*`; `goldens/reader/v2/*` | v1 covenant set (`g01` and `g06` byte-identical to before; `g02_A/B.jsonl` two identical harmony envelopes; `g03_harmony_open`, `g04_harmony_warm`, `g05_harmony_cool`, `g07_harmony_glow`; `*_leader` files and sidecars removed); v2 set (`g01_ineligible`, `g02_ab_ba_parity_A/B.jsonl`, `g03_eligible_ten_in_order`, `g04_error_invalid_version` = real `error_envelope` bytes); hash-only sidecars; written by the script | §5.6 |
| `scripts/make_release_pack.sh`; `artifacts/release_pack_manifest.json`; `artifacts/release_id.txt` | default list renamed; both tracked outputs regenerated by running the script (byte-idempotent under `tests/reader_v1/test_release_pack.py`) | §5.6 |
| `tools/evidence/generate_a7_transport_proofs.py` | `PRODUCTION_READER_PATH = '/api/reader'`; the `public_reader` row after `/api/compat/v1`; validator rule (exactly one `POST /api/reader`, `public_reader`, `internal False`, `a7_eligible False`); the PF05 §5.3 POST probe on the production route; `PROOFS[4]` text `POST /api/reader` | §5.7 |
| `tools/evidence/generate_conjunction_writer_evidence.py` | `_require_closed_rails` (refuses unless `SAFE_MODE=1` and `ALLOW_NETWORK=0`); `_fixture_rows()` (two `MappedBodyGraphRow`s from `fixtures/charts/alice.json` ("left") and `bob.json` ("right") rebased to `resolve_db_user_id` ids, `vendor "hdapi"`, `vendor_version 2`, `input_fingerprint` = SHA-256 of the fixture's canonical `bodygraph`, `payload = project_bodygraph(chart)`); control request without the seam first; seam installed as `app.config["DEV_CONJUNCTION_LOCAL_LOOKUP"] = rows.get`; eleven checks incl. `seam_absent_refuses_closed_rails`, `writer/reader_admitted_release_identity`, `no_dev_identity_stamp`; summary `conjunction_writer_summary.v2` with `release_id` and `rails: closed`; log `conjunction_write_readback.log.v2`; `DATABASE_URL` neutralized in both modes; `dev_compat_identity` no longer imported | §5.8 |
| `tools/evidence/generate_open_rails_abba_proof.py` | `FROZEN_OPEN_ABBA_SHA256` `3e78fcdb…` → `0e8f8f1aa09cf49596550cbb61fcd8a919715f869a65bfd788c1f1b56d2852e6` | §5.9 step 7 |
| `engine/config/registry_loader.py` | `"schemas/reader.v2.schema.json"` in `ADMITTED_RELEASE_ROSTER`; `!= 45`; `ADMITTED_RELEASE_VERSION = "1.2.0"`; nothing else | §5.9 |
| `catalog/manifest.json` | cut by `python scripts/cut_release_manifest.py --version 1.2.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`: 45 rows, `1.2.0`, `2026-08-24T18:04:49Z`, `release_id 5866c800b6dfff437b0ba2bf2ee8e655bd5d61262e335ea50bcc2625e53a285f` | §5.9 |
| `ci/checks/classify_ci_changes.py` | exactly the §5.11 registrations (`adapter/factory.py`, `adapter/wsgi.py`, `schemas/reader.v2.schema.json` (+`.sha256`), `scripts/make_reader_v1_goldens.py`, `scripts/make_release_pack.sh`; `engine/runtime/public.py` + v2 test; `presenter/reader_v1/emitter.py` + emitter test; `goldens/reader/` fixture lanes and owners; `generate_conjunction_writer_evidence.py` evidence owner; `tests/http/test_reader_post_v2.py` in `_HTTP_READER_TEST_OWNERS`) | §5.11 |
| Tests | new `tests/http/test_reader_post_v2.py` (plan §8.1 cases 1–11, 29 tests); `tests/http/test_reader_post_v1.py` (`/api/reader`; duplicated/malformed `v`; `POST /reader` 405; recomputed identity; pre-change dev-GET golden); `tests/http/test_reader_a7_transport.py` (§8.3); `tests/http/test_endpoint_catalog.py` (§8.4); `tests/transport/test_a7_transport_proofs.py` (§8.5); `tests/reader_v1/test_schema.py`, `test_goldens.py`, `test_emitter.py`, `test_release_pack.py` (§8.6); `tests/evidence/test_dev_conjunction_identity.py`, `tests/http/test_dev_conjunction_http.py` (§8.7); the 27 pinned rewrites of §8.8 plus two docstrings; `tests/runtime/test_identity.py` (§8.10); `tests/evidence/test_rails_ci_workflow_integration.py` (pinned owner tuple, §6.2); repairs of §6 IF-03/IF-04. `tests/reader_v1/test_cli_proof.py` untouched (D-18) | §8 |

### 4.3 Governed evidence regenerated by its owners (never hand-edited)

Canonical JSON gate (`audit/gates/canonical_json/*`, `audit/gates/json_gate/canonical/*`); A7 family (`docs/ENDPOINTS_CATALOG.json` — a tracked symlink to `artifacts/audit/ENDPOINTS_CATALOG.json`, both SHA-256 `acb7830656c4aa61451130154110fc30353173a662e11bf74add17c289382b02` — with `.sha256` companions, `artifacts/reader/endpoints_snapshot.json` byte-identical as predicted, and the seven proofs incl. `artifacts/proofs/success_writers_errors.txt` `b1ab25e79d3f16ae50d03a9ae2b74c045e0fabb91f8de0911786772096ce6584`); config family logs; determinism family (`audit/gates/parity/reader_cli/*`, `audit/gates/determinism/abba.bytes`, `tworun_identity.sha256`); open-rails fixture proof `audit/gates/determinism/open_rails_abba.json` `0e8f8f1a…`; F07 artifacts `artifacts/writer/conjunction_write_readback.log` `d467f82af98f9700487d49cec6af8f06649fdb5ec89e7b47060edb3c465c5e9b` and `conjunction_writer_summary.json` `fa8cad2d05336065ce3353b4416d4e33d0b3464c6e572c4db46fe01abd04caaa`; engine-core evidence `artifacts/core/*` (IF-05); Index `docs/evidence/INDEX.json` `163fbc218ebb9c09621bac0a23ac52a5d8363618c0a56f5035efdc5f2687bdbc`, Mirror `artifacts/evidence_index.jsonl` `8e0abd5fd16f46e554fafcf9c467caa9f36211f6d5dc9b2845a39080e2d74d42` and every path proof through the sole updater; sanity log `audit/gates/sanity_pipeline/sanity_pipeline.log` `88d787c11d58e3bd56e1d57008ef4cc2241510f9449c2fc9ce6eb1131ad3cdd7` (PASS model, byte-identical to the tracked bytes before and after the cut). Frozen families (plan §6.4) unchanged; their `--check` modes exit 0.

### 4.4 Member digests (before → after)

| Member | Before (`547dc5b`) | After (`402db72`) |
| --- | --- | --- |
| `adapter/http_reader.py` | `3a6bd46a964a5f76c43885fd0d2efdd256842d3908611f780aea028894ef7066` | `351a0611c36cd645b77d1587c06ef8fbd29f7d7387dad92d54f06b58d61ed258` |
| `engine/runtime/public.py` | `1d218315aa27d2bd30a87bb75c8951d632db2a259f6fc0cd9d4ec794c08a14ca` | `082b3daf8d4c9e588138ead0b851a48023f98619436a489c925d33092474621e` |
| `presenter/reader_v1/emitter.py` | `431bb58488d658e4b028f27af55d30cc3f043c187153e212abcbedb240a59fc2` | `55db0bc3b370b1d21d97a29aa7b3cb503c22265f394e15b00f5ee144e4bf3483` |
| `schemas/reader.v1.schema.json` | `ecfc205422034e0070dfc2a58b500012e24d02464c5b98f4034def86ea9c7550` | `5af896521f76b24833290d46de22ac6a4136021c5034399a68c9533f2e096f84` |
| `schemas/reader.v2.schema.json` | — (new) | `c9ee5c5d0f1a2c0724bda24963f905dbdfec9c561283457562da8019be8fbe48` |
| `engine/config/registry_loader.py` | `5e3146832115003137f6448e25228b83574948d565120697d20ed4254e22135c` | `fa1e6315cc5a8975791bfa52b09714787d45d4427cf6dfc16d22f8d64e218e5d` |
| `catalog/manifest.json` (= `release_id`) | `988ed2a7c597631efc30662cfab1b16763d087434a64eb588985abed12d72f0e` | `5866c800b6dfff437b0ba2bf2ee8e655bd5d61262e335ea50bcc2625e53a285f` |

Schema sidecars: `schemas/reader.v1.schema.json.sha256` and `schemas/reader.v2.schema.json.sha256` carry the "after" digests above in `sha256sum` line format. Golden comparison report (`--compare-goldens`, external): SHA-256 `a79471f2acc5fb1f54aed1c284b5c35a7d8fcf036b6bb1c7334eab107fc78f6a`, eight cases `match`, `ok: true`.

## 5. Planning decisions applied (plan §14.2)

D-01 … D-18 applied as planned, with these observations: D-01/D-02 (second production blueprint at `/api`; governed 405s) verified on all three app factories by `tests/http/test_reader_post_v2.py::test_every_app_factory_mounts_the_production_reader_under_api`; D-03 strict `getlist` selection; D-04 bands read from the validated result rows; D-05 `prompt` refused by the v1 emitter; D-06/D-07 schemas as §§5.4–5.5 except the one message corrected by IF-01; D-08/D-09/D-13 goldens, writer and release-pack companions; D-10 test homes; D-11/D-12 A7 owner and frozen digest; D-14 F07 seam and generator; D-15 `built_at_utc` unchanged; D-16 registrations only; D-17 one PR, ordered commits; D-18 `test_cli_proof` untouched.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested (identity → outcome) |
| --- | --- | --- | --- |
| IF-01 | `schemas/reader.v2.schema.json` error branch: the `ERR_READER_INVALID_CHART` message is `invalid reader payload` (the token map's), not the plan §5.5 text `invalid Reader chart` | Plan §5.5 itself binds the messages to `ERROR_TOKEN_MAP` ("the messages are the token map's; a test pins each pair"); the listed text was a transcription defect. Canon (PF05 §5.2.3.1 error bytes) is unaffected | `tests/reader_v1/test_schema.py::test_v2_error_pairs_valid_and_bound_to_the_token_map` (12 params) → passed; the first run of the plan's text failed that pin |
| IF-02 | Convergence order: the A7 owner's write mode (plan §5.9 step 7) ran before the updater (step 5); steps 5–6 then ran as planned | `tools/evidence/update_evidence_index.py` validates the tracked catalog with the A7 validator (`_validate_epic038_pr02_semantics` → `validate_catalog`), whose new production-row rule refuses the pre-change catalog; the updater cannot run until the owner has written the row. Same owners, same outputs; order only | ledger entries [9]–[12] (updater/publish-family exit 1 with `production reader catalog invalid`), then [101]–[106] exit 0; second-run byte stability proven afterwards |
| IF-03 | `tests/config/test_production_admission.py::test_result_schema_references_must_resolve_without_constructing_a_result` mutates `$defs.success.properties.categories.items.$ref` | The F05 restructure (plan §5.4) moved the success properties under `$defs.success`; the test's `schema["properties"]` raised `KeyError`. Same subject and expected refusals (`UNRESOLVED_SCHEMA_REFERENCE`, `INVALID_SCHEMA_REFERENCE_TARGET`) | 3 params → passed (failed before the repair; passed at the base) |
| IF-04 | `tests/config/test_registry_catalog_contract.py::test_source_capture_detects_later_change_and_base_needs_no_mechanics_release` pins `1.2.0` | A pinned release identity outside the plan §8.8 inventory (27 tests, six files); the same rewrite class | → passed |
| IF-05 | `artifacts/core/*` (+ path proofs) regenerated by `tools/evidence/generate_engine_core_evidence.py`; Index/Mirror re-bound by the updater | The engine-core payloads bind the source SHA-256 of `engine/config/registry_loader.py`, which the roster edit changed; `tests/evidence/test_engine_core_evidence.py::test_current_proofs_bind_actual_sources_and_behavior` refused the stale digest. Plan §5.9: a changed evidence primary restarts at step 5 (done: updater, read-only checks, sanity canonical run and gate, all exit 0; sanity log unchanged) | `tests/evidence/test_engine_core_evidence.py` → passed (18 tests in the 90-test repair run); changed-test isolation 2697 passed |
| IF-06 | `tests/evidence/test_rails_ci_workflow_integration.py::test_http_reader_owner_guard_is_selected_without_fixed_lane_duplication` expected tuple gains `tests/http/test_reader_post_v2.py`; `tests/http/test_endpoint_catalog.py` compares the blueprint module as `create_app.__module__` | The pinned owner tuple is the registration's mirror (plan §6.2 anticipated it); the literal string `"adapter.http_reader"` in a test makes the ownership registry demand a literal-reference owner registration, which §5.11 does not include — comparing the attribute keeps the classifier tables exactly as planned | `tests/evidence/test_rails_ci_workflow_integration.py` 133 passed; `tests/evidence/test_http_reader_ci_ownership.py` passed |
| IF-07 | Work vehicle: `claude/admiring-tesla-h3awg8` restarted from `origin/main` and published with a lease-guarded push replacing `c4ddf4d…` (the plan commit, already merged by PR #507, tree-identical to `main`) | The harness rule for a designated branch whose PR was merged; one branch and one PR per plan cycle; nothing unmerged was discarded | `git merge-base --is-ancestor` no / tree equality yes recorded in the publication log; `git ls-remote` read-back `402db72…` |

Also corrected before commit (not a decision about scope): the new `tests/evidence/test_dev_conjunction_identity.py` first asserted a substring (`dev_identity`) that the new `no_dev_identity_stamp=true` log line legitimately contains; the assertion now checks the retired `writer_dev_identity=` / `reader_dev_identity=` lines.

## 7. Local validation (plan §10; every command with its exit status)

### 7.1 Checkpoint suites (plan §9)

- C1 (`tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/reader_v1/test_emitter.py tests/runtime/test_identity.py tests/runtime/test_emit_public_legacy_helper.py tests/cli/test_showcompat_parity_and_identity.py tests/cli/test_cli_canonical_bytes.py`): 133 passed / 3 skipped; the three real-admission cases failed by design until C5 (`MANIFEST_MEMBER_HASH_MISMATCH: adapter/http_reader.py`, PF10 §2.12 working). `python tools/cli/serializer_grep_guard.py --output <tmp>` exit 0 (`summary: PASS`); `python tools/cli/emitter_symbol_proof.py --output <tmp>` exit 0 (`summary:PASS`; CLI symbol set unchanged). Dev `GET /reader` bytes for the fixture pair equal the pre-change golden (`test_dev_get_bytes_for_the_fixture_pair_are_unchanged` passed).
- C2 (`tests/reader_v1`): 81 passed; `test_cli_proof` pre-existing; `test_release_pack` passed once the regenerated outputs were committed (its clean-status assertion); `g01`/`g06` byte-identical (`cmp`); no `_leader` name or byte remains under `goldens/`.
- C3 (`tests/http/test_endpoint_catalog.py tests/transport/test_a7_transport_proofs.py tests/http/test_dev_conjunction_http.py tests/evidence/test_dev_conjunction_identity.py`): 54 passed; the seven real-root/tracked-artifact cases failed by design until C5; the injected-release capture proved the seam, the control refusal and the admitted identity; `HdApiClient.from_env` patched to fail in every F07 test; the generator refuses open rails (`SystemExit`).
- C4 (`tests/evidence/test_rails_ci_workflow_integration.py tests/evidence/test_http_reader_ci_ownership.py`): 141 passed after IF-06 (only the not-yet-cut real-root case failing).
- C5 convergence ledger (exit codes, in order): cutter 0; `release_id_recompute.py --check-manifest-only` 0; cutter `--check` 0; admission `5866c800… 45` and `identity_meta()` equal; `--compare-goldens` 0; gate write 0 / `--check-only` 0; [IF-02] A7 write 0 / `--check` 0; updater 0 / `--check` 0; `--publish-family` 0 / updater `--check` 0; determinism write 0 / `--check` 0; open-rails ABBA (`SAFE_MODE=0 ALLOW_NETWORK=1`, vendor keys absent, fixture mode) 0, `FROZEN_OPEN_ABBA_SHA256` refreshed, `--check` 0; F07 write 0 / `--check` 0; updater 0 / `--check` 0; `orientation_demo.py --check` 0; `validate_evidence_paths.py` 0; `check_mirror_schema.sh` 0; `check_evidence_index_hash.sh` 0; `check_lf_endings.py` 0; `check_final_lf.sh` 0; sanity non-canonical `summary:PASS`; canonical run 0 (log byte-identical); `run_sanity_pipeline_gate.py` 0; updater `--check` 0; showcompat / CLI conformance / rails gate / env matrix `--check` 0; second run of gate, updater, publish-family, A7, determinism, ABBA, F07, updater, sanity, updater `--check`: all 0 and byte-stable (4,103 files compared under `artifacts`, `audit`, `catalog`, `docs/evidence` and the catalog paths); IF-05 restart: engine-core owner 0 (it runs the updater, `--check` and orientation itself), every read-only check 0, sanity canonical run 0 (log unchanged), gate 0, updater `--check` 0.

### 7.2 Classifier dry-run at the implementation head (plan §10.3)

`python ci/checks/classify_ci_changes.py --base 547dc5b1198811483bc5b93585731558cdc3dcba --head 402db7214ce79fea472f388c71f5e671a55b7cc8 --event-name pull_request --github-output … --changed-tests-output …` → exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=128;lanes=product,compat,db,rails,evidence,qa,release`; `product=compat=db=rails=evidence=qa=release=true`, `needs_python=true`, `changed_tests=true`; 94 changed-test targets; zero `CI_CHANGE_SURFACE_UNCLASSIFIED` / `CI_PRODUCT_OWNER_TEST_MISSING` / `CI_EVIDENCE_OWNER_TEST_MISSING`.

### 7.3 Changed-test isolation (plan §10.3, as `ci.yml` runs it)

Detached worktree at `402db72`, `PYTHONPATH=<worktree>`, `python -m pytest -q -p no:cacheprovider -- <94 targets>` → **2697 passed** (196.7 s); `git diff --exit-code` 0; no untracked files. (A first round at `a3336ad`, before IF-03/IF-04/IF-05, had 6 failures / 2691 passed; all six were classified against a baseline worktree at `547dc5b` — they passed there — and repaired, none by weakening.)

### 7.4 Lane-equivalent validation (plan §10.4; commands verbatim from `.github/workflows/ci.yml`)

| Lane | Commands and results (all exit 0) |
| --- | --- |
| product | `generate_ordering_artifacts.py --check`; pytest 20 passed |
| compat | `check_cli_help.sh`; serializer grep guard; emitter symbol proof; pytest 102 passed / 3 skipped / 2 xfailed |
| db | `check_direct_db_contract.py` (`DIRECT_DB_CONTRACT_OK`); pytest 249 passed |
| rails | `run_rails_job_definitions.py` on the three job files → `RAILS_JOB_DEFINITIONS_OK` (39 passed; exit 0, never 3); pytest 133 passed |
| evidence | updater `--check`, orientation `--check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`; pytest 111 passed (253.6 s) |
| qa | detached worktree; the seven qa test files → 488 passed; diff 0; no untracked |
| release | `git diff --exit-code` 0; `release_id_recompute.py --check-manifest-only` 0; detached worktree pytest (`test_identity`, `test_release_attestation`, `test_release_manifest_content_binding`, `test_sanity_pipeline`) 64 passed; diff 0; then §7.6 |

Tree clean (diff 0, no untracked) after every lane.

### 7.5 Candidate-wide roster (plan §10.5)

`_FULL_VALIDATION_SUPPLEMENTAL_TESTS` ran inside the 94 changed-test targets (§7.3). The §10.5 extras plus every §8 home in the main tree: **1168 passed, 3 skipped, 1 failed** — `tests/reader_v1/test_cli_proof.py::test_cli_stdout_lf_hash_and_admin_sidecar_invariance` (`scripts/hd_cli.py` exit status 2), reproduced on a detached worktree at the base `547dc5b`: pre-existing, plan D-18.

### 7.6 Attestation rehearsal at the implementation head (plan §10.6)

From the clean committed tree: `python tools/evidence/build_release_attestation.py --output <external empty dir> --require-clean` → exit 0 (75 s); `--verify <same dir> --require-clean` → exit 0; `attestation.json` SHA-256 `17cdd5bf802fe8800d61186ef26ee6401434a0bd791312f465466b48bb6e9d56`, `schema hde.release_attestation.v1`, `release_admission PR06R_B_FINAL_PASS`, `validation_result PASS`, `release_id 5866c800…`, 174 files bound, 14 `omitted_files`; `git diff --exit-code` 0 and no untracked file afterwards. The bundle is external and ephemeral (plan §10.6; not transferred).

### 7.7 Stale-binding sweep (beyond plan §10)

`git grep` for the six pre-change member digests and the old `release_id` across tracked files (excluding `docs/pfcanon`, `docs/ephemeral`, `_arch`, `notes`): none remain except the pre-change `presenter/reader_v1/emitter.py` digest inside frozen EPIC037 captures (`artifacts/vendor/hdapi_v2/hde_epic037_admin_public_boundary.json`, `…_v2_to_compat_pair_order.json`, `…_v2_to_compat_proof.json`, `…_v2_to_compat_two_run.json`) and an EPIC028 QA report — frozen families with nonclaims (plan §6.4; O-P06a-17).

## 8. Code review and security review self-check (plan §11)

- §11.1: version selection cannot be bypassed (`getlist` length and membership; dev GET `("1",)`); the production handler is reachable only under `/api` on every factory (§8.1 case 8); no ETag on POST; errors `no-store`; the v2 bands come from the validated result rows in registry order (no second calculator); the emitter refuses anything but the ordered ten; canonical serialization preserves array order; Reader v1 bytes pinned; the seam is dev-gated, absent by default, never read by the production Reader (`test_production_reader_never_consults_the_seam`), and a miss still refuses under closed rails; the generator refuses open rails and never constructs a vendor client even with credentials present (`test_check_mode_never_constructs_a_vendor_client_even_with_credentials`).
- §11.2: no new secret surface; no raw vendor payload persisted (the F07 rows are projected fixture charts); `DATABASE_URL` neutralized in both generator modes; `APP_ENV=prod` keeps the seam unreachable (403 before any lookup); the body-size bound of the production route unchanged; the `_READER_POST_KEYS` grammar unchanged.
- No Codex review has run yet: this candidate's code and security reviews are PR-35's to read and resolve.

## 9. Limitations

- Hosted CI on `402db72…` and on the records head is unobserved in PR-30; local lane equivalents are the evidence here. Local Python is 3.11.15; CI installs 3.12.
- No Codex code or security review exists yet (PR-35 entry actions).
- The instruction v1.0 is still carried by open PR #506 (its SHA-256 verified against that PR's head); it is a documentation record, not a code dependency.
- `docs/changes/GCFPE_PROMPT_PROVENANCE.md` remains absent; provenance persistence `PENDING / NON_GATING` (§13).
- The second-run stability comparison used `find … | xargs sha256sum`; nine historical QA file names containing spaces were split by `xargs` and reported "No such file" identically in both runs; they are outside this change and the comparison of the 4,103 hashed files is unaffected.

## 10. Observations (non-gating; carried for their owners; plan §13.2 holds O-P06a-01 … O-P06a-15)

| ID | Observation | Owner |
| --- | --- | --- |
| O-P06a-16 | `docs/ENDPOINTS_CATALOG.json` is a tracked symlink (mode `120000`) to `artifacts/audit/ENDPOINTS_CATALOG.json`; the A7 owner writes through it, so "docs catalog is source-of-truth; audit mirror" (`AGENTS.md`) names one file reached by two paths. Git shows only the target as modified | AGENTS.md / evidence owners |
| O-P06a-17 | Frozen EPIC037 captures and an EPIC028 report still bind the pre-change emitter digest (§7.7); nonclaim, not regenerated | frozen-family owners |
| O-P06a-18 | Plan §5.5 listed `invalid Reader chart` for `ERR_READER_INVALID_CHART`; the token map says `invalid reader payload` (IF-01) | plan author (record only) |
| O-P06a-19 | Plan §5.9 ordered the updater (step 5) before the A7 owner's write (step 7); the updater validates the tracked catalog with the A7 validator, so the owner must write first when the catalog changes (IF-02) | plan author / evidence owners |
| O-P06a-20 | Two pinned identities outside the plan's 27-test inventory (`test_registry_catalog_contract.py`, the `test_production_admission.py` schema-reference cases) and one evidence family binding a member digest (`artifacts/core/*`) were found by the changed-test isolation run, not by reading; a base-vs-head sweep before publication caught them (IF-03/04/05) | plan author (record only) |
| O-P06a-21 | `dev/reader_harness/app.py` mounts the dev blueprint at `/api`; its `POST /api/reader` now reaches the governed 405 stub (the harness stays untouched per plan §5.2 and already fails at `app.getattr`, PR04 O-17) | dev harness owner |

## 11. `CANON_CONFLICT_REGISTER`

Carried unchanged from plan §13.1 (no entry reopened, relabeled, omitted or newly decided); C040-08 remains a candidate (D-06). No PF-Canon file was edited.

## 12. Publication (PR-30 initial publication; one work vehicle)

- **Pre-push confirmation** (2026-09-26T05:14:00Z): branch `claude/admiring-tesla-h3awg8`, `HEAD 402db7214ce79fea472f388c71f5e671a55b7cc8` (tree `25c64aaa…`), `origin/main 547dc5b…` (merge-base equal), six outgoing commits (§4.1), working tree clean, one primary worktree (plus detached scratch worktrees under the session scratchpad); remote branch at `c4ddf4d643e908f24399fdaaaeff8c24480e3899`, not an ancestor of `HEAD`, tree equal to `origin/main`'s (the squash-merged plan commit).
- **Implementation push** (05:14:13Z): `git push --force-with-lease=refs/heads/claude/admiring-tesla-h3awg8:c4ddf4d643e908f24399fdaaaeff8c24480e3899 -u origin claude/admiring-tesla-h3awg8` → exit 0, `+ c4ddf4d...402db72 (forced update)`, upstream set. Read-back `git ls-remote origin refs/heads/claude/admiring-tesla-h3awg8` → `402db7214ce79fea472f388c71f5e671a55b7cc8` = local `HEAD`.
- **Pull request #508** created (GitHub API) from `claude/admiring-tesla-h3awg8` into `main`, not draft, with the template headings (Why / What changed / Checks run / Not in this PR / What merging does) and the plan §15 merge statement; read back after creation (recorded in the ledger L-11).
- **Records**: this record, `docs/ephemeral/HDE-EPIC040-PR06a-pr-remote-action-ledger-v1.0.md` and `docs/ephemeral/HDE-EPIC040-PR06a-pr30-checkpoint-v1.0.md` are committed as one records commit and pushed as the second and last PR-30 push; the records commit's SHA, the `git ls-remote` read-back and the PR #508 read-back after it are recorded in the PR #508 body (rewritten once after that push) and in the ledger's final row. A records-only push changes no CI-classified path, but `ci.yml` classifies the whole pull request against its base, so the run on the records head selects the same seven lanes and is the exact-head run PR-35 reads.
- **Not done, by rule**: no merge, auto-merge, scheduled merge or `[skip ci]`; no second PR or branch; no rebase of published history beyond the lease-guarded replacement of merged-only history (IF-07); no Notion write; no `docs/pfcanon/` write; no Claude Code Review installation or trigger (reviews come from Codex).

## 13. Prompt-use provenance

`GCFPE_PROMPT_USES`: `GCFPE-USE-HDE-EPIC040-PR-30-20260926-PR06a-01` (this PR-30 phase); carried: `GCFPE-USE-HDE-EPIC040-PR-20-20260926-PR06a-01` (plan v1.0), `GCFPE-USE-HDE-EPIC040-PR-10-20260926-PR06a-01` (instruction), `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06-01` (PR06 review).

- Prompt: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204` (Notion read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members.
- Change / unit: HDE-EPIC040 / HDE-EPIC040-PR06a; Specification v1.1; instruction v1.0; plan v1.0.
- Role / stage: dedicated PR06a PR-development session / PR-30.
- Captured: 2026-09-26T05:14:13Z (implementation push).
- Execution identity: harness session `https://claude.ai/code/session_01EBvvgYQTXQqvSpd2eHtK8V`.
- Repository persistence: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; `PENDING / NON_GATING`; owner: the authorized repository writer once a procedure is installed.

## 14. Continuation

- PR-30 ends here with `PR_CANDIDATE_PUBLISHED`. PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1 (`https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`) runs in its own dedicated session, entered from the handoff this session returns, continuing pull request #508 on branch `claude/admiring-tesla-h3awg8` under the original Proceed (no second Proceed, workspace, branch, PR, instruction or plan).
- PR-35 obligations carried: subscribe to PR #508 activity; read the Codex code and security reviews and inline threads; read the exact-head CI run (all seven lanes are selected — the candidate changes `ci/checks/classify_ci_changes.py` — and `RAILS_LANE` / `RELEASE_LANE` must end green, never `RELEASE_NOT_ADMITTED`; a built and verified attestation in the release lane); resolve findings locally and push one coherent corrective revision if needed (any change to a roster member re-cuts the manifest through the cutter and restarts plan §5.9 at step 2; any evidence primary at step 5); verify the current head; `MERGE_PENDING`. Nathan merges manually; PR-40 follows `MERGE_OBSERVED`.
- Merging PR06a makes Reader v2, the production Reader at `/api/reader`, the corrected Reader v1 schema and goldens, the restored dev conjunction capture and the 45-member `1.2.0` release with its converged evidence current on `main`; it establishes none of QA verdict, acceptance, PF09 movement, OPS01's final external attestation, C040-07 drainage, deployment, activation or Epic closure (plan §15). PR07 must follow PR06a; OPS01 verifies the 45-member release.
