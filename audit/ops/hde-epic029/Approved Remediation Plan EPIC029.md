# Remediation Plan — EPIC029

## Remediation Work Plan

### Work Item W-001

* Work type: VALIDATION
* Intent: Run a bounded gap-classification review for `HDE-CONJ009.1` and `HDE-CONJ008.1` to determine whether the remaining blocker is implementation, governed approval/evidence posture, or both.
* Why needed: The escalation proves those rows are not supportable to Done now, but does not prove whether the missing closure is technical or evidentiary.
* Dependencies: Thoth approval of the remediation path; access to the current governed epic029 artifacts referenced by the escalation and approved implementation plan.
* Risks: This may uncover broader implementation work than the escalation currently isolates.
* Evidence basis: Evidence pointer: Escalation Request -> ## Required Additional Work -> **Exact blocker classification:** evidence/proof blocker
  Evidence pointer: Escalation Request -> ## PF10 Readiness Findings -> **What PF10 says:** for the evidence gaps section, `HDE-CONJ009.1` and `HDE-CONJ008.1` are still ambiguous for drain-to-Done

### Work Item W-002

* Work type: PR
* Intent: Correct the remediation sequence so PF09 row-closing work occurs before any PR-04-style closure/binding work, and so `HDE-CONJ001.4` cannot be treated as sufficiently advanced while any intended environment remains `not yet closed`.
* Why needed: The approved implementation plan’s current sequence is part of the failure, not just the backdrop to it.
* Dependencies: Thoth approval; W-001 may refine exact scope but is not required to confirm the sequencing defect.
* Risks: Documentation/sequence correction alone can be mistaken for substantive closure if not tightly controlled.
* Evidence basis: Evidence pointer: Approved Implementation Plan -> # Execution plan -> 5. **PR-04** ... `and epic-close Live QA outputs being available`
  Evidence pointer: Approved Implementation Plan -> ## OPS-01 — Validate Codespaces and local-dev sampler harness bindings and capture explicit environment evidence -> **Success criteria:** `For each intended environment, either a validated DEV_SAMPLER_URL run is evidenced, or binding_disposition.md records not-yet-closed status with reason; no environment is silently assumed closed.`
  Canon check: PF09.4 — Canon-HDE-Build-Checklist-Conjunction, §Subtask HDE-CONJ001.4 — Dev/internal HTTP harness infra wiring

### Work Item W-003

* Work type: PR
* Intent: Execute the minimum additional PR remediation needed to make `HDE-CONJ009.1` and `HDE-CONJ008.1` truthfully supportable to Done now, based on the W-001 gap-classification outcome.
* Why needed: Those two rows are proven blockers to QA entry.
* Dependencies: W-001; W-002 sequencing correction approved.
* Risks: The work may be broader than evidence-only closure if W-001 finds unresolved implementation gaps.
* Evidence basis: Evidence pointer: Escalation Request -> ## Required Additional Work -> * **ID:** `PR-01`
  Evidence pointer: Escalation Request -> ## Required Additional Work -> * **ID:** `PR-02`
  Evidence pointer: Approved Implementation Plan -> # PF09 Completion Scope -> | `HDE-CONJ009` | `HDE-CONJ009.1` | Complete in this epic | `PR-01`, `PR-04` |
  Evidence pointer: Approved Implementation Plan -> # PF09 Completion Scope -> | `HDE-CONJ008` | `HDE-CONJ008.1` | Complete in this epic | `PR-02`, `PR-04` |

### Work Item W-004

* Work type: OPS
* Intent: Execute the minimum OPS remediation needed to close `HDE-CONJ001.4` across both intended environments with governed, per-environment closure evidence.
* Why needed: The escalation proves that the environment story is still open in both Codespaces and local dev.
* Dependencies: W-002 sequencing correction approved; availability of both intended environments.
* Risks: Additional infra/tooling gaps may surface, especially for local dev.
* Evidence basis: Evidence pointer: Escalation Request -> ## Required Additional Work -> * **ID:** `OPS-01`
  Evidence pointer: Escalation Request -> ## PF10 Readiness Findings -> **What PF10 says:** evidence is still missing for a clean Codespaces prod-mode gating rerun, and still missing for a published plus validated local-dev `DEV_SAMPLER_URL`.
  Canon check: PF09.4 — Canon-HDE-Build-Checklist-Conjunction, §Subtask HDE-CONJ001.4 — Dev/internal HTTP harness infra wiring

### Work Item W-005

* Work type: VALIDATION
* Intent: Re-run the PF09-backed readiness assessment after W-003 and W-004, and do not request QA entry unless all three controlling rows are then supportable to Done now.
* Why needed: The current escalation exists because readiness was attempted before the PF09 completion backbone was truly satisfied in substance.
* Dependencies: W-003 and W-004 completed; current governed evidence available.
* Risks: The rerun may still fail, in which case descoping or carry-forward will need fresh approval.
* Evidence basis: Evidence pointer: Escalation Request -> ## Decision -> Decision: NOT QA READY
  Evidence pointer: Escalation Request -> ## QA Readiness Analysis -> That is enough to stop QA honestly.

