# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v9.1  
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

## Addendum Index:

**This section should be considered current and authoritative. Index all addenda numbers listed below.**

1. 2.1 Guard proofs are evidence-only unless and until Governance registers tokens  
2. 2.2 — Canonical JSON gate directory naming reconciliation  
3. 2.3 — Acceptance roster canonicalization for doc-delta \+ close-pack posture  
4. 2.4 — Canonical compare artifacts: reuse canon surfaces (no epic-local compare paths)  
5. 2.5 \- Doc-delta surfaces: staging vs epic-scoped capture (binding \+ naming)  
6. 2.6 — Close-pack artifacts: deterministic path-of-record  
7. 2.7 \- HDE-Phased Epics is historical-only (no in-flight epics)  
8. 2.8 \- PF23 consult is non-token closure evidence (no REALITY\_AUDIT\_OK)

9. 2.9 \- HDE-EPIC023 PR01

# 2\) Numbered Addendum List

## 2.1 Guard proofs are evidence-only unless and until Governance registers tokens

### **Why**

EPIC023 planning surfaced a recurring drift pattern: teams want to treat serializer/emitter guard proofs as “acceptance tokens,” but doing so creates unregistered token names and weakens acceptance defensibility. Guard proofs remain valuable, but they must be handled as **reviewable evidence artifacts** unless Governance explicitly registers tokens and defines their semantics.

### **Decision / Rule**

* **Default posture (normative):** Guard proofs are **evidence-only deliverables**, not acceptance tokens.  
  They must exist, be mechanically produced, and be reviewable, but they do not create new token obligations.  
* **No token invention:** A plan MUST NOT introduce or claim new “guard tokens” unless the token exists in the canonical token registry owned by HDE Governance. If a guard token is desired, it must be registered first, then adopted by plans and acceptance artifacts.  
* **Evidence quality requirement (still strict):** Evidence-only does not mean “loose.” Guard proof artifacts MUST:  
  1. be mechanically generated (no hand edits),  
  2. have a single primary log/artifact per guard check (per Live QA posture),  
  3. include a clear PASS or FAIL classification in the primary artifact,  
  4. be stored under governed roots when they are part of closure evidence, and  
  5. be index/mirror eligible when they are promoted to governed evidence.  
* **Promotion rule:** If a guard proof artifact is used to support closure wiring (for example referenced by the token/evidence matrix, acceptance map, or close pack), then it MUST be treated like other governed evidence:  
  1. stable path,  
  2. updated in the human index and machine mirror when bytes change,  
  3. with sibling path proof transcripts when required by the Evidence Catalog posture.  
* **Future tokenization path (explicit, non-implicit):** If a team wants guard proofs to become acceptance tokens later, that change MUST be routed as:  
  1. governance token registration and semantics definition, then  
  2. epic acceptance roster and evidence binding updates, then  
  3. QA/runbook updates that claim the tokens only when invariants are verified.

### **Drain targets (doc delta intents)**

* **PF04 — HDE Governance, §2.0 (Token registry and semantics)** → Add a short rule: “Guard proofs are evidence-only unless a token is registered; plans must not invent tokens.” If the project chooses to add specific guard tokens, register them here with semantics and required evidence surfaces.  
* **PF27 — Canon Plan Templates (Epic Plan Acceptance section)** → Clarify that “evidence-only deliverables” are allowed in deliverables lists and must be evidenced, but do not require token claims unless the token exists in Governance.  
* **PF19 — Glow QA Guide, §4.4 (Step logs and token claim semantics)** → Reinforce that tokens are claims and must not be introduced ad hoc; allow evidence-only guard checks to be logged without claimed tokens.  
* **PF20 — HDE Phased Epics (Acceptance conventions)** → Clarify that guard proofs can be required deliverables without being tokenized, and describe the governance-first pathway if tokenization is later desired.  
* **PF12 — HDE Schemas and Artifacts (Evidence catalog and indexing discipline)** → Clarify that evidence-only guard artifacts, when promoted to governed evidence, must follow normal index/mirror/path proof discipline.

### **Notes / conflicts**

* This addendum is intentionally conservative: it preserves token discipline and prevents “quiet token sprawl” while still requiring guard evidence to exist and be reviewable.  
* It does not prohibit future tokenization. It makes tokenization explicit and governance-led.

## 2.2 — Canonical JSON gate directory naming reconciliation

**Why**  
A canon conflict exists over where canonical JSON gate artifacts live: some canon/evidence wiring expects `audit/gates/canonical_json/*`, while mechanics language (and some existing plan wiring) has used `audit/gates/canonical/*`. This ambiguity is execution-critical because acceptance maps, evidence binding, and index/mirror entries must not be dual-homed.

r4 Epic Plan HDE-EPIC023

**Decision / Rule**

* **Canonical directory (normative):** Canonical JSON gate artifacts MUST live under:  
  `audit/gates/canonical_json/`  
  This is the only acceptable canonical home for new work and for acceptance binding in EPIC023.  
   r4 Epic Plan HDE-EPIC023  
* **No dual-home acceptance binding:** Acceptance maps, token/evidence matrices, close-pack manifests, and evidence index/mirror bindings MUST NOT reference both `audit/gates/canonical/*` and `audit/gates/canonical_json/*` for the same canonical JSON gate family. Pick one (this addendum picks `canonical_json`) and bind to it only.  
   r4 Epic Plan HDE-EPIC023  
* **Legacy directory posture:**  
  `audit/gates/canonical/` is legacy/compat-only. If artifacts exist there, they MUST NOT be treated as canonical acceptance surfaces. They MAY be retained only as non-canonical convenience copies, and MUST NOT be indexed/mirrored as the canonical gate family. (If tooling emits only to the legacy path, treat it as a tooling defect, not a documentation exception.)  
   PF10-HDE-Build-Notes-v8.8.4-spe…  
* **Evidence binding rule:** Any token that claims canonical JSON gate satisfaction MUST bind to the `audit/gates/canonical_json/*` artifacts in the acceptance map \+ token/evidence matrix \+ Evidence Index/Mirror. (No aliases.)

**Drain targets (doc delta intents)**

* **PF12 — HDE Schemas and Artifacts, §(canonical JSON gates / evidence catalog entry for canonical JSON checks)** → Declare `audit/gates/canonical_json/*` as the single canonical home for canonical JSON gate artifacts; mark `audit/gates/canonical/*` as legacy/compat-only and explicitly non-bindable for acceptance.  
* **PF14 — HDE Mechanics Guide, §17.8 (canonical JSON compare discipline)** → Update any references that imply the canonical home is `audit/gates/canonical/*` to `audit/gates/canonical_json/*`.  
* **PF27 — Canon Plan Templates, §(Epic Plan \+ acceptance/evidence posture templates)** → Ensure templates and examples reference only `audit/gates/canonical_json/*` for canonical JSON gate artifacts and explicitly forbid dual-home acceptance binding.  
* **PF09 — HDE Build Checklist, §(Calcination canonical JSON tasks)** → Align any task guidance that references canonical JSON gate paths to the single canonical directory.

**Notes / conflicts**

* This addendum is intentionally path-binding and acceptance-focused: it resolves ambiguity by selecting one canonical home and prohibiting dual-home acceptance wiring.  
   r4 Epic Plan HDE-EPIC023

---

## 2.3 — Acceptance roster canonicalization for doc-delta \+ close-pack posture

**Why**  
Multiple plans/reviews have surfaced drift where acceptance rosters contain non-canonical token strings (e.g., `CANON_JSON_OK`, `DOC_DELTA_CAPTURED_OK`, and an unverified `CLOSE_PACK_FILES_PRESENT_OK`). Token strings are contract surfaces; invalid names force guessing and undermine registry validation.

r4 Epic Plan HDE-EPIC023

r3 Epic Plan HDE-EPIC023

**Decision / Rule**

* **Token names are registry-bound (normative):** Acceptance tokens listed in epic plans, acceptance maps, token/evidence matrices, and step logs MUST match the canonical token registry spellings. No aliases, near-matches, or “local tokens.”  
   r4 Epic Plan HDE-EPIC023  
* **Canonical token replacements (normative):**  
  * Replace `CANON_JSON_OK` → `JSON_CANONICAL_CHECK_OK`.  
     r4 Epic Plan HDE-EPIC023  
    r3 Epic Plan HDE-EPIC023  
  * Replace `DOC_DELTA_CAPTURED_OK` → `DOC_DELTA_PRESENT_OK`.  
     r4 Epic Plan HDE-EPIC023  
    r3 Epic Plan HDE-EPIC023  
* **Close-pack presence posture (normative):**  
  Close-pack presence is a **baseline artifact requirement**, not a token by default. Close-pack outputs MUST exist under the canonical close-pack filenames, and any extra copies elsewhere are convenience-only and MUST NOT be used for acceptance binding.  
   PF10-HDE-Build-Notes-v8.8.4-spe…  
  * Therefore: remove `CLOSE_PACK_FILES_PRESENT_OK` from epic acceptance rosters unless and until it is explicitly registered and canonized as a token (governance-led).  
     r4 Epic Plan HDE-EPIC023  
* **Unregistered token handling (normative):**  
  If a token name appears in an epic’s acceptance roster but is not registered, it MUST NOT be claimed as satisfied. Evidence may still be collected and bound, but the token claim remains blocked until the roster/registry is reconciled.  
   PF10-HDE-Build-Notes-v8.8.4-spe…

**Drain targets (doc delta intents)**

* **PF04 — HDE Governance, §(token registry entries for DOC\_DELTA\_PRESENT\_OK and JSON\_CANONICAL\_CHECK\_OK)** → Confirm these tokens are the canonical spellings and ensure any legacy spellings are explicitly rejected (no alias acceptance).  
* **PF27 — Canon Plan Templates, §(Epic Plan deliverables \+ baseline artifacts \+ token list examples)** → Ensure the template uses `DOC_DELTA_PRESENT_OK` and `JSON_CANONICAL_CHECK_OK` (never the invalid variants), and that close-pack presence is expressed as baseline artifacts, not a token requirement.  
* **PF20 — HDE Phased Epics, §(acceptance conventions / close conditions)** → Align acceptance language to: (a) registry-canonical token names, and (b) close-pack presence as baseline artifacts (canonical filenames), not as an assumed token.  
* **PF19 — Glow QA Guide, §(token roster guidance / step-log claim posture)** → Reinforce: token lists are optional in plans; when used they must be registry-canonical; step logs must not claim unregistered tokens; close-pack presence is verified via artifact existence \+ binding, not a token.  
   PF10-HDE-Build-Notes-v8.8.4-spe…

**Notes / conflicts**

* This addendum does not weaken acceptance. It removes ambiguous token strings and anchors close-pack presence to the canonical artifact family, which is already a hard requirement.

## **2.4 — Canonical compare artifacts: reuse canon surfaces (no epic-local compare paths)**

### **Why**

EPIC023 raised an execution-critical choice: whether to reuse existing canon-defined compare artifacts/surfaces or introduce a new compare artifact. If compare surfaces are invented per-epic, acceptance binding becomes inconsistent and closure wiring becomes non-deterministic across epics.

### **Decision / Rule**

* **Default posture (normative):** Canonical compare evidence MUST reuse **canon-defined compare artifact surfaces**.

* **No epic-local compare paths:** An epic MUST NOT introduce a new compare artifact path as “the canonical compare proof” unless that path is explicitly introduced via PF10 and drained into the owning PF-Canon homes.

* **Acceptance binding constraint:** Acceptance maps and token/evidence matrices MUST bind compare evidence to the canon-defined surfaces only (no dual-home, no aliases).

* **Token constraint:** No new acceptance tokens may be introduced for compare proofs unless registered in HDE Governance.

### **Drain targets (doc delta intents)**

* **PF14 — HDE Mechanics Guide, §17.8** → Make the canonical compare artifact surfaces explicit for canonical JSON compare proofs, and explicitly prohibit per-epic alternate compare paths.

* **PF12 — HDE Schemas & Artifacts, §(canonical JSON gates / compare artifacts entry)** → List the canonical compare artifact family as part of the canonical JSON gate evidence catalog so acceptance binding has a single home.

* **PF27 — Canon Plan Templates (Epic Plan acceptance/evidence posture templates)** → Add a template rule: compare evidence must bind to canon surfaces; if a new surface is truly needed, it must be introduced via an ADR \+ doc delta path (not silently invented in an epic plan).

### **Notes / conflicts**

* This addendum governs **evidence surfaces and acceptance binding**, not implementation technique.

* If canon does not currently define a compare artifact surface for the needed compare proof, that is a canon gap that must be resolved through the drain targets above before the epic plan binds to a new path.

## 2.5 \- Doc-delta surfaces: staging vs epic-scoped capture (binding \+ naming)

**Why:** Reviews are blocking on placeholder doc-delta paths and missing epic-scoped capture artifacts, driven by ambiguous binding between doc-delta draft staging and the QA capture file. The review explicitly flags PF04 vs PF09 location differences and PF10 silence on how they bind.

**Decision / Rule**

* **MUST** treat doc-deltas as a **two-surface pair**:

  * **Draft/staging surface** under `audit/docdeltas/` (used for the in-flight doc-delta artifact and token binding).

  * **Epic-scoped capture surface** at `audit/qa/<epic-id>/00_meta/doc_deltas.md` (used as the stable QA record for the epic).

* **MUST** require a **concrete** filename for the draft/staging surface; placeholders like `audit/docdeltas/<doc-delta>.md` are nonconforming.

* **SHOULD** standardize the draft filename as: `audit/docdeltas/<epic-id>_doc_deltas.md` (lowercase epic-id), unless superseded by a later canon naming rule.

* **MUST** ensure the Epic Plan’s token↔evidence bindings reference:

  * The draft/staging surface for doc-delta token evidence, and

  * The epic-scoped capture file as the authoritative narrative/record surface.

**Drain targets (doc delta intents)**

* **PF04 — HDE Governance, §2.0.13** → Clarify the required doc-delta draft naming convention and explicitly state its relationship to the epic-scoped capture file.

* **PF09 — HDE Build Checklist, HDE-CALC003.2** → Explicitly list both required doc-delta artifacts (draft \+ epic-scoped capture) and their roles.

* **PF27 — Canon Plan Templates, HDE-EPIC-Plan (D0 / preflight deliverables)** → Add explicit plan slots for both doc-delta surfaces (so plans cannot “forget” one).

**Notes / conflicts**

* This addendum resolves *binding ambiguity* (draft vs capture) without changing token semantics.

---

## 2.6 — Close-pack artifacts: deterministic path-of-record

**Why:** Close-pack artifact “names-only” baseline expectations exist, but deterministic location is repeatedly forced into per-epic ADRs due to underspecified/competing guidance. The review calls this out as a canon reconciliation need (PF27 vs PF09/PF12), with PF10 currently not specifying the location rule.

**Decision / Rule**

* **MUST** locate the close-pack pair at the canonical `audit/` paths using the `EPIC-###` pattern (3 digits):

  * `audit/EPIC-###_close_report.md`

  * `audit/EPIC-###_MANIFEST.json`

* **MUST** treat these as **baseline close-pack artifacts** (required closure artifacts), not acceptance tokens.

* **MUST NOT** relocate these artifacts into alternative directory trees (e.g., `audit/qa/**`, `artifacts/**`) without an explicit canon change.

* **SHOULD** require Epic Plans to cite PF12 path patterns at the point the close-pack baseline is declared (so the “path-of-record” is not discretionary).

**Drain targets (doc delta intents)**

* **PF27 — Canon Plan Templates, HDE-EPIC-Plan (Plan Preflight: “Close-pack baseline declared”)** → Add deterministic path pattern or explicit normative reference to PF12 path patterns (so “names-only” cannot be interpreted as “location TBD”).

* **PF12 — HDE Schemas and Artifacts (path patterns used for close-pack artifacts)** → Ensure the close-pack path patterns are clearly and centrally stated (and easy to cite) for epic plans.

* **PF09 — HDE Build Checklist (close/pack checklist items, if any mention close-pack artifacts)** → Align any checklist references to the deterministic `audit/EPIC-###_*` locations.

**Notes / conflicts**

* This addendum chooses a single deterministic location rule aligned to the PF12 path pattern example, removing the need for per-epic ADRs.

## **2.7 \- HDE-Phased Epics is historical-only (no in-flight epics)**

### **Why**

HDE-Phased Epics is widely referenced as a stable map of what has been delivered. When in-flight epics are recorded and repeatedly edited during active work, readers interpret the document as current-state truth. That creates confusion, churn, and plan thrash.

This addendum converts HDE-Phased Epics into a historical archive only, so in-flight work is not prematurely canonized.

### **Decision / Rule**

* Historical-only scope (normative): HDE-Phased Epics MUST contain only completed epic records.

* Definition of “completed” (normative): An epic is “completed” only when its closure criteria are satisfied and the epic is formally closed per the Epic Process Guide. Until that point, it is in-flight.

* No in-flight records (normative): In-flight epics MUST NOT be added to HDE-Phased Epics. Do not create partial records. Do not pre-stage placeholders.

* Archive-on-close (normative): The epic record is added to HDE-Phased Epics only once, at epic close, as a final historical entry.

* Immutability posture (normative): Once an epic record is added to HDE-Phased Epics, it SHOULD be treated as historical. Post-close changes SHOULD be avoided. If a correction is required, it MUST be handled in a way that preserves the historical nature of the entry (for example, a clearly labeled correction note), rather than ongoing edits that reintroduce churn.

* Drift rule (normative): If HDE-Phased Epics currently contains any in-flight epic entries, those entries represent drift against this policy. HDE-Phased Epics must not contain them going forward.

### **Drain targets (doc delta intents)**

* HDE-Phased Epics: Update the document purpose/usage text to explicitly state “historical-only,” define “completed,” and state that in-flight epics are not recorded.

* Epic Process Guide: Update any epic-record guidance to reflect “archive-on-close” for HDE-Phased Epics (no creation or updates during active work).

* Canon Plan Templates: Ensure Epic Plan requirements do not imply that an in-flight epic must be present in HDE-Phased Epics as a planning gate.

* Glow QA Guide: If any QA workflow text treats HDE-Phased Epics as current-state tracking for active work, update it to reflect that it is historical-only.

### **Notes / conflicts**

* This addendum changes where “current epic tracking” lives by exclusion: HDE-Phased Epics becomes a historical ledger, not an active tracker.

* This addendum does not change what “epic close” requires. It only changes when and how the epic is recorded in HDE-Phased Epics.

## 2.8 \- PF23 consult is non-token closure evidence (no REALITY\_AUDIT\_OK)

### **Why**

Plans have attempted to represent PF23 Reality Audits consult scope as an in-scope acceptance token (example: `REALITY_AUDIT_OK`). This creates two kinds of drift:

* Token drift: the token string is not registered in the Governance token registry, so it cannot be safely claimed or wired.

* Semantics drift: Reality Audits are a separate axis of planning and scope verification. They are not equivalent to acceptance and must not be collapsed into a token.

This addendum makes the representation rule explicit so future epics do not invent tokens or mis-wire closure.

### **Decision / Rule**

* **No PF23 consult token (normative):** Plans and implementations MUST NOT mint, claim, or reference `REALITY_AUDIT_OK` (or any similar “PF23 consult completion” acceptance token) unless and until Governance registers such a token in the Governance token registry.

* **PF23 is a separate axis (normative):** PF23 consult scope MUST be represented as a consult requirement and closure evidence, not as an acceptance token.

* **How PF23 consult is evidenced (normative):** When PF23 is required for an epic or plan, the work MUST produce a short consult record that includes:

  * a **PF23 Anchors** list (components used and the key loci/pathnames pulled from PF23 that the plan will touch), and

  * a brief **“what changed / what did not”** summary scoped to the epic or plan.

* **Where the consult record lives (normative):** The PF23 consult record MUST be captured as non-token closure evidence in existing closure surfaces (for example, the epic-scoped meta record and the close report). It MUST NOT appear in the acceptance token roster.

* **Acceptance roster hygiene (normative):** Any acceptance roster that includes `REALITY_AUDIT_OK` is nonconforming and MUST be corrected before close. The correction is to remove the token and keep the PF23 consult as non-token evidence.

* **Governance change boundary (normative):** If the org decides a token is needed for PF23 consult completion, that is a Governance change. It MUST be introduced through the Governance token registry and drained to all dependent canon homes. Until that happens, no plan may treat PF23 consult as a token.

### **Canon touchpoints**

* PF04 \- HDE Governance, §2.0.18 (QA Acceptance Tokens and PF23 scope)

* PF04 \- HDE Governance, §9.7.11 (PF23 Anchors guidance)

* PF23 \- Reality Audits (consult source for components and loci)

* PF10 \- HDE Build Notes (token discipline posture: no invented tokens)

### **Drain targets (doc delta intents)**

* PF27 \- Plan Templates: ensure Epic Plan templates include a PF23 Anchors requirement and explicitly state PF23 consult is not an acceptance token.

* PF19 \- Glow QA Guide: ensure the QA Acceptance Tokens library does not introduce or imply a `REALITY_AUDIT_OK` style token.

* PF12 \- HDE Schemas and Artifacts: if any dedicated PF23 consult artifact family is later standardized, define its catalog entry and indexing rules there.

* PF04 \- HDE Governance: if needed, add an explicit example prohibition for `REALITY_AUDIT_OK` to prevent future reintroduction.

### **Notes / conflicts**

* This addendum does not change PF23 audits themselves. It only clarifies how PF23 consult is represented in plans and closure.

* This addendum intentionally prefers “consult evidence” over new tokens to avoid governance churn for implementation-only epics.

## 2.9 \- HDE-EPIC023 PR01

### Post-Remediation Final Review

### Review Summary

* Remedial PR focuses on evidence hygiene around EPIC023 scaffolds: regenerating evidence index/mirror-related metadata and refreshing topology orientation output/proofs so evidence checks are coherent.  
* The Bug Report defect (EPIC023 artifacts backdated in the evidence index via `produced_at_utc=2025-11-30` despite 2026 capture context) is addressed by updating EPIC023 evidence index entries and regenerating path proofs/sentinels.  
* The regression risk visible in the Original PR (EPIC023 scaffold entries present with `produced_at_utc=2025-11-30`) is real and is what the remediation targets.  
* Remedial PR remains aligned with the Implementation Plan’s PR-01 intent: EPIC023 QA root \+ acceptance scaffolds \+ doc-delta surfaces, with evidence tooling used to keep Index/Mirror/proofs coherent when new governed bytes exist.  
* Tests/evidence posture is sufficient for this remediation class: the Bug Report’s own acceptance notes include `update_evidence_index.py --check`, `orientation_demo.py --check`, and mirror schema validation.  
* Notable risk: this remediation necessarily touches global evidence/topology surfaces (orientation demo \+ path proofs) and may generate missing proofs for older artifacts to satisfy coherence checks; this is acceptable if the changes remain evidence-only and checks stay green.

### Findings

1. **Implementation Plan scope match (PR-01 deliverables exist and are described as introduced).**  
   * Observed: Implementation Plan PR-01 requires EPIC023 acceptance scaffolds \+ QA ledger scaffolds \+ concrete doc-delta draft.  
   * Observed: Remedial PR includes a doc-delta draft that explicitly records the addition of EPIC023 acceptance map \+ token matrix \+ QA ledgers and notes evidence index/mirror refresh.  
   * Why it matters: Confirms the remedial PR is still executing PR-01’s intended scope, not pivoting to future PR workstreams.  
2. **Bug Report defect is real in Original PR (backdated EPIC023 entries).**  
   * Observed: Bug Report calls out EPIC023 artifacts being recorded with `produced_at_utc` set to `2025-11-30`, contradicting 2026 capture context and path proof mtimes.  
   * Observed: Original PR evidence shows EPIC023 entries (e.g., `epic023.acceptance_map`) in the mirror with `produced_at_utc:"2025-11-30T03:58:47Z"`.  
   * Why it matters: Establishes the remediation is necessary and the defect is not hypothetical.  
3. **Remediation addresses the bug as specified (update produced\_at\_utc \+ regenerate proofs/sentinels).**  
   * Observed: Bug Report’s acceptance summary states the remediation updated EPIC023 evidence index entries to 2026 capture timestamps and regenerated corresponding path proofs and hash sentinel; it also lists the evidence checks run.  
   * Observed: The updated-side entries for EPIC023 show `produced_at_utc` values in 2026 for acceptance map, doc delta, QA meta doc deltas, step log manifest, and token matrix.  
   * Why it matters: This is a direct 1:1 satisfaction of the Bug Report’s request (“regenerate index entries/path proofs with the actual 2026 timestamps”).  
4. **Remediation is not superficial: it re-establishes topology/evidence coherence and corrects proof drift.**  
   * Observed: Remedial PR shows orientation demo initially reporting missing proofs, then generating missing proofs via evidence tooling, rerunning orientation generation, and reaching `status: ok` with coherence.  
   * Observed: Remedial PR also detects and corrects a stale proof size mismatch for the orientation demo artifact by re-running evidence tooling in write mode.  
   * Why it matters: This demonstrates the remediation actually fixes the kind of “CI can be green and still wrong” risk: stale/incorrect coherence artifacts and path proof drift.  
5. **Evidence \+ checks appear adequate for merge confidence for this PR class.**  
   * Observed: Bug Report explicitly lists these checks as passing: `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, and `python ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`.  
   * Why it matters: These checks directly target the affected surfaces (Index/Mirror coherence \+ topology orientation coherence \+ mirror schema validity).

\<eof\>