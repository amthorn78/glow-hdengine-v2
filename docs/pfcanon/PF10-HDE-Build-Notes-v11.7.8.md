# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v11.7.8  
Effective Date: 2026.06.28

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

\<eof\>