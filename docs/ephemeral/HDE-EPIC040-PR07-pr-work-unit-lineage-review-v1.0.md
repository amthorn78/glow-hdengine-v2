---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-EPIC040-PR07-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: ACCEPT
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR07
reviewer: retained whole-change HDE-EPIC040 Implementation Architect, read-only PR-40 role
capture_time_utc: 2026-09-26T22:50:15Z
return_owner: the same retained whole-change HDE-EPIC040 Implementation Architect
---

# HDE-EPIC040-PR07 — PR Work-Unit Lineage Review v1.0

## 1. Decision

**decision: ACCEPT.** `HDE-EPIC040-PR07` is accepted as delivered and is now `ACCEPTED_FINAL`. It delivered the final repository documentation (DOC-10, Plan v2.1 §6.7 as amended by the PR06a and PR06b addenda).

With PR07 accepted, **all eight PR units are complete**: PR01–PR06, PR06a, PR06b and PR07. The clean final candidate for OPS01 is `main` at `edbd414`.

This decision grants none of the following: QA, acceptance, OPS01 attestation, activation, deployment, PF09 movement, a PF10 edit, or closure.

**Entry.** The review was entered on `MERGE_OBSERVED`. I verified the merge independently (§2). Result v1.1's `MERGE_PENDING` stays as history.

## 2. Merge and attribution — verified

| Fact | Value |
| --- | --- |
| PR | [#518](https://github.com/amthorn78/glow-hdengine-v2/pull/518), the only PR in this unit |
| Landed commit | `edbd414`, committed 2026-09-26T22:47:07Z. A squash merge with sole parent `5a2b6a6` (#517) |
| Reviewed head | `111a0cad246b04f5e423178ef09dae4e16627ac1`, read from `refs/pull/518/head` |
| Tree equality | Head and landed commit share tree `f55b7041dc4f3651a14f965cc74b337cfc8d1d4b`, so attribution is by tree |
| Scope | 18 files, +979 / −27. Of these, 15 are documentation files (+203 / −27); the rest are PR07's `docs/ephemeral/` records |
| Scope detail | One new file, `docs/contracts/reader_v2_public_bytes.md` (the one new home the instruction allowed). There is no change outside `.md` files and `docs/` since PR06b's landed commit `8999bd0` |
| Later divergence | None. `main` = `edbd414` |
| CI on the reviewed head | `test` passed: run `36272965542`, 21:27:01–21:27:12Z, read through the API. The 11-second duration fits a docs-only change that selects no test lanes. I did not read the job log |

## 3. Verification at the landed tree

All of this was run under closed rails, and the tree was clean afterward.

**Behaviour.** No source changed, so there is no behaviour change. `release_id_recompute.py --check-manifest-only` and `update_evidence_index.py --check` both exit 0. The release is still `1.3.0`, 45 members, `release_id` `52be4558…`.

**Cited paths exist.** Every repository path cited in backticks on an added line exists in the tree. I checked this mechanically over the diff.

**Spot-checked claims against the code:**
- `ADMITTED_RELEASE_BUILT_AT_UTC` (`registry_loader.py:399`)
- `compute_core(member_a, member_b, mechanics_bundle, release_id)` (`engine/core/core.py:209`)
- `evaluate_pair` (`engine/compat/compute.py:307`)
- `--roster-from-admission` (cutter)
- `ERR_READER_FORBIDDEN` 403 (`adapter/http_reader.py:604`)
- `tools/bodygraph/check_magic10_gate_readiness.py` and `scripts/dev_start_reader.sh` exist
- the claim that `dev/reader_harness/app.py` fails at import with `AttributeError`, which I reproduced

All of these hold.

**Examples.** Every current JSON example in the Reader v1 and v2 contract pages validates against its schema. One v1 example fails: `{"compat":[…]}`. It is explicitly labelled a historical EPIC-004 shape that is "not the current body", which is acceptable as preserved history.

**Plan §6.5 correction.** The confirmed error is fixed. `docs/server/reader_v1.md` now states that production is `POST /api/reader?v=1|2`, that dev is `GET /reader`, and that `GET /api/reader` returns 405. A "Current state (HDE-EPIC040)" section marks older text as retained history.

**Non-claims.** `AGENTS.md` gains an HDE-EPIC040 posture section. It carries explicit non-claims (no QA, acceptance, OPS01, deployment or closure). It records C040-06, C040-07 and C040-08 drainage as pending, and it tells readers to cite addenda by heading because PF10 section numbers have shifted. All of this is accurate.

## 4. Conformance

- The unit is documentation only. There is no source, schema, golden, catalog, manifest, evidence or `docs/pfcanon/` change.
- The required content is present: the core, admission and cutter, the Reader v1 and v2 routes and contracts, the read-only tools, canon status, non-claims, and the carried HTML-404 limitation (O-P06a-22), which is described but not fixed.
- I found no false claim that anything was produced, passed QA, approved or drained.

## 5. Findings and carried items

No new finding. These items are carried unchanged to their owners:

| Item | Owner |
| --- | --- |
| O-P06a-22 | HTTP transport |
| O-12 | Packaging owner / Product Owner |
| O-P06a-03 | Its owner |
| O-P06a-23 | Evidence owner |
| O-P06b-17 | Evidence owner |
| O-P07-01 to O-P07-09 (result v1.0) | As recorded there |
| C040-06, C040-07, C040-08 drainage | Their PF-Canon maintainers |

**Stray branch.** The remote branch `claude/pr07-instruction` (commit `de1d6b1`), pushed in error during PR-10, may still exist. Its content landed via #514. Deleting it is Nathan's action.

## 6. Register and provenance

- **`CANON_CONFLICT_REGISTER`:** C040-01 to C040-08 are unchanged.
- **Prompt use:** `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR07-01`, PR-40 — Review PR Work-Unit Lineage — 091426.1, on GCFPE-20260914.1 / 091426.1 / 55. Repository persistence is `PENDING / NON_GATING`.
- **PF10 read:** `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md` (SHA-256 `af292883d5d4f27bd5cc510117e29b044ec2ac0b0f522df48fd0022010c6855c`).

## 7. Native return

`HDE-EPIC040-PR07` is `ACCEPTED_FINAL`. Every PR unit in the whole-change plan is complete.

The next unit is **OPS01**, per Plan v2.1 §6.8: final clean-candidate external verification of release `1.3.0` (`release_id` `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`) on the clean `main` candidate, using `tools/evidence/build_release_attestation.py` into an empty external directory. It requires its own action-specific Ops instruction and authority.
