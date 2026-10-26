# HDE-CRD-0002 doc deltas

Sources: QA RCA v1.0 section 9 (docs/ephemeral/HDE-CRD-0002-QA120-qa-rca-v1.0.md), the CL-C-10 closure decision v1.0 sections 7 and 8, and this close pull request. Check 1 (qa-01-preflight) found no Step-0B doc-delta surface (CR-11).

- PO-5, evidence persistence. Target: Glow QA Guide section 3.4.3. Owner: Product Owner. State: PENDING_DRAINAGE (HDE Build Notes 2.28).
- PO-2, do not pin tool versions. Target: the owner's choice of home. Owner: Product Owner. State: PENDING_DRAINAGE.
- D-1 of the QA RCA. Target: Plan Templates; a code-identity guard that excludes storage paths uses the classifier's whole set of CI-exempt storage prefixes. Owner: Product Owner. State: proposed.
- LR5-O1, the IR-3 observation (GET //reader?v=1 answered 403 directly). Target: as the Product Owner decides. Owner: Product Owner. State: recorded, no predicate.
- The S21 ADR's affected canon homes (docs/adr/hde/close_pack_writer_adr.md, "Affected canon and drainage consequences"). Owner: Product Owner, through canon maintenance. State: undrained; HDE Build Notes 2.15 and 2.17 govern.
- QA110-F01 remedy limits. Recorded in HDE Build Notes 2.27 and README.md "Pre-push check (HDE-CRD-0002)". State: recorded; no further delta.
- RF-12. README.md, AGENTS.md and CHANGELOG.md nonclaim lines now state that HDE-CRD-0002's close pack, candidate source and close-run family are the only ones produced with the v2 writer. Owner: this close work. State: applied in this close pull request.
