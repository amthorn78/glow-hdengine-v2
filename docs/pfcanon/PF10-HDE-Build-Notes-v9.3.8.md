# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v9.3.8  
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

1. 2.1 Acceptance token registry authority \+ legacy spellings \+ unregistered tokens (TI-001, TI-002)  
2. 2.2 Evidence path binding authority order \+ Machine Evidence Index mirror home \+ path-proof naming (TI-003, ADR-001)  
3. 2.3 Acceptance map path-of-record (global) (TI-004)  
4. 2.4 Evidence Index snapshot (D23) mechanical PASS/FAIL contract (TI-005, ADR-003)  
5. 2.5 \- Ellipsis Prohibition in Canonical Docs and Plans  
6. 2.6 \- PR01 HDE-EPIC024 Review  
7. 2.7 \- PR02 HDE-EPIC024 Review  
8. 2.8 \- PR03 HDE-EPIC024 Review  
9. 2.9 \- PR04 HDE-EPIC024 Review

# 2\) Number Addenda

---

## **2.1 \- Acceptance token registry authority \+ legacy spellings \+ unregistered tokens (TI-001, TI-002)**

Timestamp: 011426 13:28 UTC  
Details:

* **Rule (token authority; hard):** Acceptance tokens used in *acceptance artifacts* (acceptance maps, token↔evidence matrices, close-pack manifests, and any acceptance-token claims in step logs) **MUST** use the **canonical token names** from **HDE-Governance, §2.0 Acceptance Tokens (single-home roster)**. Token strings are **case-sensitive** and **aliases/legacy spellings MUST NOT appear** in acceptance artifacts.  
* **Rule (unregistered tokens; hard):** Any token string **not present** in the HDE-Governance acceptance token roster is **not registry-valid** and **MUST NOT** be claimed in acceptance artifacts. Treat any such occurrence in consumer docs as **doc drift** until drained.  
* **Resolution (TI-002; explicit):** The string **`QA_STEP_LOGS_CONSOLIDATED_OK`** is referenced in canon consumers (notably in the checklist/QA docs) but is **not** present in the HDE-Governance acceptance token roster.  
  * **Effective immediately:** `QA_STEP_LOGS_CONSOLIDATED_OK` is treated as a **deprecated doc-only alias** for **`QA_HARNESS_DISCIPLINE_OK`** (the registry-valid token in **HDE-Governance, §2.0 Acceptance Tokens (single-home roster)**).  
  * **Acceptance artifacts MUST claim:** `QA_HARNESS_DISCIPLINE_OK` (not `QA_STEP_LOGS_CONSOLIDATED_OK`).  
  * **Consumer-doc interpretation (temporary until drains complete):** When `QA_STEP_LOGS_CONSOLIDATED_OK` appears in PF text, interpret it as referring to `QA_HARNESS_DISCIPLINE_OK` and do not mint/claim a new token.  
* **Epic doc-delta handling (supports TI-001):** If any PF consumer doc contains legacy spellings for a token family, the epic must **normalize to the registry name** and record the normalization as a **doc delta** (per **HDE-Governance, §9.7 Document deltas**), rather than propagating the legacy spelling into acceptance artifacts.

Drain targets (required):

* **HDE-Build Checklist:** Replace `QA_STEP_LOGS_CONSOLIDATED_OK` references with `QA_HARNESS_DISCIPLINE_OK` in the QA harness discipline subtask (**HDE-Build Checklist, §HDE-CALC003.14 — QA harness discipline (step logs \+ manifest) — skeleton**).  
* **Glow QA Guide:** Replace `QA_STEP_LOGS_CONSOLIDATED_OK` references with `QA_HARNESS_DISCIPLINE_OK` in token naming/glossary sections and any acceptance-token examples (**Glow QA Guide, §9.2.1 Acceptance token authority** and related token glossary sections).  
* **HDE-Governance:** No new token is introduced by this addendum; confirm `QA_HARNESS_DISCIPLINE_OK` remains the sole canonical token for this posture (**HDE-Governance, §2.0 Acceptance Tokens (single-home roster)**).  
* **Doc deltas:** Any epic encountering legacy spellings must capture the canonical spelling used (and any known aliases being treated as doc drift) via the governed doc-delta mechanism (**HDE-Governance, §9.7 Document deltas**).

---

## **2.2 \- Evidence path binding authority order \+ Machine Evidence Index mirror home \+ path-proof naming (TI-003, ADR-001)**

Timestamp: 011426 13:28 UTC  
Details:

* **Rule (authority order; explicit):**  
  * **HDE Schemas and Artifacts** is the **source of truth** for **canonical artifact paths** and **sibling path-proof transcript naming** for governed evidence families.  
  * **HDE-Mechanics Guide** defines mechanics and coupling posture, but **must not introduce alternate canonical paths** that conflict with HDE Schemas and Artifacts.  
  * **Glow QA Guide** defines **check execution semantics** and **status vocabulary** for validators.  
  * **HDE-Build Checklist** defines which checks/gates are required, but those checks must bind to the canonical surfaces above.  
* **Rule (Machine Evidence Index mirror home; hard):** The **single canonical** Machine Evidence Index mirror file is:  
  * `artifacts/evidence_index.jsonl`  
    with companion:  
  * `artifacts/evidence_index.jsonl.sha256`  
    and sibling path-proof transcript:  
  * `artifacts/evidence_index.jsonl.path_proof.txt`  
    per **HDE Schemas and Artifacts, §8.3 Machine Evidence Index — JSONL mirror (records-only)**.  
    Any other mirror path strings (including `artifacts/evidence/machine_mirror.json` or any `docs/evidence/...machine_mirror...` variants) are **non-canonical** and must be treated as **doc drift** until drained.  
* **Rule (path-proof transcript suffix; hard):** The canonical sibling path-proof transcript naming is:  
  * `<artifact>.path_proof.txt`  
    per **HDE Schemas and Artifacts, §8.3.3 Path-proof transcript schema** and the governed artifact catalog rule that governed artifacts have sibling `<artifact>.path_proof.txt`.  
    Any mention of `.path_proof.json` is **non-canonical** and overridden by this addendum.  
* **Rule (validator failure posture for binding mismatches; hard):**  
  * If the validator **can run** and detects that evidence exists but **bindings do not match canonical paths / canonical proof naming**, the status is **FAIL\_BEHAVIOR**.  
  * If the validator **cannot evaluate** because required canonical inputs are missing, the status is **TOOLING\_BLOCKED**.  
    Status vocabulary is per **Glow QA Guide, §4.4.10 Status vocabulary**.  
* **Explicit resolution of ADR-001:** This addendum **closes ADR-001** by:  
  * Canonizing the authority order above,  
  * Canonizing the Machine Evidence Index mirror home and path-proof naming, and  
  * Canonizing the validator failure posture when bindings mismatch.

Drain targets (required):

* **HDE Schemas and Artifacts:** Remove/repair any internal conflicting references that mention `artifacts/evidence/machine_mirror.json` and/or `.path_proof.json`, and unify on `artifacts/evidence_index.jsonl` \+ `<artifact>.path_proof.txt` (**HDE Schemas and Artifacts, §8.3 Machine Evidence Index — JSONL mirror (records-only)**; **§8.3.3 Path-proof transcript schema**).  
* **HDE-Mechanics Guide:** Tighten any “path\_proof.txt (or equivalent)” language so canonical naming is unambiguous for governed artifacts (align to **HDE Schemas and Artifacts, §8.3.3 Path-proof transcript schema**).  
* **Glow QA Guide:** Ensure binding mismatch vs missing-input status guidance is explicit (align to **Glow QA Guide, §4.4.10 Status vocabulary**).  
* **HDE-Build Checklist:** Ensure any preflight/binding validation language binds strictly to the canonical mirror home \+ `.path_proof.txt` suffix (align to **HDE Schemas and Artifacts, §8.3** and **Glow QA Guide, §4.4.10**).

---

## **2.3 \- Acceptance map path-of-record (global) (TI-004)**

Timestamp: 011426 13:28 UTC  
Details:

* **Rule (acceptance map path-of-record; hard):** When an epic produces (or is required to produce) an acceptance map, the canonical path binding is:  
  * `docs/acceptance_map_epic<NNN>.json`  
    with sibling path-proof:  
  * `docs/acceptance_map_epic<NNN>.json.path_proof.txt`  
    per **Glow Infrastructure, §Epic acceptance-ledger artifacts (canonical paths; names-only)**.  
* **EPIC024 binding (explicit):** If EPIC024 produces an acceptance map, it is bound to:  
  * `docs/acceptance_map_epic024.json`  
  * `docs/acceptance_map_epic024.json.path_proof.txt`  
* **Scope note:** This addendum resolves TI-004 by confirming the global rule already present in canon infra and making EPIC024’s binding explicit for planning/tooling expectations.

Drain targets (if needed for consistency):

* **Plan Templates / Governance / QA docs:** If any plan/template text implies acceptance-map naming is merely “pattern” or “prior epic convention,” update it to reference the canonical binding in **Glow Infrastructure, §Epic acceptance-ledger artifacts (canonical paths; names-only)**.

---

## **2.4 \- Evidence Index snapshot (D23) mechanical PASS/FAIL contract (TI-005, ADR-003)**

Timestamp: 011426 13:28 UTC  
Details:

* **Context (existing canon):** The Evidence Index snapshot governed artifact paths exist, but the check is treated as posture-only in places. This addendum **activates a mechanical PASS/FAIL contract** suitable for QA closure proof **without introducing a new acceptance token**, resolving TI-005 and ADR-003.  
* **Canonical artifact surfaces (already governed):**  
  * Snapshot JSON: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
  * Snapshot path proof: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`  
    per **HDE Schemas and Artifacts, §2.11 Evidence Index Snapshot — canonical paths (D23)**.  
* **Snapshot schema (now canonical; minimal required fields):** `evidence_index_snapshot.json` MUST be a canonical JSON object with:  
  * `schema_version` (string; initial value `"1"`)  
  * `generated_at_utc` (string; RFC3339 UTC timestamp)  
  * `inputs` (object) with:  
    * `human_index_path` (string; MUST equal `docs/evidence/INDEX.json`)  
    * `human_index_sha256` (string; 64 lowercase hex)  
    * `machine_mirror_path` (string; MUST equal `artifacts/evidence_index.jsonl`)  
    * `machine_mirror_sha256` (string; 64 lowercase hex)  
  * `parity` (object) with:  
    * `artifact_keys_match` (boolean; whether the set of artifact\_keys in the human index matches the set in the machine mirror)  
* **Mechanical PASS/FAIL predicate (now canonical):**  
  * PASS iff all are true:  
    * Snapshot JSON exists at the governed path and conforms to the schema above.  
    * `inputs.human_index_path` is exactly `docs/evidence/INDEX.json` and `inputs.machine_mirror_path` is exactly `artifacts/evidence_index.jsonl`.  
    * `human_index_sha256` matches the computed sha256 of `docs/evidence/INDEX.json`, and `machine_mirror_sha256` matches the computed sha256 of `artifacts/evidence_index.jsonl`.  
    * `parity.artifact_keys_match` is true (artifact\_key set parity between `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`).  
    * The snapshot path-proof transcript exists and matches the snapshot file, per **HDE Schemas and Artifacts, §8.3.3 Path-proof transcript schema**.  
  * **Status mapping (must follow Glow QA vocabulary):**  
    * Missing required inputs/snapshot artifacts ⇒ **TOOLING\_BLOCKED**  
    * Predicate evaluated and any check fails ⇒ **FAIL\_BEHAVIOR**  
    * All checks pass ⇒ **PASS**  
      per **Glow QA Guide, §4.4.10 Status vocabulary**.  
* **Token posture (hard):** This check MUST remain **tokenless**: no new acceptance token is introduced, and passing this check MUST NOT be represented as an acceptance token claim. (It may still be used as closure-proof evidence.)

Drain targets (required):

* **HDE Schemas and Artifacts:** Add/extend the snapshot JSON schema requirements (fields \+ meanings) under the Evidence Index Snapshot section (**HDE Schemas and Artifacts, §2.11 Evidence Index Snapshot — canonical paths (D23)**).  
* **Glow QA Guide:** Update the D23 check definition from “posture-only” to the mechanical PASS/FAIL contract above, including status mapping (**Glow QA Guide, §4.4.10 Status vocabulary**; and the D23 check description section).  
* **HDE-Build Checklist:** Update the D23 tooling gap note to reflect that validation predicates are now canonized, and align any “posture-only” language accordingly (**HDE-Build Checklist, §HDE-CALC003.19 — Evidence Index snapshot (D23) (TOOLING\_BLOCKED)**).

## 2.5 \- Ellipsis Prohibition in Canonical Docs and Plans

**Rule (hard):** Canonical documents and plans MUST NOT contain the ASCII triple-dot sequence or the Unicode ellipsis character.

**Rationale:** Ellipsis characters are ambiguous with truncation and excerpt artifacts in review tooling. Canonical docs must be unambiguous, copy-stable, and review-safe.

**Scope:** Applies to all canonical documentation and plan records governed under the doc system (including templates in Canon Plan Templates). This rule supersedes any older guidance that used ellipses for placeholders, continuation, abbreviated paths, or omitted blocks.

**Allowed replacement markers (standard placeholders):**

* `[OMITTED]`

* `[OMITTED: <short reason>]`

* `[SNIP: <n> lines omitted]`

* `[REPEAT BLOCK]`

* `[LIST CONTINUES]`

* `<PLACEHOLDER_NAME>` for values (use `<REPO_ROOT>` and similar instead of abbreviated paths)

**Review handling:**

* If ellipsis characters appear in a review view, reviewers MUST treat them as suspicious for truncation first.

* If the characters can be proven to exist in the source document (not a view truncation artifact), they MUST be removed and replaced using the allowed replacement markers above.

* If the characters cannot be proven in the source, the review is a read failure and MUST be retried until the full source is visible.

**Drain targets (permanent canon homes):**

* Technical Writing Best Practices: document hygiene rule and approved placeholders

* Canon Plan Templates: template-safe placeholders and ban statement

* HDE Governance: reviewer enforcement posture for canonical docs and plan records (no token changes)

**Non-goal:** This addendum does not change any runtime contract, schemas, or evidence artifact byte rules. It is strictly documentation hygiene for canon and plans.

---

Artifact Map

Implementation Doc: r2 Implementation Plan HDE-EPIC024.md  
Original PR Bundle: PR01 HDE-EPIC024.md  
Remedial PR Bundle: r1 PR01 HDE-EPIC024.md  
Extra Evidence Bundle: EXTRA\_EVIDENCE\_BUNDLE\_OR\_NONE (None provided)

## 2.6 \- PR01 HDE-EPIC024 Review

* The Original PR’s dev-step intent was to implement the PR-01 scope: canonical JSON gate artifacts under `audit/gates/json_gate/canonical/` with sibling `.path_proof.txt` files, validated by the gate runner.  
* The Original PR shows gate validation (`python tools/evidence/run_canonical_json_gate.py (exit 0)`) and enumerates the required canonical files as present and non-empty.  
* The Original PR’s verification posture was incomplete for merge readiness because it did not include the evidence-suite pytest run that later appears as the targeted remediation check.  
* The Remedial PR’s change is narrowly targeted: it updates `tests/evidence/test_sanity_pipeline.py` to expect the emitted header prefix `run:sanity-pipeline`, and it runs the previously failing evidence-suite command, reporting all tests passing.  
* The Remedial PR still includes the PR-01 deliverables (canonical gate artifacts \+ path proofs) and includes a structured gate record with `status:"pass"` and pinned env pins.  
* Combined outcome aligns with the Implementation Doc’s PR-01 acceptance gate: required files exist under `audit/gates/json_gate/canonical/`, closed-rails posture is evidenced, and the basic PR-01 gate runner is shown as passing in the Original PR bundle.  
* Tests/evidence posture is sufficient for merge confidence at PR-01 scope: the Remedial PR explicitly runs `python -m pytest tests/evidence tests/ops/test_evidence_index.py` with a passing summary.  
* Notable remaining risk: the Remedial PR itself flags a broader canon conflict about sanity log markers as “Follow-up (out of scope)” (no further work is required for PR-01 acceptance).

### Findings

1. **PR-01 acceptance scope is “canonical JSON gate artifacts at `audit/gates/json_gate/canonical/` \+ `.path_proof.txt` siblings,” validated by the gate runner under closed rails.**  
   * Observed (Implementation Doc): PR-01 intent and acceptance checks are explicit (canonical paths \+ closed rails \+ basic QA command and pass condition).  
   * Why it matters: This defines the exact “merge-ready” bar for PR-01; anything beyond it is either incidental or belongs to later PRs.  
2. **Original PR delivered the canonical gate artifacts and demonstrated the gate runner passing (exit 0\) with required files enumerated as non-empty.**  
   * Observed (Original PR): “✅ python tools/evidence/run\_canonical\_json\_gate.py (exit 0)” and the list of the six required canonical files under `audit/gates/json_gate/canonical/`.  
   * Why it matters: This is direct evidence that the core PR-01 deliverable (canonical home \+ outputs \+ proofs) was implemented and demonstrably runnable.  
3. **Remedial PR adds merge-readiness verification by running the evidence-suite pytest command and showing a clean pass.**  
   * Observed (Remedial PR): “✅ python \-m pytest tests/evidence tests/ops/test\_evidence\_index.py” and “20 passed in 0.77s”.  
   * Why it matters: This closes the original “CI can be green and still wrong” concern by showing the targeted verification command passing at the repo level, not only in CI.  
4. **Remedial PR change is surgical and evidence-backed: it updates the test header expectation to `run:sanity-pipeline` and shows the updated line via numbered proof.**  
   * Observed (Remedial PR): `assert log_text.startswith("run:sanity-pipeline\n")` shown with line numbers.  
   * Why it matters: Confirms the remediation is exactly what it claims and is limited to the test surface required to unblock CI/verification.  
5. **Remedial PR still contains the PR-01 gate deliverables (canonical files) and a structured record indicating a passing gate result with closed-rails env pins.**  
   * Observed (Remedial PR): the file list includes the three required artifacts and their `.path_proof.txt` siblings under `audit/gates/json_gate/canonical/`.  
   * Observed (Remedial PR): structured record includes `env` pins and `status:"pass"`; path proof excerpt shows sha/size/mtime/produced fields present.  
   * Why it matters: Demonstrates the merged result is not only “tests pass,” but also includes the governed artifacts the Implementation Doc expects.  
6. **Legacy catalog check report preservation is explicitly documented as preserved while adopting the canonical `json_gate` family for gate artifacts.**  
   * Observed (Remedial PR): documentation line states the gate writes to `audit/gates/json_gate/canonical/...` and “The legacy catalog check report remains at `audit/gates/canonical_json/json_canonical_check.log`.”  
   * Why it matters: Prevents contract drift for any existing consumers that still reference the legacy catalog check report path while ensuring new plans bind to the canonical family.

### Requirement Satisfaction Crosswalk (Original step → Remediated satisfaction)

| Requirement label (Implementation Doc) | Original PR status | Evidence pointer(s) in Original PR | Remedial PR change that addresses it | Current status after remediation | Evidence pointer(s) in Remedial PR | Notes |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Canonical artifacts live under `audit/gates/json_gate/canonical/` with sibling `.path_proof.txt` files | Satisfied | “Required Canonical Files… non-empty” list \+ gate runner exit 0\. | None required (kept) | Satisfied | File list includes all six required files. |  |
| Acceptance tokens listed for PR-01 are addressed by evidence | Satisfied | Gate runner exit 0 \+ required files non-empty. | None required (kept) | Satisfied | Structured record shows `status:"pass"` and env pins; path proof fields present. | Token names are not re-printed in PR bundles; evidence aligns with the Implementation Doc’s pass condition. |
| Closed-rails posture (no network; pinned env) | Satisfied | Gate artifacts include env pins (see structured record excerpt in Remedial PR); PR-01 rails posture is defined in Implementation Doc. | None required (kept) | Satisfied | `env` shows `ALLOW_NETWORK:"0"`, `SAFE_MODE:"1"`, `LC_ALL:"C"`, `LANG:"C"`, `TZ:"UTC"`. |  |
| Basic QA command and pass condition | Satisfied | “✅ python tools/evidence/run\_canonical\_json\_gate.py (exit 0)” \+ required files list. | Adds targeted pytest run for merge readiness | Satisfied | “✅ python \-m pytest …” and “20 passed …”. | Gate-run evidence is shown in Original PR; Remedial adds the missing verification run. |
| Internal reference/doc pointers reflect canonical home without requiring legacy home | Satisfied | Original PR updated docs files (listed as changed). | Clarifies canonical vs legacy locations in docs | Satisfied | Doc line explicitly states canonical outputs \+ legacy report retention. |  |
| CI/verification failure resolved for mergeability | Not satisfied | Original PR shows only gate runner testing; no evidence-suite pytest run present. | Updates sanity pipeline test expectation and runs pytest | Satisfied | Test file shows updated assertion; pytest summary is all-pass. |  |

### Evidence Print (PASS PROOF; required; whole PR)

#### A) Acceptance coverage evidence (Implementation Doc)

1. **Requirement:** Canonical artifacts exist under `audit/gates/json_gate/canonical/` with `.path_proof.txt` siblings; validated by proof command.  
   * Evidence (Original PR): gate runner exit 0 and required canonical files enumerated.  
   * Evidence (Remedial PR): file list includes all six required outputs under `audit/gates/json_gate/canonical/`.  
   * Key proof facts (verbatim):  
     * “✅ python tools/evidence/run\_canonical\_json\_gate.py (exit 0)”  
     * “audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json.path\_proof.txt” (present as a new file)  
2. **Requirement:** Closed rails posture for PR-01 (no network).  
   * Evidence (Remedial PR): structured record includes env pins and shows `ALLOW_NETWORK:"0"`, `SAFE_MODE:"1"`.  
   * Key proof fact (verbatim): `"env":{"ALLOW_NETWORK":"0","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"}`  
3. **Requirement:** Basic QA pass condition and acceptance tokens list for PR-01.  
   * Acceptance tokens named (Implementation Doc): `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_PATH_PROOFS_OK`.  
   * Proof posture (Implementation Doc): run the gate runner; pass if exit 0 and six files exist and are non-empty.  
   * Evidence (Original PR \+ Remedial PR): gate exit 0 is shown in Original PR; file presence is shown in Remedial PR.

#### B) Evidence/verification posture now satisfied (Original step closure)

* **Original missing/thin item:** evidence-suite pytest run used for merge-readiness (not shown in Original PR).  
  * **Now satisfied:** Remedial PR runs `python -m pytest tests/evidence tests/ops/test_evidence_index.py` and reports “20 passed”.  
  * Key proof fact (verbatim): “============================== 20 passed in 0.77s \==============================”

#### C) Token and gate evidence (names-only; do not invent)

Tokens/gates explicitly required by the Implementation Doc for PR-01:

* `JSON_CANONICAL_CHECK_OK`  
  * Status: **Proven**  
  * Evidence pointers: gate runner exit 0 \+ structured record `status:"pass"`.  
* `EVIDENCE_PATH_PROOFS_OK`  
  * Status: **Proven**  
  * Evidence pointers: `.path_proof.txt` files are present for each required artifact under the canonical family.

#### D) Test/CI proof

* Job/test: `python -m pytest tests/evidence tests/ops/test_evidence_index.py`  
  * Pass indicator: “20 passed in 0.77s”  
  * Evidence pointer: Remedial PR “Testing” \+ “Pytest Summary”.

#### E) Artifact/evidence outputs

Implementation Doc expected evidence artifacts for PR-01:

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
  * Type: log (ndjson)  
  * Proof facts: file is listed as “New” under the canonical path.  
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`  
  * Type: text (path proof)  
  * Proof facts: file is listed as “New”.  
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`  
  * Type: log (ndjson)  
  * Proof facts: file is listed as “New”.  
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`  
  * Type: text (path proof)  
  * Proof facts: file is listed as “New”.  
* `audit/gates/json_gate/canonical/json_gate_structured_record.json`  
  * Type: json  
  * Proof facts: structured record includes `status:"pass"` and the env pins.  
* `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`  
  * Type: text (path proof)  
  * Proof facts: includes `sha256` and timestamps.  
  * sha256 (verbatim): `be0d6ff9cc5d9a77c3a4b124abeba04248efbde3896586e3263fc9305343b773`

Additional supporting artifact:

* Documentation clarifies canonical vs legacy locations for the canonical JSON gate artifacts and the legacy catalog check report.

### Doc Deltas (PF-Canon only; REQUIRED)

Doc: PF14 — HDE-Mechanics Guide  
Section: §27.5 “Sanity pipeline (release & provenance) \[Required-Now\]”  
Delta: NEW CANON PROPOSAL — Reconcile sanity log predicate markers across PF-Canon: clarify whether `artifacts/sanity/sanity.log` MUST include `run:sanity-pipeline` and `env_pins:` marker lines, and what the required first-line header is, so PF14 does not contradict PF19/PF09 on validator posture.  
Why: The Remedial PR explicitly flags an unresolved PF-Canon conflict and aligns tests to the currently emitted output, so leaving contradictory canon will cause recurring drift in validators/tests.  
Evidence pointer: Remedial PR — “Follow-up (out of scope)”: “There is a canon conflict between PF14 vs PF19 about sanity log marker requirements; this PR only aligns the test to current emitted output.”

Doc: PF19 — Glow QA Guide  
Section: §3.4.1 “Execution pattern: one command → one primary artifact”  
Delta: NEW CANON PROPOSAL — Update D18 sanity validator posture to match the reconciled PF-Canon rule for `artifacts/sanity/sanity.log` (header/marker expectations), so it no longer conflicts with PF14 §27.5 and the repo’s current emitted output.  
Why: The Remedial PR indicates tests are now aligned to the emitted header prefix `run:sanity-pipeline`, which conflicts with PF-Canon guidance that currently disagrees internally.  
Evidence pointer: Remedial PR — Summary: “Updated the sanity pipeline test to expect the emitted header prefix run:sanity-pipeline.”

Doc: PF09 — HDE-Build Checklist  
Section: “Subtask HDE-CALC003.1 — Closed-rails sanity pipeline (ordered)”  
Delta: NEW CANON PROPOSAL — Update the “Sanity log artifact” / “Validator posture (D18 canonical surface; no marker lines)” text to match the reconciled PF-Canon rule for sanity log header/marker lines (so Build Checklist validator posture does not contradict the repo’s current emitted output and PF14).  
Why: The Remedial PR aligns tests to the current emitted sanity log header prefix; checklist validator posture must not remain contradictory if it is used as an acceptance reference.  
Evidence pointer: Remedial PR — Diff excerpt (tests/evidence/test\_sanity\_pipeline.py): `assert log_text.startswith("run:sanity-pipeline\n")`

Doc: PF19 — Glow QA Guide  
Section: §3.4.1 “Execution pattern: one command → one primary artifact”  
Delta: Update D19/D20 canonical JSON gate predicate targets to include the PF12 canonical json\_gate family outputs (`audit/gates/json_gate/canonical/json_gate_check_log.ndjson` and `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, plus their `.path_proof.txt` siblings) as the canonical gate-family predicate surfaces for new remediations, and clarify that `audit/gates/canonical_json/json_canonical_check.log` is a legacy catalog check report location.  
Why: The PR introduces and documents the canonical `audit/gates/json_gate/canonical/` gate-family outputs while explicitly calling out the legacy report location, so PF-Canon QA predicate targets should reflect canonical paths-of-record to prevent plans binding to legacy paths.  
Evidence pointer: Remedial PR — Diff: docs/CLI\_commands.md → “\#\# Evidence discipline” (Canonical JSON gate bullets): “writes `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, and `audit/gates/json_gate/canonical/json_gate_structured_record.json` … The legacy catalog check report remains at `audit/gates/canonical_json/json_canonical_check.log`.”

## 2.7 \- PR02 HDE-EPIC024 Review

* The Original PR attempted to deliver PR-02 by adding a generator, a governed report artifact, and a focused test for arrays-as-sets proof on a registry surface.  
  Evidence pointer: Original PR — “Files (3)” —  
  “artifacts/canonical/arrays\_as\_sets\_report.log”  
  “tests/compare/test\_arrays\_as\_sets.py”  
  “tools/evidence/generate\_arrays\_as\_sets\_report.py”  
* The Original PR satisfied the basic proof posture (generator run \+ pytest run) and produced a report that includes explicit registry coverage markers and before/after normalization lines.  
  Evidence pointer: Original PR — Logs —  
  “LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/generate\_arrays\_as\_sets\_report.py”  
  “surface: registry.catalog.channels\_v1”  
  “============================== 1 passed in 0.04s \===============================”  
* Code review found a bug: the Original PR’s generator/test logic hard-failed if it could not find an “unsorted” case, meaning evidence refresh could fail after routine catalog normalization.  
  Evidence pointer: Original PR — Diff (tests/compare/test\_arrays\_as\_sets.py) —  
  `raise AssertionError(f"no unsorted {field} array found in channels_v1.json")`  
* The Remedial PR changed the generator and test to support deterministic fallback case selection (when `raw == normalized`) and to optionally emit/assert a note line instead of failing.  
  Evidence pointer: Remedial PR — Summary —  
  “Made arrays-as-sets report generation resilient by falling back to deterministic, already-canonical cases…”  
  Evidence pointer: Remedial PR — Diff (tools/evidence/generate\_arrays\_as\_sets\_report.py) —  
  `lines.append("note: raw == normalized (already canonical)")`  
* The remediation now satisfies the Original PR’s intended evidence/verification posture by removing the brittle assumption while keeping the same proof command and report artifact path.  
  Evidence pointer: Remedial PR — Testing —  
  “✅ LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/generate\_arrays\_as\_sets\_report.py”  
  “✅ python \-m pytest tests/compare/test\_arrays\_as\_sets.py (summary: 1 passed in 0.05s)”  
* The combined outcome aligns with the Implementation Doc’s PR-02 scope and proof-command anchor (arrays-as-sets proof via pytest proving the report is produced/covered).  
  Evidence pointer: Implementation Doc — Execution plan —  
  “2. **PR-02** — Arrays-as-sets evidence for registry/topology \+ governed report/log proof”  
  Evidence pointer: Implementation Doc — PR-04 step-log command list (arrays-as-sets proof anchor) —  
  “Arrays-as-sets proof (`python -m pytest tests/compare/test_arrays_as_sets.py` → proves `artifacts/canonical/arrays_as_sets_report.log` is produced/covered)”  
* Remaining risk is low and primarily about future data normalization: the remedial fallback path adds a report note line when needed, and the test explicitly tolerates that case.  
  Evidence pointer: Remedial PR — Diff (tests/compare/test\_arrays\_as\_sets.py) —  
  `if centers_fallback or domains_fallback:`  
  `assert "note: raw == normalized (already canonical)" in report_text`

### Findings

1. **PR-02 scope is explicitly defined in the Implementation Doc as arrays-as-sets evidence for registry/topology with governed report/log proof.**  
   * Observed (Implementation Doc): Execution plan PR-02 label.  
     Evidence pointer: Implementation Doc — Execution plan —  
     “2. **PR-02** — Arrays-as-sets evidence for registry/topology \+ governed report/log proof”  
   * Why it matters: Confirms this PR is not about new product features; it’s about deterministic evidence/proof.  
2. **Implementation Doc names the proof command and the report artifact path that must be proven/covered.**  
   * Observed (Implementation Doc): Arrays-as-sets proof anchor and path-of-proof.  
     Evidence pointer: Implementation Doc — PR-04 step-log command list —  
     “Arrays-as-sets proof (`python -m pytest tests/compare/test_arrays_as_sets.py` → proves `artifacts/canonical/arrays_as_sets_report.log` is produced/covered)”  
   * Why it matters: This is the concrete acceptance/proof bar we can verify from PR artifacts.  
3. **Original PR produced the report artifact with explicit registry coverage and before/after normalization evidence, and it ran the arrays-as-sets pytest proof command successfully.**  
   * Observed (Original PR): report excerpt and pytest summary.  
     Evidence pointer: Original PR — Logs —  
     “arrays-as-sets report v1”  
     “surface: registry.catalog.channels\_v1”  
     “============================== 1 passed in 0.04s \===============================”  
   * Why it matters: Confirms the original development step hit the primary artifact \+ proof command.  
4. **Original PR contained a brittle selection assumption that could break evidence regeneration and tests after routine data cleanup.**  
   * Observed (Original PR): hard-fail when no unsorted case exists.  
     Evidence pointer: Original PR — Diff (tests/compare/test\_arrays\_as\_sets.py) —  
     `raise AssertionError(f"no unsorted {field} array found in channels_v1.json")`  
   * Why it matters: CI can be green and still wrong; this is a correctness/stability risk for future evidence refresh.  
5. **Remedial PR implements deterministic fallback selection and makes the report/test explicitly handle the already-canonical scenario.**  
   * Observed (Remedial PR): generator emits an explicit note when fallback occurs.  
     Evidence pointer: Remedial PR — Diff (tools/evidence/generate\_arrays\_as\_sets\_report.py) —  
     `if fallback:`  
     `lines.append("note: raw == normalized (already canonical)")`  
   * Observed (Remedial PR): test asserts that note line only when fallback is used.  
     Evidence pointer: Remedial PR — Diff (tests/compare/test\_arrays\_as\_sets.py) —  
     `if centers_fallback or domains_fallback:`  
     `assert "note: raw == normalized (already canonical)" in report_text`  
   * Why it matters: Removes the brittle assumption while preserving deterministic output and auditability.  
6. **Remedial PR includes concrete verification runs for both generator regeneration and the pytest proof command.**  
   * Observed (Remedial PR): test and generator commands \+ pass indicators.  
     Evidence pointer: Remedial PR — Testing —  
     “✅ LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/generate\_arrays\_as\_sets\_report.py”  
     “✅ python \-m pytest tests/compare/test\_arrays\_as\_sets.py (summary: 1 passed in 0.05s)”  
   * Why it matters: Shows the remediation is verified under closed rails and does not rely solely on CI.

### Requirement Satisfaction Crosswalk (Original step → Remediated satisfaction)

| Requirement label (Implementation Doc) | Original PR status | Evidence pointer(s) in Original PR | Remedial PR change that addresses it | Current status after remediation | Evidence pointer(s) in Remedial PR | Notes |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| PR-02 — Arrays-as-sets evidence for registry/topology \+ governed report/log proof | Satisfied (but brittle) | Original PR — Logs — “surface: registry.catalog.channels\_v1” and “1 passed in 0.04s” | Adds deterministic fallback \+ explicit note on already-canonical cases | Satisfied | Remedial PR — Summary — “Made arrays-as-sets report generation resilient…”; Remedial PR — Testing — “1 passed in 0.05s” | Original met core output/proof but had a stability bug fixed in remediation. |
| Arrays-as-sets proof command proves report produced/covered: `python -m pytest tests/compare/test_arrays_as_sets.py` → `artifacts/canonical/arrays_as_sets_report.log` | Satisfied | Original PR — Logs — “python \-m pytest tests/compare/test\_arrays\_as\_sets.py” and report content | Keeps same proof command; hardens generator/test for already-canonical scenario | Satisfied | Remedial PR — Testing — “python \-m pytest tests/compare/test\_arrays\_as\_sets.py (summary: 1 passed in 0.05s)” | Implementation Doc defines this proof bar; remedial keeps it and strengthens robustness. |

### Evidence Print (PASS PROOF; required; whole PR)

#### A) Acceptance coverage evidence (Implementation Doc)

1. **Requirement label:** PR-02 — Arrays-as-sets evidence for registry/topology \+ governed report/log proof  
   * Evidence pointer(s) in Remedial PR proving satisfaction:  
     Remedial PR — Diff (artifacts/canonical/arrays\_as\_sets\_report.log) —  
     “surface: registry.catalog.channels\_v1”  
     “raw: \["sacral", "g"\]”  
     “normalized: \["g", "sacral"\]”  
   * Key proof facts (from Remedial PR artifacts):  
     * Report declares the registry surface: “surface: registry.catalog.channels\_v1”  
     * Report shows explicit before/after normalization: “raw: …” → “normalized: …”  
     * Report uses the named normalizer: “normalizer: engine.mech.helpers.canonicalize\_array”  
2. **Requirement label:** Arrays-as-sets proof command proves report produced/covered  
   * Evidence pointer(s) in Remedial PR proving satisfaction:  
     Remedial PR — Testing —  
     “✅ python \-m pytest tests/compare/test\_arrays\_as\_sets.py (summary: 1 passed in 0.05s)”  
     Remedial PR — Diff (tests/compare/test\_arrays\_as\_sets.py) —  
     `assert REPORT_PATH.exists()`  
     `report_text = REPORT_PATH.read_text(encoding="utf-8")`  
   * Key proof facts (from Remedial PR artifacts):  
     * Pytest pass: “1 passed in 0.05s”  
     * Test asserts the report exists and reads it.

#### B) Evidence/verification posture now satisfied (Original step closure)

* Original missing/failing evidence item (short label): **Regeneration brittleness: hard-fail when no “unsorted” case exists**  
  * Original PR evidence pointer: Original PR — Diff (tests/compare/test\_arrays\_as\_sets.py) —  
    `raise AssertionError(f"no unsorted {field} array found in channels_v1.json")`  
  * Remedial PR evidence pointer proving it is now satisfied:  
    Remedial PR — Diff (tests/compare/test\_arrays\_as\_sets.py) —  
    `return (..., True)` (fallback path)  
    Remedial PR — Diff (tools/evidence/generate\_arrays\_as\_sets\_report.py) —  
    `lines.append("note: raw == normalized (already canonical)")`  
  * Key proof fact (1 line): Remedial PR explicitly supports “already canonical” cases via fallback \+ note instead of failing.

#### C) Token and gate evidence (names-only; do not invent)

* Tokens/gates explicitly required by the Implementation Doc for this PR and/or explicitly claimed by Remedial PR artifacts: **None named in the Implementation Doc’s PR-02 proof-command anchor or in Remedial PR artifacts.**  
  Evidence pointer: Implementation Doc — proof-command anchor line —  
  “Arrays-as-sets proof (`python -m pytest tests/compare/test_arrays_as_sets.py` → proves `artifacts/canonical/arrays_as_sets_report.log` is produced/covered)”

#### D) Test/CI proof

* Job/test name (verbatim): `python -m pytest tests/compare/test_arrays_as_sets.py`  
  * Pass indicator (exact line): “✅ python \-m pytest tests/compare/test\_arrays\_as\_sets.py (summary: 1 passed in 0.05s)”  
  * Evidence pointer: Remedial PR — Testing — same line above.

#### E) Artifact/evidence outputs

* `artifacts/canonical/arrays_as_sets_report.log`  
  * Type: log/text  
  * Key proof facts (from Remedial PR artifacts):  
    * Declares registry surface: “surface: registry.catalog.channels\_v1”  
    * Shows before/after normalization: “raw: …” / “normalized: …”  
  * Evidence pointer: Remedial PR — Diff (artifacts/canonical/arrays\_as\_sets\_report.log) — the lines above.  
* `tools/evidence/generate_arrays_as_sets_report.py` (supporting regeneration tooling)  
  * Type: executable script  
  * Key proof facts (from Remedial PR artifacts):  
    * Uses determinism env enforcement: `ensure_determinism_env()`  
    * Emits fallback note when needed: “note: raw \== normalized (already canonical)”  
  * Evidence pointer: Remedial PR — Diff (tools/evidence/generate\_arrays\_as\_sets\_report.py) —  
    `ensure_determinism_env()`  
    `lines.append("note: raw == normalized (already canonical)")`

### Doc Deltas (PF-Canon only; REQUIRED)

Doc: PF12 — HDE-Schemas & Artifacts  
Section: §5.2 “Hash input”  
Delta: NEW CANON PROPOSAL — Add/clarify that `artifacts/canonical/arrays_as_sets_report.log` is a canonical, governed proof artifact used to demonstrate arrays-as-sets normalization on registry/topology surfaces, and name `tools/evidence/generate_arrays_as_sets_report.py` as its regeneration entrypoint (titles-only; no runbook).  
Why: The PR introduces and relies on this report artifact and generator as the proof surface for arrays-as-sets evidence.  
Evidence pointer: Remedial PR — Files (3) —  
“artifacts/canonical/arrays\_as\_sets\_report.log”  
“tools/evidence/generate\_arrays\_as\_sets\_report.py”

## 2.8 \- PR03 HDE-EPIC024 Review

### Review Summary

* The Original PR’s dev-step intent was to implement the D23 evidence index snapshot gate: a generator/validator plus the governed snapshot JSON and its `.path_proof.txt` sibling at the canonical gate-family path.  
  Evidence pointer: Original PR — Summary —  
  “Files added: tools/evidence/generate\_evidence\_index\_snapshot.py, audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json, audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json.path\_proof.txt.”  
* The Original PR did **not** fully satisfy the Implementation Doc’s validation strictness: it only type-checked `generated_at_utc` (string) and did not validate RFC3339 UTC format; and it assumed each mirror JSONL line parses to a dict before calling `.get()`.  
  Evidence pointer: Original PR — Diff (snapshot validator) —  
  `if not isinstance(payload.get("generated_at_utc"), str):`  
  Evidence pointer: Original PR — Diff (mirror parser) —  
  `entry = json.loads(line)` / `key = entry.get("artifact_key")`  
* The Remedial PR hardened the tool and added isolated pytest coverage for: PASS, non-object mirror line ⇒ FAIL\_BEHAVIOR (no traceback), and invalid `generated_at_utc` ⇒ FAIL\_BEHAVIOR with `GENERATED_AT_FORMAT`, while keeping the canonical CLI behavior unchanged.  
  Evidence pointer: Remedial PR — Summary —  
  “Added a path-injected runner … to support isolated testing while keeping the canonical CLI behavior unchanged.”  
* The remediation now satisfies the intended evidence/verification posture by proving the bug scenarios and keeping the proof command \+ governed outputs unchanged (still `python tools/evidence/generate_evidence_index_snapshot.py` and `audit/gates/evidence_index_snapshot/**`).  
  Evidence pointer: Remedial PR — Testing / logs —  
  “STATUS: PASS” and “============================== 3 passed in 0.06s \===============================”  
* The combined outcome aligns with the Implementation Doc’s PR-03 acceptance: canonical artifacts exist, the proof command yields PASS/FAIL\_BEHAVIOR/TOOLING\_BLOCKED status with correct exit behavior, and D23 remains tokenless (no new acceptance token introduced).  
  Evidence pointer: Implementation Doc — PR-03 Intent —  
  “yields `PASS` / `FAIL_BEHAVIOR` / `TOOLING_BLOCKED` status without introducing a new acceptance token.”  
* Tests/evidence posture is sufficient for confidence within PR-03 scope: the Remedial PR adds explicit failure-case tests that prevent “green CI but wrong” regressions for D23.  
  Evidence pointer: Remedial PR — tests/evidence/test\_evidence\_index\_snapshot.py —  
  `assert "Traceback" not in output`  
* Notable remaining risk (out of scope for this PR): the Original PR reported `ci/checks/check_mirror_schema.sh` failing due to pre-existing mirror mismatches; PR-03 does not resolve that broader evidence-index health issue (it’s covered by later EPIC024 work items).  
  Evidence pointer: Original PR — Testing —  
  “❌ ci/checks/check\_mirror\_schema.sh (exit 1: existing SHA/SIZE/proof mismatches in evidence index mirror)”

### Findings

1. **PR-03 acceptance is explicitly defined: canonical gate-family artifact \+ path proof, and a proof command that emits PASS/FAIL\_BEHAVIOR/TOOLING\_BLOCKED without minting a new acceptance token.**  
   * Observed (Implementation Doc — PR-03 Intent):  
     “The repo can generate and validate the Evidence Index snapshot artifact… and a proof command that yields `PASS` / `FAIL_BEHAVIOR` / `TOOLING_BLOCKED` status without introducing a new acceptance token.”  
   * Why it matters: This is the exact acceptance bar for merge readiness.  
2. **The Remedial PR includes the required governed outputs at the canonical path family and shows non-empty contents.**  
   * Observed (Remedial PR — Diff: snapshot JSON):  
     `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
     `{"generated_at_utc":"2026-01-16T15:30:56Z",...,"parity":{"artifact_keys_match":true},"schema_version":"1"}`  
   * Observed (Remedial PR — Diff: path proof):  
     `path: audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
     `sha256: 9381edd0de237d43c5f71e809d1ae12b715b25f1294f508a0678c69b2258d184`  
   * Why it matters: Confirms the canonical evidence surface exists and is concretely populated.  
3. **The Remedial PR demonstrates the required proof command output and exit behavior (PASS).**  
   * Observed (Remedial PR — Testing):  
     “✅ python tools/evidence/generate\_evidence\_index\_snapshot.py (STATUS: PASS, exit 0)”  
     and in logs:  
     `python tools/evidence/generate_evidence_index_snapshot.py`  
     `STATUS: PASS`  
   * Why it matters: Meets the Implementation Doc’s “Basic QA task” pass condition (exit 0 \+ artifacts present).  
4. **The Remedial PR fixes the code review bug: mirror JSONL parsing now treats non-object entries as validation errors (not crashes).**  
   * Observed (Remedial PR — Diff: tools/evidence/generate\_evidence\_index\_snapshot.py):  
     `entry = json.loads(line)`  
     `if not isinstance(entry, dict):`  
     `raise ValueError("evidence_index.jsonl entry must be an object")`  
   * Observed (Remedial PR — test):  
     `assert "STATUS: FAIL_BEHAVIOR" in output`  
     `assert "Traceback" not in output`  
   * Why it matters: Ensures deterministic FAIL\_BEHAVIOR mapping rather than unhandled exceptions.  
5. **The Remedial PR fixes the validation gap: `generated_at_utc` is now validated as RFC3339 UTC, and invalid values fail with an explicit issue marker.**  
   * Observed (Remedial PR — Diff: validator):  
     `update_evidence_index._parse_utc_iso8601(generated_at)`  
     `issues.append("GENERATED_AT_FORMAT")`  
   * Observed (Remedial PR — test):  
     `assert "GENERATED_AT_FORMAT" in output`  
     `assert "STATUS: FAIL_BEHAVIOR" in output`  
   * Why it matters: Directly enforces the Implementation Doc’s requirement: “`generated_at_utc` … must be an RFC3339 UTC timestamp.”  
6. **Original PR’s validation was incomplete relative to the Implementation Doc requirements.**  
   * Observed (Original PR — Diff: validator):  
     `if not isinstance(payload.get("generated_at_utc"), str):`  
     `issues.append("GENERATED_AT")`  
   * Observed (Original PR — Diff: mirror parser):  
     `entry = json.loads(line)`  
     `key = entry.get("artifact_key")`  
   * Why it matters: The first does not validate RFC3339 UTC; the second can raise `AttributeError` on non-dict JSON, preventing deterministic status mapping.  
7. **Doc drift is present in PF-Canon and should be drained, but it does not block merging this PR.**  
   * Observed (PF19 — Glow QA Guide, §4.4.4):  
     “Examples of posture-only check\_ids: `D22_canonical_json_gate_structured_record`, `D23_evidence_index_snapshot_artifact`.”  
   * Observed (PF09 — HDE-Build Checklist, “Subtask HDE-CALC003.19 — EPIC023 D23…”):  
     “**Subtask status:** **Not done**”  
     “`audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` (governed target; missing per Codex Audit HDE-EPIC024)”  
   * Why it matters: The Remedial PR implements the mechanical PASS/FAIL contract in-repo; these PF-Canon statements are now stale and can mislead future planning/QA.

### Requirement Satisfaction Crosswalk (Original step → Remediated satisfaction)

| Requirement label (Implementation Doc) | Original PR status | Evidence pointer(s) in Original PR | Remedial PR change that addresses it | Current status after remediation | Evidence pointer(s) in Remedial PR | Notes |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Canonical outputs exist at `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` \+ `.path_proof.txt` | Satisfied | Original PR — Diff shows both files as “New” and includes their contents. | Refreshed artifacts after tool hardening | Satisfied | Remedial PR — Diff shows snapshot JSON line and path proof fields (`path: …`, `sha256: …`). |  |
| Proof command yields PASS/FAIL\_BEHAVIOR/TOOLING\_BLOCKED (status mapping) and exit code semantics | Partially satisfied | Original PR — Testing shows PASS for the happy path: “✅ python tools/evidence/generate\_evidence\_index\_snapshot.py (STATUS: PASS, exit 0)”. | Adds explicit failure-scenario tests using path-injected runner | Satisfied | Remedial PR — tests assert FAIL\_BEHAVIOR and “Traceback” not present; logs show “STATUS: PASS” for happy path. | Remediation closes the “green-but-wrong” gap. |
| `generated_at_utc` is RFC3339 UTC (validated) | Not satisfied | Original PR — validator only checks string: `if not isinstance(payload.get("generated_at_utc"), str):` | Adds RFC3339 UTC parsing via existing helper \+ invalid timestamp test | Satisfied | Remedial PR — `update_evidence_index._parse_utc_iso8601(generated_at)` \+ test asserts `GENERATED_AT_FORMAT` and FAIL\_BEHAVIOR. |  |
| Mirror JSONL parsing must not crash on non-object entries (deterministic FAIL\_BEHAVIOR) | Not satisfied | Original PR — `_load_mirror_keys` does `entry = json.loads(line)` then `key = entry.get("artifact_key")` with no type guard. | Adds dict type guard \+ non-object mirror test | Satisfied | Remedial PR — `if not isinstance(entry, dict): raise ValueError(...)` \+ test asserts FAIL\_BEHAVIOR and no “Traceback”. |  |
| Basic QA task: run `python tools/evidence/generate_evidence_index_snapshot.py`; exit 0 and outputs exist/non-empty | Satisfied | Original PR — Testing includes “STATUS: PASS, exit 0” and diff shows non-empty outputs. | Re-runs generator after changes | Satisfied | Remedial PR — “STATUS: PASS” and updated non-empty snapshot \+ path proof. |  |
| No new acceptance token introduced for D23 (tokenless check posture) | Satisfied | Original PR — file set limited to tool \+ gate artifacts only. | Adds tests and path-injected runner; still no acceptance token claim emitted | Satisfied | Remedial PR — output/status lines only; file set is tool \+ gate artifacts \+ tests. | Implementation Doc explicitly says “without introducing a new acceptance token.” |

### Evidence Print (PASS PROOF; required; whole PR)

#### A) Acceptance coverage evidence (Implementation Doc)

1. **Requirement label:** PR-03 Intent (generate \+ validate snapshot; PASS/FAIL/TOOLING\_BLOCKED; tokenless)  
   * Evidence pointer(s) (Remedial PR — Testing / logs):  
     `python tools/evidence/generate_evidence_index_snapshot.py`  
     `STATUS: PASS`  
     and pytest pass:  
     `============================== 3 passed in 0.06s ===============================`  
   * Key proof facts:  
     * “STATUS: PASS” appears from the proof command output.  
     * Failure-scenario tests exist and pass, proving FAIL\_BEHAVIOR handling and no traceback.  
2. **Requirement label:** Evidence outputs (canonical paths)  
   * Evidence pointer(s) (Remedial PR — Diff):  
     `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
     `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`  
   * Key proof facts:  
     * Snapshot JSON includes required keys: `schema_version`, `generated_at_utc`, `inputs`, `parity`.  
     * Path proof file includes `path:`, `size_bytes:`, `sha256:`, `mtime_utc:`, `produced_at_utc:`.  
3. **Requirement label:** Basic QA task (exact command \+ pass condition)  
   * Evidence pointer(s) (Remedial PR — Testing):  
     “✅ python tools/evidence/generate\_evidence\_index\_snapshot.py (STATUS: PASS, exit 0)”  
   * Key proof facts:  
     * Exit 0 is explicitly reported alongside PASS.  
     * The governed artifacts are present in the diff and non-empty.

#### B) Evidence/verification posture now satisfied (Original step closure)

* **Original missing/weak item:** RFC3339 UTC validation for `generated_at_utc`  
  * Original PR evidence pointer: Original PR — validator excerpt —  
    `if not isinstance(payload.get("generated_at_utc"), str):`  
  * Remedial PR evidence pointer: Remedial PR — validator excerpt \+ test —  
    `update_evidence_index._parse_utc_iso8601(generated_at)`  
    `issues.append("GENERATED_AT_FORMAT")`  
    `assert "GENERATED_AT_FORMAT" in output`  
  * Key proof fact: invalid timestamp now produces FAIL\_BEHAVIOR with `GENERATED_AT_FORMAT`.  
* **Original missing/weak item:** Mirror JSONL non-object line could bypass deterministic FAIL\_BEHAVIOR mapping  
  * Original PR evidence pointer: Original PR — mirror parser excerpt —  
    `entry = json.loads(line)` / `key = entry.get("artifact_key")`  
  * Remedial PR evidence pointer: Remedial PR — mirror parser excerpt \+ test —  
    `if not isinstance(entry, dict): raise ValueError("evidence_index.jsonl entry must be an object")`  
    `assert "Traceback" not in output`  
  * Key proof fact: non-object mirror line now yields FAIL\_BEHAVIOR without a traceback.

#### C) Token and gate evidence (names-only; do not invent)

* **EVIDENCE\_PATH\_PROOFS\_OK**  
  * Status: Proven  
  * Evidence pointer(s):  
    * Implementation Doc — PR-03 Acceptance tokens list — `* EVIDENCE_PATH_PROOFS_OK`  
    * Remedial PR — Diff: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt` contains `sha256:` and `size_bytes:` lines, and the tool prints PASS.  
  * Proof fact (1 line): the governed `.path_proof.txt` exists with a concrete `sha256:` line and the validator run reports “STATUS: PASS”.

#### D) Test/CI proof

* Job/test name: `python tools/evidence/generate_evidence_index_snapshot.py`  
  * Pass indicator: `STATUS: PASS` / “(STATUS: PASS, exit 0)”  
  * Evidence pointer: Remedial PR — Testing and logs snippet.  
* Job/test name: `python -m pytest tests/evidence/test_evidence_index_snapshot.py`  
  * Pass indicator: `============================== 3 passed in 0.06s ===============================`  
  * Evidence pointer: Remedial PR — pytest output snippet.

#### E) Artifact/evidence outputs

1. `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
   * Type: json  
   * Key proof facts:  
     * Contains: `"schema_version":"1"`  
     * Contains: `"generated_at_utc":"2026-01-16T15:30:56Z"`  
   * Evidence pointer: Remedial PR — Diff: snapshot JSON one-line payload.  
2. `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`  
   * Type: text (path proof)  
   * Key proof facts:  
     * `sha256: 9381edd0de237d43c5f71e809d1ae12b715b25f1294f508a0678c69b2258d184`  
   * Evidence pointer: Remedial PR — Diff: path proof lines.  
3. Supporting verification artifact: `tests/evidence/test_evidence_index_snapshot.py`  
   * Type: test (python)  
   * Key proof facts:  
     * `assert "Traceback" not in output`  
     * `assert "GENERATED_AT_FORMAT" in output`  
   * Evidence pointer: Remedial PR — Diff: test file excerpt.

### Doc Deltas (PF-Canon only; REQUIRED)

Doc: PF09 — HDE-Build Checklist  
Section: “\#\#\# **Subtask HDE-CALC003.19 — EPIC023 D23: Evidence Index snapshot artifact (governed pointer)**”  
Delta: Update D23 posture from “tooling-blocked / missing” to “implemented gate-family surface exists,” remove claims that `audit/gates/evidence_index_snapshot/` is missing, and align the “missing tooling work” bullet list to the now-implemented outputs (snapshot JSON \+ `.path_proof.txt`) and mechanical PASS/FAIL validation.  
Why: PF09 currently states D23 is “Not done” and that the governed target is missing; the Remedial PR adds the gate artifacts and a PASS/FAIL validator with tests.  
Evidence pointer: Remedial PR — Files (4) and Diff —  
“audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json” and “audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json.path\_proof.txt” plus “STATUS: PASS”.

Doc: PF19 — Glow QA Guide  
Section: §4.4.4 “Primary step logs (one per check\_id; canonical)”  
Delta: NEW CANON PROPOSAL — Remove `D23_evidence_index_snapshot_artifact` from the “posture-only check\_ids” examples (or clarify it is no longer posture-only) now that a mechanical PASS/FAIL contract and validator exist.  
Why: PF19 currently frames D23 as an example posture-only check\_id; the Remedial PR implements deterministic FAIL\_BEHAVIOR scenarios and PASS/FAIL validation for D23.  
Evidence pointer: Remedial PR — tests/evidence/test\_evidence\_index\_snapshot.py —  
`assert "STATUS: FAIL_BEHAVIOR" in output` and `assert "Traceback" not in output`, plus generator “STATUS: PASS”.

Doc: PF12 — HDE-Schemas & Artifacts  
Section: “\#\#\# **Evidence index snapshot artifacts (single home; remove EPIC-local variant)**”  
Delta: NEW CANON PROPOSAL — Add the minimal required snapshot JSON field contract (schema\_version, generated\_at\_utc RFC3339 UTC, inputs paths/sha256s, parity.artifact\_keys\_match) as governed schema notes under the Evidence Index Snapshot section, matching the implemented snapshot artifact shape.  
Why: The PR introduces and relies on a specific minimal schema for `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` and validates it mechanically; recording the field contract in PF12 reduces drift risk for future validators and acceptance bindings.  
Evidence pointer: Remedial PR — Diff: snapshot JSON payload line containing `"schema_version":"1"`, `"generated_at_utc":…`, `"inputs":…`, `"parity":…`.

## 2.9 \- PR04 HDE-EPIC024 Review

---

### **Executive Summary**

* **PR04 scope (PLAN):** PR04 is a “final packaging” step to create a single EPIC024 QA root with deterministic check logs, token→evidence matrix, and an acceptance-map viability check.  
  **Evidence pointer:** Artifact **PLAN** — § “PR-04 — EPIC024 QA root \+ …” / “Intent” — quoted lines:  
  * “Create a single epic QA root at `audit/qa/hde-epic024/` that contains deterministic check logs, a token-to-evidence matrix, and a viability check for the acceptance map.”  
  * “This PR is the “final packaging” step…”  
* **PR0 defect state (BUG0):** PR0 produced an acceptance map that marks `QA_BOOTSTRAP_TOOLING_FAIL` as `implemented` and points it to the same bootstrap log as `QA_BOOTSTRAP_OK`, plus a viability gate that was always PASS and did not gate harness exit.  
  **Evidence pointer:** Artifact **BUG0** — top bug statement — quoted lines:  
  * “The acceptance map generator unconditionally sets the token `QA_BOOTSTRAP_TOOLING_FAIL` to `implemented` and points it to the same `audit/qa/hde-epic024/checks/D00_bootstrap/primary.log` as `QA_BOOTSTRAP_OK`.”

    **Evidence pointer:** Artifact **BUG0** — viability finding — quoted lines:  
  * “The acceptance-map viability check is always marked as PASS and never influences the harness exit status.”  
* **PR0 evidence of the bug in the produced acceptance map (PR0):** the generated acceptance map shows both bootstrap tokens as `implemented` and both reference the same `D00_bootstrap` log.  
  **Evidence pointer:** Artifact **PR0** — `docs/acceptance_map_epic024.json` excerpt — quoted lines:  
  * “"name":"QA\_BOOTSTRAP\_OK","status":"implemented","evidence\_files":\["audit/qa/hde-epic024/checks/D00\_bootstrap/primary.log"\]”  
  * “"name":"QA\_BOOTSTRAP\_TOOLING\_FAIL","status":"implemented","evidence\_files":\["audit/qa/hde-epic024/checks/D00\_bootstrap/primary.log"\]”  
* **PR1 remediation (PR1):** PR1 derived bootstrap-token statuses from the bootstrap check status, and made D13 viability status reflect detected issues so it affects harness exit code (i.e., no longer “always PASS”).  
  **Evidence pointer:** Artifact **PR1** — “PR change summary” bullets — quoted lines:  
  * “Derive QA\_BOOTSTRAP\_OK and QA\_BOOTSTRAP\_TOOLING\_FAIL token statuses from the bootstrap check’s status, so QA\_BOOTSTRAP\_TOOLING\_FAIL is Token-incomplete on a green run.”  
  * “Make D13\_acceptance\_map\_viability status reflect detected issues (PASS if none; FAIL\_BEHAVIOR if issues), so it affects harness exit code.”  
* **PR1 regression surfaced (BUG1):** the global mapping of `exit_code == 1` to `FAIL_BEHAVIOR` can misclassify bootstrap tooling failures (missing `pytest`) as behavior failures.  
  **Evidence pointer:** Artifact **BUG1** — top bug statement — quoted lines:  
  * “The change that globally maps `exit_code == 1` to `FAIL_BEHAVIOR` … may misclassify a bootstrap tooling failure …”  
  * “The bootstrap check runs `python -m pytest --version`. If pytest is missing, that returns exit\_code=1 and stderr contains `No module named pytest`…”  
* **PR2 fix (PR2):** PR2 adds a bootstrap-specific classifier so missing `pytest` maps to `FAIL_TOOLING` (and retains global `exit_code==1 => FAIL_BEHAVIOR` for true behavior failures), plus unit tests.  
  **Evidence pointer:** Artifact **PR2** — summary — quoted lines:  
  * “Add unit tests to ensure bootstrap check with missing pytest is treated as FAIL\_TOOLING, not FAIL\_BEHAVIOR.”  
  * “Implement bootstrap-specific classification helper for exit\_code \== 1 to detect missing pytest and map it to FAIL\_TOOLING.”  
* **PR2 verification evidence:** the PR2 unit test suite (`tests/qa/test_epic024_bootstrap_status.py`) is shown passing with exit code 0\.  
  **Evidence pointer:** Artifact **PR2** — testing output — quoted lines:  
  * “============================== 1 passed in 0.06s \===============================”  
  * “EXIT\_CODE:0”  
* **Deliverables appear satisfied vs PLAN (evidence outputs):** PLAN lists specific evidence outputs that must exist; PR0 shows those exact artifacts created (and PR2 scope is a targeted harness/test fix rather than a repackage of artifact paths).  
  **Evidence pointer:** Artifact **PLAN** — “Evidence outputs (must exist)” — quoted lines:  
  * “Evidence outputs (must exist):”  
  * “- `tools/qa/run_hde_epic024_harness.py`”  
  * “- `audit/qa/hde-epic024/qa_step_logs_manifest.json`”

    **Evidence pointer:** Artifact **PR0** — “Required artifacts created (new files)” — quoted lines:  
  * “Required artifacts created (new files):”  
  * “- tools/qa/run\_hde\_epic024\_harness.py”  
  * “- audit/qa/hde-epic024/qa\_step\_logs\_manifest.json”  
* **Residual risk (non-blocking):** PR2’s missing-pytest detection is string/regex based; if stderr phrasing differs, classification may not match expectation (no evidence in the 6 inputs of broader stderr variants beyond “No module named pytest”).  
  **Evidence pointer:** Artifact **BUG1** — describes the stderr phrase used for detection — quoted line:  
  * “stderr contains `No module named pytest`…”

---

### **Bug Story RCA (across PR0 → PR1 → PR2)**

#### **A) Bug statement (1–3 sentences)**

PR0 generated an acceptance map that falsely claimed the tooling-failure token `QA_BOOTSTRAP_TOOLING_FAIL` as implemented and pointed it to the same successful bootstrap log as `QA_BOOTSTRAP_OK`, while the acceptance-map viability check was always PASS and did not gate the harness exit status. PR1 remediated those issues but introduced a regression by globally mapping `exit_code == 1` to `FAIL_BEHAVIOR`, which can misclassify bootstrap tooling failures when `pytest` is missing.  
**Evidence pointer:** Artifact **BUG0** — top bug statement — quoted line:

* “The acceptance map generator unconditionally sets the token `QA_BOOTSTRAP_TOOLING_FAIL`…”

  **Evidence pointer:** Artifact **BUG0** — viability finding — quoted line:  
* “The acceptance-map viability check is always marked as PASS…”

  **Evidence pointer:** Artifact **BUG1** — regression statement — quoted line:  
* “The change that globally maps `exit_code == 1` to `FAIL_BEHAVIOR` … may misclassify a bootstrap tooling failure…”

#### **B) Timeline of the defect (bullets)**

* **PR0 produced the EPIC024 QA harness \+ artifacts, but acceptance-map bootstrap tokens and viability gating were incorrect.**  
  **Evidence pointer:** Artifact **BUG0** — acceptance map token mismatch — quoted line:  
  * “The acceptance map generator unconditionally sets the token `QA_BOOTSTRAP_TOOLING_FAIL` to `implemented`…”  
* **PR0 output demonstrates the defect concretely: both `QA_BOOTSTRAP_OK` and `QA_BOOTSTRAP_TOOLING_FAIL` appear as `implemented` and both cite the same `D00_bootstrap` log.**  
  **Evidence pointer:** Artifact **PR0** — `docs/acceptance_map_epic024.json` excerpt — quoted lines:  
  * “"name":"QA\_BOOTSTRAP\_OK","status":"implemented","evidence\_files":\["audit/qa/hde-epic024/checks/D00\_bootstrap/primary.log"\]”  
  * “"name":"QA\_BOOTSTRAP\_TOOLING\_FAIL","status":"implemented","evidence\_files":\["audit/qa/hde-epic024/checks/D00\_bootstrap/primary.log"\]”  
* **PR1 attempted remediation: bootstrap token statuses were derived from the bootstrap check status; D13 viability was made to reflect detected issues so it can gate exit code.**  
  **Evidence pointer:** Artifact **PR1** — change summary bullets — quoted lines:  
  * “Derive QA\_BOOTSTRAP\_OK and QA\_BOOTSTRAP\_TOOLING\_FAIL token statuses from the bootstrap check’s status…”  
  * “Make D13\_acceptance\_map\_viability status reflect detected issues…”  
* **BUG1 surfaced after PR1: missing `pytest` makes `python -m pytest --version` return exit\_code 1, but PR1’s global `exit_code==1 => FAIL_BEHAVIOR` mapping can misclassify that tooling failure.**  
  **Evidence pointer:** Artifact **BUG1** — bug statement — quoted lines:  
  * “The bootstrap check runs `python -m pytest --version`. If pytest is missing, that returns exit\_code=1…”  
  * “…stderr contains `No module named pytest`…”  
* **PR2 implemented bootstrap-specific classification and added unit tests to lock the behavior: missing `pytest` should be `FAIL_TOOLING`.**  
  **Evidence pointer:** Artifact **PR2** — PR2 summary — quoted lines:  
  * “Add unit tests to ensure bootstrap check with missing pytest is treated as FAIL\_TOOLING, not FAIL\_BEHAVIOR.”  
  * “Implement bootstrap-specific classification helper…”

#### **C) Root cause(s) (numbered; 1–N)**

1. **Root cause:** PR0’s acceptance-map generator treated the “tooling fail” token as implemented regardless of whether the tooling failure actually occurred (and pointed it to the same evidence as the success token), creating a false acceptance claim.  
   **Evidence pointer(s):**  
   * Artifact **BUG0** — acceptance map token mismatch — quoted line:  
     * “The acceptance map generator unconditionally sets the token `QA_BOOTSTRAP_TOOLING_FAIL` to `implemented`…”  
   * Artifact **PR0** — acceptance map excerpt — quoted line:  
     * “"name":"QA\_BOOTSTRAP\_TOOLING\_FAIL","status":"implemented","evidence\_files":\["audit/qa/hde-epic024/checks/D00\_bootstrap/primary.log"\]”  
2. **Root cause:** PR0’s acceptance-map viability check did not gate because it was always marked PASS and never influenced harness exit status.  
   **Evidence pointer:** Artifact **BUG0** — viability discussion — quoted line:  
   * “The acceptance-map viability check is always marked as PASS and never influences the harness exit status.”  
3. **Root cause:** PR1 introduced an overly broad rule (`exit_code == 1 => FAIL_BEHAVIOR`) that conflicts with the bootstrap check semantics, where missing `pytest` yields exit\_code 1 and should be treated as tooling failure.  
   **Evidence pointer:** Artifact **BUG1** — regression description — quoted line(s):  
   * “The change that globally maps `exit_code == 1` to `FAIL_BEHAVIOR` … may misclassify a bootstrap tooling failure…”  
   * “If pytest is missing, that returns exit\_code=1…”  
4. **Root cause:** Lack of automated tests for the “missing pytest” bootstrap failure case allowed the regression to survive until BUG1.  
   **Evidence pointer:** Artifact **PR2** — PR2 summary states tests were added specifically for this scenario — quoted line:  
   * “Add unit tests to ensure bootstrap check with missing pytest is treated as FAIL\_TOOLING, not FAIL\_BEHAVIOR.”

#### **D) Fix verification (bullets)**

* **PR1 addressed PR0’s acceptance-map token mismatch by deriving bootstrap token statuses from the bootstrap check’s status.**  
  **Evidence pointer:** Artifact **PR1** — change summary — quoted line:  
  * “Derive QA\_BOOTSTRAP\_OK and QA\_BOOTSTRAP\_TOOLING\_FAIL token statuses from the bootstrap check’s status…”

    **Why this addresses the root cause:** It removes unconditional “implemented” for `QA_BOOTSTRAP_TOOLING_FAIL` by tying token status to observed check status (i.e., tool-fail token should not be “implemented” on a green run).  
    **Evidence pointer:** Artifact **PR1** — same change summary line (ties token status to check status).  
* **PR1 addressed PR0’s “always PASS” viability gating by making D13 reflect detected issues (PASS vs FAIL\_BEHAVIOR), so it affects harness exit code.**  
  **Evidence pointer:** Artifact **PR1** — change summary — quoted line:  
  * “Make D13\_acceptance\_map\_viability status reflect detected issues (PASS if none; FAIL\_BEHAVIOR if issues), so it affects harness exit code.”  
* **PR2 addressed PR1’s regression by adding a bootstrap-specific classifier for missing `pytest` and validating it via unit tests.**  
  **Evidence pointer (implementation):** Artifact **PR2** — diff snippet — quoted lines:  
  * `if exit_code == 1 and re.search(r"No module named pytest", stderr or "", re.I):`  
  * `return "FAIL_TOOLING"`  
  * `if exit_code == 1:`

    **Evidence pointer (test):** Artifact **PR2** — unit test excerpt — quoted lines:  
  * `def test_status_from_bootstrap_missing_pytest_is_tooling():`  
  * `status = _status_from_bootstrap(1, "No module named pytest")`  
  * `assert status == "FAIL_TOOLING"`  
* **PR2 verification evidence (tests executed and passing):**  
  **Evidence pointer:** Artifact **PR2** — test run output — quoted lines:  
  * “============================== 1 passed in 0.06s \===============================”  
  * “EXIT\_CODE:0”

#### **E) Residual risks / Unknowns**

* **Residual risk:** The missing-pytest classifier relies on matching stderr text (`"No module named pytest"`). If stderr wording differs (e.g., different python import error phrasing), classification may not trigger.  
  **Not an Unknown:** The specific phrase that triggered the regression is explicitly documented in BUG1 and is directly covered by PR2’s unit test.  
  **Evidence pointer:** Artifact **BUG1** — quoted line:  
  * “stderr contains `No module named pytest`…”  
* **Unknowns:** None identified that block PLAN deliverables, because PLAN’s required evidence outputs are explicitly enumerated and PR0 lists them as created (see Deliverables Confirmation).  
  **Evidence pointer:** Artifact **PLAN** — “Evidence outputs (must exist)” — quoted line:  
  * “Evidence outputs (must exist):”

---

### **PR04 Deliverables Confirmation (PLAN → PR2 evidence)**

#### **DC-001**

* **Requirement label (PLAN):**  
  **Evidence pointer:** Artifact **PLAN** — “PR-04 — EPIC024 QA root \+ …” / “Intent” — quoted line:  
  * “Create a single epic QA root at `audit/qa/hde-epic024/` that contains deterministic check logs, a token-to-evidence matrix, and a viability check for the acceptance map.”  
* **Intended outcome:** EPIC024 has a governed QA root that records deterministic per-check logs and includes both token→evidence mapping and acceptance-map viability gating.  
* **Status after PR2:** **Satisfied**  
* **Evidence print for status:**  
  **Evidence pointer:** Artifact **PR0** — artifact creation list (shows QA root \+ token matrix \+ viability log exist under QA root) — quoted lines:  
  * “- audit/qa/hde-epic024/token\_evidence\_matrix.md”  
  * “- audit/qa/hde-epic024/acceptance\_map\_viability.log”  
  * “- audit/qa/hde-epic024/qa\_step\_logs\_manifest.json”

    **Evidence pointer:** Artifact **PR0** — step logs manifest excerpt (demonstrates deterministic check log inventory exists as a manifest) — quoted lines:  
  * “\#\# `audit/qa/hde-epic024/qa_step_logs_manifest.json`”  
  * `{"D00_bootstrap_pytest": {"check_id": "D00_bootstrap_pytest", "log_path": "checks/D00_bootstrap_pytest/primary.log"},`  
* **PR0/PR1 context (optional):** PR1 explicitly fixed the acceptance-map viability gating so it can function as a gate rather than “always PASS.”  
  **Evidence pointer:** Artifact **PR1** — quoted line:  
  * “Make D13\_acceptance\_map\_viability status reflect detected issues…”

#### **DC-002**

* **Requirement label (PLAN):**  
  **Evidence pointer:** Artifact **PLAN** — “Evidence outputs (must exist)” — quoted lines:  
  * “Evidence outputs (must exist):”  
  * “- `tools/qa/run_hde_epic024_harness.py`”  
  * “- `audit/qa/hde-epic024/qa_step_logs_manifest.json`”  
* **Intended outcome:** The PR must include the harness entrypoint and the governed evidence outputs at the specified paths (including QA root artifacts).  
* **Status after PR2:** **Satisfied**  
* **Evidence print for status:**  
  **Evidence pointer:** Artifact **PR0** — “Required artifacts created (new files)” — quoted lines:  
  * “Required artifacts created (new files):”  
  * “- tools/qa/run\_hde\_epic024\_harness.py”  
  * “- audit/qa/hde-epic024/qa\_step\_logs\_manifest.json”  
* **PR0/PR1 context (optional):** PR2 focused on correcting bootstrap classification and adding tests, not changing the governed path set enumerated by PLAN.  
  **Evidence pointer:** Artifact **PR2** — quoted line:  
  * “Add unit tests to ensure bootstrap check with missing pytest is treated as FAIL\_TOOLING, not FAIL\_BEHAVIOR.”

#### **DC-003**

* **Requirement label (PLAN):**  
  **Evidence pointer:** Artifact **PLAN** — “Acceptance tokens:” — quoted lines:  
  * “Acceptance tokens:”  
  * “- QA\_BOOTSTRAP\_OK”  
  * “- QA\_BOOTSTRAP\_TOOLING\_FAIL”  
* **Intended outcome:** The PR must produce acceptance proof surfaces (acceptance map, token matrix, close report, etc.) that cover the enumerated acceptance tokens.  
* **Status after PR2:** **Satisfied**  
* **Evidence print for status:**  
  **Evidence pointer:** Artifact **PR0** — `audit/EPIC-024_close_report.md` excerpt showing token roster includes the PLAN tokens — quoted lines:  
  * “\#\# Final token roster (EPIC024)”  
  * “- QA\_BOOTSTRAP\_OK: implemented — audit/qa/hde-epic024/checks/D00\_bootstrap/primary.log”  
  * “- QA\_BOOTSTRAP\_TOOLING\_FAIL: implemented — audit/qa/hde-epic024/checks/D00\_bootstrap/primary.log”  
* **PR0/PR1 context (optional):** BUG0 indicates PR0’s acceptance-map encoding of bootstrap tokens was inconsistent; PR1 fixed that mapping, and PR2 fixed bootstrap classification so missing pytest maps to tooling failure.  
  **Evidence pointer:** Artifact **BUG0** — quoted line:  
  * “The acceptance map generator unconditionally sets the token `QA_BOOTSTRAP_TOOLING_FAIL`…”

    **Evidence pointer:** Artifact **PR2** — quoted line:  
  * “Implement bootstrap-specific classification helper…”

---

### **Evidence Print (whole PR04 sequence; PR2 primary)**

#### **A) Claimed deliverables / checks / outputs (names-only; do not invent)**

1. **`tools/qa/run_hde_epic024_harness.py`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **PLAN** — evidence outputs list — quoted line:  
     * “- `tools/qa/run_hde_epic024_harness.py`”

       Artifact **PR0** — required artifacts list — quoted line:  
     * “- tools/qa/run\_hde\_epic024\_harness.py”  
   * **Key proof fact:** “- tools/qa/run\_hde\_epic024\_harness.py”  
2. **`audit/qa/hde-epic024/qa_step_logs_manifest.json`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **PLAN** — quoted line:  
     * “- `audit/qa/hde-epic024/qa_step_logs_manifest.json`”

       Artifact **PR0** — quoted line:  
     * “- audit/qa/hde-epic024/qa\_step\_logs\_manifest.json”  
   * **Key proof fact:** “\#\# `audit/qa/hde-epic024/qa_step_logs_manifest.json`”  
3. **Per-check logs (example): `audit/qa/hde-epic024/checks/D09_generate_evidence_index_snapshot/primary.log`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **PR0** — D09 primary log header excerpt — quoted line:  
     * `{"captured_env":{"LC_ALL":"C"},"check_id":"D09_generate_evidence_index_snapshot","command":"python tools/evidence/generate_evidence_index_snapshot.py","exit_code":0,"status":"PASS"...,"claimed_tokens":[],"intended_tokens":[]...}`  
   * **Key proof fact:** `"check_id":"D09_generate_evidence_index_snapshot"... "status":"PASS"... "claimed_tokens":[],"intended_tokens":[]`  
4. **`audit/qa/hde-epic024/token_evidence_matrix.md`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **PR0** — required artifacts list — quoted line:  
     * “- audit/qa/hde-epic024/token\_evidence\_matrix.md”  
   * **Key proof fact:** “- audit/qa/hde-epic024/token\_evidence\_matrix.md”  
5. **`audit/qa/hde-epic024/acceptance_map_viability.log`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **BUG0** — viability check exists but was always PASS in PR0 (shows this log’s existence and role) — quoted line:  
     * “The acceptance-map viability check is always marked as PASS…”

       Artifact **PR0** — required artifacts list — quoted line:  
     * “- audit/qa/hde-epic024/acceptance\_map\_viability.log”  
   * **Key proof fact:** “- audit/qa/hde-epic024/acceptance\_map\_viability.log”  
6. **`docs/acceptance_map_epic024.json`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **PR0** — acceptance map excerpt exists — quoted line:  
     * “\#\# `docs/acceptance_map_epic024.json`”  
   * **Key proof fact:** “"name":"QA\_BOOTSTRAP\_OK"…” (acceptance map content)  
7. **Close pack: `audit/EPIC-024_close_report.md`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **PR0** — close report excerpt — quoted lines:  
     * “\# EPIC024 Close Report”  
     * “Rails posture: Closed rails. All evidence outputs are written under governed paths; no ad-hoc artifacts.”  
   * **Key proof fact:** “Rails posture: Closed rails…”  
8. **Close pack: `audit/EPIC-024_MANIFEST.json`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **PR0** — required artifacts list — quoted line:  
     * “- audit/EPIC-024\_MANIFEST.json”  
   * **Key proof fact:** “- audit/EPIC-024\_MANIFEST.json”  
9. **Doc delta surfaces: `audit/docdeltas/hde-epic024_doc_deltas.md` and QA meta `audit/qa/hde-epic024/00_meta/doc_deltas.md`**  
   * **Status:** **Proven**  
   * **Evidence pointer(s):** Artifact **PR0** — QA meta doc delta excerpt — quoted lines:  
     * “\# EPIC024 QA Doc Deltas”  
     * “Added EPIC024 QA root with step logs, token matrix, acceptance-map viability log, and manifest.”  
   * **Key proof fact:** “Added EPIC024 QA root with step logs, token matrix, acceptance-map viability log, and manifest.”  
10. **PR2 regression fix \+ tests: `tests/qa/test_epic024_bootstrap_status.py` behavior**  
* **Status:** **Proven**  
* **Evidence pointer(s):** Artifact **PR2** — summary — quoted line:  
  * “Add unit tests to ensure bootstrap check with missing pytest is treated as FAIL\_TOOLING, not FAIL\_BEHAVIOR.”

    Artifact **PR2** — test run output — quoted line:  
  * “============================== 1 passed in 0.06s \===============================”  
* **Key proof fact:** “EXIT\_CODE:0”

#### **B) Key artifacts/outputs referenced (as shown in PR docs)**

* **`audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`**  
  * **Where referenced:** PR0 — D09\_generate\_evidence\_index\_snapshot log header lists it as evidence output.  
  * **Quoted line(s):**  
    * `..."evidence_outputs":["audit/gates/evidence_index_snapshot/evidence_index_snapshot.json","audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt"]...`  
  * **Why it matters:** This shows the harness produces a governed “evidence index snapshot” artifact and ties it to a specific check run.  
* **`audit/qa/hde-epic024/checks/D00_bootstrap_pytest/primary.log`**  
  * **Where referenced:** PR0 — acceptance map evidence file pointer; close report token roster also references bootstrap primary log.  
  * **Quoted line(s):**  
    * “"name":"QA\_BOOTSTRAP\_OK","status":"implemented","evidence\_files":\["audit/qa/hde-epic024/checks/D00\_bootstrap/primary.log"\]”  
  * **Why it matters:** This is the canonical evidence path for bootstrap proof, and it was also central to the PR0 token-mapping defect in BUG0.  
* **`audit/qa/hde-epic024/qa_step_logs_manifest.json`**  
  * **Where referenced:** PR0 — printed manifest excerpt.  
  * **Quoted line(s):**  
    * “\#\# `audit/qa/hde-epic024/qa_step_logs_manifest.json`”  
  * **Why it matters:** The manifest is the deterministic index that anchors the step-log discipline for auditability.

---

\<eof\>  
