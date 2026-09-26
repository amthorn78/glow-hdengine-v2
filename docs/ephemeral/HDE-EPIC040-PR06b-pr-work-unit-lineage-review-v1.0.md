---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-EPIC040-PR06b-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: ACCEPT
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06b
reviewer: retained whole-change HDE-EPIC040 Implementation Architect, read-only PR-40 role
capture_time_utc: 2026-09-26T17:45:00Z
return_owner: the same retained whole-change HDE-EPIC040 Implementation Architect
---

# HDE-EPIC040-PR06b — PR Work-Unit Lineage Review v1.0

## 1. Decision

**decision: ACCEPT.** `HDE-EPIC040-PR06b` is accepted as delivered and is now `ACCEPTED_FINAL`.

- **Delivered:** the Reader v1 error branch now matches the emitted envelope (C040-08, alternative A), and the release is re-cut to `1.3.0` with 45 members.
- **Scope of the decision:** it grants no QA verdict, acceptance, OPS01 attestation, activation, deployment, PF09 movement, PF10 edit or closure.
- **Entry route:** `MERGE_OBSERVED`. I verified the merge independently (§2). Result v1.4's `MERGE_PENDING` stays as pre-merge history.

## 2. Merge and attribution — verified

| Fact | Value |
| --- | --- |
| PR | [#513](https://github.com/amthorn78/glow-hdengine-v2/pull/513), the only PR in this work unit |
| Landed commit | `8999bd0`, committed 2026-09-26T17:24:49Z. A squash merge with sole parent `d031f94` (#512) |
| Reviewed head | `8855843bd65724e711f87526491270fda4b55b04`, read from `refs/pull/513/head` |
| Tree equality | Head and landed commit share tree `dae5491c057d82c48edf4e1fa4ae724147dbbfd9`, so attribution is by tree |
| Scope | 90 files, +1,822 / −11,675 |
| Scope note | Most of the deletions are the Product Owner-directed PF10 file operations (result v1.2 and v1.3). They added v13.3.6 and removed v13.3 through v13.3.4. These operations are recorded as PO actions, not PR06b deliveries. `docs/pfcanon/` now holds only `PF10-HDE-Build-Notes-v13.3.6.md` (SHA-256 `cc20d134…e6`). N-01 is closed |
| Later divergence | None. `main` = `8999bd0` |
| CI on the reviewed head | `test` passed: run `36257377433`, 16:59–17:11Z, read through the API. `main`'s post-merge push run was not read |

## 3. Behaviour executed at the landed tree

All runs were under closed rails, and the tree was clean afterward.

**Release and evidence**
- `catalog/manifest.json` has **45 members**, version **1.3.0**, `built_at_utc` 2026-08-24T18:04:49Z, and canonical bytes. Its `release_id` is `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`.
- The recompute exits 0 and admission returns `AdmittedMechanicsBundle`.
- Goldens compare `ok: true`. The canonical JSON gate and `update_evidence_index.py --check` both exit 0.

**Schema conformance: C040-08 is closed**
- The v1 error branch requires `schema`, `ok`, `code` and `error`. It has no `retry_after_ms`.
- Real errors from `POST /api/reader` validate against the v1 schema. I checked `v=1` with `{}` and with a non-JSON body, `v=2`, and a missing `v`. Dev `GET /reader` errors also validate.
- Four adverse envelopes are refused: missing `schema`, `schema:"v2"`, an ungoverned `code`, and an extra key.
- All v1 goldens validate. `g06` is now a real `ERR_READER_INVALID_INPUT` envelope.

**Bytes unchanged**
- Concatenated response bytes are identical at base `d031f94` and at `8999bd0`: SHA-256 `d5a1e732…f25a9`.
- The probe covered six error responses: four `POST /api/reader` variants, dev `GET /reader`, and `PUT /api/reader`.

**Focused suites**
- `tests/reader_v1`, the Reader POST v1/v2 tests and the pinned config homes gave **476 passed, 1 failed**. The one failure is the pre-existing `test_cli_proof.py` baseline failure (O-P06a-03), which does not come from PR06b.

## 4. Conformance to the approved scope (PF10 §2.25 in v13.3.6)

- The code diff outside records is inside the owned loci:
  - the schema, `g06`, the golden writer;
  - `registry_loader.py`, changed at `ADMITTED_RELEASE_VERSION` only;
  - the manifest, pinned tests and owner-regenerated evidence.
- `tools/evidence/generate_open_rails_abba_proof.py` changes only `FROZEN_OPEN_ABBA_SHA256`. That is a coherence dependent of the re-cut, as in the PR06a precedent.
- No change to the roster, admission logic, success branches, v2 schema, Magic-10, the attestation schema or `PR06R_B_FINAL_PASS`.

## 5. Findings and carried items

- **CR-01 / CR-02 (Codex).** The findings are that current-release captures carry origin-family Mirror labels. They were dispositioned as a class and not changed (result v1.4 §3). I concur: the regeneration is owner-run and approved, and a provenance-model change belongs to the evidence owner. This stays open as **O-P06b-17**, carried to the evidence/updater owner and non-gating.
- **Security Review** ran on `acae4c6` with no finding. PR-35 landed no later code correction.
- **Carried, unchanged:**
  - O-P06a-22 (HTML 404), to the HTTP transport owner;
  - O-12 (wheel packaging), to the packaging owner or PO;
  - O-P06a-03 (`hd_cli.py`);
  - O-P06a-23 (engine-core currency test).
- **Canon drainage** of C040-08 into PF01 §2.3 and PF04 §8.1.2 is pending with their maintainers and is non-gating.

## 6. Register and provenance

- **`CANON_CONFLICT_REGISTER`:**
  - C040-01 through C040-07 are unchanged.
  - C040-08 is decided A and delivered in the repository; its drainage is pending.
- **Prompt use:** `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06b-01`, from PR-40 — Review PR Work-Unit Lineage — 091426.1, on GCFPE-20260914.1 / 091426.1 / 55. Repository persistence: `PENDING / NON_GATING`.
- **PF10 read:** v13.3.6 (`cc20d134…`).

## 7. Native return

`HDE-EPIC040-PR06b` is `ACCEPTED_FINAL`. The next unit is **PR07**, the documentation-only DOC-10, and its PR-10 stage may begin. PR07 documents Reader v2, `/api/reader` and the v1 schema as PR06a and PR06b delivered them. After PR07 comes **OPS01**, which verifies the `1.3.0` release (`52be4558…`).
