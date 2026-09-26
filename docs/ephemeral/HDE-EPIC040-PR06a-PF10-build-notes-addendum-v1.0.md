---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
artifact_id: HDE-EPIC040-PR06a-PF10-BUILD-NOTES-ADDENDUM
artifact_version: "1.0"
addendum_id: HDE-EPIC040-PR07-F01 — Add PR06a for Reader v2 Full Magic-10 Exposure and the Deferred Reader Contract Work
status: READY_FOR_MANUAL_DRAIN
canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN
drain_owner: Nathan / Product Owner
page_ready_heading_number: NOT_ALLOCATED
observed_last_addendum_in_current_pf10_at_authoring: "2.22"
producing_context:
  route: GCF-17.RESCOPE — bounded work-unit rescope against the immutable base
  decision_owner: Isis-50 — continuing independent Lead Developer reviewer for HDE-EPIC040
  instruction: Product Owner direct instruction to the Isis-50 session, 2026-09-26
  input: the retained whole-change IA's PR07 scope analysis (options 1-3), relayed by the Product Owner in conversation; no RS-10 proposal artifact exists in the repository
  rs20_prompt: RS-20 — Review Bounded Work-Unit Rescope — 091426.1, https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204
product_owner_decisions:
  - "Option 1: add a bounded code unit, named HDE-EPIC040-PR06a, rather than widening PR07 or deferring beyond the Epic — delegated to Isis-50 and decided in this record"
  - "Public Reader exposes the full Magic-10 set — Nathan / Product Owner, 2026-09-26: 'we don't want to just emit harmony. This means PF01 needs a canon update' and 'we need full magic 10'"
approval_decision:
  id: HDE-EPIC040-PR07-F01-RESCOPE-DECISION
  version: "1.0"
  decision: APPROVE — option 1, unit HDE-EPIC040-PR06a
  decision_time_utc: 2026-09-26T02:55:39Z
  repository_path: docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md
immutable_base:
  id: HDE-EPIC040-IMPLEMENTATION-PLAN
  version: "2.1"
  sha256: 10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be
  repository_path: docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md
  approval_lineage: HDE-EPIC040 Implementation Plan Review v2.1, Isis-50 APPROVE 2026-09-09T13:36:43Z — docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md
  specification: HDE-EPIC040-SPECIFICATION v1.1, SHA-256 43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df — docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md
applicable_prior_addenda:
  - "PF10 §2.13 — docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md (dependency order, amended here)"
  - "PF10 §2.12 — docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md (admission boundary, preserved here)"
  - "PF10 §2.15 — docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md"
  - "PF10 §2.16 — docs/ephemeral/HDE-EPIC040-PR04-F03-deferral-decision-v1.0.md (return point reassigned here)"
  - "PF10 §2.17 — docs/ephemeral/HDE-EPIC040-PR04-F05-deferral-decision-v1.0.md (return point reassigned here)"
  - "PF10 §2.18 — docs/ephemeral/HDE-EPIC040-PR04-F07-deferral-decision-v1.0.md (return point reassigned here)"
  - "PF10 §2.21 — docs/ephemeral/HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md"
  - "PF10 §2.22 — docs/ephemeral/HDE-EPIC040-PR06-pr-work-unit-lineage-review-v1.0.md"
pf10_read_at_authoring:
  path: docs/pfcanon/PF10-HDE-Build-Notes-v13.3.3.md
  sha256: 6337d600e8555955f65cb68c0c29c485c6c42acb4c8c56765467b5ab70077b6a
canon_read_at_authoring:
  PF01: docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md — 101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a
  PF04: docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md — e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696
  PF05: docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md — a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e
  PF12: docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md — d7b2e0287da884fad6f4f79c69391099157c82e7ec0e78418581e1b873d21a1d
repository_baseline:
  main_head: 438269087934172ea0719e34375de3c8ad0ba999
  tree: ec30ccb6b930558e50457e2663b65ec09e3ce1c4
  admitted_release: 44 members, version 1.1.0, release_id 988ed2a7… (PR06, ACCEPTED_FINAL)
return_phase:
  pr_return_phase: NOT_APPLICABLE
  native_return_stage: PR-10 — Create PR Work-Unit Instructions — 091426.1, for HDE-EPIC040-PR06a
  native_return_owner: the retained whole-change HDE-EPIC040 Implementation Architect
  rs40_eligible: false
conflicts: "C040-07 — NEW_CANON, APPROVED by the Product Owner; see Canon decision and drainage"
transport_metadata_excluded_from_pf10_body: true
---

## 2.x HDE-EPIC040-PR07-F01 — Add PR06a for Reader v2 Full Magic-10 Exposure and the Deferred Reader Contract Work

### Status and authority

`HDE-EPIC040-PR07-F01-RESCOPE-DECISION v1.0` approves one bounded addition to the immutable HDE-EPIC040 Implementation Plan v2.1: a code work unit, **HDE-EPIC040-PR06a**, placed after PR06 and before PR07.

Two decisions stand behind it and are distinct. The Product Owner decides the product intent: the public Reader exposes the full Magic-10 set. The rescope decision owner decides the route: that intent, together with the Reader contract work deferred from PR04, is delivered by a new bounded code unit rather than by widening the documentation-only PR07 or by leaving it beyond the Epic.

The approved Specification v1.1, Implementation Audit v2.0, Implementation Plan v2.1 and Plan Review v2.1 remain immutable. This overlay does not rewrite them, create a Product Owner Proceed, reopen accepted-final PR01 through PR06, or authorize implementation beyond the stated unit. The overlays at PF10 §§2.12, 2.15 and 2.21 remain effective within their exact scopes.

### Cause

Implementation Plan v2.1 §6.7 defines HDE-EPIC040-PR07 as final repository documentation only. It forbids source behavior or contract changes presented as documentation, and it returns any newly found material code defect to change control.

Three findings from HDE-EPIC040-PR04 were deferred to PR07 by Product Owner decision, recorded at PF10 §§2.16, 2.17 and 2.18. Each requires code or public-contract change:

| Finding | Required change |
| --- | --- |
| `HDE-EPIC040-PR04-F03` | Serve the production Reader at the PF05 Required-Now route `POST /api/reader`, with its endpoint-catalog row and `/api` ingress scope |
| `HDE-EPIC040-PR04-F05` | Reconcile the published `schemas/reader.v1.schema.json` and `goldens/reader/v1/*` with the emitted Reader identities |
| `HDE-EPIC040-PR04-F07` | Restore the dev conjunction writer evidence capture: route identity, resolver seam, CI test-owner registration and artifact regeneration |

F03 and F05 change members of the admitted release manifest. PR06 admitted a forty-four-member release, so any correction requires a new manifest cut and a new `release_id`. F05 changes the public Reader contract, which is a protected external-contract boundary. None of this fits a documentation-only unit.

### Product Owner decision — full Magic-10 exposure

The public Reader exposes the full Magic-10 set: all ten canonical categories, bands only and numeric-free.

This decision reverses one explicit exclusion in the approved Specification v1.1: "No public ten-category expansion or numeric public result." For HDE-EPIC040, the ten-category clause of that exclusion is superseded by this Product Owner decision. The numeric clause is unchanged, and no public result carries a numeric.

The decision realizes the change current canon already anticipates. PF01 §2.2 records that "exposure of the full Magic-10 set is a future, versioned change". PF01 §5.1 records that public exposure of all ten categories "remains a future, versioned change". PF04 §15.2 carries it as open issue `OI-001 — Reader v2 planning (full Magic-10 exposure)`, which prescribes a versioned `reader.v2` public contract, requires Reader v1 to remain unchanged, and names PF01, PF05 and PF12 as the owning surfaces to update.

### Canon decision and drainage — `C040-07`

`C040-07` is a `NEW_CANON` decision, status `APPROVED` by the Product Owner on 2026-09-26. It discharges PF04 `OI-001`.

**Reader v2 contract.**

* Reader v2 is a versioned public contract, selected by `v=2` on the production Reader route `POST /api/reader`. Its request contract, read-only resolution, eligibility decision, transport, conditional and error behavior are those of the production Reader v1 route.
* The success body has exactly six keys: `reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`. `reader_version` is the fixed string `"v2"`. No other public field exists, and no field is numeric.
* When `eligible` is `true`, `categories` contains exactly ten items. Each is exactly `{ "id", "band" }` with `band` in `Cool`, `Open`, `Warm`, `Glow`. There is one item for each Magic-10 identifier, and the items appear in the canonical governed order of `catalog/magic10.json`: `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`. Each band is the band of that category in the complete canonical intrinsic Magic-10 result. No category is omitted, duplicated, default-filled, substituted by `harmony`, or altered by viewer preferences.
* In Reader v2, `categories` is an ordered array in canonical governed order and is not a set-sorted array.
* When `eligible` is `false`, `categories` is `[]`.
* Canonical JSON serialization, the five-key idempotence preimage recipe, AB↔BA identity and two-run identity apply to Reader v2 bytes exactly as they apply to Reader v1.

**Reader v1 is unchanged.** Reader v1 remains the bands-only, numeric-free, single-`harmony` contract of PF01 §2.2 and §4.7, selected by `v=1`. Correcting the checked-in `schemas/reader.v1.schema.json` so it conforms to that covenant is closure of an implementation gap already recorded at PF01 §2.1 and PF04 §8.1.3. It is not a v1 contract change.

**Required drainage.**

| Canon | Change | Owner |
| --- | --- | --- |
| PF01 — HDE Math Spec | Define the Reader v2 public projection alongside Reader v1 in §2. Resolve every "future, versioned change" statement to Reader v2, including §2.2, §5.1, the §1 map and the preset and pack-change statements. State the Reader v2 preimage, and emission rules per version in §4.4 and §4.7. Keep every Reader v1 statement true. | Governed PF01 maintainer |
| PF04 — HDE Governance | Add the Reader v2 exposure rule to §8.1, and move `OI-001` from `OPEN` to decided, closing it on PR06a delivery. | Governed PF04 maintainer |
| PF05 — HDE CLI-API-Vendor Ref | Admit `v=2` for the production Reader, which today refuses it. Define the v2 production projection in §5.1, add §5.6 endpoint-catalog rows, and give v2 examples. | Governed PF05 maintainer |
| PF12 — HDE Schemas and Artifacts | Register `schemas/reader.v2.schema.json` as a governed schema and release member in the Reader row. Record the forty-five-member roster and the re-cut release version. | Governed PF12 maintainer |

**Consequential drainage.** PF14 and PF29 each gain a Reader v2 statement. Their existing Reader v1 statements remain true, and so do those in PF04 §8.1.2 and PF09.4.

### Approved bounded overlay — HDE-EPIC040-PR06a

#### Objective

Deliver the public Reader contract that current canon and the Product Owner decision define: full Magic-10 exposure through Reader v2, Reader v1 conformed to its unchanged covenant, the production Reader at its PF05 route, the dev conjunction evidence capture restored, and one release re-cut binding the result.

#### Inputs and dependencies

Accepted-final PR01 through PR06, including the admitted forty-four-member release at version `1.1.0`. `C040-07`. The deferral records at PF10 §§2.16, 2.17 and 2.18, whose return point this overlay reassigns from PR07 to PR06a. Current controlled PF01, PF04, PF05 and PF12.

#### Required delivery

1. **Reader v2.** A new `schemas/reader.v2.schema.json` expresses the Reader v2 contract exactly. The existing Reader runtime and its single emitter project the ten-item result from the complete canonical intrinsic matrix, with no new presenter module and no second calculator. `v=2` is selected on the production route. New goldens under `goldens/reader/v2/` pin eligible, ineligible, AB↔BA and error cases.
2. **Reader v1 conformance (F05).** `schemas/reader.v1.schema.json` conforms to the unchanged v1 covenant: the category identifier is `harmony` only, `prompt` is removed, and the success branch enforces the exact six-key closure. `goldens/reader/v1/*` are reconciled to that covenant through their owning writer, and the retired `*_leader` identities leave the published contract.
3. **Production route (F03).** The production Reader is served at `POST /api/reader` for `v=1` and `v=2`, by the mechanism consistent with PF05 §5.6 and its alias posture. The dev `GET /reader` surface stays at its PF05 canonical path and remains Reader v1. `docs/ENDPOINTS_CATALOG.json` and its audit mirror gain the production rows, including the `POST` success row owed as observation O-03. The production route falls inside `/api`-scoped ingress policy. PR04 plan observation O-13 is superseded.
4. **Dev conjunction evidence (F07).** The dev conjunction route carries the real admitted release identity and no dev identity stamp, as PF10 §2.12 and accepted PR04 behavior require. A dev-only resolver seam, absent by default, removes the live-vendor dependency. The generator's assertions track the real identity. `tools/evidence/generate_conjunction_writer_evidence.py` is registered in `_EVIDENCE_GENERATOR_TEST_OWNERS`, so its test becomes a changed-test target. The frozen writer artifacts are regenerated through their owner.
5. **Release re-cut.** `schemas/reader.v2.schema.json` is the one new release member, so the admitted roster becomes forty-five. `ADMITTED_RELEASE_ROSTER` and its count invariant in `engine/config/registry_loader.py` change in membership only, and the admitted version changes to `1.2.0`. The admission logic and the PF10 §2.12 boundary are unchanged. The manifest is cut through `scripts/cut_release_manifest.py`, and `release_id` is recomputed from the exact bytes. Configuration artifacts, the registry report, FE/BE bundles and evidence converge through their existing owning writers in PR06's generation order. The strict attestation builds and verifies in the ordinary-CI release lane.

#### Owned loci

* `adapter/http_reader.py`, `adapter/factory.py` and, only where the route mechanism requires it, `adapter/wsgi.py`.
* `engine/runtime/public.py` and `presenter/reader_v1/emitter.py`, and `engine/presenter/emitter.py` only where the existing emission path requires it.
* `schemas/reader.v1.schema.json` and the new `schemas/reader.v2.schema.json`, with their companions.
* `goldens/reader/v1/*` and the new `goldens/reader/v2/*`, with their companions.
* `docs/ENDPOINTS_CATALOG.json` and its audit mirror.
* `tools/evidence/generate_conjunction_writer_evidence.py` and its writer artifacts.
* `ci/checks/classify_ci_changes.py`, for registration only.
* `engine/config/registry_loader.py`, for the roster constant, count invariant and admitted version only.
* `catalog/manifest.json`, only through the canonical cutter.
* The existing Reader, HTTP, transport, runtime-identity, endpoint-catalog, release, manifest and evidence test homes covering the changed seams, including `tests/evidence/test_dev_conjunction_identity.py`.
* Governed evidence companions — Index and Mirror rows, path proofs, config artifacts, registry report and bundles — only through their existing owning writers.

These loci are bounded by purpose. The PR06a instruction resolves exact paths from the delivered tree. A file genuinely required for items 1 to 5 and outside these loci is a finding for the ordinary rescope route, not an implicit extension.

#### Positive and adverse proof

* A Reader v2 eligible pair yields exactly ten items in canonical order, each band equal to the complete canonical matrix. Pairs derived from G001–G008 prove this, and the bytes validate against the Reader v2 schema.
* A Reader v2 ineligible pair yields `[]`, and a valid complete self-pair takes the existing ineligible path.
* Reader v2 bytes hold AB↔BA identity and two-run identity, and the idempotence preimage recomputes.
* A Reader v1 success validates against the corrected v1 schema and carries exactly one `harmony` item.
* Version selection is strict. A missing, unsupported, duplicated or malformed `v` is refused as PF05 specifies.
* `POST /api/reader` serves both versions. The dev `GET /reader` bytes are unchanged, and endpoint-catalog rows match the mounted routes.
* No public body carries a numeric, a prompt, a narrative key, a score, a UUID or a Gate value.
* The dev conjunction capture runs with the real admitted identity and no vendor call, and its test runs in CI.
* Admission returns `ADMITTED` on the forty-five-member cut with a recomputed `release_id`, and a tampered, missing or extra member is refused.
* The strict attestation builds and verifies on the exact candidate head.

#### Exclusions

No change to Magic-10 mathematics, membership, order, weights, caps, bands or catalog data. No public numeric field. No narrative or prompt on any public surface. No new CLI flag: Reader↔CLI dump parity remains a Reader v1 family. No Reader v1 contract change. No change to the `hde.release_attestation.v1` success schema or to the `PR06R_B_FINAL_PASS` wire value. No change to admission logic. No release activation, promotion or deployment. No live vendor or database operation. No PF-Canon edit, since `C040-07` drainage belongs to its maintainers. PR06 is not rerun, and PR07's documentation is not absorbed.

#### Completion

Real integration paths and proofs pass actual code review, security review and ordinary CI, on the exact candidate head, under the PR-30 and PR-35 lifecycle, including the strict attestation. PR06a claims no QA verdict, acceptance, deployment, PF09 movement or closure.

### Work-unit, dependency and status effects

The whole-change dependency order fixed at PF10 §2.13 becomes:

`PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR06a → PR07 → OPS01`

**PR06a** is added as specified above.

**PR07** remains the documentation-only unit of Plan v2.1 §6.7, unchanged in boundary. It inherits none of F03, F05 or F07. Its required content adds the delivered Reader v2 contract, the `/api/reader` production route and the conformed Reader v1 schema, as PR06a actually delivers them. Its instruction stage begins after PR06a is accepted final.

**OPS01** requires all eight PR units — PR01 through PR06, PR06a and PR07 — to be complete. It verifies the re-cut forty-five-member release rather than the forty-four-member release.

PR01 through PR06 remain accepted final. PR06's admission of the forty-four-member release is historical and valid, and is superseded by PR06a's re-cut only as the current release.

### Requirements and acceptance effects

| Requirement or criterion | Effect |
| --- | --- |
| Specification v1.1 exclusion "No public ten-category expansion" | Superseded for HDE-EPIC040 by the Product Owner decision. The numeric-result exclusion stands. |
| Public full Magic-10 exposure | A new product requirement introduced by the Product Owner decision and delivered by PR06a. It carries no `K040-REQ` identifier, because Specification v1.1 does not contain it. |
| `K040-REQ-010` / `AC040-06` | PR06a owns the Reader v1 golden reconciliation and the Reader v2 goldens. The G001–G008 result goldens are unchanged. |
| `K040-REQ-012` / `AC040-08` | The re-cut release and its evidence converge through their existing owning writers. |

Every other requirement, criterion, allocation and completion burden is unchanged.

### Preserved exclusions and nonclaims

The overlay establishes no QA verdict, acceptance, PF09 movement, release activation, deployment, Product Owner closeout or Epic closure. It does not claim that any canon document has been drained or that PR06a is implemented. It confers no Proceed and no merge authority.

### Canon-conflict continuity

`CANON_CONFLICT_REGISTER` entries `C040-01` through `C040-06` are carried unchanged, with no entry reopened, relabeled, omitted or newly decided. `C040-07` is added as recorded above. `HDE-EPIC040-PR07-F01` itself is not a register entry.

### Unresolved items and owners

| Item | Owner | State |
| --- | --- | --- |
| Specification lineage — recording the superseded exclusion through the native Specification-delta route (CF-E-30) | Nathan / Product Owner, with the continuing Thoth Specification reviewer | Available; this overlay is the authoritative record for HDE-EPIC040 |
| `C040-07` drainage into PF01, PF04, PF05 and PF12, and the consequential PF14 and PF29 statements | Their governed maintainers | Pending; non-gating for PR06a |
| External consumers of the Reader v1 shape | PR06a engineering owner | None identified in the repository; a consumer found to depend on the retired `*_leader` identities returns to change control |
| Exact route mechanism for `/api/reader`, within PF05 §5.6 | PR06a instruction and detailed plan | Open design choice inside the bound |
| PF12 v2.9.5 against the register's recorded v2.9.6 | Governed PF12 maintainer | Carried; non-gating |

### Resulting state

`HDE-EPIC040-PR07-F01` is approved as a bounded rescope that adds HDE-EPIC040-PR06a. The next native stage is the PR06a work-unit instruction by the retained whole-change Implementation Architect. PR06a implementation awaits the Product Owner's separate exact `PR-30` invocation against a PR06a detailed plan in `AWAITING_PO_PROCEED`. That plan does not yet exist, and this overlay does not supply the Proceed.
