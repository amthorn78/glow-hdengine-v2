# HDE-EPIC042 doc deltas (Step-0B)

## BLOCKERS

none

## CAVEATS

- DELTA-001: `README.md` line 115 says the endpoint catalog entry for `/api/compat/v1` is POST-only, while `docs/ENDPOINTS_CATALOG.json` lists 4 methods for that path (POST, GET, HEAD, OPTIONS) (Reality Audit RA-20261112-03; Guide IR-15). Target: `README.md`. Owner: Product Owner. CAVEAT; drives decision: No; a non-mandatory drain candidate owned by the Product Owner.
- DELTA-002: `AGENTS.md` still names `docs/pfcanon` on lines 49, 69, 141, 190, 204. Target: `AGENTS.md`. Owner: Product Owner. CAVEAT; drives decision: No; a non-mandatory drain candidate owned by the Product Owner.
- DELTA-003: `tools/ci/prepush_check.py` line 776 says a `documentation_only` change starts no hosted run; run 43676636514 started. Target: the pre-push tool's note. Owner: Product Owner. CAVEAT; drives decision: No; a non-mandatory drain candidate owned by the Product Owner.
- DELTA-004: HDE Build Notes text points of triage finding A-19, and its "Implementation status: Not started" line for the offsets. Target: HDE Build Notes. Owner: Product Owner. CAVEAT; drives decision: No; a non-mandatory drain candidate owned by the Product Owner.
- DELTA-005: the doc-delta record of the Magic10 v2 file paths that HDE Schemas & Artifacts asks the implementing change to make (Specification constraint C-09) is owed at close. Target: HDE Schemas & Artifacts. Owner: CL-05's operator. CAVEAT; drives decision: No; a non-mandatory drain candidate.
- DELTA-006: the evidence writer holds no QA registration for HDE-EPIC042 (`tools/evidence/update_evidence_index.py` holds 0 lines naming `audit/qa/hde-epic042/checks/`). Target: the writer registration of QA Plan v1.1 section 5.5. Owner: Product Owner. CAVEAT; drives decision: No; a non-mandatory drain candidate owned by the Product Owner.

plan-against-execution drift from qa-01: none
