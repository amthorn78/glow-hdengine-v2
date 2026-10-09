# T-PF01 exact redlines from v1.3.7

Run: `gtwpe-20261009-pf10-v13-5/T-PF01/from-v1.3.7`. Originating preparer: Codex /root, this Nathan-started T-PF01 document session; no stable conversation URL or provider session ID is exposed. Preparation: `READY`; save completeness is reported separately in the companion proof log.

Original: `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md` at `e7265a090ad0cc8de5f36de2f19481216aa3d073`; Git blob `ba07b5606153cadd033e41b1a8aafb967af10ea1`; raw UTF-8 SHA-256 `101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a`; 181867 bytes.

Control: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md` at `f057d124176143b3e02ba7ad599880fd7e9991b1`, row `T-PF01`; selected sources A05, A23–A26, A30, S01, S05, S07, S11–S12 and complete C1. Pinned preparation: TW-DRAIN-10 100926.1. Source boundaries and every disposition are in `redlines-PF01-from-v1.3.7.proof-log.md`. Apply owns document-control metadata; no header-control redline is supplied here.

Locations refer only to the unchanged original. A complete section ends immediately before the next same-or-higher-level heading outside fences. Payload labels, fences and the framing LF before a closing fence are not payload bytes: use each declared byte length, SHA-256 and final-LF flag. No payload has been normalized.

## RL-001

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 6728–7166 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A25`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Retire the superseded v1 emitter/schema gaps without changing the v1 covenant; bounded runtime, presenter and schema inspection corroborates the delivery record.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 438; SHA-256: `b7a1bdb31126ecc17ffdb4d4038ad89090e8b5a50fa9dc4251a1d975049d6861`; final LF: yes.

`````text
  * **Static implementation posture.** The pinned runtime emits the six-key envelope and computes the preimage hash, but it defaults `eligible` to `true`, retains the `harmony` item when `eligible == false`, and is not accepted by the checked-in success schema because that schema's category enum omits `harmony`. The schema and emitter also still permit `prompt`. These are implementation gaps; they do not weaken the public contract.  
`````

**NEW** — UTF-8 bytes: 314; SHA-256: `417a038e309c6408dc012a1c64353040c0ccaee6b7a79d1fc81829f65e376304`; final LF: yes.

`````text
  * **Static implementation posture.** The inspected runtime requires an explicit eligibility value and emits `[]` when it is false. The v1 success schema admits `harmony`, closes the six-key envelope and `{id,band}` items, and excludes `prompt`. These static definitions do not establish execution or acceptance.
`````

## RL-002

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 9425–9566 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The full intrinsic matrix is already Required-Now; the old harmony-only public summary no longer covers the separately approved Reader v2 projection.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 141; SHA-256: `b4e51ae12b480f15c74009184a32515e573f4d65331efd9a16e85ca6a0bd7ede`; final LF: yes.

`````text
* **Canonical Magic-10 (10 categories; scores→bands) — \[Required-Now\] (implementation gap; Reader projection remains harmony-only)**  
`````

**NEW** — UTF-8 bytes: 80; SHA-256: `5c7dcf5d0a9fef1158d9d5544cecad8e79f25c8cb527fb18f2e32ee0300ace99`; final LF: yes.

`````text
* **Canonical Magic-10 (10 categories; scores→bands) — \[Required-Now\]**  
`````

## RL-003

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 10505–10668 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Summarize the approved additional version without widening v1 or changing intrinsic math.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 163; SHA-256: `cbe99f52dc8b314803795b5634135c5c58984969abc20388288ebbf0288931c9`; final LF: yes.

`````text
  * **Public projection.** Reader v1 exposes only the `harmony` band from the complete canonical matrix. It does not expose scores or the other nine categories.  
`````

**NEW** — UTF-8 bytes: 221; SHA-256: `ee0de16a0d6e9900d57263fa4d844ba33d2b6d70ed11c0c6870e9de79ff5c824`; final LF: yes.

`````text
  * **Public projection.** Reader v1 exposes only the `harmony` band. Reader v2 exposes all ten bands in the governed Magic-10 order (§2.5). Both project the complete canonical matrix and expose no scores or narratives.
`````

## RL-004

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 10668–10972 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A24`, `A26`, `C1`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Retire the absence claim contradicted by the bounded core/runtime read; distinguish static code from supplied acceptance and closure history.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 304; SHA-256: `f51764b4a30d771a65d1ee0db2b382d597ca03b97a8763cc690dbc219b7eb95d`; final LF: yes.

`````text
  * **Static implementation posture.** The pinned repository contains three noncanonical or transitional scorer surfaces and no complete ten-category implementation in `engine.core.core`; exact upstream mechanics for every governed pair signal are also not found. These are explicit implementation gaps.
`````

**NEW** — UTF-8 bytes: 309; SHA-256: `5b021dfe100cdf1e3872471c1b825c704d41d8591faa1409bdf4964405f4e35b`; final LF: yes.

`````text
  * **Static implementation posture.** The inspected `engine.core.core` contains the pure ten-category computation, and the Reader runtime accepts its band projection. **HDE Build Notes** records the accepted delivery; current code presence alone establishes neither complete upstream conformance nor a PASS.
`````

## RL-005

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 12747–12941 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Resolve the future-version qualifier while retaining the Future-Promotion boundary.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 194; SHA-256: `58acd81a8d25cd841308677e56468408648474920d6b43d40ef78d162d6043f4`; final LF: yes.

`````text
  * **Public rule.** A future preset must not silently widen Reader v1; the public projection remains numeric-free and harmony-only unless a separately authorized version change says otherwise.
`````

**NEW** — UTF-8 bytes: 242; SHA-256: `bd6fa8b4db831f07f7ac1bda4c3779fb35cb1ce0372e463277e725415b9ef816`; final LF: yes.

`````text
  * **Public rule.** A future preset cannot widen either Reader covenant or expose configuration. Reader v1 remains harmony-only; Reader v2 follows §2.5. Both remain numeric-free. Approval of v2 does not promote presets or aggregation math.
`````

## RL-006

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 13711–13882 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Replace the superseded future-surface label with a routing reference; route syntax and operating policy remain outside PF01.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 171; SHA-256: `b58a5e73ccf94a00ec0c5fb72fd354e505a12436f26b94bc52040c978dd3a096`; final LF: yes.

`````text
  * **Production public Reader endpoint — \[Speculative\].** Future public surface; conditional delivery/headers owned in **HDE-CLI-API-Vendor Ref**/**HDE-Governance**.
`````

**NEW** — UTF-8 bytes: 242; SHA-256: `7ba5ab62317c91b38eca6f338bf2e90cb7bf3e62e93bf90e1e0dbf37823961a5`; final LF: yes.

`````text
  * **Production public Reader — \[Required-Now\].** Version selection, production routing and delivery behavior are owned in **HDE-CLI-API-Vendor Ref**/**HDE-Governance**. The public projections are constrained by §§2.1–2.2 and §2.5.
`````

## RL-007

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 13966–14210 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Prevent set sorting from overriding the v2 ordered array and retain the existing v1 CLI proof surface.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 244; SHA-256: `3a4e9992f9499d192974a50c31c8a9027fe8e0d4b896aa86e3906e08663c1660`; final LF: yes.

`````text
  * **One emitter for public bytes.** Reader and any CLI Reader-byte sidecar MUST call the same presenter/emitter; **no ad-hoc serializers**. Canonical JSON: UTF-8, sorted keys, compact, exactly one LF; arrays-as-sets (dedupe \+ ASCII sort).  
`````

**NEW** — UTF-8 bytes: 381; SHA-256: `529e0754851fbe31ad0554bf65486a58aa7b127678c130d4555ecaabf925aefc`; final LF: yes.

`````text
  * **One emitter for public bytes.** Reader and any designated CLI Reader-byte sidecar MUST call the same presenter/emitter; **no ad-hoc serializers**. Canonical JSON: UTF-8, sorted keys, compact, exactly one LF. Arrays-as-sets use their governed normalization; Reader v2 categories preserve the governed ordered sequence (§2.5). The existing CLI Reader-byte sidecar remains v1.
`````

## RL-008

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 15799–15997 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Carry the unchanged retired-field prohibition across both approved Reader versions.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 198; SHA-256: `18870a9fcdf88b19b3423038eff9c7b74af11b21bed7e09ce14808280217134d`; final LF: yes.

`````text
  * **Scope.** Public Reader v1 is required to be narrative-free; `prompt` and `uncertainty` are prohibited by §§2.1–2.2 and Appendix D. Repository conformance must be established separately.  
`````

**NEW** — UTF-8 bytes: 141; SHA-256: `8f953497c6b193d4d8f1bc97c03ade732d4f40c048bf441eaf2b7ecaf0df3684`; final LF: yes.

`````text
  * **Scope.** Public Reader v1 and v2 are narrative-free; `prompt` and `uncertainty` are prohibited by §§2.1–2.2, §2.5 and Appendix D.
`````

## RL-009

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 1\. “Map at a Glance” — What’s live vs planned \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 15997–16237 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A25`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Correct the superseded prompt-gap claim and retain error and CLI ownership.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 240; SHA-256: `ffe1f8faf9205dd60e84b3c15d9bfb1404d4f00927e41eece8dd1ae29dfa1262`; final LF: yes.

`````text
  * **Acceptance requirement.** Success bodies MUST pass the governing schema without `prompt`; error bodies remain typed and LF-terminated; Reader-sidecar parity goldens remain bands-only. The pinned schema and emitter do not yet conform.
`````

**NEW** — UTF-8 bytes: 371; SHA-256: `afb5923cbf95a88e0d1b2e9c6aaab8e7e14331fb5e827f14a615f7341b9e290f`; final LF: yes.

`````text
  * **Acceptance requirement.** Success bodies MUST pass the governing versioned schema without `prompt`; error bodies use the owned `error_v1` reference and canonical LF discipline; the existing CLI Reader-sidecar parity remains v1 and bands-only. The inspected schemas and presenter exclude the retired category fields; static inspection does not establish acceptance.
`````

## RL-010

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 16537–16606 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The approved v2 covenant belongs alongside the preserved v1 covenant in PF01 §2.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 69; SHA-256: `300bb5a65cb61323fde92cc289d908d5d7aef4a2819a507232018b56c79e9fde`; final LF: no.

`````text
# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]
`````

**NEW** — UTF-8 bytes: 76; SHA-256: `48e662bb080f6fda90235890589f738c822190500f8f302072ef7064e6788304`; final LF: no.

`````text
# 2\. Product Covenant & Public Contract (Reader v1 and v2) \[Required-Now\]
`````

## RL-011

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]`
- `## **2.1 Success payload (six keys; numeric-free) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 17055–17413 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A25`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Replace obsolete schema and presenter gap observations using the bounded baseline read, preserving all normative v1 key definitions.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 358; SHA-256: `92a02c92849b54cd56305f867c4937b0b0e616bbb867040cbaa1769d33495b00`; final LF: yes.

`````text
**Static implementation posture.** The pinned emitter constructs the six-key envelope and canonical preimage. The checked-in schema does not conform: its category enum omits `harmony`, it still permits `prompt`, and its success branch does not enforce the exact six-key field closure. This is an implementation gap; the normative covenant remains unchanged.
`````

**NEW** — UTF-8 bytes: 400; SHA-256: `40e7f8d7b97e8a4e2eac4654ddd3476c807e5eb5bc841e237c7d9356263c549e`; final LF: yes.

`````text
**Static implementation posture.** The inspected runtime and presenter construct the v1 six-key envelope and five-key preimage, enforce the public category-item keys, and emit no categories for ineligible pairs. The inspected v1 success schema closes the six top-level keys, admits only `harmony` in eligible v1 output, and excludes `prompt`. Static definitions do not prove execution or acceptance.
`````

## RL-012

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]`
- `## **2.2 Category policy (v1) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 19889–20068 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Resolve the explicit future-ten-category statement with the approved separate v2 contract.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 179; SHA-256: `8dc62e83b58c6f66373b70bee0dd507e01c596bd051ab6e92df9eab5f5dd04f9`; final LF: yes.

`````text
* No other public categories are allowed in v1. Exposure of the full Magic-10 set is a future, versioned change (PF-01 remains math-only; the public surface is constrained here).
`````

**NEW** — UTF-8 bytes: 149; SHA-256: `0deee8315c6e71c0fe56ce44c1446c12fe0eb9571bee9393e851a5b1f86ed4f5`; final LF: yes.

`````text
* No other public categories are allowed in v1. The separately approved Reader v2 projection is defined in §2.5; it does not alter the v1 covenant.
`````

## RL-013

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]`
- `## **2.2 Category policy (v1) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 21634–21883 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Retire the ineligible-category gap contradicted by the inspected runtime without asserting test passage.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 249; SHA-256: `b50a1e8da3ee3e20623a27941bbefffc8dc789b4721e27fcc1115bfa94d7d619`; final LF: yes.

`````text
**Static implementation posture.** The pinned runtime always constructs one `harmony` category even when the supplied `eligible` value is false. The required `eligible == false` ⇒ `categories: []` behavior is not implemented at the pinned commit.
`````

**NEW** — UTF-8 bytes: 274; SHA-256: `3ee86b72806efbbc7f981aa75bb672013f1f7350d0a84c42fbb94e45dc4a7e6c`; final LF: yes.

`````text
**Static implementation posture.** The inspected runtime emits one validated `harmony` item for eligible v1 output and `[]` for ineligible output. The presenter and success schema reject extra category fields. These static facts do not establish the acceptance gates above.
`````

## RL-014

Operation: `REPLACE`. Change type: `CANON_UPDATE`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]`
- `## **2.3 Errors (shape/pointers) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 21884–23288 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A25`, `A26`, `C1`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: C040-08 replaces PF01’s conflicting local shape with an error_v1 owner reference; success contracts and math remain unchanged.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 1404; SHA-256: `4857d7f012be51867314776a1390ab38ddcf984f84d8becb747c0a6969ddf64e`; final LF: yes.

`````text
## **2.3 Errors (shape/pointers) \[Required-Now\]**

### **Typed public error object (no PII; bounded numeric exception)**

* **Shape (minimum):** the public error body is a typed JSON object with:  
  * `ok: false`  
  * `code: "<token>"` — short, machine-readable error token  
  * `error: "<non-PII message>"` — human-readable, non-secret message  
* **Optional field (when applicable):**  
  * `retry_after_ms: <integer >= 0>` — present only when a rate-limit or backoff condition applies  
* **No additional public fields** (no narratives, no keys, no numerics beyond `retry_after_ms`).

### **Hygiene and guardrails**

* **No PII or secrets** in error messages; keep messages succinct and generic.  
* **Determinism:** error bodies are serialized by the same canonical path as success (**PF12-Canon-HDE-Schemas-and-Artifacts** §4): UTF-8, sorted keys, compact separators, exactly one trailing LF.

**Static implementation posture.** The pinned `error_envelope` also emits `schema` and can emit `details`; neither field is permitted by this Reader error contract. Repository conformance remains an implementation gap.

### **Pointers (transport & status live elsewhere)**

* **Transport ownership:** HTTP status mapping, headers, conditional delivery, caching, and streams/exit codes are owned by **HDE-CLI-API-Vendor-Ref** and **HDE-Governance** and are referenced here by title only.

---

`````

**NEW** — UTF-8 bytes: 1324; SHA-256: `4bed5322994bd767b512c7563598c97a066ee5d55674b52913a50472d8db0dec`; final LF: yes.

`````text
## **2.3 Errors (shape/pointers) \[Required-Now\]**

Reader v1 and v2 failures use the governed `error_v1` contract. Its exact schema, token/message pairs, status mapping and failure projection are owned by **HDE-CLI-API-Vendor-Ref**, **HDE-Governance** and **PF12-Canon-HDE-Schemas-and-Artifacts**. PF01 does not define a second error shape or taxonomy. The former PF01 minimum-field shape and optional retry-field exception are superseded by that owned reference.

Invalid or missing input MUST fail closed and MUST NOT be converted to an ineligible success. Public failure projection exposes no PII, secrets, Gate payloads, internal diagnostics, scores or narrative output. Error bytes use the same canonical JSON and single-LF discipline as success; this does not turn an error into a Reader success envelope or change its identity recipe.

**Static implementation posture.** The inspected Reader failure function calls `error_envelope` without diagnostics and emits the governed `error_v1` fields; both inspected Reader schemas admit that error branch. The shared helper can add `details` for other callers, which does not authorize diagnostics on Reader failures. This corroborates the recorded error-schema correction in **HDE Build Notes**; it does not establish execution, transport acceptance or deployment.

---

`````

## RL-015

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]`
- `## **2.4 Ordering semantics (comparators) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 24027–24269 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `S05`, `S07`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The selected sources distinguish ordered collections from sets and reject raw duplicates; existing set rules must not repair or reorder v2 categories.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 242; SHA-256: `1b5374677d66b1e00262773c473e0d26a02aedc45c99909bfb0ac484254e70a4`; final LF: yes.

`````text
**Set semantics (arrays-as-sets).** Any array that represents a set **MUST** be deduplicated and ASCII-sorted before hashing/compare (see **PF12-Canon-HDE-Schemas-and-Artifacts §4**). Non-canonical or duplicate elements **fail validation**.
`````

**NEW** — UTF-8 bytes: 467; SHA-256: `3e024f5ff851a02d083566acee31370cb47b0d4725deb146b7b05eff853fd419`; final LF: yes.

`````text
**Set semantics (arrays-as-sets).** Any array that represents a set **MUST** use its owning deduplication and ASCII-sort contract before hashing/compare (see **PF12-Canon-HDE-Schemas-and-Artifacts §4**). Non-canonical or duplicate elements **fail validation**. Reader v2 `categories` is an ordered array, not an array-as-set: preserve the governed sequence in §2.5 without deduplication or ASCII reordering. Duplicate, missing or out-of-order v2 items fail closed.
`````

## RL-016

Operation: `INSERT`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 2\. Product Covenant & Public Contract (Reader v1) \[Required-Now\]`
- `## **2.4 Ordering semantics (comparators) \[Required-Now\]**`

Original scope: whole PF01; sibling-section gap after original §2.4 and before original §3. Supporting raw UTF-8 offset: 26275 (gap). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `C1`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Add the complete approved C040-07 covenant: six keys, ten ordered bands or [], unchanged math/eligibility/privacy, versioned preimage, and explicit owner/CLI boundaries.

Action: `INSERT ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**BEFORE** — UTF-8 bytes: 240; SHA-256: `448be2ada17dc33b7a5de9815fb3ef6d06078542cb04abdbe7978138ee9cd676`; final LF: yes.

`````text
EPIC017 does **not** alter the ordering rules or arrays-as-sets behavior in this spec. Any future change to comparator policy or set semantics remains a PF01 math change and must follow the usual release-id and evidence requirements.

---

`````

**AFTER** — UTF-8 bytes: 46; SHA-256: `b52b59c4cc3d6a1c09067c771db334cccf3f0a2257f4b95bceaf17e543504c1f`; final LF: yes.

`````text
# 3\. Identity & Determinism \[Required-Now\]
`````

**INSERTED** — UTF-8 bytes: 2634; SHA-256: `2a40e4bb00d8287a7094f6b062aa4ac21e2db15009460ca536c3a0ecb5a39544`; final LF: yes.

`````text
## 2.5 Reader v2 public projection \[Required-Now\]

**Versioned covenant.** Reader v2 is a separate public projection of the same complete canonical Magic-10 result. Reader v1 remains exactly as defined in §§2.1–2.2. V2 introduces no score, formula, response profile, cap, rounding, band threshold, eligibility predicate or intrinsic identity change.

**Success envelope.** The body contains exactly the six top-level keys `reader_version`, `eligible`, `categories`, `meta`, `release_id` and `idempotence_hash`. `reader_version` is exactly `"v2"`. `eligible` is the §4 boolean; `meta` is exactly `{engine_tag,invocation_tag}` with the same non-empty string contract as v1; both hashes retain the lowercase 64-hex contract in §3. No extra top-level or metadata fields are allowed.

**Eligible projection.** When `eligible == true`, `categories` MUST contain exactly one `{id,band}` item for every governed Magic-10 identifier, in the exact frozen iteration order of `catalog/magic10.json` owned by **PF12-Canon-HDE-Schemas-and-Artifacts**. Every band is the corresponding result of the complete canonical matrix and is one of `Cool`, `Open`, `Warm` or `Glow`. This ten-item array is ordered, not a set: do not ASCII-sort, deduplicate, omit, duplicate, default-fill, substitute `harmony`, or rescore through viewer preferences. An incomplete or invalid result fails closed rather than producing a partial success.

**Ineligible projection.** When `eligible == false`, `categories` MUST be `[]`. The eligibility predicate and invalid-input refusal are unchanged from §4; ineligibility does not authorize a numeric, narrative or substitute result.

**Privacy and identity.** Category items contain only `id` and `band`. Scores, percentages, counts, weights, prompts, uncertainty, personal/shared keys and other narrative fields remain prohibited. The five-key preimage in §3.2 contains the selected `"v2"` version and this exact ordered category array, excludes `idempotence_hash`, and uses the same canonical serialization/hash/final-emission recipe as v1. AB↔BA and two-run identity apply within the selected Reader version (§3.4).

**Routing.** This section defines the public projection only. Version selection, requests, production routes, transport, conditional delivery and the shared `error_v1` reference remain in **HDE-CLI-API-Vendor-Ref**/**HDE-Governance**; schemas, the catalog sequence and evidence bindings remain in **PF12-Canon-HDE-Schemas-and-Artifacts**. Existing CLI Reader-byte parity stays v1. Approval of v2 creates no CLI flag, v2 CLI parity family, preset promotion or public numeric exception.

---

`````

## RL-017

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.1 release\_id — freeze-pack identity (sha256) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 30155–30299 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The approved v2 six-key envelope inherits the existing release identity contract.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 144; SHA-256: `a0455c463323d0a44077b4a889e4c9476ca1779fe2a05ab31adc546091bf8dea`; final LF: yes.

`````text
* `release_id` is included in the Reader v1 success body and participates in acceptance checks (see §2, §3.4; Governance A-gates by title).  
`````

**NEW** — UTF-8 bytes: 176; SHA-256: `8d6233c20c8f4e3c366a1b4fab145ec5c8c3a5e64de57d841b02b9f0cd1a494b`; final LF: yes.

`````text
* `release_id` is included in Reader v1 and v2 success bodies and participates in their five-key preimages and acceptance checks (see §2, §3.4; Governance A-gates by title).
`````

## RL-018

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.1 release\_id — freeze-pack identity (sha256) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 30976–31460 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A24`, `A25`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Reconcile the obsolete eight-member identity observation with the actual manifest and source-recorded release lineage; do not copy the complete manifest catalog or infer acceptance.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 484; SHA-256: `c8e5877de177ab6c52a164bec8d3ea9499d6f2009f4d89beaccfe3dd258c0b54`; final LF: yes.

`````text
**Static implementation posture.** The pinned runtime validates and hashes the canonical packaged manifest. The pinned manifest has eight entries, omits required topology and complete Magic-10 narrative inputs named by the current PF12 minimum, and therefore does not establish manifest conformance or a PASS. Its inclusion of adapter and migration bytes is consistent with PF12 ownership of the complete release surface and disproves only the former PF01 math-only membership claim.
`````

**NEW** — UTF-8 bytes: 475; SHA-256: `977f3680e3511099e1f65bef8f42faa1b97cdc046e2a3433c8955c1321b0cce6`; final LF: yes.

`````text
**Static implementation posture.** The inspected runtime validates and hashes the canonical packaged manifest. The inspected manifest records version `1.3.0` and 45 members, including the Reader v2 schema and the corrected v1 schema; **HDE Build Notes** records the successive release cuts. These facts replace the earlier eight-member observation. Full member integrity, manifest conformance, deployment and acceptance are not established by this bounded static inspection.
`````

## RL-019

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.2 idempotence\_hash: preimage recipe (sha256 over canonical preimage) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 31974–32196 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Extend the existing Reader hash recipe to the separately approved v2 projection.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 222; SHA-256: `91508a1487ab213bd7204afb0d2a951da3103c3f46620ffe852d080a9147cfa5`; final LF: yes.

`````text
**Definition (normative).** `idempotence_hash` is the lowercase 64-hex SHA-256 of the canonical preimage of the Reader v1 success envelope. It proves that the published bytes arise from a single, canonical representation.
`````

**NEW** — UTF-8 bytes: 246; SHA-256: `2fe11d5595daf3612884430fa260ef395a33b58a8d7cac00d43d07b283720336`; final LF: yes.

`````text
**Definition (normative).** `idempotence_hash` is the lowercase 64-hex SHA-256 of the canonical five-key preimage of the selected Reader v1 or v2 success envelope. It proves that the published bytes arise from a single, canonical representation.
`````

## RL-020

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.2 idempotence\_hash: preimage recipe (sha256 over canonical preimage) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 32377–32408 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The selected version is part of the five-key preimage, not an omitted transport-only selector.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 31; SHA-256: `43dc78c8ffa4e128a874d853dcc0fc09ad7ca223c748de592fc3fc81027f121c`; final LF: yes.

`````text
1. `reader_version` : `"v1"`  
`````

**NEW** — UTF-8 bytes: 88; SHA-256: `cec055f47c43e0c68fc7b10cf532ea3a814ba47642d96dd6700991925b7bf438`; final LF: yes.

`````text
1. `reader_version` : `"v1"` or `"v2"`, exactly the selected success-envelope version  
`````

## RL-021

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.2 idempotence\_hash: preimage recipe (sha256 over canonical preimage) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 32438–32643 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Bind the hash to the exact version-specific category projection without changing v1.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 205; SHA-256: `f99037b215d33cb8c6909c5e1e640a921443877f145353243d481b1fd269e0a9`; final LF: yes.

`````text
3. `categories` : `[{"id","band"}]` — public policy per §2.2 (v1 exposes one item `{"id":"harmony","band":<Cool|Open|Warm|Glow>}` when `eligible == true`; `[]` when `eligible == false`; numeric-free)  
`````

**NEW** — UTF-8 bytes: 223; SHA-256: `cd7e3d578f4e387e193b913cff6ff6492f292f7ece7702774084a947e547fbb1`; final LF: yes.

`````text
3. `categories` : `[{"id","band"}]` — §2.2 for v1 (one `harmony` item when eligible); §2.5 for v2 (all ten items in the exact governed order when eligible); `[]` when ineligible in either version; always numeric-free  
`````

## RL-022

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.2 idempotence\_hash: preimage recipe (sha256 over canonical preimage) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 33512–33754 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The same byte recipe preserves ordered v2 categories; general set normalization is not an alternative preimage.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 242; SHA-256: `d31eacc218803f6a5f2e3795433c95935909345cb737d14dd4b4703da09e467f`; final LF: yes.

`````text
Use **PF12-Canon-HDE-Schemas-and-Artifacts** rules: UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays that represent sets are deduplicated and ASCII-sorted. All byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
`````

**NEW** — UTF-8 bytes: 362; SHA-256: `ab005fd9bd38de57ff4d433eadb5bb899d715cad44c0c9ca3a11a2f0afb20294`; final LF: yes.

`````text
Use **PF12-Canon-HDE-Schemas-and-Artifacts** rules: UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF. Arrays that represent sets use their owning normalization; Reader v2 `categories` preserves the exact governed ordered sequence (§2.5) and is never ASCII-reordered or deduplicated. All byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
`````

## RL-023

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.2 idempotence\_hash: preimage recipe (sha256 over canonical preimage) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 34629–34905 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Preserve the existing v1-only CLI proof surface rather than silently extending it to v2.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 276; SHA-256: `0bffaa1d07e48ff17c2bae2f77c31b088daf87101c0e9ba05c3c147b28235d68`; final LF: yes.

`````text
* **Reader↔CLI parity.** For identical inputs and environment, a CLI Reader-byte sidecar and Reader MUST emit byte-identical success bodies and the same `idempotence_hash`. The general `showcompat` stdout payload is a different admin/compat surface and is not Reader bytes.
`````

**NEW** — UTF-8 bytes: 329; SHA-256: `aa11f5ee1d94773909f2ea6da2992cdd5c3a8777736d11585cec09976595491a`; final LF: yes.

`````text
* **Reader↔CLI parity (v1).** For identical inputs and environment, the existing CLI Reader-byte sidecar and Reader v1 MUST emit byte-identical success bodies and the same `idempotence_hash`. General `showcompat` stdout is a different admin/compat surface. Reader v2 approval does not create a v2 CLI parity surface or family.
`````

## RL-024

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.2 idempotence\_hash: preimage recipe (sha256 over canonical preimage) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 35566–35893 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Reconcile the old ineligible/prompt gaps and describe the inspected shared identity implementation without claiming PASS.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 327; SHA-256: `623e84a3d1c7e206f73258f11928d4b0e443456442ef5a26f0e31c516121c7f9`; final LF: yes.

`````text
**Static implementation posture.** The pinned presenter implements the five-key preimage, canonical hash, and final emission sequence. Complete public conformance remains blocked in code by the ineligible-category and `prompt` gaps identified in §§2.1–2.2; static inspection does not establish the acceptance tokens above.
`````

**NEW** — UTF-8 bytes: 439; SHA-256: `53d0f6007563ae78d6060f1468dc535f92fdef7200ffd037aa185a6923b8c3a4`; final LF: yes.

`````text
**Static implementation posture.** The inspected presenter has separate v1 and v2 preimage builders and one shared hash/final-emission function. The v2 builder preserves the governed category sequence; both exclude `idempotence_hash` from the preimage and reject extra category fields. The inspected runtime supplies the version-specific eligible or empty projection. These static definitions do not establish the acceptance tokens above.
`````

## RL-025

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.4 Two-run identity & AB↔BA parity (public) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 38030–38228 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Identity compares outputs under one selected version, not v1 against v2.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 198; SHA-256: `1a9475dd6fcb40e1979b55c7062a669d877cefb29c6ade25fc9afe5ce8c7a25e`; final LF: yes.

`````text
* **Two-run identity.** Serializing the same logical success envelope twice (same inputs, same environment, same `invocation_tag`, same `release_id`) **MUST** produce byte-identical public bytes.  
`````

**NEW** — UTF-8 bytes: 211; SHA-256: `749bfd7024c066b839fb22d2f001901e29ca82e7887188ca2a88f21e67626de1`; final LF: yes.

`````text
* **Two-run identity.** Serializing the same logical success envelope twice (same inputs, selected Reader version, environment, `invocation_tag` and `release_id`) **MUST** produce byte-identical public bytes.  
`````

## RL-026

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.4 Two-run identity & AB↔BA parity (public) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 38228–38371 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: State the inherited AB/BA predicate separately for each version.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 143; SHA-256: `b15ce2f418637d84f574ed63c14cdd7ce8f4db5ca0b9fe4a9d18276008241cc1`; final LF: yes.

`````text
* **AB↔BA parity.** For a given pair of **normalized** inputs, swapping input order (AB vs BA) **MUST** produce byte-identical public bytes.
`````

**NEW** — UTF-8 bytes: 182; SHA-256: `87943b2fcf6646a656b8b6fcbc906e6503588c7666ba78f286ab892056241d47`; final LF: yes.

`````text
* **AB↔BA parity.** For a given pair of **normalized** inputs and the same selected Reader version, swapping input order (AB vs BA) **MUST** produce byte-identical public bytes.  
`````

## RL-027

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.4 Two-run identity & AB↔BA parity (public) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 38751–38922 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Retain a single byte recipe while bounding CLI parity and v2 array order.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 171; SHA-256: `ae40bcc834366ca3201597b5d41dc60cfea25b4aaf082bd8e4e44cdd9abda373`; final LF: yes.

`````text
* **Single emitter.** One canonical JSON emitter shared across Reader and CLI (UTF-8, sorted keys, compact, exactly one LF) eliminates serializer drift across surfaces.  
`````

**NEW** — UTF-8 bytes: 265; SHA-256: `3eb744ce3016099ba84f0c1e376138865fd05736e3d5ef9e1073cb2cdb674b25`; final LF: yes.

`````text
* **Single emitter.** The canonical presenter/emitter and JSON recipe (UTF-8, sorted keys, compact, exactly one LF) serve both Reader versions. Existing corresponding CLI Reader-byte parity remains v1. V2 category order is preserved before serialization (§2.5).  
`````

## RL-028

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 3\. Identity & Determinism \[Required-Now\]`
- `## **3.4 Two-run identity & AB↔BA parity (public) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 40078–40451 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Retire the superseded schema/ineligible gaps and preserve the actual CLI version boundary confirmed by direct inspection.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 373; SHA-256: `7fa0020e8120fd00d4cb33ef78c0acad9a029efee2b3495bafe6638579774297`; final LF: yes.

`````text
**Static implementation posture.** The pinned canonical serializer and Reader presenter are deterministic by inspection, and the CLI can write Reader bytes through `--dump-reader`. General `showcompat` stdout emits a different compat object; the checked-in Reader schema and ineligible behavior are nonconforming; and static files do not prove any test or acceptance PASS.
`````

**NEW** — UTF-8 bytes: 367; SHA-256: `8bb0dea66f18aeb4c42c2774db40f196ace1309e478007082d2542f2ff6bd6a7`; final LF: yes.

`````text
**Static implementation posture.** The inspected Reader runtime and presenter contain the versioned projections and shared preimage/hash/final-emission recipe. The inspected CLI `--dump-reader` call uses the default v1 projection; general `showcompat` stdout remains a different compat object. Static definitions do not prove byte parity, test passage or acceptance.
`````

## RL-029

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **4\. Eligibility (mechanical; no numerics) \[Required-Now\]**`
- `## 4.4 Public behavior`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 45205–45364 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Version the public projection while preserving the already represented eligibility predicate.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 159; SHA-256: `c20ce0bc3026513856629179bd10ea666265da826257ab4b91fc8dee25570ca4`; final LF: yes.

`````text
* **If `eligible == true`:** the public `categories` array **MUST** comply with §2.2 (v1 Alpha: exactly one item `{id:"harmony", band:…}`; numeric-free).  
`````

**NEW** — UTF-8 bytes: 240; SHA-256: `b5ec91d24395fa576135395dd84f181ad931ba14937e8e615428d0fafb0de2fb`; final LF: yes.

`````text
* **If `eligible == true`:** the public `categories` array **MUST** comply with the selected version: §2.2 for v1 (exactly one `harmony` band item), or §2.5 for v2 (all ten band items in the exact governed order); numeric-free in both.  
`````

## RL-030

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **4\. Eligibility (mechanical; no numerics) \[Required-Now\]**`
- `## 4.5 Validation (binary)`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 46307–46467 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The new v2 projection inherits eligibility and preimage coupling.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 160; SHA-256: `271256ee04f9365cce980a6253ad1162fe9a3a4f839471ebdad1654c78e6bf97`; final LF: yes.

`````text
* **Schema coupling:** the success envelope reflects eligibility as per §2.1; the value participates in the **preimage** for `idempotence_hash` (see §3.2).  
`````

**NEW** — UTF-8 bytes: 182; SHA-256: `0c031464fad8eb02b39f1cce8640afd7cc4ead9a2871772b8f38d237b0131aba`; final LF: yes.

`````text
* **Schema coupling:** the success envelope reflects eligibility under §2.1 for v1 or §2.5 for v2; the value participates in the **preimage** for `idempotence_hash` (see §3.2).  
`````

## RL-031

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **4\. Eligibility (mechanical; no numerics) \[Required-Now\]**`
- `## 4.7 Emission rule (binary) \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 47698–47820 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Add the approved v2 emission rule without changing eligible/invalid classification.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 122; SHA-256: `c3b154f0f5aeabaeb67d7abe6fd43507beb25b1e38fcdda4209b256db0863a05`; final LF: yes.

`````text
* **Eligible ⇒** **emit categories** per §2.2 (v1 Alpha: exactly one item `{id:"harmony", band:…}`; numeric-free).  
`````

**NEW** — UTF-8 bytes: 203; SHA-256: `6ef63298f1364b6e59ddf6c1e6eef54d63e792cb1f6aa76b087c699220ae37b9`; final LF: yes.

`````text
* **Eligible ⇒** **emit categories** per the selected version: §2.2 for v1 (exactly one `harmony` band item), or §2.5 for v2 (all ten band items in the exact governed order); numeric-free in both.  
`````

## RL-032

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **4\. Eligibility (mechanical; no numerics) \[Required-Now\]**`
- `## 4.7 Emission rule (binary) \[Required-Now\]`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 47917–48362 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A24`, `A26`, `C1`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Remove the obsolete absence/default-true claim using bounded compute/runtime inspection; preserve the source’s live-readiness limitation.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 445; SHA-256: `b2b6bbbbe77b3f456b7cb156975db8e9778e2b259dc43267149f483f94209086`; final LF: yes.

`````text
**Static implementation posture.** No Reader eligibility decision function implementing this contract was found in the pinned repository. `engine.runtime.public` accepts a caller-supplied boolean, defaults it to `true`, and emits `harmony` even when false. The sampler has a separate candidate-pool predicate and MUST NOT be reused as Reader pair-computability. This is an explicit implementation gap, not a change to the Required-Now contract.
`````

**NEW** — UTF-8 bytes: 485; SHA-256: `24ac06c98131e5452b0dffcc5ab6bff372b0faaa40c55f3ad360e38123883fcc`; final LF: yes.

`````text
**Static implementation posture.** The inspected `engine.compat.compute` validates normalized parties and decides self-pair eligibility before intrinsic computation. The inspected Reader runtime requires an explicit eligibility result and emits the version-specific categories or `[]`. A sampler candidate-pool predicate remains a separate concern and MUST NOT substitute for Reader pair-computability. Code presence does not establish current-row readiness, deployment or acceptance.
`````

## RL-033

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.1 Canonical IDs (closed set) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 49082–49326 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Resolve the remaining future-full-public-array statement at the closed-ID framework boundary.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 244; SHA-256: `bc53ed7c8e87ffd61896e84540630464137248fea28ea4405833abfd2aabe66a`; final LF: yes.

`````text
* **Public surface (v1):** Reader v1 is **bands-only & numeric-free** and projects only `{"id":"harmony","band":…}` from the complete canonical matrix (see **§2.2**). Public exposure of all ten categories remains a future, versioned change.
`````

**NEW** — UTF-8 bytes: 287; SHA-256: `334dbc2cbcde85583ba1c347016621aec808884cbb08f9d23cd7415c848bac4b`; final LF: yes.

`````text
* **Public surfaces:** Reader v1 is **bands-only & numeric-free** and projects only `{"id":"harmony","band":…}` (§2.2). Reader v2 projects the complete ten-category band array in the governed order (§2.5), with no scores or narratives. Both use the same complete canonical matrix.  
`````

## RL-034

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.2 Deterministic integer scoring model (caps; fixed-point rules)**`
- `### **5.2.9 Routing (no transport bytes here)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 70629–71089 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Correct the old core-absence/admin-only routing claim without modifying any signal, response profile, reducer or numeric rule.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 460; SHA-256: `dc7f45ac95ddf84d202005de8e2f544279be15cb9b818108c89c4493b4a8ed94`; final LF: yes.

`````text
Math only. Public presentation remains the §2 harmony-only, numeric-free projection; transport bytes live in their owning transport canon. `engine.core.core` is the canonical compatibility behavior home. The pinned `engine.compat.ts_v0` path is transitional, `engine.compat.compute` is admin-only, and `engine.magic10.calculators` is transitional. No pinned `engine.core.core` function implements this complete recipe; this is an explicit implementation gap.
`````

**NEW** — UTF-8 bytes: 496; SHA-256: `ff1a1e7ec84f7e754f1d2bbec9b5d3b887e884dabb75e8b2e2406580d29c81c6`; final LF: yes.

`````text
Math only. Reader v1 remains the harmony-only, numeric-free projection; Reader v2 follows §2.5. Transport bytes live in their owning transport canon. `engine.core.core` remains the canonical compatibility behavior home. The inspected core contains the ten-category integer computation; `engine.compat.compute` validates parties and invokes that core before projection. Transitional helpers do not create an alternative mathematical authority, and static definitions do not establish acceptance.
`````

## RL-035

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.4 Manifests and freeze-pack coupling (change ⇒ new `release_id`)**`
- `### **5.4.3 Canonical manifest (construction rules)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 83853–84190 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A24`, `A25`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Reconcile release identity with the inspected manifest and the source-recorded v2/error release cuts, preserving PF12 membership ownership.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 337; SHA-256: `87addcfc9562437ac4f6f7bb5fb1a3c3095ab6c281d72b994f944f355231d8b4`; final LF: yes.

`````text
**Static implementation posture.** The pinned manifest is canonical and the runtime hashes it, but the manifest has eight entries and omits current PF12-required topology and complete Magic-10 narrative members. Its bytes and runtime definition do not establish complete manifest conformance, validation PASS, deployment, or acceptance.
`````

**NEW** — UTF-8 bytes: 363; SHA-256: `7a5330af7eb2605ec7eb74d50bb4a5ffc124695ac0dbef76f832ff51fc9478dc`; final LF: yes.

`````text
**Static implementation posture.** The inspected canonical manifest records release version `1.3.0` with 45 members, including both Reader schemas. Its bytes replace the earlier eight-entry observation; full member integrity and manifest conformance require their owning validation. Static manifest presence and hashing do not establish deployment or acceptance.
`````

## RL-036

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.4 Manifests and freeze-pack coupling (change ⇒ new `release_id`)**`
- `### **5.4.6 Validation (binary)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 86376–86540 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A24`, `A25`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Do not retain the superseded eight-member-based gap or infer full pack conformance from static bytes.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 164; SHA-256: `62576f99dda4b3de9e3c26dd8536b2f9551b2a4337d3b6e7afba0e1844bcaaba`; final LF: yes.

`````text
* **Current gap.** The pinned manifest does not yet demonstrate required closure for PF01 topology, complete Magic-10, constants, and direct-Motor→Throat inputs.
`````

**NEW** — UTF-8 bytes: 242; SHA-256: `7a7ee5be35c9214f08958da8c356e15038b2bff219d3a0bea2f11aac03d33f52`; final LF: yes.

`````text
* **Current verification limit.** The inspected manifest contains the versioned Reader schema members, but this bounded documentation inspection does not execute or establish every closure, member-integrity or release-acceptance predicate.  
`````

## RL-037

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.4 Manifests and freeze-pack coupling (change ⇒ new `release_id`)**`
- `### **5.4.7 Backwards-compatibility posture**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 86588–86958 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Resolve the pack section’s future-version wording while preserving v1 and math/input coupling.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 370; SHA-256: `189a5bb18a81ef699cccd41084f6e22dbc214b40617af30c2f3120b7e4a59d4f`; final LF: yes.

`````text
Changing governed pack bytes does not by itself change the Reader v1 public covenant. Reader v1 remains bands-only, numeric-free, and harmony-only unless a separately authorized public-contract version change widens it. Any future public exposure of the full ten-category matrix requires coordinated versioning without changing the current canonical calculation domain.
`````

**NEW** — UTF-8 bytes: 329; SHA-256: `6594fc2df9a11879488b3fd509e3a76c86121c92103431dc26872cc4c4c53562`; final LF: yes.

`````text
Changing governed pack bytes does not by itself change either Reader public covenant. Reader v1 remains bands-only, numeric-free and harmony-only. The separately approved Reader v2 projection exposes all ten bands under §2.5; it does not change the canonical calculation domain, permit numerics or promote future configuration.
`````

## RL-038

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.5 Privacy posture (no percent/numerics on public) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 87513–87771 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The approved v2 band projection inherits all existing numeric-free restrictions.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 258; SHA-256: `478a1e6f43ba3f8f7c27232124f54a960780873ca91bc5faaf8f593da10d13d8`; final LF: yes.

`````text
The public Reader v1 surface is **numeric-free**. No scores, percentages, counters, or derived numeric indicators may appear in public success bodies. Public items are **exactly** `{id, band}` (see §2.2); all other quantitative signals remain **internal**.
`````

**NEW** — UTF-8 bytes: 278; SHA-256: `5e31a4d899b32d0a3db10ad4bd11b72d32a6d861289072b7c1ebdea5caec70d7`; final LF: yes.

`````text
The public Reader v1 and v2 surfaces are **numeric-free**. No scores, percentages, counters, or derived numeric indicators may appear in public success bodies. Public items are **exactly** `{id, band}` (v1: §2.2; v2: §2.5); all other quantitative signals remain **internal**.
`````

## RL-039

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.5 Privacy posture (no percent/numerics on public) \[Required-Now\]**`
- `### **5.5.4 Validation (binary)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 89236–89482 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Correct the obsolete field-closure gap with the inspected schemas; preserve the validation requirement.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 246; SHA-256: `fc18959e6139960476842092b0629a6020294b84b0a8d715abb6d5a885dd8cc1`; final LF: yes.

`````text
* **Schema gate requirement:** the public success schema MUST reject any numeric fields beyond the six-key covenant (for example, `score` or `score_pct`). The pinned schema does not fully enforce the covenant and remains an implementation gap.  
`````

**NEW** — UTF-8 bytes: 289; SHA-256: `697d57eab1e7109944ad9f7ffc5a78bba4117e51b03a91a41331c44239fdd9bb`; final LF: yes.

`````text
* **Schema gate requirement:** each versioned public success schema MUST reject fields outside its six-key covenant and `{id,band}` items, including `score` and `score_pct`. The inspected v1 and v2 schemas close those fields; static inspection does not establish schema-validation PASS.  
`````

## RL-040

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.5 Privacy posture (no percent/numerics on public) \[Required-Now\]**`
- `### **5.5.4 Validation (binary)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 89709–89907 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Bound the existing CLI parity rule after extending the surrounding privacy covenant to both Reader versions.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 198; SHA-256: `91ca775a30fa22e9785e03bb47ae513ea1dd286914b9cb491af24b1d74ff512e`; final LF: yes.

`````text
* **Parity checks:** a CLI Reader-byte sidecar and Reader body MUST be byte-identical under this numeric-free policy. General `showcompat` stdout is an admin/compat payload and is not Reader bytes.
`````

**NEW** — UTF-8 bytes: 279; SHA-256: `706d49d7231e0a14aa336e7c4b3db6157d2d214cf2d03ea9c63166a5da46003f`; final LF: yes.

`````text
* **Parity checks (v1):** the existing CLI Reader-byte sidecar and Reader v1 body MUST be byte-identical under this numeric-free policy. General `showcompat` stdout is an admin/compat payload and is not Reader bytes. Reader v2 approval creates no additional CLI parity family.  
`````

## RL-041

Operation: `REPLACE`. Change type: `NEW_CANON`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 5\. Magic-10 Framework (closed IDs, scoring→bands) \[Required-Now\]`
- `## **5.5 Privacy posture (no percent/numerics on public) \[Required-Now\]**`
- `### **5.5.5 Change control**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 90237–90341 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Remove the explicit future-v2 statement in the privacy section.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 104; SHA-256: `f7ec320d128d94ad4f24a041a906b5cccc6f930b055d0663c814e330c39ca568`; final LF: yes.

`````text
>   
> Note: Internal math exists; public exposure of the full 10-item array is **Reader v2** (future).
`````

**NEW** — UTF-8 bytes: 176; SHA-256: `64debddd88b4da37521e1ee7768f48f0f92d5d3cc6ddf7a4ac912c1ab96cd0fb`; final LF: yes.

`````text
Reader v2 exposes the full ten-item **band** array under §2.5. That approved projection preserves the numeric-free covenant and does not promote public scores or future math.
`````

## RL-042

Operation: `INSERT`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **6\. Feature Extraction (engine-facing; deterministic) \[Required-Now\]**`
- `## **6.1 Electromagnetics (EM): detection and throat flags**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 98006 (gap). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A05`, `C1`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Add the complete C040-06 16-case oracle for the existing five-state classifier; preserve priority, full-owner normalization, one contribution and HG provenance.

Action: `INSERT ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**BEFORE** — UTF-8 bytes: 134; SHA-256: `b418d1a5e7646fe1e31a4fdf3b90bbbfa049c82308c15cfb92767d9ac2ece7f0`; final LF: yes.

`````text
* **Sorting.** Channel-state rows and the derived EM Channel list must be duplicate-free and ASCII-sorted by canonical `channel_id`.

`````

**AFTER** — UTF-8 bytes: 33; SHA-256: `e2398d47ca897d24f52eb95392f315767a4b4fb7178e2b1bdf778bce50871245`; final LF: yes.

`````text
### **Throat flags (normative)**
`````

**INSERTED** — UTF-8 bytes: 1821; SHA-256: `b9fa0eac18682480221cd95bfa49cf11c4e65e637cb32956ef3e90e22b2e6b1d`; final LF: yes.

`````text
### Complete endpoint conformance table

For this table only, `A` and `B` identify the two input members; each two-bit pattern records ownership of the Channel's lower then higher endpoint Gate. These are exhaustive presence patterns, not scores or a serialized Gate mask. The `Full owner` column identifies the full-Channel member before normalization; only `dominance` and `compromise` emit an owner, encoded as `member_lo` or `member_hi` after numeric Gate-mask ordering. All other states omit the owner field.

| Case | A endpoints | B endpoints | State | Full owner |
| --- | --- | --- | --- | --- |
| CS-01 | `00` | `00` | `none` | absent |
| CS-02 | `00` | `10` | `none` | absent |
| CS-03 | `00` | `01` | `none` | absent |
| CS-04 | `00` | `11` | `dominance` | B |
| CS-05 | `10` | `00` | `none` | absent |
| CS-06 | `10` | `10` | `none` | absent |
| CS-07 | `10` | `01` | `electromagnetic` | absent |
| CS-08 | `10` | `11` | `compromise` | B |
| CS-09 | `01` | `00` | `none` | absent |
| CS-10 | `01` | `10` | `electromagnetic` | absent |
| CS-11 | `01` | `01` | `none` | absent |
| CS-12 | `01` | `11` | `compromise` | B |
| CS-13 | `11` | `00` | `dominance` | A |
| CS-14 | `11` | `10` | `compromise` | A |
| CS-15 | `11` | `01` | `compromise` | A |
| CS-16 | `11` | `11` | `companionship` | absent |

The table applies the existing priority exactly once per Channel. Swapping A and B preserves the state and the normalized full-owner identity. Same-end or unmatched hanging Gates contribute nothing independently; reciprocal opposite hanging Gates produce one electromagnetic Channel identity through the same classifier (§6.2). Full Channel catalog facts remain owned by **PF12-Canon-HDE-Schemas-and-Artifacts**. This conformance table adds no response profile, weight, cap, threshold or category formula.

`````

## RL-043

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **7\. Presets & Configuration (A/B) \[Speculative\]**`
- `## **7.4 Ownership and public boundary**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 132847–133137 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Resolve the preset public boundary without promoting any preset requirement or weakening numeric-free restrictions.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 290; SHA-256: `dd44cb98e92be69cecf2cc36af3e7329b32b614f12f3128efe8b680b2675ab32`; final LF: yes.

`````text
* **Reader v1 boundary.** Reader v1 remains numeric-free and emits only `harmony`. That output is a projection from the complete canonical ten-category matrix; promotion cannot silently expose presets, scores, weights, tokens, other category bands, EM/HG records, or configuration details.
`````

**NEW** — UTF-8 bytes: 332; SHA-256: `b6f170f1180277fc688d0c56115aaf47e9d4fb6fe3fab4fa4e8c463950a033ab`; final LF: yes.

`````text
* **Reader public boundary.** Reader v1 remains numeric-free and emits only `harmony`; Reader v2 exposes the ordered ten-band projection (§2.5). Both project the same complete canonical matrix. Promotion cannot silently expose presets, scores, weights, tokens, EM/HG records, configuration details or any additional public fields.
`````

## RL-044

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **8\. Aggregation Algorithm (deterministic, fixed-point) \[Speculative\]**`
- `## **8.4 Ownership, handoff, and public boundary**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 138792–139189 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Carry both approved Reader boundaries into the future-aggregation routing passage without changing speculative mathematics.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 397; SHA-256: `175045ad9db67fbe531abd6b97dffec26c5cbae204e70d385b30180b1bdad07c`; final LF: yes.

`````text
Final category scores map to bands only through §5.3; this section does not define a second mapping or threshold table. Reader v1 remains numeric-free and emits only the `harmony` band as a projection from the complete canonical ten-category matrix. Promotion does not silently widen public output. Transport, HTTP, CLI stream, harness, and operational behavior remain in their owning documents.
`````

**NEW** — UTF-8 bytes: 439; SHA-256: `3c9e19c124c423e9c911059906a18a12b400a9691bb24898feb26fd78d3c19c8`; final LF: yes.

`````text
Final category scores map to bands only through §5.3; this section does not define a second mapping or threshold table. Reader v1 remains numeric-free and emits only the `harmony` band; Reader v2 follows the ordered ten-band projection in §2.5. Both project the complete canonical matrix. Promotion does not silently widen either covenant. Transport, HTTP, CLI stream, harness, and operational behavior remain in their owning documents.
`````

## RL-045

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **9\. Validation**`
- `## **9.5 Parity and two-run identity**`
- `### **Canonical Magic10 v1 goldens**`
- `#### **M10-G007: valid self-pair boundary**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 145856–145968 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Preserve the existing golden hash and identify its original v1 preimage; v2 uses a different version field even for an empty category array.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 112; SHA-256: `e9aaf056819036fab5188d9c609e9473cd2e1822b8c2933d449490cbf9528b6c`; final LF: yes.

`````text
* canonical Reader preimage bytes hash to `8214324eb0129ff1dc213a5d53bd9d7b3758a351032c5258f7ba28eace7adc15`;  
`````

**NEW** — UTF-8 bytes: 119; SHA-256: `19b589c2f2271b7b639ba139f89a3de61ea2647ea1af7b767f5415ce82277bc7`; final LF: yes.

`````text
* canonical **Reader v1** preimage bytes hash to `8214324eb0129ff1dc213a5d53bd9d7b3758a351032c5258f7ba28eace7adc15`;  
`````

## RL-046

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **9\. Validation**`
- `## **9.5 Parity and two-run identity**`
- `### **Canonical Magic10 v1 goldens**`
- `#### **M10-G008: distinct people with equal Gate masks**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 147508–147590 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Keep the original v1 expected body and make the v2 projection follow the unchanged complete zero-score matrix, without inventing a v2 digest.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 82; SHA-256: `da15db83b1edd89a3ee0ee0712189d4482d704b8190c07b1eb8b787ece63b765`; final LF: yes.

`````text
* Reader emits `eligible: true` and exactly `[{"id":"harmony","band":"Cool"}]`;  
`````

**NEW** — UTF-8 bytes: 162; SHA-256: `caebb20583ad11ec125352e6d39c48f7cb41be69b2b4f2efe88d729486b82eaa`; final LF: yes.

`````text
* **Reader v1** emits `eligible: true` and exactly `[{"id":"harmony","band":"Cool"}]`; Reader v2 projects all ten Cool bands in the governed order under §2.5;  
`````

## RL-047

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **9\. Validation**`
- `## **9.5 Parity and two-run identity**`
- `### **Canonical Magic10 v1 goldens**`
- `#### **M10-G008: distinct people with equal Gate masks**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 147590–147702 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Label the preserved original v1 hash so it cannot be reused as a v2 hash.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 112; SHA-256: `592bcab8f19aafdf3b3fd3a9eb0202edd9e3b312cdbf902128721a7eb0089626`; final LF: yes.

`````text
* canonical Reader preimage bytes hash to `ae435ccc1f9d2043b4ee825f48c54ea421276d49d159b19271e46b24c04f2f6e`;  
`````

**NEW** — UTF-8 bytes: 119; SHA-256: `b013542ab214d142902eebcd565a3ba4a18f46685787123a24217f85e6946087`; final LF: yes.

`````text
* canonical **Reader v1** preimage bytes hash to `ae435ccc1f9d2043b4ee825f48c54ea421276d49d159b19271e46b24c04f2f6e`;  
`````

## RL-048

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]`
- `## **10.1 Canonical serializer (UTF-8, sorted keys, compact, exactly one LF) \[Implemented\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 150249–150469 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Keep serializer parity tied to the existing v1 sidecar while applying canonical serialization to both versions.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 220; SHA-256: `a99b4854b0232a1ebc60e97ee4e54a7f4f26d5096621cdbbf7c8ce628e8b5569`; final LF: yes.

`````text
* **Reader↔CLI parity requirement:** corresponding Reader-envelope bytes from both surfaces must be byte-equal for the same inputs; shared canonicalization alone does not establish logical-envelope or stream parity.  
`````

**NEW** — UTF-8 bytes: 319; SHA-256: `b3b050d40e0d983f6cb1bae20aa1543da2745d1e5ec7fae0ebd2742a2cacbfd6`; final LF: yes.

`````text
* **Reader↔CLI parity requirement (v1):** corresponding Reader v1 and existing CLI Reader-envelope bytes must be byte-equal for the same inputs; shared canonicalization alone does not establish logical-envelope or stream parity. Reader v2 uses the same canonical recipe and creates no additional CLI parity family.  
`````

## RL-049

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]`
- `## **10.2 Unify emission entrypoint (CLI \+ Reader share the same emitter) \[Required-Now\]**`
- `### **10.2.4 Acceptance and validation (binary)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 153921–154159 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Bound the existing binary parity gate without weakening single-emitter obligations for either Reader version.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 238; SHA-256: `b68caa95ad11fe620b56bd446ed599fb4db2be2218812ada61885d63e281805c`; final LF: yes.

`````text
* **Reader↔CLI parity.** For identical inputs and environment, the Reader response body and corresponding CLI Reader-envelope bytes are byte-identical. Compat/admin stdout is a different surface and is not substituted for this proof.  
`````

**NEW** — UTF-8 bytes: 300; SHA-256: `f5640e9a0117768a268fd159994e0631378d6ae5daa93129fd5b6160aca6beff`; final LF: yes.

`````text
* **Reader↔CLI parity (v1).** For identical inputs and environment, the Reader v1 response body and existing corresponding CLI Reader-envelope bytes are byte-identical. Compat/admin stdout is a different surface and is not substituted for this proof; v2 creates no additional CLI parity surface.  
`````

## RL-050

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]`
- `## **10.3 Evidence & acceptance (newline; sorted keys; hash coupling) \[Required-Now\]**`
- `### **10.3.1 Acceptance gates (must all pass)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 156585–156774 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Point versioned schema conformance to both covenants.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 189; SHA-256: `e914f98dbaedab067cbbf72b31666e5f3b87336ff49d94489e9b16dc9807e907`; final LF: yes.

`````text
* **Six-key success.** Success bodies contain exactly the six top-level keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`) and no extras (§2.1).  
`````

**NEW** — UTF-8 bytes: 204; SHA-256: `b37e8061126d773c65a8c79d7ea246ab3ae0c230b0f04dfbab57bb16095650bc`; final LF: yes.

`````text
* **Six-key success.** Success bodies contain exactly the six top-level keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`) and no extras (v1: §2.1; v2: §2.5).  
`````

## RL-051

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]`
- `## **10.3 Evidence & acceptance (newline; sorted keys; hash coupling) \[Required-Now\]**`
- `### **10.3.1 Acceptance gates (must all pass)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 156774–156973 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Add version-specific count/order validation and retain the complete prohibited-field boundary.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 199; SHA-256: `eeb7dec4f29dff9d33c0ec531d8b8a0cf73de7b5226f4a0008c69c7ff45066b4`; final LF: yes.

`````text
* **Public shape.** `categories[*]` are exactly `{id, band}` with `band ∈ {Cool,Open,Warm,Glow}`; no `prompt`, `personal_key`, `shared_key`, `score`, or other field is permitted (§§2.1–2.2).  
`````

**NEW** — UTF-8 bytes: 259; SHA-256: `c2aae3fb3ed0ba9b9f13712e4f8dabad5676f072bc93ab89cb4a07e3ce58abe8`; final LF: yes.

`````text
* **Public shape.** `categories[*]` are exactly `{id, band}` with `band ∈ {Cool,Open,Warm,Glow}` and obey the selected version’s count/order policy (§§2.1–2.2, §2.5); no `prompt`, `personal_key`, `shared_key`, `score`, or other field is permitted.  
`````

## RL-052

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]`
- `## **10.3 Evidence & acceptance (newline; sorted keys; hash coupling) \[Required-Now\]**`
- `### **10.3.1 Acceptance gates (must all pass)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 157176–157285 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: The selected source expressly retains the v1-only CLI parity family.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 109; SHA-256: `d626559764cd64cb09675132413e4c431010b15cf0bc52fe3ea26387a97e0555`; final LF: yes.

`````text
  * corresponding Reader and CLI Reader-envelope bytes are identical for identical inputs and environment;  
`````

**NEW** — UTF-8 bytes: 121; SHA-256: `4d52cb696c7f7ef7e46a2360840c8ccdbc23e22ba794cd07d7a559e201f32cd7`; final LF: yes.

`````text
  * corresponding Reader v1 and existing CLI Reader-envelope bytes are identical for identical inputs and environment;  
`````

## RL-053

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]`
- `## **10.3 Evidence & acceptance (newline; sorted keys; hash coupling) \[Required-Now\]**`
- `### **10.3.2 Governed evidence families**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 157913–158373 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A24`, `A25`, `A26`, `C1`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Retire superseded prompt/schema observations while preserving evidence-currency limits and separating delivery, QA and closure proof classes.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 460; SHA-256: `a0e69bd21451cb1a54f66205476a64017970d9998b44e0d6fd1372a083ab5498`; final LF: yes.

`````text
The pinned repository contains serializer, presenter, schema, test, golden, script, and identity-related files, but the inspected bytes do not establish complete current acceptance: the named CLI schema/LF test is absent, the Reader goldens retain retired fields, the schema and presenter still permit `prompt`, and the checked-in identity marker is a historical or construction-time record rather than proof that the final required validation ran and passed.
`````

**NEW** — UTF-8 bytes: 502; SHA-256: `8bdd57b6a8575a8dbbd096a9fd59e159f4d9ecb85aa3414b222a4562e9a9ff29`; final LF: yes.

`````text
The inspected runtime, presenter and Reader schemas contain the versioned projection, canonical preimage/hash/final-emission definitions, closed success shapes and shared `error_v1` branch. **HDE Build Notes** records the accepted implementation and error-schema correction; those are attributed delivery records, not a current test run. Static artifacts or an identity marker alone do not establish complete current acceptance. PF12 remains the owner of governed evidence families and their currency.
`````

## RL-054

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# 10\. Serializer Canon & Single-Emitter Path \[Required-Now\]`
- `## **10.3 Evidence & acceptance (newline; sorted keys; hash coupling) \[Required-Now\]**`
- `### **10.3.3 CI hygiene (fail-fast)**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 158802–158925 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: State the approved version scope of identity and the unchanged CLI proof requirement.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 123; SHA-256: `f04e290fb9305aaa2119b0ae166d85ede587cf9fb149b08cbc2be4345383fff4`; final LF: yes.

`````text
* **Parity and identity:** compare AB/BA and two-run bytes and compare corresponding Reader and CLI Reader-envelope bytes.
`````

**NEW** — UTF-8 bytes: 178; SHA-256: `9365baa548f3e3d1ef88d1b4b3b0f295c0f33b8d8265d8b7fca7d564822555ad`; final LF: yes.

`````text
* **Parity and identity:** compare AB/BA and two-run bytes within each selected Reader version, and compare the existing corresponding Reader v1 and CLI Reader-envelope bytes.  
`````

## RL-055

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **12\. Implementation Notes (non-normative; repo pointers) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 164341–164837 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Replace the obsolete type-scorer/default-true/ineligible-category description with directly inspected runtime behavior.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 496; SHA-256: `63dc0af3018a8c9d37b488713a0dbda099eab88d074fb9790365b9102ca4d61d`; final LF: yes.

`````text
* **Current Reader runtime:** `engine/runtime/public.py`  
    
  * Builds the current single-`harmony` Reader envelope, computes that band separately through `engine/compat/ts_v0.py`, and calls `presenter/reader_v1/emitter.py`.  
  * The function defaults an externally supplied `eligible` value to true and constructs a `harmony` category even when `eligible` is false. Those bytes do not satisfy the complete eligibility and empty-category requirements merely because they are serializable.


`````

**NEW** — UTF-8 bytes: 501; SHA-256: `8b547177a80b8f7e88c1aeceddffe1a04eb198d8d2bea6cb8da4a6928e2b9744`; final LF: yes.

`````text
* **Current Reader runtime:** `engine/runtime/public.py`  
    
  * Requires the eligibility result and validated band projection from its caller; it does not calculate a type-derived band. Reader v1 emits one `harmony` item when eligible, Reader v2 emits the exact ordered ten-item projection, and both emit `[]` when ineligible.  
  * The two versioned projections call the canonical presenter/emitter. Static definitions do not establish handler reachability, production readiness or acceptance.


`````

## RL-056

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **12\. Implementation Notes (non-normative; repo pointers) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 165126–165291 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Replace the retired prompt carry-through instruction with the inspected versioned emitter definitions.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 165; SHA-256: `5061ba15ad3768ab8bc353ba8231ab5469cc91161c9b7867b002f809475bef38`; final LF: yes.

`````text
  * `presenter/reader_v1/emitter.py` still carries through optional `prompt`; remove that carry-through so `categories[*]` are exactly `{id, band}` (§§2.1–2.2).
`````

**NEW** — UTF-8 bytes: 227; SHA-256: `05555638927da19d57c513a7ba0f3f92c8d5e0c332277888020b9739e074f065`; final LF: yes.

`````text
  * `presenter/reader_v1/emitter.py` contains both versioned preimage builders and rejects any category fields beyond `id` and `band`; the v2 builder preserves the governed sequence and shares the final hash/emission function.
`````

## RL-057

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **12\. Implementation Notes (non-normative; repo pointers) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 165293–165937 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Replace the old independent float/admin scoring description with the inspected core/compute path, retaining the legacy-order observation as a bounded non-authoritative fact.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 644; SHA-256: `c4d422a89c8a6cdd7541d0f8685e8a2d9f45dda42df68e5387c927ae15104dba`; final LF: yes.

`````text
* **Ten-category compat internals:** `engine/compat/{compute,categories,thresholds,ordering}.py`  
    
  * This is a separate internal/admin hash-and-binary-float scoring path; it is not the source of the current public Reader `harmony` band and does not implement the canonical §5 Human Design-grounded matrix.  
  * `engine/compat/categories.py` maintains a heat-first order that differs from the harmony-first frozen order in `catalog/magic10.json`. Ordered consumers must use the governed order.  
  * Reader v1 still emits only the `harmony` projection; full public Magic-10 exposure requires an authorized versioned contract (§2.2).


`````

**NEW** — UTF-8 bytes: 772; SHA-256: `50b1cc3ad0baa069f584f135b211b1ce51fea60cb868ac2d68bf9e438f02e3ce`; final LF: yes.

`````text
* **Ten-category computation and projection:** `engine/core/core.py`, `engine/compat/compute.py`, and `engine/runtime/public.py`  
    
  * The inspected core defines the pure integer ten-category calculation. The compute boundary validates parties, decides eligibility before intrinsic evaluation, invokes the canonical core and retains intrinsic identity separately from the Reader hash.  
  * The legacy `engine/compat/categories.py` constant is heat-first; it does not change the governed harmony-first order of `catalog/magic10.json`. Ordered Reader v2 consumers must use that governed sequence.  
  * Reader v1 remains the `harmony` projection; Reader v2 follows §2.5. These pointers do not authorize a second scoring home or establish implementation acceptance.


`````

## RL-058

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **12\. Implementation Notes (non-normative; repo pointers) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 166784–167173 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `A24`, `A25`, `A26`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Reconcile the old schema-misalignment instruction with the actual v1/v2 success and corrected error branches.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 389; SHA-256: `e6fad6cd541e17e3293a5b24bfb1add6a1ad757a6906a7cd23fac592f88344e7`; final LF: yes.

`````text
* **Public success schema:** `schemas/reader.v1.schema.json`  
    
  * The inspected schema permits optional `category.prompt` and lists legacy `*_leader` category IDs rather than the current `harmony` ID. Align it to the exact six-key success covenant and `{id,band}` item contract in §§2.1–2.2.  
  * Typed errors remain governed by §2.3 and use the canonical single-LF emitter.


`````

**NEW** — UTF-8 bytes: 507; SHA-256: `c642d162fad483d28f8e6b23e4c41caaa4bd04400838707327e445f6ae0ad9cb`; final LF: yes.

`````text
* **Versioned Reader schemas:** `schemas/reader.v1.schema.json` and `schemas/reader.v2.schema.json`  
    
  * The inspected success branches close the six-key covenant and `{id,band}` items. V1 admits one eligible `harmony` item or an empty ineligible array; v2 admits the ordered ten-item projection or an empty ineligible array.  
  * Both inspected schemas admit the shared `error_v1` branch referenced in §2.3. Shape definitions do not establish validation PASS, transport acceptance or deployment.


`````

## RL-059

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **12\. Implementation Notes (non-normative; repo pointers) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 167739–167982 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A24`, `A25`, `A26`, `C1`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Preserve the evidence boundary without repeating superseded reader-field observations as current facts.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 243; SHA-256: `99e9547162a09a7a922834b32a61b00723e393df93c6136d876205189f86f776`; final LF: yes.

`````text
  * The expected CLI schema/LF test path is not present in the inspected repository. Existing Reader goldens contain retired fields, and the checked-in identity marker records a deterministic predicate rather than complete final validation.  
`````

**NEW** — UTF-8 bytes: 265; SHA-256: `322301644eea326f9db81478b8f6c49796e21001df88cb7fb9bb90f45c6116d2`; final LF: yes.

`````text
  * **HDE Build Notes** records the accepted delivery and corrected Reader error schema. Delivery, OPS, documentation, QA and closure remain distinct proof classes; historical records do not establish live current-row readiness or current evidence-family currency.
`````

## RL-060

Operation: `REPLACE`. Change type: `CONSISTENCY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **12\. Implementation Notes (non-normative; repo pointers) \[Required-Now\]**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 168409–168612 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Carry the versioned order/identity and v1 CLI boundary into implementation validation pointers.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 203; SHA-256: `c4b550a266cc6b533435de9964bbd0f6ddf29d43a4e6e058ac3fef367e0cfd9c`; final LF: yes.

`````text
  * Validate AB↔BA bytes, two-run identity, single-LF discipline, schema and shape, frozen category order, idempotence coupling, and corresponding Reader/CLI Reader-envelope parity (§§3.4, 9, 10.3).
`````

**NEW** — UTF-8 bytes: 267; SHA-256: `05add78c45a2a024afe960e0634e2dbf69d47418976d319f7e897d7a6c3e43ad`; final LF: yes.

`````text
  * Validate AB↔BA bytes and two-run identity within each selected Reader version, single-LF discipline, schema and shape, the governed v2 category order, idempotence coupling, and the existing corresponding Reader v1/CLI Reader-envelope parity (§§3.4, 9, 10.3).
`````

## RL-061

Operation: `REPLACE`. Change type: `CLARIFY`. Expected occurrence/gap count: **1**; producer observed: **1**.

Original heading path:

- `# **Appendix A — Determinism & Ordering (reference) \[Required-Now\]**`
- `## **A.2 Set normalization**`

Original scope: the complete unique section starting at the final heading above, including its children. Supporting raw UTF-8 offset: 170259–170481 (half-open span). Offsets are evidence, not substitutes for literal locators.

Target document: `PF01-Canon-HDE-Math-Spec`. Findings / source items: `A23`, `S05`, `S07`. Controlling basis: these complete source units at the pinned baseline, identified in the companion proof log.

Rationale: Remove the category example that could override the explicitly ordered v2 array or repair forbidden duplicates.

Action: `REPLACE ONCE` using the literal blocks below. Uniqueness: original heading-path matches=1; each required literal block/anchor matches within its scope=1; conflicts=0.

**OLD** — UTF-8 bytes: 222; SHA-256: `3b9287076b29c8a77310efdb20c9539014843958db6b10b0d49f6e1c611bb7f3`; final LF: yes.

`````text
* **Array → set semantics.** When an array represents a set (e.g., unique **category `id`s**, token IDs, channel IDs), **deduplicate by identity key**, then **sort deterministically (ASCII)** before use/serialization.  
`````

**NEW** — UTF-8 bytes: 395; SHA-256: `555c57d8392873d16acd581989c9ba259f9784cbf6bb20af7f4bc8d4e7377988`; final LF: yes.

`````text
* **Array → set semantics.** When an array represents a set (e.g., token IDs or channel IDs), apply its owning deduplication and deterministic ASCII-sort contract before use/serialization. Reader v1’s single-category policy remains §2.2; Reader v2 `categories` is the governed ordered array in §2.5 and MUST NOT be set-sorted, deduplicated or repaired. Invalid v2 sequences fail closed.  
`````

END OF REDLINES
