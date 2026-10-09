# Triage — GTWPE-FLOW-10 run `gtwpe-20261009-hde-epic040-specification`

Pass: TW-TRIAGE-10 — Identify PF10 Drain Targets — 100726.1 (Notion `3f24590a05eb8129b8e5e8328f9a3c3d`).

## Files read

Read from `origin/main` at commit `0c4dddece401c457b2429ddc9cb8f2e819b4a943`:

| File (repository path) | Blob at intake |
| --- | --- |
| `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` | `5937f0186298423052864822ec10500d9602115d` |
| `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` | `34c17fc52a751b7a4627165673cc2d08336daa66` |
| `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` | `e203c84c91e5584d55fcca03beadad00b57f4539` |
| `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` (editorial discipline) | `27a66aefde14e10e75cb8ed1d6d226a099f0d1b8` |

## Changes and eligible documents

Eligible documents are PF03, every PF document with `Canon` in its title, each PF09 phase file, `PF20-Reference-HDE-Phased-Epics` and the PF30 family. `PF10` and every other file is never a target. Named below by canon file name without its version.

### A. Changes carried by PF10-HDE-Build-Notes (38 addenda)

All HDE-EPIC040-scoped addenda belong to Epic `HDE-EPIC040`; the files given (the closure decision) show it `CHANGE_CLOSED`. The general `PF10-*`-coded addenda are repo-wide governance rulings, not owned by any epic.

| # | Change (addendum) | Epic / closed | Eligible documents (canon name) | Non-drainable part / reason |
| --- | --- | --- | --- | --- |
| 1 | 2.1 Establish the Notion development board and stable historical-source resolution | general | HDE Phased Epics; HD Engine Epics Map; HDE CRD Records | Exact permanent home not fixed in canon — the pass decides |
| 2 | 2.2 Canonize HDE-EPIC040 source-conflict ADR decisions (C040-01–04) | HDE-EPIC040 / closed | HDE Build Checklist — Separation (C040-01); HDE Schemas and Artifacts (C040-02); HDE Mechanics Guide (C040-03); Glow QA Guide (C040-04) | — |
| 3 | 2.3 Reconcile superseded core-test instructions (C040-05) | HDE-EPIC040 / closed | HDE Mechanics Guide | — |
| 4 | 2.4 Record in-flight resolution of C040-01 through C040-04 | HDE-EPIC040 / closed | HDE Build Checklist — Separation; HDE Schemas and Artifacts; HDE Mechanics Guide; Glow QA Guide | Record; drainage identical to 2.2 |
| 5 | 2.5 Record the approved source-backed Channel taxonomy and existing-state conformance (C040-06) | HDE-EPIC040 / closed | HDE Schemas and Artifacts; HDE Math Spec | — |
| 6 | 2.6 HDE-EPIC040-PR01 — Accept Source-Proven Catalog and Exact Contract Data | HDE-EPIC040 / closed | HDE Schemas and Artifacts; HDE Math Spec | Drainage captured under C040-06 |
| 7 | 2.7 HDE-EPIC040-PR02 — Rescoping | HDE-EPIC040 / closed | HDE Math Spec; HDE Governance; HDE CLI/API Vendor Ref; HDE Schemas and Artifacts | Drainage captured under C040-07 |
| 8 | 2.8 PF10-FORM-001 — Establish Page-Ready Canonical Form for Agent-Authored Addenda | general | — | No eligible home: governs PF10 addenda themselves, and PF10 is never a target |
| 9 | 2.9 HDE-EPIC040-PR02-F02 — Executing-Code Coherence Rescope | HDE-EPIC040 / closed | HDE Schemas and Artifacts; HDE Mechanics Guide | Drainage captured under C040-06 / C040-07 |
| 10 | 2.10 HDE-EPIC040-PR02-F03 — Existing Serializer Manifest Binding Refresh | HDE-EPIC040 / closed | HDE Schemas and Artifacts | Drainage captured under C040-06 |
| 11 | 2.11 HDE-EPIC040-PR02 — PR Work-Unit Lineage Review v1.0 | HDE-EPIC040 / closed | (none beyond register) | Lineage record; drainage captured under C040-05–10 |
| 12 | 2.12 HDE-EPIC040-PR03-R02 — Bind Executing Mechanics to the Admitted Release | HDE-EPIC040 / closed | HDE Schemas and Artifacts; HDE Mechanics Guide; HDE Math Spec | Drainage captured under C040-06 / C040-07 |
| 13 | 2.13 HDE-EPIC040-PR03 — PR Work-Unit Lineage Review v1.0 | HDE-EPIC040 / closed | (none beyond register) | Lineage record |
| 14 | 2.14 Specification format authority | general | Change Process Guide; Plan Templates | Exact home not fixed — the pass decides |
| 15 | 2.15 HDE-EPIC040-PR04-F01 — Truthful Non-Admitted Gate Outcome for the PR04-to-PR06 Interval | HDE-EPIC040 / closed | HDE Schemas and Artifacts | Lineage record; no independent canon delta |
| 16 | 2.16 HDE-EPIC040-PR04-F03 — Production Reader route gap: PO deferral | HDE-EPIC040 / closed | HDE CLI/API Vendor Ref | Deferral decision |
| 17 | 2.17 HDE-EPIC040-PR04-F05 — Reader response vs published schema: PO deferral | HDE-EPIC040 / closed | HDE CLI/API Vendor Ref; HDE Schemas and Artifacts | Deferral decision |
| 18 | 2.18 HDE-EPIC040-PR04-F07 — Dev conjunction evidence capture unrunnable: PO deferral | HDE-EPIC040 / closed | HDE CLI/API Vendor Ref | Deferral decision |
| 19 | 2.19 HDE-EPIC040-PR04-LINEAGE-001 — Bounded Application, Identity, and Consumer Integration | HDE-EPIC040 / closed | HDE Schemas and Artifacts | Lineage record |
| 20 | 2.20 HDE-EPIC040-PR05 — PR Work-Unit Lineage Review v1.0 | HDE-EPIC040 / closed | (none beyond register) | Lineage record |
| 21 | 2.21 HDE-EPIC040-PR06-F01 — Frozen-capture identity source for the canonical JSON gate | HDE-EPIC040 / closed | HDE Schemas and Artifacts | Lineage record |
| 22 | 2.22 HDE-EPIC040-PR06 — PR Work-Unit Lineage Review v1.0 | HDE-EPIC040 / closed | (none beyond register) | Lineage record |
| 23 | 2.23 HDE-EPIC040-PR07-F01 — Add PR06a for Reader v2 Full Magic-10 Exposure and the Deferred Reader Contract Work (C040-07) | HDE-EPIC040 / closed | HDE Math Spec; HDE Governance; HDE CLI/API Vendor Ref; HDE Schemas and Artifacts | — |
| 24 | 2.24 HDE-EPIC040-PR06a — PR Work-Unit Lineage Review v1.0 | HDE-EPIC040 / closed | (none beyond register) | Lineage record |
| 25 | 2.25 HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08) | HDE-EPIC040 / closed | HDE Math Spec; HDE Governance | — |
| 26 | 2.26 HDE-EPIC040-PR06b — PR Work-Unit Lineage Review v1.0 | HDE-EPIC040 / closed | (none beyond register) | Lineage record |
| 27 | 2.27 HDE-EPIC040-OPS01 — OPS_EXECUTION_RESULT v1.4 | HDE-EPIC040 / closed | HDE CLI/API Vendor Ref | OPS record; no independent canon delta |
| 28 | 2.28 HDE-EPIC040 — Change Audit Triage v1.0 (QA-10) | HDE-EPIC040 / closed | (register items; see C040 / DD below) | Analytical record |
| 29 | 2.29 PF10-CANON-001 — Repository PF-Canon Authority, Change-Process Document Storage and Canon Consultation | general | HDE Governance; Glow QA Guide; HDE Mechanics Guide; HDE Build Checklist — Calcination | Addendum 2.1's own passage is also superseded (PF10-internal) |
| 30 | 2.30 PF10-CITE-001 — PF Documents Do Not Cite HDE Build Notes by Internal Locator | general | HDE Governance; HDE Build Checklist — Calcination; HDE Build Checklist — Separation; HDE Build Checklist — Conjunction; HDE Build Checklist — Coagulation; HDE Mechanics Guide | — |
| 31 | 2.31 PF10-HDR-001 — Retirement of the Human Operator Header Model-Advice Review | general | HDE Governance | — |
| 32 | 2.32 HDE-EPIC040-QA110 — QA Evidence Review v1.0 (T01–T10) | HDE-EPIC040 / closed | (register items; see C040 below) | Review record |
| 33 | 2.33 PF10-OPENRAILS-001 — Mandatory Live Vendor Open-Rails Test | general | Plan Templates; Change Process Guide; Glow QA Guide; HDE Governance; HDE Architecture; Glow Infrastructure; HDE Mechanics Guide | — |
| 34 | 2.34 PF10-VENDOR-001 — Agents Run Live Vendor Calls When the PO Directs | general | Glow QA Guide; HDE CLI/API Vendor Ref; HDE Governance; HDE Mechanics Guide; Plan Templates; HDE Build Checklist — Fermentation | — |
| 35 | 2.35 HDE-EPIC040-QA110 — QA Evidence Review of T11 | HDE-EPIC040 / closed | (C040-10; see register) | Review record |
| 36 | 2.36 HDE-EPIC040-QA110 — QA Evidence Review of T12 | HDE-EPIC040 / closed | (C040-10 history) | Review record |
| 37 | 2.37 HDE-EPIC040-QA120 — Final QA Report (PASS) and QA RCA | HDE-EPIC040 / closed | (see DD-01–13, PF19D-001–004, OPFD-001–002 below) | Review record |
| 38 | 2.38 PF10-AINEUTRAL-001 — Governance Requires No Specific AI Provider, Product or Model | general | HDE Governance; Change Process Guide; Plan Templates; Glow QA Guide; HDE Mechanics Guide; Glow Infrastructure; HDE Architecture; Reality Audits | PF10 front matter "Cross-references" passage is also superseded (PF10-internal) |

### B. Changes carried by the closure decision (CL-E-10 v1.2 §5)

All belong to Epic `HDE-EPIC040`, shown `CHANGE_CLOSED`.

| ID | Change | Eligible documents (canon name) | Non-drainable part / reason |
| --- | --- | --- | --- |
| CC-1 | Name the governed writer for a canon-conforming close report and manifest | Change Process Guide; HDE Schemas and Artifacts; HDE Governance; Glow QA Guide | `AGENTS.md` leg has no PF home (repository docs) |
| CC-2 | Admit a home for close-workflow same-run execution evidence | Glow QA Guide; HDE Schemas and Artifacts | — |
| CC-3 | Evidence-only QA branch allowed-change list omits QA-root artifacts | Change Process Guide | — |
| CC-4 | Closure-evidence prompt path before CL-E-10; planned close mutation set | — | Process, not canon: routed to GCFPE-MGMT-10 (no PF home) |
| CC-5 | State where the exceptional closure record lives and its form | Change Process Guide | — |
| CC-6 | Plan Templates §10 scope rule vs Change Process Guide §3.5 | Plan Templates | — |
| PF19D-001 | Glow QA Guide §2.3 rails-posture pointer | Glow QA Guide | — |
| PF19D-002 | Glow QA Guide §3.4.8 "production endpoints" scope | Glow QA Guide | — |
| PF19D-003 | Glow QA Guide §9.2.15.5 evidence-branch check | Glow QA Guide | — |
| PF19D-004 | Glow QA Guide §4.4.6 executor/recorder identity | Glow QA Guide | — |
| OPFD-001 | Glow Infrastructure §2.4 rails pair / Codespaces inventory | Glow Infrastructure | — |
| OPFD-002 | Change Process Guide §0.4.1.2 QA RCA summary placement | Change Process Guide | — |
| DD-01 | QA Codespaces inventory lists retired DB_BRIDGE_URL | Glow Infrastructure | — |
| DD-02 | Glow Infrastructure §2.8 vs Glow QA Guide §3.4.9 / Plan Templates | Glow Infrastructure | — |
| DD-03 | Glow QA Guide §§3.4.3, 3.6, 10.8 name ChatGPT Library / Google Drive | Glow QA Guide | — |
| DD-04 | HDE CLI/API Vendor Ref §7.1.11 `--allow-prod-vendor` not implemented | HDE CLI/API Vendor Ref | — |
| DD-05 | `AGENTS.md` "PF10 §2.8" citation | — | Repository docs (no PF home) |
| DD-06 | Guide §8 attestation candidate hash mismatch | — | Ephemeral record (no drain target) |
| DD-07 | Drainage of C040-05 to C040-08 | (see C040-05–08) | Already accounted in register |
| DD-08 | showcompat help says Reader v1 | — | Repository CLI help (no PF home) |
| DD-09 | APP_ENV asymmetry dev GET /reader vs conjunction routes | — | Whole-change IA (no direct PF home) |
| DD-10 | `ci/checks/check_mirror_schema.sh` is Python | — | Repository docs (no PF home) |
| DD-11 | docs/ADAPTER_009.md:174 body_not_allowed vs invalid_json | — | Repository compat docs (no PF home) |
| DD-12 | Addendum 2.28 line references off by two | — | PF10 itself (never a target) |
| DD-13 | HDE CLI/API Vendor Ref §3.7 HDAPI_BASE_URL alias | HDE CLI/API Vendor Ref | — |
| C040-05 | Reconcile superseded core-test instructions | HDE Mechanics Guide | — |
| C040-06 | Channel taxonomy | HDE Schemas and Artifacts; HDE Math Spec | — |
| C040-07 | Reader v2 / Magic-10 exposure | HDE Math Spec; HDE Governance; HDE CLI/API Vendor Ref; HDE Schemas and Artifacts | PF14, PF29 consequences (recorded) |
| C040-08 | Reader v1 error-envelope conformance | HDE Math Spec; HDE Governance | — |
| C040-09 | Glow Infrastructure §2.8 wording | Glow Infrastructure | — |
| C040-10 | Passages in 2.34's superseded-passage table | Glow QA Guide; HDE CLI/API Vendor Ref; HDE Governance; HDE Mechanics Guide; Plan Templates; HDE Build Checklist — Fermentation | — |

### C. Changes carried by the governing specification (§10.3 ADR proposals C040-01–04)

Belong to Epic `HDE-EPIC040`; shown `CHANGE_CLOSED`. These four proposals are already canonized by PF10 addendum 2.2 (part A item 2): their drainage targets are HDE Build Checklist — Separation (C040-01), HDE Schemas and Artifacts (C040-02), HDE Mechanics Guide (C040-03), Glow QA Guide (C040-04). No change beyond 2.2's account.

## Eligible documents (roll-up)

Distinct target documents named above (canon file name, no version): HDE Math Spec; HDE Architecture; HDE Governance; HDE CLI/API Vendor Ref; Change Process Guide; Glow Infrastructure; HDE Build Checklist — Calcination; HDE Build Checklist — Separation; HDE Build Checklist — Conjunction; HDE Build Checklist — Fermentation; HDE Build Checklist — Coagulation; HDE Schemas and Artifacts; HDE Mechanics Guide; HD Engine Epics Map; Glow QA Guide; HDE Phased Epics; Reality Audits; Plan Templates; HDE CRD Records.

Eligible but not named by any change: Technical Writing Best Practices (PF03); HDE Build Checklist — Dissolution; HDE Build Checklist — Distillation; HDE Narratives Guide; HDE Users Guide.

Never a target: PF10-HDE-Build-Notes; all other Reference files; every repository (non-PF) document, including `AGENTS.md`.

