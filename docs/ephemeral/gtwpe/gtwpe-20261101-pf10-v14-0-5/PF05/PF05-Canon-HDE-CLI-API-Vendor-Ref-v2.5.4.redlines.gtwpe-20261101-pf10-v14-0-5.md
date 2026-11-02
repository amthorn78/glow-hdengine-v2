# PF05 redlines — gtwpe-20261101-pf10-v14-0-5 — T-02

## Package identity

| Field | Value |
| :---- | :---- |
| Redlines file | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Proof log | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, in the same directory |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-02/drain-r2`. It supersedes `drain-r1` (commit `0d22343`) at the same path, on the Product Owner's direction of 2026-11-02. |
| Preparer | TW-DRAIN-10 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`), run in the Claude Code document session Nathan started for T-02 on 2026-11-02 |
| Preparation outcome | `READY`; save state recorded in the proof log |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-02; rows C-01, C-02, C-03; support C-06 |
| Target (original) | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md`, title `PF05-Canon-HDE-CLI-API-Vendor-Ref`, v2.5.4, git blob `53e6a9028dfa5d79b91e9b98cc949160c5a5cefe`, SHA-256 `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028`, 327,342 bytes, 4,461 lines, read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56` |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; addendum 2.1 D-1 (l.225–276), D-2 (l.277–344), D-3 (l.345–396), context l.205–224 and l.491–516 |
| Simulated one-pass result | SHA-256 `1587ea2110a62813f82e43c715c45c5dc097aecc88aabb9c2f71914667e2bad6`, 332,470 bytes (scratch only; Apply produces the final file) |

## Literal and operation conventions

- Every operation is `REPLACE` against the unchanged original target. No operation reads another operation's output.
- Each OLD and NEW literal is the exact text between its opening and closing four-backtick fence lines. The newline that ends the last literal line, just before the closing fence, is not part of the literal. Every other newline and every space inside the fence is part of it, including trailing double spaces.
- An OLD literal may begin or end inside a line. Its expected occurrence count is over the whole original target.
- Section paths quote the original heading lines exactly. They locate the edit; the OLD literal's unique occurrence is the binding locator.
- Original line numbers are informative only.
- Document-control fields (version, effective date, Last Update Gate) are left to TW-APPLY-10. The proof log supplies the header schema and source identity.

## RL-01

- Ledger rows: C-02
- Source basis: PF10 2.1 D-2, l.284-289 (Selection; The v1 path; No fallback)
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# 4\. Commands (by status)" > "## 4.6 hdctl bg:resolve \[Required-Now\]"
- Original line(s): 956 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-2 decides that no non-v2 base reaches bodygraphs by fallback and that a terminal v1 base is retained legacy selection. This §4.6 permission states the superseded posture and contradicts §7.1.10.

OLD:

````
Non-v2 configured bases MAY preserve the legacy BodyGraph route only as explicit legacy fallback.
````

NEW:

````
A terminal `v1` configured base selects the retained legacy BodyGraph route under §7.1.10; that is legacy selection, not fallback, and every other non-v2 base fails with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or any external I/O.
````

## RL-02

- Ledger rows: C-03 (support C-06)
- Source basis: PF10 2.1 D-3, l.349-364 and l.377-378 (Classification, Gate order, Authentication, Wider exposure, Residual risk; Canon superseded); C-06 l.223 and l.506
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# 5\. Reader Transport (public bytes) \[Required‑Now\]" > "## **5.5 Compat v1 (dev-only) route & parity harness \[PartiallyImplemented; Required−Now\]**"
- Original line(s): 2493 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-3 adds the dev/admin gate as step 2 of 'Validation and environment gating', withdraws 'authenticated' and 'internal authentication' from 'Success body', and records the no-credential posture, the wider-exposure rule and the accepted residual risk. The gate is not in the code at the snapshot, so the gap is stated beside it.

OLD:

````
* **Success body (dev/internal; authenticated).** After the production-excluding environment gate and internal authentication, `POST /api/compat/v1` returns the canonical `magic10_compat_result.v1` defined in §4.1.3 for an eligible pair. It does not return or wrap Reader v1 bytes. Full signals, scores, and narrative keys remain internal/admin-only. A valid self-pair has no complete result, and this route must not fabricate a matrix.
````

NEW:

````
  * **Dev/admin gate (step 2).** The compatibility namespace is a dev/admin-only surface under **HDE-Governance** §4.1.4. Step 1 is the production-like guard above. Before any compatibility computation, database read, or vendor call, a request that step 1 does not refuse is served only when `APP_ENV` is exactly `dev`, `test`, or `local`, with no trimming, no case-folding, and no default. A missing, empty, or other `APP_ENV` value fails closed with the writer-style refusal that the dev/admin HTTP surfaces use: status `403`, presenter-backed `error_v1` `code=ERR_WRITER_FORBIDDEN`, `Cache-Control: no-store`, and no `ETag`; `HEAD` carries no body. `ENGINE_ENV` never admits the surface. The method, probe, and POST rules of this section apply only to a request that both steps admit.  
* **Success body (dev/internal).** After both environment-gate steps admit the request, `POST /api/compat/v1` returns the canonical `magic10_compat_result.v1` defined in §4.1.3 for an eligible pair. It does not return or wrap Reader v1 bytes. Full signals, scores, and narrative keys remain internal/admin-only. A valid self-pair has no complete result, and this route must not fabricate a matrix.  
* **Authentication.** No credential is required while the dev/admin gate admits the route only under `APP_ENV` exactly `dev`, `test`, or `local`. Before the route is served in any other environment, a later decision must require the **HDE-Governance** §8.3.2 admin credential, or an equivalent credential pinned in this document, and must add the **HDE-Governance** §8.3.4 logging rules.  
* **Residual risk (accepted).** An admitted dev, test, or local process connected to the shared production database serves stored-user compat results to any caller that reaches its port. That exposure is controlled by where the process listens, under the documented loopback access in **Glow-Infrastructure** §2.2, not by this route. The posture is the same as for every other dev/admin surface.  
* **Implementation state (informative).** Bounded static inspection at `main@e2b7427ff418ca8f08f05587c4a541308a76da56` finds that the guard in `engine/http/compat_handler.py` refuses only production-like posture. It classifies posture through `adapter/env_guard.py`, which treats an absent or blank `APP_ENV` and `ENGINE_ENV` as `dev` and passes every other non-production value through. The step 2 gate is therefore a Required-Now gap against this contract. Its fix belongs to the implementing change for Candidate CRD Items List item 9, as HDE Build Notes records. This inspection concerns checked-in bytes only and establishes no runtime behavior, deployment, or acceptance.
````

## RL-03

- Ledger rows: C-03
- Source basis: PF10 2.1 D-3, l.350-355 (Gate order: the existing method, probe and POST rules apply)
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# 5\. Reader Transport (public bytes) \[Required‑Now\]" > "## **5.5 Compat v1 (dev-only) route & parity harness \[PartiallyImplemented; Required−Now\]**" > "### **Headers & conditionals (normative)**"
- Original line(s): 2509 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Under D-3 a non-production request outside APP_ENV dev, test or local is refused 403 before the method rules; the method rules apply only to an admitted request.

OLD:

````
**Method and subpath handling.** In non-production posture, `HEAD /api/compat/v1`
````

NEW:

````
**Method and subpath handling.** For a request that both environment-gate steps admit, `HEAD /api/compat/v1`
````

## RL-04

- Ledger rows: C-03
- Source basis: PF10 2.1 D-3, l.358 and l.378 (Parity (clarified): 'authenticated' is superseded)
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# 5\. Reader Transport (public bytes) \[Required‑Now\]" > "## **5.5 Compat v1 (dev-only) route & parity harness \[PartiallyImplemented; Required−Now\]**" > "### **Parity (clarified)**"
- Original line(s): 2520 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-3 supersedes 'authenticated' in 'Parity (clarified)'; no authentication mechanism exists in canon or code.

OLD:

````
stdout and authenticated `POST /api/compat/v1` MUST emit
````

NEW:

````
stdout and `POST /api/compat/v1` MUST emit
````

## RL-05

- Ledger rows: C-02
- Source basis: PF10 2.1 D-2, l.281-283 and l.315 (What governs; §7.1.10 added to)
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**" > "## **7.1 Rails & Environment \[Required-Now\]**" > "### **7.1.10 Endpoint policy (explicit version-gated dual lineage)**"
- Original line(s): 3476 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-2 extends the §7.1.10 scope from bg:resolve to compat chart acquisition by showcompat and conjunction.

OLD:

````
`bg:resolve --source vendor` selects one full-detail route from the validated terminal API-version segment of the configured base:
````

NEW:

````
Route selection and the configured-base boundary below govern every resolver-selected vendor acquisition: `bg:resolve --source vendor`, and compat chart acquisition by `hdctl showcompat`, including its conjunction mode. Each acquisition selects one full-detail route from the validated terminal API-version segment of the configured base:
````

## RL-06

- Ledger rows: C-01
- Source basis: PF10 2.1 D-1, l.229-232 and l.259 (three-path scope; implementation-state limit becomes a gap)
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**" > "## **7.1 Rails & Environment \[Required-Now\]**" > "### **7.1.11 SAFE rails and production vendor override**"
- Original line(s): 3507 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Once D-1 widens the contract to three paths, the S14 delivery covers only bg:resolve; the claim is narrowed to what was delivered.

OLD:

````
HDE-CRD-0002 delivered this contract as its requirement S14,
````

NEW:

````
HDE-CRD-0002 delivered this contract for `hdctl bg:resolve --source vendor` as its requirement S14,
````

## RL-07

- Ledger rows: C-01 (support C-06)
- Source basis: PF10 2.1 D-1, l.259 (the limit becomes a gap against this decision); C-06 l.223 and l.506
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**" > "## **7.1 Rails & Environment \[Required-Now\]**" > "### **7.1.11 SAFE rails and production vendor override**"
- Original line(s): 3515-3521 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-1 turns the limit 'The gate covers only the command §7.1.11a names' into a gap against the decision. Bounded inspection at the snapshot confirms the uncovered paths.

OLD:

````
These limits apply:

* An account name identifies an account, not necessarily a person. §7.1.11e still decides who may initiate, and supplying the flag authorizes nothing by itself.
* The gate covers only the command §7.1.11a names. Vendor acquisition through the compat chart resolver, which `hdctl showcompat --source vendor` and its conjunction mode use, applies the generic rails but not this gate. The HDE-CRD-0002 close report defers that gap to the Product Owner as pending and non-gating.
* The same close report records S14 as met: one check proves the local matrix, and one covers a single bounded live vendor call initiated by the Product Owner, not broad HumanDesignAPI v2 conformance.

This inspection concerns checked-in bytes only, and a close-report record is not a QA verdict; neither establishes runtime behavior, deployment or acceptance.
````

NEW:

````
These limits apply:

* An account name identifies an account, not necessarily a person. §7.1.11e still decides who may initiate, and supplying the flag authorizes nothing by itself.
* The HDE-CRD-0002 close report records S14 as met: one check proves the local matrix, and one covers a single bounded live vendor call initiated by the Product Owner, not broad HumanDesignAPI v2 conformance.

**Required-Now implementation gap.** The gate applies to every path §7.1.11a names, but the delivered gate covers only `hdctl bg:resolve --source vendor`. Bounded static inspection at `main@e2b7427ff418ca8f08f05587c4a541308a76da56` finds:

* the pre-scan in `engine/cli/main.py` refuses `--allow-prod-vendor` as a usage error on every command other than `bg:resolve`;
* in conjunction mode, `engine/cli/main.py` passes the vendor source policy for every `--source` value other than `db` or `auto`, including an absent `--source`;
* vendor acquisition through the compat chart resolver in `engine/bodygraph/resolver.py`, which `hdctl showcompat --source vendor` and its conjunction mode use, applies the generic rails but not this gate.

The uncovered paths are a gap against this contract, not a decided limit. The HDE-CRD-0002 close report defers them to the Product Owner as pending and non-gating. Their fix belongs to the implementing change for Candidate CRD Items List item 9, as HDE Build Notes records.

These inspections concern checked-in bytes only, and a close-report record is not a QA verdict; none establishes runtime behavior, deployment or acceptance.
````

## RL-08

- Ledger rows: C-01
- Source basis: PF10 2.1 D-1, l.229-234 and l.255 (three-path scope; flag accepted by those paths only)
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**" > "## **7.1 Rails & Environment \[Required-Now\]**" > "### **7.1.11 SAFE rails and production vendor override**" > "#### **7.1.11a Exact CLI flag**"
- Original line(s): 3533 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-1 supersedes 'accepted only by hdctl bg:resolve --source vendor' with the three-path scope.

OLD:

````
It is one value-bearing flag accepted only by `hdctl bg:resolve --source vendor`. It has no short spelling, compatibility alias, negated form, environment-variable form, or implicit default.
````

NEW:

````
It is one value-bearing flag accepted only by the three CLI paths that acquire a chart from the vendor, and by no other command:

* `hdctl bg:resolve --source vendor`;
* `hdctl showcompat --source vendor`;
* `hdctl showcompat --conjunction` when the invocation selects vendor acquisition for either party.

Each path applies the §7.1.11b classification, the §7.1.11c matrix, the §7.1.11d order and the §7.1.11e initiator rule unchanged. The flag has no short spelling, compatibility alias, negated form, environment-variable form, or implicit default.
````

## RL-09

- Ledger rows: C-01
- Source basis: PF10 2.1 D-1, l.235 and l.256 (Order: step 2 superseded)
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**" > "## **7.1 Rails & Environment \[Required-Now\]**" > "### **7.1.11 SAFE rails and production vendor override**" > "#### **7.1.11d Evaluation order and scope**"
- Original line(s): 3577 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-1 rewrites step 2 to 'the invocation selects vendor acquisition' for each command.

OLD:

````
2. Confirm `--source vendor`; using the flag with `--source db` or `--source auto` is a CLI usage error.
````

NEW:

````
2. Confirm that the invocation selects vendor acquisition. Supplying the flag to an invocation that selects no vendor acquisition is a CLI usage error, exit `64`; that covers `--source db`, `--source auto`, and conjunction with `db` or `auto`.
````

## RL-10

- Ledger rows: C-01
- Source basis: PF10 2.1 D-1, l.236-238 (Scope of one authorization)
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**" > "## **7.1 Rails & Environment \[Required-Now\]**" > "### **7.1.11 SAFE rails and production vendor override**" > "#### **7.1.11d Evaluation order and scope**"
- Original line(s): 3584 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-1 sets the scope of one authorization to the bounded acquisitions of one invocation, at most one per party and two for a pair, with no write, no public Reader or Aux traffic and no opening of a closed rail.

OLD:

````
The flag authorizes only one bounded admin vendor HTTP opportunity. It does not authorize public Reader/Aux vendor traffic,
````

NEW:

````
One valid flag authorizes only the bounded admin vendor acquisitions of one invocation: at most one acquisition per party, so at most two for a pair. It does not authorize opening a closed rail, public Reader/Aux vendor traffic,
````

## RL-11

- Ledger rows: C-01
- Source basis: PF10 2.1 D-1, l.235, l.242-244 and l.257 (usage error exit 64; showcompat carrier rule)
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**" > "## **7.1 Rails & Environment \[Required-Now\]**" > "### **7.1.11 SAFE rails and production vendor override**" > "#### **7.1.11e Error carrier and authorized setter**"
- Original line(s): 3588 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-1 adds the showcompat carrier rule to §7.1.11e and aligns the usage case with the rewritten step 2.

OLD:

````
or use with a non-vendor source uses the canonical CLI usage carrier and exits `64`. Runtime policy refusals use the canonical `status="error"` resolver envelope with one stable typed code and a non-sensitive message and exit `1`.
````

NEW:

````
or use with an invocation that selects no vendor acquisition uses the canonical CLI usage carrier and exits `64`. On `hdctl bg:resolve`, runtime policy refusals use the canonical `status="error"` resolver envelope with one stable typed code and a non-sensitive message and exit `1`. On `hdctl showcompat`, including its conjunction mode, policy refusals use that command's existing canonical typed error carrier (§4.1.4), with the same stable codes (`PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID`, `PROVIDER_AUDIT_UNAVAILABLE`, `PROVIDER_CONFIG_INVALID`) and exit `1`.
````

## RL-12

- Ledger rows: C-01
- Source basis: PF10 2.1 D-1, l.241 and l.258 (Audit: command values)
- Change type: CANON_UPDATE
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**" > "## **7.1 Rails & Environment \[Required-Now\]**" > "### **7.1.11 SAFE rails and production vendor override**" > "#### **7.1.11f Audit contract**"
- Original line(s): 3604 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-1 supersedes the command rule 'exactly bg:resolve' with the three values.

OLD:

````
| `command` | exactly `bg:resolve` |
````

NEW:

````
| `command` | exactly one of `bg:resolve`, `showcompat`, or `showcompat:conjunction` |
````

## RL-13

- Ledger rows: C-01, C-02, C-03
- Source basis: PF05 §0.4 'Editorial vs. normative' and §11.1 'Policy' (target's own logging rule)
- Change type: DOC_HYGIENE (change-log entry required by the target)
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **11\. Change Log & Doc-Delta Hooks \[Required-Now\]**" > "## **11.1 Change Log (concise, normative)**"
- Original line(s): 4148 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: PF05 §0.4 and §11.1 require a change to transport or the CLI contract to be logged. The entry names v2.5.5, the baseline v2.5.4 bumped once by the target's patch scheme; the format carries no date.

OLD:

````
* v2.5.4 — Record the delivered production vendor override and its limits in §7.1.11, remove it from the gap statements in §§1 and 7.2.0, record the Endpoint Catalog state with the canon-retired route exclusion in §5.6, and record the resolved not-found, showcompat-help and legacy CLI proof limitations in §§4.1.6, 5.1.0 and 5.1.7. Sentinel updated: NO.
````

NEW:

````
* v2.5.4 — Record the delivered production vendor override and its limits in §7.1.11, remove it from the gap statements in §§1 and 7.2.0, record the Endpoint Catalog state with the canon-retired route exclusion in §5.6, and record the resolved not-found, showcompat-help and legacy CLI proof limitations in §§4.1.6, 5.1.0 and 5.1.7. Sentinel updated: NO.
* v2.5.5 — Extend the production vendor override to `hdctl showcompat --source vendor` and vendor-selecting conjunction, with the showcompat carrier and audit command values, and record the uncovered paths as an implementation gap in §7.1.11; extend §7.1.10 route selection to compat chart acquisition, align §4.6 with it, and correct the §1 legacy-route wording to terminal-v1 legacy selection with the §7.2.0 non-v2 gap; add the `APP_ENV` dev/admin gate to `/api/compat/v1`, withdraw its authentication wording and record the gate gap in §5.5. Sentinel updated: NO.
````

## RL-14

- Ledger rows: C-02
- Source basis: PF10 2.1 D-2, l.288-289 and l.303 (The v1 path; No fallback; §7.2.0 records broad non-v2 legacy selection as a material gap); Product Owner direction 2026-11-02
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF05-Canon-HDE-CLI-API-Vendor-Ref
- Section path: "# **1\) “Map at a Glance” — What’s live vs planned \[Required-Now\]**" > "  ## **Vendor ingest (HDAPI)**"
- Original line(s): 119 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Product Owner direction (2026-11-02): keep the dated record, but stop calling the legacy route a fallback. Its title and 'non-v2 bases retain an explicit legacy `bodygraphs` fallback' contradict D-2 and §7.1.10. The pin, the nonclaims and the §§7.1.10, 7.2 and 7.4 pointer are kept.

OLD:

````
* **Legacy BodyGraph fallback and bounded HumanDesignAPI v2 chart path — implemented with remaining PF05 gaps.** **HDE Build Checklist — Fermentation** records HDE-FERM006 through HDE-FERM008 Done for the bounded HDE BodyGraph-detail scope. At `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, configured v2 bases use the version-neutral `charts` resource, Bearer auth, and the deterministic `ChartResult` adapter; non-v2 bases retain an explicit legacy `bodygraphs` fallback. This does not claim broad HumanDesignAPI v2 platform conformance, public Reader expansion, production deployment, production DB-hot-path completion, or complete conformance to every §7.2/§7.3 byte requirement. See §§7.1.10, 7.2, and 7.4.  
````

NEW:

````
* **Retained legacy BodyGraph selection and bounded HumanDesignAPI v2 chart path — implemented with remaining PF05 gaps.** **HDE Build Checklist — Fermentation** records HDE-FERM006 through HDE-FERM008 Done for the bounded HDE BodyGraph-detail scope. At `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, configured v2 bases use the version-neutral `charts` resource, Bearer auth, and the deterministic `ChartResult` adapter. A terminal `v1` base selects the retained legacy `bodygraphs` route under §7.1.10, which is legacy selection, not fallback. Legacy selection by any other non-v2 base at that pin is the material gap recorded in §7.2.0, not a retained capability. This does not claim broad HumanDesignAPI v2 platform conformance, public Reader expansion, production deployment, production DB-hot-path completion, or complete conformance to every §7.2/§7.3 byte requirement. See §§7.1.10, 7.2, and 7.4.  
````

END OF REDLINES
