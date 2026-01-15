# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v9.3.7  
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

\<eof\>  
