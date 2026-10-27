---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002-DOCUMENTATION-DELTAS-1
proposed_pf10_number: "2.34 (the next continuous number after addendum 2.33, the last in PF10 v13.8.6 on main; allocation and publication are the Product Owner's)"
authority: Nathan / Product Owner's direct instruction in the continuing HDE-CRD-0002 Isis session, 2026-10-26, quoted under "Approval and source record". No approval prompt produced it, and none is claimed. CL-40 is not a PF10_BUILD_NOTES_ADDENDUM producer; this record is made at the Product Owner's direction, as the records published as 2.3, 2.7, 2.14, 2.17, 2.18 and 2.31 were
producing_session: Isis (Isis-53), continuing Lead Developer for HDE-CRD-0002, https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok
supersedes: nothing
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md (692,581 bytes; SHA-256 e521bf2ea8705862260f4d84100e01dddd78b07b8437751aa419a51b41c1b985), read in full for the CL-40 scan; 2.2, 2.14, 2.17, 2.26, 2.31, 2.32 and 2.33 re-read for this record. Provenance, not a gate
canon_searched_on_main: 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b. Terms "C040-06", "C040-07", "C040-08", "Reader v2", "v=2", "PR07-F01", "build_commit", "close-run family", "documentation/status drainage", "addendum" across docs/pfcanon/
source_scan: docs/ephemeral/HDE-CRD-0002-CL-40-cycle-gap-scan-v1.0.md (candidate item 11 and §6), succeeded by docs/ephemeral/HDE-CRD-0002-CL-40-cycle-gap-scan-v1.1.md
capture_time_utc: 2026-10-26T18:55:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The blocks above the H2 are record-only and are not page text
incorporated_into: not yet; the Product Owner publishes it into PF10
---

**Canon relied on:**

* PF06-Canon-Change-Process-Guide v2.5.4:
  * the paragraph that closes §0.1A: "Agent-authored HDE Build Notes addenda are self-contained canonical records at creation … one H2 with the next number and a descriptive title … only H3 or lower subordinate headings … it does not carry role-addressed publication, routing or record-maintenance instructions";
  * §0.2 "PF09 accountability for task-like work": "documentation/status drainage only, when the item is only a document, board, archive, or status reconciliation action and not implementation, QA, OPS, runtime, evidence, vendor, architecture, or product-behavior work".
* PF04-Canon-HDE-Governance v2.8.7:
  * §9.7.7 "Accountability for task-like future work" and "Required classification" ("Distinguish governed Epic work, governed CRD work, work outside both lanes, and documentation/status drainage");
  * the HDE-EPIC040 Reader v2 rules at lines 2227 and 2247 (C040-07, C040-08) and 4276 to 4277;
  * the `/internal/version` body rule at line 3800.
* PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3: §5 production Reader surface (lines 107 and 2063, `v=2` selects Reader v2).
* PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6: line 1242 (C040-06) and line 1473 (Reader error variant).
* PF14-Canon-HDE-Mechanics-Guide v3.5.8: lines 2199 to 2223 (Reader v1 and v2).
* PF29-Canon-HDE-Users-Guide v1.0.2: lines 97 and 368 (Reader v2).
* PF01-Canon-HDE-Math-Spec v1.3.8: line 118 (Reader v2 public projection).
* HDE Build Notes v13.8.6:
  * 2.14 (optional `AGENTS.md` note, owned there);
  * 2.17 (the ADR defers to HDE Build Notes; its drainage table for the ADR's next revision);
  * 2.26 (FND-017 to FND-021);
  * 2.31 (rule 8, "Close-tooling repair");
  * 2.32 (CL-05 O-1 to O-4);
  * 2.33.
* Candidate CRD Items List (Notion): inclusion criterion 1; item 11.
* An `AGENTS.md` edit needs the Product Owner's explicit instruction: QA-10 triage v1.1 FND-019 ("AGENTS.md needs the Product Owner's explicit instruction") and the repository write boundary.

## 2.34 Documentation-only changes are recorded in HDE Build Notes, not as CRD candidates; HDE-CRD-0002's stale repository documentation is corrected to the delivered state

Timestamp: 102626 18:55 (UTC). Details: Records the Product Owner's rule that a documentation change needing no development is decided in an HDE Build Notes addendum rather than carried as a CRD candidate. It applies the rule to the stale repository documentation that HDE-CRD-0002's records left with no owner (QA-10 triage FND-017 to FND-019; CL-05 O-1, O-2 and O-4; OBS-12), one further stale line found while applying it (D-3), and the S21 ADR's two open lines. For each it states the stale text, the current fact with its evidence on main 0adce9d9, and the corrected statement. Origin: the Product Owner's direction of 2026-10-26 in the continuing HDE-CRD-0002 Isis session, given in answer to the CL-40 scan's question on candidate item 11.

### Approval and source record

* The Product Owner's direction, verbatim: "if something is a documentation change and not something that needs development, then you can create a PF10 build notes addendum to litigate it".  
* It answers the CL-40 cycle gap scan v1.0 §6, which asked whether candidate item 11 ("Repository documentation left stale after HDE-CRD-0002") should stay a CRD candidate or be routed as a documentation change. The scan recorded the item on the Candidate CRD Items List under the Product Owner's 2026-10-12 precedent, while inclusion criterion 1 of that list names no documentation target.  
* Change context: CRD HDE-CRD-0002, closed (CL-C-10 v1.2, CLOSE / CHANGE\_CLOSED; addendum 2.32). Nothing here reopens it.  
* Recorded by Isis (Isis-53), https://claude.ai/code/session\_01NxRhYei7RDGmMPYdKEkpok. No approval prompt produced this addendum.

### Rule

1. **Documentation-only changes.** A change is documentation-only when it alters only repository documentation and needs no code, test, tool, workflow, schema, configuration or governed-evidence change. Repository documentation means prose files that describe the system, such as `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `docs/**` and architecture decision records.  
   * Such a change is not a CRD candidate.  
   * An HDE Build Notes addendum records and decides it, stating for each change the stale text and its location, the current fact with its evidence, and the corrected statement.  
2. **Development keeps its route.** A finding that needs development remains a CRD candidate or PF09 work, as canon assigns it, even when it also touches documentation lines.  
3. **Out of scope.** PF canon documents keep their existing route: HDE Build Notes addenda, then drainage into the permanent PF home. Governed evidence and its writers are unaffected.  
4. **Classification of the correction.** Applying a correction is documentation/status drainage only (Change Process Guide §0.2). Its owner is the Product Owner. An `AGENTS.md` edit needs the Product Owner's explicit instruction.

### Documentation deltas

Evidence is read on main 0adce9d9. Line numbers are those observed there.

| ID | Location | Stale text | Current fact and evidence | Corrected statement |
| :---- | :---- | :---- | :---- | :---- |
| D-1a (FND-017) | docs/ADAPTER\_009.md line 49 | The line "New", alone, after the "Env vars" paragraph | A stray word; no content | The line is removed |
| D-1b (FND-017) | docs/ADAPTER\_009.md lines 189 to 193 | "Body (200): exactly: {"engine\_tag","release\_id","invocation\_tag","build\_commit","emitter\_sha256"}" | The body has six keys in this order: engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id (engine/runtime/identity.py \_FIELDS, lines 26 to 33; identity\_admin, lines 150 to 151; emitted with sort\_keys=False, adapter/http\_reader.py line 1185). HDE Governance: "Body MUST be fixed-schema JSON with exactly these keys (no extras): engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id" | "Body (200): exactly the six keys engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id, in that order" |
| D-1c (FND-017) | docs/ADAPTER\_009.md line 209 | "Override (prod): X-Identity-Override ⇒ 400 JSON; no-store; no ETag" | The override is refused in every environment: adapter/http\_reader.py line 1178 tests the header with no environment condition | "Override: X-Identity-Override ⇒ 400 JSON in every environment; no-store; no ETag" |
| D-1d (FND-017) | docs/ADAPTER\_009.md line 223 | "keys in order: engine\_tag, release\_id, invocation\_tag, build\_commit, emitter\_sha256" | As D-1b | "keys in order: engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id" |
| D-2a (FND-018) | ARCHITECTURE.md lines 10 and 25 | "engine/serializer/canon.py::dumps(obj)->bytes" as the serializer | The function is sercanon(obj, \*, sort\_keys=True) -> bytes (engine/serializer/canon.py line 18), which calls engine/stable/sercanon.py serialize; dumps is "EPIC004-only compatibility alias; remove in next epic" (canon.py lines 30 to 31) | "engine/serializer/canon.py::sercanon(obj, \*, sort\_keys=True) -> bytes (UTF-8, sorted keys by default, compact, exactly one trailing LF); dumps is a compatibility alias" |
| D-2b (FND-018) | ARCHITECTURE.md line 36 | "GET ids-only (a\_id, b\_id); any JSON body → 400" | GET /api/compat/v1 returns 200 {"ok":true,"schema":"v1"} and reads no IDs; a GET with a body returns 400 invalid\_json (engine/http/compat\_handler.py lines 122 to 128) | "GET answers 200 {"ok":true,"schema":"v1"}; a GET with a body answers 400 invalid\_json" |
| D-2c (FND-018) | ARCHITECTURE.md "Routing and mounts" | No statement of the S19 production posture | In a production-like posture, the dev/internal blueprint serves no dev-harness handler and no canon-retired route: each dev-harness route answers its canonical refusal and each retired /ops route the governed not-found, before any handler runs (adapter/http\_reader.py lines 558 to 604; S19-F03, addendum 2.10) | One line under "Routing and mounts" stating that posture |
| D-3 (new) | docs/contracts/reader\_v2\_public\_bytes.md line 6 | "Normative contract: PF10-HDE-Build-Notes, addendum "HDE-EPIC040-PR07-F01 …" (Canon conflict C040-07). While that addendum is active, it is the authoritative source … including the statement in PF05-Canon-HDE-CLI-API-Vendor-Ref that the production Reader refuses v=2" | HDE Build Notes v13.8.6 contains no such addendum. HDE CLI/API/Vendor Ref §5 states that POST /api/reader selects Reader v2 with exactly one v=2. HDE Governance states C040-07's v2 exposure rule | "Normative contract: HDE CLI/API/Vendor Ref §5 (route and request), HDE Governance (the C040-07 Reader v2 exposure rule) and HDE Schemas & Artifacts (the Reader schemas)" |
| D-4 (FND-019) | docs/contracts/reader\_v2\_public\_bytes.md line 8 | "Drainage: as of HDE-EPIC040-PR07, C040-07 has not been drained into PF01-Canon-HDE-Math-Spec, PF04-Canon-HDE-Governance, PF05-Canon-HDE-CLI-API-Vendor-Ref or PF12-Canon-HDE-Schemas-and-Artifacts, nor into … PF14-Canon-HDE-Mechanics-Guide and PF29-Canon-HDE-Users-Guide" | HDE Governance, HDE CLI/API/Vendor Ref and HDE Schemas & Artifacts carry the C040-06/07/08 content; HDE Mechanics Guide and HDE Users Guide state Reader v2; HDE Math Spec states the Reader v2 public projection. Whether its §§6.1 to 6.2 are complete is open (addendum 2.26, FND-021) | "Drainage: C040-07 is drained into HDE Governance, HDE CLI/API/Vendor Ref, HDE Schemas & Artifacts, HDE Mechanics Guide and HDE Users Guide. Whether HDE Math Spec §§6.1 to 6.2 need more is open (HDE Build Notes 2.26, FND-021)" |
| D-5 (FND-019) | AGENTS.md line 134 ("HDE-EPIC040 current posture") | "Canon: C040-06, C040-07 and C040-08 are decided and delivered. PF10 records them and governs until the permanent canon is revised." | As D-3 and D-4: permanent canon carries them, and HDE Build Notes no longer records them | "Canon: C040-06, C040-07 and C040-08 are decided, delivered and drained into HDE Governance, HDE CLI/API/Vendor Ref and HDE Schemas & Artifacts." |
| D-6 (CL-05 O-2) | docs/EVIDENCE\_INDEX.md line 64 | "No Epic close-run family is admitted, and no close-run family of any change exists yet." | audit/qa/hde-crd-0002/close/ holds HDE-CRD-0002's close-run family, nine checks, merged by [\#751](https://github.com/amthorn78/glow-hdengine-v2/pull/751) | "No Epic close-run family is admitted. HDE-CRD-0002's close-run family, audit/qa/hde-crd-0002/close/ (nine checks), is the first." |
| D-7 (CL-05 O-4) | docs/EVIDENCE\_INDEX.md line 57; docs/INDEX.md line 17; docs/prompt\_ecosystem\_management/README.md line 71 | Line 57: "an isolated manual workflow\_dispatch lane … and no automatic pull-request trigger". Line 17: "manual .github/workflows/epic-closeout-validation.yml", with only the v1 source schema named. Line 71: "epic-closeout-validation.yml is workflow\_dispatch only and needs no exclusion" | .github/workflows/epic-closeout-validation.yml runs on pull\_request for the close tooling (the workflow, tools/qa/generate\_epic\_close\_pack.py, schemas/close\_candidate\_source.v\*.json, schemas/epic\_close\_candidate\_source.v\*.json) and for writer close packs under audit/, and on workflow\_dispatch (lines 9 to 28; [\#752](https://github.com/amthorn78/glow-hdengine-v2/pull/752), [\#755](https://github.com/amthorn78/glow-hdengine-v2/pull/755)). Its path filter does not include docs/prompt\_ecosystem\_management/\*\*. schemas/close\_candidate\_source.v2.json exists (HDE-CRD-0002 S21) | Line 57: "an isolated lane that runs on a pull request that changes a writer close pack or the close tooling, and on workflow\_dispatch, with read-only contents permission, exact-ref checkout …". Line 17: drop "manual" and name schemas/close\_candidate\_source.v2.json beside the v1 schema. Line 71: "epic-closeout-validation.yml runs on pull requests that change a close pack or the close tooling, and on dispatch; its path filter does not include this directory, so it needs no exclusion" |
| D-8 (OBS-12) | README.md line 100; docs/EVIDENCE\_INDEX.md line 99; docs/INDEX.md line 43 | The entries for tools/evidence/generate\_hdapi\_v2\_contract\_inventory.py state no ruby requirement; ruby is named only as a pre-push-check prerequisite (README.md line 184) | The generator calls ruby to parse YAML (parse\_yaml\_openapi, tools/evidence/generate\_hdapi\_v2\_contract\_inventory.py lines 2515 to 2520). CI obtains ruby from the runner image (addendum 2.2) | Each entry adds: "requires ruby on PATH (it parses the OpenAPI YAML sources)" |
| D-9 (CL-05 O-1) | docs/adr/hde/close\_pack\_writer\_adr.md line 7 | "under HDE Build Notes addendum 2.31 rule 5" | Published 2.31 numbers the close-tooling repair rule as rule 8; rule 5 in the record is rule 8 in PF10 | "under HDE Build Notes addendum 2.31 rule 8" |
| D-10 (FND-020, LR7-O1) | docs/adr/hde/close\_pack\_writer\_adr.md line 67 | "… and SATISFIED needs every recorded status to be PASS" | Superseded by addendum 2.17 resolution A. 2.17's drainage table already decides this line: "When the ADR is next revised: remove resolution A's superseded clause, and state that the ADR defers to HDE Build Notes" | As 2.17 states; this addendum adds nothing to it |

### Epic, task, and status effects

* HDE-CRD-0002 stays closed. No requirement, work unit, QA result or closure decision changes.  
* Candidate CRD Items List item 11 is a documentation change under rule 1, not a CRD candidate. Its contents are D-1 to D-8 above. Items 9 and 10 need development and stay CRD candidates.  
* D-9 and D-10 are documentation changes to the S21 ADR. D-10 is the item addendum 2.17 already decides.  
* No PF09 row, PF30 record, board state or release changes.

### Required canon drainage

* None into permanent PF canon. The drain targets are the repository documents in the table, as documentation/status drainage.  
* The D-3 and D-4 statements about canon describe canon as it stands. They change no canon.

### Deferred obligations and unresolved work

* D-1 to D-10 are uncorrected in the repository. Owner: the Product Owner, as documentation drainage. D-5 needs the Product Owner's explicit instruction because it edits AGENTS.md. D-9 and D-10 apply at the ADR's next revision (addendum 2.17).  
* CL-40 — Scan for PF09 Gaps and CRD Candidates — 100926.1 states that it never prepares a PF10 addendum. Under rule 1, a documentation-only finding in a later scan has a route the prompt does not name. Owner: the GCFPE-MGMT-10 maintenance owner.  
* FND-021 (whether HDE Math Spec §§6.1 to 6.2 hold the complete C040 content) stays open with the Product Owner (addendum 2.26).

### Scope boundaries and nonclaims

* Establishes no code, test, tool, workflow, schema, configuration or governed-evidence change, and no QA verdict, acceptance, PF09 or PF30 movement, board change, deployment or closure change.  
* Edits no PF canon document and no repository document. The corrections stand as decided text until drained.  
* The current facts are read from main 0adce9d9; a later change to the cited code or canon makes the matching corrected statement a fresh question.

### Evidence anchors

* Repository: main 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b. The cited files and lines are in the table.  
* Records:  
  * QA-10 change audit triage v1.1 (FND-017 to FND-021);  
  * CL-05 close mutation set result v1.0 §11 (O-1, O-2, O-4);  
  * the WU-PR-01 plan v1.1 (OBS-12, line 1051);  
  * CL-40 cycle gap scan v1.0 (item 11, §6) and v1.1.  
* PR: [\#759](https://github.com/amthorn78/glow-hdengine-v2/pull/759) carries the scans and this record.

### Relationship to existing HDE Build Notes guidance

* Applies addendum 2.17's ADR drainage (D-10) and cites 2.31's published rule numbering (D-9). It neither amends nor supersedes them.  
* Adds the documentation-only route of rule 1 beside addendum 2.11's business-case and real-input rules, which govern development work and are unchanged.  
* Numbering: PF10 v13.8.6 on main (SHA-256 e521bf2ea8705862260f4d84100e01dddd78b07b8437751aa419a51b41c1b985) runs through 2.33, so this addendum is 2.34.
