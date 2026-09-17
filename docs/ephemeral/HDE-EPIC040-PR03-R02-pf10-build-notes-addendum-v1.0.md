---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
artifact_id: HDE-EPIC040-PR03-R02-PF10-BUILD-NOTES-ADDENDUM
artifact_version: v1.0
status: READY_FOR_MANUAL_DRAIN
canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN
drain_owner: Nathan / Product Owner
approved_by: HDE-EPIC040-PR03-RESCOPE-REVIEW-01 v1.0
approved_decision: APPROVE
immutable_base: HDE-EPIC040-IMPLEMENTATION-PLAN v2.1
current_pf10_at_authoring: PF10-HDE-Build-Notes-v13.2.4.md
page_ready_heading: 2.12
transport_metadata_excluded_from_pf10_body: true
---

## 2.12 HDE-EPIC040-PR03-R02 — Bind Executing Mechanics to the Admitted Release

### Status and authority

`HDE-EPIC040-PR03-RESCOPE-REVIEW-01 v1.0` approves a bounded PR03 implementation overlay for finding `PR03-R02` against the immutable HDE-EPIC040 Specification v1.1, Implementation Plan v2.1, approving Plan Review v2.1, PR03 Instruction v1.0, and PR03 Detailed Implementation Plan v1.0.

The original Product Owner Proceed for the PR03 detailed Plan remains valid. The overlay does not replace or revise an approved base, create another Proceed, reopen accepted PR01 or PR02, or authorize implementation beyond the stated delta.

### Evidence-supported defect

The accepted PR02 admission owner passively compares actual top-level execution code with compilation of captured, manifest-bound source for four existing modules. PR03 activates four additional mechanics modules that are members of the effective complete synthetic release roster but are not included in that executable-equivalence comparison:

- `engine/core/core.py`
- `engine/magic10/composite.py`
- `engine/magic10/signals.py`
- `engine/magic10/calculators.py`

An independently reproduced synthetic complete-release case changes `engine/magic10/signals.py` from addition to subtraction after the module has been imported, compiles the changed source, and coherently regenerates the manifest and release identity. Admission succeeds, but computation continues to execute the already imported addition implementation and labels the unchanged result with the altered release ID. The executing source SHA-256 is `c1d3829c21934452ed1a34b7ba32d8f84664033730f1ec0ebdea354d24f2c690`; the altered source SHA-256 is `fa51ef85f2cc711fee24a58139214945214bc3a6630ed14d648279808cae232c`.

This proves a bounded release-to-execution attribution failure. It does not establish a production incident, actual release promotion, vendor/database exposure, historical imported-byte identity, universal runtime integrity, or arbitrary in-process tamper resistance.

### Approved bounded overlay

The existing private admission execution-provenance and executable-equivalence owner in `engine/config/registry_loader.py` covers the four newly active PR03 mechanics modules in addition to its four accepted PR02 owners.

For each covered module, admission:

- retains actual top-level execution code and compatible interpreter optimization/cache semantics;
- establishes the existing safe common source origin;
- passively compiles the exact captured, manifest-bound source bytes without executing or importing those bytes;
- compares that compiled top-level code with the actual retained execution code; and
- refuses before returning an admitted bundle when provenance is unavailable or partial, origin is unsafe, compilation semantics are incompatible, source is not captured and manifest-bound, captured source cannot compile, or executable code is not equivalent.

The additional mechanics modules retain only the private passive execution provenance required by the existing admission owner. They do not load files, compile captured source, reload modules, select configuration, validate schemas, or become independent admission authorities.

### Bounded implementation and test loci

Production changes are limited to:

- `engine/config/registry_loader.py`
- `engine/core/core.py`
- `engine/magic10/composite.py`
- `engine/magic10/signals.py`
- `engine/magic10/calculators.py`

Focused test changes are limited to:

- `tests/config/test_production_admission.py`
- `tests/core/test_engine_core_determinism.py`
- `tests/core/test_engine_core_purity.py`
- `tests/config/helpers.py` only where the existing synthetic complete-release fixture owner requires a bounded adaptation

Existing core evidence is regenerated only when affected source identities require it, through `tools/evidence/generate_engine_core_evidence.py` and the already governed companion owner `tools/evidence/update_evidence_index.py`. The overlay creates no new evidence family, schema, writer, loader, serializer, calculator, or public surface.

### Requirements and acceptance effects

The approved overlay does not rewrite a Specification requirement or acceptance criterion. It strengthens the existing implementation and proof for:

- `K040-REQ-006` and `AC040-03`: one authoritative manifest-bound mechanics configuration cannot label execution by non-equivalent covered code;
- `K040-REQ-007`, `K040-REQ-008`, and `AC040-04`: the external loader/admission owner fails closed for executing/captured mechanics incoherence without moving I/O or compilation into core;
- `K040-REQ-009` and `AC040-05`: configuration, source, manifest/release, execution, and repository identities remain distinct and truthfully attributable;
- `K040-REQ-011`, `K040-REQ-012`, and `AC040-08`: adverse executable-equivalence tests and any affected governed evidence run through existing owners; and
- `K040-REQ-013` and `AC040-09`: request, decision, source, commit, review, CI, and release identities remain exact and separate.

The mathematics, taxonomy, signal/category roster and order, profiles, operations, weights, caps, thresholds, band boundaries, schemas, result fields, fingerprint preimage, pair preimage, serializer, and four-argument entrypoint remain unchanged.

### Required completion evidence

PR03 completion requires:

1. refusal of a syntax-valid semantic source change in each newly covered mechanics module after coherent fixture manifest/release regeneration;
2. refusal after post-import source replacement and for unavailable or partial provenance, unsafe origin, incompatible compilation semantics, and captured compilation failure;
3. successful admission for equivalent executing/captured source through the supported fixture-root path with safe module initialization;
4. proof that captured source is not executed and modules are not dynamically reloaded;
5. preservation of core import and compute purity, fixed G004 values, all accepted mathematics, identity, immutability, malformed-input, threshold-refusal, PR02 admission, and incomplete-actual-release tests;
6. focused local validation followed by complete applicable regression and governed writer/check execution, with exact attributable results and no aggregation of overlapping counts;
7. substantive corrected-source code review, applicable security review, and explicit repository disposition of PR03-R02; and
8. one final exact-head hosted CI run after applicable review defects are resolved.

Historical local tests, reviews, CI #3568, and CI #3569 remain evidence for their exact pre-correction heads. They do not prove the unimplemented correction or confer merge readiness.

### Release, dependency, and status effects

The effective synthetic complete-release roster remains exactly 44 members because all four mechanics sources are already members. The actual repository manifest remains exactly 15 members and incomplete. PR03 does not refresh, promote, or activate it.

PR01 / #403 and PR02 / #404 remain accepted and final. PR03 / #405 remains suspended at `RESCOPE_PENDING` until the approved overlay is available in the controlled Build Notes, then resumes in the same engineering session, worktree, branch, and PR under the original Proceed.

PR04 and PR05 retain their existing scopes and must consume the corrected accepted PR03 dependency. PR06 retains sole ownership of final actual 44-member materialization, complete release-identity convergence, and promotion. PR07 and OPS01 remain later unchanged work. The ordered dependency chain remains PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01.

### Preserved exclusions and limitations

The overlay does not authorize:

- changes to approved mathematics, taxonomy, mechanics data, thresholds, schemas, result or identity formulas;
- source reads, compilation, imports, reloads, configuration loading, file/network/database/vendor/environment/time/randomness/process access, or mutable cache behavior inside pure computation;
- a new public/API/CLI field, selector, failure taxonomy, hidden bypass, duplicate owner, alternate calculator, remote schema, persistent cache, application behavior, transport, narrative, deployment protocol, or evidence family;
- stronger multi-file atomic visibility, cross-process locking, immutable deployment infrastructure, historical imported-source byte identity, universal runtime integrity, or arbitrary in-process tamper-resistance claims;
- changes to or promotion of the actual 15-member incomplete release;
- PR04–PR07 or OPS01 implementation, independent QA/Ops, deployment, release activation, permanent Canon maintenance, or Epic closure; or
- a replacement branch, PR, worktree, session, instruction, Plan, Proceed, accepted-work rerun, or agent merge.

### Canon-conflict continuity

`C040-01` through `C040-04` remain `CANON_RECONCILIATION / APPROVED` by Thoth-17 at `2026-09-08T13:23:24Z`. `C040-05` remains `CANON_RECONCILIATION / APPROVED`, alternative A, by Isis-49 at `2026-09-09T03:57:16Z`. `C040-06` remains `NEW_CANON / APPROVED`, alternative A, by Isis-50 at `2026-09-09T11:48:08Z`.

Their decided substance, source lineage, risks, interim treatments, and permanent maintenance owners remain unchanged. PR02 F01/F02/F03 remain approved and drained only for PR02. PR03-R02 is a separate bounded overlay and does not reopen, reinterpret, or expand those decisions.

### Resulting state

The approved PR03-R02 overlay is the controlling in-flight exception to PR03 Instruction v1.0 §7.3 and Detailed Implementation Plan v1.0 §14 for exactly the stated admission/executable-equivalence coverage. All other approved bases and constraints remain immutable.

The repository correction, focused tests, affected evidence convergence, corrected-source review, PR03-R02 disposition, and final exact-head CI remain incomplete. PR #405 is open, non-draft, and unmerged at head `b33c41721ad2320f71c2cdaf00616e27d36945da`, tree `4af351d6f7347541b9853927bf5098299adcc81f`. Merge readiness, work-unit acceptance, QA, Ops, release activation, and Epic closure are not established.
