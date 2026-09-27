---
artifact_type: CHANGE_AUDIT_TRIAGE
artifact_id: HDE-EPIC040-QA10-CHANGE-AUDIT-TRIAGE
artifact_version: "1.0"
predecessor: none
state: COMPLETE
change_class: EPIC
change_id: HDE-EPIC040
producer: Isis — continuing Lead Developer and whole-change readiness decision owner (Isis-50 session)
session_disposition: RETAIN_EXISTING
invocation_binding: EPIC / HDE-EPIC040 / QA-10 / whole change
execution_posture: MANUAL_PROMPT_EXECUTION
audit_ref: docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md
readiness_ref: docs/ephemeral/HDE-EPIC040-QA10-qa-readiness-v1.0.md
observed_revision: 39b9cdf
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-10
---

# HDE-EPIC040 — Change Audit Triage v1.0 (QA-10)

Every observation in the Reality Audit §12 (RA-01 to RA-18) and every historical PF23 finding carried there has exactly one row below. This is an analytical record, not PF10 text. No finding here is an evidenced failure of an approved Plan objective; the readiness record carries that conclusion.

## 1. Findings requiring no action

| Finding | Observed | Requirement / decision | Repo check | Disposition |
| --- | --- | --- | --- | --- |
| RA-01 | Catalog (36 ascending, no null substreams), mechanics config (20 signals, 2 Balance operations), 3 schemas, fail-closed loader, roster 1.3.0/45 matching the manifest exactly, pure four-argument core | Spec K040-REQ-003–009; Plan §§5.1–5.7 | Confirmed (E-B02–E-B29, E-B27) | No action. No doc delta: documented per DOC-20 R1–R5, A5 |
| RA-02 | Reader v1 harmony-only; Reader v2 ten ordered `{id, band}`; `POST /api/reader`; governed 405 | PF10 §2.23 (C040-07), §2.25 (C040-08) | Confirmed (E-B14, E-B15, E-C10–E-C13) | No action. Documented (DOC-20 A1–A3) |
| RA-03 | All six read-only evidence and release validators pass; Index/Mirror 606/606 | Spec K040-REQ-012; PF12 evidence contracts | Confirmed (E-D01–E-D06) | No action |
| FND-019, FND-023, FND-024 (PF23) | Resolved since 2026-09-06 | PF23 v1.2 §12 | Confirmed (E-D24, E-D27, E-D28) | No action; historical |
| FND-021 (PF23) | Public paths reach `compute_core` through compat compute | Plan §4.1 one data-to-result path | Confirmed changed (N-D05, E-D25) | No action: the change is the intended Plan outcome. The historical N-007 proof stays true for the three files |

## 2. Carried items with existing owners (non-gating)

| Finding | Observed behaviour | Applicable decision | Implications | Owner and route | Doc delta | Must act now |
| --- | --- | --- | --- | --- | --- | --- |
| RA-04 (O-12) | A non-editable wheel omits release members, so admission refuses `MISSING_FILE`; `pyproject.toml` `dependencies = []` | PF10 §2.22: Product Owner distribution decision, not material to PR06 | Affects only wheel installs; the Procfile serves from the source tree | Packaging owner / Product Owner; Candidate CRD Items List item 5 | No delta needed: README documents the limitation (DOC-20 P3) | NO |
| RA-05 (O-P06a-22) | HTML 404 for unknown non-compat paths on `adapter.factory` and `adapter.http_reader`; JSON on `adapter.wsgi` | PF10 §2.24: HTTP transport owner, non-gating | Production (Procfile) uses `adapter.factory`, so the HTML 404 is live there | HTTP transport owner; CRD candidate 5 | Documented (`docs/server/reader_v1.md`) | NO |
| RA-06 (O-P07-04, extended) | Dev `GET /reader` treats unset `APP_ENV` as dev and refuses `test`; conjunction routes allow dev/test/local and refuse unset | AGENTS.md: dev routes gated to `dev\|test\|local` | The two dev surfaces disagree; the `test` refusal on dev `GET /reader` is new detail beyond O-P07-04 | Whole-change IA through change control (DOC-20 §6) | Proposed: add the `APP_ENV=test` asymmetry to the O-P07-04 record at its next update | NO |
| RA-07 (O-P07-01, -02, -03) | showcompat help says Reader v1; `--band` ignored with `--pair-file`; dev harness `app.getattr` | DOC-20 §6 | Misleading help and a silently ignored flag on a CLI surface | Whole-change IA through change control | Documented as labelled gaps | NO |
| O-P06a-03 | `tests/reader_v1/test_cli_proof.py` fails at baseline | PF10 §2.24 | Known red test outside the lanes | PR07/IA backlog owner | No delta | NO |
| O-P06a-23, O-P06b-17 | Evidence-owner items (engine-core evidence owner; Mirror origin labels) | PF10 §§2.24, 2.26 | None for readiness | Evidence owner | No delta | NO |
| O-OPS01-01, -02 | Closure probe depends on the installed package; delegation template | OPS01 receipt v1.2 §5 | None for readiness | Evidence-tool owner; IA | No delta | NO |
| RA-18 | C040-05, -06, -07, -08 drainage pending | PF10 §§2.3, 2.5, 2.23, 2.25 | Canon text lags the delivered contract (PF04 OI-001 still "future") | PF01, PF04, PF05, PF12, PF14, PF29 maintainers | Drainage is their act; the repo documentation already states it (DOC-20 K2) | NO |

## 3. QA planning obligations (reserved for QA, not failures)

| Finding | Observed | Applicable requirement | Route |
| --- | --- | --- | --- |
| RA-10 | Readiness tool proven offline only; no live observation against current rows; no open-rails run of the affected CLI/vendor surfaces | Plan Review v2.1 §5.4 citing PF05 §7.3.9 (bounded open-rails QA step unless the PO or Canon exempts it); PF10 §2.20 L2214 | QA-20 Guide and QA Plan must include the bounded open-rails step, or record the PO/Canon exemption before QA approval |
| RA-09 | Security review never covered the implementation deltas: PR04 and PR06 none, PR05 and PR06a first push only | PF10 §2.19 L2104 leaves "whether a current-head review is required before … QA" undecided | Open question for the PO (triage Q-1); QA-20 should include a bounded security check of the public Reader surface either way |
| RA-08 | 189 test files named by no fixed lane or roster; recorded 57 failed / 13 errors among them (PR05 sweep); O-P06a-03 red | Spec K040-REQ-011 (coverage of the selected surfaces is met by the lanes; these files are outside them) | QA-20 should define which of these files QA runs and treat their pre-existing failures as baseline, not as QA results. Repair is CRD candidate 5 |

## 4. Informational observations

| Finding | Observed | Why no readiness effect | Owner / route | Doc delta |
| --- | --- | --- | --- | --- |
| RA-11 | `bg:resolve` writes with `sys.stdout.write`, bypassing the LF/CRLF guard | The guard is required for showcompat stdout (AGENTS.md); no source found requiring it for `bg:resolve` (not proven either way) | CLI owner through change control | No delta needed |
| RA-12 | `ci.yml` `paths-ignore` has 4 prefixes; the classifier exempts 8 | Documented behaviour: extra prefixes still trigger CI but select no lanes | CI owner | No delta needed; the AGENTS.md note already names `_DOCUMENTATION_PREFIXES` as the list |
| RA-13 | `ci/checks/check_mirror_schema.sh` is a Python script; running it with `bash` fails | CI invokes it directly and it passes (E-D04) | Repo docs owner | Proposed: AGENTS.md should show direct invocation (`./ci/checks/check_mirror_schema.sh`) |
| RA-14 / FND-025 | Aux, ops and health routes are not catalogue rows | The catalogue is a bounded success-proof family (PF23 §5); inclusion policy not established | Endpoint-catalog owner | Open question retained from PF23 |
| RA-15 | NaN refused only upstream; rebindable compat globals; admission per call | No failure observed; no explicit Canon rule found | Engine owner | No delta |
| RA-16 / FND-012 | Zero-byte root files, scratch files, placeholder `catalog/channels_catalog_v1.json`, duplicate `hdctl` scripts, `pytest.ini` scope differs from CI | Hygiene; the placeholder catalog is not a roster member and unreferenced | Repo owner; fits CRD candidate 5 | No delta |
| RA-17 | PF10 v13.3.8 line 1374 ends mid-word ("…persistence remains p") in the stored file; §2.27 missing from the §1.1 index | Persistent, not new: already recorded as O-P06-21 (PR06 result v1.1 §10, against v13.3.2 line 1,369). The same truncated sentence is present in every PF10 version in Git from v13.2.8 (`210250c`) to v13.3.8 (`47e2b97`). It is the §2.11 §8 prompt-use sentence; no decision depends on it. No intact copy exists in the repository | Nathan / PF10 drain owner (O-P06-21; PF-Canon is read-only for agents) | Duplicate of O-P06-21 for the truncation; proposed: add §2.27 to the index at the next PF10 publication |
| FND-001–011, 013–016, 020, 022 (PF23) | Persistent as recorded | Historical structure; none is an HDE-EPIC040 objective | Existing PF23 owners | No new delta; the full audit is available for the PO's PF23 update |
| FND-017 (PF23) | `docs/ADAPTER_009.md:174` says `body_not_allowed`; code emits `invalid_json` | Pre-existing compat docs drift, outside this change | Compat docs owner | Doc delta proposed (persistent since 2026-09-06) |
| FND-018 (PF23) | Hosted CI history | Not repo-verifiable here; current exact-head CI results are recorded per unit | — | No delta |

## 5. Open questions for the Product Owner

| ID | Question | Why it is his | Recommendation |
| --- | --- | --- | --- |
| Q-1 | Is a security review of the delivered Reader and admission code required before or within QA? | PF10 §2.19 leaves it undecided; it is policy | Yes, as one bounded QA step on `POST /api/reader` and admission refusals, rather than reopening accepted PRs |
| Q-2 | Does the PF05 §7.3.9 open-rails QA step apply, or is it exempted? | Plan Review §5.4 reserves the exemption to the PO or Canon | Keep it: include the bounded open-rails step in QA |

## 6. Accounting

- Findings triaged: RA-01 to RA-18, PF23 FND-001 to FND-025, carried O-items. Each has one row above.
- Objective failures: none evidenced.
- Proposed documentation deltas: RA-06, RA-13, RA-17, FND-017. None is required before QA.
- `PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-10`.
- `CANON_CONFLICT_REGISTER`: C040-01 to C040-08 carried unchanged (status in the readiness record §5).
