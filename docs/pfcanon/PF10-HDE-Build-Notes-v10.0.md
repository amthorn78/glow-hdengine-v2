# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v10.0

Effective Date: 02/24/26  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## Purpose

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

**Precedence and versioning**

* For any topic explicitly covered in this scratchpad, its content **temporarily supersedes canon** until those changes are reviewed and merged into the relevant PF docs.

* If multiple addenda exist for the same or similar scope (for example “1.”, “2.”, “ 3.”), the **highest-numbered / latest addendum is the only authoritative one**.

* **Older scratchpad files are considered fully drained or obsolete.** Agents must **not** read, reuse, or reconcile content from older scratchpads once a newer one exists; only the latest file matters.

Within a single scratchpad file:

* When an entry has been drained into PF-Canon, that entry is **removed completely** from the scratchpad.

* The current version of the file therefore contains **only live, not-yet-merged items**. If a topic is not present in the latest scratchpad, assume its source of truth is the relevant PF-Canon doc.

  ## Cross-references

 Inside this file, all references to PF documents MUST be **titles-only** (for example “HDE-Phased Epics”, “Glow QA Guide”), never file names or version numbers in the body text.

When editing or extending this file, ChatGPT sessions must:

* Not restate PF content here.

* Link by **document title and section only**.

# 1\) TEMPLATE

TEMPLATE Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\>  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## 1.1 Addendum Index:

**This section should be considered current and authoritative. Index all addenda numbers listed below.**

1. 2.1 Planning Template Adherence Is Structural Only  
2. 2.2 Epic Implementation plans must not require extensive QA evidence; Ops tasks are not QA; QA planning is separate  
3. 2.3 Plans must not mandate PF document updates; Reality Audits updates are PO-only  
4. 2.4 Plan review posture: minor formatting artifacts are non-blocking  
5. 2.5 PR01 HDE-EPIC026  
6. 2.6 PR02 HDE-EPIC026  
7. 2.7 PR03 HDE-EPIC026  
8. 2.8 PR04 HDE-EPIC026  
9. 2.9 PR05 HDE-EPIC026  
10. 2.10 Epic Plans must include a Business Case section (Glow product framing)  
11. 2.11 PR06 HDE-EPIC026  
12. 2.12 PR07 HDE-EPIC026  
13. 2.13 PR08 HDE-EPIC026  
14. 2.14 Docs PR HDE-EPIC026  
15. 2.15 HDE-EPIC025 Dev Retrospective  
16. 2.16 QA planning reality and plan-created artifacts (PF23 consult, locus provenance lock, plan-created outputs)  
17. 2.17 Live QA evidence is checks-only; per-run nesting is disallowed  
18. 2.18 Live QA is discovery-led; inference and over-specification are disallowed

# 2\) Numbered Addenda

---

## 2.1 Planning Template Adherence Is Structural Only

Timestamp: 020226 10:40  
Details:

Rule (normative)

1. **Template adherence is structural only.** For all planning artifacts that use PF templates (including Epic Plans and QA Plans), reviewers MUST evaluate template adherence only for **structural completeness** (required sections present, required end marker present, required gates present). Header styling is not part of structural adherence.  
2. **Header formatting is a nit.** Reviewers MUST NOT request redlines that only:  
   a) change heading levels, or  
   b) add/remove bold/italics in headings, or  
   c) reformat headings for aesthetic alignment.  
   These are non-substantive and MUST NOT be requested as approval conditions.  
3. **Approval posture.** Any header-level or heading-style discrepancy MUST be treated as **non-blocking** (Suggestion only) and MUST NOT cause “Revise and Resubmit.” Review feedback MUST focus on executable substance: scope, acceptance/evidence posture, PF pointer correctness, existence-claim citations, and canon conflicts.  
4. **What still blocks (clarity).** This addendum does not relax structural requirements. Missing required sections, missing required end markers, missing PF09/PF14 pointers where required, invalid/non-PF references, or ungrounded existence claims remain valid blockers.

Non-goals

* This addendum does not change any template-required section set or end-marker requirements.  
* This addendum does not weaken existence-claim citation rules or canon-precedence rules.  
* This addendum does not change any QA or evidence obligations.

Drain targets (informational; to be executed when a drain is scheduled)

* PF27 — Plan Templates: add explicit “structural-only adherence” language in plan review guardrails.  
* PF06 — Epic Process Guide: add explicit “do not block on heading styling/levels” language to review posture.

## 2.2 Epic Implementation plans must not require extensive QA evidence; Ops tasks are not QA; QA planning is separate

Timestamp: 021126  
Details:  
Rule (normative)

1. Epic Implementation planning must not produce QA evidence.  
   Epic Implementation Plans and Implementation Guides MUST NOT require the production of extensive QA evidence artifacts. These planning artifacts may state QA objectives and closeout proof obligations, but they MUST NOT embed a full QA runbook or require that QA evidence be generated as part of implementation planning.  
2. QA planning is a separate deliverable.  
   QA planning and QA evidence production are owned by the Live QA Plan and QA execution artifacts. The Live QA Plan is where step intents, evidence expectations, and PASS/FAIL posture are specified and where governed QA evidence is produced and indexed.  
3. Ops tasks are not QA tasks.  
   Ops tasks are implementation tasks that change the runtime environment and cannot be performed by code changes alone (for example: service configuration, environment variable changes, secrets management, privileged infrastructure actions). Ops tasks MUST be tracked and evidenced as implementation work, not as QA work.  
4. Ops evidence is not a substitute for QA evidence.  
   Ops task completion evidence may be required for a feature to function, but it does not satisfy QA verification. QA verification still requires functional proof and the required QA evidence outputs defined in QA planning.  
5. Separation rule (no category mixing).  
   Planning artifacts MUST keep these categories distinct:  
   * Implementation work and deliverables (code and implementation changes)  
   * Ops tasks (environment changes)  
   * QA planning (verification plan and evidence posture)  
   * QA execution (functional runs and governed QA evidence)

Drain targets (required)

* Epic-Process-Guide: clarify that Implementation Plans and Implementation Guides must not require extensive QA evidence and that QA planning is separate. Clarify that Ops tasks are implementation work, not QA steps.  
* Glow QA Guide: clarify that QA planning and QA evidence production are owned by QA plans and QA execution artifacts, not by implementation planning artifacts.  
* Plan Templates: ensure Implementation Plan and Live QA Plan templates enforce the separation between implementation planning, ops tasks, and QA planning.

## 2.3 Plans must not mandate PF document updates; Reality Audits updates are PO-only

Timestamp: 021426

Details:

Rule (normative)

1. **Plans MAY check PF documents during planning and review.**  
   Planning artifacts (including Epic Plans, Implementation Plans, QA Plans, and derived templates) MAY instruct the reviewer or planner to **consult** PF documents (including Reality Audits) to confirm what PF currently states.  
2. **Plans MUST NOT mandate PF document updates.**  
   Planning artifacts MUST NOT require updates to any PF documents as part of the plan’s PR or OPS deliverables, acceptance posture, tracked issues, “confirming artifacts,” or completion criteria.  
3. **Reality Audits updates are PO-only.**  
   Updates to Reality Audits are a manual PO operation only. PR scope MUST NOT include Reality Audits edits, and plans MUST NOT mandate (or schedule) Reality Audits updates inside PR or OPS work.  
4. **Allowed documentation posture inside plans (informational only).**  
   Plans MAY include a “Doc deltas capture” or “Doc delta candidates” note. These notes MUST be explicitly non-mandatory and MUST NOT be expressed as a required PR or OPS task. Any PF doc maintenance implied by those notes is PO-owned and out of plan scope.  
5. **How plans MUST express “reality/existence confirmation.”**  
   If a plan requires confirming whether a component, route, contract, or locus exists, the plan MUST express confirmation in one of these allowed forms:  
   * **PF check (allowed):** “Check Reality Audits for the current recorded existence/locus statement.” This is a read-only check and MUST NOT imply an update.  
   * **Repo-local evidence (required when PF is silent/insufficient):** capture confirmation as repo-local evidence (for example: deterministic command output recorded into an audit artifact, a governed gate log, a QA step-log entry, or a test/probe result). The plan MUST NOT require turning that result into a PF update.  
6. **Review posture (blocking condition).**  
   Any plan that mandates a PF document update (including Reality Audits) as part of PR or OPS deliverables MUST be treated as non-portable and returned for revision.

Non-goals

* This addendum does not prohibit PF doc maintenance. It prohibits making PF doc edits a mandated output of plans or PR or OPS work.  
* This addendum does not change Reality Audits authority for existence claims, nor does it prohibit consulting Reality Audits during planning.

Drain targets (required)

* **Plan Templates:** allow PF checks as inputs; prohibit mandating PF edits as deliverables; include explicit “Reality Audits updates are PO-only” language.  
* **Epic Process Guide:** clarify that PF doc maintenance (including Reality Audits updates) is PO-owned and out of PR or OPS plan scope; allow PF checks during planning/review.  
* **Reality Audits:** add a brief “Update ownership: PO-only” note and point to the plan-template prohibition on mandated updates while allowing read-only checks.

## 2.4 Plan review posture: minor formatting artifacts are non-blocking

Timestamp: 021426

Details:

Rule (normative)

1. **Plan approval MUST NOT be blocked on minor formatting artifacts.**  
   Reviewers MUST NOT return a plan for revision solely because of cosmetic markup or rendering artifacts that do not change meaning, obligations, portability, or evidence posture.  
2. **Minor formatting artifacts MUST be recorded as Nits (or ignored), not Blockers.**  
   If noted, they MUST be classified as non-blocking and MUST NOT change the binary approval outcome.  
3. **Definition: “minor formatting artifact” (non-exhaustive).**  
   The following are minor formatting artifacts when they are plainly cosmetic:  
   * Escaped Markdown list markers (for example a leading `\*` that renders as a bullet)  
   * Backslashes inserted only for Markdown rendering or escaping  
   * Cosmetic whitespace differences (blank lines, indentation, alignment)  
   * Bold/italic marker differences that do not change the underlying words  
   * Bullet style differences that do not change meaning (hyphen vs asterisk)  
4. **Boundary: formatting that changes meaning is not “minor.”**  
   A formatting issue is NOT minor (and MAY be a Blocker under the normal gates) if it affects any of the following:  
   * Commands or code that must run as written  
   * Evidence outputs, filenames, or required lowercase ASCII paths  
   * Portability rules (for example references to external attachments)  
   * Quoted-carryover blocks that must be verbatim (for example “IG Approved” or “CA vetted” quote lines)  
   * Any statement of obligation (MUST/SHOULD) or acceptance posture  
5. **Review discipline.**  
   Reviewers SHOULD assume that minor formatting artifacts can be cleaned during editorial polish without impacting implementation readiness, and SHOULD focus blocking findings on semantic, portability, evidence, and canon alignment defects.

Non-goals

* This addendum does not relax portability, evidence, or canon alignment requirements.  
* This addendum does not require reviewers to enumerate or correct cosmetic artifacts; it only prohibits blocking approval on them.

Drain targets (required)

* **Plan Templates:** add a short rule stating that cosmetic formatting artifacts are non-blocking.  
* **Epic Process Guide:** add reviewer guidance to classify cosmetic formatting artifacts as Nits.  
* **Glow QA Guide:** add the same reviewer posture guidance for plan reviews that touch QA artifacts.

## 2.5 PR01 HDE-EPIC026

Provenance (Original → Remediation) (REQUIRED; primary)

* Implementation Doc defines PR-01 intent as creating an internal conjunction computation path returning a deterministic, canonically-emittable JSON envelope (no production surface changes unless required).  
  Source: Implementation Doc  
  Evidence pointer: Implementation Doc → \#\#\# **PR-01 — Conjunction canonical output contract \+ deterministic envelope** → **Intent (what must be true after PR)**  
* Implementation Doc constrains PR-01 to an internal compute contract, canonical-emitter compatibility, no new public endpoints, and preserving existing compatibility output for non-conjunction paths.  
  Source: Implementation Doc  
  Evidence pointer: Implementation Doc → \#\#\# **PR-01 — Conjunction canonical output contract \+ deterministic envelope** → **Implementation requirements (what-not-how; include PF doc citations when you use PF canon to add specificity)**  
* Implementation Doc calls out acceptance tokens including JSON canonical emission checks and AB↔BA identity.  
  Source: Implementation Doc  
  Evidence pointer: Implementation Doc → \#\#\# **PR-01 — Conjunction canonical output contract \+ deterministic envelope** → **Acceptance tokens (minimal list; explicit; do not invent)**  
* Original PR limits scope to two files (engine compute \+ contract test), consistent with “no new public endpoints” posture.  
  Source: Original PR  
  Evidence pointer: Original PR → \#\# Files (2) → engine/compat/compute.py  
* Original PR adds `_person_from_resolved(...)` and `conjunction_public(...)` that normalizes AB/BA ordering via `normalize_pair(...)` and reuses `compat_public(...)` to produce the conjunction envelope.  
  Source: Original PR  
  Evidence pointer: Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py  
  @@ \-1,45 \+1,86 @@  
* Original PR adds a conjunction contract test proving stable canonical bytes for repeated (left,right) calls, but only for the same ordering (no swapped-order assertion).  
  Source: Original PR  
  Evidence pointer: Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,87 @@  
* Remedial PR explicitly documents the gap as missing AB↔BA byte-identity proof tied to the ABBA identity acceptance posture.  
  Source: Remedial PR  
  Evidence pointer: Remedial PR → Review Summary → Main risk: the new test verifies “same inputs, same bytes” but does not exercise AB↔BA byte-identity (swap left/right), which the Approved Plan calls out as an acceptance posture requirement via COMPOSITE\_ABBA\_IDENTITY\_OK.  
* Remedial PR updates the conjunction contract test to include a swapped (right,left) call and asserts canonical byte identity across AB and BA.  
  Source: Remedial PR  
  Evidence pointer: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,98 @@  
* Remedial PR retains the same limited file scope (two files), maintaining the original “internal compute \+ tests” change-set boundary.  
  Source: Remedial PR  
  Evidence pointer: Remedial PR → \#\# Files (2) → engine/compat/compute.py  
* Remedial PR provides an execution proof line for the Implementation Doc’s basic QA command with a concrete pass indicator.  
  Source: Remedial PR  
  Evidence pointer: Remedial PR → \#\# Testing → Pass indicator line: \============================== 8 passed in 0.50s \===============================

Review Summary

* Original PR implemented the internal conjunction contract surface (`conjunction_public`) and a deterministic canonical-bytes test, aligning with the Implementation Doc’s “internal surface \+ canonical-emittable JSON envelope” scope.  
* Original PR’s new test validated “same inputs, same bytes” but did not validate AB↔BA (swap left/right) byte-identity, leaving the ABBA identity acceptance posture unproven.  
* Remedial PR strengthens the conjunction contract test by adding a swapped-order call and asserting canonical bytes are identical across AB and BA, directly addressing the missing acceptance posture proof.  
* Combined (net) change-set remains narrow (compute helper \+ compute contract \+ contract test) and does not expand into new HTTP endpoints or provider acquisition logic.  
* Remedial PR includes a concrete pytest run line and an “8 passed” indicator for the exact basic QA command named in the Implementation Doc.  
* No new governed evidence artifacts are introduced, matching the Implementation Doc’s “Proof is via deterministic tests and reuse of the existing canonical emitter” posture.  
* RCA section is included (triggered by fix/remediation language in the artifacts) and covers the AB↔BA identity proof gap and the remediation.

RCA (REQUIRED only if RCA trigger is active)  
A) Bug/Failure statement (1–3 sentences; quote key lines verbatim from evidence)  
“Main risk: the new test verifies “same inputs, same bytes” but does not exercise AB↔BA byte-identity (swap left/right), which the Approved Plan calls out as an acceptance posture requirement via COMPOSITE\_ABBA\_IDENTITY\_OK.”  
Evidence pointer: Remedial PR → Review Summary → Main risk: the new test verifies “same inputs, same bytes” but does not exercise AB↔BA byte-identity (swap left/right), which the Approved Plan calls out as an acceptance posture requirement via COMPOSITE\_ABBA\_IDENTITY\_OK.

B) Root cause(s) (numbered; 1–N)

1. Root cause statement: The Original PR’s conjunction canonical-bytes test only exercised repeated calls for the same (left,right) ordering and did not assert swapped-order (right,left) equivalence.  
   Evidence pointer(s): Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
   @@ \-1,52 \+1,87 @@  
2. Root cause statement: The acceptance posture for PR-01 includes an explicit AB↔BA identity requirement (COMPOSITE\_ABBA\_IDENTITY\_OK), so a test that omits swap-order proof is incomplete for acceptance.  
   Evidence pointer(s): Implementation Doc → \#\#\# **PR-01 — Conjunction canonical output contract \+ deterministic envelope** → **Acceptance tokens (minimal list; explicit; do not invent)**

C) Fix across PRs (bullets)

* Remedial PR adds a swapped-order conjunction computation (`swapped = conjunction_public(right, left, ...)`) and compares `swapped_bytes` to `first_bytes`, closing the AB↔BA identity proof gap.  
  Evidence pointer: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,98 @@  
* The compute contract already normalizes the input pair via `normalize_pair(...)`, so the remediation focuses on proving that invariant at the canonical bytes layer.  
  Evidence pointer: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py  
  @@ \-1,45 \+1,86 @@

D) Fix verification (bullets)

* Remedial PR includes the explicit swapped-order canonical bytes equality assertion (`assert first_bytes == swapped_bytes`) as the direct proof mechanism.  
  Evidence pointer: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,98 @@  
* Remedial PR shows the named pytest command and a concrete pass indicator line (“8 passed …”), supporting that the updated tests run successfully.  
  Evidence pointer: Remedial PR → \#\# Testing → Pass indicator line: \============================== 8 passed in 0.50s \===============================

Findings (includes mandatory diff/code review)

1. Observed (Remedial PR): `engine/compat/compute.py` adds `_person_from_resolved(...)` plus `conjunction_public(...)` that (a) extracts `person_uid`, (b) normalizes AB/BA ordering via `normalize_pair(...)`, and (c) reuses `compat_public(...)` to populate a deterministic conjunction envelope.  
   Why it matters: This is the core PR-01 surface required by the Implementation Doc; reuse-first plus normalization reduce drift and supports canonical emission determinism.  
   Evidence pointer(s): Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py  
   @@ \-1,45 \+1,86 @@  
2. Observed (Remedial PR): `tests/http/test_compat_endpoint_contract.py` adds `test_conjunction_contract_emits_stable_canonical_bytes()` that emits canonical bytes via `emit_public(...)`, asserts repeatability (`first_bytes == second_bytes`), asserts AB↔BA identity (`first_bytes == swapped_bytes`), and asserts newline termination (`endswith(b"\n")`).  
   Why it matters: This directly supplies acceptance proof for both canonical-bytes determinism and AB↔BA identity, aligning with the Implementation Doc acceptance posture.  
   Evidence pointer(s): Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
   @@ \-1,52 \+1,98 @@  
3. Observed (Implementation Doc \+ Remedial PR): Implementation requirements explicitly forbid broadening to new public endpoints and require preserving existing non-conjunction compat output; the net change-set remains confined to compute \+ test surfaces.  
   Why it matters: Keeps PR-01 within scope and reduces regression risk to production endpoint behavior.  
   Evidence pointer(s):  
   * Implementation Doc → \#\#\# **PR-01 — Conjunction canonical output contract \+ deterministic envelope** → **Implementation requirements (what-not-how; include PF doc citations when you use PF canon to add specificity)**  
   * Remedial PR → \#\# Files (2) → engine/compat/compute.py  
4. Observed (Remedial PR): The exact basic QA command specified for PR-01 is shown as executed with a concrete “8 passed” indicator.  
   Why it matters: Provides execution confidence that the added contract test and existing catalog/compat expectations still pass under the required command.  
   Evidence pointer(s): Remedial PR → \#\# Testing → Pass indicator line: \============================== 8 passed in 0.50s \===============================

Requirement Satisfaction Crosswalk (Original step → Remediated satisfaction)

1. Requirement label: Internal conjunction contract exists and returns deterministic, canonically-emittable JSON envelope  
   Original PR status: Satisfied  
   Evidence pointer(s) in Original PR supporting that status: Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py  
   @@ \-1,45 \+1,86 @@  
   Remedial PR change that addresses it: No behavioral change required; contract retained as implemented, while remediation focused on proof coverage.  
   Current status after remediation: Satisfied  
   Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py  
   @@ \-1,45 \+1,86 @@  
2. Requirement label: No new public endpoints; no provider acquisition logic; preserve existing compat output contract for non-conjunction paths  
   Original PR status: Satisfied  
   Evidence pointer(s) in Original PR supporting that status: Original PR → \#\# Files (2) → engine/compat/compute.py  
   Remedial PR change that addresses it: No expansion; remediation remains test-only strengthening while preserving narrow file scope.  
   Current status after remediation: Satisfied  
   Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → \#\# Files (2) → engine/compat/compute.py  
3. Requirement label: JSON canonical emission determinism proof exists (stable canonical bytes for repeated computation)  
   Original PR status: Satisfied  
   Evidence pointer(s) in Original PR supporting that status: Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
   @@ \-1,52 \+1,87 @@  
   Remedial PR change that addresses it: Extends the same test to add swap-order proof while retaining repeatability proof.  
   Current status after remediation: Satisfied  
   Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
   @@ \-1,52 \+1,98 @@  
4. Requirement label: COMPOSITE\_ABBA\_IDENTITY\_OK (AB↔BA byte-identity proof)  
   Original PR status: Not satisfied  
   Evidence pointer(s) in Original PR supporting that status: Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
   @@ \-1,52 \+1,87 @@  
   Remedial PR change that addresses it: Adds swapped-order computation and asserts `first_bytes == swapped_bytes`.  
   Current status after remediation: Satisfied  
   Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
   @@ \-1,52 \+1,98 @@  
5. Requirement label: Basic QA command passes: `python -m pytest tests/http/test_compat_endpoint_contract.py tests/http/test_endpoint_catalog.py`  
   Original PR status: Unclear  
   Evidence pointer(s) in Original PR supporting that status: Original PR → Validation instructions (tests/checks) → \* `python -m pytest tests/http/test_compat_endpoint_contract.py tests/http/test_endpoint_catalog.py`  
   Remedial PR change that addresses it: Provides concrete execution proof for the exact command with a pass indicator line.  
   Current status after remediation: Satisfied  
   Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → \#\# Testing → Pass indicator line: \============================== 8 passed in 0.50s \===============================  
   Notes (optional; 1 line): Search method: searched Original PR for "passed" (case: insensitive); scope: entire document; tool: manual scan; result: 0 hits.

Evidence Print (PASS PROOF; required; whole PR outcome)  
A) Acceptance coverage evidence (Implementation Doc)

* Internal conjunction contract surface exists and is deterministic/canonical-emittable: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py  
  @@ \-1,45 \+1,86 @@  
* Canonical bytes stability \+ newline termination \+ AB↔BA identity proof: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,98 @@  
* Scope constraint (no new public endpoints / no provider acquisition logic) upheld via narrow touched-file set: Remedial PR → \#\# Files (2) → engine/compat/compute.py

B) Evidence/verification posture now satisfied (Original step closure)

* Original step provided deterministic-bytes repeatability proof; remediation adds the missing AB↔BA identity proof by introducing a swapped-order computation and comparing canonical bytes.  
  Evidence pointer: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,98 @@

C) Token and gate evidence (names-only; do not invent)

* JSON\_CANONICAL\_CHECK\_OK  
  Evidence pointer(s): Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,98 @@  
* PREIMAGE\_RECOMPUTE\_OK  
  Evidence pointer(s): Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,98 @@  
* COMPOSITE\_ABBA\_IDENTITY\_OK  
  Evidence pointer(s): Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py  
  @@ \-1,52 \+1,98 @@

D) Test/CI proof

* ✅ python \-m pytest tests/http/test\_compat\_endpoint\_contract.py tests/http/test\_endpoint\_catalog.py  
  Pass indicator (verbatim): Pass indicator line: \============================== 8 passed in 0.50s \===============================  
  Evidence pointer: Remedial PR → \#\# Testing → Pass indicator line: \============================== 8 passed in 0.50s \===============================

E) Artifact/evidence outputs

* No new governed evidence artifacts introduced for this PR outcome (test-based proof only).  
  Evidence pointer: Implementation Doc → \#\#\# **PR-01 — Conjunction canonical output contract \+ deterministic envelope** → **Evidence outputs (paths \+ artifact names; include filenames; governed where applicable)**

## 2.6  PR02 HDE-EPIC026

Provenance (Original → Remediation) (REQUIRED; primary)

* PR-02 acceptance target is “Conjunction provider acquisition via BodyGraph resolver (SAFE rails)” with local-first \+ resolver acquisition, and close-back posture. Source: Implementation Doc. Evidence pointer: Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Intent (what must be true after PR)  
* Call-site wiring requirement: keep current path when inputs already resolved; otherwise resolve via resolver before computing. Source: Implementation Doc. Evidence pointer: Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Implementation requirements (what-not-how; include PF doc citations when you use PF canon to add specificity)  
* SAFE rails posture requirement: closed by default; open only with explicit env (SAFE\_MODE=0 \+ ALLOW\_NETWORK=1); close-back after open acquisition. Source: Implementation Doc. Evidence pointer: Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Rails posture (closed by default; open only with explicit env)  
* Original PR introduced `conjunction_public_resolved(...)` to resolve unresolved conjunction inputs using `resolve_db_user_id` and `resolve_bodygraph` before computing, with local\_lookup-first behavior. Source: Original PR. Evidence pointer: Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-62,25 \+65,131 @@ def conjunction\_public(payload: Dict\[str, object\]) \-\> Dict\[str, object):  
* Original PR added tests for closed rails refusal, open rails acquisition/persistence behavior (via stub), and close-back behavior. Source: Original PR. Evidence pointer: Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-149,25 \+152,149 @@ def test\_compat\_post\_rejects\_empty\_ids() \-\> None:  
* Original PR documented a bug risk: local cache hits can be vendor-shaped and miss `person_uid`, causing downstream `ValueError`. Source: Original PR. Evidence pointer: Original PR → \# Bug fix (automated) → Comment: `_resolve_party` returns the raw `local_lookup` record directly, but `conjunction_public` later requires a resolved shape with `person_uid` and raises `ValueError` otherwise. This means local cache hits for vendor payload records can break even under closed rails.  
* Original PR implemented the bug fix by normalizing mapping/cache hits into resolved shape using `_resolved_person_with_hint`, and added a regression test for vendor-shaped local payloads using a user-id hint. Source: Original PR. Evidence pointer: Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-35,50 \+35,59 @@ ; and Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-276,25 \+277,55 @@ def test\_conjunction\_resolved\_close\_back\_uses\_local\_data(monkeypatch) \-\> None:  
* Remedial PR captured remaining required fixes (docstring \+ default-closed behavior when env is missing/empty). Source: Remedial PR. Evidence pointer: Remedial PR → \#\# Original Prompt → "Ensure default closed env fallback when env is missing/empty"  
* Remedial PR updated `conjunction_public_resolved` docstring to explicitly describe call-site gating semantics and added a default closed env fallback. Source: Remedial PR. Evidence pointer: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]:  
* Remedial PR added regression test ensuring `env=None` defaults to closed rails and refuses without provider acquisition. Source: Remedial PR. Evidence pointer: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-191,50 \+191,88 @@ def test\_conjunction\_resolved\_closed\_rails\_missing\_refuses\_without\_provider(monk  
* Remedial PR provided QA proof by running the exact pytest command required by Implementation Doc, with a “13 passed” summary. Source: Remedial PR. Evidence pointer: Remedial PR → \#\#\# Testing → "============================== 13 passed in 0.78s \=============================="

Review Summary

* Original PR implemented a resolver-backed conjunction computation helper (`conjunction_public_resolved`) that resolves user-id inputs through existing resolver logic before computing compatibility.  
* Original PR established test coverage for the required rails behaviors: closed-rails refusal, open-rails acquisition path via stubbed resolver, and close-back behavior.  
* A bug risk around vendor-shaped cache payloads lacking `person_uid` was identified and addressed via normalization \+ regression test in the Original PR.  
* Remedial PR hardened SAFE rails determinism by ensuring missing/empty env defaults to closed rails, and aligned the call-site documentation with the intended gating semantics.  
* Remedial PR added explicit regression coverage for `env=None` default-closed behavior.  
* The combined outcome aligns with the Implementation Doc’s PR-02 intent and includes concrete QA proof (`13 passed`) for the exact required command.  
* Notable risk: correctness depends on the `local_lookup` contract reflecting resolver persistence (the code re-checks local\_lookup after a resolver “ok”); this behavior is exercised in the open-rails \+ close-back tests.  
* RCA section included (covers the local cache payload-shape bug fix and how it was verified post-remediation).

RCA (REQUIRED only if RCA trigger is active)  
A) Bug/Failure statement (1–3 sentences; quote key lines verbatim from evidence)  
"Comment: `_resolve_party` returns the raw `local_lookup` record directly, but `conjunction_public` later requires a resolved shape with `person_uid` and raises `ValueError` otherwise. This means local cache hits for vendor payload records can break even under closed rails."  
"Fix: add `_resolved_person_with_hint()` to convert a cache hit or mapping into the resolved shape if a `user_id` hint is available, and use it for mapping \+ cache hits."  
Evidence pointer: Original PR → \# Bug fix (automated) → Comment: `_resolve_party` returns the raw `local_lookup` record directly, but `conjunction_public` later requires a resolved shape with `person_uid` and raises `ValueError` otherwise. This means local cache hits for vendor payload records can break even under closed rails.

B) Root cause(s) (numbered; 1–N)

1. Root cause statement: `_resolve_party` treated `local_lookup` hits as “already resolved” and returned them without normalizing into a `person_uid`\-bearing shape required by the downstream conjunction computation.  
   Evidence pointer(s):  
* Original PR → \# Bug fix (automated) → Comment: `_resolve_party` returns the raw `local_lookup` record directly, but `conjunction_public` later requires a resolved shape with `person_uid` and raises `ValueError` otherwise. This means local cache hits for vendor payload records can break even under closed rails.  
* Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-122,74 \+131,76 @@

C) Fix across PRs (bullets)

* Original PR fix: Introduced `_resolved_person_with_hint(...)` and applied it to both mapping inputs and local cache hits so vendor-shaped payloads can be treated as resolved when a `user_id` hint is available.  
  Evidence pointer: Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-35,50 \+35,59 @@  
* Original PR fix: Added a regression test explicitly exercising the vendor-shaped local payload case using a `resolve_db_user_id(...)` hint.  
  Evidence pointer: Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-276,25 \+277,55 @@ def test\_conjunction\_resolved\_close\_back\_uses\_local\_data(monkeypatch) \-\> None:  
* Remedial hardening (related to deterministic posture): Ensured missing/empty env defaults to closed rails, reducing risk of accidental open-rails behavior at the call site.  
  Evidence pointer: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]:

D) Fix verification (bullets)

* The regression test for vendor-shaped local cache payloads exists in the combined change-set (introduced in Original PR).  
  Evidence pointer: Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-276,25 \+277,55 @@ def test\_conjunction\_resolved\_close\_back\_uses\_local\_data(monkeypatch) \-\> None:  
* Post-remediation verification: the required pytest command ran and passed (`13 passed`), covering the combined test suite for this file set.  
  Evidence pointer: Remedial PR → \#\#\# Testing → "============================== 13 passed in 0.78s \=============================="

Findings (includes mandatory diff/code review)

1. Observed (Original PR): Added imports to support resolver integration (`resolve_db_user_id`, `resolve_bodygraph`) and standardized error reporting (`VendorError`). Why it matters: this is foundational to implementing PR-02’s “resolver acquisition” and deterministic refusal behavior. Evidence pointer(s): Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-1,28 \+1,31 @@ ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Implementation requirements (what-not-how; include PF doc citations when you use PF canon to add specificity)  
2. Observed (Original PR): Added `conjunction_public_resolved(...)` plus helper logic that resolves inputs via local\_lookup-first, then resolver path, and computes conjunction output from resolved bodies. Why it matters: this is the core call-site wiring required by PR-02 (resolve before compute; preserve resolved fast-path). Evidence pointer(s): Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-62,25 \+65,131 @@ def conjunction\_public(payload: Dict\[str, object\]) \-\> Dict\[str, object): ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Implementation requirements (what-not-how; include PF doc citations when you use PF canon to add specificity)  
3. Observed (Original PR): Updated test imports to support asserting `VendorError` and invoking the new resolved conjunction helper. Why it matters: ensures tests can directly validate refusal vs acquisition behavior without changing endpoint surfaces (consistent with PR-02). Evidence pointer(s): Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-1,32 \+1,35 @@ ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Tests (add/adjust; what to cover)  
4. Observed (Original PR): Added tests validating closed rails refusal (no provider acquisition), open rails acquisition path (stubbed resolver \+ persistence), and close-back behavior (subsequent closed rails uses local data). Why it matters: directly satisfies PR-02’s required test posture for rails gating and close-back safety. Evidence pointer(s): Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-149,25 \+152,149 @@ def test\_compat\_post\_rejects\_empty\_ids() \-\> None: ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Tests (add/adjust; what to cover)  
5. Observed (Original PR): Added `_resolved_person_with_hint(...)` to normalize vendor/cache records into a resolved shape when a `user_id` hint exists. Why it matters: prevents a class of runtime errors where local cache records lack `person_uid`, improving determinism under closed rails. Evidence pointer(s): Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-35,50 \+35,59 @@  
6. Observed (Original PR): Updated `_resolve_party(...)` to use `_resolved_person_with_hint` for both mapping inputs and `local_lookup` hits, ensuring the downstream conjunction logic always receives a `person_uid`\-bearing resolved record (or raises a deterministic vendor error). Why it matters: closes the specific ValueError failure mode described in the bug statement and maintains safety for cached vendor payloads. Evidence pointer(s): Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-122,74 \+131,76 @@  
7. Observed (Original PR): Updated test imports to support a regression test that asserts `resolve_db_user_id(...)` is used as a hint when local cache records are vendor-shaped. Why it matters: test ensures the normalization/hint path remains wired and prevents regression. Evidence pointer(s): Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-1,33 \+1,34 @@  
8. Observed (Original PR): Added regression test for vendor-shaped local payload behavior (`test_conjunction_resolved_local_vendor_payload_uses_user_id_hint`). Why it matters: verifies the bug fix works in a realistic cache-hit scenario and remains compatible with close-back usage (closed rails using local data). Evidence pointer(s): Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-276,25 \+277,55 @@ def test\_conjunction\_resolved\_close\_back\_uses\_local\_data(monkeypatch) \-\> None:  
9. Observed (Remedial PR): Updated `conjunction_public_resolved` docstring to explicitly define call-site gating and SAFE rails semantics, and enforced default closed behavior when env is missing/empty via `resolver_env = env or {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}`. Why it matters: aligns implementation with PR-02’s “closed by default” rails posture and prevents accidental open-rails behavior when env is not provided. Evidence pointer(s): Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]: ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Rails posture (closed by default; open only with explicit env)  
10. Observed (Remedial PR): Added regression test verifying that `env=None` yields closed-rails refusal without provider acquisition. Why it matters: concretely enforces the default-closed requirement and prevents future regressions around env plumbing. Evidence pointer(s): Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-191,50 \+191,88 @@ def test\_conjunction\_resolved\_closed\_rails\_missing\_refuses\_without\_provider(monk  
11. Observed (Remedial PR): The required validation command was executed with a concrete “13 passed” summary. Why it matters: provides the acceptance/verification evidence posture required by the Implementation Doc for PR-02. Evidence pointer(s): Remedial PR → \#\#\# Testing → "============================== 13 passed in 0.78s \==============================" ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Basic QA task (exactly one) \+ pass condition

Requirement Satisfaction Crosswalk (Original step → Remediated satisfaction)

* Requirement label: Wire conjunction compute path to invoke existing bodygraph resolver/ingest acquisition at call site (resolve unresolved inputs before computing; keep resolved fast path)  
  Original PR status: Satisfied  
  Evidence pointer(s) in Original PR supporting that status: Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-62,25 \+65,131 @@ def conjunction\_public(payload: Dict\[str, object\]) \-\> Dict\[str, object):  
  Remedial PR change that addresses it: Kept the resolver acquisition path and clarified call-site gating in the docstring (no behavior regression; reinforced semantics).  
  Current status after remediation: Satisfied  
  Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]:  
  Notes (optional; 1 line): Resolver acquisition remains implemented via `resolve_db_user_id` \+ `resolve_bodygraph` and is now explicitly documented at the call site.  
* Requirement label: Ensure SAFE rails are enforced at call site (closed rails: no provider; open rails: acquire if local missing; close-back)  
  Original PR status: Satisfied  
  Evidence pointer(s) in Original PR supporting that status: Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-149,25 \+152,149 @@ def test\_compat\_post\_rejects\_empty\_ids() \-\> None:  
  Remedial PR change that addresses it: Clarified the gating semantics and ensured missing/empty env defaults to closed rails, tightening enforcement for the “closed by default” posture.  
  Current status after remediation: Satisfied  
  Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]:  
  Notes (optional; 1 line): Close-back behavior is exercised by tests asserting local data usage after an open-rails acquisition.  
* Requirement label: Rails posture is closed by default; open only when SAFE\_MODE=0 and ALLOW\_NETWORK=1 explicitly set  
  Original PR status: Not satisfied  
  Evidence pointer(s) in Original PR supporting that status: Original PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-62,25 \+65,131 @@ def conjunction\_public(payload: Dict\[str, object\]) \-\> Dict\[str, object):  
  Remedial PR change that addresses it: Added `resolver_env = env or {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}` so missing/empty env is treated as closed rails.  
  Current status after remediation: Satisfied  
  Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]:  
  Notes (optional; 1 line): This aligns with Implementation Doc’s default-closed posture.  
* Requirement label: Tests cover closed rails \+ missing input refusal, open rails \+ missing input acquisition path invoked with persistence hook called  
  Original PR status: Satisfied  
  Evidence pointer(s) in Original PR supporting that status: Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-149,25 \+152,149 @@ def test\_compat\_post\_rejects\_empty\_ids() \-\> None:  
  Remedial PR change that addresses it: Added explicit regression test for env=None default-closed refusal to strengthen coverage for the closed-by-default posture.  
  Current status after remediation: Satisfied  
  Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-191,50 \+191,88 @@ def test\_conjunction\_resolved\_closed\_rails\_missing\_refuses\_without\_provider(monk  
  Notes (optional; 1 line): Combined suite also includes close-back and vendor-shaped cache regression coverage.  
* Requirement label: QA (exact command) run with pass proof  
  Original PR status: Unclear  
  Evidence pointer(s) in Original PR supporting that status: Original PR → \#\#\# Testing → "✅ python \-m pytest tests/http/test\_compat\_endpoint\_contract.py tests/http/test\_endpoint\_catalog.py \-q"  
  Remedial PR change that addresses it: Re-ran the exact command with full pytest output including pass summary.  
  Current status after remediation: Satisfied  
  Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → \#\#\# Testing → "============================== 13 passed in 0.78s \=============================="  
  Notes (optional; 1 line): Search method: searched Original PR for "passed in" (case: insensitive); scope: whole bundle; tool: grep; result: 0 hits.  
* Requirement label: Deliverables: Provide changed file paths and a short note describing resolver integration point and gating behavior  
  Original PR status: Satisfied  
  Evidence pointer(s) in Original PR supporting that status: Original PR → \#\# Actions Taken → Files (2):  
  Remedial PR change that addresses it: Re-stated the exact changed files and documented the corrected default-closed gating behavior as part of the remedial actions.  
  Current status after remediation: Satisfied  
  Evidence pointer(s) in Remedial PR proving the current status: Remedial PR → \#\# Actions Taken → Exact files changed:  
  Notes (optional; 1 line): Both bundles include an implementation note describing resolver integration and rails behavior.

Evidence Print (PASS PROOF; required; whole PR outcome)  
A) Acceptance coverage evidence (Implementation Doc)

* Resolver acquisition wired at call site (local-first, resolve missing, compute after resolution): Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]: ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Implementation requirements (what-not-how; include PF doc citations when you use PF canon to add specificity)  
* SAFE rails enforcement with default-closed posture: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]: ; Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-191,50 \+191,88 @@ def test\_conjunction\_resolved\_closed\_rails\_missing\_refuses\_without\_provider(monk ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Rails posture (closed by default; open only with explicit env)  
* Required rails behavior tests (closed refusal, open acquisition, close-back): Original PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-149,25 \+152,149 @@ def test\_compat\_post\_rejects\_empty\_ids() \-\> None: ; Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Tests (add/adjust; what to cover)

B) Evidence/verification posture now satisfied (Original step closure)

* Default-closed env fallback implemented and regression-tested (`env=None`): Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]: ; Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-191,50 \+191,88 @@ def test\_conjunction\_resolved\_closed\_rails\_missing\_refuses\_without\_provider(monk  
* Concrete QA proof for the exact required command is present (`13 passed`): Remedial PR → \#\#\# Testing → "============================== 13 passed in 0.78s \=============================="

C) Token and gate evidence (names-only; do not invent)

* None (Implementation Doc → \#\#\# **PR-02 — Conjunction provider acquisition via BodyGraph resolver (SAFE rails)** → Acceptance tokens)

D) Test/CI proof

* Command (verbatim): `python -m pytest tests/http/test_compat_endpoint_contract.py tests/http/test_endpoint_catalog.py`  
  Pass indicator (verbatim): "============================== 13 passed in 0.78s \=============================="  
  Evidence pointer: Remedial PR → \#\#\# Testing → "============================== 13 passed in 0.78s \=============================="

E) Artifact/evidence outputs

* Code/test outputs shipped (paths as evidenced by diffs):  
  * engine/compat/compute.py (resolver acquisition \+ SAFE rails default-closed hardening)  
    Evidence pointer: Remedial PR → engine/compat/compute.py → diff \--git a/engine/compat/compute.py b/engine/compat/compute.py | @@ \-119,81 \+119,90 @@ def \_birth\_fields(raw: object) \-\> Tuple\[str | None, str | None, str | None\]:  
  * tests/http/test\_compat\_endpoint\_contract.py (rails behavior tests \+ env None regression)  
    Evidence pointer: Remedial PR → tests/http/test\_compat\_endpoint\_contract.py → diff \--git a/tests/http/test\_compat\_endpoint\_contract.py b/tests/http/test\_compat\_endpoint\_contract.py | @@ \-191,50 \+191,88 @@ def test\_conjunction\_resolved\_closed\_rails\_missing\_refuses\_without\_provider(monk

## 2.7  PR03 HDE-EPIC026

Review Summary

* PR adds two dev-only HTTP GET endpoints for conjunction preview (`/dev/sampler/conjunction`, `/dev/reader/conjunction`) and gates them via `APP_ENV` (dev/test/local) to prevent production access.  
* PR updates the endpoint catalog to register both dev-only endpoints with dev-harness metadata and non-public posture.  
* PR adds minimal tests covering: catalog entries, prod gating denial, closed-rails refusal semantics, and an open-rails 200-path smoke check.  
* A follow-up bug-fix step regenerates endpoint-catalog checksum/path-proof sidecars after catalog byte changes to restore integrity verification.  
* Scope appears aligned with the Approved Plan’s PR-03 intent (dev sampler+reader conjunction endpoints \+ catalog entries) and keeps changes localized to HTTP adapter, endpoint catalog artifacts, and tests.  
* Test/evidence posture looks sufficient for PR-03’s stated Basic QA requirement (pytest for endpoint catalog), plus adds focused dev-gating/wiring checks.  
* Notable risk: the “open rails success” smoke test may implicitly depend on vendor/provider behavior through `conjunction_public_resolved(...)`; ensure it remains deterministic and non-flaky across environments.  
* RCA section included: PR Artifacts contain an explicit bug-fix remediation for catalog sidecar regeneration.

Diff Review (REQUIRED; primary technical review)

DR-001

* Change summary: Add conjunction-related imports into the HTTP reader adapter (categories order \+ conjunction contract \+ DB/user/vendor helpers).  
* Risk assessment: Low  
* Why it matters: Introduces new dependencies that must remain stable and safe under dev-only posture.  
* Evidence pointer:  
  * PR Artifacts → adapter/http\_reader.py → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py  
  * PR Artifacts → adapter/http\_reader.py → @@ \-1,38 \+1,42 @@  
* Approved Plan linkage: Approved Plan → PR-03 — Dev sampler \+ reader conjunction endpoints \+ catalog entries

DR-002

* Change summary: Add shared conjunction handler helpers and call `conjunction_public_resolved(...)`, including rails-env wiring and VendorError mapping.  
* Risk assessment: Medium  
* Why it matters: This is the core behavior path for the new endpoints (inputs parsing, rails posture, refusal semantics, canonical emission).  
* Evidence pointer:  
  * PR Artifacts → adapter/http\_reader.py → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py  
  * PR Artifacts → adapter/http\_reader.py → @@ \-501,50 \+505,118 @@ def get\_reader\_bp(emit\_fn=None):  
* Approved Plan linkage: Approved Plan → Implementation requirements (what-not-how; include PF doc citations when you use PF canon to add specificity)

DR-003

* Change summary: Register the two new dev-only GET routes and enforce dev-only gating via `_dev_admin_gate()`.  
* Risk assessment: Low  
* Why it matters: Ensures the endpoints exist and remain dev-only (blocked outside dev/test/local).  
* Evidence pointer:  
  * PR Artifacts → adapter/http\_reader.py → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py  
  * PR Artifacts → adapter/http\_reader.py → @@ \-569,50 \+641,66 @@ def get\_reader\_bp(emit\_fn=None):  
* Approved Plan linkage: Approved Plan → Add new dev-only endpoints

DR-004

* Change summary: Update the endpoint catalog JSON to add dev-only conjunction routes with dev-harness metadata.  
* Risk assessment: Medium  
* Why it matters: Catalog bytes are governed/validated; changes must remain consistent with validation and integrity sidecars.  
* Evidence pointer:  
  * PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json b/artifacts/audit/ENDPOINTS\_CATALOG.json  
  * PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → Update docs/ENDPOINTS\_CATALOG.json to include both new endpoints with correct metadata.

DR-005

* Change summary: Add new dev-endpoint smoke tests for prod gating denial, closed-rails refusal, and open-rails success.  
* Risk assessment: Medium  
* Why it matters: Confirms dev-only gating and handler wiring; the open-rails test must not introduce flakiness or hidden external dependencies.  
* Evidence pointer:  
  * PR Artifacts → tests/http/test\_dev\_conjunction\_http.py → diff \--git a/tests/http/test\_dev\_conjunction\_http.py b/tests/http/test\_dev\_conjunction\_http.py  
  * PR Artifacts → tests/http/test\_dev\_conjunction\_http.py → @@ \-0,0 \+1,61 @@  
* Approved Plan linkage: Approved Plan → Tests (minimal, reuse-first)

DR-006

* Change summary: Extend endpoint catalog validation test to assert both dev conjunction routes exist with dev-only posture.  
* Risk assessment: Low  
* Why it matters: Ensures catalog validation explicitly covers the newly added endpoints.  
* Evidence pointer:  
  * PR Artifacts → tests/http/test\_endpoint\_catalog.py → diff \--git a/tests/http/test\_endpoint\_catalog.py b/tests/http/test\_endpoint\_catalog.py  
  * PR Artifacts → tests/http/test\_endpoint\_catalog.py → @@ \-1,25 \+1,41 @@  
* Approved Plan linkage: Approved Plan → Basic QA task (exactly one) \+ pass condition

DR-007

* Change summary: Regenerate the audit-side sha256 sidecar for the endpoint catalog mirror.  
* Risk assessment: Low  
* Why it matters: Restores integrity verification after catalog byte changes.  
* Evidence pointer:  
  * PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256  
  * PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → Evidence outputs (paths \+ artifact names; include filenames; governed where applicable)

DR-008

* Change summary: Update the docs catalog path-proof sidecar to match the new catalog bytes (size/sha256).  
* Risk assessment: Low  
* Why it matters: Keeps governed path-proof metadata aligned with the changed catalog bytes.  
* Evidence pointer:  
  * PR Artifacts → docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → diff \--git a/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt  
  * PR Artifacts → docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → @@ \-1,5 \+1,5 @@  
* Approved Plan linkage: Approved Plan → Evidence outputs (paths \+ artifact names; include filenames; governed where applicable)

DR-009

* Change summary: Update the docs sha256 manifest for `docs/ENDPOINTS_CATALOG.json`.  
* Risk assessment: Low  
* Why it matters: Ensures `sha256sum -c` style verification for the docs catalog passes after catalog updates.  
* Evidence pointer:  
  * PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256 → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256 b/docs/ENDPOINTS\_CATALOG.json.sha256  
  * PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256 → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → Evidence outputs (paths \+ artifact names; include filenames; governed where applicable)

DR-010

* Change summary: Update the path-proof sidecar for `docs/ENDPOINTS_CATALOG.json.sha256`.  
* Risk assessment: Low  
* Why it matters: Keeps integrity metadata consistent for the sha256 manifest artifact itself.  
* Evidence pointer:  
  * PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt  
  * PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt → @@ \-1,5 \+1,5 @@  
* Approved Plan linkage: Approved Plan → Evidence outputs (paths \+ artifact names; include filenames; governed where applicable)

RCA

A) Bug/Failure statement (1–3 sentences; quote key lines from PR Artifacts)  
“Updating this catalog entry changes the bytes served by `docs/ENDPOINTS_CATALOG.json` … but the commit does not regenerate the governed checksum/path-proof sidecars, so integrity verification now fails …”  
Evidence pointer: PR Artifacts → \#\# Original Prompt (auto-generated) → Title: \[P1\] Regenerate catalog sidecars after endpoint catalog update

B) Root cause(s)

1. Root cause statement: Endpoint catalog bytes were updated, but corresponding checksum/path-proof sidecars were not regenerated, causing hash validation mismatches.  
   Evidence pointer(s):  
   * PR Artifacts → \#\# Original Prompt (auto-generated) → Comment: Updating this catalog entry changes the bytes served by `docs/ENDPOINTS_CATALOG.json` (it points to this file), but the commit does not regenerate the governed checksum/path-proof sidecars

C) Fix in this PR

* Regenerated the endpoint catalog checksum sidecars for both docs and audit mirror artifacts.  
* Refreshed governed path-proof sidecars to align integrity metadata with the regenerated artifacts.  
  Evidence pointer(s):  
* PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → diff \--git a/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256 → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256 b/docs/ENDPOINTS\_CATALOG.json.sha256  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt

D) Fix verification

* Proof that integrity checks and catalog validation pass is present in PR Artifacts test/check inventory.  
  Evidence pointer(s):  
* PR Artifacts → \#\#\# Testing → ✅ sha256sum \-c docs/ENDPOINTS\_CATALOG.json.sha256  
* PR Artifacts → \#\#\# Testing → ✅ pytest \-q tests/http/test\_endpoint\_catalog.py

Findings

1. (DR-001) Observed: HTTP adapter imports now include `CATEGORIES_ORDER_V1` and `conjunction_public_resolved`, plus `resolve_db_user_id` and `VendorError`.  
   Why it matters: Confirms the new endpoints are wired to an existing conjunction contract surface and have explicit vendor-error handling.  
   Evidence pointer(s):  
* PR Artifacts → adapter/http\_reader.py → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py  
* PR Artifacts → adapter/http\_reader.py → @@ \-1,38 \+1,42 @@  
2. (DR-002) Observed: New helper `_emit_conjunction_response()` parses `a_*` / `b_*` query parameters, constructs `rails_env` using `SAFE_MODE`/`ALLOW_NETWORK`, calls `conjunction_public_resolved(...)`, and emits canonical JSON via `emit_public(..., sort_keys=True)`.  
   Why it matters: This is the main correctness surface for conjunction preview; rails posture and canonical emission must remain deterministic and contract-compatible.  
   Evidence pointer(s):  
* PR Artifacts → adapter/http\_reader.py → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py  
* PR Artifacts → adapter/http\_reader.py → @@ \-501,50 \+505,118 @@ def get\_reader\_bp(emit\_fn=None):  
3. (DR-003) Observed: Both new routes are gated via `_dev_admin_gate()` and return `ERR_WRITER_FORBIDDEN` 403 outside dev/test/local.  
   Why it matters: Meets the “dev-only” requirement and prevents these endpoints from becoming production/public surfaces.  
   Evidence pointer(s):  
* PR Artifacts → adapter/http\_reader.py → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py  
* PR Artifacts → adapter/http\_reader.py → @@ \-569,50 \+641,66 @@ def get\_reader\_bp(emit\_fn=None):  
4. (DR-004) Observed: Endpoint catalog adds `/dev/reader/conjunction` and `/dev/sampler/conjunction` entries as `classification":"dev_harness"` and `a7_eligible":false`, with env gate `APP_ENV in {dev,test,local}`.  
   Why it matters: Ensures discoverability/validation of the new endpoints while clearly marking non-public posture; also changes governed bytes requiring sidecar alignment (addressed in later hunks).  
   Evidence pointer(s):  
* PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json b/artifacts/audit/ENDPOINTS\_CATALOG.json  
* PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json → @@ \-1 \+1 @@  
5. (DR-005) Observed: New tests assert prod gating denial (403 \+ `ERR_WRITER_FORBIDDEN`), closed-rails refusal (503 \+ `ERR_WRITER_RAILS_CLOSED`), and open-rails success (200 \+ `conjunction` structure present).  
   Why it matters: Provides direct safety/acceptance coverage for gating and rails behavior; the open-rails test should remain stable and not require uncontrolled external dependencies.  
   Evidence pointer(s):  
* PR Artifacts → tests/http/test\_dev\_conjunction\_http.py → diff \--git a/tests/http/test\_dev\_conjunction\_http.py b/tests/http/test\_dev\_conjunction\_http.py  
* PR Artifacts → tests/http/test\_dev\_conjunction\_http.py → @@ \-0,0 \+1,61 @@  
6. (DR-006) Observed: Catalog validation test now explicitly checks both dev conjunction endpoints exist and are dev-harness with `a7_eligible` false.  
   Why it matters: Aligns with Approved Plan PR-03’s Basic QA posture and reduces risk of catalog drift.  
   Evidence pointer(s):  
* PR Artifacts → tests/http/test\_endpoint\_catalog.py → diff \--git a/tests/http/test\_endpoint\_catalog.py b/tests/http/test\_endpoint\_catalog.py  
* PR Artifacts → tests/http/test\_endpoint\_catalog.py → @@ \-1,25 \+1,41 @@  
7. (DR-007) Observed: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256` updated to match the new catalog bytes (`49adad3…`).  
   Why it matters: Repairs integrity verification for the audit mirror after catalog changes (prevents evidence/CI hash failures).  
   Evidence pointer(s):  
* PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256  
* PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 → @@ \-1 \+1 @@  
8. (DR-008) Observed: `docs/ENDPOINTS_CATALOG.json.path_proof.txt` updated size/sha256 metadata (`size_bytes: 1447`, `sha256: 49adad3…`).  
   Why it matters: Keeps governed path-proof sidecar consistent with the new served catalog bytes.  
   Evidence pointer(s):  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → diff \--git a/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → @@ \-1,5 \+1,5 @@  
9. (DR-009) Observed: `docs/ENDPOINTS_CATALOG.json.sha256` updated to the new hash line for `docs/ENDPOINTS_CATALOG.json`.  
   Why it matters: Ensures `sha256sum -c docs/ENDPOINTS_CATALOG.json.sha256` succeeds after catalog update.  
   Evidence pointer(s):  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256 → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256 b/docs/ENDPOINTS\_CATALOG.json.sha256  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256 → @@ \-1 \+1 @@  
10. (DR-010) Observed: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt` sha256 metadata updated for the sha256 manifest artifact.  
    Why it matters: Completes the integrity chain for the endpoint catalog and its checksum manifest.  
    Evidence pointer(s):  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt  
* PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt → @@ \-1,5 \+1,5 @@

Evidence Print (PASS PROOF; required)

A) Tokens satisfied (names-only; do not invent)

* None (no acceptance/QA/evidence tokens are explicitly claimed as satisfied by PR Artifacts or the Approved Plan for PR-03).

B) Evidence artifacts produced/updated

* Path: artifacts/audit/ENDPOINTS\_CATALOG.json  
  * Type: json  
  * Key proof facts:  
    * “"path":"/dev/reader/conjunction"”  
    * “"path":"/dev/sampler/conjunction"”  
  * Evidence pointer: PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json → @@ \-1 \+1 @@  
* Path: artifacts/audit/ENDPOINTS\_CATALOG.json.sha256  
  * Type: sha256  
  * Key proof facts:  
    * “+49adad306ed1828241ab5f113e968589c48c0a590cb68abe7693a27f8c9363c5”  
  * Evidence pointer: PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 → @@ \-1 \+1 @@  
* Path: docs/ENDPOINTS\_CATALOG.json.path\_proof.txt  
  * Type: text  
  * Key proof facts:  
    * “+size\_bytes: 1447”  
    * “+sha256: 49adad306ed1828241ab5f113e968589c48c0a590cb68abe7693a27f8c9363c5”  
  * Evidence pointer: PR Artifacts → docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → @@ \-1,5 \+1,5 @@  
* Path: docs/ENDPOINTS\_CATALOG.json.sha256  
  * Type: sha256-manifest  
  * Key proof facts:  
    * “+49adad306ed1828241ab5f113e968589c48c0a590cb68abe7693a27f8c9363c5 docs/ENDPOINTS\_CATALOG.json”  
  * Evidence pointer: PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256 → @@ \-1 \+1 @@  
* Path: docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt  
  * Type: text  
  * Key proof facts:  
    * “+sha256: 82f4c3f56e447a762d37a0e3af12cce93bc1588e8f17f185c35884dc091e2342”  
  * Evidence pointer: PR Artifacts → docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt → @@ \-1,5 \+1,5 @@

C) Test/CI proof

* Job/test name: python \-m pytest tests/http/test\_endpoint\_catalog.py tests/http/test\_dev\_conjunction\_http.py  
  * Pass indicator: “✅ python \-m pytest tests/http/test\_endpoint\_catalog.py tests/http/test\_dev\_conjunction\_http.py”  
  * Where it appears in PR Artifacts: PR Artifacts → \#\#\# Testing → ✅ python \-m pytest tests/http/test\_endpoint\_catalog.py tests/http/test\_dev\_conjunction\_http.py  
* Job/test name: python \-m pytest tests/http/test\_endpoint\_catalog.py  
  * Pass indicator: “✅ python \-m pytest tests/http/test\_endpoint\_catalog.py”  
  * Where it appears in PR Artifacts: PR Artifacts → \#\#\# Testing → ✅ python \-m pytest tests/http/test\_endpoint\_catalog.py  
* Job/test name: python \-m pytest tests/http/test\_dev\_conjunction\_http.py  
  * Pass indicator: “✅ python \-m pytest tests/http/test\_dev\_conjunction\_http.py”  
  * Where it appears in PR Artifacts: PR Artifacts → \#\#\# Testing → ✅ python \-m pytest tests/http/test\_dev\_conjunction\_http.py  
* Job/test name: sha256sum \-c docs/ENDPOINTS\_CATALOG.json.sha256  
  * Pass indicator: “✅ sha256sum \-c docs/ENDPOINTS\_CATALOG.json.sha256”  
  * Where it appears in PR Artifacts: PR Artifacts → \#\#\# Testing → ✅ sha256sum \-c docs/ENDPOINTS\_CATALOG.json.sha256  
* Job/test name: pytest \-q tests/http/test\_endpoint\_catalog.py  
  * Pass indicator: “✅ pytest \-q tests/http/test\_endpoint\_catalog.py”  
  * Where it appears in PR Artifacts: PR Artifacts → \#\#\# Testing → ✅ pytest \-q tests/http/test\_endpoint\_catalog.py

Doc Deltas (PF-Canon only; REQUIRED; with Canon Check Gate)  
CHG-001: Added two dev-only conjunction preview HTTP endpoints and gating behavior in the HTTP reader adapter.

* Evidence pointer: PR Artifacts → adapter/http\_reader.py → @@ \-569,50 \+641,66 @@ def get\_reader\_bp(emit\_fn=None):  
* Canon basis: CANON SILENCE  
  CHG-002: Updated endpoint catalog to include the new dev-only conjunction endpoints as dev-harness and non-public.  
* Evidence pointer: PR Artifacts → artifacts/audit/ENDPOINTS\_CATALOG.json → @@ \-1 \+1 @@  
* Canon basis: CANON SILENCE  
  CHG-003: Added/extended tests for endpoint catalog coverage and dev gating/wiring smoke checks.  
* Evidence pointer: PR Artifacts → tests/http/test\_dev\_conjunction\_http.py → @@ \-0,0 \+1,61 @@  
* Canon basis: CANON SILENCE  
  CHG-004: Regenerated checksum/path-proof sidecars for endpoint catalog artifacts after catalog byte changes.  
* Evidence pointer: PR Artifacts → docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → @@ \-1,5 \+1,5 @@  
* Canon basis: CANON SILENCE

## 2.8 PR04 HDE-EPIC026

Review Summary

* Adds a new dev-only writer HTTP endpoint (`/dev/writer/conjunction`) that returns an idempotent writer-style envelope for conjunction results, gated by the existing dev admin gate.  
* Refactors writer request canonicalization/preimage building to support the new endpoint and reuse existing error-envelope behavior on non-200 conjunction outcomes.  
* Updates the endpoint catalog to include the new endpoint path and route id.  
* Updates and extends tests to cover the new dev writer endpoint (including idempotence behavior) and to assert endpoint catalog inclusion.  
* Includes a follow-up bug fix to update endpoint-catalog sha256 sidecars to match the updated catalog content.  
* Overall scope appears aligned to Approved Plan PR-04; the diff set is concentrated to the HTTP adapter, endpoint catalog artifacts, and targeted tests.

Diff Review (REQUIRED; primary technical review)

DR-001  
Change summary: Add a dedicated route id constant for the new dev writer conjunction endpoint.  
Risk assessment: Low  
Why it matters: A stable `route_id` is required for catalog consistency and writer-envelope hashing/idempotence.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-21,50 \+21,51 @@ from engine.db.errors import AdapterError, PrimaryUnavailable  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-002  
Change summary: Introduce `_build_writer_request_preimage()` and route writer-conjunction preimage construction through it.  
Risk assessment: Medium  
Why it matters: This canonicalization/hashing path drives idempotence behavior and must remain stable and correct across inputs.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-167,64 \+168,77 @@ def \_writer\_idempotence\_cache\_key(writer\_hash: str) \-\> str:  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-003  
Change summary: Extend conjunction responder to accept explicit `left/right`, and implement `_emit_dev_writer_conjunction_response()` producing a writer envelope with idempotence tracking.  
Risk assessment: Medium  
Why it matters: This is the core behavior change (new endpoint shape \+ idempotence), and it must preserve existing error-envelope behavior and not regress existing dev conjunction endpoints.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-316,35 \+330,114 @@ def \_emit\_writer\_diagnostic\_response() \-\> Response:  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-004  
Change summary: Add `/dev/writer/conjunction` route to the HTTP blueprint and gate it with `_dev_admin_gate`.  
Risk assessment: Medium  
Why it matters: Ensures the new writer endpoint is dev-only and cannot be accessed without the existing dev admin gate.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-826,31 \+919,43 @@ bp \= Blueprint("http\_reader", **name**)  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-005  
Change summary: Update the endpoint catalog JSON to include `/dev/writer/conjunction` (GET) with `route_id` `dev.writer.conjunction.v1`.  
Risk assessment: Low  
Why it matters: Catalog accuracy is required for endpoint discovery/verification and for keeping tests aligned to the shipped HTTP surface.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json b/artifacts/audit/ENDPOINTS\_CATALOG.json ; @@ \-1 \+1 @@  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-006  
Change summary: Update dev conjunction HTTP tests to cover the new `/dev/writer/conjunction` route and verify idempotence behavior.  
Risk assessment: Medium  
Why it matters: This is the primary regression protection for the new endpoint, including rails gating expectations and idempotent response behavior.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/tests/http/test\_dev\_conjunction\_http.py b/tests/http/test\_dev\_conjunction\_http.py ; @@ \-1,61 \+1,92 @@  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-007  
Change summary: A second patch hunk repeats the same `tests/http/test_dev_conjunction_http.py` file-level hunk.  
Risk assessment: Low  
Why it matters: Duplicate patch hunks can create reviewer confusion; functionally it appears to restate the same net file change in the artifact bundle.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/tests/http/test\_dev\_conjunction\_http.py b/tests/http/test\_dev\_conjunction\_http.py ; @@ \-1,61 \+1,92 @@  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-008  
Change summary: Update endpoint catalog tests to assert `/dev/writer/conjunction` path and `dev.writer.conjunction.v1` route id are present.  
Risk assessment: Low  
Why it matters: Keeps catalog verification strict and ensures the new endpoint is accounted for in catalog governance.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/tests/http/test\_endpoint\_catalog.py b/tests/http/test\_endpoint\_catalog.py ; @@ \-35,11 \+35,13 @@ def test\_endpoint\_catalog\_has\_required\_paths():  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-009  
Change summary: Update `artifacts/audit/ENDPOINTS_CATALOG.json.sha256` to the new digest after catalog change.  
Risk assessment: Low  
Why it matters: The sha256 sidecar must match the updated catalog content to prevent integrity/verification mismatches.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

DR-010  
Change summary: Update `docs/ENDPOINTS_CATALOG.json.sha256` to the new digest after catalog change.  
Risk assessment: Low  
Why it matters: Keeps the docs-facing checksum aligned with the catalog digest expected by verification checks.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256 b/docs/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@  
Approved Plan linkage: Approved Plan → **PR-04 — Dev writer conjunction endpoint (gated) \+ idempotent writer envelope**

RCA

A) Bug/Failure statement (1–3 sentences; quote key lines from PR Artifacts)  
The PR artifacts explicitly flag a checksum mismatch risk after the catalog update: “High priority bug: The endpoint catalog was updated but the sidecar sha256 files were not updated.”  
Source evidence: PR Artifacts → Bug Fix → High priority bug:

B) Root cause(s)

1. Root cause statement: The endpoint catalog content changed, but the corresponding sha256 sidecars were not regenerated as part of the initial change.  
   Evidence pointer(s): PR Artifacts → Bug Fix → \[P1\] Regenerate endpoint catalog checksum  
2. Root cause statement: The required sha256 sidecars exist in two locations and both required synchronized updates.  
   Evidence pointer(s): PR Artifacts → Bug Fix → Update artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 and docs/ENDPOINTS\_CATALOG.json.sha256

C) Fix in this PR

* Updated `artifacts/audit/ENDPOINTS_CATALOG.json.sha256` to match the new catalog content.  
  Evidence pointer: PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@  
* Updated `docs/ENDPOINTS_CATALOG.json.sha256` to match the new catalog content.  
  Evidence pointer: PR Artifacts → Diff → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256 b/docs/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@

D) Fix verification

* Targeted catalog/tests were run per the PR artifacts.  
  Evidence pointer: PR Artifacts → Actions Taken → ✅ python \-m pytest tests/http/test\_endpoint\_catalog.py tests/http/test\_dev\_conjunction\_http.py  
* The sha256 sidecars now contain updated digest lines (indicating regeneration occurred).  
  Evidence pointer: PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@

Findings

1. (DR-001) Observed: A new constant `_DEV_WRITER_CONJUNCTION_ROUTE_ID = "dev.writer.conjunction.v1"` was added.  
   Why it matters: Ensures consistent writer route identification across hashing/idempotence and endpoint catalog expectations.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-21,50 \+21,51 @@ from engine.db.errors import AdapterError, PrimaryUnavailable  
2. (DR-002) Observed: `_build_writer_request_preimage()` centralizes method/route/query/body canonicalization and hash generation, and the writer conjunction preimage path now delegates to it.  
   Why it matters: Centralization reduces duplication but increases coupling; correctness of canonical bytes and `hash` stability are critical to idempotence behavior.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-167,64 \+168,77 @@ def \_writer\_idempotence\_cache\_key(writer\_hash: str) \-\> str:  
3. (DR-003) Observed: `/dev/writer/conjunction` response is built as a writer envelope with `ok`, `writer` metadata (including `hash`), and a `result` populated from the conjunction computation; non-200 conjunction responses are returned as-is.  
   Why it matters: Matches the intended “idempotent writer envelope” behavior while preserving existing error-envelope behavior for invalid inputs.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-316,35 \+330,114 @@ def \_emit\_writer\_diagnostic\_response() \-\> Response:  
4. (DR-004) Observed: The new `/dev/writer/conjunction` route is added under the existing blueprint and gated via `_dev_admin_gate()`.  
   Why it matters: Prevents accidental exposure of a dev writer endpoint without the established dev-admin access control.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-826,31 \+919,43 @@ bp \= Blueprint("http\_reader", **name**)  
5. (DR-005) Observed: Endpoint catalog now includes an entry with `"path":"/dev/writer/conjunction","method":"GET","route_id":"dev.writer.conjunction.v1"`.  
   Why it matters: Catalog/test alignment prevents drift and supports any downstream catalog-based validation.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json b/artifacts/audit/ENDPOINTS\_CATALOG.json ; @@ \-1 \+1 @@  
6. (DR-006) Observed: Dev conjunction HTTP tests add coverage for `/dev/writer/conjunction`, including an idempotence check comparing repeated identical requests.  
   Why it matters: Provides regression protection for the new endpoint’s writer envelope and idempotence guarantees.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/tests/http/test\_dev\_conjunction\_http.py b/tests/http/test\_dev\_conjunction\_http.py ; @@ \-1,61 \+1,92 @@  
7. (DR-007) Observed: The PR artifacts include a duplicate `tests/http/test_dev_conjunction_http.py` patch/hunk with the same `@@ -1,61 +1,92 @@` header.  
   Why it matters: While the net change described appears identical, duplication in the artifacts can reduce review clarity and should be avoided in future bundles.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/tests/http/test\_dev\_conjunction\_http.py b/tests/http/test\_dev\_conjunction\_http.py ; @@ \-1,61 \+1,92 @@  
8. (DR-008) Observed: Endpoint catalog tests now explicitly assert both the path and the route id for the new dev writer conjunction endpoint.  
   Why it matters: Ensures catalog integrity checks will fail if the endpoint is removed/renamed without updating governance artifacts.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/tests/http/test\_endpoint\_catalog.py b/tests/http/test\_endpoint\_catalog.py ; @@ \-35,11 \+35,13 @@ def test\_endpoint\_catalog\_has\_required\_paths():  
9. (DR-009) Observed: The audit-side endpoint catalog sha256 file is updated to a new digest line.  
   Why it matters: Prevents checksum mismatch failures when catalog integrity is verified.  
   Evidence pointer(s): PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@  
10. (DR-010) Observed: The docs-side endpoint catalog sha256 file is updated to a new digest line.  
    Why it matters: Keeps docs-facing checksum verification consistent with the catalog update and avoids “hash drift” between audited and docs-facing artifacts.  
    Evidence pointer(s): PR Artifacts → Diff → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256 b/docs/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@

Evidence Print (PASS PROOF; required)

A) Tokens satisfied (names-only; do not invent)

* None.

B) Evidence artifacts produced/updated

* Path: `artifacts/audit/ENDPOINTS_CATALOG.json`  
  Type: json  
  Key proof facts (verbatim):  
  * `"path":"/dev/writer/conjunction","method":"GET","route_id":"dev.writer.conjunction.v1"`  
    Evidence pointer: PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json b/artifacts/audit/ENDPOINTS\_CATALOG.json ; @@ \-1 \+1 @@  
* Path: `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`  
  Type: sha256/text  
  Key proof facts (verbatim):  
  * `774d7be3b0a667fc3cefae1e7d83a7b42d625ba3630901340c6645f6f07d3a0a`  
    Evidence pointer: PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@  
* Path: `docs/ENDPOINTS_CATALOG.json.sha256`  
  Type: sha256/text  
  Key proof facts (verbatim):  
  * `774d7be3b0a667fc3cefae1e7d83a7b42d625ba3630901340c6645f6f07d3a0a`  
    Evidence pointer: PR Artifacts → Diff → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256 b/docs/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@  
* Path: `tests/http/test_dev_conjunction_http.py`  
  Type: test  
  Key proof facts (verbatim):  
  * `resp = client.get("/dev/writer/conjunction?left=111&right=222", headers=headers)`  
  * `assert payload["writer"]["route_id"] == "dev.writer.conjunction.v1"`  
    Evidence pointer: PR Artifacts → Diff → diff \--git a/tests/http/test\_dev\_conjunction\_http.py b/tests/http/test\_dev\_conjunction\_http.py ; @@ \-1,61 \+1,92 @@  
* Path: `tests/http/test_endpoint_catalog.py`  
  Type: test  
  Key proof facts (verbatim):  
  * `assert "/dev/writer/conjunction" in writer_paths`  
  * `assert "dev.writer.conjunction.v1" in writer_route_ids`  
    Evidence pointer: PR Artifacts → Diff → diff \--git a/tests/http/test\_endpoint\_catalog.py b/tests/http/test\_endpoint\_catalog.py ; @@ \-35,11 \+35,13 @@ def test\_endpoint\_catalog\_has\_required\_paths():

C) Test/CI proof

* Job/test name (verbatim): `python -m pytest tests/http/test_endpoint_catalog.py tests/http/test_dev_conjunction_http.py`  
  Pass indicator (verbatim): `✅`  
  Where it appears in PR Artifacts: PR Artifacts → Actions Taken → ✅ python \-m pytest tests/http/test\_endpoint\_catalog.py tests/http/test\_dev\_conjunction\_http.py

CHG-001  
Change claim: Add a new dev-only writer endpoint `/dev/writer/conjunction` returning a writer envelope with idempotence behavior.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/adapter/http\_reader.py b/adapter/http\_reader.py ; @@ \-826,31 \+919,43 @@ bp \= Blueprint("http\_reader", **name**)  
Canon basis: CANON SILENCE

CHG-002  
Change claim: Update the endpoint catalog to include `/dev/writer/conjunction` and `dev.writer.conjunction.v1`.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json b/artifacts/audit/ENDPOINTS\_CATALOG.json ; @@ \-1 \+1 @@  
Canon basis: CANON SILENCE

CHG-003  
Change claim: Update tests and catalog sidecar sha256 digests to match the new catalog content and validate inclusion.  
Evidence pointer: PR Artifacts → Diff → diff \--git a/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 b/artifacts/audit/ENDPOINTS\_CATALOG.json.sha256 ; @@ \-1 \+1 @@  
Canon basis: CANON SILENCE

## 2.9 PR05 HDE-EPIC026

### Provenance (Original → Remediation) (REQUIRED; primary)

* Implementation Doc defines PR-05 as adding `hdctl showcompat` conjunction support with deterministic output and SAFE-rails gating. Source: Implementation Doc. Evidence pointer: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → supports conjunction-relevant invocation, enforces argument requirements, respects SAFE rails gating for missing local BodyGraphs, and emits deterministic canonical JSON for conjunction output.  
* Implementation Doc requires extending `hdctl showcompat` to support conjunction output integrated with conjunction contract \+ resolver/rails posture, without breaking default behavior. Source: Implementation Doc. Evidence pointer: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Extend `hdctl showcompat` to support conjunction output:  
* Implementation Doc requires strict argument enforcement (deterministic non-zero exit \+ stable stderr) when required args are missing. Source: Implementation Doc. Evidence pointer: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Enforce argument contract strictly:  
* Implementation Doc requires SAFE rails behavior: missing local BodyGraphs must require open rails to fetch; closed rails must deterministically refuse/network-block. Source: Implementation Doc. Evidence pointer: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* SAFE rails:  
* Implementation Doc states no new governed evidence artifacts are required for PR-05 (determinism proven via tests). Source: Implementation Doc. Evidence pointer: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* None new governed evidence artifacts required in this PR (CLI determinism is proven via tests; governed evidence indexing is handled in PR-07).  
* Implementation Doc explicitly lists acceptance tokens as none. Source: Implementation Doc. Evidence pointer: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → **Acceptance tokens (minimal list; explicit; do not invent)**  
* Original PR implemented a `--conjunction` path in `engine/cli/main.py` as part of the initial dev step. Source: Original PR. Evidence pointer: Original PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-69,50 \+70,58 @@ def \_build\_parser() \-\> argparse.ArgumentParser:  
* Original PR added/modified CLI canonical-bytes test coverage in `tests/cli/test_cli_canonical_bytes.py` as part of the initial dev step. Source: Original PR. Evidence pointer: Original PR → diff \--git a/tests/cli/test\_cli\_canonical\_bytes.py b/tests/cli/test\_cli\_canonical\_bytes.py → @@ \-1,41 \+1,44 @@  
* Original PR encountered a CI failure in closed-rails conjunction behavior: expected `PROVIDER_REFUSED` but got `CLI_UNEXPECTED:missing_bridge_url`. Source: Original PR. Evidence pointer: Original PR → CI Failure → Captured stderr: b'CLI\_UNEXPECTED:missing\_bridge\_url\\n'  
* Remedial PR focuses the candidate-to-merge change-set to three files (CLI \+ two test modules). Source: Remedial PR. Evidence pointer: Remedial PR → \#\#\# Files (3) → \- `engine/cli/main.py`  
* Remedial PR updates `engine/cli/main.py` to add conjunction support, strict arg/rails behavior, and deterministic canonical JSON emission for conjunction output. Source: Remedial PR. Evidence pointer: Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-662,50 \+757,71 @@ def showcompat(\_: argparse.Namespace) \-\> int:  
* Remedial PR adds/updates tests covering conjunction canonical stdout and closed-rails refusal, plus conjunction-source error surfacing. Source: Remedial PR. Evidence pointer: Remedial PR → diff \--git a/tests/cli/test\_cli\_canonical\_bytes.py b/tests/cli/test\_cli\_canonical\_bytes.py → @@ \-89,25 \+93,53 @@ def test\_reader\_dump\_and\_admin\_sidecars\_are\_canonical(tmp\_path: os.PathLike\[str\]  
* Remedial PR provides direct pass proof for CLI test suites relevant to PR-05 scope. Source: Remedial PR. Evidence pointer: Remedial PR → \#\# Test Results → 5 passed in 0.33s

### Review Summary

* Original PR made the initial implementation attempt for PR-05 by adding a conjunction path to `hdctl showcompat` and extending CLI determinism tests.  
* Original PR did not satisfy the SAFE-rails closed-rails acceptance posture in CI: closed-rails conjunction returned `CLI_UNEXPECTED:missing_bridge_url` instead of a deterministic refusal (`PROVIDER_REFUSED`).  
* Remedial PR narrows the merge candidate to a small, PR-05-scoped change-set (CLI \+ targeted tests) and directly addresses closed-rails conjunction refusal and deterministic output expectations.  
* The net effective change-set adds explicit conjunction input handling, deterministic JSON emission via the existing canonical emitter, and stronger error surfacing around DB/query/payload failures.  
* Tests/evidence posture in Remedial PR is materially stronger: it includes both subprocess-based stdout canonicalization for conjunction and an in-process closed-rails refusal test that asserts exact stdout/stderr behavior.  
* Combined outcome aligns with Implementation Doc PR-05 requirements (conjunction output \+ strict args \+ SAFE rails \+ deterministic output), with explicit proof-of-pass in Remedial PR’s test results.  
* Notable remaining risk is low: changes are localized to the CLI and tests, and the remedial tests explicitly cover the previously failing closed-rails scenario.

### RCA (REQUIRED only if RCA trigger is active)

#### A) Bug/Failure statement

Original PR’s CI run shows the closed-rails conjunction test failing because the command returned an unexpected bridge/config error instead of deterministic refusal:

* “FAILED tests/cli/test\_cli\_canonical\_bytes.py::test\_showcompat\_conjunction\_closed\_rails\_refuses\_when\_local\_missing”  
* “Captured stderr: b'CLI\_UNEXPECTED:missing\_bridge\_url\\n'”  
  Evidence pointer: Original PR → CI Failure → FAILED tests/cli/test\_cli\_canonical\_bytes.py::test\_showcompat\_conjunction\_closed\_rails\_refuses\_when\_local\_missing

#### B) Root cause(s)

1. Closed-rails conjunction execution surfaced `missing_bridge_url` as an unexpected CLI error rather than producing deterministic refusal (`PROVIDER_REFUSED`) when local BodyGraphs were missing and network access was disallowed.  
   Evidence pointer(s): Original PR → CI Failure → Captured stderr: b'CLI\_UNEXPECTED:missing\_bridge\_url\\n'  
2. DB access initialization/query failures during local BodyGraph lookup were not consistently mapped into deterministic CLI error codes in the conjunction path, contributing to “unexpected” error surfacing in CI.  
   Evidence pointer(s): Original PR → CI remediation → \* Broaden DB adapter error handling in `_fetch_db_bodygraph` so adapter instantiation failures (e.g., missing bridge/DB config) are mapped to `DB_QUERY_FAILED` CliError instead of bubbling as unexpected exceptions.

#### C) Fix across PRs

* Remedial PR makes the conjunction path explicitly emit a public conjunction payload under a stable top-level key and uses the canonical JSON emitter to produce deterministic bytes.  
  Evidence pointer: Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-662,50 \+757,71 @@ def showcompat(\_: argparse.Namespace) \-\> int:  
* Remedial PR hardens local BodyGraph lookup error mapping by catching adapter/query failures and raising deterministic CLI error codes (e.g., `DB_QUERY_FAILED`, `INVALID_BODYGRAPH_PAYLOAD`) instead of leaking unexpected exceptions.  
  Evidence pointer: Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-313,90 \+322,108 @@ def \_person\_and\_chart\_from\_payload(payload: Mapping\[str, Any\], \*, uid\_hint: str  
* Remedial PR adds a closed-rails regression test that stubs DB access to simulate “missing local”, disables network (`ALLOW_NETWORK=0`), and asserts exact deterministic refusal on stderr with empty stdout.  
  Evidence pointer: Remedial PR → diff \--git a/tests/cli/test\_cli\_canonical\_bytes.py b/tests/cli/test\_cli\_canonical\_bytes.py → @@ \-89,25 \+93,53 @@ def test\_reader\_dump\_and\_admin\_sidecars\_are\_canonical(tmp\_path: os.PathLike\[str\]

#### D) Fix verification

* Remedial PR shows `tests/cli/test_cli_canonical_bytes.py` passes as a whole (covers conjunction canonical stdout \+ closed-rails refusal regression):  
  Evidence pointer: Remedial PR → \#\# Test Results → 5 passed in 0.33s  
* Remedial PR shows `tests/cli/test_showcompat_sources.py` passes as a whole (covers conjunction source/error surfacing behavior):  
  Evidence pointer: Remedial PR → \#\# Test Results → 4 passed in 0.31s

### Findings (includes mandatory diff/code review)

1. **(Remedial PR / Diff hunk)** Adds conjunction contract integration into the CLI module via importing `conjunction_public_resolved`.  
   Why it matters: This is the explicit dependency needed to meet the Implementation Doc requirement to “integrate with the conjunction contract surface (PR-01)”.  
   Evidence pointer(s): Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-1,45 \+1,46 @@  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Extend `hdctl showcompat` to support conjunction output:  
2. **(Remedial PR / Diff hunk)** Extends the `showcompat` CLI parser with a `--conjunction` flag and updates help/usage to define accepted conjunction inputs.  
   Why it matters: This is the primary user-facing interface change required for PR-05 conjunction invocation support.  
   Evidence pointer(s): Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-69,50 \+70,58 @@ def \_build\_parser() \-\> argparse.ArgumentParser:  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → supports conjunction-relevant invocation, enforces argument requirements, respects SAFE rails gating for missing local BodyGraphs, and emits deterministic canonical JSON for conjunction output.  
3. **(Remedial PR / Diff hunk)** Hardens DB BodyGraph fetching to deterministically raise CLI errors on adapter/query failures and validates payload structure, and adds a helper to build conjunction parties from payloads.  
   Why it matters: Deterministic failures \+ stable stderr are required by the Implementation Doc for strict arg contract and SAFE rails posture; this also prevents unexpected exception leakage.  
   Evidence pointer(s): Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-313,90 \+322,108 @@ def \_person\_and\_chart\_from\_payload(payload: Mapping\[str, Any\], \*, uid\_hint: str  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Enforce argument contract strictly:  
4. **(Remedial PR / Diff hunk)** Introduces canonical pair normalization (`_canonical_pair`) and conjunction input routing helpers that enforce “either user-a/user-b OR pair payload input” and ensure stable A/B ordering for output emission.  
   Why it matters: This supports deterministic canonical JSON output (stable ordering) and reduces ambiguity in conjunction invocation inputs, aligning with strict contract requirements.  
   Evidence pointer(s): Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-603,50 \+630,118 @@ def aux\_preview(args: argparse.Namespace) \-\> int:  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Extend `hdctl showcompat` to support conjunction output:  
5. **(Remedial PR / Diff hunk)** Implements the `--conjunction` execution path in `showcompat`, including strict arg checks, SAFE rails resolver usage, deterministic refusal on closed rails when local inputs are missing, and canonical JSON emission to stdout.  
   Why it matters: This is the core behavior required by PR-05 (conjunction output \+ SAFE rails \+ deterministic canonical JSON).  
   Evidence pointer(s): Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-662,50 \+757,71 @@ def showcompat(\_: argparse.Namespace) \-\> int:  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* SAFE rails:  
6. **(Remedial PR / Diff hunk)** Updates CLI canonical-bytes tests: adds a conjunction-mode stdout canonicalization test using `_run_hdctl`, validating JSON structure and exact emitted bytes.  
   Why it matters: This is direct evidence for the “emit deterministic canonical JSON” requirement, and it exercises the actual `hdctl` subprocess pathway.  
   Evidence pointer(s): Remedial PR → diff \--git a/tests/cli/test\_cli\_canonical\_bytes.py b/tests/cli/test\_cli\_canonical\_bytes.py → @@ \-1,41 \+1,45 @@  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → supports conjunction-relevant invocation, enforces argument requirements, respects SAFE rails gating for missing local BodyGraphs, and emits deterministic canonical JSON for conjunction output.  
7. **(Remedial PR / Diff hunk)** Adds a closed-rails refusal regression test that stubs DB access to simulate missing local BodyGraphs, forces `ALLOW_NETWORK=0`, invokes `cli([...])`, and asserts empty stdout plus `PROVIDER_REFUSED` on stderr.  
   Why it matters: This directly closes the Original PR CI failure mode and proves deterministic refusal behavior required under SAFE rails when closed.  
   Evidence pointer(s): Remedial PR → diff \--git a/tests/cli/test\_cli\_canonical\_bytes.py b/tests/cli/test\_cli\_canonical\_bytes.py → @@ \-89,25 \+93,53 @@ def test\_reader\_dump\_and\_admin\_sidecars\_are\_canonical(tmp\_path: os.PathLike\[str\]  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* SAFE rails:  
8. **(Remedial PR / Diff hunk)** Extends `test_showcompat_sources.py` imports to support explicit adapter error simulation in showcompat source tests.  
   Why it matters: Enables deterministic validation of error surfacing (DB/query/payload) in conjunction mode, preventing regression back into “unexpected” error classes.  
   Evidence pointer(s): Remedial PR → diff \--git a/tests/cli/test\_showcompat\_sources.py b/tests/cli/test\_showcompat\_sources.py → @@ \-1,30 \+1,31 @@  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Enforce argument contract strictly:  
9. **(Remedial PR / Diff hunk)** Adds conjunction-specific tests ensuring DB-query failures and invalid payloads surface deterministic CLI errors (`DB_QUERY_FAILED`, `INVALID_BODYGRAPH_PAYLOAD`) instead of being silently treated as “missing local” or falling through to unexpected failures.  
   Why it matters: Strengthens safety and determinism guarantees for the conjunction path (stable error codes/stderr), consistent with Implementation Doc’s determinism requirements.  
   Evidence pointer(s): Remedial PR → diff \--git a/tests/cli/test\_showcompat\_sources.py b/tests/cli/test\_showcompat\_sources.py → @@ \-55,25 \+56,62 @@ def test\_showcompat\_vendor\_dry\_run(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture\[str\], tmp\_path: Path) \-\> None:  
   Implementation Doc alignment: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Enforce argument contract strictly:

### Requirement Satisfaction Crosswalk (Original step → Remediated satisfaction)

* **Requirement label:** Extend `hdctl showcompat` to support conjunction output  
  * Original PR status: Satisfied  
  * Evidence pointer(s) (Original PR): Original PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-69,50 \+70,58 @@ def \_build\_parser() \-\> argparse.ArgumentParser:  
  * Remedial PR change that addresses it: Stabilizes and finalizes conjunction execution path and output structure under `{"conjunction": ...}` with canonical emission.  
  * Evidence pointer(s) (Remedial PR): Remedial PR → diff \--git a/engine/cli/main.py b/engine/cli/main.py → @@ \-662,50 \+757,71 @@ def showcompat(\_: argparse.Namespace) \-\> int:  
  * Current status after remediation: Satisfied  
  * Evidence pointer(s) (Remedial PR): Remedial PR → diff \--git a/tests/cli/test\_cli\_canonical\_bytes.py b/tests/cli/test\_cli\_canonical\_bytes.py → @@ \-1,41 \+1,45 @@  
  * Notes: —  
* **Requirement label:** Enforce argument contract strictly (deterministic non-zero exit, stable stderr when required args missing)  
  * Original PR status: Unclear  
  * Evidence pointer(s) (Original PR): Original PR → PR Artifacts Bundle → (no direct pass/fail evidence for “no args must fail deterministically” beyond prompt-level intent)  
  * Remedial PR change that addresses it: Adds explicit conjunction-mode validation and deterministic error surfacing tests for failure classes (`DB_QUERY_FAILED`, `INVALID_BODYGRAPH_PAYLOAD`).  
  * Evidence pointer(s) (Remedial PR): Remedial PR → diff \--git a/tests/cli/test\_showcompat\_sources.py b/tests/cli/test\_showcompat\_sources.py → @@ \-55,25 \+56,62 @@ def test\_showcompat\_vendor\_dry\_run(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture\[str\], tmp\_path: Path) \-\> None:  
  * Current status after remediation: Satisfied  
  * Evidence pointer(s) (Remedial PR): Remedial PR → \#\# Test Results → 4 passed in 0.31s  
  * Notes (optional; 1 line): Search method: searched Original PR for "cannot run without args" (case: insensitive); scope: Original PR → PR-05 sections \+ diffs; tool: grep; result: 0 hits.  
* **Requirement label:** SAFE rails (closed rails must deterministically refuse when local BodyGraphs missing; open rails required to fetch when missing locally)  
  * Original PR status: Not satisfied  
  * Evidence pointer(s) (Original PR): Original PR → CI Failure → Captured stderr: b'CLI\_UNEXPECTED:missing\_bridge\_url\\n'  
  * Remedial PR change that addresses it: Adds explicit closed-rails refusal regression test with DB stub \+ `ALLOW_NETWORK=0`, asserting exact stdout/stderr and `PROVIDER_REFUSED`.  
  * Evidence pointer(s) (Remedial PR): Remedial PR → diff \--git a/tests/cli/test\_cli\_canonical\_bytes.py b/tests/cli/test\_cli\_canonical\_bytes.py → @@ \-89,25 \+93,53 @@ def test\_reader\_dump\_and\_admin\_sidecars\_are\_canonical(tmp\_path: os.PathLike\[str\]  
  * Current status after remediation: Satisfied  
  * Evidence pointer(s) (Remedial PR): Remedial PR → \#\# Test Results → 5 passed in 0.33s  
  * Notes: —  
* **Requirement label:** Basic QA task (run deterministic CLI test)  
  * Original PR status: Satisfied  
  * Evidence pointer(s) (Original PR): Original PR → \#\#\# Summary → ✅ python \-m pytest tests/cli/test\_cli\_canonical\_bytes.py::test\_showcompat\_stdout\_is\_canonical  
  * Remedial PR change that addresses it: Re-runs and passes the relevant CLI test suites after remediation changes.  
  * Evidence pointer(s) (Remedial PR): Remedial PR → \#\# Test Results → 5 passed in 0.33s  
  * Current status after remediation: Satisfied  
  * Evidence pointer(s) (Remedial PR): Remedial PR → \#\# Test Results → 5 passed in 0.33s  
  * Notes: —

### Evidence Print (PASS PROOF; required; whole PR outcome)

A) Acceptance coverage evidence (Implementation Doc)

* Conjunction support required: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Extend `hdctl showcompat` to support conjunction output:  
* Strict/deterministic arg contract required: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* Enforce argument contract strictly:  
* SAFE rails closed-rails refusal required: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* SAFE rails:  
* Acceptance tokens explicitly none: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → **Acceptance tokens (minimal list; explicit; do not invent)**

B) Evidence/verification posture now satisfied (Original step closure)

* Original failure proof: closed-rails conjunction emitted unexpected `missing_bridge_url` in CI. Evidence pointer: Original PR → CI Failure → Captured stderr: b'CLI\_UNEXPECTED:missing\_bridge\_url\\n'  
* Closure proof: remedial tests covering conjunction canonical stdout and closed-rails refusal now pass. Evidence pointer: Remedial PR → \#\# Test Results → 5 passed in 0.33s

C) Token and gate evidence (names-only; do not invent)

* Acceptance tokens: None (per Implementation Doc). Evidence pointer: Implementation Doc → PR-05 — `hdctl showcompat` supports `--conjunction` mode → \* None  
* Search method: searched Remedial PR for "token" (case: insensitive); scope: Remedial PR → full bundle; tool: grep; result: 0 hits.

D) Test/CI proof

* `python -m pytest tests/cli/test_cli_canonical_bytes.py -q` → `5 passed in 0.33s`  
  Evidence pointer: Remedial PR → \#\# Test Results → 5 passed in 0.33s  
* `python -m pytest tests/cli/test_showcompat_sources.py -q` → `4 passed in 0.31s`  
  Evidence pointer: Remedial PR → \#\# Test Results → 4 passed in 0.31s

E) Artifact/evidence outputs

* Updated CLI implementation: `engine/cli/main.py` (adds conjunction support, deterministic error surfacing, canonical JSON emission).  
  Evidence pointer: Remedial PR → \#\#\# Files (3) → \- `engine/cli/main.py`  
* Updated test coverage: `tests/cli/test_cli_canonical_bytes.py`, `tests/cli/test_showcompat_sources.py`.  
  Evidence pointer: Remedial PR → \#\#\# Files (3) → \- `tests/cli/test_cli_canonical_bytes.py`

## 2.10 Epic Plans must include a Business Case section (Glow product framing)

Timestamp: 021426

Details:

Rule (normative)

1. **Business Case section is required in every Epic Plan.**  
   Every Epic Plan MUST include a clearly labeled **Business Case** section.  
2. **Business Case MUST be written in overall Glow product terms.**  
   The Business Case MUST describe the practical goals and reasons for the work in terms of the Glow product, not only internal mechanics or implementation details.  
3. **Minimum required contents (all MUST be present).**  
   The Business Case section MUST include, in plain language:  
   * **Product goal:** what user-facing capability or product milestone this epic enables.  
   * **Why this work exists:** the concrete problem, gap, or constraint it resolves for the product.  
   * **Who benefits:** which user or operator workflow improves (end user, internal operator, QA, growth, safety, cost control).  
   * **What changes if it ships:** the tangible before/after outcome in product terms.  
   * **Why now:** why this epic is needed at this point in the product’s evolution (dependency unblocking, risk reduction, readiness gating).  
   * **If not done:** the product-level risk or consequence of not doing the work (blocked capability, inability to validate, operational risk, cost exposure).  
   * **Non-goals:** what this epic explicitly does not attempt, stated in product terms.  
4. **Separation from technical scope.**  
   The Business Case MUST NOT be replaced by a restatement of implementation tasks, code changes, evidence artifacts, or canon citations. Those belong elsewhere in the plan.  
5. **Review posture (blocking condition).**  
   If an Epic Plan lacks a Business Case section, or if the Business Case is purely technical and does not explain the product reason for the work, the plan MUST be returned for revision.

Non-goals

* This rule does not require financial ROI calculations.  
* This rule does not require marketing copy. It requires practical product reasoning that prevents drift.

Drain targets (required)

* **PF27 — Canon Plan Templates:** add a required Business Case section with the minimum required contents listed above.  
* **PF06 — Epic Process Guide:** add a reviewer gate stating that missing or non-product Business Case is a revise condition for Epic Plans.

## 2.11 PR06 HDE-EPIC026

### Review Summary

* PR06 is a docs-only alignment pass: it updates CLI documentation for conjunction-mode `showcompat` usage and updates runbook docs for dev-only conjunction endpoints/gating (no runtime behavior changes in this PR).  
* The changes appear aligned with the Approved Plan’s PR-06 scope (documentation \+ endpoint catalog drift prevention) and stay within the “docs/catalog-only focus” constraint stated in PR Artifacts.  
* Diff review found no scope drift: only `docs/CLI_commands.md` and `docs/RUN.md` are modified in the patch.  
* Evidence posture is lightweight but plausible for a docs PR: PR Artifacts explicitly record running the endpoint-catalog test and CLI help inspection.  
* Main residual risk: because this PR documents CLI flags/syntax, correctness depends on the docs matching actual `--help` / parser behavior (PR Artifacts state the help was checked, but the artifacts do not include the help output excerpt).

### Diff Review (REQUIRED; primary technical review)

1. **DR-001**  
   * **Change summary:** Documented `showcompat` conjunction-mode invocation patterns and clarified read-only posture \+ required inputs \+ failure cases for `--conjunction`.  
   * **Risk assessment:** Low  
   * **Why it matters:** Prevents CLI syntax drift by explicitly documenting the conjunction-mode command surface and constraints that are already enforced by the CLI.  
   * **Evidence pointer:** PR Artifacts → docs/CLI\_commands.md → diff \--git a/docs/CLI\_commands.md b/docs/CLI\_commands.md ; @@ \-1,38 \+1,44 @@  
   * **Approved Plan linkage:** Approved Plan → \* showcompat conjunction usage and SAFE rails gating behavior.  
2. **DR-002**  
   * **Change summary:** Added a concise “dev-only conjunction endpoints” section in `docs/RUN.md` listing the three dev endpoints and their environment gating.  
   * **Risk assessment:** Low  
   * **Why it matters:** Reinforces dev-only posture and prevents accidental production exposure by documenting the gating mechanism and “do not enable in production” constraint.  
   * **Evidence pointer:** PR Artifacts → docs/RUN.md → diff \--git a/docs/RUN.md b/docs/RUN.md ; @@ \-17,50 \+17,54 @@  
   * **Approved Plan linkage:** Approved Plan → \* dev-only conjunction endpoints (`/dev/sampler/conjunction`, `/dev/reader/conjunction`, `/dev/writer/conjunction`) with dev-only gating notes.

### Findings

1. **(DR-001) CLI conjunction docs now include explicit invocation patterns and behavioral rails for `--conjunction`.**  
   * **What you observed:** The usage list adds a “Conjunction compatibility check” block with three invocation forms, and adds an explicit behavioral note that `showcompat --conjunction` is read-only, requires both parties, and enumerates failure/guard cases.  
   * **Why it matters:** This directly addresses the Approved Plan’s requirement to document conjunction CLI usage and to be explicit about required inputs (“cannot run without args”) and safe/read-only posture.  
   * **Evidence pointer(s):**  
     * PR Artifacts → docs/CLI\_commands.md → diff \--git a/docs/CLI\_commands.md b/docs/CLI\_commands.md ; @@ \-1,38 \+1,44 @@  
     * PR Artifacts → docs/CLI\_commands.md → \+ \- `hdctl showcompat --conjunction --user-a <user_a> --user-b <user_b> [--source db|vendor|auto]`  
2. **(DR-002) RUN docs now explicitly label the conjunction endpoints as dev-only and document the gate as `APP_ENV` dev|test|local.**  
   * **What you observed:** A new section states “Dev-only conjunction endpoints (do not enable in production)” and describes the gating mechanism and the forbidden behavior when not in the allowed env set.  
   * **Why it matters:** Matches the Approved Plan requirement to document dev-only endpoints and their real gating mechanism to prevent accidental prod exposure.  
   * **Evidence pointer(s):**  
     * PR Artifacts → docs/RUN.md → diff \--git a/docs/RUN.md b/docs/RUN.md ; @@ \-17,50 \+17,54 @@  
     * PR Artifacts → docs/RUN.md → \+APP\_ENV must be one of dev|test|local for these endpoints; otherwise requests are forbidden (forbidden writer-style envelope).  
3. **Scope discipline is preserved (docs-only change-set).**  
   * **What you observed:** PR Artifacts list exactly two changed files, both documentation paths, with small additive diffs.  
   * **Why it matters:** Keeps PR06 within the Approved Plan’s PR-06 “Documentation \+ endpoint catalog alignment” scope and avoids introducing runtime drift.  
   * **Evidence pointer:** PR Artifacts → \#\#\# Files (2) → docs/CLI\_commands.md

### Evidence Print (PASS PROOF; required)

#### A) Tokens satisfied (names-only; do not invent)

* None

#### B) Evidence artifacts produced/updated

* **Path:** docs/CLI\_commands.md  
  * **Type:** markdown  
  * **Key proof facts (verbatim):**  
    * “+ \- `hdctl showcompat --conjunction --pair-file <pair.json>`”  
    * “+`showcompat --conjunction` is a read-only compatibility check: it emits canonical JSON to stdout and does not write state. Required conjunction inputs must be present for both parties, either through `--user-a/--user-b` or through payload input (`--pair-file`, `--a-file` \+ `--b-file`, or stdin with `left`/`right`).”  
  * **Evidence pointer:** PR Artifacts → docs/CLI\_commands.md → diff \--git a/docs/CLI\_commands.md b/docs/CLI\_commands.md ; @@ \-1,38 \+1,44 @@  
* **Path:** docs/RUN.md  
  * **Type:** markdown  
  * **Key proof facts (verbatim):**  
    * “+\#\# Dev-only conjunction endpoints (do not enable in production)”  
    * “+APP\_ENV must be one of dev|test|local for these endpoints; otherwise requests are forbidden (forbidden writer-style envelope).”  
  * **Evidence pointer:** PR Artifacts → docs/RUN.md → diff \--git a/docs/RUN.md b/docs/RUN.md ; @@ \-17,50 \+17,54 @@

#### C) Test/CI proof

* **Job/test name (verbatim):** python \-m pytest tests/http/test\_endpoint\_catalog.py  
  * **Pass indicator (verbatim):** “✅ python \-m pytest tests/http/test\_endpoint\_catalog.py”  
  * **Where it appears in PR Artifacts:** PR Artifacts → \#\#\# Testing → ✅ python \-m pytest tests/http/test\_endpoint\_catalog.py  
* **Job/test name (verbatim):** python scripts/hdctl.py showcompat \--help  
  * **Pass indicator (verbatim):** “✅ python scripts/hdctl.py showcompat \--help”  
  * **Where it appears in PR Artifacts:** PR Artifacts → \#\#\# Testing → ✅ python scripts/hdctl.py showcompat \--help

#### Doc Deltas (PF-Canon only; REQUIRED; with Canon Check Gate)

* **CHG-001**  
  * **Change claim:** Documented `hdctl showcompat --conjunction` invocation forms and clarified conjunction-mode behavior notes (read-only posture, required inputs, and failure cases).  
  * **Evidence pointer:** PR Artifacts → docs/CLI\_commands.md → diff \--git a/docs/CLI\_commands.md b/docs/CLI\_commands.md ; @@ \-1,38 \+1,44 @@  
  * **Canon basis:** CANON SILENCE  
* **CHG-002**  
  * **Change claim:** Documented dev-only conjunction endpoints and environment gating posture in `docs/RUN.md`.  
  * **Evidence pointer:** PR Artifacts → docs/RUN.md → diff \--git a/docs/RUN.md b/docs/RUN.md ; @@ \-17,50 \+17,54 @@  
  * **Canon basis:** CANON SILENCE

## 2.12 PR07 HDE-EPIC026

### Review Summary

* PR Artifacts expand the governed Canonical JSON gate target surface to include conjunction-related CLI artifacts (pair/pair\_ba/showcompat/out/out\_ba and an abba\_sidecar) and refresh the corresponding gate logs/records.  
* PR Artifacts add/refresh path-proof anchors for the affected artifacts so evidence references include size and sha256 metadata.  
* PR Artifacts update the evidence index (both the machine index and the docs snapshot/sha) to reflect the new/updated governed artifacts.  
* PR Artifacts also refresh the topology orientation demo governed output to reflect the updated evidence graph size (artifact count change), aligning with the drift failure described in PR Artifacts logs.  
* Alignment: Changes are consistent with Approved Plan’s PR-07 scope (“Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs”) and appear limited to governed evidence outputs \+ the gate runner configuration (no product interface changes).  
* Evidence posture: PR Artifacts include updated canonical gate outputs (including `"status":"pass"` records) plus the updated evidence index snapshot artifacts; however, some “ran command” attestations are checkmarked rather than full raw logs.  
* RCA: Included (covers the tool-output drift failure signal and how this PR resolves it via governed fixture refresh).

### Diff Review (REQUIRED; primary technical review)

1. **DR-001**  
   * Change summary: Refresh `pair.json` path-proof into structured fields (path/size\_bytes/sha256/mtime\_utc/produced\_at\_utc).  
   * Risk assessment: Low  
   * Why it matters: Path-proof anchors are relied upon by the evidence index to bind governed artifacts deterministically.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/audit/cli/pair.json.path\_proof.txt b/artifacts/audit/cli/pair.json.path\_proof.txt → @@ \-1 \+1,5 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
2. **DR-002**  
   * Change summary: Refresh `pair_ba.json` path-proof into structured fields.  
   * Risk assessment: Low  
   * Why it matters: Ensures the `pair_ba` artifact can be validated and referenced consistently by evidence tooling.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/audit/cli/pair\_ba.json.path\_proof.txt b/artifacts/audit/cli/pair\_ba.json.path\_proof.txt → @@ \-1 \+1,5 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
3. **DR-003**  
   * Change summary: Refresh `showcompat_ab.json` path-proof into structured fields.  
   * Risk assessment: Low  
   * Why it matters: Canonical gate \+ evidence index depend on stable proof anchors for showcompat outputs.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/audit/cli/showcompat\_ab.json.path\_proof.txt b/artifacts/audit/cli/showcompat\_ab.json.path\_proof.txt → @@ \-1 \+1,5 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
4. **DR-004**  
   * Change summary: Refresh `showcompat_ba.json` path-proof into structured fields.  
   * Risk assessment: Low  
   * Why it matters: Prevents proof drift for showcompat outputs that are part of governed gate coverage.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/audit/cli/showcompat\_ba.json.path\_proof.txt b/artifacts/audit/cli/showcompat\_ba.json.path\_proof.txt → @@ \-1 \+1,5 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
5. **DR-005**  
   * Change summary: Add new path-proof artifact for `artifacts/cli/abba_sidecar.json`.  
   * Risk assessment: Low  
   * Why it matters: New/covered artifacts must have proof anchors to be governed via the evidence index.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/cli/abba\_sidecar.json.path\_proof.txt b/artifacts/cli/abba\_sidecar.json.path\_proof.txt → @@ \-0,0 \+1,5 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
6. **DR-006**  
   * Change summary: Add new path-proof artifact for `artifacts/cli/out.json`.  
   * Risk assessment: Low  
   * Why it matters: Canonical JSON gate coverage expansion requires governed anchors for the referenced CLI output file.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/cli/out.json.path\_proof.txt b/artifacts/cli/out.json.path\_proof.txt → @@ \-0,0 \+1,5 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
7. **DR-007**  
   * Change summary: Add new path-proof artifact for `artifacts/cli/out_ba.json`.  
   * Risk assessment: Low  
   * Why it matters: Ensures the BA-direction output has a governed proof anchor consistent with AB output.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/cli/out\_ba.json.path\_proof.txt b/artifacts/cli/out\_ba.json.path\_proof.txt → @@ \-0,0 \+1,5 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
8. **DR-008**  
   * Change summary: Refresh evidence index rows for updated governed artifacts (hash/size/mtime/proof anchors).  
   * Risk assessment: Medium  
   * Why it matters: The evidence index is the binding layer for what artifacts are considered current and verifiable.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-379,17 \+379,17 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
9. **DR-009**  
   * Change summary: Extend the evidence index to include conjunction-related CLI artifact keys and proof anchors.  
   * Risk assessment: Medium  
   * Why it matters: Without index entries, new gate-covered artifacts cannot be validated/consumed by downstream governance checks.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-727,38 \+727,42 @@  
   * Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
10. **DR-010**  
* Change summary: Update the path-proof record for `artifacts/evidence_index.jsonl` (including mirror\_body\_sha256 field).  
* Risk assessment: Low  
* Why it matters: The index itself is a governed artifact; its proof anchor must track the exact content hash.  
* Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl.path\_proof.txt b/artifacts/evidence\_index.jsonl.path\_proof.txt → @@ \-2,4 \+2,5 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
11. **DR-011**  
* Change summary: Refresh `canonical_json.gate.json` (gate summary) to reflect updated checked target set.  
* Risk assessment: Medium  
* Why it matters: This file is an auditable declaration of what the gate checked; it must match the current intended coverage.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/canonical\_json.gate.json b/audit/gates/canonical\_json/canonical\_json.gate.json → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
12. **DR-012**  
* Change summary: Update path-proof for the canonical JSON gate summary JSON.  
* Risk assessment: Low  
* Why it matters: Gate summary artifacts must be traceable by sha to support governance/auditability.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/canonical\_json.gate.json.path\_proof.txt b/audit/gates/canonical\_json/canonical\_json.gate.json.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
13. **DR-013**  
* Change summary: Update `json_canon_compare.log` to reflect current compare run and covered artifacts.  
* Risk assessment: Medium  
* Why it matters: Compare logs are key audit trails for what canonical comparisons were performed and with what results.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/json\_canon\_compare.log b/audit/gates/canonical\_json/json\_canon\_compare.log → @@ \-1,12 \+1,15 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
14. **DR-014**  
* Change summary: Update `json_canonical_check.log` to reflect current check coverage/status.  
* Risk assessment: Medium  
* Why it matters: This is the human-readable gate output that indicates whether the canonical checks passed.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/json\_canonical\_check.log b/audit/gates/canonical\_json/json\_canonical\_check.log → @@ \-1,12 \+1,15 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
15. **DR-015**  
* Change summary: Update path-proof for `json_canonical_check.log`.  
* Risk assessment: Low  
* Why it matters: Ensures the log’s content is bound by sha for governance traceability.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/json\_canonical\_check.log.path\_proof.txt b/audit/gates/canonical\_json/json\_canonical\_check.log.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
16. **DR-016**  
* Change summary: Refresh NDJSON check log for JSON gate canonical outputs (records for each checked artifact key).  
* Risk assessment: Medium  
* Why it matters: Structured per-artifact `"status":"pass"` records are the strongest auditable signal that the gate passed for each target.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
17. **DR-017**  
* Change summary: Update path-proof for `json_gate_check_log.ndjson`.  
* Risk assessment: Low  
* Why it matters: Keeps proof anchors aligned with the updated structured gate output.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson.path\_proof.txt b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
18. **DR-018**  
* Change summary: Update path-proof for the JSON gate compare NDJSON log.  
* Risk assessment: Low  
* Why it matters: Compare logs are part of the governed gate artifact family and must remain sha-bound.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson.path\_proof.txt b/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
19. **DR-019**  
* Change summary: Update `json_gate_structured_record.json` to reflect current gate run metadata and target set.  
* Risk assessment: Medium  
* Why it matters: The structured record is commonly used as the canonical “single JSON” summary for downstream automation.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json b/audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
20. **DR-020**  
* Change summary: Update path-proof for `json_gate_structured_record.json`.  
* Risk assessment: Low  
* Why it matters: Preserves sha-bound traceability for the structured summary record.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json.path\_proof.txt b/audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
21. **DR-021**  
* Change summary: Refresh the path-proof for `docs/ENDPOINTS_CATALOG.json`.  
* Risk assessment: Low  
* Why it matters: Endpoint catalogs are governed outputs; proof anchors ensure catalog content is traceable and immutable-by-hash.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
22. **DR-022**  
* Change summary: Refresh the path-proof for `docs/ENDPOINTS_CATALOG.json.sha256`.  
* Risk assessment: Low  
* Why it matters: The `.sha256` companion is a governed checksum; its proof anchor is required for audit integrity.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
23. **DR-023**  
* Change summary: Update the docs evidence index snapshot JSON (`docs/evidence/INDEX.json`) to match the refreshed governed artifact set.  
* Risk assessment: Medium  
* Why it matters: This is the documented “snapshot” used by reviewers/auditors; it must match the machine index.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
24. **DR-024**  
* Change summary: Update path-proof for `docs/evidence/INDEX.json`.  
* Risk assessment: Low  
* Why it matters: Ensures the docs snapshot is sha-bound like all governed artifacts.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.json.path\_proof.txt b/docs/evidence/INDEX.json.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
25. **DR-025**  
* Change summary: Update `docs/evidence/INDEX.sha256` to reflect the new `INDEX.json` content.  
* Risk assessment: Medium  
* Why it matters: Reviewers and automation rely on `INDEX.sha256` as the single-line integrity binding for the evidence snapshot.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256 → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
26. **DR-026**  
* Change summary: Update path-proof for `docs/evidence/INDEX.sha256`.  
* Risk assessment: Low  
* Why it matters: Ensures the checksum file itself is sha-bound and traceable.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.sha256.path\_proof.txt b/docs/evidence/INDEX.sha256.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
27. **DR-027**  
* Change summary: Extend `run_canonical_json_gate.py` target definitions to include conjunction-related CLI artifacts.  
* Risk assessment: Medium  
* Why it matters: The runner defines which files are canon-compared; incorrect targets here would silently reduce gate coverage or break governance.  
* Evidence pointer: PR Artifacts → diff \--git a/tools/evidence/run\_canonical\_json\_gate.py b/tools/evidence/run\_canonical\_json\_gate.py → @@ \-14,50 \+14,57 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
28. **DR-028**  
* Change summary: Update evidence index entries for topology orientation demo artifact and proof anchor.  
* Risk assessment: Medium  
* Why it matters: Topology demo outputs participate in drift detection; the evidence index must reference the current canonical output.  
* Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-250,10 \+250,10 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
29. **DR-029**  
* Change summary: Refresh JSON gate compare log NDJSON to match current canonical comparison results for the updated target set.  
* Risk assessment: Medium  
* Why it matters: Compare NDJSON is the auditable proof that each target’s content matches its canon (or not).  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson → @@ \-1 \+1 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
30. **DR-030**  
* Change summary: Refresh topology orientation demo governed output content (including artifact count).  
* Risk assessment: Medium  
* Why it matters: Drift checks depend on this output; if it’s stale it will fail CI and/or mask graph changes.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/topology/orientation\_demo.txt b/audit/gates/topology/orientation\_demo.txt → @@ \-83,7 \+83,11 @@ demo: anchor\_and\_orient  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**  
31. **DR-031**  
* Change summary: Update path-proof for topology orientation demo output.  
* Risk assessment: Low  
* Why it matters: Ensures the refreshed demo output is sha-bound for governance and drift validation.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/topology/orientation\_demo.txt.path\_proof.txt b/audit/gates/topology/orientation\_demo.txt.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Approved Plan linkage: Approved Plan → \#\#\# **PR-07 — Governed evidence posture: index/mirror \+ canonical JSON gate artifacts for conjunction outputs**

### RCA

#### A) Bug/Failure statement

PR Artifacts show a tool-output drift failure in logs for the orientation demo check:

* “Run python tools/evidence/orientation\_demo.py \--check” followed by “ORIENTATION\_DRIFT” and “exit code 1”.  
  Evidence pointer: PR Artifacts → \#\# Logs → ORIENTATION\_DRIFT

#### B) Root cause(s)

1. Governed topology demo fixture drifted relative to the current evidence graph size.  
* Root cause statement: The stored demo output no longer matched the current anchored/oriented artifact set, triggering drift detection.  
* Evidence pointer(s): PR Artifacts → diff \--git a/audit/gates/topology/orientation\_demo.txt b/audit/gates/topology/orientation\_demo.txt → @@ \-83,7 \+83,11 @@ demo: anchor\_and\_orient  
* PF references only when needed: N/A

#### C) Fix in this PR

* Updated governed demo output:  
  * `audit/gates/topology/orientation_demo.txt` (content/total\_artifacts refreshed).  
  * `audit/gates/topology/orientation_demo.txt.path_proof.txt` (proof anchor refreshed).  
* Updated evidence binding for the refreshed demo output:  
  * `artifacts/evidence_index.jsonl` (topology orientation demo entry refreshed).  
    Evidence pointers:  
* PR Artifacts → diff \--git a/audit/gates/topology/orientation\_demo.txt b/audit/gates/topology/orientation\_demo.txt → @@ \-83,7 \+83,11 @@ demo: anchor\_and\_orient  
* PR Artifacts → diff \--git a/audit/gates/topology/orientation\_demo.txt.path\_proof.txt b/audit/gates/topology/orientation\_demo.txt.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-250,10 \+250,10 @@

#### D) Fix verification

* PR Artifacts describe re-running the check after remediation: “✅ `python tools/evidence/orientation_demo.py --check`”.  
  * Evidence pointer: PR Artifacts → \#\# Actions Taken → ✅ `python tools/evidence/orientation_demo.py --check`  
* Residual risk/edge case not covered (ONLY if evidenced): N/A

### Findings

1. (DR-001) Path-proof for `pair.json` was moved to structured sha/size/mtime/provenance fields.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/audit/cli/pair.json.path\_proof.txt b/artifacts/audit/cli/pair.json.path\_proof.txt → @@ \-1 \+1,5 @@  
   * Why it matters: Makes `pair.json` independently auditable and bindable by sha for the evidence index.  
2. (DR-002) Path-proof for `pair_ba.json` was similarly refreshed to the structured schema.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/audit/cli/pair\_ba.json.path\_proof.txt b/artifacts/audit/cli/pair\_ba.json.path\_proof.txt → @@ \-1 \+1,5 @@  
   * Why it matters: Ensures BA-direction artifacts are governed with the same rigor as AB.  
3. (DR-003) `showcompat_ab.json` now has a structured path-proof suitable for sha-based governance.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/audit/cli/showcompat\_ab.json.path\_proof.txt b/artifacts/audit/cli/showcompat\_ab.json.path\_proof.txt → @@ \-1 \+1,5 @@  
   * Why it matters: Prevents silent drift in showcompat outputs used by gate comparisons.  
4. (DR-004) `showcompat_ba.json` now has a structured path-proof suitable for sha-based governance.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/audit/cli/showcompat\_ba.json.path\_proof.txt b/artifacts/audit/cli/showcompat\_ba.json.path\_proof.txt → @@ \-1 \+1,5 @@  
   * Why it matters: Keeps AB/BA showcompat variants equally governable.  
5. (DR-005) A new governed proof anchor was introduced for `artifacts/cli/abba_sidecar.json`.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/cli/abba\_sidecar.json.path\_proof.txt b/artifacts/cli/abba\_sidecar.json.path\_proof.txt → @@ \-0,0 \+1,5 @@  
   * Why it matters: Newly introduced/checked artifacts must be anchored to avoid “ungoverned” acceptance surface.  
6. (DR-006) A new governed proof anchor was introduced for `artifacts/cli/out.json`.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/cli/out.json.path\_proof.txt b/artifacts/cli/out.json.path\_proof.txt → @@ \-0,0 \+1,5 @@  
   * Why it matters: Canonical JSON gate now references this output; it must be sha-bound.  
7. (DR-007) A new governed proof anchor was introduced for `artifacts/cli/out_ba.json`.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/cli/out\_ba.json.path\_proof.txt b/artifacts/cli/out\_ba.json.path\_proof.txt → @@ \-0,0 \+1,5 @@  
   * Why it matters: Prevents asymmetric governance between AB and BA outputs.  
8. (DR-008) Evidence index rows were updated to reflect refreshed hashes/sizes for governed artifacts.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-379,17 \+379,17 @@  
   * Why it matters: Ensures downstream checks evaluate the current artifact set rather than stale bindings.  
9. (DR-009) Evidence index was extended to include conjunction-related artifact keys and their proof anchors.  
   * Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-727,38 \+727,42 @@  
   * Why it matters: Without index inclusion, the new conjunction artifacts cannot be treated as governed/validated.  
10. (DR-010) The evidence index’s own proof record was updated (including mirror\_body\_sha256).  
* Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl.path\_proof.txt b/artifacts/evidence\_index.jsonl.path\_proof.txt → @@ \-2,4 \+2,5 @@  
* Why it matters: Confirms integrity of the binding layer itself.  
11. (DR-011) Canonical JSON gate summary JSON was refreshed to reflect the updated checked\_targets set.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/canonical\_json.gate.json b/audit/gates/canonical\_json/canonical\_json.gate.json → @@ \-1 \+1 @@  
* Why it matters: Prevents misalignment between intended and recorded gate coverage.  
12. (DR-012) Canonical JSON gate summary proof anchor was updated accordingly.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/canonical\_json.gate.json.path\_proof.txt b/audit/gates/canonical\_json/canonical\_json.gate.json.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Maintains sha-bound auditability for the gate’s summary artifact.  
13. (DR-013) The canonical compare log was updated to align with the current gate run.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/json\_canon\_compare.log b/audit/gates/canonical\_json/json\_canon\_compare.log → @@ \-1,12 \+1,15 @@  
* Why it matters: Compare logs are typically used to debug mismatches; stale logs are misleading.  
14. (DR-014) The canonical check log was updated to align with the current gate run.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/json\_canonical\_check.log b/audit/gates/canonical\_json/json\_canonical\_check.log → @@ \-1,12 \+1,15 @@  
* Why it matters: This is a primary “human readable” pass/fail artifact for reviewers.  
15. (DR-015) Proof anchor for canonical check log was updated.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/canonical\_json/json\_canonical\_check.log.path\_proof.txt b/audit/gates/canonical\_json/json\_canonical\_check.log.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Ensures the log can be validated by sha rather than by convention.  
16. (DR-016) JSON gate structured NDJSON check log was refreshed; it contains per-target status records.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson → @@ \-1 \+1 @@  
* Why it matters: Structured `"status":"pass"` records are the strongest audit proof for each target.  
17. (DR-017) Proof anchor for the JSON gate check NDJSON was updated.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson.path\_proof.txt b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Ensures check-log integrity can be independently verified.  
18. (DR-018) Proof anchor for the JSON gate compare NDJSON was updated.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson.path\_proof.txt b/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Compare output is often used to confirm canon match vs mismatch across runs.  
19. (DR-019) Structured JSON gate record was updated to match the refreshed target set and run metadata.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json b/audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json → @@ \-1 \+1 @@  
* Why it matters: Downstream automation often consumes the single structured record rather than logs.  
20. (DR-020) Proof anchor for the structured JSON gate record was updated.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json.path\_proof.txt b/audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Maintains sha-bound validation for the structured record.  
21. (DR-021) `docs/ENDPOINTS_CATALOG.json` proof anchor was refreshed.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Endpoint catalog artifacts are governance-facing and must remain hash verifiable.  
22. (DR-022) `docs/ENDPOINTS_CATALOG.json.sha256` proof anchor was refreshed.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt b/docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: The checksum artifact itself is governed and must be proof-anchored.  
23. (DR-023) `docs/evidence/INDEX.json` was refreshed to reflect the current governed set.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json → @@ \-1 \+1 @@  
* Why it matters: Prevents reviewer-facing snapshot drift vs machine evidence index.  
24. (DR-024) Proof anchor for `docs/evidence/INDEX.json` was refreshed.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.json.path\_proof.txt b/docs/evidence/INDEX.json.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Keeps snapshot verifiable by hash.  
25. (DR-025) `docs/evidence/INDEX.sha256` was refreshed to match `INDEX.json`.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256 → @@ \-1 \+1 @@  
* Why it matters: This is the primary integrity line for the snapshot in many workflows.  
26. (DR-026) Proof anchor for `docs/evidence/INDEX.sha256` was refreshed.  
* Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.sha256.path\_proof.txt b/docs/evidence/INDEX.sha256.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Makes the checksum itself hash verifiable.  
27. (DR-027) Canonical JSON gate runner was updated to include conjunction-related targets.  
* Evidence pointer: PR Artifacts → diff \--git a/tools/evidence/run\_canonical\_json\_gate.py b/tools/evidence/run\_canonical\_json\_gate.py → @@ \-14,50 \+14,57 @@  
* Why it matters: Target list drift here would create silent coverage gaps in the canonical gate.  
28. (DR-028) Evidence index was updated to reflect the refreshed topology demo artifact bindings.  
* Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-250,10 \+250,10 @@  
* Why it matters: The topology demo is explicitly drift-checked; its binding must match the refreshed content.  
29. (DR-029) JSON gate compare NDJSON was refreshed to reflect updated target comparisons.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson → @@ \-1 \+1 @@  
* Why it matters: Confirms canonical matches for each target in a machine-readable way.  
30. (DR-030) Topology orientation demo output was refreshed (notably artifact count increased).  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/topology/orientation\_demo.txt b/audit/gates/topology/orientation\_demo.txt → @@ \-83,7 \+83,11 @@ demo: anchor\_and\_orient  
* Why it matters: Drift failures block CI and signal that governance fixtures lag behind repo reality.  
31. (DR-031) Proof anchor for the refreshed topology orientation demo output was updated.  
* Evidence pointer: PR Artifacts → diff \--git a/audit/gates/topology/orientation\_demo.txt.path\_proof.txt b/audit/gates/topology/orientation\_demo.txt.path\_proof.txt → @@ \-2,3 \+2,4 @@  
* Why it matters: Ensures the updated fixture is bound by sha for audit/replay.

### Evidence Print (PASS PROOF; required)

#### A) Tokens satisfied (names-only; do not invent)

1. **EVIDENCE\_INDEX\_UPDATED\_OK**  
* Evidence pointer(s): PR Artifacts → diff \--git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json → @@ \-1 \+1 @@  
2. **EVIDENCE\_INDEX\_MIRROR\_OK**  
* Evidence pointer(s): PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-727,38 \+727,42 @@  
3. **EVIDENCE\_PATHS\_VALIDATED\_OK**  
* Evidence pointer(s):  
  * PR Artifacts → \#\# Actions Taken → ✅ LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/update\_evidence\_index.py \--check  
  * PR Artifacts → \#\# Actions Taken → ✅ python ci/checks/check\_mirror\_schema.sh  
4. **CANONICAL\_JSON\_GATE\_UPDATED\_OK**  
* Evidence pointer(s): PR Artifacts → diff \--git a/tools/evidence/run\_canonical\_json\_gate.py b/tools/evidence/run\_canonical\_json\_gate.py → @@ \-14,50 \+14,57 @@  
5. **CANONICAL\_JSON\_GATE\_PASSED\_OK**  
* Evidence pointer(s): PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson → @@ \-1 \+1 @@

#### B) Evidence artifacts produced/updated

* Path: `docs/evidence/INDEX.json`  
  * Type: json  
  * Key proof facts (verbatim):  
    * `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json`  
* Path: `docs/evidence/INDEX.sha256`  
  * Type: sha256 text  
  * Key proof facts (verbatim):  
    * `39772ea326d381d035b21fd6b68810ca86371d6c6e1c3a3ca8a9b732b993c3a7 docs/evidence/INDEX.json`  
    * Evidence pointer: PR Artifacts → diff \--git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256 → @@ \-1 \+1 @@  
* Path: `artifacts/evidence_index.jsonl`  
  * Type: jsonl  
  * Key proof facts (verbatim):  
    * `"artifact_key":"cli.conjunction.output_ab"`  
    * `"artifact_key":"cli.conjunction.pair_ab"`  
    * Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-727,38 \+727,42 @@  
* Path: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
  * Type: ndjson  
  * Key proof facts (verbatim):  
    * `"status":"pass"`  
    * `"artifact_key":"cli.conjunction.output_ab"`  
    * Evidence pointer: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson → @@ \-1 \+1 @@  
* Path: `audit/gates/topology/orientation_demo.txt`  
  * Type: text  
  * Key proof facts (verbatim):  
    * `total_artifacts: 279`  
    * `total_artifacts: 286`  
    * Evidence pointer: PR Artifacts → diff \--git a/audit/gates/topology/orientation\_demo.txt b/audit/gates/topology/orientation\_demo.txt → @@ \-83,7 \+83,11 @@ demo: anchor\_and\_orient

#### C) Test/CI proof

* Job/test name (verbatim): `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/update_evidence_index.py --check`  
  * Pass indicator (verbatim): `✅ LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/evidence/update_evidence_index.py --check`  
  * Where it appears in PR Artifacts: PR Artifacts → \#\# Actions Taken → ✅ LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/update\_evidence\_index.py \--check  
* Job/test name (verbatim): `python ci/checks/check_mirror_schema.sh`  
  * Pass indicator (verbatim): `✅ python ci/checks/check_mirror_schema.sh`  
  * Where it appears in PR Artifacts: PR Artifacts → \#\# Actions Taken → ✅ python ci/checks/check\_mirror\_schema.sh  
* Job/test name (verbatim): JSON gate check log records  
  * Pass indicator (verbatim): `"status":"pass"`  
  * Where it appears in PR Artifacts: PR Artifacts → diff \--git a/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson b/audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson → @@ \-1 \+1 @@

### Doc Deltas (PF-Canon only; REQUIRED; with Canon Check Gate)

#### Doc Delta Detection Workflow

* **CHG-001**: Evidence index and governed outputs continue to include both `audit/gates/json_gate/canonical/*` and legacy `audit/gates/canonical_json/*` canonical JSON gate artifact families.  
  * Evidence pointer: PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-727,38 \+727,42 @@  
  * Canon basis: **CANON MISMATCH**  
* **CHG-002**: Canonical JSON gate target list expanded to include conjunction-related CLI artifacts (pair/pair\_ba/showcompat/out/out\_ba and abba\_sidecar proof coverage).  
  * Evidence pointer: PR Artifacts → diff \--git a/tools/evidence/run\_canonical\_json\_gate.py b/tools/evidence/run\_canonical\_json\_gate.py → @@ \-14,50 \+14,57 @@  
  * Canon basis: **CANON SILENCE** (no PF coverage found that enumerates the target key set)

#### Doc Delta Entries

* **CHG: CHG-001**  
  * **Doc:** PF12 — PF12-Canon-HDE-Schemas-and-Artifacts  
  * **Section:** Canonical JSON gate artifacts (single family; no dual-home)  
  * **Canon basis:** CANON MISMATCH  
  * **Delta:** Clarify PF12 guidance to reflect current repository reality where legacy `audit/gates/canonical_json/*` artifacts are still being produced/tracked alongside `audit/gates/json_gate/canonical/*`, and specify whether legacy artifacts are (a) non-binding and slated for deprecation or (b) still governed until a migration completes.  
  * **Why:** PR Artifacts demonstrate ongoing updates and evidence-index tracking for both canonical and legacy canonical JSON gate artifact families, while PF12 currently states acceptance artifacts must not dual-home across these families.  
  * **Evidence pointer:**  
    * PR Artifacts → diff \--git a/artifacts/evidence\_index.jsonl b/artifacts/evidence\_index.jsonl → @@ \-727,38 \+727,42 @@  
    * PR Artifacts → diff \--git a/audit/gates/canonical\_json/canonical\_json.gate.json b/audit/gates/canonical\_json/canonical\_json.gate.json → @@ \-1 \+1 @@  
  * **Canon proof excerpt:**  
    * PF12 — PF12-Canon-HDE-Schemas-and-Artifacts, Canonical JSON gate artifacts (single family; no dual-home)  
      * `### Canonical JSON gate artifacts (single family; no dual-home)`  
      * `Acceptance artifacts MUST NOT dual-home bindings across audit/gates/json_gate/canonical/ and any legacy families (including audit/gates/canonical_json/ and audit/gates/canonical/).`

## 2.13 PR08 HDE-EPIC026

### Provenance (Original → Remediation 1 → Remediation 2\) (REQUIRED; primary)

* PR-08 is defined as Deliverable D-008: “Epic close pack generator \+ artifacts” and enumerates the required close-pack outputs and helper script. Source: Implementation Doc. Evidence pointer: Implementation Doc → PR-08 (HDE-EPIC026 PR08) — Close Pack Generator → Deliverable D-008: Epic close pack generator \+ artifacts.  
* Attempt 0 positioned itself as producing the close pack artifacts and generator (manifest, close report, doc deltas, QA manifests, and generator script). Source: Original PR. Evidence pointer: Original PR → Files (9) → audit/EPIC-026\_MANIFEST.json.  
* Attempt 0 shipped an evidence manifest file as a new artifact. Source: Original PR. Evidence pointer: Original PR → audit/EPIC-026\_MANIFEST.json → diff \--git a/audit/EPIC-026\_MANIFEST.json b/audit/EPIC-026\_MANIFEST.json || @@ \-0,0 \+1 @@  
* Attempt 0 shipped a close report file as a new artifact. Source: Original PR. Evidence pointer: Original PR → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,49 @@  
* Attempt 0 was flagged for diff integrity issues: the bundle listed files as changed, but corresponding diff hunks were absent, and there were duplicate diff blocks to remove. Source: Remediation 1\. Evidence pointer: Remediation 1 → \#\# Remediation Needed → \- Diff integrity issue: PR Artifacts list includes audit/qa/hde-epic026/qa\_step\_logs\_manifest.json but the patch does not contain a diff hunk for that file.  
* Remediation 1 explicitly targeted those attempt-0 gaps (fix diff integrity; remove duplicate patch blocks; regenerate outputs; align artifacts to the required markdown ledgers and manifests). Source: Remediation 1\. Evidence pointer: Remediation 1 → \#\# Actions Taken → \- Regenerated all close-pack outputs with deterministic ordering and current time-stamps; removed the redundant `audit/doc_deltas/EPIC-026_doc_delta_ledger.json` JSON in favor of the required markdown ledgers.  
* Remediation 1 introduced an actual diff hunk for the QA step logs manifest JSON (resolving the missing-hunk defect from attempt 0). Source: Remediation 1\. Evidence pointer: Remediation 1 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json || @@ \-0,0 \+1 @@  
* Remediation 1 produced the intended markdown doc-delta ledger artifacts (audit docdeltas \+ QA meta doc deltas). Source: Remediation 1\. Evidence pointer: Remediation 1 → audit/docdeltas/hde-epic026\_doc\_deltas.md → diff \--git a/audit/docdeltas/hde-epic026\_doc\_deltas.md b/audit/docdeltas/hde-epic026\_doc\_deltas.md || @@ \-0,0 \+1,12 @@  
* Remediation 1 updated/standardized the generator to emit the close pack outputs and path proofs for core governed artifacts. Source: Remediation 1\. Evidence pointer: Remediation 1 → tools/qa/generate\_epic026\_close\_pack.py → diff \--git a/tools/qa/generate\_epic026\_close\_pack.py b/tools/qa/generate\_epic026\_close\_pack.py || @@ \-1,169 \+1,180 @@  
* Remediation 1 was still deemed non-acceptable because TI-002 closure mapping (PF09 pointers or ADR) was not yet satisfied. Source: Remediation 2\. Evidence pointer: Remediation 2 → \#\# Original Prompt → \- Still does not satisfy Implementation Doc requirement to address TI-002 closure via PF09 pointers (HDE-FERM001.3, HDE-COAG007.3) or ADR.  
* Remediation 2 explicitly added TI-002 / PF09 mapping content generation and an ADR-status line into the close pack artifacts. Source: Remediation 2\. Evidence pointer: Remediation 2 → \#\# Actions Taken → \- Added TI-002/PF09 mapping generation to the close report and doc delta ledgers, including an ADR-status line to avoid unresolved closure.  
* Remediation 2 updated the close report to include the TI-002 mapping and ADR status line. Source: Remediation 2\. Evidence pointer: Remediation 2 → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,48 @@  
* Remediation 2 updated the doc delta ledger artifacts to include the TI-002 mapping and ADR status line (while keeping “Doc Deltas: None…”). Source: Remediation 2\. Evidence pointer: Remediation 2 → audit/docdeltas/hde-epic026\_doc\_deltas.md → diff \--git a/audit/docdeltas/hde-epic026\_doc\_deltas.md b/audit/docdeltas/hde-epic026\_doc\_deltas.md || @@ \-0,0 \+1,26 @@  
* Remediation 2 recorded that the generator was run under SAFE\_MODE/ALLOW\_NETWORK posture and that compileall and a manifest/path existence assertion were run. Source: Remediation 2\. Evidence pointer: Remediation 2 → \#\# Testing → ✅ SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/qa/generate\_epic026\_close\_pack.py.  
* Remediation 2 states CI passed (per the PR artifact’s own CI note). Source: Remediation 2\. Evidence pointer: Remediation 2 → \#\# CI → ✅ CI passed (as reported by Codex internal checks).

### Review Summary

* Attempt 0 produced an initial close pack (manifest \+ path proof, close report \+ path proof, doc deltas, step log manifest path proof, and generator), but had integrity gaps (listed files without corresponding diff hunks; duplicate diff block removal requirement). Evidence pointer: Remediation 1 → \#\# Remediation Needed → \- Diff integrity issue: PR Artifacts list includes audit/qa/hde-epic026/qa\_step\_logs\_manifest.json but the patch does not contain a diff hunk for that file.  
* Remediation 1 corrected the structural issues (regenerated artifacts; fixed missing-hunk problems; standardized the generator and outputs), but was still judged insufficient for TI-002 closure mapping. Evidence pointer: Remediation 2 → \#\# Original Prompt → \- Still does not satisfy Implementation Doc requirement to address TI-002 closure via PF09 pointers (HDE-FERM001.3, HDE-COAG007.3) or ADR.  
* Remediation 2 adds explicit TI-002/PF09 mapping (plus ADR-status line) into the close report and doc delta ledgers, and updates the generator accordingly. Evidence pointer: Remediation 2 → \#\# Actions Taken → \- Added TI-002/PF09 mapping generation to the close report and doc delta ledgers, including an ADR-status line to avoid unresolved closure.  
* The final (attempt 2\) patch set is narrowly scoped to PR-08’s “close pack generator \+ artifacts” deliverable (audit artifacts \+ a tools/qa script), with no product/runtime surface changes evidenced. Evidence pointer: Remediation 2 → \#\# Diff → diff \--git a/tools/qa/generate\_epic026\_close\_pack.py b/tools/qa/generate\_epic026\_close\_pack.py  
* Validation posture in attempt 2 is documented as executed (SAFE\_MODE/ALLOW\_NETWORK generator run, compileall, and a manifest/path existence assertion), and CI is marked as passed in the PR artifact. Evidence pointer: Remediation 2 → \#\# Testing → ✅ python \-m compileall tools/qa/generate\_epic026\_close\_pack.py.  
* Notable residual risk: the close pack manifest enumerates many key outputs across the epic; this is intended for a “close pack,” but it implies ongoing sensitivity to path drift in governed artifacts (mitigated by the included manifest/path assertion test). Evidence pointer: Remediation 2 → audit/EPIC-026\_MANIFEST.json → diff \--git a/audit/EPIC-026\_MANIFEST.json b/audit/EPIC-026\_MANIFEST.json || @@ \-0,0 \+1 @@  
* No new CLI flags are introduced by the generator (it is invoked without arguments, and no arg parsing is evidenced), supporting command-line drift protection concerns. Evidence pointer: Remediation 2 → tools/qa/generate\_epic026\_close\_pack.py → diff \--git a/tools/qa/generate\_epic026\_close\_pack.py b/tools/qa/generate\_epic026\_close\_pack.py || @@ \-0,0 \+1,221 @@

### RCA (REQUIRED)

#### RCA-001

A) Failure statement (1–3 sentences; quote key lines verbatim from evidence)  
“Diff integrity issue: PR Artifacts list includes audit/qa/hde-epic026/qa\_step\_logs\_manifest.json but the patch does not contain a diff hunk for that file.”  
“Duplication: audit/EPIC-026\_MANIFEST.json.path\_proof.txt patch appears twice; remove the duplicate diff block.”  
Evidence pointer: Remediation 1 → \#\# Remediation Needed → \- Diff integrity issue: PR Artifacts list includes audit/qa/hde-epic026/qa\_step\_logs\_manifest.json but the patch does not contain a diff hunk for that file.

B) Where it occurred: Attempt 0 / Attempt 1 / Attempt 2 (may be multiple)  
Attempt 0 (identified during remediation planning in attempt 1).

C) Root cause(s) (numbered; 1–N)

1. Root cause statement: The attempt-0 PR bundle assembly was inconsistent (file list vs diff hunks) and included duplicate patch content, indicating a patch-generation / curation error rather than a code-level runtime defect.  
   Evidence pointer(s): Remediation 1 → \#\# Remediation Needed → Duplication: audit/EPIC-026\_MANIFEST.json.path\_proof.txt patch appears twice; remove the duplicate diff block.

D) Fix progression across attempts (bullets)

* Remediation 1 regenerated the close-pack outputs and fixed the missing-hunk situation by adding an explicit diff hunk for the step logs manifest JSON.  
  Evidence pointer: Remediation 1 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json || @@ \-0,0 \+1 @@  
* Remediation 2 retains the corrected structure and proceeds with content-level closure improvements (TI-002 mapping), without reintroducing integrity issues.  
  Evidence pointer: Remediation 2 → \#\# Actions Taken → \- Added TI-002/PF09 mapping generation to the close report and doc delta ledgers, including an ADR-status line to avoid unresolved closure.

E) Fix verification (bullets)

* Remediation 2 includes an actual diff hunk for `audit/qa/hde-epic026/qa_step_logs_manifest.json` (i.e., the earlier “listed but no hunk” defect is no longer present in attempt 2).  
  Evidence pointer: Remediation 2 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json || @@ \-0,0 \+1 @@  
* Remediation 2’s Testing section includes a manifest/path existence assertion to catch missing referenced artifacts.  
  Evidence pointer: Remediation 2 → \#\# Testing → ✅ python \- \<\<'PY'\\nimport json, pathlib\\nm \= json.load(open("audit/EPIC-026\_MANIFEST.json"))\\nreq \= \[\\n "audit/EPIC-026\_MANIFEST.json",\\n "audit/EPIC-026\_MANIFEST.json.path\_proof.txt",\\n "audit/EPIC-026\_close\_report.md",\\n "audit/EPIC-026\_close\_report.md.path\_proof.txt",\\n "audit/docdeltas/hde-epic026\_doc\_deltas.md",\\n "audit/qa/hde-epic026/00\_meta/doc\_deltas.md",\\n "audit/qa/hde-epic026/qa\_step\_logs\_manifest.json",\\n "audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt",\\n\]\\nfor p in req:\\n assert pathlib.Path(p).exists(), p\\nfor v in m\["key\_outputs"\].values():\\n if isinstance(v, list):\\n for p in v:\\n assert pathlib.Path(p).exists(), p\\n else:\\n assert pathlib.Path(v).exists(), v\\nprint("ok")\\nPY.

#### RCA-002

A) Failure statement (1–3 sentences; quote key lines verbatim from evidence)  
“Still does not satisfy Implementation Doc requirement to address TI-002 closure via PF09 pointers (HDE-FERM001.3, HDE-COAG007.3) or ADR.”  
Evidence pointer: Remediation 2 → \#\# Original Prompt → \- Still does not satisfy Implementation Doc requirement to address TI-002 closure via PF09 pointers (HDE-FERM001.3, HDE-COAG007.3) or ADR.

B) Where it occurred: Attempt 0 / Attempt 1 / Attempt 2 (may be multiple)  
Attempt 1 (and earlier attempts) lacked explicit TI-002 closure mapping; resolved in attempt 2\.

C) Root cause(s) (numbered; 1–N)

1. Root cause statement: The close pack artifacts and generator did not include an explicit TI-002 closure mapping to PF09 pointers (or an ADR record), leaving closure provenance incomplete relative to the Implementation Doc’s TI-002 closure requirements.  
   Evidence pointer(s): Implementation Doc → PR-08 (HDE-EPIC026 PR08) — Close Pack Generator → TI-002 closure:.

D) Fix progression across attempts (bullets)

* Remediation 1 focused on structural/diff integrity and regenerating artifacts, but did not add the TI-002/PF09 mapping content required for closure.  
  Evidence pointer: Remediation 2 → \#\# Original Prompt → \- Still does not satisfy Implementation Doc requirement to address TI-002 closure via PF09 pointers (HDE-FERM001.3, HDE-COAG007.3) or ADR.  
* Remediation 2 added TI-002/PF09 mapping generation into the close report and doc delta ledgers, including an ADR-status line.  
  Evidence pointer: Remediation 2 → \#\# Actions Taken → \- Added TI-002/PF09 mapping generation to the close report and doc delta ledgers, including an ADR-status line to avoid unresolved closure.

E) Fix verification (bullets)

* Close report now contains the explicit TI-002 closure mapping (PF09 pointers \+ TI-002 pointers \+ artifact mapping \+ ADR status line).  
  Evidence pointer: Remediation 2 → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,48 @@  
* Doc delta ledger artifacts now contain the same TI-002 closure mapping and ADR status line.  
  Evidence pointer: Remediation 2 → audit/docdeltas/hde-epic026\_doc\_deltas.md → diff \--git a/audit/docdeltas/hde-epic026\_doc\_deltas.md b/audit/docdeltas/hde-epic026\_doc\_deltas.md || @@ \-0,0 \+1,26 @@  
* Generator script includes the embedded TI-002/PF09 mapping content for the artifacts it generates (supporting regeneration without manual edits).  
  Evidence pointer: Remediation 2 → tools/qa/generate\_epic026\_close\_pack.py → diff \--git a/tools/qa/generate\_epic026\_close\_pack.py b/tools/qa/generate\_epic026\_close\_pack.py || @@ \-0,0 \+1,221 @@

### Findings (includes diff review)

1. Observed (Remediation 2): Adds the EPIC close-pack manifest `audit/EPIC-026_MANIFEST.json` enumerating key outputs and including `pf23_sha256` for the PF23 anchor.  
   Why it matters: This is a primary D-008 artifact (“evidence manifest”) that ties the close pack to governed outputs; incorrect paths here could silently break closure integrity.  
   Evidence pointer(s): Remediation 2 → audit/EPIC-026\_MANIFEST.json → diff \--git a/audit/EPIC-026\_MANIFEST.json b/audit/EPIC-026\_MANIFEST.json || @@ \-0,0 \+1 @@  
2. Observed (Remediation 2): Adds `audit/EPIC-026_MANIFEST.json.path_proof.txt` (governed path proof) for the manifest.  
   Why it matters: Path proofs provide tamper-evident linkage (sha256 \+ size \+ timestamp) for a governed artifact, supporting auditability of the close pack.  
   Evidence pointer(s): Remediation 2 → audit/EPIC-026\_MANIFEST.json.path\_proof.txt → diff \--git a/audit/EPIC-026\_MANIFEST.json.path\_proof.txt b/audit/EPIC-026\_MANIFEST.json.path\_proof.txt || @@ \-0,0 \+1 @@  
3. Observed (Remediation 2): Adds `audit/EPIC-026_close_report.md` including (a) PF23 audit note commands, (b) Doc Delta Summary, and (c) explicit TI-002 closure mapping to PF09 pointers with ADR status line.  
   Why it matters: The close report is the human-readable closure artifact, and the TI-002 mapping is explicitly called out in the Implementation Doc as required closure provenance.  
   Evidence pointer(s): Remediation 2 → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,48 @@  
4. Observed (Remediation 2): Adds `audit/EPIC-026_close_report.md.path_proof.txt` (path proof) for the close report.  
   Why it matters: Ensures the close report itself is governed with integrity metadata, matching the Implementation Doc’s evidence output list for PR-08.  
   Evidence pointer(s): Remediation 2 → audit/EPIC-026\_close\_report.md.path\_proof.txt → diff \--git a/audit/EPIC-026\_close\_report.md.path\_proof.txt b/audit/EPIC-026\_close\_report.md.path\_proof.txt || @@ \-0,0 \+1,11 @@  
5. Observed (Remediation 2): Adds the doc delta ledger artifact `audit/docdeltas/hde-epic026_doc_deltas.md` with “Doc Deltas: None…” plus TI-002/PF09 coverage mapping and ADR status line.  
   Why it matters: The Implementation Doc requires doc delta ledger artifacts to exist post-PR; even when “None,” the ledger records closure mappings and prevents ambiguity about doc drift.  
   Evidence pointer(s): Remediation 2 → audit/docdeltas/hde-epic026\_doc\_deltas.md → diff \--git a/audit/docdeltas/hde-epic026\_doc\_deltas.md b/audit/docdeltas/hde-epic026\_doc\_deltas.md || @@ \-0,0 \+1,26 @@  
6. Observed (Remediation 2): Adds the QA-meta doc delta ledger artifact `audit/qa/hde-epic026/00_meta/doc_deltas.md` mirroring the doc delta summary and TI-002 mapping.  
   Why it matters: This provides an operationally convenient, QA-local ledger consistent with the Implementation Doc’s “doc delta ledger artifacts” list.  
   Evidence pointer(s): Remediation 2 → audit/qa/hde-epic026/00\_meta/doc\_deltas.md → diff \--git a/audit/qa/hde-epic026/00\_meta/doc\_deltas.md b/audit/qa/hde-epic026/00\_meta/doc\_deltas.md || @@ \-0,0 \+1,26 @@  
7. Observed (Remediation 2): Adds `audit/qa/hde-epic026/qa_step_logs_manifest.json` with a minimal schema and `checks: []`.  
   Why it matters: The Implementation Doc requires a QA step log manifest artifact post-PR; leaving `checks` empty is acceptable if no step logs are being claimed, but it shifts reliance to CI/testing evidence elsewhere.  
   Evidence pointer(s): Remediation 2 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json || @@ \-0,0 \+1 @@  
8. Observed (Remediation 2): Adds `audit/qa/hde-epic026/qa_step_logs_manifest.json.path_proof.txt` as a governed path proof for the QA step logs manifest.  
   Why it matters: Provides integrity metadata for the QA manifest, consistent with the PR-08 evidence outputs list (step log manifest path proof is explicitly enumerated).  
   Evidence pointer(s): Remediation 2 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt || @@ \-0,0 \+1 @@  
9. Observed (Remediation 2): Adds `tools/qa/generate_epic026_close_pack.py` as a generator producing the close pack artifacts, including TI-002/PF09 mapping injection, and writing path proofs for governed artifacts.  
   Why it matters: This is the PR-08 core deliverable (“close pack generator”); it is also where any accidental CLI flag drift would surface—no argument parsing is evidenced, supporting drift protection.  
   Evidence pointer(s): Remediation 2 → tools/qa/generate\_epic026\_close\_pack.py → diff \--git a/tools/qa/generate\_epic026\_close\_pack.py b/tools/qa/generate\_epic026\_close\_pack.py || @@ \-0,0 \+1,221 @@  
10. Observed (Remediation 2): Testing section documents running the generator under SAFE\_MODE/ALLOW\_NETWORK posture and compileall, plus a manifest/path existence assertion.  
    Why it matters: Confirms (at least by claim) that the generated artifacts exist and that the manifest’s referenced paths exist, reducing risk of stale/missing artifact references in the close pack.  
    Evidence pointer(s): Remediation 2 → \#\# Testing → ✅ python \- \<\<'PY'\\nimport json, pathlib\\nm \= json.load(open("audit/EPIC-026\_MANIFEST.json"))\\nreq \= \[\\n "audit/EPIC-026\_MANIFEST.json",\\n "audit/EPIC-026\_MANIFEST.json.path\_proof.txt",\\n "audit/EPIC-026\_close\_report.md",\\n "audit/EPIC-026\_close\_report.md.path\_proof.txt",\\n "audit/docdeltas/hde-epic026\_doc\_deltas.md",\\n "audit/qa/hde-epic026/00\_meta/doc\_deltas.md",\\n "audit/qa/hde-epic026/qa\_step\_logs\_manifest.json",\\n "audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt",\\n\]\\nfor p in req:\\n assert pathlib.Path(p).exists(), p\\nfor v in m\["key\_outputs"\].values():\\n if isinstance(v, list):\\n for p in v:\\n assert pathlib.Path(p).exists(), p\\n else:\\n assert pathlib.Path(v).exists(), v\\nprint("ok")\\nPY.

### Requirement Satisfaction Crosswalk (Attempt 0 → Attempt 1 → Attempt 2\)

**Requirement: Deliverable D-008 (Close pack generator \+ artifacts)**

* Attempt 0 status: Not satisfied  
  Evidence pointer(s) in Original PR: Original PR → Files (9) → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.  
  Search method: searched Original PR for "diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b" (case: sensitive); scope: full file PR08 HDE-EPIC026.md; tool: grep; result: 0 hits.  
* Attempt 1 status: Not satisfied  
  Evidence pointer(s) in Remediation 1: Remediation 1 → \#\# Diff → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json  
  Notes: TI-002 closure mapping still not satisfied after attempt 1 (see TI-002 requirement row below).  
* Attempt 2 status: Satisfied  
  Evidence pointer(s) in Remediation 2: Remediation 2 → \#\# Diff → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md

**Requirement: EPIC026 evidence manifest and close report (plus required path proofs)**

* Attempt 0 status: Satisfied  
  Evidence pointer(s) in Original PR: Original PR → audit/EPIC-026\_MANIFEST.json.path\_proof.txt → diff \--git a/audit/EPIC-026\_MANIFEST.json.path\_proof.txt b/audit/EPIC-026\_MANIFEST.json.path\_proof.txt || @@ \-0,0 \+1 @@  
* Attempt 1 status: Satisfied  
  Evidence pointer(s) in Remediation 1: Remediation 1 → audit/EPIC-026\_close\_report.md.path\_proof.txt → diff \--git a/audit/EPIC-026\_close\_report.md.path\_proof.txt b/audit/EPIC-026\_close\_report.md.path\_proof.txt || @@ \-0,0 \+1,11 @@  
* Attempt 2 status: Satisfied  
  Evidence pointer(s) in Remediation 2: Remediation 2 → audit/EPIC-026\_MANIFEST.json → diff \--git a/audit/EPIC-026\_MANIFEST.json b/audit/EPIC-026\_MANIFEST.json || @@ \-0,0 \+1 @@

**Requirement: EPIC026 QA step log manifest (plus required path proof)**

* Attempt 0 status: Not satisfied  
  Evidence pointer(s) in Original PR: Original PR → Files (9) → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.  
  Search method: searched Original PR for "diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b" (case: sensitive); scope: full file PR08 HDE-EPIC026.md; tool: grep; result: 0 hits.  
* Attempt 1 status: Satisfied  
  Evidence pointer(s) in Remediation 1: Remediation 1 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json || @@ \-0,0 \+1 @@  
* Attempt 2 status: Satisfied  
  Evidence pointer(s) in Remediation 2: Remediation 2 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt || @@ \-0,0 \+1 @@

**Requirement: EPIC026 doc delta ledger artifacts (audit \+ QA meta)**

* Attempt 0 status: Not satisfied  
  Evidence pointer(s) in Original PR: Original PR → Files (9) → audit/qa/hde-epic026/00\_meta/doc\_deltas.md.  
  Search method: searched Original PR for "diff \--git a/audit/qa/hde-epic026/00\_meta/doc\_deltas.md b" (case: sensitive); scope: full file PR08 HDE-EPIC026.md; tool: grep; result: 0 hits.  
* Attempt 1 status: Satisfied  
  Evidence pointer(s) in Remediation 1: Remediation 1 → audit/qa/hde-epic026/00\_meta/doc\_deltas.md → diff \--git a/audit/qa/hde-epic026/00\_meta/doc\_deltas.md b/audit/qa/hde-epic026/00\_meta/doc\_deltas.md || @@ \-0,0 \+1,12 @@  
* Attempt 2 status: Satisfied  
  Evidence pointer(s) in Remediation 2: Remediation 2 → audit/qa/hde-epic026/00\_meta/doc\_deltas.md → diff \--git a/audit/qa/hde-epic026/00\_meta/doc\_deltas.md b/audit/qa/hde-epic026/00\_meta/doc\_deltas.md || @@ \-0,0 \+1,26 @@

**Requirement: Helper script tools/qa/generate\_epic026\_close\_pack.py**

* Attempt 0 status: Satisfied  
  Evidence pointer(s) in Original PR: Original PR → tools/qa/generate\_epic026\_close\_pack.py → diff \--git a/tools/qa/generate\_epic026\_close\_pack.py b/tools/qa/generate\_epic026\_close\_pack.py || @@ \-0,0 \+1,215 @@  
* Attempt 1 status: Satisfied  
  Evidence pointer(s) in Remediation 1: Remediation 1 → tools/qa/generate\_epic026\_close\_pack.py → diff \--git a/tools/qa/generate\_epic026\_close\_pack.py b/tools/qa/generate\_epic026\_close\_pack.py || @@ \-1,169 \+1,180 @@  
* Attempt 2 status: Satisfied  
  Evidence pointer(s) in Remediation 2: Remediation 2 → tools/qa/generate\_epic026\_close\_pack.py → diff \--git a/tools/qa/generate\_epic026\_close\_pack.py b/tools/qa/generate\_epic026\_close\_pack.py || @@ \-0,0 \+1,221 @@

**Requirement: TI-002 closure (PF09 pointers mapping or ADR)**

* Attempt 0 status: Not satisfied  
  Evidence pointer(s) in Original PR: Original PR → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,49 @@  
  Search method: searched Original PR for "TI-002" (case: sensitive); scope: full file PR08 HDE-EPIC026.md; tool: grep; result: 0 hits.  
* Attempt 1 status: Not satisfied  
  Evidence pointer(s) in Remediation 1: Remediation 1 → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,52 @@  
  Search method: searched Remediation 1 for "TI-002" (case: sensitive); scope: full file r1 PR08 HDE-EPIC026.md; tool: grep; result: 0 hits.  
* Attempt 2 status: Satisfied  
  Evidence pointer(s) in Remediation 2: Remediation 2 → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,48 @@  
  Notes: Includes “PF09 pointers: HDE-FERM001.3, HDE-COAG007.3”, “TI-002 pointers: …”, and “ADR status line: ADR-TI002-EPIC026-001”.

### Evidence Print (PASS PROOF; whole PR lifecycle)

A) Acceptance coverage evidence (Implementation Doc)

* Requirement: “EPIC026 evidence manifest and close report”  
  Evidence pointer(s) in Remediation 2 proving satisfaction: Remediation 2 → audit/EPIC-026\_MANIFEST.json → diff \--git a/audit/EPIC-026\_MANIFEST.json b/audit/EPIC-026\_MANIFEST.json || @@ \-0,0 \+1 @@  
  Key proof facts (from Remediation 2 artifacts):  
  * `pf23_sha256:"f8fbbb063b70cabdd12893df6f42d62a8659903c1f5f5d638157fd6c63e30bb7"`  
* Requirement: “EPIC026 QA step log manifest”  
  Evidence pointer(s) in Remediation 2 proving satisfaction: Remediation 2 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json || @@ \-0,0 \+1 @@  
  Key proof facts (from Remediation 2 artifacts):  
  * `{"epic":"HDE-EPIC026","manifest_version":"1.0","generated_at_utc":"2026-02-17T12:18:23Z","checks":[]}`  
* Requirement: “EPIC026 doc delta ledger artifacts”  
  Evidence pointer(s) in Remediation 2 proving satisfaction: Remediation 2 → audit/docdeltas/hde-epic026\_doc\_deltas.md → diff \--git a/audit/docdeltas/hde-epic026\_doc\_deltas.md b/audit/docdeltas/hde-epic026\_doc\_deltas.md || @@ \-0,0 \+1,26 @@  
  Key proof facts (from Remediation 2 artifacts):  
  * `Doc Deltas: None (no PF-Canon inconsistencies or new doc requirements found)`  
* Requirement: “TI-002 closure”  
  Evidence pointer(s) in Remediation 2 proving satisfaction: Remediation 2 → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,48 @@  
  Key proof facts (from Remediation 2 artifacts):  
  * `PF09 pointers: HDE-FERM001.3, HDE-COAG007.3`  
  * `TI-002 pointers: HDE-FERM001.3, HDE-COAG007.3`  
  * `ADR status line: ADR-TI002-EPIC026-001`

B) Closure of gaps across attempts (Attempt 0 \+ Attempt 1\)

* Attempt 0 gap (diff integrity / missing hunks) is addressed: attempt 2 includes explicit hunks for `audit/qa/hde-epic026/qa_step_logs_manifest.json` and `audit/qa/hde-epic026/00_meta/doc_deltas.md`.  
  Evidence pointer: Remediation 2 → audit/qa/hde-epic026/00\_meta/doc\_deltas.md → diff \--git a/audit/qa/hde-epic026/00\_meta/doc\_deltas.md b/audit/qa/hde-epic026/00\_meta/doc\_deltas.md || @@ \-0,0 \+1,26 @@  
* Attempt 1 gap (TI-002 closure mapping) is resolved: attempt 2 adds explicit TI-002/PF09 mapping and ADR status line to close report \+ doc delta ledgers.  
  Evidence pointer: Remediation 2 → audit/docdeltas/hde-epic026\_doc\_deltas.md → diff \--git a/audit/docdeltas/hde-epic026\_doc\_deltas.md b/audit/docdeltas/hde-epic026\_doc\_deltas.md || @@ \-0,0 \+1,26 @@

C) Token and gate evidence (names-only; do not invent)

* PF23  
* TI-002  
* SAFE\_MODE=1  
* ALLOW\_NETWORK=0

D) Test/CI proof

* “✅ SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/qa/generate\_epic026\_close\_pack.py”  
  Where it appears: Remediation 2 → \#\# Testing → ✅ SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/qa/generate\_epic026\_close\_pack.py.  
* “✅ python \-m compileall tools/qa/generate\_epic026\_close\_pack.py”  
  Where it appears: Remediation 2 → \#\# Testing → ✅ python \-m compileall tools/qa/generate\_epic026\_close\_pack.py.  
* “✅ CI passed (as reported by Codex internal checks)”  
  Where it appears: Remediation 2 → \#\# CI → ✅ CI passed (as reported by Codex internal checks).

E) Artifact/evidence outputs

* audit/EPIC-026\_MANIFEST.json  
  Evidence pointer: Remediation 2 → audit/EPIC-026\_MANIFEST.json → diff \--git a/audit/EPIC-026\_MANIFEST.json b/audit/EPIC-026\_MANIFEST.json || @@ \-0,0 \+1 @@  
* audit/EPIC-026\_MANIFEST.json.path\_proof.txt  
  Evidence pointer: Remediation 2 → audit/EPIC-026\_MANIFEST.json.path\_proof.txt → diff \--git a/audit/EPIC-026\_MANIFEST.json.path\_proof.txt b/audit/EPIC-026\_MANIFEST.json.path\_proof.txt || @@ \-0,0 \+1 @@  
* audit/EPIC-026\_close\_report.md  
  Evidence pointer: Remediation 2 → audit/EPIC-026\_close\_report.md → diff \--git a/audit/EPIC-026\_close\_report.md b/audit/EPIC-026\_close\_report.md || @@ \-0,0 \+1,48 @@  
* audit/EPIC-026\_close\_report.md.path\_proof.txt  
  Evidence pointer: Remediation 2 → audit/EPIC-026\_close\_report.md.path\_proof.txt → diff \--git a/audit/EPIC-026\_close\_report.md.path\_proof.txt b/audit/EPIC-026\_close\_report.md.path\_proof.txt || @@ \-0,0 \+1,11 @@  
* audit/docdeltas/hde-epic026\_doc\_deltas.md  
  Evidence pointer: Remediation 2 → audit/docdeltas/hde-epic026\_doc\_deltas.md → diff \--git a/audit/docdeltas/hde-epic026\_doc\_deltas.md b/audit/docdeltas/hde-epic026\_doc\_deltas.md || @@ \-0,0 \+1,26 @@  
* audit/qa/hde-epic026/00\_meta/doc\_deltas.md  
  Evidence pointer: Remediation 2 → audit/qa/hde-epic026/00\_meta/doc\_deltas.md → diff \--git a/audit/qa/hde-epic026/00\_meta/doc\_deltas.md b/audit/qa/hde-epic026/00\_meta/doc\_deltas.md || @@ \-0,0 \+1,26 @@  
* audit/qa/hde-epic026/qa\_step\_logs\_manifest.json  
  Evidence pointer: Remediation 2 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json || @@ \-0,0 \+1 @@  
* audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt  
  Evidence pointer: Remediation 2 → audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt → diff \--git a/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt b/audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt || @@ \-0,0 \+1 @@

## 2.14 Docs PR HDE-EPIC026

### Review Summary

* PR updates repo documentation to reflect HDE-EPIC026 reality (README, CHANGELOG, AGENTS, and key `docs/` pages) with a focus on conjunction preview support, CLI usage, and evidence pointers.  
* Changes align with the Approved Plan’s documentation alignment intent for conjunction surfaces and close-pack posture (Deliverables D-007 and D-008).  
* Evidence/test posture for this docs-only PR includes an explicit `hdctl showcompat --help` check plus targeted pytest runs for endpoint catalog and CLI behaviors.  
* Diff review found no scope drift: all changes are confined to markdown documentation files (no code/config edits).  
* Primary risk is “docs drift risk” (docs describe CLI flags/input modes/evidence paths); mitigated by the PR’s stated verification posture, but the correctness still depends on the underlying implementation staying consistent.  
* RCA section included to document the doc-drift “fix” nature (docs previously reflected older epic framing and needed alignment).

### Diff Review (REQUIRED; primary technical review)

1. **DR-001**  
   * Change summary: Updates `AGENTS.md` to reflect HDE-EPIC026 operational reality (close-pack generator, conjunction surfaces, and doc drift-protection guidance).  
   * Risk assessment: Medium  
   * Why it matters: `AGENTS.md` is a behavioral contract for agents; inaccuracies can cause workflow drift or incorrect operational actions.  
   * Evidence pointer:  
     PR Artifacts → AGENTS.md → diff \--git a/AGENTS.md b/AGENTS.md  
     @@ \-1,45 \+1,48 @@  
   * Approved Plan linkage: Approved Plan → Deliverable D-007 — Documentation and catalog alignment for conjunction surfaces  
2. **DR-002**  
   * Change summary: Adds an Unreleased CHANGELOG entry documenting the HDE-EPIC026 docs sweep and the specific doc surfaces updated.  
   * Risk assessment: Low  
   * Why it matters: CHANGELOG is a user-facing audit trail; it must accurately describe what changed (especially for doc-only PRs).  
   * Evidence pointer:  
     PR Artifacts → CHANGELOG.md → diff \--git a/CHANGELOG.md b/CHANGELOG.md  
     @@ \-1,27 \+1,39 @@  
   * Approved Plan linkage: Approved Plan → Deliverable D-007 — Documentation and catalog alignment for conjunction surfaces  
3. **DR-003**  
   * Change summary: Refreshes `README.md` to HDE-EPIC026 framing, adding conjunction preview support notes, CLI examples, and evidence pointers.  
   * Risk assessment: Medium  
   * Why it matters: README is the primary entrypoint; incorrect CLI or endpoint descriptions create immediate user/operator confusion.  
   * Evidence pointer:  
     PR Artifacts → README.md → diff \--git a/README.md b/README.md  
     @@ \-1,101 \+1,104 @@  
   * Approved Plan linkage: Approved Plan → Deliverable D-007 — Documentation and catalog alignment for conjunction surfaces  
4. **DR-004**  
   * Change summary: Updates `docs/CLI_commands.md` to describe `hdctl showcompat --conjunction` input modes, evidence outputs, and drift-safe constraints.  
   * Risk assessment: Medium  
   * Why it matters: CLI docs are high-risk for drift; documenting flags/input modes must match actual in-repo CLI behavior to prevent misuse.  
   * Evidence pointer:  
     PR Artifacts → docs/CLI\_commands.md → diff \--git a/docs/CLI\_commands.md b/docs/CLI\_commands.md  
     @@ \-1,46 \+1,48 @@  
   * Approved Plan linkage: Approved Plan → Deliverable D-007 — Documentation and catalog alignment for conjunction surfaces  
5. **DR-005**  
   * Change summary: Refreshes `docs/EVIDENCE_INDEX.md` for EPIC026 close-pack outputs and adds explicit references to evidence-index “machine companion” artifacts plus conjunction CLI artifacts.  
   * Risk assessment: Medium  
   * Why it matters: Evidence docs govern acceptance/verification posture; wrong paths or missing companions can break auditability and reviewer workflows.  
   * Evidence pointer:  
     PR Artifacts → docs/EVIDENCE\_INDEX.md → diff \--git a/docs/EVIDENCE\_INDEX.md b/docs/EVIDENCE\_INDEX.md  
     @@ \-1,69 \+1,74 @@  
   * Approved Plan linkage: Approved Plan → Deliverable D-008 — Close posture: rails-safe Live QA at close and close-pack completeness  
6. **DR-006**  
   * Change summary: Updates `docs/INDEX.md` to point to the endpoint catalog source-of-truth and QA ledger, and adds conjunction CLI governance as a first-class doc topic.  
   * Risk assessment: Low  
   * Why it matters: `docs/INDEX.md` is the navigation hub; mispointing “source-of-truth” artifacts can cause systemic doc drift.  
   * Evidence pointer:  
     PR Artifacts → docs/INDEX.md → diff \--git a/docs/INDEX.md b/docs/INDEX.md  
     @@ \-1,34 \+1,35 @@  
   * Approved Plan linkage: Approved Plan → Deliverable D-007 — Documentation and catalog alignment for conjunction surfaces  
7. **DR-007**  
   * Change summary: Updates `docs/RUN.md` to EPIC026 framing and adds explicit CLI conjunction/provider-rails posture guidance.  
   * Risk assessment: Medium  
   * Why it matters: RUN docs guide “how to run” flows; incorrect rails guidance (SAFE\_MODE/ALLOW\_NETWORK expectations) can cause unsafe or misleading execution.  
   * Evidence pointer:  
     PR Artifacts → docs/RUN.md → diff \--git a/docs/RUN.md b/docs/RUN.md  
     @@ \-1,70 \+1,72 @@  
   * Approved Plan linkage: Approved Plan → Deliverable D-008 — Close posture: rails-safe Live QA at close and close-pack completeness

### RCA

A) Bug/Failure statement (1–3 sentences; quote key lines from PR Artifacts)

* “Updated README.md to reflect EPIC026 (instead of EPIC025), and to include Conjunction preview support, CLI usage, and evidence pointers.”  
* “Updated docs/EVIDENCE\_INDEX.md to reflect EPIC026 close-pack outputs and evidence index machine-index companions.”

B) Root cause(s)

1. Root cause statement: Repo docs had drifted behind the implemented EPIC026 “conjunction \+ close-pack” reality (still reflecting older epic framing and missing updated surfaces/pointers).  
   * Evidence pointer(s):  
     PR Artifacts → README.md → diff \--git a/README.md b/README.md  
     @@ \-1,101 \+1,104 @@  
     PR Artifacts → docs/EVIDENCE\_INDEX.md → diff \--git a/docs/EVIDENCE\_INDEX.md b/docs/EVIDENCE\_INDEX.md  
     @@ \-1,69 \+1,74 @@

C) Fix in this PR (bullets)

* Updated `README.md`, `CHANGELOG.md`, `AGENTS.md`, and `docs/` pages to reflect EPIC026 conjunction surfaces, CLI usage/input modes, and evidence artifact locations.  
* Added/updated evidence-index companion artifact references and conjunction CLI artifacts list in `docs/EVIDENCE_INDEX.md`.

D) Fix verification (bullets)

* PR Artifacts show a docs-focused verification posture, including `python scripts/hdctl.py showcompat --help` and targeted pytest runs for endpoint catalog and CLI behaviors.  
* Residual risk: Docs correctness around flags/paths remains coupled to implementation drift; continued drift protection depends on keeping docs aligned with in-repo definitions.

### Findings

1. **(DR-001)** Observed `AGENTS.md` was updated to EPIC026 reality including close-pack generator reference and conjunction surfaces enumeration.  
   * Why it matters: `AGENTS.md` drives agent behavior; updating it reduces drift and prevents agents from following outdated EPIC025 guidance.  
   * Evidence pointer(s):  
     PR Artifacts → AGENTS.md → diff \--git a/AGENTS.md b/AGENTS.md  
     @@ \-1,45 \+1,48 @@  
2. **(DR-002)** Observed `CHANGELOG.md` adds “Unreleased — HDE-EPIC026” docs-sweep entry summarizing the specific doc files updated.  
   * Why it matters: Makes doc-only PR scope auditable and reduces reviewer ambiguity about whether this PR touched code vs docs.  
   * Evidence pointer(s):  
     PR Artifacts → CHANGELOG.md → diff \--git a/CHANGELOG.md b/CHANGELOG.md  
     @@ \-1,27 \+1,39 @@  
3. **(DR-003)** Observed `README.md` refresh includes conjunction preview support, CLI `showcompat --conjunction` example, and references to conjunction surface modules.  
   * Why it matters: README is the primary entrypoint; EPIC026 users need accurate, minimal, and current usage guidance.  
   * Evidence pointer(s):  
     PR Artifacts → README.md → diff \--git a/README.md b/README.md  
     @@ \-1,101 \+1,104 @@  
4. **(DR-004)** Observed `docs/CLI_commands.md` now documents `hdctl showcompat --conjunction` input modes and evidence outputs, explicitly avoiding invented “--pair” syntax and describing stdin payload support.  
   * Why it matters: Prevents CLI syntax drift and helps users choose correct input mode without guessing flag contracts.  
   * Evidence pointer(s):  
     PR Artifacts → docs/CLI\_commands.md → diff \--git a/docs/CLI\_commands.md b/docs/CLI\_commands.md  
     @@ \-1,46 \+1,48 @@  
5. **(DR-005)** Observed `docs/EVIDENCE_INDEX.md` updates EPIC naming and adds explicit “machine companion” artifact pointers (`artifacts/evidence_index.sha256`) plus a dedicated “Conjunction CLI artifacts” subsection.  
   * Why it matters: Evidence discoverability and auditability improve; reviewers/operators can locate both human and machine index artifacts consistently.  
   * Evidence pointer(s):  
     PR Artifacts → docs/EVIDENCE\_INDEX.md → diff \--git a/docs/EVIDENCE\_INDEX.md b/docs/EVIDENCE\_INDEX.md  
     @@ \-1,69 \+1,74 @@  
6. **(DR-006)** Observed `docs/INDEX.md` updates the endpoint catalog “source-of-truth” statement and adds “Conjunction CLI governance” as a first-class pointer.  
   * Why it matters: Keeps the docs navigation hub aligned with the shipped catalog/evidence posture; reduces misnavigation and stale references.  
   * Evidence pointer(s):  
     PR Artifacts → docs/INDEX.md → diff \--git a/docs/INDEX.md b/docs/INDEX.md  
     @@ \-1,34 \+1,35 @@  
7. **(DR-007)** Observed `docs/RUN.md` now frames the runbook as EPIC026 and documents provider/network closed-rails posture (SAFE\_MODE/ALLOW\_NETWORK gating) and refusal code expectations.  
   * Why it matters: Operator guidance must reflect rails posture to prevent unsafe assumptions about provider acquisition/network access.  
   * Evidence pointer(s):  
     PR Artifacts → docs/RUN.md → diff \--git a/docs/RUN.md b/docs/RUN.md  
     @@ \-1,70 \+1,72 @@

### Evidence Print (PASS PROOF; required)

A) Tokens satisfied (names-only; do not invent)

* None

B) Evidence artifacts produced/updated

* Path: README.md  
  * Type: markdown  
  * Key proof facts (verbatim):  
    * diff \--git a/README.md b/README.md  
    * @@ \-1,101 \+1,104 @@  
* Path: CHANGELOG.md  
  * Type: markdown  
  * Key proof facts (verbatim):  
    * diff \--git a/CHANGELOG.md b/CHANGELOG.md  
    * @@ \-1,27 \+1,39 @@  
* Path: AGENTS.md  
  * Type: markdown  
  * Key proof facts (verbatim):  
    * diff \--git a/AGENTS.md b/AGENTS.md  
    * @@ \-1,45 \+1,48 @@  
* Path: docs/CLI\_commands.md  
  * Type: markdown  
  * Key proof facts (verbatim):  
    * diff \--git a/docs/CLI\_commands.md b/docs/CLI\_commands.md  
    * @@ \-1,46 \+1,48 @@  
* Path: docs/EVIDENCE\_INDEX.md  
  * Type: markdown  
  * Key proof facts (verbatim):  
    * diff \--git a/docs/EVIDENCE\_INDEX.md b/docs/EVIDENCE\_INDEX.md  
    * @@ \-1,69 \+1,74 @@  
* Path: docs/INDEX.md  
  * Type: markdown  
  * Key proof facts (verbatim):  
    * diff \--git a/docs/INDEX.md b/docs/INDEX.md  
    * @@ \-1,34 \+1,35 @@  
* Path: docs/RUN.md  
  * Type: markdown  
  * Key proof facts (verbatim):  
    * diff \--git a/docs/RUN.md b/docs/RUN.md  
    * @@ \-1,70 \+1,72 @@

C) Test/CI proof

* Job/test name (verbatim): ✅ python scripts/hdctl.py showcompat \--help  
  * Pass indicator (verbatim): ✅ python scripts/hdctl.py showcompat \--help  
  * Where it appears in PR Artifacts: PR Artifacts → \#\# Testing → ✅ python scripts/hdctl.py showcompat \--help  
* Job/test name (verbatim): ✅ pytest \-q tests/http/test\_endpoint\_catalog.py  
  * Pass indicator (verbatim): ✅ pytest \-q tests/http/test\_endpoint\_catalog.py  
  * Where it appears in PR Artifacts: PR Artifacts → \#\# Testing → ✅ pytest \-q tests/http/test\_endpoint\_catalog.py  
* Job/test name (verbatim): ✅ pytest \-q tests/cli/test\_cli\_canonical\_bytes.py  
  * Pass indicator (verbatim): ✅ pytest \-q tests/cli/test\_cli\_canonical\_bytes.py  
  * Where it appears in PR Artifacts: PR Artifacts → \#\# Testing → ✅ pytest \-q tests/cli/test\_cli\_canonical\_bytes.py  
* Job/test name (verbatim): ✅ pytest \-q tests/cli/test\_showcompat\_sources.py  
  * Pass indicator (verbatim): ✅ pytest \-q tests/cli/test\_showcompat\_sources.py  
  * Where it appears in PR Artifacts: PR Artifacts → \#\# Testing → ✅ pytest \-q tests/cli/test\_showcompat\_sources.py

### Doc Deltas (PF-Canon only; REQUIRED; with Canon Check Gate)

CHG-001

* Change: Agent-facing operational guidance updated to EPIC026 conjunction \+ close-pack reality.  
* Evidence pointer:  
  PR Artifacts → AGENTS.md → diff \--git a/AGENTS.md b/AGENTS.md  
  @@ \-1,45 \+1,48 @@  
* Canon basis: CANON SILENCE

CHG-002

* Change: Changelog updated with EPIC026 docs sweep entry.  
* Evidence pointer:  
  PR Artifacts → CHANGELOG.md → diff \--git a/CHANGELOG.md b/CHANGELOG.md  
  @@ \-1,27 \+1,39 @@  
* Canon basis: CANON SILENCE

CHG-003

* Change: README refreshed to EPIC026 and expanded with conjunction preview \+ CLI guidance and evidence pointers.  
* Evidence pointer:  
  PR Artifacts → README.md → diff \--git a/README.md b/README.md  
  @@ \-1,101 \+1,104 @@  
* Canon basis: CANON SILENCE

CHG-004

* Change: CLI docs updated for `hdctl showcompat --conjunction` input modes and evidence outputs.  
* Evidence pointer:  
  PR Artifacts → docs/CLI\_commands.md → diff \--git a/docs/CLI\_commands.md b/docs/CLI\_commands.md  
  @@ \-1,46 \+1,48 @@  
* Canon basis: CANON SILENCE

CHG-005

* Change: Evidence index docs updated for EPIC026 and conjunction CLI artifacts \+ machine companion pointers.  
* Evidence pointer:  
  PR Artifacts → docs/EVIDENCE\_INDEX.md → diff \--git a/docs/EVIDENCE\_INDEX.md b/docs/EVIDENCE\_INDEX.md  
  @@ \-1,69 \+1,74 @@  
* Canon basis: CANON SILENCE

CHG-006

* Change: Docs index updated to clarify endpoint catalog source-of-truth and add conjunction CLI governance.  
* Evidence pointer:  
  PR Artifacts → docs/INDEX.md → diff \--git a/docs/INDEX.md b/docs/INDEX.md  
  @@ \-1,34 \+1,35 @@  
* Canon basis: CANON SILENCE

CHG-007

* Change: Runbook updated to EPIC026 framing with explicit rails posture for CLI conjunction flows.  
* Evidence pointer:  
  PR Artifacts → docs/RUN.md → diff \--git a/docs/RUN.md b/docs/RUN.md  
  @@ \-1,70 \+1,72 @@  
* Canon basis: CANON SILENCE

## 2.15 HDE-EPIC025 Dev Retrospective

### Executive Summary

* This epic (“HDE-EPIC026 / Conjunction Pass 2”) implemented an end-to-end *conjunction compatibility* computation surface with an explicit output contract, deterministic (canonical) JSON emission, and multiple invocation surfaces (engine helper(s), dev-only HTTP endpoints, and a CLI entrypoint). (PF10 — HDE-Build Notes, “\#\# 2.5 PR01 HDE-EPIC026” through “\#\# 2.14 Docs PR HDE-EPIC026”)  
* A dedicated internal/public-facing contract surface for conjunction output (`conjunction_public`) was introduced, including a deterministic “ABBA identity” contract test to prevent output drift. (PF10 — HDE-Build Notes, “\#\# 2.5 PR01 HDE-EPIC026”)  
* Resolver-backed conjunction computation was added to support ID-based invocation pathways, with rails-aware behavior and tests. (PF10 — HDE-Build Notes, “\#\# 2.6 PR02 HDE-EPIC026”)  
* Dev-only HTTP endpoints for conjunction were added (sampler \+ reader \+ writer), and the endpoint catalog artifacts were updated to keep the dev surface discoverable and governed. (PF10 — HDE-Build Notes, “\#\# 2.7 PR03 HDE-EPIC026” and “\#\# 2.8 PR04 HDE-EPIC026”)  
* The CLI gained `hdctl showcompat --conjunction` as an explicit opt-in mode, avoiding silent behavioral changes to existing showcompat semantics. (PF10 — HDE-Build Notes, “\#\# 2.9 PR05 HDE-EPIC026”)  
* Evidence posture was strengthened: canonical JSON gate targets and evidence indexes were updated and anchored with path-proofs; a topology demo output was recorded as governed evidence. (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)  
* A closure-pack generator plus governed close artifacts were added under `audit/` to support leadership closure review and drain planning (manifest, close report, doc-delta ledger, drain targets). (PF10 — HDE-Build Notes, “\#\# 2.13 PR08 HDE-EPIC026”)  
* Repo docs were swept and updated (README/CHANGELOG/AGENTS \+ docs/ excluding pfcanon) to reflect what actually landed. (PF10 — HDE-Build Notes, “\#\# 2.14 Docs PR HDE-EPIC026”)

Biggest wins / biggest remaining risks & gaps (without declaring closure):

* **Win:** Determinism was treated as a first-class contract property (ABBA identity \+ canonical JSON gate inclusion), reducing drift risk across CLI/HTTP/contract surfaces. (PF10 — HDE-Build Notes, “\#\# 2.5 PR01 HDE-EPIC026” and “\#\# 2.12 PR07 HDE-EPIC026”)  
* **Win:** Endpoint discoverability and governance improved via catalog \+ hashes, and evidence was centralized via an index \+ path-proof anchors. (PF10 — HDE-Build Notes, “\#\# 2.7 PR03 HDE-EPIC026” and “\#\# 2.12 PR07 HDE-EPIC026”)  
* **Risk/GAP:** Docs updates (notably CLI help semantics) included at least one “verified but not excerpted” claim, reducing auditability of exact CLI syntax/flags from in-PR evidence alone. (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)  
* **Risk/GAP:** There is an evidenced canon-vs-reality tension around governed artifact “dual-home” expectations vs the practical need to surface artifacts in both `audit/` and `docs/` (addressed via doc delta, but still a drain item). (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)  
* **Risk/GAP:** Exit-code mapping and CLI/vendor semantics have an explicitly called-out mismatch area that needs canonical reconciliation when draining. (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)

---

### Implementation Report (What happened in the repo)

#### PR/step breakdown (PR1…PRN or equivalent)

**PR01**

* **Purpose:** Introduce the internal conjunction output contract surface (`conjunction_public`) and enforce deterministic canonical output (ABBA identity test). (PF10 — HDE-Build Notes, “\#\# 2.5 PR01 HDE-EPIC026”)  
* **Key changes (high level):**  
  * Added/defined `conjunction_public` contract surface and output shape.  
  * Added deterministic contract test verifying canonical bytes and ABBA identity behavior. (PF10 — HDE-Build Notes, “\#\# 2.5 PR01 HDE-EPIC026”)  
* **Key surfaces touched:** engine compatibility compute \+ contract documentation \+ contract tests. (PF10 — HDE-Build Notes, “\#\# 2.5 PR01 HDE-EPIC026”)  
* **Tests/evidence produced:** `pytest -q tests/compat/test_conjunction_contract_public.py` recorded as `8 passed`. (PF10 — HDE-Build Notes, “\#\# 2.5 PR01 HDE-EPIC026”)  
* **Outcome:** Accepted after a remediation that aligned “ABBA identity” with the contract’s deterministic expectations. (PF10 — HDE-Build Notes, “\#\# 2.5 PR01 HDE-EPIC026”)

**PR02**

* **Purpose:** Add resolver-backed conjunction computation (`conjunction_public_resolved`) and ensure rails-aware behavior and correctness with tests. (PF10 — HDE-Build Notes, “\#\# 2.6 PR02 HDE-EPIC026”)  
* **Key changes (high level):**  
  * Added a resolved-conjunction helper that accepts resolved “left/right” and/or ID-backed inputs and returns the public conjunction contract. (PF10 — HDE-Build Notes, “\#\# 2.6 PR02 HDE-EPIC026”)  
  * Included an RCA because the PR contained a fix to ensure the function does not compute on “None” resolved records and instead errors deterministically. (PF10 — HDE-Build Notes, “\#\# 2.6 PR02 HDE-EPIC026”)  
* **Key surfaces touched:** engine compat compute/resolve logic; error handling; tests. (PF10 — HDE-Build Notes, “\#\# 2.6 PR02 HDE-EPIC026”)  
* **Tests/evidence produced:** `pytest -q tests/http/test_compat_conjunction_resolve.py` recorded as `13 passed`. (PF10 — HDE-Build Notes, “\#\# 2.6 PR02 HDE-EPIC026”)  
* **Outcome:** Accepted. (PF10 — HDE-Build Notes, “\#\# 2.6 PR02 HDE-EPIC026”)

**PR03**

* **Purpose:** Add dev-only HTTP surfaces for conjunction sampling and reading, and update endpoint catalog artifacts. (PF10 — HDE-Build Notes, “\#\# 2.7 PR03 HDE-EPIC026”)  
* **Key changes (high level):**  
  * Added `GET /dev/sampler/conjunction` and `GET /dev/reader/conjunction` endpoints. (PF10 — HDE-Build Notes, “\#\# 2.7 PR03 HDE-EPIC026”)  
  * Updated endpoint catalog sources (`docs/ENDPOINTS_CATALOG.md`, `audit/ENDPOINTS_CATALOG.json`, `audit/ENDPOINTS_CATALOG.sha256`). (PF10 — HDE-Build Notes, “\#\# 2.7 PR03 HDE-EPIC026”)  
* **Key surfaces touched:** HTTP adapter routes; endpoint catalog artifacts. (PF10 — HDE-Build Notes, “\#\# 2.7 PR03 HDE-EPIC026”)  
* **Tests/evidence produced:** `pytest -q tests/http/test_dev_conjunction.py` recorded as `5 passed`. (PF10 — HDE-Build Notes, “\#\# 2.7 PR03 HDE-EPIC026”)  
* **Outcome:** Accepted. (PF10 — HDE-Build Notes, “\#\# 2.7 PR03 HDE-EPIC026”)

**PR04**

* **Purpose:** Add dev-only writer endpoint for conjunction and improve canonicalization utility reuse. (PF10 — HDE-Build Notes, “\#\# 2.8 PR04 HDE-EPIC026”)  
* **Key changes (high level):**  
  * Added `POST /dev/writer/conjunction`. (PF10 — HDE-Build Notes, “\#\# 2.8 PR04 HDE-EPIC026”)  
  * Refactored canonicalization so contract and dev endpoints share deterministic JSON emission behavior. (PF10 — HDE-Build Notes, “\#\# 2.8 PR04 HDE-EPIC026”)  
  * Updated dev conjunction contract doc and endpoint catalogs again. (PF10 — HDE-Build Notes, “\#\# 2.8 PR04 HDE-EPIC026”)  
* **Key surfaces touched:** HTTP adapter; canonicalization utilities; dev contract docs; endpoint catalogs. (PF10 — HDE-Build Notes, “\#\# 2.8 PR04 HDE-EPIC026”)  
* **Tests/evidence produced:** `pytest -q tests/http/test_dev_conjunction.py` recorded as `5 passed`. (PF10 — HDE-Build Notes, “\#\# 2.8 PR04 HDE-EPIC026”)  
* **Outcome:** Accepted. (PF10 — HDE-Build Notes, “\#\# 2.8 PR04 HDE-EPIC026”)

**PR05 (multi-attempt lifecycle: original \+ remediation)**

* **Purpose:** Extend CLI `hdctl showcompat` with an explicit conjunction mode flag and deterministic output behavior, without breaking existing showcompat default semantics. (PF10 — HDE-Build Notes, “\#\# 2.9 PR05 HDE-EPIC026”)  
* **Key changes (high level):**  
  * Added `--conjunction` flag to `hdctl showcompat` with canonical JSON output under a conjunction payload key. (PF10 — HDE-Build Notes, “\#\# 2.9 PR05 HDE-EPIC026”)  
  * Fixed a closed-rails behavior gap so the CLI fails deterministically (instead of producing partial/incorrect results) when required data is missing locally. (PF10 — HDE-Build Notes, “\#\# 2.9 PR05 HDE-EPIC026”)  
* **Key surfaces touched:** CLI parser/command implementation; rails gating; CLI tests; CLI docs touchpoints. (PF10 — HDE-Build Notes, “\#\# 2.9 PR05 HDE-EPIC026”)  
* **Tests/evidence produced:** Recorded:  
  * `pytest -q tests/test_showcompat_conjunction.py` \=\> `5 passed`  
  * `pytest -q tests/test_showcompat_conjunction_closedrails.py` \=\> `4 passed` (PF10 — HDE-Build Notes, “\#\# 2.9 PR05 HDE-EPIC026”)  
* **Outcome:** Accepted after remediation. (PF10 — HDE-Build Notes, “\#\# 2.9 PR05 HDE-EPIC026”)

**PR06**

* **Purpose:** Docs alignment for conjunction usage: clarify CLI invocation patterns, input modes, side effects, and dev endpoint usage; keep docs consistent with what landed. (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)  
* **Key changes (high level):**  
  * Updated `docs/CLI_commands.md` and `docs/RUN.md` with a Conjunction-mode section, input-mode guidance, and a side-effects note (e.g., payload-only inputs are compute-only; ID-based inputs may resolve/ingest depending on rails and source). (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)  
  * Added an explicit note that dump/sidecar flags are disallowed in conjunction mode. (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)  
  * Recorded a known mismatch zone around exit codes and said PF05 remains canonical for that mapping. (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)  
* **Key surfaces touched:** docs only (`docs/CLI_commands.md`, `docs/RUN.md`). (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)  
* **Tests/evidence produced:** No tests recorded (docs-only), and PF10 explicitly notes the PR claimed `hdctl showcompat --help` was checked but did not include the excerpt as evidence. (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)  
* **Outcome:** Accepted with an evidentiary caution about the missing help excerpt. (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)

**PR07**

* **Purpose:** Strengthen evidence posture: bring conjunction outputs into governed canonical JSON checks; add evidence index \+ path proof anchors; record topology demo output as governed evidence. (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)  
* **Key changes (high level):**  
  * Added/updated canonical JSON gate targets so conjunction output artifacts are included. (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)  
  * Added a governed evidence index (`docs/evidence/INDEX.md`) and path-proofs referencing specific `audit/qa/hde-epic026/...` evidence families. (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)  
  * Added/updated `audit/qa/hde-epic026/...` artifacts, including canonical JSON outputs and a topology demo output. (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)  
* **Key surfaces touched:** QA/gates; evidence artifacts; docs evidence index and anchors. (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)  
* **Tests/evidence produced:** Canonical gate run evidence recorded as pass (log file under `audit/gates/json_gate/...`) and topology demo evidence updated. (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)  
* **Outcome:** Accepted with an explicit doc delta (PF12 alignment) recorded in PF10’s PR07 review. (PF10 — HDE-Build Notes, “\#\# 2.12 PR07 HDE-EPIC026”)

**PR08 (3-attempt lifecycle: attempt 0 → non-passing remediation → final remediation)**

* **Purpose:** Create a repeatable epic closure-pack generator and ensure the epic’s closure evidence and drain planning are explicitly recorded as governed artifacts. (PF10 — HDE-Build Notes, “\#\# 2.13 PR08 HDE-EPIC026”)  
* **Key changes (high level):**  
  * Added `tools/qa/generate_epic026_close_pack.py`. (PF10 — HDE-Build Notes, “\#\# 2.13 PR08 HDE-EPIC026”)  
  * Produced closure artifacts:  
    * `audit/EPIC-026_MANIFEST.json`  
    * `audit/EPIC-026_close_report.md`  
    * `audit/docdeltas/hde-epic026_doc_deltas.md`  
    * `audit/docdeltas/hde-epic026_drain_targets.md` (PF10 — HDE-Build Notes, “\#\# 2.13 PR08 HDE-EPIC026”)  
  * Resolved a remediation failure cluster related to TI-002 mapping and explicit canon pointers. (PF10 — HDE-Build Notes, “\#\# 2.13 PR08 HDE-EPIC026”)  
* **Key surfaces touched:** QA tooling; `audit/` closure pack artifacts; drain target planning outputs. (PF10 — HDE-Build Notes, “\#\# 2.13 PR08 HDE-EPIC026”)  
* **Tests/evidence produced:** Closure artifacts \+ explicit token list (including TI-002) recorded. (PF10 — HDE-Build Notes, “\#\# 2.13 PR08 HDE-EPIC026”)  
* **Outcome:** Accepted after attempt 2 remediation. (PF10 — HDE-Build Notes, “\#\# 2.13 PR08 HDE-EPIC026”)

**Docs PR**

* **Purpose:** Final repo docs sweep to make README/CHANGELOG/AGENTS and docs/ consistent with what landed in the epic, excluding pfcanon (read-only). (PF10 — HDE-Build Notes, “\#\# 2.14 Docs PR HDE-EPIC026”)  
* **Key changes (high level):**  
  * Updated `README.md`, `CHANGELOG.md`, `AGENTS.md`, and relevant `docs/` files (excluding `docs/pfcanon/`). (PF10 — HDE-Build Notes, “\#\# 2.14 Docs PR HDE-EPIC026”)  
* **Key surfaces touched:** docs only. (PF10 — HDE-Build Notes, “\#\# 2.14 Docs PR HDE-EPIC026”)  
* **Tests/evidence produced:** No explicit CI/doc-lint evidence recorded in PF10 for this PR; acceptance hinged on accuracy, link sanity, and in-repo verification of commands/flags. (PF10 — HDE-Build Notes, “\#\# 2.14 Docs PR HDE-EPIC026”)  
* **Outcome:** Accepted. (PF10 — HDE-Build Notes, “\#\# 2.14 Docs PR HDE-EPIC026”)

---

#### Major surfaces affected (CLI/API/DB/evidence/QA harness/etc.)

* **Engine compatibility computation surface**  
  * Introduction of public conjunction contract surface and resolved variants. (PF10 — HDE-Build Notes, PR01 \+ PR02 sections)  
* **HTTP dev-only endpoint layer**  
  * `/dev/sampler/conjunction`, `/dev/reader/conjunction`, `/dev/writer/conjunction`. (PF10 — HDE-Build Notes, PR03 \+ PR04 sections)  
* **CLI**  
  * `hdctl showcompat --conjunction` mode, including deterministic output constraints and rails behavior. (PF10 — HDE-Build Notes, PR05 section)  
* **Contracts documentation**  
  * `docs/contracts/compat_conjunction_contract.md` and `docs/contracts/dev_conjunction_contract.md`. (PF10 — HDE-Build Notes, PR01 \+ PR04 sections; explicit paths appear in PR evidence)  
* **Governed endpoint catalog**  
  * `docs/ENDPOINTS_CATALOG.md`, `audit/ENDPOINTS_CATALOG.json`, `audit/ENDPOINTS_CATALOG.sha256`. (PF10 — HDE-Build Notes, PR03 \+ PR04 sections)  
* **Evidence and QA harness**  
  * Canonical JSON gate inclusion and logs; evidence index \+ path proofs; topology demo output. (PF10 — HDE-Build Notes, PR07 section)  
* **Epic closure tooling and artifacts**  
  * Close pack generator and closure artifacts under `audit/`. (PF10 — HDE-Build Notes, PR08 section)

---

#### Evidence inventory (what exists)

Concrete evidence artifacts / logs / tests produced (as recorded in PF10):

* **Contract tests (determinism / ABBA identity)**  
  * `pytest -q tests/compat/test_conjunction_contract_public.py` \=\> `8 passed` (PF10 — HDE-Build Notes, PR01)  
* **Resolver-backed conjunction tests**  
  * `pytest -q tests/http/test_compat_conjunction_resolve.py` \=\> `13 passed` (PF10 — HDE-Build Notes, PR02)  
* **Dev endpoint tests**  
  * `pytest -q tests/http/test_dev_conjunction.py` \=\> `5 passed` (PF10 — HDE-Build Notes, PR03 and PR04)  
* **CLI conjunction tests**  
  * `pytest -q tests/test_showcompat_conjunction.py` \=\> `5 passed`  
  * `pytest -q tests/test_showcompat_conjunction_closedrails.py` \=\> `4 passed` (PF10 — HDE-Build Notes, PR05)  
* **Governed endpoint catalog artifacts**  
  * `docs/ENDPOINTS_CATALOG.md`  
  * `audit/ENDPOINTS_CATALOG.json`  
  * `audit/ENDPOINTS_CATALOG.sha256` (PF10 — HDE-Build Notes, PR03/PR04)  
* **Governed canonical JSON gate / evidence**  
  * `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` (pass log)  
  * `docs/evidence/INDEX.md`  
  * `docs/evidence/path_proof/...` anchors referencing `audit/qa/hde-epic026/...` families  
  * `audit/qa/hde-epic026/canon_json/...` canonical full outputs (public contract \+ dev reader contract)  
  * `audit/qa/hde-epic026/topology/topology_conjunction_demo.json` (+ README) (PF10 — HDE-Build Notes, PR07)  
* **Epic closure pack artifacts**  
  * `tools/qa/generate_epic026_close_pack.py`  
  * `audit/EPIC-026_MANIFEST.json`  
  * `audit/EPIC-026_close_report.md`  
  * `audit/docdeltas/hde-epic026_doc_deltas.md`  
  * `audit/docdeltas/hde-epic026_drain_targets.md` (PF10 — HDE-Build Notes, PR08)  
* **Docs sweep artifacts**  
  * `README.md`, `CHANGELOG.md`, `AGENTS.md`, plus selected `docs/` updates excluding pfcanon. (PF10 — HDE-Build Notes, Docs PR)

---

#### Evidence gaps (if any; label Unknown if you cannot verify)

* **CLI help output excerpt missing:** PF10 explicitly notes the docs PR/step claimed `hdctl showcompat --help` was checked but did not include the help output excerpt in evidence. This makes exact flag/usage drift harder to audit from the PR record alone. (PF10 — HDE-Build Notes, “\#\# 2.11 PR06 HDE-EPIC026”)  
* **Docs PR lint/validation evidence:** PF10 does not record a specific doc-lint/markdown validation command run for the Docs PR step. **Unknown** whether the repo has a doc lint job; would need a CI job log or a recorded local command \+ output. (PF10 — HDE-Build Notes, “\#\# 2.14 Docs PR HDE-EPIC026”)

---

### Retrospective (Process)

#### What went well

* The epic was decomposed into small PRs with narrowly-scoped intent (contract → resolved compute → dev endpoints → CLI → docs → evidence posture → closure pack), which reduced blast radius per change. (PF10 — HDE-Build Notes, PR01–PR08)  
* Determinism and drift protection were treated as *contract properties* early (ABBA identity \+ canonical JSON gate targeting), rather than “best effort”. (PF10 — HDE-Build Notes, PR01 \+ PR07)  
* Each invocation surface (engine helper, HTTP dev endpoints, CLI) was paired with tests or governed artifacts rather than shipping unverified behavior. (PF10 — HDE-Build Notes, PR01/02/03/04/05/07)  
* Endpoint governance improved through catalog \+ hash artifacts, reducing ambiguity about what dev endpoints exist and how they are expected to behave. (PF10 — HDE-Build Notes, PR03/PR04)  
* The epic created explicit closure-pack tooling and artifacts, which reduces ad-hoc closure decision-making and supports drain planning. (PF10 — HDE-Build Notes, PR08)  
* A final docs sweep was treated as a distinct PR step, minimizing the chance that docs correctness was lost among code diffs. (PF10 — HDE-Build Notes, Docs PR)

#### What did not go well

* Business case and “why a new contract/flag exists” had to be escalated into an explicit policy requirement (PF10 addendum) after confusion/drift concerns surfaced—this should have been explicit earlier. (PF10 — HDE-Build Notes, “\#\# 2.10 Addendum: Business-case requirement for epic plans”)  
* Some steps required remediation cycles (PR05; PR08 with a non-passing remediation attempt), indicating gaps in initial evidence posture / acceptance targeting / drift controls. (PF10 — HDE-Build Notes, PR05 and PR08)  
* Docs validation evidence was sometimes asserted rather than captured (e.g., `hdctl showcompat --help` checked but not excerpted). (PF10 — HDE-Build Notes, PR06)  
* Canon drift around artifacts/evidence location and “dual-home” expectations required explicit doc delta handling rather than being resolved by design up front. (PF10 — HDE-Build Notes, PR07)  
* Exit-code semantics and numeric mappings were surfaced as a “known mismatch” zone late, rather than being reconciled concurrently with CLI documentation changes. (PF10 — HDE-Build Notes, PR06)

#### What we learned (Process)

* Epic plans must carry an explicit **business case** and an explicit **contract-change justification**, including why a new flag/contract is required and how backward compatibility is preserved. (PF10 — HDE-Build Notes, “\#\# 2.10 Addendum: Business-case requirement for epic plans”)  
* “Verified locally” claims in docs PRs should be replaced with *captured evidence* (command \+ output excerpt) to avoid audit gaps.  
* Multi-surface features (engine \+ HTTP \+ CLI) need a single source of truth for output shape and canonicalization utility reuse to avoid drift; refactors enabling shared canonicalization are not “nice-to-have”. (PF10 — HDE-Build Notes, PR04 \+ PR07)  
* When evidence artifacts exist under `audit/`, having a documented index and path-proof anchors under `docs/` meaningfully reduces reviewer cognitive load and improves closure readiness (without implying closure). (PF10 — HDE-Build Notes, PR07)  
* Closure-pack automation is valuable when an epic spans multiple remediation attempts because it forces explicit provenance and drain planning. (PF10 — HDE-Build Notes, PR08)

---

### Retrospective (Application / System)

#### What we learned about the system itself

* Conjunction compatibility is a *distinct output contract* that needs explicit opt-in at the CLI layer (`--conjunction`) to prevent accidental breaking changes to existing showcompat behavior. (PF10 — HDE-Build Notes, PR05)  
* Resolver/rails behavior is a major axis of correctness and “side effects vs compute-only” semantics; documenting invocation modes and rails-dependent behavior is necessary to prevent operator confusion. (PF10 — HDE-Build Notes, PR06)  
* Dev-only endpoints are a practical bridge for validating new compute contracts, but they must be documented and cataloged to prevent “hidden surface area” drift. (PF10 — HDE-Build Notes, PR03 \+ PR04)  
* Evidence gates (canonical JSON checks) must include new contract artifacts explicitly, otherwise the most drift-prone surfaces (serialized output) can regress silently. (PF10 — HDE-Build Notes, PR07)

#### Known remaining risks / debt

**Must-fix**

* Canon reconciliation for exit-code mappings and any “known mismatch” zones documented during the epic (drain target identified as PF05). (PF10 — HDE-Build Notes, PR06)  
* Resolve canon guidance vs practice for evidence artifact “dual-home” so future epics don’t re-litigate where governed artifacts must live. (PF10 — HDE-Build Notes, PR07)

**Should-fix**

* Strengthen docs evidence capture for CLI syntax/flags by embedding `--help` excerpts (or equivalent authoritative evidence) into governed artifacts, rather than relying on narrative assertions. (PF10 — HDE-Build Notes, PR06)  
* Add an explicit, repeatable doc-lint or markdown validation step (if not already present) and record its output in evidence for docs-only PRs. (PF10 — HDE-Build Notes, Docs PR)

**Nice-to-have**

* Expand e2e coverage that exercises conjunction flows across surfaces (engine → dev endpoints → CLI) in a single harness run, if such an e2e harness exists or is planned (Unknown whether in-scope; would need PF10 or PF-Canon evidence).

---

### Canon Alignment and Documentation Outcomes

#### 5.1 Canon references used

Titles only (locators included only where already explicitly captured verbatim in PF10):

* PF10 — HDE-Build Notes  
* PF05 — PF05-Canon-HDE-CLI-API-Vendor-Ref  
* PF06 — PF06-Canon-Epic-Process-Guide  
* PF09 — PF09-Canon-HDE-Build-Checklist  
* PF12 — PF12-Canon-HDE-Schemas-and-Artifacts  
* PF19 — PF19-Canon-Glow-QA-Guide  
* PF27 — PF27-Canon-Plan-Templates  
* PF04 — PF04-Canon-HDE-Governance

#### 5.2 Proposed PF10 Addenda (contain drain targets / doc delta intents)

**Addendum: Require business case \+ contract/flag justification in epic plans**

* **Why:** Confusion and drift-risk concerns emerged around “why a new contract/flag exists,” prompting PF10 to introduce a hard planning requirement. (PF10 — HDE-Build Notes, “\#\# 2.10 Addendum: Business-case requirement for epic plans”)  
* **Decision / rule / clarification:**  
  * Epic plans must include: business case, contract changes/new surfaces justification, and explicit “why new flag vs reuse existing surface” rationale.  
  * Plans must state backward-compat posture and what remains unchanged by default.  
* **Drain targets (doc delta intents):**  
  * PF27 — PF27-Canon-Plan-Templates: add required sections for business case \+ contract/flag rationale and backward-compat plan.  
  * PF06 — PF06-Canon-Epic-Process-Guide: add a gate/checklist item requiring these plan sections before implementation begins.  
* **Supersedes / conflicts:** None explicitly recorded.  
* **Implementation impact:**  
  * Reduces recurrence of “feature drift” disputes during implementation/review.  
  * Makes “new contract” introductions auditable and intentional.

**Addendum: Clarify governed artifact location rules vs dual-home practice for evidence \+ docs anchors**

* **Why:** PR07 recorded a canon tension where artifacts are both governed under `audit/` and referenced/anchored under `docs/`, conflicting with a strict “single home” interpretation. (PF10 — HDE-Build Notes, PR07 doc delta discussion)  
* **Decision / rule / clarification:**  
  * Define when dual-home is allowed (e.g., governed raw artifacts in `audit/`, human-facing index/anchors in `docs/`), and what must remain immutable.  
  * Clarify which file types are “source of truth” vs “documentation pointers”.  
* **Drain targets (doc delta intents):**  
  * PF12 — PF12-Canon-HDE-Schemas-and-Artifacts: clarify governed artifact families, allowed reference/anchor patterns, and acceptable dual-home layouts.  
  * PF19 — PF19-Canon-Glow-QA-Guide: clarify audit/evidence recording conventions and how indexes/path proofs should point to governed artifacts.  
* **Supersedes / conflicts:** Potential conflict with existing “single home” expectations (exact section locator already captured in PF10 PR07 review; drain should reconcile).  
* **Implementation impact:**  
  * Prevents future epics from duplicating evidence drift debates.  
  * Makes docs/evidence discoverability compatible with governance.

**Addendum: Conjunction CLI mode semantics and contract shape must be canonicalized**

* **Why:** The epic introduced a distinct `--conjunction` mode and new output shape; docs were updated, but at least one “help checked” claim lacked excerpted evidence. (PF10 — HDE-Build Notes, PR05 \+ PR06)  
* **Decision / rule / clarification:**  
  * Canon must specify the conjunction-mode output envelope shape, required inputs (two parties), and disallowed flags in conjunction mode (e.g., dump sidecars).  
  * Canon must specify rails-dependent side effects vs compute-only invocation modes.  
* **Drain targets (doc delta intents):**  
  * PF05 — PF05-Canon-HDE-CLI-API-Vendor-Ref: add `showcompat --conjunction` syntax, input modes, output shape, and constraints; reconcile exit code mappings mentioned as mismatched in PR06.  
* **Supersedes / conflicts:** May require reconciling existing showcompat contract text with the new conjunction payload contract.  
* **Implementation impact:**  
  * Improves drift protection for CLI syntax.  
  * Reduces future operator confusion about what “conjunction mode” does.

**Addendum: Standardize epic closure pack contents \+ TI-002 mapping expectations**

* **Why:** PR08 required multiple remediation attempts and ultimately established a specific closure pack schema \+ mapping requirements (including TI-002). (PF10 — HDE-Build Notes, PR08)  
* **Decision / rule / clarification:**  
  * Define the expected closure pack file set and the minimum required fields.  
  * Require explicit mapping for TI-002 (and similar) and explicit “canon pointer” fields in closure reports.  
* **Drain targets (doc delta intents):**  
  * PF09 — PF09-Canon-HDE-Build-Checklist: add closure-pack generator expectations and required closure artifacts (manifest, close report, doc delta ledger, drain targets).  
  * PF04 — PF04-Canon-HDE-Governance: clarify TI-002 and related token semantics if TI-\* tokens are governed here.  
* **Supersedes / conflicts:** None explicitly recorded.  
* **Implementation impact:**  
  * Makes multi-attempt epics easier to close and drain consistently.

**Uncertain drain targets (only where genuinely unsure)**

* None identified beyond the targets above (PF10 already points to PF27/PF06 for the business-case rule; PR07 points to PF12; PR08 points to PF09 and TI-002 mapping).

#### 5.3 Token and evidence semantics (if applicable)

Token/evidence semantics explicitly recorded as satisfied in-epic include:

* `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_PATH_PROOF_OK`, `JSON_CANONICAL_CHECK_OK`, `TOPOLOGY_CONJUNCTION_DEMO_OK` (PF10 — HDE-Build Notes, PR07 Evidence Print)  
* `TI-002`, plus execution constraints `SAFE_MODE=1` and `ALLOW_NETWORK=0` recorded in PR08 pass proof (PF10 — HDE-Build Notes, PR08 Evidence Print)

Observed drift/clarification needs (captured above inside PF10 addenda proposals):

* Canon needs clearer guidance on **artifact location and dual-home** patterns (audit artifacts vs docs anchors/indexes). (PF10 — HDE-Build Notes, PR07)  
* Canon needs tighter specification of **CLI conjunction mode** (syntax \+ output shape \+ rails side effects \+ disallowed dump flags) and reconciliation of **exit code mapping** mismatches. (PF10 — HDE-Build Notes, PR06)

---

### Closure Evidence Snapshot (for Lead decision)

#### 6.1 Evidence produced

Concrete evidence artifacts/logs/tests recorded in PF10 (non-exhaustive; focusing on closure-critical surfaces):

* Contract determinism:  
  * `pytest -q tests/compat/test_conjunction_contract_public.py` \=\> `8 passed` (supports contract determinism expectations). (PF10 — HDE-Build Notes, PR01)  
* Resolver-backed compute correctness:  
  * `pytest -q tests/http/test_compat_conjunction_resolve.py` \=\> `13 passed`. (PF10 — HDE-Build Notes, PR02)  
* Dev endpoints:  
  * `pytest -q tests/http/test_dev_conjunction.py` \=\> `5 passed` (sampler/reader/writer coverage across PR03/PR04). (PF10 — HDE-Build Notes, PR03/PR04)  
* CLI conjunction:  
  * `pytest -q tests/test_showcompat_conjunction.py` \=\> `5 passed`  
  * `pytest -q tests/test_showcompat_conjunction_closedrails.py` \=\> `4 passed`. (PF10 — HDE-Build Notes, PR05)  
* Governed catalogs / evidence:  
  * `audit/ENDPOINTS_CATALOG.json` \+ `audit/ENDPOINTS_CATALOG.sha256` \+ `docs/ENDPOINTS_CATALOG.md`. (PF10 — HDE-Build Notes, PR03/PR04)  
  * Canonical JSON gate pass log: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`. (PF10 — HDE-Build Notes, PR07)  
  * Evidence index \+ path proofs: `docs/evidence/INDEX.md` and `docs/evidence/path_proof/...`. (PF10 — HDE-Build Notes, PR07)  
  * Topology demo evidence: `audit/qa/hde-epic026/topology/topology_conjunction_demo.json` (+ README). (PF10 — HDE-Build Notes, PR07)  
* Closure pack:  
  * `audit/EPIC-026_MANIFEST.json`, `audit/EPIC-026_close_report.md`, `audit/docdeltas/hde-epic026_doc_deltas.md`, `audit/docdeltas/hde-epic026_drain_targets.md`, generated via `tools/qa/generate_epic026_close_pack.py`. (PF10 — HDE-Build Notes, PR08)  
* Evidence tokens explicitly recorded as satisfied (names only):  
  * PR07: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_PATH_PROOF_OK`, `JSON_CANONICAL_CHECK_OK`, `TOPOLOGY_CONJUNCTION_DEMO_OK` (PF10 — HDE-Build Notes, PR07)  
  * PR08: `TI-002` (PF10 — HDE-Build Notes, PR08)

#### 6.2 Evidence missing or ambiguous

* **CLI help output excerpt** (missing/ambiguous):  
  * Missing: captured excerpt of `hdctl showcompat --help` showing actual flags and syntax as shipped.  
  * What would prove it: a governed artifact (log or markdown excerpt) containing the command \+ output, or a CI artifact log containing the same. (PF10 — HDE-Build Notes, PR06 notes)  
* **Docs PR validation evidence** (ambiguous):  
  * Missing: a recorded doc-lint / markdown validation command \+ output for the docs sweep PR.  
  * What would prove it: CI job logs or a local command transcript recorded in governed evidence. (PF10 — HDE-Build Notes, Docs PR)

#### 6.3 Open closure items / questions for the Lead

* Drain planning: confirm whether the proposed PF10 addenda drain targets (PF27/PF06; PF12; PF05; PF09/PF04) are accepted as the official drain plan for this epic. (PF10 — HDE-Build Notes, PR07 \+ PR08 \+ Addendum 2.10)  
* Canon reconciliation: decide how/when to reconcile the exit-code mismatch zone and ensure PF05 becomes the single authoritative reference for CLI semantics (including conjunction mode). (PF10 — HDE-Build Notes, PR06)  
* Evidence posture decision: decide whether missing “CLI help excerpt” and “docs-lint proof” are acceptable gaps or require additional governed evidence artifacts before closure. (PF10 — HDE-Build Notes, PR06 \+ Docs PR)

## 2.16 QA planning reality and plan-created artifacts (PF23 consult, locus provenance lock, plan-created outputs)

Timestamp: 022226  
Details:

Baseline principles (normative)

1. During QA, only loci that actually exist in the product may be treated as repo-resident and tested as such.  
2. Scripts, commands, and checks that do not exist MUST NOT be imagined or substituted.  
3. Plan-created deliverables are allowed. For each plan-created output, the Plan MUST name the exact repo-relative path and filename and include runnable instructions that produce the file at that path (creating parent directories if needed).

Veto (explicit)

The following statement is vetoed and MUST NOT be used in QA prompts, QA plans, or reviews:

"\* PF23 consult MUST NOT be consulted for QA planning or QA execution (including Live QA plans and runbooks)."

Rules (normative)

A) PF23 consultation is required in QA planning (planning-time, read-only)

1. PF23 MUST be consulted during QA planning. Any QA planning activity (including drafting, reviewing, or approving a Live QA Plan) MUST consult PF23 — Reality Audits as a primary input for repo-reality context and existence or locus framing.  
2. PF23 SHOULD be consulted before approving any plan that names repo-resident loci. If a plan references any repo-resident locus (paths, endpoints, routes, scripts, checks, test identifiers, environment variable names treated as already-existing, or fixed output locations treated as already-existing), the reviewer SHOULD consult PF23 first to reduce drift and avoid fabricated or stale locus assumptions.  
3. Consultation is read-only; updates remain PO-only. QA plans MUST NOT mandate PF23 edits, and QA execution MUST NOT include PF23 updates as a required output. PF23 maintenance remains a manual PO operation.  
4. Conflict posture. If PF23’s current record appears inconsistent with other allowed repo-reality sources, the QA plan and review MUST treat this as a reality ambiguity and MUST NOT guess or assert a reconciled locus as fact inside the plan.

B) QA planning locus provenance lock (repo-resident loci)

1. Allowed provenance sources (exclusive). In QA planning artifacts (including Live QA Plans, QA Guides, QA reviews, QA prompts, and QA checklists), the ONLY allowed sources for any repo-reality claim are:  
   * PF10 — HDE Build Notes  
   * PF-Canon (any PF document)  
   * The initial QA Audit for the epic (repo reality and readiness proof)  
2. Locus allowlist (what this applies to). This rule applies to any repo-resident or repo-reality string, including:  
   * file paths and directory paths  
   * endpoint names and routes  
   * module and component identifiers  
   * script names, runbook names, and command strings  
   * check and test identifiers, CI job names  
   * environment variable names when treated as already-existing  
   * fixed output locations when treated as already-existing  
   * negative existence claims (for example “X does not exist”, “not found”)  
3. No invention, no inference, no memory. A QA planning artifact MUST NOT introduce, guess, infer, paraphrase, normalize, or “fill in” any repo-resident locus string. If the exact locus string does not appear verbatim in an allowed provenance source, it MUST NOT appear as a repo-resident claim in the plan.  
4. Verbatim-only requirement. When a repo-resident locus string is used, it MUST be copied character-for-character from an allowed provenance source. No renaming, no case folding, no “equivalent” substitutions, no wildcard expansions, and no invented variants.  
5. Blocking posture (review gate). Any QA plan that contains a repo-resident locus string not proven verbatim by an allowed provenance source MUST be treated as invalid for approval and returned for revision.  
6. Non-goal. This rule governs repo-reality claims (existence and loci). It does not govern higher-level QA intent or conceptual acceptance statements that do not assert repo-resident loci.

C) Plan-created artifacts are allowed and expected, but MUST be explicit (how, why, and creation path)

1. QA plans MAY require creation of deliverable artifacts and evidence outputs. Creating logs, reports, manifests, captures, and other on-disk evidence artifacts as part of QA is normal and allowed.  
2. Repo-locus provenance lock applies ONLY to repo-resident loci. The provenance lock and repo-reality proof posture apply only to loci asserted to already exist in the repo. They do not prohibit plan-created evidence artifacts.  
3. Required creation clarity (blocking). If a QA plan requires creating a file (script, evidence file, manifest, report, deliverable, or any other on-disk artifact), it MUST include both:  
   * How: explicit, runnable creation instructions that produce the file.  
   * Why: one sentence stating the purpose (what proof obligation, deliverable posture, or required outcome it satisfies).  
4. Explicit creation path (blocking). When a plan requires creating a file, it MUST name the exact repo-relative path and filename that will be created as a plan-created output.  
5. Provenance labeling posture (non-blocking when unambiguous). The plan SHOULD label each mentioned file path as repo-resident versus plan-created. Missing labels MUST NOT be treated as an approval blocker if, and only if, the file is clearly a run-produced deliverable and the plan provides the required how and why.  
6. Prohibited ambiguity (blocking). A plan MUST NOT contain a directive like “create a helper script”, “write a manifest”, or “generate a report” without also providing both the explicit creation process and the reason it is created. Any plan that violates this requirement MUST be returned for revision.  
7. Determinism and reproducibility requirement (blocking when evidence-bearing). Creation instructions MUST be sufficient to reproduce the file deterministically and unambiguously. If the created file is used as evidence or a required deliverable, the plan MUST include enough creation detail to prevent ambiguity (including what inputs it uses and what stable structure and content it must contain).  
8. Non-goal. This addendum does not require that plan-created files be committed to the repo. It requires explicit creation instructions and a stated reason when a file is required to be created.

Drain targets (required)

* Plan Templates: add explicit QA-planning requirements that PF23 — Reality Audits MUST be consulted during QA planning and QA plan review; clarify PF23 is read-only and PO-only to update; enforce the repo-resident locus provenance lock; require how and why for any required plan-created file; require explicit creation paths for plan-created outputs; clarify provenance labeling is non-blocking when unambiguous.  
* Glow QA Guide: add a reviewer note that PF23 is a required consult input for QA planning and is read-only for QA execution; add a reviewer note that plan-created evidence artifacts are expected and allowed, and that required file creation must always include how, why, and an explicit creation path; reinforce that QA planning and reviews must not invent repo-resident loci or scripts.

## 2.17 Live QA evidence is checks-only; per-run nesting is disallowed

Timestamp: 022326  
Details:

Rule (normative)

1. Per-run nesting is disallowed.  
   Live QA Plans, QA prompts, and QA reviews MUST NOT introduce, require, or depend on any per-run directory nesting for evidence (for example, any run-id directory, timestamped run directory, or “fresh directory for this run” posture). This is not optional.  
2. Checks-only evidence layout.  
   Live QA evidence MUST be organized only by check\_id under a single epic-scoped QA root. Evidence paths MUST be stable across re-runs. Re-running QA MUST NOT change the directory structure by creating a new run root.  
3. Vetoed pattern: per-run root variables.  
   Any plan pattern that requires an operator-set per-run root (for example, “set EVIDENCE\_ROOT to a fresh directory for this run”) is vetoed and MUST NOT appear in QA plans or reviews. Plans MUST instead write to the stable, epic-scoped check directories.  
4. Deliverables are allowed, but must live under checks.  
   Plan-created deliverables are allowed. For each plan-created output, the Plan MUST name the exact repo-relative path and filename under the stable check directory and include runnable instructions that produce the file at that path (creating parent directories if needed). Plans MUST NOT place plan-created outputs under a per-run directory.  
5. Approval blocking posture.  
   Any Live QA Plan that introduces per-run nesting (or requires per-run root selection) is invalid for approval and MUST be returned for revision.

Rationale (informative)

Per-run nesting has repeatedly caused drift, confusion, and non-actionable evidence locations. Stable check-centric locations keep QA runnable, reviewable, and repeatable.

Drain targets (required)

* Plan Templates: explicitly prohibit per-run nesting and per-run root variables; define checks-only evidence layout as the required posture.  
* Glow QA Guide: add a reviewer rule that per-run nesting is disallowed and is an approval blocker; reinforce checks-only evidence organization.

## 2.18 Live QA is discovery-led; inference and over-specification are disallowed

Timestamp: 022326  
Details:

Rule (normative)

1. Discovery-first posture is mandatory.  
   Live QA Plans MUST assume that any repo detail not proven is unknown until discovered during the run. The Plan MUST prefer real-time discovery and observation over pre-specifying implementation guesses.  
2. Inference is not allowed.  
   A Live QA Plan MUST NOT infer, “fill in,” or pattern-match any repo-resident locus or app topology detail. This includes (non-exhaustive): assumed entrypoints, assumed module names, assumed route names, assumed file locations, assumed test IDs, or assumed command strings.  
3. Repo-resident loci may only be named when proven by allowed sources.  
   Any repo-resident locus string (paths, routes/endpoints, scripts, checks/test identifiers, CI job names, command strings, env var names treated as already-existing, fixed output locations treated as already-existing) MUST NOT appear in the Plan unless it is copied verbatim from an allowed provenance source as defined by the locus provenance lock.  
4. Unknown loci must be handled by a discovery step, not by placeholders.  
   When a check requires interacting with a repo-resident locus that is not proven at planning time, the Plan MUST do all of the following instead of guessing:  
   * State the discovery intent: what must be located or verified to exist.  
   * State the discovery acceptance: what constitutes sufficient proof that the locus exists and is the correct target.  
   * Require recording the discovered locus string verbatim into the check evidence (for example, in the primary log) before using it.  
   * Provide PASS and FAIL outcomes for discovery itself, including a BLOCKED posture when discovery cannot resolve ambiguity without guessing.  
5. Command-line minimalism is required.  
   Live QA Plans MUST NOT over-specify command lines. The Plan SHOULD describe:  
   * the goal of the action,  
   * the observable outputs that matter, and  
   * the evidence that must be captured.  
     The executor MUST record the exact commands actually used into the check evidence at runtime.  
     If the Plan must include an exact command string, it MUST be proven by an allowed provenance source.  
6. Script invention is disallowed; plan-created scripts are constrained.  
   Live QA Plans MUST NOT invent or assume helper scripts exist.  
   Plan-created scripts are permitted only when a required deliverable cannot be produced without one. When a Plan requires a plan-created script, it MUST:  
   * name the exact repo-relative path and filename where it will be created,  
   * include runnable creation instructions,  
   * state why the script is required, and  
   * keep the script minimal and purpose-bound to the deliverable.  
7. Vetoed patterns.  
   The following patterns are vetoed and MUST NOT appear in Live QA Plans:  
   * Conditional speculation that introduces unproven locus strings, even “as an example” or “if it exists” (for example, “if tests or scripts exist under X…”).  
   * Placeholder routes, placeholder file paths, placeholder module names, or placeholder commands used as scaffolding.  
   * Any statement that implies app topology certainty without proof (for example, “the app starts via X” unless X is proven).  
8. Blocking posture (review gate).  
   Any Live QA Plan that includes inferred or speculative repo-resident loci, speculative app topology claims, invented scripts, or over-specified unproven command lines MUST be treated as invalid for approval and returned for revision.

Clarification (normative)

* Real-time discovery evidence is valid for the run, not retroactive canon.  
  Loci discovered during execution may be used within that run if recorded as evidence, but MUST NOT be treated as planning-time proof for future Plans unless they are incorporated into an allowed provenance source (for example, an updated Reality Audit record under PO control, or explicit canon).

Scaled-down QA process requirement (normative)

* Each check in a Live QA Plan MUST be expressible as:  
  * Intent  
  * Discovery step (only if needed)  
  * Minimal test step  
  * Required evidence  
  * PASS criteria  
  * FAIL criteria  
  * BLOCKED criteria when discovery cannot proceed without guessing

Drain targets (required)

* Plan Templates: add a “discovery-first, no inference” rule; explicitly veto placeholder loci and over-specified commands; require that unknown loci are handled via recorded discovery evidence and BLOCKED posture.  
* Glow QA Guide: add a reviewer note that Live QA Plans should be discovery-led and minimal; prohibit invented scripts and over-specified command lines; require runtime recording of the actual commands used as evidence.

\<eof\>