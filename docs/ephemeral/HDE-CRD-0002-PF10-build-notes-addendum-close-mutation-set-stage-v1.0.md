---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: CLOSE-MUTATION-SET-STAGE-1
proposed_pf10_number: "2.31 (the next continuous number after addendum 2.30, the last in PF10 v13.8.2 on main; allocation and publication are the Product Owner's)"
authority: Nathan / Product Owner's direct instructions in the continuing HDE-CRD-0002 Isis session, 2026-10-26, quoted under "Approval and source record". The Product Owner named Isis to record it and to write the stage's prompt. No approval prompt produced it, and none is claimed
producing_session: Isis (Isis-53), continuing Lead Developer and terminal closure authority for HDE-CRD-0002, https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok
supersedes: nothing on main. An earlier draft (docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-close-pack-process-gap-v1.0.md on pull request #748) was rejected by the Product Owner and closed unmerged
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.2.md (636,840 bytes; SHA-256 d1fcffecf95a4c236cb27f95b3056a2c660d3c99e2418ed89f359c312d0f5bca); index lines 2.10 to 2.30 and addenda 2.13, 2.15, 2.17 and 2.24 read for this record. Provenance, not a gate
canon_searched_on_main: 58a27859495c21d16d8d5761be1104e502bd56d1. Terms "close mutation set", "close PR", "Close Gate", "close-pack", "Not a PR", "Ops task", "feedback-dependency" across docs/pfcanon/; the GCFPE 100926.1 closure and escalation prompts; the graph parts of QA-120, CL-C-10 and CL-E-10
stage_prompt: CL-05 — Prepare and Publish the Close Mutation Set — 102626.1 (candidate), https://app.notion.com/p/4054590a05eb8155b301e2cb6dec31d5 (a child page of the GCFPE Modification Backlog)
gcfpe_feedback: GCFPE Modification Backlog MB-030, with a dated note on MB-027
capture_time_utc: 2026-10-26T02:50:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The blocks above the H2 are record-only and are not page text
incorporated_into: not yet; the Product Owner publishes it into PF10
---

**Canon relied on:**

* PF06-Canon-Change-Process-Guide v2.5.4, read in full at these places:
  * §0.1A: an agent-authored addendum is one H2 with the next number and only H3 or lower headings;
  * §0.2 "Policy and principles": the "Not a PR" paragraph, and the OPS-01 packaging run of "already-produced close-pack artifacts";
  * §1.0.6;
  * §3.5.1: the Close Gate, "Only the close mutation set is required to carry the full close pack", the feedback-free terminal lifecycle and the exceptional closure record;
  * §3.5.2.1 to §3.5.2.4;
  * §3.5.4.
* PF27-Canon-Plan-Templates v2.0.5 §3 "Ops Task Record (Template)": "Definition", "Execution authority (normative)" and "Not a PR (normative)", read in full.
* PF04-Canon-HDE-Governance v2.8.7:
  * §2.0.19;
  * §9.1 item 2, "Not a PR";
  * the closeout-record list.
* PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6: "Close-pack artifacts" and "Change-container compatibility (normative)".
* PF19-Canon-Glow-QA-Guide v3.0.6 §3.1.3.
* HDE Build Notes v13.8.2:
  * 2.13;
  * 2.15, including "the feedback-dependency refusal kept, and requirement text bound by reference";
  * 2.17;
  * 2.24.
* GCFPE 100926.1, both pages read in full:
  * CL-C-10 (page state 2026-10-12T02:29:13.994Z): "Execute" and "Next step and recovery";
  * ESC-30 (page state 2026-10-12T02:29:51.552Z).
* Graph parts `docs/graph/parts/prompts/QA-120.json`, `CL-C-10.json` and `CL-E-10.json`: the edges and branch IDs.
* `docs/adr/hde/close_pack_writer_adr.md`: "Decision" and "Stated limits".

**First run (record-only, not page text).** HDE-CRD-0002 is CL-05's first run. Nathan starts it in a standalone session with the stage page and the change ID.

* **Known close-tooling defect B-4.** Isis rehearsed the close in scratch clones at `58a27859`, plus the CL-C-10 v1.0 record. Nothing from those clones was pushed.
  * With the writer as merged, T2 refuses with `EPIC_CLOSE_PACK_ERROR:SOURCE_SCHEMA_INVALID`.
  * Validating the same source with `jsonschema` gives one error: `['evidence_inputs', 14, 'path'] 'audit/qa/hde-crd-0002/checks/qa-03-attestation-debian/primary.log' should not be valid under {'$ref': '#/$defs/feedback_dependency'}`.
* **Cause.** Three rules combine:
  * the schema types each `evidence_inputs[].path` as "not `feedback_dependency`" (`schemas/close_candidate_source.v2.json`, blob `b3b774233ad2`);
  * the writer applies the same pattern to every causal string (`_require_feedback_free_values_v2` in `tools/qa/generate_epic_close_pack.py`, blob `c1ef3fca9221`);
  * a `MET` criterion must bind the primary of a `PASS` check whose QA-plan mapping names it, and approved QA Plan v1.3 maps S06 only to check 3, `qa-03-attestation-debian`.

  So no source reaches `SATISFIED`.
* **Nothing else blocked the close.** A narrow scratch exemption for the change's own QA-primary path form made every other step pass:
  * T2 to T6 and the close-run publication;
  * the closeout workflow's checks under a requirements-only install;
  * the writer's check with `jsonschema` only;
  * an idempotent re-run.

  The evidence-lane and qa-lane selections also passed on the final commit (134 and 488 tests), and the close-only diff selected the CI lanes `evidence` and `release`. The exemption was diagnostic, not a design.
* **Corrections CL-05's run carries for CL-C-10 v1.0.** `follow_ups` must be empty for `SATISFIED` (v1.0 §8 R-1 listed "the follow-ups"). B-4 supersedes v1.0's statements that nothing failed and that the writer was ready. CL-C-10 records both when the run returns to it.
* **TypeSafe reading for the first CL-05 session.**
  * Action sent (v8.2): "In a dedicated session, run a new close stage for an already QA-passed change request of 22 requirements: rehearse its close in a throwaway clone, fix one known defect in the close-pack writer (a refused evidence path; about three files: a schema, the writer and its tests) in its own pull request with tests, then author the close-candidate source and two short ledgers from the records, run the governed writer, the evidence-index updater, seven read-only validators and the close-run publisher in a fixed sequence under closed rails, and publish a second pull request for hosted CI and one manual validation workflow. A written step list and a reproduced failure exist; no live run against a provider occurs; the closure decision reviews the result independently after the Product Owner merges."
  * **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.30 (confidence 0.66). Rung probabilities: low 0.00, medium 0.10, high 0.51, extra high 0.37, max 0.02, ultracode 0.00.
  * Model probabilities: Fable 5.1 0.01, Opus 5.5 0.98, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.97).
  * Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.005, Fable 5.1 at extra high 0.004, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.098, Opus 5.5 at high 0.500, Opus 5.5 at extra high 0.363, Opus 5.5 at max 0.020, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.005, Sonnet 5.5 at extra high 0.004, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  * **Flags: boundary between extra high and high.** Sent 2026-10-26T02:47:18Z.
  * Detail: HTTP 200 in 0.57 s; 5500 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5.
  * Run once with the installed skill's request v8.2, session kind `review`, label "HDE-CRD-0002 CL-05 close stage, first run (candidate 102626.1)". No Notion row was written. Nathan picks the cell; his pick is not stated.

## 2.31 The change flow gains a close-mutation-set stage, CL-05, between QA-120 and the closure decision; it is Dev work and repairs its own close tooling

Timestamp: 102626 02:50 (UTC). Details: Records the Product Owner's finding of 2026-10-26: the close-pack machinery is built, but nothing in the prompt ecosystem, PF canon or the role set produces a change's close mutation set. It records his direction that the missing process be reusable and become part of the change flow, as a stage that repairs its own close tooling. The stage's prompt is written in Notion as a candidate for the next GCFPE Modification. Origin: the continuing HDE-CRD-0002 Isis session (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok), after CL-C-10 v1.0 returned DO_NOT_CLOSE for the missing close mutation set.

### Approval and source record

* The Product Owner's words:
  * "the gap seems to be that the close pack machinery is now built, but there is no actual canonical process for creating in either in the prompt ecosystem, canon, or anyone else. Record this as a pf10 build notes addendum, GCFPE feedback, and then create a task to create the close pack. The prompt should be created by you (Isis). I will need you to determine if this is an Ops or Dev task first. Either way, it will need to return to CL-C-10."
  * On a draft that routed the close through ESC-30: "No, I don't want to do it this way. This will just loop back into the change flow. This needs to be a new process."
  * "'reusable' but It needs to become PART of the change flow, that is what I wanted the PF10 addendum and GCFPE feedback to reflect."
  * On who fixes a close-tooling defect: "The process fixes it".
  * "You can write it in Notion as a new prompt, it can be used as a candidate when I run the next modification to the GCFPE".
  * "the new prompt can just run in a standalone session".
* Recorded by Isis at the Product Owner's direction. No approval prompt produced this addendum.
* Where this addendum conflicts with an earlier addendum, an in-flight change document or a prompt's routing, it governs for the scope below.

### Retained decisions and requirements

1. **The gap.** These exist:
   * the generic close-pack writer `tools/qa/generate_epic_close_pack.py` and its v2 schema (addenda 2.15 and 2.17);
   * the CRD close-run family, published by `publish_crd_close_run_family`;
   * the manual closeout validation workflow (addendum 2.13).

   But no prompt, PF section or role produces a change's close mutation set with them. PF06 §3.5.1 and §3.5.2 require the close mutation set and the close PR, but name no producing stage, entry or owner. In release 100926.1:
   * CL-C-10 and CL-E-10 route DO_NOT_CLOSE only to an existing owner or to ESC-30;
   * QA-120 defers the close-pack measure;
   * no prompt authors a close-candidate source.

   HDE-EPIC038 and HDE-EPIC040 closed by exceptional closure, and HDE-CRD-0002's closure decision had no next prompt.
2. **A new stage, part of the change flow.** CL-05 — Prepare and Publish the Close Mutation Set serves every Epic and CRD.
   * **Entries:**
     * QA-120's final QA Report with `verdict: PASS`;
     * a closure decision's DO_NOT_CLOSE whose return work is the close mutation set (missing, incomplete or defective).
   * **Exit:** the closure decision (CL-C-10 or CL-E-10), after the Product Owner merges the close pull request.
   * **What it owns:**
     * the close mutation set: the close pack, its two ledgers, the same-run close evidence, and their Index and Mirror registration;
     * any repair of the close tooling that the close needs.
   * **What it never does.** It never reopens implementation, QA or the closure decision. Close-tooling repair uses no ESC, RS or PR-10 to PR-40 stage.
3. **Dev, not Ops.** CL-05 is a PR work unit. It writes tracked repository state through the canonical writers, and its work lands by the Product Owner's merge:
   * PF06 §3.5.2.1: "The close PR MUST include the epic close-pack (canonical filenames)";
   * PF06 §3.5.2.3: the Index and Mirror trio "in the same authorized mutation set".

   An Ops task "requires privileged access to systems outside the repository", and "Ops tasks are not repository PRs" (PF27 §3; PF06 §0.2; PF04 §9.1). An OPS-01 run only packages "already-produced" close-pack artifacts (PF06 §0.2).
4. **Authority and actor.**
   * The Product Owner's invocation of CL-05 for a change authorizes that change's close mutation set and any close-tooling repair it needs, and is the Proceed for both.
   * It runs as a standalone top-level session that the Product Owner starts with the stage page and the change ID. It needs no handoff to start and resolves its inputs from the change's records.
   * The closure authority (Isis) judges its result at the closure decision. The Product Owner alone merges.
5. **Close-tooling repair.**
   * **What counts as a defect.** CL-05 first rehearses the close in a throwaway clone. A close-tooling defect is one where the tools refuse or fail on correct inputs, or lack an admission the change needs.
   * **How it is repaired.** CL-05 repairs it in its own pull request:
     * the smallest change to the close-tooling surface: the writer, its source schemas, the close-run and close-pack admission in the canonical updater, the closeout workflow and their tests;
     * owner tests that reproduce the defect and prove the fix;
     * an amendment to the close-pack ADR when the fix changes a decision the ADR records.
   * **Narrowing a recorded rule.** A repair may narrow a close-tooling rule that the ADR or an earlier HDE Build Notes addendum records, but only where that rule refuses the change's own governed evidence of record. It keeps the rule's purpose and records the narrowing and its basis. Example: 2.15's "the feedback-dependency refusal kept", which refuses HDE-CRD-0002's QA check 3 primary path.
   * **Limits.** A repair never changes approved QA evidence, product code or PF canon.
6. **Interim operation.** Until a GCFPE Modification installs CL-05:
   * the candidate page runs at the Product Owner's direct invocation: https://app.notion.com/p/4054590a05eb8155b301e2cb6dec31d5;
   * QA-120 `PASS`, and a closure decision's DO_NOT_CLOSE for the close mutation set, are read as routing to it;
   * a change's Implementation Plan needs no change-local Close Gate work unit. Where a Plan has one, as HDE-CRD-0002's WU-PR-07 T0 to T7, CL-05 performs it.
7. **HDE-CRD-0002.**
   * CL-05's first run performs CL-C-10 v1.0's return work and repairs close-tooling defect B-4.
   * Its result returns to CL-C-10. That decision records B-4, which supersedes CL-C-10 v1.0's "Nothing failed".

### Epic, task, and status effects

* No status change. HDE-CRD-0002 stays open under CL-C-10 v1.0 (DO_NOT_CLOSE).
* No PF09, PF30 or board row changes.
* Implementation Plan v1.1 is not edited. CL-05 performs its §7 WU-PR-07 T0 to T7.

### Required canon drainage

Owner of each: the Product Owner, through canon maintenance.

* **Change Process Guide** §3.5.1 and §3.5.2: name the close-mutation-set stage as part of the change flow, with its entries, its exit to the closure decision and its ownership of close-tooling repair. State that it is Dev, and that an Ops run only packages or proves already-produced artifacts.
* **Glow QA Guide** §3.1.3: state that the close mutation set precedes the closure decision, outside the post-closure drainage rule.
* **Plan Templates:** a close-mutation-set task template beside the Ops Task Record.

### Deferred obligations and unresolved work

* **GCFPE installation.** Install CL-05 as a release member with the routing its installation notes give:
  * QA-120 `pass_crd` and `pass_epic` go to CL-05;
  * CL-C-10 and CL-E-10 gain a DO_NOT_CLOSE branch back to CL-05 for the close mutation set, and read it as an input;
  * a close-tooling defect is CL-05's to repair, not ESC-30's;
  * a graph part, registry entry and catalog row.

  Tracked as MB-030, with MB-027. Owner: the GCFPE-MGMT-10 maintenance owner, at the Product Owner's next Modification.
* **B-4 repair:** CL-05's first run, for HDE-CRD-0002.
* **WU-PR-07 measure.** Its "first attempt" clause cannot be met by the writer as accepted at #668; the measure is observed on the repaired writer. Owner: the Product Owner.
* **PF10 numbering and publication:** the Product Owner.

### Scope boundaries and nonclaims

* This addendum changes no selected prompt, skill, AGENTS.md, code, test, schema, graph part or permanent PF document, and edits no in-flight record.
* The CL-05 page is a candidate. It is not a selected release member until the register selects it.
* This addendum is not a QA verdict, acceptance, closure decision or Plan approval. It authorizes no close mutation set; the Product Owner's invocation of CL-05 does.

### Evidence anchors

* **Direction:** the Product Owner's words above, 2026-10-26, session https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok.
* **Stage and feedback:**
  * the CL-05 candidate page, https://app.notion.com/p/4054590a05eb8155b301e2cb6dec31d5;
  * the GCFPE Modification Backlog's MB-030 and MB-027.
* **Records:**
  * `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md` (pull request #747);
  * `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md`;
  * `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md`;
  * `docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md`.
* **Repository state** on main `58a27859`: no `audit/HDE-CRD-0002_*`, no `audit/docdeltas/hde-crd-0002_*` and no `audit/qa/hde-crd-0002/close/`.

### Relationship to existing HDE Build Notes guidance

* **Addenda 2.13, 2.15 and 2.17.** This addendum adds to them who produces a change's close mutation set and how the result returns. It keeps their rules, except that a CL-05 repair may narrow one as rule 5 limits.
* **Addendum 2.15's drainage statement.** It stays consistent: the close mutation set is a closure prerequisite, and canon drainage is not.
