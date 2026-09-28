---
artifact_type: ALPHA_FEEDBACK_BRIEF
artifact_version: "1.0"
subject: QA-70 approved an incoherent QA Plan after QA-80; the QA planning prompts never test whole-plan coherence
requested_by: Nathan / Product Owner, 2026-09-27 ("Create a report as alpha feedback, because the prompts are failing")
author: Isis-51, Claude Code session https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq
route: GCFPE-MGMT-10 (prompt maintenance); prompt bodies are in Notion and are not edited here
prompts: QA-50, QA-70 and QA-80 of release GCFPE-20260914.1 (091426.1); Notion pages as of 2026-09-24, read in full
related: AF-021 to AF-024 on "GCFPE Alpha Feedback — Deferred Items — 091426.1"; docs/ephemeral/HDE-EPIC040-QA70-approval-revocation-v1.0.md; docs/ephemeral/HDE-EPIC040-QA70-planning-failure-rca-v1.1.md
---

# Alpha feedback: QA Plan approval never tests whole-plan coherence

## 1. What happened

On 2026-09-27 the Product Owner overturned two QA-70 approvals of the HDE-EPIC040 QA Plan.

| # | Review | Plan | Product Owner outcome | Failure |
| --- | --- | --- | --- | --- |
| 1 | Review v1.0, APPROVE | v1.0 | Rejected | The reviewer never read the rails canon, so a rails model that contradicted canon was approved (RCA v1.1; AF-024) |
| 2 | Review v1.2, APPROVE | v1.1, after QA-80 | Revoked: "abject failure" | The Plan was never judged as a whole. Checks that run nothing and a removed placeholder were approved |

Failure 2, step by step:

1. **QA-70 DENY (review v1.1).** The denial of Plan v1.0 carried 13 redlines.
   - RL-08: remove check 13, or re-posture it.
   - RL-09: record checks 12 and 14 as `PARKED`, with "No commands, inputs or probes".
2. **QA-80 revision.** QA-80 applied each redline once and preserved step identity, as its step 2 requires. The result:
   - Check 13 stays as a numbered placeholder, "kept for traceability".
   - Checks 12 and 14 stay as numbered checks that only write a `PARKED` record.
   - Of the 14 listed checks, two run nothing and a third is an empty heading.
   - Seven of the 12 executed checks (3 to 9) are built around pytest groups and validators that CI already ran on the delivering PRs. The Plan names that CI evidence and re-runs the groups "alongside it" (§10.1). Its only stated reason is a note in §10.2: CI was change-aware, so it never ran the full suite on the final tree.
   - The Plan is 951 lines (122,238 bytes) and includes a Python recording procedure for a human operator (§12).
3. **QA-70 APPROVE (review v1.2).** The same Isis session confirmed that each redline had been applied, then approved.
   - Its "Canon relied on" block was present, so AF-024's safeguard was in place and did not catch this. The failure was not a reading gap.
   - The review's own words: "In the text that QA-80 changed, I found no blocker." Checks 12 to 14 are text that QA-80 changed.

## 2. Why the prompts allowed it

| ID | Prompt | Cause |
| --- | --- | --- |
| R1 | QA-70 | A review after QA-80 runs in the same mode as a first review ("`INITIAL_QA_PLAN_REVIEW`: the Plan is pending first approval or a revised pending version after QA-80"). Nothing says what the second pass must do. Combined with Plan Templates' gate freeze ("do not introduce a new blocker from already-visible unchanged text"), the re-review shrinks to a redline-application audit. Nothing warns that a Plan can satisfy every redline and still be incoherent |
| R2 | QA-70 | The whole approval test is one sentence: "decide `APPROVE` only if the whole pending Plan is coherent, complete, bounded, and executable". "Coherent" has no operational test. Canon has concrete tests that the prompt does not point to (§3, item 1) |
| R3 | QA-80 | Step 2: "Apply each redline exactly once. Preserve all unaffected Plan content and existing step/attempt/evidence identity." A literal author keeps removed and parked checks in the collection to keep their identity. No step reshapes the Plan into a coherent runbook after the redlines are applied |
| R4 | QA-70, QA-80 | The redline author judges the result of its own redlines. QA-80 returns the Plan "in the same continuing Isis session", so the reviewer who chose RL-09's form judged its outcome. Neither prompt requires the combined effect of a redline set to be checked before the set is issued |
| R5 | QA-50 | QA-50 asks for "one complete change-wide `QA_PLAN` with uniquely identified steps, requirement/risk coverage, …", and Glow QA Guide §3.4.14 requires every criterion to be covered by a step. Neither says that a closed-rails criterion can be covered by binding existing CI or PR evidence instead of re-running it (§3.4.14 "Evidence binding"; §3.4.8). Neither requires a re-run to state what it adds. The Plan grew to the opposite of the human instruction file described in AF-022 and AF-023 |
| R6 | QA-50, QA-70, QA-80 | A minor gap. The identity rules make "explicit replacement" a reason to stop and clarify, and the vocabulary (`RETAIN_EXISTING`, `INITIAL_DEDICATED_ASSIGNMENT`, `NEW_DEDICATED`) has no value for a Product Owner-directed replacement of a continuing reviewer |

## 3. Request

These are changes for GCFPE-MGMT-10 to scope. The prompt bodies are Notion-managed and are not edited here.

1. **QA-70, coherence test.** Every approval must pass and state each of these tests, including approvals after QA-80:
   - Every listed check runs at least one command whose result decides its status. No placeholder, removed entry or record-only entry is listed as a check.
   - A requirement that is blocked by environment, deferred or out of scope is stated in the scope or deferral section, not as a check (Glow QA Guide §3.3).
   - Every check states what it proves that bound CI or PR evidence does not. A criterion already proven by bound evidence needs no re-run (Glow QA Guide §3.4.14; Plan Templates "Evidence coverage": no check "for good measure").
   - The named operator can execute the Plan as written (Plan Templates, approval materiality: "clear enough for the assigned operator").
2. **QA-70, review after QA-80.** Verifying the redlines is necessary but never sufficient. The reviewer re-reads the whole revised Plan and judges it as a first review would. Text produced by applying redlines is current-revision text, which the gate freeze does not protect.
3. **QA-80, runbook shape.** After applying the redlines, deliver a coherent runbook. Drop checks that no longer run, and record their IDs in the redline application report, not as placeholders in the Plan. Identity is preserved for the checks that remain.
4. **QA-70, DENY.** Before issuing a redline set, the reviewer states the check collection that results once every redline applies, and tests it against item 1.
5. **QA-50, re-runs.** A check that re-runs a closed-rails group CI already ran must state the gap it closes. Otherwise the criterion is covered by binding the CI evidence. Coordinate with AF-022 and AF-023.
6. **Identity.** Add a session disposition for a Product Owner-directed reviewer replacement, so the receiving session does not stop to clarify a replacement its handoff already records. The Isis-52 handoff uses `NEW_DEDICATED` and cites the revocation record.

## 4. Relation to existing entries

- **AF-024 (the "Canon relied on" block).** Necessary but not sufficient. Review v1.2 carried the block. This failure was about the scope of the review, not about reading.
- **AF-022 and AF-023 (QA as human instruction files).** Plan v1.1 shows what the current shape costs: 951 lines, 12 executed checks, and a hand operator told to run `python -c` harness calls.
- **AF-021 (the QA-90 handoff RCA).** A separate subject.

## 5. Acceptance for the prompt change

- A replay of QA-70 against `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.1.md` does not approve while checks 12, 13 and 14 remain in the collection.
- A replay of QA-80 against review v1.1's redlines produces a Plan in which every listed check runs a command.
- Each QA-70 approval states how it meets each test in §3, item 1.

## 6. Decision needed

Admit this to the Alpha Feedback list and route it to a GCFPE-MGMT-10 Modification.

## Canon relied on

Read from `docs/pfcanon/` on `main` (`bf6e8da`):

- **Plan Templates** (`PF27-Canon-Plan-Templates-v2.0.4.md`), each read in full: "Evidence coverage and optional legacy-token binding"; "Live QA Plan approval materiality discipline"; "Review stability and no-moving-target discipline".
- **Glow QA Guide** (`PF19-Canon-Glow-QA-Guide-v3.0.5.md`): §3.3; §3.4.8; §3.4.14.

Other sources:

- **Prompts**, read in full from Notion: QA-50 (page as of 2026-09-24T15:54:17.481Z), QA-70 (15:55:17.352Z) and QA-80 (15:55:48.777Z), all release GCFPE-20260914.1.
- **Alpha Feedback list:** "GCFPE Alpha Feedback — Deferred Items — 091426.1", entries AF-021 to AF-024 (read only).
- **In-flight documents, read in full:** QA Plan v1.1, reviews v1.1 and v1.2, and the QA-80 redline application report.
