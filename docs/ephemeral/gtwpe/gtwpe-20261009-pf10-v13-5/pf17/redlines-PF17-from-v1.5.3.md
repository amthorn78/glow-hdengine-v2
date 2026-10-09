# Redlines — PF17 from v1.5.3

Run: gtwpe-20261009-pf10-v13-5 / T-PF17.
Task: T-PF17; stage: TW-DRAIN-10 100926.1.
Original: `docs/pfcanon/PF17-Canon-HDE-Narratives-Guide-v1.5.3.md` at `e7265a090ad0cc8de5f36de2f19481216aa3d073`; internal title `PF17-Canon-HDE-Narratives-Guide`, version v1.5.3.
Original Git blob: `a9e73a8adf03dfccabdad8503d02c4ff4e27e190`.
Original raw UTF-8 SHA-256: `2655c959637c52868a62ab7f7f27e5e04d9c5bca5f8acb3dbcc2b5d1cfd01d1f`; 121,552 bytes.
Preparer: Nathan-started T-PF17 Work document session; workspace /workspace/scratch/64476f52c0c0; preparer and applier are the same assistant in this conversation; no platform conversation ID is available.
Selected originals: A23, A24, A26, A30; S01, S06, S07, S12; complete C1, as bounded by `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md` at `f057d124176143b3e02ba7ad599880fd7e9991b1`.

Nine content replacements. Header document-control fields are reserved for TW-APPLY-10: v1.5.4, actual execution date in native format, and `BN 13.5`. No revision-history entry is required by this target. The title, status Canon, invocation tag, and all other control values are retained.

The literal payloads below include their final LF, immediately before the closing fence. Fences are presentation delimiters, not payload. Each operation resolves independently against the unchanged original.

## RL-001

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# 0\) Front Matter`
- `## 0.2 Scope & Audience`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Extend the owned surface inventory to the approved Reader v2 without changing Aux or admin preview ownership.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [966, 1161); exact literal, with LF line endings.

Old text:

````text
* **Surfaces (policy level).** Reader v1 is narrative-free; Aux Narrative and CLI admin preview exist and are routed by title to their single homes (HDE-CLI-API-Vendor-Ref and HDE-Governance).  
````

Replacement text:

````text
* **Surfaces (policy level).** Reader v1 and Reader v2 are narrative-free; Aux Narrative and CLI admin preview exist and are routed by title to their single homes (HDE-CLI-API-Vendor-Ref and HDE-Governance).  
````

## RL-002

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# 1\) Purpose & Ground Rules`
- `## 1.1 Purpose & Non-Goals`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Keep the existing deterministic composer purpose and add the Reader v2 exclusion from narrative text.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [7854, 8474); exact literal, with LF line endings.

Old text:

````text
Specify a **deterministic, LLM-free** layer that converts validated mechanics results and a validated narrative pack view into one short, human-readable paragraph for the **Aux narrative surface** and **CLI admin preview**, while leaving **Reader v1 unchanged and narrative-free**. The composer is a **pure function** with **two-run identity**, symmetric shared behavior, and directional swap covariance; its result is emitted through the **single shared presenter/emitter**. The concrete bytes/serializer contract is routed by title to **HDE-CLI-API-Vendor-Ref**, **HDE-Schemas & Artifacts**, and **HDE Architecture**.
````

Replacement text:

````text
Specify a **deterministic, LLM-free** layer that converts validated mechanics results and a validated narrative pack view into one short, human-readable paragraph for the **Aux narrative surface** and **CLI admin preview**, while leaving **Reader v1 unchanged and narrative-free** and keeping **Reader v2 narrative-free**. The composer is a **pure function** with **two-run identity**, symmetric shared behavior, and directional swap covariance; its result is emitted through the **single shared presenter/emitter**. The concrete bytes/serializer contract is routed by title to **HDE-CLI-API-Vendor-Ref**, **HDE-Schemas & Artifacts**, and **HDE Architecture**.
````

## RL-003

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# 1\) Purpose & Ground Rules`
- `## 1.1 Purpose & Non-Goals`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Preserve every v1 obligation and state the public narrative exclusion for v2; this is a surface restriction, not a new composer rule.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [8490, 8676); exact literal, with LF line endings.

Old text:

````text
* **No change to Reader v1 public contract.** Reader success remains **bands-only (numeric-free)**; no narrative text appears on Reader v1. (Style/tone live in **HDE-Copy Tonality**.)  
````

Replacement text:

````text
* **No change to Reader v1 public contract.** Reader success remains **bands-only (numeric-free)**; no narrative text appears on Reader v1. Reader v2 also remains **bands-only (numeric-free)** and carries no prompt, narrative key, or narrative text. (Style/tone live in **HDE-Copy Tonality**.)  
````

## RL-004

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# 1\) Purpose & Ground Rules`
- `## 1.3 Terminology & Posture`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Keep terminology aligned with both public Reader versions while retaining Aux and admin CLI as the narrative surfaces.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [17435, 17573); exact literal, with LF line endings.

Old text:

````text
**Public posture (numeric-free).** Reader v1 remains bands-only and narrative-free; narratives appear only via Aux and admin CLI preview.
````

Replacement text:

````text
**Public posture (numeric-free).** Reader v1 and Reader v2 remain bands-only and narrative-free; narratives appear only via Aux and admin CLI preview.
````

## RL-005

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# 3\) Composer Specification`
- `## 3.5 Suppression Policy — deterministic, conflict-only; pack rules allowed`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Extend the Reader non-narrative statement while preserving base eligibility and the entire suppression/can_emit contract.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [45551, 45701); exact literal, with LF line endings.

Old text:

````text
**Reader posture.** Reader v1 remains numeric-free and carries no narrative text; base Reader eligibility remains separate from narrative visibility.
````

Replacement text:

````text
**Reader posture.** Reader v1 and Reader v2 remain numeric-free and carry no narrative text; base Reader eligibility remains separate from narrative visibility.
````

## RL-006

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# **5\) Surfaces (titles-only)**`
- `## **5.1 Reader v1 Posture — bands-only; narrative-free**`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Resolve the future-only full Magic-10 exposure statement to approved Reader v2, retain the v1 contract and gates, and route public bytes to their verified PF05 home.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [82946, 84572); exact literal, with LF line endings.

Old text:

````text

**Posture (unchanged).**  
Reader v1 public JSON remains numeric-free (bands-only) and contains no narrative text. Narrative text appears only on the Aux narrative surface and in admin CLI preview.

**Numeric-output gate.** Numeric public output requires a separately approved PF05, PF17, schema, and narrative change.

This guide does not restate payload shapes or header matrices; it links by title only. Payload bytes live in **PF05 — CLI/API**; transport/A7 policy lives in **PF04 — Governance**; the bands-only Reader covenant is defined in **PF01 — Math Spec**.

**Band-change dependency.** A band change requires review of the affected PF05, PF17, PF18, schema, and copy contracts before public activation.

**Implications.**  
Reader v1 keeps its existing public contract (six-key, numeric-free success body). Any narrative-related exposure continues to route through Aux/CLI, not Reader v1.

**Public expansion gate.** Full ten-category public exposure requires a separate versioned PF05, schema, narrative, and product decision.

**A7 proof surface (route-only).**  
When Reader success routes are proven, proofs run only on a cataloged JSON success route (Endpoint Catalog, PF05). The Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod — capture a headers-only env-gate proof. `/internal/version` is ops-only and not A7-eligible.

**Routing (titles-only).**

* PF05 — CLI/API: declare Reader v1 narrative-free and define Aux/CLI behaviors.  
    
* PF04 — Governance: A7 (ETag/HEAD/304; writers/errors; ops exclusion).  
    
* PF01 — Math Spec: bands-only Reader covenant.

---

````

Replacement text:

````text

**Posture (unchanged).**  
Reader v1 and Reader v2 public JSON remain numeric-free (bands-only) and contain no prompt, narrative key, or narrative text. Narrative text appears only on the Aux narrative surface and in admin CLI preview.

**Numeric-output gate.** Numeric public output requires a separately approved PF05, PF17, schema, and narrative change.

This guide does not restate payload shapes or header matrices; it links by title only. Payload bytes live in **PF05 — CLI/API**; transport/A7 policy lives in **PF04 — Governance**; the bands-only Reader covenant is defined in **PF01 — Math Spec**.

**Band-change dependency.** A band change requires review of the affected PF05, PF17, PF18, schema, and copy contracts before public activation.

**Implications.**  
Reader v1 keeps its existing public contract (six-key, numeric-free success body). Any narrative-related exposure continues to route through Aux/CLI; neither Reader v1 nor Reader v2 carries narratives.

**Public expansion gate.** The separately approved versioned contract for full ten-category public exposure is Reader v2. Its category exposure adds no narrative surface or composer behavior. The existing composer, `can_emit`, Aux, CLI admin preview, and pack semantics remain unchanged. Reader v2 payload bytes, version selection, and transport are owned by **PF05-Canon-HDE-CLI-API-Vendor-Ref**; this guide does not restate them.

**A7 proof surface (route-only).**  
When Reader success routes are proven, proofs run only on a cataloged JSON success route (Endpoint Catalog, PF05). The Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod — capture a headers-only env-gate proof. `/internal/version` is ops-only and not A7-eligible.

**Routing (titles-only).**

* PF05-Canon-HDE-CLI-API-Vendor-Ref: define Reader v1/v2 public bytes and the existing Aux/CLI behaviors.  
    
* PF04 — Governance: A7 (ETag/HEAD/304; writers/errors; ops exclusion).  
    
* PF01 — Math Spec: bands-only Reader covenant.

---

````

## RL-007

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# **5\) Surfaces (titles-only)**`
- `## **5.2 Aux Narrative (text/plain) — 200 ok text; 200 suppressed empty body (no ETag) \[Canon\]**`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Align the Aux surface reminder with both Reader versions; all Aux bodies, headers, routes, evidence, and suppression behavior are retained.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [86282, 86389); exact literal, with LF line endings.

Old text:

````text
Reader v1 remains bands-only and narrative-free; Aux/CLI are the narrative surfaces. (Routing: PF01/PF05.)
````

Replacement text:

````text
Reader v1 and Reader v2 remain bands-only and narrative-free; Aux/CLI are the narrative surfaces. (Routing: PF01/PF05.)
````

## RL-008

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# **5\) Surfaces (titles-only)**`
- `## **5.3 CLI Admin Preview — admin-only; stdout equals emitter; sidecar ids-only \[Canon\]**`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Extend the preview/public separation to v2 without changing preview authorization, output bytes, or sidecars.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [87993, 88211); exact literal, with LF line endings.

Old text:

````text
* **Admin-only.** Access to narrative preview is restricted to authorized/admin contexts; public Reader v1 remains narrative-free. Narrative preview **must** use the same emitter as Aux and emit LF-terminated bytes.  
````

Replacement text:

````text
* **Admin-only.** Access to narrative preview is restricted to authorized/admin contexts; public Reader v1 and Reader v2 remain narrative-free. Narrative preview **must** use the same emitter as Aux and emit LF-terminated bytes.  
````

## RL-009

Change type: CANON_UPDATE.
Operation: REPLACE.
Target document: `PF17-Canon-HDE-Narratives-Guide`.
Original heading path:

- `# **8\) Security, Privacy & Ops (titles-only; \[Canon\])**`
- `### **8.1 Access control & privacy — admin-only preview; no PII in artifacts \[Canon\]**`

Source-ledger basis: T-PF17 / A23, C040-07 narrative/public boundary; A24 confirms delivery, S06/S07/S12 retain non-narrative ownership, C1 establishes exceptional closure.
Rationale: Keep the access-control reminder consistent with v2 while preserving the prohibition on public preview endpoints.
Expected literal old-block occurrence: 1; observed: 1.
Original character span: [100766, 100974); exact literal, with LF line endings.

Old text:

````text
**Admin scope.** Narrative preview is **restricted to authorized/admin** contexts; public **Reader v1 remains narrative-free** (bands-only). Preview endpoints **must not** appear on public Reader surfaces.  
````

Replacement text:

````text
**Admin scope.** Narrative preview is **restricted to authorized/admin** contexts; public **Reader v1 and Reader v2 remain narrative-free** (bands-only). Preview endpoints **must not** appear on public Reader surfaces.  
````

END OF REDLINES
