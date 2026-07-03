# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v11.9.4  
Effective Date: 2026.07.03

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

2.1) Audit Provenance Is Valid Planning Context and Must Not Be Treated as a Plan Blocker

2.2) PR-01 HDE-EPIC036

2.3) Production/User-Surface Epics Must Include At Least One Open-Rails QA Step

2.4) PR-02 HDE-EPIC036

2.5) Implementation Retrospective HDE-EPIC036

2.6) Post Implementation Audit Triage HDE-EPIC035

2.7) QA Pass 1 HDE-EPIC036

# 2\) Numbered Addenda

---

### **2.1) Audit Provenance Is Valid Planning Context and Must Not Be Treated as a Plan Blocker**

Timestamp: 063026

Status: Live PF10 staging decision pending permanent PF-Canon drain

Decision owner: Lead Dev

### **Details**

A plan review incorrectly treated “audit provenance” language inside an Implementation Plan as a blocker.

That interpretation is wrong.

Audits exist to preserve observed planning context, repo-reality findings, ambiguity history, drift history, risk classification, and why a piece of work is being planned. Audit provenance is allowed in Epic Plans, Implementation Plans, QA Guides, QA Plans, review artifacts, and retrospectives when it is used as planning context or source-trace context.

The valid boundary is not “no audit provenance in plans.”

The valid boundary is:

**Audit provenance may be referenced in plans, but it must not be converted into PR instructions, OPS instructions, execution authority, acceptance proof, token authority, or current repo proof without the appropriate governing source or live repo validation.**

### **Lead decision**

Audit provenance is valid and useful in planning artifacts.

It is not a blocker for a plan to include audit provenance when the audit reference explains:

* why work exists;  
* what prior review observed;  
* what risk or ambiguity was surfaced;  
* what repo area should be inspected;  
* what PF-canon or PF09 mapping may need attention;  
* why a future proof obligation exists;  
* why a gap is being carried into an epic;  
* why an implementation or QA plan includes a specific workstream.

### **Permitted use**

Plans may reference audit provenance as:

* planning context;  
* risk context;  
* discovery context;  
* source-trace context;  
* rationale for inspection;  
* rationale for a Tracked Issue;  
* rationale for an ADR stub;  
* rationale for a planned workstream;  
* rationale for a QA proof obligation;  
* rationale for a repo-validation check;  
* rationale for PF-canon drainage.

This includes wording such as:

* “Prior audit observed...”  
* “Audit provenance indicates...”  
* “The audit classified...”  
* “The audit surfaced...”  
* “Prior read-only audit reported...”  
* “Audit context for this work...”

Such wording is allowed when it does not command execution by itself and does not replace PF-canon, PF10, PF09, or repo validation.

### **Prohibited use**

Audit provenance must not be used as:

* PR instructions;  
* OPS instructions;  
* step-by-step execution procedure;  
* Codex command source;  
* acceptance authority;  
* token authority;  
* QA PASS proof;  
* OPS completion proof;  
* PF09 Done proof;  
* closeout proof;  
* current repo truth without repo validation;  
* source of invented file/path/module/test existence;  
* source of required deliverables unless the plan or PF source adopts them;  
* source of privileged live action;  
* source of secrets or external state.

Audit provenance can say why something should be inspected or planned. It cannot by itself prove that current repo contents exist, that execution succeeded, or that acceptance is satisfied.

### **Review rule**

Reviewers must not block a plan solely because it includes audit provenance.

A blocker is valid only if the plan uses audit provenance incorrectly by turning it into execution authority or proof authority.

Allowed review classification:

* No issue  
* Note  
* Context accepted  
* Planning provenance accepted  
* Repo validation required before execution  
* Keep out of PR/OPS instruction text

Forbidden review classification when audit provenance is only context:

* Blocker  
* REVISE AND RESUBMIT  
* QA-readiness blocker  
* implementation blocker  
* evidence/proof blocker  
* token blocker  
* OPS blocker  
* repo-state blocker

### **Required review test**

Before raising a blocker about audit provenance, the reviewer must ask:

1. Is the audit being used only to explain why the work exists?  
2. Is the audit being used only to guide repo inspection, PF mapping, or proof planning?  
3. Does the plan still rely on PF10, PF-Canon, PF09, and repo validation for authority?  
4. Does the plan avoid making the audit itself a command source?  
5. Does the plan avoid making the audit itself acceptance proof?  
6. Does the plan avoid making the audit itself current repo proof?

If the answer is yes, the audit provenance is allowed and not a blocker.

### **PR and OPS boundary**

Audit provenance may appear in plan context, task rationale, Tracked Issues, ADR stubs, evidence rationale, or review history.

Audit provenance should not appear as the operative instruction inside PR or OPS execution blocks.

For PR and OPS instructions, convert audit provenance into neutral work language, such as:

* inspect the current repo state;  
* validate the current route policy;  
* prove the current behavior;  
* update the governed evidence;  
* preserve the nonclaim;  
* bind the evidence under the governed root.

Do not tell Codex or an OPS executor to “implement the audit finding” as though the audit itself is the source of authority.

### **HDE-EPIC036 application**

For HDE-EPIC036, references to prior audit provenance in the Implementation Plan are allowed as planning context.

The prior blocker based on audit provenance is withdrawn.

Audit provenance may remain in the plan when it explains why the `bg:resolve --source vendor` route-policy work exists, why evidence roots are planned, or why a proof obligation is included.

The plan should only avoid making audit provenance the direct PR or OPS instruction source. The operative implementation and evidence instructions must still be grounded in PF10, PF09.5, PF05, PF12, PF14, PF19, PF27, and current repo validation.

### **Permanent PF-Canon drain targets**

#### **PF27 — Canon Plan Templates**

Drain intent:

* Clarify that audit provenance is allowed in plans as planning context.  
* Require plans to distinguish audit context from PR/OPS instructions.  
* Prohibit reviewers from blocking solely because audit provenance appears in a plan.

#### **PF06 — Epic Process Guide**

Drain intent:

* Clarify that audits are legitimate planning inputs.  
* State that audit findings may justify workstreams, Tracked Issues, and ADR stubs.  
* State that audit findings must not become execution authority unless adopted by PF-canon, PF10, plan scope, or repo validation.

#### **PF19 — Glow QA Guide**

Drain intent:

* Clarify that audit provenance can guide QA proof obligations.  
* Clarify that audit provenance does not prove QA PASS, OPS completion, acceptance, or current repo state.

#### **PF23 — Reality Audits**

Drain intent:

* Clarify the allowed role of audits as planning-time context.  
* State that audit findings may be referenced in plans but must be repo-validated for current reality claims.

#### **PF03 — Technical Writing Best Practices**

Drain intent:

* Add language for cleanly separating audit provenance, rationale, and operative task instructions.

### **Final live rule**

Audit provenance is allowed in plans.

Audit provenance is not a blocker.

Audit provenance may explain why work exists.

Audit provenance may guide inspection and proof planning.

Audit provenance must not become PR or OPS instruction text.

Audit provenance must not replace PF-canon, PF10, PF09, repo validation, QA evidence, OPS evidence, acceptance proof, or token authority.

## 2.2) PR-01 HDE-EPIC036

Artifact Map

PR Name: PR-01

Merged PR Ref: 335

Approved Plan: Implementation Plan HDE-EPIC036.md

Optional PR Artifacts: provided

Repo root reviewed: remote GitHub repository `amthorn78/glow-hdengine-v2`, branch `main`, merged change `bb419ce9264a5028ad819ebb147bf9b072dfef02`

Output: Post-Merge PR Code Review and Validation

Review Summary

* The merged change implements explicit `bg:resolve --source vendor` route-policy classification for HDE-EPIC036 PR-01, selecting `unsupported_runtime_nonclaim` for configured v2 bases and preserving explicit legacy BodyGraph fallback for non-v2 bases.  
* The merged change aligns with the Approved Plan’s PR-01 scope: no public Reader change, no new HTTP home, no app-side HumanDesignAPI ownership, no AI scope, no raw payload persistence, no full v2 runtime-conformance claim, and no OPS execution.  
* The exact merged change set was identified as PR \#335, merged into `main` at `bb419ce9264a5028ad819ebb147bf9b072dfef02`; `main` is identical to that merge commit.  
* Final code state shows policy classification before request construction, closed-rails refusal before route-policy logic, unified vendor config source for resolver and ingest, and route metadata driven auth posture.  
* The first three automated review findings in the Optional PR Artifacts were addressed in subsequent commits before merge: partial env base resolution, evidence index registration, and process credential preservation.  
* Evidence artifacts were produced under `artifacts/vendor/hdapi_v2/` and `audit/qa/hde-epic036/`, with path proofs and Human Index / Machine Mirror updates.  
* Validation was not re-executed locally because review access was through the remote GitHub connector, not a mutable checkout. Validation was evaluated from current repo file state, merged PR metadata, Optional PR Artifacts, and final changed files.  
* The material validation roster reported in the Optional PR Artifacts is sufficient for post-merge review scope: targeted pytest, evidence generator `--check`, evidence index `--check`, orientation check, mirror schema check, evidence hash check, py\_compile, and diff check.  
* PF09 impact is HDE-FERM008 / HDE-FERM008.6 in PF09.5. Current PF09 status remains `Not done`; no PF09 status change is recommended from PR-01 alone because PR-02 evidence-loop binding remains follow-up in the Approved Plan and in the merged evidence.

Repo Inspection

Observed repo root:  
Repo proof: GitHub.get\_repo / GitHub PR inspection → repository `amthorn78/glow-hdengine-v2`, default branch `main`.

Observed HEAD:  
Repo proof: GitHub.compare\_commits → base `bb419ce9264a5028ad819ebb147bf9b072dfef02` vs head `main` returned `status: identical`, `ahead_by: 0`, `behind_by: 0`, `total_commits: 0`.

Branch or detached state:  
Repo proof: GitHub.get\_pr\_info → PR \#335 base branch `main`; GitHub.compare\_commits confirms `main` currently equals merge commit `bb419ce9264a5028ad819ebb147bf9b072dfef02`.

Working tree status before review:  
Repo proof: remote GitHub connector review only; no local mutable working tree was available. This does not prevent review because the merged commit and final branch state are immutable through GitHub inspection.

How MERGED\_PR\_REF was resolved:  
Repo proof: GitHub.get\_pr\_info → PR \#335 is `closed`, `merged: true`, `merge_commit_sha: bb419ce9264a5028ad819ebb147bf9b072dfef02`, base `main`, head SHA `a79d44e2b0c5bd195eb7b4460ec8c6f0dcb718d4`.  
Repo proof: GitHub.search\_commits → `bb419ce9264a5028ad819ebb147bf9b072dfef02` has message for PR \#335 and was created at merge time.

Changed files reviewed:  
Repo proof: GitHub.list\_pr\_changed\_filenames → 57 changed files returned and reviewed:  
`artifacts/evidence_index.jsonl`; `artifacts/evidence_index.jsonl.path_proof.txt`; `artifacts/evidence_index.jsonl.sha256`; `artifacts/evidence_index.jsonl.sha256.path_proof.txt`; `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; `artifacts/narratives/router/parity_abba.log.path_proof.txt`; `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`; `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`; `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`; `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`; `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`; `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`; `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`; `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`; `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`; `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`; `artifacts/writer/conjunction_write_readback.log.path_proof.txt`; `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`; `audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; `audit/docdeltas/hde-epic035_doc_deltas.md.path_proof.txt`; `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`; `audit/gates/narratives/pack_identity.txt.path_proof.txt`; `audit/gates/narratives/registry.diff.json.path_proof.txt`; `audit/gates/topology/orientation_demo.txt`; `audit/gates/topology/orientation_demo.txt.path_proof.txt`; `audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`; `audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`; `audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`; `audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; `audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt`; `audit/qa/hde-epic035/00_meta/doc_deltas.md.path_proof.txt`; `audit/qa/hde-epic035/acceptance_map_viability.log.path_proof.txt`; `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log.path_proof.txt`; `audit/qa/hde-epic035/token_evidence_matrix.md.path_proof.txt`; `audit/qa/hde-epic036/route_policy_decision.log`; `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`; `docs/acceptance_map_epic035.json.path_proof.txt`; `docs/evidence/INDEX.json`; `docs/evidence/INDEX.json.path_proof.txt`; `docs/evidence/INDEX.sha256`; `docs/evidence/INDEX.sha256.path_proof.txt`; `engine/bodygraph/ingest.py`; `engine/bodygraph/resolver.py`; `engine/bodygraph/vendor_client.py`; `engine/cli/main.py`; `tests/bodygraph/test_bg_resolve_route_policy.py`; `tests/bodygraph/test_resolver_vendor.py`; `tests/cli/test_bg_resolve.py`; `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`; `tools/evidence/update_evidence_index.py`.

Working tree status after validation:  
Repo proof: no local validation commands were run in a mutable working tree; GitHub remote state remained `main` identical to merge commit after review.

Changed File Review

CFR-001

File: artifacts/evidence\_index.jsonl

Change summary: Machine Mirror records were regenerated and HDE-EPIC036 PR-01 evidence entries were added for route policy, BodyGraph-detail proof, runtime nonclaims, request shape, policy binding, and route-policy decision log.

Risk assessment: High

Code review assessment: Governed evidence surface was changed; final entries include HDE-EPIC036 artifacts with expected paths, roles, sha256 values, proof anchors, and tokens. Broad timestamp churn for older artifacts is present but appears generated by the evidence-index refresh, not hand-edited payload drift.

Approved Plan linkage: Supports PR-01 evidence output registration and same-PR governed evidence posture.

Repo proof: GitHub PR diff and final artifact entries → HDE-EPIC036 records include `hdapi_v2.bg_resolve_route_policy`, `hdapi_v2.bg_resolve_bodygraph_detail_proof`, `hdapi_v2.bg_resolve_runtime_nonclaims`, `hdapi_v2.bg_resolve_request_shape`, `hdapi_v2.bg_resolve_policy_binding`, and `epic036.pr01.route_policy_decision`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-002

File: artifacts/evidence\_index.jsonl.path\_proof.txt

Change summary: Machine Mirror path proof was refreshed for the new mirror size and hash.

Risk assessment: High

Code review assessment: The path proof coheres with the updated mirror path and generated evidence refresh.

Approved Plan linkage: Supports governed path-proof discipline for PR-01 evidence outputs.

Repo proof: GitHub PR diff → path `artifacts/evidence_index.jsonl`, updated size `185206`, updated sha256, updated produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-003

File: artifacts/evidence\_index.jsonl.sha256

Change summary: Machine Mirror sha256 sidecar was updated.

Risk assessment: Medium

Code review assessment: Expected sidecar update for changed mirror bytes.

Approved Plan linkage: Supports evidence hash posture.

Repo proof: GitHub PR diff → sidecar now records hash `7656afb91c3a7e9ea0f0e010377831e0bfacb0635ff33b51b70eb1bf25747b29`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-004

File: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt

Change summary: Path proof for mirror sha256 sidecar was refreshed.

Risk assessment: Medium

Code review assessment: Expected generated proof update for changed sidecar.

Approved Plan linkage: Supports path-proof discipline.

Repo proof: GitHub PR diff → path `artifacts/evidence_index.jsonl.sha256`, updated sha256 and produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-005

File: artifacts/narratives/router/cli\_http\_parity.log.path\_proof.txt

Change summary: Existing path-proof timestamp was refreshed.

Risk assessment: Low

Code review assessment: No underlying payload hash change was observed in the PR diff excerpt; timestamp churn appears generated by evidence refresh.

Approved Plan linkage: Incidental evidence refresh; not part of PR-01 functional route-policy scope.

Repo proof: GitHub PR diff → path proof retains same path, size, and sha256 while mtime/produced timestamps changed.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-006

File: artifacts/narratives/router/parity\_abba.log.path\_proof.txt

Change summary: Existing path-proof timestamp was refreshed.

Risk assessment: Low

Code review assessment: No underlying payload hash change was observed in the PR diff excerpt; timestamp churn appears generated by evidence refresh.

Approved Plan linkage: Incidental evidence refresh; not part of PR-01 functional route-policy scope.

Repo proof: GitHub PR diff → path proof retains same path, size, and sha256 while mtime/produced timestamps changed.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-007

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json

Change summary: New canonical JSON evidence artifact records BodyGraph-detail sufficiency as unsupported runtime nonclaim.

Risk assessment: High

Code review assessment: Artifact matches Approved Plan D2. It records no complete v2 ChartResult / ChartSimpleResult adapter sufficiency and references inspected internal loci.

Approved Plan linkage: Directly implements PR-01 BodyGraph-detail sufficiency or explicit nonclaim proof.

Repo proof: GitHub.fetch\_file → artifact contains `bodygraph_detail_sufficiency:"UNSUPPORTED_RUNTIME_NONCLAIM"`, `adapter_sufficiency:"NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI"`, and `pf09_subtask_id:"HDE-FERM008.6"`.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

CFR-008

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json.path\_proof.txt

Change summary: New path proof for BodyGraph-detail evidence.

Risk assessment: Medium

Code review assessment: Path proof includes concrete path, size, sha256, mtime, and produced timestamp.

Approved Plan linkage: Required path proof for PR-01 evidence output.

Repo proof: GitHub PR diff → path proof for `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json` with sha256 `61a23685a75c9b6d53ee3e73d73c466ddad8c8f5b3bd0040b12d350571748f83`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-009

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json

Change summary: New policy-binding snapshot records selected route-policy classification and follow-up boundaries.

Risk assessment: High

Code review assessment: Artifact correctly keeps PR-02 evidence-loop binding and any optional future adapter/live observation as follow-up; it does not overclaim parent completion.

Approved Plan linkage: Supports PR-01 route-policy proof while preserving PR-02 follow-up separation.

Repo proof: GitHub PR diff → `selected_classification:"unsupported_runtime_nonclaim"`, `ops_01_requirement:"OPS-01 not required by PR-01..."`, and follow-up entries include `PR-02 evidence-loop binding`.

PF reference, if relied on: PF06 — Epic Process Guide, §0.2 Policy and principles

CFR-010

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json.path\_proof.txt

Change summary: New path proof for policy-binding snapshot.

Risk assessment: Medium

Code review assessment: Expected path proof for governed evidence.

Approved Plan linkage: Supports path-proof discipline.

Repo proof: GitHub PR diff → path proof for `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json` with sha256 `3439dee7e7bc929e7d612929d3b594bd3f8564dff3e16541410cdd67f8d5bac4`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-011

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json

Change summary: New request-shape evidence records no configured-v2 `bodygraphs` request construction and explicit legacy fallback request shape.

Risk assessment: High

Code review assessment: Artifact matches Approved Plan D1/D3 and does not treat `charts/simple` as BodyGraph-detail proof.

Approved Plan linkage: Directly supports explicit route-policy classification and unsupported-runtime posture.

Repo proof: GitHub PR diff → `configured_v2_bg_resolve_request_shape:"NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM"` and `legacy_fallback_request_shape.resource_path:"bodygraphs"`.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

CFR-012

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json.path\_proof.txt

Change summary: New path proof for request-shape snapshot.

Risk assessment: Medium

Code review assessment: Expected path proof for governed evidence.

Approved Plan linkage: Supports path-proof discipline.

Repo proof: GitHub PR diff → path proof for `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json` with sha256 `8e27ac55371cb2b1ed1edbef5c0b0ff66e71ccd1c71e73ef2f9396fe98ae4e56`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-013

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json

Change summary: New canonical route-policy evidence records configured-v2 unsupported runtime nonclaim, explicit legacy fallback for v1, route-family identity, and no-claim boundaries.

Risk assessment: High

Code review assessment: Artifact is aligned with Approved Plan and PF09.5 HDE-FERM008.6. It preserves no-claim boundaries and avoids dual-route or v2 chart-backed claims.

Approved Plan linkage: Primary PR-01 D1 evidence.

Repo proof: GitHub.fetch\_file → `selected_posture:"unsupported_runtime_nonclaim"`, `configured_v2_policy.classification:"unsupported_runtime_nonclaim"`, `legacy_fallback_policy.classification:"explicit_legacy_fallback"`, and `supported_postures.dual_route_policy:"NOT_IMPLEMENTED_ADR_REQUIRED"`.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

CFR-014

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json.path\_proof.txt

Change summary: New path proof for route-policy snapshot.

Risk assessment: Medium

Code review assessment: Expected path proof for governed evidence.

Approved Plan linkage: Supports path-proof discipline.

Repo proof: GitHub PR diff → path proof for `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json` with sha256 `fee2f82ebf247a2a6e39e1211782d38085a7ac78796ff78bcc24d223680ec410`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-015

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json

Change summary: New runtime nonclaim artifact records public/API/AI/raw-payload/full-runtime-conformance nonclaims.

Risk assessment: High

Code review assessment: Artifact matches Approved Plan exclusions and no-claim boundaries.

Approved Plan linkage: Implements PR-01 nonclaim evidence for unsupported runtime posture.

Repo proof: GitHub PR diff → `unsupported_runtime_nonclaim:true`, `no_compatibility_by_inference:true`, `full_hdapi_v2_runtime_conformance:"NONE"`, `public_reader_change:"NONE"`, `ai_scope:"NONE"`.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

CFR-016

File: artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json.path\_proof.txt

Change summary: New path proof for runtime nonclaims artifact.

Risk assessment: Medium

Code review assessment: Expected path proof for governed evidence.

Approved Plan linkage: Supports path-proof discipline.

Repo proof: GitHub PR diff → path proof for `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json` with sha256 `7c85c96654dfd2c82d6d5f1cdcdde53d46264c6248fc5f91896af95e83c15752`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-017

File: artifacts/writer/conjunction\_write\_readback.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: No content hash drift observed; generated timestamp update only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-018

File: artifacts/writer/conjunction\_writer\_summary.json.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: No content hash drift observed; generated timestamp update only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-019

File: audit/docdeltas/hde-epic032\_doc\_deltas.md.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-020

File: audit/docdeltas/hde-epic034\_doc\_deltas.md.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-021

File: audit/docdeltas/hde-epic035\_doc\_deltas.md.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-022

File: audit/gates/narratives/keys\_10x4.table.json.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-023

File: audit/gates/narratives/pack\_identity.txt.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-024

File: audit/gates/narratives/registry.diff.json.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-025

File: audit/gates/topology/orientation\_demo.txt

Change summary: Orientation demo artifact updated from `total_artifacts: 413` to `total_artifacts: 419`.

Risk assessment: Medium

Code review assessment: Artifact count increase matches six new HDE-EPIC036 evidence entries. No concern remains.

Approved Plan linkage: Supports evidence orientation after PR-01 artifact registration.

Repo proof: GitHub PR diff → `total_artifacts: 419`, `status: ok`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-026

File: audit/gates/topology/orientation\_demo.txt.path\_proof.txt

Change summary: Path proof for orientation demo updated.

Risk assessment: Low

Code review assessment: Expected update after orientation demo content changed.

Approved Plan linkage: Supports evidence proof discipline.

Repo proof: GitHub PR diff → updated sha256 and produced timestamp for `audit/gates/topology/orientation_demo.txt`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-027

File: audit/qa/hde-epic030/pr-03/category\_order\_binding.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-028

File: audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-029

File: audit/qa/hde-epic030/pr-03/compat\_parity\_binding.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-030

File: audit/qa/hde-epic030/pr-04/band\_edges\_binding.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-031

File: audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-032

File: audit/qa/hde-epic030/pr-04/band\_thresholds\_identity\_hash.txt.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-033

File: audit/qa/hde-epic030/pr-05/category\_canonical\_compare.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-034

File: audit/qa/hde-epic030/pr-05/category\_framework\_binding.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-035

File: audit/qa/hde-epic030/pr-05/per\_channel\_mechanics.json.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-036

File: audit/qa/hde-epic034/00\_meta/doc\_deltas.md.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-037

File: audit/qa/hde-epic034/pr-03/response\_mapping\_check.log.path\_proof.txt

Change summary: Existing path proof mtime refreshed while produced timestamp remains earlier.

Risk assessment: Low

Code review assessment: The proof preserves original produced timestamp and same content hash, so no evidence payload drift was observed.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub PR diff → path proof same path, size, and sha256; only mtime changed to 2026-07-02 while produced timestamp stayed 2026-06-28.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-038

File: audit/qa/hde-epic035/00\_meta/doc\_deltas.md.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-039

File: audit/qa/hde-epic035/acceptance\_map\_viability.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-040

File: audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only; no OPS rerun is claimed.

Approved Plan linkage: Incidental evidence refresh; preserves OPS separation.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF06 — Epic Process Guide, §0.2 Policy and principles

CFR-041

File: audit/qa/hde-epic035/token\_evidence\_matrix.md.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-042

File: audit/qa/hde-epic036/route\_policy\_decision.log

Change summary: New human-readable route-policy decision log records unsupported-runtime nonclaim, no public/API/AI/full-conformance claims, and OPS-01 not required by PR-01.

Risk assessment: High

Code review assessment: Log aligns with Approved Plan and does not overclaim beyond PR-01.

Approved Plan linkage: Direct PR-01 evidence output.

Repo proof: GitHub PR diff → log contains `selected_route_policy_classification=unsupported_runtime_nonclaim`, `configured_v2_bg_resolve_request_shape=NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM`, `no_full_hdapi_v2_runtime_conformance=true`, and `OPS-01 not required by PR-01`.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

CFR-043

File: audit/qa/hde-epic036/route\_policy\_decision.log.path\_proof.txt

Change summary: New path proof for route-policy decision log.

Risk assessment: Medium

Code review assessment: Expected path proof for governed evidence.

Approved Plan linkage: Supports path-proof discipline.

Repo proof: GitHub PR diff → path proof for `audit/qa/hde-epic036/route_policy_decision.log` with sha256 `02ea41e97558edc9f0975b4a6261987ea1c31738286b59861837a3823b609409`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-044

File: docs/acceptance\_map\_epic035.json.path\_proof.txt

Change summary: Existing path proof timestamp refreshed.

Risk assessment: Low

Code review assessment: Generated path-proof refresh only; no HDE-EPIC035 acceptance-map payload change was reviewed as part of PR-01.

Approved Plan linkage: Incidental evidence refresh.

Repo proof: GitHub PR diff → same path, size, and sha256; updated mtime/produced timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-045

File: docs/evidence/INDEX.json

Change summary: Human Evidence Index regenerated with HDE-EPIC036 PR-01 entries.

Risk assessment: High

Code review assessment: Required by governed evidence posture after PR-01 artifacts were introduced. Final content includes new HDE-EPIC036 artifact keys through mirror/index generation.

Approved Plan linkage: Supports evidence indexing for PR-01 artifacts.

Repo proof: GitHub PR diff → Human Index includes new HDE-EPIC036 entries and hash changed to match updated evidence set.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-046

File: docs/evidence/INDEX.json.path\_proof.txt

Change summary: Path proof for Human Evidence Index regenerated.

Risk assessment: High

Code review assessment: Expected proof update after Human Evidence Index changed.

Approved Plan linkage: Supports governed evidence posture.

Repo proof: GitHub PR diff → path proof for `docs/evidence/INDEX.json` updated with changed size/hash/timestamp.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-047

File: docs/evidence/INDEX.sha256

Change summary: Human Evidence Index hash sentinel updated.

Risk assessment: High

Code review assessment: Expected hash sentinel update after `INDEX.json` changed.

Approved Plan linkage: Supports evidence hash posture.

Repo proof: GitHub PR diff → `docs/evidence/INDEX.sha256` changed to new hash for `docs/evidence/INDEX.json`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-048

File: docs/evidence/INDEX.sha256.path\_proof.txt

Change summary: Path proof for Human Evidence Index hash sentinel regenerated.

Risk assessment: Medium

Code review assessment: Expected proof update after sentinel changed.

Approved Plan linkage: Supports path-proof discipline.

Repo proof: GitHub PR diff → path proof for `docs/evidence/INDEX.sha256` updated.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-049

File: engine/bodygraph/ingest.py

Change summary: Added `_client_config_env` to merge partial ingest env overrides with process env credentials, then pass merged env into `HdApiClient.from_env`.

Risk assessment: High

Code review assessment: Fixes review-identified partial-env credential regression. Rails checks still occur before client construction. Process credentials are preserved while explicit base overrides replace both base aliases.

Approved Plan linkage: Supports PR-01 route-policy correctness without breaking existing vendor ingest callers.

Repo proof: GitHub.fetch\_file → `_client_config_env` merges `os.environ`, removes base aliases when either base key is supplied, and applies overrides; `ingest_vendor_bodygraph` calls `HdApiClient.from_env(log_path=retry_log, env=_client_config_env(env))`.

PF reference, if relied on: PF07 — Glow Infrastructure, §Intent & scope

CFR-050

File: engine/bodygraph/resolver.py

Change summary: Added route-policy classification after rails checks and before input normalization / ingest; added env merge helper and env-based classification.

Risk assessment: High

Code review assessment: Correctly preserves `SAFE_MODE` and `ALLOW_NETWORK` refusal before route policy, then blocks configured-v2 legacy BodyGraph route with `PROVIDER_ROUTE_UNSUPPORTED`. It passes the same merged env into ingest, resolving the earlier config-source divergence.

Approved Plan linkage: Direct implementation of PR-01 D1/D3.

Repo proof: GitHub.fetch\_file → closed rails return before line 130; lines 130-147 classify and reject unsupported v2; lines 188-201 merge env; lines 204-222 classify base; line 165 passes `vendor_env` to ingest.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

CFR-051

File: engine/bodygraph/vendor\_client.py

Change summary: Added route-policy utility functions, redacted auth posture helper, `env` parameter to `HdApiClient.from_env`, and pre-request policy enforcement in `build_request`.

Risk assessment: High

Code review assessment: Implements metadata-driven route-policy classification without raw secret output. Auth posture remains driven by `_ROUTE_CONTRACTS`. `build_request` blocks configured-v2 `bodygraphs` before constructing a request.

Approved Plan linkage: Direct implementation of PR-01 route-policy and auth posture requirements.

Repo proof: GitHub.fetch\_file → `classify_bg_resolve_route_policy` selects `unsupported_runtime_nonclaim` for v2 and `explicit_legacy_fallback` otherwise; `route_auth_posture` uses `_ROUTE_CONTRACTS`; `build_request` raises `PROVIDER_ROUTE_UNSUPPORTED` when policy unsupported.

PF reference, if relied on: PF05 — HDE-CLI-API-Vendor-Ref, §0.2 Scope \[Required-Now\]

CFR-052

File: engine/cli/main.py

Change summary: `_resolver_env` now passes `HD_API_BASE_URL` and `HDAPI_BASE_URL` to the resolver.

Risk assessment: Medium

Code review assessment: Minimal and necessary so CLI dry-run cannot bypass configured-v2 route policy. It passes non-secret base config only and does not pass credential values.

Approved Plan linkage: Supports PR-01 CLI route-policy enforcement.

Repo proof: GitHub.fetch\_file → `_resolver_env` returns `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `HD_API_BASE_URL`, and `HDAPI_BASE_URL`.

PF reference, if relied on: PF07 — Glow Infrastructure, §Intent & scope

CFR-053

File: tests/bodygraph/test\_bg\_resolve\_route\_policy.py

Change summary: New targeted tests cover configured-v2 unsupported posture, closed-rails precedence, explicit legacy fallback, no accidental v2 bodygraphs request, charts/simple non-inference, CLI dry-run, unified policy/ingest env, v2 override, and partial env credential preservation.

Risk assessment: High

Code review assessment: Test coverage directly matches PR-01 high-risk behavior and addresses review-discovered regressions.

Approved Plan linkage: Implements PR-01 targeted Basic QA check.

Repo proof: GitHub.fetch\_file → tests at lines 51-70, 73-87, 90-97, 100-129, 132-156, 159-218, and 221-262 cover route-policy and env merge behavior.

PF reference, if relied on: PF19 — Glow QA Guide, §0.2 Purpose & scope

CFR-054

File: tests/bodygraph/test\_resolver\_vendor.py

Change summary: Existing resolver vendor tests were adjusted to supply explicit non-v2 base policy context.

Risk assessment: Medium

Code review assessment: Adjustments preserve existing success/error behavior while making policy context explicit.

Approved Plan linkage: Keeps prior resolver coverage compatible with PR-01 route-policy enforcement.

Repo proof: GitHub.fetch\_pr\_file\_patch → two calls changed from `env={}` to `env={"HD_API_BASE_URL": "https://vendor.test/v1"}`.

PF reference, if relied on: None

CFR-055

File: tests/cli/test\_bg\_resolve.py

Change summary: Existing CLI open-rails vendor test was adjusted to set `HD_API_BASE_URL` to v1 and remove legacy alias.

Risk assessment: Medium

Code review assessment: Adjustment preserves existing open-rails success path under explicit legacy fallback policy.

Approved Plan linkage: Keeps existing CLI coverage consistent with PR-01 route-policy boundary.

Repo proof: GitHub.fetch\_pr\_file\_patch → `monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v1")` and `monkeypatch.delenv("HDAPI_BASE_URL", raising=False)` added.

PF reference, if relied on: None

CFR-056

File: tools/evidence/generate\_hde\_epic036\_bg\_resolve\_route\_policy.py

Change summary: New evidence generator creates PR-01 route-policy evidence, enforces closed rails, writes canonical JSON and decision log, writes path proofs, and supports `--check`.

Risk assessment: High

Code review assessment: Generator matches existing evidence generator patterns, uses closed-rails enforcement, avoids live vendor calls, and produces the expected PR-01 artifacts.

Approved Plan linkage: Implements planned PR-01 evidence generator and output artifacts.

Repo proof: GitHub.fetch\_file → outputs defined at lines 23-35; closed rails enforced at lines 81-86; canonical JSON bytes at lines 45-46; evidence bodies at lines 118-229; path-proof writer at lines 232-260; `--check` support at lines 265-278.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-057

File: tools/evidence/update\_evidence\_index.py

Change summary: Evidence index loader registers HDE-EPIC036 PR-01 artifacts, validates snapshot identity, adds them to the non-backdated proof set, and loads them into Human Index / Machine Mirror generation.

Risk assessment: High

Code review assessment: Correctly addresses review finding that new governed evidence must be indexed/mirrored. It validates `artifact_kind`, `epic_id`, PF09 task/subtask, and selected posture before loading entries.

Approved Plan linkage: Supports PR-01 governed evidence posture; PR-02 acceptance-map and token-matrix binding remain follow-up.

Repo proof: GitHub.fetch\_pr\_file\_patch → `EPIC036_PR01_PRIMARY_ARTIFACTS`, `_load_epic036_pr01_entries`, `EPIC036_PR01_ARTIFACT_RELS`, and `_load_human_index` insertion were added.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

Validation Results

VAL-001

Purpose: Identify exact merged change and current final branch state.

Command or method: GitHub.get\_pr\_info for PR \#335; GitHub.compare\_commits with base `bb419ce9264a5028ad819ebb147bf9b072dfef02` and head `main`.

Result: PASS

Key output or observation: PR \#335 is closed and merged; merge commit is `bb419ce9264a5028ad819ebb147bf9b072dfef02`; `main` is identical to that merge commit.

Why it matters: Establishes the exact merged change set and that final repo state equals reviewed merge commit.

VAL-002

Purpose: Verify targeted BodyGraph route-policy and vendor-client tests.

Command or method: Evaluated Optional PR Artifacts and final repo tests for `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python -m pytest tests/bodygraph/test_vendor_client.py tests/bodygraph/test_bg_resolve_route_policy.py tests/bodygraph/test_resolver_vendor.py tests/cli/test_bg_resolve.py`.

Result: PASS

Key output or observation: Optional PR Artifacts report this command passed after final review fixes. Final repo contains matching tests for configured-v2 unsupported posture, closed rails, legacy fallback, CLI dry-run, unified config source, and partial env credential preservation.

Why it matters: This is the primary targeted validation for changed runtime behavior.

VAL-003

Purpose: Verify PR-01 evidence generator check mode.

Command or method: Evaluated Optional PR Artifacts and final generator for `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py --check`.

Result: PASS

Key output or observation: Optional PR Artifacts report command passed; final generator supports `--check` and stale artifact detection.

Why it matters: Confirms evidence artifacts are reproducible from generator logic.

VAL-004

Purpose: Verify Human Evidence Index / Machine Mirror generation checks.

Command or method: Evaluated Optional PR Artifacts for `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/update_evidence_index.py --check`.

Result: PASS

Key output or observation: Optional PR Artifacts report command passed; final `update_evidence_index.py` includes HDE-EPIC036 PR-01 entries.

Why it matters: Confirms new governed evidence is registered.

VAL-005

Purpose: Verify orientation evidence coherence.

Command or method: Evaluated Optional PR Artifacts for `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/orientation_demo.py --check`.

Result: PASS

Key output or observation: Optional PR Artifacts report coherent orientation with 419 artifacts; final `audit/gates/topology/orientation_demo.txt` records `total_artifacts: 419` and `status: ok`.

Why it matters: Confirms evidence set count reflects HDE-EPIC036 PR-01 additions.

VAL-006

Purpose: Verify Machine Mirror schema and Evidence Index hash.

Command or method: Evaluated Optional PR Artifacts for `ci/checks/check_mirror_schema.sh` and `ci/checks/check_evidence_index_hash.sh`.

Result: PASS

Key output or observation: Optional PR Artifacts report both commands passed; final mirror and hash sentinel files were updated.

Why it matters: Confirms governed index/mirror/hash posture after evidence updates.

VAL-007

Purpose: Verify changed Python module syntax.

Command or method: Evaluated Optional PR Artifacts for `python -m py_compile engine/bodygraph/resolver.py engine/bodygraph/vendor_client.py engine/bodygraph/ingest.py engine/cli/main.py tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py tools/evidence/update_evidence_index.py`.

Result: PASS

Key output or observation: Optional PR Artifacts report py\_compile passed; final files are readable and structurally consistent.

Why it matters: Confirms no syntax-level defect in changed Python code.

VAL-008

Purpose: Check GitHub workflow context for the merge commit.

Command or method: GitHub.fetch\_commit\_workflow\_runs for `bb419ce9264a5028ad819ebb147bf9b072dfef02`.

Result: INCONCLUSIVE

Key output or observation: `workflow_runs: []`.

Why it matters: No workflow data was available for independent CI confirmation; this does not block because targeted validation was evaluated from Optional PR Artifacts and final repo state.

RCA

A) Bug/Failure statement

The Optional PR Artifacts show three review-discovered defects before merge: “Use the configured base when classifying resolver routes,” “Register EPIC036 evidence in the index,” and “Preserve credentials for partial ingest envs.” The final merged change includes subsequent fixes for those review findings before merge.

B) Root cause(s)

1. Initial resolver policy classification treated partial supplied env mappings as complete vendor config, causing base-url lookup divergence or missing config in open-rails and fake-ingest paths.  
   Evidence pointer(s): Optional PR Artifacts review finding; final `engine/bodygraph/resolver.py` adds `_vendor_config_env` and passes `vendor_env` to ingest.  
   PF references: PF07 — Glow Infrastructure, §Intent & scope.  
2. Initial PR-01 evidence artifacts existed with path proofs but were not registered into the Human Evidence Index / Machine Mirror.  
   Evidence pointer(s): Optional PR Artifacts review finding; final `tools/evidence/update_evidence_index.py` adds `EPIC036_PR01_PRIMARY_ARTIFACTS` and `_load_epic036_pr01_entries`.  
   PF references: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes.  
3. Initial ingest update passed partial env mappings directly to `HdApiClient.from_env`, dropping process-level credentials for callers that supplied only rails/base overrides.  
   Evidence pointer(s): Optional PR Artifacts review finding; final `engine/bodygraph/ingest.py` adds `_client_config_env`.  
   PF references: PF07 — Glow Infrastructure, §Intent & scope.

C) Fix in this merged change

* `engine/bodygraph/resolver.py` now merges process env and supplied env, lets explicit base overrides replace both aliases, classifies policy from that merged source, and passes the same merged env to ingest.  
  Repo evidence: `engine/bodygraph/resolver.py` lines 130-147 and 188-222.  
* `engine/bodygraph/ingest.py` now merges process env credentials with supplied env before constructing `HdApiClient`.  
  Repo evidence: `engine/bodygraph/ingest.py` lines 114-124 and 147\.  
* `tools/evidence/update_evidence_index.py` now registers and validates HDE-EPIC036 PR-01 evidence artifacts.  
  Repo evidence: PR file patch adds `EPIC036_PR01_PRIMARY_ARTIFACTS`, `_load_epic036_pr01_entries`, `EPIC036_PR01_ARTIFACT_RELS`, and loader insertion.  
* `tests/bodygraph/test_bg_resolve_route_policy.py` includes regression coverage for the fixed edge cases.  
  Repo evidence: tests cover unified config source, v2 override refusal, and direct ingest partial env credential preservation.

D) Fix verification

* Optional PR Artifacts report the expanded targeted pytest command passed under closed rails.  
* Optional PR Artifacts report evidence generator `--check`, evidence index `--check`, orientation check, mirror schema check, evidence hash check, py\_compile, and diff check all passed.  
* Current final repo state includes the exact tests and evidence-generator code needed to support the fixes.  
* Residual risk: local command execution was not re-run by this reviewer due remote GitHub connector review mode, but final repo state is identical to the merged commit and the validation roster is directly tied to the changed files.

Findings

Finding ID: F-001

Related review item: CFR-050 / CFR-051

Severity: Note

Observation: The merged code implements explicit configured-v2 route-policy rejection before BodyGraph request construction and preserves explicit legacy fallback for non-v2 bases.

Why it matters: This is the core approved PR-01 behavior.

Evidence: Repo proof: `engine/bodygraph/resolver.py` lines 130-147 classify and reject unsupported route policy; `engine/bodygraph/vendor_client.py` classifies v2 as `unsupported_runtime_nonclaim` and blocks `build_request`.

Required action: None.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

Finding ID: F-002

Related review item: CFR-049 / CFR-050 / CFR-053

Severity: Note

Observation: Review-discovered config-source and partial-env regressions are addressed in final code and tests.

Why it matters: Without these fixes, open-rails or fake-ingest callers could diverge between route-policy classification and actual client configuration.

Evidence: Repo proof: `engine/bodygraph/resolver.py` `_vendor_config_env`; `engine/bodygraph/ingest.py` `_client_config_env`; `tests/bodygraph/test_bg_resolve_route_policy.py` includes regression coverage.

Required action: None.

PF reference, if relied on: PF07 — Glow Infrastructure, §Intent & scope

Finding ID: F-003

Related review item: CFR-001 / CFR-045 / CFR-057

Severity: Note

Observation: HDE-EPIC036 PR-01 evidence artifacts are registered in Human Evidence Index / Machine Mirror generation.

Why it matters: The first PR review identified missing index registration; final merged change fixes that issue.

Evidence: Repo proof: `tools/evidence/update_evidence_index.py` PR patch adds `EPIC036_PR01_PRIMARY_ARTIFACTS`, `_load_epic036_pr01_entries`, and loader insertion; `artifacts/evidence_index.jsonl` includes HDE-EPIC036 evidence records.

Required action: None.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

Finding ID: F-004

Related review item: CFR-007 / CFR-009 / CFR-011 / CFR-013 / CFR-015 / CFR-042

Severity: Note

Observation: PR-01 evidence records unsupported-runtime nonclaim and no-claim boundaries without overclaiming v2 BodyGraph-detail sufficiency, full v2 runtime conformance, public Reader change, public route, app-side vendor ownership, raw payload persistence, or AI scope.

Why it matters: This preserves the Approved Plan’s no-claim posture.

Evidence: Repo proof: HDE-EPIC036 evidence files under `artifacts/vendor/hdapi_v2/` and `audit/qa/hde-epic036/route_policy_decision.log` contain the selected unsupported-runtime nonclaim and no-claim boundaries.

Required action: None.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

Finding ID: F-005

Related review item: CFR-005 / CFR-006 / CFR-017 through CFR-041 / CFR-044

Severity: Concern

Observation: Evidence refresh regenerated many pre-existing path-proof timestamps outside HDE-EPIC036.

Why it matters: Broad generated proof churn increases review noise and should remain controlled, even when the underlying content hashes are unchanged.

Evidence: Repo proof: changed path-proof files for HDE-EPIC030, HDE-EPIC032, HDE-EPIC034, HDE-EPIC035, narratives, and writer artifacts mostly retain the same path/size/sha256 and update timestamps only.

Required action: None for this merged change; keep future evidence refreshes scoped where tooling allows, but do not treat this generated refresh as post-merge remediation because index/mirror/hash checks passed.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

Finding ID: F-006

Related review item: CFR-053 / VAL-002

Severity: Note

Observation: Targeted tests cover the route-policy behavior and the review-discovered env-merging regressions.

Why it matters: The tests directly exercise the high-risk route policy and credential/config-source paths.

Evidence: Repo proof: `tests/bodygraph/test_bg_resolve_route_policy.py` includes configured-v2, closed rails, legacy fallback, CLI dry-run, unified config source, v2 override, and direct ingest partial env credential tests.

Required action: None.

PF reference, if relied on: PF19 — Glow QA Guide, §0.2 Purpose & scope

Finding ID: F-007

Related review item: CFR-056 / VAL-003

Severity: Note

Observation: The new evidence generator uses closed-rails enforcement, canonical JSON, path-proof writing, and `--check`.

Why it matters: This supports deterministic PR-01 evidence regeneration without live vendor calls.

Evidence: Repo proof: `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py` defines closed rails, canonical JSON bytes, path-proof writing, and check mode.

Required action: None.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

Finding ID: F-008

Related review item: VAL-008

Severity: Note

Observation: No GitHub workflow runs were returned for the merge commit.

Why it matters: There is no independent CI result from GitHub workflow metadata to add to the review record.

Evidence: Repo proof: GitHub.fetch\_commit\_workflow\_runs for `bb419ce9264a5028ad819ebb147bf9b072dfef02` returned `workflow_runs: []`.

Required action: None; targeted validation is still sufficient from Optional PR Artifacts plus final repo inspection.

PF reference, if relied on: None.

Finding ID: F-009

Related review item: PF09

Severity: Note

Observation: HDE-FERM008.6 remains `Not done` in PF09.5, but PR-01 provides route-policy proof evidence supporting the first implementation slice.

Why it matters: PF09 status should not be changed from PR-01 alone because PR-02 evidence-loop binding remains follow-up in the Approved Plan and merged evidence.

Evidence: Repo proof: `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json` records follow-up `PR-02 evidence-loop binding`; PF09.5 current subtask status is `Not done`.

Required action: No post-merge remediation. Record as Doc Delta Candidate for later PF09 status-support drainage.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

PF09 Impact & Status Posture

PF09 document: PF09.5-Canon-HDE-Build-Checklist-Fermentation

PF09 task ID: HDE-FERM008

PF09 subtask ID(s): HDE-FERM008.6

Current PF09 status: Not done

Status recommendation: No status change recommended

Why this status posture is supported: PR-01 completed and evidenced the route-policy classification slice, but the Approved Plan still has PR-02 for governed evidence-loop closure. The merged policy-binding artifact also records `PR-02 evidence-loop binding` as follow-up. Therefore PR-01 makes HDE-FERM008.6 supportable in part from repo evidence, but not ready for PF09 status change from this post-merge review alone.

Evidence pointer(s):  
Repo proof: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json` → `pf09_task_id:"HDE-FERM008"`, `pf09_subtask_id:"HDE-FERM008.6"`, `selected_posture:"unsupported_runtime_nonclaim"`.  
Repo proof: `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json` → follow-up includes `PR-02 evidence-loop binding`.

PF proof excerpt(s), when PF09 is relied on:  
PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

"Define and prove the runtime vendor-route policy for `bg:resolve --source vendor` so BodyGraph detail resolution is no longer an accidental legacy BodyGraph route composed against a configured v2 base."

"The policy must explicitly classify the selected route family as v2 chart-backed BodyGraph resolution, explicit legacy fallback, dual-route policy, or unsupported-runtime nonclaim."

"Subtask status: Not done"

Evidence Print

A) Tokens satisfied

TESTS\_PASS\_OK

Evidence pointer(s): Optional PR Artifacts report closed-rails targeted pytest passed for `tests/bodygraph/test_vendor_client.py`, `tests/bodygraph/test_bg_resolve_route_policy.py`, `tests/bodygraph/test_resolver_vendor.py`, and `tests/cli/test_bg_resolve.py`. Final repo includes those tests and associated changed files.

JSON\_CANONICAL\_CHECK\_OK

Evidence pointer(s): `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`, `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`, `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`, `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`, and `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json` are generated by canonical JSON function in `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`; `artifacts/evidence_index.jsonl` records these JSON artifacts with token `JSON_CANONICAL_CHECK_OK`.

NO\_EXTERNAL\_IO\_ON\_REFUSAL\_OK

Evidence pointer(s): `tests/bodygraph/test_bg_resolve_route_policy.py` verifies closed rails refuse before route policy and external I/O; `engine/bodygraph/resolver.py` returns `PROVIDER_REFUSED` before route-policy or ingest work when `SAFE_MODE` is truthy.

ENV\_RAILS\_POLICY\_OK

Evidence pointer(s): `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py` enforces closed rails `ALLOW_NETWORK=0`, `LANG=C`, `LC_ALL=C`, `SAFE_MODE=1`, and `TZ=UTC`; Optional PR Artifacts report evidence generator and validation commands ran under those pins.

EVIDENCE\_PATH\_PROOFS\_OK

Evidence pointer(s): all HDE-EPIC036 PR-01 evidence artifacts have sibling `.path_proof.txt` files, and `tools/evidence/update_evidence_index.py` registers HDE-EPIC036 entries with token `EVIDENCE_PATH_PROOFS_OK`.

B) Evidence artifacts produced or updated

Path: artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json

Type: governed JSON snapshot

Key proof facts observed: selected posture `unsupported_runtime_nonclaim`; configured-v2 policy unsupported; explicit legacy fallback preserved for v1; dual-route not implemented and ADR required.

sha256, if observed: fee2f82ebf247a2a6e39e1211782d38085a7ac78796ff78bcc24d223680ec410

Index/Mirror/path-proof posture, if relevant: Path proof exists; Machine Mirror entry exists; Human Index updated.

Path: artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json

Type: governed JSON snapshot

Key proof facts observed: BodyGraph-detail sufficiency is `UNSUPPORTED_RUNTIME_NONCLAIM`; no complete v2 ChartResult / ChartSimpleResult adapter found in inspected loci; v2 chart data does not feed existing BodyGraph/cache/person/compat flows.

sha256, if observed: 61a23685a75c9b6d53ee3e73d73c466ddad8c8f5b3bd0040b12d350571748f83

Index/Mirror/path-proof posture, if relevant: Path proof exists; Machine Mirror entry exists; Human Index updated.

Path: artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json

Type: governed JSON snapshot

Key proof facts observed: no public route, public flag, public payload change, public Reader change, new HTTP home, app-side vendor credential ownership, raw payload persistence, AI scope, or full v2 runtime conformance claim.

sha256, if observed: 7c85c96654dfd2c82d6d5f1cdcdde53d46264c6248fc5f91896af95e83c15752

Index/Mirror/path-proof posture, if relevant: Path proof exists; Machine Mirror entry exists; Human Index updated.

Path: artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json

Type: governed JSON snapshot

Key proof facts observed: configured-v2 `bg:resolve` builds no `bodygraphs` request; non-v2 legacy fallback request shape is explicit; v2 `charts/simple` is not used for BodyGraph-detail proof.

sha256, if observed: 8e27ac55371cb2b1ed1edbef5c0b0ff66e71ccd1c71e73ef2f9396fe98ae4e56

Index/Mirror/path-proof posture, if relevant: Path proof exists; Machine Mirror entry exists; Human Index updated.

Path: artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json

Type: governed JSON snapshot

Key proof facts observed: selected classification is unsupported runtime nonclaim; OPS-01 not required by PR-01; PR-02 evidence-loop binding remains follow-up.

sha256, if observed: 3439dee7e7bc929e7d612929d3b594bd3f8564dff3e16541410cdd67f8d5bac4

Index/Mirror/path-proof posture, if relevant: Path proof exists; Machine Mirror entry exists; Human Index updated.

Path: audit/qa/hde-epic036/route\_policy\_decision.log

Type: governed log

Key proof facts observed: route-policy decision records `unsupported_runtime_nonclaim`, no `bodygraphs` request for configured v2, explicit legacy fallback boundary, no public/API/AI/full-conformance claims, and OPS-01 not required by PR-01.

sha256, if observed: 02ea41e97558edc9f0975b4a6261987ea1c31738286b59861837a3823b609409

Index/Mirror/path-proof posture, if relevant: Path proof exists; Machine Mirror entry exists; Human Index updated.

Path: docs/evidence/INDEX.json

Type: Human Evidence Index

Key proof facts observed: updated to include HDE-EPIC036 PR-01 evidence entries.

sha256, if observed: 3825d89cf2e0b379eaf059069a8f17c1ab67a3e5c2d279c425f39254c4a970fc

Index/Mirror/path-proof posture, if relevant: Path proof and hash sentinel updated.

Path: artifacts/evidence\_index.jsonl

Type: Machine Evidence Mirror

Key proof facts observed: updated with HDE-EPIC036 PR-01 evidence entries and self-record.

sha256, if observed: 7656afb91c3a7e9ea0f0e010377831e0bfacb0635ff33b51b70eb1bf25747b29 as file sidecar; self-record mirror body sha `d351a8eb68acbabdacde0eedef0399a56c40840d82ae9b3e34c7fd8b947ed4de`.

Index/Mirror/path-proof posture, if relevant: Path proof and sidecar updated.

C) Validation proof

Command or method: GitHub.compare\_commits `bb419ce9264a5028ad819ebb147bf9b072dfef02...main`

Result: PASS

Where the result appears: Repo Inspection / VAL-001

Why it is sufficient: Confirms current reviewed repo state equals merged PR \#335 change set.

Command or method: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python -m pytest tests/bodygraph/test_vendor_client.py tests/bodygraph/test_bg_resolve_route_policy.py tests/bodygraph/test_resolver_vendor.py tests/cli/test_bg_resolve.py`

Result: PASS

Where the result appears: Optional PR Artifacts; final test files verified in repo.

Why it is sufficient: Targets all changed runtime route-policy behavior and review-regression coverage.

Command or method: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py --check`

Result: PASS

Where the result appears: Optional PR Artifacts; final generator check-mode implementation verified in repo.

Why it is sufficient: Confirms generated PR-01 evidence is current and reproducible.

Command or method: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/update_evidence_index.py --check`

Result: PASS

Where the result appears: Optional PR Artifacts; final evidence-index registration verified in repo.

Why it is sufficient: Confirms Human Index / Machine Mirror entries are generated and checked.

Command or method: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/orientation_demo.py --check`

Result: PASS

Where the result appears: Optional PR Artifacts; final `audit/gates/topology/orientation_demo.txt` records `total_artifacts: 419` and `status: ok`.

Why it is sufficient: Confirms orientation artifact reflects updated evidence count.

Command or method: `ci/checks/check_mirror_schema.sh` and `ci/checks/check_evidence_index_hash.sh`

Result: PASS

Where the result appears: Optional PR Artifacts; final mirror/hash files verified in repo.

Why it is sufficient: Confirms machine mirror schema posture and index hash sentinel.

Command or method: `python -m py_compile engine/bodygraph/resolver.py engine/bodygraph/vendor_client.py engine/bodygraph/ingest.py engine/cli/main.py tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py tools/evidence/update_evidence_index.py`

Result: PASS

Where the result appears: Optional PR Artifacts; final files inspected in repo.

Why it is sufficient: Confirms changed Python files compile.

Doc Delta Candidates

DDC-001

Doc: PF09.5 — HDE Build Checklist Fermentation

Section: §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.6

PF09 status action: No status change recommended

Delta: Add a supportable-from-repo-evidence note that HDE-EPIC036 PR-01 implemented and governed the explicit `bg:resolve --source vendor` route-policy classification, selecting unsupported-runtime nonclaim for configured v2 bases and preserving explicit legacy fallback for non-v2 bases, while PR-02 evidence-loop binding remains follow-up.

Why: Current PF09.5 still records HDE-FERM008.6 as Not done. PR-01 supplies route-policy evidence, but the Approved Plan and merged policy-binding artifact keep PR-02 as follow-up, so the current recommendation is no status change yet.

Repo evidence: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`; `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`; `audit/qa/hde-epic036/route_policy_decision.log`.

Canon proof excerpt:

"Subtask status: Not done"

"The future proof must show whether `bg:resolve --source vendor` is v2 chart-backed, explicit legacy fallback, dual-route, or unsupported."

"It must not treat `charts/simple` success as proof of full BodyGraph detail."

DDC-002

Doc: PF05 — HDE-CLI-API-Vendor-Ref

Section: §0.2 Scope \[Required-Now\]

Canon basis: CANON SILENCE

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.6

PF09 status action: No status change recommended

Delta: Record the implemented CLI/vendor runtime posture for `bg:resolve --source vendor`: configured v2 bases return explicit unsupported-runtime nonclaim / `PROVIDER_ROUTE_UNSUPPORTED` before legacy `bodygraphs` request construction; non-v2 bases preserve explicit legacy fallback.

Why: The merged change affects CLI/vendor route-policy behavior and a provider error posture that PF05 owns as the CLI/API/vendor byte and behavior home.

Repo evidence: `engine/bodygraph/vendor_client.py`; `engine/bodygraph/resolver.py`; `engine/cli/main.py`; `tests/bodygraph/test_bg_resolve_route_policy.py`.

Canon proof excerpt: N/A (CANON SILENCE)

DDC-003

Doc: PF12 — HDE-Schemas and Artifacts

Section: §0.2 Scope & single homes \[Required-Now\]

Canon basis: CANON SILENCE

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.6

PF09 status action: No status change recommended

Delta: Consider whether HDE-EPIC036 PR-01’s `bg_resolve_*` evidence family should be added to a permanent Evidence Catalog description after PR-02 completes binding.

Why: The merged change introduced a new governed HDAPI v2 BodyGraph route-policy evidence family under `artifacts/vendor/hdapi_v2/` and `audit/qa/hde-epic036/`; it is indexed and mirrored, but a later catalog note may reduce future ambiguity.

Repo evidence: `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`; `tools/evidence/update_evidence_index.py`; HDE-EPIC036 PR-01 evidence artifacts.

Canon proof excerpt: N/A (CANON SILENCE)

DECISION: MERGED CHANGE ACCEPTABLE

## 2.3) Production/User-Surface Epics Must Include At Least One Open-Rails QA Step

Timestamp: 063026

Status: Live PF10 staging decision pending permanent PF-Canon drain

Decision owner: Lead Dev / PO directive

### **Details**

Repeated planning and QA-review drift has treated open-rails QA as optional, deferrable, or dependent on reviewer interpretation even when an epic affects user-facing behavior, production-facing behavior, CLI behavior, vendor ingestion, vendor transport, persistence, runtime routes, environment binding, or operational surfaces.

That is no longer allowed.

Any epic that affects user or production surfaces must include at least one bounded open-rails QA step.

This explicitly includes epics that affect:

* public app behavior;  
* user-facing behavior;  
* production runtime behavior;  
* CLI behavior;  
* operator-facing CLI surfaces;  
* vendor ingestion;  
* vendor request shaping;  
* vendor response handling;  
* vendor route policy;  
* external API transport;  
* environment or secret binding behavior;  
* database persistence or retrieval behavior;  
* runtime compute behavior;  
* deployed service behavior;  
* admin or ops-facing behavior that can affect production truth.

### **Lead decision**

A closed-rails-only QA plan is not sufficient for any epic that affects user or production surfaces.

At least one open-rails QA step is mandatory when the epic affects CLI, vendor ingestion, vendor transport, production behavior, user behavior, or any runtime surface that can differ between closed rails and open rails.

This is a QA planning requirement and a QA readiness requirement.

### **Required rule**

For any affected epic:

* the Epic Plan must declare the open-rails QA requirement;  
* the Implementation Plan must preserve it;  
* the Live QA Guide must include it as a proof obligation;  
* the Live QA Plan must include at least one bounded open-rails QA step;  
* the QA review must block if the Live QA Plan omits that step;  
* QA readiness must not be marked ready unless the open-rails requirement is accounted for;  
* closeout review must distinguish the open-rails evidence from closed-rails evidence.

### **Scope of the required open-rails step**

The open-rails QA step must be:

* bounded;  
* intentional;  
* secret-safe;  
* evidence-recorded;  
* scoped to the production/user/runtime surface affected by the epic;  
* clear about what it proves;  
* clear about what it does not prove;  
* separated from OPS work unless the action is explicitly PO-only OPS;  
* free of raw secret persistence;  
* free of uncontrolled raw vendor payload persistence;  
* free of full-runtime-conformance overclaim unless the proof actually covers that full scope.

### **What does not satisfy this rule**

The following do not satisfy the open-rails QA requirement by themselves:

* closed-rails tests;  
* unit tests;  
* static validation;  
* schema validation;  
* evidence-index validation;  
* Machine Mirror validation;  
* path-proof validation;  
* command syntax validation;  
* dry-run-only closed-rails proof;  
* fixture-only proof;  
* mock-only proof;  
* repo inspection;  
* prior epic evidence unless PF10 and the current QA plan explicitly bind it to the current epic’s open-rails proof need;  
* an OPS observation that is not bound into QA evidence;  
* a statement that open-rails QA is unnecessary without a recorded controlling exemption.

### **CLI and vendor ingestion rule**

CLI and vendor ingestion are production-relevant surfaces.

An epic that changes, proves, routes, classifies, or constrains CLI behavior or vendor ingestion behavior must include at least one open-rails QA step.

This includes:

* `bg:resolve --source vendor`;  
* vendor route-policy work;  
* HumanDesignAPI request shaping;  
* HumanDesignAPI auth/header behavior;  
* BodyGraph vendor ingest;  
* vendor response normalization;  
* vendor error/retry/rate-limit behavior;  
* vendor availability proof;  
* configured base URL behavior;  
* environment-key binding behavior;  
* provider transport behavior.

Closed-rails refusal proof is still valuable, but it is not enough by itself when the epic affects open-rails runtime behavior.

### **HDE-EPIC036 application**

HDE-EPIC036 affects CLI behavior and vendor ingestion / vendor route-policy behavior.

Therefore HDE-EPIC036 must include at least one bounded open-rails QA step.

The Live QA Plan for HDE-EPIC036 must not be approved unless it includes an open-rails QA step that directly exercises or proves the relevant route-policy / vendor-ingestion behavior, or records a controlling PO-authorized exemption with explicit rationale.

Because the epic centers on `bg:resolve --source vendor`, vendor route policy, and BodyGraph-detail resolution posture, closed-rails-only QA is not sufficient.

### **Review rule**

Reviewers must block a QA Plan, Live QA Plan, QA-readiness review, or closeout-review posture when all are true:

* the epic affects user or production surfaces;  
* the epic affects CLI, vendor ingestion, transport, runtime, persistence, or deployed behavior;  
* no bounded open-rails QA step is included;  
* no controlling PO-authorized exemption is recorded.

This is a substantive QA coverage blocker, not a documentation preference.

### **Required reviewer language**

When this blocker applies, reviewers must say:

“Open-rails QA is required because this epic affects user or production surfaces. Closed-rails-only QA is insufficient.”

The reviewer must identify the affected surface, such as CLI, vendor ingestion, vendor transport, runtime persistence, public app behavior, or deployed service behavior.

### **Valid exemption boundary**

An exemption is allowed only when explicitly recorded by the PO or controlling PF-Canon before QA approval.

The exemption must state:

* why no open-rails behavior can be safely or meaningfully exercised;  
* what risk is accepted;  
* what proof substitutes for open-rails QA;  
* why the substitute is sufficient for this epic;  
* what future work, if any, must still perform open-rails proof.

An implied exemption is invalid.

Silence is not an exemption.

Reviewer preference is not an exemption.

“Not convenient” is not an exemption.

“Closed rails passed” is not an exemption.

### **Evidence separation**

Open-rails QA evidence must remain distinct from:

* OPS evidence;  
* closed-rails evidence;  
* implementation evidence;  
* repo inspection;  
* static validation;  
* path-proof validation;  
* Evidence Index / Machine Mirror validation;  
* documentation drainage.

OPS may produce PO-only live observations, but QA must still bind or evaluate the relevant open-rails proof under QA posture when the epic requires open-rails QA.

### **Nonclaim rule**

An open-rails QA step must not overclaim.

The evidence must state the bounded behavior proven and preserve nonclaims for anything not exercised.

For vendor epics, this means a successful open-rails step must not automatically claim:

* full vendor runtime conformance;  
* complete BodyGraph-detail compatibility;  
* production deployment success;  
* public Reader success;  
* app-side vendor ownership;  
* raw payload persistence approval;  
* PF09 Done;  
* QA PASS beyond the actual QA result;  
* OPS completion unless OPS separately records it.

### **Permanent PF-Canon drain targets**

#### **PF19 — Glow QA Guide**

Drain priority: highest.

Required permanent-canon update:

* State that any epic affecting user or production surfaces must include at least one bounded open-rails QA step.  
* Explicitly include CLI and vendor ingestion as production-relevant surfaces.  
* State that closed-rails-only QA is insufficient for these epics.  
* Require Live QA Plans to include the open-rails step or an explicit PO-authorized exemption.  
* Require QA closeout to distinguish closed-rails proof, open-rails QA proof, and OPS evidence.

#### **PF27 — Canon Plan Templates**

Drain priority: highest.

Required permanent-canon update:

* Add an Epic Plan requirement to declare whether open-rails QA is mandatory.  
* Add an Implementation Plan requirement to preserve open-rails QA requirements from the Epic Plan.  
* Add a Live QA Plan requirement to include at least one bounded open-rails QA step for user/production-surface epics.  
* Add review language requiring blockers when the open-rails step is missing.  
* Explicitly list CLI and vendor ingestion as open-rails-triggering surfaces.

#### **PF06 — Epic Process Guide**

Drain priority: highest.

Required permanent-canon update:

* Add open-rails QA as mandatory for epics affecting user or production surfaces.  
* State that QA readiness is not achieved for such epics until the open-rails requirement is accounted for.  
* Preserve PR / OPS / QA separation while requiring QA binding of open-rails proof.  
* Clarify that OPS observations do not automatically replace QA open-rails steps unless explicitly bound and accepted under QA posture.

#### **PF04 — HDE Governance**

Drain priority: high.

Required permanent-canon update:

* Record open-rails QA as a governance requirement for production/user-surface epics.  
* Clarify that omission of required open-rails QA is a QA coverage blocker.  
* Clarify that tokens and closed-rails evidence cannot substitute for the required open-rails QA step unless an explicit exemption is recorded.  
* Preserve secret-safety and no-overclaim rules for open-rails evidence.

#### **PF05 — HDE CLI/API Vendor Ref**

Drain priority: high.

Required permanent-canon update:

* State that CLI, vendor ingestion, vendor transport, vendor route policy, and vendor auth/header behavior are production-relevant surfaces.  
* Require at least one bounded open-rails QA step for epics that alter or prove those surfaces.  
* For HumanDesignAPI work, require the open-rails step to distinguish actual exercised route behavior from inferred route behavior.

#### **PF07 — Glow Infrastructure**

Drain priority: high.

Required permanent-canon update:

* State that environment binding, base URL behavior, provider secrets, deployed service binding, and open-rails runtime behavior require open-rails QA when affected by an epic.  
* Clarify secret-safe evidence handling for open-rails validation.  
* Require explicit exemption when open-rails validation is not possible.

#### **PF12 — HDE Schemas and Artifacts**

Drain priority: high.

Required permanent-canon update:

* Add artifact/evidence requirements for recording open-rails QA proof separately from closed-rails proof and OPS evidence.  
* Require evidence families to preserve bounded proof and nonclaims.  
* Require Evidence Index / Machine Mirror posture to distinguish open-rails QA evidence from other evidence families.

#### **PF14 — HDE Mechanics Guide**

Drain priority: high.

Required permanent-canon update:

* State that mechanics affecting runtime compute, BodyGraph resolution, vendor ingest, or route-policy behavior require open-rails QA when they affect production/user surfaces.  
* Require mechanics proofs to distinguish closed-rails control-flow proof from open-rails runtime behavior proof.  
* For BodyGraph/vendor mechanics, require proof of the actual selected runtime route behavior.

#### **PF09 phased checklist documents**

Drain priority: medium.

Required permanent-canon update:

* Add or strengthen PF09 task/subtask language where phase rows involve user/production surfaces, CLI, vendor ingestion, runtime behavior, or deployed behavior.  
* Make open-rails QA expectation visible in relevant phase rows without turning PF09 into a QA runbook.  
* Ensure future PF09 tasks that affect production/user surfaces are visibly open-rails-accounted.

#### **PF03 — Technical Writing Best Practices**

Drain priority: medium.

Required permanent-canon update:

* Require plans and reviews to use plain, direct language distinguishing closed-rails proof from open-rails proof.  
* Ensure documentation does not bury open-rails QA requirements as optional notes.

#### **PF23 — Reality Audits**

Drain priority: medium.

Required permanent-canon update:

* Require reality audits to flag when repo-reality work affects user/production surfaces and therefore likely triggers open-rails QA.  
* Clarify that PF23 may surface the trigger but does not itself execute or satisfy open-rails QA.

### **Immediate operating rule**

Until drained, PF10 carries the live rule:

Any epic that affects user or production surfaces must include at least one bounded open-rails QA step.

CLI counts.

Vendor ingestion counts.

Vendor route policy counts.

Production runtime behavior counts.

Closed-rails-only QA is insufficient.

No exemption exists unless explicitly recorded by the PO or controlling PF-Canon.

### **Final authority**

This addendum is live immediately.

Do not approve a Live QA Plan for a user/production-surface epic without at least one open-rails QA step or an explicit PO-authorized exemption.

Do not mark QA-ready for a user/production-surface epic unless open-rails QA is accounted for.

Do not close the QA evidence loop for a user/production-surface epic using closed-rails-only proof.

## 2.4) PR-02 HDE-EPIC036

Review Summary

* The merged change binds already-landed PR-01 `bg:resolve --source vendor` route-policy evidence into HDE-EPIC036 PR-02 evidence-loop surfaces.  
* The merged change aligns with the Approved Plan’s PR-02 scope: acceptance map, token/evidence matrix, viability log, doc-delta candidate surfaces, Human Evidence Index, Machine Mirror, hash sentinels, and path proofs.  
* Expected PR-02 artifacts were found in final repo state: `docs/acceptance_map_epic036.json`, `audit/qa/hde-epic036/token_evidence_matrix.md`, `audit/qa/hde-epic036/acceptance_map_viability.log`, `audit/docdeltas/hde-epic036_doc_deltas.md`, and `audit/qa/hde-epic036/00_meta/doc_deltas.md`.  
* The merged change preserves the PR-01 classification: `unsupported_runtime_nonclaim`, with no OPS-01 execution, no QA PASS claim, no PF09 status movement claim, no epic closeout claim, no public surface expansion, no raw payload persistence, no AI scope, and no full HumanDesignAPI v2 runtime-conformance claim.  
* One pre-merge review finding was raised against `tools/evidence/update_evidence_index.py`; the final merged file fixes it by requiring the PR-02 token roster to equal the complete approved set, not merely be a subset.  
* Validation was evaluated from the Merged Change body, Optional PR Artifacts, final repo files, and final merged state. The reported validation suite is targeted and sufficient for this post-merge scope.  
* PF09 impact is PF09.5 / HDE-FERM008 / HDE-FERM008.6. HDE-FERM008.6 is supportable for status change to Done from repo evidence; HDE-FERM008 parent Done remains out of scope.  
* No post-merge remediation issue remains.

Repo Inspection

Observed repo root:  
Repo proof: GitHub.get\_repo → repository `amthorn78/glow-hdengine-v2`, default branch `main`.

Observed HEAD:  
Repo proof: GitHub.compare\_commits → base `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74` vs head `main` returned `status: identical`, `ahead_by: 0`, `behind_by: 0`, `total_commits: 0`.

Branch or detached state:  
Repo proof: GitHub.get\_pr\_info → PR \#336 base branch `main`; GitHub.compare\_commits confirms `main` currently equals merge commit `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74`.

Working tree status before review:  
Repo proof: remote GitHub connector review only; no local mutable working tree was available. This does not block review because the exact merged PR and final branch state were resolved through GitHub.

How MERGED\_PR\_REF was resolved:  
Repo proof: GitHub.get\_pr\_info → PR \#336 is `closed`, `merged: true`, `merge_commit_sha: 5e159a9f338cf160b202b6c9c64b3d9ff4dcee74`, base `main`, head SHA `2045a9cc1c28e86b33000d99b1cd208730c44272`.

Changed files reviewed:  
Repo proof: GitHub.list\_pr\_changed\_filenames → 47 changed files:  
`artifacts/evidence_index.jsonl`; `artifacts/evidence_index.jsonl.path_proof.txt`; `artifacts/evidence_index.jsonl.sha256`; `artifacts/evidence_index.jsonl.sha256.path_proof.txt`; `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; `artifacts/narratives/router/parity_abba.log.path_proof.txt`; `artifacts/writer/conjunction_write_readback.log.path_proof.txt`; `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`; `audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; `audit/docdeltas/hde-epic035_doc_deltas.md.path_proof.txt`; `audit/docdeltas/hde-epic036_doc_deltas.md`; `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`; `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`; `audit/gates/narratives/pack_identity.txt.path_proof.txt`; `audit/gates/narratives/registry.diff.json.path_proof.txt`; `audit/gates/topology/orientation_demo.txt`; `audit/gates/topology/orientation_demo.txt.path_proof.txt`; `audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`; `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`; `audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`; `audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`; `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`; `audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; `audit/qa/hde-epic035/00_meta/doc_deltas.md.path_proof.txt`; `audit/qa/hde-epic035/acceptance_map_viability.log.path_proof.txt`; `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log.path_proof.txt`; `audit/qa/hde-epic035/token_evidence_matrix.md.path_proof.txt`; `audit/qa/hde-epic036/00_meta/doc_deltas.md`; `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`; `audit/qa/hde-epic036/acceptance_map_viability.log`; `audit/qa/hde-epic036/acceptance_map_viability.log.path_proof.txt`; `audit/qa/hde-epic036/token_evidence_matrix.md`; `audit/qa/hde-epic036/token_evidence_matrix.md.path_proof.txt`; `docs/acceptance_map_epic035.json.path_proof.txt`; `docs/acceptance_map_epic036.json`; `docs/acceptance_map_epic036.json.path_proof.txt`; `docs/evidence/INDEX.json`; `docs/evidence/INDEX.json.path_proof.txt`; `docs/evidence/INDEX.sha256`; `docs/evidence/INDEX.sha256.path_proof.txt`; `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`; `tools/evidence/update_evidence_index.py`.

Working tree status after validation:  
Repo proof: no local commands were run in a mutable checkout. GitHub.compare\_commits after review still showed `main` identical to merge commit `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74`.

Changed File Review

CFR-001

File: artifacts/evidence\_index.jsonl

Change summary: Machine Evidence Mirror regenerated with PR-02 HDE-EPIC036 entries for acceptance map, token matrix, viability log, and doc-delta candidate surfaces.

Risk assessment: High

Code review assessment: Governed evidence mirror changed as expected. PR-02 entries are also validated by `tools/evidence/update_evidence_index.py` and targeted evidence-loop tests.

Approved Plan linkage: Direct PR-02 evidence-loop binding output.

Repo proof: GitHub.search for `docs/acceptance_map_epic036.json` → `artifacts/evidence_index.jsonl` contains PR-02 indexed evidence; GitHub.fetch\_file `tools/evidence/update_evidence_index.py` shows PR-02 artifact entries and loader validation.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-002

File: artifacts/evidence\_index.jsonl.path\_proof.txt

Change summary: Machine Mirror path proof regenerated.

Risk assessment: High

Code review assessment: Expected same-PR proof update after mirror bytes changed.

Approved Plan linkage: Required governed proof surface for Machine Mirror.

Repo proof: GitHub.list\_pr\_changed\_filenames → file changed; `artifacts/evidence_index.jsonl.sha256` updated in the same change set.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-003

File: artifacts/evidence\_index.jsonl.sha256

Change summary: Machine Mirror hash sidecar updated.

Risk assessment: High

Code review assessment: Expected hash sentinel update after mirror regeneration.

Approved Plan linkage: Required evidence hash posture.

Repo proof: GitHub.fetch\_file → `artifacts/evidence_index.jsonl.sha256` contains `eb8935809652a2b4430658d8d97dcf7022e30d3452c018eccae212cf420ef08b artifacts/evidence_index.jsonl`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-004

File: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt

Change summary: Path proof for Machine Mirror hash sidecar regenerated.

Risk assessment: Medium

Code review assessment: Expected same-PR path-proof update.

Approved Plan linkage: Required governed proof surface.

Repo proof: GitHub.list\_pr\_changed\_filenames → file changed with mirror hash sidecar.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-005

File: artifacts/narratives/router/cli\_http\_parity.log.path\_proof.txt

Change summary: Existing path proof timestamp/proof metadata refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only; no narrative payload change was identified.

Approved Plan linkage: Incidental evidence refresh from index/path-proof tooling.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-006

File: artifacts/narratives/router/parity\_abba.log.path\_proof.txt

Change summary: Existing path proof timestamp/proof metadata refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only; no narrative payload change was identified.

Approved Plan linkage: Incidental evidence refresh from index/path-proof tooling.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-007

File: artifacts/writer/conjunction\_write\_readback.log.path\_proof.txt

Change summary: Existing path proof timestamp/proof metadata refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only; no writer payload change was identified.

Approved Plan linkage: Incidental evidence refresh from index/path-proof tooling.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-008

File: artifacts/writer/conjunction\_writer\_summary.json.path\_proof.txt

Change summary: Existing path proof timestamp/proof metadata refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only; no writer summary payload change was identified.

Approved Plan linkage: Incidental evidence refresh from index/path-proof tooling.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-009

File: audit/docdeltas/hde-epic032\_doc\_deltas.md.path\_proof.txt

Change summary: Existing doc-delta path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-010

File: audit/docdeltas/hde-epic034\_doc\_deltas.md.path\_proof.txt

Change summary: Existing doc-delta path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-011

File: audit/docdeltas/hde-epic035\_doc\_deltas.md.path\_proof.txt

Change summary: Existing doc-delta path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-012

File: audit/docdeltas/hde-epic036\_doc\_deltas.md

Change summary: New HDE-EPIC036 PR-02 doc-delta candidate surface.

Risk assessment: Medium

Code review assessment: Correctly records documentation follow-up only, with PF-Canon untouched and PF09 status movement separate.

Approved Plan linkage: Direct PR-02 doc-delta candidate output.

Repo proof: GitHub.fetch\_file → file states `PF-Canon was not edited`; records HDE-FERM008.6 supportable from repo evidence for route-policy classification and PR-02 evidence-loop binding only; records OPS-01 not required and not executed.

PF reference, if relied on: PF06 — Epic Process Guide, §0.2 Policy and principles

CFR-013

File: audit/docdeltas/hde-epic036\_doc\_deltas.md.path\_proof.txt

Change summary: New path proof for HDE-EPIC036 doc-delta candidate surface.

Risk assessment: Medium

Code review assessment: Expected proof for new governed doc-delta artifact.

Approved Plan linkage: Direct PR-02 path-proof output.

Repo proof: GitHub.list\_pr\_changed\_filenames → new path-proof file present.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-014

File: audit/gates/narratives/keys\_10x4.table.json.path\_proof.txt

Change summary: Existing path proof timestamp/proof metadata refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only; no narrative gate payload change was identified.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-015

File: audit/gates/narratives/pack\_identity.txt.path\_proof.txt

Change summary: Existing path proof timestamp/proof metadata refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-016

File: audit/gates/narratives/registry.diff.json.path\_proof.txt

Change summary: Existing path proof timestamp/proof metadata refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-017

File: audit/gates/topology/orientation\_demo.txt

Change summary: Orientation demo regenerated after PR-02 evidence additions.

Risk assessment: Medium

Code review assessment: Expected orientation artifact update after Human Index / Machine Mirror evidence count changed.

Approved Plan linkage: Supports evidence orientation after PR-02 ledger updates.

Repo proof: Optional PR Artifacts and Merged Change body report `tools/evidence/orientation_demo.py --check` passed after update; GitHub.list\_pr\_changed\_filenames shows orientation artifact changed.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-018

File: audit/gates/topology/orientation\_demo.txt.path\_proof.txt

Change summary: Path proof for orientation demo regenerated.

Risk assessment: Low

Code review assessment: Expected proof update after orientation artifact changed.

Approved Plan linkage: Supports path-proof discipline.

Repo proof: GitHub.list\_pr\_changed\_filenames → orientation proof file changed.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-019

File: audit/qa/hde-epic030/pr-03/category\_order\_binding.log.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only; no HDE-EPIC030 payload change was identified.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-020

File: audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-021

File: audit/qa/hde-epic030/pr-03/compat\_parity\_binding.log.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-022

File: audit/qa/hde-epic030/pr-04/band\_edges\_binding.log.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-023

File: audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-024

File: audit/qa/hde-epic030/pr-04/band\_thresholds\_identity\_hash.txt.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-025

File: audit/qa/hde-epic030/pr-05/category\_canonical\_compare.log.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-026

File: audit/qa/hde-epic030/pr-05/category\_framework\_binding.log.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-027

File: audit/qa/hde-epic030/pr-05/per\_channel\_mechanics.json.path\_proof.txt

Change summary: Existing HDE-EPIC030 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-028

File: audit/qa/hde-epic034/00\_meta/doc\_deltas.md.path\_proof.txt

Change summary: Existing HDE-EPIC034 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-029

File: audit/qa/hde-epic035/00\_meta/doc\_deltas.md.path\_proof.txt

Change summary: Existing HDE-EPIC035 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-030

File: audit/qa/hde-epic035/acceptance\_map\_viability.log.path\_proof.txt

Change summary: Existing HDE-EPIC035 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-031

File: audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log.path\_proof.txt

Change summary: Existing HDE-EPIC035 OPS binding proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only; no HDE-EPIC036 OPS execution is implied.

Approved Plan linkage: Incidental path-proof refresh; preserves OPS separation.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF06 — Epic Process Guide, §0.2 Policy and principles

CFR-032

File: audit/qa/hde-epic035/token\_evidence\_matrix.md.path\_proof.txt

Change summary: Existing HDE-EPIC035 path proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-033

File: audit/qa/hde-epic036/00\_meta/doc\_deltas.md

Change summary: New PR-02 QA-meta doc-delta candidate mirror.

Risk assessment: Medium

Code review assessment: Correctly records doc-delta candidates only, preserves PF-Canon untouched, and preserves no-claim boundaries.

Approved Plan linkage: Direct PR-02 doc-delta candidate surface.

Repo proof: GitHub.fetch\_file → file records `PF-Canon was not edited`, `ops_01_executed_for_pr02=false`, `pf09_status_movement_claim=false`, `qa_pass_claim=false`, and `full_runtime_conformance_claim=false`.

PF reference, if relied on: PF06 — Epic Process Guide, §0.2 Policy and principles

CFR-034

File: audit/qa/hde-epic036/00\_meta/doc\_deltas.md.path\_proof.txt

Change summary: New path proof for PR-02 QA-meta doc-delta candidate mirror.

Risk assessment: Medium

Code review assessment: Expected proof for governed doc-delta candidate artifact.

Approved Plan linkage: Direct PR-02 path-proof output.

Repo proof: GitHub.list\_pr\_changed\_filenames → new path-proof file present.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-035

File: audit/qa/hde-epic036/acceptance\_map\_viability.log

Change summary: New PR-02 acceptance-map viability log.

Risk assessment: High

Code review assessment: Correctly records acceptance-map coherence, route-policy posture, OPS non-execution, and pass-after-update posture for index, mirror, hash, and path-proof checks.

Approved Plan linkage: Direct PR-02 viability output.

Repo proof: GitHub.fetch\_file → file records `selected_route_policy_classification=unsupported_runtime_nonclaim`, `ops_01_executed_for_pr02=false`, `actual_ops01_evidence_found=false`, `index_check_posture=PASS_AFTER_UPDATE`, `mirror_check_posture=PASS_AFTER_UPDATE`, `hash_check_posture=PASS_AFTER_UPDATE`, and `path_proof_check_posture=PASS_AFTER_UPDATE`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-036

File: audit/qa/hde-epic036/acceptance\_map\_viability.log.path\_proof.txt

Change summary: New path proof for PR-02 viability log.

Risk assessment: Medium

Code review assessment: Expected proof for governed viability artifact.

Approved Plan linkage: Direct PR-02 path-proof output.

Repo proof: GitHub.list\_pr\_changed\_filenames → new path-proof file present.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-037

File: audit/qa/hde-epic036/token\_evidence\_matrix.md

Change summary: New PR-02 token/evidence matrix.

Risk assessment: High

Code review assessment: Correctly maps approved tokens to concrete PR-01 and PR-02 evidence paths while rejecting QA PASS, OPS completion, PF09 status movement, public-surface expansion, raw payload persistence, AI scope, and full runtime-conformance claims.

Approved Plan linkage: Direct PR-02 token/evidence output.

Repo proof: GitHub.fetch\_file → file records PF09 IDs, selected route-policy classification, nonclaim fields, approved token rows, PR-01 evidence paths, PR-02 evidence-loop artifacts, and explicit “No Live QA runbook execution” / “OPS-01 was not executed for PR-02.”

PF reference, if relied on: PF04 — HDE-Governance, §0.2 Scope & boundaries

CFR-038

File: audit/qa/hde-epic036/token\_evidence\_matrix.md.path\_proof.txt

Change summary: New path proof for PR-02 token/evidence matrix.

Risk assessment: Medium

Code review assessment: Expected proof for governed token/evidence artifact.

Approved Plan linkage: Direct PR-02 path-proof output.

Repo proof: GitHub.list\_pr\_changed\_filenames → new path-proof file present.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-039

File: docs/acceptance\_map\_epic035.json.path\_proof.txt

Change summary: Existing HDE-EPIC035 acceptance-map proof refreshed.

Risk assessment: Low

Code review assessment: Generated proof churn only; no HDE-EPIC035 acceptance-map payload change was identified.

Approved Plan linkage: Incidental path-proof refresh.

Repo proof: GitHub.list\_pr\_changed\_filenames → path-proof file changed only.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-040

File: docs/acceptance\_map\_epic036.json

Change summary: New PR-02 acceptance map.

Risk assessment: High

Code review assessment: Correctly binds PR-01 route-policy evidence into HDE-FERM008.6 PR-02 evidence-loop closure, uses full approved PR-02 token roster, references PR-01 and PR-02 evidence, and preserves all no-claim boundaries.

Approved Plan linkage: Direct PR-02 acceptance-map output.

Repo proof: GitHub.fetch\_file → file records `acceptance_claims_mode:"approved_pr02_token_roster_only"`, `selected_route_policy_classification:"unsupported_runtime_nonclaim"`, full token roster, referenced PR-01 and PR-02 evidence paths, `ops_01.executed_for_pr02:false`, and no-claim boundaries.

PF reference, if relied on: PF04 — HDE-Governance, §0.2 Scope & boundaries

CFR-041

File: docs/acceptance\_map\_epic036.json.path\_proof.txt

Change summary: New path proof for PR-02 acceptance map.

Risk assessment: Medium

Code review assessment: Expected proof for governed acceptance-map artifact.

Approved Plan linkage: Direct PR-02 path-proof output.

Repo proof: GitHub.fetch\_file → path proof records `path: docs/acceptance_map_epic036.json`, `size_bytes: 5636`, and sha256 `c92c1ed76c93066612b8807e5384aed0fd7ebf999619cdd34ce5d9078fb189f6`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-042

File: docs/evidence/INDEX.json

Change summary: Human Evidence Index regenerated with PR-02 HDE-EPIC036 entries.

Risk assessment: High

Code review assessment: Required same-PR evidence index update after new governed PR-02 artifacts were introduced.

Approved Plan linkage: Direct PR-02 Human Evidence Index output.

Repo proof: GitHub.search for `docs/acceptance_map_epic036.json` → `docs/evidence/INDEX.json` participates in PR-02 evidence set; `tools/evidence/update_evidence_index.py` loader adds PR-02 entries to Human Index.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-043

File: docs/evidence/INDEX.json.path\_proof.txt

Change summary: Human Evidence Index path proof regenerated.

Risk assessment: High

Code review assessment: Expected proof update after Human Index changed.

Approved Plan linkage: Direct PR-02 path-proof output.

Repo proof: GitHub.list\_pr\_changed\_filenames → `docs/evidence/INDEX.json.path_proof.txt` changed with Index update.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-044

File: docs/evidence/INDEX.sha256

Change summary: Human Evidence Index hash sentinel updated.

Risk assessment: High

Code review assessment: Expected sentinel update after `docs/evidence/INDEX.json` changed.

Approved Plan linkage: Direct PR-02 hash sentinel output.

Repo proof: GitHub.fetch\_file → `docs/evidence/INDEX.sha256` records `a204d9f913197d193a24262cc13f6a80d51b439df2b59ec1b0d49b8869730369 docs/evidence/INDEX.json`.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-045

File: docs/evidence/INDEX.sha256.path\_proof.txt

Change summary: Path proof for Human Evidence Index hash sentinel regenerated.

Risk assessment: Medium

Code review assessment: Expected proof update after hash sentinel changed.

Approved Plan linkage: Direct PR-02 path-proof output.

Repo proof: GitHub.list\_pr\_changed\_filenames → `docs/evidence/INDEX.sha256.path_proof.txt` changed with sentinel.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

CFR-046

File: tests/evidence/test\_hde\_epic036\_pr02\_evidence\_loop.py

Change summary: New targeted PR-02 evidence-loop tests.

Risk assessment: High

Code review assessment: Tests validate canonical acceptance JSON, exact approved token roster, PR-01 evidence references, PR-02 index/mirror/path-proof parity, Human/Machine parity, OPS-01 nonclaim posture, and no-claim boundaries.

Approved Plan linkage: Direct PR-02 Basic QA check.

Repo proof: GitHub.fetch\_file → tests define `ALLOWED_TOKENS`, require `names == ALLOWED_TOKENS`, verify PR-01 and PR-02 paths, verify index/mirror/path-proof parity, and reject forbidden claim text.

PF reference, if relied on: PF19 — Glow QA Guide, §0.2 Purpose & scope

CFR-047

File: tools/evidence/update\_evidence\_index.py

Change summary: Evidence-index tooling extended for HDE-EPIC036 PR-02 artifacts and tightened after review to require exact PR-02 token roster.

Risk assessment: High

Code review assessment: Final state addresses the pre-merge review finding. Loader validates canonical acceptance JSON, epic identity, selected route-policy classification, exact token roster, required nonclaims, OPS-01 non-execution posture, and existence of all PR-02 artifacts.

Approved Plan linkage: Direct PR-02 ledger tooling change.

Repo proof: GitHub.fetch\_file → `_load_epic036_pr02_entries()` requires canonical JSON, `token_names != allowed` failure condition, required nonclaims, `executed_for_pr02 is False`, and all PR-02 artifact paths to exist.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

Validation Results

VAL-001

Purpose: Identify exact merged change and final repo state.

Command or method: GitHub.get\_pr\_info for PR \#336; GitHub.compare\_commits with base `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74` and head `main`.

Result: PASS

Key output or observation: PR \#336 is closed and merged; merge commit is `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74`; `main` is identical to that merge commit.

Why it matters: Establishes the exact merged change set and confirms current repo state equals the reviewed change.

VAL-002

Purpose: Verify PR-02 evidence generator / route-policy artifacts remain current.

Command or method: Evaluated Merged Change and Optional PR Artifacts for `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py --check`.

Result: PASS

Key output or observation: Reported passed; PR-02 evidence references PR-01 route-policy outputs without changing runtime behavior.

Why it matters: Ensures PR-02 binds current route-policy evidence, not stale PR-01 artifacts.

VAL-003

Purpose: Verify Human Evidence Index / Machine Mirror generation.

Command or method: Evaluated Merged Change and final repo file state for `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/update_evidence_index.py --check`.

Result: PASS

Key output or observation: Reported passed; final `tools/evidence/update_evidence_index.py` includes `_load_epic036_pr02_entries()` and exact PR-02 token roster validation.

Why it matters: This is the core PR-02 evidence-loop binding check.

VAL-004

Purpose: Verify orientation evidence.

Command or method: Evaluated Merged Change for `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/orientation_demo.py --check`.

Result: PASS

Key output or observation: Reported passed; `audit/gates/topology/orientation_demo.txt` changed in the merged change set.

Why it matters: Confirms evidence orientation reflects regenerated ledgers.

VAL-005

Purpose: Verify mirror schema.

Command or method: Evaluated Merged Change for `ci/checks/check_mirror_schema.sh`.

Result: PASS

Key output or observation: Reported passed.

Why it matters: Checks Machine Mirror schema posture after PR-02 entries were added.

VAL-006

Purpose: Verify evidence hash sentinel.

Command or method: Evaluated Merged Change for `ci/checks/check_evidence_index_hash.sh`.

Result: PASS

Key output or observation: Reported passed; final repo contains updated `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl.sha256`.

Why it matters: Confirms hash sidecars match regenerated ledger bytes.

VAL-007

Purpose: Verify PR-02 targeted evidence-loop tests.

Command or method: Evaluated Merged Change for `python -m pytest tests/evidence/test_hde_epic036_pr02_evidence_loop.py`.

Result: PASS

Key output or observation: Reported passed; final test file verifies canonical acceptance JSON, exact token roster, PR-01 evidence references, PR-02 index/mirror/path-proof parity, OPS nonclaim, and no-claim boundaries.

Why it matters: This is the most direct PR-02 behavioral validation.

VAL-008

Purpose: Verify retained runtime tests around PR-01 route-policy behavior.

Command or method: Evaluated Merged Change for `python -m pytest tests/bodygraph/test_vendor_client.py tests/bodygraph/test_bg_resolve_route_policy.py tests/bodygraph/test_resolver_vendor.py tests/cli/test_bg_resolve.py`.

Result: PASS

Key output or observation: Reported passed.

Why it matters: Confirms PR-02 evidence binding did not regress the route-policy implementation it binds.

VAL-009

Purpose: Verify changed Python syntax.

Command or method: Evaluated Merged Change for `python -m py_compile tools/evidence/update_evidence_index.py tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`.

Result: PASS

Key output or observation: Reported passed; final files were readable and structurally coherent.

Why it matters: Confirms changed evidence tooling compiles.

VAL-010

Purpose: Verify LF and diff hygiene.

Command or method: Evaluated Merged Change for `python tools/evidence/check_lf_endings.py` and `git diff --check`.

Result: PASS

Key output or observation: Reported passed.

Why it matters: Confirms governed text artifacts and diff whitespace hygiene.

VAL-011

Purpose: Check GitHub workflow context for merge commit.

Command or method: GitHub.fetch\_commit\_workflow\_runs for `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74`.

Result: INCONCLUSIVE

Key output or observation: `workflow_runs: []`.

Why it matters: No GitHub workflow result was available as independent CI proof. This does not block because targeted validation was reported in Merged Change / Optional PR Artifacts and final repo state matches the merged commit.

VAL-012

Purpose: Verify no HDE-EPIC036 OPS-01 evidence was introduced or claimed.

Command or method: Search method: searched Repo for `audit/ops/hde-epic036/ops-01` (case: sensitive); scope: repo code search; tool: GitHub.search; result: 1 hit, test-only reference in `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`, no actual OPS artifact path found. Search method: searched Repo for `ops_01_executed_for_pr02=true OR ops_completion_claim=true OR qa_pass_claim=true OR pf09_status_movement_claim=true` (case: sensitive); scope: repo code search; tool: GitHub.search; result: 0 hits.

Result: PASS

Key output or observation: Current PR-02 artifacts record `ops_01_executed_for_pr02=false`, and no true-claim strings were found.

Why it matters: Confirms OPS was not simulated or claimed.

RCA

A) Bug/Failure statement

The Optional PR Artifacts report a pre-merge review finding: the PR-02 evidence-index validator initially allowed any subset of approved tokens even though the acceptance-map mode required the approved PR-02 token roster only. The reported example was that a missing token such as `NO_EXTERNAL_IO_ON_REFUSAL_OK` could still let `tools/evidence/update_evidence_index.py --check` index and mirror an incomplete evidence loop.

B) Root cause(s)

1. The initial PR-02 loader checked for tokens outside the allowed set but did not require equality with the complete approved token set.  
   Evidence pointer(s): Optional PR Artifacts finding; final repo proof in `tools/evidence/update_evidence_index.py` now computes `token_names` and requires `token_names == allowed`.  
   PF references: PF04 — HDE-Governance, §0.2 Scope & boundaries; PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes.

C) Fix in this merged change

* `tools/evidence/update_evidence_index.py` now rejects PR-02 acceptance maps whose token names do not exactly equal the approved set.  
  Repo evidence: `_load_epic036_pr02_entries()` defines the allowed token set and raises `INVALID_EPIC036_PR02_ACCEPTANCE_IDENTITY` unless `token_names == allowed`.  
* `tests/evidence/test_hde_epic036_pr02_evidence_loop.py` also requires the acceptance-map token names to equal `ALLOWED_TOKENS`.  
  Repo evidence: test file records `assert names == ALLOWED_TOKENS`.

D) Fix verification

* Optional PR Artifacts report the fix-specific validations passed: `tools/evidence/update_evidence_index.py --check`, PR-02 evidence-loop pytest, `py_compile`, and `git diff --check`.  
* Final repo state contains the stricter loader and exact-token test.  
* No residual token-roster proof gap remains.

Findings

Finding ID: F-001

Related review item: CFR-001 / CFR-002 / CFR-003 / CFR-004 / CFR-042 / CFR-043 / CFR-044 / CFR-045

Severity: Note

Observation: Human Evidence Index, Machine Mirror, hash sentinels, and path proofs were updated in the same merged change.

Why it matters: PR-02 introduced governed evidence artifacts, and ledger parity is required for trustable evidence binding.

Evidence: Repo proof: `tools/evidence/update_evidence_index.py` adds PR-02 entries and loader insertion; `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl.sha256` changed with ledger updates. PF proof excerpt: “The Human Evidence Index (`docs/evidence/INDEX.json`) and Machine Evidence Mirror (`artifacts/evidence_index.jsonl`) are an explicit dual-home pair of pointer ledgers and MUST maintain strict parity.”

Required action: None.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

Finding ID: F-002

Related review item: CFR-005 / CFR-006 / CFR-007 / CFR-008 / CFR-009 / CFR-010 / CFR-011 / CFR-014 / CFR-015 / CFR-016 / CFR-019 / CFR-020 / CFR-021 / CFR-022 / CFR-023 / CFR-024 / CFR-025 / CFR-026 / CFR-027 / CFR-028 / CFR-029 / CFR-030 / CFR-031 / CFR-032 / CFR-039

Severity: Concern

Observation: The merged change refreshed many pre-existing path-proof files outside HDE-EPIC036.

Why it matters: Broad proof refreshes increase review noise, but this appears to be generated ledger/path-proof churn rather than payload drift.

Evidence: Repo proof: changed file list shows many existing `.path_proof.txt` files outside HDE-EPIC036 changed; no underlying paired payloads for those older epics were listed as changed.

Required action: None for this merged change; keep future refreshes as scoped as tooling allows.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

Finding ID: F-003

Related review item: CFR-012 / CFR-013 / CFR-033 / CFR-034

Severity: Note

Observation: PR-02 created doc-delta candidate surfaces only and did not edit PF-Canon.

Why it matters: Documentation drainage must remain separate from implementation and evidence-loop binding.

Evidence: Repo proof: `audit/docdeltas/hde-epic036_doc_deltas.md` states “PF-Canon was not edited”; `audit/qa/hde-epic036/00_meta/doc_deltas.md` states the QA-meta mirror records doc-delta candidates only. PF proof excerpt: “Coding agents and Implementation Agents MAY NOT directly modify PF-Canon documents as part of implementation PR work.”

Required action: None.

PF reference, if relied on: PF06 — Epic Process Guide, §0.2 Policy and principles

Finding ID: F-004

Related review item: CFR-017 / CFR-018

Severity: Note

Observation: Orientation evidence was regenerated as part of evidence-loop update.

Why it matters: Orientation evidence should remain coherent after new governed artifacts are indexed.

Evidence: Repo proof: changed file list includes `audit/gates/topology/orientation_demo.txt` and its path proof; Merged Change reports `tools/evidence/orientation_demo.py --check` passed.

Required action: None.

PF reference, if relied on: PF12 — HDE-Schemas and Artifacts, §0.2 Scope & single homes

Finding ID: F-005

Related review item: CFR-035 / CFR-036 / CFR-037 / CFR-038 / CFR-040 / CFR-041

Severity: Note

Observation: PR-02 acceptance-map, viability, and token/evidence surfaces correctly preserve no-claim boundaries and OPS non-execution posture.

Why it matters: PR-02 must bind evidence without claiming QA PASS, OPS completion, PF09 status movement, closeout, public surface expansion, raw payload persistence, AI scope, or full runtime conformance.

Evidence: Repo proof: `docs/acceptance_map_epic036.json` records required nonclaims and `ops_01.executed_for_pr02:false`; `audit/qa/hde-epic036/token_evidence_matrix.md` records false claim fields; `audit/qa/hde-epic036/acceptance_map_viability.log` records `ops_01_executed_for_pr02=false` and `PF-Canon edit=false`.

Required action: None.

PF reference, if relied on: PF04 — HDE-Governance, §0.2 Scope & boundaries

Finding ID: F-006

Related review item: CFR-046

Severity: Note

Observation: New PR-02 tests directly cover the acceptance map, token roster, PR-01 references, PR-02 indexing/mirroring/path proofs, OPS nonclaim posture, and no-claim boundaries.

Why it matters: The tests are scoped to the merged evidence-loop work and prevent the exact token-roster regression identified in review.

Evidence: Repo proof: `tests/evidence/test_hde_epic036_pr02_evidence_loop.py` includes `assert names == ALLOWED_TOKENS`, PR-01 path checks, PR-02 index/mirror/path-proof checks, and forbidden-claim checks.

Required action: None.

PF reference, if relied on: PF19 — Glow QA Guide, §0.2 Purpose & scope

Finding ID: F-007

Related review item: CFR-047 / RCA

Severity: Note

Observation: The pre-merge validator bug was fixed in final repo state.

Why it matters: A subset token roster would weaken the PR-02 evidence loop while still passing the generator check.

Evidence: Repo proof: `tools/evidence/update_evidence_index.py` requires `token_names == allowed` and raises `INVALID_EPIC036_PR02_ACCEPTANCE_IDENTITY` otherwise.

Required action: None.

PF reference, if relied on: PF04 — HDE-Governance, §0.2 Scope & boundaries

Finding ID: F-008

Related review item: VAL-001

Severity: Note

Observation: Current branch state equals the merged PR \#336 commit.

Why it matters: The reviewed state is the current merged repo state.

Evidence: Repo proof: GitHub.compare\_commits returned `status: identical`, `ahead_by: 0`, `behind_by: 0`, and `total_commits: 0`.

Required action: None.

PF reference, if relied on: None

Finding ID: F-009

Related review item: VAL-002 / VAL-003 / VAL-004 / VAL-005 / VAL-006 / VAL-007 / VAL-008 / VAL-009 / VAL-010

Severity: Note

Observation: Targeted validation was sufficient for this post-merge review scope.

Why it matters: The commands cover evidence generation checks, index/mirror/hash checks, PR-02 tests, retained route-policy tests, py\_compile, LF endings, and diff hygiene.

Evidence: Repo proof: Merged Change body reports all targeted commands passed; final files contain the test and loader coverage that those commands exercise.

Required action: None.

PF reference, if relied on: PF19 — Glow QA Guide, §0.2 Purpose & scope

Finding ID: F-010

Related review item: VAL-011

Severity: Note

Observation: No GitHub workflow runs were returned for the merge commit.

Why it matters: There is no independent GitHub workflow proof to add, but that does not block because targeted validation and final repo state were inspected.

Evidence: Repo proof: GitHub.fetch\_commit\_workflow\_runs for `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74` returned `workflow_runs: []`.

Required action: None.

PF reference, if relied on: None

Finding ID: F-011

Related review item: VAL-012 / Evidence

Severity: Note

Observation: OPS-01 was not executed or simulated for PR-02.

Why it matters: OPS is PO-only, and PR-02 scope is evidence-loop binding only.

Evidence: Repo proof: `docs/acceptance_map_epic036.json`, `audit/qa/hde-epic036/token_evidence_matrix.md`, and `audit/qa/hde-epic036/acceptance_map_viability.log` all record OPS non-execution. Search method: searched Repo for `ops_01_executed_for_pr02=true OR ops_completion_claim=true OR qa_pass_claim=true OR pf09_status_movement_claim=true` (case: sensitive); scope: repo code search; tool: GitHub.search; result: 0 hits.

Required action: None.

PF reference, if relied on: PF06 — Epic Process Guide, §0.2 Policy and principles

Finding ID: F-012

Related review item: PF09

Severity: Note

Observation: HDE-FERM008.6 is now supportable for status change to Done from repo evidence, while HDE-FERM008 parent Done remains out of scope.

Why it matters: PR-01 implemented route-policy proof; PR-02 bound it into the governed evidence loop. The PR artifacts explicitly avoid parent Done and closeout claims.

Evidence: Repo proof: `docs/acceptance_map_epic036.json` records `pf09_scope_supported_by_this_pr:["HDE-FERM008.6 route-policy classification and evidence-loop binding only"]`; `audit/docdeltas/hde-epic036_doc_deltas.md` records HDE-FERM008.6 supportable from repo evidence and PF09 status movement as separate drainage. PF proof excerpt: “Subtask status: Not done”; “The future proof must show whether `bg:resolve --source vendor` is v2 chart-backed, explicit legacy fallback, dual-route, or unsupported.”

Required action: No remediation. PF09 status drainage may later update HDE-FERM008.6 to Done.

PF reference, if relied on: PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

PF09 Impact & Status Posture

PF09 document: PF09.5-Canon-HDE-Build-Checklist-Fermentation

PF09 task ID: HDE-FERM008

PF09 subtask ID(s): HDE-FERM008.6

Current PF09 status: HDE-FERM008: Partial; HDE-FERM008.6: Not done

Status recommendation: change to Done

Why this status posture is supported: PR-01 implemented and evidenced the explicit `bg:resolve --source vendor` route-policy classification. PR-02 then bound that already-landed evidence into the governed evidence loop with acceptance map, token matrix, viability log, doc-delta candidate surfaces, Human Evidence Index, Machine Mirror, hash sentinels, path proofs, and targeted validation. The recommendation applies to HDE-FERM008.6 only; HDE-FERM008 parent Done, epic closeout, and full HumanDesignAPI v2 runtime conformance remain out of scope.

Evidence pointer(s):  
Repo proof: `docs/acceptance_map_epic036.json` → `selected_route_policy_classification:"unsupported_runtime_nonclaim"`, `pf09_scope_supported_by_this_pr:["HDE-FERM008.6 route-policy classification and evidence-loop binding only"]`, `pf09_scope_not_completed_by_this_pr:["HDE-FERM008 parent Done","PF09 status drainage","epic closeout","full HumanDesignAPI v2 runtime conformance"]`.  
Repo proof: `audit/qa/hde-epic036/token_evidence_matrix.md` → `pf09_task_id=HDE-FERM008`, `pf09_subtask_id=HDE-FERM008.6`, `pf09_status_movement_claim=false`, and approved token-to-evidence mapping.  
Repo proof: `audit/qa/hde-epic036/acceptance_map_viability.log` → `index_check_posture=PASS_AFTER_UPDATE`, `mirror_check_posture=PASS_AFTER_UPDATE`, `hash_check_posture=PASS_AFTER_UPDATE`, and `path_proof_check_posture=PASS_AFTER_UPDATE`.  
Repo proof: `tests/evidence/test_hde_epic036_pr02_evidence_loop.py` validates PR-02 acceptance map, token roster, PR-01 evidence references, PR-02 index/mirror/path-proof parity, OPS nonclaim posture, and no-claim boundaries.

PF proof excerpt(s), when PF09 is relied on:  
PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

“Define and prove the runtime vendor-route policy for `bg:resolve --source vendor` so BodyGraph detail resolution is no longer an accidental legacy BodyGraph route composed against a configured v2 base.”

“Subtask status: Not done”

“The future proof must show whether `bg:resolve --source vendor` is v2 chart-backed, explicit legacy fallback, dual-route, or unsupported.”

Evidence Print

A) Tokens satisfied

TESTS\_PASS\_OK

Evidence pointer(s): `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`; `tests/bodygraph/test_bg_resolve_route_policy.py`; Merged Change reports PR-02 evidence-loop pytest and retained bodygraph/CLI suites passed.

DOC\_DELTA\_PRESENT\_OK

Evidence pointer(s): `audit/docdeltas/hde-epic036_doc_deltas.md`; `audit/qa/hde-epic036/00_meta/doc_deltas.md`; both have sibling path proofs and are indexed/mirrored by PR-02.

EVIDENCE\_INDEX\_UPDATED\_OK

Evidence pointer(s): `docs/evidence/INDEX.json`; `tools/evidence/update_evidence_index.py`; Merged Change reports `update_evidence_index.py --check` passed.

MACHINE\_MIRROR\_UPDATED\_OK

Evidence pointer(s): `artifacts/evidence_index.jsonl`; `tools/evidence/update_evidence_index.py`; PR-02 tests verify PR-02 paths in Machine Mirror.

EVIDENCE\_INDEX\_HASH\_OK

Evidence pointer(s): `docs/evidence/INDEX.sha256`; `artifacts/evidence_index.jsonl.sha256`; Merged Change reports `ci/checks/check_evidence_index_hash.sh` passed.

EVIDENCE\_PATHS\_VALIDATED\_OK

Evidence pointer(s): `tools/evidence/update_evidence_index.py --check`; `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`; PR-02 tests verify PR-02 artifact paths and sibling path proofs.

EVIDENCE\_PATH\_PROOFS\_OK

Evidence pointer(s): `docs/acceptance_map_epic036.json.path_proof.txt`; `audit/qa/hde-epic036/token_evidence_matrix.md.path_proof.txt`; `audit/qa/hde-epic036/acceptance_map_viability.log.path_proof.txt`; `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`; `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`; retained PR-01 path proofs.

JSON\_CANONICAL\_CHECK\_OK

Evidence pointer(s): `docs/acceptance_map_epic036.json`; PR-01 JSON route-policy artifacts; `tools/evidence/update_evidence_index.py` canonical JSON check; `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`.

NO\_EXTERNAL\_IO\_ON\_REFUSAL\_OK

Evidence pointer(s): `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`; `tests/bodygraph/test_bg_resolve_route_policy.py`; `docs/acceptance_map_epic036.json`.

ENV\_RAILS\_POLICY\_OK

Evidence pointer(s): `audit/qa/hde-epic036/route_policy_decision.log`; `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`; closed-rails validation commands reported in Merged Change.

B) Evidence artifacts produced or updated

Path: docs/acceptance\_map\_epic036.json

Type: governed canonical JSON acceptance map

Key proof facts observed: approved PR-02 token roster only; `selected_route_policy_classification:"unsupported_runtime_nonclaim"`; OPS-01 not executed; HDE-FERM008.6 supported only for route-policy classification and evidence-loop binding; no-claim boundaries preserved.

sha256, if observed: c92c1ed76c93066612b8807e5384aed0fd7ebf999619cdd34ce5d9078fb189f6

Index/Mirror/path-proof posture, if relevant: Sibling path proof exists; registered through `EPIC036_PR02_PRIMARY_ARTIFACTS`; indexed/mirrored.

Path: audit/qa/hde-epic036/token\_evidence\_matrix.md

Type: governed token/evidence matrix

Key proof facts observed: maps every approved token to concrete PR-01/PR-02 evidence; records false claims for QA PASS, OPS completion, PF09 status movement, closeout, full runtime conformance, public surface expansion, raw payload persistence, and AI scope.

sha256, if observed: not separately observed in fetched content.

Index/Mirror/path-proof posture, if relevant: Sibling path proof exists; registered through `EPIC036_PR02_PRIMARY_ARTIFACTS`; indexed/mirrored.

Path: audit/qa/hde-epic036/acceptance\_map\_viability.log

Type: governed viability log

Key proof facts observed: records acceptance-map coherence; unsupported-runtime nonclaim; no OPS-01 execution; pass-after-update posture for index, mirror, hash, and path proofs.

sha256, if observed: not separately observed in fetched content.

Index/Mirror/path-proof posture, if relevant: Sibling path proof exists; registered through `EPIC036_PR02_PRIMARY_ARTIFACTS`; indexed/mirrored.

Path: audit/docdeltas/hde-epic036\_doc\_deltas.md

Type: governed doc-delta candidate surface

Key proof facts observed: records HDE-FERM008.6 supportable from repo evidence; PF-Canon not edited; PF09 status movement separate; no runtime-conformance or public-surface claims.

sha256, if observed: not separately observed in fetched content.

Index/Mirror/path-proof posture, if relevant: Sibling path proof exists; registered through `EPIC036_PR02_PRIMARY_ARTIFACTS`; indexed/mirrored.

Path: audit/qa/hde-epic036/00\_meta/doc\_deltas.md

Type: governed QA-meta doc-delta candidate mirror

Key proof facts observed: records doc-delta candidates only; PF-Canon untouched; route-policy and no-claim posture preserved.

sha256, if observed: not separately observed in fetched content.

Index/Mirror/path-proof posture, if relevant: Sibling path proof exists; registered through `EPIC036_PR02_PRIMARY_ARTIFACTS`; indexed/mirrored.

Path: docs/evidence/INDEX.json

Type: Human Evidence Index

Key proof facts observed: regenerated to include PR-02 governed artifacts.

sha256, if observed: a204d9f913197d193a24262cc13f6a80d51b439df2b59ec1b0d49b8869730369 from `docs/evidence/INDEX.sha256`.

Index/Mirror/path-proof posture, if relevant: Hash sentinel and path proof updated.

Path: artifacts/evidence\_index.jsonl

Type: Machine Evidence Mirror

Key proof facts observed: regenerated to include PR-02 governed artifacts and preserve mirror parity.

sha256, if observed: eb8935809652a2b4430658d8d97dcf7022e30d3452c018eccae212cf420ef08b from `artifacts/evidence_index.jsonl.sha256`.

Index/Mirror/path-proof posture, if relevant: Hash sidecar and path proof updated.

Path: docs/evidence/INDEX.sha256

Type: Human Evidence Index hash sentinel

Key proof facts observed: points to `docs/evidence/INDEX.json`.

sha256, if observed: file content records `a204d9f913197d193a24262cc13f6a80d51b439df2b59ec1b0d49b8869730369`.

Index/Mirror/path-proof posture, if relevant: Sibling path proof updated.

Path: artifacts/evidence\_index.jsonl.sha256

Type: Machine Evidence Mirror hash sidecar

Key proof facts observed: points to `artifacts/evidence_index.jsonl`.

sha256, if observed: file content records `eb8935809652a2b4430658d8d97dcf7022e30d3452c018eccae212cf420ef08b`.

Index/Mirror/path-proof posture, if relevant: Sibling path proof updated.

C) Validation proof

Command or method: GitHub.compare\_commits `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74...main`

Result: PASS

Where the result appears: Repo Inspection / VAL-001

Why it is sufficient: Confirms current reviewed repo state equals the merged change set.

Command or method: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py --check`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms PR-01 route-policy evidence bound by PR-02 remains current.

Command or method: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/update_evidence_index.py --check`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms Human Index / Machine Mirror / PR-02 loader posture, including exact token roster validation.

Command or method: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/orientation_demo.py --check`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms orientation evidence after ledger regeneration.

Command or method: `ci/checks/check_mirror_schema.sh`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms Machine Mirror schema posture.

Command or method: `ci/checks/check_evidence_index_hash.sh`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms Evidence Index hash sentinel.

Command or method: `python -m pytest tests/evidence/test_hde_epic036_pr02_evidence_loop.py`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts; final test file inspected.

Why it is sufficient: Direct targeted PR-02 evidence-loop validation.

Command or method: `python -m pytest tests/bodygraph/test_vendor_client.py tests/bodygraph/test_bg_resolve_route_policy.py tests/bodygraph/test_resolver_vendor.py tests/cli/test_bg_resolve.py`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms retained route-policy runtime tests after evidence-loop binding.

Command or method: `python -m py_compile tools/evidence/update_evidence_index.py tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms changed evidence tooling compiles.

Command or method: `python tools/evidence/check_lf_endings.py`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms governed text LF discipline.

Command or method: `git diff --check`

Result: PASS

Where the result appears: Merged Change and Optional PR Artifacts.

Why it is sufficient: Confirms diff whitespace hygiene.

Doc Delta Candidates

DDC-001

Doc: PF09.5 — HDE Build Checklist Fermentation

Section: §Subtask HDE-FERM008.6 \- Define and prove explicit vendor-route policy for `bg:resolve --source vendor`

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.6

PF09 status action: change to Done

Delta: Update HDE-FERM008.6 from Not done to Done, supported by HDE-EPIC036 PR-01 route-policy implementation and PR-02 governed evidence-loop binding.

Why: PR-01 implemented and evidenced explicit `bg:resolve --source vendor` route-policy classification; PR-02 completed the governed acceptance/evidence-loop binding without OPS execution, PF09 parent Done, epic closeout, or full HumanDesignAPI v2 runtime-conformance claims.

Repo evidence: `docs/acceptance_map_epic036.json`; `audit/qa/hde-epic036/token_evidence_matrix.md`; `audit/qa/hde-epic036/acceptance_map_viability.log`; `audit/docdeltas/hde-epic036_doc_deltas.md`; `audit/qa/hde-epic036/00_meta/doc_deltas.md`; `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`; `tools/evidence/update_evidence_index.py`.

Canon proof excerpt:

“Subtask status: Not done”

“The future proof must show whether `bg:resolve --source vendor` is v2 chart-backed, explicit legacy fallback, dual-route, or unsupported.”

“It must not treat `charts/simple` success as proof of full BodyGraph detail.”

DDC-002

Doc: PF05 — HDE CLI/API Vendor Ref

Section: §0.2 Scope \[Required-Now\]

Canon basis: CANON SILENCE

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.6

PF09 status action: No status change recommended

Delta: Consider recording the implemented `bg:resolve --source vendor` route-policy behavior: configured v2 bases select explicit unsupported-runtime nonclaim and block legacy `bodygraphs` request construction; non-v2 bases preserve explicit legacy fallback.

Why: The merged HDE-EPIC036 work changes CLI/vendor route-policy behavior and provider error posture. PF05 owns CLI/vendor bytes and behavior, but permanent PF05 text has not yet recorded this exact `bg:resolve` route-policy classification.

Repo evidence: `engine/bodygraph/vendor_client.py`; `engine/bodygraph/resolver.py`; `engine/cli/main.py`; `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`; `audit/qa/hde-epic036/route_policy_decision.log`.

Canon proof excerpt: N/A (CANON SILENCE)

DDC-003

Doc: PF12 — HDE Schemas and Artifacts

Section: §0.2 Scope & single homes \[Required-Now\]

Canon basis: CANON SILENCE

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.6

PF09 status action: No status change recommended

Delta: Consider adding the HDE-EPIC036 `bg_resolve_*` and PR-02 evidence-loop family to permanent Evidence Catalog description if this evidence family should be permanently discoverable beyond current Human Index / Machine Mirror records.

Why: PR-01 and PR-02 introduced and bound a new governed evidence family under `artifacts/vendor/hdapi_v2/`, `audit/qa/hde-epic036/`, `audit/docdeltas/`, and `docs/acceptance_map_epic036.json`. The Human Index and Machine Mirror are current, but permanent catalog prose may reduce future ambiguity.

Repo evidence: `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`; `tools/evidence/update_evidence_index.py`; `docs/acceptance_map_epic036.json`; `audit/qa/hde-epic036/token_evidence_matrix.md`; `audit/qa/hde-epic036/acceptance_map_viability.log`; `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`.

Canon proof excerpt: N/A (CANON SILENCE)

DDC-004

Doc: PF10 — HDE Build Notes

Section: §2.2 PR-01 HDE-EPIC036

Canon basis: PF09 STATUS SUPPORT

Impacted PF09 task ID(s): HDE-FERM008

Impacted PF09 subtask ID(s): HDE-FERM008.6

PF09 status action: change to Done

Delta: Record the PR-02 post-merge review result as merged change acceptable and mark HDE-FERM008.6 supportable for PF09 status drainage to Done, while preserving later Live QA / closeout / PF-canon drainage as separate axes.

Why: PF10 already holds live HDE-EPIC036 PR-01 review posture and PR-02 follow-up context. PR-02 now closes the evidence-loop binding that PR-01 left as follow-up.

Repo evidence: PR \#336 merge commit `5e159a9f338cf160b202b6c9c64b3d9ff4dcee74`; `docs/acceptance_map_epic036.json`; `audit/qa/hde-epic036/token_evidence_matrix.md`; `audit/qa/hde-epic036/acceptance_map_viability.log`.

Canon proof excerpt:

“no PF09 status change is recommended from PR-01 alone because PR-02 evidence-loop binding remains follow-up in the Approved Plan and in the merged evidence.”

“Closure axes remain separate. QA evidence, PF09 status drainage, PO closeout, board state, merge provenance, and PF-canon drainage are separate closure axes and MUST NOT be collapsed.”

DECISION: MERGED CHANGE ACCEPTABLE

##  2.5) Implementation Retrospective HDE-EPIC036

Executive Summary

* HDE-EPIC036 set out to resolve the remaining Fermentation route-policy gap for the operator-facing workflow `bg:resolve --source vendor`. The Implementation Plan described the target as defining and proving whether BodyGraph-detail resolution should be v2 chart-backed, explicit legacy fallback, dual-route, or unsupported-runtime nonclaim. Artifact → Implementation Plan HDE-EPIC036 → Brief recap of scope → “HDE-EPIC036 completes the remaining Fermentation route-policy gap...” | “The work defines and proves the selected runtime posture...”  
* The conservative planned posture was to prevent accidental legacy `bodygraphs` composition against a configured v2 base from being treated as compatibility, while avoiding new public Reader scope, public flags, public payloads, new HTTP homes, app-side HumanDesignAPI calls, raw secret persistence, uncontrolled raw vendor payload persistence, AI scope, or full HumanDesignAPI v2 runtime-conformance claims. Artifact → Implementation Plan HDE-EPIC036 → Brief recap of scope → “prevent accidental legacy `bodygraphs` composition against a configured v2 base...” | “No public Reader surface... AI scope, or full HumanDesignAPI v2 runtime conformance claim is planned.”  
* PF10 records PR-01 as the route-policy implementation slice: configured v2 bases select `unsupported_runtime_nonclaim`, non-v2 bases preserve explicit legacy BodyGraph fallback, route policy happens before request construction, and closed-rails refusal remains earlier than route-policy logic. PF10 — HDE-Build Notes → §2.2 PR-01 HDE-EPIC036 → “The merged change implements explicit `bg:resolve --source vendor` route-policy classification...” | “Final code state shows policy classification before request construction...”  
* Current repo code supports that record: `classify_bg_resolve_route_policy()` returns `unsupported_runtime_nonclaim` with `PROVIDER_ROUTE_UNSUPPORTED` for configured v2 bases and `explicit_legacy_fallback` for non-v2 bases. Repo → `engine/bodygraph/vendor_client.py` → “`classification`: `unsupported_runtime_nonclaim`” | “`error_code`: `PROVIDER_ROUTE_UNSUPPORTED`” | “`classification`: `explicit_legacy_fallback`”  
* Current resolver code enforces the policy before vendor input normalization and ingest: it classifies route policy, attaches it to resolver metadata, and returns a vendor error when `route_policy["supported"]` is false. Repo → `engine/bodygraph/resolver.py` → “`route_policy = _classify_env_route_policy(vendor_env)`” | “`if not route_policy["supported"]:`”  
* PR-01 evidence exists for route-policy decision, request shape, BodyGraph-detail sufficiency nonclaim, runtime nonclaims, and policy binding. Repo → `audit/qa/hde-epic036/route_policy_decision.log` → “`selected_route_policy_classification=unsupported_runtime_nonclaim`” | “`configured_v2_bg_resolve_request_shape=NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM`” | “`OPS-01 not required by PR-01...`”  
* PF10 records PR-02 as the evidence-loop binding slice: it bound PR-01 route-policy evidence into `docs/acceptance_map_epic036.json`, token/evidence matrix, viability log, doc-delta candidate surfaces, Human Evidence Index, Machine Mirror, hash sentinels, and path proofs. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “Expected PR-02 artifacts were found...” | “The merged change preserves the PR-01 classification...”  
* Current repo evidence also records PR-02’s no-claim posture: no OPS-01 execution, no PF09 status movement, no epic closeout, no HDE-FERM008 parent Done, and no full HumanDesignAPI v2 runtime-conformance claim. Repo → `docs/acceptance_map_epic036.json` → “`executed_for_pr02`: false” | “`pf09_scope_supported_by_this_pr`: \[`HDE-FERM008.6 route-policy classification and evidence-loop binding only`\]” | “`nonclaims`: \[`QA PASS`, `OPS completion`, `PF09 status movement`...\]”  
* The final repo-docs sweep is present in current repo state: the docs PR merged as `369e7b5e3fee05ef012a756241e160c691bb8a6b`, and current README/CHANGELOG/AGENTS/docs now describe HDE-EPIC036 route-policy and evidence-loop posture. Repo → Git commit search → “`sha: 369e7b5e3fee05ef012a756241e160c691bb8a6b`” | “`message: docs: add HDE-EPIC036 final sweep (#337)`”

Biggest wins and remaining risks or gaps:

* Biggest win: the epic turned an ambiguous `bg:resolve --source vendor` v2/legacy mismatch into an explicit route-policy classification, with tests and governed evidence rather than a silent compatibility assumption. Repo → `engine/bodygraph/vendor_client.py` → “configured v2 base cannot use legacy bodygraphs as final BodyGraph-detail behavior...”  
* Biggest win: evidence-loop binding now exists in repo-managed surfaces, including acceptance map, token/evidence matrix, viability log, Human Evidence Index, Machine Mirror, hash sentinels, and path proofs. Repo → `docs/acceptance_map_epic036.json` → referenced evidence paths include PR-01 artifacts, PR-02 artifacts, `docs/evidence/INDEX.json`, and `artifacts/evidence_index.jsonl`.  
* Remaining risk: PF09.5 status drainage is separate from implementation/evidence work. PF10 records HDE-FERM008.6 as supportable for a later status action, while the repo docs explicitly say the docs sweep does not move PF09.5 status. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “HDE-FERM008.6 is supportable for status change to Done...” | “HDE-FERM008 parent Done remains out of scope.”  
* Remaining risk: PF05 and PF12 permanent canon text has not been shown as drained in the current inspected repo/PF10 set. Docs PR content names PF05 route-policy wording and PF12 `bg_resolve_*` catalog prose as PF-Canon follow-up homes. Repo → Docs PR HDE-EPIC036 → “PF05 route-policy wording and PF12 `bg_resolve_*` catalog prose remain PF-Canon follow-up.”  
* Unknown: this report did not establish a current dedicated HDE-EPIC036 close-pack manifest or close report. What would prove it: current repo evidence such as `audit/EPIC-036_MANIFEST.json` and `audit/EPIC-036_close_report.md`, or another Lead-authorized close-pack artifact inspected directly.

Repo Inspection Summary

* Observed repo root: `amthorn78/glow-hdengine-v2`. Repo → GitHub PR \#337 metadata → base branch `main`, merge commit `369e7b5e3fee05ef012a756241e160c691bb8a6b`.  
* Observed HEAD: latest inspected commit for the current `main` branch was `369e7b5e3fee05ef012a756241e160c691bb8a6b`, message `docs: add HDE-EPIC036 final sweep (#337)`. Repo → Git commit search → “`sha: 369e7b5e3fee05ef012a756241e160c691bb8a6b`” | “`created_at: 2026-07-02T13:48:56.000+01:00`”  
* Branch or detached state: remote GitHub inspection showed PR \#337 merged into base branch `main`; no local checkout branch state was available through the connector. Repo → GitHub PR \#337 metadata → “`state`: `closed`” | “`merged`: true” | “`base`: `main`”  
* Working tree status before review: Unknown in a local shell sense because inspection used the GitHub connector against remote repo state, not a mutable local working tree. What would prove it: a live local `git status --short --branch` from `glow-hdengine-v2`.  
* Primary epic-related repo evidence discovered:  
  * Code: `engine/bodygraph/vendor_client.py`, `engine/bodygraph/resolver.py`, `engine/bodygraph/ingest.py`, and `engine/cli/main.py`. Repo → `engine/cli/main.py` → `bg:resolve` parser and source choices `auto`, `db`, `vendor`  
  * PR-01 route-policy decision evidence: `audit/qa/hde-epic036/route_policy_decision.log`. Repo → route-policy decision log → selected classification and no-claim lines  
  * PR-02 acceptance evidence: `docs/acceptance_map_epic036.json`. Repo → acceptance map → selected classification, referenced paths, tokens, and nonclaims  
  * Docs sweep evidence: README, CHANGELOG, AGENTS, `docs/CLI_commands.md`, `docs/EVIDENCE_INDEX.md`, `docs/INDEX.md`, and `docs/RUN.md` changed in PR \#337. Repo → PR \#337 metadata → “`changed_files`: 7” | “`additions`: 53” | “`deletions`: 20”  
* Primary epic-related repo evidence not found:  
  * Current HDE-EPIC036 OPS-01 execution evidence was not found in the inspected repo-search posture. Search method: searched Repo for `audit/ops/hde-epic036/ops-01` (case: sensitive); scope: repo code search; tool: GitHub.search; result: 1 hit, test-only reference in `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`, no actual OPS artifact path found.  
  * No true-claim strings were found for PR-02 OPS execution, OPS completion, QA PASS, or PF09 status movement. Search method: searched Repo for `ops_01_executed_for_pr02=true OR ops_completion_claim=true OR qa_pass_claim=true OR pf09_status_movement_claim=true` (case: sensitive); scope: repo code search; tool: GitHub.search; result: 0 hits.  
* Key current repo surfaces that shaped this report:  
  * `engine/bodygraph/vendor_client.py` for route-family classification and redacted auth posture. Repo → `route_auth_posture` and `classify_bg_resolve_route_policy`  
  * `engine/bodygraph/resolver.py` for pre-ingest route-policy enforcement. Repo → route-policy classification and unsupported rejection  
  * `docs/acceptance_map_epic036.json` for PR-02 evidence-loop scope and nonclaim posture. Repo → acceptance map one-line canonical JSON  
  * `docs/EVIDENCE_INDEX.md` and `docs/INDEX.md` for docs-side evidence navigation. Repo → `docs/EVIDENCE_INDEX.md` HDE-EPIC036 evidence navigation ; Repo → `docs/INDEX.md` HDE-EPIC036 current section  
* Human Evidence Index and Machine Mirror posture:  
  * Repo docs identify the Human Evidence Index at `docs/evidence/INDEX.json` and Machine Mirror at `artifacts/evidence_index.jsonl`. Repo → README Evidence & QA → “Evidence skeleton...”  
  * PR-02 acceptance map references both `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` among its evidence paths. Repo → `docs/acceptance_map_epic036.json` → referenced evidence paths include `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`  
* Working tree status after read-only validation commands: no validation commands were run locally by this report session; remote repo state was inspected read-only.

Implementation Report (What happened in the repo)

PR/step breakdown

* Planning and approval step:  
  * Purpose: define implementation scope for HDE-EPIC036 route-policy work.  
  * Key planned work: make `bg:resolve --source vendor` route policy explicit; avoid treating v2 configured-base \+ legacy `bodygraphs` composition as compatibility; produce governed evidence for BodyGraph-detail sufficiency or unsupported-runtime nonclaim. Artifact → Implementation Plan HDE-EPIC036 → Brief recap of scope → “prevent accidental legacy `bodygraphs` composition...” | “produce governed evidence...”  
  * Supplemental artifact use:  
    * Gap in PF10/PF-Canon/Repo: PF10 and repo prove outcomes/current state, but not the original intended implementation scope.  
    * Evidence pointer: Artifact → Implementation Plan HDE-EPIC036 → Brief recap of scope → “HDE-EPIC036 completes the remaining Fermentation route-policy gap...”  
  * Outcome: plan approval artifact recorded no blockers and no ADR action. Artifact → approval Implementation Plan HDE-EPIC036 → Review Summary → “No blockers found.” | “No ADR action required.”  
* PR-01 — route-policy implementation and proof artifacts:  
  * Purpose: implement explicit `bg:resolve --source vendor` route-policy classification and produce route-policy evidence.  
  * Key changes, high level: PR-01 changed vendor/resolver behavior so configured v2 bases classify as `unsupported_runtime_nonclaim` and return `PROVIDER_ROUTE_UNSUPPORTED`; non-v2 bases preserve explicit legacy fallback. Repo → `engine/bodygraph/vendor_client.py` → v2 and non-v2 return branches  
  * Key surfaces touched: `engine/bodygraph/vendor_client.py`, `engine/bodygraph/resolver.py`, `engine/bodygraph/ingest.py`, `engine/cli/main.py`, `tests/bodygraph/test_bg_resolve_route_policy.py`, `tests/bodygraph/test_resolver_vendor.py`, `tests/cli/test_bg_resolve.py`, and `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`. PF10 — HDE-Build Notes → §2.2 PR-01 HDE-EPIC036 → “Changed files reviewed...” | “final code state shows policy classification before request construction...”  
  * Tests or evidence produced: PR-01 evidence includes `bg_resolve_route_policy.snapshot.json`, `bg_resolve_bodygraph_detail_proof.json`, `bg_resolve_runtime_nonclaims.json`, `bg_resolve_request_shape.snapshot.json`, `bg_resolve_policy_binding.snapshot.json`, and `route_policy_decision.log`. Repo → README HDE-EPIC036 overview lists PR-01 route-policy evidence paths  
  * Outcome: PF10 records PR-01 as a merged change with post-review fixes for partial-env base resolution, evidence index registration, and process credential preservation. PF10 — HDE-Build Notes → §2.2 PR-01 HDE-EPIC036 → “The first three automated review findings... were addressed...”  
  * Evidence pointer(s): Repo → `audit/qa/hde-epic036/route_policy_decision.log` → classification and nonclaim lines  
* PR-02 — evidence-loop binding:  
  * Purpose: bind PR-01 route-policy evidence into HDE-EPIC036 governed ledgers and acceptance/evidence posture.  
  * Key changes, high level: PR-02 introduced or updated `docs/acceptance_map_epic036.json`, token/evidence matrix, acceptance-map viability log, doc-delta candidate surfaces, Human Evidence Index, Machine Mirror, hash sentinels, and path proofs. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “The merged change binds already-landed PR-01... evidence into HDE-EPIC036 PR-02 evidence-loop surfaces.”  
  * Key surfaces touched: `docs/acceptance_map_epic036.json`, `audit/qa/hde-epic036/token_evidence_matrix.md`, `audit/qa/hde-epic036/acceptance_map_viability.log`, `audit/docdeltas/hde-epic036_doc_deltas.md`, `audit/qa/hde-epic036/00_meta/doc_deltas.md`, `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`, `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`, and `tools/evidence/update_evidence_index.py`. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “Expected PR-02 artifacts were found...”  
  * Tests or evidence produced: PR-02 artifact bundle records the acceptance map, viability log, doc deltas, QA-meta doc deltas, and token matrix with proof anchors, hashes, and token names. Artifact → PR-02 HDE-EPIC036 → Machine Mirror snippet → `epic036.pr02.acceptance_map` | `epic036.pr02.acceptance_map_viability` | `epic036.pr02.token_matrix`  
  * Outcome: PF10 records that a pre-merge validator issue was fixed by requiring the PR-02 token roster to equal the complete approved set rather than merely being a subset. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “the final merged file fixes it by requiring the PR-02 token roster to equal the complete approved set...”  
  * Evidence pointer(s): Repo → `docs/acceptance_map_epic036.json` → `acceptance_claims_mode`, nonclaims, selected route-policy classification, referenced paths, and token list  
* Conditional OPS-01 decision:  
  * Purpose: provide a PO-only live observation only if PR-01 could not truthfully classify the selected posture from closed-rails implementation evidence, current code, prior governed evidence, and repo-resident contract inventory. Artifact → Implementation Plan HDE-EPIC036 → OPS-01 intent → “only if PR-01 cannot truthfully classify...”  
  * Repo/PF10-recorded outcome: PR-01 and PR-02 evidence record OPS-01 as not required / not executed for this epic path. Repo → route-policy decision log → “OPS-01 not required by PR-01...” ; Repo → acceptance map → `executed_for_pr02:false` and `actual_ops01_evidence_found:false`  
  * Evidence pointer(s): Repo → `docs/acceptance_map_epic036.json`; Repo → `audit/qa/hde-epic036/route_policy_decision.log`.  
* Docs PR — final repo-docs sweep:  
  * Purpose: update public/developer repo docs to reflect HDE-EPIC036 route-policy and evidence-loop posture.  
  * Key changes, high level: PR \#337 updated seven docs files and merged into `main`. Repo → PR \#337 metadata → changed file count and merge commit  
  * Key surfaces touched: `README.md`, `CHANGELOG.md`, `AGENTS.md`, `docs/CLI_commands.md`, `docs/EVIDENCE_INDEX.md`, `docs/INDEX.md`, and `docs/RUN.md`. Repo → PR \#337 body line lists these files in the docs PR description.  
  * Tests or evidence produced: docs PR metadata reports `git diff --check`, `python tools/evidence/check_lf_endings.py`, and manual markdown sanity checks as passed. Repo → PR \#337 body → testing summary in body line  
  * Outcome: current README and docs index now identify HDE-EPIC036 as the current repo-docs sweep / current docs state. Repo → README title ; Repo → docs index title

Major surfaces affected

* CLI / BodyGraph resolver:  
  * `bg:resolve` remains the operator-facing CLI surface with `--source auto|db|vendor`, birth tuple fields, `--dry-run`, and `--upsert`. Repo → `engine/cli/main.py` → `bg:resolve` parser and arguments  
  * CLI resolver env now includes `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `HD_API_BASE_URL`, and `HDAPI_BASE_URL`. Repo → `engine/cli/main.py` → `_resolver_env`  
* Vendor seam / route policy:  
  * Route family auth posture is metadata-driven through `_ROUTE_CONTRACTS` and `route_auth_posture`. Repo → `engine/bodygraph/vendor_client.py` → route auth function  
  * Configured v2 base behavior is explicit unsupported-runtime nonclaim; non-v2 configured base behavior is explicit legacy fallback. Repo → `engine/bodygraph/vendor_client.py` → classification return branches  
* Resolver enforcement:  
  * Resolver computes route policy after rails checks and before vendor input normalization. Repo → `engine/bodygraph/resolver.py` → route policy classification and unsupported branch  
* Evidence / QA:  
  * PR-01 evidence artifacts live under `artifacts/vendor/hdapi_v2/` and `audit/qa/hde-epic036/`.  
  * PR-02 acceptance/evidence surfaces live under `docs/`, `audit/qa/hde-epic036/`, and `audit/docdeltas/`. Repo → `docs/acceptance_map_epic036.json` → referenced evidence paths  
* Docs:  
  * README, CHANGELOG, AGENTS, `docs/CLI_commands.md`, `docs/EVIDENCE_INDEX.md`, `docs/INDEX.md`, and `docs/RUN.md` now contain HDE-EPIC036 route-policy and evidence-loop posture. Repo → CHANGELOG HDE-EPIC036 entry ; Repo → docs RUN posture  
* OPS:  
  * OPS-01 was a conditional PO-only live observation in the plan, but repo evidence records it as not required by PR-01 and not executed for PR-02. Repo → route-policy decision log ; Repo → acceptance map

Evidence inventory (what exists)

* PR-01 route-policy decision log:  
  * `audit/qa/hde-epic036/route_policy_decision.log`  
  * Key facts: `selected_route_policy_classification=unsupported_runtime_nonclaim`; no configured-v2 legacy BodyGraph request; explicit legacy fallback only for non-v2 configured base; no public/API/AI/full-conformance claim; OPS-01 not required by PR-01. Repo → route-policy decision log  
* PR-01 governed JSON snapshots:  
  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`  
  * Evidence record excerpts in PR artifacts show these are registered as HDE-EPIC036 PR-01 route-policy records with `JSON_CANONICAL_CHECK_OK` and `EVIDENCE_PATH_PROOFS_OK` token names. Artifact → PR-02 HDE-EPIC036 → Machine Mirror excerpt → `hdapi_v2.bg_resolve_route_policy` | `hdapi_v2.bg_resolve_runtime_nonclaims`  
* PR-02 acceptance/evidence-loop surfaces:  
  * `docs/acceptance_map_epic036.json`  
  * `audit/qa/hde-epic036/token_evidence_matrix.md`  
  * `audit/qa/hde-epic036/acceptance_map_viability.log`  
  * `audit/docdeltas/hde-epic036_doc_deltas.md`  
  * `audit/qa/hde-epic036/00_meta/doc_deltas.md`  
  * Repo → `docs/acceptance_map_epic036.json` references each of these and records selected route-policy classification plus nonclaims  
* Evidence index / mirror:  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * Repo docs identify the Human Evidence Index and Machine Mirror as evidence skeleton homes. Repo → README Evidence & QA → evidence skeleton line  
* Tests / validation surfaces:  
  * `tests/bodygraph/test_bg_resolve_route_policy.py`  
  * `tests/bodygraph/test_vendor_client.py`  
  * `tests/bodygraph/test_resolver_vendor.py`  
  * `tests/cli/test_bg_resolve.py`  
  * `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`  
  * PF10 records targeted validation covering route-policy tests, evidence-loop tests, evidence generator checks, evidence index checks, orientation, mirror schema, evidence hash, py\_compile, LF endings, and diff hygiene. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → validation results.  
* Docs sweep:  
  * `README.md`  
  * `CHANGELOG.md`  
  * `AGENTS.md`  
  * `docs/CLI_commands.md`  
  * `docs/EVIDENCE_INDEX.md`  
  * `docs/INDEX.md`  
  * `docs/RUN.md`  
  * Repo → PR \#337 metadata → seven docs files changed

Evidence gaps

* Unknown: dedicated HDE-EPIC036 close-pack manifest / close report status.  
  * Why it matters: a Lead closure decision may require close-pack style evidence separate from implementation and evidence-loop binding.  
  * What would prove it: direct repo inspection showing `audit/EPIC-036_MANIFEST.json`, `audit/EPIC-036_close_report.md`, or another Lead-authorized close-pack artifact.  
  * Where that proof should exist, if known: likely under `audit/`, but no current repo search proof was collected in this report session, so this remains Unknown.  
* Unknown: whether PF09.5 has already been drained after PF10’s supportability recommendation.  
  * Why it matters: PF10 records HDE-FERM008.6 as supportable for status drainage, but repo docs say the docs sweep does not move PF09.5 status. Repo → README HDE-EPIC036 overview → “this docs sweep does not move PF09.5 status...”  
  * What would prove it: direct inspection of current phased PF09.5 text showing HDE-FERM008.6 status updated, or current PF10/drain memo explicitly recording the drainage.  
  * Where that proof should exist, if known: `docs/pfcanon/PF09.5-...` if repo-resident, or current in-session PF09.5 canon.  
* Unknown: whether PF05 has been permanently updated with the implemented `bg:resolve --source vendor` route-policy behavior.  
  * Why it matters: PF10 DDC and repo docs identify PF05 as the likely permanent CLI/vendor wording home.  
  * What would prove it: current PF05 section text explicitly documenting configured-v2 unsupported-runtime nonclaim and non-v2 explicit legacy fallback for `bg:resolve --source vendor`.  
  * Where that proof should exist, if known: PF05 — HDE CLI/API Vendor Ref.  
* Unknown: whether PF12 has been permanently updated with the `bg_resolve_*` evidence family.  
  * Why it matters: the evidence family is indexed and mirrored, but PF10/doc-delta candidates identified permanent Evidence Catalog prose as a possible drain target.  
  * What would prove it: current PF12 Evidence Catalog text naming the HDE-EPIC036 `bg_resolve_*` family.  
  * Where that proof should exist, if known: PF12 — HDE Schemas and Artifacts.  
* HDE-EPIC036 OPS-01 execution evidence was not found and is not expected from the inspected route-policy outcome.  
  * Why it matters: OPS work is PO-only, and no report should imply live vendor observation was performed for HDE-EPIC036.  
  * What would prove otherwise: current repo evidence under `audit/ops/hde-epic036/ops-01/` plus corresponding index/mirror entries.  
  * Where that proof should exist, if known: `audit/ops/hde-epic036/ops-01/`.  
  * Search method: searched Repo for `audit/ops/hde-epic036/ops-01` (case: sensitive); scope: repo code search; tool: GitHub.search; result: 1 hit, test-only reference in `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`, no actual OPS artifact path found.

Retrospective (Process)

What went well

* Scope stayed conservative and explicit: the Implementation Plan limited the epic to route-policy classification and evidence, excluding public Reader changes, new HTTP homes, app-side vendor calls, raw payload persistence, AI scope, and full HumanDesignAPI v2 runtime-conformance claims. Artifact → Implementation Plan HDE-EPIC036 → Brief recap of scope.  
* The plan anticipated conditional OPS only if closed-rails evidence could not classify the posture; later repo evidence recorded OPS-01 as not required by PR-01 and not executed for PR-02. Repo → route-policy decision log ; Repo → acceptance map  
* PR-01 kept route-policy behavior ahead of vendor request construction, which prevented the v2 configured-base / legacy `bodygraphs` route from becoming an implicit compatibility claim. Repo → vendor client classification  
* PR-01 review caught meaningful implementation issues before merge: partial-env base resolution, evidence-index registration, and process credential preservation. PF10 — HDE-Build Notes → §2.2 PR-01 HDE-EPIC036 → “The first three automated review findings... were addressed...”  
* PR-02 review caught a token-roster validator issue before the evidence loop was relied on as a durable binding; final PR-02 state required the complete approved token roster. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “the final merged file fixes it by requiring the PR-02 token roster to equal the complete approved set...”  
* Evidence stayed under closed rails and did not require live vendor observation for this route-policy classification. Repo → route-policy decision log → “OPS-01 not required...”  
* The final docs sweep updated public and developer-facing documentation after implementation and evidence-loop binding, so repo-facing docs now reflect HDE-EPIC036 current behavior. Repo → README HDE-EPIC036 section ; Repo → CHANGELOG HDE-EPIC036 entry  
* The documentation sweep preserved prior-epic history while making HDE-EPIC036 current, avoiding a silent rewrite of HDE-EPIC035 context. Repo → README HDE-EPIC036 section followed by HDE-EPIC035 section

What did not go well

* Before implementation, the readiness audit found HDE-EPIC036-specific planned evidence roots and artifacts absent. This was expected before the epic work, but it meant PR-01/PR-02 had to create a full evidence family rather than only bind existing HDE-EPIC036 artifacts. Artifact → Implementation Audit Epic Plan HDE-EPIC036 → `Seed: Missing in repo` → “all seeded HDE-EPIC036 evidence roots and ledger artifacts.”  
* The first Implementation Plan review found that audit provenance had been embedded inside Codex-facing task sections, which made the plan less portable until revised. Artifact → review Implementation Plan HDE-EPIC036 → Review Summary → “REVISE AND RESUBMIT because the plan embeds `Prior read-only audit` provenance...”  
* PR-01 initially had multiple review findings: route-policy config-source handling, evidence-index registration, and credential/env preservation. PF10 — HDE-Build Notes → §2.2 PR-01 HDE-EPIC036 → “The first three automated review findings... were addressed...”  
* PR-02 initially allowed a subset of approved tokens in the evidence-index validator; review identified that a missing token could still pass the validator before the final fix. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “requiring the PR-02 token roster to equal the complete approved set, not merely be a subset.”  
* Evidence refreshes changed many older path-proof timestamps outside HDE-EPIC036, increasing review noise even where payload content was not the core epic work. PF10 — HDE-Build Notes → §2.2 PR-01 HDE-EPIC036 → “Evidence refresh regenerated many pre-existing path-proof timestamps outside HDE-EPIC036.”  
* GitHub workflow metadata did not provide independent workflow-run proof for the inspected merge commits. Repo → workflow runs → “workflow\_runs: \[\]”  
* The epic surfaced several closure-axis distinctions repeatedly: implementation, evidence-loop binding, PF09 drainage, PF-Canon drainage, PO closeout, and docs sweep were separate and easy to conflate without explicit wording. PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “Closure axes remain separate...”

What we learned (Process)

* Route-policy work needs explicit classification vocabulary early. The plan’s four-posture framing made later repo behavior and evidence review more deterministic. Artifact → Implementation Plan HDE-EPIC036 → Brief recap of scope → “v2 chart-backed BodyGraph resolution, explicit legacy fallback, dual-route policy, or unsupported-runtime nonclaim.”  
* Audit provenance can be useful for planning, but it must not become Codex-facing execution authority. The Implementation Plan review required removal of prior audit provenance from PR task context. Artifact → review Implementation Plan HDE-EPIC036 → REV-001 / REV-002 expected fixes.  
* Evidence generators need index/mirror registration in the same working slice, not afterthought registration. PR-01 review caught missing HDE-EPIC036 evidence registration and final PR-01 fixed it. PF10 — HDE-Build Notes → §2.2 PR-01 HDE-EPIC036 → “HDE-EPIC036 PR-01 evidence artifacts are registered...”  
* Token rosters should be exact when an artifact says “approved roster only.” PR-02 review showed that “no unsupported tokens” was weaker than “complete expected roster.” PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → token roster equality finding.  
* Conditional OPS should be decided by evidence need, not by habit. PR-01’s closed-rails repo evidence resolved the route-policy classification without live vendor observation. Repo → route-policy decision log  
* Docs sweeps should follow implementation/evidence work and should explicitly preserve no-claim boundaries. Repo → CHANGELOG HDE-EPIC036 entry preserves no QA PASS, OPS, PF09 movement, parent Done, closeout, runtime conformance, public surface, raw payload, and AI nonclaims  
* Current repo truth is the reliable way to validate docs claims. The docs PR itself used repo crossproofs for `pyproject.toml`, `engine/cli/main.py`, `engine/bodygraph/vendor_client.py`, and `engine/bodygraph/resolver.py`. Repo → PR \#337 body testing/crossproof statement  
* Status language requires discipline: evidence support, PF09 status drainage, parent task posture, and closure state remained separate throughout. Repo → `docs/acceptance_map_epic036.json` separates supported scope and not-completed scope

Retrospective (Application / System)

What we learned about the system itself

* `bg:resolve --source vendor` is a real operator-facing workflow with `--source auto|db|vendor`, `--birthdate`, `--birthtime`, and `--location` inputs. Repo → `engine/cli/main.py`  
* The vendor route family cannot be inferred safely from a configured base URL alone; route metadata remains needed for auth posture and request behavior. Repo → `route_auth_posture()` uses `_ROUTE_CONTRACTS` rather than raw URL string auth inference  
* Configured v2 bases are now explicitly treated as unsupported for legacy BodyGraph-detail resolution unless a future adapter proves otherwise. Repo → `engine/bodygraph/vendor_client.py` → v2 unsupported reason  
* Non-v2 bases preserve legacy BodyGraph fallback, but that fallback is now explicit rather than accidental. Repo → `engine/bodygraph/vendor_client.py` → explicit legacy fallback branch  
* Closed-rails refusal remains earlier than route-policy logic and external I/O. Repo → route-policy decision log and resolver sequence; resolver checks and route-policy rejection happen before vendor inputs/ingest in the shown flow  
* `charts/simple` evidence from earlier epics did not prove full BodyGraph-detail sufficiency for `bg:resolve`; HDE-EPIC036 preserved that as a nonclaim. Repo → route-policy decision log → `v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows=false`  
* Evidence-loop correctness depends on both Human Evidence Index and Machine Mirror; HDE-EPIC036 artifacts are not just local files but need ledger and path-proof binding. Repo → acceptance map referenced evidence paths include Index/Mirror/hash files  
* Docs are operationally important because `README.md`, `docs/CLI_commands.md`, `docs/EVIDENCE_INDEX.md`, `docs/INDEX.md`, and `docs/RUN.md` now carry the route-policy truth that prevents future misuse of `bg:resolve --source vendor`. Repo → CLI docs route-policy evidence posture

Known remaining risks / debt

* Should-fix — PF09.5 status drainage remains separate from repo evidence. Evidence: repo docs state HDE-FERM008.6 is supportable for later PF09.5 drainage but the docs sweep does not move PF09.5 status. Repo → README HDE-EPIC036 overview  
* Should-fix — PF05 permanent wording may not yet include the implemented `bg:resolve --source vendor` route-policy behavior. Evidence: PF10 DDC identifies PF05 as a canon-silence drain candidate for route-policy behavior; docs PR also names PF05 route-policy wording as follow-up. Repo → docs index scope boundary says PF05 route-policy wording remains PF-Canon follow-up  
* Should-fix — PF12 permanent catalog prose may not yet include the `bg_resolve_*` evidence family. Evidence: docs PR names PF12 `bg_resolve_*` catalog prose as PF-Canon follow-up. Repo → docs index scope boundary  
* Nice-to-have — evidence refresh tooling caused broad path-proof timestamp churn outside the narrow epic family. Evidence: PF10 PR-01 review finding records older path-proof refresh noise outside HDE-EPIC036.  
* Should-fix — close-pack / formal closure artifact status is Unknown in this report. Evidence: this report inspected implementation, PR, docs, and evidence-loop surfaces, but did not establish current `audit/EPIC-036_MANIFEST.json` or `audit/EPIC-036_close_report.md`. What would prove it: direct repo inspection of those paths or Lead-specified close-pack location.  
* Nice-to-have — GitHub workflow-run metadata was not available for the docs merge commit. Evidence: Repo → workflow runs → `workflow_runs: []`  
* Should-fix — permanent operator guide PF29 alignment is Unknown. Evidence: docs PR updated repo docs, but PF29 was not shown drained in the inspected sources. What would prove it: current PF29 text reflecting HDE-EPIC036 route-policy behavior, if PF29 is deemed a drain home.  
* Nice-to-have — future developers may still confuse HDE-EPIC035 `charts/simple` open-rails evidence with HDE-EPIC036 BodyGraph-detail route-policy. Evidence: HDE-EPIC036 docs explicitly warn that `bg:resolve --source vendor` is not the canonical v2 chart/geokey validation path. Repo → docs index route-policy posture

Canon Alignment and Documentation Outcomes

5.1 Canon references used

* PF10 — HDE-Build Notes: used for latest explicit HDE-EPIC036 PR-01 and PR-02 historical outcomes, supportability posture, and closure-axis separation.  
* PF09.5 — HDE Build Checklist Fermentation: used for HDE-FERM008 / HDE-FERM008.6 mapping and Fermentation-phase interpretation. PF09.5 scope says Fermentation tracks work that captures live signal, support loops, and meaningful adaptation, while PF09 tasks cover dev/ops engagement including code, tests, runtime configuration, ops, or required runnable evidence. PF09.5 — HDE Build Checklist Fermentation, §0.1 Scope.  
* PF05 — HDE CLI/API Vendor Ref: used as the likely permanent home for CLI/vendor byte and behavior wording, including `bg:resolve --source vendor` route-policy behavior.  
* PF12 — HDE Schemas and Artifacts: used for Human Evidence Index, Machine Mirror, canonical JSON, path-proof, and evidence-family interpretation. PF12 owns Human Evidence Index at `docs/evidence/INDEX.json` and Machine Evidence Mirror at `artifacts/evidence_index.jsonl`, with strict parity and path-proof discipline.  
* PF04 — HDE Governance: used for rails, token, SAFE-rails, vendor HTTP, no-secret, and no-PII posture, and for interpreting token names as governance rather than mechanics.  
* PF06 — Epic Process Guide: used for PR/OPS separation, no direct PF-Canon edits by implementation agents, documentation drainage separation, and closure-axis separation.  
* PF07 — Glow Infrastructure: used for environment/config-key ownership and evidence/QA root posture in interpretation, not as proof of current repo content.  
* PF14 — HDE Mechanics Guide: used for mechanics/component interpretation and the rule that PF14 is not a token registry or planning authority.  
* PF19 — Glow QA Guide: used for QA posture and phased PF09 reference discipline, not for declaring QA PASS.  
* PF20 — HDE Phased Epics: not used as current planning or acceptance authority; if read later, it should be treated only as historical context.  
* PF23 — Reality Audits: not used as PR/review or closure proof authority in this report.

Closure Evidence Snapshot (for Lead decision)

6.1 Evidence produced

* PR-01 route-policy decision log:  
  * `audit/qa/hde-epic036/route_policy_decision.log`  
  * Evidence facts: `unsupported_runtime_nonclaim`, no configured-v2 `bodygraphs` request, explicit legacy fallback only for non-v2 configured bases, no full HDAPI v2 runtime conformance, no AI scope, and OPS-01 not required by PR-01. Repo → route-policy decision log  
* PR-01 route-policy JSON evidence:  
  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`  
  * Evidence facts: route-policy classification, BodyGraph-detail sufficiency nonclaim, runtime nonclaims, request-shape posture, and policy binding. Artifact → PR-02 HDE-EPIC036 → Machine Mirror excerpt → `hdapi_v2.bg_resolve_route_policy` | `hdapi_v2.bg_resolve_request_shape` | `hdapi_v2.bg_resolve_runtime_nonclaims`  
* PR-02 acceptance/evidence-loop evidence:  
  * `docs/acceptance_map_epic036.json`  
  * `audit/qa/hde-epic036/token_evidence_matrix.md`  
  * `audit/qa/hde-epic036/acceptance_map_viability.log`  
  * `audit/docdeltas/hde-epic036_doc_deltas.md`  
  * `audit/qa/hde-epic036/00_meta/doc_deltas.md`  
  * Evidence facts: route-policy classification remains `unsupported_runtime_nonclaim`, OPS-01 not executed, HDE-FERM008.6 route-policy/evidence-loop binding only, HDE-FERM008 parent Done not claimed, and no full runtime conformance. Repo → acceptance map  
* Evidence ledger surfaces:  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * Evidence facts: HDE-EPIC036 evidence paths are referenced in acceptance map and docs-side evidence navigation; Human Index / Machine Mirror coverage is documented. Repo → `docs/EVIDENCE_INDEX.md` HDE-EPIC036 navigation  
* Tests / validation surfaces:  
  * `tests/bodygraph/test_bg_resolve_route_policy.py`  
  * `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`  
  * `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`  
  * `tools/evidence/update_evidence_index.py`  
  * PF10 records targeted route-policy tests, PR-02 evidence-loop tests, generator checks, index/mirror/hash checks, LF check, py\_compile, and diff hygiene as validation evidence. PF10 — HDE-Build Notes → §2.2 PR-01 HDE-EPIC036 and §2.4 PR-02 HDE-EPIC036.  
* Docs sweep evidence:  
  * `README.md`  
  * `CHANGELOG.md`  
  * `AGENTS.md`  
  * `docs/CLI_commands.md`  
  * `docs/EVIDENCE_INDEX.md`  
  * `docs/INDEX.md`  
  * `docs/RUN.md`  
  * Evidence facts: HDE-EPIC036 docs now record route-policy posture, evidence anchors, supportability wording, and no-claim boundaries. Repo → README HDE-EPIC036 overview ; Repo → CHANGELOG HDE-EPIC036 entry  
* Token names referenced by HDE-EPIC036 evidence:  
  * `TESTS_PASS_OK`  
  * `DOC_DELTA_PRESENT_OK`  
  * `EVIDENCE_INDEX_UPDATED_OK`  
  * `MACHINE_MIRROR_UPDATED_OK`  
  * `EVIDENCE_INDEX_HASH_OK`  
  * `EVIDENCE_PATHS_VALIDATED_OK`  
  * `EVIDENCE_PATH_PROOFS_OK`  
  * `JSON_CANONICAL_CHECK_OK`  
  * `NO_EXTERNAL_IO_ON_REFUSAL_OK`  
  * `ENV_RAILS_POLICY_OK`  
  * Repo → acceptance map lists token names and evidence titles in `tokens`.

6.2 Evidence missing or ambiguous

* Close-pack evidence:  
  * What is missing: current proof of `audit/EPIC-036_MANIFEST.json`, `audit/EPIC-036_close_report.md`, or an equivalent Lead-authorized close-pack artifact was not established in this report.  
  * What would prove it: direct repo inspection showing those files or a current Lead-designated close-pack path with contents.  
  * Where that proof should exist, if known: likely under `audit/`, if the project follows prior close-pack path style.  
* PF09.5 drainage:  
  * What is missing: current proof that PF09.5 HDE-FERM008.6 status has been drained after PF10’s supportability recommendation.  
  * What would prove it: current PF09.5 text showing HDE-FERM008.6 status updated, or PF10/current drain artifact explicitly recording the status drainage.  
  * Where that proof should exist, if known: PF09.5 — HDE Build Checklist Fermentation or PF10 live addendum.  
* PF05 permanent route-policy wording:  
  * What is missing: current proof that PF05 now records the implemented `bg:resolve --source vendor` route-policy behavior.  
  * What would prove it: current PF05 text naming configured-v2 unsupported-runtime nonclaim and non-v2 explicit legacy fallback.  
  * Where that proof should exist, if known: PF05 — HDE CLI/API Vendor Ref.  
* PF12 evidence-family catalog wording:  
  * What is missing: current proof that PF12 permanently catalogs the HDE-EPIC036 `bg_resolve_*` evidence family.  
  * What would prove it: current PF12 Evidence Catalog text naming the `bg_resolve_*` family and HDE-EPIC036 evidence-loop surfaces.  
  * Where that proof should exist, if known: PF12 — HDE Schemas and Artifacts.  
* Production deployment:  
  * What is missing: this report did not inspect or receive proof of production deployment.  
  * What would prove it: deployment logs, release notes, environment metadata, or production artifact evidence naming HDE-EPIC036 behavior.  
  * Where that proof should exist, if known: Unknown from inspected sources.  
* HDE-EPIC036 live vendor observation:  
  * What is missing: actual HDE-EPIC036 OPS-01 live vendor evidence was not found and is not expected from the route-policy classification source set.  
  * What would prove it: files under `audit/ops/hde-epic036/ops-01/` plus index/mirror/path-proof binding.  
  * Where that proof should exist, if known: `audit/ops/hde-epic036/ops-01/`.  
  * Search method: searched Repo for `audit/ops/hde-epic036/ops-01` (case: sensitive); scope: repo code search; tool: GitHub.search; result: 1 hit, test-only reference in `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`, no actual OPS artifact path found.

6.3 Open closure items / questions for the Lead

* Does the Lead want to treat PF10’s HDE-FERM008.6 supportability record plus repo evidence as sufficient for PF09.5 status drainage? PF10 — HDE-Build Notes → §2.4 PR-02 HDE-EPIC036 → “HDE-FERM008.6 is supportable for status change to Done...” | Repo → acceptance map → HDE-FERM008.6 route-policy/evidence-loop binding only  
* Is a dedicated close-pack expected for HDE-EPIC036, and if so what repo path should hold it? Evidence needed: current close-pack manifest/report artifacts or Lead-specified close-pack source.  
* Should PF05 receive permanent route-policy wording for `bg:resolve --source vendor` now, or should PF10 remain the live interim home? PF10 DDC identifies PF05 as a canon-silence drain candidate for the implemented route-policy behavior.  
* Should PF12 receive permanent Evidence Catalog prose for the HDE-EPIC036 `bg_resolve_*` evidence family, or is Human Index / Machine Mirror discoverability sufficient for now? PF10 DDC identifies PF12 as a canon-silence drain candidate for permanent evidence-family prose.  
* Should PF29 / runnable operator guide be drained with HDE-EPIC036 route-policy usage wording? Current repo docs were updated, but PF29 alignment was not established in this report.  
* Does the Lead want any Reality Audit after this retrospective? PF23 is PO-only and not used here as a closure gate; any audit decision remains separate from this historical report.

  ## 2.6) Post Implementation Audit Triage HDE-EPIC035

Audit Summary

* The audit compares post-implementation repo reality against the HDE-EPIC036 plan posture for HDAPI v2 BodyGraph route-policy proof, route-family classification, evidence surfaces, component homes, endpoint placement, deterministic compute boundaries, vendor/DB seams, path casing, and root discipline.  
* Targeted repo cross-check was performed through current GitHub repo inspection against `glow-hdengine-v2` at commit `369e7b5e3fee05ef012a756241e160c691bb8a6b`.  
* 9 findings were mapped in audit order.  
* 0 findings are marked Must-act-now.  
* Top drift themes: presenter namespace ambiguity, CLI entrypoint versus auxiliary script ambiguity, split HTTP/adapter surface placement, multi-route reader file concentration, multi-root evidence interpretation, deterministic compute versus sanctioned I/O seams, vendor/DB seam placement, path-case conventions, and truth-home-like root proliferation.  
* Repo cross-check confirmed or partially confirmed the major audit themes, but narrowed them to already-classified PF canon posture rather than new PF doc-delta work.  
* No PF09.x, PF14, PF02, PF12, PF05, or PF20 doc delta proposals are needed.  
* PF doc homes consulted for classification: PF02 — HDE Architecture, PF05 — HDE CLI/API Vendor Ref, PF12 — HDE Schemas and Artifacts, and PF14 — HDE Mechanics Guide.

Repo Inspection Summary

observed repo root

glow-hdengine-v2

observed HEAD

369e7b5e3fee05ef012a756241e160c691bb8a6b

Repo: "pyproject.toml@369e7b5e3fee05ef012a756241e160c691bb8a6b" → "\[project.scripts\]" | "hdctl \= "engine.cli.main:cli""

branch or detached state

Audit Report states branch `work`; GitHub connector inspection used commit ref `369e7b5e3fee05ef012a756241e160c691bb8a6b`.

working tree status before analysis

Audit Report states: `Working tree cleanliness: git status --porcelain produced no changed-path output before branch output; working tree observed clean.` GitHub connector inspection was read-only and did not expose a mutable working tree.

repo inspection scope

Targeted repo inspection covered current repo metadata and current repo files or searches for `pyproject.toml`, `adapter/wsgi.py`, `adapter/http_reader.py`, `engine/http/compat_handler.py`, `engine/cli/main.py`, `scripts/hd_cli.py`, `engine/presenter/emitter.py`, `presenter/reader_v1/emitter.py`, `tools/evidence/update_evidence_index.py`, `audit/qa/hde-epic036/token_evidence_matrix.md`, `engine/sampler/core.py`, `engine/db/providers/bridge_provider.py`, `engine/bodygraph/vendor_client.py`, `.github/workflows/ci.yml`, `AGENTS.md`, `AcceptanceMap.md`, and `Run`.

repo commands or inspection methods used

GitHub repo metadata lookup, GitHub commit-ref file fetches, GitHub file-line fetches, bounded GitHub code search, and local read-only inspection of the attached Audit Report, Epic Plan, latest PF10, and task-relevant PF-Canon.

key repo cross-check outcomes

Repo cross-check confirmed the plan/audit surfaces needed for disposition: package discovery includes `engine*`, `adapter*`, and `presenter*`; the canonical CLI entrypoint is `engine.cli.main:cli`; app registration imports and mounts `reader_bp` and `compat_blueprint`; `/api/compat/v1` is implemented by `engine/http/compat_handler.py`; the Reader blueprint contains reader, aux narrative, ops DB, and diagnostic writer routes; Evidence Index and Machine Mirror paths are defined in `tools/evidence/update_evidence_index.py`; HDE-EPIC036 QA evidence exists under `audit/qa/hde-epic036/`; sampler code declares pure deterministic behavior; DB bridge and BodyGraph vendor code contain sanctioned I/O seams; mixed-case top-level files and lowercase QA roots coexist.

material audit findings contradicted or narrowed by Repo, if any

No material audit finding was contradicted. Repo inspection narrowed the findings to classification surfaces already governed by PF canon, so no doc delta is proposed.

working tree status after analysis, if commands were run

No local working tree was modified. GitHub connector inspection was read-only; no local repo commands were run.

Findings → Doc Delta Map

FND-001 —

Finding:

Presenter code exists in both root `presenter/` and `engine/presenter/`, but current architecture canon already distinguishes namespace split from serializer split.

Audit anchor:

Observed: Presenter code exists both as root presenter/ and as engine/presenter/.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: Presenter code exists both as root presenter/ and as engine/presenter/."

Epic Plan linkage:

The Epic Plan keeps existing public Reader behavior unchanged and does not introduce a new public Reader transport or payload surface.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "\* Backward-compat posture: Existing public Reader behavior remains unchanged by default. Legacy v1 BodyGraph behavior remains explicitly legacy behavior. HDAPI v2 work must not collapse v1 and v2 auth behavior, source-family identity, response mapping, or evidence posture into a generic vendor path."

Repo cross-check:

Repo confirms package discovery includes `presenter*` and `engine*`, and confirms both byte-authoritative engine presenter emission and root reader presenter wrapping.

Repo posture: Confirmed

Repo evidence pointer:

Repo: "pyproject.toml" → "include \= \["engine\*", "adapter\*", "presenter\*"\]"; Repo: "engine/presenter/emitter.py" → "def emit\_public(envelope: Dict\[str, Any\], \*, sort\_keys: bool \= True) \-\> bytes:"; Repo: "presenter/reader\_v1/emitter.py" → "def emit\_reader\_v1(enriched: Dict\[str, Any\]) \-\> Tuple\[bytes, Dict\[str, Any\]\]:"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF02 — HDE Architecture

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF02 owns architecture boundaries and component responsibility, and already classifies this namespace split. PF02 — HDE Architecture, §Routing (titles-only) → "\* **Presenter component home (names-only).** The presenter component is single-home by role and byte-authoritative emitter symbol, not by one literal repository path." | "\* **Namespace split without serializer split.** Wrapper envelope builders MAY live under top-level `presenter/`, while the byte-authoritative emitter entrypoint MAY live under `engine/presenter/`, provided all public-byte emission delegates to the same governed emitter path."

FND-002 —

Finding:

The CLI implementation lives under `engine/cli/` while additional CLI-like scripts exist under `scripts/`, but current CLI canon already anchors the shipped CLI to `engine.cli.main:cli`.

Audit anchor:

Observed: CLI implementation lives under engine/cli/, while additional CLI-like scripts exist under scripts/.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: CLI implementation lives under engine/cli/, while additional CLI-like scripts exist under scripts/."

Epic Plan linkage:

The Epic Plan keeps CLI public-output covenant and public Reader behavior unchanged by default.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "\* Backward-compat posture: Existing public Reader behavior remains unchanged by default. Legacy v1 BodyGraph behavior remains explicitly legacy behavior. HDAPI v2 work must not collapse v1 and v2 auth behavior, source-family identity, response mapping, or evidence posture into a generic vendor path."

Repo cross-check:

Repo confirms the package CLI entrypoint and confirms an auxiliary script under `scripts/`.

Repo posture: Confirmed

Repo evidence pointer:

Repo: "pyproject.toml" → "hdctl \= "engine.cli.main:cli""; Repo: "engine/cli/main.py" → "def cli(argv: list\[str\] | None \= None) \-\> int:"; Repo: "scripts/hd\_cli.py" → "import sys, argparse, json, os, hashlib, math, tempfile, pathlib, re"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF05 — HDE CLI/API Vendor Ref; PF02 — HDE Architecture

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF05 owns CLI/API contract posture and already defines the console entrypoint. PF05 — HDE CLI/API Vendor Ref, §3.1 Global flags & process contract → "`[project.scripts]` defines `hdctl = \"engine.cli.main:cli\"`." | "**Module-runner parity:** `python -m engine.cli --help` ≡ `hdctl --help` (exit 0)." PF02 — HDE Architecture, §3.8.2 QA entrypoints (concept-only) → "\* **CLI entrypoint wiring (repo surface; names-only).** `pyproject.toml` exposes `hdctl = engine.cli.main:cli`, `engine/cli/main.py` is the repo-local wiring surface, and `python -m engine.cli` is the module-runner surface over the same CLI entrypoint family for conjunction-oriented `showcompat` flows."

FND-003 —

Finding:

The compat HTTP route is implemented under `engine/http/compat_handler.py` while app mounting is in `adapter/wsgi.py`, but current architecture and endpoint canon already distinguish handler placement from adapter-owned HTTP mounting.

Audit anchor:

Observed: HTTP compat route is implemented under engine/http/compat\_handler.py, while app mounting lives in adapter/wsgi.py.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: HTTP compat route is implemented under engine/http/compat\_handler.py, while app mounting lives in adapter/wsgi.py."

Epic Plan linkage:

The Epic Plan states that no new public product surface is introduced.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "\* Contract changes / new surfaces: No new public product surface is introduced. The epic affects the internal HD Engine vendor-backed BodyGraph resolution policy for an existing operator-facing resolver workflow."

Repo cross-check:

Repo confirms the compat blueprint is defined in `engine/http/compat_handler.py` and mounted by `adapter/wsgi.py`.

Repo posture: Confirmed

Repo evidence pointer:

Repo: "engine/http/compat\_handler.py" → "compat\_blueprint \= Blueprint("compat", **name**, url\_prefix="/api/compat/v1")"; Repo: "adapter/wsgi.py" → "from engine.http.compat\_handler import compat\_blueprint" | "app.register\_blueprint(compat\_blueprint)"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF02 — HDE Architecture; PF05 — HDE CLI/API Vendor Ref; PF14 — HDE Mechanics Guide

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF02 owns HTTP-home architecture, PF05 owns Reader/compat API surface posture, and PF14 owns endpoint mechanics. Existing canon already distinguishes mounted HTTP family from handler package path. PF02 — HDE Architecture, §1.1 Single homes → "\* **Repo layout note (HTTP surfaces).** Single HTTP home means the adapter component owns route registration, guard rails, and surface mounting." | "Implementation may temporarily host some HTTP handlers in modules outside the `adapter/` directory, but Architecture still treats all HTTP entrypoints as belonging to the adapter component." PF05 — HDE CLI/API Vendor Ref, §5.6 Endpoint Catalog (JSON success) \[Required−Now\] → "\* Public Reader output and internal/admin compatibility output are distinct proof classes. Do not treat `/api/compat/v1` proof as public `/reader` proof, and do not treat `/reader` proof-surface status as internal/admin compat enablement." PF14 — HDE Mechanics Guide, §9.1 Endpoint Catalog (JSON success) \[Required-Now\] → "Endpoint-class authority note (normative). Endpoint class, A7-eligibility posture, and dev/internal scope are per-endpoint catalog facts."

FND-004 —

Finding:

The Reader blueprint concentrates reader, aux narrative, ops, and diagnostic routes in one file, but endpoint class is governed per endpoint and not inferred from file co-location.

Audit anchor:

Observed: Reader blueprint includes reader, aux narrative, ops, and writer/diagnostic routes in the same file.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: Reader blueprint includes reader, aux narrative, ops, and writer/diagnostic routes in the same file."

Epic Plan linkage:

The Epic Plan does not create a new public product surface and keeps existing public Reader behavior unchanged.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "\* Contract changes / new surfaces: No new public product surface is introduced. The epic affects the internal HD Engine vendor-backed BodyGraph resolution policy for an existing operator-facing resolver workflow."

Repo cross-check:

Repo confirms `adapter/http_reader.py` contains `/reader`, aux narrative, ops DB, and diagnostic writer routes.

Repo posture: Confirmed

Repo evidence pointer:

Repo: "adapter/http\_reader.py" → "@bp.get("/reader")"; Repo: "adapter/http\_reader.py" → "@bp.get("/api/aux/narrative")"; Repo: "adapter/http\_reader.py" → "@bp.route("/ops/db/unavailable", methods=\["GET"\])"; Repo: "adapter/http\_reader.py" → "@bp.route("/ops/writer/diagnostic", methods=\["POST"\], provide\_automatic\_options=False)"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF02 — HDE Architecture; PF14 — HDE Mechanics Guide; PF05 — HDE CLI/API Vendor Ref

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF02 owns surface-class distinction, PF14 owns endpoint-class mechanics, and PF05 owns endpoint catalog posture. Existing canon already prevents route class from being inferred solely by file co-location. PF02 — HDE Architecture, §3.8.2 QA entrypoints (concept-only) → "\* **Surface-class distinction (names-only).** Reader-like success surfaces, compat API surfaces (for example `/api/compat/v1`), and dev/internal harness surfaces may coexist inside one adapter-mounted HTTP family without collapsing into one proof class." PF14 — HDE Mechanics Guide, §9.1 Endpoint Catalog (JSON success) \[Required-Now\] → "Endpoint-class authority note (normative). Endpoint class, A7-eligibility posture, and dev/internal scope are per-endpoint catalog facts." PF05 — HDE CLI/API Vendor Ref, §5.6 Endpoint Catalog (JSON success) \[Required−Now\] → "\* The governed machine-readable inventory for this surface remains `docs/ENDPOINTS_CATALOG.json`; do not create a second inventory or designation carrier."

FND-005 —

Finding:

Evidence and proof outputs are spread across several governed and tooling roots, but PF12 already defines multi-root evidence as valid when bound through the Human Evidence Index, Machine Mirror, and path-proof discipline.

Audit anchor:

Observed: Evidence/proof outputs are spread across docs/, artifacts/, audit/, and additional roots such as catalog/, proofs/, reports/, goldens/, and validation/.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: Evidence/proof outputs are spread across docs/, artifacts/, audit/, and additional roots such as catalog/, proofs/, reports/, goldens/, and validation/."

Epic Plan linkage:

The Epic Plan binds HDE-EPIC036 evidence into PF12-governed Evidence Index and Machine Mirror surfaces.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "The route-policy, BodyGraph-detail proof or unsupported-runtime nonclaim, request-shape evidence, and policy-binding evidence are governed by HDE Schemas and Artifacts. Alternative homes for these proof families are not planned."

Repo cross-check:

Repo confirms canonical Evidence Index and Machine Mirror path constants and HDE-EPIC036 evidence under the QA root.

Repo posture: Confirmed

Repo evidence pointer:

Repo: "tools/evidence/update\_evidence\_index.py" → "HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json"" | "MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl""; Repo: "audit/qa/hde-epic036/token\_evidence\_matrix.md" → "epic\_id=HDE-EPIC036"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF12 — HDE Schemas and Artifacts

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF12 owns artifact families, governed evidence paths, Human Evidence Index, Machine Mirror, and path-proof discipline. Current PF12 already treats multi-root evidence as valid when bound by those mechanisms. PF12 — HDE Schemas and Artifacts, §0.2 Scope & single homes \[Required-Now\] → "\* Evidence artifacts MAY be stored across multiple governed roots. Single-home means the Human Evidence Index and Machine Evidence Mirror are the single authoritative bindings between artifact keys and repo paths, with one co-located `*.path_proof.txt` transcript per governed artifact." | "\* Evidence layout is evaluated by index, mirror, and path-proof completeness and coherence, plus same-PR coupling and path validation, not by whether files live in one directory."

FND-006 —

Finding:

Deterministic sampler/core code coexists with adjacent time/network/file I/O paths, but PF02/PF14 already distinguish deterministic compute from sanctioned operational seams.

Audit anchor:

Observed: Deterministic sampler/core paths coexist with time/network/file I/O paths in adjacent engine/adapter areas.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: Deterministic sampler/core paths coexist with time/network/file I/O paths in adjacent engine/adapter areas."

Epic Plan linkage:

The Epic Plan keeps public Reader behavior unchanged and requires route-policy evidence to preserve no-claim boundaries rather than collapsing all engine behavior into one proof class.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "\* Backward-compat posture: Existing public Reader behavior remains unchanged by default. Legacy v1 BodyGraph behavior remains explicitly legacy behavior. HDAPI v2 work must not collapse v1 and v2 auth behavior, source-family identity, response mapping, or evidence posture into a generic vendor path."

Repo cross-check:

Repo confirms sampler code declares no randomness/clocks/external state, while bridge and ingest paths use network/time and rails-gated vendor behavior.

Repo posture: Confirmed

Repo evidence pointer:

Repo: "engine/sampler/core.py" → "- No randomness, clocks, or external state are consulted."; Repo: "engine/db/providers/bridge\_provider.py" → "with urllib.request.urlopen(req, timeout=10) as resp:"; Repo: "engine/bodygraph/ingest.py" → "safe\_mode \= \_truthy(env.get("SAFE\_MODE"))" | "allow\_network \= \_truthy(env.get("ALLOW\_NETWORK"))"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF02 — HDE Architecture; PF14 — HDE Mechanics Guide

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF02 owns architecture seam classification and PF14 owns mechanics responsibilities. Current canon already allows BodyGraph vendor/DB I/O as a sanctioned seam while preserving pure-compute restrictions for deterministic compute modules. PF02 — HDE Architecture, §1.1 Single homes → "Purity rule (normative). Any module designated as deterministic compute (including sampler core and Engine Core modules) MUST be pure-compute: no time, network, file I/O, randomness, or environment reads at compute time; no import-time side effects." | "BodyGraph seam carve-out (normative). BodyGraph resolution and ingest MAY perform vendor and DB I/O through the DB abstraction as a sanctioned seam, including when implemented under `engine/bodygraph/`." PF14 — HDE Mechanics Guide, §HDAPI v2 vendor seam mechanics → "HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration."

FND-007 —

Finding:

The vendor seam and DB bridge network provider live under `engine/` subpackages, but current PF02/PF14 already classify these as sanctioned seams rather than proof of forbidden engine-wide impurity.

Audit anchor:

Observed: Vendor seam lives under engine/bodygraph/vendor\_client.py, and DB bridge network provider also lives under engine/db/providers/bridge\_provider.py.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: Vendor seam lives under engine/bodygraph/vendor\_client.py, and DB bridge network provider also lives under engine/db/providers/bridge\_provider.py."

Epic Plan linkage:

The Epic Plan frames the work as internal HD Engine vendor-backed BodyGraph resolution policy and does not create app-side vendor calls or new public product surfaces.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "\* Contract changes / new surfaces: No new public product surface is introduced. The epic affects the internal HD Engine vendor-backed BodyGraph resolution policy for an existing operator-facing resolver workflow."

Repo cross-check:

Repo confirms `HdApiClient` under `engine/bodygraph/vendor_client.py` and `BridgeProvider` under `engine/db/providers/bridge_provider.py`.

Repo posture: Confirmed

Repo evidence pointer:

Repo: "engine/bodygraph/vendor\_client.py" → "class HdApiClient:"; Repo: "engine/db/providers/bridge\_provider.py" → "class BridgeProvider:"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF02 — HDE Architecture; PF14 — HDE Mechanics Guide; PF05 — HDE CLI/API Vendor Ref

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF02 and PF14 own vendor/DB seam architecture and mechanics, while PF05 owns CLI/API/vendor contract posture. Current PF02 and PF14 already classify BodyGraph vendor and DB I/O seams under existing architecture boundaries. PF14 — HDE Mechanics Guide, §HDAPI v2 vendor seam mechanics → "HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration. That seam MUST route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through the existing architecture boundaries." PF02 — HDE Architecture, §1.1 Single homes → "BodyGraph seam carve-out (normative). BodyGraph resolution and ingest MAY perform vendor and DB I/O through the DB abstraction as a sanctioned seam, including when implemented under `engine/bodygraph/`."

FND-008 —

Finding:

Lowercase QA/evidence roots coexist with mixed-case top-level documentation/root files, but PF12 already distinguishes directory-case rails from filename-style and close-pack filename posture.

Audit anchor:

Observed: Most epic QA roots sampled are lowercase hyphenated paths such as audit/qa/hde-epic036; root/top-level includes mixed/uppercase files such as AGENTS.md, README.md, AcceptanceMap.md, CANON\_CHECKSUMS.json, and Run.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: Most epic QA roots sampled are lowercase hyphenated paths such as audit/qa/hde-epic036; root/top-level includes mixed/uppercase files such as AGENTS.md, README.md, AcceptanceMap.md, CANON\_CHECKSUMS.json, and Run."

Epic Plan linkage:

The Epic Plan requires lowercase ASCII naming for new epic-scoped directories.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "All new epic-scoped directories must use lowercase ASCII naming."

Repo cross-check:

Repo confirms mixed-case top-level files and lowercase HDE-EPIC036 QA evidence root.

Repo posture: Confirmed

Repo evidence pointer:

Repo: "AGENTS.md" → "\# AGENTS.md — Glow HD Engine (agent rules)"; Repo: "AcceptanceMap.md" → "\# EPIC-2 Acceptance Map (Mechanics & Stability)"; Repo: "Run" → "content:"; Repo: "audit/qa/hde-epic036/token\_evidence\_matrix.md" → "epic\_id=HDE-EPIC036"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF12 — HDE Schemas and Artifacts

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF12 owns governed artifact path and directory-name posture and already separates directory rules from filename casing. PF12 — HDE Schemas and Artifacts, §Directory naming (lower-case ASCII) → "All directory names in the repository and application codebase MUST use lower-case ASCII." | "\* This rail applies to directory names only. Filenames MAY contain uppercase characters unless separately forbidden by canon." | "\* Canon-defined close-pack filenames such as `audit/EPIC-030_MANIFEST.json` and `audit/EPIC-030_close_report.md` are not directory-case drift when every directory segment remains lowercase ASCII and the filename follows the governed close-pack pattern."

FND-009 —

Finding:

The audit observes many truth-home-like roots, but PF12 already classifies root proliferation as drift only when a root is treated as an independent authoritative evidence home outside PF12 catalog, Human Evidence Index, Machine Mirror, and path-proof discipline.

Audit anchor:

Observed: At least 16 truth-home-like roots were observed: audit/, artifacts/, docs/, tools/, scripts/, ci/, .github/, catalog/, schemas/, goldens/, fixtures/, proofs/, reports/, validation/, math/, config/.

Audit evidence pointer:

Post Implementation Audit HDE-EPIC036.md: "Observed: At least 16 truth-home-like roots were observed: audit/, artifacts/, docs/, tools/, scripts/, ci/, .github/, catalog/, schemas/, goldens/, fixtures/, proofs/, reports/, validation/, math/, config/."

Epic Plan linkage:

The Epic Plan states that alternative homes for route-policy proof families are not planned.

Epic Plan anchor:

Epic Plan HDE-EPIC036.md: "The route-policy, BodyGraph-detail proof or unsupported-runtime nonclaim, request-shape evidence, and policy-binding evidence are governed by HDE Schemas and Artifacts. Alternative homes for these proof families are not planned."

Repo cross-check:

Repo cross-check confirmed representative roots and the canonical index/mirror binding surfaces; a full directory listing was not needed to decide doc-delta disposition because PF12 classifies multi-root storage by index/mirror/path-proof authority rather than by root count alone.

Repo posture: Partially confirmed

Repo evidence pointer:

Repo: "tools/evidence/update\_evidence\_index.py" → "HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json"" | "MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl""; Repo: "audit/qa/hde-epic036/token\_evidence\_matrix.md" → "epic\_id=HDE-EPIC036"; Repo: ".github/workflows/ci.yml" → "name: ci"; Repo: "scripts/hd\_cli.py" → "import sys, argparse, json, os, hashlib, math, tempfile, pathlib, re"

Must-act-now: NO

Disposition: No doc delta needed

Correct home(s):

PF12 — HDE Schemas and Artifacts

PF09.x task delta: NO

PF09.x target: N/A

PF14 mechanics delta: NO

PF02 architecture delta: NO

Other PF doc delta(s): None

PF20 historical correction: NO

Existing issue duplicate: N/A

Why these are the correct homes:

PF12 owns evidence cataloging, evidence path bindings, and truth-home classification. Current PF12 already distinguishes multi-root storage from unauthorized truth homes. PF12 — HDE Schemas and Artifacts, §0.2 Scope & single homes \[Required-Now\] → "\* Root proliferation is drift only when a root is treated as an independent authoritative evidence home outside PF12 catalog, Human Index, Machine Mirror, and path-proof discipline." | "\* `tools/` and `scripts/` remain tooling and code roots by default. Outputs under those roots are non-governed unless explicitly cataloged as governed evidence outputs and bound by the Human Index, Machine Mirror, and path-proof discipline."

Doc Delta Proposals — PF09.x (Tasks)

None.

Final line

END OF AUDIT ANALYSIS

## 2.7) QA Pass 1 HDE-EPIC036

Review Summary

For QA\_STEP\_NAME `step-0b-doc-delta-capture / po-001 / po-002 / po-003 / po-004 / po-005 / po-006 / po-007 / po-008 / po-009`, Decision: PASS. Evidence pointer: Deliverables Report | Executive Summary | "- Overall result: `PASS` for all requested checks." | "- Check count: `10/10 PASS`" | "- Primary logs and sibling path proofs: present for all checks."

Live repo cross-check confirmed the material reported evidence is present on `main` in tracked repo locations, with no report/repo contradiction found for the checked artifacts. Evidence pointer: Repo | GitHub compare main...main | "status=identical" | "HEAD=369e7b5e3fee05ef012a756241e160c691bb8a6b" | "files=\[\]"

The top reason for the verdict is that every selected check reports `PASS`, `exit_code=0`, and required primary-log/path-proof evidence, and Repo validation confirmed the selected proof facts in current repo files. Evidence pointer: Repo | audit/qa/hde-epic036/00\_meta/hde\_epic036\_step0b\_po001\_po009\_action\_report.md | "| `step-0b-doc-delta-capture` | `PASS` | `0` | `2026-07-03T01:13:08Z` | `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log` |" | "| `po-009` | `PASS` | `0` | `2026-07-03T01:13:16Z` | `audit/qa/hde-epic036/checks/po-009/primary.log` |"

Findings

F-001

What you observed: Deliverables Report states all 10 requested checks passed and that primary logs plus sibling path proofs are present for all checks.

Evidence pointer: Deliverables Report | Executive Summary | "- Overall result: `PASS` for all requested checks." | "- Check count: `10/10 PASS`" | "- Primary logs and sibling path proofs: present for all checks."

Why it matters: The Live QA Plan requires check-scoped primary logs and sibling path proofs for the selected steps; this supports step-level closure for the requested scope.

Drives decision: Yes

F-002

What you observed: Repo validation confirmed the uploaded Deliverables Report is also present in the repo under the HDE-EPIC036 QA meta root, and it records the same scope, branch, and generated time.

Evidence pointer: Repo | audit/qa/hde-epic036/00\_meta/hde\_epic036\_step0b\_po001\_po009\_action\_report.md | "- Scope: `step-0b-doc-delta-capture`, `po-001` ... `po-009`" | "- Repo: `amthorn78/glow-hdengine-v2`" | "- Branch: `main`"

Why it matters: The report itself is repo-resident and mergeable, so the review can bind the uploaded Deliverables Report to current repo state.

Drives decision: Yes

F-003

What you observed: Step-0B produced the approved doc-delta surfaces, QA helper, primary log, and path proofs.

Evidence pointer: Deliverables Report | Check step-0b-doc-delta-capture | "- `audit/docdeltas/hde-epic036_doc_deltas.md`" | "- `audit/qa/hde-epic036/00_meta/doc_deltas.md`" | "- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py`"

Why it matters: Step-0B is the setup dependency for subsequent check-scoped execution and for governed doc-delta capture.

Drives decision: Yes

F-004

What you observed: PO-001 and PO-002 repo logs confirm configured-v2 route-policy refusal and explicit legacy-fallback separation.

Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-001/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.classification='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.error\_code='PROVIDER\_ROUTE\_UNSUPPORTED'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: configured\_v2\_bg\_resolve\_request\_shape='NO\_BODYGRAPHS\_REQUEST\_BUILT\_UNSUPPORTED\_RUNTIME\_NONCLAIM'"

Why it matters: These are the primary route-policy behavior checks for the epic; they confirm the plan-defined PASS predicates for refusing unsupported configured-v2 bg:resolve behavior before accidental legacy BodyGraph request construction.

Drives decision: Yes

F-005

What you observed: PO-003 through PO-005 repo logs confirm the BodyGraph-detail nonclaim, no v2-chart compatibility feed claim, and explicit non-v2 legacy fallback boundary.

Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-003/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: bodygraph\_detail\_sufficiency='UNSUPPORTED\_RUNTIME\_NONCLAIM'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: route\_family\_identity.v2\_chart\_candidate.bodygraph\_detail\_sufficiency='NOT\_CLAIMED'" | "TEXT\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: NO\_COMPLETE\_V2\_CHARTRESULT\_OR\_CHARTSIMPLERESULT\_TO\_BODYGRAPH\_PERSON\_CACHE\_ADAPTER\_FOUND\_IN\_INSPECTED\_LOCI"

Why it matters: These checks prevent overclaiming v2 chart success as full BodyGraph compatibility and preserve the approved implementation boundary.

Drives decision: Yes

F-006

What you observed: PO-006 and PO-009 repo logs confirm secret-safe and public/runtime/AI/raw-payload nonclaim posture.

Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-009/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.public\_reader\_change='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.full\_hdapi\_v2\_runtime\_conformance='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.ai\_scope='NONE'"

Why it matters: The selected QA scope explicitly excludes public product behavior, public transport expansion, raw payload persistence, app-side vendor credential ownership, full runtime conformance, and AI scope.

Drives decision: Yes

F-007

What you observed: PO-007 and PO-008 repo logs confirm source-of-truth separation and coherent evidence-set binding, including route-policy classification scope only.

Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK audit/qa/hde-epic036/route\_policy\_decision.log.path\_proof.txt sha256=a2469bbe0f7b8443cd3448af3454a98c88b230a51ac3e8c11f54380d9a066be9" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.selected\_classification='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.hde\_ferm008\_6\_completion\_role='Complete in this epic for route-policy classification only'"

Why it matters: The evidence remains bounded to route-policy classification and does not become status movement, OPS completion, QA PASS by implication, or closeout.

Drives decision: Yes

Repo Cross-Check

observed repo root: `amthorn78/glow-hdengine-v2`

observed HEAD: `369e7b5e3fee05ef012a756241e160c691bb8a6b`

branch or detached state: `main`

working tree status before review: Remote GitHub validation only; `main...main` comparison returned identical.

working tree status after review, if commands were run: Remote GitHub validation only; no mutating commands were run. Evidence pointer: Repo | GitHub compare main...main | "status=identical" | "ahead\_by=0" | "behind\_by=0"

repo validation commands or inspection methods used: GitHub.get\_repo; GitHub.compare\_commits base=`main` head=`main`; GitHub.fetch\_file for selected primary logs, action report, route-policy artifacts, and material evidence files; GitHub.search for path-proof existence spot-check.

deliverable paths checked: `audit/qa/hde-epic036/00_meta/hde_epic036_step0b_po001_po009_action_report.md`; `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`; `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`; `audit/qa/hde-epic036/checks/po-001/primary.log`; `audit/qa/hde-epic036/checks/po-002/primary.log`; `audit/qa/hde-epic036/checks/po-003/primary.log`; `audit/qa/hde-epic036/checks/po-004/primary.log`; `audit/qa/hde-epic036/checks/po-005/primary.log`; `audit/qa/hde-epic036/checks/po-006/primary.log`; `audit/qa/hde-epic036/checks/po-007/primary.log`; `audit/qa/hde-epic036/checks/po-008/primary.log`; `audit/qa/hde-epic036/checks/po-009/primary.log`; `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`; `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`; `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`.

tracked or mergeable evidence locations confirmed: Repo fetches from `main` confirm tracked presence for the checked primary logs, action report, and material artifacts. Evidence pointer: Repo | GitHub fetch\_file on main | "audit/qa/hde-epic036/checks/po-001/primary.log" | "audit/qa/hde-epic036/checks/po-009/primary.log" | "artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json"

reported evidence not found in repo, if any: None among checked material paths. Search method: searched Repo for "audit/qa/hde-epic036/checks/po-009/primary.log.path\_proof.txt" (case: sensitive); scope: "amthorn78/glow-hdengine-v2 on main"; tool: GitHub.search; result: 1 hit. Search method: searched Repo for "audit/qa/hde-epic036/00\_meta/hde\_epic036\_step0b\_po001\_po009\_action\_report.md" (case: sensitive); scope: "amthorn78/glow-hdengine-v2 on main"; tool: GitHub.fetch\_file; result: 1 hit.

repo/report contradictions, if any: None found for checked material paths. Search method: searched Deliverables Report for "Status: `PASS`" (case: sensitive); scope: "all check sections"; result: 10 hits. Search method: searched Repo for "status": "PASS"" (case: sensitive); scope: "selected primary logs on main"; tool: GitHub.fetch\_file/manual scan; result: 10 checked logs with PASS headers.

For each repo-checked artifact:

* Artifact path or label: `audit/qa/hde-epic036/00_meta/hde_epic036_step0b_po001_po009_action_report.md`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: No  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/00\_meta/hde\_epic036\_step0b\_po001\_po009\_action\_report.md | "- Overall result: `PASS` for all requested checks." | "- Check count: `10/10 PASS`" | "- Primary logs and sibling path proofs: present for all checks."  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log | "check\_id=step-0b-doc-delta-capture" | "DOC\_DELTA\_DRAFT=audit/docdeltas/hde-epic036\_doc\_deltas.md" | "QA\_HELPER=audit/qa/hde-epic036/00\_meta/hde036\_live\_qa\_harness.py"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path\_proof.txt | "path: audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log" | "size\_bytes: 1674" | "sha256: db45e1cb6b03349fe5a6f7b87aa7b2ec7ec99995c96cd9e2e5f77aaa8d726d06"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-001/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-001/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.classification='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.error\_code='PROVIDER\_ROUTE\_UNSUPPORTED'" | "TEXT\_OK tests/bodygraph/test\_bg\_resolve\_route\_policy.py :: assert calls \== \[\]"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-002/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-002/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: selected\_posture='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: supported\_postures.explicit\_legacy\_fallback='PRESERVED\_ONLY\_FOR\_NON\_V2\_CONFIGURED\_BASE'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: explicit\_legacy\_fallback=PRESERVED\_ONLY\_FOR\_NON\_V2\_CONFIGURED\_BASE"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-003/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-003/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: bodygraph\_detail\_sufficiency='UNSUPPORTED\_RUNTIME\_NONCLAIM'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: route\_family\_identity.v2\_chart\_candidate.bodygraph\_detail\_sufficiency='NOT\_CLAIMED'" | "TEXT\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: ChartSimpleResult"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-004/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-004/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: v2\_chart\_data\_feeds\_existing\_bodygraph\_cache\_person\_compat\_flows=False" | "JSON\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: normalized\_data\_path\_proof\_claim='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: schema\_gap\_status='GAP\_RECORDED'"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-005/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-005/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: legacy\_fallback\_policy.classification='explicit\_legacy\_fallback'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: legacy\_fallback\_policy.configured\_base\_version='v1'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.supported=False"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-006/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-006/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.raw\_payload\_persistence='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: raw\_response\_body\_persisted=False" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: raw\_vendor\_payload\_persisted=False"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-007/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-007/primary.log | "JSON\_LIST\_OK docs/acceptance\_map\_epic036.json :: nonclaims contains 'QA PASS'" | "JSON\_LIST\_OK docs/acceptance\_map\_epic036.json :: nonclaims contains 'PF09 status movement'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence."  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-008/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json.path\_proof.txt sha256=c7ac108a5171aa10c0fe32d54fda81aa0a0712495ceb6ebd5dbecd25bf3271d5" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.selected\_classification='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.hde\_ferm008\_6\_completion\_role='Complete in this epic for route-policy classification only'"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `audit/qa/hde-epic036/checks/po-009/primary.log`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-009/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.public\_reader\_change='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.full\_hdapi\_v2\_runtime\_conformance='NONE'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: no\_ai\_scope=true"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json | "content: {"artifact\_kind":"bg\_resolve\_route\_policy","configured\_v2\_policy":{"classification":"unsupported\_runtime\_nonclaim"" | ""error\_code":"PROVIDER\_ROUTE\_UNSUPPORTED"" | ""selected\_posture":"unsupported\_runtime\_nonclaim""  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json | "content: {"artifact\_kind":"bg\_resolve\_request\_shape","configured\_v2\_bg\_resolve\_request\_shape":"NO\_BODYGRAPHS\_REQUEST\_BUILT\_UNSUPPORTED\_RUNTIME\_NONCLAIM"" | ""raw\_request\_body\_persisted":false" | ""raw\_vendor\_payload\_persisted":false"  
* Negative-claim proof, if Present in repo \= No: N/A  
* Artifact path or label: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* Reported by Deliverables Report: Yes  
* Required by Plan/Caveats: Yes  
* Present in repo: Yes  
* Tracked or mergeable: Yes  
* Allowed root: Yes  
* Content/proof facts checked: Yes  
* Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json | "content: {"adapter\_sufficiency":"NO\_COMPLETE\_V2\_CHARTRESULT\_OR\_CHARTSIMPLERESULT\_TO\_BODYGRAPH\_PERSON\_CACHE\_ADAPTER\_FOUND\_IN\_INSPECTED\_LOCI"" | ""bodygraph\_detail\_sufficiency":"UNSUPPORTED\_RUNTIME\_NONCLAIM"" | ""v2\_chart\_data\_feeds\_existing\_bodygraph\_cache\_person\_compat\_flows":false"  
* Negative-claim proof, if Present in repo \= No: N/A

Evidence Print

A) Required deliverables checklist

* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK step-0b-doc-delta-capture Required deliverables | "\* `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log | "check\_id=step-0b-doc-delta-capture" | "DOC\_DELTA\_DRAFT=audit/docdeltas/hde-epic036\_doc\_deltas.md" | "QA\_HELPER=audit/qa/hde-epic036/00\_meta/hde036\_live\_qa\_harness.py"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK step-0b-doc-delta-capture Required deliverables | "\* `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path\_proof.txt | "path: audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log" | "size\_bytes: 1674" | "sha256: db45e1cb6b03349fe5a6f7b87aa7b2ec7ec99995c96cd9e2e5f77aaa8d726d06"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/docdeltas/hde-epic036_doc_deltas.md`  
* Evidence pointer for requirement: Live QA Plan | CHECK step-0b-doc-delta-capture Required deliverables | "\* `audit/docdeltas/hde-epic036_doc_deltas.md`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/docdeltas/hde-epic036_doc_deltas.md`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Check step-0b-doc-delta-capture | "- `audit/docdeltas/hde-epic036_doc_deltas.md`" | "- `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`" | "- `audit/qa/hde-epic036/00_meta/doc_deltas.md`"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK step-0b-doc-delta-capture Required deliverables | "\* `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/docdeltas/hde-epic036_doc_deltas.md` (exists=`True`)" | "- `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt` (exists=`True`)" | "- `audit/qa/hde-epic036/00_meta/doc_deltas.md` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/00_meta/doc_deltas.md`  
* Evidence pointer for requirement: Live QA Plan | CHECK step-0b-doc-delta-capture Required deliverables | "\* `audit/qa/hde-epic036/00_meta/doc_deltas.md`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/00_meta/doc_deltas.md`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Additional Step-0B Deliverables | "- `audit/docdeltas/hde-epic036_doc_deltas.md` (exists=`True`)" | "- `audit/qa/hde-epic036/00_meta/doc_deltas.md` (exists=`True`)" | "- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK step-0b-doc-delta-capture Required deliverables | "\* `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Additional Step-0B Deliverables | "- `audit/qa/hde-epic036/00_meta/doc_deltas.md` (exists=`True`)" | "- `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt` (exists=`True`)" | "- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py`  
* Evidence pointer for requirement: Live QA Plan | CHECK step-0b-doc-delta-capture Required deliverables | "\* `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Additional Step-0B Deliverables | "- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` (exists=`True`)" | "- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK step-0b-doc-delta-capture Required deliverables | "\* `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Additional Step-0B Deliverables | "- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` (exists=`True`)" | "- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-001/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-001 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-001/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-001/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-001/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.classification='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: configured\_v2\_bg\_resolve\_request\_shape='NO\_BODYGRAPHS\_REQUEST\_BUILT\_UNSUPPORTED\_RUNTIME\_NONCLAIM'" | "TEXT\_OK tests/bodygraph/test\_bg\_resolve\_route\_policy.py :: assert calls \== \[\]"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-001 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-001/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-001 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json | "content: {"artifact\_kind":"bg\_resolve\_route\_policy","configured\_v2\_policy":{"classification":"unsupported\_runtime\_nonclaim"" | ""error\_code":"PROVIDER\_ROUTE\_UNSUPPORTED"" | ""selected\_posture":"unsupported\_runtime\_nonclaim""  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-001 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json | "content: {"artifact\_kind":"bg\_resolve\_request\_shape","configured\_v2\_bg\_resolve\_request\_shape":"NO\_BODYGRAPHS\_REQUEST\_BUILT\_UNSUPPORTED\_RUNTIME\_NONCLAIM"" | ""raw\_request\_body\_persisted":false" | ""raw\_vendor\_payload\_persisted":false"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `tests/bodygraph/test_bg_resolve_route_policy.py`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-001 Required deliverables | "\* `tests/bodygraph/test_bg_resolve_route_policy.py`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `tests/bodygraph/test_bg_resolve_route_policy.py`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-001/primary.log | "FILE\_OK tests/bodygraph/test\_bg\_resolve\_route\_policy.py sha256=d9a8219e1a2dd54ca1e63a5d1d871ce4eee291e6bd9770206733f1df260e9803" | "TEXT\_OK tests/bodygraph/test\_bg\_resolve\_route\_policy.py :: assert calls \== \[\]"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-002/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-002 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-002/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-002/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-002/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: selected\_posture='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: supported\_postures.explicit\_legacy\_fallback='PRESERVED\_ONLY\_FOR\_NON\_V2\_CONFIGURED\_BASE'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: explicit\_legacy\_fallback=PRESERVED\_ONLY\_FOR\_NON\_V2\_CONFIGURED\_BASE"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-002/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-002 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-002/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-002/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-002/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-002/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-002 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-002/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json sha256=fee2f82ebf247a2a6e39e1211782d38085a7ac78796ff78bcc24d223680ec410" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: selected\_posture='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: legacy\_fallback\_policy.classification='explicit\_legacy\_fallback'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/route_policy_decision.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-002 Required deliverables | "\* `audit/qa/hde-epic036/route_policy_decision.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/route_policy_decision.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-002/primary.log | "FILE\_OK audit/qa/hde-epic036/route\_policy\_decision.log sha256=02ea41e97558edc9f0975b4a6261987ea1c31738286b59861837a3823b609409" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: explicit\_legacy\_fallback=PRESERVED\_ONLY\_FOR\_NON\_V2\_CONFIGURED\_BASE"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-003/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-003 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-003/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-003/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-003/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: bodygraph\_detail\_sufficiency='UNSUPPORTED\_RUNTIME\_NONCLAIM'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: route\_family\_identity.v2\_chart\_candidate.bodygraph\_detail\_sufficiency='NOT\_CLAIMED'" | "TEXT\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: ChartSimpleResult"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-003/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-003 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-003/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-003/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-003/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-003/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-003 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json | "content: {"adapter\_sufficiency":"NO\_COMPLETE\_V2\_CHARTRESULT\_OR\_CHARTSIMPLERESULT\_TO\_BODYGRAPH\_PERSON\_CACHE\_ADAPTER\_FOUND\_IN\_INSPECTED\_LOCI"" | ""bodygraph\_detail\_sufficiency":"UNSUPPORTED\_RUNTIME\_NONCLAIM"" | ""v2\_chart\_data\_feeds\_existing\_bodygraph\_cache\_person\_compat\_flows":false"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-003 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-003/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json sha256=fee2f82ebf247a2a6e39e1211782d38085a7ac78796ff78bcc24d223680ec410" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: route\_family\_identity.v2\_chart\_candidate.bodygraph\_detail\_sufficiency='NOT\_CLAIMED'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-003 Required deliverables | "\* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-003/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json sha256=b7ee708ad8a3b35c4b402d9304040ce55498c783a356c08ea3613c017b8a7a23" | "TEXT\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: ChartSimpleResult"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-004/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-004 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-004/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-004/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-004/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: v2\_chart\_data\_feeds\_existing\_bodygraph\_cache\_person\_compat\_flows=False" | "JSON\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: normalized\_data\_path\_proof\_claim='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: schema\_gap\_status='GAP\_RECORDED'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-004/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-004 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-004/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-004/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-004/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-004/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-004 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-004/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json sha256=61a23685a75c9b6d53ee3e73d73c466ddad8c8f5b3bd0040b12d350571748f83" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: v2\_chart\_data\_feeds\_existing\_bodygraph\_cache\_person\_compat\_flows=False"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-004 Required deliverables | "\* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-004/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json sha256=b7ee708ad8a3b35c4b402d9304040ce55498c783a356c08ea3613c017b8a7a23" | "JSON\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: normalized\_data\_path\_proof\_claim='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: schema\_gap\_status='GAP\_RECORDED'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-005/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-005 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-005/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-005/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-005/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: legacy\_fallback\_policy.classification='explicit\_legacy\_fallback'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: legacy\_fallback\_policy.configured\_base\_version='v1'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.supported=False"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-005/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-005 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-005/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-005/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-005/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-005/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-005 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-005/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json sha256=fee2f82ebf247a2a6e39e1211782d38085a7ac78796ff78bcc24d223680ec410" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: legacy\_fallback\_policy.classification='explicit\_legacy\_fallback'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.supported=False"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `tests/bodygraph/test_bg_resolve_route_policy.py`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-005 Required deliverables | "\* `tests/bodygraph/test_bg_resolve_route_policy.py`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `tests/bodygraph/test_bg_resolve_route_policy.py`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-005/primary.log | "FILE\_OK tests/bodygraph/test\_bg\_resolve\_route\_policy.py sha256=d9a8219e1a2dd54ca1e63a5d1d871ce4eee291e6bd9770206733f1df260e9803" | "TEXT\_OK tests/bodygraph/test\_bg\_resolve\_route\_policy.py :: test\_explicit\_legacy\_fallback\_remains\_available\_for\_non\_v2\_configured\_base"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-006/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-006 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-006/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-006/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-006/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.raw\_payload\_persistence='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: raw\_response\_body\_persisted=False" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: raw\_vendor\_payload\_persisted=False"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-006/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-006 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-006/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-006/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-006/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-006/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-006 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-006/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json sha256=7c85c96654dfd2c82d6d5f1cdcdde53d46264c6248fc5f91896af95e83c15752" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.raw\_payload\_persistence='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.app\_side\_humandesignapi\_credential\_ownership='NONE'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-006 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-006/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json sha256=8e27ac55371cb2b1ed1edbef5c0b0ff66e71ccd1c71e73ef2f9396fe98ae4e56" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: raw\_request\_body\_persisted=False" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: raw\_vendor\_payload\_persisted=False"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-007/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-007 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-007/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-007/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-007/primary.log | "JSON\_LIST\_OK docs/acceptance\_map\_epic036.json :: nonclaims contains 'QA PASS'" | "JSON\_LIST\_OK docs/acceptance\_map\_epic036.json :: nonclaims contains 'HDE-FERM008 parent Done'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence."  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-007/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-007 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-007/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-007/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-007/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-007/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `docs/acceptance_map_epic036.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-007 Required deliverables | "\* `docs/acceptance_map_epic036.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `docs/acceptance_map_epic036.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-007/primary.log | "FILE\_OK docs/acceptance\_map\_epic036.json sha256=c92c1ed76c93066612b8807e5384aed0fd7ebf999619cdd34ce5d9078fb189f6" | "JSON\_LIST\_OK docs/acceptance\_map\_epic036.json :: nonclaims contains 'QA PASS'" | "JSON\_LIST\_OK docs/acceptance\_map\_epic036.json :: nonclaims contains 'epic closeout'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-007 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-007/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json sha256=3439dee7e7bc929e7d612929d3b594bd3f8564dff3e16541410cdd67f8d5bac4" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.ops\_01\_requirement='OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence.'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/route_policy_decision.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-007 Required deliverables | "\* `audit/qa/hde-epic036/route_policy_decision.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/route_policy_decision.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-007/primary.log | "FILE\_OK audit/qa/hde-epic036/route\_policy\_decision.log sha256=02ea41e97558edc9f0975b4a6261987ea1c31738286b59861837a3823b609409" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence."  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-008/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-008/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-008/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json.path\_proof.txt sha256=c7ac108a5171aa10c0fe32d54fda81aa0a0712495ceb6ebd5dbecd25bf3271d5" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.selected\_classification='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.hde\_ferm008\_6\_completion\_role='Complete in this epic for route-policy classification only'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-008/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-008/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-008/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-008/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-008/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json sha256=fee2f82ebf247a2a6e39e1211782d38085a7ac78796ff78bcc24d223680ec410" | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json.path\_proof.txt sha256=c7ac108a5171aa10c0fe32d54fda81aa0a0712495ceb6ebd5dbecd25bf3271d5"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json.path\_proof.txt sha256=c7ac108a5171aa10c0fe32d54fda81aa0a0712495ceb6ebd5dbecd25bf3271d5"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json sha256=61a23685a75c9b6d53ee3e73d73c466ddad8c8f5b3bd0040b12d350571748f83" | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json.path\_proof.txt sha256=3ab6833447003278a77a81da71abc866bf4333b0dcb53dcbb2024b737a39350b"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json.path\_proof.txt sha256=3ab6833447003278a77a81da71abc866bf4333b0dcb53dcbb2024b737a39350b"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json sha256=7c85c96654dfd2c82d6d5f1cdcdde53d46264c6248fc5f91896af95e83c15752" | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json.path\_proof.txt sha256=c9bd1834537b6dfa4ef704d2ecc940f7e0e919b8669040f5acf3ecaca5564969"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json.path\_proof.txt sha256=c9bd1834537b6dfa4ef704d2ecc940f7e0e919b8669040f5acf3ecaca5564969"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json sha256=8e27ac55371cb2b1ed1edbef5c0b0ff66e71ccd1c71e73ef2f9396fe98ae4e56" | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json.path\_proof.txt sha256=e355c31a547e3a06ec4dee9b4b7606d14870e246acad07bab5221d18fd6eef03"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json.path\_proof.txt sha256=e355c31a547e3a06ec4dee9b4b7606d14870e246acad07bab5221d18fd6eef03"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json sha256=3439dee7e7bc929e7d612929d3b594bd3f8564dff3e16541410cdd67f8d5bac4" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.selected\_classification='unsupported\_runtime\_nonclaim'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json.path\_proof.txt sha256=6e1f299d237a2c8a17f50f1c25f0162be80a031832c213bc827cd355716bafe6"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/route_policy_decision.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `audit/qa/hde-epic036/route_policy_decision.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/route_policy_decision.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK audit/qa/hde-epic036/route\_policy\_decision.log sha256=02ea41e97558edc9f0975b4a6261987ea1c31738286b59861837a3823b609409" | "FILE\_OK audit/qa/hde-epic036/route\_policy\_decision.log.path\_proof.txt sha256=a2469bbe0f7b8443cd3448af3454a98c88b230a51ac3e8c11f54380d9a066be9"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-008 Required deliverables | "\* `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK audit/qa/hde-epic036/route\_policy\_decision.log.path\_proof.txt sha256=a2469bbe0f7b8443cd3448af3454a98c88b230a51ac3e8c11f54380d9a066be9"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-009/primary.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-009 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-009/primary.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-009/primary.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-009/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.public\_reader\_change='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.full\_hdapi\_v2\_runtime\_conformance='NONE'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: no\_full\_hdapi\_v2\_runtime\_conformance=true"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/checks/po-009/primary.log.path_proof.txt`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-009 Required deliverables | "\* `audit/qa/hde-epic036/checks/po-009/primary.log.path_proof.txt`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/checks/po-009/primary.log.path_proof.txt`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Deliverables Report | Consolidated Evidence Outputs | "- `audit/qa/hde-epic036/checks/po-009/primary.log` (exists=`True`)" | "- `audit/qa/hde-epic036/checks/po-009/primary.log.path_proof.txt` (exists=`True`)"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-009 Required deliverables | "\* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-009/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json sha256=7c85c96654dfd2c82d6d5f1cdcdde53d46264c6248fc5f91896af95e83c15752" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.public\_reader\_change='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.ai\_scope='NONE'"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `docs/acceptance_map_epic036.json`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-009 Required deliverables | "\* `docs/acceptance_map_epic036.json`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `docs/acceptance_map_epic036.json`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-009/primary.log | "FILE\_OK docs/acceptance\_map\_epic036.json sha256=c92c1ed76c93066612b8807e5384aed0fd7ebf999619cdd34ce5d9078fb189f6"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None  
* Deliverable name/label, quoted from Plan/Caveats: `audit/qa/hde-epic036/route_policy_decision.log`  
* Evidence pointer for requirement: Live QA Plan | CHECK po-009 Required deliverables | "\* `audit/qa/hde-epic036/route_policy_decision.log`"  
* Expected path, from Plan/Caveats if specified, otherwise exactly: `audit/qa/hde-epic036/route_policy_decision.log`  
* Present in Deliverables Report: Yes  
* Present in live repo when repo-resident: Yes  
* Tracked or mergeable when repo-resident: Yes  
* Evidence pointer showing presence, or if missing, negative-claim proof plus the word Missing: Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-009/primary.log | "FILE\_OK audit/qa/hde-epic036/route\_policy\_decision.log sha256=02ea41e97558edc9f0975b4a6261987ea1c31738286b59861837a3823b609409" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: no\_ai\_scope=true" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: no\_full\_hdapi\_v2\_runtime\_conformance=true"  
* Alternate proof available: N/A  
* Alternate proof pointer(s) or None: None

B) Evidence artifacts relied on

* Path/label, exact as listed in Deliverables Report or live repo validation: `hde_epic036_step0b_po001_po009_action_report.md`  
* Evidence pointer: Deliverables Report | Executive Summary | "- Overall result: `PASS` for all requested checks." | "- Check count: `10/10 PASS`" | "- Primary logs and sibling path proofs: present for all checks."  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `PASS for all requested checks`; `10/10 PASS`; `Primary logs and sibling path proofs: present for all checks`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log | "check\_id=step-0b-doc-delta-capture" | "DOC\_DELTA\_DRAFT=audit/docdeltas/hde-epic036\_doc\_deltas.md" | "QA\_HELPER=audit/qa/hde-epic036/00\_meta/hde036\_live\_qa\_harness.py"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `check_id=step-0b-doc-delta-capture`; `DOC_DELTA_DRAFT`; `QA_HELPER`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-001/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-001/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.classification='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.error\_code='PROVIDER\_ROUTE\_UNSUPPORTED'" | "TEXT\_OK tests/bodygraph/test\_bg\_resolve\_route\_policy.py :: assert calls \== \[\]"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `unsupported_runtime_nonclaim`; `PROVIDER_ROUTE_UNSUPPORTED`; `assert calls == []`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-002/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-002/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: selected\_posture='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: supported\_postures.explicit\_legacy\_fallback='PRESERVED\_ONLY\_FOR\_NON\_V2\_CONFIGURED\_BASE'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: explicit\_legacy\_fallback=PRESERVED\_ONLY\_FOR\_NON\_V2\_CONFIGURED\_BASE"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `selected_posture='unsupported_runtime_nonclaim'`; `explicit_legacy_fallback`; `PRESERVED_ONLY_FOR_NON_V2_CONFIGURED_BASE`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-003/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-003/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: bodygraph\_detail\_sufficiency='UNSUPPORTED\_RUNTIME\_NONCLAIM'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: route\_family\_identity.v2\_chart\_candidate.bodygraph\_detail\_sufficiency='NOT\_CLAIMED'" | "TEXT\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: ChartSimpleResult"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `UNSUPPORTED_RUNTIME_NONCLAIM`; `NOT_CLAIMED`; `ChartSimpleResult`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-004/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-004/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json :: v2\_chart\_data\_feeds\_existing\_bodygraph\_cache\_person\_compat\_flows=False" | "JSON\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: normalized\_data\_path\_proof\_claim='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json :: schema\_gap\_status='GAP\_RECORDED'"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows=False`; `normalized_data_path_proof_claim='NONE'`; `schema_gap_status='GAP_RECORDED'`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-005/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-005/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: legacy\_fallback\_policy.classification='explicit\_legacy\_fallback'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: legacy\_fallback\_policy.configured\_base\_version='v1'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json :: configured\_v2\_policy.supported=False"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `explicit_legacy_fallback`; `configured_base_version='v1'`; `configured_v2_policy.supported=False`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-006/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-006/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.raw\_payload\_persistence='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: raw\_response\_body\_persisted=False" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json :: raw\_vendor\_payload\_persisted=False"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `raw_payload_persistence='NONE'`; `raw_response_body_persisted=False`; `raw_vendor_payload_persisted=False`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-007/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-007/primary.log | "JSON\_LIST\_OK docs/acceptance\_map\_epic036.json :: nonclaims contains 'QA PASS'" | "JSON\_LIST\_OK docs/acceptance\_map\_epic036.json :: nonclaims contains 'PF09 status movement'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence."  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `QA PASS` nonclaim; `PF09 status movement` nonclaim; `OPS-01 not required by PR-01`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-008/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-008/primary.log | "FILE\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json.path\_proof.txt sha256=c7ac108a5171aa10c0fe32d54fda81aa0a0712495ceb6ebd5dbecd25bf3271d5" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.selected\_classification='unsupported\_runtime\_nonclaim'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_policy\_binding.snapshot.json :: policy\_binding.hde\_ferm008\_6\_completion\_role='Complete in this epic for route-policy classification only'"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `path_proof`; `selected_classification='unsupported_runtime_nonclaim'`; `route-policy classification only`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `audit/qa/hde-epic036/checks/po-009/primary.log`  
* Evidence pointer: Repo | audit/qa/hde-epic036/checks/po-009/primary.log | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.public\_reader\_change='NONE'" | "JSON\_OK artifacts/vendor/hdapi\_v2/bg\_resolve\_runtime\_nonclaims.json :: no\_claims.full\_hdapi\_v2\_runtime\_conformance='NONE'" | "TEXT\_OK audit/qa/hde-epic036/route\_policy\_decision.log :: no\_ai\_scope=true"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `public_reader_change='NONE'`; `full_hdapi_v2_runtime_conformance='NONE'`; `no_ai_scope=true`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_route\_policy.snapshot.json | "content: {"artifact\_kind":"bg\_resolve\_route\_policy","configured\_v2\_policy":{"classification":"unsupported\_runtime\_nonclaim"" | ""error\_code":"PROVIDER\_ROUTE\_UNSUPPORTED"" | ""selected\_posture":"unsupported\_runtime\_nonclaim""  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `bg_resolve_route_policy`; `PROVIDER_ROUTE_UNSUPPORTED`; `unsupported_runtime_nonclaim`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_request\_shape.snapshot.json | "content: {"artifact\_kind":"bg\_resolve\_request\_shape","configured\_v2\_bg\_resolve\_request\_shape":"NO\_BODYGRAPHS\_REQUEST\_BUILT\_UNSUPPORTED\_RUNTIME\_NONCLAIM"" | ""raw\_request\_body\_persisted":false" | ""raw\_vendor\_payload\_persisted":false"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM`; `raw_request_body_persisted=false`; `raw_vendor_payload_persisted=false`.  
* Path/label, exact as listed in Deliverables Report or live repo validation: `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* Evidence pointer: Repo | artifacts/vendor/hdapi\_v2/bg\_resolve\_bodygraph\_detail\_proof.json | "content: {"adapter\_sufficiency":"NO\_COMPLETE\_V2\_CHARTRESULT\_OR\_CHARTSIMPLERESULT\_TO\_BODYGRAPH\_PERSON\_CACHE\_ADAPTER\_FOUND\_IN\_INSPECTED\_LOCI"" | ""bodygraph\_detail\_sufficiency":"UNSUPPORTED\_RUNTIME\_NONCLAIM"" | ""v2\_chart\_data\_feeds\_existing\_bodygraph\_cache\_person\_compat\_flows":false"  
* Repo mergeability: tracked  
* Key proof facts, 1-3 exact strings, status lines, hashes, or short observed facts: `NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI`; `UNSUPPORTED_RUNTIME_NONCLAIM`; `false`.

C) Tokens/gates

* Token/gate name, quoted from Plan/Caveats: `DOC_DELTA_PRESENT_OK`  
* Evidence pointer for token/gate requirement: Live QA Plan | CHECK step-0b-doc-delta-capture PASS criteria | "\* PASS may claim `DOC_DELTA_PRESENT_OK`."  
* Evidence pointer(s) proving it: Evidence pointer: Deliverables Report | Check step-0b-doc-delta-capture | "- Intended tokens: `['DOC_DELTA_PRESENT_OK']`" | "- Claimed tokens: `['DOC_DELTA_PRESENT_OK']`"  
* Token/gate name, quoted from Plan/Caveats: `NO_EXTERNAL_IO_ON_REFUSAL_OK`  
* Evidence pointer for token/gate requirement: Live QA Plan | CHECK po-001 PASS criteria | "\* PASS may claim `NO_EXTERNAL_IO_ON_REFUSAL_OK`."  
* Evidence pointer(s) proving it: Evidence pointer: Deliverables Report | Check po-001 | "- Intended tokens: `['NO_EXTERNAL_IO_ON_REFUSAL_OK']`" | "- Claimed tokens: `['NO_EXTERNAL_IO_ON_REFUSAL_OK']`"  
* Token/gate name, quoted from Plan/Caveats: `ENV_RAILS_POLICY_OK`  
* Evidence pointer for token/gate requirement: Live QA Plan | CHECK po-002 PASS criteria | "\* PASS may claim `ENV_RAILS_POLICY_OK`."  
* Evidence pointer(s) proving it: Evidence pointer: Deliverables Report | Check po-002 | "- Intended tokens: `['ENV_RAILS_POLICY_OK']`" | "- Claimed tokens: `['ENV_RAILS_POLICY_OK']`"

C) PASS branch

QA Verdict and Optional Follow-ups

* Verdict line: PASS  
* The selected HDE-EPIC036 checks `step-0b-doc-delta-capture` through `po-009` have PASS status, exit code 0, primary logs, and sibling path proofs. Evidence pointer: Deliverables Report | Status Matrix | "| `step-0b-doc-delta-capture` | `PASS` | `0` | `2026-07-03T01:13:08Z` | `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log` |" | "| `po-009` | `PASS` | `0` | `2026-07-03T01:13:16Z` | `audit/qa/hde-epic036/checks/po-009/primary.log` |"  
* Live repo cross-check confirmed the material repo-resident evidence is present on `main` and tracked/mergeable. Evidence pointer: Repo | GitHub compare main...main | "status=identical" | "HEAD=369e7b5e3fee05ef012a756241e160c691bb8a6b" | "files=\[\]"  
* No remediation or dev-escalation condition remains for this selected scope. Evidence pointer: Deliverables Report | Executive Summary | "- Overall result: `PASS` for all requested checks." | "- Check count: `10/10 PASS`" | "- Primary logs and sibling path proofs: present for all checks."  
* Non-binding follow-up: the next review scope should evaluate PO-010 onward separately, because this verdict covers only `step-0b-doc-delta-capture` through `po-009`. Evidence pointer: Deliverables Report | HDE-EPIC036 Live QA Action Report | "- Scope: `step-0b-doc-delta-capture`, `po-001` ... `po-009`"

Verdict line: PASS

\<eof\>