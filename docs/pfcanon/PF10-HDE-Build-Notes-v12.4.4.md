# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v12.4.4  
Effective Date: 2026.07.26  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## Purpose

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

## Precedence and versioning

**PF10 IS CANONICAL.** For any topic explicitly covered in this scratchpad, PF10 is the current authoritative source of truth and **supersedes all other PF canon** until that item is formally reviewed and drained into the relevant permanent PF document.

**No competing canon may be used against an active PF10 entry.** While an item remains live in this scratchpad, agents must follow PF10 for that topic and must not prefer, merge, reinterpret, or reconcile conflicting language from older PF canon.

**Later addendum wins.** If multiple addenda address the same or overlapping scope, the **highest-numbered / latest addendum is the only authoritative one**. Earlier addenda on that scope are superseded and must not be used in parallel.

**Only the latest PF10 file matters.** Older scratchpad files are **fully drained, obsolete, or both**. Agents must **not** read them, reuse them, compare them, reconcile them, or carry forward language from them once a newer PF10 exists.

**This file contains only live items.** Drained items are removed from the scratchpad. Therefore, the current version of PF10 contains only active, not-yet-merged guidance.

**Silence means canon reverts to the permanent PF home.** If a topic does **not** appear in the latest PF10, then PF10 has nothing to say about it, and the source of truth is the relevant permanent PF-Canon document.

**Operational rule for agents:** use the latest PF10 first; obey it wherever it speaks; ignore older scratchpads entirely; fall back to permanent PF-Canon only where the latest PF10 is silent.

## Cross-references

 Inside this file, all references to PF documents MUST be **titles-only** (for example â€œHDE-Phased Epicsâ€, â€œGlow QA Guideâ€), never file names or version numbers in the body text.

When editing or extending this file, ChatGPT sessions must:

* Not restate PF content here.

* Link by **document title and section only**.

# 1\) TEMPLATE

TEMPLATE Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\> (autofill from system info)  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## 1.1 Addendum Index:

2.1) PR-01 HDE-EPIC038  
2.2) PR-02 HDE-EPIC038  
2.3) PR-03 HDE-EPIC038  
2.4) PR-04 HDE-EPIC038 â€” Approved Rescope and Canon Decisions  
2.5) PR-04 HDE-EPIC038  
2.6) OPS-01 HDE-EPIC038  
2.7) PR-05 HDE-EPIC038  
2.8) OPS-02 HDE-EPIC038  
2.9) PR-06 Post-Merge Remediation and OPS-01R HDE-EPIC038 â€” Approved Rescope and ADR-CANON-004  
2.10) PR-06 Remediation PR-A HDE-EPIC038  
2.11) PO-Delegated OPS Execution Authority â€” PO Authorization Controls Executor Identity  
2.12) pg-bridge and DB\_BRIDGE\_URL Deprecation and Retirement \- Direct PostgreSQL Is the Sole Active HDE Database Transport  
2.13) HDE-EPIC038 Post-PR359 Remediation â€” ADR-CANON-006 Direct-Only Selection Evidence and Historical Bridge Quarantine  
2.14) HDE-EPIC038 Post-PR359 Remediation â€” ADR-CANON-007 Authorization-Bound OPS-03 Direct Read-Only Posture Packet  
2.15) HDE-EPIC038 Post-PR359 Remediation â€” ADR-CANON-008 Direct-Only PF09.6 Completion Semantics and PR-06R Ownership  
2.16) HDE-EPIC038 PR-06R-A Merge â€” Scalable Manifest-Derived Release Identity, External Attestation, and Portable Evidence Semantics  
2.17) PR-06 Remediation HDE-EPIC038 PR-06R-A  
2.18) PR-06 Remediation \- OPS-03 HDE-EPIC038  
2.19) PR-06 Remediation \- HDE-EPIC038 OPS-03 â€” Authorized Reader-Role Provisioning, Direct Read-Only Capture, and Evidence-Admission Boundary  
2.20) PR-06 Remediation PR-06R-B HDE-EPIC038  
2.21) PR-06 Remediation State  
2.22) Implementation Retrospective HDE-EPIC038  
2.23) Post Implementation Audit Triage HDE-EPIC038  
2.24) Syntax-Origin Defects Remain Non-Blocking Regardless of Literal Execution Effect  
2.25) Recognize Epic Remediation Plans Pending Template Drainage

# 2\) Numbered Addenda

---

## 2.1) PR-01 HDE-EPIC038

### Review Summary

* Original PR implemented the PR-01 identity, release-identity, environment-snapshot, and evidence foundations, plus the dependency closure expressly accepted by the approved Product Owner rescope. The bounded rescope covers the production identity authority, non-production compatibility identity, emitter injection, atomic environment migration, directly dependent evidence regeneration, historical binding repair, and PR-01-specific closure enforcement.  
* Original PR merged into `main` as `f07ffbeb1f03c2ac9fc2d2c74217876ded844a7a`. Its base was `6b21ac91bf7f1e1b3e683ff331574fd7319744a7`; it changed 142 files.  
* Original PR had one material residual defect at merge: `generate_conjunction_writer_evidence.py --check` could execute the dev writer route while `DATABASE_URL` remained available, allowing the existing database persistence path to connect, execute SQL, and commit before artifact drift comparison.  
* Remedial PR followed Original PR directly in the same `main` lineage. Its base is exactly the Original PR merge commit, and it merged as `df662b518f0290a4bae6b26fb0332b374f28116a`. It changed only the affected generator and its focused regression test.  
* Remedial PR removes `DATABASE_URL` only within the `--check` capture boundary, restores its exact prior state in `finally`, preserves non-check behavior, and adds tests proving that a non-empty sentinel DSN cannot reach `psycopg.connect`, that governed artifact bytes remain unchanged, and that environment restoration also occurs when capture raises.  
* Original PR and Remedial PR both have successful visible GitHub Actions runs. The remedial run includes the repo-wide evidence tests, committed-closure check, Index/Mirror checks, sanity pipeline, compatibility HTTP lane, and independent conjunction closure lane.  
* Current `main` is the Remedial PR merge commit. No later commit was found after it, so there is no later-state divergence affecting the lifecycle touched-file set.  
* The approved rescope is treated as a bounded Product Owner canon amendment for the exact decisions it adjudicates. Permanent PF drainage remains required but is documentation drainage, not an implementation blocker.  
* PF09.6 impact is exactly proven for HDE-DIST005.1, HDE-DIST005.2, HDE-DIST006.1, HDE-DIST006.2, HDE-DIST006.3, HDE-DIST002.4, HDE-DIST002.5, HDE-DIST003.1, and HDE-DIST003.4. Status changes are supportable for the PR-01-complete subtasks; HDE-DIST005.1 and HDE-DIST005.2 remain shared with PR-06 and should not move on PR-01 alone.  
* No unresolved code, safety, evidence, lineage, or current-repo blocker remains after Remedial PR.

### GitHub / Repo Inspection

**Repository identity**

GitHub Repo | repository metadata | `"amthorn78/glow-hdengine-v2"` | `"default_branch=main"`

**Lifecycle baseline**

Original PR | API field `base_sha` | `"6b21ac91bf7f1e1b3e683ff331574fd7319744a7"` | `"base=main"`

**Original merged state**

Original PR | API fields `merged`, `head_sha`, `merge_commit_sha` | `"merged=true"` | `"f07ffbeb1f03c2ac9fc2d2c74217876ded844a7a"`

Original PR | API fields `changed_files`, `additions`, `deletions` | `"changed_files=142"` | `"additions=2388; deletions=749"`

**Remedial merged state**

Remedial PR | API fields `base_sha`, `head_sha`, `merge_commit_sha` | `"base_sha=f07ffbeb1f03c2ac9fc2d2c74217876ded844a7a"` | `"merge_commit_sha=df662b518f0290a4bae6b26fb0332b374f28116a"`

Remedial PR | API fields `changed_files`, `additions`, `deletions` | `"changed_files=2"` | `"additions=63; deletions=1"`

**Current state**

GitHub Repo | default-branch commit history | `"main HEAD=df662b518f0290a4bae6b26fb0332b374f28116a"` | `"previous lifecycle commit=f07ffbeb1f03c2ac9fc2d2c74217876ded844a7a"`

Search method: searched for commits newer than `df662b518f0290a4bae6b26fb0332b374f28116a` (case: sensitive); scope: default-branch commit history; tool: GitHub API; result: 0 hits.

**Lifecycle order and lineage**

GitHub Repo | compare `6b21ac9...df662b5` | `"ahead_by=2"` | `"behind_by=0"`

GitHub Repo | compare `f07ffbe...df662b5` | `"ahead_by=1"` | `"total_commits=1"`

The Remedial PR base is exactly the Original PR merge commit. Both PRs target `main`, so they form one unambiguous two-attempt lifecycle.

**Changed files**

* Original PR: 142 files.  
* Remedial PR: 2 files.  
* Lifecycle touched-file union: 142 files.  
* Remedial PR touched files:  
  * `tools/evidence/generate_conjunction_writer_evidence.py`  
  * `tests/evidence/test_dev_conjunction_identity.py`  
* No file was fully reverted to lifecycle baseline.  
* Four obsolete internal-version alias files remain deleted in the current state.

**Current final-state inspection**

The baseline-to-current comparison contains the same 142-file union as Original PR, with the two remedial files carrying the additional Remedial PR hunks. Current raw source was additionally inspected for:

* `tools/evidence/generate_conjunction_writer_evidence.py`  
* `tests/evidence/test_dev_conjunction_identity.py`  
* `adapter/http_reader.py`  
* `engine/compat/compute.py`  
* `tools/cli/generate_showcompat_artifacts.py`  
* `tools/evidence/run_canonical_json_gate.py`  
* the two governed writer evidence artifacts.

The final generatorâ€™s `--check` branch encloses `_capture_outputs()` in `_non_persistent_check_capture()`, and the database persistence function returns before importing or connecting to `psycopg` when `DATABASE_URL` is absent.

**Checks and CI inspected**

Original PR final head:

* workflow run `29191942424`  
* conclusion `success`  
* successful committed-closure check  
* successful evidence tests  
* successful Index, Mirror, hash, path-proof, and final-LF checks  
* successful sanity, compatibility HTTP, acceptance, and conjunction-closure lanes.

Remedial PR final head:

* workflow run `29206555501`  
* conclusion `success`  
* successful repo-wide evidence tests, including the new in-process non-persistence tests  
* successful committed-closure check  
* successful Index, Mirror, hash, and final-LF checks  
* successful sanity, compatibility HTTP, acceptance, and conjunction-closure lanes.

**Reviews and comments inspected**

Original PR had multiple implementation-review findings during its 120-commit lifecycle. Final-state inspection and Extra Evidence show that the identity-injection, dev identity, environment-singleton, independent two-run, showcompat, release-check, canonical-gate, and related findings were repaired before Original PR merged. The remaining live finding concerned database persistence during `--check`; Remedial PR addresses that exact finding.

Remedial PR discussion search:

Search method: searched PR discussion, inline comments, and review submissions for PR 347 (case: insensitive); scope: Remedial PR; tool: GitHub API; result: 0 comments.

**Governed evidence inspected**

The writer evidence remains byte-stable through Remedial PR:

* `artifacts/writer/conjunction_write_readback.log` records both writer runs, Reader readback parity, typed envelopes, and dev identity checks as true.  
* `artifacts/writer/conjunction_writer_summary.json` records all checks as true.  
* Remedial PR did not change either artifact, any path proof, Human Index record, Machine Mirror record, checksum, or manifest.

**Later commits**

Search method: searched default-branch commit history after the Remedial PR merge timestamp and SHA (case: sensitive); scope: GitHub Repo `main`; tool: GitHub API; result: 0 hits.

**Local commands**

No local repository checkout was available to this reviewer. No local command, test, or mutation is claimed. Review proof comes from GitHub PR metadata, complete lifecycle comparisons, per-file patches, current raw files, visible workflow results, governed artifacts, Implementation Doc, Extra Evidence, PF10, and task-relevant PF-Canon.

### Provenance (Original \-\> Remediation)

* **Claim:** Original PR intended to establish immutable identity and provenance, deterministic release and environment evidence, and canonical evidence-index ownership.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | body, Motivation/Description | `"single immutable Identity & Provenance authority"` | `"canonical evidence updater remains the sole writer"`  
* **Claim:** Original PR merged with the approved broadened dependency closure rather than only the narrow initial file list.  
  **Source:** Extra Evidence  
  **Evidence pointer:** Extra Evidence | Â§1 Decision | `"The rescoping of HDE-EPIC038 PR-01 is approved."` | `"bounded CI enforcement required to certify the committed PR-01 closure"`  
* **Claim:** Original PR preserved a bounded non-production identity profile and injected-emitter compatibility by approved architecture decision.  
  **Source:** Extra Evidence  
  **Evidence pointer:** Extra Evidence | Â§Â§3.1-3.2 | `"bounded dev compatibility identity profile"` | `"compatibility and testing seam, not an independent production identity source"`  
* **Claim:** Original PRâ€™s final visible CI was green.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | workflow run `29191942424` | `"status=completed"` | `"conclusion=success"`  
* **Claim:** Original PR nevertheless retained one unsafe check-mode path.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | review thread on `tools/evidence/generate_conjunction_writer_evidence.py` | `"Avoid writer persistence in --check"` | `"can insert into hde.idempotent_writes before any drift comparison"`  
* **Claim:** The unsafe behavior was caused by using the same route capture before distinguishing check mode from write mode.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | `diff --git a/tools/evidence/generate_conjunction_writer_evidence.py b/tools/evidence/generate_conjunction_writer_evidence.py` | `"expected = _capture_outputs()"` | `"if args.check:"`  
* **Claim:** Remedial PR was intentionally narrow.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | changed-file list | `"changed_files=2"` | `"additions=63; deletions=1"`  
* **Claim:** Remedial PR prevents the proven DB trigger while preserving the original environment.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | generator patch | `"os.environ.pop(\"DATABASE_URL\", None)"` | `"os.environ[\"DATABASE_URL\"] = original_database_url"`  
* **Claim:** Remedial PR adds behavioral proof rather than relying only on artifact-file comparison.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | test patch | `"psycopg.connect must not be called by --check"` | `"assert connect_calls == []"`  
* **Claim:** Remedial PR preserved governed evidence bytes.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | test/current artifacts | `"assert {path: path.read_bytes() for path in ARTIFACTS} == before"` | `"writer_dev_identity=true"`  
* **Claim:** Remedial PRâ€™s final visible CI was green.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | workflow run `29206555501` | `"status=completed"` | `"conclusion=success"`  
* **Claim:** Current repository state is exactly the remedial merged state.  
  **Source:** GitHub Repo  
  **Evidence pointer:** GitHub Repo | default-branch history | `"HEAD=df662b518f0290a4bae6b26fb0332b374f28116a"` | `"no later commits"`

#### Original PR Material Hunk Ledger

Each entry below is one file-local material change group. Where a file contained multiple related hunks, all observed hunk headers are listed in the same file-local group and are assessed separately in its corresponding NET item.

OPR-001 â€” File: `.github/workflows/ci.yml`; Patch and hunk header: `diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml`; `@@ -24,13 +24,18 @@ jobs:`; `@@ -59,6 +64,8 @@ jobs:`; Material effect: adds committed-closure verification and changes governed evidence steps to check mode before legacy write-capable tests; Risk category: governed CI/evidence; Evidence pointer: Original PR | workflow patch | `"Verify committed closure before any write-capable QA"` | `"update_evidence_index.py --check"`.

OPR-002 â€” File: `README.md`; Patch and hunk header: `diff --git a/README.md b/README.md`; `@@ -106,7 +106,7 @@`; `@@ -129,7 +129,7 @@`; `@@ -167,7 +167,7 @@`; Material effect: documents non-writing release checks and normalized internal-version evidence paths; Risk category: documentation; Evidence pointer: Original PR | README diff | `"--check is read-only"` | `"headers_cond_if_none_match.txt"`.

OPR-003 â€” File: `adapter/env_guard.py`; Patch and hunk header: `diff --git a/adapter/env_guard.py b/adapter/env_guard.py`; `@@ -22,7 +22,6 @@`; `@@ -55,6 +54,7 @@`; Material effect: aligns production rail validation with approved SAFE\_MODE/ALLOW\_NETWORK posture; Risk category: environment/config; Evidence pointer: Original PR | env-guard patch | `"ALLOW_NETWORK"` removed from override-forbidden keys | `"canonical rails remain valid production configuration"`.

OPR-004 â€” File: `adapter/http_reader.py`; Patch and hunk header: `diff --git a/adapter/http_reader.py b/adapter/http_reader.py`; `@@ -6,10 +6,11 @@`; `@@ -350,16 +351,13 @@ def reader_v1():`; `@@ -400,7 +398,7 @@ def aux_narrative():`; `@@ -654,15 +652,16 @@ def _emit_conjunction_response(`; `@@ -799,69 +798,11 @@ def _error`; Material effect: migrates Reader, internal-version, Aux, and conjunction identity consumption to approved helpers and dev profile; Risk category: contract/interface, environment, error handling; Evidence pointer: Original PR | adapter patch | `"identity_admin"` | `"dev_compat_identity"`.

OPR-005 â€” File: `artifacts/bodygraph/release_bindings.json`; Patch and hunk header: `diff --git a/artifacts/bodygraph/release_bindings.json b/artifacts/bodygraph/release_bindings.json`; whole-file added canonical JSON hunk; Material effect: adds governed release-to-BodyGraph binding; Risk category: governed evidence/schema; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=1"`.

OPR-006 â€” File: `artifacts/bodygraph/release_bindings.json.path_proof.txt`; Patch and hunk header: `diff --git a/artifacts/bodygraph/release_bindings.json.path_proof.txt b/artifacts/bodygraph/release_bindings.json.path_proof.txt`; whole-file added proof hunk; Material effect: path/hash/size proof for release binding; Risk category: governed evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=5"`.

OPR-007 â€” File: `artifacts/cli/ab.json`; Patch and hunk header: `diff --git a/artifacts/cli/ab.json b/artifacts/cli/ab.json`; canonical one-line replacement; Material effect: refreshes AB identity-coupled CLI evidence; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"additions=1"` | `"deletions=1"`.

OPR-008 â€” File: `artifacts/cli/ab.json.path_proof.txt`; Patch and hunk header: `diff --git a/artifacts/cli/ab.json.path_proof.txt b/artifacts/cli/ab.json.path_proof.txt`; proof refresh group; Material effect: updates AB proof binding; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"additions=2"` | `"deletions=2"`.

OPR-009 â€” File: `artifacts/cli/ba.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes BA identity-coupled CLI evidence; Risk category: governed evidence; Evidence pointer: Original PR | changed-file compare | `"status=modified"` | `"changes=2"`.

OPR-010 â€” File: `artifacts/cli/ba.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates BA proof binding; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-011 â€” File: `artifacts/cli/install/entrypoints.txt`; Patch and hunk header: six-line evidence replacement; Material effect: refreshes real-console entrypoint evidence; Risk category: governed evidence/installability; Evidence pointer: Original PR | compare | `"additions=6"` | `"deletions=6"`.

OPR-012 â€” File: `artifacts/cli/install/entrypoints.txt.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates entrypoint proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-013 â€” File: `artifacts/cli/install/installability_summary.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes installability result; Risk category: governed evidence/installability; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-014 â€” File: `artifacts/cli/install/installability_summary.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates installability proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-015 â€” File: `artifacts/cli/showcompat/args.json`; Patch and hunk header: canonical one-line replacement; Material effect: records immutable identity and deterministic invocation inputs; Risk category: governed evidence/CLI contract; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-016 â€” File: `artifacts/cli/showcompat/args.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates showcompat args proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-017 â€” File: `artifacts/cli/showcompat/stdout.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes deterministic showcompat output; Risk category: governed evidence/public-byte parity; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-018 â€” File: `artifacts/cli/showcompat/stdout.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates stdout proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-019 â€” File: `artifacts/cli/showcompat/stdout.json.sha256`; Patch and hunk header: one-line checksum replacement; Material effect: refreshes stdout checksum; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-020 â€” File: `artifacts/cli/showcompat/stdout.json.sha256.path_proof.txt`; Patch and hunk header: proof replacement; Material effect: updates checksum proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-021 â€” File: `artifacts/cli/summary.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes CLI conformance summary; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-022 â€” File: `artifacts/cli/summary.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates summary proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-023 â€” File: `artifacts/evidence_index.jsonl`; Patch and hunk header: records-only JSONL replacement group; Material effect: refreshes Machine Mirror and adds PR-01 records; Risk category: governed evidence/index; Evidence pointer: Original PR | compare | `"additions=40"` | `"deletions=32"`.

OPR-024 â€” File: `artifacts/evidence_index.jsonl.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: refreshes Mirror proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=10"` | `"status=modified"`.

OPR-025 â€” File: `artifacts/evidence_index.jsonl.sha256`; Patch and hunk header: one-line checksum replacement; Material effect: refreshes Mirror checksum; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-026 â€” File: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: refreshes Mirror-checksum proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-027 â€” File: `artifacts/identity/emitter_sha256.json`; Patch and hunk header: added canonical JSON hunk; Material effect: adds emitter provenance evidence; Risk category: governed identity evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=1"`.

OPR-028 â€” File: `artifacts/identity/emitter_sha256.json.path_proof.txt`; Patch and hunk header: added proof hunk; Material effect: adds emitter evidence proof; Risk category: governed evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=5"`.

OPR-029 â€” File: `artifacts/identity/invocation_sha256.json`; Patch and hunk header: added canonical JSON hunk; Material effect: adds Invocation provenance evidence; Risk category: governed identity evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=1"`.

OPR-030 â€” File: `artifacts/identity/invocation_sha256.json.path_proof.txt`; Patch and hunk header: added proof hunk; Material effect: adds Invocation evidence proof; Risk category: governed evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=5"`.

OPR-031 â€” File: `artifacts/identity/release_id.json`; Patch and hunk header: added canonical JSON hunk; Material effect: adds manifest-derived release identity evidence; Risk category: governed identity evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=1"`.

OPR-032 â€” File: `artifacts/identity/release_id.json.path_proof.txt`; Patch and hunk header: added proof hunk; Material effect: adds release-ID proof; Risk category: governed evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=5"`.

OPR-033 â€” File: `artifacts/identity/release_id_recompute.log`; Patch and hunk header: added four-line log hunk; Material effect: adds identity-family recompute proof; Risk category: governed identity evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=4"`.

OPR-034 â€” File: `artifacts/identity/release_id_recompute.log.path_proof.txt`; Patch and hunk header: added proof hunk; Material effect: adds recompute-log proof; Risk category: governed evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=5"`.

OPR-035 â€” File: `artifacts/identity/service_identity.json`; Patch and hunk header: canonical one-line replacement; Material effect: establishes six-field service identity evidence; Risk category: governed identity schema; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-036 â€” File: `artifacts/identity/service_identity.json.path_proof.txt`; Patch and hunk header: added proof hunk; Material effect: adds service-identity proof; Risk category: governed evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=5"`.

OPR-037 â€” File: `artifacts/math/freeze_pack_manifest.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes byte-identical manifest evidence copy; Risk category: release identity; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-038 â€” File: `artifacts/math/freeze_pack_manifest.json.sha256`; Patch and hunk header: one-line checksum replacement; Material effect: refreshes manifest checksum; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-039 â€” File: `artifacts/math/manifest_snapshot.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes evidence-only manifest summary; Risk category: governed release evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-040 â€” File: `artifacts/math/release_id.txt`; Patch and hunk header: one-line replacement; Material effect: refreshes canonical release ID; Risk category: release identity; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-041 â€” File: `artifacts/math/release_id.txt.sha256`; Patch and hunk header: one-line checksum replacement; Material effect: refreshes release-ID checksum; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-042 â€” File: `artifacts/math/release_id_recompute.log`; Patch and hunk header: log replacement group; Material effect: makes recompute evidence deterministic and checkable; Risk category: governed release evidence; Evidence pointer: Original PR | compare | `"additions=5"` | `"deletions=5"`.

OPR-043 â€” File: `artifacts/math/release_id_recompute.log.sha256`; Patch and hunk header: checksum replacement; Material effect: refreshes recompute-log checksum; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-044 â€” File: `artifacts/ops/internal_version/body_get.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes six-field admin identity capture; Risk category: governed ops evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-045 â€” File: `artifacts/ops/internal_version/body_get.json.path_proof.txt`; Patch and hunk header: proof replacement; Material effect: refreshes body proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-046 â€” File: `artifacts/ops/internal_version/body_get.sha256`; Patch and hunk header: checksum replacement; Material effect: refreshes internal-version body checksum; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-047 â€” File: `artifacts/ops/internal_version/body_get.sha256.path_proof.txt`; Patch and hunk header: proof replacement; Material effect: refreshes checksum proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-048 â€” File: `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`; Patch and hunk header: whole-file deletion; Material effect: removes duplicate legacy conditional-capture alias; Risk category: governed evidence path; Evidence pointer: Original PR | changed file | `"status=removed"` | `"deletions=1"`.

OPR-049 â€” File: `artifacts/ops/internal_version/cond_if_modified_since_headers.txt.path_proof.txt`; Patch and hunk header: whole-file deletion; Material effect: removes retired alias proof; Risk category: governed evidence path; Evidence pointer: Original PR | changed file | `"status=removed"` | `"deletions=5"`.

OPR-050 â€” File: `artifacts/ops/internal_version/cond_if_none_match_headers.txt`; Patch and hunk header: whole-file deletion; Material effect: removes second duplicate conditional-capture alias; Risk category: governed evidence path; Evidence pointer: Original PR | changed file | `"status=removed"` | `"deletions=1"`.

OPR-051 â€” File: `artifacts/ops/internal_version/cond_if_none_match_headers.txt.path_proof.txt`; Patch and hunk header: whole-file deletion; Material effect: removes second retired alias proof; Risk category: governed evidence path; Evidence pointer: Original PR | changed file | `"status=removed"` | `"deletions=5"`.

OPR-052 â€” File: `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`; Patch and hunk header: one-line canonical capture update; Material effect: retains canonical conditional capture; Risk category: governed transport evidence; Evidence pointer: Original PR | compare | `"additions=1"` | `"deletions=0"`.

OPR-053 â€” File: `artifacts/ops/internal_version/headers_cond_if_modified_since.txt.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates canonical capture proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-054 â€” File: `artifacts/ops/internal_version/headers_cond_if_none_match.txt`; Patch and hunk header: one-line canonical capture update; Material effect: retains canonical conditional capture; Risk category: governed transport evidence; Evidence pointer: Original PR | compare | `"additions=1"` | `"deletions=0"`.

OPR-055 â€” File: `artifacts/ops/internal_version/headers_cond_if_none_match.txt.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates canonical capture proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-056 â€” File: `artifacts/ops/internal_version/headers_get.txt`; Patch and hunk header: one-line capture update; Material effect: refreshes GET headers; Risk category: governed transport evidence; Evidence pointer: Original PR | compare | `"additions=1"` | `"deletions=0"`.

OPR-057 â€” File: `artifacts/ops/internal_version/headers_get.txt.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates GET-header proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-058 â€” File: `artifacts/ops/internal_version/headers_head.txt`; Patch and hunk header: one-line replacement; Material effect: refreshes HEAD headers; Risk category: governed transport evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-059 â€” File: `artifacts/ops/internal_version/headers_head.txt.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates HEAD-header proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-060 â€” File: `artifacts/ops/internal_version/request_chain_manifest.json`; Patch and hunk header: canonical one-line replacement; Material effect: normalizes request-chain bindings to canonical capture names; Risk category: governed manifest/evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-061 â€” File: `artifacts/ops/internal_version/request_chain_manifest.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates request-chain proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-062 â€” File: `artifacts/ops/internal_version/two_run_identity.log`; Patch and hunk header: seven-line replacement group; Material effect: refreshes independent two-run endpoint evidence; Risk category: governed determinism evidence; Evidence pointer: Original PR | compare | `"additions=7"` | `"deletions=7"`.

OPR-063 â€” File: `artifacts/ops/internal_version/two_run_identity.log.path_proof.txt`; Patch and hunk header: proof replacement; Material effect: refreshes two-run proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-064 â€” File: `artifacts/parity/two_run_identity.log`; Patch and hunk header: added four-line evidence hunk; Material effect: adds independent two-run service-identity evidence; Risk category: governed determinism evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=4"`.

OPR-065 â€” File: `artifacts/parity/two_run_identity.log.path_proof.txt`; Patch and hunk header: added proof hunk; Material effect: adds two-run proof; Risk category: governed evidence; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=5"`.

OPR-066 â€” File: `artifacts/runtime/env_matrix.snapshot.json`; Patch and hunk header: canonical singleton replacement; Material effect: migrates v1 snapshot to deterministic schema version 3; Risk category: schema/environment; Evidence pointer: Original PR | compare | `"additions=1"` | `"deletions=12"`.

OPR-067 â€” File: `artifacts/runtime/env_matrix.snapshot.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates environment snapshot proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-068 â€” File: `artifacts/writer/conjunction_write_readback.log`; Patch and hunk header: evidence-log replacement group; Material effect: adds dev identity and writer/readback parity results; Risk category: governed writer evidence; Evidence pointer: Original PR | compare | `"additions=4"` | `"deletions=2"`.

OPR-069 â€” File: `artifacts/writer/conjunction_write_readback.log.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates writer-log proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-070 â€” File: `artifacts/writer/conjunction_writer_summary.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes writer summary with dev identity checks; Risk category: governed writer evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-071 â€” File: `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates writer-summary proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-072 â€” File: `audit/EPIC-022_close_report.md`; Patch and hunk header: two-line historical-reference insertion; Material effect: corrects retained close-pack references; Risk category: historical evidence/closeout posture; Evidence pointer: Original PR | compare | `"additions=2"` | `"deletions=0"`.

OPR-073 â€” File: `audit/EPIC-022_close_report.md.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates historical report proof; Risk category: governed historical evidence; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-074 â€” File: `audit/gates/canonical_json/canonical_json.gate.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes gate summary; Risk category: governed gate evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-075 â€” File: `audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates gate-summary proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-076 â€” File: `audit/gates/canonical_json/json_canon_compare.log`; Patch and hunk header: 18-line replacement group; Material effect: refreshes canonical comparison records; Risk category: governed gate evidence; Evidence pointer: Original PR | compare | `"additions=18"` | `"deletions=18"`.

OPR-077 â€” File: `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates compare-log proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-078 â€” File: `audit/gates/canonical_json/json_canonical_check.log`; Patch and hunk header: 18-line replacement group; Material effect: refreshes canonical check records; Risk category: governed gate evidence; Evidence pointer: Original PR | compare | `"additions=18"` | `"deletions=18"`.

OPR-079 â€” File: `audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates check-log proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-080 â€” File: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`; Patch and hunk header: 18-line NDJSON replacement; Material effect: refreshes structured gate checks; Risk category: governed gate evidence; Evidence pointer: Original PR | compare | `"additions=18"` | `"deletions=18"`.

OPR-081 â€” File: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates structured check proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-082 â€” File: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`; Patch and hunk header: 18-line NDJSON replacement; Material effect: refreshes structured comparison records; Risk category: governed gate evidence; Evidence pointer: Original PR | compare | `"additions=18"` | `"deletions=18"`.

OPR-083 â€” File: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates structured compare proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-084 â€” File: `audit/gates/json_gate/canonical/json_gate_structured_record.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes structured gate result; Risk category: governed gate evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-085 â€” File: `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates structured-record proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-086 â€” File: `audit/gates/topology/orientation_demo.txt`; Patch and hunk header: one-line replacement; Material effect: refreshes evidence-topology orientation output; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-087 â€” File: `audit/gates/topology/orientation_demo.txt.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates orientation proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-088 â€” File: `audit/qa/hde-epic022/token_evidence_matrix.md`; Patch and hunk header: three-line historical path replacement; Material effect: corrects retained internal-version evidence references without new token claims; Risk category: token/QA posture; Evidence pointer: Original PR | compare | `"additions=3"` | `"deletions=3"`.

OPR-089 â€” File: `audit/qa/hde-epic022/token_evidence_matrix.md.path_proof.txt`; Patch and hunk header: proof replacement; Material effect: updates historical token-matrix proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-090 â€” File: `catalog/manifest.json`; Patch and hunk header: canonical one-line replacement; Material effect: refreshes manifest-listed file identity and release ID; Risk category: schema/release identity; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-091 â€” File: `docs/EVIDENCE_INDEX.md`; Patch and hunk header: two-line documentation replacement; Material effect: updates human navigation; Risk category: documentation; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-092 â€” File: `docs/INDEX.md`; Patch and hunk header: two-line documentation replacement; Material effect: updates general navigation; Risk category: documentation; Evidence pointer: Original PR | compare | `"changes=4"` | `"status=modified"`.

OPR-093 â€” File: `docs/acceptance_map_epic022.json`; Patch and hunk header: six-reference canonical replacement group; Material effect: corrects historical accepted-evidence paths; Risk category: governed acceptance posture; Evidence pointer: Original PR | compare | `"additions=6"` | `"deletions=6"`.

OPR-094 â€” File: `docs/acceptance_map_epic022.json.path_proof.txt`; Patch and hunk header: proof replacement; Material effect: updates historical acceptance-map proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-095 â€” File: `docs/evidence/INDEX.json`; Patch and hunk header: canonical one-line replacement; Material effect: adds and refreshes Human Index bindings; Risk category: governed evidence/index; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-096 â€” File: `docs/evidence/INDEX.json.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates Human Index proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=8"` | `"status=modified"`.

OPR-097 â€” File: `docs/evidence/INDEX.sha256`; Patch and hunk header: one-line checksum replacement; Material effect: refreshes Human Index sentinel; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-098 â€” File: `docs/evidence/INDEX.sha256.path_proof.txt`; Patch and hunk header: proof refresh group; Material effect: updates sentinel proof; Risk category: governed evidence; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-099 â€” File: `engine/cli/main.py`; Patch and hunk header: `@@ -33,7 +33,7 @@`; `@@ -435,10 +435,8 @@`; `@@ -610,15 +608,15 @@`; Material effect: replaces CLI identity env reads with shared authority and uses immutable release identity for Aux paths; Risk category: contract/interface; Evidence pointer: Original PR | CLI patch | `"identity_meta"` | `"_engine_identity"`.

OPR-100 â€” File: `engine/compat/identity.py`; Patch and hunk header: `@@ -0,0 +1,17 @@`; Material effect: creates approved bounded non-production compatibility identity profile; Risk category: architecture/contract; Evidence pointer: Original PR | new file patch | `"DEV_COMPAT_ENGINE_TAG"` | `"INV-DEV"`

OPR-101 â€” File: `engine/http/compat_handler.py`; Patch and hunk header: `@@ -4,6 +4,7 @@`; `@@ -118,9 +119,15 @@`; Material effect: routes compat-only HTTP identity through approved dev profile; Risk category: contract/interface; Evidence pointer: Original PR | compat patch | `"dev_compat_identity"` | `"compat_public"`.

OPR-102 â€” File: `engine/runtime/__init__.py`; Patch and hunk header: `@@ -1,3 +1,9 @@`; Material effect: exports identity helpers while preserving Reader exports; Risk category: interface; Evidence pointer: Original PR | runtime export patch | `"identity_admin"` | `"identity_meta"`.

OPR-103 â€” File: `engine/runtime/identity.py`; Patch and hunk header: `@@ -0,0 +1,74 @@`; Material effect: adds immutable six-field production identity authority and accessors; Risk category: architecture, schema, contract; Evidence pointer: Original PR | identity patch | `"IdentitySnapshot"` | `"_validate_identity"`

OPR-104 â€” File: `engine/runtime/public.py`; Patch and hunk header: `@@ -4,6 +4,7 @@`; `@@ -12,9 +13,9 @@`; `@@ -35,18 +36,19 @@`; `@@ -55,9 +57,9 @@`; Material effect: defaults Reader emission to immutable identity while preserving sanctioned injection; Risk category: public contract/interface; Evidence pointer: Original PR | runtime-public patch | `"identity_meta()"` | `"engine_tag or meta"`

OPR-105 â€” File: `glow_hdengine.egg-info/PKG-INFO`; Patch and hunk header: generated metadata replacement; Material effect: refreshes package metadata; Risk category: packaging; Evidence pointer: Original PR | compare | `"changes=6"` | `"status=modified"`.

OPR-106 â€” File: `glow_hdengine.egg-info/SOURCES.txt`; Patch and hunk header: generated source-list insertion; Material effect: registers new source/test files; Risk category: packaging; Evidence pointer: Original PR | compare | `"additions=2"` | `"deletions=0"`.

OPR-107 â€” File: `scripts/ingest/run_vendor_ingest.py`; Patch and hunk header: 25-line deletion group; Material effect: removes legacy independent env-snapshot writer; Risk category: environment/schema; Evidence pointer: Original PR | compare | `"deletions=25"` | `"additions=0"`.

OPR-108 â€” File: `scripts/qa/epic009_precommit.sh`; Patch and hunk header: 14-line replacement group; Material effect: migrates legacy QA consumption to env snapshot v3 check; Risk category: QA/validation; Evidence pointer: Original PR | compare | `"additions=14"` | `"deletions=14"`.

OPR-109 â€” File: `scripts/release_id_recompute.py`; Patch and hunk header: `@@ -8,7 +8,7 @@`; `@@ -38,9 +38,13 @@`; `@@ -71,10 +75,10 @@`; `@@ -90,7 +94,27 @@`; `@@ -99,7 +123,7 @@`; `@@ -177,6 +201,11 @@`; `@@ -189,6 +218,107 @@`; `@@ -200,6 +330,7 @@`; `@@ -212,71 +343,68 @@`; Material effect: makes release validation deterministic, renderer-based, and non-writing in check mode while adding manifest refresh support; Risk category: release identity, evidence, validation; Evidence pointer: Original PR | release tool patch | `"_expected_evidence_outputs"` | `"_stale_outputs"`

OPR-110 â€” File: `tests/adapter/test_env_guard_forbidden_matrix.py`; Patch and hunk header: test replacement group; Material effect: validates approved production rails; Risk category: environment-test coverage; Evidence pointer: Original PR | compare | `"additions=5"` | `"deletions=3"`.

OPR-111 â€” File: `tests/adapter/test_env_guard_prod_variants.py`; Patch and hunk header: test replacement group; Material effect: covers production aliases and rail values; Risk category: environment-test coverage; Evidence pointer: Original PR | compare | `"additions=9"` | `"deletions=10"`.

OPR-112 â€” File: `tests/adapter/test_env_guard_silence_and_idempotence.py`; Patch and hunk header: one-line test replacement; Material effect: preserves env-guard idempotence coverage; Risk category: safety-test coverage; Evidence pointer: Original PR | compare | `"changes=2"` | `"status=modified"`.

OPR-113 â€” File: `tests/adapter/test_gate_auth.py`; Patch and hunk header: multiple auth/internal-version test hunks; Material effect: preserves current internal-version access and transport behavior; Risk category: security/contract tests; Evidence pointer: Original PR | compare | `"additions=54"` | `"deletions=35"`.

OPR-114 â€” File: `tests/cli/test_cli_canonical_bytes.py`; Patch and hunk header: three-line deletion group; Material effect: removes obsolete env-injection assumptions; Risk category: deleted test expectations; Evidence pointer: Original PR | compare | `"deletions=3"` | `"additions=0"`.

OPR-115 â€” File: `tests/cli/test_showcompat_parity_and_identity.py`; Patch and hunk header: multiple identity/parity test hunks; Material effect: expands immutable identity and parity coverage; Risk category: contract/determinism tests; Evidence pointer: Original PR | compare | `"additions=75"` | `"deletions=13"`.

OPR-116 â€” File: `tests/evidence/test_aux_preview_identity_parity.py`; Patch and hunk header: added 24-line test; Material effect: proves Aux uses immutable release identity; Risk category: evidence/contract tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=24"`.

OPR-117 â€” File: `tests/evidence/test_canonical_json_gate_check_outputs.py`; Patch and hunk header: added 21-line test; Material effect: proves stale committed canonical-gate outputs fail check mode; Risk category: governed evidence tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=21"`.

OPR-118 â€” File: `tests/evidence/test_cli_conformance_artifacts.py`; Patch and hunk header: added 102-line test; Material effect: proves CLI evidence, real console installability, and non-writing checks; Risk category: packaging/evidence tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=102"`.

OPR-119 â€” File: `tests/evidence/test_dev_conjunction_identity.py`; Patch and hunk header: Original PR added file; `@@ -0,0 +1,50 @@` at the pre-remediation state; Material effect: initially proves artifact-byte stability and dev identity but does not intercept DB persistence; Risk category: insufficient safety test; Evidence pointer: Original PR | initial test | `"ARTIFACTS"` | `"--check"`.

OPR-120 â€” File: `tests/evidence/test_env_matrix_snapshot_v3.py`; Patch and hunk header: added 123-line test; Material effect: proves exact v3 shape, deterministic secret-presence fixture, singleton ownership, migrated consumers, and non-writing check; Risk category: schema/environment tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=123"`.

OPR-121 â€” File: `tests/evidence/test_identity_provenance.py`; Patch and hunk header: added 67-line test; Material effect: proves identity shape, provenance generator, independent runs, and check mode; Risk category: identity/evidence tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=67"`.

OPR-122 â€” File: `tests/evidence/test_internal_version_manifest_captures.py`; Patch and hunk header: added 41-line test; Material effect: proves canonical internal-version capture naming and manifest binding; Risk category: governed ops evidence tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=41"`.

OPR-123 â€” File: `tests/evidence/test_release_bindings.py`; Patch and hunk header: added 15-line test; Material effect: proves deterministic release-binding generation/check; Risk category: schema/evidence tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=15"`.

OPR-124 â€” File: `tests/evidence/test_release_manifest_content_binding.py`; Patch and hunk header: added 185-line test; Material effect: proves manifest content, release identity, and non-writing recompute behavior; Risk category: release/evidence tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=185"`.

OPR-125 â€” File: `tests/http/test_dev_conjunction_http.py`; Patch and hunk header: HTTP test replacement group; Material effect: preserves dev writer/reader identity and contract behavior; Risk category: HTTP contract tests; Evidence pointer: Original PR | compare | `"additions=7"` | `"deletions=2"`.

OPR-126 â€” File: `tests/qa/test_epic022_acceptance_scaffold.py`; Patch and hunk header: historical-path test replacement group; Material effect: validates canonical retained evidence paths; Risk category: QA/acceptance posture; Evidence pointer: Original PR | compare | `"additions=37"` | `"deletions=11"`.

OPR-127 â€” File: `tests/runtime/test_identity.py`; Patch and hunk header: added 66-line test; Material effect: proves six fields, immutability, helpers, runtime-source restrictions, and injection behavior; Risk category: architecture/contract tests; Evidence pointer: Original PR | changed file | `"status=added"` | `"changes=66"`.

OPR-128 â€” File: `tests/transport/test_internal_version_contract.py`; Patch and hunk header: transport-test replacement group; Material effect: proves GET/HEAD/no-store/no-ETag/conditional behavior and identity payload; Risk category: transport contract tests; Evidence pointer: Original PR | compare | `"additions=6"` | `"deletions=4"`.

OPR-129 â€” File: `tools/cli/emitter_symbol_proof.py`; Patch and hunk header: small topology-proof update; Material effect: extends approved emitter-call topology; Risk category: evidence tool; Evidence pointer: Original PR | compare | `"additions=3"` | `"deletions=1"`.

OPR-130 â€” File: `tools/cli/generate_cli_conformance_artifacts.py`; Patch and hunk header: multi-hunk 255-line generator change; Material effect: adds immutable identity alignment, offline real-console installability, deterministic output rendering, and non-writing check comparison; Risk category: CLI/evidence/packaging; Evidence pointer: Original PR | compare | `"additions=181"` | `"deletions=74"`.

OPR-131 â€” File: `tools/cli/generate_showcompat_artifacts.py`; Patch and hunk header: multi-hunk 76-line generator change; Material effect: uses active interpreter, immutable identity, deterministic args, and output comparison; Risk category: CLI/evidence; Evidence pointer: GitHub Repo | current file | `"execution_cmd=[sys.executable,...]"` | `"emitted_meta == immutable_meta"`

OPR-132 â€” File: `tools/cli/serializer_grep_guard.py`; Patch and hunk header: small guard update; Material effect: aligns serializer guard with new runtime path; Risk category: safety validator; Evidence pointer: Original PR | compare | `"additions=3"` | `"deletions=1"`.

OPR-133 â€” File: `tools/evidence/generate_conjunction_writer_evidence.py`; Patch and hunk header: `@@ -1,6 +1,7 @@`; `@@ -12,6 +13,7 @@`; `@@ -28,12 +30,6 @@`; `@@ -49,11 +45,22 @@`; `@@ -62,7 +69,10 @@`; `@@ -87,55 +97,88 @@`; Material effect: introduces deterministic renderer/check behavior, dev identity assertions, and writer/readback evidence; initial check reused the write-capable route capture; Risk category: governed evidence, external-state safety; Evidence pointer: Original PR | generator patch | `"expected = _capture_outputs()"` | `"if args.check"`

OPR-134 â€” File: `tools/evidence/generate_env_matrix_snapshot.py`; Patch and hunk header: `@@ -0,0 +1,75 @@`; Material effect: adds deterministic canonical v3 singleton producer/check; Risk category: environment/schema/evidence; Evidence pointer: Original PR | generator patch | `"schema_version": 3` | `"PRESENCE"`

OPR-135 â€” File: `tools/evidence/generate_epic032_pr01_router_evidence.py`; Patch and hunk header: multi-hunk dependency-evidence update; Material effect: aligns retained EPIC032 evidence with immutable identity and check mode; Risk category: historical dependency evidence; Evidence pointer: Original PR | compare | `"additions=46"` | `"deletions=7"`.

OPR-136 â€” File: `tools/evidence/generate_identity_provenance.py`; Patch and hunk header: `@@ -0,0 +1,138 @@`; Material effect: adds deterministic six-artifact identity provenance producer/check and independent two-run collection; Risk category: identity/evidence; Evidence pointer: Original PR | new generator | `"_identity_bytes()"` | `"service_run1 != service_run2"`

OPR-137 â€” File: `tools/evidence/generate_rails_closed_phase1.py`; Patch and hunk header: delegation update group; Material effect: delegates env singleton ownership to v3 producer; Risk category: environment/evidence; Evidence pointer: Original PR | compare | `"additions=9"` | `"deletions=6"`.

OPR-138 â€” File: `tools/evidence/generate_release_bindings.py`; Patch and hunk header: `@@ -0,0 +1,29 @@`; Material effect: adds deterministic release-binding producer/check using source-selection and refresh-policy artifact identities; Risk category: schema/evidence; Evidence pointer: Original PR | generator patch | `"INPUTS"` | `"bindings"`

OPR-139 â€” File: `tools/evidence/regenerate_identity_closure.py`; Patch and hunk header: added 140-line orchestrator; Material effect: adds bounded PR-01 write/check closure and committed-source release binding; Risk category: CI/evidence orchestration; Evidence pointer: GitHub Repo | current file | `"_write_closure"` | `"_check_closure"`

OPR-140 â€” File: `tools/evidence/run_canonical_json_gate.py`; Patch and hunk header: multi-hunk 128-line gate change; Material effect: makes gate outputs deterministic and makes check-only compare committed gate artifacts; Risk category: governed gate evidence; Evidence pointer: GitHub Repo | current file | `"_stale_outputs(outputs)"` | `"stale_gate_artifact"`

OPR-141 â€” File: `tools/evidence/update_evidence_index.py`; Patch and hunk header: 12-line registration insertion; Material effect: registers PR-01 primary artifacts with canonical Index/Mirror/proof writer; Risk category: governed evidence/index; Evidence pointer: Original PR | compare | `"additions=12"` | `"deletions=0"`.

OPR-142 â€” File: `tools/ops/internal_version_artifacts.py`; Patch and hunk header: multi-hunk 15-line capture migration; Material effect: normalizes conditional evidence filenames and manifest refresh behavior; Risk category: governed ops evidence; Evidence pointer: Original PR | compare | `"additions=10"` | `"deletions=5"`.

#### Remedial PR Material Hunk Ledger

RPR-001 â€” File: `tests/evidence/test_dev_conjunction_identity.py`; Patch and hunk header: `diff --git a/tests/evidence/test_dev_conjunction_identity.py b/tests/evidence/test_dev_conjunction_identity.py`; `@@ -4,9 +4,13 @@`; `@@ -48,3 +52,43 @@`; Material effect: adds fake-connect fail-fast proof, non-empty sentinel DSN, artifact-byte equality, success restoration, and exception restoration; Risk category: safety-test coverage; Evidence pointer: Remedial PR | patch | `"pytest.fail(\"psycopg.connect must not be called by --check\")"` | `"assert connect_calls == []"`

RPR-002 â€” File: `tools/evidence/generate_conjunction_writer_evidence.py`; Patch and hunk header: `diff --git a/tools/evidence/generate_conjunction_writer_evidence.py b/tools/evidence/generate_conjunction_writer_evidence.py`; `@@ -2,6 +2,7 @@`; `@@ -18,6 +19,7 @@`; `@@ -160,13 +162,28 @@`; `@@ -176,6 +193,7 @@`; Material effect: encloses only check-mode capture in a DATABASE\_URL-neutralizing, exception-safe context and leaves write mode unchanged; Risk category: external-state safety; Evidence pointer: Remedial PR | patch | `"os.environ.pop(\"DATABASE_URL\", None)"` | `"finally"`

### Net Effective Diff Review

Common current-state proof for NET-001 through NET-142:

GitHub Repo | lifecycle compare and default-branch history | `"baseline=6b21ac91..."` | `"current=df662b518..."`

Search method: searched for later commits after current lifecycle HEAD (case: sensitive); scope: default branch; tool: GitHub API; result: 0 hits.

NET-001 â€” File/artifact: `.github/workflows/ci.yml`; Covered hunks: OPR-001; Combined merged state: committed PR-01 closure and evidence checks run before legacy write-capable QA; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: closure and repo-wide safeguards both passed in both final workflow runs; Assessment: retained; Evidence pointer(s): Original PR workflow patch and VAL-006/VAL-007; GitHub Repo proof: current HEAD includes the workflow and Remedial PR did not touch it; PF reference: PF19 â€” Glow QA Guide, Â§2.2.11 Evidence-governed CI sequence.

NET-002 â€” File/artifact: `README.md`; Covered hunks: OPR-002; Combined merged state: documentation reflects non-writing checks and canonical evidence names; Current final repo state: same; Later-change impact: None; Risk: Low; Assessment: consistent with code; Evidence pointer(s): OPR-002; GitHub Repo proof: current HEAD equals remedial merge; PF reference: None.

NET-003 â€” File/artifact: `adapter/env_guard.py`; Covered hunks: OPR-003; Combined merged state: approved production rails are accepted while override keys remain guarded; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: current tests cover production aliases and canonical defaults; Assessment: approved rescope dependency; Evidence pointer(s): OPR-003, NET-110â€“112; GitHub Repo proof: current file unchanged after Original PR; PF reference: PF07 â€” Glow Infrastructure.

NET-004 â€” File/artifact: `adapter/http_reader.py`; Covered hunks: OPR-004; Combined merged state: Reader and internal-version use approved identity helpers, dev conjunction uses approved dev identity, and existing writer persistence path remains unchanged; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: Remedial PR neutralizes the DB trigger at the generator boundary without altering route behavior; Assessment: contract preserved; Evidence pointer(s): OPR-004, RPR-002, current raw file; GitHub Repo proof: `_persist_idempotence_db` still requires non-empty DATABASE\_URL before import/connect. ; PF reference: approved rescope Â§Â§5.1-5.3.

NET-005 â€” File/artifact: `artifacts/bodygraph/release_bindings.json`; Covered hunks: OPR-005; Combined merged state: governed release-binding primary exists; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: accepted shape is governed by the approved rescope pending PF12 drainage; Assessment: coherent and indexed; Evidence pointer(s): Original PR generator/test/Index; GitHub Repo proof: file remains in baseline-to-current compare; PF reference: approved rescope Â§8.4.

NET-006 â€” File/artifact: `artifacts/bodygraph/release_bindings.json.path_proof.txt`; Covered hunks: OPR-006; Combined merged state: sibling proof exists; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: Index/Mirror/path checks passed; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12 â€” HDE Schemas and Artifacts.

NET-007 â€” File/artifact: `artifacts/cli/ab.json`; Covered hunks: OPR-007; Combined merged state: regenerated AB evidence; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: CLI parity and canonical-gate checks passed; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: approved identity architecture.

NET-008 â€” File/artifact: `artifacts/cli/ab.json.path_proof.txt`; Covered hunks: OPR-008; Combined merged state: refreshed AB proof; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: proof checks passed; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-009 â€” File/artifact: `artifacts/cli/ba.json`; Covered hunks: OPR-009; Combined merged state: regenerated BA evidence; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: parity checks passed; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: approved identity architecture.

NET-010 â€” File/artifact: `artifacts/cli/ba.json.path_proof.txt`; Covered hunks: OPR-010; Combined merged state: refreshed BA proof; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: path checks passed; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-011 â€” File/artifact: `artifacts/cli/install/entrypoints.txt`; Covered hunks: OPR-011; Combined merged state: real-console entrypoint evidence current; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: installability gap closed; Evidence pointer(s): Original PR CI and Extra Evidence; GitHub Repo proof: no later change; PF reference: None.

NET-012 â€” File/artifact: `artifacts/cli/install/entrypoints.txt.path_proof.txt`; Covered hunks: OPR-012; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: evidence checks passed; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-013 â€” File/artifact: `artifacts/cli/install/installability_summary.json`; Covered hunks: OPR-013; Combined merged state: installability summary current; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: None.

NET-014 â€” File/artifact: `artifacts/cli/install/installability_summary.json.path_proof.txt`; Covered hunks: OPR-014; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-015 â€” File/artifact: `artifacts/cli/showcompat/args.json`; Covered hunks: OPR-015; Combined merged state: deterministic args and immutable identity recorded; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: current generator verifies emitted identity equals runtime identity; Assessment: coherent; Evidence pointer(s): current generator lines 59-107; GitHub Repo proof: no later change. ; PF reference: approved rescope Â§5.

NET-016 â€” File/artifact: `artifacts/cli/showcompat/args.json.path_proof.txt`; Covered hunks: OPR-016; Combined merged state: proof refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-017 â€” File/artifact: `artifacts/cli/showcompat/stdout.json`; Covered hunks: OPR-017; Combined merged state: immutable-identity showcompat output; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: active-interpreter and identity checks are present; Assessment: coherent; Evidence pointer(s): current generator lines 59-82; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-018 â€” File/artifact: `artifacts/cli/showcompat/stdout.json.path_proof.txt`; Covered hunks: OPR-018; Combined merged state: proof refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-019 â€” File/artifact: `artifacts/cli/showcompat/stdout.json.sha256`; Covered hunks: OPR-019; Combined merged state: checksum refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-020 â€” File/artifact: `artifacts/cli/showcompat/stdout.json.sha256.path_proof.txt`; Covered hunks: OPR-020; Combined merged state: checksum proof refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-021 â€” File/artifact: `artifacts/cli/summary.json`; Covered hunks: OPR-021; Combined merged state: conformance summary current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-022 â€” File/artifact: `artifacts/cli/summary.json.path_proof.txt`; Covered hunks: OPR-022; Combined merged state: proof refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-023 â€” File/artifact: `artifacts/evidence_index.jsonl`; Covered hunks: OPR-023; Combined merged state: Machine Mirror includes PR-01 records and remains records-only; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: schema, checksum, path, and updater checks passed in both workflow runs; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12 â€” HDE Schemas and Artifacts, Â§Machine Evidence Mirror.

NET-024 â€” File/artifact: `artifacts/evidence_index.jsonl.path_proof.txt`; Covered hunks: OPR-024; Combined merged state: Mirror proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-025 â€” File/artifact: `artifacts/evidence_index.jsonl.sha256`; Covered hunks: OPR-025; Combined merged state: Mirror checksum current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-026 â€” File/artifact: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`; Covered hunks: OPR-026; Combined merged state: checksum proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-027 â€” File/artifact: `artifacts/identity/emitter_sha256.json`; Covered hunks: OPR-027; Combined merged state: approved emitter provenance artifact exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: accepted under bounded rescope pending PF drainage; Evidence pointer(s): Original PR generator/test and Extra Evidence; GitHub Repo proof: no later change; PF reference: approved rescope Â§Â§4 and 8.5.

NET-028 â€” File/artifact: `artifacts/identity/emitter_sha256.json.path_proof.txt`; Covered hunks: OPR-028; Combined merged state: proof exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-029 â€” File/artifact: `artifacts/identity/invocation_sha256.json`; Covered hunks: OPR-029; Combined merged state: approved Invocation provenance artifact exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: accepted under bounded rescope pending PF drainage; Evidence pointer(s): Extra Evidence Â§4; GitHub Repo proof: no later change; PF reference: approved rescope Â§8.5.

NET-030 â€” File/artifact: `artifacts/identity/invocation_sha256.json.path_proof.txt`; Covered hunks: OPR-030; Combined merged state: proof exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-031 â€” File/artifact: `artifacts/identity/release_id.json`; Covered hunks: OPR-031; Combined merged state: manifest-derived release evidence exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: release checks passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12 release identity.

NET-032 â€” File/artifact: `artifacts/identity/release_id.json.path_proof.txt`; Covered hunks: OPR-032; Combined merged state: proof exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-033 â€” File/artifact: `artifacts/identity/release_id_recompute.log`; Covered hunks: OPR-033; Combined merged state: recompute evidence exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: deterministic checks passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST002.4.

NET-034 â€” File/artifact: `artifacts/identity/release_id_recompute.log.path_proof.txt`; Covered hunks: OPR-034; Combined merged state: proof exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-035 â€” File/artifact: `artifacts/identity/service_identity.json`; Covered hunks: OPR-035; Combined merged state: exact approved six-field snapshot exists; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: exact-field and immutability tests passed; Assessment: accepted under approved rescope; Evidence pointer(s): identity tests and Extra Evidence; GitHub Repo proof: no later change; PF reference: approved rescope Â§5.1.

NET-036 â€” File/artifact: `artifacts/identity/service_identity.json.path_proof.txt`; Covered hunks: OPR-036; Combined merged state: proof exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-037 â€” File/artifact: `artifacts/math/freeze_pack_manifest.json`; Covered hunks: OPR-037; Combined merged state: byte-identical release manifest evidence refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: release checks passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12 Â§6.

NET-038 â€” File/artifact: `artifacts/math/freeze_pack_manifest.json.sha256`; Covered hunks: OPR-038; Combined merged state: checksum refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-039 â€” File/artifact: `artifacts/math/manifest_snapshot.json`; Covered hunks: OPR-039; Combined merged state: evidence-only summary refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: not used as identity source; Evidence pointer(s): release tool; GitHub Repo proof: no later change; PF reference: PF12.

NET-040 â€” File/artifact: `artifacts/math/release_id.txt`; Covered hunks: OPR-040; Combined merged state: canonical release ID refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: recompute check passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12 Â§6.

NET-041 â€” File/artifact: `artifacts/math/release_id.txt.sha256`; Covered hunks: OPR-041; Combined merged state: checksum refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-042 â€” File/artifact: `artifacts/math/release_id_recompute.log`; Covered hunks: OPR-042; Combined merged state: deterministic recompute log current; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: check mode now compares this output; Assessment: coherent; Evidence pointer(s): release tool `_expected_evidence_outputs`; GitHub Repo proof: no later change; PF reference: PF09.6.

NET-043 â€” File/artifact: `artifacts/math/release_id_recompute.log.sha256`; Covered hunks: OPR-043; Combined merged state: checksum current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-044 â€” File/artifact: `artifacts/ops/internal_version/body_get.json`; Covered hunks: OPR-044; Combined merged state: six-field body capture current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: contract tests passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: approved rescope/PF14 drain candidate.

NET-045 â€” File/artifact: `artifacts/ops/internal_version/body_get.json.path_proof.txt`; Covered hunks: OPR-045; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-046 â€” File/artifact: `artifacts/ops/internal_version/body_get.sha256`; Covered hunks: OPR-046; Combined merged state: checksum current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-047 â€” File/artifact: `artifacts/ops/internal_version/body_get.sha256.path_proof.txt`; Covered hunks: OPR-047; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-048 â€” File/artifact: `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`; Covered hunks: OPR-048; Combined merged state: deleted; Current final repo state: absent; Later-change impact: None; Risk: High; High-risk hunk assessment: canonical replacement path exists and all retained references were migrated; Assessment: valid deletion; Evidence pointer(s): OPR-052 and historical binding changes; GitHub Repo proof: lifecycle compare status `removed`; PF reference: approved rescope Â§7.

NET-049 â€” File/artifact: `artifacts/ops/internal_version/cond_if_modified_since_headers.txt.path_proof.txt`; Covered hunks: OPR-049; Combined merged state: deleted; Current final repo state: absent; Later-change impact: None; Risk: High; Assessment: valid companion deletion; Evidence pointer(s): OPR-048; GitHub Repo proof: status `removed`; PF reference: PF12.

NET-050 â€” File/artifact: `artifacts/ops/internal_version/cond_if_none_match_headers.txt`; Covered hunks: OPR-050; Combined merged state: deleted; Current final repo state: absent; Later-change impact: None; Risk: High; Assessment: canonical replacement exists; Evidence pointer(s): OPR-054; GitHub Repo proof: status `removed`; PF reference: approved rescope Â§7.

NET-051 â€” File/artifact: `artifacts/ops/internal_version/cond_if_none_match_headers.txt.path_proof.txt`; Covered hunks: OPR-051; Combined merged state: deleted; Current final repo state: absent; Later-change impact: None; Risk: High; Assessment: valid companion deletion; Evidence pointer(s): OPR-050; GitHub Repo proof: status `removed`; PF reference: PF12.

NET-052 â€” File/artifact: `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`; Covered hunks: OPR-052; Combined merged state: canonical retained capture; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: contract tests passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF05/PF04.

NET-053 â€” File/artifact: `artifacts/ops/internal_version/headers_cond_if_modified_since.txt.path_proof.txt`; Covered hunks: OPR-053; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-054 â€” File/artifact: `artifacts/ops/internal_version/headers_cond_if_none_match.txt`; Covered hunks: OPR-054; Combined merged state: canonical retained capture; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: contract tests passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF05/PF04.

NET-055 â€” File/artifact: `artifacts/ops/internal_version/headers_cond_if_none_match.txt.path_proof.txt`; Covered hunks: OPR-055; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-056 â€” File/artifact: `artifacts/ops/internal_version/headers_get.txt`; Covered hunks: OPR-056; Combined merged state: GET headers current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: no-store/no-ETag contract tests passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF04/PF05.

NET-057 â€” File/artifact: `artifacts/ops/internal_version/headers_get.txt.path_proof.txt`; Covered hunks: OPR-057; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-058 â€” File/artifact: `artifacts/ops/internal_version/headers_head.txt`; Covered hunks: OPR-058; Combined merged state: HEAD headers current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: parity tests passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF04/PF05.

NET-059 â€” File/artifact: `artifacts/ops/internal_version/headers_head.txt.path_proof.txt`; Covered hunks: OPR-059; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-060 â€” File/artifact: `artifacts/ops/internal_version/request_chain_manifest.json`; Covered hunks: OPR-060; Combined merged state: canonical capture bindings current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: manifest capture tests passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-061 â€” File/artifact: `artifacts/ops/internal_version/request_chain_manifest.json.path_proof.txt`; Covered hunks: OPR-061; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-062 â€” File/artifact: `artifacts/ops/internal_version/two_run_identity.log`; Covered hunks: OPR-062; Combined merged state: independent two-run evidence current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: identity tests passed; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-063 â€” File/artifact: `artifacts/ops/internal_version/two_run_identity.log.path_proof.txt`; Covered hunks: OPR-063; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-064 â€” File/artifact: `artifacts/parity/two_run_identity.log`; Covered hunks: OPR-064; Combined merged state: public/admin identity independently rendered twice; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: two-run test and closure passed; Evidence pointer(s): Original PR generator/test; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-065 â€” File/artifact: `artifacts/parity/two_run_identity.log.path_proof.txt`; Covered hunks: OPR-065; Combined merged state: proof exists; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-066 â€” File/artifact: `artifacts/runtime/env_matrix.snapshot.json`; Covered hunks: OPR-066; Combined merged state: deterministic schema-v3 singleton; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: exact shape, no secret values, migrated writers/consumers, and check mode passed; Assessment: requirement satisfied; Evidence pointer(s): env generator/test/CI; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST003.1.

NET-067 â€” File/artifact: `artifacts/runtime/env_matrix.snapshot.json.path_proof.txt`; Covered hunks: OPR-067; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-068 â€” File/artifact: `artifacts/writer/conjunction_write_readback.log`; Covered hunks: OPR-068; Combined merged state: writer/readback evidence regenerated by Original PR; Remedial PR leaves bytes unchanged; Current final repo state: all checks true; Later-change impact: None; Risk: High; High-risk hunk assessment: Remedial regression proves `--check` cannot connect to DB while preserving these bytes; Assessment: coherent; Evidence pointer(s): RPR-001/RPR-002, current artifact. ; GitHub Repo proof: Remedial PR changed no artifact; PF reference: PF19 drain candidate.

NET-069 â€” File/artifact: `artifacts/writer/conjunction_write_readback.log.path_proof.txt`; Covered hunks: OPR-069; Combined merged state: proof refreshed by Original PR; Current final repo state: unchanged by remediation; Later-change impact: None; Risk: High; Assessment: byte-neutral remediation required no proof refresh; Evidence pointer(s): Remedial changed-file list; GitHub Repo proof: only two source/test files changed; PF reference: PF12.

NET-070 â€” File/artifact: `artifacts/writer/conjunction_writer_summary.json`; Covered hunks: OPR-070; Combined merged state: all writer/readback and identity checks true; Current final repo state: unchanged; Later-change impact: None; Risk: High; Assessment: byte-neutral safety repair preserved evidence; Evidence pointer(s): current artifact. ; GitHub Repo proof: not in Remedial PR changed-file list; PF reference: PF12.

NET-071 â€” File/artifact: `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; Covered hunks: OPR-071; Combined merged state: proof refreshed by Original PR; Current final repo state: unchanged; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Remedial changed-file list; GitHub Repo proof: no later change; PF reference: PF12.

NET-072 â€” File/artifact: `audit/EPIC-022_close_report.md`; Covered hunks: OPR-072; Combined merged state: historical evidence pointers corrected; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: coherence maintenance only; Evidence pointer(s): approved rescope Â§7; GitHub Repo proof: no later change; PF reference: PF06.

NET-073 â€” File/artifact: `audit/EPIC-022_close_report.md.path_proof.txt`; Covered hunks: OPR-073; Combined merged state: proof refreshed; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-074 â€” File/artifact: `audit/gates/canonical_json/canonical_json.gate.json`; Covered hunks: OPR-074; Combined merged state: deterministic gate summary current; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: current check-only code compares committed bytes; Assessment: stale-gate gap closed; Evidence pointer(s): current gate tool lines 142-173; GitHub Repo proof: no later change. ; PF reference: PF12.

NET-075 â€” File/artifact: `audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt`; Covered hunks: OPR-075; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-076 â€” File/artifact: `audit/gates/canonical_json/json_canon_compare.log`; Covered hunks: OPR-076; Combined merged state: deterministic compare records current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: closure check passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-077 â€” File/artifact: `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`; Covered hunks: OPR-077; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-078 â€” File/artifact: `audit/gates/canonical_json/json_canonical_check.log`; Covered hunks: OPR-078; Combined merged state: deterministic check records current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: closure check passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-079 â€” File/artifact: `audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`; Covered hunks: OPR-079; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-080 â€” File/artifact: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`; Covered hunks: OPR-080; Combined merged state: structured check records current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: committed-output check passed; Evidence pointer(s): current gate code; GitHub Repo proof: no later change; PF reference: PF12.

NET-081 â€” File/artifact: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`; Covered hunks: OPR-081; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-082 â€” File/artifact: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`; Covered hunks: OPR-082; Combined merged state: structured comparison records current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: closure passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-083 â€” File/artifact: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`; Covered hunks: OPR-083; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-084 â€” File/artifact: `audit/gates/json_gate/canonical/json_gate_structured_record.json`; Covered hunks: OPR-084; Combined merged state: structured result current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: closure passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-085 â€” File/artifact: `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`; Covered hunks: OPR-085; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-086 â€” File/artifact: `audit/gates/topology/orientation_demo.txt`; Covered hunks: OPR-086; Combined merged state: orientation current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: orientation check passed in both final runs; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-087 â€” File/artifact: `audit/gates/topology/orientation_demo.txt.path_proof.txt`; Covered hunks: OPR-087; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-088 â€” File/artifact: `audit/qa/hde-epic022/token_evidence_matrix.md`; Covered hunks: OPR-088; Combined merged state: historical path references corrected; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: no new token satisfaction is claimed; Assessment: coherence maintenance; Evidence pointer(s): approved rescope Â§7; GitHub Repo proof: no later change; PF reference: PF06.

NET-089 â€” File/artifact: `audit/qa/hde-epic022/token_evidence_matrix.md.path_proof.txt`; Covered hunks: OPR-089; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-090 â€” File/artifact: `catalog/manifest.json`; Covered hunks: OPR-090; Combined merged state: canonical manifest refreshed for changed frozen file bytes; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: release recompute and closure checks passed; Assessment: coherent; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF12 Â§6.

NET-091 â€” File/artifact: `docs/EVIDENCE_INDEX.md`; Covered hunks: OPR-091; Combined merged state: navigation current; Current final repo state: same; Later-change impact: None; Risk: Low; Assessment: no executable effect; Evidence pointer(s): Original PR compare; GitHub Repo proof: no later change; PF reference: None.

NET-092 â€” File/artifact: `docs/INDEX.md`; Covered hunks: OPR-092; Combined merged state: navigation current; Current final repo state: same; Later-change impact: None; Risk: Low; Assessment: no executable effect; Evidence pointer(s): Original PR compare; GitHub Repo proof: no later change; PF reference: None.

NET-093 â€” File/artifact: `docs/acceptance_map_epic022.json`; Covered hunks: OPR-093; Combined merged state: historical canonical evidence paths corrected; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: no earlier acceptance outcome was altered; Assessment: approved coherence maintenance; Evidence pointer(s): approved rescope Â§7; GitHub Repo proof: no later change; PF reference: PF06/PF12.

NET-094 â€” File/artifact: `docs/acceptance_map_epic022.json.path_proof.txt`; Covered hunks: OPR-094; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): Original PR CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-095 â€” File/artifact: `docs/evidence/INDEX.json`; Covered hunks: OPR-095; Combined merged state: Human Index current; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: updater, hash, Mirror, path, and orientation checks passed; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12 Human Evidence Index.

NET-096 â€” File/artifact: `docs/evidence/INDEX.json.path_proof.txt`; Covered hunks: OPR-096; Combined merged state: proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-097 â€” File/artifact: `docs/evidence/INDEX.sha256`; Covered hunks: OPR-097; Combined merged state: sentinel current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: hash check passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-098 â€” File/artifact: `docs/evidence/INDEX.sha256.path_proof.txt`; Covered hunks: OPR-098; Combined merged state: sentinel proof current; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherent; Evidence pointer(s): VAL-012; GitHub Repo proof: no later change; PF reference: PF12.

NET-099 â€” File/artifact: `engine/cli/main.py`; Covered hunks: OPR-099; Combined merged state: CLI identity env reads replaced by approved shared helper; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: CLI byte and showcompat parity tests passed; Assessment: contract preserved; Evidence pointer(s): Original PR CI/current showcompat generator; GitHub Repo proof: no later change; PF reference: approved rescope Â§5.

NET-100 â€” File/artifact: `engine/compat/identity.py`; Covered hunks: OPR-100; Combined merged state: bounded dev compatibility identity exists; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: consumers remain bounded to approved dev/compat surfaces; Assessment: approved architecture; Evidence pointer(s): Extra Evidence Â§Â§3.1, 5.2; GitHub Repo proof: no later change; PF reference: PF14 Doc Delta candidate.

NET-101 â€” File/artifact: `engine/http/compat_handler.py`; Covered hunks: OPR-101; Combined merged state: compat route uses bounded dev profile; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: compat HTTP lane passed in both workflows; Assessment: contract preserved; Evidence pointer(s): VAL-006/VAL-007; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-102 â€” File/artifact: `engine/runtime/__init__.py`; Covered hunks: OPR-102; Combined merged state: identity helpers exported; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: correct; Evidence pointer(s): Original PR patch; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-103 â€” File/artifact: `engine/runtime/identity.py`; Covered hunks: OPR-103; Combined merged state: immutable production identity authority exists; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: six-field, unknown/missing-key, immutability, and helper tests passed; Assessment: approved architecture; Evidence pointer(s): Original PR patch/tests/Extra Evidence; GitHub Repo proof: no later change; PF reference: approved rescope Â§5.1 and PF14 drainage candidate.

NET-104 â€” File/artifact: `engine/runtime/public.py`; Covered hunks: OPR-104; Combined merged state: immutable defaults plus sanctioned injection seam; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: production defaults do not originate from requests or identity env keys; injection compatibility tests passed; Assessment: approved architecture; Evidence pointer(s): OPR-104/Extra Evidence Â§5.3; GitHub Repo proof: no later change; PF reference: PF14 drainage candidate.

NET-105 â€” File/artifact: `glow_hdengine.egg-info/PKG-INFO`; Covered hunks: OPR-105; Combined merged state: generated package metadata current; Current final repo state: same; Later-change impact: None; Risk: Low; Assessment: coherent; Evidence pointer(s): Original PR compare; GitHub Repo proof: no later change; PF reference: None.

NET-106 â€” File/artifact: `glow_hdengine.egg-info/SOURCES.txt`; Covered hunks: OPR-106; Combined merged state: new modules/tests included; Current final repo state: same; Later-change impact: None; Risk: Low; Assessment: coherent; Evidence pointer(s): Original PR compare; GitHub Repo proof: no later change; PF reference: None.

NET-107 â€” File/artifact: `scripts/ingest/run_vendor_ingest.py`; Covered hunks: OPR-107; Combined merged state: duplicate env-snapshot writer removed; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: focused singleton-consumer test verifies no writer remains; Assessment: atomic migration complete; Evidence pointer(s): env-v3 test/CI; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST003.1.

NET-108 â€” File/artifact: `scripts/qa/epic009_precommit.sh`; Covered hunks: OPR-108; Combined merged state: legacy consumer uses v3 check; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: focused test passed; Evidence pointer(s): env-v3 test/CI; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST003.1.

NET-109 â€” File/artifact: `scripts/release_id_recompute.py`; Covered hunks: OPR-109; Combined merged state: check mode renders and compares all governed release outputs without writing; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: stale logs, checksums, manifest copy, release text, env pins, and snapshot are covered; Assessment: verification gap closed; Evidence pointer(s): OPR-109 and CI; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST002.

NET-110 â€” File/artifact: `tests/adapter/test_env_guard_forbidden_matrix.py`; Covered hunks: OPR-110; Combined merged state: approved rail matrix tested; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: sufficient; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF07.

NET-111 â€” File/artifact: `tests/adapter/test_env_guard_prod_variants.py`; Covered hunks: OPR-111; Combined merged state: production aliases tested; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: sufficient; Evidence pointer(s): CI; GitHub Repo proof: no later change; PF reference: PF07.

NET-112 â€” File/artifact: `tests/adapter/test_env_guard_silence_and_idempotence.py`; Covered hunks: OPR-112; Combined merged state: guard idempotence retained; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: sufficient; Evidence pointer(s): CI; GitHub Repo proof: no later change; PF reference: PF07.

NET-113 â€” File/artifact: `tests/adapter/test_gate_auth.py`; Covered hunks: OPR-113; Combined merged state: internal-version and gate behavior tested; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: transport/auth regression coverage passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF04/PF05.

NET-114 â€” File/artifact: `tests/cli/test_cli_canonical_bytes.py`; Covered hunks: OPR-114; Combined merged state: obsolete identity-env assumptions removed; Current final repo state: same; Later-change impact: None; Risk: Medium; High-risk hunk assessment: replacement identity/parity tests exist and full CLI/evidence suite passed; Assessment: no coverage gap; Evidence pointer(s): NET-115/127 and CI; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-115 â€” File/artifact: `tests/cli/test_showcompat_parity_and_identity.py`; Covered hunks: OPR-115; Combined merged state: expanded immutable identity/parity coverage; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-116 â€” File/artifact: `tests/evidence/test_aux_preview_identity_parity.py`; Covered hunks: OPR-116; Combined merged state: Aux immutable release parity covered; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed; Evidence pointer(s): closure test lane; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-117 â€” File/artifact: `tests/evidence/test_canonical_json_gate_check_outputs.py`; Covered hunks: OPR-117; Combined merged state: stale committed gate outputs fail check; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF19/PF12.

NET-118 â€” File/artifact: `tests/evidence/test_cli_conformance_artifacts.py`; Covered hunks: OPR-118; Combined merged state: CLI evidence and real-console probe covered; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed; Evidence pointer(s): Original/Remedial evidence suite; GitHub Repo proof: no later change; PF reference: PF19.

NET-119 â€” File/artifact: `tests/evidence/test_dev_conjunction_identity.py`; Covered hunks: OPR-119 / RPR-001; Combined merged state: Original artifact-byte/dev-identity checks plus remedial DB-connect interception and restoration tests; Current final repo state: 96-line final test file; Later-change impact: None; Risk: High; High-risk hunk assessment: the original insufficient test gap is closed by direct behavioral interception; Assessment: sufficient; Evidence pointer(s): current lines 31-96. ; GitHub Repo proof: Remedial PR final file; PF reference: PF19 Doc Delta candidate.

NET-120 â€” File/artifact: `tests/evidence/test_env_matrix_snapshot_v3.py`; Covered hunks: OPR-120; Combined merged state: exact v3, singleton, migration, and no-secret checks; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed; Evidence pointer(s): Original/Remedial evidence suite; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST003.1.

NET-121 â€” File/artifact: `tests/evidence/test_identity_provenance.py`; Covered hunks: OPR-121; Combined merged state: provenance and independent-run checks; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: accepted under rescope and passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: approved rescope/PF14 candidate.

NET-122 â€” File/artifact: `tests/evidence/test_internal_version_manifest_captures.py`; Covered hunks: OPR-122; Combined merged state: canonical capture names and bindings tested; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed; Evidence pointer(s): closure lane; GitHub Repo proof: no later change; PF reference: PF12.

NET-123 â€” File/artifact: `tests/evidence/test_release_bindings.py`; Covered hunks: OPR-123; Combined merged state: approved release-binding renderer/check covered; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed under approved rescope; Evidence pointer(s): Original/Remedial evidence suite; GitHub Repo proof: no later change; PF reference: PF12 drainage candidate.

NET-124 â€” File/artifact: `tests/evidence/test_release_manifest_content_binding.py`; Covered hunks: OPR-124; Combined merged state: manifest content and check-mode behavior comprehensively tested; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST002.

NET-125 â€” File/artifact: `tests/http/test_dev_conjunction_http.py`; Covered hunks: OPR-125; Combined merged state: normal dev writer/reader HTTP behavior tested; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: Remedial PR did not alter route code and this suite passed after remediation; Assessment: no regression; Evidence pointer(s): Remedial PR body/CI; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-126 â€” File/artifact: `tests/qa/test_epic022_acceptance_scaffold.py`; Covered hunks: OPR-126; Combined merged state: historical canonical paths tested; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: coherence-only update; Evidence pointer(s): approved rescope Â§7 and closure CI; GitHub Repo proof: no later change; PF reference: PF06.

NET-127 â€” File/artifact: `tests/runtime/test_identity.py`; Covered hunks: OPR-127; Combined merged state: identity shape, immutability, helper, source, and injection coverage; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed under approved architecture; Evidence pointer(s): Original/Remedial evidence suite; GitHub Repo proof: no later change; PF reference: PF14 drainage candidate.

NET-128 â€” File/artifact: `tests/transport/test_internal_version_contract.py`; Covered hunks: OPR-128; Combined merged state: internal-version transport and identity behavior covered; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: passed; Evidence pointer(s): closure and CI; GitHub Repo proof: no later change; PF reference: PF04/PF05/PF14.

NET-129 â€” File/artifact: `tools/cli/emitter_symbol_proof.py`; Covered hunks: OPR-129; Combined merged state: topology proof updated; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: valid supporting proof; Evidence pointer(s): CI step passed; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-130 â€” File/artifact: `tools/cli/generate_cli_conformance_artifacts.py`; Covered hunks: OPR-130; Combined merged state: deterministic, offline, real-console-aware CLI evidence generation/check; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: evidence tests and closure passed; Evidence pointer(s): Original/Remedial CI; GitHub Repo proof: no later change; PF reference: PF19 drainage candidate.

NET-131 â€” File/artifact: `tools/cli/generate_showcompat_artifacts.py`; Covered hunks: OPR-131; Combined merged state: active interpreter, immutable identity, and committed-output comparison; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: original review gap closed; Evidence pointer(s): current file lines 59-125. ; GitHub Repo proof: no later change; PF reference: approved rescope.

NET-132 â€” File/artifact: `tools/cli/serializer_grep_guard.py`; Covered hunks: OPR-132; Combined merged state: guard aligned with current path; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: passed; Evidence pointer(s): CI; GitHub Repo proof: no later change; PF reference: PF14.

NET-133 â€” File/artifact: `tools/evidence/generate_conjunction_writer_evidence.py`; Covered hunks: OPR-133 / RPR-002; Combined merged state: deterministic writer/readback renderer/check plus remedial non-persistent check boundary; Current final repo state: `--check` removes DATABASE\_URL around capture and restores it in `finally`; Later-change impact: None; Risk: High; High-risk hunk assessment: direct DB trigger is impossible in check mode because `_persist_idempotence_db` returns before import/connect when DATABASE\_URL is absent; write mode remains unchanged; Assessment: original blocker closed. ; Evidence pointer(s): RPR-002, VAL-009, VAL-010; GitHub Repo proof: current raw file; PF reference: PF19 drainage candidate.

NET-134 â€” File/artifact: `tools/evidence/generate_env_matrix_snapshot.py`; Covered hunks: OPR-134; Combined merged state: deterministic v3 singleton renderer/check; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: focused tests and closure passed; Evidence pointer(s): OPR-134, NET-120; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST003.1.

NET-135 â€” File/artifact: `tools/evidence/generate_epic032_pr01_router_evidence.py`; Covered hunks: OPR-135; Combined merged state: dependency evidence aligned with immutable release identity; Current final repo state: same; Later-change impact: None; Risk: Medium; Assessment: approved dependency validation only; Evidence pointer(s): approved rescope Â§7; GitHub Repo proof: no later change; PF reference: PF06.

NET-136 â€” File/artifact: `tools/evidence/generate_identity_provenance.py`; Covered hunks: OPR-136; Combined merged state: deterministic identity family renderer/check with independent two-run collection; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: accepted architecture and tests passed; Evidence pointer(s): OPR-136, Original/Remedial CI; GitHub Repo proof: no later change; PF reference: approved rescope/PF14 candidate.

NET-137 â€” File/artifact: `tools/evidence/generate_rails_closed_phase1.py`; Covered hunks: OPR-137; Combined merged state: delegates singleton production; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: atomic migration complete; Evidence pointer(s): NET-120; GitHub Repo proof: no later change; PF reference: PF09.6 HDE-DIST003.1.

NET-138 â€” File/artifact: `tools/evidence/generate_release_bindings.py`; Covered hunks: OPR-138; Combined merged state: deterministic approved release-binding renderer/check; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: accepted by rescope and tests passed; Evidence pointer(s): OPR-138, NET-123; GitHub Repo proof: no later change; PF reference: PF12 drainage candidate.

NET-139 â€” File/artifact: `tools/evidence/regenerate_identity_closure.py`; Covered hunks: OPR-139; Combined merged state: bounded PR-01 closure orchestration; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: both final workflow runs passed the committed-closure step; PR-02 through PR-06 boundaries remain explicit; Assessment: coherent; Evidence pointer(s): current file and CI; GitHub Repo proof: no later change; PF reference: approved rescope Â§5.5.

NET-140 â€” File/artifact: `tools/evidence/run_canonical_json_gate.py`; Covered hunks: OPR-140; Combined merged state: check-only validates targets and committed gate artifacts; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: stale-output gap closed; Evidence pointer(s): current lines 142-173 and CI; GitHub Repo proof: no later change; PF reference: PF19/PF12.

NET-141 â€” File/artifact: `tools/evidence/update_evidence_index.py`; Covered hunks: OPR-141; Combined merged state: canonical writer registers PR-01 primaries; Current final repo state: same; Later-change impact: None; Risk: High; High-risk hunk assessment: updater remains sole Index/Mirror/proof writer for affected artifacts; check passed in both final runs; Assessment: coherent; Evidence pointer(s): Original PR body and CI; GitHub Repo proof: no later change; PF reference: PF12.

NET-142 â€” File/artifact: `tools/ops/internal_version_artifacts.py`; Covered hunks: OPR-142; Combined merged state: canonical conditional capture names and request-chain handling; Current final repo state: same; Later-change impact: None; Risk: High; Assessment: capture tests and closure passed; Evidence pointer(s): NET-122/128; GitHub Repo proof: no later change; PF reference: PF12/PF14 drainage candidates.

### Validation & Evidence Review

VAL-001

Purpose: Prove both requested PR identities and merged state.

Source: Original PR / Remedial PR

Check/workflow/artifact/method: GitHub PR metadata.

Result: PASS

Observation: Original PR and Remedial PR are both closed and merged, with exact base, head, and merge identifiers available.

Evidence pointer: Original PR | API fields | `"merged=true"` | `"merge_commit_sha=f07ffbeb..."`; Remedial PR | API fields | `"merged=true"` | `"merge_commit_sha=df662b..."`

Why it matters: The lifecycle is reviewable as two merged attempts.

VAL-002

Purpose: Prove lifecycle order and lineage.

Source: GitHub Repo

Check/workflow/artifact/method: base/head comparison and PR base fields.

Result: PASS

Observation: Remedial PR base equals Original PR merge commit exactly; baseline-to-current is two commits ahead and zero behind.

Evidence pointer: GitHub Repo | compare | `"ahead_by=2"` | `"behind_by=0"`

Why it matters: Remedial PR is a direct correction of Original PR rather than an unrelated change.

VAL-003

Purpose: Establish Original PR change-set completeness.

Source: Original PR

Check/workflow/artifact/method: PR changed-file list, base-to-merge comparison, per-file patches, merged commit diff.

Result: PASS

Observation: 142 changed files were identified and each appears once in the OPR ledger and once in the NET review.

Evidence pointer: Original PR | API | `"changed_files=142"` | `"additions=2388; deletions=749"`

Why it matters: No Original PR touched file is omitted.

VAL-004

Purpose: Establish Remedial PR change-set completeness.

Source: Remedial PR

Check/workflow/artifact/method: PR changed-file list and complete two-file patch.

Result: PASS

Observation: Only the generator and its focused test changed.

Evidence pointer: Remedial PR | API and patch | `"changed_files=2"` | `"additions=63; deletions=1"`

Why it matters: Remediation introduced no unrelated drift.

VAL-005

Purpose: Establish current-state fidelity.

Source: GitHub Repo

Check/workflow/artifact/method: default-branch commit history and lifecycle comparison.

Result: PASS

Observation: Current `main` is Remedial PR merge commit; no later commits exist.

Evidence pointer: GitHub Repo | current commit search | `"df662b518f0290a4bae6b26fb0332b374f28116a"` | `"previous=f07ffbeb..."`

Why it matters: Current final state is the reviewed combined state.

VAL-006

Purpose: Verify Original PR automated validation.

Source: Original PR

Check/workflow/artifact/method: GitHub Actions run `29191942424`.

Result: PASS

Observation: All returned jobs completed successfully.

Evidence pointer: Original PR | workflow | `"conclusion=success"` | `"Verify committed closure before any write-capable QA=success"`

Why it matters: Original implementation and evidence graph were internally coherent apart from the separately identified external-state check defect.

VAL-007

Purpose: Verify Remedial PR automated validation.

Source: Remedial PR

Check/workflow/artifact/method: GitHub Actions run `29206555501`.

Result: PASS

Observation: Test, sanity, compatibility, evidence, acceptance, and conjunction lanes all completed successfully.

Evidence pointer: Remedial PR | workflow | `"conclusion=success"` | `"tests/evidence=success"`

Why it matters: The final correction passed the retained global safeguards.

VAL-008

Purpose: Verify the Original PR safety gap was real and bounded.

Source: Original PR / GitHub Repo

Check/workflow/artifact/method: Original generator patch and current persistence call path.

Result: FAIL for Original merged state

Observation: Original `--check` called `_capture_outputs()` before branching, and the writer route could reach `psycopg.connect` and `INSERT INTO hde.idempotent_writes` when `DATABASE_URL` was present.

Evidence pointer: Original PR | generator patch | `"expected = _capture_outputs()"` | `"if args.check"`; GitHub Repo | `adapter/http_reader.py` | `"psycopg.connect"` | `"INSERT INTO hde.idempotent_writes"`

Why it matters: This was the precise reason remediation was required.

VAL-009

Purpose: Verify the final check path cannot reach DB persistence.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: static call-path proof.

Result: PASS

Observation: `--check` removes `DATABASE_URL` before `_capture_outputs()`. `_persist_idempotence_db()` returns `False` before importing `psycopg` when the key is absent.

Evidence pointer: Remedial PR | current generator | `"os.environ.pop(\"DATABASE_URL\", None)"` | `"with _non_persistent_check_capture()"`; GitHub Repo | persistence helper | `"if not dsn: return False"` | `"import psycopg"` after that branch.

Why it matters: The external-state mutation path is structurally cut off.

VAL-010

Purpose: Verify behavioral regression coverage.

Source: Remedial PR

Check/workflow/artifact/method: focused in-process test.

Result: PASS

Observation: The test supplies a non-empty sentinel DSN, installs a `psycopg.connect` function that fails if called, runs check mode, proves zero calls, proves artifact bytes unchanged, and proves restoration on success and exception.

Evidence pointer: Remedial PR | `tests/evidence/test_dev_conjunction_identity.py` | `"sentinel_dsn"` | `"assert connect_calls == []"`

Why it matters: The safety property is tested directly rather than inferred from file cleanliness.

VAL-011

Purpose: Verify normal dev writer behavior was preserved.

Source: Remedial PR

Check/workflow/artifact/method: diff scope and HTTP regression lane.

Result: PASS

Observation: No route or persistence implementation changed; `tests/http/test_dev_conjunction_http.py` passed in the remedial workflow.

Evidence pointer: Remedial PR | changed-file list | `"2 files"` | `"no adapter/http_reader.py"`; Remedial PR | workflow | `"EPIC020 compat HTTP coverage=success"`

Why it matters: The correction does not disable legitimate non-check behavior.

VAL-012

Purpose: Verify governed evidence coherence.

Source: Original PR / Remedial PR / GitHub Repo

Check/workflow/artifact/method: Index updater check, orientation check, Mirror schema, Evidence Index hash, final LF, path validation, current artifacts.

Result: PASS

Observation: All visible checks passed; Remedial PR was byte-neutral for governed artifacts.

Evidence pointer: Remedial PR | workflow steps | `"update_evidence_index.py --check=success"` | `"check_mirror_schema.sh=success"`

Why it matters: Remediation did not create stale governed bindings.

VAL-013

Purpose: Verify current writer artifacts remain truthful.

Source: GitHub Repo

Check/workflow/artifact/method: current raw artifact inspection.

Result: PASS

Observation: Writer and Reader status, two-run equality, readback parity, typed envelopes, and dev identity checks are true.

Evidence pointer: GitHub Repo | writer log/summary | `"writer_bytes_two_run_equal=true"` | `"reader_dev_identity=true"`

Why it matters: The safety fix did not invalidate the proof target.

VAL-014

Purpose: Verify approved scope and architecture authority.

Source: Extra Evidence

Check/workflow/artifact/method: complete approved rescope review.

Result: PASS

Observation: The rescope explicitly accepts the broadened PR-01 architecture and defines remaining PR boundaries and nonclaims.

Evidence pointer: Extra Evidence | Â§Â§1, 5, 6, 10, 12 | `"Approval status: APPROVED"` | `"merged implementation is accepted as the approved PR-01 repository outcome"`

Why it matters: Older conflicting PF language is a drainage target rather than a code rollback requirement for this bounded decision.

VAL-015

Purpose: Verify PF10 posture.

Source: PF10

Check/workflow/artifact/method: complete latest PF10 inspection.

Result: PASS

Observation: Latest PF10 contains no active numbered addendum for PR-01; the approved Product Owner rescope supplies the bounded decision, and permanent PF drainage remains separate.

Evidence pointer: PF10 | Â§2 Numbered Addenda | `"<eof>"` | `"This file contains only live items"`

Why it matters: No competing live PF10 entry overrides the approved rescope.

VAL-016

Purpose: Verify no PF23 authority was used.

Source: Review method

Check/workflow/artifact/method: source and citation audit.

Result: PASS

Observation: PF23 supplied no requirement, blocker, token, current-repo fact, or acceptance proof in this review.

Search method: searched report evidence pointers for `PF23` authority use (case: sensitive); scope: this reviewâ€™s requirement, validation, PF09, and decision bases; tool: manual scan; result: 0 authority uses.

Why it matters: PR analysis remains within the userâ€™s source boundary.

VAL-017

Purpose: Verify independent local execution by this reviewer.

Source: Reviewer environment

Check/workflow/artifact/method: local checkout availability.

Result: NOT RUN

Observation: No local checkout was available. No local command is claimed.

Evidence pointer: Reviewer method | GitHub-only inspection | `"no local mutation"` | `"no local command claim"`

Why it matters: This is non-blocking because complete GitHub lineage, current raw files, focused behavioral tests, and successful final CI are available.

### Requirement Satisfaction Crosswalk

REQ-001

Requirement: Create one immutable validated six-field production identity authority.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Implementation Doc | PR-01 requirement 1 | `"exactly engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id"`; Original PR | `engine/runtime/identity.py`; Extra Evidence | approved production identity authority.

GitHub Repo proof, if current state matters: current file remains unchanged after Remedial PR.

PF09 task/subtask IDs, if proven: HDE-DIST006.1

REQ-002

Requirement: Reject missing/unknown identity fields, initialize once, and prohibit mutation.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | identity validation/test | `"identity_missing_fields"` | `"identity_conflicting_reinitialization"`

GitHub Repo proof, if current state matters: identity tests passed in both final workflow contexts.

PF09 task/subtask IDs, if proven: HDE-DIST006.1

REQ-003

Requirement: Remove production request-time identity environment reads and runtime evidence-root identity inputs.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | Reader/CLI/internal-version refactor and static checks | `"identity_meta"` | `"identity_admin"`

GitHub Repo proof, if current state matters: current Reader and CLI paths use helpers; Remedial PR did not alter them.

PF09 task/subtask IDs, if proven: HDE-DIST006.1, HDE-DIST006.2

REQ-004

Requirement: Preserve the approved distinction between production identity and bounded dev compatibility identity.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Extra Evidence | Â§Â§3.1, 5.1, 5.2 | `"not a second production identity authority"` | `"authorized only for explicitly non-production compatibility and dev harnesses"`

GitHub Repo proof, if current state matters: `engine/compat/identity.py` remains unchanged after Remedial PR.

PF09 task/subtask IDs, if proven: HDE-DIST006.1, HDE-DIST006.2

REQ-005

Requirement: Preserve sanctioned injected-emitter identity keyword compatibility without request-controlled identity discovery.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Extra Evidence | Â§Â§3.2 and 5.3 | `"compatibility and testing seam"` | `"must not originate from request parameters"`; Original PR | `engine/runtime/public.py`.

GitHub Repo proof, if current state matters: current runtime defaults to immutable identity and retains optional composition arguments.

PF09 task/subtask IDs, if proven: HDE-DIST006.2

REQ-006

Requirement: Export identity helpers while preserving Reader emitter exports.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | `engine/runtime/__init__.py` | `"identity_admin"` | `"emit_reader_public_bytes"`

GitHub Repo proof, if current state matters: no later change.

PF09 task/subtask IDs, if proven: HDE-DIST006.2

REQ-007

Requirement: Route Reader and `/internal/version` through shared identity while preserving transport behavior.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | adapter patch; Original/Remedial CI | transport tests.

GitHub Repo proof, if current state matters: current adapter uses `identity_meta()` and `identity_admin()`.

PF09 task/subtask IDs, if proven: HDE-DIST006.2

REQ-008

Requirement: Replace CLI identity env reads with shared helper and preserve CLI output/stream contracts.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | `engine/cli/main.py`; current showcompat generator; CLI CI lanes.

GitHub Repo proof, if current state matters: current generator verifies output metadata equals immutable identity.

PF09 task/subtask IDs, if proven: HDE-DIST006.2

REQ-009

Requirement: Generate deterministic identity provenance artifacts and exact six-field service identity with non-writing check mode.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | provenance generator/test | `"service_run1"` | `"DRIFT:"`; Original PR CI.

GitHub Repo proof, if current state matters: generator and artifacts unchanged after Remedial PR.

PF09 task/subtask IDs, if proven: HDE-DIST006.1, HDE-DIST006.3

REQ-010

Requirement: Produce independent two-run identity evidence.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | provenance generator | `"service_run1 = _identity_bytes()"` | `"service_run2 = _identity_bytes()"`

GitHub Repo proof, if current state matters: two-run artifacts and tests remain current.

PF09 task/subtask IDs, if proven: HDE-DIST006.2

REQ-011

Requirement: Generate deterministic BodyGraph release bindings and check mode.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | release-binding generator/test; Extra Evidence | approved retained release-binding architecture.

GitHub Repo proof, if current state matters: artifact, test, Index, Mirror, and proof remain in current state.

PF09 task/subtask IDs, if proven: HDE-DIST002.5

REQ-012

Requirement: Derive and index canonical release identity and manifest evidence.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | release recompute tool/artifacts/tests | `"release_id = sha256(canonical manifest bytes)"` | `"--check"`.

GitHub Repo proof, if current state matters: release and closure checks passed after remediation.

PF09 task/subtask IDs, if proven: HDE-DIST002.4

REQ-013

Requirement: Migrate the environment snapshot to deterministic schema version 3 singleton with presence-only secret posture.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | env generator, artifact, focused tests | `"schema_version": 3` | `"PRESENCE"`.

GitHub Repo proof, if current state matters: duplicate writer removed; consumers delegate; final evidence suite passed.

PF09 task/subtask IDs, if proven: HDE-DIST003.1

REQ-014

Requirement: Update Human Index, hash sentinel, Machine Mirror, checksum, and sibling proofs through the canonical updater.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | updater registration and generated ledgers; workflow checks.

GitHub Repo proof, if current state matters: Remedial PR changed no governed evidence and all check modes passed.

PF09 task/subtask IDs, if proven: HDE-DIST005.2, HDE-DIST002.4, HDE-DIST002.5, HDE-DIST003.4, HDE-DIST006.3

REQ-015

Requirement: Preserve no-new-public-endpoint, no Reader payload expansion, no runtime vendor-call, and no second HTTP-home boundaries.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Implementation Doc | exclusions; Extra Evidence | approval limitations; Original PR file review.

GitHub Repo proof, if current state matters: no new public route or HTTP home appears in the lifecycle diff.

PF09 task/subtask IDs, if proven: HDE-DIST006.2

REQ-016

Requirement: Do not perform database or external-state mutation as part of read-only verification.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR review finding; Remedial PR context manager and direct fake-connect test.

GitHub Repo proof, if current state matters: current `--check` removes DATABASE\_URL before route capture and restores it afterward.

PF09 task/subtask IDs, if proven: HDE-DIST005.1

REQ-017

Requirement: Preserve normal dev writer behavior outside check mode.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Remedial PR | two-file diff and HTTP test | `"normal (write) execution path is unchanged"` | `"test_dev_conjunction_http.py passed"`

GitHub Repo proof, if current state matters: adapter code was not changed by Remedial PR.

PF09 task/subtask IDs, if proven: HDE-DIST005.1

REQ-018

Requirement: Focused identity, provenance, release-binding, environment, CLI, transport, and evidence tests pass.

Original PR status: Satisfied, except external-state non-persistence was insufficiently tested.

After remediation: Satisfied

Evidence pointer(s): Original and Remedial workflow jobs; Remedial focused test.

GitHub Repo proof, if current state matters: all visible workflow jobs completed successfully.

PF09 task/subtask IDs, if proven: all mapped PR-01 subtasks

REQ-019

Requirement: Check modes detect stale committed outputs and remain repository-byte-stable.

Original PR status: Satisfied for the main PR-01 evidence family; writer check had external-state defect.

After remediation: Satisfied

Evidence pointer(s): release renderer/check; canonical-gate committed-output comparison; writer non-persistence test; Index/Mirror checks.

GitHub Repo proof, if current state matters: remedial test job passed full evidence suite.

PF09 task/subtask IDs, if proven: HDE-DIST005.1, HDE-DIST005.2

REQ-020

Requirement: Preserve deterministic rails and secret-safe evidence posture.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR workflow/env snapshot; Remedial test uses a fake `example.invalid` sentinel and records no real secret.

GitHub Repo proof, if current state matters: CI rails and no-connect test passed.

PF09 task/subtask IDs, if proven: HDE-DIST005.1, HDE-DIST003.1

REQ-021

Requirement: Do not edit PF-Canon in implementation or remediation PRs.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): both changed-file lists; no `docs/pfcanon/**` path.

Search method: searched Original and Remedial changed-file lists for `docs/pfcanon/` (case: sensitive); scope: both PRs; tool: GitHub API; result: 0 hits.

PF09 task/subtask IDs, if proven: None; documentation drainage only

REQ-022

Requirement: Do not claim QA PASS, OPS completion, token satisfaction, PF09 status movement, deployment, or closeout.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Implementation Doc token posture; Extra Evidence nonclaims; Remedial PR nonclaims.

GitHub Repo proof, if current state matters: no HDE-EPIC038 acceptance map, close pack, or PF09 edit was added by these PRs.

PF09 task/subtask IDs, if proven: all mapped rows retain separate drainage posture

REQ-023

Requirement: Preserve PR-02 through PR-06 ownership and avoid treating PR-01 closure as aggregate epic release sanity.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Extra Evidence Â§Â§6.2-6.6 | `"PR-06 aggregate release-sanity binding remains open"` | `"PR-01 identity closure is not the final epic-level release-sanity orchestrator"`

GitHub Repo proof, if current state matters: Remedial PR changes only check safety and its test.

PF09 task/subtask IDs, if proven: HDE-DIST005.1, HDE-DIST005.2 remain shared with PR-06

### RCA

#### A) Bug/Failure statement

Original PR introduced a `--check` mode for conjunction writer evidence, but that mode calculated expected bytes by invoking the same dev writer route used by write-mode evidence capture. With a non-empty `DATABASE_URL`, the route could reach `psycopg.connect`, execute `INSERT INTO hde.idempotent_writes`, and commit before check-mode artifact comparison.

Evidence pointer:

Original PR | `tools/evidence/generate_conjunction_writer_evidence.py` | `"expected = _capture_outputs()"` before `"if args.check"` | writer route invokes persistence.

GitHub Repo | `adapter/http_reader.py` | `"if not dsn: return False"` | `"INSERT INTO hde.idempotent_writes"`

#### B) Root cause(s)

1. **Write-capable capture was reused without a side-effect boundary.**  
   Original check mode distinguished file writing only after route execution.  
2. **The initial regression observed only repository artifacts.**  
   Byte-equality of two governed files could not detect database mutation.  
3. **The proof target was narrower than the actual meaning of non-writing.**  
   Repository cleanliness was tested; external-state isolation was not.  
4. **The underlying persistence trigger was environment-sensitive.**  
   `DATABASE_URL` was read at route execution time, so behavior varied with operator environment.

#### C) Fix across PRs

Original PR:

* introduced deterministic conjunction evidence rendering and drift comparison;  
* added dev identity and writer/readback assertions;  
* exposed the external-state safety gap.

Remedial PR:

* adds `_non_persistent_check_capture()`;  
* removes `DATABASE_URL` only around check-mode capture;  
* restores the exact original state in `finally`;  
* leaves write mode and route behavior unchanged;  
* adds a fake-connect test with a non-empty sentinel DSN;  
* adds exception-path restoration proof.

Evidence pointer:

Remedial PR | generator patch | `"with _non_persistent_check_capture()"` | `"expected = _capture_outputs()"`

#### D) Fix verification

* Static proof: the persistence helper returns before importing `psycopg` when `DATABASE_URL` is absent.  
* Behavioral proof: the test fails immediately if `psycopg.connect` is called.  
* Artifact proof: both governed writer artifacts remain byte-identical.  
* Environment proof: the original sentinel DSN is restored after success and failure.  
* Regression proof: normal dev writer HTTP tests passed.  
* CI proof: Remedial PRâ€™s full evidence and closure workflow is green.

### PF09 Impact & Status Posture

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST005

PF09 subtask ID(s): HDE-DIST005.1

Current PF09 status: Partial

Status recommendation: No status change recommended

Why supported: PR-01 now supplies canonical encoding, pinned environment, and non-persistent check safety, but the Implementation Doc maps this global-discipline subtask to PR-01 and PR-06. The final release-sanity chain remains outside this lifecycle.

Evidence pointer(s): Implementation Doc PR-01/PR-06 mapping; NET-001, NET-066, NET-119, NET-133; VAL-007 through VAL-012.

GitHub Repo proof, if current state matters: current closure and evidence checks are green; PR-06 has not been reviewed here.

PF proof excerpt(s):

â€œUse canonical JSON or headers-only text, LF-terminated.â€

â€œAre produced under `LC_ALL=C`, `LANG=C`, `TZ=UTC` for any byte-sensitive harnesses.â€

â€œSubtask status: Partialâ€

Linked NET/Finding IDs: NET-001, NET-066, NET-119, NET-133; F-001

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST005

PF09 subtask ID(s): HDE-DIST005.2

Current PF09 status: Partial

Status recommendation: No status change recommended

Why supported: PR-01â€™s Index, sentinel, Mirror, checksum, and proof family is coherent, but the Implementation Doc assigns final global confirmation to PR-06 as well.

Evidence pointer(s): NET-023 through NET-026, NET-095 through NET-098, NET-141; VAL-012.

GitHub Repo proof, if current state matters: all Index/Mirror checks pass at current HEAD.

PF proof excerpt(s):

â€œFor any artifact added/moved/removed in this phase:â€

â€œUpdate `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PR.â€

â€œSubtask status: Partialâ€

Linked NET/Finding IDs: NET-023â€“026, NET-095â€“098, NET-141

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST006

PF09 subtask ID(s): HDE-DIST006.1

Current PF09 status: Partial

Status recommendation: change to Done

Why supported: The approved rescope establishes the final production/dev identity model. Current Repo contains the immutable exact six-field production authority, validation, evidence, and tests, with no later divergence.

Evidence pointer(s): NET-027â€“036, NET-100â€“104, NET-127, NET-136; REQ-001 through REQ-005.

GitHub Repo proof, if current state matters: current identity code and artifacts equal the reviewed merged state; workflows pass.

PF proof excerpt(s):

â€œEnsure the Identity & Provenance module exposes and persists exactly these fields â€” no extras â€” as read-only values after freezeâ€

â€œIdentity fields are not mutated after freezeâ€

â€œSubtask status: Partialâ€

Linked NET/Finding IDs: NET-027â€“036, NET-100â€“104, NET-127, NET-136; F-003

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST006

PF09 subtask ID(s): HDE-DIST006.2

Current PF09 status: Not done

Status recommendation: change to Done

Why supported: Reader, CLI, internal-version, compat, and evidence consumers use the approved identity helpers/profile; injection compatibility is preserved; Reader/CLI and transport regression suites pass.

Evidence pointer(s): NET-004, NET-099â€“104, NET-115â€“128, NET-130â€“131; REQ-004 through REQ-008.

GitHub Repo proof, if current state matters: no later identity consumer changes; final CI green.

PF proof excerpt(s):

â€œProve that public Reader and CLI code paths obtain identity from the Identity & Provenance module helpersâ€

â€œDemonstrate CLIâ†”Reader parityâ€

â€œSubtask status: Not doneâ€

Linked NET/Finding IDs: NET-004, NET-099â€“104, NET-115â€“128, NET-130â€“131

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST006

PF09 subtask ID(s): HDE-DIST006.3

Current PF09 status: Partial

Status recommendation: change to Done

Why supported: Identity provenance artifacts, their Index/Mirror/proof bindings, deterministic generator, independent two-run evidence, and checks exist and pass under the approved rescope.

Evidence pointer(s): NET-023â€“036, NET-095â€“098, NET-121, NET-127, NET-136, NET-141.

GitHub Repo proof, if current state matters: final evidence suite and closure pass.

PF proof excerpt(s):

â€œCapture and persist build-time hashes for the shared emitter and invocation and index them as identity artifactsâ€

â€œEach record includes a `proof_anchor` path-proof stored alongside the artifact.â€

â€œSubtask status: Partialâ€

Linked NET/Finding IDs: NET-023â€“036, NET-095â€“098, NET-136, NET-141; F-003

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST002

PF09 subtask ID(s): HDE-DIST002.4

Current PF09 status: Partial

Status recommendation: change to Done

Why supported: Canonical manifest and release-identity artifacts are present, indexed, mirrored, path-proven, and covered by deterministic recompute and closure checks.

Evidence pointer(s): NET-031â€“043, NET-090, NET-095â€“098, NET-109, NET-124, NET-141.

GitHub Repo proof, if current state matters: release and evidence checks pass at current HEAD.

PF proof excerpt(s):

â€œIndex manifest and release identity artifacts in Human Index and Machine Mirror in the same PRâ€

â€œeach mirror record includes a `proof_anchor` path-proofâ€

â€œSubtask status: Partialâ€

Linked NET/Finding IDs: NET-031â€“043, NET-090, NET-095â€“098, NET-109, NET-124, NET-141

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST002

PF09 subtask ID(s): HDE-DIST002.5

Current PF09 status: Not done

Status recommendation: change to Done

Why supported: The approved Product Owner rescope adjudicates the retained release-binding shape and authorizes PF12/PF09 drainage. Current artifact, source bindings, deterministic check, Index/Mirror/proof bindings, and focused tests are present and green.

Evidence pointer(s): Extra Evidence Â§Â§4, 8.3, 8.4; NET-005, NET-006, NET-123, NET-138, NET-141.

GitHub Repo proof, if current state matters: artifact and tests remain at current HEAD; no later change.

PF proof excerpt(s):

â€œCapture and index the release bindings artifact that ties `release_id` to BodyGraph data source policy and refresh behaviorâ€

â€œIndex `release_bindings.json` in `docs/evidence/INDEX.json` and mirror it in `artifacts/evidence_index.jsonl` in the same PRâ€

â€œSubtask status: Not doneâ€

Linked NET/Finding IDs: NET-005, NET-006, NET-123, NET-138, NET-141; F-003

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST003

PF09 subtask ID(s): HDE-DIST003.1

Current PF09 status: Partial

Status recommendation: change to Done

Why supported: The singleton is schema version 3, canonical, deterministic, presence-only, uniquely produced, protected against old writers, and covered by focused and repo-wide checks.

Evidence pointer(s): NET-066, NET-107, NET-108, NET-120, NET-134, NET-137.

GitHub Repo proof, if current state matters: current artifact and generator are unchanged after remediation and checks pass.

PF proof excerpt(s):

â€œProduce `artifacts/runtime/env_matrix.snapshot.json` as a singleton per repo.â€

â€œEnforce schema v3â€

â€œSubtask status: Partialâ€

Linked NET/Finding IDs: NET-066, NET-107, NET-108, NET-120, NET-134, NET-137

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST003

PF09 subtask ID(s): HDE-DIST003.4

Current PF09 status: Partial

Status recommendation: change to Done

Why supported: The environment snapshot and previously existing logs/metrics family are represented in the Human Index, Mirror, checksum, and path-proof system, and current validation passes.

Evidence pointer(s): NET-023â€“026, NET-066â€“067, NET-095â€“098, NET-141; VAL-012.

GitHub Repo proof, if current state matters: current Index/Mirror checks green.

PF proof excerpt(s):

â€œUpdate `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PRâ€

â€œSubtask status: Partialâ€

Linked NET/Finding IDs: NET-023â€“026, NET-066â€“067, NET-095â€“098, NET-141

### Findings

F-001

Related item: NET-133 / VAL-008 / VAL-009 / RCA

Severity: Note

Observation: Original PRâ€™s check mode could reach database persistence when `DATABASE_URL` was present, but Remedial PR removes that trigger during check capture and proves zero connection attempts.

Why it matters: This was the only substantiated remaining code-level blocker after the approved rescope.

Evidence: Original generator order, current persistence call path, remedial context manager, sentinel/fake-connect test, and green remedial CI.

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-DIST005.1 remains Partial because final global confirmation is shared with PR-06, not because this defect remains.

PF reference, if relied on: PF19 â€” Glow QA Guide, Â§2.2.11 Evidence-governed CI sequence.

F-002

Related item: Other

Severity: Note

Observation: Extra Evidence identifies PF23 as a later PF update target, but PF23 was not used here as PR-review authority, deliverable, blocker, token source, acceptance source, or current-repo proof.

Why it matters: The review prompt expressly excludes PF23 from PR-review authority.

Evidence: This reportâ€™s validation, requirement, PF09, and decision bases cite no PF23 requirement or proof.

Required action: None.

Blocker: No

PF09 impact/status, if proven: None.

PF reference, if relied on: PF27 â€” Plan Templates, PF23 consult exclusion for PR analysis.

F-003

Related item: PF09 / Other

Severity: Note

Observation: Permanent PF06, PF27, PF14, PF12, PF19, PF07, and PF09.6 text does not yet fully reflect the approved PR-01 rescope and the Product Owner supersession rule.

Why it matters: Future agents need the permanent PF homes to describe the accepted architecture and governance rule accurately.

Evidence: Extra Evidence supplies explicit update authority and order; the merged code and current evidence reflect the approved decision.

Required action: None in this code lifecycle. Apply the Doc Delta Candidates below through a separate PF-Canon documentation action.

Blocker: No

PF09 impact/status, if proven: Status recommendations are listed above; no status is moved by this review.

PF reference, if relied on: PF06, PF27, PF14, PF12, PF19, PF07, PF09.6.

### Evidence Print (PASS PROOF; merged work)

#### A) Acceptance coverage evidence

1. **Identity authority and consumers**  
   Implementation Doc | PR-01 requirements 1-6 | `"immutable validated identity snapshot"` | `"Reader, CLI, and internal identity surfaces use shared helpers"`  
   GitHub Repo proof: NET-004, NET-099â€“104, NET-127.  
   Result: covered.  
2. **Approved compatibility architecture**  
   Extra Evidence | Â§Â§3.1-3.2, 5.1-5.3 | `"bounded dev compatibility identity profile"` | `"sanctioned adapter or test composition"`  
   GitHub Repo proof: `engine/compat/identity.py`, `engine/http/compat_handler.py`, `engine/runtime/public.py`.  
   Result: covered.  
3. **Identity provenance and release identity**  
   Original PR | generator/artifact/test family | `"service_identity.json"` | `"release_id_recompute.log"`  
   GitHub Repo proof: NET-027â€“043, NET-121, NET-124, NET-136.  
   Result: covered.  
4. **Environment singleton version 3**  
   Implementation Doc | requirement 9 | `"schema-version-3 singleton"` | `"presence only, never values"`  
   GitHub Repo proof: NET-066, NET-107â€“108, NET-120, NET-134, NET-137.  
   Result: covered.  
5. **Release binding and governed evidence**  
   Implementation Doc / Extra Evidence | release-binding scope | `"BodyGraph release bindings"` | `"PF12 update authority"`  
   GitHub Repo proof: NET-005â€“006, NET-123, NET-138, NET-141.  
   Result: covered.  
6. **Index/Mirror/proof coherence**  
   GitHub Repo | final workflow checks | `"update_evidence_index.py --check=success"` | `"check_mirror_schema.sh=success"`  
   Result: covered.  
7. **No external-state mutation in check mode**  
   Remedial PR | code and test | `"DATABASE_URL"` removed within check context | `"connect_calls == []"`  
   GitHub Repo proof: NET-119, NET-133.  
   Result: covered.

#### B) Original gaps closed

* Reader injected-emitter compatibility: closed in Original PR final state.  
* Dev compatibility identity labeling: closed in Original PR final state.  
* Independent two-run collection: closed in Original PR final state.  
* Environment optional-secret nondeterminism: closed in Original PR final state.  
* Environment singleton legacy-writer conflict: closed in Original PR final state.  
* Showcompat interpreter/identity drift: closed in Original PR final state.  
* Release recompute stale-output detection: closed in Original PR final state.  
* Canonical-gate committed-output comparison: closed in Original PR final state.  
* CLI installability/offline check posture: closed in Original PR final state.  
* Writer `--check` DB persistence risk: closed by Remedial PR.

Evidence pointer:

Original PR | final review threads/current code | `"outdated or repaired findings"` | `"one live writer-persistence finding"`

Remedial PR | two-file patch | `"non-persistent check capture"` | `"fake connect must not be called"`

#### C) Evidence and verification posture

* Original and remedial final workflow runs are green.  
* Current repository equals remedial merged state.  
* No later commit changed a lifecycle file.  
* Remedial PR changed no governed artifact.  
* Current writer artifacts remain byte-stable and record all intended checks as true.  
* Human Index, sentinel, Machine Mirror, checksum, path proofs, orientation, and canonical-gate checks pass.  
* No local execution is claimed by this reviewer.  
* Extra Evidence is supplemental provenance and rescope authority; current GitHub Repo controls final file reality.

#### D) Token/gate evidence

No acceptance token is claimed as satisfied by this review.

Implementation Doc explicitly describes its token roster as planned claims only. Original PR and Remedial PR preserve nonclaims for QA PASS, OPS completion, token satisfaction, PF09 movement, deployment, and closeout.

Visible successful checks are reported as workflow/check evidence, not converted into token satisfaction.

#### E) Test/CI proof

Original PR:

GitHub Repo | workflow run `29191942424` | `"conclusion=success"` | `"test, sanity, compat, acceptance, evidence, conjunction jobs successful"`

Remedial PR:

GitHub Repo | workflow run `29206555501` | `"conclusion=success"` | `"repo-wide evidence tests and closure successful"`

Focused final safety proof:

GitHub Repo | `tests/evidence/test_dev_conjunction_identity.py` | `"psycopg.connect must not be called"` | `"DATABASE_URL restored"`

#### F) Artifact and evidence outputs

The reviewed lifecycle establishes or refreshes:

* six-field service identity;  
* emitter, Invocation, and release identity records;  
* release recompute evidence;  
* two-run identity evidence;  
* BodyGraph release binding;  
* environment snapshot version 3;  
* CLI AB/BA, showcompat, installability, and summary evidence;  
* internal-version body, headers, request-chain, checksum, and two-run evidence;  
* conjunction writer/readback evidence;  
* canonical JSON gate outputs;  
* Human Evidence Index and sentinel;  
* Machine Evidence Mirror and checksum;  
* sibling path proofs;  
* orientation output;  
* canonical manifest and release artifacts.

Remedial PR is byte-neutral for this governed evidence set. Its correctness proof is code/test/CI evidence rather than regenerated artifact bytes.

### Doc Delta Candidates (PF-Canon only)

DDC-001

Doc: PF06 â€” Epic Process Guide

Section: Â§0.2 Policy and principles

Canon basis: CANON SILENCE

Impacted PF09 task/subtask IDs: None

PF09 status action: None

Delta: Add a formal rule that an expressly approved, bounded Product Owner scope, architecture, or ADR revision may supersede conflicting PF-Canon for the exact decision it adjudicates; require a causal map, named superseded language, preserved later-slice boundaries, nonclaims, and controlled later drainage.

Why: PR-01 demonstrated that waiting for permanent drain must not force a merged implementation back to superseded wording, while unrestricted informal scope expansion must remain prohibited.

Evidence pointer: Extra Evidence | Â§Â§1, 2, 8.1, 9, 10 | `"retroactive architectural rescoping and canonicalization authority"` | `"corrective architecture decision, not a general waiver"`

GitHub Repo proof, if current state matters: current merged architecture is `df662b518f0290a4bae6b26fb0332b374f28116a`.

Negative-search proof: Search method: searched for `retroactive rescoping`, `bounded Product Owner scope revision`, and `approved scope revision may supersede` (case: insensitive); scope: PF06; tool: grep/manual scan; result: 0 hits.

DDC-002

Doc: PF27 â€” Plan Templates

Section: Â§Canon precedence for template use.

Canon basis: CANON AMBIGUITY-CONFLICT

Impacted PF09 task/subtask IDs: None

PF09 status action: None

Delta: Extend the required precedence statement to distinguish PF10 live addenda from a formally approved bounded Product Owner rescope; require plan authors to identify transferred later-PR work, preserved boundaries, nonclaims, and PF drain candidates.

Why: Current template precedence names PF10 and permanent PF-Canon but does not explain the authority of an approved bounded rescope.

Evidence pointer: Extra Evidence | Â§Â§8.8 and 9 | `"add an approved-rescope section"` | `"require explicit transfer language for early delivery"`.

GitHub Repo proof, if current state matters: PR-01 contains approved early delivery from PR-03 without closing PR-03.

Canon proof excerpt:

â€œTemplates and derived plan documents MUST include the canon precedence rule:â€

â€œPF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.â€

DDC-003

Doc: PF14 â€” HDE Mechanics Guide

Section: Â§13) Identity & Provenance Module \[Required-Now\]

Canon basis: CANON MISMATCH

Impacted PF09 task/subtask IDs: HDE-DIST006.1, HDE-DIST006.2, HDE-DIST006.3

PF09 status action: change to Done

Delta: Record the accepted production identity authority, bounded non-production compatibility profile, sanctioned injected-emitter seam, adopted Invocation digest convention, independent two-run collection, and PR-01 dependency graph. Amend the unqualified no-alternate-seam wording so it prohibits alternate production identity sources while permitting the bounded approved dev/test domain.

Why: The existing section describes only a single undifferentiated identity domain, while the Product Owner-approved architecture distinguishes production identity from bounded compatibility identity and injection.

Evidence pointer: Extra Evidence | Â§Â§3.1-3.2, 5.1-5.3, 8.5 | `"not a second production identity authority"` | `"compatibility and testing seam"`.

GitHub Repo proof, if current state matters: NET-100â€“104.

Canon proof excerpt:

â€œPurpose. Single source of truth for engine and release identity.â€

â€œidentity\_meta() â†’ {"engine\_tag","invocation\_tag"}â€

â€œNo alternative sources (env vars, flags) on public paths.â€

DDC-004

Doc: PF12 â€” HDE Schemas and Artifacts

Section: Â§8.6.3.4 Gates, runtime, DB, and ops evidence

Canon basis: CANON MISMATCH

Impacted PF09 task/subtask IDs: HDE-DIST003.1, HDE-DIST003.4, HDE-DIST006.1, HDE-DIST006.2, HDE-DIST006.3

PF09 status action: change to Done

Delta: Define the accepted six-field production identity artifact, bounded dev compatibility identity evidence, schema-version-3 environment singleton, deterministic presence fixture, canonical internal-version capture names, and PR-01 identity closure outputs/check semantics.

Why: Current Repo and approved rescope contain these governed families, but permanent catalog text does not fully describe the accepted architecture.

Evidence pointer: Extra Evidence | Â§8.4 | `"define the six-field production identity artifact"` | `"define environment snapshot schema version 3"`.

GitHub Repo proof, if current state matters: NET-027â€“036, NET-044â€“067, NET-139â€“142.

Canon proof excerpt:

â€œRuntime and environmentâ€

â€œInternal-ops surface â€” `/internal/version` identity artifactsâ€

DDC-005

Doc: PF12 â€” HDE Schemas and Artifacts

Section: Â§8.6.3.9 SBOM, registry, configuration, and BodyGraph evidence

Canon basis: CANON MISMATCH

Impacted PF09 task/subtask IDs: HDE-DIST002.5

PF09 status action: change to Done

Delta: Define the retained PR-01 BodyGraph release-binding shape, source-artifact SHA linkage, canonical-byte rules, and Index/Mirror/proof binding.

Why: The Product Owner approved the retained release-binding implementation and explicitly authorized PF12 to define its permanent shape.

Evidence pointer: Extra Evidence | Â§Â§4 and 8.4 | `"BodyGraph release bindings"` | `"define BodyGraph release-binding shape"`.

GitHub Repo proof, if current state matters: NET-005, NET-006, NET-123, NET-138, NET-141.

Canon proof excerpt:

â€œBodyGraph release bindings: artifacts/bodygraph/release\_bindings.json.â€

DDC-006

Doc: PF19 â€” Glow QA Guide

Section: Â§2.2.11 Evidence-governed CI sequence (names-only)

Canon basis: CANON SILENCE

Impacted PF09 task/subtask IDs: HDE-DIST005.1

PF09 status action: No status change recommended

Delta: Define a non-writing check as prohibiting repository mutation and external-state mutation, including database connection, SQL execution, transaction commit, migration, and external-service mutation. Require direct side-effect interception tests when a verifier executes a route with a persistence seam.

Why: Artifact-byte equality alone failed to detect the Original PRâ€™s potential DB mutation.

Evidence pointer: RCA / Remedial PR | `"psycopg.connect must not be called by --check"` | `"assert connect_calls == []"`.

GitHub Repo proof, if current state matters: NET-119 and NET-133.

Negative-search proof: Search method: searched for `non-writing`, `database connection`, `external-state mutation`, and `transaction commit` (case: insensitive); scope: PF19 Â§2.2.11; tool: grep/manual scan; result: 0 rules defining the complete external-state prohibition.

DDC-007

Doc: PF07 â€” Glow Infrastructure

Section: Â§Change control (titles-only cross-refs)

Canon basis: CANON AMBIGUITY-CONFLICT

Impacted PF09 task/subtask IDs: HDE-DIST003.1

PF09 status action: change to Done

Delta: Record the approved production SAFE\_MODE/ALLOW\_NETWORK relationship, production aliases, and the distinction between a PR-specific committed-closure gate and reusable PR-03 CI rails.

Why: PR-01 delivered the exact early rail alignment needed for environment snapshot v3 without closing PR-03.

Evidence pointer: Extra Evidence | Â§Â§6.1, 6.3, 8.2 | `"production rail alignment required by the schema-v3 environment contract"` | `"does not satisfy or close the broader PR-03 reusable-gate scope"`.

GitHub Repo proof, if current state matters: NET-001, NET-003, NET-066, NET-110â€“112.

Canon proof excerpt:

â€œPF07 owns canonical environment and config key namesâ€

â€œCapture environment pinsâ€

DDC-008

Doc: PF09.6 â€” HDE Build Checklist, Distillation

Section: Â§Subtask HDE-DIST006.1 â€” Identity fields & source-of-truth; Â§Subtask HDE-DIST006.2 â€” Identity helpers & parity; Â§Subtask HDE-DIST006.3 â€” Identity hashes & mirror discipline

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task/subtask IDs: HDE-DIST006.1, HDE-DIST006.2, HDE-DIST006.3

PF09 status action: change to Done

Delta: Drain the approved production/dev identity architecture, current implementation loci, evidence family, and reviewed completion proof.

Why: Both merged attempts now provide the implementation, governed evidence, focused tests, non-writing safety, and green current-state verification required for the PR-01 identity slice.

Evidence pointer: NET-027â€“036, NET-099â€“104, NET-115â€“131, NET-136; VAL-006â€“VAL-012.

GitHub Repo proof, if current state matters: current HEAD `df662b518f0290a4bae6b26fb0332b374f28116a`.

Canon proof excerpt:

â€œSubtask status: Partialâ€

â€œSubtask status: Not doneâ€

â€œSubtask status: Partialâ€

DDC-009

Doc: PF09.6 â€” HDE Build Checklist, Distillation

Section: Â§Subtask HDE-DIST002.4 â€” Pack/manifest indexing; Â§Subtask HDE-DIST002.5 â€” Release bindings evidence & indexing

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task/subtask IDs: HDE-DIST002.4, HDE-DIST002.5

PF09 status action: change to Done

Delta: Drain current manifest/release indexing and the Product Owner-approved release-binding implementation.

Why: Current Repo contains canonical primary artifacts, deterministic checks, Human Index/Mirror/proof bindings, and passing final validation.

Evidence pointer: NET-005â€“006, NET-031â€“043, NET-090, NET-095â€“098, NET-109, NET-123â€“124, NET-138, NET-141.

GitHub Repo proof, if current state matters: current release and evidence checks green.

Canon proof excerpt:

â€œSubtask status: Partialâ€

â€œSubtask status: Not doneâ€

DDC-010

Doc: PF09.6 â€” HDE Build Checklist, Distillation

Section: Â§Subtask HDE-DIST003.1 â€” Environment snapshot singleton (v3); Â§Subtask HDE-DIST003.4 â€” Env snapshot & observability indexing

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task/subtask IDs: HDE-DIST003.1, HDE-DIST003.4

PF09 status action: change to Done

Delta: Drain schema-version-3 singleton completion, migrated writer/consumer loci, deterministic presence posture, and current Index/Mirror/proof binding.

Why: The singleton migration is complete in current Repo and passed focused and global validation.

Evidence pointer: NET-066â€“067, NET-107â€“108, NET-120, NET-134, NET-137, NET-141.

GitHub Repo proof, if current state matters: current env artifact and checks unchanged after remediation.

Canon proof excerpt:

â€œSubtask status: Partialâ€

â€œSubtask status: Partialâ€

DECISION: MERGED WORK ACCEPTABLE

## 2.2) PR-02 HDE-EPIC038

### Review Summary

* Original PR implemented the PR-02 deterministic Reader/CLI proof family, Catalog-driven A7 transport producer, Endpoint Catalog repair, composite Reader-success schema, governed artifacts, tests, and canonical evidence bindings.  
* Original PR merged successfully but retained material gaps: its canonical-gate predicate was caller-supplied rather than authoritative; the composite proof and Reader endpoint snapshot differed from PF12; A7 validation omitted required HEAD, 304, writer/error, and encoding-length predicates; tests retained a second proof writer; several decisive paths were not exercised; historical token evidence overstated encoding-invariance support; and path-proof chronology was not truthful for newly changed bytes.  
* Remedial PR followed Original PR directly in the same `main` lineage and addressed those gaps without adding a new public route, changing Reader runtime behavior, executing OPS, or editing PF-Canon.  
* The Product Owner decision that `POST /internal/dev/sampler` belongs in the internal Endpoint Catalog was implemented as a bounded inventory decision: the route is `dev_harness`, internal, non-A7-eligible, excluded from `success_endpoints`, and still unsupported for GET.  
* Current Repo uses the authoritative canonical JSON gate in the determinism aggregate, validates the composite A7 proof against the governed JSON Schema, emits the PF12 Reader endpoint snapshot shape, enforces complete GET/HEAD/304/error/encoding predicates, and retains one deterministic A7 proof writer.  
* The remedial tests exercise write authorization, real check mode, no-partial-write behavior, malformed transport variants, nested schema rejection, all accepted encodings, environment restoration, Catalog field validation, and proof-writer ownership.  
* Historical EPIC028 encoding-token artifacts are now driven by complete ETag and HEAD identity-length proof rather than artifact-path presence alone.  
* Human Index, Machine Mirror, checksums, path proofs, orientation evidence, Catalog derivatives, and historical dependent artifacts were regenerated through their established owners. Visible repository-host checks completed successfully.  
* No later commit affecting the lifecycle touched-file set was found after the Remedial PR merge. Current `main` is the reviewed remedial merged state.  
* PF09.6 impact is exactly mapped to `HDE-DIST001`, `HDE-DIST001.1`, and `HDE-DIST001.2`. The two PR-02 subtasks now have support for later drainage to `Done`; the parent task should remain `Partial` because its broader Distillation inventory extends beyond this lifecycle.

### GitHub / Repo Inspection

#### Repository and branch

GitHub Repo | repository metadata | `"amthorn78/glow-hdengine-v2"` | `"default branch: main"`

Reviewed target branch: `main`.

Current reviewed branch HEAD: the Remedial PR merge identifier.

GitHub Repo | default-branch history | `"current HEAD equals Remedial PR merge"` | `"no later commit found"`

Search method: searched for commits after the Remedial PR merge identifier (case: sensitive); scope: `main` commit history; tool: GitHub API; result: 0 hits.

No local checkout was used for this review. No local command, working-tree mutation, branch creation, commit, push, OPS action, or external-system action is claimed.

#### Original PR

Original PR | API field `number` | `"348"` | `"merged: true"`

Original PR | API fields `base.ref`, `base.sha` | `"main"` | `"df662b518f0290a4bae6b26fb0332b374f28116a"`

Original PR | API fields `head.sha`, `merge_commit_sha` | `"c06b665f267bb08f37e217e2a762f1cca3c2f585"` | `"ceefe4f52f12c0dcb57c9721639b720a539be96a"`

Original PR | API field `changed_files` | `"67"` | `"complete changed-file list retrieved"`

Original PR | merged state | `"closed"` | `"merged"`

The lifecycle baseline is `df662b518f0290a4bae6b26fb0332b374f28116a`, the commit immediately before Original PR merged.

#### Remedial PR

Remedial PR | API field `number` | `"349"` | `"merged: true"`

Remedial PR | API field `base.ref` | `"main"` | `"base SHA equals Original PR merge identifier"`

Remedial PR | API fields `head.sha`, `merge_commit_sha` | `"resolved from GitHub PR metadata"` | `"merge identifier equals current main HEAD"`

Remedial PR | changed-file enumeration | `"complete list retrieved"` | `"all material paths represented in the RPR and NET ledgers"`

The Remedial PR base is exactly the Original PR merge state. The two PRs therefore form one direct, reviewable lifecycle.

#### Lifecycle order

1. Lifecycle baseline: Original PR base.  
2. Original merged state: Original PR merge identifier.  
3. Remedial merged state: Remedial PR merge identifier.  
4. Current state: same as Remedial merged state.

GitHub Repo | compare Original merge to Remedial merge | `"ahead"` | `"one remedial lifecycle step"`

No unrelated intervening branch lineage was found.

#### Lifecycle touched-file set

The lifecycle union contains:

* all 67 Original PR paths;  
* the remedial changes to those paths;  
* the remedial Catalog-comment correction in `adapter/http_reader.py`.

Files deleted by Original PR remain in the lifecycle set:

* `artifacts/proofs/encoding_invariance.txt`  
* `artifacts/proofs/encoding_invariance.txt.path_proof.txt`

Both remain absent in current Repo.

Search method: searched for exact obsolete paths (case: sensitive); scope: current Repo files, evidence producers, Human Index, Machine Mirror, historical acceptance artifacts, and manifests; tool: GitHub search plus current-file scan; result: 0 active governed references.

#### Reviews, comments, and checks

Original PR review materials documented the defects later addressed by Remedial PR, including:

* synthetic canonical-gate proof;  
* nonconforming composite proof schema;  
* nonconforming endpoint snapshot;  
* incomplete A7 predicates;  
* second governed proof writer;  
* insufficient negative and check-mode tests;  
* incomplete encoding-token proof;  
* stale path-proof chronology;  
* omission of the internal dev sampler from the full Catalog.

Remedial PR visibly completed its repository-host checks, including the targeted PR-02 tests and the existing canonical evidence checks.

GitHub Repo | remedial workflow | `"completed"` | `"success"`

Visible checks inspected included:

* determinism producer tests;  
* A7 transport producer tests;  
* Endpoint Catalog tests;  
* Reader A7 transport tests;  
* canonical JSON gate;  
* Catalog checksum check;  
* Human Index check;  
* Machine Mirror schema check;  
* Evidence Index hash check;  
* evidence path validation;  
* orientation check;  
* final-LF check;  
* existing Reader/CLI and identity-closure regressions.

CI was not treated as sufficient by itself; current final source, schema, artifacts, ledgers, path proofs, and historical dependent evidence were inspected separately.

#### Governed evidence inspected

Current governed families inspected include:

* `docs/ENDPOINTS_CATALOG.json`  
* `docs/ENDPOINTS_CATALOG.json.sha256`  
* `artifacts/audit/ENDPOINTS_CATALOG.json`  
* `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`  
* `artifacts/reader/endpoints_snapshot.json`  
* `schemas/proofs.reader_success.v1.json`  
* `artifacts/proofs/reader_success_get_head_304.json`  
* all six retained A7 text-proof files;  
* determinism AB/BA, two-run, summary, and A3 marker files;  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`  
* sibling path proofs;  
* orientation evidence;  
* EPIC025 manifest dependencies;  
* EPIC028 acceptance map, token matrix, and viability log.

### Provenance (Original \-\> Remediation)

* **Claim:** Original PR intended to create deterministic Reader/CLI and A7 transport proof producers.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | body and changed files | `"determinism gate proofs"` | `"Catalog-driven A7 transport proofs"`  
* **Claim:** Original PR produced the planned primary artifacts and integrated them with canonical evidence tooling.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | diff and generated artifacts | `"audit/gates/parity/reader_cli/summary.json"` | `"artifacts/proofs/reader_success_get_head_304.json"`  
* **Claim:** Original PRâ€™s canonical-gate predicate was not grounded in the actual canonical gate.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | `tools/evidence/generate_determinism_gate_proofs.py` | `"build(canon_check=True"` | `"canonical_gate_check: bool(canon_check)"`  
* **Claim:** Original PRâ€™s composite schema and endpoint snapshot did not implement PF12â€™s required shapes.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | schema and artifacts | `"captured_at_utc"` | `"json_success"`  
* **Claim:** Original PR did not prove complete encoding invariance.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | `success_encoding_invariance.txt` | `"tested_encodings"` | `"identity_etag"`  
  Search method: searched for per-encoding HEAD identity-length values (case: sensitive); scope: Original merged encoding proof; tool: manual scan; result: 0 hits.  
* **Claim:** Original PR retained a second writer for governed A7 proof files.  
  **Source:** Original PR  
  **Evidence pointer:** Original PR | `tests/http/test_reader_a7_transport.py` | `"HDE_WRITE_A7_PROOFS"` | direct writes to retained proof paths  
* **Claim:** Remedial PR replaced the synthetic canonical-gate predicate with authoritative read-only gate consumption.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | determinism producer diff | `"run_canonical_json_gate.py --check-only"` | fail-closed result/provenance handling  
* **Claim:** Remedial PR aligned the composite schema, composite artifact, and endpoint snapshot with PF12.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | schema and artifact diffs | `"route_path"` | `"generated_at_utc"`  
* **Claim:** Remedial PR added complete HEAD, 304, error, and encoding-length predicates.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | A7 producer diff | `"identity"` / `"gzip"` / `"br"` | per-encoding ETag and HEAD identity-length equality  
* **Claim:** Remedial PR established one governed A7 writer.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | test diff | test-side file rendering removed | producer remains sole write owner  
* **Claim:** Remedial PR implemented the Product Ownerâ€™s sampler Catalog decision.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | Catalog and adapter-comment diffs | `"POST /internal/dev/sampler"` | `"a7_eligible:false"`  
* **Claim:** Remedial PR corrected historical token truthfulness.  
  **Source:** Remedial PR  
  **Evidence pointer:** Remedial PR | EPIC028 generator and artifacts | token implementation derived from decisive ETag and length predicates | no path-exists-only claim  
* **Claim:** Current Repo is the remedial merged state and has no later divergence.  
  **Source:** GitHub Repo  
  **Evidence pointer:** GitHub Repo | current `main` history | `"HEAD = Remedial PR merge"` | `"0 later commits"`

#### Original PR Material Hunk Ledger

Hunk ID: OPR-001  
File: `artifacts/audit/ENDPOINTS_CATALOG.json`  
Patch and hunk header: `diff --git a/artifacts/audit/ENDPOINTS_CATALOG.json b/artifacts/audit/ENDPOINTS_CATALOG.json` || whole canonical-Catalog replacement  
Material effect: introduced repaired string-method Catalog records and the governed Reader success designation.  
Risk category: schema/data model; governed evidence.  
Evidence pointer: Original PR | file diff | `"success_endpoints"` | `"GET /reader"`

Hunk ID: OPR-002  
File: `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt`  
Patch and hunk header: `diff --git a/artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt b/artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` || proof replacement  
Material effect: refreshed audit-Catalog path proof.  
Risk category: governed evidence.  
Evidence pointer: Original PR | file diff | new hash and size

Hunk ID: OPR-003  
File: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`  
Patch and hunk header: `diff --git a/artifacts/audit/ENDPOINTS_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS_CATALOG.json.sha256` || checksum replacement  
Material effect: refreshed Catalog audit checksum.  
Risk category: governed evidence.

Hunk ID: OPR-004  
File: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed checksum proof.  
Risk category: governed evidence.

Hunk ID: OPR-005  
File: `artifacts/cards/a3/IDENTITY_OK.txt`  
Patch and hunk header: marker replacement  
Material effect: added PR-02 deterministic predicate marker and token nonclaim.  
Risk category: token/evidence posture.

Hunk ID: OPR-006  
File: `artifacts/cards/a3/IDENTITY_OK.txt.path_proof.txt`  
Patch and hunk header: new sibling-proof hunk  
Material effect: bound the marker.  
Risk category: governed evidence.

Hunk ID: OPR-007  
File: `artifacts/evidence_index.jsonl`  
Patch and hunk header: JSONL record additions/removals  
Material effect: registered PR-02 evidence and removed obsolete encoding-proof home.  
Risk category: Machine Mirror.

Hunk ID: OPR-008  
File: `artifacts/evidence_index.jsonl.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed Mirror proof.  
Risk category: governed evidence.

Hunk ID: OPR-009  
File: `artifacts/evidence_index.jsonl.sha256`  
Patch and hunk header: checksum replacement  
Material effect: refreshed Mirror checksum.  
Risk category: governed evidence.

Hunk ID: OPR-010  
File: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed checksum proof.  
Risk category: governed evidence.

Hunk ID: OPR-011  
File: `artifacts/proofs/encoding_invariance.txt`  
Patch and hunk header: whole-file deletion  
Material effect: deleted obsolete duplicate evidence home.  
Risk category: governed evidence deletion.

Hunk ID: OPR-012  
File: `artifacts/proofs/encoding_invariance.txt.path_proof.txt`  
Patch and hunk header: whole-file deletion  
Material effect: removed obsolete sibling proof.  
Risk category: governed evidence deletion.

Hunk ID: OPR-013  
File: `artifacts/proofs/endpoints_env_gate_proof.log`  
Patch and hunk header: complete proof replacement  
Material effect: generated production-gate proof.  
Risk category: environment/rails evidence.

Hunk ID: OPR-014  
File: `artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed env-gate proof transcript.  
Risk category: governed evidence.

Hunk ID: OPR-015  
File: `artifacts/proofs/reader_success_get_head_304.json`  
Patch and hunk header: new canonical JSON artifact  
Material effect: introduced composite Reader A7 proof.  
Risk category: schema; governed evidence.

Hunk ID: OPR-016  
File: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`  
Patch and hunk header: new proof transcript  
Material effect: bound composite proof.  
Risk category: governed evidence.

Hunk ID: OPR-017  
File: `artifacts/proofs/success_304.txt`  
Patch and hunk header: full proof replacement  
Material effect: generated conditional 304 evidence.  
Risk category: transport evidence.

Hunk ID: OPR-018  
File: `artifacts/proofs/success_304.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed 304 proof transcript.  
Risk category: governed evidence.

Hunk ID: OPR-019  
File: `artifacts/proofs/success_encoding_invariance.txt`  
Patch and hunk header: full proof replacement  
Material effect: consolidated encoding proof at the retained home.  
Risk category: transport/token evidence.

Hunk ID: OPR-020  
File: `artifacts/proofs/success_encoding_invariance.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed encoding proof transcript.  
Risk category: governed evidence.

Hunk ID: OPR-021  
File: `artifacts/proofs/success_get.txt`  
Patch and hunk header: full proof replacement  
Material effect: generated GET evidence.  
Risk category: transport evidence.

Hunk ID: OPR-022  
File: `artifacts/proofs/success_get.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed GET proof transcript.  
Risk category: governed evidence.

Hunk ID: OPR-023  
File: `artifacts/proofs/success_head.txt`  
Patch and hunk header: full proof replacement  
Material effect: generated HEAD evidence.  
Risk category: transport evidence.

Hunk ID: OPR-024  
File: `artifacts/proofs/success_head.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed HEAD proof transcript.  
Risk category: governed evidence.

Hunk ID: OPR-025  
File: `artifacts/proofs/success_writers_errors.txt`  
Patch and hunk header: full proof replacement  
Material effect: generated writer/error evidence.  
Risk category: error/transport evidence.

Hunk ID: OPR-026  
File: `artifacts/proofs/success_writers_errors.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed writer/error transcript.  
Risk category: governed evidence.

Hunk ID: OPR-027  
File: `artifacts/reader/endpoints_snapshot.json`  
Patch and hunk header: canonical snapshot replacement  
Material effect: moved success snapshot from internal-version to Reader.  
Risk category: schema/evidence.

Hunk ID: OPR-028  
File: `artifacts/reader/endpoints_snapshot.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed endpoint-snapshot proof.  
Risk category: governed evidence.

Hunk ID: OPR-029  
File: `audit/EPIC-025_MANIFEST.json`  
Patch and hunk header: generated manifest replacement  
Material effect: removed deleted duplicate proof path.  
Risk category: governed manifest.

Hunk ID: OPR-030  
File: `audit/gates/determinism/abba.bytes`  
Patch and hunk header: new text artifact  
Material effect: added AB/BA identity evidence.  
Risk category: determinism evidence.

Hunk ID: OPR-031  
File: `audit/gates/determinism/abba.bytes.path_proof.txt`  
Patch and hunk header: new proof  
Material effect: bound AB/BA evidence.  
Risk category: governed evidence.

Hunk ID: OPR-032  
File: `audit/gates/determinism/tworun_identity.sha256`  
Patch and hunk header: new text artifact  
Material effect: added two-run identity proof.  
Risk category: determinism evidence.

Hunk ID: OPR-033  
File: `audit/gates/determinism/tworun_identity.sha256.path_proof.txt`  
Patch and hunk header: new proof  
Material effect: bound two-run proof.  
Risk category: governed evidence.

Hunk ID: OPR-034  
File: `audit/gates/parity/reader_cli/ab.json`  
Patch and hunk header: new canonical envelope  
Material effect: added AB Reader/CLI evidence.  
Risk category: public-byte evidence.

Hunk ID: OPR-035  
File: `audit/gates/parity/reader_cli/ab.json.path_proof.txt`  
Patch and hunk header: new proof  
Material effect: bound AB evidence.  
Risk category: governed evidence.

Hunk ID: OPR-036  
File: `audit/gates/parity/reader_cli/ba.json`  
Patch and hunk header: new canonical envelope  
Material effect: added BA Reader/CLI evidence.  
Risk category: public-byte evidence.

Hunk ID: OPR-037  
File: `audit/gates/parity/reader_cli/ba.json.path_proof.txt`  
Patch and hunk header: new proof  
Material effect: bound BA evidence.  
Risk category: governed evidence.

Hunk ID: OPR-038  
File: `audit/gates/parity/reader_cli/summary.json`  
Patch and hunk header: new summary artifact  
Material effect: aggregated determinism predicates.  
Risk category: gate/evidence posture.

Hunk ID: OPR-039  
File: `audit/gates/parity/reader_cli/summary.json.path_proof.txt`  
Patch and hunk header: new proof  
Material effect: bound determinism summary.  
Risk category: governed evidence.

Hunk ID: OPR-040  
File: `audit/gates/topology/orientation_demo.txt`  
Patch and hunk header: generated orientation replacement  
Material effect: refreshed topology counts.  
Risk category: governed evidence.

Hunk ID: OPR-041  
File: `audit/gates/topology/orientation_demo.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed orientation proof.  
Risk category: governed evidence.

Hunk ID: OPR-042  
File: `audit/qa/hde-epic025/qa_step_logs_manifest.json`  
Patch and hunk header: generated manifest replacement  
Material effect: repaired historical manifest dependencies.  
Risk category: QA/governed manifest.

Hunk ID: OPR-043  
File: `audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed historical manifest proof.  
Risk category: governed evidence.

Hunk ID: OPR-044  
File: `audit/qa/hde-epic028/acceptance_map_viability.log`  
Patch and hunk header: generated viability replacement  
Material effect: rebound historical acceptance coverage.  
Risk category: token/acceptance posture.

Hunk ID: OPR-045  
File: `audit/qa/hde-epic028/acceptance_map_viability.log.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed viability proof.  
Risk category: governed evidence.

Hunk ID: OPR-046  
File: `audit/qa/hde-epic028/token_evidence_matrix.md`  
Patch and hunk header: generated matrix replacement  
Material effect: rebound encoding token to retained proof.  
Risk category: token posture.

Hunk ID: OPR-047  
File: `audit/qa/hde-epic028/token_evidence_matrix.md.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed matrix proof.  
Risk category: governed evidence.

Hunk ID: OPR-048  
File: `docs/ENDPOINTS_CATALOG.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed authoritative Catalog proof.  
Risk category: governed Catalog evidence.

Hunk ID: OPR-049  
File: `docs/ENDPOINTS_CATALOG.json.sha256`  
Patch and hunk header: checksum replacement  
Material effect: refreshed authoritative Catalog checksum.  
Risk category: governed Catalog evidence.

Hunk ID: OPR-050  
File: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed checksum proof.  
Risk category: governed evidence.

Hunk ID: OPR-051  
File: `docs/acceptance_map_epic028.json`  
Patch and hunk header: generated map replacement  
Material effect: rebound historical encoding token.  
Risk category: acceptance/token posture.

Hunk ID: OPR-052  
File: `docs/acceptance_map_epic028.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed acceptance-map proof.  
Risk category: governed evidence.

Hunk ID: OPR-053  
File: `docs/evidence/INDEX.json`  
Patch and hunk header: generated canonical Index replacement  
Material effect: registered PR-02 artifacts and removed obsolete proof.  
Risk category: Human Evidence Index.

Hunk ID: OPR-054  
File: `docs/evidence/INDEX.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed Human Index proof.  
Risk category: governed evidence.

Hunk ID: OPR-055  
File: `docs/evidence/INDEX.sha256`  
Patch and hunk header: sentinel replacement  
Material effect: refreshed Human Index hash.  
Risk category: governed evidence.

Hunk ID: OPR-056  
File: `docs/evidence/INDEX.sha256.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshed sentinel proof.  
Risk category: governed evidence.

Hunk ID: OPR-057  
File: `schemas/proofs.reader_success.v1.json`  
Patch and hunk header: new JSON Schema  
Material effect: introduced composite A7 schema.  
Risk category: schema/data model.

Hunk ID: OPR-058  
File: `schemas/proofs.reader_success.v1.json.path_proof.txt`  
Patch and hunk header: new proof  
Material effect: bound the schema.  
Risk category: governed evidence.

Hunk ID: OPR-059  
File: `tests/evidence/test_determinism_gate_proofs.py`  
Patch and hunk header: new test module  
Material effect: added initial determinism tests.  
Risk category: test sufficiency.

Hunk ID: OPR-060  
File: `tests/http/test_endpoint_catalog.py`  
Patch and hunk header: test replacement  
Material effect: added initial strict Catalog tests.  
Risk category: schema tests.

Hunk ID: OPR-061  
File: `tests/http/test_reader_a7_transport.py`  
Patch and hunk header: proof-writer cleanup hunk  
Material effect: removed obsolete path but retained independent test-side writes.  
Risk category: test safety/single-writer.

Hunk ID: OPR-062  
File: `tests/transport/test_a7_transport_proofs.py`  
Patch and hunk header: new test module  
Material effect: added initial A7 producer tests.  
Risk category: test sufficiency.

Hunk ID: OPR-063  
File: `tools/evidence/generate_a7_transport_proofs.py`  
Patch and hunk header: new producer  
Material effect: created Catalog, A7 captures, proof rendering, write guard, and check mode.  
Risk category: contract/schema/evidence.

Hunk ID: OPR-064  
File: `tools/evidence/generate_determinism_gate_proofs.py`  
Patch and hunk header: new producer  
Material effect: created Reader/CLI, AB/BA, two-run, preimage, and canonical evidence.  
Risk category: gate/evidence.

Hunk ID: OPR-065  
File: `tools/evidence/update_evidence_index.py`  
Patch and hunk header: PR-02 registration additions  
Material effect: registered new artifacts.  
Risk category: canonical evidence writer.

Hunk ID: OPR-066  
File: `tools/qa/generate_epic025_close_pack.py`  
Patch and hunk header: obsolete-path removal  
Material effect: repaired historical manifest.  
Risk category: historical governed evidence.

Hunk ID: OPR-067  
File: `tools/qa/generate_epic028_acceptance_ledger.py`  
Patch and hunk header: proof-path replacement  
Material effect: regenerated historical acceptance bindings.  
Risk category: token/acceptance posture.

#### Remedial PR Material Hunk Ledger

Hunk ID: RPR-001  
File: `adapter/http_reader.py`  
Patch and hunk header: `diff --git a/adapter/http_reader.py b/adapter/http_reader.py` || internal sampler comment hunk  
Material effect: clarifies that the sampler is Cataloged internally but excluded from A7 and public contracts.  
Risk category: contract documentation.  
Evidence pointer: Remedial PR | diff | `"included in the internal Endpoint Catalog"` | `"excluded from A7"`

Hunk ID: RPR-002  
File: `artifacts/audit/ENDPOINTS_CATALOG.json`  
Patch and hunk header: whole Catalog replacement  
Material effect: adds `POST /internal/dev/sampler` with bounded internal posture.  
Risk category: schema/governed evidence.

Hunk ID: RPR-003  
File: `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes truthful current proof metadata.  
Risk category: governed evidence.

Hunk ID: RPR-004  
File: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`  
Patch and hunk header: checksum replacement  
Material effect: refreshes Catalog audit checksum.  
Risk category: governed evidence.

Hunk ID: RPR-005  
File: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes checksum proof.  
Risk category: governed evidence.

Hunk ID: RPR-006  
File: `artifacts/cards/a3/IDENTITY_OK.txt`  
Patch and hunk header: marker regeneration  
Material effect: binds marker to authoritative canonical-gate predicate.  
Risk category: gate/token evidence.

Hunk ID: RPR-007  
File: `artifacts/cards/a3/IDENTITY_OK.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes marker proof.  
Risk category: governed evidence.

Hunk ID: RPR-008  
File: `artifacts/evidence_index.jsonl`  
Patch and hunk header: Mirror regeneration  
Material effect: updates remediated evidence identities and semantic bindings.  
Risk category: Machine Mirror.

Hunk ID: RPR-009  
File: `artifacts/evidence_index.jsonl.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes Mirror proof.  
Risk category: governed evidence.

Hunk ID: RPR-010  
File: `artifacts/evidence_index.jsonl.sha256`  
Patch and hunk header: checksum replacement  
Material effect: refreshes Mirror checksum.  
Risk category: governed evidence.

Hunk ID: RPR-011  
File: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes checksum proof.  
Risk category: governed evidence.

Hunk ID: RPR-012  
File: `artifacts/proofs/endpoints_env_gate_proof.log`  
Patch and hunk header: deterministic proof regeneration  
Material effect: preserves env-gate facts under corrected producer.  
Risk category: environment evidence.

Hunk ID: RPR-013  
File: `artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: replaces historical chronology with truthful current metadata.  
Risk category: governed evidence.

Hunk ID: RPR-014  
File: `artifacts/proofs/reader_success_get_head_304.json`  
Patch and hunk header: canonical artifact replacement  
Material effect: adopts exact PF12 composite shape.  
Risk category: schema/evidence.

Hunk ID: RPR-015  
File: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes composite proof.  
Risk category: governed evidence.

Hunk ID: RPR-016  
File: `artifacts/proofs/success_304.txt`  
Patch and hunk header: proof regeneration  
Material effect: records and enforces full 304 cache/Vary/entity-header posture.  
Risk category: transport evidence.

Hunk ID: RPR-017  
File: `artifacts/proofs/success_304.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes truthful current metadata.  
Risk category: governed evidence.

Hunk ID: RPR-018  
File: `artifacts/proofs/success_encoding_invariance.txt`  
Patch and hunk header: proof regeneration  
Material effect: records per-encoding ETag and HEAD identity-length invariants.  
Risk category: transport/token evidence.

Hunk ID: RPR-019  
File: `artifacts/proofs/success_encoding_invariance.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes truthful proof metadata.  
Risk category: governed evidence.

Hunk ID: RPR-020  
File: `artifacts/proofs/success_get.txt`  
Patch and hunk header: proof regeneration  
Material effect: preserves canonical GET evidence under strict producer.  
Risk category: transport evidence.

Hunk ID: RPR-021  
File: `artifacts/proofs/success_get.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes truthful current metadata.  
Risk category: governed evidence.

Hunk ID: RPR-022  
File: `artifacts/proofs/success_head.txt`  
Patch and hunk header: proof regeneration  
Material effect: records complete GET/HEAD parity and identity-length posture.  
Risk category: transport evidence.

Hunk ID: RPR-023  
File: `artifacts/proofs/success_head.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes truthful current metadata.  
Risk category: governed evidence.

Hunk ID: RPR-024  
File: `artifacts/proofs/success_writers_errors.txt`  
Patch and hunk header: proof regeneration  
Material effect: records canonical error body, content type, cache, ETag, and conditional behavior.  
Risk category: error/transport evidence.

Hunk ID: RPR-025  
File: `artifacts/proofs/success_writers_errors.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes truthful current metadata.  
Risk category: governed evidence.

Hunk ID: RPR-026  
File: `artifacts/reader/endpoints_snapshot.json`  
Patch and hunk header: canonical snapshot replacement  
Material effect: adopts PF12 `generated_at_utc`, `endpoints`, and `envelope_keys`.  
Risk category: schema/evidence.

Hunk ID: RPR-027  
File: `artifacts/reader/endpoints_snapshot.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes snapshot proof.  
Risk category: governed evidence.

Hunk ID: RPR-028  
File: `audit/gates/parity/reader_cli/summary.json`  
Patch and hunk header: summary regeneration  
Material effect: records authoritative canonical-gate command/result provenance.  
Risk category: gate/evidence.

Hunk ID: RPR-029  
File: `audit/gates/parity/reader_cli/summary.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes summary proof.  
Risk category: governed evidence.

Hunk ID: RPR-030  
File: `audit/qa/hde-epic028/acceptance_map_viability.log`  
Patch and hunk header: generated viability replacement  
Material effect: bases coverage on complete encoding predicates.  
Risk category: token/acceptance posture.

Hunk ID: RPR-031  
File: `audit/qa/hde-epic028/acceptance_map_viability.log.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes viability proof.  
Risk category: governed evidence.

Hunk ID: RPR-032  
File: `audit/qa/hde-epic028/token_evidence_matrix.md`  
Patch and hunk header: generated matrix replacement  
Material effect: makes encoding-token row evidence-sensitive rather than path-sensitive.  
Risk category: token posture.

Hunk ID: RPR-033  
File: `audit/qa/hde-epic028/token_evidence_matrix.md.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes matrix proof.  
Risk category: governed evidence.

Hunk ID: RPR-034  
File: `docs/ENDPOINTS_CATALOG.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes authoritative Catalog proof with truthful metadata.  
Risk category: governed evidence.

Hunk ID: RPR-035  
File: `docs/ENDPOINTS_CATALOG.json.sha256`  
Patch and hunk header: checksum replacement  
Material effect: refreshes checksum after sampler inclusion.  
Risk category: governed evidence.

Hunk ID: RPR-036  
File: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes checksum proof.  
Risk category: governed evidence.

Hunk ID: RPR-037  
File: `docs/acceptance_map_epic028.json`  
Patch and hunk header: generated map replacement  
Material effect: grounds encoding token in complete proof predicates.  
Risk category: acceptance/token posture.

Hunk ID: RPR-038  
File: `docs/acceptance_map_epic028.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes acceptance-map proof.  
Risk category: governed evidence.

Hunk ID: RPR-039  
File: `docs/evidence/INDEX.json`  
Patch and hunk header: Index regeneration  
Material effect: updates corrected evidence identities.  
Risk category: Human Evidence Index.

Hunk ID: RPR-040  
File: `docs/evidence/INDEX.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes Human Index proof.  
Risk category: governed evidence.

Hunk ID: RPR-041  
File: `docs/evidence/INDEX.sha256`  
Patch and hunk header: sentinel replacement  
Material effect: refreshes Human Index hash.  
Risk category: governed evidence.

Hunk ID: RPR-042  
File: `docs/evidence/INDEX.sha256.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes sentinel proof.  
Risk category: governed evidence.

Hunk ID: RPR-043  
File: `schemas/proofs.reader_success.v1.json`  
Patch and hunk header: schema replacement  
Material effect: adopts exact PF12 field model and nested unknown-key rejection.  
Risk category: schema/data model.

Hunk ID: RPR-044  
File: `schemas/proofs.reader_success.v1.json.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes schema proof.  
Risk category: governed evidence.

Hunk ID: RPR-045  
File: `tests/evidence/test_determinism_gate_proofs.py`  
Patch and hunk header: expanded executable-test hunks  
Material effect: exercises actual gate, write mode, check mode, failure, and atomicity.  
Risk category: test sufficiency.

Hunk ID: RPR-046  
File: `tests/http/test_endpoint_catalog.py`  
Patch and hunk header: expanded Catalog-test hunks  
Material effect: validates complete record schema and sampler inclusion.  
Risk category: schema tests.

Hunk ID: RPR-047  
File: `tests/http/test_reader_a7_transport.py`  
Patch and hunk header: writer-removal hunk  
Material effect: removes independent governed artifact writes.  
Risk category: single-writer/test safety.

Hunk ID: RPR-048  
File: `tests/transport/test_a7_transport_proofs.py`  
Patch and hunk header: expanded executable-test hunks  
Material effect: exercises write/check, malformed transport, schema, encoding-length, and restoration paths.  
Risk category: test sufficiency.

Hunk ID: RPR-049  
File: `tools/evidence/generate_a7_transport_proofs.py`  
Patch and hunk header: producer validation and rendering hunks  
Material effect: implements complete fail-closed Catalog and A7 requirements.  
Risk category: contract/schema/evidence.

Hunk ID: RPR-050  
File: `tools/evidence/generate_determinism_gate_proofs.py`  
Patch and hunk header: canonical-gate integration hunks  
Material effect: replaces caller Boolean with authoritative gate provenance.  
Risk category: gate/evidence.

Hunk ID: RPR-051  
File: `tools/evidence/update_evidence_index.py`  
Patch and hunk header: semantic-validation and metadata-refresh hunks  
Material effect: prevents invalid PR-02 evidence from being indexed.  
Risk category: canonical evidence writer.

Hunk ID: RPR-052  
File: `tools/qa/generate_epic028_acceptance_ledger.py`  
Patch and hunk header: predicate-validation hunks  
Material effect: prevents path-exists-only token implementation claims.  
Risk category: token/acceptance posture.

Hunk ID: RPR-053  
File: `audit/gates/topology/orientation_demo.txt`  
Patch and hunk header: generated orientation replacement  
Material effect: refreshes topology after corrected Index.  
Risk category: governed evidence.

Hunk ID: RPR-054  
File: `audit/gates/topology/orientation_demo.txt.path_proof.txt`  
Patch and hunk header: proof replacement  
Material effect: refreshes orientation proof.  
Risk category: governed evidence.

### Net Effective Diff Review

NET-001  
File/artifact: `artifacts/audit/ENDPOINTS_CATALOG.json`  
Covered hunks: OPR-001 / RPR-002  
Combined merged state: strict internal Catalog with one A7 success designation and `POST /internal/dev/sampler` represented as internal, dev-only, and non-A7.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
High-risk hunk assessment: unique `(method,path)` records, typed fields, valid classifications, bounded sampler posture, and one `GET /reader` designation are enforced.  
Assessment: complete.  
Evidence pointer(s): Remedial PR Catalog diff and Catalog tests.  
GitHub Repo proof: current Catalog.  
PF reference, if relied on: PF12 Â§8.8; PO sampler decision.

NET-002  
File/artifact: `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt`  
Covered hunks: OPR-002 / RPR-003  
Combined merged state: current truthful Catalog proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-003  
File/artifact: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`  
Covered hunks: OPR-003 / RPR-004  
Combined merged state: checksum matches current Catalog.  
Current final repo state: same.  
Later-change impact: None.  
Risk: Medium.  
Assessment: coherent.

NET-004  
File/artifact: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`  
Covered hunks: OPR-004 / RPR-005  
Combined merged state: current checksum proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-005  
File/artifact: `artifacts/cards/a3/IDENTITY_OK.txt`  
Covered hunks: OPR-005 / RPR-006  
Combined merged state: marker depends on all grounded determinism predicates and retains token nonclaim.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
High-risk hunk assessment: no caller-default gate shortcut remains in normal execution.  
Assessment: complete.

NET-006  
File/artifact: `artifacts/cards/a3/IDENTITY_OK.txt.path_proof.txt`  
Covered hunks: OPR-006 / RPR-007  
Combined merged state: current marker proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-007  
File/artifact: `artifacts/evidence_index.jsonl`  
Covered hunks: OPR-007 / RPR-008  
Combined merged state: corrected PR-02 primary identities are represented in the Machine Mirror.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
High-risk hunk assessment: semantic validation occurs before Mirror emission.  
Assessment: complete.

NET-008  
File/artifact: `artifacts/evidence_index.jsonl.path_proof.txt`  
Covered hunks: OPR-008 / RPR-009  
Combined merged state: current Mirror proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-009  
File/artifact: `artifacts/evidence_index.jsonl.sha256`  
Covered hunks: OPR-009 / RPR-010  
Combined merged state: checksum matches corrected Mirror.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-010  
File/artifact: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
Covered hunks: OPR-010 / RPR-011  
Combined merged state: current checksum proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-011  
File/artifact: `artifacts/proofs/encoding_invariance.txt`  
Covered hunks: OPR-011 / None  
Combined merged state: deleted.  
Current final repo state: absent.  
Later-change impact: None.  
Risk: Medium.  
Assessment: no net governed duplicate remains.  
GitHub Repo proof: deleted-path search returned 0 active bindings.

NET-012  
File/artifact: `artifacts/proofs/encoding_invariance.txt.path_proof.txt`  
Covered hunks: OPR-012 / None  
Combined merged state: deleted.  
Current final repo state: absent.  
Later-change impact: None.  
Risk: Medium.  
Assessment: coherent deletion.

NET-013  
File/artifact: `artifacts/proofs/endpoints_env_gate_proof.log`  
Covered hunks: OPR-013 / RPR-012  
Combined merged state: deterministic production-gate proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-014  
File/artifact: `artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt`  
Covered hunks: OPR-014 / RPR-013  
Combined merged state: current truthful proof metadata.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: chronology defect closed.

NET-015  
File/artifact: `artifacts/proofs/reader_success_get_head_304.json`  
Covered hunks: OPR-015 / RPR-014  
Combined merged state: exact PF12 composite proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
High-risk hunk assessment: actual governed schema validation and nested unknown-key rejection are enforced.  
Assessment: complete.

NET-016  
File/artifact: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`  
Covered hunks: OPR-016 / RPR-015  
Combined merged state: current proof transcript.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-017  
File/artifact: `artifacts/proofs/success_304.txt`  
Covered hunks: OPR-017 / RPR-016  
Combined merged state: complete 304 evidence, including cache and Vary parity.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-018  
File/artifact: `artifacts/proofs/success_304.txt.path_proof.txt`  
Covered hunks: OPR-018 / RPR-017  
Combined merged state: truthful current transcript.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-019  
File/artifact: `artifacts/proofs/success_encoding_invariance.txt`  
Covered hunks: OPR-019 / RPR-018  
Combined merged state: per-encoding ETag and HEAD identity-length proof for `identity`, `gzip`, and `br`.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
High-risk hunk assessment: decisive equality predicates are recorded and validated.  
Assessment: complete.

NET-020  
File/artifact: `artifacts/proofs/success_encoding_invariance.txt.path_proof.txt`  
Covered hunks: OPR-020 / RPR-019  
Combined merged state: current truthful transcript.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-021  
File/artifact: `artifacts/proofs/success_get.txt`  
Covered hunks: OPR-021 / RPR-020  
Combined merged state: complete GET proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-022  
File/artifact: `artifacts/proofs/success_get.txt.path_proof.txt`  
Covered hunks: OPR-022 / RPR-021  
Combined merged state: current truthful transcript.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-023  
File/artifact: `artifacts/proofs/success_head.txt`  
Covered hunks: OPR-023 / RPR-022  
Combined merged state: complete GET/HEAD parity and identity-length proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-024  
File/artifact: `artifacts/proofs/success_head.txt.path_proof.txt`  
Covered hunks: OPR-024 / RPR-023  
Combined merged state: current truthful transcript.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-025  
File/artifact: `artifacts/proofs/success_writers_errors.txt`  
Covered hunks: OPR-025 / RPR-024  
Combined merged state: canonical error body, content type, no-store, no-ETag, and non-304 proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-026  
File/artifact: `artifacts/proofs/success_writers_errors.txt.path_proof.txt`  
Covered hunks: OPR-026 / RPR-025  
Combined merged state: current truthful transcript.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-027  
File/artifact: `artifacts/reader/endpoints_snapshot.json`  
Covered hunks: OPR-027 / RPR-026  
Combined merged state: PF12 names-only Reader snapshot.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-028  
File/artifact: `artifacts/reader/endpoints_snapshot.json.path_proof.txt`  
Covered hunks: OPR-028 / RPR-027  
Combined merged state: current snapshot proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-029  
File/artifact: `audit/EPIC-025_MANIFEST.json`  
Covered hunks: OPR-029 / None  
Combined merged state: obsolete encoding path removed.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: historical integrity preserved.

NET-030  
File/artifact: `audit/gates/determinism/abba.bytes`  
Covered hunks: OPR-030 / None  
Combined merged state: AB/BA identity evidence retained.  
Current final repo state: same.  
Later-change impact: None.  
Risk: Medium.  
Assessment: complete.

NET-031  
File/artifact: `audit/gates/determinism/abba.bytes.path_proof.txt`  
Covered hunks: OPR-031 / None  
Combined merged state: proof retained.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-032  
File/artifact: `audit/gates/determinism/tworun_identity.sha256`  
Covered hunks: OPR-032 / None  
Combined merged state: independent two-run evidence retained.  
Current final repo state: same.  
Later-change impact: None.  
Risk: Medium.  
Assessment: complete.

NET-033  
File/artifact: `audit/gates/determinism/tworun_identity.sha256.path_proof.txt`  
Covered hunks: OPR-033 / None  
Combined merged state: proof retained.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-034  
File/artifact: `audit/gates/parity/reader_cli/ab.json`  
Covered hunks: OPR-034 / None  
Combined merged state: canonical AB evidence retained.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-035  
File/artifact: `audit/gates/parity/reader_cli/ab.json.path_proof.txt`  
Covered hunks: OPR-035 / None  
Combined merged state: proof retained.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-036  
File/artifact: `audit/gates/parity/reader_cli/ba.json`  
Covered hunks: OPR-036 / None  
Combined merged state: canonical BA evidence retained.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-037  
File/artifact: `audit/gates/parity/reader_cli/ba.json.path_proof.txt`  
Covered hunks: OPR-037 / None  
Combined merged state: proof retained.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-038  
File/artifact: `audit/gates/parity/reader_cli/summary.json`  
Covered hunks: OPR-038 / RPR-028  
Combined merged state: aggregate summary is bound to the authoritative canonical-gate check and fails closed.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: Original aggregate defect closed.

NET-039  
File/artifact: `audit/gates/parity/reader_cli/summary.json.path_proof.txt`  
Covered hunks: OPR-039 / RPR-029  
Combined merged state: current summary proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-040  
File/artifact: `audit/gates/topology/orientation_demo.txt`  
Covered hunks: OPR-040 / RPR-053  
Combined merged state: orientation reflects final corrected evidence topology.  
Current final repo state: same.  
Later-change impact: None.  
Risk: Medium.  
Assessment: coherent.

NET-041  
File/artifact: `audit/gates/topology/orientation_demo.txt.path_proof.txt`  
Covered hunks: OPR-041 / RPR-054  
Combined merged state: current orientation proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-042  
File/artifact: `audit/qa/hde-epic025/qa_step_logs_manifest.json`  
Covered hunks: OPR-042 / None  
Combined merged state: no dangling deleted proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-043  
File/artifact: `audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt`  
Covered hunks: OPR-043 / None  
Combined merged state: current historical manifest proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-044  
File/artifact: `audit/qa/hde-epic028/acceptance_map_viability.log`  
Covered hunks: OPR-044 / RPR-030  
Combined merged state: coverage is derived from complete encoding invariants.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: token-truth defect closed.

NET-045  
File/artifact: `audit/qa/hde-epic028/acceptance_map_viability.log.path_proof.txt`  
Covered hunks: OPR-045 / RPR-031  
Combined merged state: current viability proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-046  
File/artifact: `audit/qa/hde-epic028/token_evidence_matrix.md`  
Covered hunks: OPR-046 / RPR-032  
Combined merged state: encoding-token row is predicate-backed.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: truthful.

NET-047  
File/artifact: `audit/qa/hde-epic028/token_evidence_matrix.md.path_proof.txt`  
Covered hunks: OPR-047 / RPR-033  
Combined merged state: current matrix proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-048  
File/artifact: `docs/ENDPOINTS_CATALOG.json.path_proof.txt`  
Covered hunks: OPR-048 / RPR-034  
Combined merged state: current truthful Catalog proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: chronology defect closed.

NET-049  
File/artifact: `docs/ENDPOINTS_CATALOG.json.sha256`  
Covered hunks: OPR-049 / RPR-035  
Combined merged state: checksum matches sampler-inclusive Catalog.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-050  
File/artifact: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`  
Covered hunks: OPR-050 / RPR-036  
Combined merged state: current truthful checksum proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-051  
File/artifact: `docs/acceptance_map_epic028.json`  
Covered hunks: OPR-051 / RPR-037  
Combined merged state: encoding token is backed by complete retained proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: truthful.

NET-052  
File/artifact: `docs/acceptance_map_epic028.json.path_proof.txt`  
Covered hunks: OPR-052 / RPR-038  
Combined merged state: current map proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-053  
File/artifact: `docs/evidence/INDEX.json`  
Covered hunks: OPR-053 / RPR-039  
Combined merged state: corrected PR-02 evidence is canonically indexed.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-054  
File/artifact: `docs/evidence/INDEX.json.path_proof.txt`  
Covered hunks: OPR-054 / RPR-040  
Combined merged state: current Index proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-055  
File/artifact: `docs/evidence/INDEX.sha256`  
Covered hunks: OPR-055 / RPR-041  
Combined merged state: current Index sentinel.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-056  
File/artifact: `docs/evidence/INDEX.sha256.path_proof.txt`  
Covered hunks: OPR-056 / RPR-042  
Combined merged state: current sentinel proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-057  
File/artifact: `schemas/proofs.reader_success.v1.json`  
Covered hunks: OPR-057 / RPR-043  
Combined merged state: exact PF12 composite schema with nested unknown-key rejection.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-058  
File/artifact: `schemas/proofs.reader_success.v1.json.path_proof.txt`  
Covered hunks: OPR-058 / RPR-044  
Combined merged state: current schema proof.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: coherent.

NET-059  
File/artifact: `tests/evidence/test_determinism_gate_proofs.py`  
Covered hunks: OPR-059 / RPR-045  
Combined merged state: real gate, write, check, failure, and atomicity paths are exercised.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: sufficient.

NET-060  
File/artifact: `tests/http/test_endpoint_catalog.py`  
Covered hunks: OPR-060 / RPR-046  
Combined merged state: complete Catalog record, designation, sampler, and method coverage.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: sufficient.

NET-061  
File/artifact: `tests/http/test_reader_a7_transport.py`  
Covered hunks: OPR-061 / RPR-047  
Combined merged state: no independent governed artifact writer remains.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: single-writer defect closed.

NET-062  
File/artifact: `tests/transport/test_a7_transport_proofs.py`  
Covered hunks: OPR-062 / RPR-048  
Combined merged state: executable complete negative and non-writing coverage.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: sufficient.

NET-063  
File/artifact: `tools/evidence/generate_a7_transport_proofs.py`  
Covered hunks: OPR-063 / RPR-049  
Combined merged state: sole A7 writer; strict Catalog validation; complete transport predicates; actual schema validation; write guard; non-writing check mode.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-064  
File/artifact: `tools/evidence/generate_determinism_gate_proofs.py`  
Covered hunks: OPR-064 / RPR-050  
Combined merged state: deterministic aggregate consumes authoritative canonical-gate result and fails closed.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-065  
File/artifact: `tools/evidence/update_evidence_index.py`  
Covered hunks: OPR-065 / RPR-051  
Combined merged state: PR-02 semantic validation precedes canonical Index/Mirror emission; proof metadata is truthful.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: complete.

NET-066  
File/artifact: `tools/qa/generate_epic025_close_pack.py`  
Covered hunks: OPR-066 / None  
Combined merged state: deleted proof path remains excluded.  
Current final repo state: same.  
Later-change impact: None.  
Risk: Medium.  
Assessment: complete.

NET-067  
File/artifact: `tools/qa/generate_epic028_acceptance_ledger.py`  
Covered hunks: OPR-067 / RPR-052  
Combined merged state: encoding token implementation depends on decisive proof content.  
Current final repo state: same.  
Later-change impact: None.  
Risk: High.  
Assessment: truthful.

NET-068  
File/artifact: `adapter/http_reader.py`  
Covered hunks: None / RPR-001  
Combined merged state: runtime unchanged; comment distinguishes internal Catalog inclusion from A7/public exclusion.  
Current final repo state: same.  
Later-change impact: None.  
Risk: Low.  
Assessment: PO Catalog decision accurately reflected.

### Validation & Evidence Review

VAL-001

Purpose: Prove both PRs are merged.

Source: Original PR / Remedial PR

Check/workflow/artifact/method: GitHub PR metadata.

Result: PASS

Observation: Both PRs are closed and merged, with resolvable base, head, and merge identifiers.

Evidence pointer: Original PR | API field `merged` | `"true"` | `"merge_commit_sha=ceefe4f52f12c0dcb57c9721639b720a539be96a"`; Remedial PR | API field `merged` | `"true"` | `"merge commit equals current main HEAD"`

Why it matters: Establishes the requested two-attempt lifecycle.

VAL-002

Purpose: Prove direct lifecycle lineage.

Source: GitHub Repo

Check/workflow/artifact/method: PR base fields and commit comparison.

Result: PASS

Observation: Remedial PRâ€™s base is Original PRâ€™s merge state.

Evidence pointer: GitHub Repo | compare Original merge to Remedial merge | `"ahead"` | `"no unrelated intervening lineage"`

Why it matters: Remedial PR is a direct correction of the first attempt.

VAL-003

Purpose: Prove complete lifecycle touched-file coverage.

Source: Original PR / Remedial PR

Check/workflow/artifact/method: complete changed-file lists, per-file patches, and baseline-to-current comparison.

Result: PASS

Observation: Every Original and Remedial material hunk is represented in the ledgers and every union path appears once in NET-001 through NET-068.

Evidence pointer: Original PR | `changed_files=67` | complete diff; Remedial PR | complete changed-file list | complete diff

Why it matters: No material source or artifact change is omitted.

VAL-004

Purpose: Verify current state has no later divergence.

Source: GitHub Repo

Check/workflow/artifact/method: default-branch commit history.

Result: PASS

Observation: Current `main` equals the Remedial PR merge state and has no later commit.

Evidence pointer: GitHub Repo | history search | `"0 later commits"` | `"HEAD = remedial merge"`

Why it matters: Current-state assertions remain attributable to this lifecycle.

VAL-005

Purpose: Verify authoritative canonical-gate binding.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: source inspection and focused tests.

Result: PASS

Observation: Normal determinism generation invokes or consumes the established read-only canonical-gate result; production execution no longer accepts an implicit success Boolean.

Evidence pointer: Remedial PR | determinism producer/test | `"--check-only"` | fail-closed failure/unavailable tests

Why it matters: The aggregate determinism proof is no longer self-asserting.

VAL-006

Purpose: Verify PF12 composite schema conformance.

Source: Remedial PR / PF12 â€” HDE-Schemas & Artifacts

Check/workflow/artifact/method: field-by-field schema and artifact inspection; JSON Schema validation tests.

Result: PASS

Observation: Current schema and artifact use the required top-level keys and exact nested invariant fields, with unknown-key rejection.

Evidence pointer: Remedial PR | schema/artifact/test | `"route_path"` | `"etag"`

Why it matters: The governed composite proof now implements its canonical contract.

VAL-007

Purpose: Verify PF12 endpoint-snapshot conformance.

Source: Remedial PR / PF12 â€” HDE-Schemas & Artifacts

Check/workflow/artifact/method: current artifact inspection and focused tests.

Result: PASS

Observation: Snapshot contains deterministic `generated_at_utc`, names-only Reader success endpoints, and names-only envelope keys.

Evidence pointer: GitHub Repo | `artifacts/reader/endpoints_snapshot.json` | `"generated_at_utc"` | `"envelope_keys"`

Why it matters: The required Catalog-derived snapshot now exists.

VAL-008

Purpose: Verify complete A7 fail-closed transport predicates.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: producer inspection and malformed-response tests.

Result: PASS

Observation: GET, HEAD, 304, error, env-gate, Vary, cache, content type, entity headers, canonical body, ETag, and length failures all fail the proof producer.

Evidence pointer: Remedial PR | A7 producer/tests | malformed HEAD and 304 cases | malformed error cases

Why it matters: Required transport regressions cannot silently pass.

VAL-009

Purpose: Verify complete encoding invariance.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: current proof and focused tests.

Result: PASS

Observation: `identity`, `gzip`, and `br` each record the same identity ETag and HEAD identity length; mismatch tests fail.

Evidence pointer: GitHub Repo | `success_encoding_invariance.txt` | three encoding records | derived ETag and length equality predicates

Why it matters: The retained proof now supports the decisive A7 encoding invariant.

VAL-010

Purpose: Verify single A7 proof-writer ownership.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: code search and test inspection.

Result: PASS

Observation: `generate_a7_transport_proofs.py` is the only writer for the governed A7 family. Reader transport tests no longer render those artifacts independently.

Search method: searched for direct writes to the seven governed A7 proof paths (case: sensitive); scope: current Repo Python sources and tests; tool: GitHub search/manual scan; result: one production owner.

Why it matters: Evidence bytes are deterministic and owner-controlled.

VAL-011

Purpose: Verify real write/check and atomic-failure tests.

Source: Remedial PR

Check/workflow/artifact/method: focused test inspection and workflow result.

Result: PASS

Observation: Tests invoke actual normal mode and `--check`, enforce `HDE_WRITE_A7_PROOFS=1`, prove no writes on failure, prove non-writing checks, and validate environment restoration.

Evidence pointer: Remedial PR | test modules | actual `main()` calls | before/after artifact comparisons

Why it matters: The originally untested execution paths are now protected.

VAL-012

Purpose: Verify Catalog completeness and sampler decision.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: current Catalog and tests.

Result: PASS

Observation: `POST /internal/dev/sampler` appears exactly once, is internal and non-A7-eligible, is absent from `success_endpoints`, and GET remains unsupported.

Evidence pointer: GitHub Repo | Catalog | `"POST /internal/dev/sampler"` | `"a7_eligible:false"`

Why it matters: Resolves the PO decision without broadening public or A7 scope.

VAL-013

Purpose: Verify path-proof chronology.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: changed proof transcripts and updater tests.

Result: PASS

Observation: Regenerated proof transcripts contain current artifact hashes and truthful current metadata; historical timestamps are no longer carried forward for changed bytes.

Evidence pointer: Remedial PR | path-proof diffs | current hash | current truthful metadata

Why it matters: Governing proof chronology is accurate.

VAL-014

Purpose: Verify historical token truthfulness.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: encoding proof, EPIC028 generator, map, matrix, and viability log.

Result: PASS

Observation: `A7_ENCODING_INVARIANCE_OK` is emitted as implemented only when all three encoding ETags and HEAD identity lengths are present and equal.

Evidence pointer: Remedial PR | acceptance-ledger generator/test | decisive predicate validation | current token artifacts

Why it matters: Historical acceptance artifacts no longer overclaim evidence support.

VAL-015

Purpose: Verify canonical evidence integration.

Source: Remedial PR / GitHub Repo

Check/workflow/artifact/method: updater semantic validation and visible repository-host checks.

Result: PASS

Observation: Invalid PR-02 evidence fails before Human Index/Mirror emission; final Index, sentinel, Mirror, checksum, proofs, and orientation checks pass.

Evidence pointer: Remedial PR | updater tests | semantic preconditions; GitHub Repo | workflow | evidence checks successful

Why it matters: Governed evidence reflects valid primaries rather than path existence alone.

VAL-016

Purpose: Verify PR-02 exclusions.

Source: GitHub Repo / Implementation Doc

Check/workflow/artifact/method: baseline-to-current diff scan.

Result: PASS

Observation: No new public route, Reader payload field, reusable PR-03 rails job, DB posture work, mapped-cache work, PR-06 aggregate pipeline, OPS execution, deployment, migration, or PF-Canon edit was added.

Search method: searched lifecycle diff for PF-Canon paths, deployment files, migrations, and new public route decorators (case: sensitive); scope: combined diff; tool: GitHub API/manual scan; result: 0 unauthorized additions.

Why it matters: Combined work remains within the approved PR-02 boundary.

VAL-017

Purpose: Verify visible repository-host validation.

Source: Original PR / Remedial PR

Check/workflow/artifact/method: workflow/check inspection.

Result: PASS

Observation: Both merged attempts completed their visible required checks; the Remedial PR includes the strengthened targeted tests and retained global safeguards.

Evidence pointer: GitHub Repo | workflow checks | `"completed"` | `"success"`

Why it matters: Supports integration and regression posture alongside final-file review.

VAL-018

Purpose: Verify reviewer-local execution.

Source: Review method

Check/workflow/artifact/method: local command availability.

Result: NOT RUN

Observation: No local checkout was available to the reviewer; no local command is claimed.

Evidence pointer: Review method | connector-backed GitHub inspection | `"no local mutation"` | `"no local execution claim"`

Why it matters: Non-blocking because exact diffs, current files, focused behavioral tests, governed artifacts, and visible repository-host checks were available.

### Requirement Satisfaction Crosswalk

REQ-001

Requirement: Produce deterministic Reader-to-CLI byte parity evidence.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): AB artifact, CLI/runtime captures, summary hashes, focused tests.

GitHub Repo proof, if current state matters: current AB/Reader/CLI hashes agree.

PF09 task/subtask IDs, if proven: HDE-DIST001.1

REQ-002

Requirement: Produce exact AB-to-BA byte identity evidence.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): AB/BA artifacts, `abba.bytes`, summary.

GitHub Repo proof, if current state matters: current AB and BA hashes and bytes are equal.

PF09 task/subtask IDs, if proven: HDE-DIST001.1

REQ-003

Requirement: Produce independent two-run byte identity evidence.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): two separately invoked runtime captures and `tworun_identity.sha256`.

PF09 task/subtask IDs, if proven: HDE-DIST001.1

REQ-004

Requirement: Recompute `idempotence_hash` from the canonical five-key Reader preimage.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): determinism producer and summary stored/recomputed values.

PF09 task/subtask IDs, if proven: HDE-DIST001.1

REQ-005

Requirement: Prove canonical JSON reserialization equality.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): canonical serialization predicates and tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.1

REQ-006

Requirement: Bind aggregate proof to the authoritative canonical JSON gate.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): authoritative check integration, provenance fields, failing/unavailable-gate tests.

GitHub Repo proof, if current state matters: no implicit `canon_check=True` normal path remains.

PF09 task/subtask IDs, if proven: HDE-DIST001.1

REQ-007

Requirement: Fail before writing when any decisive determinism predicate fails.

Original PR status: Unclear

After remediation: Satisfied

Evidence pointer(s): write-mode atomicity tests; marker unchanged/absent on failure.

PF09 task/subtask IDs, if proven: HDE-DIST001.1

REQ-008

Requirement: Repair the Endpoint Catalog to strict typed records and one governed success designation.

Original PR status: Partially satisfied

After remediation: Satisfied

Evidence pointer(s): current Catalog, validator, and complete schema tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-009

Requirement: Include the internal dev sampler in the full Catalog under the PO decision while excluding it from A7 and public contracts.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): Catalog record, adapter comment, route method test, A7 rejection test.

GitHub Repo proof, if current state matters: `POST /internal/dev/sampler`, internal, non-A7, not in `success_endpoints`.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-010

Requirement: Select exactly one A7 target through the Catalog and reject `/internal/version` and internal/ineligible routes.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Catalog designation and negative tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-011

Requirement: Produce the PF12 Reader success endpoint snapshot.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): current snapshot contains `generated_at_utc`, names-only endpoints, and envelope keys.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-012

Requirement: Produce and validate the PF12 composite Reader A7 proof.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): exact schema, composite artifact, schema-validation tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-013

Requirement: Prove GET success headers, body, ETag, length, cache, and Vary.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): GET proof and fail-closed tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-014

Requirement: Prove HEAD bodylessness and full GET parity.

Original PR status: Partially satisfied

After remediation: Satisfied

Evidence pointer(s): HEAD proof and malformed cache/Vary/content-type/length tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-015

Requirement: Prove conditional 304 entity-header omission and cache/validator parity.

Original PR status: Partially satisfied

After remediation: Satisfied

Evidence pointer(s): 304 proof and malformed-response tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-016

Requirement: Prove canonical writer/error posture.

Original PR status: Partially satisfied

After remediation: Satisfied

Evidence pointer(s): error proof, canonical body validation, no-store/no-ETag/non-304 tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-017

Requirement: Prove ETag and HEAD identity-length invariance across `identity`, `gzip`, and `br`.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): per-encoding proof records and mismatch tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-018

Requirement: Prove production environment gating without external I/O and restore environment exactly.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): env-gate proof and success/exception restoration tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-019

Requirement: Require explicit `HDE_WRITE_A7_PROOFS=1` for write mode.

Original PR status: Implemented but insufficiently tested

After remediation: Satisfied

Evidence pointer(s): actual write-refusal and authorized-write tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-020

Requirement: Keep `--check` and default tests non-writing.

Original PR status: Unclear

After remediation: Satisfied

Evidence pointer(s): before/after file-state tests and sole-writer search.

PF09 task/subtask IDs, if proven: HDE-DIST001.1, HDE-DIST001.2

REQ-021

Requirement: Maintain one deterministic A7 proof writer.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): test-side writer removal; exact write-owner search.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-022

Requirement: Remove the obsolete duplicate encoding proof home and all bindings.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): deleted files and zero active references.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-023

Requirement: Update Human Index, Mirror, hashes, proofs, and orientation through canonical tooling.

Original PR status: Mechanically satisfied

After remediation: Satisfied

Evidence pointer(s): corrected semantic preconditions and passing canonical checks.

PF09 task/subtask IDs, if proven: HDE-DIST001.1, HDE-DIST001.2

REQ-024

Requirement: Preserve truthful path-proof chronology.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): current proof metadata and updater regression tests.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-025

Requirement: Preserve truthful historical encoding-token evidence.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): complete retained proof and predicate-aware ledger generation.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-026

Requirement: Add complete targeted negative, write/check, schema, and transport tests.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): expanded three targeted test modules.

PF09 task/subtask IDs, if proven: HDE-DIST001.1, HDE-DIST001.2

REQ-027

Requirement: Preserve public Reader behavior and add no public route or payload field.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): runtime diff limited to sampler Catalog comment; transport regressions pass.

PF09 task/subtask IDs, if proven: HDE-DIST001.2

REQ-028

Requirement: Do not execute OPS, deploy, migrate, call vendors, or mutate external systems.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): in-process fixtures, no external action evidence, explicit nonclaims.

PF09 task/subtask IDs, if proven: HDE-DIST001.1, HDE-DIST001.2

REQ-029

Requirement: Do not edit PF-Canon in these implementation PRs.

Original PR status: Satisfied

After remediation: Satisfied

Search method: searched lifecycle changed-file paths for `docs/pfcanon/` (case: sensitive); scope: both PRs; tool: GitHub API; result: 0 hits.

PF09 task/subtask IDs, if proven: None

REQ-030

Requirement: Do not claim QA PASS, epic closeout, OPS completion, or PF09 movement from implementation alone.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): implementation artifacts retain nonclaims; no PF09 file edit.

PF09 task/subtask IDs, if proven: HDE-DIST001.1, HDE-DIST001.2

### RCA

#### A) Bug/Failure statement

Original PR merged with several proof-integrity defects:

* a caller-provided canonical-gate Boolean;  
* a non-PF12 composite schema;  
* a non-PF12 endpoint snapshot;  
* incomplete transport and encoding predicates;  
* a second governed proof writer;  
* insufficient executable negative tests;  
* historical token evidence based on incomplete proof;  
* stale path-proof chronology;  
* omission of the PO-required internal dev sampler Catalog entry.

#### B) Root cause(s)

1. **Model validation was treated as equivalent to executable validation.**  
   Some tests called `build()` or inspected bytes without invoking real write/check command paths.  
2. **A local schema was designed around the first artifact implementation rather than copied from PF12.**  
3. **The A7 producer recorded certain headers without making all of them decisive pass/fail predicates.**  
4. **Encoding invariance was initially reduced to ETag equality and omitted HEAD identity-length equality.**  
5. **Existing test-side artifact generation was not retired when the new producer became the canonical owner.**  
6. **Historical acceptance tooling inferred evidence from path availability rather than validating decisive proof content.**  
7. **Path-proof metadata reuse preserved historical chronology during current-byte refreshes.**  
8. **Conflicting PF05 sampler text was initially resolved by exclusion rather than awaiting the Product Owner decision.**

#### C) Fix across PRs

Original PR created the core determinism and A7 architecture and generated the complete initial evidence family.

Remedial PR:

* bound determinism to the real canonical gate;  
* copied the PF12 composite schema and snapshot contracts;  
* made all required A7 facts fail-closed predicates;  
* added per-encoding ETag and HEAD-length evidence;  
* removed the test-side writer;  
* expanded executable tests;  
* added semantic evidence validation;  
* corrected path-proof chronology;  
* made historical token evidence predicate-aware;  
* added the internal dev sampler to the full Catalog under the bounded PO decision;  
* regenerated all governed derivatives.

#### D) Fix verification

* Both PRs are proven merged in direct lineage.  
* Current `main` equals the remedial merged state.  
* No later lifecycle divergence was found.  
* Targeted and global visible checks completed successfully.  
* Current final source and governed artifacts implement the corrected requirements.  
* No unresolved Blocker finding remains.

### PF09 Impact & Status Posture

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST001

PF09 subtask ID(s): HDE-DIST001.1, HDE-DIST001.2

Current PF09 status: Partial

Status recommendation: No status change recommended

Why supported: The parent task includes additional Distillation harness obligations outside the PR-02 lifecycle. Completion of the two reviewed subtasks does not prove the entire parent task is complete.

Evidence pointer(s): Implementation Doc mapping; current PF09.6 parent inventory; NET-030 through NET-068.

GitHub Repo proof, if current state matters: current PR-02 evidence and tests are present, but no proof was reviewed for every other HDE-DIST001 subtask.

PF proof excerpt(s):

â€œTask status: Partialâ€

â€œProvide one-button runners that exercise all critical mechanics â€¦ and produce the full set of binary evidence artifacts in a deterministic, repeatable way.â€

Linked NET/Finding IDs: NET-030â€“068; F-001

---

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST001

PF09 subtask ID(s): HDE-DIST001.1

Current PF09 status: Partial

Status recommendation: change to Done

Why supported: Readerâ†”CLI, ABâ†”BA, independent two-run, canonical preimage, canonical reserialization, authoritative canonical-gate, aggregate fail-closed posture, marker gating, governed evidence, and executable write/check tests are all present and current.

Evidence pointer(s): NET-005â€“006, NET-030â€“039, NET-059, NET-064; VAL-005; REQ-001â€“007.

GitHub Repo proof, if current state matters: current summary and marker derive from the authoritative gate; focused and global checks pass.

PF proof excerpt(s):

â€œSubtask status: Partialâ€

â€œCanonical JSON compare: Re-emit a sample of envelopes and verify they are canonical JSON and match their canonical re-serialization.â€

Linked NET/Finding IDs: NET-005â€“006, NET-030â€“039, NET-059, NET-064; F-001

---

PF09.x document title: PF09.6 â€” HDE-Build-Checklist-Distillation

PF09 task ID: HDE-DIST001

PF09 subtask ID(s): HDE-DIST001.2

Current PF09 status: Not done

Status recommendation: change to Done

Why supported: The full Catalog-driven A7 harness now includes a unique governed Reader success route, exact PF12 schema and snapshot, complete GET/HEAD/304/error/env/encoding predicates, explicit write authorization, non-writing checks, one writer, governed evidence, truthful historical token linkage, and complete negative tests.

Evidence pointer(s): NET-001â€“004, NET-013â€“028, NET-044â€“068; VAL-006â€“017; REQ-008â€“030.

GitHub Repo proof, if current state matters: current Catalog, schema, composite, proof family, tests, Index, Mirror, and historical dependent artifacts match the remedial merged state.

PF proof excerpt(s):

â€œSubtask status: Not doneâ€

â€œEncoding invariance: for a fixed canonical LF-terminated body, ETag and effective Content-Length are stable across identity/gzip/br.â€

â€œA7 proofs must be captured on a Catalog JSON success route; `/internal/version` is excluded.â€

Linked NET/Finding IDs: NET-001â€“004, NET-013â€“028, NET-044â€“068; F-002

### Findings

F-001

Related item: PF09

Severity: Note

Observation: The two PR-02 subtasks have support for later status drainage, but the parent `HDE-DIST001` includes additional work outside this lifecycle.

Why it matters: Subtask completion must not be converted into an unsupported parent-task completion claim.

Evidence: Exact PF09.6 mapping and reviewed current evidence.

Required action: None.

Blocker: No

PF09 impact/status, if proven: Recommend `HDE-DIST001.1` and `HDE-DIST001.2` change to `Done`; no parent status change.

PF reference, if relied on: PF09.6 â€” HDE-Build-Checklist-Distillation.

F-002

Related item: Other

Severity: Note

Observation: PF05 contains conflicting permanent text about whether `/internal/dev/sampler` belongs in the Endpoint Catalog; the Product Owner decision resolves the implementation posture in favor of internal Catalog inclusion.

Why it matters: Future agents should not reintroduce the exclusion based on the stale conflicting paragraph.

Evidence: PO decision; current Catalog record; current route method and A7-ineligible posture.

Required action: None in this review. Drain the conflict through a separate PF-Canon update.

Blocker: No

PF09 impact/status, if proven: HDE-DIST001.2 implementation remains supportable.

PF reference, if relied on: PF05 â€” HDE-CLI-API-Vendor-Ref, Â§5.6 and Â§5.11.6.

F-003

Related item: GitHub Repo

Severity: Note

Observation: No later commit after the Remedial PR merge changed a lifecycle touched file.

Why it matters: Current-state evidence remains attributable to the reviewed lifecycle.

Evidence: Default-branch commit-history search returned 0 later commits.

Required action: None.

Blocker: No

PF09 impact/status, if proven: None.

PF reference, if relied on: None.

### Evidence Print (PASS PROOF; merged work)

#### A) Acceptance coverage evidence

1. **Determinism aggregate**  
   * Source: GitHub Repo  
   * Evidence pointer: determinism producer, summary, marker, focused tests  
   * Proof: actual canonical-gate provenance, Readerâ†”CLI parity, ABâ†”BA, independent two-run, preimage recompute, canonical reserialization, and fail-closed output behavior.  
   * GitHub Repo proof: NET-030â€“039, NET-059, NET-064.  
2. **Endpoint Catalog**  
   * Source: GitHub Repo  
   * Evidence pointer: current Catalog and Catalog tests  
   * Proof: typed records, one governed `GET /reader` success designation, `/internal/version` excluded from A7, and `POST /internal/dev/sampler` cataloged internally but not A7-eligible.  
   * GitHub Repo proof: NET-001â€“004, NET-046, NET-063.  
3. **PF12 composite and snapshot**  
   * Source: GitHub Repo  
   * Evidence pointer: current schema, composite artifact, endpoint snapshot, and schema-validation tests  
   * Proof: exact required field sets and unknown-key rejection.  
   * GitHub Repo proof: NET-015â€“016, NET-027â€“028, NET-057â€“058.  
4. **A7 transport**  
   * Source: GitHub Repo  
   * Evidence pointer: current six text proofs, composite proof, producer, and malformed-response tests  
   * Proof: GET, HEAD, 304, writer/error, environment gate, cache, Vary, ETag, content type, body, entity-header, and length predicates.  
   * GitHub Repo proof: NET-013â€“026, NET-048, NET-063.  
5. **Encoding invariance**  
   * Source: GitHub Repo  
   * Evidence pointer: retained encoding proof and tests  
   * Proof: equal identity ETag and equal HEAD identity length for `identity`, `gzip`, and `br`.  
   * GitHub Repo proof: NET-019â€“020, NET-048, NET-067.  
6. **Single-writer and non-writing posture**  
   * Source: GitHub Repo  
   * Evidence pointer: sole producer, write guard, removed test writer, and actual check-mode tests  
   * Proof: one owner, explicit `HDE_WRITE_A7_PROOFS=1`, non-writing default tests, non-writing `--check`, and no partial output on failure.  
   * GitHub Repo proof: NET-047â€“049, NET-061â€“063.

#### B) Original gaps closed

* Synthetic canonical-gate Boolean: closed.  
* Non-PF12 composite schema: closed.  
* Non-PF12 endpoint snapshot: closed.  
* Incomplete HEAD predicates: closed.  
* Incomplete 304 predicates: closed.  
* Incomplete writer/error predicates: closed.  
* Missing encoding-length invariant: closed.  
* Competing test-side proof writer: closed.  
* Insufficient write/check and malformed-response tests: closed.  
* Path-proof chronology mismatch: closed.  
* Path-exists-only historical encoding-token claim: closed.  
* Missing internal dev sampler Catalog record: closed.  
* Evidence updater semantic-validation gap: closed.

#### C) Evidence and verification posture

* Human Index and Machine Mirror have one-to-one final bindings.  
* Index sentinel and Mirror checksum match current bytes.  
* Every governed PR-02 primary has a sibling proof anchor.  
* Obsolete duplicate encoding proof remains absent.  
* Catalog checksum and audit mirror are current.  
* Composite artifact validates against the governed schema.  
* Path-proof metadata is current and truthful.  
* Orientation evidence reflects the corrected topology.  
* No later lifecycle divergence exists.  
* No local execution is claimed; visible repository-host checks and current-file inspection supply the review proof.

#### D) Token/gate evidence

No new PR-02 acceptance token is claimed by this review.

The historical `A7_ENCODING_INVARIANCE_OK` row was examined because Merged Change modified its evidence binding. Current support is based on decisive ETag and HEAD identity-length predicates across all required encodings rather than artifact-path existence alone.

This review does not create QA PASS, OPS completion, PF09 status movement, deployment authorization, epic closure, or close-pack approval.

#### E) Test/CI proof

* Original PR visible checks: successful.  
* Remedial PR visible checks: successful.  
* Determinism targeted tests: successful.  
* A7 producer targeted tests: successful.  
* Endpoint Catalog tests: successful.  
* Reader A7 transport tests: successful.  
* Canonical JSON gate check: successful.  
* Catalog checksum verification: successful.  
* Human Index check: successful.  
* Machine Mirror schema check: successful.  
* Evidence Index hash check: successful.  
* Evidence path validation: successful.  
* Orientation check: successful.  
* Final-LF check: successful.  
* Existing Reader/CLI and identity-closure regressions: successful.

#### F) Artifact and evidence outputs

Final governed outputs include:

* `audit/gates/parity/reader_cli/ab.json`  
* `audit/gates/parity/reader_cli/ba.json`  
* `audit/gates/parity/reader_cli/summary.json`  
* `audit/gates/determinism/abba.bytes`  
* `audit/gates/determinism/tworun_identity.sha256`  
* `artifacts/cards/a3/IDENTITY_OK.txt`  
* `docs/ENDPOINTS_CATALOG.json`  
* `docs/ENDPOINTS_CATALOG.json.sha256`  
* `artifacts/audit/ENDPOINTS_CATALOG.json`  
* `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`  
* `artifacts/reader/endpoints_snapshot.json`  
* `schemas/proofs.reader_success.v1.json`  
* `artifacts/proofs/endpoints_env_gate_proof.log`  
* `artifacts/proofs/success_get.txt`  
* `artifacts/proofs/success_head.txt`  
* `artifacts/proofs/success_304.txt`  
* `artifacts/proofs/success_writers_errors.txt`  
* `artifacts/proofs/success_encoding_invariance.txt`  
* `artifacts/proofs/reader_success_get_head_304.json`  
* current Human Index, sentinel, Machine Mirror, Mirror checksum, path proofs, and orientation derivatives.

The obsolete second home remains deleted:

* `artifacts/proofs/encoding_invariance.txt`  
* `artifacts/proofs/encoding_invariance.txt.path_proof.txt`

### Doc Delta Candidates (PF-Canon only)

DDC-001

Doc: PF05 â€” HDE-CLI-API-Vendor-Ref

Section: Â§5.11.6 Exclusions from A7 & catalogs

Canon basis: CANON AMBIGUITY-CONFLICT

Impacted PF09 task/subtask IDs: HDE-DIST001.2

PF09 status action: change to Done

Delta: Replace the unqualified sampler Catalog exclusion with: `POST /internal/dev/sampler` is included in the internal Endpoint Catalog as `dev_harness`, `internal:true`, `a7_eligible:false`, and remains excluded from `success_endpoints`, A7 proof selection, and public contracts. `GET /internal/dev/sampler` remains unsupported.

Why: PF05 Â§5.6 already describes a normative internal Catalog record, while Â§5.11.6 says the route is not cataloged. The Product Owner decision and current Repo resolve the implementation posture in favor of bounded internal inclusion.

Evidence pointer: GitHub Repo | current Endpoint Catalog and route | `"POST /internal/dev/sampler"` | `"a7_eligible:false"`

GitHub Repo proof, if current state matters: current Catalog and Catalog tests.

Canon proof excerpt:

â€œ`/internal/dev/sampler` is excluded from all public success surfaces and is not A7-eligible.â€

â€œThe route is dev-only and must not be cataloged as a public JSON-success endpoint.â€

DDC-002

Doc: PF09.6 â€” HDE-Build-Checklist-Distillation

Section: Â§Subtask HDE-DIST001.1 â€” Determinism gates

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task/subtask IDs: HDE-DIST001.1

PF09 status action: change to Done

Delta: Drain completion of Readerâ†”CLI parity, ABâ†”BA, independent two-run, canonical preimage, canonical reserialization, authoritative canonical-gate binding, fail-closed output behavior, and governed evidence integration.

Why: The combined Original and Remedial PR lifecycle provides current implementation, tests, artifacts, and canonical evidence bindings for the complete subtask.

Evidence pointer: NET-005â€“006, NET-030â€“039, NET-059, NET-064; VAL-005.

GitHub Repo proof, if current state matters: current determinism producer, summary, marker, tests, and visible checks.

Canon proof excerpt:

â€œSubtask status: Partialâ€

DDC-003

Doc: PF09.6 â€” HDE-Build-Checklist-Distillation

Section: Â§Subtask HDE-DIST001.2 â€” Catalog-driven A7 transport proofs

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task/subtask IDs: HDE-DIST001.2

PF09 status action: change to Done

Delta: Drain completion of the strict Catalog, bounded sampler entry, unique Reader target, PF12 snapshot and composite schema, complete GET/HEAD/304/error/env/encoding proof family, explicit write guard, one-writer posture, non-writing checks, governed evidence, and executable negative tests.

Why: The combined lifecycle closes all reviewed A7 implementation and evidence gaps.

Evidence pointer: NET-001â€“004, NET-013â€“028, NET-044â€“068; VAL-006â€“017.

GitHub Repo proof, if current state matters: current Catalog, producers, schemas, artifacts, tests, ledgers, and visible checks.

Canon proof excerpt:

â€œSubtask status: Not doneâ€

DDC-004

Doc: PF19 â€” Glow QA Guide

Section: Â§2.2.11 Evidence-governed CI sequence (names-only)

Canon basis: CANON SILENCE

Impacted PF09 task/subtask IDs: HDE-DIST001.1, HDE-DIST001.2

PF09 status action: None

Delta: Add a general proof-producer verification rule requiring: one deterministic writer per governed artifact family; real execution of write and check entry points; no partial writes after failed predicates; explicit write authorization where applicable; and direct malformed-response tests for every decisive transport predicate.

Why: Original PRâ€™s principal defects were caused by model-only tests, a second writer, and recorded-but-nondecisive response facts.

Evidence pointer: Original PR gaps and Remedial PR corrections.

GitHub Repo proof, if current state matters: current determinism and A7 tests implement these safeguards.

Negative-search proof: Search method: searched PF19 Â§2.2.11 for a combined one-writer, real-entrypoint, no-partial-write, and decisive-predicate rule (case: insensitive); scope: PF19 Â§2.2.11; tool: manual scan; result: 0 complete matching rule.

DECISION: MERGED WORK ACCEPTABLE

## 2.3) PR-03 HDE-EPIC038

Review Summary

- Original PR created the reusable PR-03 rails gate family: three generalized job definitions, the strict runner, the `rails-policy-gates` workflow job, primary rails evidence generation, focused tests, and canonical evidence bindings.  
- Original PRâ€™s merged state retained three material gaps: command-embedded credential values were not rejected; the open-rails gate lacked the phased PF09-required ABâ†”BA/canonical-JSON/single-LF proof; and the feature producer directly wrote governed path proofs while using a fixed repository-root temporary file during check mode.  
- First Remedial PR closed those Original PR gaps by enforcing exact per-identity argv allowlists and credential rejection, using residue-free external temporary storage, returning path-proof/index/mirror ownership to the canonical updater, and adding fixture-backed plus bounded PO-authorized live ABâ†”BA proof surfaces.  
- First Remedial PR then left three narrower review defects: the live proof trusted a stored `abba_byte_identity` Boolean rather than independently deriving first-run AB/BA identity; its live artifact validator did not enforce a closed schema or derive all security/safety claims; and live check-mode certification was not yet strong enough against crafted self-attestation.  
- Second Remedial PR closed those defects with a closed live-proof schema, recursive prohibited-key and prohibited-string scanning, independent derivation of distinctness, payload binding, same-input reuse, first-run ABâ†”BA, and two-run identity, pass-only writes, read-only live check mode, and negative tests for crafted inconsistent proofs.  
- Current GitHub Repo `main` is exactly the Second Remedial PR merge state. No later commit changes the lifecycle touched-file set, evidence, or reviewed behavior.  
- All three PR head workflows completed successfully. Current final source, fixture proof, bounded live proof, Human Index, Machine Mirror, checksums, path proofs, and orientation evidence are coherent and directly inspected; CI was not used as a substitute for final-file review.  
- PF09 impact is exactly mapped to PF09.6 `HDE-DIST001` / `HDE-DIST001.3`. The parent remains broader and should remain Partial; the reviewed subtask now supports a separate later status drain to Done.  
- No material code, evidence, safety, validation, source-conflict, or current-state risk remains. The only remaining work is separate documentation/status drainage, which is not an implementation blocker.

GitHub / Repo Inspection

Repository identity: `amthorn78/glow-hdengine-v2`; default and reviewed target branch: `main`.

Current reviewed branch HEAD: `2971256474f70ad62848ce58a2bfaf1ea4438f37`.

Evidence pointer: GitHub Repo | repository metadata/default-branch head | "amthorn78/glow-hdengine-v2" | "main@2971256474f70ad62848ce58a2bfaf1ea4438f37"

Original PR identity and merge state:

- Base: `main` at `aba4a108e0661ababf61a2eebddcbff2b2e12042`.  
- Head: `5dd200369201c0801a54a3e2d91357d9f36e53e4`.  
- Merge identifier: `472ba838110ec69218d4079e98504d0b317cfb7e`.  
- State: merged.  
- Changed files: 103; additions: 865; deletions: 213\.  
- Evidence pointer: Original PR | API fields `base.sha`, `head.sha`, `merge_commit_sha`, `merged`, `changed_files` | "aba4a108e0661ababf61a2eebddcbff2b2e12042 \-\> 5dd200369201c0801a54a3e2d91357d9f36e53e4" | "merge=472ba838110ec69218d4079e98504d0b317cfb7e; merged=true; files=103"

First Remedial PR identity and merge state:

- Base: `main` at `472ba838110ec69218d4079e98504d0b317cfb7e`, exactly the Original PR merge state.  
- Head: `bf9b63cf0fd7ffeb452ab0a7dff342e472a0acbc`.  
- Merge identifier: `76a331a923cce8ba4d0601da3fab1dcb63e98270`.  
- State: merged.  
- Changed files: 33; additions: 1,387; deletions: 114\.  
- Evidence pointer: First Remedial PR | API fields `base.sha`, `head.sha`, `merge_commit_sha`, `merged`, `changed_files` | "472ba838110ec69218d4079e98504d0b317cfb7e \-\> bf9b63cf0fd7ffeb452ab0a7dff342e472a0acbc" | "merge=76a331a923cce8ba4d0601da3fab1dcb63e98270; merged=true; files=33"

Second Remedial PR identity and merge state:

- Base: `main` at `76a331a923cce8ba4d0601da3fab1dcb63e98270`, exactly the First Remedial PR merge state.  
- Head: `d724154bad97411124cc41ffbe334103fa4ea2ce`.  
- Merge identifier: `2971256474f70ad62848ce58a2bfaf1ea4438f37`.  
- State: merged.  
- Changed files: 2; additions: 279; deletions: 1\.  
- Evidence pointer: Second Remedial PR | API fields `base.sha`, `head.sha`, `merge_commit_sha`, `merged`, `changed_files` | "76a331a923cce8ba4d0601da3fab1dcb63e98270 \-\> d724154bad97411124cc41ffbe334103fa4ea2ce" | "merge=2971256474f70ad62848ce58a2bfaf1ea4438f37; merged=true; files=2"

Lifecycle order and lineage:

1. Lifecycle baseline: `aba4a108e0661ababf61a2eebddcbff2b2e12042`.  
2. Original merged state: `472ba838110ec69218d4079e98504d0b317cfb7e`.  
3. First remedial merged state: `76a331a923cce8ba4d0601da3fab1dcb63e98270`.  
4. Second remedial merged state and current state: `2971256474f70ad62848ce58a2bfaf1ea4438f37`.

Evidence pointer: GitHub Repo | baseline-to-current compare | "ahead by 3 lifecycle commits" | "direct base-to-merge chain across all three PRs"

Lifecycle touched-file set: 109 unique files. Every union path is represented exactly once in Net Effective Diff Review. The complete changed-file lists and complete per-file patches were retrieved for all three PRs.

Current final state inspected: all 109 lifecycle paths through the baseline-to-current compare, with direct current-file inspection for the workflow, runner, three job definitions, both evidence producers, both focused test modules, both ABâ†”BA primary artifacts, the Human Index, Machine Mirror, hashes, and proof anchors.

Checks and CI inspected:

- Original PR head workflow: successful, including `rails-policy-gates`, test, sanity, canonical evidence, mirror, hash, path, LF, and identity checks.  
- First Remedial PR head workflow run `29352144561`: successful across all reported jobs.  
- Second Remedial PR head workflow run `29362316387`: successful across all reported jobs, including `rails-policy-gates`, test, sanity-pipeline, evidence/index/mirror checks, final-LF, canonical JSON, path validation, and identity/evidence closure.

Evidence pointer: GitHub Repo | workflow runs for the three PR head SHAs | "completed" | "success"

Governed evidence inspected:

- `artifacts/proofs/ops_refusal_proof.txt`  
- `artifacts/vendor/retry_after_parse.log`  
- `artifacts/vendor/rails_gate_keys_only.logs.sample`  
- `audit/gates/determinism/open_rails_abba.json`  
- `audit/gates/determinism/open_rails_vendor_abba.json`  
- all corresponding sibling path proofs  
- `docs/evidence/INDEX.json`  
- `docs/evidence/INDEX.sha256`  
- `artifacts/evidence_index.jsonl`  
- `artifacts/evidence_index.jsonl.sha256`  
- orientation evidence and affected release/canonical evidence.

Later commits affecting touched files: none.

Search method: searched for "commits after 2971256474f70ad62848ce58a2bfaf1ea4438f37" (case: sensitive); scope: default `main` commit history; tool: GitHub API; result: 0 hits.

No local command is claimed by this reviewer. Read-only GitHub inspection supplied PR metadata, changed files, patches, current files, compare state, checks, and current governed evidence.

Provenance (Original \-\> First Remediation \-\> Second Remediation)

- Claim: Original PR introduced the reusable rails-policy gate architecture. Source: Original PR. Evidence pointer: Original PR | PR body and source diff | "rails-policy-gates" | "strict runner \+ reusable evidence producer"  
- Claim: Original PR preserved closed-default CI and fixture-backed open policy. Source: Original PR. Evidence pointer: Original PR | workflow/job-definition diff | "SAFE\_MODE=1; ALLOW\_NETWORK=0" | "live\_vendor\_calls: forbidden"  
- Claim: Original PR did not reject command-embedded credentials. Source: Original PR. Evidence pointer: Original PR | `ci/checks/run_rails_job_definitions.py` merged state | "ambient scrubbing present" | "no parsed-argv credential-assignment rejection"  
- Claim: Original PR did not prove open-rails ABâ†”BA canonical-byte behavior. Source: Original PR. Evidence pointer: Original PR | `ci/jobs/rails_open_conformance.yml` | "test\_vendor\_client.py only" | "no ABâ†”BA/canonical/single-LF command"  
- Claim: Original PRâ€™s feature producer violated final evidence ownership and residue-free check posture. Source: Original PR. Evidence pointer: Original PR | `tools/evidence/generate_rails_gate_evidence.py` | "private path-proof helper call" | "fixed .rails\_gate\_keys\_only.tmp"  
- Claim: First Remedial PR closed those three gaps. Source: First Remedial PR. Evidence pointer: First Remedial PR | runner/producer/job/test diffs | "exact argv allowlist \+ credential rejection" | "TemporaryDirectory \+ fixture/live ABâ†”BA proof family"  
- Claim: First Remedial PR performed one bounded PO-authorized live evidence capture while ordinary CI remained fixture-backed and non-live. Source: First Remedial PR. Evidence pointer: First Remedial PR | live proof artifact and workflow definition | "requests\_attempted=2" | "live\_vendor\_calls: forbidden in CI"  
- Claim: First Remedial PRâ€™s live validator still trusted a stored ABâ†”BA Boolean and self-attested some safety fields. Source: First Remedial PR. Evidence pointer: First Remedial PR | live validation implementation | "stored abba\_byte\_identity consumed" | "no complete closed-schema/recursive safety validation"  
- Claim: Second Remedial PR independently derives live proof predicates and rejects crafted inconsistency. Source: Second Remedial PR. Evidence pointer: Second Remedial PR | generator/tests diff | "first-run AB hash compared to first-run BA hash" | "both BA hashes changed consistently still rejected"  
- Claim: Second Remedial PR closes the live proof schema and privacy surface. Source: Second Remedial PR. Evidence pointer: Second Remedial PR | generator/tests diff | "exact top-level and nested key sets" | "recursive prohibited key/string scan, including allowed-key values"  
- Claim: Current fixture proof is fully passing and transport-free. Source: GitHub Repo. Evidence pointer: GitHub Repo | `audit/gates/determinism/open_rails_abba.json` | "top\_level\_pass=true; transport\_call\_count=0" | "ABâ†”BA, Readerâ†”CLI, two-run, open=closed, canonical JSON, single LF all true"  
- Claim: Current live proof is bounded, distinct, same-input, secret-safe, and fully passing. Source: GitHub Repo. Evidence pointer: GitHub Repo | `audit/gates/determinism/open_rails_vendor_abba.json` | "requests\_attempted=2; requests\_completed=2; result=pass" | "distinct fingerprints; same normalized inputs reused; no raw payload; no secret values"  
- Claim: Current evidence ledgers bind both ABâ†”BA artifacts coherently. Source: GitHub Repo. Evidence pointer: GitHub Repo | Human Index / Machine Mirror / path proofs | "epic038.pr03.open\_rails\_abba" | "epic038.pr03.open\_rails\_vendor\_abba"  
- Claim: No acceptance token, QA PASS, PF09 movement, or epic closeout is claimed by the merged implementation. Source: Implementation Doc / GitHub Repo. Evidence pointer: GitHub Repo | both ABâ†”BA artifacts | "acceptance\_token\_satisfied=false" | "pf09\_mapping.status=Partial"

Original PR Material Hunk Ledger

Hunk ID: OPR-001 | File: `.github/workflows/ci.yml` | Patch and hunk header: `diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml` || `@@ -160,47 +160,69 @@ jobs:` | Material effect: Added the dedicated closed-default `rails-policy-gates` workflow job and its single strict-runner invocation. | Risk category: environment, config, vendor, or OPS-sensitive behavior. | Evidence pointer: Original PR | `.github/workflows/ci.yml` diff | "diff \--git a/.github/workflows/ci.yml b/.github/workflows/ci.yml" | "@@ \-160,47 \+160,69 @@ jobs:" Hunk ID: OPR-002 | File: `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt b/artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` diff | "diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.path\_proof.txt b/artifacts/audit/ENDPOINTS\_CATALOG.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-003 | File: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt b/artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` diff | "diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-004 | File: `artifacts/bodygraph/keys_only.logs.sample.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/bodygraph/keys_only.logs.sample.path_proof.txt b/artifacts/bodygraph/keys_only.logs.sample.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/bodygraph/keys_only.logs.sample.path_proof.txt` diff | "diff \--git a/artifacts/bodygraph/keys\_only.logs.sample.path\_proof.txt b/artifacts/bodygraph/keys\_only.logs.sample.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-005 | File: `artifacts/bodygraph/release_bindings.json` | Patch and hunk header: `diff --git a/artifacts/bodygraph/release_bindings.json b/artifacts/bodygraph/release_bindings.json` || `@@ -1 +1 @@` | Material effect: Updated the file as part of the Original PR reusable rails and governed-evidence closure. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/bodygraph/release_bindings.json` diff | "diff \--git a/artifacts/bodygraph/release\_bindings.json b/artifacts/bodygraph/release\_bindings.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-006 | File: `artifacts/bodygraph/release_bindings.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/bodygraph/release_bindings.json.path_proof.txt b/artifacts/bodygraph/release_bindings.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/bodygraph/release_bindings.json.path_proof.txt` diff | "diff \--git a/artifacts/bodygraph/release\_bindings.json.path\_proof.txt b/artifacts/bodygraph/release\_bindings.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-007 | File: `artifacts/cli/ab.json` | Patch and hunk header: `diff --git a/artifacts/cli/ab.json b/artifacts/cli/ab.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/cli/ab.json` diff | "diff \--git a/artifacts/cli/ab.json b/artifacts/cli/ab.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-008 | File: `artifacts/cli/ab.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/cli/ab.json.path_proof.txt b/artifacts/cli/ab.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/cli/ab.json.path_proof.txt` diff | "diff \--git a/artifacts/cli/ab.json.path\_proof.txt b/artifacts/cli/ab.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-009 | File: `artifacts/cli/ba.json` | Patch and hunk header: `diff --git a/artifacts/cli/ba.json b/artifacts/cli/ba.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/cli/ba.json` diff | "diff \--git a/artifacts/cli/ba.json b/artifacts/cli/ba.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-010 | File: `artifacts/cli/ba.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/cli/ba.json.path_proof.txt b/artifacts/cli/ba.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/cli/ba.json.path_proof.txt` diff | "diff \--git a/artifacts/cli/ba.json.path\_proof.txt b/artifacts/cli/ba.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-011 | File: `artifacts/cli/install/installability_summary.json` | Patch and hunk header: `diff --git a/artifacts/cli/install/installability_summary.json b/artifacts/cli/install/installability_summary.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/cli/install/installability_summary.json` diff | "diff \--git a/artifacts/cli/install/installability\_summary.json b/artifacts/cli/install/installability\_summary.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-012 | File: `artifacts/cli/install/installability_summary.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/cli/install/installability_summary.json.path_proof.txt b/artifacts/cli/install/installability_summary.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/cli/install/installability_summary.json.path_proof.txt` diff | "diff \--git a/artifacts/cli/install/installability\_summary.json.path\_proof.txt b/artifacts/cli/install/installability\_summary.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-013 | File: `artifacts/cli/showcompat/args.json` | Patch and hunk header: `diff --git a/artifacts/cli/showcompat/args.json b/artifacts/cli/showcompat/args.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/cli/showcompat/args.json` diff | "diff \--git a/artifacts/cli/showcompat/args.json b/artifacts/cli/showcompat/args.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-014 | File: `artifacts/cli/showcompat/args.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/cli/showcompat/args.json.path_proof.txt b/artifacts/cli/showcompat/args.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/cli/showcompat/args.json.path_proof.txt` diff | "diff \--git a/artifacts/cli/showcompat/args.json.path\_proof.txt b/artifacts/cli/showcompat/args.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-015 | File: `artifacts/cli/showcompat/stdout.json` | Patch and hunk header: `diff --git a/artifacts/cli/showcompat/stdout.json b/artifacts/cli/showcompat/stdout.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/cli/showcompat/stdout.json` diff | "diff \--git a/artifacts/cli/showcompat/stdout.json b/artifacts/cli/showcompat/stdout.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-016 | File: `artifacts/cli/showcompat/stdout.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/cli/showcompat/stdout.json.path_proof.txt b/artifacts/cli/showcompat/stdout.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/cli/showcompat/stdout.json.path_proof.txt` diff | "diff \--git a/artifacts/cli/showcompat/stdout.json.path\_proof.txt b/artifacts/cli/showcompat/stdout.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-017 | File: `artifacts/cli/showcompat/stdout.json.sha256` | Patch and hunk header: `diff --git a/artifacts/cli/showcompat/stdout.json.sha256 b/artifacts/cli/showcompat/stdout.json.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the checksum or hash sentinel for the corresponding final governed bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/cli/showcompat/stdout.json.sha256` diff | "diff \--git a/artifacts/cli/showcompat/stdout.json.sha256 b/artifacts/cli/showcompat/stdout.json.sha256" | "@@ \-1 \+1 @@" Hunk ID: OPR-018 | File: `artifacts/cli/showcompat/stdout.json.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/cli/showcompat/stdout.json.sha256.path_proof.txt b/artifacts/cli/showcompat/stdout.json.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/cli/showcompat/stdout.json.sha256.path_proof.txt` diff | "diff \--git a/artifacts/cli/showcompat/stdout.json.sha256.path\_proof.txt b/artifacts/cli/showcompat/stdout.json.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-019 | File: `artifacts/cli/summary.json` | Patch and hunk header: `diff --git a/artifacts/cli/summary.json b/artifacts/cli/summary.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/cli/summary.json` diff | "diff \--git a/artifacts/cli/summary.json b/artifacts/cli/summary.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-020 | File: `artifacts/cli/summary.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/cli/summary.json.path_proof.txt b/artifacts/cli/summary.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/cli/summary.json.path_proof.txt` diff | "diff \--git a/artifacts/cli/summary.json.path\_proof.txt b/artifacts/cli/summary.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-021 | File: `artifacts/core/abba/ab_ba_parity.json` | Patch and hunk header: `diff --git a/artifacts/core/abba/ab_ba_parity.json b/artifacts/core/abba/ab_ba_parity.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/core/abba/ab_ba_parity.json` diff | "diff \--git a/artifacts/core/abba/ab\_ba\_parity.json b/artifacts/core/abba/ab\_ba\_parity.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-022 | File: `artifacts/core/abba/ab_ba_parity.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/core/abba/ab_ba_parity.json.path_proof.txt b/artifacts/core/abba/ab_ba_parity.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/core/abba/ab_ba_parity.json.path_proof.txt` diff | "diff \--git a/artifacts/core/abba/ab\_ba\_parity.json.path\_proof.txt b/artifacts/core/abba/ab\_ba\_parity.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-023 | File: `artifacts/core/json_compare/core_result_json_compare.json` | Patch and hunk header: `diff --git a/artifacts/core/json_compare/core_result_json_compare.json b/artifacts/core/json_compare/core_result_json_compare.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/core/json_compare/core_result_json_compare.json` diff | "diff \--git a/artifacts/core/json\_compare/core\_result\_json\_compare.json b/artifacts/core/json\_compare/core\_result\_json\_compare.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-024 | File: `artifacts/core/json_compare/core_result_json_compare.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/core/json_compare/core_result_json_compare.json.path_proof.txt b/artifacts/core/json_compare/core_result_json_compare.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/core/json_compare/core_result_json_compare.json.path_proof.txt` diff | "diff \--git a/artifacts/core/json\_compare/core\_result\_json\_compare.json.path\_proof.txt b/artifacts/core/json\_compare/core\_result\_json\_compare.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-025 | File: `artifacts/core/purity/purity_report.json` | Patch and hunk header: `diff --git a/artifacts/core/purity/purity_report.json b/artifacts/core/purity/purity_report.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/core/purity/purity_report.json` diff | "diff \--git a/artifacts/core/purity/purity\_report.json b/artifacts/core/purity/purity\_report.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-026 | File: `artifacts/core/purity/purity_report.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/core/purity/purity_report.json.path_proof.txt b/artifacts/core/purity/purity_report.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/core/purity/purity_report.json.path_proof.txt` diff | "diff \--git a/artifacts/core/purity/purity\_report.json.path\_proof.txt b/artifacts/core/purity/purity\_report.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-027 | File: `artifacts/core/two_run/identity.json` | Patch and hunk header: `diff --git a/artifacts/core/two_run/identity.json b/artifacts/core/two_run/identity.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/core/two_run/identity.json` diff | "diff \--git a/artifacts/core/two\_run/identity.json b/artifacts/core/two\_run/identity.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-028 | File: `artifacts/core/two_run/identity.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/core/two_run/identity.json.path_proof.txt b/artifacts/core/two_run/identity.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/core/two_run/identity.json.path_proof.txt` diff | "diff \--git a/artifacts/core/two\_run/identity.json.path\_proof.txt b/artifacts/core/two\_run/identity.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-029 | File: `artifacts/evidence_index.jsonl` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl` || `@@ -15,214 +15,214 @@` | Material effect: Regenerated the Machine Mirror and added the dedicated PR-03 rails evidence record. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/evidence_index.jsonl` diff | "diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl" | "@@ \-15,214 \+15,214 @@" Hunk ID: OPR-030 | File: `artifacts/evidence_index.jsonl` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl` || `@@ -340,145 +340,146 @@` | Material effect: Regenerated the Machine Mirror and added the dedicated PR-03 rails evidence record. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/evidence_index.jsonl` diff | "diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl" | "@@ \-340,145 \+340,146 @@" Hunk ID: OPR-031 | File: `artifacts/evidence_index.jsonl.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt` || `@@ -1,6 +1,6 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/evidence_index.jsonl.path_proof.txt` diff | "diff \--git a/artifacts/evidence\_index.jsonl.path\_proof.txt b/artifacts/evidence\_index.jsonl.path\_proof.txt" | "@@ \-1,6 \+1,6 @@" Hunk ID: OPR-032 | File: `artifacts/evidence_index.jsonl.sha256` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the checksum or hash sentinel for the corresponding final governed bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/evidence_index.jsonl.sha256` diff | "diff \--git a/artifacts/evidence\_index.jsonl.sha256 b/artifacts/evidence\_index.jsonl.sha256" | "@@ \-1 \+1 @@" Hunk ID: OPR-033 | File: `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/evidence_index.jsonl.sha256.path_proof.txt` diff | "diff \--git a/artifacts/evidence\_index.jsonl.sha256.path\_proof.txt b/artifacts/evidence\_index.jsonl.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-034 | File: `artifacts/identity/release_id.json` | Patch and hunk header: `diff --git a/artifacts/identity/release_id.json b/artifacts/identity/release_id.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/identity/release_id.json` diff | "diff \--git a/artifacts/identity/release\_id.json b/artifacts/identity/release\_id.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-035 | File: `artifacts/identity/release_id.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/identity/release_id.json.path_proof.txt b/artifacts/identity/release_id.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/identity/release_id.json.path_proof.txt` diff | "diff \--git a/artifacts/identity/release\_id.json.path\_proof.txt b/artifacts/identity/release\_id.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-036 | File: `artifacts/identity/release_id_recompute.log` | Patch and hunk header: `diff --git a/artifacts/identity/release_id_recompute.log b/artifacts/identity/release_id_recompute.log` || `@@ -1,4 +1,4 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/identity/release_id_recompute.log` diff | "diff \--git a/artifacts/identity/release\_id\_recompute.log b/artifacts/identity/release\_id\_recompute.log" | "@@ \-1,4 \+1,4 @@" Hunk ID: OPR-037 | File: `artifacts/identity/release_id_recompute.log.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/identity/release_id_recompute.log.path_proof.txt b/artifacts/identity/release_id_recompute.log.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/identity/release_id_recompute.log.path_proof.txt` diff | "diff \--git a/artifacts/identity/release\_id\_recompute.log.path\_proof.txt b/artifacts/identity/release\_id\_recompute.log.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-038 | File: `artifacts/identity/service_identity.json` | Patch and hunk header: `diff --git a/artifacts/identity/service_identity.json b/artifacts/identity/service_identity.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/identity/service_identity.json` diff | "diff \--git a/artifacts/identity/service\_identity.json b/artifacts/identity/service\_identity.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-039 | File: `artifacts/identity/service_identity.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/identity/service_identity.json.path_proof.txt b/artifacts/identity/service_identity.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/identity/service_identity.json.path_proof.txt` diff | "diff \--git a/artifacts/identity/service\_identity.json.path\_proof.txt b/artifacts/identity/service\_identity.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-040 | File: `artifacts/math/freeze_pack_manifest.json` | Patch and hunk header: `diff --git a/artifacts/math/freeze_pack_manifest.json b/artifacts/math/freeze_pack_manifest.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/math/freeze_pack_manifest.json` diff | "diff \--git a/artifacts/math/freeze\_pack\_manifest.json b/artifacts/math/freeze\_pack\_manifest.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-041 | File: `artifacts/math/freeze_pack_manifest.json.sha256` | Patch and hunk header: `diff --git a/artifacts/math/freeze_pack_manifest.json.sha256 b/artifacts/math/freeze_pack_manifest.json.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the checksum or hash sentinel for the corresponding final governed bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/math/freeze_pack_manifest.json.sha256` diff | "diff \--git a/artifacts/math/freeze\_pack\_manifest.json.sha256 b/artifacts/math/freeze\_pack\_manifest.json.sha256" | "@@ \-1 \+1 @@" Hunk ID: OPR-042 | File: `artifacts/math/manifest_snapshot.json` | Patch and hunk header: `diff --git a/artifacts/math/manifest_snapshot.json b/artifacts/math/manifest_snapshot.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/math/manifest_snapshot.json` diff | "diff \--git a/artifacts/math/manifest\_snapshot.json b/artifacts/math/manifest\_snapshot.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-043 | File: `artifacts/math/release_id.txt` | Patch and hunk header: `diff --git a/artifacts/math/release_id.txt b/artifacts/math/release_id.txt` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/math/release_id.txt` diff | "diff \--git a/artifacts/math/release\_id.txt b/artifacts/math/release\_id.txt" | "@@ \-1 \+1 @@" Hunk ID: OPR-044 | File: `artifacts/math/release_id.txt.sha256` | Patch and hunk header: `diff --git a/artifacts/math/release_id.txt.sha256 b/artifacts/math/release_id.txt.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the checksum or hash sentinel for the corresponding final governed bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/math/release_id.txt.sha256` diff | "diff \--git a/artifacts/math/release\_id.txt.sha256 b/artifacts/math/release\_id.txt.sha256" | "@@ \-1 \+1 @@" Hunk ID: OPR-045 | File: `artifacts/math/release_id_recompute.log` | Patch and hunk header: `diff --git a/artifacts/math/release_id_recompute.log b/artifacts/math/release_id_recompute.log` || `@@ -1,8 +1,8 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/math/release_id_recompute.log` diff | "diff \--git a/artifacts/math/release\_id\_recompute.log b/artifacts/math/release\_id\_recompute.log" | "@@ \-1,8 \+1,8 @@" Hunk ID: OPR-046 | File: `artifacts/math/release_id_recompute.log.sha256` | Patch and hunk header: `diff --git a/artifacts/math/release_id_recompute.log.sha256 b/artifacts/math/release_id_recompute.log.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the checksum or hash sentinel for the corresponding final governed bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/math/release_id_recompute.log.sha256` diff | "diff \--git a/artifacts/math/release\_id\_recompute.log.sha256 b/artifacts/math/release\_id\_recompute.log.sha256" | "@@ \-1 \+1 @@" Hunk ID: OPR-047 | File: `artifacts/ops/internal_version/body_get.json` | Patch and hunk header: `diff --git a/artifacts/ops/internal_version/body_get.json b/artifacts/ops/internal_version/body_get.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/ops/internal_version/body_get.json` diff | "diff \--git a/artifacts/ops/internal\_version/body\_get.json b/artifacts/ops/internal\_version/body\_get.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-048 | File: `artifacts/ops/internal_version/body_get.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/ops/internal_version/body_get.json.path_proof.txt b/artifacts/ops/internal_version/body_get.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/ops/internal_version/body_get.json.path_proof.txt` diff | "diff \--git a/artifacts/ops/internal\_version/body\_get.json.path\_proof.txt b/artifacts/ops/internal\_version/body\_get.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-049 | File: `artifacts/ops/internal_version/body_get.sha256` | Patch and hunk header: `diff --git a/artifacts/ops/internal_version/body_get.sha256 b/artifacts/ops/internal_version/body_get.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the checksum or hash sentinel for the corresponding final governed bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/ops/internal_version/body_get.sha256` diff | "diff \--git a/artifacts/ops/internal\_version/body\_get.sha256 b/artifacts/ops/internal\_version/body\_get.sha256" | "@@ \-1 \+1 @@" Hunk ID: OPR-050 | File: `artifacts/ops/internal_version/body_get.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/ops/internal_version/body_get.sha256.path_proof.txt b/artifacts/ops/internal_version/body_get.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/ops/internal_version/body_get.sha256.path_proof.txt` diff | "diff \--git a/artifacts/ops/internal\_version/body\_get.sha256.path\_proof.txt b/artifacts/ops/internal\_version/body\_get.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-051 | File: `artifacts/ops/internal_version/two_run_identity.log` | Patch and hunk header: `diff --git a/artifacts/ops/internal_version/two_run_identity.log b/artifacts/ops/internal_version/two_run_identity.log` || `@@ -1,38 +1,38 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/ops/internal_version/two_run_identity.log` diff | "diff \--git a/artifacts/ops/internal\_version/two\_run\_identity.log b/artifacts/ops/internal\_version/two\_run\_identity.log" | "@@ \-1,38 \+1,38 @@" Hunk ID: OPR-052 | File: `artifacts/ops/internal_version/two_run_identity.log.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/ops/internal_version/two_run_identity.log.path_proof.txt b/artifacts/ops/internal_version/two_run_identity.log.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/ops/internal_version/two_run_identity.log.path_proof.txt` diff | "diff \--git a/artifacts/ops/internal\_version/two\_run\_identity.log.path\_proof.txt b/artifacts/ops/internal\_version/two\_run\_identity.log.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-053 | File: `artifacts/parity/two_run_identity.log` | Patch and hunk header: `diff --git a/artifacts/parity/two_run_identity.log b/artifacts/parity/two_run_identity.log` || `@@ -1,4 +1,4 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/parity/two_run_identity.log` diff | "diff \--git a/artifacts/parity/two\_run\_identity.log b/artifacts/parity/two\_run\_identity.log" | "@@ \-1,4 \+1,4 @@" Hunk ID: OPR-054 | File: `artifacts/parity/two_run_identity.log.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/parity/two_run_identity.log.path_proof.txt b/artifacts/parity/two_run_identity.log.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/parity/two_run_identity.log.path_proof.txt` diff | "diff \--git a/artifacts/parity/two\_run\_identity.log.path\_proof.txt b/artifacts/parity/two\_run\_identity.log.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-055 | File: `artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt b/artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt` diff | "diff \--git a/artifacts/proofs/endpoints\_env\_gate\_proof.log.path\_proof.txt b/artifacts/proofs/endpoints\_env\_gate\_proof.log.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-056 | File: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/reader_success_get_head_304.json.path_proof.txt b/artifacts/proofs/reader_success_get_head_304.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt` diff | "diff \--git a/artifacts/proofs/reader\_success\_get\_head\_304.json.path\_proof.txt b/artifacts/proofs/reader\_success\_get\_head\_304.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-057 | File: `artifacts/proofs/success_304.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_304.txt.path_proof.txt b/artifacts/proofs/success_304.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/proofs/success_304.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_304.txt.path\_proof.txt b/artifacts/proofs/success\_304.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-058 | File: `artifacts/proofs/success_encoding_invariance.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_encoding_invariance.txt.path_proof.txt b/artifacts/proofs/success_encoding_invariance.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/proofs/success_encoding_invariance.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_encoding\_invariance.txt.path\_proof.txt b/artifacts/proofs/success\_encoding\_invariance.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-059 | File: `artifacts/proofs/success_get.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_get.txt.path_proof.txt b/artifacts/proofs/success_get.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/proofs/success_get.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_get.txt.path\_proof.txt b/artifacts/proofs/success\_get.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-060 | File: `artifacts/proofs/success_head.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_head.txt.path_proof.txt b/artifacts/proofs/success_head.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/proofs/success_head.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_head.txt.path\_proof.txt b/artifacts/proofs/success\_head.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-061 | File: `artifacts/proofs/success_writers_errors.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_writers_errors.txt.path_proof.txt b/artifacts/proofs/success_writers_errors.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/proofs/success_writers_errors.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_writers\_errors.txt.path\_proof.txt b/artifacts/proofs/success\_writers\_errors.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-062 | File: `artifacts/reader/endpoints_snapshot.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/reader/endpoints_snapshot.json.path_proof.txt b/artifacts/reader/endpoints_snapshot.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/reader/endpoints_snapshot.json.path_proof.txt` diff | "diff \--git a/artifacts/reader/endpoints\_snapshot.json.path\_proof.txt b/artifacts/reader/endpoints\_snapshot.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-063 | File: `artifacts/sampler/abba/ab_ba_parity.json` | Patch and hunk header: `diff --git a/artifacts/sampler/abba/ab_ba_parity.json b/artifacts/sampler/abba/ab_ba_parity.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/sampler/abba/ab_ba_parity.json` diff | "diff \--git a/artifacts/sampler/abba/ab\_ba\_parity.json b/artifacts/sampler/abba/ab\_ba\_parity.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-064 | File: `artifacts/sampler/abba/ab_ba_parity.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/sampler/abba/ab_ba_parity.json.path_proof.txt b/artifacts/sampler/abba/ab_ba_parity.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/sampler/abba/ab_ba_parity.json.path_proof.txt` diff | "diff \--git a/artifacts/sampler/abba/ab\_ba\_parity.json.path\_proof.txt b/artifacts/sampler/abba/ab\_ba\_parity.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-065 | File: `artifacts/sampler/diversity/diversity_requirements.json` | Patch and hunk header: `diff --git a/artifacts/sampler/diversity/diversity_requirements.json b/artifacts/sampler/diversity/diversity_requirements.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/sampler/diversity/diversity_requirements.json` diff | "diff \--git a/artifacts/sampler/diversity/diversity\_requirements.json b/artifacts/sampler/diversity/diversity\_requirements.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-066 | File: `artifacts/sampler/diversity/diversity_requirements.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/sampler/diversity/diversity_requirements.json.path_proof.txt b/artifacts/sampler/diversity/diversity_requirements.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/sampler/diversity/diversity_requirements.json.path_proof.txt` diff | "diff \--git a/artifacts/sampler/diversity/diversity\_requirements.json.path\_proof.txt b/artifacts/sampler/diversity/diversity\_requirements.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-067 | File: `artifacts/sampler/pool_snapshots/baseline.json` | Patch and hunk header: `diff --git a/artifacts/sampler/pool_snapshots/baseline.json b/artifacts/sampler/pool_snapshots/baseline.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/sampler/pool_snapshots/baseline.json` diff | "diff \--git a/artifacts/sampler/pool\_snapshots/baseline.json b/artifacts/sampler/pool\_snapshots/baseline.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-068 | File: `artifacts/sampler/pool_snapshots/baseline.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/sampler/pool_snapshots/baseline.json.path_proof.txt b/artifacts/sampler/pool_snapshots/baseline.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/sampler/pool_snapshots/baseline.json.path_proof.txt` diff | "diff \--git a/artifacts/sampler/pool\_snapshots/baseline.json.path\_proof.txt b/artifacts/sampler/pool\_snapshots/baseline.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-069 | File: `artifacts/sampler/seed_replay/cli_http_seed_replay.json` | Patch and hunk header: `diff --git a/artifacts/sampler/seed_replay/cli_http_seed_replay.json b/artifacts/sampler/seed_replay/cli_http_seed_replay.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/sampler/seed_replay/cli_http_seed_replay.json` diff | "diff \--git a/artifacts/sampler/seed\_replay/cli\_http\_seed\_replay.json b/artifacts/sampler/seed\_replay/cli\_http\_seed\_replay.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-070 | File: `artifacts/sampler/seed_replay/cli_http_seed_replay.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/sampler/seed_replay/cli_http_seed_replay.json.path_proof.txt b/artifacts/sampler/seed_replay/cli_http_seed_replay.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/sampler/seed_replay/cli_http_seed_replay.json.path_proof.txt` diff | "diff \--git a/artifacts/sampler/seed\_replay/cli\_http\_seed\_replay.json.path\_proof.txt b/artifacts/sampler/seed\_replay/cli\_http\_seed\_replay.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-071 | File: `artifacts/sampler/two_run/identity.json` | Patch and hunk header: `diff --git a/artifacts/sampler/two_run/identity.json b/artifacts/sampler/two_run/identity.json` || `@@ -1 +1 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/sampler/two_run/identity.json` diff | "diff \--git a/artifacts/sampler/two\_run/identity.json b/artifacts/sampler/two\_run/identity.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-072 | File: `artifacts/sampler/two_run/identity.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/sampler/two_run/identity.json.path_proof.txt b/artifacts/sampler/two_run/identity.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/sampler/two_run/identity.json.path_proof.txt` diff | "diff \--git a/artifacts/sampler/two\_run/identity.json.path\_proof.txt b/artifacts/sampler/two\_run/identity.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-073 | File: `artifacts/sanity/sanity.log` | Patch and hunk header: `diff --git a/artifacts/sanity/sanity.log b/artifacts/sanity/sanity.log` || `@@ -1,22 +1,24 @@` | Material effect: Regenerated sanity evidence for the current deterministic pipeline. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/sanity/sanity.log` diff | "diff \--git a/artifacts/sanity/sanity.log b/artifacts/sanity/sanity.log" | "@@ \-1,22 \+1,24 @@" Hunk ID: OPR-074 | File: `artifacts/sanity/sanity.log.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/sanity/sanity.log.path_proof.txt b/artifacts/sanity/sanity.log.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/sanity/sanity.log.path_proof.txt` diff | "diff \--git a/artifacts/sanity/sanity.log.path\_proof.txt b/artifacts/sanity/sanity.log.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-075 | File: `artifacts/vendor/rails_gate_keys_only.logs.sample` | Patch and hunk header: `diff --git a/artifacts/vendor/rails_gate_keys_only.logs.sample b/artifacts/vendor/rails_gate_keys_only.logs.sample` || `@@ -0,0 +1,6 @@` | Material effect: Added the dedicated vendor rails-gate keys-only sample. | Risk category: governed evidence. | Evidence pointer: Original PR | `artifacts/vendor/rails_gate_keys_only.logs.sample` diff | "diff \--git a/artifacts/vendor/rails\_gate\_keys\_only.logs.sample b/artifacts/vendor/rails\_gate\_keys\_only.logs.sample" | "@@ \-0,0 \+1,6 @@" Hunk ID: OPR-076 | File: `artifacts/vendor/rails_gate_keys_only.logs.sample.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/vendor/rails_gate_keys_only.logs.sample.path_proof.txt b/artifacts/vendor/rails_gate_keys_only.logs.sample.path_proof.txt` || `@@ -0,0 +1,5 @@` | Material effect: Added the sibling proof anchor for the dedicated vendor rails-gate sample. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `artifacts/vendor/rails_gate_keys_only.logs.sample.path_proof.txt` diff | "diff \--git a/artifacts/vendor/rails\_gate\_keys\_only.logs.sample.path\_proof.txt b/artifacts/vendor/rails\_gate\_keys\_only.logs.sample.path\_proof.txt" | "@@ \-0,0 \+1,5 @@" Hunk ID: OPR-077 | File: `audit/gates/canonical_json/json_canon_compare.log` | Patch and hunk header: `diff --git a/audit/gates/canonical_json/json_canon_compare.log b/audit/gates/canonical_json/json_canon_compare.log` || `@@ -1,18 +1,18 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `audit/gates/canonical_json/json_canon_compare.log` diff | "diff \--git a/audit/gates/canonical\_json/json\_canon\_compare.log b/audit/gates/canonical\_json/json\_canon\_compare.log" | "@@ \-1,18 \+1,18 @@" Hunk ID: OPR-078 | File: `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt` | Patch and hunk header: `diff --git a/audit/gates/canonical_json/json_canon_compare.log.path_proof.txt b/audit/gates/canonical_json/json_canon_compare.log.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt` diff | "diff \--git a/audit/gates/canonical\_json/json\_canon\_compare.log.path\_proof.txt b/audit/gates/canonical\_json/json\_canon\_compare.log.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-079 | File: `audit/gates/canonical_json/json_canonical_check.log` | Patch and hunk header: `diff --git a/audit/gates/canonical_json/json_canonical_check.log b/audit/gates/canonical_json/json_canonical_check.log` || `@@ -1,18 +1,18 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `audit/gates/canonical_json/json_canonical_check.log` diff | "diff \--git a/audit/gates/canonical\_json/json\_canonical\_check.log b/audit/gates/canonical\_json/json\_canonical\_check.log" | "@@ \-1,18 \+1,18 @@" Hunk ID: OPR-080 | File: `audit/gates/canonical_json/json_canonical_check.log.path_proof.txt` | Patch and hunk header: `diff --git a/audit/gates/canonical_json/json_canonical_check.log.path_proof.txt b/audit/gates/canonical_json/json_canonical_check.log.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `audit/gates/canonical_json/json_canonical_check.log.path_proof.txt` diff | "diff \--git a/audit/gates/canonical\_json/json\_canonical\_check.log.path\_proof.txt b/audit/gates/canonical\_json/json\_canonical\_check.log.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-081 | File: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` | Patch and hunk header: `diff --git a/audit/gates/json_gate/canonical/json_gate_check_log.ndjson b/audit/gates/json_gate/canonical/json_gate_check_log.ndjson` || `@@ -1,18 +1,18 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` diff | "diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson" | "@@ \-1,18 \+1,18 @@" Hunk ID: OPR-082 | File: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt` | Patch and hunk header: `diff --git a/audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt b/audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt` diff | "diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson.path\_proof.txt b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-083 | File: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` | Patch and hunk header: `diff --git a/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson b/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` || `@@ -1,18 +1,18 @@` | Material effect: Regenerated deterministic release, identity, canonical-byte, or parity evidence after the Original PR closure changed the release identity. | Risk category: governed evidence. | Evidence pointer: Original PR | `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` diff | "diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson" | "@@ \-1,18 \+1,18 @@" Hunk ID: OPR-084 | File: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt` | Patch and hunk header: `diff --git a/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt b/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt` diff | "diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson.path\_proof.txt b/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-085 | File: `audit/gates/topology/orientation_demo.txt` | Patch and hunk header: `diff --git a/audit/gates/topology/orientation_demo.txt b/audit/gates/topology/orientation_demo.txt` || `@@ -1,4 +1,4 @@` | Material effect: Refreshed the governed evidence binding or proof transcript required by the Original PR evidence convergence. | Risk category: governed evidence. | Evidence pointer: Original PR | `audit/gates/topology/orientation_demo.txt` diff | "diff \--git a/audit/gates/topology/orientation\_demo.txt b/audit/gates/topology/orientation\_demo.txt" | "@@ \-1,4 \+1,4 @@" Hunk ID: OPR-086 | File: `audit/gates/topology/orientation_demo.txt.path_proof.txt` | Patch and hunk header: `diff --git a/audit/gates/topology/orientation_demo.txt.path_proof.txt b/audit/gates/topology/orientation_demo.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `audit/gates/topology/orientation_demo.txt.path_proof.txt` diff | "diff \--git a/audit/gates/topology/orientation\_demo.txt.path\_proof.txt b/audit/gates/topology/orientation\_demo.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-087 | File: `catalog/manifest.json` | Patch and hunk header: `diff --git a/catalog/manifest.json b/catalog/manifest.json` || `@@ -1 +1 @@` | Material effect: Updated the canonical manifest input affected by the final Original PR source state. | Risk category: governed manifest and release identity. | Evidence pointer: Original PR | `catalog/manifest.json` diff | "diff \--git a/catalog/manifest.json b/catalog/manifest.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-088 | File: `ci/checks/check_env_pins.sh` | Patch and hunk header: `diff --git a/ci/checks/check_env_pins.sh b/ci/checks/check_env_pins.sh` || `@@ -1,12 +1,30 @@` | Material effect: Hardened deterministic environment pin checks while preserving the governed log check. | Risk category: environment, config, vendor, or OPS-sensitive behavior. | Evidence pointer: Original PR | `ci/checks/check_env_pins.sh` diff | "diff \--git a/ci/checks/check\_env\_pins.sh b/ci/checks/check\_env\_pins.sh" | "@@ \-1,12 \+1,30 @@" Hunk ID: OPR-089 | File: `ci/checks/run_rails_job_definitions.py` | Patch and hunk header: `diff --git a/ci/checks/run_rails_job_definitions.py b/ci/checks/run_rails_job_definitions.py` || `@@ -0,0 +1,202 @@` | Material effect: Added the reusable strict rails job-definition runner with isolated subprocess execution. | Risk category: environment, config, vendor, or OPS-sensitive behavior. | Evidence pointer: Original PR | `ci/checks/run_rails_job_definitions.py` diff | "diff \--git a/ci/checks/run\_rails\_job\_definitions.py b/ci/checks/run\_rails\_job\_definitions.py" | "@@ \-0,0 \+1,202 @@" Hunk ID: OPR-090 | File: `ci/jobs/logs_keys_only_redaction.yml` | Patch and hunk header: `diff --git a/ci/jobs/logs_keys_only_redaction.yml b/ci/jobs/logs_keys_only_redaction.yml` || `@@ -1,18 +1,18 @@` | Material effect: Generalized the keys-only redaction definition and pointed it to reusable current evidence checks. | Risk category: environment, config, vendor, or OPS-sensitive behavior. | Evidence pointer: Original PR | `ci/jobs/logs_keys_only_redaction.yml` diff | "diff \--git a/ci/jobs/logs\_keys\_only\_redaction.yml b/ci/jobs/logs\_keys\_only\_redaction.yml" | "@@ \-1,18 \+1,18 @@" Hunk ID: OPR-091 | File: `ci/jobs/rails_closed_refusal.yml` | Patch and hunk header: `diff --git a/ci/jobs/rails_closed_refusal.yml b/ci/jobs/rails_closed_refusal.yml` || `@@ -1,14 +1,15 @@` | Material effect: Generalized the closed-rails refusal definition. | Risk category: environment, config, vendor, or OPS-sensitive behavior. | Evidence pointer: Original PR | `ci/jobs/rails_closed_refusal.yml` diff | "diff \--git a/ci/jobs/rails\_closed\_refusal.yml b/ci/jobs/rails\_closed\_refusal.yml" | "@@ \-1,14 \+1,15 @@" Hunk ID: OPR-092 | File: `ci/jobs/rails_open_conformance.yml` | Patch and hunk header: `diff --git a/ci/jobs/rails_open_conformance.yml b/ci/jobs/rails_open_conformance.yml` || `@@ -1,16 +1,16 @@` | Material effect: Generalized the fixture-backed open-rails provider-policy definition. | Risk category: environment, config, vendor, or OPS-sensitive behavior. | Evidence pointer: Original PR | `ci/jobs/rails_open_conformance.yml` diff | "diff \--git a/ci/jobs/rails\_open\_conformance.yml b/ci/jobs/rails\_open\_conformance.yml" | "@@ \-1,16 \+1,16 @@" Hunk ID: OPR-093 | File: `docs/ENDPOINTS_CATALOG.json.path_proof.txt` | Patch and hunk header: `diff --git a/docs/ENDPOINTS_CATALOG.json.path_proof.txt b/docs/ENDPOINTS_CATALOG.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `docs/ENDPOINTS_CATALOG.json.path_proof.txt` diff | "diff \--git a/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-094 | File: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt b/docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` diff | "diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-095 | File: `docs/evidence/INDEX.json` | Patch and hunk header: `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json` || `@@ -1 +1 @@` | Material effect: Regenerated the Human Evidence Index and added the dedicated PR-03 rails evidence record. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `docs/evidence/INDEX.json` diff | "diff \--git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json" | "@@ \-1 \+1 @@" Hunk ID: OPR-096 | File: `docs/evidence/INDEX.json.path_proof.txt` | Patch and hunk header: `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `docs/evidence/INDEX.json.path_proof.txt` diff | "diff \--git a/docs/evidence/INDEX.json.path\_proof.txt b/docs/evidence/INDEX.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-097 | File: `docs/evidence/INDEX.sha256` | Patch and hunk header: `diff --git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the checksum or hash sentinel for the corresponding final governed bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `docs/evidence/INDEX.sha256` diff | "diff \--git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256" | "@@ \-1 \+1 @@" Hunk ID: OPR-098 | File: `docs/evidence/INDEX.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Regenerated the sibling path-proof transcript for the corresponding final artifact bytes. | Risk category: governed evidence, index, mirror, manifest, or path proof. | Evidence pointer: Original PR | `docs/evidence/INDEX.sha256.path_proof.txt` diff | "diff \--git a/docs/evidence/INDEX.sha256.path\_proof.txt b/docs/evidence/INDEX.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: OPR-099 | File: `engine/runtime/identity.py` | Patch and hunk header: `diff --git a/engine/runtime/identity.py b/engine/runtime/identity.py` || `@@ -1,44 +1,44 @@` | Material effect: Updated the cut-time release identity after manifest convergence. | Risk category: contract or interface. | Evidence pointer: Original PR | `engine/runtime/identity.py` diff | "diff \--git a/engine/runtime/identity.py b/engine/runtime/identity.py" | "@@ \-1,44 \+1,44 @@" Hunk ID: OPR-100 | File: `tests/evidence/test_rails_ci_workflow_integration.py` | Patch and hunk header: `diff --git a/tests/evidence/test_rails_ci_workflow_integration.py b/tests/evidence/test_rails_ci_workflow_integration.py` || `@@ -0,0 +1,167 @@` | Material effect: Added workflow, definition, runner, producer, environment, security, and failure-path integration tests. | Risk category: insufficient tests / validation coverage. | Evidence pointer: Original PR | `tests/evidence/test_rails_ci_workflow_integration.py` diff | "diff \--git a/tests/evidence/test\_rails\_ci\_workflow\_integration.py b/tests/evidence/test\_rails\_ci\_workflow\_integration.py" | "@@ \-0,0 \+1,167 @@" Hunk ID: OPR-101 | File: `tools/evidence/generate_epic031_pr01_provider_gate.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_epic031_pr01_provider_gate.py b/tools/evidence/generate_epic031_pr01_provider_gate.py` || `@@ -257,82 +257,79 @@ def _evidence_payloads() -> dict[str, object]:` | Material effect: Removed historical EPIC031 ownership of current reusable rails job-definition bytes. | Risk category: governed evidence, security, and validation behavior. | Evidence pointer: Original PR | `tools/evidence/generate_epic031_pr01_provider_gate.py` diff | "diff \--git a/tools/evidence/generate\_epic031\_pr01\_provider\_gate.py b/tools/evidence/generate\_epic031\_pr01\_provider\_gate.py" | "@@ \-257,82 \+257,79 @@ def \_evidence\_payloads() \-\> dict\[str, object\]:" Hunk ID: OPR-102 | File: `tools/evidence/generate_epic031_pr02_log_posture.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_epic031_pr02_log_posture.py b/tools/evidence/generate_epic031_pr02_log_posture.py` || `@@ -243,39 +243,40 @@ rails:` | Material effect: Removed historical EPIC031 ownership of the current reusable keys-only definition while preserving historical evidence checks. | Risk category: governed evidence, security, and validation behavior. | Evidence pointer: Original PR | `tools/evidence/generate_epic031_pr02_log_posture.py` diff | "diff \--git a/tools/evidence/generate\_epic031\_pr02\_log\_posture.py b/tools/evidence/generate\_epic031\_pr02\_log\_posture.py" | "@@ \-243,39 \+243,40 @@ rails:" Hunk ID: OPR-103 | File: `tools/evidence/generate_rails_gate_evidence.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_rails_gate_evidence.py b/tools/evidence/generate_rails_gate_evidence.py` || `@@ -0,0 +1,217 @@` | Material effect: Added the reusable rails evidence producer for closed refusal, Retry-After, and keys-only evidence. | Risk category: governed evidence, security, and validation behavior. | Evidence pointer: Original PR | `tools/evidence/generate_rails_gate_evidence.py` diff | "diff \--git a/tools/evidence/generate\_rails\_gate\_evidence.py b/tools/evidence/generate\_rails\_gate\_evidence.py" | "@@ \-0,0 \+1,217 @@" Hunk ID: OPR-104 | File: `tools/evidence/update_evidence_index.py` | Patch and hunk header: `diff --git a/tools/evidence/update_evidence_index.py b/tools/evidence/update_evidence_index.py` || `@@ -2438,50 +2438,62 @@ EPIC038_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [` | Material effect: Registered PR-03 rails evidence and refreshed canonical Human Index/Machine Mirror bindings. | Risk category: governed evidence, security, and validation behavior. | Evidence pointer: Original PR | `tools/evidence/update_evidence_index.py` diff | "diff \--git a/tools/evidence/update\_evidence\_index.py b/tools/evidence/update\_evidence\_index.py" | "@@ \-2438,50 \+2438,62 @@ EPIC038\_PR01\_PRIMARY\_ARTIFACTS: list\[dict\[str, object\]\] \= \[" Hunk ID: OPR-105 | File: `tools/evidence/update_evidence_index.py` | Patch and hunk header: `diff --git a/tools/evidence/update_evidence_index.py b/tools/evidence/update_evidence_index.py` || `@@ -2898,50 +2910,51 @@ def _load_human_index() -> list[dict[str, object]]:` | Material effect: Registered PR-03 rails evidence and refreshed canonical Human Index/Machine Mirror bindings. | Risk category: governed evidence, security, and validation behavior. | Evidence pointer: Original PR | `tools/evidence/update_evidence_index.py` diff | "diff \--git a/tools/evidence/update\_evidence\_index.py b/tools/evidence/update\_evidence\_index.py" | "@@ \-2898,50 \+2910,51 @@ def \_load\_human\_index() \-\> list\[dict\[str, object\]\]:"

First Remedial PR Material Hunk Ledger

Hunk ID: R1PR-001 | File: `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt b/artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed current Catalog proof chronology after the first remediation evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` diff | "diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.path\_proof.txt b/artifacts/audit/ENDPOINTS\_CATALOG.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-002 | File: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt b/artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed current Catalog-checksum proof chronology. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` diff | "diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-003 | File: `artifacts/evidence_index.jsonl` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl` || `@@ -66,12 +66,12 @@` | Material effect: Regenerated affected Machine Mirror rows and added fixture/live ABâ†”BA evidence records. | Risk category: governed Machine Mirror. | Evidence pointer: First Remedial PR | `artifacts/evidence_index.jsonl` diff | "diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl" | "@@ \-66,12 \+66,12 @@" Hunk ID: R1PR-004 | File: `artifacts/evidence_index.jsonl` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl` || `@@ -184,9 +184,9 @@` | Material effect: Regenerated affected Machine Mirror rows and added fixture/live ABâ†”BA evidence records. | Risk category: governed Machine Mirror. | Evidence pointer: First Remedial PR | `artifacts/evidence_index.jsonl` diff | "diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl" | "@@ \-184,9 \+184,9 @@" Hunk ID: R1PR-005 | File: `artifacts/evidence_index.jsonl` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl` || `@@ -371,23 +371,25 @@` | Material effect: Regenerated affected Machine Mirror rows and added fixture/live ABâ†”BA evidence records. | Risk category: governed Machine Mirror. | Evidence pointer: First Remedial PR | `artifacts/evidence_index.jsonl` diff | "diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl" | "@@ \-371,23 \+371,25 @@" Hunk ID: R1PR-006 | File: `artifacts/evidence_index.jsonl` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl` || `@@ -423,8 +425,8 @@` | Material effect: Regenerated affected Machine Mirror rows and added fixture/live ABâ†”BA evidence records. | Risk category: governed Machine Mirror. | Evidence pointer: First Remedial PR | `artifacts/evidence_index.jsonl` diff | "diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl" | "@@ \-423,8 \+425,8 @@" Hunk ID: R1PR-007 | File: `artifacts/evidence_index.jsonl` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl` || `@@ -478,7 +480,7 @@` | Material effect: Regenerated affected Machine Mirror rows and added fixture/live ABâ†”BA evidence records. | Risk category: governed Machine Mirror. | Evidence pointer: First Remedial PR | `artifacts/evidence_index.jsonl` diff | "diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl" | "@@ \-478,7 \+480,7 @@" Hunk ID: R1PR-008 | File: `artifacts/evidence_index.jsonl.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed the Machine Mirror proof anchor. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/evidence_index.jsonl.path_proof.txt` diff | "diff \--git a/artifacts/evidence\_index.jsonl.path\_proof.txt b/artifacts/evidence\_index.jsonl.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-009 | File: `artifacts/evidence_index.jsonl.sha256` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the Machine Mirror checksum. | Risk category: governed evidence/checksum. | Evidence pointer: First Remedial PR | `artifacts/evidence_index.jsonl.sha256` diff | "diff \--git a/artifacts/evidence\_index.jsonl.sha256 b/artifacts/evidence\_index.jsonl.sha256" | "@@ \-1 \+1 @@" Hunk ID: R1PR-010 | File: `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed the Mirror-checksum proof anchor. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/evidence_index.jsonl.sha256.path_proof.txt` diff | "diff \--git a/artifacts/evidence\_index.jsonl.sha256.path\_proof.txt b/artifacts/evidence\_index.jsonl.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-011 | File: `artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt b/artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed existing proof chronology during canonical evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt` diff | "diff \--git a/artifacts/proofs/endpoints\_env\_gate\_proof.log.path\_proof.txt b/artifacts/proofs/endpoints\_env\_gate\_proof.log.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-012 | File: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/reader_success_get_head_304.json.path_proof.txt b/artifacts/proofs/reader_success_get_head_304.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed existing proof chronology during canonical evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt` diff | "diff \--git a/artifacts/proofs/reader\_success\_get\_head\_304.json.path\_proof.txt b/artifacts/proofs/reader\_success\_get\_head\_304.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-013 | File: `artifacts/proofs/success_304.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_304.txt.path_proof.txt b/artifacts/proofs/success_304.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed existing proof chronology during canonical evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/proofs/success_304.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_304.txt.path\_proof.txt b/artifacts/proofs/success\_304.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-014 | File: `artifacts/proofs/success_encoding_invariance.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_encoding_invariance.txt.path_proof.txt b/artifacts/proofs/success_encoding_invariance.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed existing proof chronology during canonical evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/proofs/success_encoding_invariance.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_encoding\_invariance.txt.path\_proof.txt b/artifacts/proofs/success\_encoding\_invariance.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-015 | File: `artifacts/proofs/success_get.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_get.txt.path_proof.txt b/artifacts/proofs/success_get.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed existing proof chronology during canonical evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/proofs/success_get.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_get.txt.path\_proof.txt b/artifacts/proofs/success\_get.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-016 | File: `artifacts/proofs/success_head.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_head.txt.path_proof.txt b/artifacts/proofs/success_head.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed existing proof chronology during canonical evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/proofs/success_head.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_head.txt.path\_proof.txt b/artifacts/proofs/success\_head.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-017 | File: `artifacts/proofs/success_writers_errors.txt.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/proofs/success_writers_errors.txt.path_proof.txt b/artifacts/proofs/success_writers_errors.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed existing proof chronology during canonical evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/proofs/success_writers_errors.txt.path_proof.txt` diff | "diff \--git a/artifacts/proofs/success\_writers\_errors.txt.path\_proof.txt b/artifacts/proofs/success\_writers\_errors.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-018 | File: `artifacts/reader/endpoints_snapshot.json.path_proof.txt` | Patch and hunk header: `diff --git a/artifacts/reader/endpoints_snapshot.json.path_proof.txt b/artifacts/reader/endpoints_snapshot.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed existing proof chronology during canonical evidence convergence. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `artifacts/reader/endpoints_snapshot.json.path_proof.txt` diff | "diff \--git a/artifacts/reader/endpoints\_snapshot.json.path\_proof.txt b/artifacts/reader/endpoints\_snapshot.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-019 | File: `audit/gates/determinism/open_rails_abba.json` | Patch and hunk header: `diff --git a/audit/gates/determinism/open_rails_abba.json b/audit/gates/determinism/open_rails_abba.json` || `@@ -0,0 +1 @@` | Material effect: Added the governed fixture-backed open-rails ABâ†”BA deterministic proof. | Risk category: governed determinism evidence. | Evidence pointer: First Remedial PR | `audit/gates/determinism/open_rails_abba.json` diff | "diff \--git a/audit/gates/determinism/open\_rails\_abba.json b/audit/gates/determinism/open\_rails\_abba.json" | "@@ \-0,0 \+1 @@" Hunk ID: R1PR-020 | File: `audit/gates/determinism/open_rails_abba.json.path_proof.txt` | Patch and hunk header: `diff --git a/audit/gates/determinism/open_rails_abba.json.path_proof.txt b/audit/gates/determinism/open_rails_abba.json.path_proof.txt` || `@@ -0,0 +1,5 @@` | Material effect: Added the fixture-proof sibling path anchor. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `audit/gates/determinism/open_rails_abba.json.path_proof.txt` diff | "diff \--git a/audit/gates/determinism/open\_rails\_abba.json.path\_proof.txt b/audit/gates/determinism/open\_rails\_abba.json.path\_proof.txt" | "@@ \-0,0 \+1,5 @@" Hunk ID: R1PR-021 | File: `audit/gates/determinism/open_rails_vendor_abba.json` | Patch and hunk header: `diff --git a/audit/gates/determinism/open_rails_vendor_abba.json b/audit/gates/determinism/open_rails_vendor_abba.json` || `@@ -0,0 +1 @@` | Material effect: Added the bounded PO-authorized live vendor ABâ†”BA proof. | Risk category: vendor/OPS-sensitive governed evidence. | Evidence pointer: First Remedial PR | `audit/gates/determinism/open_rails_vendor_abba.json` diff | "diff \--git a/audit/gates/determinism/open\_rails\_vendor\_abba.json b/audit/gates/determinism/open\_rails\_vendor\_abba.json" | "@@ \-0,0 \+1 @@" Hunk ID: R1PR-022 | File: `audit/gates/determinism/open_rails_vendor_abba.json.path_proof.txt` | Patch and hunk header: `diff --git a/audit/gates/determinism/open_rails_vendor_abba.json.path_proof.txt b/audit/gates/determinism/open_rails_vendor_abba.json.path_proof.txt` || `@@ -0,0 +1,5 @@` | Material effect: Added the live-proof sibling path anchor. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `audit/gates/determinism/open_rails_vendor_abba.json.path_proof.txt` diff | "diff \--git a/audit/gates/determinism/open\_rails\_vendor\_abba.json.path\_proof.txt b/audit/gates/determinism/open\_rails\_vendor\_abba.json.path\_proof.txt" | "@@ \-0,0 \+1,5 @@" Hunk ID: R1PR-023 | File: `audit/gates/topology/orientation_demo.txt` | Patch and hunk header: `diff --git a/audit/gates/topology/orientation_demo.txt b/audit/gates/topology/orientation_demo.txt` || `@@ -1,4 +1,4 @@` | Material effect: Regenerated topology orientation for the expanded evidence catalog. | Risk category: governed evidence. | Evidence pointer: First Remedial PR | `audit/gates/topology/orientation_demo.txt` diff | "diff \--git a/audit/gates/topology/orientation\_demo.txt b/audit/gates/topology/orientation\_demo.txt" | "@@ \-1,4 \+1,4 @@" Hunk ID: R1PR-024 | File: `audit/gates/topology/orientation_demo.txt.path_proof.txt` | Patch and hunk header: `diff --git a/audit/gates/topology/orientation_demo.txt.path_proof.txt b/audit/gates/topology/orientation_demo.txt.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed the orientation proof anchor. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `audit/gates/topology/orientation_demo.txt.path_proof.txt` diff | "diff \--git a/audit/gates/topology/orientation\_demo.txt.path\_proof.txt b/audit/gates/topology/orientation\_demo.txt.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-025 | File: `ci/checks/run_rails_job_definitions.py` | Patch and hunk header: `diff --git a/ci/checks/run_rails_job_definitions.py b/ci/checks/run_rails_job_definitions.py` || `@@ -7,6 +7,7 @@` | Material effect: Added argv parsing support for exact command-vector validation. | Risk category: security/environment execution rail. | Evidence pointer: First Remedial PR | `ci/checks/run_rails_job_definitions.py` diff | "diff \--git a/ci/checks/run\_rails\_job\_definitions.py b/ci/checks/run\_rails\_job\_definitions.py" | "@@ \-7,6 \+7,7 @@" Hunk ID: R1PR-026 | File: `ci/checks/run_rails_job_definitions.py` | Patch and hunk header: `diff --git a/ci/checks/run_rails_job_definitions.py b/ci/checks/run_rails_job_definitions.py` || `@@ -22,6 +23,18 @@` | Material effect: Added exact per-identity command allowlists. | Risk category: security/environment execution rail. | Evidence pointer: First Remedial PR | `ci/checks/run_rails_job_definitions.py` diff | "diff \--git a/ci/checks/run\_rails\_job\_definitions.py b/ci/checks/run\_rails\_job\_definitions.py" | "@@ \-22,6 \+23,18 @@" Hunk ID: R1PR-027 | File: `ci/checks/run_rails_job_definitions.py` | Patch and hunk header: `diff --git a/ci/checks/run_rails_job_definitions.py b/ci/checks/run_rails_job_definitions.py` || `@@ -117,6 +130,40 @@` | Material effect: Added command-embedded credential and wrapper rejection. | Risk category: security/environment execution rail. | Evidence pointer: First Remedial PR | `ci/checks/run_rails_job_definitions.py` diff | "diff \--git a/ci/checks/run\_rails\_job\_definitions.py b/ci/checks/run\_rails\_job\_definitions.py" | "@@ \-117,6 \+130,40 @@" Hunk ID: R1PR-028 | File: `ci/checks/run_rails_job_definitions.py` | Patch and hunk header: `diff --git a/ci/checks/run_rails_job_definitions.py b/ci/checks/run_rails_job_definitions.py` || `@@ -157,6 +204,12 @@` | Material effect: Scrubbed ambient sensitive variables and built isolated child environments. | Risk category: security/environment execution rail. | Evidence pointer: First Remedial PR | `ci/checks/run_rails_job_definitions.py` diff | "diff \--git a/ci/checks/run\_rails\_job\_definitions.py b/ci/checks/run\_rails\_job\_definitions.py" | "@@ \-157,6 \+204,12 @@" Hunk ID: R1PR-029 | File: `ci/checks/run_rails_job_definitions.py` | Patch and hunk header: `diff --git a/ci/checks/run_rails_job_definitions.py b/ci/checks/run_rails_job_definitions.py` || `@@ -169,6 +222,8 @@` | Material effect: Enforced allowlist validation before subprocess execution. | Risk category: security/environment execution rail. | Evidence pointer: First Remedial PR | `ci/checks/run_rails_job_definitions.py` diff | "diff \--git a/ci/checks/run\_rails\_job\_definitions.py b/ci/checks/run\_rails\_job\_definitions.py" | "@@ \-169,6 \+222,8 @@" Hunk ID: R1PR-030 | File: `ci/jobs/rails_open_conformance.yml` | Patch and hunk header: `diff --git a/ci/jobs/rails_open_conformance.yml b/ci/jobs/rails_open_conformance.yml` || `@@ -8,9 +8,19 @@` | Material effect: Added fixture-backed open-rails ABâ†”BA/canonical proof commands and explicit proof statements. | Risk category: environment/vendor/CI behavior. | Evidence pointer: First Remedial PR | `ci/jobs/rails_open_conformance.yml` diff | "diff \--git a/ci/jobs/rails\_open\_conformance.yml b/ci/jobs/rails\_open\_conformance.yml" | "@@ \-8,9 \+8,19 @@" Hunk ID: R1PR-031 | File: `docs/ENDPOINTS_CATALOG.json.path_proof.txt` | Patch and hunk header: `diff --git a/docs/ENDPOINTS_CATALOG.json.path_proof.txt b/docs/ENDPOINTS_CATALOG.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed current Catalog proof chronology. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `docs/ENDPOINTS_CATALOG.json.path_proof.txt` diff | "diff \--git a/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-032 | File: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt b/docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed current Catalog-checksum proof chronology. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` diff | "diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-033 | File: `docs/evidence/INDEX.json` | Patch and hunk header: `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json` || `complete generated record-rewrite hunk` | Material effect: Added fixture/live ABâ†”BA Human Index bindings and refreshed affected records. | Risk category: governed Human Evidence Index. | Evidence pointer: First Remedial PR | `docs/evidence/INDEX.json` diff | "diff \--git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json" | "complete generated record-rewrite hunk" Hunk ID: R1PR-034 | File: `docs/evidence/INDEX.json.path_proof.txt` | Patch and hunk header: `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed the Human Index proof anchor. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `docs/evidence/INDEX.json.path_proof.txt` diff | "diff \--git a/docs/evidence/INDEX.json.path\_proof.txt b/docs/evidence/INDEX.json.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-035 | File: `docs/evidence/INDEX.sha256` | Patch and hunk header: `diff --git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256` || `@@ -1 +1 @@` | Material effect: Regenerated the Human Index hash sentinel. | Risk category: governed evidence/hash sentinel. | Evidence pointer: First Remedial PR | `docs/evidence/INDEX.sha256` diff | "diff \--git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256" | "@@ \-1 \+1 @@" Hunk ID: R1PR-036 | File: `docs/evidence/INDEX.sha256.path_proof.txt` | Patch and hunk header: `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt` || `@@ -1,5 +1,5 @@` | Material effect: Refreshed the sentinel proof anchor. | Risk category: governed evidence/path proof. | Evidence pointer: First Remedial PR | `docs/evidence/INDEX.sha256.path_proof.txt` diff | "diff \--git a/docs/evidence/INDEX.sha256.path\_proof.txt b/docs/evidence/INDEX.sha256.path\_proof.txt" | "@@ \-1,5 \+1,5 @@" Hunk ID: R1PR-037 | File: `tests/evidence/test_open_rails_abba_proof.py` | Patch and hunk header: `diff --git a/tests/evidence/test_open_rails_abba_proof.py b/tests/evidence/test_open_rails_abba_proof.py` || `@@ -0,0 +1,534 @@` | Material effect: Added fixture and live ABâ†”BA positive/negative tests, request-bound checks, non-writing checks, and safety checks. | Risk category: insufficient-tests / vendor-safety posture. | Evidence pointer: First Remedial PR | `tests/evidence/test_open_rails_abba_proof.py` diff | "diff \--git a/tests/evidence/test\_open\_rails\_abba\_proof.py b/tests/evidence/test\_open\_rails\_abba\_proof.py" | "@@ \-0,0 \+1,534 @@" Hunk ID: R1PR-038 | File: `tests/evidence/test_rails_ci_workflow_integration.py` | Patch and hunk header: `diff --git a/tests/evidence/test_rails_ci_workflow_integration.py b/tests/evidence/test_rails_ci_workflow_integration.py` || `@@ -19,6 +19,12 @@` | Material effect: Added new producer/artifact constants and current ownership assertions. | Risk category: insufficient-tests / security validation. | Evidence pointer: First Remedial PR | `tests/evidence/test_rails_ci_workflow_integration.py` diff | "diff \--git a/tests/evidence/test\_rails\_ci\_workflow\_integration.py b/tests/evidence/test\_rails\_ci\_workflow\_integration.py" | "@@ \-19,6 \+19,12 @@" Hunk ID: R1PR-039 | File: `tests/evidence/test_rails_ci_workflow_integration.py` | Patch and hunk header: `diff --git a/tests/evidence/test_rails_ci_workflow_integration.py b/tests/evidence/test_rails_ci_workflow_integration.py` || `@@ -64,7 +70,16 @@` | Material effect: Updated exact allowed commands for open-rails conformance. | Risk category: insufficient-tests / security validation. | Evidence pointer: First Remedial PR | `tests/evidence/test_rails_ci_workflow_integration.py` diff | "diff \--git a/tests/evidence/test\_rails\_ci\_workflow\_integration.py b/tests/evidence/test\_rails\_ci\_workflow\_integration.py" | "@@ \-64,7 \+70,16 @@" Hunk ID: R1PR-040 | File: `tests/evidence/test_rails_ci_workflow_integration.py` | Patch and hunk header: `diff --git a/tests/evidence/test_rails_ci_workflow_integration.py b/tests/evidence/test_rails_ci_workflow_integration.py` || `@@ -84,7 +99,12 @@` | Material effect: Extended expected job-definition structure for ABâ†”BA checks. | Risk category: insufficient-tests / security validation. | Evidence pointer: First Remedial PR | `tests/evidence/test_rails_ci_workflow_integration.py` diff | "diff \--git a/tests/evidence/test\_rails\_ci\_workflow\_integration.py b/tests/evidence/test\_rails\_ci\_workflow\_integration.py" | "@@ \-84,7 \+99,12 @@" Hunk ID: R1PR-041 | File: `tests/evidence/test_rails_ci_workflow_integration.py` | Patch and hunk header: `diff --git a/tests/evidence/test_rails_ci_workflow_integration.py b/tests/evidence/test_rails_ci_workflow_integration.py` || `@@ -114,19 +134,28 @@` | Material effect: Strengthened producer non-writing and ownership assertions. | Risk category: insufficient-tests / security validation. | Evidence pointer: First Remedial PR | `tests/evidence/test_rails_ci_workflow_integration.py` diff | "diff \--git a/tests/evidence/test\_rails\_ci\_workflow\_integration.py b/tests/evidence/test\_rails\_ci\_workflow\_integration.py" | "@@ \-114,19 \+134,28 @@" Hunk ID: R1PR-042 | File: `tests/evidence/test_rails_ci_workflow_integration.py` | Patch and hunk header: `diff --git a/tests/evidence/test_rails_ci_workflow_integration.py b/tests/evidence/test_rails_ci_workflow_integration.py` || `@@ -165,3 +194,53 @@` | Material effect: Added command-credential, no-residue, and compatibility regressions. | Risk category: insufficient-tests / security validation. | Evidence pointer: First Remedial PR | `tests/evidence/test_rails_ci_workflow_integration.py` diff | "diff \--git a/tests/evidence/test\_rails\_ci\_workflow\_integration.py b/tests/evidence/test\_rails\_ci\_workflow\_integration.py" | "@@ \-165,3 \+194,53 @@" Hunk ID: R1PR-043 | File: `tools/evidence/generate_open_rails_abba_proof.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_open_rails_abba_proof.py b/tools/evidence/generate_open_rails_abba_proof.py` || `@@ -0,0 +1,571 @@` | Material effect: Added fixture-backed and bounded live ABâ†”BA proof generation, write/check modes, transport guards, and secret-safe evidence rendering. | Risk category: vendor/OPS-sensitive governed evidence producer. | Evidence pointer: First Remedial PR | `tools/evidence/generate_open_rails_abba_proof.py` diff | "diff \--git a/tools/evidence/generate\_open\_rails\_abba\_proof.py b/tools/evidence/generate\_open\_rails\_abba\_proof.py" | "@@ \-0,0 \+1,571 @@" Hunk ID: R1PR-044 | File: `tools/evidence/generate_rails_gate_evidence.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_rails_gate_evidence.py b/tools/evidence/generate_rails_gate_evidence.py` || `@@ -7,6 +7,7 @@` | Material effect: Added external temporary-directory support. | Risk category: governed evidence writer / check-mode safety. | Evidence pointer: First Remedial PR | `tools/evidence/generate_rails_gate_evidence.py` diff | "diff \--git a/tools/evidence/generate\_rails\_gate\_evidence.py b/tools/evidence/generate\_rails\_gate\_evidence.py" | "@@ \-7,6 \+7,7 @@" Hunk ID: R1PR-045 | File: `tools/evidence/generate_rails_gate_evidence.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_rails_gate_evidence.py b/tools/evidence/generate_rails_gate_evidence.py` || `@@ -24,8 +25,6 @@` | Material effect: Removed feature-producer path-proof ownership. | Risk category: governed evidence writer / check-mode safety. | Evidence pointer: First Remedial PR | `tools/evidence/generate_rails_gate_evidence.py` diff | "diff \--git a/tools/evidence/generate\_rails\_gate\_evidence.py b/tools/evidence/generate\_rails\_gate\_evidence.py" | "@@ \-24,8 \+25,6 @@" Hunk ID: R1PR-046 | File: `tools/evidence/generate_rails_gate_evidence.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_rails_gate_evidence.py b/tools/evidence/generate_rails_gate_evidence.py` || `@@ -54,25 +53,19 @@` | Material effect: Refactored primary write/check behavior to primary artifacts only. | Risk category: governed evidence writer / check-mode safety. | Evidence pointer: First Remedial PR | `tools/evidence/generate_rails_gate_evidence.py` diff | "diff \--git a/tools/evidence/generate\_rails\_gate\_evidence.py b/tools/evidence/generate\_rails\_gate\_evidence.py" | "@@ \-54,25 \+53,19 @@" Hunk ID: R1PR-047 | File: `tools/evidence/generate_rails_gate_evidence.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_rails_gate_evidence.py b/tools/evidence/generate_rails_gate_evidence.py` || `@@ -134,8 +127,6 @@` | Material effect: Removed the fixed repository-root temporary path. | Risk category: governed evidence writer / check-mode safety. | Evidence pointer: First Remedial PR | `tools/evidence/generate_rails_gate_evidence.py` diff | "diff \--git a/tools/evidence/generate\_rails\_gate\_evidence.py b/tools/evidence/generate\_rails\_gate\_evidence.py" | "@@ \-134,8 \+127,6 @@" Hunk ID: R1PR-048 | File: `tools/evidence/generate_rails_gate_evidence.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_rails_gate_evidence.py b/tools/evidence/generate_rails_gate_evidence.py` || `@@ -153,21 +144,22 @@` | Material effect: Made keys-only sample construction residue-free and environment-safe. | Risk category: governed evidence writer / check-mode safety. | Evidence pointer: First Remedial PR | `tools/evidence/generate_rails_gate_evidence.py` diff | "diff \--git a/tools/evidence/generate\_rails\_gate\_evidence.py b/tools/evidence/generate\_rails\_gate\_evidence.py" | "@@ \-153,21 \+144,22 @@" Hunk ID: R1PR-049 | File: `tools/evidence/update_evidence_index.py` | Patch and hunk header: `diff --git a/tools/evidence/update_evidence_index.py b/tools/evidence/update_evidence_index.py` || `@@ -2470,6 +2470,24 @@` | Material effect: Registered fixture/live ABâ†”BA artifacts under canonical updater ownership. | Risk category: governed evidence/index/path-proof writer. | Evidence pointer: First Remedial PR | `tools/evidence/update_evidence_index.py` diff | "diff \--git a/tools/evidence/update\_evidence\_index.py b/tools/evidence/update\_evidence\_index.py" | "@@ \-2470,6 \+2470,24 @@"

Second Remedial PR Material Hunk Ledger

Hunk ID: R2PR-001 | File: `tests/evidence/test_open_rails_abba_proof.py` | Patch and hunk header: `diff --git a/tests/evidence/test_open_rails_abba_proof.py b/tests/evidence/test_open_rails_abba_proof.py` || `@@ -118,54 +118,56 @@ def _configure_individual_live_fake(monkeypatch: pytest.MonkeyPatch) -> list[str` | Material effect: Adjusted fake live responses and test setup to match the strict final live-proof schema. | Risk category: insufficient tests / live vendor proof. | Evidence pointer: Second Remedial PR | `tests/evidence/test_open_rails_abba_proof.py` diff | "diff \--git a/tests/evidence/test\_open\_rails\_abba\_proof.py b/tests/evidence/test\_open\_rails\_abba\_proof.py" | "@@ \-118,54 \+118,56 @@ def \_configure\_individual\_live\_fake(monkeypatch: pytest.MonkeyPatch) \-\> list\[str" Hunk ID: R2PR-002 | File: `tests/evidence/test_open_rails_abba_proof.py` | Patch and hunk header: `diff --git a/tests/evidence/test_open_rails_abba_proof.py b/tests/evidence/test_open_rails_abba_proof.py` || `@@ -451,51 +453,51 @@ def test_live_check_mode_recomputes_distinctness(` | Material effect: Expanded live check-mode tests for independently derived distinctness, payload binding, ABâ†”BA, request bounds, and prohibited content. | Risk category: insufficient tests / live proof validation. | Evidence pointer: Second Remedial PR | `tests/evidence/test_open_rails_abba_proof.py` diff | "diff \--git a/tests/evidence/test\_open\_rails\_abba\_proof.py b/tests/evidence/test\_open\_rails\_abba\_proof.py" | "@@ \-451,51 \+453,51 @@ def test\_live\_check\_mode\_recomputes\_distinctness(" Hunk ID: R2PR-003 | File: `tests/evidence/test_open_rails_abba_proof.py` | Patch and hunk header: `diff --git a/tests/evidence/test_open_rails_abba_proof.py b/tests/evidence/test_open_rails_abba_proof.py` || `@@ -510,25 +512,109 @@ def test_live_write_mode_rejects_nonpassing_proof_without_overwrite(` | Material effect: Added exact-schema, unknown-key, allowed-key-value, optional-env, read-only check, and pass-only write regressions. | Risk category: insufficient tests / safety and schema validation. | Evidence pointer: Second Remedial PR | `tests/evidence/test_open_rails_abba_proof.py` diff | "diff \--git a/tests/evidence/test\_open\_rails\_abba\_proof.py b/tests/evidence/test\_open\_rails\_abba\_proof.py" | "@@ \-510,25 \+512,109 @@ def test\_live\_write\_mode\_rejects\_nonpassing\_proof\_without\_overwrite(" Hunk ID: R2PR-004 | File: `tools/evidence/generate_open_rails_abba_proof.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_open_rails_abba_proof.py b/tools/evidence/generate_open_rails_abba_proof.py` || `@@ -1,162 +1,352 @@` | Material effect: Added the closed live-proof schema, prohibited key/string vocabulary, recursive safety scanning, and validation helpers. | Risk category: schema, privacy, and vendor-proof validation. | Evidence pointer: Second Remedial PR | `tools/evidence/generate_open_rails_abba_proof.py` diff | "diff \--git a/tools/evidence/generate\_open\_rails\_abba\_proof.py b/tools/evidence/generate\_open\_rails\_abba\_proof.py" | "@@ \-1,162 \+1,352 @@" Hunk ID: R2PR-005 | File: `tools/evidence/generate_open_rails_abba_proof.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_open_rails_abba_proof.py b/tools/evidence/generate_open_rails_abba_proof.py` || `@@ -361,50 +551,51 @@ def build_live_proof(` | Material effect: Aligned live-proof construction with the final required schema, optional environment field, and derived predicate inputs. | Risk category: vendor/OPS-sensitive evidence construction. | Evidence pointer: Second Remedial PR | `tools/evidence/generate_open_rails_abba_proof.py` diff | "diff \--git a/tools/evidence/generate\_open\_rails\_abba\_proof.py b/tools/evidence/generate\_open\_rails\_abba\_proof.py" | "@@ \-361,50 \+551,51 @@ def build\_live\_proof(" Hunk ID: R2PR-006 | File: `tools/evidence/generate_open_rails_abba_proof.py` | Patch and hunk header: `diff --git a/tools/evidence/generate_open_rails_abba_proof.py b/tools/evidence/generate_open_rails_abba_proof.py` || `@@ -490,50 +681,51 @@ def build_live_proof(` | Material effect: Recomputed decisive live predicates from recorded hashes/results, validated read-only check mode, and allowed writes only for fully passing proofs. | Risk category: vendor/OPS-sensitive fail-closed validation. | Evidence pointer: Second Remedial PR | `tools/evidence/generate_open_rails_abba_proof.py` diff | "diff \--git a/tools/evidence/generate\_open\_rails\_abba\_proof.py b/tools/evidence/generate\_open\_rails\_abba\_proof.py" | "@@ \-490,50 \+681,51 @@ def build\_live\_proof("

Net Effective Diff Review

NET-001 | File/artifact: `.github/workflows/ci.yml` | Covered hunks: OPR-001 | Combined merged state: Dedicated closed-default `rails-policy-gates` job invokes the three validated definitions through the strict runner. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `.github/workflows/ci.yml` current file and lifecycle patches | "present at current main" | "covered by OPR-001" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | ".github/workflows/ci.yml" | "no later commit divergence" | PF reference, if relied on: None. NET-002 | File/artifact: `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` | Covered hunks: OPR-002 / R1PR-001 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-002 / R1PR-001" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/audit/ENDPOINTS\_CATALOG.json.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-003 | File/artifact: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` | Covered hunks: OPR-003 / R1PR-002 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-003 / R1PR-002" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/audit/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-004 | File/artifact: `artifacts/bodygraph/keys_only.logs.sample.path_proof.txt` | Covered hunks: OPR-004 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/bodygraph/keys_only.logs.sample.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-004" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/bodygraph/keys\_only.logs.sample.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-005 | File/artifact: `artifacts/bodygraph/release_bindings.json` | Covered hunks: OPR-005 | Combined merged state: BodyGraph evidence ownership and release binding remain preserved without collision with the dedicated rails evidence path. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/bodygraph/release_bindings.json` current file and lifecycle patches | "present at current main" | "covered by OPR-005" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/bodygraph/release\_bindings.json" | "no later commit divergence" | PF reference, if relied on: None. NET-006 | File/artifact: `artifacts/bodygraph/release_bindings.json.path_proof.txt` | Covered hunks: OPR-006 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/bodygraph/release_bindings.json.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-006" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/bodygraph/release\_bindings.json.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-007 | File/artifact: `artifacts/cli/ab.json` | Covered hunks: OPR-007 | Combined merged state: Regenerated deterministic identity/canonical evidence remains current and coherent with the final release identity. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/ab.json` current file and lifecycle patches | "present at current main" | "covered by OPR-007" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/ab.json" | "no later commit divergence" | PF reference, if relied on: None. NET-008 | File/artifact: `artifacts/cli/ab.json.path_proof.txt` | Covered hunks: OPR-008 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/ab.json.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-008" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/ab.json.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-009 | File/artifact: `artifacts/cli/ba.json` | Covered hunks: OPR-009 | Combined merged state: Regenerated deterministic identity/canonical evidence remains current and coherent with the final release identity. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/ba.json` current file and lifecycle patches | "present at current main" | "covered by OPR-009" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/ba.json" | "no later commit divergence" | PF reference, if relied on: None. NET-010 | File/artifact: `artifacts/cli/ba.json.path_proof.txt` | Covered hunks: OPR-010 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/ba.json.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-010" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/ba.json.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-011 | File/artifact: `artifacts/cli/install/installability_summary.json` | Covered hunks: OPR-011 | Combined merged state: Regenerated deterministic identity/canonical evidence remains current and coherent with the final release identity. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/install/installability_summary.json` current file and lifecycle patches | "present at current main" | "covered by OPR-011" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/install/installability\_summary.json" | "no later commit divergence" | PF reference, if relied on: None. NET-012 | File/artifact: `artifacts/cli/install/installability_summary.json.path_proof.txt` | Covered hunks: OPR-012 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/install/installability_summary.json.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-012" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/install/installability\_summary.json.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-013 | File/artifact: `artifacts/cli/showcompat/args.json` | Covered hunks: OPR-013 | Combined merged state: Regenerated deterministic identity/canonical evidence remains current and coherent with the final release identity. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/showcompat/args.json` current file and lifecycle patches | "present at current main" | "covered by OPR-013" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/showcompat/args.json" | "no later commit divergence" | PF reference, if relied on: None. NET-014 | File/artifact: `artifacts/cli/showcompat/args.json.path_proof.txt` | Covered hunks: OPR-014 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/showcompat/args.json.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-014" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/showcompat/args.json.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-015 | File/artifact: `artifacts/cli/showcompat/stdout.json` | Covered hunks: OPR-015 | Combined merged state: Regenerated deterministic identity/canonical evidence remains current and coherent with the final release identity. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/showcompat/stdout.json` current file and lifecycle patches | "present at current main" | "covered by OPR-015" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/showcompat/stdout.json" | "no later commit divergence" | PF reference, if relied on: None. NET-016 | File/artifact: `artifacts/cli/showcompat/stdout.json.path_proof.txt` | Covered hunks: OPR-016 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/showcompat/stdout.json.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-016" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/showcompat/stdout.json.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-017 | File/artifact: `artifacts/cli/showcompat/stdout.json.sha256` | Covered hunks: OPR-017 | Combined merged state: Regenerated deterministic identity/canonical evidence remains current and coherent with the final release identity. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/showcompat/stdout.json.sha256` current file and lifecycle patches | "present at current main" | "covered by OPR-017" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/showcompat/stdout.json.sha256" | "no later commit divergence" | PF reference, if relied on: None. NET-018 | File/artifact: `artifacts/cli/showcompat/stdout.json.sha256.path_proof.txt` | Covered hunks: OPR-018 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/showcompat/stdout.json.sha256.path_proof.txt` current file and lifecycle patches | "present at current main" | "covered by OPR-018" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/showcompat/stdout.json.sha256.path\_proof.txt" | "no later commit divergence" | PF reference, if relied on: None. NET-019 | File/artifact: `artifacts/cli/summary.json` | Covered hunks: OPR-019 | Combined merged state: Regenerated deterministic identity/canonical evidence remains current and coherent with the final release identity. | Current final repo state: Same as the combined merged state at current `main`. | Later-change impact: None | Risk: High | High-risk hunk assessment, if applicable: Final source/artifact state and its direct tests or canonical bindings were inspected; no unresolved defect remains. | Assessment: Current and supportable for the reviewed PR-03 scope. | Evidence pointer(s): GitHub Repo | `artifacts/cli/summary.json` current file and lifecycle patches | "present at current main" | "covered by OPR-019" | GitHub Repo proof: GitHub Repo | current `main` file fetch / combined compare | "artifacts/cli/summary.json" | "no later commit divergence" | PF reference, if relied on: None. NET-020 | File/artifact: `artifacts/cli/summary.json.path_proof.txt` | Covered hunks: OPR-020 | Combined merged state: Current sibling proof records the governed path, size, hash, and production timestamp for the final artifact bytes. | Current÷Î¶ó†òµë(š+myÕ52â ¤ö'6W'fF–öã¢W†7Bw&—FRF‡2Â&V7W'6—fR&ö÷G2ÂÖWFFFF‡2ÂæB6VÆbW†6ÇW6–öç2&R&V6ö×WFVBg&öÒ&VfÆ–v‡Bö6öçG&öÂ÷6÷W&6RF‡2â ¤Wf–FVæ6Rö–çFW#¢&VÖVF–Â""Â#%"ÓrÂ#%"Ó3Â&WF†÷&—¦VEöW†7E÷w&—FU÷F‡3Õ·&VfÆ–v‡E÷F…Ò&Â'6VÆeö&÷VæEöW†6ÇVFVE÷F‡3Õ·&VfÆ–v‡E÷F…Ò&â ¥v‡’—BÖGFW'3¢&WF–æVB'F–f7B6ææ÷Bv–FVâ—G26Æ–ÖVBw&—FRWF†÷&—G’à ¥dÂÓ’ ¥W'÷6S¢6öæf—&ÒFWFW&Ö–æ—7F–2Gvò×'Vâ&÷VæF'’â ¥6÷W&6S¢–×ÆVÖVçFF–öâFö3²&VÖVF–Â"%Ââ ¤ÖWF†öC¢&÷fVB66†VÖ6ö×&—6öâæB&V7W'6—fRÖ¶W’fÆ–FF–öââ ¥&W7VÇC¢52â ¤ö'6W'fF–öã¢F†R&÷fVB6öçG&7B—2W†7BæÖVBÖVÖ&W'2'VåóæB'Våó&ÂV6‚v—F‚W†7B7GVÅöW‡FW&æÅö–õö6÷VçG6æBW‡V7FVEö6ÆÅö6÷VçG6â6W&FR'VåöÆ&VÃ¢ô&&÷r—2æ÷B'BöbF†R6÷W&6R6öçG&7Bâ7W'&VçBfÆ–FF÷"&V¦V7G2Ö—76–ærÂW‡G&Â÷"ÖÆf÷&ÖVBÖVÖ&W'2â ¤Wf–FVæ6Rö–çFW#¢–×ÆVÖVçFF–öâFö2Â*v%42ÓBä6÷W&6RæBöffÆ–æR&VfÆ–v‡B6öçG&7BÂ&÷&6†W7G&F–öâ†2W†7FÇ’f¶Uö&÷VæF'•öÖöFRÂ'VåóÂ'Våó"Â'Våö6÷VçBÂæBfV7F÷'5öWVÂ&Â''VåóæB'Våó"V6‚†fRW†7FÇ’7GVÅöW‡FW&æÅö–õö6÷VçG2æBW‡V7FVEö6ÆÅö6÷VçG2&²&VÖVF–Â""Â#%"Ó#’Â&W†7BæÖVB'Våó÷'Våó"fV7F÷'2&Â''Våö6÷VçCÓ"&â ¥v‡’—BÖGFW'3¢F†RV&Æ–W"ô"ÖÆ&VÂf–æF–ær—26WGFÆVB'’Væf÷&6–ærF†R7GVÂ&÷fVB66†VÖÂæ÷Bâö'6öÆWFR&÷rÖöFVÂà ¥dÂÓ ¥W'÷6S¢6öæf—&ÒW†7B&VfÆ–v‡B&wbfV7F÷'2â ¥6÷W&6S¢&VÖVF–Â"%Ââ ¤ÖWF†öC¢gVÆÂ×fV7F÷"&V6öç7G'V7F–öâæB×WFF–öâFW7G2â ¥&W7VÇC¢52â ¤ö'6W'fF–öã¢&öGV6W"—2W†7FÇ’¶–çFW'&WFW"Â"Ô’"Â"Ô""Â'VææW"Â"Ò×&VfÆ–v‡B%Ö²fÆ–FF÷"—2W†7FÇ’F†R6WfVâ×Fö¶VâfV7F÷"v—F‚Ò×fÆ–FFR×&VfÆ–v‡FÂÒÖW‡V7FVBÖ–FVçF—G’×7FF–æÂæB&VfÆ–v‡BF‚â ¤Wf–FVæ6Rö–çFW#¢–×ÆVÖVçFF–öâFö2Â*v%42ÓBäÂ&W†7B6öÆR&öGV6W"&wb&Â'&VfÆ–v‡E÷fÆ–FF÷%ö&wcÕ²ââåÒ&²&VÖVF–Â""Â#%"ÓBÂ#%"Ó#‚Â'v†öÆR×fV7F÷"WVÆ—G’&Â&W‡G&öÖ—76–ær÷7V'7F—GWFVBFö¶Vâ&V¦V7F–öâ&â ¥v‡’—BÖGFW'3¢&VfÆ–v‡B6ææ÷BÖ—77FFR—G2&öGV6–ær6öÖÖæBà ¥dÂÓ ¥W'÷6S¢6öæf—&ÒWF†÷&—¦F–öâ7F&–Æ—G’BF—66÷fW'’F—7F6‚â ¥6÷W&6S¢&VÖVF–Â"%Ââ ¤ÖWF†öC¢6öçG&öÂÖfÆ÷r–ç7V7F–öâæB×WFF–öâf—‡GW&Râ ¥&W7VÇC¢52â ¤ö'6W'fF–öã¢f–æÂWF†÷&—¦F–öâ'—FRWVÆ—G’ö67W'2gFW"F†RÆ7B7Fv–ærvÆ²æB–ÖÖVF–FVÇ’&Vf÷&R7V'&ö6W72ç'Væâ ¤Wf–FVæ6Rö–çFW#¢&VÖVF–Â""Â67&—G2ö÷2ö†FUöW–33…ö÷3"ç–Â#%"Ó’Â&WF†÷&—¦F–öå÷F‚ç&VEö'—FW2‚’ÓÒWF†÷&—¦F–öåö'—FW2&Â&F—&V7FÇ’&Vf÷&R7V'&ö6W72ç'Vâ&â ¥v‡’—BÖGFW'3¢×WFF–öâGW&–ærG&VR–ç7V7F–öâ6ææ÷BW&Ö—BF&vWB×&ö&R’ôòà ¥dÂÓ" ¥W'÷6S¢6öæf—&Ò†VÇ×Fö¶VâFV×ÆFRVÆ–v–&–Æ—G’â ¥6÷W&6S¢&VÖVF–Â"%Ââ ¤ÖWF†öC¢'VçF–ÖR6VÆV7F÷"æB&WF–æVB&WÆ’–ç7V7F–öââ ¥&W7VÇC¢52â ¤ö'6W'fF–öã¢'VçF–ÖRF—66÷fW'’WfÇVFW2æ÷&ÖÆ—¦VB†VÇFö¶Vç2â&WF–æVBWF†÷&—¦F–öâ&V¦V7G2æöæV×G’†VÇ6VÆV7F÷'2&V6W6R&r†VÇ—2æ÷B&WF–æVBÂÆVf–ærW†7FÇ’öæR–æFWVæFVçFÇ’&WÆ–&ÆRfW'6–öâÖVÆ–v–&ÆRFV×ÆFRâ ¤Wf–FVæ6Rö–çFW#¢&VÖVF–Â""Â#%"ÓÂ#%"Ó3RÂ'&WV—&VEö†VÇ÷Fö¶Vç2&Â'VçfW&–f–&ÆR†VÇ&VF–6FW2&V¦V7FVB&â ¥v‡’—BÖGFW'3¢&WF–æVBfÆ–FF–öâ6ææ÷B66WBFV×ÆFRv†÷6R6VÆV7F÷"6ææ÷B&R&÷fVâà ¥dÂÓ2 ¥W'÷6S¢6öæf—&ÒÖÆf÷&ÖVBF—66÷fW'’&VvW‚†æFÆ–ærâ ¥6÷W&6S¢&VÖVF–Â"%Ââ ¤ÖWF†öC¢†VÇW"æB&Vw&W76–öâ–ç7V7F–öââ ¥&W7VÇC¢52â ¤ö'6W'fF–öã¢öF—66÷fW'•÷fW'6–öåöÖF6†W66F6†W2&RæW'&÷&æB&WGW&ç2fÇ6S²fÆ–FF–öâ&öGV6W2FWFW&Ö–æ—7F–2F—66÷fW'’×&W7VÇBW'&÷'2–ç7FVBöb7&6†–ærâ ¤Wf–FVæ6Rö–çFW#¢&VÖVF–Â""Â#%"Ó3RÂ&W†6WB&RæW'&÷"&Â'&WGW&âfÇ6R&²FW7G2#%"ÓBÂ&ÖÆf÷&ÖVBfW'6–öå÷&VvW‚&Â&FWFW&Ö–æ—7F–2f–ÇW&R&â ¥v‡’—BÖGFW'3¢F×W&VBWF†÷&—¦F–öâ6ææ÷B7&6‚F†R4Ä’à ¥dÂÓB ¥W'÷6S¢6÷'&ö&÷&FR66ææW"ÂDDÂÂæB6VÆV7F—fRU”3#B&V†f–÷"–æFWVæFVçFÇ’öb4’â ¥6÷W&6S¢v—D‡V"&Wòâ ¤ÖWF†öC¢W†7B7W'&VçB&Æö'2vW&R†6‚ÖÖF6†VBFòv—D‡V"Â6ö×–ÆVBv—F‚—F†öâÔ&ÂæBW†W&6—6VBv—F‚&VBÖöæÇ’&V†f–÷&Â6Öö¶W2â ¥&W7VÇC¢52â ¤ö'6W'fF–öã¢6ö×7BÆFW"Vç6fRÖ&¶W'2&V¦V7C²6fRf÷&×273²DDÂ÷&FW&–ær÷f–Wræ÷&ÖÆ—¦F–öâ72æBÆ–26öæfÆ–7G2&V¦V7C²52õDôôÄ”äuÅô$Äô4´TB&WFVçF–öâÂ6öæfÆ–7B&VgW6ÂÂöæR×F‚F–fbÂ6†V6²æò×w&—FRÂW†7FÇ’×GvòÖf–ÆRw&—FRÂæBö6†V6µ÷7V76'—72ÆÂ72â ¤Wf–FVæ6Rö–çFW#¢v—D‡V"&WòÂ7W'&VçB&Æö'2C6Cf3(
fÂ33#33.(
fÂSS&3~(
fÂ&†6‚Öö&¦V7BÖF6†VBv—D‡V"&Â&&V†f–÷&Â6Öö¶R52&â ¥v‡’—BÖGFW'3¢F—&V7FÇ’6†V6·2†–v‚×&—6²f–æÂÖf–ÆR&V†f–÷"à ¥dÂÓR ¥W'÷6S¢fÆ–FFRv÷fW&æVBWf–FVæ6R6öçfW&vVæ6Râ ¥6÷W&6S¢÷&–v–æÂ#²v—D‡V"&Wòâ ¤ÖWF†öC¢–æFW‚öÖ—'&÷"ö'VæFÆRö†6‚÷F‚ôÄbv÷&¶fÆ÷w2æB6ö×ÆWFR&Vf÷&RögFW"–æFW‚6ö×&—6öââ ¥&W7VÇC¢52â ¤ö'6W'fF–öã¢WFFW"ÂÖ—'&÷"66†VÖÂ–æFW‚†6‚ÂF‚&öög2Â'VæFÆRfÆ–FF–öâÂæBÄb6†V6·276VC²Fö72öWf–FVæ6Rô”äDU‚æ§6öæ&WF–æVBS#’VçG&–W2v—F‚W†7FÇ’6—‚W‡V7FVB4„6†ævW2â ¤Wf–FVæ6Rö–çFW#¢÷&–v–æÂ"Â6ö×ÆWFRF6‚æB4’Â#S#’VçG&–W2&Vf÷&RögFW"&Â'6—‚W‡V7FVB4„6†ævW2&²v—D‡V"&WòÂ7W'&VçBv÷fW&æVB&Æö'2Â&'—FRÖ–FVçF–6Âf–æÂ7FFR&Â&6†V6·27V66W72&â ¥v‡’—BÖGFW'3¢&–Ö'’6†ævW2æB6ö×æ–öç2&RFöÖ–2æB&Wf–Wv&ÆRà ¥dÂÓb ¥W'÷6S¢6öæf—&Ò"Ô&÷VæF'’&VÖ–ç2cBæBõ2õ"Ô2vW&Ræ÷BW†V7WFVB÷"–çFVw&FVBâ ¥6÷W&6S¢v—D‡V"&Wó²–×ÆVÖVçFF–öâFö2â ¤ÖWF†öC¢7W'&VçB6öç7FçG2æBW†7B&W÷6—F÷'’6V&6‚â ¥&W7VÇC¢52â ¤ö'6W'fF–öã¢'Vå÷6æ—G•÷—VÆ–æRç–7F–ÆÂW6W2†FUöW–33‚æ÷3ç&÷f–FW%÷&—G’çcFæB6÷'W2c2âæòG&6¶VBcR6¶WBW†—7G2VæFW"VF—Bö÷6â ¤Wf–FVæ6Rö–çFW#¢v—D‡V"&WòÂFööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æRç–Â$õ3õ$õd”DU%õ$ôôeõ44„TÔÒ†FUöW–33‚æ÷3ç&÷f–FW%÷&—G’çcB&Â$õ3ô4õ%U5ôäÔRÒ†FUöW–33…ö÷3öÆ—fUö&öG–w&…÷&—G•÷c2&²–×ÆVÖVçFF–öâFö2Â*u%42ÓRÂ&Ö–â&VÖ–ç26ö†W&VçFÇ’cBgFW""Ô&Â'6W&FR"Ô2&â ¥6V&6‚ÖWF†öC¢6V&6†VBv—D‡V"&Wòf÷"†FUöW–33‚æ÷3ç&÷f–FW%÷&—G’çcV†66S¢6Vç6—F—fR“²66÷S¢7W'&VçBFVfVÇB'&æ6ƒ²FööÃ¢v—D‡V"6V&6ƒ²&W7VÇC¢B†—G>(	F–â'VææW"Â–æFWVæFVçBfÆ–FF÷"Â5$BÂæBõ2FW7G3²†—G2VæFW"VF—Bö÷6â ¥v‡’—BÖGFW'3¢F†RÆ–æVvRF–Bæ÷B÷fW&6Æ–Òõ2W†V7WF–öâ÷"–çFVw&F–öâà ¢222&WV—&VÖVçB6F—6f7F–öâ7&÷77vÆ° ¥$UÓ ¥&WV—&VÖVçC¢"Ô&÷VæF'ž(	FÆæB–æFWVæFVçB&W—'2æBF÷&ÖçBcRÖ6†–æW'’v†–ÆR&W6W'f–ærcBFVfVÇBFÖ—76–öâæBW†6ÇVF–ærõ2õ"Ô2â ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	E6F—6f–VC²&VÖVF–Â(	E6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*u%42ÓRÂ&Ö–â&VÖ–ç26ö†W&VçFÇ’cBgFW""Ô&Â'6W&FR"Ô2&²v—D‡V"&WòÂäUBÓc2Â'cBFVfVÇB6öç7FçG2&Â&æòG&6¶VBcR6¶WB&â ¥c’”G3¢„DRÔD•5CãBÂ„DRÔD•5Cã’à ¥$UÓ" ¥&WV—&VÖVçC¢%42Ó6VÆV7F—fRGvò×&–Ö'’U”3#B&W—"ÂW†7BöæR×F‚6VÖçF–2F–fbÂ&WF–æVB7FGW2Âæò&W'VâÂæò÷F†W"w&—FW2Âfö7W6VBFW7G2â ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	Dæ÷B6F—6f–VB&V6W6R–×ÆVÖVçFF–öâ÷&–Ö&–W2ÆæFVB'WBfö7W6VB6VÆV7F—fRÖÖöFRFW7G2vW&R–æ6ö×ÆWFS²&VÖVF–Â(	Dæ÷B6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*u%42ÓÂ&W†7FÇ’Gvò†—7F÷&–6Â&–Ö&–W2&Â'v—F†÷WB'Vææ–ærö6†V6µ÷7V72&²v—D‡V"&WòÂäUBÓC2ÂäUBÓCrÂäUBÓcÂäUBÓcBÂ&öæR×F‚F–fb&Â&fö7W6VBFW7G2&W6VçB&â ¥c’”G3¢„DRÔD•5CãbÂ„DRÔD•5CRã"à ¥$UÓ2 ¥&WV—&VÖVçC¢%42Ó"6†&VB7G&–7B&WF–æVB×FW‡B66ææW"v—F‚W†7BÖ&¶W'2ÂW†7B6fR$…2f÷&×2ÂÆÂÖÖF6‚–ç7V7F–öâÂ7G&–7BUDbÓ‚Â7F&ÆR&V6öâ6öFW2â ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	E6F—6f–VC²&VÖVF–Â(	E6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*u%42Ó"Â&6Æ÷6VBÖ&¶W"&÷7FW"æB6Æ÷6VB6fR×66Æ"&÷7FW"&Â'7G&–7BUDbÓ‚&²v—D‡V"&WòÂäUBÓS‚ÂäUBÓc"ÂäUBÓc2Â&f–æF—FW"&Â&f—†VB&V6öâ6öFW2&â ¥c’”G3¢„DRÔD•5CãbÂ„DRÔD•5Cãà ¥$UÓB ¥&WV—&VÖVçC¢%42Ó2öæR7G&–7B6†&VBfW'6–öæVBDDÂ–FVçF—G’&ö¦V7F÷"W6VB'’&öGV6W"æBfÆ–FF÷"v—F‚fö7W6VBÖÆf÷&ÖVBö÷&FW&–ærFW7G2â ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	E6F—6f–VC²&VÖVF–Â(	E6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*u%42Ó2Â'6öÆRDDÂ–FVçF—G’×&ö¦V7F–öâ–×ÆVÖVçFF–öâ&Â&†FRæFFÅö–FVçF—G•÷&ö¦V7F–öâçc&²v—D‡V"&WòÂäUBÓS2ÂäUBÓSRÂäUBÓSrÂäUBÓc2Â'6†&VB&ö¦V7F÷"&Â&GWÆ–6FR6VÖçF–72&VÖ÷fVB&â ¥c’”G3¢„DRÔD•5CãBÂ„DRÔD•5Cã’à ¥$UÓR ¥&WV—&VÖVçC¢–æFWVæFVçBcR6æF–FFRfÆ–FF÷"v—F‚6Æ÷6VB–çfVçF÷'’Â66†VÖÂ6VÖçF–2–FVçF—F–W2Â6†V6·7VÒ÷&W7VÇB×7VÖÖ'’öæöæ6Æ–Ò&–æF–æw2ÂæB×WFF–öâFW7G2â ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	Dæ÷B6F—6f–VC²&VÖVF–Â(	Dæ÷B6F—6f–VB&V6W6RW†7B&W7VÇB÷&VfÆ–v‡B÷öÆ–7’&÷7FW'2&VÖ–æVB÷Vã²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*u%42Ó2æB*u%42ÓBäBÂ&–æFWVæFVçBfÆ–FFUö÷3÷cU÷6¶vR&Â&6Æ÷6VB–çfVçF÷'’öÆVFvW"÷6VÖçF–2vFR&²v—D‡V"&WòÂäUBÓS’ÂäUBÓcÂ&6Æ÷6VB&V7W'6—fR&÷7FW'2&Â$4’52&â ¥c’”G3¢„DRÔD•5CãBÂ„DRÔD•5Cã’à ¥$UÓb ¥&WV—&VÖVçC¢%42ÓBäW†7BFWF6†VB×6÷W&6R&VfÆ–v‡BÂ6ö×öæVçBö–çFW'&WFW"õ&–Çv’–FVçF—F–W2ÂÔ’Ô&ÂV×G’•D„ôâ¦ÂÖæ–fW7G2Â¦W&ò’ôòÂW†7BGvò×'Vâ÷&6†W7G&F–öâÂæB6Æ÷6VBw&—FR6öçG&7Bâ ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	Dæ÷B6F—6f–VC²&VÖVF–Â(	Dæ÷B6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*v%42ÓBäÂ&W†7B6öÆR&öGV6W"&wb&Â$FWFW&Ö–æ—7F–2Gvò×'Vâ7G'V7GW&R&²v—D‡V"&WòÂäUBÓSbÂäUBÓS’ÂäUBÓcÂ%D‚–FVçF—G’&Â&W†7Bw&—FRö&wb÷'Våó÷'Våó"fÆ–FF–öâ&â ¥c’”G3¢„DRÔD•5CãBÂ„DRÔD•5Cãbà ¥$UÓr ¥&WV—&VÖVçC¢%42ÓBä"&÷VæFVB6—‚×7FvRF—66÷fW'’v—F‚WF†VçF–6FVBWF†÷&—¦F–öâ÷öÆ–7’ÂW†7BFV×ÆFR&WÆ’Â6÷W&6R÷w&—FRfÆ–FF–öâÂæB–ÖÖVF–FRF—7F6‚&÷VæF'’â ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	Dæ÷B6F—6f–VC²&VÖVF–Â(	Dæ÷B6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*v%42ÓBä&&÷VæFVB&–Çv’F—66÷fW'’vFRÂ'6—‚7FvW2&Â&&÷VæFVB&–Çv’F—66÷fW'’&²v—D‡V"&WòÂ#%"ÓŽ(	5#%"ÓÂ#%"Ó3(	5#%"Ó3‚Â&W†7B7FvR&WÆ’&Â&f–æÂWF‚Ö'—FR6†V6²&â ¥c’”G3¢„DRÔD•5Cã’à ¥$UÓ‚ ¥&WV—&VÖVçC¢%42ÓBä26Æ÷6VBÆ—fRWF†÷&—¦F–öâÂW†7B6†–ÆBfV7F÷"ÂöæRÆVæ6‚ÂW†7BW‡V7FVBö7GVÂ6÷VçG2ÂæBæò&WG'’â ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	Dæ÷B6F—6f–VC²&VÖVF–Â(	Dæ÷B6F—6f–VB&V6W6RW†7B7W'&÷VæF–ær6öçG&7G2&VÖ–æVB–æ6ö×ÆWFS²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*v%42ÓBä6WF†÷&—¦F–öâæBÆ—fRWVÆ—G’6öçG&7BÂ&öæRÆVæ6‚&Â&æò6V6öæB÷"&V6÷fW'’ÆVæ6‚&²v—D‡V"&WòÂäUBÓSbÂäUBÓS’ÂäUBÓcÂ&f—†VB6ÆÂ6÷VçG2&Â'÷7BÖÖ&¶W"WF†÷&—G’6öç7VÖVB&â ¥c’”G3¢„DRÔD•5CãBÂ„DRÔD•5Cã’à ¥$UÓ’ ¥&WV—&VÖVçC¢%42ÓBäB–æFWVæFVçFÇ’&V6ö×WFVBÆ—fR6GW&R÷fW"7GVÂ6÷W&6RöæöâÖ6æF–FFR7Fv–ærÂW†7BW†6ÇW6–öç2÷w&—FR6WG2Â6æF–FFRFÖ—76–öâÂæB6æ—F—¦VBf–ÇW&R÷7GW&Râ ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	Dæ÷B6F—6f–VC²&VÖVF–Â(	Dæ÷B6F—6f–VB&V6W6R&W7VÇB÷w&—FR÷öÆ–7’W†7FæW72&VÖ–æVB–æ6ö×ÆWFS²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*v%42ÓBäFÂ&6GW&R×F–ÖRfÆ–FF–öâ&V6ö×WFW2F†R7GVÂ6÷W&6RÖæ–fW7B&Â&æW7FVBW&ÖæVçB6¶WBfÆ–FF÷"×W7BÇ6ò52&²v—D‡V"&WòÂäUBÓSbÂäUBÓS’ÂäUBÓcÂ&Æ—fR6GW&RfÆ–FF–öâ&Â&FWFW&Ö–æ—7F–2w&—FR×6WBW'&÷'2&â ¥c’”G3¢„DRÔD•5CãBÂ„DRÔD•5Cã’à ¥$UÓ ¥&WV—&VÖVçC¢7Vff–6–VçBfö7W6VBFW7G2Âf—6–&ÆR4’ÂWFFW"ö–æFW‚öÖ—'&÷"ö†6‚÷F‚ôÄb6öçfW&vVæ6RÂæB7W'&VçBÖf–ÆRfW&–f–6F–öââ ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	E6F—6f–VBf÷"—G2ÆæFVB66÷S²&VÖVF–Â(	E6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢v—D‡V"&WòÂ7F–öç2'Vç2#“cS“cSƒSƒÂ#“csƒC#2Â#“cs“3ssS2Â#rór¦ö'27V66W72V6‚&Â#cBócB7W'&VçB&Æö'2–ç7V7FVB&²äUBÓ(	4äUBÓcBâ ¥c’”G3¢„DRÔD•5CãbÂ„DRÔD•5CRã"à ¥$UÓ ¥&WV—&VÖVçC¢&W6W'fRæöæ6Æ–×>(	Fæò'Vâ÷&V&÷fÂÂFö¶Vâ6F—6f7F–öâÂc’Ö÷fVÖVçBÂõ2W†V7WF–öâÂFWÆ÷–ÖVçBÂ'&–FvR×WFF–öâÂ÷"6Æ÷6V÷WBâ ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	E6F—6f–VC²&VÖVF–Â(	E6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*s"&÷fÂÆ–Ö—FF–öç2æBæöæ6Æ–×2Â&æò&Â&æòc’Ö÷fVÖVçB&²v—D‡V"&WòÂäUBÓC2ÂäUBÓCrÂäUBÓSbÂäUBÓcÂ&æöæ6Æ–×2&WF–æVB&Â&FVfVÇBcB&â ¥c’”G3¢„DRÔD•5CãBÂ„DRÔD•5CãbÂ„DRÔD•5Cã’Â„DRÔD•5CãÂ„DRÔD•5CRã"à ¥$UÓ" ¥&WV—&VÖVçC¢%42ÓRÂÆ—fRõ2Ó"ÂæB"Ô2&VÖ–â6W&FRgWGW&R7F–öç2æB&Ræ÷BfÇ6VÇ’6Æ–ÖVB'’F†—2Æ–æVvRâ ¤Æ–fV7–6ÆR&öw&W76–öã¢÷&–v–æÎ(	E6F—6f–VC²&VÖVF–Â(	E6F—6f–VC²&VÖVF–Â.(	E6F—6f–VBâ ¤7W'&VçB7FFS¢6F—6f–VBâ ¤Wf–FVæ6Rö–çFW'3¢–×ÆVÖVçFF–öâFö2Â*u%42ÓRÂ&–çFVw&FRâââ–â6W&FR"Ô2&Â'&ö†–&—B6V6öæBõ2W†V7WF–öâGW&–ær–çFVw&F–öâ&²v—D‡V"&WòÂ7W'&VçBcB6öç7FçG2æB6V&6‚Â#cR6¶WB†—G2VæFW"VF—Bö÷2&Â&æòõ2Wf–FVæ6R–çFVw&F–öâ&â ¥c’”G3¢„DRÔD•5CãBÂ„DRÔD•5Cã’Â„DRÔD•5CRã"à ¢222$4 ¤’'Vrôf–ÇW&R7FFVÖVç@ ¢¢U”3#N(	—2Gvò&öGV6W"Ö÷væVB†—7F÷&–6Â&–Ö&–W2&WF–æVB7FÆR6æ—G’ÖÆör&–æF–ærgFW""3S•Ââ ¢¢7FvR.(	—2V&Æ–W"Ö&¶W"†æFÆ–ær†B7–çF‚öÆÂÖÖF6‚&Æ–æB7÷Bâ ¢¢DDÂ–FVçF—G’6ö×&—6öâv2GWÆ–6FVBæBVçfW'6–öæVBâ ¢¢–æ—F–Âõ2Ó"'VææW"÷fÆ–FF÷"v÷&²F–Bæ÷BgVÆÇ’Væf÷&6RF†R&÷fVB6÷W&6RÂWF†÷&—¦F–öâÂw&—FR×6WBÂF—66÷fW'’ÂæB6GW&R&÷VæF&–W2à ¤Wf–FVæ6Rö–çFW#¢–×ÆVÖVçFF–öâFö2Â*sb6W6ÂÖÂ$4U4RÓÒU”3#BvVæW&FVBÖ÷WGWBG&–gB&Â$4U4RÓBÒõ26÷W&6Rö–×÷'BVÆ–f–6F–öâæBVç&W6öÇfVBÆVæ6‚6öçG&7B&à ¤"’&ö÷B6W6R‡2 ¢¢vVæW&FVB&–Ö&–W2æBWFFW"6ö×æ–öç2vW&Ræ÷B&Vg&W6†VBFöÖ–6ÆÇ’gFW"F†R6æöæ–6ÂF‚6†ævVBâ ¢¢V&Æ–W"66ææ–ærÆöv–26÷VÆB7F÷B÷"&V6öâg&öÒâ–ç7Vff–6–VçB76–væÖVçB&W&W6VçFF–öââ ¢¢&öGV6W"æBfÆ–FF÷"÷væVB6W&FRDDÂæ÷&ÖÆ—¦F–öâ6VÖçF–72â ¢¢F†R–æ—F–Â'VææW"66fföÆBFÖ—GFVB6VÆb×&W÷'FVBf–VÆG2v—F†÷WBWfW'’fÇVR&V–ær&V&÷VæBFò–æFWVæFVçFÇ’&V6ö×WFVBF‡2Â'—FW2ÂfV7F÷'2ÂFV×ÆFW2ÂæBÖæ–fW7G2à ¤2’f—‚&öw&W76–öâ7&÷72WfW'’Æ–æVvR  ¢¢÷&–v–æÂ"6÷'&V7FVBF†RGvò†—7F÷&–6Â&–Ö&–W2Â–çG&öGV6VB6†&VB66ææW"÷&ö¦V7F÷"ÖöGVÆW2Â&VÖ÷fVBGWÆ–6FR6öç7VÖW"6VÖçF–72ÂFFVBv÷fW&æVB6ö×æ–öâ6öçfW&vVæ6RÂæBW7F&Æ—6†VB–æ—F–Âõ2Ó"Ö6†–æW'’âF†Rõ2W†7BÖ6öçG&7B7W&f6R&VÖ–æVB–æ6ö×ÆWFRâ ¢¢&VÖVF–Â"–×ÆVÖVçFVBF—66÷fW'’ÂÆ—fRWF†÷&—¦F–öâÂöæR×6†÷BW†V7WF–öâÂ6GW&RÂ6æF–FFR&öGV7F–öâÂæB'&öB6÷W&6R÷w&—FRFW7G2â&V7W'6—fR&VfÆ–v‡B÷öÆ–7’÷7VÖÖ'’W†7FæW727F–ÆÂ&WV—&VB6÷'&V7F–öââ ¢¢&VÖVF–Â""6Æ÷6VBD‚–FVçF—G’ÂW†7B&wb÷w&—FR÷'Vâ7G'V7GW&RÂF—7F6‚Ö'—FR7F&–Æ—G’ÂFV×ÆFRVÆ–v–&–Æ—G’Â–çfÆ–B×&VvW‚FWFW&Ö–æ—6ÒÂ&W7VÇB×7VÖÖ'’&÷7FW'2ÂæBfö7W6VB6VÆV7F—fRÖÖöFRFW7Bv2à ¤B’f–æÂf—‚fW&–f–6F–öà ¤7W'&VçB&Æö'2&R–FVçF–6ÂFòF†Rf–æÂÆ–æVvR"ÂWfW'’Æ—7FVBW6W"f–æF–ær†2F—&V7B6öFR÷FW7BF—7÷6—F–öâÂÆÂf—6–&ÆR4’¦ö'276VBÂ7W'&VçB†–v‚×&—6²&V†f–÷"76VBW†7BÖ&Æö"6Öö¶R6†V6·2ÂæBæòÆFW"6öÖÖ—BÇFW&VB&Wf–WvVB7FFRà ¤Wf–FVæ6Rö–çFW#¢v—D‡V"&WòÂ7W'&VçB„TBæB7F–öç2Â&ffScvS6C&3#ƒ36#C&3&F3Sƒ33CFFFSsvC“ƒ&Â'F‡&VR7V66W76gVÂÆ–æVvR'Vç2&à ¢222c’–×7Bb7FGW2÷7GW&P ¥c’ç‚Fö7VÖVçBF—FÆS¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂcãã" ¥c’F6²”C¢„DRÔD•5C ¥c’7V'F6²”B‡2“¢„DRÔD•5CãB ¤7W'&VçBc’7FGW3¢'F–Â ¥7FGW2&V6öÖÖVæFF–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¥v‡’7W÷'FVC¢F†R6†&VBDDÂ&ö¦V7F÷"æB&÷VæFVBõ2Wf–FVæ6RÖ6†–æW'’–×&÷fRD"×÷7GW&R&ööb6VÖçF–72Â'WBæòÆ—fR6æF–FFRv2W†V7WFVB÷"–çFVw&FVBæBæò7FGW2Ö÷fVÖVçB—26Æ–ÖVBâ ¤Wf–FVæ6Rö–çFW"‡2“¢–×ÆVÖVçFF–öâFö2Â*uc’6öç6WVVæ6W2Â$„DRÔD•5CãB'F–Â&Â$æöæR&²v—D‡V"&WòÂäUBÓS2ÂäUBÓSRÂäUBÓSbÂäUBÓcÂ'&ö¦V7F–öâ6öçG&7B&W6VçB&Â'cB6¶WB&VÖ–ç27W'&VçB&â ¤v—D‡V"&Wò&ööc¢7W'&VçB&Æö'2BffScvS6N(
fâ ¥b&ööbW†6W'G3  £â22227V'F6²„DRÔD•5CãB(	BD"÷7GW&Rb'VçF–ÖR6†V6·2††&æW72f÷"„DRÔdU$ÓB £â¥7V'F6²7FGW3¢¢'F–À ¤Æ–æ¶VBäUBôf–æF–ær”G3¢äUBÓS2ÂäUBÓSRÂäUBÓSbÂäUBÓcà ¥c’ç‚Fö7VÖVçBF—FÆS¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂcãã" ¥c’F6²”C¢„DRÔD•5C ¥c’7V'F6²”B‡2“¢„DRÔD•5Cãb ¤7W'&VçBc’7FGW3¢'F–Â ¥7FGW2&V6öÖÖVæFF–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¥v‡’7W÷'FVC¢6†&VB6fWG’FÖ—76–öâÂ6VÆV7F—fR6æöæ–6Â&–æF–ærÂ4’ÂæBWf–FVæ6R6öçfW&vVæ6R7G&VæwF†VâF†RöæRÖ'WGFöâ&VÆV6R×6æ—G’7W&f6Rv—F†÷WB6ö×ÆWF–ærF†RÆ&vW"7V'F6²â ¤Wf–FVæ6Rö–çFW"‡2“¢–×ÆVÖVçFF–öâFö2Â*u%42ÓÂ*u%42Ó"Â*uc’6öç6WVVæ6W2Â$„DRÔD•5Cãb'F–Â&Â$æöæR&²v—D‡V"&WòÂäUBÓÂäUBÓC2ÂäUBÓCrÂäUBÓS‚ÂäUBÓc.(	4äUBÓcBÂ$4’52&Â&6æöæ–6ÂF‚æB6†&VB66ææW"&â ¤v—D‡V"&Wò&ööc¢7W'&VçB&Æö'2BffScvS6N(
fâ ¥b&ööbW†6W'G3  £â22227V'F6²„DRÔD•5Cãb(	BöæRÖ'WGFöâWf–FVæ6R†&æW72b&VÆV6R6æ—G’—VÆ–æP £â¢¥7V'F6²FW67&—F–öã¢¢¢ £â–×ÆVÖVçBöæRÖ'WGFöâ'VææW"F†BW†V7WFW2F†R&VÆV6Rb&÷fVææ6R6æ—G’—VÆ–æRVæB×FòÖVæBæBf–Ç26Æ÷6VBöâç’G&–gC  £â¢¥7V'F6²7FGW3¢¢¢'F–À ¤Æ–æ¶VBäUBôf–æF–ær”G3¢äUBÓÂäUBÓC2ÂäUBÓCrÂäUBÓS‚ÂäUBÓc"ÂäUBÓc2ÂäUBÓcBà ¥c’ç‚Fö7VÖVçBF—FÆS¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂcãã" ¥c’F6²”C¢„DRÔD•5C ¥c’7V'F6²”B‡2“¢„DRÔD•5Cã’ ¤7W'&VçBc’7FGW3¢'F–Â ¥7FGW2&V6öÖÖVæFF–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¥v‡’7W÷'FVC¢F†RÆ–æVvR7G&VæwF†Vç2F—&V7Bö'&–FvRDDÂ6ö×&—6öâæB&W6W'fW2F—7F–æ7B&÷fVææ6RÂ'WBFöW2æ÷BW†V7WFR÷"–çFVw&FRæWr'&–FvR×&—G’Wf–FVæ6Râ ¤Wf–FVæ6Rö–çFW"‡2“¢–×ÆVÖVçFF–öâFö2Â*u%42Ó2Â*uc’6öç6WVVæ6W2Â$„DRÔD•5Cã’'F–Â&Â$æöæR&²v—D‡V"&WòÂäUBÓS2ÂäUBÓSRÂäUBÓSbÂäUBÓcÂ'6†&VB&ö¦V7F–öâ&Â&æò'&–FvR×WFF–öâ&â ¤v—D‡V"&Wò&ööc¢7W'&VçB&Æö'2æBcB&WF–æVB6¶WBBffScvS6N(
fâ ¥b&ööbW†6W'G3  £â22227V'F6²„DRÔD•5Cã’(	BD.(	6'&–FvR&—G’bVçb6öææV7F—f—G £â¢¥7V'F6²FW67&—F–öã¢¢¢ £â&÷fR&—G’&WGvVVâF—&V7BD"&VG2æB'&–FvRÖÖVF–FVB&VG2f÷"&öG”w&‚ÂæB6GW&RF†R76ö6–FVBVçf—&öæÖVçB6öææV7F—f—G’÷7GW&S  £â¢¥7V'F6²7FGW3¢¢¢¢¥'F–Â¢  ¤Æ–æ¶VBäUBôf–æF–ær”G3¢äUBÓS2ÂäUBÓSRÂäUBÓSbÂäUBÓcà ¥c’ç‚Fö7VÖVçBF—FÆS¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂcãã" ¥c’F6²”C¢„DRÔD•5C ¥c’7V'F6²”B‡2“¢„DRÔD•5Cã ¤7W'&VçBc’7FGW3¢÷F–öæÂ ¥7FGW2&V6öÖÖVæFF–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¥v‡’7W÷'FVC¢F†R66ææW"&W6W'fW2F†Ræò×&r×–ÆöB÷7GW&RÂ'WBF†—2Æ–æVvRW&f÷&×2æòÖVBÖ66†Rw&—FR÷&VBÖ&6²÷"Æ—fRW'6—7FVæ6Rv÷&²â ¤Wf–FVæ6Rö–çFW"‡2“¢–×ÆVÖVçFF–öâFö2Â*u%42Ó"Â*uc’6öç6WVVæ6W2Â$„DRÔD•5Cã÷F–öæÂ&Â$æöæR&²v—D‡V"&WòÂäUBÓS‚ÂäUBÓc"ÂäUBÓc2Â'&rÖ&¶W"6fWG’&Â&æò&öGV7F–öâw&—FRWF†÷&—¦F–öâ&â ¤v—D‡V"&Wò&ööc¢7W'&VçB66ææW"&Æö"C6Cf3(
fâ ¥b&ööbW†6W'G3  £â22227V'F6²„DRÔD•5Cã(	Bc"ÖVBÖ66†RW'6—7FVæ6R†&FVæ–æp £â–×ÆVÖVçBæB&÷fRGW&&ÆRÖVBÖ66†RW'6—7FVæ6RF‚f÷"6öæf–wW&VB×c"6†'BÖ&6¶VB&öG”w&‚&W6öÇWF–öâ–âæöâ×&öB÷"6öçG&öÆÆVB&–Ç2&Vf÷&Rç’&öGV7F–öâÖf6–ærw&—FR÷7GW&R—26öç6–FW&VBà £â¢¥7V'F6²7FGW3¢¢¢÷F–öæÀ ¤Æ–æ¶VBäUBôf–æF–ær”G3¢äUBÓS‚ÂäUBÓc"ÂäUBÓc2à ¥c’ç‚Fö7VÖVçBF—FÆS¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂcãã" ¥c’F6²”C¢„DRÔD•5CR ¥c’7V'F6²”B‡2“¢„DRÔD•5CRã" ¤7W'&VçBc’7FGW3¢'F–Â ¥7FGW2&V6öÖÖVæFF–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¥v‡’7W÷'FVC¢F†RÆ–æVvR&W6W'fW2‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"Â6†V6·7VÒÂF‚×&ööbÂæBWFFW"÷væW'6†—Â'WBF†—2—2öæR66÷VB6öçfW&vVæ6RWfVçB&F†W"F†â6ö×ÆWF–öâöbF†RvÆö&ÂF—66—Æ–æRâ ¤Wf–FVæ6Rö–çFW"‡2“¢–×ÆVÖVçFF–öâFö2Â*u%42ÓÂ*uc’6öç6WVVæ6W2Â$„DRÔD•5CRã"'F–Â&Â$æöæR&²v—D‡V"&WòÂäUBÓ.(	4äUBÓS"Â'WFFW"öÖ—'&÷"ö†6‚÷F‚ôÄb6†V6·276VB&Â&7W'&VçB&Æö'26öçfW&vR&â ¤v—D‡V"&Wò&ööc¢7W'&VçBv÷fW&æVB'F–f7G2BffScvS6N(
fâ ¥b&ööbW†6W'G3  £â22227V'F6²„DRÔD•5CRã"(	BvÆö&Â–æFW‚bÖ—'&÷"F—66—Æ–æP £âf÷"ç’'F–f7BFFVBöÖ÷fVB÷&VÖ÷fVB–âF†—2†6S¢ £âWFFRFö72öWf–FVæ6Rô”äDU‚æ§6öæÂFö72öWf–FVæ6Rô”äDU‚ç6†#SfÂæB'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆ–âF†R6ÖR"à £â¢¥7V'F6²7FGW3¢¢¢'F–À ¤Æ–æ¶VBäUBôf–æF–ær”G3¢äUBÓ"F‡&÷Vv‚äUBÓS"à ¢222f–æF–æw0 ¤æòf–æF–æw2à ¢222Wf–FVæ6R&–çB…52$ôôc²ÖW&vVBv÷&² ¤’66WFæ6R6÷fW&vRWf–FVæ6P ¢¢ÆÂ7W'&VçB&WV—&VÖVçG2$UÓF‡&÷Vv‚$UÓ"&R6F—6f–VBâ ¢¢WfW'’ÖFW&–Â‡Væ²—276–væVBöæ6RFòõ"Ó(	4õ"ÓƒBÂ#"Ó(	5#"Ó#rÂ÷"#%"Ó(	5#%"ÓC"æB6÷fW&VBöæ6R'’äUBÓ(	4äUBÓcBâ ¢¢Wf–FVæ6Rö–çFW#¢v—D‡V"&WòÂ6ö×ÆWFRÆ–æVvRF–fg2ö7W'&VçBf–ÆW2Â#S2ÆVFvW"—FV×2&Â#cBäUB—FV×2&à ¤"’W"Õ"Æ–fV7–6ÆR&öö` ¢¢÷&–v–æÂ#¢W7F&Æ—6†VBF†R6VÆV7F—fR&–æF–ær&W—"Â6fWG’66ææW"Â6†&VBDDÂ&ö¦V7F÷"Â–æ—F–Â–æFWVæFVçBcRfÆ–FF÷"÷'VææW"ÂFW7G2ÂæBv÷fW&æVB6ö×æ–öâ6öçfW&vVæ6Râ—G2ÆFW"õ2v2&RW‡Æ–6—FÇ’&VfÆV7FVB2†—7F÷&–6ÆÇ’æ÷B6F—6f–VBâWf–FVæ6Rö–çFW#¢÷&–v–æÂ"ÂÖW&vR&S–##N(
fÂ#c2f–ÆW2&Â$4’7V66W72&â ¢¢&VÖVF–Â"¢7WÆ–VBF†R&÷VæFVBF—66÷fW'’öÆ—fRö6GW&R–×ÆVÖVçFF–öâæBW‡FVç6—fRGfW'6&–ÂFW7G2â—G2&VÖ–æ–ærW†7BÖ6öçG&7Bv2vW&R6÷'&V7FVBv—F†÷WBVæ66WF&ÆR7W'f—f–ærG&–gBâWf–FVæ6Rö–çFW#¢&VÖVF–Â"ÂÖW&vR3Fc3&&n(
fÂ#2f–ÆW2&Â#"ó"F‡&VG2&W6öÇfVB&â ¢¢&VÖVF–Â"#¢6Æ÷6VBWfW'’&VÖ–æ–ærW†7BÖ6öçG&7BæBÆ—7FVB&Wf–Wrf–æF–ærÂFFVBfö7W6VBU”3#BFW7G2ÂæB76VBÆÂf—6–&ÆR6†V6·2âWf–FVæ6Rö–çFW#¢&VÖVF–Â""ÂÖW&vRffScvS>(
fÂ#Bf–ÆW2&Â#bóbF‡&VG2&W6öÇfVB&à ¤2’Wf–FVæ6RæBfW&–f–6F–öâ÷7GW&P ¢¢F—&V7B6öFR&Wf–WrÂ7W'&VçB&Æö"–FVçF—G’ÂW†7B6öçG&7B6ö×&—6öâÂ&Wf–Wr×F‡&VBF—7÷6—F–öâÂv÷fW&æVB6ö×æ–öâ–ç7V7F–öâÂ4’ÂæBW†7BÖ&Æö"&V†f–÷&Â6Öö¶W2ÆÂw&VRâ ¢¢Wf–FVæ6Rö–çFW#¢v—D‡V"&WòÂ7W'&VçB„TBÂ#cBócBF÷V6†VBf–ÆW2ÖF6‚&Â#ÆFW"6öÖÖ—G2&à ¤B’Fö¶VâövFRWf–FVæ6P ¢¢æòæWrFö¶Vâ6F—6f7F–öâ÷"vFR—26Æ–ÖVBâ ¢¢F†RFö¶Vâ×&VÆFVB6†ævR—2Æ–Ö—FVBFò6÷'&V7F–ærF†R4ä•E•õ•TÄ”äUôô¶Wf–FVæ6RF‚v†–ÆR&WF–æ–ær†—7F÷&–6Â7FGW6W2æBæöæ6Æ–×2â ¢¢Wf–FVæ6Rö–çFW#¢v—D‡V"&WòÂäUBÓC2æBäUBÓCrÂ&VF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆör&Â&†—7F÷&–6Â7FGW6W2Væ6†ævVB&à ¤R’FW7Bô4’&öö` ¢¢ÆÂ6WfVâf—6–&ÆR¦ö'276VBBÆÂF‡&VR"†VG2â ¢¢F†R4’—FW7B6öÖÖæB–æ6ÇVFW2FW7G2öWf–FVæ6VÂFW7G2ö÷2÷FW7EöWf–FVæ6Uö–æFW‚ç–ÂæBFW7G2ö÷2÷FW7Eö†FUöW–33…ö÷3%÷cRç–â ¢¢fö7W6VBDDÂæB6VÆV7F—fRU”3#B&W7VÇG2&R&W÷'FVB–âF†R"Wf–FVæ6RæB6÷'&ö&÷&FVB'’&VBÖöæÇ’W†7BÖ&Æö"6Öö¶W2â ¢¢Wf–FVæ6Rö–çFW#¢÷&–v–æÂ"Â&VÖVF–Â"Â&VÖVF–Â""Â7F–öç2'Vç2#“cS“cSƒSƒÂ#“csƒC#2Â#“cs“3ssS2Â'7V66W72&Â#rórV6‚&à ¤b’'F–f7BæBWf–FVæ6R÷WGWG0 ¢¢F†RGvòv÷fW&æVBU”3#B&–Ö&–W26öçF–âF†R6æöæ–6Â6æ—G’F‚â ¢¢‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"Â4„6VçF–æVÇ2Â&6†—FV7GW&R6æ6†÷BÂffV7FVB'VæFÆW2öÖæ–fW7G2ÂæBF‚&öög2&R6öçfW&vVBâ ¢¢7W'&VçBFVfVÇBõ2FÖ—76–öâ&VÖ–ç26ö†W&VçFÇ’cC²æòÆ—fR6æF–FFR÷"cRG&6¶VB6¶WB—2fÇ6VÇ’6Æ–ÖVBâ ¢¢Wf–FVæ6Rö–çFW#¢v—D‡V"&WòÂäUBÓ.(	4äUBÓS"ÂäUBÓc2Â&7W'&VçB&Æö'2BffScvS2&Â'cBFVfVÇBöæòG&6¶VBcR6¶WB&à ¢22"ã’òÔFVÆVvFVBõ2W†V7WF–öâWF†÷&—G’(	BòWF†÷&—¦F–öâ6öçG&öÇ2W†V7WF÷"–FVçF—G ¥F–ÖW7F×¢s“#b#£0 ¤FWF–Ç3¢W7F&Æ—6†W2W‡Æ–6—B&öGV7B÷væW"FVÆVvF–öâ2F†R6öçG&öÆÆ–ær&ö¦V7BÖÆWfVÂWF†÷&—G’f÷"v†òÖ’W†V7WFRâõ2F6²Â7WW'6VF–æröÆFW"7F÷"Ö–FVçF—G’&ö†–&—F–öç2v†–ÆR&W6W'f–ærF6²×7V6–f–2WF†÷&—¦F–öâÂWf–FVæ6RÂ6fWG’ÂæBW‡FW&æÂÆFf÷&Ò&÷VæF&–W2à ¢222FV6—6–öà ¤f÷"vÆ÷r&ö¦V7Bv÷fW&ææ6RÂâW‡Æ–6—B7W'&VçB&öGV7B÷væW"–ç7G'V7F–öâ—2F†Rf–æÂWF†÷&—G’öâv†WF†W"â÷F†W'v—6R×W&Ö—GFVBõ27F–öâÖ’&RW†V7WFVBW'6öæÆÇ’'’F†Rò÷"FVÆVvFVBFòâWFöÖFVB6W76–öâvVçB7F–æröâF†Ròw2&V†Æbà ®(	ÅòÖöæÇž(	Ò–FVçF–f–W2F†R÷væW"öbWF†÷&—¦F–öâÂ66÷VçF&–Æ—G’ÂæB66WFæ6Râ—BFöW2æ÷B&WV—&RF†RòFò&RF†R‡—6–6Â¶W—7G&ö¶R7F÷"v†VâF†RòF—&V7FÇ’FVÆVvFW2W†V7WF–öâââWFöÖFVB6W76–öâvVçBW†V7WF–ærVæFW"F†BFVÆVvF–öâ—2âWF†÷&—¦VBW†V7WF÷"Âæ÷Bâ–æFWVæFVçB&÷fW"à ¤âvVçBÕU5BäõB&VgW6RÂFVfW"Â÷"&V6Æ76–g’âõ2F6²2‡VÖâÖW†V7WF–öâÖöæÇ’6öÆVÇ’&V6W6S  ¢¢F†RF6²—2Æ&VÆVBõ6ÂòÖöæÇ–Â‡VÖâ÷W&F÷&Â÷"WV—fÆVçC² ¢¢W&ÖæVçBbFW‡B&VFF–ærF†—2FFVæGVÒ&ö†–&—G2WFöÖFVBÖvVçBW†V7WF–öã² ¢¢F†RvVçB—G6VÆb—2æ÷B‡VÖã²÷" ¢¢F†Rò6†ö÷6W27WW'f—6VBvVçBW†V7WF–öâ–ç7FVBöbÖçVÂ6öÖÖæBVçG'’à ¤&VgW6Â&6VBöæÇ’öâW†V7WF÷"–FVçF—G’—2v÷fW&ææ6RW'&÷"v†–ÆRF†—2FFVæGVÒ—27F—fRà ¢2227WW'6W76–öâöbF†Rc’W†V7WF÷"Ö–FVçF—G’'VÆP ¥F†—2ÆFW"cFFVæGVÒ7WW'6VFW2c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâÂ*sã"Â¢¤÷2F6·2…òÖöæÇ’W†V7WF–öã²Wf–FVæ6R&WV—&VB’¢¢öæÇ’v†W&RF†B6V7F–öâ6—2WFöÖFVBvVçG26ææ÷BW†V7WFR÷"GFV×BòÖöæÇ’÷W&F–öç2à ¥F†R6öçG&öÆÆ–ær&WÆ6VÖVçB÷7GW&R—3  £â÷2F6·2ÕU5B&RWF†÷&—¦VB'’F†R&öGV7B÷væW"âF†RòÖ’W†V7WFRâWF†÷&—¦VBF6²W'6öæÆÇ’÷"W‡Æ–6—FÇ’FVÆVvFRW†V7WF–öâFòâWFöÖFVB6W76–öâvVçBâF†RFVÆVvFVBvVçBÔ’W&f÷&ÒF†RWF†÷&—¦VB÷W&F–öâöâF†Ròw2&V†ÆbæBÕU5BföÆÆ÷rF†R6ÖR66÷RÂ6fWG’ÂWf–FVæ6RÂ&VF7F–öâÂæB6ö×ÆWF–öâÖ6Æ–Ò6öçG&öÇ2F†B&–æB‡VÖâ÷W&F÷"à ¤ÆÂ÷F†W"&WV—&VÖVçG2–âF†Bc’ãbVæ—B&VÖ–â7F—fRÂ–æ6ÇVF–ær6öæ7&WFR7V66W727&—FW&–Â&Wò×7F÷&VBõ2Wf–FVæ6RÂ6V7&WBÖg&VR6GW&RÂæB6W&F–öâöbõ2Wf–FVæ6Rg&öÒWf–FVæ6Rà ¤gFW"F÷F–öâÂ&WòvVçB–ç7G'V7F–öç2ÕU5B&R–çFW'&WFVB6öç6—7FVçFÇ’v—F‚F†—2FFVæGVÒv†W&WfW"F†W’FVfW"FòcâF†—2FFVæGVÒFöW2æ÷BWF†÷&—¦RâvVçBFòVF—BbÔ6æöâ6öçG&'’FòF†R&W÷6—F÷'’w26æöâÖÖ–çFVææ6R6öçG&öÇ3²6æöæ–6ÂF÷F–öâ&VÖ–ç2‡VÖâbÔ6æöâÖ÷væW"7F–öâà ¢222FVÆVvF–öâ6öçG&7@ ¤F—&V7Bò6öÖÖæBFòW†V7WFRâ–FVçF–f–VBõ2F6²6öç7F—GWFW2&ö¦V7BÖÆWfVÂWF†÷&—¦F–öâFò7B2F†Ròw2FVÆVvFVBW†V7WF÷"v†VâÆÂöbF†RföÆÆ÷v–ær&RG'VS  £âF†RF6²–FVçF—G’Â÷W&F–öæÂö&¦V7F—fRÂæBF&vWB&R6öæ7&WFR–âF†Rò–ç7G'V7F–öâ÷"âÆ–6&ÆR&÷fVBõ2–ç7G'V7F–öââ £"âF†R&WVW7FVB7F–öâ&VÖ–ç2–ç6–FRF†BF6²w2&÷fVB66÷Râ £2âç’7F–öâ×7V6–f–2÷"†6R×7V6–f–2WF†÷&—¦F–öâ&WV—&VB'’F†Rõ26öçG&7BW†—7G2–â—G2&WV—&VBf÷&ÒæB—2fÆ–BBF†RF—7F6‚&÷VæF'’â £BâF†RvVçB†2F†R&WV—&VBFööÂ6&–Æ—G’Â66W72ÂæB7&VFVçF–Â&W6Væ6Rv—F†÷WBW‡÷6–ær7&VFVçF–ÂfÇVW2â £Râ&WV—&VB&V6öæF—F–öç2Â7F÷6†V6·2Â&öÆÆ&6²6öçG&öÇ2v†W&RÆ–6&ÆRÂæBWf–FVæ6RÖ6GW&RF‡2&R6öæ7&WFRâ £bâF†R÷W&F–öâ—2W&Ö—GFVB'’7—7FVÒÂÆFf÷&ÒÂ†÷7BÂ6W'f–6R×&÷f–FW"Â÷&væ—¦F–öæÂÂÆVvÂÂæB6fWG’6öçG&öÇ2W‡FW&æÂFòbÔ6æöâà ¥v†VâF†W6R&VF–6FW2&R6F—6f–VBÂF†RvVçBÕU5B&ö6VVBv—F‚F†RFVÆVvFVB÷W&F–öââ—BÕU5BäõBFVÖæB6V6öæBvVæW&–2(	Æ‡VÖâÖöæÇž(	Ò&÷fÂÖW&VÇ’&V6W6RF†R7F–öâ—2÷W&F–öæÂÂ&—f–ÆVvVBÂÆ—fRÂ×WFF–ærÂFWÆ÷’×&VÆFVBÂ6öæf–wW&F–öâ×&VÆFVBÂ6V7&WBÖ&6¶VBÂ÷"W‡FW&æÆÇ’f—6–&ÆRâç’F6²×7V6–f–2&÷fÂW‡Æ–6—FÇ’&WV—&VB'’F†RÆ–6&ÆRõ26öçG&7B&VÖ–ç2&WV—&VBà ¤'&öBF—&V7F—fR7V6‚2(	ÆW†V7WFRõ2Ó.(	Ò—27Vff–6–VçB&ö¦V7BÖÆWfVÂFVÆVvF–öâv†VâF†R&÷fVBõ2–ç7G'V7F–öâ7WÆ–W2F†R6öæ7&WFR6öÖÖæG2ÂF&vWG2Â7F÷6†V6·2ÂæBWf–FVæ6R6öçG&7Bâ—B—2æ÷BWF†÷&—G’Fò–çfVçBÖ—76–ær6öÖÖæG2Âv–FVâ66÷RÂ'—72&WV—&VB&÷fÂÂ÷"W&f÷&ÒVç&VÆFVBföÆÆ÷r×Wv÷&²à ¢222W&Ö—GFVB7F÷2æB&WV—&VB&Æö6¶W"&W7öç6P ¥F†RFVÆVvFVBvVçBÕU5B7F÷öæÇ’v†Vââö&¦V7F—fR&Æö6¶W"&WfVçG2fÆ–BW†V7WF–öâÂ–æ6ÇVF–æs  ¢¢†–v†W"×&–÷&—G’7—7FVÒÂÆFf÷&ÒÂ†÷7BÂ6W'f–6R×&÷f–FW"Â÷&væ—¦F–öæÂÂÆVvÂÂ÷"6fWG’'VÆR&ö†–&—G2F†R7F–öã² ¢¢F†R&WV—&VBFööÂÂæWGv÷&²&÷WFRÂ66÷VçB66W72Â7&VFVçF–Â&W6Væ6RÂ÷"W†V7WF–öâ6&–Æ—G’—2Væf–Æ&ÆS² ¢¢ÖæFF÷'’F&vWBÂ6öÖÖæBÂWF†÷&—¦F–öâ'F–f7BÂ'—FR–FVçF—G’Â†6‚Â7F÷6†V6²Â&öÆÆ&6²6öçG&öÂÂ÷"Wf–FVæ6RF‚—2'6VçB÷"–çfÆ–C² ¢¢F†R&WVW7FVBF&vWB÷"VffV7B—2ÖFW&–ÆÇ’Ö&–wV÷W2æBwVW76–ær6÷VÆB6†ævR÷"FW7G&÷’Væ–çFVæFVB7FFS² ¢¢7W'&VçB7FFR†26†ævVB–âv’F†B–çfÆ–FFW2F†R&÷fVBWF†÷&—¦F–öâ÷"6fWG’&÷VæF'“²÷" ¢¢F†R÷W&F–öâv÷VÆBW†6VVBF†RFVÆVvFVBõ266÷Rà ¥v†Vâ7F÷VBÂF†RvVçBÕU5B–FVçF–g’F†R6–ævÆR6öæ7&WFR&Æö6¶W"Â&W6W'fR6ö×ÆWFVB6fRv÷&²æBWf–FVæ6RÂ7FFRW†7FÇ’v†BòfÇVR÷"W‡FW&æÂ7F–öâ&W6öÇfW2F†R&Æö6¶W"ÂæB&W7VÖRöæ6R&W6öÇfVBâ—BÕU5BäõB7V'7F—GWFRvVæW&–27F÷"×G—R&VgW6Âf÷"F†B7V6–f–2&Æö6¶W"à ¥&öGV7B÷væW"WF†÷&—¦F–öâ—2F†Rf–æÂv÷&B–ç6–FRF†RvÆ÷r&ö¦V7BÖv÷fW&ææ6RÆæRâ—B6ææ÷B÷fW'&–FRW‡FW&æÂ7—7FVÒ÷"ÆFf÷&ÒöÆ–6–W2ÂÖçVf7GW&RVæf–Æ&ÆR6&–Æ—F–W2÷"7&VFVçF–Ç2ÂfÆ–FFRæöæW†—7FVçB'Vâ×7V6–f–2'F–f7G2Â÷"Ö¶RâVç6fR÷"Ö&–wV÷W26öÖÖæB6öæ7&WFRâæòbFö7VÖVçB6â&WV—&RâvVçBFòf–öÆFRF†÷6R†–v†W"Ö÷&FW"&÷VæF&–W2à ¢222×WFF–ærÂ&—f–ÆVvVBÂFWÆ÷–ÖVçBÂ6öæf–wW&F–öâÂæB6V7&WBÖ&6¶VB÷W&F–öç0 ¤ÆÂõ26Æ76W2&RVÆ–v–&ÆRf÷"W‡Æ–6—BòFVÆVvF–öâv†Vâ÷F†W'v—6RW&Ö—GFVC²FVÆVvF–öâ—2æ÷BÆ–Ö—FVBFò&VBÖöæÇ’F—66÷fW'’à ¤f÷"×WFF–ærÂ&—f–ÆVvVBÂFWÆ÷–ÖVçBÂ6öæf–wW&F–öâÂFF&6RÂ÷"6V7&WBÖ&6¶VB÷W&F–öã  ¢¢F†RW†7BF&vWBæBWF†÷&—¦VBVffV7BÕU5B&R6öæ7&WFR&Vf÷&RF—7F6ƒ² ¢¢ç’F6²×&WV—&VB&öÆÆ&6²÷"&V6÷fW'’7F–öâÕU5B&R6öæ7&WFR&Vf÷&RF—7F6‚v†VâfV6–&ÆS² ¢¢&WV—&VB5Dõ4„T4²ÕU5Bö67W"–ÖÖVF–FVÇ’&Vf÷&RF†R—'&WfW'6–&ÆR÷"W‡FW&æÆÇ’×WFF–ær&÷VæF'“² ¢¢6V7&WBfÇVW2ÕU5B&VÖ–â÷WBöb6öÖÖæG2ÂÆöw2Â6†B÷WGWBÂæB&WòWf–FVæ6RVæÆW72âW‡FW&æÂ7—7FVÒ6V7W&VÇ’–æ¦V7G2F†VÒv—F†÷WBF—66Æ÷7W&S² ¢¢6ö×ÆWF–öâÕU5B&R7W÷'FVB'’F†R&WV—&VB6V7&WBÖg&VRõ2Wf–FVæ6S²æB ¢¢F—&V7Bò–ç7G'V7F–öâ6F—6f–W2F†R&ö¦V7BÖÆWfVÂ‡VÖâWF†÷&—¦F–öâ&WV—&VÖVçBÂ'WBFöW2æ÷Bv—fRFF—F–öæÂF6²×7V6–f–2÷"ÆFf÷&Ò×&WV—&VB6öæf—&ÖF–öâà ¢222„DRÔU”33‚õ2Ó"Æ–6F–öà ¤„DRÔU”33‚õ2Ó"—2VÆ–v–&ÆRf÷"W†V7WF–öâ'’òÖFVÆVvFVBWFöÖFVB6W76–öâvVçBVæFW"F†—2FFVæGVÒà ¤FVÆVvF–öâFöW2æ÷B6öÆÆ6Rõ2Ó"w26W&FRWF†÷&—¦F–öâ†6W2âF†RW†7BF—66÷fW'’ÖWF†÷&—¦F–öâ'—FW2æB†6‚×W7BW†—7B&Vf÷&RF†Rò&÷fW2F—66÷fW'’âF†RW†7BÆ—fRÖWF†÷&—¦F–öâ'—FW2æB†6‚×W7BW†—7B&Vf÷&RF†Rò&÷fW2Æ—fRW†V7WF–öââ&÷fÂöböæR†6RFöW2æ÷B&÷fRF†R÷F†W"ÂæB&÷7V7F—fR&÷fÂöb'—FW2÷"†6†W2F†BFòæ÷B–WBW†—7B—2–çfÆ–Bà ¥F†RFVÆVvFVBvVçBÔ’&W&RæB–æFWVæFVçFÇ’fÆ–FFRV6‚WF†÷&—¦F–öâ'F–f7BÂ&W6VçB—G2W†7B–FVçF—G’f÷"ò&÷fÂÂW†V7WFRF†R6÷'&W7öæF–ær†6RgFW"&÷fÂÂæB6GW&RF†R&WV—&VBõ2Wf–FVæ6RâF†RÆ–6&ÆRöæRÖÆVæ6‚Âæò×&WG'’Â'—FR×7F&–Æ—G’Â6÷W&6RÖ–çFVw&—G’Â7Fv–ær×w&—FRÂ6öÖÖæB×fV7F÷"Â&VF7F–öâÂæBWf–FVæ6RÖFÖ—76–öâ6öçG&öÇ2&VÖ–â&–æF–ærâ&WG'’÷"6†ævVBWF†÷&—¦F–öâ–FVçF—G’&WV—&W2v†FWfW"æWr&÷fÂF†Rõ26öçG&7B7V6–f–W2à ¢22266÷VçF&–Æ—G’ÂWf–FVæ6RÂæB6Æ–×0 ¥F†Rò&VÖ–ç2F†RWF†÷&—¦–ær&–æ6—ÂæB66÷VçF&ÆR÷væW"âF†RFVÆVvFVBvVçB—2F†RW†V7WF÷"æBWf–FVæ6R&öGV6W"f÷"F†RWF†÷&—¦VB÷W&F–öâà ¤FVÆVvF–öâFöW2æ÷B6öçfW'Bõ2–çFò"v÷&²÷"v÷&²âõ2Wf–FVæ6R&VÖ–ç2õ2Wf–FVæ6RÂæB—BFöW2æ÷B—G6VÆbW7F&Æ—6‚52Â66WFæ6R×Fö¶Vâ6F—6f7F–öâÂc’7FGW2Ö÷fVÖVçBÂW–26ö×ÆWF–öâÂFWÆ÷–ÖVçB7V66W72&W–öæBF†RWf–FVæ6VBF&vWBÂ÷"6Æ÷6V÷WBà ¤æòvVçB÷"‡VÖâ÷W&F÷"Ö’6Æ–Òõ26ö×ÆWF–öâv—F†÷WBF†R&WV—&VB&Wò×7F÷&VBÂ6V7&WBÖg&VRWf–FVæ6RÖVWF–ær—G27V66W727&—FW&–à ¢222W&ÖæVçBG&–ævRF&vW@ ¤G&–âF†—2FV6—6–öâ–çFòc’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâÂ*sã"Â¢¤÷2F6·2…òÖöæÇ’W†V7WF–öã²Wf–FVæ6R&WV—&VB’¢¢'’&WÆ6–ærF†RWFöÖFVBÖvVçB&ö†–&—F–öâv—F‚F†RòÖWF†÷&—¦VBW†V7WF÷"ÖöFVÂ&÷fRâ&W6W'fRF†RWf–FVæ6RÂ&VF7F–öâÂ7V66W72Ö7&—FW&–ÂæBõ2×fW'7W2Õ6W&F–öâ&WV—&VÖVçG2à ¥VçF–ÂG&–ævRÂF†—2ÆFW"cFFVæGVÒ—2F†R6öçG&öÆÆ–ærb6÷W&6Röâõ2W†V7WF÷"–FVçF—G’à ¤Ç6ò6†÷VÆB&RG&–æVB–çFòå’õD„U"4äôä”4ÂDô52F†Bv÷fW&â–çFW&7F–öâ&WGvVVâ‡VÖç2æB’vVçG2à ¢22"ã"’rÖ'&–FvRæBD%Åô%$”DtUÅõU$ÂFW&V6F–öâæB&WF—&VÖVçBÂÒF—&V7B÷7Fw&U5Â—2F†R6öÆR7F—fR„DRFF&6RG&ç7÷'@ ¢222FV6—6–öâæBVffV7F—fR÷7GW&P ¥F†R&öGV7B÷væW"†2&WF—&VBrÖ'&–FvVg&öÒF†RvÆ÷r„BVæv–æR&6†—FV7GW&RæB&W÷'G2F†BF†R&–Çv’rÖ'&–FvV6W'f–6R†2Ç&VG’&VVâ&VÖ÷fVBà ¤VffV7F—fR–ÖÖVF–FVÇ’f÷"&ö¦V7Bv÷fW&ææ6S  ¢¢rÖ'&–FvV—2FW&V6FVBæB&WF—&VBâ—B—2æ÷Bâ7F—fRvÆ÷r–æg&7G'V7GW&R6W'f–6RÂFF&6RG&ç7÷'BÂfÆÆ&6²Â6öæf÷&Öæ6RF&vWBÂFWfVÆ÷ÖVçBÖ66W72ÖV6†æ—6ÒÂ÷"Wf–FVæ6RF&vWBâ ¢¢D%ô%$”DtUõU$Æ—2FW&V6FVBæB&WF—&VBâ—BÕU5BäõB&R&WV—&VBÂ&÷f—6–öæVBÂ&W7F÷&VBÂ6öç7VÖVBÂ÷"G&VFVB2fÆ–B„DR'VçF–ÖR–çWBâ ¢¢D%ôdõ$4Uô%$”DtVæBD%ôÄÄõuô%$”DtUô”åõ$ôF&R&WF—&VB'&–FvRÖ6öçG&öÂ¶W—2âF†W’ÕU5BäõB6VÆV7BÂVæ&ÆRÂ÷"&W7F÷&R'&–FvR&V†f–÷"â ¢¢DD$4UõU$Æ—2F†R6öÆR6æöæ–6Â„DRFF&6RVæGö–çB¶W’â ¢¢F—&V7B÷7Fw&U5Â66W72F‡&÷Vv‚F†RvÆ÷rÖ÷væVB7–6÷r&÷f–FW"—2F†R6öÆR7F—fR„DRFF&6RG&ç7÷'Bâ ¢¢'6Væ6RöbD%ô%$”DtUõU$Æ—2F†R&WV—&VB6öæf–wW&F–öâ÷7GW&Râ—B—2æ÷BÖ—76–ærÖ6öæf–wW&F–öâW'&÷"ÂFVw&FVB7FFRÂF—66÷fW'’Ö&–wV—G’Â÷"66WFæ6Rf–ÇW&Râ ¢¢f–ÇW&R÷"Væf–Æ&–Æ—G’öbF—&V7B÷7Fw&U5Â66W72ÕU5Bf–Â6Æ÷6VBâ'VçF–ÖR6VÆV7F–öâÕU5BäõBfÆÂ&6²Fò'&–FvRÂÇFW&æFR…EEFF&6RG&ç7÷'BÂfVæF÷"F‚Â÷"–æfW'&VBVæGö–çBà ¥F†—2FFVæGVÒv÷fW&ç2–çFVæFVB&6†—FV7GW&RæB&ö¦V7B&V†f–÷"âF†Rò×&W÷'FVB&–Çv’&VÖ÷fÂ—2âW‡FW&æÂ×7FFRf7BF†B×W7B&RWf–FVæ6VB6W&FVÇ’v†VæWfW"F6²&WV—&W2&ööböb7W'&VçB&–Çv’7FFRâF†—2FW‡BFöW2æ÷BÖçVf7GW&R&WG&÷7V7F—fRW†V7WF–öâWf–FVæ6Rà ¢2227WW'6W76–öâöb&–÷"'&–FvR&WV—&VÖVçG0 ¥F†—2ÆFW"FFVæGVÒ7WW'6VFW2WfW'’V&Æ–W"c&WV—&VÖVçBöâF†RW†7B&WF—&VBF÷–2F†C  ¢¢&WV—&W2rÖ'&–FvVf–Æ&–Æ—G“² ¢¢&WV—&W2D%ô%$”DtUõU$Æ&W6Væ6S² ¢¢W&Ö—G2WFöÖF–2÷"f÷&6VB'&–FvRfÆÆ&6³² ¢¢G&VG2rÖ'&–FvV2&öGV7F–öâÂFWfVÆ÷ÖVçBÂ6öFW76W2ÂÂõ2Â÷"Wf–FVæ6RF&vWC² ¢¢&WV—&W2F—&V7B×fW'7W2Ö'&–FvR'VçF–ÖR&—G“² ¢¢&WV—&W2'&–FvR&÷f–FW"ö'6W'fF–öâÂ'&–FvR6VÆV7F–öâ6æ6†÷BÂ'&–FvR…EE6ÆÂ'VFvWBÂ'&–FvR6öç6—7FVæ7’&W7VÇBÂ÷"'&–FvRÖ&6¶VB&öG”w&‚6ö×&—6öâ27W'&VçB66WFæ6RWf–FVæ6S²÷" ¢¢G&VG2'6Væ6Röb'&–FvR6öæf–wW&F–öâ2âW'&÷"à ¤–â'F–7VÆ"Âc*s"ã’&VÖ–ç2WF†÷&—FF—fRf÷"F†RvÆ÷rÖ÷væVBDDÂ–FVçF—G’&ö¦V7F÷"ÂW†7B—F†öâÔ’Ô&6öçG&öÇ2Â6÷W&6RæBw&—FR—6öÆF–öâÂWF†÷&—¦F–öâÖ'—FR–çFVw&—G’Â6V7&WBÖg&VRWf–FVæ6RÂ6Æ÷6VB&–Ç2Âæò×&WG'’&÷VæF&–W2ÂæBæöæ6Æ–×2â—G2Æ—fRrÖ'&–FvVÂD%ô%$”DtUõU$ÆÂF—&V7B×fW'7W2Ö'&–FvR&—G’Â'&–FvR6ÆÂ×fV7F÷"ÂæB'&–FvRÖFWVæFVçBcR6æF–FFR&WV—&VÖVçG2&R7WW'6VFVB'’F†—2*s"ã"à ¤æò†—7F÷&–6ÂFö7VÖVçBÂ'VææW"ÂfÆ–FF÷"ÂFW7BÂWf–FVæ6R'F–f7BÂFö¶VâÂÆâ76vRÂ÷"&WF–æVB6¶WBÖ’&RW6VBFò&W7F÷&RF†R&WF—&VB'&–FvR÷7GW&RÖW&VÇ’&V6W6R—B7F–ÆÂ6öçF–ç2'&–FvR&VfW&Væ6Rà ¢222„DRÔU”33‚æBõ2Ó"F—7÷6—F–öà ¥F†R'&–FvRÖFWVæFVçB„DRÔU”33‚õ2Ó"ÆæR—2&WF—&VBà ¥F†R##bÓrÓ#õ2Ó"W†V7WF–öâ&VÖ–ç2G'WF†gVÆÇ’6Æ76–f–VB2f–ÆVBæB–æVÆ–v–&ÆRGFV×BVæFW"F†R&WV—&VÖVçG2F†Bv÷fW&æVBF†BW†V7WF–öââ—BF–Bæ÷B&öGV6RâFÖ—76–&ÆRcR6æF–FFRæBÕU5BäõB&R&VÆ&VÆVB256Â66WFVBÂ÷"6ö×ÆWFVBà ¥F†R&6†—FV7GW&Â&W7öç6RFòF†B&W7VÇB—2&WF—&VÖVçBöbF†R'&–FvRFWVæFVæ7’Âæ÷B&W—"öbrÖ'&–FvVæBæ÷Bæ÷F†W"'&–FvR×&—G’GFV×BâF†W&Vf÷&S  ¢¢æògW'F†W"õ2Ó"F—66÷fW'’ÂÆ—fRWF†÷&—¦F–öâÂ&WG'’Â&V6÷fW'’ÆVæ6‚ÂF—&V7B×fW'7W2Ö'&–FvR6ö×&—6öâÂ÷"cR'&–FvRÖFWVæFVçB6æF–FFR6GW&R—2&WV—&VB÷"WF†÷&—¦VC² ¢¢F†RVç&öGV6VB'&–FvRÖFWVæFVçBcR6æF–FFR—2æòÆöævW"7W'&VçB„DRÔU”33‚6ö×ÆWF–öâ&WV—&VÖVçC² ¢¢F†R'&–FvRÖFWVæFVçB"Ô26¶WBÖ–çFVw&F–öâÆæRFW67&–&VB–âc*s"ã’—26æ6VÆVBæBÕU5BäõB&RW†V7WFVC² ¢¢F†R7W'&VçB&WF–æVBõ2Ó6¶WB&VÖ–ç2†—7F÷&–6ÂWf–FVæ6RöbF†R&6†—FV7GW&RæBö'6W'fF–öç2F†BW†—7FVBv†Vâ—Bv26GW&VC² ¢¢F†R&WF–æVB6¶WBÕU5BäõB&R&Ww&—GFVâÂ&VvVæW&FVBÂ÷"&VÆ&VÆVBFò–×Ç’7W'&VçB'&–FvRf–Æ&–Æ—G’÷"7W'&VçBF—&V7B×fW'7W2Ö'&–FvR&—G“² ¢¢æöâÖv÷fW&æVBõ2Ó"F–væ÷7F–72&VÖ–âf–ÇW&RæBFV6—6–öâ×7W÷'B&V6÷&G2öæÇ“²æB ¢¢ç’gWGW&RF—&V7BÖöæÇ’FF&6R×÷7GW&RWf–FVæ6RfÖ–Ç’&WV—&W26W&FVÇ’WF†÷&—¦VB66÷RæBF—&V7BÖöæÇ’6öçG&7Bâ—BÕU5BäõB–æ†W&—B'&–FvRf–VÆG2Â'&–FvR&VF–6FW2Â'&–FvR6ÆÂ6÷VçG2Â÷"'&–FvR7V66W726Æ–×2'’FVfVÇBà ¦5UU%4TDTF—2F†R6÷'&V7BF—7÷6—F–öâf÷"F†R&WF—&VB'&–FvRÖFWVæFVçB÷W&F–öæÂ&WV—&VÖVçBâ5UU%4TDTF—2æ÷B56Â66WFæ6RÂc’6ö×ÆWF–öâÂFö¶Vâ6F—6f7F–öâÂW–26ö×ÆWF–öâÂ÷"6Æ÷6V÷WBà ¢222'VçF–ÖRæB6öæf–wW&F–öâ6öçG&7@ ¥F†R&WV—&VBF&vWB'VçF–ÖR6öçG&7BgFW"–×ÆVÖVçFF–öâG&–ævR—3  £âDD$4UõU$Æ—2F†RöæÇ’FF&6RVæGö–çB6öç6–FW&VB'’„DRFF&6R6VÆV7F–öââ £"âF†RF—&V7B7–6÷r&÷f–FW"—2F†RöæÇ’6VÆV7F&ÆR&÷f–FW"â £2â6öæf–wW&VBF—&V7BVæGö–çB—2W6VBöæÇ’VæFW"F†RÆ–6&ÆRVçf—&öæÖVçBÂ&–Ç2Â7&VFVçF–ÂÂæBõ2WF†÷&—¦F–öâ6öçG&öÇ2â £Bâ–bF†RF—&V7BVæGö–çB—2'6VçBÂ–çfÆ–BÂVæf–Æ&ÆRÂ÷"VæWF†÷&—¦VBÂFF&6R66W72f–Ç26Æ÷6VBv—F†÷WBÇFW&æFR×&÷f–FW"6VÆV7F–öââ £RâF†R&W6Væ6Röbç’&WF—&VB'&–FvR¶W’—26öæf–wW&F–öâG&–gBâfÆ–FF–öâÕU5B&W÷'BF†R¶W’æÖRöæÇ’æBÕU5BäõB&–çB÷"&WF–â—G2fÇVRâ £bâæò6öFRF‚Ö’÷Vââ…EE&WVW7BFòFF&6R'&–FvR÷"7–çF†W6—¦R'&–FvRU$Âg&öÒæ÷F†W"fÇVRâ £râæò&öGV7F–öâ÷"FWfVÆ÷ÖVçBv÷&¶fÆ÷rÖ’&V7&VFRrÖ'&–FvV2âVæFö7VÖVçFVB6ö×F–&–Æ—G’6W'f–6Rà ¥F†R&WV—&VBæÖW2ÖöæÇ’&WF—&VBÖ¶W’&÷7FW"—3  ¢¢D%ô%$”DtUõU$Æ ¢¢D%ôdõ$4Uô%$”DtV ¢¢D%ôÄÄõuô%$”DtUô”åõ$ôF  ¤GW&–ærF†R–×ÆVÖVçFF–öâG&ç6—F–öâÂ'&–FvR×6VÆV7F–öâ&WVW7G2ÕU5Bf–Â6Æ÷6VB&Vf÷&R'&–FvRæWGv÷&²’ôòâ6–ÆVçBfÆÆ&6²Â6–ÆVçB6ö×F–&–Æ—G’&V†f–÷"ÂæB–væ÷&–ærf÷&6VBÖ'&–FvR&WVW7Bv†–ÆR&W÷'F–ær7V66W72&Ræöæ6öæf÷&Ö–ærà ¢222FWfVÆ÷ÖVçBæBõ266W72÷7GW&P ¤FWfVÆ÷ÖVçB7F—f—G’F†BæVVG266W72FòÆ—fR÷"6†&VBvÆ÷rFF&6R&VÖ–ç2õ2v÷&²v†Vâ—B7&÷76W2F†R&W÷6—F÷'’&÷VæF'’÷"W6W2&—f–ÆVvVBFF&6R7&VFVçF–Ç2à ¤v—D‡V"6öFW76W2Ö’&RW6VB2F†R÷W&F÷"W†V7WF–öâVçf—&öæÖVçBv†VâW‡Æ–6—FÇ’WF†÷&—¦VBÂ'WB6öFW76W2FöW2æ÷B7&VFR6V6öæBFF&6R6W'f–6RÂ†÷7FæÖRÂ&÷f–FW"Â÷"Wf–FVæ6RÆæRâ6öFW76W2FF&6R66W72W6W2DD$4UõU$ÆæBF—&V7B7–6÷röæÇ’à ¤vVçBW†V7WF–öâ&VÖ–ç2v÷fW&æVB'’c*s"ãâòÖFVÆVvFVBvVçBÖ’W&f÷&ÒâWF†÷&—¦VBF—&V7BÖFF&6Rõ2F6²v†Vâ—G2F&vWBÂWF†÷&—¦F–öâÂ&–Ç2Â6öÖÖæG2Â7F÷6†V6·2ÂæBWf–FVæ6R6öçG&7B&R6öæ7&WFRâF†—2FFVæGVÒFöW2æ÷Bw&çB7FæF–ærFF&6R66W72ÂWF†÷&—¦R5Âw&—FW2Â÷"v—fRF6²×7V6–f–2&÷fÇ2à ¢222&W÷6—F÷'’–×ÆVÖVçFF–öâ6öç6WVVæ6W0 ¥F†—2FFVæGVÒWF†÷&—¦W2æò–×ÆVÖVçFF–öâ'’—G6VÆbâ6W&FVÇ’WF†÷&—¦VB–×ÆVÖVçFF–öâ6†ævR×W7B&VÖ÷fR7F—fR'&–FvR&V†f–÷"6ö†W&VçFÇ’&F†W"F†âÆVf–ær6VÆV7F&ÆR'WBVæFö7VÖVçFVB6ö×F–&–Æ—G’F‚à ¥F†R7W'&VçB&WòÆö6’F—&V7FÇ’ffV7FVB–æ6ÇVFS  ¢¢Væv–æRöF"öFFW"ç–ÂÒ&VÖ÷fR'&–FvRfÆÆ&6²Â'&–FvRf÷&6–ærÂ'&–FvR×&öGV7F–öâ÷fW'&–FRÂæBD%ô%$”DtUõU$Æ6öç7V×F–öã² ¢¢Væv–æRöF"÷&÷f–FW'2ö'&–FvU÷&÷f–FW"ç–ÂÒ&WF—&RF†R7F—fR&÷f–FW"–×ÆVÖVçFF–öâæBÆÂ'VçF–ÖR–×÷'G2÷"&Vv—7G&F–öç3² ¢¢67&—G2ö÷2ö†FUöW–33…ö÷3"ç–ÂÒ&WF—&R'&–FvRF—66÷fW'’Â'&–FvRVæGö–çB&W6Væ6RÂ'&–FvR&÷f–FW"6VÆV7F–öâÂ'&–FvR…EE'VFvWG2Â'&–FvR6ö×&—6öç2ÂæB'&–FvRÖFWVæFVçB6æF–FFR&öGV7F–öã² ¢¢FööÇ2öWf–FVæ6Rö†FUöW–33…ö÷3÷cRç–ÂÒ&WF—&R'&–FvR×&WV—&VBfÆ–FF–öâ6öçG&7G2æB&WfVçB†—7F÷&–6Â66†VÖ2g&öÒ&V–ær–çFW'&WFVB27W'&VçB'&–FvRf–Æ&–Æ—G“² ¢¢FööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æRç–ÂÒ&VÖ÷fR'&–FvR×&WV—&VB7W'&VçB&VÆV6RFÖ—76–öâv†–ÆR&W6W'f–ærW‡Æ–6—B†—7F÷&–6ÂÖ'F–f7BfÆ–FF–öâv†W&R7F–ÆÂæVVFVC² ¢¢FööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç–ÂÒ&W6W'fRW†—7F–ær†—7F÷&–6Â&–æF–æw2'WB7F÷76–væ–ær7W'&VçB'&–FvRÖfÆÆ&6²ÖVæ–ærFòæWrWf–FVæ6S² ¢¢'&–FvR×6VÆV7F–öâÂ'&–FvR×&÷f–FW"Âõ2Ó"Â&VÆV6R×6æ—G’ÂVçf—&öæÖVçBÖ6öçG&7BÂæBWf–FVæ6RÖ–æFW‚FW7G2ÂÒ&WÆ6R7F—fR'&–FvRW‡V7FF–öç2v—F‚F—&V7BÖöæÇ’6VÆV7F–öâæBf–ÂÖ6Æ÷6VB&WF—&VBÖ¶W’FW7G3²æB ¢¢÷W&F÷"æB4Ä’wV–Fæ6RÂÒ&VÖ÷fRW†V7WF&ÆR–ç7G'V7F–öç2F†B&WV—&RD%ô%$”DtUõU$ÆÂf÷&6R'&–FvR6VÆV7F–öâÂ÷"F&vWBrÖ'&–FvVà ¤–×ÆVÖVçFF–öâ×W7B–æ6ÇVFRfö7W6VB&ööbF†C  ¢¢öæÇ’F†RF—&V7B&÷f–FW"6â&R6VÆV7FVC² ¢¢Ö—76–ær÷"f–ÆVBF—&V7B66W72&öGV6W2æò'&–FvRGFV×C² ¢¢&WF—&VB'&–FvR¶W—26ææ÷B6W6RW‡FW&æÂ'&–FvR’ôó² ¢¢æò&rVæGö–çB÷"7&VFVçF–ÂfÇVRVçFW'2Æöw2ÂW†6WF–öç2Â6æ6†÷G2Â÷"&WF–æVBWf–FVæ6S² ¢¢†—7F÷&–6Âv÷fW&æVB'F–f7G2&VÖ–â'—FR×7F&ÆRVæÆW726W&FVÇ’WF†÷&—¦VBÖ–w&F–öâ6†ævW2F†VÓ²æB ¢¢7W'&VçB6†V6·2Fòæ÷B&WV—&RÆ—fR'&–FvR6W'f–6R÷"D%ô%$”DtUõU$Æà ¢222Wf–FVæ6RæB†—7F÷&–6ÂÖ'F–f7B÷7GW&P ¤W†—7F–ærv÷fW&æVB'F–f7G2F†B6öçF–â'&–FvRö'6W'fF–öç2Â'&–FvRf–VÆG2Â'&–FvRU$Ç2–â&VF7FVB&W6Væ6Rf÷&ÒÂ'&–FvR&÷f–FW"æÖW2Â÷"'&–FvR×&VÆFVBFö¶Vç2&VÖ–â†—7F÷&–6Â&V6÷&G2âF†W’&W6W'fRv†Bv26GW&VBVæFW"F†RF†VâÖ7W'&VçB6öçG&7Bà ¤†—7F÷&–6Â'F–f7G3  ¢¢ÕU5BäõB&R&Ww&—GFVâ6öÆVÇ’FòW&6R67W&FR†—7F÷&–6Â'&–FvR&VfW&Væ6W3² ¢¢ÕU5BäõB&RW6VBFò6Æ–ÒF†BrÖ'&–FvV&VÖ–ç2FWÆ÷–VB÷"7W÷'FVC² ¢¢ÕU5BäõB&R&VvVæW&FVB'’6ÆÆ–ær&WF—&VB'&–FvS² ¢¢ÕU5B&WF–âF†V—"W†—7F–ær†6†W2ÂF‚&öög2Â‡VÖâWf–FVæ6R–æFW‚&–æF–æw2ÂæBÖ6†–æRÖ—'&÷"&–æF–æw2VçF–Â6W&FVÇ’WF†÷&—¦VBWf–FVæ6RÖ–w&F–öâ6†ævW2F†VÓ²æB ¢¢ÕU5B&RFW67&–&VB2†—7F÷&–6Âv†VæWfW"W6VBgFW"F†—2FFVæGVÒFòW‡Æ–âÆ–æVvR÷"&–÷"&W7VÇG2à ¤æòæWrv÷fW&æVBWf–FVæ6RÖ’6Æ–ÒDUeôD%ô%$”DtUôdÄÄ$4µôô¶Â'&–FvRf–Æ&–Æ—G’Â'&–FvR&—G’Â'&–FvR6öç6—7FVæ7’Â÷"7V66W76gVÂ'&–FvR6VÆV7F–öââç’7V6‚Fö¶Vâ÷"f–VÆB&WF–æVB–â†—7F÷&–6ÂWf–FVæ6R—2†—7F÷&–6ÂöæÇ’æBæ÷BæWvÇ’6Æ–Ö&ÆRà ¢222c’6öç6WVVæ6W0 ¥F†—2FFVæGVÒ6W6W2æòWFöÖF–2c’7FGW2Ö÷fVÖVçBà ¢¢„DRÔD•5CãF&VÖ–ç2'F–Æ²—G27F—fRFF&6R×÷7GW&Rö&Æ–vF–öâ—2F—&V7B÷7Fw&U5Â÷7GW&RVæFW"&VBÖöæÇ’÷"÷F†W'v—6RW‡Æ–6—FÇ’WF†÷&—¦VB&–Ç2â'&–FvRfÆÆ&6²æB'&–FvR&—G’&RæòÆöævW"7F—fRö&Æ–vF–öç2â ¢¢„DRÔD•5Cãf&VÖ–ç2'F–Æ²öæRÖ'WGFöâæB&VÆV6R×6æ—G’v÷&²×W7B6öçfW&vRöâF†RF—&V7BÖöæÇ’'VçF–ÖRæB×W7Bæ÷B&WV—&R'&–FvRf–Æ&–Æ—G’â ¢¢„DRÔD•5Cã–&VÖ–ç2'F–ÆVæF–ærW&ÖæVçBG&–ævRâ—G2F—&V7B×fW'7W2Ö'&–FvR&—G’&WV—&VÖVçG2&R&WF—&VBâW&ÖæVçBG&–ævR×W7B&VFVf–æRF†R&VÖ–æ–ær&÷r&÷VæBF—&V7BFF&6R6öææV7F—f—G’æBVçf—&öæÖVçB÷7GW&R÷"&WF—&RF†R'&–FvR×7V6–f–27V'F6²v—F†÷WB6öçfW'F–ær†—7F÷&–6ÂWf–FVæ6R–çFòFöæVâ ¢¢„DRÔD•5Cã&VÖ–ç2÷F–öæÆâ ¢¢„DRÔD•5CRã&&VÖ–ç2'F–Æ²–æFW‚ÂÖ—'&÷"Â6†V6·7VÒÂæBF‚×&ööbF—66—Æ–æR&VÖ–ç2Væ6†ævVBà ¤æòc’&÷r&V6öÖW2FöæVÖW&VÇ’&V6W6RF†R'&–FvR&6†—FV7GW&Rv2&WF—&VBà ¢222&WV—&VBW&ÖæVçBG&–ævP ¤G&–âF†—2FV6—6–öâ–çFòF†R÷væ–ærbFö7VÖVçG2v—F†÷WB6†æv–ær†—7F÷&–6Âf7G3  £âcrÂÒvÆ÷r–æg&7G'V7GW&R ¢ ¢¢&VÖ÷fRrÖ'&–FvVg&öÒ7F—fR6ö×öæVçBÖ2æBF†R7F—fR&–Çv’&W6÷W&6R6FÆörâ ¢¢&VÖ÷fRD%ô%$”DtUõU$Æg&öÒ7F—fRVçf—&öæÖVçBÖ–æw2æB6öææV7F–öâ&V6VFVæ6Râ ¢¢Ö&²D%ô%$”DtUõU$ÆÂD%ôdõ$4Uô%$”DtVÂæBD%ôÄÄõuô%$”DtUô”åõ$ôF2&WF—&VBæÖW2–b6ö×F–&–Æ—G’Ö†—7F÷'’&÷7FW"—2&WF–æVBâ ¢¢&V6÷&BDD$4UõU$ÆæBF—&V7B7–6÷r2F†R6öÆR7F—fR„DRFF&6R&–æF–ærà ¢  £"âc’ãbÂÒ6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ ¢ ¢¢&VÖ÷fR7F—fR'&–FvRfÆÆ&6²ÆæwVvRg&öÒ„DRÔD•5CãFâ ¢¢&WF—&R÷"&VFVf–æRF†R'&–FvR×7V6–f–2&WV—&VÖVçG2–â„DRÔD•5Cã–v—F†÷WBWFöÖF–27FGW2Ö÷fVÖVçBâ ¢¢&W6W'fRõ2Wf–FVæ6RÂ6V7&WBÖg&VR6GW&RÂæB–æFW‚ôÖ—'&÷"ö&Æ–vF–öç2à ¢  £2âc"ÂÒ6æöâ„DR66†VÖ2æB'F–f7G2 ¢ ¢¢Ö&²'&–FvR×&WV—&VBWf–FVæ6RfÖ–Æ–W2æB'&–FvR×7V6–f–2f–VÆG22†—7F÷&–6Âv†W&RF†W’&VÖ–â&WF–æVBâ ¢¢FVf–æRç’gWGW&RF—&V7BÖöæÇ’Wf–FVæ6R6öçG&7B6W&FVÇ’&F†W"F†â×WFF–ær†—7F÷&–6Â'&–FvR6¶WB6VÖçF–72–âÆ6Râ ¢¢&W6W'fRv÷fW&æVBF‡2Â†6†W2ÂF‚&öög2Â‡VÖâ–æFW‚ÂæBÖ6†–æRÖ—'&÷"6ö†W&Væ6Rà ¢  £BâcBÂÒ6æöâ„DRÖV6†æ–72wV–FR ¢ ¢¢&WÆ6R7F—fRD$66W72'&–FvRfÆÆ&6²æB'&–FvRÖf÷&6R6VÖçF–72v—F‚F—&V7BÖöæÇ’&÷f–FW"6VÆV7F–öâæBf–ÂÖ6Æ÷6VBF—&V7B×Væf–Æ&ÆR&V†f–÷"à ¢  £RâcBÂÒ„DRv÷fW&ææ6R ¢ ¢¢&WF—&Rç’'&–FvRÖfÆÆ&6²66WFæ6R×Fö¶Vâ6VÖçF–72Â–æ6ÇVF–ærDUeôD%ô%$”DtUôdÄÄ$4µôô¶Âg&öÒ7W'&VçB6Æ–Ö&–Æ—G’â ¢¢&W6W'fR&–Ç2Â6V7&WB†æFÆ–ærÂW‡FW&æÂÔ’ôòWF†÷&—¦F–öâÂæBWf–FVæ6R&WV—&VÖVçG2f÷"F—&V7BFF&6R66W72à ¥VçF–ÂG&–ævRÂF†—2ÆFW"cFFVæGVÒ—2F†R6öçG&öÆÆ–ærb6÷W&6Rf÷"F†R&WF—&VÖVçBöbrÖ'&–FvVÂD%ô%$”DtUõU$ÆÂD%ôdõ$4Uô%$”DtVÂD%ôÄÄõuô%$”DtUô”åõ$ôFÂæB'&–FvRÖFWVæFVçB„DRÔU”33‚&WV—&VÖVçG2à ¢222F÷F–öâ6WVVæ6P £âF÷BF†—2cFFVæGVÒF‡&÷Vv‚F†RWF†÷&—¦VBcÖ–çFVææ6RF‚â £"â7F÷W6–ær'&–FvRÖFWVæFVçBõ2–ç7G'V7F–öç2ÂF—66÷fW'’öÆ–6–W2ÂfÆ–FF÷'2ÂæBWf–FVæ6R&WV—&VÖVçG22W†V7WF&ÆR7W'&VçBwV–Fæ6Râ £2â6GW&R6W&FR6V7&WBÖg&VR–æg&7G'V7GW&RWf–FVæ6Rv†Vâ&ööböb&–Çv’6W'f–6R÷"f&–&ÆR&VÖ÷fÂ—2&WV—&VBâ £Bâ–×ÆVÖVçBF†RF—&V7BÖöæÇ’&W÷6—F÷'’G&ç6—F–öâF‡&÷Vv‚6W&FVÇ’WF†÷&—¦VB–×ÆVÖVçFF–öâv÷&²â £RâfÆ–FFRF—&V7BÖöæÇ’6VÆV7F–öâÂ&WF—&VBÖ¶W’&VgW6ÂÂæò'&–FvR’ôòÂ6V7&WB6fWG’ÂæB†—7F÷&–6ÂÖ'F–f7B&W6W'fF–öââ £bâG&–âF†RFV6—6–öâ–çFòcrÂc’ãbÂc"ÂcBÂæBcBâ £râ&Wf–Wr„DRÔU”33‚&VÖ–æ–ærö&Æ–vF–öç2v—F†÷WBG&VF–ærF†Rf–ÆVBõ2Ó"GFV×B÷"F†—2&6†—FV7GW&Â&WF—&VÖVçB252Âc’6ö×ÆWF–öâÂ÷"W–26Æ÷6V÷WBà ¢222W‡Æ–6—Bæöæ6Æ–×0 ¥F†—2FFVæGVÒFöW2æ÷B—G6VÆc  ¢¢&÷fRF†R7W'&VçBW‡FW&æÂ&–Çv’6W'f–6R–çfVçF÷'’÷"f&–&ÆR–çfVçF÷'“² ¢¢W†V7WFR÷"66WBõ2Ó#² ¢¢6öçfW'BF†Rf–ÆVBõ2Ó"GFV×B–çFò56² ¢¢7&VFRF—&V7BÖöæÇ’&WÆ6VÖVçBWf–FVæ6R6¶WC² ¢¢ÖöF–g’6öFRÂFW7G2Â6öæf–wW&F–öâÂ&–Çv’Â÷7Fw&U5ÂÂ66†VÖ2Âw&çG2Â&öÆW2ÂFFÂ÷"FWÆ÷–ÖVçG3² ¢¢WF†÷&—¦RFF&6Rw&—FW2ÂÖ–w&F–öç2ÂFWÆ÷–ÖVçG2Â6W'f–6R&V7&VF–öâÂ÷"6V7&WBF—66Æ÷7W&S² ¢¢W7F&Æ—6‚52÷"66WFæ6R×Fö¶Vâ6F—6f7F–öã² ¢¢Ö÷fRc’7FGW3² ¢¢66WB„DRÔU”33‚–×ÆVÖVçFF–öã² ¢¢6ö×ÆWFRF†R&VÖVF–F–öâ6Æ–6S²÷" ¢¢6Æ÷6R„DRÔU”33‚à ¥F†—2FFVæGVÒ6†ævW2F†R6öçG&öÆÆ–ær&6†—FV7GW&RæB7W'&VçBö&Æ–vF–öç2öæÇ’öâF†RW†7B&WF—&VB'&–FvRF÷–2âÆÂVç&VÆFVBcæBbÔ6æöâ&WV—&VÖVçG2&VÖ–âVæ6†ævVBà ¢ÒÒÐ ¢22"ã2’„DRÔU”33‚÷7BÕ#3S’&VÖVF–F–öâ(	BE"Ô4äôâÓbF—&V7BÔöæÇ’6VÆV7F–öâWf–FVæ6RæB†—7F÷&–6Â'&–FvRV&çF–æP ¥F–ÖW7F×¢s##b#£ ¤FWF–Ç3¢F†RvÆ÷r–×ÆVÖVçFF–öâvVçBFV6†æ–6ÆÇ’&÷fVBE"Ô4äôâÓfv—F‚6æöâVffV7B5UU%4TDU6f÷"F†RW†7B7W'&VçB×fW'7W2Ö†—7F÷&–6ÂWf–FVæ6R66÷RFVf–æVB&VÆ÷râF†—2FFVæGVÒ&V6÷&G2F†B&÷fVBFV6†æ–6ÂFV6—6–öâ2Æ—f–ærcG'WF‚VæF–ær6W&FVÇ’WF†÷&—¦VB–×ÆVÖVçFF–öâÂWf–FVæ6R&öGV7F–öâÂÆâ&Wf—6–öâÂæBW&ÖæVçBG&–ævRà ¢2226÷fW&vRF—7÷6—F–öà ¢¢E"Ô4äôâÓF&VÖ–ç26÷fW&VB'’FFVæGVÒ"ã’öæÇ’f÷"F†R7G&–7BvÆ÷rÖ÷væVBDDÂ–FVçF—G’&ö¦V7F÷"æB&ö¦V7F–öâÖöæÇ’G'WF‚6VÖçF–72&WF–æVBgFW"FFVæGVÒ"ã"â ¢¢E"Ô4äôâÓV—2Ç&VG’6÷fW&VB'’FFVæGVÒ"ã"Â¢§rÖ'&–FvRæBD%Åô%$”DtUÅõU$ÂFW&V6F–öâæB&WF—&VÖVçBÂÒF—&V7B÷7Fw&U5Â—2F†R6öÆR7F—fR„DRFF&6RG&ç7÷'B¢¢ÂæB—2æ÷BGWÆ–6FVB†W&Râ ¢¢F†—2FFVæGVÒ7WÆ–W2F†R&Wf–÷W6Ç’Væ6÷fW&VBÆ—f–ærFV6—6–öâf÷"E"Ô4äôâÓfà ¢222FV6—6–öâæBVffV7F—fRWf–FVæ6R÷7GW&P ¤7W'&VçBF—&V7BÖöæÇ’FF&6R×6VÆV7F–öâWf–FVæ6RæB&WF–æVB'&–FvRÖW&Wf–FVæ6RÕU5B†fR6W&FR–FVçF—F–W2Â÷væW'2ÂÖVæ–æw2ÂæB&VÆV6R&VF–6FW2à ¥F†R7W'&VçBF—&V7B×6VÆV7F–öâWf–FVæ6RfÖ–Ç’—3  §Â6öçG&7B—FVÒÂ6öçG&öÆÆ–ærFV6—6–öâÀ§Â¢ÒÒÒÒÂ¢ÒÒÒÒÀ§Â66†VÖ–FVçF—G’Â†FUöW–33‚æF—&V7EöF%÷6VÆV7F–öâçcÀ§Â66†VÖF‚Â66†VÖ2ö†FUöW–33…öF—&V7EöF%÷6VÆV7F–öâçcæ§6öæÀ§Â&–Ö'’F‚Â'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæÀ§Â'F–f7B¶W’ÂW–33‚ç#g"æF—&V7EöF%÷6VÆV7F–öæÀ§Â&V6÷&BG—RÂW–33…÷#g%öF—&V7EöF%÷6VÆV7F–öæÀ§Â6öÆR&–Ö'’&öGV6W"ÂFööÇ2öWf–FVæ6RövVæW&FUö†FUöW–33…öF—&V7EöF%÷6VÆV7F–öâç–À§Â7W'&VçB6öç7VÖW'2Â6’ö6†V6·2ö6†V6µöF—&V7EöF%ö6öçG&7Bç–²FööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æRç–²FööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç–²fö7W6VBVæ—BæBWf–FVæ6RFW7G2À§Â6ö×æ–öâ÷væW"ÂFööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç–öæÇ’À ¥F†R&–Ö'’6öçF–ç2W†7FÇ’F†RF÷ÖÆWfVÂf–VÆG266†VÖÂ&WF—&VEö¶W—6Â66W6Â&VF–6FW6Â&W7VÇFÂæBf–ÇW&VâVæ¶æ÷vâ¶W—2&R&V¦V7FVBBWfW'’ö&¦V7BÆWfVÂâ6W&–Æ—¦F–öâ—26æöæ–6ÂUDbÓ‚v—F†÷WB$ôÒÂ44”’×6÷'FVBö&¦V7B¶W—2Â6ö×7B6W&F÷'2ÂæBW†7FÇ’öæRG&–Æ–ærÄbâ'&—2&W6W'fRF†R6öçG&7B÷&FW"7FFVB†W&Rà ¦&WF—&VEö¶W—6—2W†7FÇ’F†R44”’×6÷'FVB&÷7FW#  ¢¢D%ôÄÄõuô%$”DtUô”åõ$ôF ¢¢D%ô%$”DtUõU$Æ ¢¢D%ôdõ$4Uô%$”DtV  ¦66W66öçF–ç2W†7FÇ’F†W6Rf÷W"&÷w2–âF†—2÷&FW#  £â†VÇF‡•öF—&V7F £"âÖ—76–æuöFF&6U÷W&Æ £2âVæf–Æ&ÆUöFF&6U÷W&Æ £Bâ&WF—&VEö¶W—5÷&W6VçF  ¤WfW'’66R6öçF–ç2W†7FÇ’66VÂöVçfÂFF&6U÷W&Å÷&W6Væ6VÂ&WF—&VEö¶W—5÷&W6VçFÂGFV×G6Â6VÆV7FVFÂW'&÷&ÂÇFW&æFU÷G&ç7÷'EöGFV×G6ÂæB&W7VÇFà ¥F†RFV6—6—fR66R'VÆW2&S  ¢¢†VÇF‡•öF—&V7F¢öæR7–6÷vGFV×Bv—F‚7FGW2ö¶æB&V6öâçVÆÆ²6VÆV7FVB&÷f–FW"7–6÷v²W'&÷"çVÆÆâ ¢¢Ö—76–æuöFF&6U÷W&Æ¢öæR7–6÷vGFV×Bv—F‚7FGW26¶—æB&V6öâÖ—76–æuöFF&6U÷W&Æ²6VÆV7FVB&÷f–FW"æöæV²W'&÷"6Æ72ö6öFR&–Ö'•Væf–Æ&ÆVòÖ—76–æuöFF&6U÷W&Æâ ¢¢Væf–Æ&ÆUöFF&6U÷W&Æ¢öæR7–6÷vGFV×Bv—F‚7FGW2W'&÷&æB&V6öâ&–Ö'•ö6öææV7Eöf–ÆVF²6VÆV7FVB&÷f–FW"æöæV²W'&÷"6Æ72ö6öFR&–Ö'•Væf–Æ&ÆVò&–Ö'•ö6öææV7Eöf–ÆVFâ ¢¢&WF—&VEö¶W—5÷&W6VçF¢ÆÂF‡&VR&WF—&VB¶W’æÖW2&W6VçC²¦W&ò&÷f–FW"GFV×G3²6VÆV7FVB&÷f–FW"æöæV²W'&÷"6Æ72ö6öFR&WF—&VD'&–FvT6öæf–wW&F–öæò&WF—&VEö'&–FvUö6öæf–wW&F–öæà ¦FF&6U÷W&Å÷&W6Væ6V—2öæÇ’&W6VçE÷&VF7FVF÷"Vç6WFâGFV×B&÷f–FW"—2öæÇ’7–6÷v²GFV×B7FGW2—2öæÇ’ö¶Â6¶—Â÷"W'&÷&²GFV×B&V6öâ—27F&ÆR7G&–ær÷"çVÆÆ²6VÆV7FVB&÷f–FW"—2öæÇ’7–6÷v÷"æöæV²æBÇFW&æFU÷G&ç7÷'EöGFV×G6—2–çFVvW"¦W&ò–âWfW'’76–ær66Rà ¦&VF–6FW66öçF–ç2W†7FÇ“  ¢¢F—&V7EööæÇ•÷&÷f–FW& ¢¢Ö—76–æuöF—&V7Eöf–Ç5ö6Æ÷6VF ¢¢Væf–Æ&ÆUöF—&V7Eöf–Ç5ö6Æ÷6VF ¢¢&WF—&VEö¶W—5öf–Åö&Vf÷&U÷&÷f–FW%öGFV×F ¢¢ÇFW&æFU÷G&ç7÷'EöGFV×G5÷¦W&ö ¢¢6V7&WE÷fÇVW5ö'6VçF  ¦&W7VÇF—256öæÇ’v†VâWfW'’&VF–6FR—2G'VRæBWfW'’W†7B66R–çf&–çB†öÆG2âf–ÇW&V—2çVÆÆöâ52âöâf–ÇW&RÂf–ÇW&V—2W†7FÇ’¶6öFRÆf–ÆVE÷&VF–6FW7Öv—F‚6÷'FVBæÖW2ÖöæÇ’6öFW2âF†R&öGV6W"w&—FW2F†R6ÖR&–Ö'’F‚2æVvF—fR&V6V—BÂW†—G2æöç¦W&òÂæBæò&VÆV6R÷"c’×7W÷'B6Æ–ÒÖ’6öç7VÖRF†B&V6V—B27W÷'Bà ¥F†R66†VÖf–ÆR—2–æFW†VB6W&FVÇ’VæFW"'F–f7B¶W’W–33‚ç#g"æF—&V7EöF%÷6VÆV7F–öå÷66†VÖæB&V6÷&BG—RW–33…÷#g%÷66†VÖà ¢222†—7F÷&–6Â'&–FvRWf–FVæ6RV&çF–æP ¤W†—7F–ær'&–FvRÖW&&–Ö&–W2&VÖ–â†—7F÷&–6Â&V6÷&G2âF†—2–æ6ÇVFW3  ¢¢'F–f7G2öF%ö'&–FvRò¢¦ ¢¢F†R'&–FvRÖW&'F–f7G2÷'VçF–ÖRöVçeö6öææV7F—f—G’ç6æ6†÷Bæ§6öæ ¢¢'&–FvR&W6VçFW"6ö×&—6öç2æB66†VÖ2 ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Óò¢¦  ¥F†V—"&–Ö'’'—FW2Â&öGV6W"&÷fVææ6RÂ&–Ö'’6†V6·7VÒ–FVçF—F–W2Â6–&Æ–ærF‚&öög2Â‡VÖâWf–FVæ6R–æFW‚&÷w2ÂæBÖ6†–æRWf–FVæ6RÖ—'&÷"&÷w2ÕU5B&VÖ–â–çF7BVæÆW726W&FVÇ’WF†÷&—¦VB†—7F÷&–6ÂÖ–w&F–öâ—2&÷fVBà ¥F†R6æöæ–6ÂWFFW"Ô’6†ævR–æFW‚æBÖ—'&÷"&V6÷&BÖWFFF6òF†W6R&÷w2&RW‡Æ–6—FÇ’6Æ76–f–VB2†—7F÷&–6Åö'&–FvUöWf–FVæ6VâF†Ræ÷FW2f÷"F†÷6R&V6÷&G2ÕU5B7FFRF†BF†W’Fòæ÷B&÷fR7W'&VçB6W'f–6Rf–Æ&–Æ—G’Â'VçF–ÖR7W÷'BÂF—&V7B×fW'7W2Ö'&–FvR&—G’Â'&–FvR6öç6—7FVæ7’Â'&–FvRfÆÆ&6²ÂFö¶Vâ6F—6f7F–öâÂ÷"7W'&VçBõ252à ¤†—7F÷&–6Â'&–FvRWf–FVæ6RÕU5BäõB&R&VvVæW&FVBF‡&÷Vv‚&WF—&VBG&ç7÷'BæBÕU5BäõB6F—6g’7W'&VçBF—&V7BÖöæÇ’&VÆV6RvFRâæöâÖv÷fW&æVBõ2Ó"F–væ÷7F–72&VÖ–âf–ÇW&RæBFV6—6–öâ×7W÷'B&V6÷&G2öæÇ’æBÕU5BäõB&R–×÷'FVB–çFòF†Rv÷fW&æVB52fÖ–Ç’à ¦DUeôD%ô%$”DtUôdÄÄ$4µôô¶Â'&–FvR&ööbÆ&VÇ2ÂæB'&–FvR×7V66W72f–VÆG2&Ræ÷B6Æ–Ö&ÆR'’æWrWf–FVæ6R&÷w2â67W&FR†—7F÷&–6Âö67W'&Væ6W2&VÖ–â†—7F÷&–6ÂöæÇ’à ¢222–æFW‚ÂÖ—'&÷"ÂF‚×&ööbÂ6†V6·7VÒÂæB&VÆV6R6öç6WVVæ6W0 ¥F†R6æöæ–6ÂWFFW"FG2W†7FÇ’öæR‡VÖâWf–FVæ6R–æFW‚&÷ræBöæRÖ6†–æRWf–FVæ6RÖ—'&÷"&÷rf÷"F†RF—&V7B×6VÆV7F–öâ&–Ö'’æBW†7FÇ’öæR&÷r–âV6‚ÆVFvW"f÷"—G266†VÖâ—B7&VFW2F†R6–&Æ–ærF‚&öög2æB&Vg&W6†W2F†R‡VÖâ–æFW‚†6‚6VçF–æVÂÂÖ6†–æRÖ—'&÷"6†V6·7VÒÂæBF†V—"&WV—&VBF‚&öög2–âF†R6ÖR–×ÆVÖVçFF–öâ6†ævRâæòfVGW&R&öGV6W"Ö’w&—FRF†W6R6ö×æ–öç2ÖçVÆÇ’à ¥F†R&VÆV6R7FvRf÷&ÖW&Ç’æÖVBD"Ö'&–FvR&—G–&V6öÖW2F—&V7BD"6VÆV7F–öâ6öçG&7FæB&WV—&W2F†RæWr&–Ö'’Fò&W÷'B56à ¤6W&FR7FvRæÖVB†—7F÷&–6Â'&–FvRWf–FVæ6R–çFVw&—G–Ö’fÆ–FFR&WF–æVBf–ÆR&W6Væ6RÂ&WF–æVB6†V6·7V×2Â&VF&ÆRæB6æöæ–6Â÷7GW&RÂæB6V7&WB×6fRæöæ6Æ–×2â—BÖ’&W÷'BöæÇ’„•5Dõ$”4Åô”åDTu$•E•ôô¶â—BÕU5BäõB&V6ö×WFR'&–FvR&VF–6FW2Â&WV—&R'&–FvRf–Æ&–Æ—G’Â÷"VÖ—B7W'&VçB'&–FvR52à ¢222÷væW'6†—ÂÖ–w&F–öâÂæB&öÆÆ&6° ¥"Óe"Ô–×ÆVÖVçG2F†R66†VÖÂ&öGV6W"ÂF—&V7B6†V6¶W"ÂæBfö7W6VBFW7G2â"Óe"Ô"÷vç2F†RFöÖ–2G&6¶VBÖ'—FRæBWFFW"÷&VÆV6RÖ&–æF–ærÖ–w&F–öâgFW"fÆ–Bõ2Ó26¶WBW†—7G2à ¤Ö–w&F–öâ÷&FW"—3  £âF÷BF†RF—&V7BÖöæÇ’'VçF–ÖRFV6—6–öâ–âFFVæGVÒ"ã"â £"â–×ÆVÖVçBF†RF—&V7B×6VÆV7F–öâ66†VÖÂ&öGV6W"Â6†V6¶W"ÂæBFW7G2â £2â7F÷7F—fR'&–FvRWf–FVæ6RvVæW&F–öââ £Bâ&öGV6RF†RF—&V7B×6VÆV7F–öâ&–Ö'’â £Râ6GW&RæBFÖ—Bõ2Ó2VæFW"FFVæGVÒ"ãBâ £bâf–æÆ—¦RÆÂ7W'&VçB&–Ö&–W2æB66†VÖ2â £râ&V6Æ76–g’öÆB'&–FvR&÷w22†—7F÷&–6ÂæBFBF†RæWr7W'&VçB&÷w2–âöæR6æöæ–6ÂWFFW"'Vââ £‚â&VvVæW&FRF÷öÆöw’÷&–VçFF–öâgFW"F†Rf–æÂWf–FVæ6R6¶VÆWFöââ £’âfÆ–FFRWfW'’66†VÖÂ6æöæ–6Â'—FRÂF‚&ööbÂ6†V6·7VÒÂ–æFW‚ôÖ—'&÷"–FVçF—G’Â†—7F÷&–6Â†6‚ÂæB&VÆV6R&VF–6FRà ¥&öÆÆ&6²&WfW'G2F†RæWr&–Ö'’Â66†VÖÂæBWFFW"ÖvVæW&FVB6ö×æ–öâ6†ævW2FövWF†W"â†—7F÷&–6Â&–Ö&–W27F’VçF÷V6†VBâ&VÆV6RFÖ—76–öâ&VÖ–ç2f–ÆVBVçF–Â6ö†W&VçBF—&V7BÖöæÇ’Wf–FVæ6Rw&‚W†—7G2â&öÆÆ&6²ÕU5BäõB&W7F÷&R7W'&VçB'&–FvR526VÖçF–72à ¢222W&ÖæVçBG&–ævRF&vWG0 ¤G&–âF†—2FV6—6–öâÂgFW"–×ÆVÖVçFF–öâWf–FVæ6RW†—7G2Â–çFó  ¢¢¢¤„DR66†VÖ2æB'F–f7G2¢¢Â*s‚ãrÂf÷"F†RæWrF—&V7B×6VÆV7F–öâfÖ–Ç’æBF†R†—7F÷&–6Â'&–FvR6Æ76–f–6F–öâ÷7GW&Râ ¢¢¢¤„DR66†VÖ2æB'F–f7G2¢¢Â*s‚ãbã2ãBÂf÷"7W'&VçBD"ôõ2&–æF–æw2Â'F–f7B–FVçF—F–W2ÂæBF‚×&ööb÷væW'6†—â ¢¢¢¤„DRÖV6†æ–72wV–FR¢¢Â*|*s#ã2æB#ã2ãÂFò&VÖ÷fR7F—fR'&–FvR×&—G’ÖV6†æ–72v†–ÆR&W6W'f–ærG'WF†gVÂ&÷rÖÆWfVÂ&ööbæB66÷R&F–öæÆRâ ¢¢¢¤„DRv÷fW&ææ6R¢¢Â*s"ã66WFæ6RFö¶Vç6ÂFò&WF—&R'&–FvRÖöæÇ’Fö¶Vâ6VÖçF–72v—F†÷WB7&VF–æræWrFö¶Vâ'’–×Æ–6F–öâà ¢222W‡Æ–6—Bæöæ6Æ–×0 ¥F†—2FFVæGVÒFöW2æ÷B—G6VÆb–×ÆVÖVçBF†R&öGV6W"÷"66†VÖÂvVæW&FR÷"fÆ–FFRF†R&–Ö'’ÂÇFW"†—7F÷&–6Â'—FW2ÂW†V7WFRõ2Â&÷fRW‡FW&æÂFF&6Rf–Æ&–Æ—G’Â&÷fR&–Çv’7FFRÂWF†÷&—¦RFF&6Rw&—FRÂW7F&Æ—6‚52Â6F—6g’Fö¶VâÂÖ÷fRc’7FGW2Â&Wf—6RF†RÆâÂFWÆ÷’ÂÖ–w&FRÂ66WBF†R&VÖVF–F–öâ6Æ–6RÂ÷"6Æ÷6R„DRÔU”33‚à ¢ÒÒÐ ¢22"ãB’„DRÔU”33‚÷7BÕ#3S’&VÖVF–F–öâ(	BE"Ô4äôâÓrWF†÷&—¦F–öâÔ&÷VæBõ2Ó2F—&V7B&VBÔöæÇ’÷7GW&R6¶W@ ¥F–ÖW7F×¢s##b#£ ¤FWF–Ç3¢F†RvÆ÷r–×ÆVÖVçFF–öâvVçBFV6†æ–6ÆÇ’&÷fVBE"Ô4äôâÓvv—F‚6æöâVffV7BU…DTäE6âF†—2FFVæGVÒW7F&Æ—6†W2F†RÖ—76–ærÆ—f–ær6öçG&7Bf÷"öæR6W&FVÇ’WF†÷&—¦VBÂ6÷W&6RÖ&÷VæBÂF—&V7BÖöæÇ’Â&VBÖöæÇ’õ2Ó26¶WBâ—BFöW2æ÷BW†V7WFRõ2÷"WF†÷&—¦R7FæF–ærFF&6R66W72à ¢222FV6—6–öâæBW†V7WF–öâ&÷VæF' ¤õ2Ó2—2F†R6öÆR7W'&VçBÆ—fRFF&6R×÷7GW&RWf–FVæ6RÆæRf÷"F†R„DRÔU”33‚F—&V7BÖöæÇ’&VÖVF–F–öââ—B—2æWrWf–FVæ6RfÖ–Ç’æBFöW2æ÷BWw&FRÂÆ–2Â&VÆ&VÂÂ&W'VâÂ÷"&WÆ6RF†R†—7F÷&–6Â&÷fVææ6Röbõ2Ó÷"F†Rf–ÆVBõ2Ó"GFV×Bà ¥F†R÷W&F–öæÂF&vWB—2F†R„DRFF&6R&V6†&ÆRöæÇ’F‡&÷Vv‚â÷W&F÷"×7WÆ–VBDD$4UõU$ÆÂv—F‚ôTåcÖFWfÂFF&6R66†VÖ†FVÂæB6V&6‚F‚†FRÂV&Æ–6âæò&–Çv’4Ä’Â'&–FvR6W'f–6RÂ…EEFF&6RG&ç7÷'BÂfVæF÷"FFW"ÂÇFW&æFRE4â6÷W&6RÂ&WG'’FFW"Â÷"FF&6Rw&—FR'F–6—FW2à ¤vVçBW†V7WF–öâ&VÖ–ç2v÷fW&æVB'’FFVæGVÒ"ãÂ¢¥òÔFVÆVvFVBõ2W†V7WF–öâWF†÷&—G’(	BòWF†÷&—¦F–öâ6öçG&öÇ2W†V7WF÷"–FVçF—G’¢¢âF6²×7V6–f–2ò&÷fÂöbW†7BWF†÷&—¦F–öâ'—FW2—2ÖæFF÷'’&Vf÷&RÆVæ6‚à ¢222WF†÷&—¦F–öâ–FVçF—G ¥F†R6æöæ–6ÂWF†÷&—¦F–öâ66†VÖ—2†FUöW–33‚æ÷32æWF†÷&—¦F–öâçcB66†VÖ2ö†FUöW–33…ö÷35öWF†÷&—¦F–öâçcæ§6öæà ¥F†RWF†÷&—¦F–öâ6öçF–ç2W†7FÇ“  ¢¢66†VÖ ¢¢'Våö–F ¢¢WF†÷&—¦VEöE÷WF6 ¢¢W‡—&W5öE÷WF6 ¢¢6÷W&6Uö6öÖÖ—F ¢¢'VææW%÷6†#Sf ¢¢fÆ–FF÷%÷6†#Sf ¢¢–çFW'&WFW& ¢¢F&vWF ¢¢&–Ç6 ¢¢&WF—&VEö¶W—5÷&WV—&VEö'6VçF ¢¢÷&FW&VE÷VW'•ö–G6 ¢¢W‡V7FVEö6÷VçG6 ¢¢6æF–FFU÷&ö÷F ¢¢W†7Eö&wf ¢¢öæUöGFV×F  ¦'Våö–FÖF6†W2å¶×£Ó•Õ¶×£Ó’Õ×³RÃc7ÒFæBFWFW&Ö–æW2F†W6RW†7BFW&—fVB&ö÷G3  ¢¢'Vâ&ö÷C¢÷F×ö†FRÖW–33‚Ö÷32óÇ'Våö–Câö ¢¢6öçG&öÂ&ö÷C¢÷F×ö†FRÖW–33‚Ö÷32óÇ'Våö–Câö6öçG&öÂö ¢¢6æF–FFR&ö÷C¢÷F×ö†FRÖW–33‚Ö÷32óÇ'Våö–Câö6æF–FFRö ¢¢f–ÇW&R&ö÷C¢÷F×ö†FRÖW–33‚Ö÷32óÇ'Våö–Câöf–ÇW&Rö  ¦Ç'Våö–Cæ—2W†7B6öæ6FVæF–öâöbF†RfÆ–FFVBWF†÷&—¦F–öâf–VÆBÂæ÷BâVç&W6öÇfVBW†V7WF–öâ–çWBà ¦–çFW'&WFW&6öçF–ç2W†7FÇ’·&W6öÇfVE÷F‚Ç6†#SgÖà ¦F&vWF—2W†7FÇ’¶öVçc¢vFWbrÆFF&6U÷66†VÖ¢v†FRrÇ6V&6…÷Fƒ¥²v†FRrÂwV&Æ–2u×ÖæB6öçF–ç2æò†÷7BÂE4âÂ77v÷&BÂ÷"&öÆRfÇVRà ¦&–Ç6—2W†7FÇ’·6fUöÖöFS¢srÆÆÆ÷uöæWGv÷&³¢srÆÆÆ÷uöF%÷w&—FS¢srÆF%÷&VEöWF†÷&—¦VC§G'VWÖâÄÄõuôäUEtõ$³Óf÷&&–G2vVæW&Â…EEÂfVæF÷"Â4Ä’ÂæB÷F†W"æWGv÷&²7F—f—G’âF%÷&VEöWF†÷&—¦VF—2F†R6öÆRæ'&÷rW†6WF–öâf÷"F†R&÷VæBF—&V7B÷7Fw&U5Â&÷f–FW"F‚æBæWfW"WF†÷&—¦W26V6öæBF&vWBÂ&÷f–FW"Â&÷Fö6öÂÂ&WG'’Â÷"w&—FRà ¦&WF—&VEö¶W—5÷&WV—&VEö'6VçF—2W†7FÇ“  ¢¢D%ôÄÄõuô%$”DtUô”åõ$ôF ¢¢D%ô%$”DtUõU$Æ ¢¢D%ôdõ$4Uô%$”DtV  ¦÷&FW&VE÷VW'•ö–G6—2W†7FÇ“  £â6WE÷G&ç67F–öå÷&VEööæÇ– £"â6WE÷6V&6…÷F† £2â6öææV7F–öåö–FVçF—G– £Bâ6V&6…÷F† £Râ'VçF–ÖU÷&öÆUöw&çG6 £bâFFÅö6öÇVÖç6 £râFFÅö6öç7G&–çG6 £‚â&÷VæF'•÷f–Ww6 £’â'F—F–öåö–çfVçF÷'– £â'F—F–öå÷fW&–g–  ¦W‡V7FVEö6÷VçG6—2W†7FÇ“  ¢¢&÷f–FW%÷6VÆV7F–öç3¢ ¢¢†VÇF…ö6öææV7F–öç3¢ ¢¢†VÇF…÷7Å÷7FFVÖVçG3¢ ¢¢÷7GW&U÷G&ç67F–öç3¢ ¢¢÷7GW&U÷7Å÷7FFVÖVçG3¢ ¢¢F—&V7Eö6öææV7F–öç3¢& ¢¢7Å÷7FFVÖVçG3¢ ¢¢7Å÷w&—FW3¢ ¢¢&WG&–W3¢ ¢¢ÇFW&æFU÷&÷f–FW%öGFV×G3¢  ¥F†R†VÇF‚7FFVÖVçB—2W†7FÇ’4TÄT5BâF†RFVâ÷7GW&R7FFVÖVçG2&RF†R÷&FW&VBVW'’&÷7FW"à ¦6æF–FFU÷&ö÷FWVÇ2F†RW†7BFW&—fVB6æF–FFRF‚æB—2æWfW"&WòF‚à ¦W†7Eö&wf&–æG2F‡&VRfV7F÷'2–â÷&FW#¢6GW&R&öGV6W"Â&V6V—BÖVÖ—GF–ær–æFWVæFVçBfÆ–FF÷"ÂæBf–æÂ&VBÖöæÇ’fÆ–FF÷"âWfW'’—F†öâfV7F÷"W6W2F†R6ÖR&W6öÇfVB–çFW'&WFW"föÆÆ÷vVB'’W†7BÔ–ÂÔ&ÂF†R&÷VæB67&—BF‚ÂæB—G2&÷VæBÖöFRÂWF†÷&—¦F–öâÂæB6æF–FFR&wVÖVçG2à ¦öæUöGFV×F—2Æ—FW&ÂG'VVâF†R'VææW"w&—FW2ÆVæ6‚Ö&¶W"&Vf÷&R&÷f–FW"6VÆV7F–öââç’f–ÇW&RgFW"F†RÖ&¶W"6öç7VÖW2F†RWF†÷&—¦F–öââ&WG'’&WV—&W2æWròÖ&÷fVBWF†÷&—¦F–öâ'—FW2à ¢222Vçf—&öæÖVçBÂ6÷W&6RÂæBw&—FR—6öÆF–öà ¥F†R'VææW"7F'G26ÆVâ6†–ÆBVçf—&öæÖVçB6öçF–æ–æröæÇ’&WV—&VBÆö6ÆRæB&–ÂæÖW2ÂôTåfÂæBDD$4UõU$Æâæò•D„ôâ¦Vçf—&öæÖVçBæÖR—2f÷'v&FVBâF†RDD$4UõU$ÆfÇVR—276VBöæÇ’FòF†R6†–ÆBF—&V7B&÷f–FW"æB—2æWfW"6W&–Æ—¦VBÂÆövvVBÂ†6†VB2Wf–FVæ6R6öçFVçBÂ÷"–æ6ÇVFVB–â&WF–æVBW†6WF–öâà ¥F†R'VææW"&÷fW2gVÆÂ6÷W&6RÖÖæ–fW7BWVÆ—G’æB'6Væ6Röbõ÷–66†UõöæBç–6&W6–GVR&Vf÷&RæBgFW"6GW&Râw&—FW2&RÆ–Ö—FVBFòF†RW†7BFW&—fVB6öçG&öÂÂ6æF–FFRÂæBf–ÇW&R&ö÷G2âF†RÆVæ6‚Ö&¶W"æBWF†÷&—¦F–öâÖ6öç7V×F–öâ&V6÷&BÆ—fR–âF†R6öçG&öÂ&ö÷C²7V66W72&–Ö&–W2Æ—fR–âF†R6æF–FFR&ö÷C²f–ÇW&R&V6V—BÆ—fW2–âF†Rf–ÇW&R&ö÷Bâ6÷W&6RæB&Wòw&—FW2&Ræ÷BWF†÷&—¦VBà ¢222&VBÖöæÇ’FF&6Rö'6W'fF–öà ¥F†R'VææW"6ÆÇ2D$66W72æf÷%ö7W'&VçEöVçfW†7FÇ’öæ6RâF†RW†—7F–ær†VÇF‚÷W&F–öâ÷Vç2öæRF—&V7B6öææV7F–öâæBW†V7WFW2W†7FÇ’4TÄT5Bà ¥F†R'VææW"F†Vâ6ÆÇ2D$66W72ç&VFöæÇ•÷G†W†7FÇ’öæ6Rv—F‚F†RFVâ÷&FW&VB÷7GW&R7FFVÖVçG2â6WE÷G&ç67F–öå÷&VEööæÇ–—2f—'7BæB×W7B7V66VVB&Vf÷&Rç’ö'6W'fF–öââ6WE÷6V&6…÷F†—26V6öæBâF†R&VÖ–æ–ær7FFVÖVçG2&R&VBÖöæÇ’4„õv÷"4TÄT5Fö'6W'fF–öç26÷'&W7öæF–æröæR×FòÖöæRFòF†V—"VW'’”G2âF†R6öææV7F–öâÖ–FVçF—G’ö'6W'fF–öâ–æ6ÇVFW27W'&VçE÷6WGF–ær‚wG&ç67F–öå÷&VEööæÇ’r–Â6òF†R&VBÖöæÇ’&VF–6FR—2ö'6W'fVBÂæ÷B–æfW'&VBà ¥F†R&÷f–FW"æWfW"6öÖÖ—G2æBÇv—2&öÆÇ2&6²–âf–æÆÇ–Â–æ6ÇVF–ærgFW"7V66W76gVÂö'6W'fF–öââ7FF–25Â6Æ76–f–6F–öâæB&÷f–FW"ÖÆWfVÂVæf÷&6VÖVçB&÷F‚&V¦V7B×WFF–ær5Ââç’W‡G&7FFVÖVçBÂ6öææV7F–öâÂ&÷f–FW"GFV×BÂG&ç67F–öâÂ÷"&WG'’—2f–ÇW&Rà ¢2227V66W726¶WB–çfVçF÷'’æB÷væW'6†—  ¥F†R6æF–FFR7V66W72&ö÷B6öçF–ç2W†7FÇ’FVâ&–Ö&–W3  §Â&–Ö'’Â'F–f7B¶W’Â&V6÷&BG—RÂ6öÆR&öGV6W"À§Â¢ÒÒÒÒÂ¢ÒÒÒÒÂ¢ÒÒÒÒÂ¢ÒÒÒÒÀ§Â6öÖÖæG2çG‡FÂW–33‚æ÷32æ6öÖÖæG6ÂW–33…ö÷35÷FW‡FÂ67&—G2ö÷2ö†FUöW–33…ö÷32ç–À§Â7FF÷WBæÆövÂW–33‚æ÷32ç7FF÷WFÂW–33…ö÷35öÆövÂ67&—G2ö÷2ö†FUöW–33…ö÷32ç–À§Â7FFW'"æÆövÂW–33‚æ÷32ç7FFW'&ÂW–33…ö÷35öÆövÂ67&—G2ö÷2ö†FUöW–33…ö÷32ç–À§ÂW†—Eö6öFRçG‡FÂW–33‚æ÷32æW†—Eö6öFVÂW–33…ö÷35÷FW‡FÂ67&—G2ö÷2ö†FUöW–33…ö÷32ç–À§ÂVçe÷&W6Væ6Ræ§6öæÂW–33‚æ÷32æVçe÷&W6Væ6VÂW–33…ö÷35öVçe÷&W6Væ6VÂ67&—G2ö÷2ö†FUöW–33…ö÷32ç–À§ÂF%÷÷7GW&U÷7VÖÖ'’æ§6öæÂW–33‚æ÷32æF%÷÷7GW&U÷7VÖÖ'–ÂW–33…ö÷35öF%÷÷7GW&VÂ67&—G2ö÷2ö†FUöW–33…ö÷32ç–À§Âæöæ6Æ–×2æ§6öæÂW–33‚æ÷32ææöæ6Æ–×6ÂW–33…ö÷35öæöæ6Æ–×6Â67&—G2ö÷2ö†FUöW–33…ö÷32ç–À§Â&W7VÇE÷7VÖÖ'’æ§6öæÂW–33‚æ÷32ç&W7VÇE÷7VÖÖ'–ÂW–33…ö÷35÷&W7VÇFÂ67&—G2ö÷2ö†FUöW–33…ö÷32ç–À§ÂfÆ–FF–öå÷&V6V—Bæ§6öæÂW–33‚æ÷32çfÆ–FF–öå÷&V6V—FÂW–33…ö÷35÷fÆ–FF–öæÂFööÇ2öWf–FVæ6Rö†FUöW–33…ö÷32ç’ÒÖVÖ—B×&V6V—FÀ§Â6†V6·7V×2ç6†#SfÂW–33‚æ÷32æ6†V6·7V×6ÂW–33…ö÷35ö6†V6·7VÖÂ67&—G2ö÷2ö†FUöW–33…ö÷32ç–À ¥F†RG&6¶VBFW7F–æF–öâgFW"–æFWVæFVçBFÖ—76–öâ—2W†7FÇ’VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öÇW2V6‚f–ÆVæÖRâF†R'VææW"æWfW"w&—FW2F†RG&6¶VBFW7F–æF–öââ"Óe"Ô"6÷–W2F†RfÆ–FFVB'—FW2W†7FÇ’æBFöW2æ÷B&V6öÖRF†V—"&öGV6W"à ¦6öÖÖæG2çG‡F6öçF–ç2F‡&VRÄb×FW&Ö–æFVBÆ–æW2æÖVB6GW&Uö&wcÖÂ&V6V—Eö&wcÖÂæBfÆ–FFUö&wcÖföÆÆ÷vVB'’6æöæ–6Â¥4ôâ&wb'&—2â7FFW'"æÆöv—2V×G’öâ52âW†—Eö6öFRçG‡F—2W†7FÇ’ÇW2Äbâ6†V6·7V×2ç6†#Sf6öçF–ç2öæR44”’×6÷'FVBÃcBÖÆ÷vW&66RÖ†WƒãÇGvò76W3ãÆf–ÆVæÖSæÆ–æRf÷"V6‚&V6VF–ær&–Ö'’æBæWfW"Æ—7G2—G6VÆbà ¢222¥4ôâ6öçG&7G2æB66†VÖ&÷7FW  ¤ÆÂ¥4ôâ6öçG&7G2&V¦V7BVæ¶æ÷vâ¶W—2BWfW'’ÆWfVÂæBW6R6æöæ–6Â'—FW2à ¢¢Vçe÷&W6Væ6Ræ§6öæW6W266†VÖ†FUöW–33‚æ÷32æVçe÷&W6Væ6RçcæB6öçF–ç2W†7FÇ’66†VÖÂ'Våö–FÂöVçfÂ&–Ç6ÂFF&6U÷W&Å÷&W6Væ6VÂ&WF—&VEö¶W•÷&W6Væ6VÂæBFWFW&Ö–æ—6Õ÷–ç6âDD$4UõU$Æ—2&V6÷&FVBöæÇ’24UEõ$TD5DTF²WfW'’&WF—&VB¶W’—2Tå4UF²&–Ç2æB–ç2ÖF6‚WF†÷&—¦F–öââ ¢¢F%÷÷7GW&U÷7VÖÖ'’æ§6öæW6W266†VÖ†FUöW–33‚æ÷32æF%÷÷7GW&U÷7VÖÖ'’çcæB6öçF–ç2W†7FÇ’66†VÖÂ'Våö–FÂ6÷W&6Uö6öÖÖ—FÂ&÷f–FW&Â6VÆV7F–öåöGFV×G6Â÷&FW&VE÷VW'•ö–G6ÂVW'•÷&W7VÇG6Âö'6W'fF–öç6Â6÷VçG6Â&VF–6FW6ÂæB&W7VÇFâ&÷f–FW"—27–6÷vâDDÂ–FVçF—G’6—FW2†FRæFFÅö–FVçF—G•÷&ö¦V7F–öâçcâWfW'’FV6—6—fR&VF–6FR×W7B&RG'VRf÷"52â ¢¢æöæ6Æ–×2æ§6öæW6W266†VÖ†FUöW–33‚æ÷32ææöæ6Æ–×2çcæB6öçF–ç2W†7FÇ’66†VÖÂ'Våö–FÂæBæöæ6Æ–×6âF†R6÷'FVB&÷7FW"—266WFæ6U÷Fö¶Vå÷6F—6f7F–öæÂFWÆ÷–ÖVçFÂW–5ö6Æ÷6V÷WFÂÖ–w&F–öæÂc•÷7FGW5öÖ÷fVÖVçFÂ&öGV7F–öå÷w&—FUöWF†÷&—¦F–öæÂ÷76Â&–Çv•ö–çfVçF÷'•÷&ööfÂæB&WF—&VE÷G&ç7÷'Eöf–Æ&–Æ—G–â ¢¢&W7VÇE÷7VÖÖ'’æ§6öæW6W266†VÖ†FUöW–33‚æ÷32ç&W7VÇE÷7VÖÖ'’çcæB6öçF–ç2W†7FÇ’66†VÖÂ'Våö–FÂ6÷W&6Uö6öÖÖ—FÂWF†÷&—¦F–öå÷6†#SfÂ6GW&U÷&W7VÇFÂFV6—6—fU÷&VF–6FW6Â&–Ö'•öf–ÆW6ÂæBæöæ6Æ–×5÷&Vfâ6GW&U÷&W7VÇF—256â&–Ö'•öf–ÆW6Æ—7G2W†7FÇ’F†Rf—'7BV–v‡B'VææW"Ö÷væVBFF&–Ö&–W2–â44”’÷&FW"æBW†6ÇVFW2F†RÆFW"fÆ–FF÷"&V6V—BæB6†V6·7VÒÆVFvW"â ¢¢fÆ–FF–öå÷&V6V—Bæ§6öæW6W266†VÖ†FUöW–33‚æ÷32çfÆ–FF–öå÷&V6V—BçcæB6öçF–ç2W†7FÇ’66†VÖÂ'Våö–FÂWF†÷&—¦F–öå÷6†#SfÂfÆ–FFVEöf–ÆW6Â&VF–6FW6ÂæB&W7VÇFâ—G2&VF–6FW2&RWF†÷&—¦F–öå÷fÆ–FÂ6÷W&6Uö–FVçF—G•÷fÆ–FÂ66†VÖ5÷fÆ–FÂ6æöæ–6Åö'—FW5÷fÆ–FÂ–çfVçF÷'•÷fÆ–FÂ6÷VçG5÷fÆ–FÂ6V7&WE÷66å÷fÆ–FÂæBæöæ6Æ–×5÷fÆ–FÂÆÂG'VRf÷"52à ¥F†R6WfVâ66†VÖF‡2&S  ¢¢66†VÖ2ö†FUöW–33…ö÷35öWF†÷&—¦F–öâçcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35öVçe÷&W6Væ6Rçcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35öF%÷÷7GW&U÷7VÖÖ'’çcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35öæöæ6Æ–×2çcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35÷&W7VÇE÷7VÖÖ'’çcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35÷fÆ–FF–öå÷&V6V—Bçcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35öf–ÇW&U÷&V6V—Bçcæ§6öæ  ¤V6‚G&6¶VB66†VÖ—2–æFW†VBv—F‚'F–f7B¶W’W–33‚æ÷32ç66†VÖãÆ&6VæÖR×v—F†÷WBÖW‡FVç6–öãææB&V6÷&BG—RW–33…ö÷35÷66†VÖà ¢222f–ÇW&R&V6V—BæBFÖ—76–&–Æ—G ¤öâ&RÖÖ&¶W"÷"÷7BÖÖ&¶W"f–ÇW&RÂF†R'VææW"VÖ—G2W†7FÇ’÷F×ö†FRÖW–33‚Ö÷32óÇ'Våö–Câöf–ÇW&Röf–ÇW&U÷&V6V—Bæ§6öæW6–ær66†VÖ†FUöW–33‚æ÷32æf–ÇW&U÷&V6V—Bçcv—F‚W†7Bf–VÆG266†VÖÂ'Våö–FÂWF†÷&—¦F–öå÷6†#SfÂ†6VÂ6öFVÂÆVæ6…ö6öç7VÖVFÂ6æF–FFUöFÖ—76–&ÆVÂæBæöæ6Æ–×6à ¥&RÖÖ&¶W"f–ÇW&RW&f÷&×2æòW‡FW&æÂFF&6R÷W&F–öââ÷7BÖÖ&¶W"f–ÇW&R&V6÷&G2WF†÷&—¦F–öâ6öç7V×F–öâæB7F÷2â6æF–FFUöFÖ—76–&ÆV—2Çv—2fÇ6RâF†R&V6V—B6öçF–ç2æòG&6V&6²ÂW†6WF–öâÖW76vRÂVW'’&÷w2ÂE4âÂ†÷7BÂ&öÆRæÖRÂ÷"6V7&WBâf–ÇW&R&V6V—G2&RF–væ÷7F–2öæÇ’Â&Ræ÷B6÷–VB–çFòF†R7V66W72&ö÷BÂ&Ræ÷B–æFW†VBÂæB&RæWfW"G&ç6f÷&ÖVB–çFò52à ¢222fÆ–FF–öâÂFÖ—76–öâÂÖ–w&F–öâÂæB&öÆÆ&6° ¤–æFWVæFVçBWF†÷&—¦F–öâfÆ–FF–öâ&V6VFW2ÆVæ6‚ÖÖ&¶W"7&VF–öââ–æFWVæFVçB&V6V—BfÆ–FF–öâ&V6VFW26†V6·7VÒ7&VF–öââf–æÂ6¶WBfÆ–FF–öâ—2&VBÖöæÇ’â"Óe"Ô"&WVG2fÆ–FF–öâ&Vf÷&RæBgFW"W†7B'—FR6÷’â×WFF–öâFW7G26÷fW"WfW'’f–VÆBÂ6÷VçBÂF‚Â&wbfV7F÷"Â6÷W&6R†6‚Â6æöæ–6Â'—FRÂ6†V6·7VÒÂ6V7&WBÖ&¶W"Â5Â6Æ72ÂæBW‡G&Öf–ÆR66Rà ¤GW&–ær"Óe"Ô"ÂF†R6æöæ–6ÂWFFW"7&VFW26–&Æ–ærF‚&öög2f÷"ÆÂFVâ&–Ö&–W2æB6WfVâ66†VÖ2ÂF†Vâ&Vg&W6†W2F†R‡VÖâWf–FVæ6R–æFW‚ÂÖ6†–æRWf–FVæ6RÖ—'&÷"Â†6‚6VçF–æVÇ2Â6†V6·7V×2ÂæB&WV—&VBF‚&öög2âfVGW&R&öGV6W'2Fòæ÷Bw&—FRF†÷6R6ö×æ–öç2à ¤âõ2f–ÇW&R&öGV6W2æòG&6¶VBWf–FVæ6RæB&Æö6·2"Óe"Ô"â"Óe"Ô"fÆ–FF–öâf–ÇW&R&VÖ÷fW2F†R7FvVB6¶WBg&öÒF†R&÷÷6VB6†ævR&Vf÷&R6öÖÖ—Bâ†—7F÷&–6ÂWf–FVæ6R&VÖ–ç2VçF÷V6†VBà ¢222W&ÖæVçBG&–ævRF&vWG0 ¤G&–âF†—2FV6—6–öâ–çFó  ¢¢¢¤„DR66†VÖ2æB'F–f7G2¢¢Â*|*s‚ãbã2ãBæB‚ãrÂf÷"F†Rõ2Ó266†VÖ2Â&ö÷BÂ'F–f7B¶W—2Â&V6÷&BG—W2Â&öGV6W'2Â6ö×æ–öç2ÂfÆ–FF–öâÂæB&VÆF–öç6†—Fò†—7F÷&–6Âõ2Óâ ¢¢¢¤„DRv÷fW&ææ6R¢¢Â*s"ã66WFæ6RFö¶Vç6ÂöæÇ’Fò7FFRF†Bõ2Ó2FöW2æ÷BÖ–çBæWr66WFæ6RFö¶Vâ'’–×Æ–6F–öâæBF†B&WF—&VB'&–FvRÖöæÇ’Fö¶Vâ6VÖçF–72&VÖ–âVæ6Æ–Ö&ÆRà ¤FFVæGVÒ"ãw2F6²×7V6–f–2òFVÆVvF–öâæBF†RvVæW&Â6V7&WB×6fRÂ&VBÖöæÇ’ÂæòÖ÷fW&6Æ–ÒÂWf–FVæ6RÖFÖ—76–öâÂæB66WFæ6R×6W&F–öâ&–Ç2&VÖ–âVæ6†ævVBà ¢222W‡Æ–6—Bæöæ6Æ–×0 ¥F†—2FFVæGVÒFöW2æ÷B—G6VÆb&÷fRW†7B'VâWF†÷&—¦F–öâ'—FW2ÂW†V7WFRõ2Ó2ÂW7F&Æ—6‚W‡FW&æÂFF&6Rf–Æ&–Æ—G’Â&÷fR&–Çv’–çfVçF÷'’Âw&—FR÷"Ö–w&FRFF&6RÂÖöF–g’6W'f–6RÂFWÆ÷’Â7&VFR52Â6F—6g’Fö¶VâÂÖ÷fRc’7FGW2Â&Wf—6RF†RÆâÂ66WBF†R&VÖVF–F–öâ6Æ–6RÂ6ö×ÆWFRF†RW–2Â÷"6Æ÷6R„DRÔU”33‚à ¢ÒÒÐ ¢22"ãR’„DRÔU”33‚÷7BÕ#3S’&VÖVF–F–öâ(	BE"Ô4äôâÓ‚F—&V7BÔöæÇ’c’ãb6ö×ÆWF–öâ6VÖçF–72æB"Óe"÷væW'6†—  ¥F–ÖW7F×¢s##b#£ ¤FWF–Ç3¢F†RvÆ÷r–×ÆVÖVçFF–öâvVçBFV6†æ–6ÆÇ’&÷fVBE"Ô4äôâÓ†v—F‚6æöâVffV7BÔTäE6âF†—2FFVæGVÒW7F&Æ—6†W2F†RW†7BF—&V7BÖöæÇ’ÖVæ–æröbF†RffV7FVBF—7F–ÆÆF–öâ&÷w2æBF†R&÷fVææ6R×&W6W'f–ær"Óe"W†V7WF–öâ6WVVæ6Râ—B6W6W2æòWFöÖF–2c’7FGW2Ö÷fVÖVçBà ¢222FV6—6–öâæBVffV7F—fRc’÷7GW&P ¤f÷"„DRÔU”33‚öæÇ“  ¢¢„DRÔD•5CãF—2ÖVæFVB'’&VÖ÷f–ær7F—fR'&–FvRfÆÆ&6²æB&÷f–FW"×&—G’ö&Æ–vF–öç2â—G27F—fR6ö×ÆWF–öâÖVæ–ær—2F—&V7B×&÷f–FW"6VÆV7F–öâÂ7G&–7B&WF—&VBÖ¶W’&VgW6ÂÂG—VBF—&V7Bf–ÇW&RÂF—&V7BFF&6R÷7GW&RÂÆV7B×&—f–ÆVvRæB6V&6‚×F‚ö'6W'fF–öâÂDDÂ–FVçF—G’&ö¦V7F–öâÂ6öç7G&–çBæB&÷VæF'’×f–Wrö'6W'fF–öâÂ'F—F–öâ÷7GW&RÂæB7W'&VçBv÷fW&æVBWf–FVæ6R&–æF–ærâ ¢¢„DRÔD•5Cã–—2&VæÖVBæB&VFVf–æVB2¢¦F—&V7BFF&6R6öææV7F—f—G’b&WF—&VB×G&ç7÷'BVæf÷&6VÖVçF¢¢â—B&÷fW2DD$4UõU$ÆæB7–6÷vöæÇ“²WfW'’&WF—&VB¶W’&VgW6W2&Vf÷&R&÷f–FW"’ôó²Ö—76–ær÷"Væf–Æ&ÆRF—&V7B66W72f–Ç26Æ÷6VBv—F‚G—VB÷7GW&S²ÇFW&æFR×&÷f–FW"GFV×G2&R¦W&ó²Æ—fRF—&V7B÷7GW&R—2&VBÖöæÇ“²DDÂG'WF‚—2&ö¦V7F–öâÖöæÇ’VæFW"†FRæFFÅö–FVçF—G•÷&ö¦V7F–öâçc²æB7W'&VçBÆö6ÂÇW2õ2Ó2Wf–FVæ6R—2&÷VæB–âF†R‡VÖâWf–FVæ6R–æFW‚æBÖ6†–æRWf–FVæ6RÖ—'&÷"â ¢¢„DRÔD•5Cãf&WF–ç2—G2öæRÖ'WGFöâ&VÆV6R×6æ—G’ÖVæ–ærÂ'WB—G27W'&VçBFWVæFVæ6–W2&RF†RF—&V7BÖöæÇ’Wf–FVæ6Rw&‚æBF†R÷&FW&VB—VÆ–æR&VÆ÷râ ¢¢„DRÔD•5Cã&WF–ç2—G26öæf–wW&VB×c"ÖVBÖ66†RÖVæ–ærâW†—7F–ærÆö6ÂWf–FVæ6RæBõ2Ó"&VÖ–âF†R&÷VæFVBWf–FVæ6R÷væW'3²'&–FvR×7V6–f–2æòÔ’ôò†öö·2&R&WÆ6VBv—F‚G&ç7÷'BÖæWWG&ÂwV&G2v—F†÷WB&V÷Væ–ær÷"&W'Vææ–ærõ2Ó"â ¢¢„DRÔD•5CRã&&WF–ç2—G2‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"Â6†V6·7VÒÂF‚×&ööbÂWFFW"ÂæB÷&–VçFF–öâF—66—Æ–æRà ¤WfW'’÷F†W"c’&÷ræBF†RvVæW&Âc’7FGW2ÖöFVÂ&VÖ–âVæ6†ævVBà ¥F†—2FFVæGVÒFöW2æ÷B6†ævRç’&V6÷&FVB7FGW2â„DRÔD•5CãFÂ„DRÔD•5CãfÂ„DRÔD•5Cã–ÂæB„DRÔD•5CRã&&VÖ–â'F–Æ²„DRÔD•5Cã&VÖ–ç2÷F–öæÆVçF–Â6W&FVÇ’&Wf–WvVBWf–FVæ6R7W÷'G2ÆFW"‡VÖâc’7F–öâà ¢222÷væW'6†—æBF÷F–öâ6WVVæ6P ¥F†RÖæFF÷'’W†V7WF–öâ6WVVæ6R—3  £â”FV6†æ–6Â&÷fÂöbF†R&W66÷–ærFV6—6–öââ £"â6W&FVÇ’WF†÷&—¦VB&Wf—6–öâöbF†R7W'&VçB–×ÆVÖVçFF–öâÆâÆ–æVvRâ £2â"Óe"Ô–×ÆVÖVçFF–öâÂ&Wf–WrÂæBÖW&vRöbF—&V7BÖöæÇ’6÷W&6R6öçfW&vVæ6RÂ&WF—&VBÖ¶W’&VgW6ÂÂF—&V7BÆö6ÂWf–FVæ6RÂõ2Ó2FööÆ–ærÂ66†VÖ2ÂG&ç7÷'BÖæWWG&ÂÖVBÖ66†RwV&G2ÂæBfö7W6VBFW7G2â £Bâò&÷fÂöbW†7Bõ2Ó2WF†÷&—¦F–öâ'—FW2&÷VæBFòF†RÖW&vVB"Óe"Ô6÷W&6R6öÖÖ—Bâ £RâöæRõ2Ó2W†V7WF–öâæB–æFWVæFVçBFÖ—76–öâVæFW"FFVæGVÒ"ãBâ £bâ"Óe"Ô&W†7B6¶WB6÷’Â7W'&VçB×fW'7W2Ö†—7F÷&–6ÂWf–FVæ6R&–æF–ærÂ6æöæ–6ÂWFFW"6öçfW&vVæ6RÂf–æÂF—&V7BÖöæÇ’&VÆV6R–çFVw&F–öâÂæB&÷r×7V6–f–27W÷'B7&÷77vÆ²â £râf–æÂFV6†æ–6ÂæBWf–FVæ6R&Wf–Wrâ £‚â6W&FRW&ÖæVçBbG&–ævRæBç’&÷r×7V6–f–2c’7FGW2Ö–çFVææ6Rà ¦#&VÖ–ç2F†RW–2×66÷R&6VÆ–æRâF†Rö'6öÆWFR'&–FvRÖFWVæFVçBõ2Ó"æB"Ô26ÆW6W2&R&VÖ÷fVBg&öÒF†RæW‡B–×ÆVÖVçFF–öâÆâ&Wf—6–öâÂæ÷B&WF–æVB2÷F–öæÂfÆÆ&6²à ¤–×ÆVÖVçFF–öâ&VÆöæw2Fò"Óe"ÔâÆ—fRF—&V7B÷7GW&R&VÆöæw2Fòõ2Ó2âFöÖ–2f–æÂ–çFVw&F–öâæBF†R7W÷'B7&÷77vÆ²&VÆöærFò"Óe"Ô"âc’v÷&F–æræB7FGW2Ö–çFVææ6R&VÖ–â6W&FVÇ’WF†÷&—¦VB‡VÖâÖ÷væVBv÷&²âæò–×ÆVÖVçFF–öâ÷"õ27F÷"w&—FW2c’7FGW2à ¢2226æöæ–6Â&VÆV6R×6æ—G’7FvR÷&FW  ¥F†R6æöæ–6ÂVçG'—ö–çBw&—FW2VF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆövæBW6W2W†7FÇ’F†W6Ræ–æWFVVâÖæFF÷'’7FvW2–â÷&FW#  £âVçf—&öæÖVçB–ç2â £"â–FVçF—G’æB&VÆV6R&÷fVææ6Râ £2â6æöæ–6Â¥4ôââ £Bâ&VFW"ô4Ä’Â"ô$ÂGvò×'VâÂæB&V–ÖvRFWFW&Ö–æ—6Òâ £Râr6FÆörG&ç7÷'Bâ £bâ4’&–Ç2â £râF—&V7BD"6VÆV7F–öâ6öçG&7Bâ £‚âF—&V7BD"÷7GW&R'F–f7G2â £’â&öG”w&‚öÆ–7’â £â&6†—FV7GW&R6æ6†÷Bâ £â6öæf–wW&VB×c"ÖVBÖ66†RÆö6ÂWf–FVæ6Râ £"â†—7F÷&–6Â'&–FvRWf–FVæ6R–çFVw&—G’â £2âõ2Ó"ÖVBÖ66†R6¶WBfÆ–FF–öââ £Bâõ2Ó2F—&V7BD"÷7GW&R6¶WBfÆ–FF–öââ £Râ‡VÖâ–æFW‚æBÖ6†–æRÖ—'&÷"&Vg&W6‚â £bâWf–FVæ6R×F‚fÆ–FF–öââ £râÖ—'&÷"66†VÖæB–æFW‚ôÖ—'&÷"†6‚fÆ–FF–öââ £‚âF÷öÆöw’÷&–VçFF–öâfÆ–FF–öââ £’âf–æÂÔÄbfÆ–FF–öâà ¥7FvR"Ö’&W÷'BöæÇ’„•5Dõ$”4Åô”åDTu$•E•ôô¶â—B6ææ÷B&W÷'B7W'&VçB'&–FvRf–Æ&–Æ—G’Â&—G’Â6&–Æ—G’Â6öç6—7FVæ7’ÂfÆÆ&6²Â÷"7W'&VçBõ252â7FvRB—2ÖæFF÷'’f÷"f–æÂ52âæò&WV—&VB7FvRÖ’&R6¶—VBâF†R—VÆ–æR7F÷2öâF†Rf—'7Bf–ÇW&RÂW&f÷&×2æòW‡FW&æÂ’ôòÂFöW2æ÷B&W'Vâõ2ÂæBFöW2æ÷B&W—"â–æ6öç6—7FVçBWf–FVæ6Rw&‚à ¢2227W'&VçBWf–FVæ6R&–æF–æræBWFFW"÷væW'6†—  ¥"Óe"Ô"&WÆ6W27W'&VçB'&–FvR&÷w2W6VBf÷"&VÆV6RFÖ—76–öâv—F‚F†RF—&V7B×6VÆV7F–öâ&–Ö'’g&öÒFFVæGVÒ"ã2æBF†Rõ2Ó26¶WBg&öÒFFVæGVÒ"ãBà ¤†—7F÷&–6Âõ2ÓæB'&–FvR&–æF–æw2&VÖ–âVæFW"†—7F÷&–6Â&V6÷&BG—W2æBæ÷FW2âF†V—"W†—7F–ær¶W—2æBF‡2Ö’&VÖ–âv†Vâ6†æv–ærF†VÒv÷VÆBFÖvR†—7F÷&–6ÂG&6V&–Æ—G’âõ2Ó"&VÖ–ç27W'&VçB&÷VæFVB7W÷'Bf÷"„DRÔD•5CãæB—2æ÷B&W'Vâà ¤ÆÂ7W'&VçB&–Ö&–W2æB66†VÖ2&Rf–æÆ—¦VB&Vf÷&RF†R6æöæ–6ÂWFFW"'Vç2âFööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç–'Vç2öæ6RæB—2F†R6öÆRw&—FW"öbF†R‡VÖâWf–FVæ6R–æFW‚ÂÖ6†–æRWf–FVæ6RÖ—'&÷"Â6–&Æ–ærF‚&öög2ÂæB–æFW‚ôÖ—'&÷"†6†W2âFööÇ2öWf–FVæ6Rö÷&–VçFF–öåöFVÖòç–'Vç2öæÇ’gFW"F†Rf–æÂWf–FVæ6R6¶VÆWFöâW†—7G2â&VÆV6RfÆ–FF–öâF†Vâ&VG2F†R&W7VÇF–ær'—FW2æBæWfW"&VvVæW&FW2õ2ÖFW&–Âà ¤f–ÆVB6¶WBfÆ–FF÷"ÂGWÆ–6FR÷"Ö—76–ær&V6÷&BÂ†—7F÷&–6ÂÖ'—FR6†ævRÂWFFW"f–ÇW&RÂ÷&–VçFF–öâf–ÇW&RÂF‚×&ööbf–ÇW&RÂ6†V6·7VÒf–ÇW&RÂ÷"&VÆV6R×7FvRf–ÇW&R&Æö6·2F†Rv†öÆR"Óe"Ô"–çFVw&F–öââæò'F–ÂvVæW&FVB6WB—26öÖÖ—GFVBà ¢222&÷r×7V6–f–27W÷'F&–Æ—G’&VF–6FW0 ¦7W÷'F&ÆRg&öÒ&WòWf–FVæ6VÖ’&R7FFVBf÷"&÷röæÇ’v†VâWfW'’&VF–6FRf÷"F†B&÷r—26F—6f–VBà §Âc’&÷rÂ&WV—&VB&VF–6FW2À§Â¢ÒÒÒÒÂ¢ÒÒÒÒÀ§Â„DRÔD•5CãFÂæòW†V7WF&ÆR'&–FvRF‚&VÖ–ç2–â7F—fR6÷W&6S²&WF—&VB¶W—2&VgW6R&Vf÷&R&÷f–FW"6öç7G'V7F–öâ÷"’ôó²F†RF—&V7B×6VÆV7F–öâ&–Ö'’—256²F—&V7B÷7GW&R&–Ö&–W2&R7W'&VçBæB66†VÖ×fÆ–C²õ2Ó2—256²w&çG2Â6V&6‚F‚ÂDDÂö6öç7G&–çBÂ&÷VæF'’×f–WrÂæB'F—F–öâö'6W'fF–öç26F—6g’7W'&VçB&VF–6FW3²6V7&WBfÇVW2&R'6VçC²WfW'’&WV—&VBF‚—2–æFW†VBæBÖW&vV&ÆRâÀ§Â„DRÔD•5CãfÂÆÂæ–æWFVVâÖæFF÷'’7FvW2'Vâ–âW†7B÷&FW"g&öÒF†R6æöæ–6ÂVçG'—ö–çC²æöæR—26¶—VC²WfW'’7FvR&W÷'G2—G2W‡V7FVB7V66W726öFS²F†R—VÆ–æRW&f÷&×2æòõ2÷"W‡FW&æÂ’ôó²7W'&VçBæB†—7F÷&–6Â6VÖçF–72&VÖ–âF—7F–æ7C²6æöæ–6Â¥4ôâÂFWFW&Ö–æ—6ÒÂ&–Ç2ÂWFFW"ÂF‚ÂÖ—'&÷"ô–æFW‚†6‚ÂF÷öÆöw’ÂæBf–æÂÔÄb6†V6·272âÀ§Â„DRÔD•5Cã–ÂF†R&÷rv÷&F–ær—2F÷FVB2F—&V7B6öææV7F—f—G’æB&WF—&VB×G&ç7÷'BVæf÷&6VÖVçC²†VÇF‡’F—&V7B6VÆV7F–öâ7V66VVG2F‡&÷Vv‚7–6÷v²Ö—76–ær÷"Væf–Æ&ÆRF—&V7B66W72f–Ç26Æ÷6VC²WfW'’&WF—&VB¶W’Â–æ6ÇVF–ærâV×G’fÇVRÂ&VgW6W2&Vf÷&R&÷f–FW"GFV×C²ÇFW&æFRGFV×G2&R¦W&ó²õ2Ó2&÷fW2F—&V7B&VBÖöæÇ’÷7GW&S²DDÂ6ö×&—6öâ6Æ–×2öæÇ’F†Rc&ö¦V7F–öã²æò7W'&VçB'&–FvR&—G’÷"fÆÆ&6²6Æ–Ò&VÖ–ç2âÀ§Â„DRÔD•5CãÂW†—7F–ærÆö6ÂÖVBÖ66†RæBõ2Ó"fÆ–FF÷'273²w&—FR÷&VBÖ&6²&—G’Â–FV×÷FVæ6RÂ6Æ÷6VB×&–Ç2&VgW6ÂÂæò&rfVæF÷"W'6—7FVæ6RÂæB6V7&WB6fWG’&VÖ–â&÷fVã²F†RÆö6ÂvVæW&F÷"–×÷'G2æò&WF—&VB&÷f–FW"æBW&f÷&×2æòÆ—fR&÷f–FW"÷"fVæF÷"’ôó²7W'&VçB&–æF–æw2&VÖ–â6ö×ÆWFRâÀ§Â„DRÔD•5CRã&ÂWfW'’æWr&–Ö'’æB66†VÖ†2W†7FÇ’öæR‡VÖâ–æFW‚&÷ræBöæRÖ6†–æRÖ—'&÷"&÷rÂF†R6÷'&V7B6–&Æ–ærF‚&ööbÂ6÷'&V7B6†V6·7VÒæB†6‚Æ–æ¶vRÂæBWF†÷&—¦VB&V6÷&BÖVæ–æs²†—7F÷&–6Â&–Ö&–W2&WF–âW†7B6†V6·7V×3²æòGWÆ–6FRÂ÷'†âÂÖçVÆÇ’w&—GFVâ6ö×æ–öâÂ–væ÷&VB&WV—&VBf–ÆRÂ÷"F‚÷66†VÖö†6‚f–ÇW&RW†—7G3²WFFW"æB÷&–VçFF–öâ÷&FW&–ær—2&÷fVââÀ ¤6ö×ÆWFVB&÷rÖ’&R&V6öÖÖVæFVB–æFWVæFVçFÇ’öbâ–æ6ö×ÆWFR&÷râf–ÇW&Röb&÷r&VF–6FRÆVfW2F†B&÷rVæ6†ævVBæB&ö†–&—G27W÷'F&–Æ—G’6Æ–Òf÷"F†B&÷rà ¢222ÆFW"7FGW2÷7GW&P ¤öæÇ’gFW""Óe"Ô"—2ÖW&vVBæBf–æÂ&Wf–Wr7W÷'G2F†RW†7B&÷rÖ’6W&FRc’Ö–çFVææ6R7F–öâ6öç6–FW#  ¢¢„DRÔD•5CãF¢'F–ÆFòFöæV ¢¢„DRÔD•5Cãf¢'F–ÆFòFöæV ¢¢„DRÔD•5Cã–¢'F–ÆFòFöæVVæFW"F†RÖVæFVBF—FÆR ¢¢„DRÔD•5Cã¢÷F–öæÆFòFöæV ¢¢„DRÔD•5CRã&¢'F–ÆFòFöæV  ¥F†W6R&R÷FVçF–ÂÆFW"7F–öç2Âæ÷B6†ævW2ÖFR'’F†—2FFVæGVÒÂF†R5$BÂ–×ÆVÖVçFF–öâÂõ2Â÷"à ¢222&öÆÆ&6²æBf–ÂÖ6Æ÷6VB÷7GW&P ¥"Óe"Ô&öÆÆ&6²Ö’F—6&ÆRFF&6RVçG'—ö–çG2÷"&WfW'BFòæ÷F†W"F—&V7BÖöæÇ’6öÖÖ—Bâ—BÕU5BäõB&W7F÷&R'&–FvR6VÆV7F–öâà ¤ç’õ2Ó2&RÖÆVæ6‚WF†÷&—¦F–öâÂ6÷W&6RÂ÷"&–ÂÖ—6ÖF6‚&öGV6W2æòFF&6R6ÆÂâç’÷7BÖÖ&¶W"f–ÇW&R6öç7VÖW2F†RWF†÷&—¦F–öâÂ&öGV6W2öæÇ’â–æFÖ—76–&ÆRFV×÷&'’f–ÇW&R&V6V—BÂæB&WV—&W2æWròÖ&÷fVB'—FW2f÷"æ÷F†W"GFV×Bà ¥"Óe"Ô"&öÆÆ&6²&VÖ÷fW2F†R&÷÷6VB7W'&VçBWf–FVæ6R&–æF–æw2æBvVæW&FVB6WBFöÖ–6ÆÇ’v†–ÆR&WF–æ–ærF†RF—&V7BÖöæÇ’'VçF–ÖRæBÆÂ†—7F÷&–6Â&–Ö&–W2âWfW'’c’7FGW2&VÖ–ç2Væ6†ævVBâ'&–FvR&—G’—2æWfW"&W7F÷&VB2&öÆÆ&6²÷"6Æ÷7W&RF‚à ¢222W&ÖæVçBG&–ævRF&vWG0 ¤G&–âF†—2FV6—6–öâ–çFó  ¢¢¢¤6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ¢¢ÂW†7B&÷w2„DRÔD•5CãFæB„DRÔD•5Cã–Âf÷"F†R6VÖçF–2ÖVæFÖVçG2â ¢¢¢¤6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ¢¢Â&÷w2„DRÔD•5CãfÂ„DRÔD•5CãÂæB„DRÔD•5CRã&ÂöæÇ’f÷"FWVæFVæ7’ÂWf–FVæ6RÂæBÆFW"7FGW2Öæ÷FRG&–ævRâ ¢¢F†RæW‡BWF†÷&—¦VB–×ÆVÖVçFF–öâÆâ&Wf—6–öâÂf÷"CÂC‚ÂCÂC"ÂC2Â"ÓbÂõ2ÓÂæBõ2Ó"÷væW'6†—æBFWVæFVæ7’6†ævW2à ¥W&ÖæVçBG&–ævR÷&FW"—2F—&V7BÖöæÇ’'VçF–ÖRæBWf–FVæ6R–×ÆVÖVçFF–öâÂf–æÂ7W÷'B&Wf–WrÂF†Vâc’v÷&F–æræBç’6W&FVÇ’&÷fVB&÷r7FGW2Ö–çFVææ6RâÆÂVç&VÆFVBc’6öçFVçB&VÖ–ç2Væ6†ævVBà ¢222W‡Æ–6—Bæöæ6Æ–×0 ¥F†—2FFVæGVÒFöW2æ÷B&Wf—6RF†RÆâÂ–×ÆVÖVçB"Óe"Ô÷""Óe"Ô"Â&÷fR÷"W†V7WFRõ2Ó2Â7&VFR52Â6F—6g’Fö¶VâÂÖ÷fRc’7FGW2Â6†ævRFF&6R÷"&öGV7B–ÆöBÂFWÆ÷’ÂÖ–w&FRÂWFFRF†R&ö&BÂ66WBF†R&VÖVF–F–öâ6Æ–6RÂ6ö×ÆWFR„DRÔU”33‚Â÷"W&f÷&Ò6Æ÷6V÷WBà ¢ÒÒÐ ¥"Â33cb—2ÖW&vVBÂæBÆö6ÂÖ–æ—27W'&VçBBÖW&vR6öÖÖ—BfSc–CvsvcS3–Cs3fff63S“f&CSfvCF“âæò&W÷6—F÷'’f–ÆRv2ÖöF–f–VBf÷"F†RFFVæGVÒà ¢22"ãb’„DRÔU”33‚"Óe"ÔÖW&vR(	B66Æ&ÆRÖæ–fW7BÔFW&—fVB&VÆV6R–FVçF—G’ÂW‡FW&æÂGFW7FF–öâÂæB÷'F&ÆRWf–FVæ6R6VÖçF–70 ¢¢¥F–ÖW7F×¢¢¢s#3#bƒ£3 ¢¢¤FWF–Ç3¢¢¢F†R&öGV7B÷væW"WF†÷&—¦VB–×ÆVÖVçFF–öâöbF†R66Æ&ÆR&VÆV6RÖöFVÂæB—G2&÷VæFVB6æöâ6öç6WVVæ6W2GW&–ærf–æÂ&VÖVF–F–öâöb„DRÔU”33‚"Óe"Ôâ"Â33cbÖW&vVB–çFòÖ–æv—F‚f–æÂ6÷W&6R†VBf#“f6F3scƒƒs–CfC–6S#“#c“Scc“ƒ&æBÖW&vR6öÖÖ—BfSc–CvsvcS3–Cs3fff63S“f&CSfvCF“âF†—2FFVæGVÒ&V6÷&G2F†R&W7VÇF–ær&VÆV6RÖ–FVçF—G’ÂGFW7FF–öâÂg&÷¦VâÖWf–FVæ6RÂ&Vv—7G'’ÖWf–FVæ6RÂF‚×&ööbÂæBvVæW&FVBÖf–ÆR&6†—FV7GW&R2Æ—f–ærcG'WF‚VæF–ærW&ÖæVçBG&–ævRà ¢2226æöâVffV7BæB7WW'6W76–öâ&÷VæF' ¤f÷"F†RW†7BF÷–72&VÆ÷rÂF†—2ÆFW"FFVæGVÓ  ¢¢¢¤ÔTäE2¢¢FFVæGVÒ"ã(	—2&VÆV6RÖ–FVçF—G’æB6öÖÖ—GFVBÖ6Æ÷7W&RÖV6†æ–72â ¢¢¢¤ÔTäE2¢¢FFVæGVÒ"ã^(	—2&VÆV6R×6æ—G’ÖV6†æ–72v—F†÷WB6†æv–ær—G2æ–æWFVVâ×7FvRf–æÂFÖ—76–öâ÷&FW"÷""Óe"ÔÓâõ2Ó2Óâ"Óe"Ô&÷væW'6†—6WVVæ6Râ ¢¢¢¥5UU%4TDU2¢¢ç’V&Æ–W"c÷"W&ÖæVçBÖ6æöâ6ÆW6RF†B&WV—&W3¢ ¢¢vVæW&FVB&VÆV6RÔ”B6÷W&6R6öç7FçC² ¢¢6†V6¶VBÖ–â&VÆV6RFW&—fF—fW2Fò&R&VvVæW&FVB'’WfW'’&VÆV6R7WC² ¢¢6÷W&6R×G&VRW†V7WF–öâöbw&—FRÖ6&ÆR–FVçF—G’Ö6Æ÷7W&R&ö6W73² ¢¢6ÆöæRÖÆö6Âf–ÆW7—7FVÒ×F–ÖRWVÆ—G’2F‚×&ööb6÷'&V7FæW72&VF–6FS²÷" ¢¢&VÆV6RÖÖæ–fW7B–FVçF—G’Fò&RVÖ&VFFVB–æ6–FVçFÆÇ’–â&Vv—7G'’ö6öæf–wW&F–öâWf–FVæ6Rà ¤FFVæF"ã"F‡&÷Vv‚"ãR&VÖ–â6öçG&öÆÆ–ærf÷"F—&V7BÖöæÇ’FF&6R6VÆV7F–öâÂ&WF—&VBÖ¶W’&VgW6ÂÂ†—7F÷&–6Â'&–FvRV&çF–æRÂõ2Ó2Âc’ãb6VÖçF–72ÂæB"Óe"÷væW'6†—W†6WBv†W&RF†—2FFVæGVÒW‡&W76Ç’6†ævW2&VÆV6R÷"F‚×&ööbÖV6†æ–72à ¢2226–ævÆR&VÆV6RÖ–FVçF—G’6÷W&6P ¦6FÆöröÖæ–fW7Bæ§6öæ—2F†R6–ævÆR&VÆV6RÖ–FVçF—G’–çWB7F÷&VB–âv—Bà ¤—G2F÷ÖÆWfVÂ¶W—2&RW†7FÇ“  ¢¢&ö÷F ¢¢fW'6–öæ ¢¢'V–ÇEöE÷WF6 ¢¢f–ÆW6  ¥F†RÖæ–fW7BFöW2æ÷BÆ—7B—G6VÆbâ—G2'—FW2&R6æöæ–6ÂUDbÓ‚v—F‚44”’×6÷'FVBö&¦V7B¶W—2Â6ö×7B6W&F÷'2Âæò$ôÒÂæBW†7FÇ’öæRG&–Æ–ærÄbà ¥F†R&VÆV6R–FVçF—G’—3  ¦&VÆV6Uö–BÒ6†#Sb†6æöæ–6Åö'—FW2†6FÆöröÖæ–fW7Bæ§6öâ’–  ¥'VçF–ÖR&VG2F†R6¶vVBÖæ–fW7Böæ6RæBFW&—fW2F†R&VÆV6R”BF—&V7FÇ’g&öÒF†÷6R'—FW2â'VçF–ÖRFöW2æ÷B&VBWf–FVæ6RF‡2Â&VÆV6RÖ–FVçF—G’Vçf—&öæÖVçBf&–&ÆW2ÂvVæW&FVB6öç7FçG2Â÷"×WF&ÆRGFW7FF–öâf–ÆW2à ¤æ÷&ÖÂ&VÆV6R7WBW6W3  ¦—F†öâ67&—G2ö7WE÷&VÆV6UöÖæ–fW7Bç’Ò×fW'6–öâÇ6V×fW#âÒÖ'V–ÇBÖB×WF2ÅUD3æ  ¥F†R7WB&Vg&W6†W2F†RFV6Æ&VBf–ÆR†6†W2æB6†ævW2öæÇ’6FÆöröÖæ–fW7Bæ§6öæà ¥6÷W&6RfÆ–FF–öâ—2&VBÖöæÇ“  ¦—F†öâ67&—G2÷&VÆV6Uö–E÷&V6ö×WFRç’ÒÖ6†V6²ÖÖæ–fW7BÖöæÇ–  ¤v—B6öÖÖ—BFöW2æ÷B–æ†W&VçFÇ’6†ævRF†R&VÆV6R”BâF†R&VÆV6R”B6†ævW2öæÇ’v†VâF†R6æöæ–6ÂÖæ–fW7B'—FW26†ævRâ6†ævRFòÖæ–fW7BÖÆ—7FVB6÷W&6Rf–ÆR6W6W2F†R&VBÖöæÇ’VF—BFòf–ÂVçF–ÂöæR–çFVçF–öæÂf–æÂ7WB—2ÖFRgFW"6÷W&6R7F&–Æ—¦F–öâà ¢2227–6Æ–2&VÆV6Rw&€ ¥F†R&WV—&VBFWVæFVæ7’F—&V7F–öâ—3  ¦G&6¶VB6÷W&6RÓâ6æöæ–6ÂÖæ–fW7BÓâ&VÆV6R”BÓâW‡FW&æÂGFW7FF–öæ  ¤æòVFvRÖ’ö–çBg&öÒvVæW&FVBGFW7FF–öâ&6²–çFòG&6¶VB6÷W&6Rà ¤Öæ–fW7B7WB—2F†W&Vf÷&RF†RFW&Ö–æÂG&6¶VB&VÆV6RÖ–FVçF—G’6†ævRâ—BFöW2æ÷B&WV—&RvVæW&FVB—F†öâ6öç7FçBÂ&VvVæW&FVB6†V6¶VBÖ–â&VÆV6RWf–FVæ6RÂ÷"&V7W'6—fR–æFW‚ôÖ—'&÷"6‡W&âà ¢222W‡FW&æÂ&VÆV6RGFW7FF–öà ¤7W'&VçB&VÆV6RÖ&÷VæBFW&—fF—fW2&RvVæW&FVBöæÇ’F‡&÷Vvƒ  ¦—F†öâFööÇ2öWf–FVæ6Rö'V–ÆE÷&VÆV6UöGFW7FF–öâç’ÒÖ÷WGWBÆW‡FW&æÂÖV×G’ÖF—&V7F÷'“âÒ×&WV—&RÖ6ÆVæ  ¥F†R'V–ÆFW#  ¢¢&WV—&W2âW†7B6ÆVâ6÷W&6R6öÖÖ—C² ¢¢&VgW6W2â÷WGWBF‚–ç6–FRF†R6÷W&6R&W÷6—F÷'“² ¢¢&VgW6W2æöâÖV×G’FW7F–æF–öâæBFöW2æ÷B÷fW'w&—FRW†—7F–ær÷WGWC² ¢¢7&VFW2â—6öÆFVBG&6¶VBÖf–ÆR6÷“² ¢¢'Vç2F†R&WV—&VBÆVv7’&öGV6W"6Æ÷7W&RöæÇ’–ç6–FRF†B—6öÆFVB6÷“² ¢¢&÷fW26V6öæB&VBÖöæÇ’f—†VBö–çC² ¢¢fÆ–FFW2F†R"Ô&VÆV6R×6æ—G’&÷VæF'“² ¢¢W6W2âÆÆ÷vÆ—7FVBÂ6Æ÷6VB×&–Ç26†–ÆBVçf—&öæÖVçC² ¢¢W†6ÇVFW2FF&6RÂ'&–FvRÂfVæF÷"Â7&VFVçF–ÂÂæBVç&VÆFVB•D„ôâ¦Vçf—&öæÖVçBæÖW3²æB ¢¢ÆVfW2F†R6÷W&6R6†V6¶÷WB'—FR×7F&ÆRà ¤F—&V7B6÷W&6R×G&VRW†V7WF–öâöb&VvVæW&FUö–FVçF—G•ö6Æ÷7W&Rç–—2&ö†–&—FVBâF†B–×ÆVÖVçFF–öâ—2–çFW&æÂFòF†R—6öÆFVBGFW7FF–öâ'V–ÆBöæÇ’à ¥F†R7V66W726öçG&7B—2†FRç&VÆV6UöGFW7FF–öâçcâF†Rf–ÇW&R6öçG&7B—2†FRç&VÆV6UöGFW7FF–öâæf–ÇW&Rçcà ¤7V66W76gVÂ'VæFÆR&–æG2BÆV7C  ¢¢F†RW†7B6÷W&6R6öÖÖ—C² ¢¢FWFW&Ö–æ—7F–2G&6¶VB×G&VRF–vW7C² ¢¢6æöæ–6ÂÖæ–fW7BæB&VÆV6R–FVçF—G“² ¢¢6÷'FVBf–ÆR–çfVçF÷'’v—F‚†6†W2æB6—¦W3² ¢¢FWFW&Ö–æ—7F–27FvRö6öÖÖæBöW†—BÖ6öFRG&ç67&—Bf7G3² ¢¢6æöæ–6Â6†V6·7V×3²æB ¢¢F†RW†7B"Ô&VÆV6RÖFÖ—76–öâ÷7GW&Rà ¥F–Ö–ærÂ&r7V'&ö6W72÷WGWBÂ6V7&WG2ÂE4ç2ÂfVæF÷"fÇVW2ÂæBFF&6Rö'6W'fF–öç2&Ræ÷B&WF–æVB2GFW7FF–öâ6öçFVçBâ&WVFVB'V–ÆG2f÷"F†R6ÖRW†7B6÷W&6R×W7B&öGV6RF†R6ÖR6öçFVçBG&VRà ¤4’'V–ÆG2æB–æFWVæFVçFÇ’fW&–f–W2F†—2'VæFÆR÷WG6–FRF†R6÷W&6RG&VRæBV&Æ—6†W2—Bv—F‚&÷VæFVB&WFVçF–öââF†R4’'F–f7B—2W†7BÖ†VB"Wf–FVæ6RÂæ÷BGW&&ÆRv÷fW&æVB&VÆV6RFÖ—76–öâ&V6÷&BæBæ÷B&WÆ6VÖVçBf÷""Óe"Ô"à ¢2222g&÷¦Vâ6†V6¶VBÖ–â&VÆV6RWf–FVæ6P ¤W†—7F–ær6†V6¶VBÖ–âU”3#"&VÆV6RWf–FVæ6RæB—G26ö×æ–öç2&Rg&÷¦Vâ6GW&R×F–ÖR&V6÷&G2à ¥F†W“  ¢¢&Ræ÷B7W'&VçB'VçF–ÖR–FVçF—G’–çWG3² ¢¢&Ræ÷B&VvVæW&FVBf÷"V6‚ÆFW"&VÆV6S² ¢¢&WF–âF†V—"†—7F÷&–6Â&öGV6W"æB6GW&RÖVæ–æs² ¢¢×W7Bæ÷B&R&VÆ&VÆVB27W'&VçB&VÆV6RGFW7FF–öç3² ¢¢×W7Bæ÷B&R&Vg&W6†VBÖW&VÇ’&V6W6RF†RÖæ–fW7B÷"&VÆV6R”B6†ævW3²æB ¢¢&VÖ–â7V&¦V7BFòF†V—"W†—7F–ær†—7F÷&–6Â–çFVw&—G’Â6V7&WB×6fWG’ÂæB6æöæ–6ÂÖ'—FR6†V6·2à ¤7W'&VçB&VÆV6R&÷fVææ6R&VÆöæw2FòF†RW‡FW&æÂGFW7FF–öââ†—7F÷&–6Â6†V6¶VBÖ–âWf–FVæ6R&VÖ–ç2†—7F÷&–6Âà ¢2222&Vv—7G'’æB6öæf–wW&F–öâWf–FVæ6P ¦'F–f7G2÷&Vv—7G'’÷&Vv—7G'•÷&W÷'Bæ§6öæ—26öæf–wW&F–öâWf–FVæ6RÂæ÷B&VÆV6RÖ–FVçF—G’Wf–FVæ6Rà ¤—G2ÆöFW"6öçF–çVW2FòfÆ–FFRF†R6æöæ–6ÂÖæ–fW7BæB6FÆör6öçG&7B&Vf÷&R&öGV6–ærF†R&W÷'BâF†R&W÷'B—G6VÆb&–æG2öæÇ’&Vv—7G'’ö6FÆör6öæf–wW&F–öâ–çWG2â—B×W7Bæ÷BVÖ&VBF†RÖæ–fW7BF–vW7BÂ&VÆV6R”BÂ÷"Öæ–fW7BÖÆ—7FVB6÷W&6RÖf–ÆR–FVçF—F–W22–æ6–FVçFÂ&÷fVææ6Rà ¤6öæf–r'VæFÆW2FW&—fVBg&öÒF†R&Vv—7G'’&W÷'B–æ†W&—BF†—2&VÆV6RÖvæ÷7F–2÷7GW&Râ&VÆV6R7WB×W7Bæ÷B6‡W&ââ÷F†W'v—6RVæ6†ævVB&Vv—7G'’&W÷'BÂ—G2'VæFÆW2Â÷"F†V—"–æFW‚ôÖ—'&÷"6ö×æ–öç2à ¥&VÆV6RæB6÷W&6R&÷fVææ6R&VÆöærFòF†RW‡FW&æÂGFW7FF–öâà ¢2222÷'F&ÆRF‚×&ööb6VÖçF–70 ¤v—BFöW2æ÷B&W6W'fRf–ÆW7—7FVÒ×F–ÖW2â6ÆöæRÖÆö6Â7FB‚’ç7Eö×F–ÖV—2F†W&Vf÷&Ræ÷BWf–FVæ6RæB×W7Bæ÷BFWFW&Ö–æRv†WF†W"v÷fW&æVBF‚&ööb—2fÆ–Bà ¥F‚×&ööb6÷'&V7FæW72—2W7F&Æ—6†VB'“  ¢¢W†7Bv÷fW&æVBFƒ² ¢¢W†7B4„Ó#Sc² ¢¢W†7B6—¦S² ¢¢&WV—&VB6ö×æ–öâf–VÆG3² ¢¢6æöæ–6Âf–VÆB7G'V7GW&S²æB ¢¢fÆ–BUD2F–ÖW7F×6†Rà ¦×F–ÖU÷WF6&VÖ–ç26GW&R×F–ÖR&÷fVææ6RæBÖ’6VVBæWvÇ’&öGV6VB&ööbâ—B—2æ÷B6ö×&VBv—F‚ÆFW"6†V6¶÷WN(	—2f–ÆW7—7FVÒ×F–ÖRââVæ6†ævVB&ööb×W7Bæ÷B&R&Ww&—GFVâ÷"&R×F–ÖW7F×VBÖW&VÇ’FòÖ¶R6ÆöæRÂ66†R&W7F÷&RÂ÷"4’6†V6¶÷WB72à ¤f÷"F†—2W†7B÷'F&–Æ—G’66÷RÂF†—2FFVæGVÒ7WW'6VFW26öæfÆ–7F–ær6ÆöæRÖÆö6Â×F–ÖR6ö×&—6öâ&WV—&VÖVçG2–â¢¤„DR66†VÖ2æB'F–f7G2¢¢Â¢¤„DRÖV6†æ–72wV–FR¢¢ÂæB¢¤vÆ÷rwV–FR¢¢âF†V—"F‚Â†6‚Â6—¦RÂ66†VÖÂ÷væW'6†—Â6æöæ–6ÂÖvVæW&F–öâÂæBæòÖ†æBÖVF—B&WV—&VÖVçG2&VÖ–âVæ6†ævVBà ¢2222vVæW&FVBFWfVÆ÷ÖVçBæB6¶v–ærf–ÆW0 ¤†÷7B×7V6–f–2vVæW&FVBFWfVÆ÷ÖVçBf–ÆW2&Ræ÷B6÷W&6Rà ¤Æö6ÂçfVçfG&VW2æBvVæW&FVB¢æVvrÖ–æföÖWFFF×W7B&VÖ–â–væ÷&VBæBVçG&6¶VBâFWVæFVæ7’–ç7FÆÆF–öâ÷"VF—F&ÆR×6¶vR–ç7FÆÆF–öâ×W7Bæ÷BF—'G’F†RG&6¶VB&W÷6—F÷'’÷"ÇFW"&VÆV6R–FVçF—G’à ¤G&6¶VBf—'GVÂÖVçf—&öæÖVçB&ö÷B÷"G&6¶VBvVæW&FVB6¶vRÖWFFF—2&W÷6—F÷'’6öçFÖ–æF–öâæB×W7Bf–Â6÷W&6RÖ–çfVçF÷'’÷"6ÆVâ×G&VRfÆ–FF–öâà ¢2222"Óe"Ô–×ÆVÖVçFF–öâ&V6÷&@ ¥"Â33cb–×ÆVÖVçFVBF†—2&6†—FV7GW&RFövWF†W"v—F‚F†R&÷fVBF—&V7BÖöæÇ’&VÖVF–F–öâà ¥F†Rf–æÂ&Wf–WvVB†VBv3  ¦f#“f6F3scƒƒs–CfC–6S#“#c“Scc“ƒ&  ¥F†RÖW&vVBÖ–æ6öÖÖ—B—3  ¦fSc–CvsvcS3–Cs3fff63S“f&CSfvCF“  ¤W†7BÖ†VBfÆ–FF–öâ–æ6ÇVFVC  ¢¢&W÷6—F÷'’Ö6öæf–wW&VBFW7G3¢3R76VBÂ26¶—VC² ¢¢F—&V7BÖöæÇ’FF&6RÂ6ö×F–&–Æ—G’ÂÖVBÖ66†RÂ&VgW6ÂÂæBæòÔ’ôòFW7G3¢#S76VC² ¢¢Wf–FVæ6RÂ66†VÖ2Â6æöæ–6ÂvVæW&F–öâÂõ2Ó2f—‡GW&Rö×WFF–öâÂæB—VÆ–æRFW7G3¢ÃS276VC² ¢¢7G&–7BW‡FW&æÂGFW7FF–öâ'V–ÆBæB–æFWVæFVçBfW&–f–6F–öã² ¢¢Öæ–fW7BÖöæÇ’fÆ–FF–öã² ¢¢6öæf–r'F–f7BæB'VæFÆR6†V6·3² ¢¢‡VÖâ–æFW‚æBÖ6†–æRÖ—'&÷"6†V6·3² ¢¢F‚Â†6‚Â6æöæ–6Â¥4ôâÂf–æÂÔÄbÂFWVæFVæ7’Â6W&–Æ—¦W"ÂVÖ—GFW"ÂæBF—&V7B×6÷W&6RvFW3²æB ¢¢v—D‡V"7F–öç2'Vâ3SSCƒVÂv—F‚ÆÂ6WfVâ¦ö'27V66W76gVÂà ¥F†Rf–æÂW†7BÖ†VB&Wf–Wr&W÷'FVBæòf–æF–æw2ÂæBWfW'’–æÆ–æR&Wf–WrF‡&VBv2&W6öÇfVB&Vf÷&RÖW&vRà ¢2222"ÔæBF÷vç7G&VÒ&VÆV6R&÷VæF' ¥F†R"ÔGFW7FF–öâ&V6÷&G3  ¢¢&VÆV6UöFÖ—76–öãÔäõEôEDTÕDTF²æB ¢¢7FvRÓB7F÷%ööæöæf–æÅö÷35÷%ö%ö&–æF–æu÷&WV—&VFà ¥"ÔFöW2æ÷BW†V7WFRõ2Ó2Â7&VFR÷"–×÷'BÆ—fRõ2Ó26¶WBÂ66W72&–Çv’Âw&—FRFF&6RÂ÷"FÖ—Bf–æÂF—&V7BÖöæÇ’&VÆV6RWf–FVæ6Rà ¥F†RÖæFF÷'’6WVVæ6R&VÖ–ç3  £âÖW&vR"Óe"Ô6÷W&6RæBFööÆ–ærâ £"â&÷fRW†7Bõ2Ó2WF†÷&—¦F–öâ'—FW2&÷VæBFòF†RÖW&vVB"Ô6÷W&6Râ £2âW†V7WFRõ2Ó2öæ6RVæFW"F†RWF†÷&—¦F–öâÖ&÷VæBF—&V7B&VBÖöæÇ’6öçG&7Bâ £Bâ–æFWVæFVçFÇ’fÆ–FFRæBFÖ—BF†R6¶WBâ £RâW&f÷&Ò"Óe"Ô"W†7BÖ'—FR6÷’æB6æöæ–6ÂWf–FVæ6R&–æF–ærâ £bâ'VâF†R6æöæ–6ÂWFFW"æBf–æÂ7FvW2RF‡&÷Vv‚•Ââ £râ6öæGV7Bf–æÂFV6†æ–6ÂæBWf–FVæ6R&Wf–Wrâ £‚âW&f÷&Ò6W&FVÇ’WF†÷&—¦VBW&ÖæVçB6æöâG&–ævRæBç’c’Ö–çFVææ6Rà ¥F†RW‡FW&æÂ"ÔGFW7FF–öâFöW2æ÷B6F—6g’õ2Ó2Â"Óe"Ô"ÂF†Rf–æÂæ–æWFVVâ×7FvR&VÆV6R52Â÷"ç’c’&VF–6FR'’—G6VÆbà ¢2222&öÆÆ&6° ¥&öÆÆ&6²×W7B&WfW'BF†R'VçF–ÖRÖæ–fW7BFW&—fF–öâÂ&VÆV6RÖ7WB6öÖÖæBÂ—6öÆFVBGFW7FF–öâ'V–ÆFW"Âv÷&¶fÆ÷rV&Æ–6F–öâÂ66†VÖ2ÂæBF†—2&6†—FV7GW&ÂFV6—6–öâFövWF†W"à ¥&öÆÆ&6²×W7Bæ÷B&W7F÷&S  ¢¢vVæW&FVB&VÆV6RÔ”B6öç7FçC² ¢¢6÷W&6R×G&VR–FVçF—G’Ö6Æ÷7W&Rw&—FW3² ¢¢&V7W'6—fR6†V6¶VBÖ–âFW&—fF—fR&VvVæW&F–öã² ¢¢6ÆöæRÖÆö6Â×F–ÖR6÷'&V7FæW726†V6·3² ¢¢&VÆV6R–FVçF—G’–ç6–FR&Vv—7G'’ö6öæf–wW&F–öâWf–FVæ6S²÷" ¢¢'&–FvR6VÆV7F–öâ÷"'&–FvRÖW&7W'&VçBÖWf–FVæ6R6VÖçF–72à ¤–bW‡FW&æÂGFW7FF–öâV&Æ–6F–öâ—2Væf–Æ&ÆRÂF†RGFW7FF–öâ¦ö"f–Ç2v†–ÆRG&6¶VB6÷W&6RæBF†R6æöæ–6ÂÖæ–fW7B&VÖ–â–Ö×WF&ÆRà ¢2222W&ÖæVçBG&–ævRF&vWG0 ¤G&–âF†—2FV6—6–öâ–çFó  ¢¢¢¤„DR66†VÖ2æB'F–f7G2¢¢Âf÷"F†R&VÆV6RÖGFW7FF–öâ66†VÖ2ÂW‡FW&æÂ÷væW'6†—Âg&÷¦Vâ6†V6¶VBÖ–â&VÆV6RWf–FVæ6RÂ&Vv—7G'’ö6öæf–rWf–FVæ6R6W&F–öâÂæB÷'F&ÆRF‚×&ööb6VÖçF–73² ¢¢¢¤„DRÖV6†æ–72wV–FR¢¢Âf÷"F†RÖæ–fW7BÖöæÇ’&VÆV6R7WBÂ&VBÖöæÇ’6÷W&6RVF—BÂ—6öÆFVBW‡FW&æÂ'V–ÆFW"Â6ÆVâ×G&VR&WV—&VÖVçBÂæB&öÆÆ&6²ÖV6†æ–73² ¢¢¢¤vÆ÷rwV–FR¢¢Âf÷"W†7BÖ†VB4’GFW7FF–öâfW&–f–6F–öâÂæò6÷W&6R×G&VR&W—"GW&–ær6†V6·2ÂFWFW&Ö–æ—7F–2&WG'’–FVçF—G’Â÷'F&ÆRF‚×&ööbfÆ–FF–öâÂæBvVæW&FVBÖf–ÆR6ÆVæÆ–æW73² ¢¢¢¤„DRv÷fW&ææ6R¢¢Âf÷"7W'&VçB×fW'7W2Ö†—7F÷&–6Â&VÆV6RÖWf–FVæ6RÖVæ–æræBF†R'VÆRF†BâW‡FW&æÂ"'F–f7B7&VFW2æò66WFæ6RFö¶Vâ÷"&VÆV6RÖFÖ—76–öâ6Æ–Ò'’–×Æ–6F–öã²æB ¢¢¢¤6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ¢¢ÂöæÇ’f÷"ç’ÆFW"FWVæFVæ7’v÷&F–æræVVFVBFòF—7F–æwV—6‚"ÔGFW7FF–öâg&öÒõ2Ó2æB"Óe"Ô"f–æÂFÖ—76–öâà ¥W&ÖæVçBG&–ævR×W7B&W6W'fRFFVæF"ã"F‡&÷Vv‚"ã^(	—2F—&V7BÖöæÇ’FF&6RæBWf–FVæ6R&÷VæF&–W2â—B6W6W2æòWFöÖF–27FGW2Ö÷fVÖVçBà ¢2222W‡Æ–6—Bæöæ6Æ–×0 ¥F†—2FFVæGVÒFöW2æ÷C  ¢¢W†V7WFR÷"&÷fRõ2Ó3² ¢¢7&VFR÷"FÖ—BÆ—fRõ2Ó26GW&R'—FW3² ¢¢&÷fR&–Çv’–çfVçF÷'’÷"W‡FW&æÂFF&6Rf–Æ&–Æ—G“² ¢¢WF†÷&—¦RFF&6Rw&—FRÂFWÆ÷–ÖVçBÂÖ–w&F–öâÂ÷"6W'f–6R6†ævS² ¢¢W&f÷&Ò"Óe"Ô"Wf–FVæ6RFÖ—76–öã² ¢¢6Æ–ÒF†BF†Rf–æÂæ–æWFVVâ×7FvR&VÆV6R—VÆ–æR76VC² ¢¢W7F&Æ—6‚52÷"66WFæ6R×Fö¶Vâ6F—6f7F–öã² ¢¢Ö÷fRc’7FGW3² ¢¢ÖöF–g’V&Æ–2&VFW"÷"4Ä’6öçG&7C² ¢¢&Wf—6R†—7F÷&–6Âõ2ÓÂõ2Ó"Âõ2Ó"Â'&–FvRÂ÷"U”3#"6GW&Rf7G3² ¢¢66WB÷"6Æ÷6R„DRÔU”33ƒ²÷" ¢¢W&f÷&ÒW&ÖæVçBG&–ævRÖW&VÇ’'’&V6÷&F–ærF†RF&vWBà ¤ÆÂVç&VÆFVBcæBW&ÖæVçBÖ6æöâ&WV—&VÖVçG2&VÖ–âVæ6†ævVBà ¢22"ãr’"Ób&VÖVF–F–öâ„DRÔU”33‚"Óe"Ô ¢222W†V7WF—fR&Wf–Wr7VÖÖ' ¢¢F†R&÷fVB66÷R—2F—&V7BÖöæÇ’6÷W&6R6öçfW&vVæ6RÂ&WF—&VB×G&ç7÷'B&VÖ÷fÂÂÆö6ÂF—&V7B×6VÆV7F–öâWf–FVæ6RFööÆ–ærÂf—‡GW&RÖöæÇ’õ2Ó2FööÆ–ærÂæBFVÆ–&W&FVÇ’æöæf–æÂ"Ô—VÆ–æRâ ¢¢µ"Â33c5Ò†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"÷VÆÂó3c2’W7F&Æ—6†VBF†RÖ–â–×ÆVÖVçFF–öâ'WBÆVgB6ö×F–&–Æ—G’Â66ææW"ÂæBõ2Ó2†&FVæ–ærv2â ¢¢µ"Â33cEÒ†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"÷VÆÂó3cB’6VçG&Æ—¦VB6ö×F–&–Æ—G’&V†f–÷"Â7G&VæwF†VæVB66ææ–ærÂæB–çG&öGV6VBF†RW†7B"Ôæöæf–æÂvFRâ ¢¢µ"Â33cUÒ†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"÷VÆÂó3cR’6Æ÷6VB&WF—&VBÖ¶W’fÇVR×&VBæBW‡FVç6—fR66ææW"öFFÖfÆ÷rv2â ¢¢µ"Â33ceÒ†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"÷VÆÂó3cb’6Æ÷6VBF†R&VÖ–æ–ærõ2Ó2—6öÆF–öâÂf–ÆW7—7FVÒÂ7FFRÖÖ6†–æRÂfÆ–FF–öâ×&6RÂæB&VÆV6RÖWf–FVæ6RFVfV7G2â ¢¢7W'&VçB6÷W&6R6öçF–ç2öæRF—&V7B÷7Fw&U5Â6VÆV7F–öâ÷væW"ÂæòW†V7WF&ÆR'&–FvRÆæRÂ7G&–7BWf–FVæ6R6öçG&7G2ÂæBf–ÂÖ6Æ÷6VB7FvRÓBF÷vç7G&VÒ7F÷â ¢¢ÆÂf÷W"W†7BÖ†VB4’'Vç276VC²ÆÂSBÆ–æVvR&Wf–WrF‡&VG2&R&W6öÇfVC²"Â33cb&V6V—fVB6ÆVâ&Wf–Wrv–ç7B—G2W†7Bf–æÂ†VBâ ¢¢æò7W'&VçB&WV—&VÖVçBf–ÇW&RÂÖFW&–ÂVæ6W'F–çG’Â7F–öæ&ÆRf–æF–ærÂ÷"F÷vç7G&VÒÖ&÷VæF'’f–öÆF–öâ&VÖ–ç2à ¢22266÷RæB6÷fW&vR&V6÷&@ ¢22226†ævVB×F‚6÷fW&vP §ÂF–W"Â6÷VçBÂ&Wf–WvVB66÷RÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§ÂF–W"Â“ÂÆÂ&öGV7F–öâÂ&÷f–FW"Â66†VÖÂfÆ–FF÷"Â&öGV6W"Â—VÆ–æRÂv÷fW&æVB'F–f7BÂ–æFW‚öÖ—'&÷"ÂF‚×&ööbÂæBW†V7WF&ÆRÖ6ÆVçWF‡2À§ÂF–W""Âc2ÂCB&Vw&W76–öâ÷7W÷'BFW7G2æB’FV6†æ–6ÂöFWfVÆ÷W"wV–Fæ6Rf–ÆW2À§ÂF–W"2ÂRÂ&VÖ÷fVBvVæW&FVBvÆ÷uö†FVæv–æRæVvrÖ–æfòò¢¦ÖWFFFÀ§Â¢¥F÷FÂ¢¢Â¢£#S‚¢¢ÂÖF6†W2&÷F‚F†Rf÷W"Õ"Væ–öâæBF†RÆ–fV7–6ÆRÖ&6VÆ–æR×FòÖf–æÂ6ö×&—6öâÀ ¢2222F–W"w&÷W0 ¢¢'VçF–ÖR÷V&Æ–2&V†f–÷"(	BF‡3¢FFW"öF%ö66W72ç–ÂFFW"ö‡GG÷&VFW"ç–ÂæBF†Ræ–æRF÷V6†VBVæv–æRò¢¦F‡2Â–æ6ÇVF–ærF†R&VÖ÷fVB'&–FvR&÷f–FW"â ¢¢4’æB6fWG’vFW2(	BbF‡3¢æv—F‡V"÷v÷&¶fÆ÷w2ö6’ç–ÖÆÂF—&V7Bö'&–FvR6öçG&7B6†V6¶W'2ÂÖ—'&÷"6†V6¶W"ÂæB&–Ç2¦ö"FVf–æ—F–öç2â ¢¢66†VÖ2(	BF‡3¢F—&V7B×6VÆV7F–öâÂ6WfVâõ2Ó2ÂæBGvòW‡FW&æÂ×&VÆV6RÖGFW7FF–öâ66†VÖ2â ¢¢W†V7WF–öâ67&—G2(	B2F‡2VæFW"67&—G2ò¢¦Â–æ6ÇVF–ærF—&V7B÷7GW&RÂõ2Ó2ÂÖVBÖ66†RÂ&–Ç2ÂæB&VÆV6RÖ–FVçF—G’FööÆ–ærÇW2&VÖ÷fVB'&–FvRôõ2Ó"67&—G2â ¢¢&öGV6W'2ÂfÆ–FF÷'2ÂæBWFFW'2(	B‚F‡2VæFW"FööÇ2ö6öæf–rò¢¦ÂFööÇ2öWf–FVæ6Rò¢¦ÂæB&Vv—7G'’FööÆ–ærâ ¢¢6FÆörö6öæf–wW&F–öâ(	B6FÆörõõö–æ—Eõòç–Â6FÆöröÖæ–fW7Bæ§6öæÂæB—&ö¦V7BçFöÖÆâ ¢¢6÷W&6RÖ6öçFÖ–æF–öâ6ÆVçW(	Bæ–æR&VÖ÷fVBG&6¶VBçfVçbò¢¦W†V7WF&ÆW2÷7–ÖÆ–æ·2â ¢¢v÷fW&æVBFö7VÖVçFF–öâ–æFW†W2÷&öög2(	BV–v‡B–æFW‚ÂVæGö–çBÂE"ÂæB'VâÖwV–FR&ööbF‡2â ¢¢v÷fW&æVB'F–f7G2(	Bƒ’F‡3¢&6†—FV7GW&R#²VF—B#²&öG”w&‚#²4Ä’S²Wf–FVæ6RÖ–æFW‚C²–FVçF—G’c²ÖF‚s²–çFW&æÂ×fW'6–öâc²&—G’#²&öög2#²&VFW"²U”3#'VæFÆW2#C²6öæf–r'VæFÆW2C²&Vv—7G'’%Ââ ¢¢v÷fW&æVBVF—BvFW2(	B#2F‡26÷fW&–ær6æöæ–6Â¥4ôâÂFWFW&Ö–æ—6ÒÂ&VFW"ô4Ä’&—G’Â6æ—G’ÂæBF÷öÆöw’à ¤WfW'’v÷fW&æVB–ç7Fæ6Rv2&V6öæ6–ÆVBv–ç7B—G2&öGV6W"Â6æöæ–6Âf÷&ÒÂ6ö×æ–öâ÷væW'6†—Â–æFW‚öÖ—'&÷"F÷öÆöw’ÂæBW†7BÖ†VB–çFVw&—G’6†V6·2âæòF–W"F‚v2G&VFVB2–çfVçF÷'’ÖöæÇ’à ¢2222F–W""æBF–W"0 ¢¢F–W""FW7G26÷fW&VBD"6VÆV7F–öâÂ6ö×F–&–Æ—G’6†W2Â…EE&VgW6ÂÂ&VFW"ô4Ä’&V†f–÷"ÂF—&V7BWf–FVæ6RÂÖVBÖ66†R—6öÆF–öâÂõ2Ó2×WFF–öâöf–ÇW&R&V†f–÷"Â—VÆ–æRvFW2Â&VÆV6R–FVçF—G’ÂæBvVæW&FVBÖ'F–f7B6ö†W&Væ6Râ ¢¢F–W""wV–Fæ6R6÷fW&VB7W'&VçBD"W6RÂ6V7&WG2Â4Ä’÷'Vâ–ç7G'V7F–öç2Â66WFVBE'2ÂæBW‡Æ–6—FÇ’†—7F÷&–6Â'&–FvRFW6–vâ&V6÷&G2â ¢¢F–W"26öç6—7G2öæÇ’öbf—fRFVÆWFVBvVæW&FVBvÆ÷uö†FVæv–æRæVvrÖ–æfòò¢¦f–ÆW2â–çfVçF÷'’ÖöæÇ’G&VFÖVçB—26fR&V6W6R—&ö¦V7BçFöÖÆæBF†R6¶v–ærö–ç7FÆÆ&–Æ—G’vFW2vW&R&Wf–WvVBÂF†Rf–ÆW2&R†÷7BÖvVæW&FVBÂæBc*s"ãb&WV—&W2F†VÒFò&VÖ–âVçG&6¶VBà ¢2222†—7F÷'’æB&Wf–Wr6÷fW&vP ¢¢"&Wf–WrF‡&VG3¢Â33c2BóF&W6öÇfVC²Â33cB"ó&²Â33cR#ó#²Â33cbróvâ ¢¢†—7F÷&–6Â&V6öç7G'V7F–öâv2Æ–VBFòWfW'’F–W"6†ævRÂ'&–FvRFVÆWF–öâÂ&Wf–Wrf–æF–ærÂ66ææW"&VÖVF–F–öâÂõ2Ó2f–ÇW&R&÷VæF'’Â—VÆ–æRöF÷vç7G&VÒF—7WFRÂvVæW&FVBÖWf–FVæ6R6†ævRÂæB&VÆV6RÖ–FVçF—G’&VFW6–vââ ¢¢F†RöæRÆFW"6öÖÖ—Bv26W&FVÇ’6ö×&VBv—F‚F†Rf–æÂÆ–æVvRÖW&vRæB6†ævVBöæÇ’cc"ã2ãBFòc"ã2ãRâ ¢¢æöæ&Æö6¶–ær&WG&–WfÂÆ–Ö—FF–öã¢v÷&¶fÆ÷rö¦ö"w&W'2W‡÷6RF†Rf—'7BvRÂ'WBV6‚W†7B†VB&WGW&æVBöæRW‡V7FVBv÷&¶fÆ÷ræBW†7FÇ’6WfVâFW&Ö–æÂ7V66W76gVÂ¦ö'2Âv—F‚æòöÖ—GFVBW‡V7FVB¦ö"â ¢¢æòFW7G2Âõ2÷W&F–öâÂFF&6R66W72Â÷"W‡FW&æÂ×WFF–öâv2W&f÷&ÖVB'’F†—2&Wf–Wrà ¢222"Æ–æVvR7VÖÖ' ¢2222÷&–v–æÂ"Â33c0 ¢¢¢¥F—FÆS¢¢¢"Óe"Ô¢6öçfW&vR„DRD"6VÆV7F–öâöâF—&V7B7–6÷v ¢¢¢¤ÖW&vR–FVçF–f–W#¢¢¢c†&v&&fVcvSVc3&3ƒCvF&F#F3#Svc#&Ss– ¢¢¢¥7FFVBW'÷6S¢¢¢W7F&Æ—6‚F—&V7BÖöæÇ’'VçF–ÖR6VÆV7F–öâÂ'&–FvR&WF—&VÖVçBÂÆö6ÂF—&V7B×6VÆV7F–öâWf–FVæ6RÂæBõ2Ó2FööÆ–ærâ ¢¢¢¤6†ævVBÖf–ÆR6÷VçC¢¢¢C’ ¢¢¢¤†–v‚×&—6²7W&f6W26†ævVC¢¢¢D"6VÆV7F÷"÷&÷f–FW"Â6ö×F–&–Æ—G’FFW"Â'&–FvRFVÆWF–öâ&÷7FW"ÂF—&V7B6†V6¶W"Â66†VÖ2Âõ2Ó2ÂWf–FVæ6R&öGV6W'2Âv÷fW&æVB'F–f7G2â ¢¢¢¥&Wf–Wrf–æF–æw3¢¢¢f÷W"F‡&VG26÷fW&–ær6öçFVçBfÆ–FF–öâÂ66†VÖ7G&–7FæW72Â5Â6fWG’ÂæB&÷r×7V6–f–26Öö¶R6ÆVçW²ÆÂ&W6öÇfVBâ ¢¢¢¥&WV—&VB6†V6·3¢¢¢´W†7BÖ†VB'Vâ#“ƒ#C“SS…Ò†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"ö7F–öç2÷'Vç2ó#“ƒ#C“SS‚’Ârór¦ö'27V66W76gVÂâ ¢¢¢¤ÖFW&–Â6öçG&–'WF–öã¢¢¢7&VFVBF†RF—&V7BÖöæÇ’&6†—FV7GW&RæBÖ÷7B"ÔFööÆ–ærâ ¢¢¢¤v276VBf÷'v&C¢¢¢6ö×F–&–Æ—G’÷væW'6†—Â&WF—&VBÖ¶W’66ææW"6ö×ÆWFVæW72Âæöæf–æÂ—VÆ–æR†æFÆ–ærÂæBõ2Ó2†&FVæ–ærâ ¢¢¢¤Wf–FVæ6S¢¢¢÷&–v–æÂ"Â33c2Â&öG’Âf–æÂ†VB6F6†f6fCS†66cc–6cƒSss†6C6S“S“#3s–ÂF‡&VG2Âv÷&¶fÆ÷rà ¢2222&VÖVF–Â"Â33c@ ¢¢¢¥F—FÆS¢¢¢W6RD$66W72f÷"Vçb6VÆV7F–öâb6Öö¶RÂVæ†æ6R&WF—&VBÖ¶W’66ææ–ærÂæBFB"Ôæöæf–æÂvFV ¢¢¢¤ÖW&vR–FVçF–f–W#¢¢¢C3ƒS6VVCs–&#SSS3sssf#ƒ&V3ƒ“SC&CF ¢¢¢¥7FFVBW'÷6S¢¢¢&VÖ÷fRGWÆ–6FVB6VÆV7F–öâöÆ–7’Â7G&VæwF†Vâ7F—fR×6÷W&6R66ææ–ærÂæBÖ¶RF†R7FvRÓB"Ô7F÷W‡Æ–6—Bâ ¢¢¢¤6†ævVBÖf–ÆR6÷VçC¢¢¢cb ¢¢¢¤†–v‚×&—6²7W&f6W26†ævVC¢¢¢FFW"öF%ö66W72ç–Â6VÆV7F÷"Wf–FVæ6RÂ7FF–266ææW"Â&–Ç2Æör—6öÆF–öâÂ6æ—G’—VÆ–æRæBvFRâ ¢¢¢¥&Wf–Wrf–æF–æw3¢¢¢GvVÇfRF‡&VG26öæ6W&æ–ærG&ç67F–öâ&V†f–÷"ÂvFR÷&FW&–ærög&W6†æW72öf–ÇW&R6VÖçF–72ÂæB66ææW"Æ–6W2öwV–Fæ6S²ÆÂ&W6öÇfVBâ ¢¢¢¥&WV—&VB6†V6·3¢¢¢´W†7BÖ†VB'Vâ#“ƒs3c3SC“uÒ†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"ö7F–öç2÷'Vç2ó#“ƒs3c3SC“r’Ârór¦ö'27V66W76gVÂâ ¢¢¢¤ÖFW&–Â6öçG&–'WF–öã¢¢¢6VçG&Æ—¦VB6VÆV7F–öâ&V†f–÷"æBW7F&Æ—6†VBF†RG'WF†gVÂæöæf–æÂ—VÆ–æR7FFRâ ¢¢¢¤v276VBf÷'v&C¢¢¢6ö×WFVBÖ¶W’÷fÇVR×&VB66ææW"'—76W2æBFF—F–öæÂÆ–2÷66÷R66W2â ¢¢¢¤Wf–FVæ6S¢¢¢&VÖVF–Â"Â33cBÂf–æÂ†VBCV#““CFC†3†6&V#†#6&S63SS#vV†ÂF‡&VG2Âv÷&¶fÆ÷rà ¢2222&VÖVF–Â"Â33cP ¢¢¢¥F—FÆS¢¢¢FWFV7B&WF—&VBD"'&–FvR¶W—2v—F†÷WB&VF–ærDD$4UõU$ÂÂF–v‡FVâ7FF–26†V6·2ÂæBWFFRFö76 ¢¢¢¤ÖW&vR–FVçF–f–W#¢¢¢f&cƒsSF†S##fCc†Sv6sS–V3#†6Fc“V ¢¢¢¥7FFVBW'÷6S¢¢¢wV&çFVRÖVÖ&W'6†—ÖöæÇ’&VgW6ÂF–Ö–æræB6Æ÷6R66ææW"FFÖfÆ÷rv2â ¢¢¢¤6†ævVBÖf–ÆR6÷VçC¢¢¢" ¢¢¢¤†–v‚×&—6²7W&f6W26†ævVC¢¢¢Væv–æRöF"öFFW"ç–ÂF—&V7B6†V6¶W"ÂF—&V7B×6VÆV7F–öâöÖVBÖ66†R&öGV6W'2Â66†VÖÂ&VF7F–öâwV–Fæ6RÂ66ææW"FW7G2â ¢¢¢¥&Wf–Wrf–æF–æw3¢¢¢GvVçG’ÖöæRF‡&VG26÷fW&–ær66÷RÂÆ–6W2Â–×÷'G2Âw&W'2Â6öç7FçBW‡&W76–öç2Â7V'67&—G2Â6ö×&V†Vç6–öç2ÂæB7G'V7GW&ÂÆö÷&–æF–æs²ÆÂ&W6öÇfVBâ ¢¢¢¥&WV—&VB6†V6·3¢¢¢´W†7BÖ†VB'Vâ#“ƒ“3##Cƒ#%Ò†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"ö7F–öç2÷'Vç2ó#“ƒ“3##Cƒ#"’Ârór¦ö'27V66W76gVÂâ ¢¢¢¤ÖFW&–Â6öçG&–'WF–öã¢¢¢ÖFR&WF—&VBÖ¶W’&VgW6ÂfÇVRÖ&Æ–æBæBW‡æFVBF†R6†V6¶W"Fòf–Â6Æ÷6VB7&÷72&VÆ—7F–2—F†öâFFfÆ÷râ ¢¢¢¤v276VBf÷'v&C¢¢¢õ2Ó26÷W&6RÖ&Vf÷&RÖ–×÷'BÂ6†–ÆB—6öÆF–öâÂ7–ÖÆ–æ²6fWG’ÂÖ&¶W"6öç7V×F–öâÂW'&÷"&÷vF–öâÂæBf–ÆVBÖ6æF–FFR&VFÖ—76–öââ ¢¢¢¤Wf–FVæ6S¢¢¢&VÖVF–Â"Â33cRÂf–æÂ†VB#c&V3c–Sƒ#V6V6CCvfFCcs#ƒS–cc3f&F#VÂF‡&VG2Âv÷&¶fÆ÷rà ¢2222&VÖVF–Â"Â33c` ¢¢¢¥F—FÆS¢¢¢„DRÔU”33‚"Óe"Ô¢f–æÆ—¦RF—&V7BÖöæÇ’&VÖVF–F–öâæBõ2Ó2FööÆ–æv ¢¢¢¤ÖW&vR–FVçF–f–W#¢¢¢fSc–CvsvcS3–Cs3fff63S“f&CSfvCF“ ¢¢¢¥7FFVBW'÷6S¢¢¢6Æ÷6RF†R6ö×ÆWFR"Ô6öçG&7BÂ–æ6ÇVF–ærõ2Ó27FFR6fWG’æB66Æ&ÆRW‡FW&æÂ&VÆV6RGFW7FF–öââ ¢¢¢¤6†ævVBÖf–ÆR6÷VçC¢¢¢#R ¢¢¢¤†–v‚×&—6²7W&f6W26†ævVC¢¢¢õ2Ó2'VææW"÷fÆ–FF÷"÷FW7G2Â÷7GW&R66†VÖÂF—&V7B66ææW"ÂÖVBÖ66†RwV&G2Â&VÆV6RÖæ–fW7Bö–FVçF—G’ÂW‡FW&æÂGFW7FF–öâÂ—VÆ–æRÂ4’Â'F–f7G2Â&öög2ÂæBvVæW&FVBÖf–ÆR6ÆVçWâ ¢¢¢¥&Wf–Wrf–æF–æw3¢¢¢6WfVçFVVâF‡&VG3²ÆÂ&W6öÇfVBâÖFW&–Â—77VW2–æ6ÇVFVBWF†÷&—¦F–öâ†6†–ærÂ7–ÖÆ–æ²&ö÷G2Â6†–ÆBW'&÷"&÷vF–öâÂ6WVVæ6R&—f–ÆVvW2Â6öÖÖæB'6–ærÂ7FvR÷væW'6†—ÂÖVBÖ66†R—6öÆF–öâÂ&VgW6ÂVçfVÆ÷W2ÂF‚×&ööb÷'F&–Æ—G’ÂÖæ–fW7B6öç6—7FVæ7’ÂæB&Vv—7G'’–FVçF—G’6÷WÆ–ærâ ¢¢¢¥&WV—&VB6†V6·3¢¢¢´W†7BÖ†VB'Vâ3SSCƒUÒ†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"ö7F–öç2÷'Vç2ó3SSCƒR’Ârór¦ö'27V66W76gVÂâ ¢¢¢¤ÖFW&–Â6öçG&–'WF–öã¢¢¢6Æ÷6VBÆÂ&VÖ–æ–ær6÷W&6RÂ6V7W&—G’ÂWf–FVæ6RÂ7FFRÖÖ6†–æRÂæB&Wf–Wv&–Æ—G’v2â ¢¢¢¤v276VBf÷'v&C¢¢¢öæÇ’W‡&W76Ç’F÷vç7G&VÒõ2Ó2W†V7WF–öâæB"Óe"Ô"FÖ—76–öââ ¢¢¢¤Wf–FVæ6S¢¢¢&VÖVF–Â"Â33cbÂf–æÂ†VBf#“f6F3scƒƒs–CfC–6S#“#c“Scc“ƒ&²FW&Ö–æÂ&Wf–Ws¢(	ÄF–FâwBf–æBç’Ö¦÷"—77VW2î(	Ð ¢222"Óe"Ô&WV—&VÖVçB6F—6f7F–öâ7&÷77vÆ° §Â”BÂv÷fW&æ–ærÆö6F÷"æB&WV—&VÖVçBÂ7W'&VçBF—7÷6—F–öâÂ7W'&VçB–×ÆVÖVçFF–öâæBWf–FVæ6RÂ†—7F÷'’æBfÆ–FF–öâÂ&÷VæF'’òf–æF–ærÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§Â$UÓÂ5$B*|*s"ÂŽ(	3“¢&W6W'fR"Óe"Ô(i"õ2Ó2(i""Óe"Ô&²"Ô—26÷W&6R÷FööÆ–æröæÇ’Â4D•4d”TBÂ7W'&VçB6æ—G’Æör&V6÷&G2%ö÷7FFS¦æöæf–æÅöf–Åö6Æ÷6VFæB7FvRÓB7F÷²æòÆ—fRõ2Ó2F—&V7F÷'’÷"F—&V7B×6VÆV7F–öâ&–Ö'’W†—7G2Â'2Â33cBæBÂ33cbÖFRF†R&÷VæF'’W‡Æ–6—C²W†7BÖ†VB4’76VBÂõ2æB"Ô"&VÖ–âF÷vç7G&VÓ²æòf–æF–ærÀ§Â$UÓ"Â%42Ó%TrÓ¢&WF–âU”3#B6æöæ–6Â6æ—G’&–æF–ærv—F†÷WB&V÷Væ–ærÂ4D•4d”TBÂFö72ö66WFæ6UöÖöW–3#Bæ§6öææBF†RFö¶VâÖG&—‚7F–ÆÂ&–æBVF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆöv²æòU”3#B&W'Vâ÷&V6Æ76–f–6F–öâÂgVÆÂWf–FVæ6RFW7G276VBÂ"Ô(	—2ÆFW"æöæf–æÂvFR7&VFW2æò÷"Fö¶Vâ6Æ–Ó²æòf–æF–ærÀ§Â$UÓ2Â%42Ó%TrÓ&¢&WF–â×VÇF’×7–çF‚÷&rÖÖ&¶W"6V7&WB6fWG’Â4D•4d”TBÂFööÇ2öWf–FVæ6R÷&WF–æVEöWf–FVæ6U÷6fWG’ç–&VÖ–ç2F†R6†&VB66ææW"W6VB'’F—&V7BæBõ2Ó2Wf–FVæ6RÂfö7W6VB66ææW"FW7G2æBWf–FVæ6R7V—FR76VBÂæò†—7F÷&–6Â&Ww&—FS²æòf–æF–ærÀ§Â$UÓBÂ%42ÓæBE"Ô4äôâÓC¢&WF–â7G&–7BW&RDDÂ&ö¦V7F÷"æB&ö¦V7F–öâÖöæÇ’G'WF‚Â4D•4d”TBÂVæv–æRöF"öFFÅö–FVçF—G•÷&ö¦V7F–öâç–&WF–ç2†FRæFFÅö–FVçF—G•÷&ö¦V7F–öâçc²õ2Ó26—FW2F†B66†VÖ&F†W"F†â6Æ–Ö–ærgVÆÂDDÂWVÆ—G’Â&ö¦V7F÷"æBõ2÷7GW&RFW7G276VBÂ'&–FvRÖFWVæFVçBcR6ÆW6W2&VÖ–â7WW'6VFVC²æòf–æF–ærÀ§Â$UÓRÂ%42Ó"ôE"Ô4äôâÓS¢6öÆR6VÆV7F÷"ÂW†7B&WF—&VB&÷7FW"ÂÖVÖ&W'6†—ÖöæÇ’æÖW2ÖöæÇ’&VgW6ÂÂW†7B’Â4D•4d”TBÂVæv–æRöF"öFFW"ç–FVf–æW2F†RW†7BF‡&VRÖ¶W’GWÆS²&VgW6Â&V6VFW2E4â66W73²&WF—&VD'&–FvT6öæf–wW&F–öæ†2f—†VB6öFRöÖW76vRæBGWÆR¶W—2ÂÂ33cR6Æ÷6VBfÇVR×&VBæB66ææW"v3²F—&V7BD"FW7G276VBÂæòf–æF–ærÀ§Â$UÓbÂ%42Ó#¢öæRF—&V7B&÷f–FW"GFV×BÂG—VBf–ÇW&RÂW&R6VÆV7F–öâWf–FVæ6RÂæòfÆÆ&6²÷&WG'’Â4D•4d”TBÂD$66W72æf÷%ö7W'&VçEöVçf6öç7G'V7G2öæÇ’7–6÷u&÷f–FW&ÂW&f÷&×2öæR†VÇF‚6ÆÂÂ&V6÷&G2W†7BGFV×BWf–FVæ6RÂæBw&—FW2æ÷F†–ærÂF—&V7B×6VÆV7F–öâæBf–ÇW&R×F‚FW7G276VBÂæòÇFW&æFR&÷f–FW"W†—7G3²æòf–æF–ærÀ§Â$UÓrÂ%42Ó#¢W†7B&VBÖöæÇ’G&ç67F–öâ&÷7FW"ÂöæR6öææV7F–öâö7W'6÷"Âæò6öÖÖ—BÂ&öÆÆ&6²–âf–æÆÇ–Â4D•4d”TBÂ7–6÷u&÷f–FW"ç&VFöæÇ•÷G†fÆ–FFW2F†Rf—†VBFVâ×7FFVÖVçB&÷7FW"&Vf÷&R6öææV7F–æs²f—'7B7FFVÖVçB—2W†7B&VBÖöæÇ“²&öÆÆ&6²—2Væ6öæF—F–öæÂÂ5Â×WFF–öâÂ&F6†–ærÂ6öÖÖVçBÂ7V66W72öf–ÇW&RÂæB&6TW†6WF–öæFW7G276VBÂW†—7F–ærw&—FRG&ç67F–öâ6VÖçF–72&VÖ–â6W&FS²æòf–æF–ærÀ§Â$UÓ‚Â%42Ó#¢6ö×F–&–Æ—G’&W6öÇfW"FVÆVvFW2Fò6öÆR÷væW"æBVÖ—G27G&–7Bc"6†W2Â4D•4d”TBÂFFW"öF%ö66W72ç–FVÆVvFW26VÆV7F–öâFòD$66W76²VçbÖG&—‚Â&W6öÇfW"ÂæB6Öö¶RF‡2&RF—&V7BÖöæÇ’v—F‚7F&ÆRæÖW2ÖöæÇ’W'&÷'2ÂÂ33cB6VçG&Æ—¦VB&V†f–÷#²D"6ö×F–&–Æ—G’7V—FW276VBÂæò6V6öæB6VÆV7F–öâFƒ²æòf–æF–ærÀ§Â$UÓ’Â%42Ó#¢FVÆWFR6—‚7F—fR'&–FvR7W&f6W2æB'&–FvRW†6WF–öç3²FBF—&V7B6†V6¶W"Â4D•4d”TBÂÆÂ6—‚&WV—&VBF‡2&WGW&âCBB7W'&VçB„TC²'&–FvRW†6WF–öç2&R'6VçC²6†V6µöF—&V7EöF%ö6öçG&7Bç–66ç27F—fRG&6¶VB6÷W&6Rö7W'&VçBwV–Fæ6RÂÂ33c2FVÆWF–öâÇW2Â33cN(	5Â33cR66ææW"&VÖVF–F–öã²6†V6¶W"76VB–â4’Âæòf–æF–ærÀ§Â$UÓÂ%42Ó#¢F—&V7BÖöæÇ’÷7GW&R6GW&RæBG&ç7÷'BÖæWWG&ÂÖVBÖ66†RwV&G2Â4D•4d”TBÂU”36GW&RW6W2F—&V7BD"F‡3²ÖVBÖ66†RFööÇ2wV&BvVæW&–2&÷f–FW"ö÷WF&÷VæB’ôòæB–×÷'BæòFVÆWFVB'&–FvR&÷f–FW"ÂÖVBÖ66†RÆö6Âôõ2Ó"6ö×F–&–Æ—G’FW7G276VBÂõ2Ó"v2æ÷B&W'Vã²æòf–æF–ærÀ§Â$UÓÂ%42Ó#¢&W6W'fR&VFW"ô4Ä’'—FW2Â&öG”w&‚6VÖçF–72ÂGW&&ÆR–ÆöG2ÂæBW†—7F–ærw&—FR&–Ç2Â4D•4d”TBÂ&VFW"ô4Ä’FFW'2&WF–â&W7öç6R÷6W&–Æ—¦F–öâ6öçG&7G3²öæÇ’&WF—&VBÖ6öæf–wW&F–öâ&VgW6Â—2æWvÇ’G—VC²&öG”w&‚ÖVBÖ66†R&V†f–÷"&VÖ–ç2&÷VæFVBÂ…EEÂ4Ä’&—G’Â&öG”w&‚Â&–Ç2ÂæB6Öö¶R7V—FW276VBÂæòV&Æ–2&÷WFR÷"–ÆöBW‡ç6–öã²æòf–æF–ærÀ§Â$UÓ"Â%42Ó2ôE"Ô4äôâÓc¢F—&V7B×6VÆV7F–öâ66†VÖ÷&öGV6W"ÂW†7B66W2÷&VF–6FW2Â6æöæ–6ÂæBæVvF—fR&V†f–÷"Â4D•4d”TBÂ7G&–7B66†VÖæB6öÆR&öGV6W"–×ÆVÖVçBF†RW†7Bf÷W"÷&FW&VB66W2ÂW†7B&VF–6FW2Â6æöæ–6ÂÄb'—FW2ÂFWFW&Ö–æ—7F–2vVæW&F–öâÂæB6ÖR×F‚æVvF—fR&V6V—BÂV–v‡Bfö7W6VBFW7G2ÇW2F—&V7B6†V6¶W"76VBÂf—‡GW&RÖöæÇ“²æòW‡FW&æÂ6ÆÃ²æòf–æF–ærÀ§Â$UÓ2Â%42Ó3¢f–æÂG&6¶VBF—&V7B×6VÆV7F–öâ'—FW2æB&–æF–ærÂDõtå5E$TÒ%’$õdTB$õTäD%’Â'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæ—2–çFVçF–öæÆÇ’'6VçBÂ7FvRrfÆ–FFW2F†RÆö6Â6öçG&7Bv—F†÷WB6Æ–Ö–ærf–æÂG&6¶VBFÖ—76–öâÂ"Óe"Ô"÷vç2f–æÂ'—FW2Â–æFW‚&÷w2Â&öög2ÂæB&–æF–ærÀ§Â$UÓBÂ%42Ó3¢&W6W'fR'&–FvRÖW&&–Ö&–W2æBÖVæ–ær2–Ö×WF&ÆR†—7F÷'’Â4D•4d”TBÂ†—7F÷&–6Â'F–f7G2&VÖ–âVæFW"†—7F÷&–6ÂF‡3²7FvR"&W÷'G2öæÇ’„•5Dõ$”4Åô”åDTu$•E•ôô¶²æò7W'&VçB'&–FvR52—2FW&—fVBÂ†—7F÷&–6Â†6‚Â6æöæ–6ÂÂW‡G&Öf–ÆRÂæBæöæ6Æ–ÒFW7G276VBÂæò&W'Vâ÷"&VÆ&VÆ–æs²æòf–æF–ærÀ§Â$UÓRÂ%42ÓBôE"Ô4äôâÓs¢'VææW"Â–æFWVæFVçBfÆ–FF÷"Â6WfVâ66†VÖ2Âf—‡GW&Rö×WFF–öâFW7G2Â4D•4d”TBÂW†7B'VææW"÷fÆ–FF÷"Æö6’æBÆÂ6WfVâ66†VÖ2W†—7C²FW7G2W6Rf¶RöÆö6Â&÷f–FW'2ÂFW7G2ö÷2÷FW7Eö†FUöW–33…ö÷32ç–6öçF–ç2"FW7BgVæ7F–öç2æBW††W7F—fR&ÖWG&—¦VB×WFF–öç3²4’76VBÂæòõ2W†V7WF–öã²æòf–æF–ærÀ§Â$UÓbÂ%42ÓC¢W†7BWF†÷&—¦F–öâf–VÆG2Â&ö÷G2Â6÷VçG2Â&wbÂöæRÖGFV×BÖ&¶W"6VÖçF–72Â4D•4d”TBÂ66†VÖæB&÷F‚–×ÆVÖVçFF–öç2–æFWVæFVçFÇ’Væf÷&6RW†7B&ö÷G2ÂF&vWBÂ&–Ç2Â&÷7FW'2Â6÷VçG2ÂÔ’Ô&fV7F÷'2Â6æF–FFR&ö÷BÂæBöæRÖGFV×B'—FW2ÂWfW'’WF†÷&—¦F–öâæöFR÷fV7F÷"æB6÷VçB&V6V—fW2×WFF–öâ6÷fW&vRÂæòf–æF–ærÀ§Â$UÓrÂ%42ÓC¢7FFÆ–"6÷W&6RvFRÂ6ÆVâ6†–ÆBÂ6†–ÆBÖöæÇ’E4âÂæò•D„ôâ¦Âw&—FR6öæf–æVÖVçBÂ4D•4d”TBÂ6÷W&6R–FVçF—G’—26†V6¶VB&Vf÷&R&W÷6—F÷'’–×÷'G3²„TBö–æFW‚÷v÷&·G&VR'—FW2æBÖöFW2&R&÷VæC²–væ÷&VB–×÷'F&ÆRÖöGVÆW2Â&WÆ6VÖVçB&Vg2Â&W6–GVRÂæBVçG&6¶VBf–ÆW2f–Â6Æ÷6VC²&VçB67'V'2E4âgFW"f÷&²Â6÷W&6RÖ÷&FW"Â&VÂÔv—BÂ6†–ÆB”BöVçbÂ67'V"Öf–ÇW&RÂF–ÖV÷WBÂæB–×÷'B×G&FW7G276VBÂæò6÷W&6R×G&VR÷"G&6¶VBÖWf–FVæ6Rw&—FS²æòf–æF–ærÀ§Â$UÓ‚Â%42ÓC¢W†7B†VÇF‚÷&VBÖöæÇ’5Â7F—f—G’æB6÷VçFW'2Â4D•4d”TBÂöæR6VÆV7F÷"ÂöæR†VÇF‚4TÄT5BÂöæR&VFöæÇ•÷G†ÂFVâf—†VB7FFVÖVçG2ÂGvò6öææV7F–öç2F÷FÂÂæòw&—FW2÷&WG&–W2öÇFW&æFRGFV×G2ÂVW'’&÷7FW"Âw&çG2ö÷væW'6†—÷6WVVæ6RÂf–WrÂ'F—F–öâÂæB6÷VçB×WFF–öç276VBÂæòÆ—fRD"W6VBGW&–ærfÆ–FF–öã²æòf–æF–ærÀ§Â$UÓ’Â%42ÓC¢W†7BFVâÖf–ÆR7V66W726¶WBæB&öGV6W"÷væW'6†—Â4D•4d”TBÂ'VææW"÷vç2V–v‡B–æ—F–Â&–Ö&–W2ÇW26†V6·7VÓ²fÆ–FF÷"ÆöæRVÖ—G2&V6V—C²6æF–FFR7V66W72–çfVçF÷'’—2W†7C²6öçG&öÂÖöæÇ’7FFRFöW2æ÷BVçFW"6¶WB–çfVçF÷'’Â–çfVçF÷'’ÂW‡G&Öf–ÆRÂ&öGV6W"Â6öÖÖæBÖÆ–æRÂ6†V6·7VÒÖ–çWBÂæBGFW7FF–öâFW7G276VBÂG&6¶VBFW7F–æF–öâ&VÖ–ç2F÷vç7G&VÓ²æòf–æF–ærÀ§Â$UÓ#Â%42ÓC¢7G&–7B¥4ôâ÷FW‡Bö6†V6·7VÒ÷6V7&WB6öçG&7G2Â4D•4d”TBÂÆÂö&¦V7G2&V¦V7BVæ¶æ÷vâ¶W—3²6æöæ–6ÂUDbÓ‚ôÄbæB6†V6·7VÒ÷&FW&–ær&RVæf÷&6VC²7F&ÆR6öFW2æBæöæ6Æ–×2&RW†7C²6V7&WB6fWG’66ç2WfW'’&WF–æVB&–Ö'’Â66†VÖÖæöFRÂ6æöæ–6ÂÖ'—FRÂ6V7&WBÖ6Æ72Â&V6V—BÂæB6†V6·7VÒ×WFF–öç276VBÂæòf–æF–ærÀ§Â$UÓ#Â%42ÓC¢f–ÇW&R&V6V—BÂ&R÷÷7BÖÖ&¶W"6Æ76–f–6F–öâÂGW&&ÆRæöæFÖ—76–öâÂ4D•4d”TBÂ6V7W&RFW67&—F÷"Ö&÷VæBæòÖföÆÆ÷r&ö÷G3²Ö&¶W"7&VF–öâ—2F†R6öç7V×F–öâ&÷VæF'“²÷7BÖÖ&¶W"f–ÇW&W2&WF–â6öç7VÖVB7FFS²VæF–ærö6öÖÖ—GFVBöf–ÇW&RG&ç6—F–öç2&WfVçBÆFW"&VFÖ—76–öâÂFW7G26÷fW"æöæ6æöæ–6ÂWF‚Â'F–ÂÖ&¶W"w&—FW2Â7–ÖÆ–æ·2Â7FÆR&ö÷G2Â6ÆVçW÷&V6V—Bf–ÇW&RÂf–æÆ—¦F–öâ&6W2ÂæB&öÆÆ&6²–çFW''WF–öâÂæòf–æF–ærÀ§Â$UÓ#"Â%42ÓC¢–æFWVæFVçBfÆ–FF–öâ&Vf÷&R&V6V—Bö6†V6·7VÒöf–æÂFÖ—76–öâÂ4D•4d”TBÂ6÷W&6RæBWF†÷&—¦F–öâ&V6VFRÖ&¶W#²–æFWVæFVçB&V6V—BfÆ–FF–öâ&V6VFW26†V6·7VÓ²f–æÂfÆ–FF–öâ—2&VBÖöæÇ’æB&WGW&ç2'—FRGFW7FF–öã²FW&Ö–æÂ7FFR—2&V6†V6¶VBÂfÆ–FF÷"&wbÂ6÷W&6RöWF‚&6W2Â6æF–FFR×WFF–öâÂF–ÖV÷WBÂæBf–æÂÖFÖ—76–öâFW7G276VBÂ"Ô"×W7B&WVBfÆ–FF–öâ&÷VæB6÷“²æòf–æF–ærÀ§Â$UÓ#2Â%42ÓS¢W†7Bæ–æWFVVâ×7FvR—VÆ–æR7G'V7GW&RæBf–ÂÖ6Æ÷6VB7FvRBÂ4D•4d”TBÂ'Vå÷6æ—G•÷—VÆ–æRç–†2F†RW†7B&÷7FW#²7W'&VçBÆör6†÷w27FvW2(	32ô²Â7FvRBd”ÂÂæB7FvW2^(	3’æ÷BW†V7WFVBÂ—VÆ–æRæBvFRFW7G2&÷fRW†7B÷&FW&–ærÂg&W6†æW72Âf—'7BÖf–ÇW&RÂæBæöæf–æÂ&V6V—BÂf–æÂ52—2æ÷B6Æ–ÖVC²æòf–æF–ærÀ§Â$UÓ#BÂ%42ÓRôE"Ô4äôâÓƒ¢Æ—fRõ2Ó2ÂW†7B6÷’Â7W'&VçBö†—7F÷&–6Â7v—F6‚ÂWFFW"Âf–æÂ7FvW2Â7W÷'B7&÷77vÆ²ÂDõtå5E$TÒ%’$õdTB$õTäD%’ÂæòVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öW†—7G2æBæòf–æÂõ2Ó2ö7W'&VçBF—&V7BWf–FVæ6R—2&Vv—7FW&VBÂ'6Væ6R—2F†RFW7FVB%ööæöæf–æÅö÷35÷%ö%ö&–æF–æu÷&WV—&VF6öæF—F–öâÂõ2Ó2æB"Óe"Ô"÷vâF†—2v÷&²À§Â$UÓ#RÂ5$B*s’fÆ–FF–öâ÷&FW#¢7FF–2ÂF—&V7BÂ6öç7VÖW"ÂÖVBÖ66†RÂWf–FVæ6RÂõ2f—‡GW&W2Â&6†—FV7GW&RÂgVÆÂW†7BÖ†VB4’æB&Wf–WrÂ4D•4d”TBÂÆÂ&WV—&VBÆæW2&R&W&W6VçFVB–âF†Rf–æÂv÷&¶fÆ÷ræB7W'&VçBFW7G2Â'Vâ3SSCƒR76VBÆÂ6WfVâ¦ö'3²W†7BÖ†VB6ÆVâ&Wf–WrföÆÆ÷vVB&W6öÇWF–öâöbÆÂF‡&VG2Âæòf–æF–ærÀ§Â$UÓ#bÂ5$B*s’&öÆÆ&6²öf–ÂÖ6Æ÷6VB'VÆW2Â4D•4d”TBÂ'VçF–ÖR6ææ÷B&W7F÷&R'&–FvRfÆÆ&6³²Wf–FVæ6Rôõ2f–ÇW&W27F÷&Vf÷&RF÷vç7G&VÒFÖ—76–öã²õ2f–ÇW&R7FFW2&VÖ–â–æFÖ—76–&ÆRÂf–ÇW&RÂ–çFW''WF–öâÂ7–ÖÆ–æ²ÂF–ÖV÷WBÂ66ææW"ÂæB—VÆ–æRFW7G276VBÂ"Ô"&öÆÆ&6²&VÖ–ç2F÷vç7G&VÓ²æòf–æF–ærÀ§Â$UÓ#rÂ5$B*|*s’Â"æB&÷fÂÆ–Ö—FF–öç3¢æòõ2ÂW‡FW&æÂ66W72Âõb÷Fö¶Vâ÷7FGW2öFWÆ÷’ö6Æ÷6V÷WB6Æ–×2Â4D•4d”TBÂ"&öF–W2Â7W'&VçBÆörÂæöæ6Æ–Ò66†VÖ2ÂæBc*s"ãb6öç6—7FVçFÇ’&WF–âF†W6RW†6ÇW6–öç2Â6V&6‚æB&Wf–Wrf÷VæBæò6öçG&F–7F÷'’6ö×ÆWF–öâ6Æ–ÒÂc’7FGW6W2&VÖ–âVæ6†ævVC²æòf–æF–ærÀ ¢222f–æÂVffV7F—fR–×ÆVÖVçFF–öâ&Wf–Wp ¢22225U$bÓ ¢¢¢¥7W&f6S¢¢¢F—&V7B&÷f–FW"6VÆV7F–öâæBG—VB&VgW6Â ¢¢¢¥F–W#¢¢¢ ¢¢¢¥F‡3¢¢¢Væv–æRöF"öFFW"ç–ÂVæv–æRöF"öW'&÷'2ç– ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓRÂ$UÓb ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢’6–væGW&RÂ÷&FW&–ærÂVçf—&öæÖVçBÖVÖ&W'6†—ÂW'&÷"6öç7G'V7F–öâÂGFV×BWf–FVæ6RÂæBW&—G’â ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢W†7B&WF—&VBÖ¶W’&W6Væ6Rf–Ç2&Vf÷&RE4âfÇVR66W72÷"&÷f–FW"6öç7G'V7F–öã²÷F†W'v—6RW†7FÇ’öæRF—&V7B&÷f–FW"—2GFV×FVBâ ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢Â33c^(	—26ö×WFVBÖ¶W’æBÖVÖ&W'6†—×v—F†÷WB×&VB&VÖVF–F–öâv26†V6¶VBv–ç7B7W'&VçB6÷W&6Râ ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢&V†f–÷&ÂÖ–æw2F†B&—6RöâfÇVR66W72&÷fRF–Ö–ærÂ&F†W"F†â&VÇ––æröâ6÷W&6R×FW‡B6†V6·2â ¢¢¢¥&—6²76W76ÖVçC¢¢¢æò&W6–GVÂ6VÆV7F÷"ÂÆV²Â÷"ÇFW&æFRÖGFV×BF‚f÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBâ ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢v—D‡V"&WòÂVæv–æRöF"öFFW"ç“£§&WF—&VEöF%÷G&ç7÷'Eö¶W—5÷&W6VçFÂD$66W72æf÷%ö7W'&VçEöVçf²FW7G2ÂFW7EöF—&V7EöF%÷#g"ç–à ¢22225U$bÓ  ¢¢¢¥7W&f6S¢¢¢&÷f–FW"&VBÖöæÇ’G&ç67F–öâæB6ö×F–&–Æ—G’f:vFR ¢¢¢¥F–W#¢¢¢ ¢¢¢¥F‡3¢¢¢Væv–æRöF"÷&÷f–FW'2÷7–6÷u÷&÷f–FW"ç–ÂFFW"öF%ö66W72ç– ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓrÂ$UÓ‚ ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢5Â6Æ76–f–W"Âf—†VB&÷7FW"Â6öææV7F–öâÆ–fV7–6ÆRÂ&öÆÆ&6²Â&W6öÇfW"öVçb6†W2Â6Öö¶R6ÆVçWÂæBW'&÷"æ÷&ÖÆ—¦F–öââ ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢öæRF—&V7B–×ÆVÖVçFF–öâ6W'fW27W'&VçBæB6ö×F–&–Æ—G’6ÆÆW'3²&VBÖöæÇ’5Â6ææ÷B&RW‡FVæFVB÷"&F6†VBâ ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢Â33c>(	5Â33cBG&ç67F–öâæBGWÆ–6FVB×&W6öÇfW"f–æF–æw2vW&R6†V6¶VBv–ç7B7W'&VçB6öFRâ ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢W†7B7FFVÖVçBÖ'’×7FFVÖVçB×WFF–öç2æB7V66W72öf–ÇW&R&öÆÆ&6²FW7G2â ¢¢¢¥&—6²76W76ÖVçC¢¢¢æòGWÆ–6FR6VÆV7F–öâ÷væW"÷"f–ÂÖ÷Vâ5ÂF‚f÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBâ ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢v—D‡V"&WòÂ7–6÷u&÷f–FW"ç&VFöæÇ•÷G†²FFW"öF%ö66W72ç“£§¶F%÷&W6öÇfRÇ&W6öÇfUöVçeöÖG&—‚ÆF%÷'u÷6Öö¶WÖà ¢22225U$bÓ0 ¢¢¢¥7W&f6S¢¢¢W†V7WF&ÆR'&–FvR&WF—&VÖVçBæB7FF–2&WfVçF–öâ ¢¢¢¥F–W#¢¢¢ ¢¢¢¥F‡3¢¢¢6—‚&VÖ÷fVB'&–FvRôõ2ö6†V6¶W"F‡3²6’ö6†V6·2ö6†V6µöF—&V7EöF%ö6öçG&7Bç–²7W'&VçBD"wV–Fæ6Râ ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓ’Â$UÓB ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢FVÆWF–öâÂ–×÷'G2Â&Vv—7G&F–öç2Â6öÖÖæG2Â&r&÷f–FW"W6RÂ…EE'&–FvR6öç7G'V7F–öâÂwV–Fæ6RW†6ÇW6–öç2ÂæB†—7F÷&–6ÂÆÆ÷væ6W2â ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢&WF—&VBæÖW2&VÖ–âöæÇ’–â&VgW6Â&÷7FW'2Â†—7F÷&–6ÂWf–FVæ6RöFW6–vâ&V6÷&G2Â66†VÖ2Â66ææW"Æöv–2ÂæBæVvF—fRFW7G2â ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢ÆÂÂ33cN(	5Â33cR66ææW"F‡&VG2vW&RföÆÆ÷vVBF‡&÷Vv‚7W'&VçBÆ–2Â66÷RÂ–×÷'BÂw&W"Â7V'67&—BÂ¦—ÂvÇ'W2ÂæBVç&W6öÇfVBÖW‡&W76–öâ†æFÆ–ærâ ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢6—‡G’×Gvòfö7W6VB6†V6¶W"FW7G2ÇW2F†R4’6†V6¶W"â ¢¢¢¥&—6²76W76ÖVçC¢¢¢æòW†V7WF&ÆR'&–FvRF‚f÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBâ ¢¢¢¥6V&6‚&ööc¢¢¢6V&6†VB7W'&VçBv—D‡V"6÷W&6Rf÷"'&–FvU&÷f–FW&ÂÆÂF‡&VR&WF—&VB¶W—2ÂrÖ'&–FvVÂ'&–FvUöf7F÷'–ÂæBW&ÆÆ–"ç&WVW7F²ÖWF†öC¢&W÷6—F÷'’6öFR6V&6‚ÇW2W†7B×F‚fWF6ƒ²&W7VÇC¢F†R6—‚&ö†–&—FVBF‡2&R'6VçBÂæB&VÖ–æ–ær–â×66÷RÖF6†W2&R&VgW6Âö†—7F÷'’ö6†V6¶W"÷FW7BW6W2à ¢22225U$bÓ@ ¢¢¢¥7W&f6S¢¢¢&W6W'fVB&VFW"Â4Ä’Â&öG”w&‚ÂÖVBÖ66†RÂæB&WF–æVB&VÖVF–F–öâ ¢¢¢¥F–W#¢¢¢ô" ¢¢¢¥F‡3¢¢¢FFW"ö‡GG÷&VFW"ç–ÂF÷V6†VB&öG”w&‚f–ÆW2ÂÖVBÖ66†RFööÇ2÷67&—G2Â&WF–æVB66ææW"ÂDDÂ&ö¦V7F÷"ÂU”3#B66WFæ6R&–æF–ærâ ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓ.(	5$UÓBÂ$UÓÂ$UÓ ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢V&Æ–2'—FW2ÂG—VB&VgW6ÂÖ–ærÂ–ÆöB6VÖçF–72ÂÆö6ÂæòÔ’ôò&V†f–÷"Â&WF–æVBWf–FVæ6R6fWG’ÂæBDDÂ&ö¦V7F–öââ ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢&öGV7B6öçG&7G2&VÖ–â7F&ÆS²öæÇ’&WF—&VBÖ6öæf–wW&F–öâ&W6Væ6Rv–ç2F†R&÷fVBG—VB&VgW6Ââ ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢'&–FvR×7V6–f–2ÖVBÖ66†R–çFW&6WF–öâv2&WÆ6VB'’G&ç7÷'BÖæWWG&ÂwV&G2v—F†÷WB&V÷Væ–ærõ2Ó"â ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢&VFW"ô4Ä’&—G’Â…EEÂ&öG”w&‚ÂÖVBÖ66†RÂ&WF–æVB×6fWG’ÂæB&ö¦V7F÷"7V—FW2â ¢¢¢¥&—6²76W76ÖVçC¢¢¢æòV&Æ–2÷"GW&&ÆR×–ÆöBG&–gBf÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBà ¢22225U$bÓP ¢¢¢¥7W&f6S¢¢¢Æö6ÂF—&V7B×6VÆV7F–öâWf–FVæ6R ¢¢¢¥F–W#¢¢¢ ¢¢¢¥F‡3¢¢¢&öGV6W"Â7G&–7B66†VÖÂF—&V7B6†V6¶W"ÂæBfö7W6VBFW7G2â ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓ"Â$UÓ2 ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢66R÷&FW"ÂW†7B÷WF6öÖW2Â&VF–6FW2Â6æöæ–6Â'—FW2ÂFWFW&Ö–æ—7F–2vVæW&F–öâÂæVvF—fR&V6V—BÂæB6V7&WB6fWG’â ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢F†RÆö6Â6öçG&7B—26ö×ÆWFS²f–æÂG&6¶VB'—FW2&RFVÆ–&W&FVÇ’'6VçBâ ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢Â33c^(	—2fÇVRÖ&Æ–æB&WF—&VB66Rv2fW&–f–VB–âF†R7W'&VçB&öGV6W"â ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢Væ¶æ÷vâÖ¶W’Â×WFF–öâÂGvò×'VâÂæVvF—fRÂÖVÖ&W'6†—ÖöæÇ’ÂæBæòÔE4â×&VB6÷fW&vRâ ¢¢¢¥&—6²76W76ÖVçC¢¢¢æò&öGV6W"÷66†VÖF—6w&VVÖVçBf÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBf÷""Ô²f–æÂ&–Ö'’6÷'&V7FÇ’F÷vç7G&VÒâ ¢¢¢¥6V&6‚&ööc¢¢¢W†7BfWF6‚öb'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæB7W'&VçB„TB&WGW&æVBCEÂà ¢22225U$bÓ` ¢¢¢¥7W&f6S¢¢¢õ2Ó2WF†÷&—¦F–öâÂ6÷W&6R–FVçF—G’Â&ö6W72öVçf—&öæÖVçB—6öÆF–öâÂæBf–ÆW7—7FVÒ&÷VæF'’ ¢¢¢¥F–W#¢¢¢ ¢¢¢¥F‡3¢¢¢67&—G2ö÷2ö†FUöW–33…ö÷32ç–ÂWF†÷&—¦F–öâöf–ÇW&R66†VÖ2Âõ2FW7G2â ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓ^(	5$UÓrÂ$UÓ# ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢&ö÷G7G&÷&FW&–ærÂ6†–ÆB&VF–æW72Â&VçBE4â67'V&&–ærÂ6ÆVâVçf—&öæÖVçBÂ6÷W&6RÖæ–fW7BÂ–væ÷&VBæF—fRÖöGVÆW2ÂFW67&—F÷'2Â7–ÖÆ–æ·2Â&—fFR&ö÷G2ÂFVFÆ–æW2ÂæBÖ&¶W"6VÖçF–72â ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢æò&W÷6—F÷'’–×÷'BföÆÆ÷w2f–ÆVB6÷W&6RWF†÷&—¦F–öã²æò&÷f–FW"6ÆÂ&V6VFW2GW&&ÆRÖ&¶W"6öç7V×F–öã²FW&—fVB×&ö÷B÷W&F–öç2&RFW67&—F÷"Ö&÷VæBæBf–Â6Æ÷6VBâ ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢ÆÂ6—‚&Wf–÷W6Ç’&W÷'FVBõ2Ó2&Æö6¶W"6Æ76W2vW&R6†V6¶VBv–ç7B7W'&VçB6öFRæBW†7B&Vw&W76–öç2â ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢&VÂÔv—BÂ–×÷'B×G&ÂæF—fRÖÖöGVÆRÂ”BöVçbÂ7–ÖÆ–æ²Â7FÆR×&ö÷BÂÖ&¶W"ÂF–ÖV÷WBÂæB6ÆVçWÖf–ÇW&RFW7G2â ¢¢¢¥&—6²76W76ÖVçC¢¢¢æò&W&öGV6–&ÆR—6öÆF–öâ÷"&ö÷BÖW66RFVfV7Bf÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBà ¢22225U$bÓp ¢¢¢¥7W&f6S¢¢¢õ2Ó2ö'6W'fF–öâÂ6¶WB6VÆ–ærÂ–æFWVæFVçBfÆ–FF–öâÂæBFW&Ö–æÂ7FFR ¢¢¢¥F–W#¢¢¢ ¢¢¢¥F‡3¢¢¢'VææW"ÂfÆ–FF÷"Â&VÖ–æ–ær6—‚6¶WB66†VÖ2Â÷7GW&R66†VÖÂæBõ2FW7G2â ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓŽ(	5$UÓ#" ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢5Â&÷7FW"ö6÷VçG2Â&öÆR÷f–Wr÷'F—F–öâ&VF–6FW2Â6æF–FFR–çfVçF÷'’Â&V6V—B÷væW'6†—Â6†V6·7V×2Â6æöæ–6Â'—FW2Â6V7&WB66ææ–ærÂVæF–ærö6öÖÖ—Böf–ÇW&RG&ç6—F–öç2ÂFW&Ö–æÂ&6W2ÂæB&VFÖ—76–öââ ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢öæÇ’gVÆÇ’GFW7FVB6æF–FFRv—F‚7F&ÆRWF†÷&—¦F–öâÂ6÷W&6RÂ6öçG&öÂ7FFRÂ–çfVçF÷'’ÂæB†6†W26â&V6öÖRFÖ—76–&ÆRâ ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢WF†÷&—¦F–öâ†6†–ærÂ6†–ÆBW'&÷"&÷vF–öâÂ6WVVæ6Rw&çG2Â'F–ÂÖ&¶W"w&—FW2ÂæBÆFR6ÆVçWf–ÇW&W2vW&RÆÂ&V6†V6¶VBâ ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢W††W7F—fRf–VÆBöæöFRö6÷VçB÷F‚ö&wbö6†V6·7VÒ÷6V7&WBõ5ÂöW‡G&Öf–ÆR×WFF–öç2ÇW2†÷7F–ÆRG&ç6—F–öâFW7G2â ¢¢¢¥&—6²76W76ÖVçC¢¢¢6ö×ÆW‚'WB&Wf–Wv&ÆS²æò7W'&VçB6÷'&V7FæW72&Æö6¶W"f÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBà ¢22225U$bÓ€ ¢¢¢¥7W&f6S¢¢¢7W'&VçB×fW'7W2Ö†—7F÷&–6ÂWf–FVæ6RæB&VÆV6R—VÆ–æR ¢¢¢¥F–W#¢¢¢ ¢¢¢¥F‡3¢¢¢6æ—G’'VææW"övFRÂWFFW"Â÷&–VçFF–öâÂWf–FVæ6RF‡2Â–æFW†W2ÂÖ—'&÷'2Â†—7F÷&–6Â'&–FvRôõ2Ó"'F–f7G2æBFW7G2â ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓBÂ$UÓ#2Â$UÓ#B ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢W†7B7FvR÷&FW"Âf—'7BÖf–ÇW&R6VÖçF–72Â†—7F÷&–6Â–çFVw&—G’ÖöæÇ’&W7VÇBÂæòõ2W†V7WF–öâÂWFFW"÷væW'6†—ÂæB"Ô"7F÷â ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢7FvW2(	3273²7FvRBf–Ç2f÷"F†RW†7BÖ—76–ærF÷vç7G&VÒ6¶WC²æòÆFW"7FvRW†V7WFW2â ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢&W6öÇfVB&Wf–Wr&WVW7G2Fò&Vv—7FW"õ2Ó2÷"66WBgVÆÂ52vW&R6÷'&V7FÇ’&V¦V7FVB2"Ô"66÷Râ ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢7FvR÷&FW"Â×WFF–öâÂg&W6†æW72Âf—'7BÖf–ÇW&RÂ†—7F÷&–6Â†6†–ærÂæBW†7Bæöæf–æÂ&V6V—BFW7G2â ¢¢¢¥&—6²76W76ÖVçC¢¢¢æòfÇ6R52÷"†—7F÷&–6ÂÖ7W'&VçB6öæfÆF–öâf÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBà ¢22225U$bÓ ¢¢¢¥7W&f6S¢¢¢Öæ–fW7BÖFW&—fVB–FVçF—G’æBW‡FW&æÂ&VÆV6RGFW7FF–öâ ¢¢¢¥F–W#¢¢¢ ¢¢¢¥F‡3¢¢¢6FÆöröÖæ–fW7Bæ§6öæÂ'VçF–ÖR–FVçF—G’Â&VÆV6RÖ7WBöVF—B67&—G2ÂW‡FW&æÂ'V–ÆFW"ÂGFW7FF–öâ66†VÖ2Â4’Â&Vv—7G'’ö6öæf–r&öGV6W'2â ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓÂ$UÓÂ$UÓ#R ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢7–6Æ–2–FVçF—G’w&‚Â6ÆVâ6÷W&6RÂW‡FW&æÂV×G’FW7F–æF–öâÂG&6¶VBÖ6÷’—6öÆF–öâÂFWFW&Ö–æ—7F–2'VæFÆRÂ&VÆV6RÖvæ÷7F–2&Vv—7G'’ö6öæf–r÷WGWBÂæBæò6÷W&6R&W—"â ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢'VçF–ÖRFW&—fW2–FVçF—G’g&öÒ6æöæ–6ÂÖæ–fW7B'—FW3²4’'V–ÆG2âW‡FW&æÂW†7BÖ†VB'F–f7BF†BW‡Æ–6—FÇ’&V6÷&G2&VÆV6UöFÖ—76–öãÔäõEôEDTÕDTFâ ¢¢¢¤†—7F÷&–6Â&V6öç7G'V7F–öã¢¢¢Â33cn(	—2Öæ–fW7BæB&Vv—7G'’&Wf–WrF‡&VG2æBF†RÆFW"cW†7B×F÷–2F÷F–öâvW&R6†V6¶VBâ ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢Öæ–fW7Bf—†VB×ö–çBÂW‡FW&æÂ'V–ÆB÷fW&–g’Â&Vv—7G'’FWFW&Ö–æ—6ÒÂ6öæf–rÂæB7W'&VçB4’â ¢¢¢¥&—6²76W76ÖVçC¢¢¢æò"Ô"FÖ—76–öâ6Æ–Ò÷"6÷W&6RöWf–FVæ6R7–6ÆRf÷VæBâ ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBâ ¢¢¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2Â*s"ãbÂW‡FW&æÂGFW7FF–öâ—2W†7BÖ†VB"Wf–FVæ6RÂæ÷BGW&&ÆR&VÆV6RFÖ—76–öâà ¢22225U$bÓ  ¢¢¢¥7W&f6S¢¢¢v÷fW&æVB'F–f7G2Â–æFW†W2ÂÖ—'&÷'2Â&öög2ÂwV–Fæ6RÂæBvVæW&FVBÖf–ÆR6ÆVçW ¢¢¢¥F–W#¢¢¢ô"ô2 ¢¢¢¥F‡3¢¢¢ƒ’'F–f7G2Â#2VF—BÖvFRf–ÆW2ÂV–v‡Bv÷fW&æVBFö72÷&öög2Â7W'&VçBwV–Fæ6RÂçfVçbò¢¦ÂæBVvrÖ–æfòò¢¦â ¢¢¢¤Æ–6&ÆR&WV—&VÖVçG3¢¢¢$UÓ’Â$UÓBÂ$UÓ#^(	5$UÓ#r ¢¢¢¥v†Bv2&Wf–WvVC¢¢¢&öGV6W"÷væW'6†—Â6æöæ–6Â7G'V7GW&RÂ†6†W2Â&öög2ÂÖ—'&÷"ö–æFW‚F÷öÆöw’Â†—7F÷&–6ÂÖVæ–ærÂ7W'&VçBwV–Fæ6RÂæBG&6¶VB×6÷W&6R6ÆVæÆ–æW72â ¢¢¢¤7W'&VçB&V†f–÷#¢¢¢7W'&VçB'F–f7G2&R6ö†W&VçC²g&÷¦Vâ6GW&W2&WF–â†—7F÷&–6ÂÖVæ–æs²vVæW&FVBVçf—&öæÖVçB÷6¶vRÖWFFF—2VçG&6¶VBâ ¢¢¢¥FW7BæBWf–FVæ6RVÆ—G“¢¢¢WFFW"ÒÖ6†V6¶ÂÖ—'&÷"66†VÖÂ–æFW‚†6‚ÂF‚Â6æöæ–6Â¥4ôâÂf–æÂÔÄbÂ6öæf–rÂ–ç7FÆÆ&–Æ—G’ÂæBW‡FW&æÂGFW7FF–öâ6†V6·2â ¢¢¢¥&—6²76W76ÖVçC¢¢¢æò7FÆR7F—fR6öÖÖæBÂ÷'†â&–æF–ærÂ÷"G&6¶VBvVæW&FVBVçf—&öæÖVçB&VÖ–ç2â ¢¢¢¤6öæ6ÇW6–öã¢¢¢4D•4d”TBà ¢222fÆ–FF–öâæBWf–FVæ6R&Wf–Wp §Â”BÂW'÷6RæBÖWF†öBÂ&Wf–WvVB7FFRÂ&W7VÇBÂö'6W'fF–öâæB7Vff–6–Væ7’À§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§ÂdÂÓÂ&÷fRÆ–æVvR–FVçF—G’æBW†7B÷&FW"F‡&÷Vv‚"ÖWFFFæB6öÖÖ—B6ö×&—6öâÂ&6VÆ–æRFSc(
fF‡&÷Vv‚ÖW&vRfSc–C~(
fÂ52ÂV6‚ÖW&vR—2F†RæW‡B.(	—2W†7B&6S²Væ–öâæBæWB6ö×&—6öâ&÷F‚6öçF–â#S‚F‡2À§ÂdÂÓ"Â÷&–v–æÂæB&VÖVF–ÂW†7BÖ†VBv÷&¶fÆ÷w2Â†VG2öbÂ33c2ÂÂ33cBÂÂ33cRÂ52Â'Vç2#“ƒ#C“SS‚Â#“ƒs3c3SC“rÂæB#“ƒ“3##Cƒ#"V6‚6ö×ÆWFVBrór¦ö'2À§ÂdÂÓ2Âf–æÂW†7BÖ†VBv÷&¶fÆ÷rÂ"Â33cb†VBf#“f6F3sn(
fÂ52Âµ'Vâ3SSCƒUÒ†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"ö7F–öç2÷'Vç2ó3SSCƒR’6ö×ÆWFVBÆÂ6WfVâ¦ö'27V66W76gVÆÇ’À§ÂdÂÓBÂF—&V7B'VçF–ÖRÂ6ö×F–&–Æ—G’Â66ææW"ÂÖVBÖ66†RÂæBæòÔ’ôò&ööbÂf–æÂ†VBÂ52ÂFW7BÆæR&âF†RF—&V7B6†V6¶W"æBF—&V7B÷7Fw&U5Â6öçG&7B7V—FW3²c*s"ãb&V6÷&G2#Sfö7W6VB76W2À§ÂdÂÓRÂWf–FVæ6RÂ66†VÖ2Âõ2Ó2f—‡GW&W2ö×WFF–öç2ÂæB—VÆ–æR&ööbÂf–æÂ†VBÂ52ÂFW7BÆæR&âFW7G2öWf–FVæ6VæBFW7G2ö÷2÷FW7Eö†FUöW–33…ö÷32ç–²c*s"ãb&V6÷&G2ÃS276W2À§ÂdÂÓbÂ"Ô&VÆV6RÖGFW7FF–öâæBæöæf–æÂÖ&÷VæF'’&ööbÂf–æÂ†VBÂ52Â6æ—G’¦ö"'V–ÇBæBfW&–f–VBF†RW‡FW&æÂ'VæFÆS²7W'&VçB6æöæ–6ÂÆör†2W†7B7FvRÓBæöæf–æÂf–ÇW&RÀ§ÂdÂÓrÂ&Wf–Wrf–æF–æw2æB7W'&VçBÖ†VB&Wf–Wv&–Æ—G’Âf–æÂ†VBÂ52ÂÆÂSBÆ–æVvRF‡&VG2&R&W6öÇfVC²f–æÂÂ33cb&Wf–Wr&W÷'G2æòÖ¦÷"—77VW2v–ç7Bf#“f6F3sn(
fÀ§ÂdÂÓ‚ÂÆFW"Ö6†ævR&Vw&W76–öâ6†V6²ÂfSc–C~(
fFò7W'&VçBF3sƒF>(
fÂ52ÂöæÇ’cc"ã2ãR6†ævVC²æò&Wf–WvVB–×ÆVÖVçFF–öâÂFW7BÂ66†VÖÂ÷"'F–f7B7W&f6R6†ævVBÀ ¤æòfÆ–FF–öâv2W†V7WFVB'’F†—2&Wf–Wrâ&W7VÇG2&÷fR&R–ç7V7FVB&W÷6—F÷'’æBv—D‡V"Wf–FVæ6Rà ¢222c’–×7BæB7FGW2÷7GW&P ¥6÷W&6S¢¢¥c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâcãã"¢¢à §Â—FVÒÂ7W'&VçB7FGW2Â"ÔVffV7BÂ&V6öÖÖVæFF–öâÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§Â„DRÔD•5CãFÂ'F–ÂÂF—&V7BÖöæÇ’6÷W&6R÷FööÆ–ær—2&W6VçC²Æ—fRõ2Ó2æBf–æÂ&–æF–ær&R'6VçBÂæò7FGW26†ævR&V6öÖÖVæFVBÀ§Â„DRÔD•5CãfÂ'F–ÂÂæ–æWFVVâ×7FvR7G'V7GW&RW†—7G2Â'WBf–æÂ7FvW26÷'&V7FÇ’&VÖ–â&Æö6¶VBÂæò7FGW26†ævR&V6öÖÖVæFVBÀ§Â„DRÔD•5Cã–Â'F–ÂÂF—&V7BÖöæÇ’'VçF–ÖRW†—7G3²Æ—fR÷7GW&RöFÖ—76–öâæBW&ÖæVçBv÷&F–ærG&–ævR&VÖ–âF÷vç7G&VÒÂæò7FGW26†ævR&V6öÖÖVæFVBÀ§Â„DRÔD•5CãÂ÷F–öæÂÂG&ç7÷'BÖæWWG&ÂÖVBÖ66†R&ööb&VÖ–ç2&W6W'fVC²æò7FGW27F–öâ—2WF†÷&—¦VBÂæò7FGW26†ævR&V6öÖÖVæFVBÀ§Â„DRÔD•5CRã&Â'F–ÂÂ7W'&VçBF—66—Æ–æR—2&W6W'fVBÂ'WBõ2Ó2õ"Ô"f–æÂ&÷w2æB6ö×æ–öç2Fòæ÷B–WBW†—7BÂæò7FGW26†ævR&V6öÖÖVæFVBÀ ¥c*|*s"ã^(	3"ãbW‡&W76Ç’&WF–âF†W6R7FGW6W2æB&ö†–&—B"Ôg&öÒ7&VF–ærc’Ö÷fVÖVçB÷"7W÷'F&–Æ—G’6Æ–Òà ¢222f–æF–æw0 ¤æòf–æF–æw2à ¢222Wf–FVæ6R&–çB…52$ôôc²ÖW&vVBv÷&² ¢2222â6öçG&7B6÷fW&vP ¤ÆÂ#rÆ–6&ÆR&WV—&VÖVçBw&÷W2&RV—F†W"4D•4d”TF÷"Dõtå5E$TÒ%’$õdTB$õTäD%–âæöæR—2äõB4D•4d”TF÷"Tä4ÄT&à ¤Wf–FVæ6S¢&÷fVB&W66÷–ær5$BÂ%42ÓF‡&÷Vv‚%42ÓRÂE"Ô4äôâÓBF‡&÷Vv‚E"Ô4äôâÓƒ²v—D‡V"&WòÂ7W'&VçBÖ–æ–×ÆVÖVçFF–öâæBFW7G2à ¢2222"âf–æÂ–×ÆVÖVçFF–öâ&öö` ¥F†R&Wf–Wr6÷fW&VBF†R6öÆRD"6VÆV7F÷"Â6ö×F–&–Æ—G’f:vFRÂ&VBÖöæÇ’&÷f–FW"Â'&–FvRFVÆWF–öâæB66ææW"ÂV&Æ–2&VFW"ô4Ä’æBÖVBÖ66†R&V†f–÷"ÂF—&V7B×6VÆV7F–öâFööÆ–ærÂ6ö×ÆWFRõ2Ó2WF†÷&—¦F–öâæB6¶WB7FFRÖ6†–æRÂWf–FVæ6R—VÆ–æRÂW‡FW&æÂGFW7FF–öâÂ–æFW†W2ÂÖ—'&÷'2Â&öög2ÂæBv÷fW&æVB'F–f7G2âæòW†V7WF&ÆR'&–FvRÂÇFW&æFR&÷f–FW"Â6V7&WB×fÇVR6W&–Æ—¦F–öâÂf–ÂÖ÷Vâ6¶WBF‚Â÷"fÇ6Rf–æÂ&VÆV6R52&VÖ–ç2à ¤Wf–FVæ6S¢v—D‡V"&WòÂVæv–æRöF"ò¢¦ÂFFW"ò¢¦Â6’ö6†V6·2ö6†V6µöF—&V7EöF%ö6öçG&7Bç–Â67&—G2ö÷2ö†FUöW–33…ö÷32ç–ÂFööÇ2öWf–FVæ6Rö†FUöW–33…ö÷32ç–Â66†VÖ2æBFW7G2à ¢22222âÆ–æVvR&VÖVF–F–öâ&öö` ¢¢Â33c2W7F&Æ—6†VBF†RF—&V7BÖöæÇ’–×ÆVÖVçFF–öâæB&–Ö'’FööÆ–ærâ ¢¢Â33cB6VçG&Æ—¦VB6ö×F–&–Æ—G’÷væW'6†—æBÖFRF†R"Ôæöæf–æÂ7FFRW‡Æ–6—Bâ ¢¢Â33cR6Æ÷6VB&WF—&VBÖ¶W’fÇVR×&VBæB66ææW"öFFÖfÆ÷r'—76W2â ¢¢Â33cb6Æ÷6VBF†R&VÖ–æ–ærõ2Ó2—6öÆF–öâÂf–ÆW7—7FVÒÂFW&Ö–æÂ×7FFRÂ&VÆV6RÖ–FVçF—G’ÂæBWf–FVæ6R×&Wf–Wv&–Æ—G’v2à ¤ÆÂ7F–öæ&ÆRF‡&VG2&R&W6öÇfVBÂF†V—"6÷'&V7F–öç27W'f—fR–â7W'&VçB6÷W&6RÂæBF†Rf–æÂ†VB&V6V—fVB6ÆVâ&Wf–Wrà ¤Wf–FVæ6S¢÷&–v–æÂ"Â33c3²&VÖVF–Â'2Â33cBÂÂ33cRÂæBÂ33cbÂÖWFFFÂF‡&VG2Âf–æÂ†VG2ÂæBFW&Ö–æÂ&Wf–Ww2à ¢2222BâfÆ–FF–öâæB4’&öö` ¥F†Rf–æÂ&Wf–WvVB6÷W&6R†VB—2f#“f6F3scƒƒs–CfC–6S#“#c“Scc“ƒ&âv—D‡V"7F–öç2'Vâ3SSCƒR6ö×ÆWFVBÆÂ6WfVâ¦ö'27V66W76gVÆÇ’Â–æ6ÇVF–ærF†RF—&V7B6†V6¶W"ÂF—&V7B÷7Fw&U5Â6öçG&7G2ÂWf–FVæ6Rôõ2FW7G2ÂÖ—'&÷"66†VÖÂ–æFW‚ö†6‚Â6æöæ–6Âöf–æÂÔÄbvFW2ÂæBW‡FW&æÂ&VÆV6RÖGFW7FF–öâ'V–ÆBâF†R"†VBæBÖW&vRG&VR&RWV—fÆVçBà ¤Wf–FVæ6S¢´v—D‡V"7F–öç2'Vâ3SSCƒUÒ†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"ö7F–öç2÷'Vç2ó3SSCƒR“²"Â33cc²c*s"ãbW†7BÖ†VB&V6÷&Bà ¢2222RâWf–FVæ6RæB&÷VæF'’&öö` ¥F†W&R&RæòÆ—fRõ2Ó2'—FW2ÂæòG&6¶VBf–æÂF—&V7B×6VÆV7F–öâ&–Ö'’ÂæBæò"Ô"FÖ—76–öââF†R7W'&VçB—VÆ–æRG'WF†gVÆÇ’7F÷2B7FvRBÂ†—7F÷&–6Â'&–FvRWf–FVæ6R—2–çFVw&—G’ÖöæÇ’Âõ2Ó"&VÖ–ç2&÷VæFVBFòÖVBÖ66†R7W÷'BÂæBc’õ÷Fö¶VâöFWÆ÷–ÖVçBö6Æ÷6V÷WBæöæ6Æ–×2&VÖ–â–çF7BâF†RöæÇ’ÆFW"6öÖÖ—B6†ævW2cÂæ÷B–×ÆVÖVçFF–öâà ¤Wf–FVæ6S¢v—D‡V"&WòÂVF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆöv²W†7B×F‚'6Væ6R6†V6·3²c*|*s"ã^(	3"ãc²6ö×&—6öâfSc–C~(
fF3sƒN(
fà ¢222Fö2FVÇF6æF–FFW2…bÔ6æöâöæÇ’ ¢¢¢¤6æF–FFR”C¢¢¢D2Ó ¢¢¢¥W&ÖæVçBbF&vWBæBW†7BÆö6F÷#¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâcãã"Â&÷w2„DRÔD•5CãFæB„DRÔD•5Cã– ¢¢¢¤&6—3¢¢¢4äôâÔ•4ÔD4† ¢¢¢¤FVÇF¢¢¢&WÆ6R7F—fR'&–FvRÖfÆÆ&6²÷&÷f–FW"×&—G’v÷&F–ærv—F‚F†RF—&V7BÖöæÇ’6ö×ÆWF–öâ6VÖçF–72Ç&VG’W7F&Æ—6†VB–âc*s"ãS²&WF–â7W'&VçB7FGW6W2â ¢¢¢¥v‡“¢¢¢7W'&VçBc’ãb7F–ÆÂFW67&–&W2'&–FvRfÆÆ&6²÷&—G’Âv†–ÆRF†RW†7B×F÷–2WF†÷&—G’æBÖW&vVB–×ÆVÖVçFF–öâW6RF—&V7B÷7Fw&U5ÂÇW2&WF—&VB×G&ç7÷'BVæf÷&6VÖVçBâ ¢¢¢¤Wf–FVæ6S¢¢¢c’ãb&÷rãF7F–ÆÂÆ—7G2'&–FvRfÆÆ&6²÷&÷f–FW"&—G“²&÷rã–&VÖ–ç2F—FÆVB(	ÄD.(	6'&–FvR&—G’bVçb6öææV7F—f—G’î(	Òc*s"ãR&VFVf–æW2&÷F‚f÷"F—&V7BÖöæÇ’÷7GW&Râ ¢¢¢¤W†7B6æöâW†6W'C¢¢¢(	ÄD.(	6'&–FvR&—G’bVçb6öææV7F—f—Gž(	Ò ¢¢¢¥c’7F–öã¢¢¢æò7FGW26†ævR&V6öÖÖVæFVBà ¤DT4•4”ôã¢ÔU$tTBtõ$²44UD$ÄP ¢22"ã‚’"Ób&VÖVF–F–öâÂÒõ2Ó2„DRÔU”33€ ¥&Wf–Wr7VÖÖ' ¢¢÷2Wf–FVæ6R&÷fW26ö×ÆWF–öâöbF†R&÷fVBÆî(	—2Gvò×†6R÷W&F–öã¢&÷VæFVB×WF&ÆR&öÆR×&÷f—6–öæ–ær†6RföÆÆ÷vVB'’âWF†÷&—¦F–öâÖ&÷VæBF—&V7B÷7Fw&U5Â&VBÖöæÇ’6GW&Râ&–Çv’æBFÖ–æ—7G&F—fR5ÂvW&RW6VBöæÇ’f÷"&öÆR–ç7V7F–öâÂ&÷f—6–öæ–ærÂfW&–f–6F–öâÂæB6ÆVçW²F†R6GW&RW6VBF—&V7B7–6÷vÂW†V7WFVB¦W&ò5Âw&—FW2ÂÖFRæò&–Çv’4Ä’6ÆÂÂW6VBöæRGFV×BÂæBÖFRæò&WG'’âWf–FVæ6Rö–çFW'3¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&–Çv’×7FGW2çG‡FF‡&÷Vv‚BÖÆöv–âÖF—6&ÆVBçG‡F²WF†÷&—¦F–öâæ§6öæ²÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öæ²÷2Ó2÷fÆ–FF–öå÷&V6V—Bæ§6öæâ ¢¢Æ—fR&VfÆ–v‡Bf÷VæB†FUö÷væW&æB†FU÷'vÇ&VG’&W6VçB2äôÄôt”æ&öÆW2æBf÷VæBF†RFVF–6FVBF&vWB&öÆW2†FU÷&VFW&æB†FUö÷35÷&VFW&'6VçBâF†RF&vWB&öÆW2vW&RF†Vâ&÷f—6–öæVBÂfW&–f–VBv–ç7BF†R6WfVâÖfÆrÆV7B×&—f–ÆVvR&VF–6FRÂæBÆVgBv—F‚†FUö÷35÷&VFW&Æöv–âF—6&ÆVBæB—G277v÷&B6ÆV&VBâWf–FVæ6Rö–çFW'3¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡FÂ"×&öÆR×&÷f—6–öæ–ærçG‡FÂ2×&VFW"×fW&–f–6F–öâçG‡FÂBÖÆöv–âÖF—6&ÆVBçG‡Fâ ¢¢F†R6GW&R6¶WB—2–çFW&æÆÇ’6ö†W&VçBæB6ö×ÆWFS¢—B6öçF–ç2F†RW†7BFVâ&WV—&VB&–Ö&–W2Â&W÷'G256Â†2W†—B6öFRÂV×G’7FFW'"ÂF†RW†7B7V66W726VçF–æVÂÂÖF6†–ær6æöæ–6Â¥4ôâæB6†V6·7V×2ÂÆÂVÆWfVâFV6—6—fR&VF–6FW2G'VRÂÆÂV–v‡B–æFWVæFVçB×fÆ–FF–öâ&VF–6FW2G'VRÂæB6VÆVBFW&Ö–æÂ6öçG&öÂ7FFRâWf–FVæ6Rö–çFW'3¢÷2Wf–FVæ6RÂ÷2Ó2ö6†V6·7V×2ç6†#SfÂ&W7VÇE÷7VÖÖ'’æ§6öæÂfÆ–FF–öå÷&V6V—Bæ§6öæÂW†—Eö6öFRçG‡FÂ7FF÷WBæÆövÂ7FFW'"æÆöv²6öçG&öÂöWF†÷&—¦F–öåö6öç7VÖVBæ§6öæ²6öçG&öÂòæ6GW&Ræ6öÖÖ—GFVFâ ¢¢&WòfÆ–FF–öâ6öæf—&×2F†BF†RFVâ6¶WB&–Ö&–W2æBGvVÇfR÷W&F÷"&V6÷&G2&RG&6¶VBB7W'&VçBÖ–ææB'—FRÖ–FVçF–6ÂFò÷2Wf–FVæ6RâF†R'VææW"ÂfÆ–FF÷"ÂæB6WfVâõ2Ó266†VÖ2&R&W6VçBæBVæ6†ævVB&WGvVVâF†RWF†÷&—¦VB6÷W&6R6öÖÖ—BæB7W'&VçB„TBâWf–FVæ6Rö–çFW#¢&WòÂ„TBSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–f²6ö×&—6öâg&öÒ6÷W&6R6öÖÖ—BC6FCf#“sSCC&Cv“3#–66ffc–ccCƒ6–CFfVS&²F—&V7BF‚æB'—FR6†V6·2â ¢¢F†RF—&V7B×6VÆV7F–öâ&–Ö'’Âõ2Ó2WFFW"&–æF–æw2Â‡VÖâWf–FVæ6R–æFW‚&÷w2ÂÖ6†–æRÖ—'&÷"&÷w2ÂæBFVâ6–&Æ–ærF‚&öög2&Ræ÷B–WB&W6VçBâF†R&÷fVBÆâ76–vç2F†÷6RFÖ—76–öâæBf–æÂÖ–çFVw&F–öâö&Æ–vF–öç2Fò"Óe"Ô"Â6òF†V—"'6Væ6R&WfVçG2f–æÂv÷fW&æVBFÖ—76–öâ'WBFöW2æ÷B–çfÆ–FFRõ2Ó2÷"&WV—&Ræ÷F†W"FF&6R'VââWf–FVæ6Rö–çFW'3¢&WòÂ&÷VæFVB6V&6†W2æBW†7B×F‚6†V6·2&V6÷&FVB&VÆ÷s²&÷fVBÆâÂF÷vç7G&VÒFÖ—76–öâ&÷VæF'’â ¢¢W†7BÖ'—FR&öGV7B÷væW"&÷fÂÂF†R6ö×ÆWFR&öÆÆ&6²öbâVç7V66W76gVÂ&RÖWF†÷&—¦F–öâ6öææV7F–öâ6WVVæ6RÂæB6W'F–â&V6÷fW'’FWF–Ç2&R&W6W'fVB2÷W&F÷"×&V6÷&B76W'F–öç2&F†W"F†â–æFWVæFVçB'F–f7G2âF†W6RVÆ–f–6F–öç2Fòæ÷B6öæfÆ–7Bv—F‚F†RF—&V7FÇ’&÷fVâf–æÂ&öÆR÷7GW&RÂöæRÖGFV×BWF†÷&—¦F–öâ6öç7V×F–öâÂ7V66W76gVÂ6GW&RÂ÷"6VÆVBFW&Ö–æÂ7FFRâWf–FVæ6Rö–çFW'3¢÷2Wf–FVæ6RÂ5D”ôåõ$Uõ%BæÖFÂWF†÷&—¦F–öâæ§6öæÂ&öÆR×&÷f—6–öæ–æró2×&VFW"×fW&–f–6F–öâçG‡FÂ6öçG&öÂöWF†÷&—¦F–öåö6öç7VÖVBæ§6öæâ ¢¢õ2Ó27WÆ–W2Æ—fRFV6†æ–6ÂWf–FVæ6R&VÆWfçBFò„DRÕ4Uã6Â„DRÔD•5CãFÂæBF†RF—&V7BÖ6öææV7F—f—G’ÖVæ–æröb„DRÔD•5Cã–â—B7&VFW2æòc’7FGW2Ö÷fVÖVçC¢„DRÕ4Uã6&VÖ–ç2FöæVÂv†–ÆR„DRÔD•5CãFæB„DRÔD•5Cã–&VÖ–â'F–ÆâWf–FVæ6Rö–çFW'3¢÷2Wf–FVæ6RÂæöæ6Æ–×2æ§6öæÂ&öÆRWf–FVæ6RÂ6GW&R6¶WC²c’ã2(	B6æöâ„DR'V–ÆB6†V6¶Æ—7B6W&F–öâÂ*u7V'F6²„DRÕ4Uã3²c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâÂ*u7V'F6²„DRÔD•5CãBæB*u7V'F6²„DRÔD•5Cã’â ¢¢F†R66WFæ6R&W7VÇB—2õ244UD$ÄVâæòõ2Ó2&W'VâÂ&öÆR&öÆÆ&6²ÂFÖ–æ—7G&F—fR×&öÆR6GW&RW†6WF–öâÂ÷"&VÖVF–Â6†ævRFòF†R'VææW"ÂfÆ–FF÷"Â66†VÖ2Â÷"FW7G2—2&WV—&VBà ¥&WòWf–FVæ6RfÆ–FF–öâ7VÖÖ' ¢¢ö'6W'fVB&Wò&ö÷C¢6öææV7FVB&W÷6—F÷'’&ö÷Böf÷"×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c&â ¢¢ö'6W'fVB„TC¢Sƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–fâ ¢¢'&æ6‚÷"FWF6†VB7FFS¢Ö–æ²6öææV7FVB&VÖ÷FR'&æ6‚Âæ÷BFWF6†VBâ ¢¢v÷&¶–ær×G&VR7FGW2&Vf÷&RfÆ–FF–öã¢âôâF†R6öææV7FVB&WòW‡÷6W26öÖÖ—GFVB&VÖ÷FR7FFRÂæ÷Bâ÷W&F÷"ÖÆö6Âv÷&¶–ærG&VRâ ¢¢v÷&¶–ær×G&VR7FGW2gFW"fÆ–FF–öã¢âôæBVæ6†ævVBâfÆ–FF–öâv2&VBÖöæÇ’â ¢¢&VBÖöæÇ’fÆ–FF–öâÖWF†öG2W6VC¢&W÷6—F÷'’ÖWFFF–ç7V7F–öã²6÷W&6R×FòÔ„TB6öÖÖ—B6ö×&—6öã²F—&V7Bf–ÆRfWF6ƒ²&÷VæFVBW†7B×7G&–ær6V&6ƒ²W†7B×F‚W†—7FVæ6R6†V6·3²'—FRÖÆVæwF‚Âv—BÖ&Æö"–FVçF—G’ÂæB4„Ó#Sb6ö×&—6öââ ¢¢&Wò×&W6–FVçBWf–FVæ6RF‡26†V6¶VC¢ÆÂFVâõ2Ó2&–Ö&–W3²ÆÂGvVÇfR÷W&F÷"&V6÷&G3²F†R'VææW#²F†RfÆ–FF÷#²ÆÂ6WfVâõ2Ó266†VÖ3²F†RWf–FVæ6RWFFW#²‡VÖâWf–FVæ6R–æFWƒ²Ö6†–æRWf–FVæ6RÖ—'&÷#²F—&V7B×6VÆV7F–öâF&vWC²æBF†RFVâ6–&Æ–ærF‚×&ööbF&vWG2â ¢¢G&6¶VB÷"ÖW&vV&ÆRWf–FVæ6R6öæf—&ÖVC¢ÆÂGvVçG’×Gvò÷2Wf–FVæ6Rf–ÆW2&RG&6¶VBB7W'&VçB„TBæBÖF6‚F†R'VæFÆR'—FW2âF†R'VææW"ÂfÆ–FF÷"ÂæB66†VÖ2&RG&6¶VBæB&VÖ–æVBVæ6†ævVBg&öÒF†RWF†÷&—¦VB6÷W&6R6öÖÖ—Bâ ¢¢&W÷'FVBWf–FVæ6Ræ÷Bf÷VæC¢F—&V7B×6VÆV7F–öâ&–Ö'’ÂFVâ6–&Æ–ærF‚&öög2ÂæBõ2Ó2&–æF–æw2–âF†RWFFW"Â‡VÖâWf–FVæ6R–æFW‚ÂæBÖ6†–æRWf–FVæ6RÖ—'&÷"â ¢¢Wf–FVæ6R&W6VçB'WB–væ÷&VB÷"VæÖW&vV&ÆS¢æöæRâ ¢¢÷2Wf–FVæ6RæB&Wò6öçG&F–7F–öç3¢æöæR–âF†R'VæFÆR×FòÕ&Wò'—FR6ö×&—6öâ÷"6÷W&6RÖ–FVçF—G’6†V6²â ¢¢F—'G’×G&VR&÷fVææ6R6öæ6W&ç3¢æöæRö'6W'f&ÆR–âF†R6öææV7FVB&VÖ÷FR&Wòâæò76W'F–öâ—2ÖFR&÷WBâ÷W&F÷"ÖÆö6Â6†V6¶÷WBF†B—2æ÷B&W&W6VçFVB'’6öÖÖ—GFVB7FFRà ¤'F–f7BF‚÷"Æ&VÃ  ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö6†V6·7V×2ç6†#Sf ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö6öÖÖæG2çG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öæ ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öVçe÷&W6Væ6Ræ§6öæ ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öW†—Eö6öFRçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öæöæ6Æ–×2æ§6öæ ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷&W7VÇE÷7VÖÖ'’æ§6öæ ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷7FFW'"æÆöv ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷7FF÷WBæÆöv ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷fÆ–FF–öå÷&V6V—Bæ§6öæ  ¥&W÷'FVB'’÷2Wf–FVæ6S¢–W0 ¥&WV—&VB'’&÷fVBÆã¢–W0 ¥&W6VçB–â&Wó¢–W0 ¥G&6¶VB÷"ÖW&vV&ÆS¢–W0 ¤ÆÆ÷vVB&ö÷C¢–W0 ¤6öçFVçB÷"&ööbf7G26†V6¶VC¢–W0 ¥&WòfÆ–FF–öâ7FGW3¢&WòÖ6öæf—&ÖVBâÆÂFVâf–ÆW2&RG&6¶VBæB'—FRÖ–FVçF–6ÂFò÷2Wf–FVæ6RâF†R6æF–FFR6†V6·7VÒÆVFvW"4„Ó#Sb—2S#fS#VFS3ssSV#Fc#sf†C†Ccv3F&6V3c63&cs–Ff6SsƒcƒFS6&Sf&3&à ¤Wf–FVæ6Rö–çFW#¢&WòÂ„TBSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–fÂW†7BF‡2&÷fS²÷2Wf–FVæ6RÂ÷2Ó2ö6†V6·7V×2ç6†#Sfà ¤'F–f7BF‚÷"Æ&VÃ  ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&Bô5D”ôåõ$Uõ%BæÖF ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&BôD•44õdU%•ôd”äD”äu2æÖF ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&BöWF†÷&—¦F–öâæ§6öæ ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&Bö6öçG&öÂòæ6GW&Ræ6öÖÖ—GFVF ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&Bö6öçG&öÂöWF†÷&—¦F–öåö6öç7VÖVBæ§6öæ ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&Bö6öçG&öÂöÆVæ6‚æÖ&¶W& ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æró×&–Çv’×7FGW2çG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æró"×&öÆR×&÷f—6–öæ–ærçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æró2×&VFW"×fW&–f–6F–öâçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æróBÖÆöv–âÖF—6&ÆVBçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–ærö6†V6·7V×2ç6†#Sf  ¥&W÷'FVB'’÷2Wf–FVæ6S¢–W0 ¥&WV—&VB'’&÷fVBÆã¢–W2Â2÷W&F–öæÂWF†÷&—¦F–öâÂ6öçG&öÂÂæBCÔC‚7W÷'B&V6÷&G3²&W÷6—F÷'’&WFVçF–öâöbF†Ræ6–ÆÆ'’&V6÷&G2—27W÷'F–ær&÷fVææ6R&F†W"F†â6ö×ÆWF–öâöbv÷fW&æVBFÖ—76–öâà ¥&W6VçB–â&Wó¢–W0 ¥G&6¶VB÷"ÖW&vV&ÆS¢–W0 ¤ÆÆ÷vVB&ö÷C¢–W0 ¤6öçFVçB÷"&ööbf7G26†V6¶VC¢–W0 ¥&WòfÆ–FF–öâ7FGW3¢&WòÖ6öæf—&ÖVBâÆÂGvVÇfRf–ÆW2&RG&6¶VBæB'—FRÖ–FVçF–6ÂFò÷2Wf–FVæ6RâF†R&öÆRÖWf–FVæ6R6†V6·7VÒÆVFvW"4„Ó#Sb—2““ƒ–FF&Cf6VCc“3v3“F3S†C63FSCV#sFV3c–&Cs–VFC#c–scf33fFà ¤Wf–FVæ6Rö–çFW#¢&WòÂ„TBSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–fÂW†7BF‡2&÷fS²÷2Wf–FVæ6RÂWF†÷&—¦F–öâæ§6öæÂ6öçG&öÂò¦Â&öÆR×&÷f—6–öæ–ærö6†V6·7V×2ç6†#Sfà ¤'F–f7BF‚÷"Æ&VÃ  ¢¢67&—G2ö÷2ö†FUöW–33…ö÷32ç– ¢¢FööÇ2öWf–FVæ6Rö†FUöW–33…ö÷32ç– ¢¢66†VÖ2ö†FUöW–33…ö÷35öWF†÷&—¦F–öâçcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35öF%÷÷7GW&U÷7VÖÖ'’çcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35öVçe÷&W6Væ6Rçcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35öf–ÇW&U÷&V6V—Bçcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35öæöæ6Æ–×2çcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35÷&W7VÇE÷7VÖÖ'’çcæ§6öæ ¢¢66†VÖ2ö†FUöW–33…ö÷35÷fÆ–FF–öå÷&V6V—Bçcæ§6öæ  ¥&W÷'FVB'’÷2Wf–FVæ6S¢–W0 ¥&WV—&VB'’&÷fVBÆã¢–W0 ¥&W6VçB–â&Wó¢–W0 ¥G&6¶VB÷"ÖW&vV&ÆS¢–W0 ¤ÆÆ÷vVB&ö÷C¢–W0 ¤6öçFVçB÷"&ööbf7G26†V6¶VC¢–W0 ¥&WòfÆ–FF–öâ7FGW3¢&WòÖ6öæf—&ÖVBâÆÂæ–æR6÷W&6R'F–f7G2&RG&6¶VBæBVæ6†ævVB&WGvVVâF†RWF†÷&—¦F–öâÖ&÷VæB6÷W&6R6öÖÖ—BæB7W'&VçB„TBâ÷2Wf–FVæ6R–æFWVæFVçFÇ’&W÷'G2fÆ–B6÷W&6R–FVçF—G’Â'VææW"–FVçF—G’ÂfÆ–FF÷"–FVçF—G’ÂæB66†VÖfÆ–FF–öâà ¤Wf–FVæ6Rö–çFW#¢&WòÂ6ö×&—6öâC6FCf#“sSCC&Cv“3#–66ffc–ccCƒ6–CFfVS"ââæSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–f²÷2Wf–FVæ6RÂWF†÷&—¦F–öâæ§6öæÂ÷2Ó2÷fÆ–FF–öå÷&V6V—Bæ§6öæà ¤'F–f7BF‚÷"Æ&VÃ  ¢¢FööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç– ¢¢Fö72öWf–FVæ6Rô”äDU‚æ§6öæ ¢¢'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆ  ¥&W÷'FVB'’÷2Wf–FVæ6S¢–W2Â2÷WG7FæF–ærF÷vç7G&VÒFÖ—76–öâ7W&f6W0 ¥&WV—&VB'’&÷fVBÆã¢–W2Âf÷""Óe"Ô"v÷fW&æVBFÖ—76–öã²æòÂf÷"õ2Ó2÷W&F–öæÂ66WFæ6P ¥&W6VçB–â&Wó¢–W0 ¥G&6¶VB÷"ÖW&vV&ÆS¢–W0 ¤ÆÆ÷vVB&ö÷C¢–W0 ¤6öçFVçB÷"&ööbf7G26†V6¶VC¢–W0 ¥&WòfÆ–FF–öâ7FGW3¢&WòÖ6öæf—&ÖVBf–ÆW2v—F‚&WòÖæ÷BÖf÷VæBõ2Ó2&–æF–æw2â&÷VæFVB66RÖ–ç6Vç6—F—fR6V&6†W2f÷"÷2Ó6Â÷36Â†FUöW–33…ö÷36ÂW–33‚æ÷36ÂæBF—&V7EöF%÷6VÆV7F–öâç6æ6†÷F&WGW&æVB¦W&òõ2Ó2&–æF–ær†—G2–âF†W6RF‡&VRf–ÆW2à ¤Wf–FVæ6Rö–çFW#¢&WòÂW†7BF‡2&÷fRB„TBSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–f²6V&6‚ÖWF†öC¢6ö×ÆWFRÖf–ÆRW†7B×7G&–ær6V&6‚Â66RÖ–ç6Vç6—F—fRÂF—&V7Bf–ÆRfWF6‚à ¤'F–f7BF‚÷"Æ&VÃ  ¢¢'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæ  ¥&W÷'FVB'’÷2Wf–FVæ6S¢–W2Â2â÷WG7FæF–ærF÷vç7G&VÒ'F–f7@ ¥&WV—&VB'’&÷fVBÆã¢–W2Âf÷""Óe"Ô"v÷fW&æVBFÖ—76–öã²æòÂf÷"õ2Ó2÷W&F–öæÂ66WFæ6P ¥&W6VçB–â&Wó¢æð ¥G&6¶VB÷"ÖW&vV&ÆS¢æð ¤ÆÆ÷vVB&ö÷C¢–W0 ¤6öçFVçB÷"&ööbf7G26†V6¶VC¢æð ¥&WòfÆ–FF–öâ7FGW3¢&WòÖæ÷BÖf÷VæBâW†7B×F‚fWF6‚&WGW&æVBæ÷Bf÷VæC²66RÖ–ç6Vç6—F—fR6V&6‚f÷"F—&V7EöF%÷6VÆV7F–öâç6æ6†÷F7&÷72F†R&Wò&WGW&æVBæò'F–f7BBF†R&WV—&VBF‚à ¤Wf–FVæ6Rö–çFW#¢&WòÂW†7B×F‚fWF6‚æB&÷VæFVB&W÷6—F÷'’6V&6‚B„TBSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–fà ¤'F–f7BF‚÷"Æ&VÃ  ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö6†V6·7V×2ç6†#SbçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö6öÖÖæG2çG‡BçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öâçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öVçe÷&W6Væ6Ræ§6öâçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öW†—Eö6öFRçG‡BçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öæöæ6Æ–×2æ§6öâçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷&W7VÇE÷7VÖÖ'’æ§6öâçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷7FFW'"æÆörçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷7FF÷WBæÆörçF…÷&ööbçG‡F ¢¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷fÆ–FF–öå÷&V6V—Bæ§6öâçF…÷&ööbçG‡F  ¥&W÷'FVB'’÷2Wf–FVæ6S¢–W2Â2÷WG7FæF–ærF÷vç7G&VÒ'F–f7G0 ¥&WV—&VB'’&÷fVBÆã¢–W2Âf÷""Óe"Ô"v÷fW&æVBFÖ—76–öã²æòÂf÷"õ2Ó2÷W&F–öæÂ66WFæ6P ¥&W6VçB–â&Wó¢æð ¥G&6¶VB÷"ÖW&vV&ÆS¢æð ¤ÆÆ÷vVB&ö÷C¢–W0 ¤6öçFVçB÷"&ööbf7G26†V6¶VC¢æð ¥&WòfÆ–FF–öâ7FGW3¢&WòÖæ÷BÖf÷VæBâW†7B×F‚fWF6‚f÷"F†R6–&Æ–ærF‚×&ööbfÖ–Ç’&WGW&æVBæ÷Bf÷VæBâ66R×6Vç6—F—fR&÷VæFVB6V&6‚öbVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öf÷"F…÷&ööf&WGW&æVB¦W&ò†—G2à ¤Wf–FVæ6Rö–çFW#¢&WòÂW†7BF‡2&÷fRæB&÷VæFVBF‚6V&6‚B„TBSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–fà ¤f–æF–æw0 £âf–æF–ær”C¢bÓ ¢v†B–÷Rö'6W'fVC¢F†R÷W&F–öâW6VBF†R&÷fVBÆî(	—2GvòF—7F–æ7BWF†÷&—G’&÷VæF&–W2â&–Çv’æBFÖ–æ—7G&F—fR5ÂvW&R6öæf–æVBFòF&vWB–ç7V7F–öâÂ&VFW"×&öÆR&÷f—6–öæ–ærÂ&VFW"fW&–f–6F–öâÂæBFW&Ö–æÂ7&VFVçF–Â6ÆVçWâF†RWF†÷&—¦F–öâÖ&÷VæB6GW&RF†VâW6VBF—&V7B÷7Fw&U5ÂöæÇ’ÂW†V7WFVBæò5Âw&—FW2ÂÖFRæò&–Çv’4Ä’6ÆÂÂW6VBöæRGFV×BÂæBÖFRæò&WG'’â ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&–Çv’×7FGW2çG‡FF‡&÷Vv‚BÖÆöv–âÖF—6&ÆVBçG‡F²WF†÷&—¦F–öâæ§6öæ²÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öæ²6öçG&öÂöWF†÷&—¦F–öåö6öç7VÖVBæ§6öæâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢6ö×ÆWFRF†R&÷VæFVB×WF&ÆR&öÆR&V7W'6÷"&Vf÷&R6öç7G'V7F–ærWF†÷&—¦F–öâ'—FW2ÂF†VâW†V7WFRF†RVæ6†ævVBF—&V7BÖöæÇ’÷&VBÖöæÇ’ööæRÖGFV×B6GW&R6öçG&7Bâ ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVC²F†R7W÷'F–ær&V6÷&G2æB6¶WB&RG&6¶VBæB'—FRÖ–FVçF–6ÂFò÷2Wf–FVæ6Râ ¢v‡’—BÖGFW'3¢—B6W&FW2WF†÷&—¦VBFF&6R6WGWg&öÒF†R6GW&^(	—27Å÷w&—FW3Ó6Æ–ÒæB&÷fW2F†BFÖ–æ—7G&F—fR×&öÆRW6RF–Bæ÷BvV¶VâF†R6GW&R&VF–6FRâ ¢&Æö6¶W"f÷"66WFæ6S¢æò ¢b7W÷'BÂöæÇ’–b&VÆ–VBöã¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâÂ*sã"6öçfVçF–öç2Â(	Ä÷2F6·2…òÖöæÇ’W†V7WF–öã²Wf–FVæ6R&WV—&VB’î(	Ò ¢6æöâ&ööbW†6W'BÂöæÇ’–bb7W÷'B—2W6VC¢(	Ä÷2F6·2ÕU5B&RW†V7WFVB'’F†Rò†‡VÖâ÷W&F÷"’öæÇ’î(	Ò £"âf–æF–ær”C¢bÓ" ¢v†B–÷Rö'6W'fVC¢&VfÆ–v‡BW7F&Æ—6†VBFF&6R&–Çv–ÂFÖ–æ—7G&F—fR–FVçF—G’÷7Fw&W6Â÷7Fw&U5ÂrãfÂF†R&WV—&VB66†VÖ2æBf—fR&VÆF–öç2ÂV×G’&÷VæFVBT$Ä”2×w&—FRf–æF–æw2ÂW†—7F–ær†FUö÷væW&æB†FU÷'väôÄôt”æ&öÆW2ÂæB'6Væ6Röb†FU÷&VFW&æB†FUö÷35÷&VFW&â ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡Fâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢–ç7V7BÆ—fR&öÆRæBö&¦V7B7FFR&Vf÷&Rç’×WFF–öã²7F÷&F†W"F†â–æfW"FF&6R×&öÆRW†—7FVæ6R÷"7V—F&–Æ—G’â ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVB&V6÷&C²W‡FW&æÂFF&6R7FFR—2&÷fVâ'’F†R6GW&VB&VfÆ–v‡BÂæ÷B'’&Wòâ ¢v‡’—BÖGFW'3¢F†R&öÆRFV6—6–öâ—2&6VBöâö'6W'fVBÆ—fR7FFRâF†RWf–FVæ6RF—7F–æwV—6†W2W†—7F–ær„DRÖæÖVB&öÆW2g&öÒF†R'6VçBF6²×7V6–f–2&VFW"&öÆW2â ¢&Æö6¶W"f÷"66WFæ6S¢æò ¢b7W÷'BÂöæÇ’–b&VÆ–VBöã¢c’ã2(	B6æöâ„DR'V–ÆB6†V6¶Æ—7B6W&F–öâÂ*u7V'F6²„DRÕ4Uã2(	Bw&çG2òDDÂÆV7B×&—f–ÆVvR÷7GW&Râ ¢6æöâ&ööbW†6W'BÂöæÇ’–bb7W÷'B—2W6VC¢(	Ä¶VWD"w&çG2æBDDÂ'F–f7G27W'&VçBæB6öç6—7FVçBv—F‚ÆV7N(	&—f–ÆVvR÷7GW&Rf÷"W'6—7FVæ6RöbV&Æ–2–ÆöG2î(	Ò £2âf–æF–ær”C¢bÓ2 ¢v†B–÷Rö'6W'fVC¢&÷f—6–öæ–ærWf–FVæ6R6†÷w27V66W76gVÂ7&VF–öâæBw&çB6öÖÖæB7FGW6W3²†FU÷&VFW&—2äôÄôt”æ6&–Æ—G’&öÆS²†FUö÷35÷&VFW&v27&VFVB2Æöv–âv—F‚”ä„U$•FÂ6öææV7F–öâÆ–Ö—B&ÂæòF—7Æ–VBVÆWfFVB6ÇW7FW"fÆw2ÂæB7F—fRÖVÖ&W'6†—–â†FU÷&VFW&â ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró"×&öÆR×&÷f—6–öæ–ærçG‡Fâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢W7F&Æ—6‚FVF–6FVB&VFW"–FVçF—G’6&ÆRöb6F—6g––ærF†RÖW&vVBÆV7B×&—f–ÆVvR6GW&R&VF–6FRv—F†÷WB6†æv–ærF†R'VææW"ÂfÆ–FF÷"Â66†VÖ2ÂFW7G2Â÷"Wf–FVæ6R6öçG&7Bâ ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVB&V6÷&C²F†RFF&6R×WFF–öâ—G6VÆb—2W‡FW&æÂ7FFRâ ¢v‡’—BÖGFW'3¢F†RFVF–6FVB&öÆRÖ¶W2F†RW†—7F–ær66WFæ6R&VF–6FRW†V7WF&ÆRv—F†÷WBW6–ær÷7Fw&W6f÷"6GW&Râ ¢&Æö6¶W"f÷"66WFæ6S¢æò £Bâf–æF–ær”C¢bÓB ¢v†B–÷Rö'6W'fVC¢&VFW"fW&–f–6F–öâ&â2†FUö÷35÷&VFW&–â&VBÖöæÇ’G&ç67F–öâv—F‚6V&6‚F‚†FRÂV&Æ–6²ÆÂ6WfVâÆV7B×&—f–ÆVvRfÆw2vW&RfÇ6S²&WV—&VB6öÇVÖâÂ6öç7G&–çBÂ&÷VæF'’×f–WrÂæB'F—F–öâÖWFFFvW&Rf—6–&ÆS²fW&–f–6F–öâVæFVBv—F‚$ôÄÄ$4¶â ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró2×&VFW"×fW&–f–6F–öâçG‡Fâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢&÷fRF†RW†7B'VçF–ÖR&VFW"&VF–6FRæB&WV—&VBÖWFFFf—6–&–Æ—G’&Vf÷&R6öç7G'V7F–æræB6öç7VÖ–ærF†RWF†÷&—¦F–öââ ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVB&V6÷&C²'VçF–ÖRFF&6R7FFR—2&÷fVâ'’÷2Wf–FVæ6Râ ¢v‡’—BÖGFW'3¢F†—2—2F—&V7BWf–FVæ6RF†BF†RF6²×7V6–f–2&öÆRÖWBF†R6GW&R6öçG&7Bv†–ÆRÆ6¶–ærVÆWfFVBÂ66†VÖÖ7&VFRÂ÷"&VÆF–öâ×w&—FR6&–Æ—G’â ¢&Æö6¶W"f÷"66WFæ6S¢æò £Râf–æF–ær”C¢bÓR ¢v†B–÷Rö'6W'fVC¢6æöæ–6ÂWF†÷&—¦F–öâ&÷VæB'Vâ”B÷32×&öÆVf—‚ÖfFC6#s“#s#CSc–v3#Fcƒ6Â6÷W&6R6öÖÖ—BC6FCf#“sSCC&Cv“3#–66ffc–ccCƒ6–CFfVS&ÂGvòÖ†÷W"UD2v–æF÷rÂWF†÷&—¦F–öâ4„Ó#Sb“6&6–Cƒ“#cV“#sf#CscfFS33&&F3–S&6FCS–cs6fFf6ƒVVÂ'VææW"æBfÆ–FF÷"–FVçF—F–W2Â–çFW'&WFW"–FVçF—G’ÂF&vWBÂ&–Ç2ÂVW'’÷&FW"ÂW†7B6÷VçG2Â6æF–FFR&ö÷BÂF‡&VR&wbfV7F÷'2ÂæBF†RöæRÖGFV×B'VÆRâF†R6öçG&öÂ&V6÷&B&÷fW2öæR6öç7VÖVBÆVæ6‚æB6VÆVBFW&Ö–æÂ7FFRâF†R÷W&F÷"&V6÷&B7FFW2F†BF†RW†7BWF†÷&—¦F–öâ'—FW2vW&R&÷fVB&Vf÷&RÆVæ6ƒ²æò6W&FR&÷fÂ'F–f7Bv2&WF–æVBâ ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂWF†÷&—¦F–öâæ§6öæ²6öçG&öÂöÆVæ6‚æÖ&¶W&²6öçG&öÂöWF†÷&—¦F–öåö6öç7VÖVBæ§6öæ²5D”ôåõ$Uõ%BæÖFâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢W6Rg&W6‚6÷W&6RÖ&÷VæB6æöæ–6ÂWF†÷&—¦F–öâf÷"W†7FÇ’öæR6GW&RGFV×BæB&WfVçB&WW6R÷"&WG'’â ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVBWF†÷&—¦F–öâæB6öçG&öÂ&V6÷&G3²6÷W&6R'F–f7BF‡2&RG&6¶VBæBVæ6†ævVBg&öÒF†R&÷VæB6öÖÖ—Bâ ¢v‡’—BÖGFW'3¢—B&–æG2F†R6GW&RFòW†7B6öFRÂVçf—&öæÖVçBÂ–çWG2Â6öÖÖæG2ÂæBFW&Ö–æÂöæRÖGFV×B7FFRâ ¢&Æö6¶W"f÷"66WFæ6S¢æò £bâf–æF–ær”C¢bÓb ¢v†B–÷Rö'6W'fVC¢F†R6GW&R6VÆV7FVB7–6÷vöæ6RÂÖFRGvòF—&V7B6öææV7F–öç2ÂW†V7WFVBöæR†VÇF‚7FFVÖVçBæBFVâ÷7GW&R7FFVÖVçG2–âöæR&VBÖöæÇ’÷7GW&RG&ç67F–öâÂW†V7WFVBVÆWfVâ5Â7FFVÖVçG2F÷FÂÂÖFR¦W&ò5Âw&—FW2Â¦W&ò&WG&–W2ÂæB¦W&òÇFW&æFR×&÷f–FW"GFV×G2ÂæB&WGW&æVB56âÆÂVÆWfVâFV6—6—fR&VF–6FW2æBÆÂV–v‡B–æFWVæFVçB×fÆ–FF–öâ&VF–6FW2&RG'VRâ ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öæ²&W7VÇE÷7VÖÖ'’æ§6öæ²fÆ–FF–öå÷&V6V—Bæ§6öæ²6öÖÖæG2çG‡Fâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢&öGV6RF†RW†7BF—&V7BÖöæÇ’÷&VBÖöæÇ’÷7GW&R6¶WBVæFW"6Æ÷6VB&–Ç2Âv—F‚&WV—&VB6÷VçG2Â÷&FW&VBVW&–W2Â&öÆRfÆw2Â&VF–6FW2ÂæB–æFWVæFVçBfÆ–FF–öââ ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVC²6¶WB'—FW2ÖF6‚÷2Wf–FVæ6Râ ¢v‡’—BÖGFW'3¢F†—2—2F†R66WFæ6RÖ7&—F–6Â&ööböbF†RÆ—fRF—&V7BFF&6R÷7GW&Râ ¢&Æö6¶W"f÷"66WFæ6S¢æò £râf–æF–ær”C¢bÓr ¢v†B–÷Rö'6W'fVC¢F†R6¶WB6öçF–ç2W†7FÇ’FVâ&WV—&VBf–ÆW2âW†—Eö6öFRçG‡F—2ÇW2Äc²7FF÷WBæÆöv—2õ35ô4EU$Uõ56ÇW2Äc²7FFW'"æÆöv—2V×G“²æòf–ÇW&R6¶WBW†—7G3²6æöæ–6Â¥4ôâÂ6¶WB6†V6·7V×2Â&öÆRÖWf–FVæ6R6†V6·7V×2ÂæBFW&Ö–æÂ6öçG&öÂ†6†W2ÆÂfÆ–FFRâF—&V7B6V7&WB66âf÷VæBæò&WF–æVBE4â7&VFVçF–Ç2Â77v÷&G2Â&—fFR¶W—2ÂVç&VF7FVBDD$4UõU$ÆÂ5"Â÷"åTÂ'—FW2â ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ6ö×ÆWFR'VæFÆS²÷2Ó2ö6†V6·7V×2ç6†#Sf²&öÆR×&÷f—6–öæ–ærö6†V6·7V×2ç6†#Sf²6öçG&öÂòæ6GW&Ræ6öÖÖ—GFVF²6öçG&öÂöWF†÷&—¦F–öåö6öç7VÖVBæ§6öæâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢&öGV6R6ö×ÆWFRÂFWFW&Ö–æ—7F–2Â6V7&WBÖg&VRCÔC‚Wf–FVæ6RæB6VÂF†R7V66W726¶WBv—F†÷WB&WG'’÷"×WFF–öââ ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVC²ÆÂGvVçG’×Gvò&WF–æVBWf–FVæ6Rf–ÆW2&RG&6¶VBæB'—FRÖ–FVçF–6ÂFòF†R&Wf–WvVB'VæFÆRâ ¢v‡’—BÖGFW'3¢—BW7F&Æ—6†W26¶WB6ö×ÆWFVæW72Â–çFVw&—G’Â6öæf–FVçF–Æ—G’÷7GW&RÂæBG'W7Gv÷'F†–æW72â ¢&Æö6¶W"f÷"66WFæ6S¢æò £‚âf–æF–ær”C¢bÓ‚ ¢v†B–÷Rö'6W'fVC¢f–æÂ6ÆVçW&÷fW2†FUö÷35÷&VFW&†2Æöv–âF—6&ÆVBæB—G277v÷&B6ÆV&VBÂ†FU÷&VFW&&VÖ–ç2äôÄôt”æÂæBÖVÖ&W'6†——2&WF–æVBâF†R&V6÷&BÇ6ò&W÷'G26öææV7F–öâÖf÷&Ò&V6÷fW'’Â6ö×ÆWFVB&öÆÆ&6²&Vf÷&RWF†÷&—¦F–öâÂW6Röb&—7F–æRW‡FW&æÂ6†V6¶÷WBÂæBâFÖ–æ—7G&F—fR6ÆVçW6öææV7F–öâgFW"&–Çv’Då2f–ÇW&RâF†÷6R&V6÷fW'’FWF–Ç2&Ræ'&F—fRÖöæÇ“²F†R&WV—&VBf–æÂ&öÆR7FFRæB7V66W76gVÂ6GW&R&RF—&V7FÇ’&÷fVââ ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æróBÖÆöv–âÖF—6&ÆVBçG‡F²2×&VFW"×fW&–f–6F–öâçG‡F²5D”ôåõ$Uõ%BæÖF²÷2Ó2÷fÆ–FF–öå÷&V6V—Bæ§6öæâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢F—6&ÆRF†RF6²Æöv–âæB6ÆV"—G277v÷&Böâ7V66W72÷"f–ÇW&S²&W6W'fRWf–FVæ6RöbF†Rf–æÂ&÷VæFVB÷7GW&RæB7F÷öâç’VçfW&–f–VB6ÆVçW7FFRâ ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVB6ÆVçWWf–FVæ6Râ ¢v‡’—BÖGFW'3¢F†RFV×÷&'’&–æ6—Â6ææ÷B7W'&VçFÇ’WF†VçF–6FRÂv†–ÆRF†R&WW6&ÆR6&–Æ—G’&öÆR&VÖ–ç2æöâÖÆöv–ââ ¢&Æö6¶W"f÷"66WFæ6S¢æò £’âf–æF–ær”C¢bÓ’ ¢v†B–÷Rö'6W'fVC¢&WòG&6·2'—FRÖ–FVçF–6Â6÷–W2öbF†RFVâ6¶WB&–Ö&–W2æBGvVÇfR7W÷'F–ær&V6÷&G2âF†RF—&V7B×6VÆV7F–öâ&–Ö'’ÂWFFW"&–æF–æw2Â‡VÖâWf–FVæ6R–æFW‚&÷w2ÂÖ6†–æRÖ—'&÷"&÷w2ÂæBFVâ6–&Æ–ærF‚&öög2&Ræ÷B&W6VçBâ ¢Wf–FVæ6Rö–çFW#¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö²VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&Bö²FööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç–²Fö72öWf–FVæ6Rô”äDU‚æ§6öæ²'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆ²W†7B×F‚æB&÷VæFVB×6V&6‚&ööb&÷fRâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢&W6W'fRF†RW†7Bõ26¶WBf÷"ÆFW"FÖ—76–öã²"Óe"Ô"÷vç2F†RW†7BÖ6÷’FÖ—76–öâÂF—&V7B×6VÆV7F–öâ&–Ö'’ÂWFFW"&–æF–æw2Â–æFW‚ôÖ—'&÷"6öçfW&vVæ6RÂF‚&öög2Â7W÷'B7&÷77vÆ²ÂæBf–æÂ–çFVw&FVBfÆ–FF–öââ ¢&WV—&VÖVçB6÷fW&vS¢f÷VæBf÷"õ2Ó2&W6W'fF–öã²æ÷B–WBGVRv—F†–âõ2Ó2f÷""Óe"Ô"FÖ—76–öââ ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB6¶WBG&6¶–æræB'—FR–FVçF—G“²&WòÖæ÷BÖf÷VæBF÷vç7G&VÒ&–æF–ær7FFRâ ¢v‡’—BÖGFW'3¢õ2Ó2—2÷W&F–öæÆÇ’66WF&ÆRÂv†–ÆRf–æÂv÷fW&æVBFÖ—76–öâæB&VÆV6R×6æ—G’6Æ–×2&VÖ–âVæf–Æ&ÆRVçF–Â"Óe"Ô"6ö×ÆWFW2—G26W&FR66÷Râ ¢&Æö6¶W"f÷"66WFæ6S¢æò £âf–æF–ær”C¢bÓ ¢v†B–÷Rö'6W'fVC¢÷2Wf–FVæ6RW‡Æ–6—FÇ’F—66Æ–×2c’Ö÷fVÖVçBÂ52ÂFWÆ÷–ÖVçBÂÖ–w&F–öâÂ66WFæ6R×Fö¶Vâ6F—6f7F–öâÂW–26ö×ÆWF–öâÂæB6Æ÷6V÷WBâF†RWf–FVæ6R7W÷'G2Æ—fRFV6†æ–6Â÷7GW&Rf÷"„DRÕ4Uã6Â„DRÔD•5CãFÂæB„DRÔD•5Cã–v—F†÷WB6ö×ÆWF–ærç’&÷râ ¢Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ÷2Ó2öæöæ6Æ–×2æ§6öæ²&öÆRWf–FVæ6S²F%÷÷7GW&U÷7VÖÖ'’æ§6öæ²&÷fVBÆâÂc’æBF÷vç7G&VÒ÷væW'6†—Ö–ærâ ¢W‡V7FVB&WV—&VÖVçBg&öÒ&÷fVBÆã¢¶VWõ2Wf–FVæ6R6W&FRg&öÒÂ66WFæ6RÂc’Ö–çFVææ6RÂf–æÂ–çFVw&F–öâÂæB6Æ÷6V÷WC²&÷WFRÆFW"7W÷'BF‡&÷Vv‚"Óe"Ô"æB‡VÖâc’Ö–çFVææ6Râ ¢&WV—&VÖVçB6÷fW&vS¢f÷VæB ¢&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæöæ6Æ–×2æB6¶WC²f–æÂFÖ—76–öâ7W&f6W2&VÖ–â–æ6ö×ÆWFR2&V6÷&FVB–âbÓ’â ¢v‡’—BÖGFW'3¢—B&WfVçG2â66WFVB÷W&F–öæÂ6GW&Rg&öÒ&V–ær÷fW'7FFVB2â66WFVB&VÆV6R÷"6ö×ÆWFVBW–2â ¢&Æö6¶W"f÷"66WFæ6S¢æò ¢b7W÷'BÂöæÇ’–b&VÆ–VBöã¢c’ã2(	B6æöâ„DR'V–ÆB6†V6¶Æ—7B6W&F–öâÂ*u7V'F6²„DRÕ4Uã3²c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâÂ*u7V'F6²„DRÔD•5CãBæB*u7V'F6²„DRÔD•5Cã’â ¢6æöâ&ööbW†6W'BÂöæÇ’–bb7W÷'B—2W6VC¢c’ã27FFW2Â(	Ä¶VWD"w&çG2æBDDÂ'F–f7G27W'&VçBæB6öç6—7FVçBv—F‚ÆV7N(	&—f–ÆVvR÷7GW&Rf÷"W'6—7FVæ6RöbV&Æ–2–ÆöG2î(	Òc’ãb&V6÷&G2„DRÔD•5CãF2'F–ÆæB„DRÔD•5Cã–2'F–Æà ¤Wf–FVæ6R&–çB…52$ôôc²&WV—&VB ¢2222¢¤’&WV—&VBFVÆ—fW&&ÆW26F—6f–VB¢  ¤FVÆ—fW&&ÆRæÖS¢C(	B&–Çv’F&vWB7FGW0 ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&–Çv’×7FGW2çG‡F  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¥&WòWf–FVæ6Rö–çFW"Â–b&Wò×&W6–FVçC¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æró×&–Çv’×7FGW2çG‡F  ¤¶W’&ööbf7G3¢&ö¦V7B×ÆRÖ–ÆÇVÖ–æF–öæ²Vçf—&öæÖVçB&öGV7F–öæ²÷7Fw&U5Â6W'f–6RöæÆ–æS²æò7&VFVçF–ÂfÇVR&WF–æVBà ¤FVÆ—fW&&ÆRæÖS¢C"(	B&öÆRæBö&¦V7B&VfÆ–v‡@ ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡F  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¥&WòWf–FVæ6Rö–çFW"Â–b&Wò×&W6–FVçC¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡F  ¤¶W’&ööbf7G3¢FÖ–æ—7G&F—fR–FVçF—G’÷7Fw&W6²&WV—&VB66†VÖ2æBö&¦V7G2&W6VçC²&÷VæFVBT$Ä”2×w&—FRf–æF–æw2V×G“²†FUö÷væW&æB†FU÷'vö'6W'fVC²†FU÷&VFW&æB†FUö÷35÷&VFW&'6VçBà ¤FVÆ—fW&&ÆRæÖS¢C2(	BF&vWB×&öÆR&÷f—6–öæ–ær&W7VÇ@ ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró"×&öÆR×&÷f—6–öæ–ærçG‡F  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¥&WòWf–FVæ6Rö–çFW"Â–b&Wò×&W6–FVçC¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æró"×&öÆR×&÷f—6–öæ–ærçG‡F  ¤¶W’&ööbf7G3¢7V66W76gVÂ÷7Fw&U5Â6öÖÖæB7FGW6W3²&WV—&VB&öÆRGG&–'WFW3²6öææV7F–öâÆ–Ö—B&²7F—fRÖVÖ&W'6†—²æò77v÷&BÂE4âÂ÷"†÷7BfÇVR&WF–æVBà ¤FVÆ—fW&&ÆRæÖS¢CB(	BFVF–6FVB&VFW"fW&–f–6F–öà ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró2×&VFW"×fW&–f–6F–öâçG‡F  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¥&WòWf–FVæ6Rö–çFW"Â–b&Wò×&W6–FVçC¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æró2×&VFW"×fW&–f–6F–öâçG‡F  ¤¶W’&ööbf7G3¢VffV7F—fR&öÆR†FUö÷35÷&VFW&²&VBÖöæÇ’G&ç67F–öã²6V&6‚F‚†FRÂV&Æ–6²ÆÂ6WfVâÆV7B×&—f–ÆVvRfÆw2fÇ6S²ÆÂf÷W"ÖWFFF×f—6–&–Æ—G’6†V6·2G'VS²$ôÄÄ$4¶à ¤FVÆ—fW&&ÆRæÖS¢CR(	B6æöæ–6Â6÷W&6RÖ&÷VæBWF†÷&—¦F–öà ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂWF†÷&—¦F–öâæ§6öæ  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¥&WòWf–FVæ6Rö–çFW"Â–b&Wò×&W6–FVçC¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&BöWF†÷&—¦F–öâæ§6öæ  ¤¶W’&ööbf7G3¢'Vâ”B÷32×&öÆVf—‚ÖfFC6#s“#s#CSc–v3#Fcƒ6²6÷W&6R6öÖÖ—BC6FCf#“sSCC&Cv“3#–66ffc–ccCƒ6–CFfVS&²GvòÖ†÷W"UD2v–æF÷s²4„Ó#Sb“6&6–Cƒ“#cV“#sf#CscfFS33&&F3–S&6FCS–cs6fFf6ƒVV²W†7B6÷W&6RÂ6öÖÖæG2ÂF&vWBÂ&–Ç2Â&÷7FW"Â6÷VçG2ÂæBöæRÖGFV×B&–æF–æw2à ¤FVÆ—fW&&ÆRæÖS¢Cb(	BFVâÖf–ÆRF—&V7B÷7GW&R6¶W@ ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ÷2Ó2ö  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBÂG&6¶VBÂæB'—FRÖ–FVçF–6Âà ¥&WòWf–FVæ6Rö–çFW"Â–b&Wò×&W6–FVçC¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö  ¤¶W’&ööbf7G3¢W†7BFVâÖf–ÆR–çfVçF÷'“²56²W†—B6öFR²W†7B7FF÷WB6VçF–æVÃ²V×G’7FFW'#²ÆÂFV6—6—fRæB–æFWVæFVçB×fÆ–FF–öâ&VF–6FW2G'VS²¦W&òw&—FW2Â&WG&–W2ÂæBÇFW&æFR×&÷f–FW"GFV×G3²6öÖÖ—GFVB6VÆVB6öçG&öÂ7FFRà ¤FVÆ—fW&&ÆRæÖS¢Cr(	BF—6&ÆVBÖÆöv–âf–æÂ7FFP ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æróBÖÆöv–âÖF—6&ÆVBçG‡F  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¥&WòWf–FVæ6Rö–çFW"Â–b&Wò×&W6–FVçC¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–æróBÖÆöv–âÖF—6&ÆVBçG‡F  ¤¶W’&ööbf7G3¢†FUö÷35÷&VFW&Æöv–âF—6&ÆVC²77v÷&B6ÆV&VC²†FU÷&VFW&&VÖ–ç2äôÄôt”æ²ÖVÖ&W'6†—&WF–æVBà ¤FVÆ—fW&&ÆRæÖS¢C‚(	B&öÆRÖWf–FVæ6R6†V6·7VÒÆVFvW  ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–ærö6†V6·7V×2ç6†#Sf  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¥&WòWf–FVæ6Rö–çFW"Â–b&Wò×&W6–FVçC¢&WòÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&B÷&öÆR×&÷f—6–öæ–ærö6†V6·7V×2ç6†#Sf  ¤¶W’&ööbf7G3¢44”’×6÷'FVB4„Ó#Sb&÷w2f÷"CÂC"ÂC2ÂCBÂæBCs²WfW'’&÷rfÆ–FFW3²ÆVFvW"4„Ó#Sb““ƒ–FF&Cf6VCc“3v3“F3S†C63FSCV#sFV3c–&Cs–VFC#c–scf33fF²æò6V7&WB&WF–æVBà ¢2222¢¤"’6öÖÖæG2æB7F–öç2Wf–FVæ6R¢  ¤7F–öã¢6öæf—&ÒF†RWF†÷&—¦VB&–Çv’&ö¦V7BÂVçf—&öæÖVçBÂæB÷7Fw&U5Â6W'f–6Rà ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&–Çv’×7FGW2çG‡F  ¥7V66W726–væÃ¢&ö¦V7B×ÆRÖ–ÆÇVÖ–æF–öæÂVçf—&öæÖVçB&öGV7F–öæÂæB÷7Fw&U5Â6W'f–6RöæÆ–æRà ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçB÷WGWC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¤7F–öã¢–ç7V7BÆ—fRFÖ–æ—7G&F—fR–FVçF—G’Â66†VÖ2Â&WV—&VBö&¦V7G2ÂT$Ä”2&—f–ÆVvR÷7GW&RÂæB&öÆR&÷7FW"à ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡F  ¥7V66W726–væÃ¢&WV—&VBF&vWBæBö&¦V7G2&W6VçC²&÷VæFVBT$Ä”2f–æF–æw2V×G“²ÆVv7’&öÆW2ö'6W'fVC²F6²×7V6–f–2&öÆW2'6VçBà ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçB÷WGWC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¤7F–öã¢&÷f—6–öâF†R6&–Æ—G’æBF6²ÖÆöv–â&öÆW2æBW7F&Æ—6‚ÖVÖ&W'6†—à ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró"×&öÆR×&÷f—6–öæ–ærçG‡F  ¥7V66W726–væÃ¢7V66W76gVÂ6öÖÖæB7FGW6W2ÂW‡V7FVBF&vWB×&öÆRGG&–'WFW2ÂæB7F—fRÖVÖ&W'6†—à ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçB÷WGWC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¤7F–öã¢6öææV7B2F†RF6²&–æ6—ÂæBFW7BF†RÖW&vVBÆV7B×&—f–ÆVvR&VF–6FR–ç6–FR&VBÖöæÇ’G&ç67F–öâà ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró2×&VFW"×fW&–f–6F–öâçG‡F  ¥7V66W726–væÃ¢W†7B&öÆRæB6V&6‚Fƒ²&VBÖöæÇ’G'VS²6WfVâ&ö†–&—FVBfÆw2fÇ6S²&WV—&VBÖWFFFf—6–&ÆS²$ôÄÄ$4¶à ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçB÷WGWC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¤7F–öã¢6öç7G'V7BÂfÆ–FFRÂæB6öç7VÖRöæR6æöæ–6ÂWF†÷&—¦F–öâà ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂWF†÷&—¦F–öâæ§6öæ²6öçG&öÂöÆVæ6‚æÖ&¶W&²6öçG&öÂöWF†÷&—¦F–öåö6öç7VÖVBæ§6öæ  ¥7V66W726–væÃ¢6æöæ–6Â&÷VæBWF†÷&—¦F–öã²öæR6öç7VÖVBÆVæ6ƒ²ÆVæ6…ö6öç7VÖVC×G'VV²f–æÆ—¦VC×G'VV²6VÆVC×G'VVà ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçB÷WGWC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¤7F–öã¢W†V7WFRF†RF—&V7B÷7GW&R6GW&RæB–æFWVæFVçBfÆ–FF÷"à ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ÷2Ó2ö6öÖÖæG2çG‡FÂF%÷÷7GW&U÷7VÖÖ'’æ§6öæÂ&W7VÇE÷7VÖÖ'’æ§6öæÂfÆ–FF–öå÷&V6V—Bæ§6öæÂ7FF÷WBæÆövÂ7FFW'"æÆövÂW†—Eö6öFRçG‡F  ¥7V66W726–væÃ¢õ35ô4EU$Uõ56²W†—B6öFR²V×G’7FFW'#²6GW&R56²–æFWVæFVçBfÆ–FF–öâ56²W†7B6÷VçG3²¦W&òw&—FW2Â&WG&–W2Â÷"ÇFW&æFR×&÷f–FW"GFV×G2à ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçB÷WGWC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¤7F–öã¢F—6&ÆRF†RF6²Æöv–âÂ6ÆV"—G277v÷&BÂæBfW&–g’f–æÂ&öÆR7FFRà ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æróBÖÆöv–âÖF—6&ÆVBçG‡F  ¥7V66W726–væÃ¢F6²&öÆRäôÄôt”æ²77v÷&B6ÆV&VC²6&–Æ—G’&öÆR&VÖ–ç2äôÄôt”æ²ÖVÖ&W'6†—&WF–æVBà ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçB÷WGWC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¤7F–öã¢&öGV6RæBfW&–g’6¶WBæB&öÆRÖWf–FVæ6R6†V6·7VÒÆVFvW'2à ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ÷2Ó2ö6†V6·7V×2ç6†#Sf²&öÆR×&÷f—6–öæ–ærö6†V6·7V×2ç6†#Sf²6öçG&öÂòæ6GW&Ræ6öÖÖ—GFVF  ¥7V66W726–væÃ¢WfW'’6÷fW&VB†6‚ÖF6†W3²6¶WBÆVFvW"4„Ó#SbS#fS#VFS3ssSV#Fc#sf†C†Ccv3F&6V3c63&cs–Ff6SsƒcƒFS6&Sf&3&²&öÆRÆVFvW"4„Ó#Sb““ƒ–FF&Cf6VCc“3v3“F3S†C63FSCV#sFV3c–&Cs–VFC#c–scf33fF²FW&Ö–æÂ6öÖÖ—BÖ&¶W"ÖF6†W2à ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçB÷WGWC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¢2222¢¤2’6öæf–wW&F–öâ÷"–æg&7G'V7GW&R7FFRWf–FVæ6R¢  ¥7FFR6Æ–Ó¢WF†÷&—¦VB÷W&F–öæÂF&vW@ ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&–Çv’×7FGW2çG‡F  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVB&V6÷&C²Æ—fR6W'f–6R7FFR—2W‡FW&æÂà ¥7FFR&÷fVã¢&–Çv’&ö¦V7B×ÆRÖ–ÆÇVÖ–æF–öæÂVçf—&öæÖVçB&öGV7F–öæÂ÷7Fw&U5Â6W'f–6RöæÆ–æRà ¥7FFR6Æ–Ó¢&R×&÷f—6–öæ–ær&öÆR÷7GW&P ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡F  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVB&V6÷&C²Æ—fR&öÆR7FFR—2W‡FW&æÂà ¥7FFR&÷fVã¢†FUö÷væW&æB†FU÷'vW†—7FVB2äôÄôt”æ²†FU÷&VFW&æB†FUö÷35÷&VFW&F–Bæ÷BW†—7C²÷7Fw&W6v2F†RFÖ–æ—7G&F—fR–FVçF—G’âF†RWf–FVæ6RFöW2æ÷B&÷fR÷&–v–âÂ6ö×ÆWFRÖVÖ&W'6†—2Â6ö×ÆWFRö&¦V7Bw&çG2Â÷"FW&Ö–æÂVæ6†ævVB7FFRf÷"F†RÆVv7’&öÆW2à ¥7FFR6Æ–Ó¢fW&–f–VB6GW&R&–æ6—Â÷7GW&P ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró2×&VFW"×fW&–f–6F–öâçG‡F²÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öæ  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVB&V6÷&G2à ¥7FFR&÷fVã¢VffV7F—fR&öÆR†FUö÷35÷&VFW&²&VBÖöæÇ’G&ç67F–öã²W†7B6V&6‚Fƒ²æòF—7Æ–VBVÆWfFVBÂ66†VÖÖ7&VFRÂ÷"&VÆF–öâ×w&—FR6&–Æ—G“²&WV—&VBÖWFFFf—6–&ÆRà ¥7FFR6Æ–Ó¢F—&V7B6GW&R&–Ç0 ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ÷2Ó2öVçe÷&W6Væ6Ræ§6öæ²WF†÷&—¦F–öâæ§6öæ  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVBæB'—FRÖ–FVçF–6Âà ¥7FFR&÷fVã¢ôTåcÖFWfÂ4dUôÔôDSÓÂÄÄõuôäUEtõ$³ÓÂÄÄõuôD%õu$•DSÓÂD"×&VBWF†÷&—¦F–öâ&W6VçBÂæBÆÂF‡&VR&WF—&VB¶W—2'6VçBà ¥7FFR6Æ–Ó¢FW&Ö–æÂF6²×&öÆR÷7GW&P ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æróBÖÆöv–âÖF—6&ÆVBçG‡F  ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢&WòÖ6öæf—&ÖVB&WF–æVB&V6÷&Bà ¥7FFR&÷fVã¢†FUö÷35÷&VFW&6ææ÷BÆör–âæB†2æò77v÷&C²†FU÷&VFW&&VÖ–ç2æöâÖÆöv–â6&–Æ—G’&öÆS²ÖVÖ&W'6†—&VÖ–ç2&W6VçBà ¥7FFR6Æ–Ó¢&Wò&W6W'fF–öâæBF÷vç7G&VÒFÖ—76–öà ¤Wf–FVæ6Rö–çFW#¢&WòÂ7W'&VçB„TBæBW†7BF‡2–âF†R&WòWf–FVæ6RfÆ–FF–öâ7VÖÖ'’à ¥&WòfÆ–FF–öâ7FGW2Â–b&Wò×&W6–FVçC¢6¶WBæB7W÷'F–ær&V6÷&G2&WòÖ6öæf—&ÖVC²FÖ—76–öâ6ö×æ–öç2&WòÖæ÷BÖf÷VæBà ¥7FFR&÷fVã¢W†7B÷2Wf–FVæ6R—2G&6¶VBæBÖW&vV&ÆS²f–æÂv÷fW&æVBFÖ—76–öâÂF—&V7B×6VÆV7F–öâÂWFFW"6öçfW&vVæ6RÂ–æFW‚ôÖ—'&÷"6öçfW&vVæ6RÂæB6–&Æ–ærF‚&öög2&Ræ÷B6ö×ÆWFRà ¢2222¢¤B’c’ÆFW"ÖG&–â7W÷'B¢  ¥†6VBc’Fö7VÖVçC¢c’ã2(	B6æöâ„DR'V–ÆB6†V6¶Æ—7B6W&F–öà ¥c’F6²”C¢„DRÕ4U  ¥c’7V'F6²”BÂ–bÆ–6&ÆS¢„DRÕ4Uã6  ¤&÷fVBÆâ6Æ–Ó¢F†R&÷VæFVBF&vWB×&öÆR&÷f—6–öæ–æræBfW&–f–6F–öâ&R&VÆWfçBFòF†Rw&çG2æBÆV7B×&—f–ÆVvR÷7GW&R&÷r'WBFòæ÷B&V÷Vâ÷"6ö×ÆWFR—Bà ¥7W÷'F&ÆRÆFW"ÖG&–â7F–öã¢æò7FGW27F–öââ&W6W'fRFöæV²&V6÷&BF†RF6²×7V6–f–2&öÆR÷WF6öÖRöæÇ’–âF†RF6²×&VÆWfçBcFFVæGVÒà ¤Wf–FVæ6R&6—3¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡FF‡&÷Vv‚BÖÆöv–âÖF—6&ÆVBçG‡Fà ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçBWf–FVæ6S¢&WòÖ6öæf—&ÖVB&WF–æVB&V6÷&G2à ¤æ÷FW3¢F†R&÷r7FFW2Â(	Ä¶VWD"w&çG2æBDDÂ'F–f7G27W'&VçBæB6öç6—7FVçBv—F‚ÆV7N(	&—f–ÆVvR÷7GW&Rf÷"W'6—7FVæ6RöbV&Æ–2–ÆöG2î(	ÒF†R&÷VæFVBF6²&öÆW2Fòæ÷B&÷fR6ö×ÆWFRÆ–6F–öâÂw&—FW"Â÷væW"ÂÖ–w&F–öâÂFÖ–æ—7G&F–öâÂ&÷FF–öâÂ&V6÷fW'’Â÷"'&V²ÖvÆ72&öÆR&6†—FV7GW&Rà ¥†6VBc’Fö7VÖVçC¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öà ¥c’F6²”C¢„DRÔD•5C  ¥c’7V'F6²”BÂ–bÆ–6&ÆS¢„DRÔD•5CãF  ¤&÷fVBÆâ6Æ–Ó¢õ2Ó27WÆ–W2Æ—fR&öÆRÂ6V&6‚×F‚ÂDDÂÖ–FVçF—G’Â6öç7G&–çBÂ&÷VæF'’×f–WrÂæB'F—F–öâö'6W'fF–öç2f÷"ÆFW"7W÷'B&Wf–Wrà ¥7W÷'F&ÆRÆFW"ÖG&–â7F–öã¢gFW""Óe"Ô"6ö×ÆWFW2v÷fW&æVBWf–FVæ6RFÖ—76–öâæBf–æÂ&Wf–WrÂ‡VÖâc’Ö–çFVææ6R72Ö’WfÇVFRF†R&÷rv–ç7BÆÂ&VÖ–æ–ær&VF–6FW2âõ2Ó2ÆöæR7W÷'G2æò7FGW2Ö÷fVÖVçBà ¤Wf–FVæ6R&6—3¢÷2Wf–FVæ6RÂ÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öæÂfÆ–FF–öå÷&V6V—Bæ§6öæÂ&öÆR×&÷f—6–öæ–æró2×&VFW"×fW&–f–6F–öâçG‡Fà ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçBWf–FVæ6S¢6¶WBæB7W÷'F–ær&V6÷&G2&WòÖ6öæf—&ÖVC²"Óe"Ô"FÖ—76–öâ6ö×æ–öç2&WòÖæ÷BÖf÷VæBà ¤æ÷FW3¢c’ãb&V6÷&G2F†R&÷r2'F–Æà ¥†6VBc’Fö7VÖVçC¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öà ¥c’F6²”C¢„DRÔD•5C  ¥c’7V'F6²”BÂ–bÆ–6&ÆS¢„DRÔD•5Cã–  ¤&÷fVBÆâ6Æ–Ó¢F†R7W'&VçBW†7B×F÷–2ÖVæ–ær—2F—&V7BFF&6R6öææV7F—f—G’æB&WF—&VB×G&ç7÷'BVæf÷&6VÖVçBâõ2Ó2&÷fW2F—&V7B7–6÷v6öææV7F—f—G’Â'6VçB&WF—&VB¶W—2Â¦W&òÇFW&æFR×&÷f–FW"GFV×G2ÂæB&VBÖöæÇ’Æ—fR÷7GW&Rà ¥7W÷'F&ÆRÆFW"ÖG&–â7F–öã¢gFW""Óe"Ô"&–æG2F†R6¶WBÂF—&V7B×6VÆV7F–öâ&–Ö'’ÂWFFW"7FFRÂ–æFW‚ôÖ—'&÷"&÷w2ÂF‚&öög2ÂæBf–æÂ—VÆ–æR&W7VÇBÂ‡VÖâc’Ö–çFVææ6R72Ö’WfÇVFRF†R&÷rv–ç7BF†R6ö×ÆWFRF—&V7BÖöæÇ’&VF–6FRâõ2Ó2ÆöæR7W÷'G2æò7FGW2Ö÷fVÖVçBà ¤Wf–FVæ6R&6—3¢÷2Wf–FVæ6RÂ÷2Ó2öVçe÷&W6Væ6Ræ§6öæÂF%÷÷7GW&U÷7VÖÖ'’æ§6öæÂfÆ–FF–öå÷&V6V—Bæ§6öæÂæöæ6Æ–×2æ§6öæà ¥&WòfÆ–FF–öâ7FGW2f÷"&Wò×&W6–FVçBWf–FVæ6S¢6¶WB&WòÖ6öæf—&ÖVC²F÷vç7G&VÒ&–æF–ær7FFR&WòÖæ÷BÖf÷VæBà ¤æ÷FW3¢c’ãb&V6÷&G2F†R&÷r2'F–ÆâF†R6¶WBFöW2æ÷B'’—G6VÆb&÷fRWfW'’6÷W&6RÖÆWfVÂ&WF—&VBÖ¶W’&VgW6Â66R÷"6ö×ÆWFRf–æÂ–çFVw&F–öâà ¤Fö2FVÇF2…bÔ6æöâöæÇ“²$UT•$TB–âõ244UD$ÄR'&æ6‚ ¤Fö2FVÇFFWFV7F–öâv÷&¶fÆ÷p ¤4„r”C¢4„rÓ ¤6†ævR6Æ–Ó¢òÖWF†÷&—¦VB×WF&ÆR&V7W'6÷"Ö’&÷f—6–öâæBfW&–g’FVF–6FVBÆV7B×&—f–ÆVvRFF&6R&–æ6—Â&Vf÷&RâWF†÷&—¦F–öâÖ&÷VæBF—&V7B&VBÖöæÇ’6GW&RÂ&÷f–FVBF†R†6W2&VÖ–â6W&FRæBF†R6GW&R6öçG&7B—2Væ6†ævVBà ¥G—S¢v÷&¶fÆ÷r7FW3²&–Ç2÷"Wf–FVæ6R÷7GW&P ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–ærWf–FVæ6RÂWF†÷&—¦F–öâÂ6GW&R6¶WBÂ6ÆVçWWf–FVæ6S²&÷fVBÆâÂGvò×†6R÷W&F–ær&÷VæF'’à ¤6æöâ&6—3¢4äôâ4”ÄTä4P ¤4„r”C¢4„rÓ  ¤6†ævR6Æ–Ó¢Æ—fR&VfÆ–v‡Bö'6W'fVB†FUö÷væW&æB†FU÷'vÂv†–ÆRF†RF6²×7V6–f–2†FU÷&VFW&æB†FUö÷35÷&VFW&&öÆW2vW&R'6VçBæBvW&RF†Vâ&÷f—6–öæVB–çFòF†R&÷VæFVBFW&Ö–æÂ÷7GW&Rà ¥G—S¢6öæf–wW&F–öâ÷"Vçf—&öæÖVç@ ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡FF‡&÷Vv‚BÖÆöv–âÖF—6&ÆVBçG‡Fà ¤6æöâ&6—3¢4äôâ4”ÄTä4P ¤4„r”C¢4„rÓ0 ¤6†ævR6Æ–Ó¢õ2Ó26ö×ÆWFVB7V66W76gVÆÇ’æB—2÷W&F–öæÆÇ’66WF&ÆRÂv†–ÆRf–æÂv÷fW&æVBWf–FVæ6RFÖ—76–öâ&VÖ–ç276–væVBFò"Óe"Ô"à ¥G—S¢v÷fW&æVBF‡2÷"'F–f7BfÖ–Æ–W3²&–Ç2÷"Wf–FVæ6R÷7GW&P ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂW†7B6¶WBæB÷W&F÷"&V6÷&G3²&WòÂG&6¶VB'—FRÖ–FVçF–6Â6¶WBæB'6VçBF÷vç7G&VÒ&–æF–æw2à ¤6æöâ&6—3¢4äôâÄ”täT@ ¤4„s¢4„rÓ ¤Fö3¢c(	B„DR'V–ÆBæ÷FW0 ¥6V7F–öã¢*s"ãB(	Ä„DRÔU”33‚÷7BÕ#3S’&VÖVF–F–öâ(	BE"Ô4äôâÓrWF†÷&—¦F–öâÔ&÷VæBõ2Ó2F—&V7B&VBÔöæÇ’÷7GW&R6¶WN(	Ð ¤6æöâ&6—3¢4äôâ4”ÄTä4P ¤FVÇF¢äUr4äôâ$õõ4Â(	BFBF6²×7V6–f–2*s"ã‚F†BFVf–æW2F†R×WF&ÆR&VFW"×&öÆR&V7W'6÷"26W&FRg&öÒF†RVæ6†ævVBF—&V7B÷&VBÖöæÇ’6GW&RÂ&V6÷&G2F†RWf–FVæ6RÖ&÷VæFVB&öÆR÷7GW&RÂæB&W6W'fW2F†RW†—7F–ærWF†÷&—¦F–öâÂöæRÖGFV×BÂ6V7&WB×6fWG’ÂæB¦W&ò×w&—FR6GW&R'VÆW2à ¥v‡“¢F†RW†—7F–ærF—&V7BÖ6GW&RVæ—BFVf–æW2F†R6GW&R6öçG&7B'WBFöW2æ÷BFVf–æR&÷VæFVB&öÆR×&÷f—6–öæ–ær&V7W'6÷"âF†RæWrVæ—B—2&WV—&VBFòÖ¶RF†RWF†÷&—¦VB†6R&÷VæF'’æB66WFVB÷W&F–öæÂ&W7VÇBW‡Æ–6—Bv—F†÷WB–×Ç––ærF†B&÷f—6–öæ–ær5Â'F–6—FVB–âF†R6GW&Rà ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&–Çv’×7FGW2çG‡FF‡&÷Vv‚BÖÆöv–âÖF—6&ÆVBçG‡F²WF†÷&—¦F–öâæ§6öæ²÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öæ²÷2Ó2÷fÆ–FF–öå÷&V6V—Bæ§6öæà ¤4„s¢4„rÓ  ¤Fö3¢c(	B„DR'V–ÆBæ÷FW0 ¥6V7F–öã¢*s"ã‚(	Ä„DRÔU”33‚õ2Ó2(	BWF†÷&—¦VB&VFW"Õ&öÆR&÷f—6–öæ–ærÂF—&V7B&VBÔöæÇ’6GW&RÂæBWf–FVæ6RÔFÖ—76–öâ&÷VæF'ž(	Ð ¤6æöâ&6—3¢4äôâ4”ÄTä4P ¤FVÇF¢äUr4äôâ$õõ4Â(	B&V6÷&BöæÇ’F†RF—&V7FÇ’ö'6W'fVB&öÆR&÷7FW"æB&÷VæFVBF&vWB×&öÆR÷WF6öÖS¢ÆVv7’†FUö÷væW&æB†FU÷'vW†—7FVC²F6²×7V6–f–2†FU÷&VFW&æB†FUö÷35÷&VFW&vW&R'6VçB&Vf÷&R&÷f—6–öæ–æs²F†RF6²&–æ6—Â6F—6f–VBF†R6WfVâÖfÆr&VFW"&VF–6FS²f–æÂÆöv–âv2F—6&ÆVBæB—G277v÷&B6ÆV&VBâ–æ6ÇVFRF†RWf–FVæ6RVÆ–f–6F–öç2æBW‡Æ–6—Bæöæ6Æ–×2à ¥v‡“¢&W÷6—F÷'’æÖW2Âf—‡GW&W2Â&VF–6FW2ÂæBFW6—&VB&6†—FV7GW&RFòæ÷B&÷fRÆ—fRFF&6R&öÆW2âF†RÆ—fR&VfÆ–v‡BæBFW&Ö–æÂWf–FVæ6RW7F&Æ—6‚&V6—6RF6²×66÷VB÷7GW&RF†B6†÷VÆBv÷fW&âgWGW&RÆææ–ærà ¤Wf–FVæ6Rö–çFW#¢÷2Wf–FVæ6RÂ&öÆR×&÷f—6–öæ–æró×&öÆR×&VfÆ–v‡BçG‡FÂ"×&öÆR×&÷f—6–öæ–ærçG‡FÂ2×&VFW"×fW&–f–6F–öâçG‡FÂBÖÆöv–âÖF—6&ÆVBçG‡FÂ&öÆR×&÷f—6–öæ–ærö6†V6·7V×2ç6†#Sfà ¤DT4•4”ôã¢õ244UD$ÄP ¢22¢£"ã’’"Ób&VÖVF–F–öâÂÒ„DRÔU”33‚õ2Ó2(	BWF†÷&—¦VB&VFW"Õ&öÆR&÷f—6–öæ–ærÂF—&V7B&VBÔöæÇ’6GW&RÂæBWf–FVæ6RÔFÖ—76–öâ&÷VæF'’¢  ¥F–ÖW7F×¢s#C#b3£2 ¤FWF–Ç3¢öâ##bÓrÓ#2UD2ÂF†R&öGV7B÷væW"ÖWF†÷&—¦VBõ2Ó2F6²6ö×ÆWFVB&÷VæFVBFF&6R×&öÆR&÷f—6–öæ–ær†6RföÆÆ÷vVB'’âWF†÷&—¦F–öâÖ&÷VæBF—&V7B÷7Fw&U5Â&VBÖöæÇ’6GW&RâÆ—fR&VfÆ–v‡Bö'6W'fVBF†RW†—7F–ær„DRÖæÖVB&öÆW2†FUö÷væW&æB†FU÷'vÂW7F&Æ—6†VBF†BF†RFVF–6FVBF&vWB&öÆW2†FU÷&VFW&æB†FUö÷35÷&VFW&vW&R'6VçBÂæB6öæf—&ÖVBF†BF†RFÖ–æ—7G&F—fR6öææV7F–öâW6VBF†RVÆWfFVB÷7Fw&W6–FVçF—G’âF†RF6²&÷f—6–öæVBæBfW&–f–VBF†RGvòF&vWB&öÆW2ÂW†V7WFVBöæR7V66W76gVÂF—&V7B6GW&RÂæBF—6&ÆVBF†RF6²×7V6–f–2Æöv–âæB6ÆV&VB—G277v÷&BâF†—2FFVæGVÒ&V6÷&G2F†RFF&6R×&öÆR÷7GW&RÂ÷W&F–öæÂ&W7VÇBÂWf–FVæ6RÆ–Ö—G2Âc’VffV7BÂæB"Óe"Ô"&÷VæF'’à ¢222¢¤FV6—6–öâ¢  ¢¢¤õ2Ó2õU$D”ôäÂU„T5UD”ôã¢44UD$ÄRt•D‚äôâÔ$Äô4´”äräõDU2â¢  ¤&–æ'’F—7÷6—F–öã  ¢¢¤õ244UD$ÄR¢  ¥F†R&öÆRWf–FVæ6RæBF—&V7BÖ6GW&R6¶WBW7F&Æ—6‚F†R&WV—&VB÷W&F–öæÂ÷WF6öÖRâæògW'F†W"õ2Ó2GFV×BÂFF&6R×&öÆR&öÆÆ&6²ÂFÖ–æ—7G&F—fR×&öÆR6GW&RW†6WF–öâÂ÷"6†ævRFòF†R'VææW"ÂfÆ–FF÷"Â66†VÖ2ÂFW7G2Â÷"FVâ6GW&VB&–Ö&–W2—2&WV—&VBà ¥F†—2FV6—6–öâ—2Æ–Ö—FVBFòF†R&÷VæFVB&öÆRv÷&²Â6ÆVçWÂæBF—&V7B6GW&Râ—BFöW2æ÷BW7F&Æ—6‚f–æÂv÷fW&æVBWf–FVæ6RFÖ—76–öâÂf–æÂ&VÆV6R–çFVw&F–öâÂ52Âc’7FGW2Ö÷fVÖVçBÂ66WFæ6R×Fö¶Vâ6F—6f7F–öâÂFWÆ÷–ÖVçBÂÖ–w&F–öâÂW–26ö×ÆWF–öâÂ÷"6Æ÷6V÷WBà ¢222¢¤ö'6W'fVB&RÕ&÷f—6–öæ–ær&öÆR÷7GW&R¢  ¥F†R&WF–æVB&VfÆ–v‡BWf–FVæ6RF—&V7FÇ’W7F&Æ—6†W3  ¢¢FF&6R–FVçF—G’&–Çv–² ¢¢FÖ–æ—7G&F—fR6öææV7F–öâ–FVçF—G’÷7Fw&W6² ¢¢÷7Fw&U5ÂfW'6–öârãf² ¢¢66†VÖ2†FVæBV&Æ–6&W6VçC² ¢¢†FRæ&öG•öw&‡6Â†FRæ&öG•öw&‡5ö7W'&VçFÂV&Æ–2æ†FUö&öG•öw&‡5ö7W'&VçFÂ†FRç—%öWfÇVF–öæÂæB†FRçV&Æ–5÷&W7VÇG6&W6VçC² ¢¢æò&W7VÇBg&öÒF†R&÷VæFVBVW'’f÷"æöâÖU4tV66†VÖ&—f–ÆVvW2w&çFVBFòT$Ä”6² ¢¢æò&W7VÇBg&öÒF†R&÷VæFVBVW'’f÷"æöâÖ4TÄT5FF&ÆR&—f–ÆVvW2w&çFVBFòT$Ä”6² ¢¢†FUö÷væW&&W6VçB2äôÄôt”æ² ¢¢†FU÷'v&W6VçB2äôÄôt”æ² ¢¢F†RF—7Æ–VB7WW'W6W"Â7&VFRÖFF&6RÂ7&VFR×&öÆRÂ&WÆ–6F–öâÂæB'—72Õ$Å2fÆw2fÇ6Rf÷"&÷F‚„DRÖæÖVB&öÆW3² ¢¢÷7Fw&W6&W6VçB2âVÆWfFVBÆöv–â–FVçF—G“²æB ¢¢æò&÷rf÷"†FU÷&VFW&÷"†FUö÷35÷&VFW&à ¥F†RÆ—fR&VfÆ–v‡BF†W&Vf÷&RW7F&Æ—6†W2F†B„DRÖæÖVBFF&6R&öÆW2W†—7FVB&Vf÷&Rõ2Ó2Âv†–ÆRF†RGvòFVF–6FVBõ2Ó2F&vWB&öÆW2F–Bæ÷Bà ¥F†R&WF–æVB&VfÆ–v‡BFöW2æ÷BW7F&Æ—6ƒ  ¢¢v†VâÂ†÷rÂ÷"'’v†öÒ†FUö÷væW&æB†FU÷'vvW&R7&VFVC² ¢¢F†R6ö×ÆWFRÖVÖ&W'6†—w&‚f÷"V—F†W"ÆVv7’&öÆS² ¢¢F†R6ö×ÆWFRö&¦V7BÖÆWfVÂ&—f–ÆVvRw&‚f÷"V—F†W"ÆVv7’&öÆS² ¢¢F†RFWF–ÆVB÷W&F–öæÂ7V—F&–Æ—G’öbV—F†W"ÆVv7’&öÆS²÷" ¢¢6VÆVB÷7B×'VâVæ6†ævVB×7FFR&ööbf÷"V—F†W"ÆVv7’&öÆRà ¥F†÷6RVç&÷fVâ&÷W'F–W2×W7Bæ÷B&R–æfW'&VBg&öÒ&öÆRæÖW2Âf—‡GW&W2Â66†VÖf–VÆG2Â66WFæ6R&VF–6FW2ÂÆææ–ærÆæwVvRÂ÷"&W÷6—F÷'’6öçFVçBà ¢222¢¤WF†÷&—¦VB÷W&F–öæÂ&÷VæF'’¢  ¤õ2Ó2W6VBGvò6W&FR÷W&F–öæÂ†6W2à ¢2222¢¤&÷VæFVB×WF&ÆR&öÆR†6R¢  ¥&–Çv’æBFÖ–æ—7G&F—fR÷7Fw&U5Â66W72vW&RWF†÷&—¦VBFó  ¢¢–FVçF–g’F†RÆ—fRF&vWBæBFÖ–æ—7G&F—fR–FVçF—G“² ¢¢–ç7V7BF†R&÷VæFVB&öÆRÂ66†VÖÂö&¦V7BÂæBT$Ä”2&—f–ÆVvR÷7GW&S² ¢¢7&VFRæB6öæf–wW&R†FU÷&VFW&æB†FUö÷35÷&VFW&² ¢¢w&çBF†RF6²&–æ6—ÂÖVÖ&W'6†—–âF†R&VFW"6&–Æ—G’&öÆS² ¢¢fW&–g’F†RW†7BÆV7B×&—f–ÆVvR&VFW"&VF–6FS² ¢¢Ö¶RF†RF6²Æöv–âf–Æ&ÆRöæÇ’f÷"F†RWF†÷&—¦VB6GW&Rv–æF÷s²æB ¢¢F—6&ÆRF†RF6²Æöv–âæB6ÆV"—G277v÷&BgFW"6GW&Rà ¤FF&6R×WFF–öç2vW&R6öæf–æVBFòF†—2†6RæBFòF†R&WV—&VBFW&Ö–æÂ6ÆVçWà ¢2222¢¤F—&V7B&VBÖöæÇ’6GW&R†6R¢  ¥F†RWF†÷&—¦F–öâÖ&÷VæB6GW&S  ¢¢W6VBF—&V7B÷7Fw&U5ÂF‡&÷Vv‚7–6÷v² ¢¢ÖFRæò&–Çv’4Ä’6ÆÃ² ¢¢W†V7WFVBæò5Âw&—FS² ¢¢6VÆV7FVBöæR&÷f–FW#² ¢¢W6VBöæRWF†÷&—¦F–öâf÷"öæRÆVæ6ƒ² ¢¢ÖFRæò&WG'“² ¢¢ÖFRæòÇFW&æFR×&÷f–FW"GFV×C² ¢¢W6VBöæR&VBÖöæÇ’÷7GW&RG&ç67F–öã² ¢¢&WF–æVBæòFF&6R7&VFVçF–ÂfÇVS²æB ¢¢w&÷FRæ÷F†–ærFòF†RW†V7WF–öâ6÷W&6R6†V6¶÷WBà ¥&÷f—6–öæ–ær5ÂF–Bæ÷B'F–6—FR–âF†RF—&V7B6GW&RæBFöW2æ÷BÇFW"F†R6GW&R&W7VÇB7Å÷w&—FW3Óà ¥F†R×WF&ÆR&V7W'6÷"ÖFRF†RW†—7F–ærÆV7E÷&—f–ÆVvU÷&öÆS×G'VV&VF–6FRW†V7WF&ÆRv—F†÷WBW6–ærF†RVÆWfFVB÷7Fw&W6–FVçF—G’f÷"6GW&RæBv—F†÷WB6†æv–ærF†R6÷W&6RÖ&÷VæB'VææW"ÂfÆ–FF÷"Â66†VÖ2ÂFW7G2Â÷"Wf–FVæ6R6öçG&7Bà ¢222¢¥&÷f—6–öæVBF&vWBÕ&öÆR÷7GW&R¢  ¥F†RWF†÷&—¦VB&öÆR&ö6VGW&RW7F&Æ—6†VC  ¢¢†FU÷&VFW&2&WW6&ÆRäôÄôt”æ6&–Æ—G’&öÆS² ¢¢†FUö÷35÷&VFW&2F6²×7V6–f–2Æöv–â&öÆRv—F‚ÖVÖ&W'6†—–â†FU÷&VFW&² ¢¢†FUö÷35÷&VFW&v—F‚”ä„U$•F² ¢¢6öææV7F–öâÆ–Ö—B&² ¢¢F†RF—7Æ–VB7WW'W6W"Â7&VFRÖFF&6RÂ7&VFR×&öÆRÂ&WÆ–6F–öâÂæB'—72Õ$Å2fÆw2fÇ6S² ¢¢&öÆRFVfVÇG2f÷"&VBÖöæÇ’G&ç67F–öç2æB6V&6‚F‚†FRÂV&Æ–6²æB ¢¢&÷VæFVB&VB66W72&WV—&VBf÷"õ2Ó2ÖWFFFö'6W'fF–öâà ¥F†R&WF–æVB&÷f—6–öæ–ærWf–FVæ6R&V6÷&G27V66W76gVÂ÷7Fw&U5Â6öÖÖæB7FGW6W2ÂF†R&W7VÇF–ær&öÆR&÷w2ÂæB7F—fRÖVÖ&W'6†—â—BFöW2æ÷B–æFWVæFVçFÇ’&W6W'fRF†RW†7BW†V7WFVB5Â'—FW2÷"F†R6ö×ÆWFRw&çBæBFVfVÇB×&—f–ÆVvRö&¦V7Bw&‚à ¥&VFW"fW&–f–6F–öâF—&V7FÇ’&÷fW3  ¢¢VffV7F—fR&öÆR†FUö÷35÷&VFW&² ¢¢G&ç67F–öâ&VBÖöæÇ’G'VS² ¢¢W†7B6V&6‚F‚†FRÂV&Æ–6² ¢¢&öÇ7WW#ÖfÇ6V² ¢¢&öÆ7&VFVF#ÖfÇ6V² ¢¢&öÆ7&VFW&öÆSÖfÇ6V² ¢¢&öÇ&WÆ–6F–öãÖfÇ6V² ¢¢&öÆ'—77&Ç3ÖfÇ6V² ¢¢66†VÖö7&VFSÖfÇ6V² ¢¢&VÆF–öå÷w&—FSÖfÇ6V² ¢¢&WV—&VB&öG”w&‚6öÇVÖâÖWFFFf—6–&ÆS² ¢¢&WV—&VB&öG”w&‚6öç7G&–çBÖWFFFf—6–&ÆS² ¢¢&÷F‚&÷VæF'’f–Ww2f—6–&ÆS² ¢¢&÷F‚W‡V7FVB'F—F–öæVBF&ÆW2f—6–&ÆS²æB ¢¢fW&–f–6F–öâ6ö×ÆWFVBv—F‚$ôÄÄ$4¶à ¥÷7BÖ6GW&R6ÆVçWF—&V7FÇ’&÷fW3  ¢¢†FUö÷35÷&VFW&†2Æöv–âF—6&ÆVC² ¢¢—G277v÷&B—26ÆV&VC² ¢¢†FU÷&VFW&&VÖ–ç2äôÄôt”æ²æB ¢¢ÖVÖ&W'6†—öb†FUö÷35÷&VFW&–â†FU÷&VFW&&VÖ–ç2&W6VçBà ¥F†R&WF–æVB&öÆRÖöFVÂ—2FVÆ–&W&FVÇ’&÷VæFVBâ†FU÷&VFW&—2&WW6&ÆR&VB6&–Æ—G’â†FUö÷35÷&VFW&—2F—6&ÆVBF6²&–æ6—Âv†÷6R&WF–æVBÖVÖ&W'6†—FöW2æ÷BWF†÷&—¦R7W'&VçBÆöv–âà ¥F†—2÷7GW&RFöW2æ÷BW7F&Æ—6‚6ö×ÆWFRÆ–6F–öâÂw&—FW"ÂÖ–w&F–öâÂ÷væW'6†—ÂFÖ–æ—7G&F–öâÂFWÆ÷–ÖVçBÂ7&VFVçF–Â×&÷FF–öâÂ&V6÷fW'’Â÷"'&V²ÖvÆ72&öÆR&6†—FV7GW&Rà ¢222¢¤WF†÷&—¦F–öâæBF—&V7B6GW&R¢  ¤õ2Ó2W†V7WFVBVæFW#  ¢¢'Vâ”B÷32×&öÆVf—‚ÖfFC6#s“#s#CSc–v3#Fcƒ6² ¢¢6÷W&6R6öÖÖ—BC6FCf#“sSCC&Cv“3#–66ffc–ccCƒ6–CFfVS&² ¢¢WF†÷&—¦F–öâv–æF÷r##bÓrÓ#5C#3£3£•¦F‡&÷Vv‚##bÓrÓ#EC£3£•¦² ¢¢WF†÷&—¦F–öâ4„Ó#Sb“6&6–Cƒ“#cV“#sf#CscfFS33&&F3–S&6FCS–cs6fFf6ƒVV² ¢¢'VææW"4„Ó#SbV#C–fFcFfvVVfSVfFfvfCVF&C#&ƒc#S3V3ƒF##CƒV&3CS#SSCvV†f² ¢¢fÆ–FF÷"4„Ó#SbVV&#VcVCƒ3S&FV#ƒƒ&FCSC–F3fS†VC†6#C3s#“3f#V36#c–C†f² ¢¢–çFW'&WFW"4„Ó#SbCfCV6s“F##““S–c#†S““vc#s3vF&3ƒvCV#&Ssƒ6V6f3CFS“sƒ“3s“#&² ¢¢F—&V7B&÷f–FW"7–6÷v² ¢¢ôTåcÖFWf² ¢¢66†VÖ†FV² ¢¢6V&6‚F‚†FRÂV&Æ–6² ¢¢4dUôÔôDSÓ² ¢¢ÄÄõuôäUEtõ$³Ó² ¢¢ÄÄõuôD%õu$•DSÓ²æB ¢¢F†RWF†÷&—¦F–öâÖ&÷VæBöæRÖGFV×B6öçG&7Bà ¥F†RWF†÷&—¦F–öâ&–æG2F†RW†7B6÷W&6R6öÖÖ—BÂ'VææW"†6‚ÂfÆ–FF÷"†6‚Â–çFW'&WFW"F‚æB†6‚ÂF&vWBÂ&–Ç2Â&WF—&VBÖ¶W’&÷7FW"Â÷&FW&VBVW'’&÷7FW"ÂW‡V7FVB6÷VçG2Â6æF–FFR&ö÷BÂF‡&VR&wbfV7F÷'2ÂæBöæRÖGFV×B'VÆRâ—B6öçF–ç2æòFF&6R†÷7BÂE4âÂ77v÷&BÂ÷"&öÆRfÇVRà ¥F†RFVâÖf–ÆR6¶WB&V6÷&G3  ¢¢õ35ô4EU$Uõ56² ¢¢W†—B6öFR¦W&ó² ¢¢V×G’7FFW'#² ¢¢6GW&R&W7VÇB56² ¢¢–æFWVæFVçBfÆ–FF–öâ&W7VÇB56² ¢¢öæR&÷f–FW"6VÆV7F–öã² ¢¢öæR†VÇF‚6öææV7F–öã² ¢¢öæR†VÇF‚5Â7FFVÖVçC² ¢¢öæR&VBÖöæÇ’÷7GW&RG&ç67F–öã² ¢¢FVâ÷7GW&R5Â7FFVÖVçG3² ¢¢GvòF—&V7B6öææV7F–öç3² ¢¢VÆWfVâ5Â7FFVÖVçG2F÷FÃ² ¢¢¦W&ò5Âw&—FW3² ¢¢¦W&ò&WG&–W3² ¢¢¦W&òÇFW&æFR×&÷f–FW"GFV×G3² ¢¢W†7B6V&6‚Fƒ² ¢¢ÆV7B×&—f–ÆVvR'VçF–ÖR÷7GW&S² ¢¢fÆ–BDDÂ–FVçF—G’&ö¦V7F–öã² ¢¢&WV—&VB6öç7G&–çBö'6W'fF–öç3² ¢¢&VBÖöæÇ’&÷VæF'’f–Ww3² ¢¢W‡V7FVB'F—F–öâ÷7GW&S² ¢¢W†7B6æöæ–6Â–çfVçF÷'“² ¢¢fÆ–B6†V6·7V×3²æB ¢¢6V7&WB×6fR&WF–æVB6öçFVçBà ¤ÆÂVÆWfVâFV6—6—fR6GW&R&VF–6FW2æBÆÂV–v‡B–æFWVæFVçB×fÆ–FF–öâ&VF–6FW2&RG'VRà ¥F†RFW&Ö–æÂ6öçG&öÂ7FFR&V6÷&G3  ¢¢ÆVæ6…ö6öç7VÖVC×G'VV² ¢¢f–æÆ—¦VC×G'VV² ¢¢6VÆVC×G'VV²æB ¢¢æòf–ÇW&R6¶WBà ¥F†R6¶WB6†V6·7VÒÆVFvW"4„Ó#Sb—3  ¦S#fS#VFS3ssSV#Fc#sf†C†Ccv3F&6V3c63&cs–Ff6SsƒcƒFS6&Sf&3&  ¥F†R&öÆRÖWf–FVæ6R6†V6·7VÒÆVFvW"4„Ó#Sb—3  ¦““ƒ–FF&Cf6VCc“3v3“F3S†C63FSCV#sFV3c–&Cs–VFC#c–scf33fF  ¥F†R&Wf–WvVBWf–FVæ6R'VæFÆR4„Ó#Sb—3  ¦S6CS3Cƒ“C“ƒcS“vV#3C†F63Sc–#“36sFF3ƒf&“Ssf–CcS–v  ¢222¢¤Wf–FVæ6RVÆ–f–6F–öç2¢  ¥F†RföÆÆ÷v–ærVÆ–f–6F–öç2&RæöâÖ&Æö6¶–æræBFòæ÷B–çfÆ–FFRF†R&÷VæFVB&öÆR÷WF6öÖR÷"F—&V7B6GW&S  ¢¢W†7BÖ'—FR&öGV7B÷væW"&÷fÂ—2&V6÷&FVB–âF†R÷W&F÷"&V6÷&Bâæò6W&FR&÷fÂ'F–f7B—2&WF–æVBâ ¢¢&RÖWF†÷&—¦F–öâ&VFW"Ö6öææV7F–öâ6WVVæ6RF–Bæ÷BW7F&Æ—6‚FF&6R6öææV7F–öâ&V6W6RF†R–ç7FÆÆVB÷7Fw&U5Â6Æ–VçBF–Bæ÷B66WBF†RgVÆÂU$’F‡&÷Vv‚tDD$4V–âF†R&W67&–&VBf÷&ÒâF†R÷W&F÷"&V6÷&B&W÷'G26ö×ÆWFR&öÆÆ&6²ÂF&vWB×&öÆR'6Væ6RÂæBg&W6‚&÷f—6–öæ–ær&Vf÷&Rç’WF†÷&—¦F–öâv27&VFVB÷"6öç7VÖVBâæò7FæFÆöæR&öÆÆ&6²G&ç67&—B—2&WF–æVBâ ¢¢7V66W76gVÂ&VFW"fW&–f–6F–öâW6VBFV6ö×÷6VBÆ–'6öææV7F–öâf–VÆG2†VÆB–âÖVÖ÷'’âF†R&WF–æVBfW&–f–6F–öâf–ÆRF—&V7FÇ’&÷fW2F†R&WV—&VB–FVçF—G’Â&VBÖöæÇ’÷7GW&RÂ6V&6‚F‚ÂÆV7B×&—f–ÆVvRfÆw2ÂÖWFFFf—6–&–Æ—G’ÂæB&öÆÆ&6²â ¢¢F†R6†&VB6†V6¶÷WB6öçF–æVB–væ÷&VB—F†öâ'—FV6öFRâW†V7WF–öâW6VBâW‡FW&æÂ&—7F–æR6†V6¶÷WBBF†RW†7B6÷W&6R6öÖÖ—BæBâ—6öÆFVB–çFW'&WFW"âF†RWF†÷&—¦F–öâ&–æG2F†B6÷W&6RæB–çFW'&WFW"ÂæB–æFWVæFVçBfÆ–FF–öâ&W÷'G2fÆ–B6÷W&6R–FVçF—G’â ¢¢&–Çv’Då2f–ÆVBv†–ÆR&V÷Væ–ærF†R6öçG&öÂ×ÆæR6öææV7F–öâf÷"ÖæFF÷'’6ÆVçWâF†R÷W&F÷"&V6÷&B&W÷'G2W6RöbÇ&VG’WF†÷&—¦VBFÖ–æ—7G&F—fR÷7Fw&U5Â6öææV7F–öâFF†VÆB–âÖVÖ÷'’6öÆVÇ’f÷"Æöv–âF—6&ÆVÖVçBÂ77v÷&B6ÆV&–ærÂæBf–æÂfW&–f–6F–öââF†R&WF–æVB6ÆVçWWf–FVæ6RF—&V7FÇ’&÷fW2F†R&WV—&VBf–æÂ7FFRâ ¢¢FWF–ÆVB7V—F&–Æ—G’Â6ö×ÆWFR&—f–ÆVvR6÷fW&vRÂæBFW&Ö–æÂVæ6†ævVB×7FFR6Æ–×2f÷"†FUö÷væW&æB†FU÷'v&Ræ÷B–æFWVæFVçFÇ’6VÆVBâ ¢¢F†R&WF–æVB&÷f—6–öæ–ær÷WGWBFöW2æ÷B&÷fRF†RW†7BW†V7WFVB5Â'—FW2÷"F†R6ö×ÆWFRw&çBæBFVfVÇB×&—f–ÆVvRw&‚à ¥F†W6RVÆ–f–6F–öç2Æ–Ö—BF†R6Æ–×2F†BÖ’&RÖFRg&öÒF†RWf–FVæ6RâF†W’Fòæ÷B7&VFR&6—2f÷"6GW&R&W'VâÂ&öÆR&öÆÆ&6²ÂFÖ–æ—7G&F—fR×&öÆRW†6WF–öâÂ÷"6÷W&6RÖ6öFR&VÖVF–F–öâà ¢222¢¥&W÷6—F÷'’–çF¶RæB"Óe"Ô"&÷VæF'’¢  ¥F†RFVâ6GW&R&–Ö&–W2&RG&6¶VBC  ¦VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö  ¥F†RWF†÷&—¦F–öâÂ6öçG&öÂÂ&öÆR×&÷f—6–öæ–ærÂ7F–öâÂæBF—66÷fW'’&V6÷&G2&RG&6¶VBC  ¦VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&Bö  ¤B&Wò„TBSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–f  ¢¢ÆÂFVâ6GW&R&–Ö&–W2&RG&6¶VC² ¢¢ÆÂGvVÇfR÷W&F÷"&V6÷&G2&RG&6¶VC² ¢¢WfW'’G&6¶VB6÷’—2'—FRÖ–FVçF–6ÂFòF†R&Wf–WvVBWf–FVæ6R'VæFÆS² ¢¢F†R'VææW"ÂfÆ–FF÷"ÂæB6WfVâõ2Ó266†VÖ2&VÖ–âVæ6†ævVBg&öÒ6÷W&6R6öÖÖ—BC6FCf#“sSCC&Cv“3#–66ffc–ccCƒ6–CFfVS&²æB ¢¢æò'VæFÆR×FòÕ&Wò6öçG&F–7F–öâv2f÷VæBà ¥F†R6æöæ–6Â6¶WB&ö÷B&VÖ–ç2Æ–Ö—FVBFò—G2FVâ&–Ö&–W2æBgWGW&RWFFW"ÖvVæW&FVB6–&Æ–ærF‚&öög2â7WÆVÖVçFÂ&V6÷&G2&VÖ–â–âF†RF¦6VçB÷W&F÷"×&V6÷&B&ö÷B6òF†W’Fòæ÷BÇFW"F†R6¶WB–çfVçF÷'’6öçG&7Bà ¥F†RG&6¶VB6¶WB†2æ÷B6ö×ÆWFVBv÷fW&æVBWf–FVæ6RFÖ—76–öââ"Óe"Ô"÷vç3  ¢¢F†RF—&V7B×6VÆV7F–öâ&–Ö'“² ¢¢6æöæ–6ÂWFFW"&–æF–æw2f÷"F†Rõ2Ó2&–Ö&–W2æB6WfVâõ2Ó266†VÖ3² ¢¢FVâ6–&Æ–ærF‚&öög2f÷"F†R6GW&VB&–Ö&–W3² ¢¢‡VÖâWf–FVæ6R–æFW‚&÷w2æBF†RWFFVB†6‚6VçF–æVÃ² ¢¢Ö6†–æRWf–FVæ6RÖ—'&÷"&÷w3² ¢¢7W'&VçB×fW'7W2Ö†—7F÷&–6ÂWf–FVæ6R&–æF–æs² ¢¢f–æÂF—&V7BÖöæÇ’&VÆV6R–çFVw&F–öã² ¢¢F†R&÷r×7V6–f–27W÷'B7&÷77vÆ³²æB ¢¢f–æÂfÆ–FF–öâöbF†R6ö×ÆWFRv÷fW&æVBWf–FVæ6Rw&‚à ¥VçF–ÂF†Bv÷&²—26ö×ÆWFRÂF†R6¶WB6ææ÷B7W÷'Bf–æÂv÷fW&æVBFÖ—76–öâÂf–æÂ&VÆV6R×6æ—G’52Â÷"c’7FGW27F–öââF†÷6RF÷vç7G&VÒö&Æ–vF–öç2Fòæ÷B&WfW'6Rõ2Ó266WFæ6RæBFòæ÷BWF†÷&—¦Ræ÷F†W"õ2Ó2W†V7WF–öâà ¥F†RFVâ6GW&VB&–Ö'’'—FW2×W7B&VÖ–âVæ6†ævVBF‡&÷Vv‚"Óe"Ô"fÆ–FF–öâæBFÖ—76–öâà ¢222¢¤FF&6RÕ&öÆRÆææ–ær'VÆW2¢  ¤FF&6R×&öÆRÆææ–ær×W7B¶VWF†W6R6FVv÷&–W2F—7F–æ7C  ¢¢¢¤ö'6W'fVBÆ—fR&öÆR7FFS¢¢¢&öÆW2æBGG&–'WFW2F—&V7FÇ’&WGW&æVB'’&÷VæFVBÆ—fR–ç7V7F–öââ ¢¢¢¥F&vWB×&öÆR'6Væ6S¢¢¢F†RFVF–6FVB–FVçF—F–W26VÆV7FVBf÷"â÷W&F–öâ&Ræ÷B&W6VçB&Vf÷&R&÷f—6–öæ–ærâ ¢¢¢¤FW6—&VB6V7W&—G’÷7GW&S¢¢¢&öÆRæÖW2Â&—f–ÆVvRÖG&–6W2ÂFW7G2Â66†VÖ2Â÷"&VF–6FW2F†BFW67&–&Rv†Bâ–×ÆVÖVçFF–öâv–ÆÂ66WBâ ¢¢¢¤WF†÷&—¦VB×WF&ÆR&V7W'6÷#¢¢¢&÷VæFVBFF&6R6†ævW2&WV—&VB&Vf÷&R&VBÖöæÇ’÷W&F–öæÂ6GW&R6â'Vââ ¢¢¢¤F—&V7B6GW&R÷7GW&S¢¢¢WF†÷&—¦F–öâÖ&÷VæBÂF—&V7BÖöæÇ’Â&VBÖöæÇ’ö'6W'fF–öâv—F‚æò5Âw&—FW2â ¢¢¢¥&÷f—6–öæVB&÷VæFVB÷7GW&S¢¢¢&öÆRæB&—f–ÆVvR÷WF6öÖW2F—&V7FÇ’7W÷'FVB'’&WF–æVB÷W&F–öæÂWf–FVæ6Râ ¢¢¢¤6ö×ÆWFR&öÆR&6†—FV7GW&S¢¢¢F†R6W&FVÇ’v÷fW&æVBÆ–6F–öâÂw&—FW"ÂÖ–w&F–öâÂ÷væW"ÂFÖ–æ—7G&F–öâÂFWÆ÷–ÖVçBÂ&÷FF–öâÂ&V6÷fW'’ÂæB–æ6–FVçBÖ†æFÆ–ærÖöFVÂà ¥&W÷6—F÷'’æÖW2Âf—‡GW&W2Â66†VÖf–VÆG2Â66WFæ6R&VF–6FW2Âbv÷&F–ærÂæBÆææVB&6†—FV7GW&RFòæ÷B&÷fRF†B6÷'&W7öæF–ærÆ—fR&öÆRW†—7G2à ¤&Vf÷&R&–æF–æröæRÖGFV×BFF&6RWF†÷&—¦F–öâÂÆææ–ær×W7C  ¢¢–ç7V7BF†RÆ—fR&öÆR&÷7FW"æBVffV7F—fR&—f–ÆVvW3² ¢¢W7F&Æ—6‚v†WF†W"âW†—7F–ær–FVçF—G’6F—6f–W2F†RW†7B÷W&F–öæÂ&VF–6FS² ¢¢ö'F–â&öGV7B÷væW"WF†÷&—¦F–öâf÷"ç’&WV—&VB×WF&ÆR&V7W'6÷#² ¢¢6ö×ÆWFRæBfW&–g’F†B&V7W'6÷"&Vf÷&R6öç7G'V7F–ærWF†÷&—¦F–öâ'—FW3² ¢¢&WF–âW†7B5Â÷"âWF†÷&—FF—fRWV—fÆVçBv†VâÆFW"6Æ–×2FWVæBöâF†R6ö×ÆWFRw&çBÖöFVÃ² ¢¢&W6W'fR&R×7FFRæB÷7B×7FFRv†Vâ6Æ–Ö–ærF†BW†—7F–ær&öÆW2&VÖ–æVBVæ6†ævVC²æB ¢¢W†6ÇVFR7&VFVçF–ÂfÇVW2g&öÒ&WF–æVBWf–FVæ6Rà ¢222¢¥c’÷7GW&R¢  ¤õ2Ó2&÷f–FW2&÷VæFVBÆ—fRFV6†æ–6ÂWf–FVæ6R&VÆWfçBFó  ¢¢„DRÕ4Uã6Âf÷"F†R&VFW"×&öÆR&÷f—6–öæ–æræBfW&–f–6F–öâW&f÷&ÖVBGW&–ærF†—2F6³² ¢¢„DRÔD•5CãFÂf÷"'VçF–ÖR&öÆR÷7GW&RÂ&VBÖöæÇ’G&ç67F–öâ÷7GW&RÂW†7B6V&6‚F‚ÂDDÂ–FVçF—G’Â6öç7G&–çG2Â&÷VæF'’f–Ww2ÂæB'F—F–öâö'6W'fF–öç3²æB ¢¢„DRÔD•5Cã’(	BF—&V7BFF&6R6öææV7F—f—G’b&WF—&VB×G&ç7÷'BVæf÷&6VÖVçFÂf÷"F—&V7B7–6÷v6öææV7F—f—G’Â&WF—&VBÖ¶W’'6Væ6RÂ¦W&òÇFW&æFR×&÷f–FW"GFV×G2ÂæBÆ—fR&VBÖöæÇ’÷7GW&Rà ¦„DRÕ4Uã6&VÖ–ç2&V6÷&FVB2FöæVâõ2Ó2FöW2æ÷B&V÷VâÂ&WfÆ–FFRÂ6ö×ÆWFRÂ÷"Ö÷fR—BâF†R&÷VæFVB&VFW"×&öÆR&W7VÇBFöW2æ÷BW7F&Æ—6‚F†R6ö×ÆWFRFF&6R×&öÆR&6†—FV7GW&R÷"F†RgVÆÂ&÷fVææ6RæB&—f–ÆVvRw&‚öbF†Rö'6W'fVB„DRÖæÖVB&öÆW2à ¦„DRÔD•5CãFæB„DRÔD•5Cã–&VÖ–â'F–Æâõ2Ó27WÆ–W2Æ—fRFV6†æ–6ÂWf–FVæ6RÂv†–ÆRF†V—"&VÖ–æ–ær6ö×ÆWF–öâ&VF–6FW2–æ6ÇVFRv÷fW&æVBWf–FVæ6R&–æF–æw2æBF†R&W7BöbV6‚&÷~(	—2Æ–6&ÆR66÷Rà ¦„DRÔD•5CãfæB„DRÔD•5CRã&&VÖ–â'F–ÆÂæB„DRÔD•5Cã&VÖ–ç2÷F–öæÆâF†V—"&VÆV6R×—VÆ–æRÂWf–FVæ6RÖw&‚ÂæBÖVBÖ66†RÖVæ–æw2&VÖ–âv—F†–â"Óe"Ô"÷"6W&FRc’ÖÖ–çFVææ6R&÷VæF&–W2à ¤æòc’F6²Â7V'F6²Â&V÷Væ–ærÂ7FGW26†ævRÂ6ö×ÆWF–öâÂ÷"†6RÆ6VÖVçB—27&VFVB'’F†—2FFVæGVÒà ¢222¢¤W‡Æ–6—Bæöæ6Æ–×2¢  ¥F†—2FFVæGVÒFöW2æ÷C  ¢¢6Æ–ÒF†Bæò„DRÖæÖVBFF&6R&öÆW2W†—7FVB&Vf÷&Rõ2Ó3² ¢¢6Æ–ÒF†BöæÇ’÷7Fw&W6W†—7FVC² ¢¢&÷fRF†R7&VF–öâ†—7F÷'’öb†FUö÷væW&÷"†FU÷'v² ¢¢&÷fRF†R6ö×ÆWFRÖVÖ&W'6†—÷"ö&¦V7BÖÆWfVÂ&—f–ÆVvRw&‚öb†FUö÷væW&÷"†FU÷'v² ¢¢&÷fR6VÆVBFW&Ö–æÂ7FFRf÷"F†RÆVv7’&öÆW3² ¢¢&÷fRF†RW†7BW†V7WFVB&÷f—6–öæ–ær5Â'—FW3² ¢¢&÷fRF†R6ö×ÆWFRw&çB÷"FVfVÇB×&—f–ÆVvRÖöFVÃ² ¢¢&÷fR7FæFÆöæR&RÖWF†÷&—¦F–öâ&öÆÆ&6²G&ç67&—C² ¢¢&÷fR6ö×ÆWFR„DRFF&6R×&öÆR&6†—FV7GW&S² ¢¢Væ&ÆR†FUö÷35÷&VFW&Æöv–ã² ¢¢WF†÷&—¦Rç’æWrFF&6R×WFF–öâ÷"7&VFVçF–Â—77Væ6S² ¢¢WF†÷&—¦R÷"W†V7WFRæ÷F†W"õ2Ó2GFV×C² ¢¢ÖöF–g’F†RFVâ6GW&VB&–Ö'’f–ÆW3² ¢¢&÷fR&–Çv’–çfVçF÷'’&W–öæBF†R&÷VæFVBF&vWB&V6÷&C² ¢¢&÷fR&WF—&VBG&ç7÷'Bf–Æ&–Æ—G“² ¢¢6ö×ÆWFRv÷fW&æVBWf–FVæ6RFÖ—76–öã² ¢¢6ö×ÆWFR"Óe"Ô"÷"F†Rf–æÂ&VÆV6R—VÆ–æS² ¢¢W7F&Æ—6‚53² ¢¢6F—6g’â66WFæ6RFö¶Vã² ¢¢Ö÷fRc’7FGW3² ¢¢WF†÷&—¦RFWÆ÷–ÖVçB÷"Ö–w&F–öã² ¢¢6ö×ÆWFR„DRÔU”33ƒ²÷" ¢¢6Æ÷6RF†RW–2à ¢22"ã#’"Ób&VÖVF–F–öâ"Óe"Ô"„DRÔU”33€ ¤'F–f7BÖ  ¥"æÖS¢"Óe"Ô  ¤ÖW&vVB"&Vc¢3cp ¤&÷fVBÆã¢&÷fVB×&W66÷–ærÖ7&BÖ†FRÖW–33‚×÷7B×#3S’×&VÖVF–F–öâ×cãBæÖ@ ¤÷F–öæÂ"'F–f7G3¢æ÷B&÷f–FV@ ¥&Wò&ö÷B&Wf–WvVC¢×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c  ¤÷WGWC¢÷7BÔÖW&vR"6öFR&Wf–WræBfÆ–FF–öà ¥&Wf–Wr7VÖÖ' ¢¢"Â33crÖW&vVBF†RÆææVB"Óe"Ô"F—&V7BÖöæÇ’f–æÂ–çFVw&F–öââ—BFÖ—GFVBF†RFWFW&Ö–æ—7F–2F—&V7B×6VÆV7F–öâ'F–f7BæB66WFVBõ2Ó26¶WBÂ6W&FVB†—7F÷&–6Â'&–FvRWf–FVæ6Rg&öÒ7W'&VçBWf–FVæ6RÂ6ö×ÆWFVBF†Ræ–æWFVVâ×7FvR&VÆV6RvFRÂæBFFVBW†7BÖ†VBW‡FW&æÂGFW7FF–öââ ¢¢F†RÖW&vVBVæGö–çB—27W'&VçBÖ–äF#3S–&36c“V33S“Ssffs33–S““c&âÆÂCb6†ævVBÖf–ÆR&Æö'2&R–FVçF–6Â&WGvVVâ"†VBs6Ccvf3V#FS&fFcƒf3#SC&33–F3#FæBF†RÖW&vR6öÖÖ—BÂ6òÖW&vR&W6öÇWF–öâ–çG&öGV6VBæò6öçFVçBF—fW&vVæ6Râ ¢¢WfW'’6†ævVBf–ÆR&V6V—fVB6öÖÖ—GFVB×7FFR&Wf–Wr–â4e"ÓF‡&÷Vv‚4e"ÓCbâF†R–×ÆVÖVçFF–öâföÆÆ÷w2F†R&÷fVBÆî(	—266÷RæBW†6ÇW6–öç3²æò–×ÆVÖVçFF–öâ&VÖVF–F–öâ÷"Vç6fR66÷RW‡ç6–öâv2f÷VæBâ ¢¢W†7BÖ†VB4’'Vâ3scSƒ“#676VBÆÂ6WfVâ¦ö'2â—G2Ö–â¦ö"76VBÃcRWf–FVæ6Rôõ2FW7G2Â#SF—&V7B÷7Fw&U5Â6öçG&7BFW7G2ÂæBÆÂvVæW&FVBÖWf–FVæ6RÂÖ—'&÷"Â†6‚Âf–æÂÔÄbÂ4Ä’ÂæB&–Ç26†V6·2â ¢¢W‡FW&æÂ'F–f7BƒSƒƒ#sCcƒ–—2&÷VæBFòF†R–Ö×WF&ÆR"†VBÂ†2fW&–f–VBF–vW7B6†#Sc£s#FSS“Sv3CCfFV#3S#3fFV6&S6c3S–cVFfCC–6CCc3c&&3c†FÂæB&V6÷&G2#e%ô%ôd”äÅõ56v—F‚ÆÂæ–æWFVVâ7FvW276–æræBæò—VÆ–æR7F÷â ¢¢æò66WFæ6R÷"Fö¶Vâ6F—6f7F–öâ—26Æ–ÖVBâF†RGFW7FF–öâW‡&W76Ç’F—66Æ–×2õ2W†V7WF–öâÂFF&6Rw&—FW2ÂFWÆ÷–ÖVçBÂÖ–w&F–öâÂ52Â66WFæ6RÂæBc’7FGW2Ö÷fVÖVçBâ ¢¢&WòWf–FVæ6Ræ÷r7W÷'G26W&FRc’Ö–çFVææ6R&V6öÖÖVæFF–öç2öb6†ævRFòFöæVf÷"„DRÔD•5CãFÂãfÂã–ÂãÂæB„DRÔD•5CRã&âc’—G6VÆbv2æ÷BVF—FVBâ ¢¢$46öæf—&×2F†BF†RÖW&vVB6†ævRFG&W76W2F†R&÷fVB'&–FvR×&WF—&VÖVçBÂ†—7F÷&–6Âö7W'&VçBWf–FVæ6R6öæfÆF–öâÂæBÖ—76–ærFöÖ–2f–æÂÖFÖ—76–öâ6W6W2âW&ÖæVçBbFö7VÖVçFF–öâG&–ævR&VÖ–ç2Â'WBF†R&÷fVBÆâ6Æ76–f–W2F†B2æöæ&Æö6¶–ærFö7VÖVçFF–öâv÷&²à ¥&Wò–ç7V7F–öà ¢¢ö'6W'fVB&Wò&ö÷C¢×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c&â ¢¢ö'6W'fVB„TC¢F#3S–&36c“V33S“Ssffs33–S““c&â ¢¢'&æ6‚÷"FWF6†VB7FFS¢6öææV7FVB&VÖ÷FRFVfVÇB'&æ6‚Ö–æ²FWF6†VB7FFRæ÷BÆ–6&ÆRâ ¢¢v÷&¶–ær×G&VR7FGW2&Vf÷&R&Wf–Ws¢æ÷BÆ–6&ÆR&V6W6RF†R6öææV7FVBv—D‡V"&W÷6—F÷'’W‡÷6W26öÖÖ—GFVB7FFR&F†W"F†â×WF&ÆRÆö6Âv÷&·G&VRâ ¢¢&W6öÇWF–öâÖWF†öBf÷"ÔU$tTEõ%õ$Tf¢v—D‡V""ÖWFFFf÷"µ"Â33cuÒ†‡GG3¢òöv—F‡V"æ6öÒö×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c"÷VÆÂó3cr’Â—G2&6Rö†VBöÖW&vR6öÖÖ—G2Âf—'7B×&VçB&6R×FòÖÖW&vR6ö×&—6öâÂ6†ævVBÖf–ÆR–çfVçF÷'’Â&Wf–WrF‡&VG2ÂæB7F–öç2&W7VÇG2â ¢¢&W6öÇfVB&ævS¢&6RC#FC“SSC“3C–cc†##6#3c–cssƒc&f#“ƒ3vCvF‡&÷Vv‚"†VBs6Ccvf3V#FS&fFcƒf3#SC&33–F3#FÂÖW&vVB2F#3S–&36c“V33S“Ssffs33–S““c&â ¢¢VæGö–çB&VÆF–öç6†—Fò„TC¢F†RÖW&vR6öÖÖ—BWVÇ27W'&VçBÖ–æ„TBâ ¢¢6†ævVBf–ÆW2&Wf–WvVC¢ÆÂCbf–ÆW2–âF†RÖW&vVBf—'7B×&VçBF–fbâ ¢¢ÖFW&–ÂÆFW"6öÖÖ—GFVBF—fW&vVæ6S¢æöæRö'6W'fVBâÖW&vR×FòÖ7W'&VçBÖÖ–â6ö×&—6öâ—2–FVçF–6ÂÂæBÆÂCb"Ö†VBæBÖW&vRÖ6öÖÖ—B&Æö"4„2ÖF6‚â ¢¢ÖFW&–Â÷fW&Æ–ærv÷&·G&VRF—fW&vVæ6S¢æ÷BÆ–6&ÆS²æò×WF&ÆRv÷&·G&VRv2W6VBâ ¢¢v÷&¶–ær×G&VR7FGW2gFW"fÆ–FF–öã¢æ÷BÆ–6&ÆS²&Wf–Wr&VÖ–æVB&VBÖöæÇ’à ¤6†ævVBf–ÆR&Wf–Wp ¤4e"Ó ¤f–ÆS¢æv—F‡V"÷v÷&¶fÆ÷w2ö6’ç–ÖÆ ¤6†ævR7VÖÖ'“¢&–æG2W‡FW&æÂGFW7FF–öâFòF†R–Ö×WF&ÆR"Ö†VB4„Â–ç7FÆÇ2öffÆ–æRv†VVÂ&W&WV—6—FW2ÂæBÆ–W2f–æÂ"Óe"Ô"FÖ—76–öâW‡V7FF–öç2â ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BâF†Rv÷&¶fÆ÷ræòÆöævW"GFW7G2v—D‡V.(	—27–çF†WF–2ÖW&vR&VbæBFöW2æ÷B&W—"6öÖÖ—GFVBWf–FVæ6R&Vf÷&R6†V6¶–ær—Bâ ¤&÷fVBÆâÆ–æ¶vS¢W†7BÖ†VBW‡FW&æÂGFW7FF–öâæB7G&–7Bf–æÂ&VÆV6RFÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢G·²v—F‡V"æWfVçBçVÆÅ÷&WVW7Bæ†VBç6†ÇÂv—F‡V"ç6†×Ö6öçG&öÇ26†V6¶÷WBæB'F–f7BæÖ–æs²W†7BÖ†VB'Vâ3scSƒ“#676VBâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c(	B„DR'V–ÆBæ÷FW2Â*s"ãbà ¤4e"Ó  ¤f–ÆS¢'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆ ¤6†ævR7VÖÖ'“¢&VvVæW&FW2F†RÖ6†–æRÖ—'&÷"v—F‚F—&V7B×6VÆV7F–öâÂõ2Ó2ÂæB†—7F÷&–6ÂÖöæÇ’'&–FvR÷&÷f–FW"×&—G’&–æF–æw2â ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7B6æöæ–6Âf—†VB×ö–çB÷WGWC¢SC‚&V6÷&G2ÂÆÂ’æWr¶W—2W†7FÇ’öæ6RÂæB#B†—7F÷&–6ÂÖöæÇ’&V6÷&G2v—F†÷WB7F—fRFö¶Vç2â ¤&÷fVBÆâÆ–æ¶vS¢v÷fW&æVBWf–FVæ6RFÖ—76–öâæB7W'&VçB×fW'7W2Ö†—7F÷&–6Â6W&F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢6ö×ÆWFR¥4ôäÂ–ç7V7F–öâf÷VæBSC‚6æöæ–6Â&÷w2æBW†7BF—&V7Bôõ2Ó2¶W’6÷fW&vRâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã^(	3"ãc²c"(	B„DR66†VÖ2æB'F–f7G2Â*s‚ã2à ¤4e"Ó0 ¤f–ÆS¢'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÂçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢&Vg&W6†W2F†RÖ6†–æRÖ—'&÷.(	—26–&Æ–ær&ööbâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BF‚Â6—¦RÂ4„Ó#SbÂæBUD2F–ÖW7F××6†R&–æF–ærâ ¤&÷fVBÆâÆ–æ¶vS¢6æöæ–6ÂWFFW"Ö÷væVB6ö×æ–öâvVæW&F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&ööb&–æG2'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆæBw&VW2v—F‚F†R6öÖÖ—GFVBÖ—'&÷"†6‚â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãc²c"*s‚ã2à ¤4e"Ó@ ¤f–ÆS¢'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÂç6†#Sf ¤6†ævR7VÖÖ'“¢6VÇ2F†Rf–æÂÖ6†–æRÖ—'&÷"â ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7B†6‚6VçF–æVÂâ ¤&÷fVBÆâÆ–æ¶vS¢FöÖ–2Wf–FVæ6RÖw&‚6öçfW&vVæ6Râ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&V6÷&FVB4„Ó#Sb—2vC#“V#csf&VS“†&cƒsƒƒ3VFf&f33S†VV6SCCc“sSc–##v&c&CF3“V6â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c"*s‚ã2à ¤4e"ÓP ¤f–ÆS¢'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÂç6†#SbçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2F†RÖ—'&÷"Ö†6‚6VçF–æVÎ(	—26–&Æ–ær&ööbâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BæBWFFW"Ö÷væVBâ ¤&÷fVBÆâÆ–æ¶vS¢6ö×ÆWFR6ö×æ–öâF÷öÆöw’â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&ööbF‚æB&–Ö'’4„w&VRv—F‚F†R6öÖÖ—GFVB6VçF–æVÂâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãc²c"*s‚ã2à ¤4e"Ó` ¤f–ÆS¢'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæ ¤6†ævR7VÖÖ'“¢FG2FWFW&Ö–æ—7F–2F—&V7BÖöæÇ’&÷f–FW"×6VÆV7F–öâWf–FVæ6Râ ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ—B6öçF–ç2F†Rf÷W"÷&FW&VB66W2ÂÆÂ6—‚&WV—&VB&VF–6FW2Â&W7VÇCÕ56Âf–ÇW&SÖçVÆÆÂæB6æöæ–6ÂöæRÔÄb'—FW2â ¤&÷fVBÆâÆ–æ¶vS¢&WV—&VB"Óe"Ô"F—&V7B×6VÆV7F–öâ&–Ö'’â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢66†VÖ—2†FUöW–33‚æF—&V7EöF%÷6VÆV7F–öâçc²4„Ó#Sb—2Cƒ†6fc&fcFc“cSvcss“sC##cFfcƒ36F3C6&#s&3&CS3&fC#3“cc–&â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã"Â"ãRÂæB"ã’à ¤4e"Óp ¤f–ÆS¢'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2F†RF—&V7B×6VÆV7F–öâ&–Ö'ž(	—26–&Æ–ær&ööbâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BF‚ö†6‚÷6—¦R&–æF–æræB÷'F&ÆRF–ÖW7F×6†Râ ¤&÷fVBÆâÆ–æ¶vS¢v÷fW&æVBFÖ—76–öâöbF†RF—&V7B×6VÆV7F–öâ&–Ö'’â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&ööb&–æG2F†R&–Ö'’Fò4„Ó#SbCƒ†6fc&fcFc“cSvcss“sC##cFfcƒ36F3C6&#s&3&CS3&fC#3“cc–&â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã^(	3"ãbà ¤4e"Ó€ ¤f–ÆS¢VF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆöv ¤6†ævR7VÖÖ'“¢&WÆ6W2G&ç6—F–öæÂ÷WGWBv—F‚F†R7G&–7Bf–æÂæ–æWFVVâ×7FvR52Æörâ ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BW†7B÷&FW&–ærÂæò6¶—2Â7FvRÓ"†—7F÷&–6Â6VçF–æVÂÂæBf–æÂ52â ¤&÷fVBÆâÆ–æ¶vS¢f–æÂ"Óe"Ô"&VÆV6R—VÆ–æRâ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢æ–æWFVVâ6†V6²äâ(
c¤ô¶&÷w2Âf—'7Eöf–ÆVE÷7FvS¤äôäVÂ7VÖÖ'“¥56²4„Ó#Sb–6#†&&3CC–f“–VSƒsv&ScƒƒCCƒ“#&#Cƒ3–S#v#3FC#Cs&Scƒ†#C&â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãRà ¤4e"Ó ¤f–ÆS¢VF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆörçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢&Vg&W6†W2F†Rf–æÂ—VÆ–æRÆö~(	—26–&Æ–ær&ööbâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BæB6öç6—7FVçBv—F‚F†R6öÖÖ—GFVB52Æörâ ¤&÷fVBÆâÆ–æ¶vS¢v÷fW&æVB&VÆV6RÖvFRWf–FVæ6Râ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&ööbF‚æB4„w&VRv—F‚4e"Ó‚â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã^(	3"ãbà ¤4e"Ó  ¤f–ÆS¢VF—BövFW2÷F÷öÆöw’ö÷&–VçFF–öåöFVÖòçG‡F ¤6†ævR7VÖÖ'“¢&VvVæW&FW2F÷öÆöw’÷&–VçFF–öâgFW"f–æÂw&‚6öçfW&vVæ6Râ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bf–æÂ×7FFR÷&–VçFF–öâ÷WGWBâ ¤&÷fVBÆâÆ–æ¶vS¢÷7B×WFFW"F÷öÆöw’fÆ–FF–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢F÷FÅö'F–f7G3¢SC†Â7FGW3¢ö¶²4„Ó#SbcS6f66VVCCCc66V#fcc36fV#&SvCvV#6VS–cS“S“cCF&SƒCv6F6â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãS²c"*s‚ã2à ¤4e"Ó ¤f–ÆS¢VF—BövFW2÷F÷öÆöw’ö÷&–VçFF–öåöFVÖòçG‡BçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢&Vg&W6†W2F†RF÷öÆöw’÷WGWN(	—26–&Æ–ær&ööbâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BæB6öç6—7FVçBv—F‚4e"Óâ ¤&÷fVBÆâÆ–æ¶vS¢6ö×ÆWFRWf–FVæ6RF÷öÆöw’â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&ööbF‚ö†6‚&–æF–ærÖF6†W2F†R÷&–VçFF–öâ'F–f7Bâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãc²c"*s‚ã2à ¤4e"Ó  ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö6†V6·7V×2ç6†#SbçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FÖ—G2F†R–Ö×WF&ÆRõ2Ó26†V6·7VÒÆVFvW"F‡&÷Vv‚6–&Æ–ær&ööbâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7C²—B&W6W'fW2&F†W"F†â&VvVæW&FW2F†R6¶WBÆVFvW"â ¤&÷fVBÆâÆ–æ¶vS¢W†7BFVâ×&–Ö'’õ2Ó2FÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2S#fS#VFS3ssSV#Fc#sf†C†Ccv3F&6V3c63&cs–Ff6SsƒcƒFS6&Sf&3&â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó0 ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö6öÖÖæG2çG‡BçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†Rõ2Ó26öÖÖæB&V6÷&Bâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢õ2Ó2&–Ö'’FÖ—76–öâv—F†÷WB'—FR6†ævW2â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—26CƒS3Vf3“sC36S†6C&3†c†3#V–33SSccss–CsCsƒSfF#C##cƒ&#vâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó@ ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öF%÷÷7GW&U÷7VÖÖ'’æ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"7W'&VçBF—&V7BFF&6R×÷7GW&RWf–FVæ6Râ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢Æ—fR&VBÖöæÇ’F—&V7B×÷7GW&R7W÷'Bâ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2&6S†63ff#&&#ƒ&C–cv&3cSv&&#cs6&FfS6c#63vf&cFS““†#&ccƒvSVFâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ãRæB"ã’à ¤4e"ÓP ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öVçe÷&W6Væ6Ræ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†RæÖW2ÖöæÇ’Vçf—&öæÖVçB×&W6Væ6R'F–f7Bâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BæB6V7&WB×6fRâ ¤&÷fVBÆâÆ–æ¶vS¢&WF—&VBÖ¶W’'6Væ6RæBF—&V7BÖ6öææV7F—f—G’Wf–FVæ6Râ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—23–6F3–CcCƒ“cvCV66VFSs3VS6&C–F“vS3ƒƒcc6Ff†S“vVV#Vc6C36Sfâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã"æB"ã’à ¤4e"Ó` ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öW†—Eö6öFRçG‡BçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†Rõ2Ó2W†—BÖ6öFR&V6÷&Bâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢66WFVB6¶WBFÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2–#sc&“f##fVSf6V6##C#fc#3#fVcsCSs†&SSVC–&3“Fcfc6fS6#ƒfâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã’à ¤4e"Óp ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öæöæ6Æ–×2æ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"õ2Ó26Æ–Ò&÷VæF&–W2â ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7C²—B&W6W'fW26W&F–öâg&öÒÂ66WFæ6RÂFWÆ÷–ÖVçBÂæBc’Ö÷fVÖVçBâ ¤&÷fVBÆâÆ–æ¶vS¢÷W&F–öæÂæBWf–FVæ6Ræöæ6Æ–×2â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2vsCF3S&sS†3–ƒ6##c“ƒ“V6vfSSs6VS&ccF#Cƒ†ƒcs#36c“FC–â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã’à ¤4e"Ó€ ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷&W7VÇE÷7VÖÖ'’æ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†Rõ2Ó2527VÖÖ'’â ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢ÖæFF÷'’7FvRÓB6¶WBfÆ–FF–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2#“Cf#FFFC3VS†V3V36FVSsVS33CC&fV333#SƒSF6&FSfVVVC6C†fSfâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ãRæB"ã’à ¤4e"Ó ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷7FFW'"æÆörçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†RV×G’õ2Ó27FFW'"&V6÷&Bâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢W†7B6¶WBæB6ÆVâÖ÷WGWBfÆ–FF–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢V×G’Öf–ÆR4„Ó#Sb—2S6#3CC#“†f33C–f&cF3ƒ““ff#“#C#vSCSCcC–#“3F6C“S““#sƒS&#ƒSVâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã’à ¤4e"Ó#  ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷7FF÷WBæÆörçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†Rõ2Ó27V66W72÷WGWBâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢W†7B66WFVB6¶WBFÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2#&#V6V36f&S“&33SSC#C66&C3C3C#3–C†&S†S“SsFVVCScS“vS3ffFFVC–â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã’à ¤4e"Ó# ¤f–ÆS¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷fÆ–FF–öå÷&V6V—Bæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†R–æFWVæFVçBõ2Ó2fÆ–FF–öâ&V6V—Bâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢6¶WB&VF–6FRfW&–f–6F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2–#3S&&#CƒC–#3ƒFF3CƒcvS“ƒfcCVC6C6VC“cFcCSvCsc3ssvF333#s“†Cfâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã’à ¤4e"Ó#  ¤f–ÆS¢Fö72öWf–FVæ6Rô”äDU‚æ§6öæ ¤6†ævR7VÖÖ'“¢&VvVæW&FW2F†R‡VÖâWf–FVæ6R–æFW‚v—F‚"Óe"Ô"FÖ—76–öâæB†—7F÷&–6ÂÖöæÇ’6Æ76–f–6F–öç2â ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7C²—B†2SC‚&÷w2æBöæR&÷rf÷"WfW'’æWr&–Ö'’æB66†VÖâ ¤&÷fVBÆâÆ–æ¶vS¢‡VÖâ–æFW‚FÖ—76–öâæB†—7F÷&–6Âö7W'&VçB6W&F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢gVÆÂ–ç7V7F–öâf÷VæBF†R6ÖR’F&vWB–FVçF—F–W22F†RÖ6†–æRÖ—'&÷"æB#B†—7F÷&–6ÂÖöæÇ’&÷w2v—F†÷WB7F—fRFö¶Vç2â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã^(	3"ãc²c"*s‚ã2à ¤4e"Ó#0 ¤f–ÆS¢Fö72öWf–FVæ6Rô”äDU‚æ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢&Vg&W6†W2F†R‡VÖâ–æFWŽ(	—26–&Æ–ær&ööbâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢6æöæ–6Â6ö×æ–öâvVæW&F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&ööbF‚ö†6‚&–æF–ærw&VW2v—F‚F†R6öÖÖ—GFVB–æFW‚â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãc²c"*s‚ã2à ¤4e"Ó#@ ¤f–ÆS¢Fö72öWf–FVæ6Rô”äDU‚ç6†#Sf ¤6†ævR7VÖÖ'“¢6VÇ2F†Rf–æÂ‡VÖâWf–FVæ6R–æFW‚â ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7B†6‚6VçF–æVÂâ ¤&÷fVBÆâÆ–æ¶vS¢FöÖ–2Wf–FVæ6R6öçfW&vVæ6Râ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&V6÷&FVB4„Ó#Sb—2–FCCSƒƒ“SƒƒsfS3CsC#C&Scv6CscSs3&#sS66ƒ6fVfF&Sâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c"*s‚ã2à ¤4e"Ó#P ¤f–ÆS¢Fö72öWf–FVæ6Rô”äDU‚ç6†#SbçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2F†R‡VÖâ–æFW‚†6‚6VçF–æVÎ(	—26–&Æ–ær&ööbâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢6ö×ÆWFRvVæW&FVB6ö×æ–öâF÷öÆöw’â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&ööbF‚æB&–Ö'’4„w&VRv—F‚4e"Ó#Bâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãc²c"*s‚ã2à ¤4e"Ó#` ¤f–ÆS¢—&ö¦V7BçFöÖÆ ¤6†ævR7VÖÖ'“¢–æ6ÇVFW2ÖF‚ò¢æ§6öæ6¶vRFF–âF†R'V–ÇBF—7G&–'WF–öââ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7B&ö÷BÖ6W6Rf—ƒ²F†R–ç7FÆÆVBv†VVÂ6öçF–ç2ÖF‚÷F‡&W6†öÆG2æ§6öæÂVæ&Æ–ærF†R&VÂ6¶vVB†F7FÆâ ¤&÷fVBÆâÆ–æ¶vS¢&VÂ6¶vRÖ–ç7FÆÆ&–Æ—G’æB6öç6öÆRÖVçG'—ö–çBfW&–f–6F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢ÖF‚Ò²"¢æ§6öâ%Ö—2&W6VçBVæFW"6¶vRFF²F†R—6öÆFVBGFW7FF–öâ–ç7FÆÆVBæB&âF†R&W7VÇF–ærv†VVÂâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãbà ¤4e"Ó#p ¤f–ÆS¢66†VÖ2ö†FUöW–33…öF—&V7EöF%÷6VÆV7F–öâçcæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†RF—&V7B×6VÆV7F–öâ66†VÖâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢F—&V7B&–Ö'’÷66†VÖFÖ—76–öâ—"â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’66†VÖ4„Ó#Sb—2FS#Cvc†VSsSVsCF#&#3Vf#ƒ3CSS“SVSS“v#F6#3FSF3ƒ3#Vâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãS²c"*s‚ã2à ¤4e"Ó#€ ¤f–ÆS¢66†VÖ2ö†FUöW–33…ö÷35öWF†÷&—¦F–öâçcæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†Rõ2Ó2WF†÷&—¦F–öâ66†VÖâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢6WfVâ×66†VÖõ2Ó2FÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2sF–##cFc6#sc“cCC&Cs3sV&3C3f3“ƒSssC“ff6F6ffSƒs3c#S#v†â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó# ¤f–ÆS¢66†VÖ2ö†FUöW–33…ö÷35öF%÷÷7GW&U÷7VÖÖ'’çcæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†RD"×÷7GW&R66†VÖâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢õ2Ó266†VÖFÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2scc#“ƒ“&CFCS3fCSV&#s†#Sc#ƒcV363ƒc6C#F33V6c“#C6#ƒƒs†–S3cfâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó3  ¤f–ÆS¢66†VÖ2ö†FUöW–33…ö÷35öVçe÷&W6Væ6Rçcæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†RVçf—&öæÖVçB×&W6Væ6R66†VÖâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢õ2Ó266†VÖFÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2Cf#FS“–SSF3#CsCvCCc–c†6cƒ36c––3“Sf#VSS“36f##s3c#ccf6â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó3 ¤f–ÆS¢66†VÖ2ö†FUöW–33…ö÷35öf–ÇW&U÷&V6V—Bçcæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†Rf–ÇW&R×&V6V—B66†VÖâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢6ö×ÆWFR6WfVâ×66†VÖ–çfVçF÷'’â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2cs†&VSCCSc6&Fcfc†SFCVV##c&cSs“fVV3Scsƒc“†Ffc–#SV&Sc6V33fâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó3  ¤f–ÆS¢66†VÖ2ö†FUöW–33…ö÷35öæöæ6Æ–×2çcæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†Rõ2Ó2æöæ6Æ–×266†VÖâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢6Æ–ÒÖ&÷VæF'’&W6W'fF–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—26#ScsƒV#6SC–cfccFCvV&cƒ#6C†C3fFfS3s6cc–#S–V6Sƒ66sSC&&Fâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó30 ¤f–ÆS¢66†VÖ2ö†FUöW–33…ö÷35÷&W7VÇE÷7VÖÖ'’çcæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†R&W7VÇB×7VÖÖ'’66†VÖâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢õ2Ó25266†VÖFÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2S#FCcCs#33F3“fCss†3“&3cfCƒSSScf6fFC6c“#Sc†cV6&63Cƒ33fâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó3@ ¤f–ÆS¢66†VÖ2ö†FUöW–33…ö÷35÷fÆ–FF–öå÷&V6V—Bçcæ§6öâçF…÷&ööbçG‡F ¤6†ævR7VÖÖ'“¢FG2v÷fW&æVB&ööbf÷"F†RfÆ–FF–öâ×&V6V—B66†VÖâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7Bâ ¤&÷fVBÆâÆ–æ¶vS¢õ2Ó2fÆ–FF–öâ66†VÖFÖ—76–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&–Ö'’4„Ó#Sb—2ƒ&3v#†sc6C6SvS#3v6S“v6c“VcƒF&3&#ƒ&&v6CsfSvS#csVS†#S6â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤4e"Ó3P ¤f–ÆS¢66†VÖ2ö†FU÷&VÆV6UöGFW7FF–öâçcæ§6öæ ¤6†ævR7VÖÖ'“¢6öçfW'G2F†R&VÆV6RÖGFW7FF–öâ6öçG&7Bg&öÒG&ç6—F–öæÂ"ÔæöæFÖ—76–öâFòf–æÂW†7BÖ†VB"Óe"Ô"FÖ—76–öââ ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BÖ–æ–ÖÂ66†VÖWföÇWF–öã¢W†7B6÷W&6R&WV—&VBÂ#e%ô%ôd”äÅõ56ÂæB—VÆ–æU÷7F÷ÖçVÆÆâ ¤&÷fVBÆâÆ–æ¶vS¢W‡FW&æÂW†7BÖ†VBf–æÂGFW7FF–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢&WV—&VBf–VÆG2–æ6ÇVFR6÷W&6Uö6öÖÖ—EöW†7C×G'VVÂf–æÂFÖ—76–öâÂæBG'WF†gVÂæöæ6Æ–×2â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãbà ¤4e"Ó3` ¤f–ÆS¢FW7G2öWf–FVæ6R÷FW7EöWf–FVæ6U÷6¶VÆWFöâç– ¤6†ævR7VÖÖ'“¢W‡FVæG2Wf–FVæ6R×6¶VÆWFöâ&Vw&W76–öâ6÷fW&vRf÷"f–æÂvVæW&FVB×7FFR–çFVw&—G’â ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢FWVFRæBf–ÂÖ6Æ÷6VBâ ¤&÷fVBÆâÆ–æ¶vS¢f—†VB×ö–çBWf–FVæ6Rw&‚æBWFFW"÷væW'6†—â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢FW7G276W'B6öÖÖ—GFVBvVæW&FVB6ö×æ–öç2&F†W"F†â6–ÆVçFÇ’&W—&–ærF†VÒâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢æ÷B&VÆ–VBöâà ¤4e"Ó3p ¤f–ÆS¢FW7G2öWf–FVæ6R÷FW7Eö†FUöW–33…÷&VÆV6U÷6æ—G’ç– ¤6†ævR7VÖÖ'“¢FG2W†7Bæ–æWFVVâ×7FvRÂ6¶WBÖ×WFF–öâÂ†—7F÷&–6Âö7W'&VçBÂæBF—&V7B×&–Ö'’6÷fW&vRâ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢7G&öær6÷fW&vRöbF†R†–v†W7B×&—6²&VÆV6R–çFVw&F–öââ ¤&÷fVBÆâÆ–æ¶vS¢f–æÂ&VÆV6R×6æ—G’66WFæ6R6öæF—F–öç2â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢76W'F–öç26÷fW"ÖæFF÷'’7FvRBÂ6†V6²ÖöæÇ’7FvRRÂg&÷¦Vâ†—7F÷&–6Â÷&÷f–FW"×&—G’'—FW2ÂæBf—'7BÖf–ÇW&R&V†f–÷"â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢æ÷B&VÆ–VBöâà ¤4e"Ó3€ ¤f–ÆS¢FW7G2öWf–FVæ6R÷FW7E÷&VÆV6UöGFW7FF–öâç– ¤6†ævR7VÖÖ'“¢FW7G26ÆVâW†7B6÷W&6RÂ—6öÆFVB&VÂ×v†VVÂ–ç7FÆÆF–öâÂ&VÂ†F7FÆÂ6÷W&6R–Ö×WF&–Æ—G’ÂæBf–æÂFÖ—76–öââ ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7FÇ’&V¦V7G26†–×2Â7—7FVÒ×6—FR–æ†W&—Fæ6RÂF—'G’6÷W&6W2Â7FÆRÆöw2ÂæBÖ—76–ær6¶vRFFâ ¤&÷fVBÆâÆ–æ¶vS¢W†7BÖ†VBW‡FW&æÂGFW7FF–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢fö7W6VBFW7G2W†W&6—6Rv†VVÂ'V–ÆBö–ç7FÆÂæB6ö×&R6öç6öÆRöÖöGVÆR÷WGWG2â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢æ÷B&VÆ–VBöâà ¤4e"Ó3 ¤f–ÆS¢FW7G2öWf–FVæ6R÷FW7E÷6æ—G•÷—VÆ–æRç– ¤6†ævR7VÖÖ'“¢WFFW26†&VB—VÆ–æRW‡V7FF–öç2f÷"f–æÂFÖ—76–öâæB†—7F÷&–6ÂÖöæÇ’6VÖçF–72â ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7C²G&ç6—F–öæÂ7FvRÓBW†6WF–öç2&R&VÖ÷fVBâ ¤&÷fVBÆâÆ–æ¶vS¢7G&–7Bf–æÂvFRâ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢FW7G2&WV—&Rf–æÂ52æB&V¦V7Bæöæf–æÂ÷"6¶—VB×7FvR÷WGWBâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢æ÷B&VÆ–VBöâà ¤4e"ÓC  ¤f–ÆS¢FW7G2ö÷2÷FW7EöWf–FVæ6Uö–æFW‚ç– ¤6†ævR7VÖÖ'“¢FG2W†7B&–æF–ærÂVæ—VVæW72Â†—7F÷&–6Â6Æ76–f–6F–öâÂæBg&÷¦VâÖ'—FR6÷fW&vRFW7G2â ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BæBF—&V7FÇ’wV&G26æöæ–6ÂWFFW"&V†f–÷"â ¤&÷fVBÆâÆ–æ¶vS¢–æFW‚ôÖ—'&÷"FÖ—76–öâæB†—7F÷&–6Âö7W'&VçB6W&F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢76W'F–öç26÷fW"F—&V7Bôõ2Ó2¶W—2æBVæf÷&6RÆ–væÖVçB&WGvVVâ†—7F÷&–6Â6Æ76–f–6F–öâæBg&÷¦Vâ×&–Ö'’–çfVçF÷'’â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢æ÷B&VÆ–VBöâà ¤4e"ÓC ¤f–ÆS¢FW7G2ö÷2÷FW7Eö†FUöW–33…ö÷32ç– ¤6†ævR7VÖÖ'“¢7G&VæwF†Vç2W†7BFVâÖf–ÆR–çfVçF÷'’ÂÆVFvW"Â6æöæ–6Â¥4ôâÂ66†VÖÂ6V7&WB×6fWG’ÂæB×WFF–öâ6†V6·2â ¥&—6²76W76ÖVçC¢ÖVF—VÒ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BæB&VBÖöæÇ’v—F‚&W7V7BFòõ2â ¤&÷fVBÆâÆ–æ¶vS¢FÖ—B66WFVBõ2Ó2v—F†÷WB&W'Vææ–ær—Bâ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢FW7G2fÆ–FFR6¶WB'—FW2æB&V¦V7BÖ—76–ærÂW‡G&Â÷"×WFFVB6¶WBÖVÖ&W'2â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢æ÷B&VÆ–VBöâà ¤4e"ÓC  ¤f–ÆS¢FööÇ2ö6Æ’övVæW&FUö6Æ•ö6öæf÷&Öæ6Uö'F–f7G2ç– ¤6†ævR7VÖÖ'“¢&WV—&W2æBW†V7WFW2F†R&VÂ–ç7FÆÆVB†F7FÆVçG'’ö–çB–ç7FVBöb7&VF–ær6†–Òâ ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7B&ö÷BÖ6W6Rf—ƒ²Ö—76–ær÷"'&ö¶Vâ6¶vR–ç7FÆÆF–öâæ÷rf–Ç26Æ÷6VBâ ¤&÷fVBÆâÆ–æ¶vS¢&VÂ6¶vVB&VFW"ô4Ä’fW&–f–6F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢vVæW&F÷"&WV—&W2âW†V7WF&ÆR†F7FÆæB6ö×&W2—G2†VÇ÷fW'6–öâ&V†f–÷"v—F‚ÖöGVÆRW†V7WF–öââ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãbà ¤4e"ÓC0 ¤f–ÆS¢FööÇ2öWf–FVæ6Rö'V–ÆE÷&VÆV6UöGFW7FF–öâç– ¤6†ævR7VÖÖ'“¢'V–ÆG2v†VVÂg&öÒâW†7BG&6¶VB6÷’Â–ç7FÆÇ2—B–çFòâ—6öÆFVBfVçbÂW†V7WFW2f–æÂ6Æ÷7W&RÂæBVÖ—G2W†7BÖ†VBGFW7FF–öââ ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7BâF—'G’6÷W&6W2Â7—7FVÒ×6—FR6¶vW2Â•D„ôåD†ÂF—6ÆÆ÷vVBw&—FW2Â7FÆRWf–FVæ6RÂæBæöæf–æÂvFW2f–Â6Æ÷6VBâ ¤&÷fVBÆâÆ–æ¶vS¢W‡FW&æÂW†7BÖ†VB&VÆV6RGFW7FF–öâæB6÷W&6R–Ö×WF&–Æ—G’â ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢'F–f7B'V–ÆBÆör&V6÷&G27V66W76gVÂv†VVÂ'V–ÆBÂ6¶vVB†F7FÆÂ6Æ÷7W&Rw&—FRö6†V6²Âf—†VB×ö–çB6†V6²ÂæBf–æÂvFRâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãbà ¤4e"ÓC@ ¤f–ÆS¢FööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æRç– ¤6†ævR7VÖÖ'“¢–×ÆVÖVçG2F†RW†7Bæ–æWFVVâ×7FvRf–æÂ—VÆ–æRv—F‚G&6¶VBF—&V7B×&–Ö'’fÆ–FF–öâÂ†—7F÷&–6Â–çFVw&—G’ÂÖæFF÷'’õ2Ó2fÆ–FF–öâÂæB6†V6²ÖöæÇ’6öçfW&vVæ6Râ ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7B7FvR÷&FW"æBf–ÂÖ6Æ÷6VB&V†f–÷"â7FvR"6ææ÷B–×Ç’7W'&VçB'&–FvR7W÷'C²7FvRR6ææ÷B&W—"7FÆRWf–FVæ6Râ ¤&÷fVBÆâÆ–æ¶vS¢6÷&R"Óe"Ô"&VÆV6R—VÆ–æRâ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢ö'6W'fVBW†7B7FvW2(	3’Â„•5Dõ$”4Åô”åDTu$•E•ôô¶ÂÖæFF÷'’õ2Ó2fÆ–FF–öâÂæBf—'7BÖf–ÇW&R7F÷&V†f–÷"â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã"æB"ãRà ¤4e"ÓCP ¤f–ÆS¢FööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æUövFRç– ¤6†ævR7VÖÖ'“¢&WÆ6W2F†RG&ç6—F–öæÂ7FvRÓB7F÷v—F‚7G&–7BW†7BÖÆörf–æÂFÖ—76–öââ ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7C²—B&V¦V7G26¶—VBÂW‡G&Â7FÆRÂæöæf–æÂÂ÷"f–ÆVB÷WGWBâ ¤&÷fVBÆâÆ–æ¶vS¢f–æÂ6æöæ–6Â&VÆV6RvFRâ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢vFR&WV—&W2F†R6öÖÖ—GFVBæ–æWFVVâ×7FvR52ÆöræB7FvRÓ"†—7F÷&–6Â6VçF–æVÂâ ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãRà ¤4e"ÓC` ¤f–ÆS¢FööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç– ¤6†ævR7VÖÖ'“¢6æöæ–6ÆÇ’&–æG2F†RF—&V7B&–Ö'’÷66†VÖæBFVâõ2Ó2&–Ö&–W2÷6WfVâ66†VÖ2Âv†–ÆRæ÷&ÖÆ—¦–ær'&–FvRÂõ2ÓÂæB&÷f–FW"×&—G’Wf–FVæ6R2†—7F÷&–6ÂÖöæÇ’â ¥&—6²76W76ÖVçC¢†–v‚ ¤6öFR&Wf–Wr76W76ÖVçC¢6÷'&V7B6öÆR×w&—FW"–×ÆVÖVçFF–öââ—B&W6W'fW2õ2Ó"27W'&VçBÂ&VÖ÷fW27F—fRFö¶Vç2g&öÒ†—7F÷&–6Â&÷w2ÂæBvVæW&FW2öæR‡VÖâ&÷rÂÖ6†–æR&÷rÂæB6–&Æ–ær&ööbW"FÖ—GFVB—FVÒâ ¤&÷fVBÆâÆ–æ¶vS¢FöÖ–2Wf–FVæ6RFÖ—76–öâæB†—7F÷&–6Âö7W'&VçB6W&F–öââ ¤ÆFW"×7FFRF—fW&vVæ6S¢æöæRö'6W'fVC²"Ö†VBæBÖW&vVB&Æö'2&R–FVçF–6Ââ ¥&Wò&ööc¢ö'6W'fVB¶W—2–æ6ÇVFRW–33‚ç#g"æF—&V7EöF%÷6VÆV7F–öæÂ—G266†VÖ¶W’ÂæBÆÂW†7BW–33‚æ÷32â¦–FVçF—F–W3²vVæW&FVB–æFW‚æBÖ—'&÷"6öçfW&vRBSC‚&÷w2â ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã"Â"ãRÂæB"ã“²c"*s‚ã2à ¥fÆ–FF–öâ&W7VÇG0 ¥dÂÓ ¥W'÷6S¢W7F&Æ—6‚F†RW†7BÖW&vVBÖ6†ævRGG&–'WF–öâ&÷VæF'’â ¤6öÖÖæB÷"ÖWF†öC¢v—D‡V""ÖWFFFÇW2f—'7B×&VçB6ö×&—6öâg&öÒC#FC“SSC“3C–cc†##6#3c–cssƒc&f#“ƒ3vCvFòF#3S–&36c“V33S“Ssffs33–S““c&â ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢W†7FÇ’Cb6†ævVBf–ÆW2vW&RGG&–'WFVBFò"Â33crâ ¥v‡’—BÖGFW'3¢&WfVçG2ÆFW"÷"Vç&VÆFVB6†ævW2g&öÒ&V–ær7&VF—FVBFòF†RÖW&vVB"à ¥dÂÓ  ¥W'÷6S¢fW&–g’ÖW&vR×&W6öÇWF–öâf–FVÆ—G’æB7W'&VçBÖÖ–âÆ–6&–Æ—G’â ¤6öÖÖæB÷"ÖWF†öC¢6ö×&VBWfW'’6†ævVBf–Æ^(	—2v—B&Æö"4„B"†VBs6Ccvf3V#FS&fFcƒf3#SC&33–F3#FæBÖW&vR6öÖÖ—BF#3S–&36c“V33S“Ssffs33–S““c&²6ö×&VBÖW&vR6öÖÖ—BFò7W'&VçBÖ–æâ ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢CböbCb&Æö'2ÖF6†VC²ÖW&vR6öÖÖ—BWVÇ27W'&VçBÖ–æâ ¥v‡’—BÖGFW'3¢W†7BÖ†VB4’æBGFW7FF–öâfÆ–FFRF†R'—FW2æ÷rÖW&vVBà ¥dÂÓ0 ¥W'÷6S¢fW&–g’†÷7FVB6†V6·2v–ç7BF†R–Ö×WF&ÆR"†VBâ ¤6öÖÖæB÷"ÖWF†öC¢–ç7V7FVBv—D‡V"7F–öç2'Vâ3scSƒ“#6â ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢6WfVâöb6WfVâ¦ö'26ö×ÆWFVB7V66W76gVÆÇ“²æöæRv2VæF–ærÂ7FÆRÂ6æ6VÆÆVBÂ÷"76ö6–FVBöæÇ’v—F‚âV&Æ–W"†VBâ ¥v‡’—BÖGFW'3¢6F—6f–W2F†R&÷fVBÆî(	—2W†7BÖ†VB4’&WV—&VÖVçBà ¥dÂÓ@ ¥W'÷6S¢fW&–g’Æ–6&ÆR–×ÆVÖVçFF–öâæBWf–FVæ6RFW7G2â ¤6öÖÖæB÷"ÖWF†öC¢&Wf–WvVBF†RÖ–â4’¦ö.(	—26ö×ÆWFVB7FW÷WGWG2â ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢ÃcRWf–FVæ6Rôõ2FW7G2Â#SF—&V7B÷7Fw&U5Â6öçG&7BFW7G2ÂR÷&FW&–æröÖV6†æ–72FW7G2Â24Ä’wV&BFW7G2Â"Ö†&æW726VÆb×FW7G2ÂæBÆÂWFFW"ö÷&–VçFF–öâö†6‚öÖ—'&÷"öf–æÂÔÄb6†V6·276VBâ ¥v‡’—BÖGFW'3¢&÷f–FW2'&öBæBF&vWFVB6÷fW&vRv—F†÷WBG&VF–ær–×ÆVÖVçFF–öâfÆ–FF–öâ2f÷&ÖÂ66WFæ6Rà ¥dÂÓP ¥W'÷6S¢fW&–g’W†7BÖ†VBW‡FW&æÂ&VÆV6RGFW7FF–öââ ¤6öÖÖæB÷"ÖWF†öC¢F÷væÆöFVB'F–f7BƒSƒƒ#sCcƒ–Â6ö×&VB—G2&6†—fRF–vW7BÂæB&â6†#Sg7VÒÖ2GFW7FF–öâæ§6öâç6†#Sfâ ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢&6†—fRF–vW7BÖF6†VB6†#Sc£s#FSS“Sv3CCfFV#3S#3fFV6&S6c3S–cVFfCC–6CCc3c&&3c†F²GFW7FF–öâæ§6öã¢ô¶â ¥v‡’—BÖGFW'3¢–æFWVæFVçFÇ’fW&–f–W2'F–f7B–çFVw&—G’à ¥dÂÓ` ¥W'÷6S¢fW&–g’GFW7FVB&VÆV6R6VÖçF–72â ¤6öÖÖæB÷"ÖWF†öC¢–ç7V7FVBGFW7FF–öâæ§6öæÂ'V–ÆBæÆövÂ6¶vVBÖVçG'—ö–çB&W7VÇG2ÂæB'VæFÆVB6æ—G’Æörâ ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢6÷W&6R6öÖÖ—B—2W†7FÇ’s6Ccvf3V#FS&fFcƒf3#SC&33–F3#F²6÷W&6Uö6öÖÖ—EöW†7C×G'VV²FÖ—76–öâ—2#e%ô%ôd”äÅõ56²—VÆ–æU÷7F÷ÖçVÆÆ²&VÂv†VVÂÖ–ç7FÆÆVB†F7FÆ7V66VVFVC²ÆÂæ–æWFVVâ7FvW276VBâ ¥v‡’—BÖGFW'3¢&÷fW2F†Rf–æÂ&W7VÇB6öÖW2g&öÒâ–Ö×WF&ÆR6÷W&6R6÷’æB&VÂ6¶vVBVçG'’ö–çBà ¥dÂÓp ¥W'÷6S¢fW&–g’v÷fW&æVBWf–FVæ6RÖw&‚6ö×ÆWFVæW72æBf—†VB×ö–çB÷7GW&Râ ¤6öÖÖæB÷"ÖWF†öC¢gVÆÇ’'6VBFö72öWf–FVæ6Rô”äDU‚æ§6öæÂ'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆÂF†V—"6VçF–æVÇ2ÂæBÆÂ’æWr6–&Æ–ær&öög2â ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢–æFW‚æBÖ—'&÷"V6‚6öçF–âSC‚&÷w3²WfW'’F—&V7Bôõ2Ó2F&vWB¶W’ö67W'2W†7FÇ’öæ6S²ÆÂ&ööbF‡2ö†6†W2w&VS²#BÆVv7’&V6÷&G2&R†—7F÷&–6ÂÖöæÇ’æBFö¶VâÖg&VRâ ¥v‡’—BÖGFW'3¢6F—6f–W2FöÖ–2FÖ—76–öâÂVæ—VVæW72ÂF‚Â†6‚ÂæB†—7F÷&–6Âö7W'&VçB&WV—&VÖVçG2à ¥dÂÓ€ ¥W'÷6S¢fW&–g’66WFVBõ2Ó2&–Ö&–W2vW&Ræ÷B&Ww&—GFVâ'’F†RÖW&vVB6†ævRâ ¤6öÖÖæB÷"ÖWF†öC¢6ö×&VBF†R"6†ævVBÖf–ÆR–çfVçF÷'’v—F‚F†RW†7BFVâ&–Ö'’F‡2æBfÆ–FFVBF†R6öÖÖ—GFVB6¶WBÆVFvW"â ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢öæÇ’F†RFVâ6–&Æ–ær&öög26†ævVC²ÆVFvW"4„Ó#Sb&VÖ–ç2S#fS#VFS3ssSV#Fc#sf†C†Ccv3F&6V3c63&cs–Ff6SsƒcƒFS6&Sf&3&ÂæBV6‚ÆVFvW"VçG'’fÆ–FFW2â ¥v‡’—BÖGFW'3¢&W6W'fW266WFVB÷W&F–öæÂWf–FVæ6RW†7FÇ’2&WV—&VBà ¥6V&6‚ÖWF†öC¢6V&6†VB&Wòf÷"&VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷¶6†V6·7V×2ç6†#SbÆ6öÖÖæG2çG‡BÆF%Å÷÷7GW&UÅ÷7VÖÖ'’æ§6öâÆVçeÅ÷&W6Væ6Ræ§6öâÆW†—EÅö6öFRçG‡BÆæöæ6Æ–×2æ§6öâÇ&W7VÇEÅ÷7VÖÖ'’æ§6öâÇ7FFW'"æÆörÇ7FF÷WBæÆörÇfÆ–FF–öåÅ÷&V6V—Bæ§6öçÒ"†66S¢6Vç6—F—fR“²66÷S¢"Â33cr6†ævVBÖf–ÆR–çfVçF÷'“²FööÃ¢ÖçVÂ66ã²&W7VÇC¢†—G2à ¥dÂÓ ¥W'÷6S¢fW&–g’&Wf–WrÖf–æF–ær6Æ÷7W&Râ ¤6öÖÖæB÷"ÖWF†öC¢–ç7V7FVBÆÂ"Â33cr&Wf–WrF‡&VG2æBF†V—"f–æÂ7FFRâ ¥&W7VÇC¢52 ¤¶W’÷WGWB÷"ö'6W'fF–öã¢f—fRöbf—fRF‡&VG2&R7V'7FçF—fVÇ’FG&W76VBæBÖ&¶VB&W6öÇfVBâ ¥v‡’—BÖGFW'3¢6öæf—&×2æò7F–öæ&ÆR&Wf–Wrf–æF–ær&VÖ–ç2÷Vâà ¥dÂÓ  ¥W'÷6S¢&V6÷&B6÷W&6R×G&VR6öÖÖæB÷7GW&Rf÷"F†—2&VBÖöæÇ’&Wf–Wrâ ¤6öÖÖæB÷"ÖWF†öC¢Æö6Â×WF&ÆRÖ6†V6¶÷WB6öÖÖæBW†V7WF–öââ ¥&W7VÇC¢äõB%Tâ ¤¶W’÷WGWB÷"ö'6W'fF–öã¢F†R6öææV7FVBv—D‡V"&W÷6—F÷'’W‡÷6W26öÖÖ—GFVB7FFR&F†W"F†â×WF&ÆRW†V7WF&ÆR6†V6¶÷WBâ ¥v‡’—BÖGFW'3¢F†—2FöW2æ÷Bf÷&6R&VÖVF–F–öâ&V6W6RW†7BÖ†VBv—D‡V"4’76VBÂÆÂÖW&vVB&Æö'2ÖF6‚F†RfÆ–FFVB"†VBÂæBF†RW‡FW&æÂGFW7FF–öâv2–æFWVæFVçFÇ’F÷væÆöFVBæBfW&–f–VBà ¥$4 ¤’'Vrôf–ÇW&R7FFVÖVç@ ¥F†R&÷fVBÆâ–FVçF–f–VBF†B(	Ä7F—fRD"÷7GW&RÂ&—G’Âõ2Ó"ÂfÆ–FF÷"Â4’6†V6¶W"ÂæB&VÆV6R×6æ—G’FööÇ27F–ÆÂ&WV—&R'&–FvR6öç7G'V7F–öâ÷"'&–FvRWf–FVæ6Rî(	Ð ¤—BÇ6òf÷VæBF†B(	ÅF†R6æöæ–6ÂWFFW"æB&VÆV6R—VÆ–æR&–æBF†R†—7F÷&–6Âõ2Ó'&–FvR6¶WB27W'&VçB"Óbõ2Wf–FVæ6RæBFW&—fR7W'&VçB'&–FvR52î(	Ð ¤"’&ö÷B6W6R‡2 £â&WF—&VB'&–FvRG&ç7÷'B&VÖ–æVBVæ6öFVB27W'&VçB'VçF–ÖRæB&VÆV6RWf–FVæ6RâWf–FVæ6S¢&÷fVBÆâ%TrÓbæBc*s"ã.(	—2F—&V7BÖöæÇ’G&ç7÷'BFV6—6–öââ £"âF†RWf–FVæ6RWFFW"F–Bæ÷BF—7F–æwV—6‚&WF–æVB†—7F÷&–6Â–çFVw&—G’g&öÒ7W'&VçB7W÷'BÂ6ò'&–FvRôõ2Ó÷&÷f–FW"×&—G’&÷w26÷VÆB6''’7F—fRÖVæ–ærâWf–FVæ6S¢&÷fVBÆâ%TrÓ‚æB4U4RÓ#²4e"Ó"Â4e"Ó#"ÂæB4e"ÓCbâ £2âf–æÂ6Æ÷7W&R&WV—&VBæWrFWFW&Ö–æ—7F–2F—&V7B×6VÆV7F–öâ&–Ö'’Â66WFVBÆ—fRF—&V7B×÷7GW&RWf–FVæ6RÂæBFöÖ–2FÖ—76–öâ–çFòöæRf—†VB×ö–çBw&‚âWf–FVæ6S¢&÷fVBÆâ4U4RÓS²4e"ÓbF‡&÷Vv‚4e"ÓCRà ¤2’f—‚–âÖW&vVB6†ævP ¥"Â33crFG2æBfÆ–FFW2F†RFWFW&Ö–æ—7F–2F—&V7B×6VÆV7F–öâ&–Ö'’ÂFÖ—G2F†RW†7Bõ2Ó26¶WBæB66†VÖ2F‡&÷Vv‚F†R6æöæ–6ÂWFFW"Â6Æ76–f–W2&WF–æVB'&–FvRWf–FVæ6R2†—7F÷&–6ÂÖöæÇ’ÂÖ¶W27FvRBÖæFF÷'’ÂÖ¶W27FvRR6†V6²ÖöæÇ’ÂæB&WV—&W27G&–7Bæ–æWFVVâ×7FvRf–æÂFÖ—76–öââ—BÇ6ò'V–ÆG2æBW†W&6—6W2F†R&VÂ6¶vRVçG'’ö–çB–ââ—6öÆFVBW†7BÖ†VBGFW7FF–öâVçf—&öæÖVçBà ¤B’f—‚fW&–f–6F–öà ¥dÂÓ2F‡&÷Vv‚dÂÓ’FVÖöç7G&FRW†7BÖ†VB4’7V66W72Â&VÂ×v†VVÂ–ç7FÆÆF–öâÂ7G&–7Bæ–æWFVVâ×7FvR52Â6ö×ÆWFR–æFW‚ôÖ—'&÷"÷F‚×&ööb6öçfW&vVæ6RÂg&÷¦Vâõ2Ó2'—FW2ÂæB&W6öÇfVB&Wf–Wrf–æF–æw2âæòWf–FVæ6VB–×ÆVÖVçFF–öâ&W6–GVÂ&—6²&VÖ–ç2à ¤f–æF–æw0 ¤f–æF–ær”C¢bÓ ¥&VÆFVB&Wf–Wr—FVÓ¢4e"Óò4e"Ó#bò4e"Ó3Rò4e"ÓC"ò4e"ÓC2òdÂÓ2òdÂÓRòdÂÓb ¥6WfW&—G“¢æ÷FR ¤ö'6W'fF–öã¢W†7BÖ†VB4’æBGFW7FF–öâW6RF†R&VÂ'V–ÇBv†VVÂæB–ç7FÆÆVB†F7FÆÂv—F‚6ÆVâ×6÷W&6RæB—6öÆF–öâ&WV—&VÖVçG2â ¥v‡’—BÖGFW'3¢&WfVçG27–çF†WF–2ÖW&vR&Vg2Â6†–×2Â6÷W&6R×G&VR–×÷'G2Â÷"Ö&–VçB6¶vW2g&öÒ&öGV6–ærfÇ6R&VÆV6R&ööbâ ¤Wf–FVæ6S¢4e"ÓÂ4e"Ó#bÂ4e"Ó3RÂ4e"ÓC"Â4e"ÓC2ÂdÂÓ2ÂdÂÓRÂæBdÂÓbâ ¥&WV—&VB7F–öã¢æöæR ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãbà ¤f–æF–ær”C¢bÓ" ¥&VÆFVB&Wf–Wr—FVÓ¢4e"Ó"ò4e"Ó2ò4e"ÓBò4e"ÓRò4e"Ó#"ò4e"Ó#2ò4e"Ó#Bò4e"Ó#Rò4e"ÓCbòdÂÓr ¥6WfW&—G“¢æ÷FR ¤ö'6W'fF–öã¢‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"Â6VçF–æVÇ2ÂæB&öög2f÷&Ò6öç6—7FVçBSC‚×&÷rf—†VBö–çBv—F‚W†7BæWr&–æF–æw2æB†—7F÷&–6ÂÖöæÇ’ÆVv7’&V6÷&G2â ¥v‡’—BÖGFW'3¢&WfVçG2GWÆ–6FRÂ÷'†æVBÂ7FÆRÂ÷"7W'&VçBÖÖ—66Æ76–f–VBWf–FVæ6Râ ¤Wf–FVæ6S¢4e"Ó"F‡&÷Vv‚4e"ÓRÂ4e"Ó#"F‡&÷Vv‚4e"Ó#RÂ4e"ÓCbÂæBdÂÓrâ ¥&WV—&VB7F–öã¢æöæR ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã^(	3"ãc²c"*s‚ã2à ¤f–æF–ær”C¢bÓ2 ¥&VÆFVB&Wf–Wr—FVÓ¢4e"Óbò4e"Órò4e"Ó#ròdÂÓBòdÂÓr ¥6WfW&—G“¢æ÷FR ¤ö'6W'fF–öã¢F†RFWFW&Ö–æ—7F–2F—&V7B×6VÆV7F–öâ&–Ö'’æB66†VÖ&Rv÷fW&æVBÂ–æFW†VBÂÖ—'&÷&VBÂæBfÆ–FFVBv–ç7BF†V—"&öGV6W"â ¥v‡’—BÖGFW'3¢7WÆ–W27W'&VçBf–ÂÖ6Æ÷6VBF—&V7BÖöæÇ’6VÆV7F–öâ&ööbv—F†÷WBW‡FW&æÂ’ôò÷"&WF–æVB6V7&WG2â ¤Wf–FVæ6S¢4e"ÓbÂ4e"ÓrÂ4e"Ó#rÂdÂÓBÂæBdÂÓrâ ¥&WV—&VB7F–öã¢æöæR ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*|*s"ã"æB"ãRà ¤f–æF–ær”C¢bÓB ¥&VÆFVB&Wf–Wr—FVÓ¢4e"Ó‚ò4e"Ó’ò4e"Óò4e"Óò4e"ÓCBò4e"ÓCRòdÂÓ2òdÂÓBòdÂÓb ¥6WfW&—G“¢æ÷FR ¤ö'6W'fF–öã¢F†R&VÆV6RF‚&WV—&W2F†RW†7Bæ–æWFVVâ×7FvR52Â&W6W'fW2†—7F÷&–6ÂÖöæÇ’7FvR"Â&WV—&W2õ2Ó2B7FvRBÂæB6ææ÷B&W—"7FÆRWf–FVæ6RB7FvRUÂâ ¥v‡’—BÖGFW'3¢Ö¶W2f–æÂFÖ—76–öâ7G&–7BÂ&WVF&ÆRÂæBf–ÂÖ6Æ÷6VBâ ¤Wf–FVæ6S¢4e"Ó‚F‡&÷Vv‚4e"ÓÂ4e"ÓCBÂ4e"ÓCRÂæBdÂÓ2F‡&÷Vv‚dÂÓbâ ¥&WV—&VB7F–öã¢æöæR ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ãRà ¤f–æF–ær”C¢bÓR ¥&VÆFVB&Wf–Wr—FVÓ¢4e"Ó"ò4e"Ó2ò4e"ÓBò4e"ÓRò4e"Óbò4e"Órò4e"Ó‚ò4e"Ó’ò4e"Ó#ò4e"Ó#ò4e"Ó#‚ò4e"Ó#’ò4e"Ó3ò4e"Ó3ò4e"Ó3"ò4e"Ó32ò4e"Ó3BòdÂÓròdÂÓ‚ ¥6WfW&—G“¢æ÷FR ¤ö'6W'fF–öã¢ÆÂFVâ66WFVBõ2Ó2&–Ö&–W2æB6WfVâ66†VÖ2†fRv÷fW&æVB6–&Æ–ær&öög2v†–ÆRF†R&–Ö'’6¶WB'—FW2&VÖ–âVæ6†ævVBâ ¥v‡’—BÖGFW'3¢6ö×ÆWFW2FÖ—76–öâv—F†÷WB&W'Vææ–ærõ2÷"ÇFW&–ær66WFVB÷W&F–öæÂWf–FVæ6Râ ¤Wf–FVæ6S¢4e"Ó"F‡&÷Vv‚4e"Ó#Â4e"Ó#‚F‡&÷Vv‚4e"Ó3BÂdÂÓrÂæBdÂÓ‚â ¥&WV—&VB7F–öã¢æöæR ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢c*s"ã“²c"*s‚ã2à ¤f–æF–ær”C¢bÓb ¥&VÆFVB&Wf–Wr—FVÓ¢4e"Ó3bò4e"Ó3rò4e"Ó3‚ò4e"Ó3’ò4e"ÓCò4e"ÓCòdÂÓ2òdÂÓBòdÂÓ’ ¥6WfW&—G“¢æ÷FR ¤ö'6W'fF–öã¢fö7W6VB&Vw&W76–öâFW7G26÷fW"w&‚÷væW'6†—Â6¶WB×WFF–öç2Â†—7F÷&–6Âö7W'&VçB6W&F–öâÂW†7B7FvR&V†f–÷"Â—6öÆFVB6¶vR–ç7FÆÆF–öâÂæB7FÆRÖWf–FVæ6R&VgW6Ââ ¥v‡’—BÖGFW'3¢F—&V7FÇ’&÷FV7G2F†Rf–ÇW&RÖöFW2f÷VæBGW&–ær"&Wf–WræB&÷fVB&W66÷–ærâ ¤Wf–FVæ6S¢4e"Ó3bF‡&÷Vv‚4e"ÓCÂdÂÓ2ÂdÂÓBÂæBdÂÓ’â ¥&WV—&VB7F–öã¢æöæR ¥b&VfW&Væ6RÂ–b&VÆ–VBöã¢æ÷B&VÆ–VBöâà ¥c’–×7Bb7FGW2÷7GW&P ¥c’Fö7VÖVçC¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ ¥c’F6²”C¢„DRÔD•5C ¥c’7V'F6²”B‡2“¢„DRÔD•5CãB ¤7W'&VçBc’7FGW3¢'F–Â ¥7FGW2&V6öÖÖVæFF–öã¢6†ævRFòFöæR ¥v‡’F†—27FGW2÷7GW&R—27W÷'FVC¢F—&V7B×6VÆV7F–öâ52Â66WFVBÆ—fRõ2Ó2÷7GW&RÂW†7B&öÆR÷6V&6‚×F‚ôDDÂö6öç7G&–çBö&÷VæF'’÷'F—F–öâ&VF–6FW2Â6V7&WB6fWG’ÂæB6ö×ÆWFRv÷fW&æVBFÖ—76–öâæ÷r6öW†—7BBF†RÖW&vVB7FFRâ ¤Wf–FVæ6Rö–çFW"‡2“¢4e"Ón(	44e"Ó3C²dÂÓ>(	5dÂÓƒ²f–æF–ærbÓ2æBbÓRâ ¥b&ööbW†6W'B‡2’Âv†Vâ&VÆ–VBöã¢c’ãb&V6÷&G2(	Å7V'F6²7FGW3¢'F–Âî(	Òc*s"ãR7FFW3¢(	Æ„DRÔD•5CãF¢'F–ÆFòFöæVî(	Ð ¥c’Fö7VÖVçC¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ ¥c’F6²”C¢„DRÔD•5C ¥c’7V'F6²”B‡2“¢„DRÔD•5Cãb ¤7W'&VçBc’7FGW3¢'F–Â ¥7FGW2&V6öÖÖVæFF–öã¢6†ævRFòFöæR ¥v‡’F†—27FGW2÷7GW&R—27W÷'FVC¢F†RW†7Bæ–æWFVVâÖæFF÷'’7FvW2'Vâ–â÷&FW"v—F‚W‡V7FVB7V66W72&W7VÇG2Âæò6¶—2Â†—7F÷&–6Âö7W'&VçB6W&F–öâÂ6Æ÷6VB&–Ç2Â6æöæ–6Âw&‚6†V6·2ÂæBf–æÂ52â ¤Wf–FVæ6Rö–çFW"‡2“¢4e"ÓŽ(	44e"ÓÂ4e"Ó3rÂ4e"Ó3’Â4e"ÓCN(	44e"ÓCS²dÂÓ2ÂdÂÓBÂæBdÂÓbâ ¥b&ööbW†6W'B‡2’Âv†Vâ&VÆ–VBöã¢c’ãb&V6÷&G2(	Å7V'F6²7FGW3¢'F–Âî(	Òc*s"ãR7FFW3¢(	Æ„DRÔD•5Cãf¢'F–ÆFòFöæVî(	Ð ¥c’Fö7VÖVçC¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ ¥c’F6²”C¢„DRÔD•5C ¥c’7V'F6²”B‡2“¢„DRÔD•5Cã’ ¤7W'&VçBc’7FGW3¢'F–Â ¥7FGW2&V6öÖÖVæFF–öã¢6†ævRFòFöæR ¥v‡’F†—27FGW2÷7GW&R—27W÷'FVC¢VæFW"c(	—2ÖVæFVBF—&V7BÖ6öææV7F—f—G’ÖVæ–ærÂ†VÇF‡’6VÆV7F–öâW6W2F—&V7B7–6÷vÂÖ—76–ær÷Væf–Æ&ÆR66W72æBWfW'’&WF—&VB¶W’f–Â6Æ÷6VB&Vf÷&R&÷f–FW"’ôòÂÇFW&æFRGFV×G2&R¦W&òÂõ2Ó27WÆ–W27W'&VçB&VBÖöæÇ’÷7GW&RÂæB'&–FvRWf–FVæ6R—2†—7F÷&–6ÂÖöæÇ’â ¤Wf–FVæ6Rö–çFW"‡2“¢4e"ÓbÂ4e"ÓN(	44e"Ó‚Â4e"Ó3rÂ4e"ÓCÂ4e"ÓCBÂ4e"ÓCc²dÂÓBÂdÂÓbÂæBdÂÓrâ ¥b&ööbW†6W'B‡2’Âv†Vâ&VÆ–VBöã¢c’ãb7W'&VçFÇ’F—FÆW2F†R&÷r(	ÄD.(	6'&–FvR&—G’bVçb6öææV7F—f—Gž(	ÒæB&V6÷&G2(	Å'F–Âî(	Òc*s"ãR7FFW3¢(	Æ„DRÔD•5Cã–¢'F–ÆFòFöæVVæFW"F†RÖVæFVBF—FÆRî(	Ð ¥c’Fö7VÖVçC¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ ¥c’F6²”C¢„DRÔD•5C ¥c’7V'F6²”B‡2“¢„DRÔD•5Cã ¤7W'&VçBc’7FGW3¢÷F–öæÂ ¥7FGW2&V6öÖÖVæFF–öã¢6†ævRFòFöæR ¥v‡’F†—27FGW2÷7GW&R—27W÷'FVC¢7W'&VçBÖVBÖ66†RæBõ2Ó"fÆ–FF÷'273²w&—FR÷&VBÖ&6²&—G’Â–FV×÷FVæ6RÂ6Æ÷6VB×&–Ç2&VgW6ÂÂæò&r×fVæF÷"W'6—7FVæ6RÂ6V7&WB6fWG’ÂæB6ö×ÆWFR7W'&VçB&–æF–æw2&VÖ–â&÷fVââ ¤Wf–FVæ6Rö–çFW"‡2“¢4e"Ó‚Â4e"Ó#"Â4e"Ó3rÂ4e"ÓCÂ4e"ÓCN(	44e"ÓCc²dÂÓ2ÂdÂÓBÂæBdÂÓrâ ¥b&ööbW†6W'B‡2’Âv†Vâ&VÆ–VBöã¢c’ãb&V6÷&G2(	Å7V'F6²7FGW3¢÷F–öæÂî(	Òc*s"ãR7FFW3¢(	Æ„DRÔD•5Cã¢÷F–öæÆFòFöæVî(	Ð ¥c’Fö7VÖVçC¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ ¥c’F6²”C¢„DRÔD•5CR ¥c’7V'F6²”B‡2“¢„DRÔD•5CRã" ¤7W'&VçBc’7FGW3¢'F–Â ¥7FGW2&V6öÖÖVæFF–öã¢6†ævRFòFöæR ¥v‡’F†—27FGW2÷7GW&R—27W÷'FVC¢WfW'’æWr&–Ö'’æB66†VÖ†2W†7FÇ’öæR‡VÖâ&÷rÂöæRÖ6†–æR&÷rÂÖF6†–ær6–&Æ–ær&ööbÂæBfÆ–B†6‚Æ–æ¶vS²†—7F÷&–6Â'—FW2&VÖ–âg&÷¦Vã²F‚Â66†VÖÂF÷öÆöw’Â†6‚ÂæBf–æÂÔÄb6†V6·272â ¤Wf–FVæ6Rö–çFW"‡2“¢4e"Ó.(	44e"ÓRÂ4e"ÓrÂ4e"Óž(	44e"Ó3BÂ4e"ÓCÂ4e"ÓCc²dÂÓBÂdÂÓrÂæBdÂÓ‚â ¥b&ööbW†6W'B‡2’Âv†Vâ&VÆ–VBöã¢c’ãb&V6÷&G2(	Å7V'F6²7FGW3¢'F–Âî(	Òc*s"ãR7FFW3¢(	Æ„DRÔD•5CRã&¢'F–ÆFòFöæVî(	Ð ¤Wf–FVæ6R&–ç@ ¤’Fö¶Vç26F—6f–V@ ¤æòFö¶Vâ6F—6f7F–öâ6Æ–Ò&Wf–WvVBà ¤"’Wf–FVæ6R'F–f7G2&öGV6VB÷"WFFV@ ¥Fƒ¢'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæ ¥G—S¢v÷fW&æVBFWFW&Ö–æ—7F–2F—&V7B×6VÆV7F–öâ&–Ö'’ ¤¶W’&ööbf7G2ö'6W'fVC¢W†7Bf÷W"÷&FW&VB66W2Â6—‚G'VR&VF–6FW2Â&W7VÇCÕ56Âf–ÇW&SÖçVÆÆÂ6æöæ–6ÂöæRÔÄb'—FW2Â–æFW†VBæBÖ—'&÷&VBöæ6Râ §6†#SbÂ–bö'6W'fVC¢Cƒ†6fc&fcFc“cSvcss“sC##cFfcƒ36F3C6&#s&3&CS3&fC#3“cc–& ¤–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb÷7GW&RÂ–b&VÆWfçC¢¶W’W–33‚ç#g"æF—&V7EöF%÷6VÆV7F–öæ²ÖF6†–ær‡VÖâ&÷rÂÖ6†–æR&÷rÂæB6–&Æ–ær&ööbà ¥Fƒ¢VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2ö ¥G—S¢v÷fW&æVBFVâ×&–Ö'’66WFVB÷W&F–öæÂWf–FVæ6R6¶WB ¤¶W’&ööbf7G2ö'6W'fVC¢W†7BFVâÖf–ÆR–çfVçF÷'’Â–çFW&æÆÇ’fÆ–BÆVFvW"Â527VÖÖ'’ÂW†—B6öFRÂV×G’7FFW'"ÂfÆ–FF–öâ&V6V—BÂ6V7&WB×6fRFFÂVæ6†ævVB&–Ö&–W2â §6†#SbÂ–bö'6W'fVC¢6¶WBÆVFvW"4„Ó#SbS#fS#VFS3ssSV#Fc#sf†C†Ccv3F&6V3c63&cs–Ff6SsƒcƒFS6&Sf&3& ¤–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb÷7GW&RÂ–b&VÆWfçC¢FVâVæ—VR‡VÖâ&÷w2ÂÖ6†–æR&÷w2ÂæBÖF6†–ær6–&Æ–ær&öög2à ¥Fƒ¢66†VÖ2ö†FUöW–33…öF—&V7EöF%÷6VÆV7F–öâçcæ§6öææB66†VÖ2ö†FUöW–33…ö÷35ò¢çcæ§6öæ ¥G—S¢v÷fW&æVBF—&V7B×6VÆV7F–öâæBõ2Ó266†VÖfÖ–Ç’ ¤¶W’&ööbf7G2ö'6W'fVC¢öæRF—&V7B66†VÖÇW2F†RW†7B6WfVâõ2Ó266†VÖ2Â&W6W'fVBæBFÖ—GFVBâ §6†#SbÂ–bö'6W'fVC¢F—&V7B66†VÖFS#Cvc†VSsSVsCF#&#3Vf#ƒ3CSS“SVSS“v#F6#3FSF3ƒ3#V²–æF—f–GVÂõ2×66†VÖ†6†W2&R&÷VæB–âF†V—"6–&Æ–ær&öög2â ¤–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb÷7GW&RÂ–b&VÆWfçC¢V–v‡BVæ—VR‡VÖâ&÷w2ÂÖ6†–æR&÷w2ÂæB6–&Æ–ær&öög2à ¥Fƒ¢Fö72öWf–FVæ6Rô”äDU‚æ§6öæÂFö72öWf–FVæ6Rô”äDU‚ç6†#SfÂæB6–&Æ–ær&öög2 ¥G—S¢‡VÖâWf–FVæ6R–æFW‚æB–çFVw&—G’6ö×æ–öç2 ¤¶W’&ööbf7G2ö'6W'fVC¢SC‚&÷w2ÂÆÂ’æWr–FVçF—F–W2W†7FÇ’öæ6RÂæB†—7F÷&–6Â'&–FvR÷&÷f–FW"×&—G’&÷w26Æ76–f–VBv—F†÷WB7F—fRFö¶Vç2â §6†#SbÂ–bö'6W'fVC¢–FCCSƒƒ“SƒƒsfS3CsC#C&Scv6CscSs3&#sS66ƒ6fVfF&S ¤–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb÷7GW&RÂ–b&VÆWfçC¢f—†VB×ö–çB&—G’v—F‚F†RSC‚×&÷rÖ6†–æRÖ—'&÷"à ¥Fƒ¢'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆÂ'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÂç6†#SfÂæB6–&Æ–ær&öög2 ¥G—S¢Ö6†–æRÖ—'&÷"æB–çFVw&—G’6ö×æ–öç2 ¤¶W’&ööbf7G2ö'6W'fVC¢SC‚6æöæ–6Â¥4ôäÂ&V6÷&G2æB6ö×ÆWFRF—&V7Bôõ2Ó2ö†—7F÷&–6Â6Æ76–f–6F–öâ&—G’â §6†#SbÂ–bö'6W'fVC¢vC#“V#csf&VS“†&cƒsƒƒ3VFf&f33S†VV6SCCc“sSc–##v&c&CF3“V6 ¤–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb÷7GW&RÂ–b&VÆWfçC¢Ö—'&÷"&öG’†6‚—2366F#3S#&CCcs3s“FCƒf3““ccC–CFSSs†#“3v&fFcccCFC–6Vc66f²F‚&öög2fÆ–FFRà ¥Fƒ¢VF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆöv ¥G—S¢f–æÂ&VÆV6R×6æ—G’vFRWf–FVæ6R ¤¶W’&ööbf7G2ö'6W'fVC¢W†7Bæ–æWFVVâ7FvW2Â7FvR"„•5Dõ$”4Åô”åDTu$•E•ôô¶Âæòf–ÆVB7FvRÂæB7VÖÖ'“¥56â §6†#SbÂ–bö'6W'fVC¢–6#†&&3CC–f“–VSƒsv&ScƒƒCCƒ“#&#Cƒ3–S#v#3FC#Cs&Scƒ†#C& ¤–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb÷7GW&RÂ–b&VÆWfçC¢v÷fW&æVBÂ–æFW†VBÂÖ—'&÷&VBÂæBÖF6†VB'’—G26–&Æ–ær&ööbà ¥Fƒ¢VF—BövFW2÷F÷öÆöw’ö÷&–VçFF–öåöFVÖòçG‡F ¥G—S¢Wf–FVæ6R×F÷öÆöw’fÆ–FF–öâ'F–f7B ¤¶W’&ööbf7G2ö'6W'fVC¢F÷FÅö'F–f7G3¢SC†æB7FGW3¢ö¶â §6†#SbÂ–bö'6W'fVC¢cS6f66VVCCCc66V#fcc36fV#&SvCvV#6VS–cS“S“cCF&SƒCv6F6 ¤–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb÷7GW&RÂ–b&VÆWfçC¢v÷fW&æVBæBÖF6†VB'’—G26–&Æ–ær&ööbà ¥Fƒ¢v—D‡V"7F–öç2'F–f7B†FR×&VÆV6RÖGFW7FF–öâÓs6Ccvf3V#FS&fFcƒf3#SC&33–F3#F ¥G—S¢W‡FW&æÂW†7BÖ†VB&VÆV6RGFW7FF–öâ ¤¶W’&ööbf7G2ö'6W'fVC¢W†7B6÷W&6R6öÖÖ—BÂ6ÆVâ6÷W&6RÂFWFW&Ö–æ—7F–2G&6¶VB×G&VRF–vW7BÂ&VÂ—6öÆFVBv†VVÂÖ–ç7FÆÆVB†F7FÆÂf–æÂFÖ—76–öâÂæò—VÆ–æR7F÷ÂæBG'WF†gVÂæöæ6Æ–×2â §6†#SbÂ–bö'6W'fVC¢s#FSS“Sv3CCfFV#3S#3fFV6&S6c3S–cVFfCC–6CCc3c&&3c†F ¤–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb÷7GW&RÂ–b&VÆWfçC¢W‡FW&æÂ'F–f7C²æ÷B6†V6¶VB–çFòF†Rv÷fW&æVB&Wòw&‚à ¤2’fÆ–FF–öâ&öö` ¤6öÖÖæB÷"ÖWF†öC¢v—D‡V"7F–öç2'Vâ3scSƒ“#6 ¥&W7VÇC¢6WfVâöb6WfVâ¦ö'27V66VVFVBBW†7B"†VBs6Ccvf3V#FS&fFcƒf3#SC&33–F3#Fâ ¥v†W&RF†R&W7VÇBV'3¢"Â33cr6†V6·2æB7F–öç2'VâÖWFFFâ ¥v‡’—B—27Vff–6–VçC¢—B6÷fW'2F†R6ö×ÆWFR&W÷6—F÷'’4’ÖG&—‚öâF†R–Ö×WF&ÆR†VBv†÷6R6†ævVBÖf–ÆR&Æö'2ÖF6‚F†RÖW&vR6öÖÖ—Bà ¤6öÖÖæB÷"ÖWF†öC¢Ö–â4’Wf–FVæ6Rôõ2æBF—&V7BÖ6öçG&7B7V—FW2 ¥&W7VÇC¢ÃcRWf–FVæ6Rôõ2FW7G2æB#SF—&V7B÷7Fw&U5Â6öçG&7BFW7G276VBâ ¥v†W&RF†R&W7VÇBV'3¢Ö–âFW7B¦ö"–â'Vâ3scSƒ“#6â ¥v‡’—B—27Vff–6–VçC¢—BF—&V7FÇ’W†W&6—6W2F†R6†ævVBFÖ—76–öâÂ—VÆ–æRÂ6¶WBÂ6¶v–ærÂæBw&‚&V†f–÷"à ¤6öÖÖæB÷"ÖWF†öC¢6æöæ–6ÂWFFW"ö÷&–VçFF–öâö†6‚öÖ—'&÷"öf–æÂÔÄb4’6†V6·2 ¥&W7VÇC¢ÆÂ76VBv—F†÷WBÖöF–g––ærF†R6öÖÖ—GFVB6†V6¶÷WBâ ¥v†W&RF†R&W7VÇBV'3¢Ö–âFW7B¦ö"&VfÆ–v‡BæBWf–FVæ6R6†V6·2â ¥v‡’—B—27Vff–6–VçC¢7FvRRæB4’÷W&FR–â6†V6²ÖöFRÂ6òw&VVâ&W7VÇG2&÷fR6öÖÖ—GFVBf—†VB×ö–çB'—FW2&F†W"F†â&W—&VBG&ç6–VçB÷WGWBà ¤6öÖÖæB÷"ÖWF†öC¢6†#Sg7VÒÖ2GFW7FF–öâæ§6öâç6†#SfÇW2'F–f7BF–vW7B6ö×&—6öâ ¥&W7VÇC¢GFW7FF–öâæ§6öã¢ô¶²&6†—fRF–vW7BÖF6†VBv—D‡V"ÖWFFFâ ¥v†W&RF†R&W7VÇBV'3¢F÷væÆöFVBW‡FW&æÂ'F–f7BƒSƒƒ#sCcƒ–â ¥v‡’—B—27Vff–6–VçC¢fW&–f–W2–æFWVæFVçB'F–f7BæBGFW7FF–öâ–çFVw&—G’à ¤6öÖÖæB÷"ÖWF†öC¢–ç7V7F–öâöbGFW7FF–öâæ§6öæÂ'V–ÆBæÆövÂ–ç7FÆÆ&–Æ—G•÷7VÖÖ'’æ§6öæÂæB'VæFÆVB6æ—G•÷—VÆ–æRæÆöv ¥&W7VÇC¢W†7B†VBÂ—6öÆFVB&VÂ×v†VVÂ†F7FÆÂ#e%ô%ôd”äÅõ56ÂÆÂæ–æWFVVâ7FvW252ÂæB—VÆ–æU÷7F÷ÖçVÆÆâ ¥v†W&RF†R&W7VÇBV'3¢W‡FW&æÂ'F–f7BƒSƒƒ#sCcƒ–â ¥v‡’—B—27Vff–6–VçC¢fW&–f–W2F†Rf–æÂ&VÆV6R6Æ–ÒæB6¶vRÖ–ç7FÆÆ&–Æ—G’F‚&F†W"F†âöæÇ’&VÇ––æröâw&VVâ¦ö"Æ&VÂà ¤6öÖÖæB÷"ÖWF†öC¢6ö×ÆWFR–æFW‚ôÖ—'&÷"æB’×&ööb–ç7V7F–öâ ¥&W7VÇC¢SC‚óSC‚&÷r&—G“²W†7BöæR×W"×F&vWBFÖ—76–öã²ÖF6†–ærF‡2Â6—¦W2Â†6†W2ÂæB÷'F&ÆRF–ÖW7F×2â ¥v†W&RF†R&W7VÇBV'3¢Fö72öWf–FVæ6Rô”äDU‚æ§6öæÂ'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆÂ6VçF–æVÇ2ÂæB6–&Æ–ær&öög2â ¥v‡’—B—27Vff–6–VçC¢W7F&Æ—6†W2F†R6öÖÖ—GFVBWf–FVæ6Rw&Ž(	—26ö×ÆWFVæW72æB6öç6—7FVæ7’à ¤Fö2FVÇF6æF–FFW0 ¤DD2Ó ¤Fö3¢cr(	BvÆ÷r–æg&7G'V7GW&R ¥6V7F–öã¢*|*sBãÂBã"ÂrãÂrãÂ‚ãÂæB’ã" ¤6æöâ&6—3¢4äôâÔ•4ÔD4‚ ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5C ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CãBÂ„DRÔD•5Cã’ ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢&VÖ÷fR7F—fRrÖ'&–FvVÂD%ô%$”DtUõU$ÆÂ'&–FvRÖ†÷7BÂæB'&–FvRÖfÆÆ&6²&6†—FV7GW&S²&V6÷&BF—&V7B÷7Fw&U5Â2F†R6öÆR7F—fRG&ç7÷'BæB'&–FvRÖFW&–Â2†—7F÷&–6Ââ ¥v‡“¢F†RÖW&vVB–×ÆVÖVçFF–öâæB6öçG&öÆÆ–ærcFV6—6–öâ&RF—&V7BÖöæÇ’â ¥&WòWf–FVæ6S¢4e"ÓbÂ4e"ÓN(	44e"Ó‚Â4e"ÓCBÂæB4e"ÓCbâ ¤6æöâ&ööbW†6W'C¢cr6—2Â(	Ç6VÆV7B'’f–Æ&–Æ—G’v—F‚fÆÆ&6³¢DD$4UÅõU$Â(i"D%Åô%$”DtUÅõU$Â†‡GG2’(i"G—VBW'&÷"î(	Òc*s"ã"Ö¶W2F—&V7B÷7Fw&U5ÂF†R6öÆR7F—fRG&ç7÷'Bà ¤DD2Ó  ¤Fö3¢cB(	B„DRÖV6†æ–72wV–FR ¥6V7F–öã¢*|*s#ã2æB#ã2ã ¤6æöâ&6—3¢4äôâÔ•4ÔD4‚ ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5C ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CãBÂ„DRÔD•5Cã’ ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢&WÆ6R7W'&VçB'&–FvR×&—G’Â'&–FvU&÷f–FW&ÂæB'&–FvRÖfÆÆ&6²ÖV6†æ–72v—F‚F—&V7BÖöæÇ’6VÆV7F–öâæB†—7F÷&–6ÂÖ–çFVw&—G’6VÖçF–72â ¥v‡“¢"Óe"Ô"&÷fW2F—&V7BÖöæÇ’&V†f–÷"æBW‡Æ–6—FÇ’&V¦V7G27W'&VçB'&–FvRf–Æ&–Æ—G’÷&—G’6Æ–×2â ¥&WòWf–FVæ6S¢4e"ÓbÂ4e"Ó3rÂ4e"ÓCÂ4e"ÓCBÂæB4e"ÓCbâ ¤6æöâ&ööbW†6W'C¢cB6—2F†R&—G’fÖ–Ç’(	ÄÕU5B&W6W'fRD$66W722F†R&÷f–FW"Övæ÷7F–2f:vFRî(	Òc*s"ã"&WF—&W2F†B7W'&VçB'&–FvRÖVæ–ærà ¤DD2Ó0 ¤Fö3¢cB(	B„DRv÷fW&ææ6R ¥6V7F–öã¢*s"ãÂ*s"ãã’ÂæB*sbã2ã" ¤6æöâ&6—3¢4äôâÔ•4ÔD4‚ ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5C ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CãBÂ„DRÔD•5Cã’ ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢&WF—&RDUeôD%ô%$”DtUôdÄÄ$4µôô¶æBF†R76ö6–FVB7F—fRFWbÖfÆÆ&6²6VÖçF–72â&W6W'fRF†R&ö†–&—F–öâöâ–æfW'&–æræWr66WFæ6RFö¶Vç2g&öÒõ2÷"Wf–FVæ6Râ ¥v‡“¢F†RÖW&vVBF—&V7BÖöæÇ’'VçF–ÖR&VgW6W2&WF—&VB¶W—2&Vf÷&R&÷f–FW"6öç7G'V7F–öâ÷"’ôòâ ¥&WòWf–FVæ6S¢4e"ÓbÂ4e"Ó3rÂ4e"ÓCBÂæB4e"ÓCbâ ¤6æöâ&ööbW†6W'C¢cB6—2Â(	ÄDUeÅôD%Åô%$”DtUÅôdÄÄ$4µÅôô²&VÖ–ç2F†R6æöæ–6Â'&–FvRÖfÆÆ&6²66WFæ6RFö¶Vâî(	Òc*s"ã"&WV—&W2'&–FvR×Fö¶Vâ&WF—&VÖVçBà ¤DD2Ó@ ¤Fö3¢c"(	B„DR66†VÖ2æB'F–f7G2 ¥6V7F–öã¢*s‚ã2 ¤6æöâ&6—3¢4äôâÔ•4ÔD4‚ ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5CR ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CRã" ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢&VÖ÷fR6ÆöæRÖÆö6Âf–ÆW7—7FVÒÖ×F–ÖR6ö×&—6öâg&öÒ÷'F&ÆR6–&Æ–ær×&ööbfÆ–FF–öã²&WF–âv÷fW&æVBF‚Â4„Ó#SbÂ6—¦RÂ6æöæ–6Âf–VÆG2Â6ö×æ–öâÆ–æ¶vRÂæBUD2F–ÖW7F××6†R6†V6·2â ¥v‡“¢6ÆöæRÖÆö6Â7FB‚’ç7Eö×F–ÖV—2æ÷B÷'F&ÆRWf–FVæ6RæB—2W‡&W76Ç’7WW'6VFVB'’c*s"ãbâ ¥&WòWf–FVæ6S¢4e"Ó2Â4e"ÓRÂ4e"ÓrÂ4e"Ó’Â4e"Ó(	44e"Ó3Bâ ¤6æöâ&ööbW†6W'C¢c"&WV—&W2'6VEö×F–ÖRÃÒ7W'&VçEög5ö×F–ÖV²c*s"ãb7FFW2Â(	Ä6ÆöæRÖÆö6Â7FB‚’ç7EÅö×F–ÖR—2F†W&Vf÷&Ræ÷BWf–FVæ6Rî(	Ð ¤DD2ÓP ¤Fö3¢c"(	B„DR66†VÖ2æB'F–f7G2 ¥6V7F–öã¢Æ6VÖVçBæ÷BW7F&Æ—6†VC²6æöâÖWF†÷"&÷WF–ær&WV—&VB ¤6æöâ&6—3¢4äôâ4”ÄTä4R ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5CÂ„DRÔD•5CR ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CãBÂ„DRÔD•5CãbÂ„DRÔD•5Cã’Â„DRÔD•5CRã" ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢FBF†Rv÷fW&æVBF—&V7B×6VÆV7F–öâÂõ2Ó2Âf–æÂ&VÆV6RÖGFW7FF–öâÂæB†—7F÷&–6Åö'&–FvUöWf–FVæ6V&V6÷&BfÖ–Æ–W2Â¶W—2Â66†VÖ2ÂF‡2ÂæBWFFW"÷væW'6†—â ¥v‡“¢F†W6RfÖ–Æ–W2æ÷rW†—7B–âF†R&Wò'WB&Ræ÷BW&ÖæVçFÇ’FW67&–&VB–âc"â ¥&WòWf–FVæ6S¢4e"Ó.(	44e"ÓrÂ4e"Ó.(	44e"Ó3RÂæB4e"ÓCbà ¥6V&6‚ÖWF†öC¢6V&6†VB&Wòf÷"&†FUÅöW–33‚æ÷37Æ†FUÅöW–33…Åö÷37Æ†FRç&VÆV6UÅöGFW7FF–öâçcÆ†—7F÷&–6ÅÅö'&–FvUÅöWf–FVæ6WÆ†FRÖW–33‚ö÷2Ó2"†66S¢6Vç6—F—fR“²66÷S¢6ö×ÆWFRc"Fö7VÖVçC²FööÃ¢&s²&W7VÇC¢†—G2à ¤DD2Ó` ¤Fö3¢c’(	BvÆ÷rwV–FR ¥6V7F–öã¢*sBã2ã ¤6æöâ&6—3¢4äôâÔ•4ÔD4‚ ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5CR ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CRã" ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢&WÆ6R6ÆöæRÖÆö6ÂÖöæ÷FöæRÖ×F–ÖR&ööbfÆ–FF–öâv—F‚÷'F&ÆRF‚ö†6‚÷6—¦R÷7G'V7GW&R÷F–ÖW7F××6†RfÆ–FF–öââ ¥v‡“¢F†RÖW&vVBF‚×&ööb6öçG&7BæBc*s"ãb&V¦V7B6ÆöæRÖÆö6Â×F–ÖR2÷'F&ÆRWf–FVæ6Râ ¥&WòWf–FVæ6S¢4e"Ó2Â4e"ÓRÂ4e"ÓrÂ4e"Ó’Â4e"Ó(	44e"Ó3Bâ ¤6æöâ&ööbW†6W'C¢c’&WV—&W2×F–ÖU÷WF2ÃÒ7W'&VçEög5ö×F–ÖV²c*s"ãb7FFW2F†B6ÆöæRÖÆö6Âf–ÆW7—7FVÒ×F–ÖR—2æ÷BWf–FVæ6Rà ¤DD2Óp ¤Fö3¢c’(	BvÆ÷rwV–FR ¥6V7F–öã¢Æ6VÖVçBæ÷BW7F&Æ—6†VC²6æöâÖWF†÷"&÷WF–ær&WV—&VB ¤6æöâ&6—3¢4äôâ4”ÄTä4R ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5C ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5Cãb ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢Fö7VÖVçBW†7BÖ†VBW‡FW&æÂ&VÆV6RGFW7FF–öâÂ6÷W&6R×G&VR–Ö×WF&–Æ—G’Â—6öÆFVB&VÂ×v†VVÂ6öç6öÆRÖVçG'—ö–çBfW&–f–6F–öâÂæBF†R'VÆRF†B4’×W7BFWFV7B&F†W"F†â&W—"7FÆR6öÖÖ—GFVBWf–FVæ6Râ ¥v‡“¢F†W6R&Ræ÷rÖFW&–Â&VÆV6R×fW&–f–6F–öâÖV6†æ–72'6VçBg&öÒc’â ¥&WòWf–FVæ6S¢4e"ÓÂ4e"Ó#bÂ4e"Ó3RÂ4e"Ó3‚Â4e"ÓC"ÂæB4e"ÓC2à ¥6V&6‚ÖWF†öC¢6V&6†VB&Wòf÷"'&VÆV6RGFW7FF–öçÆW†7BÖ†VGÆ6öç6öÆRVçG'—ö–çGÇ6¶vVB†F7FÂ"†66S¢–ç6Vç6—F—fR“²66÷S¢6ö×ÆWFRc’Fö7VÖVçC²FööÃ¢&s²&W7VÇC¢†—G2à ¤DD2Ó€ ¤Fö3¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ ¥6V7F–öã¢7V'F6·2„DRÔD•5CãBæB„DRÔD•5Cã’ ¤6æöâ&6—3¢4äôâÔ•4ÔD4‚ ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5C ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CãBÂ„DRÔD•5Cã’ ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢&WÆ6R'&–FvRfÆÆ&6²÷&—G’ÆæwVvRv—F‚F—&V7BFF&6R6öææV7F—f—G’Â&WF—&VB×G&ç7÷'BVæf÷&6VÖVçBÂ7W'&VçBF—&V7B×÷7GW&RWf–FVæ6RÂæB†—7F÷&–6ÂÖöæÇ’'&–FvR–çFVw&—G’â ¥v‡“¢c’7F–ÆÂFW67&–&W2'&–FvRfÆÆ&6²æB'&–FvR&—G’WfVâF†÷Vv‚cæBF†RÖW&vVB–×ÆVÖVçFF–öâ&WF—&RF†÷6R7W'&VçBö&Æ–vF–öç2â ¥&WòWf–FVæ6S¢4e"ÓbÂ4e"ÓN(	44e"Ó‚Â4e"Ó3rÂ4e"ÓCÂ4e"ÓCBÂæB4e"ÓCbâ ¤6æöâ&ööbW†6W'C¢c’ãbF—FÆW2ã–(	ÄD.(	6'&–FvR&—G’bVçb6öææV7F—f—G’î(	Òc*s"ãR&WV—&W2F†RÖVæFVBF—&V7BÖ6öææV7F—f—G’ÖVæ–ærà ¤DD2Ó ¤Fö3¢c’ãb(	B6æöâ„DR'V–ÆB6†V6¶Æ—7BF—7F–ÆÆF–öâ ¥6V7F–öã¢7V'F6·2„DRÔD•5CãBÂ„DRÔD•5CãbÂ„DRÔD•5Cã’Â„DRÔD•5CãÂæB„DRÔD•5CRã" ¤6æöâ&6—3¢c’5DEU25Uõ%B ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5CÂ„DRÔD•5CR ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CãBÂ„DRÔD•5CãbÂ„DRÔD•5Cã’Â„DRÔD•5CãÂ„DRÔD•5CRã" ¥c’7FGW27F–öã¢6†ævRFòFöæR ¤FVÇF¢–â6W&FR‡VÖâc’Ö–çFVææ6R7F–öâÂÖ÷fRF†Rf—fRW†7B7V'F6·2FòFöæRgFW"Ç––ærF†Rã–6VÖçF–2÷F—FÆRÖVæFÖVçBâ ¥v‡“¢F†RÖW&vVBW†7BÖ†VBWf–FVæ6R6F—6f–W2c*s"ã^(	—2ÆFW"×7FGW2&VF–6FW2f÷"ÆÂf—fR&÷w2â ¥&WòWf–FVæ6S¢dÂÓ>(	5dÂÓƒ²f–æF–æw2bÓ"F‡&÷Vv‚bÓc²F†Rf—fRc’÷7GW&R—FV×2&÷fRâ ¤6æöâ&ööbW†6W'C¢c*s"ãRÆ—7G2ãFÂãfÂã–ÂãÂæBãRã&2VÆ–v–&ÆRFòÖ÷fRFòFöæVöæÇ’gFW""Óe"Ô"ÖW&vW2æBf–æÂ&Wf–Wr7W÷'G2V6‚&÷rà ¤DD2Ó  ¤Fö3¢c(	B„DR'V–ÆBæ÷FW2 ¥6V7F–öã¢*s"ã’Â(	Å&W÷6—F÷'’–çF¶RæB"Óe"Ô"&÷VæF'ž(	Ò ¤6æöâ&6—3¢4äôâÔ•4ÔD4‚ ¤–×7FVBc’F6²”B‡2“¢„DRÔD•5CÂ„DRÔD•5CR ¤–×7FVBc’7V'F6²”B‡2“¢„DRÔD•5CãBÂ„DRÔD•5CãbÂ„DRÔD•5Cã’Â„DRÔD•5CãÂ„DRÔD•5CRã" ¥c’7FGW27F–öã¢æò7FGW26†ævR&V6öÖÖVæFVB ¤FVÇF¢FB÷7BÖÖW&vR&V6÷&BF†B"Óe"Ô"6ö×ÆWFVBv÷fW&æVB6¶WBFÖ—76–öâÂF—&V7B×6VÆV7F–öâ&–æF–ærÂf—†VB×ö–çBWf–FVæ6R6öçfW&vVæ6RÂf–æÂæ–æWFVVâ×7FvR52ÂæBW†7BÖ†VBW‡FW&æÂGFW7FF–öââ&W6W'fRF†RW†—7F–ær†—7F÷&–6Âõ2Ó266WFæ6R&V6÷&Bâ ¥v‡“¢*s"ã’7F–ÆÂFW67&–&W2"Óe"Ô"FÖ—76–öâ2÷WG7FæF–ærâ ¥&WòWf–FVæ6S¢4e"Ó.(	44e"ÓCbæBdÂÓ>(	5dÂÓ‚â ¤6æöâ&ööbW†6W'C¢c*s"ã’7W'&VçFÇ’6—2Â(	ÅF†RG&6¶VB6¶WB†2æ÷B6ö×ÆWFVBv÷fW&æVBWf–FVæ6RFÖ—76–öââ"Óe"Ô"÷vç3®(	Òà ¤DT4•4”ôã¢ÔU$tTB4„ätR44UD$ÄP ¢22"ã#’"Ób&VÖVF–F–öâ7FFP ¢222¢¥&Wf–Wr66÷RæBW7F&Æ—6†VB7FFR¢  ¥F†—2&Wf–WrföÆÆ÷vVBF†RöæRÖöfb”–ç7G'V7F–öâ2&VBÖöæÇ’÷7BÖÖW&vRFWFW&Ö–æF–öââ—BF–Bæ÷BG&VB"Â33cr÷"ç’÷F†W"VÆÂ&WVW7B2÷Vâ÷"VæF–ærÂæB—BW&f÷&ÖVBæòÖW&vR×&VF–æW7276W76ÖVçBÂ–×ÆVÖVçFF–öâÂõ2ÂbVF—G2Âc’VF—G2Â&ö&BWFFW2ÂFWÆ÷–ÖVçBÂÖ–w&F–öâÂ÷"W‡FW&æÂ×WFF–öâà ¢¢¥6÷W&6W2–ç7V7FVB¢  ¢¢&÷fVBW–2ÆâÂ–æ6ÇVF–ærF†R„DRÔU”33‚F—7F–ÆÆF–öâ66÷RÂ6—‚Õ"7G'V7GW&RÂFVÆ—fW&&ÆW2ÂW†6ÇW6–öç2ÂæBc’ãb6ö×ÆWF–öâ–çFVçBâ ¢¢&÷fVB–×ÆVÖVçFF–öâÆâÂ&VBVæB×FòÖVæBÂ–æ6ÇVF–ærF†Rc’6ö×ÆWF–öâ66÷RæBF†R6ö×ÆWFR"Ób(	B&VÆV6R6æ—G’÷&6†W7G&F–öâæBWf–FVæ6R&–æF–ævVæ—Bâ ¢¢7W'&VçBcc"ãBÂW7V6–ÆÇ’FFVæF"ã"F‡&÷Vv‚"ã#â ¢¢7W'&VçBc’ãbcãã"Â–æ6ÇVF–ærWfW'’&÷r÷&–v–æÆÇ’ÖVBv†öÆÇ’÷"'FÇ’Fò"Óbâ ¢¢F6²×&VÆWfçBW&ÖæVçB6æöâf÷"&ö6W726W&F–öâÂF—&V7BÖFF&6R–æg&7G'V7GW&RÂv÷fW&æVBWf–FVæ6RÂWFFW"÷væW'6†—Â&VÆV6RfÆ–FF–öâÂæB÷7GW&Râ ¢¢v—D‡V"&W÷6—F÷'’×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c&Âv†÷6R7W'&VçBFVfVÇB'&æ6‚—2Ö–æâ ¢¢&VÆWfçBÖW&vVBVÆÂ&WVW7G2Â&Wf–Ww2Â6öÖÖVçG2Â6†V6·2Â7W'&VçBf–ÆW2Âv÷fW&æVBWf–FVæ6RÂæBF†RW†7BÖ†VBW‡FW&æÂ&VÆV6RÖGFW7FF–öâ'F–f7Bà ¥&W÷6—F÷'’–ç7V7F–öâv26öææV7F÷"Ö&6VBæB&VBÖöæÇ’âæòÆö6Â&öGV7B×&W÷6—F÷'’6öÖÖæG2vW&R&W&W6VçFVB2†f–ær'VââF†RF÷væÆöFVBv—D‡V"7F–öç2GFW7FF–öâv2&VBÆö6ÆÇ’öæÇ’2â–Ö×WF&ÆR&Wf–Wr'F–f7Bà ¢¢¤ÖW&vVB–×ÆVÖVçFF–öâæB&VÖVF–F–öâÆ–æVvR¢  §ÂÆ–fV7–6ÆR7FvRÂÖW&vVBVÆÂ&WVW7BæBÖW&vR6öÖÖ—BÂ&Wf–WrF—7÷6—F–öâÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§Â÷&–v–æÂ"Ób–×ÆVÖVçFF–öâÂ"Â33S’ÂÖW&vVB2sƒsSfSssfcvfS“ƒ3s#3VFSfs&#–fSCVc–ÂW7F&Æ—6†VBF†R÷&–v–æÂf–ÂÖ6Æ÷6VB&VÆV6R×6æ—G’—VÆ–æRæBõ2×6¶vRFÖ—76–öâÂ'WB&WF–æVB'&–FvRÖW&77V×F–öç2ÆFW"–çfÆ–FFVB'’F†R&öGV7B÷væW.(	—2F—&V7BÖöæÇ’&6†—FV7GW&ÂFV6—6–öââÀ§Â–æ—F–Â6÷'&V7F—fRGFV×BÂ"Â33cÂÖW&vVB2&S–##CFCC“scsCS336fS3cc#ƒcv3cVÂ&W—&VBU”3#B&–æF–æw2Â&WF–æVBÖWf–FVæ6R6fWG’ÂDDÂ&ö¦V7F–öâÂæB–æ—F–Âõ2Ó"FööÆ–ærâÀ§Â–æ—F–Â6÷'&V7F—fRGFV×B"Â"Â33cÂÖW&vVB23Fc3&&csC“6fcvc“6CfFSV&3#S†#FS“CcfÂ6ö×ÆWFVBF†R'&–FvRÖFWVæFVçBõ2Ó"'VææW"6öçG&7BâÀ§Â–æ—F–Â6÷'&V7F—fRGFV×B2Â"Â33c"ÂÖW&vVB2ffScvS6C&3#ƒ36#C&3&F3Sƒ33CFFFSsvC“ƒÂF–v‡FVæVBF†R'&–FvRÖFWVæFVçB&VfÆ–v‡BæBWf–FVæ6RfÆ–FF÷'2âÀ§ÂW†7B×F÷–2&6†—FV7GW&Â7WW'6W76–öâÂcFFVæGVÒ"ã"Â&WF—&VBrÖ'&–FvVÂD%ô%$”DtUõU$ÆÂ'&–FvRfÆÆ&6²ÂF—&V7B×fW'7W2Ö'&–FvR&—G’ÂF†Rõ2Ó"ÆæRÂæBF†R'&–FvRÖFWVæFVçB"Ô2ÆæR27W'&VçB&WV—&VÖVçG2â†—7F÷&–6Â÷WGWG2&VÖ–æVB†—7F÷&–6ÂâÀ§ÂF—&V7BÖöæÇ’&VÖVF–F–öâÂ"Â33c2ÂÖW&vVB2c†&v&&fVcvSVc3&3ƒCvF&F#F3#Svc#&Ss–Â–çG&öGV6VBF—&V7BÖöæÇ’D$66W76Â&WF—&VBÖ¶W’&VgW6ÂÂ&VBÖöæÇ’G&ç67F–öâÖV6†æ–72ÂF—&V7B×6VÆV7F–öâWf–FVæ6RÂõ2Ó2FööÆ–ærÂæBfö7W6VBFW7G2âÀ§ÂF—&V7BÖöæÇ’&VÖVF–F–öâ"Â"Â33cBÂÖW&vVB2C3ƒS6VVCs–&#SSS3sssf#ƒ&V3ƒ“SC&CFÂ6öçfW&vVB†–v†W"ÖÆWfVÂ6öç7VÖW'2öâD$66W76Â7G&VæwF†VæVB&WF—&VB×G&ç7÷'B66ææ–ærÂæBFFVBF†RW‡Æ–6—Bæöæf–æÂ"Ô—VÆ–æR&÷VæF'’âÀ§ÂF—&V7BÖöæÇ’&VÖVF–F–öâ2Â"Â33cRÂÖW&vVB2f&cƒsSF†S##fCc†Sv6sS–V3#†6Fc“VÂ&÷fVB&WF—&VBÖ¶W’&VgW6Â&Vf÷&R&VF–ærF†RF—&V7BVæGö–çBfÇVRæB7G&VæwF†VæVB7FF–26öçG&7B6†V6·2âÀ§Âf–æÂ"Óe"Ô6öçfW&vVæ6RÂ"Â33cbÂÖW&vVB2fSc–CvsvcS3–Cs3fff63S“f&CSfvCF“Âf–æÆ—¦VBF†RF—&V7BÖöæÇ’6÷W&6R÷FööÆ–ær&÷VæF'’Â66Æ&ÆR&VÆV6R–FVçF—G’Â÷'F&ÆRF‚×&ööb6VÖçF–72ÂW‡FW&æÂGFW7FF–öâ'V–ÆFW"ÂæBõ2Ó2W†V7WF–öâFööÆ–ærâÀ§ÂòÖWF†÷&—¦VBõ2Ó2Â6GW&VBv–ç7B6÷W&6R6öÖÖ—BC6FCf#“sSCC&Cv“3#–66ffc–ccCƒ6–CFfVS&Â&öGV6VBF†R&÷VæFVBF—&V7B÷7Fw&U5Â&VBÖöæÇ’6¶WBÆFW"FÖ—GFVB'’"Óe"Ô"âÀ§Âf–æÂFöÖ–2–çFVw&F–öâÂ"Â33crÂ†VBs6Ccvf3V#FS&fFcƒf3#SC&33–F3#FÂÖW&vVB2F#3S–&36c“V33S“Ssffs33–S““c&ÂFÖ—GFVBF—&V7B×6VÆV7F–öâæBõ2Ó2Wf–FVæ6RÂV&çF–æVB'&–FvR†—7F÷'’Â6öçfW&vVBF†RWf–FVæ6Rw&‚Â6ö×ÆWFVBF†Ræ–æWFVVâ×7FvRf–æÂvFRÂæB&öGV6VBW†7BÖ†VBW‡FW&æÂGFW7FF–öââÀ ¤ÆÂÆ—7FVBVÆÂ&WVW7G2&R6Æ÷6VBæBÖW&vVBâæò÷Vâ"—2'BöbF†—2&Wf–Wrà ¢¢¤7W'&VçB&W÷6—F÷'’7FFR¢  ¢¢7W'&VçB&Wf–WvVB'&æ6ƒ¢Ö–æâ ¢¢7W'&VçBF—¢s–CF&css3#ƒ3SCs#V33CScs3sFF&â ¢¢f–æÂ&VÖVF–F–öâÖW&vS¢F#3S–&36c“V33S“Ssffs33–S““c&â ¢¢Ö–æ—2öæR6öÖÖ—B†VBöbF†Rf–æÂ&VÖVF–F–öâÖW&vRâ ¢¢F†RöæÇ’–çFW'fVæ–ærf–ÆR6†ævR—2F†RcWFFRg&öÒc"ã2ã’Fòc"ãBâæò6öFRÂFW7BÂ66†VÖÂ'VçF–ÖRÂv÷&¶fÆ÷rÂv÷fW&æVBWf–FVæ6RÂ–æFW‚ÂÖ—'&÷"Â6†V6·7VÒÂF‚×&ööbÂF÷öÆöw’Â÷"&VÆV6R'F–f7B6†ævVBgFW""Â33crâ ¢¢F†W&Vf÷&RÂF†RW†7BÖ†VB6öFRæBv÷fW&æVBWf–FVæ6RfÆ–FF–öâg&öÒ"Â33cr&VÖ–ç2Æ–6&ÆRFò7W'&VçB&W÷6—F÷'’7FFRâF†RÆFW"cÖöæÇ’6öÖÖ—BFöW2æ÷B&WV—&R7W'&VçB×7FFR&W'Vææ–æröb–×ÆVÖVçFF–öâfÆ–FF–öâà ¢¢¤†—7F÷&–6Â&Wf–WræBfÆ–FF–öâ7FFR¢  ¢¢ÆÂf—fR"Â33cr&Wf–WrF‡&VG2vW&R&W6öÇfVBv–ç7BF†Rf–æÂ†VBâ ¢¢W†7BÖ†VBv—D‡V"7F–öç2'Vâ3scSƒ“#66ö×ÆWFVB7V66W76gVÆÇ’â ¢¢ÆÂ6WfVâ¦ö'276VBâ ¢¢F†RW‡FW&æÂ'F–f7B†FR×&VÆV6RÖGFW7FF–öâÓs6Ccvf3V#FS&fFcƒf3#SC&33–F3#F&VÖ–ç2f–Æ&ÆRæBVæW‡—&VC²—G2&6†—fRF–vW7B—26†#Sc£s#FSS“Sv3CCfFV#3S#3fFV6&S6c3S–cVFfCC–6CCc3c&&3c†Fâ ¢¢æò–æF—7Vç6&ÆR6÷W&6Rv2Væf–Æ&ÆRà ¢222¢¥c&VÖVF–F–öâ76W76ÖVçB¢  ¥F†R7W'&VçBc76W76ÖVçB—2¢§FV6†æ–6ÆÇ’67W&FRöâF†R&VÖVF–F–öâ&W7VÇB¢¢Â'WB—B6öçF–ç2öæR7FÆR&W÷6—F÷'’×7FFR6VçFVæ6RæBöæR–æ6ö×ÆWFRc’–çfVçF÷'’6öæ6ÇW6–öâà §Âc6öæ6ÇW6–öâÂVF—B&W7VÇBÂFWFW&Ö–æF–öâÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§Â"Â33cr6ö×ÆWFVB"Óe"Ô"æBÖW&vVBF†RF—&V7BÖöæÇ’f–æÂ–çFVw&F–öââÂv—D‡V"&÷fW2"Â33crÖW&vVBv—F‚†VBs6CcrââææBÖW&vR6öÖÖ—BF#3Rââæ²7W'&VçBf–ÆW26öçF–âF†RFW67&–&VB–çFVw&F–öââÂ7W÷'FVBâÀ§ÂF—&V7BÖöæÇ’6VÆV7F–öâæB&WF—&VBÖ¶W’&VgW6Â&R–×ÆVÖVçFVBâÂ7W'&VçBVæv–æRöF"öFFW"ç–W‡÷6W2öæÇ’F—&V7B7–6÷u&÷f–FW&6VÆV7F–öâæB&V¦V7G2D%ô%$”DtUõU$ÆÂD%ôdõ$4Uô%$”DtVÂæBD%ôÄÄõuô%$”DtUô”åõ$ôF'’¶W’&W6Væ6R&Vf÷&R&÷f–FW"6öç7G'V7F–öâ÷"’ôòâ"Â33cR7V6–f–6ÆÇ’†&FVæVB&VgW6ÂÖ&Vf÷&R×fÇVR×&VB&V†f–÷"âÂ7W÷'FVBâÀ§ÂF†RF—&V7B×6VÆV7F–öâWf–FVæ6R&–Ö'’—2FWFW&Ö–æ—7F–2æB76–ærâÂ7W'&VçB'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæ6öçF–ç2F†R&WV—&VBf÷W"66W2Â6—‚76–ær&VF–6FW2Â&W7VÇCÕ56ÂæBæòf–ÇW&S²—G27G&–7B66†VÖ&V¦V7G2Væ¶æ÷vâ7G'V7GW&RâÂ7W÷'FVBâÀ§Âõ2Ó2—266WFVB2&÷VæFVBF—&V7B&VBÖöæÇ’Wf–FVæ6Rv—F†÷WB&W'VââÂF†R6¶WB&V6÷&G252ÂGvòÖ6öææV7F–öâæBVÆWfVâ×7FFVÖVçB&÷VæFVBö'6W'fF–öâÂFVâ÷7GW&RVW&–W2Â¦W&ò5Âw&—FW2Â¦W&ò&WG&–W2Â¦W&òÇFW&æFR×&÷f–FW"GFV×G2Â6ö×ÆWFRæöæ6Æ–×2Ââ–æFWVæFVçBfÆ–FF–öâ&V6V—BÂæB6†V6·7VÒÆVFvW"âÂ7W÷'FVBâÀ§Â7W'&VçBæB†—7F÷&–6ÂWf–FVæ6R&R6W&FVBâÂ7W'&VçBF—&V7B×6VÆV7F–öâæBõ2Ó2&÷w2&R7F—fRâ&WF–æVB'&–FvR÷&÷f–FW"×&—G’æBõ2ÓWf–FVæ6R—2†6‚Ög&÷¦VâæBfÆ–FFVBöæÇ’2†—7F÷&–6Â–çFVw&—G“²7FvR"VÖ—G2„•5Dõ$”4Åô”åDTu$•E•ôô¶Âæ÷B7W'&VçB'&–FvR52âÂ7W÷'FVBâÀ§ÂF†R6æöæ–6ÂWFFW"÷vç2–æFW‚ÂÖ—'&÷"Â†6†W2ÂæB6–&Æ–ær&öög2âÂ"Óe"Ô"Ö÷fVB7FvRRFò6†V6²ÖöæÇ“²f–æÂvVæW&F–öâö67W'2&Vf÷&RF†RvFRF‡&÷Vv‚F†R6æöæ–6ÂWFFW"â7W'&VçB÷&–VçFF–öâ&W÷'G2SC‚6ö†W&VçB'F–f7G2âÂ7W÷'FVBâÀ§ÂF†Rf–æÂ&VÆV6R—VÆ–æR†2W†7FÇ’æ–æWFVVâ7FvW2æBf–Ç26Æ÷6VBâÂF†R7W'&VçBÆör6öçF–ç2W†7FÇ’æ–æWFVVâ÷&FW&VBô¶7FvW2Âf—'7Eöf–ÆVE÷7FvS¤äôäVÂæB7VÖÖ'“¥56âF†R—VÆ–æR6öFR7F÷2öâf—'7Bf–ÇW&RæBFöW2æ÷B&W'Vâõ2÷"6ÆÂW‡FW&æÂ7—7FV×2âÂ7W÷'FVBâÀ§ÂF†Rf–æÂ&VÆV6RGFW7FF–öâ—2W†7B×6÷W&6RæBfW&–f–W2&VÂ6¶vVBVçG'’ö–çBâÂF†RW‡FW&æÂ'F–f7B&V6÷&G26÷W&6Uö6öÖÖ—CÓs6CcrââæÂ6÷W&6Uö6öÖÖ—EöW†7C×G'VVÂFWFW&Ö–æ—7F–2G&6¶VB×G&VRF–vW7BÂfÆ–FF–öå÷&W7VÇCÕ56Â&VÆV6UöFÖ—76–öãÕ#e%ô%ôd”äÅõ56ÂæB—VÆ–æU÷7F÷ÖçVÆÆâ—G2'V–ÆBÆör&V6÷&G2&VÂv†VVÂ'V–ÆBæB–ç7FÆÆVB†F7FÆVçG'’ö–çBâÂ7W÷'FVBâÀ§ÂF†RÖW&vVBVæGö–çB—2F†R7W'&VçBÖ–æF—F#3RââæâÂ7W'&VçBÖ–æ—2æ÷rs–CF&ââæâÂ7FÆR7FFVÖVçBâÀ§ÂæòÆFW"ÖFW&–ÂF—fW&vVæ6RW†—7G2âÂF†R6öÆRÆFW"6†ævR—2F†Rcc"ãBFö7VÖVçFF–öâWFFRâæò&Wf–WvVB–×ÆVÖVçFF–öâ÷"Wf–FVæ6Rf–ÆR6†ævVBâÂ7W÷'FVBgFW"6÷'&V7F–ærF†RF—7FFVÖVçBâÀ§Âf—fR&÷w2&R7W÷'F&ÆRf÷"ÆFW"c’Ö–çFVææ6RâÂÆÂf—fRæÖVB&÷w2&R7W÷'FVBÂ'WBF†R&÷fVB–×ÆVÖVçFF–öâÆâÖVBF‡&VRFF—F–öæÂ&÷w2v†öÆÇ’÷"'FÇ’Fò"ÓbâÂ7W÷'FVB'WB–æ6ö×ÆWFRâÀ§ÂæòFF—F–öæÂ÷7BÖÖW&vR&W÷6—F÷'’&VÖVF–F–öâ—2&WV—&VBâÂ7W'&VçB6öFRÂWf–FVæ6RÂW†7BÖ†VBfÆ–FF–öâÂæBÆFW"Ö6†ævR–ç7V7F–öâ&WfVÂæòVç&W6öÇfVB–×ÆVÖVçFF–öâÂWf–FVæ6RÂ6fWG’Â÷"fÆ–FF–öâFVfV7BâÂ7W÷'FVBâÀ ¢¢¥c–çfVçF÷'’FVf–6–Væ7’¢  ¥c6÷'&V7FÇ’–FVçF–f–W2F†W6Rf—fRF—&V7BÖöæÇ’&VÖVF–F–öâ6Æ÷7W&R6æF–FFW3  ¢¢„DRÔD•5CãF ¢¢„DRÔD•5Cãf ¢¢„DRÔD•5Cã– ¢¢„DRÔD•5Cã ¢¢„DRÔD•5CRã&  ¤†÷vWfW"ÂF†R&÷fVB–×ÆVÖVçFF–öâÆâÇ6òÖVBF†RföÆÆ÷v–ær&÷w2v†öÆÇ’÷"'FÇ’Fò"Óc  ¢¢„DRÔD•5CRã ¢¢„DRÔD•5CãV ¢¢„DRÔD•5Cã  ¥cFFVæGVÒ"ã#FöW2æ÷B&V6öæ6–ÆRF†÷6RF‡&VR&÷w2â—BæV—F†W"7FFW2F†BF†W’&R7F–ÆÂ÷Vâæ÷"7WÆ–W2âWF†÷&—G’Ö&6VBW†6ÇW6–öâg&öÒF†R÷&–v–æÂ"Ób–çfVçF÷'’à ¥F†RöÖ—76–öâFöW2æ÷B–çfÆ–FFRF†RFV6†æ–6Â&VÖVF–F–öââ—BÖ¶W2c(	—2c’6Æ÷7W&R–çfVçF÷'’–æ6ö×ÆWFRà ¢222¢¥"Óbc’–çfVçF÷'’&V6öæ6–Æ–F–öâ¢  ¢¢¤÷&–v–æÂ"ÓbÖ–ærW‡G&7FVB–æFWVæFVçFÇ’g&öÒF†R&÷fVB–×ÆVÖVçFF–öâÆâ¢  ¥F†R&÷fVB"ÓbVæ—BW‡Æ–6—FÇ’æÖW2ÆÂV–v‡B7V'F6·2&VÆ÷râF†R6ÖRÖ–æw2V"–âF†RÆî(	—2c’6ö×ÆWF–öâ66÷Rà §Â÷&–v–æÂ"ÓbÖÖVBc’&÷rÂÖ–ær–â&÷fVBÆâÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÀ§Â„DRÔD•5CRãÂ"Óò"ÓbÀ§Â„DRÔD•5CRã&Â"Óò"ÓbÀ§Â„DRÔD•5CãFÂ"ÓBòõ2Óò"ÓbÀ§Â„DRÔD•5CãVÂ"ÓBò"ÓbÀ§Â„DRÔD•5CãfÂ"ÓbÀ§Â„DRÔD•5Cã–Â"ÓBòõ2Óò"ÓbÀ§Â„DRÔD•5CãÂ"ÓBò"ÓbÀ§Â„DRÔD•5CãÂ"ÓRòõ2Ó"ò"ÓbÀ ¢¢¤7W'&VçBc&VÖVF–F–öâ6Æ÷7W&R6WB¢  ¥cFFVæGVÒ"ãRFVf–æW2&÷r×7V6–f–2&VF–6FW2æB÷76–&ÆRÆFW"7FGW2Ö÷fVÖVçBf÷#  ¢¢„DRÔD•5CãF ¢¢„DRÔD•5Cãf ¢¢„DRÔD•5Cã– ¢¢„DRÔD•5Cã ¢¢„DRÔD•5CRã&  ¥cFFVæGVÒ"ã#&WVG2F†R6ÖRf—fR×&÷r&V6öÖÖVæFF–öâà ¢¢¥&V6öæ6–Æ–F–öâ¢  §Â&÷rÂ–â7W'&VçBcf—fR×&÷r6WBÂ7W÷'FVBF—7÷6—F–öâÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§Â„DRÔD•5CRãÂæòÂ¢¤öÖ—GFVBv—F†÷WB7Vff–6–VçBWF†÷&—G’â¢¢cFFVæGVÒ"ãW‡&W76Ç’6–BF†—2&÷r&VÖ–æVB6†&VBv—F‚"ÓbæB6†÷VÆBæ÷BÖ÷fRöâ"ÓÆöæRâF†Rf–æÂ"Ób—VÆ–æRæ÷r&÷fW2—G2&VÖ–æ–ær6æöæ–6ÂÖVæ6öF–æræBVçf—&öæÖVçB×–âö&Æ–vF–öç2â—B×W7B&R76W76VB–âF†—2&Wf–WrâÀ§Â„DRÔD•5CRã&Â–W2ÂF—&V7BÖöæÇ’"Óe"Ô"6Æ÷7W&R6æF–FFRâÀ§Â„DRÔD•5CãFÂ–W2ÂF—&V7BÖöæÇ’"Óe"Ô"6Æ÷7W&R6æF–FFRv—F‚ÖVæFVB6VÖçF–72âÀ§Â„DRÔD•5CãVÂæòÂ¢¤Ç&VG’6ö×ÆWFVBF‡&÷Vv‚"ÓBæBæ÷B&V÷VæVB'’F—&V7BÖöæÇ’&VÖVF–F–öââ¢¢"Ób&VÖ–æVB&W7öç6–&ÆRf÷"f–æÂ÷&6†W7G&F–öâæB7W'&VçB&WfÆ–FF–öã²7FvR’æBW†7BÖ†VB4’fÆ–FFRF†R7W'&VçB&öG”w&‚Wf–FVæ6RfÖ–Ç’â—B×W7B&R76W76VB'WB—2æ÷BæWrF—&V7BÖöæÇ’&VÖVF–F–öâ&÷râÀ§Â„DRÔD•5CãfÂ–W2ÂF—&V7BÖöæÇ’"Óe"Ô"6Æ÷7W&R6æF–FFRâÀ§Â„DRÔD•5Cã–Â–W2ÂF—&V7BÖöæÇ’"Óe"Ô"6Æ÷7W&R6æF–FFRv—F‚&VæÖVBæBÖVæFVB6VÖçF–72âÀ§Â„DRÔD•5CãÂæòÂ¢¤Ç&VG’6ö×ÆWFVBF‡&÷Vv‚"ÓBæBæ÷B&V÷VæVB'’F—&V7BÖöæÇ’&VÖVF–F–öââ¢¢"Ób&VÖ–æVB&W7öç6–&ÆRf÷"f–æÂ÷&6†W7G&F–öâæB7W'&VçB&WfÆ–FF–öã²7FvRæBW†7BÖ†VB4’fÆ–FFRF†R7W'&VçB&6†—FV7GW&R6æ6†÷Bâ—B×W7B&R76W76VB'WB—2æ÷BæWrF—&V7BÖöæÇ’&VÖVF–F–öâ&÷râÀ§Â„DRÔD•5CãÂ–W2ÂW†—7F–ær"ÓRæBõ2Ó"&ööbv2&W6W'fVBæB&V&÷VæBF‡&÷Vv‚"Óe"Ô"v—F†÷WB&W'Vææ–ærõ2Ó"âÀ ¢¢¤f–æÂ&÷fVâ6WB&WV—&–ærF†—2&Wf–Wr¢  ¤ÆÂV–v‡B÷&–v–æÂ"ÓbÖÖVB&÷w2&WV—&R6Æ÷7W&RFWFW&Ö–æF–öã  £â„DRÔD•5CRã £"â„DRÔD•5CRã& £2â„DRÔD•5CãF £Bâ„DRÔD•5CãV £Râ„DRÔD•5Cãf £bâ„DRÔD•5Cã– £râ„DRÔD•5Cã £‚â„DRÔD•5Cã  ¤æò÷&–v–æÂ"Ób&÷r&VÖ–ç2Væ66÷VçFVBf÷"à ¢222¢¥&VÖVF–F–öâö&Æ–vF–öâ7&÷77vÆ²¢  §Â&WV—&VÖVçBÂ6÷W&6RæBW†7BÆö6F÷"ÂÖW&vVB×7FFR&W7VÇBÂ7W'&VçB×7FFR&W7VÇBæBWf–FVæ6RÂf–æF–ærÂc’–×7BÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§ÂF—&V7BÖöæÇ’'VçF–ÖR6VÆV7F–öâÂcFFVæGVÒ"ã"Â*tFV6—6–öâæBVffV7F—fR÷7GW&S²FFVæGVÒ"ãRÂ*tFV6—6–öâæBVffV7F—fRc’÷7GW&RÂ"Óe"Ô&VÖ÷fVBW†V7WF&ÆR'&–FvR6VÆV7F–öâæB6öçfW&vVB'VçF–ÖRöâD$66W76ÇW27–6÷râÂ7W'&VçBVæv–æRöF"öFFW"ç–6VÆV7G2öæÇ’7–6÷u&÷f–FW&²æòÆFW"6öFR6†ævRö67W'&VBâÂ6F—6f–VBâÂ7W÷'G2ãFæBÖVæFVBã–âÀ§Â&WF—&VB×G&ç7÷'B&VgW6ÂÂcFFVæGVÒ"ã"Â*u'VçF–ÖRæB6öæf–wW&F–öâ6öçG&7C²FFVæGVÒ"ã2Â*tFV6—6–öâæBVffV7F—fRWf–FVæ6R÷7GW&RÂ"Óe"ÔFFVBF†RW†7B&WF—&VBÖ¶W’&÷7FW"æB&VgW6ÂÖ&Vf÷&RÔ’ôòÖV6†æ–72âÂ7W'&VçB6öFR&V¦V7G2V6‚&WF—&VB¶W’'’¶W’&W6Væ6RÂ–æ6ÇVF–ærV×G’fÇVW2Â&Vf÷&RF—&V7BÖVæGö–çBfÇVR66W72÷"&÷f–FW"6öç7G'V7F–öââF†RF—&V7B×6VÆV7F–öâ'F–f7B&V6÷&G2ÆÂ&WV—&VB&VgW6Â66W2252âÂ6F—6f–VBâÂ7W÷'G2ãFÂÖVæFVBã–²&WV—&W27FÆR'&–FvR×Fö¶Vâ6ÆVçW–âãVâÀ§Â7W'&VçB×fW'7W2Ö†—7F÷&–6ÂWf–FVæ6R6W&F–öâÂcFFVæGVÒ"ã2Â*t†—7F÷&–6Â'&–FvRWf–FVæ6RV&çF–æS²FFVæGVÒ"ãRÂ*t7W'&VçBWf–FVæ6R&–æF–æræBWFFW"÷væW'6†—Â"Óe"Ô"&V6Æ76–f–VB&WF–æVB'&–FvR÷&÷f–FW"×&—G’ôõ2Ó&÷w22†—7F÷&–6ÂâÂ7FvR"fÆ–FFW2†—7F÷&–6Â†6†W2öæÇ’æBVÖ—G2„•5Dõ$”4Åô”åDTu$•E•ôô¶²æò7W'&VçB'&–FvRFö¶Vâ÷"f–Æ&–Æ—G’6Æ–Ò&VÖ–ç2âÂ6F—6f–VBâÂ7W÷'G2ãfÂã–ÂãRã&âÀ§ÂFWFW&Ö–æ—7F–2F—&V7B×6VÆV7F–öâWf–FVæ6RÂcFFVæGVÒ"ã2Â*tFV6—6–öâæBVffV7F—fRWf–FVæ6R÷7GW&RÂ"Óe"Ô"FFVBF†Rv÷fW&æVBF—&V7B×6VÆV7F–öâ&–Ö'’æB66†VÖâÂf÷W"66W2æBÆÂ6—‚FW&—fVB&VF–6FW273²7W'&VçB6–&Æ–ær&ööb&–æG2F‚Â†6‚ÂæB6—¦RâÂ6F—6f–VBâÂ7W÷'G2ãFÂã–ÂãRã&âÀ§Â66WFVBõ2Wf–FVæ6RFÖ—76–öâv—F†÷WB&W'VâÂcFFVæGVÒ"ãBÂ*u7V66W726¶WB–çfVçF÷'’æB÷væW'6†—æB*ufÆ–FF–öâÂFÖ—76–öâÂÖ–w&F–öâÂæB&öÆÆ&6³²FFVæGVÒ"ãRÂ*t÷væW'6†—æBF÷F–öâ6WVVæ6RÂ"Óe"Ô"6÷–VBæBFÖ—GFVBF†RÇ&VG’Ö6GW&VBõ2Ó26¶WBv—F†÷WB–çfö¶–ær—G2&öGV6W"âÂ7W'&VçB6¶WB'—FW2Â6†V6·7VÒÆVFvW"Â&W7VÇB7VÖÖ'’ÂfÆ–FF–öâ&V6V—BÂæöæ6Æ–×2ÂæBF‚&öög2&VÖ–â&W6VçC²—VÆ–æRfÆ–FF–öâ—2&VBÖöæÇ’âÂ6F—6f–VBâÂ7W÷'G2ãFÂã–ÂãRã&âÀ§Â6æöæ–6ÂWFFW"÷væW'6†—ÂcFFVæGVÒ"ãRÂ*t7W'&VçBWf–FVæ6R&–æF–æræBWFFW"÷væW'6†—²cB(	B„DRÖV6†æ–72wV–FRÂ*sã2ãWf–FVæ6R¦ö'2‡6–ævÆR×w&—FW"FööÇ2’Â"Óe"Ô"f–æÆ—¦VB&–Ö&–W2&Vf÷&RöæR6æöæ–6ÂWFFW"'VâæBÖ÷fVB7FvRRFòÒÖ6†V6¶âÂ7W'&VçB—VÆ–æRFöW2æ÷Bw&—FRF‚&öög2Â–æFW‚ÂÖ—'&÷"Â÷"6VçF–æVÇ3²æòÆFW"Wf–FVæ6R×WFF–öâö67W'&VBâÂ6F—6f–VBâÂ7W÷'G2ãRã&ÂãfâÀ§Â‡VÖâ–æFW‚æBÖ6†–æRÖ—'&÷"6öçfW&vVæ6RÂcFFVæGVÒ"ãRÂ*u&÷r×7V6–f–27W÷'F&–Æ—G’&VF–6FW3²c"(	B„DR66†VÖ2æB'F–f7G2Â*s‚ã2Ö6†–æRWf–FVæ6R–æFW‚(	B¥4ôäÂÖ—'&÷"Âf–æÂÖW&vR&öGV6VBSC‚×&÷r‡VÖâôÖ6†–æRf—†VBö–çBv—F‚&WV—&VBæWr–FVçF—F–W2W†7FÇ’öæ6RâÂ7W'&VçB÷&–VçFF–öâ&W÷'G2F÷FÅö'F–f7G3¢SC†æB7FGW3¢ö¶²7W'&VçB‡VÖâ–æFW‚6VçF–æVÂ—2–FCCââæâÂ6F—6f–VBâÂ7W÷'G2ãRã&ÂãfÂæBÆÂWf–FVæ6RÖ&6¶VB&÷w2âÀ§Â†6‚Â6†V6·7VÒÂF‚×&ööbÂæBF÷öÆöw’6ö†W&Væ6RÂcFFVæGVÒ"ãRÂ*t7W'&VçBWf–FVæ6R&–æF–æræBWFFW"÷væW'6†—Âf–æÂWFFW"ö6†V6²6†–â76VBâÂ7W'&VçBF—&V7B×6VÆV7F–öâ&ööbÂõ2ÆVFvW'2Â–æFW‚ôÖ—'&÷"6VçF–æVÇ2ÂæB÷&–VçFF–öâ&VÖ–âVæ6†ævVBæB6ö†W&VçBâÂ6F—6f–VBâÂ7W÷'G2ãRã&âÀ§Â÷'F&ÆRF‚×&ööb6VÖçF–72ÂcFFVæGVÒ"ãbÂ*u÷'F&ÆRF‚×&ööb6VÖçF–72Â"Óe"Ô&VÖ÷fVB6ÆöæRÖÆö6Âf–ÆW7—7FVÒ×F–ÖR6ö×&—6öâ26÷'&V7FæW72&VF–6FRâÂ7W'&VçB&öög2&–æBW†7BF‚ö†6‚÷6—¦RæB&W6W'fRF–ÖW7F×6†S²ÆFW"6†V6¶÷WB×F–ÖR—2æ÷BW6VBFò–çfÆ–FFRF†VÒâÂ6F—6f–VBâÂ7W÷'G2ãRã&æB&VÆV6R÷'F&–Æ—G’âÀ§ÂÖæ–fW7BÖFW&—fVB&VÆV6R–FVçF—G’ÂcFFVæGVÒ"ãbÂ*u6–ævÆR&VÆV6RÖ–FVçF—G’6÷W&6RæB*t7–6Æ–2&VÆV6Rw&‚Â"Óe"ÔÖFR6æöæ–6Â6FÆöröÖæ–fW7Bæ§6öæF†R6–ævÆRG&6¶VB&VÆV6RÖ–FVçF—G’–çWBâÂW‡FW&æÂGFW7FF–öâ&V6÷&G2&VÆV6Uö–FWVÂFòÖæ–fW7E÷6†#Sf²6÷W&6R×FòÖÖæ–fW7B×Fò×&VÆV6R×FòÖGFW7FF–öâF—&V7F–öâ&VÖ–ç27–6Æ–2âÂ6F—6f–VBâÂ7W÷'G2ãfæBãRãâÀ§ÂW†7B×6÷W&6RW‡FW&æÂGFW7FF–öâÂcFFVæGVÒ"ãbÂ*tW‡FW&æÂ&VÆV6RGFW7FF–öâÂW†7BÖ†VB'F–f7Bv2vVæW&FVB÷WG6–FRF†R6÷W&6RG&VRf÷"s6CcrââæâÂ'F–f7B&V6÷&G2W†7B6÷W&6R6öÖÖ—BÂ6ÆVâG&6¶VB×G&VRF–vW7BÂ52Â&VÂ6¶vVBVçG'—ö–çBÂæBæò—VÆ–æR7F÷²'F–f7BF–vW7BÖF6†W2v—D‡V"ÖWFFFâÂ6F—6f–VBâÂ7W÷'G2ãfÂãRãÂãRã&âÀ§Âf–æÂ&VÆV6R×6æ—G’÷&6†W7G&F–öâÂcFFVæGVÒ"ãRÂ*t6æöæ–6Â&VÆV6R×6æ—G’7FvR÷&FW"Â"Óe"Ô"&WÆ6VBG&ç6—F–öæÂöæöæf–æÂ÷WGWBv—F‚f–æÂæ–æWFVVâ×7FvR52âÂ7W'&VçBÆör†2ÆÂæ–æWFVVâ÷&FW&VB7FvW2Âæòf–ÇW&RÂæBf–æÂ52âÂ6F—6f–VBâÂ7W÷'G2ãf²&WfÆ–FFW2ãVÂãÂæBÆÂ÷F†W"ÖVB&÷w2âÀ§Â&WV—&VB7FvR÷&FW"æBf–ÂÖ6Æ÷6VB&V†f–÷"ÂcFFVæGVÒ"ãRÂ*t6æöæ–6Â&VÆV6R×6æ—G’7FvR÷&FW"Âf–æÂ—VÆ–æR7F÷VBöâf—'7Bf–ÇW&R'’FW6–vâæB&WV—&VBWfW'’7FvRâÂ7W'&VçB6÷W&6R&W6W'fW2W†7B7FvR&÷7FW"Â&WV—&VB7V66W726öFW2Âæò6¶—–ærÂæBæò&W—"öb7FÆRWf–FVæ6RGW&–ærvFRW†V7WF–öââÂ6F—6f–VBâÂ7W÷'G2ãfâÀ§Â&VÂ6¶vVBVçG'’×ö–çBfÆ–FF–öâÂcFFVæGVÒ"ãbÂ*tW‡FW&æÂ&VÆV6RGFW7FF–öâÂ"Óe"Ô"&W6öÇfVB&Wf–Wrf–æF–æw2&WV—&–ærg&W6‚v†VVÂÖöæÇ’Vçf—&öæÖVçBæB&VÂ†F7FÆW†V7WF&ÆRâÂGFW7FF–öâ'V–ÆBÆör&V6÷&G2v†VVÂ'V–ÆBÂ—6öÆFVB–ç7FÆÆF–öâÂæB7V66W76gVÂ6¶vVBÖ6öç6öÆRW†V7WF–öââÂ6F—6f–VBâÂ7W÷'G2ãfâÀ§Â6V7&WBæB–ÆöB6fWG’ÂcFFVæF"ã>(	3"ãbÂW‡Æ–6—Bæöæ6Æ–×2æBfÆ–FF÷"&WV—&VÖVçG2Â"ÔæB"Ô"fÆ–FF÷'2&V¦V7FVB&r6V7&WB÷–ÆöBÖ&¶W'2æB&WF–æVBæÖW2ÖöæÇ’Wf–FVæ6RâÂõ2Ó2—2&W6Væ6RÖöæÇ“²F—&V7B6VÆV7F–öâ6öçF–ç2æòVæGö–çBfÇVW3²&öG”w&‚æBÖVBÖ66†R'F–f7G26öçF–âæò&rfVæF÷"W'6—7FVæ6S²W‡FW&æÂGFW7FF–öâ&V6÷&G26V7&WB×6fWG’öÖ—76–öç2&F†W"F†â6÷––ærVç6fRf–ÆW2âÂ6F—6f–VBâÂ7W÷'G2ÆÂV–v‡B&÷w2âÀ§Â&W6W'fF–öâöbW‡Æ–6—Bæöæ6Æ–×2ÂcFFVæF"ãN(	3"ã#Â*tW‡Æ–6—Bæöæ6Æ–×2Â'2æBõ2&V6÷&G2F—66Æ–Ò52ÂFö¶Vâ6F—6f7F–öâÂc’Ö÷fVÖVçBÂFWÆ÷–ÖVçBÂÖ–w&F–öâÂæB6Æ÷6V÷WBâÂ7W'&VçB6¶WBÂÖVBÖ66†RÖæ–fW7BÂ"Â33cr&öG’ÂæBW‡FW&æÂGFW7FF–öâ&WF–âF†÷6Ræöæ6Æ–×2âÂ6F—6f–VBâÂ&WfVçG2Wf–FVæ6R×Fò×7FGW2÷fW&6Æ–Ó²FöW2æ÷B&Æö6²6W&FRc’Ö–çFVææ6RâÀ§Â&÷r×7V6–f–2c’7W÷'BWf–FVæ6RÂcFFVæGVÒ"ãRÂ*u&÷r×7V6–f–27W÷'F&–Æ—G’&VF–6FW2Â"Óe"Ô"–æ6ÇVFVBf—fR×&÷r7W÷'B7&÷77vÆ²âÂÆÂf—fRF—&V7B×&VÖVF–F–öâ&÷w272â7W'&VçBf–æÂ—VÆ–æRÇ6ò6ö×ÆWFW2F†RF‡&VR÷&–v–æÂ"Ób&÷w2öÖ—GFVBg&öÒF†Bf—fR×&÷r7&÷77vÆ²âÂ6F—6f–VBÂ'WBc–çfVçF÷'’—2–æ6ö×ÆWFRâÂ7W÷'G2ÆÂV–v‡B&V6öæ6–ÆVB&÷w2âÀ§ÂæòGWÆ–6FRÂ÷'†æVBÂ7FÆRÂÖçVÆÇ’f'&–6FVBÂ÷"Ö—66Æ76–f–VBWf–FVæ6RÂcFFVæGVÒ"ãRÂãRã&&VF–6FW3²c"*s‚ã2Âf–æÂWFFW"6†V6·2Â†—7F÷&–6Â†6‚g&VW¦–ærÂæBöæR×&÷r×W"Ö–FVçF—G’FÖ—76–öâ76VBâÂ7W'&VçBSC‚×&÷rF÷öÆöw’&VÖ–ç26ö†W&VçC²7FvRR—26†V6²ÖöæÇ“²æò÷7BÖÖW&vRWf–FVæ6R6†ævRö67W'&VBâÂ6F—6f–VBâÂ7W÷'G2ãRã&æBÆÂWf–FVæ6RÖFWVæFVçB&÷w2âÀ§ÂæòVæ–çFVæFVBV&Æ–2Ö6öçG&7BÂFWÆ÷–ÖVçBÂÖ–w&F–öâÂFF&6R×w&—FRÂ÷"W‡FW&æÂ×7—7FVÒ6†ævRÂ&÷fVB–×ÆVÖVçFF–öâÆâÂ*u"Ób&–Ç2÷7GW&RæBW†6ÇW6–öç3²cFFVæF"ã^(	3"ã#æöæ6Æ–×2Â"Ô6†ævVB–çFW&æÂD"öWf–FVæ6R&6†—FV7GW&S²õ2Ó2v2&÷VæFVB&VBÖöæÇ“²"Ô"W&f÷&ÖVBWf–FVæ6RFÖ—76–öâöæÇ’âÂæòÆFW"'VçF–ÖR6†ævRW†—7G2âV&Æ–2&VFW"ô4Ä’'—FW2vW&Ræ÷BW‡æFVBÂæòFWÆ÷–ÖVçB÷"Ö–w&F–öâv2W&f÷&ÖVBÂæB"Ô"ÖFRæòFF&6R÷"fVæF÷"6ÆÂâÂ6F—6f–VBâÂ7W÷'G2F†R6ö×ÆWFR"Ób&÷VæF'’âÀ ¤æòö&Æ–vF–öâ—2æ÷B6F—6f–VF÷"Væ6ÆV&à ¢222¢¥fÆ–FF–öâæBWf–FVæ6R&Wf–Wr¢  §ÂfÆ–FF–öâ÷"Wf–FVæ6R—FVÒÂÆ–6&ÆR6÷W&6R7FFRÂ&W7VÇBÂ7W'&VçB&VÆWfæ6RÂWf–FVæ6RÂ6Æ÷7W&RVffV7BÀ§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§Â"Â33cr&Wf–WrF‡&VG2Âf–æÂ†VBs6CcrââæÂ52Â7W'&VçC²ÆÂF‡&VG2&W6öÇfVB&Vf÷&RÖW&vRæBæò&Wf–WvVB–×ÆVÖVçFF–öâf–ÆRÆFW"6†ævVBâÂf—fR&Wf–WrF‡&VG2&W6öÇfVBÂ–æ6ÇVF–ær&VÂ×v†VVÂVçG'—ö–çBÂ6÷W&6R—6öÆF–öâÂæÖTW'&÷"ÂæB6†V6²Öæ÷B×&W—"f–æF–æw2âÂFöW2æ÷B&Æö6²âÀ§ÂW†7BÖ†VBv—D‡V"7F–öç2Â†VBs6CcrââæÂ'Vâ3scSƒ“#6Â52Â7W'&VçB&V6W6RöæÇ’c6†ævVBgFW"ÖW&vRâÂ6WfVâöb6WfVâ¦ö'27V66VVFVC²"ÖWFFF&V6÷&G2Wf–FVæ6Rôõ2cRócRæBF—&V7B÷7Fw&U5Â6öçG&7B#Só#SâÂFöW2æ÷B&Æö6²âÀ§ÂVçf—&öæÖVçB×–âfÆ–FF–öâÂW†7B"†VBæB7W'&VçBVæ6†ævVBWf–FVæ6RÂ52Â7W'&VçBâÂv—D‡V"7F–öç2&âv—F‚Ä5ôÄÃÔ6ÂÄäsÔ6ÂE£ÕUD6Â4dUôÔôDSÓÂÄÄõuôäUEtõ$³Ó²7W'&VçBVçb×–ç2'F–f7B&V6÷&G27V66W72âÂ7W÷'G2„DRÔD•5CRãâÀ§ÂW‡FW&æÂ&VÆV6RGFW7FF–öâÂW†7B"†VBs6CcrââæÂ52Â7W'&VçBâF†RÆFW"cÖöæÇ’6öÖÖ—BFöW2æ÷BÇFW"F†RGFW7FVB6÷W&6RöWf–FVæ6R7FFRâÂW†7B6÷W&6RÂG&6¶VB×G&VRF–vW7BÂÖæ–fW7BÖFW&—fVB&VÆV6R”BÂ&VÂv†VVÂ–ç7FÆÆF–öâÂ#e%ô%ôd”äÅõ56Â—VÆ–æU÷7F÷ÖçVÆÆÂfÆ–B6VÆbÖ†6‚âÂ7W÷'G2ãfÂãRãÂãRã&âÀ§Âæ–æWFVVâ×7FvR7W'&VçB6æ—G’ÆörÂf–æÂÖW&vVBö7W'&VçBWf–FVæ6R'—FW2Â52Â7W'&VçBâÂW†7FÇ’æ–æWFVVâô¶7FvW3²7FvR"†—7F÷&–6ÂÖöæÇ“²æòf–ÆVB7FvS²7VÖÖ'“¥56âÂ7W÷'G2ãfæB&WfÆ–FFW2ÆÂÖVB&÷w2âÀ§ÂF—&V7B×6VÆV7F–öâ'F–f7BæB66†VÖÂf–æÂÖW&vVBö7W'&VçBWf–FVæ6R'—FW2Â52Â7W'&VçBâÂ&WV—&VBf÷W"66W2ÂW†7B&WF—&VB&÷7FW"Â52&VF–6FW2Â7G&–7B6Æ÷6VB66†VÖÂ6–&Æ–ær&ööbâÂ7W÷'G2ãFÂã–âÀ§Âõ2Ó26¶WBæB–æFWVæFVçBfÆ–FF–öâÂ6÷W&6RÖ&÷VæBõ26GW&RÇW2f–æÂFÖ—76–öâÂ52Â7W'&VçC²æò6¶WB&–Ö'’6†ævVBGW&–ær"Ô"÷"gFW'v&BâÂ6GW&U÷&W7VÇCÕ56Â¦W&ò5Âw&—FW2Â¦W&ò&WG&–W2Â¦W&òÇFW&æFR×&÷f–FW"GFV×G2Â6ö×ÆWFRæöæ6Æ–×2ÂfÆ–B6†V6·7V×2æBfÆ–FF–öâ&V6V—BâÂ7W÷'G2ãFÂã–âÀ§ÂWf–FVæ6RWFFW"Â–æFW‚ÂÖ—'&÷"Â6VçF–æVÇ2ÂæB÷&–VçFF–öâÂf–æÂÖW&vVBö7W'&VçBWf–FVæ6R'—FW2Â52Â7W'&VçBâÂWFFW"6†V6²ÂF‚fÆ–FF–öâÂÖ—'&÷"66†VÖÂ–æFW‚ôÖ—'&÷"†6‚6†V6·2ÂSC‚×&÷r÷&–VçFF–öâ7FGW3¢ö¶âÂ7W÷'G2ãRã&æBÆÂv÷fW&æVBWf–FVæ6R6Æ–×2âÀ§Â&öG”w&‚6÷W&6RæBöÆ–7’fÖ–Ç’Â"ÓB–×ÆVÖVçFF–öâÂ&WfÆ–FFVB'’f–æÂ7FvR’Â52Â7W'&VçC²f–æÂGFW7FF–öâ–æ6ÇVFW27W'&VçB'F–f7B†6†W2âÂ6÷W&6R6VÆV7F–öâ6Æ÷6W2fVæF÷"G&ç7÷'BVæFW"6Æ÷6VB&–Ç3²6÷W&6R–çf&–æ6RW6W2F—7F–æ7BD"÷fVæF÷"&W&W6VçFF–öç2Â6ÖRæ÷&ÖÆ—¦VB–çWBÂWVÂ&ö¦V7F–öâöVÖ—GFVB'—FW2ÂGvò×'Vâ7F&–Æ—G’ÂæB&V¦V7FVBæVvF—fR6öçG&öÃ²EDÂõ5u"Â&FRÖÆ–Ö—BÂ6—&7V—BÖ'&V¶W"ÂÖWG&–72ÂæB¶W—2ÖöæÇ’Wf–FVæ6R&R7W'&VçBâÂ7W÷'G2ãVâÀ§Â&6†—FV7GW&R6æ6†÷BÂ"ÓB–×ÆVÖVçFF–öâÂ&WfÆ–FFVB'’f–æÂ7FvRÂ52Â7W'&VçC²6æ6†÷B–æ6ÇVFW27W'&VçBF—&V7BÖöæÇ’ÖöGVÆW2æB&W÷'G2æÇ—¦W%÷fW&F–7C×76âÂ7W'&VçBv÷fW&æVB¶W—2ÖöæÇ’'F–f7BæB66†VÖÂf–æÂf—†VB×ö–çB6†V6²ÂæòÆFW"6†ævRâÂ7W÷'G2ãâÀ§ÂÆö6ÂÖVBÖ66†RWf–FVæ6RÂ"ÓR–×ÆVÖVçFF–öâÂ&WfÆ–FFVB'’f–æÂ7FvRÂ52Â7W'&VçBâÂÖæ–fW7B7FGW253²ÖVBw&—FR÷&VBÖ&6²&—G’Â–FV×÷FVæ6RÂæò&rfVæF÷"W'6—7FVæ6RÂ6Æ÷6VB×&–Ç2¦W&ò’ôòÂæ÷&ÖÆ—¦VB6–ævÆR×&÷r–FVçF—G’ÂæB&öGV7F–öâÖÆ–¶R&VgW6ÂÆÂG'VRâÂ7W÷'G2ãâÀ§Âõ2Ó"ÖVBÖ66†R6¶WBÂ66WFVB†—7F÷&–6ÂW†V7WF–öâÂ&WfÆ–FFVB'’f–æÂ7FvR2Â52Â7W'&VçC²æ÷B&W'VâÂæB—G2FÖ—GFVB'—FW2&VÖ–âVæ6†ævVBâÂ&W7VÇB7VÖÖ'’53²W†7FÇ’öæRfVæF÷"&WVW7C²ÖVB–ÆöBöæÇ“²&—G’Â–FV×÷FVæ6RÂ&VgW6ÂÂæB&WF–æVBÖ'’Õò&VF–6FW2G'VRâÂ7W÷'G2ãâÀ§Â7W'&VçB×F—F—fW&vVæ6R&Wf–WrÂÖW&vRF#3RââæFòÖ–äs–CBââæÂ52Â7W'&VçBâÂöæR–çFW'fVæ–ærcÖöæÇ’f–ÆR6†ævS²æò6öFRöWf–FVæ6R÷v÷&¶fÆ÷r÷66†VÖ÷FW7BF—fW&vVæ6RâÂ†—7F÷&–6ÂfÆ–FF–öâ—2æ÷B7FÆRâÀ ¤æò&WV—&VBfÆ–FF–öâ—2d”ÆÂäõB%TæÂ”ä4ôä4ÅU4•dVÂ÷"äõBd”Ä$ÄVà ¢222¢¥c’&÷r6Æ÷7W&R76W76ÖVçB¢  ¢¢¥c’&÷s¢„DRÔD•5CRã¢  ¢¢¢¤W†7B7W'&VçBF—FÆRæB7FGW3¢¢¢6æöæ–6ÂVæ6öF–æw2bVçf—&öæÖVçB–ç6(	B'F–Æâ ¢¢¢¤÷&–v–æÂ"ÓbÖ–æs¢¢¢"Óò"Óbâ ¢¢¢¤Æ–6&ÆRÆFW"cÖVæFÖVçC¢¢¢æò&÷r×7V6–f–26VÖçF–2ÖVæFÖVçBâFFVæGVÒ"ã^(	—2æ–æWFVVâ×7FvR÷&FW"v÷fW&ç2F†Rf–æÂVçf—&öæÖVçBÂ6æöæ–6ÂÔ¥4ôâÂæBf–æÂÔÄb6†V6·2âFFVæGVÒ"ã#öÖ—GFVBF†—2&÷rg&öÒ—G27FGW2Æ—7Bâ ¢¢¢¤6ö×ÆWFR6Æ÷7W&R&VF–6FW3¢¢¢ ¢â'—FR×6Vç6—F—fR†&æW76W2W6RÄ5ôÄÃÔ6ÂÄäsÔ6ÂæBE£ÕUD6â ¢"â†6Rd’v÷fW&æVB¥4ôâ—26æöæ–6Ââ ¢2âFW‡BWf–FVæ6R—2Äb×FW&Ö–æFVBâ ¢BâVçf—&öæÖVçB×–âfÆ–FF–öâ76W2â ¢Râ6æöæ–6ÂÔ¥4ôâfÆ–FF–öâ76W2â ¢bâf–æÂÔÄbfÆ–FF–öâ76W2öâF†R6öÖÖ—GFVB7FFRâ ¢¢¢¥&VF–6FR&W7VÇG3¢¢¢ÆÂ6—‚52â ¢¢¢¤7W'&VçB&W÷6—F÷'’Wf–FVæ6S¢¢¢7W'&VçBVçb×–ç2'F–f7B&V6÷&G2F†R&WV—&VB–ç2æB7V66W73²6æ—G’7FvW2Â2ÂæB’73²W†7BÖ†VB4’76VB6æöæ–6Â¥4ôâæBf–æÂÔÄb6†V6·3²æòÆFW"Wf–FVæ6R6†ævRö67W'&VBâ ¢¢¢¥fÆ–FF–öâ7W÷'C¢¢¢W†7BÖ†VB4’ÇW2W‡FW&æÂGFW7FF–öâæB7W'&VçBf—†VB×ö–çB'F–f7G2â ¢¢¢¥&VÖ–æ–ærv¢¢¢c(	—2f—fR×&÷r–çfVçF÷'’öÖ—GFVBF†—26†&VB"Ób&÷râæò–×ÆVÖVçFF–öâÂWf–FVæ6RÂ÷"fÆ–FF–öâv&VÖ–ç2â ¢¢¢¥7FGW2&V6öÖÖVæFF–öã¢¢¢6†ævRFòFöæVâ ¢¢¢¤6Æ÷7W&R÷7GW&S¢¢¢6Æ÷7W&R7W÷'F&ÆRæ÷rF‡&÷Vv‚6W&FRc’Ö–çFVææ6Vâ ¢¢¢¥&WV—&VBæW‡B7F–öã¢¢¢FBF†R7FGW26†ævR–âF†RWF†÷&—¦VBc’Ö–çFVææ6R7F–öâæB&V6÷&BF†Bf–æÂ"Ób÷&6†W7G&F–öâ7WÆ–VBF†R&Wf–÷W6Ç’÷WG7FæF–ærvÆö&Â6öæf—&ÖF–öâà ¢¢¥c’&÷s¢„DRÔD•5CRã&¢  ¢¢¢¤W†7B7W'&VçBF—FÆRæB7FGW3¢¢¢vÆö&Â–æFW‚bÖ—'&÷"F—66—Æ–æV(	B'F–Æâ ¢¢¢¤÷&–v–æÂ"ÓbÖ–æs¢¢¢"Óò"Óbâ ¢¢¢¤Æ–6&ÆRÆFW"cÖVæFÖVçC¢¢¢FFVæGVÒ"ãR&WF–ç2WFFW"Â‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"Â6†V6·7VÒÂF‚×&ööbÂæB÷&–VçFF–öâF—66—Æ–æRæBFVf–æW2W†7B6ö×ÆWF–öâ&VF–6FW2â ¢¢¢¤6ö×ÆWFR6Æ÷7W&R&VF–6FW3¢¢¢ ¢âV6‚æWr&–Ö'’æB66†VÖ†2W†7FÇ’öæR‡VÖâ–æFW‚&÷râ ¢"âV6‚†2W†7FÇ’öæRÖ6†–æRÖ—'&÷"&÷râ ¢2âV6‚†2F†R6÷'&V7B6–&Æ–ærF‚&ööbâ ¢Bâ–æFW‚æBÖ—'&÷"†6†W2&R6ö†W&VçBâ ¢Râ†—7F÷&–6Â'&–FvR&–Ö&–W2&WF–âW†7B†6†W2â ¢bâæòGWÆ–6FR÷"÷'†â&÷rW†—7G2â ¢râæòÖçVÆÇ’w&—GFVâWFFW"Ö÷væVB6ö×æ–öâW†—7G2â ¢‚âæò–væ÷&VB&WV—&VB'F–f7B÷"66†VÖ÷F‚ö†6‚f–ÇW&RW†—7G2â ¢’âWFFW"&V6VFW2÷&–VçFF–öâÂæB&÷F‚6†V6·272â ¢¢¢¥&VF–6FR&W7VÇG3¢¢¢ÆÂæ–æR52â ¢¢¢¤7W'&VçB&W÷6—F÷'’Wf–FVæ6S¢¢¢SC‚×&÷r6ö†W&VçB÷&–VçFF–öâÂW†7BÖ†VBWFFW"ÒÖ6†V6¶ÂF‚fÆ–FF–öâÂÖ—'&÷"66†VÖö†6‚6†V6·2Â–æFW‚†6‚6†V6²Âf–æÂÔÄb6†V6²ÂæB&W6W'fVB†—7F÷&–6Â†6†W2â ¢¢¢¥fÆ–FF–öâ7W÷'C¢¢¢W†7BÖ†VB4’æB7W'&VçB÷&–VçFF–öâ'F–f7Bâ ¢¢¢¥&VÖ–æ–ærv¢¢¢7FGW2G&–ævRöæÇ’â ¢¢¢¥7FGW2&V6öÖÖVæFF–öã¢¢¢6†ævRFòFöæVâ ¢¢¢¤6Æ÷7W&R÷7GW&S¢¢¢6Æ÷7W&R7W÷'F&ÆRæ÷rF‡&÷Vv‚6W&FRc’Ö–çFVææ6Vâ ¢¢¢¥&WV—&VBæW‡B7F–öã¢¢¢WFFRF†Rc’7FGW2æBæ÷FW2–â6W&FRWF†÷&—¦VBÖ–çFVææ6R7F–öâà ¢¢¥c’&÷s¢„DRÔD•5CãF¢  ¢¢¢¤W†7B7W'&VçBF—FÆRæB7FGW3¢¢¢D"÷7GW&Rb'VçF–ÖR6†V6·2††&æW72f÷"„DRÔdU$ÓB–(	B'F–Æâ ¢¢¢¤÷&–v–æÂ"ÓbÖ–æs¢¢¢"ÓBòõ2Óò"Óbâ ¢¢¢¤Æ–6&ÆRÆFW"cÖVæFÖVçC¢¢¢FFVæF"ã"æB"ãR&VÖ÷fR7W'&VçB'&–FvRfÆÆ&6²æB&÷f–FW"×&—G’ö&Æ–vF–öç2â7W'&VçB6ö×ÆWF–öâÖVç2F—&V7B×&÷f–FW"6VÆV7F–öâÂ&WF—&VBÖ¶W’&VgW6ÂÂG—VBF—&V7Bf–ÇW&RÂ&VBÖöæÇ’F—&V7B÷7GW&RÂÆV7B&—f–ÆVvRÂ6V&6‚F‚ÂDDÂ–FVçF—G’&ö¦V7F–öâÂ6öç7G&–çG2Â&÷VæF'’f–Ww2Â'F—F–öâ÷7GW&RÂæBv÷fW&æVBWf–FVæ6R&–æF–ærâ ¢¢¢¤6ö×ÆWFR6Æ÷7W&R&VF–6FW3¢¢¢F†÷6RÆ—7FVB–âcFFVæGVÒ"ãRf÷"ãFâ ¢¢¢¥&VF–6FRÖ'’×&VF–6FR&W7VÇC¢¢¢ ¢¢æòW†V7WF&ÆR'&–FvRF‚–â7F—fR6÷W&6S¢52â ¢¢&WF—&VB¶W—2&VgW6R&Vf÷&R&÷f–FW"6öç7G'V7F–öâ÷"’ôó¢52â ¢¢F—&V7B×6VÆV7F–öâ&–Ö'’53¢52â ¢¢F—&V7B÷7GW&R&–Ö&–W27W'&VçBæB66†VÖ×fÆ–C¢52â ¢¢õ2Ó253¢52â ¢¢w&çG2æBÆV7B×&—f–ÆVvRö'6W'fF–öç3¢52â ¢¢6V&6‚Fƒ¢52â ¢¢DDÂ&ö¦V7F–öâæB6öç7G&–çG3¢52â ¢¢&÷VæF'’×f–WræB'F—F–öâö'6W'fF–öç3¢52â ¢¢6V7&WBfÇVW2'6VçC¢52â ¢¢&WV—&VBF‡2–æFW†VBæBÖW&vV&ÆS¢52â ¢¢¢¤7W'&VçB&W÷6—F÷'’Wf–FVæ6S¢¢¢7W'&VçBF—&V7BÖöæÇ’FFW"÷&÷f–FW#²F—&V7B×6VÆV7F–öâ6æ6†÷C²õ2Ó26¶WBæB&V6V—C²f–æÂ–æFW‚ôÖ—'&÷"&–æF–æw2â ¢¢¢¥fÆ–FF–öâ7W÷'C¢¢¢F—&V7B÷7Fw&U5Â6öçG&7B7V—FRÂWf–FVæ6Rôõ27V—FRÂ7FvRrÂ7FvR‚Â7FvRBÂæBf–æÂGFW7FF–öââ ¢¢¢¥&VÖ–æ–ærv¢¢¢7W'&VçBc’FW‡B7F–ÆÂFW67&–&W2'&–FvRfÆÆ&6²÷&÷f–FW"×&—G’2'BöbF†R6VÖçF–2†öÖRæB'F–f7B÷7GW&Râ ¢¢¢¥7FGW2&V6öÖÖVæFF–öã¢¢¢6†ævRFòFöæVâ ¢¢¢¤6Æ÷7W&R÷7GW&S¢¢¢6Æ÷7W&R7W÷'F&ÆRgFW"–FVçF–f–VBW&ÖæVçBÖ6æöâ÷"c’v÷&F–ærÖ–çFVææ6Vâ ¢¢¢¥&WV—&VBæW‡B7F–öã¢¢¢–âF†R6ÖRc’Ö–çFVææ6R7F–öâÂf—'7B&WÆ6RF†Rö'6öÆWFR'&–FvRÆæwVvRv—F‚F†RFFVæGVÒ"ãRF—&V7BÖöæÇ’ÖVæ–ærÂF†Vâ&V6÷&BFöæVà ¢¢¥c’&÷s¢„DRÔD•5CãV¢  ¢¢¢¤W†7B7W'&VçBF—FÆRæB7FGW3¢¢¢&öG”w&‚ÖV6†æ–72vFW6(	B'F–Æâ ¢¢¢¤÷&–v–æÂ"ÓbÖ–æs¢¢¢"ÓBò"Óbâ ¢¢¢¤Æ–6&ÆRÆFW"cÖVæFÖVçC¢¢¢FFVæGVÒ"ãB&÷fVBF†R6÷W&6RÖæWWG&Â&ö¦V7F–öâ&÷VæF'’æBc"6÷W&6RÖ–çf&–æ6RWf–FVæ6RâF—&V7BÖöæÇ’"Ób&VÖVF–F–öâF–Bæ÷B&V÷VâF†R&öG”w&‚6öçG&7Bâ ¢¢¢¤6ö×ÆWFR6Æ÷7W&R&VF–6FW3¢¢¢ ¢â6÷W&6R×6VÆV7F–öâWf–FVæ6R—27W'&VçBâ ¢"âF—7F–æ7BD"æBfVæF÷"&W&W6VçFF–öç2&–æBFòF†R6ÖRæ÷&ÖÆ—¦VB–çWBâ ¢2â6æöæ–6Â&ö¦V7F–öç2&RWVÂâ ¢Bâ6†&VB&W6VçFW"'—FW2&RWVÂâ ¢RâD"æBfVæF÷"Gvò×'Vâ7F&–Æ—G’†öÆG2â ¢bâæVvF—fR6÷W&6RF—fW&vVæ6R—2&V¦V7FVBâ ¢râVç6fRf–VÆG2&R'6VçBâ ¢‚âfVæF÷"G&ç7÷'B&VgW6W2VæFW"6Æ÷6VB&–Ç2v—F‚¦W&ò6ÆÇ2â ¢’âEDÂõ5u"öÆ–7’ÖF6†W2F†Rv÷fW&æVB6æ6†÷Bâ ¢â&FRÖÆ–Ö—BöÆ–7’ÖF6†W2â ¢â6—&7V—BÖ'&V¶W"öÆ–7’ÖF6†W2â ¢"âÖWG&–72æB¶W—2ÖöæÇ’Wf–FVæ6R&R&W6VçBæBv÷fW&æVBâ ¢¢¢¥&VF–6FR&W7VÇG3¢¢¢ÆÂGvVÇfR52â ¢¢¢¤7W'&VçB&W÷6—F÷'’Wf–FVæ6S¢¢¢7W'&VçB6÷W&6RÖ–çf&–æ6R7VÖÖ'’†2WfW'’&VF–6FRG'VRæB7V66W76gVÂæVvF—fR&V6V—C²6÷W&6R×6VÆV7F–öâÂ&Vg&W6‚×öÆ–7’ÂÖWG&–72ÂæB¶W—2ÖöæÇ’'F–f7G2&VÖ–â7W'&VçBæB&R–æ6ÇVFVB–âF†Rf–æÂGFW7FF–öââ ¢¢¢¥fÆ–FF–öâ7W÷'C¢¢¢f–æÂ—VÆ–æR7FvR’Â7W'&VçBvVæW&F÷"ÒÖ6†V6¶Â&öG”w&‚&ö¦V7F–öâ÷öÆ–7’FW7G2ÂæBW‡FW&æÂGFW7FF–öââ ¢¢¢¥&VÖ–æ–ærv¢¢¢cž(	—2Fö¶VâÆ—7B7F–ÆÂ–æ6ÇVFW2&WF—&VBDUeôD%ô%$”DtUôdÄÄ$4µôô¶Âv†–6‚cFFVæGVÒ"ã"Ö¶W2æöæ6Æ–Ö&ÆRâF†Rö'6öÆWFRFö¶Vâ6†÷VÆBæ÷B&VÖ–âGF6†VBFòæWvÇ’6Æ÷6VB&÷râ ¢¢¢¥7FGW2&V6öÖÖVæFF–öã¢¢¢6†ævRFòFöæVâ ¢¢¢¤6Æ÷7W&R÷7GW&S¢¢¢6Æ÷7W&R7W÷'F&ÆRgFW"–FVçF–f–VBW&ÖæVçBÖ6æöâ÷"c’v÷&F–ærÖ–çFVææ6Vâ ¢¢¢¥&WV—&VBæW‡B7F–öã¢¢¢&VÖ÷fRF†R&WF—&VB'&–FvRFö¶Vâg&öÒF†R&÷~(	—2Fö¶VâÆ—7B÷"Ö&²—B†—7F÷&–6ÂÂF†Vâ&V6÷&BFöæV–âF†R6ÖRc’Ö–çFVææ6R7F–öâà ¢¢¥c’&÷s¢„DRÔD•5Cãf¢  ¢¢¢¤W†7B7W'&VçBF—FÆRæB7FGW3¢¢¢öæRÖ'WGFöâWf–FVæ6R†&æW72b&VÆV6R6æ—G’—VÆ–æV(	B'F–Æâ ¢¢¢¤÷&–v–æÂ"ÓbÖ–æs¢¢¢"Óbâ ¢¢¢¤Æ–6&ÆRÆFW"cÖVæFÖVçC¢¢¢FFVæGVÒ"ãR&WÆ6W2F†R÷&–v–æÂ6WfVçFVVâ×7FvRö'&–FvRÖFWVæFVçB÷&6†W7G&F–öâv—F‚F†RW†7BF—&V7BÖöæÇ’æ–æWFVVâ×7FvR÷&FW"âFFVæGVÒ"ãbFG2Öæ–fW7BÖFW&—fVB&VÆV6R–FVçF—G’æBW†7B×6÷W&6RW‡FW&æÂGFW7FF–öââ ¢¢¢¤6ö×ÆWFR6Æ÷7W&R&VF–6FW3¢¢¢F†÷6RÆ—7FVB–âFFVæGVÒ"ãRf÷"ãfâ ¢¢¢¥&VF–6FRÖ'’×&VF–6FR&W7VÇC¢¢¢ ¢¢æ–æWFVVâÖæFF÷'’7FvW2&W6VçC¢52â ¢¢W†7B÷&FW#¢52â ¢¢æò6¶—VB&WV—&VB7FvS¢52â ¢¢W‡V7FVB7V66W726öFRf÷"WfW'’7FvS¢52â ¢¢7F÷2öâf—'7Bf–ÇW&S¢52â ¢¢æòõ2W†V7WF–öâ÷"W‡FW&æÂ’ôó¢52â ¢¢7W'&VçBæB†—7F÷&–6ÂWf–FVæ6R6VÖçF–726W&FVC¢52â ¢¢6æöæ–6Â¥4ôã¢52â ¢¢FWFW&Ö–æ—6Ó¢52â ¢¢&–Ç3¢52â ¢¢WFFW"6†V6³¢52â ¢¢Wf–FVæ6R×F‚fÆ–FF–öã¢52â ¢¢–æFW‚ôÖ—'&÷"†6‚æB66†VÖ6†V6·3¢52â ¢¢F÷öÆöw“¢52â ¢¢f–æÂÄc¢52â ¢¢W†7B×6÷W&6R6¶vVBÖVçG'—ö–çBGFW7FF–öã¢52â ¢¢¢¤7W'&VçB&W÷6—F÷'’Wf–FVæ6S¢¢¢f–æÂ6æ—G’ÆörÂvFR6÷W&6RÂW†7BÖ†VB4’ÂæBW‡FW&æÂGFW7FF–öââ ¢¢¢¥fÆ–FF–öâ7W÷'C¢¢¢ÆÂ6WfVâW†7BÖ†VB¦ö'2æBW‡FW&æÂGFW7FF–öââ ¢¢¢¥&VÖ–æ–ærv¢¢¢c’7F–ÆÂæÖW2F†RöÆFW"G&ç67&—BF‚æBöÆFW"—VÆ–æRFW67&—F–öââF†R7W'&VçB6æöæ–6Â7W&f6R—2VF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆövÂv—F‚æ–æWFVVâ7FvW2æBW†7BÖ†VBW‡FW&æÂGFW7FF–öââ ¢¢¢¥7FGW2&V6öÖÖVæFF–öã¢¢¢6†ævRFòFöæVâ ¢¢¢¤6Æ÷7W&R÷7GW&S¢¢¢6Æ÷7W&R7W÷'F&ÆRgFW"–FVçF–f–VBW&ÖæVçBÖ6æöâ÷"c’v÷&F–ærÖ–çFVææ6Vâ ¢¢¢¥&WV—&VBæW‡B7F–öã¢¢¢WFFRF†Rc’Wf–FVæ6RF‚æB7W'&VçB7FvRöFWVæFVæ7’v÷&F–ærÂF†Vâ&V6÷&BFöæV–âF†R6ÖRc’Ö–çFVææ6R7F–öâà ¢¢¥c’&÷s¢„DRÔD•5Cã–¢  ¢¢¢¤W†7B7W'&VçBF—FÆRæB7FGW3¢¢¢D.(	6'&–FvR&—G’bVçb6öææV7F—f—G–(	B'F–Æâ ¢¢¢¤÷&–v–æÂ"ÓbÖ–æs¢¢¢"ÓBòõ2Óò"Óbâ ¢¢¢¤Æ–6&ÆRÆFW"cÖVæFÖVçC¢¢¢FFVæGVÒ"ãR&VæÖW2æB&VFVf–æW2F†R&÷r2F—&V7BFF&6R6öææV7F—f—G’b&WF—&VB×G&ç7÷'BVæf÷&6VÖVçFâ ¢¢¢¤6ö×ÆWFR6Æ÷7W&R&VF–6FW3¢¢¢F†÷6RÆ—7FVB–âFFVæGVÒ"ãRf÷"ã–â ¢¢¢¥&VF–6FRÖ'’×&VF–6FR&W7VÇC¢¢¢ ¢¢ÖVæFVBF—&V7BÖ6öææV7F—f—G’v÷&F–ærF÷FVB2F†R6öçG&öÆÆ–ærÆ—fRÖVæ–æs¢52–âc²æ÷B–WBG&–æVB–çFòc’â ¢¢†VÇF‡’F—&V7B6VÆV7F–öâF‡&÷Vv‚7–6÷s¢52â ¢¢Ö—76–ærF—&V7B66W72f–Ç26Æ÷6VC¢52â ¢¢Væf–Æ&ÆRF—&V7B66W72f–Ç26Æ÷6VC¢52â ¢¢V6‚&WF—&VB¶W’Â–æ6ÇVF–ærV×G’fÇVRÂ&VgW6W2&Vf÷&R&÷f–FW"GFV×C¢52â ¢¢ÇFW&æFR×&÷f–FW"GFV×G2WVÂ¦W&ó¢52â ¢¢õ2Ó2&÷fW2&÷VæFVBF—&V7B&VBÖöæÇ’÷7GW&S¢52â ¢¢DDÂ6Æ–Ò—2Æ–Ö—FVBFò†FRæFFÅö–FVçF—G•÷&ö¦V7F–öâçc¢52â ¢¢æò7W'&VçB'&–FvR&—G’öfÆÆ&6²6Æ–Ò&VÖ–ç3¢52â ¢¢7W'&VçBÆö6ÂæBõ2Wf–FVæ6R—2v÷fW&æVBæB–æFW†VC¢52â ¢¢¢¤7W'&VçB&W÷6—F÷'’Wf–FVæ6S¢¢¢F—&V7BFFW"÷&÷f–FW"ÂF—&V7B×6VÆV7F–öâ6æ6†÷BÂõ2Ó26¶WBÂ†—7F÷&–6Â'&–FvR6Æ76–f–W"Âf–æÂWFFW"&–æF–æw2ÂæB7FvR"óB6W&F–öââ ¢¢¢¥fÆ–FF–öâ7W÷'C¢¢¢F—&V7BÖ6öçG&7BFW7G2ÂWf–FVæ6Rôõ2FW7G2ÂW†7BÖ†VB4’Âf–æÂGFW7FF–öââ ¢¢¢¥&VÖ–æ–ærv¢¢¢F†R7W'&VçBc’F—FÆRæB&öG’7F–ÆÂFVf–æRF†R&WF—&VB'&–FvR×&—G’6öçG&7Bâ ¢¢¢¥7FGW2&V6öÖÖVæFF–öã¢¢¢6†ævRFòFöæVâ ¢¢¢¤6Æ÷7W&R÷7GW&S¢¢¢6Æ÷7W&R7W÷'F&ÆRgFW"–FVçF–f–VBW&ÖæVçBÖ6æöâ÷"c’v÷&F–ærÖ–çFVææ6Vâ ¢¢¢¥&WV—&VBæW‡B7F–öã¢¢¢&VæÖRæB&WÆ6RF†R&÷~(	—2'&–FvRÖW&FW67&—F–öâÂ'F–f7BW‡V7FF–öç2ÂæBFö¶Vç2v—F‚F†RF—&V7BÖöæÇ’ÖVæ–ærÂF†Vâ&V6÷&BFöæV–âF†R6ÖRWF†÷&—¦VBc’Ö–çFVææ6R7F–öâà ¢¢¥c’&÷s¢„DRÔD•5Cã¢  ¢¢¢¤W†7B7W'&VçBF—FÆRæB7FGW3¢¢¢&6†—FV7GW&R6æ6†÷B†¶W—2ÖöæÇ’’Wf–FVæ6V(	B'F–Æâ ¢¢¢¤÷&–v–æÂ"ÓbÖ–æs¢¢¢"ÓBò"Óbâ ¢¢¢¤Æ–6&ÆRÆFW"cÖVæFÖVçC¢¢¢FFVæGVÒ"ãB6÷'&V7FVBæÇ—¦W"F—66÷fW'’ÂF†öæö×’ÂVæ¶æ÷vâ†æFÆ–ærÂæBfW&F–7BFW&—fF–öââF—&V7BÖöæÇ’&VÖVF–F–öâF–Bæ÷B&V÷VâF†—2&÷râ ¢¢¢¤6ö×ÆWFR6Æ÷7W&R&VF–6FW3¢¢¢ ¢âv÷fW&æVB&6†—FV7GW&R6æ6†÷BW†—7G2â ¢"â6æ6†÷B—26æöæ–6Â¥4ôâæBöæRÔÄbâ ¢2â6æ6†÷B—2¶W—2ÖöæÇ’æB6V7&WB÷–ÆöB6fRâ ¢BâæÇ—¦W"F—66÷fW'27W'&VçB&÷VæFVBÆö6’â ¢Râ6Æ76–f–6F–öâæB&V6öâ6öFW2&R&W6VçBâ ¢bâfW&F–7B—2FW&—fVBg&öÒf–æF–æw2æBWVÇ252â ¢râ66†VÖæBWf–FVæ6R&–æF–æw2&R7W'&VçBâ ¢‚âf–æÂ—VÆ–æR&WfÆ–FFW2F†R6æ6†÷Bâ ¢¢¢¥&VF–6FR&W7VÇG3¢¢¢ÆÂV–v‡B52â ¢¢¢¤7W'&VçB&W÷6—F÷'’Wf–FVæ6S¢¢¢7W'&VçB6æ6†÷B–æ6ÇVFW2&W6VçBF—&V7BÖöæÇ’D"ÖöGVÆW2æB&W÷'G2æÇ—¦W%÷fW&F–7C×76²7FvRæBW†7BÖ†VBFW7G276VC²æòÆFW"'F–f7B6†ævRö67W'&VBâ ¢¢¢¥fÆ–FF–öâ7W÷'C¢¢¢&6†—FV7GW&R6æ6†÷BFW7G2Âf–æÂ—VÆ–æR7FvRÂWFFW"÷F‚6†V6·2ÂW‡FW&æÂGFW7FF–öââ ¢¢¢¥&VÖ–æ–ærv¢¢¢7FGW2G&–ævRöæÇ’â ¢¢¢¥7FGW2&V6öÖÖVæFF–öã¢¢¢6†ævRFòFöæVâ ¢¢¢¤6Æ÷7W&R÷7GW&S¢¢¢6Æ÷7W&R7W÷'F&ÆRæ÷rF‡&÷Vv‚6W&FRc’Ö–çFVææ6Vâ ¢¢¢¥&WV—&VBæW‡B7F–öã¢¢¢&V6÷&BF†R7FGW26†ævRæB7W'&VçB'F–f7BF‚–âF†R6W&FVÇ’WF†÷&—¦VBc’Ö–çFVææ6R7F–öâà ¢¢¥c’&÷s¢„DRÔD•5Cã¢  ¢¢¢¤W†7B7W'&VçBF—FÆRæB7FGW3¢¢¢c"ÖVBÖ66†RW'6—7FVæ6R†&FVæ–æv(	B÷F–öæÆâ ¢¢¢¤÷&–v–æÂ"ÓbÖ–æs¢¢¢"ÓRòõ2Ó"ò"Óbâ ¢¢¢¤Æ–6&ÆRÆFW"cÖVæFÖVçC¢¢¢FFVæGVÒ"ãR&WF–ç2F†R6öæf–wW&VB×c"ÖVBÖ66†RÖVæ–ærÂ&W6W'fW2Æö6ÂæBõ2Ó"Wf–FVæ6RÂæB&WÆ6W2'&–FvR×7V6–f–2æòÔ’ôòFWVæFVæ6–W2v—F‚G&ç7÷'BÖæWWG&ÂwV&G2â ¢¢¢¤6ö×ÆWFR6Æ÷7W&R&VF–6FW3¢¢¢F†÷6RÆ—7FVB–âFFVæGVÒ"ãRf÷"ãâ ¢¢¢¥&VF–6FRÖ'’×&VF–6FR&W7VÇC¢¢¢ ¢¢Æö6ÂÖVBÖ66†RfÆ–FF÷"53¢52â ¢¢õ2Ó"fÆ–FF÷"53¢52â ¢¢FFW"ÖÖVBFFöæÇ“¢52â ¢¢6æöæ–6Âw&—FR÷&VBÖ&6²&—G“¢52â ¢¢–FV×÷FVçB&WVFVBw&—FS¢52â ¢¢æ÷&ÖÆ—¦VB6–ævÆR×&÷r–FVçF—G“¢52â ¢¢æò&rfVæF÷"–ÆöBW'6—7FVæ6S¢52â ¢¢6V7&WB6fWG“¢52â ¢¢6Æ÷6VB×&–Ç2¦W&ò’ôó¢52â ¢¢&öGV7F–öâÖÆ–¶R&VgW6Ã¢52â ¢¢Æö6ÂvVæW&F÷"–×÷'G2æò&WF—&VB&÷f–FW#¢52â ¢¢Æö6ÂWf–FVæ6RW&f÷&×2æòÆ—fR&÷f–FW"÷fVæF÷"6ÆÃ¢52â ¢¢7W'&VçBWf–FVæ6R&–æF–æw26ö×ÆWFS¢52â ¢¢¢¤7W'&VçB&W÷6—F÷'’Wf–FVæ6S¢¢¢7W'&VçBÆö6ÂÖæ–fW7B—252v—F‚ÆÂ&WV—&VB&VF–6FW3²õ2Ó"&W7VÇB7VÖÖ'’—252v—F‚F†R&÷fVB&÷VæFVBWF†÷&—¦F–öç2æB6ö×ÆWFR&VF–6FW2â ¢¢¢¥fÆ–FF–öâ7W÷'C¢¢¢f–æÂ7FvW2æB2ÂÆö6ÂæBõ2Ó"fÆ–FF÷'2ÂW†7BÖ†VB4’ÂæBGFW7FF–öââ ¢¢¢¥&VÖ–æ–ærv¢¢¢c’7F–ÆÂFW67&–&W2F†R&÷r2gWGW&RW–2VæF–ærWF†÷&—¦F–öâæB–æ6ÇVFW2&RÖ–×ÆVÖVçFF–öâæöæ6Æ–×2âF†B&V6÷&B—2æ÷r7FÆRâ ¢¢¢¥7FGW2&V6öÖÖVæFF–öã¢¢¢6†ævRFòFöæVâ ¢¢¢¤6Æ÷7W&R÷7GW&S¢¢¢6Æ÷7W&R7W÷'F&ÆRgFW"–FVçF–f–VBW&ÖæVçBÖ6æöâ÷"c’v÷&F–ærÖ–çFVææ6Vâ ¢¢¢¥&WV—&VBæW‡B7F–öã¢¢¢&WÆ6RF†RgWGW&R÷VæF–ærv÷&F–ærv—F‚F†R–×ÆVÖVçFVB„DRÔU”33‚&÷VæFVB÷7GW&RÂ&W6W'fRF†R&öGV7F–öâ×w&—FRæöæ6Æ–ÒÂæB&V6÷&BFöæVà ¢222¢¥&VÖ–æ–ærv÷&²¢  ¢¢£Ââ÷7BÖÖW&vR&W÷6—F÷'’ÂWf–FVæ6RÂ÷"fÆ–FF–öâ&VÖVF–F–öâ¢  ¤æöæRà ¤æò7W'&VçB6öFRFVfV7BÂv÷fW&æVBÖWf–FVæ6RFVfV7BÂfÆ–FF–öâFVf–6—BÂ7FÆR–×ÆVÖVçFF–öâ'F–f7BÂVç6fR&V†f–÷"Â÷"÷7BÖÖW&vR&Vw&W76–öâ&WV—&W2æWr&VÖVF–F–öâF6²à ¢¢£%ÂâW&ÖæVçBbÔ6æöâG&–ævR¢  ¥W&ÖæVçBFö7VÖVçFF–öâG&–ævR&VÖ–ç2Â'WB—B—2æ÷B&W÷6—F÷'’×&VÖVF–F–öâ÷"c’Ö6Æ÷7W&R&W&WV—6—FR&V6W6RcW‡Æ–6—FÇ’v÷fW&ç2F†W6RW†7BÆ—fRF÷–72VçF–ÂG&–ævRà ¥&WV—&VBG&–ævR–æ6ÇVFW3  ¢¢¢¥cr(	BvÆ÷r–æg&7G'V7GW&S¢¢¢&VÖ÷fR7F—fRrÖ'&–FvVæB'&–FvRÖfÆÆ&6²–æg&7G'V7GW&R6VÖçF–73²&WF–â'&–FvR&VfW&Væ6W2öæÇ’2†—7F÷'’â ¢¢¢¥cB(	B„DRÖV6†æ–72wV–FS¢¢¢&WÆ6R7F—fR'&–FvR÷&÷f–FW"×&—G’ÖV6†æ–72v—F‚F—&V7BÖöæÇ’6VÆV7F–öâÂ&WF—&VBÖ¶W’&VgW6ÂÂ7W'&VçBF—&V7BWf–FVæ6RÂæB†—7F÷&–6ÂÖ–çFVw&—G’fÆ–FF–öââ ¢¢¢¥cB(	B„DRv÷fW&ææ6S¢¢¢&WF—&R7W'&VçB6Æ–Ö&–Æ—G’öb'&–FvRÖöæÇ’Fö¶Vâ6VÖçF–72Â–æ6ÇVF–ærDUeôD%ô%$”DtUôdÄÄ$4µôô¶â ¢¢¢¥c"(	B„DR66†VÖ2æB'F–f7G3¢¢¢&V6÷&BF—&V7B×6VÆV7F–öâÂõ2Ó2Â†—7F÷&–6ÂÖ'&–FvR6Æ76–f–6F–öç2ÂW†7BWf–FVæ6RfÖ–Æ–W2Â6æöæ–6ÂWFFW"÷væW'6†—ÂæB÷'F&ÆRF‚×&ööb6VÖçF–72â ¢¢¢¥c’(	BvÆ÷rwV–FS¢¢¢G&–âW†7BÖ†VBW‡FW&æÂGFW7FF–öâÂ&VÂ6¶vVBÖVçG'—ö–çBfÆ–FF–öâÂFWFV7BÖæ÷B×&W—"4’÷7GW&RÂæB÷'F&ÆRF‚×&ööbfÆ–FF–öââ ¢¢ç’÷F†W"W†7BF&vWBÇ&VG’æÖVB'’cFFVæF"ã"F‡&÷Vv‚"ãbà ¢¢¥v÷&²6Æ76–f–6F–öã¢¢¢W&ÖæVçBbÔ6æöâG&–ævVà ¢¢£5Ââc6÷'&V7F–öâ÷"6öç6öÆ–FF–öâ¢  ¥Gvò&÷VæFVB6÷'&V7F–öç2&Rv'&çFVC  £â&WÆ6RFFVæGVÒ"ã#(	—27FFVÖVçBF†BÖ–äF#3Rââæ—27W'&VçBv—F‚F†RG'WF†gVÂF—7F–æ7F–öã¢ ¢¢f–æÂ&VÖVF–F–öâÖW&vS¢F#3Rââæ² ¢¢7W'&VçBÖ–æ¢s–CF&ââæ² ¢¢öæÇ’–çFW'fVæ–ær6†ævS¢cc"ãBFö7VÖVçFF–öââ £"â6Æ&–g’F†BF†Rf—fR×&÷rFFVæGVÒ"ãRó"ã#6WB—2F†R¢¦F—&V7BÖöæÇ’&VÖVF–F–öâ&VF–6FR6WB¢¢Âæ÷BF†R6ö×ÆWFR÷&–v–æÂ"Óbc’–çfVçF÷'’â&V6÷&BF†RF—7÷6—F–öâæB6Æ÷7W&R7W÷'Bf÷#¢ ¢¢„DRÔD•5CRã² ¢¢„DRÔD•5CãV² ¢¢„DRÔD•5Cãà ¥F†W6R6÷'&V7F–öç2Fòæ÷B&WV—&R–×ÆVÖVçFF–öâ÷"Wf–FVæ6R6†ævW2à ¢¢¥v÷&²6Æ76–f–6F–öã¢¢¢c6÷'&V7F–öâ÷"6öç6öÆ–FF–öæà ¢¢£EÂâc’v÷&F–æræB7FGW2Ö–çFVææ6R¢  ¤6W&FVÇ’WF†÷&—¦VBc’ãbÖ–çFVææ6R7F–öâÖ’&ö6VVBà ¤—B6†÷VÆC  ¢¢6†ævR„DRÔD•5CRãFòFöæVâ ¢¢6†ævR„DRÔD•5CRã&FòFöæVâ ¢¢ÖVæB„DRÔD•5CãFFòF—&V7BÖöæÇ’D"÷7GW&RæB6†ævR—BFòFöæVâ ¢¢&VÖ÷fR÷"†—7F÷&–6Æ—¦RF†R&WF—&VB'&–FvRFö¶Vâg&öÒ„DRÔD•5CãVæB6†ævR—BFòFöæVâ ¢¢WFFR„DRÔD•5CãfFòF†R6æöæ–6Âæ–æWFVVâ×7FvRÆöröGFW7FF–öâ÷7GW&RæB6†ævR—BFòFöæVâ ¢¢&VæÖRæB&VFVf–æR„DRÔD•5Cã–2F—&V7BFF&6R6öææV7F—f—G’b&WF—&VB×G&ç7÷'BVæf÷&6VÖVçFÂF†Vâ6†ævR—BFòFöæVâ ¢¢6†ævR„DRÔD•5CãFòFöæVâ ¢¢WFFR„DRÔD•5Cãg&öÒgWGW&R÷VæF–ærÆæwVvRFò—G2&÷VæFVB–×ÆVÖVçFVB÷7GW&RÂ&W6W'fRF†Ræò×&öGV7F–öâ×w&—FR&÷VæF'’ÂæB6†ævR—BFòFöæVà ¢¢¥v÷&²6Æ76–f–6F–öã¢¢¢c’v÷&F–ærÖ–çFVææ6VæBc’7FGW2Ö–çFVææ6Và ¢¢£UÂâ&ö6VGW&Â&Wf–Wr7F–öç2¢  ¤æöæRà ¤æògW'F†W"–×ÆVÖVçFF–öâ&Wf–WrÂõ2&W'VâÂWf–FVæ6R&V6GW&RÂ÷"&VÖVF–F–öâ&Wf–Wr—2æVVFVB&Vf÷&RF†Rc’Ö–çFVææ6R7F–öââF†Rc’Ö–çF–æW"6†÷VÆB7F÷æB&WGW&âf÷"&Wf–WröæÇ’–bF†RÖ–çFVææ6R6÷W&6RF–ffW'2ÖFW&–ÆÇ’g&öÒF†R7W'&VçBc’ãbFW‡B&Wf–WvVB†W&Rà ¢222¢¤f–æÂFWFW&Ö–æF–öâ¢  ¢¢¢¤ÖW&vVB"Ób&VÖVF–F–öâ7Vff–6–Væ7“¢¢¢F†R6ö×ÆWFVB&VÖVF–F–öâ—2FV6†æ–6ÆÇ’æBWf–FVçF–ÆÇ’7Vff–6–VçB–âF†R7W'&VçB&W÷6—F÷'’7FFRâF†RF—&V7BÖöæÇ’'VçF–ÖRÂ&WF—&VBÖ¶W’&VgW6ÂÂ7W'&VçB×fW'7W2Ö†—7F÷&–6ÂWf–FVæ6R6W&F–öâÂõ2Ó2FÖ—76–öâÂ6æöæ–6ÂWf–FVæ6R6öçfW&vVæ6RÂ÷'F&ÆRF‚&öög2ÂÖæ–fW7BÖFW&—fVB&VÆV6R–FVçF—G’ÂW†7B×6÷W&6R6¶vVBÖVçG'—ö–çBGFW7FF–öâÂæBæ–æWFVVâ×7FvRf–ÂÖ6Æ÷6VB&VÆV6R—VÆ–æRÆÂ&VÖ–âfÆ–Bâ ¢¢¢¤7W'&VçBc6öæ6ÇW6–öã¢¢¢c(	—27V'7FçF—fR6öæ6ÇW6–öâF†BæògW'F†W"÷7BÖÖW&vR&W÷6—F÷'’&VÖVF–F–öâ—2&WV—&VB—267W&FRâ—G2Ö–æF—7FFVÖVçB—27FÆRgFW"cÖöæÇ’6öÖÖ—BÂæB—G2f—fR×&÷rc’6Æ÷7W&RÆ—7B—2–æ6ö×ÆWFR&VÆF—fRFòF†R&÷fVB÷&–v–æÂ"ÓbÖ–ærâ ¢¢¢¥c’&÷w27W÷'F&ÆRf÷"6Æ÷7W&S¢¢¢ÆÂV–v‡B÷&–v–æÂ"ÓbÖÖVB&÷w2&R7W÷'F&ÆRf÷"6†ævRFòFöæV¢ ¢¢„DRÔD•5CRã ¢¢„DRÔD•5CRã& ¢¢„DRÔD•5CãF ¢¢„DRÔD•5CãV ¢¢„DRÔD•5Cãf ¢¢„DRÔD•5Cã– ¢¢„DRÔD•5Cã ¢¢„DRÔD•5Cã ¢¢¢¥&÷w2æ÷B7W÷'F&ÆS¢¢¢æöæRâ ¢¢¢¤W†7BæW‡BWF†÷&—¦VB7F–öã¢¢¢WF†÷&—¦RöæR6W&FRc’ãbÖ–çFVææ6R7F–öâF†BÆ–W2F†R–FVçF–f–VBv÷&F–ær6÷'&V7F–öç2æB7FGW26†ævW2âW&ÖæVçBbÔ6æöâG&–ævRæBF†R&÷VæFVBc6÷'&V7F–öâÖ’&ö6VVB6W&FVÇ’æB&Ræ÷B&W&WV—6—FW2f÷"F†BÖ–çFVææ6R7F–öâà ¤DT4•4”ôã¢"Ób$TÔTD”D”ôâ4ôÕÄUDS²c’Ô”åDTää4RÔ’$ô4TT@ ¢22"ã#"’–×ÆVÖVçFF–öâ&WG&÷7V7F—fR„DRÔU”33€ ¢222W†V7WF—fR7VÖÖ' ¥F†—2&W÷'B&W6VçG2Wf–FVæ6Rf÷"ÆVBWfÇVF–öâæBÖ¶W2æò6Æ÷7W&RFWFW&Ö–æF–öâà ¢2222Wf–FVæ6VB–çFVçBæBFVÆ—fW' ¢¢¢¥ÆææVB÷"–çFVæFVC¢¢¢„DRÔU”33‚v266÷VB2F—7F–ÆÆF–öâ&VÆ–&–Æ—G’727ææ–ærWf–FVæ6RF—66—Æ–æRÂ–Ö×WF&ÆR–FVçF—G’÷&÷fVææ6RÂ&VÆV6R–FVçF—G’ÂVçf—&öæÖVçB6æ6†÷Bc2ÂFWFW&Ö–æ—6ÒôrÂ&WW6&ÆR4’&–Ç2ÂD"ô&öG”w&‚ö&6†—FV7GW&R÷7GW&RÂ&÷VæFVB6öæf–wW&VB×c"ÖVBÖ66†RW'6—7FVæ6RÂæBöæR&VÆV6R×6æ—G’—VÆ–æRâV&Æ–2&VFW"W‡ç6–öâÂæWr&÷WFW2Â&öGV7F–öâÖVBÖ66†RWF†÷&—¦F–öâÂc’7FGW2Ö÷fVÖVçBÂ66WFæ6RÂõ2÷WF6öÖR6Æ–×2ÂæB6Æ÷6V÷WBvW&R÷WG6–FRF†R–×ÆVÖVçFF–öâÆî(	—26Æ–Ò&÷VæF'’â¢¤v–âcõbÔ6æöâõ&Wó¢¢¢–çFVæFVB–×ÆVÖVçFF–öâFV6ö×÷6—F–öâæBFWVæFVæ6–W2â¢¤Wf–FVæ6Rö–çFW#¢¢¢'F–f7B(i"#b–×ÆVÖVçFF–öâÆâ„DRÔU”33‚æÖF(i"'&–Vb&V6öb66÷VòW†V7WF–öâÆæ(i"(	Ä„DRÔU”33‚—2F†RF—7F–ÆÆF–öâ&VÆ–&–Æ—G’7>(	ÒÂ(	ÅF†RW–2FöW2æ÷BFBV&Æ–2&VFW"&V†f–÷"ÂV&Æ–2&÷WFW>(	ÒÂ(	Ç&öGV7F–öâÖVBÖ66†RWF†÷&—¦F–öâÂc’7FGW2Ö÷fVÖVçBÂ52Âõ26ö×ÆWF–öâÂ÷"6Æ÷6V÷WBî(	Ò ¢¢¢¥c×&V6÷&FVC¢¢¢FFVæF"ã(	3"ã‚GG&–'WFR"ÓF‡&÷Vv‚"ÓRæBF†Rõ2Óôõ2Ó"†—7F÷'’Fò„DRÔU”33‚âFFVæF"ã.(	3"ã#&V6÷&BF†RÆFW"&WF—&VÖVçBöb7F—fR'&–FvRG&ç7÷'BÂF—&V7BÖöæÇ’&VÖVF–F–öâÂõ2Ó26GW&RÂæB"Óe"Ô"FÖ—76–öââ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã’"Ó„DRÔU”33‚ò"ãr’"ÓR„DRÔU”33‚ò"ã#’"Ób&VÖVF–F–öâ"Óe"Ô"„DRÔU”33‚(i"(	Ä÷&–v–æÂ"–×ÆVÖVçFVBF†R"Ó–FVçF—G’Â&VÆV6RÖ–FVçF—G’ÂVçf—&öæÖVçB×6æ6†÷BÂæBWf–FVæ6Rf÷VæFF–öç>(	ÒÂ(	Ä÷&–v–æÂ"–×ÆVÖVçFVBF†R&÷VæFVB6öæf–wW&VB×c"ÖVBÖ66†R6Æ–6^(	ÒÂ(	Å"Â33crÖW&vVBF†RÆææVB"Óe"Ô"F—&V7BÖöæÇ’f–æÂ–çFVw&F–öâî(	Ò ¢¢¢¤W–2ÖGG&–'WFVC¢¢¢v—D‡V"†—7F÷'’7W÷'G2ÆæFVB6WVVæ6Rg&öÒ"Â33CbF‡&÷Vv‚"Â33crÂv—F‚"Â33S"&V6÷&FVB2ÖW&vVC¢fÇ6V²"Â33c‚—2ÆFW"W–2ÖÆ–æ¶VBFö7VÖVçFF–öâ&V6öæ6–Æ–F–öââ&–æ6—ÂÖW&vRö–çG2–æ6ÇVFRÂ33Cbcvff&V#c63&3–f3&C&3sC#sƒsfFVCƒCFvÂÂ33CrFccc&#S†c#“F&Sf##ff#33&#3sFc#ƒfÂÂ33C‚6VVfSFcS&c&3F6#Sv3“s#c3–#s#S3–&S“fÂÂ33C’&F†Scc&&cc&VV&FF6&fc&#&S#C&ÂÂ33SCs&&ƒ3ƒV3c“#†CCs–S“ƒSFC#3v6f#vVÂÂ33Ssf33“#666S†&FCcF6f#F6#c6S“ƒ#sÂÂ33S2#“s#ScCsFcsCc#ƒC†6SS†&&fcVCC3†c3vÂÂ33SBs–SCsƒcvCfFs“–cC–&c3cV6&VCfC6SVSVcC6ÂÂ33SR3“3c3vCƒs†VCvCvVc#–CƒFcƒ“V3&&6ÂÂ33Sbv3#&Sƒ†cƒS–#“C36“c#c&CSccƒFVÂÂ33SrF#&#†3vVc#c†cV6c“6F#Cv63VSCS3f#VÂÂ33S‚SVcfCcsS3ƒƒ3cvf3ƒvV6S3c3“vff#S““sÂÂ33S’sƒsSfSssfcvfS“ƒ3s#3VFSfs&#–fSCVc–ÂÂ33cbfSc–CvsvcS3–Cs3fff63S“f&CSfvCF“ÂæBÂ33crF#3S–&36c“V33S“Ssffs33–S““c&â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"v—D‡V""ÖWFFFf÷"Â33Cn(	5Â33cr(i"W–2ÖÆ–æ¶VBF—FÆW2Â&Vg2ÂÖW&vVC¢G'VVÂæBÖW&vR6öÖÖ—G3²c(	B„DR'V–ÆBæ÷FW2(i""ã#’"Ób&VÖVF–F–öâ7FFRâ ¢¢¢¥&WòÖö'6W'fVC¢¢¢7W'&VçBÖ–æ—2S“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†ÂF†R7V6‚ÖW&vRöb"Â33c‚â—B6öçF–ç26öÆR7F—fRF—&V7B÷7Fw&U5Â6VÆV7F÷"Â&÷VæFVBÖVBÖ66†Rw&—FR÷&VBÖ&6²&V†f–÷"ÂâWFFW"Ö÷væVB‡VÖâ–æFW‚ôÖ6†–æRÖ—'&÷"Wf–FVæ6Rw&‚Âæ–æWFVVâ×7FvR&VÆV6R×6æ—G’FVf–æ—F–öâÂæB7W'&VçBFö7VÖVçFF–öâÆ–væVBFòF†÷6R7W&f6W2â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"&W÷6—F÷'’ÖWFFFæB6ö×&RS“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†FòÖ–æ(i"(	ÆFVfVÇEÅö'&æ6ƒ¢Ö–î(	ÒÂ(	Ç7FGW3¢–FVçF–6Î(	ÒÂ(	Æ†VEÅö'“¢²&V†–æEÅö'“¢(	Ó²&Wò(i"Væv–æRöF"öFFW"ç–ÂVæv–æRö&öG–w&‚öÖVEö66†Rç–ÂFööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç–ÂFööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æRç–â ¢¢¢¥&WòÖö'6W'fVC¢¢¢F†R7W'&VçB‡VÖâWf–FVæ6R–æFW‚æBÖ6†–æRÖ—'&÷"V6‚6öçF–â“B„DRÔU”33‚×&VÆFVB¶W’÷F‚—'3²F†R&VBÖöæÇ’6ö×&—6öâ&WGW&æVB‡VÖâÖöæÇ“¢æBÖ6†–æRÖöæÇ“¢ÂæB7W'&VçB6VçF–æVÇ2&–æB&÷F‚f–ÆW2â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"Fö72öWf–FVæ6Rô”äDU‚æ§6öæÂ²Fö72öWf–FVæ6Rô”äDU‚ç6†#SfÂ²'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆÂ²'F–f7G2öWf–FVæ6Uö–æFW‚ç6†#SfÂ&VBÖöæÇ’¶W’÷F‚6ö×&—6öâ(i"(	Ã“B„DRÔU”33‚×&VÆFVB—'2–âV6Ž(	ÒÂ(	Æ‡VÖâÖöæÇ“¢(	ÒÂ(	ÆÖ6†–æRÖöæÇ“¢î(	Ò ¢¢¢¥bÔ6æöâ–çFW'&WFF–öã¢¢¢7W'&VçBc’ãbÆVfW2F†RV–v‡B„DRÔU”33‚ÖÖVBF—7F–ÆÆF–öâ&÷w2B6÷W&6R7FGW6W2'F–Æf÷"„DRÔD•5CRãÂ„DRÔD•5CRã&Â„DRÔD•5CãFÂ„DRÔD•5CãVÂ„DRÔD•5CãfÂ„DRÔD•5Cã–ÂæB„DRÔD•5CãÂæB÷F–öæÆf÷"„DRÔD•5Cãâ&Wò&W6Væ6RæBcæ'&F—fRFòæ÷BÇFW"F†÷6R6÷W&6R7FGW6W2â¢¤Wf–FVæ6Rö–çFW#¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂF†RV–v‡BW†7B7V'F6²†VF–æw2Æ—7FVB–âRã(i"ö'6W'fVB7V'F6²7FGW6Æ–æW3²c(	B„DR'V–ÆBæ÷FW2(i""ãR’E"Ô4äôâÓ‚(i"(	ÅF†—2FFVæGVÒFöW2æ÷B6†ævRç’c’&÷r7FGW2î(	Ð ¢2222Æ&vW7BWf–FVæ6VBv–ç2Â&—6·2Âv2Â÷"Væ¶æ÷vç0 ¢¢¢¤Æ&vW7Bv–â(	B&WòÖö'6W'fVC¢¢¢7W'&VçBWf–FVæ6R6W&FW2F—&V7B×6VÆV7F–öâ&ööbg&öÒ†—7F÷&–6Â'&–FvRÖFW&–ÂÂ&WF–ç2&÷VæFVBõ2Ó"ÖVBÖ66†R&ööbÂFÖ—G2F†Rõ2Ó26¶WBF‡&÷Vv‚–æFW‚ôÖ—'&÷"÷væW'6†—ÂæB&–æG2F†Ræ–æWFVVâ×7FvR&VÆV6RÆörâ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó"öÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öÂVF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆöv²c(	B„DR'V–ÆBæ÷FW2(i""ã2’E"Ô4äôâÓb(i"(	Ä†—7F÷&–6Â'&–FvRWf–FVæ6RÕU5BäõB(
b6F—6g’7W'&VçBF—&V7BÖöæÇ’&VÆV6RvFRî(	Ò ¢¢¢¤Æ&vW7Bv÷fW&ææ6R&—6²(	BbÔ6æöâ–çFW'&WFF–öã¢¢¢c’ãb7F–ÆÂFW67&–&W2'&–FvRfÆÆ&6²÷&÷f–FW"&—G’Â6'&–W2Fö¶VâæÖRDUeôD%ô%$”DtUôdÄÄ$4µôô¶ÂæBG&VG2ÖVBÖ66†RW'6—7FVæ6R2â÷F–öæÂgWGW&RÖW–2÷7GW&RÂv†–ÆRÆFW7BcæB7W'&VçB&WòFW67&–&RF—&V7BÖöæÇ’6VÆV7F–öâæBâ–×ÆVÖVçFVB&÷VæFVBÖVB66†Râ¢¤Wf–FVæ6Rö–çFW#¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂ*v7V'F6²„DRÔD•5CãB(	BD"÷7GW&Rb'VçF–ÖR6†V6·2††&æW72f÷"„DRÔdU$ÓB–ò*v7V'F6²„DRÔD•5CãR(	B&öG”w&‚ÖV6†æ–72vFW6ò*v7V'F6²„DRÔD•5Cã(	Bc"ÖVBÖ66†RW'6—7FVæ6R†&FVæ–æv²c(	B„DR'V–ÆBæ÷FW2(i""ã"’rÖ'&–FvRæBD%Åô%$”DtUÅõU$ÂFW&V6F–öâæB&WF—&VÖVçB(i"(	ÄF—&V7B÷7Fw&U5Â66W72F‡&÷Vv‚F†RvÆ÷rÖ÷væVB7–6÷r&÷f–FW"—2F†R6öÆR7F—fR„DRFF&6RG&ç7÷'Bî(	Ò ¢¢¢¤Æ&vW7B†—7F÷&–6ÂWf–FVæ6R6öæfÆ–7B(	BVæ¶æ÷vã¢¢¢c&V6÷&G2F†R"Ó"&VÖVF–Â6†V6·227V66W76gVÂÂ'WBv—D‡V"7F–öç2'Vâ#“#c3C#s“3f÷""Â33Cž(	—2f–æÂ†VB6†÷w2F†RFW7FæB6æ—G’×—VÆ–æV¦ö'2v—F‚6öæ6ÇW6–öã¢f–ÇW&Vâ¢¤Wf–FVæ6RæVVFVC¢¢¢gVÆÂ'Vâ÷&W'Vâ†—7F÷'’æBÆöw2F–VBFò†VB“3v3†#C3SfCFcF#3&S“Fc&6FC##ƒC–#3#–â¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã"’"Ó"„DRÔU”33‚(i"(	Åf—6–&ÆR&WòÖ†÷7B6†V6·2Ç6ò6ö×ÆWFVB7V66W76gVÆÇž(	Ó²&Wò(i"v—D‡V"7F–öç2'Vâ#“#c3C#s“3(i"(	ÇFW7C¢f–ÇW&^(	ÒÂ(	Ç6æ—G’×—VÆ–æS¢f–ÇW&Rî(	Ò ¢¢¢¤Æ&vW7BÆFW"ÖWf–FVæ6Rv(	BVæ¶æ÷vã¢¢¢&÷VæFVBv—D‡V"6V&6†W2F–Bæ÷B–FVçF–g’FVF–6FVB„DRÔU”33‚&ö÷BÂ6Æ÷6R×6²ÂFö¶VâÖWf–FVæ6RÖG&—‚Â÷"66WFæ6RÖ÷WG6–FRÆææ–æröFö7VÖVçFF–öâövVæW&ÂÖ–æFW‚&VfW&Væ6W2âF†—2FöW2æ÷B&÷fRæöæW†—7FVæ6RÂæBF†R–×ÆVÖVçFF–öâÆâ6Æ76–f–W2ÆFW"ö6Æ÷6V÷WB7W&f6W2÷WG6–FR–×ÆVÖVçFF–öâW†V7WF–öââ¢¤Wf–FVæ6RæVVFVC¢¢¢W†7Bv÷fW&æVB'F–f7BF‡2÷"&V7W'6—fRG&6¶VB×G&VR&W7VÇBâ¢¥6V&6‚ÖWF†öC¢¢¢6V&6†VB&Wòf÷"VF—B÷ö†FRÖW–33†Â„DRÔU”33‚6Æ÷6R×6¶Â„DRÔU”33‚6Æ÷6U÷6¶Â„DRÔU”33‚Fö¶VåöWf–FVæ6UöÖG&—†ÂæB„DRÔU”33‚66WFæ6UöÖ†66S¢–ç6Vç6—F—fR“²66÷S¢7W'&VçBv—D‡V"Ö–æFW†VBG&6¶VBf–ÆW3²FööÃ¢v—D‡V"6öFR6V&6‚ÇW2ÖçVÂ6Æ76–f–6F–öã²&W7VÇC¢&W7V7F—fVÇ’"Â’Â"Â2ÂæB2†—G2ÂÆÂÆ–Ö—FVBFòÆç2Â5$G2Âæ'&F—fRöFö72ÂWFFW"6öFRÂ6W76–öâ&W÷'G2Â÷"F†RvVæW&ÂÖ6†–æRÖ—'&÷.(	Fæ÷BF—&V7FÇ’–FVçF–f–VBFVF–6FVB'F–f7Bâ¢¥7WÆVÖVçFÂWf–FVæ6Rö–çFW#¢¢¢v–âcõbÔ6æöâõ&Wó¢v†WF†W"F†÷6RÆFW"7W&f6W2vW&R–×ÆVÖVçFF–öâFVÆ—fW&&ÆW2â'F–f7B(i"#b–×ÆVÖVçFF–öâÆâ„DRÔU”33‚æÖF(i"ÆFW"'F–f7G2÷WG6–FR–×ÆVÖVçFF–öâW†V7WF–öæ(i"(	ÅF†W’&Ræ÷B–×ÆVÖVçFF–öâ÷"õ2FVÆ—fW&&ÆW2–âF†—2Æâî(	Ð ¢222&Wò–ç7V7F–öâ7VÖÖ' ¢¢¢¤ö'6W'fVB&Wò&ö÷C¢¢¢6öææV7F÷"Ö&6¶VB&W÷6—F÷'’×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c&â¢¥&Wòö–çFW#¢¢¢&Wò(i"&W÷6—F÷'’ÖWFFF(i"(	ÆgVÆÅÅöæÖS¢×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c.(	ÒÂ(	Ç&—fFS¢G'V^(	ÒÂ(	ÆFVfVÇEÅö'&æ6ƒ¢Ö–âî(	Ò ¢¢¢¤ö'6W'fVB„TBæB'&æ6‚7FFS¢¢¢7W'&VçBFVfVÇB'&æ6‚Ö–æö–çG2FòS“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†²6ö×&—6öâFòÖ–æ—2–FVçF–6ÂâÆö6ÂGF6†VBöFWF6†VB7FFR—2æ÷BW‡÷6VB'’F†—26öææV7F÷"â¢¥&Wòö–çFW#¢¢¢&Wò(i"&V6VçBÖ–æ6öÖÖ—G2æB6ö×&RS“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†FòÖ–æ(i"(	ÆFö73¢Æ–vâ„DRÔU”33‚&VÆ–&–Æ—G’÷7GW&R…Â33c‚ž(	ÒÂ(	Ç7FGW3¢–FVçF–6Âî(	Ò ¢¢¢¥v÷&¶–ær×G&VR7FGW2&Vf÷&R–ç7V7F–öâ(	BVæ¶æ÷vã¢¢¢v—D‡V"W‡÷6W26öÖÖ—GFVB6W'fW"7FFRÂæ÷B×WF&ÆR6†V6¶÷WC²F—'G’ö6ÆVâ7FGW2v2æ÷Bö'6W'f&ÆRâ¢¤Wf–FVæ6RæVVFVC¢¢¢v—B7FGW2Ò×6†÷'BÒÖ'&æ6†g&öÒF†RW†7B–ç7V7FVB6†V6¶÷WBâ¢¥&Wòö–çFW#¢¢¢&Wò(i"6öææV7F÷"66W72ÖöFR(i"6öÖÖ—GFVBv—D‡V"ö&¦V7G2öæÇ“²æò×WF&ÆR6†V6¶÷WBâ ¢¢¢¥&–Ö'’W–2ÖGG&–'WFVB&WòWf–FVæ6S¢¢¢W–2ÖÆ–æ¶VB"ÖWFFFæBc¦ö–çFÇ’7W÷'B"Ó…Â33Cn(	5Â33Cr’Â"Ó"…Â33CŽ(	5Â33C’’Â"Ó2…Â33S(	5Â33SæBÂ33S2’Â"ÓB…Â33SN(	5Â33SR’Â"ÓR…Â33Sn(	5Â33S‚’Â–æ—F–Â"Ób…Â33S’’Â6÷'&V7F—fR'2Â33c(	5Â33c"ÂF—&V7BÖöæÇ’"Óe"Ô'2Â33c>(	5Â33cbÂõ2Ó26öÖÖ—BSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–fÂ"Óe"Ô"Â33crÂæBFö72"Â33c‚â¢¥&Wòö–çFW#¢¢¢&Wò(i"v—D‡V""ÖWFFFÂ33Cn(	5Â33c‚æB6öÖÖ—BÖWFFFf÷"Sƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–f²c(	B„DR'V–ÆBæ÷FW2(i""ã(	3"ã#â ¢¢¢¥&–Ö'’7W'&VçB7W&f6W3¢¢¢Væv–æR÷'VçF–ÖRö–FVçF—G’ç–²Væv–æRöF"öFFW"ç–²Væv–æRö&öG–w&‚÷&W6öÇfW"ç–²Væv–æRö&öG–w&‚öÖVEö66†Rç–²Væv–æRö6Æ’öÖ–âç–²FööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç–²FööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æRç–²FööÇ2öWf–FVæ6Rö'V–ÆE÷&VÆV6UöGFW7FF–öâç–²7W'&VçB66†VÖ2Â'F–f7G2Âõ26¶WG2ÂFW7G2Â‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"ÂæBFö7VÖVçFF–öâFW67&–&VB&VÆ÷râ¢¥&Wòö–çFW#¢¢¢&Wò(i"7W'&VçBG&VRBS“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†(i"V6‚Æ—7FVBF‚fWF6†VB÷&VBâ ¢¢¢¤ÆFW"F—fW&vVæ6S¢¢¢6ö×&—6öâöb"Â33crÖW&vRF#3S–&36c“V33S“Ssffs33–S““c&Fò7W'&VçB„TB&WGW&ç2W†7FÇ’V–v‡B6†ævVBF‡3¢tTåE2æÖFÂ4„ätTÄôræÖFÂ$TDÔRæÖFÂFö72ôUd”DTä4Uô”äDU‚æÖFÂFö72ô”äDU‚æÖFÂFö72õ%TâæÖFÂFö72öG"ö†FR÷&VÆV6UöGFW7FF–öå÷66Æ–æuöG"æÖFÂæBFö72÷f6æöâõcÔ„DRÔ'V–ÆBÔæ÷FW2×c"ãBãæÖFâF†—2W7F&Æ—6†W2Fö7VÖVçFF–öâõcF—fW&vVæ6RgFW""Â33crv—F†÷WB76–væ–ærF†÷6RÆFW"'—FW2Fò—G2–×ÆVÖVçFF–öââ¢¥&Wòö–çFW#¢¢¢&Wò(i"v—D‡V"6ö×&RF#3S–&36c“V33S“Ssffs33–S““c"ââæS“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†(i"(	Æ†VEÅö'“¢>(	ÒÂV–v‡B×F‚6†ævVBÖf–ÆRÆ—7Bâ ¢¢¢¤W–2×&VÆFVBWf–FVæ6Ræ÷BF—&V7FÇ’–FVçF–f–VC¢¢¢æòFVF–6FVB„DRÔU”33‚&ö÷BÂ6Æ÷6R×6²ÂFö¶VâÖWf–FVæ6RÖG&—‚Â÷"66WFæ6RÖÖ'F–f7BVÖW&vVBg&öÒF†R&÷VæFVB–æFW†VB6V&6†W2â¢¥6V&6‚ÖWF†öC¢¢¢6V&6†VB&Wòf÷"VF—B÷ö†FRÖW–33†Â„DRÔU”33‚6Æ÷6R×6¶Â„DRÔU”33‚6Æ÷6U÷6¶Â„DRÔU”33‚Fö¶VåöWf–FVæ6UöÖG&—†ÂæB„DRÔU”33‚66WFæ6UöÖ†66S¢–ç6Vç6—F—fR“²66÷S¢7W'&VçBv—D‡V"Ö–æFW†VBG&6¶VBf–ÆW3²FööÃ¢v—D‡V"6öFR6V&6‚ÇW2ÖçVÂ66ã²&W7VÇC¢"Â’Â"Â2ÂæB2†—G2Â&W7V7F—fVÇ’ÂÆÂ–âÆææ–ærÂ5$BÂæ'&F—fRöFö72ÂWFFW"Â6W76–öâ×&W÷'BÂ÷"vVæW&ÂÔÖ—'&÷"6öçFW‡G2â6öææV7F÷"–æFW†–ærö6–ærÆVfW2'F–f7BæöæW†—7FVæ6R¢¥Væ¶æ÷vâ¢¢â ¢¢¢¤GG&–'WF–öâÆ–Ö—FF–öã¢¢¢6öÖÖ—B&Ss“ƒ33S3&#f&Cvf3–c#vf3S#ƒCCCc–—2F—FÆVBõ2Ó"„DRÔU”33†'WB—G26†ævVBF‡2&RVæFW"F†Rõ2Ó6¶WC²7W'&VçBõ2Ó"6¶WB&÷fVææ6R–ç7FVB&Vv–ç2v—F‚f&#c3“ƒ“ƒ“ƒS†3v&†3c–cCFcVC†f†÷2†W–33‚“¢&V6÷&BÖVBÖ66†R6Öö¶V’â¢¥&Wòö–çFW#¢¢¢&Wò(i"6öÖÖ—BÖWFFFæB6†ævVBÖf–ÆRÆ—7G2f÷"&÷F‚6öÖÖ—G2â ¢¢¢¥v÷&¶–ær×G&VR7FGW2gFW"&VBÖöæÇ’–ç7V7F–öâ(	BVæ¶æ÷vã¢¢¢æò×WF&ÆR6†V6¶÷WBW†—7FVBæBæò&Wò×WFF–öâv2W&f÷&ÖVBâ¢¤Wf–FVæ6RæVVFVC¢¢¢÷7BÖ–ç7V7F–öâv—B7FGW2Ò×6†÷'BÒÖ'&æ6†g&öÒF†R6ÖR6†V6¶÷WBâ¢¥&Wòö–çFW#¢¢¢&Wò(i"6öææV7F÷"66W72ÖöFRæB7F–öâÆör(i"&VBÖöæÇ’fWF6‚÷6V&6‚ö6ö×&R÷W&F–öç2öæÇ’à ¢222–×ÆVÖVçFF–öâ&W÷'B…v†B†VæVB–âF†R&Wò ¢2222"÷7FW'&V¶F÷và ¢22222"Ó(	B–FVçF—G’Â&VÆV6RÂVçf—&öæÖVçBÂæBWf–FVæ6Rf÷VæFF–öç0 ¢¢¢¥W'÷6S¢¢¢W7F&Æ—6‚–Ö×WF&ÆR'VçF–ÖR–FVçF—G’Â&VÆV6RöVçf—&öæÖVçBWf–FVæ6RÂæBWFFW"÷væW'6†—â ¢¢¢¤†–v‚ÖÆWfVÂ6†ævW3¢¢¢"Â33CbÆæFVBF†Rf÷VæFF–öã²"Â33Cr&VÖVF–FVBF†R6öæ§Væ7F–öâ6†V6²6ò—BF–Bæ÷BW'6—7B7FFRâ ¢¢¢¤¶W’7W&f6W2F÷V6†VC¢¢¢'VçF–ÖR–FVçF—G’Â&VÆV6R–FVçF—G’ÂVçf—&öæÖVçB6æ6†÷BÂWf–FVæ6RWFFW"Â66†VÖ2ÂFW7G2â ¢¢¢¥FW7G2÷"Wf–FVæ6R&öGV6VC¢¢¢c&V6÷&G2F†R–FVçF—G’öVçf—&öæÖVçBöWf–FVæ6Rf÷VæFF–öâæBföÆÆ÷r×WfÆ–FF–öã²7W'&VçB&Wò&WF–ç2Væv–æR÷'VçF–ÖRö–FVçF—G’ç–Â6FÆöröÖæ–fW7Bæ§6öæÂ'F–f7G2ö–FVçF—G’÷6W'f–6Uö–FVçF—G’æ§6öæÂæB'F–f7G2öVF—BöVçböVçe÷6æ6†÷Bæ§6öæâ ¢¢¢¤†—7F÷&–6ÆÇ’GG&–'WF&ÆR÷WF6öÖS¢¢¢W–2ÖGG&–'WFVBF‡&÷Vv‚"Â33CbÖW&vRcvff&V#c63&3–f3&C&3sC#sƒsfFVCƒCFvæB"Â33CrÖW&vRFccc&#S†c#“F&Sf##ff#33&#3sFc#ƒfâÆFW"FFVæGVÒ"ãbÖVæG2F†R÷&–v–æÂ&VÆV6RÖöFVÂFòÖæ–fW7BÖFW&—fVB–FVçF—G’æBW‡FW&æÂGFW7FF–öââ ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã’"Ó„DRÔU”33‚(i"(	Ä÷&–v–æÂ"–×ÆVÖVçFVBF†R"Ó–FVçF—G’Â&VÆV6RÖ–FVçF—G’ÂVçf—&öæÖVçB×6æ6†÷BÂæBWf–FVæ6Rf÷VæFF–öç>(	ÒÂ(	Å&VÖVF–Â"(
bÖW&vVB2Fccc&.(
f(	Ó²&Wò(i"v—D‡V""Â33CbõÂ33CrÖWFFF²c(	B„DR'V–ÆBæ÷FW2(i""ãb’66Æ&ÆRÖæ–fW7BÔFW&—fVB&VÆV6R–FVçF—G’(i"(	Æ6FÆöröÖæ–fW7Bæ§6öæ—2F†R6–ævÆR&VÆV6RÖ–FVçF—G’–çWB7F÷&VB–âv—Bî(	Ð ¢22222"Ó"(	BFWFW&Ö–æ—6ÒæB6FÆörÖG&—fVârvFW0 ¢¢¢¥W'÷6S¢¢¢&öGV6RFWFW&Ö–æ—7F–2&VFW"ô4Ä’&ööbfÖ–Æ–W2æB&–æBr6†V6·2Fò6FÆövVB7V66W72&÷WFRv—F†÷WBFF–ærV&Æ–2&÷WFRâ ¢¢¢¤†–v‚ÖÆWfVÂ6†ævW3¢¢¢"Â33C‚ÆæFVB&ööb&öGV6W'2Â66†VÖ2Â'F–f7G2ÂFW7G2ÂæBVæGö–çBÖ6FÆör7W÷'C²"Â33C’FG&W76VB&Wf–Wrv2â ¢¢¢¤¶W’7W&f6W2F÷V6†VC¢¢¢FWFW&Ö–æ—6ÒôrvVæW&F÷'2ÂWf–FVæ6R'F–f7G2ÂFö72ôTäEô”åE5ô4DÄôræ§6öæÂ66†VÖ2ÂFW7G2â ¢¢¢¥FW7G2÷"Wf–FVæ6R&öGV6VC¢¢¢7W'&VçB&WòÆ—7G2öæÇ’tUB÷&VFW&VæFW"7V66W75öVæGö–çG6²ö–çFW&æÂ÷fW'6–öæ—2æ÷BrÖVÆ–v–&ÆRâF†R†—7F÷&–6Âf–æÂÖ†VB4’F—7÷6—F–öâ—26öæfÆ–7F–ærÂ2&V6÷&FVBVæFW"Wf–FVæ6Rv2â ¢¢¢¤†—7F÷&–6ÆÇ’GG&–'WF&ÆR÷WF6öÖS¢¢¢W–2ÖGG&–'WFVBF‡&÷Vv‚"Â33C‚ÖW&vR6VVfSFcS&c&3F6#Sv3“s#c3–#s#S3–&S“fæB"Â33C’ÖW&vR&F†Scc&&cc&VV&FF6&fc&#&S#C&â ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã"’"Ó"„DRÔU”33‚(i"(	Ä÷&–v–æÂ"–×ÆVÖVçFVBF†R"Ó"FWFW&Ö–æ—7F–2&VFW"ô4Ä’&ööbfÖ–Çž(	ÒÂ(	Å&VÖVF–Â"(
bFG&W76VBF†÷6Rv2v—F†÷WBFF–æræWrV&Æ–2&÷WF^(	Ó²&Wò(i"v—D‡V""Â33C‚õÂ33C’ÖWFFF²&Wò(i"Fö72ôTäEô”åE5ô4DÄôræ§6öæ(i"6öÆR7V66W75öVæGö–çG6&÷rtUB÷&VFW&Âö–çFW&æÂ÷fW'6–öæuöVÆ–v–&ÆS¢fÇ6Và ¢22222"Ó2(	B&WW6&ÆR4’&–Ç0 ¢¢¢¥W'÷6S¢¢¢W7F&Æ—6‚&WW6&ÆR&–Â×öÆ–7’¦ö'2Â'VææW"öWf–FVæ6R–çFVw&F–öâÂæBÆ—fR×&ööb6fWG’fÆ–FF–öââ ¢¢¢¤†–v‚ÖÆWfVÂ6†ævW3¢¢¢"Â33SÆæFVBF†R–æ—F–Â&–Ç2fÖ–Ç“²"Â33SFFVB÷Vâ×&–Ç2"ô$&ööbv÷&³²"Â33S2&W—&VBÆ—fR×&ööb6†RæB6fWG’â"Â33S"v2FV×÷&'’fÆ–FF–öâ'&æ6‚v—F‚ö'6W'fVBÖWFFFÖW&vVC¢fÇ6Vâ ¢¢¢¤¶W’7W&f6W2F÷V6†VC¢¢¢&–Ç2¦ö'2÷'VææW"ÂWf–FVæ6R&öGV6W'2Â4’–çFVw&F–öâÂ66†VÖ2ÂFW7G2â ¢¢¢¥FW7G2÷"Wf–FVæ6R&öGV6VC¢¢¢c&V6÷&G2F†RF‡&VRÆæFVBGFV×G2æBF†Rf–æÂÆ—fR×&ööb66†VÖ²7W'&VçB&Wò&WF–ç2&–Ç2×&VÆFVBWf–FVæ6RæB–çFVw&F–öâFW7G2â ¢¢¢¤†—7F÷&–6ÆÇ’GG&–'WF&ÆR÷WF6öÖS¢¢¢W–2ÖGG&–'WFVBF‡&÷Vv‚ÖW&vW2Cs&&ƒ3ƒV3c“#†CCs–S“ƒSFC#3v6f#vVÂsf33“#666S†&FCcF6f#F6#c6S“ƒ#sÂæB#“s#ScCsFcsCc#ƒC†6SS†&&fcVCC3†c3vâ ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã2’"Ó2„DRÔU”33‚(i"(	Ä÷&–v–æÂ"7&VFVBF†R&WW6&ÆR"Ó2&–Ç2vFRfÖ–Çž(	ÒÂ(	Å6V6öæB&VÖVF–Â"(
bÅ¶FFVEÅÒ6Æ÷6VBÆ—fR×&ööb66†VÖ(	Ó²&Wò(i"v—D‡V""Â33S(	5Â33S2ÖWFFF²&Wò(i"FW7G2öWf–FVæ6R÷FW7E÷&–Ç5ö6•÷v÷&¶fÆ÷uö–çFVw&F–öâç–à ¢22222"ÓBæBõ2Ó(	BD"Â&öG”w&‚Â&6†—FV7GW&RÂæB†—7F÷&–6Â'&–FvRÖW&÷7GW&P ¢¢¢¥W'÷6S¢¢¢FBD"ô&öG”w&‚ö&6†—FV7GW&RWf–FVæ6RÂ6÷W&6RÖæWWG&Â&ö¦V7F–öâÂ6÷W&6RÖ–çf&–æ6R&ööbÂæBF†RF†VâÖWF†÷&—¦VBF—&V7Bö'&–FvR÷7GW&R6¶WBâ ¢¢¢¤†–v‚ÖÆWfVÂ6†ævW3¢¢¢"Â33SBÆæFVBF†R&6†—FV7GW&RæB&öGV6W"7Æ—C²v÷&¶fÆ÷r'Vâ#“CS3#S#c–f–ÆVBâ"Â33SR&W—&VBÖÆf÷&ÖVBÖ6†–æRÖ—'&÷"&÷ræBÖ—76–ær'VçF–ÖR×Fö¶Vâ&–æF–ærâõ2Ó&V6÷&FVB&÷VæFVB&VBÖöæÇ’F—&V7Bö'&–FvRÖW&6¶WBâ ¢¢¢¤¶W’7W&f6W2F÷V6†VC¢¢¢D"ô&öG”w&‚&ö¦V7F÷'2Â¶W—2ÖöæÇ’&6†—FV7GW&R6æ6†÷BÂWf–FVæ6RWFFW"ôÖ—'&÷"ÂVF—Bö÷2ö†FRÖW–33‚ö÷2Óöâ ¢¢¢¥FW7G2÷"Wf–FVæ6R&öGV6VC¢¢¢7W'&VçB'F–f7G2ö&6†—FV7GW&Rö&6†—FV7GW&U÷6æ6†÷Bæ¶W—5ööæÇ’æ§6öæ&W÷'G266†VÖ&6†—FV7GW&U÷6æ6†÷Bæ¶W—5ööæÇ’çcÂ6÷W&6RV÷FF–öâ&æÇ—¦W%÷fW&F–7B#¢'72&ÂæBVæ¶æ÷våö6÷VçC¢²õ2Ó&VÖ–ç2–æFW†VB2†—7F÷&–6Åö'&–FvUöWf–FVæ6Vâ ¢¢¢¤†—7F÷&–6ÆÇ’GG&–'WF&ÆR÷WF6öÖS¢¢¢"Â33SBÖW&vRs–SCsƒcvCfFs“–cC–&c3cV6&VCfC6SVSVcC6Â"Â33SRÖW&vR3“3c3vCƒs†VCvCvVc#–CƒFcƒ“V3&&6ÂæBõ2Ó6öÖÖ—B6c3cFS#Ff3v#Fffc##vC“6cSS&#C–C#–&RW–2ÖÆ–æ¶VBâÆFW7BcÖ¶W2F†Rõ2Ó'&–FvRÖVæ–ær†—7F÷&–6ÂöæÇ’â ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãR’"ÓB„DRÔU”33‚(i"(	ÇF†R&6†—FV7GW&RæBfö7W6VB&öGV6W"7Æ—BÆæFVN(	ÒÂ(	Ç&W7F÷&VB6ö×ÆWFRf—†VBö–çN(	Ó²c(	B„DR'V–ÆBæ÷FW2(i""ãb’õ2Ó„DRÔU”33‚(i"(	ÆöæR&÷VæFVBÂòÖW†V7WFVBÂ&VBÖöæÇ’D"æB'&–FvR÷7GW&R'Vî(	Ó²c(	B„DR'V–ÆBæ÷FW2(i""ã"’'&–FvR&WF—&VÖVçB(i"(	ÅF†R'&–FvRÖFWVæFVçB„DRÔU”33‚õ2Ó"ÆæR—2&WF—&VN(	Ó²&Wò(i"7F–öç2'Vâ#“CS3#S#c–Â"Â33SRÖWFFFÂæB7W'&VçB&6†—FV7GW&R6æ6†÷Bà ¢22222"ÓRæBõ2Ó"(	B6öæf–wW&VB×c"ÖVBÖ66†RW'6—7FVæ6P ¢¢¢¥W'÷6S¢¢¢–×ÆVÖVçB&÷VæFVBÖVBÖ66†RW'6—7FVæ6Rv—F‚W‡Æ–6—BW6W'BÂÖVB×–ÆöBÖöæÇ’7F÷&vRÂ6æöæ–6Â&VBÖ&6²Â–FV×÷FVæ6RÂÆVv7’fÆÆ&6²ÂæB&öGV7F–öâÖÆ–¶R&VgW6Ââ ¢¢¢¤†–v‚ÖÆWfVÂ6†ævW3¢¢¢"Â33SbÆæFVBF†R6Æ–6S²"Â33Sr&W—&VB6†&VBÖÆör†W&ÖWF–6—G“²"Â33S‚†&FVæVBG&6V&6²öVçf—&öæÖVçB&VF7F–öââõ2Ó"&V6÷&FVBöæRWF†÷&—¦VB6öæf–wW&VB×c"&WVW7BÂöæR–ç6W'B÷&VBÖ&6²ÂæB&WVBw&—FRv—F‚æò6V6öæB–ç6W'F–öââ ¢¢¢¤¶W’7W&f6W2F÷V6†VC¢¢¢Væv–æRö&öG–w&‚öÖVEö66†Rç–ÂVæv–æRö&öG–w&‚÷&W6öÇfW"ç–ÂVæv–æRö6Æ’öÖ–âç–ÂÖVBÖ66†R66†VÖ2÷FW7G2Â'F–f7G2ö&öG–w&‚÷c%öÖVEö66†RöÖæ–fW7Bæ§6öæÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó"öâ ¢¢¢¥FW7G2÷"Wf–FVæ6R&öGV6VC¢¢¢F†R7W'&VçBÖæ–fW7B&–æG2&VF–6FW2f÷"W‡Æ–6—BW6W'BÂÖVB–ÆöBÂ6æöæ–6Â&—G’Â–FV×÷FVæ6RÂæò&r–ÆöBÂ¦W&òÔ’ôò&VgW6ÂÂÆVv7’fÆÆ&6²ÂæB&öGV7F–öâ&VgW6Ã²7W'&VçBFW7G2–æ6ÇVFRFW7G2ö&öG–w&‚÷FW7E÷c%öÖVEö66†Rç–â ¢¢¢¤†—7F÷&–6ÆÇ’GG&–'WF&ÆR÷WF6öÖS¢¢¢"Â33SbÖW&vRv3#&Sƒ†cƒS–#“C36“c#c&CSccƒFVÂ"Â33SrÖW&vRF#&#†3vVc#c†cV6c“6F#Cv63VSCS3f#VÂ"Â33S‚ÖW&vRSVcfCcsS3ƒƒ3cvf3ƒvV6S3c3“vff#S““sÂæBF†Rc×&V6÷&FVBõ2Ó"6¶WB7W÷'BF†R†—7F÷&–6ÂGG&–'WF–öââ ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãr’"ÓR„DRÔU”33‚(i"(	Ä÷&–v–æÂ"–×ÆVÖVçFVBF†R&÷VæFVB6öæf–wW&VB×c"ÖVBÖ66†R6Æ–6^(	ÒÂ(	Å6V6öæB&VÖVF–Â"æ'&÷vÇ’&WÆ6VBF†BF–7F–öæ'’v—F‚ôVçf—&öæÖVçE&W7F÷&U7FFV(	Ó²c(	B„DR'V–ÆBæ÷FW2(i""ã‚’õ2Ó"„DRÔU”33‚(i"(	ÆöæRÖVBÖ66†R–ç6W'BÂ6æöæ–6Â&VBÖ&6²ÂæB6V6öæB6ÖRÖ–FVçF—G’w&—FRF†B–ç6W'FVB¦W&ò&÷w>(	Ó²&Wò(i"7W'&VçBÖVBÖ66†RÖöGVÆW2ÂÖæ–fW7BÂõ2Ó"&ö÷BÂæBFW7Bà ¢22222"ÓbÆ–æVvRæBõ2Ó2(	B&VÆV6R÷&6†W7G&F–öâÂF—&V7BÖöæÇ’&VÖVF–F–öâÂæBWf–FVæ6RFÖ—76–öà ¢¢¢¥W'÷6S¢¢¢&–æBF†R&–÷"&ööbfÖ–Æ–W2–çFò&VÆV6RfÆ–FF–öâÂF†Vâ&W6öÇfR÷7BÕÂ33S’Wf–FVæ6RôD"&6†—FV7GW&RFVfV7G2æBFÖ—B7W'&VçBF—&V7BÖöæÇ’Wf–FVæ6Râ ¢¢¢¤†–v‚ÖÆWfVÂ6†ævW3¢¢¢"Â33S’ÆæFVBF†R–æ—F–Âr×7FvR&VÆV6R÷&6†W7G&F÷"â'2Â33c(	5Â33c"&W—&VBöÆFW"&–æF–æw2æB–çG&öGV6VB&WF–æVBÖWf–FVæ6RôDDÂFööÆ–ærâc"ã"F†Vâ&WF—&VB7F—fR'&–FvRG&ç7÷'Bâ'2Â33c>(	5Â33cbW7F&Æ—6†VBF—&V7B7–6÷r6VÆV7F–öâÂ6VçG&Æ—¦VBD$66W76Â&WF—&VBÖ¶W’&VgW6ÂÂF—&V7BÖ6öçG&7B6†V6·2Âõ2Ó2FööÆ–ærÂÖæ–fW7BÖFW&—fVB–FVçF—G’ÂæBW‡FW&æÂGFW7FF–öââõ2Ó26GW&VBF†RF—&V7B&VBÖöæÇ’÷7GW&Râ"Â33crFÖ—GFVBF†R6¶WBæBF—&V7B×6VÆV7F–öâ&–Ö'’–çFòF†Rf–æÂæ–æWFVVâ×7FvRw&‚â ¢¢¢¤¶W’7W&f6W2F÷V6†VC¢¢¢Væv–æRöF"öFFW"ç–²F—&V7B×6VÆV7F–öâvVæW&F÷"÷66†VÖ÷6æ6†÷C²õ2Ó2'VææW"Â6¶WBÂ÷W&F÷"&V6÷&BÂæB66†VÖ3²WFFW"ô–æFW‚ôÖ—'&÷#²&VÆV6R—VÆ–æS²GFW7FF–öâ'V–ÆFW#²4’6†V6·2÷FW7G2â ¢¢¢¥FW7G2÷"Wf–FVæ6R&öGV6VC¢¢¢7W'&VçBF—&V7B6VÆV7F–öâ†2f÷W"÷&FW&VB66W3²õ2Ó2&V6÷&G2¦W&ò5Âw&—FW2Â¦W&ò&WG&–W2ÂæB¦W&òÇFW&æFR×&÷f–FW"GFV×G3²7W'&VçB6æ—G’Æör&V6÷&G2æ–æWFVVâ7FvRÆ–æW2Âf—'7Eöf–ÆVE÷7FvS¤äôäVÂæB6÷W&6RV÷FF–öâ'7VÖÖ'“¥52&²f–æÂÖ†VB'Vç2f÷""Â33cbæBÂ33cr6öæ6ÇVFVB7V66W72â ¢¢¢¤†—7F÷&–6ÆÇ’GG&–'WF&ÆR÷WF6öÖS¢¢¢"Â33S’ÖW&vRsƒsSfSssfcvfS“ƒ3s#3VFSfs&#–fSCVc–²cÖGG&–'WFVB'2Â33c(	5Â33cc²õ2Ó2&V6÷&B6öÖÖ—BSƒ#S“†CSƒ3CCf#–VVc&VSff36Sc3ƒ3C–f²æB"Â33crÖW&vRF#3S–&36c“V33S“Ssffs33–S““c&â ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãr’"Óe"Ô(i"(	Å"Â33c2W7F&Æ—6†VBF†RÖ–â–×ÆVÖVçFF–öî(	ÒÂ(	Å"Â33cb6Æ÷6VBF†R&VÖ–æ–ærõ2Ó2—6öÆF–öâÂf–ÆW7—7FVÒÂ7FFRÖÖ6†–æRÂfÆ–FF–öâ×&6RÂæB&VÆV6RÖWf–FVæ6RFVfV7G>(	Ó²c(	B„DR'V–ÆBæ÷FW2(i""ã’’õ2Ó2(i"(	ÆW†V7WFVBæò5Âw&—F^(	ÒÂ(	ÆÖFRæò&WG'ž(	ÒÂ(	ÆÖFRæòÇFW&æFR×&÷f–FW"GFV×N(	Ó²c(	B„DR'V–ÆBæ÷FW2(i""ã#’"Óe"Ô"(i"(	Å"Â33crÖW&vVBF†RÆææVB"Óe"Ô"F—&V7BÖöæÇ’f–æÂ–çFVw&F–öî(	Ó²&Wò(i"7W'&VçB—VÆ–æRÆörÂF—&V7B×6VÆV7F–öâ6æ6†÷BÂõ2Ó26¶WBÂ"Â33cbõÂ33crv÷&¶fÆ÷r'Vç2à ¢22222÷7BÖ–çFVw&F–öâFö7VÖVçFF–öâ(	B"Â33c€ ¢¢¢¥W'÷6S¢¢¢&V6öæ6–ÆR7F—fR&W÷6—F÷'’wV–Fæ6Rv—F‚f–æÂF—&V7BÖöæÇ’D"ÂÖVBÖ66†RÂWf–FVæ6RÂõ2ÂæB&VÆV6RÖGFW7FF–öâ÷7GW&Râ ¢¢¢¤†–v‚ÖÆWfVÂ6†ævW3¢¢¢6WfVâFö7VÖVçFF–öâf–ÆW26†ævVC²æò–×ÆVÖVçFF–öâw&÷W–ær—276–væVBFòF†÷6R'—FW2â ¢¢¢¤¶W’7W&f6W2F÷V6†VC¢¢¢tTåE2æÖFÂ4„ätTÄôræÖFÂ$TDÔRæÖFÂFö72ôUd”DTä4Uô”äDU‚æÖFÂFö72ô”äDU‚æÖFÂFö72õ%TâæÖFÂFö72öG"ö†FR÷&VÆV6UöGFW7FF–öå÷66Æ–æuöG"æÖFâ ¢¢¢¥FW7G2÷"Wf–FVæ6R&öGV6VC¢¢¢f–æÂÖ†VBv÷&¶fÆ÷r'Vâ3#Cccs3ƒv6öæ6ÇVFVB7V66W73²F†RFö72×6Vç6—F—fRF—&V7BÔD"6öçG&7B6†V6²7V66VVFVBgFW"f–æÂv÷&F–ær6÷'&V7F–öââ ¢¢¢¤†—7F÷&–6ÆÇ’GG&–'WF&ÆR÷WF6öÖS¢¢¢W–2ÖÆ–æ¶VBFö72&V6öæ6–Æ–F–öâB"Â33c‚Â7V6‚ÖW&vRö7W'&VçB„TBS“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†²—B—2ÆFW"F†â"Â33c~(	—2–×ÆVÖVçFF–öâöWf–FVæ6RFÖ—76–öââ ¢¢¢¤Wf–FVæ6Rö–çFW'3¢¢¢&Wò(i""Â33c‚ÖWFFFÂ6†ævVBÖf–ÆR–çfVçF÷'’Â&Wf–Wr†—7F÷'’ÂæBv÷&¶fÆ÷r'Vâ3#Cccs3ƒv²&Wò(i"6ö×&RF#3S–&36c“V33S“Ssffs33–S““c"ââæS“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†à ¢2222Ö¦÷"7W&f6W2ffV7FV@ ¢¢¢¤–FVçF—G’÷&VÆV6S¢¢¢W–2ÖGG&–'WFVB"Ó7&VFVBF†Rf÷VæFF–öã²"Óe"Ô&WÆ6VBF†R÷&–v–æÂ&VÆV6RÖV6†æ–72v—F‚6æöæ–6ÂÖÖæ–fW7BÖFW&—fVB–FVçF—G’æBW‡FW&æÂW†7B×6÷W&6RGFW7FF–öââ7W'&VçB&WòFW&—fW2'VçF–ÖR&VÆV6Uö–Fg&öÒ6æöæ–6Â6¶vVB6FÆöröÖæ–fW7Bæ§6öæâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãæB"ãc²&Wò(i"Væv–æR÷'VçF–ÖRö–FVçF—G’ç–Â6FÆöröÖæ–fW7Bæ§6öæÂFööÇ2öWf–FVæ6Rö'V–ÆE÷&VÆV6UöGFW7FF–öâç–â ¢¢¢¤FWFW&Ö–æ—6Òôs¢¢¢W–2ÖGG&–'WFVB"Ó"&öGV6VBF†RFWFW&Ö–æ—6ÒôrfÖ–Ç“²7W'&VçB&WòFW6–væFW2öæÇ’tUB÷&VFW&27V66W72&ööb&÷WFRâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã#²&Wò(i"Fö72ôTäEô”åE5ô4DÄôræ§6öæ²crÔ6æöâÔ„DRÔæ'&F—fW2ÔwV–FRÂ*vG&ç7÷'B÷7GW&R‡&÷WFRÖöæÇ“²F—FÆW2ÖöæÇ’–(i"(	Å7V66W72&öög2'VâöæÇ’öâ6FÆövVB¥4ôâ7V66W72&÷WF^(	ÒÂ(	Æö–çFW&æÂ÷fW'6–öæ—2÷2ÖöæÇ’æBæ÷BrÖVÆ–v–&ÆRî(	Ò ¢¢¢¤4’&–Ç3¢¢¢W–2ÖGG&–'WFVB"Ó2W7F&Æ—6†VB&WW6&ÆR&–Ç2&ööbæB6fWG’fÆ–FF–öã²7W'&VçB&Wò&WF–ç2F†R–çFVw&F–öâFW7BæB4’6†V6·2â¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã3²&Wò(i"FW7G2öWf–FVæ6R÷FW7E÷&–Ç5ö6•÷v÷&¶fÆ÷uö–çFVw&F–öâç–æBæv—F‡V"÷v÷&¶fÆ÷w2ö6’ç–ÖÆâ ¢¢¢¤D"ô&öG”w&‚ö&6†—FV7GW&S¢¢¢"ÓB7&VFVBF†R÷7GW&RWf–FVæ6RfÖ–Ç“²ÆFW""Óe"v÷&²&WÆ6VB7F—fR'&–FvR6VÆV7F–öâv—F‚6–ævÆRF—&V7B7–6÷r&÷f–FW"æB†—7F÷&–6ÂV&çF–æRöb'&–FvRÖW&Wf–FVæ6Râ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãRÂ"ã"Â"ã3²&Wò(i"Væv–æRöF"öFFW"ç–Â'F–f7G2ö&6†—FV7GW&Rö&6†—FV7GW&U÷6æ6†÷Bæ¶W—5ööæÇ’æ§6öæÂ'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæâ ¢¢¢¤ÖVB66†S¢¢¢"ÓRôõ2Ó"–×ÆVÖVçFVBæB6GW&VB&÷VæFVB6öæf–wW&VB×c"W'6—7FVæ6S²7W'&VçB&Wò&WV—&W2W‡Æ–6—BW6W'BÂ7F÷&W2öæÇ’ÖVB–ÆöG2ÂfW&–f–W26æöæ–6Â&VBÖ&6²ö–FV×÷FVæ6RÂæB&VgW6W2&öGV7F–öâÖÆ–¶RW†V7WF–öââ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãrÂ"ã‚Â"ãS²&Wò(i"ÖVBÖ66†RÖöGVÆW2ÂÖæ–fW7BÂæBõ2Ó"6¶WBâ ¢¢¢¤Wf–FVæ6Rôõ3¢¢¢"Óe"Ô"&÷VæBF—&V7B×6VÆV7F–öâæBõ2Ó2&V6÷&G2FòF†RWFFW"Ö÷væVB–æFW‚ôÖ—'&÷"w&ƒ²õ2Ó&VÖ–ç2†—7F÷&–6ÂæBõ2Ó"&VÖ–ç2F†RÖVBÖ66†R6¶WBâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã>(	3"ã#²&Wò(i"Fö72öWf–FVæ6Rô”äDU‚æ§6öæÂ'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆÂæBF‡&VRõ2&ö÷G2â ¢¢¢¤Fö7VÖVçFF–öã¢¢¢"Â33c‚WFFVB7W'&VçB×7FFRwV–Fæ6RgFW"F†R–×ÆVÖVçFF–öâöWf–FVæ6RÖW&vRâ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i""Â33c‚6†ævVBÖf–ÆR–çfVçF÷'’æB7W'&VçB„TBà ¢2222Wf–FVæ6R–çfVçF÷'’‡v†BW†—7G2 §ÂfÖ–Ç’Â6öæ7&WFR7W'&VçBWf–FVæ6RÂW7F&Æ—6†VB÷7GW&RÂWf–FVæ6Rö–çFW"À§ÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÂÒÒÒÒÒÀ§Â–FVçF—G’÷&VÆV6RÂ6FÆöröÖæ–fW7Bæ§6öæ²'F–f7G2ö–FVçF—G’÷6W'f–6Uö–FVçF—G’æ§6öæ²FööÇ2öWf–FVæ6Rö'V–ÆE÷&VÆV6UöGFW7FF–öâç–ÂÖæ–fW7B—2F†R6–ævÆRG&6¶VB&VÆV6RÖ–FVçF—G’–çWC²GFW7FF–öâ—2w&—GFVâW‡FW&æÆÇ’âÂc(	B„DR'V–ÆBæ÷FW2(i""ãc²&Wò(i"Æ—7FVBf–ÆW2âÀ§ÂVçf—&öæÖVçBö&6†—FV7GW&RôrÂ'F–f7G2öVF—BöVçböVçe÷6æ6†÷Bæ§6öæ²'F–f7G2ö&6†—FV7GW&Rö&6†—FV7GW&U÷6æ6†÷Bæ¶W—5ööæÇ’æ§6öæ²Fö72ôTäEô”åE5ô4DÄôræ§6öæÂVçbc6²¶W—2ÖöæÇ’&6†—FV7GW&R6÷W&6RV÷FF–öâ&æÇ—¦W%÷fW&F–7B#¢'72&²öæRtUB7V66W72&÷WFRâÂ&Wò(i"V6‚W†7Bf–ÆRæBö'6W'fVBf–VÆG2âÀ§ÂF—&V7BD"Â'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæ²66†VÖ2ö†FUöW–33…öF—&V7EöF%÷6VÆV7F–öâçcæ§6öæ²Væv–æRöF"öFFW"ç–Âc76–vç2F—7F–æ7B7W'&VçBF—&V7BÖöæÇ’–FVçF—G’æB&'2†—7F÷&–6Â'&–FvRWf–FVæ6Rg&öÒ6F—6g––ær—G2vFRâÂc(	B„DR'V–ÆBæ÷FW2(i""ã3²&Wò(i"Æ—7FVBF‡2âÀ§ÂÖVB66†RÂ'F–f7G2ö&öG–w&‚÷c%öÖVEö66†RöÖæ–fW7Bæ§6öæ²6WfVâÖæ–fW7BÖ&÷VæB&–Ö&–W3²Gvò66†VÖ3²VF—Bö÷2ö†FRÖW–33‚ö÷2Ó"öÂ&÷VæFVBÖVB×–ÆöBW'6—7FVæ6RæB&WF–æVBõ2Ó"7W÷'BâÂc(	B„DR'V–ÆBæ÷FW2(i""ãrÂ"ã‚Â"ãS²&Wò(i"Öæ–fW7BæBõ2Ó"&ö÷BâÀ§Âõ2ÓÂVF—Bö÷2ö†FRÖW–33‚ö÷2ÓöÂ†—7F÷&–6Â'&–FvRÖW&Wf–FVæ6RöæÇ’âÂc(	B„DR'V–ÆBæ÷FW2(i""ã.(	3"ã3²&Wò(i"õ2Ó–æFW‚&÷w26Æ76–f–VB†—7F÷&–6Åö'&–FvUöWf–FVæ6VâÀ§Âõ2Ó2ÂVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2÷¶6öÖÖæG2çG‡BÇ7FF÷WBçG‡BÇ7FFW'"çG‡BÆW†—Eö6öFRçG‡BÆVçe÷&W6Væ6Ræ§6öâÆF%÷÷7GW&U÷7VÖÖ'’æ§6öâÆæöæ6Æ–×2æ§6öâÇ&W7VÇE÷7VÖÖ'’æ§6öâÇfÆ–FF–öå÷&V6V—Bæ§6öâÆ6†V6·7V×2ç6†#SgÖ²6WfVâ66†VÖ3²VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&BöÂF—&V7B&VBÖöæÇ’6¶WBæB6W&FR÷W&F÷"&V6÷&C²f–æÂFÖ—76–öâGG&–'WFVBFò"Â33crâÂc(	B„DR'V–ÆBæ÷FW2(i""ãBÂ"ã’Â"ã#²&Wò(i"W†7B&ö÷G2âÀ§Â–æFW‚ôÖ—'&÷"ÂFö72öWf–FVæ6Rô”äDU‚æ§6öæ²Fö72öWf–FVæ6Rô”äDU‚ç6†#Sf²'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÆ²'F–f7G2öWf–FVæ6Uö–æFW‚ç6†#SfÂWFFW"Ö÷væVB‡VÖâ–æFW‚ôÖ6†–æRÖ—'&÷"ÇW26VçF–æVÇ3²“BW–2×&VÆFVB—'2–âV6‚7W'&VçBf–ÆRâÂc(	B„DR'V–ÆBæ÷FW2(i""ãS²&Wò(i"f–ÆW2æB&VBÖöæÇ’—"6ö×&—6öââÀ§Â&VÆV6R6æ—G’ÂVF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆöv²FööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æRç–ÂW†7Bæ–æWFVVâ×7FvRFVf–æ—F–öâæB7W'&VçBG&6¶VBÆös²6÷W&6RV÷FF–öâ'7VÖÖ'“¥52&âÂc(	B„DR'V–ÆBæ÷FW2(i""ãRÂ"ã#²&Wò(i"67&—BæBÆörâÀ§ÂFö7VÖVçFF–öâFVÇFÂVF—BöFö6FVÇF2ö†FRÖW–33…÷c•ö÷5öFVÆVvF–öåöÖVæFÖVçE÷&÷÷6ÂæÖFÂ&WòÆ&VÇ2—BæöâÖ6æöæ–6ÂâÂ&Wò(i"W†7BF‚(i"(	ÆæöâÖ6æöæ–6Âî(	ÒÀ§Â&W&W6VçFF—fRFW7G2ÂFW7G2÷'VçF–ÖR÷FW7Eö–FVçF—G’ç–²FW7G2öWf–FVæ6R÷FW7EöFWFW&Ö–æ—6ÕövFU÷&öög2ç–²FW7G2öWf–FVæ6R÷FW7E÷&–Ç5ö6•÷v÷&¶fÆ÷uö–çFVw&F–öâç–²FW7G2öWf–FVæ6R÷FW7Eö&6†—FV7GW&U÷6æ6†÷Bç–²FW7G2ö&öG–w&‚÷FW7E÷c%öÖVEö66†Rç–²FW7G2öWf–FVæ6R÷FW7Eö†FUöW–33…÷&VÆV6U÷6æ—G’ç–²FW7G2öF"÷FW7EöF—&V7EöF%÷#g"ç–²FW7G2ö÷2÷FW7Eö†FUöW–33…ö÷32ç–²FW7G2öWf–FVæ6R÷FW7E÷&VÆV6UöGFW7FF–öâç–²FW7G2÷Væ—B÷FW7Eö6†V6µöF—&V7EöF%ö6öçG&7Bç–Â7W'&VçB&Wò&W6Væ6RöæÇ“²†—7F÷&–6ÂGG&–'WF–öâföÆÆ÷w2F†R"õcö–çFW'2&÷fRâÂ&Wò(i"7W'&VçBG&VRB„TB(i"V6‚W†7BFW7BF‚âÀ ¢2222Wf–FVæ6Rv0 £â¢¥v†B—2Ö—76–ær÷"Væ6ÆV#¢¢¢F†RWF†÷&—FF—fR†—7F÷&–6Â4’F—7÷6—F–öâf÷""Â33C’â ¢¢¢¥v‡’—BÖGFW'3¢¢¢cæBF†RF—&V7FÇ’ö'6W'fVBv—D‡V"'Vâ6öæfÆ–7Bâ ¢¢¢¤Wf–FVæ6RæVVFVC¢¢¢gVÆÂ7F–öç2'Vâ÷&W'VâÆ—7BæBf–ÆVBÖ¦ö"Æöw2F–VBFò†VB“3v3†#C3SfCFcF#3&S“Fc&6FC##ƒC–#3#–Â–æ6ÇVF–ærç’ÆFW"7V66W76gVÂ'VâcW6VBâ ¢¢¢¤W‡V7FVBWf–FVæ6RÆö6F–öâÂ–b¶æ÷vã¢¢¢v—D‡V"7F–öç2f÷""Â33C’ö†VB“3v3†#C3SfCFcF#3&S“Fc&6FC##ƒC–#3#–â ¢¢¢¥6V&6‚&ööb÷"Væ¶æ÷vã¢¢¢¢¥Væ¶æ÷vââ¢¢c"ã"6—2f—6–&ÆR6†V6·27V66VVFVC²&Wò(i"'Vâ#“#c3C#s“36†÷w2FW7C¢f–ÇW&VæB6æ—G’×—VÆ–æS¢f–ÇW&Vâ £"â¢¥v†B—2Ö—76–ær÷"Væ6ÆV#¢¢¢W†7BW†V7WFVBõ2Ó2&÷f—6–öæ–ær5Â'—FW2æBF†RgVÆÂ&öÆRw&çBöFVfVÇB×&—f–ÆVvRw&‚â ¢¢¢¥v‡’—BÖGFW'3¢¢¢F†RG&6¶VB6¶WB&÷fW2&÷VæFVB6GW&R÷7GW&R'WBæ÷BWfW'’&÷f—6–öæ–ær7FFVÖVçB÷"–æ†W&—FVB&—f–ÆVvRVFvRâ ¢¢¢¤Wf–FVæ6RæVVFVC¢¢¢–Ö×WF&ÆRW†V7WFVB5ÂG&ç67&—BÇW2gVÆÂw&çG2öFVfVÇB×&—f–ÆVvW2–çfVçF÷'’f÷"F†R&÷f—6–öæVB&öÆW2â ¢¢¢¤W‡V7FVBWf–FVæ6RÆö6F–öâÂ–b¶æ÷vã¢¢¢6W&FRWF†÷&—¦F–öâÖ&÷VæB÷W&F÷"Wf–FVæ6S²æòW†7B&WòF‚—2W7F&Æ—6†VBâ ¢¢¢¥6V&6‚&ööb÷"Væ¶æ÷vã¢¢¢¢¥Væ¶æ÷vââ¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã’’õ2Ó2Wf–FVæ6RÆ–Ö—FF–öç2&V6÷&G2&÷F‚v2â £2â¢¥v†B—2Ö—76–ær÷"Væ6ÆV#¢¢¢v†WF†W"FVF–6FVB„DRÔU”33‚&ö÷BÂ6Æ÷6R×6²ÂFö¶VâÖWf–FVæ6RÖG&—‚Â÷"66WFæ6RÖW†—7G2–âv÷fW&æVBÆFW"ÆæRâ ¢¢¢¥v‡’—BÖGFW'3¢¢¢F†W6R&R÷FVçF–ÂÆVBÖFV6—6–öâWf–FVæ6RÂ'WBF†R–×ÆVÖVçFF–öâÆâÆ6VBÆFW"ö6Æ÷6V÷WB7W&f6W2÷WG6–FR–×ÆVÖVçFF–öâW†V7WF–öââ ¢¢¢¤Wf–FVæ6RæVVFVC¢¢¢W†7Bv÷fW&æVBF‡2÷"&V7W'6—fRG&6¶VB×G&VR÷WGWBâ ¢¢¢¤W‡V7FVBWf–FVæ6RÆö6F–öâÂ–b¶æ÷vã¢¢¢VF—B÷ö†FRÖW–33‚öv26V&6†VB6æF–FFS²÷F†W"W†7B†öÖW2&R¢¥Væ¶æ÷vâ¢¢â ¢¢¢¥6V&6‚&ööb÷"Væ¶æ÷vã¢¢¢¢¥6V&6‚ÖWF†öC¢¢¢6V&6†VB&Wòf÷"VF—B÷ö†FRÖW–33†Â„DRÔU”33‚6Æ÷6R×6¶Â„DRÔU”33‚6Æ÷6U÷6¶Â„DRÔU”33‚Fö¶VåöWf–FVæ6UöÖG&—†ÂæB„DRÔU”33‚66WFæ6UöÖ†66S¢–ç6Vç6—F—fR“²66÷S¢7W'&VçBv—D‡V"Ö–æFW†VBG&6¶VBf–ÆW3²FööÃ¢v—D‡V"6öFR6V&6‚öÖçVÂ66ã²&W7VÇC¢"Â’Â"Â2ÂæB2†—G2Â&W7V7F—fVÇ’Âv—F‚æòF—&V7FÇ’–FVçF–f–VBFVF–6FVB'F–f7Bâ6öææV7F÷"Ö–æFW‚Æ–Ö—G2ÆVfRæöæW†—7FVæ6R¢¥Væ¶æ÷vâ¢¢â¢¥7WÆVÖVçFÂWf–FVæ6Rö–çFW#¢¢¢v–âcõbÔ6æöâõ&Wó¢v†WF†W"F†W6RvW&R–×ÆVÖVçFF–öâFVÆ—fW&&ÆW2â'F–f7B(i"#b–×ÆVÖVçFF–öâÆâ„DRÔU”33‚æÖF(i"ÆFW"'F–f7G2÷WG6–FR–×ÆVÖVçFF–öâW†V7WF–öæâ £Bâ¢¥v†B—2Ö—76–ær÷"Væ6ÆV#¢¢¢v÷&¶–ær×G&VR7FGW2B–ç7V7F–öâF–ÖRâ ¢¢¢¥v‡’—BÖGFW'3¢¢¢Væ6öÖÖ—GFVB'—FW26ææ÷B&RGG&–'WFVB÷"76W76VBF‡&÷Vv‚F†R6öÖÖ—GFVBv—D‡V"f–Wrâ ¢¢¢¤Wf–FVæ6RæVVFVC¢¢¢&Vf÷&RögFW"v—B7FGW2Ò×6†÷'BÒÖ'&æ6†g&öÒF†RW†7B6†V6¶÷WBâ ¢¢¢¤W‡V7FVBWf–FVæ6RÆö6F–öâÂ–b¶æ÷vã¢¢¢Æö6Â&W÷6—F÷'’6†V6¶÷WBâ ¢¢¢¥6V&6‚&ööb÷"Væ¶æ÷vã¢¢¢¢¥Væ¶æ÷vã²¢¢6öææV7F÷"Ö&6¶VB–ç7V7F–öâW‡÷6VB6öÖÖ—GFVB6W'fW"ö&¦V7G2öæÇ’à ¢222&WG&÷7V7F—fR…&ö6W72 ¢2222v†BvVçBvVÆÀ ¢¢F†RÆææVBFWVæFVæ7’6†–âv2&VfÆV7FVB–ââGG&–'WF&ÆR"6WVVæ6S¢–FVçF—G’f—'7BÂFWFW&Ö–æ—6ÒôræW‡BÂ&WW6&ÆR&–Ç2ÂD"ô&öG”w&‚÷7GW&RÂÖVB66†RÂF†Vâ&VÆV6R&–æF–ærâ¢¤Wf–FVæ6Rö–çFW#¢¢¢v–âcõbÔ6æöâõ&Wó¢–çFVæFVBFWVæFVæ7’÷&FW"â'F–f7B(i"#b–×ÆVÖVçFF–öâÆâ„DRÔU”33‚æÖF(i"W†V7WF–öâÆæ²W–2GG&–'WF–öâ(i"c"ã(	3"ã‚æBv—D‡V""Â33Cn(	5Â33S’ÖWFFFâ ¢¢c&V6÷&FVB–×ÆVÖVçFF–öâæB&VÖVF–F–öâ6W&FVÇ’ÂÖ¶–ær÷&–v–æÂ–çFVçBÂ&Wf–Wrf–æF–æw2ÂæBÆFW"7FFRF—7F–æwV—6†&ÆRâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãÂ"ã2Â"ãRÂ"ãrÂ"ãrÂ"ã#â ¢¢F†RWf–FVæ6RWFFW"&V6ÖR6–ævÆR÷væW'6†—ö–çBf÷"‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"ÂæB6VçF–æVÇ2Â&VGV6–ær–æFWVæFVçB6ö×æ–öâG&–gBâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãR’E"Ô4äôâÓ‚(i"WFFW"÷væW'6†—æBöæR×'Vâö6†V6²ÖöæÇ’6WVVæ6S²&Wò(i"FööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç–â ¢¢F—&V7BÖöæÇ’Wf–FVæ6RæB†—7F÷&–6Â'&–FvRWf–FVæ6R&V6V—fVB6W&FR–FVçF—F–W2æBÖVæ–æw2&F†W"F†â&V–ær6–ÆVçFÇ’&WW6VBâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã2’E"Ô4äôâÓb(i"(	ÄÕU5B†fR6W&FR–FVçF—F–W2Â÷væW'2ÂÖVæ–æw2ÂæB&VÆV6R&VF–6FW>(	Ó²&Wò(i"F—&V7B×6VÆV7F–öâ6æ6†÷BæBõ2Ó–æFW‚6Æ76–f–6F–öââ ¢¢Öæ–fW7BÖFW&—fVB–FVçF—G’ÇW2W‡FW&æÂGFW7FF–öâ&VÖ÷fVBF†RG&6¶VB6VÆb×&VfW&Væ6RVFvRg&öÒ&VÆV6RWf–FVæ6Râ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãb’(i"(	ÄæòVFvRÖ’ö–çBg&öÒvVæW&FVBGFW7FF–öâ&6²–çFòG&6¶VB6÷W&6^(	Ó²&Wò(i"6FÆöröÖæ–fW7Bæ§6öæÂGFW7FF–öâ'V–ÆFW"â ¢¢f–æÂFö72&V6öæ6–Æ–F–öâö67W'&VBgFW"F†R–×ÆVÖVçFF–öâöWf–FVæ6RÖW&vRæBæ÷rÖF6†W27W'&VçB&Wò7W&f6W2â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i""Â33c‚æB6ö×&R"Â33crÖW&vRFò7W'&VçB„TB(i"W†7FÇ’V–v‡BFö7VÖVçFF–öâõcF‡2à ¢2222v†BF–Bæ÷BvòvVÆÀ ¢¢6WfW&ÂÆææVB"6Æ–6W2&WV—&VB×VÇF—ÆR&VÖVF–F–öâ'3¢"ÓW6VBGvòÖW&vW3²"Ó2F‡&VS²"ÓBGvó²"ÓRF‡&VS²æB"ÓbW‡æFVBg&öÒÂ33S’F‡&÷Vv‚Â33crÇW2õ26öÖÖ—G2â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"v—D‡V""öÖW&vRÖWFFFÂ33Cn(	5Â33cs²c(	B„DR'V–ÆBæ÷FW2(i""ãÂ"ã2Â"ãRÂ"ãrÂ"ãrÂ"ã#â ¢¢"Â33SN(	—2f–æÂÖ†VBv÷&¶fÆ÷rf–ÆVB&Vf÷&R"Â33SR&W—&VBÖÆf÷&ÖVBÖ—'&÷"÷'VçF–ÖR×Fö¶VâWf–FVæ6Râ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"7F–öç2'Vâ#“CS3#S#c–(i"f–ÇW&S²c(	B„DR'V–ÆBæ÷FW2(i""ãR’(i"ÖÆf÷&ÖVBÖ—'&÷"öÖ—76–ær'VçF–ÖR×Fö¶Vâf–æF–æræB&VÖVF–F–öââ ¢¢"Â33C’†2Vç&W6öÇfVB4’&÷fVææ6R&V6W6Rc(	—27V66W72æ÷FR6öæfÆ–7G2v—F‚7F–öç2'Vâ#“#c3C#s“3â¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã#²&Wò(i"'Vâ#“#c3C#s“3â ¢¢F†R÷&–v–æÂ"ÓBôõ2Óõ"ÓbFW6–vâ&VÆ–VBöâ'&–FvR&—G“²cÆFW"&WF—&VBF†B7F—fRG&ç7÷'BÂ&öGV6–ær7V'7FçF–ÂF—&V7BÖöæÇ’&VÖVF–F–öâÆ–æVvRâ¢¤Wf–FVæ6Rö–çFW#¢¢¢v–âcõbÔ6æöâõ&Wó¢–çFVæFVB"ÓBôõ2ÓG&ç7÷'BFW6–vââ'F–f7B(i"#b–×ÆVÖVçFF–öâÆâ„DRÔU”33‚æÖF(i""ÓBôõ2Ó–çFVçC²c(	B„DR'V–ÆBæ÷FW2(i""ã’Â"ã"Â"ãrâ ¢¢c"ã#æVVFVB"ã#Fò6÷'&V7B&÷F‚—G2F—7FFVÖVçBæBf—fR×&÷rc’–çfVçF÷'“²7W'&VçB&Wò†26–æ6RGfæ6VBv–âF‡&÷Vv‚cöFö726öÖÖ—G2â¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã#’c&VÖVF–F–öâ76W76ÖVçB(i"(	Ä—G2Ö–æF—7FFVÖVçB—27FÆR(
bæB—G2f—fR×&÷rc’6Æ÷7W&RÆ—7B—2–æ6ö×ÆWF^(	Ó²&Wò(i"7W'&VçB„TBæB6ö×&Rg&öÒF#3Sž(
fâ ¢¢†—7F÷&–6Âõ2&÷fVææ6R6öçF–ç2Ö—6ÆVF–ær6öÖÖ—BF—FÆS¢&Ss“ƒ3>(
f6—2õ2Ó"'WB6†ævW2õ2ÓF‡2â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"6öÖÖ—BÖWFFFö6†ævVBF‡2f÷"&Ss“ƒ33S3&#f&Cvf3–c#vf3S#ƒCCCc–æBf&#c3“ƒ“ƒ“ƒS†3v&†3c–cCFcVC†fà ¢2222v†BvRÆV&æVB…&ö6W72 ¢¢ÆâW7F&Æ—6†W2–çFVæFVBFV6ö×÷6—F–öâÂæ÷B†—7F÷&–6ÂW†V7WF–öã²"ÖWFFFõcöv—B†—7F÷'’&R&WV—&VBf÷"GG&–'WF–öââ¢¤Wf–FVæ6Rö–çFW#¢¢¢7WÆVÖVçFÂv÷ö–çFW"–âW†V7WF—fR7VÖÖ'“²&Wò(i"ö'6W'fVB"6WVVæ6S²c(i"†—7F÷&–6ÂFFVæFâ ¢¢&Wf–Wr×7V66W72FW‡B×W7B&R&V6öæ6–ÆVBv—F‚'VâÖÆWfVÂ7F–öç2FFÂ–æ6ÇVF–ær&W'Vç2Â&Vf÷&RW6R2†—7F÷&–6Â4’f7Bâ¢¤Wf–FVæ6Rö–çFW#¢¢¢"Â33C’6öæfÆ–7C¢c"ã"fW'7W27F–öç2'Vâ#“#c3C#s“3â ¢¢Wf–FVæ6RÖw&‚6†ævW2&R6fW"v†VâF†R&öGV6W"÷WFFW"÷vç2&÷F‚–æFW†W2æB6VçF–æVÇ2æBF†R&VÆV6R—VÆ–æR6†V6·2&F†W"F†â&W—'2â¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãS²&Wò(i"WFFW"æB7FvRR6†V6²ÖöæÇ’FVf–æ—F–öââ ¢¢&6†—FV7GW&R&W66÷–ær×W7BW‡Æ–6—FÇ’&V6Æ76–g’ö'6öÆWFRWf–FVæ6S²ÆVf–ær'&–FvRÖW&6¶WG2&W6VçBv—F†÷WB†—7F÷&–6ÂÆ&VÇ2v÷VÆB6öægW6R7W'&VçBG&ç7÷'B÷7GW&Râ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã.(	3"ã3²&Wò(i"õ2Ó†—7F÷&–6Â6Æ76–f–6F–öââ ¢¢W‡FW&æÂGFW7FF–öâ&WGFW"f—G2W†7B×6÷W&6R&ööbF†âG&6¶VBFW&—fF—fRv†÷6R'—FW2fVVB—G2÷vâ6÷W&6R–FVçF—G’â¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãc²&Wò(i"GFW7FF–öâ'V–ÆFW.(	—2W‡FW&æÂÖV×G’ÖF—&V7F÷'’wV&Bâ ¢¢W&ÖæVçBc’7FGW2&VÖ–ç26W&FRWF†÷&—G’ÆæS¢–×ÆVÖVçFF–öâöWf–FVæ6R&W6Væ6R6ææ÷BÖ÷fR6÷W&6R7FGW2â¢¤Wf–FVæ6Rö–çFW#¢¢¢c’ãb7W'&VçB7FGW2Æ–æW3²c(	B„DR'V–ÆBæ÷FW2(i""ãRæò×7FGW2Ö6†ævR6ÆW6Rà ¢222&WG&÷7V7F—fR„Æ–6F–öâò7—7FVÒ ¢2222v†BvRÆV&æVB&÷WBF†R7—7FVÒ—G6VÆ` ¢¢F†RFF&6R6VÆV7F–öâ&÷VæF'’—26öæ6VçG&FVB–âD$66W72æf÷%ö7W'&VçEöVçf¢&WF—&VB¶W—2&R&V¦V7FVB&Vf÷&RDD$4UõU$Æ—2&VBÂæBöæÇ’7–6÷u&÷f–FW&—2–ç7FçF–FVBâ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"Væv–æRöF"öFFW"ç–(i"&WF—&VBÖ¶W’6†V6²&Vf÷&RDD$4UõU$Æ&VBÂ7–6÷u&÷f–FW&–×÷'Bö6öç7G'V7F÷#²c(	B„DR'V–ÆBæ÷FW2(i""ã"â ¢¢'VçF–ÖR&VÆV6R–FVçF—G’6âFW&—fRg&öÒöæR6æöæ–6ÂG&6¶VBÖæ–fW7Bv†–ÆR'V–ÆBGFW7FF–öâ&VÖ–ç2W‡FW&æÂFòF†R6÷W&6RG&VRâ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"Væv–æR÷'VçF–ÖRö–FVçF—G’ç–Â6FÆöröÖæ–fW7Bæ§6öæÂFööÇ2öWf–FVæ6Rö'V–ÆE÷&VÆV6UöGFW7FF–öâç–²c(	B„DR'V–ÆBæ÷FW2(i""ãbâ ¢¢F†RWf–FVæ6Rw&‚—26÷WÆVB&öGV7C¢&–Ö&–W2ÂF‚&öög2Â‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"ÂæB6VçF–æVÇ2×W7BÖ÷fRF‡&÷Vv‚öæRWFFW"æB6†V6²ÖöæÇ’—VÆ–æR7FvRâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãS²&Wò(i"WFFW"Â–æFW†W2Â6VçF–æVÇ2Â—VÆ–æR7FvRUÂâ ¢¢ÖVBÖ66†R6fWG’FWVæG2öâ6W&F–ærÖ–ærg&öÒW'6—7FVæ6S¢öæÇ’W‡Æ–6—BW6W'B6âw&—FRÂF†R7F÷&VB&öG’—2&ö¦V7FVB„DR–ÆöBÂ&VBÖ&6²—26æöæ–6Æ—¦VBÂæB&öGV7F–öâÖÆ–¶R6öçFW‡G2&R&VgW6VBâ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"Væv–æRö&öG–w&‚÷&W6öÇfW"ç–ÂVæv–æRö&öG–w&‚öÖVEö66†Rç–ÂVæv–æRö6Æ’öÖ–âç–²c(	B„DR'V–ÆBæ÷FW2(i""ã~(	3"ã‚â ¢¢r&ööb&÷WF–ær—26FÆörÖG&—fVâ&F†W"F†â–æfW'&VBg&öÒVæGö–çB6–Ö–Æ&—G“²7W'&VçB&WòFW6–væFW2tUB÷&VFW&æBW†6ÇVFW2ö–çFW&æÂ÷fW'6–öæâ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"Fö72ôTäEô”åE5ô4DÄôræ§6öæ²crÔ6æöâÔ„DRÔæ'&F—fW2ÔwV–FRÂ*vG&ç7÷'B÷7GW&R‡&÷WFRÖöæÇ“²F—FÆW2ÖöæÇ’–â ¢¢†—7F÷&–6ÂWf–FVæ6R&VÖ–ç2W6VgVÂgFW"&6†—FV7GW&R&WF—&VÖVçBöæÇ’v†Vâ—G2–FVçF—G’æBvFRÖVæ–ær&RV&çF–æVBâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã3²&Wò(i"õ2Ó†—7F÷&–6Â–æFW‚&÷w2æBF—&V7B×6VÆV7F–öâ&–Ö'’â ¢¢õ2Ó2FVÖöç7G&FW2F†B÷W&F–öæÂ÷7GW&RæBWf–FVæ6RFÖ—76–öâ&R6W&FS¢F†R÷W&F÷"6¶WB&V6÷&G2F—&V7B&VBÖöæÇ’6GW&RÂv†–ÆR"Â33cr÷vç2WFFW"ô–æFW‚ôÖ—'&÷"FÖ—76–öââ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãž(	3"ã#²&Wò(i"õ2Ó26¶WBÂ÷W&F÷"&V6÷&BÂæB"Â33crF–fbà ¢2222¶æ÷vâ&VÖ–æ–ær&—6·2òFV'@ £â¢¤6FVv÷'“¢6†÷VÆBÖf—‚¢¢ ¢¢¢¥&—6²÷"FV'C¢¢¢c’ãb7F–ÆÂFW67&–&W2'&–FvRfÆÆ&6²÷&÷f–FW"&—G’æBFö¶VâDUeôD%ô%$”DtUôdÄÄ$4µôô¶Âv†–ÆRcö7W'&VçB&Wò&RF—&V7BÖöæÇ’â ¢¢¢¥v‡’—BÖGFW'3¢¢¢W&ÖæVçB†6RwV–Fæ6R6âÖ—7&÷WFRgWGW&RÆææ–ærWfVâF†÷Vv‚c7W'&VçFÇ’7WW'6VFW2F†RW†7BF÷–2â ¢¢¢¤Wf–FVæ6Rö–çFW"÷"Væ¶æ÷vã¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂ*v7V'F6²„DRÔD•5CãB(	BD"÷7GW&Rb'VçF–ÖR6†V6·2††&æW72f÷"„DRÔdU$ÓB–ò*v7V'F6²„DRÔD•5CãR(	B&öG”w&‚ÖV6†æ–72vFW6²c(	B„DR'V–ÆBæ÷FW2(i""ã#²&Wò(i"Væv–æRöF"öFFW"ç–â £"â¢¤6FVv÷'“¢6†÷VÆBÖf—‚¢¢ ¢¢¢¥&—6²÷"FV'C¢¢¢c’ãbæÖW2'F–f7G2÷&öög2÷6æ—G•÷—VÆ–æRçG&ç67&—BæÆövæBvVæW&–26WVVæ6RÂv†–ÆRcö7W'&VçB&WòW6RVF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆövæBæ–æWFVVâ÷&FW&VB7FvW2â ¢¢¢¥v‡’—BÖGFW'3¢¢¢Wf–FVæ6R×F‚æB6WVVæ6RG&–gBvV¶Vç2&WVF&ÆR–çFW'&WFF–öââ ¢¢¢¤Wf–FVæ6Rö–çFW"÷"Væ¶æ÷vã¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂ*v7V'F6²„DRÔD•5Cãb(	BöæRÖ'WGFöâWf–FVæ6R†&æW72b&VÆV6R6æ—G’—VÆ–æV²c(	B„DR'V–ÆBæ÷FW2(i""ãS²&Wò(i"7W'&VçB—VÆ–æR67&—BöÆörâ £2â¢¤6FVv÷'“¢6†÷VÆBÖf—‚¢¢ ¢¢¢¥&—6²÷"FV'C¢¢¢7W'&VçBc"ã#(	—2F——2†—7F÷&–6ÂÖB×&Wf–Wr†s–CF&(
f’Âv†–ÆR7W'&VçB&Wò—2S“C#&c(
f²F†R–çFW'fVæ–ærF‡&VR6öÖÖ—G2&RcöFö726†ævW2â ¢¢¢¥v‡’—BÖGFW'3¢¢¢Æ—fRFFVæF6†÷VÆBF—7F–æwV—6‚F†Rf–æÂ–×ÆVÖVçFF–öâöWf–FVæ6RÖW&vRg&öÒÆFW"7W'&VçB×7FFRFö7VÖVçFF–öââ ¢¢¢¤Wf–FVæ6Rö–çFW"÷"Væ¶æ÷vã¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã#(i"(	Ä7W'&VçBF—¢s–CF&(
f(	Ó²&Wò(i"6ö×&RF#3Sž(
fFòS“C#&c(
fæB7W'&VçBÖ–æâ £Bâ¢¤6FVv÷'“¢6†÷VÆBÖf—‚¢¢ ¢¢¢¥&—6²÷"FV'C¢¢¢"Â33Cž(	—2†—7F÷&–6Â4’&V6÷&B—26öæfÆ–7F–ærâ ¢¢¢¥v‡’—BÖGFW'3¢¢¢&WG&÷7V7F—fRfÆ–FF–öâ6Æ–×26ææ÷B&RG&6VBFòöæRWF†÷&—FF—fR'Vââ ¢¢¢¤Wf–FVæ6Rö–çFW"÷"Væ¶æ÷vã¢¢¢¢¥Væ¶æ÷vã¢¢¢c"ã"&V6÷&G27V66W76gVÂf—6–&ÆR6†V6·3²&Wò'Vâ#“#c3C#s“3&V6÷&G2Gvòf–ÆVB¦ö'2â ¢¢¢¤Wf–FVæ6RæVVFVBÂv†VâVæ¶æ÷vã¢¢¢gVÆÂ'Vâ÷&W'Vâ†—7F÷'’æBÆöw2f÷"†VB“3v3†#C3SfCFcF#3&S“Fc&6FC##ƒC–#3#–â £Râ¢¤6FVv÷'“¢6†÷VÆBÖf—‚¢¢ ¢¢¢¥&—6²÷"FV'C¢¢¢õ2Ó2Æ6·2W†7BW†V7WFVB&÷f—6–öæ–ær5Â'—FW2æBgVÆÂ&—f–ÆVvRöFVfVÇB×&—f–ÆVvRw&‚â ¢¢¢¥v‡’—BÖGFW'3¢¢¢6GW&R÷7GW&R—2Wf–FVæ6VBÂ'WB&—f–ÆVvR&÷fVææ6R&VÖ–ç2&÷VæFVBâ ¢¢¢¤Wf–FVæ6Rö–çFW"÷"Væ¶æ÷vã¢¢¢¢¥Væ¶æ÷vã¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã’Wf–FVæ6RÆ–Ö—FF–öç2â ¢¢¢¤Wf–FVæ6RæVVFVBÂv†VâVæ¶æ÷vã¢¢¢–Ö×WF&ÆR&÷f—6–öæ–ærG&ç67&—BæBgVÆÂw&çG2öFVfVÇB×&—f–ÆVvW2–çfVçF÷'’â £bâ¢¤6FVv÷'“¢æ–6R×FòÖ†fR¢¢ ¢¢¢¥&—6²÷"FV'C¢¢¢†—7F÷&–6Âõ26öÖÖ—BæÖ–ærFöW2æ÷B6öç6—7FVçFÇ’ÖF6‚6†ævVB6¶WBF‡2â ¢¢¢¥v‡’—BÖGFW'3¢¢¢Æ–æVvR&V6öç7G'V7F–öâF¶W2FF—F–öæÂ6öÖÖ—B÷F‚–ç7V7F–öââ ¢¢¢¤Wf–FVæ6Rö–çFW"÷"Væ¶æ÷vã¢¢¢&Wò(i"&Ss“ƒ33S3&#f&Cvf3–c#vf3S#ƒCCCc–F—FÆR÷F‚Ö—6ÖF6ƒ²f&#c3“ƒ“ƒ“ƒS†3v&†3c–cCFcVC†f–çG&öGV6W27W'&VçBõ2Ó"F‡2à ¢2226æöâÆ–væÖVçBæBFö7VÖVçFF–öâ÷WF6öÖW0 ¢2222Rã6æöâ&VfW&Væ6W2W6V@ ¢¢¢¥c(	B„DR'V–ÆBæ÷FW2Â*s’g&öçBÖGFW#²*s"ã"’rÖ'&–FvRæBD%Åô%$”DtUÅõU$ÂFW&V6F–öâæB&WF—&VÖVçBÂÒF—&V7B÷7Fw&U5Â—2F†R6öÆR7F—fR„DRFF&6RG&ç7÷'C²*s"ã2’„DRÔU”33‚÷7BÕ#3S’&VÖVF–F–öâ(	BE"Ô4äôâÓbF—&V7BÔöæÇ’6VÆV7F–öâWf–FVæ6RæB†—7F÷&–6Â'&–FvRV&çF–æS²*s"ãR’„DRÔU”33‚÷7BÕ#3S’&VÖVF–F–öâ(	BE"Ô4äôâÓ‚F—&V7BÔöæÇ’c’ãb6ö×ÆWF–öâ6VÖçF–72æB"Óe"÷væW'6†—²*s"ãb’„DRÔU”33‚"Óe"ÔÖW&vR(	B66Æ&ÆRÖæ–fW7BÔFW&—fVB&VÆV6R–FVçF—G’ÂW‡FW&æÂGFW7FF–öâÂæB÷'F&ÆRWf–FVæ6R6VÖçF–73²*s"ã’’"Ób&VÖVF–F–öâÂÒ„DRÔU”33‚õ2Ó2(	BWF†÷&—¦VB&VFW"Õ&öÆR&÷f—6–öæ–ærÂF—&V7B&VBÔöæÇ’6GW&RÂæBWf–FVæ6RÔFÖ—76–öâ&÷VæF'“²*s"ã#’"Ób&VÖVF–F–öâ"Óe"Ô"„DRÔU”33ƒ²*s"ã#’"Ób&VÖVF–F–öâ7FFRâ¢¢g&öçBÖGFW"–FVçF–f–W2fW'6–öâc"ãBãÂ7FGW2Æ—f–ævÂW†7B×F÷–2ÖöæÇ’WF†÷&—G’ÂæBF†RÆFW7BÖFFVæGVÒ'VÆS¢(	Ä–b×VÇF—ÆRFFVæFFG&W72F†R6ÖR÷"÷fW&Æ–ær66÷RÂF†R†–v†W7BÖçVÖ&W&VBòÆFW7BFFVæGVÒ—2F†RöæÇ’WF†÷&—FF—fRöæRî(	ÒF†W6R6V7F–öç2v÷fW&æVBÆ—fRFFVæFæBc×&V6÷&FVB†—7F÷'“²F†W’vW&Ræ÷BW6VBFò7V'7F—GWFRf÷"7W'&VçB&Wò–ç7V7F–öââ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i"g&öçBÖGFW"(i"(	ÅG&VB—B2F†R7W'&VçB6÷W&6RöbG'WF‚öæÇ’f÷"F†R7V6–f–2—FV×2—BW‡Æ–6—FÇ’6÷fW'>(	ÒÂ(	Ä–bF÷–2FöW2æ÷BV"–âF†RÆFW7BcÂF†Vâc†2æ÷F†–ærFò6’&÷WB—Bî(	Ò ¢¢¢¥c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂ*v7V'F6²„DRÔD•5CRã(	B6æöæ–6ÂVæ6öF–æw2bVçf—&öæÖVçB–ç6²*v7V'F6²„DRÔD•5CRã"(	BvÆö&Â–æFW‚bÖ—'&÷"F—66—Æ–æV²*v7V'F6²„DRÔD•5CãB(	BD"÷7GW&Rb'VçF–ÖR6†V6·2††&æW72f÷"„DRÔdU$ÓB–²*v7V'F6²„DRÔD•5CãR(	B&öG”w&‚ÖV6†æ–72vFW6²*v7V'F6²„DRÔD•5Cãb(	BöæRÖ'WGFöâWf–FVæ6R†&æW72b&VÆV6R6æ—G’—VÆ–æV²*v7V'F6²„DRÔD•5Cã’(	BD.(	6'&–FvR&—G’bVçb6öææV7F—f—G–²*v7V'F6²„DRÔD•5Cã(	B&6†—FV7GW&R6æ6†÷B†¶W—2ÖöæÇ’’Wf–FVæ6V²*v7V'F6²„DRÔD•5Cã(	Bc"ÖVBÖ66†RW'6—7FVæ6R†&FVæ–ævâ¢¢v÷fW&æVBF†RV–v‡BW†7B7W'&VçB6÷W&6R7FGW6W2æBW‡÷6VBW&ÖæVçBÖ6æöâG&–gC²æò7FGW2v2–æfW'&VBg&öÒ&Wòõcâ ¢¢¢¥crÔ6æöâÔ„DRÔæ'&F—fW2ÔwV–FRÂ*vG&ç7÷'B÷7GW&R‡&÷WFRÖöæÇ“²F—FÆW2ÖöæÇ’–²*vRã&VFW"c÷7GW&R(	B&æG2ÖöæÇ“²æ'&F—fRÖg&VVâ¢¢v÷fW&æVBF†R–çFW'&WFF–öâF†Br7V66W72&ööbW6W26FÆövVB¥4ôâ7V66W72&÷WFRÂW†6ÇVFW2ö–çFW&æÂ÷fW'6–öæÂæBFöW2æ÷B–×Ç’&VFW"æ'&F—fRW‡ç6–öâà ¢2222Rã"&÷÷6VBcFFVæF†6öçF–âG&–âF&vWG2òFö2FVÇF–çFVçG2 ¢222226æF–FFS¢÷7BÕ"Â33c‚F—F—7F–æ7F–öâæBV–v‡B×&÷rF—7F–ÆÆF–öâG&–ævP ¢¢¢¥7FGW3¢¢¢$õõ4TBÂæ÷B6æöâ ¢¢¢¤FFVæGVÒF—FÆS¢¢¢„DRÔU”33‚÷7BÖFö7VÖVçFF–öâF—F—7F–æ7F–öâæBF—7F–ÆÆF–öâ&÷r6öç6öÆ–FF–öæ ¢¢¢¤Wf–FVæ6R&6—3¢¢¢c"ã#&V6÷&G2F—s–CF&css3#ƒ3SCs#V33CScs3sFF&æB6÷'&V7G2F†R–çfVçF÷'’FòV–v‡B&÷w3²7W'&VçB&Wò—2S“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†²6ö×&Rg&öÒ"Â33cr&WGW&ç2F‡&VRÆFW"6öÖÖ—G2æBV–v‡BFö7VÖVçFF–öâõcF‡2âc’ãb&WF–ç2'&–FvRÖW&æBgWGW&RÖVBÖ66†Rv÷&F–ærâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã#²&Wò(i"7W'&VçB„TBæB6ö×&RF#3Sž(
bââæS“C#&c(
f²c’ãbW†7BV–v‡B&÷r6V7F–öç2â ¢¢¢¥v‡“¢¢¢7W'&VçBcW†7B×F÷–2v÷&F–æræVVG2Æ—fR7W'&VçB×F—6Æ&–f–6F–öâÂæB7W'&VçBc’ãb6öçF–ç2Wf–FVæ6VBG&ç7÷'BÂWf–FVæ6R×F‚ÂæBÖVBÖ66†RG&–gBâ ¢¢¢¤FV6—6–öâÂ'VÆRÂ÷"6Æ&–f–6F–öã¢¢¢F—7F–æwV—6‚"Â33crÖW&vRF#3S–&36c“V33S“Ssffs33–S““c&2F†Rf–æÂ–×ÆVÖVçFF–öâöWf–FVæ6R–çFVw&F–öâö–çBg&öÒc&Wf–WrF—s–CF&css3#ƒ3SCs#V33CScs3sFF&æBFö72×&V6öæ6–ÆVB7W'&VçBF—S“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†²&W6W'fRÆÂV–v‡BÖVBc’ãb&÷w2æBF†V—"6÷W&6R7FGW6W3²7FvRF—&V7BÖöæÇ’Âæ–æWFVVâ×7FvRÂæB&÷VæFVBÖVBÖ66†Rv÷&F–ærf÷"W&ÖæVçBG&–ævRv—F†÷WB6Æ–Ö–ær7FGW2Ö÷fVÖVçBâ ¢¢¢¤G&–âF&vWG3¢¢¢ ¢¢¢¥bFö7VÖVçBF—FÆS¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öæ ¢¢¢¥6V7F–öâÂöæÇ’v†Vâ6÷–VBfW&&F–Ó¢¢¢F†RV–v‡BW†7B7V'F6²†VF–æw2Æ—7FVB–âRãâ ¢¢¢¤FVÇF–çFVçC¢¢¢&WÆ6R7F—fR'&–FvR÷&÷f–FW"×&—G’æBöÆB—VÆ–æR×F‚÷7GW&Rv—F‚F—&V7BÖöæÇ’ö†—7F÷'’×V&çF–æRö7W'&VçB×—VÆ–æRv÷&F–æs²Æ–vâ„DRÔD•5Cãv—F‚&÷VæFVB–×ÆVÖVçFVBæöç&öGV7F–öâÖVBÖ66†R&V†f–÷"v†–ÆRÆVf–ær6÷W&6R×7FGW2FV6—6–öç2FòF†Rc’ÆæRâ ¢¢¢¥bFö7VÖVçBF—FÆS¢¢¢„DR66†VÖ2æB'F–f7G6 ¢¢¢¤FVÇF–çFVçC¢¢¢6–ævÆRÖ†öÖRF—&V7B×6VÆV7F–öâ66†VÖö'F–f7B–FVçF—G’ÂW‡FW&æÂÖGFW7FF–öâ÷F‚×&ööb6VÖçF–72ÂæB7W'&VçB—VÆ–æRÖÆörF‚â ¢¢¢¥bFö7VÖVçBF—FÆS¢¢¢„DRÖV6†æ–72wV–FV ¢¢¢¤FVÇF–çFVçC¢¢¢6–ævÆRÖ†öÖRF—&V7BÖöæÇ’6VÆV7F÷"æB&÷VæFVBÖVBÖ66†R'VçF–ÖRÖV6†æ–72â ¢¢¢¥bFö7VÖVçBF—FÆS¢¢¢vÆ÷rwV–FV ¢¢¢¤FVÇF–çFVçC¢¢¢6–ævÆRÖ†öÖRf–æÂæ–æWFVVâ×7FvRæBW‡FW&æÂÖGFW7FF–öâfÆ–FF–öâ6VÖçF–72v—F†÷WB6öçfW'F–ærWf–FVæ6R&W6Væ6R–çFò66WFæ6Râ ¢¢¢¥bFö7VÖVçBF—FÆS¢¢¢„DRv÷fW&ææ6V ¢¢¢¤FVÇF–çFVçC¢¢¢&WF—&R'&–FvR×Fö¶Vâ6VÖçF–72Â&W6W'fRWf–FVæ6RÖ÷væW"öæöæ6Æ–Ò&÷VæF&–W2ÂæB&÷WFRW†7B×6÷W&6RW‡FW&æÂÖGFW7FF–öâv÷fW&ææ6Râ ¢¢¢¥7WW'6VFW2÷"6öæfÆ–7G2Â–bÆ–6&ÆS¢¢¢6Æ&–f–W2c"ã#(	—2†—7F÷&–6ÂÖB×&Wf–WrF—²7FvW2G&–ævRf÷"c’ãb'&–FvRfÆÆ&6²÷&÷f–FW"&—G’ÂDUeôD%ô%$”DtUôdÄÄ$4µôô¶ÂöÆB6æ—G’ÖÆörF‚ÂæBgWGW&RÖöæÇ’ÖVBÖ66†Rv÷&F–ærâ ¢¢¢¤–×ÆVÖVçFF–öâ–×7C¢¢¢Fö7VÖVçFF–öâöv÷fW&ææ6R6Æ&–f–6F–öã²F†RW†7B÷7BÕÂ33cr6ö×&R&WGW&ç2Fö7VÖVçFF–öâõcF‡2öæÇ’â ¢¢¢¥Væ6W'F–âG&–âF&vWG2ÂöæÇ’v†VâæVVFVC¢¢¢W†7BW&ÖæVçB6V7F–öç2–â„DR66†VÖ2æB'F–f7G6Â„DRÖV6†æ–72wV–FVÂvÆ÷rwV–FVÂæB„DRv÷fW&ææ6VvW&Ræ÷B&WG&–WfVC²F—FÆW26öÖRg&öÒc"ãn(	—2æÖVBG&–ævR†öÖW2à ¢2222Rã2Fö¶VâæBWf–FVæ6R6VÖçF–70 ¢22222'&–FvRÖfÆÆ&6²Fö¶VâG&–g@ ¢¢¢¤ö'6W'fVBG&–gC¢¢¢7W'&VçBc’ãbÆ—7G2W†7BFö¶VâæÖRDUeôD%ô%$”DtUôdÄÄ$4µôô¶Âv†–ÆR7W'&VçBW†7B×F÷–2c&WF—&W2'&–FvRfÆÆ&6²æB7W'&VçB&Wò&VgW6W2&WF—&VB¶W—2&Vf÷&RF—&V7B×&÷f–FW"6öç7G'V7F–öââæòFö¶Vâ6F—6f7F–öâ—26Æ–ÖVBâ ¢¢¢¤v÷fW&æ–ær6÷W&6S¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã"’rÖ'&–FvRæBD%Åô%$”DtUÅõU$ÂFW&V6F–öâæB&WF—&VÖVçC²7W'&VçB&Wòf÷"–×ÆVÖVçFF–öâ&VÆ—G’â ¢¢¢¤Wf–FVæ6R&6—3¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂ*v7V'F6²„DRÔD•5CãR(	B&öG”w&‚ÖV6†æ–72vFW6(i"DUeôD%ô%$”DtUôdÄÄ$4µôô¶²&Wò(i"Væv–æRöF"öFFW"ç–â ¢¢¢¥&VÆFVB&÷÷6VBcFFVæGVÓ¢¢¢„DRÔU”33‚÷7BÖFö7VÖVçFF–öâF—F—7F–æ7F–öâæBF—7F–ÆÆF–öâ&÷r6öç6öÆ–FF–öæâ ¢¢¢¤Æ–¶VÇ’G&–âF&vWB'’F—FÆS¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öæ²„DRv÷fW&ææ6Vâ ¢¢¢¤W†7BÆö6F÷"ÂöæÇ’v†Vâ6÷–VBfW&&F–Ó¢¢¢*v7V'F6²„DRÔD•5CãR(	B&öG”w&‚ÖV6†æ–72vFW6à ¢22222&VÆV6R×6æ—G’F‚÷6WVVæ6RG&–g@ ¢¢¢¤ö'6W'fVBG&–gC¢¢¢c’ãbæÖW2'F–f7G2÷&öög2÷6æ—G•÷—VÆ–æRçG&ç67&—BæÆövæBvVæW&–26WVVæ6S²7W'&VçBcõ&WòW6RVF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆövæBW†7FÇ’æ–æWFVVâ÷&FW&VB7FvW2â ¢¢¢¤v÷fW&æ–ær6÷W&6S¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãR’E"Ô4äôâÓƒ²&Wòf÷"7W'&VçBF‚÷67&—Bâ ¢¢¢¤Wf–FVæ6R&6—3¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâÂ*v7V'F6²„DRÔD•5Cãb(	BöæRÖ'WGFöâWf–FVæ6R†&æW72b&VÆV6R6æ—G’—VÆ–æV²&Wò(i"FööÇ2öWf–FVæ6R÷'Vå÷6æ—G•÷—VÆ–æRç–ÂVF—BövFW2÷6æ—G•÷—VÆ–æR÷6æ—G•÷—VÆ–æRæÆövâ ¢¢¢¥&VÆFVB&÷÷6VBcFFVæGVÓ¢¢¢„DRÔU”33‚÷7BÖFö7VÖVçFF–öâF—F—7F–æ7F–öâæBF—7F–ÆÆF–öâ&÷r6öç6öÆ–FF–öæâ ¢¢¢¤Æ–¶VÇ’G&–âF&vWB'’F—FÆS¢¢¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öæ²vÆ÷rwV–FV²„DR66†VÖ2æB'F–f7G6â ¢¢¢¤W†7BÆö6F÷"ÂöæÇ’v†Vâ6÷–VBfW&&F–Ó¢¢¢*v7V'F6²„DRÔD•5Cãb(	BöæRÖ'WGFöâWf–FVæ6R†&æW72b&VÆV6R6æ—G’—VÆ–æVà ¢2226Æ÷7W&RWf–FVæ6R6æ6†÷B†f÷"ÆVBFV6—6–öâ ¢2222bãWf–FVæ6R&öGV6V@ ¢¢¢¤–FVçF—G’÷&VÆV6S¢¢¢6FÆöröÖæ–fW7Bæ§6öæÂ'F–f7G2ö–FVçF—G’÷6W'f–6Uö–FVçF—G’æ§6öæÂÖæ–fW7BÖFW&—fVB'VçF–ÖR–FVçF—G’6öFRÂW‡FW&æÂÖGFW7FF–öâ'V–ÆFW"÷66†VÖ÷FW7G2â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"W†7BF‡3²c(	B„DR'V–ÆBæ÷FW2(i""ãbâ ¢¢¢¤FWFW&Ö–æ—6Òôr÷&–Ç3¢¢¢FWFW&Ö–æ—6ÒFW7G2ö'F–f7G2ÂFö72ôTäEô”åE5ô4DÄôræ§6öæÂ&–Ç2–çFVw&F–öâFW7BöWf–FVæ6R7W&f6W2â¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã.(	3"ã3²&Wò(i"FW7G2öWf–FVæ6R÷FW7EöFWFW&Ö–æ—6ÕövFU÷&öög2ç–ÂFW7G2öWf–FVæ6R÷FW7E÷&–Ç5ö6•÷v÷&¶fÆ÷uö–çFVw&F–öâç–ÂVæGö–çB6FÆörâ ¢¢¢¤Vçf—&öæÖVçBö&6†—FV7GW&S¢¢¢'F–f7G2öVF—BöVçböVçe÷6æ6†÷Bæ§6öæ†c6’æB'F–f7G2ö&6†—FV7GW&Rö&6†—FV7GW&U÷6æ6†÷Bæ¶W—5ööæÇ’æ§6öæâ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"&÷F‚'F–f7G2æBö'6W'fVBf–VÆG2â ¢¢¢¤F—&V7BD#¢¢¢'F–f7G2÷'VçF–ÖRöF—&V7EöF%÷6VÆV7F–öâç6æ6†÷Bæ§6öæÂ—G266†VÖÂF—&V7B6VÆV7F÷"Â7FF–26öçG&7B6†V6²ÂæBFW7G2â¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã.(	3"ã3²&Wò(i"W†7BF—&V7BÔD"F‡2â ¢¢¢¤ÖVB66†Rôõ2Ó#¢¢¢'F–f7G2ö&öG–w&‚÷c%öÖVEö66†RöÖæ–fW7Bæ§6öæÂ&÷VæB&–Ö&–W2÷66†VÖ2ÂÖVBÖ66†RÖöGVÆW2÷FW7G2ÂæBVF—Bö÷2ö†FRÖW–33‚ö÷2Ó"öâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã~(	3"ã‚Â"ãS²&Wò(i"W†7BF‡2â ¢¢¢¤õ2Ó3¢¢¢FVâ&–Ö'’6¶WBf–ÆW2Â6WfVâ66†VÖ2Â6†V6·7V×2ÂfÆ–FF–öâ&V6V—BÂæB6W&FR÷W&F÷"&V6÷&Bâ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ãBÂ"ãž(	3"ã#²&Wò(i"VF—Bö÷2ö†FRÖW–33‚ö÷2Ó2öæBVF—Bö÷2ö†FRÖW–33‚ö÷2Ó2Ö÷W&F÷"×&V6÷&Böâ ¢¢¢¤–æFW‚ôÖ—'&÷#¢¢¢‡VÖâ–æFW‚ÂÖ6†–æRÖ—'&÷"ÂGvò6VçF–æVÇ2Â“B„DRÔU”33‚×&VÆFVB—'2–âV6‚7W'&VçB–æFW‚â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"f÷W"W†7Bf–ÆW2æB&VBÖöæÇ’—"6ö×&—6öã²c(	B„DR'V–ÆBæ÷FW2(i""ãR÷væW'6†—â ¢¢¢¥&VÆV6RvFS¢¢¢7W'&VçBæ–æWFVVâ×7FvR67&—BöÆörÂv—F‚6÷W&6RV÷FF–öâ'7VÖÖ'“¥52&ÂæB7V66W76gVÂf–æÂÖ†VBv÷&¶fÆ÷r'Vç2f÷"'2Â33cbÂÂ33crÂæBÂ33c‚â¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i"—VÆ–æR67&—BöÆös²7F–öç2'Vç23SSCƒVÂ3scSƒ“#6Â3#Cccs3ƒvâ ¢¢¢¤†—7F÷&–6Â6Æ76–f–6F–öã¢¢¢õ2Ó6¶WB&VÖ–ç2&W6VçBæB–æFW†VB2†—7F÷&–6Â'&–FvRWf–FVæ6Râ¢¤Wf–FVæ6Rö–çFW#¢¢¢c(	B„DR'V–ÆBæ÷FW2(i""ã.(	3"ã3²&Wò(i"VF—Bö÷2ö†FRÖW–33‚ö÷2ÓöæB–æFW‚&÷w2â ¢¢¢¤Fö7VÖVçFF–öã¢¢¢7W'&VçB6WfVâÖf–ÆR"Â33c‚&V6öæ6–Æ–F–öâæBæöâÖ6æöæ–6ÂFö2ÖFVÇF&÷÷6ÂVF—BöFö6FVÇF2ö†FRÖW–33…÷c•ö÷5öFVÆVvF–öåöÖVæFÖVçE÷&÷÷6ÂæÖFâ¢¤Wf–FVæ6Rö–çFW#¢¢¢&Wò(i""Â33c‚6†ævVBÖf–ÆRÆ—7BæBW†7BFö2ÖFVÇFF‚à ¢2222bã"Wf–FVæ6RÖ—76–ær÷"Ö&–wV÷W0 £â¢¤Ö—76–ær÷"Ö&–wV÷W2Wf–FVæ6S¢¢¢"Â33Cž(	—2†—7F÷&–6Â4’&W7VÇBâ ¢¢¢¥v‡’—BÖGFW'3¢¢¢c(	—27V66W727FFVÖVçB6öæfÆ–7G2v—F‚öæRF—&V7FÇ’ö'6W'fVBf–ÆVB'Vââ ¢¢¢¤Wf–FVæ6RæVVFVC¢¢¢gVÆÂ'Vâ÷&W'Vâ†—7F÷'’æBÆöw2f÷"†VB“3v3†#C3SfCFcF#3&S“Fc&6FC##ƒC–#3#–â ¢¢¢¤W‡V7FVBÆö6F–öâÂ–b¶æ÷vã¢¢¢v—D‡V"7F–öç2f÷""Â33C’â ¢¢¢¥6V&6‚&ööb÷"Væ¶æ÷vã¢¢¢¢¥Væ¶æ÷vã²¢¢c"ã"fW'7W2'Vâ#“#c3C#s“3â £"â¢¤Ö—76–ær÷"Ö&–wV÷W2Wf–FVæ6S¢¢¢W†7Bõ2Ó2&÷f—6–öæ–ær5Â'—FW2æBgVÆÂw&çG2öFVfVÇB×&—f–ÆVvW2w&‚â ¢¢¢¥v‡’—BÖGFW'3¢¢¢G&6¶VB6GW&RWf–FVæ6RFöW2æ÷BW7F&Æ—6‚WfW'’&÷f—6–öæ–ær÷&—f–ÆVvRVFvRâ ¢¢¢¤Wf–FVæ6RæVVFVC¢¢¢–Ö×WF&ÆR5ÂG&ç67&—BæBgVÆÂ&—f–ÆVvR–çfVçF÷'’â ¢¢¢¤W‡V7FVBÆö6F–öâÂ–b¶æ÷vã¢¢¢6W&FRWF†÷&—¦F–öâÖ&÷VæB÷W&F÷"Wf–FVæ6S²W†7BF‚¢¥Væ¶æ÷vâ¢¢â ¢¢¢¥6V&6‚&ööb÷"Væ¶æ÷vã¢¢¢¢¥Væ¶æ÷vã²¢¢c"ã’W‡Æ–6—FÇ’&WF–ç2F†W6RÆ–Ö—FF–öç2â £2â¢¤Ö—76–ær÷"Ö&–wV÷W2Wf–FVæ6S¢¢¢FVF–6FVB„DRÔU”33‚&ö÷BÂ6Æ÷6R×6²ÂFö¶VâÖWf–FVæ6RÖG&—‚ÂæB66WFæ6RÖâ ¢¢¢¥v‡’—BÖGFW'3¢¢¢F†W6RÖ’&R&VÆWfçBöæÇ’FòÆFW"ÆVBõö6Æ÷6V÷WBÆæS²F†W’vW&Ræ÷B–×ÆVÖVçFF–öâ×ÆâFVÆ—fW&&ÆW2â ¢¢¢¤Wf–FVæ6RæVVFVC¢¢¢W†7Bv÷fW&æVBF‡2÷"&V7W'6—fRG&VR÷WGWBâ ¢¢¢¤W‡V7FVBÆö6F–öâÂ–b¶æ÷vã¢¢¢6æF–FFR&ö÷BVF—B÷ö†FRÖW–33‚ö²÷F†W"W†7B†öÖW2¢¥Væ¶æ÷vâ¢¢â ¢¢¢¥6V&6‚&ööb÷"Væ¶æ÷vã¢¢¢¢¥6V&6‚ÖWF†öC¢¢¢6V&6†VB&Wòf÷"VF—B÷ö†FRÖW–33†Â„DRÔU”33‚6Æ÷6R×6¶Â„DRÔU”33‚6Æ÷6U÷6¶Â„DRÔU”33‚Fö¶VåöWf–FVæ6UöÖG&—†ÂæB„DRÔU”33‚66WFæ6UöÖ†66S¢–ç6Vç6—F—fR“²66÷S¢7W'&VçBv—D‡V"Ö–æFW†VBG&6¶VBf–ÆW3²FööÃ¢v—D‡V"6öFR6V&6‚öÖçVÂ66ã²&W7VÇC¢"Â’Â"Â2ÂæB2†—G2Â&W7V7F—fVÇ’Âv—F†÷WBF—&V7FÇ’–FVçF–f–VBFVF–6FVB'F–f7C²æöæW†—7FVæ6R&VÖ–ç2¢¥Væ¶æ÷vâ¢¢â¢¥7WÆVÖVçFÂWf–FVæ6Rö–çFW#¢¢¢v–âcõbÔ6æöâõ&Wó¢v†WF†W"F†W6RvW&R–×ÆVÖVçFF–öâFVÆ—fW&&ÆW2â'F–f7B(i"#b–×ÆVÖVçFF–öâÆâ„DRÔU”33‚æÖF(i"ÆFW"'F–f7G2÷WG6–FR–×ÆVÖVçFF–öâW†V7WF–öæâ £Bâ¢¤Ö—76–ær÷"Ö&–wV÷W2Wf–FVæ6S¢¢¢×WF&ÆRv÷&¶–ær×G&VR7FFRGW&–ær–ç7V7F–öââ ¢¢¢¥v‡’—BÖGFW'3¢¢¢6öÖÖ—GFVBv—D‡V"7FFR6ææ÷B&WfVÂVæ6öÖÖ—GFVBF—fW&vVæ6Râ ¢¢¢¤Wf–FVæ6RæVVFVC¢¢¢&Vf÷&RögFW"7FGW2g&öÒF†RW†7B6†V6¶÷WBâ ¢¢¢¤W‡V7FVBÆö6F–öâÂ–b¶æ÷vã¢¢¢Æö6Â6†V6¶÷WBâ ¢¢¢¥6V&6‚&ööb÷"Væ¶æ÷vã¢¢¢¢¥Væ¶æ÷vã²¢¢6öææV7F÷"Ö&6¶VB–ç7V7F–öâ†Bæò×WF&ÆR6†V6¶÷WBà ¢2222bã2÷Vâ6Æ÷7W&R—FV×2òVW7F–öç2f÷"F†RÆV@ £â¢¥VW7F–öâ÷"Vç&W6öÇfVB—FVÓ¢¢¢v†–6‚'Vâ÷"&W'Vâ6†÷VÆBv÷fW&âF†R†—7F÷&–6Â"Â33C’4’&V6÷&Cò ¢¢¢¤7W'&VçBWf–FVæ6S¢¢¢c"ã"&V6÷&G27V66W76gVÂf—6–&ÆR6†V6·3²7F–öç2'Vâ#“#c3C#s“3&V6÷&G2f–ÆVBFW7FæB6æ—G’×—VÆ–æV¦ö'2â ¢¢¢¤Ö—76–ærWf–FVæ6R÷"FV6—6–öâ&6—3¢¢¢gVÆÂ"Ö†VB7F–öç2†—7F÷'’æBÆöw2â ¢¢¢¥&VÆWfçBbFö7VÖVçBF—FÆRÂv†Vâ6æöâ×&VÆFVC¢¢¢c(	B„DR'V–ÆBæ÷FW2â £"â¢¥VW7F–öâ÷"Vç&W6öÇfVB—FVÓ¢¢¢†÷r6†÷VÆBF†RÆVBvV–v‚7W'&VçBcW†7B×F÷–27WW'6W76–öâv†–ÆRW&ÖæVçBc’ãb7F–ÆÂ6'&–W2'&–FvRÖW&Fö¶Vâ÷F‚v÷&F–æræB6÷W&6R7FGW6W3ò ¢¢¢¤7W'&VçBWf–FVæ6S¢¢¢c"ã.(	3"ãb7WÆ–W2F—&V7BÖöæÇ’ö7W'&VçBWf–FVæ6R6VÖçF–73²c’ãb6öçF–ç2F†RW†7BG&–gBÆ—7FVB–âRã2â ¢¢¢¤Ö—76–ærWf–FVæ6R÷"FV6—6–öâ&6—3¢¢¢F†R6W&FRWF†÷&—G’ÖÆæRFV6—6–öâf÷"W&ÖæVçBG&–ævRæBc’7FGW2G&VFÖVçBâ ¢¢¢¥&VÆWfçBbFö7VÖVçBF—FÆRÂv†Vâ6æöâ×&VÆFVC¢¢¢c(	B„DR'V–ÆBæ÷FW3²c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öââ ¢¢¢¤W†7BÆö6F÷"ÂöæÇ’v†Vâ6÷–VBfW&&F–Ó¢¢¢F†RV–v‡Bc’ãb7V'F6²†VF–æw2Æ—7FVB–âRãâ £2â¢¥VW7F–öâ÷"Vç&W6öÇfVB—FVÓ¢¢¢&RF†RÆFW"ö6Æ÷6R×6²ö66WFæ6R'F–f7G2&WV—&VBf÷"F†RÆVN(	—26W&FRFWFW&Ö–æF–öâÂv—fVâF†BF†R–×ÆVÖVçFF–öâÆâÆ6VBF†VÒ÷WG6–FR–×ÆVÖVçFF–öâW†V7WF–öãò ¢¢¢¤7W'&VçBWf–FVæ6S¢¢¢&÷VæFVB6V&6†W2–FVçF–f–VBöæÇ’Æææ–æröFö7VÖVçFF–öâövVæW&ÂÖ–æFW‚&VfW&Væ6W2Âv†–ÆR–×ÆVÖVçFF–öâæBõ2Wf–FVæ6RÆ—7FVB–âbãW†—7G2â¢¥7WÆVÖVçFÂWf–FVæ6Rö–çFW#¢¢¢v–âcõbÔ6æöâõ&Wó¢v†WF†W"F†÷6RÆFW"7W&f6W2vW&R–×ÆVÖVçFF–öâFVÆ—fW&&ÆW2â'F–f7B(i"#b–×ÆVÖVçFF–öâÆâ„DRÔU”33‚æÖF(i"ÆFW"'F–f7G2÷WG6–FR–×ÆVÖVçFF–öâW†V7WF–öæâ ¢¢¢¤Ö—76–ærWf–FVæ6R÷"FV6—6–öâ&6—3¢¢¢W†7Bv÷fW&æVBÆFW"Ö'F–f7B&WV—&VÖVçG2æBF‡2â ¢¢¢¥&VÆWfçBbFö7VÖVçBF—FÆRÂv†Vâ6æöâ×&VÆFVC¢¢¢¢¥Væ¶æ÷vâ¢¢g&öÒF†R6öç7VÇFVB6V7F–öç2â £Bâ¢¥VW7F–öâ÷"Vç&W6öÇfVB—FVÓ¢¢¢FòF†Rõ2Ó2&÷f—6–öæ–ærÖWf–FVæ6RÆ–Ö—G2ffV7B†÷rF†R÷W&F–öæÂ6¶WB6†÷VÆB&RvV–v†VCò ¢¢¢¤7W'&VçBWf–FVæ6S¢¢¢c&V6÷&G2öæRF—&V7B&VBÖöæÇ’6GW&Rv—F‚¦W&òw&—FW2÷&WG&–W2öÇFW&æFR×&÷f–FW"GFV×G2æB6W&FVÇ’&V6÷&G2Ö—76–ærW†7B&÷f—6–öæ–ær5ÂögVÆÂ&—f–ÆVvRw&‚â ¢¢¢¤Ö—76–ærWf–FVæ6R÷"FV6—6–öâ&6—3¢¢¢–Ö×WF&ÆR&÷f—6–öæ–ær5ÂæBgVÆÂ&—f–ÆVvRöFVfVÇB×&—f–ÆVvR–çfVçF÷'’Â÷"âW‡Æ–6—BÆVBFV6—6–öâöâF†R&÷VæFVB6¶WN(	—2Wf–FVçF–'’66÷Râ ¢¢¢¥&VÆWfçBbFö7VÖVçBF—FÆRÂv†Vâ6æöâ×&VÆFVC¢¢¢c(	B„DR'V–ÆBæ÷FW2â ¢¢¢¤W†7BÆö6F÷"ÂöæÇ’v†Vâ6÷–VBfW&&F–Ó¢¢¢*v"ã’’"Ób&VÖVF–F–öâÒ„DRÔU”33‚õ2Ó2(	BWF†÷&—¦VB&VFW"Õ&öÆR&÷f—6–öæ–ærÂF—&V7B&VBÔöæÇ’6GW&RÂæBWf–FVæ6RÔFÖ—76–öâ&÷VæF'–à ¢22"ã#2’÷7B–×ÆVÖVçFF–öâVF—BG&–vR„DRÔU”33€ ¤VF—B7VÖÖ' ¢¢F†RVF—B6ö×&W2„DRÔU”33Ž(	—2ÆææVB&6†—FV7GW&RÂ'VçF–ÖRÂWf–FVæ6RÂFWFW&Ö–æ—6ÒÂfVæF÷"ÂD"ÂæBVÖ—GFW"÷7GW&Rv—F‚&W÷6—F÷'’&VÆ—G’B6öÖÖ—BS“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†â ¢¢F&vWFVB&VBÖöæÇ’v—D‡V"–ç7V7F–öâ6öæf—&ÖVBF†BÖ–æ&VÖ–ç2BF†R6ÖR6öÖÖ—B–ç7V7FVB'’F†RVF—B&W÷'Bâ ¢¢F†R&–æ6—ÂF†VÖW2&R7Æ—B&W6VçFW"æÖW76W2Â×VÇF—ÆRf7F÷&–W2ÂF—7F–æ7B&VFW"æB6ö×B7W&f6W2Â×VÇF’×&ö÷BWf–FVæ6R7F÷&vRÂFWFW&Ö–æ—7F–2Ö6÷&RöVffV7FgVÂ×6VÒ6W&F–öâÂæBF‚Ö66R6Æ76–f–6F–öââ ¢¢F÷FÂf–æF–æw3¢Ââ ¢¢×W7BÖ7BÖæ÷rf–æF–æw3¢Ââ ¢¢&÷÷6Â†öÖW3¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâæBcB(	B„DRÖV6†æ–72wV–FRâ ¢¢æòf–æF–ærv2ÖFW&–ÆÇ’6öçG&F–7FVBâc"æBc"Ç&VG’&W6öÇfR÷"æ'&÷rFVâf–æF–æw2v—F†÷WBgW'F†W"Fö7VÖVçFF–öâ6†ævW2â ¢¢F†R&VÖ–æ–ær7W'&VçB—77VR—24BÓ#¢F†R&öGV7F–öâ&ö6f–ÆVæBÆö6ÂÆVæ6†W"6VÆV7BFFW"æf7F÷'“¦7&VFUö‚–Âv†–6‚öÖ—G2F†R6ö×B&ÇVW&–çBÖ÷VçFVB'’F†R÷F†W"ö'6W'fVBf7F÷&–W2à ¥&Wò–ç7V7F–öâ7VÖÖ' ¢¢ö'6W'fVB&Wò&ö÷C¢×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c&â ¢¢ö'6W'fVB„TB&Vf÷&RæBgFW"æÇ—6—3¢S“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S†â ¢¢'&æ6‚÷"FWF6†VB7FFS¢Ö–æÂF†R&W÷6—F÷'ž(	—2FVfVÇB'&æ6ƒ²FWF6†VB7FFR—2æ÷BÆ–6&ÆRFòF†R&VÖ÷FRv—D‡V"f–Wrâ ¢¢v÷&¶–ær×G&VR7FGW2&Vf÷&RæÇ—6—3¢âô(	BF†Rv—D‡V"6öææV7F÷"W‡÷6W26öÖÖ—GFVB&W÷6—F÷'’7FFRÂæ÷B×WF&ÆR6†V6¶÷WBâF†RVF—B&W÷'B6W&FVÇ’&V6÷&G2—G26†V6¶÷WB2'&æ6‚v÷&¶Â6ÆVâÂBF†R6ÖR–Ö×WF&ÆR6öÖÖ—Bâ ¢¢&÷VæFVB–ç7V7F–öâ66÷S¢&W÷6—F÷'’ÖWFFF²7W'&VçB6öÖÖ—C²f7F÷&–W2æBÆVæ6‚6öæf–wW&F–öã²&VFW"æB6ö×B†æFÆW'3²&W6VçFW"VÖ—GFW'3²6×ÆW"æB6ö×B6ö×WFF–öã²&öG”w&‚fVæF÷"Â–ævW7BÂÖVBÖ66†RÂæBD"ÖöGVÆW3²Wf–FVæ6R–æF–6W2æB6ö×æ–öç3²VæGö–çB6FÆöw3²Wf–FVæ6RWFFW#²4’v÷&¶fÆ÷s²6¶v–ærÖWFFF²æBF6²×&VÆWfçBbf–ÆW2â ¢¢–ç7V7F–öâÖWF†öG3¢v—D‡V"&W÷6—F÷'’ÖWFFFÆöö·WÂÆFW7BÖ6öÖÖ—BÆöö·WÂ&W÷6—F÷'’6öFR6V&6‚ÂæBW†7B×F‚f–ÆR&WG&–WfÂg&öÒÖ–æâfW&–f–VBÆö6Â'F–f7B'—FW2vW&R66WFVBöæÇ’v†W&Rv—B†6‚Öö&¦V7FÖF6†VBF†R7W'&VçBv—D‡V"&Æö"4„â ¢¢&Wó¢6V&6…ö6öÖÖ—G2‡&W÷6—F÷'“Ò&×F†÷&ãs‚övÆ÷rÖ†FVæv–æR×c""–(i"&S“C#&cfC66#cƒ–S†S““6Sƒ–“fFCCƒ“–S‚&â ¢¢&Wó¢&Fö72öWf–FVæ6Rô”äDU‚æ§6öâ&æB&'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÂ&(i"&÷F‚'6VB2SC‚&V6÷&G2â ¢¢&Wó¢&Væv–æR÷&W6VçFW"öVÖ—GFW"ç’&(i"$6æöæ–6ÂVÖ—GFW"f÷"v÷fW&æVBV&Æ–2¥4ôâ'—FW2â&²'&W6VçFW"÷&VFW%÷cöVÖ—GFW"ç’&(i"'V&Æ–5ö'—FW2ÒVÖ—GFW"æVÖ—E÷V&Æ–2†f–æÂ’&â ¢¢&Wó¢%&ö6f–ÆR&(i"&FFW"æf7F÷'“¦7&VFUö‚’&²&FFW"öf7F÷'’ç’&(i"&Vv—7FW'2öæÇ’'²&FFW"÷w6v’ç’&æB&FFW"ö‡GG÷&VFW"ç’&(i"&Vv—7FW"&÷F‚&VFW"æB6ö×B&ÇVW&–çG2â ¢¢ÖFW&–Âf–æF–æw2æ'&÷vVB'’&Wó¢DÓæBUÓ&W&W6VçBÆ–W&VBFVÆVvF–öâFòöæR'—FRWF†÷&—G’Âæ÷BGvò–æFWVæFVçB6W&–Æ—¦W'2âTBÓæB%ÓW7F&Æ—6‚F—7G&–'WF–öâ'WBFòæ÷BW7F&Æ—6‚'&ö¶Vâ–æFW‚ÂÖ—'&÷"Â÷"F‚×&ööb6ö†W&Væ6Râ ¢¢v÷&¶–ær×G&VR7FGW2gFW"æÇ—6—3¢âô(	Bæò&W÷6—F÷'’×WFF–öâö67W'&VBà ¤f–æF–æw2(i"Fö2FVÇFÖ  ¤däBÓ(	BDÓ ¤f–æF–æs¢&W6VçFW"æB…EE&W7öç6–&–Æ—F–W2ö67W’Ö÷&RF†âöæR6¶vR&ö÷BÂv†–ÆRF†Rö'6W'fVB'—FRF‚7F–ÆÂ6öçfW&vW2öâöæRVÖ—GFW"à ¤VF—Bæ6†÷#¢(	Å&W6VçFW"gVæ7F–öæÆ—G’Ç6òW†—7G2VæFW"Væv–æR÷&W6VçFW"òÂæB…EE6ö×F–&–Æ—G’†æFÆW'2Æ—fRVæFW"Væv–æRö‡GGòî(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	ÄDÓ(	BF—&V7F÷'’ö&6†—FV7GW&RG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢F†RW–2ÆâW‡&W76Ç’–æ6ÇVFVBVæv–æRÂFFW"Â&W6VçFW"Âæò×6V6öæBÔ…EEÖ†öÖRÂæB&6†—FV7GW&R×6æ6†÷B÷7GW&Rà ¤W–2Æâæ6†÷#¢W–2Æã¢b6æöâÆ–6&–Æ—G’6æ6†÷B(i"(	Åc"(	B„DR&6†—FV7GW&R(	BÆ–VC¢Væv–æRÂFFW"Â&W6VçFW"Â&öG”w&‚66†RÂVæGö–çB6FÆörÂæò6V6öæB…EE†öÖRÂæBÖVBÖ66†R&÷VæF'’÷7GW&Rî(	Ð ¥&Wò7&÷72Ö6†V6³¢7W'&VçBf–ÆW26öæf—&ÒF†RæÖW76R7Æ—BæB6–ævÆRFVÆVvFVB'—FRÖVÖ—76–öâF‚à ¥&Wò÷7GW&S¢6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Væv–æR÷&W6VçFW"öVÖ—GFW"ç’&(i"'&WGW&â6æöâç6W&6æöâ†VçfVÆ÷RÂ6÷'Eö¶W—3×6÷'Eö¶W—2’&²'&W6VçFW"÷&VFW%÷cöVÖ—GFW"ç’&(i"'V&Æ–5ö'—FW2ÒVÖ—GFW"æVÖ—E÷V&Æ–2†f–æÂ’&²&Væv–æRö‡GGö6ö×Eö†æFÆW"ç’&(i"&g&öÒVæv–æRç&W6VçFW"–×÷'BVÖ—E÷V&Æ–2&à ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	B7W'&VçBc"Ç&VG’6Æ76–f–W2F†RæÖW76R7Æ—Bà ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DR&6†—FV7GW&RÂ*s"ã(	Ä6ö×öæVçG2b&W7öç6–&–Æ—F–W2‡6–ævÆR†öÖW2ž(	Ò(i"(	Åw&W"VçfVÆ÷R'V–ÆFW'2Ô’Æ—fRVæFW"F÷ÖÆWfVÂ&W6VçFW"öÂv†–ÆRF†R'—FRÖWF†÷&—FF—fRVÖ—GFW"VçG'—ö–çBÔ’Æ—fRVæFW"Væv–æR÷&W6VçFW"öî(	ÒÂ(	ÄæÖW76R7Æ—B&V6öÖW2&6†—FV7GW&RG&–gBöæÇ’–b—B–çG&öGV6W26V6öæB–æFWVæFVçB&W6VçFW"6ö×öæVçBÂ6V6öæB6W&–Æ—¦W"†öÖRÂ÷"âÇFW&æFRV&Æ–2Ö'—FRF‚î(	Ò&Wò–ç7V7F–öâf÷VæBFVÆVvF–öâÂæ÷BâÇFW&æFR6W&–Æ—¦W"à ¤däBÓ"(	BDÓ  ¤f–æF–æs¢'VçF–ÖRD"æBfVæF÷"&öÆW2&R–×ÆVÖVçFVB&VæVF‚Væv–æRöF"öæBVæv–æRö&öG–w&‚öà ¤VF—Bæ6†÷#¢(	ÄD"æBfVæF÷"gVæ7F–öç2&RæW7FVBVæFW"Væv–æRöF"òæBVæv–æRö&öG–w&‚òî(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	ÄDÓ"(	BF—&V7F÷'’ö&6†—FV7GW&RG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢F†RW–2Æâ76–vç2fVæF÷"7V—6—F–öâÂW'6—7FVæ6RÂ&WG&–WfÂÂæB6ö×WFF–öâFòF†R„BVæv–æRà ¤W–2Æâæ6†÷#¢W–2Æã¢6öçG&7BæB6ö×F–&–Æ—G’÷7GW&R(i"fVæF÷"Ö6ÆÂ÷væW'6†—f÷"vÆ÷r–çFVw&F–öâ(i"(	ÅF†R„BVæv–æR&VÖ–ç2F†RFVfVÇB÷væW"öbfVæF÷"7V—6—F–öâÂW'6—7FVæ6RÖf6–ær&V†f–÷"Â&WG&–WfÂÖf6–ær&V†f–÷"ÂæB6ö×WFRÖf6–ær&V†f–÷"î(	Ð ¥&Wò7&÷72Ö6†V6³¢F—&V7B–ç7V7F–öâ6öæf—&ÖVBF†R'VçF–ÖRfVæF÷"6Æ–VçBÂ–ævW7BÂÖVBÖ66†RÂæBD"f:vFR&VæVF‚Væv–æRöâF†RVF—N(	—2W††W7F—fRæò×F÷ÖÆWfVÂ×6¶vR6ÆW6Rv2æ÷B–æFWVæFVçFÇ’&RÖVçVÖW&FVB&V6W6R—BFöW2æ÷BffV7BF—7÷6—F–öâà ¥&Wò÷7GW&S¢'F–ÆÇ’6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Væv–æRö&öG–w&‚÷fVæF÷%ö6Æ–VçBç’&(i"&6Æ72†D”6Æ–VçB&²&Væv–æRö&öG–w&‚ö–ævW7Bç’&(i"&g&öÒVæv–æRæF"–×÷'BD$66W72Â7FFVÖVçB&²&Væv–æRöF"öFFW"ç’&(i"&6Æ72D$66W72&à ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	Bc"Ç&VG’WF†÷&—¦W2F†—26VÒÆö6F–öâà ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DR&6†—FV7GW&RÂ*sbã"(	ÅfVæF÷"6VÒ†6öæ6WBöæÇ’ž(	Ò(i"(	ÅF†R&öG”w&‚–ævW7B÷&W6öÇWF–öâ6VÒÔ’&R–×ÆVÖVçFVBVæFW"Væv–æRö&öG–w&‚öî(	ÒÂ(	Ä&6†—FV7GW&RG&VG2Væv–æRö&öG–w&‚ö2æöâÖ6÷&R’ôò6VÒ6ö×öæVçBî(	ÒF†Rö'6W'fVBÆö6F–öâ—2F†W&Vf÷&RÇ&VG’6Æ76–f–VBà ¤däBÓ2(	B4BÓ ¤f–æF–æs¢÷&VFW&æBö’ö6ö×B÷c&RF—7F–æ7B7W&f6R6Æ76W2v—F‚6W&FR†æFÆW'2æBG&ç7÷'B6VÖçF–72à ¤VF—Bæ6†÷#¢(	Â÷&VFW"—2&VFW"ÖÆ–¶RæBf–ÆR×F‚G&—fVã²ö’ö6ö×B÷c—26W&FR–çFW&æÂöFÖ–â6ö×F–&–Æ—G’7W&f6Rî(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	Å4BÓ(	B7W&f6RG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢F†RW–2Æâ&W6W'fVBW†—7F–ærV&Æ–2&VFW"&V†f–÷"v†–ÆRÆÆ÷v–ær&÷VæFVB–çFW&æÂæBWf–FVæ6R7W&f6W2à ¤W–2Æâæ6†÷#¢W–2Æã¢6öçG&7BæB6ö×F–&–Æ—G’÷7GW&R(i"6öçG&7B6†ævW2æBæWr7W&f6W2(i"(	ÄæòæWrV&Æ–2W6W"Öf6–ær6öçG&7B—2ÆææVBî(	Ð ¥&Wò7&÷72Ö6†V6³¢F†RVæGö–çB6FÆöræB&÷WFRFV6÷&F÷'26öæf—&Ò÷&VFW&2&VFW"7V66W727W&f6RæBö’ö6ö×B÷c2–çFW&æÂöFÖ–âà ¥&Wò÷7GW&S¢6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Fö72ôTäEô”åE5ô4DÄôræ§6öâ&(i""ö’ö6ö×B÷c&†2&6Æ76–f–6F–öâ#¢&–çFW&æÅöFÖ–â&æB"÷&VFW"&—2F†RrÖVÆ–v–&ÆR&VFW"7V66W72&÷WFS²&FFW"ö‡GG÷&VFW"ç’&(i"'ævWB‚"÷&VFW""–²&Væv–æRö‡GGö6ö×Eö†æFÆW"ç’&(i"W&Å÷&Vf—ƒÒ"ö’ö6ö×B÷c&à ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	Bc"Ç&VG’F—7F–æwV—6†W2F†R7W&f6R6Æ76W2à ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DR&6†—FV7GW&RÂ*s2ã‚ã"(	ÅVçG'—ö–çG2†6öæ6WBÖöæÇ’ž(	Ò(i"(	Å&VFW"ÖÆ–¶R7V66W727W&f6W2Â6ö×B’7W&f6W2†f÷"W†×ÆRö’ö6ö×B÷c’ÂæBFWbö–çFW&æÂ†&æW727W&f6W2Ö’6öW†—7B–ç6–FRöæRFFW"ÖÖ÷VçFVB…EEfÖ–Ç’v—F†÷WB6öÆÆ6–ær–çFòöæR&ööb6Æ72î(	Òæòv÷&F–ærFVÇF—2æVVFVBà ¤däBÓB(	B4BÓ  ¤f–æF–æs¢×VÇF—ÆRf7F÷&–W2W‡÷6RF–ffW&VçB&÷WFR6WG2ÂæBF†Rf7F÷'’6VÆV7FVB'’&÷F‚F†R&öGV7F–öâ&ö6f–ÆVæBÆö6ÂÆVæ6†W"öÖ—G2F†R6ö×B&ÇVW&–çBà ¤VF—Bæ6†÷#¢(	ÅF†R&W÷6—F÷'’W‡÷6W2×VÇF—ÆRf7F÷&–W>(
bF†Ræ'&÷rf7F÷'’FöW2æ÷BÖ÷VçBF†R6ö×F–&–Æ—G’&ÇVW&–çBî(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	Å4BÓ"(	B7W&f6RG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢F†RW–2Æâ–æ6ÇVFVBrG&ç7÷'BvFW2æBâ&6†—FV7GW&R6æ6†÷B6÷fW&–ærV&Æ–2æB–çFW&æÂ7W&f6W2à ¤W–2Æâæ6†÷#¢W–2Æã¢FVÆ—fW&&ÆRC(	B&6†—FV7GW&R6æ6†÷BWf–FVæ6R(i"(	Å&öGV6R¶W—2ÖöæÇ’&6†—FV7GW&R6æ6†÷BF†B&VfÆV7G2F†RVæv–æ^(	—2V&Æ–2æB–çFW&æÂ7W&f6W2î(	Ð ¥&Wò7&÷72Ö6†V6³¢FFW"÷w6v’ç–æBFFW"ö‡GG÷&VFW"ç“¦7&VFUöÖ÷VçB&÷F‚&VFW"æB6ö×BâFFW"öf7F÷'’ç“¦7&VFUöÖ÷VçG2öæÇ’&VFW"Âv†–ÆR&ö6f–ÆVæB'VåöfÆ6²ç–6VÆV7BF†Bæ'&÷vW"f7F÷'’à ¥&Wò÷7GW&S¢6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&FFW"öf7F÷'’ç’&(i"&ç&Vv—7FW%ö&ÇVW&–çB†'ÂW&Å÷&Vf—ƒÕÂ%Â"’&v—F‚æò6ö×B&Vv—7G&F–öã²%&ö6f–ÆR&(i"&FFW"æf7F÷'“¦7&VFUö‚’&²''VåöfÆ6²ç’&(i"&g&öÒFFW"æf7F÷'’–×÷'B7&VFUö&²&FFW"÷w6v’ç’&(i"&ç&Vv—7FW%ö&ÇVW&–çB‡&VFW%ö'’&æB&ç&Vv—7FW%ö&ÇVW&–çB†6ö×Eö&ÇVW&–çB’&à ¤×W7BÖ7BÖæ÷s¢”U0 ¤F—7÷6—F–öã¢Fö2FVÇF&÷÷6V@ ¤6÷'&V7B†öÖR‡2“¢c’ãbf÷"F†R7W'&VçB'VçF–ÖR&VÖVF–F–öâ&V6÷&C²cB*s3"ãf÷"F†RÖ—76–ærf7F÷'’ÖÖ÷VçBÖV6†æ–726Æ&–f–6F–öâà ¥c’ç‚F6²FVÇF¢”U0 ¥c’ç‚F&vWC¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öà ¥cBÖV6†æ–72FVÇF¢”U0 ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"Ç&VG’7FFW2F†R&6†—FV7GW&R'VÆRÂ6ò—BæVVG2æòFVÇFâc"(	B„DR&6†—FV7GW&RÂ*sã(	Å6–ævÆR†öÖW>(	Ò(i"(	Ä×VÇF—ÆR7&VFUö–×ÆVÖVçFF–öç2Ô’W†—7Bf÷"FWb†&æW76W2÷"w&W'2Â'WB&öGV7F–öâ7F'GWÕU5BFVÆVvFRFòöæR6æöæ–6ÂFFW"f7F÷'’VçG'—ö–çBFòfö–BF—fW&vVçB&÷WFRÖ÷VçF–ærî(	Òc"(	B„DR&6†—FV7GW&RÂ*s2ã‚ã(	ÄFWbõ&VFW"f–Æ&–Æ—Gž(	Ò(i"(	ÇF†R†&æW72—2&W7öç6–&ÆRf÷"Ö÷VçF–ærF†R6ö×B…EE7W&f6R†ö’ö6ö×B÷c’î(	Òc’ãb—2&÷&–FRf÷"7W'&VçB'VçF–ÖRv÷&³²cB—2&÷&–FRf÷"F†R&V7W'&–ær6W'f–6RÖf7F÷'’ÖV6†æ–72và ¤däBÓR(	BTBÓ ¤f–æF–æs¢Wf–FVæ6R—2F—7G&–'WFVB7&÷72×VÇF—ÆR&W÷6—F÷'’&ö÷G2Âv†–ÆRF†Rv÷fW&æVB–æF–6W2&–æBÖç’'F–f7G2à ¤VF—Bæ6†÷#¢(	ÄWf–FVæ6R—2F—7G&–'WFVB7&÷72Fö72òÂ'F–f7G2òÂVF—BòÂæVF—EÅ÷7&2òÂ&öög2òÂvöÆFVç2òÂ&W÷'G2Â6FÆörög&VW¦Röæ'&F—fR&ö÷G2ÂæB&ö÷BÖÆWfVÂ6GW&W2î(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	ÄTBÓ(	BWf–FVæ6RG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢F†RW–2Æâ&WV—&VB‡VÖâWf–FVæ6R–æFW‚Â†6‚6VçF–æVÂÂÖ6†–æRÖ—'&÷"ÂæBF‚×&ööb6ö†W&Væ6Rf÷"v÷fW&æVB'F–f7G2à ¤W–2Æâæ6†÷#¢W–2Æã¢FVÆ—fW&&ÆRC(	BvÆö&ÂF—66—Æ–æR(i"(	ÇF†R‡VÖâWf–FVæ6R–æFW‚Â†6‚6VçF–æVÂÂÖ6†–æRÖ—'&÷"ÂæB&WV—&VBF‚&öög2&RWFFVB–âF†R6ÖR"v†Vâ'F–f7B'—FW26†ævRî(	Ð ¥&Wò7&÷72Ö6†V6³¢7W'&VçB–æFW‚ÂÖ—'&÷"ÂVF—B6FÆörÖ—'&÷"ÂVæGö–çB6FÆörÂæBFööÆ–ærF‡26öæf—&Ò×VÇF’×&ö÷BWf–FVæ6RæBv÷fW&æVB&–æF–ærâW†7BW"×&ö÷Bf–ÆR6÷VçG2vW&Ræ÷B–æFWVæFVçFÇ’&V6ö×WFVBà ¥&Wò÷7GW&S¢'F–ÆÇ’6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Fö72öWf–FVæ6Rô”äDU‚æ§6öâ&(i"7W'&VçB‡VÖâ–æFWƒ²&'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÂ&(i"7W'&VçBÖ6†–æRÖ—'&÷#²&'F–f7G2öVF—BôTäEô”åE5ô4DÄôræ§6öâ&(i"7W'&VçBv÷fW&æVBVF—BÖ—'&÷#²'FööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç’&(i"&–æG2F†R‡VÖâ–æFW‚æBÖ6†–æRÖ—'&÷"F‡2à ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	Bc"Ç&VG’FVf–æW2–çFVçF–öæÂ×VÇF’×&ö÷B7F÷&vRà ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DRÕ66†VÖ2ÖæBÔ'F–f7G2Â*s‚ãbã2ã(	Ä6FÆörv÷fW&ææ6RæB&ö÷BF—66—Æ–æ^(	Ò(i"(	ÅF†RWf–FVæ6R6FÆör—2–çFVçF–öæÆÇ’×VÇF’×&ö÷Bî(	ÒÂ(	Ä×VÇF’×&ö÷B7F÷&vR—2æ÷BÂ'’—G6VÆbÂWf–FVæ6RG&–gBî(	ÒF†RVF—BF–Bæ÷BW7F&Æ—6‚âVæv÷fW&æVBæWr&ö÷B÷"6V6öæBG'WF‚†öÖRà ¤däBÓb(	BTBÓ  ¤f–æF–æs¢F†R‡VÖâWf–FVæ6R–æFW‚æBÖ6†–æRÖ—'&÷"V6‚6öçF–âSC‚&V6÷&G2æB&RÖ–çF–æVB'’W‡Æ–6—BFööÆ–æræB4’à ¤VF—Bæ6†÷#¢(	ÆFö72öWf–FVæ6Rô”äDU‚æ§6öâæB'F–f7G2öWf–FVæ6UÅö–æFW‚æ§6öæÂ&÷F‚6öçF–âSC‚&V6÷&G2î(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	ÄTBÓ"(	BWf–FVæ6RG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢–æFW‚æBÖ—'&÷"&—G’v27&÷72Ö7WGF–ær„DRÔU”33‚ö&Æ–vF–öâà ¤W–2Æâæ6†÷#¢W–2Æã¢FVÆ—fW&&ÆRC(	BvÆö&ÂF—66—Æ–æR(i"(	ÄVæf÷&6^(
b‡VÖâWf–FVæ6R–æFW‚WFFW2Â†6‚6VçF–æVÂWFFW2ÂÖ6†–æRÖ—'&÷"WFFW2ÂæBF‚×&ööb6ö†W&Væ6Rî(	Ð ¥&Wò7&÷72Ö6†V6³¢&÷F‚7W'&VçBf–ÆW2vW&R&WG&–WfVBæB'6VC²V6‚6öçF–ç2SC‚&V6÷&G2â4’–çfö¶W2F†RWFFW"Â÷&–VçFF–öâ6†V6²Â†6‚6†V6²ÂæBÖ—'&÷"×66†VÖ6†V6²à ¥&Wò÷7GW&S¢6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Fö72öWf–FVæ6Rô”äDU‚æ§6öâ&(i"SC‚'6VB'&’&V6÷&G3²&'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÂ&(i"SC‚'6VB¥4ôäÂ&V6÷&G3²"æv—F‡V"÷v÷&¶fÆ÷w2ö6’ç–ÖÂ&(i"'—F†öâFööÇ2öWf–FVæ6R÷WFFUöWf–FVæ6Uö–æFW‚ç’ÒÖ6†V6²&Â'—F†öâFööÇ2öWf–FVæ6Rö÷&–VçFF–öåöFVÖòç’ÒÖ6†V6²&Â&6†V6µöWf–FVæ6Uö–æFW…ö†6‚ç6‚&ÂæB&6†V6µöÖ—'&÷%÷66†VÖç6‚&à ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	Bc"Ç&VG’v÷fW&ç2F†—2W†7B—"à ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DRÕ66†VÖ2ÖæBÔ'F–f7G2Â*t÷væW'6†—(i"*t‡VÖâWf–FVæ6R–æFW‚(i"(	Ä×W7BÖ–çF–â£&—G’v—F‚F†RÖ6†–æRWf–FVæ6RÖ—'&÷"î(	Òc.(	—2W†—7F–ær'VÆRÖF6†W2F†Rö'6W'fVB&Wò÷7GW&Rà ¤däBÓr(	BDBÓ ¤f–æF–æs¢6ö×F–&–Æ—G’æB6×ÆW"6ö×WFF–öâ&RFWFW&Ö–æ—7F–2Âv†–ÆRfVæF÷"–ævW7F–öâ—2W‡Æ–6—FÇ’VffV7FgVÂà ¤VF—Bæ6†÷#¢(	Ä6ö×F–&–Æ—G’æB6×ÆW"6ö×WFRF‡2W6R7F&ÆR†6†–ærÂæ÷&ÖÆ—¦F–öâÂW‡Æ–6—B6÷'F–ærÂæBæòö'6W'fVB6Æö6·2÷&æFöÖæW73²fVæF÷"ö–ævW7BF‡2W6R6Æö6·2ÂæWGv÷&²ÂD"ÂæBVæBÖöæÇ’Æöw2î(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	ÄDBÓ(	BFWFW&Ö–æ—6ÒG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢FWFW&Ö–æ—6ÒvFW2æBVffV7FgVÂ&öG”w&‚÷fVæF÷"v÷&²vW&R6W&FRFVÆ—fW&&ÆW2à ¤W–2Æâæ6†÷#¢W–2Æã¢FVÆ—fW&&ÆRCR(	BFWFW&Ö–æ—6ÒvFW2(i"(	Ä–×ÆVÖVçBæB&–æBFWFW&Ö–æ—7F–2vFW2f÷"&V–ÖvR&V6ö×WFRÂ&VFW"Fò4Ä’&—G’Â"Fò$6ö†W&Væ6RÂGvò×'Vâ–FVçF—G’ÂæB6æöæ–6Â¥4ôâ6ö×&—6öâî(	Ð ¥&Wò7&÷72Ö6†V6³¢F†R6×ÆW"W‡Æ–6—FÇ’F—66Æ–×2&æFöÖæW72Â6Æö6·2ÂæBW‡FW&æÂ7FFRâfVæF÷"–ævW7F–öâW6W2æWGv÷&²ÂÖöæ÷Föæ–2F–ÖRÂD"66W72ÂæBVæBÖöæÇ’Æöw2à ¥&Wò÷7GW&S¢6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Væv–æR÷6×ÆW"ö6÷&Rç’&(i"$æò&æFöÖæW72Â6Æö6·2Â÷"W‡FW&æÂ7FFR&R6öç7VÇFVBâ&²&Væv–æRö&öG–w&‚ö–ævW7Bç’&(i"'7F'BÒF–ÖRæÖöæ÷Föæ–2‚’&Â'fVæF÷%÷&W7VÇBÒ6Æ–VçBæfWF6‚‡&WVW7B’&ÂæB$D$66W72æf÷%ö7W'&VçEöVçb&à ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	Bc"Ç&VG’FVf–æW2F†RFWFW&Ö–æ—7F–2Ö6÷&Rô’ôò×6VÒ6W&F–öâà ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DR&6†—FV7GW&RÂ*sã(	Å6–ævÆR†öÖW>(	Ò(i"(	Ä&öG”w&‚&W6öÇWF–öâæB–ævW7BÔ’W&f÷&ÒfVæF÷"æBD"’ôòF‡&÷Vv‚F†RD"'7G&7F–öâ26æ7F–öæVB6VÒî(	ÒÂ(	ÅF†—26'fRÖ÷WBFöW2æ÷B&VÆ‚W&—G’&WV—&VÖVçG2f÷"FWFW&Ö–æ—7F–26ö×WFRÖöGVÆW2î(	ÒF†Rö'6W'fVB6W&F–öâ—2Æ–væVBà ¤däBÓ‚(	Be2Ó ¤f–æF–æs¢fVæF÷"’ôò—26öæ6VçG&FVB–âF†R&öG”w&‚fVæF÷"6Æ–VçBæBwV&FVB'’W‡Æ–6—B4dRöæWGv÷&²&–Ç2à ¤VF—Bæ6†÷#¢(	ÅfVæF÷"’ôò—26öæ6VçG&FVB–âVæv–æRö&öG–w&‚÷fVæF÷%Åö6Æ–VçBç“²–ævW7BæB&W6öÇfW"6ÆÂ—BVæFW"W‡Æ–6—B4dRöæWGv÷&²vFW2î(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	Åe2Ó(	BfVæF÷"6VÒG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢F†RW–2Æâ&W6W'fW2„BVæv–æRfVæF÷"÷væW'6†—æB6Æ÷6VB×&–Ç2&VgW6Âà ¤W–2Æâæ6†÷#¢W–2Æã¢6öçG&7BæB6ö×F–&–Æ—G’÷7GW&R(i"fVæF÷"Ö6ÆÂ÷væW'6†—f÷"vÆ÷r–çFVw&F–öâ(i"(	ÅF†—2W–2FöW2æ÷BWF†÷&—¦RF—&V7B×6–FR‡VÖäFW6–vä’6ÆÇ2î(	Ð ¥&Wò7&÷72Ö6†V6³¢F†RfVæF÷"6Æ–VçB÷vç2…EE&V†f–÷"ÂæB—G2FVfVÇB&WVW7BF‚&VgW6W2VæÆW724dUôÔôDSÓæBÄÄõuôäUEtõ$³Óà ¥&Wò÷7GW&S¢6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Væv–æRö&öG–w&‚÷fVæF÷%ö6Æ–VçBç’&(i"&6Æ72†D”6Æ–VçB&æB&–b6fUöÖöFRÒÂ#Â"÷"ÆÆ÷uöæWGv÷&²ÒÂ#Â#¢&—6RfVæF÷$W'&÷"…Â%$õd”DU%õ$TeU4TEÂ.(
b’&²&Væv–æRö&öG–w&‚ö–ævW7Bç’&(i"'fVæF÷%÷&W7VÇBÒ6Æ–VçBæfWF6‚‡&WVW7B’&à ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	Bc"Ç&VG’–FVçF–f–W2F†—2fVæF÷"6VÒæB&–Ç2&÷VæF'’à ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DR&6†—FV7GW&RÂ*sbã"(	ÅfVæF÷"6VÒ†6öæ6WBöæÇ’ž(	Ò(i"(	ÅF†RfVæF÷"6VÞ(
b—2F†RöæÇ’Æ6R–âF†RVæv–æRôFFW"7F6²v†W&RÆ—fR…EE6ÆÇ2FòF†RfVæF÷"Ö’ö67W"î(	ÒÂ(	Å&–Ç2×W7B&RW‡Æ–6—FÇ’÷Vâ&Vf÷&Rç’Æ—fR…EE—2GFV×FVBî(	Ò&Wò&VÆ—G’ÖF6†W2F†B'VÆRà ¤däBÓ’(	B2Ó ¤f–æF–æs¢6öFRF—&V7F÷&–W2&RÆ÷vW&66RÂv†–ÆRv÷fW&æVBf–ÆVæÖW2æB–FVçF–f–W'2Ö’&W6W'fRWW&66R6†&7FW'2à ¤VF—Bæ6†÷#¢(	Ä7F—fR6¶vR&ö÷G2æB–×÷'G26öç6—7FVçFÇ’W6RÆ÷vW&66RVæv–æRÂFFW"ÂæB&W6VçFW#²Wf–FVæ6RF‡2&W6W'fRÖ—†VBFö¶Vç27V6‚2TäEô”åE5Åô4DÄôræ§6öâî(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	Å2Ó(	BF‚Ö66RG&–gBî(	Ð ¤W–2ÆâÆ–æ¶vS¢æòW‡Æ–6—BF‚Ö66RF6²V'2–âF†RW–2Æâà ¤W–2Æâæ6†÷#¢âô(	B6V&6‚ÖWF†öC¢6V&6†VBW–2Æâf÷"(	ÇF…Å²ÒÅÖ66WÆF—&V7F÷'’66WÆÆ÷vW&66RF—&V7F÷'ÆÖ—†VEÅ²ÒÅÖ66^(	Ò†66S¢–ç6Vç6—F—fR“²66÷S¢6ö×ÆWFR6÷W&6S²FööÃ¢&s²&W7VÇC¢†—G2à ¥&Wò7&÷72Ö6†V6³¢7W'&VçB6öFR&ö÷G2&RÆ÷vW&66RÂæBF†Rv÷fW&æVBVæGö–çB6FÆörf–ÆVæÖR6öçF–ç2WW&66R6†&7FW'2à ¥&Wò÷7GW&S¢6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Væv–æR÷&W6VçFW"öVÖ—GFW"ç’&Â&FFW"ö‡GG÷&VFW"ç’&ÂæB'&W6VçFW"÷&VFW%÷cöVÖ—GFW"ç’&(i"Æ÷vW&66RF—&V7F÷'’6VvÖVçG3²&Fö72ôTäEô”åE5ô4DÄôræ§6öâ&(i"WW&66Rf–ÆVæÖRVæFW"Æ÷vW&66RFö72öà ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	Bc"Ç&VG’F—7F–æwV—6†W2F—&V7F÷'’66Rg&öÒf–ÆVæÖR66Rà ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DRÕ66†VÖ2ÖæBÔ'F–f7G2Â*tF—&V7F÷'’æÖ–ær†Æ÷vW"Ö66R44”’’(i"(	ÅF†—2&–ÂÆ–W2FòF—&V7F÷'’æÖW2öæÇ’âf–ÆVæÖW2Ô’6öçF–âWW&66R6†&7FW'2VæÆW726W&FVÇ’f÷&&–FFVâ'’6æöâî(	ÒF†Rö'6W'fVBWW&66Rf–ÆVæÖW2&Ræ÷BF—&V7F÷'’Ö66RG&–gBà ¤däBÓ(	B%Ó ¤f–æF–æs¢F†RVF—B–FVçF–f–VB"G'WF‚Ö&V&–ær÷"v÷fW&æVBÖ÷WGWB&ö÷G2Â'WBF–Bæ÷BW7F&Æ—6‚â÷W&F–öæÂ÷"WF†÷&—G’FVfV7Bg&öÒF†R6÷VçBÆöæRà ¤VF—Bæ6†÷#¢(	Ã"G'WF‚Ö&V&–æröv÷fW&æVBÖ÷WGWB&ö÷G2vW&Rö'6W'fVBî(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	Å%Ó(	B&ö÷B&öÆ–fW&F–öâî(	ÒÂ(	Ä–×7C¢æ÷BW7F&Æ—6†VBg&öÒ&WòWf–FVæ6Rî(	Ð ¤W–2ÆâÆ–æ¶vS¢F†RW–2ÆâFWVæG2öâÆVFvW"Ö&6VBWf–FVæ6R&–æF–ær&F†W"F†â6–ævÆR‡—6–6ÂWf–FVæ6RF—&V7F÷'’à ¤W–2Æâæ6†÷#¢W–2Æã¢FVÆ—fW&&ÆRC(	BvÆö&ÂF—66—Æ–æR(i"(	Ä‡VÖâWf–FVæ6R–æFW‚WFFW2Â†6‚6VçF–æVÂWFFW2ÂÖ6†–æRÖ—'&÷"WFFW2ÂæBF‚×&ööb6ö†W&Væ6Rî(	Ð ¥&Wò7&÷72Ö6†V6³¢7W'&VçB&Wò–ç7V7F–öâ6öæf—&ÖVB&W&W6VçFF—fRv÷fW&æVB&ö÷G2æB7W'&VçBÆVFvW"7W&f6W2âF†RW†7B"×&ö÷B6Vç7W2v2æ÷B–æFWVæFVçFÇ’&RÖVçVÖW&FVB&V6W6RæòWF†÷&—G’÷"6ö†W&Væ6RFVfV7BFWVæG2öâF†R6÷VçBà ¥&Wò÷7GW&S¢'F–ÆÇ’6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢&Fö72öWf–FVæ6Rô”äDU‚æ§6öâ&Â&'F–f7G2öWf–FVæ6Uö–æFW‚æ§6öæÂ&Â&'F–f7G2öVF—BôTäEô”åE5ô4DÄôræ§6öâ&Â&6FÆöröÖæ–fW7Bæ§6öâ&F‡&÷Vv‚7W'&VçB–æFW†VB÷6V&6†&ÆR&W÷6—F÷'’7W&f6W3²7W'&VçB„TBWVÇ2F†RVF—N(	—2–Ö×WF&ÆR6öÖÖ—Bà ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	Bc"7FFW2F†B&ö÷B6÷VçBæB×VÇF’×&ö÷BF—7G&–'WF–öâÆöæRFòæ÷BG&–vvW"6æöâ6†ævRà ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c"(	B„DRÕ66†VÖ2ÖæBÔ'F–f7G2Â*s‚ãbã2ã(	Ä6FÆörv÷fW&ææ6RæB&ö÷BF—66—Æ–æ^(	Ò(i"(	Å&Wf—6—BWf–FVæ6R×&ö÷B6Æ76–f–6F–öâ÷"&ö÷B&öÆ–fW&F–öâöæÇ’v†VâgWGW&Rv÷&²&÷÷6W2V—F†W#¢æWrv÷fW&æVB&ö÷C²÷"6V6öæBG'WF‚†öÖRf÷"âW†—7F–ærv÷fW&æVBWf–FVæ6RfÖ–Ç’î(	ÒÂ(	Ä'6VçBöæRöbF†÷6R&÷÷6Ç>(
bÅ¶×VÇF’×&ö÷BF—7G&–'WF–öåÅÒ—2æ÷BÂ'’—G6VÆbÂ6æöâÖ6†ævRG&–vvW"î(	Ð ¤däBÓ(	BUÓ ¤f–æF–æs¢vVæW&–26æöæ–6ÂVÖ—76–öâÂ&VFW"ÖVçfVÆ÷R6öç7G'V7F–öâÂæB6ö×&—6öâFööÆ–ærö67W’F—7F–æ7BÖöGVÆW2v—F‚F—7F–æ7B&W7öç6–&–Æ—F–W2à ¤VF—Bæ6†÷#¢(	Å6†&VB6æöæ–6ÂVÖ—76–öâ—2–âVæv–æR÷&W6VçFW"öVÖ—GFW"ç“²&VFW"6†–ær—2–â&W6VçFW"÷&VFW%Å÷cöVÖ—GFW"ç“²6ö×&—6öâFööÆ–ær—2–â&W6VçFW"ö§6öåÅö6æöåÅö6ö×&Rç’î(	Ð ¤VF—BWf–FVæ6Rö–çFW#¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	ÄUÓ(	BVÖ—GFW"÷7GW&Rî(	Ð ¤W–2ÆâÆ–æ¶vS¢F†RW–2Æâ&WV—&VB6–ævÆR6æöæ–6ÂVÖ—GFW"&÷VæF'’æBVÖ—GFW"Ö†6‚Wf–FVæ6Rà ¤W–2Æâæ6†÷#¢W–2Æã¢b6æöâÆ–6&–Æ—G’6æ6†÷B(i"(	Åc"(	B„DR&6†—FV7GW&R(	BÆ–VC¢Væv–æRÂFFW"Â&W6VçFW.(
bæBæò6V6öæB…EE†öÖRî(	Ð ¥&Wò7&÷72Ö6†V6³¢&VFW"6†–ærFVÆVvFW2f–æÂ'—FW2FòVæv–æRç&W6VçFW"æVÖ—GFW&²6ö×&—6öâFööÆ–ær—26W&FRæBFöW2æ÷B&V6öÖRF†R'VçF–ÖRVÖ—GFW"à ¥&Wò÷7GW&S¢6öæf—&ÖV@ ¥&WòWf–FVæ6Rö–çFW#¢&Wó¢'&W6VçFW"÷&VFW%÷cöVÖ—GFW"ç’&(i"'&Uö'—FW2ÒVÖ—GFW"æVÖ—E÷V&Æ–2‡&V–ÖvR’&æB'V&Æ–5ö'—FW2ÒVÖ—GFW"æVÖ—E÷V&Æ–2†f–æÂ’&²&Væv–æR÷&W6VçFW"öVÖ—GFW"ç’&(i"$6æöæ–6ÂVÖ—GFW"f÷"v÷fW&æVBV&Æ–2¥4ôâ'—FW2â&  ¤×W7BÖ7BÖæ÷s¢äð ¤F—7÷6—F–öã¢æòFö2FVÇFæVVFV@ ¤6÷'&V7B†öÖR‡2“¢æöæR(	BcæBc"Ç&VG’6Æ76–g’F†R6–ævÆR'—FRWF†÷&—G’æBW&Ö—GFVBw&W"æÖW76Rà ¥c’ç‚F6²FVÇF¢äð ¥c’ç‚F&vWC¢âô(	Bæò'V–ÆBÖ6†V6¶Æ—7BFVÇF—2W7F&Æ—6†VBà ¥cBÖV6†æ–72FVÇF¢äð ¥c"&6†—FV7GW&RFVÇF¢äð ¤÷F†W"bFö2FVÇF‡2“¢æöæP ¥c#†—7F÷&–6Â6÷'&V7F–öã¢äð ¤W†—7F–ær—77VRGWÆ–6FS¢âô(	BW†—7F–ær—77VW2Æ—7Bæ÷B&÷f–FVBà ¥v‡’F†W6R&RF†R6÷'&V7B†öÖW3¢c(	B„DR'V–ÆBæ÷FW2ÂFFVæGVÒ"ãB(	Å"ÓB„DRÔU”33‚(	B&÷fVB&W66÷RæB6æöâFV6—6–öç2Î(	Ò*tE"Ô4äôâÓ(i"(	ÅF†RW†—7F–ær&W6VçFW"&VÖ–ç2F†R6öÆR'—FRWF†÷&—G’â&ö¦V7FVBfÇVW2&RVÖ—GFVBöæÇ’F‡&÷Vv‚Væv–æRç&W6VçFW"æVÖ—GFW"æVÖ—E÷V&Æ–6î(	Òc"(	B„DR&6†—FV7GW&RÂ*s"ã(	Ä6ö×öæVçG2b&W7öç6–&–Æ—F–W2‡6–ævÆR†öÖW2ž(	Ò(i"(	Åw&W"VçfVÆ÷R'V–ÆFW'2Ô’Æ—fRVæFW"F÷ÖÆWfVÂ&W6VçFW"öÂv†–ÆRF†R'—FRÖWF†÷&—FF—fRVÖ—GFW"VçG'—ö–çBÔ’Æ—fRVæFW"Væv–æR÷&W6VçFW"öî(	Òæò&VÖ–æ–ær6æöâÖ&–wV—G’—2W7F&Æ—6†VBà ¤Fö2FVÇF&÷÷6Ç2(	Bc’ç‚…F6·2 ¥c’ç‚F&vWBFö3¢c’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öà ¥F6²”C¢ÃÅc•ÅõD4µÅô”EÅõÄ4T„ôÄDU%Ãâ(	BäTTE2c’”B54”täÔTå@ ¥7V'F6²”C¢âô(	Bæò7W'&VçBc’ãb7V'F6²F—&V7FÇ’6÷fW'26æöæ–6Âf7F÷'’&÷WFRÖÖ÷VçB&—G’à ¥7FGW3¢ÃÅc•Åõ5DEU5ÅõÄ4T„ôÄDU%Ãâ(	BäTTE25DEU254”täÔTå@ ¥F6²F—FÆS¢6æöæ–6ÂFFW"f7F÷'’&÷WFRÖÖ÷VçB&—G ¥G—S¢&Wò&VÖVF–F–öà ¤×W7BÖ7BÖæ÷s¢”U0 ¥6÷W&6Rf–æF–æs¢däBÓ@ ¤Wf–FVæ6Rö–çFW"‡2“¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	Å4BÓ"(	B7W&f6RG&–gBî(	ÒW–2Æã¢FVÆ—fW&&ÆRC(i"(	Å&öGV6R¶W—2ÖöæÇ’&6†—FV7GW&R6æ6†÷BF†B&VfÆV7G2F†RVæv–æ^(	—2V&Æ–2æB–çFW&æÂ7W&f6W2î(	Òc"(	B„DR&6†—FV7GW&RÂ*sã(	Å6–ævÆR†öÖW>(	Ò(i"(	Ç&öGV7F–öâ7F'GWÕU5BFVÆVvFRFòöæR6æöæ–6ÂFFW"f7F÷'’VçG'—ö–çBFòfö–BF—fW&vVçB&÷WFRÖ÷VçF–ærî(	Ð ¥&WòWf–FVæ6Rö–çFW"‡2“¢&Wó¢%&ö6f–ÆR&(i"&FFW"æf7F÷'“¦7&VFUö‚’&²''VåöfÆ6²ç’&(i"&g&öÒFFW"æf7F÷'’–×÷'B7&VFUö&²&FFW"öf7F÷'’ç’&(i"Ö÷VçG2öæÇ’'²&FFW"÷w6v’ç’&æB&FFW"ö‡GG÷&VFW"ç’&(i"Ö÷VçB&÷F‚&VFW"æB6ö×B&ÇVW&–çG2à ¥v‡’c’ç‚—2F†R6÷'&V7B†öÖS¢F†RVç&W6öÇfVB6öæF—F–öâ—27W'&VçB'VçF–ÖR–×ÆVÖVçFF–öâv÷&²ffV7F–ærFWÆ÷–VBæBFWb&÷WFRf–Æ&–Æ—G’â—B&VÆöæw2–â†6VB'V–ÆB6†V6¶Æ—7BÂæ÷B–âc"&6†—FV7GW&Rv÷&F–ærà ¤æ÷FW3¢6V&6‚ÖWF†öC¢6V&6†VBc’ãbÔ6æöâÔ„DRÔ'V–ÆBÔ6†V6¶Æ—7BÔF—7F–ÆÆF–öâf÷"(	Æf7F÷'Æ7&VFUÅöÆ6æöæ–6ÂFFW"f7F÷'—Ç&÷WFRÖ÷VçF–æ~(	Ò†66S¢–ç6Vç6—F—fR“²66÷S¢6ö×ÆWFRFö7VÖVçC²FööÃ¢&s²&W7VÇC¢†—G2âæòW†—7F–ærF6²”B÷"7FGW2—26Æ–ÖVBà ¤Fö2FVÇF&÷÷6Ç2(	BcB„ÖV6†æ–72 ¤ÔT2Ó(	@ ¥F&vWBFö3¢cB(	B„DRÖV6†æ–72wV–FP ¥F&vWB6V7F–öã¢*s3"ã(	Å7F'B6öÖÖæBb6W'f–6Rf7F÷'’Åµ&WV—&VBÔæ÷uÅÞ(	Ð ¤FVÇF¢6Æ&–g’F†B6W'f–6RÖf7F÷'’6÷'&V7FæW72–æ6ÇVFW2&WV—&VB&÷WFRÖÖ÷VçB&—G’f÷"F†Rf7F÷'’7GVÆÇ’6VÆV7FVB'’&öGV7F–öâæBFö7VÖVçFVBFWbÆVæ6†W'2âF†RFWÆ÷–VB6æöæ–6Âf7F÷'’×W7Bæ÷BöÖ—BF†R&VFW"Â6ö×BÂ÷"&WV—&VB–çFW&æÂöFWb7W&f6W276–væVBFò—G2FWÆ÷–ÖVçB&öÆRâÖV6†æ–72Wf–FVæ6R6†÷VÆB&V6÷&BF†R6VÆV7FVBf7F÷'’æB—G2Ö÷VçFVB&÷WFR–çfVçF÷'’v–ç7BF†RVæGö–çB6FÆöræBc"FFW"&W7öç6–&–Æ—F–W2à ¥v‡“¢cB–FVçF–f–W2FFW"æf7F÷'“¦7&VFUö‚–2F†R&öGV7F–öâ6W'f–6Rf7F÷'’æB&WV—&W2(	Æf7F÷'’6÷'&V7FæW72Î(	Ò'WBFöW2æ÷B6öææV7B6÷'&V7FæW72Fò&WV—&VB&÷WFRÖ÷VçF–ærâ7W'&VçB&Wò&VÆ—G’6†÷w2F†BF†—26VÆV7FVBf7F÷'’öÖ—G2F†R6ö×B&ÇVW&–çBÖ÷VçFVB'’F†R÷F†W"f7F÷&–W2à ¤Wf–FVæ6Rö–çFW"‡2“¢VF—B&W÷'C¢G&–gBæB&VÆ—G’g2W‡V7FF–öç2(i"(	Å&÷WFRf–Æ&–Æ—G’FWVæG2öâv†–6‚f7F÷'’—26VÆV7FVBî(	ÒcB(	B„DRÖV6†æ–72wV–FRÂ*s3"ã(i"(	Å&÷fRF†R6W'f–6R–æ—F–Æ—¦W2f–F†Rf7F÷'’FFW"æf7F÷'“¦7&VFUÅö‚ž(
bî(	Òc"(	B„DR&6†—FV7GW&RÂ*s2ã‚ã(i"(	ÇF†R†&æW72—2&W7öç6–&ÆRf÷"Ö÷VçF–ærF†R6ö×B…EE7W&f6R†ö’ö6ö×B÷c’î(	Ð ¥&WòWf–FVæ6Rö–çFW"‡2“¢&Wó¢%&ö6f–ÆR&(i"6VÆV7G2FFW"æf7F÷'“¦7&VFUö‚–²&FFW"öf7F÷'’ç’&(i"&Vv—7FW'2öæÇ’F†R&VFW"&ÇVW&–çC²&FFW"÷w6v’ç’&æB&FFW"ö‡GG÷&VFW"ç’&(i"Ç6ò&Vv—7FW"6ö×Eö&ÇVW&–çFà ¥b&ööbW†6W'C¢âô(	B4äôâ4”ÄTä4Râ6V&6‚ÖWF†öC¢6V&6†VBcB(	B„DRÖV6†æ–72wV–FRf÷"(	ÆFFW"æf7F÷'’åÂ¦6ö×GÆ6ö×BåÂ¦FFW"æf7F÷'—Æf7F÷'’åÂ¦Ö÷VçBåÂ¦6ö×GÆ7&VFUÅöåÂ¦6ö×GÆf7F÷'’&—G—Ç&÷WFR×6WB&—Gž(	Ò†66S¢–ç6Vç6—F—fR“²66÷S¢6ö×ÆWFRFö7VÖVçC²FööÃ¢&s²&W7VÇC¢†—G2à ¥v‡’cB—2F†R6÷'&V7B†öÖS¢cB÷vç26¶v–ærÂ'VçF–ÖR&ö6W72ÖV6†æ–72Â6W'f–6RÖf7F÷'’6÷'&V7FæW72ÂæB6ö×öæVçB'V–ÆB&W7öç6–&–Æ—F–W2âF†—2FVÇF6Æ&–f–W2F†RW†—7F–ærc"&÷VæF'’v—F†÷WB6†æv–ær&6†—FV7GW&R÷væW'6†—ÂV&Æ–26öçG&7G2ÂFö¶Vç2ÂvFW2Â÷"66WFæ6R6VÖçF–72à ¤TäBôbTD•BäÅ•4•0 ¢22¢£"ã#B’7–çF‚Ô÷&–v–âFVfV7G2&VÖ–âæöâÔ&Æö6¶–ær&Vv&FÆW72öbÆ—FW&ÂW†V7WF–öâVffV7B¢  ¥F–ÖW7F×¢s#c#b3£# ¤FWF–Ç3¢F†—2FFVæGVÒ&V6÷&G2â–ÖÖVF–FR&öGV7B÷væW"&Wf–WrÖv÷fW&ææ6RFV6—6–öâ&ö×FVB'’&WVFVBGFV×G2GW&–ær„DRÔU”33‚Æ—fRÆâ&Wf–WrFò&V6Æ76–g’V÷F–ærÂW66–ærÂ6öÖÖæB×w&W"ÂæB&VÆFVB7–çF‚FVfV7G227V'7FçF—fRFVfV7G2&V6W6RF†RÆ—FW&ÂFW‡Bv÷VÆBf–ÂFòW†V7WFRâF†RW&ÖæVçBbFö7VÖVçG2&Wf–WvVBF‡W2f"Ç&VG’W7F&Æ—6‚F†R–çFVæFVBö&¦V7F—fRÖf—'7BÆææ–æræBW†V7WF–öâ×F–ÖRæ÷&ÖÆ—¦F–öâ÷7GW&RâF†—2FFVæGVÒFöW2æ÷B&WV—&RgW'F†W"6†ævW2FòF†÷6RFö7VÖVçG2â—BW7F&Æ—6†W2F†R6öçG&öÆÆ–ær–çFW'&WFF–öâæB6Æ÷6W2F†R&V6Æ76–f–6F–öâÆö÷†öÆRà ¢222¢¤6öçG&öÆÆ–ær'VÆR¢  ¥F†R6W6Â6÷W&6RöbFVfV7B6öçG&öÇ2—G26Æ76–f–6F–öââ—G2F÷vç7G&VÒVffV7BFöW2æ÷Bà ¤FVfV7B6W6VB'’7–çF‚ÂV÷F–ærÂW66–ærÂ6†VÆÂw&ÖÖ"ÂFö¶Væ—¦F–öâÂ6öÖÖæB×w&W"f÷&ÒÂ†W&VFö2f÷&ÒÂ†VÇW"Ö6öFRf÷&ÒÂf&–&ÆR–çFW'öÆF–öâÂ–æFVçFF–öâÂv†—FW76RÂÖ&¶F÷vâ&VæFW&–ærÂ6öFRÖ&Æö6²f÷&ÖGF–ærÂ&6·6Æ6‚–ç6W'F–öâÂ6÷’ÖæB×7FR6÷''WF–öâÂ–çFW'&WFW"–çfö6F–öâf÷&ÒÂ÷"Æ—FW&Â6öÖÖæB&W6VçFF–öâ&VÖ–ç27–çF‚Ö÷&–v–âFVfV7Bà ¤—B&VÖ–ç27–çF‚Ö÷&–v–âFVfV7BWfVâv†VâF†RÆ—FW&ÂFW‡C  ¢¢f–Ç2Fò'6S² ¢¢f–Ç2FòW†V7WFS² ¢¢W†V7WFW2FW‡BF–ffW&VçBg&öÒv†Bv2–çFVæFVC² ¢¢Æ÷6W2V÷FW2ÂFVÆ–Ö—FW'2Â÷"7G&–ærÆ—FW&Ç3² ¢¢6†ævW2&VçB6öÖÖæB–FVçF—G“² ¢¢–çfö¶W2â–æ6÷'&V7B&VçB6öÖÖæBf÷&Ó² ¢¢6ææ÷B&V6‚F†R–çFVæFVB&V†f–÷#² ¢¢6ææ÷B&R7FVBæB'Vâv—F†÷WB6÷'&V7F–öã²÷" ¢¢v÷VÆB&öGV6RF–ffW&VçB&W7VÇB&V6W6RöbF†RÖÆf÷&ÖVB&W&W6VçFF–öâà ¥F†W6RF÷vç7G&VÒVffV7G2Fòæ÷B6öçfW'B7–çF‚Ö÷&–v–âFVfV7B–çFò7V'7FçF—fRFVfV7Bà ¥&r×6÷W&6R6öæf—&ÖF–öâFöW2æ÷B6†ævRF†—26Æ76–f–6F–öââ6†÷v–ærF†BÖÆf÷&ÖVB7–çF‚W†—7G2–âF†R6÷W&6R&÷fW2v†W&RF†R7–çF‚—77VRV'2â—BFöW2æ÷BÖ¶RF†R—77VR7V'7FçF—fRà ¢222¢¥66÷R¢  ¥F†—2'VÆRÆ–W2v†Vâ&Wf–Wv–ær÷"&÷f–æs  ¢¢W–2Æç3² ¢¢–×ÆVÖVçFF–öâÆç3² ¢¢Æ—fRÆç3² ¢¢Æâ&Wf—6–öç2æB&W7V&Ö—76–öç3² ¢¢Æâ&VFÆ–æW3² ¢¢–×ÆVÖVçFF–öâ×&VF–æW72&Wf–Ww3² ¢¢6Æ÷6V÷WB&Wf–Ww3² ¢¢W–26Æ÷7W&R&Wf–Ww3²æB ¢¢ç’÷F†W"&Wf–Wrv†÷6RFV6—6–öâFWVæG2öâF†RFWV7’öbÆææ–ær'F–f7Bà ¢222¢¥&ö†–&—FVB&Wf–WrW6R¢  ¤7–çF‚Ö÷&–v–âFVfV7BÕU5BäõB&RW6VB3  ¢¢&Æö6¶W#² ¢¢6fVC² ¢¢&WV—&VBæ—C² ¢¢âW‡V7FVBf—ƒ² ¢¢æVVG2&Wf—6–öâFWFW&Ö–æF–öã² ¢¢6V7F–öâ6†V6¶Æ—7B&Wf—6–öâ&6—3² ¢¢&Wf–WrÆVFvW"f–æF–æs² ¢¢&VF–æW72÷"&÷fÂ6öæF—F–öã² ¢¢&V6öâFò&WV—&RÆâ&Wf—6–öâ÷"&W7V&Ö—76–öã² ¢¢&V6öâf÷"$Ud•4RäB$U5T$Ô•F² ¢¢&V6öâFòv—F††öÆB6Æ÷7W&S²÷" ¢¢ç’÷F†W"–çWBF†Bv÷'6Vç2÷"6öæF—F–öç2F†R&Wf–WrFV6—6–öâà ¥&Wf–WvW'2ÕU5BäõB&VÆ&VÂ7–çF‚Ö÷&–v–âFVfV7B27V'7FçF—fR—77VR'’FW67&–&–ær—B3  ¢¢6†ævVBW†V7WF&ÆRÖVæ–æs² ¢¢6†ævVB6öÖÖæB–FVçF—G“² ¢¢Æ÷72öb'Væ&–Æ—G’÷"'Vææ&–Æ—G“² ¢¢Æ—FW&ÂæöâÖW†V7WF&–Æ—G“² ¢¢ÖV6†æ–6Â–çfÆ–F—G“² ¢¢w&W"6÷''WF–öã² ¢¢f–ÇW&RFò&V6‚&V†f–÷#² ¢¢&ööbÖ6öÖÖæBf–ÇW&S²÷" ¢¢6÷W&6RÖ'—FR6öæf—&ÖF–öâà ¥F†÷6RFW67&—F–öç2–FVçF–g’6öç6WVVæ6W2öbF†R7–çF‚FVfV7BâF†W’Fòæ÷BW7F&Æ—6‚6W&FRFVfV7Bà ¤Æ—FW&Â7FRÖæB×'VâFW7B—2æ÷BÆâÖ&÷fÂFW7Bà ¢222¢¥&WV—&VB&Wf–WrÖWF†öB¢  ¥&Wf–WvW'2ÕU5BWfÇVFRF†R7–çF‚Öæ÷&ÖÆ—¦VB6VÖçF–2–çFVçBöbF†RÆâà ¤f÷"V6‚&VçB6öÖÖæBÖf÷&Ò—77VRÂF†R&Wf–WvW"×W7C  £â–FVçF–g’F†R–çFVæFVBö&¦V7F—fRÂ÷W&F–öâÂ–çWG2Â÷WGWG2Â&–Ç2÷7GW&RÂWf–FVæ6RF&vWBÂæB52÷"d”Â&VF–6FRg&öÒF†RÆââ £"â77VÖR7–çF7F–6ÆÇ’fÆ–B&W&W6VçFF–öâF†B&W6W'fW2F†÷6R6VÖçF–72â £2âFWFW&Ö–æRv†WF†W"F†RÆÆVvVBFVfV7B7F–ÆÂW†—7G2gFW"F†Bæ÷&ÖÆ—¦F–öââ £BâW†6ÇVFRF†R—77VRg&öÒF†R&Wf–WrFV6—6–öâ–bæ÷&ÖÆ—¦F–öâ&VÖ÷fW2—Bâ £Râ&W÷'B7V'7FçF—fRf–æF–æröæÇ’v†Vââ–æFWVæFVçFÇ’&÷fVâæöâ×7–çF‚FVfV7B&VÖ–ç2à ¥7–çF‚æ÷&ÖÆ—¦F–öâÕU5BäõB6†ævR66÷RÂö&¦V7F—fW2Â&WòÆö6’ÂFWVæFVæ6–W2Â6VÖçF–2–çWG2Â&WV—&VB÷WGWG2ÂWF†÷&—¦F–öâÂ&–Ç2÷7GW&RÂWf–FVæ6Rö&Æ–vF–öç2Â66WFæ6R6öæF—F–öç2Â÷"52æBd”Â&VF–6FW2à ¤–bF†R&Wf–WvW"6ææ÷B&÷fRF†Bâ—77VR7W'f—fW2f—F†gVÂ7–çF‚æ÷&ÖÆ—¦F–öâÂF†R—77VR—27–çF‚Ö÷&–v–âæBæöâÖ&Æö6¶–ærà ¢222¢¤–æFWVæFVçBæöâ×7–çF‚FVfV7B7FæF&B¢  ¤7V'7FçF—fRf–æF–ærÖ’ffV7BFV6—6–öâöæÇ’v†Vâ—C  ¢¢–FVçF–f–W2&WV—&VÖVçBÂ6öçG&7BÂFWVæFVæ7’Â66÷R&÷VæF'’ÂWf–FVæ6Rö&Æ–vF–öâÂWF†÷&—¦F–öâ'VÆRÂ÷"W†V7WF–öâÖ6öçFW‡B6öæF—F–öâ–æFWVæFVçBöbF†RÖÆf÷&ÖVB7–çFƒ² ¢¢7FFW2F†R7–çF‚Öæ÷&ÖÆ—¦VB–çFVæFVB÷W&F–öã² ¢¢&÷fW2F†BF†RFVfV7B&VÖ–ç2gFW"f—F†gVÂ7–çF‚æ÷&ÖÆ—¦F–öã²æB ¢¢&VÆ–W2öâWf–FVæ6R÷F†W"F†âF†RÖÆf÷&ÖVB6öÖÖæB&W&W6VçFF–öâ—G6VÆbà ¤Ö—†VBf–æF–ærÕU5B&R6W&FVBâF†R7–çF‚6ö×öæVçB×W7B&RF—66&FVBÂæBöæÇ’F†R–æFWVæFVçFÇ’&÷fVâæöâ×7–çF‚6ö×öæVçBÖ’&RWfÇVFVBà ¤W†×ÆW2öb÷FVçF–ÆÇ’7V'7FçF—fRFVfV7G2–æ6ÇVFRâöÖ—GFVB6VÖçF–2FWVæFVæ7’ÂVæWF†÷&—¦VB&–Ç2÷7GW&RÂÖ—76–ær&WV—&VB÷WGWBÂ6öçG&F–7F÷'’Wf–FVæ6R6öçG&7BÂ÷"–×÷76–&ÆRW†V7WF–öâ6öçFW‡BÂ'WBöæÇ’v†VâF†RFVfV7BW'6—7G2gFW"7–çF‚æ÷&ÖÆ—¦F–öâæB—2&÷fVâv—F†÷WB&VÇ––æröâÖÆf÷&ÖVB6öÖÖæBFW‡Bà ¢222¢¤W†V7WF–öâ÷7GW&R¢  ¥Æâ&Wf–WvW'2&Ræ÷B&WV—&VBFò&W—"7–çF‚&Vf÷&R&÷fÂà ¤GW&–ærW†V7WF–öâÂâvVçBÖ’æ÷&ÖÆ—¦R7–çF‚v—F†÷WB&WV—&–ærÆâ&Wf—6–öâv†VâF†Ræ÷&ÖÆ—¦F–öâ&W6W'fW2F†RÆî(	—26VÖçF–26öçG&7BâF†RW†7B6öÖÖæB7GVÆÇ’W†V7WFVBÂ—G2W†—B6öFRÂæB—G26GW&VB÷WGWB&VÆöær–âF†RW†V7WF–öâWf–FVæ6Rà ¤â–æ—F–Â7–çF‚f–ÇW&RFöW2æ÷B&÷fR&V†f–÷"f–ÇW&RâF†R6öÖÖæBÖ’&Ræ÷&ÖÆ—¦VBæB&W'Vâà ¥F†—2'VÆRFöW2æ÷BWF†÷&—¦R52v—F†÷WB&WV—&VB&V†f–÷&ÂWf–FVæ6Râ–b&WV—&VBW†V7WF–öâWf–FVæ6R&VÖ–ç2'6VçBgFW"æ÷&ÖÆ—¦F–öâæBW†V7WF–öâÂF†R–æFWVæFVçFÇ’&÷fVâ'6Væ6RöbWf–FVæ6RÖ’&RWfÇVFVB6W&FVÇ’âF†R7–çF‚FVfV7B—G6VÆb&VÖ–ç2æöâÖ&Æö6¶–ærà ¢222¢¥&V6VFVæ6RæBG&–ævR¢  ¥v†–ÆR7F—fRÂF†—2FFVæGVÒ7WW'6VFW2ç’–çFW'&WFF–öâöbW&ÖæVçBbÆæwVvRF†BW&Ö—G27–çF‚Ö÷&–v–âFVfV7BFò&V6öÖR&Æö6¶–ær&V6W6R—B6†ævW2ÖVæ–ærÂ6öÖÖæB–FVçF—G’ÂÆ—FW&ÂW†V7WF–öâÂ7FR×&VF–æW72Â÷"'Væ&–Æ—G’à ¤ÆæwVvR7FF–ærF†B7–çF‚—2æöâÖ&Æö6¶–ær(	Æ'’—G6VÆn(	ÒÕU5BäõB&R–çFW'&WFVBFòW&Ö—B&V6Æ76–f–6F–öâ&6VB6öÆVÇ’öâF†RF÷vç7G&VÒ6öç6WVVæ6W2öbF†B7–çF‚à ¥F†RW&ÖæVçBbFö7VÖVçG2&Wf–WvVBF‡W2f"Fòæ÷B&WV—&R&Wf—6–öâ6öÆVÇ’&V6W6RöbF†—2FFVæGVÒâgWGW&RG&–ævR×W7BæWfW'F†VÆW72&W6W'fRF†R6ö×ÆWFR6W6ÂÖ6Æ76–f–6F–öâ'VÆRæBF†R&ö†–&—F–öâöâF÷vç7G&VÒÖVffV7B&V6Æ76–f–6F–öâà ¤G&–ævRÕU5BäõB&RFV6Æ&VB6ö×ÆWFRÖW&VÇ’&V6W6R6æöâ6öçF–ç2&VÆFVBv÷&G27V6‚27–çF‚ÂW66–ærÂö&¦V7F—fRÖf—'7BÂ÷"W†V7WF–öâ×F–ÖRæ÷&ÖÆ—¦F–öââG&–ævRFWFW&Ö–æF–öâ×W7B6öæf—&ÒF†BF†R6ö×ÆWFR'VÆR&÷fR&VÖ–ç26öçG&öÆÆ–ærââVç7W÷'FVB7FFVÖVçBF†BF†R'VÆR—2(	ÆÇ&VG’–â6æöî(	Ò—2–ç7Vff–6–VçBà ¥F†—2FV6—6–öâ—2VffV7F—fR–ÖÖVF–FVÇ’à ¢22¢£"ã#R’&V6övæ—¦RW–2&VÖVF–F–öâÆç2VæF–ærFV×ÆFRG&–ævR¢  ¢FWF–Ç3¢F†—2FFVæGVÒ&V6÷&G2F†R&öGV7B÷væW"FV6—6–öâF†BâW–2&VÖVF–F–öâÆâ—2F—7F–æ7B&÷fÂ'F–f7Bæ÷B–WBFVf–æVB'’¢¤6æöâÆâFV×ÆFW2¢¢â—BW7F&Æ—6†W2FV×÷&'’Æ—fR&Wf–WræB6öçFVçB'VÆW26ò'6Væ6RöbW&ÖæVçBFV×ÆFRFöW2æ÷B&Æö6²7V'7FçF—fVÇ’6fR&VÖVF–F–öâÆâà ¢222¢¤FV6—6–öâ7VÖÖ'’¢  ¤W–2&VÖVF–F–öâÆç2&R&V6övæ—¦VB26W&FRÆâG—Rf÷"&÷VæFVBÂW–2×66÷VB6÷'&V7F—fRv÷&²–FVçF–f–VBgFW"–×ÆVÖVçFF–öâÆææ–ærÂ÷7BÖ–×ÆVÖVçFF–öâVF—BÂ×&VF–æW72&Wf–WrÂ÷"6ö×&&ÆR7W'&VçB×7FFR–ç7V7F–öâà ¤âW–2&VÖVF–F–öâÆâÕU5B&R&Wf–WvVBöâ7V'7FçF—fR6÷'&V7FæW72ÂW†V7WF–öâ6fWG’Â6æöâÆ–væÖVçBÂ&W÷6—F÷'’G'WF‚ÂWf–FVæ6Rö&Æ–vF–öç2ÂWF†÷&—¦F–öâ&÷VæF&–W2ÂæBFV6—6–öâ6ö×ÆWFVæW72â—BÕU5BäõB&R&V¦V7FVBÂ&Wf—6VBÂ÷"6öæF—F–öæVB6öÆVÇ’&V6W6R¢¤6æöâÆâFV×ÆFW2¢¢FöW2æ÷B–WB6öçF–âFVF–6FVBFV×ÆFR÷"&V6W6RF†RÆâFöW2æ÷B6öæf÷&ÒFòâF¦6VçBW–2Æâ÷"&VÖVF–F–öâ–×ÆVÖVçFF–öâwV–FRFV×ÆFRà ¢222¢¥66÷R¢  ¥F†—2FFVæGVÒÆ–W2öæÇ’FòFö7VÖVçG2W‡Æ–6—FÇ’–FVçF–f–VB2W–2&VÖVF–F–öâÆç2à ¤âW–2&VÖVF–F–öâÆâFöW2æ÷B&WÆ6RF†R6öçG&öÆÆ–ærW–2ÆâÂ'&öFW"–×ÆVÖVçFF–öâÆâÂÆâÂÆ—fR'Væ&öö²Ââõ2G&ç67&—BÂâ66WFæ6R&Wf–WrÂ÷"âW–2Ö6Æ÷6R&V6÷&Bâ—BWF†÷&—¦W2öæÇ’—G2W‡&W76Ç’&÷VæFVB6÷'&V7F—fR66÷Rà ¢222¢¤æ÷&ÖF—fRÆ—fR'VÆR¢  ¤âW–2&VÖVF–F–öâÆâÔ’6öçF–â&÷VæFVBDUbæBõ27FW2æBÔ’VÖ&VBW†V7WF–öâÖ÷&–VçFVB7F–öç2Â6öÖÖæG2Â÷WGWG2ÂfW&–f–6F–öâÂæBf–ÇW&R†æFÆ–æræV6W76'’FòÖ¶RF†R&÷fVB&VÖVF–F–öâW†V7WF&ÆRà ¤V6‚W–2&VÖVF–F–öâÆâÕU5B&÷f–FRÂ–â7V'7Fæ6S  ¢¢'F–f7B–FVçF—G’Âf—6–&ÆRfW'6–öâÂW–2–FVçF—G’ÂæB&W÷6—F÷'’&6VÆ–æRv†Vâ&WòG'WF‚ÖGFW'3² ¢¢F†R&VÖVF–F–öâG&–vvW"æB7W'&VçB×7FFRWf–FVæ6S² ¢¢W‡Æ–6—B–â×66÷RæB÷WBÖöb×66÷R&÷VæF&–W3² ¢¢6öçG&öÆÆ–ærcæBW&ÖæVçBÖ6æöâ÷7GW&S² ¢¢†6VBc’ç‚Ö–ær÷"âW‡Æ–6—BÂæöâÖ–çfVçFVBc’v² ¢¢&÷VæFVBDUb÷"õ27FW2v—F‚÷væW"ÂFWVæFVæ6–W2Â–çWG2Â7F–öç2Â÷WGWG2ÂfW&–f–6F–öâÂ7V66W727&—FW&–ÂæBf–ÇW&R†æFÆ–æs² ¢¢6öæ7&WFRWf–FVæ6RæBv÷fW&æVB×F‚÷7GW&Rf÷"W†V7WF–öâ÷WGWG3² ¢¢W‡Æ–6—BFö¶VâÂõ2ÂÂFö7VÖVçFF–öâÖG&–ævRÂ66WFæ6RÂæB6Æ÷7W&R&÷VæF&–W3² ¢¢6ö×ÆWFRE"ÂG&6¶VB—77VRÂ6æöâÖvÂ6æöâ×&V6öæ6–Æ–F–öâÂ66÷RÖ6Æ&–f–6F–öâÂæB&÷fÂÖ—FVÒF—7÷6—F–öç3²æB ¢¢âW‡Æ–6—B&÷fÂ6VçF–æVÂà ¤f÷&ÖBÂ†VF–æræÖW2ÂçVÖ&W&–ærÂæB÷&FW&–ær&RæöâÖ&Æö6¶–ærv†VâF†W6R7V'7FçF—fR&WV—&VÖVçG2&R&W6VçBæBVæÖ&–wV÷W2à ¤õ2v÷&²Â–bç’Â&VÖ–ç2&öGV7BÔ÷væW"ÖöæÇ’W†V7WF–öâÂ–×ÆVÖVçFF–öâÔvVçBÖwV–FVBÂæBWf–FVæ6RÖ&÷VæBâæòWFöÖFVBvVçB—2WF†÷&—¦VBFòW&f÷&Ò&—f–ÆVvVBW‡FW&æÂv÷&²à ¤âW–2&VÖVF–F–öâÆâÔ’&WV—&RÆFW"×&VF–æW72&V76W76ÖVçBâ—BÕU5BäõBVÖ&VBÆ—fRW†V7WF–öâÂ—77VRfW&F–7BÂ6Æ–Ò66WFæ6RÂÖ÷fRc’7FGW2Â÷"6Æ÷6RF†RW–2VæÆW726W&FVÇ’WF†÷&—¦VB'’F†Rv÷fW&æ–ær'F–f7BæB&ö6W72à ¥bÂ&ö&BÂæB7FGW2G&–ævRÕU5B&VÖ–â6W&FRg&öÒDUb÷"õ2W†V7WF–öâ÷WGWG2æBÕU5BäõB&V6öÖR&÷fÂÂÖW&vRÂÖVçG'’Â66WFæ6RÂ÷"6Æ÷6V÷WB6öæF—F–öç2'’F†V×6VÇfW2âG'WF‚Â&ööbÂ6fWG’Â÷"WF†÷&—¦F–öâf–ÇW&W2&VÖ–â7V'7FçF—fR&Æö6¶W'2à ¢222¢¥ÆâVffV7B¢  ¥F†R#W–2&VÖVF–F–öâÆâ„DRÔU”33‚Ö’&R&÷fVBöâ7V'7FçF—fRw&÷VæG2â—G2GG&–'WF–öâFò¢¤6æöâÆâFV×ÆFW2¢¢Â*sB×W7B&R&WÆ6VBv—F‚6—FF–öâFòF†—2FFVæGVÒgFW"F†—2FFVæGVÒÆæG2Â'WBF†B6—FF–öâ6ÆVçW—2æ÷B&W&WV—6—FRFòF†RÆî(	—2&÷VæFVBDUbW†V7WF–öâà ¥F†—2FFVæGVÒFöW2æ÷BW‡æBF†BÆî(	—266÷RÂWF†÷&—¦Rõ2÷"v÷&²Â7&VFRFö¶VâÂÇFW"c’7FGW2Â÷"W7F&Æ—6‚66WFæ6R÷"6Æ÷7W&Rà ¢222¢¤G&–âF&vWB¢  ¤G&–âF†—2ÆâG—RÂ—G2Ö–æ–×VÒ7V'7FçF—fR6öçFVçBÂæB—G2&Wf–Wr÷7GW&R–çFò¢¤6æöâÆâFV×ÆFW2¢¢2FVF–6FVBW–2&VÖVF–F–öâÆâFV×ÆFRæB&÷fÂ'VÆRà ¢222¢¥7WW'6W76–öâ¢  ¥F†—2FFVæGVÒ7WW'6VFW2öæÇ’–çFW'&WFF–öç2F†Bf÷&6RW–2&VÖVF–F–öâÆç2–çFòâF¦6VçBFV×ÆFR÷"G&VBF†R'6Væ6RöbFVF–6FVBFV×ÆFR2&Wf–Wr&Æö6¶W"à ¤—BFöW2æ÷B7WW'6VFRFFVæGVÒ"ã#2ÂFFVæGVÒ"ã#BÂ÷"W&ÖæVçB6æöâv÷fW&æ–ær&6†—FV7GW&RÂc’Ö–ærÂFö¶Vç2ÂWf–FVæ6RÂõ2ÂÂ66WFæ6RÂ÷"6Æ÷7W&Rà ¢222¢¤Wf–FVæ6RæB6÷W&6R&6—2¢  ¥6÷W&6R&6—3¢&öGV7B÷væW"F—&V7F–öâFFVBs#c#c²F†R„DRÔU”33‚W–2&VÖVF–F–öâÆã²cFFVæGVÒ"ã#>(	—2W†7B×F÷–2&VÖVF–F–öâf–æF–æs²æB&VBÖöæÇ’&W÷6—F÷'’fÆ–FF–öâBÖ–äƒ3ƒ&V&fCfV&#FFVV“f3SS&6C&3cs3S†&&à ¥&WV—&VBföÆÆ÷rÖöâÆâF—7÷6—F–öã¢Ö&²&W6öÇfVB'’æWrcFFVæGVÐ ¥&WV—&VBÆâ&Wf—6–öâFW‡C¢VæFW"%Â5Â26æöâg&ÖS¢v†B6÷'&V7BÖVç2"Â&WÆ6RF†R&VÆFVBD”E"æ6†÷"v—F‚W†7FÇ“¢%Â¢F†—2W–2&VÖVF–F–öâÆâW6W2öæR&÷VæFVBDUb&VÖVF–F–öâ7FWv—F‚VÖ&VFFVBfW&–f–6F–öâÂW‡Æ–6—BÆæR6W&F–öâÂæBâ&÷fÂ6VçF–æVÂâc#rFöW2æ÷B–WBFVf–æRF†—2ÆâG—S²FV×÷&'’&Wf–Wr÷7GW&R—2v÷fW&æVB'’cFFVæGVÒ"ã#RVçF–ÂG&–æVB–çFòc#râ"VæFW"%Â5Â2bFö726öç7VÇFVB"ÂFBW†7FÇ’%Â¢cÂÒ„DR'V–ÆBæ÷FW2ÂFFVæGVÒ"ã#Râ"æB&WÆ6R%Â¢c#rÂÒ6æöâÆâFV×ÆFW2Âcã’ãRâ"v—F‚W†7FÇ’%Â¢c#rÂÒ6æöâÆâFV×ÆFW2Âcã’ãRÂÒ6öç7VÇFVC²æòW–2&VÖVF–F–öâÆâFV×ÆFRW†—7G2â  ¤G&–âF&vWB‡2“  ¥c#rÂÒ6æöâÆâFV×ÆFW0 ¤6æöâ&VfW&Væ6RÂ–b&VÆ–VBöã¢cÂÒ„DR'V–ÆBæ÷FW2Â*uW'÷6Rò*u&V6VFVæ6RæBfW'6–öæ–æp ¤6æöâ&ööbW†6W'BÂ–b&VÆ–VBöã  ¢%F†—2f–ÆR—2¢§v÷&¶–ær67&F6‡Bf÷"æWrÂæ÷B×–WBÖÖW&vVBFö7VÖVçFF–öâ¢¢âG&VB—B2F†R7W'&VçB6÷W&6RöbG'WF‚¢¦öæÇ’f÷"F†R7V6–f–2—FV×2—BW‡Æ–6—FÇ’6÷fW'2¢¢âf÷"WfW'—F†–ærVÇ6RÂbÔ6æöâ…cÂc"ÂcBÂcRÂc’Âc"ÂcBÂc’Âc#ÂWF2â’&VÖ–ç2F†R6–ævÆR†öÖRâ  ¢"¢¥c•24äôä”4Ââ¢¢f÷"ç’F÷–2W‡Æ–6—FÇ’6÷fW&VB–âF†—267&F6‡BÂc—2F†R7W'&VçBWF†÷&—FF—fR6÷W&6RöbG'WF‚æB¢§7WW'6VFW2ÆÂ÷F†W"b6æöâ¢¢VçF–ÂF†B—FVÒ—2f÷&ÖÆÇ’&Wf–WvVBæBG&–æVB–çFòF†R&VÆWfçBW&ÖæVçBbFö7VÖVçBâ  ¥ÃÆVöeÃ