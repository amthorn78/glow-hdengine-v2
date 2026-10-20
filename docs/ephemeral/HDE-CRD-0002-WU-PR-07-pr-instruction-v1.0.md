---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-PR-07-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
work_unit_title: "Close-pack writer for Epic and CRD identities, close-run evidence home, ADR draft (PR; Distillation; S21)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_pf10_overlays: PF10 addendum 2.11 (business case, cost ceiling and gates; real inputs; constructed inputs; no emulation of external systems; finding disposition; repeated finding class), read with addendum 2.12's numbering of it; addendum 2.12 (WU-PR-06 accepted; decision 1, WU-PR-07's business case, returned to the Product Owner and since decided); addendum 2.5 (WU-PR-02 accepted: the updater's CRD admission model and `publish_crd_check_family`, OBS-17, AQ-1 carried to WU-PR-07, LR-O2); addendum 2.3 (the reviewer chain without the Codex security review); addendum 2.1 (§19 only). Addenda 2.6 to 2.8 have no item for this unit: it changes no release member, so no refresh runs
product_owner_disposition: docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md (decided 2026-10-20, "adopt the business case, option A, give me the PR-10 handoff"; blob 88a65d8a4663; landed by #663 as 731f03c). Decision 1 is the WU-PR-07 business case and cost ceiling (§4.3 below). Decision 2, option A for WU-PR-06, sets a line in this unit's PR-40 (ID-17)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; approved by PLAN_REVIEW_REF)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE; blob 0cc0276524b2). Its §3 note M1 (the CRD close-pack Index registration) binds this unit (ID-9)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — §5.6, §6 S21, §7.1 EC-10 and §8 AQ-1 bind this unit; §5 below re-measures them at the current baseline
predecessor_unit_acceptance: WU-PR-02 (the dependency) through addendum 2.5 (lineage review v2.0); WU-PR-06 (the unit before this one in the merge order) docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-work-unit-lineage-review-v1.0.md (ACCEPT on #660; blob 1b69f1370c80; landed by #662 as ff14383; addendum 2.12)
incident_record_read: docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md (blob df95ae21903a) §0 and §1 (B-1, B-2), through the Audit's §5.6 and §6 S21, which cite it
structure_precedent: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (blob f3a6a8855ec0)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md (v13.6.3; blob 41d5cfd2da6d; 271,926 bytes; sha256 5c26c80b3eb6b36e305ee22b998a8e5d41156c5702d659827dd9b8fdc513ff35; Product Owner commit 043fa91, "PF10"). Read for this unit, in this invocation: the complete v13.6.2 → v13.6.3 diff (the version lines, one index line and addendum 2.12 appended; nothing else changed), with 2.12 read in full; 2.11 in full; 2.5 in full; 2.3 and 2.1, read in full at PR-10 for WU-PR-06 in this session and byte-unchanged since (the diffs show); a search of the whole file for this unit's terms (WU-PR-07, S21, AQ-1, OBS-17, LR-O2, close pack), which finds items only in 2.4, 2.5, 2.8, 2.9, 2.10, 2.11 and 2.12, each read at its hit
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md §2.11, §2.12, §2.5, §2.3; §2.1 for §19
pf10_note: addendum 2.11's internal cross-references are misnumbered (addendum 2.12, decision 3; LR6-O2). This instruction cites 2.11's rules by the numbering addendum 2.12 states (rule 1 business case; 2 not a business case; 3 gates; 4 real inputs; 5 constructed inputs; 6 no emulation; 7 finding disposition; 8 repeated finding class). Where 2.11's own text points to "rule 3" for real inputs (rule 7) it is read as rule 4, by the wording it describes
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state as of 2026-10-12T02:29:33.739Z, fetched in this invocation at 13:14:32Z, byte-identical to the copy used for WU-PR-06, and read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-20T13:42:00Z
repository_baseline: origin/main 731f03c96bda3dcd033913d1852edcdc118c86c5 (tree 540a0b588600). Outside docs/ephemeral/ and docs/pfcanon/, every byte equals fc51620 (#660, accepted WU-PR-06, plus #661): the three later commits add the WU-PR-06 lineage review (ff14383, #662), PF10 v13.6.3 (043fa91) and the Product Owner disposition (731f03c, #663). Every repository fact in §5 was measured at 731f03c in detached scratch copies
receiver: dedicated HDE-CRD-0002 WU-PR-07 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z, re-fetched in this invocation and unchanged from the copy used for WU-PR-06)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§16)
---

# HDE-CRD-0002 WU-PR-07 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete, self-contained PR instruction for work unit WU-PR-07 of HDE-CRD-0002. The whole-change IA issues it from the approved Implementation Plan v1.1, with the business case and cost ceiling the Product Owner adopted on 2026-10-20 (§4.3). A dedicated PR-20 session can plan the unit from this instruction and the linked current repository and canon, without reconstructing upstream intent (§17).

It does not:
- author the detailed per-file plan, the schema, the writer's or updater's design, the ADR text or the tests. Those are the PR session's (§9);
- authorize implementation, a commit, a pull request, a merge, Ops, QA, acceptance or closure. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for the exact PR-20 plan authorizes implementation, and only Nathan merges;
- approve the ADR. AQ-1 is the Product Owner's, before this unit merges (ID-12);
- produce HDE-CRD-0002's own close pack, candidate source or close-run evidence. Those belong to HDE-CRD-0002's close mutation set, after QA (§7);
- decide a canon, product or scope question, change canon or create a PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-07 (Plan v1.1 §7 heading "WU-PR-07 — Close-pack writer for Epic and CRD identities, close-run evidence home, ADR draft (PR; Distillation)") |
| Requirement | S21 (source items 8, CC-1, CC-2); CD-1 (resolved by S21); EC-10; IF-3; IF-4 |
| Approved base | Specification v1.1 → Plan v1.1 + review v1.1 (refs above). Review v1.1 §3 note M1 binds this unit |
| Overlays | PF10 addenda 2.11, 2.12, 2.5, 2.3 and 2.1, as named in the header; the Product Owner disposition of 2026-10-20 |
| Upstream units | WU-PR-01 to WU-PR-06, all accepted |
| Phase | Distillation |
| Live QA class (Specification table; Plan §6) | Not production-affecting ("close-pack tooling and evidence-index tooling") |

## 3. Unit selection and dependency state

- **Plan approval.** Isis approved exactly Plan v1.1 (review v1.1, INITIAL_APPROVE).
- **Unit type.** PR unit.
- **Dependency state: ready.**
  - Plan v1.1 §7: "Seventh; after WU-PR-02 (updater model)." WU-PR-02 is accepted (addendum 2.5), and its CRD admission model is on `main`: `ADMITTED_CRD_QA` holds `HDE-CRD-0001` and `HDE-CRD-0002` (§5.4).
  - WU-PR-06, the unit before this one in the merge order, is accepted (lineage review v1.0 on #660; addendum 2.12).
  - Addendum 2.11 rule 3 required a business case before this PR-10. The Product Owner adopted it on 2026-10-20 (§4.3), which meets addendum 2.12's decision 1.
  - No `HDE-CRD-0002-WU-PR-07-*` file other than the disposition record exists on `main`.
  - No QA Guide, QA Plan or Ops receipt is a prerequisite (Plan §9 item 4). AQ-1 gates the merge, not the planning or the implementation (Plan §13).
- **Order.** WU-PR-01 → … → WU-PR-06 → **WU-PR-07** → WU-PR-08 → WU-DOC-01 → WU-OPS-01 → QA-10 (Plan §7). WU-PR-07 and WU-PR-02 are the two updater-changing units, and WU-PR-02 has landed, so the two cannot race.
- **Downstream dependents** (contracts in §8):
  - WU-PR-08 runs the updater after the `1.4.0` cut ("after … WU-PR-07 (updater families)"), so the absent-tolerant registration and the IF-4 entrypoint must leave every existing input publishing and validating;
  - WU-DOC-01 updates `AGENTS.md` "HDE-EPIC039 current workflow posture" and `README.md` line 25 for the new writer (Audit §6 S21 "Canon and documentation effects");
  - HDE-CRD-0002's close mutation set, after QA, runs the T1 to T6 sequence of Plan v1.1 WU-PR-07 "Terminal-state reachability" with this unit's tools;
  - the Product Owner decides AQ-1 on the ADR this unit drafts.

## 4. Required behavior

**Acceptance intent and constraints**, verbatim from the approved Specification:

| ID | Scope | Acceptance intent |
| :- | :- | :- |
| S21 | "A governed, feedback-free close-pack writer for Epic and CRD identities, and an admitted home for close-workflow run evidence" | "The writer produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD; close-workflow run evidence has a home, inside an existing evidence family or in one S21's ADR admits, that does not reopen an approved QA manifest; the accompanying ADR is approved" |

- **Constraint "Close-pack writer."** "HDE-EPIC039 made the generic writer neutral on purpose; S21 reverses that choice and must weigh its rationale. S21 touches the release-sanity and close-validation lanes."
- **CD-1.** "The governed close-pack schema accepts only Epic identities: its `epic_id` pattern is `^HDE-EPIC[0-9]{3}$`" — "Resolved by S21".
- **Exclusions** that bind this unit: "No new evidence family, acceptance token or token matrix, except a home for close-workflow run evidence that S21's ADR admits (S21)"; "No canon change beyond S21's ADR-covered close-pack change"; "no retroactive close pack for HDE-EPIC040" (Plan §15); "As implementation work: no deployment, no production configuration change, and no live vendor call".
- **Canon impact** (Specification): "S21 changes close-pack canon: which writer produces the close report, and where close-workflow run evidence lives"; affected canon "Change Process Guide §3.5.2 (close pack); HDE Schemas & Artifacts §1.2 "Close-pack artifacts"; Glow QA Guide "Close-pack truthfulness and same-run execution" and "Close report requirements""; "Accompanying ADR reference and status: required for S21 (Change Process Guide §1.0.5) … It must be approved before S21's changed behavior is relied on."
- **Distillation row.** "S21's ADR is approved before S21's changed behavior is relied on … S21 completes before HDE-CRD-0002 enters its ordinary Close Gate."

**Plan v1.1 §7 WU-PR-07 block.** Its Purpose, Bounded scope, Inputs, Deliverables, Terminal-state reachability (a) to (e) with T0 to T7 and the restart rules, Dependencies and order, and Acceptance (1) to (7) are binding as written and are not restated here except where a binding reading below needs a quotation. PR-20 reads the block in full. Its Deliverables line:

> "`schemas/close_candidate_source.v2.json` (new; IF-3); `schemas/epic_close_candidate_source.v1.json` retained; `tools/qa/generate_epic_close_pack.py` (v2 source, both identities, required headings and pointers, `key_outputs`, check mode non-writing); `tests/qa/test_generate_epic_close_pack.py`; `tools/evidence/update_evidence_index.py` and its tests (IF-4 family admission); `ci/checks/classify_ci_changes.py` (registrations for new files); `.github/workflows/epic-closeout-validation.yml` and the release-sanity stage that validates close packs, only where they read the schema version (`Unknown pending discovery`, resolved at PR-20); `docs/adr/hde/close_pack_writer_adr.md` (new; status `Proposed`; decision, affected canon homes with exact locators, drainage consequences, alternatives considered, nonclaims)."

**Plan v1.1 §5 IF-3 and IF-4**, verbatim:
- IF-3: "`schema_version: close_candidate_source.v2`; `change_id` `^HDE-(EPIC[0-9]{3}|CRD-[0-9]{4,})$` mapped to the filename prefix (`EPIC-NNN` for an Epic; the CRD ID itself, `HDE-CRD-NNNN`, for a CRD) and the lower-case directory form; `plan_path`, `evidence_inputs[]` (tracked path + binding), `acceptance[]` (criterion id, tracked evidence paths, result, limitation), `deliverables[]`, `deferrals[]` (id, drain target or ADR status), `later_drain_statements[]` (fixed vocabulary of HDE Schemas & Artifacts §1.2), `closure_decision` (`SATISFIED`/`NOT SATISFIED` plus posture), `follow_ups[]`, `pointers[]`, `qa_rca` (embedded summary or exact path), `key_outputs` (close report, manifest); every causal field keeps the feedback-dependency refusal; candidate identity only by tracked-path digests. Writer outputs `audit/<PREFIX>_close_report.md` (with the verbatim heading `QA Rails — Open/Close (Final PR)` and an "Acceptance and evidence pointers" list) and `audit/<PREFIX>_MANIFEST.json` (with a `key_outputs` map); check mode writes nothing."
- IF-4: "`audit/qa/<change-id>/close/<check_id>/primary.log` (+ `.path_proof.txt`), a post-verdict family admitted by the S21 ADR and published by the canonical updater; it never adds a check to `qa_step_logs_manifest.json`."

**Review v1.1 §3 note M1**, verbatim: "T3 relies on "the CRD close-pack registration this unit adds", absent-tolerant like the Epic rows. WU-PR-07's Deliverables line for `tools/evidence/update_evidence_index.py` names only "IF-4 family admission". The file is already a deliverable, and the reachability bullet states the registration, so the PR-20 plan carries both. Whether the existing Epic rows are absent-tolerant was not verified here; acceptance (7)'s rehearsal exercises it." This IA measured it: they are not (§5.4; ID-9).

**Audit §6 S21 "Required behavior"** (a) to (d) and "Risks" ("Canon drift between the three close-pack homes …; over-wide free text (validated sections with required headings); the `QA Rails` heading's em dash versus the current heading regex (the v2 schema admits it explicitly)") are inputs. Where the Audit and Plan v1.1 differ, Plan v1.1 governs: the CRD filename prefix is the CRD ID itself, `HDE-CRD-0002` (Plan v1.1 IF-3 after redline R4; HDE Schemas & Artifacts §1.2 "Change-container compatibility"), not the Audit's `CRD-NNNN`.

### 4.1 Requirements mapped to canon

| # | Requirement | Governing canon on `main` (read for this instruction) |
| :- | :- | :- |
| C1 | Close-pack files at canonical filenames, an exact-source acceptance section, a verification statement, TI mapping, a binary decision, follow-ups, the superseded-artifact statement | Change Process Guide §3.5.2.1 "Close-pack files" (read in full) |
| C2 | No source → CI → source back-edge; all tracked candidate bytes complete before hosted validation | Change Process Guide §3.5.1 "Requirement", "Feedback-free terminal lifecycle" |
| C3 | CRD prefix and directory form; one contract for both lanes; Epic-only validators updated before the first CRD close pack | HDE Schemas & Artifacts §1.2 "Change-container compatibility (normative)": "For a CRD, the stable CRD ID recorded in PF30 replaces `EPIC-\#\#\#` as the filename prefix … and replaces `<epic-id>` in supporting paths using its lower-case ASCII, hyphenated directory form"; "Before the first affected CRD close-pack enters QA or closeout, every schema, generator, or validator that accepts only `EPIC-\#\#\#` or `<epic-id>` MUST be identified and updated through the authorized change lane" (ID-4) |
| C4 | Close report content: shipped deliverables, deferrals, later-drain statements in the fixed vocabulary, decision posture, `key_outputs` pointer, QA RCA; supporting ledgers | HDE Schemas & Artifacts §1.2 "Close-pack artifacts" (ID-5) |
| C5 | `key_outputs` is a named map; values | HDE Schemas & Artifacts §1.2 "Close-pack manifest key_outputs (named binding map; normative)" (a value is a path string or a non-empty list); HDE Mechanics Guide §37.3 "Conventions": "each value is a repo-relative artifact path (string)"; "key\_outputs MUST NOT be a list" (ID-6) |
| C6 | A titled "Key outputs" section; manifest points to the close report; "Doc Deltas: None"; one deterministic generator; no drainage prerequisite | HDE Mechanics Guide §37.2 "Governance & homes": "Close report (minimum content; generated)", "Doc deltas capture file", "Close-pack manifest (minimum binding responsibilities; generated)", "Close-pack generator (mechanics; single-writer; normative)", "Documentation drainage posture for closeout artifacts": close reports "MUST NOT encode PF10 drain or any other post-QA documentation drainage as a prerequisite, required deliverable, required check, acceptance condition, readiness condition, or blocker" |
| C7 | The verbatim heading and pointer list; same-run mechanical evidence under the QA root | Glow QA Guide "Close report requirements (validator-bound; mechanical)": "the heading `QA Rails — Open/Close (Final PR)` (verbatim), and an "Acceptance and evidence pointers" list containing the epic's canonical pointer strings (exact text)"; "Close-pack truthfulness and same-run execution (normative)" |
| C8 | Canon change needs an approved ADR naming affected canon and drainage; ADRs are Product Owner-owned, agents draft | Change Process Guide §1.0.5 "Canon changes"; HDE Governance §9.7.3 ("Planning artifacts owned by the Product Owner, including Tracked Issues and ADR stubs, remain PO-owned. Agents MAY draft suggestions") |
| C9 | The Index trio in the same mutation set; one canonical updater | Change Process Guide §3.5.2.3 "Index and mirror trio (same authorized mutation set)"; `AGENTS.md` "Evidence harness" and "Governed evidence rules" |
| C10 | Business case, real inputs, no emulation, finding disposition, repeated finding class | PF10 addendum 2.11 rules 1 to 8 (§4.3; ID-1, ID-2, ID-13) |
| C11 | Authority, Proceed and merge | HDE Governance §9.1.1; §9.1.2 (canon precedence; in-flight documents govern within their scope) |

### 4.2 Binding IA decisions (canon-conforming readings; HDE Governance §9.1.2)

**ID-1. The cost ceiling, and how the plan stays within it** (addendum 2.11 rule 3; disposition record §2).
- The ceiling is the Product Owner's adopted text: "One PR, with review rounds capped by addendum 2.11 rule 8. At most 4 sessions or 3 days from PR-10 to merge. Past that, the unit returns to the Product Owner."
- **Counting**, as the disposition record states it:
  - Sessions: the PR-10 invocation (this one), the PR-20/PR-30 session and the PR-35 session make three. Any further session, or any repeat of a stage, counts toward the four.
  - Days: from the start of PR-10 to the merge. This PR-10 started by 2026-10-20T13:14:32Z (the time this invocation saved the PR-10 prompt). Time waiting on a Product Owner decision does not count: the Proceed, AQ-1 and the merge.
- **Spent at this instruction:** 1 session. The PR-20 plan has 2 sessions of slack after PR-20/PR-30 and PR-35, and about 3 days less this PR-10's working time.
- **What PR-20 states.** The plan states how it stays within the ceiling: the scope it builds (acceptance (1) to (7), nothing more), the order of work, which checks it runs once and which it re-runs, and its own estimate of PR-30's and PR-35's spend. "A unit whose business case is met stops; further work on it needs a new business case" (rule 3): the plan adds no capability the measure does not need.
- **Checkpoints.** PR-30 and PR-35 record the sessions and elapsed working time spent so far in each result record. A projected or actual pass of the ceiling is "a change of budget, schedule or risk needing Product Owner direction", which is material (§14); the work returns to the Product Owner before it continues.
- **The measure** ("HDE-CRD-0002 closes through the ordinary Close Gate with the new writer on the first attempt") is checked at HDE-CRD-0002's close, not in this unit. This unit's acceptance (7) is the rehearsal of that path; PR-40 records the unit's cost against the ceiling.

**ID-2. The real-input set** (addendum 2.11 rules 4 and 5).
- **The writer's real inputs** are tracked files at the HEAD of a clean checkout, read by the writer's own git reader:
  - a v2 candidate source, the plan path and the declared evidence inputs it names. The first real v2 source is HDE-CRD-0002's own `audit/HDE-CRD-0002_close_candidate_source.json`, authored at T1 of HDE-CRD-0002's close from its approved Specification (S01 to S22), Plan, QA verdict and evidence. The next is any later Epic's or CRD's;
  - a v1 source. **No tracked v1 candidate source exists on `main`** (§5.3). v1 stays accepted for history and is not extended.
- **The real environments:** a local clean clone under closed rails with Python 3.12 and CI's install (T1 to T6), the ordinary `test` job, and the `epic-closeout-validation` job, which runs Python 3.12 with only `jsonschema==4.23.0` installed and no repository install (§5.2).
- **The synthetic candidates of acceptance (1) and (7) stand for real inputs.** The synthetic `HDE-CRD-0002` candidate carries the Specification's real requirement IDs and acceptance-intent texts (S01 to S22), so the test exercises the content the real source will hold. The synthetic Epic candidate uses an Epic ID and structure of the same kind.
- **Outside the real set** (rule 5): arbitrary Markdown, other schema versions, other identity forms, untracked or symlinked inputs. Each gets one refusal with a stable code, or a stated limit; never a model of it. The plan lists the refusals it keeps and adds; it promises no fail-closed handling over an open-ended input language.

**ID-3. The feedback-dependency refusal meets HDE-CRD-0002's own text.**
- Acceptance (2): "The feedback-dependency refusal still rejects run, receipt, attestation and commit identities in causal fields; candidate identity is tracked-path digests only."
- **Measured (§5.3):** the v1 `FEEDBACK_DEPENDENCY_RE` matches the word "attestation" in S06's scope and acceptance intent, and "`release_id`" and "release identity" in S11's. Two of the Specification's 22 requirement rows carry text the v1 refusal rejects. Those rows are a real input (rule 4(a)): HDE-CRD-0002's own close source must record S06's and S11's acceptance.
- **Binding:** the v2 source can express all 22 rows' acceptance, while run, receipt, attestation and commit **identities** in causal fields still refuse. PR-20 chooses the mechanism and records why it keeps the invariant. Options include: binding requirement text by reference (Specification path, requirement ID and its digest) instead of copying it; scoping the refusal to identity-shaped values; or a validated vocabulary for the real terms. The plan proves the choice against the 22 real rows and against the v1 refusal's existing negative cases.
- The v1 refusal and its tests stay unchanged for v1 sources.

**ID-4. Identity and the Epic-only inventory** (C3; CD-1).
- `change_id` `^HDE-(EPIC[0-9]{3}|CRD-[0-9]{4,})$`. Prefix and directory form:
  - Epic `HDE-EPICNNN`: `audit/EPIC-NNN_close_report.md`, `audit/EPIC-NNN_MANIFEST.json`, directory `hde-epicNNN`;
  - CRD `HDE-CRD-NNNN`: `audit/HDE-CRD-NNNN_close_report.md`, `audit/HDE-CRD-NNNN_MANIFEST.json`, directory `hde-crd-nnnn`.
- The writer selects the model by the source's `schema_version`; v1 output for a v1 source is byte-unchanged.
- **Epic-only inventory** (PF12 §1.2 "every schema, generator, or validator that accepts only `EPIC-\#\#\#` or `<epic-id>` MUST be identified"). This IA's search at the baseline (§5.5) finds, among the generic close-pack surfaces, only the v1 schema's `epic_id` pattern and the writer's `EPIC_RE`. The per-epic generators (`tools/qa/generate_epic025_close_pack.py` to `generate_epic029_close_pack.py`, `tools/qa/epic021_qa.py`) are epic-specific families and stay so (PF12 §1.2: "Named HDE-EPIC-specific families remain epic-specific"). `ci/checks/check_mirror_schema.sh` already admits `crd_id`. PR-20 re-runs the search, records the inventory, and the ADR names it.

**ID-5. Close report content.**
- The v2 report carries every element of C1, C4, C6 and C7, each rendered from a structured source field: the verbatim heading `QA Rails — Open/Close (Final PR)` (with the em dash, which the v1 `REPORT_HEADING_RE` rejects); the "Acceptance and evidence pointers" list as literal strings; a titled "Key outputs" section; the exact-source acceptance section (each criterion bound to tracked evidence paths with their digests, result and limitation); the verification statement of the canonical filenames; the TI mapping, or a statement that none is cited; the binary `SATISFIED` / `NOT SATISFIED` decision with its posture; follow-ups when `NOT SATISFIED`; the superseded-artifact statement when an earlier verdict differed; shipped deliverables; deferrals by ID with a drain target or ADR status; later-drain statements in the fixed vocabulary of PF12 §1.2; the QA RCA embedded or by exact path; the supporting-ledger pointers.
- Free text is limited to validated sections with required headings (Audit §6 S21 "Risks").
- **No drainage prerequisite** (C6): later-drain statements are statements, never a condition of the decision.
- **Nonclaims.** v1's five mandatory nonclaims include "No QA PASS, acceptance, or token satisfaction is claimed.", which a `SATISFIED` close report contradicts. The v2 nonclaims are those true for a close (for example no deployment, no PF09 or PF30 movement, no drainage performed); the plan names them. A v2 report claims nothing its bound evidence does not show.
- PR-20 maps each canon element to its source field, renderer and test in a table.

**ID-6. Manifest and `key_outputs`.**
- The v2 manifest has a `key_outputs` JSON object whose values are repo-relative path **strings**. That satisfies both PF12 §1.2 (a string or a non-empty list) and PF14 §37.3 (a string; the map is not a list); a list value is not used. This is a reading that satisfies both sources, not a conflict (§16).
- It points to the close report (C6) and names the supporting ledgers and the QA manifest as paths of record.
- **The commit point stays.** The manifest still binds the report's SHA-256 and size, is written last, and is read `manifest → report → manifest` (HDE-EPIC039's invariant; `AGENTS.md`). That binding points from the manifest to the report only, so it creates no cycle.
- `key_outputs` carries **no digest** of the Index, path proofs, orientation output or close-run family (Plan v1.1 (d)).

**ID-7. Invariants kept from HDE-EPIC039** (`AGENTS.md` "HDE-EPIC039 current workflow posture"; Audit §6 S21 "Feasibility").
- One writer at its registered path; `--source` plus exactly one of `--write` or `--check`; the closed-rails refusal (`CLOSED_RAILS_REQUIRED`); clean tree at a tracked HEAD; tracked inputs only.
- Report first, manifest last; `manifest → report → manifest` validation; mixed or interrupted state refused; symlink-byte verification; no hosted receipt feedback.
- Check mode writes nothing and compares exact committed bytes (acceptance (3)).
- The v2 writer refuses, as causal inputs, the Index trio and its sentinels, every `.path_proof.txt`, the orientation output, every path under `audit/qa/<change-id>/close/`, the close-pack outputs and `catalog/manifest.json` (Plan v1.1 (d)).

**ID-8. The IF-4 entrypoint and the CRD reconciler.**
- **Measured by code reading (§5.4):** `_load_crd_qa_entries` claims every Index row under an admitted CRD's QA root and accepts only `qa_step_logs_manifest.json` and `checks/<check_id>/primary.log`. A row at `audit/qa/hde-crd-0002/close/<check_id>/primary.log` would be refused today as "CRD index key/path relationship is malformed". The IF-4 rows therefore need a change inside that reconciler, not only a new list.
- **The entrypoint** is added to `tools/evidence/update_evidence_index.py`, modelled on `publish_crd_check_family`:
  - refuse an ID not in `ADMITTED_CRD_QA`;
  - refuse existing incoherence first (`_run_once(check=True)`);
  - write the primaries and their path proofs and converge the Index inside one `_WriteTransaction`, then run the read-only verifiers inside it; any failure restores the prior bytes;
  - **never** read or write `qa_step_logs_manifest.json` or any `checks/` primary;
  - render each primary from captured command, exit status and output only (T5), with check IDs validated as `qa_harness.validate_check_id` does.
  - each primary states the exact command executed and its resulting PASS, FAIL or BLOCKED posture (Glow QA Guide "Close-pack truthfulness and same-run execution": the evidence set "MUST include same-run primary logs or step-scoped mechanical outputs that capture the exact commands executed and the resulting PASS, FAIL, or BLOCKED posture"), under the CRD's QA root, which replaces "the epic QA root" for a CRD (PF12 §1.2 "Change-container compatibility").
- If rendering a close-run primary needs a change to `tools/qa/qa_harness.py`, the plan names it inside S21's bound (Plan v1.1 T5). `tools/qa/qa_harness.py` is otherwise expected unchanged (§6).
- **Epic identities.** The updater admits close-run families only for IDs it admits. HDE-CRD-0002 is admitted; no Epic QA root is. PR-20 states whether this unit admits an Epic close-run family or records it as a stated limit in the ADR (an Epic admission is a later explicit row, as `ADMITTED_CRD_QA`'s comment requires for CRDs). HDE-CRD-0002's close is the real input; an Epic close-run family is not needed for the measure.

**ID-9. The CRD close-pack Index registration (M1).**
- **Measured (§5.4):** the Epic close-pack rows are **not** absent-tolerant. With `audit/EPIC-022_close_report.md` removed in a throwaway copy, `update_evidence_index.py` exits 1 with a `FileNotFoundError` traceback from `_read_bytes` (via `_render_mirror`), in both `--check` and write mode.
- The real input: until HDE-CRD-0002's close, `audit/HDE-CRD-0002_close_report.md` and `_MANIFEST.json` do not exist, and every pull request's evidence lane runs the updater. So the registration must be conditional, by the existing precedent `_load_epic036_pr01_entries` (returns `[]` when its anchor is absent):
  - neither file present: no rows, no change to the Index;
  - both present: rows for the report and manifest, with path proofs by `_write_path_proof`;
  - one present: a typed refusal (a mixed pair).
- At this unit's merge, `main` has neither file, so the Index trio is byte-unchanged (§10 check).

**ID-10. The workflow and the release-sanity stage ("Unknown pending discovery", resolved).**
- `.github/workflows/epic-closeout-validation.yml` passes `candidate_source` to `generate_epic_close_pack.py --check` and reads no schema version. **No release-sanity stage of `tools/evidence/run_sanity_pipeline.py` invokes the writer or reads a candidate source** (§5.2). Both are expected unchanged.
- **Consequence for the writer:** the hosted job installs only `jsonschema==4.23.0` and does not install the repository. The writer's imports at the baseline are the standard library and `jsonschema` (§5.3), and the v2 writer and schema keep that. The v2 schema validates with `Draft202012Validator` under `jsonschema` 4.23.0.
- The job also runs the updater's `--check`, `orientation_demo.py --check`, the hash, path, Mirror-schema and final-LF checks. ID-9 keeps them passing before HDE-CRD-0002's close pack exists.

**ID-11. Classifier registration and CI shape.**
- **Measured (§5.6):** `schemas/close_candidate_source.v2.json` is refused by the classifier today (`CI_CHANGE_CLASSIFIER_ERROR:CI_PRODUCT_OWNER_TEST_MISSING:schemas/close_candidate_source.v2.json`). The registration gives it `tests/qa/test_generate_epic_close_pack.py` as owner, alongside v1's entry. `docs/adr/hde/close_pack_writer_adr.md` classifies as `documentation_only` and needs no registration.
- A change to `ci/checks/classify_ci_changes.py` selects all seven lanes (acceptance (6)).
- Pins in `tests/evidence/test_rails_ci_workflow_integration.py` that enumerate the registry the new entry joins may gain exactly that entry. Every other pin stays true.
- No workflow, job, step or lane is added.

**ID-12. The ADR and AQ-1.**
- `docs/adr/hde/close_pack_writer_adr.md`, status `Proposed`, in the form of the precedent `docs/adr/hde/release_attestation_scaling_adr.md` (a status line, problem, numbered decision, dependency direction, safety and compatibility). It records: the decision (v2 schema, the writer kept at its registered path, the IF-4 family, the absent-tolerant registration); affected canon with exact locators (PF06 §3.5.2 and §3.5.2.1; PF12 §1.2 "Close-pack artifacts" and "Change-container compatibility"; PF19 "Close-pack truthfulness and same-run execution" and "Close report requirements"; PF14 §37.2 "Close-pack generator", which names an EPIC-025 entrypoint); the drainage consequences, as statements, never a prerequisite; the alternatives weighed (Audit §8 AQ-1 (a) to (c), the Product Owner's choice of the writer over a canon change or keeping exceptional closure, disposition record §2); HDE-EPIC039's neutral-writer rationale and what is kept (ID-7); the candidate-source path `audit/HDE-CRD-0002_close_candidate_source.json` (Plan v1.1 (a)); the Epic-only inventory (ID-4); the Epic close-run limit if any (ID-8); nonclaims.
- It is not added to the Index (precedent: `release_attestation_scaling_adr.md` is not indexed). Acceptance (5) checks its named canon.
- **AQ-1.** The Product Owner decides before merging (Plan §13; R-4). A decision that differs from the draft revises this unit before merge, through RS-10 where it changes the bounded scope. The PR states AQ-1's state; no agent marks the ADR approved.

**ID-13. No emulation of external systems** (rule 6).
- The writer reads git objects itself (an in-process object store, `_GitObjectStore` at line 1,087, with loose-object, pack and delta decoding from line 1,004; §5.3). That is HDE-EPIC039's existing code, unchanged by this unit. New code reimplements no external system: no new git, GitHub Actions, YAML or packaging behaviour.
- The rehearsal (acceptance (7)) runs the real tools with the real git in a throwaway clone. The hosted `epic-closeout-validation` run belongs to HDE-CRD-0002's close (T7), not to this unit.

**ID-14. OBS-17 is on this unit's surface.**
- `tests/qa/test_generate_epic_close_pack.py::test_manifest_reader_rejects_new_report_with_old_manifest` (line 2848 at the baseline) failed intermittently on the hosted runner (`MANIFEST_BINDING_MISMATCH`, `CHECK_MODE_MUTATION`; run 39345008218; again on #660's `7a3b7b2`, LR6-O8). Its mechanism is not established. It passed locally at the baseline (§5.7). It is a real input under rule 4(b).
- The plan includes a bounded diagnosis in the prototype (for example repeated runs of that test, and a reading of the reader path it exercises). If the mechanism is found and lies in code this unit touches, the fix is in scope. Otherwise it is recorded as OBS-17 with what was tried.
- A recurrence on this unit's pull request is a red CI run that PR-35 root-causes. The test is never skipped, deselected, marked `xfail` or quarantined.

**ID-15. Run every updater consumer** (LR-O2, addendum 2.5). An updater change runs every test file that references `tools/evidence/update_evidence_index.py`: 24 at the baseline (§5.7), plus the QA harness tests.

**ID-16. A correction outside the plan's change set** (LR5-O2). If PR-30 or PR-35 must correct this unit's own change in a path outside the plan's change set, it records an in-flight decision with the path, reason, validation and review coverage. That is a rescope trigger (§14) only when the path is in §6's expected-unchanged list or the change is material.

**ID-17. Review findings and option A.**
- Findings are dispositioned under addendum 2.11 rule 7: fixed when they show a wrong result, a crash or a guarantee breach on a real input (ID-2); otherwise the reply gives the traced path and the stated limit and the thread is resolved. Declining a P1 or a security finding goes to the Product Owner first. PO-35-5 and PO-35-6 of the WU-PR-06 pull request are the standing default.
- Rule 8: two consecutive review rounds raising findings of the same class (the same component or contract) stop the fixing of instances; PR-35 asks the Product Owner one design question (narrow the design, accept a stated limit, or rescope).
- Option A (disposition record §3): this unit's PR-40 records any hosted CI failure that `python tools/ci/prepush_check.py replay` would have caught. PR-30 and PR-35 record each replay they run, with its outcome, so that PR-40 can state it.

## 5. Current repository and reference baseline (measured at `731f03c`)

Every fact below was measured by this IA at `731f03c` under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, database and GitHub keys unset), in detached scratch clones, with a scratch venv (CPython 3.12.3 with CI's install) whose editable install maps to a scratch checkout of `731f03c`. Every copy ended with an empty `git status --short --untracked-files=all`, except the copy where a file was removed on purpose (§5.4), which was restored. PR-20 re-verifies at its own head before planning edits.

### 5.1 Repository state

- `origin/main` `731f03c` (tree `540a0b588600`). `git diff --name-only fc51620 731f03c` lists only `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-work-unit-lineage-review-v1.0.md`, `docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md` and `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md`.
- Absent: `schemas/close_candidate_source.v2.json`, `docs/adr/hde/close_pack_writer_adr.md`, `audit/qa/hde-crd-0002/`, `audit/HDE-CRD-0002_*`, `audit/docdeltas/hde-crd-0002_*`.

### 5.2 Files of the unit

| Path | Lines | Bytes | Blob |
| :- | -: | -: | :- |
| `tools/qa/generate_epic_close_pack.py` | 3,869 | 142,791 | `4b5e57f46f32` |
| `schemas/epic_close_candidate_source.v1.json` | 214 | 8,298 | `10e337e96273` |
| `tests/qa/test_generate_epic_close_pack.py` | 4,274 | 163,343 | `e1c4ed58699b` |
| `tools/evidence/update_evidence_index.py` | 5,163 | 243,302 | `d98550cf60f3` |
| `tests/evidence/test_evidence_index_missing_state.py` | 1,245 | 56,809 | `aa22fda9c69d` |
| `ci/checks/classify_ci_changes.py` | 2,086 | 79,156 | `10a7155f3df2` |
| `tools/qa/qa_harness.py` | 3,999 | 150,784 | `c325fe6e51f1` |
| `.github/workflows/epic-closeout-validation.yml` | 98 | 3,108 | `959e4a6fb691` |
| `tools/evidence/run_sanity_pipeline.py` | 444 | 19,806 | `853566a0e4f7` |

- **`epic-closeout-validation.yml`:** `workflow_dispatch` with inputs `git_ref` and `candidate_source`; `permissions: contents: read`; one job `validate-closeout-candidate` (`timeout-minutes: 15`), env closed rails plus `GIT_OPTIONAL_LOCKS: "0"` and `GIT_NO_LAZY_FETCH: "1"`. Steps: checkout `persist-credentials: false` at `git_ref`; input and clean-head validation (the source must match `^[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*$`, be tracked, a regular file and not a symlink); Python 3.12; `python -m pip install 'jsonschema==4.23.0'` only; `generate_epic_close_pack.py --source "$CANDIDATE_SOURCE" --check`; the updater `--check`, `orientation_demo.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`; a final clean-checkout assertion. It reads no schema version. `audit/HDE-CRD-0002_close_candidate_source.json` matches its path pattern.
- **`run_sanity_pipeline.py`:** fifteen stages (`01 Environment pins` to `15 Final-LF validation`); none invokes `generate_epic_close_pack.py` or reads a candidate source. `git grep` of the writer's name and the v1 schema's name outside `docs/` finds only the workflow, `AGENTS.md`, `README.md`, HDE-EPIC039's frozen QA records, the classifier, `tests/evidence/test_rails_ci_workflow_integration.py`, the writer, its schema and its test.

### 5.3 The writer and schema (CLOSE01 B-1; Audit §5.6)

- **Imports:** the standard library, plus `jsonschema` (`Draft202012Validator`, `SchemaError`; a missing module is a dependency-readiness failure). `sys.dont_write_bytecode = True`.
- **Constants:** `SCHEMA_REL = "schemas/epic_close_candidate_source.v1.json"`, `SOURCE_SCHEMA_VERSION = "epic_close_candidate_source.v1"`, `MANIFEST_SCHEMA_VERSION = "epic_close_candidate_manifest.v1"`, `EPIC_RE` `HDE-EPIC(?P<number>[0-9]{3})\Z` (line 43); `FEEDBACK_DEPENDENCY_PATTERN` (line 46); the four `REPORT_SECTION_HEADINGS` (line 60); the ten `REPORT_BODY_LINES` (line 66); `REPORT_HEADING_RE` (line 96), which rejects the em dash; `CLOSED_RAILS` (line 116); the five `NONCLAIM_TEXT` entries (line 124), including "No QA PASS, acceptance, or token satisfaction is claimed.".
- **CLI** (lines 3797 to 3808): `--source` and a required mutually exclusive `--write` / `--check`.
- **Git access:** an in-process object store (`_GitObjectStore`, line 1,087; object, delta and pack decoding from line 1,004), with no subprocess.
- **Manifest (lines 2145 to 2170):** `candidate_posture: "candidate_only"`, `epic_id`, `inputs` (candidate source, evidence, plan and schema bindings), `nonclaims`, `outputs` (`close_manifest` path; `close_report` path, SHA-256 and size), `schema_version`. No `key_outputs` map in the manifest; the v1 **source** has a `key_outputs` object naming the two output paths.
- **v1 schema:** required and only properties `schema_version` (const), `epic_id` (`^HDE-EPIC[0-9]{3}$`), `plan_path`, `evidence_inputs` (1 to 128), `report_sections` (1 to 32), `key_outputs`, `nonclaims` (exactly 5); `additionalProperties: false`.
- **Tests:** 116 `def test_` functions. The closed sets are pinned at lines 418 (`REPORT_SECTION_HEADINGS`), 422 (`REPORT_BODY_LINES`), 597, 754 and 788 (parametrized over them) and 1000 (`NONCLAIM_TEXT`). OBS-17's test is at line 2848.
- **No tracked v1 candidate source exists:** `git grep` for `"schema_version": "epic_close_candidate_source.v1"` in tracked JSON finds none.
- **The refusal against the real Specification** (ID-3): applying the v1 `FEEDBACK_DEPENDENCY_RE` to the scope and acceptance-intent cells of the Specification's 22 requirement rows, by importing the baseline writer in a separate process, gives matches in two rows: S06 (`attestation`, in both cells) and S11 (`` `release_id` `` in the intent; `release identity` in the scope).

### 5.4 The updater (CLOSE01 B-2; M1)

- **Admission:** `ADMITTED_CRD_QA` (line 51) maps `HDE-CRD-0001` → (`audit/qa/hde-crd-0001`, `audit.qa.hde_crd_0001`) and `HDE-CRD-0002` → (`audit/qa/hde-crd-0002`, `audit.qa.hde_crd_0002`), "another CRD needs its own explicit row here".
- **CRD rows:** `_crd_qa_entry` (line 3933) builds the manifest row and `checks/<check_id>/primary.log` rows. `_load_crd_qa_entries` (line 3947) claims every row whose key starts with an admitted prefix or whose path lies under an admitted root, and refuses any path that is not the manifest or a six-part `…/checks/<check_id>/primary.log` ("CRD index key/path relationship is malformed"). For an existing root it validates the family with `qa_harness.validate_crd_check_family`, which reads the manifest and its listed primaries and does not scan the directory.
- **`publish_crd_check_family`** (line 5072): refuses a non-admitted ID, a foreign repository root or QA root, a nested transaction, an empty or duplicate family; runs `_run_once(check=True)` first; captures the planned logs and the manifest in a `_WriteTransaction`; calls `qa_harness.record_check_family`, `_converge_and_publish()`, `qa_harness.validate_crd_check_family` and the optional verifier inside the transaction.
- **CLI:** `--check`, `--rebind-sanity-log`, `--epic-id` (repeatable).
- **Static close-pack rows:** `EPIC022_PRIMARY_ARTIFACTS` (line 389) lists `audit/EPIC-022_close_report.md` and `audit/EPIC-022_MANIFEST.json`, among others; the static lists are concatenated unconditionally (around line 4095). Conditional loaders exist: `_load_epic036_pr01_entries` (line 1801) returns `[]` when its snapshot is absent.
- **Absent-tolerance, measured.** In a throwaway clone of `731f03c`: `update_evidence_index.py --check` exits 0 (0.95 s). With `audit/EPIC-022_close_report.md` removed, `--check` exits 1 and write mode exits 1, both with `FileNotFoundError: … audit/EPIC-022_close_report.md` from `_read_bytes` called by `_render_mirror` (line 4289) in `_run_once` (line 4661). The copy was restored and its status was empty.
- `audit/qa/` holds `hde-crd-0001/` (`00_meta/`, `checks/`, `qa_step_logs_manifest.json` and its path proof) and no `hde-crd-0002/`.
- **ADR precedents:** `docs/adr/hde/body_graphs_adr.md` (indexed, with a path proof) and `docs/adr/hde/release_attestation_scaling_adr.md` (not indexed; landed by #394).

### 5.5 Epic-only identity inventory (ID-4)

- Generic close-pack surfaces that accept only Epic identities: the v1 schema's `epic_id` pattern; the writer's `EPIC_RE`.
- Epic-specific families (unchanged by design): `tools/qa/epic021_qa.py` and `tools/qa/generate_epic025_close_pack.py` to `generate_epic029_close_pack.py`, each with fixed `audit/EPIC-0NN_*` paths.
- The read-only checks the close run uses: `validate_evidence_paths.py` (74 lines), `check_evidence_index_hash.sh`, `orientation_demo.py`, `check_final_lf.sh` and `check_lf_endings.py` contain no Epic or CRD identity rule; `check_mirror_schema.sh` lists `crd_id` and `epic_id` among the allowed Mirror keys.

### 5.6 Lanes and membership (by `python tools/ci/prepush_check.py lanes membership build-notes --path …`)

| Path | Lanes (classifier, given-path mode) |
| :- | :- |
| `schemas/close_candidate_source.v2.json` | refused: `CI_CHANGE_CLASSIFIER_ERROR:CI_PRODUCT_OWNER_TEST_MISSING:schemas/close_candidate_source.v2.json` |
| `schemas/epic_close_candidate_source.v1.json` | `product`, `compat`, `release`; 1 target |
| `tools/qa/generate_epic_close_pack.py` | `evidence`, `qa`; 2 targets |
| `tests/qa/test_generate_epic_close_pack.py` | `evidence`, `qa`; 1 target |
| `tools/evidence/update_evidence_index.py` | `evidence`, `release`; 2 targets |
| `tests/evidence/test_evidence_index_missing_state.py` | `evidence`; 0 targets |
| `tools/qa/qa_harness.py` | `evidence`, `qa`; 1 target |
| `ci/checks/classify_ci_changes.py` | all seven lanes; 166 targets |
| `docs/adr/hde/close_pack_writer_adr.md` | `documentation_only`, no lane |
| `audit/HDE-CRD-0002_close_report.md`; `audit/qa/hde-crd-0002/close/x/primary.log` | `evidence`; 0 targets |

- **Membership:** none of the nine unit paths is a release member (release `1.3.0`, 45 members, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`). No refresh is owed.
- **Build Notes:** `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md`, 271,926 bytes, SHA-256 `5c26c80b3eb6b36e305ee22b998a8e5d41156c5702d659827dd9b8fdc513ff35`.
- The tool's run left the scratch clone unchanged ("repository unchanged (tree, ignored files, directories, HEAD and git metadata)"). Its output is not CI's result, not QA and not evidence.

### 5.7 Baseline test runs

- `python -m pytest -q -p no:cacheprovider tests/qa/test_generate_epic_close_pack.py`: **405 passed** in 75.3 s (13:26:17Z to 13:27:33Z); exit 0. OBS-17 did not recur.
- The updater consumers (ID-15): the 23 test files below that reference `tools/evidence/update_evidence_index.py`, other than the writer's test, plus `tests/qa/test_generic_qa_harness.py`, in one run: **1,169 passed** in 807.7 s (13:27:33Z to 13:41:02Z); exit 0.
- Afterwards the copy's `git status --short --untracked-files=all` and `git diff` were empty.
- The 24 test files that reference the updater (`git grep -l update_evidence_index -- 'tests/*.py'`): `tests/config/test_config_artifacts.py`, `tests/config/test_typed_bundles.py`, `tests/evidence/test_engine_core_evidence.py`, `tests/evidence/test_evidence_index_env.py`, `tests/evidence/test_evidence_index_missing_state.py`, `tests/evidence/test_evidence_index_snapshot.py`, `tests/evidence/test_evidence_index_token_sets.py`, `tests/evidence/test_evidence_skeleton.py`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/evidence/test_hdapi_v2_contract_inventory.py`, `tests/evidence/test_hde_epic037_v2_adapter.py`, `tests/evidence/test_internal_version_manifest_captures.py`, `tests/evidence/test_machine_mirror_self_proof.py`, `tests/evidence/test_orientation_demo.py`, `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/evidence/test_release_attestation.py`, `tests/evidence/test_release_manifest_content_binding.py`, `tests/ops/test_evidence_index.py`, `tests/qa/test_epic020_qa_docs.py`, `tests/qa/test_epic024_bootstrap_status.py`, `tests/qa/test_generate_epic_close_pack.py`, `tests/qa/test_viability_generator_wrappers.py`, `tests/transport/test_internal_version_contract.py`, `tests/unit/test_check_agents_md_citations.py`.

## 6. Bounded files and components

| Path | Bound |
| :- | :- |
| `schemas/close_candidate_source.v2.json` (new) | IF-3 (ID-3 to ID-6) |
| `schemas/epic_close_candidate_source.v1.json` | retained, byte-unchanged |
| `tools/qa/generate_epic_close_pack.py` | the v2 model beside v1 (ID-3 to ID-7, ID-14) |
| `tests/qa/test_generate_epic_close_pack.py` | v2 tests; v1 tests kept |
| `tools/evidence/update_evidence_index.py` | the IF-4 entrypoint and reconciler change (ID-8); the conditional CRD close-pack registration (ID-9) |
| `tests/evidence/test_evidence_index_missing_state.py`, and any other existing updater test that must assert the new behaviour | updater tests (the plan names them) |
| `ci/checks/classify_ci_changes.py` | the v2 schema's registration and any other new file's (ID-11) |
| `tests/evidence/test_rails_ci_workflow_integration.py` | only where a pin enumerates the registry the new entry joins (ID-11) |
| `tools/qa/qa_harness.py` | only if rendering a close-run primary needs it, named in the plan (ID-8) |
| `docs/adr/hde/close_pack_writer_adr.md` (new) | the ADR draft, status `Proposed` (ID-12) |
| `docs/ephemeral/` PR result records | evidence obligations (§10) |

Expected unchanged, so that a needed change is a finding under §14:
- `.github/workflows/epic-closeout-validation.yml`, `.github/workflows/ci.yml` and every other workflow; `tools/evidence/run_sanity_pipeline.py` (ID-10);
- `requirements*.txt`, `pyproject.toml`, `pytest.ini`, `.gitignore`;
- every release member, `catalog/manifest.json`, `engine/config/registry_loader.py`;
- the Index trio, its sentinels, every path proof, the orientation output and every existing governed artifact or close pack (ID-9: no row changes at merge);
- `ADMITTED_CRD_QA`'s rows; `audit/qa/**`; `qa_step_logs_manifest.json` of any change;
- the per-epic close-pack generators and every other existing tool;
- `README.md`, `AGENTS.md`, `CHANGELOG.md` (WU-DOC-01), `docs/**` outside `docs/ephemeral/` and the new ADR; `docs/pfcanon/**`.

## 7. Exclusions

- **No close of anything.** No real close pack, candidate source, close-run family, doc-delta or drain-target ledger for HDE-CRD-0002 or any other change. No retroactive close pack for HDE-EPIC040 (Plan §15). Dry-run and rehearsal outputs live only under `tmp_path` or a throwaway copy.
- **No canon edit**, no PF10 addendum and no approval of the ADR (AQ-1 is the Product Owner's).
- **No new evidence family** other than the IF-4 home the ADR proposes; no acceptance token or token matrix.
- **No CI change.** No new workflow, job, step or lane; the validation workflow and release-sanity stages stay as they are (ID-10).
- **No new dependency**: the writer stays standard library plus `jsonschema` (ID-10).
- **No emulation** of git, GitHub Actions, YAML or packaging in new code (ID-13).
- **No write-mode run** of the updater or the writer in the session's checkout; write modes run only in throwaway copies or under `tmp_path`.
- **No live vendor, production or database call; no deployment.**
- **Tests:** no skipped, disabled, expected-failure or quarantined test.

## 8. Interface contracts with other units

| Contract | Consumer | Content |
| :- | :- | :- |
| H-1 Close sequence | HDE-CRD-0002's close mutation set | the commands, inputs and outputs of T1 to T6 as the PR result record states them, with the v2 source fields and the IF-4 entrypoint's call |
| H-2 Absent-tolerant registration | WU-PR-08 and every later updater run | neither file: no row; both: rows; one: refusal (ID-9) |
| H-3 IF-4 family | QA-10, HDE-CRD-0002's close | path form, key form, rendering source (captured command and outcome), transaction and verifiers; never touches `qa_step_logs_manifest.json` (ID-8) |
| H-4 Writer usage and posture | WU-DOC-01 (`AGENTS.md` "HDE-EPIC039 current workflow posture"; `README.md` line 25) | the v2 schema, both identities, the outputs, the nonclaims, as the PR result record states them |
| H-5 ADR | the Product Owner (AQ-1); PF drainage owners | the ADR's decision, canon locators and drainage statements (ID-12) |
| H-6 Validation workflow | the Product Owner's T7 dispatch | unchanged inputs; the writer stays runnable with `jsonschema==4.23.0` only (ID-10) |

## 9. Disposition rules PR-20 must apply and record

1. **Choices left to PR-20,** each recorded with its reason:
   - the v2 field shapes within IF-3, and how S06's and S11's text is expressed while identities still refuse (ID-3);
   - the v2 nonclaims (ID-5);
   - the IF-4 entrypoint's signature and the reconciler change (ID-8);
   - whether an Epic close-run family is admitted now or recorded as a limit (ID-8);
   - the registration form (ID-9, ID-11);
   - the ADR text (ID-12);
   - the OBS-17 diagnosis (ID-14).
2. **Ceiling.** State how the plan stays within ID-1's ceiling, with the spend so far.
3. **Real-input set.** State each component's real-input set and how inputs outside it are refused (ID-2).
4. **Prototype** in a throwaway copy: the v2 dry runs for both identities, the IF-4 publication under a fixture root, and the T0 to T6 rehearsal (acceptance (7)). T0's QA family in the rehearsal is produced by the real `publish_crd_check_family` in the copy, never written by hand. Record each command, exit status, duration and the copy's state before and after.
5. **Baseline re-check.** Re-measure §5.2 to §5.6 at the plan's head; record any difference before planning edits.
6. **Canon map.** A table from each element of §4.1 C1 to C7 to its source field, renderer and test (ID-5).
7. **Carried items.** Record each item of §15 with its disposition.
8. **Stale documents.** Name each document the change makes stale but this unit may not change, with its owner (WU-DOC-01, the Product Owner, or the PF drainage owner).

## 10. Acceptance, tests and evidence

**Plan v1.1 §7 WU-PR-07 acceptance**, verbatim, with the binding readings in brackets:
1. "A dry run writes a complete close pack for a synthetic `HDE-CRD-0002` candidate and for a synthetic Epic candidate into `tmp_path`, with the verbatim `QA Rails — Open/Close (Final PR)` heading, the pointers list, the binary decision, deferrals, later-drain statements and a manifest `key_outputs` map." [Every element of ID-5 and ID-6; the CRD candidate carries the Specification's 22 real requirement rows (ID-2, ID-3).]
2. "The feedback-dependency refusal still rejects run, receipt, attestation and commit identities in causal fields; candidate identity is tracked-path digests only." [ID-3; ID-7.]
3. "Check mode writes nothing and validates exact committed bytes." [ID-7.]
4. "The updater publishes and validates an IF-4 family under a fixture root without touching `qa_step_logs_manifest.json`." [ID-8; plus ID-9's three registration cases.]
5. "The ADR draft names Change Process Guide §3.5.2, HDE Schemas & Artifacts §1.2 "Close-pack artifacts" and Glow QA Guide "Close-pack truthfulness and same-run execution" / "Close report requirements" as affected canon with drain targets." [ID-12.]
6. "Lanes green (qa, evidence, release and any full-validation trigger)." [The classifier changes, so all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK` on the exact head.]
7. "An end-to-end rehearsal of the stated transition sequence for a synthetic `HDE-CRD-0002` candidate in a throwaway copy of the repository ends with the writer's check mode, `tools/evidence/update_evidence_index.py --check`, `ci/checks/check_mirror_schema.sh` and `ci/checks/check_evidence_index_hash.sh` exiting 0; a second run of the sequence is byte-stable; no byte the final state needs is produced by hosted CI." [Also the rest of the T4 set: `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_final_lf.sh`. The rehearsal also runs the writer's `--check` with only `jsonschema` importable beside the standard library, as the hosted job does (ID-10).]

**Evidence obligations.** The PR result record holds: the dry-run outputs (as test evidence, not governed evidence); the rehearsal's commands, exit statuses, durations and byte-stability comparison; the registration cases; the Epic-only inventory; the canon map; each check actually run, with counts; the OBS-17 diagnosis; the ceiling spend (ID-1); the replay lines (ID-17); the nonclaims (§12).

**Validation PR-20 plans** (minimum). Every item ran at the baseline in its read-only form (§5); the new tests and the rehearsal need the change to exist:
- `tests/qa/test_generate_epic_close_pack.py` (405 at the baseline), alone and repeated for OBS-17;
- every updater consumer (ID-15) and the QA harness tests;
- `tests/evidence/test_rails_ci_workflow_integration.py` and `tests/evidence/test_http_reader_ci_ownership.py`;
- `update_evidence_index.py --check` and the other read-only evidence checks on the candidate head, showing the Index byte-unchanged;
- the classifier dry run on the pull request's base and head (all seven lanes);
- the full `tests/` sweep in a detached copy with `ruby`, `bash` and `curl` on `PATH`, under closed rails, with `XDG_STATE_HOME` pointed at an empty scratch directory and the editable install mapping to the copy under test (OBS-W5-5); or `python tools/ci/prepush_check.py replay --full`, recorded under ID-17.

Each run that can write tracked files runs in a detached copy and ends with `git diff --exit-code` and an empty untracked status.

| Requirement | Acceptance item | Proof | Stage |
| :- | :- | :- | :- |
| S21 "produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD" | (1), (2), (3) | v2 writer tests; the dry runs; the canon map | PR-30; CI; PR-40 |
| S21 "close-workflow run evidence has a home … that does not reopen an approved QA manifest" | (4) | updater tests under a fixture root | PR-30; CI |
| S21 "the accompanying ADR is approved" | (5); AQ-1 | the ADR draft; the Product Owner's decision | PR-30; before merge |
| Plan "Terminal-state reachability" | (7) | the rehearsal | PR-30; PR-40 |
| M1 | (4), (7) | the three registration cases; the rehearsal | PR-30 |
| CD-1; PF12 §1.2 inventory | (1) | the CRD dry run; the inventory | PR-30 |
| Lanes | (6) | hosted CI on the exact head | PR-35 |

## 11. Migration and security constraints

- **Migration:** none. v1 stays; no existing close pack, Index row or QA record is rewritten.
- **Rollback:** Nathan's revert of the squash commit. No member changes, so no refresh.
- **Security** (PF10 addendum 2.3: the Codex code review is in the chain, the Codex security review is not; Plan v1.1 §7's "security review" wording is read under it):
  - closed rails for every run; the writer's `CLOSED_RAILS_REQUIRED` refusal kept;
  - no secret, token, key value, birth input, location or user identifier in a source field, output, test, record or commit. Close-run primaries record command text and outcomes, with environment values limited to the rails and determinism pins (`AGENTS.md` redaction rule);
  - paths in a source are validated as tracked, regular, non-symlinked repository-relative paths before use (the v1 rules kept);
  - the IF-4 entrypoint writes only under the admitted QA root's `close/` and the Index trio and companions, inside one recoverable transaction.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated PR session):
  - reads this instruction and its lineage, the Plan block in full, the writer, schema, updater, QA harness and canon on `main`;
  - re-checks the baseline (§9.5) and prototypes (§9.4);
  - writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/`: the choices of §9.1 with reasons, the ceiling statement, the real-input set, the canon map, the requirement-to-change/test map, ordered steps, validation, risks and recovery;
  - returns `AWAITING_PO_PROCEED` only for a complete plan within this scope and ceiling.
- **PR-30** (after Nathan's Proceed for that exact plan, against the business case and ceiling): recovers existing work first; implements only the planned files; tests and rehearses under §10; commits coherently; records spend; publishes `PR_CANDIDATE_PUBLISHED`; hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session): retrieves and dispositions the Codex code review findings under ID-17; retests and pushes coherent corrections (ID-16); verifies current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability; records spend; returns `MERGE_PENDING` without merging. The PR description states AQ-1's state.
- **PR description:** the `.github/pull_request_template.md` headings with the `AGENTS.md` content rules.
- **Merge:** after AQ-1, Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage, records the unit's cost against the ceiling (rule 3) and the option A line (ID-17), and on ACCEPT selects the next unit (WU-PR-08, whose S01 real-input fact is due before its PR-10; addendum 2.12 decision 4).
- **Nonclaims** every record keeps: the writer and family are capability only; no close pack of any change is produced; no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; the ADR is `Proposed` until the Product Owner decides.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect existing worktrees, branches, PRs and `docs/ephemeral/` before creating anything. A resumed session counts toward the ceiling (ID-1).
- **A failed prototype or rehearsal** leaves the session's checkout untouched: write modes run only in throwaway copies. Discard the copy and run again from a fresh clone; the restart rules of Plan v1.1 T7 apply to the rehearsal.
- **An ordinary defect in this instruction** returns to this IA through PR-10; a corrected instruction is a new version.
- **Abort** is only Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material** means a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or budget, schedule or risk needing Product Owner direction, which includes a projected or actual pass of ID-1's ceiling.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional support; RS-30 for revisions); this IA reviews it through RS-20.
- **After Proceed:** PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Expected triggers:** a needed change in an expected-unchanged path of §6 (the validation workflow, a release-sanity stage, a dependency, an existing governed artifact); an AQ-1 decision that differs from the draft; the ceiling; rule 8's design question.
- **Not a trigger:** an in-scope correction recorded under ID-16; a choice §9.1 leaves to PR-20; a `qa_harness.py` change the plan names under ID-8.

## 15. Unresolved items, carried observations and owners

| Item | Owner | State |
| :- | :- | :- |
| The choices of §9.1 | PR-20 session | In the plan |
| AQ-1 (the S21 ADR) | Product Owner | Before merge (ID-12) |
| M1 (review v1.1 §3) | this unit (ID-9) | Measured: Epic rows not absent-tolerant |
| "Unknown pending discovery" (workflow, release-sanity stage) | this instruction (ID-10) | Resolved: neither reads the schema version |
| OBS-17 | this unit (ID-14); QA tool and test owner through the IA if the mechanism is outside the unit | Real input; diagnose, never skip |
| LR-O2 (run every updater consumer) | this unit (ID-15) | 24 files at the baseline |
| Option A line (disposition record §3) | this IA at PR-40 (ID-17) | Carried |
| The ceiling and its counting | PR-20 to PR-35; this IA at PR-40 (ID-1) | 1 session spent |
| LR6-O2 (2.11's misnumbered references) | Product Owner (addendum 2.12 decision 3) | Read by wording here |
| LR6-O5 (the pre-push tool's `ci.yml` pin) | any PR that edits `ci.yml` | This unit does not |
| OBS-W5-5 (`hdctl` subprocess tests use the installed package) | this unit's sweep environment (§10) | A hazard here |
| OBS-4, OBS-14 (WU-PR-01): tests that rewrite tracked files or write under the repository root | this unit (tests run only in copies) | A hazard here |
| HDE-EPIC040's close records (CL-E-10 v1.0 to v1.2, CLOSE01, QAEV01) | none: historical | Not reopened; no retroactive close pack |
| WU-PR-08's S01 real-input fact | Product Owner (addendum 2.12 decision 4) | Not this unit |
| The current `release_id` `77204764…`, 45 members | this unit (`membership`: none of its paths is a member) | Carried |
| S19-R01 to S19-R07, X-01 to X-04, OBS-P4-1, OBS-P3-5, and the other carried OBS items | their named owners (addenda 2.10 and 2.12) | Not this unit |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict:
- **`key_outputs` values.** PF12 §1.2 allows a path string or a non-empty list; PF14 §37.3 says each value is a path string and the map is not a list. String values satisfy both (ID-6), and PF14 itself says "The manifest schema is owned by PF12". A reading that meets both sources is not a conflict.
- **The S21 canon change.** The writer that produces the close report and the post-verdict home are a canon change by the Specification's own statement. It is ADR-covered (Change Process Guide §1.0.5) and gated by AQ-1, not a conflict.
- **PF14 §37.2 "Close-pack generator"** names `tools/qa/generate_epic025_close_pack.py` for EPIC-025 only; it does not bind other changes. The ADR names it among the affected homes.
- **The Audit's `CRD-NNNN` prefix** was corrected by Plan v1.1 (R4) to the CRD ID itself, which is PF12 §1.2's rule.

Coverage read for this instruction (in this invocation):
- Change Process Guide §1.0.5, §1.0.6, §3.5.1 "Requirement" in full (including "Feedback-free terminal lifecycle" and "Exceptional closure record"), §3.5.2.1 in full, §3.5.2.3 (opening list);
- HDE Schemas & Artifacts §1.2 "Close-pack artifacts" and "Change-container compatibility (normative)", and "Close-pack manifest key_outputs (named binding map; normative)";
- HDE Mechanics Guide §37.2 "Governance & homes" (close report, doc deltas, manifest, generator, drainage posture) and §37.3 "Conventions" (`key_outputs`);
- Glow QA Guide "Close-pack truthfulness and same-run execution (normative)" and "Close report requirements (validator-bound; mechanical)";
- HDE Governance §9.7.3 (ADR ownership), §9.1.1, §9.1.2;
- PF10 addenda 2.11 and 2.12 in full, 2.5 in full; 2.3 and 2.1 (read in full earlier in this session, byte-unchanged);
- whole-canon searches for close pack, close report, `key_outputs`, ADR, CRD prefix and change-container identity.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Unit | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S21 "produces a canon-conforming close report and manifest" | every canon-required element, rendered from tracked inputs | ID-5; ID-6; canon map (§9.6) | WU-PR-07 | (1) | PR-30; CI; PR-40 |
| S21 "from tracked inputs" | no hosted or later-commit byte; tracked-path digests | ID-7 | WU-PR-07 | (2), (3) | PR-30; CI |
| S21 "for an Epic or a CRD" | both identity forms and their paths | ID-4 | WU-PR-07 | (1) | PR-30 |
| S21 "feedback-free" against the real content | identities refuse; HDE-CRD-0002's own requirement text is expressible | ID-3 (S06, S11 measured) | WU-PR-07 | (1), (2) | PR-30 |
| S21 "a home … that does not reopen an approved QA manifest" | the IF-4 family, published by the updater, never touching the QA manifest | ID-8 | WU-PR-07 | (4) | PR-30; CI |
| S21 "the accompanying ADR is approved" | drafted here, approved by the Product Owner before merge | ID-12; AQ-1 | WU-PR-07 | (5) | before merge |
| CD-1; PF12 §1.2 "MUST be identified and updated" | the Epic-only inventory | ID-4; §5.5 | WU-PR-07 | (1) | PR-30 |
| Plan T3 "absent-tolerant" (M1) | no row before the close; rows after; refusal when mixed | ID-9 (measured not absent-tolerant today) | WU-PR-07 | (4), (7) | PR-30 |
| Plan "Unknown pending discovery" | neither the workflow nor a stage reads the schema version | ID-10 | WU-PR-07 | (6) | PR-20 (re-check) |
| Plan "Terminal-state reachability" | T0 to T6 in a throwaway copy, byte-stable | §9.4; acceptance (7) | WU-PR-07 | (7) | PR-30; PR-40 |
| Addendum 2.11 rules 1 and 3 | the ceiling carried and stated | ID-1 | WU-PR-07 | — | PR-20; PR-40 |
| Addendum 2.11 rules 4 to 8 | real inputs, no emulation, dispositions, rule 8 | ID-2; ID-13; ID-17 | WU-PR-07 | — | PR-20 to PR-35 |

Checks against the full PR-20 contract:
- Its sole substantive input is `PR_INSTRUCTION_ID`.
- This instruction carries everything PR-20 needs: the Specification, Audit, Plan and review lineage; the PF10 path and overlays; the business case and ceiling; the baseline, loci, exclusions, interfaces and dependencies; acceptance, evidence, migration and security; recovery, rescope, merge ownership and the return owner.
- PR-20's step 2 forbids mutating the repository while planning. Its prototype runs in a throwaway copy, and its only writes are its own artifacts.
- Numeric domains and sentinels: the decision is binary `SATISFIED` / `NOT SATISFIED`; `key_outputs` values are path strings; no boolean enters a numeric field.
- Closed schemas: v1 is `additionalProperties: false` and stays; v2 is closed by the plan's design.
- No decisive comparison fails. Every fact in §5 was measured at `731f03c` by this IA.

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated top-level WU-PR-07 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Return to the IA:** PR-40 lineage review after Nathan's merge; rescope review through RS-20; same-owner correction of this instruction through PR-10.

## 19. TypeSafe reading for the receiving session (PR-20, WU-PR-07)

Action sent (v8.2): "Write, in a new dedicated session, the first detailed PR implementation plan, not yet reviewed, for one work unit of an approved change: extend an existing close-pack writer of about 3,900 lines and its 4,300-line test file to a new candidate-source schema version that accepts Epic and CRD identities and renders the canon-required close report and manifest, add a close-run evidence family and an absent-tolerant close-pack registration to the canonical evidence updater of about 5,200 lines with its tests, register the new paths in the CI classifier, and draft one architecture decision record. A ready instruction lists the files, contracts, baseline, cost ceiling and the terminal-state transition sequence; the planner prototypes and rehearses the sequence in a throwaway copy, no live provider call occurs, and a Product Owner Proceed, implementation, code review and lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.38 (confidence 0.73); rung probabilities low 0.00, medium 0.01, high 0.65, extra high 0.29, max 0.05, ultracode 0.00. Model probabilities Fable 5.1 0.13, Opus 5.5 0.83, Sonnet 5.5 0.04, Haiku 5.5 0.00 (confidence 0.77). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.085, Fable 5.1 at extra high 0.038, Fable 5.1 at max 0.007, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.008, Opus 5.5 at high 0.539, Opus 5.5 at extra high 0.241, Opus 5.5 at max 0.042, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.026, Sonnet 5.5 at extra high 0.012, Sonnet 5.5 at max 0.002, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-20T13:28:24Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-20T13:28:24Z; HTTP 200 in 0.74 s; 5522 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Which request.** The installed TypeSafe scoring skill's request v8.2 (`request-v8.2.json`) and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records.** The Notion row was not written (addendum 2.1). Nathan's pick for PR-20 is not stated. Nathan's pick for this PR-10 session is not stated; its reading is the disposition record's.

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.** Python 3.12 with CI's install (package-index access for `pip install -r requirements-dev.txt`), `ruby` on `PATH` for the contract-inventory test, `bash`, `curl` and git. Closed rails with the vendor, database and GitHub keys unset; the container sets several of them. Work in throwaway clones outside the session's checkout, and point the editable install at the copy under test (OBS-W5-5).
- **Run times observed.** The writer's test: 75 s. The updater check: 1 s. A full `tests/` sweep: about 17 to 28 minutes in this lineage; a full-validation replay: about 21 to 25 minutes.
- **Access.** No live vendor, production or database access is needed.
- **Order.** This instruction's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-07 / PR-10 / instruction 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-07 (S21) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state as of 2026-10-12T02:29:33.739Z). Receiver contract read: PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z) |
| role/stage | continuing whole-change IA / PR-10 |
| capture time | 2026-10-20T13:42:00Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | the Product Owner disposition record (Isis, https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2) and WU-PR-06 lineage review v1.0 |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `731f03c` (`docs/pfcanon/` last changed by `043fa91`, PF10 v13.6.3; every other PF file unchanged).

| Topic | Sources and sections |
| :- | :- |
| Instruction authority, content and readiness | PR-10 — Create PR Work-Unit Instructions — 100926.1 (read in full); PR-20 — Create Detailed PR Implementation Plan — 100926.1 (the receiver contract); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (PR Instructions are the IA's; Proceed per detailed PR plan; merges are Product Owner actions), §9.1.2 (canon precedence; in-flight documents; ID-1 to ID-17 rest on it), §9.7.3 (ADR stubs are Product Owner-owned; agents may draft) |
| Overlays and carried items | PF10-HDE-Build-Notes v13.6.3 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md`): addendum 2.11 in full (rules 1 to 8; "Scope and supersession"; "Epic, task, and status effects"); 2.12 in full (the numbering of 2.11; decisions 1 to 5; resume point); 2.5 in full (WU-PR-02 acceptance; OBS-17; AQ-1; LR-O2); 2.3 (reviewer chain); 2.1 (§19) |
| Close-pack files, lifecycle and canon change (C1, C2, C8) | Change Process Guide (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md`) §1.0.5 "Canon changes", §1.0.6, §3.5.1 "Requirement" ("Feedback-free terminal lifecycle"; "Exceptional closure record"), §3.5.2.1 "Close-pack files", §3.5.2.3 "Index and mirror trio (same authorized mutation set)" |
| Close-pack artifacts and identities (C3, C4, C5) | HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §1.2 "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", "Change-container compatibility (normative)", "Close-pack manifest key_outputs (named binding map; normative)" |
| Close-pack mechanics (C5, C6) | HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §37.2 "Governance & homes" (close report, doc deltas, manifest, generator, drainage posture), §37.3 "Conventions" (`key_outputs`) |
| Close report and same-run evidence (C7) | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) "Close-pack truthfulness and same-run execution (normative)", "Close report requirements (validator-bound; mechanical)" |
| In-flight documents | Specification v1.1: row S21, CD-1, constraint "Close-pack writer", Exclusions, canon impact, ADR status, Live QA class table, the Distillation row; Plan v1.1 §2, §5 IF-3 and IF-4, §6, §7 (common paragraph and the WU-PR-07 block in full), §9 items 1, 4 and 5, §11 R-4, §13 AQ-1, §15; review v1.1 §3 (M1); Audit §5.6, §6 S21, §7.1 EC-10, §8 AQ-1; the Product Owner disposition of 2026-10-20 in full; WU-PR-06 lineage review v1.0 (LR6-O2, LR6-O5, LR6-O8) through addendum 2.12; CLOSE01 result v1.0 §1.1 and §1.2 through the Audit |
| Operative documentation | `AGENTS.md`: canon-first rule; "HDE-EPIC039 current workflow posture" (the generic writer's invariants); "Evidence harness" and "Governed evidence rules"; closed rails and redaction; pytest readiness; "Code review guidelines" (Markdown excluded; the real-input rule) and "Code review scope"; "PR descriptions"; "Truncation/retrieval-failure guardrail" |

Silence: canon states no business-case content for WU-PR-07 beyond addendum 2.11 and the disposition record, and no rule for a close-run evidence family; the Specification and the ADR govern the latter.
