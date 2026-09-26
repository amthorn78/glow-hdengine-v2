# HDE-EPIC040-PR06a — PR Implementation Result v1.1 (PR-35)

| Field | Value |
| --- | --- |
| Artifact | `PR_IMPLEMENTATION_RESULT` — `HDE-EPIC040-PR06a-PR-IMPLEMENTATION-RESULT` v1.1, the PR-35 phase record. It continues v1.0 (PR-30, `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.0.md`), which is unchanged as issued and remains the implementation record (scope, planning decisions, in-flight decisions IF-01 to IF-07, PR-30 local validation) |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06a — Reader v2 full Magic-10 and deferred Reader work (overlay PF10 §2.23, C040-07) |
| Change | `EPIC / HDE-EPIC040`; `HDE-EPIC040-SPECIFICATION` v1.1 (`SPECIFICATION_APPROVED`); PR06a rescope decision v1.0 |
| Producer | the dedicated PR-35 session for HDE-EPIC040-PR06a (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; runtime `https://claude.ai/code/session_01QAme7bG6ZDJ5AEsYfRbLr9`); `EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION` |
| Result | `MERGE_PENDING` — Ready to merge, on the condition under *Final head* (§1) |
| Prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1 (`https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`); page read as of `2026-09-24T15:48:24.405Z` (Notion read only) |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/admiring-tesla-h3awg8` |
| Pull request | [#508](https://github.com/amthorn78/glow-hdengine-v2/pull/508), the one work vehicle, reused |
| Base | merge-base `547dc5b1198811483bc5b93585731558cdc3dcba`, unchanged. `main` advanced once during PR-35, to `cf9198dfad4710e85c3a8cd0a4739708e27e88c0` (PR #506, the instruction record: one file under `docs/ephemeral/`); no overlap with this PR |
| Commits | PR-30: `894bb6f6…` … `402db7214ce79fea472f388c71f5e671a55b7cc8` (implementation, tree `25c64aaa1a056a5602f0e889cc4c89c6747ce9eb`) and `b23c06f891a80ad0b02d98218189adcd9b30ceec` (records, tree `280194e0b34a88505db90eb31877d171379329da`). PR-35: `dc958ec568e55984d2c4a242cd4ff51726a132fb` (corrective, tree `0f29d0905e37036823877ec957d0ca3014131ab9`). Records: the commit adding this file, ledger v1.1, the PR-35 checkpoint v1.0 and the conditional PR-40 handoff v1.0; a commit cannot embed its own SHA, so its SHA and the remote head after its push are recorded in the PR #508 body and the PR-35 return |
| Recorded by | the dedicated PR-35 session, 2026-09-26 (UTC) |

## 1. Outcome

**`MERGE_PENDING` — Ready to merge,** on the condition under *Final head*. This record is historical pre-merge evidence. It does not claim the PR is merged, and it is not a QA verdict, acceptance, release activation, PF09 movement, OPS01 attestation, C040-07 drainage, deployment or closure. Nathan / Product Owner merges manually as a separate action; nothing here enables, schedules or requests a merge.

- **Reviews.** Codex raised three findings (§4). **CR-01** (P2, TRACE/CONNECT/extension methods on `/api/reader` answered by each factory's own 405) is a real gap against plan CC-3 and §11.2: fixed in `dc958ec`. **CR-02** (P1, the Reader v1 schema rejects the route's real four-key error bytes) is canon-conflict candidate C040-08, which the approved plan carries rather than decides (§5.4, D-06, R-02, §13.1): not changed. **CR-03** (P2, HTML 404 for unknown `/api/reader/*` subpaths on two factories) is pre-existing and outside the approved route contract: not changed, carried as O-P06a-22. Each thread is answered and resolved after the push, so the replies can name the pushed commit; resolving CR-02 and CR-03 means dispositioned for this PR, not fixed. Codex's Security Review of the implementation head `402db72` completed with no finding.
- **Correction.** `adapter/http_reader.py` is a release member, so the manifest was re-cut (`1.2.0`, 45 members, `release_id 9f962ce338c448c7a2312f05695d5fdab12b01fbc1a67d490465d9fc87edab3f`) and plan §5.9 restarted at step 2; every governed family converged through its owner, and a second run of every producer was byte-stable (§6).
- **Local.** Every `.github/workflows/ci.yml` step, replayed verbatim at `dc958ec` on Python 3.12.3, exited 0, including the strict attestation build and verify (§7).
- **Final head.** This record's commit adds only `docs/ephemeral/` records above `dc958ec`. The pushed head's exact-head CI and Codex review are read after the push and recorded in the PR #508 body and the PR-35 return. The return states `MERGE_PENDING` only if both are clean; otherwise this result no longer stands and a later version replaces it.
- **Correction to the PR-30 record.** Result v1.0 IF-05 and the PR-30 checkpoint say the engine-core owner runs "when `engine/config/registry_loader.py` changes". Measured here: the engine-core payloads also carry the admitted `release_id` (their synthetic root is built from the real roster), so every re-cut needs that owner. PR-35 ran it (IF-09; O-P06a-23).

## 2. Authority, identity and controlling sources

| Source | Exact identity | Repository path |
| --- | --- | --- |
| Product Owner Proceed | The original PR-30 Proceed for exactly `HDE-EPIC040-PR06a-PR-IMPLEMENTATION-PLAN` v1.0 and `HDE-EPIC040-PR06a-PR-INSTRUCTION` v1.0 (result v1.0 §2); it covers PR-30 and PR-35 of this one work unit. No second Proceed exists, was requested or was needed | result v1.0 §2 |
| PR-35 invocation | Nathan's pasted PR-30 handoff naming this prompt, PR #508 and the input artifacts; `session_disposition: NEW_DEDICATED`, `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06a / PR-35`, `context_conflict: NONE` | this session |
| Detailed PR plan | v1.0, SHA-256 `48cf4120e4613b4fde38ebe26c99186ead627808593540155eb79e576aaa9d68` (124,954 bytes), read completely | `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-plan-v1.0.md` |
| PR instruction | v1.0, SHA-256 `b6e1c663fe19a073e519ef57455701d1b437c0fb9c12d284b4b0d6fb83220fcb` (12,599 bytes); on `main` since PR #506 merged (`cf9198d`) | `docs/ephemeral/HDE-EPIC040-PR06a-pr-instruction-v1.0.md` |
| Overlay and decision | addendum v1.0 `a69e2205de410bf6332bb558f3ee0110e3524b7143a84591bbed18ff476528e9` (drained as PF10 §2.23); rescope decision v1.0 `0c3d4ad718cbed410f1d248fcea5f1772b140bd06bc2866bc0ecc4257a7e8a55` | `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md`, `docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md` |
| PR-30 result, ledger, checkpoint | result v1.0 `b3cbc9ce9842241b49b5adce31ae95e909e658cdcb0fe3cc8badaa78cd5b9f80`; ledger v1.0 `0982b9b9be12f9d36db06c6d3c4be54378a62fed30e9070348e069c7e7ae373c`; checkpoint v1.0 `c53b1963c83da89bb1b45a92bbab32222ff1310d40357fa1a25503438a9da98c`. Read completely; digests equal the handoff's; none edited | `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.0.md`, `…-pr-remote-action-ledger-v1.0.md`, `…-pr30-checkpoint-v1.0.md` |
| Immutable approved base | as plan v1.0 §2.1 (Specification v1.1, Implementation Audit v2.0, Implementation Plan v2.1, Plan Review v2.1, accepted PR01–PR06) | plan §2.1 paths |
| Current PF10 read | PF10 — HDE Build Notes v13.3.4, 270,087 bytes / 2,485 lines, SHA-256 `0029e2827904f6b798f6367f54a8d134bb55d170a412cc544b1555594c4e4f29`, the latest base version beside v13.3–v13.3.3 (not read); §§2.12, 2.16–2.18, 2.23 and the precedence front matter read (provenance, not a gate) | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md` |
| Other canon read | PF05 v2.5.2 (`a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e`) §§5.1–5.6, for CR-01 to CR-03 | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md` |

No Google Doc, DOC, DOCX or Drive copy was opened. Notion was read only (the PR-35 and PR-40 prompt pages); no Notion page was written. `docs/pfcanon/` was read only.

## 3. Recovery at PR-35 entry

- **Checkout.** Fresh container clone on the harness branch `claude/youthful-faraday-o3tsf8` at `547dc5b` (= the base; absent on `origin` by `git ls-remote`; never committed to or pushed). The handoff binds PR-35 to PR #508 on `claude/admiring-tesla-h3awg8`, the work unit's one work vehicle, so all PR-35 work is on that branch, created locally from `origin/claude/admiring-tesla-h3awg8`. PR-30's container is not reachable; the repository, branch, pull request and records establish continuity, and nothing was reconstructed.
- **Remote state.** `refs/heads/claude/admiring-tesla-h3awg8` = `refs/pull/508/head` = `b23c06f891a80ad0b02d98218189adcd9b30ceec` (`git ls-remote`), the head the PR-30 records publish. PR #508: open, not draft, not merged, 7 commits, 131 files (+2,178/−465), `mergeable_state: unstable` (CI then running on `b23c06f`).
- **Subscription.** The PR #508 activity subscription is active for this session (tool result confirmed).
- **Inputs.** Every input artifact read completely; SHA-256 values equal the handoff's (§2).

## 4. Review findings and dispositions

Reviews read: Codex Code Review `5324720466` (`COMMENTED`, 05:18:28Z, commit `402db72`, one thread) and `5324740370` (`COMMENTED`, 05:25:36Z, commit `b23c06f`, two threads); the Codex summary comment `5843452513` (Code Review completed 05:25:39Z on `b23c06f`, trigger "New commits"; Security Review completed 05:20:13Z on `402db72`, trigger "PR opened"; `mergeGateEnabled: false`; `blockingSeverityThreshold: P0`). The Security Review posted no review, thread or comment. No other reviewer.

| ID | Source and location | Finding | Reproduction | Disposition |
| --- | --- | --- | --- | --- |
| CR-01 | Codex P2, thread `PRRT_kwDOP103ks6mN-mX` (comment `4110293882`), `adapter/http_reader.py:559–560`, review of `402db72` | A method outside the method-catch rule's finite list (TRACE, CONNECT) on `/api/reader` falls to Flask's HTML 405 on `adapter.factory` and `adapter.http_reader` (no governed body, no `no-store`, no `Allow: POST`) | Reproduced at `b23c06f` for TRACE, CONNECT, PROPFIND and BREW: HTML 405 with the framework's `Allow` list on both factories; `adapter.wsgi` returns JSON without `Allow`. At base `547dc5b` the path did not exist (404) | **Fixed in `dc958ec`** (IF-08). Plan CC-3 and §11.2 require every non-POST method on `/api/reader` to be the governed 405 and "never framework HTML"; plan O-P06a-06 records it as "fixed here". Answered and resolved after the push |
| CR-02 | Codex P1, thread `PRRT_kwDOP103ks6mOBEL` (comment `4110310244`), `schemas/reader.v1.schema.json:1`, review of `b23c06f` | Every real Reader v1 error envelope (`{"schema":"v1","ok":false,"code","error"}`) fails the published v1 schema, whose `$defs.error` omits `schema` under `additionalProperties: false` | Reproduced: `error_envelope("ERR_READER_INVALID_VERSION")` bytes fail the v1 schema at `b23c06f` and at base `547dc5b` (pre-existing; plan F-05) | **Out of scope; not changed; carried as C040-08.** Plan v1.0 §5.4 keeps the v1 error branch semantically unchanged and names this exact conflict: PF05 §5.2 (the four-key envelope, which the v1 schema's error branch "MUST enforce") against PF01 §2.3 and PF04 §8.1.2 (no `schema` in the Reader v1 error contract). D-06 classifies it "in scope by omission"; R-02 accepts the risk; §13.1 records candidate C040-08 (`PROPOSED`, recommended alternative A, which is what this finding asks for); the overlay excludes any Reader v1 contract change beyond the three F05 items. Deciding it in the PR would settle a canon conflict outside this work unit's authority. Not material to PR06a delivery, so no rescope. Owner: the register owner (the whole-change IA; Isis disposition), then the PF01/PF04 maintainers. Answered and resolved as dispositioned for this PR, after the push |
| CR-03 | Codex P2, thread `PRRT_kwDOP103ks6mOBEM` (comment `4110310245`), `adapter/factory.py:12`, review of `b23c06f` | Unknown descendants such as `/api/reader/missing` get Flask's HTML 404 (no `no-store`) from `adapter.factory` and `adapter.http_reader`; only `adapter.wsgi` returns `ERR_NOT_FOUND` JSON | Reproduced for `/api/reader/missing` and `/api/reader/`. Identical at base `547dc5b`, and identical for every unknown path in those two factories (`/api/aux/narrative/x`, `/api/anything`, `/reader/x`) | **Out of scope; not changed; O-P06a-22.** Pre-existing and not introduced by this PR. The approved route contract (CC-3, §11.2) is `POST /api/reader` plus the governed 405 on that path, which `dc958ec` makes identical on all three factories. Governed 404s for unknown paths are a factory-wide error-surface decision (PF05 §5.2); a Reader-only conversion would open a new inconsistency inside `/api`. Neither obvious nor necessary to deliver the approved scope, so not done (skill rule 3) and carried for its owner. Answered and resolved as dispositioned for this PR, after the push |

## 5. In-flight decisions

PR-35 took two decisions without a rescope. Neither is material: no outcome, acceptance criterion, protected boundary, other work unit or dependency changes.

| ID | What changed | Why it was necessary to deliver the approved scope | Tested (identity → outcome) |
| --- | --- | --- | --- |
| IF-08 | `adapter/http_reader.py::get_reader_api_bp` records, on every app the blueprint is registered on, a `before_request` guard that answers a routing `MethodNotAllowed` for exactly the blueprint's mounted route (`<url_prefix>/reader`) with the existing `_reader_method_not_allowed("POST")`. The six-method rule of plan §5.2 is kept; the three factories and their handlers are unchanged | CC-3 and §11.2 require every non-POST method on `/api/reader` to be the governed 405. A method no rule names fails routing before any view or blueprint error handler is chosen, so the plan's finite method list cannot cover TRACE, CONNECT or extension methods, and an app-level 405 handler would collide with each factory's own. The guard is the route owner's, is bound to its mounted path, and leaves every other route's 405 untouched | `tests/http/test_reader_post_v2.py::test_every_non_post_method_is_the_same_governed_405_on_every_app_factory` (10 methods × `factory`, `http_reader`, `wsgi` = 30 cases) and `::test_the_unrouted_method_refusal_is_bound_to_the_mounted_route` → 31 passed at `dc958ec`; the same 31 cases on `b23c06f` code: 13 failed (TRACE, CONNECT, PROPFIND and QUERY on each factory, and the binding test), 18 passed. Whole file: 66 passed after the re-cut |
| IF-09 | `artifacts/core/two_run/identity.json`, `artifacts/core/abba/ab_ba_parity.json`, `artifacts/core/json_compare/core_result_json_compare.json` (+ path proofs) regenerated by `tools/evidence/generate_engine_core_evidence.py` after the re-cut; `artifacts/core/purity/purity_report.json` kept its bytes and capture time | The engine-core payloads carry the admitted `release_id`: the owner's synthetic root is built from the real roster, so its release equals the real one. After the re-cut the tracked payloads still named the superseded `5866c800…`, and no gate would have caught it: the owner's currency test checks source digests and behaviour, not that field. Plan CC-6 requires evidence to converge through its owners. Regenerating with the owner then restarting at plan §5.9 step 5 is the recorded procedure | Fresh-versus-tracked comparison before regeneration: differences only in release-bound fields (`inputs.release_id`, the run payloads). After the owner: `tests/evidence/test_engine_core_evidence.py` 10 passed; `git grep` for `5866c800…` outside `docs/` finds nothing; steps 5–10 all exit 0; second run byte-stable (§6) |

The work unit's earlier in-flight decisions are PR-30's, recorded in full in result v1.0 §6 and unchanged: IF-01 (v2 schema message bound to the token map), IF-02 (A7 owner before the updater), IF-03 and IF-04 (tests outside the plan inventory), IF-05 (engine-core owner after the roster edit), IF-06 (classifier-pinned test expectations), IF-07 (the work vehicle).

## 6. Corrective change and convergence (`dc958ec`)

### 6.1 Files

| Path | Change | Owner / basis |
| --- | --- | --- |
| `adapter/http_reader.py` | IF-08 guard (+19 lines; one `werkzeug.exceptions.MethodNotAllowed` import) | release member; owned locus |
| `tests/http/test_reader_post_v2.py` | the two IF-08 tests (+33 lines; `flask.Flask` import) | owned test home, already registered in the classifier |
| `catalog/manifest.json` | re-cut; only the `adapter/http_reader.py` row changed; 45 members, `1.2.0`, `2026-08-24T18:04:49Z` unchanged | the cutter |
| `tools/evidence/generate_open_rails_abba_proof.py` | `FROZEN_OPEN_ABBA_SHA256` → `29223e6f8a30ed80f857a5ded666e13eab8b54440c14d068ac8c40330a1fdbda` (the regenerated primary) | plan §5.9 step 7, D-12 |
| Governed evidence | canonical JSON gate outputs (4 files), catalog logs (2), A7 success proofs (5), determinism family (5), open-rails fixture proof (1), F07 writer artifacts (2), engine-core payloads (3), Machine Mirror and its `.sha256` (2), and 24 path proofs | their owners only (§6.3) |

52 files, +151/−99. Unchanged, by measurement: the endpoint catalog (`artifacts/audit/ENDPOINTS_CATALOG.json`, reached also through the `docs/ENDPOINTS_CATALOG.json` symlink, `acb7830656c4aa61451130154110fc30353173a662e11bf74add17c289382b02`), `artifacts/reader/endpoints_snapshot.json`, `artifacts/proofs/success_writers_errors.txt`, the Human Index `docs/evidence/INDEX.json` (`163fbc218ebb9c09621bac0a23ac52a5d8363618c0a56f5035efdc5f2687bdbc`), the sanity log (`88d787c11d58e3bd56e1d57008ef4cc2241510f9449c2fc9ce6eb1131ad3cdd7`), the release-pack outputs, every golden and schema, and `engine/config/registry_loader.py`.

### 6.2 Digests (before `402db72` → after `dc958ec`)

| Path | Before | After |
| --- | --- | --- |
| `adapter/http_reader.py` | `351a0611c36cd645b77d1587c06ef8fbd29f7d7387dad92d54f06b58d61ed258` | `85ced552678dc5a9080330f9082d0e1cb34130abb8979d4c1a271005e6ec0b9a` |
| `catalog/manifest.json` (= `release_id`) | `5866c800b6dfff437b0ba2bf2ee8e655bd5d61262e335ea50bcc2625e53a285f` | `9f962ce338c448c7a2312f05695d5fdab12b01fbc1a67d490465d9fc87edab3f` |
| `audit/gates/determinism/open_rails_abba.json` | `0e8f8f1aa09cf49596550cbb61fcd8a919715f869a65bfd788c1f1b56d2852e6` | `29223e6f8a30ed80f857a5ded666e13eab8b54440c14d068ac8c40330a1fdbda` |
| `artifacts/writer/conjunction_write_readback.log` | `d467f82af98f9700487d49cec6af8f06649fdb5ec89e7b47060edb3c465c5e9b` | `9ee92ef7ce2c8379d2c5aece2d7b89ce7f07085923d9bca7fca9a5044c72397d` |
| `artifacts/writer/conjunction_writer_summary.json` | `fa8cad2d05336065ce3353b4416d4e33d0b3464c6e572c4db46fe01abd04caaa` | `7873d888497292eec980324ee7e67ef5b08604225452a91f24d8ec41f7788d5e` |
| `artifacts/evidence_index.jsonl` | `8e0abd5fd16f46e554fafcf9c467caa9f36211f6d5dc9b2845a39080e2d74d42` | `6bd7cbc95124177c1868bd4d2de877c3fa510a93b0b19c5a4d88fe581cfde966` |
| `artifacts/core/two_run/identity.json` | `e1cfea2243123d0ec914e1c6de96b77bb7a8f5595777251f8c5643a26848cbd2` | `fe0d4d2b6d7554e8eeaaa059c39916ecc116edb044ed2b9b9868354f7737bfdf` |
| `artifacts/core/abba/ab_ba_parity.json` | `ed73685d481f57a294f756e6955169bbcd5eeae6cc19f5093be1ca9ce686b1f8` | `0d9dcdd4a2744348cf9506a89461052759fe67c6bd835dbd9fd176d3665777a1` |
| `artifacts/core/json_compare/core_result_json_compare.json` | `3c3ba1450dc779ccafe9964694ef18a8c38c4e73cecb39d1ca3cd9b747a6d132` | `a29d26d5db4302aad4c12bee78f02c6b5faba40be9421cbd356711169c5d1694` |

### 6.3 Convergence log (plan §5.9 from step 2; closed rails unless stated; exit codes as returned)

| Step | Commands → exit |
| --- | --- |
| 2 Cut | `scripts/cut_release_manifest.py --version 1.2.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` 0; `scripts/release_id_recompute.py --check-manifest-only` 0; cutter `--check` 0 |
| 3 Admission, goldens | `load_active_mechanics_bundle()` → `9f962ce3…`, 45 identities, `identity_meta()["release_id"]` equal; `tools/config/generate_config_artifacts.py --compare-goldens . --report <scratch>` 0: eight cases `match`, `ok: true`, report SHA-256 `466aa4e0b62508c40ec52c7d4f8a0c0dfe760887c040de967fb30f0080851339` |
| 4 Gate | `run_canonical_json_gate.py --check-only` 1 before the write (manifest target changed); write 0; `--check-only` 0 |
| A7 before the updater (IF-02) | `generate_a7_transport_proofs.py --check` 1 (`DRIFT` on the five success proofs, which carry `release_id`); `HDE_WRITE_A7_PROOFS=1` write 0; `--check` 0 |
| 5 Updater | write 0; `--check` 0 |
| 6 Config family | `--publish-family` 0 (the two catalog logs); updater `--check` 0 |
| 7 Live producers | determinism `--check` 1 (`DRIFT`), write 0, `--check` 0; open-rails fixture proof with `SAFE_MODE=0 ALLOW_NETWORK=1` and the vendor and DB keys absent: write 0, `FROZEN_OPEN_ABBA_SHA256` refreshed, `--check` 0; F07 generator `--check` 1 (`DRIFT`), write 0, `--check` 0 |
| IF-09 | `generate_engine_core_evidence.py` 0 (runs the updater, its `--check` and `orientation_demo.py --check` itself) |
| 5–8 restart | updater 0 / `--check` 0; `--publish-family` 0 / updater `--check` 0; A7, determinism, open-rails and F07 `--check` 0 each; updater 0 / `--check` 0; `orientation_demo.py --check` 0; `validate_evidence_paths.py` 0; `check_mirror_schema.sh` 0; `check_evidence_index_hash.sh` 0; `check_lf_endings.py` 0; `check_final_lf.sh` 0 |
| 9 Sanity | non-canonical run to a scratch log 0, `summary:PASS`, `first_failed_stage:NONE`; canonical run 0, log byte-identical to the tracked PASS model; `run_sanity_pipeline_gate.py` 0; updater `--check` 0 |
| 10 Frozen families | showcompat, CLI conformance, rails gate (`RAILS_GATE_EVIDENCE_OK`) and env matrix `--check` 0 each |
| Second run | cutter `--check`, gate, updater, `--publish-family`, A7, determinism, open-rails, F07 and engine-core writers, updater, canonical sanity, gate wrapper, updater `--check`: all 0; the digest of the complete working-tree diff was `d81f6c0f2e409d05cc87923cbcf675ee6a3c677c7b1eeded18c2e091fa257fe4` before and after; no untracked file |
| Stale-binding sweep | `git grep` outside `docs/pfcanon` and `docs/ephemeral` for the superseded `release_id` `5866c800…`, the superseded `adapter/http_reader.py` digest `351a0611…` and the superseded open-rails digest `0e8f8f1a…`: none remain |

## 7. Local validation at `dc958ec`

Environment: Python 3.12.3 venv with CI's install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`: setuptools 84.0.0, pytest 8.4.2, Flask 2.3.3, Werkzeug 3.1.8, jsonschema 4.23.0), the editable install resolving `engine` from this checkout; `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL` and `GH_TOKEN` removed from the process environment (the container carries values for several of them). No vendor call and no database connection occurred.

### 7.1 Focused suites (plan §10.2 plus `tests/evidence/test_engine_core_evidence.py`)

Working tree after convergence, before the commit: 1173 passed, 3 skipped in 104.08s, exit 0.

### 7.2 Every `ci.yml` step, replayed at `dc958ec`

The repository checkout at the committed head `dc958ec568e55984d2c4a242cd4ff51726a132fb` (clean tree), with the venv above. Each `run:` block of `.github/workflows/ci.yml` was copied verbatim into a local runner script for the `pull_request` event (`BASE_SHA` = the merge-base `547dc5b`, `RUNNER_TEMP` a fresh scratch directory), and every applicable step ran in CI order with its own exit status recorded, 05:46:15Z–05:57:56Z.

| Step | Exit | Outcome |
| --- | --- | --- |
| Classify (`--base 547dc5b --head dc958ec --event-name pull_request`) | 0 | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=131;lanes=product,compat,db,rails,evidence,qa,release`; `needs_python=true`, `changed_tests=true`; 94 changed-test targets (as at `402db72`) |
| Pytest readiness | 0 | `pytest 8.4.2` |
| Environment pins (`ci/checks/check_env_pins.sh`) | 0 | `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC` |
| Changed-test isolation (detached worktree, then `git diff --exit-code` and the clean-status assertion) | 0 | 2728 passed in 190.62s (PR-30: 2697; the difference is the 31 IF-08 cases) |
| Product lane | 0 | ordering `--check` 0; 20 passed |
| Compat lane | 0 | CLI help 0; serializer grep guard `summary: PASS` (scope `adapter/http_reader.py`, `engine/cli`); emitter symbol proof `summary:PASS`; 102 passed, 3 skipped, 2 xfailed (the pre-existing closed-rails skips and xfail markers) |
| DB lane | 0 | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| Rails lane | 0 | runner exit 0: `rails_closed_refusal` 4 passed; `rails_open_conformance` 113 passed and `--check-current` → `{"path": "audit/gates/determinism/open_rails_abba.json", "result": "pass", "status": "OK", "top_level_pass": true}`; `logs_keys_only_redaction` `RAILS_GATE_EVIDENCE_OK`, 39 passed; `RAILS_JOB_DEFINITIONS_OK`; workflow integration 133 passed. `RELEASE_NOT_ADMITTED` appears nowhere in the log |
| Evidence lane | 0 | updater, orientation, step-log, index-hash, path, mirror-schema and final-LF checks 0 each; 111 passed in 350.46s |
| QA lane (detached worktree, clean-tree assertions) | 0 | 488 passed |
| Release lane | 0 | `git diff --exit-code` 0; manifest-only check 0; regression suites 64 passed (detached worktree, clean); `build_release_attestation.py --output` then `--verify`, each printing only the bundle path; `RELEASE_NOT_ADMITTED` appears nowhere in the log. Bundle `attestation.json` 28,163 bytes, SHA-256 `2d336ad722b2d894f3e7761376c965ac7b6709480b585a3557c27381360b98fb`: `schema: hde.release_attestation.v1`, `source_commit dc958ec568e55984d2c4a242cd4ff51726a132fb`, `source_commit_exact: true`, `source_tree_sha256 09bbab78661c95c793c756112a280e59596eda80978ec4d20b54672fcdf8fadf`, `release_id` = `manifest_sha256` = `9f962ce338c448c7a2312f05695d5fdab12b01fbc1a67d490465d9fc87edab3f`, `validation_result: PASS`, `release_admission: PR06R_B_FINAL_PASS`, `pipeline_stop: null`, closed `rails` with `PIP_NO_INDEX=1`, 174 files bound, 14 `omitted_files` (the pre-existing secret-safety omissions), five `nonclaims`. The bundle stayed in the scratchpad |
| Final tree (`git diff --check`, `git diff --exit-code`, empty `git status --short --untracked-files=all`) | 0 | clean; no worktree left behind |

Every step exited 0. No test was skipped, deselected or marked by PR-35. `tests/http/test_reader_post_v2.py` alone: 66 passed.

### 7.3 Records head

The records commit adds exactly four files above `dc958ec` (`git diff --name-only`), all under `docs/ephemeral/`, a documentation prefix that selects no lane and no owner test (`_DOCUMENTATION_PREFIXES` in `ci/checks/classify_ci_changes.py`). On the committed records head, in the repository checkout with the same venv, before the push:

| Check | Exit | Outcome |
| --- | --- | --- |
| `python ci/checks/classify_ci_changes.py --base 547dc5b --head <records head> --event-name pull_request` | 0 | `paths=135` (131 + these four), all seven lanes, `reason=selected_lanes`; the 94 changed-test targets are byte-identical to `dc958ec`'s |
| `tools/evidence/update_evidence_index.py --check`; `orientation_demo.py --check`; `refresh_step_logs_manifest.py --check`; `ci/checks/check_evidence_index_hash.sh`; `validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_final_lf.sh`; `tools/evidence/check_lf_endings.py` | 0 each | converged; the four records end in exactly one LF |
| `python scripts/release_id_recompute.py --check-manifest-only` | 0 | OK |
| `git show --check` on the records commit | 0 | no whitespace error |
| `git diff --exit-code`; empty `git status --short --untracked-files=all` | 0 | clean |

## 8. Hosted CI observed

| Run | Head | Outcome |
| --- | --- | --- |
| `36220256198` (#3634) | `402db72` | `cancelled` by the workflow's pull-request-only cancellation when `b23c06f` was pushed |
| `36220539219` (#3635), job `108344875020` | `b23c06f` (PR-30 records head) | `success`, every job step `success`, 2026-09-26T05:21:30Z–05:37:14Z. Superseded as a gate once CR-01 required a corrective revision; its result is diagnostic evidence that the PR-30 candidate was green on hosted Python 3.12 |
| records head | this record's commit | read after the push (§1, *Final head*) |

No CI run was cancelled or retriggered by PR-35. No CI waiver was requested, granted or used. No `[skip ci]`.

## 9. Merge-readiness predicates (PR-35 prompt)

| Predicate | Evidence | State at this record |
| --- | --- | --- |
| Every applicable current-head review read; every required substantive finding resolved or lawfully waived | §4: CR-01 fixed; CR-02 and CR-03 dispositioned out of scope to their owners; Security Review on `402db72` without a finding | Holds through `b23c06f`; the records head's automatic review is read after the push |
| No required review thread unresolved | All three threads answered and resolved after the push (the reply ids go in the PR #508 body) | After the push |
| Required current-head CI passes | §7.2 locally; the records head's hosted run | After the push |
| Local required tests pass for the current head | §7 | Holds |
| Remote head equals the verified candidate | `git ls-remote` after the push (PR body, PR-35 return) | After the push |
| PR open and mergeable, no blocking conflict | At entry: open; `main` gained one `docs/ephemeral/` file that this PR does not touch | Re-read after the push |
| Ledger and final checkpoint complete, saved, read back, linked | `docs/ephemeral/HDE-EPIC040-PR06a-pr-remote-action-ledger-v1.1.md`, `docs/ephemeral/HDE-EPIC040-PR06a-pr35-checkpoint-v1.0.md` | Holds |

## 10. Limitations

- **Pre-existing, carried, unfixed:** CR-02 / C040-08 (a client validating Reader v1 errors against the published v1 schema rejects real errors) and CR-03 / O-P06a-22 (framework HTML 404 for unknown paths on two factories). Both predate PR06a and are outside its authority.
- The Security Review ran on `402db72`. Whether one covers the corrective delta (IF-08) depends on Codex answering the `@codex security review` request on the records head; its outcome is recorded in the PR #508 body and the PR-35 return.
- `tests/reader_v1/test_cli_proof.py` still fails at the base and here (plan D-18; O-P06a-03); it is in no lane or roster.
- Local runs describe this container (Python 3.12.3); hosted CI remains the record.
- Result v1.0 §9 limitations stand unchanged.
- Not executed: bare `pytest tests` (plan §10.5); any live vendor or database action; any open-rails run other than the fixture-mode ABBA proof the plan prescribes.

## 11. Observations (non-gating; carried for their owners)

- Plan v1.0 §13.2 O-P06a-01 to O-P06a-18 and result v1.0 §10 O-P06a-16 to O-P06a-21 are carried unchanged. Result v1.0 §10 reuses the numbers O-P06a-16 to O-P06a-18, which plan §13.2 already assigns to other observations; both sets stand as issued, identified by their record. New numbers here start after both.
- **O-P06a-22** (CR-03). `adapter.factory` and `adapter.http_reader` answer every unknown path with Flask's HTML 404 (no `no-store`); only `adapter.wsgi` has global governed 404/405 handlers. Whether PF05 §5.2's governed error surfaces include unknown paths under `/api` is a factory-wide decision. Owner: the HTTP transport / PF05 maintainer.
- **O-P06a-23** (IF-09). The engine-core evidence binds the admitted `release_id` through its synthetic root, and its currency test (`tests/evidence/test_engine_core_evidence.py`) does not check that field, so a re-cut without the engine-core owner leaves stale release bindings that no gate detects. Every future re-cut should run that owner (plan §5.9 lists it nowhere). Owner: evidence owners / plan authors.
- **O-P06a-24** (CR-02). Codex independently confirms the practical effect of C040-08. The register entry stays `PROPOSED`; its owner's disposition decides whether the v1 schema's error branch admits `schema`.

## 12. `CANON_CONFLICT_REGISTER`

C040-01 to C040-07 are carried unchanged from plan v1.0 §13.1 and result v1.0 §11. No entry was reopened, relabeled, omitted, newly decided or resolved; PR-35 opened none. Candidate C040-08 stays `PROPOSED` (plan §13.1), with CR-02 as further evidence of its interim risk; this record decides nothing about it.

## 13. Publication (PR-35)

- **Corrective commit.** `dc958ec568e55984d2c4a242cd4ff51726a132fb` (tree `0f29d0905e37036823877ec957d0ca3014131ab9`), one commit above `b23c06f`: the fix, its tests, the re-cut and the converged evidence. An intermediate commit with the fix but no re-cut would refuse admission on every lane (plan §9), so the correction is one commit.
- **Records commit.** This file, ledger v1.1, the PR-35 checkpoint v1.0 and the conditional PR-40 handoff v1.0, all under `docs/ephemeral/`, directly above `dc958ec`.
- **Push.** One `git push origin claude/admiring-tesla-h3awg8` carrying both commits, so hosted CI runs once, on the records head, which classifies the whole pull request against its base (all seven lanes). The pushed SHA, the `git ls-remote` read-back, the PR read-back, that head's CI run and Codex review are recorded in the PR #508 body and the PR-35 return.
- **After the push.** One reply on each of the three threads, then each thread resolved; one `@codex security review` request, so a Security Review covers the corrected head. Their ids are recorded in the PR #508 body.
- **Not done, by rule.** No merge, auto-merge or scheduled merge; no `[skip ci]`; no second pull request or branch (the harness branch `claude/youthful-faraday-o3tsf8` was never committed to or pushed); no force-push or rebase; no Notion write; no `docs/pfcanon/` write; no Claude Code Review installation or trigger (Codex is the only reviewer).

## 14. Prompt-use provenance

`GCFPE_PROMPT_USES`: `GCFPE-USE-HDE-EPIC040-PR-35-20260926-PR06a-01` (this PR-35 phase); carried: `GCFPE-USE-HDE-EPIC040-PR-30-20260926-PR06a-01` and the earlier entries result v1.0 §13 lists.

- Prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1, `https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`, page read as of `2026-09-24T15:48:24.405Z` (Notion read only).
- Release: GCFPE-20260914.1 / 091426.1.
- Change / unit: HDE-EPIC040 / HDE-EPIC040-PR06a; Specification v1.1; instruction v1.0; plan v1.0.
- Role / stage: dedicated PR-35 session / PR-35.
- Execution identity: harness session `https://claude.ai/code/session_01QAme7bG6ZDJ5AEsYfRbLr9`.
- Repository persistence: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` remains absent; `PENDING / NON_GATING`; owner: the authorized repository writer once a procedure is installed.

## 15. Continuation

- `MERGE_PENDING`, subject to *Final head* (§1). Nathan / Product Owner merges PR #508 manually. This session stays subscribed to PR #508 and does not poll; if the subscription delivers Nathan's merge, it returns `MERGE_OBSERVED` with the PR-40 handoff.
- Conditional PR-40 handoff, usable only after Nathan's manual merge and only where no `MERGE_OBSERVED` result was returned for that merge: `docs/ephemeral/HDE-EPIC040-PR06a-conditional-PR40-handoff-v1.0.md`.
- Merging PR06a makes Reader v2 (`POST /api/reader?v=2`), the production Reader at `/api/reader` with the governed 405 for every other method, the corrected Reader v1 schema and goldens, the restored dev conjunction capture and the 45-member `1.2.0` release (`release_id 9f962ce3…`) with its converged evidence current on `main`. It establishes none of QA verdict, acceptance, PF09 movement, OPS01's final external attestation, C040-07 drainage, deployment, activation or Epic closure (plan §15). PR07 must follow PR06a; OPS01 verifies the 45-member release.
