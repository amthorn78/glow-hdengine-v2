# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v11.8.1  
Effective Date: 2026.06.29

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

 Inside this file, all references to PF documents MUST be **titles-only** (for example “HDE-Phased Epics”, “Glow QA Guide”), never file names or version numbers in the body text.

When editing or extending this file, ChatGPT sessions must:

* Not restate PF content here.

* Link by **document title and section only**.

# 1\) TEMPLATE

TEMPLATE Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\> (autofill from system info)  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## 1.1 Addendum Index:

2.1) PR-01 HDE-EPIC035  
2.2) PR-02 HDE-EPIC035  
2.3) PF29 HD Engine User Guide seed — runnable end-to-end workflows  
2.4) OPS-01 HDE-EPIC035  
2.5) PR-02 HDE-EPIC035  
2.6) Implementation Retrospective  HDE-EPIC035  
2.7) ADR — ChartResult adapter gap is accepted for HDE-EPIC035 evidence, but future runtime work must prove full BodyGraph-detail mapping  
2.8) ADR — bg:resolve \--source vendor must resolve BodyGraph detail through an explicit vendor-route policy, not accidental legacy route composition

# 2\) Numbered Addenda

---

## 2.1) PR-01 HDE-EPIC035

Review Summary

* Original PR \#328 added the HDE-EPIC035 PR-01 HDAPI v2 provider-outcome evidence family for PF09.5 / HDE-FERM008 / HDE-FERM008.3: a generator, two governed snapshots, path proofs, evidence-index / mirror bindings, and targeted tests.  
* Original PR \#328 left material gaps: direct artifact path proofs were backdated, the Machine Mirror family later showed proof chronology drift, and the generator declared closed rails without enforcing closed-rails environment before certification.  
* First Remedial PR \#329 corrected direct PR-01 artifact timestamping and added chronology regression coverage, but current review of that lifecycle found remaining Machine Mirror path-proof chronology and closed-rails enforcement gaps.  
* Second Remedial PR \#330 addressed the remaining two gaps: it added `enforce_closed_rails()` before generator check/write certification and extended non-backdating path-proof handling to PR-01 artifacts plus `artifacts/evidence_index.jsonl` and `artifacts/evidence_index.jsonl.sha256`.  
* Current GitHub Repo state equals the second remedial merge commit; no later commits affect the reviewed files.  
* Current governed evidence now shows coherent chronology for the PR-01 snapshots, Human Index, Machine Mirror, hash sentinels, and their reviewed path proofs.  
* Visible CI for all three PR heads completed successfully; Second Remedial PR reports the required targeted tests, generator check, evidence-index check, path validation, mirror schema check, hash check, and negative open-rails generator refusal.  
* PF09 impact is limited to PF09.5 / HDE-FERM008 / HDE-FERM008.3. The reviewed evidence supports a status recommendation to change HDE-FERM008.3 to Done, without claiming HDE-FERM008 parent completion.

GitHub / Repo Inspection

Repository identity:

* GitHub Repo | repo metadata | "repository\_full\_name: amthorn78/glow-hdengine-v2" | "default\_branch: main"

Reviewed branch/default branch:

* GitHub Repo | repo metadata | "default\_branch: main"

Current HEAD:

* GitHub Repo | compare `bb0092398b50c54fea62da6cb825e3c845fbdf0b..main` | "status: identical" | "total\_commits: 0"

Original PR merged state and merge identifier:

* Original PR | PR \#328 metadata | "state: closed" | "merged: true" | "merge\_commit\_sha: 56ac6a26efe29d43e5399f47ec002a84c7b82ba0"

First Remedial PR merged state and merge identifier:

* First Remedial PR | PR \#329 metadata | "state: closed" | "merged: true" | "merge\_commit\_sha: bf6cea65ee252c2f18924416d3b8ba56b8c1c276"

Second Remedial PR merged state and merge identifier:

* Second Remedial PR | PR \#330 metadata | "state: closed" | "merged: true" | "merge\_commit\_sha: bb0092398b50c54fea62da6cb825e3c845fbdf0b"

Changed files per PR:

* Original PR | PR \#328 metadata / changed-file list | "changed\_files: 36" | included the PR-01 generator, PR-01 tests, evidence updater, two HDAPI v2 snapshots and path proofs, Human Index, Machine Mirror, hash sentinels, and updater-convergence path proofs.  
* First Remedial PR | PR \#329 metadata / changed-file list | "changed\_files: 35" | updated the PR-01 generator, tests, evidence updater, PR-01 snapshots, evidence index/mirror/hash/path-proof family, and updater-convergence path proofs.  
* Second Remedial PR | PR \#330 metadata / changed-file list | "changed\_files: 35" | updated the PR-01 generator, tests, evidence updater, PR-01 snapshots, evidence index/mirror/hash/path-proof family, and updater-convergence path proofs.

Net touched files:

* GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | "ahead\_by: 3" | "files: 36"

Current final file state inspected:

* GitHub Repo | final file inspection | `tools/evidence/generate_hdapi_v2_live_conformance.py` | complete file lines 1-216 inspected.  
* GitHub Repo | final file inspection | `tools/evidence/update_evidence_index.py` | EPIC035 loader, `NON_BACKDATED_PROOF_RELS`, and `_write_path_proof` logic inspected.  
* GitHub Repo | final file inspection | `tests/evidence/test_hdapi_v2_live_conformance.py` | complete file lines 1-208 inspected.  
* GitHub Repo | final file inspection | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` and `.path_proof.txt` inspected.  
* GitHub Repo | final file inspection | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` and `.path_proof.txt` inspected.  
* GitHub Repo | final file inspection | `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.path_proof.txt`, `artifacts/evidence_index.jsonl.sha256`, and `artifacts/evidence_index.jsonl.sha256.path_proof.txt` inspected.  
* GitHub Repo | final file inspection | `docs/evidence/INDEX.json.path_proof.txt` and `docs/evidence/INDEX.sha256.path_proof.txt` inspected.

Checks/CI inspected:

* Original PR | workflow runs for head `83885086bc882bfc17b71ed4ff1d426dfef4fb6d` | "name: ci" | "conclusion: success"  
* First Remedial PR | workflow runs for head `9f9646607a7c5a2c8bbe7e681b1f6fa77c094107` | "name: ci" | "conclusion: success"  
* Second Remedial PR | workflow runs for head `eae7778e21ff9f33cf008089acd865074898d8c5` | "name: ci" | "conclusion: success"

Governed evidence inspected:

* GitHub Repo | final evidence inspection | PR-01 HDAPI v2 snapshots, snapshot path proofs, Human Index proof, Human Index hash proof, Machine Mirror rows, Machine Mirror proof, Machine Mirror hash sentinel, Machine Mirror hash proof.

Later commits affecting touched files:

* GitHub Repo | compare `bb0092398b50c54fea62da6cb825e3c845fbdf0b..main` | "status: identical" | "files: \[\]"

Provenance (Original \-\> First Remediation \-\> Second Remediation)

* Claim: Original PR intended to add deterministic governed HDAPI v2 provider outcome evidence for HDE-FERM008.3.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#328 body | "Provide deterministic, closed-rails governed evidence for HDE-FERM008.3" | "v2 HTTP status → provider-code mapping, retry classification, Retry-After parsing, malformed-response classification, network-error posture, and secret-safe observability."  
* Claim: Original PR added the planned generator and two required governed artifacts.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#328 body | "Add a new evidence generator `tools/evidence/generate_hdapi_v2_live_conformance.py`" | "`artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`" | "`artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`"  
* Claim: Extra Evidence corroborates Original PR implementation and validation claims, but is supplemental to GitHub Repo current truth.  
  Source: Extra Evidence  
  Evidence pointer: Extra Evidence | bundle summary | "Added a new deterministic closed-rails HDE-EPIC035 PR-01 generator" | "No validation was intentionally skipped. The final git status \--short was clean."  
* Claim: Original PR direct artifact path proofs were backdated.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#328 diff for `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T05:30:40Z" | "produced\_at\_utc: 2026-06-28T00:00:00Z"  
* Claim: Original PR had an unresolved rail-enforcement review concern.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#328 review thread on `tools/evidence/generate_hdapi_v2_live_conformance.py` | "Require closed rails before emitting provider evidence" | "`SAFE_MODE=0 ALLOW_NETWORK=1 ... --check` exits 0"  
* Claim: First Remedial PR targeted generated timestamp and direct artifact chronology.  
  Source: First Remedial PR  
  Evidence pointer: First Remedial PR | PR \#329 body | "Prevent generated HDAPI v2 evidence snapshots from appearing to be produced earlier than their filesystem mtimes and path-proofs" | "Make the live-conformance generator produce and propagate canonical UTC produced timestamps"  
* Claim: First Remedial PR fixed the direct artifact-level chronology but left Machine Mirror proof chronology and rail-enforcement gaps.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | first remediation review state | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt` showed matching artifact proof timestamps after PR \#329 | `artifacts/evidence_index.jsonl.path_proof.txt` still showed `mtime_utc: 2026-06-28T07:47:36Z` and `produced_at_utc: 2026-06-28T07:46:57Z`.  
* Claim: Second Remedial PR targeted the remaining evidence chronology and closed-rails enforcement issues.  
  Source: Second Remedial PR  
  Evidence pointer: Second Remedial PR | PR \#330 body | "Fix governed-evidence chronology defects where the machine mirror and mirror-hash path proofs could be backdated" | "Ensure the HDE-EPIC035 PR-01 HDAPI v2 generator enforces closed deterministic rails"  
* Claim: Second Remedial PR added a closed-rails guard before certification.  
  Source: Second Remedial PR  
  Evidence pointer: Second Remedial PR | patch for `tools/evidence/generate_hdapi_v2_live_conformance.py` | "@@ \-160,6 \+161,16 @@" | "def enforce\_closed\_rails()" | "env \= ensure\_determinism\_env()"  
* Claim: Current GitHub Repo confirms closed-rails enforcement is in the final generator.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | `tools/evidence/generate_hdapi_v2_live_conformance.py` | "from engine.runtime.determinism\_env import DeterminismEnvError, ensure\_determinism\_env" | "enforce\_closed\_rails()" | "raise SystemExit(f"HDAPI\_V2\_LIVE\_CONFORMANCE\_CLOSED\_RAILS\_REQUIRED:{exc}")"  
* Claim: Second Remedial PR expanded non-backdating proof protection to Machine Mirror artifacts.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | `tools/evidence/update_evidence_index.py` | "NON\_BACKDATED\_PROOF\_RELS" | ""artifacts/evidence\_index.jsonl"" | ""artifacts/evidence\_index.jsonl.sha256""  
* Claim: Current GitHub Repo confirms Machine Mirror proof chronology is now coherent.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"; GitHub Repo | `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"  
* Claim: Current GitHub Repo confirms the direct HDAPI v2 PR-01 artifact proofs remain coherent after the second remediation.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"; GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"  
* Claim: Current tests now cover both remediated failure families.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | `tests/evidence/test_hdapi_v2_live_conformance.py` | "test\_machine\_mirror\_path\_proofs\_are\_not\_backdated" | "test\_generator\_refuses\_non\_closed\_rails\_without\_writing" | "test\_generator\_refuses\_network\_enabled\_check\_without\_certifying"  
* Claim: Current PR-01 evidence retains the approved no-claim posture.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""live\_vendor\_call":"NONE"" | ""full\_hdapi\_v2\_runtime\_conformance":"NONE"" | ""public\_reader\_change":"NONE""

Net Effective Diff Review

NET ID: NET-001

File/artifact: `artifacts/evidence_index.jsonl`

Covered hunks: OPR-002 / R1PR-002 / R2PR-002

Final repo state: Contains PR-01 rows for `hdapi_v2.error_mapping` and `hdapi_v2.rate_limit_headers`, plus current index self-records.

Risk: High

Assessment: Current Machine Mirror rows bind the PR-01 artifacts with HDE-EPIC035 metadata, PR-01 record type, correct current sha / size values, and non-backdated produced timestamps. Final state is acceptable for reviewed scope.

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl` | ""artifact\_key":"hdapi\_v2.error\_mapping"" | ""produced\_at\_utc":"2026-06-28T08:36:03Z"" | ""artifact\_key":"hdapi\_v2.rate\_limit\_headers"" | ""produced\_at\_utc":"2026-06-28T08:36:03Z""

GitHub Repo proof: GitHub Repo | final file inspection | `artifacts/evidence_index.jsonl` rows for `hdapi_v2.error_mapping`, `hdapi_v2.rate_limit_headers`, `index.human_index`, and `index.machine_mirror`.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-002

File/artifact: `artifacts/evidence_index.jsonl.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Machine Mirror path proof has matching `mtime_utc` and `produced_at_utc`.

Risk: High

Assessment: Original and first-remediation chronology defects are closed.

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"

GitHub Repo proof: GitHub Repo | final file inspection | `path: artifacts/evidence_index.jsonl`, `size_bytes: 166029`, `mirror_body_sha256: cedd3bb559bef29b93a2c710f4e307b9a6002997c489c15362e1dc5f0e28c4a3`.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-003

File/artifact: `artifacts/evidence_index.jsonl.sha256`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Mirror hash sentinel points to current Machine Mirror bytes.

Risk: Medium

Assessment: Expected hash sentinel update for changed Machine Mirror; companion proof is also coherent.

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl.sha256` | "2b50c08284959483dd31fd76b62c850f5c7990a17e7ebc91859371fab7c6aeb3 artifacts/evidence\_index.jsonl"

GitHub Repo proof: GitHub Repo | final file inspection | single-line hash sentinel observed.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-004

File/artifact: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Mirror hash sentinel path proof has matching `mtime_utc` and `produced_at_utc`.

Risk: High

Assessment: Remaining first-remediation mirror-hash chronology defect is closed.

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"

GitHub Repo proof: GitHub Repo | final file inspection | `path: artifacts/evidence_index.jsonl.sha256`, `size_bytes: 97`.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-005

File/artifact: `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No product, contract, or PR-01 scope drift identified.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/narratives/router/cli_http_parity.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-006

File/artifact: `artifacts/narratives/router/parity_abba.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No product, contract, or PR-01 scope drift identified.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/narratives/router/parity_abba.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-007

File/artifact: `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`

Covered hunks: OPR-001 / OPR-003 / R1PR-001 / R2PR-001

Final repo state: New canonical JSON provider outcome mapping snapshot with HDE-EPIC035 / HDE-FERM008.3 metadata and current `generated_at_utc: 2026-06-28T08:36:03Z`.

Risk: High

Assessment: Satisfies PR-01 mapping scope: status-to-provider-code mapping, retry classification, malformed/bad-response, network error, secret-safe observability, closed-rails metadata, and no-claim posture.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""pf09\_subtask\_id":"HDE-FERM008.3"" | ""retry\_classification":{"429":false,"4xx":false,"5xx":true,"http\_status\_other":false,"network\_error":true,"redirect\_response":false}" | ""no\_raw\_vendor\_payload":true"

GitHub Repo proof: GitHub Repo | final file inspection | full one-line canonical JSON snapshot observed.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.3 \- Map v2 error, retry, and rate-limit behavior

NET ID: NET-008

File/artifact: `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt`

Covered hunks: OPR-001 / OPR-003 / R1PR-001 / R2PR-002

Final repo state: Path proof exists and is non-backdated.

Risk: High

Assessment: Direct artifact path-proof chronology is coherent.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"

GitHub Repo proof: GitHub Repo | final file inspection | path, size, sha256, mtime, and produced fields observed.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-009

File/artifact: `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`

Covered hunks: OPR-001 / OPR-003 / R1PR-001 / R2PR-001

Final repo state: New canonical JSON Retry-After / rate-limit snapshot with HDE-EPIC035 / HDE-FERM008.3 metadata and current `generated_at_utc: 2026-06-28T08:36:03Z`.

Risk: High

Assessment: Satisfies PR-01 rate-limit scope: 429 non-retryable posture, delta-seconds parsing, HTTP-date parsing, invalid omission, and overflow omission.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | ""rate\_limit\_status\_record":{"classification":"429","provider\_code":"PROVIDER\_RATE\_LIMITED"" | ""case":"delta\_seconds"" | ""case":"http\_date"" | ""case":"invalid"" | ""case":"overflow""

GitHub Repo proof: GitHub Repo | final file inspection | full one-line canonical JSON snapshot observed.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.3 \- Map v2 error, retry, and rate-limit behavior

NET ID: NET-010

File/artifact: `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt`

Covered hunks: OPR-001 / OPR-003 / R1PR-001 / R2PR-002

Final repo state: Path proof exists and is non-backdated.

Risk: High

Assessment: Direct artifact path-proof chronology is coherent.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"

GitHub Repo proof: GitHub Repo | final file inspection | path, size, sha256, mtime, and produced fields observed.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-011

File/artifact: `artifacts/writer/conjunction_write_readback.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No PR-01 product or evidence-family drift identified.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/writer/conjunction_write_readback.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-012

File/artifact: `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No PR-01 product or evidence-family drift identified.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/writer/conjunction_writer_summary.json.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-013

File/artifact: `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing doc-delta path-proof companion refreshed.

Risk: Low

Assessment: Documentation-drainage companion only; no execution or acceptance blocker.

Evidence pointer(s): GitHub Repo | net compare | "`audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-014

File/artifact: `audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing doc-delta path-proof companion refreshed.

Risk: Low

Assessment: Documentation-drainage companion only; no execution or acceptance blocker.

Evidence pointer(s): GitHub Repo | net compare | "`audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-015

File/artifact: `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/gates/narratives/keys_10x4.table.json.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-016

File/artifact: `audit/gates/narratives/pack_identity.txt.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/gates/narratives/pack_identity.txt.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-017

File/artifact: `audit/gates/narratives/registry.diff.json.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/gates/narratives/registry.diff.json.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-018

File/artifact: `audit/gates/topology/orientation_demo.txt`

Covered hunks: OPR-002

Final repo state: Orientation demo count updated from 390 to 392 in the net change set.

Risk: Medium

Assessment: Original orientation-demo drift was corrected and remains part of the final net change.

Evidence pointer(s): Original PR | PR \#328 patch for `audit/gates/topology/orientation_demo.txt` | "total\_artifacts: 390" | "total\_artifacts: 392"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | `audit/gates/topology/orientation_demo.txt` modified with 1 addition and 1 deletion.

PF reference, if relied on: None

NET ID: NET-019

File/artifact: `audit/gates/topology/orientation_demo.txt.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Orientation demo path proof refreshed as companion to the updated artifact count.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/gates/topology/orientation_demo.txt.path_proof.txt`" | "changes: 6"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-020

File/artifact: `audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-021

File/artifact: `audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-022

File/artifact: `audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-023

File/artifact: `audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-024

File/artifact: `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-025

File/artifact: `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-026

File/artifact: `audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-027

File/artifact: `audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-028

File/artifact: `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No independent issue found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-029

File/artifact: `audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Existing doc-delta path-proof companion refreshed.

Risk: Low

Assessment: Documentation-drainage companion only; no execution or acceptance blocker.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`" | "changes: 4"

GitHub Repo proof: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | file listed as modified.

PF reference, if relied on: None

NET ID: NET-030

File/artifact: `docs/evidence/INDEX.json`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Human Evidence Index updated for PR-01 artifacts and proof family.

Risk: High

Assessment: Required Human Index update is present and companion proof chronology is coherent.

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl` | ""artifact\_key":"hdapi\_v2.error\_mapping"" | ""artifact\_key":"hdapi\_v2.rate\_limit\_headers"" | ""artifact\_key":"index.human\_index""

GitHub Repo proof: GitHub Repo | `docs/evidence/INDEX.json.path_proof.txt` | `sha256: 70f1de940cbb9597ff3d875b76f3f6f2238af0c6cb6af4de67826448cd8bb508`, `mtime_utc: 2026-06-28T08:36:04Z`, `produced_at_utc: 2026-06-28T08:36:04Z`.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-031

File/artifact: `docs/evidence/INDEX.json.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Human Index path proof exists and is non-backdated.

Risk: High

Assessment: Required companion proof is coherent.

Evidence pointer(s): GitHub Repo | `docs/evidence/INDEX.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"

GitHub Repo proof: GitHub Repo | final file inspection | path, size, sha256, mtime, produced fields observed.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-032

File/artifact: `docs/evidence/INDEX.sha256`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Human Index hash sentinel refreshed.

Risk: Medium

Assessment: Required hash sentinel update is present; companion proof is coherent.

Evidence pointer(s): GitHub Repo | `docs/evidence/INDEX.sha256.path_proof.txt` | "path: docs/evidence/INDEX.sha256" | "sha256: 6130d5b0d3504a23e85ac880f23e4f4d8275284ec507fd4fa305328df0337e6c"

GitHub Repo proof: GitHub Repo | final file inspection | `docs/evidence/INDEX.sha256.path_proof.txt`.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-033

File/artifact: `docs/evidence/INDEX.sha256.path_proof.txt`

Covered hunks: OPR-002 / R1PR-003 / R2PR-002

Final repo state: Human Index hash sentinel path proof exists and is non-backdated.

Risk: High

Assessment: Required companion proof is coherent.

Evidence pointer(s): GitHub Repo | `docs/evidence/INDEX.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"

GitHub Repo proof: GitHub Repo | final file inspection | path, size, sha256, mtime, produced fields observed.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-034

File/artifact: `tests/evidence/test_hdapi_v2_live_conformance.py`

Covered hunks: OPR-003 / R1PR-002 / R2PR-003

Final repo state: Adds tests for artifact canonicality and scope, provider mapping, retry posture, Retry-After cases, index/mirror/path-proof binding, artifact chronology, checkout-mtime independence, Machine Mirror proof chronology, and non-closed-rails generator refusal.

Risk: Medium

Assessment: Test coverage now addresses both original and remediation-discovered gaps.

Evidence pointer(s): GitHub Repo | `tests/evidence/test_hdapi_v2_live_conformance.py` | "test\_machine\_mirror\_path\_proofs\_are\_not\_backdated" | "test\_generator\_refuses\_non\_closed\_rails\_without\_writing" | "test\_generator\_refuses\_network\_enabled\_check\_without\_certifying"

GitHub Repo proof: GitHub Repo | final file inspection | tests present at lines 163-208.

PF reference, if relied on: None

NET ID: NET-035

File/artifact: `tools/evidence/generate_hdapi_v2_live_conformance.py`

Covered hunks: OPR-001 / OPR-004 / R1PR-001 / R2PR-001

Final repo state: Adds the PR-01 evidence generator with canonical rendering, produced timestamp handling, artifact mtime alignment, and closed-rails enforcement before check/write certification.

Risk: High

Assessment: Final generator aligns with approved PR-01 scope. It reuses the existing vendor client seam for deterministic mappings, has no live vendor call path, and now refuses non-closed-rails certification.

Evidence pointer(s): GitHub Repo | `tools/evidence/generate_hdapi_v2_live_conformance.py` | "def enforce\_closed\_rails()" | "env \= ensure\_determinism\_env()" | "write\_outputs(render\_outputs(produced\_at=produced\_at), check=args.check)"

GitHub Repo proof: GitHub Repo | final file inspection | complete file lines 1-216, including import of `ensure_determinism_env`, `enforce_closed_rails`, and `SystemExit` on rails mismatch.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

NET ID: NET-036

File/artifact: `tools/evidence/update_evidence_index.py`

Covered hunks: OPR-002 / R1PR-002 / R2PR-002

Final repo state: Adds EPIC035 PR-01 index entries and non-backdating path-proof validation for PR-01 snapshots plus Machine Mirror and mirror-hash artifacts.

Risk: High

Assessment: Final updater supports required PR-01 index/mirror binding and remediates the previously observed mirror proof chronology gap.

Evidence pointer(s): GitHub Repo | `tools/evidence/update_evidence_index.py` | "EPIC035\_PR01\_ARTIFACT\_RELS" | "NON\_BACKDATED\_PROOF\_RELS" | "if rel in NON\_BACKDATED\_PROOF\_RELS and produced\_parsed \< mtime\_parsed"

GitHub Repo proof: GitHub Repo | final file inspection | `NON_BACKDATED_PROOF_RELS` includes both PR-01 snapshot paths, `artifacts/evidence_index.jsonl`, and `artifacts/evidence_index.jsonl.sha256`.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

Validation & Evidence Review

VAL-001

Purpose: Prove all three PRs are merged.

Source: GitHub Repo

Check/workflow/artifact/method: GitHub PR metadata inspection.

Result: PASS

Observation: PR \#328, PR \#329, and PR \#330 are all `state: closed` and `merged: true`.

Evidence pointer: Original PR | PR \#328 metadata | "merged: true" | "merge\_commit\_sha: 56ac6a26efe29d43e5399f47ec002a84c7b82ba0"; First Remedial PR | PR \#329 metadata | "merged: true" | "merge\_commit\_sha: bf6cea65ee252c2f18924416d3b8ba56b8c1c276"; Second Remedial PR | PR \#330 metadata | "merged: true" | "merge\_commit\_sha: bb0092398b50c54fea62da6cb825e3c845fbdf0b"

Why it matters: Establishes the three-PR lifecycle and exact merge identities.

VAL-002

Purpose: Prove current GitHub Repo state is the second remedial merge state.

Source: GitHub Repo

Check/workflow/artifact/method: Compare `bb0092398b50c54fea62da6cb825e3c845fbdf0b..main`.

Result: PASS

Observation: Compare returned `status: identical`, `ahead_by: 0`, `behind_by: 0`, and `files: []`.

Evidence pointer: GitHub Repo | compare `bb0092398b50c54fea62da6cb825e3c845fbdf0b..main` | "status: identical" | "total\_commits: 0"

Why it matters: No later changes need to be separated from the reviewed lifecycle.

VAL-003

Purpose: Verify net changed file set.

Source: GitHub Repo

Check/workflow/artifact/method: Compare `68a9ca661056d4f2940a241a6401a6084453131d..main`.

Result: PASS

Observation: Net compare shows 36 files and 3 commits ahead.

Evidence pointer: GitHub Repo | compare `68a9ca661056d4f2940a241a6401a6084453131d..main` | "ahead\_by: 3" | "files: 36"

Why it matters: Establishes net effective change set.

VAL-004

Purpose: Verify Original PR CI.

Source: Original PR

Check/workflow/artifact/method: Workflow run for head `83885086bc882bfc17b71ed4ff1d426dfef4fb6d`.

Result: PASS

Observation: CI completed successfully.

Evidence pointer: Original PR | workflow runs | "name: ci" | "conclusion: success"

Why it matters: Confirms visible CI state for attempt 0\.

VAL-005

Purpose: Verify First Remedial PR CI.

Source: First Remedial PR

Check/workflow/artifact/method: Workflow run for head `9f9646607a7c5a2c8bbe7e681b1f6fa77c094107`.

Result: PASS

Observation: CI completed successfully.

Evidence pointer: First Remedial PR | workflow runs | "name: ci" | "conclusion: success"

Why it matters: Confirms visible CI state for remediation attempt 1\.

VAL-006

Purpose: Verify Second Remedial PR CI.

Source: Second Remedial PR

Check/workflow/artifact/method: Workflow run for head `eae7778e21ff9f33cf008089acd865074898d8c5`.

Result: PASS

Observation: CI completed successfully.

Evidence pointer: Second Remedial PR | workflow runs | "name: ci" | "conclusion: success"

Why it matters: Confirms visible CI state for remediation attempt 2\.

VAL-007

Purpose: Verify direct PR-01 artifact chronology.

Source: GitHub Repo

Check/workflow/artifact/method: Current path-proof inspection.

Result: PASS

Observation: Both PR-01 snapshot path proofs have `mtime_utc` equal to `produced_at_utc`.

Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"; GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"

Why it matters: Closes the Original PR direct artifact chronology defect.

VAL-008

Purpose: Verify Machine Mirror and mirror-hash chronology.

Source: GitHub Repo

Check/workflow/artifact/method: Current path-proof inspection.

Result: PASS

Observation: Both Machine Mirror companion proofs have `mtime_utc` equal to `produced_at_utc`.

Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"; GitHub Repo | `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"

Why it matters: Closes the First Remedial PR remaining chronology defect.

VAL-009

Purpose: Verify generator closed-rails enforcement.

Source: GitHub Repo

Check/workflow/artifact/method: Current generator inspection.

Result: PASS

Observation: Generator calls `enforce_closed_rails()` before render/check/write certification and raises `SystemExit` with `HDAPI_V2_LIVE_CONFORMANCE_CLOSED_RAILS_REQUIRED` on determinism-env error.

Evidence pointer: GitHub Repo | `tools/evidence/generate_hdapi_v2_live_conformance.py` | "try:" | "enforce\_closed\_rails()" | "raise SystemExit(f"HDAPI\_V2\_LIVE\_CONFORMANCE\_CLOSED\_RAILS\_REQUIRED:{exc}")"

Why it matters: Closes the original rail-enforcement gap.

VAL-010

Purpose: Verify regression tests for remaining gaps.

Source: GitHub Repo

Check/workflow/artifact/method: Current test-file inspection.

Result: PASS

Observation: Tests cover Machine Mirror proof chronology and non-closed-rails generator refusal without writing/certifying artifacts.

Evidence pointer: GitHub Repo | `tests/evidence/test_hdapi_v2_live_conformance.py` | "test\_machine\_mirror\_path\_proofs\_are\_not\_backdated" | "test\_generator\_refuses\_non\_closed\_rails\_without\_writing" | "test\_generator\_refuses\_network\_enabled\_check\_without\_certifying"

Why it matters: Reduces recurrence risk for both remediated defects.

VAL-011

Purpose: Verify reported Second Remedial validation set.

Source: Second Remedial PR

Check/workflow/artifact/method: PR \#330 body testing section.

Result: PASS

Observation: Second Remedial PR reports targeted pytest, generator `--check`, evidence-index `--check`, evidence path validation, mirror schema check, hash check, and negative `SAFE_MODE=0` validation.

Evidence pointer: Second Remedial PR | PR \#330 body | "Ran `python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_live_conformance.py` under closed rails and all tests passed" | "negative validation with `SAFE_MODE=0` ... fail closed"

Why it matters: Matches the required post-remediation validation posture for reviewed scope.

VAL-012

Purpose: Verify current PR-01 evidence content.

Source: GitHub Repo

Check/workflow/artifact/method: Current snapshot inspection.

Result: PASS

Observation: Final snapshots include HDE-EPIC035 / HDE-FERM008.3 metadata, no-claim posture, error mapping, retry mapping, Retry-After records, and secret-safe observability posture.

Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""pf09\_subtask\_id":"HDE-FERM008.3"" | ""network\_error\_record"" | ""observability\_posture"" | GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | ""rate\_limit\_status\_record"" | ""retry\_after\_records""

Why it matters: Confirms final current evidence supports PR-01 scope.

Requirement Satisfaction Crosswalk

Requirement: Produce deterministic canonical JSON evidence for v2 HTTP status-to-provider-code mapping.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""status\_mapping\_records"" | ""PROVIDER\_UNAUTHORIZED"" | ""PROVIDER\_RATE\_LIMITED"" | ""PROVIDER\_UNAVAILABLE"" | ""PROVIDER\_ERROR""

GitHub Repo proof, if current state matters: Final snapshot contains 401, 403, 404, 429, 500, 503, and 302 mappings.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Notes, optional: None.

Requirement: Prove `network_error` and `5xx` retryable classification.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""network\_error\_record":{"classification":"network\_error","provider\_code":"PROVIDER\_NETWORK\_ERROR","retryable":true}" | ""5xx":true"

GitHub Repo proof, if current state matters: Final snapshot contains retry classification.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Prove `429`, other `4xx`, non-200 non-5xx statuses, and redirect responses are non-retryable.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""429":false" | ""4xx":false" | ""http\_status\_other":false" | ""redirect\_response":false"

GitHub Repo proof, if current state matters: Final snapshot contains retry classification.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Prove Retry-After delta-seconds parsing.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | ""case":"delta\_seconds"" | ""parsed\_retry\_after\_ms":7000"

GitHub Repo proof, if current state matters: Final snapshot contains delta-seconds Retry-After case.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Prove Retry-After HTTP-date parsing.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | ""case":"http\_date"" | ""parsed\_retry\_after\_ms":5000"

GitHub Repo proof, if current state matters: Final snapshot contains HTTP-date Retry-After case.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Prove invalid or overflow Retry-After omission.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | ""case":"invalid"" | ""parsed\_retry\_after\_ms":null" | ""case":"overflow""

GitHub Repo proof, if current state matters: Final snapshot contains invalid and overflow omission cases.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Prove malformed JSON response classification and provider bad-response classification.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""bad\_response\_records"" | ""scenario":"malformed\_json\_response"" | ""provider\_code":"PROVIDER\_BAD\_RESPONSE""

GitHub Repo proof, if current state matters: Final snapshot contains bad-response records.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Prove keys-only, bounded, secret-safe observability posture.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""keys\_only":true" | ""no\_raw\_request\_body":true" | ""no\_raw\_response\_body":true" | ""no\_raw\_secret\_header":true" | ""no\_plaintext\_secret\_value":true"

GitHub Repo proof, if current state matters: Final snapshot contains observability posture.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Preserve no live vendor call, no full HumanDesignAPI v2 runtime conformance, no public Reader change, no public route/flag/payload/transport change, no raw vendor payload persistence.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""live\_vendor\_call":"NONE"" | ""full\_hdapi\_v2\_runtime\_conformance":"NONE"" | ""public\_reader\_change":"NONE"" | ""raw\_vendor\_payload\_persisted":"NONE""

GitHub Repo proof, if current state matters: Final snapshots retain no-claim posture.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Run PR work and evidence certification under closed deterministic rails, or fail closed before certifying artifacts.

Original PR status: Not satisfied

After First Remedial PR: Not satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `tools/evidence/generate_hdapi_v2_live_conformance.py` | "def enforce\_closed\_rails()" | "env \= ensure\_determinism\_env()" | "raise SystemExit(f"HDAPI\_V2\_LIVE\_CONFORMANCE\_CLOSED\_RAILS\_REQUIRED:{exc}")"

GitHub Repo proof, if current state matters: Final generator enforces closed rails before `write_outputs(render_outputs(...), check=args.check)`.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Produce `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` and sibling path proof.

Original PR status: Not satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""generated\_at\_utc":"2026-06-28T08:36:03Z"" | GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"

GitHub Repo proof, if current state matters: Final artifact and path proof exist and are non-backdated.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Notes, optional: Original PR status is Not satisfied because original proof chronology was backdated.

Requirement: Produce `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` and sibling path proof.

Original PR status: Not satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | ""generated\_at\_utc":"2026-06-28T08:36:03Z"" | GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"

GitHub Repo proof, if current state matters: Final artifact and path proof exist and are non-backdated.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Notes, optional: Original PR status is Not satisfied because original proof chronology was backdated.

Requirement: Update Human Evidence Index rows in `docs/evidence/INDEX.json`.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl` | ""artifact\_key":"hdapi\_v2.error\_mapping"" | ""artifact\_key":"hdapi\_v2.rate\_limit\_headers"" | ""artifact\_key":"index.human\_index""

GitHub Repo proof, if current state matters: Final index proof shows `mtime_utc: 2026-06-28T08:36:04Z` and `produced_at_utc: 2026-06-28T08:36:04Z`.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Update Machine Mirror rows in `artifacts/evidence_index.jsonl`.

Original PR status: Not satisfied

After First Remedial PR: Not satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl` | ""artifact\_key":"hdapi\_v2.error\_mapping"" | ""artifact\_key":"hdapi\_v2.rate\_limit\_headers"" | GitHub Repo | `artifacts/evidence_index.jsonl.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"

GitHub Repo proof, if current state matters: Final Machine Mirror rows exist and Machine Mirror path proof is non-backdated.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Refresh `docs/evidence/INDEX.sha256` if `docs/evidence/INDEX.json` changes.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `docs/evidence/INDEX.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"

GitHub Repo proof, if current state matters: Human Index hash sentinel proof is coherent.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Refresh `artifacts/evidence_index.jsonl.sha256` if maintained by tooling.

Original PR status: Not satisfied

After First Remedial PR: Not satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"

GitHub Repo proof, if current state matters: Machine Mirror hash sentinel proof is coherent.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Add targeted tests for generator and evidence shape.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `tests/evidence/test_hdapi_v2_live_conformance.py` | "test\_generator\_rendered\_outputs\_are\_canonical\_and\_scoped" | "test\_error\_mapping\_artifact\_covers\_provider\_codes\_retry\_and\_observability" | "test\_rate\_limit\_artifact\_covers\_retry\_after\_forms"

GitHub Repo proof, if current state matters: Final test file contains targeted tests.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Add regression coverage for timestamp remediation.

Original PR status: Not applicable

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `tests/evidence/test_hdapi_v2_live_conformance.py` | "test\_live\_conformance\_evidence\_chronology\_is\_not\_backdated" | "test\_epic035\_index\_entries\_use\_payload\_timestamp\_not\_checkout\_mtime" | "test\_machine\_mirror\_path\_proofs\_are\_not\_backdated"

GitHub Repo proof, if current state matters: Final test file contains direct artifact and Machine Mirror chronology regression tests.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Add regression coverage for non-closed-rails generator refusal.

Original PR status: Not satisfied

After First Remedial PR: Not satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `tests/evidence/test_hdapi_v2_live_conformance.py` | "test\_generator\_refuses\_non\_closed\_rails\_without\_writing" | "test\_generator\_refuses\_network\_enabled\_check\_without\_certifying"

GitHub Repo proof, if current state matters: Final tests assert `HDAPI_V2_LIVE_CONFORMANCE_CLOSED_RAILS_REQUIRED` and unchanged artifact bytes/mtimes.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Do not introduce vendor-v2-specific acceptance token.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `tools/evidence/update_evidence_index.py` | PR-01 token lists include `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_PATH_PROOFS_OK`, `PF04_LOG_ALLOWLIST_009_OK`, `ERROR_TOKEN_MAP_OK`.

GitHub Repo proof, if current state matters: Search method: searched GitHub Repo for "vendor-v2-specific token" (case: insensitive); scope: PR-01 changed files and current PR-01 artifact rows; tool: manual scan via GitHub final-file inspection; result: 0 hits.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

Requirement: Do not execute live vendor calls or OPS in PR work.

Original PR status: Satisfied

After First Remedial PR: Satisfied

After Second Remedial PR: Satisfied

Final current status: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""live\_vendor\_call":"NONE"" | ""open\_rails\_ops\_execution":"NONE"" | GitHub Repo | `tools/evidence/generate_hdapi_v2_live_conformance.py` | `base_url="https://example.invalid/v2"` | `api_key="redacted"`

GitHub Repo proof, if current state matters: Final generator uses deterministic seam inputs and closed-rails enforcement; final snapshots preserve no-live-call / no-OPS claims.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.3

RCA

A) Bug/Failure statement

Original PR \#328 introduced valid PR-01 evidence content but failed evidence-integrity posture because direct artifact proofs were backdated and the generator could certify closed-rails evidence without enforcing closed rails. First Remedial PR \#329 fixed direct artifact chronology but left Machine Mirror proof chronology and rail-enforcement gaps. Second Remedial PR \#330 fixed both remaining gaps.

B) Root cause(s)

1. Original PR used a static generated timestamp for newly generated governed artifacts.  
   Evidence pointer(s): Original PR | diff for `tools/evidence/generate_hdapi_v2_live_conformance.py` | `PRODUCED_AT = "2026-06-28T00:00:00Z"` | generated artifact proofs later showed `mtime_utc` after `produced_at_utc`.  
   PF reference: PF04 — HDE-Governance, §2.0.6 Evidence & indexing  
2. Original PR declared closed-rails evidence posture but did not enforce `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC` before generator certification.  
   Evidence pointer(s): Original PR | PR \#328 review thread | "Require closed rails before emitting provider evidence" | "`SAFE_MODE=0 ALLOW_NETWORK=1 ... --check` exits 0"  
3. First Remedial PR narrowed timestamp correction to direct PR-01 artifacts and index rows but did not fully cover Machine Mirror proof companions.  
   Evidence pointer(s): First Remedial PR | PR \#329 review thread | "Avoid deriving index timestamps from checkout mtimes" | "`tools/evidence/update_evidence_index.py --check` ... `STALE:/workspace/glow-hdengine-v2/docs/evidence/INDEX.json`"

C) Fix across PRs

* Original PR added the generator, PR-01 evidence snapshots, path proofs, index/mirror bindings, and initial tests.  
* First Remedial PR replaced the static generated timestamp with dynamic UTC produced timestamps, preserved existing generated timestamps during check mode, aligned direct artifact mtimes, and added direct artifact chronology tests.  
* Second Remedial PR added `ensure_determinism_env()` / `enforce_closed_rails()` guard before certification, extended `NON_BACKDATED_PROOF_RELS` to PR-01 snapshots plus Machine Mirror and mirror-hash artifacts, regenerated governed evidence, and added tests for Machine Mirror proof chronology and non-closed-rails refusal.

D) Fix verification

* Current direct PR-01 path proofs are not backdated: both direct artifact proofs have matching `mtime_utc` and `produced_at_utc`.  
* Current Machine Mirror and mirror-hash proofs are not backdated: both have matching `mtime_utc` and `produced_at_utc`.  
* Current generator refuses non-closed-rails certification before rendering/checking/writing.  
* Second Remedial PR reports the full targeted validation set and current CI is green.

PF09 Impact & Status Posture

PF09.x document title: PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.4

PF09 task ID: HDE-FERM008

PF09 subtask ID(s): HDE-FERM008.3

Current PF09 status: Subtask status: Not done

Status recommendation: change to Done

Why supported: The net merged work now supplies the exact PF09.5 HDE-FERM008.3 evidence artifacts, maps v2 HTTP outcomes, error classes, Retry-After behavior, rate-limit behavior, malformed/bad-response handling, retryability, and secret-safe observability, and binds the artifacts through current non-backdated governed evidence index/mirror/path-proof posture. This recommendation applies only to HDE-FERM008.3, not the HDE-FERM008 parent and not HDE-FERM008.4 or HDE-FERM008.5.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | HDE-FERM008.3 metadata and provider outcome records; GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | HDE-FERM008.3 metadata and Retry-After records; GitHub Repo | `artifacts/evidence_index.jsonl` | `hdapi_v2.error_mapping` and `hdapi_v2.rate_limit_headers` rows; GitHub Repo | path proofs | non-backdated `mtime_utc` / `produced_at_utc`.

GitHub Repo proof, if repo state matters: Current `main` equals second remedial merge commit `bb0092398b50c54fea62da6cb825e3c845fbdf0b`; no later commits alter reviewed files.

PF proof excerpt(s):

PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.3 \- Map v2 error, retry, and rate-limit behavior

"Map v2 vendor HTTP outcomes, error envelope behavior, Retry-After behavior, ratelimit headers, and malformed-response handling into HDE typed errors. The mapping must avoid vendor payload echo, avoid secrets in logs, and preserve deterministic output."

"Subtask status: Not done"

"\* `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`

* `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`  
* `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt`"

PF04 — HDE-Governance, §2.0.6 Evidence & indexing

"No backdating. A record MUST NOT claim an earlier `produced_at_utc` or proof timestamp for an artifact whose bytes were created or modified later; that is treated as an integrity failure."

"Failure posture (merge-blocking). If these fields are stale or contradictory (for example, a changed artifact whose proof timestamps or mirror `produced_at_utc` imply a prior production context), the merge is blocked until corrected (see §2.0.5 and §9.7.0)."

Linked NET/Finding IDs: NET-007, NET-008, NET-009, NET-010, NET-001, NET-002, NET-003, NET-004, NET-030, NET-031, NET-032, NET-033, F-001, F-002, F-003

Findings

F-001

Related item: NET-007 / NET-009 / Crosswalk

Severity: Note

Observation: The final PR-01 snapshots cover the approved HDE-FERM008.3 provider outcome and rate-limit mapping scope.

Why it matters: This is the core Implementation Doc requirement for PR-01.

Evidence: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | provider code and retry records; GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | Retry-After and 429 records.

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.3; change to Done.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.3 \- Map v2 error, retry, and rate-limit behavior

F-002

Related item: NET-002 / NET-004 / NET-008 / NET-010 / VAL-007 / VAL-008

Severity: Note

Observation: The Original PR and First Remedial PR chronology gaps are closed in current GitHub Repo state.

Why it matters: Governed evidence can now support the reviewed PR-01 scope without the prior backdating defect.

Evidence: GitHub Repo | PR-01 artifact path proofs and Machine Mirror path proofs | matching `mtime_utc` and `produced_at_utc` values.

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.3; change to Done.

PF reference, if relied on: PF04 — HDE-Governance, §2.0.6 Evidence & indexing

F-003

Related item: NET-035 / VAL-009

Severity: Note

Observation: The generator now enforces closed deterministic rails before check/write certification.

Why it matters: The generated evidence claims closed-rails posture, and current code now validates that posture before certification.

Evidence: GitHub Repo | `tools/evidence/generate_hdapi_v2_live_conformance.py` | `enforce_closed_rails()` and `ensure_determinism_env()` call before `write_outputs(...)`.

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.3; change to Done.

PF reference, if relied on: None

F-004

Related item: NET-034 / VAL-010

Severity: Note

Observation: Regression coverage now includes direct artifact chronology, Machine Mirror chronology, and non-closed-rails refusal.

Why it matters: The two remediation defect classes are now covered by targeted tests.

Evidence: GitHub Repo | `tests/evidence/test_hdapi_v2_live_conformance.py` | `test_live_conformance_evidence_chronology_is_not_backdated`, `test_machine_mirror_path_proofs_are_not_backdated`, `test_generator_refuses_non_closed_rails_without_writing`, and `test_generator_refuses_network_enabled_check_without_certifying`.

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.3; change to Done.

PF reference, if relied on: None

F-005

Related item: PF09

Severity: Note

Observation: HDE-FERM008.3 is supportable for a PF09.5 status recommendation to Done, but HDE-FERM008 parent, HDE-FERM008.4, and HDE-FERM008.5 are not included in this PR’s status recommendation.

Why it matters: This prevents overclaiming the parent live-conformance sequence.

Evidence: GitHub Repo | PR-01 artifacts | HDE-FERM008.3 metadata only; PF09.5 | HDE-FERM008.4 and HDE-FERM008.5 remain separate subtasks.

Required action: PF09.5 status-drain candidate only for HDE-FERM008.3.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.3; change to Done.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.3 \- Map v2 error, retry, and rate-limit behavior

Evidence Print (PASS PROOF; merged work)

A) Acceptance coverage evidence

* Requirement covered: v2 provider outcome mapping.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""status\_mapping\_records"" | ""PROVIDER\_UNAUTHORIZED"" | ""PROVIDER\_RATE\_LIMITED"" | ""PROVIDER\_UNAVAILABLE"" | ""PROVIDER\_ERROR""  
  GitHub Repo proof: Final canonical snapshot exists and is indexed.  
* Requirement covered: retry classification.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""network\_error":true" | ""5xx":true" | ""429":false" | ""redirect\_response":false"  
  GitHub Repo proof: Final snapshot includes retry classification map.  
* Requirement covered: Retry-After / rate-limit evidence.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | ""parsed\_retry\_after\_ms":7000" | ""parsed\_retry\_after\_ms":5000" | ""parsed\_retry\_after\_ms":null"  
  GitHub Repo proof: Final snapshot includes delta, HTTP-date, invalid, and overflow cases.  
* Requirement covered: secret-safe and no-claim posture.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | ""no\_raw\_request\_body":true" | ""no\_raw\_response\_body":true" | ""no\_raw\_secret\_header":true" | ""live\_vendor\_call":"NONE""  
  GitHub Repo proof: Final snapshot includes observability and no-claim fields.

B) Original gaps closed

* Original direct path-proof backdating closed.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"; GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"  
  GitHub Repo proof: Final path proofs are non-backdated.  
* Original closed-rails enforcement gap closed.  
  Evidence pointer: GitHub Repo | `tools/evidence/generate_hdapi_v2_live_conformance.py` | "def enforce\_closed\_rails()" | "env \= ensure\_determinism\_env()" | "HDAPI\_V2\_LIVE\_CONFORMANCE\_CLOSED\_RAILS\_REQUIRED"  
  GitHub Repo proof: Final generator enforces closed rails before check/write certification.  
* Original orientation-demo drift closed.  
  Evidence pointer: Original PR | `audit/gates/topology/orientation_demo.txt` patch | "total\_artifacts: 390" | "total\_artifacts: 392"  
  GitHub Repo proof: Net compare retains the orientation demo update.

C) First remediation gaps closed or safely superseded

* Machine Mirror proof backdating closed.  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"  
  GitHub Repo proof: Final Machine Mirror proof is non-backdated.  
* Mirror-hash proof backdating closed.  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T08:36:04Z" | "produced\_at\_utc: 2026-06-28T08:36:04Z"  
  GitHub Repo proof: Final mirror-hash proof is non-backdated.  
* Checkout-mtime / proof chronology regression covered.  
  Evidence pointer: GitHub Repo | `tests/evidence/test_hdapi_v2_live_conformance.py` | "test\_epic035\_index\_entries\_use\_payload\_timestamp\_not\_checkout\_mtime" | "test\_machine\_mirror\_path\_proofs\_are\_not\_backdated"  
  GitHub Repo proof: Final tests include both regression cases.

D) Evidence and verification posture

* Human Evidence Index posture.  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | ""artifact\_key":"index.human\_index"" | ""produced\_at\_utc":"2026-06-28T08:36:04Z""  
  GitHub Repo proof: `docs/evidence/INDEX.json.path_proof.txt` has matching `mtime_utc` and `produced_at_utc`.  
* Machine Mirror posture.  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | ""artifact\_key":"index.machine\_mirror"" | ""sha256":"cedd3bb559bef29b93a2c710f4e307b9a6002997c489c15362e1dc5f0e28c4a3""  
  GitHub Repo proof: `artifacts/evidence_index.jsonl.path_proof.txt` includes matching `mirror_body_sha256` and non-backdated proof chronology.  
* Artifact path-proof posture.  
  Evidence pointer: GitHub Repo | PR-01 path proofs | "mtime\_utc: 2026-06-28T08:36:03Z" | "produced\_at\_utc: 2026-06-28T08:36:03Z"  
  GitHub Repo proof: Both PR-01 direct path proofs are present and non-backdated.

E) Token/gate evidence, only for explicitly claimed tokens/gates

* Token: `JSON_CANONICAL_CHECK_OK`  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | PR-01 rows list `"JSON_CANONICAL_CHECK_OK"` | tests assert canonical JSON bytes.  
  GitHub Repo proof: `tests/evidence/test_hdapi_v2_live_conformance.py` asserts one final LF, no BOM, sorted keys, and compact separators.  
* Token: `EVIDENCE_PATH_PROOFS_OK`  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | PR-01 rows list `"EVIDENCE_PATH_PROOFS_OK"` | path-proof files exist for both PR-01 artifacts.  
  GitHub Repo proof: Direct and mirror path proofs inspected and non-backdated.  
* Token: `PF04_LOG_ALLOWLIST_009_OK`  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | `hdapi_v2.error_mapping` row lists `"PF04_LOG_ALLOWLIST_009_OK"` | final snapshot includes bounded log keys only.  
  GitHub Repo proof: `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` includes `observed_log_keys` and no raw request/response/secret/vendor payload fields.  
* Token: `ERROR_TOKEN_MAP_OK`  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | PR-01 rows list `"ERROR_TOKEN_MAP_OK"` | final snapshots use governed provider-code values such as `PROVIDER_RATE_LIMITED`, `PROVIDER_BAD_RESPONSE`, and `PROVIDER_NETWORK_ERROR`.  
  GitHub Repo proof: Final snapshots include provider-code records.

F) Test/CI proof

* Original PR CI.  
  Evidence pointer: Original PR | workflow run | "name: ci" | "conclusion: success"  
* First Remedial PR CI.  
  Evidence pointer: First Remedial PR | workflow run | "name: ci" | "conclusion: success"  
* Second Remedial PR CI.  
  Evidence pointer: Second Remedial PR | workflow run | "name: ci" | "conclusion: success"  
* Second Remedial PR targeted validation.  
  Evidence pointer: Second Remedial PR | PR \#330 body | "`python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_live_conformance.py`" | "`python tools/evidence/generate_hdapi_v2_live_conformance.py --check`" | "`python tools/evidence/update_evidence_index.py --check`" | "`python tools/evidence/validate_evidence_paths.py`" | "`python ci/checks/check_mirror_schema.sh`" | "`bash ci/checks/check_evidence_index_hash.sh`" | "negative validation with `SAFE_MODE=0`"

G) Artifact and evidence outputs, including governed path/index/mirror/path-proof posture when relevant

* Path: `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`  
  Type: canonical JSON snapshot  
  Key proof facts observed: HDE-EPIC035, HDE-FERM008.3, status mapping, retry classification, bad-response/network-error records, no-claim posture.  
  Index/Mirror/path-proof posture: Indexed and mirrored under `hdapi_v2.error_mapping`; path proof non-backdated.  
* Path: `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt`  
  Type: path proof  
  Key proof facts observed: `mtime_utc: 2026-06-28T08:36:03Z`; `produced_at_utc: 2026-06-28T08:36:03Z`.  
  Index/Mirror/path-proof posture: Co-located companion proof.  
* Path: `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`  
  Type: canonical JSON snapshot  
  Key proof facts observed: HDE-EPIC035, HDE-FERM008.3, 429 non-retryable record, Retry-After delta/HTTP-date/invalid/overflow cases, no-claim posture.  
  Index/Mirror/path-proof posture: Indexed and mirrored under `hdapi_v2.rate_limit_headers`; path proof non-backdated.  
* Path: `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt`  
  Type: path proof  
  Key proof facts observed: `mtime_utc: 2026-06-28T08:36:03Z`; `produced_at_utc: 2026-06-28T08:36:03Z`.  
  Index/Mirror/path-proof posture: Co-located companion proof.  
* Path: `docs/evidence/INDEX.json`  
  Type: Human Evidence Index  
  Key proof facts observed: PR-01 artifact rows present through evidence-index / mirror inspection.  
  Index/Mirror/path-proof posture: Companion proof and hash sentinel updated.  
* Path: `artifacts/evidence_index.jsonl`  
  Type: Machine Mirror  
  Key proof facts observed: `hdapi_v2.error_mapping`, `hdapi_v2.rate_limit_headers`, and `index.machine_mirror` rows present; `index.machine_mirror` sha matches the current mirror body.  
  Index/Mirror/path-proof posture: Companion proof and hash sentinel updated.

Doc Delta Candidates (PF-Canon only)

DDC-001

Doc: PF09.5 — HDE Build Checklist Fermentation

Section: §Subtask HDE-FERM008.3 \- Map v2 error, retry, and rate-limit behavior

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task/subtask IDs: HDE-FERM008 / HDE-FERM008.3

PF09 status action: change to Done

Delta: Update HDE-FERM008.3 status from `Not done` to `Done`, preserving the subtask scope as v2 error, retry, and rate-limit behavior only. Do not update HDE-FERM008 parent, HDE-FERM008.4, or HDE-FERM008.5 from this PR-01 evidence.

Why: Current GitHub Repo evidence now contains the required HDE-FERM008.3 artifacts, non-backdated path proofs, Human Index / Machine Mirror bindings, closed-rails generator enforcement, and targeted regression coverage.

Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` | HDE-FERM008.3 provider outcome mapping; GitHub Repo | `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` | HDE-FERM008.3 Retry-After / 429 mapping; GitHub Repo | `artifacts/evidence_index.jsonl` | indexed and mirrored PR-01 artifacts.

GitHub Repo proof, if repo state matters: Current `main` equals second remedial merge commit `bb0092398b50c54fea62da6cb825e3c845fbdf0b`; direct artifact, Human Index, Machine Mirror, and hash path proofs inspected and non-backdated.

Canon proof excerpt, unless Canon basis is CANON SILENCE:

"\#\#\# **Subtask HDE-FERM008.3 \- Map v2 error, retry, and rate-limit behavior**"

"Map v2 vendor HTTP outcomes, error envelope behavior, Retry-After behavior, ratelimit headers, and malformed-response handling into HDE typed errors. The mapping must avoid vendor payload echo, avoid secrets in logs, and preserve deterministic output."

"Subtask status: Not done"

"\* `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`

* `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`  
* `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt`"

DECISION: MERGED WORK ACCEPTABLE

## 2.2) PR-02 HDE-EPIC035

Review Summary

* Original PR \#331 added HDE-EPIC035 PR-02 response-normalization evidence for PF09.5 / HDE-FERM008 / HDE-FERM008.4, including a new generator, promoted `response_mapping.snapshot.json`, new `release_binding.snapshot.json`, tests, and evidence-index / mirror bindings.  
* Original PR \#331 aligned with the Approved Plan’s core PR-02 posture by recording an exact schema/adapter gap rather than claiming a normalized data path or full HumanDesignAPI v2 runtime conformance.  
* Original PR \#331 left material evidence-indexing gaps: the shared `response_mapping.snapshot.json` path created conflicting EPIC034 / EPIC035 index semantics, and the first attempted fix removed the distinct EPIC034 PR-03 response-mapping check-log row.  
* Remedial PR \#332 fixed those gaps by preserving the EPIC034 check-log row, skipping only the promoted shared snapshot row, validating PR-02 snapshot identity, validating release-binding SHA linkage, and failing closed on HDAPI v2 route/schema drift.  
* Current GitHub Repo state equals the Remedial PR merge commit `7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d`; no later commits affect the reviewed files.  
* Current evidence posture is supportable: PR-02 artifacts exist, path proofs are non-backdated, Human Index / Machine Mirror entries are present, the EPIC034 check log remains indexed, and tests cover the original PR bug.  
* Visible CI for both PR heads completed successfully, and reported targeted validation covers generator check, evidence-index check, path validation, mirror schema, hash check in the Original PR, and remedial regression tests.  
* PF09 impact is limited to PF09.5 / HDE-FERM008 / HDE-FERM008.4. The reviewed evidence supports a status recommendation to change HDE-FERM008.4 to Done, without claiming HDE-FERM008 parent completion or HDE-FERM008.5 closure.

GitHub / Repo Inspection

Repository identity:

* GitHub Repo | repo metadata | "repository\_full\_name: amthorn78/glow-hdengine-v2" | "default\_branch: main"

Reviewed branch/default branch:

* GitHub Repo | repo metadata | "default\_branch: main"

Current HEAD:

* GitHub Repo | compare `7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d..main` | "status: identical" | "total\_commits: 0"

Original PR merged state and merge identifier:

* Original PR | PR \#331 metadata | "state: closed" | "merged: true" | "merge\_commit\_sha: 37f06dc021709d535b28814f69f7289a9d555c0d"

Remedial PR merged state and merge identifier:

* Remedial PR | PR \#332 metadata | "state: closed" | "merged: true" | "merge\_commit\_sha: 7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d"

Original PR changed files:

* Original PR | PR \#331 metadata / changed-file list | "changed\_files: 37" | material files included `tools/evidence/generate_hdapi_v2_response_normalization.py`, `tests/evidence/test_hdapi_v2_response_normalization.py`, `tools/evidence/update_evidence_index.py`, PR-02 response-mapping / release-binding artifacts, Human Index, Machine Mirror, hash sentinels, and path proofs.

Remedial PR changed files:

* Remedial PR | PR \#332 metadata / changed-file list | "changed\_files: 33" | material files included `tools/evidence/generate_hdapi_v2_response_normalization.py`, `tests/evidence/test_hdapi_v2_response_normalization.py`, `tools/evidence/update_evidence_index.py`, Human Index, Machine Mirror, hash sentinels, orientation demo, and path proofs.

Net touched files:

* GitHub Repo | compare `bb0092398b50c54fea62da6cb825e3c845fbdf0b..main` | "ahead\_by: 2" | "files: 38"

Current final file state inspected:

* GitHub Repo | final file inspection | `tools/evidence/generate_hdapi_v2_response_normalization.py` complete file inspected.  
* GitHub Repo | final file inspection | `tools/evidence/update_evidence_index.py` EPIC034 PR-03 and EPIC035 PR-02 loader logic inspected.  
* GitHub Repo | final file inspection | `tests/evidence/test_hdapi_v2_response_normalization.py` complete current file inspected.  
* GitHub Repo | final file inspection | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` and `.path_proof.txt` inspected.  
* GitHub Repo | final file inspection | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` and `.path_proof.txt` inspected.  
* GitHub Repo | final file inspection | `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.path_proof.txt`, `artifacts/evidence_index.jsonl.sha256`, and `artifacts/evidence_index.jsonl.sha256.path_proof.txt` inspected.  
* GitHub Repo | final file inspection | `docs/evidence/INDEX.json.path_proof.txt` and `docs/evidence/INDEX.sha256.path_proof.txt` inspected.

Checks/CI inspected:

* Original PR | workflow runs for head `5f02dcc18beb27c889884be9617b707b325c6044` | "name: ci" | "conclusion: success"  
* Remedial PR | workflow runs for head `8b9dfcc7b462cdd53fcdcdddd21d16bf936f5814` | "name: ci" | "conclusion: success"

Governed evidence inspected:

* GitHub Repo | final evidence inspection | PR-02 response-mapping snapshot, release-binding snapshot, path proofs, Human Index proof, Human Index hash proof, Machine Mirror rows, Machine Mirror proof, Machine Mirror hash sentinel, Machine Mirror hash proof, EPIC034 PR-03 check-log row retention.

Later commits affecting touched files:

* GitHub Repo | compare `7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d..main` | "status: identical" | "files: \[\]"

Provenance (Original \-\> Remediation)

* Claim: Original PR intended to implement HDE-FERM008.4 response-normalization evidence.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#331 body | "Record HDE-FERM008.4 evidence that either proves v2 ChartResult/ChartSimpleResult can feed existing HDE BodyGraph/cache/compat boundaries or, if not, capture the exact adapter/schema gap without inference." | "Bind the new PR-02 evidence to the already-landed PR-01 provider-outcome artifacts"  
* Claim: Original PR added a closed-rails response-normalization generator and release binding.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#331 body | "Added a closed-rails evidence generator `tools/evidence/generate_hdapi_v2_response_normalization.py`" | "Created `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`"  
* Claim: Original PR explicitly chose exact gap posture, not normalized-data-path proof.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#331 body | "records an exact adapter/schema gap" | "normalized-data-path proof claim remains `NONE`"  
* Claim: Extra Evidence corroborates Original PR implementation, validation, and the review finding that triggered remediation.  
  Source: Extra Evidence  
  Evidence pointer: Extra Evidence | PR-02 artifact summary | "Fixed the stale EPIC034 binding by gating \_load\_epic034\_pr03\_entries() when the reused artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json has been promoted to HDE-EPIC035 / HDE-FERM008.4" | "Added regression coverage proving INDEX/Mirror no longer retain the conflicting EPIC034 response-mapping row and do retain the HDE-EPIC035 PR-02 row."  
* Claim: Original PR had a stale EPIC034 binding bug for the reused response-mapping snapshot path.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#331 review comment | "Registering PR-02 at `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` reuses the same path" | "generated INDEX/Mirror now contain two rows for the same SHA/path with conflicting epic IDs and record types"  
* Claim: Original PR had a second indexing bug after the first attempted fix: the distinct EPIC034 PR-03 response-mapping check log was dropped.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#331 review comment | "this early return drops every EPIC034 PR-03 entry, not just the reused `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` row" | "`audit/qa/hde-epic034/pr-03/response_mapping_check.log` still exists with a path proof but no longer has any index/mirror row"  
* Claim: Original PR needed fail-closed validation that the shared snapshot and release binding still represented EPIC035 PR-02.  
  Source: Original PR  
  Evidence pointer: Original PR | PR \#331 review comment | "This loader emits HDE-EPIC035 PR-02 rows whenever both files exist, but it never verifies that the shared `response_mapping.snapshot.json` is still the EPIC035/HDE-FERM008.4 payload" | "Fail closed unless the snapshot identity and release binding reference match."  
* Claim: Remedial PR fixed the stale EPIC034 / EPIC035 index collision while preserving the EPIC034 check log.  
  Source: Remedial PR  
  Evidence pointer: Remedial PR | PR \#332 body | "skip only the promoted snapshot row" | "preserving `audit/qa/hde-epic034/pr-03/response_mapping_check.log` and other distinct EPIC034 entries"  
* Claim: Remedial PR added strict PR-02 snapshot identity and release-binding SHA checks.  
  Source: Remedial PR  
  Evidence pointer: Remedial PR | PR \#332 body | "Added strict identity and release-binding validation in `_load_epic035_pr02_entries()`" | "failing with a clear `SystemExit` if checks fail"  
* Claim: Remedial PR hardened route/schema drift handling.  
  Source: Remedial PR  
  Evidence pointer: Remedial PR | PR \#332 body | "replacing substring inference with explicit route requirements" | "raising `ValueError` on drift"  
* Claim: Current GitHub Repo confirms the EPIC034 check-log row is retained and the conflicting EPIC034 shared snapshot row is absent from final Machine Mirror posture.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | `"artifact_key":"hdapi_v2.response_mapping_pr02"` | `"discovered_physical_path":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"` | `"epic_id":"HDE-EPIC035"`  
* Claim: Current GitHub Repo confirms PR-02 artifacts are non-backdated and bound.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T09:27:28Z" | "produced\_at\_utc: 2026-06-28T09:27:28Z"; GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T09:27:28Z" | "produced\_at\_utc: 2026-06-28T09:27:28Z"  
* Claim: Current GitHub Repo confirms no later commits changed the reviewed state.  
  Source: GitHub Repo  
  Evidence pointer: GitHub Repo | compare `7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d..main` | "status: identical" | "total\_commits: 0"

Net Effective Diff Review

NET ID: NET-001

File/artifact: `artifacts/evidence_index.jsonl`

Covered hunks: OPR-001 / RPR-001

Final repo state: Contains PR-02 `hdapi_v2.response_mapping_pr02` and `hdapi_v2.release_binding` rows, preserves PR-01 rows, and retains governed index self-records.

Risk: High

Assessment: Final Machine Mirror state is acceptable for reviewed PR-02 scope. The Remedial PR corrected the conflicting EPIC034 shared-snapshot binding while preserving distinct EPIC034 evidence rows.

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl` | `"artifact_key":"hdapi_v2.response_mapping_pr02"` | `"artifact_key":"hdapi_v2.release_binding"` | `"produced_at_utc":"2026-06-28T09:27:28Z"`

GitHub Repo proof: GitHub Repo | final file inspection | `artifacts/evidence_index.jsonl` includes PR-02 artifact rows and index self-records.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-002

File/artifact: `artifacts/evidence_index.jsonl.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Machine Mirror path proof exists with `mtime_utc: 2026-06-28T10:17:56Z` and `produced_at_utc: 2026-06-28T10:17:56Z`.

Risk: High

Assessment: Coherent and non-backdated.

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl.path_proof.txt` | "mtime\_utc: 2026-06-28T10:17:56Z" | "produced\_at\_utc: 2026-06-28T10:17:56Z"

GitHub Repo proof: GitHub Repo | final path proof inspection | `path: artifacts/evidence_index.jsonl`, `mirror_body_sha256: 2c61fb329fc0ca0aee2f7bf5d71436bb833d10308292fb730f8005a873d55bff`.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-003

File/artifact: `artifacts/evidence_index.jsonl.sha256`

Covered hunks: OPR-001 / RPR-001

Final repo state: Machine Mirror hash sentinel refreshed.

Risk: Medium

Assessment: Expected companion update for changed Machine Mirror.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/evidence_index.jsonl.sha256`" | "status: modified"

GitHub Repo proof: GitHub Repo | changed-file list / net compare | `artifacts/evidence_index.jsonl.sha256` modified.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-004

File/artifact: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Machine Mirror hash sentinel path proof exists with `mtime_utc: 2026-06-28T10:17:56Z` and `produced_at_utc: 2026-06-28T10:17:56Z`.

Risk: High

Assessment: Coherent and non-backdated.

Evidence pointer(s): GitHub Repo | `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T10:17:56Z" | "produced\_at\_utc: 2026-06-28T10:17:56Z"

GitHub Repo proof: GitHub Repo | final path proof inspection | `path: artifacts/evidence_index.jsonl.sha256`.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-005

File/artifact: `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No PR-02 scope drift or independent defect identified.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/narratives/router/cli_http_parity.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-006

File/artifact: `artifacts/narratives/router/parity_abba.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing path-proof companion refreshed as evidence-updater convergence.

Risk: Low

Assessment: No PR-02 scope drift or independent defect identified.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/narratives/router/parity_abba.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-007

File/artifact: `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`

Covered hunks: OPR-001 / RPR-001

Final repo state: New canonical JSON release-binding snapshot exists with HDE-EPIC035 metadata, PR-01 evidence bindings, PR-02 response-normalization gap binding, HDE-FERM008.5 follow-up nonclaim, no public Reader / AI / live-vendor / full-conformance claims, and SHA linkage to `response_mapping.snapshot.json`.

Risk: High

Assessment: Matches Approved Plan PR-02 requirement and current remedial identity-validation posture.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` | `"artifact_kind":"hdapi_v2_release_binding"` | `"subtask_id":"HDE-FERM008.4"` | `"posture":"FOLLOW_UP_NOT_CLAIMED_BY_PR02"`

GitHub Repo proof: GitHub Repo | final file inspection | release binding references PR-01 artifacts and PR-02 response-mapping artifact with matching SHA.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows

NET ID: NET-008

File/artifact: `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: New path proof exists with `sha256: b8b8e88f016374fba7c9ce13b1c63394c280889a1826e7c1ec011a7c7fe69c82`, `mtime_utc: 2026-06-28T09:27:28Z`, and `produced_at_utc: 2026-06-28T09:27:28Z`.

Risk: High

Assessment: Required path proof is present and coherent.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T09:27:28Z" | "produced\_at\_utc: 2026-06-28T09:27:28Z"

GitHub Repo proof: GitHub Repo | final path proof inspection | path, size, sha256, mtime, produced fields observed.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-009

File/artifact: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

Covered hunks: OPR-001 / RPR-001

Final repo state: Promoted / refreshed response-mapping snapshot exists as HDE-EPIC035 HDE-FERM008.4 evidence recording exact schema/adapter gap and `normalized_data_path_proof_claim:"NONE"`.

Risk: High

Assessment: Matches Approved Plan: records exact adapter/schema gap without inference and avoids false compatibility claims.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"artifact_kind":"hdapi_v2_response_normalization_gap"` | `"pf09_subtask_id":"HDE-FERM008.4"` | `"schema_gap_status":"GAP_RECORDED"` | `"normalized_data_path_proof_claim":"NONE"`

GitHub Repo proof: GitHub Repo | final snapshot inspection | internal loci, route family identity, no-claim posture, and exact gap basis observed.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows

NET ID: NET-010

File/artifact: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Path proof exists with `sha256: b7ee708ad8a3b35c4b402d9304040ce55498c783a356c08ea3613c017b8a7a23`, `mtime_utc: 2026-06-28T09:27:28Z`, and `produced_at_utc: 2026-06-28T09:27:28Z`.

Risk: High

Assessment: Required path proof is present and coherent.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T09:27:28Z" | "produced\_at\_utc: 2026-06-28T09:27:28Z"

GitHub Repo proof: GitHub Repo | final path proof inspection | path, size, sha256, mtime, produced fields observed.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-011

File/artifact: `artifacts/writer/conjunction_write_readback.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing writer evidence path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect only; no PR-02 product-scope drift found.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/writer/conjunction_write_readback.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-012

File/artifact: `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing writer evidence path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect only; no PR-02 product-scope drift found.

Evidence pointer(s): GitHub Repo | net compare | "`artifacts/writer/conjunction_writer_summary.json.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-013

File/artifact: `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing doc-delta path-proof companion refreshed.

Risk: Low

Assessment: Documentation-drainage companion only; no execution or acceptance blocker.

Evidence pointer(s): GitHub Repo | net compare | "`audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-014

File/artifact: `audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing doc-delta path-proof companion refreshed.

Risk: Low

Assessment: Documentation-drainage companion only; no execution or acceptance blocker.

Evidence pointer(s): GitHub Repo | net compare | "`audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-015

File/artifact: `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing narrative evidence path-proof companion refreshed.

Risk: Low

Assessment: No independent PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/gates/narratives/keys_10x4.table.json.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-016

File/artifact: `audit/gates/narratives/pack_identity.txt.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing narrative evidence path-proof companion refreshed.

Risk: Low

Assessment: No independent PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/gates/narratives/pack_identity.txt.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-017

File/artifact: `audit/gates/narratives/registry.diff.json.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing narrative evidence path-proof companion refreshed.

Risk: Low

Assessment: No independent PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/gates/narratives/registry.diff.json.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-018

File/artifact: `audit/gates/topology/orientation_demo.txt`

Covered hunks: RPR-001

Final repo state: Orientation demo count updated by remedial evidence refresh.

Risk: Medium

Assessment: Expected evidence-topology companion update after index/mirror changes; no product behavior drift identified.

Evidence pointer(s): GitHub Repo | Remedial PR changed-file list | "`audit/gates/topology/orientation_demo.txt`" | "changed\_files: 33"

GitHub Repo proof: GitHub Repo | net compare | file listed as modified.

PF reference, if relied on: None

NET ID: NET-019

File/artifact: `audit/gates/topology/orientation_demo.txt.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Orientation demo path-proof companion refreshed.

Risk: Low

Assessment: Expected companion update.

Evidence pointer(s): GitHub Repo | net compare | "`audit/gates/topology/orientation_demo.txt.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-020

File/artifact: `audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-021

File/artifact: `audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-022

File/artifact: `audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-023

File/artifact: `audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-024

File/artifact: `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-025

File/artifact: `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-026

File/artifact: `audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-027

File/artifact: `audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-028

File/artifact: `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC030 path-proof companion refreshed.

Risk: Low

Assessment: Updater convergence side effect; no PR-02 defect found.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-029

File/artifact: `audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing doc-delta path-proof companion refreshed.

Risk: Low

Assessment: Documentation-drainage companion only; no execution or acceptance blocker.

Evidence pointer(s): GitHub Repo | net compare | "`audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: None

NET ID: NET-030

File/artifact: `audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Existing EPIC034 PR-03 check-log path proof refreshed and its evidence row is preserved by remedial logic.

Risk: High

Assessment: Remedial PR closed the review finding that had dropped the check-log row.

Evidence pointer(s): Remedial PR | PR \#332 body | "preserving `audit/qa/hde-epic034/pr-03/response_mapping_check.log` and other distinct EPIC034 entries" | GitHub Repo | `tools/evidence/update_evidence_index.py` | `shared_snapshot_promoted` skips only the shared snapshot row.

GitHub Repo proof: GitHub Repo | final `tools/evidence/update_evidence_index.py` | `_load_epic034_pr03_entries()` skips only when `entry.get("discovered_physical_path") == snapshot.relative_to(ROOT).as_posix()`.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-031

File/artifact: `docs/evidence/INDEX.json`

Covered hunks: OPR-001 / RPR-001

Final repo state: Human Evidence Index updated for PR-02 artifacts and related proof family.

Risk: High

Assessment: Required same-PR Human Index binding is present; current proof is coherent.

Evidence pointer(s): GitHub Repo | `docs/evidence/INDEX.json.path_proof.txt` | "sha256: 769aecff85b305fa2c4966a73472fcc1e69562464e683a9c5304b22be0240ecf" | "produced\_at\_utc: 2026-06-28T10:17:56Z"

GitHub Repo proof: GitHub Repo | Human Index path proof and Machine Mirror rows inspected.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-032

File/artifact: `docs/evidence/INDEX.json.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Human Evidence Index path proof exists and is not backdated.

Risk: High

Assessment: Required path proof is coherent.

Evidence pointer(s): GitHub Repo | `docs/evidence/INDEX.json.path_proof.txt` | "mtime\_utc: 2026-06-28T10:17:47Z" | "produced\_at\_utc: 2026-06-28T10:17:56Z"

GitHub Repo proof: GitHub Repo | final path proof inspection | path, size, sha256, mtime, produced fields observed.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-033

File/artifact: `docs/evidence/INDEX.sha256`

Covered hunks: OPR-001 / RPR-001

Final repo state: Human Evidence Index hash sentinel refreshed.

Risk: Medium

Assessment: Expected companion update.

Evidence pointer(s): GitHub Repo | net compare | "`docs/evidence/INDEX.sha256`" | "status: modified"

GitHub Repo proof: GitHub Repo | compare net files | file listed as modified.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-034

File/artifact: `docs/evidence/INDEX.sha256.path_proof.txt`

Covered hunks: OPR-001 / RPR-001

Final repo state: Human Evidence Index hash sentinel path proof exists and is not backdated.

Risk: High

Assessment: Required path proof is coherent.

Evidence pointer(s): GitHub Repo | `docs/evidence/INDEX.sha256.path_proof.txt` | "mtime\_utc: 2026-06-28T10:17:47Z" | "produced\_at\_utc: 2026-06-28T10:17:56Z"

GitHub Repo proof: GitHub Repo | final path proof inspection | path, size, sha256, mtime, produced fields observed.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

NET ID: NET-035

File/artifact: `tests/evidence/test_hdapi_v2_contract_inventory.py`

Covered hunks: OPR-002 / None

Final repo state: Existing contract-inventory tests were adapted to coexist with the promoted PR-02 response-mapping posture.

Risk: Medium

Assessment: Acceptable; it prevents old EPIC034-only assertions from falsely rejecting the promoted current artifact.

Evidence pointer(s): Extra Evidence | file list / summary | "Updated existing contract-inventory evidence tests so the shared response\_mapping.snapshot.json can remain compatible with prior EPIC034 boundary analyzers while also carrying the promoted PR-02 gap posture."

GitHub Repo proof: GitHub Repo | PR \#331 changed-file list | `tests/evidence/test_hdapi_v2_contract_inventory.py` modified.

PF reference, if relied on: None

NET ID: NET-036

File/artifact: `tests/evidence/test_hdapi_v2_response_normalization.py`

Covered hunks: OPR-002 / RPR-002

Final repo state: New PR-02 tests cover canonical JSON, HDE-EPIC035 / HDE-FERM008.4 metadata, exact schema/adapter gap posture, route/schema drift fail-closed behavior, release-binding SHA drift, EPIC034 check-log retention, and index/mirror/path-proof binding.

Risk: High

Assessment: Test coverage is adequate for the reviewed PR-02 evidence and remediation gaps.

Evidence pointer(s): GitHub Repo | `tests/evidence/test_hdapi_v2_response_normalization.py` | `test_route_rows_fail_closed_on_required_schema_drift` | `test_index_retains_epic034_pr03_check_log_when_pr02_snapshot_is_promoted` | `test_pr02_loader_fails_closed_on_release_binding_sha_drift`

GitHub Repo proof: GitHub Repo | final test file inspection and PR \#332 patch | regression tests observed.

PF reference, if relied on: None

NET ID: NET-037

File/artifact: `tools/evidence/generate_hdapi_v2_response_normalization.py`

Covered hunks: OPR-001 / RPR-001

Final repo state: New generator renders PR-02 canonical JSON response-normalization gap evidence, enforces closed rails, validates required v2 route schemas and envelope fields, and writes / checks `response_mapping.snapshot.json` and `release_binding.snapshot.json`.

Risk: High

Assessment: Matches Approved Plan and remedial hardening. It records the exact schema/adapter gap without adding runtime behavior, public surface changes, live calls, or AI scope.

Evidence pointer(s): GitHub Repo | `tools/evidence/generate_hdapi_v2_response_normalization.py` | `REQUIRED_ROUTE_SCHEMAS` | `HDAPI_V2_RESPONSE_NORMALIZATION_ROUTE_MISSING` | `HDAPI_V2_RESPONSE_NORMALIZATION_ENVELOPE_DRIFT` | `HDAPI_V2_RESPONSE_NORMALIZATION_CLOSED_RAILS_REQUIRED`

GitHub Repo proof: GitHub Repo | final generator inspection | closed-rails enforcement, explicit route-schema checks, response mapping builder, and release-binding builder observed.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows

NET ID: NET-038

File/artifact: `tools/evidence/update_evidence_index.py`

Covered hunks: OPR-001 / RPR-001

Final repo state: Evidence-index loader includes PR-02 entries, validates PR-02 snapshot identity, validates release-binding SHA reference, skips only the promoted shared EPIC034 snapshot row, and preserves distinct EPIC034 PR-03 evidence.

Risk: High

Assessment: Remedial PR closed the material Original PR indexing defects.

Evidence pointer(s): GitHub Repo | `tools/evidence/update_evidence_index.py` | `_load_epic034_pr03_entries()` | `_load_epic035_pr02_entries()` | `INVALID_EPIC035_RESPONSE_MAPPING_IDENTITY` | `INVALID_EPIC035_RELEASE_BINDING_RESPONSE_REFERENCE`

GitHub Repo proof: GitHub Repo | final updater inspection | loader and guards observed.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

Validation & Evidence Review

VAL-001

Purpose: Prove both PRs are merged.

Source: GitHub Repo

Check/workflow/artifact/method: GitHub PR metadata inspection.

Result: PASS

Observation: PR \#331 and PR \#332 are both `state: closed` and `merged: true`.

Evidence pointer: Original PR | PR \#331 metadata | "merged: true" | "merge\_commit\_sha: 37f06dc021709d535b28814f69f7289a9d555c0d"; Remedial PR | PR \#332 metadata | "merged: true" | "merge\_commit\_sha: 7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d"

Why it matters: Establishes the two-attempt lifecycle and exact merged sources.

VAL-002

Purpose: Prove current GitHub Repo state equals the remedial merge state.

Source: GitHub Repo

Check/workflow/artifact/method: Compare `7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d..main`.

Result: PASS

Observation: Compare returned `status: identical`, `ahead_by: 0`, `behind_by: 0`, and `total_commits: 0`.

Evidence pointer: GitHub Repo | compare `7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d..main` | "status: identical" | "total\_commits: 0"

Why it matters: No later changes need to be separated from the reviewed lifecycle.

VAL-003

Purpose: Prove net changed file set.

Source: GitHub Repo

Check/workflow/artifact/method: Compare `bb0092398b50c54fea62da6cb825e3c845fbdf0b..main`.

Result: PASS

Observation: Net compare shows 38 files and 2 commits ahead.

Evidence pointer: GitHub Repo | compare `bb0092398b50c54fea62da6cb825e3c845fbdf0b..main` | "ahead\_by: 2" | "files: 38"

Why it matters: Establishes net effective change set.

VAL-004

Purpose: Verify Original PR CI.

Source: Original PR

Check/workflow/artifact/method: Workflow run for head `5f02dcc18beb27c889884be9617b707b325c6044`.

Result: PASS

Observation: CI completed successfully.

Evidence pointer: Original PR | workflow runs | "name: ci" | "conclusion: success"

Why it matters: Confirms visible CI state for attempt 0\.

VAL-005

Purpose: Verify Remedial PR CI.

Source: Remedial PR

Check/workflow/artifact/method: Workflow run for head `8b9dfcc7b462cdd53fcdcdddd21d16bf936f5814`.

Result: PASS

Observation: CI completed successfully.

Evidence pointer: Remedial PR | workflow runs | "name: ci" | "conclusion: success"

Why it matters: Confirms visible CI state for remediation.

VAL-006

Purpose: Verify PR-02 generator validation.

Source: Original PR / Remedial PR

Check/workflow/artifact/method: Reported generator commands and current code inspection.

Result: PASS

Observation: Original PR reports generator update and `--check`; Remedial PR adds strict route/schema drift and release-binding guards.

Evidence pointer: Original PR | PR \#331 body | "`python tools/evidence/generate_hdapi_v2_response_normalization.py`" | "`--check`"; Remedial PR | PR \#332 body | "replacing substring inference with explicit route requirements" | "raising `ValueError` on drift"

Why it matters: Confirms generator is exercised and hardened.

VAL-007

Purpose: Verify direct PR-02 artifact proof chronology.

Source: GitHub Repo

Check/workflow/artifact/method: Current path-proof inspection.

Result: PASS

Observation: `response_mapping.snapshot.json.path_proof.txt` and `release_binding.snapshot.json.path_proof.txt` both have matching `mtime_utc` and `produced_at_utc`.

Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T09:27:28Z" | "produced\_at\_utc: 2026-06-28T09:27:28Z"; GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt` | "mtime\_utc: 2026-06-28T09:27:28Z" | "produced\_at\_utc: 2026-06-28T09:27:28Z"

Why it matters: Confirms governed PR-02 artifacts are not backdated.

VAL-008

Purpose: Verify Human Index and Machine Mirror proof posture.

Source: GitHub Repo

Check/workflow/artifact/method: Current proof inspection.

Result: PASS

Observation: Human Index and Machine Mirror proofs are present and not backdated.

Evidence pointer: GitHub Repo | `docs/evidence/INDEX.json.path_proof.txt` | "mtime\_utc: 2026-06-28T10:17:47Z" | "produced\_at\_utc: 2026-06-28T10:17:56Z"; GitHub Repo | `artifacts/evidence_index.jsonl.path_proof.txt` | "mtime\_utc: 2026-06-28T10:17:56Z" | "produced\_at\_utc: 2026-06-28T10:17:56Z"

Why it matters: Confirms same-PR evidence binding posture is currently coherent.

VAL-009

Purpose: Verify Original PR review gap was remediated.

Source: GitHub Repo / Remedial PR

Check/workflow/artifact/method: Review comments and final updater/test inspection.

Result: PASS

Observation: Remedial PR keeps EPIC034 PR-03 check log indexed, validates EPIC035 PR-02 snapshot identity, validates release-binding SHA, and fails closed on route/schema drift.

Evidence pointer: Remedial PR | PR \#332 body | "skip only the promoted snapshot row" | "strict identity and release-binding validation" | GitHub Repo | `tests/evidence/test_hdapi_v2_response_normalization.py` | `test_index_retains_epic034_pr03_check_log_when_pr02_snapshot_is_promoted`

Why it matters: Closes the known Original PR evidence-indexing blockers.

VAL-010

Purpose: Verify reported scoped validation.

Source: Original PR / Remedial PR / Extra Evidence

Check/workflow/artifact/method: PR body testing sections and Extra Evidence testing report.

Result: PASS

Observation: Original PR reports 312 passing tests plus generator, update index, path validation, mirror schema, and hash checks; Remedial PR reports 9 passing targeted tests, update index, orientation demo, and mirror schema; Extra Evidence reports the remedial suite as 313 passed plus update-index, path-validation, mirror-schema, and hash checks.

Evidence pointer: Original PR | PR \#331 body | "312 passed" | "`bash ci/checks/check_evidence_index_hash.sh`"; Remedial PR | PR \#332 body | "9 passed" | "`ci/checks/check_mirror_schema.sh`"; Extra Evidence | Testing | "313 passed" | "`bash ci/checks/check_evidence_index_hash.sh`"

Why it matters: Supports validation sufficiency beyond CI alone.

Requirement Satisfaction Crosswalk

Requirement: Produce governed HDE-FERM008.4 evidence that proves normalized v2 response flow or records exact adapter/schema gap without inference.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"response_normalization_posture":"EXACT_SCHEMA_ADAPTER_GAP_RECORDED"` | `"schema_gap_status":"GAP_RECORDED"` | `"no_compatibility_by_inference":true`

GitHub Repo proof, if current state matters: Final snapshot records exact bodygraph/cache/compat/admin gap basis and no normalized-data-path proof claim.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Notes, optional: Gap posture is acceptable because PF09.5 explicitly allows recording the schema gap when v2 response cannot truthfully feed the cache.

Requirement: Preserve no public Reader change, no public route/flag/payload/transport change, no new HTTP home, no app-side HDAPI path, no AI scope, no raw payload persistence, and no full v2 runtime conformance claim.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"full_hdapi_v2_runtime_conformance":"NONE"` | `"public_reader_change":"NONE"` | `"app_side_humandesignapi_call_path":"NONE"` | `"raw_vendor_payload_persisted":"NONE"`

GitHub Repo proof, if current state matters: Final response-mapping and release-binding artifacts preserve nonclaim posture.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Produce `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` and sibling path proof.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"pf09_subtask_id":"HDE-FERM008.4"` | GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt` | "sha256: b7ee708ad8a3b35c4b402d9304040ce55498c783a356c08ea3613c017b8a7a23"

GitHub Repo proof, if current state matters: Artifact and path proof exist and are non-backdated.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Produce `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` and sibling path proof.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` | `"artifact_kind":"hdapi_v2_release_binding"` | `"subtask_id":"HDE-FERM008.4"` | GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt` | "sha256: b8b8e88f016374fba7c9ce13b1c63394c280889a1826e7c1ec011a7c7fe69c82"

GitHub Repo proof, if current state matters: Artifact and path proof exist and are non-backdated.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Bind PR-02 artifacts into Human Evidence Index and Machine Mirror in the same PR.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | review comment | "generated INDEX/Mirror now contain two rows for the same SHA/path with conflicting epic IDs" | Remedial PR | PR \#332 body | "skip only the promoted snapshot row" | GitHub Repo | `artifacts/evidence_index.jsonl` | `"artifact_key":"hdapi_v2.response_mapping_pr02"` | `"artifact_key":"hdapi_v2.release_binding"`

GitHub Repo proof, if current state matters: Final Machine Mirror contains PR-02 rows and no conflicting EPIC034 shared-snapshot row was observed in reviewed relevant rows.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Preserve distinct EPIC034 PR-03 response-mapping check-log evidence when promoting the shared response-mapping snapshot path.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | review comment | "`audit/qa/hde-epic034/pr-03/response_mapping_check.log` still exists with a path proof but no longer has any index/mirror row" | Remedial PR | PR \#332 body | "preserving `audit/qa/hde-epic034/pr-03/response_mapping_check.log`"

GitHub Repo proof, if current state matters: Final updater skips only the promoted shared snapshot row and tests assert EPIC034 check-log retention.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Fail closed if the shared response-mapping snapshot is not the EPIC035 / HDE-FERM008.4 payload or if release binding points at a stale SHA.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | review comment | "Fail closed unless the snapshot identity and release binding reference match." | GitHub Repo | `tools/evidence/update_evidence_index.py` | `"INVALID_EPIC035_RESPONSE_MAPPING_IDENTITY"` | `"INVALID_EPIC035_RELEASE_BINDING_RESPONSE_REFERENCE"`

GitHub Repo proof, if current state matters: Final `_load_epic035_pr02_entries()` validates snapshot fields and release-binding artifact SHA.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Fail closed on HDAPI v2 route/schema drift.

Original PR status: Not satisfied

After remediation: Satisfied

Evidence pointer(s): Remedial PR | PR \#332 body | "replacing substring inference with explicit route requirements" | GitHub Repo | `tools/evidence/generate_hdapi_v2_response_normalization.py` | `REQUIRED_ROUTE_SCHEMAS` | `REQUIRED_ENVELOPE_FIELDS` | `HDAPI_V2_RESPONSE_NORMALIZATION_ENVELOPE_DRIFT`

GitHub Repo proof, if current state matters: Final generator validates required routes, POST method, exact success envelopes, and exact response envelope fields.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Add targeted tests for response-normalization evidence and remedial gaps.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): GitHub Repo | `tests/evidence/test_hdapi_v2_response_normalization.py` | `test_route_rows_fail_closed_on_required_schema_drift` | `test_index_retains_epic034_pr03_check_log_when_pr02_snapshot_is_promoted` | `test_pr02_loader_fails_closed_on_release_binding_sha_drift`

GitHub Repo proof, if current state matters: Final tests include original PR evidence checks and remedial regression checks.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Do not claim HDE-FERM008.5 closure or HDE-FERM008 parent completion from PR-02.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` | `"posture":"FOLLOW_UP_NOT_CLAIMED_BY_PR02"` | `"subtask_id":"HDE-FERM008.5"` | GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"hde_ferm008_5_closure":"NONE"`

GitHub Repo proof, if current state matters: Final PR-02 artifacts explicitly leave HDE-FERM008.5 as follow-up.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

Requirement: Run scoped validation and evidence checks.

Original PR status: Satisfied

After remediation: Satisfied

Evidence pointer(s): Original PR | PR \#331 body | "312 passed" | "`tools/evidence/update_evidence_index.py --check`" | "`tools/evidence/validate_evidence_paths.py`" | "`ci/checks/check_mirror_schema.sh`" | "`bash ci/checks/check_evidence_index_hash.sh`"; Remedial PR | PR \#332 body | "9 passed" | "`python tools/evidence/update_evidence_index.py --check`" | "`python tools/evidence/orientation_demo.py --check`" | "`ci/checks/check_mirror_schema.sh`"

GitHub Repo proof, if current state matters: Current CI for both PR heads concluded success and current final artifact proofs are coherent.

PF09 task/subtask IDs, if proven: HDE-FERM008 / HDE-FERM008.4

RCA

A) Bug/Failure statement

Original PR \#331 introduced the intended PR-02 evidence family but had an index ownership defect for the reused `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` path. The automated review stated that generated INDEX/Mirror rows contained “two rows for the same SHA/path with conflicting epic IDs and record types,” and later that an early return dropped the distinct EPIC034 PR-03 check-log row.

B) Root cause(s)

1. Shared artifact-path promotion was not filtered precisely enough.  
   Evidence pointer(s): Original PR | review comment | "Registering PR-02 at `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` reuses the same path" | "two rows for the same SHA/path with conflicting epic IDs and record types"  
2. The first fix logic skipped all EPIC034 PR-03 entries when the shared snapshot was promoted.  
   Evidence pointer(s): Original PR | review comment | "this early return drops every EPIC034 PR-03 entry, not just the reused `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` row"  
3. PR-02 index loading originally lacked identity and release-binding-reference checks.  
   Evidence pointer(s): Original PR | review comment | "it never verifies that the shared `response_mapping.snapshot.json` is still the EPIC035/HDE-FERM008.4 payload" | "or that `release_binding.snapshot.json` points at its current SHA"

C) Fix across PRs

* Original PR created the HDE-FERM008.4 response-normalization gap evidence family.  
* Remedial PR changed `_load_epic034_pr03_entries()` to skip only the promoted shared snapshot row, preserving the distinct EPIC034 PR-03 check-log row.  
* Remedial PR added PR-02 snapshot identity validation and release-binding SHA validation in `_load_epic035_pr02_entries()`.  
* Remedial PR hardened route/schema handling by validating exact required paths, POST method, exact `success_envelope`, and required `response_envelope_fields`.

D) Fix verification

* Current tests include regression coverage for EPIC034 check-log retention, release-binding SHA drift, and route-schema drift.  
* Current Machine Mirror includes PR-02 rows for `hdapi_v2.response_mapping_pr02` and `hdapi_v2.release_binding`.  
* Current PR-02 direct path proofs and index/mirror path proofs are coherent and non-backdated.  
* Visible CI for the Remedial PR succeeded.

PF09 Impact & Status Posture

PF09.x document title: PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.4

PF09 task ID: HDE-FERM008

PF09 subtask ID(s): HDE-FERM008.4

Current PF09 status: Subtask status: Not done

Status recommendation: change to Done

Why supported: The net merged work provides the PF09.5 HDE-FERM008.4 required artifacts, records an exact adapter/schema gap as PF09.5 allows when v2 response data cannot truthfully feed the existing BodyGraph cache, avoids compatibility by inference, preserves no public Reader / AI / full runtime conformance claims, and binds the evidence through current Human Index / Machine Mirror / path-proof posture. This recommendation applies only to HDE-FERM008.4, not HDE-FERM008 parent, HDE-FERM008.5, or full HumanDesignAPI v2 runtime conformance.

Evidence pointer(s): GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"pf09_subtask_id":"HDE-FERM008.4"` | `"schema_gap_status":"GAP_RECORDED"` | `"normalized_data_path_proof_claim":"NONE"`; GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` | `"subtask_id":"HDE-FERM008.4"` | `"posture":"FOLLOW_UP_NOT_CLAIMED_BY_PR02"`

GitHub Repo proof, if repo state matters: Current `main` equals Remedial PR merge commit `7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d`; no later commits alter reviewed files.

PF proof excerpt(s):

PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows

"Prove that a v2 response, from fixture or PO-run smoke evidence as permitted, can be normalized into the existing BodyGraph/cache and compat input path without changing public Reader bytes or leaking admin-only data."

"Subtask status: Not done"

"\* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`  
* `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt`"

PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows

"If the v2 response cannot truthfully feed the existing BodyGraph cache without schema changes, record the schema gap and route it to PF12 and PF14. Do not claim compatibility by inference."

Linked NET/Finding IDs: NET-007, NET-008, NET-009, NET-010, NET-030, NET-031, NET-036, NET-037, NET-038, F-001, F-002, F-003, F-004

Findings

F-001

Related item: NET-009 / Crosswalk / PF09

Severity: Note

Observation: Final `response_mapping.snapshot.json` records exact HDE-FERM008.4 schema/adapter gap posture rather than claiming normalized-data-path proof.

Why it matters: This satisfies the allowed PF09.5 fallback when v2 response data cannot truthfully feed existing BodyGraph/cache/compat paths.

Evidence: GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"schema_gap_status":"GAP_RECORDED"` | `"no_compatibility_by_inference":true`

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.4; change to Done.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows

F-002

Related item: NET-007 / NET-008 / NET-010 / Evidence

Severity: Note

Observation: Required PR-02 artifacts and path proofs are present and coherent.

Why it matters: PF09.5 lists these artifacts as the HDE-FERM008.4 evidence surface.

Evidence: GitHub Repo | `response_mapping.snapshot.json.path_proof.txt` and `release_binding.snapshot.json.path_proof.txt` | matching `mtime_utc` and `produced_at_utc`.

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.4; change to Done.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

F-003

Related item: NET-038 / RCA

Severity: Note

Observation: Remedial PR corrected evidence-index ownership by skipping only the promoted shared snapshot EPIC034 row and preserving the EPIC034 PR-03 check-log row.

Why it matters: This closes the Original PR indexing defect without losing historical EPIC034 governed evidence.

Evidence: GitHub Repo | `tools/evidence/update_evidence_index.py` | `shared_snapshot_promoted` | `if shared_snapshot_promoted and entry.get("discovered_physical_path") == snapshot.relative_to(ROOT).as_posix(): continue`

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.4; change to Done.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

F-004

Related item: NET-038 / VAL-009 / RCA

Severity: Note

Observation: PR-02 index loading now fails closed on invalid snapshot identity or release-binding SHA drift.

Why it matters: Prevents stale or EPIC034-owned response-mapping bytes from being mislabeled as HDE-EPIC035 PR-02 evidence.

Evidence: GitHub Repo | `tools/evidence/update_evidence_index.py` | `INVALID_EPIC035_RESPONSE_MAPPING_IDENTITY` | `INVALID_EPIC035_RELEASE_BINDING_RESPONSE_REFERENCE`

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.4; change to Done.

PF reference, if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

F-005

Related item: NET-037 / NET-036 / VAL-009

Severity: Note

Observation: Tests now cover route/schema drift, release-binding SHA drift, EPIC034 check-log retention, canonical JSON, no-claim posture, and path-proof binding.

Why it matters: Regression coverage matches the material Original PR and remedial risk areas.

Evidence: GitHub Repo | `tests/evidence/test_hdapi_v2_response_normalization.py` | `test_route_rows_fail_closed_on_required_schema_drift` | `test_index_retains_epic034_pr03_check_log_when_pr02_snapshot_is_promoted` | `test_pr02_loader_fails_closed_on_release_binding_sha_drift`

Required action: None.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.4; change to Done.

PF reference, if relied on: None

F-006

Related item: PF09

Severity: Note

Observation: HDE-FERM008.4 is supportable for a PF09.5 status recommendation to Done, but HDE-FERM008 parent and HDE-FERM008.5 are not included in this PR’s status recommendation.

Why it matters: Prevents overclaiming the broader live-conformance sequence.

Evidence: GitHub Repo | `release_binding.snapshot.json` | `"posture":"FOLLOW_UP_NOT_CLAIMED_BY_PR02"` | `"subtask_id":"HDE-FERM008.5"`

Required action: PF09.5 status-drain candidate only for HDE-FERM008.4.

Blocker: No

PF09 impact/status, if proven: HDE-FERM008 / HDE-FERM008.4; change to Done.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows

Evidence Print (PASS PROOF; merged work)

A) Acceptance coverage evidence

* Requirement covered: HDE-FERM008.4 response-normalization or exact schema/adapter gap evidence.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"response_normalization_posture":"EXACT_SCHEMA_ADAPTER_GAP_RECORDED"` | `"schema_gap_status":"GAP_RECORDED"` | `"normalized_data_path_proof_claim":"NONE"`  
  GitHub Repo proof: Final snapshot exists with HDE-EPIC035 / HDE-FERM008.4 metadata and exact gap basis.  
* Requirement covered: no compatibility by inference.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"no_compatibility_by_inference":true` | `"schema_gap_summary":"HDE-FERM008.4 remains an exact adapter/schema gap"`  
  GitHub Repo proof: Final snapshot records gap instead of compatibility proof.  
* Requirement covered: no public Reader / no full v2 conformance / no AI / no raw payload overclaim.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | `"full_hdapi_v2_runtime_conformance":"NONE"` | `"public_reader_change":"NONE"` | `"raw_vendor_payload_persisted":"NONE"` | `"no_ai_transformation_posture"`  
  GitHub Repo proof: Final snapshot and release binding preserve no-claim posture.  
* Requirement covered: release binding.  
  Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` | `"pr01_hde_ferm008_3_provider_outcome"` | `"pr02_hde_ferm008_4_response_normalization"` | `"follow_up_hde_ferm008_5_evidence_loop_closure"`  
  GitHub Repo proof: Final release-binding artifact binds PR-01 and PR-02 evidence without claiming HDE-FERM008.5.

B) Original gaps closed

* Original stale EPIC034 response-mapping shared-path row closed.  
  Evidence pointer: Remedial PR | PR \#332 body | "skip only the promoted snapshot row" | "preserving `audit/qa/hde-epic034/pr-03/response_mapping_check.log`"  
  GitHub Repo proof: Final updater skips only the promoted shared snapshot row.  
* Original missing PR-02 snapshot identity / release-binding validation closed.  
  Evidence pointer: GitHub Repo | `tools/evidence/update_evidence_index.py` | `INVALID_EPIC035_RESPONSE_MAPPING_IDENTITY` | `INVALID_EPIC035_RELEASE_BINDING_RESPONSE_REFERENCE`  
  GitHub Repo proof: Final loader validates snapshot identity and release-binding SHA linkage.  
* Original route/schema inference risk closed.  
  Evidence pointer: GitHub Repo | `tools/evidence/generate_hdapi_v2_response_normalization.py` | `REQUIRED_ROUTE_SCHEMAS` | `REQUIRED_ENVELOPE_FIELDS` | `HDAPI_V2_RESPONSE_NORMALIZATION_ENVELOPE_DRIFT`  
  GitHub Repo proof: Final generator validates route set, method, envelope, and fields.

C) Evidence and verification posture

* Human Evidence Index posture.  
  Evidence pointer: GitHub Repo | `docs/evidence/INDEX.json.path_proof.txt` | "sha256: 769aecff85b305fa2c4966a73472fcc1e69562464e683a9c5304b22be0240ecf" | "produced\_at\_utc: 2026-06-28T10:17:56Z"  
  GitHub Repo proof: Human Index path proof is present and not backdated.  
* Machine Mirror posture.  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | `"artifact_key":"hdapi_v2.response_mapping_pr02"` | `"artifact_key":"hdapi_v2.release_binding"` | GitHub Repo | `artifacts/evidence_index.jsonl.path_proof.txt` | "produced\_at\_utc: 2026-06-28T10:17:56Z"  
  GitHub Repo proof: Machine Mirror rows and self-proof are present.  
* PR-02 artifact path-proof posture.  
  Evidence pointer: GitHub Repo | PR-02 path proofs | "mtime\_utc: 2026-06-28T09:27:28Z" | "produced\_at\_utc: 2026-06-28T09:27:28Z"  
  GitHub Repo proof: Response mapping and release binding path proofs are present and non-backdated.

D) Token/gate evidence, only for explicitly claimed tokens/gates

* Token: `JSON_CANONICAL_CHECK_OK`  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | PR-02 rows list `"JSON_CANONICAL_CHECK_OK"` | GitHub Repo | `tests/evidence/test_hdapi_v2_response_normalization.py` | canonical JSON tests present.  
  GitHub Repo proof: Final tests assert canonical JSON shape.  
* Token: `EVIDENCE_PATH_PROOFS_OK`  
  Evidence pointer: GitHub Repo | `artifacts/evidence_index.jsonl` | PR-02 rows list `"EVIDENCE_PATH_PROOFS_OK"` | GitHub Repo | PR-02 path proofs | response mapping and release binding proof files present.  
  GitHub Repo proof: Direct path proofs inspected.

E) Test/CI proof

* Original PR CI.  
  Evidence pointer: Original PR | workflow run | "name: ci" | "conclusion: success"  
* Remedial PR CI.  
  Evidence pointer: Remedial PR | workflow run | "name: ci" | "conclusion: success"  
* Original PR targeted validation.  
  Evidence pointer: Original PR | PR \#331 body | "312 passed" | "`python tools/evidence/generate_hdapi_v2_response_normalization.py --check`" | "`python tools/evidence/update_evidence_index.py --check`" | "`bash ci/checks/check_evidence_index_hash.sh`"  
* Remedial PR targeted validation.  
  Evidence pointer: Remedial PR | PR \#332 body | "9 passed" | "`python tools/evidence/update_evidence_index.py --check`" | "`python tools/evidence/orientation_demo.py --check`" | "`ci/checks/check_mirror_schema.sh`"

F) Artifact and evidence outputs, including governed path/index/mirror/path-proof posture when relevant

* Path: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
  Type: canonical JSON snapshot  
  Key proof facts observed: HDE-EPIC035, HDE-FERM008.4, exact schema/adapter gap, no compatibility by inference, no public Reader change, no AI scope, no raw payload persistence.  
  Index/Mirror/path-proof posture: Indexed and mirrored under `hdapi_v2.response_mapping_pr02`; path proof present and non-backdated.  
* Path: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`  
  Type: path proof  
  Key proof facts observed: `sha256: b7ee708ad8a3b35c4b402d9304040ce55498c783a356c08ea3613c017b8a7a23`; `mtime_utc: 2026-06-28T09:27:28Z`; `produced_at_utc: 2026-06-28T09:27:28Z`.  
  Index/Mirror/path-proof posture: Co-located companion proof.  
* Path: `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`  
  Type: canonical JSON snapshot  
  Key proof facts observed: binds PR-01 HDE-FERM008.3 artifacts, PR-02 HDE-FERM008.4 response-mapping artifact, and marks HDE-FERM008.5 as follow-up not claimed.  
  Index/Mirror/path-proof posture: Indexed and mirrored under `hdapi_v2.release_binding`; path proof present and non-backdated.  
* Path: `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt`  
  Type: path proof  
  Key proof facts observed: `sha256: b8b8e88f016374fba7c9ce13b1c63394c280889a1826e7c1ec011a7c7fe69c82`; `mtime_utc: 2026-06-28T09:27:28Z`; `produced_at_utc: 2026-06-28T09:27:28Z`.  
  Index/Mirror/path-proof posture: Co-located companion proof.  
* Path: `docs/evidence/INDEX.json`  
  Type: Human Evidence Index  
  Key proof facts observed: PR-02 evidence family bound through final path proof and Machine Mirror rows.  
  Index/Mirror/path-proof posture: Companion proof and hash sentinel updated.  
* Path: `artifacts/evidence_index.jsonl`  
  Type: Machine Mirror  
  Key proof facts observed: PR-02 rows for `hdapi_v2.response_mapping_pr02` and `hdapi_v2.release_binding`; Machine Mirror self-proof current.  
  Index/Mirror/path-proof posture: Companion proof and hash sentinel updated.

Doc Delta Candidates (PF-Canon only)

DDC-001

Doc: PF09.5 — HDE Build Checklist Fermentation

Section: §Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task/subtask IDs: HDE-FERM008 / HDE-FERM008.4

PF09 status action: change to Done

Delta: Update HDE-FERM008.4 status from `Not done` to `Done`, preserving the subtask scope as v2 response normalization proof or exact schema/adapter gap recording only. Do not update HDE-FERM008 parent or HDE-FERM008.5 from this PR-02 evidence.

Why: Current GitHub Repo evidence contains the required HDE-FERM008.4 artifacts, exact schema/adapter gap proof, release binding, same-PR Human Index / Machine Mirror / path-proof posture, and regression coverage for the original indexing defect.

Evidence pointer: GitHub Repo | `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` | HDE-FERM008.4 exact schema/adapter gap evidence; GitHub Repo | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` | PR-01 / PR-02 binding and HDE-FERM008.5 nonclaim; GitHub Repo | `artifacts/evidence_index.jsonl` | PR-02 rows.

GitHub Repo proof, if repo state matters: Current `main` equals Remedial PR merge commit `7e42e51a6b4ba4b43dd65c384b7f4fad05e6e41d`; direct artifact, Human Index, Machine Mirror, and path proofs inspected and coherent.

Canon proof excerpt, unless Canon basis is CANON SILENCE:

"\#\#\# **Subtask HDE-FERM008.4 \- Prove v2 response normalization feeds existing HDE flows**"

"Prove that a v2 response, from fixture or PO-run smoke evidence as permitted, can be normalized into the existing BodyGraph/cache and compat input path without changing public Reader bytes or leaking admin-only data."

"Subtask status: Not done"

"\* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`  
* `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt`"

DECISION: MERGED WORK ACCEPTABLE

## **2.3) PF29 HD Engine User Guide seed — runnable end-to-end workflows**

Timestamp: 062826 12:51 Africa/Casablanca

Drain target: PF29-Canon-HDE-User-Guide

Details:

This addendum seeds a new permanent PF Canon document, PF29-Canon-HDE-User-Guide. PF29 must not replace HDE Architecture, HDE CLI/API Vendor Ref, Glow Infrastructure, HDE Schemas & Artifacts, HDE Mechanics Guide, Glow QA Guide, or HDE Build Checklist. PF29’s job is to give a runnable, end-to-end operator and agent guide for using the HD Engine itself: generating BodyGraph-shaped payloads, running compat, using the Reader/dev harness, accessing JSON payloads, running sampler/admin/dev surfaces, and understanding which production paths are currently supported versus intentionally blocked.

This addendum is based on current repo reality and must be drained into PF29 after review. The repo currently exposes `hdctl` as the console entrypoint through `engine.cli.main:cli`, with a source-tree fallback launcher at `scripts/hdctl.py`; the install proof records `pip install -e . --no-deps --no-build-isolation` and confirms the console entrypoint is available.

### **2.3.1 Scope boundary for PF29**

PF29 must document HD Engine usage, not the Glow app product UX.

PF29 must include:

* how to start the local/dev QA Reader harness;  
* how to call the dev sampler harness;  
* how to run compat from CLI payloads;  
* how to run compat through the local HTTP Reader/adapter surface;  
* how to emit Reader JSON;  
* how to emit admin JSON payloads, including left/right BodyGraph JSON, composite BodyGraph JSON, and compat proof JSON;  
* how to run conjunction compat;  
* how to resolve or ingest BodyGraph data from DB or vendor paths when rails and configuration allow;  
* how to run evidence/index/mirror checks after generated evidence changes;  
* how to distinguish QA/dev, closed-rails runs from production/open-rails runs;  
* how to avoid secret leakage and raw payload overclaim.

PF29 must not claim:

* that `/api/compat/v1` POST is production-public;  
* that the production app owns a direct HumanDesignAPI credential path;  
* that v2 ChartResult / ChartSimpleResult currently feeds the BodyGraph cache and compat path end-to-end;  
* that HDE-FERM008.5 is completed by PR-01 or PR-02;  
* that a live vendor call is safe without PO authorization and open-rails scope;  
* that raw vendor payload bodies, raw request bodies, raw response bodies, bearer token values, API key values, or geocode key values may be captured as evidence.

The current repo confirms that the Reader/adapter factory registers the Reader blueprint and the compat blueprint, that `/api/compat/v1` is the compat route prefix, and that the compat POST path returns 404 when `APP_ENV=prod`.

### **2.3.2 Canonical rails posture for runnable examples**

Closed-rails QA/default command prefix:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`

Use that prefix for deterministic local/QA CLI, Reader harness, sampler harness, compat payload tests, canonical JSON checks, evidence-index checks, and mirror checks. The repo docs explicitly pin this determinism environment, and the dev Reader script defaults to `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, and `PORT=8000`.

Open-rails vendor/live prefix, only when explicitly authorized:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=0 ALLOW_NETWORK=1`

Open rails are required for real vendor acquisition. The current BodyGraph resolver refuses vendor source under `SAFE_MODE=1` and blocks network unless `ALLOW_NETWORK=1`; with open rails it calls `ingest_vendor_bodygraph`.

### **2.3.3 Install and entrypoint workflow**

Preferred setup from a clean checkout:

`python -m pip install -e . --no-deps --no-build-isolation`

Then verify:

`hdctl --help`

`hdctl --version`

If the console entrypoint is unavailable in a source-tree context, use:

`python scripts/hdctl.py --help`

The repo validates `hdctl = "engine.cli.main:cli"` in `pyproject.toml`, and the fallback launcher directly imports `engine.cli.main.cli`.

### **2.3.4 Start the local/dev QA Reader harness**

Use this as the canonical local/dev QA app harness start:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh`

This starts the Reader/adapter process with the Flask dev runner through `python -m adapter.http_reader`, binding to `0.0.0.0` on `PORT`, default `8000`.

Default local URL family:

`http://127.0.0.1:8000`

Dev sampler URL:

`http://127.0.0.1:8000/internal/dev/sampler`

Run the dev sampler healthcheck in a second terminal:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler scripts/qa/dev_sampler_healthcheck.py`

The repo docs list the same Reader helper, dev sampler healthcheck, dev sampler Live QA, and output log locations.

### **2.3.5 Dev sampler HTTP workflow**

The internal dev sampler route is:

`POST /internal/dev/sampler`

It is dev/admin gated. It proceeds only when `APP_ENV` is `dev`, `test`, or `local`; otherwise it returns a writer-style forbidden envelope. The route accepts only `viewer_id`, `candidate_ids`, and optional `seed`.

Example request body:

`{"viewer_id":"qa-viewer-001","candidate_ids":["qa-candidate-001","qa-candidate-002"],"seed":"pf29-smoke-001"}`

Example local command:

`curl -sS -X POST http://127.0.0.1:8000/internal/dev/sampler -H 'Content-Type: application/json; charset=utf-8' --data-binary '{"viewer_id":"qa-viewer-001","candidate_ids":["qa-candidate-001","qa-candidate-002"],"seed":"pf29-smoke-001"}'`

Expected successful response shape:

* canonical JSON;  
* `viewer_id`;  
* `meta.seed`;  
* ordered `candidate_ids`;  
* `Cache-Control: no-store`;  
* no ETag.

The implementation builds exactly those fields and removes ETag.

### **2.3.6 Reader v1 local workflow**

Reader route:

`GET /reader?v=1&a=<fixture-chart-a>&b=<fixture-chart-b>&a_tz=<iana-or-offset>&b_tz=<iana-or-offset>`

Rules:

* `v=1` is required.  
* `APP_ENV` must be `dev` for `/reader`.  
* `a` and `b` must point to safe chart files under `fixtures/charts`.  
* Missing timezone in the chart may be supplied via `a_tz` / `b_tz`.  
* Success returns public Reader bytes with JSON content type, cache headers, ETag, and content length.

The repo confirms these reader parameters, `APP_ENV=dev` gate, safe fixture root, and timezone requirement.

PF29 must warn that Reader v1 public output is bands-only / public posture. Numeric/admin details belong to CLI/admin dumps, not Reader public JSON.

### **2.3.7 HTTP compat workflow in QA/dev, not prod-public**

Local QA/dev compat computation route:

`POST /api/compat/v1`

Example local command:

`curl -sS -X POST http://127.0.0.1:8000/api/compat/v1 -H 'Content-Type: application/json; charset=utf-8' --data-binary @compat_request.json > compat_response.json`

Example `compat_request.json`:

`{"a":{"person_uid":"qa-left"},"b":{"person_uid":"qa-right"},"viewer_prefs":{"top_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}}`

The canonical category IDs and order are `heat`, `harmony`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`.

Important production boundary:

`/api/compat/v1` POST returns 404 when `APP_ENV=prod`. PF29 must state directly that HTTP compat POST is a QA/dev/internal surface in current repo reality, not a production-public compat endpoint.

### **2.3.8 CLI compat workflow from payloads**

Use CLI payload mode for deterministic local/QA compat without DB or vendor IO.

Create `pair.json`:

`{"left":{"person_uid":"qa-left","birthdate":"1990-01-01","birthtime":"12:00","location":"Paris, FR"},"right":{"person_uid":"qa-right","birthdate":"1991-02-03","birthtime":"08:30","location":"Lisbon, PT"}}`

Run:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file pair.json > compat.json`

Fallback if `hdctl` is not installed:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python scripts/hdctl.py showcompat --pair-file pair.json > compat.json`

The CLI supports `showcompat --pair-file`, `--a-file/--b-file`, or stdin; success bytes are LF-terminated canonical JSON printed to stdout.

### **2.3.9 Generate BodyGraph JSON, composite BodyGraph JSON, compat proof JSON, and Reader JSON from CLI**

PF29 should define this as the main end-to-end local QA workflow because it uses current repo code and produces useful JSON payloads without vendor IO.

Command:

`mkdir -p audit/tmp/pf29/compat_admin`

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file pair.json --dump-reader audit/tmp/pf29/reader.json --dump-admin-dir audit/tmp/pf29/compat_admin > audit/tmp/pf29/compat.json`

Fallback:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python scripts/hdctl.py showcompat --pair-file pair.json --dump-reader audit/tmp/pf29/reader.json --dump-admin-dir audit/tmp/pf29/compat_admin > audit/tmp/pf29/compat.json`

Expected outputs when the pair file is named `pair.json`:

* `audit/tmp/pf29/compat.json`  
* `audit/tmp/pf29/reader.json`  
* `audit/tmp/pf29/compat_admin/pair.left.bodygraph.json`  
* `audit/tmp/pf29/compat_admin/pair.right.bodygraph.json`  
* `audit/tmp/pf29/compat_admin/pair.composite.bodygraph.json`  
* `audit/tmp/pf29/compat_admin/pair.compat.proof.json`  
* `.sha256` sidecars for admin dumps, because the admin dump helper writes canonical JSON and sidecars.

The current CLI code writes left BodyGraph, right BodyGraph, composite BodyGraph, and compat proof JSON under `--dump-admin-dir`, and the fallback launcher documents that admin dumps are written with mode `0600` alongside `.sha256` files.

### **2.3.10 Conjunction compat workflow**

Payload/file mode, closed rails:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --conjunction --pair-file conjunction_pair.json > conjunction.json`

`conjunction_pair.json` shape:

`{"left":{"person_uid":"qa-left","birthdate":"1990-01-01","birthtime":"12:00","location":"Paris, FR"},"right":{"person_uid":"qa-right","birthdate":"1991-02-03","birthtime":"08:30","location":"Lisbon, PT"}}`

Other supported forms:

`hdctl showcompat --conjunction --a-file left.json --b-file right.json`

`hdctl showcompat --conjunction < conjunction_pair.json`

DB/vendor user mode:

`hdctl showcompat --conjunction --user-a <user_a> --user-b <user_b> --source db`

`SAFE_MODE=0 ALLOW_NETWORK=1 hdctl showcompat --conjunction --user-a <user_a> --user-b <user_b> --source vendor --birthdate-a YYYY-MM-DD --birthtime-a HH:MM --location-a "Place" --birthdate-b YYYY-MM-DD --birthtime-b HH:MM --location-b "Place"`

The CLI docs state conjunction mode supports `--user-a/--user-b`, `--pair-file`, `--a-file/--b-file`, or stdin; unresolved user inputs can trigger BodyGraph resolution and vendor ingest under open rails, while closed rails may emit explicit refusal codes.

### **2.3.11 Dev HTTP conjunction routes**

Dev-only HTTP routes:

* `GET /dev/sampler/conjunction`  
* `GET /dev/reader/conjunction`  
* `GET /dev/writer/conjunction`

Required query parameters:

* `a_user_id`  
* `b_user_id`

Optional query parameters:

* `a_birthdate`  
* `a_birthtime`  
* `a_location`  
* `b_birthdate`  
* `b_birthtime`  
* `b_location`

Example:

`curl -sS 'http://127.0.0.1:8000/dev/reader/conjunction?a_user_id=qa-left&b_user_id=qa-right&a_birthdate=1990-01-01&a_birthtime=12:00&a_location=Paris%2C%20FR&b_birthdate=1991-02-03&b_birthtime=08:30&b_location=Lisbon%2C%20PT' > dev_reader_conjunction.json`

These routes are APP\_ENV-gated by the same dev/admin gate, and the implementation builds canonical request fields from the query parameters.

### **2.3.12 Aux narrative preview workflow**

CLI Aux preview from a compat payload:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl aux-preview --pair-file compat.json --category harmony --band Cool --perspective shared --show-narrative --admin-out aux_sidecar.json`

The CLI supports `aux-preview --pair-file <compat.json> --category <slug> --band <band> --perspective <perspective> [--show-narrative] [--admin-out <ids.json>]`.

HTTP Aux narrative routes on the Reader harness:

* `GET /api/aux/narrative`  
* `GET /aux/narrative`

Key query parameters:

* `category`  
* `band`  
* `perspective`  
* optional `viewer_top`  
* optional `flags` / `flag`  
* optional `families_fired`  
* optional `release_id`  
* optional `pack_sha`

The implementation exposes both `/api/aux/narrative` and `/aux/narrative`, emits text/plain, and includes narrative pack/composition headers.

### **2.3.13 BodyGraph resolution and vendor ingest workflow**

Closed-rails DB/default dry path:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl bg:resolve --user qa-user --source auto --dry-run`

Vendor source requires a full birth tuple:

`SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user qa-user --source vendor --birthdate YYYY-MM-DD --birthtime HH:MM --location "Place" --dry-run`

To request persistence into the BodyGraph DB path, omit `--dry-run` and use the current repo’s supported DB environment. If DB is unavailable or configuration is absent, the command may fail with typed DB/provider errors. Do not claim rows were written unless the command output reports `rows_written` / `db_rows_after`.

The CLI parser requires `--user`, supports `--source auto|db|vendor`, `--upsert`, `--dry-run`, and vendor birth fields; source `vendor` requires `birthdate`, `birthtime`, and `location`.

The resolver refuses vendor source under SAFE rails, blocks network without `ALLOW_NETWORK=1`, and calls `ingest_vendor_bodygraph` only after open-rails checks and input resolution.

### **2.3.14 Vendor config and geokey syntax**

Current canonical environment keys:

* `HD_API_BASE_URL`  
* `HD_API_KEY`  
* `GEO_API_KEY`  
* compatibility alias: `HDAPI_BASE_URL`, only if `HD_API_BASE_URL` is absent

The current vendor client resolves `HD_API_BASE_URL` first, falls back to `HDAPI_BASE_URL`, requires `HD_API_KEY`, and reads `GEO_API_KEY`.

Current route/header truth:

* legacy `bodygraphs` and `bodygraphs/simple` routes use `HD-Api-Key`;  
* v2 `charts`, `charts/simple`, and `charts/coordinates` routes use `Authorization: Bearer`;  
* `charts` and `charts/simple` require geocode and therefore require `HD-Geocode-Key`;  
* `charts/coordinates` uses lat/lng and does not require geocode.

The current route contract table and request builder implement those header choices.

PF29 must state the gap plainly: current PR-02 evidence records that v2 ChartResult / ChartSimpleResult data is not yet truthfully proven to feed the existing BodyGraph cache or compat input path without a ChartResult-to-BodyGraph/person adapter proof. The current `response_mapping.snapshot.json` records `normalized_data_path_proof_claim:"NONE"` and `schema_gap_status:"GAP_RECORDED"`, while preserving v2 route identity and header posture.

### **2.3.15 Production usage posture**

Production use must be separated into three categories.

1. Production Reader/service identity checks

Use production service base URL from infrastructure, not from guessed docs. Safe checks include:

`GET /internal/version`

`HEAD /internal/version`

The `/internal/version` route is implemented on the Reader blueprint, emits no-store JSON identity bytes, and is registered with GET/HEAD.

2. Production compat

Do not document `/api/compat/v1` POST as a production-public compat endpoint. Current code returns 404 for compat POST when `APP_ENV=prod`. Production compat computation, if needed, must be an internal/server-side or CLI/operator workflow, not a public HTTP claim.

3. Production/open-rails vendor BodyGraph acquisition

Use only with explicit authorization, correct production config, and secret-safe evidence capture:

`SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user <approved-user-or-test-id> --source vendor --birthdate YYYY-MM-DD --birthtime HH:MM --location "Place" --dry-run`

For a persistent run, remove `--dry-run` only when DB config is present and the operator intends to write. The ingest path persists to `hde.body_graphs` only when not dry-run; dry-run reports zero rows written.

PF29 must warn that the current `bg:resolve` runtime path uses the current BodyGraph ingest path. It does not prove v2 ChartResult/ChartSimpleResult normalization into compat; PR-02 intentionally records that as a schema/adapter gap.

### **2.3.16 Evidence and validation commands after generated artifacts change**

When workflows create governed evidence or update artifacts, run the current evidence refresh/check sequence.

Write/update sequence:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/update_evidence_index.py`

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/orientation_demo.py`

Check sequence:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/update_evidence_index.py --check`

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/validate_evidence_paths.py`

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python ci/checks/check_mirror_schema.sh`

`bash ci/checks/check_evidence_index_hash.sh`

The current CLI docs define the refresh order as update evidence index, orientation demo, check variants, then mirror schema check; RUN.md also identifies evidence/index/mirror discipline and governed path-proof requirements.

### **2.3.17 Minimum PF29 workflow recipes**

PF29 should include these exact runnable recipes.

Recipe A — local QA Reader \+ dev sampler

Terminal 1:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh`

Terminal 2:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler scripts/qa/dev_sampler_healthcheck.py`

Recipe B — local CLI compat \+ BodyGraph/admin JSON payloads

`cat > pair.json <<'EOF'`  
 `{"left":{"person_uid":"qa-left","birthdate":"1990-01-01","birthtime":"12:00","location":"Paris, FR"},"right":{"person_uid":"qa-right","birthdate":"1991-02-03","birthtime":"08:30","location":"Lisbon, PT"}}`  
 `EOF`

`mkdir -p audit/tmp/pf29/compat_admin`

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file pair.json --dump-reader audit/tmp/pf29/reader.json --dump-admin-dir audit/tmp/pf29/compat_admin > audit/tmp/pf29/compat.json`

Fallback if console entrypoint is unavailable:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python scripts/hdctl.py showcompat --pair-file pair.json --dump-reader audit/tmp/pf29/reader.json --dump-admin-dir audit/tmp/pf29/compat_admin > audit/tmp/pf29/compat.json`

Expected files:

* `audit/tmp/pf29/compat.json`  
* `audit/tmp/pf29/reader.json`  
* `audit/tmp/pf29/compat_admin/pair.left.bodygraph.json`  
* `audit/tmp/pf29/compat_admin/pair.right.bodygraph.json`  
* `audit/tmp/pf29/compat_admin/pair.composite.bodygraph.json`  
* `audit/tmp/pf29/compat_admin/pair.compat.proof.json`

Recipe C — local HTTP compat

Start Reader as in Recipe A.

`cat > compat_request.json <<'EOF'`  
 `{"a":{"person_uid":"qa-left"},"b":{"person_uid":"qa-right"},"viewer_prefs":{"top_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}}`  
 `EOF`

`curl -sS -X POST http://127.0.0.1:8000/api/compat/v1 -H 'Content-Type: application/json; charset=utf-8' --data-binary @compat_request.json > http_compat_response.json`

Recipe D — local Aux narrative preview

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl aux-preview --pair-file audit/tmp/pf29/compat.json --category harmony --band Cool --perspective shared --show-narrative --admin-out audit/tmp/pf29/aux_sidecar.json`

Recipe E — local conjunction compat from payload

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --conjunction --pair-file pair.json > audit/tmp/pf29/conjunction.json`

Recipe F — open-rails vendor BodyGraph dry-run

Before running, confirm the production/operator environment has `HD_API_BASE_URL`, `HD_API_KEY`, and, for geocode-required routes, `GEO_API_KEY`. Do not print their values.

`SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user qa-user --source vendor --birthdate YYYY-MM-DD --birthtime HH:MM --location "Place" --dry-run > vendor_bodygraph_dry_run.json`

Recipe G — open-rails vendor BodyGraph persistence

Only run when DB configuration is present and persistence is intended.

`SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user qa-user --source vendor --birthdate YYYY-MM-DD --birthtime HH:MM --location "Place" > vendor_bodygraph_persist.json`

PF29 must state that success is determined by the emitted JSON payload and, for persistence, by `rows_written`, `db_rows_after`, and parity fields in the output, not by assumption.

### **2.3.18 Known current limitations to preserve**

* `/api/compat/v1` POST is not production-public because current code returns 404 when `APP_ENV=prod`.  
* `/internal/dev/sampler` and `/dev/*/conjunction` are dev/test/local-only.  
* Current `bg:resolve --source vendor` can acquire vendor BodyGraph data under open rails, but v2 ChartResult/ChartSimpleResult normalization into the existing BodyGraph cache remains an exact schema/adapter gap.  
* The current HDAPI v2 evidence records route/header correctness and exact gap posture, not full HumanDesignAPI v2 runtime conformance.  
* No workflow may record raw vendor payload bodies, raw request bodies, raw response bodies, bearer token values, API key values, geocode key values, or production user PII.  
* PF29 must distinguish evidence-generation workflows from user-facing runtime workflows. Evidence outputs under `audit/**` and `artifacts/**` require Human Evidence Index / Machine Mirror / path-proof discipline when promoted.

### **2.3.19 PF29 structure recommendation**

PF29 should use this first-draft section spine:

1. Purpose and scope  
2. Rails and environment modes  
3. Install and entrypoints  
4. Local/dev QA Reader harness  
5. Dev sampler workflow  
6. Reader v1 workflow  
7. Compat HTTP workflow  
8. CLI compat workflow  
9. BodyGraph/admin JSON export workflow  
10. Conjunction workflow  
11. Aux narrative preview workflow  
12. BodyGraph resolve and vendor ingest workflow  
13. HDAPI config and geokey/header syntax  
14. Production posture  
15. Evidence and validation workflow  
16. Known limitations and nonclaims  
17. Troubleshooting table  
18. Quick command reference

Drain note:

Drain this addendum into PF29-Canon-HDE-User-Guide. Keep PF29 as a runnable workflow guide only. Do not use PF29 to redefine architecture, transport bytes, token semantics, evidence schemas, PF09 status, QA policy, infrastructure ownership, or vendor contracts.

##  2.4) OPS-01 HDE-EPIC035

Review Summary

* OPS actions performed: one bounded open-rails `hdctl bg:resolve --source vendor --dry-run` observation, one diagnostic no-version rerun, and one command-backed v2 `charts/simple` geocode-required provider observation.  
* The OPS evidence aligns with the Approved Plan’s bounded PO-only live-observation role: it contributes evidence only and preserves nonclaims for QA PASS, PF09 status movement, closeout, full v2 runtime conformance, public Reader change, new route, app-side vendor credential ownership, raw payload persistence, and AI scope.  
* Repo validation confirms the retained OPS evidence is present on current `main`, readable, and tracked or modified-tracked under governed evidence roots.  
* The earlier proof gaps were remediated: the v2 `charts/simple` geokey observation now has command, exit code, stdout, stderr, result summary, final classification, final repo status, and checksum-ledger evidence.  
* The retained evidence proves the provider responds successfully on the correct v2 `charts/simple` geocode-required route with `Authorization: Bearer <redacted>`, `HD-Geocode-Key: <redacted>`, and no legacy `HD-Api-Key` on the v2 path.  
* The retained evidence also proves `bg:resolve` is not the correct v2 chart/geokey validation path: it uses legacy BodyGraph route/header posture against the configured v2 base and returns `PROVIDER_NOT_FOUND` / 404\.  
* PF09 support is limited to evidence contribution. OPS-01 does not support PF09 status movement or HDE-FERM008.5 closure by itself.

Repo Evidence Validation Summary

Observed repo root:

Repo | GitHub repository metadata | "repository\_full\_name: amthorn78/glow-hdengine-v2" | "default\_branch: main"

Observed HEAD:

Repo | compare `main..main` | "base\_commit.sha: 3196a2b4029b05155e12d772ca24f9b3af129cae" | "status: identical"

Branch or detached state:

Repo | GitHub repository metadata / compare | "default\_branch: main" | "head: main"

Working tree status before validation:

Not applicable to GitHub read-only review. Repo state was validated against current GitHub `main`; no mutable local checkout was used.

Working tree status after validation:

Not applicable to GitHub read-only review. No files were edited, copied, moved, staged, regenerated, or committed by this review.

Read-only repo validation commands or methods used:

* Repo | GitHub `get_repo` | "repository\_full\_name: amthorn78/glow-hdengine-v2" | "default\_branch: main"  
* Repo | GitHub `compare_commits main..main` | "status: identical" | "base\_commit.sha: 3196a2b4029b05155e12d772ca24f9b3af129cae"  
* Repo | GitHub `compare_commits a05ed43dc013a5693ef8cf0c807498e6fcb559ed..main` | "ahead\_by: 1" | "files" included the OPS evidence files and retry trace.  
* Repo | GitHub `fetch_file` | OPS evidence files under `audit/ops/hde-epic035/ops-01/` and `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/` | files were readable.

Repo-resident evidence paths checked:

Artifact path or label: `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; produced as remediation mapping for Approved Plan deliverables.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt` | "Purpose: map approved-plan OPS-01 deliverable names to retained evidence paths without moving or deleting current evidence." | "v2\_charts\_simple=success" | "geokey\_header\_posture=proven\_for\_v2\_charts\_simple"

Artifact path or label: `audit/ops/hde-epic035/ops-01/files_sha256.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: Yes

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/files_sha256.txt` | "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2\_charts\_simple\_stdout.log" | "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor\_bodygraph\_dry\_run.json"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/commands.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: Yes, mapped from `audit/ops/hde-epic035/ops-01/commands.txt`

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/commands.txt` | "PO authorizes one bounded live production HumanDesignAPI geokey observation for HDE-EPIC035 OPS-01." | "Command: SAFE\_MODE=0 ALLOW\_NETWORK=1 LC\_ALL=C LANG=C TZ=UTC hdctl bg:resolve"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stdout.log`

Reported by Ops Evidence: Yes

Required by Approved Plan: Yes, mapped from `audit/ops/hde-epic035/ops-01/stdout.log`

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stdout.log` | "status=error" | "error\_code=PROVIDER\_NOT\_FOUND" | "error\_status=404"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stderr.log`

Reported by Ops Evidence: Yes

Required by Approved Plan: Yes, mapped from `audit/ops/hde-epic035/ops-01/stderr.log`

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stderr.log` | "no terminal stderr"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/exit_codes.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: Yes, mapped from `audit/ops/hde-epic035/ops-01/exit_codes.txt`

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/exit_codes.txt` | "hdctl bg:resolve \--user qa-user \--source vendor \--birthdate 1990-01-01 \--birthtime 12:00 \--location "Paris, FR" \--dry-run: 1" | "observed\_error\_code: PROVIDER\_NOT\_FOUND"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/redacted_env_presence.json`

Reported by Ops Evidence: Yes

Required by Approved Plan: Yes, mapped from `audit/ops/hde-epic035/ops-01/env_presence_redacted.json`

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/redacted_env_presence.json` | ""GEO\_API\_KEY": "present\_redacted"" | ""HD\_API\_BASE\_URL": "present\_redacted"" | ""HD\_API\_KEY": "present\_redacted""

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/request_summary.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: Yes, mapped from `audit/ops/hde-epic035/ops-01/request_summary.json`

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/request_summary.txt` | "HD-Geocode-Key: observed: not visible in retained keys-only retry log" | "Authorization: Bearer observed: not\_applicable\_to\_current\_bg\_resolve\_bodygraphs\_path" | "Observation status: vendor\_error\_class\_observed."

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/result_summary.md`

Reported by Ops Evidence: Yes

Required by Approved Plan: Yes, mapped from `audit/ops/hde-epic035/ops-01/result_summary.json`

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/result_summary.md` | "Result classification: `vendor_error_class_observed`" | "Final app result: `vendor_error_class`" | "Geokey behavior supportable from redacted evidence: partially bounded only."

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/session_summary_and_evidence.md`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; supplemental retained session summary.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/session_summary_and_evidence.md` | "has\_authorization=True" | "has\_hd\_geocode\_key=True" | "response\_type=ChartSimpleResult"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; produced to resolve final classification.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt` | "v2\_charts\_simple=success" | "geokey\_header\_posture=proven\_for\_v2\_charts\_simple" | "runtime\_gap=bg:resolve\_still\_uses\_legacy\_bodygraph\_route\_against\_configured\_v2\_base"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_repo_status.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; produced to complete final preservation status.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_repo_status.txt` | "Command: git status \--short \--untracked-files=all" | "Exit: 0" | "?? audit/ops/hde-epic035/ops-01/files\_sha256.txt"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_commands.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; produced to support v2 geokey remediation.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_commands.txt` | "Uses `Authorization: Bearer <redacted>`." | "Uses `HD-Geocode-Key: <redacted>`." | "Verifies `HD-Api-Key` is absent on the v2 chart path."

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; produced to support v2 geokey remediation.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log` | ""classification":"success"" | ""has\_authorization":true" | ""has\_hd\_geocode\_key":true"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stderr.log`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; produced to support v2 geokey remediation.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stderr.log` | "no terminal stderr"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_result_summary.txt`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; produced to support v2 geokey remediation.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_result_summary.txt` | "classification=success" | "authorization\_header\_shape=Authorization: Bearer " | "hd\_geocode\_key\_header\_shape=HD-Geocode-Key: "

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.json`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; supporting output for `bg:resolve` observation.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.json` | ""code":"PROVIDER\_NOT\_FOUND"" | ""status":404" | ""safe\_mode":false"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.stderr`

Reported by Ops Evidence: Yes

Required by Approved Plan: No

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | compare `a05ed43dc013a5693ef8cf0c807498e6fcb559ed..main` | "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor\_bodygraph\_dry\_run.stderr" | "status: added" | "additions: 0"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.json`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; diagnostic output.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.json` | ""code":"PROVIDER\_NOT\_FOUND"" | ""status":404" | ""safe\_mode":false"

Artifact path or label: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.stderr`

Reported by Ops Evidence: Yes

Required by Approved Plan: No

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed tracked

Evidence pointer: Repo | compare `a05ed43dc013a5693ef8cf0c807498e6fcb559ed..main` | "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor\_bodygraph\_dry\_run\_no\_version.stderr" | "status: added" | "additions: 0"

Artifact path or label: `artifacts/ingest/retry_trace.log`

Reported by Ops Evidence: Yes

Required by Approved Plan: No; supporting side-effect log.

Present in Repo: Yes

Tracked or mergeable: Yes

Allowed root: Yes

Content/proof facts checked: Yes

Repo validation status: Repo-confirmed modified tracked

Evidence pointer: Repo | `artifacts/ingest/retry_trace.log` | ""error\_code":"PROVIDER\_NOT\_FOUND"" | ""route":"vendor.hdapi.post:/bodygraphs"" | ""status":404"

Tracked or mergeable evidence confirmed:

* Repo-confirmed tracked: retained OPS evidence files under `audit/ops/hde-epic035/ops-01/`.  
* Repo-confirmed modified tracked: `artifacts/ingest/retry_trace.log`.

Reported evidence not found in Repo:

* None after remediation.

Evidence present but ignored or not mergeable:

* None observed.

Ops Evidence / Repo contradictions:

* None. Repo current `main` contains the evidence paths reported by Ops Evidence.  
* Ops Evidence contains an older `result_summary.md` with `vendor_error_class_observed` for `bg:resolve`, but this is clarified by `final_classification.txt`, `v2_charts_simple_result_summary.txt`, and `ops_evidence_manifest.txt`.

Findings

Finding ID: F-001

What you observed: OPS-01 evidence is present and mergeable in Repo under governed `audit/` and `artifacts/` roots.

Evidence pointer: Repo | compare `a05ed43dc013a5693ef8cf0c807498e6fcb559ed..main` | "audit/ops/hde-epic035/ops-01/files\_sha256.txt" | "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2\_charts\_simple\_stdout.log" | "artifacts/ingest/retry\_trace.log"

Expected requirement from Approved Plan: OPS evidence must be retained under `audit/ops/hde-epic035/ops-01/`, redacted, and suitable for PR-03 binding if OPS-01 executes.

Repo validation status, if repo-resident: Repo-confirmed tracked / Repo-confirmed modified tracked

Why it matters: Mergeability and governed-root placement are sufficient for later PR binding.

Blocker for acceptance: No

PF support, only if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

Canon proof excerpt, only if PF support is used: "Evidence artifacts MAY be stored across multiple governed roots." / "Source-of-truth payload artifacts MUST remain at their governed Evidence Catalog paths (`audit/` and `artifacts/`)."

Finding ID: F-002

What you observed: Approved Plan deliverable path/name mismatches remain, but the retained evidence manifest explicitly maps each planned deliverable to retained evidence and identifies supplemental files for partial original captures.

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt` | "map approved-plan OPS-01 deliverable names to retained evidence paths without moving or deleting current evidence" | "request\_summary.json | ... request\_summary.txt | partial\_format\_mismatch" | "result\_summary.json | ... result\_summary.md | partial\_format\_mismatch"

Expected requirement from Approved Plan: Planned output files include commands, stdout, stderr, exit codes, env presence, request summary, result summary, checksums, and later binding outputs.

Repo validation status, if repo-resident: Repo-confirmed tracked

Why it matters: The manifest makes the retained evidence reviewable and mergeable despite nested-root and format differences. The supplemental v2 files and final classification resolve the substantive proof gap.

Blocker for acceptance: No

PF support, only if relied on: PF12 — HDE-Schemas & Artifacts, §0.2 Scope & single homes

Canon proof excerpt, only if PF support is used: "Evidence artifacts MAY be stored across multiple governed roots." / "The Evidence Catalog defines the canonical, governed paths for evidence payload artifacts (typically under `audit/` and `artifacts/`)."

Finding ID: F-003

What you observed: The v2 `charts/simple` observation is now command-backed and proves the expected v2 geokey/auth posture.

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log` | ""classification":"success"" | ""authorization\_header\_shape":"Authorization: Bearer "" | ""hd\_geocode\_key\_header\_shape":"HD-Geocode-Key: ""

Expected requirement from Approved Plan: OPS evidence must identify provider behavior class without raw secret or raw payload leakage.

Repo validation status, if repo-resident: Repo-confirmed tracked

Why it matters: This closes the previous geokey proof gap for the v2 chart path.

Blocker for acceptance: No

PF support, only if relied on: PF10 — HDE Build Notes, §2.3.14 Vendor config and geokey syntax

Canon proof excerpt, only if PF support is used: "\* v2 `charts`, `charts/simple`, and `charts/coordinates` routes use `Authorization: Bearer`;" / "\* `charts` and `charts/simple` require geocode and therefore require `HD-Geocode-Key`;"

Finding ID: F-004

What you observed: The `bg:resolve` path remains a vendor error class observation, not a v2 geokey success path.

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt` | "bg\_resolve=vendor\_error\_class\_observed" | "bg\_resolve\_http\_status=404" | "runtime\_gap=bg:resolve\_still\_uses\_legacy\_bodygraph\_route\_against\_configured\_v2\_base"

Expected requirement from Approved Plan: OPS-01 contributes bounded provider-behavior evidence only and must not overclaim full conformance or PF09 status movement.

Repo validation status, if repo-resident: Repo-confirmed tracked

Why it matters: The evidence is acceptable as a classified runtime gap and provider error observation, but it must not be used as proof that `bg:resolve` is working for v2 geokey behavior.

Blocker for acceptance: No

PF support, only if relied on: PF10 — HDE Build Notes, §2.3.15 Production usage posture

Canon proof excerpt, only if PF support is used: "PF29 must warn that the current `bg:resolve` runtime path uses the current BodyGraph ingest path." / "It does not prove v2 ChartResult/ChartSimpleResult normalization into compat; PR-02 intentionally records that as a schema/adapter gap."

Finding ID: F-005

What you observed: Secret-safe and nonclaim posture is preserved.

Evidence pointer: Repo | `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt` | "- no QA PASS" | "- no PF09 status movement" | "- no raw payload persistence"

Expected requirement from Approved Plan: OPS action must not persist raw secrets, raw payload bodies, or claim QA/PF09/closeout status.

Repo validation status, if repo-resident: Repo-confirmed tracked

Why it matters: Prevents OPS evidence from becoming an overclaim.

Blocker for acceptance: No

PF support, only if relied on: PF04 — HDE Governance, §0.2 Scope & boundaries

Canon proof excerpt, only if PF support is used: "\* SAFE-rails posture and vendor HTTP policy." / "\* Logging & privacy requirements (keys-only logs; no secrets/PII)."

Finding ID: F-006

What you observed: PF09 support is evidence-only. The OPS evidence does not support PF09 status movement by itself.

Evidence pointer: Approved Plan | OPS-01 PF09 completion role | "PF09 completion role" | "Contributes evidence only." | Repo | `final_classification.txt` | "no PF09 status movement"

Expected requirement from Approved Plan: OPS-01 contributes evidence only; PR-03 owns later evidence-loop binding if OPS-01 executes.

Repo validation status, if repo-resident: Repo-confirmed tracked

Why it matters: Keeps OPS acceptance separate from PF09 status drainage and closeout.

Blocker for acceptance: No

PF support, only if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.5 \- Index v2 live conformance and close the evidence loop

Canon proof excerpt, only if PF support is used: "Update the Human Evidence Index, hash sentinel, Machine Mirror, and path-proof transcripts for all vendor v2 artifacts changed or produced by HDE-FERM006 through HDE-FERM008." / "Verify single mirror file, governed paths only, final LF, canonical JSON where applicable, and no stale path-proofs."

Evidence Print (PASS PROOF; required)

A) Required deliverables satisfied

Deliverable name: `audit/ops/hde-epic035/ops-01/commands.txt`

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "commands.txt | .../hdapi-v2-open-rails-smoke/commands.txt | equivalent\_by\_mapping"

Repo validation status, if repo-resident: Repo-confirmed tracked

Repo evidence pointer, if repo-resident: Repo | `.../commands.txt` | "PO authorizes one bounded live production HumanDesignAPI geokey observation" | "Command: SAFE\_MODE=0 ALLOW\_NETWORK=1 LC\_ALL=C LANG=C TZ=UTC hdctl bg:resolve"

Key proof facts: PO authorization, repo preflight, env presence probe, bg:resolve command, diagnostic rerun command.

Deliverable name: `audit/ops/hde-epic035/ops-01/stdout.log`

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "stdout.log | .../stdout.log | partial\_for\_bg\_resolve; supplemented by v2\_charts\_simple\_stdout.log"

Repo validation status, if repo-resident: Repo-confirmed tracked

Repo evidence pointer, if repo-resident: Repo | `.../stdout.log` | "status=error" | "error\_code=PROVIDER\_NOT\_FOUND" | "error\_status=404"

Key proof facts: bg:resolve stdout summary and error class; v2 stdout supplement proves chart/geokey success.

Deliverable name: `audit/ops/hde-epic035/ops-01/stderr.log`

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "stderr.log | .../stderr.log | equivalent\_by\_mapping for original bg:resolve capture"

Repo validation status, if repo-resident: Repo-confirmed tracked

Repo evidence pointer, if repo-resident: Repo | `.../stderr.log` | "no terminal stderr"

Key proof facts: No terminal stderr for main capture.

Deliverable name: `audit/ops/hde-epic035/ops-01/exit_codes.txt`

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "exit\_codes.txt | .../exit\_codes.txt | partial\_for\_bg\_resolve; supplemented by v2\_charts\_simple\_commands.txt"

Repo validation status, if repo-resident: Repo-confirmed tracked

Repo evidence pointer, if repo-resident: Repo | `.../exit_codes.txt` | "observed\_app\_flow: vendor\_error\_class\_observed" | "observed\_error\_code: PROVIDER\_NOT\_FOUND"

Key proof facts: bg:resolve exit `1`; v2 charts/simple exit `0` captured in supplemental command file.

Deliverable name: `audit/ops/hde-epic035/ops-01/env_presence_redacted.json`

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "env\_presence\_redacted.json | .../redacted\_env\_presence.json | equivalent\_by\_content\_name\_mismatch"

Repo validation status, if repo-resident: Repo-confirmed tracked

Repo evidence pointer, if repo-resident: Repo | `.../redacted_env_presence.json` | ""HD\_API\_BASE\_URL": "present\_redacted"" | ""HD\_API\_KEY": "present\_redacted"" | ""GEO\_API\_KEY": "present\_redacted""

Key proof facts: Required key names present as redacted/presence-only.

Deliverable name: `audit/ops/hde-epic035/ops-01/request_summary.json`

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "request\_summary.json | .../request\_summary.txt | partial\_format\_mismatch; supplemented by v2\_charts\_simple\_stdout.log and v2\_charts\_simple\_result\_summary.txt"

Repo validation status, if repo-resident: Repo-confirmed tracked

Repo evidence pointer, if repo-resident: Repo | `.../request_summary.txt` | "Route-family label or app flow label: hd\_engine\_cli\_open\_rails\_vendor\_bodygraph\_geocode\_dry\_run" | "Geocode behavior required: yes; sanitized input location=Paris, FR"

Key proof facts: Bounded request label, route-family posture, geocode requirement, sanitized input, redacted header posture.

Deliverable name: `audit/ops/hde-epic035/ops-01/result_summary.json`

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "result\_summary.json | .../result\_summary.md | partial\_format\_mismatch; supplemented by final\_classification.txt"

Repo validation status, if repo-resident: Repo-confirmed tracked

Repo evidence pointer, if repo-resident: Repo | `.../final_classification.txt` | "v2\_charts\_simple=success" | "geokey\_header\_posture=proven\_for\_v2\_charts\_simple" | "bg\_resolve=vendor\_error\_class\_observed"

Key proof facts: Final safe classification separates successful v2 geokey route from failing bg:resolve path.

Deliverable name: `audit/ops/hde-epic035/ops-01/files_sha256.txt`

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "files\_sha256.txt | audit/ops/hde-epic035/ops-01/files\_sha256.txt | produced\_by\_remediation"

Repo validation status, if repo-resident: Repo-confirmed tracked

Repo evidence pointer, if repo-resident: Repo | `audit/ops/hde-epic035/ops-01/files_sha256.txt` | "v2\_charts\_simple\_stdout.log" | "vendor\_bodygraph\_dry\_run.json"

Key proof facts: Checksum ledger covers retained OPS evidence files.

Deliverable name: Sibling path proofs for OPS artifacts if promoted into governed evidence

Evidence pointer: Approved Plan | OPS-01 Evidence outputs | "Planned output: sibling path proofs for each OPS artifact if promoted into governed evidence."

Repo validation status, if repo-resident: Not checked because OPS evidence has not yet been promoted into Human Evidence Index / Machine Mirror by PR-03.

Repo evidence pointer, if repo-resident: Not applicable.

Key proof facts: Not required before PR-03 binding.

Deliverable name: `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`

Evidence pointer: Approved Plan | OPS-01 Evidence outputs | "Planned output: `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`; created by later PR binding if OPS-01 executes."

Repo validation status, if repo-resident: Not checked because this is explicitly later PR binding output, not an OPS-01 execution output.

Repo evidence pointer, if repo-resident: Not applicable.

Key proof facts: Not required for OPS acceptance; PR-03 binding remains separate.

B) Commands/actions evidence

Evidence pointer: Ops Evidence | `commands.txt` | "PO authorizes one bounded live production HumanDesignAPI geokey observation for HDE-EPIC035 OPS-01."

Success signal found in evidence: Authorization recorded.

Repo validation status for repo-resident output: Repo-confirmed tracked.

Evidence pointer: Ops Evidence | `commands.txt` | "Command: SAFE\_MODE=0 ALLOW\_NETWORK=1 LC\_ALL=C LANG=C TZ=UTC hdctl bg:resolve \--user qa-user \--source vendor \--birthdate 1990-01-01 \--birthtime 12:00 \--location "Paris, FR" \--dry-run" | "Exit: 1"

Success signal found in evidence: Command executed and produced classified vendor error evidence.

Repo validation status for repo-resident output: Repo-confirmed tracked.

Evidence pointer: Ops Evidence | `v2_charts_simple_commands.txt` | "Uses `Authorization: Bearer <redacted>`." | "Uses `HD-Geocode-Key: <redacted>`." | "Exit code: 0"

Success signal found in evidence: v2 `charts/simple` command-backed observation exited 0 and produced success output.

Repo validation status for repo-resident output: Repo-confirmed tracked.

Evidence pointer: Ops Evidence | `final_repo_status.txt` | "Command: git status \--short \--untracked-files=all" | "Exit: 0"

Success signal found in evidence: Final preservation status captured.

Repo validation status for repo-resident output: Repo-confirmed tracked.

C) Configuration/infra state evidence, if applicable

Evidence pointer: Ops Evidence | `redacted_env_presence.json` | ""HD\_API\_BASE\_URL": "present\_redacted"" | ""HD\_API\_KEY": "present\_redacted"" | ""GEO\_API\_KEY": "present\_redacted""

Repo validation status, if repo-resident: Repo-confirmed tracked.

What state it proves: Required HumanDesignAPI base/key/geokey configuration names were present in redacted/presence-only form.

Evidence pointer: Ops Evidence | `session_summary_and_evidence.md` | "HD\_API\_BASE\_URL=[https://api.humandesignapi.nl/v2/](https://api.humandesignapi.nl/v2/)" | "HD\_API\_BASE\_URL=present\_redacted" | "GEO\_API\_KEY=present\_redacted"

Repo validation status, if repo-resident: Repo-confirmed tracked.

What state it proves: Active configured vendor base was the v2 base, and secret-bearing keys were present without recording secret values.

D) PF09.x later-drain support, only if Approved Plan ties this OPS task to PF09.x completion, close, or later-drain posture

PF09.x document: PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.4

PF09.x task ID: HDE-FERM008

PF09.x subtask ID, if any: HDE-FERM008.3

Current claim in Approved Plan: OPS-01 contributes evidence only if live observation is needed.

Supportable later-drain action: no PF09.x support proven

Evidence basis: `bg:resolve` produced a provider error class observation; v2 `charts/simple` provider observation supports bounded live provider/geokey behavior but does not itself update PF09 status.

Repo validation status for repo-resident evidence: Repo-confirmed tracked.

Notes: OPS-01 evidence may be bound later by PR-03; no PF09 status movement is supported from OPS alone.

PF09.x document: PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.4

PF09.x task ID: HDE-FERM008

PF09.x subtask ID, if any: HDE-FERM008.4

Current claim in Approved Plan: OPS-01 contributes evidence only if live observation is needed.

Supportable later-drain action: no PF09.x support proven

Evidence basis: v2 `charts/simple` shows successful provider response and header posture, but does not prove v2 ChartResult / ChartSimpleResult normalization into existing BodyGraph/cache/compat flow; current final classification preserves the runtime gap.

Repo validation status for repo-resident evidence: Repo-confirmed tracked.

Notes: No normalized-data-path proof or HDE-FERM008.4 status action is supported by OPS alone.

PF09.x document: PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.4

PF09.x task ID: HDE-FERM008

PF09.x subtask ID, if any: HDE-FERM008.5

Current claim in Approved Plan: OPS-01 contributes evidence only; PR-03 owns governed evidence-loop closure if OPS evidence is produced.

Supportable later-drain action: no PF09.x support proven

Evidence basis: OPS evidence is present and mergeable, but Human Evidence Index, Machine Mirror, hash sentinel, and path-proof binding remain PR-03 work.

Repo validation status for repo-resident evidence: Repo-confirmed tracked.

Notes: HDE-FERM008.5 is not completed by OPS-01.

Doc Deltas (PF-Canon only; REQUIRED in OPS ACCEPTABLE branch)

Doc Delta Detection Workflow

CHG-001

Evidence pointer: Ops Evidence | `final_classification.txt` | "runtime\_gap=bg:resolve\_still\_uses\_legacy\_bodygraph\_route\_against\_configured\_v2\_base" | "bg\_resolve\_http\_status=404"

Canon basis: CANON AMBIGUITY/CONFLICT

CHG-002

Evidence pointer: Ops Evidence | `v2_charts_simple_stdout.log` | ""route":"vendor.hdapi.post:/charts/simple"" | ""classification":"success"" | ""has\_hd\_geocode\_key":true"

Canon basis: CANON ALIGNED

CHG-003

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "request\_summary.json | ... request\_summary.txt | partial\_format\_mismatch" | "result\_summary.json | ... result\_summary.md | partial\_format\_mismatch"

Canon basis: CANON SILENCE

CHG: CHG-001

Doc: PF10 — HDE Build Notes

Section: §2.3.15 Production usage posture

Canon basis: CANON AMBIGUITY/CONFLICT

Delta: Clarify the PF29 seed before drainage: `hdctl bg:resolve --source vendor` is an open-rails legacy BodyGraph ingest-path observation and may return `PROVIDER_NOT_FOUND` when `HD_API_BASE_URL` is the v2 base. It must not be presented as the canonical v2 chart/geokey validation path. For v2 chart/geokey header posture, use a v2 `charts` or `charts/simple` observation that records `Authorization: Bearer <redacted>`, `HD-Geocode-Key: <redacted>`, and legacy `HD-Api-Key` absent.

Why: OPS-01 proved that `bg:resolve` builds `/v2/bodygraphs` against the v2 base and fails with 404, while the v2 `charts/simple` route succeeds and proves the intended header posture. The current PF10 production recipe still lists `hdctl bg:resolve --source vendor` under production/open-rails vendor BodyGraph acquisition, which is true as BodyGraph ingest-path documentation but unsafe as a geokey validation instruction unless the limitation is explicit.

Evidence pointer: Ops Evidence | `final_classification.txt` | "runtime\_gap=bg:resolve\_still\_uses\_legacy\_bodygraph\_route\_against\_configured\_v2\_base" | "v2\_charts\_simple=success" | "geokey\_header\_posture=proven\_for\_v2\_charts\_simple"

Canon proof excerpt: "`SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user <approved-user-or-test-id> --source vendor --birthdate YYYY-MM-DD --birthtime HH:MM --location \"Place\" --dry-run`" / "PF29 must warn that the current `bg:resolve` runtime path uses the current BodyGraph ingest path." / "It does not prove v2 ChartResult/ChartSimpleResult normalization into compat; PR-02 intentionally records that as a schema/adapter gap."

CHG: CHG-003

Doc: PF29 — HDE User Guide

Section: §OPS/live evidence deliverable conventions

Canon basis: CANON SILENCE

Delta: NEW CANON PROPOSAL: PF29 should document that OPS evidence may retain a nested evidence root such as `audit/ops/<epic-id>/<ops-id>/<run-label>/` when accompanied by a manifest mapping approved deliverable names to retained evidence paths. PF29 should also prefer JSON only when the approved task requires machine-readable JSON semantics; otherwise text/markdown summaries must be explicitly mapped and not treated as schema-governed JSON.

Why: OPS-01 retained reviewable evidence under a nested smoke-root and used an evidence manifest to map planned outputs to retained files. This was acceptable for reviewability, but PF29 should prevent future ambiguity about whether exact root-level filenames are required or whether mapped nested roots are acceptable.

Evidence pointer: Ops Evidence | `ops_evidence_manifest.txt` | "Purpose: map approved-plan OPS-01 deliverable names to retained evidence paths without moving or deleting current evidence." | "equivalent\_by\_mapping; nested smoke-root retained"

DECISION: OPS ACCEPTABLE

## 2.5) PR-03 HDE-EPIC035

Artifact Map

PR Name: PR-03

Merged PR Ref: 333

Approved Plan: r1 Implementation Plan HDE-EPIC035.md

Optional PR Artifacts: provided

Repo root reviewed: current @GitHub / amthorn78/glow-hdengine-v2

Output: Post-Merge PR Code Review and Validation

Review Summary

* The merged change binds HDE-EPIC035 PR-01, PR-02, and retained OPS-01 evidence into the governed PR-03 evidence-loop closure surface for HDE-FERM008.5.  
* The merged change aligns with the Approved Plan’s PR-03 scope: Human Evidence Index, Machine Mirror, hash sentinels, path proofs, acceptance-boundary artifacts, token evidence matrix, OPS evidence binding, and doc-delta candidates were added or refreshed.  
* The merged change preserves required boundaries: no OPS rerun, no live vendor call by PR-03, no PF-Canon edit, no QA PASS claim, no OPS completion claim, no PF09 status movement claim, no HDE-FERM008 parent Done claim, no full v2 runtime-conformance claim, and no public-surface change claim.  
* PR review comments identified two tooling risks, and final repo state shows both were addressed: the v2 stdout guard now requires `legacy_hd_api_key_on_v2_path is False` and `has_hd_api_key is False`, and retained OPS checksum ledger validation now fails closed on missing or mismatched hashes. Repo proof: GitHub file inspection → `tools/evidence/update_evidence_index.py` lines 17-25 and 43-57.  
* Optional PR Artifacts report targeted validation as passing: 316 existing evidence tests, 5 PR-03 evidence-loop tests, evidence index update/check, orientation update/check, path validation, mirror schema check, evidence index hash check, and `git diff --check`; no validation was intentionally skipped.  
* Current repo evidence supports HDE-FERM008.5 as supportable for a later PF09 status change to Done, but the merged change itself correctly does not edit PF09 or claim PF09 status movement.  
* Remaining risk is documentation drainage only: PF29 and PF09 status-delta candidates should be drained later, but documentation drainage is not a post-merge remediation blocker.

Repo Inspection

Observed repo root:

Repo proof: GitHub repository metadata → `amthorn78/glow-hdengine-v2`; default branch `main`.

Observed HEAD:

Repo proof: GitHub compare `824953bf8c8b16bcc8e89b1c6f722b1f6080b73f..main` → `status: identical`, `ahead_by: 0`, `behind_by: 0`.

Branch or detached state:

Repo proof: GitHub repository metadata and compare → reviewed current default branch `main`; no mutable local checkout was used.

Working tree status before review:

Repo proof: GitHub read-only inspection only; no local mutable working tree available. PR merge commit and current `main` were identical by compare.

How MERGED\_PR\_REF was resolved:

Repo proof: GitHub PR metadata → PR \#333 is closed and merged, title is `Bind HDE-EPIC035 PR-03 evidence loop (HDE-FERM008.5)`, base is `main`, head is `codex/implement-hde-ferm008.5-evidence-loop-closure`, and merge commit is `824953bf8c8b16bcc8e89b1c6f722b1f6080b73f`.

Changed files reviewed:

59 changed files were reviewed from the PR changed-file list:  
`artifacts/evidence_index.jsonl`; `artifacts/evidence_index.jsonl.path_proof.txt`; `artifacts/evidence_index.jsonl.sha256`; `artifacts/evidence_index.jsonl.sha256.path_proof.txt`; `artifacts/ingest/retry_trace.log.path_proof.txt`; `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; `artifacts/narratives/router/parity_abba.log.path_proof.txt`; `artifacts/writer/conjunction_write_readback.log.path_proof.txt`; `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`; `audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; `audit/docdeltas/hde-epic035_doc_deltas.md`; `audit/docdeltas/hde-epic035_doc_deltas.md.path_proof.txt`; `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`; `audit/gates/narratives/pack_identity.txt.path_proof.txt`; `audit/gates/narratives/registry.diff.json.path_proof.txt`; `audit/gates/topology/orientation_demo.txt`; `audit/gates/topology/orientation_demo.txt.path_proof.txt`; `audit/ops/hde-epic035/ops-01/files_sha256.txt.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/exit_codes.txt.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/request_summary.txt.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/result_summary.md.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stderr.log.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stdout.log.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_commands.txt.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_result_summary.txt.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stderr.log.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.json.path_proof.txt`; `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.json.path_proof.txt`; `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt.path_proof.txt`; `audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`; `audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`; `audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`; `audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; `audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt`; `audit/qa/hde-epic035/00_meta/doc_deltas.md`; `audit/qa/hde-epic035/00_meta/doc_deltas.md.path_proof.txt`; `audit/qa/hde-epic035/acceptance_map_viability.log`; `audit/qa/hde-epic035/acceptance_map_viability.log.path_proof.txt`; `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`; `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log.path_proof.txt`; `audit/qa/hde-epic035/token_evidence_matrix.md`; `audit/qa/hde-epic035/token_evidence_matrix.md.path_proof.txt`; `docs/acceptance_map_epic035.json`; `docs/acceptance_map_epic035.json.path_proof.txt`; `docs/evidence/INDEX.json`; `docs/evidence/INDEX.json.path_proof.txt`; `docs/evidence/INDEX.sha256`; `docs/evidence/INDEX.sha256.path_proof.txt`; `tests/evidence/test_hde_epic035_pr03_evidence_loop.py`; `tools/evidence/update_evidence_index.py`.

Working tree status after validation:

Repo proof: GitHub read-only inspection only; no commands mutated the repo. Current `main` remains identical to merge commit `824953bf8c8b16bcc8e89b1c6f722b1f6080b73f`.

Changed File Review

CFR-001

File: `artifacts/evidence_index.jsonl`

Change summary: Machine Mirror rows refreshed and expanded to include HDE-EPIC035 PR-03 acceptance-boundary artifacts and retained OPS-01 evidence.

Risk assessment: High

Code review assessment: Sound. This is a governed machine ledger change; final tooling and tests assert parity, path proofs, and current SHA values.

Approved Plan linkage: PR-03 required Machine Mirror update for HDE-FERM008.5 evidence-loop closure.

Repo proof: Repo proof: PR diff / current file inspection → `artifacts/evidence_index.jsonl` changed and current mirror includes EPIC035 PR-03 rows. Search method: searched Repo for `epic035.pr03.acceptance_map` and `epic035.ops01.v2_charts_simple_stdout` (case: sensitive); scope: current repository; tool: GitHub search; result: 2 hits.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-002

File: `artifacts/evidence_index.jsonl.path_proof.txt`

Change summary: Refreshed path proof for the Machine Mirror.

Risk assessment: Medium

Code review assessment: Sound; required by governed mirror/path-proof posture.

Approved Plan linkage: PR-03 required Machine Mirror path-proof refresh.

Repo proof: Repo proof: PR changed-file list → path proof file changed; current repo fetch confirmed sibling mirror proof path exists.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-003

File: `artifacts/evidence_index.jsonl.sha256`

Change summary: Refreshed Machine Mirror hash sentinel.

Risk assessment: Medium

Code review assessment: Sound; hash sentinel update is expected after mirror refresh.

Approved Plan linkage: PR-03 required Machine Mirror hash sentinel update.

Repo proof: Repo proof: PR changed-file list → hash sentinel changed; validation artifacts claim mirror/hash checks passed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-004

File: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Change summary: Refreshed path proof for Machine Mirror hash sentinel.

Risk assessment: Medium

Code review assessment: Sound; generated proof sibling matches governed artifact pattern.

Approved Plan linkage: PR-03 required path proofs for changed hash sentinels.

Repo proof: Repo proof: PR changed-file list → path proof changed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-005

File: `artifacts/ingest/retry_trace.log.path_proof.txt`

Change summary: Refreshed path proof for existing retry trace after OPS evidence touched `artifacts/ingest/retry_trace.log`.

Risk assessment: Medium

Code review assessment: Sound; binds existing modified tracked OPS side-effect log into path-proof posture.

Approved Plan linkage: PR-03 required path-proof coherence for retained OPS evidence artifacts when bound.

Repo proof: Repo proof: current file inspection → retry trace retains `PROVIDER_NOT_FOUND` / 404 proof and path proof was changed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-006

File: `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`

Change summary: Refreshed existing path proof due evidence tooling refresh.

Risk assessment: Low

Code review assessment: Presentation/path-proof timestamp refresh only; no executable narrative behavior changed.

Approved Plan linkage: Indirect evidence-tool refresh; allowed when governed tooling refreshes existing stale proofs.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-007

File: `artifacts/narratives/router/parity_abba.log.path_proof.txt`

Change summary: Refreshed existing path proof due evidence tooling refresh.

Risk assessment: Low

Code review assessment: Sound; no behavior change.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-008

File: `artifacts/writer/conjunction_write_readback.log.path_proof.txt`

Change summary: Refreshed existing writer evidence path proof.

Risk assessment: Low

Code review assessment: Sound; path-proof-only refresh.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-009

File: `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`

Change summary: Refreshed existing writer summary path proof.

Risk assessment: Low

Code review assessment: Sound; path-proof-only refresh.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-010

File: `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC032 doc-delta path proof.

Risk assessment: Low

Code review assessment: Sound; no content evidence change detected in reviewed scope.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-011

File: `audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC034 doc-delta path proof.

Risk assessment: Low

Code review assessment: Sound; no PR-03 scope drift.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-012

File: `audit/docdeltas/hde-epic035_doc_deltas.md`

Change summary: Added HDE-EPIC035 PR-03 doc-delta candidates for PF29 guidance.

Risk assessment: Medium

Code review assessment: Sound; records candidates without editing PF-Canon and preserves nonclaims.

Approved Plan linkage: PR-03 allowed doc-delta candidate artifacts if process required same-PR drift capture.

Repo proof: Repo proof: GitHub file inspection → `audit/docdeltas/hde-epic035_doc_deltas.md` says PF29 should clarify `bg:resolve` is not the canonical v2 chart/geokey validation path and that PF-Canon was not edited.

PF reference, if relied on: PF06 — HDE Epic Process Guide, §0.2 Policy and principles.

CFR-013

File: `audit/docdeltas/hde-epic035_doc_deltas.md.path_proof.txt`

Change summary: Added path proof for HDE-EPIC035 doc-delta candidate artifact.

Risk assessment: Low

Code review assessment: Sound; required proof sibling exists.

Approved Plan linkage: PR-03 path-proof posture for new governed artifacts.

Repo proof: Repo proof: PR changed-file list → path proof added.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-014

File: `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`

Change summary: Refreshed existing narrative gate path proof via evidence tooling.

Risk assessment: Low

Code review assessment: Sound; no HDE-EPIC035 behavior change.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-015

File: `audit/gates/narratives/pack_identity.txt.path_proof.txt`

Change summary: Refreshed existing narrative pack identity path proof.

Risk assessment: Low

Code review assessment: Sound; no behavior change.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-016

File: `audit/gates/narratives/registry.diff.json.path_proof.txt`

Change summary: Refreshed existing narrative registry path proof.

Risk assessment: Low

Code review assessment: Sound; no HDE-EPIC035 scope drift.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-017

File: `audit/gates/topology/orientation_demo.txt`

Change summary: Refreshed orientation demo artifact through governed evidence tooling.

Risk assessment: Low

Code review assessment: Sound; expected when `orientation_demo.py` is run with evidence refresh.

Approved Plan linkage: PR-03 validation included orientation demo update/check when repo workflow required it.

Repo proof: Repo proof: PR body reports orientation demo update/check; PR changed-file list includes artifact.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-018

File: `audit/gates/topology/orientation_demo.txt.path_proof.txt`

Change summary: Refreshed path proof for orientation demo.

Risk assessment: Low

Code review assessment: Sound; proof sibling refresh follows changed artifact.

Approved Plan linkage: PR-03 evidence-tool validation.

Repo proof: Repo proof: PR changed-file list → path proof changed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-019

File: `audit/ops/hde-epic035/ops-01/files_sha256.txt.path_proof.txt`

Change summary: Added path proof for retained OPS-01 checksum ledger.

Risk assessment: Medium

Code review assessment: Sound; supports later binding of retained OPS evidence.

Approved Plan linkage: PR-03 required OPS-01 evidence path proofs if OPS-01 executed.

Repo proof: Repo proof: `tools/evidence/update_evidence_index.py` now parses and validates OPS checksum ledger before indexing.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-020

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/exit_codes.txt.path_proof.txt`

Change summary: Added path proof for retained OPS-01 exit-code evidence.

Risk assessment: Medium

Code review assessment: Sound; retained evidence only, no OPS rerun.

Approved Plan linkage: PR-03 must bind retained OPS outputs if produced.

Repo proof: Repo proof: current OPS binding log says retained OPS root and checksum ledger are bound; no OPS rerun.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-021

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt.path_proof.txt`

Change summary: Added path proof for final OPS-01 classification.

Risk assessment: Medium

Code review assessment: Sound; final classification separates v2 success from `bg:resolve` runtime gap.

Approved Plan linkage: PR-03 required truthful retained OPS binding and no overclaim.

Repo proof: Repo proof: `tools/evidence/update_evidence_index.py` validates `final_classification` contains `v2_charts_simple=success`, `bg_resolve_http_status=404`, and `runtime_gap=` before indexing.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

CFR-022

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/request_summary.txt.path_proof.txt`

Change summary: Added path proof for retained OPS-01 request summary.

Risk assessment: Medium

Code review assessment: Sound; supports retained evidence mapping.

Approved Plan linkage: PR-03 binds retained OPS evidence if produced.

Repo proof: Repo proof: `docs/acceptance_map_epic035.json` references the retained request summary path.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-023

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/result_summary.md.path_proof.txt`

Change summary: Added path proof for retained OPS-01 result summary.

Risk assessment: Medium

Code review assessment: Sound; result summary remains evidence only and not PF09 movement.

Approved Plan linkage: PR-03 retained OPS binding.

Repo proof: Repo proof: `docs/acceptance_map_epic035.json` references the retained result summary path.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-024

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stderr.log.path_proof.txt`

Change summary: Added path proof for retained OPS-01 stderr log.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: PR-03 retained OPS evidence proof.

Repo proof: Repo proof: `ops_evidence_binding.log` records retained OPS root and related outputs.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-025

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stdout.log.path_proof.txt`

Change summary: Added path proof for retained OPS-01 stdout log.

Risk assessment: Medium

Code review assessment: Sound; stdout supports `bg:resolve` provider-error/runtime-gap posture, not success.

Approved Plan linkage: PR-03 retained OPS evidence proof.

Repo proof: Repo proof: `tools/evidence/update_evidence_index.py` notes bg:resolve stdout is provider-error/runtime-gap evidence, not success.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

CFR-026

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_commands.txt.path_proof.txt`

Change summary: Added path proof for v2 charts/simple command transcript.

Risk assessment: Medium

Code review assessment: Sound; proof binds command-backed OPS evidence without rerun.

Approved Plan linkage: PR-03 retained OPS evidence binding.

Repo proof: Repo proof: `ops_evidence_binding.log` records v2 charts/simple success evidence path and no OPS rerun.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

CFR-027

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_result_summary.txt.path_proof.txt`

Change summary: Added path proof for v2 charts/simple result summary.

Risk assessment: Medium

Code review assessment: Sound; binds header posture evidence.

Approved Plan linkage: PR-03 retained OPS evidence binding.

Repo proof: Repo proof: `ops_evidence_binding.log` records result-summary path and header shapes.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

CFR-028

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stderr.log.path_proof.txt`

Change summary: Added path proof for v2 charts/simple stderr log.

Risk assessment: Low

Code review assessment: Sound; retained stderr artifact is governed.

Approved Plan linkage: PR-03 retained OPS proof.

Repo proof: Repo proof: `tools/evidence/update_evidence_index.py` includes this artifact in PR-03 OPS evidence rows.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-029

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log.path_proof.txt`

Change summary: Added path proof for v2 charts/simple stdout log.

Risk assessment: High

Code review assessment: Sound; update tooling validates parsed JSON fields and fails closed on legacy header regression.

Approved Plan linkage: PR-03 retained OPS v2 geokey success proof.

Repo proof: Repo proof: `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` asserts header shapes, `legacy_hd_api_key_on_v2_path is False`, `has_hd_api_key is False`, and no raw secret/request/response/vendor payload persistence.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

CFR-030

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.json.path_proof.txt`

Change summary: Added path proof for bg:resolve dry-run provider-error output.

Risk assessment: Medium

Code review assessment: Sound; output is bound as runtime gap/provider error, not success.

Approved Plan linkage: PR-03 retained OPS binding.

Repo proof: Repo proof: `tools/evidence/update_evidence_index.py` labels this as bg:resolve dry-run provider-error/runtime-gap evidence.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

CFR-031

File: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.json.path_proof.txt`

Change summary: Added path proof for diagnostic no-version bg:resolve output.

Risk assessment: Medium

Code review assessment: Sound; bound as diagnostic provider-error/runtime-gap evidence.

Approved Plan linkage: PR-03 retained OPS binding.

Repo proof: Repo proof: `tools/evidence/update_evidence_index.py` includes the no-version dry-run artifact as retained evidence.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

CFR-032

File: `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt.path_proof.txt`

Change summary: Added path proof for retained OPS evidence manifest.

Risk assessment: Medium

Code review assessment: Sound; manifest resolves nested evidence-root mapping.

Approved Plan linkage: PR-03 retained OPS evidence binding.

Repo proof: Repo proof: `tools/evidence/update_evidence_index.py` includes `epic035.ops01.ops_evidence_manifest`.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-033

File: `audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound; unrelated proof refresh from evidence tooling.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-034

File: `audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-035

File: `audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-036

File: `audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-037

File: `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-038

File: `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-039

File: `audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-040

File: `audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-041

File: `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC030 path proof.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-042

File: `audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`

Change summary: Refreshed existing HDE-EPIC034 QA meta doc-delta path proof.

Risk assessment: Low

Code review assessment: Sound; no PR-03 content drift.

Approved Plan linkage: Indirect evidence-tool refresh.

Repo proof: Repo proof: PR changed-file list → path proof refreshed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-043

File: `audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt`

Change summary: Refreshed existing EPIC034 response-mapping check-log path proof.

Risk assessment: Medium

Code review assessment: Sound; important because PR-02 remediation preserved this distinct EPIC034 row, and PR-03 tooling retains PR-02 loader logic.

Approved Plan linkage: Preserve existing evidence while adding PR-03 loader.

Repo proof: Repo proof: `tools/evidence/update_evidence_index.py` preserves EPIC035 PR-02 loader after EPIC034 PR-06 loaders and before PR-03 loader.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-044

File: `audit/qa/hde-epic035/00_meta/doc_deltas.md`

Change summary: Added QA meta doc-delta candidate artifact for HDE-EPIC035.

Risk assessment: Medium

Code review assessment: Sound; current-epic doc-delta surface records candidate only and no PF-Canon edit.

Approved Plan linkage: Conditional doc-delta candidate output.

Repo proof: Repo proof: PR changed-file list and update tooling include `epic035.pr03.qa_meta_doc_deltas`.

PF reference, if relied on: PF06 — HDE Epic Process Guide, §0.2 Policy and principles.

CFR-045

File: `audit/qa/hde-epic035/00_meta/doc_deltas.md.path_proof.txt`

Change summary: Added path proof for QA meta doc-delta artifact.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Conditional doc-delta path proof.

Repo proof: Repo proof: PR changed-file list → path proof added.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-046

File: `audit/qa/hde-epic035/acceptance_map_viability.log`

Change summary: Added mechanical viability log for acceptance map.

Risk assessment: Medium

Code review assessment: Sound; explicitly not QA plan or Live QA runbook.

Approved Plan linkage: Required PR-03 output.

Repo proof: Repo proof: GitHub file inspection → viability log records canonical JSON expectation, allowed token set, no forbidden vendor-v2-specific tokens, nonclaims, and no PF-canon edit requirement.

PF reference, if relied on: PF04 — HDE Governance, §0.2 Scope & boundaries.

CFR-047

File: `audit/qa/hde-epic035/acceptance_map_viability.log.path_proof.txt`

Change summary: Added path proof for viability log.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Required PR-03 path proof.

Repo proof: Repo proof: PR changed-file list → path proof added.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-048

File: `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`

Change summary: Added PR-03 binding log for retained OPS-01 evidence.

Risk assessment: High

Code review assessment: Sound; binds retained evidence without rerunning OPS and records critical nonclaims.

Approved Plan linkage: Required if OPS-01 executed.

Repo proof: Repo proof: GitHub file inspection → binding log records `ops_rerun=false`, `live_vendor_call_by_pr03=false`, v2 header shapes, legacy key absent, runtime gap, and nonclaims.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

CFR-049

File: `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log.path_proof.txt`

Change summary: Added path proof for OPS evidence binding log.

Risk assessment: Medium

Code review assessment: Sound.

Approved Plan linkage: Required path proof for PR-03 OPS binding artifact.

Repo proof: Repo proof: PR changed-file list → path proof added.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-050

File: `audit/qa/hde-epic035/token_evidence_matrix.md`

Change summary: Added compact token evidence matrix.

Risk assessment: High

Code review assessment: Sound; uses existing token names only and preserves nonclaims.

Approved Plan linkage: Required PR-03 output with no vendor-v2-specific invented token.

Repo proof: Repo proof: GitHub file inspection → matrix lists token rows for `DOC_DELTA_PRESENT_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_PATH_PROOFS_OK`, `JSON_CANONICAL_CHECK_OK`, and `TESTS_PASS_OK`; it separates PR-01, PR-02, OPS-01, and PR-03 roles.

PF reference, if relied on: PF04 — HDE Governance, §0.2 Scope & boundaries.

CFR-051

File: `audit/qa/hde-epic035/token_evidence_matrix.md.path_proof.txt`

Change summary: Added path proof for token evidence matrix.

Risk assessment: Low

Code review assessment: Sound.

Approved Plan linkage: Required path proof for acceptance-boundary artifact.

Repo proof: Repo proof: PR changed-file list → path proof added.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-052

File: `docs/acceptance_map_epic035.json`

Change summary: Added canonical acceptance map for HDE-EPIC035 PR-03.

Risk assessment: High

Code review assessment: Sound; canonical JSON, allowed existing tokens only, referenced evidence paths, explicit nonclaims, and no vendor-v2-specific token.

Approved Plan linkage: Required PR-03 output.

Repo proof: Repo proof: GitHub file inspection → acceptance map records `acceptance_claims_mode:"baseline_existing_tokens_only"`, HDE-FERM008.5 evidence-loop scope, required nonclaims, referenced PR-01/PR-02/OPS-01/PR-03 evidence paths, and only allowed token names.

PF reference, if relied on: PF04 — HDE Governance, §0.2 Scope & boundaries; PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-053

File: `docs/acceptance_map_epic035.json.path_proof.txt`

Change summary: Added path proof for acceptance map.

Risk assessment: Medium

Code review assessment: Sound; proof binds path, size, SHA-256, mtime, and produced-at posture.

Approved Plan linkage: Required PR-03 path proof.

Repo proof: Repo proof: GitHub file inspection → path proof records `path: docs/acceptance_map_epic035.json`, `size_bytes: 6305`, and SHA-256.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-054

File: `docs/evidence/INDEX.json`

Change summary: Refreshed Human Evidence Index with PR-01, PR-02, retained OPS-01, and PR-03 evidence rows.

Risk assessment: High

Code review assessment: Sound; tests assert Human Index / Machine Mirror parity and required HDE-EPIC035 paths.

Approved Plan linkage: Required PR-03 Human Evidence Index update.

Repo proof: Repo proof: `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` asserts required HDE-EPIC035 paths are present in Human Index and Mirror.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-055

File: `docs/evidence/INDEX.json.path_proof.txt`

Change summary: Refreshed Human Evidence Index path proof.

Risk assessment: Medium

Code review assessment: Sound.

Approved Plan linkage: Required PR-03 Human Evidence Index path-proof refresh.

Repo proof: Repo proof: PR changed-file list → path proof changed; tests assert path-proof existence and SHA matching for required evidence paths.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-056

File: `docs/evidence/INDEX.sha256`

Change summary: Refreshed Human Evidence Index hash sentinel.

Risk assessment: Medium

Code review assessment: Sound; required after Index update.

Approved Plan linkage: Required PR-03 hash sentinel update.

Repo proof: Repo proof: PR body says evidence index hash check passed; changed-file list includes hash sentinel.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-057

File: `docs/evidence/INDEX.sha256.path_proof.txt`

Change summary: Refreshed Human Evidence Index hash path proof.

Risk assessment: Medium

Code review assessment: Sound.

Approved Plan linkage: Required PR-03 path-proof refresh.

Repo proof: Repo proof: PR changed-file list → path proof changed.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-058

File: `tests/evidence/test_hde_epic035_pr03_evidence_loop.py`

Change summary: Added targeted PR-03 evidence-loop tests.

Risk assessment: High

Code review assessment: Sound; tests cover canonical JSON, token allowlist, nonclaims, retained OPS paths, v2 header posture, legacy-key rejection, raw-payload nonpersistence, index/mirror parity, path proofs, and checksum ledger validation.

Approved Plan linkage: Required targeted validation for PR-03 evidence-loop closure.

Repo proof: Repo proof: GitHub file inspection → test file imports update-tool guards, checks allowed tokens and nonclaims, validates OPS paths and header flags, checks index/mirror parity, rejects legacy key regression, and validates checksum ledger.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

CFR-059

File: `tools/evidence/update_evidence_index.py`

Change summary: Extended evidence-index tooling with HDE-EPIC035 PR-03 OPS/artifact rows, PR-03 loader, allowed-token/nonclaim checks, v2 stdout parsed guard, checksum-ledger validation, required-artifact existence checks, and loader registration.

Risk assessment: High

Code review assessment: Sound. The earlier PR review issues were addressed in final code: parsed stdout validates legacy key absence as boolean false, and checksum ledger validation verifies missing/mismatched hashes before indexing.

Approved Plan linkage: Required to update Human Evidence Index, Machine Mirror, path-proof, and acceptance-boundary artifacts without duplicating or weakening PR-01/PR-02 evidence.

Repo proof: Repo proof: GitHub file inspection → PR-01/PR-02 loaders remain intact; PR-03 rows are added; `_epic035_ops01_v2_stdout_is_valid` and `_validate_epic035_ops01_checksums` fail closed; `_load_epic035_pr03_entries` validates acceptance tokens, required nonclaims, final classification, stdout JSON, checksum ledger, and required artifact existence.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

Validation Results

VAL-001

Purpose: Confirm merged PR state and exact merged change set.

Command or method: GitHub PR metadata and PR changed-file list inspection.

Result: PASS

Key output or observation: PR \#333 is `state: closed`, `merged: true`, `merge_commit_sha: 824953bf8c8b16bcc8e89b1c6f722b1f6080b73f`, and has 59 changed files.

Why it matters: Establishes the exact merged change set for post-merge review.

VAL-002

Purpose: Confirm current repo state matches merged commit.

Command or method: GitHub compare `824953bf8c8b16bcc8e89b1c6f722b1f6080b73f..main`.

Result: PASS

Key output or observation: Compare returned `status: identical`, `ahead_by: 0`, `behind_by: 0`.

Why it matters: Confirms final reviewed files are the current merged state.

VAL-003

Purpose: Evaluate reported test suite and evidence-tool validation.

Command or method: Optional PR Artifacts and PR body inspection.

Result: PASS

Key output or observation: Optional PR Artifacts and PR body report 316 existing evidence tests passed, 5 PR-03 evidence-loop tests passed, evidence index update/check, orientation update/check, evidence path validation, mirror schema check, evidence index hash check, and `git diff --check`; no validation was intentionally skipped.

Why it matters: Shows targeted validation was performed for the evidence-loop closure slice.

VAL-004

Purpose: Inspect final PR-03 test coverage.

Command or method: GitHub file inspection of `tests/evidence/test_hde_epic035_pr03_evidence_loop.py`.

Result: PASS

Key output or observation: Tests assert allowed token names, required nonclaims, retained OPS paths, v2 header posture, legacy-key absence, raw-payload nonpersistence, Human Index/Machine Mirror parity, path-proof existence, and checksum-ledger correctness.

Why it matters: The tests directly cover the high-risk evidence-loop behavior.

VAL-005

Purpose: Inspect final evidence-index guard behavior.

Command or method: GitHub file inspection of `tools/evidence/update_evidence_index.py`.

Result: PASS

Key output or observation: The loader validates allowed tokens, required nonclaims, final OPS classification, parsed v2 stdout JSON, absence of legacy `HD-Api-Key` on v2 path, and checksum ledger matches before emitting PR-03 entries.

Why it matters: High-risk mirror/index binding now fails closed on the exact regressions raised during PR review.

VAL-006

Purpose: Check GitHub-visible workflow run evidence.

Command or method: GitHub commit workflow run inspection for merge commit.

Result: NOT RUN

Key output or observation: `workflow_runs: []`.

Why it matters: No GitHub Actions run was available to rely on. This is non-blocking because repo-attached PR validation and final file-state inspections provide targeted proof, and CI alone would not have been sufficient anyway.

VAL-007

Purpose: Confirm PR review comments were addressed in final repo state.

Command or method: GitHub review-thread inspection plus final source inspection.

Result: PASS

Key output or observation: Review comments flagged missing false-check for legacy `HD-Api-Key` and stale checksum-ledger risk; final code validates `legacy_hd_api_key_on_v2_path is False`, `has_hd_api_key is False`, and ledger SHA matches promoted retained files.

Why it matters: Ensures the material review issues do not remain post-merge.

Findings

Finding ID: F-001

Related review item: CFR-001 / CFR-054 / VAL-004 / VAL-005

Severity: Note

Observation: Human Evidence Index and Machine Mirror are updated and final tests assert parity for HDE-EPIC035 paths.

Why it matters: This is the central HDE-FERM008.5 evidence-loop closure requirement.

Evidence: Repo proof: `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` asserts required HDE-EPIC035 paths are in both Human Index and Mirror and validates SHA/path proofs.

Required action: None.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

Finding ID: F-002

Related review item: CFR-048 / CFR-058 / CFR-059 / VAL-007

Severity: Note

Observation: Retained OPS-01 v2 `charts/simple` evidence is bound with parsed guardrails for Bearer auth, `HD-Geocode-Key`, and legacy `HD-Api-Key` absence.

Why it matters: This closes the high-risk evidence truth issue for geokey/header posture without rerunning OPS.

Evidence: Repo proof: `ops_evidence_binding.log` records header shapes and legacy key absence; update tooling and tests enforce boolean false for legacy key fields.

Required action: None.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

Finding ID: F-003

Related review item: CFR-019 / CFR-058 / CFR-059 / VAL-007

Severity: Note

Observation: Retained OPS checksum ledger validation now parses ledger rows and compares each promoted retained OPS file SHA before indexing.

Why it matters: Prevents stale retained checksum ledgers from being indexed as trusted evidence.

Evidence: Repo proof: `_load_epic035_ops01_checksum_ledger` and `_validate_epic035_ops01_checksums` validate ledger syntax, missing entries, and mismatched SHA.

Required action: None.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

Finding ID: F-004

Related review item: CFR-012 / CFR-044 / Evidence

Severity: Note

Observation: Doc-delta candidate artifacts were added without editing PF-Canon.

Why it matters: Captures canon-drain candidates while preserving implementation boundary.

Evidence: Repo proof: `audit/docdeltas/hde-epic035_doc_deltas.md` states PF-Canon was not edited and records PF29 clarification candidates.

Required action: Drain separately only if PO assigns canon-edit work.

PF reference, if relied on: PF06 — HDE Epic Process Guide, §0.2 Policy and principles.

Finding ID: F-005

Related review item: CFR-050 / CFR-052 / Evidence

Severity: Note

Observation: Acceptance map and token evidence matrix use existing token names and do not mint vendor-v2-specific tokens.

Why it matters: Prevents unsupported token satisfaction claims.

Evidence: Repo proof: acceptance map token list uses existing token names only; viability log records `forbidden_vendor_v2_specific_tokens=NONE`; token matrix lists only existing token names.

Required action: None.

PF reference, if relied on: PF04 — HDE Governance, §0.2 Scope & boundaries.

Finding ID: F-006

Related review item: CFR-021 / CFR-025 / CFR-030 / CFR-031 / CFR-048

Severity: Note

Observation: The merged change truthfully distinguishes v2 `charts/simple` geokey success from `bg:resolve` legacy BodyGraph route 404/runtime gap.

Why it matters: Prevents full v2 runtime conformance or BodyGraph adapter success from being inferred.

Evidence: Repo proof: `ops_evidence_binding.log` records v2 success evidence and `bg_resolve_runtime_gap`; final classification is validated by update tooling.

Required action: None.

PF reference, if relied on: PF10 — HDE Build Notes, Addendum 2.4.

Finding ID: F-007

Related review item: CFR-046 / CFR-048 / CFR-050 / CFR-052 / PF09

Severity: Note

Observation: Nonclaims are explicit and consistent across acceptance map, token matrix, viability log, and OPS binding.

Why it matters: Keeps PR-03 acceptance separate from QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, full v2 runtime conformance, and public surface changes.

Evidence: Repo proof: acceptance map includes nonclaims; token matrix repeats nonclaims; OPS binding records `ops_completion_claim=false`, `qa_pass_claim=false`, and `pf09_status_movement_claim=false`.

Required action: None.

PF reference, if relied on: PF04 — HDE Governance, §0.2 Scope & boundaries.

Finding ID: F-008

Related review item: CFR-006 / CFR-007 / CFR-008 / CFR-009 / CFR-010 / CFR-011 / CFR-014 / CFR-015 / CFR-016 / CFR-033 / CFR-034 / CFR-035 / CFR-036 / CFR-037 / CFR-038 / CFR-039 / CFR-040 / CFR-041 / CFR-042 / CFR-043

Severity: Note

Observation: Existing non-HDE-EPIC035 path proofs were refreshed by evidence tooling; no reviewed evidence showed executable behavior change or scope drift.

Why it matters: Evidence-tool refreshes can be noisy but are acceptable when they keep governed proof metadata current.

Evidence: Repo proof: changed-file list contains only `.path_proof.txt` siblings for those non-HDE-EPIC035 files; no corresponding payload/code changes were in those loci.

Required action: None.

PF reference, if relied on: PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.

Finding ID: F-009

Related review item: CFR-059 / VAL-007

Severity: Note

Observation: Two automated review threads remain not manually resolved in GitHub UI, but final source state addresses the underlying technical issues.

Why it matters: Unresolved UI state is not a blocker when final code evidence proves the issue is fixed.

Evidence: Repo proof: review threads identify the legacy-key guard and stale checksum-ledger risks; final code validates both.

Required action: None for post-merge remediation; optional UI cleanup if desired.

PF reference, if relied on: None.

Finding ID: F-010

Related review item: CFR-058 / VAL-003 / VAL-004

Severity: Note

Observation: Targeted validation was reported and the test file directly covers the high-risk evidence-loop invariants.

Why it matters: Supports merged change acceptability without relying solely on CI.

Evidence: Optional PR Artifacts report all relevant commands passed; repo test file includes checks for tokens, nonclaims, retained OPS paths, v2 header posture, mirror parity, path proofs, and checksum ledger.

Required action: None.

PF reference, if relied on: PF19 — Glow QA Guide, §0.2 Purpose & scope.

PF09 Impact & Status Posture

PF09 document: PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.4

PF09 task ID: HDE-FERM008

PF09 subtask ID(s): HDE-FERM008.5

Current PF09 status: Not done

Status recommendation: change to Done

Why this status posture is supported: PF09.5 defines HDE-FERM008.5 as the subtask to update the Human Evidence Index, hash sentinel, Machine Mirror, and path-proof transcripts for vendor v2 artifacts changed or produced by HDE-FERM006 through HDE-FERM008, and to verify single mirror file, governed paths only, final LF, canonical JSON where applicable, and no stale path-proofs. The merged change adds the HDE-EPIC035 acceptance map, token evidence matrix, OPS evidence binding, doc-delta candidates, retained OPS path proofs, Human Index, Machine Mirror, hash sentinels, path proofs, and targeted tests that validate these surfaces.

Evidence pointer(s): Repo proof: `docs/acceptance_map_epic035.json` records HDE-FERM008.5 governed evidence-loop closure scope and references PR-01, PR-02, OPS-01, and PR-03 evidence paths. Repo proof: `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` asserts HDE-EPIC035 rows are indexed/mirrored/path-proven and Human Index / Machine Mirror parity holds. Repo proof: PR body reports evidence index update/check, orientation update/check, evidence path validation, mirror schema check, hash check, and targeted tests passed.

PF proof excerpt(s), when PF09 is relied on:  
"Update the Human Evidence Index, hash sentinel, Machine Mirror, and path-proof transcripts for all vendor v2 artifacts changed or produced by HDE-FERM006 through HDE-FERM008. Verify single mirror file, governed paths only, final LF, canonical JSON where applicable, and no stale path-proofs."  
"Subtask status: Not done"  
"This subtask is the PF09.5 closure gate for vendor v2 evidence coherence. It is not satisfied by live smoke success alone."

Evidence Print

A) Tokens satisfied

Token: DOC\_DELTA\_PRESENT\_OK

Evidence pointer(s): Repo proof: `docs/acceptance_map_epic035.json` includes `DOC_DELTA_PRESENT_OK`; `audit/docdeltas/hde-epic035_doc_deltas.md` and `audit/qa/hde-epic035/00_meta/doc_deltas.md` exist as candidate doc-delta artifacts.

Token: EVIDENCE\_INDEX\_UPDATED\_OK

Evidence pointer(s): Repo proof: `docs/acceptance_map_epic035.json` includes `EVIDENCE_INDEX_UPDATED_OK`; `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` verifies required HDE-EPIC035 paths exist in Human Index.

Token: MACHINE\_MIRROR\_UPDATED\_OK

Evidence pointer(s): Repo proof: `docs/acceptance_map_epic035.json` includes `MACHINE_MIRROR_UPDATED_OK`; tests verify required HDE-EPIC035 paths exist in Machine Mirror.

Token: EVIDENCE\_INDEX\_HASH\_OK

Evidence pointer(s): Repo proof: `docs/acceptance_map_epic035.json` includes `EVIDENCE_INDEX_HASH_OK`; PR body reports `bash ci/checks/check_evidence_index_hash.sh` passed.

Token: EVIDENCE\_PATHS\_VALIDATED\_OK

Evidence pointer(s): Repo proof: `docs/acceptance_map_epic035.json` includes `EVIDENCE_PATHS_VALIDATED_OK`; PR body reports `python tools/evidence/validate_evidence_paths.py` passed.

Token: EVIDENCE\_PATH\_PROOFS\_OK

Evidence pointer(s): Repo proof: `docs/acceptance_map_epic035.json` includes `EVIDENCE_PATH_PROOFS_OK`; tests verify sibling path proofs exist and include expected path and SHA for required HDE-EPIC035 artifacts.

Token: JSON\_CANONICAL\_CHECK\_OK

Evidence pointer(s): Repo proof: `docs/acceptance_map_epic035.json` includes `JSON_CANONICAL_CHECK_OK`; tests assert acceptance map bytes equal sorted compact JSON with one trailing LF.

Token: TESTS\_PASS\_OK

Evidence pointer(s): Optional PR Artifacts and PR body report targeted tests passed: 316 existing evidence tests and 5 PR-03 evidence-loop tests.

B) Evidence artifacts produced or updated

Path: `docs/acceptance_map_epic035.json`

Type: canonical JSON acceptance-boundary map

Key proof facts observed: HDE-EPIC035 evidence-loop scope, baseline existing token mode, referenced evidence paths, nonclaims, PR-01/PR-02/OPS-01/PR-03 posture, and no vendor-v2-specific token.

sha256, if observed: `c2069cc489cd749f67e6335e8482a9a0bb488bfab4cfb72809637d983068a7e1`

Index/Mirror/path-proof posture, if relevant: Path proof exists at `docs/acceptance_map_epic035.json.path_proof.txt`; index/mirror tests assert required PR-03 paths are present.

Path: `audit/qa/hde-epic035/token_evidence_matrix.md`

Type: token evidence matrix

Key proof facts observed: Existing token names only; PR-01, PR-02, OPS-01, and PR-03 roles separated; nonclaims preserved.

sha256, if observed: not listed in review text; path proof exists.

Index/Mirror/path-proof posture, if relevant: Included in update-tool PR-03 rows and path-proven.

Path: `audit/qa/hde-epic035/acceptance_map_viability.log`

Type: mechanical viability log

Key proof facts observed: canonical JSON expected, referenced paths checked by tests and path validator, allowed token set listed, forbidden vendor-v2-specific tokens none, nonclaims present, HDE-FERM008.5 not claimed by OPS alone, no PF-canon edit required.

sha256, if observed: not listed in review text; path proof exists.

Index/Mirror/path-proof posture, if relevant: Included in update-tool PR-03 rows and path-proven.

Path: `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`

Type: OPS evidence binding log

Key proof facts observed: retained OPS evidence bound for PR-03 review, `ops_rerun=false`, `live_vendor_call_by_pr03=false`, v2 `charts/simple` header shapes, legacy key absent, `bg_resolve_runtime_gap`, and nonclaims.

sha256, if observed: not listed in review text; path proof exists.

Index/Mirror/path-proof posture, if relevant: Included in update-tool PR-03 rows and path-proven.

Path: `audit/docdeltas/hde-epic035_doc_deltas.md`

Type: doc-delta candidate artifact

Key proof facts observed: PF29 candidate clarifications for `bg:resolve`, v2 chart/geokey validation path, and OPS nested evidence-root manifest mapping; PF-Canon not edited.

sha256, if observed: not listed in review text; path proof exists.

Index/Mirror/path-proof posture, if relevant: Included in update-tool PR-03 rows and path-proven.

Path: `audit/qa/hde-epic035/00_meta/doc_deltas.md`

Type: QA meta doc-delta candidate artifact

Key proof facts observed: current-epic doc-delta companion artifact was added and indexed by PR-03 loader.

sha256, if observed: not listed in review text; path proof exists.

Index/Mirror/path-proof posture, if relevant: Included in update-tool PR-03 rows and path-proven.

Path: `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt`

Type: retained OPS manifest

Key proof facts observed: mapped approved-plan deliverables to retained evidence paths; accepted as retained evidence for PR-03 binding.

sha256, if observed: tracked through checksum ledger and path proof.

Index/Mirror/path-proof posture, if relevant: Included in PR-03 update-tool rows and path-proven.

Path: `audit/ops/hde-epic035/ops-01/files_sha256.txt`

Type: retained OPS checksum ledger

Key proof facts observed: parsed and validated by update-tool guard before indexing; tests confirm promoted retained-file hashes match ledger.

sha256, if observed: path proof exists.

Index/Mirror/path-proof posture, if relevant: Included in PR-03 update-tool rows and path-proven.

Path: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log`

Type: retained OPS stdout JSON log

Key proof facts observed: `classification:"success"`, `authorization_header_shape:"Authorization: Bearer <redacted>"`, `hd_geocode_key_header_shape:"HD-Geocode-Key: <redacted>"`, `has_authorization:true`, `has_hd_geocode_key:true`, `legacy_hd_api_key_on_v2_path:false`, `has_hd_api_key:false`, and raw payload/secret persistence false by test inspection.

sha256, if observed: ledger/path proof validates current bytes.

Index/Mirror/path-proof posture, if relevant: Included in PR-03 update-tool rows and path-proven.

Path: `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt`

Type: retained OPS final classification

Key proof facts observed: `v2_charts_simple=success`, `bg_resolve_http_status=404`, and runtime-gap distinction are validated by tests and update tooling.

sha256, if observed: ledger/path proof validates current bytes.

Index/Mirror/path-proof posture, if relevant: Included in PR-03 update-tool rows and path-proven.

Path: `artifacts/evidence_index.jsonl`

Type: Machine Evidence Mirror

Key proof facts observed: updated with HDE-EPIC035 PR-03 and OPS retained evidence rows; tests assert parity with Human Evidence Index.

sha256, if observed: hash sentinel updated.

Index/Mirror/path-proof posture, if relevant: Primary machine mirror at governed path.

Path: `docs/evidence/INDEX.json`

Type: Human Evidence Index

Key proof facts observed: updated with HDE-EPIC035 PR-03 and OPS retained evidence rows; tests assert required paths present.

sha256, if observed: hash sentinel updated.

Index/Mirror/path-proof posture, if relevant: Primary human index at governed path.

C) Validation proof

Command or method: GitHub PR metadata and changed-file list inspection

Result: PASS

Where the result appears: PR metadata and changed-file list.

Why it is sufficient: Resolves merged PR state, exact merge commit, and changed files.

Command or method: GitHub compare `824953bf8c8b16bcc8e89b1c6f722b1f6080b73f..main`

Result: PASS

Where the result appears: Repo Inspection.

Why it is sufficient: Confirms final current repo state is the merged PR state.

Command or method: Optional PR Artifacts / PR body reported command `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_live_conformance.py tests/evidence/test_hdapi_v2_response_normalization.py tests/evidence/test_hdapi_v2_contract_inventory.py`

Result: PASS

Where the result appears: Optional PR Artifacts and PR body.

Why it is sufficient: Covers pre-existing PR-01/PR-02 evidence suites and regression surfaces.

Command or method: Optional PR Artifacts / PR body reported command `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hde_epic035_pr03_evidence_loop.py`

Result: PASS

Where the result appears: Optional PR Artifacts and PR body.

Why it is sufficient: Covers PR-03 acceptance map, tokens, nonclaims, OPS binding, v2 success/gap separation, index/mirror parity, path proofs, and checksum ledger.

Command or method: Optional PR Artifacts / PR body reported evidence tooling commands: `python tools/evidence/update_evidence_index.py`, `python tools/evidence/orientation_demo.py`, `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, `python tools/evidence/validate_evidence_paths.py`, `python ci/checks/check_mirror_schema.sh`, `bash ci/checks/check_evidence_index_hash.sh`, and `git diff --check`

Result: PASS

Where the result appears: Optional PR Artifacts and PR body.

Why it is sufficient: Covers governed evidence refresh, checks, path validation, mirror schema, hash sentinel, and diff hygiene.

Doc Delta Candidates

DDC-001

Doc: PF09.5 — HDE Build Checklist Fermentation

Section: §Subtask HDE-FERM008.5 \- Index v2 live conformance and close the evidence loop

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.5

PF09 status action: change to Done

Delta: Update HDE-FERM008.5 from Not done to Done when PO performs PF09 drainage, with evidence pointers to PR-03 Human Evidence Index, Machine Mirror, hash sentinel, path proofs, acceptance map, token evidence matrix, OPS evidence binding, and validation outputs.

Why: The merged change implements the PF09.5-described evidence-loop closure work for HDE-FERM008.5 and validates the single mirror, governed paths, canonical JSON where applicable, path proofs, and no stale OPS checksum/legacy-header evidence regressions.

Repo evidence: Repo proof: `docs/acceptance_map_epic035.json` references PR-01, PR-02, OPS-01, and PR-03 evidence paths; `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` verifies index/mirror/path-proof parity and checksum-ledger validity.

Canon proof excerpt: "Update the Human Evidence Index, hash sentinel, Machine Mirror, and path-proof transcripts for all vendor v2 artifacts changed or produced by HDE-FERM006 through HDE-FERM008. Verify single mirror file, governed paths only, final LF, canonical JSON where applicable, and no stale path-proofs."

DDC-002

Doc: PF29 — HDE User Guide

Section: HDAPI v2 geokey and BodyGraph ingest workflow

Canon basis: CANON SILENCE

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.5

PF09 status action: No status change recommended

Delta: NEW CANON PROPOSAL: PF29 should clarify that `hdctl bg:resolve --source vendor` is a legacy BodyGraph ingest-path observation and not the canonical v2 chart/geokey validation path. The v2 chart/geokey path should be documented through `charts` or `charts/simple` observations that prove `Authorization: Bearer <redacted>`, `HD-Geocode-Key: <redacted>`, and legacy `HD-Api-Key` absent.

Why: PR-03 binds OPS-01 evidence showing `bg:resolve` returned `PROVIDER_NOT_FOUND` / 404 against the configured v2 base, while v2 `charts/simple` produced successful geokey/auth header posture.

Repo evidence: Repo proof: `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log` records v2 charts/simple header success and bg:resolve runtime gap; `audit/docdeltas/hde-epic035_doc_deltas.md` records this PF29 candidate.

Canon proof excerpt: Not required for CANON SILENCE.

DDC-003

Doc: PF29 — HDE User Guide

Section: OPS/live evidence deliverable conventions

Canon basis: CANON SILENCE

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.5

PF09 status action: No status change recommended

Delta: NEW CANON PROPOSAL: PF29 should document that retained OPS evidence may use a nested run-label evidence root when a manifest maps approved deliverable names to retained paths, and that text/markdown summaries must be explicitly mapped rather than treated as schema-governed JSON.

Why: PR-03 accepts retained OPS-01 evidence under `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/` because `ops_evidence_manifest.txt` maps approved deliverable names to retained paths and the PR adds path proofs/index/mirror binding.

Repo evidence: Repo proof: `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt` is indexed through update tooling, and `audit/docdeltas/hde-epic035_doc_deltas.md` records the PF29 nested-root mapping candidate.

Canon proof excerpt: Not required for CANON SILENCE.

DECISION: MERGED CHANGE ACCEPTABLE

## 2.6) Implementation Retrospective  HDE-EPIC035

Executive Summary

* Planned / intended work: HDE-EPIC035 was scoped to handle the remaining HumanDesignAPI v2 Fermentation live-conformance sequence for HDE-FERM008.3 through HDE-FERM008.5: provider error/retry/rate-limit mapping, v2 response normalization or exact adapter/schema gap recording, and governed evidence-loop closure. Artifact → r1 Implementation Plan HDE-EPIC035 → Brief recap of scope → "HDE-EPIC035 completes the remaining HumanDesignAPI v2 Fermentation live-conformance sequence for HDE-FERM008.3 through HDE-FERM008.5." | "The plan covers deterministic v2 error, retry, rate-limit, malformed-response, redirect, network-error, and provider-status mapping" | "response normalization or exact adapter/schema gap recording for existing HDE flows; and governed evidence-loop closure."  
* Planned / intended boundaries: the plan preserved no public Reader change, no public route/flag/payload/transport change, no new HTTP home, no app-side HumanDesignAPI call path, no AI scope, no raw secrets, no raw request/response payload persistence, and no vendor-v2-specific acceptance token. Artifact → r1 Implementation Plan HDE-EPIC035 → Brief recap of scope → "The plan preserves the stated boundaries: no public Reader change, no public route, no public flag, no public payload or transport change, no new HTTP home" | "no app-side HumanDesignAPI call path, no AI scope, no raw secrets" | "no vendor-v2-specific acceptance token."  
* PF10-recorded PR-01 outcome: PF10 records that PR \#328 added the PR-01 provider-outcome evidence family for HDE-FERM008.3, with governed snapshots, path proofs, index/mirror bindings, and tests; PF10 also records two remediation attempts for chronology and closed-rails enforcement issues. PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "Original PR \#328 added the HDE-EPIC035 PR-01 HDAPI v2 provider-outcome evidence family for PF09.5 / HDE-FERM008 / HDE-FERM008.3" | "First Remedial PR \#329 corrected direct PR-01 artifact timestamping" | "Second Remedial PR \#330 addressed the remaining two gaps."  
* Current repo reality for PR-01: current Repo contains `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` and `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`, both carrying HDE-EPIC035 / HDE-FERM008.3 metadata, closed-rails posture, no-claim fields, and redacted/keys-only observability posture. Repo → `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` → `"artifact_kind":"hdapi_v2_provider_outcome_mapping"` | `"epic_id":"HDE-EPIC035"` | `"pf09_subtask_id":"HDE-FERM008.3"` Repo → `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` → `"artifact_kind":"hdapi_v2_retry_after_mapping"` | `"epic_id":"HDE-EPIC035"` | `"pf09_subtask_id":"HDE-FERM008.3"`  
* PF10-recorded PR-02 outcome: PF10 records that PR \#331 added response-normalization evidence for HDE-FERM008.4 and that remedial PR \#332 fixed evidence-indexing conflicts while preserving EPIC034 semantics. PF10 — HDE-Build Notes → 2.2) PR-02 HDE-EPIC035 → "Original PR \#331 added HDE-EPIC035 PR-02 response-normalization evidence for PF09.5 / HDE-FERM008 / HDE-FERM008.4" | "recording an exact schema/adapter gap rather than claiming a normalized data path" | "Remedial PR \#332 fixed those gaps."  
* Current repo reality for PR-02: current Repo records the v2 ChartResult / ChartSimpleResult work as an exact schema/adapter gap, not a normalized data-path proof, and release-binding evidence explicitly leaves HDE-FERM008.5 as follow-up from the PR-02 frame. Repo → `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` → `"artifact_kind":"hdapi_v2_response_normalization_gap"` | `"response_normalization_posture":"EXACT_SCHEMA_ADAPTER_GAP_RECORDED"` | `"normalized_data_path_proof_claim":"NONE"` Repo → `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` → `"release_binding_posture":"PR02 binds PR01 HDE-FERM008.3 provider outcome evidence to PR02 HDE-FERM008.4 exact schema/adapter gap evidence without claiming full HumanDesignAPI v2 runtime conformance or HDE-FERM008.5 closure."`  
* PF10-recorded OPS-01 outcome: PF10 records OPS-01 as bounded PO-only live observation that contributes evidence only, with v2 `charts/simple` success and `bg:resolve` remaining a legacy BodyGraph ingest-path runtime gap. PF10 — HDE-Build Notes → 2.4) OPS-01 HDE-EPIC035 → "one bounded open-rails `hdctl bg:resolve --source vendor --dry-run` observation" | "one command-backed v2 `charts/simple` geocode-required provider observation" | "PF09 support is limited to evidence contribution."  
* Current repo reality for OPS-01: current Repo retains mapped OPS evidence under `audit/ops/hde-epic035/ops-01/`, with `v2_charts_simple=success`, `bg_resolve=vendor_error_class_observed`, and explicit nonclaims. Repo → `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt` → `"v2_charts_simple=success"` | `"bg_resolve_http_status=404"` | `"runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base"`  
* PF10-recorded PR-03 outcome: PF10 records that PR-03 bound PR-01, PR-02, and retained OPS-01 evidence into the governed HDE-FERM008.5 evidence-loop surface, preserving boundaries and leaving PF29/PF09 drainage as later documentation/canon work. PF10 — HDE-Build Notes → 2.5) PR-03 HDE-EPIC035 → "The merged change binds HDE-EPIC035 PR-01, PR-02, and retained OPS-01 evidence into the governed PR-03 evidence-loop closure surface for HDE-FERM008.5." | "no PF09 status movement claim" | "Remaining risk is documentation drainage only."  
* Current repo reality for PR-03: current Repo contains `docs/acceptance_map_epic035.json`, `audit/qa/hde-epic035/token_evidence_matrix.md`, `audit/qa/hde-epic035/acceptance_map_viability.log`, `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`, HDE-EPIC035 tests, and HDE-EPIC035 docs. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `ACCEPTANCE = ROOT / "docs/acceptance_map_epic035.json"` | `MATRIX = ROOT / "audit/qa/hde-epic035/token_evidence_matrix.md"` | `MIRROR = ROOT / "artifacts/evidence_index.jsonl"`

Biggest wins and remaining risks / gaps:

* Win: the work kept vendor v2 evidence secret-safe and bounded; current Repo snapshots and OPS logs show redacted header posture and no raw payload persistence. Repo → `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log` → `"v2_charts_simple_authorization_header_shape=Authorization: Bearer <redacted>"` | `"v2_charts_simple_hd_geocode_key_header_shape=HD-Geocode-Key: <redacted>"` | `"raw_payload_persistence_claim=false"`  
* Win: the evidence-loop slice has explicit tests for Human Index / Machine Mirror parity, path proofs, allowed tokens, nonclaims, OPS binding, and checksum-ledger validation. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `assert required <= set(index_by_path)` | `assert required <= set(mirror_by_path)` | `assert proof.exists()`  
* Remaining risk / gap: current repo reality still records the v2 response work as an adapter/schema gap rather than a proven normalized data path into BodyGraph/cache/compat. Repo → `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` → `"schema_gap_summary":"HDE-FERM008.4 remains an exact adapter/schema gap"` | `"required_follow_up":"A bounded adapter/schema proof or implementation must map v2 ChartResult/ChartSimpleResult data"`  
* Remaining risk / gap: `bg:resolve --source vendor` is not the canonical v2 chart/geokey validation path; current OPS evidence records it as a legacy BodyGraph route observation returning 404 against the configured v2 base. Repo → `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt` → `"bg_resolve_request_shape=/v2/bodygraphs"` | `"bg_resolve_http_status=404"` | `"geokey_header_posture_not_proven_for_bg_resolve=true"`  
* Remaining risk / gap: PF29 and PF09 status-drainage items are staged as documentation/canon follow-up; current Repo contains doc-delta candidates, not PF-Canon edits. Repo → `audit/docdeltas/hde-epic035_doc_deltas.md` → `"Scope: same-PR drift-capture candidates only. PF-Canon was not edited."` | `"PF29 should clarify"` | `"Nonclaims: no PF09 status movement"`

Repo Inspection Summary

* Observed repo root: `amthorn78/glow-hdengine-v2`. Repo → GitHub repository metadata → `"repository_full_name":"amthorn78/glow-hdengine-v2"` | `"default_branch":"main"`  
* Observed HEAD: `2c077453eeb5a5db502c16ecc82a3ea9c05679ec`. Repo → GitHub compare `main..main` → `"status":"identical"` | `"base_commit.sha":"2c077453eeb5a5db502c16ecc82a3ea9c05679ec"`  
* Branch or detached state: current GitHub default branch is `main`. Repo → GitHub repository metadata → `"default_branch":"main"`  
* Working tree status before review: no mutable local working tree was exposed by the GitHub connector; current branch self-compare was identical. Repo → GitHub compare `main..main` → `"status":"identical"` | `"ahead_by":0` | `"behind_by":0`  
* Primary epic-related repo evidence discovered:  
  * HDE-EPIC035 search surfaced `audit/docdeltas/hde-epic035_doc_deltas.md`, `audit/qa/hde-epic035/token_evidence_matrix.md`, `audit/ops/hde-epic035/ops-01/`, `docs/acceptance_map_epic035.json`, `docs/RUN.md`, `docs/CLI_commands.md`, `AGENTS.md`, `README.md`, `CHANGELOG.md`, `tools/evidence/generate_hdapi_v2_response_normalization.py`, `tools/evidence/generate_hdapi_v2_live_conformance.py`, `tools/evidence/update_evidence_index.py`, `artifacts/evidence_index.jsonl`, and HDE-EPIC035 tests. Repo → GitHub search `HDE-EPIC035 OR hde-epic035 OR epic035` → paths listed under `audit/`, `docs/`, `tools/`, `tests/`, and `artifacts/`  
* Primary epic-related repo evidence not found: no negative repo claim is used as a report foundation. Formal closure/close-pack status remains in the Lead decision area, not a negative repo fact in this report.  
* Key current repo surfaces that shaped the report:  
  * Vendor snapshot artifacts under `artifacts/vendor/hdapi_v2/`. Repo → `error_mapping.snapshot.json` and `rate_limit_headers.snapshot.json` → `"pf09_subtask_id":"HDE-FERM008.3"`  
  * Response-normalization gap artifact and release binding under `artifacts/vendor/hdapi_v2/`. Repo → `response_mapping.snapshot.json` → `"schema_gap_status":"GAP_RECORDED"`; Repo → `release_binding.snapshot.json` → `"follow_up_hde_ferm008_5_evidence_loop_closure"`  
  * OPS evidence under `audit/ops/hde-epic035/ops-01/`. Repo → `ops_evidence_manifest.txt` → `"Purpose: map approved-plan OPS-01 deliverable names to retained evidence paths"` | `"v2_charts_simple=success"` | `"geokey_header_posture=proven_for_v2_charts_simple"`  
  * Acceptance boundary, token matrix, and tests under `docs/acceptance_map_epic035.json`, `audit/qa/hde-epic035/`, and `tests/evidence/`. Repo → `token_evidence_matrix.md` → `"Scope: compact evidence matrix for HDE-FERM008.5 evidence-loop binding."` | `"Nonclaims: no QA PASS, no OPS completion, no PF09 status movement"`  
  * Current public/developer repo docs updated for HDE-EPIC035. Repo → `README.md` → `"What HDE-EPIC035 adds for Fermentation Pass 6"` | `"Scope boundaries remain explicit"`  
* Working tree status after read-only validation commands: no repo-mutating commands were run; inspection used GitHub metadata, compare, search, and file reads only. Repo → GitHub compare `main..main` → `"status":"identical"` | `"total_commits":0`

Implementation Report (What happened in the repo)

PR/step breakdown

PR1 — PR-01 provider-outcome evidence for HDE-FERM008.3

* Purpose: produce governed deterministic evidence for v2 provider status/error mapping, retry posture, rate-limit/Retry-After handling, malformed/bad responses, network errors, closed-rails refusal context, and secret-safe observability. PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "Original PR \#328 added the HDE-EPIC035 PR-01 HDAPI v2 provider-outcome evidence family" | "two governed snapshots, path proofs, evidence-index / mirror bindings, and targeted tests."  
* Key changes, high level: PF10 records an original PR plus two remedial PRs; the final PF10-recorded posture addresses backdated path-proof chronology and closed-rails enforcement gaps. PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "First Remedial PR \#329 corrected direct PR-01 artifact timestamping" | "Second Remedial PR \#330 addressed the remaining two gaps" | "Current governed evidence now shows coherent chronology."  
* Key surfaces touched: current Repo contains vendor outcome snapshots under `artifacts/vendor/hdapi_v2/`; tests and update tooling are discoverable by repo search. Repo → GitHub search HDE-EPIC035 → `tools/evidence/generate_hdapi_v2_live_conformance.py`, `tests/evidence/test_hdapi_v2_live_conformance.py`, `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`, `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`  
* Tests or evidence produced: current Repo contains `error_mapping.snapshot.json` and `rate_limit_headers.snapshot.json`. Repo → `error_mapping.snapshot.json` → `"status_mapping_records"` | `"retry_classification"` | `"observability_posture"` Repo → `rate_limit_headers.snapshot.json` → `"retry_after_records"` | `"rate_limit_status_record"` | `"rails":{"allow_network":"0","closed_rails_only":true,"safe_mode":"1"}`  
* Outcome: PF10 records the PF09 impact as limited to HDE-FERM008.3 and records a later status recommendation for that subtask without claiming HDE-FERM008 parent completion. PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "PF09 impact is limited to PF09.5 / HDE-FERM008 / HDE-FERM008.3." | "without claiming HDE-FERM008 parent completion."  
* Evidence pointer(s): PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "Current GitHub Repo state equals the second remedial merge commit" | "Visible CI for all three PR heads completed successfully"; Repo → `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` → `"artifact_kind":"hdapi_v2_provider_outcome_mapping"`

PR2 — PR-02 response-normalization or exact adapter/schema gap evidence for HDE-FERM008.4

* Purpose: prove a v2 response can feed existing HDE flows or record the exact adapter/schema gap without compatibility by inference. Artifact → r1 Implementation Plan HDE-EPIC035 → PR-02 → "Implement HDE-FERM008.4 by producing governed evidence that either proves v2 response data can be normalized into existing HDE flow boundaries or records the exact adapter/schema gap without inference." | "This PR must not change public Reader bytes or leak admin-only data."  
* Key changes, high level: PF10 records that original PR \#331 added the generator, promoted `response_mapping.snapshot.json`, added `release_binding.snapshot.json`, tests, and index/mirror bindings; remedial PR \#332 fixed EPIC034/EPIC035 indexing conflicts and fail-closed route/schema drift checks. PF10 — HDE-Build Notes → 2.2) PR-02 HDE-EPIC035 → "Original PR \#331 added HDE-EPIC035 PR-02 response-normalization evidence" | "recording an exact schema/adapter gap" | "Remedial PR \#332 fixed those gaps."  
* Key surfaces touched: current Repo contains `tools/evidence/generate_hdapi_v2_response_normalization.py`, `tests/evidence/test_hdapi_v2_response_normalization.py`, `response_mapping.snapshot.json`, and `release_binding.snapshot.json`. Repo → GitHub search HDE-EPIC035 → `tools/evidence/generate_hdapi_v2_response_normalization.py` | `tests/evidence/test_hdapi_v2_response_normalization.py` | `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`  
* Tests or evidence produced: current Repo records the adapter/schema gap, the inspected HDE loci, route-family identity, and no-claim posture. Repo → `response_mapping.snapshot.json` → `"inspected_internal_loci"` | `"response_normalization_posture":"EXACT_SCHEMA_ADAPTER_GAP_RECORDED"` | `"no_compatibility_by_inference":true`  
* Outcome: PF10 records the PF09 impact as limited to HDE-FERM008.4 and records a later status recommendation for that subtask without claiming HDE-FERM008 parent completion or HDE-FERM008.5 closure. PF10 — HDE-Build Notes → 2.2) PR-02 HDE-EPIC035 → "PF09 impact is limited to PF09.5 / HDE-FERM008 / HDE-FERM008.4." | "without claiming HDE-FERM008 parent completion or HDE-FERM008.5 closure."  
* Evidence pointer(s): Repo → `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` → `"posture":"EXACT_SCHEMA_ADAPTER_GAP_RECORDED"` | `"follow_up_hde_ferm008_5_evidence_loop_closure"` | `"hde_ferm008_5_closure":"NONE"`

OPS1 — OPS-01 bounded PO-run live observation

* Purpose: contribute bounded open-rails provider evidence only when live provider facts were needed without turning OPS into QA PASS, PF09 status movement, or closure. PF10 — HDE-Build Notes → 2.4) OPS-01 HDE-EPIC035 → "The OPS evidence aligns with the Approved Plan’s bounded PO-only live-observation role" | "it contributes evidence only" | "preserves nonclaims."  
* Key changes, high level: current Repo retains OPS evidence under a nested smoke-root and maps approved-plan deliverable names to retained files via `ops_evidence_manifest.txt`. Repo → `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt` → `"Purpose: map approved-plan OPS-01 deliverable names to retained evidence paths without moving or deleting current evidence."` | `"nested smoke-root retained"` | `"Additional retained evidence"`  
* Key surfaces touched: OPS evidence lives under `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/`; PR-03 later bound it via `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`. Repo → `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log` → `"retained_ops01_root=audit/ops/hde-epic035/ops-01"` | `"v2_charts_simple_success_evidence"` | `"bg_resolve_provider_error_stdout"`  
* Tests or evidence produced: current Repo records `v2_charts_simple=success`, `Authorization_Bearer_present`, `HD-Geocode-Key_present`, legacy key absence on the v2 path, and `bg_resolve` 404 / provider-not-found runtime gap. Repo → `final_classification.txt` → `"v2_charts_simple=success"` | `"v2_charts_simple_auth_posture=Authorization_Bearer_present; HD-Geocode-Key_present; legacy_HD-Api-Key_absent"` | `"bg_resolve_http_status=404"`  
* Outcome: PF10 records that OPS-01 evidence supports evidence contribution only and does not support PF09 status movement or HDE-FERM008.5 closure by itself. PF10 — HDE-Build Notes → 2.4) OPS-01 HDE-EPIC035 → "PF09 support is limited to evidence contribution." | "OPS-01 does not support PF09 status movement or HDE-FERM008.5 closure by itself."  
* Evidence pointer(s): Repo → `ops_evidence_manifest.txt` → `"Final classification summary:"` | `"bg_resolve=vendor_error_class_observed"` | `"v2_charts_simple=success"`

PR3 — PR-03 evidence-loop binding for HDE-FERM008.5

* Purpose: bind PR-01, PR-02, and retained OPS-01 evidence into the governed HDE-FERM008.5 evidence-loop surface. PF10 — HDE-Build Notes → 2.5) PR-03 HDE-EPIC035 → "The merged change binds HDE-EPIC035 PR-01, PR-02, and retained OPS-01 evidence into the governed PR-03 evidence-loop closure surface for HDE-FERM008.5."  
* Key changes, high level: PF10 records that PR-03 added/refreshed Human Evidence Index, Machine Mirror, hash sentinels, path proofs, acceptance-boundary artifacts, token evidence matrix, OPS evidence binding, and doc-delta candidates. PF10 — HDE-Build Notes → 2.5) PR-03 HDE-EPIC035 → "Human Evidence Index, Machine Mirror, hash sentinels, path proofs, acceptance-boundary artifacts, token evidence matrix, OPS evidence binding, and doc-delta candidates were added or refreshed."  
* Key surfaces touched: current Repo contains `docs/acceptance_map_epic035.json`, `audit/qa/hde-epic035/token_evidence_matrix.md`, `audit/qa/hde-epic035/acceptance_map_viability.log`, `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`, `audit/docdeltas/hde-epic035_doc_deltas.md`, and tests. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `ACCEPTANCE = ROOT / "docs/acceptance_map_epic035.json"` | `MATRIX = ROOT / "audit/qa/hde-epic035/token_evidence_matrix.md"` | `BINDING = ROOT / "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log"`  
* Tests or evidence produced: current Repo tests validate allowed tokens, nonclaims, OPS paths, v2 stdout redaction/header posture, Human Index / Machine Mirror parity, path proofs, and checksum-ledger validation. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `def test_acceptance_map_uses_only_allowed_tokens_and_nonclaims()` | `def test_epic035_rows_are_indexed_mirrored_and_path_proven()` | `def test_epic035_ops01_checksum_ledger_matches_promoted_retained_files()`  
* Outcome: PF10 records that current repo evidence supports HDE-FERM008.5 as supportable for a later PF09 status change, while PR-03 itself does not edit PF09 or claim PF09 status movement. PF10 — HDE-Build Notes → 2.5) PR-03 HDE-EPIC035 → "Current repo evidence supports HDE-FERM008.5 as supportable for a later PF09 status change to Done" | "the merged change itself correctly does not edit PF09 or claim PF09 status movement."  
* Evidence pointer(s): Repo → `audit/qa/hde-epic035/token_evidence_matrix.md` → `"Scope: compact evidence matrix for HDE-FERM008.5 evidence-loop binding."` | `"OPS-01: retained files under ... are bound as already-produced open-rails evidence only; PR-03 did not rerun OPS."` | `"Nonclaims: no QA PASS, no OPS completion, no PF09 status movement"`

Docs step — final repo-docs sweep

* Purpose: update repo-facing docs to reflect HDE-EPIC035 outcomes and guardrails without editing PF-Canon. Artifact → Docs PR HDE-EPIC035 → Actions Taken → "Updated the README title and current-epic overview to HDE-EPIC035 / Fermentation Pass 6" | "Added an HDE-EPIC035 Unreleased changelog entry" | "Added agent-facing EPIC035 docs posture to AGENTS.md."  
* Key changes, high level: current Repo docs describe HDE-EPIC035 evidence outcomes, v2 chart/geokey posture, `bg:resolve` legacy runtime gap, and nonclaims. Repo → `README.md` → `"What HDE-EPIC035 adds for Fermentation Pass 6"` | `"OPS-01 retained PO-run open-rails evidence"` | `"Scope boundaries remain explicit"`  
* Key surfaces touched: docs-only current repo surfaces include `README.md`, `CHANGELOG.md`, `AGENTS.md`, `docs/CLI_commands.md`, `docs/INDEX.md`, and `docs/RUN.md`. Repo → compare `824953bf8c8b16bcc8e89b1c6f722b1f6080b73f..main` → files list showed those six docs files only.  
* Tests or evidence produced: PR Artifacts reported `git diff --check`, manual Markdown sanity, and HDE-EPIC035 targeted evidence checks; Repo inspection found no repo-verified Markdown lint command. Artifact → Docs PR HDE-EPIC035 → Validation Performed → "git diff \--check" | "Manual Markdown sanity check" | "No doc lint command found."  
* Outcome: current docs now include HDE-EPIC035 posture and preserve no-PF-Canon-edit status. Repo → `docs/INDEX.md` → `"EPIC035 scope boundaries"` | `"PF29 drainage remains PF-Canon follow-up and is not performed in repo docs."`  
* Evidence pointer(s): Repo → `CHANGELOG.md` → `"Unreleased — HDE-EPIC035: Fermentation Pass 6 final repo docs sweep"` | `"Preserved HDE-EPIC035 nonclaims"`

Major surfaces affected

* Vendor seam / HumanDesignAPI v2 evidence: outcome mapping, Retry-After/rate-limit mapping, route/auth posture, response-normalization gap, and release binding under `artifacts/vendor/hdapi_v2/`. Repo → `error_mapping.snapshot.json` → `"route_family_identity"` | `"v2_chart_routes"` | `"legacy_v1_bodygraph_routes"`  
* BodyGraph / compat boundary: PR-02 evidence records that no ChartResult/ChartSimpleResult-to-BodyGraph/person adapter proof currently exists in inspected loci. Repo → `response_mapping.snapshot.json` → `"bodygraph_boundary"` | `"compat_boundary"` | `"required_follow_up"`  
* OPS / live-provider observation: OPS-01 retained evidence records one successful v2 `charts/simple` geokey/auth observation and a separate `bg:resolve` runtime gap. Repo → `final_classification.txt` → `"v2_charts_simple=success"` | `"bg_resolve=vendor_error_class_observed"` | `"runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base"`  
* Evidence / QA artifacts: acceptance map, token matrix, viability log, OPS evidence binding, doc deltas, Human Evidence Index, Machine Mirror, hash sentinels, and path proofs. Repo → `token_evidence_matrix.md` → `"EVIDENCE_INDEX_UPDATED_OK"` | `"MACHINE_MIRROR_UPDATED_OK"` | `"EVIDENCE_PATH_PROOFS_OK"`  
* Evidence tooling / tests: HDE-EPIC035 PR-03 tests assert allowed tokens, nonclaims, OPS path existence, v2 header posture, index/mirror parity, path proof freshness, and checksum ledger validation. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `ALLOWED_TOKENS = {` | `REQUIRED_OPS_PATHS = [` | `assert _epic035_ops01_v2_stdout_is_valid(payload) is True`  
* Repo docs: README, CHANGELOG, AGENTS, docs/CLI\_commands.md, docs/INDEX.md, and docs/RUN.md now document HDE-EPIC035 posture and nonclaims. Repo → `docs/RUN.md` → `"## HumanDesignAPI v2 evidence / geokey posture (HDE-EPIC035)"` | `"Secret/config names are HD_API_BASE_URL, HD_API_KEY, and GEO_API_KEY"` | "`hdctl bg:resolve --source vendor` remains the legacy BodyGraph ingest-path workflow"

Evidence inventory (what exists)

* `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` — provider outcome mapping, typed provider codes, retry classification, closed-rails refusal context, route-family identity, keys-only observability, and no-claim posture. Repo → `error_mapping.snapshot.json` → `"artifact_kind":"hdapi_v2_provider_outcome_mapping"` | `"status_mapping_records"` | `"no_claims"`  
* `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` — Retry-After delta/date/invalid/overflow posture and 429 rate-limit classification. Repo → `rate_limit_headers.snapshot.json` → `"retry_after_records"` | `"rate_limit_status_record"` | `"retryable":false`  
* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` — exact v2 ChartResult / ChartSimpleResult adapter/schema gap evidence. Repo → `response_mapping.snapshot.json` → `"artifact_kind":"hdapi_v2_response_normalization_gap"` | `"schema_gap_status":"GAP_RECORDED"` | `"normalized_data_path_proof_claim":"NONE"`  
* `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` — PR-01 / PR-02 binding and HDE-FERM008.5 follow-up posture from the PR-02 evidence frame. Repo → `release_binding.snapshot.json` → `"artifact_kind":"hdapi_v2_release_binding"` | `"pr01_hde_ferm008_3_provider_outcome"` | `"pr02_hde_ferm008_4_response_normalization"`  
* `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt` — mapping between approved deliverables and retained OPS evidence paths. Repo → `ops_evidence_manifest.txt` → `"Approved-plan deliverable"` | `"Retained evidence path"` | `"Status"`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt` — final OPS classification of v2 charts/simple success and bgresolve runtime gap. Repo → `final_classification.txt` → `"v2_charts_simple=success"` | `"provider_availability=provider_responding_on_correct_v2_chart_path"` | `"runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base"`  
* `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log` — PR-03 binding of retained OPS evidence and nonclaims. Repo → `ops_evidence_binding.log` → `"ops_completion_claim=false"` | `"qa_pass_claim=false"` | `"full_runtime_conformance_claim=false"`  
* `docs/acceptance_map_epic035.json` — canonical acceptance-boundary map with baseline existing tokens only, nonclaims, referenced evidence paths, and PR/OPS posture. Repo → `docs/acceptance_map_epic035.json` → `"acceptance_claims_mode":"baseline_existing_tokens_only"` | `"nonclaims"` | `"referenced_evidence_paths"`  
* `audit/qa/hde-epic035/token_evidence_matrix.md` — token-to-evidence-role matrix and explicit nonclaims. Repo → `token_evidence_matrix.md` → `"Token"` | `"Evidence paths"` | `"Role"`  
* `audit/qa/hde-epic035/acceptance_map_viability.log` — mechanical viability record for allowed token set, forbidden vendor-specific tokens, nonclaims, and non-runbook/non-closeout posture. Repo → `acceptance_map_viability.log` → `"allowed_token_set=DOC_DELTA_PRESENT_OK,EVIDENCE_INDEX_UPDATED_OK"` | `"forbidden_vendor_v2_specific_tokens=NONE"` | `"hde_ferm008_5_claimed_by_ops_alone=false"`  
* `audit/docdeltas/hde-epic035_doc_deltas.md` — PF29 doc-delta candidates and no-PF-Canon-edit status. Repo → `hde-epic035_doc_deltas.md` → `"PF-Canon was not edited."` | `"PF29 should clarify"` | `"Nonclaims: no PF09 status movement"`  
* `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` — targeted tests for the HDE-EPIC035 evidence loop. Repo → test file → `"def test_human_index_machine_mirror_parity_for_epic035()"` | `"def test_boundary_logs_are_not_closeout_or_runbooks()"` | `"def test_epic035_ops01_checksum_ledger_matches_promoted_retained_files()"`

Evidence gaps

* Adapter/data-path proof remains a recorded gap.  
  * What is missing or unclear: v2 ChartResult / ChartSimpleResult data is not proven to feed the existing BodyGraph/cache and compat input shape.  
  * Why it matters: without the adapter proof, full HumanDesignAPI v2 runtime flow into existing HDE BodyGraph/compat cannot be inferred from response evidence.  
  * What would prove it: a bounded adapter/schema proof or implementation mapping v2 ChartResult / ChartSimpleResult into existing BodyGraph/person cache contracts.  
  * Where that proof should exist, if known: a future scoped evidence or implementation slice routed through PF12 / PF14 homes as indicated by the current artifact.  
  * Evidence pointer: Repo → `response_mapping.snapshot.json` → `"required_follow_up":"A bounded adapter/schema proof or implementation must map v2 ChartResult/ChartSimpleResult data into the existing BodyGraph/person cache contract before compatibility can be claimed."`  
* `bg:resolve` v2 chart/geokey semantics remain a runtime gap, not a successful v2 chart/geokey validation path.  
  * What is missing or unclear: geokey posture is proven for v2 `charts/simple`, not for `bg:resolve`.  
  * Why it matters: operators or agents could incorrectly run `bg:resolve --source vendor` as if it were canonical v2 chart/geokey validation.  
  * What would prove it: a current repo implementation/evidence path showing `bg:resolve` no longer uses the legacy BodyGraph route against a v2 base, or a separate canonical workflow documenting the intended path.  
  * Where that proof should exist, if known: PF29 user-guide drainage and any future BodyGraph adapter/ingest proof.  
  * Evidence pointer: Repo → `final_classification.txt` → `"geokey_header_posture_not_proven_for_bg_resolve=true"` | `"runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base"`  
* PF29 drainage remains documentation/canon follow-up.  
  * What is missing or unclear: PF29-Canon-HDE-User-Guide is seeded in PF10 and doc-delta candidates, but this report did not observe a completed PF29 canon document in current repo evidence.  
  * Why it matters: the project now has repeatable operator/agent workflow knowledge that should be drained into a durable user guide.  
  * What would prove it: PF29-Canon-HDE-User-Guide existing as a reviewed PF-Canon doc with the HDE-EPIC035 workflow guidance drained.  
  * Where that proof should exist, if known: PF29 — HDE User Guide.  
  * Evidence pointer: PF10 — HDE-Build Notes → 2.3) PF29 HD Engine User Guide seed → "Drain target: PF29-Canon-HDE-User-Guide" | "This addendum seeds a new permanent PF Canon document"; Repo → `audit/docdeltas/hde-epic035_doc_deltas.md` → `"PF29 should clarify"` | `"PF-Canon was not edited."`  
* Closure decision evidence remains a Lead decision area.  
  * What is missing or unclear: this report does not establish a formal Lead closure decision, close-pack acceptance, or PF09 status edit.  
  * Why it matters: repo reality and PF10-recorded outcomes are evidence; they do not themselves declare closure.  
  * What would prove it: a Lead closure decision or explicitly governed close-pack/closure artifact.  
  * Where that proof should exist, if known: Unknown; likely a future closure/Lead review artifact if assigned.  
  * Evidence pointer: Repo → `token_evidence_matrix.md` → `"This is not a QA plan, Live QA runbook, closeout review, or OPS completion record."` | `"Nonclaims: no QA PASS, no OPS completion, no PF09 status movement"`

Retrospective (Process)

What went well

* The plan held a narrow Fermentation boundary: HDE-FERM008.3 through HDE-FERM008.5 were targeted without public Reader expansion, new HTTP homes, app-side vendor calls, AI scope, or raw payload persistence. Artifact → r1 Implementation Plan HDE-EPIC035 → Brief recap of scope → "HDE-EPIC035 completes the remaining HumanDesignAPI v2 Fermentation live-conformance sequence" | "no public Reader change" | "no AI scope."  
* The implementation split deterministic closed-rails evidence, live OPS evidence, and evidence-loop binding into separate steps. PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "closed rails"; PF10 → 2.4) OPS-01 HDE-EPIC035 → "bounded open-rails"; PF10 → 2.5) PR-03 HDE-EPIC035 → "binds HDE-EPIC035 PR-01, PR-02, and retained OPS-01 evidence."  
* PR-01 remediation surfaced and repaired proof chronology and closed-rails enforcement defects before the evidence posture was treated as historical fact. PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "left material gaps" | "First Remedial PR \#329 corrected" | "Second Remedial PR \#330 addressed the remaining two gaps."  
* PR-02 remediation handled a shared-artifact/indexing conflict without smoothing over the evidence gap. PF10 — HDE-Build Notes → 2.2) PR-02 HDE-EPIC035 → "shared `response_mapping.snapshot.json` path created conflicting EPIC034 / EPIC035 index semantics" | "Remedial PR \#332 fixed those gaps."  
* OPS-01 was ultimately bounded as evidence contribution only, with explicit nonclaims preserved. Repo → `ops_evidence_manifest.txt` → `"Final classification summary:"` | `"v2_charts_simple=success"` | `"Nonclaims:"`  
* PR-03 converted scattered PR/OPS outputs into a governed evidence loop with explicit tests for index, mirror, path proof, token, and nonclaim posture. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `def test_epic035_rows_are_indexed_mirrored_and_path_proven()` | `def test_human_index_machine_mirror_parity_for_epic035()`  
* The docs sweep pushed current HDE-EPIC035 posture into README, CHANGELOG, AGENTS, docs/INDEX.md, docs/CLI\_commands.md, and docs/RUN.md without PF-Canon edits. Repo → `CHANGELOG.md` → `"Unreleased — HDE-EPIC035: Fermentation Pass 6 final repo docs sweep"` | Repo → `audit/docdeltas/hde-epic035_doc_deltas.md` → `"PF-Canon was not edited."`

What did not go well

* PR-01 required two remedial PRs because initial evidence/path-proof chronology and generator closed-rails enforcement were not sufficient. PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "Original PR \#328 left material gaps" | "First Remedial PR \#329" | "Second Remedial PR \#330."  
* PR-02 initially created evidence-index ambiguity by sharing `response_mapping.snapshot.json` between EPIC034 and EPIC035 semantics. PF10 — HDE-Build Notes → 2.2) PR-02 HDE-EPIC035 → "the shared `response_mapping.snapshot.json` path created conflicting EPIC034 / EPIC035 index semantics."  
* OPS-01 execution initially produced a misleading `bg:resolve` outcome for v2 chart/geokey validation because `bg:resolve` remained on the legacy BodyGraph route shape. Repo → `final_classification.txt` → `"bg_resolve_request_shape=/v2/bodygraphs"` | `"bg_resolve_http_status=404"` | `"geokey_header_posture_not_proven_for_bg_resolve=true"`  
* OPS-01 evidence required retained-path mapping because the approved deliverable names and retained evidence paths diverged in format and nesting. Repo → `ops_evidence_manifest.txt` → `"equivalent_by_mapping; nested smoke-root retained"` | `"partial_format_mismatch"` | `"equivalent_by_content_name_mismatch"`  
* PR-02 evidence could not honestly prove the normalized v2 data path, so the output had to record a gap rather than complete the intended "feeds existing HDE flows" proof. Repo → `response_mapping.snapshot.json` → `"mapping_result":"schema_gap_recorded"` | `"not_truthfully_proven_for_v2_chart_data"` | `"no_compatibility_by_inference":true`  
* The final HDE-EPIC035 docs and PF29 seed had to clarify several non-obvious distinctions: v2 chart routes versus legacy BodyGraph routes, evidence contribution versus OPS completion, and repo docs versus PF-Canon drainage. Repo → `audit/docdeltas/hde-epic035_doc_deltas.md` → `"PF29 should clarify"` | `"PF-Canon was not edited."` | `"Nonclaims"`

What we learned (Process)

* PR evidence must test its own governance metadata, not just produce artifacts. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `assert payload["epic_id"] == "HDE-EPIC035"` | `assert names <= ALLOWED_TOKENS` | `assert "VENDOR_V2" not in joined`  
* Shared artifact names across epics create ambiguity unless the loader/index semantics are explicit. PF10 — HDE-Build Notes → 2.2) PR-02 HDE-EPIC035 → "shared `response_mapping.snapshot.json` path created conflicting EPIC034 / EPIC035 index semantics."  
* OPS evidence should include a manifest mapping approved deliverables to retained paths when live evidence roots diverge from plan paths. Repo → `ops_evidence_manifest.txt` → `"Purpose: map approved-plan OPS-01 deliverable names to retained evidence paths"` | `"Approved-plan deliverable"` | `"Retained evidence path"`  
* Nonclaims need to be machine-tested where possible, because evidence artifacts can otherwise be misread as status movement or runtime conformance. Repo → `tests/evidence/test_boundary_logs_are_not_closeout_or_runbooks()` → `assert "closeout_review=false" in text` | `assert "ops_completion_claim=false" in text` | `assert "full_runtime_conformance_claim=false" in text`  
* Evidence-loop closure is stronger when the same tests verify Human Index, Machine Mirror, SHA, path proof, and payload existence. Repo → `tests/evidence/test_epic035_rows_are_indexed_mirrored_and_path_proven()` → `assert required <= set(index_by_path)` | `assert required <= set(mirror_by_path)` | `assert f"sha256: {expected_sha}" in proof_text`  
* Documentation must distinguish current engine workflows from app/product UX; PF10 seeded PF29 as an HD Engine user guide, not an app guide. PF10 — HDE-Build Notes → 2.3) PF29 HD Engine User Guide seed → "PF29 must document HD Engine usage, not the Glow app product UX."  
* Repo-docs drainage can reduce future agent drift, but it remains separate from PF-Canon drainage. Repo → `docs/INDEX.md` → `"PF29 drainage remains PF-Canon follow-up and is not performed in repo docs."`

Retrospective (Application / System)

What we learned about the system itself

* The current HD Engine distinguishes v2 chart-style routes from legacy BodyGraph-style routes by route family and auth posture. Repo → `error_mapping.snapshot.json` → `"v2_chart_routes"` | `"Authorization: Bearer <redacted>"` | `"legacy_v1_bodygraph_routes"`  
* v2 chart/geokey success was observed on `charts/simple`, not on `bg:resolve`. Repo → `final_classification.txt` → `"v2_charts_simple_request_shape=/v2/charts/simple"` | `"v2_charts_simple_response_type=ChartSimpleResult"` | `"geokey_header_posture=proven_for_v2_charts_simple"`  
* `bg:resolve` remains tied to the current legacy BodyGraph ingest path against the configured v2 base in the observed OPS evidence. Repo → `final_classification.txt` → `"bg_resolve_request_shape=/v2/bodygraphs"` | `"runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base"`  
* The current response-normalization proof records that v2 ChartResult / ChartSimpleResult data does not yet have a proven adapter into existing BodyGraph/cache/compat input shapes. Repo → `response_mapping.snapshot.json` → `"schema_gap_summary":"HDE-FERM008.4 remains an exact adapter/schema gap"` | `"required_follow_up"`  
* Closed-rails evidence can prove deterministic classifications, but live/open-rails behavior still requires PO-run evidence and secret-safe capture. PF09.5 — HDE Build Checklist Fermentation → HDE-FERM008 task notes → "open-rails vendor calls require secrets and privileged runtime posture" | "Automated agents must not execute vendor calls or claim completion without PO-run evidence."  
* Existing token posture stayed baseline-existing-token-only; no vendor-v2-specific token was introduced. Repo → `docs/acceptance_map_epic035.json` → `"acceptance_claims_mode":"baseline_existing_tokens_only"` | `"forbidden_vendor_v2_specific_tokens=NONE"` via viability log  
* HDE-EPIC035 evidence artifacts can be validated by repo tests that inspect actual file bytes, SHA, path proofs, and mirror rows. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `expected_sha = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()` | `assert mirror_by_path[rel]["sha256"] == expected_sha` | `assert proof.exists()`  
* Repo docs now carry the operational distinction future agents need: `bg:resolve` is not the canonical v2 chart/geokey validation path. Repo → `docs/CLI_commands.md` → `"HDE-EPIC035 note: --source vendor uses the preserved legacy BodyGraph ingest path."` | `"Do not use it as the canonical v2 chart/geokey validation path"`

Known remaining risks / debt

* Should-fix — Adapter/data-path proof debt: current evidence records a gap for v2 ChartResult / ChartSimpleResult into BodyGraph/cache/compat; future work needs a bounded adapter/schema proof or implementation before compatibility can be claimed. Repo → `response_mapping.snapshot.json` → `"required_follow_up":"A bounded adapter/schema proof or implementation must map v2 ChartResult/ChartSimpleResult data"`  
* Should-fix — `bg:resolve` workflow ambiguity: current evidence shows `bg:resolve` still uses `/v2/bodygraphs` and returns 404; future docs/workflows must keep it out of the canonical v2 chart/geokey path unless implementation changes. Repo → `final_classification.txt` → `"bg_resolve_request_shape=/v2/bodygraphs"` | `"bg_resolve_http_status=404"`  
* Should-fix — PF29 drainage debt: PF10 and repo doc-deltas identify PF29 as the durable home for runnable HD Engine usage guidance; current repo evidence contains candidates, not a completed PF29 canon drain. PF10 — HDE-Build Notes → 2.3) PF29 seed → "Drain target: PF29-Canon-HDE-User-Guide"; Repo → `audit/docdeltas/hde-epic035_doc_deltas.md` → `"PF29 should clarify"`  
* Should-fix — Nested OPS evidence-root convention: OPS-01 retained evidence required manifest mapping due to nested smoke-root paths and text/markdown summary formats; PF29 doc-delta candidates name this as a convention to document. Repo → `ops_evidence_manifest.txt` → `"nested smoke-root retained"` | `"partial_format_mismatch"` | Repo → `hde-epic035_doc_deltas.md` → `"PF29 should clarify acceptable OPS nested evidence-root manifest mapping"`  
* Should-fix — Closure decision ambiguity: current evidence preserves no QA PASS, no OPS completion, no PF09 status movement, no HDE-FERM008 parent Done, and no epic closeout; a Lead decision would need to interpret evidence separately. Repo → `token_evidence_matrix.md` → `"Nonclaims: no QA PASS, no OPS completion, no PF09 status movement, no HDE-FERM008 parent Done, no epic closeout"`  
* Nice-to-have — Repo PF10 version drift visibility: latest session PF10 used for this report is v11.8, while current Repo search surfaced `docs/pfcanon/PF10-HDE-Build-Notes-v11.7.8.md`; this may be normal PF10 workflow but should be visible to Lead if repo-resident PF10 freshness matters. PF10 — HDE-Build Notes → Front Matter → "Version: v11.8"; Repo → GitHub search HDE-EPIC035 → `docs/pfcanon/PF10-HDE-Build-Notes-v11.7.8.md`  
* Nice-to-have — Documentation freshness watch: docs now reflect HDE-EPIC035, but PF29 and PF09 status drainage are still follow-up/out-of-scope in repo docs. Repo → `docs/INDEX.md` → `"PF29 drainage remains PF-Canon follow-up"` | Repo → `README.md` → `"no PF09 status movement"`

Canon Alignment and Documentation Outcomes

5.1 Canon references used

* PF10 — HDE-Build Notes. Used for epic-specific live addenda and historical implementation notes where it explicitly covers HDE-EPIC035 PR-01, PR-02, PF29 seed, OPS-01, and PR-03. PF10 — HDE-Build Notes → Addendum Index → "2.1) PR-01 HDE-EPIC035" | "2.2) PR-02 HDE-EPIC035" | "2.4) OPS-01 HDE-EPIC035" | "2.5) PR-02 HDE-EPIC035."  
* PF09.5 — HDE Build Checklist Fermentation. Used for phase interpretation and HDE-FERM008.3 / .4 / .5 task/subtask semantics. PF09.5 — HDE Build Checklist Fermentation, §Task HDE-FERM008 \- HDAPI v2 live conformance, rails, and evidence.  
* PF12 — HDE Schemas & Artifacts. Used titles-only for Human Evidence Index, Machine Mirror, hash sentinel, canonical JSON, path-proof, and governed artifact interpretation. PF12 — HDE Schemas & Artifacts, §0.2 Scope & single homes.  
* PF04 — HDE Governance. Used titles-only for SAFE rails, evidence/release discipline, logging/privacy, no secrets/PII, and token semantics ownership. PF04 — HDE Governance, §0.2 Scope & boundaries.  
* PF05 — HDE CLI/API/Vendor Ref. Used titles-only for CLI/vendor bytes, headers, vendor ingest, payload shapes, validators, and exact transport/CLI wording homes. PF05 — HDE CLI/API/Vendor Ref, §0.2 Scope.  
* PF06 — Epic Process Guide. Used titles-only for implementation/PF-Canon separation, doc-delta handling, and documentation-drainage posture. PF06 — Epic Process Guide, §0.2 Policy and principles.  
* PF07 — Glow Infrastructure. Used titles-only for infrastructure-owned config/env key names and governed evidence roots. PF07 — Glow Infrastructure, §Intent & scope.  
* PF14 — HDE Mechanics Guide. Used titles-only for mechanics/component interpretation and evidence-tool/harness mechanics boundaries. PF14 — HDE Mechanics Guide, §0.2 Purpose — Components & build tasks.  
* PF19 — Glow QA Guide. Used titles-only for QA posture and phased PF09 reference discipline. PF19 — Glow QA Guide, §0.2 Purpose & scope.  
* PF20 — HDE Phased Epics and PF23 — Reality Audits were not used as current proof sources. PF20 posture was treated as historical-only; PF23 was not used as closure proof, acceptance source, token source, or blocker source. PF20 — HDE Phased Epics → Purpose & Scope → "Historical reference only. Not for planning." | "PF20 MUST NOT be used to plan new epics" | "PF20 itself is not authoritative for planning rules."

Closure Evidence Snapshot (for Lead decision)

6.1 Evidence produced

* PR-01 evidence family: `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` and `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`, with HDE-EPIC035 / HDE-FERM008.3 metadata, route/auth posture, closed-rails no-claim posture, Retry-After/rate-limit records, and provider outcome mapping. Repo → `error_mapping.snapshot.json` → `"pf09_subtask_id":"HDE-FERM008.3"` | Repo → `rate_limit_headers.snapshot.json` → `"pf09_subtask_id":"HDE-FERM008.3"`  
* PR-02 evidence family: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` and `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`, with exact schema/adapter gap posture and PR-01/PR-02 binding. Repo → `response_mapping.snapshot.json` → `"response_normalization_posture":"EXACT_SCHEMA_ADAPTER_GAP_RECORDED"` | Repo → `release_binding.snapshot.json` → `"release_binding_posture":"PR02 binds PR01"`  
* OPS-01 evidence family: retained evidence under `audit/ops/hde-epic035/ops-01/`, including manifest, final classification, v2 charts/simple evidence, bgresolve error capture, checksum ledger, and mapped retained paths. Repo → `ops_evidence_manifest.txt` → `"Additional retained evidence"` | `"final_classification.txt"` | `"files_sha256.txt"`  
* PR-03 acceptance-boundary and evidence-loop artifacts: `docs/acceptance_map_epic035.json`, `audit/qa/hde-epic035/token_evidence_matrix.md`, `audit/qa/hde-epic035/acceptance_map_viability.log`, `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`, and `audit/docdeltas/hde-epic035_doc_deltas.md`. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → constants for `ACCEPTANCE`, `MATRIX`, `VIABILITY`, `BINDING`, `HUMAN_INDEX`, and `MIRROR`  
* Human Evidence Index / Machine Mirror posture: HDE-EPIC035 PR-03 tests assert required HDE-EPIC035 paths are in both the Human Index and Machine Mirror and that path proofs match SHA. Repo → `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` → `assert required <= set(index_by_path)` | `assert required <= set(mirror_by_path)` | `assert f"sha256: {expected_sha}" in proof_text`  
* Token names referenced by current acceptance-boundary evidence: `DOC_DELTA_PRESENT_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_PATH_PROOFS_OK`, `JSON_CANONICAL_CHECK_OK`, and `TESTS_PASS_OK`. This report does not independently claim token satisfaction as an epic closure verdict. Repo → `token_evidence_matrix.md` → token table rows  
* Repo docs produced/updated: README, CHANGELOG, AGENTS, docs/INDEX.md, docs/CLI\_commands.md, and docs/RUN.md now carry HDE-EPIC035 evidence posture and nonclaims. Repo → `CHANGELOG.md` → `"Unreleased — HDE-EPIC035: Fermentation Pass 6 final repo docs sweep"`

6.2 Evidence missing or ambiguous

* Missing/ambiguous: formal Lead closure decision or close-pack proof.  
  * What would prove it: a Lead closure memo, close-pack artifact, or explicit governed closure record.  
  * Where that proof should exist, if known: Unknown.  
  * Evidence pointer: current HDE-EPIC035 boundary artifacts explicitly say they are not closeout artifacts. Repo → `token_evidence_matrix.md` → `"This is not a QA plan, Live QA runbook, closeout review, or OPS completion record."`  
* Missing/ambiguous: adapter/schema implementation or proof that v2 ChartResult / ChartSimpleResult feeds existing BodyGraph/cache/compat.  
  * What would prove it: bounded adapter/schema proof or implementation mapped to existing BodyGraph/person contracts.  
  * Where that proof should exist, if known: future PF12 / PF14 routed evidence or implementation artifact.  
  * Evidence pointer: Repo → `response_mapping.snapshot.json` → `"schema_gap_status":"GAP_RECORDED"` | `"required_follow_up"`  
* Missing/ambiguous: canonical PF29 drained guide.  
  * What would prove it: reviewed PF29 — HDE User Guide with HDE-EPIC035 HD Engine runnable workflow guidance drained.  
  * Where that proof should exist, if known: PF29 — HDE User Guide.  
  * Evidence pointer: Repo → `audit/docdeltas/hde-epic035_doc_deltas.md` → `"PF29 should clarify"` | `"PF-Canon was not edited."`  
* Missing/ambiguous: PF09 status movement, HDE-FERM008 parent status, or whole-epic closure status.  
  * What would prove it: a separate PF09.5 update or Lead decision artifact that explicitly records status movement.  
  * Where that proof should exist, if known: PF09.5 — HDE Build Checklist Fermentation and/or Lead closure record.  
  * Evidence pointer: Repo → `docs/acceptance_map_epic035.json` → `"pf09_scope_not_completed_by_this_pr":["HDE-FERM008 parent","PF09 status drainage","epic closeout"]`

6.3 Open closure items / questions for the Lead

* Should the evidence set support a later PF09.5 status-drain update for HDE-FERM008.3, HDE-FERM008.4, and/or HDE-FERM008.5? PF10 records status recommendations for the PR slices, but this report does not edit PF09 or declare status movement. PF10 — HDE-Build Notes → 2.1) PR-01 HDE-EPIC035 → "supports a status recommendation"; PF10 → 2.2) PR-02 HDE-EPIC035 → "supports a status recommendation"; PF10 → 2.5) PR-03 HDE-EPIC035 → "supportable for a later PF09 status change."  
* Should PF29 drainage be assigned now, and should it include both the `bg:resolve` warning and nested OPS evidence-root manifest convention? Repo → `audit/docdeltas/hde-epic035_doc_deltas.md` → `"PF29 should clarify that hdctl bg:resolve --source vendor is a legacy BodyGraph ingest-path observation"` | `"PF29 should clarify acceptable OPS nested evidence-root manifest mapping"`  
* Should future implementation work address the ChartResult / ChartSimpleResult adapter gap, or is the current recorded gap sufficient for the present evidence slice? Repo → `response_mapping.snapshot.json` → `"required_follow_up":"A bounded adapter/schema proof or implementation must map v2 ChartResult/ChartSimpleResult data into the existing BodyGraph/person cache contract"`  
* Should the project keep `bg:resolve --source vendor` as legacy BodyGraph ingest behavior, or should future runtime work align it with the v2 chart/geokey path? Repo → `final_classification.txt` → `"bg_resolve_request_shape=/v2/bodygraphs"` | `"v2_charts_simple_request_shape=/v2/charts/simple"` | `"runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base"`  
* Should latest PF10 v11.8 be made repo-visible or drained before the Lead uses repo-only artifacts for closure review? PF10 — HDE-Build Notes → Front Matter → "Version: v11.8"; Repo → GitHub search HDE-EPIC035 → `docs/pfcanon/PF10-HDE-Build-Notes-v11.7.8.md`

## **2.7) ADR — ChartResult adapter gap is accepted for HDE-EPIC035 evidence, but future runtime work must prove full BodyGraph-detail mapping**

Timestamp: 062925

Status: Live Lead decision

Decision owner: Isis / Lead Dev

### **Decision**

The current recorded `ChartResult` / `ChartSimpleResult` adapter gap is sufficient for the present HDE-EPIC035 evidence slice.

It is not sufficient for future runtime, production, app-integration, or BodyGraph-resolution claims.

Future implementation work must address the adapter/schema gap before claiming that HumanDesignAPI v2 chart data feeds the existing HD Engine BodyGraph/person/cache/compatibility contract.

### **Report basis**

The HDE-EPIC035 report records the current repo posture as an exact schema/adapter gap, not a normalized data-path proof:

`Repo → response_mapping.snapshot.json → "schema_gap_summary":"HDE-FERM008.4 remains an exact adapter/schema gap"`

`Repo → response_mapping.snapshot.json → "required_follow_up":"A bounded adapter/schema proof or implementation must map v2 ChartResult/ChartSimpleResult data into the existing BodyGraph/person cache contract before compatibility can be claimed."`

The report also records that v2 chart/geokey success was observed on `charts/simple`, not on `bg:resolve`, and that `ChartSimpleResult` was the observed response type for that narrow smoke.

### **Clarification**

The HDE-EPIC035 evidence slice truthfully recorded the gap.

That is acceptable for HDE-EPIC035 because the epic’s purpose included exact adapter/schema gap recording and governed evidence-loop closure.

But the recorded gap cannot be reused later as proof that v2 chart data already feeds BodyGraph, cache, compatibility, or compute flows.

### **Vendor payload decision**

The HD Engine needs enough vendor payload detail to resolve full BodyGraph details for HD computation and later Glow app integration.

`ChartSimpleResult` is not the preferred product/runtime source for BodyGraph detail.

`ChartSimpleResult` may remain useful for:

* bounded live smoke;  
* authentication proof;  
* geocode-key proof;  
* provider availability proof;  
* minimal route-family confirmation.

`ChartSimpleResult` must not be treated as sufficient for the full BodyGraph/person/cache contract unless a future bounded adapter/schema proof demonstrates that it contains every required field.

The preferred future v2 payload candidate is the richest relevant v2 chart response, currently understood as the full chart route / `ChartResult` family, not the simple chart response.

If full `ChartResult` does not contain all BodyGraph details required by the HD Engine, future implementation must record the exact field gap and either:

* define a sanctioned adapter strategy;  
* identify the correct vendor route for full BodyGraph detail;  
* retain explicit legacy fallback;  
* or raise a new ADR before claiming runtime compatibility.

### **Runtime claim rule**

Future work must not claim any of the following until the adapter/schema proof or implementation exists:

* v2 chart data feeds existing BodyGraph cache;  
* v2 chart data feeds existing person/bodygraph compute input;  
* v2 chart data replaces legacy BodyGraph ingest;  
* `ChartSimpleResult` is sufficient for BodyGraph detail;  
* full vendor runtime conformance;  
* full HDE-FERM008 parent completion from HDE-EPIC035 evidence alone.

### **Evidence rule**

A future proof must show, in governed and secret-safe form:

* which vendor payload family is used;  
* which response fields are required;  
* which internal BodyGraph/person/cache fields are populated;  
* which fields are intentionally absent or unsupported;  
* whether the adapter is lossless enough for HD Engine compute;  
* whether any legacy fallback remains;  
* whether raw vendor payloads are persisted, redacted, summarized, or excluded;  
* what the normalized internal output contract is.

The proof must not persist raw secrets or uncontrolled raw vendor payloads.

### **HDE-EPIC035 scope interpretation**

HDE-EPIC035 remains valid as an evidence and gap-recording slice.

The recorded gap is not a failure of HDE-EPIC035.

The recorded gap is a future implementation boundary.

### **Implementation impact**

Future implementation work that claims v2 BodyGraph resolution must include a bounded adapter/schema proof or implementation.

That work must decide the actual product/runtime payload:

* full v2 chart response if sufficient;  
* another v2 route if required;  
* explicit legacy BodyGraph fallback if v2 cannot provide required detail;  
* or a new ADR if the vendor payload strategy cannot be decided from available evidence.

### **Drain targets**

#### **PF05 — HDE CLI/API Vendor Ref**

Drain intent:

* Record that `ChartSimpleResult` is not presumed sufficient for full BodyGraph detail.  
* Record that future runtime work must identify the vendor payload family that actually supports BodyGraph/person/cache needs.  
* Preserve the distinction between v2 chart smoke, v2 full chart payload, legacy BodyGraph payload, and normalized HD Engine BodyGraph contract.

#### **PF14 — HDE Mechanics Guide**

Drain intent:

* Add mechanics guidance for mapping vendor chart payloads into the HD Engine BodyGraph/person/cache contract.  
* Require explicit adapter/schema proof before v2 chart data is treated as compute-ready BodyGraph data.  
* Preserve the distinction between response-envelope proof and normalized data-path proof.

#### **PF12 — HDE Schemas and Artifacts**

Drain intent:

* Define governed evidence posture for adapter/schema proof.  
* Require evidence to distinguish raw vendor payload shape, normalized internal shape, field coverage, and nonclaims.  
* Preserve secret-safe and payload-safe evidence rules.

#### **PF19 — Glow QA Guide**

Drain intent:

* Require QA to verify the actual normalized BodyGraph-detail contract when a future epic claims v2 chart-to-BodyGraph compatibility.  
* Prevent QA from accepting a simple chart smoke as proof of full BodyGraph resolution.

#### **PF27 — Canon Plan Templates**

Drain intent:

* Require plans involving vendor payload normalization to state whether they prove a real data-path adapter or only record a schema gap.  
* Require explicit nonclaim language when adapter/schema proof is not included.

#### **PF09.5 — HDE Build Checklist Fermentation**

Drain intent:

* Clarify that HDE-FERM008.4 is not satisfied by recording a gap alone unless the subtask’s scoped epic is explicitly gap-recording only.  
* Future runtime completion requires adapter/schema proof or implementation.

### **Supersedes / conflicts**

This addendum supersedes any interpretation that HDE-EPIC035’s recorded gap is enough for future runtime compatibility.

It does not supersede HDE-EPIC035’s evidence-slice validity.

### **Final authority**

Until drained, PF10 is the live source of truth:

The ChartResult / ChartSimpleResult adapter gap is accepted for HDE-EPIC035 evidence, but future runtime work must prove the full BodyGraph-detail mapping before compatibility is claimed.

---

## **2.8) ADR — `bg:resolve --source vendor` must resolve BodyGraph detail through an explicit vendor-route policy, not accidental legacy route composition**

Timestamp: 062925

Status: Live Lead decision

Decision owner: Isis / Lead Dev

### **Decision**

`bg:resolve --source vendor` must remain a supported HD Engine workflow for resolving BodyGraph details.

It must not remain accidentally coupled to legacy BodyGraph route composition when the configured vendor base is v2.

Future runtime work must align `bg:resolve --source vendor` with an explicit vendor-route policy that can truthfully resolve the required BodyGraph detail.

### **Report basis**

The HDE-EPIC035 report records the current runtime gap:

`Repo → final_classification.txt → "bg_resolve_request_shape=/v2/bodygraphs"`

`Repo → final_classification.txt → "v2_charts_simple_request_shape=/v2/charts/simple"`

`Repo → final_classification.txt → "runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base"`

The report also records:

`Repo → final_classification.txt → "bg_resolve_http_status=404"`

`Repo → final_classification.txt → "geokey_header_posture_not_proven_for_bg_resolve=true"`

### **Clarification**

The project does need to resolve BodyGraph details.

Therefore, the long-term answer cannot be: leave `bg:resolve --source vendor` as a broken or ambiguous legacy route call.

The current evidence is acceptable as a gap record.

It is not acceptable as future runtime posture.

### **Vendor route policy**

Future `bg:resolve --source vendor` behavior must choose one of the following explicitly:

#### **Option A — v2 chart-backed BodyGraph resolution**

Use the correct v2 chart route family, prove the response contains the required BodyGraph detail, and map it into the existing HD Engine BodyGraph/person/cache contract.

This is preferred if the full v2 chart payload contains the necessary detail.

#### **Option B — explicit legacy BodyGraph fallback**

Preserve legacy v1 BodyGraph ingest as an explicit fallback or compatibility mode.

This is allowed only if it is clearly configured and does not accidentally compose legacy resource paths against a v2 base URL.

#### **Option C — dual-route policy**

Use v2 chart routes as the primary path and legacy BodyGraph routes only for fields not available in v2, if such a hybrid is explicitly justified and secret-safe.

This requires a future ADR because it creates a more complex vendor contract.

#### **Option D — no runtime vendor resolution claim**

If neither v2 chart nor legacy BodyGraph fallback can be safely proven, do not claim runtime vendor resolution.

Record the unresolved adapter/vendor-route gap instead.

### **Invalid future posture**

The following are not acceptable as final runtime behavior:

* composing `/v2/bodygraphs` accidentally from a v2 base URL and legacy BodyGraph resource path;  
* treating `bg:resolve` 404 as vendor unavailability when the request shape is wrong;  
* using `charts/simple` as proof of full BodyGraph resolution;  
* using simple chart success as proof that bodygraph detail exists;  
* silently switching between v1 and v2 route families without evidence;  
* storing or computing from partial vendor payloads while claiming full BodyGraph resolution;  
* moving vendor resolution into the Glow app layer to avoid the HD Engine adapter work.

### **Base URL and route composition rule**

Vendor API version ownership remains with the configured base URL.

Runtime resource paths must be selected from the intended route family.

If the configured base URL is v2, `bg:resolve --source vendor` must not append a legacy `bodygraphs` resource unless that combination is explicitly supported by vendor evidence and PF10 or permanent PF canon.

If the implementation needs both v1 and v2 route families at runtime, future work must explicitly define the base-url/config strategy.

It must not overload `HD_API_BASE_URL` in a way that makes route-family behavior ambiguous.

If separate v1 and v2 base URLs are required, that requires infrastructure and vendor-contract clarification before runtime claims are made.

### **BodyGraph detail requirement**

The HD Engine must preserve the ability to resolve the BodyGraph detail required for:

* HD computation;  
* BodyGraph/person cache contract;  
* compatibility helpers;  
* future Glow app use of HD Engine outputs.

The exact vendor source for those details must be proven, not assumed.

### **Relationship to `charts/simple`**

`charts/simple` may remain useful for:

* proving the provider responds;  
* proving v2 auth posture;  
* proving geocode-key posture;  
* proving route-family availability.

It is not the canonical proof of full BodyGraph detail.

Future QA, OPS, or implementation plans must not treat `charts/simple` success as proof that `bg:resolve` can resolve complete BodyGraph data.

### **HDE-EPIC035 scope interpretation**

HDE-EPIC035 correctly recorded that `bg:resolve` remains a runtime gap.

That gap record is sufficient for HDE-EPIC035’s evidence slice.

The gap must be addressed before any future claim that `bg:resolve --source vendor` works as the canonical v2 BodyGraph-resolution path.

### **Implementation impact**

Future runtime work must either:

* update `bg:resolve --source vendor` to use the correct v2 chart-backed adapter path;  
* preserve an explicit legacy BodyGraph fallback with correct base-url semantics;  
* or record that vendor BodyGraph resolution remains unsupported pending a vendor-payload decision.

No future plan may treat the current `bg:resolve` runtime gap as acceptable production behavior.

### **QA impact**

Future QA must prove the actual selected behavior:

* if v2 chart-backed resolution is implemented, QA must prove it resolves sufficient BodyGraph detail;  
* if legacy fallback is preserved, QA must prove it is explicit, correctly configured, and not version-mismatched;  
* if dual-route behavior is implemented, QA must prove the selection logic and nonclaim boundaries;  
* if no runtime claim is made, QA must preserve that nonclaim.

### **Drain targets**

#### **PF05 — HDE CLI/API Vendor Ref**

Drain intent:

* Define the vendor-route policy for `bg:resolve --source vendor`.  
* Distinguish v2 chart routes, legacy BodyGraph routes, and simple chart smoke.  
* Forbid accidental `/v2/bodygraphs` composition unless vendor evidence explicitly supports it.  
* Clarify when legacy fallback is allowed.

#### **PF07 — Glow Infrastructure**

Drain intent:

* Clarify whether one canonical base URL is sufficient when both v1 and v2 routes are needed.  
* If dual version support is required, define a safe infrastructure posture for separate base URLs or route-family config.  
* Preserve secret-safe environment handling.

#### **PF14 — HDE Mechanics Guide**

Drain intent:

* Define BodyGraph resolution mechanics for vendor-backed resolution.  
* Clarify how `bg:resolve --source vendor` selects route family, maps payload, handles fallback, and stores or retrieves normalized data.  
* Preserve HD Engine ownership of BodyGraph resolution.

#### **PF12 — HDE Schemas and Artifacts**

Drain intent:

* Define evidence semantics for proving `bg:resolve` vendor route selection and normalized BodyGraph output.  
* Require evidence to distinguish simple route availability from full BodyGraph detail resolution.

#### **PF19 — Glow QA Guide**

Drain intent:

* Require QA to test the actual chosen BodyGraph-resolution path, not a nearby smoke route.  
* Require QA to classify route-shape mismatch separately from provider unavailability.

#### **PF27 — Canon Plan Templates**

Drain intent:

* Require future plans involving `bg:resolve --source vendor` to state whether the command is v2 chart-backed, legacy fallback, dual-route, or unsupported.  
* Require nonclaim language when `bg:resolve` is not covered.

#### **PF09.5 — HDE Build Checklist Fermentation**

Drain intent:

* Clarify that live conformance and normalized data-path closure require an actual bodygraph-resolution policy.  
* Preserve HDE-FERM008.4 / HDE-FERM008.5 distinction from simple v2 provider smoke.

### **Supersedes / conflicts**

This addendum supersedes any interpretation that `bg:resolve --source vendor` can remain accidentally legacy while being treated as the canonical v2 BodyGraph-resolution path.

It does not prohibit an explicit legacy fallback.

It does prohibit ambiguous route composition and unsupported runtime claims.

### **Final authority**

Until drained, PF10 is the live source of truth:

`bg:resolve --source vendor` must continue to resolve BodyGraph details, but future work must align it with an explicit vendor-route policy and must not treat the current legacy-route runtime gap as acceptable final behavior.

\<eof\>