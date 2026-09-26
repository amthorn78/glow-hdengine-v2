---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-EPIC040-PR06b
decision_id: HDE-EPIC040-PR06b-RESCOPE-DECISION v1.0 (APPROVE, alternative A)
immutable_base: HDE-EPIC040-IMPLEMENTATION-PLAN v2.1 (SHA-256 10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be) + PF10 §2.23
pf10_number: not allocated (Product Owner publication)
capture_time_utc: 2026-09-26T12:28:59Z
---

# HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08)

## Status and authority

This addendum is approved by the whole-change IA, by Product Owner direction, on 2026-09-26. The decision record is `docs/ephemeral/HDE-EPIC040-PR06b-rescope-decision-v1.0.md`. The bases are not rewritten.

## Objective

Make the published Reader v1 schema accept the Reader v1 error envelope the routes actually emit, per PF05 §5.2. Then bind the result with one release re-cut.

## Required delivery

1. **Schema.** In `schemas/reader.v1.schema.json`, the error branch admits `schema` (const `"v1"`, required, as the routes emit it) and restricts `code`/`error` to the governed token/message pairs, as `schemas/reader.v2.schema.json`'s error branch does. Optional integer `retry_after_ms ≥ 0` is kept only if a governed emitter produces it. The success branch is unchanged, and so is `additionalProperties: false`. The `.sha256` companion is regenerated.
2. **Goldens.** The synthetic `goldens/reader/v1/g06_error_invalid_input.json` (currently `{"code":"InvalidInput",…}` with no `schema`) is regenerated through `scripts/make_reader_v1_goldens.py` as a real governed v1 error envelope. Its companion and the release-pack outputs are regenerated through `scripts/make_release_pack.sh`.
3. **Release re-cut.**
   - The membership stays at 45 and the admission logic is unchanged.
   - In `engine/config/registry_loader.py`, only `ADMITTED_RELEASE_VERSION` changes, to `1.3.0`.
   - The manifest is cut through `scripts/cut_release_manifest.py`, and `release_id` is recomputed.
   - Config artifacts, the registry report, bundles and evidence (including the engine-core owner, per O-P06a-23) converge through their owning writers in PR06's generation order.
   - The strict attestation builds and verifies in the ordinary-CI release lane.

## Owned loci

- `schemas/reader.v1.schema.json` (+ `.sha256`)
- `goldens/reader/v1/g06_error_invalid_input.json` (+ `.sha256`), through its writer
- `scripts/make_reader_v1_goldens.py`, only where needed to emit the governed envelope
- `engine/config/registry_loader.py`, version constant only
- `catalog/manifest.json`, through the cutter only
- The existing test homes covering the changed seams: `tests/reader_v1/` (`test_schema.py`, `test_goldens.py`, `test_release_pack.py`), `tests/http/test_reader_post_v1.py`, and the release, manifest and config test homes that pin the version or `release_id`
- Governed evidence companions, through their owning writers only

A file that items 1–3 genuinely require but that falls outside these loci is a finding for the rescope route.

## Positive and adverse proof

- Every governed Reader v1 error response from `POST /api/reader?v=1` and dev `GET /reader` validates against the corrected v1 schema. Test this for every token in `ERROR_TOKEN_MAP` that the v1 routes can emit.
- The following are refused:
  - a v1 error with no `schema`;
  - a wrong `schema` const;
  - an ungoverned `code`;
  - an extra key.
- Every existing v1 success golden still validates. Reader v1 and v2 response bytes are unchanged, and so are the dev `GET /reader` bytes.
- Admission returns `ADMITTED` on the re-cut `1.3.0` release. The strict attestation passes on the exact candidate head.

## Exclusions

This addendum does not authorise any of the following:
- a change to Reader v1 or v2 response bytes, routes, the success branches, Magic-10, or the v2 schema;
- a roster membership change;
- an admission-logic change;
- a change to `hde.release_attestation.v1` or `PR06R_B_FINAL_PASS`;
- a PF-Canon edit;
- deployment or activation.

CR-03 and O-12 stay with their owners.

## Completion

Real code review, security review and ordinary CI pass on the exact candidate head, under PR-30 and PR-35. PR06b claims no QA verdict, acceptance, PF09 movement or closure.

## Work-unit effects

- The order becomes `PR01 → … → PR06 → PR06a → PR06b → PR07 → OPS01`.
- PR07 documents the v1 schema as PR06b delivers it.
- OPS01 requires all nine PR units and verifies the `1.3.0` release.

## Canon conflict

`C040-08` is decided A. PF01 §2.3 and PF04 §8.1.2 drainage belongs to their maintainers and is pending and non-gating. C040-01 through C040-07 are unchanged.
