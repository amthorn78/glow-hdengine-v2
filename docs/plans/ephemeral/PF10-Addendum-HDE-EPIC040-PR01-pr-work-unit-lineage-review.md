## 2.6 HDE-EPIC040-PR01 — Accept Source-Proven Catalog and Exact Contract Data

Timestamp: 091226 11:01 (UTC)  
Details: Record the bounded PR-01 lineage review and acceptance for HDE-EPIC040, including exact source authority, landed attribution, contract and evidence findings, CI and security qualifications, downstream boundaries, and the direct handoff to PR-10.

### **Approval and source record**

**Approval type:** PR work-unit lineage review.  
**Decision:** **ACCEPT**.  
**Source:** `HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md`  
**Artifact type:** `PR_WORK_UNIT_LINEAGE_REVIEW`  
**Logical ID:** `HDE-EPIC040-PR01-PR-WORK-UNIT-LINEAGE-REVIEW`  
**Review capture:** `2026-09-12T10:49:37Z`  
**Reviewer / continuing owner:** Product Owner-assigned retained whole-change HDE-EPIC040 Implementation Architect.  
**Execution posture:** `MANUAL_PROMPT_EXECUTION`.

This v1.1 is the complete successor to `HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.0`, library ID `libfile_1d1ae2082c148191b747726713b0b6a9`, SHA-256 `a5fd61806e2b4afe4c6a7a86bec658fcb57e9b35c6815c0484efcdc9ad39f7bd`. The predecessor truthfully remained **PENDING** because its source-and-proof comparison was incomplete. It is preserved unchanged as historical review evidence.

The present decision is **ACCEPT** for the bounded work unit only: HDE-EPIC040-PR01, “Source-proven catalog and exact contract data.” The reviewed implementation is attributable to merged PR #403 and has no observed later-main divergence at this review capture. Acceptance is not a claim that PR02–PR07, OPS01, independent QA, release activation, production fallback, or Epic closure occurred.

The current PR-40 contract used for onward routing is `PR-40 — Review PR Work-Unit Lineage — 091126.1`, AI Prompts / HDE IA, Notion page `3d84590a-05eb-816b-85e5-ed1458a6008d`. It requires direct native handoff rather than an intermediary assessment. The historical invoked 090926.1 PR-40 prompt remains part of the input lineage and is not rewritten.

### **Retained decisions and requirements**

| Input | State and verified SHA-256 |
| --- | --- |
| PR01 Instruction v2.0, `libfile_68be4bc4c4b88191aab5f5c7062c774b` | INSTRUCTION_READY; `dc556774202196b7d94f09870ff5b0d2c3fc47195e997f071ff4897ffb39e9fa` |
| Detailed Plan v1.1, `libfile_7960d01d117881919c0004545ae3a4d7` | Original AWAITING_PO_PROCEED body preserved; `a77d453aa2a8b50b8e559cb8f6e5e2098f667760802366646f539a772769916e` |
| Implementation Result v1.0, `libfile_dbc2c204e99c8191a4179b022697bb00` | Historical MERGE_PENDING checkpoint preserved; `5dc65f1a775f34fb92d9afa79b3d788258b2f6daedaf1df52657052f6f7b8551` |
| Whole-change Plan v2.1, `libfile_11c992cda3f0819199827e86584e41f1` | Approved parent Plan; `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| Approving Plan Review v2.1, `libfile_b85b81651a508191abdfd8f81803caf8` | Isis-50 APPROVE, 2026-09-09T13:36:43Z; `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |

All five bodies were materialized and matched their supplied hashes. The actual Product Owner Proceed for the exact Detailed Plan/Instruction remains the PR-30 authority. This PR-40 review neither reissues it nor authorizes a different work unit.

The approved six-entry Canon-conflict register is retained from the exact Instruction, Detailed Plan, whole-change Plan and approving Review. C040-01–04, C040-05 alternative A, and C040-06 alternative A retain their stated approvals and owners. Published canonical Build Notes Addendum 2.5 body/index verification and the non-gating stale-wording/drainage qualifications are preserved. No new Canon decision is made here.

##### 4.1 Catalog, schemas, mechanics and result contracts

Direct comparison of the landed `catalog/channels_v1.json` against the complete approved table found:

- exactly 36 Channel rows in the approved ASCII ID order;
- no mismatch in ID, ascending integer Gate pair, Gate-derived Center set, `circuit_primary`, or `substream` for any row;
- no change to any retained `primary_domain`, `domains`, or `flags` metadata value versus the original base; and
- all Center sets agree with the current gate catalog.

The landed Channel schema is Draft 2020-12, top-level and row-closed, requires the intended fields, and retains the seven non-null substreams including `ego`. The three new schemas are closed Draft 2020-12 schemas. The mechanics schema has exactly ten top-level properties; both pure and internal result schemas have exactly six required top-level properties, with the internal contract retaining its additional narrative-key conditions.

The landed mechanics configuration has exactly the approved ten keys, `config_id` `m10-channel-state-v1.0.0`, 3 profiles and 15 exact responses, 20 ordered signals, 90 memberships, 10 ordered category weights `[1,1]`, all 36 Channels represented, response scale `10000`, signal scale `2`, and the approved rounding values. Its four source references have the required paths and lowercase 64-hex digests. The dependent thresholds preserve clamp `[0,100]`, edges `[24,49,74,100]`, `ROUND_HALF_UP`, and version `1`.

This is local data/schema contract delivery only. It does not claim PR03/PR04 calculation, augmentation, Reader transport, or runtime production of those result objects.

##### 4.2 Loader, selected-root writers, generated outputs and recovery

Direct review of the changed implementation and its dedicated test homes confirms the intended boundaries:

| Area | Reviewed delivery and adverse coverage |
| --- | --- |
| F07 / loader | Duplicate-aware raw JSON handling; canonical-byte/schema/relational checks; strict numeric/type/domain checks; source capture/recheck; exact channel/config relations; explicit ledger-only aliases. Tests cover duplicate/noncanonical input, unsafe roots, schema references, source races, invalid Gate forms, unknown/duplicate Gate IDs, and forbidden authoritative aliases. |
| F08–F12 / selected-root projections | Registry report, config-artifact and FE/BE bundle paths derive from selected captured sources; paired bundles validate before publication and checks are read-only. Tests cover two-root isolation, stale/missing primary refusal, consumer-schema validation, paired rollback, destination races, symlink refusal, and post-replacement conflict preservation. |
| F13–F14 / Gate integration | The canonical gate retains `EXPECTED_SET_RULES`; the Channel-Gate path is subject to numeric endpoint/order validation, while unrelated set behavior remains separately covered. Arrays and canonical-gate tests include reversed/noncanonical, schema-pin, identity-substitution, count-drift, raw duplicate-key and type-coercion refusals. |
| F15 / evidence closure | The existing updater remains the sole Index/Mirror/proof writer. The scoped config-family transaction rejects out-of-closure changes and preserves preimages, original errors and conflicting external changes; check mode is non-writing. Two governed catalog logs and the required primary/proof/index/mirror/orientation companions are present in the landed collection. |
| F29 / manifest | `catalog/manifest.json` remains version `1.0.0`, time `2025-12-26T00:00:00Z`, and 15-member roster. Its changed listed-member hashes/sizes are the expected source consequence; no PR06 promotion is represented. Cutter tests cover fixed point, input/roster/raw/symlink refusal and private-publisher check behavior. |

The recovery claim is bounded. The reviewed sources and tests provide caught-failure restoration, source/destination race refusal, no-write check paths, and preservation of conflicting external changes. They do **not** promise crash atomicity, multi-file atomic visibility, or cross-process locking.

##### 4.3 Generated/evidence identity

The landed 67-path set contains the required report, two catalog logs, FE/BE bundles, arrays report, canonical-gate outputs, JSON-gate outputs, updater Index/Mirror/checksum outputs, orientation output, and associated path proofs. Directly fetched proof records bind the expected physical paths, sizes and SHA-256 values; the complete exact per-file Git blob/SHA/byte register remains in Implementation Result v1.0. The evidence index contains 606 rows and retains the two bounded new catalog records rather than a new generic evidence family.

This review relies on actual current-head source retrieval, path/proof/index content, dedicated tests, and the exact Result’s saved attribution. It does not relabel the Result’s engineering-run evidence as a fresh reviewer-run generator or test execution.

### **Epic, task, and status effects**

| Point | Commit / tree | Verified fact |
| --- | --- | --- |
| Original base | `9065e6f0c01ad82a65c78687cd6c55e26ca33a1f` / `e07c4e4297c75fe83e0f286aa1cee46ffca6c62e` | Original PR base |
| Initial branch commit | `924ae36a0bfe320f81fc9b6e4fd3891436096f27` / `543ea921385410c6eda57404b8038b2d90f896e7` | Initial tested/published candidate |
| Corrected reviewed/tested head | `75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950` / `529306a74268f2a46765bf40defdae49026d103e` | Token-reader repair included; final CI and current-head reviews apply here |
| Landed squash commit | `3828d4b3454259841a3e48d13039dd1475754f2f` / `529306a74268f2a46765bf40defdae49026d103e` | Sole parent is original base; merged by `amthorn78` at 2026-09-09T22:01:54Z |
| Observed main | `3828d4b3454259841a3e48d13039dd1475754f2f` | Equals landed commit; no later main divergence observed |

PR #403 has two ordered branch commits and 67 changed paths. The landed tree equals the corrected branch-head tree. This is squash-merge topology, not evidence that tests ran on `3828d4b...`; final CI ran on `75ddaf2...`.

The complete PR changed-path collection contains every F01–F29 planned source/test path and the required generated/companion outputs. The additional bounded paths are the governed outputs and their proof companions, `scripts/cut_release_manifest.py` plus its tests, and the two-file token-reader correction (`tools/qa/token_roster_validate.py`, `tests/qa/test_qa_tool_ownership.py`). No unselected PR or intermediate merge dependency was identified.

The substantive status is **PR01 ACCEPTED**. No unresolved attributable defect, required-evidence gap, or later-main divergence was identified for this bounded work unit.

### **Required canon drainage**

No new Canon decision or completed Canon update is established by this review. The source retains the approved six-entry Canon-conflict register: C040-01–04, C040-05 alternative A, and C040-06 alternative A, with their stated approvals and owners. The published canonical Build Notes addendum 2.5 body/index verification and non-gating stale-wording and drainage qualifications remain prior context. Any later permanent drainage remains subject to its named owner and separate authority; this review performs no Canon movement.

### **Deferred obligations and unresolved work**

**Next owner:** the same retained whole-change IA.  
**Next substantive destination:** `PR-10 — Create PR Work-Unit Instructions — 091126.1`, AI Prompts / HDE IA, Notion page `3d84590a-05eb-8100-bc35-d6d5414dbdbf`.

Native package for that destination:

- `IMPLEMENTATION_PLAN_ID`: `libfile_11c992cda3f0819199827e86584e41f1`, HDE-EPIC040 Implementation Plan v2.1, exact approved Plan;
- `PLAN_REVIEW_ID`: `libfile_b85b81651a508191abdfd8f81803caf8`, approving Review v2.1;
- completed predecessor unit and accepted review: HDE-EPIC040-PR01 / this PR_WORK_UNIT_LINEAGE_REVIEW v1.1;
- planned dependency-ready unit only: `WORK_UNIT_ID: HDE-EPIC040-PR02`.

PR-10 must read its current complete contract and create exactly one PR02 instruction under its own authority. This ACCEPT does not fabricate a future Proceed, engineer assignment, implementation, merge, QA/Ops/release action, or any other role execution.

The following remain planned or outside this bounded work unit: PR02 immutable admission/freezing/runtime Gate normalization; PR03 classifier, four-argument kernel, and intrinsic identity; PR04 application/Reader behavior; PR05 goldens, comparator, and readiness; PR06 release promotion; PR07 DOC-10; OPS01; independent QA; active release or production fallback; Canon drainage; and Epic closure. The eight goldens and 31-member promoted roster remain later-unit scope.

### **Scope boundaries and nonclaims**

PR403 delivers the attributable PR01 source-contract, local-validation, writer/recovery, generated-companion, test, documentation-in-code and CI-owner obligations. It preserves the approved no-new-math, no-tuning, no-public-field, no-caller-UUID, no-fabricated-Gate, no-persistent-identity, no-Reader-UUID5 conversion, no-SEPA006 migration and no-inherited-CRD-exception boundaries.

The following are expressly not decided or completed by this review: PR02 immutable admission/freezing/runtime Gate normalization; PR03 classifier/four-argument kernel/intrinsic identity; PR04 application/Reader behavior; PR05 goldens/comparator/readiness; PR06 release promotion; PR07 DOC-10; OPS01; independent QA; active release or production fallback; Canon drainage; and Epic closure.

No unresolved attributable defect, required-evidence gap, or later-main divergence was identified for this bounded work unit. **PR01 is ACCEPTED.**

### **Evidence and traceability**

##### 5.1 Requirement/proof completion

| Proof group | Completion basis |
| --- | --- |
| T01–T03 | Exact 36-row direct comparison, unchanged 108 metadata values, closed Channel schema, loader/catalog/alias tests, Gate-order/arrays/canonical-gate adverse cases |
| T04–T07 | Exact mechanics structure/defaults/profiles/signals/memberships/category weights/sources, closed schemas, result-contract and strict-domain tests |
| T08–T10 | Selected-root report/config/bundle source review; check-mode, paired publication, race/recovery, generated-output and updater-convergence tests; governed companions and index/proof presence |
| T11 | Current 15-member manifest/metadata and cutter validation tests; no promotion or release activation claim |
| T12 | Classifier source maps actual PR01 owners including the added config/report/test support paths; workflow integration tests cover missing/symlinked/unmapped paths, full validation and all selected lanes |

The Detailed Plan’s K040-REQ-001 through K040-REQ-013 and PR01-applicable AC040-01/02/03/08/09 are satisfied through these F/T groups. AC040-04 through AC040-07 retain the planned downstream owners where the Plan assigns them. The eight goldens and 31-member promoted roster remain planned later-unit material, not PR01 delivery claims.

##### 5.2 Actual CI

The initial CI run `34391523823` at initial head `924ae36...` is preserved as historical failure: one token-alignment test failed, later lanes were skipped, and the final guard failed.

The corrected final CI run `34393325625`, job `102606798665`, ran on exact head `75ddaf2...` and completed successfully. All seven selected lanes passed: product, compat, DB, rails, evidence, QA subsystem isolation, and release. Its log records 1,544 affected owner tests passed, the stated per-lane outcomes, and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. The compatibility 3 skipped / 2 xfailed tests are retained as test outcomes, not skipped CI lanes; counts overlap and are not summed. This is CI evidence only, not independent QA, OPS01, release activation, or deployment.

##### 5.3 Reviews and the fsync/EIO finding

Current-head code and security outcomes were reviewed. The accessible security outcome comment `5607726236` identifies `75ddaf2...` and reports no issues; its private report was not opened. The formal COMMENTED review `5158828852` remains material evidence: it reports P1 EIO/fsync failures in the reviewer overlay, including an independent temporary-file probe.

The finding’s two dispositions (`5607519817`, `5607603260`) are accepted as correctly scoped, not as an erased failure:

- the relevant `tools/evidence/update_evidence_index.py` publication path already flushed and called `os.fsync` before replacement on the original base, so PR403 did not introduce that operation;
- the corrected source retains the error-propagating write/flush/fsync path and adds transaction identity/recovery handling rather than suppressing EIO;
- the Detailed Plan explicitly required this integrity operation; and
- targeted recovery tests and successful exact-head CI provide source/test support in a different environment.

Accordingly, the review-environment EIO observation is **not accepted as a PR403 code defect** and is **not recast as a passing test, portability promise, or waiver**. No EIO suppression, workaround, or finding-dismissal API is observed.

- PR: https://github.com/amthorn78/glow-hdengine-v2/pull/403
- Final CI: https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34393325625
- Formal finding: https://github.com/amthorn78/glow-hdengine-v2/pull/403#pullrequestreview-5158828852
- First disposition: https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607519817
- Security outcome: https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607726236
- Exact full per-file implementation and engineering evidence: HDE-EPIC040-PR01 PR Implementation Result v1.0, `libfile_dbc2c204e99c8191a4179b022697bb00`.

The review relies on current-head source retrieval, path/proof/index content, dedicated tests, and the Result’s saved attribution. It does not relabel engineering-run evidence as a fresh reviewer-run generator or test execution. No PF09 row-closure record is included because the source contains no PF09 mapping or closure determination.
