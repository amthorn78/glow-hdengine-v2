# Redlines — PF09.4-Canon-HDE-Build-Checklist-Conjunction, from v1.2

Run: `gtwpe-20261009-pf10-v13-5 / T-PF09-4`. Preparation revision: `1`. Outcome: `READY` (producer validation passed; saved-package verification is recorded separately in the proof log).
Original: `docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.2.md` at `e7265a090ad0cc8de5f36de2f19481216aa3d073`; Git blob `5a97004918e15b5f5783869fd1d2de7d68b4df9f`; raw UTF-8 SHA-256 `441979071515ee95ea8ebb9d02cfc478768c1870d36a92b5bf5aa037a95b8cbb`; 96,003 bytes; LF-only; final LF preserved.
Originating preparer: Codex, this Nathan-started T-PF09-4 Work conversation; workspace /workspace/scratch/ef74eefe8666; stable platform conversation URL/ID not exposed.
Ledger: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md` at `f057d124176143b3e02ba7ad599880fd7e9991b1`; assigned row `T-PF09-4`.
Prompt: TW-DRAIN-20 100926.1 — https://app.notion.com/p/3f44590a05eb815ebfd2cf992bec9862.
Selected originals at the baseline: PF10-HDE-Build-Notes-v13.5.md A16–A18, A22–A24, A26, A30; HDE-EPIC040-specification-v1.1-approved.md S01–S02, S06, S11–S12; complete HDE-EPIC040-CL-E-10-closure-decision-v1.2.md C1. Exact source boundaries and dispositions are in the paired proof log.
Apply reserves the native header: v1.2 → v1.3; application execution date in YYYY-MM-DD; Last Update Gate from recorded change-source identities, in source order. Status remains Canon; invocation tag/title unchanged. No native change/revision-history entry exists or is required in this target.

## RL-001

Change type: Phase Master Update / Clarity Fix
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: S02, S06, C1; complete original task and subtask status lines
Rationale: Align the summary with its own detailed rows without changing the native phase master Not done or inferring a phase exit.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)**
Original scope heading: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
**Done:** Dev HTTP Harness (single home), Writer Surfaces (API), Global discipline

**Not done:** Compat Surface (internal), CLI Serializer Coupling, CLI Conformance, Reader Surface (API), Caching & Transport Wiring (Reader), CLI Tooling (showcompat, sample)
````
Replacement text (literal; delimiter newlines are not payload):
````text
**Done:** Dev HTTP Harness (single home), Compat Surface (internal), CLI Serializer Coupling, CLI Conformance, Reader Surface (API), Caching & Transport Wiring (Reader), CLI Tooling (showcompat, sample), Writer Surfaces (API), Global discipline

**Partial:** Full Magic10 deterministic scoring integration (HDE-CONJ010)

**Not done:** HDE-CONJ010.1, HDE-CONJ010.2, and HDE-CONJ010.5 remain open within the Partial integration task.
````

## RL-002

Change type: Clarity Fix
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A30
Rationale: Name the override source by title while retaining the exact EPIC029 bounded closure statement.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)**
Original scope heading: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
The controlling Conjunction subtasks for that close decision were `HDE-CONJ009.1`, `HDE-CONJ008.1`, and `HDE-CONJ001.4`, and the review states that PF10’s final in-epic close authority records all three as supportable for later drain to Done at epic close.
````
Replacement text (literal; delimiter newlines are not payload):
````text
The controlling Conjunction subtasks for that close decision were `HDE-CONJ009.1`, `HDE-CONJ008.1`, and `HDE-CONJ001.4`, and the review states that HDE Build Notes’ final in-epic close authority records all three as supportable for later drain to Done at epic close.
````

## RL-003

Change type: Clarity Fix / Epic-information Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24, A26, A30, S01, S02, S06, S11, S12, C1; supporting PF09.3 HDE-SEPA006
Rationale: Remove the brittle locator and record the approved overlay and controlling exceptional-closure qualifications without turning Separation delivery into Conjunction completion.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)**
Original scope heading: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
The remaining caveat is auditability rather than closure truth: PF10 2.21 uses evidence-basis prose rather than direct `Evidence pointer:` lines for the final row-closing decision. The review states that this gap is real but not enough to overturn the explicit live close authority.
````
Replacement text (literal; delimiter newlines are not payload):
````text
The remaining caveat is auditability rather than closure truth: HDE Build Notes uses evidence-basis prose rather than direct `Evidence pointer:` lines for the final row-closing decision. The review states that this gap is real but not enough to overturn the explicit live close authority.

**HDE-EPIC040 consequential integration:** Separation Pass 3 selects HDE-SEPA005 and its five subtasks. Its approved C040-07 overlay delivers Reader v2 and the adjacent Reader and dev conjunction corrections; this phase records their consequences only in the existing consumer and integration-proof rows. The approved Specification's twenty-nine Done/context exclusions remain excluded, and the overlay supersedes only the public ten-category exclusion. The public numeric, extra-surface, and independent-scoring exclusions remain effective.

The closure decision records HDE-EPIC040 as `CLOSE` / `CHANGE_CLOSED` by Product Owner-authorized exceptional closure on 2026-09-29. It records whole-change QA `PASS`, 12 of 12 checks, at tested source `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d`, with the two user-bound live observations environment-blocked. PR #559 resolved QA50-F01 by landing and registering the evidence of record; it did not rerun QA. Ordinary Close Gate completion, a close pack, release activation, deployment, board movement, and phase exit are not established by that closure.

HDE-CONJ010 remains Partial. Its unresolved full integration and proof obligations are assessed independently below; HDE-EPIC040 does not complete the Conjunction population or absorb HDE-SEPA006's separate chart-loader boundary migration. Existing historical EPIC026–EPIC029 evidence retains its original scope.
````

## RL-004

Change type: Clarity Fix
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A30
Rationale: Remove a current row-authority locator; preserve the drain label, EPIC identity, closure mode, environment evidence, and Done status.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ001 — Dev HTTP Harness (single home) > ### **Subtask HDE-CONJ001.4 — Dev/internal HTTP harness infra wiring**
Original scope heading: `### **Subtask HDE-CONJ001.4 — Dev/internal HTTP harness infra wiring**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
* **Status (Drain 10.5.7 — PF10 Addenda 2.20-2.21 HDE-EPIC029):** Done.  
````
Replacement text (literal; delimiter newlines are not payload):
````text
* **Status (Drain 10.5.7 — HDE-EPIC029):** Done.  
````

## RL-005

Change type: Task Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24, A26, S11, S12
Rationale: Expand the existing Reader consumer obligation to the delivered versioned projection without creating a second contract home or moving production POST into the dev A7 family.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ005 — Reader Surface (API)
Original scope heading: `## Task HDE-CONJ005 — Reader Surface (API)`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
Provide a six-key Reader v1 envelope on a Catalog JSON success route via the shared presenter/emitter, prove A7 transport invariants (200/HEAD/304, ETag, Vary, encoding invariance), maintain an Endpoint Catalog, and index proofs.
````
Replacement text (literal; delimiter newlines are not payload):
````text
Provide the production Reader v1 and Reader v2 projections through the shared presenter/emitter, maintain their production Endpoint Catalog entries, and index their governed proofs. Preserve the existing Reader v1 Catalog GET/HEAD/304 A7 proof family separately from non-conditional production POST behavior. The exact public wire contracts remain owned by PF05-Canon-HDE-CLI-API-Vendor-Ref and PF12-Canon-HDE-Schemas-and-Artifacts.
````

## RL-006

Change type: Notes Update / Evidence Update / Epic-information Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A16, A17, A18, A22, A23, A24, A26, S02, S06, S11, C1
Rationale: Replace stale deferral implications with delivered scope and current accepted release chronology, while retaining the recorded limits.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ005 — Reader Surface (API)
Original scope heading: `## Task HDE-CONJ005 — Reader Surface (API)`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
 Addendum 05-08 PR03 HDE-EPIC026 adds dev-only HTTP GET endpoints for conjunction preview (/dev/sampler/conjunction, /dev/reader/conjunction), gates them via APP\_ENV (dev/test/local), updates the endpoint catalog entries, adds minimal catalog and dev-gating tests, and regenerates endpoint-catalog checksum/path-proof sidecars after catalog byte changes.
````
Replacement text (literal; delimiter newlines are not payload):
````text
 Addendum 05-08 PR03 HDE-EPIC026 adds dev-only HTTP GET endpoints for conjunction preview (/dev/sampler/conjunction, /dev/reader/conjunction), gates them via APP\_ENV (dev/test/local), updates the endpoint catalog entries, adds minimal catalog and dev-gating tests, and regenerates endpoint-catalog checksum/path-proof sidecars after catalog byte changes.

**Accepted HDE-EPIC040 consumer delivery:** PR06a (#508) delivers Reader v2 on `POST /api/reader?v=2`, preserves Reader v1 on `POST /api/reader?v=1`, conforms the v1 success schema to the single-harmony covenant, and resolves PR04-F03, PR04-F05, and PR04-F07. PR06b (#513) resolves C040-08 by conforming the v1 error schema to emitted errors without changing response bytes. The earlier PR07 deferrals are historical; PR07 retains its documentation-only boundary.

Reader v2 exposes bands for all ten governed categories, with no public numerics, prompt, narrative key, or additional field. It does not add a CLI flag or change Reader v1 dump parity. The accepted PR06b release is `1.3.0`, 45 members, with release identity `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`; PR06's 44-member `1.1.0` and PR06a's 45-member `1.2.0` remain historical accepted cuts.

Done retains this row's implemented surface and bounded tested-evidence scope. It does not assert deployed reachability or live current-row DB success. The carried HTML-404 transport observation, wheel-distribution decision, legacy CLI proof failure, and evidence-owner currency/provenance observations remain with their recorded owners; they are not resolved by these notes.
````

## RL-007

Change type: Subtask Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24, S11, S12
Rationale: State the actual v1/v2 projection and ordered-array verification burden rather than leaving a v1-only example as the whole Reader requirement.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ005 — Reader Surface (API) > ### Subtask HDE-CONJ005.1 — Reader success body & canonical JSON
Original scope heading: `### Subtask HDE-CONJ005.1 — Reader success body & canonical JSON`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
 Ensure public success body is the six-key envelope:

{

"reader\_version": "v1",

"eligible": \<eligible\>,

"categories": \<categories\>,

"meta": \<meta\>,

"release\_id": \<release\_id\>,

"idempotence\_hash": \<idempotence\_hash\>

}

Emitted via the single presenter/emitter as canonical JSON: UTF-8 (no BOM); ASCII-sorted keys; compact; exactly one LF; arrays-as-sets deduped and ASCII-sorted; checks under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
````
Replacement text (literal; delimiter newlines are not payload):
````text
Enforce each version's governed six-key success envelope through the single presenter/emitter: `reader_version`, `eligible`, `categories`, `meta`, `release_id`, and `idempotence_hash`.

Reader v1 retains its unchanged numeric-free single-harmony covenant. Reader v2 uses `reader_version: "v2"`; an eligible pair exposes exactly one `{id, band}` item for each of the ten governed Magic-10 categories, in their canonical catalog order, with each band projected from the same complete intrinsic result. An ineligible pair exposes an empty categories array. Reader v2 categories is an ordered array, not an array-as-set; do not ASCII-sort it, omit or duplicate categories, fill defaults, substitute harmony, or apply viewer preferences.

Require canonical UTF-8 JSON with no BOM, ASCII-sorted object keys, compact separators, and exactly one trailing LF, under `LC_ALL=C`, `LANG=C`, and `TZ=UTC`. Apply the governed five-key idempotence preimage, AB/BA identity, and two-run identity to the versioned bytes. PF05-Canon-HDE-CLI-API-Vendor-Ref and PF12-Canon-HDE-Schemas-and-Artifacts own the exact shape and byte contracts.
````

## RL-008

Change type: Evidence Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24, A26, C1
Rationale: Keep older Reader v1 proof as history and add attributed later evidence rather than relabeling that earlier run as Reader v2 verification.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ005 — Reader Surface (API) > ### Subtask HDE-CONJ005.1 — Reader success body & canonical JSON
Original scope heading: `### Subtask HDE-CONJ005.1 — Reader success body & canonical JSON`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
Attempt 0 strengthens the six-key Reader success-body coverage in `tests/http/test_reader_a7_transport.py`, and the final PR-02 lifecycle preserves that runtime/test slice while the targeted Reader pytest subset is recorded as passing.
````
Replacement text (literal; delimiter newlines are not payload):
````text
Attempt 0 strengthens the six-key Reader success-body coverage in `tests/http/test_reader_a7_transport.py`, and the final PR-02 lifecycle preserves that runtime/test slice while the targeted Reader pytest subset is recorded as passing.

**Accepted HDE-EPIC040 evidence:** PR06a records v1/v2 production POST coverage and owner-generated goldens under `goldens/reader/v1/` and `goldens/reader/v2/`; the v2 family includes eligible, ineligible, AB/BA, ten-in-order, and invalid-version cases. PR06b records schema-valid v1 errors and unchanged emitted response bytes. The exceptional closure accepts the tested scope with live DB Reader success still environment-blocked; no deployed or current-row success is inferred.
````

## RL-009

Change type: Subtask Update / Evidence Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A16, A23, A24, S12
Rationale: Use the actual existing Endpoint Catalog row to own route consequences; preserve the separate dev/proof route and refuse a new proof-surface inference.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ005 — Reader Surface (API) > ### **Subtask HDE-CONJ005.2 — Endpoint Catalog & env-gates**
Original scope heading: `### **Subtask HDE-CONJ005.2 — Endpoint Catalog & env-gates**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
 Maintain `docs/ENDPOINTS_CATALOG.json` as the canonical, machine-readable inventory of HTTP endpoints in the repo, and within that inventory clearly identify which endpoints are JSON success routes eligible for A7 proofs. Entries are titles-only; bytes/examples and detailed contract semantics remain routed to their single homes by title only.
````
Replacement text (literal; delimiter newlines are not payload):
````text
 Maintain `docs/ENDPOINTS_CATALOG.json` as the canonical, machine-readable inventory of HTTP endpoints in the repo, and within that inventory clearly identify which endpoints are JSON success routes eligible for A7 proofs. Entries are titles-only; bytes/examples and detailed contract semantics remain routed to their single homes by title only.

Track production `POST /api/reader` for both `v=1` and `v=2` and preserve the dev Reader v1 GET/proof surface at `/reader`. The production catalog rows and audit mirror must match the mounted route and `/api` ingress scope. Keep the production route, its governed method refusal, and version selection distinct from the dev GET/HEAD proof family; do not treat a dev route or a declaration alone as deployed production reachability. PR06a delivers the former F03 route gap and O-03 POST catalog obligation.
````

## RL-010

Change type: Clarity Fix
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A30
Rationale: Remove the named internal locator while preserving EPIC028 scope, the historical artifact facts, and the proof-surface distinction.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ005 — Reader Surface (API) > ### **Subtask HDE-CONJ005.2 — Endpoint Catalog & env-gates**
Original scope heading: `### **Subtask HDE-CONJ005.2 — Endpoint Catalog & env-gates**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
Current-state QA records `/reader` as the governed Reader success-proof surface for the current HDE-EPIC028 scope under the active PF10 addendum 2.14 interpretation, with the deciding lookup artifact showing `a7_eligible:true`, `env_gate:"APP_ENV=dev"`, and route ownership evidence from `adapter/http_reader.py`.
````
Replacement text (literal; delimiter newlines are not payload):
````text
Current-state QA records `/reader` as the governed Reader success-proof surface for the current HDE-EPIC028 scope under the HDE Build Notes interpretation, with the deciding lookup artifact showing `a7_eligible:true`, `env_gate:"APP_ENV=dev"`, and route ownership evidence from `adapter/http_reader.py`.
````

## RL-011

Change type: Subtask Update / Clarity Fix
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24
Rationale: Make the existing transport proof scope explicit and retain every listed invariant without inventing versioned conditional POST behavior.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ005 — Reader Surface (API) > ### Subtask HDE-CONJ005.3 — A7 transport invariants (Reader)
Original scope heading: `### Subtask HDE-CONJ005.3 — A7 transport invariants (Reader)`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
`On the Catalog JSON success route, prove:`
````
Replacement text (literal; delimiter newlines are not payload):
````text
`On the Catalog JSON success route, preserve the Reader v1 GET/HEAD/304 proof family. Production POST /api/reader for v=1 and v=2 remains non-conditional; Reader v2 inherits production Reader v1 transport and error behavior. Prove:`
````

## RL-012

Change type: Evidence Update / Clarity Fix
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24, A26, S11, C1
Rationale: Replace the stored incomplete evidence pointer with exact selected-source Reader families, without guessing the missing original suffix; record writer-owned convergence and the resolved registration gap.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ005 — Reader Surface (API) > ### Subtask HDE-CONJ005.4 — Reader A7 evidence indexing
Original scope heading: `### Subtask HDE-CONJ005.4 — Reader A7 evidence indexing`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
`artifacts/proofs/su`
````
Replacement text (literal; delimiter newlines are not payload):
````text
`schemas/reader.v1.schema.json`

`schemas/reader.v2.schema.json`

`goldens/reader/v1/`

`goldens/reader/v2/`

**Accepted HDE-EPIC040 evidence and current requirement:** PR06a records owner-regenerated Reader schema/golden and route evidence, with canonical gate and Evidence Index checks passing at its landed tree. PR06b records the later `1.3.0` cut, owner-regenerated dependents, and passing canonical gate and Index checks. Maintain applicable same-change Index/Mirror/hash/path-proof coherence through the existing owning writers; these records do not replace the whole-family requirement above. PR #559 separately landed and registered the QA evidence of record, resolving QA50-F01. Preserve capture-time identity and provenance; O-P06b-17's origin-family mirror labels remain with the evidence/updater owner.
````

## RL-013

Change type: Clarity Fix
Operation: `FIND_AND_REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A30
Rationale: Remove the three named current-status authority locators in CONJ008, CONJ008.1, and CONJ009.1, preserving W-003, the historical drain label, and all status/evidence content.
Section path: Whole unchanged original; the three literal matches are in ## Task HDE-CONJ008 — Writer Surfaces (API) > ### **Subtask HDE-CONJ008.1 — Writer envelope & posture**; and ## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates) > ### **Subtask HDE-CONJ009.1 — Canonical JSON invariants (all surfaces)**
Original scope heading: `WHOLE ORIGINAL PF`
Expected literal occurrence count: 3
Old text / FIND (literal; delimiter newlines are not payload):
````text
W-003 / PF10 Addendum 2.21 HDE-EPIC029
````
Replacement text (literal; delimiter newlines are not payload):
````text
W-003 / HDE-EPIC029
````

## RL-014

Change type: Task Notes / Evidence Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A18, A22, A23, A24, A26, C1
Rationale: Account for delivered F07 remediation where the writer task owns its evidence consequences, without treating historical non-admission as a current blocker.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ008 — Writer Surfaces (API)
Original scope heading: `## Task HDE-CONJ008 — Writer Surfaces (API)`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
The final accepted bundle carries forward the canonical writer-side JSON fix in `adapter/http_reader.py`, preserves the existing dev-only writer route posture, and reports the full named validation and evidence-refresh suite green under closed rails.
````
Replacement text (literal; delimiter newlines are not payload):
````text
The final accepted bundle carries forward the canonical writer-side JSON fix in `adapter/http_reader.py`, preserves the existing dev-only writer route posture, and reports the full named validation and evidence-refresh suite green under closed rails.

**Accepted HDE-EPIC040 conjunction-proof consequence:** PR04-F07's vendor dependency and non-admission failure are historical. PR06 first admitted the complete release; PR06a then restored the dev conjunction evidence capture with the real admitted release identity, a dev-only resolver seam absent by default, corrected generator assertions, CI test-owner registration, and owner-regenerated writer artifacts. PR06b records the later release and owner-generated evidence convergence. This preserves the existing dev-only writer scope and introduces no production writer, live vendor/DB operation, dev identity stamp, or admission bypass.
````

## RL-015

Change type: Evidence Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A18, A23, A24, C1
Rationale: Preserve the typed-envelope requirement and old proof companions while distinguishing the delivered admitted-identity capture from the removed bypass.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ008 — Writer Surfaces (API) > ### **Subtask HDE-CONJ008.1 — Writer envelope & posture**
Original scope heading: `### **Subtask HDE-CONJ008.1 — Writer envelope & posture**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
`artifacts/writer/conjunction_writer_summary.json.path_proof.txt`
````
Replacement text (literal; delimiter newlines are not payload):
````text
`artifacts/writer/conjunction_writer_summary.json.path_proof.txt`

**HDE-EPIC040 evidence qualification:** The restored dev capture carries the real admitted release identity, not the former `dev` stamp. Its resolver seam is dev-only and absent by default, and the generator supplies deterministic mapped rows for its capture. PR06a's accepted F07 delivery supports this bounded proof; it does not establish live DB persistence or production writer behavior.
````

## RL-016

Change type: Evidence Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24, A26, C1
Rationale: Update the existing parity evidence row without inventing a DB write or treating new capture identity as proof of every persistence predicate.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ008 — Writer Surfaces (API) > ### Subtask HDE-CONJ008.2 — Idempotent writer path & byte parity
Original scope heading: `### Subtask HDE-CONJ008.2 — Idempotent writer path & byte parity`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
Reviewed closure evidence records explicit writer/readback parity artifacts, coherent governed path proofs for those artifacts, preserved idempotence behavior, and a green writer-route validation run.
````
Replacement text (literal; delimiter newlines are not payload):
````text
Reviewed closure evidence records explicit writer/readback parity artifacts, coherent governed path proofs for those artifacts, preserved idempotence behavior, and a green writer-route validation run.

**Later HDE-EPIC040 proof:** PR06a records restoration and owner regeneration of the writer capture under admitted identity; PR06b records convergence through the existing evidence owners for the accepted `1.3.0` release. The prior EPIC027 write/readback evidence remains a historical scoped proof. The restored dev capture alone is not a new live-persistence execution or broader write-path acceptance.
````

## RL-017

Change type: Subtask Notes / Evidence Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A18, A23, A24, A26
Rationale: Record the delivered resolver/CI ownership repair and preserve the existing writer/A7, rails, and governed-writer boundaries.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ008 — Writer Surfaces (API) > ### Subtask HDE-CONJ008.3 — Writer evidence presence & indexing
Original scope heading: `### Subtask HDE-CONJ008.3 — Writer evidence presence & indexing`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
Writer proof behavior remains outside the A7 proof family. The writer evidence generator now requires explicit caller-provided open rails and no longer silently widens rails on its own.
````
Replacement text (literal; delimiter newlines are not payload):
````text
Writer proof behavior remains outside the A7 proof family. The writer evidence generator now requires explicit caller-provided open rails and no longer silently widens rails on its own.

**HDE-EPIC040 owner and registration consequence:** PR06a registers `tools/evidence/generate_conjunction_writer_evidence.py` with `_EVIDENCE_GENERATOR_TEST_OWNERS` so `tests/evidence/test_dev_conjunction_identity.py` is a changed-test target, and records owner-regenerated writer artifacts. The restored proof has no live-vendor dependency and uses real admission without a fabricated release. Keep its artifact and CI-owner registration coherent through those existing owners. The A7 exclusion and caller-controlled rails remain unchanged; the separate O-P06b-17 provenance-label observation is still owned by the evidence/updater lane.
````

## RL-018

Change type: Task Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24, S11
Rationale: Preserve set-like normalization where it applies and explicitly protect the delivered ordered v2 category array.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates)
Original scope heading: `## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates)`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
Arrays-as-sets deduped and ASCII-sorted.
````
Replacement text (literal; delimiter newlines are not payload):
````text
Arrays-as-sets deduped and ASCII-sorted.

Reader v2 categories retains the governed Magic-10 order and is not normalized as a set. Its object-key sorting, LF, preimage, AB/BA, and two-run proofs use the same canonical emission path; this adds no alternate serializer or scoring authority.
````

## RL-019

Change type: Evidence Update / Subtask Notes
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A23, A24, A26, S11, C1
Rationale: Add new evidence and ordered-array consequences to the actual canonical invariants row without reinterpreting the prior QA stream.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates) > ### **Subtask HDE-CONJ009.1 — Canonical JSON invariants (all surfaces)**
Original scope heading: `### **Subtask HDE-CONJ009.1 — Canonical JSON invariants (all surfaces)**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
`audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`
````
Replacement text (literal; delimiter newlines are not payload):
````text
`audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`

**HDE-EPIC040 integration-proof consequence:** PR06a records canonical Reader v2 goldens and the restored admitted-identity dev conjunction capture; PR06b records the later release-bound owner convergence. Verify v2 category order and complete intrinsic-result projection alongside canonical object keys, preimage, AB/BA, and two-run identity. The existing EPIC029 all-surface inventory and proofs remain scoped historical evidence; neither they nor the EPIC040 closure establish complete HDE-CONJ010 integration or phase exit.
````

## RL-020

Change type: Clarity Fix / Evidence Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A22, A24, A26, A30, S11, C1
Rationale: Remove the named current locator and distinguish evidence convergence/landing from QA, closure, and unresolved provenance work.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates) > ### Subtask HDE-CONJ009.2 — Global Index/Mirror discipline
Original scope heading: `### Subtask HDE-CONJ009.2 — Global Index/Mirror discipline`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
HDE-CONJ009 is now **Done**. This subtask closed the EPIC027 global-discipline slice, and the later W-003 plus PF10 Addendum 2.21 decision closes the remaining canonical-JSON invariants slice.
````
Replacement text (literal; delimiter newlines are not payload):
````text
HDE-CONJ009 is now **Done**. This subtask closed the EPIC027 global-discipline slice, and the later W-003 decision recorded in HDE Build Notes closes the remaining canonical-JSON invariants slice.

**Later HDE-EPIC040 evidence:** PR06a and PR06b record owner-regenerated release dependents with passing canonical gate and Index checks. The exceptional closure records PR #559's separate landing and Index/Mirror registration of the QA evidence of record, resolving QA50-F01; that landing is not a new QA run. Maintain the existing same-change evidence discipline, preserve frozen capture-time identities, and retain O-P06b-17 with its evidence/updater owner. None of these facts creates an acceptance map, token matrix, close pack, or Conjunction phase exit.
````

## RL-021

Change type: Task Notes / Epic-information Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A22, A23, A24, A26, S01, S02, S06, S11, S12, C1; supporting PF09.3 HDE-SEPA006
Rationale: Explain exactly how accepted Separation evidence contributes to the existing Partial Conjunction task without blanket row completion or a second inventory home.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## **Task HDE-CONJ010 — Full Magic10 deterministic scoring integration**
Original scope heading: `## **Task HDE-CONJ010 — Full Magic10 deterministic scoring integration**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
**Task status:** **Partial**
````
Replacement text (literal; delimiter newlines are not payload):
````text
**Task status:** **Partial**

**Task notes:**

HDE-EPIC040 is Separation Pass 3, with HDE-SEPA005 and its five subtasks as the sole selected inventory. Its accepted Reader v2 and adjacent contract overlay supplies reusable consumer/proof evidence for this task, especially HDE-CONJ010.4 and HDE-CONJ010.6; it does not transfer the Epic into Conjunction, reopen its twenty-nine Done/context exclusions, or establish completion of this task's full population.

The admitted release and exact repository-root golden comparison are delivered foundations. PR06a resolves F03/F05/F07, and PR06b resolves C040-08 and records the accepted 45-member `1.3.0` release. Full Conjunction completion still requires the actual behavior, complete consumer/proof coverage, evidence, and decisions of each subtask. HDE-CONJ010.1, .2, .3, and .5 are not closed by the selected sources' narrower consumer delivery or by exceptional Epic closure; their existing statuses remain. HDE-CONJ010.4 and .6 retain the precise remaining limitations below.

No new Epic, successor identifier, implementation unit, acceptance token, or documentation-only task is allocated. HDE-SEPA006's Adapter/Engine chart-loader and caller migration remains separately owned in Separation. The known legacy CLI proof failure, wheel-distribution decision, and evidence currency/provenance observations retain their existing owners.
````

## RL-022

Change type: Subtask Update / Evidence Update / Epic-information Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A16, A17, A18, A22, A23, A24, A26, S06, S11, S12, C1; supporting C0 §§3–6 and PF09.3 HDE-SEPA006
Rationale: Use the actual existing consumer-integration subtask for delivered v2/route/schema/dev evidence, retaining Partial with its complete migration and live-success gaps.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## **Task HDE-CONJ010 — Full Magic10 deterministic scoring integration** > ### **Subtask HDE-CONJ010.4 — Engine Core and pre-admin surface integration**
Original scope heading: `### **Subtask HDE-CONJ010.4 — Engine Core and pre-admin surface integration**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
### **Subtask HDE-CONJ010.4 — Engine Core and pre-admin surface integration**

**Subtask ID:** HDE-CONJ010.4

**Subtask name/label:** Engine Core and pre-admin surface integration

**Subtask description:**  
 Replace precomputed-score input and migrate compat, CLI, internal HTTP, production Reader POST/projection, narrative routing, presenter, and current generators to one result.

**Subtask status:** **Partial**


````
Replacement text (literal; delimiter newlines are not payload):
````text
### **Subtask HDE-CONJ010.4 — Engine Core and pre-admin surface integration**

**Subtask ID:** HDE-CONJ010.4

**Subtask name/label:** Engine Core and pre-admin surface integration

**Subtask description:**  
 Replace precomputed-score input and migrate compat, CLI, internal HTTP, production Reader POST/projection, narrative routing, presenter, and current generators to one result.

**Subtask status:** **Partial**

**Subtask notes:**

**Delivered consumer sub-slice:** PR06a serves production `POST /api/reader` for v1 and v2 through the existing canonical result and emitter, conforms the unchanged v1 success schema, and restores the admitted-identity dev conjunction capture. PR06b conforms the v1 error schema without changing emitted errors. Reader v2 projects all ten governed bands in canonical order, remains numeric-free, and adds no prompt, narrative key, CLI flag, calculator, or independent rescoring path. Reader v1 and Reader-to-CLI dump parity retain their original scope.

**Remaining Partial burden:** Establish the complete supported pre-admin consumer migration required by this row, including the narrative, presenter, and current-generator obligations, with the row's no-legacy boundary and scoped evidence. The selected sources do not establish that complete population. PR06a/PR06b retain the pre-existing `scripts/hd_cli.py` / `tests/reader_v1/test_cli_proof.py` failure with its recorded owner; the wheel-distribution decision and evidence currency/provenance observations are also carried, not waived. Do not represent the corrected production route as deployed/live current-row DB success.

DEFERRED → CL-40 / future Epic with the App user model — live DB Reader success is blocked by environment; not a close blocker for HDE-EPIC040. No successor ID or completed live observation is recorded. Preserve HDE-SEPA006's separate orchestration/caller boundary; this integration neither performs nor completes that migration.

**Epic or card:** HDE-EPIC040 supplies the accepted supporting consumer delivery only; the full Conjunction work population remains this row's obligation.

**Evidence / artifacts:**

* `schemas/reader.v1.schema.json`, `schemas/reader.v2.schema.json`, `goldens/reader/v1/`, and `goldens/reader/v2/`: accepted schema/projection families recorded by PR06a/PR06b.
* `artifacts/writer/conjunction_write_readback.log` and `artifacts/writer/conjunction_writer_summary.json`: restored dev capture through its owning writer, with real admitted identity.
* HDE-EPIC040 closure decision: attributed tested-source QA and the live-environment limitations, not proof of every Conjunction consumer or production deployment.


````

## RL-023

Change type: Subtask Update / Evidence Update
Operation: `REPLACE`
Target document: `PF09.4-Canon-HDE-Build-Checklist-Conjunction`
Source-ledger basis: A18, A22, A23, A24, A26, S06, S11, C1; supporting C0 §§3–6, §15
Rationale: Account for the delivered versioned goldens and real-identity capture while retaining the complete integration-proof and deferred live observation obligations.
Section path: # **Phase IV — Conjunction (Surfaces and tools meet the core)** > ## **Task HDE-CONJ010 — Full Magic10 deterministic scoring integration** > ### **Subtask HDE-CONJ010.6 — Integration goldens and parity**
Original scope heading: `### **Subtask HDE-CONJ010.6 — Integration goldens and parity**`
Expected literal occurrence count: 1
Old text / FIND (literal; delimiter newlines are not payload):
````text
### **Subtask HDE-CONJ010.6 — Integration goldens and parity**

**Subtask ID:** HDE-CONJ010.6

**Subtask name/label:** Integration goldens and parity

**Subtask description:**  
 Implement full-matrix, AB/BA, two-run, pair/cache identity, UID-independence, result-schema, Reader-projection, failure-token, and internal-parity proofs.

**Subtask status:** **Partial**


````
Replacement text (literal; delimiter newlines are not payload):
````text
### **Subtask HDE-CONJ010.6 — Integration goldens and parity**

**Subtask ID:** HDE-CONJ010.6

**Subtask name/label:** Integration goldens and parity

**Subtask description:**  
 Implement full-matrix, AB/BA, two-run, pair/cache identity, UID-independence, result-schema, Reader-projection, failure-token, and internal-parity proofs.

**Subtask status:** **Partial**

**Subtask notes:**

**Established bounded proof:** PR06 records exact comparison of the eight governed result goldens at the actual admitted repository root. PR06a records Reader v1/v2 POST, endpoint-catalog, admission, and dev conjunction evidence coverage; v2 goldens pin eligible/ineligible results, canonical ten-category order, AB/BA, and invalid-version behavior. Its required v2 proof includes two-run identity and recomputation of the governed five-key preimage. PR06b records schema-valid v1 errors, adverse-envelope refusals, unchanged emitted errors, and the owner-converged 45-member `1.3.0` release. The closure decision records the accepted 12-check QA scope at tested source `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d`; PR #559 separately resolves QA50-F01.

**Remaining Partial burden:** Reconcile and prove this row's full matrix, pair/cache identity, UID-independence, result schema, Reader projection, failure-token, and internal-parity population, with exact tested-state attribution and disclosed baseline failures. The selected consumer/golden proof does not independently establish the entire Conjunction population. Reader-to-CLI dump parity remains a v1 family, and the legacy CLI proof failure remains with its recorded owner. Preserve capture-time identity for frozen evidence; no current service identity substitutes for it, and O-P06b-17's origin-family mirror labels remain an evidence-owner question.

DEFERRED → CL-40 / future Epic with the App user model — live current-row Gate readiness and live DB Reader success remain environment-blocked; not close blockers for HDE-EPIC040. Their later owner/re-homing route is retained without allocating a new ID, inventing a live PASS, or changing the Separation inventory.

**Evidence / artifacts:**

* `goldens/reader/v1/`, `goldens/reader/v2/`, `tests/evidence/test_dev_conjunction_identity.py`, and the admitted writer capture family: bounded accepted proof recorded by PR06a/PR06b.
* `audit/qa/hde-epic040/`: QA evidence of record landed through PR #559 and registered by its owner; landing is distinct from the original tested source and verdict.
* Required remaining Conjunction proofs use the actual owning contracts and governed writers; these notes create no new evidence schema, acceptance roster, writer, or path home.

````

END OF REDLINES
