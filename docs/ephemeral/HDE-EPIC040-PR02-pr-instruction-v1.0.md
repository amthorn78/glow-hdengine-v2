# HDE-EPIC040-PR02 — PR Work-Unit Instruction v1.0

## 1. Identity, state and authority boundary

| Field | Value |
| --- | --- |
| Artifact type / logical identity | PR_INSTRUCTION / HDE-EPIC040-PR02-PR-INSTRUCTION |
| Version / state | 1.0 / INSTRUCTION_READY |
| Change | EPIC / HDE-EPIC040 — Separation Pass 3 |
| WORK_UNIT_ID / name | HDE-EPIC040-PR02 / Strict immutable input and admission boundary |
| Producer | Product Owner-assigned retained whole-change HDE-EPIC040 Implementation Agent; sole instruction author and native-output writer |
| EXECUTION_POSTURE | MANUAL_PROMPT_EXECUTION |
| session_disposition | RETAIN_EXISTING |
| role_session_ref | Product Owner-assigned retained whole-change HDE-EPIC040 Implementation Agent |
| invocation_binding | EPIC / HDE-EPIC040 / HDE-EPIC040-PR02 / PR-10 instruction creation after accepted PR01 lineage |
| context_conflict | NONE |
| SPECIFICATION_REF | `libfile_12bab860949c8191881510875f051460`; HDE-EPIC040-SPECIFICATION v1.1; SPECIFICATION_APPROVED; Thoth-17 APPROVE, 2026-09-08T13:23:24Z |
| IMPLEMENTATION_AUDIT_REF | `libfile_823ee8e9ecb0819185181ec7695265fb`; HDE-EPIC040-IMPLEMENTATION-AUDIT v2.0; AUDIT_COMPLETE |
| IMPLEMENTATION_PLAN_REF | `libfile_11c992cda3f0819199827e86584e41f1`; HDE-EPIC040-IMPLEMENTATION-PLAN v2.1; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| PLAN_REVIEW_REF | `libfile_b85b81651a508191abdfd8f81803caf8`; HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW v2.1; Isis-50 APPROVE, 2026-09-09T13:36:43Z; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Accepted dependency | HDE-EPIC040-PR01 PR Work-Unit Lineage Review v1.1, `libfile_47bf2e063d208191bf57f93c71f96821`; ACCEPT; SHA-256 `f103798f7c8344e8cec763f0496d82a9ca81f82ea9cb8e6ac4cf0cd4c59e3273` |
| Storage class / home | EPHEMERAL_LIBRARY / `/Glow HDE 3.0` |

This is one complete instruction for exactly one planned PR unit. It authorizes only PR-20 detailed planning when handed off by the Product Owner/operator. It does not authorize implementation, Product Owner Proceed, repository mutation, PR publication, merge, QA, Ops, release activation, PF/Canon publication, scope change or Epic closure.

The effective whole-change authority is the exact unchanged Plan v2.1 plus the separate approving Review v2.1. The Plan's preserved author text `PLAN_PENDING_REVISED` and `ASK OK?` is historical author-stage content; the separate Review v2.1 supplies the effective approval. HDE-EPIC040 Implementation Plan v1.0 and its v1.0 review are invalidated source-failure history and must never be used as PR02 authority. Denied Plan v2.0 and Review v2.0 remain lineage and Canon-decision history, not the current approved Plan/review pair.

The PR-10 source is `PR-10 — Create PR Work-Unit Instructions — 091226.1`, AI Prompts / HDE IA, Notion page `3d94590a-05eb-815c-aaad-d396564fe6df`, retrieved revision `2026-09-12T13:41:35.418Z`, ecosystem release `GCFPE-20260912.1`. The page's final template block contains a stale `091126.1` phrase; the title, header, direct reference and release identify 091226.1 unambiguously. This internal prompt-text anomaly does not change the task or artifact lineage and is pending the GCFPE management owner rather than repaired here.

## 2. Dependency readiness and repository/reference baseline

PR02's sole earlier delivery dependency is PR01. That dependency is satisfied by the saved PR01 lineage review v1.1 decision **ACCEPT**. PR #403 is the attributable merged delivery for PR01. At the PR01 review capture (`2026-09-12T10:49:37Z`), the landed squash commit and observed main were `3828d4b3454259841a3e48d13039dd1475754f2f`, tree `529306a74268f2a46765bf40defdae49026d103e`; the reviewed/tested branch head was `75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950` with the same tree. Tests were not claimed on the landed SHA. No later-main divergence was observed at that capture.

This PR-10 execution does not claim a fresh repository head. PR-20 must establish action-time repository instructions, checkout, main/head, user changes and later divergence before planning changes. It must preserve the accepted PR01 source contracts and distinguish any later repository work from PR #403 attribution. No PR02 branch, commit, PR, implementation, test execution, review, CI, QA, Ops or release result exists yet.

The accepted PR01 baseline delivered the exact source/config/schema and bounded local-validation layer on which PR02 depends, including:

- the canonical Channel, Gate, Magic10 configuration, caps/category/threshold and strict schema sources at their approved repository homes;
- bounded duplicate-aware raw/schema/relational checks and explicit no-active-handle separation in `engine/config/registry_loader.py`;
- selected-root writer/projection corrections and required generated companions;
- unchanged FE/BE schema identities and promises;
- current `catalog/manifest.json` version `1.0.0`, timestamp `2025-12-26T00:00:00Z`, root `catalog/` and 15-member roster, with only legitimate PR01 source consequences; and
- no claim of full immutable production admission, recursive freezing, active release, 31-member promotion or production fallback.

PR02 must consume those accepted outputs. It must not redo PR01, silently replace its exact data, or use local fixtures/generated projections as evidence that the actual complete production release already exists.

## 3. Approved scope and exclusions

The selected Epic scope remains exactly HDE-SEPA005 and HDE-SEPA005.1 through HDE-SEPA005.5. PR02 owns the strict admission/immutability and shared Gate-normalization portion of HDE-SEPA005.3–005.5, within the parent production mechanics configuration contract.

The following 29 units remain Done/context and excluded from this Epic's implementation scope: HDE-SEPA001 and HDE-SEPA001.1–001.6; HDE-SEPA002 and HDE-SEPA002.1–002.8; HDE-SEPA003 and HDE-SEPA003.1–003.6; HDE-SEPA004 and HDE-SEPA004.1–004.5. Current PF09.3 v1.1.5 is status evidence only; HDE-SEPA006 and its family do not enlarge the pinned PF09.3 v1.1.3 inventory.

PR02 expressly excludes:

- PR03's classifier, four-argument Gate-based kernel, signals/categories, pair identity and pure-result production;
- PR04's no-user/admin birth/chart/identity resolution, application eligibility, cache/orientation, Reader/internal/CLI behavior and narrative augmentation;
- PR05's eight-golden comparator and current-row readiness tool;
- PR06's actual 31-member promoted manifest, complete release convergence and active-release proof;
- PR07 DOC-10 documentation and OPS01 external clean-candidate verification;
- new mathematics, tuning, optional configuration, public fields/routes, caller UUID, fabricated Gates, persistent identity model, public Reader UUID5 conversion, second calculator, SEPA006 migration, database migration/backfill, vendor acquisition, live production changes or inherited HDE-CRD-0001 exceptions; and
- direct edits to PF10 or other Canon, new generic evidence families, prompt/policy/register mutations, or a deployment/release claim.

## 4. Required PR02 outcome and bounded ownership

Construct one validated, deeply immutable internal production mechanics bundle only from a complete admitted release, while keeping local authoring/candidate data semantically and structurally distinct. A candidate capture can support diagnostics and projections but cannot become an active production handle. Only the active admission path may supply the exact immutable interface later consumed by PR03.

| Concern / locus | Required PR02 outcome | Ownership limit |
| --- | --- | --- |
| `engine/config/registry_loader.py` | One fail-closed admission pipeline using the accepted shared raw/schema/relational validation implementation; safe root, exact captured bytes, source and manifest closure, internal candidate/admitted distinction, recursively immutable result | Do not create a caller-selectable mechanics path, alternate validator, permissive fallback or active bundle from incomplete release data |
| `engine/bodygraph/gates.py` | One shared pure Gate normalizer with the exact contract in §5; reusable by later application/readiness owners | No I/O, environment access, hardcoded second topology or public Reader raw-Gate input |
| `engine/config/bundles.py` and existing configuration tooling hooks | Consume only the validation/capture interfaces they genuinely need; preserve selected-root attribution and FE/BE compatibility | Do not advertise an active Magic10 identity from a lower-level projection or regenerate unrelated outputs |
| `catalog/manifest.json` and its current schema/validation owner | Validate complete member format, paths, canonical bytes, hashes and sizes for production admission | Current 15-member baseline is not the final 31-member promotion; PR02 must not mutate it merely to manufacture production conformance |
| Existing config/schema sources | Validate exact PR01 bytes and cross-source closure before admission | Do not repair malformed active input by reserialization, use generated snapshots as authority or modify adopted data/defaults |
| Tests under `tests/config/` and exact current owners discovered by PR-20 | Demonstrate all positive, adverse, identity and mutation boundaries against actual implementation | Synthetic complete release fixtures are permitted only as labeled test fixtures, never production-release proof |
| CI classification/workflow owners when actually affected | Ensure every changed production/test path maps to meaningful applicable checks and the selected current CI lanes | No gate weakening, broad CI redesign, stale-head result, fabricated waiver or inherited exception |

Internal class/function names for candidate capture and admitted bundle are PR-20 design choices after source inspection. Their semantic distinction is mandatory; this instruction does not claim those APIs already exist.

## 5. Shared Gate-normalization contract

Implement one normalizer in `engine/bodygraph/gates.py` with no I/O or environment dependency.

Accepted input is a nonempty raw array whose members are only:

- exact integers 1 through 64, excluding booleans; or
- canonical decimal strings `"1"` through `"64"`, with no sign, whitespace, leading zero or decimal form.

Reject missing or empty input; integers outside 1–64; booleans; floats; signed, zero-padded, whitespace-bearing, decimal or otherwise noncanonical strings; unknown forms; and duplicates after normalization, including `[1, "1"]`. Do not deduplicate invalid input into success.

The normalized result is all three of:

1. an ascending unique tuple of Gate integers;
2. an unsigned 64-bit mask with Gate `g` at bit `g-1`; and
3. exactly sixteen lowercase hexadecimal digits for that mask.

Center/catalog closure is supplied through the admitted registry; do not add another hardcoded topology. Persistence, resolver/adapter, application and readiness owners later call this same function at their own seams. The existing public Reader continues to accept only exact canonical lowercase UUID input IDs under its own contract; PR02 does not add public raw-Gate input.

## 6. Production admission pipeline

The production admission implementation must perform these semantics in a coherent fail-closed order. PR-20 may refine exact per-file sequencing after reading current code, but it may not weaken or omit a predicate.

1. Resolve one explicit authorized repository root once. Reject path escapes, symlink escapes, missing or ambiguous authoritative paths and unexpected source locations. No global-root leakage or mixed-root assembly is permitted.
2. Read each authoritative source into an owned byte capture. Validate and parse those captured bytes; never hash one read while parsing another. Recheck sources at the required consistency boundary and refuse if they changed between capture stages.
3. Reject duplicate JSON object keys before ordinary JSON decoding can erase them.
4. Validate UTF-8 with no BOM, exactly one terminal LF, canonical compact/sorted object bytes, governed array order and exact numeric form. Reserialization is a comparison, not a repair of invalid active input and not a basis for laundering a hash.
5. Execute the actual local closed schemas without remote resolution. Decode only exact schema types and explicitly reject booleans where integers are required.
6. Run the accepted shared relational validator for complete roster/order, Channel/Gate/Center closure, caps/category/signal/profile/default joins, source-path and source-hash equality, fixed operations/scales and all initial adopted defaults. Schema validity alone is insufficient.
7. Validate every manifest/member format before exact member-path, canonical-byte, SHA-256 and size comparison. Production admission rejects missing or extra promoted rows, unsafe or unexpected paths, hash/size mismatch, invalid format and noncanonical bytes.
8. Reject generated config snapshots, Markdown, aliases, candidate roots, caller-supplied config IDs, direct selectors, skip-manifest/skip-validation flags and prior successful bundles as production fallback.
9. Copy data out of temporary parser structures, then recursively freeze every nested value. Ordered collections become tuples; mappings and records are immutable; no mutable parser, source or caller reference survives.
10. Retain configuration-byte digest, referenced source-byte identities and manifest-derived release identity as distinct internal facts. No free caller override enters scoring; no internal digest becomes a new public or config field.
11. Return the active immutable bundle only after every predicate succeeds. Any failure returns the owning typed failure and no partial handle; no stale successful bundle is served to rescue the request.

The accepted local authoring/candidate capability remains separate: it may validate proposed data/config/schema graphs and generate diagnostics/projections in one selected root, but it cannot return an active mechanics bundle or select an active release. Production generation of `config.magic10` through its owning generator must refuse when active admission is unavailable. Its complete active snapshot awaits the actual full release owned by PR06.

## 7. Source contracts that PR02 must enforce

PR02 validates, but does not redefine, the accepted PR01 sources:

- the exact 36-row Channel catalog and 64-Gate topology, including ascending Gate-pair IDs, sorted distinct Gate-derived Center sets, fixed `circuit_primary`/`substream` assignments, and all 108 retained non-scoring Product metadata values;
- the mechanics configuration's exact ten top-level keys: `category_weights`, `config_id`, `profiles`, `response_scale`, `result_schema`, `rounding`, `schema`, `signal_scale`, `signals`, `sources`;
- `schema=magic10_mechanics_config.v1`, `config_id=m10-channel-state-v1.0.0`, `result_schema=magic10_result.v1`, `response_scale=10000`, `signal_scale=2`, signal rounding `round_half_up_to_half_score_unit`, category rounding `round_half_up_once`;
- exactly three ASCII-profile-ID-ordered nested profiles and 15 response values; `none=0` is valid, while Channel/category weights are exact integers 1–3 with adopted defaults 1 and `[1,1]`; booleans, floats and strings are invalid numeric substitutes;
- exactly 20 ordered signals, 90 default Channel memberships and 10 ordered category-input pairs; every Channel is used, there is no duplicate Channel within a signal or across the two signals of one category, and Balance signals have no profile;
- exactly four source records, each only `path` and lowercase 64-hex `sha256`, for caps, categories, channels and thresholds at their accepted paths, hashing the actual validated bytes;
- closed config, pure-result and internal-result schemas, with strict nested objects and governed order/domains; and
- unchanged FE/BE schema identities and field promises.

The pure-result and internal-result shapes are validation dependencies, not PR02 producers. PR03/PR04 remain responsible for actual calculation and application results. PR02 must not manufacture result fixtures as evidence of those later behaviors.

## 8. Acceptance, tests and evidence

These are future PR02 engineering proofs, not tests executed by this instruction. PR-20 must bind each proof to actual current functions, files, commands, writers and CI owners after source inspection.

| Proof group | Required positive proof | Required adverse proof / no-success condition |
| --- | --- | --- |
| Complete synthetic admission | A labeled complete valid synthetic release loads through the real production admission path and returns the active immutable interface expected by PR03 | Fixture success is not described as actual promoted release, deployment or production conformance |
| Gate normalization | Every canonical integer/string boundary produces the same ascending tuple, uint64 mask and 16-lower-hex form | Missing/empty, duplicate, `[1,"1"]`, 0/65, bool, float, signed/leading-zero/whitespace/decimal/nondecimal strings refuse |
| Raw/canonical bytes | Exact canonical UTF-8 source bytes with one LF validate without rewrite | Duplicate keys at governed levels, BOM, CRLF, extra LF, noncanonical objects/order/numeric form and normalized-hash laundering refuse |
| Schema and relational closure | Actual local schemas plus all roster/order/topology/profile/signal/category/default/source joins succeed for a complete fixture | Valid-looking but relationally incoherent data, remote schema resolution, wrong operations/scales/defaults/types/order or source closure refuse |
| Root and capture integrity | Deliberately different valid roots remain isolated; one owned capture supplies parse/hash/identity | Path/symlink escape, global-root leakage, identical-source cross-root mixing, source replacement/change between capture stages or ambiguous authority refuses |
| Manifest admission | Complete member formats, expected roster, canonical bytes, paths, exact hashes and sizes all agree | Missing/extra/unsafe member, wrong path/hash/size/format, noncanonical member bytes or partial roster produces no active handle |
| Candidate/admitted separation | Candidate/local validation can support its bounded projections without an active identity; only complete admission returns the active bundle | Generated snapshot, alias, caller config ID, direct selector, skip flag or prior bundle cannot bypass admission |
| Deep immutability | Attempted mutation of every nested collection, record, mapping, profile response, source, caps/category/signal/Channel structure and returned value cannot alter a usable bundle | Leaked parser/caller references, shallow freezing or mutable nested state fails; freeze never substitutes for prior validation |
| Failure/fallback | Every owning typed failure returns no partial handle, and a later failed admission cannot serve a stale prior success | Cached prior bundle, partial success, exception suppression or successful legacy fallback is prohibited |
| Projection/evidence | Only actually affected projections are regenerated from one selected root through owning writers, with exact attribution and required existing companions | Unrelated regeneration, direct companion edits, partial family success, generic evidence token or early active `config.magic10` claim cannot pass |
| Engineering review and CI | Actual changed diff receives code and security review; all findings are read and dispositioned; corrected code is re-reviewed/retested; applicable CI passes on the identified head | Green counts alone, skipped required lane, stale-head review/check, missing changed-path ownership, unsupported waiver or unreviewed repair cannot complete the unit |

The minimum adverse matrix from approved Plan §7.3 remains applicable. For PR02, the deciding rows are config shape, cross-source closure, bytes/path, immutability, Gates and release/evidence. Later mechanics, application, comparison/readiness and external-final rows remain explicit downstream dependencies rather than PR02 completion claims.

Required evidence is native per-file/behavior attribution, exact test commands and observed results, tested commit/tree, changed paths, review mechanism and findings/dispositions, corrected-code coverage, current CI run/check/job/log identity, generated primary/companion changes where any, and truthful remaining limits. Reuse existing valid evidence, but never substitute PR01 results for PR02 execution.

## 9. Requirement and acceptance allocation

| Requirement | PR02 obligation and retained later owner | Acceptance contribution |
| --- | --- | --- |
| K040-REQ-001 | Deliver the second bounded layer in the ordered eight-unit capability; no parent/Epic completion claim | AC040-01/08 dependency continuity |
| K040-REQ-002 | Preserve exact PF01/PF02/PF12 homes and all approved C040 decisions; no new Canon interpretation | AC040-01/09 |
| K040-REQ-003 | Enforce the complete PR01 36-Channel/Gate/Center/schema contract during admission | AC040-02 |
| K040-REQ-004 | Preserve all Product metadata and existing FE/BE/public contracts through validation/interfaces; application use remains PR04 | AC040-02/09 |
| K040-REQ-005 | Validate adopted config/default and result-schema dependencies; actual signal/category production remains PR03/04 | AC040-03/04 |
| K040-REQ-006 | Supply one immutable manifest-bound active configuration with no partial/snapshot fallback; actual complete promotion remains PR06 | AC040-04/09, partial AC040-05 |
| K040-REQ-007 | Own strict schema-loaded immutable bundle and shared Gate normalizer; PR03/04 consume them | AC040-04/07 |
| K040-REQ-008 | Own admission/Gate/raw/schema/path/hash/immutability/fallback refusal; later runtime/application refusal remains PR03–PR06 | AC040-04/09 |
| K040-REQ-009 | Keep config/source/manifest/release identities distinct and exact; pair identity remains PR03 and final release/repo proof PR06/OPS01 | AC040-05 |
| K040-REQ-010 | Preserve the interface needed by all eight later goldens; do not claim or compute their actual results here | AC040-06 later |
| K040-REQ-011 | Deliver complete Gate/admission/immutability adverse coverage; later identity/application/readiness coverage remains PR03–PR06 | AC040-04/07/08 |
| K040-REQ-012 | Use owning writers and same-root required companions for any actually affected projection; final convergence PR06 and external proof OPS01 | AC040-08/09 |
| K040-REQ-013 | Preserve exact instruction/Plan/dependency/test/PR/commit/decision lineage and prompt-use evidence; repository provenance stays separately authorized | AC040-01/09 |

PR02's decisive acceptance is candidate-versus-admitted separation, actual schema/closure execution, exact shared Gate normalization, recursive immutability and fail-closed production admission. PR03 may consume the resulting exact immutable interface with complete fixtures. Production conformance, active full release and AC040-05/06 whole-chain completion remain unclaimed until their assigned later units.

## 10. Engineering lifecycle, generation and recovery

PR-20 receives only this saved PR_INSTRUCTION_ID as its substantive input and creates one detailed executable per-file Plan. It must inspect the complete current repository instructions and affected source, then map every obligation above to actual changes, tests, commands, evidence, review and CI. It must preserve user work and action-time branch state. It may split the unit into ordered PRs only when dependencies remain explicit and the whole PR02 unit cannot be represented as complete until all ordered parts are delivered and reviewed.

Only the Product Owner's later invocation of PR-30 for the exact visible PR_IMPLEMENTATION_PLAN supplies Proceed. The same dedicated PR02 session then owns implementation, tests, publication where authorized, actual code/security review, reading and dispositioning findings, in-scope repairs, re-review and corrected-code coverage, CI interpretation, completion evidence and attributable return. PR-30 never gains merge authority from Proceed. At engineering completion it reports **Ready to merge** with the PR reference and returns control to the Product Owner.

Primary data/config outputs must precede any derived projections and required companions. Regenerate only families whose actual sources or implementation attribution changed, from one selected root through their owning writers. Preserve Index/Mirror/pathproof/checksum ownership. No partial success is claimed if a primary, validation, derived generation, replacement or companion step fails.

Recovery restores the loader, Gate normalizer, compatible callers, tests, typed interfaces and any actually affected generated outputs as one compatible set. Keep the previously active complete release untouched. Preserve caught-failure restoration and conflicting external changes; do not overwrite user changes to force rollback. This instruction promises no crash/process-death atomicity, multi-file atomic visibility or cross-process locking beyond the approved/reviewed mechanisms actually implemented and evidenced.

Security boundaries are fail-closed safe paths, zero network/remote-schema fetch, no environment-driven or caller-selected active configuration, redacted diagnostics, and no secrets, birth records, real chart payloads, DB/vendor access or live settings changes. Synthetic fixtures must contain no sensitive production data.

## 11. Canon-conflict register and unresolved facts

The complete six-entry register is carried by exact retrievable lineage: approved Plan v2.1 §11 (current overlay §11.1 and original proposals/history §§11.2–11.3), original C040-06 ADR v1.0 `libfile_c9897950d9588191a2c822b65e7b31a8`, Review v2.0 §§7–8 `libfile_aecae34a83e88191a205d22fd0348b62`, and approving Review v2.1 §6. No proposal, source binding, alternative, affected requirement, interim treatment, risk, drainage owner or decision is omitted or changed by this instruction.

| Entry | Preserved decision and current status |
| --- | --- |
| C040-01 CANON_RECONCILIATION | Thoth-17 APPROVED exactly, 2026-09-08T13:23:24Z. Current PF09.3 Notes/status align; pinned selected/excluded inventory remains; published Addenda 2.2/2.4 history retained. |
| C040-02 CANON_RECONCILIATION | Same Thoth decision. PF12 filename/body resolved at v2.9.6; old discrepancy is history. |
| C040-03 CANON_RECONCILIATION | Same Thoth decision. PF14 filename/body resolved at v3.5.7; C040-05 legacy content is separate. |
| C040-04 CANON_RECONCILIATION | Same Thoth decision. PF19 filename/body resolved at v3.0.5; no QA authority inferred. |
| C040-05 CANON_RECONCILIATION | Isis-49 APPROVED alternative A exactly, 2026-09-09T03:57:16Z. Four-argument Gate-based core controls; no optional scoring configuration or second calculator. PF14 §6.7 legacy precomputed-score drainage remains pending/non-gating with its governed maintainer; Addendum 2.3 is published; HDE-DIST008.1 stays separate. |
| C040-06 NEW_CANON | Isis-50 APPROVED alternative A exactly, 2026-09-09T11:48:08Z, against Plan v2.0 and original ADR v1.0; Plan v2.1 later independently APPROVED. Exact 36 assignments, 64 Gate facts and 16 states remain. PF10 v13.1.6 Addendum 2.5 body/index publication is verified; permanent PF12/PF01 drainage and stale preparation wording remain pending/non-gating. |

None of C040-01–06 is REJECTED or APPROVED_AS_CHANGED. The unselected alternatives and invalidated Plan v1.0 are different objects and do not change these decisions. PR02 may enforce the approved data/structure but cannot decide Canon, reopen research generically, duplicate published addenda or mutate PF10.

Unresolved but non-gating facts carried forward:

- permanent C040-05/C040-06 Canon drainage and stale published-preparation wording remain with their existing governed owners;
- repository prompt-use persistence is pending an actually installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure and an authorized repository writer; at the last verified baseline that procedure was absent, and PR02 must verify action-time state before any authorized persistence;
- the Notion connection cannot inspect Custom Agent sessions, but the user-assigned retained IA reference is sufficient for this PR-10 operation; no platform ID is invented; and
- PR02 actual branch/head, implementation, tests, reviews, CI, PR and merge remain NOT PRODUCED / NOT EXECUTED.

## 12. Rescope and failure routing

An ordinary instruction transcription defect is corrected by this same retained IA. An ordinary in-scope engineering defect is owned by the later dedicated PR02 session under its actual PR-30 authority. Neither needs a new ADR or rescope.

A genuinely evidenced material scope, architecture, requirement, design, public-contract or migration change must not be absorbed into PR02. Preserve the exact source/path/clause, evidence, affected requirement, dependency impact, completed unaffected work and current state, then route through the current RS-10 and RS-20 contracts. If the approved whole-change Plan itself is defective, return the exact Plan/review/Specification and evidenced delta to the existing IA/Isis correction owner. No PLAN_REVIEW_ID, Product Owner disposition, Canon decision or approval is fabricated.

If an indispensable PR02 source or dependency is unavailable, preserve the instruction and return BLOCKED with the precise missing identifier, evidence location, recovery owner and resume point. Mere commit movement, age, slow work, unavailable session-inspection API or the separately pending drainage/provenance tasks do not by themselves invalidate this instruction.

## 13. Prompt-use and artifact lineage

`GCFPE_PROMPT_USES`:

- usage ID: `GCFPE-USE-HDE-EPIC040-PR-10-20260912-PR02-REV21-01`;
- capture: `2026-09-12T16:04:04Z`;
- change/component: EPIC / HDE-EPIC040 / HDE-EPIC040-PR02;
- Specification: `libfile_12bab860949c8191881510875f051460`, v1.1;
- source prompt: PR-10 / 091226.1 / GCFPE-20260912.1 / Notion page `3d94590a-05eb-815c-aaad-d396564fe6df` / retrieved revision `2026-09-12T13:41:35.418Z`;
- role/stage: retained whole-change IA / PR work-unit instruction creation;
- actual runtime identity: unobserved and not inferred;
- result: this PR_INSTRUCTION v1.0; its actual Library ID and saved-byte digest are populated by the returned handoff after persistence rather than invented inside the source body;
- preserved upstream use/history: exact Plan v2.1 §13, Review v2.1 §7, PR01 Instruction v2.0 §13, PR01 Detailed Plan v1.1 §12/Appendix E, PR01 Result v1.0, and PR01 lineage review v1.1; prepared-only uses remain non-executed history; and
- repository persistence: pending/non-gating until an authorized writer verifies an installed current provenance procedure. This instruction grants no repository write.

The earlier source-failure Plan v1.0/review, denied Plan v2.0/review and superseded PR01 artifacts remain preserved history. They are not current PR02 inputs. PR01's actual instruction, detailed Plan, implementation Result, PR #403 and ACCEPT review remain the exact completed dependency lineage and are not reissued by PR02.

## 14. Semantic comparison and readiness

| Approved source meaning | Instruction location | Owner / evidence stage |
| --- | --- | --- |
| Plan §6.2: strict immutable input/admission after PR01 | §§2, 4, 6 | PR02; actual implementation/review/CI later |
| Plan §§5.2/5.5: exact Gate inputs, capture, raw/schema/relational/hash checks and recursive freeze | §§5–7 | PR02 tests; AC040-04/07 |
| Plan §4.3: candidate validation is not active admission | §§4, 6, 8 | PR02 interface/adverse proof; active full release PR06 |
| Plan §7.3: path, bytes, manifest, mutation and fallback refusals | §§6, 8 | PR02 test matrix; no present PASS claimed |
| Plan §§6–8: preserve PR01 data, later unit ownership and ordered dependencies | §§2–3, 9–10 | Same IA decomposition; PR03 only after PR02 ACCEPT |
| Review v2.1 §§5.2–5.3: exact requirements, acceptance and unit closure | §§8–11 | PR02 contributes only its assigned layers |
| PR01 review v1.1: merged attributable dependency, PR02 not yet delivered | §§2, 13 | Dependency ready; no PR02 execution invented |
| Current PR-20 091226.1: sole substantive input, detailed planning, code/security review, CI, recovery and direct PR-30 package | §§8–10, 15 | Dedicated PR02 session; PR-20 only after handoff |
| Current PR-10 091226.1: exact identity, rescope, storage, provenance and direct handoff | §§1, 11–15 | Retained IA; artifact save/readback now |

No decisive source-comparison failure, missing approval, dependency gap or material boundary was found. The exact approved Plan/review IDs and `WORK_UNIT_ID: HDE-EPIC040-PR02` are present. This instruction is therefore **INSTRUCTION_READY**.

## 15. Direct handoff to PR-20

`NEXT_PROMPT_HANDOFF`

**Destination prompt name, direct Notion reference and verified directory:** [PR-20 — Create Detailed PR Implementation Plan — 091226.1](https://app.notion.com/p/3d94590a05eb812293cbf71033757a85), AI Prompts / HDE IA; retrieved revision `2026-09-12T13:41:41.142Z`.

**Receiving session or role:** dedicated HDE-EPIC040-PR02 PR engineering/planning session. `session_disposition: INITIAL_DEDICATED_ASSIGNMENT`; `role_session_ref: NOT_YET_ASSIGNED — Product Owner/operator assigns the dedicated PR02 session at launch`; `invocation_binding: EPIC / HDE-EPIC040 / HDE-EPIC040-PR02 / PR-20 detailed planning from this exact instruction`; `context_conflict: NONE established`. This handoff does not create, replace, message or dispatch a session, and the PR01 engineer session is not repurposed.

**Relevant identifiers:** `CHANGE_CLASS: EPIC`; `CHANGE_ID: HDE-EPIC040`; `WORK_UNIT_ID: HDE-EPIC040-PR02`.

**Sole substantive input:** `PR_INSTRUCTION_ID` for this exact saved HDE-EPIC040-PR02 PR Work-Unit Instruction v1.0. The returned outer handoff must populate its actual Library ID and saved-byte SHA-256 after save/readback; no self-ID is invented in this body.

**Complete native lineage:**

- `SPECIFICATION_ID: libfile_12bab860949c8191881510875f051460`, HDE-EPIC040 Specification v1.1, approved by Thoth-17;
- `IMPLEMENTATION_AUDIT_ID: libfile_823ee8e9ecb0819185181ec7695265fb`, Audit v2.0 / AUDIT_COMPLETE;
- `IMPLEMENTATION_PLAN_ID: libfile_11c992cda3f0819199827e86584e41f1`, Plan v2.1;
- `PLAN_REVIEW_ID: libfile_b85b81651a508191abdfd8f81803caf8`, Review v2.1 / Isis-50 APPROVE;
- accepted predecessor `libfile_47bf2e063d208191bf57f93c71f96821`, PR01 lineage review v1.1 / ACCEPT, with merged PR #403 attribution; and
- the complete Canon-conflict, repository/reference, source, dependency, exclusions, behavior, interface, acceptance/test/evidence, security, recovery and prompt-use package in this instruction.

**Current status, decisions, constraints and unresolved items:** PR02 instruction is INSTRUCTION_READY. PR02 detailed planning and implementation are NOT EXECUTED; PR02 branch/commit/PR/tests/reviews/CI/merge are NOT PRODUCED. PR-20 must confirm action-time repository instructions and baseline and distinguish later divergence. Plan v1.0/review v1.0 are invalid history. No Product Owner Proceed, implementation, merge, QA/Ops, release, PF publication or scope change is authorized. Canon drainage, repository provenance installation/persistence and the PR-10 stale-version-text anomaly remain pending/non-gating with their existing owners.

**Expected receiving output:** one complete PR_IMPLEMENTATION_PLAN for HDE-EPIC040-PR02, saved in `/Glow HDE 3.0`, with exact instruction/upstream refs, action-time repository baseline, actual files/components and interfaces, ordered implementation sequence, requirement-to-change/test/evidence mapping, dependency/PR ordering, migration/security/recovery, review/CI duties and continuing session identity. Use `AWAITING_PO_PROCEED` only if the Plan is executable within approved scope and identifies its exact saved Plan/version. A material boundary returns a truthful draft and the exact RS-10/RS-20 route.

**Operational tools/channel and gates:** use the current Notion PR-20 contract and permitted Library/Drive/repository boundaries; resolve controlled PF sources only through the canonical predicate when action-time source selection is needed; inspect current repository instructions and affected source read-only during planning; preserve the automation hold, dedicated-session boundary, Product Owner Proceed, manual merge, code/security review, CI, storage, recovery and rescope controls. The inability to inspect Notion Custom Agent sessions is an access limitation, not permission to invent a session ID.

**Required next action:** the Product Owner/operator assigns or selects the dedicated PR02 session and invokes PR-20 with the sole substantive input `PR_INSTRUCTION_ID`. Do not execute PR-20, PR-30, implementation, merge, QA/Ops, release, publication or rescope from this handoff.

**Handoff status:** READY_FOR_NEXT_TASK

**END — HDE-EPIC040-PR02 PR WORK-UNIT INSTRUCTION v1.0 / INSTRUCTION_READY**
