## 1) Approval Doc — ASK OK WITH CAVEATS (for QA step incorporation)

This approval package unblocks Live QA execution by allowing the existing plan to run **as-is**, while requiring the caveats below to be **embedded into the affected QA steps/check blocks** (as additional PASS/FAIL gates and/or supplemental validations recorded in the step logs). **Do not claim PASS** for any affected check unless its caveat’s evidence trigger is satisfied; otherwise classify the check as **REMEDIATION NEEDED** (per the safe default) and proceed without guessing.
**Note:** The source review doc does not provide explicit `REV-###` IDs; the `REV-###` IDs below are assigned **in the same order as the “Mechanical Blockers” bullets** so Kronos/PO can reference them deterministically.

### Caveats list

**CAV-001**

* Source REV ID: REV-001
* Severity: Caveat
* Where it applies: Plan structure (document-level); Step-0 / planning metadata; overall plan acceptance posture
* Caveat statement: The plan is **not PF27-format compliant**; execution may proceed, but PF27-required structure gaps must be explicitly captured as run evidence and **must block any “plan is PF27-format” claim**.
* Resolution approach:

  * Owner: Kronos
  * Evidence trigger: A Step‑0/plan meta artifact under `audit/qa/hde-epic023/00_meta/` (or equivalent epic QA meta location used by the run) that explicitly maps **PF27 required sections** (front matter, scope statement, PF23 anchors trace section, PO inputs needed, evidence posture + directory structure, runbook check matrix, check blocks) to the plan’s actual sections **or marks them as missing**, and the final evidence print references that mapping.
  * Safe default until resolved: Proceed with the check bundles, but treat the run as **REMEDIATION NEEDED (structure)** at acceptance time; do **not** approve the plan as PF27-format and do not allow a “PF27 compliance” assertion in the close-out narrative.
  * Impact if unresolved: QA execution may be rejected on template compliance, forcing re-run/rework and prolonging the approval loop.

---

**CAV-002**

* Source REV ID: REV-002
* Severity: Caveat
* Where it applies: `DELIVERABLE D07` step/check block; deliverables inventory alignment
* Caveat statement: The plan’s D07 check (PF20 update note) **does not satisfy** the guide-required D07; D07 must validate the **doc‑deltas draft/staging surface** at `audit/docdeltas/hde-epic023_doc_deltas.md` with the guide-required proof fact(s).
* Resolution approach:

  * Owner: Kronos
  * Evidence trigger: A D07 validation log (either by amending the existing D07 block or adding a supplemental D07 check) that proves:

    * `audit/docdeltas/hde-epic023_doc_deltas.md` exists, is non-empty, and
    * includes a **concrete D4 note referencing PF23 consult capture as evidence-only (non-token)** (i.e., explicitly not introducing any PF23 consult token).
  * Safe default until resolved:

    * Do **not** treat `audit/qa/hde-epic023/00_meta/pf20_update.md` as a substitute for D07.
    * If `audit/docdeltas/hde-epic023_doc_deltas.md` is missing or lacks the D4 non-token note, classify D07 as **TOOLING_BLOCKED** (missing) or **FAIL_BEHAVIOR** (content/proof fact mismatch) and do not claim `DOC_DELTA_PRESENT_OK`.
  * Impact if unresolved: Token-bound doc-delta evidence cannot be trusted; acceptance will fail for the doc-delta surface intent.

---

**CAV-003**

* Source REV ID: REV-003
* Severity: Caveat
* Where it applies: `DELIVERABLE D01` step/check block; acceptance map proof posture
* Caveat statement: D01 “present + parseable JSON” is insufficient; D01 may only PASS if the acceptance map satisfies the guide’s decisive proof facts (token roster exactness + explicit exclusions + forbidden binding/string exclusions + non-empty primary-evidence bindings).
* Resolution approach:

  * Owner: Kronos
  * Evidence trigger: D01 validation evidence (in D01 `primary.log` or an explicit supplemental validation log) proves at minimum:

    * Token roster is **exactly**:
      `QA_ACCEPTANCE_MAP_VIABILITY_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `SANITY_PIPELINE_OK`, `DETERMINISM_ENV_PINS_OK`, `JSON_CANONICAL_CHECK_OK`, `DOC_DELTA_PRESENT_OK`, `TWO_RUN_IDENTITY_OK`
    * No `REALITY_AUDIT_OK` (and no other unregistered/alias tokens).
    * No evidence binding references `audit/gates/canonical/` or `artifacts/determinism/env_pins.lock`.
    * `JSON_CANONICAL_CHECK_OK` evidence is bound **only** to `audit/gates/canonical_json/*` artifacts (no `audit/gates/canonical/*` references anywhere in EPIC023 bindings).
  * Safe default until resolved: If these validations are not explicitly performed and recorded, treat D01 as **FAIL_BEHAVIOR** (even if JSON is parseable) and do not rely on D01-derived PASS for any acceptance determination.
  * Impact if unresolved: Acceptance map can incorrectly PASS while violating canonical token/binding constraints, invalidating downstream token/evidence claims.

---

**CAV-004**

* Source REV ID: REV-004
* Severity: Caveat
* Where it applies: `DELIVERABLE D08` step/check block; PF23 consult capture posture
* Caveat statement: D08 must validate required PF23 consult capture **shape**, not just “non-empty file”.
* Resolution approach:

  * Owner: Kronos
  * Evidence trigger: D08 validation evidence proves `audit/qa/hde-epic023/00_meta/pf23_consult.md` contains headings/sections that unambiguously correspond to:

    * “PF23 Anchors”
    * “what changed”
    * “what did not”
      …and does not claim/introduce `REALITY_AUDIT_OK` (consult is non-token closure evidence).
  * Safe default until resolved: If required headings/structure are not validated and recorded, classify D08 as **FAIL_BEHAVIOR** and do not treat PF23 consult capture as proven closure evidence for acceptance review.
  * Impact if unresolved: PF23 consult evidence can be “present” but non-compliant, undermining closure evidence posture.

---

**CAV-005**

* Source REV ID: REV-005
* Severity: Caveat
* Where it applies: `DELIVERABLE D09` step/check block; canonical JSON gate evidence posture
* Caveat statement: D09 must enforce the guide’s required **exact filenames**, required sibling `*.path_proof.txt` transcripts, and PASS state proof; permissive globs/parse-only checks are insufficient.
* Resolution approach:

  * Owner: Kronos
  * Evidence trigger: D09 validation evidence proves all required artifacts exist **exactly** at:

    * `audit/gates/canonical_json/json_canonical_check.log`
    * `audit/gates/canonical_json/json_canon_compare.log`
    * `audit/gates/canonical_json/canonical_json.gate.json`
      …and each has a sibling `*.path_proof.txt` transcript co-located in the same directory; additionally, `canonical_json.gate.json` indicates an unambiguous **PASS** outcome for the gate family.
  * Safe default until resolved: If any required file/path-proof is missing or PASS state is not proven, classify D09 as **FAIL_BEHAVIOR** and do not claim `JSON_CANONICAL_CHECK_OK`.
  * Impact if unresolved: Canonical JSON discipline cannot be trusted (risk of accepting a failed/partial/legacy-homed gate family).

---

**CAV-006**

* Source REV ID: REV-006
* Severity: Caveat
* Where it applies: `DELIVERABLE D10` step/check block; evidence registry surfaces posture
* Caveat statement: D10 must validate the guide-required registry surfaces and proof facts; the plan’s `audit/index/...` set is not the guide-required surface set and omits required checks.
* Resolution approach:

  * Owner: Kronos
  * Evidence trigger: D10 validation evidence proves the guide-required artifacts exist and satisfy core proof facts:

    * `docs/evidence/INDEX.json`
    * `docs/evidence/INDEX.sha256` (and it matches the hash of `INDEX.json`)
    * `artifacts/evidence_index.jsonl`
      …plus required sibling path-proof transcript(s) where required; and evidence registry coherence is demonstrated for EPIC023-governed families.
  * Safe default until resolved: If only the plan’s current `audit/index/...` set is checked, treat D10 as **FAIL_BEHAVIOR** (wrong surface set / missing required proof checks) and do not claim evidence-registry-related closure assertions for acceptance.
  * Impact if unresolved: Evidence catalog integrity and Index/Mirror coherence are not proven, invalidating acceptance confidence in governed evidence bindings.

---

**CAV-007**

* Source REV ID: REV-007
* Severity: Caveat
* Where it applies: Step‑log helper tooling; all checks producing `primary.log`
* Caveat statement: Step log header `captured_env` must include `APP_ENV`; omission is a PF19 schema conflict and invalidates step-log compliance posture.
* Resolution approach:

  * Owner: Kronos
  * Evidence trigger: At least one representative check’s `primary.log` header shows `captured_env` includes `APP_ENV` (populated from runtime environment) alongside the other required rails/pins keys, and this is consistent across checks for the run.
  * Safe default until resolved: If `APP_ENV` is missing from `captured_env`, classify affected checks as **FAIL_TOOLING** for evidence-compliance purposes (even if the underlying surface behaved correctly), and do not rely on those logs for acceptance proof until corrected evidence exists.
  * Impact if unresolved: QA evidence may be rejected at review/acceptance due to PF19 schema non-compliance.

---

## 2) PF10 Build Notes Addenda (canon issues only)

No PF10 addenda drafted.

Decision: ASK OK WITH CAVEATS
