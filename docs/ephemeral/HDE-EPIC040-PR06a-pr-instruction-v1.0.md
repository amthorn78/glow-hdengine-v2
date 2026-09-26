---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-EPIC040-PR06a-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06a
authoring_context: APPROVED_BASE_WITH_OVERLAYS
issuer: retained whole-change HDE-EPIC040 Implementation Architect (PR-10)
capture_time_utc: 2026-09-26T03:08:10Z
baseline_main: 7f58ad613a0991bdc32accb179c30c11715209bc
receiver: dedicated HDE-EPIC040-PR06a PR-development session (PR-20)
---

# HDE-EPIC040-PR06a — PR Work-Unit Instruction v1.0

## 1. Identity

| Field | Value |
| --- | --- |
| Work unit | `HDE-EPIC040-PR06a` — Reader v2 full Magic-10 exposure and the deferred Reader contract work (F03, F05, F07) plus the 45-member release re-cut |
| Origin | Finding `HDE-EPIC040-PR07-F01`, decided by `docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md` (SHA-256 `0c3d4ad7…8a55`) |
| Operative overlay | `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` (SHA-256 `a69e2205…28e9`), drained as PF10 §2.23 |
| State | `INSTRUCTION_READY` |
| Dependency position | `PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR06a → PR07 → OPS01`. PR01–PR06 are `ACCEPTED_FINAL` |

## 2. Lineage and overlays

Immutable bases, not rewritten: Specification v1.1 (`43e1b182…`), Audit v2.0, Plan v2.1 (`10732f93…`), Plan Review v2.1 (APPROVE). Accepted lineage reviews PR01 v1.1 and PR02–PR06 v1.0 (PR06: `docs/ephemeral/HDE-EPIC040-PR06-pr-work-unit-lineage-review-v1.0.md`).

PF10 read: `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md`, SHA-256 `0029e2827904f6b798f6367f54a8d134bb55d170a412cc544b1555594c4e4f29`, addenda through §2.23. The PR06a handoff cited v13.3.3; v13.3.4 is the later superset and governs. Bearing addenda: §2.12 (admission boundary), §§2.16–2.18 (F03/F05/F07 deferrals, return point reassigned to PR06a), §2.21 (frozen-capture identity), §2.23 (this overlay). §2.15's interval ended with PR06.

Where this instruction and the overlay differ, the overlay governs.

## 3. Baseline and verified loci

Baseline `main` = `7f58ad613a0991bdc32accb179c30c11715209bc`. Verified by reading at that commit:

- `catalog/manifest.json`: 44 members, version `1.1.0`, `release_id` `988ed2a7…`; admission returns `ADMITTED` (PR06 review §3).
- `engine/config/registry_loader.py`: `ADMITTED_RELEASE_VERSION = "1.1.0"` at line 398, `ADMITTED_RELEASE_ROSTER` at line 400, count invariant `!= 44` at line 447.
- `_EVIDENCE_GENERATOR_TEST_OWNERS` at `ci/checks/classify_ci_changes.py:507`.
- The Reader blueprint mounts with `url_prefix=""` (`adapter/factory.py`, `adapter/http_reader.py`); today's served path is `/reader`.
- `goldens/reader/v1/`: `g01_minimal_ineligible.json`, `g02_ab_ba_parity_A.jsonl`, `g02_ab_ba_parity_B.jsonl`, `g03_open_leader.json`, `g04_warm_leader.json`, `g05_cool_leader.json`, `g06_error_invalid_input.json`, each with a `.sha256` sibling.
- Absent, to be created: `schemas/reader.v2.schema.json`, `goldens/reader/v2/`.

## 4. Objective and completion

**Objective (overlay §Objective).** Deliver full Magic-10 exposure through Reader v2, Reader v1 conformed to its unchanged covenant, the production Reader at its PF05 route, the dev conjunction evidence capture restored, and one release re-cut binding the result.

**Completion.** Real integration paths and proofs pass actual code review, security review and ordinary CI on the exact candidate head, under the PR-30 and PR-35 lifecycle, including the strict attestation. PR06a claims no QA verdict, acceptance, deployment, PF09 movement or closure.

## 5. Required deliveries

1. **Reader v2.** New `schemas/reader.v2.schema.json` expressing `C040-07` exactly: `v=2` on `POST /api/reader`; six-key numeric-free envelope with `reader_version` `"v2"`; when eligible, ten `{id,band}` items in canonical order `harmony, heat, communication, alignment, comfort, consistency, expansion, creativity, drive, balance`; `[]` when ineligible; same preimage recipe, AB↔BA identity and two-run identity as v1. Projected by the existing runtime and single emitter from the complete canonical intrinsic matrix — no new presenter module, no second calculator. Goldens under `goldens/reader/v2/` pin eligible, ineligible, AB↔BA and error cases.
2. **Reader v1 conformance (F05).** `schemas/reader.v1.schema.json`: category `harmony` only, `prompt` removed, exact six-key success closure. `goldens/reader/v1/*` reconciled through their owning writer; retired `*_leader` identities (`g03`–`g05`) leave the published contract.
3. **Production route (F03).** `POST /api/reader` serves `v=1` and `v=2`, by a mechanism consistent with PF05 §5.6 and its alias posture (mechanism is the plan's open design choice). Dev `GET /reader` stays at its path and remains v1, byte-unchanged. `docs/ENDPOINTS_CATALOG.json` and `artifacts/audit/ENDPOINTS_CATALOG.json` gain the production rows, including the O-03 `POST` success row. Route falls inside `/api`-scoped ingress policy. PR04 observation O-13 is superseded.
4. **Dev conjunction evidence (F07).** Real admitted release identity, no dev stamp (PF10 §2.12). A dev-only resolver seam, absent by default, removes the live-vendor dependency. Generator assertions track the real identity. Register `tools/evidence/generate_conjunction_writer_evidence.py` in `_EVIDENCE_GENERATOR_TEST_OWNERS`. Regenerate writer artifacts through the owner.
5. **Release re-cut.** `schemas/reader.v2.schema.json` is the one new member → 45. In `registry_loader.py` change only the roster membership, the count invariant (`44` → `45`) and `ADMITTED_RELEASE_VERSION` (`1.1.0` → `1.2.0`). Cut through `scripts/cut_release_manifest.py`; `release_id` recomputed from exact bytes. Config artifacts, registry report, FE/BE bundles and evidence converge through existing owning writers in PR06's generation order. Strict attestation builds and verifies in the ordinary-CI release lane.

## 6. Owned loci (exact paths)

| Path | Bound |
| --- | --- |
| `adapter/http_reader.py`, `adapter/factory.py` | Route and version selection |
| `adapter/wsgi.py` | Only where the route mechanism requires it |
| `engine/runtime/public.py`, `presenter/reader_v1/emitter.py` | v2 projection through existing path |
| `engine/presenter/emitter.py` | Only where the existing emission path requires it |
| `schemas/reader.v1.schema.json` (+ companions) | F05 |
| `schemas/reader.v2.schema.json` (+ companions) | **NEW** |
| `goldens/reader/v1/*` | Via owning writer |
| `goldens/reader/v2/*` | **NEW** |
| `docs/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json` | F03 rows |
| `tools/evidence/generate_conjunction_writer_evidence.py` and its writer artifacts | F07 |
| `ci/checks/classify_ci_changes.py` | Registration only |
| `engine/config/registry_loader.py` | Roster, invariant, version only |
| `catalog/manifest.json` | Only via the cutter |
| Test homes: `tests/http/` (incl. `test_reader_post_v1.py`, `test_reader_a7_transport.py`, `test_endpoint_catalog.py`, `test_dev_conjunction_http.py`, `test_compat_endpoint_contract.py`), `tests/reader_v1/` (`test_schema.py`, `test_goldens.py`, `test_emitter.py`, `test_release_pack.py`, `test_cli_proof.py`), `tests/evidence/test_dev_conjunction_identity.py`, and existing runtime-identity/release/manifest test homes covering changed seams | Covering changed seams; new test files only inside these homes |
| Index/Mirror rows, path proofs, config artifacts, registry report, bundles | Only through owning writers |

A file genuinely required for items 1–5 outside these loci is a finding for the rescope route (§9), not an implicit extension.

## 7. Proof and evidence

Positive and adverse proof, per overlay:
- v2 eligible pairs derived from G001–G008 yield exactly ten items in canonical order, each band equal to the canonical matrix; bytes validate against the v2 schema.
- v2 ineligible pair yields `[]`; a valid complete self-pair takes the ineligible path.
- v2 AB↔BA identity, two-run identity, preimage recomputes.
- v1 success validates against the corrected schema with exactly one `harmony` item.
- Strict version selection: missing, unsupported, duplicated or malformed `v` refused per PF05.
- `POST /api/reader` serves both versions; dev `GET /reader` bytes unchanged; catalog rows match mounted routes.
- No public body carries a numeric, prompt, narrative key, score, UUID or Gate value.
- Dev conjunction capture runs with real admitted identity, no vendor call; its test runs in CI.
- Admission `ADMITTED` on the 45-member cut with recomputed `release_id`; tampered, missing or extra member refused.
- Strict attestation builds and verifies on the exact candidate head.

Evidence lives in native PR artifacts and owner-regenerated governed evidence. QA outputs, if any, go under an HDE-EPIC040 evidence directory, never the repo root.

## 8. Exclusions and inherited state

Exclusions (overlay): no change to Magic-10 mathematics, membership, order, weights, caps, bands or catalog data; no public numeric; no narrative or prompt on any public surface; no new CLI flag; no Reader v1 contract change beyond F05 conformance; no change to `hde.release_attestation.v1` or `PR06R_B_FINAL_PASS`; no admission-logic change; no activation, promotion or deployment; no live vendor or DB operation; no PF-Canon edit; PR06 not rerun; PR07 documentation not absorbed.

Inherited: CR-01 / O-12 (packaged wheel omits members) stays open with the packaging owner / PO; adding a member does not resolve it. §2.21 frozen-capture identity remains in force; frozen captures are not re-identified.

## 9. Rescope route

A required change outside §6 or contrary to §8 is raised as a finding by the PR06a session and routed to the retained whole-change IA, which decides and returns the decision to that same session. Before Proceed there is no RS-40.

## 10. Sessions, merge and CI

- PR-20 runs in the dedicated PR06a PR-development session (`session_disposition: INITIAL_DEDICATED_ASSIGNMENT`, `role_session_ref: NOT_YET_ASSIGNED`). PR-30 and PR-35 run in their own dedicated sessions.
- Nathan / Product Owner alone gives Proceed and merges. No auto-merge.
- Ordinary CI is the single `test` job; the release lane runs the strict attestation on the exact head.

## 11. Migration, security and recovery

- The retired `*_leader` identities are a published-contract change; no repository consumer was identified. A consumer found to depend on them returns to change control.
- Security review of the new public route and the dev resolver seam (must be absent by default and unreachable outside `dev|test|local`) is part of completion.
- Recovery: revert of the squash commit restores the 44-member release; no data migration.

## 12. Register

`CANON_CONFLICT_REGISTER`: C040-01–C040-06 carried unchanged. C040-07 (NEW_CANON, PO-APPROVED): public full Magic-10 via Reader v2; its drainage into PF01/PF04/PF05/PF12 belongs to their maintainers and is non-gating. PF12 v2.9.5 vs recorded v2.9.6 carried, non-gating.

Observation N-01 (Nathan, non-gating): `docs/pfcanon/` holds stale PF10 v13.3, v13.3.1, v13.3.2 and v13.3.3 beside v13.3.4.

## 13. Truth and provenance

Prompt use `GCFPE-USE-HDE-EPIC040-PR-10-20260926-PR06a-01` — PR-10 — Create PR Work-Unit Instructions — 091426.1, on GCFPE-20260914.1 / 091426.1 / 55. Repository persistence `PENDING / NON_GATING`. Inputs: overlay (`a69e2205…`), rescope decision (`0c3d4ad7…`), PR06a PR-10 handoff (`46602a03…`), PF10 v13.3.4. This instruction implements nothing, requests no Proceed, and edits no PF10.

## 14. Readiness

`INSTRUCTION_READY`. PR-20 may begin.

## 15. PR-20 handoff

```text
Run PR-20 — Create PR Implementation Plan — 091426.1
https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204

Receiver: dedicated HDE-EPIC040-PR06a PR-development session
(session_disposition: INITIAL_DEDICATED_ASSIGNMENT; role_session_ref: NOT_YET_ASSIGNED).

Inputs:
- docs/ephemeral/HDE-EPIC040-PR06a-pr-instruction-v1.0.md — PR06a instruction v1.0, INSTRUCTION_READY
- docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md — operative overlay (PF10 §2.23)
- docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md — PR07-F01 decision adding PR06a
- docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md — current PF10
- docs/ephemeral/HDE-EPIC040-PR06-pr-work-unit-lineage-review-v1.0.md — PR06 ACCEPTED_FINAL review

Issue the PR06a implementation plan in state AWAITING_PO_PROCEED. Findings outside the owned loci go to the whole-change IA and return to this session.
```
