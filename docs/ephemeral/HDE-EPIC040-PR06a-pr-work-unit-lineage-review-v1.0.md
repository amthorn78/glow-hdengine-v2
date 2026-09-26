---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-EPIC040-PR06a-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: ACCEPT
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06a
reviewer: retained whole-change HDE-EPIC040 Implementation Architect, read-only PR-40 role
capture_time_utc: 2026-09-26T12:28:59Z
return_owner: the same retained whole-change HDE-EPIC040 Implementation Architect
---

# HDE-EPIC040-PR06a — PR Work-Unit Lineage Review v1.0

## 1. Decision

**decision: ACCEPT.** `HDE-EPIC040-PR06a` is accepted as delivered and is now `ACCEPTED_FINAL`. It delivered Reader v2 full Magic-10 on `POST /api/reader`, Reader v1 F05 conformance, the F03 production route, the F07 dev conjunction capture, and the 45-member release `1.2.0`.

Four limitations qualify the acceptance, and none of them is waived:
- **CR-02 / C040-08:** real Reader v1 error bytes fail the published v1 schema. This predates PR06a and was outside its authority. I decide it separately in `docs/ephemeral/HDE-EPIC040-PR06b-rescope-decision-v1.0.md`, which adds PR06b.
- **CR-03 / O-P06a-22:** two factories answer unknown paths with Flask's HTML 404. This predates PR06a; it goes to the HTTP transport / PF05 owner and is non-gating.
- **The Security Review does not cover the IF-08 delta.** Codex's Security Review ran on `402db72` with no finding. Only a Code Review covered head `1b4a510`, which contains the IF-08 corrective delta (a 405 guard).
- **CR-01 / O-12 (from PR06):** a packaged wheel install does not admit the release. This stays open with the packaging owner / Product Owner.

This decision grants none of the following: a QA verdict, acceptance, OPS01 attestation, activation, deployment, PF09 movement, a PF10 edit, or closure.

**Entry route.** The review entered on `MERGE_OBSERVED`. I verified the merge independently (§2). Result v1.1's `MERGE_PENDING` stays as pre-merge history.

## 2. Merge and attribution — verified

| Fact | Value |
| --- | --- |
| PR | [#508](https://github.com/amthorn78/glow-hdengine-v2/pull/508), the only PR in this unit. Merged by amthorn78 at 2026-09-26T12:20:15Z |
| Landed commit | `d79cfc1c398eb83934aa30653c7779a7bf9f3e69`, a squash commit whose sole parent is `cf9198d` (#506) |
| Reviewed head | `1b4a510517de5676530dc49727992164d5e3e9dc`, whose base was `547dc5b` |
| Tree comparison | `git diff 1b4a510 d79cfc1` shows exactly one file: `docs/ephemeral/HDE-EPIC040-PR06a-pr-instruction-v1.0.md`, which is #506's content and landed on `main` independently. The landed tree is therefore the reviewed head plus #506, so attribution is by tree |
| Scope | 135 files, +2,592 / −465 |
| Later divergence | None. `main` = `d79cfc1` |
| CI on the reviewed head | `test` passed: run `36222478818`, job `108350204251`, 06:01–06:16Z (read through the API) |

## 3. Behaviour executed at the landed tree

Everything below ran under closed rails, and the working tree was clean afterward.

- `catalog/manifest.json` has **45 members**, version **1.2.0**, and `built_at_utc` 2026-08-24T18:04:49Z. Its bytes are canonical. `release_id` is `9f962ce338c448c7a2312f05695d5fdab12b01fbc1a67d490465d9fc87edab3f`. `release_id_recompute.py --check-manifest-only` exits 0.
- `load_active_mechanics_bundle()` returns `AdmittedMechanicsBundle`.
- `generate_config_artifacts.py --compare-goldens .` reports `ok: true` with no mismatches.
- `run_canonical_json_gate.py --check-only` and `update_evidence_index.py --check` both exit 0.
- The mounted Reader routes are:
  - `POST /api/reader`;
  - the governed 405 for GET, PUT, PATCH and DELETE on `/api/reader`;
  - dev `GET /reader`;
  - `POST /reader`, which is a 405 stub.
- Version selection: a missing `v`, `v=3` and `v=1&v=2` each return 400 `ERR_READER_INVALID_VERSION`.
- Goldens:
  - `goldens/reader/v2/` holds ineligible, AB/BA, ten-in-order and invalid-version cases.
  - `goldens/reader/v1/` now uses harmony identities (`g03`–`g05`, `g07`). The `*_leader` files are gone.
- Focused suites: the Reader v1/v2 POST tests, `tests/reader_v1`, the endpoint catalog, dev conjunction identity and production admission gave **351 passed, 1 failed**. The failure is `tests/reader_v1/test_cli_proof.py`, and it fails identically at the pre-merge base `cf9198d`. It is pre-existing: plan D-18 and O-P06a-03 record it, and `scripts/hd_cli.py` is a legacy stub that still emits `open_leader`. It is not attributable to PR06a.
- **C040-08 reproduced.** `POST /api/reader?v=1` with body `{}` returns 422 `{"code":"ERR_READER_INVALID_INPUT","error":…,"ok":false,"schema":"v1"}`. Those bytes **fail** `schemas/reader.v1.schema.json`. The same bytes validate against `schemas/reader.v2.schema.json`.

## 4. Conformance to the approved scope and overlay (PF10 §2.23)

- **Deliveries 1–5 are present.**
  - Change to `engine/config/registry_loader.py` is limited to the roster (+`schemas/reader.v2.schema.json`), the invariant (45) and the version (`1.2.0`). The admission logic is unchanged.
  - The manifest was cut by the cutter.
  - Evidence was regenerated by its owners.
- **Paths outside the listed loci:**
  - `tools/evidence/generate_a7_transport_proofs.py` and `generate_open_rails_abba_proof.py`, plus the `tests/config/*`, `tests/scripts/*` and `tests/transport/*` rewrites, are coherence dependents of the re-cut and the route, as with PR06 under plan v2.1 §6.2.
  - `scripts/make_reader_v1_goldens.py` and `scripts/make_release_pack.sh` are the goldens' owning writers.

  I find no unauthorised widening.
- **Nothing changed** in Magic-10 math, the attestation schema, `PR06R_B_FINAL_PASS`, or `docs/pfcanon/`.
- **Reader v1 is not retired.** `v=1` is live on `/api/reader`, as §2.23 requires. Only the `*_leader` category identities were retired.

## 5. Findings and carried items

- **C040-08 (CR-02, O-P06a-24):** decided **alternative A** in the PR06b rescope decision.
- **O-P06a-22 (CR-03):** HTTP transport / PF05 owner. Non-gating.
- **O-P06a-23 (IF-09):** the engine-core evidence currency test does not check `release_id`. This is carried to the evidence owner, and PR06b's re-cut must run the engine-core owner.
- **O-P06a-03:** `scripts/hd_cli.py` / `test_cli_proof.py` baseline failure. Its owner is PR07 / the IA backlog. Non-gating.
- **N-01 (Nathan, non-gating):** stale PF10 v13.3 through v13.3.3 files are still beside v13.3.4.

## 6. Register and provenance

- **`CANON_CONFLICT_REGISTER`:**
  - C040-01 through C040-06 are unchanged.
  - C040-07 was delivered by PR06a; its drainage is pending with its maintainers.
  - C040-08 is decided in the PR06b decision.
- **Prompt use:** `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06a-01`, PR-40 — Review PR Work-Unit Lineage — 091426.1, on GCFPE-20260914.1 / 091426.1 / 55. Repository persistence is `PENDING / NON_GATING`.
- **PF10 read:** v13.3.4 (`0029e282…`).

## 7. Native return

`HDE-EPIC040-PR06a` is `ACCEPTED_FINAL`. The dependency order becomes `… → PR06a → PR06b → PR07 → OPS01`. The next stage is PR-10 for **PR06b**.
