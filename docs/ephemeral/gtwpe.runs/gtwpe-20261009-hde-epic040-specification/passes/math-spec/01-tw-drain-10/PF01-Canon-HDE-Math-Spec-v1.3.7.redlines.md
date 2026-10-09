# Redlines — HDE Math Spec (PF01)

## Header

- Run: `gtwpe-20261009-hde-epic040-specification`
- Prompt: `TW-DRAIN-10 — Prepare PF Document Redlines — 100726.1` (Notion `3f24590a05eb81fc872ad0003ac03086`)
- Target (directory + versionless name): `docs/pfcanon/` → `HDE Math Spec`
- Target file: `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md`
- Target base blob: `ba07b5606153cadd033e41b1a8aafb967af10ea1`
- Target baseline SHA-256: `101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a`
- Preparation outcome: `READY`
- Save completeness: `COMPLETE_PACKAGE`

## Sources read whole

1. `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` — governing addenda `2.5` (C040-06), `2.23` (C040-07), `2.25` (C040-08).
2. `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`.
3. `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`.
4. `docs/ephemeral/gtwpe.runs/gtwpe-20261009-hde-epic040-specification/passes/triage/01-tw-triage-10/triage.md` (names the changes that bear on this target).
5. `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` (editorial standard).

Canon read from `origin/main` at intake `0c4dddece401c457b2429ddc9cb8f2e819b4a943`; `docs/pfcanon/` verified unchanged from that commit (target and sources byte-identical to intake). Working branch `docs/20261009-gtwpe-run-hde-epic040-specification`.

---

## Redline R1

- Redline number: `R1`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec`.
- Rationale: Section 2 now defines the public contract for both Reader versions.
- Section path: `# 2) Product Covenant & Public Contract`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]
````

### NEW (complete replacement)

````markdown
# 2\. Product Covenant & Public Contract (Reader v1 and v2) \[Required-Now\]
````

---

## Redline R2

- Redline number: `R2`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("Resolve every `future, versioned change` statement to Reader v2").
- Rationale: Resolve the "future, versioned change" statement to the delivered Reader v2.
- Section path: `# 2) Product Covenant & Public Contract` → `2.2 Category policy (v1)`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* No other public categories are allowed in v1. Exposure of the full Magic-10 set is a future, versioned change (PF-01 remains math-only; the public surface is constrained here).
````

### NEW (complete replacement)

````markdown
* No other public categories are allowed in v1. Exposure of the full Magic-10 set is a versioned public-contract change, delivered by Reader v2 (see §2.5). PF-01 remains math-only; the v1 public surface stays constrained to the single `harmony` item.
````
---

## Redline R3

- Redline number: `R3`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("Define the Reader v2 public projection alongside Reader v1 in §2").
- Rationale: Define the Reader v2 public projection (six keys, ten categories in canonical order, v1 unchanged) in a new §2.5 appended after §2.4.
- Section path: `# 2) Product Covenant & Public Contract` → `2.4 Ordering semantics` (append §2.5 after the closing paragraph)
- Action: `REPLACE ONCE` — replace the unique old block below with the same block followed by the new §2.5 subsection.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
EPIC017’s “deterministic tie-break and total-order module” deliverable, as recorded in **HDE Phased Epics Map**, is associated with comparator code and evidence intended to cover IDs, channels, categories, arrays-as-sets, antisymmetry, transitivity, totality, AB↔BA identity, and two-run identity. Static repository inspection confirms comparator definitions but does not establish execution or PASS. EPIC017 does **not** alter the ordering rules or arrays-as-sets behavior in this spec. Any future change to comparator policy or set semantics remains a PF01 math change and must follow the usual release-id and evidence requirements.
````

### NEW (complete replacement)

````markdown
EPIC017’s “deterministic tie-break and total-order module” deliverable, as recorded in **HDE Phased Epics Map**, is associated with comparator code and evidence intended to cover IDs, channels, categories, arrays-as-sets, antisymmetry, transitivity, totality, AB↔BA identity, and two-run identity. Static repository inspection confirms comparator definitions but does not establish execution or PASS. EPIC017 does **not** alter the ordering rules or arrays-as-sets behavior in this spec. Any future change to comparator policy or set semantics remains a PF01 math change and must follow the usual release-id and evidence requirements.

## **2.5 Reader v2 public projection (versioned) \[Required-Now\]**

**Definition (normative).** Reader v2 is a versioned public contract, selected by `v=2` on the production Reader route. Its request contract, read-only resolution, eligibility decision, transport, conditional delivery, and error behavior are those of the Reader v1 route (§§2.1–2.3); only `reader_version` and the public `categories` projection differ by version.

**Success payload (same six keys).** The Reader v2 success body has exactly the same six top-level keys as Reader v1 (§2.1): `reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`. `reader_version` is the fixed string `"v2"`. No other public field exists, and no field is numeric.

**Category policy (v2).**

* If `eligible == true`: `categories` contains **exactly ten** items, each exactly `{ "id", "band" }` with `band` in `Cool`/`Open`/`Warm`/`Glow`. There is one item for each Magic-10 identifier, in the canonical governed order of `catalog/magic10.json`: `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`. Each band is that category's band in the complete canonical intrinsic Magic-10 result (§§5.2–5.3). No category is omitted, duplicated, default-filled, substituted by `harmony`, or altered by viewer preferences.  
* In Reader v2, `categories` is an **ordered array in canonical governed order**, not a set-sorted array.  
* If `eligible == false`: `categories` **MUST** be `[]`.

**Determinism and identity.** Canonical JSON serialization (**PF12-Canon-HDE-Schemas-and-Artifacts** §4), the five-key idempotence preimage recipe (§3.2), AB↔BA identity, and two-run identity apply to Reader v2 bytes exactly as they apply to Reader v1.

**Reader v1 unchanged.** Reader v1 remains the bands-only, numeric-free, single-`harmony` contract of §2.2, selected by `v=1`.
````
---

## Redline R4

- Redline number: `R4`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("State the Reader v2 preimage").
- Rationale: State the Reader v2 five-key preimage as the shared recipe with `reader_version` `v2`.
- Section path: `# 3) Identity & Determinism` → `3.2 idempotence_hash: preimage recipe`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
Do not include `idempotence_hash` in the preimage.
````

### NEW (complete replacement)

````markdown
Do not include `idempotence_hash` in the preimage.

**Reader v2 preimage.** Reader v2 uses the same five-key preimage recipe with `reader_version : "v2"` and `categories` set to the complete ten-item v2 array in canonical governed order (§2.5); when `eligible == false`, `categories` is `[]`.
````

---

## Redline R5

- Redline number: `R5`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("emission rules per version in §4.4 and §4.7").
- Rationale: Per-version emission rule for the eligible case.
- Section path: `# 4) Eligibility` → `4.4 Public behavior`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **If `eligible == true`:** the public `categories` array **MUST** comply with §2.2 (v1 Alpha: exactly one item `{id:"harmony", band:…}`; numeric-free).  
````

### NEW (complete replacement)

````markdown
* **If `eligible == true`:** the public `categories` array **MUST** comply with the version's category policy — §2.2 (v1: exactly one item `{id:"harmony", band:…}`; numeric-free) or §2.5 (v2: exactly ten items in canonical governed order).  
````

---

## Redline R6

- Redline number: `R6`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec`.
- Rationale: Ineligible emission is identical across versions.
- Section path: `# 4) Eligibility` → `4.4 Public behavior`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **If `eligible == false`:** the public `categories` array **MUST** be `[]`. No numerics or narrative fields appear in either case.  
````

### NEW (complete replacement)

````markdown
* **If `eligible == false`:** the public `categories` array **MUST** be `[]` (both v1 and v2). No numerics or narrative fields appear in either case.  
````

---

## Redline R7

- Redline number: `R7`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("emission rules per version in §4.4 and §4.7").
- Rationale: Per-version emission rule for the eligible case.
- Section path: `# 4) Eligibility` → `4.7 Emission rule (binary)`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **Eligible ⇒** **emit categories** per §2.2 (v1 Alpha: exactly one item `{id:"harmony", band:…}`; numeric-free).  
````

### NEW (complete replacement)

````markdown
* **Eligible ⇒** **emit categories** per the version's policy — §2.2 (v1: exactly one item `{id:"harmony", band:…}`; numeric-free) or §2.5 (v2: exactly ten items in canonical governed order).  
````

---

## Redline R8

- Redline number: `R8`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec`.
- Rationale: Ineligible emission is identical across versions.
- Section path: `# 4) Eligibility` → `4.7 Emission rule (binary)`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **Ineligible ⇒** **`categories: []`** (empty array). No numerics, no narrative fields.
````

### NEW (complete replacement)

````markdown
* **Ineligible ⇒** **`categories: []`** (empty array, both v1 and v2). No numerics, no narrative fields.
````
---

## Redline R9

- Redline number: `R9`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("Resolve every `future, versioned change` statement to Reader v2, including §5.1").
- Rationale: Resolve the §5.1 "future, versioned change" statement and state the v2 projection.
- Section path: `# 5) Magic-10 Framework` → `5.1 Canonical IDs (closed set)`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **Public surface (v1):** Reader v1 is **bands-only & numeric-free** and projects only `{"id":"harmony","band":…}` from the complete canonical matrix (see **§2.2**). Public exposure of all ten categories remains a future, versioned change.
````

### NEW (complete replacement)

````markdown
* **Public surface (v1):** Reader v1 is **bands-only & numeric-free** and projects only `{"id":"harmony","band":…}` from the complete canonical matrix (see **§2.2**).  
* **Public surface (v2):** Reader v2 projects the complete ten-category matrix as ten `{id, band}` items in canonical governed order (see §2.5).
````

---

## Redline R10

- Redline number: `R10`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("the preset and pack-change statements").
- Rationale: Resolve the pack-change "future public exposure" statement to the delivered Reader v2.
- Section path: `# 5) Magic-10 Framework` → `5.4.4 Change policy`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
Changing governed pack bytes does not by itself change the Reader v1 public covenant. Reader v1 remains bands-only, numeric-free, and harmony-only unless a separately authorized public-contract version change widens it. Any future public exposure of the full ten-category matrix requires coordinated versioning without changing the current canonical calculation domain.
````

### NEW (complete replacement)

````markdown
Changing governed pack bytes does not by itself change the Reader public covenant. Reader v1 remains bands-only, numeric-free, and harmony-only; Reader v2 is the separately authorized public-contract version that exposes the full ten-category matrix (§2.5). Any further public exposure change requires coordinated versioning without changing the current canonical calculation domain.
````

---

## Redline R11

- Redline number: `R11`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("Resolve every `future, versioned change` statement to Reader v2").
- Rationale: Remove the "(future)" qualifier now that Reader v2 is delivered.
- Section path: `# 5) Magic-10 Framework` → `5.6 Resonance posture`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
> Note: Internal math exists; public exposure of the full 10-item array is **Reader v2** (future).
````

### NEW (complete replacement)

````markdown
> Note: Internal math exists; public exposure of the full 10-item array is **Reader v2** (§2.5).
````

---

## Redline R12

- Redline number: `R12`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("the §1 map").
- Rationale: The map at a glance reflects both Reader versions.
- Section path: `# 1) Map at a Glance` → `Public Reader v1`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **Public Reader v1 (bands-only, single “harmony”) — \[Required-Now\]**  
````

### NEW (complete replacement)

````markdown
* **Public Reader v1 (bands-only, single “harmony”) and Reader v2 (full Magic-10, bands-only) — \[Required-Now\]**  
````

---

## Redline R13

- Redline number: `R13`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("the §1 map").
- Rationale: The Magic-10 map bullet reflects Reader v2 exposure of all ten.
- Section path: `# 1) Map at a Glance` → `Canonical Magic-10`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **Canonical Magic-10 (10 categories; scores→bands) — \[Required-Now\] (implementation gap; Reader projection remains harmony-only)**  
````

### NEW (complete replacement)

````markdown
* **Canonical Magic-10 (10 categories; scores→bands) — \[Required-Now\] (implementation gap; Reader v1 projection remains harmony-only, Reader v2 exposes all ten)**  
````

---

## Redline R14

- Redline number: `R14`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("the §1 map").
- Rationale: Public projection reflects Reader v2.
- Section path: `# 1) Map at a Glance` → `Canonical Magic-10` → `Public projection`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
  * **Public projection.** Reader v1 exposes only the `harmony` band from the complete canonical matrix. It does not expose scores or the other nine categories.  
````

### NEW (complete replacement)

````markdown
  * **Public projection.** Reader v1 exposes only the `harmony` band from the complete canonical matrix; Reader v2 exposes all ten category bands (scores remain internal).  
````

---

## Redline R15

- Redline number: `R15`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("the preset ... statements").
- Rationale: The preset public rule reflects the authorized versioned contract (Reader v2).
- Section path: `# 1) Map at a Glance` → `Presets & aggregation math` → `Public rule`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
  * **Public rule.** A future preset must not silently widen Reader v1; the public projection remains numeric-free and harmony-only unless a separately authorized version change says otherwise.
````

### NEW (complete replacement)

````markdown
  * **Public rule.** A future preset must not silently widen Reader v1; Reader v1 remains numeric-free and harmony-only, while Reader v2 is the separately authorized version that exposes the full ten-category matrix (§2.5).
````
---

## Redline R16

- Redline number: `R16`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec` ("the preset ... statements").
- Rationale: The preset public boundary reflects Reader v2.
- Section path: `# 7) Presets & Configuration` → `7.4 Ownership and public boundary`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **Reader v1 boundary.** Reader v1 remains numeric-free and emits only `harmony`. That output is a projection from the complete canonical ten-category matrix; promotion cannot silently expose presets, scores, weights, tokens, other category bands, EM/HG records, or configuration details.
````

### NEW (complete replacement)

````markdown
* **Reader v1 boundary.** Reader v1 remains numeric-free and emits only `harmony`; Reader v2 emits all ten category bands (§2.5). Both are projections from the complete canonical ten-category matrix; promotion cannot silently expose presets, scores, weights, tokens, EM/HG records, or configuration details beyond those versioned public projections.
````

---

## Redline R17

- Redline number: `R17`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec`.
- Rationale: The aggregation public boundary reflects Reader v2.
- Section path: `# 8) Aggregation Algorithm` → `8.4 Ownership, handoff, and public boundary`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
Final category scores map to bands only through §5.3; this section does not define a second mapping or threshold table. Reader v1 remains numeric-free and emits only the `harmony` band as a projection from the complete canonical ten-category matrix. Promotion does not silently widen public output. Transport, HTTP, CLI stream, harness, and operational behavior remain in their owning documents.
````

### NEW (complete replacement)

````markdown
Final category scores map to bands only through §5.3; this section does not define a second mapping or threshold table. Reader v1 remains numeric-free and emits only the `harmony` band, and Reader v2 emits the ten category bands (§2.5), each as a projection from the complete canonical ten-category matrix. Promotion does not silently widen public output. Transport, HTTP, CLI stream, harness, and operational behavior remain in their owning documents.
````

---

## Redline R18

- Redline number: `R18`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.23` (C040-07), drainage row `PF01 — HDE Math Spec`.
- Rationale: Implementation note reflects the delivered Reader v2.
- Section path: `# 12) Implementation Notes` → `Ten-category compat internals`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
  * Reader v1 still emits only the `harmony` projection; full public Magic-10 exposure requires an authorized versioned contract (§2.2).
````

### NEW (complete replacement)

````markdown
  * Reader v1 still emits only the `harmony` projection; full public Magic-10 exposure is delivered by Reader v2 (§2.5).
````

---

## Redline R19

- Redline number: `R19`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.25` (C040-08).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.25` (C040-08), drainage note ("Canon drainage of C040-08 into PF01 §2.3").
- Rationale: The public error object now carries no numeric field (retry_after_ms removed).
- Section path: `# 2) Product Covenant & Public Contract` → `2.3 Errors`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
### **Typed public error object (no PII; bounded numeric exception)**
````

### NEW (complete replacement)

````markdown
### **Typed public error object (no PII; no numerics)**
````

---

## Redline R20

- Redline number: `R20`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.25` (C040-08).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.25` (C040-08), required delivery item 1 ("the error branch admits schema (const 'v1', required)") and closure ("The v1 error branch requires schema, ok, code and error. It has no retry_after_ms.").
- Rationale: Conform the §2.3 shape to the delivered four-key Reader v1 error envelope.
- Section path: `# 2) Product Covenant & Public Contract` → `2.3 Errors` → `Typed public error object`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
* **Shape (minimum):** the public error body is a typed JSON object with:  
  * `ok: false`  
  * `code: "<token>"` — short, machine-readable error token  
  * `error: "<non-PII message>"` — human-readable, non-secret message  
* **Optional field (when applicable):**  
  * `retry_after_ms: <integer >= 0>` — present only when a rate-limit or backoff condition applies  
* **No additional public fields** (no narratives, no keys, no numerics beyond `retry_after_ms`).
````

### NEW (complete replacement)

````markdown
* **Shape:** the public error body is a typed JSON object with exactly four keys:  
  * `ok: false`  
  * `code: "<token>"` — short, machine-readable error token  
  * `error: "<non-PII message>"` — human-readable, non-secret message  
  * `schema: "v1"` — fixed string, required  
* **No additional public fields** (no `details`, no `retry_after_ms`, no narratives, no keys, no numerics).
````

---

## Redline R21

- Redline number: `R21`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.25` (C040-08).
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.25` (C040-08), closure ("Real errors from POST /api/reader validate against the v1 schema").
- Rationale: The static posture note now reflects the conformed four-key envelope (schema required, retry_after_ms and details absent).
- Section path: `# 2) Product Covenant & Public Contract` → `2.3 Errors`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
**Static implementation posture.** The pinned `error_envelope` also emits `schema` and can emit `details`; neither field is permitted by this Reader error contract. Repository conformance remains an implementation gap.
````

### NEW (complete replacement)

````markdown
**Static implementation posture.** The Reader v1 error branch emits exactly `schema`, `ok`, `code`, and `error`, with `schema` const `"v1"`; `retry_after_ms` and `details` are not emitted and are not permitted by this Reader error contract.
````
---

## Redline R22

- Redline number: `R22`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.5` (C040-06), drainage table row `HDE-Math-Spec §§6.1–6.2` ("Existing-predicate sixteen-case conformance clarification ... route static taxonomy to its owning home").
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF01-Canon-HDE-Math-Spec`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.5` (C040-06), "Complete approved existing-state conformance oracle" and "Permanent drainage targets and owners".
- Rationale: Add the exhaustive sixteen-case existing-predicate conformance oracle (single Channel classification, normalized full-owner attribution, no independent hanging-Gate contribution) and route the static Channel taxonomy to its owning home (HDE-Schemas & Artifacts §2.1), by inserting it immediately before the §6.1 "Throat flags" heading.
- Section path: `# 6) Feature Extraction` → `6.1 Electromagnetics (EM)`
- Action: `REPLACE ONCE` — replace the unique old block below (the §6.1 "Throat flags" heading) with the new §6.1 conformance-oracle subsection followed by the same heading.
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
### **Throat flags (normative)**
````

### NEW (complete replacement)

````markdown
### **Existing-state conformance oracle (sixteen cases)**

For one fixed canonical Channel, each two-character presence string means the lower endpoint followed by the higher endpoint; `10` means only the lower endpoint and `01` means only the higher. This is not a Gate-mask serialization and does not create numeric scoring inputs.

| Case | A endpoints | B endpoints | State | Full-Channel owner before pair normalization |
| :---- | :---- | :---- | :---- | :---- |
| CS-01 | 00 | 00 | none | absent |
| CS-02 | 00 | 10 | none | absent |
| CS-03 | 00 | 01 | none | absent |
| CS-04 | 00 | 11 | dominance | B |
| CS-05 | 10 | 00 | none | absent |
| CS-06 | 10 | 10 | none | absent |
| CS-07 | 10 | 01 | electromagnetic | absent |
| CS-08 | 10 | 11 | compromise | B |
| CS-09 | 01 | 00 | none | absent |
| CS-10 | 01 | 10 | electromagnetic | absent |
| CS-11 | 01 | 01 | none | absent |
| CS-12 | 01 | 11 | compromise | B |
| CS-13 | 11 | 00 | dominance | A |
| CS-14 | 11 | 10 | compromise | A |
| CS-15 | 11 | 01 | compromise | A |
| CS-16 | 11 | 11 | companionship | absent |

Apply the existing §6.1 priority — `companionship`, `compromise`, `dominance`, `electromagnetic`, `none` — and translate the full-Channel owner to `member_lo`/`member_hi` only after intrinsic numeric Gate-mask ordering; the owner is absent in the other three states. Reversing A/B preserves the state and swaps the full-owner attribution where applicable.

Seven cases resolve to `none`, four to `compromise`, two to `dominance`, two to `electromagnetic`, and one to `companionship`. Same-end hanging Gates do not form an electromagnetic Channel; a unilateral hanging Gate does not add a score; and reciprocal opposite halves for the same Channel form one electromagnetic identity, not two contributions.

This table is an exhaustive conformance expansion of the existing §6.1 predicates, not new scoring mathematics. It is not evidence that the implementation has executed or passed the cases; the mathematical response assigned to a state remains solely the already-adopted configuration/profile contract. The Channel taxonomy itself (circuit/substream classification and the thirty-six-row assignment) is owned by HDE-Schemas & Artifacts §2.1 and is not restated here.

### **Throat flags (normative)**
````

END OF REDLINES
