---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002-WU-PR-07-ADR-DEFERS-1
proposed_pf10_number: "2.16 (the next continuous number after addendum 2.15, the last in PF10 v13.6.6 on main; allocation and publication are the Product Owner's)"
authority: Nathan / Product Owner's direction of 2026-10-21 in the continuing HDE-CRD-0002 Implementation Agent session "HDE-CRD-0002-2", given in answer to the PR-40 lineage review's finding LR7-O1 and quoted under "Source and authority". No approval prompt produced this addendum, and none is claimed
decision_record: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-work-unit-lineage-review-v1.0.md (PR-40 v1.0, ACCEPT; finding LR7-O1, observation LR7-O9; pull request #672)
producing_session: continuing whole-change HDE-CRD-0002 Implementation Agent session "HDE-CRD-0002-2", https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md on main a4189c5 (301,279 bytes; sha256 6604d8906d66c05e647109158894cce601e5c116f6ffbe51cca09a3ace37de86). Read: the silence and operational rules (§8, §9 of its front matter); addenda 2.11, 2.13, 2.14 and 2.15 in full; a search of the whole file for "TOOLING_BLOCKED", "closure override" and "closure-override", which finds only 2.15 C-1. Provenance, not a gate
silence_finding: PF10 does not say whether a SATISFIED v2 close may stand over a TOOLING_BLOCKED check that a closure override names, and it does not say how the S21 ADR stands against a later Product Owner decision. Addendum 2.15 C-3 provides a field for a tracked-issue pointer item, which a later Product Owner decision removed. Under the Product Owner's rule below, these contradictions need this addendum
capture_time_utc: 2026-10-21T17:10:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The "Canon relied on" block above the H2 is record-only and is not page text
incorporated_into: not yet; the Product Owner publishes it into PF10
---

**Canon relied on:**

* PF10-HDE-Build-Notes v13.6.6:
  * front matter §8 "Silence rule" and §9 "Operational rule for agents";
  * addendum 2.15 in full, in particular "What is approved", C-1, C-3 and C-4;
  * addenda 2.11 (rules 7 and 8), 2.13 and 2.14.
* PF06-Canon-Change-Process-Guide v2.5.4:
  * §0.1A (HDE Build Notes records material decisions and temporary pre-drain authority);
  * §1.0.5 "Canon changes";
  * §3.5.2.1 "Close-pack files" (tracked-issue forms (a) and (b));
  * §3.5.4 "ADR block in the close-pack (all epics)" ("Closure override", "No posture-only PASS").
* PF04-Canon-HDE-Governance v2.8.7:
  * §2.0.19 "Close report minimal content (normative)": the canon-pointer fields and the coverage ledger;
  * §9.1.2 (canon precedence; in-flight documents govern within their scope).
* In-flight:
  * the S21 ADR `docs/adr/hde/close_pack_writer_adr.md` on main (blob fcaa9da66fb7);
  * WU-PR-07 PR-35 result records v1.6, v1.8, v1.9, v1.11 to v1.15, v1.17 to v1.19, read through the PR-40 lineage review v1.0, §6 and §7;
  * the landed writer `tools/qa/generate_epic_close_pack.py` and the v2 schema `schemas/close_candidate_source.v2.json` at 8b73b57.

## 2.16 HDE-CRD-0002 WU-PR-07: the S21 close-pack writer ADR defers to HDE Build Notes; the Product Owner's amendments of 2026-10-21 are recorded and the ADR's contradictions are resolved

Timestamp: 102126 17:10 (UTC). Details: Records the Product Owner's rule that the S21 architecture decision record, `docs/adr/hde/close_pack_writer_adr.md`, defers to HDE Build Notes. It also records his amendments of 2026-10-21 to the design that addendum 2.15 approved, and resolves the two contradictions that no addendum resolved.

Origin: finding LR7-O1 of the WU-PR-07 PR-40 lineage review v1.0 (`docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-work-unit-lineage-review-v1.0.md`), and the Product Owner's answer to it.

Evidence: the ADR on `main` at `8b73b57`; the landed writer, schema and tests; the PR-35 result records named below.

### Source and authority

This addendum records the Product Owner's rule, in his words (2026-10-21): "The adr document should defer to PF10. So if there is a contradiction unresolved by PF10, it needs a build notes addendum to resolve it."

Where this addendum conflicts with the S21 ADR, with addendum 2.15 or with an in-flight change document, this addendum governs for the scope below.

### Rule

1. **Precedence.** The S21 ADR defers to HDE Build Notes. Where its text conflicts with an applicable addendum, the addendum governs.
2. **Unresolved contradictions.** A contradiction that no addendum resolves is resolved by a new HDE Build Notes addendum. That covers a contradiction inside the ADR, between the ADR and an addendum, or between the ADR and a later Product Owner decision.
3. **The amended design.** The design addendum 2.15 approved, at pull request #668 head `45e4cef`, is amended by the Product Owner's decisions in the table below.
   * Each decision is the one recorded in the WU-PR-07 PR-35 result record named beside it.
   * The PO-35 numbers here are WU-PR-07's series. They are distinct from WU-PR-06's PO-35-1 to PO-35-6, which addendum 2.11 cites.
   * The landed writer and schema at `8b73b57` implement every amendment.

| Decision | Record | Effect on the approved design | Relation to addendum 2.15 |
| :- | :- | :- | :- |
| PO-35-4 | result v1.6 §2 | The QA step-logs manifest is read in its pinned format before any decision | Adds a check |
| PO-35-5 | result v1.8 §2 | Each ledger entry's tracked `primary.log` is read, and its header must agree | Adds a check |
| PO-35-7 | result v1.9 §2 | Every deferral, in both forms, names an ID in the drain-targets ledger. The ADR's R-2 is reworded to match 2.15's summary of R-2 | Brings the ADR into line with 2.15 |
| PO-35-8 | result v1.9 §2 | A tracked-issue pointer names a register heading | Superseded by PO-35-11 |
| PO-35-9 | result v1.9 §2 | The plan is the change's current implementation plan | Adds a check |
| PO-35-10 | result v1.12 §2 | The QA ledger is accepted only in the canonical QA harness's own bytes | Adds a check |
| PO-35-11 | result v1.14 §2 | A tracked issue maps only through an ADR status; the pointer form is refused | **Narrows C-3** (resolution B below) |
| PO-35-12 | result v1.15 §2 | The supporting ledgers meet a pinned minimum content | Adds a check |
| PO-35-13 | result v1.17 §2 | A closure-override gap names the `TOOLING_BLOCKED` check it accepts | Extends C-1 (resolution A below) |
| PO-35-14 | result v1.17 §2 | The writer states no PO-closeout posture | Adds a limit |
| PO-35-15 | result v1.17 §2 and §4 | One audit of the v2 contract against canon. A separate QA RCA is the canonical `audit/<prefix>_QA_RCA.md`, and the report states HDE Governance's no-over-claim line | Adds checks |
| PO-35-16 | result v1.17 §2 | Every PF title names a tracked PF-Canon document. Result v1.18 widens the PF-title forms to every tracked file-name convention | Adds a check |
| PO-35-17 | result v1.17 §2 | A deferral's drain target names a heading in the change kind's register | Adds a check |
| PO-35-18 | result v1.17 §2 | The QA plan is pinned, and the report carries HDE Governance's coverage ledger against it | Adds a check and a section |
| PO-35-19 | result v1.17 §2 | Delivered scope is allocated to slices, and the report carries a reuse boundary. Result v1.18 widens the slice forms | Adds a check and a section |
| PO-35-20 | result v1.19 §2 | The authorized decision is the change's current QA-120 report; `SATISFIED` needs its `verdict: PASS`; the only posture is review-trace-only | Adds a check and a limit |
| PO-35-21 | result v1.19 §2 | Each `MET` criterion binds the primary of a `PASS` check whose QA plan mapping names it | Adds a check |

The P1 fixes made under addendum 2.14 without a decision number also changed the ADR's text, and stand with the table:
* CX7-12 (result v1.11): the whole PF27 v2 header of each QA primary is checked;
* CX7-14 (result v1.13): the later-drain epic-close expectation uses HDE Governance's three values;
* CX7-19 (result v1.18): PF titles are read from every tracked PF-Canon file name.

### Resolutions

**A. A `TOOLING_BLOCKED` check under a closure override (PO-35-13).**
* **The contradiction.** The ADR's stated limit on the QA step-logs manifest ends "and `SATISFIED` needs every recorded status to be `PASS`". That text came from PO-35-4. The ADR's decision 4 and its closure-override limit state PO-35-13 instead. PF10 did not decide between them.
* **Resolved.** A v2 `SATISFIED` decision needs every check of the change's current QA plan to be recorded in the QA step-logs manifest in one of two ways:
  * as `PASS`; or
  * as `TOOLING_BLOCKED`, where a closure-override gap in the ADR block names that check, once.
* **What blocks `SATISFIED`:** a check recorded as `FAIL_BEHAVIOR`, `FAIL_TOOLING` or `PARKED`, and a planned check the manifest does not record.
* **Not PASS evidence:** a `TOOLING_BLOCKED` check accepted under an override is never `PASS` evidence for a `MET` criterion (PO-35-21).
* **Superseded:** the stated-limit clause "and `SATISFIED` needs every recorded status to be `PASS`".
* **Basis:** Change Process Guide §3.5.4, "Closure override" and "No posture-only PASS". The landed writer at `8b73b57` and its test `test_v2_closure_override_exempts_only_the_tooling_blocked_check_it_names` already behave this way.

**B. The tracked-issue pointer field of addendum 2.15 C-3 (PO-35-11).**
* **The contradiction.** C-3 has a tracked-issue item render HDE Governance §2.0.19's `TI-<id> pointers:` field for a pointer item, and `ADR status line:` for an ADR-status item. PO-35-11 removed the pointer item from the v2 schema.
* **Resolved.** For `close_candidate_source.v2`:
  * a tracked-issue item is an ADR-status item only, and renders `ADR status line:`;
  * C-3's pointer clause is superseded.
* **Consequence.** A tracked issue closed as satisfied through PF09 or PF30 pointers cannot be expressed by the v2 writer: that is Change Process Guide §3.5.2.1 form (a), and HDE Governance §2.0.19's `PF09 pointers:` and `TI-<id> pointers:` fields. Such a close needs a later schema version.
* **Basis.** The ADR records it: no PF09 or PF30 file cites a TI ID, so no pointer can show that issue's closure. Form (b), an ADR status line, satisfies §3.5.2.1.

### Scope and supersession

* **Applies** to the S21 ADR and to `close_candidate_source.v2` and its writer, from this addendum on.
* **Supersedes:**
  * addendum 2.15 C-3, for pointer items only;
  * the ADR clause named in resolution A.
* **Extends:**
  * addendum 2.15 C-1, by PO-35-13's naming rule;
  * 2.15's "What is approved", by the table.
* **Does not change:**
  * the rest of addendum 2.15: the AQ-1 approval, the status line, C-1, C-2, C-4, the close-run evidence family and its membership exception;
  * addenda 2.11, 2.13 and 2.14;
  * any other ADR, schema or work unit.
* **Not reopened:** WU-PR-07's delivery, which PR-40 lineage review v1.0 accepts.

### Epic, task, and status effects

* No epic, CRD, task, PF09 or PF30 row changes status by this addendum.
* WU-PR-07: PR-40 lineage review v1.0 accepts the unit. Its finding LR7-O1 is resolved here, and its observation LR7-O9 is resolved as resolution B.
* No code change is needed: the landed writer already implements both resolutions.

### Required canon drainage

Drainage is unperformed.

| Target | Required change |
| :- | :- |
| The S21 ADR | When the ADR is next revised: remove resolution A's superseded clause, and state that the ADR defers to HDE Build Notes. Editing the ADR needs the Product Owner's instruction |
| Change Process Guide §3.5.4; HDE Governance §2.0.19 "Close report minimal content" | Carry resolution A as the close pack's treatment of a `TOOLING_BLOCKED` check under a closure override, with the ADR's other drainage items |
| Change Process Guide §3.5.2.1; HDE Governance §2.0.19 canon-pointer fields | Note that the generic v2 writer supports only form (b) (resolution B) |

### Deferred obligations and unresolved work

* Publication of this addendum into PF10, after 2.15: the Product Owner.
* The ADR revision named above, if the Product Owner directs one: its owner.
* WU-DOC-01's usage note for the writer (contract H-4) reads the ADR together with this addendum.

### Scope boundaries and nonclaims

* This addendum changes no code, schema, test, prompt, skill, `AGENTS.md`, ADR text or permanent PF document.
* It produces no close pack for any change.
* It establishes no QA, acceptance, Ops, deployment, merge or closure.

### Evidence anchors

* The Product Owner's words, quoted under "Source and authority".
* PR-40 lineage review v1.0 of WU-PR-07, §6 and §11 (LR7-O1, LR7-O9).
* The ADR on `main` (blob fcaa9da66fb7):
  * "Stated limits", the QA step-logs manifest item (the superseded clause);
  * decision 4 and the closure-override limit (PO-35-13);
  * the tracked-issue limit (PO-35-11).
* The writer on `main` at `8b73b57`:
  * the `SATISFIED` decision check;
  * the closure-override check (`CLOSURE_OVERRIDE_INVALID`);
  * the schema's tracked-issue definition, `{id, adr_status}` only.
* Addendum 2.15 C-1 and C-3.

### Relationship to existing HDE Build Notes guidance

The addendum amends addendum 2.15 as stated under "Scope and supersession". It is consistent with addenda 2.11, 2.13 and 2.14.

It follows 2.14 in recording design narrowings that fixed P1 findings on real inputs: CX7-15 by PO-35-11, and CX7-17 by PO-35-13.
