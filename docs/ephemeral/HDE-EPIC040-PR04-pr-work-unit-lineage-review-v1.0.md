---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-EPIC040-PR04-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: ACCEPT
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
reviewer: retained whole-change HDE-EPIC040 Implementation Architect, read-only PR lineage-review role
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-22T21:35:55Z
return_owner: the same retained whole-change HDE-EPIC040 Implementation Architect
---

# HDE-EPIC040-PR04 — PR Work-Unit Lineage Review v1.0

## 1. Decision

**decision: ACCEPT**

`HDE-EPIC040-PR04` — Bounded application, identity and consumer integration — is accepted as the landed, attributable PR work unit for its approved scope. This is a read-only PR-40 decision after Nathan / Product Owner's manual merge of PR #467.

It approves no later work. It is not a QA verdict, acceptance-token satisfaction, OPS result, PF09 movement, release admission or activation, deployment, PF10 edit, Canon drainage, Product Owner closeout, or Epic closure. It authorizes no PR05, PR06, PR07 or OPS01 activity.

**ACCEPT is qualified by three Product Owner-decided deferrals and one stated review limitation**, all recorded in §9 and §10 and none of them waived here. Most consequentially: **the landed head leaves two tests failing (§9.3) and the PF05 Required-Now production Reader route unserved (§9.1)**. Both are explicit, written, Product Owner-decided, PR07-owned deviations — not silent waivers, and not defects this review discovered and passed over.

| Field | Value |
| --- | --- |
| Artifact type | `PR_WORK_UNIT_LINEAGE_REVIEW` |
| Logical ID / version | `HDE-EPIC040-PR04-PR-WORK-UNIT-LINEAGE-REVIEW` / `1.0` |
| `CHANGE_CLASS` / `CHANGE_ID` | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| `WORK_UNIT_ID` | `HDE-EPIC040-PR04` |
| Reviewer / role | The retained whole-change HDE-EPIC040 Implementation Architect, in its established **read-only** lineage-review role, as instruction v1.0 §14 designates — not the PR04 engineer and not Isis-50 |
| `session_disposition` / `role_session_ref` | `RETAIN_EXISTING` / that same retained whole-change IA session |
| `invocation_binding` | `HDE-EPIC040 / HDE-EPIC040-PR04 / PR-40` (`GCF-17.LINEAGE`) |
| `context_conflict` | `NONE` established |
| Decision time | `2026-09-22T21:35:55Z` |
| Return owner | The same retained whole-change HDE-EPIC040 Implementation Architect, for current immutable Plan progression |

## 2. Correction to an artifact this reviewer authored

Recorded first, because it is a defect in this reviewer's own earlier output and observation **O-13** routes it here.

`HDE-EPIC040-PR04-PR-INSTRUCTION` v1.0 §6.5 named `POST /api/reader?v=1` as "the existing declared route" and directed implementation there, while its own §3.2 recorded the observed 405 at **`POST /reader`**. The instruction did not flag that these are different paths. Verified at the approved base `3b8084d0`: `adapter/http_reader.py:459` defines `@bp.post("/reader")` returning 405, and both `adapter/factory.py:11` and `adapter/http_reader.py:913` register the blueprint with `url_prefix=""`. The served path was `/reader`; `/api/reader` was never mounted.

The instruction inherited that conflation from the immutable Plan v2.1 §5.8 ("Production Reader's existing contracted `POST /api/reader?v=1`") and carried it without qualification. Plan v1.2 item 5 / risk R-18 / plan observation O-11 then restated it as an identity. Execution disproved it (result §8.3, F03).

**Effect on this decision: none.** The engineering delivered the handler the instruction described; what the conflation obscured is *where it is served*, which is exactly F03. **Owner: this reviewer**, for any later instruction or PR07 input package. The instruction v1.0 is historical and is not rewritten here.

## 3. Verified merge state and landed attribution

Independently verified from repository and authorized API evidence, not from the PR description or the handoff. Nathan's invocation supplies the merge assertion only; it is not proof.

| Fact | Verified value | Method |
| --- | --- | --- |
| Pull request | [#467](https://github.com/amthorn78/glow-hdengine-v2/pull/467) — the only PR in this work unit | API `get` |
| Merge state | `merged: true`, `state: closed` | API `get` |
| `merged_at` / `merged_by` | `2026-09-22T21:12:30Z` / `amthorn78` | API `get` |
| Base | `3b8084d09e974f15c2b71112e5a596af01b1a371` | API `get`; confirmed as the merge commit's sole parent |
| Reviewed / tested head | `106496971fe46ef7a0414a00944bb034d508b9e2`, tree `72f0868de3635494916097b36656af302b914003` | `git log` on `refs/pull/467/head` |
| Landed commit | `cd6f9e6ca4541f448f77b206269f3882cb919f36`, tree `72f0868de3635494916097b36656af302b914003`, committed `2026-09-22T22:12:30+01:00` | `git log` |
| Merge method | **SQUASH** — the landed commit has exactly one parent, `3b8084d0` (the approved base) | `git log --format=%P` |
| Ancestry | Head `1064969` is **NOT** an ancestor of `main`; landed commit `cd6f9e6` **IS** | `git merge-base --is-ancestor` |
| Tree equality | `git diff 1064969..cd6f9e6` is **empty**; both trees are `72f0868d` | `git diff --stat` |
| Scope, base..landed | **98 files, 9,509 insertions, 2,072 deletions** | `git diff --shortstat` |
| Commits on branch | **33**, `3b8084d0..1064969` | `git rev-list --count`; API reports 33 |

**Attribution rule applied.** Because the merge was a squash, the PR head is not reachable from `main`, so attribution is by **tree identity, not ancestry**. The landed tree is byte-identical to the reviewed and CI-tested head, so everything CI and review observed on `1064969` is exactly what landed. Every handoff-supplied merge fact was independently reproduced and matched.

**Merged-change attribution.** Comparison cutoff `main` at `71511b99fe1e96898ffdbfc8426f39f2e113de4a` (tree `d259b760`). Attributed change: PR #467, landed `cd6f9e6`. Reconciliation of the direct PR delta against the landed delta: **EXACT** — identical trees. Read-only invariant held: the working tree was clean before and after every observation, and no repository mutation occurred.

**Later repository divergence, excluded from attribution.** Exactly one commit sits between the landed commit and the comparison cutoff: `71511b9` "docs: GCFPE MGMT change-process audit, RCA and redesign - plus D20 (#468)" — 9 files, 2,058 insertions, documentation only. It is **not** PR04 work and is excluded. No revert, interstage non-lineage commit or worktree-only divergence was found.

**Branch preservation — a correction to the handoff.** The handoff states the branch is preserved on origin. It is not: `git ls-remote --heads origin` returns no `claude/peaceful-gauss-jhyezn`, so the branch was deleted at or after merge. The head remains reachable as `refs/pull/467/head`, which is how this review resolved it, so no evidence was lost and nothing in the attribution depends on the branch ref. Non-gating.

## 4. Controlling lineage and sources

All repository paths in `amthorn78/glow-hdengine-v2`, verified at the comparison cutoff.

| Role | Identity | Path / SHA-256 |
| --- | --- | --- |
| `PR_INSTRUCTION_ID` | `HDE-EPIC040-PR04-PR-INSTRUCTION` v1.0, `INSTRUCTION_READY` | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md` — recomputed `8769d12f8e4df82eed9f4869e4a48ca53ae8a99d7a6b6497df526036f30ffdcf` ✓ |
| `PR_IMPLEMENTATION_PLAN_ID` | `HDE-EPIC040-PR04-PR-IMPLEMENTATION-PLAN` v1.2 — the Proceeded plan | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.2.md` — recomputed `dc005adc9ec0acd4541241f1893712d5c780f01632a09284aa6bd3d779779160` ✓ |
| PR-30 result | `PR_CANDIDATE_PUBLISHED`; implementation `881cc2df6ca79ab8564bba9d9e20013807ecf077`, tree `475ba9b440fbcac6336e49cca2739097991dea88`; records `e7c5323a6db0eb651db3bf81c90c40efd95d3f70` | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-result-v1.0.md`, SHA-256 `734e69f24cc4891dfb72c10d10137c774af7e3a586384df1a462bcb6313243e5` |
| PR-35 result | `MERGE_PENDING — Ready to merge`, §11A of the same continuous record, on head `1064969` | same path |
| Original Proceed | PR-30 — PR Implementation Proceed — 091426.1, for plan v1.2 **only**; authorizes implementation only; preserved unchanged through PR-35. **No second Proceed exists** | result §2 |
| `SPECIFICATION_ID` | `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`, Thoth-17 `APPROVE` 2026-09-08T13:23:24Z | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` |
| `IMPLEMENTATION_AUDIT_ID` | v2.0, `AUDIT_COMPLETE` | `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md` |
| `IMPLEMENTATION_PLAN_ID` | v2.1, immutable approved base | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`, `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| `PLAN_REVIEW_ID` | v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z; redline `R040-IA30-02` | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` |
| Accepted dependencies | PR01 `ACCEPT` (#403); PR02 `ACCEPT` (#404); PR03 `ACCEPT` / `ACCEPTED_FINAL` (#405) | the three `…-pr-work-unit-lineage-review-…md` files. **Accepted-final: not rerun, reopened or revised by this review** |
| Checkpoints and ledger | PR-30 checkpoint; PR-35 entry and corrective checkpoints; remote-action ledger **L-01…L-72, 72 rows verified** | `…-pr30-checkpoint-v1.0.md`, `…-pr35-entry-checkpoint-v1.0.md`, `…-pr35-corrective-checkpoint-v1.0.md`, `…-pr-remote-action-ledger-v1.0.md` |

**Current controlled PF10, resolved by this reviewer from `docs/pfcanon/`.** `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`, **1,760 lines / 194,329 bytes, SHA-256 `abcf86b82e6de7a0103534bf1deff140f5da273cb67412fd6e0a2c5838590afa`**. §2.15 is present in both the Addendum Index (line 200) and the body (line 1636). Recorded as provenance of what was read; it gates nothing.

**A PF10 currency fact, recorded rather than treated as a defect.** The same version string `v13.2.9` carried different bytes earlier in this lineage: at the RS-20/RS-30 stage it was 1,649 lines / 181,316 bytes, SHA-256 `1421e4d6…`. The difference is the insertion of §2.15 — the F01 addendum — in commit `3b8084d0`, which is exactly PR04's approved base. So Nathan published the approved F01 addendum into PF10 before the work unit branched, without a version bump. Consistent, and it independently corroborates the F01 overlay's publication. PF10's own index/body inconsistency at §2.14 (U-05) persists and remains the PF10 drain owner's.

`docs/pfcanon/` was read only and was not written. Google Drive was not used as a source, store or authority.

## 5. F01 overlay conformance — verified by reading and by execution

F01 was approved by **Isis-50, `decision: APPROVE`** (`docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md`, SHA-256 `7700796f…`), after an earlier `REVISION_REQUIRED` against proposal v1.0. One addendum was emitted: `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md`, recomputed SHA-256 `86708f5c32de990be892bbb3f1ced973c5a110e30496753ca871b8f72c8082c1` ✓, corresponding to PF10 §2.15.

**File-set conformance.** The implemented overlay (result §5) covers exactly the enumeration the approved proposal v1.1 derived, including the two files added during the RS-20/RS-30 round trip: `run_sanity_pipeline_gate.py` (the R-1 find) and `generate_determinism_gate_proofs.py` (the R-2 trace find). The four pinning test homes were updated as enumerated. `run_canonical_json_gate.py` needed no `RELEASE_NOT_ADMITTED` expression — frozen-digest validation only, `--check-only` returns 0 — which confirms the proposal's exclusion **X-8** was correctly reasoned. `tests/evidence/test_release_attestation.py` was not edited and passes, confirming exclusion **X-10**. No thirteenth or fourteenth file was required.

**The four binding conditions, each verified independently.**

| Condition | Verification |
| --- | --- |
| Never `PASS`, never `top_level_pass: true`, never a frozen-byte substitute presented as live | **Executed at the landed tree**: `generate_open_rails_abba_proof.py --check-current` under the job-declared rails exits **3** and prints `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED`; nothing written; working tree clean before and after. The pipeline's third status is `NOT_ADMITTED`, and `summary:PASS` still requires all `OK` |
| Acceptance keys on the one explicit outcome and the observed non-admitted state — never a generic failure, lane name or time window | `ci.yml` accepts the rails runner's exit 3 **only with the independent probe**, and the release step accepts a non-zero builder exit **only** when `failure.json` carries `code == release_not_admitted` **and** the probe observes `INCOMPLETE_RELEASE_ROSTER` (result §5 row 8) |
| Self-extinguishing by construction | The discriminator classifies exactly `SchemaValidationError.code == "INCOMPLETE_RELEASE_ROSTER"`; every other exception and every post-admission failure stays an ordinary failure. Once PR06 admits the roster the branch is never taken |
| No change to `hde.release_attestation.v1` or to `PR06R_B_FINAL_PASS` | **`git diff 3b8084d0..cd6f9e6 -- schemas/hde_release_attestation*.json` is empty.** At the landed tree `release_admission` remains `{"const": "PR06R_B_FINAL_PASS"}` and `validation_result` remains `{"const": "PASS"}`. No PF12 canon decision was consumed |

The non-admitted outcome travels the **existing** failure-receipt path under `hde.release_attestation.failure.v1` with the code `release_not_admitted`, exactly as the approved narrowing predicted — an open `^[a-z0-9_]+$` token requiring no schema change.

## 6. F02 delta conformance — verified exactly

F02 is a **Product Owner direct approval** of `docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md` §5 (SHA-256 `cf6d8f2c…`), recorded in plan v1.2 §1 and §14.3. There is no RS-20 decision, no addendum and no new Proceed, and this review neither invents nor requires one.

Verified by parsing `catalog/manifest.json` at the approved base and at the landed commit:

| Check | Result |
| --- | --- |
| Top-level keys | `{built_at_utc, files, root, version}` both sides — unchanged, no self-listing |
| `root` / `version` / `built_at_utc` | `catalog/` / `1.0.0` / `2025-12-26T00:00:00Z` — **all preserved** |
| Member count | **15 both sides** — the release remains the incomplete roster; nothing admitted, activated or promoted |
| Row order | **Identical** |
| Rows changed | **Exactly one** — `adapter/http_reader.py` (`9f0cde20…` → `3a6bd46a…`) |
| `release_id` = sha256 of canonical bytes | base `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856` → landed **`a5f06ae3fcc964c41bb80c3630f455d9c246d9f87fcad500a5b74bf79b96bc01`** — matches the handoff exactly |

The re-cut ran four times because `adapter/http_reader.py` changed four times; each pass changed only the same row, through the owning writer `scripts/cut_release_manifest.py` with pinned arguments. **Result v1.0 §6 documents only the first two re-cuts** (ending `a6db0106…`); the final two are recorded in the PR body and the ledger. The landed manifest is the authority and it is verified above. Non-gating record-completeness observation, noted in §11 as **N-02**.

## 7. Requirement coverage across the complete work unit

Assessed against instruction v1.0 §8.1, which allocates to PR04: `K040-REQ-001`, `-004`, `-005`, `-007`, `-008`, `-010`, `-011`, `-012`, `-013`, and the PR04 portions of `AC040-03`, `-04`, `-06`, `-07`, `-08`, `-09`.

| Area | Finding |
| --- | --- |
| Three admitted input classes; chart-bearing resolution | Delivered. `engine/bodygraph/resolver.py::resolve_compat_chart` implements the three classes with guarded dry-run acquisition and `projection_refusal`; `_resolve_party`'s UID-only returns are gone |
| Canonical internal identity via the birth seed and `resolve_db_user_id` | Delivered in `engine/bodygraph/projection.py` (`bind_projection_identity`, canonical/strict UUID helpers) |
| Complete normalized projection → `EvaluationParty`; eligibility before core/cache/router | Delivered in `engine/compat/compute.py` (`EvaluationParty`, PF01 §4 carrier, `orient`, intrinsic `pair_key`, cache seam, bidirectional router augmentation, `evaluate_pair`) |
| One core; legacy success paths removed | **Verified directly**: `ts_v0` no longer appears in `engine/runtime/public.py`; `evaluate_pair` and `admitted_bundle` delegate to `load_active_mechanics_bundle` |
| Admission consumed, never bypassed | **Verified by execution**: the landed gates refuse with `INCOMPLETE_RELEASE_ROSTER` and express it truthfully. No synthetic release reaches any governed gate or the attestation |
| PF05 §5.2.3 token surface | Delivered — eleven tokens, `MAGIC10_HTTP_STATUS`, `BOUNDARY_REASONS`, `CompatBoundaryError`; `errors/token_map/token_map.json` regenerated by its owner |
| Reader POST success path | **Delivered as a handler at `POST /reader`; NOT served at PF05's Required-Now `POST /api/reader?v=1`.** See §9.1 (F03) |
| Reader envelope / numeric-free six-key output | Delivered through the existing single emitter; **but the emitted `categories` identity fails the published schema.** See §9.2 (F05) |
| `R040-IA30-02` no-user proof classes | Delivered — the boundary, acquisition-seam, closed-rails-miss, invalid-identity, source/side-effect and separate-Reader classes, with the old stable-hash fixture converted to the truthful negative case |
| Evidence ownership and regeneration | Conforms. Result §7 maps every touched family to its owning writer; frozen families keep capture-time bytes with nonclaims; **nothing governed was hand-edited**, and this review found no evidence of hand-editing |
| Governed-artifact owner regeneration | Conforms — `token_map.json`, `catalog/manifest.json`, canonical-JSON gate outputs, the sanity log (PASS → NOT_ADMITTED model, 799 → 837 bytes) and Index/Mirror, each through its declared owner |
| Migration / security / recovery | Conforms — no DDL, backfill, account creation, new vendor route, credential, production mutation or rail opening. The P-21 fix bounds the production POST body read (5,000,102 → 32,769 bytes consumed) with a regression test |

**Conclusion.** The approved bounded scope is delivered, with two production-surface requirements partially delivered (§9.1, §9.2) under explicit Product Owner deferral. No requirement was silently dropped, and no scope was added.

## 8. Review and CI evidence

**Code review.** Codex review rounds are independently visible on the PR across `73b9812`, `7fe3630`, `730208c`, `aa5c3cc`, `dca3a93`, `c147e76`, `caec701` and `6f5aeed`, matching the recorded sequence. Sixteen threads; twelve resolved, four open by design with named owners (O-12 packaging; O-19/F07; O-20 and O-21 capture generators — the last three to PR06/PR07). Thirteen findings were dispositioned; eight fixed in scope (P-21 unbounded body read, F04 rails-runner exit 3, sanity-stage gating, F06/P-23 stored-Gate 503, P-24 legacy emitter contract, P-25 core config classification, P-26 admission classifier, P-27 the config-before-stale ordering gap in P-25). No review event carries `APPROVED` or `CHANGES_REQUESTED`; all are `COMMENTED`, consistent with an advisory reviewer rather than a human approval gate. No approval was invented here.

**CI.** Exact-head run **`35777936856`** verified through the authorized API: `conclusion: success`, `status: completed`, **`head_sha` exactly `106496971fe46ef7a0414a00944bb034d508b9e2`**, event `pull_request`, workflow `.github/workflows/ci.yml`. Zero failed jobs; all seven lanes; final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; the accepted `RAILS_LANE:RELEASE_NOT_ADMITTED` and `RELEASE_LANE:RELEASE_NOT_ADMITTED` outcomes. Because the landed tree equals that head's tree, this CI result attaches to exactly what landed.

Two earlier runs in this phase failed on the session's own defects and both were fixed before the final head: `35763461703` (the `http_reader` owner-guard tuple, §8.7) and `35770839639` (a test writing a wall-clock timestamp into a tracked artifact, §8.9). Recorded as history, not as the current state.

**No scoped CI waiver was requested, granted or relied upon.** The RELEASE_NOT_ADMITTED outcomes are the approved F01 posture, not waivers.

## 9. Deferrals, limitations and open items — recorded, not waived

### 9.1 F03 — the PF05 Required-Now production Reader route is not served

`POST /api/reader?v=1` returns **404**; the handler is served at `POST /reader` because the blueprint mounts at `url_prefix=""`. **Independently verified** at both the base and the landed tree. **Decision: DEFER to PR07 — Nathan / Product Owner, 2026-09-22**, recorded in `docs/ephemeral/HDE-EPIC040-PR04-F03-deferral-decision-v1.0.md` as "PR04 merges as implemented; the gap is an accepted, owned deviation". Carries observation O-14 and the O-03 catalog row. This is the requirement §2's conflation obscured.

### 9.2 F05 — the Reader response fails its published schema

The Reader emits `harmony`; **verified independently** that `schemas/reader.v1.schema.json` contains no `harmony` and admits only `open_leader`, `warm_leader`, `cool_leader`, `glow_leader`, and that `goldens/reader/v1/*` pin the legacy identities. **Decision: DEFER to PR07 — Product Owner, 2026-09-22 (option 3: fix F06, defer F05)**, recorded in `…-F05-deferral-decision-v1.0.md`. Observation O-15. Settles alongside F03 as one production-Reader surface.

### 9.3 F07 — two tests fail at the landed head

**Reproduced by this reviewer at the landed tree**: `tests/evidence/test_dev_conjunction_identity.py` → **2 failed, 1 passed**, failing at `tools/evidence/generate_conjunction_writer_evidence.py:85: SystemExit`. Working tree clean after.

Two facts matter and are stated plainly. First, **PR04 edited neither file** — `git diff 3b8084d0..cd6f9e6` over both paths is empty — so this is a *consequential* regression from the boundary change, not an edit. Second, **no CI lane runs it**: `_lanes_for_path` maps it to `{'evidence'}`, but the evidence lane's pytest list does not include it, it is not in `_FULL_VALIDATION_SUPPLEMENTAL_TESTS`, and it was not a changed-test target. So it does not gate, and CI's green result does not cover it. Both verified directly.

**Decision: DEFER to PR07 — Product Owner, 2026-09-22**, recorded in `…-F07-deferral-decision-v1.0.md`. Observation O-19 records the three-way measurement showing no PR04-internal fix exists that is not an admission bypass. PR07 depends on PR06 admitting the roster.

**This review does not treat a failing test as passing.** The repository is left with two failing tests outside CI coverage. That is an accepted, owned, written deviation — and it is a real cost, carried forward visibly rather than absorbed.

### 9.4 Security review — a stated limitation, not a satisfied predicate

Codex's security review completed only on the **PR-open head `e927ed0fa2e737f96d47e0cf7b238033484e4006`**. It does not re-run on new commits; both `@codex security review` requests were routed to the Code Review track; the connector reports `mergeGateEnabled: false`. **There is no current-head security review.** Recorded as a limitation. This review does not convert its absence into a satisfied predicate, does not invent a review, and does not create a new merge gate for it. Owner: Product Owner, for whether a current-head security review is required before PR05–PR07 or QA.

Relatedly, the final Codex round on `1064969` is recorded by the PR-35 session as completing with no findings. The reviews API shows no review event on that head, which is consistent with the connector's documented behaviour of reacting rather than commenting when it has no suggestions — so that particular outcome is **not independently verifiable from the API** and is carried as the session's record. Non-gating.

### 9.5 Open review threads and carried observations

Four threads open by design with named owners: **O-12** (roster not shipped with installed packages — packaging/release owner), **O-19/F07** (PR07), **O-20** (capture generators parse the retired `compat.meta` shape) and **O-21** (canonical parity harness aborts on its own birth-only inputs) — the last two to PR06, where capture write mode first becomes reachable. Also carried: **O-16** (`ERR_M10_GATES_MISSING` registered but unreachable), **O-17** (pre-existing `dev/reader_harness` `AttributeError`, patch recorded), **O-18** (narrative pack mounts from the request path — a production failure mode, unreachable pre-admission), **O-03**, **O-06** through **O-11**.

**Plan defects surfaced and recorded rather than silently overwritten**: O-13 (§2), P-23 (the plan specified a 422 that PF05 §5.2.3 contradicts), P-24 (the plan checked `engine/emit_public.py` for removed helpers rather than the changed signature), and O-18's sharpening of plan O-07/R-09 from tree hygiene to a production failure mode. This reviewer endorses recording them in place; none is a rescope and none changes approved scope.

### 9.6 Coverage finding

The base-vs-head sweep of the **132 test files reached by neither a CI lane nor a changed-test target** found **4 regressions and 0 fixes** (result §8.8); two were fixed here and two are F07. Fourteen files fail at collection at both base and head, so the sweep requires `--continue-on-collection-errors`. This reviewer regards the sweep as the right response to a real blind spot and its adoption as a standing pre-push check as proportionate. The pre-existing collection errors and five pre-existing failures are outside CI lanes and are **not** claimed fixed.

## 10. `CANON_CONFLICT_REGISTER`

Carried unchanged through instruction, plan, implementation result, PR lineage and this review. **No entry is reopened, relabeled, omitted, newly decided or resolved. PR04 opened no new register entry.**

| ID | Classification / status | Decision lineage | Carried effect | Remaining owner / state |
| --- | --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION` / `APPROVED` exactly as proposed | Thoth-17, 2026-09-08T13:23:24Z, against Specification v1.0 represented by approved v1.1 | Explicit `Done` exclusions and current PF09.3 agreement preserved | Source correction resolved; no drainage pending |
| `C040-02` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Current controlled PF12 Markdown used; historical identity mismatch is history only | Resolved; PF12 version currency remains ordinary maintenance (U-04) |
| `C040-03` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Current PF14 v3.5.7; C040-05 controls its contradictory core-test text | Historical mismatch resolved |
| `C040-04` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | QA identity history preserved; PR04 performed engineering checks, not independent QA | Historical mismatch resolved |
| `C040-05` | `CANON_RECONCILIATION` / `APPROVED`, alternative A exactly | Isis-49, 2026-09-09T03:57:16Z, against Plan v1.0 | The four-argument Gate core supersedes precomputed-score passages; PR04 introduced no second calculator and removed `ts_v0` | Permanent PF14 §6.7 correction pending with its governed maintainer; non-gating |
| `C040-06` | `NEW_CANON` / `APPROVED`, alternative A exactly | Isis-50, 2026-09-09T11:48:08Z, Review v2.0 against Plan v2.0 and ADR v1.0 | 36-row taxonomy and 16-case conformance consumed through PR01–PR03; no changed weights | Permanent PF12 §2.1 and PF01 §§6.1–6.2 drainage pending with governed maintainers; non-gating |

**On the PF01 §4.5 versus PF05 §5.2.3 token-naming tension**, carried as plan observation O-01 / result O-16 and routed to the governed PF01/PF05 maintainers, decided by no one in PR04 — **this reviewer assesses that treatment as correct.** It is a naming conflict between two Canon owners, not an implementation defect: plan decision D-04 settled PR04's behaviour (application boundaries keep the instruction §6.6 `ERR_READER_*` mapping while the §5.2.3 tokens are registered), and overriding it during PR-35 would have contradicted the approved plan. It is **not** silently resolved here, and it is **not** promoted to a register entry, because no Canon decision has been made. It remains with its named owners, non-gating, with a one-tuple-plus-owner-regeneration remedy recorded if they want it.

**PF10 boundary.** This review numbered, inserted, edited, uploaded or published nothing in PF10. The F01 addendum is carried as evidence under its own native authority.

## 11. Findings from this review

| ID | Finding | Effect | Owner |
| --- | --- | --- | --- |
| **N-01** | Instruction v1.0 §6.5 conflated `POST /api/reader?v=1` with the route its own §3.2 observed at `POST /reader`, inheriting Plan v2.1 §5.8's wording. Root of O-13 and the framing gap behind F03 | None on this decision; the handler described was delivered | **This reviewer**, for later instruction or PR07 inputs |
| **N-02** | Result v1.0 §6 records two of the four F02 manifest re-cuts (ending `a6db0106…`); the final `a5f06ae3…` appears in the PR body and ledger. The landed manifest is verified correct in §6 | Record completeness only; no manifest defect | PR04 engineering session, if it revises the result |
| **N-03** | The handoff states the PR branch is preserved on origin; it is not (§3). The head remains reachable via `refs/pull/467/head` | None — attribution was completed without the branch ref | Recorded |
| **N-04** | Two tests fail at the landed head, outside all CI coverage (§9.3) | Accepted, Product Owner-decided, PR07-owned deviation. Not a silent waiver | PR07 (gated on PR06) |
| **N-05** | No current-head security review exists (§9.4) | Stated limitation; not a satisfied predicate and not converted into one | Product Owner |

No finding in this review is a precise substantiated defect requiring the PR-40 bounded-owner return route, because every one is either already dispositioned by its authorized owner or is a record-completeness item. No material scope, architecture, requirement or design boundary was discovered, so no RS-10/RS-20 route is opened.

## 12. Truthful state values

`NOT EXECUTED` by this review and by PR04: independent QA of any kind, QA verdict, acceptance-token satisfaction, Ops execution, deployment, release admission, promotion or activation, PF09 status movement, PF10 edit or Canon drainage, Product Owner closeout, Epic closure, PR05, PR06, PR07 and OPS01 work.

`NOT PRODUCED`: any PR05/PR06/PR07/OPS01 artifact; any QA Guide, Plan, task, execution result or report for this change; any new PF10 addendum; any second acceptance receipt.

Preserved unchanged: the immutable Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review v2.1; the approved F01 overlay and its addendum; the Product Owner-approved F02 delta; accepted-final PR01, PR02 and PR03; the original Proceed; every checkpoint, ledger entry and deferral decision; and the PR-35 `MERGE_PENDING` record, which remains a truthful **pre-merge** checkpoint and is **not** restated here as a post-merge fact or rewritten.

## 13. Coverage limitations of this review

- Read-only throughout. Three executions were performed against the landed tree — the F01 rails gate, the F07 test module, and manifest parsing — each with a clean working tree before and after and no repository mutation. Everything else is reading.
- This review did not re-run the full CI suite, the seven lanes, or the attestation builder. It verified the hosted run's identity, conclusion and exact head binding through the authorized API and relies on that, plus the tree equality in §3.
- The final Codex round's "no findings" outcome on `1064969` is not independently verifiable from the reviews API (§9.4).
- Requirement coverage in §7 was assessed against instruction §8.1 and verified by targeted source reading and execution at the landed tree, not by exhaustively re-deriving every acceptance criterion.
- PF sources were resolved only from `docs/pfcanon/`. No Google Doc, `.doc`, `.docx`, export, archive result or search hit was opened, compared or cited.

## 14. Prompt-use provenance

`GCFPE_PROMPT_USES` — this entry, preserving earlier ones by exact reference:

- `usage_id`: `GCFPE-USE-HDE-EPIC040-PR-40-20260922-PR04-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`
- `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`
- `work_unit_id`: `HDE-EPIC040-PR04`
- `ecosystem_release`: `GCFPE-20260914.1`, selected contract `091426.1`, 55 members
- `prompt`: `PR-40 — Review PR Work-Unit Lineage — 091426.1`
- `prompt_page`: `https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634?pvs=204`
- `prompt_retrieved_revision`: page fetched, `page_last_edited_at` `2026-09-21T22:56:56.431Z`
- `role_stage`: retained whole-change HDE-EPIC040 IA session / PR-40 read-only lineage reviewer
- `execution_posture`: `MANUAL_PROMPT_EXECUTION`
- `capture_time`: `2026-09-22T21:35:55Z`
- `supporting_skill`: `glow-merged-change-attribution-lock` consulted for the post-merge attribution method (§3); evidence-only, no authority
- `result`: this `HDE-EPIC040-PR04-PR-WORK-UNIT-LINEAGE-REVIEW v1.0`, `decision: ACCEPT`

Preserved earlier entries by exact reference: `GCFPE-USE-HDE-EPIC040-RS-30-20260922-PR04-F01-01` (proposal v1.1 §13), `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-01` (review §13), `GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01`, `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01` (plan §16) and `GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01` (instruction §15). The PR-30 and PR-35 entries are preserved in the implementation result.

Repository provenance persistence remains `PENDING / NON_GATING`: `docs/changes` holds no installed `GCFPE_PROMPT_PROVENANCE.md` procedure, schema, writer or destination.

## 15. Native return

`HDE-EPIC040-PR04` is **`ACCEPTED_FINAL`**. It is never rerun, reopened, revised or issued a duplicate acceptance receipt.

The next native owner is the **same retained whole-change HDE-EPIC040 Implementation Architect**, for current immutable Plan progression under the fixed order `PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01`. The next planned unit is **PR05** — full golden comparison and read-only Gate readiness — whose PR-10 instruction-authoring stage may now begin.

PR05 inherits the F01 interim gate condition through the release lane, as the approved rescope review established; it requires no separate overlay and receives no new loci. PR06 retains complete release admission and convergence; PR07 inherits F03, F05 and F07 with their written decision records; OPS01 retains final external verification.

This acceptance authorizes no PR05 implementation, no Proceed, no merge action, no PF10 modification, no QA or Ops execution, no release admission or activation, no PF09 movement, and no Epic closure.
