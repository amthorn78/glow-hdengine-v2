# Rescoping CRD - HDE-EPIC038 - PR-04

## 1. Document Control

| Field | Value |
| --- | --- |
| CRD ID | CRD-HDE-EPIC038-PR-04 |
| CRD version | v1.4 |
| Supersedes | v1.3 |
| Epic ID and name | HDE-EPIC038 - Distillation Pass 3 |
| PR or slice ID | PR-04 - DB, BodyGraph, bridge, and architecture posture harness |
| Author role | Sekhmet |
| PO authorization | APPROVED |
| IA review status | READY FOR IA RE-REVIEW |
| Confirmed rescoping findings | BUG-001, BUG-003 |
| Confirmed retained-scope repairs | BUG-002, BUG-004 |
| Repo identity | amthorn78/glow-hdengine-v2 |
| Repo root used | Connected GitHub repository root; no local product worktree was available in the CRD workspace |
| PF-Canon root | docs/pfcanon at the reviewed PR head |
| Reviewed HEAD | d880e54bfd8b1d689ee08f9b352694924a7ae8d0 |
| Reviewed branch state | codex/implement-pr-04-for-hde-epic038; PR #354 is open and unmerged against main |
| Base reviewed | main at 2971256474f70ad62848ce58a2bfaf1ea4438f37 |
| ADR inventory | ADR-CANON-001 - PROPOSED - PENDING IA TECHNICAL APPROVAL (EXTENDS); ADR-CANON-002 - PROPOSED - PENDING IA TECHNICAL APPROVAL (AMENDS); ADR-CANON-003 - PROPOSED - PENDING IA TECHNICAL APPROVAL (AMENDS) |
| Creation date | 2026-07-15 |
| Revised date | 2026-07-15 |

The target is HDE-EPIC038, not HDE-EPIC034. One earlier conversational label associated PR #354 with HDE-EPIC034, but the connected PR head branch, the Approved Epic Plan, the Current Implementation Plan, the PF09.6 mappings, and every PR-04 artifact registration independently identify HDE-EPIC038. The conflict is therefore resolved without operator input.

Evidence pointer: Repo | GitHub PR #354 metadata | "head=codex/implement-pr-04-for-hde-epic038"; "head_sha=d880e54bfd8b1d689ee08f9b352694924a7ae8d0"; "base=main@2971256474f70ad62848ce58a2bfaf1ea4438f37"; "state=open; merged=false; changed_files=62".

Evidence pointer: Implementation Plan | r6 Implementation Plan HDE-EPIC038, "PR-04 - DB, BodyGraph, bridge, and architecture posture harness" | "Complete the deterministic local mechanics and evidence producers for DB runtime posture, BodyGraph source and policy behavior, direct-versus-bridge parity, environment connectivity, and a keys-only architecture snapshot."

Exact source units used:

- Current Debugging Context: the complete PR #354 implementation and remediation flow in Pasted text(93).txt; subsequent PR #354 finding analysis; IA reviews v1.0, v1.1, and v1.2 as debugging-context findings; and current GitHub review threads.
- Repo: PR #354 metadata, review threads, changed-head files, current artifacts, schemas, tests, Human/Machine evidence bindings, and current generator behavior at d880e54bfd8b1d689ee08f9b352694924a7ae8d0.
- Approved Epic Plan: r1 Epic Plan HDE-EPIC038.md, complete document.
- Current Implementation Plan: r6 Implementation Plan HDE-EPIC038.md, complete document, especially PF09 Completion Scope, Execution Plan items 4 through 8, PR-04, PR-05, PR-06, OPS-01, and OPS-02.
- PF10-HDE-Build-Notes v12.2.1, complete current unit, especially Addendum Index and §2.1) PR-01 HDE-EPIC038.
- PF02-Canon-HDE-Architecture v2.3.8, §5.4 Evidence & determinism flows (concept only), §6.1 BodyGraph ingest & refresh posture (concept only), and §6.2 Vendor seam (concept only).
- PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, HDE-DIST001.4, HDE-DIST001.5, HDE-DIST001.7, HDE-DIST001.9, HDE-DIST001.10, HDE-DIST001.11, and HDE-DIST002.5.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8, §8.3 Machine Evidence Index — JSONL mirror (records-only) [Required-Now], including canonical JSONL, sibling path-proof, and write-discipline requirements, consulted only for REV-002.
- PF14-Canon-HDE-Mechanics-Guide v3.4.3, §1.3.1 Evidence jobs (single-writer tools), plus the source-invariance and HDAPI adapter/presenter mechanics already preserved from v1.3; §1.3.1 was revalidated only for REV-001 and REV-002.
- PF27-Canon-Plan-Templates v1.9.5, §Review guardrails, including Governed evidence family coherence, Evidence-family path collision repair, Evidence artifact-key collision repair, and Final generator logic rule; the collision unit was revalidated only for REV-001 and REV-002.

No product, plan, PF-Canon, ADR, PF09, evidence, or GitHub state was modified while authoring this CRD. The only created file is this standalone CRD outside the product repository.

## 2. Executive Summary

PR #354 contains two confirmed architectural defects that cannot be repaired coherently by regenerating the current artifacts.

First, the BodyGraph source-invariance producer proves only that two synthetic party orders carry the same hard-coded source labels. Both AB and BA contain only source "db"; no independent DB and vendor representations are acquired, projected, emitted, or compared. The artifact can therefore report PASS while the canonical property - byte-identical DB-sourced and vendor-sourced BodyGraph output for the same normalized input through the shared Presenter - remains untested.

Second, PR-04 exposed a broader producer-ownership defect. The legacy Rails Closed Phase 1 generator directly writes DB posture, DB-bridge, BodyGraph policy, rails-refusal, shared Presenter, and sibling path-proof families now assigned to focused producers; it also delegates the environment-matrix producer. Independently, the DB-runtime and DB-bridge generators both write the two environment-connectivity primaries. PR-04 also attempts to preserve Presenter history by replaying hard-coded records. The result is not one collision but a cross-family writer graph in which command order can change or erase governed evidence and updater-owned companions.

The selected architecture is:

1. Add a pure, source-neutral BodyGraph projection boundary at proposed module engine/bodygraph/projection.py. It exposes the exact type CanonicalBodyGraph and the exact API project_bodygraph(mapped) -> CanonicalBodyGraph. It normalizes only already-mapped HDE BodyGraph data, strips source metadata, rejects unknown or unsafe fields, performs no I/O, and continues to use engine.presenter.emitter.emit_public as the only byte emitter.
2. Replace the semantically invalid v1 AB, BA, and summary records in place with a closed, versioned v2 evidence contract. Each source is independently re-acquired from a distinct deterministic representation twice, bound to the same normalized input hash, projected through the shared boundary, emitted through the shared Presenter, and compared. A generated negative-control receipt must prove divergence is rejected.
3. Retire tools/evidence/generate_rails_closed_phase1.py from current evidence generation as a no-write, fail-closed compatibility guard. Assign every affected primary to exactly one focused owner: DB posture to generate_db_runtime_posture.py; DB-bridge selection, capability, provider parity, and both environment-connectivity primaries to generate_db_bridge_parity.py; BodyGraph policy to generate_bodygraph_policy_proofs.py; rails refusal to generate_rails_gate_evidence.py; and all proof companions/indexes to update_evidence_index.py. Move PR-04's DB-versus-bridge Presenter comparison to proposed path artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json. Add proposed tools/evidence/generate_presenter_history.py as the sole selective owner of artifacts/presenter/json_canon_compare.log, reading exactly four immutable historical payloads from tools/evidence/fixtures/presenter/json_canon_compare.history.v1.json and reproducing the approved four-line body with SHA-256 64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c. Remove the provisional PR-04 row, replay constants, direct companion writes, and PR-specific duplicate keys.

BUG-002 and BUG-004 remain mandatory original-scope repairs. The architecture analyzer must recognize current Flask method decorators and derive its verdict from findings; the release-binding artifact must be regenerated after all final BodyGraph inputs and must add the new source-invariance summary to its existing source-policy and refresh inputs. Neither defect creates an additional RSC.

The minimum rescope is RSC-001 through RSC-003. RSC-001 EXTENDS the current architecture with a named pure convergence boundary. RSC-002 AMENDS the governed source-invariance evidence contract in place. RSC-003 AMENDS the directly implicated evidence-producer ownership graph, Presenter-history reconstruction contract, and PR-04 plan output. Deferral is unsafe because the current proof can certify a false invariant and the current writer graph cannot guarantee path ownership, byte stability, order independence, or updater-only companions.

Preserved boundaries are explicit: no public Reader or CLI contract changes; no live DB, bridge, or vendor execution; no mapped-cache write implementation; no raw vendor persistence authorization; no PR-05, OPS-01, OPS-02, or PR-06 closure; no PF09 status movement; no QA PASS; and no epic closeout.

Evidence pointer: Repo | tools/evidence/generate_bodygraph_policy_proofs.py, inv() and generate() | "source:'db'" for every row; "canonical_source_sequence:['db','db']"; summary compares only those arrays.

Evidence pointer: Repo | tools/evidence/generate_db_bridge_parity.py and tools/evidence/generate_rails_closed_phase1.py | Both replace artifacts/presenter/json_canon_compare.log; the PR-04 producer uses PRESENTER_BASE_RECORDS.

Evidence pointer: Repo | artifacts/evidence_index.jsonl at PR #354 head | The shared Presenter path has both "presenter.bodygraph.json_canon_compare" and "epic038.pr04.presenter_json_canon_compare"; each source-invariance path likewise has an established key and an added PR-specific duplicate.

## 3. Authority and Decision Posture

### PO authority

The Product Owner has approved bounded rescoping for this slice. That authority permits this CRD to propose precise changes to architecture, evidence contracts, ownership, plans, and PF-Canon. It is not technical proof and does not authorize implementation.

PF10 provides a controlling precedent for HDE-EPIC038: an approved rescope is a bounded Product Owner canon amendment for the exact decisions it adjudicates, while permanent PF drainage remains later documentation work.

Evidence pointer: PF10-HDE-Build-Notes | §2.1) PR-01 HDE-EPIC038 | "The approved rescope is treated as a bounded Product Owner canon amendment for the exact decisions it adjudicates. Permanent PF drainage remains required but is documentation drainage, not an implementation blocker."

### Sekhmet decisions and IA review

RSC-001 through RSC-003 and ADR-CANON-001 through ADR-CANON-003 are proposed technical decisions authored by Sekhmet. IA must approve or return the complete decisions for revision. IA is not being asked to choose a module, type, API, source scope, schema, path, key, producer, owner, migration, validation, rollback, or adoption order.

### Required lifecycle after approval

The required sequence is:

1. IA technical approval of this CRD.
2. Separately authorized revision of the Current Implementation Plan to incorporate the plan-consequence matrix.
3. Separate implementation authorization and reconciliation of provisional PR #354 with the approved CRD and revised plan.
4. Implementation and deterministic validation in the authorized lane.
5. Later QA, OPS, acceptance, and closeout work under their existing owners.
6. Permanent PF10, PF02, PF12, PF14, PF09.6, and PF27 drainage as applicable.

IA approval is not implementation authorization. This CRD neither accepts nor rejects PR #354's provisional commits.

### Prohibited claims

This CRD does not establish PF-Canon adoption, ADR adoption, PF09 movement, implementation completion, QA PASS, OPS completion, acceptance-token satisfaction, deployment authorization, migration authorization, slice acceptance, PR merge approval, epic closeout, or board closeout.

## 4. Debugging Flow Basis

### Finding disposition ledger

| ID | Classification | Disposition |
| --- | --- | --- |
| BUG-001 | Confirmed rescoping premise | Current source-invariance evidence proves party/source-label repetition rather than same-input DB/vendor projected and emitted byte equality. Creates RSC-001 and RSC-002. |
| BUG-002 | Confirmed retained-scope repair | Current architecture scan misses Flask method decorators such as @app.get and hard-codes PASS. Correct inside D11/HDE-DIST001.10; no new RSC. |
| BUG-003 | Confirmed rescoping premise | A broad legacy generator competes with focused DB, bridge, BodyGraph, rails-gate, and updater owners; the DB-runtime and DB-bridge generators also compete for both environment-connectivity primaries; two producers and duplicate keys compete for the shared Presenter log. Creates RSC-003. |
| BUG-004 | Confirmed retained-scope evidence blocker | release_bindings.json is stale after its primary inputs changed. Repair through existing release-binding and updater ownership; no new RSC. |
| SUSP-001 | Suspected or conditional concern; ROOT CAUSE UNCONFIRMED beyond BUG-002 | Additional current or future route-registration forms may be omitted. Later analyzer must classify discovered route-like forms or fail closed. |
| TB-001 | Stale tooling blocker | Earlier inability to resolve the PR is superseded by the connected GitHub repository and unique PR #354 metadata. |
| STALE-001 | Ruled out at current head | Generator self-scan drift was fixed by excluding the generator and using AST inspection. |
| STALE-002 | Ruled out at current head | Registered engine compat routes are now classified as allowed. |
| STALE-003 | Ruled out as written | BA identity order is reversed at current head; the remaining defect is source semantics, BUG-001. |
| STALE-004 | Ruled out at current head | Hard-coded SELECT grants were replaced by a derived no-grant posture. |
| STALE-005 | Ruled out as written | The current shared Presenter file is JSONL, not mixed format. Dual ownership and duplicate keys remain BUG-003. |

Evidence pointer: Debugging Context | BUG-001 final RCA | "tools/evidence/generate_bodygraph_policy_proofs.py source-invariance evidence proves only hard-coded DB source decisions and does not compare DB/vendor emitted payloads or hashes."

Evidence pointer: Debugging Context | BUG-002 final RCA | "adapter/wsgi.py declares /internal/healthz and /internal/readyz via @app.get(...), but the scanner only detects Blueprint(...) calls and .route(...) attributes."

Evidence pointer: Repo | GitHub review finding "Preserve the JSONL presenter compare log" and current generators | The earlier mixed-format symptom was repaired, but both generators still full-write the same path.

Evidence pointer: Repo | current artifacts/bodygraph/release_bindings.json and tools/evidence/generate_release_bindings.py | The committed input hashes and sizes do not match current source-selection and refresh-policy bytes; check mode therefore reports drift.

### Relevant actions and diagnostics

- The initial PR implementation added DB runtime posture, DB-bridge parity, BodyGraph policy, architecture snapshot, evidence registration, and focused tests.
- Follow-up commits repaired architecture self-scanning, registered engine route classification, JSONL formatting, BA identity ordering, path-proof ownership, and grant derivation.
- Static inspection then established that the local fixes did not repair source semantics or unique Presenter ownership.
- IA review v1.2 expanded BUG-003's confirmed collision surface: the legacy generator also writes overlapping DB, DB-bridge, BodyGraph, rails-refusal, and path-proof outputs, and both PR-04 DB generators write the environment-connectivity pair.
- Reviewer-directed read-only inspection established the complete direct-write inventory, the focused producers' current ownership, the four approved historical Presenter rows, the selected legacy generator's wall-clock/top-level/direct-proof behavior, and the absence of a selective check interface.
- Current GitHub inspection established PR #354's exact head, open/unmerged status, 62-file change set, current review findings, and current duplicate Machine Mirror rows.
- Current Repo inspection compared the false proof with engine/bodygraph/ingest.py, engine/bodygraph/v2_adapter.py, engine/presenter/emitter.py, both shared-log writers, current schemas, current artifacts, and current tests.

Evidence pointer: Repo | PR #354 commit sequence d56c553c, c68b328d, d95cb479, d880e54b | The sequence implemented PR-04 and then repaired local evidence and analyzer defects before the remaining architecture findings were raised.

### RCA conclusions

BUG-001 root cause is a category error: party order was treated as source acquisition, and PASS was derived from labels instead of independently acquired canonical bodies. A second error allowed dry-run self-hashing and hard-coded fixtures to stand in for two-run convergence.

BUG-003 root cause is missing evidence ownership design at the command graph level. A historical monolithic generator remained executable after focused producers assumed its DB, bridge, BodyGraph, rails-refusal, and companion responsibilities; two focused PR-04 generators independently materialized the same environment-connectivity pair; and PR-04 was added to a shared historical file by copying old rows instead of assigning a selective historical owner and a task-specific primary. The prior RSC-003 treated the visible Presenter collision but not the transitive writer graph, so its selected owner could not satisfy its own determinism, preservation, or rollback contract.

BUG-002 root cause is an incomplete route-declaration taxonomy combined with a renderer that can assert PASS independently of discovered unknowns.

BUG-004 root cause is generation-order incompleteness: a derived historical binding was checked before being rematerialized after all changed primaries reached final bytes.

### Rejected resolution alternatives

1. Restore only the pre-PR artifact shape: rejected because shape restoration does not establish a production-owned convergence boundary or independent acquisitions.
2. Reuse engine/bodygraph/ingest.py wholesale: rejected because it performs live I/O and persistence, its dry-run path assigns the same hash to both sides, and its current persistence semantics belong to a legacy ingest path rather than PR-04's closed-rails proof.
3. Compare parsed dictionaries only: rejected because the canonical property is final Presenter byte equality, not object equality.
4. Append a PR-04 row to the shared Presenter log: rejected because append order and multiple writers remain nondeterministic.
5. Replay historical rows from constants: rejected because it turns PR-04 into an unauthorized owner of another evidence family.
6. Move PR-05 mapped-cache persistence into PR-04: rejected because a deterministic mapped fixture can prove the PR-04 boundary without moving durable writes, idempotence, or live read-back ownership.
7. Retain generate_rails_closed_phase1.py as the shared Presenter owner: rejected because it emits one wall-clock row, writes unrelated primaries and sibling path proofs, has no selective mode, and has no read-only check mode.
8. Convert the broad legacy generator into a dispatcher over focused writers: rejected because the compatibility command would continue to mutate several independently owned families and would obscure which producer owns the final bytes. A no-write retirement guard makes stale invocations visible instead.

### Residual non-material Unknown

The complete future universe of Flask or extension-specific registration forms is not knowable statically. This does not affect the selected architecture because the analyzer must report every unclassified route-like decorator or registration call as unknown and derive FAIL until the taxonomy is explicitly extended. There are no residual material Unknowns in module, API, source scope, schema, path, key, producer, consumer, ownership, migration, validation, rollback, or adoption.

## 5. Current Contract and Observed Conflict

### Implemented contract

The current BodyGraph producer writes schema "v1" AB and BA records using synthetic identity order. Every source decision is "db"; both source sequences are ["db","db"]; the summary Boolean is the equality of those arrays. The synthetic vendor-upsert and DB-resolve artifacts contain posture metadata rather than two independently emitted BodyGraph bodies.

The current v2 adapter already maps a supported ChartResult into HDE-shaped bodygraph, person, and cache data. It adds source metadata. The existing Presenter emitter delegates to the canonical serializer and is the correct final-byte authority.

The current legacy ingest path demonstrates vendor emit, persistence, DB read-back, re-emit, and hash comparison, but its dry-run path reuses one hash and its live I/O/persistence behavior is outside PR-04.

The current producer graph violates the intended focused ownership model. tools/evidence/generate_rails_closed_phase1.py executes generation at module import/top level, uses the wall clock, calls its own path-proof writer after every primary, delegates env-matrix generation, and directly writes DB posture, DB-bridge selection/capabilities, BodyGraph policy, the shared Presenter log, and rails-refusal evidence. It produces only one Presenter row and has no --check or selective family interface. Separately, generate_db_runtime_posture.py and generate_db_bridge_parity.py both render artifacts/runtime/env_connectivity.snapshot.json and artifacts/runtime/env_connectivity.nondev_failure.json. The current shared Presenter log contains four historical rows plus one provisional PR-04 row; generate_db_bridge_parity.py reconstructs those bytes from PRESENTER_BASE_RECORDS.

Evidence pointer: Repo | engine/bodygraph/v2_adapter.py, adapt_v2_chart_payload() | The adapter builds bodygraph, person, person_uid, and source fields and a mapped cache payload.

Evidence pointer: Repo | engine/presenter/emitter.py, emit_public() | "Delegates to the canonical serializer (LF-terminated UTF-8)".

Evidence pointer: Repo | engine/bodygraph/ingest.py, ingest_vendor_bodygraph() | Live mode emits vendor bytes, persists, reads back, re-emits, and compares hashes; dry_run assigns db_emitted_sha256=payload_sha and parity_match=True.

Repo evidence: Repo | tools/evidence/generate_rails_closed_phase1.py at d880e54bfd8b1d689ee08f9b352694924a7ae8d0 | "NOW" is derived from the wall clock; writes occur at module top level; _write_bytes calls _write_path_proof; no --check interface exists.

Repo evidence: Repo | tools/evidence/generate_db_runtime_posture.py and tools/evidence/generate_db_bridge_parity.py at the reviewed head | Both name and write the two artifacts/runtime/env_connectivity primaries.

Repo evidence: Repo | artifacts/presenter/json_canon_compare.log at the reviewed head | Five canonical JSONL rows are present: four historical rows followed by one provisional PR-04 row.

### Canonical contract

PF09.6 HDE-DIST001.5 requires BodyGraph source selection and AB/BA source invariance. HDE-DIST001.7 states the exact reused source-invariance rule: for the same normalized inputs, DB-sourced and vendor-sourced BodyGraph bodies must be byte-identical through the shared Presenter/emitter. PF02 requires offline evidence to exercise existing behavior without introducing a second emitter or runtime route. PF14 requires a bounded set of single-writer evidence tools and assigns all governed path-proof transcripts to tools/evidence/update_evidence_index.py. PF12 requires canonical JSONL, one trailing LF per line, coherent sibling path proofs, and unique mirror bindings. PF27 makes path/key collisions blocking until task-specific evidence is moved and overwritten shared/dependency artifacts plus companions are coherently repaired.

Evidence pointer: PF09.6-Canon-HDE-Build-Checklist-Distillation | §Subtask HDE-DIST001.7 - Vendor ingest source policy & proofs | "for the same normalized inputs, DB-sourced and vendor-sourced BodyGraph bodies MUST be byte-identical when emitted via the shared presenter/emitter."

Evidence pointer: PF02-Canon-HDE-Architecture | §5.4 Evidence & determinism flows (concept only) | Offline pipelines "do not introduce new runtime surfaces or alter Reader/CLI behaviour" and use the single Presenter emitter.

Evidence pointer: PF27-Canon-Plan-Templates | §Review guardrails, Evidence-family path collision repair | A collision is blocking until task-specific evidence is moved, shared artifacts are restored, and proof/index/mirror bindings are coherent.

### Plan contract

The Current Implementation Plan assigns D9/HDE-DIST001.5 and D10/HDE-DIST001.9 to PR-04, with final binding in PR-06. OPS-01 owns later live read-only DB/bridge evidence. PR-05 and OPS-02 own configured-v2 mapped-cache persistence. PR-04 is closed-rails, fixture-backed, and may not call live DB, bridge, or vendor services.

Evidence pointer: Implementation Plan | r6 Implementation Plan HDE-EPIC038, PR-04 "Rails posture" | "SAFE_MODE=1, ALLOW_NETWORK=0"; "No live DB call"; "No live bridge call"; "No vendor call."

### Exact conflict and dependency

An artifact-only patch cannot solve BUG-001 because DB and vendor values must converge through one source-neutral internal representation before the shared emitter can prove final-byte equality. That representation must be reusable by PR-05 without implementing PR-05 persistence now.

A log-format patch cannot solve BUG-003 because the shared Presenter collision is one edge in a larger writer graph. The legacy command would still overwrite focused DB, bridge, BodyGraph, rails-refusal, and updater-owned outputs, while the two focused DB generators would still compete for environment-connectivity. The repair must retire the broad command from current generation, allocate every directly implicated primary to one focused owner, reconstruct the shared Presenter history from one immutable source through one selective owner, move PR-04 to a dedicated receipt, and migrate consumers, keys, and updater companions atomically.

Deferral would permit false BG source-invariance evidence, order-dependent history loss, a PASS architecture snapshot that omits active routes, and a stale release binding. The selected resolution therefore adds the minimum pure projection and evidence/ownership contracts while retaining all live and durable work downstream.

## 6. Causal Map

### CAUSE-001 - No source-neutral convergence boundary

- Linked finding: BUG-001.
- Current contract: same normalized input from DB and vendor must produce byte-identical Presenter output.
- Repo reality: the v2 adapter produces mapped HDE data, the legacy ingest path compares emitted bytes only after I/O, and no exact current CanonicalBodyGraph/project_bodygraph symbol exists.
- Conflict: the PR-04 proof has no shared pure domain in which DB and vendor representations can be compared without live persistence.
- Consequence: evidence can either duplicate mapping semantics in the generator or continue proving only labels.
- Selected technical decision: RSC-001 and ADR-CANON-001 introduce engine/bodygraph/projection.py, CanonicalBodyGraph, and project_bodygraph().
- Dependency graph: existing v2 adapter output -> project_bodygraph -> existing Presenter emitter -> v2 evidence; DB mapped fixture -> project_bodygraph -> same emitter -> v2 evidence; PR-05 later consumes the same projection before persistence.
- Owners: PR-04 owns the pure projection and proof integration; PR-05 retains durable write/read-back; OPS-01 and OPS-02 retain live evidence.
- Validation: exact-field, source-stripping, unknown-field rejection, adapter-to-projection parity, DB fixture parity, mutation rejection, and no-I/O tests.
- Rollback: remove the unapproved projection and leave source-invariance status non-PASS; never restore the current false PASS as a rollback target.
- Plan consequence: amend D9/PR-04 and make PR-05 consume the approved projection without moving D12.
- Canon/ADR consequence: EXTENDS PF02/PF14 through ADR-CANON-001.

Evidence pointer: Repo | negative search | Terms "CanonicalBodyGraph" and "project_bodygraph"; scope amthorn78/glow-hdengine-v2; GitHub code search; case-sensitive exact terms; result 0 hits.

### CAUSE-002 - Evidence schema can pass without DB/vendor comparison

- Linked finding: BUG-001.
- Current contract: governed evidence must bind same input, distinct sources, independent runs, canonical projection, shared-emitter bytes, and fail-closed predicates.
- Repo reality: current schema "v1" records identity order and a hard-coded source sequence only.
- Conflict: check mode compares the same semantically invalid expected bytes to committed bytes and can certify the wrong property.
- Consequence: BG_SOURCE_INVARIANCE evidence is misleading even when generation and CI are deterministic.
- Selected technical decision: RSC-002 and ADR-CANON-002 replace the three primary records in place with closed v2 schemas, independent source/run acquisition, a negative control, and derived PASS.
- Dependency graph: committed fixtures -> independent acquisition adapters -> projection -> Presenter -> AB/BA/summary -> release bindings -> updater/index/mirror/path proofs -> PR-06.
- Owners: generate_bodygraph_policy_proofs.py is sole primary producer; update_evidence_index.py owns companions; PR-06 is downstream consumer.
- Validation: schema validation, exact key set, independent run IDs, source-representation distinctness, same input hash, order reversal, two-run stability, projection equality, byte equality, unsafe-field absence, and negative-control rejection.
- Rollback: an incomplete v2 migration fails check and cannot emit PASS; no dual v1/v2 acceptance period.
- Plan consequence: amend D9 evidence and validation; refresh D3 release binding; amend PR-06 required primaries.
- Canon/ADR consequence: AMENDS PF12/PF14 through ADR-CANON-002.

### CAUSE-003 - Shared Presenter path and key ownership collision

- Linked finding: BUG-003.
- Current contract: each governed primary has one authoritative producer; focused generators mutate only their owned family; tools/evidence/update_evidence_index.py alone writes sibling path proofs and indexes; shared historical bytes have one deterministic reconstruction source; and each physical path has one canonical current binding.
- Repo reality: generate_rails_closed_phase1.py uses a wall clock, runs at module top level, writes fourteen primaries across six ownership areas plus every sibling path proof, and has no check/selective interface. Focused DB, bridge, BodyGraph, and rails-gate producers write overlapping primaries. generate_db_runtime_posture.py and generate_db_bridge_parity.py both write the environment-connectivity pair. generate_db_bridge_parity.py also replays four historical Presenter rows and appends PR-04 to the shared path.
- Conflict: no allowed command order preserves family boundaries. The prior selected historical owner cannot reproduce the approved four-row history deterministically and cannot check it without rewriting unrelated families or companions.
- Consequence: a command can erase another family's final bytes, path proofs can be generated outside the updater's fixed point, historical bytes can drift with time, and PR-04 can certify or roll back from an unauthoritative source.
- Selected technical decision: RSC-003 and ADR-CANON-003 retire the broad legacy generator from current generation; allocate all directly implicated primaries to focused owners; add tools/evidence/generate_presenter_history.py as the sole selective shared-log producer; bind it to a fixed four-row source manifest and exact output digest; move PR-04 comparison to a dedicated JSON primary; remove replay constants, direct proof writes, and PR-specific duplicate keys.
- Dependency graph: immutable Presenter-history source -> selective Presenter-history producer -> shared four-row JSONL; focused DB/bridge/BodyGraph/rails producers -> their disjoint primary sets; DB-bridge producer -> dedicated direct/bridge receipt; updater -> all companions/index bindings; PR-06 -> dedicated receipt and final focused primaries.
- Owners: generate_db_runtime_posture.py owns DB posture plus the two legacy partition outputs; generate_db_bridge_parity.py owns adapter selection, capabilities, provider parity, both environment-connectivity primaries, and the dedicated PR-04 receipt; generate_bodygraph_policy_proofs.py owns BodyGraph policy; generate_rails_gate_evidence.py owns rails refusal; generate_presenter_history.py owns only the shared log; generate_env_matrix_snapshot.py owns only the env-matrix singleton; update_evidence_index.py owns all companions and indexes. The retired legacy command owns no governed output.
- Validation: one-row-per-primary ownership checks; forbidden-writer static scan; every retained producer's write-set assertion; all allowed producer permutations; four-row exact history and SHA-256; no PR-04 row; no wall-clock read; check-mode no-write; atomic replacement failure tests; unique current keys; dedicated schema/negative control; updater fixed point.
- Rollback: the immutable Presenter-history source and digest, not the legacy generator, are authoritative. A failed preflight leaves the shared file untouched; a failed post-migration validation restores the four-row generated body atomically, removes the dedicated PR-04 family atomically, and leaves PR-04 non-PASS. The broad legacy writer and replay constants are never restored.
- Plan consequence: replace the PR-04 shared-log output with the dedicated path; replace any executable legacy-generator invocation with the focused producer set; update the source-ownership test; preserve historical prose only as provenance; revise PR-06 consumers and order.
- Canon/ADR consequence: AMENDS PF09.6/PF12/PF14 under PF27 collision repair through ADR-CANON-003.

Evidence pointer: Repo | artifacts/evidence_index.jsonl | The shared path has keys "presenter.bodygraph.json_canon_compare" and "epic038.pr04.presenter_json_canon_compare"; each source-invariance path also has established and PR-specific keys.

Evidence pointer: IA Review | REV-001 and REV-002 | The collision inventory must include all overlapping DB, environment-connectivity, adapter-selection, BodyGraph, rails-refusal, Presenter, and direct path-proof writes, and the shared owner must reproduce exactly four historical rows without wall-clock or unrelated writes.

### CAUSE-004 - Route analyzer omits current Flask method decorators

- Linked finding: BUG-002; retained scope.
- Current contract: D11 architecture evidence is discovered, keys-only, and fail-closed on unknowns.
- Repo reality: adapter/wsgi.py uses @app.get; the analyzer recognizes Blueprint and .route only, then hard-codes PASS and unknown_count=0.
- Conflict: active route-bearing code is absent from a passing snapshot.
- Consequence: route drift can bypass the evidence gate.
- Selected technical decision: retain D11 scope; implement the bounded AST taxonomy and analyzer-derived verdict specified in §9.
- Owners: PR-04 retains analyzer/test ownership; PR-06 retains final binding.
- Validation: current method decorators appear; ordinary mapping.get calls are not routes; unknown route-like forms force FAIL.
- Rollback: no PASS artifact is emitted while an unknown or forbidden form exists.
- Plan/canon consequence: correct the existing D11 implementation; NO CANON CHANGE and no RSC.

### CAUSE-005 - Derived release binding is generated before dependency closure

- Linked finding: BUG-004; retained scope.
- Current contract: release_bindings.json binds final BodyGraph source-policy and refresh inputs.
- Repo reality: its current input hashes and sizes are stale; its canonical generator already supports deterministic check mode.
- Conflict: a historical derivative is checked before changed primaries have reached final bytes.
- Consequence: CI fails and final release evidence can misstate its dependencies.
- Selected technical decision: extend the existing input list to include the v2 source-invariance summary, generate after all three inputs are final, then run the updater.
- Owners: the existing release-binding producer and PR-01 artifact identity remain; PR-04 performs status-neutral dependency maintenance; PR-06 consumes.
- Validation: exact path/hash/size binding, sorted deterministic order, check-mode byte comparison, and updater fixed point.
- Rollback: release binding remains non-current and blocks closure if any dependency is missing or stale.
- Plan/canon consequence: update D3/PR-06 dependency order; no new RSC and no historical PF09 movement.

## 7. Requested Rescope

### RSC-001 - Source-neutral BodyGraph projection boundary

**Proposed CRD decision.**

- Canon effect: EXTENDS.
- Linked CAUSE: CAUSE-001.
- Requested addition: add one pure internal projection module used by PR-04 evidence and exposed as the required mapped-payload boundary for PR-05.
- Exact module: engine/bodygraph/projection.py.
- Exact types:
  - BodyGraphFields, a TypedDict with exactly authority, birthDateUtc, centers, channelsLong, channelsShort, definition, gates, profile, strategy, and type.
  - CanonicalBodyGraph, a TypedDict with exactly bodygraph, person, and person_uid.
  - BodyGraphProjectionError, a ValueError subclass whose public code attribute is one of MISSING_FIELD, UNKNOWN_FIELD, PERSON_UID_MISMATCH, INVALID_SHAPE, and UNSAFE_FIELD; the message may add bounded field context but no input value.
- Exact API: project_bodygraph(mapped: Mapping[str, Any]) -> CanonicalBodyGraph.
- Input contract:
  - mapped is an already-adapted HDE payload, not a raw vendor envelope.
  - Allowed top-level input keys are bodygraph, person, person_uid, and optional source.
  - person must contain exactly person_uid.
  - bodygraph must contain exactly the ten BodyGraphFields keys.
  - top-level person_uid and person.person_uid must be the same non-empty string.
  - Every value must be JSON-compatible; mappings must have string keys; non-finite floats, bytes, callables, and custom objects reject with INVALID_SHAPE.
  - A recursive case-insensitive key scan rejects transport, raw, request, response, credential, credentials, authorization, header, headers, token, secret, database_url, db_bridge_url, sql, and parameters with UNSAFE_FIELD.
- Output contract:
  - Output contains exactly bodygraph, person, and person_uid.
  - source and all transport, vendor, request, response, credential, header, and raw-envelope metadata are absent.
  - Input is deep-copied; the function does not mutate caller data.
  - The function performs no network, database, filesystem, clock, environment, random, logging, or persistence operation.
- Deterministic validation order: validate root/JSON shape; run the recursive unsafe-key scan; report the first ASCII-sorted missing required field; report the first ASCII-sorted unknown field; then validate person UID equality. The error code and bounded field path are therefore stable for the same input.
- Source-adapter scope:
  - Vendor side: existing engine.bodygraph.v2_adapter.adapt_v2_chart_payload maps the deterministic configured-v2 ChartResult fixture; its resolved mapping is projected.
  - DB side: a deterministic mapped-cache-row fixture supplies its payload field; that payload is projected.
  - Legacy v1 ingest is not converted, reauthorized, or claimed by this slice.
- Same-input identity: both source fixtures bind to the SHA-256 of tests/fixtures/bodygraph/source_invariance/normalized_input.v1.json canonical bytes.
- Exact fixture paths:
  - tests/fixtures/bodygraph/source_invariance/normalized_input.v1.json
  - tests/fixtures/bodygraph/source_invariance/vendor_chart_result.v1.json
  - tests/fixtures/bodygraph/source_invariance/db_cached_payload.v1.json
- Normalized-input fixture contract:
  - It contains exactly schema, fixture_id, person_uid, birthdate, birthtime, and location.
  - Values are bodygraph.source_invariance.normalized_input.v1, hde-epic038-pr04-source-invariance-01, 00000000-0000-4000-8000-000000000038, 2000-01-01, 00:00, and Synthetic Test Location respectively.
  - Both source fixtures contain input_fingerprint equal to the canonical SHA-256 of this fixture. The DB fixture is committed independently and may not be generated from, copied from, or rewritten from the vendor fixture during proof execution.
- Vendor fixture contract:
  - Top-level keys are exactly schema, input_fingerprint, context, and payload; schema is bodygraph.source_invariance.vendor_chart_result.v1.
  - context contains exactly person_uid, user_id, vendor, vendor_version, input_fingerprint, route_family, route, and payload_family. Values are the normalized person_uid, 00000000-0000-4000-8000-000000000039, hdapi, 2, the shared input fingerprint, recommended_v2_chart, /v2/charts, and ChartResult.
  - payload contains exactly the existing CHART_RESULT_REQUIRED_FIELDS exported by engine.bodygraph.v2_adapter; the fixture must satisfy the adapter's current type checks and contain no transport envelope or raw request metadata.
- DB fixture contract:
  - Top-level keys are exactly schema, input_fingerprint, payload, and payload_posture; schema is bodygraph.source_invariance.db_cached_payload.v1 and payload_posture is mapped_no_raw_vendor_payload.
  - payload is an independently authored mapped cache payload containing exactly bodygraph, person, person_uid, and source; source is db_mapped_cache_fixture and the other keys satisfy project_bodygraph.
  - The full canonical vendor and DB fixture hashes must differ even though their projected CanonicalBodyGraph values and Presenter bytes must match.
- Presenter rule: bytes are emitted only by engine.presenter.emitter.emit_public; no projection serializer or alternate emitter is added.
- Durable-data effect: none in PR-04. PR-05 must project mapped configured-v2 data before writing its existing planned cache payload, but PR-05 retains schema choice, write, read-back, idempotence, and authorization work.
- Compatibility: no public route, Reader, CLI, compat, vendor transport, or existing legacy cache behavior changes. The current v2 adapter may keep source metadata in its diagnostic result; only project_bodygraph output is source-neutral.
- Migration: land the module and its focused tests before the v2 evidence producer. PR-05's later plan row must name this API as its input boundary.
- Validation: proposed tests/bodygraph/test_projection.py must cover exact fields, missing/unknown/unsafe rejection, person UID consistency, nonmutation, v2 adapter integration, DB fixture integration, and no-I/O behavior.
- Rollback/fail-closed: if projection validation fails, no source-invariance PASS or release binding may be produced. Reverting the module does not restore the invalid v1 proof as acceptable evidence.
- Downstream effect: PR-05 consumes the type/API later; OPS-01/OPS-02 remain unchanged; PR-06 binds final evidence.
- Plan consequence: amend D9/PR-04 and add a dependency note to D12/PR-05 without moving work.
- Documentation consequence: ADR-CANON-001; later PF02 and PF14 drainage.
- Nonclaims: no durable write, no live read-back, no public contract, no legacy migration, no production authorization, and no PF09 movement.

### RSC-002 - Versioned same-input DB/vendor source-invariance evidence

**Proposed CRD decision.**

- Canon effect: AMENDS.
- Linked CAUSE: CAUSE-002.
- Requested addition: replace the current semantically invalid records in place with independently acquired, source-distinct, two-run, final-byte evidence.
- Sole producer: tools/evidence/generate_bodygraph_policy_proofs.py.
- Primary paths and canonical artifact keys:

| Path | Canonical artifact key | Schema |
| --- | --- | --- |
| artifacts/bodygraph/source_invariance/ab.json | bodygraph.source_invariance.ab | bodygraph.source_invariance.run.v2 |
| artifacts/bodygraph/source_invariance/ba.json | bodygraph.source_invariance.ba | bodygraph.source_invariance.run.v2 |
| artifacts/bodygraph/source_invariance/summary.json | bodygraph.source_invariance.summary | bodygraph.source_invariance.summary.v2 |
| schemas/bodygraph_source_invariance.run.v2.json | bodygraph.source_invariance.schema.run.v2 | JSON Schema 2020-12 |
| schemas/bodygraph_source_invariance.summary.v2.json | bodygraph.source_invariance.schema.summary.v2 | JSON Schema 2020-12 |

- Run-record required fields:
  - schema, captured_at_utc, fixture_id, pair_order, source_order, normalized_input_sha256, acquisitions, predicates, and status.
  - captured_at_utc retains the producer's deterministic evidence epoch 2026-07-14T00:00:00Z; it is not wall-clock time.
  - pair_order is exactly ab or ba.
  - source_order is exactly ["db","vendor"] for AB and ["vendor","db"] for BA.
  - acquisitions contains exactly one DB row and one vendor row in source_order.
  - Each acquisition contains exactly source, adapter_id, source_representation_sha256, payload_posture, and runs.
  - source is the enum db or vendor. adapter_id is mapped_db_cache_payload.v1 for DB and engine.bodygraph.v2_adapter.adapt_v2_chart_payload for vendor. source_representation_sha256 hashes the complete canonical source fixture bytes.
  - runs contains exactly two independently generated entries. Each entry contains acquisition_id, projection_sha256, and emitted_sha256.
  - acquisition_id values must be distinct. Each run reopens and re-deserializes its source fixture, re-runs mapping/projection, and re-emits; run2 may not hash run1 bytes.
  - payload_posture is hashes_only_synthetic_fixture; no raw payload or normalized input is embedded.
  - status is derived PASS only when every run predicate is true; otherwise it is FAIL.
- Run predicates:
  - distinct_sources
  - distinct_source_representations
  - same_normalized_input
  - two_run_stable
  - projection_equal
  - presenter_bytes_equal
  - unsafe_fields_absent
- Summary required fields:
  - schema, captured_at_utc, fixture_id, ab_sha256, ba_sha256, normalized_input_sha256, source_scope, predicates, negative_receipt, proof_labels, and top_level_pass.
  - captured_at_utc and fixture_id equal the run records. ab_sha256 and ba_sha256 hash the complete canonical AB and BA artifact bytes respectively.
  - source_scope is exactly ["configured_v2_chart_result","mapped_db_cache_payload"].
  - predicates are ab_pass, ba_pass, source_order_reversed, same_normalized_input, distinct_sources, distinct_source_representations, db_two_run_stable, vendor_two_run_stable, canonical_projection_equal, presenter_emitted_bytes_equal, unsafe_fields_absent, and negative_control_rejected.
  - top_level_pass is the conjunction of every predicate and may not be written as a constant.
  - proof_labels contains exactly {"name":"BG_SOURCE_INVARIANCE_OK","type":"non_token"}; no acceptance token is claimed.
- Negative receipt:
  - receipt_id is bodygraph_source_invariance_profile_mutation_v1.
  - mutated_source is db.
  - mutated_field is bodygraph.profile.
  - It records baseline_emitted_sha256, mutated_emitted_sha256, expected_failure_code BODYGRAPH_SOURCE_DIVERGENCE, observed_failure_code BODYGRAPH_SOURCE_DIVERGENCE, divergence_detected true, and receipt_sha256.
  - receipt_sha256 is SHA-256 of the canonical negative-receipt object with receipt_sha256 omitted.
  - It contains no raw value.
- Schema posture: additionalProperties is false at every object level; required arrays have exact cardinality; hashes are lowercase 64-character hex; status is PASS or FAIL; unknown keys reject.
- Canonical serialization: engine.serializer.canon.sercanon, UTF-8, no BOM, sorted keys, compact separators, exactly one trailing LF.
- Compatibility and key migration:
  - The three existing primary paths and their established canonical keys remain.
  - Remove duplicate keys epic038.pr04.bodygraph_source_invariance_ab, epic038.pr04.bodygraph_source_invariance_ba, and epic038.pr04.bodygraph_source_invariance_summary.
  - No dual v1/v2 acceptance window exists. Consumers in the same authorized change must require v2.
  - Existing v1 bytes are superseded as evidence, not preserved as a PASS fallback.
- Consumers:
  - tests/evidence/test_bodygraph_policy_proofs.py
  - tools/evidence/generate_release_bindings.py
  - tools/evidence/update_evidence_index.py
  - Human Evidence Index
  - Machine Evidence Index and companion hash/path proofs
  - PR-06 release-sanity orchestration
- Updater-owned companions: all sibling path proofs, docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence_index.jsonl, its checksum, and their path proofs remain solely updater-owned.
- Release-binding effect: artifacts/bodygraph/release_bindings.json keeps schema_version 1 and key epic038.pr01.bodygraph_release_bindings. Its ASCII-sorted binding set is exactly refresh_policy.snapshot.json, source_invariance/summary.json, and source_selection.snapshot.json. The D10 DB-bridge Presenter receipt is intentionally not a BodyGraph source-policy release-binding input.
- Migration order: projection and tests; schemas; producer; three primaries; release binding; updater and companions; check-only validation; PR-06 consumer update.
- Validation: positive AB/BA, independent run acquisition, source-representation distinctness, same-input binding, byte equality, schema closure, canonical bytes, negative mutation, unsafe-field rejection, duplicate-key absence, release-binding freshness, and second-run fixed point.
- Rollback/fail-closed: any partial migration, v1 record, duplicate key, missing source, reused acquisition, missing negative receipt, byte mismatch, unknown field, or stale companion forces nonzero check and top_level_pass false.
- Downstream effect: PR-06 consumes v2. OPS-01 remains the live DB/bridge owner and is not required for this fixture proof. PR-05 remains the persistence owner.
- Plan consequence: amend D9 evidence/validation, D3 binding dependencies, and PR-06 primary requirements.
- Documentation consequence: ADR-CANON-002; later PF12, PF14, PF09.6, and plan drainage.
- Nonclaims: fixture evidence does not prove live vendor access, live DB access, mapped-cache persistence, all vendor versions, token satisfaction, or production behavior.

### RSC-003 - Unique DB-bridge Presenter evidence ownership for PR-04

**Proposed CRD decision.**

- Canon effect: AMENDS.
- Linked CAUSE and revisions: CAUSE-003, REV-001, REV-002.
- Requested addition: repair the complete directly implicated producer graph, separate PR-04's direct-DB-versus-bridge Presenter receipt from the shared historical JSONL family, and enforce one governed producer per primary plus updater-only companions.
- Exact ownership result: the one-row-per-primary ledger in §8 is normative. No retained primary producer may write a primary assigned to another row or any sibling path proof, Human Index, Machine Mirror, checksum sentinel, or orientation companion.
- Legacy generator disposition:
  - tools/evidence/generate_rails_closed_phase1.py is retired from current evidence generation. It is not retained as a whole, split into active owners, or used as a dispatcher.
  - Its path remains for one compatibility window only as a no-write retirement guard. Invocation performs no module-level generation, imports no focused producer for side effects, writes no file, emits the stable diagnostic `RETIRED_EVIDENCE_GENERATOR: use focused generators`, and exits nonzero.
  - Every current executable invocation and source-code assertion is migrated in the same change to the focused owner set. In particular, tests/evidence/test_env_matrix_snapshot_v3.py must stop requiring legacy delegation and instead require the legacy path to have no env-matrix write/delegation side effect.
  - Historical prose, captured grep files, and accepted evidence that merely name the old command remain historical provenance; they are not rewritten or treated as active invocations. Any undiscovered executable call fails visibly at the guard and cannot mutate governed bytes.
- Focused owner allocation:
  - tools/evidence/generate_env_matrix_snapshot.py remains sole owner of artifacts/runtime/env_matrix.snapshot.json.
  - tools/evidence/generate_db_runtime_posture.py owns the DB posture paths and absorbs the legacy-only artifacts/db/partition_plan.txt and artifacts/db/partition_verify.log outputs. It removes both environment-connectivity paths from its write set.
  - tools/evidence/generate_db_bridge_parity.py owns adapter selection, capabilities, provider parity, both environment-connectivity paths, its two synthetic fixture primaries, and the dedicated PR-04 Presenter receipt. It removes the shared Presenter path and PRESENTER_BASE_RECORDS.
  - tools/evidence/generate_bodygraph_policy_proofs.py remains sole owner of BodyGraph source-selection, source-invariance, refresh-policy, metrics, and keys-only primaries.
  - tools/evidence/generate_rails_gate_evidence.py remains sole owner of artifacts/proofs/ops_refusal_proof.txt.
  - proposed tools/evidence/generate_presenter_history.py is sole owner of the shared Presenter primary and writes no other path.
  - tools/evidence/update_evidence_index.py remains sole owner of all sibling path proofs, Human Index, Machine Mirror, checksum sentinels, and orientation/index companions.
- Shared historical path retained:
  - Path: artifacts/presenter/json_canon_compare.log.
  - Canonical artifact key: presenter.bodygraph.json_canon_compare.
  - Sole governed producer: proposed tools/evidence/generate_presenter_history.py.
  - Authoritative source: proposed repo source fixture tools/evidence/fixtures/presenter/json_canon_compare.history.v1.json. This is immutable generator input, not a governed acceptance artifact, has no Machine Mirror key, and may change only through an independently reviewed historical-evidence migration.
  - Source contract: canonical JSON with exact top-level keys schema, records, and output_sha256; schema is presenter.history_source.v1; records is an ordered four-element array; each element has exactly record_id, payload, and payload_sha256; output_sha256 is the digest of the four emitted canonical payload lines including each LF.
  - Exact record order and identities are `epic011_s10_rails_closed_match`, `epic011_s10_diff`, `epic011_live_match_a`, and `epic011_live_match_b`.
  - Exact canonical row hashes, including each trailing LF, are respectively 601c48f5a1d57a15e769d34fe02ae9ada830e3e46256e0c66e596cf6d4f8102a, 44be55631c71a7717fea11cca56f18c4c389dfc661949ec20626085001d55489, ea2ba6b4097770b6075c9b6b905c9a227f455db1bc47c248858cd8d7d4484cc5, and e44b9f222b34335488de917d452f21b2720f655e6545f48672085154687c0cf5.
  - Exact four-line output length is 1559 bytes and exact output SHA-256 is 64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c.
  - The exact payloads copied once from the approved current first four rows into the source fixture are:

```json
{"at":"2025-11-18T05:24:24Z","db_emitted_sha256":"a0f5c8a94da6df5a0f9fb0e4d0de394381f65c4593cdb95c5f0cfa7a39f7c4b1","input_fingerprint":"stub-db-payload","match":true,"notes":"deterministic stub payload compared under rails closed","schema":"v1","user_id":"epic011-s10-invariance-1","vendor":"hdapi","vendor_sha256":"a0f5c8a94da6df5a0f9fb0e4d0de394381f65c4593cdb95c5f0cfa7a39f7c4b1","vendor_version":"offline"}
{"at":"2025-11-20T01:10:21Z","compare":"DIFF","left_path":"artifacts/bodygraph/vendor_upsert.epic011-s10-invariance-1.json","left_sha256":"fa0baad03333ad1d03fde339a9ce25ebd5289431afc57edd3b220706d11d37c4","match":false,"right_path":"artifacts/bodygraph/db_resolve.epic011-s10-invariance-1.json","right_sha256":"5226051a12100ae06a91e17ed3264afba177708f18424666c1aefd4d85f395aa"}
{"at":"2026-03-01T02:32:34Z","db_emitted_sha256":"34f18c26416ce920f5a346b9ea1c730bff6210b6f1bc21aa57d3338c18d42eef","input_fingerprint":"a050279aa87c66070c04b4276b42428ed0621463d878d1fd5e09c32b2295442d","match":true,"user_id":"d8b2ce05-d2a8-5b91-8821-a894d20dd22c","vendor":"hdapi","vendor_sha256":"34f18c26416ce920f5a346b9ea1c730bff6210b6f1bc21aa57d3338c18d42eef","vendor_version":1}
{"at":"2026-03-01T02:32:36Z","db_emitted_sha256":"c8771cc1827261ef4264afd96bd2610bbe401f81c493b6710e7e045ccff5be14","input_fingerprint":"12970e0e4f417cc4e6ecbe2a2cd0dc9a347c0906e47adeeaef61bc469485179c","match":true,"user_id":"2d31ea34-c2d9-5103-9cf0-fc845565050d","vendor":"hdapi","vendor_sha256":"c8771cc1827261ef4264afd96bd2610bbe401f81c493b6710e7e045ccff5be14","vendor_version":1}
```

- Shared-log producer contract:
  - Materialization reads the fixture fresh, rejects any unknown/missing key, duplicate record_id, wrong count/order, payload/hash mismatch, output length mismatch, or output hash mismatch before opening a destination temporary file.
  - It emits each payload only through engine.serializer.canon.sercanon and requires one canonical UTF-8 JSON object plus exactly one LF per row. It never reads the wall clock, environment-dependent evidence, or the current destination to construct expected rows.
  - Normal mode writes only the shared primary through a same-directory temporary file, flushes and fsyncs it, and replaces the destination atomically only after every preflight predicate passes. A preflight or temporary-write failure leaves the previous destination unchanged; temporary residue is removed.
  - `--check` is read-only and compares the recomputed 1559 expected bytes with the destination, exact row count/order, and expected digest. Missing, extra, changed, noncanonical, provisional PR-04, or wall-clock-derived rows fail nonzero.
  - The producer does not create or update a sibling path proof, index, checksum, or other companion. Only update_evidence_index.py does so after all primaries are final.
  - A second materialization followed by `--check` is a byte fixed point; file bytes and hash remain exactly unchanged.
- Operational append posture:
  - engine/bodygraph/ingest.py and presenter/json_canon_compare.py must not default to the governed shared path.
  - Their log-path parameter becomes explicit; when omitted, comparison still executes but no governed file is mutated.
  - Tests needing diagnostic JSONL use a temporary caller-supplied path.
  - This changes internal diagnostic persistence defaults only, not public bytes or ingest parity results.
- Dedicated PR-04 primary:
  - Path: artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json.
  - Artifact key: epic038.pr04.presenter_db_bridge_compare.
  - Schema ID: presenter.db_bridge_compare.v1.
  - Schema path: schemas/presenter_db_bridge_compare.v1.json.
  - Schema artifact key: epic038.pr04.presenter_db_bridge_compare_schema.
  - Sole producer: tools/evidence/generate_db_bridge_parity.py.
- Direct and bridge acquisition contract:
  - Reuse the existing ordered deterministic harness case corpus exactly: select_one, search_path, version, and tx_select_one. No new DB query or fixture family is introduced.
  - The existing HarnessProvider-backed direct and bridge DBAccess façades are invoked independently for every case. Direct and bridge values are normalized separately into ordered arrays of exactly {name,value} records before Presenter emission.
  - case_corpus_sha256 is the canonical SHA-256 of the ordered case-name array ["select_one","search_path","version","tx_select_one"]. SQL text and parameters are not copied into governed evidence.
  - Each active side must be available, non-skipped, non-error, and have a distinct acquisition_id.
  - Each provider's complete normalized case array is emitted once by engine.presenter.emitter.emit_public.
  - The dedicated record contains hashes and bounded case counts only; it contains no SQL text, parameters, case values, connection values, raw payloads, or secrets.
- Dedicated record required fields:
  - schema, captured_at_utc, fixture_id, case_corpus_sha256, provider_parity_path, provider_parity_sha256, direct, bridge, predicates, negative_receipt, payload_posture, and status.
  - schema is presenter.db_bridge_compare.v1; captured_at_utc retains the producer's deterministic evidence epoch 2026-05-18T00:00:00Z; fixture_id is hde_epic038_pr04_fixture_corpus_v1; provider_parity_path is artifacts/db_bridge/provider_parity.proof.json.
  - direct and bridge each contain provider, acquisition_id, availability, case_count, and emitted_sha256. Provider values are direct_db and db_bridge; acquisition_id values are direct-db-acquisition-01 and db-bridge-acquisition-01; availability is available only after all four independent case invocations succeed.
  - predicates are same_case_corpus, direct_available, bridge_available, active_cases_complete, case_count_equal, presenter_bytes_equal, unsafe_fields_absent, and negative_control_rejected.
  - status is derived PASS only when every predicate is true and provider_parity_sha256 matches artifacts/db_bridge/provider_parity.proof.json.
  - payload_posture is hashes_and_counts_only_no_case_values.
- Negative receipt:
  - receipt_id is db_bridge_case_mutation_v1.
  - mutated_side is bridge.
  - mutated_case is tx_select_one; the negative run changes only that normalized bridge value after acquisition and before Presenter emission.
  - It records baseline_emitted_sha256, mutated_emitted_sha256, expected_failure_code DB_BRIDGE_PARITY_DIVERGENCE, observed_failure_code DB_BRIDGE_PARITY_DIVERGENCE, divergence_detected true, and receipt_sha256.
  - receipt_sha256 is SHA-256 of the canonical receipt object excluding receipt_sha256.
- Schema posture: additionalProperties is false at every object level; hashes are lowercase 64-character hex; canonical serialization is sercanon with exactly one LF.
- Focused validation locus: proposed tests/evidence/test_presenter_evidence_ownership.py covers the dedicated schema, direct/bridge predicates and negative mutation, shared-log ownership, producer-order independence, unique path/key binding, and check-mode read-only behavior.
- Key migration:
  - Remove epic038.pr04.presenter_json_canon_compare from the shared path.
  - Retain presenter.bodygraph.json_canon_compare for the shared path.
  - Add the dedicated path/key and schema path/key.
- Consumer migration: proposed tests/evidence/test_presenter_evidence_ownership.py, the PR-04/PR-06 plan evidence inventory, updater, Human/Machine indexes, and PR-06 consume the dedicated JSON receipt. The BodyGraph release binding does not consume it because it is a D10 DB-bridge proof, not a D9 source-policy input. Historical consumers of the shared log remain on the unchanged shared path and exact four-row bytes.
- Historical treatment: no historical row is copied into PR-04 code or a broad producer. The source fixture is the sole reconstruction authority. The provisional fifth PR-04 row is removed by generating exactly the four approved payloads; it survives only in git history and is not migrated into the shared family.
- Compatibility: shared path, four historical payloads, row order, canonical bytes, and canonical key remain available to historical consumers. PR-04 changes to a task-specific path. Current executable references to the broad generator migrate to the focused owner set; historical references remain provenance. No public API changes.
- Atomic migration:
  1. Add the immutable source fixture, selective history producer, source-contract tests, and expected output digest without changing the shared destination.
  2. Add focused ownership/write-set tests and move partition outputs, capability snapshot, environment-connectivity, and rails/bodygraph primaries to the §8 owners; remove every overlapping write and every direct path-proof write from the legacy code.
  3. Remove PRESENTER_BASE_RECORDS and the shared path from generate_db_bridge_parity.py; add and materialize the dedicated PR-04 receipt.
  4. Atomically materialize the four-row shared body from the fixture, removing only the provisional fifth row.
  5. Convert the legacy command to the no-write retirement guard; update active invocation/source assertions; remove PR-specific duplicate key rows.
  6. Run every focused materializer, then the updater once, every focused check, the updater check, producer-permutation tests, and a second shared materialization/check. Publication is all-or-nothing: any failure blocks the migration and PR-04 remains non-PASS.
- Validation: in isolated copies, run all retained primary producers in every allowed permutation before one updater pass. Each producer's declared write set must be exact; no producer may change another row's primary or any companion; all permutations must converge to identical final primary bytes; the four-row shared digest must remain exact; the dedicated bytes must remain exact; the provisional row and replay constants must be absent; both active DB providers must be complete; the negative mutation must fail; current keys must be unique; and updater normal/check cycles must reach a fixed point.
- Rollback/fail-closed: the authoritative rollback body is the 1559-byte four-row output regenerated from the immutable source fixture and verified against its digest. If failure occurs before atomic replacement, the old destination remains untouched. If failure occurs after replacement, atomically restore only that verified four-row body, remove the dedicated primary/key/schema and any partially registered rows, run the updater to coherent companions, and leave PR-04 DB-bridge Presenter parity non-PASS. Never execute or restore the broad legacy writer, provisional PR-04 row, or replay constants.
- Downstream effect: PR-06 changes one required path; OPS-01 retains its own live direct/bridge evidence; no historical work is reopened.
- Plan consequence: replace artifacts/presenter/json_canon_compare.log in the PR-04/PR-06 D10 inventory with the dedicated path; replace active broad-generator steps with the focused owner sequence; retain the shared path as historical evidence outside PR-04 ownership; make updater execution follow all primary materializers.
- Documentation consequence: ADR-CANON-003; later PF09.6 HDE-DIST001.9, PF12 §8.3 and catalog/key rows, PF14 §1.3.1, and PF27 collision/final-generator guardrail drainage.
- Nonclaims: no live DB or bridge parity, no deletion or reapproval of historical evidence, no conversion of the shared log into a PR-04 truth home, no blanket historical-evidence migration, no QA or OPS rerun, no PF09 movement, and no implementation completion.

## 8. Ownership and Boundary Effects

### Ownership disposition

| Surface or owner | Work moved into PR-04 | Work retained or remaining elsewhere | Status and nonclaim boundary |
| --- | --- | --- | --- |
| PR-04 / D9 / HDE-DIST001.5 | Pure projection boundary and v2 source-invariance schemas and proofs | Live DB/vendor facts remain outside PR-04 | HDE-DIST001.5 remains Partial; no token or completion claim |
| Historical HDE-DIST001.7 evidence | Status-neutral replacement of invalid current bytes at the established AB/BA/summary paths | Historical implementation and prior acceptance are not reopened | HDE-DIST001.7 remains Done |
| PR-04 / D10 / HDE-DIST001.9 | Dedicated direct-DB/bridge Presenter receipt and producer/key separation | OPS-01 retains live direct/bridge posture and row-level evidence; PR-06 retains final binding | HDE-DIST001.9 remains Partial |
| PR-04 / D11 / HDE-DIST001.10 | Correct the route analyzer and fail-closed verdict inside existing scope | PR-06 retains final evidence binding | HDE-DIST001.10 remains Partial |
| PR-01 / D3 / HDE-DIST002.5 | No implementation is moved; the existing release-binding derivative is refreshed because its inputs change | PR-01 stays historical; PR-06 retains final release sanity | HDE-DIST002.5 remains Not done; no PR-01 reopening |
| PR-05 / D12 / HDE-DIST001.11 | No persistence work moves into PR-04; PR-04 defines the projection input contract PR-05 must consume | PR-05 owns mapped writes/read-back/idempotence; OPS-02 owns controlled live proof | HDE-DIST001.11 remains Optional |
| OPS-01 | None | Live read-only DB/bridge observation after PR-04 | No OPS execution or completion claim |
| OPS-02 | None | Controlled configured-v2 mapped-cache proof after PR-05 | No OPS execution or completion claim |
| PR-06 | None | Final orchestration, all primary checks, OPS package validation, release binding, and close-oriented evidence binding | No PR-06 completion claim |
| Canonical updater | No semantic product work; register final primary paths and remove duplicates | Sole owner of Human Index, Machine Mirror, hash sentinels, and path proofs | No producer may write updater-owned companions |
| Historical Presenter owner | Add one selective source-manifest-backed generator for the shared four-row JSONL | PR-04 leaves that family and receives a dedicated primary | Historical bytes remain exact; no replay constants or status movement |
| Legacy Rails Closed Phase 1 generator | Retire from current generation and retain only a no-write failure guard while active invocations migrate | Historical prose/evidence mentions remain provenance | Owns no governed output; no historical rerun or rewrite claim |

Evidence pointer: PF09.6-Canon-HDE-Build-Checklist-Distillation | HDE-DIST001.5, .7, .9, .10, .11 and HDE-DIST002.5 | Current statuses are Partial, Done, Partial, Partial, Optional, and Not done respectively.

Evidence pointer: Implementation Plan | r6 Implementation Plan HDE-EPIC038, Execution plan items 4 through 8 | PR-04 covers D8-D11; OPS-01 follows PR-04; PR-05 owns D12; OPS-02 follows PR-05; PR-06 depends on PR-01 through PR-05 and both OPS tasks.

### One-row-per-governed-primary ownership ledger after adoption

The following ledger is the complete disposition of every primary directly written by the broad legacy generator, both environment-connectivity primaries written by two focused PR-04 generators, and the task-specific Presenter replacement. `Canonical key` is the one current Machine Mirror key retained for the physical path. PR-specific duplicate current keys are removed; historical acceptance reports remain unchanged and may cite the canonical path without owning a second current Mirror row.

| Governed primary | Sole post-adoption producer | Canonical key | Displaced writer treatment | Direct consumers and migration consequence |
| --- | --- | --- | --- | --- |
| artifacts/runtime/env_matrix.snapshot.json | tools/evidence/generate_env_matrix_snapshot.py | runtime.env_matrix.snapshot | Legacy delegation removed; legacy guard writes nothing | Snapshot tests and updater call/check the focused producer directly |
| artifacts/db/check_schema.txt | tools/evidence/generate_db_runtime_posture.py | db.check_schema | Legacy direct write removed; epic038.pr04.db_check_schema duplicate current key removed | DB posture tests, updater, PR-06 |
| artifacts/db/ddl_fingerprint.json | tools/evidence/generate_db_runtime_posture.py | db.ddl_fingerprint | Legacy direct write removed; epic038.pr04.db_ddl_fingerprint removed | DB posture tests, updater, PR-06 |
| artifacts/db/grants.txt | tools/evidence/generate_db_runtime_posture.py | db.grants | Legacy direct write removed; epic038.pr04.db_grants removed | DB posture tests, updater, PR-06 |
| artifacts/db/boundary_view.readonly.proof.txt | tools/evidence/generate_db_runtime_posture.py | db.boundary_view.readonly_proof | Legacy direct write removed; epic038.pr04.db_boundary_view_readonly removed | DB posture tests, updater, PR-06 |
| artifacts/db/partition_plan.txt | tools/evidence/generate_db_runtime_posture.py | db.partition.plan | Moved from retired legacy generator; bytes retained unless focused source derivation proves an approved deterministic refresh | Historical DB evidence consumers, focused tests, updater |
| artifacts/db/partition_verify.log | tools/evidence/generate_db_runtime_posture.py | db.partition.verify | Moved from retired legacy generator under the same byte-preservation rule | Historical DB evidence consumers, focused tests, updater |
| artifacts/db_bridge/adapter_selection.snapshot.json | tools/evidence/generate_db_bridge_parity.py | db_bridge.adapter_selection.snapshot | Legacy direct write removed; epic038.pr04.db_bridge_adapter_selection removed | ci/checks/check_bridge_consistency.py, focused tests, updater, PR-06 |
| artifacts/db_bridge/caps.snapshot.json | tools/evidence/generate_db_bridge_parity.py | db_bridge.caps.snapshot | Moved from retired legacy generator; derived deterministically from the same fixture bridge capability used by provider parity | Bridge consistency/focused tests, updater, PR-06 |
| artifacts/runtime/env_connectivity.snapshot.json | tools/evidence/generate_db_bridge_parity.py | runtime.env_connectivity | Removed from generate_db_runtime_posture.py and legacy generator; epic038.pr04.env_connectivity removed | ci/checks/check_bridge_consistency.py consumes it with adapter selection and provider parity; updater and PR-06 retain it |
| artifacts/runtime/env_connectivity.nondev_failure.json | tools/evidence/generate_db_bridge_parity.py | epic032.pr04.env_connectivity_nondev_failure | Removed from generate_db_runtime_posture.py and legacy generator; epic038.pr04.env_nondev_failure removed | Non-dev failure tests, updater, PR-06; prior EPIC032 evidence meaning is not reopened |
| artifacts/bodygraph/source_selection.snapshot.json | tools/evidence/generate_bodygraph_policy_proofs.py | bodygraph.source_selection | Legacy direct write removed; epic038.pr04.bodygraph_source_selection removed | Release binding, BodyGraph tests, updater, PR-06 |
| artifacts/bodygraph/metrics.snapshot.json | tools/evidence/generate_bodygraph_policy_proofs.py | bodygraph.refresh_metrics | Legacy direct write removed; epic038.pr04.bodygraph_metrics removed | BodyGraph tests, updater, PR-06 |
| artifacts/bodygraph/keys_only.logs.sample | tools/evidence/generate_bodygraph_policy_proofs.py | bodygraph.refresh_logs | Legacy direct write removed; epic038.pr04.bodygraph_keys_only_logs removed | BodyGraph tests, updater, PR-06 |
| artifacts/proofs/ops_refusal_proof.txt | tools/evidence/generate_rails_gate_evidence.py | ops.rails_refusal | Legacy direct write removed; duplicate current alias ops.refusal_proof removed | Rails-gate tests, historical rails consumers, updater; no OPS rerun |
| artifacts/presenter/json_canon_compare.log | tools/evidence/generate_presenter_history.py | presenter.bodygraph.json_canon_compare | Legacy direct write and DB-bridge replay removed; epic038.pr04.presenter_json_canon_compare removed | Historical consumers remain on exact four-row bytes; focused ownership tests and updater check them |
| artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json | tools/evidence/generate_db_bridge_parity.py | epic038.pr04.presenter_db_bridge_compare | New task-specific replacement for the provisional fifth shared row | Focused tests, updater, PR-06; excluded from BodyGraph release binding |
| every governed `*.path_proof.txt`, docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence_index.jsonl, its checksum, and orientation/index companions | tools/evidence/update_evidence_index.py | Existing updater-owned keys | `_write_path_proof` and every direct companion write are removed from the retired legacy generator and forbidden in all primary producers | Mirror/path validators and PR-06; updater runs only after all primaries, then converges in check mode |

The focused DB-runtime producer also remains sole owner of artifacts/db/check_constraints.txt; the focused DB-bridge producer remains sole owner of artifacts/db_bridge/provider_parity.proof.json and the two PR-04 synthetic BodyGraph fixtures; and the focused BodyGraph producer remains sole owner of source-invariance and refresh-policy primaries. Those paths were not directly written by the legacy generator and their existing ownership is unchanged.

Allowed-order contract: the six retained primary materializers—env matrix, DB runtime, DB bridge, BodyGraph policy, rails gate, and Presenter history—may run in any permutation because their declared write sets are disjoint. Running any one may change only its ledger rows and may not change another primary or any companion. The updater is not permuted with primary materializers: it runs once after all primaries, and its `--check` must then be a fixed point. Every retained producer `--check`, including the shared-history check, is read-only.

### Boundaries explicitly unchanged

- D8/HDE-DIST001.4 DB runtime posture remains original PR-04 scope.
- Public Reader, CLI, compat, and route contracts remain unchanged.
- No second Presenter or serializer is created.
- No configured-v2 durable write, database schema migration, live read-back, idempotence claim, or production write authorization moves from PR-05/OPS-02.
- No live vendor, DB, bridge, or infrastructure work moves from OPS-01/OPS-02.
- No historical PF09 row is reopened or reapproved.
- No PF09 status changes occur.

## 9. Implementation Requirements and Plan Consequences

### Source-grounded technical requirements

1. Implement RSC-001 exactly as a pure mapped-payload projection. It must not parse raw vendor transport envelopes, emit public bytes itself, or perform I/O.
2. Extend tools/evidence/generate_bodygraph_policy_proofs.py so each of DB and vendor is acquired twice by reopening and re-deserializing its distinct fixture, then independently mapped/projected/emitted.
3. Bind both sources to the canonical SHA-256 of the same normalized-input fixture. Source representation hashes must differ; canonical projection and Presenter hashes must match.
4. Generate AB as DB then vendor and BA as vendor then DB. Summary comparison must key acquisitions by source and must not infer equality from array order alone.
5. Generate and validate the negative mutation receipt. PASS is derived only from every decisive predicate.
6. Use the current canonical serializer and Presenter. No json.dumps evidence serializer is added for these JSON primaries.
7. Apply the §8 ledger exactly. Remove every named PR-specific or duplicate current Machine Mirror key before updater dedupe; preserve the selected canonical key and historical source artifacts without creating a second current binding.
8. Retire tools/evidence/generate_rails_closed_phase1.py as the exact no-write failure guard in RSC-003. Remove its module-level generation, wall-clock dependence, env-matrix delegation, primary writes, and direct path-proof writes. Migrate every active invocation/source assertion to focused owners in the same change.
9. Move partition_plan.txt and partition_verify.log into generate_db_runtime_posture.py; remove environment-connectivity from that producer. Move caps.snapshot.json and both environment-connectivity primaries into generate_db_bridge_parity.py. Remove all overlapping legacy writes.
10. Implement tools/evidence/generate_presenter_history.py and its exact four-row source manifest, hashes, selective write/check interface, and atomic/fail-closed behavior from RSC-003. Remove PRESENTER_BASE_RECORDS, the provisional shared row, and implicit governed-path defaults from diagnostic appenders.
11. Generate the dedicated DB-bridge Presenter receipt from independently queried direct and bridge fixture providers, bind the exact provider-parity artifact hash, and derive PASS from every required predicate and negative control.
12. Enforce declared write sets mechanically. Each primary generator must fail a focused test if it writes outside its §8 rows; all retained primary generators must converge under every allowed permutation; none may write a companion.
13. Expand the existing release binding without changing its artifact identity or schema_version. Bind final paths in ASCII path order and regenerate only after all three inputs are final.
14. Keep check modes read-only. A missing, stale, v1, duplicate-key, unknown-field, unsafe, noncanonical, wrong-row, wrong-owner, cross-family-write, or predicate-failing artifact returns nonzero.

### Retained-scope architecture analyzer correction

BUG-002 must be corrected without a new RSC:

- Build a symbol table for names assigned from Flask(...) and Blueprint(...).
- Recognize route decorators only when the decorator receiver is a known Flask or Blueprint symbol and the attribute is route, get, post, put, patch, delete, head, or options.
- Recognize add_url_rule calls on known route-owner symbols.
- Recognize register_blueprint calls and bind the registered Blueprint symbol to its route declarations.
- Do not classify ordinary mapping.get or client.get calls as route declarations.
- Record any decorator or registration call with a route-like form but an unclassified receiver as unknown.
- Compute unknown_count from analyzer results.
- Compute analyzer_verdict as fail when any forbidden or unknown row exists; otherwise pass.
- Render verdict only from analyzer_verdict. The renderer may not hard-code pass or zero unknowns.
- Extend tests/evidence/test_architecture_snapshot.py to require adapter/wsgi.py, its healthz and readyz method decorators, registered engine blueprints, no ordinary-get false positive, and unknown-form FAIL.

### Retained-scope release-binding correction

BUG-004 must be corrected through the existing producer:

- Keep artifacts/bodygraph/release_bindings.json, schema_version 1, and artifact key epic038.pr01.bodygraph_release_bindings.
- Bind exactly these final primaries in ASCII path order: artifacts/bodygraph/refresh_policy.snapshot.json; artifacts/bodygraph/source_invariance/summary.json; artifacts/bodygraph/source_selection.snapshot.json.
- Record exact path, SHA-256, and size for each.
- Extend tests/evidence/test_release_bindings.py to reject a missing path, stale size/hash, unsorted binding list, and any generation before source-invariance finalization.
- Treat this as dependency maintenance. It does not reopen or reapprove PR-01.

### Plan-consequence matrix

| Affected deliverable / owner / PF09 status | Current plan baseline | CRD decision and affected components | Evidence and validation change | Dependency, order, updater, and release effect | Retained owner and exclusions |
| --- | --- | --- | --- | --- | --- |
| D8 / PR-04 / HDE-DIST001.4 Partial | DB posture plus environment-connectivity evidence | Keep DB posture, absorb partition plan/verify, and remove env-connectivity from DB-runtime producer; bridge producer becomes sole env owner | Add exact-write-set, deterministic-byte, no-companion, and producer-permutation checks | Retire broad legacy writer; focused owners materialize before updater | PR-04 retains D8; no live DB, prior-slice reopening, or status movement |
| D9 / PR-04 / HDE-DIST001.5 Partial | Source selection, AB/BA source invariance, refresh policy, metrics, keys-only logs | Add projection.py; replace v1 AB/BA/summary with v2; add fixtures and schemas | Add independent acquisitions, two-run checks, final-byte equality, negative mutation, schema and canonical-byte checks | Projection precedes primary generation; release binding follows; updater runs after final primaries | PR-06 retains final binding; no live source or token claim |
| Historical HDE-DIST001.7 Done | Historical same-input DB/vendor Presenter-byte invariant | Reuse the contract; refresh current invalid evidence at established paths | Status-neutral proof maintenance only | No implementation dependency or PF09 movement | Historical owner remains closed; no reapproval |
| D10 / PR-04 plus OPS-01 and PR-06 / HDE-DIST001.9 Partial | Shared Presenter log plus DB/bridge and env evidence | Replace PR-04 shared-log dependency with dedicated direct/bridge receipt; make DB-bridge sole owner of adapter/caps/provider/env/receipt rows; retire broad writer | Add same-query direct/bridge Presenter parity, negative mutation, exact write-set, order independence, dedicated schema, and bridge-consistency checks | Receipt is not a release-binding input; updater follows all primary materializers and removes duplicate keys | OPS-01 retains live DB/bridge rows; no live rerun |
| Historical Presenter evidence / no PF09 status move | Shared five-row file at PR head and broad/PR-04 competing writers | New selective history owner reproduces only the approved first four rows from immutable source manifest; fifth PR-04 row moves to dedicated receipt | Exact 1559-byte body/hash, per-row hashes/order, no clock, read-only check, atomic-failure, second-run fixed-point tests | Shared history materializes before updater; all other producers are forbidden from the path | Historical consumers and bytes retained; no reapproval, rerun, or deletion claim |
| D11 / PR-04 and PR-06 / HDE-DIST001.10 Partial | Keys-only architecture snapshot, fail-closed unknowns | Retained-scope AST taxonomy and analyzer-derived verdict | Require @app.get coverage, registration binding, false-positive rejection, unknown FAIL | Analyzer correction precedes artifact regeneration; updater follows | No new route or architecture family |
| D3 / historical PR-01 and PR-06 / HDE-DIST002.5 Not done | Release binding ties release identity to BodyGraph source and refresh policy | Keep artifact identity; add v2 source-invariance summary dependency | Exact path/hash/size and sorted-order checks | Generate after all three BodyGraph inputs, before updater; PR-06 validates | PR-01 not reopened; no status movement |
| D12 / PR-05, OPS-02, PR-06 / HDE-DIST001.11 Optional | Configured-v2 mapped-cache write/read-back and idempotence | Consume CanonicalBodyGraph/project_bodygraph as the approved pre-write mapping boundary | Later PR-05 tests prove persistence; PR-04 proves only pure projection | PR-05 still depends on PR-04; no persistence is pulled forward | PR-05/OPS-02 retain all durable/live work |
| PR-06 / HDE-DIST001.5, .9, .10 and .11 | Final release sanity and evidence binding | Require v2 schemas/primaries, dedicated receipt, unique keys, final release binding, corrected architecture artifact | Reject v1, duplicate keys, missing negative receipt, stale binding, unknown route forms | Consume only after PR-04, PR-05, OPS-01, and OPS-02 according to revised plan | No PR-06 execution or close claim in this CRD |

The later authorized plan revision must replace the PR-04 and PR-06 references to artifacts/presenter/json_canon_compare.log with the dedicated PR-04 receipt while retaining that shared path in selective historical ownership. It must replace every active broad-generator step with the six focused primary owners followed by the updater; add the §8 ownership ledger, legacy retirement guard, source-manifest migration, projection and v2 schema loci, exact keys, migration order, negative controls, order-permutation checks, and release-binding dependencies. D8's deliverable meaning is unchanged even though its producer allocation is corrected. The plan must not move D12 or add OPS commands.

### Adoption and evidence-generation order

1. Adopt ADR-CANON-001 through ADR-CANON-003 through IA approval of this CRD.
2. Revise the Current Implementation Plan under separate authorization.
3. Add projection type/API, fixture contracts, and focused unit tests.
4. Add closed v2 source-invariance schemas, the dedicated DB-bridge Presenter schema, the immutable four-row Presenter-history source manifest, and the selective history producer/tests. Do not replace the shared destination yet.
5. Refactor the focused DB, bridge, BodyGraph, and rails-gate producers to the exact §8 write sets; move partition/capability/environment outputs; remove all direct path-proof writes; add write-set and permutation tests.
6. Update the BodyGraph producer and generate AB, BA, and summary.
7. Remove shared-history replay from the DB-bridge producer, generate its dedicated Presenter receipt, remove implicit governed-path append defaults, then atomically materialize the four-row shared JSONL from its source manifest.
8. Convert generate_rails_closed_phase1.py to the no-write retirement guard and migrate every active invocation/source assertion. Do not restore the broad writer as a fallback.
9. Correct the route analyzer and regenerate the architecture primary/schema if its schema changes.
10. Generate the release binding after every bound input has final bytes.
11. Remove the named duplicate current keys and run the canonical updater once to produce all companions.
12. Run producer checks, source-manifest/hash checks, schema/canonical-byte checks, path/mirror validation, release-binding checks, exact write-set tests, every allowed primary-producer permutation, atomic-failure tests, and focused tests without retaining writes.
13. Materialize/check the shared history a second time, then run the updater in check/fixed-point mode only. Final bytes, keys, and companions must be unchanged.
14. Hand the final primary inventory to PR-06; do not execute OPS or QA in this slice.

### Rollback stops

- Do not publish or preserve PASS if projection, source acquisition, schema, negative control, or Presenter equality fails.
- Do not permit a mixed v1/v2 family.
- Do not permit both canonical and PR-specific keys for one physical path.
- Do not allow any generator except the canonical updater to write path proofs or evidence indexes.
- Do not allow a partial collision migration to fall back to replay constants.
- Do not allow the retired broad generator to materialize or dispatch any evidence family.
- Do not accept a shared Presenter body unless it contains exactly the four approved rows, 1559 bytes, and SHA-256 64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c.
- Do not accept a primary producer whose observed write set exceeds its §8 ledger rows or whose execution changes another family or any companion.
- Do not regenerate the release binding before all bound primary bytes are final.
- If implementation must be reverted, restore the shared log only from the immutable four-row source manifest through atomic replacement, remove the dedicated PR-04 family and partial current bindings, reconverge companions through the updater, and leave PR-04 source-invariance and DB-bridge Presenter parity unclaimed until a coherent replacement exists.

### Exclusions

No commands, patches, runbook, database transaction, migration, live vendor call, live DB/bridge call, QA execution, OPS execution, deployment, public API change, PF09 move, acceptance claim, or closeout is authorized here.

## 10. PF-Canon, ADR, PF09.x, and PF10 Consequences

### ADR-CANON-001 - Source-neutral BodyGraph projection boundary

- ADR ID: ADR-CANON-001.
- Title: Source-neutral BodyGraph projection boundary.
- Status: PROPOSED - PENDING IA TECHNICAL APPROVAL.
- Linked IDs: BUG-001, CAUSE-001, RSC-001.
- Canon effect: EXTENDS.
- Current PF-Canon contract:
  - PF02-Canon-HDE-Architecture, §6.2 Vendor seam (concept only): vendor responses are normalized into BodyGraphs/internal structures; Core sees normalized data; engine/bodygraph is the allowed non-core I/O seam; public bytes use the single Presenter.
  - PF02-Canon-HDE-Architecture, §5.4 Evidence & determinism flows (concept only): offline proof uses existing behavior and no alternate runtime or emitter.
  - PF14-Canon-HDE-Mechanics-Guide, §Source invariance (single presenter/emitter): same-input DB/vendor output must be byte-identical.
- Observed Repo reality: v2_adapter.py maps ChartResult into HDE-shaped data and adds source metadata; ingest.py contains a live emit/write/read/emit comparison; no exact CanonicalBodyGraph or project_bodygraph implementation exists.
- Problem: PR-04 lacks a pure shared domain that both source representations can enter without live persistence or duplicated generator mapping.
- Alternatives considered:
  1. Use legacy ingest wholesale - rejected for live I/O, legacy persistence, and dry-run self-hash.
  2. Compare current adapter dictionaries directly - rejected because source metadata and shape differences remain and no stable boundary is established.
  3. Strip fields inside the evidence generator - rejected as proof-only duplicate architecture.
  4. Add the pure projection described in RSC-001 - selected.
- Selected decision: add engine/bodygraph/projection.py with CanonicalBodyGraph, BodyGraphFields, BodyGraphProjectionError, and project_bodygraph().
- Minimum-scope rationale: one pure function reuses existing mapped data and Presenter, solves the proof-domain gap, and gives PR-05 a stable input without moving persistence.
- Exact implementation owner and locus: PR-04 implementation owner; engine/bodygraph/projection.py; proposed tests/bodygraph/test_projection.py.
- Exact API decision: project_bodygraph(mapped: Mapping[str, Any]) -> CanonicalBodyGraph with exact fields and errors defined in RSC-001.
- Affected boundaries: mapped configured-v2 adapter output, deterministic DB fixture input, PR-04 evidence, later PR-05 pre-write input.
- Unchanged boundaries: public Reader/CLI/compat; vendor transport; legacy v1 ingest persistence; DB schema; production authorization.
- Source-adapter scope: configured-v2 ChartResult through existing adapt_v2_chart_payload and mapped DB cache payload fixture only.
- Persistence and durable-data effect: no PR-04 persistence. PR-05 later persists only the projected mapped payload under its existing ownership.
- Compatibility: current diagnostic adapter result may retain source metadata; projection output never does.
- Migration: land and test projection before evidence v2; later revise PR-05 dependency text.
- Producer and consumer ownership: projection is production-owned pure code; BodyGraph producer and later PR-05 consume it; Presenter remains sole emitter.
- Validation: exact shape, no I/O, nonmutation, source stripping, unsafe/unknown rejection, UID consistency, both adapter inputs, mutation tests.
- Safeguards: closed key sets, stable errors, no serializer, no environment access, no raw envelope acceptance.
- Rollback/fail-closed: failure prevents evidence PASS; rollback never legitimizes current v1 proof.
- Adoption sequence: IA approval, plan revision, separate implementation authorization, module/tests, evidence adoption, later PR-05 consumption.
- Plan consequences: amend D9 and add a D12 dependency/interface note.
- Permanent drainage: PF02 §6.2 and PF14 source-invariance mechanics must name the projection boundary after adoption.
- Downstream effects: PR-05 consumes; PR-06 validates; OPS remains unchanged.
- Nonclaims: no mapped-cache persistence, live proof, production writes, public contract, token satisfaction, or PF09 movement.

Negative-search basis for EXTENDS: searched exact terms CanonicalBodyGraph, project_bodygraph, bodygraph_projection, and source-neutral bodygraph; scope current PR repository; GitHub code search; case-sensitive for symbols and case-insensitive for phrase; no exact implementation was found. Semantically related v2 adapter and ingest mechanisms were then inspected, so the decision is an extraction/generalization rather than an absence-only inference.

### ADR-CANON-002 - Versioned DB/vendor source-invariance evidence

- ADR ID: ADR-CANON-002.
- Title: Versioned DB/vendor source-invariance evidence.
- Status: PROPOSED - PENDING IA TECHNICAL APPROVAL.
- Linked IDs: BUG-001, CAUSE-002, RSC-002.
- Canon effect: AMENDS.
- Current PF-Canon contract:
  - PF09.6-Canon-HDE-Build-Checklist-Distillation, HDE-DIST001.5 and HDE-DIST001.7 require source selection/invariance and same-input DB/vendor Presenter-byte equality.
  - PF12-Canon-HDE-Schemas-and-Artifacts, §8.6.3.9 and Appendix C register the source-invariance family and records-only evidence discipline.
  - PF14-Canon-HDE-Mechanics-Guide, §Source invariance (single presenter/emitter) and §1.3.1 Evidence jobs require the actual predicate and single-writer proof.
- Observed Repo reality: the current v1 artifacts contain no DB/vendor bodies or hashes and duplicate canonical plus PR-specific Machine Mirror keys.
- Problem: a deterministic but semantically invalid family can pass its own check.
- Alternatives considered:
  1. Preserve v1 and add fields - rejected because consumers could still accept old semantics.
  2. Add a second PR-specific family - rejected because it creates another truth home and leaves invalid canonical paths.
  3. Replace current paths/keys in place with closed v2 schemas - selected.
- Selected decision: exact paths, keys, schemas, fields, predicates, negative receipt, and source scope defined in RSC-002.
- Minimum-scope rationale: preserve established paths and canonical keys while correcting semantics and eliminating duplicate rows.
- Exact implementation owner and locus: tools/evidence/generate_bodygraph_policy_proofs.py; two proposed schema files; three fixture files; existing focused tests.
- Exact schema/path/key decision: bodygraph.source_invariance.run.v2 and summary.v2 at the exact paths and keys in RSC-002.
- Affected boundaries: PR-04 D9 evidence, release bindings, updater/index/mirror/path proofs, PR-06 required primaries.
- Unchanged boundaries: public bytes, live source access, DB schema, cache persistence, OPS.
- Source-adapter scope: configured-v2 chart mapping and mapped DB cache payload; evidence must state this bounded scope.
- Persistence/durable-data effect: none; DB side is a fixture shaped as a mapped cache row.
- Compatibility: in-place path/key continuity; v1 rejected; no dual-version window.
- Migration: atomic producer/schema/consumer/key update in the order defined in RSC-002.
- Producer/consumer ownership: one primary producer; updater owns companions; release binding and PR-06 consume the source-invariance summary.
- Validation: independent acquisitions, same input, distinct representations, two-run stability, projection equality, Presenter equality, negative control, unsafe absence, schema closure, canonical bytes, fixed point.
- Safeguards: no raw payloads; hashes only; additionalProperties false; PASS derived from every predicate.
- Rollback/fail-closed: partial or stale family blocks; current v1 never resumes as accepted evidence.
- Adoption sequence: projection, schema, producer, primaries, receipt, binding, updater, check-only validation, PR-06.
- Plan consequences: amend D9 evidence and validation; update D3 dependency and PR-06 inventory.
- Permanent drainage: PF12 schema/catalog and PF14 mechanics; PF09.6 path/proof wording if needed.
- Downstream effects: PR-06 consumes v2; PR-05 may reuse projection but does not depend on evidence artifacts.
- Nonclaims: no live or all-version invariance; no token, QA, OPS, acceptance, or PF09 completion.

### ADR-CANON-003 - Dedicated PR-04 Presenter comparison and unique ownership

- ADR ID: ADR-CANON-003.
- Title: Dedicated PR-04 Presenter comparison and unique ownership.
- Status: PROPOSED - PENDING IA TECHNICAL APPROVAL.
- Linked IDs: BUG-003, CAUSE-003, RSC-003, REV-001, REV-002.
- Canon effect: AMENDS.
- Current PF-Canon contract:
  - PF09.6-Canon-HDE-Build-Checklist-Distillation, HDE-DIST001.9 currently names artifacts/presenter/json_canon_compare.log for DB/bridge comparison.
  - PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8, §8.3 Machine Evidence Index — JSONL mirror (records-only) [Required-Now]: "One JSON object per line."; "Sorted keys."; "Exactly one trailing \\n per line."
  - PF14-Canon-HDE-Mechanics-Guide v3.4.3, §1.3.1 Evidence jobs (single-writer tools): "Only a small set of evidence writers may write governed evidence artifacts (ordering artifacts, Evidence Index, Machine Mirror, bundles/manifests, and path-proofs). All other code — including tests and ad-hoc scripts — MUST NOT modify governed evidence directly." The same unit assigns governed path-proof transcripts to tools/evidence/update_evidence_index.py.
  - PF27-Canon-Plan-Templates v1.9.5, §Review guardrails: "A review MUST treat evidence outputs that overwrite or collide with an existing governed evidence family as blocking until the collision is repaired." The same rule requires task-specific evidence, restored shared/dependency artifacts, and coherent path-proof/index/mirror bindings.
- Observed current Repo reality:
  - generate_rails_closed_phase1.py directly writes DB schema/fingerprint/grants/partition/boundary, bridge adapter/capability, BodyGraph source/metrics/logs, shared Presenter, rails refusal, and sibling path proofs; delegates env-matrix generation; reads the wall clock; executes at module top level; and has no --check/selective interface.
  - generate_db_runtime_posture.py and generate_db_bridge_parity.py both write the two environment-connectivity primaries.
  - generate_db_bridge_parity.py copies four historical records through PRESENTER_BASE_RECORDS and appends the provisional PR-04 fifth row to the shared path.
  - The approved retained shared body is the first four canonical rows, 1559 bytes, SHA-256 64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c.
  - Current Machine Mirror bindings include generic/historical keys plus PR-specific duplicates for several affected paths.
- Engineering problem or limitation: the former monolithic producer and newer focused producers form a non-disjoint write graph. The prior proposed historical owner cannot reproduce the approved row set, check it read-only, or roll it back without wall-clock and unrelated side effects. Evidence meaning, history, and companions therefore depend on execution order rather than one authoritative source.
- Alternatives considered:
  1. Append PR-04 to shared JSONL - rejected because multiple writers remain.
  2. Continue constant replay - rejected because PR-04 owns copied history.
  3. Replace the shared path globally - rejected because historical consumers and PF09 currently bind it.
  4. Keep the broad generator as shared owner or dispatcher - rejected because it would retain unrelated writes, hide focused ownership, and violate selective/check-mode requirements.
  5. Retire the broad generator, allocate focused owners, add one source-manifest-backed history producer, and create one dedicated PR-04 JSON receipt - selected.
- Selected decision: adopt the complete §8 ownership ledger and RSC-003 contracts. The broad legacy generator becomes a no-write nonzero guard. Each focused generator owns one disjoint primary set. A new selective history producer owns only the unchanged shared path and reconstructs exactly four approved rows from one immutable source manifest. PR-04 owns one dedicated DB/bridge JSON receipt. The updater alone owns companions.
- Exact canon amendment:
  - Current rule changed: HDE-DIST001.9 and associated evidence catalogs use artifacts/presenter/json_canon_compare.log as the PR-04 DB/bridge compare output, while the mechanics/collision rules do not enumerate the directly competing command graph.
  - Replacement meaning: PR-04 DB/bridge Presenter evidence is artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json under key epic038.pr04.presenter_db_bridge_compare. artifacts/presenter/json_canon_compare.log remains historical-only under key presenter.bodygraph.json_canon_compare and is generated solely from the fixed four-row source by generate_presenter_history.py. All directly implicated primaries use the §8 focused owners; no primary producer writes companions; generate_rails_closed_phase1.py owns no governed path.
  - Unaffected remainder: HDE-DIST001.9 remains Partial; same-input Presenter semantics, governed artifact roots, canonical JSON/JSONL, historical payloads, public APIs, live OPS ownership, PR-05 persistence, PR-06 closure ownership, and all unrelated evidence families remain in force.
- Exact affected topic and bounded scope: PR-04 D8-D10 evidence-producer allocation only; the current shared Presenter historical family; current DB/environment/bridge/BodyGraph/rails primaries directly written by the retired generator; updater-owned companions; and PR-06's consumption of those paths. This is not a repository-wide producer audit.
- Minimum-scope rationale: retirement plus one selective historical owner is the smallest design that makes every retained write set disjoint, preserves the shared path/bytes, removes PR-04 from historical ownership, and supplies deterministic rollback.
- Exact implementation owners/loci:
  - generate_env_matrix_snapshot.py: env-matrix singleton.
  - generate_db_runtime_posture.py: DB posture plus partition plan/verify, excluding environment connectivity.
  - generate_db_bridge_parity.py: adapter/caps/provider parity, both environment-connectivity primaries, synthetic pair, and dedicated receipt, excluding shared history.
  - generate_bodygraph_policy_proofs.py: BodyGraph policy; generate_rails_gate_evidence.py: rails refusal.
  - proposed generate_presenter_history.py and tools/evidence/fixtures/presenter/json_canon_compare.history.v1.json: four-row shared history only.
  - update_evidence_index.py: every companion/index; tests/evidence/test_presenter_evidence_ownership.py plus focused producer tests: ownership, migration, fixed-point, and failure paths.
- Applicable API, schema, path, key, producer, and consumer decisions:
  - Source manifest schema presenter.history_source.v1 has exact keys and four records defined in RSC-003; it is source input without an artifact key.
  - Shared path/key/output and dedicated path/key/schema are exact in RSC-003.
  - Shared generator API is normal materialization plus read-only --check; no selective flag is needed because it owns exactly one file.
  - Consumers and current-key migrations are exact in §8; diagnostic appenders require explicit caller paths.
- Source-adapter scope: the dedicated receipt covers only the existing fixture-backed direct-DB and bridge DBAccess facades over the same ordered four-case deterministic harness corpus. The shared history producer performs no DB, bridge, vendor, adapter, Presenter comparison, or source acquisition.
- Persistence/durable-data effect: none.
- Compatibility and migration: shared path, four payloads, order, bytes, digest, and canonical key remain unchanged. PR-04 consumers migrate atomically to the dedicated receipt. Active broad-command references migrate to focused owners; historical mentions remain provenance. Migration follows RSC-003's six steps and never enters a dual-owner or dual-v1/v2 acceptance period.
- Dependency, adoption-order, and plan consequences: IA approval precedes separately authorized plan revision; source fixture/selective owner and focused write-set tests precede destination replacement; primary owners materialize before updater; release binding follows final BodyGraph primaries; fixed-point and all-order validation precede PR-06 handoff. The plan must replace broad-generator steps and the D10 shared-path reference but may not move OPS or persistence work.
- Validation and evidence requirements: exact manifest key/type/order validation; four per-row hashes; 1559-byte/output-digest equality; canonical serializer/LF; no clock/environment reads; check-mode no-write; same-directory atomic failure behavior; absent provisional row/replay constants; exact producer write sets; every allowed producer permutation; unique current path/key bindings; updater-only companions and fixed point; dedicated receipt schema, provider-parity binding, independent acquisitions, Presenter-byte equality, and negative-control rejection.
- Risks and safeguards: source-manifest tampering is caught by per-row and output digests; cross-family writes are caught by isolated before/after inventories; stale invocations hit the no-write guard; partial replacement cannot publish due atomic preflight; implicit diagnostic writes are removed; raw payloads remain excluded.
- Rollback/fail-closed: the only rollback source is the validated immutable manifest's exact four-row body. Pre-replacement failure preserves the old file. Post-replacement failure atomically restores that body, removes the dedicated partial family/current bindings, reconverges companions through the updater, and withholds PR-04 PASS. The broad generator and replay constants are never restored.
- Adoption sequence: IA approval, separate plan revision, source/owner scaffolding, focused ownership split, dedicated receipt, four-row atomic shared migration, legacy guard, canonical updater, all-order/fixed-point validation, PR-06 handoff.
- Permanent drainage targets:
  - PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, HDE-DIST001.9: replace PR-04's shared Presenter output with the dedicated path and record focused ownership without status movement.
  - PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8, §8.3 and affected catalog/key rows: record one current key/path binding, canonical four-row JSONL, and updater-owned companions.
  - PF14-Canon-HDE-Mechanics-Guide v3.4.3, §1.3.1 Evidence jobs (single-writer tools): record the focused producer allocation, retired broad generator, selective Presenter-history owner, and disjoint write-set/check posture.
  - PF27-Canon-Plan-Templates v1.9.5, §Review guardrails: add the bounded example that collision repair must inventory transitive writers, active invocation migration, and deterministic rollback source.
- Downstream effects: PR-06 consumes the dedicated path; OPS-01 stays independent.
- Explicit nonclaims: no historical deletion, reapproval, rerun, or PF09 status change; no public behavior, API, serializer, DB schema, persistence, live vendor/DB/bridge, OPS/QA, token, acceptance, merge, slice, or epic-completion claim; no permanent PF text is changed by this CRD.

### PF09.6 consequences

| Exact row | Current status | Proposed consequence | Status action |
| --- | --- | --- | --- |
| HDE-DIST001.4 - DB posture & runtime checks | Partial | Retain D8 meaning; assign DB/partition outputs to the focused DB-runtime producer and environment-connectivity to the focused bridge producer | No status change |
| HDE-DIST001.5 - BodyGraph mechanics gates | Partial | Adopt projection and v2 source-invariance evidence under PR-04 | No status change |
| HDE-DIST001.7 - Vendor ingest source policy & proofs | Done | Reuse its same-input invariant and maintain current evidence without reopening | No status change |
| HDE-DIST001.9 - DB-bridge parity & env connectivity | Partial | Replace PR-04 shared Presenter dependency with dedicated receipt; make bridge producer sole owner of adapter/caps/provider/env rows; retain OPS-01 | No status change |
| HDE-DIST001.10 - Architecture snapshot evidence | Partial | Correct existing analyzer taxonomy and verdict | No status change |
| HDE-DIST001.11 - v2 mapped-cache persistence hardening | Optional | Require later PR-05 to consume projection; move no persistence work | No status change |
| HDE-DIST002.5 - Release bindings evidence & indexing | Not done | Refresh the existing derived artifact and bind the v2 source-invariance summary in addition to source-selection and refresh-policy inputs | No status change |

PO approval and IA approval do not move these statuses. Any later supportable status action requires implemented, validated, accepted evidence and a separate authorized drainage step.

### PF10 consequence

The current PF10 v12.2.1 Addendum Index contains only §2.1 PR-01, §2.2 PR-02, and §2.3 PR-03 for HDE-EPIC038. It is silent on PR-04. After IA technical approval, a later authorized documentation step should add §2.4) PR-04 HDE-EPIC038 recording only the approved RSC/ADR decisions, bounded canon-amendment posture, plan-revision dependency, and nonclaims. This CRD does not write that addendum.

Evidence pointer: PF10-HDE-Build-Notes v12.2.1 | §1.1 Addendum Index | Entries are PR-01, PR-02, and PR-03 HDE-EPIC038; case-insensitive whole-file search for PR-04 returned zero hits.

### Permanent documentation drainage and order

| Target | Exact locator | Decision to drain | Effect | Ordering | Unchanged canon |
| --- | --- | --- | --- | --- | --- |
| PF02-Canon-HDE-Architecture | §6.2 Vendor seam; §5.4 Evidence & determinism flows | Source-neutral mapped BodyGraph projection and single Presenter use | EXTENDS | After IA approval; permanent text after implementation validation | Core purity, no second emitter, no public route |
| PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8 | §8.3 Machine Evidence Index — JSONL mirror (records-only) [Required-Now]; §8.6.3.9; Appendix C | v2 schemas; one current key/path binding; dedicated Presenter path/key; exact canonical four-row shared JSONL; duplicate-key removal | AMENDS | After approved implementation and updater convergence | Existing governed roots, canonical JSON/JSONL, and updater companion ownership |
| PF14-Canon-HDE-Mechanics-Guide v3.4.3 | §Source invariance; §1.3.1 Evidence jobs (single-writer tools) | Independent acquisition predicates; projection boundary; focused owner ledger; retired broad generator; selective history owner; updater-only companions | AMENDS | After implementation validation | Same-input final-byte invariant and fail-closed posture |
| PF09.6-Canon-HDE-Build-Checklist-Distillation | HDE-DIST001.5, .7, .9, .10, .11; HDE-DIST002.5 | Path/proof wording and exact dependency clarification only | AMENDS | Later documentation drainage; no status movement | Current statuses and downstream owners |
| PF27-Canon-Plan-Templates v1.9.5 | §Review guardrails | Preserve the bounded-rescope rule and add a collision-repair example requiring transitive-writer inventory, active-invocation migration, deterministic rollback source, and final-generator currentness | EXTENDS | Nonblocking process drainage after IA approval | Existing collision, evidence, and review guardrails |
| PF10-HDE-Build-Notes | Proposed §2.4) PR-04 HDE-EPIC038 | Stage approved decisions and nonclaims until permanent drainage | AMENDS live addenda only | After IA approval under separate docs authorization | PR-01 through PR-03 addenda remain topic-bounded |

CRD adoption and permanent wording changes are separate. No PF file is changed by this document.

## 11. Evidence, Risks, and Residual Unknowns

### Repo validation

- PR #354 is uniquely identified and current at the reviewed head.
- generate_bodygraph_policy_proofs.py hard-codes DB for both sources and compares source arrays.
- v2_adapter.py supplies an existing mapped HDE shape suitable for projection.
- ingest.py supplies a reusable final-byte comparison pattern but not a safe PR-04 proof implementation.
- emitter.py is the existing canonical byte authority.
- generate_db_bridge_parity.py and generate_rails_closed_phase1.py both full-write the shared Presenter log; the former replays four historical constants and appends PR-04, while the latter emits one wall-clock row.
- generate_rails_closed_phase1.py also writes overlapping DB, bridge, BodyGraph, rails-refusal, and sibling path-proof outputs, delegates env-matrix generation, executes at module top level, and has no --check interface.
- generate_db_runtime_posture.py and generate_db_bridge_parity.py both write env_connectivity.snapshot.json and env_connectivity.nondev_failure.json; bridge consistency consumes environment connectivity with adapter selection and provider parity.
- artifacts/presenter/json_canon_compare.log contains four retained historical rows plus one provisional PR-04 row. The retained four-row body is 1559 bytes with SHA-256 64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c.
- artifacts/evidence_index.jsonl contains PR-specific duplicate keys for the directly implicated generic/historical paths, including source-invariance and the shared Presenter log.
- generate_architecture_snapshot.py recognizes Blueprint and .route only and hard-codes PASS/zero unknown.
- adapter/wsgi.py contains @app.get declarations.
- release_bindings.json is stale relative to current bound inputs.

Evidence pointer: Repo | artifacts/evidence_index.jsonl at PR head | Established keys are bodygraph.source_invariance.ab, bodygraph.source_invariance.ba, bodygraph.source_invariance.summary, and presenter.bodygraph.json_canon_compare; PR-04 adds duplicate keys for the same paths.

### Plan and PF validation

- The Approved Epic Plan identifies HDE-EPIC038 - Distillation Pass 3 and D9 through D12.
- The Current Implementation Plan assigns PR-04, OPS-01, PR-05, OPS-02, and PR-06 in dependency order and explicitly keeps PR-04 closed-rails.
- PF09.6 supplies exact status and source-invariance requirements.
- PF02 supplies the pure/normalized/single-emitter architecture.
- PF27 supplies blocking collision and duplicate-key repair posture.
- Current PF10 supplies bounded-rescope precedent and is silent on PR-04.

### Diagnostics performed for this CRD

- Read-only GitHub PR metadata and current review-thread inspection.
- Read-only GitHub file fetches at the PR head for every relied-on implementation locus, artifact, test, index, and PF file.
- Reviewer-directed v1.4 validation re-read the complete IA review v1.2 and conditionally inspected only the directly implicated broad/focused generators, shared Presenter artifact, current mirror bindings, bridge consumer, legacy-reference loci, and PF12/PF14/PF27 collision units.
- The first four shared Presenter lines were isolated without writing Repo state; their per-row LF-inclusive digests, exact 1559-byte concatenation, and SHA-256 64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c were recomputed.
- Complete reads of the Approved Epic Plan, Current Implementation Plan, current PF10, and complete relied-on PF sections.
- Exact-string and semantic-locus searches for existing projection mechanisms, schema IDs, artifact keys, and PR-04 addenda.
- Local CRD workspace git-status checks before and after diagnostics both returned "fatal: not a git repository"; no product worktree status was claimed and no unexpected state change was observed through that diagnostic.
- No QA, OPS, generator write mode, package installation, service start, external vendor call, DB/bridge call, commit, push, or GitHub mutation was performed.

### Negative-search methods

1. Projection names: terms CanonicalBodyGraph, project_bodygraph, bodygraph_projection, and source-neutral bodygraph; scope current GitHub repository; exact symbol searches case-sensitive and phrase search case-insensitive; GitHub code search; no exact implementation hit. Semantically related v2_adapter.py and ingest.py were then directly inspected.
2. Proposed contracts: terms bodygraph.source_invariance.run.v2 and epic038.pr04.presenter_db_bridge_compare; scope current GitHub repository; exact case-sensitive search; zero hits.
3. PF10 PR-04: term PR-04; scope complete PF10 v12.2.1; rg, case-insensitive; zero hits. Addendum Index directly lists only PR-01 through PR-03.
4. Local product checkout: directory name glow-hdengine-v2; scope /workspace depth three; find, case-sensitive; no local checkout found. Connected GitHub access was used instead.
5. Legacy executable references: terms `generate_rails_closed_phase1.py`, `python tools/evidence/generate_rails_closed_phase1.py`, `generate_rails_closed_phase1.py --`, `generate_rails_closed_phase1.main`, and `import generate_rails_closed_phase1`; scope connected repository code-search index; exact-path/name search with case preserved; results included historical captures/prose, updater commentary, and tests/evidence/test_env_matrix_snapshot_v3.py's source assertion, while no selective/check interface was found. Because connector search is indexed against the repository default ref rather than a complete checked-out PR tree, exhaustive active-invocation absence is not claimed; the no-write retirement guard is the compatibility safeguard for any undiscovered executable call.

The search for presenter.bodygraph.json_canon_compare did return current Machine Mirror and historical evidence hits. That key is therefore retained as the canonical key for the shared path rather than invented anew.

### Source conflicts and access limits

- The conversational HDE-EPIC034 label conflicted with every authoritative target source and was rejected in favor of HDE-EPIC038.
- Earlier debugging could not resolve a current PR; connected GitHub now resolves it, so that blocker is stale.
- The CRD workspace is not a product Git worktree. Local uncommitted state and a complete local PR diff cannot be claimed. The connected PR head supplied the required read-only Repo facts.
- No complete remote PR diff is claimed. Only the connected PR metadata, current files, current review threads, and changed-head loci required by this rescope were used.
- GitHub code-search results used for the legacy-reference inventory were indexed at the repository default ref; current-head file fetches were used for each decisive producer/artifact fact. The search is not treated as proof that no other active invocation exists, so the selected retirement guard fails any undiscovered call closed without mutating evidence.

### Material risks and safeguards

| Risk | Safeguard |
| --- | --- |
| Projection accidentally becomes a second adapter or emitter | Input is already mapped; output exact; no serializer or I/O; existing Presenter remains sole byte authority |
| Two fixtures are copies and make equality trivial | Distinct source-representation hashes are mandatory and must differ |
| Run2 rehashes run1 bytes | Each run must reopen, deserialize, map, project, and emit independently with distinct acquisition IDs |
| Same-input claim is unbound | Both sources must bind the same normalized-input canonical SHA-256 |
| Evidence passes despite a broken comparator | Required negative mutation must produce BODYGRAPH_SOURCE_DIVERGENCE |
| Raw or sensitive data enters governed evidence | Artifacts contain hashes and bounded identifiers only; closed schemas and unsafe-field scan fail closed |
| Duplicate keys survive updater regeneration | Migration removes named duplicates before dedupe; one physical path/one canonical key is tested |
| Shared history changes by execution order or clock | Immutable exact four-row source, per-row/output hashes, selective no-clock owner, no implicit append default, dedicated PR-04 path, all-order and second-run fixed-point tests |
| A focused producer still overwrites another family | Normative §8 ledger, exact write-set assertions, isolated before/after inventories, and every allowed producer permutation |
| A stale legacy invocation rematerializes broad evidence | Legacy path is a no-write nonzero guard; active invocations migrate; historical mentions remain provenance only |
| Migration failure leaves mixed shared/dedicated bytes | All preflight checks precede same-directory atomic replacement; rollback source is the verified four-row body; PR-04 stays non-PASS on any failure |
| PR-05 scope is pulled forward | PR-04 uses deterministic fixtures only; no write/read-back or DB schema work |
| Route analyzer silently misses new syntax | Unclassified route-like forms increment unknown_count and force FAIL |
| Release binding certifies stale dependencies | It is generated after final primaries and checks exact path/hash/size in sorted order |

### Residual Unknowns

Two non-material factual Unknowns remain. First, future route registration syntax not present in the inspected Repo is unknowable; bounded discovery and unknown-form FAIL preserve safety. Second, connector code search does not prove the exhaustive universe of active legacy-generator invocations at the PR head; the no-write nonzero guard makes any undiscovered call visible and incapable of changing evidence. Neither Unknown alters the proposed module, schema, path, key, producer, ownership, migration, validation, rollback, or scope decisions.

## 12. Approval Limitations and Nonclaims

This CRD:

- does not implement code or evidence changes;
- does not edit product, planning, PF-Canon, ADR, PF09, or PF10 files;
- does not move PF09 status;
- does not create QA PASS;
- does not execute OPS;
- does not authorize deployment, persistence, database migration, or production writes;
- does not satisfy acceptance tokens;
- does not accept provisional PR #354 implementation;
- does not authorize PR merge;
- does not close PR-04;
- does not close HDE-EPIC038;
- does not perform permanent canon drainage;
- does not retire or refactor any generator, create the proposed source fixture, migrate any artifact, or change any current evidence byte; and
- does not reapprove, reopen, rerun, or change the status of the four retained historical Presenter records.

## 13. Questions for the Implementation Agent

None.

## 14. Implementation Agent Review Gate

### APPROVE

IA should APPROVE only if all of the following are true:

1. BUG-001 through BUG-004 and SUSP-001 retain the classifications in §4.
2. RSC-001 is technically feasible as a pure mapped-payload boundary and does not move PR-05 persistence into PR-04.
3. CanonicalBodyGraph, project_bodygraph, exact fields, errors, source scope, and no-I/O contract are complete and internally coherent.
4. RSC-002 cannot PASS without two distinct sources, distinct source representations, the same normalized input, two independent runs per source, canonical projection equality, Presenter byte equality, unsafe-field absence, and a rejected negative control.
5. The v2 schema IDs, paths, canonical keys, required fields, unknown-key posture, serialization, producer, consumers, migration, and rollback are complete.
6. RSC-003 creates exactly one PR-04 Presenter primary; gives every directly implicated governed primary exactly one focused owner; retires the broad legacy generator to a no-write guard; removes implicit governed-path append defaults and direct companion writes; preserves exactly four historical rows from one immutable source; and removes named duplicate current keys.
7. BUG-002's retained analyzer design derives PASS/FAIL from complete discovery and fails unknown route forms closed.
8. BUG-004's retained release-binding order and expanded input set close every changed dependency without reopening PR-01.
9. The plan-consequence matrix preserves OPS-01, PR-05, OPS-02, PR-06, historical PF09 rows, and public-contract boundaries.
10. The §8 ownership ledger dispositions every broad-generator primary, both environment-connectivity primaries, the dedicated receipt, and updater companions with exact displaced-writer, consumer, invocation, migration, and key treatment.
11. The shared Presenter source/producer contract fixes the exact records, order, per-row hashes, 1559-byte output, output digest, serializer, no-clock/check behavior, atomic migration, fixed point, and rollback source.
12. ADR-CANON-001 through ADR-CANON-003 are complete, minimal, adoptable, and consistent with the stated canon effects and exact permanent drainage targets.
13. Validation, adoption, and rollback orders are feasible and contain no hidden live, QA, OPS, or product-data migration action.
14. No material technical or canon decision is delegated to IA.

### RETURN FOR REVISION

IA should RETURN FOR REVISION if any of the following is true:

- any module, type, API, adapter scope, schema, path, key, producer, consumer, owner, compatibility rule, migration, validation predicate, rollback, or adoption order remains undecided;
- the projection duplicates a Presenter or performs I/O;
- the evidence can PASS from labels, parsed-object equality, copied source fixtures, one materialization hashed twice, or a missing negative control;
- a PR-specific duplicate key remains for an established physical path;
- more than one governed producer or implicit default writer can mutate the shared Presenter log;
- the broad legacy generator remains an active writer or dispatcher, any primary producer writes a companion, or any §8 write set overlaps;
- either environment-connectivity primary remains owned by both DB-runtime and DB-bridge producers;
- the shared-history owner reads the clock/current destination to construct expected rows, emits other primaries, lacks read-only check, or cannot reproduce the exact four-row digest;
- any active legacy invocation is left to mutate evidence rather than migrated or failed by the no-write guard;
- allowed producer permutations do not converge to identical final primary bytes before updater convergence;
- the dedicated DB-bridge receipt is treated as BodyGraph source-invariance truth or added to the BodyGraph release binding instead of remaining a separately hash-bound D10 proof;
- PR-05 persistence, OPS work, public routes, or acceptance claims move into PR-04;
- unknown route forms can remain compatible with PASS;
- release bindings can be generated before final primary bytes;
- a PF09 status movement or completion claim is implied; or
- any ADR-CANON is incomplete or inconsistent with its linked RSC.

IA approval is technical approval of this CRD only. It is not implementation authorization, plan adoption, PF-Canon adoption, QA PASS, OPS completion, acceptance, deployment, migration, PF09 movement, or closeout.

### Revision Response Ledger

#### Response item 1

- REV ID: REV-001.
- IA-required change: extend BUG-003/CAUSE-003/RSC-003 and linked ownership, plan, validation, rollback, and ADR content to every directly colliding governed path; select one owner per primary; disposition every displaced writer and active legacy invocation; and decide whether generate_rails_closed_phase1.py remains, splits, or retires.
- Disposition: RESOLVED.
- Revised CRD section or item: §§2, 4, 5; CAUSE-003; RSC-003; §8 one-row-per-primary ledger; §9 requirements, matrix, adoption, rollback; ADR-CANON-003; §§11, 12, and 14.
- Affected ADR-CANON-### ID(s), or None: ADR-CANON-003.
- Canon effect: AMENDS.
- Change made or reason unresolved: the complete broad/focused writer graph is inventoried. Each DB, bridge, environment, BodyGraph, rails-refusal, Presenter, and companion path has one selected owner, displaced-writer and key treatment, consumers, invocation compatibility, adoption, rollback, and validation. The broad legacy generator is retired from current generation and retained only as a no-write nonzero guard; focused primary write sets are disjoint; updater ownership is exclusive.
- Baseline, review, or permitted conditional-source evidence pointer: IA Review v1.2 | REV-001 | "At minimum the revised CRD must disposition the overlapping DB artifacts, both environment-connectivity artifacts, adapter-selection snapshot, BodyGraph source-selection/metrics/keys-only artifacts, rails-refusal proof, shared Presenter log, and all direct path-proof writes." Repo evidence: Repo | current broad/focused generators and §8 inspection inventory | the broad generator writes across all named families and both focused DB generators write the environment-connectivity pair.
- Permanent canon drainage target(s), or None: PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2 HDE-DIST001.9; PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8 §8.3 and affected catalog/key rows; PF14-Canon-HDE-Mechanics-Guide v3.4.3 §1.3.1 Evidence jobs (single-writer tools); PF27-Canon-Plan-Templates v1.9.5 §Review guardrails.
- IA acceptance condition: one-row-per-governed-primary ownership ledger for every directly colliding path, exactly one selected owner, explicit displaced-writer treatment, complete consumer/migration consequences, and proof that all retained producers may run in any allowed order without changing another family or companions.
- Acceptance condition satisfied: Yes.

#### Response item 2

- REV ID: REV-002.
- IA-required change: define the exact authoritative source, retained row set/order, deterministic timestamp posture, canonical serialization, selective materialization, read-only check, updater-only companions, atomic failure behavior, compatibility, rollback, provisional-row removal, and second-run fixed point for the shared Presenter log.
- Disposition: RESOLVED.
- Revised CRD section or item: §§2, 4, 5; CAUSE-003; RSC-003 Shared historical path retained, Shared-log producer contract, Atomic migration, Validation, and Rollback; §8; §9; ADR-CANON-003; §§11 and 14.
- Affected ADR-CANON-### ID(s), or None: ADR-CANON-003.
- Canon effect: AMENDS.
- Change made or reason unresolved: tools/evidence/fixtures/presenter/json_canon_compare.history.v1.json is selected as the immutable source and tools/evidence/generate_presenter_history.py as the sole one-file owner. The CRD fixes the four payloads/order, per-row hashes, 1559-byte/output digest, no-clock posture, canonical serializer, preflight, atomic replacement, read-only check, no-companion rule, active-consumer migration, provisional fifth-row removal, fixed-point proof, and authoritative rollback body.
- Baseline, review, or permitted conditional-source evidence pointer: IA Review v1.2 | REV-002 | "A complete next-version CRD defines a deterministic, selective, directly checkable shared-log owner that reproduces the exact approved historical row set with no PR-04 row, no unrelated primary writes, no direct companion writes, no wall-clock drift, and a tested atomic migration and rollback path." Repo evidence: Repo | artifacts/presenter/json_canon_compare.log and generate_rails_closed_phase1.py at reviewed head | five current rows; legacy owner emits one wall-clock row, writes unrelated paths/companions, and has no --check.
- Permanent canon drainage target(s), or None: PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2 HDE-DIST001.9; PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8 §8.3 and affected catalog/key rows; PF14-Canon-HDE-Mechanics-Guide v3.4.3 §1.3.1; PF27-Canon-Plan-Templates v1.9.5 §Review guardrails.
- IA acceptance condition: deterministic, selective, directly checkable owner reproducing exactly four approved historical rows with no PR-04 row, unrelated primary, direct companion, or clock drift, plus atomic migration/rollback and a second-run fixed point.
- Acceptance condition satisfied: Yes.

### Conditional Source Record

| Triggering revision | Affected ADR | Source | Exact locator or inspection method | Relied-on excerpt or observed fact | Revision use |
| --- | --- | --- | --- | --- | --- |
| REV-001 | ADR-CANON-003 | Repo | GitHub read-only fetch at d880e54bfd8b1d689ee08f9b352694924a7ae8d0: tools/evidence/generate_rails_closed_phase1.py | Broad top-level generator uses NOW, writes DB/bridge/BodyGraph/Presenter/rails primaries, calls _write_path_proof, and has no --check | Complete collision/write-set inventory; retire broad owner |
| REV-001 | ADR-CANON-003 | Repo | GitHub read-only fetch at reviewed head: tools/evidence/generate_db_runtime_posture.py and tools/evidence/generate_db_bridge_parity.py | Both write artifacts/runtime/env_connectivity.snapshot.json and artifacts/runtime/env_connectivity.nondev_failure.json | Select DB-bridge as sole environment-connectivity owner |
| REV-001 | ADR-CANON-003 | Repo | GitHub read-only fetch at reviewed head: tools/evidence/generate_bodygraph_policy_proofs.py, tools/evidence/generate_rails_gate_evidence.py, tools/evidence/update_evidence_index.py, ci/checks/check_bridge_consistency.py | Focused BodyGraph/rails owners exist; updater writes path proofs/indexes; bridge consistency jointly reads adapter, environment, and provider parity | Allocate focused owners, consumers, and updater-only companions |
| REV-001 | ADR-CANON-003 | Repo | GitHub repository code search; terms `generate_rails_closed_phase1.py`, `python tools/evidence/generate_rails_closed_phase1.py`, `generate_rails_closed_phase1.py --`, `generate_rails_closed_phase1.main`, and `import generate_rails_closed_phase1`; case preserved; default-ref index | Results include historical captures/prose, updater commentary, and tests/evidence/test_env_matrix_snapshot_v3.py's source assertion; no exhaustive PR-head absence claim is made | Migrate active references; use no-write guard for undiscovered invocations |
| REV-002 | ADR-CANON-003 | Repo | GitHub read-only fetch at reviewed head: artifacts/presenter/json_canon_compare.log | Four historical canonical rows precede one provisional PR-04 row; approved first-four body is 1559 bytes and SHA-256 64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c | Fix authoritative source, exact row set, order, hashes, removal, and rollback body |
| REV-002 | ADR-CANON-003 | Repo | GitHub read-only fetch at reviewed head: tools/evidence/generate_db_bridge_parity.py | PRESENTER_BASE_RECORDS copies four historical rows and appends the PR-04 row | Remove replay and shared writer; create dedicated receipt |
| REV-002 | ADR-CANON-003 | PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8 | §8.3 Machine Evidence Index — JSONL mirror (records-only) [Required-Now], Format (canonical JSONL) | "One JSON object per line."; "Sorted keys."; "Exactly one trailing \\n per line." | Define canonical four-row serialization and updater-coherent bindings |
| REV-001, REV-002 | ADR-CANON-003 | PF14-Canon-HDE-Mechanics-Guide v3.4.3 | §1.3.1 Evidence jobs (single-writer tools) | "Only a small set of evidence writers may write governed evidence artifacts (ordering artifacts, Evidence Index, Machine Mirror, bundles/manifests, and path-proofs). All other code — including tests and ad-hoc scripts — MUST NOT modify governed evidence directly." | One producer per primary and updater-only companion ownership |
| REV-001, REV-002 | ADR-CANON-003 | PF27-Canon-Plan-Templates v1.9.5 | §Review guardrails, Evidence-family path collision repair | "A review MUST treat evidence outputs that overwrite or collide with an existing governed evidence family as blocking until the collision is repaired." | Require task-specific PR-04 evidence, restored shared/dependency bytes, invocation migration, and coherent companions |

## 15. Revision History

- v1.0 - 2026-07-15 - Sekhmet: Initial PR-04 Rescoping CRD derived from the active debugging flow.
- v1.1 - 2026-07-15 - Sekhmet: Full-document revision responding to IA review v1.0. Corrected epic identity, current PF10/PF12 posture, PF09 active-versus-historical mapping, lifecycle sequence, canon effects, and PF27 scope; added a plan crosswalk, three incomplete ADR-CANON records, bounded route discovery, and the complete Revision Response Ledger. Material plan, architecture, schema, path, key, ownership, and migration decisions absent from the two permitted inputs remained blocked pending IA clarification.
- v1.2 - 2026-07-15 - Sekhmet: Revision-only attempt under a two-input restriction. It preserved the blocked posture and did not supply the technical decisions required for IA approval; superseded by v1.3.
- v1.3 - 2026-07-15 - Sekhmet: Complete re-authoring under Prompt Version 071526.3 from the full active debugging flow, current Repo, current PF-Canon, current PF10, Approved Epic Plan, and Current Implementation Plan. Authored the source-neutral projection, versioned evidence contract, unique Presenter ownership, exact schema/path/key migration, retained repairs, plan consequences, validation, rollback, and complete ADR-CANON decisions.
- v1.4 - 2026-07-15 - Sekhmet: Full-document revision resolving IA review v1.2 REV-001 and REV-002. Completed ADR-CANON-003 (AMENDS) for the PR-04 evidence-producer ownership graph and shared Presenter-history family; retired the broad legacy writer, assigned every directly implicated primary to one focused owner, fixed the four-row source/serialization/digest/atomic rollback contract, and propagated migration, compatibility, validation, plan, boundary, and nonclaim effects. Permanent drainage targets are PF09.6 HDE-DIST001.9, PF12 v2.7.8 §8.3 and catalog/key rows, PF14 v3.4.3 §1.3.1, and PF27 v1.9.5 §Review guardrails.

STATUS: READY FOR IA RE-REVIEW


# Rescoping CRD Review - HDE-EPIC038 - PR-04

## 1. Document Control

- **Review version:** v1.3
- **Reviewed CRD ID and version:** CRD-HDE-EPIC038-PR-04 v1.4
- **Epic ID and name:** HDE-EPIC038 - Distillation Pass 3
- **PR or slice ID:** PR-04 - DB, BodyGraph, bridge, and architecture posture harness
- **Reviewer role:** Glow Implementation Agent, technical and execution-readiness reviewer
- **PO approval posture:** Rescoping authority is established as APPROVED. This review does not re-litigate that authority and does not treat it as proof of technical correctness or implementation authorization.
- **CRD_FILE:** `rescoping-crd-hde-epic038-pr-04-v1.4.md`
- **APPROVED_IMPLEMENTATION_GUIDE_FILE:** `r1 Epic Plan HDE-EPIC038.md`
- **CURRENT_IMPLEMENTATION_PLAN_FILE:** `r6 Implementation Plan HDE-EPIC038.md`
- **REPO_ROOT_OR_GITHUB:** `glow-hdengine-v2`
- **Repo inspection mode:** Connected GitHub repository, read-only inspection only. No local product-worktree command is claimed.
- **Observed Repo revision or equivalent inspected state:** `amthorn78/glow-hdengine-v2`, PR #354 head `d880e54bfd8b1d689ee08f9b352694924a7ae8d0`, branch `codex/implement-pr-04-for-hde-epic038`, base `main@2971256474f70ad62848ce58a2bfaf1ea4438f37`; PR state open, unmerged, four commits, 62 changed files.
- **Review lineage:** Earlier review files established v1.0, v1.1, and v1.2; this review is therefore v1.3. Those prior review files were used only to establish review-version lineage, not as substantive authority for the present decision.

**Current PF-Canon consulted**

- `PF10-HDE-Build-Notes`, v12.2.1: Purpose; Precedence and versioning; §1.1 Addendum Index; bounded PR-01 rescope precedent in §2.1. This was established as the latest applicable PF10 by its complete document-control unit. Older PF10 copies were not combined with it.
- `PF02-Canon-HDE-Architecture`, v2.3.8: §5.4 Evidence & determinism flows (concept only); §6.1 BodyGraph ingest & refresh posture (concept only); §6.2 Vendor seam (concept only).
- `PF06-Canon-Epic-Process-Guide`, v2.3.5: §0.2 Policy and principles; the current CRD/Implementation Guide process units; documentation-drainage separation and PF-edit boundaries.
- `PF09.6-Canon-HDE-Build-Checklist-Distillation`, v1.1.2: HDE-DIST001.4, HDE-DIST001.5, HDE-DIST001.7, HDE-DIST001.9, HDE-DIST001.10, HDE-DIST001.11, and HDE-DIST002.5.
- `PF12-Canon-HDE-Schemas-and-Artifacts`, v2.7.8: §8.3 Machine Evidence Index — JSONL mirror (records-only) [Required-Now]; §8.6.3.9; Appendix C.
- `PF14-Canon-HDE-Mechanics-Guide`, v3.4.3: §1.3.1 Evidence jobs (single-writer tools); §Source invariance (single presenter/emitter).
- `PF27-Canon-Plan-Templates`, v1.9.5: §Review guardrails, including governed-family coherence, path-collision repair, artifact-key collision repair, and final-generator logic.

**Reviewed canon-changing ADRs**

- **ADR-CANON-001 — Source-neutral BodyGraph projection boundary:** APPROVED; effect `EXTENDS`.
- **ADR-CANON-002 — Versioned DB/vendor source-invariance evidence:** APPROVED; effect `AMENDS`.
- **ADR-CANON-003 — Dedicated PR-04 Presenter comparison and unique ownership:** APPROVED; effect `AMENDS`.

Evidence pointer: CRD | §1 Document Control | "CRD ID | CRD-HDE-EPIC038-PR-04"; "CRD version | v1.4"; "PO authorization | APPROVED".

Evidence pointer: CRD | §1 Document Control | "Reviewed HEAD | d880e54bfd8b1d689ee08f9b352694924a7ae8d0"; "Reviewed branch state | codex/implement-pr-04-for-hde-epic038; PR #354 is open and unmerged against main".

Evidence pointer: Repo | GitHub PR #354 metadata inspection | "head_sha=d880e54bfd8b1d689ee08f9b352694924a7ae8d0"; "base_sha=2971256474f70ad62848ce58a2bfaf1ea4438f37"; "merged=false"; "changed_files=62".

Evidence pointer: PF10 - PF10-HDE-Build-Notes | Front Matter and §1.1 Addendum Index | "Version: v12.2.1"; entries are "2.1) PR-01 HDE-EPIC038", "2.2) PR-02 HDE-EPIC038", and "2.3) PR-03 HDE-EPIC038".

## 2. Review Decision

Decision: APPROVED

The CRD is technically ready to govern a later revision of the Current Implementation Plan. It establishes two confirmed rescoping conflicts and two retained-scope repairs against current Repo reality; supplies complete causal chains; requests a bounded, coherent rescope rather than convenience expansion; preserves PR-05, OPS-01, OPS-02, PR-06, historical evidence, PF09 status, QA, acceptance, and closeout boundaries; and specifies executable ownership, schema, migration, validation, rollback, and documentation consequences.

All seven review gates pass. No material claim remains `UNVERIFIED`. Each proposed canon change is contained in a complete, technically sound `ADR-CANON-###` with a bounded effect, unchanged-canon boundary, migration and compatibility posture, validation, safeguards, rollback or fail-closed behavior, adoption order, and permanent drainage targets.

Approval is limited to the CRD and its three architectural decisions. It does not accept the provisional implementation on PR #354, authorize implementation, revise either plan, edit PF-Canon, execute QA or OPS, move PF09 status, satisfy tokens, deploy, migrate, accept work, or close the slice or epic.

Evidence pointer: CRD | §2 Executive Summary | "The minimum rescope is RSC-001 through RSC-003"; "Preserved boundaries are explicit: no public Reader or CLI contract changes; no live DB, bridge, or vendor execution; no mapped-cache write implementation".

Evidence pointer: CRD | §14 Implementation Agent Review Gate, APPROVE | Approval requires all three ADRs to be sound, all three RSCs necessary, BUG-002 and BUG-004 retained, producer ownership unique, and no status or completion claim.

Evidence pointer: Implementation Guide | Deliverables D8-D12 and Work Category Separation | PR implementation is separated from PO-only OPS, later QA, documentation drainage, and closeout.

Evidence pointer: Implementation Plan | Execution plan items 4-8 | PR-04 precedes OPS-01 and PR-05; PR-06 depends on PR-01 through PR-05 plus OPS-01 and OPS-02.

## 3. Source Coverage and Conflicts

**Complete-source coverage**

The Rescoping CRD, Approved Implementation Guide, and Current Implementation Plan were read end-to-end. The current PF10 document-control and applicable topic units were resolved without combining older PF10 copies. The topic-owning PF02, PF06, PF09.6, PF12, PF14, and PF27 sections materially relied on by the CRD or this review were retrieved as complete units. Repo inspection was scoped to current PR metadata, directly implicated producers, runtime and evidence components, tests, artifacts, schemas, updater registrations, and current governed outputs.

**CRD item coverage**

Every material CRD item was accounted for:

- Confirmed and retained findings: BUG-001 through BUG-004.
- Bounded suspicion and stale findings: SUSP-001 and STALE-001 through STALE-005.
- Causal chains: CAUSE-001 through CAUSE-005.
- Requested rescope: RSC-001 through RSC-003.
- Ownership and boundary changes: §§8-9.
- Plan and sequencing consequences: §9 plan-consequence matrix and adoption order.
- Canon consequences: ADR-CANON-001 through ADR-CANON-003, PF09.6 ledger, PF10 consequence, and permanent drainage table.
- Prior revision-response items: REV-001 and REV-002 are resolved inside the CRD and were re-evaluated as part of ADR-CANON-003.
- Approval limitations and nonclaims: §12.

**Repo validation posture**

Direct read-only GitHub inspection corroborated the material current-state premises:

- The current BodyGraph source-invariance producer records DB labels for both orders and compares `['db','db']` arrays rather than independently acquired DB/vendor canonical bodies.
- The current v2 adapter already provides a pure mapped HDE-shaped result suitable as one input to a source-neutral projection boundary.
- The current ingest path includes live I/O/persistence and its dry-run path reuses one emitted hash, so it is not a safe wholesale replacement for the proposed closed-rails proof boundary.
- The legacy Rails Closed Phase 1 generator uses wall-clock state, executes top-level writes, writes multiple unrelated primary families, writes path proofs directly, and has no selective or check interface.
- The DB-runtime and DB-bridge generators both name the environment-connectivity primary pair.
- The architecture snapshot generator does not discover current Flask method decorators and hard-codes a passing verdict with zero unknowns.
- The release-binding artifact is stale relative to the current source-selection and refresh-policy primaries.
- The shared Presenter log contains four historical rows plus one provisional PR-04 row, while the DB-bridge producer reconstructs historical rows from code constants.
- The updater patch adds PR-specific keys for physical paths already bound under established canonical keys.

**CRD evidence sufficiency**

The CRD contains checkable paths, symbols, hashes, exact source and output identities, negative-search methods, ownership rows, consumer migrations, adoption order, rollback stops, and nonclaims. Direct Repo inspection agreed with the material premises. The four-row historical Presenter body’s stated 1559-byte length and SHA-256 `64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c` are reproducible from the four current historical rows.

**Plan and PF-Canon conflicts**

- The Current Implementation Plan assigns the shared `artifacts/presenter/json_canon_compare.log` path to PR-04 D10 and leaves producer allocation insufficiently exclusive. ADR-CANON-003 expressly amends that implementation design by moving PR-04 to a dedicated receipt while retaining the shared path for deterministic historical reconstruction.
- PF09.6 HDE-DIST001.9 currently names the shared Presenter log. ADR-CANON-003 expressly amends that exact PR-04 proof boundary without reopening historical status.
- Current PF02 and PF14 require normalized internal data and shared-Presenter source invariance but do not name the proposed pure projection API. ADR-CANON-001 boundedly extends those architectural mechanics.
- Current PF12/PF14 establish the source-invariance family and evidence discipline but do not close the current v1 semantic hole. ADR-CANON-002 boundedly amends the governed evidence contract in place.
- PF06’s general CRD concision and titles-only posture does not invalidate the detailed ADR records here because the current PO review instruction expressly requires complete `ADR-CANON-###` decisions for canon-changing rescope. Permanent PF text remains separate drainage.

**Material `UNVERIFIED` claims**

None.

The CRD’s residual unknown about future Flask or extension-specific route forms is not a material unverified premise. The selected analyzer contract treats any unclassified route-like form as `unknown` and derives FAIL, so the uncertainty is bounded by fail-closed behavior rather than used as evidence of absence.

Evidence pointer: Repo | `tools/evidence/generate_bodygraph_policy_proofs.py`, `inv()` and `generate()` | Every source decision uses `source='db'`; both canonical source sequences are `['db','db']`; summary equality is array equality.

Evidence pointer: Repo | `engine/bodygraph/v2_adapter.py`, `adapt_v2_chart_payload()` | The pure adapter maps a validated ChartResult plus explicit context into `bodygraph`, `person`, `person_uid`, and cache-shaped mapped data and performs no I/O.

Evidence pointer: Repo | `engine/bodygraph/ingest.py`, `ingest_vendor_bodygraph()` | Live mode fetches, persists, reads back, re-emits, and compares; dry-run sets `db_emitted_sha256=payload_sha` and `parity_match=True`.

Evidence pointer: Repo | `tools/evidence/generate_rails_closed_phase1.py` | Module-level generation uses current UTC time; `_write_bytes` calls `_write_path_proof`; the script writes DB, bridge, BodyGraph, Presenter, and rails-refusal families.

Evidence pointer: Repo | `tools/evidence/generate_db_runtime_posture.py` and `tools/evidence/generate_db_bridge_parity.py` | Both define and write `artifacts/runtime/env_connectivity.snapshot.json` and `artifacts/runtime/env_connectivity.nondev_failure.json`.

Evidence pointer: Repo | `tools/evidence/generate_architecture_snapshot.py` and `adapter/wsgi.py` | Analyzer handles Blueprint and `.route`, while current app routes include `@app.get('/internal/healthz')` and `@app.get('/internal/readyz')`; analyzer verdict is hard-coded PASS with `unknown_count=0`.

Evidence pointer: Repo | `tools/evidence/generate_release_bindings.py`, `artifacts/bodygraph/release_bindings.json`, current source-selection and refresh-policy artifacts | Producer binds only source-selection and refresh-policy; committed binding hashes and sizes do not match the current two primaries.

Evidence pointer: Repo | `artifacts/presenter/json_canon_compare.log` and `tools/evidence/generate_db_bridge_parity.py` | Current shared log has five rows; the producer contains `PRESENTER_BASE_RECORDS` for the first four and appends a PR-04 row.

Evidence pointer: Repo | PR #354 patch for `tools/evidence/update_evidence_index.py` | `EPIC038_PR04_PRIMARY_ARTIFACTS` adds PR-specific keys for existing DB, bridge, BodyGraph, runtime, and Presenter paths, including `epic038.pr04.bodygraph_source_invariance_ab` and `epic038.pr04.presenter_json_canon_compare`.

Evidence pointer: Repo | negative search | Search term `CanonicalBodyGraph`; source/scope `amthorn78/glow-hdengine-v2`; method GitHub code search; case sensitive; result 0 hits.

Evidence pointer: Repo | negative search | Search term `project_bodygraph`; source/scope `amthorn78/glow-hdengine-v2`; method GitHub code search; case sensitive; result 0 hits.

Evidence pointer: Repo | exact-path inspection | Path `engine/bodygraph/projection.py`; GitHub contents lookup at PR #354 head; case sensitive; result 404 Not Found.

Evidence pointer: PF10 - PF10-HDE-Build-Notes | whole-file bounded search and §1.1 Addendum Index | Search pattern `PR-04` scoped to current v12.2.1; case sensitive exact identifier; result 0 hits; index ends at PR-03 for HDE-EPIC038.

## 4. Review Gate Results

### Gate 1: Authority and source fidelity — PASS

**Covered CRD items:** §1 Document Control; §3 Authority and Decision Posture; §12 Approval Limitations and Nonclaims; §13 Questions; §14 approval/return gate.

The CRD stays within the PO-approved rescoping boundary and treats the Approved Implementation Guide and Current Implementation Plan as baselines to be revised later rather than as already changed. It clearly separates PO authority from technical proof and implementation authorization. It makes no claim of implementation, plan revision, permanent PF editing, QA PASS, OPS completion, deployment, migration, token satisfaction, acceptance, PF09 movement, merge, slice completion, or epic closeout.

The CRD follows the current rescoping procedure: confirmed findings are distinguished from retained-scope repairs and residual unknowns; each canon-changing decision is placed in an explicit ADR; plan and permanent-document consequences are identified without performing them.

Evidence pointer: CRD | §3 Authority and Decision Posture | "PO approval establishes permission to rescope. It does not approve this CRD's technical content, authorize implementation, or change PF09 status."

Evidence pointer: CRD | §12 Approval Limitations and Nonclaims | The CRD explicitly disclaims implementation, plan and PF edits, QA, OPS, deployment, migration, persistence, tokens, acceptance, merge, slice completion, epic closeout, and drainage completion.

Evidence pointer: Implementation Guide | Work Category Separation | Implementation, OPS, QA planning, QA execution, and documentation drainage are separate categories; OPS is PO-only and QA execution is not included.

Evidence pointer: Implementation Plan | Source posture and Later artifacts outside implementation execution | No PF document edit is an implementation or OPS deliverable; QA and closeout artifacts remain later surfaces.

Evidence pointer: PF06 - PF06-Canon-Epic-Process-Guide | §0.2 Policy and principles | Implementation agents do not directly modify PF-Canon during implementation; documentation drainage is separate and is not an implementation or closeout gate.

### Gate 2: Conflict and causal accuracy — PASS

**Covered CRD items:** BUG-001 through BUG-004; SUSP-001; STALE-001 through STALE-005; CAUSE-001 through CAUSE-005; §4 Debugging Flow Basis; §5 Current Contract and Observed Conflict.

The CRD identifies specific, current technical conflicts and correctly distinguishes them:

- BUG-001 is a confirmed rescoping defect: the source-invariance family proves repeated labels and party order, not DB/vendor same-input canonical-byte invariance.
- BUG-003 is a confirmed rescoping defect: the command graph contains transitive primary writers, direct path-proof writers, duplicate environment owners, a shared Presenter collision, and duplicate current artifact keys.
- BUG-002 and BUG-004 are correctly retained as repairs inside original D11 and release-binding scope rather than used to justify additional rescoping.
- SUSP-001 is bounded as a future taxonomy unknown and handled fail-closed.
- STALE-001 through STALE-005 are not promoted into mandatory scope without current support.

CAUSE-001 through CAUSE-005 each connect governing contract, observed Repo reality, conflict, consequence, minimum change, dependencies, owner, validation, rollback or fail-closed behavior, plan consequence, and canon/documentation consequence. The mandatory additions rest on confirmed current premises rather than suspicion, green CI, or implementation history alone.

Evidence pointer: CRD | CAUSE-001 | The chain connects the source-invariance contract, current adapter/ingest/proof reality, missing pure convergence domain, projection decision, PR-04/PR-05 ownership split, validation, rollback, and PF02/PF14 extension.

Evidence pointer: CRD | CAUSE-002 | The chain connects v1 semantic insufficiency to the in-place closed v2 schema, independent acquisitions, negative control, release binding, updater, and PR-06.

Evidence pointer: CRD | CAUSE-003 | The chain inventories the broad legacy writer, focused collisions, environment pair collision, shared history replay, consequences, exact owner allocation, migration, all-order validation, rollback, plan changes, and permanent drainage.

Evidence pointer: CRD | CAUSE-004 and CAUSE-005 | Both are retained-scope repairs with exact owners, validation, rollback posture, and no new RSC.

Evidence pointer: Repo | current producer and artifact inspection listed in §3 of this review | The decisive BUG-001 through BUG-004 premises are directly corroborated at PR #354 head.

Evidence pointer: PF09.6 - PF09.6-Canon-HDE-Build-Checklist-Distillation | HDE-DIST001.7 | "for the same normalized inputs, DB-sourced and vendor-sourced BodyGraph bodies MUST be byte-identical when emitted via the shared presenter/emitter."

Evidence pointer: PF14 - PF14-Canon-HDE-Mechanics-Guide | §1.3.1 Evidence jobs (single-writer tools) | Only bounded evidence writers may write governed artifacts; `tools/evidence/update_evidence_index.py` is the single writer for the Human Index, hash sentinel, Machine Mirror, and governed path proofs.

### Gate 3: Minimum coherent rescope — PASS

**Covered CRD items:** RSC-001; RSC-002; RSC-003; §4 Rejected resolution alternatives; §7 Requested Rescope.

The requested scope is the minimum coherent architecture, not merely the smallest code diff:

- RSC-001 adds one pure source-neutral projection boundary because the proof cannot safely compare independently shaped DB and vendor representations without either duplicating production mapping inside a generator or invoking live persistence. It reuses the existing configured-v2 adapter and single Presenter, creates no public surface, and moves no durable write work from PR-05.
- RSC-002 corrects the canonical source-invariance family in place rather than creating a second truth home. It requires distinct source representations, two independent runs, shared normalized-input binding, projection equality, final Presenter-byte equality, closed schemas, a mutation receipt, and a conjunction-derived PASS.
- RSC-003 repairs the complete transitive ownership graph required to retire the broad writer safely. It does not use the visible Presenter collision as a pretext for unrelated cleanup: every moved artifact is already written by the directly implicated legacy generator or colliding focused generators, and every replacement has a named owner, consumer, migration, validation, and rollback posture.

The CRD expressly rejects convenience alternatives: restoring shape only, reusing live ingest wholesale, comparing parsed objects only, appending another shared row, copying historical rows into PR-04 code, moving PR-05 persistence forward, retaining the broad generator as owner/dispatcher, or accepting replay constants.

Evidence pointer: CRD | RSC-001 | Exact module, API, field sets, stable error codes, source-adapter scope, fixtures, Presenter rule, PR-05 boundary, tests, rollback, and nonclaims are fully specified.

Evidence pointer: CRD | RSC-002 | Exact paths, canonical keys, schemas, fields, independent acquisitions, predicates, negative receipt, atomic migration, release-binding dependency, validation, and no-live/non-persistence boundaries are fully specified.

Evidence pointer: CRD | RSC-003 | Exact retirement guard, focused owner allocation, four-row source fixture, hashes, output length/digest, atomic writer, dedicated PR-04 receipt, key migration, consumer migration, all-permutation validation, rollback, and nonclaims are fully specified.

Evidence pointer: PF02 - PF02-Canon-HDE-Architecture | §5.4 Evidence & determinism flows (concept only) | Offline evidence exercises existing Engine behavior and does not introduce new runtime routes, alternate emitter paths, or replacement transport surfaces.

Evidence pointer: PF02 - PF02-Canon-HDE-Architecture | §6.2 Vendor seam (concept only) | The vendor seam normalizes vendor responses into internal BodyGraphs; Engine Core receives only normalized data; public bytes remain emitted by the single Presenter.

Evidence pointer: PF27 - PF27-Canon-Plan-Templates | §Review guardrails, Evidence-family path collision repair | A path collision remains blocking until task-specific evidence is moved, shared/dependency artifacts are restored, and path-proof/index/mirror bindings are coherent.

Evidence pointer: PF27 - PF27-Canon-Plan-Templates | §Review guardrails, Evidence artifact-key collision repair | Canonical keys must be retained and stale duplicate/epic-specific keys removed before coherent regeneration.

### Gate 4: Epic and slice boundaries — PASS

**Covered CRD items:** §8 Ownership and Boundary Effects; §9 Plan-consequence matrix; §10 PF09.6 consequences; all moved-forward, retained, historical, and downstream ownership statements.

The CRD preserves the epic and slice architecture:

- PR-04 receives only the pure projection, corrected local evidence, focused producer ownership, analyzer repair, and release-binding dependency maintenance needed for D8-D11.
- PR-05 retains mapped-cache schema choice, durable write, read-back, idempotence, and authorization work under HDE-DIST001.11.
- OPS-01 retains live direct-DB/bridge evidence; OPS-02 retains controlled live mapped-cache proof.
- PR-06 retains final orchestration, final evidence binding, and later release-sanity consumption.
- Historical HDE-DIST001.7 remains Done and is used only as a current contract; it is not reopened or reapproved.
- Historical shared Presenter evidence remains at its current path with the exact four approved rows and one canonical key; PR-04 receives a dedicated current receipt.
- Each governed primary in the directly implicated write set has one selected producer; displaced writers and active consumers are explicitly treated.
- No unsupported completion or status claim is made.

The moved partition and capability outputs are not speculative platform expansion. They are existing outputs that require an owner when the directly implicated broad generator is retired. This is a bounded dependency transfer necessary to prevent orphaned or competing governed bytes.

Evidence pointer: CRD | §8 one-row-per-governed-primary ownership ledger | Each directly implicated DB, bridge, runtime, BodyGraph, rails-refusal, Presenter, and companion family has a selected owner, key treatment, displaced-writer disposition, and consumer.

Evidence pointer: CRD | §8 Boundaries explicitly unchanged | D8 meaning, public surfaces, single Presenter, PR-05 durable work, OPS live work, historical PF09 status, and PF09 status movement remain unchanged.

Evidence pointer: CRD | §9 Plan-consequence matrix | D8-D12, historical HDE-DIST001.7, D3 release bindings, and PR-06 have explicit bounded consequences and retained owners.

Evidence pointer: Implementation Plan | Execution plan items 4-8 | PR-04 -> OPS-01 and PR-05 -> OPS-02 -> PR-06 dependency order remains intact.

Evidence pointer: PF09.6 - PF09.6-Canon-HDE-Build-Checklist-Distillation | HDE-DIST001.4/.5/.9/.10/.11 and HDE-DIST002.5 | Current statuses are Partial, Partial, Partial, Partial, Optional, and Not done respectively; HDE-DIST001.7 is Done.

### Gate 5: Implementation Plan executability — PASS

**Covered CRD items:** §9 Source-grounded technical requirements; retained analyzer correction; retained release-binding correction; plan-consequence matrix; adoption and evidence-generation order; rollback stops; exclusions.

The CRD gives enough source-grounded direction to revise the Current Implementation Plan without inventing material paths, APIs, schemas, commands, tests, evidence, dependencies, ordering, or ownership.

Execution-critical decisions are closed:

- Exact new production module, types, API, error codes, input/output contract, validation order, and tests for the projection boundary.
- Exact fixture paths and fixture contracts for independent DB/vendor acquisition.
- Exact existing source-invariance paths, replacement v2 schema paths/IDs, canonical keys, fields, predicates, and negative receipt.
- Exact broad-generator retirement behavior and diagnostic.
- Exact focused producer write sets, dedicated Presenter-history fixture/producer, dedicated PR-04 receipt path/key/schema, consumers, and duplicate-key removals.
- Exact analyzer taxonomy and verdict derivation.
- Exact release-binding input set and generation order.
- Exact fourteen-step adoption order, rollback stops, and exclusions.

All named current loci were validated against the Repo. Proposed loci that do not currently exist are explicitly introduced by approved RSC/ADR decisions rather than asserted as present. The design remains fail-closed when an expected source, row, schema, key, producer, or invocation cannot be established.

Evidence pointer: CRD | §9 Source-grounded technical requirements | Fourteen numbered requirements map the three RSCs and two retained repairs into exact implementation and evidence consequences.

Evidence pointer: CRD | §9 Adoption and evidence-generation order | The order begins with ADR adoption and separate plan revision, lands projection/schema/ownership scaffolding before destination replacement, runs primaries before the updater, generates release bindings after final inputs, and ends at PR-06 handoff without OPS/QA execution.

Evidence pointer: Repo | exact current paths inspected | `engine/bodygraph/v2_adapter.py`, `engine/bodygraph/ingest.py`, `engine/presenter/emitter.py`, `tools/evidence/generate_bodygraph_policy_proofs.py`, `tools/evidence/generate_db_runtime_posture.py`, `tools/evidence/generate_db_bridge_parity.py`, `tools/evidence/generate_rails_closed_phase1.py`, `tools/evidence/generate_architecture_snapshot.py`, `tools/evidence/generate_release_bindings.py`, `tools/evidence/update_evidence_index.py`, and current governed artifacts all exist at the reviewed head.

Evidence pointer: Repo | exact negative-path inspection | `engine/bodygraph/projection.py` is absent at the reviewed head; the CRD correctly identifies it as a proposed output rather than an existing component.

Evidence pointer: Implementation Plan | PR-04, PR-05, OPS-01, OPS-02, PR-06 | The CRD identifies every plan row whose path, dependency, producer sequence, evidence inventory, or consumer must change, while preserving the established lifecycle.

### Gate 6: Validation, evidence, and safeguards — PASS

**Covered CRD items:** §11 Evidence, Risks, and Residual Unknowns; §9 validation/adoption/rollback units; §14 Conditional Source Record.

Validation follows the causal graph and tests both positive and false-pass paths:

- Projection shape, source stripping, JSON safety, stable errors, nonmutation, no-I/O behavior, and both source adapters.
- Independent DB/vendor acquisitions, distinct source representations, two-run stability, same normalized input, projection equality, Presenter-byte equality, schema closure, canonical bytes, and mutation rejection.
- Exact producer write sets, every allowed producer permutation, no cross-family or companion writes, no clock-derived history, exact historical bytes/digest, atomic failure behavior, unique keys, and updater fixed point.
- Architecture route-form discovery, ordinary `.get` false-positive exclusion, and unknown-form FAIL.
- Release-binding path/hash/size/order validation after all bound inputs reach final bytes.

Evidence governance is correctly assigned: focused feature producers write primaries; the canonical evidence skeleton tools own governed companions and ledgers; the Human and Machine indexes remain coherent; final artifacts are regenerated from final logic; no raw payloads, secret values, SQL, request/response bodies, or environment values are admitted into the new evidence.

Rollback is concrete and fail-closed. The invalid v1 source-invariance proof is not a rollback target; partial migrations do not publish PASS; the shared Presenter history can be restored only from the exact validated four-row source fixture; the broad writer and replay constants are never restored; release bindings are not generated before dependency closure.

Evidence pointer: CRD | §11 Repo validation and Diagnostics performed | Material producer behavior, artifact bytes, key collisions, route forms, release-binding drift, current PF sources, and exact negative searches are recorded with methods and results.

Evidence pointer: CRD | §11 Material risks and safeguards | Source-fixture tampering, writer overlap, provisional-history contamination, unsafe fields, route-taxonomy drift, stale bindings, duplicate keys, partial migration, and downstream misuse each have a corresponding safeguard.

Evidence pointer: CRD | §9 Rollback stops | Mixed v1/v2, duplicate path keys, direct companion writes, replay constants, broad writer fallback, incorrect shared history, cross-family writes, and premature release binding are all forbidden.

Evidence pointer: PF12 - PF12-Canon-HDE-Schemas-and-Artifacts | §8.3 Machine Evidence Index — JSONL mirror (records-only) [Required-Now] | The Mirror is canonical records-only JSONL, rejects unknown keys, requires unique bindings and `proof_anchor`, and maintains 1:1 parity with the Human Index.

Evidence pointer: PF14 - PF14-Canon-HDE-Mechanics-Guide | §1.3.1 Evidence jobs (single-writer tools) | PASS must derive from decisive predicates; canonical-byte equality cannot be replaced with parsed-object equality; negative-path tests are required; final artifacts and companions must be regenerated from final logic.

Evidence pointer: PF27 - PF27-Canon-Plan-Templates | §Review guardrails, Final generator logic rule | Final governed artifacts and companions must be regenerated or rerun from final generator logic before review or later drainage relies on them.

### Gate 7: Canon-changing ADRs, documentation consequences, and nonclaims — PASS

**Covered CRD items:** ADR-CANON-001; ADR-CANON-002; ADR-CANON-003; REV-001; REV-002; PF09.6 consequences; PF10 consequence; permanent documentation drainage and order.

**ADR-CANON-001 — APPROVED (`EXTENDS`)**

The ADR identifies the exact PF02/PF14 baseline, the missing pure convergence boundary, related current Repo mechanisms, rejected alternatives, the selected module/API/types/errors, affected and unchanged boundaries, compatibility and migration, PR-04/PR-05/PR-06 dependencies, validation, safeguards, rollback, adoption sequence, permanent PF02/PF14 drainage, and explicit nonclaims. Its engineering need is causal: without a pure source-neutral domain, the source-invariance proof must either duplicate architecture inside a generator or invoke out-of-scope persistence. The extension preserves the existing single Presenter and core purity.

Evidence pointer: CRD | ADR-CANON-001 | "add engine/bodygraph/projection.py with CanonicalBodyGraph, BodyGraphFields, BodyGraphProjectionError, and project_bodygraph()"; no PR-04 persistence or public contract is added.

Evidence pointer: PF02 - PF02-Canon-HDE-Architecture | §6.2 Vendor seam (concept only) | Vendor responses are normalized into internal structures, Core sees normalized data only, `engine/bodygraph/` is a sanctioned non-core seam, and public bytes remain Presenter-owned.

Evidence pointer: PF14 - PF14-Canon-HDE-Mechanics-Guide | §Source invariance (single presenter/emitter) | Same normalized inputs from DB and vendor must emit byte-identical bodies through the shared Presenter.

Evidence pointer: Repo | negative search | Exact symbols `CanonicalBodyGraph` and `project_bodygraph`; GitHub code search in the current repository; case-sensitive; 0 hits, followed by direct inspection of related adapter and ingest mechanisms.

**ADR-CANON-002 — APPROVED (`AMENDS`)**

The ADR identifies the exact PF09.6/PF12/PF14 baseline and the current v1 false-pass limitation; rejects preserving v1 or creating a second PR-specific truth home; specifies in-place v2 schemas, fields, paths, keys, fixtures, acquisitions, predicates, negative receipt, compatibility and no-dual-version migration; assigns producer/consumer/companion ownership; defines validation, safeguards, rollback, adoption order, plan consequences, permanent drainage, and nonclaims. The amendment strengthens evidence truth without changing public or runtime behavior.

Evidence pointer: CRD | ADR-CANON-002 | Current v1 can pass without DB/vendor bodies or hashes; selected decision is a closed in-place v2 family with independently acquired source runs and final-byte predicates.

Evidence pointer: PF09.6 - PF09.6-Canon-HDE-Build-Checklist-Distillation | HDE-DIST001.5 and HDE-DIST001.7 | BodyGraph source selection/invariance and same-input DB/vendor Presenter-byte equality are required.

Evidence pointer: PF12 - PF12-Canon-HDE-Schemas-and-Artifacts | §8.6.3.9 and Appendix C | The existing source-invariance AB/BA/summary paths are governed current evidence identities.

Evidence pointer: PF14 - PF14-Canon-HDE-Mechanics-Guide | §1.3.1 | A false-positive PASS requires decisive-predicate hardening, canonical-byte comparison, negative-path tests, and same-change final artifact regeneration.

**ADR-CANON-003 — APPROVED (`AMENDS`)**

The ADR now contains the complete transitive writer graph and the complete shared-history reconstruction contract. It identifies the exact PF09.6/PF12/PF14/PF27 baseline; the broad/focused writer conflict; wall-clock, import-side-effect, environment-pair, shared-history, direct-companion, and duplicate-key problems; rejected alternatives; the retirement guard; exact focused owners and write sets; the immutable four-row source fixture, row hashes, 1559-byte output and digest; atomic/check/fixed-point behavior; diagnostic append changes; dedicated PR-04 path/key/schema and direct/bridge acquisition contract; key and consumer migration; validation; risks; safeguards; rollback; adoption; plan consequences; permanent drainage; and nonclaims.

REV-001 and REV-002 are independently verifiable and resolved: the directly implicated collision set is fully allocated, and the shared historical owner can reproduce exactly the approved four-row body without PR-04, clock, unrelated primary, or direct companion writes.

Evidence pointer: CRD | ADR-CANON-003 | The ADR expressly retires the broad generator, assigns each primary, preserves one shared-history key/path, moves PR-04 to `artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json`, and requires all-order/fixed-point validation.

Evidence pointer: CRD | §14 Revision Response Ledger, REV-001 and REV-002 | Both items are `RESOLVED` with exact affected sections, canon effect, changes, evidence, drainage targets, and satisfied acceptance conditions.

Evidence pointer: PF27 - PF27-Canon-Plan-Templates | §Review guardrails | Path and artifact-key collisions are blocking until task-specific evidence, shared restoration, duplicate-key removal, companions, and final generator logic are coherent.

Evidence pointer: PF14 - PF14-Canon-HDE-Mechanics-Guide | §1.3.1 | Governed path proofs and evidence skeleton outputs remain bounded single-writer surfaces.

**PF09, PF10, drainage, and nonclaims**

The CRD maps only the materially affected PF09.6 rows, records their current statuses, and proposes no automatic movement. Current PF10 v12.2.1 is correctly treated as silent for PR-04; a future §2.4 entry is documentation drainage after approval, not a precondition or completed action. Every permanent drainage target has an exact document/section and a bounded effect. The CRD explicitly states that no PF file has been edited.

Evidence pointer: CRD | §10 PF09.6 consequences | HDE-DIST001.4/.5/.7/.9/.10/.11 and HDE-DIST002.5 each retain `No status change`.

Evidence pointer: CRD | §10 PF10 consequence | Current index contains PR-01 through PR-03; proposed PR-04 addendum is a later authorized documentation step only.

Evidence pointer: CRD | §10 Permanent documentation drainage and order | PF02, PF12, PF14, PF09.6, PF27, and PF10 targets identify exact topics, effects, order, and unchanged canon.

Evidence pointer: CRD | §12 Approval Limitations and Nonclaims | No implementation, plan revision, PF edit, QA, OPS, deployment, persistence, token satisfaction, acceptance, merge, status movement, slice completion, or epic closeout is claimed.

## 5. Findings

None.

## 7. Nonblocking Notes

1. PR #354 remains open and unmerged. Its current implementation is debugging and repo-reality evidence for the CRD; this approval is not implementation acceptance and does not authorize merging that provisional state.

2. PF10 v12.2.1 contains no active PR-04 entry. The three approved ADRs govern only their exact architectural scopes after this decision. A future PF10 entry and permanent PF02/PF09.6/PF12/PF14/PF27 edits remain documentation drainage and are not implementation or approval blockers.

3. The exact four-row shared Presenter source fixture, hashes, byte length, and output digest are implementation obligations to reproduce and test. Their inclusion in the approved CRD does not claim that the proposed fixture or producer already exists.

4. The CRD’s future-route-form uncertainty is acceptably bounded by `unknown` plus analyzer-derived FAIL. New route-registration syntax may require later taxonomy extension, but no CRD change is required now.

5. PR-05 mapped-cache persistence, OPS-01 live DB/bridge evidence, OPS-02 controlled mapped-cache proof, PR-06 final orchestration, QA, acceptance, and closeout remain downstream and retain their existing owners.

Evidence pointer: Repo | GitHub PR #354 metadata | "state=open"; "merged=false".

Evidence pointer: CRD | §13 Questions for the Implementation Agent | "None."

Evidence pointer: CRD | §11 Residual Unknowns | Future route forms and exhaustive legacy-invocation discovery are bounded by fail-closed analyzer and retirement-guard behavior.

## 8. Approval Scope and Nonclaims

This IA decision technically approves `CRD-HDE-EPIC038-PR-04 v1.4` as the governing rescoping decision for a later revision of the HDE-EPIC038 Current Implementation Plan.

The following architectural decisions are approved for their exact stated scopes:

- **ADR-CANON-001 (`EXTENDS`):** add the pure, source-neutral BodyGraph projection boundary defined in RSC-001 for configured-v2 mapped vendor output, deterministic mapped-DB fixture input, PR-04 evidence, and later PR-05 pre-write consumption. All public contracts, vendor transport, persistence, DB schema, and production authorization boundaries remain unchanged.
- **ADR-CANON-002 (`AMENDS`):** replace the existing source-invariance AB/BA/summary semantics in place with the closed v2, independent-acquisition, two-run, same-input, shared-Presenter, negative-control contract in RSC-002. Existing canonical paths and canonical keys remain the truth home; no parallel v1/v2 current family is approved.
- **ADR-CANON-003 (`AMENDS`):** retire the broad legacy evidence generator from current materialization; adopt the focused producer allocation, deterministic four-row shared-history reconstruction, updater-owned companion posture, dedicated PR-04 Presenter receipt, atomic migration, duplicate-key repair, active-consumer migration, and rollback contract in RSC-003.

These approved ADRs now govern their exact architectural scopes and may be used to revise the Current Implementation Plan. Permanent PF-Canon edits remain required later documentation drainage. No PF document has been edited by this review, and the absence of that later edit does not invalidate these bounded approved engineering decisions.

This approval does **not**:

- authorize or perform implementation;
- approve, accept, merge, or validate the provisional PR #354 implementation;
- revise the Approved Implementation Guide or Current Implementation Plan;
- edit PF10 or permanent PF-Canon;
- move any PF09.6 status;
- execute or authorize QA, OPS, live DB, live bridge, live vendor, deployment, migration, or persistence;
- satisfy acceptance tokens or proof labels;
- establish QA PASS, implementation completion, slice completion, epic acceptance, or closeout;
- reopen or reapprove historical PF09 rows or historical evidence;
- authorize public Reader, CLI, compat, route, payload, serializer, or transport changes;
- transfer mapped-cache write/read-back/idempotence work from PR-05 or live evidence from OPS-01/OPS-02.

Evidence pointer: CRD | §3 Required lifecycle after approval | IA approval is followed by separately authorized plan revision and implementation; documentation drainage remains separate.

Evidence pointer: CRD | §12 Approval Limitations and Nonclaims | The same implementation, plan, PF, QA, OPS, deployment, persistence, token, acceptance, merge, status, and closeout boundaries are explicit.

Evidence pointer: PF06 - PF06-Canon-Epic-Process-Guide | §0.2 Policy and principles | PF edits and status drainage are separate closure axes and are not performed by implementation or review artifacts.

## 9. Re-review Instructions

No re-review required.

DECISION: APPROVED
