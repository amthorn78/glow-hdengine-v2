# Implementation Plan for HDE-EPIC034 with PR tasks, OPS tasks, PF09 Completion Scope, crosswalk, Codex prompts, and PF10 revision notes.

Version: r4

Artifact Map

Inputs:

* IG: r2 Epic Plan HDE-EPIC034.md  
    
* Caveats: None provided.  
    
* Codex Audit: Implementation Audit HDE-EPIC034.md  
    
* PF10: PF10-HDE-Build-Notes-v11.4.6.md  
    
* Relevant PF canon used:  
    
  * PF09.5 — HDE Build Checklist Fermentation  
  * PF14 — HDE Mechanics Guide  
  * PF12 — HDE Schemas and Artifacts  
  * PF04 — HDE Governance  
  * PF05 — HDE CLI-API-Vendor Ref  
  * PF07 — Glow Infrastructure  
  * PF02 — HDE Architecture  
  * PF06 — Epic Process Guide  
  * PF19 — Glow QA Guide  
  * PF27 — Canon Plan Templates

Output:

* Implementation Plan for HDE-EPIC034 with PRs, OPS tasks, PF09 Completion Scope, Crosswalk, and Codex Prompts.

Brief recap of scope

HDE-EPIC034 implements the canon-safe HumanDesignAPI v2 vendor adapter architecture work for Fermentation Pass 5\. The plan now follows latest PF10 live guidance: discoverable operational, infrastructure, vendor, credential, environment, open-rails, and OPS-root facts are not deferred by default. Unknown but safely discoverable facts route through bounded OPS discovery, and open-rails testing is allowed when needed, provided it is PO-authorized, bounded, secret-safe, and evidence-recorded.

The revised implementation scope includes source-selection policy and v1 legacy isolation, OPS discovery for v2 request-shaping facts, v2 request shaping, v2 response-envelope mapping into HDE internal inputs, adapter/presenter boundary proof, closed-rails deterministic shaping and refusal proof, and a bounded PO-run open-rails v2 smoke. This plan still does not claim full HumanDesignAPI v2 runtime conformance, does not change public Reader bytes, does not add public routes or flags, does not create a new HTTP home, and does not introduce AI runtime or AI evidence scope.

## PF09 Completion Scope

| PF09 document | PF09 task ID | PF09 subtask ID | Disposition for this plan | Implementing task ID(s) | IG source item(s) | Caveat ID(s) | Proof pointer | ADR ID | PF07-gap note | Notes |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM005 | HDE-FERM005.1 | Already implemented and reused | Already implemented | Existing Work Check; PF09 Completion Map | None | PF09.5 proof: "*Subtask status:* Done (EPIC-010 / EPIC-017)"; "*Task status:* Done (history-locked via EPIC-010 / EPIC-017)" | N/A | N/A | Reused only as prior CLI Aux preview posture. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM006 | HDE-FERM006.1 | Already implemented and reused | Already implemented | Existing Work Check | None | PF09.5 proof: "Subtask status: Done"; "Epic or card: HDE-EPIC033 PR-01"; "HDE-EPIC033 PR-01 produces the governed source inventory in canonical JSON and markdown summary forms." | N/A | N/A | Reused as contract-inventory foundation only. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM006 | HDE-FERM006.2 | Already implemented and reused | Already implemented | Existing Work Check | None | PF09.5 proof: "Subtask status: Done"; "Epic or card: HDE-EPIC033 PR-01"; "HDE-EPIC033 PR-01 validates `v2-routes.yaml` and `v1-routes.yaml`, records `[v2-routes.yaml] status=VALIDATED`, records `[v1-routes.yaml] status=VALIDATED`, quarantines suspect `api-reference/openapi.json`, and records `[route-spec-gate] status=PASS`." | N/A | N/A | Reused as contract-inventory foundation only. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM006 | HDE-FERM006.3 | Already implemented and reused | Already implemented | Existing Work Check | None | PF09.5 proof: "Subtask status: Done"; "Epic or card: HDE-EPIC033 PR-01"; "The contract map binds validated vendor sources to `POST /v2/charts`, `POST /v2/charts/simple`, `POST /v2/charts/coordinates`, `POST /v1/bodygraphs`, and `POST /v1/bodygraphs/simple`." | N/A | N/A | Reused as contract-inventory foundation only. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM006 | HDE-FERM006.4 | Already implemented and reused | Already implemented | Existing Work Check | None | PF09.5 proof: "Subtask status: Done"; "Epic or card: HDE-EPIC033 PR-01"; "HDE-EPIC033 PR-01 binds the HDAPI v2 contract-inventory artifacts into the Human Evidence Index and Machine Mirror, refreshes hash sentinels, adds sibling path proofs, and validates the governed evidence set." | N/A | N/A | Reused as contract-inventory foundation only. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.1 | Complete in this epic | PR-01 | Deliverable D1 | None | N/A | N/A | N/A | Source-selection policy and v1 legacy isolation. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.2 | Complete in this epic | OPS-01; PR-02 | PF09 Completion Map — HDE-FERM007.2; TI-001; PF10 Addendum 2.3 ADR-001 | None | N/A | N/A | N/A | PF10 supersedes r1 deferral; route OPS discovery plus dependent PR work. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.3 | Complete in this epic | PR-03 | Deliverable D2 | None | N/A | N/A | N/A | Response-envelope mapping into HDE internal inputs. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.4 | Complete in this epic | PR-04 | Deliverable D3 | None | N/A | N/A | N/A | Adapter and presenter boundary proof. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.5 | Complete in this epic | OPS-01; PR-02; PR-05 | PF09 Completion Map — HDE-FERM007.5; TI-002; PF10 Addendum 2.3 ADR-002 | None | N/A | N/A | N/A | PF10 supersedes r1 blocked posture; closed-rails proof follows OPS discovery and request-shaping PR. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.1 | Complete in this epic | PR-05 | PF09 Completion Map — HDE-FERM008.1 | None | N/A | N/A | N/A | Closed-rails refusal can be proven by PR work and does not require PO secrets. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.2 | Complete in this epic | OPS-02; PR-06 | PF09 Completion Map — HDE-FERM008.2; TI-004; PF10 Addendum 2.3 ADR-003 | None | N/A | N/A | N/A | PF10 supersedes r1 blocked posture; route bounded PO-run open-rails smoke plus evidence-binding PR. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.3 | Deferred by IG/CAVEATS | N/A | PF09 Completion Map — HDE-FERM008.3; TI-005 | None | N/A | N/A | N/A | Deferred to future full error, retry, and rate-limit mapping work. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.4 | Deferred by IG/CAVEATS | N/A | PF09 Completion Map — HDE-FERM008.4; TI-006 | None | N/A | N/A | N/A | PR-03 records response mapping and schema gaps but does not claim full normalized-data-path proof. |
| PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.5 | Deferred by IG/CAVEATS | N/A | PF09 Completion Map — HDE-FERM008.5; TI-007 | None | N/A | N/A | N/A | PR-06 binds OPS smoke evidence for HDE-FERM008.2 only; it does not close the full live-conformance evidence loop. |

## Crosswalk: IG items \-\> Plan tasks

| IG work item (exact label from IG) | Caveats applied | PF09 document(s) | PF09 task ID(s) | PF09 subtask ID(s) | Implementation tasks | Evidence pointer (Already implemented only) | Status |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Existing Work Check — HDE-FERM005.1 is already Done and reused only as prior CLI Aux preview posture. | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM005 | HDE-FERM005.1 | Already implemented | PF09.5 proof: "*Subtask status:* Done (EPIC-010 / EPIC-017)"; "*Task status:* Done (history-locked via EPIC-010 / EPIC-017)" | Already implemented |
| Existing Work Check — HDE-FERM006 is already Done and provides the governed HumanDesignAPI v2 and legacy v1 contract-inventory foundation. | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM006 | HDE-FERM006.1; HDE-FERM006.2; HDE-FERM006.3; HDE-FERM006.4 | Already implemented | PF09.5 proof: "Task status: Done"; "HDE-EPIC033 PR-01 closes the inventory-only HDE-FERM006 slice."; "HDE-FERM006 and HDE-FERM006.1 through HDE-FERM006.4 are already drained to Done." | Already implemented |
| Deliverable D1: v2 source-selection policy and v1 legacy isolation | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.1 | PR-01 | N/A | Planned |
| PF09 Completion Map — HDE-FERM007.2 | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.2 | OPS-01; PR-02 | N/A | Planned |
| Deliverable D2: v2 response-envelope mapping into HDE internal inputs | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.3 | PR-03 | N/A | Planned |
| Deliverable D3: Adapter and presenter boundary preservation | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.4 | PR-04 | N/A | Planned |
| PF09 Completion Map — HDE-FERM007.5 | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007 | HDE-FERM007.5 | OPS-01; PR-02; PR-05 | N/A | Planned |
| PF09 Completion Map — HDE-FERM008.1 | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.1 | PR-05 | N/A | Planned |
| PF09 Completion Map — HDE-FERM008.2 | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.2 | OPS-02; PR-06 | N/A | Planned |
| PF09 Completion Map — HDE-FERM008.3 | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.3 | Deferred | N/A | Deferred |
| PF09 Completion Map — HDE-FERM008.4 | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.4 | Deferred | N/A | Deferred |
| PF09 Completion Map — HDE-FERM008.5 | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM008 | HDE-FERM008.5 | Deferred | N/A | Deferred |
| Tokens and Evidence (Acceptance) — Evidence pointers | None | PF09.5 — HDE Build Checklist Fermentation | HDE-FERM007; HDE-FERM008 | HDE-FERM007.1; HDE-FERM007.2; HDE-FERM007.3; HDE-FERM007.4; HDE-FERM007.5; HDE-FERM008.1; HDE-FERM008.2 | PR-01; OPS-01; PR-02; PR-03; PR-04; PR-05; OPS-02; PR-06 | N/A | Planned |

## Execution plan

1. Task ID: PR-01  
     
   * One-line intent: Implement and prove source-selection policy and v1 legacy isolation for the v2 vendor seam.  
   * Depends on: Existing HDE-FERM006 contract inventory.  
   * IG item(s) covered: Deliverable D1; PF09 Completion Map — HDE-FERM007.1.  
   * PF09 document(s): PF09.5 — HDE Build Checklist Fermentation.  
   * PF09 task ID(s): HDE-FERM007.  
   * PF09 subtask ID(s): HDE-FERM007.1.  
   * PF09 completion role: Complete in this epic.

   

2. Task ID: OPS-01  
     
   * One-line intent: PO discovers and records v2 request-shaping operational facts without exposing secret values.  
   * Depends on: PR-01.  
   * IG item(s) covered: PF09 Completion Map — HDE-FERM007.2; PF09 Completion Map — HDE-FERM007.5; TI-001; TI-002.  
   * PF09 document(s): PF09.5 — HDE Build Checklist Fermentation.  
   * PF09 task ID(s): HDE-FERM007.  
   * PF09 subtask ID(s): HDE-FERM007.2; HDE-FERM007.5.  
   * PF09 completion role: Contributes evidence only.

   

3. Task ID: PR-02  
     
   * One-line intent: Implement and prove v2 request shaping using OPS-discovered facts without guessing credential or infrastructure values.  
   * Depends on: PR-01; OPS-01.  
   * IG item(s) covered: PF09 Completion Map — HDE-FERM007.2; PF10 Addendum 2.3 ADR-001.  
   * PF09 document(s): PF09.5 — HDE Build Checklist Fermentation.  
   * PF09 task ID(s): HDE-FERM007.  
   * PF09 subtask ID(s): HDE-FERM007.2.  
   * PF09 completion role: Complete in this epic.

   

4. Task ID: PR-03  
     
   * One-line intent: Implement and prove v2 response-envelope mapping into HDE internal inputs without claiming full live conformance.  
   * Depends on: PR-01; PR-02.  
   * IG item(s) covered: Deliverable D2; PF09 Completion Map — HDE-FERM007.3.  
   * PF09 document(s): PF09.5 — HDE Build Checklist Fermentation.  
   * PF09 task ID(s): HDE-FERM007.  
   * PF09 subtask ID(s): HDE-FERM007.3.  
   * PF09 completion role: Complete in this epic.

   

5. Task ID: PR-04  
     
   * One-line intent: Prove adapter and presenter boundary preservation for the v2 vendor seam.  
   * Depends on: PR-01; PR-02; PR-03.  
   * IG item(s) covered: Deliverable D3; PF09 Completion Map — HDE-FERM007.4.  
   * PF09 document(s): PF09.5 — HDE Build Checklist Fermentation.  
   * PF09 task ID(s): HDE-FERM007.  
   * PF09 subtask ID(s): HDE-FERM007.4.  
   * PF09 completion role: Complete in this epic.

   

6. Task ID: PR-05  
     
   * One-line intent: Prove v2 adapter deterministic shaping and closed-rails refusal without external I/O.  
   * Depends on: PR-02; PR-04.  
   * IG item(s) covered: PF09 Completion Map — HDE-FERM007.5; PF09 Completion Map — HDE-FERM008.1.  
   * PF09 document(s): PF09.5 — HDE Build Checklist Fermentation.  
   * PF09 task ID(s): HDE-FERM007; HDE-FERM008.  
   * PF09 subtask ID(s): HDE-FERM007.5; HDE-FERM008.1.  
   * PF09 completion role: Complete in this epic.

   

7. Task ID: OPS-02  
     
   * One-line intent: PO executes bounded open-rails HumanDesignAPI v2 smoke and records secret-safe evidence.  
   * Depends on: OPS-01; PR-02; PR-05.  
   * IG item(s) covered: PF09 Completion Map — HDE-FERM008.2; TI-004; PF10 Addendum 2.3 ADR-003.  
   * PF09 document(s): PF09.5 — HDE Build Checklist Fermentation.  
   * PF09 task ID(s): HDE-FERM008.  
   * PF09 subtask ID(s): HDE-FERM008.2.  
   * PF09 completion role: Complete in this epic.

   

8. Task ID: PR-06  
     
   * One-line intent: Bind OPS-02 smoke evidence and final HDE-EPIC034 implementation evidence into governed repo artifacts without claiming full HDE-FERM008 completion.  
   * Depends on: OPS-02.  
   * IG item(s) covered: Tokens and Evidence (Acceptance) — Evidence pointers; PF09 Completion Map — HDE-FERM008.2.  
   * PF09 document(s): PF09.5 — HDE Build Checklist Fermentation.  
   * PF09 task ID(s): HDE-FERM008.  
   * PF09 subtask ID(s): HDE-FERM008.2.  
   * PF09 completion role: Complete in this epic.

## PR series

### PR-01 — v2 source selection and v1 legacy isolation

Intent (what must be true after PR)

HumanDesignAPI v2 chart endpoints are represented as the recommended vendor path for internal source-selection policy, while v1 BodyGraph endpoints remain explicitly named legacy behavior. The implementation must distinguish the full chart, simple chart, and coordinates chart route families and produce governed source-selection and v1 legacy-guard evidence under closed rails.

IG source items (exact IG labels)

* Deliverable D1: v2 source-selection policy and v1 legacy isolation  
* PF09 Completion Map — HDE-FERM007.1  
* TI-001 \- HDE-FERM007.2 request-shaping execution blocked by PF05/PF07 facts

Caveats applied (CAV-001 style IDs; None if not applicable)

None

PF09 document(s) \+ task IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 document: PF09.5 — HDE Build Checklist Fermentation

PF09 task ID: HDE-FERM007

Proof excerpt:

"Task ID: HDE-FERM007"

"Task name/label: HDAPI v2 vendor adapter architecture"

"Update the HDE vendor seam so the architecture can use HumanDesignAPI v2 chart endpoints as the recommended vendor path while preserving v1 BodyGraph routes as explicit legacy behavior."

PF09 subtask IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 subtask ID: HDE-FERM007.1

Proof excerpt:

"\#\#\# **Subtask HDE-FERM007.1 \- Pin v2 source-selection policy**"

"Define and implement source-selection behavior so v2 chart endpoints are the recommended vendor path. v1 BodyGraph endpoints may be retained only as explicitly named legacy behavior."

"The policy must distinguish full chart, simple chart, and coordinates chart routes rather than treating all vendor calls as one legacy BodyGraph endpoint."

PF09 completion role: Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR | Blocked on PF07-gap

Complete in this epic

PF14 pointers (anchors \+ proof excerpts from PF14)

PF14 anchor: HDAPI v2 vendor seam mechanics

Proof excerpt:

"HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration. That seam MUST route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through the existing architecture boundaries."

PF14 anchor: HDAPI v2 evidence mechanics

Proof excerpt:

"HDAPI v2 evidence mechanics. The repo MUST provide evidence generators and validators for the HDAPI v2 contract inventory, request shaping, response mapping, source selection, legacy-v1 guard, adapter-boundary proof, closed-rails refusal proof, open-rails smoke summary where PO-executed, error mapping, rate-limit mapping, normalized data path proof, source-cache replay, source-cache checksum proof, endpoint-tier parsing, anomaly quarantine, and index or mirror binding."

PF07 facts / gaps (exact PF07 facts if needed, else None; if missing, state exact PF07-gap blocker)

None required for PR-01 execution.

Observed repo reality (non-PF; only when needed for portability, copied from CODEX\_AUDIT)

None. No audit-derived existing repo-locus claim is asserted for PR-01. Repository loci used by this PR are discovery-first and must be inspected before Codex relies on them.

Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Inspect whether these repo paths exist before relying on them:

* artifacts/vendor/hdapi\_v2/contract\_map.json  
* artifacts/vendor/hdapi\_v2/source\_inventory.json  
* tools/evidence/generate\_hdapi\_v2\_contract\_inventory.py  
* tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
* engine/bodygraph/vendor\_client.py  
* engine/bodygraph/ingest.py  
* engine/bodygraph/resolver.py  
* tools/evidence/update\_evidence\_index.py

If present, confirm the contract inventory records these endpoint families:

* Planned endpoint: POST /v2/charts  
* Planned endpoint: POST /v2/charts/simple  
* Planned endpoint: POST /v2/charts/coordinates  
* Planned endpoint: POST /v1/bodygraphs  
* Planned endpoint: POST /v1/bodygraphs/simple

Confirm missing or create:

* Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json.path\_proof.txt  
* Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log  
* Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-01/source\_selection\_check.log  
* Planned output: audit/qa/hde-epic034/pr-01/source\_selection\_check.log.path\_proof.txt

Implementation requirements (what, not how; include PF doc citations when PF canon adds specificity)

* Implement source-selection behavior from the governed contract inventory, not from guessed endpoint names.  
* Treat Planned endpoint: POST /v2/charts, Planned endpoint: POST /v2/charts/simple, and Planned endpoint: POST /v2/charts/coordinates as the recommended v2 chart route family.  
* Treat Planned endpoint: POST /v1/bodygraphs and Planned endpoint: POST /v1/bodygraphs/simple as explicit legacy v1 BodyGraph behavior.  
* Do not implement HDE-FERM007.2 request shaping in this PR.  
* Do not use or guess v2 base URL, credential/config key names, or secret-binding names.  
* Do not perform live vendor calls.  
* Do not create any public Reader route, public flag, public payload, or new HTTP home.  
* Do not introduce AI, OpenAI, LLM, prompt, embedding, chatbot, model-call, AI-provider credentials, AI rails, AI evidence families, or AI acceptance-token scope.  
* Produce governed evidence and update the Human Evidence Index, hash sentinel, Machine Mirror, and path-proof transcripts in the same PR.

Concrete anchors (small snippets, pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json must be canonical JSON and include, at minimum:

* route families for Planned endpoint: POST /v2/charts, Planned endpoint: POST /v2/charts/simple, Planned endpoint: POST /v2/charts/coordinates, Planned endpoint: POST /v1/bodygraphs, and Planned endpoint: POST /v1/bodygraphs/simple  
* recommended route family classification for v2 chart routes  
* explicit legacy classification for v1 BodyGraph routes  
* no runtime conformance claim  
* no open-rails vendor smoke claim  
* no public Reader change claim  
* no AI scope claim

Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log must be LF-terminated text and must prove that v1 BodyGraph routes are not silently collapsed into v2 chart routes.

Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)

* Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json.path\_proof.txt  
* Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log  
* Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-01/source\_selection\_check.log  
* Planned output: audit/qa/hde-epic034/pr-01/source\_selection\_check.log.path\_proof.txt  
* Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Acceptance tokens (minimal list; explicit; do not invent)

* JSON\_CANONICAL\_CHECK\_OK  
* EVIDENCE\_INDEX\_UPDATED\_OK  
* MACHINE\_MIRROR\_UPDATED\_OK  
* EVIDENCE\_PATHS\_VALIDATED\_OK  
* EVIDENCE\_PATH\_PROOFS\_OK  
* TESTS\_PASS\_OK  
* DOC\_DELTA\_PRESENT\_OK

Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed rails only. Do not open rails. Do not execute live vendor calls.

Basic QA check (one-line, non-runbook) \+ pass condition

Run targeted unit/evidence tests for source-selection and legacy-v1 guard plus canonical JSON/index checks; pass condition is green tests and current indexed evidence outputs with path proofs.

PO inputs (only if required; names-only; no secret values)

None.

Codex Prompt (paste-ready; required)

You are implementing PR-01 for HDE-EPIC034.

Goal: Implement and prove source-selection policy and v1 legacy isolation for the internal HumanDesignAPI v2 vendor seam. After this PR, v2 chart endpoints are the recommended internal vendor route family and v1 BodyGraph endpoints remain explicit legacy behavior.

Scope:

* Complete PF09.5 — HDE Build Checklist Fermentation task HDE-FERM007, subtask HDE-FERM007.1.  
* Do not implement HDE-FERM007.2 request shaping.  
* Do not execute live vendor calls.  
* Do not open rails.  
* Do not change public Reader bytes, public response shape, public transport behavior, public routes, public flags, or CLI public-output covenant.  
* Do not create a new HTTP home.  
* Do not introduce OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, AI evidence-family, or AI acceptance-token scope.

PF09.5 applies:

* Task ID: HDE-FERM007.  
* Subtask ID: HDE-FERM007.1.  
* PF09.5 proof text: "Define and implement source-selection behavior so v2 chart endpoints are the recommended vendor path. v1 BodyGraph endpoints may be retained only as explicitly named legacy behavior. The policy must distinguish full chart, simple chart, and coordinates chart routes rather than treating all vendor calls as one legacy BodyGraph endpoint."

PF14 anchors apply:

* HDAPI v2 vendor seam mechanics.  
* HDAPI v2 evidence mechanics.  
* PF14 proof text: "HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration. That seam MUST route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through the existing architecture boundaries."  
* PF14 proof text: "HDAPI v2 evidence mechanics. The repo MUST provide evidence generators and validators for the HDAPI v2 contract inventory, request shaping, response mapping, source selection, legacy-v1 guard, adapter-boundary proof, closed-rails refusal proof, open-rails smoke summary where PO-executed, error mapping, rate-limit mapping, normalized data path proof, source-cache replay, source-cache checksum proof, endpoint-tier parsing, anomaly quarantine, and index or mirror binding."

PF10 live rule:

* Unknown operational facts are not deferred by default.  
* This PR does not need v2 credential or base URL facts because it is source-selection only.  
* Later request-shaping facts are routed through OPS-01.

Repo-locus posture:

* No existing repo path below is asserted as pre-verified.  
* Inspect whether each path exists before relying on it.  
* If a path is missing, report the missing path and use the nearest canon-safe implementation target without inventing the locus.

Inspect first:

* Inspect whether this path exists: artifacts/vendor/hdapi\_v2/contract\_map.json  
* Inspect whether this path exists: artifacts/vendor/hdapi\_v2/source\_inventory.json  
* Inspect whether this path exists: tools/evidence/generate\_hdapi\_v2\_contract\_inventory.py  
* Inspect whether this path exists: tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
* Inspect whether this path exists: tools/evidence/update\_evidence\_index.py  
* Inspect whether this path exists: engine/bodygraph/vendor\_client.py  
* Inspect whether this path exists: engine/bodygraph/ingest.py  
* Inspect whether this path exists: engine/bodygraph/resolver.py

Change:

* Add the minimal source-selection implementation needed to classify Planned endpoint: POST /v2/charts, Planned endpoint: POST /v2/charts/simple, and Planned endpoint: POST /v2/charts/coordinates as recommended v2 chart routes.  
    
* Preserve Planned endpoint: POST /v1/bodygraphs and Planned endpoint: POST /v1/bodygraphs/simple as explicit legacy v1 BodyGraph routes.  
    
* Add or update tests proving the route family distinction and no silent collapse of v1 legacy routes into v2 chart routes.  
    
* Add or update an evidence generator that writes:  
    
  * Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
  * Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json.path\_proof.txt  
  * Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log  
  * Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log.path\_proof.txt  
  * Planned output: audit/qa/hde-epic034/pr-01/source\_selection\_check.log  
  * Planned output: audit/qa/hde-epic034/pr-01/source\_selection\_check.log.path\_proof.txt


* Update existing evidence ledgers:  
    
  * Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Evidence requirements:

* Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json is canonical JSON with one trailing LF.  
* Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log is LF-terminated text.  
* Both primary artifacts have co-located Planned output: .path\_proof.txt files.  
* Existing: docs/evidence/INDEX.json and Existing: artifacts/evidence\_index.jsonl include the new artifact bindings.  
* No new acceptance token names are introduced.

Tests/checks to run:

* Run targeted tests covering the source-selection policy and legacy-v1 guard.  
* Run canonical JSON checks for Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json.  
* Run evidence index and path-proof validation checks available in the repo.

Success means:

* HDE-FERM007.1 behavior is implemented and proven.  
* Planned output: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json exists, is canonical, and distinguishes recommended v2 chart routes from legacy v1 BodyGraph routes.  
* Planned output: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log exists and proves v1 routes remain explicit legacy behavior.  
* New artifacts are indexed and mirrored with path proofs.  
* No public Reader, public route, public flag, open-rails, live vendor, new HTTP home, or AI scope was added.

Failure means:

* Any route family is guessed instead of derived from the governed contract map.  
* Any v1 route is silently collapsed into v2 behavior.  
* Any v2 base URL or credential/config fact is guessed.  
* Any live vendor call is attempted.  
* Any public Reader byte, public route, public flag, new HTTP home, or AI scope appears.  
* Evidence artifacts are missing, non-canonical where canonical JSON is required, unindexed, or missing path proofs.

### PR-02 — v2 request shaping after OPS discovery

Intent (what must be true after PR)

The repo contains v2-aware request shaping for POST /v2/charts, POST /v2/charts/simple, and POST /v2/charts/coordinates, using validated contract-map fields and PF10-decided vendor key/header posture. It must preserve `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, and `HD-Geocode-Key` where required. OPS-01 must not rediscover those PF10-decided names or header families; it may confirm deployment presence, secret-binding status, deprecated alias status, environment presence, endpoint-family availability, account/tier posture, and safe execution posture.

IG source items (exact IG labels)

* PF09 Completion Map — HDE-FERM007.2  
* TI-001 \- HDE-FERM007.2 request-shaping execution blocked by PF05/PF07 facts  
* PF10 Addendum 2.3 ADR-001 — HDE-FERM007.2 request-shaping execution

Caveats applied (CAV-001 style IDs; None if not applicable)

None

PF09 document(s) \+ task IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 document: PF09.5 — HDE Build Checklist Fermentation

PF09 task ID: HDE-FERM007

Proof excerpt:

"Task ID: HDE-FERM007"

"Task name/label: HDAPI v2 vendor adapter architecture"

"The adapter must route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through one sanctioned vendor seam and must not create a second HTTP home or bypass adapter and presenter boundaries."

PF09 subtask IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 subtask ID: HDE-FERM007.2

Proof excerpt:

"\#\#\# **Subtask HDE-FERM007.2 \- Update request shaping for v2 endpoints**"

"Replace or gate legacy vendor request shaping with v2-aware shaping for POST /v2/charts, POST /v2/charts/simple, and POST /v2/charts/coordinates."

"Request shaping must use validated contract-map fields, canonical body construction where governed artifacts are emitted, and the v2 auth model. Exact secret/config key names must be pinned in PF05 and PF07 before execution."

PF09 completion role: Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR | Blocked on PF07-gap

Complete in this epic

PF14 pointers (anchors \+ proof excerpts from PF14)

PF14 anchor: HDAPI v2 request-shaping and response-mapping mechanics

Proof excerpt:

"HDAPI v2 request-shaping and response-mapping mechanics. The repo MUST provide deterministic request-shaping and response-mapping proofs for the pending v2 vendor path."

"Derive v2 endpoint selection, auth-header use, geocode-key handling, and request-body shaping from governed contract inventory and the owning bytes document, not from guesses."

PF14 anchor: HDAPI v2 vendor seam mechanics

Proof excerpt:

"HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration. That seam MUST route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through the existing architecture boundaries."

PF07 facts / gaps (exact PF07 facts if needed, else None; if missing, state exact PF07-gap blocker)

PF10 decides the canonical request-shaping key/header posture for this slice: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, and `HD-Geocode-Key` where required. The deprecated spelling `HDAPI_BASE_URL` may be handled only as legacy drift or temporary compatibility fallback and must not be treated as canonical. Codex must read Planned output after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json before implementing request shaping. If the fact summary is missing or incomplete for deployment presence, secret-binding status, deprecated alias status, endpoint-family availability, account/tier posture, or safe execution posture, Codex must stop the PR slice as blocked by missing OPS discovery evidence and must not guess.

Observed repo reality (non-PF; only when needed for portability, copied from CODEX\_AUDIT)

Observed Evidence (non-PF):

"Seed: v2 base URL posture"

"Status: Found"

"Paths: docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.3.1.md; docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.1.2.md"

"Proof: PF05 states exact v2 base URL posture remains pending; PF07 audit result records no HDAPI v2 base URL facts found."

Observed Evidence (non-PF):

"Seed: v2 auth header names"

"Status: Unclear"

"Proof: Contract inventory and PF05 mention auth model/header ownership, but no concrete HDE v2 auth header binding was found."

Observed Evidence (non-PF):

"Seed: credential/config key names"

"Status: Unclear"

"Proof: HDAPI\_BASE\_URL appears as legacy/current env posture; PF05 says exact v2 credential/config key names remain pending. Permanent v2-specific names are not pinned."

PF10 update to observed posture:

* `HD_API_BASE_URL` is the canonical HumanDesignAPI base URL environment variable.  
* `HDAPI_BASE_URL` is deprecated legacy drift and may be used only as a temporary compatibility alias under the PF10 resolution rule.  
* `HD_API_KEY` is the canonical vendor API key environment variable.  
* `GEO_API_KEY` is the canonical geocode key environment variable.  
* v2 chart requests must project `HD_API_KEY` as `Authorization: Bearer`.  
* v1 legacy BodyGraph requests must project `HD_API_KEY` as `HD-Api-Key`.  
* Geocode-required routes must project `GEO_API_KEY` as `HD-Geocode-Key`.

Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Inspect first:

* Existing after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json  
* Planned output from PR-01: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Inspect whether this path exists before relying on it: artifacts/vendor/hdapi\_v2/contract\_map.json  
* Inspect whether this path exists before relying on it: engine/bodygraph/vendor\_client.py  
* Inspect whether this path exists before relying on it: engine/bodygraph/ingest.py  
* Inspect whether this path exists before relying on it: engine/bodygraph/resolver.py

Confirm found:

* OPS-01 confirms deployment presence for `HD_API_BASE_URL` without secret values.  
* OPS-01 confirms `HD_API_KEY` secret-binding status without secret values.  
* OPS-01 confirms `GEO_API_KEY` secret-binding status where geocoding is required, without secret values.  
* OPS-01 classifies any observed `HDAPI_BASE_URL` usage only as deprecated legacy drift, temporary compatibility fallback, or migration evidence.  
* OPS-01 records documented environment-variable bindings without secret values.  
* OPS-01 records endpoint-family availability.  
* OPS-01 records account/tier posture.  
* OPS-01 records whether request-shaping PR work can proceed safely.

Confirm missing or create:

* Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
* Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-02/request\_shaping\_check.log  
* Planned output: audit/qa/hde-epic034/pr-02/request\_shaping\_check.log.path\_proof.txt

Implementation requirements (what, not how; include PF doc citations when PF canon adds specificity)

* Implement v2-aware request shaping only after OPS-01 evidence exists.  
* Use validated contract-map fields for endpoint selection and request-body shape.  
* Use PF10-decided canonical names and header posture: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, and `HD-Geocode-Key` where required.  
* Use OPS-01 only for deployment presence, secret-binding status, deprecated alias status, endpoint-family availability, account/tier posture, and safe execution posture.  
* Do not embed secret values.  
* Do not treat `HDAPI_BASE_URL` as canonical; if supported temporarily, treat it only as deprecated legacy drift or compatibility fallback.  
* If both `HD_API_BASE_URL` and `HDAPI_BASE_URL` exist and values differ, fail closed with a configuration ambiguity.  
* Emit deterministic request-shaping proof artifacts under closed rails.  
* Do not execute a live vendor call in this PR.  
* Preserve public Reader output and public route posture.

Concrete anchors (small snippets, pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json must be canonical JSON and include, at minimum:

* route family  
* endpoint path  
* request content-type posture  
* v2 auth header posture: `Authorization: Bearer <redacted>`  
* v1 legacy auth header posture: `HD-Api-Key: <redacted>`  
* credential environment-variable posture: `HD_API_KEY` without value  
* base URL environment-variable posture: `HD_API_BASE_URL` without value  
* deprecated alias posture for `HDAPI_BASE_URL` only if observed or compatibility fallback is implemented  
* geocode environment-variable posture: `GEO_API_KEY` without value when required  
* geocode header posture: `HD-Geocode-Key: <redacted>` when required  
* body-field source list from contract map  
* canonical request-body construction proof for governed artifact bytes  
* no live vendor call claim  
* no public Reader change claim  
* no AI scope claim

Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)

* Existing after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json  
* Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
* Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-02/request\_shaping\_check.log  
* Planned output: audit/qa/hde-epic034/pr-02/request\_shaping\_check.log.path\_proof.txt  
* Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Acceptance tokens (minimal list; explicit; do not invent)

* JSON\_CANONICAL\_CHECK\_OK  
* EVIDENCE\_INDEX\_UPDATED\_OK  
* MACHINE\_MIRROR\_UPDATED\_OK  
* EVIDENCE\_PATHS\_VALIDATED\_OK  
* EVIDENCE\_PATH\_PROOFS\_OK  
* TESTS\_PASS\_OK  
* DOC\_DELTA\_PRESENT\_OK

Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed rails only. Do not open rails. Do not execute live vendor calls.

Basic QA check (one-line, non-runbook) \+ pass condition

Run targeted request-shaping tests plus canonical JSON/index checks; pass condition is green tests and a current indexed request-shaping artifact with path proof.

PO inputs (only if required; names-only; no secret values)

* OPS-01 fact summary must exist before this PR starts.  
* No secret values may be supplied to Codex.

Codex Prompt (paste-ready; required)

You are implementing PR-02 for HDE-EPIC034.

Goal: Implement and prove v2-aware request shaping for POST /v2/charts, POST /v2/charts/simple, and POST /v2/charts/coordinates using PF10-decided key/header posture plus OPS-discovered deployment and safety facts. Do not guess infrastructure, credential, config, secret-binding, or legacy-to-v2 mapping values.

Scope:

* Complete PF09.5 — HDE Build Checklist Fermentation task HDE-FERM007, subtask HDE-FERM007.2.  
* Use PF10 live guidance: unknown but discoverable operational facts are not deferred by default, but PF10-decided canonical names and header families must not be rediscovered or treated as unknown.  
* Use `HD_API_BASE_URL` as the canonical HumanDesignAPI base URL key.  
* Treat `HDAPI_BASE_URL` only as deprecated legacy drift or temporary compatibility fallback.  
* Use `HD_API_KEY` as the canonical vendor API key environment variable.  
* Use `GEO_API_KEY` as the canonical geocode key environment variable.  
* Project v2 chart-route auth as `Authorization: Bearer <redacted>`.  
* Project v1 legacy BodyGraph auth as `HD-Api-Key: <redacted>`.  
* Project geocode auth as `HD-Geocode-Key: <redacted>` when required.  
* Do not execute live vendor calls.  
* Do not open rails.  
* Do not change public Reader bytes, public response shape, public transport behavior, public routes, public flags, or CLI public-output covenant.  
* Do not create a new HTTP home.  
* Do not introduce OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, AI evidence-family, or AI acceptance-token scope.

PF09.5 applies:

* Task ID: HDE-FERM007.  
* Subtask ID: HDE-FERM007.2.  
* PF09.5 proof text: "Replace or gate legacy vendor request shaping with v2-aware shaping for POST /v2/charts, POST /v2/charts/simple, and POST /v2/charts/coordinates. Request shaping must use validated contract-map fields, canonical body construction where governed artifacts are emitted, and the v2 auth model. Exact secret/config key names must be pinned in PF05 and PF07 before execution."

PF14 anchors apply:

* HDAPI v2 request-shaping and response-mapping mechanics.  
* HDAPI v2 vendor seam mechanics.  
* PF14 proof text: "Derive v2 endpoint selection, auth-header use, geocode-key handling, and request-body shaping from governed contract inventory and the owning bytes document, not from guesses."  
* PF14 proof text: "HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration. That seam MUST route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through the existing architecture boundaries."

Required OPS input:

* Existing after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json  
* Existing after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json.path\_proof.txt  
* If either file is missing, stop and report the PR as blocked by missing OPS-01 evidence. Do not guess any value.  
* OPS-01 may confirm deployment presence, secret-binding status, deprecated alias status, endpoint-family availability, account/tier posture, and safe execution posture. It must not redefine `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, or `HD-Geocode-Key`.

Inspect first:

* Existing after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json  
* Planned output from PR-01: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Existing: artifacts/vendor/hdapi\_v2/contract\_map.json (Observed Evidence, non-PF)  
* Existing: engine/bodygraph/vendor\_client.py (Observed Evidence, non-PF)  
* Existing: engine/bodygraph/ingest.py (Observed Evidence, non-PF)  
* Existing: engine/bodygraph/resolver.py (Observed Evidence, non-PF)

Change:

* Add or update v2 request-shaping code using PF10-decided canonical names and header posture.  
* Use `HD_API_BASE_URL` as the canonical base URL key.  
* If compatibility fallback is implemented, read deprecated alias `HDAPI_BASE_URL` only when `HD_API_BASE_URL` is absent.  
* If both `HD_API_BASE_URL` and `HDAPI_BASE_URL` exist and values match, use `HD_API_BASE_URL`.  
* If both `HD_API_BASE_URL` and `HDAPI_BASE_URL` exist and values differ, fail closed with a configuration ambiguity.  
* Use `HD_API_KEY` as the secret source for the vendor API key.  
* For v2 chart routes, construct auth as `Authorization: Bearer <HD_API_KEY value>`.  
* For v1 legacy BodyGraph routes, preserve auth as `HD-Api-Key: <HD_API_KEY value>`.  
* Use `GEO_API_KEY` as the secret source for `HD-Geocode-Key` when geocoding is required.  
* Use validated contract-map fields for route, content type, request body, auth model, and geocode-key posture.  
* Keep secret values out of code, logs, prompts, commits, and artifacts.  
* Add targeted tests for v2 request shaping under closed rails, including tests that v2 does not use `HD-Api-Key` and v1 legacy does not silently migrate to Bearer auth.  
* Add or update evidence generation for:  
  * Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
  * Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json.path\_proof.txt  
  * Planned output: audit/qa/hde-epic034/pr-02/request\_shaping\_check.log  
  * Planned output: audit/qa/hde-epic034/pr-02/request\_shaping\_check.log.path\_proof.txt  
* Update existing evidence ledgers:  
  * Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Evidence requirements:

* Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json is canonical JSON with one trailing LF.  
* It records route family, endpoint path, request content-type posture, v2 `Authorization: Bearer <redacted>`, v1 legacy `HD-Api-Key: <redacted>`, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `HD-Geocode-Key` when required, deprecated alias posture for `HDAPI_BASE_URL` if observed or implemented, body-field source list, and no live vendor call claim.  
* It has a co-located Planned output: .path\_proof.txt file.  
* Existing: docs/evidence/INDEX.json and Existing: artifacts/evidence\_index.jsonl include the new artifact binding.

Tests/checks to run:

* Run targeted tests covering v2 request shaping.  
* Run targeted tests proving v2 uses Bearer auth and v1 legacy BodyGraph uses `HD-Api-Key`.  
* Run targeted tests for canonical `HD_API_BASE_URL` resolution and deprecated `HDAPI_BASE_URL` fallback or fail-closed ambiguity behavior if compatibility fallback exists.  
* Run canonical JSON checks for Planned output: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json.  
* Run evidence index and path-proof validation checks available in the repo.

Success means:

* HDE-FERM007.2 behavior is implemented and proven.  
* The request-shaping artifact is canonical, indexed, mirrored, and path-proven.  
* v2 request shaping uses `Authorization: Bearer <redacted>`.  
* v1 legacy BodyGraph shaping uses `HD-Api-Key: <redacted>`.  
* `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` are preserved as canonical environment-variable names.  
* `HDAPI_BASE_URL` is not treated as canonical.  
* No secret value is exposed.  
* No live vendor call, public Reader change, new HTTP home, or AI scope is introduced.

Failure means:

* OPS-01 evidence is missing or incomplete for deployment presence, secret-binding status, deprecated alias status, endpoint-family availability, account/tier posture, or safe execution posture.  
* Any v2 base URL, credential/config, auth header, or secret-binding fact is guessed.  
* Any secret value is committed or logged.  
* v2 request shaping uses legacy `HD-Api-Key`.  
* v1 legacy BodyGraph request shaping silently migrates to Bearer auth without later PF10 or PF05 authority.  
* `HDAPI_BASE_URL` is treated as canonical or silently preferred over `HD_API_BASE_URL`.  
* Both `HD_API_BASE_URL` and `HDAPI_BASE_URL` exist with different values and the implementation does not fail closed.  
* Any live vendor call is attempted.  
* Any public Reader behavior or public transport behavior changes.  
* Evidence artifacts are missing, non-canonical where canonical JSON is required, unindexed, or missing path proofs.

### PR-03 — v2 response-envelope mapping into HDE internal inputs

Intent (what must be true after PR)

The repo contains deterministic v2 response-envelope mapping into HDE internal inputs at the proof level, preserving response type, success status, errorCode, data payload identity, and route variant. If the v2 response cannot truthfully feed existing BodyGraph, cache, compatibility, sampler, or admin paths without schema changes, the PR must record the mapping gap and avoid compatibility by inference.

IG source items (exact IG labels)

* Deliverable D2: v2 response-envelope mapping into HDE internal inputs  
* PF09 Completion Map — HDE-FERM007.3  
* TI-006 \- HDE-FERM008.4 normalized data path proof deferred

Caveats applied (CAV-001 style IDs; None if not applicable)

None

PF09 document(s) \+ task IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 document: PF09.5 — HDE Build Checklist Fermentation

PF09 task ID: HDE-FERM007

Proof excerpt:

"Task ID: HDE-FERM007"

"Task name/label: HDAPI v2 vendor adapter architecture"

"The adapter must route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through one sanctioned vendor seam and must not create a second HTTP home or bypass adapter and presenter boundaries."

PF09 subtask IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 subtask ID: HDE-FERM007.3

Proof excerpt:

"\#\#\# **Subtask HDE-FERM007.3 \- Normalize v2 response envelopes into HDE BodyGraph and chart inputs**"

"Map the v2 response envelope into the HDE internal data model used by BodyGraph cache, compatibility, sampler, and admin surfaces."

"The mapping must preserve response type, success status, errorCode, data payload identity, and route variant."

PF09 completion role: Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR | Blocked on PF07-gap

Complete in this epic

PF14 pointers (anchors \+ proof excerpts from PF14)

PF14 anchor: HDAPI v2 request-shaping and response-mapping mechanics

Proof excerpt:

"HDAPI v2 request-shaping and response-mapping mechanics. The repo MUST provide deterministic request-shaping and response-mapping proofs for the pending v2 vendor path."

"\* Map the standard v2 response envelope into HDE internal structures only after the mapping is proven."

"\* Prove whether v2 response data can feed the existing BodyGraph cache and compat input path, or identify that a schema update is required in the owning schema home."

PF14 anchor: HDAPI v2 evidence mechanics

Proof excerpt:

"HDAPI v2 evidence mechanics. The repo MUST provide evidence generators and validators for the HDAPI v2 contract inventory, request shaping, response mapping, source selection, legacy-v1 guard, adapter-boundary proof, closed-rails refusal proof, open-rails smoke summary where PO-executed, error mapping, rate-limit mapping, normalized data path proof, source-cache replay, source-cache checksum proof, endpoint-tier parsing, anomaly quarantine, and index or mirror binding."

PF07 facts / gaps (exact PF07 facts if needed, else None; if missing, state exact PF07-gap blocker)

None required for PR-03 execution.

Do not use PF07-gap fields for live request execution. The response mapping must be fixture-backed, contract-map-backed, or OPS-01-fact-backed under closed rails and must not require live vendor secrets.

Observed repo reality (non-PF; only when needed for portability, copied from CODEX\_AUDIT)

None. No audit-derived existing repo-locus claim is asserted for PR-03. Contract-map and internal engine loci are discovery-first and must be inspected before Codex relies on them.

Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Confirm dependency outputs:

* Planned output from PR-01: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Planned output from PR-01: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log  
* Planned output from PR-02: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json

Inspect whether these repo paths exist before relying on them:

* artifacts/vendor/hdapi\_v2/contract\_map.json  
* engine/bodygraph/vendor\_client.py  
* engine/bodygraph/ingest.py  
* engine/bodygraph/resolver.py  
* engine/compat/compute.py

If artifacts/vendor/hdapi\_v2/contract\_map.json is present, inspect whether it contains v2 success-envelope descriptions before using it as the response-envelope source.

If any internal engine locus is present, inspect how BodyGraph, cache, compatibility, sampler, or admin paths consume mapped inputs before using that locus in the proof.

If any listed repo path is missing, report it as missing and do not invent a replacement locus.

Confirm missing or create:

* Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
* Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-03/response\_mapping\_check.log  
* Planned output: audit/qa/hde-epic034/pr-03/response\_mapping\_check.log.path\_proof.txt

Implementation requirements (what, not how; include PF doc citations when PF canon adds specificity)

Map v2 response-envelope fields into HDE internal input semantics at the proof level.

Preserve response type, success status, errorCode, data payload identity, and route variant.

Use fixture-backed, contract-map-backed, or OPS-01-fact-backed closed-rails evidence only.

Do not claim the full HDE-FERM008.4 normalized data path proof.

If v2 ChartResult data differs from the legacy BodyGraph shape, record the mismatch as a schema or adapter mapping gap.

Do not smooth over incompatibility by inference.

Do not log vendor payload bodies or secrets.

Do not use AI interpretation or model-generated transformation.

Do not change public Reader output.

Concrete anchors (small snippets, pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json must be canonical JSON and include, at minimum:

* source contract map digest or input reference  
* route variant  
* response type  
* success status handling  
* errorCode handling  
* data payload identity posture  
* internal target posture for BodyGraph/cache/compatibility/sampler/admin paths  
* schema gap status when applicable  
* explicit non-claim for live vendor conformance  
* explicit non-claim for public Reader changes  
* explicit no-AI transformation posture

Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)

* Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
* Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-03/response\_mapping\_check.log  
* Planned output: audit/qa/hde-epic034/pr-03/response\_mapping\_check.log.path\_proof.txt  
* Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Acceptance tokens (minimal list; explicit; do not invent)

* JSON\_CANONICAL\_CHECK\_OK  
* EVIDENCE\_INDEX\_UPDATED\_OK  
* MACHINE\_MIRROR\_UPDATED\_OK  
* EVIDENCE\_PATHS\_VALIDATED\_OK  
* EVIDENCE\_PATH\_PROOFS\_OK  
* TESTS\_PASS\_OK  
* DOC\_DELTA\_PRESENT\_OK

Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed rails only. Do not open rails. Do not execute live vendor calls.

Basic QA check (one-line, non-runbook) \+ pass condition

Run targeted mapping tests plus canonical JSON/index checks; pass condition is green tests and a current response-mapping artifact with path proof and no compatibility-by-inference claim.

PO inputs (only if required; names-only; no secret values)

None.

Codex Prompt (paste-ready; required)

You are implementing PR-03 for HDE-EPIC034.

Goal: Implement and prove v2 response-envelope mapping into HDE internal inputs without claiming full live vendor conformance, request-shaping live execution, or public Reader changes.

Scope:

* Complete PF09.5 — HDE Build Checklist Fermentation task HDE-FERM007, subtask HDE-FERM007.3.  
* Do not claim HDE-FERM008.4 normalized data path proof.  
* Do not execute live vendor calls.  
* Do not open rails.  
* Do not change public Reader bytes, public response shape, public transport behavior, public routes, public flags, or CLI public-output covenant.  
* Do not use AI interpretation or model-generated transformation.

PF09.5 applies:

* Task ID: HDE-FERM007.  
* Subtask ID: HDE-FERM007.3.  
* PF09.5 proof text: "Map the v2 response envelope into the HDE internal data model used by BodyGraph cache, compatibility, sampler, and admin surfaces. The mapping must preserve response type, success status, errorCode, data payload identity, and route variant."

PF14 anchors apply:

* HDAPI v2 request-shaping and response-mapping mechanics.  
* HDAPI v2 evidence mechanics.  
* PF14 proof text: "HDAPI v2 request-shaping and response-mapping mechanics. The repo MUST provide deterministic request-shaping and response-mapping proofs for the pending v2 vendor path."  
* PF14 proof text: "Map the standard v2 response envelope into HDE internal structures only after the mapping is proven."  
* PF14 proof text: "Prove whether v2 response data can feed the existing BodyGraph cache and compat input path, or identify that a schema update is required in the owning schema home."

PF10 live rule:

* Unknown but discoverable facts are routed through OPS discovery, not guessed.  
* This PR must use PR-01 source selection, PR-02 request-shaping posture, and controlled fixtures or snapshots. It must inspect contract inventory before relying on any contract-map path and must not require live vendor access.

Repo-locus posture:

* No existing repo path below is asserted as pre-verified.  
* Inspect whether each path exists before relying on it.  
* If a path is missing, report the missing path and use the nearest canon-safe implementation target without inventing the locus.

Inspect first:

* Planned output from PR-01: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Planned output from PR-01: artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log  
* Planned output from PR-02: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
* Inspect whether this path exists before relying on it: artifacts/vendor/hdapi\_v2/contract\_map.json  
* Inspect whether this path exists before relying on it: engine/bodygraph/vendor\_client.py  
* Inspect whether this path exists before relying on it: engine/bodygraph/ingest.py  
* Inspect whether this path exists before relying on it: engine/bodygraph/resolver.py  
* Inspect whether this path exists before relying on it: engine/compat/compute.py

Change:

* Add deterministic response-envelope mapping proof logic that reads from governed contract inventory only after the contract-map path has been found, and otherwise stops with a missing-locus report rather than inventing the locus  
* Preserve response type, success status, errorCode, data payload identity, and route variant.  
    
* Record whether the v2 response can feed existing BodyGraph, cache, compatibility, sampler, and admin paths.  
    
* If the response cannot truthfully feed an existing path without schema changes, record a schema gap in the response mapping artifact.  
    
* Add or update tests for response-envelope mapping and schema-gap behavior.  
    
* Add or update an evidence generator that writes:  
    
  * Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
  * Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json.path\_proof.txt  
  * Planned output: audit/qa/hde-epic034/pr-03/response\_mapping\_check.log  
  * Planned output: audit/qa/hde-epic034/pr-03/response\_mapping\_check.log.path\_proof.txt


* Update existing evidence ledgers:  
    
  * Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Evidence requirements:

* Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json is canonical JSON with one trailing LF.  
* It preserves response type, success status, errorCode, data payload identity, and route variant.  
* It states internal path compatibility or records schema gap without inference.  
* It includes no vendor payload bodies, secrets, AI transformation, public Reader change, live vendor conformance claim, or open-rails claim.  
* The artifact has a co-located Planned output: .path\_proof.txt file.  
* Existing: docs/evidence/INDEX.json and Existing: artifacts/evidence\_index.jsonl include the new artifact binding.

Tests/checks to run:

* Run targeted tests covering response-envelope mapping and schema-gap behavior.  
* Run canonical JSON checks for Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json.  
* Run evidence index and path-proof validation checks available in the repo.

Success means:

* HDE-FERM007.3 behavior is implemented and proven.  
* Planned output: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json exists, is canonical, and truthfully records the response-envelope mapping posture.  
* Schema gaps are recorded when applicable.  
* New artifacts are indexed and mirrored with path proofs.  
* No live vendor call, public Reader change, or AI transformation was introduced.

Failure means:

* Mapping depends on guessed v2 request-shaping or credential facts.  
* Mapping claims compatibility by inference.  
* Mapping logs vendor payload bodies or secrets.  
* Mapping changes public Reader output.  
* Evidence artifacts are missing, non-canonical where canonical JSON is required, unindexed, or missing path proofs.

### PR-04 — adapter and presenter boundary proof

Intent (what must be true after PR)

The repo contains a structural boundary proof showing that the HumanDesignAPI v2 vendor seam does not create a new HTTP home, bypass adapter guards, bypass the presenter boundary, introduce ad-hoc serialization, or authorize external I/O inside pure compute modules. HDE-FERM007.1, HDE-FERM007.2, and HDE-FERM007.3 evidence remains bound through governed index and mirror posture.

IG source items (exact IG labels)

* Deliverable D3: Adapter and presenter boundary preservation  
* PF09 Completion Map — HDE-FERM007.4  
* Tokens and Evidence (Acceptance) — Evidence pointers  
* TI-008 \- PF23 vendor seam drift remains planning context only

Caveats applied (CAV-001 style IDs; None if not applicable)

None

PF09 document(s) \+ task IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 document: PF09.5 — HDE Build Checklist Fermentation

PF09 task ID: HDE-FERM007

Proof excerpt:

"Task ID: HDE-FERM007"

"Task name/label: HDAPI v2 vendor adapter architecture"

"The adapter must route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through one sanctioned vendor seam and must not create a second HTTP home or bypass adapter and presenter boundaries."

PF09 subtask IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 subtask ID: HDE-FERM007.4

Proof excerpt:

"\#\#\# **Subtask HDE-FERM007.4 \- Preserve adapter and presenter boundaries**"

"Ensure the v2 vendor seam does not create a new HTTP home, does not bypass adapter guards, and does not introduce ad-hoc serialization."

"Adapter remains the HTTP home; presenter remains the byte-authoritative emitter; deterministic compute remains pure except for the sanctioned BodyGraph/vendor seam."

PF09 completion role: Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR | Blocked on PF07-gap

Complete in this epic

PF14 pointers (anchors \+ proof excerpts from PF14)

PF14 anchor: HDAPI v2 vendor seam mechanics

Proof excerpt:

"HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration. That seam MUST route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through the existing architecture boundaries."

"It MUST NOT create a second HTTP home, bypass the Adapter, bypass the Presenter, or authorize I/O in pure compute modules."

PF14 anchor: HDAPI v2 evidence mechanics

Proof excerpt:

"HDAPI v2 evidence mechanics. The repo MUST provide evidence generators and validators for the HDAPI v2 contract inventory, request shaping, response mapping, source selection, legacy-v1 guard, adapter-boundary proof, closed-rails refusal proof, open-rails smoke summary where PO-executed, error mapping, rate-limit mapping, normalized data path proof, source-cache replay, source-cache checksum proof, endpoint-tier parsing, anomaly quarantine, and index or mirror binding."

PF07 facts / gaps (exact PF07 facts if needed, else None; if missing, state exact PF07-gap blocker)

None required for PR-04 execution.

Observed repo reality (non-PF; only when needed for portability, copied from CODEX\_AUDIT)

None. No audit-derived existing architecture or repo-locus claim is asserted for PR-04. Adapter, presenter, engine, and evidence-tool loci are discovery-first and must be inspected before Codex relies on them.

Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Confirm dependency outputs:

* Planned output from PR-01: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Planned output from PR-02: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
* Planned output from PR-03: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Inspect whether these repo paths or roots exist before relying on them:

* adapter/wsgi.py  
* adapter/factory.py  
* presenter/  
* engine/cli/main.py  
* engine/bodygraph/vendor\_client.py  
* engine/bodygraph/ingest.py  
* engine/bodygraph/resolver.py  
* engine/compat/compute.py

After inspection, report the real adapter, presenter, and engine boundary loci in the boundary proof. Do not assume adapter, presenter, or engine paths exist if inspection does not find them.

Confirm missing or create:

* Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log  
* Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-04/boundary\_check.log  
* Planned output: audit/qa/hde-epic034/pr-04/boundary\_check.log.path\_proof.txt

Implementation requirements (what, not how; include PF doc citations when PF canon adds specificity)

* Produce a structural proof that no second HTTP home was introduced.  
* Prove adapter guards are not bypassed.  
* Prove presenter boundary is not bypassed.  
* Prove no ad-hoc serializer is introduced on governed/public output paths.  
* Prove pure compute modules did not gain external I/O because of the v2 vendor seam.  
* Bind PR-01, PR-02, PR-03, and PR-04 evidence families in the existing Human Evidence Index and Machine Mirror.  
* Do not claim HDE-FERM007.5, HDE-FERM008, runtime v2 conformance, live vendor conformance, or open-rails smoke.  
* Do not mandate PF document edits as implementation deliverables.

Concrete anchors (small snippets, pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log must be LF-terminated and include:

* observed adapter HTTP home posture  
* observed presenter/emitter posture  
* observed vendor seam posture  
* no second HTTP home claim  
* no adapter bypass claim  
* no presenter bypass claim  
* no ad-hoc serialization claim  
* no pure-compute external I/O claim  
* no live vendor success claim  
* no public Reader change claim  
* no AI scope claim

Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)

* Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log  
* Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-04/boundary\_check.log  
* Planned output: audit/qa/hde-epic034/pr-04/boundary\_check.log.path\_proof.txt  
* Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Acceptance tokens (minimal list; explicit; do not invent)

* JSON\_CANONICAL\_CHECK\_OK  
* EVIDENCE\_INDEX\_UPDATED\_OK  
* MACHINE\_MIRROR\_UPDATED\_OK  
* EVIDENCE\_PATHS\_VALIDATED\_OK  
* EVIDENCE\_PATH\_PROOFS\_OK  
* TESTS\_PASS\_OK  
* DOC\_DELTA\_PRESENT\_OK

Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed rails only. Do not open rails. Do not execute live vendor calls.

Basic QA check (one-line, non-runbook) \+ pass condition

Run boundary-proof tests/checks plus evidence index, path-proof, final-LF, and canonical JSON checks; pass condition is green checks and current indexed boundary evidence.

PO inputs (only if required; names-only; no secret values)

None.

Codex Prompt (paste-ready; required)

You are implementing PR-04 for HDE-EPIC034.

Goal:  
 Prove adapter and presenter boundary preservation for the HumanDesignAPI v2 vendor seam and bind implementation evidence for HDE-FERM007.1, HDE-FERM007.2, HDE-FERM007.3, and HDE-FERM007.4.

Scope:

* Complete PF09.5 — HDE Build Checklist Fermentation task HDE-FERM007, subtask HDE-FERM007.4.  
* Do not claim HDE-FERM007.5 closed-rails deterministic shaping proof in this PR.  
* Do not claim HDE-FERM008.  
* Do not execute live vendor calls.  
* Do not open rails.  
* Do not change public Reader bytes, public response shape, public transport behavior, public routes, public flags, or CLI public-output covenant.  
* Do not create a new HTTP home.  
* Do not introduce OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, AI evidence-family, or AI acceptance-token scope.

PF09.5 applies:

* Task ID: HDE-FERM007.  
* Subtask ID: HDE-FERM007.4.  
* PF09.5 proof text: "Ensure the v2 vendor seam does not create a new HTTP home, does not bypass adapter guards, and does not introduce ad-hoc serialization. Adapter remains the HTTP home; presenter remains the byte-authoritative emitter; deterministic compute remains pure except for the sanctioned BodyGraph/vendor seam."

PF14 anchors apply:

* HDAPI v2 vendor seam mechanics.  
* HDAPI v2 evidence mechanics.  
* PF14 proof text: "HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration. That seam MUST route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through the existing architecture boundaries."  
* PF14 proof text: "It MUST NOT create a second HTTP home, bypass the Adapter, bypass the Presenter, or authorize I/O in pure compute modules."  
* PF14 proof text: "HDAPI v2 evidence mechanics. The repo MUST provide evidence generators and validators for the HDAPI v2 contract inventory, request shaping, response mapping, source selection, legacy-v1 guard, adapter-boundary proof, closed-rails refusal proof, open-rails smoke summary where PO-executed, error mapping, rate-limit mapping, normalized data path proof, source-cache replay, source-cache checksum proof, endpoint-tier parsing, anomaly quarantine, and index or mirror binding."

Repo-locus posture:

* No existing repo path below is asserted as pre-verified.  
* Inspect whether each path or root exists before relying on it.  
* Report the actual adapter, presenter, engine, and evidence-tool loci found before using them in the boundary proof.  
* If a path is missing, report the missing path and use the nearest canon-safe implementation target without inventing the locus.

Inspect first:

* Inspect whether this path exists before relying on it: adapter/wsgi.py  
* Inspect whether this path exists before relying on it: adapter/factory.py  
* Inspect whether this root exists before relying on it: presenter/  
* Inspect whether this path exists before relying on it: engine/cli/main.py  
* Inspect whether this path exists before relying on it: engine/bodygraph/vendor\_client.py  
* Inspect whether this path exists before relying on it: engine/bodygraph/ingest.py  
* Inspect whether this path exists before relying on it: engine/bodygraph/resolver.py  
* Inspect whether this path exists before relying on it: engine/compat/compute.py  
* Planned output from PR-01: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Planned output from PR-02: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
* Planned output from PR-03: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
* Discover the repo-supported evidence updater before relying on any specific updater path. If no updater is found, stop and report the missing updater instead of inventing a path.

Change:

* Add a boundary proof generator or bounded check that verifies:  
  * no new HTTP home was introduced  
  * adapter remains the HTTP home  
  * adapter guards are not bypassed  
  * presenter remains the byte-authoritative emitter  
  * no ad-hoc serializer is introduced on governed/public output paths  
  * deterministic compute remains pure except for the sanctioned BodyGraph/vendor seam  
  * no live vendor success, open-rails smoke, public Reader change, new public route, public flag, new HTTP home, or AI scope is claimed


* Add or update tests for the boundary proof.  
    
* Write:  
    
  * Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log  
  * Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log.path\_proof.txt  
  * Planned output: audit/qa/hde-epic034/pr-04/boundary\_check.log  
  * Planned output: audit/qa/hde-epic034/pr-04/boundary\_check.log.path\_proof.txt


* Update existing evidence ledgers:  
    
  * Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Evidence requirements:

* Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log is LF-terminated text.  
* Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log.path\_proof.txt exists.  
* Evidence index and mirror updates are coherent and path-proven.  
* No new acceptance token names are introduced.

Tests/checks to run:

* Run targeted boundary-proof tests/checks.  
* Run evidence index, path-proof, final-LF, mirror schema, and canonical JSON checks available in the repo.  
* Run targeted tests added or changed for PR-01 through PR-04.

Success means:

* HDE-FERM007.4 behavior is proven.  
* Planned output: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log exists and truthfully proves the boundary posture.  
* HDE-FERM007.1, HDE-FERM007.2, HDE-FERM007.3, and HDE-FERM007.4 evidence families are indexed and mirrored.  
* No HDE-FERM007.5, HDE-FERM008, runtime v2 conformance, live vendor conformance, open-rails smoke, public Reader change, new HTTP home, or AI scope is claimed.

Failure means:

* Any second HTTP home, adapter bypass, presenter bypass, ad-hoc serializer, or pure-compute external I/O is introduced.  
* Any live vendor call is attempted.  
* Any v2 base URL, credential/config, or secret-binding fact is guessed.  
* Any unregistered vendor-v2-specific token is introduced.  
* Evidence artifacts are missing, unindexed, or missing path proofs.  
* Public Reader or public transport behavior changes.

### PR-05 — closed-rails deterministic shaping and refusal proof

Intent (what must be true after PR)

Under SAFE\_MODE=1 and ALLOW\_NETWORK=0, the repo proves that v2 source selection, request shaping, route choice, typed refusal behavior, and PF10-decided key/header projection are deterministic and perform no external I/O. The PR also satisfies the closed-rails refusal proof for every v2 vendor path now implemented.

IG source items (exact IG labels)

* PF09 Completion Map — HDE-FERM007.5  
* PF09 Completion Map — HDE-FERM008.1  
* PF10 Addendum 2.3 ADR-002 — HDE-FERM007.5 closed-rails deterministic shaping proof

Caveats applied (CAV-001 style IDs; None if not applicable)

None

PF09 document(s) \+ task IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 document: PF09.5 — HDE Build Checklist Fermentation

PF09 task ID: HDE-FERM007

Proof excerpt:

"Task ID: HDE-FERM007"

"Task name/label: HDAPI v2 vendor adapter architecture"

"Update the HDE vendor seam so the architecture can use HumanDesignAPI v2 chart endpoints as the recommended vendor path while preserving v1 BodyGraph routes as explicit legacy behavior."

PF09 task ID: HDE-FERM008

Proof excerpt:

"Task ID: HDE-FERM008"

"Task name/label: HDAPI v2 live conformance, rails, and evidence"

"Prove the implemented v2 vendor architecture against live or controlled vendor behavior under PO-authorized open rails, with secret-safe evidence."

PF09 subtask IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 subtask ID: HDE-FERM007.5

Proof excerpt:

"\#\#\# **Subtask HDE-FERM007.5 \- Prove v2 adapter determinism under closed rails**"

"Under SAFE\_MODE=1 and ALLOW\_NETWORK=0, prove that v2 source selection, request shaping, route choice, and typed refusal behavior are deterministic and perform no external I/O."

"This subtask must not be used as a substitute for open-rails vendor conformance. It proves fail-closed behavior and deterministic shaping only."

PF09 subtask ID: HDE-FERM008.1

Proof excerpt:

"\#\#\# **Subtask HDE-FERM008.1 \- Prove closed-rails refusal for v2 vendor path**"

"Prove that when rails are closed, every v2 vendor path refuses deterministically without DNS, socket, HTTP, or other external I/O."

"This subtask may be implemented by PR work and does not require PO secrets."

PF09 completion role: Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR | Blocked on PF07-gap

Complete in this epic

PF14 pointers (anchors \+ proof excerpts from PF14)

PF14 anchor: HDAPI v2 rails and Live QA mechanics

Proof excerpt:

"HDAPI v2 rails and Live QA mechanics. The repo MUST provide closed-rails and open-rails proof mechanics for HumanDesignAPI v2 conformance. Closed-rails mechanics MUST prove deterministic refusal and no outbound I/O when rails are closed."

PF14 anchor: HDAPI v2 request-shaping and response-mapping mechanics

Proof excerpt:

"HDAPI v2 request-shaping and response-mapping mechanics. The repo MUST provide deterministic request-shaping and response-mapping proofs for the pending v2 vendor path."

PF07 facts / gaps (exact PF07 facts if needed, else None; if missing, state exact PF07-gap blocker)

None. PR-05 uses PF10-decided canonical names and header posture plus OPS-01 discovered deployment and secret-binding facts from Existing after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json. It must not use secret values.

Observed repo reality (non-PF; only when needed for portability, copied from CODEX\_AUDIT)

Observed Evidence (non-PF):

"Seed: closed-rails deterministic shaping proof"

"Status: Not found"

"Proof: No artifact for artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt found in path/output checks."

Observed Evidence (non-PF):

"Seed: v2 closed-rails refusal"

"Status: Not found"

"Readiness impact: Closed-rails refusal proof absent for HDE-EPIC034."

Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Inspect first:

* Planned output from PR-01: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Planned output from PR-02: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
* Planned output from PR-03: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
* Planned output from PR-04: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log  
* Existing after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json

Confirm found:

* Source-selection artifact exists and is indexed.  
* Request-shaping artifact exists and is indexed.  
* Boundary proof exists and is indexed.  
* OPS-01 facts needed for deterministic closed-rails proof are present in safe form.  
* Closed rails are represented by SAFE\_MODE=1 and ALLOW\_NETWORK=0.  
* PR-02 request-shaping proof preserves `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, and `HD-Geocode-Key` where required.  
* Deprecated `HDAPI_BASE_URL` is not treated as canonical and any compatibility fallback is explicit.

Confirm missing or create:

* Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt  
* Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-05/closed\_rails\_check.log  
* Planned output: audit/qa/hde-epic034/pr-05/closed\_rails\_check.log.path\_proof.txt

Implementation requirements (what, not how; include PF doc citations when PF canon adds specificity)

* Prove deterministic source selection, request shaping, route choice, and typed refusal under closed rails.  
* Prove deterministic preservation of PF10-decided key/header posture: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, and `HD-Geocode-Key` where required.  
* Prove no DNS, socket, HTTP, or other external I/O is attempted under closed rails.  
* Prove two-run identity for the closed-rails proof where bytes are governed.  
* Preserve no-public-Reader-change posture.  
* Preserve no-open-rails and no-live-conformance claim.  
* Do not claim HDE-FERM008.2 open-rails smoke.  
* Do not claim HDE-FERM008.3, HDE-FERM008.4, or HDE-FERM008.5.

Concrete anchors (small snippets, pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt must be LF-terminated and include:

* rails posture: SAFE\_MODE=1  
* rails posture: ALLOW\_NETWORK=0  
* v2 route family tested  
* deterministic route choice posture  
* v2 auth posture: `Authorization: Bearer <redacted>`  
* v1 legacy auth posture: `HD-Api-Key: <redacted>`  
* canonical base URL key posture: `HD_API_BASE_URL`  
* canonical vendor key posture: `HD_API_KEY`  
* canonical geocode key posture: `GEO_API_KEY`  
* geocode header posture: `HD-Geocode-Key: <redacted>` where required  
* deprecated alias posture for `HDAPI_BASE_URL`, if observed or fallback exists  
* typed refusal posture  
* no DNS/socket/HTTP/external I/O posture  
* no open-rails smoke claim  
* no live vendor conformance claim  
* no public Reader change claim  
* no AI scope claim

Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)

* Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt  
* Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/pr-05/closed\_rails\_check.log  
* Planned output: audit/qa/hde-epic034/pr-05/closed\_rails\_check.log.path\_proof.txt  
* Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Acceptance tokens (minimal list; explicit; do not invent)

* JSON\_CANONICAL\_CHECK\_OK  
* TWO\_RUN\_IDENTITY\_OK  
* NO\_EXTERNAL\_IO\_ON\_REFUSAL\_OK  
* ERROR\_JSON\_CANON\_OK  
* ERROR\_TOKEN\_MAP\_OK  
* EVIDENCE\_INDEX\_UPDATED\_OK  
* MACHINE\_MIRROR\_UPDATED\_OK  
* EVIDENCE\_PATHS\_VALIDATED\_OK  
* EVIDENCE\_PATH\_PROOFS\_OK  
* TESTS\_PASS\_OK  
* DOC\_DELTA\_PRESENT\_OK

Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed rails only. Use SAFE\_MODE=1 and ALLOW\_NETWORK=0 for the proof. Do not open rails.

Basic QA check (one-line, non-runbook) \+ pass condition

Run closed-rails deterministic refusal tests twice; pass condition is identical governed proof output or a deterministic log showing no external I/O, successful typed refusal, and preserved PF10-decided key/header posture.

PO inputs (only if required; names-only; no secret values)

None after OPS-01 fact summary exists.

Codex Prompt (paste-ready; required)

You are implementing PR-05 for HDE-EPIC034.

Goal: Prove v2 adapter determinism under closed rails and prove closed-rails refusal for every implemented v2 vendor path. The proof must show deterministic source selection, request shaping, route choice, typed refusal, PF10-decided key/header posture, and no external I/O.

Scope:

* Complete PF09.5 — HDE Build Checklist Fermentation task HDE-FERM007, subtask HDE-FERM007.5.  
* Complete PF09.5 — HDE Build Checklist Fermentation task HDE-FERM008, subtask HDE-FERM008.1.  
* Preserve `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, and `HD-Geocode-Key` where required.  
* Do not execute live vendor calls.  
* Do not open rails.  
* Do not claim HDE-FERM008.2 open-rails smoke.  
* Do not claim HDE-FERM008.3, HDE-FERM008.4, or HDE-FERM008.5.  
* Do not change public Reader bytes, public response shape, public transport behavior, public routes, public flags, or CLI public-output covenant.  
* Do not introduce OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, AI evidence-family, or AI acceptance-token scope.

PF09.5 applies:

* Task ID: HDE-FERM007.  
* Subtask ID: HDE-FERM007.5.  
* PF09.5 proof text: "Under SAFE\_MODE=1 and ALLOW\_NETWORK=0, prove that v2 source selection, request shaping, route choice, and typed refusal behavior are deterministic and perform no external I/O."  
* Task ID: HDE-FERM008.  
* Subtask ID: HDE-FERM008.1.  
* PF09.5 proof text: "Prove that when rails are closed, every v2 vendor path refuses deterministically without DNS, socket, HTTP, or other external I/O."

PF14 anchors apply:

* HDAPI v2 rails and Live QA mechanics.  
* HDAPI v2 request-shaping and response-mapping mechanics.  
* PF14 proof text: "HDAPI v2 rails and Live QA mechanics. The repo MUST provide closed-rails and open-rails proof mechanics for HumanDesignAPI v2 conformance. Closed-rails mechanics MUST prove deterministic refusal and no outbound I/O when rails are closed."  
* PF14 proof text: "HDAPI v2 request-shaping and response-mapping mechanics. The repo MUST provide deterministic request-shaping and response-mapping proofs for the pending v2 vendor path."

PF10 live rule:

* Do not defer HDE-FERM007.5 solely because it depends on discoverable request-shaping or infrastructure facts.  
* Closed-rails deterministic proof must not invent values and may use safely recorded OPS facts.  
* PF10-decided facts are not discovery items: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, and `HD-Geocode-Key` where required.  
* Open-rails contrast, if needed later, belongs to OPS-02.

Inspect first:

* Planned output from PR-01: artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* Planned output from PR-02: artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
* Planned output from PR-03: artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
* Planned output from PR-04: artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log  
* Existing after OPS-01: audit/ops/hde-epic034/ops-01/fact\_summary.json

Change:

* Add closed-rails deterministic proof coverage for every implemented v2 vendor path.  
* Prove v2 request shaping uses Bearer auth and does not use legacy `HD-Api-Key`.  
* Prove v1 legacy BodyGraph shaping uses legacy `HD-Api-Key` and does not silently migrate to Bearer auth.  
* Prove `HD_API_BASE_URL` is canonical and `HDAPI_BASE_URL` is deprecated legacy drift or explicit compatibility fallback only.  
* Prove no DNS, socket, HTTP, or other external I/O under SAFE\_MODE=1 and ALLOW\_NETWORK=0.  
* Prove deterministic typed refusal and route choice.  
* Add or update tests for closed-rails deterministic refusal.  
* Write:  
  * Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt  
  * Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt.path\_proof.txt  
  * Planned output: audit/qa/hde-epic034/pr-05/closed\_rails\_check.log  
  * Planned output: audit/qa/hde-epic034/pr-05/closed\_rails\_check.log.path\_proof.txt  
* Update existing evidence ledgers:  
  * Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Evidence requirements:

* Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt is LF-terminated text.  
* It records SAFE\_MODE=1 and ALLOW\_NETWORK=0.  
* It proves deterministic route choice, typed refusal, no external I/O, PF10-decided key/header posture, no open-rails claim, no live conformance claim, no public Reader change, and no AI scope.  
* It has a co-located Planned output: .path\_proof.txt file.  
* Existing: docs/evidence/INDEX.json and Existing: artifacts/evidence\_index.jsonl include the new artifact binding.

Tests/checks to run:

* Run targeted closed-rails deterministic refusal tests.  
* Run tests or checks proving v2 Bearer auth posture and v1 legacy `HD-Api-Key` posture.  
* Run tests or checks proving canonical `HD_API_BASE_URL` resolution and fail-closed behavior for conflicting canonical/deprecated base-url values if compatibility fallback exists.  
* Run two-run identity or equivalent deterministic output checks for the closed-rails proof.  
* Run final-LF, evidence index, mirror, and path-proof validation checks available in the repo.

Success means:

* HDE-FERM007.5 and HDE-FERM008.1 are implemented and proven.  
* Planned output: artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt exists and truthfully proves closed-rails refusal and no external I/O.  
* The proof verifies that v2 shaping uses Bearer auth and v1 legacy shaping uses `HD-Api-Key`.  
* The proof preserves `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` as canonical environment-variable names.  
* No open-rails smoke or live vendor conformance is claimed.

Failure means:

* Any external I/O is attempted under closed rails.  
* Any live vendor call is attempted.  
* Any proof depends on guessed or secret values.  
* v2 shaping uses legacy `HD-Api-Key`.  
* v1 legacy shaping silently migrates to Bearer auth without later PF10 or PF05 authority.  
* `HDAPI_BASE_URL` is treated as canonical or silently preferred over `HD_API_BASE_URL`.  
* Conflicting canonical/deprecated base-url values do not fail closed if both are present.  
* Any public Reader behavior changes.  
* Evidence artifacts are missing, unindexed, or missing path proofs.

### PR-06 — OPS smoke evidence binding and final implementation artifact posture

Intent (what must be true after PR)

OPS-02 open-rails smoke evidence is committed or indexed in governed repo artifacts without exposing secrets, and HDE-EPIC034 implementation evidence is bound coherently. This PR completes HDE-FERM008.2 evidence posture only; it does not claim full HDE-FERM008 completion, HDE-FERM008.3, HDE-FERM008.4, HDE-FERM008.5, or broad runtime v2 conformance.

IG source items (exact IG labels)

* Tokens and Evidence (Acceptance) — Evidence pointers  
* PF09 Completion Map — HDE-FERM008.2  
* PF10 Addendum 2.3 ADR-003 — HDE-FERM008.2 PO-only open-rails smoke  
* PF10 Addendum 2.3 ADR-004 — PF27 close-stage path posture

Caveats applied (CAV-001 style IDs; None if not applicable)

None

PF09 document(s) \+ task IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 document: PF09.5 — HDE Build Checklist Fermentation

PF09 task ID: HDE-FERM008

Proof excerpt:

"Task ID: HDE-FERM008"

"Task name/label: HDAPI v2 live conformance, rails, and evidence"

"This task includes OPS work because open-rails vendor calls require secrets and privileged runtime posture. Automated agents must not execute vendor calls or claim completion without PO-run evidence."

PF09 subtask IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 subtask ID: HDE-FERM008.2

Proof excerpt:

"\#\#\# **Subtask HDE-FERM008.2 \- Execute PO-only open-rails v2 smoke**"

"Run a controlled PO-executed open-rails vendor smoke against the v2 vendor path. The run must capture command transcript, stdout, stderr, exit code, redacted/presence-only secret posture, request summary, result summary, and file checksums."

"This subtask must remain PO-only. Development agents may specify intent, constraints, success criteria, evidence requirements, and rollback intent, but must not execute the vendor call."

PF09 completion role: Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR | Blocked on PF07-gap

Complete in this epic

PF14 pointers (anchors \+ proof excerpts from PF14)

PF14 anchor: HDAPI v2 rails and Live QA mechanics

Proof excerpt:

"Open-rails vendor smoke, when required, is PO-only execution and MUST be treated as an ops task, not PR work and not QA substitution."

"The mechanics MUST require secret-safe, governed evidence for any PO-run open-rails smoke, including command transcript, stdout, stderr, exit code, redacted or presence-only secret posture, request summary, result summary, and file checksums, while avoiding plaintext secrets and unapproved vendor payload storage."

PF14 anchor: HDAPI v2 evidence mechanics

Proof excerpt:

"HDAPI v2 evidence mechanics. The repo MUST provide evidence generators and validators for the HDAPI v2 contract inventory, request shaping, response mapping, source selection, legacy-v1 guard, adapter-boundary proof, closed-rails refusal proof, open-rails smoke summary where PO-executed, error mapping, rate-limit mapping, normalized data path proof, source-cache replay, source-cache checksum proof, endpoint-tier parsing, anomaly quarantine, and index or mirror binding."

PF07 facts / gaps (exact PF07 facts if needed, else None; if missing, state exact PF07-gap blocker)

Uses OPS-02 evidence outputs as PO-run operational evidence under PF10 live authority. Do not convert OPS evidence into PF07 permanent facts in this PR. Record any permanent-doc drain targets as doc-delta candidates only.

Observed repo reality (non-PF; only when needed for portability, copied from CODEX\_AUDIT)

Observed Evidence (non-PF):

"Seed: open-rails HumanDesignAPI v2 smoke"

"Status: Not found"

"Proof: No EPIC034 open-rails smoke root or outputs found."

"Readiness impact: Open-rails smoke evidence absent."

Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Inspect first:

* Existing after OPS-02: audit/ops/hde-epic034/ops-02/commands.txt  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/stdout.log  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/stderr.log  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/exit\_codes.txt  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/request\_summary.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/result\_summary.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/files\_sha256.txt

Confirm found:

* OPS-02 evidence contains no raw API keys, bearer tokens, geocode keys, secret values, sensitive account details, unnecessary personally identifying information, uncontrolled production data, or unapproved full private payloads.  
* OPS-02 evidence records command transcript, stdout, stderr, exit code, redacted/presence-only secret posture, request summary, result summary, file checksums, and v2 `Authorization: Bearer <redacted>` header-shape evidence.  
* OPS-02 evidence does not overclaim full runtime conformance from a narrow smoke.  
* OPS-02 evidence does not classify a v2 `HD-Api-Key` header-shape failure as vendor unavailability.

Confirm missing or create:

* Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log  
* Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log.path\_proof.txt  
* Planned output: docs/acceptance\_map\_epic034.json  
* Planned output: docs/acceptance\_map\_epic034.json.path\_proof.txt  
* Planned output: audit/docdeltas/hde-epic034\_doc\_deltas.md  
* Planned output: audit/docdeltas/hde-epic034\_doc\_deltas.md.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/00\_meta/doc\_deltas.md  
* Planned output: audit/qa/hde-epic034/00\_meta/doc\_deltas.md.path\_proof.txt

Implementation requirements (what, not how; include PF doc citations when PF canon adds specificity)

* Validate that OPS-02 evidence is present and secret-safe.  
* Validate that OPS-02 evidence preserves v2 `Authorization: Bearer <redacted>` header-shape posture without raw secrets.  
* Validate that OPS-02 evidence does not show legacy `HD-Api-Key` used for v2.  
* Bind OPS-02 evidence into governed Evidence Index and Machine Mirror if canon requires indexing for the claimed HDE-FERM008.2 posture.  
* Create or update Planned output: docs/acceptance\_map\_epic034.json without inventing vendor-v2-specific acceptance tokens.  
* Create or update doc-delta candidate artifacts that record PF10 drain targets without requiring PF document edits in this PR.  
* Do not claim HDE-FERM008.3, HDE-FERM008.4, HDE-FERM008.5, or full runtime v2 conformance.  
* Do not treat vendor smoke success as broader conformance than it proves.  
* Do not treat vendor smoke failure as product failure without classifying credential, config, vendor, endpoint, account/tier, request-shaping, auth-header, response-mapping, infrastructure, rate-limit, external outage, product, and QA-expectation categories.

Concrete anchors (small snippets, pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log must be LF-terminated and include:

* OPS-02 evidence files checked  
* secret-safety classification  
* HDE-FERM008.2 posture  
* no HDE-FERM008.3 claim  
* no HDE-FERM008.4 claim  
* no HDE-FERM008.5 claim  
* no full runtime conformance claim  
* no public Reader change claim  
* no AI scope claim

Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)

* Existing after OPS-02: audit/ops/hde-epic034/ops-02/commands.txt  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/stdout.log  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/stderr.log  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/exit\_codes.txt  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/request\_summary.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/result\_summary.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/files\_sha256.txt  
* Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log  
* Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log.path\_proof.txt  
* Planned output: docs/acceptance\_map\_epic034.json  
* Planned output: docs/acceptance\_map\_epic034.json.path\_proof.txt  
* Planned output: audit/docdeltas/hde-epic034\_doc\_deltas.md  
* Planned output: audit/docdeltas/hde-epic034\_doc\_deltas.md.path\_proof.txt  
* Planned output: audit/qa/hde-epic034/00\_meta/doc\_deltas.md  
* Planned output: audit/qa/hde-epic034/00\_meta/doc\_deltas.md.path\_proof.txt  
* Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
* Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Acceptance tokens (minimal list; explicit; do not invent)

* EVIDENCE\_INDEX\_UPDATED\_OK  
* MACHINE\_MIRROR\_UPDATED\_OK  
* EVIDENCE\_INDEX\_HASH\_OK  
* EVIDENCE\_PATHS\_VALIDATED\_OK  
* EVIDENCE\_PATH\_PROOFS\_OK  
* TESTS\_PASS\_OK  
* DOC\_DELTA\_PRESENT\_OK

Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

PR-06 is repo-local and closed-rails. It consumes already-captured OPS-02 evidence. It must not perform open-rails execution.

Basic QA check (one-line, non-runbook) \+ pass condition

Run evidence-binding and secret-safety checks for OPS-02 artifacts plus index/mirror/path-proof checks; pass condition is indexed, path-proven, secret-safe evidence with no overclaim.

PO inputs (only if required; names-only; no secret values)

OPS-02 evidence bundle must exist before this PR starts.

Codex Prompt (paste-ready; required)

You are implementing PR-06 for HDE-EPIC034.

Goal: Bind PO-run OPS-02 open-rails smoke evidence for HDE-FERM008.2 into governed repo evidence without exposing secrets and without claiming full HumanDesignAPI v2 runtime conformance. Preserve secret-safe v2 Bearer-auth posture in the evidence binding.

Scope:

* Complete evidence posture for PF09.5 — HDE Build Checklist Fermentation task HDE-FERM008, subtask HDE-FERM008.2.  
* Do not execute live vendor calls.  
* Do not open rails.  
* Do not claim HDE-FERM008.3, HDE-FERM008.4, HDE-FERM008.5, or full runtime v2 conformance.  
* Do not treat vendor smoke success as broader conformance than it proves.  
* Do not treat vendor smoke failure as product failure until failure class is separated.  
* Do not treat v2 `HD-Api-Key` use as vendor unavailability; classify it as a request-shaping/auth-header defect or OPS setup defect.  
* Do not introduce new acceptance tokens.

PF09.5 applies:

* Task ID: HDE-FERM008.  
* Subtask ID: HDE-FERM008.2.  
* PF09.5 proof text: "Run a controlled PO-executed open-rails vendor smoke against the v2 vendor path. The run must capture command transcript, stdout, stderr, exit code, redacted/presence-only secret posture, request summary, result summary, and file checksums. It must not persist plaintext secrets or vendor payload bodies beyond the approved evidence shape."

PF14 anchors apply:

* HDAPI v2 rails and Live QA mechanics.  
* HDAPI v2 evidence mechanics.  
* PF14 proof text: "Open-rails vendor smoke, when required, is PO-only execution and MUST be treated as an ops task, not PR work and not QA substitution."  
* PF14 proof text: "The mechanics MUST require secret-safe, governed evidence for any PO-run open-rails smoke, including command transcript, stdout, stderr, exit code, redacted or presence-only secret posture, request summary, result summary, and file checksums, while avoiding plaintext secrets and unapproved vendor payload storage."

PF10 live rule:

* Open-rails testing is allowed when needed.  
* If open-rails proof is necessary and the work is in scope, create a bounded OPS open-rails task.  
* Do not defer merely because open rails, live vendor access, credentials, or PO-run operational execution are involved.  
* Do not overclaim full conformance from a narrow smoke.  
* OPS-02 v2 smoke must preserve `Authorization: Bearer <redacted>` for v2 chart routes.  
* OPS-02 v2 smoke must not use legacy `HD-Api-Key` for v2.  
* Evidence may record `HD_API_KEY`, `GEO_API_KEY`, `Authorization: Bearer <redacted>`, `HD-Api-Key: <redacted>`, and `HD-Geocode-Key: <redacted>`, but must not record raw secret values.

Required OPS evidence:

* Existing after OPS-02: audit/ops/hde-epic034/ops-02/commands.txt  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/stdout.log  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/stderr.log  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/exit\_codes.txt  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/request\_summary.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/result\_summary.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/files\_sha256.txt  
* If these files are missing, stop and report the PR as blocked by missing OPS-02 evidence. Do not fabricate the evidence.

Inspect first:

* Existing after OPS-02: audit/ops/hde-epic034/ops-02/commands.txt  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/stdout.log  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/stderr.log  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/exit\_codes.txt  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/request\_summary.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/result\_summary.json  
* Existing after OPS-02: audit/ops/hde-epic034/ops-02/files\_sha256.txt  
* Discover the repo-supported evidence updater before relying on any specific updater path. If no updater is found, stop and report the missing updater instead of inventing a path.

Change:

* Validate that OPS-02 evidence contains no raw API keys, bearer tokens, geocode keys, secret values, sensitive account details, unnecessary personally identifying information, uncontrolled production data, or unapproved full private payloads.  
* Validate that OPS-02 evidence preserves v2 `Authorization: Bearer <redacted>` header shape.  
* Validate that OPS-02 evidence does not show legacy `HD-Api-Key` used for v2 chart routes.  
* Validate that any v2 auth-header failure caused by sending `HD-Api-Key` is classified as request-shaping/auth-header defect or OPS setup defect, not vendor unavailability.  
* Add or update binding evidence:  
  * Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log  
  * Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log.path\_proof.txt  
* Add or update:  
  * Planned output: docs/acceptance\_map\_epic034.json  
  * Planned output: docs/acceptance\_map\_epic034.json.path\_proof.txt  
  * Planned output: audit/docdeltas/hde-epic034\_doc\_deltas.md  
  * Planned output: audit/docdeltas/hde-epic034\_doc\_deltas.md.path\_proof.txt  
  * Planned output: audit/qa/hde-epic034/00\_meta/doc\_deltas.md  
  * Planned output: audit/qa/hde-epic034/00\_meta/doc\_deltas.md.path\_proof.txt  
* Update existing evidence ledgers:  
  * Existing: docs/evidence/INDEX.json (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.json.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: docs/evidence/INDEX.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256 (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.path\_proof.txt (PF12 — HDE Schemas and Artifacts)  
  * Existing: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt (PF12 — HDE Schemas and Artifacts)

Evidence requirements:

* Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log is LF-terminated text.  
* It records the OPS-02 evidence files checked, secret-safety classification, v2 `Authorization: Bearer <redacted>` posture, HDE-FERM008.2 posture, and explicit non-claims for HDE-FERM008.3, HDE-FERM008.4, HDE-FERM008.5, full runtime conformance, public Reader change, and AI scope.  
* It records that v2 `HD-Api-Key` usage, if present, is a request-shaping/auth-header defect or OPS setup defect rather than vendor unavailability.  
* Planned output: docs/acceptance\_map\_epic034.json uses only registered tokens.  
* New and changed governed artifacts are indexed, mirrored, and path-proven.

Tests/checks to run:

* Run secret-safety scan/checks available in the repo against OPS-02 evidence.  
* Run evidence index, mirror, final-LF, path-proof, and acceptance-map checks available in the repo.

Success means:

* HDE-FERM008.2 evidence is present, secret-safe, indexed or bound as required, and does not overclaim.  
* Planned output: audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log exists and is path-proven.  
* OPS-02 evidence preserves v2 `Authorization: Bearer <redacted>` posture without raw secrets.  
* Planned output: docs/acceptance\_map\_epic034.json exists and does not invent tokens.  
* HDE-FERM008.3, HDE-FERM008.4, HDE-FERM008.5, and full runtime v2 conformance remain unclaimed.

Failure means:

* OPS-02 evidence is missing.  
* Any secret value appears in repo artifacts.  
* OPS-02 evidence fails to preserve v2 Bearer-auth posture.  
* OPS-02 evidence uses or permits legacy `HD-Api-Key` as v2 auth without classifying it as a request-shaping/auth-header defect or OPS setup defect.  
* The evidence overclaims full v2 conformance or broader success than the smoke proves.  
* Any unregistered token is introduced.  
* Evidence artifacts are missing, unindexed, or missing path proofs.

## Ops tasks

### **OPS-01 — Discover v2 request-shaping operational facts**

Intent (what must be true after OPS task)

The PO discovers and records the non-secret operational facts required to implement HDE-FERM007.2 request shaping and HDE-FERM007.5 deterministic closed-rails proof. OPS-01 must not rediscover or rename PF10-decided canonical names and header families.

IG source items (exact IG labels)

* PF09 Completion Map — HDE-FERM007.2  
* PF09 Completion Map — HDE-FERM007.5  
* TI-001  
* TI-002  
* PF10 Addendum 2.3 ADR-001  
* PF10 Addendum 2.3 ADR-002

Caveats applied (CAV-001 style IDs; None if not applicable)

None

PF09 document(s) \+ task IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 document: PF09.5 — HDE Build Checklist Fermentation

PF09 task ID: HDE-FERM007

Proof excerpt:

"Task ID: HDE-FERM007"

"Task name/label: HDAPI v2 vendor adapter architecture"

"The adapter must route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through one sanctioned vendor seam and must not create a second HTTP home or bypass adapter and presenter boundaries."

PF09 subtask IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 subtask ID: HDE-FERM007.2

Proof excerpt:

"\#\#\# **Subtask HDE-FERM007.2 \- Update request shaping for v2 endpoints**"

"Request shaping must use validated contract-map fields, canonical body construction where governed artifacts are emitted, and the v2 auth model. Exact secret/config key names must be pinned in PF05 and PF07 before execution."

PF09 subtask ID: HDE-FERM007.5

Proof excerpt:

"\#\#\# **Subtask HDE-FERM007.5 \- Prove v2 adapter determinism under closed rails**"

"Under SAFE\_MODE=1 and ALLOW\_NETWORK=0, prove that v2 source selection, request shaping, route choice, and typed refusal behavior are deterministic and perform no external I/O."

PF09 completion role: Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR | Blocked on PF07-gap

Contributes evidence only

PF14 pointers (anchors \+ proof excerpts from PF14)

PF14 anchor: HDAPI v2 request-shaping and response-mapping mechanics

Proof excerpt:

"Derive v2 endpoint selection, auth-header use, geocode-key handling, and request-body shaping from governed contract inventory and the owning bytes document, not from guesses."

PF14 anchor: HDAPI v2 rails and Live QA mechanics

Proof excerpt:

"Open-rails vendor smoke, when required, is PO-only execution and MUST be treated as an ops task, not PR work and not QA substitution."

PF07 facts / gaps (exact PF07 facts if needed, else None; if missing, state exact PF07-gap blocker)

PF10 decides the canonical vendor environment-variable names and header families for this slice. OPS-01 may confirm deployment presence, secret-binding status, deprecated alias status, environment presence, endpoint-family availability, account/tier posture, and safe execution posture, but must not rename or rediscover `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, or `HD-Geocode-Key`.

Preconditions (which PRs must already be merged; which environment must exist)

* PR-01 merged or otherwise accepted as the source-selection baseline.  
* PO has authorized bounded discovery.  
* PO has access to the relevant runtime, vendor account, deployment configuration, or secret-binding management surfaces.  
* No secret value may be copied into chat, prompts, commits, logs, or artifacts.

Operator action (canon-grounded when available; what-not-how only where canon is silent)

PO-only execution, IA-guided.

Record the following PF10-decided facts without treating them as discovery questions:

* canonical base URL key: `HD_API_BASE_URL`  
* deprecated legacy base URL alias: `HDAPI_BASE_URL`  
* canonical vendor API key: `HD_API_KEY`  
* canonical geocode key: `GEO_API_KEY`  
* v2 chart-route auth header shape: `Authorization: Bearer <redacted>`  
* v1 legacy BodyGraph auth header shape: `HD-Api-Key: <redacted>`  
* geocode header shape when required: `HD-Geocode-Key: <redacted>`

Discover and record only the following operational fact set:

* whether `HD_API_BASE_URL` is present in each target environment  
* whether deprecated `HDAPI_BASE_URL` is absent, present as temporary compatibility alias, or present as legacy drift  
* whether any simultaneous `HD_API_BASE_URL` and `HDAPI_BASE_URL` values match or conflict  
* `HD_API_KEY` secret-binding presence, not secret value  
* `GEO_API_KEY` secret-binding presence where geocoding is required, not secret value  
* documented environment-variable bindings  
* endpoint-family availability  
* account/tier posture  
* whether request-shaping PR work can proceed safely  
* whether closed-rails deterministic proof can be designed honestly  
* whether open-rails smoke can proceed safely after PR prerequisites

Do not record raw API keys, bearer tokens, geocode keys, secret values, sensitive account details, unnecessary personally identifying information, uncontrolled production data, or full private payloads.

Evidence outputs (exact artifact names \+ concrete lowercase paths including filenames)

* Planned output: audit/ops/hde-epic034/ops-01/fact\_summary.json  
* Planned output: audit/ops/hde-epic034/ops-01/fact\_summary.json.path\_proof.txt  
* Planned output: audit/ops/hde-epic034/ops-01/commands.txt  
* Planned output: audit/ops/hde-epic034/ops-01/stdout.log  
* Planned output: audit/ops/hde-epic034/ops-01/stderr.log  
* Planned output: audit/ops/hde-epic034/ops-01/exit\_codes.txt  
* Planned output: audit/ops/hde-epic034/ops-01/files\_sha256.txt

Verification (embedded; what proves success and what evidence to capture)

Success is proven when Planned output: audit/ops/hde-epic034/ops-01/fact\_summary.json records the exact non-secret fact set above, identifies any facts that remain unavailable with reason, and includes a clear proceed or blocked classification for PR-02, PR-05, and OPS-02.

If a fact cannot be safely discovered, the summary must classify it under the PF10 planning categories, such as unsafe to discover now, requires PO/Thoth decision, requires PF10 live rule, requires permanent canon update before safe execution, valid deferral, out of scope, or phase drift.

Evidence commit plan (which PR will add or index the evidence if canon requires repo indexing or mirror update)

PR-02 consumes OPS-01 facts for request shaping. PR-06 may bind OPS discovery evidence into final evidence posture if required by repo evidence checks.

PO inputs (only if required; names-only; no secret values)

* PO authorization for bounded OPS discovery.  
* PO access to relevant runtime, vendor, deployment, and secret-binding surfaces.  
* Names-only deployment presence and secret-binding posture for `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY`.  
* Deprecated alias status for `HDAPI_BASE_URL`.  
* No secret values.

### OPS-02 — PO-only open-rails v2 smoke

Intent (what must be true after OPS task)

The PO runs a controlled, bounded, secret-safe open-rails HumanDesignAPI v2 smoke and records evidence sufficient to classify live reachability, credential-binding correctness, endpoint availability, account/tier posture, vendor error class, redacted response shape, safe status outcome, v2 Bearer-auth posture, and whether follow-up PR, OPS, QA update, or canon update is needed.

IG source items (exact IG labels)

* PF09 Completion Map — HDE-FERM008.2  
* TI-004  
* PF10 Addendum 2.3 ADR-003

Caveats applied (CAV-001 style IDs; None if not applicable)

None

PF09 document(s) \+ task IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 document: PF09.5 — HDE Build Checklist Fermentation

PF09 task ID: HDE-FERM008

Proof excerpt:

"Task ID: HDE-FERM008"

"Task name/label: HDAPI v2 live conformance, rails, and evidence"

"This task includes OPS work because open-rails vendor calls require secrets and privileged runtime posture. Automated agents must not execute vendor calls or claim completion without PO-run evidence."

PF09 subtask IDs \+ proof excerpts from the relevant phased PF09.x document(s)

PF09 subtask ID: HDE-FERM008.2

Proof excerpt:

"\#\#\# **Subtask HDE-FERM008.2 \- Execute PO-only open-rails v2 smoke**"

"Run a controlled PO-executed open-rails vendor smoke against the v2 vendor path. The run must capture command transcript, stdout, stderr, exit code, redacted/presence-only secret posture, request summary, result summary, and file checksums."

"It must not persist plaintext secrets or vendor payload bodies beyond the approved evidence shape."

PF09 completion role: Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR | Blocked on PF07-gap

Complete in this epic

PF14 pointers (anchors \+ proof excerpts from PF14)

PF14 anchor: HDAPI v2 rails and Live QA mechanics

Proof excerpt:

"Open-rails vendor smoke, when required, is PO-only execution and MUST be treated as an ops task, not PR work and not QA substitution."

"The mechanics MUST require secret-safe, governed evidence for any PO-run open-rails smoke, including command transcript, stdout, stderr, exit code, redacted or presence-only secret posture, request summary, result summary, and file checksums, while avoiding plaintext secrets and unapproved vendor payload storage."

PF07 facts / gaps (exact PF07 facts if needed, else None; if missing, state exact PF07-gap blocker)

OPS-02 depends on OPS-01 discovered deployment and secret-binding facts. If OPS-01 does not confirm a safe live smoke basis, OPS-02 must not proceed. OPS-02 must use PF10-decided v2 `Authorization: Bearer <redacted>` header shape for v2 chart routes and must not use legacy `HD-Api-Key` for v2.

Preconditions (which PRs must already be merged; which environment must exist)

* OPS-01 completed with fact\_summary.json and proceed classification for open-rails smoke.  
* PR-02 completed request-shaping implementation.  
* PR-05 completed closed-rails deterministic refusal proof.  
* PO explicitly authorizes live external execution.  
* Required `HD_API_KEY` credential binding exists and can be projected as `Authorization: Bearer <redacted>` without exposing secret values.  
* `HD_API_BASE_URL` deployment posture is confirmed.  
* `GEO_API_KEY` binding exists if the selected route requires geocoding.  
* The smoke target is HumanDesignAPI only. No OpenAI, LLM, AI-agent, or other AI-provider call is in scope.

Operator action (canon-grounded when available; what-not-how only where canon is silent)

PO-only execution, IA-guided.

Run one bounded open-rails v2 vendor smoke using the implementation-approved route family and PF10-decided v2 Bearer-auth posture. The smoke must use `Authorization: Bearer <redacted>` for v2 chart routes. It must not use legacy `HD-Api-Key` for v2 chart routes.

The smoke may record:

* task ID  
* operator or owner role  
* date/time if available  
* environment label  
* vendor family or endpoint family  
* credential-binding name, not secret value  
* `HD_API_BASE_URL` presence, not secret value  
* `HD_API_KEY` presence, not secret value  
* `GEO_API_KEY` presence when required, not secret value  
* v2 header-shape evidence: `Authorization: Bearer <redacted>`  
* `HD-Geocode-Key: <redacted>` presence when required  
* request class, not secret payload  
* high-level result  
* status code or vendor error class when safe  
* redacted response excerpt when safe  
* whether behavior matched expectation  
* whether follow-up PR, OPS, QA update, or canon update is needed

The smoke must not record:

* raw API keys  
* raw bearer tokens  
* raw geocode keys  
* raw secrets  
* sensitive account details  
* unnecessary personally identifying information  
* uncontrolled production data  
* full private payloads unless explicitly approved and safe

Evidence outputs (exact artifact names \+ concrete lowercase paths including filenames)

* Planned output: audit/ops/hde-epic034/ops-02/commands.txt  
* Planned output: audit/ops/hde-epic034/ops-02/stdout.log  
* Planned output: audit/ops/hde-epic034/ops-02/stderr.log  
* Planned output: audit/ops/hde-epic034/ops-02/exit\_codes.txt  
* Planned output: audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json  
* Planned output: audit/ops/hde-epic034/ops-02/request\_summary.json  
* Planned output: audit/ops/hde-epic034/ops-02/result\_summary.json  
* Planned output: audit/ops/hde-epic034/ops-02/files\_sha256.txt

Verification (embedded; what proves success and what evidence to capture)

Success is not defined as vendor success alone. Success is a complete, secret-safe evidence bundle that truthfully classifies the live result without overclaiming and records v2 Bearer-auth header shape in secret-safe form. If the smoke fails, the result summary must classify the likely failure category without collapsing it into product failure by default. A v2 open-rails failure caused by sending `HD-Api-Key` instead of `Authorization: Bearer` must be classified as a request-shaping/auth-header defect or OPS setup defect, not as vendor unavailability.

Allowed failure categories include:

* credential issue  
* config issue  
* vendor account/tier limitation  
* endpoint unavailability  
* vendor contract mismatch  
* request-shaping defect  
* auth-header defect  
* response-mapping defect  
* infrastructure gap  
* rate-limit or retry posture  
* external outage  
* product implementation defect  
* QA plan expectation mismatch

Evidence commit plan (which PR will add or index the evidence if canon requires repo indexing or mirror update)

PR-06 consumes and binds OPS-02 evidence.

PO inputs (only if required; names-only; no secret values)

* PO live execution authorization.  
* PO access to required `HD_API_KEY` credential binding.  
* PO access to `GEO_API_KEY` credential binding if geocoding is required.  
* PO access to the target environment.  
* No secret values.

PO Inputs Summary

* PO authorization for OPS-01 bounded operational discovery.  
* PO access to relevant runtime, vendor, deployment, and secret-binding surfaces for OPS-01.  
* PO authorization for OPS-02 live external open-rails smoke.  
* PO access to required `HD_API_KEY` credential binding for OPS-02.  
* PO access to `GEO_API_KEY` credential binding if geocoding is required.  
* PO access to target environment for OPS-02.  
* Names-only deployment presence and secret-binding posture for `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY`.  
* Deprecated alias status for `HDAPI_BASE_URL`.  
* No secret values.

## ADRs (Canon reconciliation notes)

DR ID: ADR-001

Type/Tag: ADR / PF10-SUPERSEDED-R1-BLOCKER

Decision/Problem

r1 treated HDE-FERM007.2 request-shaping execution as blocked on PF07-gap because v2 request-shaping infrastructure and credential facts were unknown. Latest PF10 Addendum 2.3 decides that HDE-FERM007.2 must not be deferred solely because those facts are unknown and should be routed as OPS discovery plus dependent PR work.

Bounded PF10 update

OPS discovery must not rediscover PF10-decided canonical names or header families. `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 `HD-Api-Key`, and `HD-Geocode-Key` are PF10-decided facts. OPS discovery may confirm deployment presence, secret-binding state, QA legacy-key drift, deprecated alias status, and safe execution posture.

Options

* Option 1: Keep r1 blocked posture.  
* Option 2: Follow PF10 and route OPS discovery plus dependent PR implementation.

Recommendation

Use Option 2\. OPS-01 discovers deployment and safety facts. PR-02 implements request shaping using PF10-decided canonical names and OPS-01 evidence.

Canon touchpoints: PF document titles and sections

* PF10 — HDE Build Notes, Addendum 2.3.  
* PF10 — HDE Build Notes, Addendum 2.6.  
* PF10 — HDE Build Notes, Addendum 2.7.  
* PF09.5 — HDE Build Checklist Fermentation, HDE-FERM007.2.  
* PF05 — HDE CLI-API-Vendor Ref.  
* PF07 — Glow Infrastructure.  
* PF14 — HDE Mechanics Guide.

Drain target: which PF doc must ultimately own the rule

* PF09.5 — HDE Build Checklist Fermentation  
* PF05 — HDE CLI-API-Vendor Ref  
* PF07 — Glow Infrastructure  
* PF14 — HDE Mechanics Guide

Plan impact: which IG items and which PRs or OPS tasks are blocked or affected

* Affected IG items: PF09 Completion Map — HDE-FERM007.2; TI-001.  
* Affected tasks: OPS-01; PR-02; PR-05.  
* No remaining blocker if OPS-01 produces the required fact summary and PR-02 preserves PF10-decided key/header posture.

ADR ID: ADR-002

Type/Tag: ADR / PF10-SUPERSEDED-R1-BLOCKER

Decision/Problem

r1 treated HDE-FERM007.5 closed-rails deterministic shaping proof as blocked on ADR because it depended on request-shaping facts. Latest PF10 Addendum 2.3 decides that HDE-FERM007.5 should remain in scope after OPS discovery and PR prerequisites, not deferred by default.

Bounded PF10 update

HDE-FERM007.5 proof must use PF10-decided canonical key and header posture: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 `HD-Api-Key`, and `HD-Geocode-Key` where required. Closed-rails deterministic shaping proof must verify that v2 shaping uses Bearer auth and v1 shaping uses legacy `HD-Api-Key`.

Options

* Option 1: Keep r1 blocked posture.  
* Option 2: Follow PF10 and sequence OPS discovery, request-shaping PR, and closed-rails proof PR.

Recommendation

Use Option 2\. PR-05 completes closed-rails deterministic shaping and refusal proof after OPS-01 and PR-02, with PF10-decided key/header posture preserved.

Canon touchpoints: PF document titles and sections

* PF10 — HDE Build Notes, Addendum 2.3.  
* PF10 — HDE Build Notes, Addendum 2.6.  
* PF10 — HDE Build Notes, Addendum 2.7.  
* PF09.5 — HDE Build Checklist Fermentation, HDE-FERM007.5.  
* PF09.5 — HDE Build Checklist Fermentation, HDE-FERM008.1.  
* PF14 — HDE Mechanics Guide.  
* PF05 — HDE CLI-API-Vendor Ref.  
* PF07 — Glow Infrastructure.

Drain target: which PF doc must ultimately own the rule

* PF09.5 — HDE Build Checklist Fermentation  
* PF14 — HDE Mechanics Guide  
* PF05 — HDE CLI-API-Vendor Ref  
* PF07 — Glow Infrastructure

Plan impact: which IG items and which PRs or OPS tasks are blocked or affected

* Affected IG items: PF09 Completion Map — HDE-FERM007.5; TI-002.  
* Affected tasks: OPS-01; PR-02; PR-05.  
* No remaining blocker if OPS-01 and PR-02 complete and PR-05 verifies PF10-decided key/header posture.

ADR ID: ADR-003

Type/Tag: ADR / PF10-SUPERSEDED-R1-BLOCKER

Decision/Problem

r1 treated HDE-FERM008.2 PO-only open-rails smoke as blocked on PF07-gap and out of the implementation plan because it required live vendor access, credentials, and PO-only execution. Latest PF10 Addendum 2.2 and Addendum 2.3 decide that open-rails testing is allowed when needed and HDE-FERM008.2 should route as a PO-run OPS open-rails task when in scope and authorized.

Bounded PF10 update

OPS-02 v2 open-rails smoke must use `Authorization: Bearer <redacted>` for v2 chart routes and must not use legacy `HD-Api-Key` for v2. A v2 open-rails failure caused by sending `HD-Api-Key` instead of `Authorization: Bearer` must be classified as a request-shaping/auth-header defect or OPS setup defect, not as vendor unavailability.

Options

* Option 1: Keep r1 blocked posture.  
* Option 2: Follow PF10 and route a bounded PO-run OPS open-rails smoke with secret-safe evidence.

Recommendation

Use Option 2\. OPS-02 executes the bounded open-rails smoke after OPS-01, PR-02, and PR-05. PR-06 binds the evidence with v2 Bearer auth posture preserved and without raw secrets.

Canon touchpoints: PF document titles and sections

* PF10 — HDE Build Notes, Addendum 2.2.  
* PF10 — HDE Build Notes, Addendum 2.3.  
* PF10 — HDE Build Notes, Addendum 2.7.  
* PF09.5 — HDE Build Checklist Fermentation, HDE-FERM008.2.  
* PF14 — HDE Mechanics Guide.  
* PF12 — HDE Schemas and Artifacts.  
* PF19 — Glow QA Guide.  
* PF06 — Epic Process Guide.

Drain target: which PF doc must ultimately own the rule

* PF09.5 — HDE Build Checklist Fermentation  
* PF05 — HDE CLI-API-Vendor Ref  
* PF07 — Glow Infrastructure  
* PF12 — HDE Schemas and Artifacts  
* PF19 — Glow QA Guide  
* PF06 — Epic Process Guide

Plan impact: which IG items and which PRs or OPS tasks are blocked or affected

* Affected IG items: PF09 Completion Map — HDE-FERM008.2; TI-004.  
* Affected tasks: OPS-02; PR-06.  
* Remaining condition: PO must authorize live external execution before OPS-02 runs.

ADR ID: ADR-004

Type/Tag: ADR / CLOSE-STAGE PATH POSTURE

Decision/Problem

PF27-required close-stage baseline surfaces may be listed in implementation plans without turning the plan into a QA runbook. r1 kept close-pack baseline path posture but did not convert it into QA execution steps. Latest PF10 Addendum 2.3 preserves this ADR.

Options

* Option 1: Omit close-stage baseline surfaces from implementation planning.  
* Option 2: Preserve planning-level path posture while keeping QA commands, step logs, and Live QA runbook procedures out of this plan.

Recommendation

Use Option 2\. PR-06 may list and update planning-level acceptance map and doc-delta surfaces while avoiding Live QA runbook content and closeout review content.

Canon touchpoints: PF document titles and sections

* PF10 — HDE Build Notes, Addendum 2.3 ADR-004.  
* PF27 — Canon Plan Templates.  
* PF12 — HDE Schemas and Artifacts.  
* PF06 — Epic Process Guide.  
* PF19 — Glow QA Guide.

Drain target: which PF doc must ultimately own the rule

* PF27 — Canon Plan Templates  
* PF12 — HDE Schemas and Artifacts  
* PF06 — Epic Process Guide  
* PF19 — Glow QA Guide

Plan impact: which IG items and which PRs or OPS tasks are blocked or affected

* Affected IG items: Tokens and Evidence (Acceptance) — Evidence pointers.  
* Affected tasks: PR-06.  
* No blocker created.

ASK OK?

