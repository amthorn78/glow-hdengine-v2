# CRD — HDE-EPIC025 — po-002 Negative Coverage Gap

## CRD summary

This CRD records a PO‑approved development change to add explicit negative coverage for malformed and empty identifiers in the compat endpoint contract tests. The gap was discovered during Live QA step po‑002. The fix is scoped to tests only and is required for deterministic QA evidence.

**PO approval:** Approved for dev change (tests only) to satisfy QA coverage.

## Motivation

Live QA po‑002 requires explicit negative coverage for malformed and empty identifiers and deterministic client‑facing error posture. The current test suite lacks these cases, so the step cannot pass despite successful execution. This is a coverage deficiency, not a confirmed runtime defect.

## Scope

**In scope**
- Add tests for malformed and empty identifier inputs in the compat contract suite.

**Out of scope**
- Changes to runtime behavior, API contract bytes, schemas, or error token definitions.

## Proposed change

Add two tests in the compat endpoint contract suite to assert:
- Empty identifiers are rejected with a deterministic client‑facing error response.
- Malformed identifiers are rejected with a deterministic client‑facing error response.

## Files impacted

- tests/http/test_compat_endpoint_contract.py (add two negative‑case tests)

## Validation

- Re‑run `python -m pytest -q -vv tests/http/test_compat_endpoint_contract.py` and confirm pass.
- Re‑run QA step po‑002 to confirm PASS criteria are satisfied.

## Canon references (titles only)

- PF06 — Epic-Process-Guide (CRD scope and titles‑only posture)
- PF19 — Glow QA Guide (deterministic QA evidence and step‑level deliverables)

## Moon Loop eligibility

Eligible: YES

Reason:
- The fix is tests‑only and required for deterministic QA evidence.
- Adds coverage for malformed and empty identifier inputs in the compat contract suite.
- No changes to runtime behavior, API contract bytes, schemas, or error token definitions.
- Files impacted are limited to tests/http/test_compat_endpoint_contract.py.

## Canon check (proof excerpts)

PF reference: PF19 — Canon Glow QA Guide, §3.4.8

Proof excerpt:
- “Manual Live QA MUST NOT modify code or configuration except for minimal, in‑session remediation under the Moon Loop policy below. Evidence outputs MUST still be written under audit/qa/** for governed evidence.”
- “Moon Loop (allowed; minimal in‑session remediation to unblock QA). Live QA may include a small remediation loop when a check fails due to an execution‑blocking mismatch, only to the extent required to produce a PASS‑grade proof for the already‑approved scope. The only goal is to unblock the existing QA check and prove the existing implementation works.”
- “Hard boundary: no scope expansion. In‑session remediation MUST NOT:”
- “* add new features or acceptance criteria”
- “* change public contracts”

PF reference: PF06 — Canon Epic Process Guide, §0.5

Proof excerpt:
- “Live QA Moon Loop: minimal in‑session remediation is allowed to unblock QA”
- “Live QA may include a small remediation loop when a check fails due to a small, execution‑blocking issue (wrong predicate target, missing guard, etc.) and the smallest correction is required to produce a PASS‑grade proof for the already‑approved epic scope.”
- “Hard boundary: no scope expansion. In‑session remediation MUST NOT:”
- “* add new features or acceptance criteria”
- “* introduce new evidence families”

## Findings

FIN-001 | Severity: Caveat

CRD quote (verbatim):
“The fix is scoped to tests only and is required for deterministic QA evidence.”

Why it matters:
This is Moon Loop‑eligible (tests‑only) and does not modify production behavior or contracts. It aligns with the Moon Loop boundary rules in canon.

Required change:
- Ensure implementation touches only the listed test file and does not modify runtime code paths.

Canon reference: PF19 — Canon Glow QA Guide, §3.4.8

Canon proof excerpt:
- “Hard boundary: no scope expansion. In‑session remediation MUST NOT:”
- “* add new features or acceptance criteria”
- “* change public contracts”

FIN-002 | Severity: Caveat

CRD quote (verbatim):
“Add two tests in the compat endpoint contract suite to assert:”
“- Empty identifiers are rejected with a deterministic client‑facing error response.”
“- Malformed identifiers are rejected with a deterministic client‑facing error response.”

Why it matters:
The CRD is correct in intent, but “deterministic client‑facing error response” must be implemented without defining new contract bytes or acceptance criteria beyond the approved QA requirement.

Required change:
- Keep assertions limited to deterministic client‑facing error posture for empty/malformed identifiers, without introducing new public contract requirements not already implied by the existing QA proof obligation.

Canon reference: PF06 — Canon Epic Process Guide, §0.5

Canon proof excerpt:
- “Hard boundary: no scope expansion. In‑session remediation MUST NOT:”
- “* add new features or acceptance criteria”
- “* introduce new evidence families”

FIN-003 | Severity: Nit

CRD quote (verbatim):
“Lead Dev / Thoth: Pending per standard CRD routing”

Why it matters:
This is clear as status, but does not specify whether the Moon Loop change is applied immediately during Live QA or queued for dev routing. Clarity reduces execution friction.

Required change:
- Add one line specifying that this is approved for immediate QA‑time implementation as a Moon Loop tests‑only change (or explicitly state it will be queued for dev routing instead).

## Risk

Low. Test‑only change; no production code or contract bytes are altered.

## Approval

- **PO:** Approved (dev change authorized)
- **Lead Dev / Thoth:** Pending per standard CRD routing
