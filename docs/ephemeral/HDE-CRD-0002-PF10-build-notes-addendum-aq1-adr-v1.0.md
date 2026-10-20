---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002-WU-PR-07-AQ1-ADR-1
proposed_pf10_number: "2.15 (next continuous number after addendum 2.14, which PF10 v13.6.5 on pull request #668's head carries; allocation and publication are the Product Owner's)"
authority: Nathan / Product Owner's AQ-1 decision, "Approve with changes", given on 2026-10-20 in the continuing HDE-CRD-0002 Implementation Agent session after the IA's ADR review, and his direction in the same session to "create a PF10 build notes addenda to canonize decision". No approval prompt produced this addendum, and none is claimed
decision_record: docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md (the IA's review, findings, conditions C-1 to C-7 and redlines R-1 to R-4)
producing_session: continuing whole-change HDE-CRD-0002 Implementation Agent session, https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.5.md on #668's branch (addenda 2.11, 2.13 and 2.14; index and the last addendum number); main carries v13.6.3. Provenance, not a gate
capture_time_utc: 2026-10-20T23:40:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The "Canon relied on" block above the H2 is record-only and is not page text
incorporated_into: not yet; the Product Owner publishes it into PF10
---

**Canon relied on:**

* PF06-Canon-Change-Process-Guide v2.5.4: §0.1A (addendum form); §1.0.5 "Canon changes"; §3.5.1 ("Exceptional closure record"); §3.5.2.1 "Close-pack files"; §3.5.4 "ADR block in the close-pack (all epics)".
* PF04-Canon-HDE-Governance v2.8.7: §2.0.19 ("Close-pack baseline artifacts", "Close report minimal content (normative)", "Close-pack manifest `key_outputs` shape (normative)"); §9.7.3 (ADRs are Product Owner-owned; agents draft).
* PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6: §1.2 "Close-pack artifacts" and "Change-container compatibility (normative)"; §8.17 "New standardized evidence families (MUST)" and "Current-state evidence (normative)"; §8.17.1.
* PF19-Canon-Glow-QA-Guide v3.0.6: §3.4.3; "Close-pack truthfulness and same-run execution (normative)"; "Close report requirements (validator-bound; mechanical)".
* PF14-Canon-HDE-Mechanics-Guide v3.5.8: §37.2, §37.3.
* PF27-Canon-Plan-Templates v2.0.5, "Canon precedence for template use".
* PF10-HDE-Build-Notes v13.6.5: addenda 2.11 (rules 3 to 8), 2.13, 2.14.
* In-flight: Specification v1.1-approved (S21); Implementation Plan v1.1 §7 WU-PR-07, §9 item 5, §13 AQ-1; WU-PR-07 instruction v1.0 ID-5, ID-8, ID-12; the AQ-1 proposal v1.0 and the ADR at #668 head `45e4cef`; the IA's ADR review v1.0.

## 2.15 HDE-CRD-0002 WU-PR-07: the Product Owner approves the S21 close-pack writer ADR with changes, and the close-run evidence family is introduced

Timestamp: 102026 23:40 (UTC). Details: Records the Product Owner's AQ-1 decision on the S21 architecture decision record, `docs/adr/hde/close_pack_writer_adr.md`, of work unit WU-PR-07 of the approved HDE-CRD-0002 Implementation Plan v1.1. The record is approved with changes. This addendum also introduces the post-verdict close-run evidence family that HDE Schemas & Artifacts §8.17 requires a Build Notes addendum to introduce. Origin: the AQ-1 proposal v1.0 from the WU-PR-07 PR-35 session, the Implementation Agent's review of it, and the Product Owner's choice in the Implementation Agent session on 2026-10-20. Evidence: the review's checks of the ADR, the v2 writer and canon at pull request [amthorn78/glow-hdengine-v2\#668](https://github.com/amthorn78/glow-hdengine-v2/pull/668)'s head `45e4cef`.

### Decision and approval status

* **Decision.** AQ-1 is decided: the S21 ADR is **approved with changes**. The decision is the Product Owner's (Implementation Plan v1.1 §13; HDE Governance §9.7.3). It satisfies Change Process Guide §1.0.5's requirement of an approved ADR for S21's canon change, on condition that changes C-1 to C-4 below land in pull request #668 before it merges.
* **What is approved.** The design of the ADR at #668 head `45e4cef`:
  * one writer at `tools/qa/generate_epic_close_pack.py` with a second, closed source schema `schemas/close_candidate_source.v2.json` for Epic (`HDE-EPICNNN`) and CRD (`HDE-CRD-NNNN`) identities, v1 unchanged;
  * CRD paths of record `audit/HDE-CRD-NNNN_close_report.md` and `audit/HDE-CRD-NNNN_MANIFEST.json`, with the directory form `hde-crd-nnnn`;
  * the v2 report and manifest rendered only from tracked inputs, with a `key_outputs` map of path strings;
  * the feedback-dependency refusal kept, and requirement text bound by reference;
  * the post-verdict close-run family (below);
  * absent-tolerant CRD close-pack Index rows;
  * the dependency direction: causal inputs → close report and manifest → Index; close-run primaries → Index.
* **Not approved as drafted.** The proposal's §6 text delta is replaced by redlines R-1 to R-4 of the review.
* **Status line.** When C-1 to C-4 are pushed, the ADR's status line reads: `Status: Approved with changes by the Product Owner on 2026-10-20 (AQ-1; HDE Build Notes addendum 2.15; review docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md).` The WU-PR-07 PR-35 session writes that line as a transcription of this decision. Instruction v1.0 ID-12's "no agent marks the ADR approved" is satisfied because the Product Owner, not the agent, made the decision and gave its text here.

### Required changes before #668 merges

1. **C-1. ADR block.** Change Process Guide §3.5.4 requires an ADR block in every close report, and HDE Schemas & Artifacts §1.2 "Change-container compatibility" applies it to a CRD close.
   * The v2 schema gains a required, non-empty list of ADR-block entries. Each entry has a label, a statement, the decision point, the options considered when more than one was real, the bounding PF titles, the final decision, whether it becomes canonical or stays change-specific, and the doc-delta targets by PF title.
   * An optional closure-override entry enumerates accepted gaps with their evidence basis and drain targets.
   * The report renders the entries as an ADR block with titles-only canon references.
2. **C-2. The current approved Specification.** The requirements document a v2 source binds must be its own change's `docs/ephemeral/<change-id>-specification-v<N>.<N>-approved.md`, at the highest version tracked. Any other document is refused with one typed code.
   * Both real approved Specifications follow that pattern: HDE-CRD-0002 v1.1 and HDE-EPIC040 v1.1.
   * A superseded Specification, such as HDE-CRD-0002 v1.0 with 21 requirement rows, can then no longer support a `SATISFIED` close.
3. **C-3. Tracked-issue fields.** A tracked-issue item renders HDE Governance §2.0.19's literal canon-pointer fields: `TI-<id> pointers:` for a pointer item, and `ADR status line:` for an ADR-status item.
4. **C-4. ADR text.** The ADR's Decision section and canon table carry redlines R-1 to R-4 of the review, together with C-1 to C-3. In summary:
   * R-1: the binary decision and its posture; requirement IDs read from the current approved Specification in the change kind's pinned format; every criterion ID one of them; `SATISFIED` needs a met row for every ID and no follow-up, and `NOT SATISFIED` needs a follow-up;
   * R-2: the drain-targets ledger names the deferral's or tracked issue's own ID;
   * R-3: every key output other than the close report and manifest is also a bound tracked input;
   * R-4: five further canon homes in the table.
5. **Validation.**
   * The negative controls, the writer test file, every updater consumer, and the evidence and qa lanes pass locally before one push.
   * Hosted CI and a fresh Codex code review run on the resulting head.
   * Every P1 finding on a real input is fixed (addendum 2.14).
6. **Scope.** C-1 to C-3 are corrections within S21's acceptance intent ("a canon-conforming close report"), in files already in WU-PR-07's bounded set. They need no rescope. A projected pass of the unit's cost ceiling returns to the Product Owner before work continues (addendum 2.11 rule 3; addendum 2.14 rule 5).

### The close-run evidence family (introduced)

HDE Schemas & Artifacts §8.17 requires a new recurring QA evidence family to be introduced through a Build Notes addendum. This addendum introduces one:

* **Path.** `audit/qa/<change-dir>/close/<check_id>/primary.log`, each with its sibling `.path_proof.txt`, for a CRD admitted in the canonical updater's CRD admission table. `<change-dir>` is the lower-case directory form, for example `hde-crd-0002`.
* **What it holds.** Same-run mechanical evidence of a change's close workflow: one primary per close-run check, rendered from that check's captured command, exit code and output as a PF27 v2 step-log header. Its posture is PASS, FAIL or BLOCKED, as Glow QA Guide "Close-pack truthfulness and same-run execution" requires.
* **Status.** A post-verdict family. It is written after the final QA verdict, and it neither reopens nor adds to the change's approved `qa_step_logs_manifest.json` or any `checks/` primary.
* **Writer.** Only the canonical updater, `tools/evidence/update_evidence_index.py`, writes it, through its close-run publication entrypoint inside one recoverable transaction. The given results replace the whole family. The entrypoint requires the change's recorded QA family to exist.
* **Membership.** The family's members are the validated primaries and path proofs under `close/`, in a closed shape; anything else under `close/` is refused.
  * This is a scoped exception, for the `close/` directory only, to §8.17 "Current-state evidence": "Tools MUST NOT infer run state by enumerating subdirectories". That rule continues to govern `checks/` and every other part of a QA root, where `qa_step_logs_manifest.json` stays the authoritative index.
* **Not admitted.** No Epic close-run family. An Epic needs its own explicit admission later, as each CRD needs its admission row.

### Scope, exclusions and nonclaims

* This addendum produces no close pack, candidate source or close-run family for any change. HDE-EPIC040 gets no retroactive close pack.
* It changes no Specification requirement or acceptance criterion, no other work unit, and no CI lane.
* It establishes no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, merge or closure.
* Drainage of the ADR's affected canon homes is unperformed. Its absence is not a blocker of any change or close (HDE Governance §2.0.19; HDE Schemas & Artifacts §8.17).
* Earlier canon governs except where this addendum speaks: the approval itself; the close-run family and its membership exception; the ADR status text.

### Dependencies, conflicts and unresolved obligations

* **Dependencies.**
  * C-1 to C-4 land in #668 in the WU-PR-07 PR-35 session.
  * The Product Owner merges #668 only after they land and the pull request is green.
  * WU-PR-08 and the later units wait on that merge.
* **Conflicts.** None. Where this addendum departs from HDE Schemas & Artifacts §8.17's no-enumeration rule, it does so only for the `close/` family. The canon-conflict register (CR-1 to CR-8) is unchanged.
* **Unresolved, with owners.**
  * The C-1 to C-4 implementation and its records: the WU-PR-07 PR-35 session.
  * Drainage of the ADR's canon table, including this family into HDE Schemas & Artifacts §8.17 and Glow QA Guide §3.4.3: the Product Owner, through the normal canon-maintenance route.
  * Publication of this addendum into PF10, after 2.14: the Product Owner.
