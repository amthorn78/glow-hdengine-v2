---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: CLOSE-MUTATION-SET-PROCESS-GAP-1
proposed_pf10_number: "2.31 (the next continuous number after addendum 2.30, the last in PF10 v13.8.2 on main; allocation and publication are the Product Owner's)"
authority: Nathan / Product Owner's direct instruction in the continuing HDE-CRD-0002 Isis session, 2026-10-26, quoted under "Approval and source record". The Product Owner named Isis to record it. No approval prompt produced it, and none is claimed; CL-C-10, the stage in progress, is not a PF10_BUILD_NOTES_ADDENDUM producer
producing_session: Isis (Isis-53), continuing Lead Developer and terminal closure authority for HDE-CRD-0002, https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.2.md (636,840 bytes; SHA-256 d1fcffecf95a4c236cb27f95b3056a2c660d3c99e2418ed89f359c312d0f5bca); index lines 2.10 to 2.30 and addenda 2.13, 2.15, 2.17, 2.24 read for this record. Provenance, not a gate
canon_searched_on_main: 58a27859495c21d16d8d5761be1104e502bd56d1. Terms "close mutation set", "close PR", "Close Gate", "close-pack", "Not a PR", "Ops task" across docs/pfcanon/; the HDE Build Notes index; the GCFPE 100926.1 closure and escalation prompts
capture_time_utc: 2026-10-26T02:30:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The "Canon relied on" block above the H2 is record-only and is not page text
incorporated_into: not yet; the Product Owner publishes it into PF10
---

**Canon relied on:**

* PF06-Canon-Change-Process-Guide v2.5.4: §0.1A (one H2 per addendum, next continuous number; HDE Build Notes records material decisions and temporary pre-drain authority); §0.2 "Policy and principles" (the "Not a PR" paragraph; the OPS-01 closeout packaging run, "already-produced close-pack artifacts"); §1.0.6; §3.5.1 (Close Gate; "Only the close mutation set is required to carry the full close pack"; exceptional closure record); §3.5.2.1 to §3.5.2.4; §3.5.4. Read in full.
* PF27-Canon-Plan-Templates v2.0.5: §3 "Ops Task Record (Template)", "Definition", "Execution authority (normative)" and "Not a PR (normative)", read in full; the closeout-automation lane rule ("Administrative closeout work MUST NOT become ordinary required PR CI solely to create, refresh, normalize, package, index, mirror, hash, sign, transfer, or validate an epic close report, token matrix, Doc Delta package, close pack, historical receipt, closeout ledger, acceptance package, or other administrative proof.").
* PF04-Canon-HDE-Governance v2.8.7: §2.0.19 (close-pack presence is a baseline closure artifact requirement); §9.1 item 2 ("Not a PR").
* PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6: "Close-pack artifacts" and "Change-container compatibility (normative)" ("This generic close-pack contract supports both Epic/PF09 and CRD/PF30 work").
* PF19-Canon-Glow-QA-Guide v3.0.6 §3.1.3 (drainage and administration follow closure; it does not cover the close mutation set).
* HDE Build Notes v13.8.2: 2.13, 2.15 and 2.17 (the S21 writer and the close-run family); 2.24 (FND-001 measure (2)).
* GCFPE 100926.1: CL-C-10 (page state 2026-10-12T02:29:13.994Z), "Execute" and "Next step and recovery"; ESC-30 (2026-10-12T02:29:51.552Z), "Required inputs"; both read in full.
* The cases: docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md and docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md (read in full); docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md and v1.1; docs/ephemeral/HDE-CRD-0002-CLOSE01-close-rehearsal-record-v1.0.md.

## 2.31 Producing a change's close mutation set has no canonical process, prompt or owner; until one exists, the closure authority writes a one-time Dev task prompt for it, and its result returns to the closure decision

Timestamp: 102626 02:30 (UTC). Details: Records the Product Owner's finding of 2026-10-26 that the close-pack machinery is built but nothing in the prompt ecosystem, PF canon or the role set produces a change's close mutation set. It records the determination that the work is Dev (a PR work unit), not Ops. It sets the interim treatment: a one-time task prompt written by the closure authority, whose result returns to the closure decision. It applies the treatment to HDE-CRD-0002. Origin: the Product Owner's direction in the continuing HDE-CRD-0002 Isis session (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok), after CL-C-10 v1.0 returned DO_NOT_CLOSE for the missing close mutation set.

### Approval and source record

* The Product Owner's words: "the gap seems to be that the close pack machinery is now built, but there is no actual canonical process for creating in either in the prompt ecosystem, canon, or anyone else. Record this as a pf10 build notes addendum, GCFPE feedback, and then create a task to create the close pack. The prompt should be created by you (Isis). I will need you to determine if this is an Ops or Dev task first. Either way, it will need to return to CL-C-10."  
* Recorded by Isis at the Product Owner's direction. No approval prompt produced this addendum. The GCFPE feedback is GCFPE Modification Backlog entry MB-030.  
* Where this addendum conflicts with an earlier addendum or an in-flight change document, it governs for the scope below.

### Retained decisions and requirements

1. **The gap.** These exist:
   * the generic close-pack writer `tools/qa/generate_epic_close_pack.py` with schema `schemas/close_candidate_source.v2.json` (S21; addenda 2.15 and 2.17);
   * the post-verdict close-run family published by `tools.evidence.update_evidence_index.publish_crd_close_run_family`;
   * the manual closeout validation workflow `.github/workflows/epic-closeout-validation.yml` (addendum 2.13);
   * for HDE-CRD-0002, the approved T0 to T7 sequence of Implementation Plan v1.1 §7 WU-PR-07.

   No canonical process produces a change's close mutation set with them:
   * **Prompt ecosystem (GCFPE 100926.1).**
     * CL-C-10 and CL-E-10 route a DO_NOT_CLOSE only to "the existing owner for already-authorized ordinary correction" or to ESC-30.
     * QA-120 names the close-pack measure as later work.
     * No PR or Ops prompt takes a closure finding, and no prompt authors a close-candidate source.
     * MB-027 recorded this for Epics; 100926.1 has not closed it.
   * **PF canon.**
     * PF06 §3.5.1 and §3.5.2 require the close mutation set, the close PR and its contents. They name no producing stage, entry point or owner.
     * PF19 §3.1.3 covers drainage and administration after closure, not the close mutation set.
     * PF27 has no close-mutation-set task template.
   * **Roles.** No role owns it. HDE-CRD-0002's Plan names an actor only for that change: "a dedicated top-level close PR session acting under the Product Owner's authorization of that close PR", or the Product Owner.
   * **Effect.** HDE-EPIC038 and HDE-EPIC040 closed by exceptional closure. HDE-EPIC040 first needed a one-time task prompt. HDE-CRD-0002's CL-C-10 v1.0 returned DO_NOT_CLOSE with no prompt to run its return work.
2. **Dev, not Ops.** A change's close mutation set is a PR work unit (Dev). It writes tracked repository state through the canonical writers and lands by the Product Owner's merge:
   * PF06 §3.5.2.1: "The close PR MUST include the epic close-pack (canonical filenames)";
   * PF06 §3.5.2.3: the Index and Mirror trio "in the same authorized mutation set".

   An Ops task is "any work item that requires privileged access to systems outside the repository" (PF27 §3), and "Ops tasks are not repository PRs" (PF27 "Not a PR (normative)"; PF06 §0.2; PF04 §9.1). An OPS-01 run only packages "already-produced" close-pack artifacts, and an OPS-02 run is provenance-only (PF06 §0.2, §3.5.2.1). Neither produces the close mutation set. It belongs to the phase block the Plan assigns to the Close Gate; for HDE-CRD-0002 that is Distillation, which holds S21.
3. **Interim treatment.** Until canon and the prompt ecosystem name a route, these rules apply when a closure decision returns DO_NOT_CLOSE because the close mutation set is missing:
   * The closure authority (Isis) writes a one-time task prompt for it under `docs/ephemeral/`, in the form of `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md`.
   * The Product Owner's invocation of that prompt is the authorization of the close mutation set and the Proceed for that one work unit. Its vehicle is a dedicated top-level session.
   * The task's result returns to the closure decision (CL-C-10 or CL-E-10), never directly to CL-20. A blocker it meets returns to the Product Owner as its terminal result.
   * A product defect found while preparing or running it goes through the closure prompt's own route for a substantive new remedy: ESC-30, ESC-40, normal delivery, verification and the closure return.
   * The prompt is not a GCFPE release member and creates no standing route.
4. **HDE-CRD-0002.**
   * The task prompt is `docs/ephemeral/HDE-CRD-0002-CLOSE01-close-mutation-set-task-prompt-v1.0.md`, work unit HDE-CRD-0002-CLOSE01 (Dev; Distillation). It returns to CL-C-10.
   * A rehearsal of it on the real records (`docs/ephemeral/HDE-CRD-0002-CLOSE01-close-rehearsal-record-v1.0.md`) found closure finding B-4: the S21 writer refuses the primary path of QA check 3, the only check mapped to S06, so the close pack cannot reach SATISFIED.
   * Under rule 3, CL-C-10 v1.1 routes B-4 to ESC-30. The task prompt runs only after the remedy is merged, accepted and verified as ESC-40 requires.

### Epic, task, and status effects

* No status change. HDE-CRD-0002 stays open: CL-C-10 v1.1, DO_NOT_CLOSE, CLOSURE_RETURNED_FOR_REMEDIATION.  
* New work unit HDE-CRD-0002-CLOSE01, defined by its task prompt. Implementation Plan v1.1 is not edited. CLOSE01 performs its §7 WU-PR-07 T0 to T7, and this addendum overlays the Plan's work-unit list for that scope only.  
* No PF09, PF30 or board row changes.

### Required canon drainage

* **Change Process Guide** §3.5.1 and §3.5.2: name the close mutation set's producing stage and owner (a PR work unit), its entry from the closure decision's DO_NOT_CLOSE and its return to that decision. State that it is not post-closure administration, and that an Ops run only packages or proves already-produced artifacts. Owner: the Product Owner, through canon maintenance.  
* **Plan Templates:** a close-mutation-set task template beside the Ops Task Record. Owner: the Product Owner.  
* **Glow QA Guide** §3.1.3: state that the close mutation set precedes the closure decision and is not covered by the drainage rule. Owner: the Product Owner.

### Deferred obligations and unresolved work

* **Prompt route:** MB-030 in the GCFPE Modification Backlog, which also records that 100926.1 leaves MB-027 open. Owner: the GCFPE-MGMT-10 maintenance owner.  
* **Proposed, not decided: rehearse the close before QA and before closure.**
  * Before a change's QA executes, and again before its closure decision, run its close mutation set in a throwaway clone against its real QA plan and evidence.
  * HDE-CRD-0002's B-4 stayed invisible until that was done. The QA check IDs were written after the writer merged, and no review compared them with the writer's text refusal.
  * Owner of the decision: the Product Owner, with GCFPE-MGMT-10 for the prompts.
* **B-4 remedy:** ESC-30 (Thoth), then ESC-40 (Isis), which produces its own addendum on approval.  
* **WU-PR-07 measure:** the measure's first-attempt clause cannot be met by the writer as accepted at #668 (CL-C-10 v1.1 §4). Owner: the Product Owner.  
* **PF10 numbering and publication:** the Product Owner.

### Scope boundaries and nonclaims

* This addendum changes no prompt, skill, AGENTS.md, code, test, schema or permanent PF document, and edits no in-flight record.  
* It creates no standing route: rule 3 is interim.  
* It is not a QA verdict, acceptance, closure decision, Plan approval or Proceed. It authorizes no close mutation set: the Product Owner's invocation of a task prompt does.

### Evidence anchors

* **Direction:** the Product Owner's words above, 2026-10-26, session https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok.  
* **Prompts:** CL-C-10 and ESC-30, release 100926.1, at their page states above. The GCFPE Modification Backlog's MB-027 and MB-030.  
* **Records:**
  * `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md` and `v1.1.md`;
  * `docs/ephemeral/HDE-CRD-0002-CLOSE01-close-rehearsal-record-v1.0.md`;
  * `docs/ephemeral/HDE-CRD-0002-CLOSE01-close-mutation-set-task-prompt-v1.0.md`;
  * `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md`;
  * `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md`;
  * `docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md`.
* **Repository state** on main `58a27859`: no `audit/HDE-CRD-0002_*`, no `audit/docdeltas/hde-crd-0002_*` and no `audit/qa/hde-crd-0002/close/`.

### Relationship to existing HDE Build Notes guidance

This addendum adds who produces a close mutation set, and how its result returns, to addenda 2.13, 2.15 and 2.17, which define the tools and HDE-CRD-0002's close-run family. It changes none of their rules. It is consistent with 2.15's statement that undrained canon is not a closure prerequisite: the close mutation set is a closure prerequisite, and canon drainage is not.
