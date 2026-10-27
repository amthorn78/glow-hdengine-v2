# T-PF12 — exact redlines from PF12 v2.9.6

Run: `gtwpe-20261026-pf10-v13-8-8/T-PF12`. Preparation revision: `P1`.
Originating preparer: TW-DRAIN-10 in the Nathan-started T-PF12 document session, Claude Code cloud session https://claude.ai/code/session_01AaKkpYtrGxYudeyWaEnMX3.
Target: `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md` (`PF12-Canon-HDE-Schemas-and-Artifacts` v2.9.6) at `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a`, byte-identical at `0838ba08254eaefc888019df49a06aa2ae99cc6c`; Git blob `1542a8f78846fcdd684f6a4dec7b663616ec8c02`; 622,934 bytes; 6,096 LF line terminators, the last line empty (the file ends `LF LF`); raw UTF-8 SHA-256 `5bf86058e30c4cfd7dbaa9532b169d9a9b0e3d64089abc254a75bbf162a2227d`.
Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`, unchanged on `main`), task `T-PF12`, rows A07, A08, A24, A25, A26, A15, A16, A17 with X03 and S-APR, and S-CR3.
Sources: PF10 v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter 1–223; addenda 2.7 (688–889), 2.8 (890–1002), 2.15 (1620–1690), 2.16 (1691–1825), 2.17 (1826–1955), 2.24 (2693–2790), 2.25 (2791–2899), 2.26 (2900–2986); 2.18 (1956–2081) read as supporting reading for the supersession of 2.15 and 2.16 ceiling passages. HDE-CRD-0002 Specification v1.1 approved (`docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, blob `c4802a5a7fa3`): S-APR 147–193 and CR-3 221–230, overlaid by delta 01 (`docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, blob `9408d6ed091b`) C-8 to C-12. Supporting cross-references: X03 `docs/adr/hde/close_pack_writer_adr.md` (blob `2d91679a1981`), Decision section and lines 76–88; X04 `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md` §18 (lines 753–792), carried by 2.8.
Prompt: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.
Preparation outcome: `READY` after whole-batch producer validation. Save completeness is recorded in the separate proof log, `redlines-PF12-from-v2.9.6.proof-log.md`.

These are thirteen independent original-bound `REPLACE` operations. Each resolves to one exact span of the unchanged original; no two spans intersect or touch. Where a redline adds text after existing text, its OLD block is one unique anchor line or block, and its NEW block reproduces that anchor verbatim before the added text, so no gap anchor is needed. Header control fields are reserved for TW-APPLY-10.

Payloads are literal. The single LF immediately before a closing fence is presentation only and is not part of the payload; every other LF, including blank lines inside a payload, and every trailing space is exact. Every OLD block starts at a line start and ends at a line end, so the original LF that follows it stays in place. Fences are four backticks, longer than any backtick run in a payload. The byte count and SHA-256 under each literal are of its UTF-8 bytes as delimited here.

## RL-001

Redline number: RL-001
Findings or source items: S-CR3 (Specification CR-3, APPROVED_AS_CHANGED); CD-2
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
Original-bound location: §1.2 "Change-container compatibility (normative)." second bullet
Original lines (context only): 590
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-3 records that §1.2 points to "the stable CRD ID recorded in PF30" while HDE Governance §9.1.1 forbids the active workflow to create HDE CRD Records entries, so the record the passage names will not exist. Its approved disposition is that the HDE Schemas & Artifacts owner rewords §1.2; its interim treatment names the change's own Specification as the governing record and the Product Owner-assigned ID as the CRD ID. HDE Governance §9.1.1 assigns class selection to the Product Owner, and its §1.1 holds a CRD accountable through its controlled CRD identity and approved CRD Specification, whose record control carries the CRD ID. The rest of the bullet is unchanged.

OLD

````text
* For a CRD, the stable CRD ID recorded in PF30 replaces `EPIC-\#\#\#` as the filename prefix in the baseline suffix patterns below and replaces `<epic-id>` in supporting paths using its lower-case ASCII, hyphenated directory form.  
````

OLD literal: 233 bytes; SHA-256 `46e22eab9f617e88b9436f3478057259260f9ac2e95e3989f2c33252eda64470`.

NEW

````text
* For a CRD, its controlled CRD ID, which the Product Owner assigns at class selection and the change's approved CRD Specification records, replaces `EPIC-\#\#\#` as the filename prefix in the baseline suffix patterns below and replaces `<epic-id>` in supporting paths using its lower-case ASCII, hyphenated directory form. The identity does not depend on an HDE CRD Records entry.  
````

NEW literal: 383 bytes; SHA-256 `ef403e26c2908a5980d00043e16428371bad72b209c9df2118f56dcbd188fccc`.

## RL-002

Redline number: RL-002
Findings or source items: A15 (approved design); A16 (required drainage: §1.2 "Close-pack artifacts"); A17 (amended design, routed by title); X03 (ADR canon table row for §1.2; Decision 1 to 4, 6, 8; "Epic-only identity inventory"); S-APR (S21 canon impact)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
Original-bound location: §1.2, the paragraph that closes "Change-container compatibility (normative)."
Original lines (context only): 595
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.15 approves one writer with a second, closed v2 schema for Epic and CRD identities, v1 unchanged, CRD paths of record with the directory form, rendering from tracked inputs, the kept feedback-dependency refusal, requirement text bound by reference, and absent-tolerant CRD close-pack Index rows. 2.16 names §1.2 "Close-pack artifacts" as required drainage and confirms the landed rows, posture and check mode. The ADR's canon table asks §1.2 to record close_candidate_source.v2 and the closed Epic-only inventory, which its "Epic-only identity inventory" section states. The closure decision's criteria and the closure-override treatment (2.17 resolution A) drain to Change Process Guide and HDE Governance, so this redline routes them by title instead of restating them. Repository facts were inspected read-only on main 0838ba0c: the v2 schema's identity pattern and posture enum, the v1 schema's epic_id pattern, the writer's EPIC_RE, the six Epic-specific tools, and the updater's close-pack row keys and absent-tolerant refusals.

OLD

````text
Before the first affected CRD close-pack enters QA or closeout, every schema, generator, or validator that accepts only `EPIC-\#\#\#` or `<epic-id>` MUST be identified and updated through the authorized change lane.
````

OLD literal: 215 bytes; SHA-256 `e2debffc70dd2b02cd400a2ecff49fe1025aa1d1f29f3464c35540e40754cce0`.

NEW

````text
Before the first affected CRD close-pack enters QA or closeout, every schema, generator, or validator that accepts only `EPIC-\#\#\#` or `<epic-id>` MUST be identified and updated through the authorized change lane.

That identification is complete for the generic close-pack surfaces. The v1 candidate-source schema's `epic_id` pattern and the writer's `EPIC_RE` accepted only Epic identities; both remain for v1 sources, and the v2 candidate-source schema accepts both Epic and CRD identities. The Epic-specific families `tools/qa/epic021_qa.py` and `tools/qa/generate_epic025_close_pack.py` to `tools/qa/generate_epic029_close_pack.py` remain epic-specific. The read-only checks that a close run uses carry no Epic or CRD identity rule, and `ci/checks/check_mirror_schema.sh` admits `crd_id`.

Generic close-pack writer (normative).

* `tools/qa/generate_epic_close_pack.py` is the single generic writer for Epic and CRD close packs. It selects its model by the candidate source's `schema_version`.  
* A source whose `schema_version` is `epic_close_candidate_source.v1` is read against `schemas/epic_close_candidate_source.v1.json` and keeps the v1 model, refusals, and output bytes.  
* A source whose `schema_version` is `close_candidate_source.v2` is read against `schemas/close_candidate_source.v2.json`, a closed schema for exactly one Epic (`HDE-EPICNNN`) or CRD (`HDE-CRD-NNNN`, four or more digits) identity.  
* An Epic close writes `audit/EPIC-NNN_close_report.md` and `audit/EPIC-NNN_MANIFEST.json`. A CRD close uses its CRD ID as the filename prefix, writing `audit/HDE-CRD-NNNN_close_report.md` and `audit/HDE-CRD-NNNN_MANIFEST.json`, and uses its lower-case ID, for example `hde-crd-0002`, as its directory form.  
* The v2 close report and manifest are rendered only from tracked inputs. Requirement and acceptance text is bound by reference, never copied into a causal field. The feedback-dependency refusal is kept, and the writer refuses as causal inputs the Human Evidence Index, the Machine Evidence Mirror, their hash and checksum sentinels, every `.path_proof.txt`, the orientation output, the close-run family, and `catalog/manifest.json`. Check mode writes nothing and validates the exact committed bytes.  
* The v2 closure decision is `SATISFIED` or `NOT SATISFIED`, stated with the review-trace-only posture. Change Process Guide and HDE-Governance govern the decision criteria, the close report's required content, and the treatment of a check accepted under a closure override.  
* The canonical updater registers a CRD close pack's report and manifest as Human Evidence Index and Machine Evidence Mirror rows `hde_crd_nnnn.close_report` and `hde_crd_nnnn.manifest`, each carrying `crd_id`. The rows are absent-tolerant: when neither file is present there are no rows, and when both are present there is one row each. One file present without the other, or a row whose file is absent, is refused.
````

NEW literal: 2929 bytes; SHA-256 `5bbb14155731f9b817e365478dffc5272e943a854f1019b2055784680a1f96b5`.

## RL-003

Redline number: RL-003
Findings or source items: A15 (close-run family introduced); X03 (ADR canon table row for §1.2: the close-run family path and its post-verdict status; Decision 7); S-APR (S21: where close-workflow run evidence lives)
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
Original-bound location: §1.2, the paragraph that begins "These are baseline closure artifacts (required artifacts)", before "Acceptance-binding family coherence (normative)."
Original lines (context only): 654
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.15 introduces the post-verdict close-run family at audit/qa/<change-dir>/close/<check_id>/primary.log for an admitted CRD, states that it neither reopens nor adds to the approved QA step-logs manifest or any checks/ primary, and admits no Epic family. The ADR canon table asks §1.2 to record the close-run family path and its post-verdict status, and the Specification's S21 canon impact names where close-workflow run evidence lives. §8.17 (RL-010) holds the membership, writer and indexing detail, so §1.2 states only the path, status and boundary.

OLD

````text
These are baseline closure artifacts (required artifacts), not acceptance tokens by default. They MUST NOT be relocated into alternate directory trees (for example audit/qa/\*\* or artifacts/\*\*) without an explicit canon change.
````

OLD literal: 230 bytes; SHA-256 `43f0a78c290aed8c30023e2364ad620cae33c068793426a78b0298f2b39936f9`.

NEW

````text
These are baseline closure artifacts (required artifacts), not acceptance tokens by default. They MUST NOT be relocated into alternate directory trees (for example audit/qa/\*\* or artifacts/\*\*) without an explicit canon change.

Same-run close evidence for a CRD (normative). For a CRD admitted in the canonical updater's CRD admission table, the same-run evidence of the close workflow is its post-verdict close-run family under `audit/qa/<change-id>/close/`, where `<change-id>` is the CRD's lower-case directory form: one `primary.log` per close-run check at `audit/qa/<change-id>/close/<check_id>/primary.log`, each with its sibling `primary.log.path_proof.txt`. The family is written after the final QA verdict. It neither reopens nor adds to the approved `audit/qa/<change-id>/qa_step_logs_manifest.json` or any `checks/` primary, and it is not a close-pack baseline artifact. §8.17 owns its writer, membership, and indexing. No Epic close-run family is admitted.
````

NEW literal: 973 bytes; SHA-256 `9336d2f610f87dda92db125493f9a52dc24a1c9e4d9056e96e7427b72f580269`.

## RL-004

Redline number: RL-004
Findings or source items: A15 (approved design: key_outputs map of path strings); A16 (S21 acceptance (1): key_outputs as an object of strings); X03 (ADR canon table row for §1.2: the v2 manifest and its key_outputs minimum; Decision 5)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
Original-bound location: §1.2 "Close-pack manifest key_outputs (named binding map; normative)", after the generic map rule and before "EPIC023 required bindings (normative)"
Original lines (context only): 926
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.15 approves a key_outputs map of path strings; 2.16 confirms key_outputs as an object of strings. The ADR canon table asks §1.2 to record the v2 manifest and its key_outputs minimum, which ADR Decision 5 states. The schema facts were confirmed on main 0838ba0c: an object of 5 to 64 properties, keys matching ^[a-z][a-z0-9_]{0,63}$, string path values, and the five required keys; HDE-CRD-0002's committed manifest carries exactly those five. The existing generic map rule, which also allows lists, is unchanged; the new paragraph states the narrower v2 instance.

OLD

````text
* when a value is a list, list order MUST be stable and SHOULD be deterministic to preserve diff integrity
````

OLD literal: 106 bytes; SHA-256 `49ca846fd5d9be53bec6b64553511be90eab8ba2f646b7a134aee6e32856ba7d`.

NEW

````text
* when a value is a list, list order MUST be stable and SHOULD be deterministic to preserve diff integrity

Generic v2 writer `key_outputs` minimum (normative)

A close-pack manifest written from a `close_candidate_source.v2` source carries `key_outputs` as an object of five to 64 entries. Each key matches `^[a-z][a-z0-9_]{0,63}$`, and each value is one repo-relative path string, not a list. The map MUST include at least `close_report`, `close_manifest`, `doc_deltas`, `drain_targets`, and `qa_step_logs_manifest`. Every key output other than the close report and the close manifest is also a bound tracked evidence input of the source, so its digest is recorded. The manifest points to the close report by SHA-256 and size and carries no digest of the Human Evidence Index, a path proof, the orientation output, or the close-run family.
````

NEW literal: 841 bytes; SHA-256 `b3a77c50bd260f016a0355a9ac7f887d1e378e47e945a93d9c39e8d6aeca24f1`.

## RL-005

Redline number: RL-005
Findings or source items: A24 (CR-10 APPROVED, alternative (a); drainage: §8.3, where the mutual-exclusion rule is enforced); A25 (CR-10 drainage: the key set gaining crd_id); A26 (CR-10 drainage, unperformed)
Change type: CLARIFY
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.3 Machine Evidence Index — JSONL mirror (records-only) \[Required-Now\]**` > `### **Bundle-aware extension (evidence bundles, manifests, and change-container metadata)**` > `#### **Allowed top-level keys and unknown-key rejection**`
Original-bound location: §8.3 "Allowed top-level keys and unknown-key rejection", the paragraph beginning "Before the first affected CRD enters QA"
Original lines (context only): 2318
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-10 (2.24, approved alternative (a)) finds that the paragraph asks every validator to enforce the epic_id/crd_id mutual exclusion, while a row with both keys cannot reach the Mirror skeleton test or the QA harness: the sole writer refuses it and check_mirror_schema.sh rejects it with EPIC_CRD_EXCLUSIVE. The rule stays enforced by those two; the two validators accept crd_id only, as a stated limit. 2.24, 2.25 and 2.26 name §8.3 as the drainage target. The four surfaces were confirmed read-only on main 0838ba0c. crd_id is already in the allowed key list, so only the enforcement sentence changes.

OLD

````text
Before the first affected CRD enters QA, the Machine Mirror schema and every serializer or validator enforcing this allowed-key set MUST accept crd\_id, enforce the epic\_id/crd\_id mutual-exclusion rule, and preserve valid historical and active epic\_id records.
````

OLD literal: 263 bytes; SHA-256 `2796b25885bcc8bfdfaad98348fdbace59924f54ba8875cb0b0d278c6c234ad7`.

NEW

````text
Before the first affected CRD enters QA, the Machine Mirror schema and every serializer or validator enforcing this allowed-key set MUST accept crd\_id and preserve valid historical and active epic\_id records. The epic\_id/crd\_id mutual-exclusion rule is enforced where records are written and where the Machine Mirror is schema-checked: the canonical updater, `tools/evidence/update_evidence_index.py`, refuses an entry that carries both keys, and the Machine Mirror schema check, `ci/checks/check_mirror_schema.sh`, rejects such a record with `EPIC_CRD_EXCLUSIVE`. A validator that reads only records those two have admitted, such as the Mirror skeleton test `tests/evidence/test_evidence_skeleton.py` and the evidence-graph validation of the QA harness `tools/qa/qa_harness.py`, accepts crd\_id without repeating the mutual-exclusion check. A record carrying both keys is not a real input for such a validator; that is a stated limit, not a defect.
````

NEW literal: 953 bytes; SHA-256 `81af8e0417481fc12666916c8f0c5b35336a71038d13f9392b86963b6281dbfa`.

## RL-006

Redline number: RL-006
Findings or source items: A07 (CR-7, AD-1; doc-delta candidate: §8.8, public_aux); A08 (required drainage for CR-7 into §8.8); X04 (plan v2.0 §18, §8.8 row)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.8 Reader JSON Success Endpoint Catalog snapshot (records-only)**` > `### **Authoritative Endpoint Catalog file (records-only; names-only fields)**`
Original-bound location: §8.8 "Authoritative Endpoint Catalog file", "Minimum required fields", the classification and env_gate bullets
Original lines (context only): 4708–4709
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-7 (2.7 AD-1, approved alternative (a)) names §8.8 and public_aux among the doc-delta candidates, and 2.8 makes CR-7's §8.8 drainage required. HDE-CLI-API-Vendor-Ref §5.6, read as supporting reading, requires PF12 to register public_aux and the public env_gate sentinel for the Aux record. On main 0838ba0c the Catalog carries one public_aux record with env_gate not_applicable_public, and the validator accepts public_aux (its comment records that PF12 had not yet registered it) and refuses the public sentinel on an internal record. The two adjacent bullets are replaced together so that no two edits touch.

OLD

````text
* `classification`: One of public\_reader, public\_compat, internal\_identity, internal\_admin, ops, dev\_harness.  
* `env_gate`: For non-public endpoints, either a string expression (example: `APP_ENV!=prod`) or an object mapping env var names to required values (example: `{"APP_ENV":"dev"}`). The approved public Reader record uses the literal string `not_applicable_public`; this sentinel describes its public posture and does not unlock a non-public route.  
````

OLD literal: 464 bytes; SHA-256 `b12b0ca15a015b2193cca03e6e447bbb711f8e0e4f6e14687cfce48f427de031`.

NEW

````text
* `classification`: One of public\_reader, public\_compat, public\_aux, internal\_identity, internal\_admin, ops, dev\_harness.  
* `env_gate`: For non-public endpoints, either a string expression (example: `APP_ENV!=prod`) or an object mapping env var names to required values (example: `{"APP_ENV":"dev"}`). The approved public records, the production Reader record and the Aux narrative record, use the literal string `not_applicable_public`; this sentinel describes their public posture, MUST NOT appear on an internal record, and does not unlock a non-public route.  
````

NEW literal: 572 bytes; SHA-256 `ec5e05e38046543994d6100fdba6f6599784b8546ca73add671a8110cf40aa97`.

## RL-007

Redline number: RL-007
Findings or source items: A07 (CR-7, AD-1 class (b); doc-delta candidate: §8.8, aliases); A08 (required drainage for CR-7 into §8.8; F1 aliases on the Aux record); X04 (§8.8 row)
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.8 Reader JSON Success Endpoint Catalog snapshot (records-only)**` > `### **Authoritative Endpoint Catalog file (records-only; names-only fields)**`
Original-bound location: §8.8, after "Additional key for writer surfaces (conditional)." and its route_id bullet, before "Minimum schema (records-only):"
Original lines (context only): 4716
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: AD-1 class (b) accounts for an alias spelling through the canonical record's aliases; 2.8 records the review finding that moved aliases onto the Aux record. HDE-CLI-API-Vendor-Ref §5.6 requires PF12 to register the optional aliases mechanism and its validation, and defines aliases as reachable spellings of the same contract, without query selectors, to be omitted when the mount does not expose them. The validator on main 0838ba0c refuses an empty, duplicated, query-bearing or self-equal alias and any duplicate (method, path) across paths and aliases.

OLD

````text
* `route_id`: Stable route identifier string (names-only). Required for endpoint catalog entries referenced by writer-envelope idempotence behavior (example: dev.writer.conjunction.v1).
````

OLD literal: 185 bytes; SHA-256 `e40e3d48f6dfc7df34ea86251758be62d438430f8f1cd866396dd05b487e9c43`.

NEW

````text
* `route_id`: Stable route identifier string (names-only). Required for endpoint catalog entries referenced by writer-envelope idempotence behavior (example: dev.writer.conjunction.v1).

Optional key for alias spellings (conditional).

* `aliases`: A non-empty array of unique path strings on a canonical record. Each alias begins with `/`, carries no query string, differs from the record's `path`, and is a reachable spelling of the same contract under the same method, not an independent surface. A record carries `aliases` only where its owning transport contract in HDE-CLI-API-Vendor-Ref defines an alias spelling, and omits an alias that the configured mount does not expose. No `(method, path)` pair may occur twice in the Catalog, whether as a record's `path` or as one of its aliases.
````

NEW literal: 794 bytes; SHA-256 `8126bc33e4669b8c683bd3f6226de37a240a54d7b7154ce23af666c25f1e99b0`.

## RL-008

Redline number: RL-008
Findings or source items: A07 (CR-7 APPROVED, alternative (a); AD-1 accounting rule, exclusion classes (a) to (d), canon-retired refusal; AD-6 enumeration test); A08 (required drainage for CR-7 into §8.8); X04 (§8.8 row)
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.8 Reader JSON Success Endpoint Catalog snapshot (records-only)**` > `### **Authoritative Endpoint Catalog file (records-only; names-only fields)**`
Original-bound location: §8.8, after the "Minimum schema (records-only):" bullet and before the "### **Indexing**" heading
Original lines (context only): 4720
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: AD-1 sets the accounting rule (every served (method, path) accounted for once, by one record or one exclusion class with its basis), the four exclusion classes, the canon-retired set from HDE Architecture §3.5 and HDE Users Guide §1.1, and the fail-closed refusal of a canon-retired record; AD-6 makes the enumeration test record every excluded pair's class and basis and fail CI on an unaccounted pair or a retired record. CR-7 reads S15 under canon precedence: route removal stays with its canon owner. HDE-CLI-API-Vendor-Ref §5.6 asks PF12 to register the Aux record. The factory set, the exclusion bases, the stale-exclusion and unmounted-record failures, and the validator's rules were confirmed in tests/http/test_endpoint_catalog.py and tools/evidence/generate_a7_transport_proofs.py on main 0838ba0c. No served-pair count is stated, because the count is a repository fact that changes with routes.

OLD

````text
* {"generated\_at\_utc":"YYYY-MM-DDThh:mm:ssZ","endpoints":\[{"path":"\\","method":"\\","internal":true,"classification":"\\","env\_gate":"\\","a7\_eligible":false,"blueprint\_module":"\\","rails\_profile":"\\"}\]}
````

OLD literal: 214 bytes; SHA-256 `1d08fefd49d8e9466c20a4a66a5c9769d48dafd21fbc01ac8dd7fa6f202b245f`.

NEW

````text
* {"generated\_at\_utc":"YYYY-MM-DDThh:mm:ssZ","endpoints":\[{"path":"\\","method":"\\","internal":true,"classification":"\\","env\_gate":"\\","a7\_eligible":false,"blueprint\_module":"\\","rails\_profile":"\\"}\]}

Aux narrative record (normative).

The public Aux narrative surface is one canonical per-method record: `GET /aux/narrative` with `classification: public_aux`, `internal: false`, `env_gate: not_applicable_public`, and `a7_eligible: false`. While the configured mount exposes the `/api` spelling, the record carries `aliases: ["/api/aux/narrative"]`. Aux is not an A7 JSON-success surface, and its transport facts remain owned by HDE-CLI-API-Vendor-Ref.

Catalog population (normative).

* Every `(method, path)` pair that the application factories serve is accounted for exactly once: by one Catalog record, or by one exclusion class with its recorded canon basis. The application factories are `adapter/factory.py`, `adapter/http_reader.py::create_app`, and `adapter/wsgi.py`.  
* The exclusion classes are: (a) governed refusal of a catalogued record; (b) alias spelling of a canonical record, carried by that record's `aliases`; (c) framework-implicit method, a method the web framework adds automatically, such as `HEAD` for a `GET` view or `OPTIONS`, whose behavior neither HDE-CLI-API-Vendor-Ref nor the route's own view defines; and (d) canon-retired route.  
* A canon-retired route is one that HDE Architecture and HDE Users Guide mark `RETIRED/NONCANONICAL` and exclude from the Endpoint Catalog: `/ops/db/unavailable`, `/ops/probe/env`, and `/ops/writer/diagnostic`, in every method that a factory serves for it. A record whose `path` or alias is canon-retired is invalid, and the Catalog validator MUST refuse it, fail-closed. Removing a canon-retired route stays with its canon owner; Catalog population adds, removes, and changes no route.  
* A record for a route that no application factory serves is invalid.  
* The route-enumeration test records the class and canon basis of every excluded pair. A served pair with neither a record nor a recorded exclusion, an exclusion for a pair that is no longer served, or a record for a canon-retired path fails continuous integration.  
* Current implementation: `tools/evidence/generate_a7_transport_proofs.py` produces the Catalog, and its `validate_catalog` applies the record, alias, Aux, canon-retired, and success-designation rules of this section; `tests/http/test_endpoint_catalog.py` is the route-enumeration test.
````

NEW literal: 2498 bytes; SHA-256 `a86f2b3573f2c494d8660072db2082a60598429880c5aa019df06430d63f3c66`.

## RL-009

Redline number: RL-009
Findings or source items: S-CR3 (Specification CR-3, APPROVED_AS_CHANGED; §8.17 added by review v1.0 §6); CD-2
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.17 Live QA evidence layout (audit/qa/\\/) \[Required-Now\]**`
Original-bound location: §8.17 "Change-container identity (normative)." second bullet
Original lines (context only): 5273
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-3 names §8.17 "Change-container identity" (added by Specification review v1.0 §6, the "as changed" part of APPROVED_AS_CHANGED) as the second passage that points to a PF30 record that will not exist. The same reasoning and wording as RL-001 apply; the directory-form rule and the QA root are unchanged.

OLD

````text
* For a CRD, `<change-id>` is the stable CRD ID recorded in PF30 using the lower-case ASCII, hyphenated directory form required by PF12; its governed QA root is `audit/qa/<change-id>/`.  
````

OLD literal: 187 bytes; SHA-256 `5f2697d0b1d302c854ddeffcfac4ec11d738db89ed0d7d798a51bcb9548d4ec8`.

NEW

````text
* For a CRD, `<change-id>` is its controlled CRD ID, which the Product Owner assigns at class selection and the change's approved CRD Specification records, in the lower-case ASCII, hyphenated directory form required by PF12; its governed QA root is `audit/qa/<change-id>/`. The identity does not depend on an HDE CRD Records entry.  
````

NEW literal: 334 bytes; SHA-256 `f5691ba9ce2bcb28240b8cea440e3703e50b6a160833a7b61764bc7a9c8f4736`.

## RL-010

Redline number: RL-010
Findings or source items: A15 ("The close-run evidence family (introduced)": path, holdings, status, writer, membership, scoped exception, no Epic family); X03 (ADR canon table row for §8.17 "New standardized evidence families" and "Current-state evidence"; Decision 7)
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.17 Live QA evidence layout (audit/qa/\\/) \[Required-Now\]**`
Original-bound location: §8.17 "Current-state evidence (normative).", after its closing paragraph and before "### **8.17.1 Root and step directories**"
Original lines (context only): 5362
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.15 introduces the close-run family through HDE Build Notes, as §8.17 "New standardized evidence families" requires, and states its path, holdings, PF27 v2 header, PASS/FAIL/BLOCKED posture under Glow QA Guide "Close-pack truthfulness and same-run execution", post-verdict status, sole writer and transaction, whole-family replacement, the recorded-QA-family precondition, closed membership, and a scoped exception, for close/ only, to the no-enumeration rule, which keeps governing checks/. The ADR canon table asks §8.17 "New standardized evidence families" and "Current-state evidence" to record this. The admission table, key prefix and close-run key form, the membership checks, and the entrypoint were confirmed read-only in tools/evidence/update_evidence_index.py on main 0838ba0c; the header schema name is Plan Templates' pf27.step_log_header.v2.

OLD

````text
Tools MUST NOT infer run state by enumerating subdirectories under audit/qa/\\/. The manifest is the authoritative index of current-state step evidence.
````

OLD literal: 152 bytes; SHA-256 `890aa564a6c44f9d9a53ee3b373026818b8fc975eb3dbac8a716002f0fde4dc3`.

NEW

````text
Tools MUST NOT infer run state by enumerating subdirectories under audit/qa/\\/. The manifest is the authoritative index of current-state step evidence.

Close-run family exception (normative; admitted CRDs only).

* A CRD admitted in the canonical updater's source-owned CRD admission table, `ADMITTED_CRD_QA` in `tools/evidence/update_evidence_index.py`, has a post-verdict close-run family at `audit/qa/<change-id>/close/<check_id>/primary.log`, each primary with its sibling `primary.log.path_proof.txt`. Each row of that table maps a CRD ID to its QA root and Index key prefix; another CRD needs its own row.  
* The family holds the same-run mechanical evidence of the change's close workflow: one primary per close-run check, rendered from that check's captured command, exit code, and output with a `pf27.step_log_header.v2` header as Plan Templates defines it. Its posture is `PASS`, `FAIL`, or `BLOCKED`, as Glow QA Guide "Close-pack truthfulness and same-run execution" requires.  
* The family is written after the final QA verdict. It neither reopens nor adds to the change's approved `qa_step_logs_manifest.json` or any `checks/` primary, and that manifest never lists it.  
* Only the canonical updater writes the family, through its close-run publication entrypoint `publish_crd_close_run_family`, inside one recoverable write transaction. The given results replace the whole family. The entrypoint requires the change's recorded QA family to exist.  
* The family's members are its validated primaries and their path proofs under `close/`, in a closed shape: each member is a directory, not a symlink, named by a valid lower-case check ID, and it holds only `primary.log` and `primary.log.path_proof.txt`. Anything else under `close/`, an aliased `close/` root, or a `close/` root without a primary is refused.  
* This is a scoped exception, for `close/` only, to the rule above that tools MUST NOT infer run state by enumerating subdirectories: the canonical updater discovers the family's members by enumerating `close/`. That rule continues to govern `checks/` and every other part of a QA root, where `qa_step_logs_manifest.json` stays the authoritative index.  
* Each primary has one Human Evidence Index row and one Machine Evidence Mirror record with artifact key `<key_prefix>.close.<check_id>.primary.log`, where `<key_prefix>` is the CRD's Index key prefix in the admission table, and Mirror role `log`. HDE Build Notes introduced this family under the rule for new standardized evidence families above.  
* No Epic close-run family is admitted. An Epic close run needs its own explicit admission later, as each CRD needs its admission row.
````

NEW literal: 2669 bytes; SHA-256 `5eefa1d9a8e5c87719013fdf2d9aa63ff07df86ddbd99a7834950c6a09add6dd`.

## RL-011

Redline number: RL-011
Findings or source items: A15 (close-run family at audit/qa/<change-dir>/close/); X03 (ADR canon table row for §8.17.1)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.17 Live QA evidence layout (audit/qa/\\/) \[Required-Now\]**` > `### **8.17.1 Root and step directories**`
Original-bound location: §8.17.1 "EPIC_QA_ROOT MAY contain:" list, after the checks/ bullet
Original lines (context only): 5377
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: The ADR canon table names §8.17.1 for the close-run family. The EPIC_QA_ROOT contents list gains close/, limited to admitted CRDs and written only by the canonical updater; the checks/ bullet is reproduced unchanged.

OLD

````text
* checks/ — current-state per-check directories (one directory per check\_id). Each check directory contains primary.log and MAY contain auxiliary tmp\_\* supporting files or plan-owned outputs.  
````

OLD literal: 198 bytes; SHA-256 `465743ebb960c51ca1405111d5c8094a4104f534969b565b698d17e864367845`.

NEW

````text
* checks/ — current-state per-check directories (one directory per check\_id). Each check directory contains primary.log and MAY contain auxiliary tmp\_\* supporting files or plan-owned outputs.  
* close/ — for a CRD in the canonical updater's CRD admission table only, the post-verdict close-run family; written only by the canonical updater, never plan-owned (§8.17 "Close-run family exception").  
````

NEW literal: 406 bytes; SHA-256 `f6fe42dfc7efbb5385f859aa70a860e16414c206ab14f95e3e0d1479b86a6775`.

## RL-012

Redline number: RL-012
Findings or source items: A15 (close-run family membership: directories named by check ID); X03 (ADR canon table row for §8.17.1)
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.17 Live QA evidence layout (audit/qa/\\/) \[Required-Now\]**` > `### **8.17.1 Root and step directories**`
Original-bound location: §8.17.1 "Directory name rules." first two bullets
Original lines (context only): 5395–5396
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: §8.17.1's directory rules list every structural child directory and name per-check directories. close/ is a structural child of an admitted CRD's QA root, and its members are directories named by check IDs, which the harness's validate_check_id requires to be lower-case ASCII safe path segments (confirmed on main 0838ba0c). The two adjacent bullets are replaced together.

OLD

````text
* The `EPIC_QA_ROOT` directory name and all structural child directories, including `00_meta/`, `checks/`, `results/`, `snapshots/`, `closeout/`, and `remediation/`, MUST use lower-case ASCII.  
* Per-check directories under checks/ MUST be named by the check\_id slug used for manifest keying, and that slug MUST be lower-case ASCII.  
````

OLD literal: 336 bytes; SHA-256 `77bc4f3f409ebad9076a793adfac0f12c4082e22e2405abc029fa019480cd8a9`.

NEW

````text
* The `EPIC_QA_ROOT` directory name and all structural child directories, including `00_meta/`, `checks/`, `close/`, `results/`, `snapshots/`, `closeout/`, and `remediation/`, MUST use lower-case ASCII.  
* Per-check directories under checks/, and close-run member directories under close/, MUST be named by the check\_id slug used for manifest keying or close-run publication, and that slug MUST be lower-case ASCII.  
````

NEW literal: 419 bytes; SHA-256 `216c3987e59ee0d90348e35de48fe8e3a6fa02b4c1eee57e76cf9ebde81985e7`.

## RL-013

Redline number: RL-013
Findings or source items: TW-DRAIN-10 change-history rule; PF12 §9.1 (a Doc-Delta is required for a change to governed evidence or parity rules) and §9.2 template, in the established form of §9.5
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF12-Canon-HDE-Schemas-and-Artifacts`
Section path: `# **9\) Change Log & Doc-Delta Hooks \[Required-Now\]**` > `## **9.5 Documentary drainage record — 2026-10-09**`
Original-bound location: end of §9.5 "Documentary drainage record — 2026-10-09" (its closing yaml fence), before "# **Appendix A: UMS Schemas**"
Original lines (context only): 5994–5995
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: §9.1 requires a Doc-Delta when a change alters governed evidence or parity rules, and §9.5 records the earlier documentary drainage in that form, so this change gets its own entry in the same form. Per TW-DRAIN-10 it names the version TW-APPLY-10 will derive (v2.9.6 bumped once by the established patch scheme, v2.9.7) and the preparation date 2026-10-26. It cites HDE Build Notes by title only and states no Apply outcome in advance. The release_id it records is the static SHA-256 of catalog/manifest.json at 9dda63dd, unchanged at 0838ba0c; it states that §5.3 is not refreshed. The new heading has no outer bold, as Technical Writing Best Practices §8 requires.

OLD

````text
    preservation obligations retain their original standing.
```
````

OLD literal: 64 bytes; SHA-256 `deb71c1f1b16b6eb6d42efacffa13cdcd65d4461f1b4b5aa978aa69363f4b8ba`.

NEW

````text
    preservation obligations retain their original standing.
```

## 9.6 Documentary drainage record — 2026-10-26

This record drains the closed HDE-CRD-0002 decisions on close-pack canon, CRD identity, Machine Mirror change-container metadata, and Endpoint Catalog population into PF12. It changes PF text only. HDE-CRD-0002's closure decision permits the documentary drainage; neither that decision nor this record establishes a QA verdict, acceptance, Ops, deployment, or register movement. §5.3 "Current repository posture" is not refreshed by this record.

```yaml
doc_delta:
  id: "DOCDELTA-20261026-pf12-hde-crd-0002-drain"
  date: "2026-10-26"
  author: "Claude Code — T-PF12 document worker"
  document_version: "v2.9.7"
  scope:
    catalogs: "false"
    schemas: "true"
    manifest_checksums: "false"
    validation: "true"
    evidence_index: "true"
    routing_only: "false"
    operation_boundary: "documented contracts and status only; no governed payload writes"
  targets:
    catalogs_changed: []
    schemas_changed: []
    other_artifacts_changed: []
    documented_contracts:
      - title: "Close candidate source v1 schema"
        path: "schemas/epic_close_candidate_source.v1.json"
      - title: "Close candidate source v2 schema"
        path: "schemas/close_candidate_source.v2.json"
      - title: "Generic close-pack writer"
        path: "tools/qa/generate_epic_close_pack.py"
      - title: "Evidence Index updater"
        path: "tools/evidence/update_evidence_index.py"
      - title: "Machine Mirror schema check"
        path: "ci/checks/check_mirror_schema.sh"
      - title: "QA harness"
        path: "tools/qa/qa_harness.py"
      - title: "Mirror skeleton test"
        path: "tests/evidence/test_evidence_skeleton.py"
      - title: "Endpoint Catalog"
        path: "docs/ENDPOINTS_CATALOG.json"
      - title: "Endpoint Catalog producer and validator"
        path: "tools/evidence/generate_a7_transport_proofs.py"
      - title: "Route-enumeration test"
        path: "tests/http/test_endpoint_catalog.py"
      - title: "CRD close-run family"
        path: "audit/qa/<change-id>/close/<check_id>/primary.log"
  summary: |
    Record the generic close-pack writer and its close_candidate_source.v2
    schema for Epic and CRD identities, the CRD close-pack paths and Index
    rows, the v2 manifest key_outputs minimum, the closed Epic-only identity
    inventory, and the post-verdict CRD close-run family with its close/-only
    membership exception. Reword the CRD identity passages so that they no
    longer depend on an HDE CRD Records entry. State where the epic_id/crd_id
    mutual-exclusion rule is enforced. Register the Endpoint Catalog
    population rule with its four exclusion classes, the canon-retired
    exclusion, the public_aux classification, the aliases mechanism, and the
    Aux narrative record.
  domain_impact:
    current_domains_changed: []
    future_promotions: []
    documented_closed_set_additions: ["Endpoint Catalog classification public_aux"]
    mathematical_or_public_numeric_change: "none"
  release_identity:
    frozen_input_changed: "false"
    manifest_changed: "false"
    release_id_expected_change: "false"
    prior_release_id: "77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e"
    computed_release_id: "77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e"
    disposition: "prior release_id remains valid; static SHA-256 of the unchanged catalog/manifest.json bytes at the source baseline commit"
  acceptance_impact:
    tokens_added: []
    tokens_removed: []
    tokens_unchanged: []
    decision_boundary: "no new QA, OPS, acceptance, deployment, register movement, or closure claim"
  validation:
    - behavior: "CRD close-pack rows, close-run family, CRD admission, and crd_id handling as documented"
      entrypoint: "python tools/evidence/update_evidence_index.py --check"
      result: "not-run by this documentary revision; implementation statically inspected"
      evidence_path: "tools/evidence/update_evidence_index.py"
    - behavior: "epic_id/crd_id mutual exclusion in the Machine Evidence Mirror"
      entrypoint: "ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl"
      result: "not-run by this documentary revision; implementation statically inspected"
      evidence_path: "ci/checks/check_mirror_schema.sh"
    - behavior: "v2 candidate-source schema, writer model selection, and key_outputs minimum"
      entrypoint: "python tools/qa/generate_epic_close_pack.py --source <candidate-source> --check"
      result: "not-run by this documentary revision; schema and writer statically inspected"
      evidence_path: "schemas/close_candidate_source.v2.json"
    - behavior: "Endpoint Catalog population, exclusion classes, aliases, Aux record, and canon-retired refusal"
      entrypoint: "python -m pytest tests/http/test_endpoint_catalog.py"
      result: "not-run by this documentary revision; validator and test statically inspected"
      evidence_path: "tests/http/test_endpoint_catalog.py"
    - behavior: "complete exact original-bound PF redline preparation and application"
      entrypoint: "TW-DRAIN-10 then TW-APPLY-10, both 100926.1"
      result: "recorded in the evidence path; this record states no outcome in advance"
      evidence_path: "docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf12/PF12-from-v2.9.6.proof-log.md"
  evidence_updates: []
  index_and_mirror:
    human_index: "docs/evidence/INDEX.json"
    human_index_sentinel: "docs/evidence/INDEX.sha256"
    machine_mirror: "artifacts/evidence_index.jsonl"
    machine_mirror_checksum: "artifacts/evidence_index.jsonl.sha256"
    parity_status: "not-run; no governed evidence bytes, paths, records, sidecars, sentinels, or companions changed"
    required_updates: "none for this PF-text-only drainage; original owner rules continue to govern future payload changes"
  routing_titles_only:
    math: "HDE-Math-Spec"
    governance: "HDE-Governance"
    cli_api_vendor: "HDE-CLI-API-Vendor-Ref"
    architecture: "HDE Architecture"
  open_decisions: []
  traceability:
    pull_request: "https://github.com/amthorn78/glow-hdengine-v2/pull/761"
    source_baseline_commit: "9dda63dd3f05f496c3ff67e95da78550d3950c5a"
    publication: "document output only; canonical source publication remains separately governed"
  change_log_entry: |
    v2.9.7 / 2026-10-26 — Documentary drainage of the closed HDE-CRD-0002
    decisions into the close-pack, Machine Evidence Mirror, Endpoint Catalog,
    and Live QA evidence layout homes above. Canonical runtime and evidence
    bytes remain unchanged; the prior release_id remains valid. Exact
    preparation and application evidence is retained in the document output
    proof logs.
```
````

NEW literal: 6780 bytes; SHA-256 `29091cfe2f7328bcd3c41dccc898d9a14b09d8517390a7ba794ee5e04413f842`.

END OF REDLINES
