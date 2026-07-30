# HDE-EPIC038 Epic Remediation Plan — Formal Close-Pack and Acceptance-Ledger Completion

**Plan type:** Epic Remediation Plan  
**Version:** r5  
**Revision note:** Gate A publication revalidation  
**Status:** Gate A complete; Gates B–D and every scope, rails, or authorization stop govern execution
**Epic:** HDE-EPIC038
**Repository:** `amthorn78/glow-hdengine-v2`
**Repository baseline:** `main@25953d713f398dedb9d5587218c4bb3f02ecac36`
**Plan date:** 072926  
**Trigger:** Closure-evidence review found required formal close-pack and acceptance-ledger artifacts absent after implementation and Live QA completion.  
**Product Owner decisions already received:** Mint `RELEASE_ID_RECOMPUTE_OK`; publish HDE Build Notes Addenda 2.37 and 2.38.
**Product Owner decision requested:** Full-plan approval for the bounded DEV remediation lineage, subject to Gates B–D and every separately stated authorization stop.
**Execution model:** One bounded closed-rails DEV remediation lineage. DEV-01 constructs the standalone token/evidence matrix; the independent Gate B owner must record `PASS` before DEV-02. DEV-03 establishes the governed evidence fixed point through the canonical updater, orientation producer, and second canonical-updater write. After Gate D records `PASS` and the Lead Developer approves the pull request, the Product Owner alone squash-merges the same bounded remediation pull request under normal branch protection. No token is claimed by approval, matrix construction, or Gate B review, and merge is not Product Owner closeout, acceptance, PF09 or board movement, or epic closure. Any proposed change to the approved scope, rails, or authorization stops this lineage and requires plan or authority revision before execution resumes. No OPS or Live QA is planned. Any later external action, runtime-behavior correction, or affected Live QA revalidation requires its own explicit authorization and routing before this lineage resumes.
**Required terminal outcome:** HDE-EPIC038 close report `SATISFIED`, corrected roster fully PASS, and every formal close gate complete.

## 1. Executive decision

HDE Build Notes Addenda 2.37 and 2.38 are published and Gate A has passed. The published token-roster correction remains necessary but insufficient to close HDE-EPIC038.

The active addendum resolves the registry conflict by:

* minting `RELEASE_ID_RECOMPUTE_OK`;
* removing `DEV_DB_BRIDGE_FALLBACK_OK` from current claimability; and
* preserving every other registry-valid token in the approved roster.

It did not create the missing acceptance map, token/evidence matrix, viability log, close report, close manifest, or their required path proofs. Direct inspection at the current repository baseline confirms that those artifacts remain absent. A bounded remediation plan is therefore still necessary.

This plan does not reopen the implementation, OPS, or 24-check Live QA result without a concrete failing predicate. It completes the formal evidence package and eliminates every evidence-based blocker required to reach a truthful passing state.

`NOT SATISFIED` is the required truthful close-report decision whenever any corrected-roster token lacks sufficient current evidence. It does not complete this remediation; the report must list the minimum follow-up, remain governed, and may be superseded only after the recorded evidence change supports `SATISFIED`.

Published PF10 Addendum 2.38 resolves the PF04/PF06 checkpoint conflict for this plan: the exact 33-token roster and matrix pointer are sufficient for full-plan approval, while DEV-01 must complete the standalone matrix and pass Gate B before DEV-02. No token result follows from plan approval or matrix construction.

## 2. Authority and source posture

| Source | Controlling use in this plan |
|---|---|
| HDE Build Notes, Addendum 2.12 | Direct PostgreSQL is the sole active transport; bridge fallback and new bridge-token claims are retired. |
| HDE Build Notes, Addendum 2.25 | Recognizes this bounded Epic Remediation Plan type pending permanent template drainage. |
| HDE Build Notes, Addendum 2.36 | Records QA `READY WITH CAVEATS`; does not claim formal close-pack completion, token satisfaction, acceptance, or closure. |
| HDE Build Notes v12.5.7 lettered set, Addendum 2.37 | Active authority that mints `RELEASE_ID_RECOMPUTE_OK`, removes current `DEV_DB_BRIDGE_FALLBACK_OK` claimability, and supplies the corrected 33-token HDE-EPIC038 roster. |
| HDE Build Notes, Addendum 2.38 | Resolves the PF04/PF06 matrix-checkpoint conflict for this bounded remediation plan: full-plan approval may precede matrix construction, while Gate B blocks DEV-02, token claims, and closeout until matrix completeness is independently verified. |
| HDE Governance, acceptance-token registry | Controls all token names and permanent semantics except the exact temporary admission supplied by Addendum 2.37 pending drainage. |
| Epic Process Guide, §§0.5.1, 1.1.9.3–1.1.9.5, and 3.5.2 | Controls canonical close-pack paths, token/evidence wiring, final PASS roster, close-manifest bindings, and binary closure decision. |
| Canon Plan Templates | Consulted for plan and close-pack posture. It contains no dedicated Epic Remediation Plan template; Addendum 2.25 controls that format gap. |
| Current PF10 HDE-EPIC038 addenda, PF06 §3.5.2, PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, and current repository state | Supply current close-pack obligations, HDE-EPIC038 task/status posture, and proof of absent outputs; earlier plans are context only and are not authority for this plan. |
| Current repository state | Controls path existence, current evidence, source, tests, validation reality, and PR state. Gate A publication is verified at `main@25953d713f398dedb9d5587218c4bb3f02ecac36`. |

No older HDE Build Notes base version is used.

## 3. Remediation trigger and verified current state

### 3.1 Missing required outputs

The following exact paths were checked at the repository baseline and were not found:

| Required path | Required role | Current state |
|---|---|---|
| `audit/EPIC-038_close_report.md` | Canonical close report and binary decision | Absent |
| `audit/EPIC-038_close_report.md.path_proof.txt` | Close-report sibling proof | Absent |
| `audit/EPIC-038_MANIFEST.json` | Canonical close manifest | Absent |
| `audit/EPIC-038_MANIFEST.json.path_proof.txt` | Close-manifest sibling proof | Absent |
| `docs/acceptance_map_epic038.json` | Approved acceptance map | Absent |
| `docs/acceptance_map_epic038.json.path_proof.txt` | Acceptance-map sibling proof | Absent |
| `audit/qa/hde-epic038/token_evidence_matrix.md` | Governed token/evidence matrix | Absent |
| `audit/qa/hde-epic038/token_evidence_matrix.md.path_proof.txt` | Token-matrix sibling proof | Absent |
| `audit/qa/hde-epic038/acceptance_map_viability.log` | Meaningful viability result | Absent |
| `audit/qa/hde-epic038/acceptance_map_viability.log.path_proof.txt` | Viability-log sibling proof | Absent |

### 3.2 Existing evidence that must be reused, not rerun

The current repository contains the finalized 24-check QA family, including:

* `audit/qa/hde-epic038/qa_step_logs_manifest.json`
* `audit/qa/hde-epic038/qa_step_logs_manifest.json.path_proof.txt`
* `audit/qa/hde-epic038/00_meta/qa_rca_doc_delta_summary.md`
* `tools/evidence/check_hde_epic038_qa_current_state.py`
* `tests/evidence/test_hde_epic038_qa_current_state.py`

The manifest records all 24 approved check IDs as PASS. The QA RCA and Doc Delta summary records `READY FOR CLOSEOUT REVIEW` while expressly withholding formal close-pack and epic-closure claims.

The current release-identity evidence family also exists:

* `catalog/manifest.json`
* `artifacts/identity/release_id.json`
* `artifacts/identity/release_id_recompute.log`
* `tools/evidence/generate_identity_provenance.py`
* `tests/evidence/test_identity_provenance.py`

These are candidate bindings for `RELEASE_ID_RECOMPUTE_OK`; they do not become a PASS claim until the complete governed matrix and final close package validate the exact current evidence.

### 3.3 Failure classification

This is a closeout-packaging and governance failure.

It is not supported as:

* an implementation-behavior failure;
* a failed QA check;
* an OPS failure;
* a reason to repeat a live vendor request;
* a reason to repeat a database action;
* a reason to recreate historical bridge evidence; or
* a reason to perform a new Codespaces run.

### 3.4 Gate A publication verification

Gate A passed at `main@25953d713f398dedb9d5587218c4bb3f02ecac36`.

The publication commit:

* publishes the active HDE Build Notes v12.5.7 lettered set;
* carries Addendum 2.37 forward as active authority;
* adds Addendum 2.38 and its index entry; and
* changes no implementation, QA evidence, acceptance-ledger, close-pack, generator, test, CI-workflow, or governed-evidence path.

The commit therefore satisfies publication of Addenda 2.37 and 2.38 only. It does not satisfy any token, Gate B, Gate C, Gate D, or DEV task.

### 3.5 Post-Gate-A task revalidation

| Task | Revalidated status | Current-repository basis | Next permitted transition |
|---|---|---|---|
| DEV-01 | Required; first post-approval execution task | Gate A is complete; the corrected roster is active; the matrix and its proof remain absent; existing QA, identity, Index, Mirror, tests, and CI inputs exist | Begin after full-plan approval |
| DEV-02 | Required; sequenced after DEV-01 and Gate B | The planned closeout generator and focused test remain absent | DEV-01 completes and Gate B passes |
| DEV-R1 | Required conditional loop; not invoked | No remediation-ledger pair exists and no concrete post-Gate-A predicate failure has yet been produced | A matrix, preflight, focused test, validator, or exact-head CI predicate fails |
| DEV-03 | Required; sequenced after DEV-02 and Gate C | All ten adopted close-pack and acceptance-ledger paths remain absent; existing fixed-point commands and entrypoints resolve | DEV-02 completes, Gate C passes, and any invoked DEV-R1 entries are closed |
| DEV-04 | Required; sequenced after DEV-03 | No open pull request exists in the repository; no closeout remediation PR has been created | DEV-03 establishes Gate D readiness |

No task is removed or treated as passed merely because Gate A passed.

## 4. Objective

Create one deterministic, reviewable closeout package that:

1. uses the corrected, registry-valid 33-token roster;
2. binds every token to complete, exact, non-placeholder evidence wiring;
3. creates the adopted acceptance map, token/evidence matrix, and meaningful viability log;
4. creates the canonical close report and close manifest at their exact paths;
5. delegates all sibling proof, Human Evidence Index, hash-sentinel, and Machine Mirror writes to the canonical evidence updater;
6. identifies all reused proof families explicitly;
7. states the full approved PF09 scope separately from token claims;
8. maps all tracked issues and decision records;
9. clears every evidence-based blocker through the bounded corrective loop;
10. produces a canonical `SATISFIED` decision from evidence rather than plan intent; and
11. permits Product Owner closeout review without performing that review or moving any status.

## 5. Scope

### 5.1 In scope

* Read-only inventory of the corrected token roster and current governed evidence.
* A complete token/evidence matrix with one unique row per token.
* Deterministic closeout-generation and read-only validation tooling under the existing evidence-tooling home.
* Focused unit and negative tests for the new tooling.
* The ten exact required close-pack and acceptance-ledger paths listed in §3.1.
* A governed remediation ledger and sibling path proof recording every discovered closeout blocker and its resolution.
* Coherent refresh of the existing Human Evidence Index, hash sentinel, Machine Mirror, mirror checksum, and required sibling path proofs through the canonical updater.
* The smallest evidence-producer, validator, test, CI, or governed-artifact correction required by a reproducible failing predicate when that correction does not alter application or runtime behavior.
* A closed-rails pull request carrying the complete remediation delta and exact-head CI validation.

### 5.2 Out of scope

* Feature work, scope expansion, new routes, new payloads, new public contracts, or behavior beyond the already-approved HDE-EPIC038 predicates.
* Application, adapter, engine, database, BodyGraph, route, serializer, payload, or other runtime-behavior changes. A reproducible behavior defect must be routed through a separately authorized implementation-remediation lane, followed by revalidation of every affected QA proof before this closeout lineage resumes.
* New acceptance-token names beyond the Product Owner-approved `RELEASE_ID_RECOMPUTE_OK`.
* Any current or replacement bridge token.
* Planned QA execution, QA reruns, QA-result edits, new QA verdicts, or mutation of prior primary logs. If separately authorized runtime remediation makes any retained QA proof stale, the affected QA work must be revalidated through its owning QA process before reuse.
* Planned OPS execution, credentials, external services, network calls, vendor calls, live database calls, migrations, deployments, or environment discovery. A proven external-only blocker may be routed only through separately authorized bounded OPS work.
* Rewriting historical bridge or remediation evidence.
* PF09 status movement or reopening completed PF09 work.
* Permanent PF-document edits or drainage.
* Development-board mutation.
* Product Owner acceptance or epic closure.

## 6. PF09 accountability

Formal close-pack and acceptance-ledger completion, including the epic-specific generator, focused test, CI enforcement, remediation ledger, and close-report and manifest creation, is an epic-close process obligation under PF06 §3.5 and is outside the HDE phased build checklist. The canonical-updater, Human Evidence Index, hash-sentinel, Machine Mirror, checksum, and path-proof work in DEV-01 through DEV-03 is in-epic work that advances PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, §`Subtask HDE-DIST005.2 — Global Index & Mirror discipline`; this mapping creates no token claim and moves no status in that phased document. No new task is created in that phased document.

The final close report and manifest must nevertheless state the full approved HDE-EPIC038 PF09 scope:

* `HDE-DIST005.1`
* `HDE-DIST005.2`
* `HDE-DIST006.1`
* `HDE-DIST006.2`
* `HDE-DIST006.3`
* `HDE-DIST002.4`
* `HDE-DIST002.5`
* `HDE-DIST003.1`
* `HDE-DIST003.4`
* `HDE-DIST001.1`
* `HDE-DIST001.2`
* `HDE-DIST001.3`
* `HDE-DIST001.4`
* `HDE-DIST001.5`
* `HDE-DIST001.9`
* `HDE-DIST001.10`
* `HDE-DIST001.11`
* `HDE-DIST001.6`
* `HDE-DIST007` with subtask `N/A`, as subsequently mapped by HDE Build Notes

The following remain excluded future scope and must not be imported:

* `HDE-DIST004.1`
* `HDE-DIST004.2`
* `HDE-DIST004.3`
* `HDE-DIST004.4`

Any later PF09 status drainage remains a separate documentation/status action.

## 7. Corrected token scope

The current HDE-EPIC038 acceptance roster contains exactly 33 tokens:

* `TESTS_PASS_OK`
* `DOC_DELTA_PRESENT_OK`
* `EVIDENCE_INDEX_UPDATED_OK`
* `MACHINE_MIRROR_UPDATED_OK`
* `EVIDENCE_INDEX_HASH_OK`
* `QA_PRECOMMIT_CHECKLIST_OK`
* `QA_POSTCOMMIT_CHECKLIST_OK`
* `ENV_RAILS_POLICY_OK`
* `PREIMAGE_RECOMPUTE_OK`
* `CLI_READER_PARITY_OK`
* `COMPOSITE_ABBA_IDENTITY_OK`
* `TWO_RUN_IDENTITY_OK`
* `JSON_CANONICAL_CHECK_OK`
* `A7_GET_QUOTED_ETAG_OK`
* `A7_HEAD_PARITY_OK`
* `A7_304_OMITS_CT_CL_OK`
* `A7_VARY_AUTH_AE_OK`
* `A7_ENCODING_INVARIANCE_OK`
* `A7_TRANSPORT_PROOF_OK`
* `ENDPOINTS_CATALOG_OK`
* `ENDPOINTS_CATALOG_ENV_GATE_OK`
* `ENV_LC_ALL_C_OK`
* `EVIDENCE_INDEX_MIRROR_OK`
* `EVIDENCE_PATHS_VALIDATED_OK`
* `DB_RUNTIME_SEARCH_PATH_OK`
* `DB_ROLE_OK`
* `DB_SCHEMA_FINGERPRINT_OK`
* `DB_CONN_ENV_OK`
* `EVIDENCE_PATH_PROOFS_OK`
* `CI_CHECK_MIRROR_SCHEMA_OK`
* `CI_CHECK_FINAL_LF_OK`
* `NO_EXTERNAL_IO_ON_REFUSAL_OK`
* `RELEASE_ID_RECOMPUTE_OK`

`DEV_DB_BRIDGE_FALLBACK_OK` is prohibited from the current matrix and every newly generated acceptance or closeout artifact.

The nine row-listed non-token proof obligations named by the approved Epic Plan remain non-token obligations. They must not be promoted into the roster.

Gate A is complete. After full-plan approval, DEV-01 constructs the matrix with no in-scope token claims. The plan begins consuming the roster for acceptance and close-pack generation only after Gate B confirms matrix completeness. This separation prevents matrix construction from being misread as token approval.

## 8. Approval and execution gates

### Gate A — Addendum publication

**Status:** `PASSED`

**Evidence:** HDE Build Notes Addenda 2.37 and 2.38 are published in the active v12.5.7 lettered set at `main@25953d713f398dedb9d5587218c4bb3f02ecac36`.

**Result:** Addendum 2.37 corrects the HDE-EPIC038 token roster, Addendum 2.38 resolves this plan’s matrix checkpoint, and neither publication establishes any token result or downstream gate.

### Gate B — Token/evidence matrix completion

**Entry condition:** The token/evidence matrix contains exactly one complete row for each of the 33 tokens.

Each row must contain:

* exact canonical token name;
* exact acceptance-map and manifest token name;
* unit or integration tests by exact existing path or exact approved planned path or stable identifier;
* exact existing closed-rails CI job name and, where new enforcement is planned inside that job, the exact planned step;
* applicable Live QA check IDs, or explicit `N/A` with a substantive reason;
* governed evidence artifact paths;
* Human Evidence Index and Machine Mirror artifact keys;
* epic identity;
* proof-anchor paths;
* current evidence posture without an acceptance claim;
* existing/reused-versus-planned-new evidence classification; and
* intended claim status and the exact execution evidence required to derive it, never inferred from naming or path presence.

No `TBD`, `e.g.`, `??`, wildcard-only path, omitted field, duplicate token, local synonym, retired token, or guessed artifact key is permitted.

**Approval posture:** Full-plan approval may precede matrix creation under published PF10 Addendum 2.38. Gate B is an execution checkpoint after DEV-01 and before DEV-02; it does not grant approval or establish any token result.

**Gate owner:** An independent technical reviewer who did not author the DEV-01 matrix.

**Gate record:** The reviewer records `PASS` or `FAIL` on the DEV-01 draft pull request against the exact PR head and matrix path, including 33-token set equality, row uniqueness, the no-placeholder result, and every blocking row. Full-plan approval authorizes this read-only review; only a recorded `PASS` permits DEV-02.

**Failure handling:** If any row cannot be completed without guessing, record the exact evidence gap, keep the token unclaimed, return to DEV-01, and repeat Gate B after correction. Do not remove an approved token, mark it PASS, invent replacement evidence, or proceed to DEV-02 until Gate B passes. Revise the plan or authority only if scope, rails, or authorization changes.

### Gate C — Pre-generation repository fixed point

**Entry condition:** Gate B has a recorded `PASS` on the DEV-01 draft pull request against the exact PR head and matrix path. After DEV-02, the finalized HDE-EPIC038 QA current-state checker, release-identity check, closeout preflight, focused tests, canonical updater check, canonical orientation-demo check, path validator, Index hash check, Mirror schema check, final-LF check, and `git diff --check` all pass at the remediation PR head. Every check or preflight mode is read-only.

**Failure handling:** Stop close-pack promotion and enter DEV-R1 for the actual failing owner. Do not modify historical QA logs or run external work to conceal the failure.

### Gate D — PF06 Stage B and final closeout decision

**Pre-generation entry condition:** The full proof-family roster is represented; every existing or reused prerequisite is current; every planned-new binding is exact and computable; every non-token prerequisite used by the close package is supported; the remediation ledger has no open entry; the planned tests and workflow checks exist; projected generation contains no blocker; and Gates B and C pass. Tokens whose decisive proof depends on DEV-03 outputs remain unclaimed until the post-generation acceptance condition passes.

**Post-generation acceptance condition:** Every required artifact exists at its canonical path; every planned test and exact-head workflow check has executed successfully; the final matrix matches repository reality; every proof, required-path, Human Evidence Index, Machine Mirror, and evidence-ledger binding is coherent; all 33 tokens remain PASS; and the close report and manifest both record the same `SATISFIED` decision.

**Decision rule:**

* if every governing pre-generation requirement passes, emit a candidate package whose close report and manifest state `SATISFIED`, then subject the entire candidate to the post-generation acceptance condition;
* if local post-generation checks pass, commit the candidate only to the existing draft remediation pull request so exact-head CI can evaluate it; the candidate remains provisional;
* if any local or exact-head post-generation requirement fails, do not mark the pull request ready, merge it, or otherwise publish the candidate as final; use the canonical generator to record the blocker in the remediation ledger, enter DEV-R1, and repeat preflight and generation after correction;
* if any corrected-roster token lacks sufficient current evidence when a close report is generated, keep that token non-PASS and emit a complete atomic `NOT SATISFIED` close report and manifest with the minimum follow-up; do not treat that truthful decision as remediation completion;
* never treat a generated file, waived validator, narrowed roster, or narrative assertion as a substitute for PASS evidence.

Artifact generation success alone is not closure. A truthful `NOT SATISFIED` package records current blockers but does not complete this remediation.

## 9. Planned repository outputs

### 9.1 New tooling and tests

The following are planned new repository paths, not claims of current existence:

* `tools/evidence/generate_hde_epic038_closeout.py`
* `tests/evidence/test_hde_epic038_closeout.py`
* `audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md`
* `audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md.path_proof.txt`

The existing `.github/workflows/ci.yml` must be updated in place. Its existing `test` job must strengthen the current HDE-EPIC038 current-state step with `--require-finalized`, then run the new closeout generator in `--check` mode and the focused closeout test after DEV-03 creates the governed outputs. No parallel updater, duplicate workflow, or invented job identity is authorized.

The current canonical updater registers `epic038.qa_step_logs_manifest` but none of the new closeout, manifest, acceptance-map, token-matrix, viability-log, or remediation-ledger families. DEV-01 and DEV-02 must extend `tools/evidence/update_evidence_index.py` for the new families and continue to use that single updater.

DEV-01 must first scaffold the planned generator path with deterministic `--token-matrix` and read-only `--check-token-matrix` modes. Those modes may write or check only the token/evidence matrix and must never emit a PASS claim. DEV-02 must extend the same generator and test paths with the remaining closeout behavior. No second matrix or closeout generator is authorized.

The completed generator must provide:

* write mode for deterministic generation;
* a read-only `--preflight` mode that reports blockers without creating canonical final close-pack artifacts;
* a read-only `--check` mode;
* stable ordering and canonical JSON where applicable;
* no timestamps or mutable facts unless an owning schema requires them and supplies a deterministic source;
* fail-closed validation;
* no network or external-system access; and
* no direct writing of governed path proofs, the Human Evidence Index, its hash sentinel, the Machine Mirror, or its checksum; and
* canonical, validated remediation-ledger record and closure operations so no task hand-edits the governed ledger.

### 9.2 Required close-pack and acceptance outputs

DEV-03 must use the generator and canonical updater to produce the ten adopted paths in §3.1 as one atomic evidence-derived package. A clean preflight permits a `SATISFIED` candidate; a blocking predicate requires a complete `NOT SATISFIED` close report and manifest with minimum follow-up, never a partial package. The remediation lineage must additionally produce the governed remediation-ledger pair in §9.1.

The close manifest’s `key_outputs` field must be a JSON object mapping stable names to exact repository-relative paths. It must not be a list.

### 9.3 Existing governed companions to refresh coherently

* `docs/evidence/INDEX.json`
* `docs/evidence/INDEX.sha256`
* `docs/evidence/INDEX.json.path_proof.txt`
* `docs/evidence/INDEX.sha256.path_proof.txt`
* `artifacts/evidence_index.jsonl`
* `artifacts/evidence_index.jsonl.sha256`
* `artifacts/evidence_index.jsonl.path_proof.txt`
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Only `tools/evidence/update_evidence_index.py` may create or refresh governed sibling path proofs and those evidence-ledger companions.

## 10. DEV execution plan

### DEV-01 — Build and validate the complete token/evidence matrix

**Owner:** CodEx for DEV-01 repository execution; Implementation Agent for scope guidance and verification; Gate B is owned by the independent technical reviewer defined in Gate B
**Revalidated status:** Required; first post-approval execution task
**Authorization required:** Full-plan approval authorizes DEV-01
**Dependencies:** Gate A `PASSED` and full-plan approval recorded
**Rails:** Closed; `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`
**PF09.6 accountability:** The epic-specific token/evidence matrix and generator-scaffold work is PF06 §3.5 close-gate work outside the phased build checklist. The canonical-updater, Human Evidence Index, hash-sentinel, Machine Mirror, checksum, and path-proof work advances PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, §`Subtask HDE-DIST005.2 — Global Index & Mirror discipline`; it creates no token claim and moves no status in that phased document.

**Inputs:**

* corrected 33-token roster in §7;
* current HDE Governance registry plus Addendum 2.37;
* current repository tests, CI configuration, QA manifest, primary logs, governed artifacts, Human Evidence Index, and Machine Mirror;
* active PF10 HDE-EPIC038 addenda, PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, and current repository history; and
* existing QA RCA and Doc Delta summary.

**Actions:**

1. Resolve every token to exact existing or approved planned tests, CI enforcement, applicable QA checks, governed artifacts, artifact keys, and proof anchors.
2. Scaffold `tools/evidence/generate_hde_epic038_closeout.py` and `tests/evidence/test_hde_epic038_closeout.py` with deterministic `--token-matrix` and read-only `--check-token-matrix` behavior.
3. Use the token-matrix mode to generate one unique non-placeholder row per token at `audit/qa/hde-epic038/token_evidence_matrix.md`. Do not hand-edit the matrix.
4. Classify every evidence binding as existing/reused evidence or exact planned-new closeout-slice evidence.
5. Bind `RELEASE_ID_RECOMPUTE_OK` to the canonical release manifest, release-identity JSON, recomputation log, identity-provenance generator, focused tests, and exact Index/Mirror records.
6. Exclude `DEV_DB_BRIDGE_FALLBACK_OK` and all non-token PF09 labels.
7. Preserve an unclaimed posture for any token whose decisive evidence is insufficient and record the exact prerequisite gap for correction before Gate B.
8. Add the matrix to the canonical evidence updater, run the updater, run the canonical orientation producer, run the updater a second time to bind the refreshed orientation report and its proof, then require updater `--check` and orientation `--check` to pass. No step may infer a token result.
9. Run token-matrix focused tests and `--check-token-matrix`; both must be read-only after generation.
10. Create the one remediation draft pull request with the DEV-01 fixed point. No open pull request exists at the revalidated repository baseline.
11. Submit the completed matrix on the DEV-01 draft pull request to the Gate B owner for review against the exact PR head and matrix path. Continue to DEV-02 only after the reviewer records `PASS` with the required Gate B record.

**Outputs:**

* `audit/qa/hde-epic038/token_evidence_matrix.md`
* `audit/qa/hde-epic038/token_evidence_matrix.md.path_proof.txt`
* token-matrix modes at `tools/evidence/generate_hde_epic038_closeout.py`
* token-matrix coverage at `tests/evidence/test_hde_epic038_closeout.py`
* coherently refreshed Index, Mirror, checksums, and proofs

**Verification:**

* exactly 33 unique token rows;
* exact corrected-roster set equality;
* no retired or unregistered name;
* all required fields complete;
* every existing path and artifact key resolves at the PR head;
* every planned-new path, artifact key, test, and workflow step is exact, task-owned, and explicitly non-existent or non-executed until its owning task;
* every proof anchor matches its governed artifact;
* no token is marked PASS merely because the row exists; and
* independent Gate B review is recorded before DEV-02.

**Success:** Gate B passes without placeholders or guessed bindings, authorizing transition to DEV-02 under the already-approved plan.

**Failure:** Preserve truthful nonclaiming work, record the exact incomplete rows, correct them within DEV-01, and repeat Gate B. Do not proceed to DEV-02 until Gate B passes; revise the plan or authority only if scope, rails, or authorization changes.

### DEV-02 — Implement deterministic closeout generation and fail-closed validation

**Owner:** CodEx for repository execution; Implementation Agent for scope guidance and verification
**Revalidated status:** Required; sequenced after DEV-01 and Gate B
**Authorization required:** Full-plan approval authorizes DEV-02 subject to Gate B
**Dependencies:** DEV-01 complete and Gate B passed
**Rails:** Closed
**PF09.6 accountability:** The epic-specific generator, focused-test, CI, remediation-ledger, close-report, and manifest work is PF06 §3.5 close-gate work outside the phased build checklist. The canonical-updater, Human Evidence Index, hash-sentinel, Machine Mirror, checksum, and path-proof work advances PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, §`Subtask HDE-DIST005.2 — Global Index & Mirror discipline`; it creates no token claim and moves no status in that phased document.

**Actions:**

1. Extend `tools/evidence/generate_hde_epic038_closeout.py` from its approved token-matrix scaffold to the complete closeout generator.
2. Extend `tests/evidence/test_hde_epic038_closeout.py` with focused positive and negative closeout coverage.
3. Make the generator consume, at minimum:
   * the complete token/evidence matrix;
   * current QA manifest and finalized-state validation;
   * existing QA RCA and Doc Delta summary;
   * approved PF09 scope and exclusions;
   * tracked-issue and ADR dispositions;
   * the corrected token roster;
   * reused governed evidence paths and proof anchors; and
   * canonical close-pack path constants.
4. Generate the acceptance map from the full intended proof-family roster, not a reduced global subset.
5. Implement preflight that distinguishes existing/reused evidence from planned-new evidence. It must fail on incomplete, duplicate, unregistered, retired, stale, incoherent, or unsupported existing bindings and on any planned binding that is inexact or not computable. It must never treat a not-yet-produced planned output as PASS, and it must record every execution-phase blocker for DEV-R1.
6. Generate a meaningful viability log in every candidate package. Record PASS only when all corrected-roster tokens and required proof-family bindings are supported by the generated fixed point; otherwise record the exact non-PASS posture and minimum follow-up without suppressing the package.
7. Generate the close report with:
   * exact close-pack pointers;
   * full approved PF09 scope;
   * token roster and per-token status;
   * reused-proof disclosure;
* an embedded complete QA RCA and Doc Delta summary that identifies `audit/qa/hde-epic038/00_meta/qa_rca_doc_delta_summary.md` as preserved execution-level source evidence and carries forward the complete closeout-level remediation, accepted-deviation, source-of-truth, evidence-light-source, RCA, remediation-loop, and Doc Delta accounting from HDE Build Notes Addendum 2.36;
* tracked-issue closeout mapping for TI-001 and TI-R1-001 through TI-R1-005;
* a PF06 §3.5.4 ADR block for ADR-R1-001 through ADR-R1-005 containing each decision label, decision point, materially different options when applicable, governing canon, final decision, epic-specific-versus-canonical disposition, and drain targets;
   * superseded interim-readiness posture;
   * explicit nonclaims; and
* evidence-derived final decision `SATISFIED` or `NOT SATISFIED`, with minimum follow-up when not satisfied.
8. Generate the close manifest with the same evidence-derived binary decision, roster, PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2 scope, and a named `key_outputs` object.
9. Emit the close package atomically with the evidence-derived binary decision. A blocking predicate produces `NOT SATISFIED` with minimum follow-up; it must never produce a partial package, suppress the binary decision, or force `SATISFIED`.
10. Implement a read-only `--check` mode that byte-compares expected outputs and fails on drift.
11. Implement canonical remediation-ledger record and close operations with stable blocker IDs, validated fields, deterministic ordering, and no hand-edit path.
12. Update the existing `.github/workflows/ci.yml` `test` job to add `--require-finalized` to the HDE-EPIC038 current-state check and run the new closeout `--check` command and focused closeout test against the complete PR head.

**Required negative tests:**

* duplicate token row;
* missing corrected-roster token;
* unexpected token;
* `DEV_DB_BRIDGE_FALLBACK_OK` in a current artifact;
* unregistered token;
* missing evidence artifact;
* missing or mismatched path proof;
* nonexistent or mismatched Index/Mirror key;
* reduced proof-family roster;
* stale QA current state;
* close report that only points to the execution-level QA RCA source without embedding the complete closeout-level QA RCA and Doc Delta summary;
* missing PF09 scope item;
* missing tracked-issue disposition;
* missing or incomplete PF06 §3.5.4 ADR block;
* manifest `key_outputs` encoded as a list;
* close-report and manifest decision mismatch;
* forced `SATISFIED` with any blocking predicate false;
* `NOT SATISFIED` without the minimum follow-up when any blocking predicate is false;
* suppression or partial emission of the close report or manifest when a blocking predicate is false; and
* any write attempted in `--check` mode.

**Outputs:**

* planned generator and test paths in §9.1;
* deterministic generator, preflight, and check behavior;
* canonical-updater registration for every new artifact family; and
* existing-workflow integration in `.github/workflows/ci.yml`.

DEV-02 does not create the canonical final close-pack or acceptance outputs. DEV-03 creates those outputs only after Gate C passes.

**Success:** Focused tests prove deterministic generation, read-only preflight and checking, atomic final output, and evidence-derived `SATISFIED` or `NOT SATISFIED` decision logic.

**Failure:** Preserve the failing test, record it in the remediation ledger, and enter DEV-R1. If current evidence is insufficient when a close package is generated, emit or retain the complete atomic `NOT SATISFIED` package with minimum follow-up.

### DEV-R1 — Eliminate every closeout blocker

**Owner:** CodEx for repository-local remediation execution; Implementation Agent for scope guidance, verification, and bounded OPS-authorization-record preparation; Product Owner alone for any separately approved OPS execution
**Revalidated status:** Required conditional loop; available when invoked after full-plan approval
**Authorization required:** Full-plan approval authorizes evidence, tooling, test, CI, and governed-artifact corrections within this plan; separately approved Product-Owner-only OPS execution for external work; separately approved implementation remediation for runtime-behavior changes; and separate owning-process authorization for any required QA revalidation
**Dependencies:** Any failed or unsupported result after its applicable producer, test, preflight, validator, or exact-head CI check has run. A Gate B failure returns to DEV-01 for correction and repeat review; the plan or authority must be revised only if scope, rails, or authorization changes.
**Rails:** Closed by default

**Purpose:** Convert every evidence-based blocker into an exact owned correction and continue until zero blockers remain. This is a required loop, not an optional follow-up list.

**Remediation ledger:**

Every loop instance must use the canonical closeout generator to add one stable entry to `audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md` containing:

* blocker ID and failing predicate;
* decisive failing evidence and command;
* failure class;
* exact owner and exact files permitted to change;
* correction performed;
* tests and validators run;
* before and after outcomes;
* governed artifacts regenerated;
* confirmation that no historical evidence was rewritten;
* external-action posture; and
* reviewer disposition.

The ledger must not be hand-edited. The canonical evidence updater must create and validate the ledger’s sibling proof and Index/Mirror bindings.

**Allowed correction classes:**

1. **Registry or wiring defect:** Correct the matrix, acceptance-map binding, artifact key, proof anchor, generator rule, or manifest binding without changing token semantics.
2. **Evidence-producer or validator defect:** Correct the smallest existing producer, validator, focused test, or closed-rails CI job required to prove the registered predicate.
3. **Governed-artifact drift:** Regenerate the affected primary artifact with its canonical producer, then run the canonical updater and all companion checks.
4. **Existing-behavior regression:** Stop this closeout lineage. Route the defect through a separately approved implementation-remediation plan, then revalidate every affected QA proof through its owning process. Resume this lineage only after the behavior and all affected evidence are current.
5. **Source-authority conflict:** Apply Addendum 2.37 and the highest applicable HDE Build Notes addendum; do not average or merge conflicting authorities.
6. **External-only proof gap:** Stop this DEV lineage before any external action. The Implementation Agent may prepare an exact bounded OPS authorization record naming the target, command family, evidence output, secret boundary, and one-pass success predicate. The Product Owner alone may authorize and execute that separately bounded OPS task. Return its secret-free governed evidence to this loop; no automated agent may perform the privileged action, and no generic discovery or repeated live call is authorized.

**Prohibitions:**

* no token removal merely to make the roster pass;
* no validator weakening, default-PASS path, hard-coded PASS, or evidence fabrication;
* no hand-edited generated proof;
* no historical QA result mutation;
* no new feature or public-contract scope;
* no unrelated cleanup; and
* no closure claim while any blocker remains.

**Loop verification:**

1. Re-run the smallest affected focused test and producer check.
2. Re-run the complete Gate C fixed-point suite.
3. Re-run closeout `--preflight`.
4. Keep the blocker open if any command fails or any evidence binding remains incomplete.
5. Close the ledger entry only when the original predicate and all downstream integrity checks pass.
6. Repeat for the next blocker until every pre-generation prerequisite is supported, every planned-new binding remains exactly computable, and preflight reports zero blockers.

**Success:** Zero open remediation-ledger entries, every pre-generation token prerequisite and non-token close obligation is supported, every planned-new binding is ready for deterministic generation, and Gates B and C pass. Gate D remains responsible for the final 33-of-33 PASS decision after DEV-03 outputs exist.

**Failure posture:** Every unresolved blocker remains recorded in the governed ledger and in a current `NOT SATISFIED` close report with minimum follow-up. The plan stays `IN PROGRESS`; `NOT SATISFIED` does not complete the remediation.

### DEV-03 — Generate the governed package and establish the evidence fixed point

**Owner:** CodEx for repository execution; Implementation Agent for scope guidance and verification
**Revalidated status:** Required; sequenced after DEV-02 and Gate C
**Authorization required:** Full-plan approval authorizes DEV-03 subject to its dependencies
**Dependencies:** Gates A and B passed, DEV-01 and DEV-02 complete, Gate C passed, Gate D pre-generation entry condition satisfied, and successful DEV-R1 clearance when the loop was invoked
**Rails:** Closed
**PF09.6 accountability:** Epic-specific close-report and manifest generation is PF06 §3.5 close-gate work outside the phased build checklist. The canonical-updater, Human Evidence Index, hash-sentinel, Machine Mirror, checksum, and path-proof work advances PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, §`Subtask HDE-DIST005.2 — Global Index & Mirror discipline`; it creates no token claim and moves no status in that phased document.

**Write order:**

1. Run current-state preflight and focused tests.
2. Run the closeout generator in read-only `--preflight` mode and record every blocker and evidence-derived decision input.
3. Run the closeout generator in write mode to emit the complete atomic binary package. A zero-blocker preflight is required for `SATISFIED`; any blocker produces `NOT SATISFIED` with minimum follow-up.
4. Run the canonical evidence updater after all primary artifacts exist.
5. Run the canonical orientation producer.
6. Run the canonical evidence updater a second time to bind the refreshed orientation report and its proof into the Human Evidence Index and Machine Mirror.
7. Run generator `--check`, updater `--check`, orientation `--check`, path validation, Mirror schema validation, Index hash validation, final-LF validation, and focused tests.
8. Do not hand-edit any generated artifact or companion after the fixed point.

**Runner readiness before pytest:**

```text
python -m pip install -r requirements-dev.txt
python -m pytest --version
```

**Existing fixed-point commands:**

```text
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_identity_provenance.py --check
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m pytest -q tests/evidence/test_identity_provenance.py tests/evidence/test_hde_epic038_qa_current_state.py
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC bash ci/checks/check_evidence_index_hash.sh
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC ci/checks/check_final_lf.sh
test "$(git rev-parse --show-toplevel)" = "$PWD"
git diff --check
```

**Planned new commands after DEV-02 creates the paths:**

```text
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hde_epic038_closeout.py --preflight
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hde_epic038_closeout.py
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hde_epic038_closeout.py --check
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m pytest -q tests/evidence/test_hde_epic038_closeout.py
```

The exact commands actually executed, exit codes, and PR-head workflow run must be retained in the pull-request evidence. This plan does not claim that the planned new commands already exist or have run.

**Success:**

* all required outputs exist;
* generator and updater checks are clean;
* all generic evidence checks pass;
* all focused tests pass;
* the PR diff contains no prohibited surface;
* no historical evidence was rewritten;
* the generated close report and manifest both record provisional `SATISFIED`; and
* the candidate is ready for DEV-04 exact-head CI and Gate D post-generation review.

**Failure:** Retain the truthful generated or test failure on the remediation branch, do not claim closure, and emit or preserve the complete atomic `NOT SATISFIED` close report and manifest with minimum follow-up. Enter DEV-R1 for the actual owner defect and repeat DEV-03 only after the recorded evidence change supports regeneration.

### DEV-04 — Close-PR review and Product Owner handoff

**Owner:** CodEx for pull-request preparation and updates; Implementation Agent for scope and evidence verification; Lead Developer for the PR gate review; Product Owner for squash-merge and later closeout
**Revalidated status:** Required; sequenced after DEV-03 and Gate D readiness
**Dependencies:** DEV-03 complete and Gate D post-generation review ready to run

**Actions:**

1. Update the bounded remediation draft pull request created in DEV-01 so it contains the complete tooling, tests, close-pack, acceptance-ledger, Index/Mirror, checksum, and proof delta. No open pull request existed at the revalidated baseline.
2. Require exact-head closed-rails CI, including the existing `test` job with its new closeout checks, to run all DEV-03 checks.
3. Inspect the complete changed-file list and confirm that no unapproved, external, runtime-behavior, PF-document, board, or historical QA surface changed. Any separately authorized runtime-behavior correction and affected-QA revalidation must be complete in their own approved lineage before this closeout pull request resumes.
4. Resolve review findings without weakening validators, shrinking the proof roster, removing approved tokens, or altering historical evidence.
5. Perform Gate D post-generation review against the exact PR head and its completed workflow run.
6. Mark the same pull request ready only after Gate D and every remediation acceptance criterion pass.
7. After Gate D records `PASS` and the Lead Developer approves the pull request, the Product Owner alone squash-merges the same bounded remediation pull request under normal branch protection. Merge remains distinct from Product Owner closeout, acceptance, PF09 or board movement, and epic closure.
8. After merge, hand the canonical close report and manifest to the Product Owner for the separate closeout decision and any later board/status drainage.

**Success:** The merged repository contains a coherent formal close package with an evidence-derived `SATISFIED` decision eligible for Product Owner closeout.

**Failure:** Return the exact blocking predicate to DEV-R1. Do not mark the remediation complete, ready the pull request, merge a knowingly failing close package, or accept an open blocker as the terminal outcome.

## 11. Acceptance criteria for this remediation

This remediation is complete only when all of the following are true:

* HDE Build Notes Addenda 2.37 and 2.38 are published at the recorded repository baseline; Addendum 2.37 controls the token correction, and Addendum 2.38 controls the matrix checkpoint.
* Full-plan approval was recorded before DEV-01 began, and Gate B passed before DEV-02 began.
* The matrix contains exactly the corrected 33-token roster.
* `DEV_DB_BRIDGE_FALLBACK_OK` is absent from every current acceptance and closeout artifact.
* `RELEASE_ID_RECOMPUTE_OK` is evidence-bound under the minted semantics.
* Every corrected-roster token is supported and recorded as PASS.
* All ten required paths in §3.1 exist and their proofs validate.
* The remediation ledger and sibling proof exist, all entries are closed, and their Index/Mirror bindings validate.
* The acceptance map and viability log cover the complete intended proof-family roster.
* The close manifest uses a named `key_outputs` object.
* Reused evidence is explicitly identified and never described as newly implemented.
* The full approved PF09 scope and excluded performance scope are stated.
* The close report contains the complete QA RCA and Doc Delta summary required by PF06 §0.4.1.2, identifies `audit/qa/hde-epic038/00_meta/qa_rca_doc_delta_summary.md` as preserved execution-level source evidence, and does not treat that noncanonical source path as the separate canonical closeout-summary location.
* The close report contains a complete PF06 §3.5.4 ADR block for ADR-R1-001 through ADR-R1-005, including each decision label, decision point, materially different options when applicable, governing canon, final decision, epic-specific-versus-canonical disposition, and drain targets.
* Index, Mirror, checksums, and proofs are coherent.
* Generator check mode is read-only and clean.
* All focused and generic validation passes at the PR head.
* The close report and manifest both record evidence-derived `SATISFIED`.
* No unauthorized OPS, Live QA, external access, runtime-behavior change, PF edit, PF09 movement, board mutation, acceptance, or closure is performed or falsely claimed; for any contingent external-only proof, the Implementation Agent may prepare the bounded OPS authorization record and process returned secret-free evidence, but the Product Owner alone may authorize and execute the separately bounded OPS task; any runtime correction is separately approved and followed by affected-QA revalidation before its evidence is reused.

## 12. Tracked issues and decision records

### TI-001 — Original registry-safe handling

**Disposition:** Resolved for the exact current HDE-EPIC038 roster by active Addendum 2.37.

* `RELEASE_ID_RECOMPUTE_OK` is admitted.
* `DEV_DB_BRIDGE_FALLBACK_OK` is removed from current claimability.
* The nine listed non-token obligations remain non-token obligations.
* Permanent registry drainage remains a separate non-blocking documentation action.

### TI-R1-001 — Missing token/evidence matrix

**Disposition:** Assigned to DEV-01 as the post-approval Gate B ledger-completion task under published PF10 Addendum 2.38; DEV-02 begins only after the matrix is complete and independently verified.

**Closure proof:** A unique, complete, non-placeholder 33-row matrix with exact existing or approved planned tests, CI enforcement, QA steps, paths, artifact keys, proof anchors, and intended claim states.

### TI-R1-002 — Missing adopted acceptance outputs

**Disposition:** Assigned to DEV-02 and DEV-03.

**Closure proof:** Acceptance map, matrix, meaningful PASS viability log, sibling proofs, and 33-of-33 PASS roster validation at the canonical paths.

### TI-R1-003 — Missing formal close pack

**Disposition:** Assigned to DEV-02 through DEV-04.

**Closure proof:** Canonical close report and manifest, both sibling proofs, exact named bindings, 33-of-33 final PASS roster, tracked-issue mapping, full PF09 scope, an embedded complete QA RCA and Doc Delta summary under PF06 §0.4.1.2 carrying forward HDE Build Notes Addendum 2.36, and `SATISFIED` decision.

### TI-R1-004 — Evidence-based blocker elimination

**Disposition:** Assigned to DEV-R1. Every unresolved blocker must remain recorded in the governed ledger and in a current `NOT SATISFIED` close report with minimum follow-up; `NOT SATISFIED` does not complete the remediation.

**Closure proof:** Governed remediation ledger with every discovered blocker closed by exact before/after evidence, followed by clean Gate C and zero-blocker closeout preflight.

### TI-R1-005 — Matrix-checkpoint reconciliation

**Disposition:** Resolved by published PF10 Addendum 2.38: full-plan approval may precede matrix creation; DEV-01 completes the standalone matrix; DEV-02 begins only after Gate B independently verifies matrix completeness. No token claim or closeout may occur before Gate B.

**Closure proof:** Full-plan approval recorded before DEV-01; complete non-placeholder 33-row matrix; and Gate B recorded before DEV-02.

### ADR-R1-001 — One closed-rails DEV lineage

**Decision:** Use one bounded DEV remediation lineage. No OPS or Live QA is necessary on current evidence.

**Reason:** The missing work is deterministic repository evidence packaging. Existing implementation, OPS, and QA evidence is sufficient for binding and review.

### ADR-R1-002 — Require `SATISFIED` without fabricating it

**Decision:** The remediation completes only at evidence-derived `SATISFIED`, but it must never suppress a required `NOT SATISFIED` decision. Whenever any corrected-roster token lacks sufficient current evidence, that token remains non-PASS and the close report records `NOT SATISFIED` with the minimum follow-up. DEV-R1 may continue, and a later report may supersede that decision only after the recorded evidence change supports `SATISFIED`. A candidate `SATISFIED` report remains provisional until exact-head CI and Gate D pass.

**Reason:** PF10 requires truthful binary close-report posture at the reviewed state. `NOT SATISFIED` records the blocker without completing the remediation; only evidence may support a later `SATISFIED` decision.

### ADR-R1-003 — Historical bridge evidence is immutable

**Decision:** Remove the bridge token only from current claim surfaces.

**Reason:** Historical evidence must preserve the transport semantics that existed when captured. Rewriting it would damage provenance.

### ADR-R1-004 — No new PF09 task

**Decision:** Treat epic-specific close-pack generation, testing, CI enforcement, remediation-ledger handling, and close-report and manifest creation as PF06 close-gate work outside the phased build checklist. Map the canonical-updater, Human Evidence Index, hash-sentinel, Machine Mirror, checksum, and path-proof work to PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2, §`Subtask HDE-DIST005.2 — Global Index & Mirror discipline`. Create no new task in that phased document and move no status in it.

**Reason:** The formal close package is a process obligation, while its governed Index/Mirror maintenance already has an exact phased subtask home.

### ADR-R1-005 — DEV-01 follows full-plan approval

**Decision:** Full-plan approval may precede matrix creation under published PF10 Addendum 2.38. After approval, DEV-01 constructs the standalone matrix; DEV-02 begins only after the matrix is complete and independently verified by Gate B. Any proposed change to the approved scope, rails, or authorization stops this lineage and requires plan or authority revision before execution resumes.

**Reason:** Published PF10 Addendum 2.38 reconciles PF04 Stage B with PF06’s conflicting approval-time rule for this plan. Approval and matrix construction claim no token; Gate B preserves complete non-placeholder wiring before token-consuming closeout work.

## 13. Canon and drainage dispositions

The following are separate, non-blocking drainage actions:

* add `RELEASE_ID_RECOMPUTE_OK` to the permanent acceptance-token registry;
* mark `DEV_DB_BRIDGE_FALLBACK_OK` deprecated or historical for current claimability;
* drain the Epic Remediation Plan type into Canon Plan Templates;
* preserve `HDE-DIST007` in the permanent Distillation checklist; and
* perform any supported PF09 or board status movement after Product Owner closeout.

None of those documentation or administrative actions may substitute for the governed close package. None is performed by this plan.

## 14. Approval request and nonclaim

Gate A has already passed; no approval is requested for it.

The approval sentinel below requests full-plan approval only after published PF10 Addendum 2.38 and its exact post-publication repository baseline are recorded in this plan. Approval authorizes DEV-01 through DEV-04 and DEV-R1 only within their stated gates and prohibitions; it does not make Gate B pass, claim any token, or authorize any separately gated runtime, QA, OPS, external, acceptance, status, board, or closure action.

Any proposed change to the approved scope, rails, or authorization stops this lineage and requires plan or authority revision before execution resumes.

It does not by itself:

* satisfy Gate B;
* claim any token as PASS;
* authorize external work;
* authorize runtime-behavior changes or QA revalidation;
* approve a generated close report;
* accept HDE-EPIC038;
* move PF09 or board status; or
* close the epic.

After Gate D `PASS` and Lead Developer approval, full-plan approval permits the Product Owner alone to squash-merge the same bounded remediation pull request under normal branch protection; that merge remains distinct from Product Owner closeout and epic acceptance.

After approval, DEV-01 begins. DEV-02 may begin only after Gate B passes. Product Owner closeout remains a later, separate action after a merged, validated close package exists.

ASK OK?
