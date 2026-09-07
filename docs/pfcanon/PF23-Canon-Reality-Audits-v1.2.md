# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.2

**Status:** Canon

**Effective date:** 2026-09-06

**Last Update Gate:** HDE-CRD-0001

---

**Intent & scope \[Required-Now\]**

These audits are **Codex review passes run by the Product Owner at the closure of each epic** to compare what actually shipped (code, evidence, repo layout) with what PF-Canon and the epic plan said should exist. Their purpose is to:

* Highlight any **gaps between reality and expectation** (missing evidence, drift from PF docs, unrecorded behavior, or unclosed issues).

* Produce a **historical record** of what was found at close (including any “unknowns” that become future work, PF10 addenda, PF20 issues, or PF09 updates).

* Feed back into canon and planning **after** the epic is closed, without blocking day-to-day execution.

These audits:

* Are **PO-only responsibilities**; they are **not** part of any agent plan, CRD, or implementation workflow.

* Do **not** introduce new acceptance gates for agents and must **not** be treated as tasks or subtasks in PF09 or PF20.

* Are **archived for history** as standalone artifacts (for example, under `audit/codex/...`) so future epics and doc updates can refer to them when reconciling drift.

Agents may **read** these audits as context when planning future work, but they do **not** schedule, trigger, or satisfy them.

# 1\) \- HD Engine Current Audit 

**Date:** 2026-09-06

# 

## **1\. Audit Snapshot Metadata**

| Field | Observed value |
| ----- | ----- |
| Artifact / version | HDE-CRD-0001-reality-audit-v1.0.md / 1.0; REALITY\_AUDIT; COMPLETE factual inspection |
| Class / change / producer | CRD / HDE-CRD-0001 / Isis-49, continuing Lead Developer |
| Capture completion | 2026-09-06T11:25:45+00:00 |
| Repository / branch | amthorn78/glow-hdengine-v2 / main |
| Inspected commit | 71307d9ae51927ec2886c3903e52e687834afc22 |
| Complete tree | fc0807339b343d6b0b8a20f6e3137a39b91a2fe2, as identified by the inspected commit; complete cached recursive inventory is bound to commit 71307d9ae51927ec2886c3903e52e687834afc22; 7,006 entries; truncated=false |
| Access / runtime | Read-only remote GitHub snapshot and verified off-repository text caches. Local repository worktree/dirty state, deployed environment, installed Python/Node and service health: Unknown; no checkout/runtime was inspected. |
| Predecessor posture | First complete integrated audit for this rerun. Preserve historical readiness v1.0 and cancelled QA-15; neither is overwritten or counted as a failed QA execution/retry. |
| Historical comparison | PF23 v1.1.9, audit dated 2026-08-21, commit 273889f1a09d609ffbf77f0c77711c6294484b8f. Historical facts are comparison evidence. |
| Selected operation | QA-10 — Audit Implementation and Establish QA Readiness, 090626.2 / GCFPE-20260906.2; same-Isis integrated assessment. |
| Related complete outputs | HDE-CRD-0001-change-audit-triage-v1.0.md; HDE-CRD-0001-qa-readiness-v1.1.md (separate analyses; this audit does not make those decisions). |
| Storage and publication | EPHEMERAL\_LIBRARY: /Glow HDE 3.0. Manual PF23 publication remains pending with the Product Owner. Source caches are TRANSIENT\_SCRATCH; repository and PF sources were read-only. |

This is a fresh integrated read-only factual audit. It reuses exact supporting evidence after checking its continuing applicability. It is neither a repeated PR acceptance nor a live QA execution. The separate triage owns Canon interpretation and the separate readiness result owns the progression decision. \[E-001, E-049, E-050\]

### **Exact approved and delivery lineage**

| Complete artifact | Native Library identity | Preserved state |
| ----- | ----- | ----- |
| HDE-CRD-0001-specification-v1.1-approved.md | libfile\_e5eb92b5d8808191848b3a170fd429ba | APPROVE — Thoth-17; exact v1.1 |
| HDE-CRD-0001-implementation-plan-v1.0.md | libfile\_342af81012a48191a48cb5b3ee82293c | Approved Plan v1.0; PR-01 → PR-02 → PR-03; Ops explicitly none |
| HDE-CRD-0001-implementation-plan-review-v1.0.md | libfile\_a27278b1002c8191baae35e939fb9374 | APPROVE — Isis-49; exact Plan v1.0 |
| HDE-CRD-0001-documentation-completion-v1.0.md | libfile\_73ca1e07dc488191bc40be296c657644 | COMPLETE; documentary completion, not live QA |
| HDE-CRD-0001-qa-readiness-v1.0.md | libfile\_608b30300108819192fcd6e1a11c9bcf | Historical READY\_FOR\_QA; original QA-10 090526.8 retained |
| HDE-CRD-0001-PR-01-pr-work-unit-lineage-review-v1.0.md | libfile\_31d0c4b37b688191af720fdb426dd519 | ACCEPT — PR-01 |
| HDE-CRD-0001-PR-02-pr-work-unit-lineage-review-v1.1.md | libfile\_d2cb91ee6e54819189a3840aa536fe76 | ACCEPT; PR-02 v1.1 supersedes its v1.0 |
| HDE-CRD-0001-PR-03-pr-work-unit-lineage-review-v1.0.md | libfile\_7556500f1b6c81918fce11b968ccf8ea | ACCEPT — PR-03 |
| HDE-CRD-0001-PR-01-pr-implementation-result-v1.1.md | libfile\_738b87a2979c8191b5bfbcfce152e27f | Implementation result |
| HDE-CRD-0001-PR-02-pr-implementation-result-v1.0.md | libfile\_3ccb62ef9278819194e4e6d4dc304e22 | Implementation result |
| HDE-CRD-0001-PR-03-pr-implementation-result-v1.0.md | libfile\_2bcab850c6c481919870f42fa290b4b5 | Implementation result |

Current governing Markdown was selected in Drive `Glow / Core Docs / PFCanon`: PF02 v2.4.5, PF03 v1.8.7, PF04 v2.8.5, PF05 v2.5.2, PF12 v2.9.5, PF14 v3.5.4, PF19 v3.0.3, PF23 v1.1.9 and PF27 v2.0.4. PF23 was freshly retrieved in full. Other complete source caches retain the current controlled versions confirmed by directory metadata. Supplied PF10 context is limited to the exact accepted artifacts and already-available §2.8–§2.12 records; discovered PF10 v13.0.6 metadata was not permission to read its body. Whole-current-PF10 overlap remains unverified and is an optional manual publication check. \[E-043–E-050\]

Cancelled QA-15 recovery: the actual local work contains source copies, repository text and a complete tree, with no located audit/triage report in that bounded work inventory; exact output-name discovery likewise returned no complete prior audit/triage. The two preserved source caches are not promoted to completed reports. User cancellation remains cancellation, with no QA execution retry consumed. Historical readiness v1.0 retains its original QA-10 090526.8 / GCFPE-20260905.6 usage and decision. \[E-051; N-008\]

### **Evidence register**

| ID | Source | Exact bounded locus | Directly observed excerpt or result |
| ----- | ----- | ----- | ----- |
| E-001 | GitHub branch main; complete recursive Git tree | Branch response / tree response | main \= 71307d9ae51927ec2886c3903e52e687834afc22; tree fc0807339b343d6b0b8a20f6e3137a39b91a2fe2; 7,006 entries; truncated=false. Fresh branch resolution and blob identity checks support one snapshot. |
| E-002 | Complete Git tree and locally parsed inventory | All root entries; path/mode/type fields | Root and material-home inventories below are derived from every returned tree entry, not a search sample. assert and import are zero-byte blobs. |
| E-003 | pyproject.toml | \[project\], \[project.scripts\], package discovery | glow-hdengine 0.0.0; requires-python \>=3.10; hdctl \= engine.cli.main; engine\*, adapter\*, presenter\*, catalog\*, math\* package families. |
| E-004 | requirements.txt; requirements-dev.txt; pytest.ini | Complete dependency and pytest configuration | Flask \>=2.3,\<3.0; gunicorn \>=21,\<22; psycopg \>=3.1,\<3.3; jsonschema 4.23; pytest \>=7.4,\<9 in dev requirements. These are declarations, not the inspector runtime. |
| E-005 | Procfile; run\_flask.py; adapter/app.py | web command; development entry; app factory import | Procfile selects adapter.factory(); run\_flask.py selects the same factory; adapter/app.py imports adapter.wsgi.create\_app. Configuration is not proof of the deployed process. |
| E-006 | adapter/factory.py; adapter/wsgi.py | Complete create\_app functions and mounts | Both factories mount Reader and compat; wsgi additionally wires environment/logging guards and health/ready routes. Factory applies compat response/error handling. Distinct factories must not be treated as interchangeable guard evidence. |
| E-007 | engine/core/core.py | Complete module; compute\_core and dataclasses | Normalized compatibility structures, neutral/directional results, deterministic ordering and input-derived computation. This module exists separately from currently wired compat computation. |
| E-008 | engine/sampler/core.py | Complete module; build\_candidate\_pool, rank\_candidates, sample\_and\_rank | Zero/nonpositive weight exclusion, score/band/diversity eligibility, deterministic comparator ordering, ranked output. Dataclasses and imported comparison/banding helpers define the inspected compute boundary. |
| E-009 | engine/runtime/public.py; engine/compat/compute.py; engine/compat/ordering.py | Reader/compat public paths and compatibility computation | Public paths use compat computation; Reader builds a harmony category. The inspected public runtime, HTTP compat and CLI files have zero compute\_core token hits (N-007); this is a bounded direct-wiring fact. |
| E-010 | engine/runtime/determinism\_env.py; engine/runtime/identity.py | Environment guard and manifest-derived identity functions | Closed-rail/pin handling is separate from compute; runtime identity derives from the packaged catalog manifest. Stored evidence does not establish the current deployed identity. |
| E-011 | adapter/http\_reader.py; adapter/wsgi.py; engine/http/compat\_handler.py | Complete route registration scan plus factories | Reader, aux, ops, sampler/conjunction and identity routes are registered in the inspected modules; compat blueprint is mounted by adapter factories. Route inventory below distinguishes methods from mount context. |
| E-012 | adapter/http\_reader.py | Reader handler and Reader response class | Reader validates dev inputs and emits canonical bytes; quoted digest ETag; conditional match returns empty 304 with Content-Type/Length removed; HEAD 200 is empty with computed length. Wildcard-containing If-None-Match is excluded by the inspected condition. |
| E-013 | engine/http/compat\_handler.py | Complete blueprint and compat handler | Blueprint prefix /api/compat/v1; GET body rejection uses invalid\_json; POST validates input mode; JSON bytes delegate to presenter; no-store responses and HEAD/OPTIONS behavior are explicit. |
| E-014 | adapter/http\_reader.py | Aux handlers and dev sampler/conjunction handlers | Aux text and gated dev surfaces have separate output/response paths. Internal sampler validates input then invokes sampler core. Route existence is not a permission to invoke it. |
| E-015 | engine/presenter/emitter.py; engine/serializer/canon.py; engine/stable/sercanon.py | Complete public emitter and serializer chain | emit\_public → canon.sercanon → stable.serialize → compact JSON, sort\_keys default true, ensure\_ascii=False, UTF-8 with one LF. |
| E-016 | presenter/reader\_v1/emitter.py | Complete module; \_dedupe\_and\_sort\_categories, emit\_reader\_v1 | Duplicate category IDs raise ValueError; allowed category keys are retained and IDs sorted. Hash preimage excludes idempotence\_hash; final envelope delegates to the same public emitter. |
| E-017 | engine/cli/main.py; engine/cli/**main**.py | Complete parser, top-level dispatch and exit handling | Subcommands: showcompat, aux-preview, bg, dev. Package entry calls cli. No \--crd-id option occurs in these complete parser/entry files (N-006). |
| E-018 | engine/cli/main.py; engine/cli/\_admin\_dump.py | showcompat dispatch, stdout writer, dump paths | showcompat stdout is the compat wrapper; \--dump-reader produces Reader bytes separately. Optional admin files are canonical sidecars. Conjunction mode emits a conjunction wrapper and refuses incompatible dump options. |
| E-019 | engine/cli/main.py | aux-preview, bg and dev implementations | Aux preview emits text and optional admin output; bg selects auto/db/vendor with explicit upsert/dry-run and birth inputs; dev reads fixtures and dispatches gated compute. |
| E-020 | engine/bodygraph/vendor\_client.py | Configuration, fetch/retry and default request implementation | HdApiClient builds requests, retries injected/default transport and parses responses. Actual default urllib transport checks process SAFE\_MODE=0 and ALLOW\_NETWORK=1 before I/O; redirects are handled by its rejecting handler. |
| E-021 | engine/bodygraph/resolver.py | resolve\_bodygraph and \_resolve\_vendor\_v2\_chart | auto/db branch explicitly reports DB resolution stubbed with no I/O. Vendor-v2 path separates preview from explicit upsert, chooses DB before vendor for durable work, refuses production-like writes and uses mapped-cache persistence. |
| E-022 | engine/bodygraph/mapped\_cache.py; engine/bodygraph/v2\_adapter.py | Validated projection, persistence and canonical readback | Mapped input projection feeds a transaction with a four-key conflict identity; row/readback checks compare canonical bytes. This is distinct from the raw-payload legacy ingest path. |
| E-023 | engine/db/adapter.py; engine/db/providers/psycopg\_provider.py; adapter/db\_access.py | DBAccess.for\_current\_env, provider, facade | Retired bridge-key presence is rejected before provider construction; DATABASE\_URL selects direct psycopg. Adapter facade re-exports the shared access layer; BodyGraph modules contain persistence SQL. |
| E-024 | engine/bodygraph/ingest.py; scripts/ingest/run\_vendor\_ingest.py; scripts/bodygraph/run\_refresh\_worker.py; scripts/db/run\_retention\_job.py | Complete ingest/worker main units and retention caller | Legacy ingest checks rails, obtains DB for writes, fetches vendor data, stores canonical payload, reads back and logs parity. Refresh persists rate/breaker/time state. Retention caller uses DBAccess and run\_bodygraph\_retention; the retention callee was not audited here. |
| E-025 | engine/charts/loader.py | Complete module; load\_chart, \_log\_call, \_call\_legacy | Loader reads SAFE\_MODE, uses perf\_counter/UTC time, selects legacy provider or fixture result, and writes artifacts/logs/loader\_call.jsonl in finally. This is an observed side-effecting engine module. |
| E-026 | tools/evidence/update\_evidence\_index.py; tools/evidence/orientation\_demo.py; tools/evidence/validate\_evidence\_paths.py | Updater ownership, convergence, orientation delegation and validators | Updater owns Human Index, sentinel, Mirror/checksum, orientation and companions. Compatibility orientation write delegates; \--check paths validate without repair. Publication is staged and converged. |
| E-027 | docs/evidence/INDEX.json; docs/evidence/INDEX.sha256; artifacts/evidence\_index.jsonl; audit/gates/topology/orientation\_demo.txt | Complete JSON/JSONL parsing and stored orientation result | 593 Human rows; 593 Mirror rows; one self\_record using discovered\_physical\_path; Human sentinel equals direct SHA-256 of inspected bytes. Current stored orientation says total\_artifacts=593 and status=ok. |
| E-028 | docs/ENDPOINTS\_CATALOG.json; artifacts/audit/ENDPOINTS\_CATALOG.json; tests/http/test\_endpoint\_catalog.py | Git symlink blob, target JSON and full tests | docs path is mode 120000, target ../artifacts/audit/ENDPOINTS\_CATALOG.json. Target has nine entries; success\_endpoints selects GET /reader. Tests require internal/non-A7 classification for identity and internal sampler. |
| E-029 | tools/qa/step\_log\_header.py; tests/qa/test\_qa\_tool\_ownership.py | Complete helper; omitted-claim and mutation/publication assertions | Omitted/None/empty claims remain empty; new outcomes clear earlier claims; explicit non-PASS claims and malformed token fields reject before mutation/write. Helper remains a reduced compatibility header, not full v2. |
| E-030 | tools/qa/qa\_harness.py | HarnessConfig; CRD record/validate/supersede entrypoints | Exactly one Epic or CRD identity; safe canonical CRD IDs; CRD root/check path validation; ordinary CRD recording without Epic map/viability; local flat current-state manifest; superseded logs retained. |
| E-031 | tools/qa/qa\_harness.py | Full-v2 render/parse; run\_pytest\_check | Fourteen-field primary header; actual command/provenance/exit/status/evidence; empty claims. Same sys.executable runs pytest readiness and tests. Unavailable prerequisites, tooling problems and behavior failures have separate classifications. |
| E-032 | tools/qa/qa\_harness.py; tools/evidence/update\_evidence\_index.py | \_publish\_with\_rollback; \_WriteTransaction; publish\_crd\_check\_family; \_crd\_generated\_rows | Governed CRD0001 publication checks prior graph, validates local family, runs sole updater, verifies final coherence inside one handled-exception rollback boundary. Admission rejects aliases/forgery before deduplication. Whole-family concurrent visibility/process-death recovery are outside this API promise. |
| E-033 | tests/qa/test\_generic\_qa\_harness.py; tests/qa/test\_qa\_tool\_ownership.py | CRD/status/schema/path/supersession and explicit-claim tests | Assertions cover ambiguity, traversal/symlink refusal, malformed manifests/primaries, actual same-interpreter outcomes, strict legacy operations, omitted claims and rejected-write preservation. Source inspection, not new test execution. |
| E-034 | tests/evidence/test\_evidence\_index\_missing\_state.py | Complete governed CRD publication and rollback test functions | Tests bind real files into both ledgers/proofs; repeatability and supersession preserve other records; forged rows fail; injected mid-write/final-verifier failures restore files/parents; rollback failure retains original cause and reports untrustworthy state. |
| E-035 | .github/workflows/ci.yml; ci/checks/classify\_ci\_changes.py | Complete workflow; repository-owned classifier invocation | Exact PR head checkout; PR supersession cancellation; seven selected lanes and changed-tests handling; same-interpreter pytest; final aggregate checks selection/outcomes and clean tree. Classifier is a tracked dependency; workflow source is not run success. |
| E-036 | .github/workflows/epic-closeout-validation.yml | Complete manual workflow | workflow\_dispatch; exact-ref checkout; contents read; candidate/evidence check modes; closed rails and clean-tree verification. Its Epic closeout purpose is distinct from ordinary PR and CRD QA. |
| E-037 | ci/jobs/rails\_closed\_refusal.yml; ci/jobs/rails\_open\_conformance.yml; ci/jobs/logs\_keys\_only\_redaction.yml | Complete reusable job declarations | All three declare live\_vendor\_calls forbidden; open conformance uses fixture/mocked checks. A job filename containing open does not authorize live vendor traffic. |
| E-038 | AGENTS.md; docs/qa\_harness\_pattern.md; docs/ADAPTER\_009.md; docs/acceptance/http\_transport\_evidence.md | Final PR-03 operative sections and complete harness guide | Native evidence, distinct states, eight operating routes, scoped CI direction, local/governed CRD publication boundaries and historical token scope are described. Transport documents retain the separately identified inherited predicates. |
| E-039 | HDE-CRD-0001-PR-03-pr-work-unit-lineage-review-v1.0.md; documentation-completion-v1.0.md | Final documentation inventory and completion assessment | Accepted review records 669 Markdown paths: 185 body-reviewed operative/source documents and 484 historical/reference records explicitly accounted for. Four authorized repo documents changed; this audit reuses that complete exact accepted review, not a new all-669 body review. |
| E-040 | Exact accepted PR reviews and implementation results listed in §1 | Accepted tested-state and delivery tables | PR01 corrected 149 \= 139 ownership \+ 10 compatibility; PR02 groups 167, 653, 90 and 52 overlap; PR03 V1–V8 documentation checks. All are historical implementation validation at their stated sources, not current live QA. |
| E-041 | Exact PR01/02/03 implementation results and accepted reviews | Hosted CI observations and PO scoped direction | Actual failed runs are retained in §10; billing-lock annotation is limited to the reported PR02 observation, not inferred for every failure. Existing Plan-wide override covers unavailability, not code/security review or substantive QA. |
| E-042 | PF23-Canon-Reality-Audits v1.1.9 | Complete historical audit, 2026-08-21, findings F-001–F-010 | Historical snapshot 273889f1a09d609ffbf77f0c77711c6294484b8f; historical local environment and root descriptions belong to that capture only. Comparison below preserves every authored historical finding. |
| E-043 | PF02-Canon-HDE-Architecture v2.4.5 | §1.1 Single homes; §2.1 Components & responsibilities; Endpoint Catalog routing | Handler mounting and role-based presenter delegation are expressly allowed. Loader side effects and public compat-vs-Core wiring are expressly identified as existing discrepancies. Canon classification is performed in the separate triage. |
| E-044 | PF12-Canon-HDE-Schemas-and-Artifacts v2.9.5 | §0.2 Routing and process ownership | Exact-source evidence and scoped decisions are primary; token fields are compatibility; valid empty arrays stay valid; catalogs/manifests/ledgers/proofs retain their artifact responsibilities. |
| E-045 | PF19-Canon-Glow-QA-Guide v3.0.3 | Change-lane QA applicability; §10.8 | CRD and Epic carry applicable QA rigor and distinct QA evidence. Permanent current-source/scope-equivalence wording remains separately pending alignment with the supplied PO correction; it is not silently rewritten here. |
| E-046 | PF27-Canon-Plan-Templates v2.0.4 | Exact-source acceptance; Step-log header; Executable helper boundary | Full v2 header has fourteen keys; five causal statuses; tokenless PASS is valid. Historical pinned helper warning describes an older source, not the full current helper result. |
| E-047 | PF14-Canon-HDE-Mechanics-Guide v3.5.4 | §0.2; §§1.3.1–1.3.2; §§1.6.1–1.6.3 | Mechanics owns components and jobs, single-writer evidence tooling and QA harness responsibilities; same-interpreter pytest and failure classification have established homes. |
| E-048 | PF04-Canon-HDE-Governance v2.8.5 | §2.0 Acceptance Tokens; Layered integrity; §2.0.0 | Tokens are optional indexing, not acceptance authority. Commit/PR/run/hash/manifest/attestation and scoped decisions each establish distinct facts. |
| E-049 | Notion QA-10 and current GCFPE Membership and Release Register | QA-10 090626.2; current selection GCFPE-20260906.2 | Current integrated QA-10 requires complete audit, historical comparison, triage and fresh readiness; manual PF10/PF23 informational publication is non-gating. Register explicitly directs this Isis-49 rerun. |
| E-050 | Eleven exact Library lineage files listed in §1 | Full-body retrieval and identity comparison | All eleven bodies were retrieved completely; old source-cache bodies matched after accounting for a terminal LF omitted by line-oriented retrieval. Raw Library file digests are not inferred from reconstructed line text. |
| E-051 | Visible user cancellation; qa15-work inventory; bounded Library filename search | Cancelled QA-15 evidence recovery | Recovered source Markdown, repository blobs and complete tree; no audit/triage report was located within that working inventory or exact named-output search. This is a bounded recovery result, not a global Library absence claim. |
| E-052 | Complete tree N-001/N-002; approved Plan and supplied PF10 excerpts | Future QA and deferred provenance scope | Selected CRD QA root and installed provenance procedure are Not found at this snapshot. Plan explicitly reserves actual QA and excludes deferred provenance implementation. |
| E-053 | Negative-proof methods in §13 | Complete bounded path/content searches | Each claimed nonexistence below has its exact searched unit and zero-hit result. Omitted probes/runtime metadata are Unknown, not missing product behavior. |
| E-054 | artifacts/hde-epic023\_orientation\_demo/orientation\_demo\_report.json | Complete stored historical orientation report | Historical orientation capture says total\_artifacts=252 and status=ok. It is distinct from the current topology output at audit/gates/topology/orientation\_demo.txt with 593\. |
| E-055 | PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.2 | §3.3 Reader parity; §4.1.3 CLI full-matrix diagnostic; §4.1.6; §5.6 | Reader parity uses \--dump-reader. Current full-result and catalog projection requirements are distinguished from pinned implementation-gap statements; their presence does not claim delivery. |

## **2\. Top-level Repo Map**

Every root entry from the complete tree is listed below. Types and byte sizes are Git metadata. A path name alone supplies no runtime, ownership or acceptance claim. \[E-001, E-002\]

| Root entry | Type | Git blob bytes |
| ----- | ----- | ----- |
| .audit\_src | directory | — |
| .backup\_epic004 | directory | — |
| .body200.json | file | 300 |
| .code304.txt | file | 4 |
| .devcontainer | directory | — |
| .env.example | file | 87 |
| .gitattributes | file | 123 |
| .github | directory | — |
| .gitignore | file | 586 |
| .tmp\_refusal\_get.txt | file | 325 |
| .tmp\_refusal\_post.txt | file | 325 |
| .vscode | directory | — |
| AGENTS.md | file | 45697 |
| ARCHITECTURE.md | file | 2191 |
| AcceptanceMap.md | file | 1657 |
| Approved Remediation Plan EPIC029.md | file | 1292 |
| CANON\_CHECKSUMS.json | file | 1479 |
| CHANGELOG.md | file | 41063 |
| EPIC023\_D12\_close\_pack\_manifest\_FINAL\_EVIDENCE.md | file | 8136 |
| FLASK\_AUTO\_RUN\_GUIDE.md | file | 17134 |
| HDE-EPIC023\_\_d07-codespaces-snapshot-d08-qa-doc-deltas-capture\_\_step\_report.md | file | 20373 |
| IMPLEMENTATION\_REPORT\_r7\_header\_template.md | file | 13644 |
| LICENSE | file | 1066 |
| Procfile | file | 128 |
| README.md | file | 46195 |
| Run | file | 0 |
| VERIFY.sh | file | 4539 |
| \_arch | directory | — |
| \_archive | directory | — |
| \_backup\_1761350008.tgz | file | 82375 |
| \_backup\_corrupted\_1761349750.tgz | file | 94584 |
| \_backup\_corrupted\_1761349780.tgz | file | 96598 |
| adapter | directory | — |
| adapters.DEPRECATED.md | file | 109 |
| artifacts | directory | — |
| assert | file | 0 |
| audit | directory | — |
| big.json | file | 33008 |
| card\_close.sh | file | 1085 |
| catalog | directory | — |
| changes\_report.txt | file | 3281 |
| ci | directory | — |
| code304\_new.txt | file | 4 |
| codex | directory | — |
| config | directory | — |
| dev | directory | — |
| dev\_sampler\_http\_consolidated.md | file | 1108 |
| docs | directory | — |
| engine | directory | — |
| errors | directory | — |
| fixtures | directory | — |
| freeze | directory | — |
| goldens | directory | — |
| handoff | directory | — |
| hde-epic023\_\_d05-d06-manifest-validation\_\_step\_report.md | file | 11453 |
| hde-epic023\_\_d10-d11-checks\_\_step\_report.md | file | 6269 |
| hde-epic023\_\_d10-d11-d12-checks\_\_step\_report.md | file | 8738 |
| hde-epic023\_\_d10-doc-delta-draft-check\_\_step\_report.md | file | 5433 |
| hde-epic023\_\_d11-close-report-final-remediation\_\_step\_report.md | file | 8403 |
| hde-epic023\_\_d11-close-report-remediation\_\_step\_report.md | file | 6960 |
| hde-epic023\_\_d12-close-pack-manifest-remediation\_\_step\_report.md | file | 7907 |
| hde-epic023\_\_d12-close-pack-manifest\_\_step\_report.md | file | 3679 |
| hde-epic023\_\_d13-d14-d15-evidence-indexing\_\_step\_report.md | file | 11628 |
| hde-epic023\_\_d13-d14-d15-evidence-indexing\_\_step\_report\_REMEDIATED.md | file | 17755 |
| hde-epic023\_\_d16-d17-d18-checks\_\_step\_report.md | file | 17759 |
| hde-epic023\_\_d16-d17-d18\_\_step\_report.md | file | 14303 |
| hde-epic023\_\_s2-d04-acceptance-alignment-validator\_\_step\_report.md | file | 8407 |
| import | file | 0 |
| internal | directory | — |
| manifest\_post.sha256 | file | 515513 |
| manifest\_pre.sha256 | file | 507113 |
| math | directory | — |
| migrations | directory | — |
| narratives | directory | — |
| notes | directory | — |
| parity | directory | — |
| patch.diff | file | 612 |
| presenter | directory | — |
| proofs | directory | — |
| pyproject.toml | file | 479 |
| pytest.ini | file | 442 |
| release | directory | — |
| reports | directory | — |
| requirements-dev.txt | file | 118 |
| requirements.txt | file | 78 |
| run\_d3\_2\_complete.sh | file | 1107 |
| run\_d3\_2\_validation\_complete.sh | file | 13027 |
| run\_flask.py | file | 1679 |
| run\_flask\_dev.sh | file | 981 |
| scan\_reports | directory | — |
| schemas | directory | — |
| scripts | directory | — |
| sql | directory | — |
| temp\_run.ec | file | 2 |
| temp\_run.err | file | 0 |
| temp\_run.out | file | 0 |
| tests | directory | — |
| tools | directory | — |
| validation | directory | — |

### **Material home inventory and coverage**

| Home | Recursive tracked blobs | Complete immediate children |
| ----- | ----- | ----- |
| engine | 98 | `__init__.py`, `bodygraph`, `canon`, `categories`, `charts`, `cli`, `compat`, `compliance`, `config`, `constants.py`, `core`, `db`, `emit_public.py`, `errors`, `http`, `magic10`, `mech`, `narratives`, `ops`, `order`, `presenter`, `presets`, `provider`, `providers`, `runtime`, `sampler`, `serializer`, `stable`, `testsupport`, `util`, `validation` |
| adapter | 17 | `__init__.py`, `app.py`, `cache_keys.py`, `db_access.py`, `env_guard.py`, `etag_core.py`, `factory.py`, `gunicorn.conf.py`, `http_reader.py`, `logging_filter.py`, `no_io_guard.py`, `retry_after.py`, `schemas`, `wsgi.py` |
| presenter | 4 | `__init__.py`, `json_canon_compare.py`, `reader_v1` |
| docs | 155 | `ADAPTER_009.md`, `ADAPTER_DB.md`, `CLI_commands.md`, `ENDPOINTS_CATALOG.json`, `ENDPOINTS_CATALOG.json.path_proof.txt`, `ENDPOINTS_CATALOG.json.sha256`, `ENDPOINTS_CATALOG.json.sha256.path_proof.txt`, `EVIDENCE_INDEX.md`, `INDEX.md`, `QA_CHECKLIST_EPIC020.md`, `RUN.md`, `SECRETS.md`, `SYNC_LOG.md`, `acceptance`, `acceptance_map_epic017.json`, `acceptance_map_epic017.json.path_proof.txt`, `acceptance_map_epic019.json`, `acceptance_map_epic019.json.path_proof.txt`, `acceptance_map_epic020.json`, `acceptance_map_epic021.json`, `acceptance_map_epic021.json.path_proof.txt`, `acceptance_map_epic022.json`, `acceptance_map_epic022.json.path_proof.txt`, `acceptance_map_epic023.json`, `acceptance_map_epic023.json.path_proof.txt`, `acceptance_map_epic024.json`, `acceptance_map_epic024.json.path_proof.txt`, `acceptance_map_epic027.json`, `acceptance_map_epic027.json.path_proof.txt`, `acceptance_map_epic028.json`, `acceptance_map_epic028.json.path_proof.txt`, `acceptance_map_epic029.json`, `acceptance_map_epic029.json.path_proof.txt`, `acceptance_map_epic030.json`, `acceptance_map_epic033.json`, `acceptance_map_epic033.json.path_proof.txt`, `acceptance_map_epic034.json`, `acceptance_map_epic034.json.path_proof.txt`, `acceptance_map_epic035.json`, `acceptance_map_epic035.json.path_proof.txt`, `acceptance_map_epic036.json`, `acceptance_map_epic036.json.path_proof.txt`, `acceptance_map_epic037.json`, `acceptance_map_epic037.json.path_proof.txt`, `acceptance_maps.json`, `adr`, `alpha_acceptance.md`, `architecture`, `auth-writers.md`, `changes`, `codespaces-codex-vcs-extension.md`, `config_and_bundles.md`, `contracts`, `crd`, `design`, `evidence`, `hde_epic019_remediation.md`, `idempotence.md`, `ops`, `pfcanon`, `plans`, `qa`, `qa_harness_pattern.md`, `run`, `schemas`, `server`, `transport-writers.md`, `validation-writers.md` |
| artifacts | 1022 | `CANON_CHECKSUMS.json`, `CHECKSUMS.txt`, `_closeout_validate.txt`, `adjacency_test_run.txt`, `admin`, `architecture`, `audit`, `bodygraph`, `canon`, `canon_report.json`, `canonical`, `cards`, `cli`, `compat`, `config_bundles`, `constants`, `core`, `db`, `db_bridge`, `db_discovery`, `db_discovery_20251113`, `ddl`, `det_report.json`, `det_report.json.sha256`, `dyad_AB.json`, `dyad_AB_debug.json`, `dyad_BA.json`, `dyad_BA_debug.json`, `engine`, `env`, `env_guard_import_ok.txt`, `epic003`, `epic004`, `epic007`, `epic020`, `errors`, `evidence_index.jsonl`, `evidence_index.jsonl.path_proof.txt`, `evidence_index.jsonl.sha256`, `evidence_index.jsonl.sha256.path_proof.txt`, `force_deploy.txt`, `goldens`, `hd_cli_admin.json`, `hdapi`, `hde-epic023_orientation_demo`, `headers`, `hotfix`, `idempotence`, `identity.txt`, `identity`, `ingest`, `invocation.json`, `live_vendor`, `logs`, `m10`, `math`, `mech`, `mvp`, `narratives`, `ops`, `parity`, `presenter`, `prod`, `proofs`, `provider`, `qa`, `reader`, `redaction`, `registry`, `release_id.txt`, `release_pack_manifest.json`, `reports`, `runtime`, `sampler`, `sanity`, `serializer`, `showcompat`, `thresholds`, `validation`, `vendor`, `writer` |
| audit | 3049 | `ASSESSMENT_epic006_part4.md`, `ASSESSMENT_part1.md`, `EPIC-008_MANIFEST.json`, `EPIC-008_QA_Report.md`, `EPIC-008_QA_Summary.json`, `EPIC-008_close_report.md`, `EPIC-010_MANIFEST.json`, `EPIC-010_close_report.md`, `EPIC-018_MANIFEST.json`, `EPIC-018_MANIFEST.json.path_proof.txt`, `EPIC-018_close_report.md`, `EPIC-018_close_report.md.path_proof.txt`, `EPIC-018_config_acceptance_map.json`, `EPIC-018_config_acceptance_map.json.path_proof.txt`, `EPIC-021_MANIFEST.json`, `EPIC-021_MANIFEST.json.path_proof.txt`, `EPIC-021_close_report.md`, `EPIC-021_close_report.md.path_proof.txt`, `EPIC-022_MANIFEST.json`, `EPIC-022_MANIFEST.json.path_proof.txt`, `EPIC-022_close_report.md`, `EPIC-022_close_report.md.path_proof.txt`, `EPIC-023_MANIFEST.json`, `EPIC-023_MANIFEST.json.path_proof.txt`, `EPIC-023_close_report.md`, `EPIC-023_close_report.md.path_proof.txt`, `EPIC-024_MANIFEST.json`, `EPIC-024_MANIFEST.json.path_proof.txt`, `EPIC-024_QA_RCA.md`, `EPIC-024_QA_RCA.md.path_proof.txt`, `EPIC-024_close_report.md`, `EPIC-024_close_report.md.path_proof.txt`, `EPIC-025_MANIFEST.json`, `EPIC-025_close_report.md`, `EPIC-026_MANIFEST.json`, `EPIC-026_MANIFEST.json.path_proof.txt`, `EPIC-026_close_report.md`, `EPIC-026_close_report.md.path_proof.txt`, `EPIC-027_MANIFEST.json`, `EPIC-027_MANIFEST.json.path_proof.txt`, `EPIC-027_close_report.md`, `EPIC-027_close_report.md.path_proof.txt`, `EPIC-028_MANIFEST.json`, `EPIC-028_MANIFEST.json.path_proof.txt`, `EPIC-028_close_report.md`, `EPIC-028_close_report.md.path_proof.txt`, `EPIC-029_MANIFEST.json`, `EPIC-029_MANIFEST.json.path_proof.txt`, `EPIC-029_close_report.md`, `EPIC-029_close_report.md.path_proof.txt`, `EPIC-030_MANIFEST.json`, `EPIC-030_MANIFEST.json.path_proof.txt`, `EPIC-030_QA_RCA.md`, `EPIC-030_close_report.md`, `EPIC-030_close_report.md.path_proof.txt`, `EPIC-033_READ_ONLY_REPO_READINESS_AUDIT.md`, `EPIC017_MANIFEST.json`, `EPIC017_MANIFEST.json.path_proof.txt`, `EPIC017_close_report.md`, `EPIC017_close_report.md.path_proof.txt`, `EPIC017_closeout_notes.md`, `EPIC017_closeout_notes.md.path_proof.txt`, `EPIC019_MANIFEST.json`, `EPIC020_MANIFEST.json`, `EVIDENCE_INDEX.jsonl`, `PR02_session_diff_report.md`, `REPORT.txt`, `adr_body_graphs_adr.path_proof.txt`, `bootstrap`, `codex`, `codex_survey_epic007.json`, `db_plan`, `docdeltas`, `docs_delta_r7`, `docs_discovery_r7`, `docs_phase8`, `docs_snapshot`, `docs_snapshot_r7`, `gates`, `inventory_epic007.json`, `observed_gate_counts.json`, `ops`, `pf09_recheck`, `preflight`, `qa` |
| catalog | 24 | `__init__.py`, `channels_catalog_v1.json`, `channels_v1.json`, `gates_v1.json`, `magic10.json`, `magic10_caps.json`, `magic10_seeds.json`, `manifest.json`, `manifest.json.path_proof.txt`, `narratives` |
| schemas | 41 | `architecture_snapshot.keys_only.v1.json`, `architecture_snapshot.keys_only.v1.json.path_proof.txt`, `bodygraph_source_invariance.run.v2.json`, `bodygraph_source_invariance.run.v2.json.path_proof.txt`, `bodygraph_source_invariance.summary.v2.json`, `bodygraph_source_invariance.summary.v2.json.path_proof.txt`, `bodygraph_v2_mapped_cache_manifest.v1.json`, `bodygraph_v2_mapped_cache_manifest.v1.json.path_proof.txt`, `bodygraph_v2_mapped_cache_transcript.v1.json`, `bodygraph_v2_mapped_cache_transcript.v1.json.path_proof.txt`, `canon_checksums_v2.schema.json`, `channels_catalog_v1.schema.json`, `channels_v1.schema.json`, `epic_close_candidate_source.v1.json`, `gates_v1.schema.json`, `hdapi.normalized.v1.schema.json`, `hde_epic038_direct_db_selection.v1.json`, `hde_epic038_direct_db_selection.v1.json.path_proof.txt`, `hde_epic038_ops03_authorization.v1.json`, `hde_epic038_ops03_authorization.v1.json.path_proof.txt`, `hde_epic038_ops03_db_posture_summary.v1.json`, `hde_epic038_ops03_db_posture_summary.v1.json.path_proof.txt`, `hde_epic038_ops03_env_presence.v1.json`, `hde_epic038_ops03_env_presence.v1.json.path_proof.txt`, `hde_epic038_ops03_failure_receipt.v1.json`, `hde_epic038_ops03_failure_receipt.v1.json.path_proof.txt`, `hde_epic038_ops03_nonclaims.v1.json`, `hde_epic038_ops03_nonclaims.v1.json.path_proof.txt`, `hde_epic038_ops03_result_summary.v1.json`, `hde_epic038_ops03_result_summary.v1.json.path_proof.txt`, `hde_epic038_ops03_validation_receipt.v1.json`, `hde_epic038_ops03_validation_receipt.v1.json.path_proof.txt`, `hde_release_attestation.v1.json`, `hde_release_attestation_failure.v1.json`, `presenter_db_bridge_compare.v1.json`, `presenter_db_bridge_compare.v1.json.path_proof.txt`, `proofs.reader_success.v1.json`, `proofs.reader_success.v1.json.path_proof.txt`, `reader.v1.schema.json`, `reader.v1.schema.json.sha256`, `toggles_v1.schema.json` |
| tests | 302 | `_helpers`, `adapter`, `adapters`, `arch`, `artifacts`, `audit`, `bodygraph`, `canon`, `categories`, `cli`, `compare`, `compat`, `compliance`, `config`, `conftest.py`, `core`, `db`, `em`, `epic003`, `evidence`, `fixtures`, `goldens`, `hdctl`, `http`, `identity`, `infra`, `integration`, `invariance`, `loader`, `m10`, `mech`, `ops`, `order`, `provider`, `qa`, `reader_v1`, `runtime`, `scripts`, `support`, `test_catalog_canon.py`, `test_pipeline_properties.py`, `test_pipeline_public.py`, `test_resolver_prod_rules.py`, `test_sercanon.py`, `tools`, `transport`, `unit` |
| tools | 98 | `__init__.py`, `audit`, `cli`, `config`, `diagnostics`, `errors`, `evidence`, `generate_registry_report.py`, `lint_emit_paths.py`, `ops`, `order`, `presenter`, `qa` |
| scripts | 66 | `__init__.py`, `_emit_canon_checksums.py.REMOVED.md`, `architecture_capture.sh`, `audit`, `bodygraph`, `card_close.sh`, `card_close.sh.bak`, `cli`, `cut_release_manifest.py`, `db`, `db_adapter`, `demo_mvp.sh`, `dev_start_reader.sh`, `diag_env.sh`, `emit_env_guard_artifact.py`, `ensure_env.py`, `hd_cli.py`, `hd_resolve.py.REMOVED.md`, `hdapi_cli.py`, `hdctl.backup.py`, `hdctl.clean.py`, `hdctl.py`, `hdctl.py.bak`, `hello_demo.py`, `identity_bump.py.REMOVED.md`, `ingest`, `make_audit.sh`, `make_change_snapshot.sh`, `make_cli_smoke_audit.sh`, `make_compat_determinism_artifacts.py`, `make_reader_v1_goldens.py`, `make_release_pack.sh`, `make_source_bundle.sh`, `ops`, `probe_internal_version.py`, `qa`, `release_id.sh`, `release_id_recompute.py`, `release_id_tools.py`, `run_gate_canon.sh`, `run_sanity.sh`, `runtime`, `scratch.py`, `start_web.sh`, `validate`, `validate_canon.sh.REMOVED.md`, `validate_det.sh` |
| ci | 13 | `checks`, `jobs` |
| proofs | 6 | `AB_BA_PARITY.txt`, `HELP_OK.txt`, `READER_CLI_PARITY.txt`, `SERIALIZER_GUARD.txt`, `SUCCESS_SHAPE.txt`, `TWO_RUN_IDENTITY.txt` |
| fixtures | 17 | `charts`, `hdapi` |
| goldens | 14 | `reader` |
| release | 1 | `manifest.sorted.json` |
| reports | 2 | `qa_acceptance_tokens.json`, `tokens_summary.txt` |
| validation | 2 | `acceptance_map.txt`, `service_cmd.txt` |
| config | 2 | `bands_4B60_v1.json`, `toggles_v1.json` |
| sql | 1 | `check_schema.sql` |
| migrations | 3 | `005_identity.sql`, `008_writers_auth.sql`, `011_body_graphs_durability.sql` |

The engine/adapter/presenter homes contain runtime and output code; tests and ci contain assertions and orchestration; tools and scripts contain evidence/QA/operations callers. docs, artifacts, audit, catalog, schemas, fixtures, goldens, proofs and release are distinct source/evidence/configuration families. Archive, handoff, backup, reports and root report files are retained inventory, not promoted to current executable authority. Full root/path inventory is complete; executable inspection is the declared set below rather than all repository blobs. \[E-002, E-003–E-041\]

### **Addressed repository source coverage**

Regular cached blobs were checked against the pinned tree Git object identity. Line-oriented retrieval normalization was corrected only where exact Git blob hashing confirmed the bytes. The docs catalog is the explicit symlink exception. Full retrieval makes each unit addressable; the evidence register identifies the actual relied-on bounded implementations, registrations and callers. \[E-001, E-028, E-050\]

| Retrieved source | Pinned Git blob identity | Inspection boundary |
| ----- | ----- | ----- |
| [.github/workflows/ci.yml](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/.github/workflows/ci.yml) | a35e8670229c7b7b1a6549ba70b15322dc39e4ab | complete blob retrieved; relied-on units and callers inspected |
| [.github/workflows/epic-closeout-validation.yml](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/.github/workflows/epic-closeout-validation.yml) | 959e4a6fb69198adeb86266d753e195faa06c0d7 | complete blob retrieved; relied-on units and callers inspected |
| [AGENTS.md](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/AGENTS.md) | 2bb1c7118dcaea9331c3dbbba479f5dd9d61ec6d | complete blob retrieved; relied-on units and callers inspected |
| [Procfile](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/Procfile) | e9ab44a0aea6bb519284284ad21ab4269de881d4 | complete blob retrieved; relied-on units and callers inspected |
| [adapter/app.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/adapter/app.py) | 6468fe10a43ad4e8ff5ca659cb03d0d8c770cb44 | complete blob retrieved; relied-on units and callers inspected |
| [adapter/db\_access.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/adapter/db_access.py) | 1e25607cb66731f0fbb4433f9a0e3028fe17af50 | complete blob retrieved; relied-on units and callers inspected |
| [adapter/env\_guard.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/adapter/env_guard.py) | ba0cb043c469927e2ef18a6f7ffd5d26e11e2f72 | complete blob retrieved; relied-on units and callers inspected |
| [adapter/factory.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/adapter/factory.py) | 9dbccfeab7ea7db75665450b2d13c3d45af21961 | complete blob retrieved; relied-on units and callers inspected |
| [adapter/http\_reader.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/adapter/http_reader.py) | 0cfeafefc79c914955b3b457ee4ea4226e4471c4 | complete blob retrieved; relied-on units and callers inspected |
| [adapter/logging\_filter.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/adapter/logging_filter.py) | 3da3cbadb0896bcd3a75986aa893d8d467e4d5be | complete blob retrieved; relied-on units and callers inspected |
| [adapter/wsgi.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/adapter/wsgi.py) | eb416764580b1b70606d537c51a1354c2a6f4bd1 | complete blob retrieved; relied-on units and callers inspected |
| [artifacts/audit/ENDPOINTS\_CATALOG.json](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/artifacts/audit/ENDPOINTS_CATALOG.json) | f6a378970fbb4be9833d1c8136d17406eac23254 | complete blob retrieved; relied-on units and callers inspected |
| [artifacts/evidence\_index.jsonl](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/artifacts/evidence_index.jsonl) | 1ee8718e3f1275af1e2db2602bd600bf31bf5b40 | complete blob retrieved; relied-on units and callers inspected |
| [artifacts/hde-epic023\_orientation\_demo/orientation\_demo\_report.json](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/artifacts/hde-epic023_orientation_demo/orientation_demo_report.json) | 37ce26003f1236092ae5c25907b1b32de23933a9 | complete blob retrieved; relied-on units and callers inspected |
| [artifacts/hde-epic023\_orientation\_demo/sample\_result.json](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/artifacts/hde-epic023_orientation_demo/sample_result.json) | 1757520e6f6af4e57d5ed775982a026c997ab37f | complete blob retrieved; relied-on units and callers inspected |
| [ci/checks/check\_evidence\_index\_hash.sh](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/ci/checks/check_evidence_index_hash.sh) | 0c562cd882125249ccb462e6aa197f52ee348c99 | complete blob retrieved; relied-on units and callers inspected |
| [ci/checks/check\_mirror\_schema.sh](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/ci/checks/check_mirror_schema.sh) | 78ba46814cbc219dfee1bb46fda5f5379fdc3e2c | complete blob retrieved; relied-on units and callers inspected |
| [ci/checks/classify\_ci\_changes.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/ci/checks/classify_ci_changes.py) | 64abae0c3a2ac820828d2f73de989614317ebd3a | complete blob retrieved; relied-on units and callers inspected |
| [docs/ADAPTER\_009.md](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/docs/ADAPTER_009.md) | 239c74a89673ccdcf22b7c7e5469148a67b59ac1 | complete blob retrieved; relied-on units and callers inspected |
| [docs/ENDPOINTS\_CATALOG.json](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/docs/ENDPOINTS_CATALOG.json) | 5d041e91a8c01957975e16c715aa7bdd7d3b06b3 | tracked symlink; cached JSON is dereferenced target, not raw symlink bytes |
| [docs/acceptance/http\_transport\_evidence.md](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/docs/acceptance/http_transport_evidence.md) | 0cb53fc8ad0fa379bb382cbb07b84fb8b6e2f73f | complete blob retrieved; relied-on units and callers inspected |
| [docs/evidence/INDEX.json](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/docs/evidence/INDEX.json) | 896c705d2678c38684380252d41078b1e0818d0e | complete blob retrieved; relied-on units and callers inspected |
| [docs/evidence/INDEX.sha256](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/docs/evidence/INDEX.sha256) | d990e3e530c23be8b043bf11919710607ebf06ae | complete blob retrieved; relied-on units and callers inspected |
| [docs/qa\_harness\_pattern.md](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/docs/qa_harness_pattern.md) | 0da679193a756b6e24bd59991bc8f0aecfa52273 | complete blob retrieved; relied-on units and callers inspected |
| [engine/bodygraph/ingest.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/bodygraph/ingest.py) | 02e2ce6140160d4a56a1be9f6b2474417cad3447 | complete blob retrieved; relied-on units and callers inspected |
| [engine/bodygraph/mapped\_cache.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/bodygraph/mapped_cache.py) | 6537712351e3b0e2074afc84122296ef16b93963 | complete blob retrieved; relied-on units and callers inspected |
| [engine/bodygraph/resolver.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/bodygraph/resolver.py) | b1048694d87a7d638ef18c0043dd3ed5b0f15b95 | complete blob retrieved; relied-on units and callers inspected |
| [engine/bodygraph/v2\_adapter.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/bodygraph/v2_adapter.py) | e2742256108d712fb13938c3d9cb92f8872c8139 | complete blob retrieved; relied-on units and callers inspected |
| [engine/bodygraph/vendor\_client.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/bodygraph/vendor_client.py) | ac98075772da2c446abed8d3bfb422143c82c0af | complete blob retrieved; relied-on units and callers inspected |
| [engine/charts/loader.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/charts/loader.py) | 8ea4dce2602d653a7de0d510d56a0f85cc1f585b | complete blob retrieved; relied-on units and callers inspected |
| [engine/cli/**main**.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/cli/__main__.py) | eb8cefbb7f7ca0457a130ad316a108388b667e75 | complete blob retrieved; relied-on units and callers inspected |
| [engine/cli/\_admin\_dump.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/cli/_admin_dump.py) | 3a1bb3261229f11c23866a250e2c16de0cd37e7c | complete blob retrieved; relied-on units and callers inspected |
| [engine/cli/main.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/cli/main.py) | eb9e23db13c24d33770c5335dda215ec21c66c59 | complete blob retrieved; relied-on units and callers inspected |
| [engine/compat/compute.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/compat/compute.py) | f3107aef3370e5b9e19f1452c3bca8ef6eda8691 | complete blob retrieved; relied-on units and callers inspected |
| [engine/compat/ordering.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/compat/ordering.py) | 48952a9a4b4aa464b64f7b22a00d31efeb0ab6fb | complete blob retrieved; relied-on units and callers inspected |
| [engine/core/core.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/core/core.py) | 07c088507c03f0125c48e61fa9b2aa07812db4b3 | complete blob retrieved; relied-on units and callers inspected |
| [engine/db/adapter.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/db/adapter.py) | b4cd8ed140905ea304c179bd21794439b5292a4f | complete blob retrieved; relied-on units and callers inspected |
| [engine/db/providers/psycopg\_provider.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/db/providers/psycopg_provider.py) | 3aefa0cb5ade166840392c9040000ccf60128db7 | complete blob retrieved; relied-on units and callers inspected |
| [engine/http/compat\_handler.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/http/compat_handler.py) | 8851aad4c7204f5fb9a131c932f5fc956a4110ef | complete blob retrieved; relied-on units and callers inspected |
| [engine/presenter/emitter.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/presenter/emitter.py) | 63f4896cb8902372ee536063e2d848dab1595f26 | complete blob retrieved; relied-on units and callers inspected |
| [engine/provider/base.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/provider/base.py) | 2a60be5b2488a72d33e5a03c32f39cc5b051ccad | complete blob retrieved; relied-on units and callers inspected |
| [engine/provider/internal\_engine.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/provider/internal_engine.py) | b5b8317884576dfd949f585f7612deebcfbea5c9 | complete blob retrieved; relied-on units and callers inspected |
| [engine/provider/vendor\_http.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/provider/vendor_http.py) | b0851b0bb82d46efb9d5d014f4174c66a4f8ca3a | complete blob retrieved; relied-on units and callers inspected |
| [engine/providers/internal\_engine.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/providers/internal_engine.py) | 817878511dfc2fe66049925ddb036302a74e237d | complete blob retrieved; relied-on units and callers inspected |
| [engine/providers/vendor\_http.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/providers/vendor_http.py) | aa24c80f501c809b1598b5acdbf8ac0b74f82905 | complete blob retrieved; relied-on units and callers inspected |
| [engine/providers/vendor\_http\_hdapi.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/providers/vendor_http_hdapi.py) | 109576079968403ad8e0db7ca1b3db562d35b970 | complete blob retrieved; relied-on units and callers inspected |
| [engine/runtime/**init**.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/runtime/__init__.py) | 29a1826f602eba0bdc39f26dc8d033bbab7a3acb | complete blob retrieved; relied-on units and callers inspected |
| [engine/runtime/determinism\_env.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/runtime/determinism_env.py) | afb75e14c9a993ef1d31d7bb6e3b214cea7a4b91 | complete blob retrieved; relied-on units and callers inspected |
| [engine/runtime/identity.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/runtime/identity.py) | b082b17e049a9d5b26ddd34934b8572668e5d576 | complete blob retrieved; relied-on units and callers inspected |
| [engine/runtime/public.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/runtime/public.py) | f3dd0149c2a019a557f765f6d034f579e98ec941 | complete blob retrieved; relied-on units and callers inspected |
| [engine/sampler/core.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/sampler/core.py) | a1ea0a2966f2e342fc58cffaf06485ee031f8f7e | complete blob retrieved; relied-on units and callers inspected |
| [engine/serializer/canon.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/serializer/canon.py) | 05508f3163ad5a2e6a5f1efa7b5e7930086ddec6 | complete blob retrieved; relied-on units and callers inspected |
| [engine/stable/sercanon.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/stable/sercanon.py) | d0375b59f7aacfcbda4826a8d0b07b20736ac9b7 | complete blob retrieved; relied-on units and callers inspected |
| [engine/validation/viewer\_prefs.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/engine/validation/viewer_prefs.py) | 180e264d9e75b49d7829c60dd539bce521b6938c | complete blob retrieved; relied-on units and callers inspected |
| [presenter/reader\_v1/emitter.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/presenter/reader_v1/emitter.py) | 8c24638f9f7c717a4e964e1834b9d253dbed9b67 | complete blob retrieved; relied-on units and callers inspected |
| [pyproject.toml](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/pyproject.toml) | 352380348047c532834d2a5d7ccc401bd52601c3 | complete blob retrieved; relied-on units and callers inspected |
| [pytest.ini](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/pytest.ini) | 4ce55429eb54d8f10368fafdc496835845ad41e3 | complete blob retrieved; relied-on units and callers inspected |
| [requirements-dev.txt](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/requirements-dev.txt) | 8d00fd81cf752f365f1cc94efb6bd6b48bb8776e | complete blob retrieved; relied-on units and callers inspected |
| [requirements.txt](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/requirements.txt) | 9b8afb3aed17650687ff700033a146a25a587b08 | complete blob retrieved; relied-on units and callers inspected |
| [run\_flask.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/run_flask.py) | 61493b36fb16ef53a4ca23fdd142521d04380b64 | complete blob retrieved; relied-on units and callers inspected |
| [scripts/bodygraph/run\_refresh\_worker.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/scripts/bodygraph/run_refresh_worker.py) | df2e12ea48ba04a30690e71feb07bf8905a20b3d | complete blob retrieved; relied-on units and callers inspected |
| [scripts/ingest/run\_vendor\_ingest.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/scripts/ingest/run_vendor_ingest.py) | b36b30212e1869deca73a8c7d187c97a51cb6684 | complete blob retrieved; relied-on units and callers inspected |
| [tests/bodygraph/test\_v2\_mapped\_cache.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tests/bodygraph/test_v2_mapped_cache.py) | a484be56cc6c6c875cba52150f43a0a562875e09 | complete blob retrieved; relied-on units and callers inspected |
| [tests/cli/test\_cli\_canonical\_bytes.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tests/cli/test_cli_canonical_bytes.py) | cceb0bbd94de607ee059a909df43e321cf9334ad | complete blob retrieved; relied-on units and callers inspected |
| [tests/evidence/test\_evidence\_index\_missing\_state.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tests/evidence/test_evidence_index_missing_state.py) | 4d327b7c6cf0dce2200611cd55239703f65fadbf | complete blob retrieved; relied-on units and callers inspected |
| [tests/http/test\_compat\_endpoint\_contract.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tests/http/test_compat_endpoint_contract.py) | b2fac742721d7d120d5597999745e475d561782e | complete blob retrieved; relied-on units and callers inspected |
| [tests/http/test\_endpoint\_catalog.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tests/http/test_endpoint_catalog.py) | 92e6ba7d8f355a3eece20361cca0bfd04c4cbc91 | complete blob retrieved; relied-on units and callers inspected |
| [tests/http/test\_reader\_a7\_transport.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tests/http/test_reader_a7_transport.py) | 1b9903c772f5415bb713ceba48fb8973722f1963 | complete blob retrieved; relied-on units and callers inspected |
| [tests/qa/test\_generic\_qa\_harness.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tests/qa/test_generic_qa_harness.py) | de3cf4d2af15279ff552ae10613c74b6c710502e | complete blob retrieved; relied-on units and callers inspected |
| [tests/qa/test\_qa\_tool\_ownership.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tests/qa/test_qa_tool_ownership.py) | 308c10e16113bafd2959ce4986c9b183f3d0b963 | complete blob retrieved; relied-on units and callers inspected |
| [tools/evidence/orientation\_demo.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tools/evidence/orientation_demo.py) | 6c49024720e94071b2ae327a1d1fef53a67a905e | complete blob retrieved; relied-on units and callers inspected |
| [tools/evidence/update\_evidence\_index.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tools/evidence/update_evidence_index.py) | 9fae492aff8b4db3f5e9974b40c37bbc1a29b038 | complete blob retrieved; relied-on units and callers inspected |
| [tools/evidence/validate\_evidence\_paths.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tools/evidence/validate_evidence_paths.py) | 907eebbd551a1b3c4fb863f822e4f0d6fceb4380 | complete blob retrieved; relied-on units and callers inspected |
| [tools/qa/epic021\_qa.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tools/qa/epic021_qa.py) | 93a7fd6e62377ade6e6e72c16d5f9fc34b3fa9af | complete blob retrieved; relied-on units and callers inspected |
| [tools/qa/qa\_harness.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tools/qa/qa_harness.py) | c325fe6e51f1814f34e67dda0d6f3108d6a0fd7b | complete blob retrieved; relied-on units and callers inspected |
| [tools/qa/step\_log\_header.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/tools/qa/step_log_header.py) | e5cb1a712c06a9562cda3bf388c4087bd36086d2 | complete blob retrieved; relied-on units and callers inspected |
| [audit/gates/topology/orientation\_demo.txt](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/audit/gates/topology/orientation_demo.txt) | 5cf5f58f88d75c0c985a13b986750077395a74e2 | complete blob retrieved; relied-on units and callers inspected |
| [ci/jobs/logs\_keys\_only\_redaction.yml](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/ci/jobs/logs_keys_only_redaction.yml) | 015ea26b4f1520629b3c9e51643b07c276a4cf29 | complete blob retrieved; relied-on units and callers inspected |
| [ci/jobs/rails\_closed\_refusal.yml](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/ci/jobs/rails_closed_refusal.yml) | c159b502ee5b71655538c50f7af211e0564f871e | complete blob retrieved; relied-on units and callers inspected |
| [ci/jobs/rails\_open\_conformance.yml](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/ci/jobs/rails_open_conformance.yml) | c42301f90d425fae6f630ebbafea4b184d5fd67f | complete blob retrieved; relied-on units and callers inspected |
| [presenter/json\_canon\_compare.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/presenter/json_canon_compare.py) | cdd8d9246331f53c674fa4523bc8a0bd5cf9b9b5 | complete blob retrieved; relied-on units and callers inspected |
| [scripts/db/run\_retention\_job.py](https://github.com/amthorn78/glow-hdengine-v2/blob/71307d9ae51927ec2886c3903e52e687834afc22/scripts/db/run_retention_job.py) | d652061aa1956ba09a99b5b33d5c8ba01411cff8 | complete blob retrieved; relied-on units and callers inspected |

## **3\. Packaging and Entrypoints**

The package registers `hdctl` to `engine.cli.main:cli`; `engine.cli.__main__` calls that dispatcher. Python compatibility, packaged families and dependency declarations are in E-003/E-004. The dependency declarations do not identify a currently installed execution environment.

The configured web command in Procfile selects `adapter.factory:create_app()` under gunicorn. The development launcher uses that factory. `adapter/app.py` instead imports the WSGI factory. Both factories mount Reader and compat, but their additional guards/health/error wiring differs. This audit therefore records both entrypoints and the actual configured one, without asserting which process is deployed. Historical PF23's WSGI-primary description is compared in FND-011. \[E-005, E-006\]

## **4\. Engine Modules**

`engine.core.core` defines normalized compatibility computation with deterministic ordering and separate neutral/directional results. `engine.sampler.core` builds an eligible pool, excludes nonpositive weights, applies explicit score/band/diversity constraints, and ranks through deterministic comparators. The complete two source modules were read; this is a bounded dataflow account, not a transitive runtime purity proof for every import or the engine package. \[E-007, E-008\]

The current public runtime, compatibility HTTP and CLI use the compat implementation rather than directly calling `compute_core`. The runtime Reader construction exposes a harmony category; it does not establish a complete ten-category Human Design computation. Direct-reference proof is bounded to three complete wiring files (N-007), supplemented by the observed compat calls and the separately present Core module. \[E-009, E-013, E-018\]

Runtime environment/identity modules, BodyGraph resolver/ingest/cache, provider packages, DB access, CLI, and chart loading carry different responsibilities from compute. The complete chart loader performs environment reads, timing, correlation/provider handling and logging to `artifacts/logs/loader_call.jsonl`; its new-signature fixture path returns a minimal fixture chart, while the legacy path resolves a provider. It is not evidence that all engine code is effect-free. \[E-010, E-020–E-025\]

Current source establishes ordering and explicit seams. Numerical correctness, production behavior, complete domain coverage and live determinism remain verification questions for appropriately scoped work, not claims from this static inspection.

## **5\. Adapter / HTTP Surfaces**

The following inventory comes from complete registration units and their factory mounting. Declared GET routes can receive Flask's implicit HEAD/OPTIONS behavior; the table identifies explicit methods where they differ. It does not count implicit methods as independently audited implementations. \[E-006, E-011\]

| Path | Methods | Mount / exposure context | Observed behavior |
| ----- | ----- | ----- | ----- |
| /reader | GET; implicit HEAD; separately registered POST refusal | Reader application mounted through adapter factories; dev input guard | Reader envelope/canonical JSON; conditional GET and HEAD described in E-012 |
| /api/compat/v1 | GET, POST, HEAD, OPTIONS | engine.http blueprint mounted by adapter | Compat canonical JSON; typed refusals; no-store |
| /api/aux/narrative; /aux/narrative | GET | Reader/aux application | Aux text, success/suppression and caching branches |
| /ops/db/unavailable; /ops/probe/env | GET | Reader/ops application | Diagnostic/guard surfaces; values were not probed |
| /ops/rails/refusal | GET, POST | Reader/ops application | Explicit refusal/rails behavior |
| /internal/dev/sampler | POST | APP\_ENV-gated dev/test/local handler | Validated viewer/candidates → sampler core → canonical output |
| /dev/sampler/conjunction; /dev/reader/conjunction; /dev/writer/conjunction | GET | Gated dev conjunction handlers | Conjunction compute/acquisition boundary and governed output |
| /internal/version | GET, HEAD | Module-level registration included in mounted Reader app | Internal identity surface; catalog excludes it from A7 success proof |
| /ops/writer/diagnostic | POST, HEAD, OPTIONS | Module-level diagnostic registration | Writer/diagnostic response behavior; no invocation here |
| /healthz; /readyz | GET | adapter.wsgi factory | Health/readiness handlers specific to that factory; not inferred for Procfile factory |

Reader's current handler enforces its input/path/TZ conditions, constructs bytes through the governed emitter, uses a quoted digest ETag and distinguishes GET, HEAD and conditional 304\. The tested source condition excludes a wildcard-containing If-None-Match from the matching branch; no wider HTTP conformance claim follows. Compat's current GET-body rejection is `invalid_json`; its public response policy is no-store with explicit method handling. The auxiliary text surface is separate from JSON success emission. \[E-012–E-016\]

The catalog intentionally selects a bounded success-proof family; it is not asserted to enumerate every diagnostic or factory-specific route. Registered routes were inspected, not invoked. Exposed deployment, authenticated access, live DB and vendor health remain Unknown. \[E-011, E-028\]

## **6\. Presenter / Emitter**

The inspected byte chain is `engine.presenter.emitter.emit_public` → `engine.serializer.canon.sercanon` → `engine.stable.sercanon.serialize`. The serializer uses compact JSON, Unicode-preserving UTF-8, sorted keys by default and one terminal LF. Wrapper assembly and transport response construction are separate responsibilities. \[E-015\]

Root `presenter/reader_v1/emitter.py` validates category bands, rejects duplicate category IDs, sorts the retained categories, forms an envelope without its idempotence hash, hashes the emitted preimage, then emits the final envelope through the same chain. A namespace split therefore describes wrapper placement; this inspected path does not establish a second serializer. \[E-016\]

`presenter/json_canon_compare.py` is a separate comparison utility: it reads object JSON files, canonicalizes, compares hashes and can write a comparison log. It is not treated as the default public emitter or the canonical evidence publisher. Source existence/inspection does not prove AB↔BA or every domain predicate has passed.

## **7\. CLI Surfaces**

| Command | Actual inputs / dispatch | Output and side effects |
| ----- | ----- | ----- |
| showcompat | Pair/file/stdin/user and source options; optional \--conjunction | Canonical compatibility wrapper to stdout. \--dump-reader and admin directory are separate optional file outputs; resolved inputs may use DB/vendor seams. |
| aux-preview | Category/band/perspective or fixture input | Narrative text; optional canonical admin output; catalog/fixture reads. |
| bg | \--user; \--source auto/db/vendor; \--upsert; \--dry-run; required vendor birth tuple | Resolution result; vendor/upsert boundary may acquire/persist only through its selected branch. auto/db stub is explicitly reported. |
| dev | Viewer and candidates file; dev gating and seed echo | Reads fixture JSON, invokes sampler core, emits ranked result. |

Top-level `--version` is a standalone operation; inappropriate combination and usage errors map to 64, help to 0, typed CLI errors retain their declared code and unexpected failures map to 1\. The stdout writer relies on the canonical emitter for complete byte formatting; its newline guard is not independently a serializer proof. There is no `--crd-id` option in the two inspected package parser/entry files (N-006); CRD recording/publication is a Python API. \[E-017–E-019, E-030–E-032\]

Full tests in `tests/cli/test_cli_canonical_bytes.py` assert compat-wrapper stdout, distinct Reader/admin outputs and explicit closed-rail refusal; `tests/http/test_reader_a7_transport.py` compares HTTP Reader bytes to the CLI Reader sidecar for the same normalized pair. These are source assertions, not executions in this audit. The older compat wrapper differs from the current full-matrix contract; FND-024 preserves that separate required gap. \[E-018, E-033, E-038, E-055\]

## **8\. Vendor Seam & BodyGraph Storage**

The discovered transport family is `engine/bodygraph/vendor_client.py`, with additional provider/provider(s) packages inventoried in §2; top-level `vendor/` is Not found (N-003). HdApiClient obtains configuration by name, builds requests and supports injected transport/retry. The actual default request function checks process rails before urllib I/O. Credential values were not inspected or recorded. \[E-020\]

Vendor-v2 resolution separates preview from explicit upsert, rejects production-like persistence, establishes DB availability before vendor work for a durable write, validates mapped projection and uses a conflict-keyed transaction followed by canonical readback. `resolve_bodygraph`'s auto/db branch remains an explicit no-I/O stub; it must not be cited as the actual DB lookup implementation. CLI showcompat has a separate DB acquisition path. \[E-018, E-021–E-023\]

DBAccess rejects retired bridge configuration by presence before provider selection and uses direct psycopg with `DATABASE_URL`. Adapter's DB module is a facade. Legacy BodyGraph ingest stores the canonical raw vendor payload with idempotent conflict handling and then compares stored emission, unlike the mapped-v2 projection path. The ingestion script calls it twice for its historical evidence family; the refresh worker persists time/rate/breaker state and logs outcomes. The retention entrypoint's call chain was inspected only through its named retention callee. \[E-023, E-024\]

Open-rail vendor, production database access, actual durable writes and retention effects were not executed. Their current availability is Unknown; they are not new readiness prerequisites for this code/documentation CRD.

## **9\. Evidence, Indices, Catalogs**

The complete material-home inventories in §2 include the discovered audit, artifacts, documentation, schema, catalog, fixture, golden and proof families. Git inventory contains 2,417 blobs under `audit/qa/`; directory membership does not establish QA acceptance for the active CRD. \[E-002, E-052\]

The updater owns the Human Index/sentinel, Machine Mirror/checksum, current topology orientation and companions. Parsed current Human/Mirror counts are 593/593 with one Mirror self-record. The direct Human Index SHA-256 is `5ce93ed945fdf290bea173db676e3f58073ed356977f84c913dab5984905f75f` and matches the inspected sentinel. The Mirror self-record's body hash is not casually equated to a hash of the full self-containing file. This inspection did not execute the full evidence gate. \[E-026, E-027\]

Current stored topology orientation has 593 artifacts and status `ok`. The retained EPIC023 orientation report has 252 and status `ok`; those two captures are not interchangeable. Stored favorable outcomes remain statements about their captures, not new audit executions. \[E-027, E-054\]

The docs Endpoint Catalog is a symlink with raw target `../artifacts/audit/ENDPOINTS_CATALOG.json`, Git blob `5d041e91a8c01957975e16c715aa7bdd7d3b06b3`. Its dereferenced JSON has nine endpoint entries and one selected success entry, GET `/reader`. A fetched dereferenced JSON body cannot be hashed as the raw symlink blob. The logical docs path remains the catalog access point, with its physical storage identified separately. Its complete population lacks the canonical Aux/admin-bundle entries (N-009), a separate projection discrepancy recorded in FND-025. \[E-028, E-055\]

The current CRD QA root is Not found in the complete tracked tree (N-001). The generic API can record local CRD families and the updater explicitly admits HDE-CRD-0001 when actual records exist; current code and implementation fixtures are not themselves that live QA family. Generated primaries, manifest, ledgers and proofs retain distinct identities and owners. \[E-030–E-034, E-052\]

## **10\. Tests, QA Harness, CI/Checks**

The complete tree inventories 302 tracked test blobs across the roots in §2. Selected complete tests were read for current claim transitions, CRD identity/paths/full headers/manifest/supersession, real updater admission/rollback, Reader transport/catalog and CLI canonical bytes. Broader suites are represented by their exact accepted implementation receipts; this is not a newly executed complete test run. \[E-002, E-029–E-041\]

The compatibility header helper keeps omitted claims empty and validates before mutating or truncating output. Its default PASS/reduced shape is not a full-v2 verdict generator. The generic harness writes the full fourteen-field primary contract and a flat manifest with actual command provenance, outcomes and self-binding. It records tokenless CRD outcomes without normal Epic map/viability prerequisites while explicit legacy operations remain strict. `run_pytest_check` invokes readiness and tests through the same Python interpreter and distinguishes prerequisite, tooling and behavior failures. \[E-029–E-031, E-033\]

Local recording has file-family validation and rollback. Governed `publish_crd_check_family` first checks the existing evidence graph, then records and publishes under the updater's outer transaction, ending in final verification. Injected-failure tests assert actual bytes and parent metadata restoration after partial writes and final-verifier failure. A rollback failure reports an untrustworthy state and retains its original cause. Neither implementation nor final docs claim concurrent whole-family atomic visibility or process-death recovery for this CRD API. \[E-032, E-034, E-038\]

Ordinary CI checks out the exact candidate head, cancels superseded PR runs, invokes the tracked change classifier, executes its applicable seven lanes and changed tests, and reaches one truthful aggregate conclusion with a clean-tree check. Shared setup and isolated worktree lanes are visible in the workflow. Manual Epic closeout validation is separately dispatched and read-only. The three reusable rails/logging jobs declare live calls forbidden, including the fixture-backed open-conformance job. These workflow declarations are not a green hosted result. \[E-035–E-037\]

### **Accepted implementation validation and actual failed CI**

| Unit | Actual implementation tested state / checks | Delivery and evidence limits |
| ----- | ----- | ----- |
| PR-01 / \#399 | Corrected local d3afbeb4f7cca1b8c33c2d4f7d7686b2ed970f81; 139 ownership \+ 10 compatibility \= 149; seven integrity gates plus environment check | Earlier 569 count belongs to an older candidate. Accepted result v1.1 preserves corrected evidence. Landed 062f7dbe613cd27ea60725e39069c01d85e959f4. |
| PR-02 / \#400 | Local bb198384b7c4060a12444fd0500b19cb4b426a44; 167 generic, 653 QA/ownership, 90 evidence and 52 release tests | Groups overlap and must not be summed. Attestation fixture work is not release/QA approval. Landed 72b1af74f98b0168496a1e2c51492aeff51e9af8. |
| PR-03 / \#401 | V1–V8 documentary checks; no new Python lane required by this docs unit | git diff \--no-index \--check returned 1 with no diagnostic; preserve that value. Landed 71307d9ae51927ec2886c3903e52e687834afc22. DOC-20 did not execute live QA. |

| Unit / stage | Recorded run IDs | Actual observation and limit |
| ----- | ----- | ----- |
| PR-01 initial / corrected | 33962246693; 33963778938 | failure; older baseline 33467618187 also failed. A common cause is not established. |
| PR-02 initial / corrected / post-merge | 33985352746; 33985997280; 33994697736 | failure; early runs failed before steps and the implementation result identifies a billing-lock annotation for that observation. Post-merge steps=\[\]; cause not independently established. |
| PR-03 initial / corrected / post-merge | 34008783686; 34009183236; 34014353421 | failure; recorded steps=\[\]; not converted to PASS or assumed to share an unverified cause. |

These observations are preserved from the complete accepted reviews/results (E-040/E-041). Their actual tested environments identify Python 3.12.13, pytest 8.4.2 and closed dev rails/pins, with isolated test APP\_ENV where recorded. They do not prove the inspector or future QA environment has been provisioned. The PO's Plan-wide direction governs the unavailability disposition separately; it does not waive code/security review, local validation or future QA.

## **11\. Flows & Call Chains**

| Comparison / discovered family | Classification | Observed source-to-output hops | Evidence |
| ----- | ----- | ----- | ----- |
| Reader HTTP | Present | adapter.factory/create\_app or wsgi/create\_app → mounted adapter.http\_reader Reader handler → input/path/TZ validation → engine.runtime.public Reader construction → presenter.reader\_v1.emit\_reader\_v1 → engine.presenter.emit\_public → stable serializer → HTTP bytes/ETag/HEAD/304 | E-005, E-006, E-009, E-011, E-012, E-015, E-016 |
| Compatibility HTTP | Present | adapter factory → engine.http.compat\_handler blueprint → input-mode validation → runtime/compat computation → governed public emitter → response/refusal/no-store handling | E-006, E-009, E-013, E-015 |
| showcompat CLI | Present | hdctl / engine.cli.**main** → cli parser → source/input resolution → compat/conjunction computation → public emitter → stdout; optional Reader envelope → \--dump-reader; optional admin canonical sidecars | E-003, E-017, E-018 |
| Sampler CLI/dev HTTP | Present | CLI dev or /internal/dev/sampler → validation/gating → sampler.core.sample\_and\_rank → pool eligibility → comparator ranking → emitted result | E-008, E-014, E-019 |
| Aux preview/HTTP | Present | CLI aux-preview or aux route → public aux/narrative entry → text result → CLI text/admin output or HTTP success/suppression response. Deeper narrative catalog semantics were not re-audited. | E-014, E-019 |
| Vendor-v2 resolution and mapped cache | Closest evidenced equivalent to generic vendor family | bg/vendor caller → resolver.\_resolve\_vendor\_v2\_chart → rail/production/upsert gates → DBAccess selection when writing → HdApiClient → v2\_adapter projection → mapped\_cache transaction/readback → result. auto/db resolver branch is explicitly stubbed and is not this path. | E-019–E-023 |
| Legacy vendor ingestion | Present | scripts/ingest/run\_vendor\_ingest.main → gather\_inputs\_from\_env → ingest\_vendor\_bodygraph → rails → DBAccess for writes → HdApiClient.fetch → canonical payload → SQL transaction → stored payload readback → parity/logs; script repeats twice and emits evidence summaries | E-020, E-023, E-024 |
| Refresh/retention | Present, bounded caller coverage | run\_refresh → persisted rate/breaker/freshness state → permitted ingest path → keys-only logs/metrics/state. run\_retention\_job → DBAccess → run\_bodygraph\_retention → retention log; callee internals remain outside inspected coverage. | E-024 |
| Evidence update/orientation | Present | updater entry → complete known artifact selection and validation → Human/Mirror/proof/orientation staging → convergence → publication; \--check detects stale/missing bytes without repair; orientation compatibility writer delegates to updater | E-026, E-027, E-032 |
| CRD local recording | Present | HarnessConfig(crd\_id) → CheckResult / actual command result → full-v2 render → primary.log \+ flat manifest → local validation/supersession/handled-error rollback; historical records are retained | E-030, E-031, E-033 |
| CRD governed publication | Present | publish\_crd\_check\_family → exact admitted CRD0001 \+ prior graph check → outer \_WriteTransaction → harness local family → updater convergence → family/final verifier → success, or handled-exception rollback across captured files/parents | E-032, E-034 |
| Compatibility helper claims | Present | create\_header/update\_header\_status → validate explicit claims/status → reduced header → validate/serialize before write; omitted new claims remain empty and earlier claims are cleared | E-029, E-033 |

All material comparison flow families are mapped. Externally running services, complete retention internals and narrative-domain semantics remain explicitly bounded Unknown/uninspected facts; no endpoint or vendor call was made to fill them speculatively.

## **12\. Drift and Reality vs Expectations**

### **Independently verifiable findings**

The following IDs are authored for this audit. “Alignment” describes the evidenced comparison, not a Canon decision or readiness gate. Separate current-source and historical observations are retained where their dispositions differ. Normative interpretation belongs to the separate Change Audit Triage.

| Finding | Subject / classification | Comparison source | Current observation | Evidence | Actual impact / limit |
| ----- | ----- | ----- | ----- | ----- | ----- |
| FND-001 | Presenter component mapping — Present; changed/equivalent | PF23 F-001, 2026-08-21 | Engine emitter and root Reader envelope builder remain split by namespace, while the inspected chain delegates to one serializer. | E-015, E-016, E-043 | Historical path split persists; role/delegation mapping is clarified. Independent competing emission is not established by these paths. |
| FND-002 | HTTP handler mapping — Present; changed/equivalent | PF23 F-002, 2026-08-21 | Compat blueprint remains under engine/http and is mounted through adapter factories. | E-006, E-011, E-013, E-043 | Historical placement persists; adapter-owned mounting is the actual surface boundary. |
| FND-003 | CLI family — Present; persistent aligned observation | PF23 F-003, 2026-08-21 | One hdctl registration dispatches the four current engine.cli subcommands. | E-003, E-017–E-019 | A packaged CLI family is present; stdout and sidecar output identities remain distinct. |
| FND-004 | Evidence family distribution — Present; persistent partial physical mapping | PF23 F-004, 2026-08-21 | Human Index and Machine Mirror still bind artifacts across several roots through the canonical updater. | E-026, E-027 | Multiple physical homes remain visible; they are not competing acceptance authorities. |
| FND-005 | Compute and sanctioned I/O boundaries — Present; persistent bounded observation | PF23 F-005, 2026-08-21 | Core/sampler inspected computation is data-derived and ordered; BodyGraph/CLI boundary units explicitly acquire, persist and write evidence. | E-007, E-008, E-020–E-025 | The historical statement is valid for its named bounded compute/seam units. It does not classify every engine module as pure; loader is separately FND-022. |
| FND-006 | Vendor home mapping — Closest evidenced equivalent; persistent | PF23 F-006, 2026-08-21 | Top-level vendor/ is Not found (N-003); current transport is engine/bodygraph/vendor\_client.py; engine/provider and engine/providers are separate discovered packages. | E-002, E-020, E-021 | Equivalent transport is addressable; live service reachability is Unknown because it was not probed. |
| FND-007 | DB family mapping — Closest evidenced equivalent; persistent | PF23 F-007, 2026-08-21 | Direct DBAccess lives in engine/db with adapter facade and BodyGraph SQL callers. | E-022–E-024 | Facade does not establish a second transport implementation. Current configured production DB state is Unknown. |
| FND-008 | Expected path case — Present; persistent aligned observation | PF23 F-008, 2026-08-21 | engine, adapter, presenter, docs, artifacts, audit, tools, ci, tests and scripts are exact lowercase root names. | E-002 | Requested family paths resolve without case translation; this does not assert all paths in the repo are lowercase. |
| FND-009 | Producer/evidence root count — Present; persistent count-only comparison | PF23 F-009, 2026-08-21 | The same seven compared roots remain: docs, artifacts, audit, catalog, proofs, tools, scripts. | E-002, E-026 | Impact from the count alone is not established. Counts of files changed since the historical snapshot are not all attributed to this CRD. |
| FND-010 | Endpoint Catalog physical identity — Present; changed/equivalent physical-home description | PF23 F-010, 2026-08-21 | docs/ENDPOINTS\_CATALOG.json is a tracked symlink to the artifact catalog, not an independently stored JSON mirror. | E-028 | Logical designated path and physical target must be distinguished for byte inspection and ownership. |
| FND-011 | Configured server factory — Present; newly explicit comparison correction | PF23 Packaging/Entrypoints, 2026-08-21 | Procfile selects adapter.factory; adapter.wsgi.create\_app also exists and is used by adapter/app.py. | E-005, E-006 | Calling wsgi the configured primary loses a material guard/mount distinction. Actual deployed command is Unknown. |
| FND-012 | Root artifact types — Present; newly explicit comparison correction | PF23 top-level descriptions, 2026-08-21 | assert and import are zero-byte tracked files at the current snapshot. | E-002 | Treating their names as directories is inaccurate for current inventory; execution effect is not established. |
| FND-013 | Reader duplicate categories — Present; newly explicit comparison correction | PF23 Presenter/Emitter description, 2026-08-21 | Duplicate category IDs raise ValueError; sorting follows validation. | E-016 | A description of silent deduplication would misstate the observed failure behavior. |
| FND-014 | Truthful compatibility claims helper — Present; new implementation / earlier audited defect resolved | Approved Plan PR-01 and accepted corrected result | Current helper does not infer or retain omitted claims for a new outcome and validates rejection before mutation/publication. | E-029, E-033, E-040 | The repaired claim behavior is present; reduced helper header remains a documented compatibility boundary, not a full-v2 writer. |
| FND-015 | Ordinary CRD recording and governed publication — Present; new implementation | Approved Plan PR-02 and accepted result | Generic local CRD records, full v2 primaries, flat manifest, strict legacy separation and updater-owned HDE-CRD-0001 publication are wired, with handled-exception recovery. | E-030–E-034 | Local ID acceptance is wider than governed admission. Crash-atomic/concurrent whole-family visibility is outside the documented guarantee; future QA must respect it. |
| FND-016 | Final operative documentation — Present; new implementation | Approved Plan PR-03, accepted review and DOC-20 completion | Four changed repository homes explain native evidence, routes, source policy, CI scope, current helper/harness and evidence ownership; the complete accepted Markdown inventory is retained. | E-038–E-040, E-050 | Final docs describe delivered capability; implementation checks and DOC completion do not supply a live QA verdict. |
| FND-017 | Inherited HTTP documentation predicates — Present; persistent qualified discrepancy | PR-03 accepted review and documentation-completion caveat | ADAPTER\_009 retains body\_not\_allowed, canonical-header-capture and CLI-stdout/Reader wording; current compat and dedicated transport evidence use invalid\_json, plain-text captures and \--dump-reader parity. | E-012, E-013, E-018, E-038 | These predicates need source-specific interpretation. The accepted docs scope preserved them as inherited adjacent work rather than claiming resolution. |
| FND-018 | Hosted CI outcomes — Present; persistent failed evidence with scoped disposition | Accepted PR lineage and Plan-wide PO direction | The recorded hosted runs failed; the existing override treats known CI unavailability as non-blocking across Plan v1.0. | E-040, E-041 | CI failure is retained, not relabeled PASS. The cause of every failed run is not established; local tests and reviews retain their own scope. |
| FND-019 | Permanent PF19 current-source wording — Present; persistent separately owned alignment work | PF19 §10.8 and supplied PF10 §2.8 / approved Plan correction | The current permanent Guide retains scope-equivalence wording while supplied PO direction distinguishes substantive changes from a SHA change alone. | E-045, E-050 | Approved runtime direction is preserved; permanent text is not claimed updated. Manual alignment is separately owned and non-gating here. |
| FND-020 | Deferred prompt provenance installation — Not found; persistent excluded work | Approved Plan exclusion; supplied PF10 §2.9 | docs/changes/GCFPE\_PROMPT\_PROVENANCE.md is Not found at current HEAD (N-002); PR398 was closed unmerged in supplied lineage. | E-052, E-053 | Prompt-use metadata must remain in permitted artifacts until an authorized installation/writer exists; deferred installation is not CRD delivery scope. |
| FND-021 | Public compatibility versus canonical Engine Core — Present; persistent source-established discrepancy | PF02 §2.1 Current repository discrepancy | Current direct public runtime/HTTP compat/CLI paths select compat computation; direct compute\_core references are Not found in those three files (N-007). | E-007, E-009, E-013, E-018, E-043 | Presence of compute\_core does not establish public-path migration or complete domain mathematics. This CRD did not implement that migration. |
| FND-022 | Chart loader side effects — Present; persistent source-established discrepancy | PF02 §1.1 Non-BodyGraph chart loader classification | engine/charts/loader.py still performs environment reads, timing, provider resolution and file logging. | E-025, E-043 | The whole engine package cannot be described as effect-free from the two compute modules. Architecture already identifies this separate discrepancy. |
| FND-023 | Actual CRD QA evidence state — Not found at inspected tracked root; expected future work | Plan §11 readiness and prior readiness v1.0 | audit/qa/hde-crd-0001 is Not found in the complete tracked tree (N-001). Accepted implementation fixtures and Library readiness are different records. | E-030–E-034, E-040, E-052 | Current source inspection does not supply an executed CRD live QA result. Actual QA remains the later authorized workflow. |
| FND-024 | Current compatibility output versus full-matrix contract — Present; source-established required gap | PF05 §4.1.3 CLI full-matrix diagnostic and §4.1.6 Implementation status | Current showcompat emits the a/b/viewer\_prefs/compat wrapper; its complete-result contract specifies magic10\_compat\_result.v1 without that wrapper. Current compat computation and source tests establish the observed older path. | E-009, E-018, E-055 | The current behavior must not be described as delivered full-matrix conformance. The approved CRD excludes product/math/CLI contract implementation. |
| FND-025 | Endpoint Catalog projection completeness — Present; source-established partial projection | PF05 §5.6 Endpoint Catalog / Implementation and acceptance state | The complete nine-entry catalog contains neither the canonical Aux nor admin-bundle records (N-009), while those are required projection entries in the current transport owner. | E-028, E-055; N-009 | A coherent catalog artifact is not proof of complete current catalog population. The approved CRD does not implement these separate product/catalog requirements. |

### **Complete dated historical finding comparison**

| Prior PF23 finding | Current finding | Disposition at 2026-09-06 | Evidence |
| ----- | ----- | ----- | ----- |
| F-001 | FND-001 | Changed/equivalent: physical split persists; shared-emitter delegation and current role-based classification clarify it. | E-015, E-016, E-043 |
| F-002 | FND-002 | Changed/equivalent: engine blueprint remains; adapter mounting explicitly owns its surface. | E-006, E-013, E-043 |
| F-003 | FND-003 | Persistent: registered CLI and typed dispatch still present. | E-003, E-017 |
| F-004 | FND-004 | Persistent: distributed evidence remains tied through two governed ledgers. | E-026, E-027 |
| F-005 | FND-005; bounded by FND-022 | Persistent for inspected core/sampler and sanctioned BodyGraph seams; does not generalize to loader side effects. | E-007, E-008, E-024, E-025 |
| F-006 | FND-006 | Persistent closest equivalent: BodyGraph-specific transport, not top-level vendor. | E-020, E-021; N-003 |
| F-007 | FND-007 | Persistent closest equivalent: shared engine DB access with adapter facade. | E-022, E-023 |
| F-008 | FND-008 | Persistent: exact requested root spellings resolve. | E-002 |
| F-009 | FND-009 | Persistent count-only fact; impact remains not established. | E-002 |
| F-010 | FND-010 | Changed/equivalent: docs catalog is a symlink to physical artifact storage, not independently stored duplicate JSON. | E-028 |

PF23's other historical statements about configured factory, assert/import directory types and Reader deduplication receive explicit current corrections in FND-011–FND-013. These are new comparison findings, not claims that this CRD introduced those facts. FND-014 records resolution of the earlier approved implementation-audit helper defect; FND-015/016 record newly delivered CRD and docs capability. FND-017–FND-025 preserve qualified adjacent discrepancies, actual CI, pending permanent/provenance work and future QA state.

The prior audit's local clean-worktree, Linux/Python/Node and service context are unverifiable for this remote snapshot and are not copied as present state. Historical counts (docs 151, artifacts 1,022, audit 3,015 and audit/qa 2,383) differ from current counts (155, 1,022, 3,049 and 2,417 respectively); the count delta is observed, but attribution of every added file to this CRD is not established. \[E-001, E-002, E-042\]

## **13\. Negative-Claim Proof Appendix**

Each record below is a bounded absence proof only. Python reads/parses cached text/tree; it does not import repository modules or run tests. Case sensitivity is explicit. Local work inventory/search limits do not assert global absence from a remote account.

| Proof | Exact pattern | Method/tool | Case | Complete bounded scope | Result |
| ----- | ----- | ----- | ----- | ----- | ----- |
| N-001 | ^audit/qa/hde-crd-0001(?:/|$) | Python re.search over every path in complete GitHub recursive tree | sensitive | complete recursive tracked tree: 7006 entries, truncated | 0 hits |
| N-002 | ^docs/changes/GCFPE\_PROMPT\_PROVENANCE.md$ | Python re.search over every path in complete GitHub recursive tree | sensitive | complete recursive tracked tree: 7006 entries, truncated | 0 hits |
| N-003 | ^vendor(?:/|$) | Python re.search over every path in complete GitHub recursive tree | sensitive | complete recursive tracked tree: 7006 entries, truncated | 0 hits |
| N-005 | ^(?|server|adapters)(?:/|$) | Python re.search over every path in complete GitHub recursive tree | sensitive | complete recursive tracked tree: 7006 entries, truncated | 0 hits |
| N-006 | \--crd-id | Python re.search over all lines in each complete file | sensitive | engine/cli/main.py, engine/cli/**main**.py | 0 hits |
| N-007 | \\bcompute\_core\\b | Python re.search over all lines in each complete file | sensitive | engine/runtime/public.py, engine/http/compat\_handler.py, engine/cli/main.py | 0 hits |

N-001 supports only the tracked CRD evidence-root absence; Library reports and implementation fixture outputs are different surfaces. N-002 supports only the installed procedure path. N-003 identifies a renamed/equivalent vendor family. N-005 establishes the literal denied root paths are Not found; it does not prove all alternative-import behavior. N-006 concerns only the two named CLI files. N-007 establishes direct token absence in three current wiring files, not a full transitive call-graph proof.

**N-008 — Cancelled-attempt report recovery.** Method: complete recursive file inventory of `qa15-work` plus bounded output-name discovery; case-sensitive local suffix/name scan for `reality-audit`, `change-audit-triage` and QA-15 report Markdown, distinguished from `sources/PF23-Canon-Reality-Audits-v1.1.9.md` and source readiness. Result: zero authored audit/triage report files in the working inventory. Library filename search for the HDE-CRD-0001 reality-audit/change-audit-triage names returned no matching complete report; scope is that query, not a claim about every differently named Library file. Existing actual source caches are preserved.

This audit ends with factual observations and their scope. Canon/Plan disposition is in HDE-CRD-0001-change-audit-triage-v1.0.md; the independent integrated readiness decision is in HDE-CRD-0001-qa-readiness-v1.1.md. It supplies no QA PASS, new PR acceptance, PF publication or closure.

**N-009 — Catalog record population.** Exact case-sensitive field-equality query: endpoint.path in {`/aux/narrative`, `/internal/admin/bundle/v1`}. Method: Python JSON parsing of the complete `artifacts/audit/ENDPOINTS_CATALOG.json` target (nine entries), reached by the tracked docs symlink. Result: 0 matching endpoint records. This proves catalog population only, not repository-wide route absence.

