# Redlines — PF05-Canon-HDE-CLI-API-Vendor-Ref from v2.5.3 (T-PF05)

Preparation outcome: **READY**. Save completeness and validation are recorded in the companion proof log, `redlines-PF05-from-v2.5.3.proof-log.md`, in this directory.

## Package identity

| Field | Value |
| :---- | :---- |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff (fetched live 2026-10-26) |
| Run identity | `gtwpe-20261026-pf10-v13-8-8 / T-PF05 / TW-DRAIN-10 / run 1` |
| Preparer | Claude Code cloud session https://claude.ai/code/session_01D49VTgmgq8kpkcN9WLDdAW, started by Nathan for T-PF05 |
| Target | `PF05-Canon-HDE-CLI-API-Vendor-Ref` v2.5.3, `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md` |
| Baseline bytes | blob `8b136def4c22f8308169a1b0315086b3e90ead1d`; 323,966 bytes; 4,439 LF-terminated lines; no CR; SHA-256 `65a9ad6e9d4e75cf50c4e0ae5ac6b3cbabce35bea759de9a6ef4c77549dd6352` |
| Baseline commit | read at `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`; the same blob as at the ledger baseline `9dda63dd3f05f496c3ff67e95da78550d3950c5a` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, task T-PF05; rows A07, A08, A09 (with X05), S-APR |
| Change sources | PF10 `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` v13.8.8 (addenda 2.7 lines 688–889, 2.8 lines 890–1002, 2.9 lines 1003–1101; front matter lines 1–223); `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` lines 147–193 (S-APR), overlaid by `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` C-8 to C-12; `audit/HDE-CRD-0002_close_report.md` (the recorded limits in RL-03) |
| Held, not drafted | H-03 (LR5-O1, §5.11.2 and §5.12); H-04 (OBS-W4-4, §7.1.11f "governed clock boundary") |

## Payload convention

- Every payload is the exact UTF-8 text between its opening fence line (`````` ````text ``````) and its closing fence line (`````` ```` ``````), with lines joined by LF. The LF before the closing fence is fence syntax, not payload, unless the field says `ends with LF: yes`; then exactly one LF is part of the payload.
- Each payload states its byte length and SHA-256 so the extraction can be checked. No payload contains a fence, a CR or trailing spaces.
- Every locator is the literal OLD block or the BEFORE+AFTER anchor pair, matched against the unchanged original. Line numbers and heading paths are informative only.
- Operations resolve independently against the original; none overlaps another, and no insertion gap touches a replaced span.
- Document-control fields (version, effective date, Last Update Gate) are not redlined here. TW-APPLY-10 derives them; the proof log supplies the header schema and the source identities in order.

## RL-01

- Redline ID: RL-01
- Operation: `REPLACE`
- Change type: CONSISTENCY
- Source items: S-APR (Specification "Canon, QA & Build Notes posture", S14 status drainage); A09 with X05 (the DD-04 status, stale since S14 was delivered)
- Target document: `PF05-Canon-HDE-CLI-API-Vendor-Ref`
- Section path: line 73: `# **1\) “Map at a Glance” — What’s live vs planned \[Required-Now\]**` > line 117: `  ## **Vendor ingest (HDAPI)**`
- Location: original line 125; the "Live HTTP gated by SAFE rails — Required-Now." bullet, second sentence
- Scope and expected count: whole PF; expected 1; observed 1
- Rationale: This sentence restates the DD-04 status that RL-03 drains: S14 delivered the production vendor override, so "unimplemented" is stale. The pointer to §7.1 stays.
- OLD (115 bytes; SHA-256 `9a4ba5f0480d254636d6e7457093ff0d26ed1b9dc41025249c9733f5b9905d3d`; ends with LF: no):

````text
Closed-rails refusal behavior, the unimplemented production override requirement, and rails evidence live in §7.1.
````

- NEW (96 bytes; SHA-256 `4ee12aeb4c521f6709a6a7bdad24b388404fafa224fe9d41c94d57167f64631b`; ends with LF: no):

````text
Closed-rails refusal behavior, the production vendor override, and rails evidence live in §7.1.
````

## RL-02

- Redline ID: RL-02
- Operation: `REPLACE`
- Change type: CANON_UPDATE
- Source items: A07 (CR-7 and AD-1; canon doc-delta candidate "HDE-CLI-API-Vendor-Ref §5.6 'Implementation and acceptance state'"); A08 ("Required canon drainage": CR-7 into §5.6); supporting X04 §18 row for §5.6
- Target document: `PF05-Canon-HDE-CLI-API-Vendor-Ref`
- Section path: line 2042: `# 5\. Reader Transport (public bytes) \[Required‑Now\]` > line 2535: `## **5.6 Endpoint Catalog (JSON success) \[Required−Now\]**`
- Location: original line 2577; the "Implementation and acceptance state (informative)." paragraph, the last paragraph of §5.6 before the `---` rule
- Scope and expected count: whole PF; expected 1; observed 1
- Rationale: The paragraph records the Catalog at `aa58e93` without the Aux record, `public_aux` or `aliases`. HDE-CRD-0002 later added the Aux record (S15) and, under CR-7, removed the five records of the three canon-retired routes (23 to 18), with a validator that refuses such a record. The replacement states the Catalog verified at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c` and routes the population rule to its owner.
- OLD (452 bytes; SHA-256 `244434aa139c28e77d2de6febbe27701f677427bb8599405abae1621e95e609c`; ends with LF: no):

````text
**Implementation and acceptance state (informative).** At pinned authoring inspection `main@aa58e93ddedb9738af33de20e42c39a38b7c1e08`, `docs/ENDPOINTS_CATALOG.json` used PF12's current per-method model but did not yet contain the Aux or admin-bundle records, `public_aux`, or `aliases`. This Required-Now projection is a dependent contract requirement, not a claim that the checked-in Catalog, deployment, QA, OPS, or acceptance state already conforms.
````

- NEW (1669 bytes; SHA-256 `3d7e22165edf2a9d6e3be073ea082d513425527917598f09fcc512d029cfb3ff`; ends with LF: no):

````text
**Implementation and acceptance state (informative).** Bounded static inspection at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c` finds:

* `docs/ENDPOINTS_CATALOG.json`, a symlink to `artifacts/audit/ENDPOINTS_CATALOG.json`, holds 18 per-method records, and `success_endpoints` is exactly `GET /reader`.
* The Aux spellings are one canonical `GET /aux/narrative` record with `classification:"public_aux"`, `internal:false`, `env_gate:"not_applicable_public"`, `a7_eligible:false` and `aliases:["/api/aux/narrative"]`.
* No record exists for `/internal/admin/bundle/v1`; a bounded search of `adapter/` and `engine/` finds no such route (§5.10).
* No record carries `/ops/db/unavailable`, `/ops/probe/env` or `/ops/writer/diagnostic`, the routes **HDE-Architecture** and **HDE-Users-Guide** mark retired and noncanonical. The validator in `tools/evidence/generate_a7_transport_proofs.py` refuses a record whose path or alias is one of them, and `tests/http/test_endpoint_catalog.py` asserts that every served method and path is accounted for exactly once, by one record or by one exclusion with its recorded basis.

HDE Build Notes records the HDE-CRD-0002 decision CR-7 behind this state: a registered route that canon retires and excludes from the Endpoint Catalog is accounted for by that exclusion, not by a record, and its removal stays with its canon owner. The Catalog went from 23 records to 18 when the five records for those three routes were removed. The population rule and its exclusion classes stay in **HDE-Schemas & Artifacts**. These findings concern checked-in bytes only; they do not establish reachability, deployment, QA, OPS or acceptance state.
````

## RL-03

- Redline ID: RL-03
- Operation: `REPLACE`
- Change type: CANON_UPDATE
- Source items: S-APR (S14 makes the "Required-Now implementation gap (DD-04; held)" paragraph stale); A09 with X05 (§17 row for this paragraph); A09 LR4-O2 and the carried OBS-W4-1 as limits; X14 (`DD-04`, `FND-012` and the S14 line) as the source of the recorded limits
- Target document: `PF05-Canon-HDE-CLI-API-Vendor-Ref`
- Section path: line 3315: `# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**` > line 3317: `## **7.1 Rails & Environment \[Required-Now\]**` > line 3498: `### **7.1.11 SAFE rails and production vendor override**`
- Location: original line 3500; the bold-labelled paragraph immediately under the §7.1.11 heading
- Scope and expected count: whole PF; expected 1; observed 1
- Rationale: S14 delivered `--allow-prod-vendor` and its audit gate, so "not an available CLI facility" and "do not invoke or describe the flag as operational" are stale. The replacement records the delivery, the implementation verified at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c` and its recorded limits. The contract in §7.1.11a to §7.1.11f is unchanged, and §7.1.11f's clock term (H-04) is not touched.
- OLD (694 bytes; SHA-256 `f1561d111595e852fcb8bc72398995432c164c1c647b138372ce7ca5cbcd4a46`; ends with LF: no):

````text
**Required-Now implementation gap (DD-04; held).** The following production override contract is a requirement, not an available CLI facility. At `main@e7265a090ad0cc8de5f36de2f19481216aa3d073`, bounded parser/resolver inspection finds no `--allow-prod-vendor` implementation or corresponding authenticated override/audit gate. HDE Build Notes records DD-04 / QA50-B01 outside HDE-EPIC040, retained by the PF05 and CLI owners through change control. Neither the Reader deliveries, exceptional closure nor the directed-agent vendor rule implements or waives this contract. Preserve its required flag, authentication, rails and audit predicates; do not invoke or describe the flag as operational.
````

- NEW (1986 bytes; SHA-256 `140bb0df3b787874be8c4f94d577b6621f5f8ad3e57f64a48706cbec8fa9a42a`; ends with LF: no):

````text
**Implementation state (informative).** HDE-CRD-0002 delivered this contract as its requirement S14, and HDE Build Notes records the delivery. That delivery resolves the DD-04 / QA50-B01 implementation gap recorded outside HDE-EPIC040. Bounded static inspection at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c` finds:

* the §7.1.11a flag, its pre-scan and its usage refusals in `engine/cli/main.py`;
* the §7.1.11b classification, the §7.1.11c matrix and the §7.1.11d order in `engine/bodygraph/resolver.py`;
* the §7.1.11f record in `engine/bodygraph/vendor_audit.py`: its sixteen keys are appended as one canonical JSON line to a file created owner-only, and the file and its directory entries are fsynced before vendor I/O;
* the audit sink at the path in `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, otherwise `glow-hdengine/vendor_prod_override.jsonl` under an absolute `XDG_STATE_HOME` or under `~/.local/state`; a relative sink, or one inside the repository checkout, is refused as `PROVIDER_AUDIT_UNAVAILABLE`;
* the actor taken as the account name of the process's effective user ID, read from the system user database.

These limits apply:

* An account name identifies an account, not necessarily a person. §7.1.11e still decides who may initiate, and supplying the flag authorizes nothing by itself.
* The gate covers only the command §7.1.11a names. Vendor acquisition through the compat chart resolver, which `hdctl showcompat --source vendor` and its conjunction mode use, applies the generic rails but not this gate. The HDE-CRD-0002 close report defers that gap to the Product Owner as pending and non-gating.
* The same close report records S14 as met: one check proves the local matrix, and one covers a single bounded live vendor call initiated by the Product Owner, not broad HumanDesignAPI v2 conformance.

This inspection concerns checked-in bytes only, and a close-report record is not a QA verdict; neither establishes runtime behavior, deployment or acceptance.
````

## RL-04

- Redline ID: RL-04
- Operation: `REPLACE`
- Change type: CANON_UPDATE
- Source items: A09 with X05 (§17 row: §7.2.0 "lists 'no production-vendor override flag or audit gate' among the material gaps")
- Target document: `PF05-Canon-HDE-CLI-API-Vendor-Ref`
- Section path: line 3315: `# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**` > line 3599: `## **7.2 Request Shaping (owned here) \[Required-Now\]**` > line 3603: `### **7.2.0 Contract and implementation posture**`
- Location: original line 3605; the first paragraph of §7.2.0
- Scope and expected count: whole PF; expected 1; observed 1
- Rationale: The delivered override is no longer a gap. The two remaining gaps were re-verified at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c`, so the inspection is pinned to that commit.
- OLD (534 bytes; SHA-256 `c92c423362b1ccd682cd6df639ce709862c86c5e291e58b9f302fc1770222ead`; ends with LF: no):

````text
The contract in this section is Required-Now. Static inspection of the pinned repository confirms low-level request builders for all five inventoried resources and current resolver selection of v2 `charts` or legacy `bodygraphs`; it also shows material gaps against this contract: broad non-v2 legacy selection, no production-vendor override flag or audit gate, and retry configuration outside the five approved tuples. Repository definitions do not establish runtime success, deployment, live-provider availability, or QA acceptance.
````

- NEW (631 bytes; SHA-256 `4827e9ec774c76b70c23301588df2b258f75055d09a9f4c7376ffa5ef7b9f7ec`; ends with LF: no):

````text
The contract in this section is Required-Now. Static inspection at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c` confirms low-level request builders for all five inventoried resources and current resolver selection of v2 `charts` or legacy `bodygraphs`; it also shows two material gaps against this contract: broad non-v2 legacy selection, and retry configuration outside the five approved tuples. The production-vendor override flag and audit gate, a third gap in the earlier inspection, are delivered (§7.1.11). Repository definitions do not establish runtime success, deployment, live-provider availability, or QA acceptance.
````

## RL-05

- Redline ID: RL-05
- Operation: `INSERT`
- Change type: CONSISTENCY (change-history entry the target's own rules require)
- Source items: PF05 §0.4 "Editorial vs. normative" and §11.1 "Policy" and "Entry style"; the changes of RL-01 to RL-04
- Target document: `PF05-Canon-HDE-CLI-API-Vendor-Ref`
- Section path: line 4113: `# **11\. Change Log & Doc-Delta Hooks \[Required-Now\]**` > line 4115: `## **11.1 Change Log (concise, normative)**`
- Location: original line 4127; the gap between the `v2.5.3` Change Log entry and the "Where to put links." bullet
- Scope and expected count: whole PF; expected 1; observed 1
- Rationale: RL-03 lifts the canon directive "do not invoke or describe the flag as operational", a normative delta that §0.4 and §11.1 require to be logged. The entry uses the target's one-line format and names the version TW-APPLY-10 derives (v2.5.3 bumped once, v2.5.4). The format records no date.
- BEFORE anchor (445 bytes; SHA-256 `e5c18567bd896f69d90742aad08e8dcd1c764f7cb2923053da7ce0729979f302`; ends with LF: yes; occurs once):

````text
* v2.5.3 — Admit production Reader v1/v2 on the distinct POST mount; define ordered v2 projection/examples and inherited transport; correct v1 success/error schema references and resolve PR04 F03/F05/F07 deferrals; conform directed-agent vendor execution and environment/base-URL alias facts; retain held DD-04 and proof/availability limits in §§0.2, 1, 3.7, 4.1, 5.1–5.6, 5.12, 6, 7.1, 7.4, 8.1, 9.1 and Appendix C. Sentinel updated: NO.
````

- AFTER anchor (417 bytes; SHA-256 `adafe4dbe84db32b463a0a5826518a11e8d7954a9ebc1f86d2c196215b139f73`; ends with LF: no; occurs once; it begins immediately after the BEFORE anchor):

````text
* **Where to put links.** Governed artifact identities and paths are indexed through the Evidence Catalog in **HDE-Schemas & Artifacts**; do not paste payload or transport bytes here. If the Human Evidence Index changes, record “Sentinel updated: YES” only after recomputing `docs/evidence/INDEX.sha256`; the sentinel is the SHA-256 digest of the canonical bytes of `docs/evidence/INDEX.json` and is not mirrored.
````

- INSERTED TEXT (252 bytes; SHA-256 `a68f4e6f41c980a21969654ba944a4fc91e67c0a182206f17de8e0a31edd15ad`; ends with LF: yes), placed at the gap between the two anchors:

````text
* v2.5.4 — Record the delivered production vendor override and its limits in §7.1.11, remove it from the gap statements in §§1 and 7.2.0, and record the Endpoint Catalog state with the canon-retired route exclusion in §5.6. Sentinel updated: NO.
````

END OF REDLINES
