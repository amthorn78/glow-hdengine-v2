---
artifact_type: QA_PLAN
artifact_id: HDE-EPIC040-QA50-QA-PLAN
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md (QA_PLAN v1.0, PLAN_PENDING; DENY by the QA-70 review v1.1; preserved unchanged; SHA-256 f3500c4952d4ee4f2080c2eaeb7b50c3b9fd77bb404d4287fd8806ec048403f3)
state: PLAN_PENDING_REVISED
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos, continuing QA authority for HDE-EPIC040 (the same Kronos who authored v1.0)
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-80 / QA_PLAN v1.0 revised to v1.1
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-80 — Revise Whole-Change QA Plan — 091426.1 (Notion 3db4590a05eb813ba9a9dbd9a641d36c; page as of 2026-09-24T15:55:48.777Z; read in full at QA-80)
ecosystem_release: GCFPE-20260914.1 (091426.1)
redline_source: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.1.md (QA_PLAN_REVIEW v1.1, DENY; findings FND-001 to FND-009; redlines RL-01 to RL-13; SHA-256 cc61419956c1232c0b7340915c39e03c6940acb25deb00272579faaa20f9ad79)
redline_application_report: docs/ephemeral/HDE-EPIC040-QA80-redline-application-report-v1.0.md
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE; locus provenance)
live_qa_guide: docs/ephemeral/HDE-EPIC040-QA20-live-qa-guide-v1.0.md (GUIDE_READY; its §4.3 and §5 are superseded by canon per the QA-70 review v1.1)
qa_readiness: docs/ephemeral/HDE-EPIC040-QA10-qa-readiness-v1.0.md (READY_FOR_QA)
po_disposition: docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md (Q-1 yes, Q-2 yes)
planning_failure_rca: docs/ephemeral/HDE-EPIC040-QA70-planning-failure-rca-v1.1.md
pf10: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md (SHA-256 c53b8d102d255bf55e58d621a87efee3878515e23a6dbab2652d9cf5142c5919; read as stated under Canon relied on)
planning_basis_revision: a6002d27cd955c814e90661ae2309dc74b190733 (locus basis of the QA Audit; planning basis only; not a PASS predicate)
revision_observed_at_qa80: bf6e8dab4a12cba6cbbe252f38fc2ba0580e5f80 (origin/main; changes since the planning basis outside `docs/ephemeral/` and `docs/pfcanon/` are listed in the redline application report §7)
review_route: QA-70 — Review Whole-Change QA Plan — 091426.1, the same continuing Isis (execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-80 (QA-80 is not an addendum producer)
---

# HDE-EPIC040 — Whole-Change Live QA Plan v1.1 (QA-80 revision)

Epic ID: HDE-EPIC040
Plan type: Live QA Plan / Runbook
Execution venue: Codespaces (preferred): GitHub Codespaces for `amthorn78/glow-hdengine-v2` (PF07-Canon-Glow-Infrastructure §2.6–§2.8), used as a QA console and artifact sink, never as production (Glow QA Guide §14.4.2). Other: a Product Owner-controlled Linux shell that satisfies every `d0-discovery` prerequisite. Every check runs in one QA console checkout (§7.1).
Approval sentinel: `ASK OK?`
Venue-specific claim: NOT CLAIMED. No check asserts a Codespaces capability, and no acceptance criterion depends on the venue.
Why venue can affect the result: in one check only. In `ac040-08-evidence-validators`, pytest group G includes `tests/evidence/test_evidence_index_missing_state.py`, which deletes evidence-index files, regenerates them through `tools/evidence/update_evidence_index.py` and asserts that each regenerated file keeps the file mode it had in the checkout. The updater creates a missing file with mode 644, while the checkout's modes depend on the umask the venue applied when the repository was checked out (QA-80 inspection at `bf6e8da`). The QA-100 attempt in `06b04a9` observed a checkout mode of 438 (666) and a regenerated mode of 420 (644) for `docs/evidence/INDEX.sha256`, and that assertion failed (QA-70 review v1.1 FND-008). The filesystem cannot affect any other check: their predicates are exit codes, byte identity, digests of file contents and captured output. A QA-80 search of the Audit's test files for file-mode assertions found three other files that read or set modes; each compares a file with itself before and after an operation, or asserts a mode its own code sets.
Required venue evidence: in `ac040-08-evidence-validators`, before its first command, the output of `umask` and of `stat -c '%a %n' docs/evidence/INDEX.sha256`, recorded in the body.
Effect of missing venue evidence: a group G failure confined to that test's file-mode assertion is not attributable to product behavior when the recorded checkout mode is not 644, or when the venue evidence is missing. That check is then `TOOLING_BLOCKED` (a required environment fact is unavailable), never `FAIL_BEHAVIOR`, and AC040-08 relies for that test on the exact-head CI evidence of §10.2. With a recorded checkout mode of 644 the same failure is `FAIL_BEHAVIOR`.
Target environment: other: a local QA console (§7.1) running the tested source tree under the closed posture (§5.2), with a loopback HTTP server built from that tree for `sec-reader-http-live`; and, for `open-rails-showcompat-vendor` only, the CLI-local vendor posture (§5.2), which reaches HumanDesignAPI through `HD_API_BASE_URL` (PF07-Canon-Glow-Infrastructure §2.7). No deployed service and no database is a target. The console is not production (Glow QA Guide §3.5.5, §14.4.2).
Plan revision: r2 (artifact v1.1)
Date (UTC): 2026-09-27
Operators (names-only): PO (Nathan): `open-rails-showcompat-vendor` only (class 3); QA/infra executor: one authorized execution operator/session delegated by the PO, for every class 1 and class 2 check (§7.1); Kronos: QA author and evidence reviewer, who also evaluates the [K] predicates at QA-110 (§12)

"Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates."

No formally approved Product Owner rescope applies to QA. The PO dispositions Q-1 and Q-2 set required QA steps; they are not rescopes.

This Plan executes nothing. Every artifact it lists is NOT RUN until the producing check executes under an approved QA-90 task.

Revision record: v1.1 applies each redline RL-01 to RL-13 of the QA-70 review v1.1 once. `docs/ephemeral/HDE-EPIC040-QA80-redline-application-report-v1.0.md` maps every redline, finding and carried decision to its resulting anchor here, and lists every change outside the redline bundle with its cause. Content that no redline, consequence, currency correction or QA-80 contract item affects is unchanged from v1.0.

## Canon relied on

Read from `docs/pfcanon/` on `main` at `bf6e8da` for this revision. Each section named here was read in full.

- **HDE Build Notes** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`): its predecessor v13.3.9 (SHA-256 54e660e364c29b9f0d91b6de28ca15efee4ae346f8ecd032833f2e47d8cebf0d) was read in full at QA-50 in this Kronos session. A line diff at QA-80 shows that v13.4.2 changes only the version line and the addendum index and adds addenda 2.29, 2.30 and 2.31, which were read in full at QA-80. Relied on here: the addenda listed in §1 and §2.2, whose text is unchanged since v13.3.9; the CI records of 2.6 §5.2, 2.11, 2.13, 2.19, 2.20, 2.22, 2.24 and 2.26 (§10.2); and 2.29 "PF10-CANON-001 — Repository PF-Canon Authority, Change-Process Document Storage and Canon Consultation" (canon location; DD-03, DD-05). Addenda 2.30 and 2.31 set no rule for this Plan: 2.30 governs citations inside PF documents, and 2.31 governs prompt headers.
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`): §2.2.6; §2.3; §3.1.1, §3.1.2, §3.2, §3.3; §3.4.1 to §3.4.14; §3.5.1 to §3.5.7; §4.4.1 to §4.4.7; §11.1 to §11.3; §14.1 to §14.6.
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Unknowns, discovery, deferral, and open rails"; "Database-role evidence boundary"; "Template-safe placeholders and omission syntax"; "Canon precedence for template use"; §A.1 Live QA Plan in full, from its front matter to "Close-out deliverables", including "Rails posture (explicit)", "Step-log header schema expectations (required; v2)" with the `PARKED` definition and "Executable helper boundary", Step-0B, Step-0C, "Runbook Check Matrix", "Check Blocks" and "Vendor-dependent steps (rails-scoped)"; "Review guardrails" in full; §2 "QA Rails — Open/Close (Final PR)".
- **Glow Infrastructure** (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md`): §0 (production rails and CI-lane boundary; PF07-derived and PF07-gap postures); §2.1; §2.2; §2.4; §2.6; §2.7; §2.8; §10.1 to §10.6.
- **HDE CLI/API Vendor Ref** (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`): §7.3.9; §7.4.
- **HDE Build Checklist — Separation** (`docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md`): Task HDE-SEPA005 and subtasks HDE-SEPA005.1 to HDE-SEPA005.5.

| Topic | Governing section |
| --- | --- |
| Rail postures | Glow QA Guide §2.2.6, §2.3, §14.5.1; Glow Infrastructure §0 (production rails), §2.4, §2.7; QA-70 review v1.1 §2 |
| Production and the QA console | Glow QA Guide §3.5.5, §11.3, §14.2, §14.4.2; Glow Infrastructure §2.2, §2.6 |
| No-user environment, deferral and local/offline labels | Glow QA Guide §3.3 |
| Check classes and the PO Live QA subset | Glow QA Guide §3.5.5, §3.5.6 |
| Executors and delegation | Glow QA Guide §3.3 (final bullets), §11.1 |
| Decisive evaluation and helpers | Glow QA Guide §3.4.8, §3.4.10; C040-09 as approved as changed (§2.3) |
| Step-log header, `PARKED` and header correction | Plan Templates "Step-log header schema expectations (required; v2)"; Glow QA Guide §4.4.3 to §4.4.5 |
| Venue | Glow QA Guide §14.1; Plan Templates Live QA Plan front matter |
| Exact-head CI and PR evidence | Glow QA Guide §3.4.14; HDE Build Notes lineage addenda (§10.2) |
| Vendor step | HDE CLI/API Vendor Ref §7.3.9; Glow QA Guide §3.3, §3.5.7; Glow Infrastructure §2.7; Plan Templates "Vendor-dependent steps (rails-scoped)" |
| PF09 accountability | Plan Templates "Hard blockers" (PF09 task accountability) and "PF09 phased-routing boundary"; HDE Build Checklist — Separation, HDE-SEPA005 |
| Omission syntax and fences | Plan Templates "Template-safe placeholders and omission syntax"; Glow QA Guide §3.4.10 |
| Canon location and change documents | HDE Build Notes addendum 2.29 |

In-flight change documents (`docs/ephemeral/`): the QA-70 review v1.1 and this Plan's v1.0, each in full at QA-80; the PO disposition v1.0 and the planning-failure RCA v1.1, in full at QA-80; the QA Audit v1.0 (authored at QA-50; §4 loci and §10 to §12 re-read at QA-80); the QA readiness v1.0 and the Live QA Guide v1.0 (read in full at QA-50 in this session; the QA-70 review v1.1 sets Guide §4.3 and §5 aside in favor of canon); the Implementation Plan v2.1 §8 acceptance-to-work-unit table; the PR07 work-unit lineage review v1.0 §1 to §4; the QA-70 review v1.0 §4 and §5 (C040-09 history only); the Alpha state record v1.0. Repository observations at `bf6e8da`, read-only: `tools/qa/qa_harness.py`; the `APP_ENV` reads in `adapter/http_reader.py`, `adapter/factory.py`, `engine/db/adapter.py` and `engine/http/compat_handler.py`; `tests/http/test_reader_post_v1.py` and `tests/http/test_dev_conjunction_http.py`; `tests/evidence/test_evidence_index_missing_state.py` and the file-mode handling of `tools/evidence/update_evidence_index.py`; and commit `06b04a9` on branch `qa/hde-epic040-qa100-checks-1-10`.

## 1. Canon set

Titles only; exact locators are in the QA Audit §2.

- PF10 — HDE Build Notes (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`). Relevant addenda (numbering as in v13.4.2, which keeps the v13.3.9 numbers 2.2 to 2.28; with headings): 2.2 "Canonize HDE-EPIC040 source-conflict ADR decisions"; 2.3 "Reconcile superseded core-test instructions"; 2.4 "Record in-flight resolution of C040-01 through C040-04"; 2.5 "Record the approved source-backed Channel taxonomy and existing-state conformance"; 2.12 "HDE-EPIC040-PR03-R02 — Bind Executing Mechanics to the Admitted Release"; 2.15 "HDE-EPIC040-PR04-F01 — Truthful Non-Admitted Gate Outcome for the PR04-to-PR06 Interval"; 2.16–2.18 (PR04-F03, F05, F07 Product Owner deferral decisions); 2.19 "HDE-EPIC040-PR04-LINEAGE-001"; 2.20 "HDE-EPIC040-PR05 — PR Work-Unit Lineage Review v1.0"; 2.21 "HDE-EPIC040-PR06-F01 — Frozen-capture identity source for the canonical JSON gate"; 2.22 "HDE-EPIC040-PR06 — PR Work-Unit Lineage Review v1.0"; 2.23 "HDE-EPIC040-PR07-F01 — Add PR06a for Reader v2 Full Magic-10 Exposure and the Deferred Reader Contract Work"; 2.24 "HDE-EPIC040-PR06a — PR Work-Unit Lineage Review v1.0"; 2.25 "HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08)"; 2.26 "HDE-EPIC040-PR06b — PR Work-Unit Lineage Review v1.0"; 2.27 "HDE-EPIC040-OPS01 — OPS_EXECUTION_RESULT v1.4"; 2.28 "HDE-EPIC040 — Change Audit Triage v1.0 (QA-10)"; 2.29 "PF10-CANON-001 — Repository PF-Canon Authority, Change-Process Document Storage and Canon Consultation".
- PF04 — HDE Governance, §2.0 (acceptance-token roster; this Plan is tokenless).
- PF06 — Change Process Guide, §0.4.1 (D0 Discovery artifact; QA RCA and Doc Delta summary).
- HDE Build Checklist phase document: `PF09.3-Canon-HDE-Build-Checklist-Separation`, Task HDE-SEPA005 "Production Magic10 mechanics configuration contract" and subtasks HDE-SEPA005.1 to HDE-SEPA005.5.
- PF12 — HDE Schemas & Artifacts, §8.3 and §8.6 (Machine Mirror and Evidence Index; follow-up publication only).
- PF19 — Glow QA Guide, §§2.2.6, 2.3, 3.1.2, 3.3, 3.4.3, 3.4.8, 3.4.9, 3.4.10, 3.4.14, 3.5.5, 3.5.6, 3.5.7, 3.5.10, 3.6, 4.4.3–4.4.6, 10.6, 10.7, 10.8, 11.1, 11.3, 14.1, 14.4.2, 14.5.1 (§3.4.3's plan-location row, §3.6 and §10.8 as superseded in part by PF10 Addendum 2.29).
- PF27 — Canon Plan Templates, §A.1 Live QA Plan and Review guardrails.
- PF05 — HDE CLI/API Vendor Ref, §7.1.11, §7.3.9, §7.4.
- PF07 — Glow Infrastructure, §§0 (production rails and CI-lane boundary), 2.2, 2.4, 2.6–2.8, 7.0, 7.2.1, 8.1, 10.1–10.3.
- PF01 — HDE Math Spec, §9.5 (goldens, as transcribed in the fixture).

PF20 is not used. PF23 is not used as a requirement.

## 2. Scope statement

This plan evaluates the following in-scope surfaces and checks:

- D0 Discovery and tooling bootstrap: `d0-discovery`
- D1 Step-0B doc-delta capture: `step-0b-doc-delta-capture`
- D2 AC040-08 owner-generated evidence coherence and evidence tests: `ac040-08-evidence-validators`
- D3 AC040-02, AC040-03 catalog, configuration and schemas: `ac040-02-03-catalog-config`
- D4 AC040-04, AC040-05 admission, pure core and release identity: `ac040-04-05-admission-identity`
- D5 AC040-06 read-only golden comparison: `ac040-06-golden-comparison`
- D6 AC040-07 Gate ingress and readiness, offline: `ac040-07-gate-ingress-offline`
- D7 AC040-04, AC040-09 compat and CLI, offline: `ac040-04-09-compat-cli-offline`
- D8 AC040-09 Reader, HTTP and transport, in-process: `ac040-09-reader-http-in-process`
- D9 Q-1 security of the Reader route over loopback HTTP, under the closed posture with `APP_ENV=dev` (a local process, not production): `sec-reader-http-live`
- D10 Q-2 PF05 §7.3.9 bounded open-rails vendor step: `open-rails-showcompat-vendor`
- D11 AC040-07 live, read-only Gate readiness against current rows: `live-db-gate-readiness`. Blocked by environment and deferred under Glow QA Guide §3.3: no app-level user IDs or user-bound BodyGraph rows exist that QA may rely on before the App. Recorded `PARKED` before execution. Reactivation condition: a future epic defines user-bound QA surfaces once the App user model exists.
- D12 removed by QA-80 (RL-08). `live-db-reader-refusal` is not in the collection; no D12 check exists.
- D13 AC040-09 live DB Reader success path: `live-db-reader-success`. Blocked by environment and deferred under Glow QA Guide §3.3, as D11. Recorded `PARKED` before execution, with the same reactivation condition.
- D14 Close-out deliverables and coverage accounting: `qa-closeout-deliverables`

AC040-01 (scope and ownership) is a documentary criterion. It is assessed in the QA-120 Report from the lineage records and the `qa-closeout-deliverables` coverage accounting; no separate executable check protects it.

This plan explicitly excludes:

- Any deployed service, including `https://glow-hdengine-v2-production.up.railway.app`. No deployment, activation or production-runtime claim is made.
- Rebuilding the release attestation (`tools/evidence/build_release_attestation.py`). OPS01's accepted evidence is consumed as corroboration only.
- `hdctl bg:resolve` in any mode, `hdctl showcompat --source db`, `--source auto`, `--user-a`, `--user-b`, `--dump-admin-dir` and `--conjunction` live runs, `hdctl aux-preview` and `hdctl dev:sampler`. PF19 §3.3 blocks DB-user compat in the no-user environment; no HDE-EPIC040 criterion needs the others live.
- Live probing of `adapter.wsgi` and `adapter.http_reader` factories; their route parity is covered in-process by `tests/http/test_reader_post_v2.py`.
- Tests outside the 70-file HDE-EPIC040 surface, including `tests/reader_v1/test_cli_proof.py` (baseline failure O-P06a-03) and the 57 failures and 13 errors recorded among other uncovered files. They are not results of this change.
- Any DB write, backfill, migration or upsert; any AI-provider call; any PF-Canon or PF10 edit; Index or Mirror publication; close-pack generation; OPS re-execution; merges.

### 2.1 Live QA Guide coverage

Every obligation and risk in `docs/ephemeral/HDE-EPIC040-QA20-live-qa-guide-v1.0.md` maps to a check or a stated treatment.

| Guide item | Treatment in this Plan |
| --- | --- |
| §3 AC040-01 to AC040-09 | Checks per §2 scope list; AC040-01 in the QA-120 Report |
| §4.1 open-rails step (Q-2) | `open-rails-showcompat-vendor` |
| §4.2 security step (Q-1) | `sec-reader-http-live` (loopback HTTP, closed posture), `ac040-09-reader-http-in-process` (admission refusal, CONNECT, QUERY, and the production gating of the dev routes) |
| §4.3 live Gate readiness with non-mutation proof | Superseded by canon (QA-70 review v1.1 §3): blocked by environment and deferred under Glow QA Guide §3.3; `live-db-gate-readiness` is `PARKED` |
| §5 Python 3.12, fresh venv, editable install, closed rails, `DATABASE_URL` only, keys never printed, `adapter.factory:create_app()` | `d0-discovery`; §5.2 postures (Guide §5's rails statement is superseded by canon, QA-70 review v1.1 §3); no check uses `DATABASE_URL`; `sec-reader-http-live` uses the factory |
| §6 exact admission | `d0-discovery` admission probe with the manifest audit; tested source recorded |
| §6 wheel installs refuse (O-12) | Editable install from the source tree |
| §6 HTML 404 on the factory (O-P06a-22) | Probe S-26, observed as a known limitation |
| §6 `APP_ENV` asymmetry (O-P07-04) | Dev-route production gating is covered in-process by group F in `ac040-09-reader-http-in-process`; no HTTP probe (RL-06 option (b)); DD-09 |
| §6 `--band` ignored with `--pair-file` (O-P07-02) | Not used by any check |
| §6 `bg:resolve` bypasses the LF guard | `bg:resolve` excluded |
| §7 evidence root, per-step record, status vocabulary, redaction, Index/Mirror only through the updater | §8; Index/Mirror publication is the QA50-F01 follow-up |
| §8 baseline failures and out-of-lane files | `tests/reader_v1/test_cli_proof.py` and non-EPIC040 failures excluded; all 70 EPIC040 test files run in groups A to G |
| §9 permitted and forbidden actions | §2 exclusions; §7 executors and evidence storage |
| §10 recovery | §7.3 to §7.5 |

### 2.2 PF10 overrides and conflicts

- PF10 Addendum 2.23 (C040-07) → Reader v2 is an approved public surface on `POST /api/reader?v=2`, superseding the PF05 statement that the production Reader refuses `v=2` → PF05, PF01, PF04, PF12 (drainage pending).
- PF10 Addendum 2.25 and 2.26 (C040-08) → Reader v1 errors use the four-key `error_v1` envelope → PF01 §2.3, PF04 §8.1.2 (drainage pending).
- PF10 Addendum 2.20 → readiness was proven offline only; the live observation (D11) is blocked by environment and deferred under Glow QA Guide §3.3, so `live-db-gate-readiness` is `PARKED` → PF09.3 HDE-SEPA005.5.
- PF10 Addendum 2.22 → a non-editable wheel refuses admission (O-12); installs are editable from the source tree → packaging.
- PF10 Addendum 2.24 → HTML 404 on unknown non-compat paths is a known limitation (O-P06a-22), observed, not failed; `tests/reader_v1/test_cli_proof.py` is a baseline failure outside scope → PF05 transport.
- PF10 Addenda 2.16–2.18 → the F03, F05 and F07 deferrals were later delivered or bounded by PR06a; dev conjunction evidence capture is not required here.
- PF10 Addendum 2.15 → the non-admitted interval is historical; release 1.3.0 is admitted, so `RELEASE_NOT_ADMITTED` is not an expected outcome at the tested source.
- PF10 Addenda 2.12 and 2.21 → admission and the canonical JSON gate bind to the admitted release and frozen-capture identity; D2 and D4 predicates follow them.
- PF10 Addendum 2.19 and 2.28 → security review did not cover four units (Q-1 → D9); RA-10 requires the open-rails step (Q-2 → D10).
- PF10 Addendum 2.27 → OPS01 is accepted; QA does not re-run it.
- Addenda 2.2–2.5 → C040-01 to C040-06 decisions govern source versions and the Channel taxonomy used by D3.
- PF10 Addendum 2.29 (PF10-CANON-001) → PF-Canon is resolved from `docs/pfcanon/` on `main`, and change-process documents are stored in `docs/ephemeral/`; it supersedes the Google Drive and ChatGPT Library passages of PF19 §3.4.3 (plan-location row), §3.6 and §10.8 → DD-03, DD-05 (PF19 drainage pending).

The single `CANON_CONFLICT_REGISTER` is carried in §2.3: C040-01 to C040-08 unchanged from the QA Audit §11, and C040-09 `APPROVED_AS_CHANGED` by the QA-70 review v1.1. Treatment of C040-09 in this runbook: read-only git observations for attribution only, never as a PASS gate; no script file is created; tracked, tested entrypoints (`tools.qa.qa_harness`, `_refresh_path_proof`) are invoked through `python -c` (PF27 "Embedded harness checks"); no decisive evaluator is written at run time (§12).

### 2.3 CANON_CONFLICT_REGISTER

One register, carried from the QA Audit v1.0 §11 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`). C040-01 to C040-08 are unchanged, with their full original proposals and decision histories retrievable at the exact references in each row. C040-09 carries its decision from the QA-70 review v1.1. PF10 references in the rows use the v13.3.9 numbering, which v13.4.2 keeps for 2.2 to 2.28. A proposal here is not approval.

| ID | Classification | Sources and clauses | Decision and status | Reviewer, artifact, time | Interim treatment | Drainage target and owner | Full history |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C040-01 | CANON_RECONCILIATION | Pinned source/scope predicate | APPROVED exactly as proposed | Thoth-17, Specification v1.0 (represented by approved v1.1), 2026-09-08T13:23:24Z | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 v13.3.9 §2.2, §2.4 |
| C040-02 | CANON_RECONCILIATION | PF12 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-03 | CANON_RECONCILIATION | PF14 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-04 | CANON_RECONCILIATION | PF19 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-05 | CANON_RECONCILIATION | PF14 §6.7 superseded precomputed-score test instructions | APPROVED, alternative A | Isis-49, Plan v1.0 review, 2026-09-09T03:57:16Z | PF10 §2.3 governs | PF14 §6.7; PF14 maintainer; pending, non-gating | Plan v2.1 §11.2; PF10 §2.3 |
| C040-06 | NEW_CANON | 36-row Channel taxonomy and 16-case existing-state conformance | APPROVED, alternative A | Isis-50, Implementation Plan Review v2.0, 2026-09-09T11:48:08Z | PF10 §2.5 governs | PF12 §2.1, PF01 §§6.1–6.2; their maintainers; pending | Plan v2.1 §11.3; `docs/ephemeral/HDE-EPIC040-C040-06-HD-mechanics-ADR-v1.0.md`; PF10 §2.5 |
| C040-07 | NEW_CANON | Full Magic-10 exposure via Reader v2 versus Specification line 265 and PF01, PF04, PF05, PF12 statements | PO decision 2026-09-26; delivered by PR06a | Product Owner; PF10 §2.23 | PF10 §2.23 governs; QA tests `?v=2` | PF01, PF04, PF05, PF12, with PF14 and PF29 consequences; their maintainers; pending | PF10 §2.23, §2.24 |
| C040-08 | CANON_RECONCILIATION | Reader v1 error envelope versus schema | Alternative A; delivered by PR06b | PF10 §2.25 decision record | PF10 §2.25 governs; QA asserts the four-key envelope | PF01 §2.3, PF04 §8.1.2; their maintainers; pending | PF10 §2.25, §2.26 |
| C040-09 | CANON_CONFLICT (QA process) | PF07-Canon-Glow-Infrastructure §2.8 ("Live QA runbooks MUST NOT include git operations"; "QA plans MUST NOT create new scripts at run time") versus PF19-Canon-Glow-QA-Guide §3.4.9 (read-only repository observations may establish source) and §3.6, and PF27-Canon-Plan-Templates ("Embedded harness checks"; QA-only harness scaffolding permitted) | `APPROVED_AS_CHANGED`. Proposed: alternative (a), PF19 and PF27 govern the execution rail and plan shape; alternative (b), forbid all git reads and embedded helpers, which loses the tested-source attribution PF19 §10.8 requires, was not adopted. Change: the approval covers invoking tracked, tested entrypoints (`tools.qa.qa_harness`, `_refresh_path_proof`) through `python -c`; it does not cover newly written decisive evaluators, which Glow QA Guide §3.4.8 governs. Rationale: Glow Infrastructure §2.1 is names-only ("No procedures or policy here") and §2.8 routes the Live QA execution rail to the Glow QA Guide, so Glow QA Guide §3.4.9 (read-only repository observation for attribution, never a PASS predicate) and Plan Templates govern | Isis, continuing QA Plan reviewer (execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq); reviewed QA Plan v1.0 and QA Audit v1.0; decision in `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.1.md` §3, "Decisions carried to this review"; 2026-09-27 | Applied in this Plan: read-only git observations for attribution only, never a PASS gate; no script file is created; tracked harness APIs through `python -c`; no decisive evaluator written at run time (§12). Unresolved risk: a reader who applies PF07 §2.8 literally until its wording is drained | PF07 §2.8 wording; PF07 maintainer; documentation drainage only | Original proposal: QA Audit v1.0 §11 (`PROPOSED`, 2026-09-27). QA-70 review v1.0 §4: APPROVED as proposed; that review was rejected by the Product Owner on 2026-09-27 and is history only (RCA v1.1, C2). QA-70 review v1.1 §3: `APPROVED_AS_CHANGED` (current) |

Affected requirements for C040-09: AC040-08 and AC040-09 evidence attribution (K040-REQ-012, K040-REQ-013).

## 3. Open-Rails Live QA Requirement

HDE-EPIC040 is production-affecting: it changes public Reader behavior, runtime compute, CLI behavior and the vendor-backed resolution path. One bounded open-rails step is included (`open-rails-showcompat-vendor`, PO Q-2; PF05 §7.3.9). No exemption applies.

| Field | Value |
| --- | --- |
| Behavior proved | `hdctl showcompat --source vendor` with birth-only inputs acquires both charts from HumanDesignAPI, maps them, evaluates the pair through the admitted release and emits canonical `magic10_compat_result.v1` bytes and a Reader v1 dump, identically for AB and BA |
| Live target | CLI-local vendor smoke target (PF07 §2.7): command `hdctl showcompat`, `--source vendor`, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `APP_ENV=dev` |
| Rails | `SAFE_MODE=0`, `ALLOW_NETWORK=1` for this step only, pins `LC_ALL=C LANG=C TZ=UTC`; default closed rails restored immediately after |
| Secret safety | PO-only execution; secrets never printed, logged or persisted; presence recorded as SET/UNSET; a zero-occurrence scan of secret values over all evidence files before storage |
| Evidence | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/` files listed in the check block |
| Proves | Live vendor-backed CLI resolution through the HDE-EPIC040 core and emitter, canonical stdout, AB↔BA identity, Reader v1 bands-only dump, binding to the admitted release |
| Does not prove | Exact vendor resource path and auth-header family unless the captured output shows them; rate-limit, `Retry-After`, typed vendor error, malformed-response and v1-legacy-guard handling; mapped-cache persistence; Reader v2 over HTTP; deployed-service behavior; broad HumanDesignAPI v2 conformance |

## 4. Reality Audits historical context

The QA-10 Reality Audit (`docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md`) is consulted as provenance only. Current loci come from this Plan's QA Audit. No Reality Audit update is assigned.

## 5. Environment and rails posture

### 5.1 Determinism pins

`LC_ALL=C`, `LANG=C`, `TZ=UTC` for every check. No other pin is required.

### 5.2 Rail postures

This Plan uses only the postures that canon allows for HDE-EPIC040 Live QA (QA-70 review v1.1 §2; Glow QA Guide §2.2.6, §2.3, §3.3, §14.5.1; Glow Infrastructure §0, §2.4, §2.7). Rails change only between checks, never inside one. No posture pairs a production `APP_ENV` with a local or Codespaces process.

Default rails for this runbook: the closed posture, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`.

Presence of secret-bearing and drift keys is recorded as SET or UNSET only, before any change, in the body of the check's primary log. Values are never printed.

| Posture | Values | Used by | Must be SET | Must be UNSET |
| --- | --- | --- | --- | --- |
| Closed (default) | `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; pins `LC_ALL=C LANG=C TZ=UTC` | Every executed check except `open-rails-showcompat-vendor`, including the local server and the client of `sec-reader-http-live`; also the recording of the two `PARKED` checks | none; `PORT=8000` for the `sec-reader-http-live` server only | `DATABASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV` |
| CLI-local vendor | `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev`; the same pins | `open-rails-showcompat-vendor` only, for the whole check; the closed posture is restored when that check ends, before any other check | `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` | `HDAPI_BASE_URL`, `DATABASE_URL`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV` |
| Production | `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod` | Not used. It belongs only to the deployed Railway service `glow-hdengine-v2` (Glow Infrastructure §0, §2.4 Production, §2.6), never to a local or Codespaces process (Glow QA Guide §3.5.5, §14.4.2). No check targets the deployed service | not applicable | not applicable |

Rails change by check (PF27 "Rails posture (explicit)"): `open-rails-showcompat-vendor` → CLI-local vendor posture for the whole check → the step needs HumanDesignAPI I/O through the CLI (PF05 §7.3.9; Glow QA Guide §3.3; PF07 §2.7) → the five vendor files and the check's primary log. No other check changes rails.

Reasons: closed rails do not gate database access (QA Audit QA50-F03), so the closed posture unsets `DATABASE_URL`; local writer routes can insert rows when a DB is reachable (QA50-F09); `HD_API_BASE_URL` is canonical and `HDAPI_BASE_URL` is a deprecated alias (PF07 §2.4, PF19 §3.5.7; QA50-F10); retired bridge keys are drift and are only reported by name (PF07 §7.0). No check reads a database: the live-DB checks are `PARKED` or removed (§2), because Glow QA Guide §3.3 bars relying on user-bound rows before the App.

Pytest runs mirror the CI lane posture (`.github/workflows/ci.yml` L106): the closed posture plus `PYTHONDONTWRITEBYTECODE=1` and `python -m pytest -q -p no:cacheprovider -rs`.

The local server of `sec-reader-http-live` uses the PF07 §10.1 declaration with `PORT=8000`: `python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:8000 --workers 2 --threads 4 --timeout 30`. The client uses `http://127.0.0.1:8000` (PF07 §2.2).

### 5.3 VCS and source identity

No check performs a VCS mutation. `d0-discovery` records the tested source read-only (`git rev-parse HEAD`, `git status --porcelain` line count) for attribution only (PF19 §3.4.9). Neither value, a branch name nor working-tree noise is a PASS or FAIL predicate. The tested source is expected to be the planning basis or a later commit; Kronos assesses any substantive difference under PF19 §10.8. Evidence storage is a separate lane (§7).

## 6. PO inputs needed

Names only; no value is stored in this Plan.

| Input | Needed by | Source | If missing at runtime |
| --- | --- | --- | --- |
| `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` | D10 | PF07 §2.4, §2.7 | D10 `TOOLING_BLOCKED` |
| Birth tuples A and B (synthetic, not a real person's data) | D10 | Default: A = (`1999-10-16`, `04:37`, `Santiago, Chile`), B = (`1978-06-17`, `02:35`, `Tallinn, Estonia`) from `audit/ops/hde-epic030/ops-02/vendor_command.txt` (Audit-proven L-51), unless the PO names other synthetic tuples in the QA-90 task | D10 `TOOLING_BLOCKED` |
| `PORT=8000` | D9 | PF07 §2.4 | Server not started; D9 `TOOLING_BLOCKED` |
| Delegation record naming the QA/infra executor (§7.1) | D0 to D9, D14, and the `PARKED` records of D11 and D13 | QA-90 task | The class 1 and class 2 checks are not run, and the PO does not run them in their place (Glow QA Guide §3.5.5); D10 is then `TOOLING_BLOCKED` by its dependencies |
| Evidence branch name | Evidence storage (§7) | QA-90 task | Evidence stays uncommitted until named |

No database input is requested: no check reads a database (§5.2), and no selection of user rows exists to supply (Glow QA Guide §3.3).

## 7. Executors, authority, evidence storage, rerun and recovery

### 7.1 Executors by check class

Glow QA Guide §3.5.5 and §3.5.6 assign each class of check to its executor. All checks run in one QA console checkout, so that one QA root and one manifest hold the complete current-state evidence.

- PO Live QA subset: `open-rails-showcompat-vendor` (class 3, vendor-focused) only. Nathan (Product Owner) executes it, PO-only and Kronos-guided (Glow QA Guide §3.3, §3.5.7). The Plan assigns no class 1 pre-flight to the PO; that check's own step-local readiness and recording preflight (§12) are part of the check.
- QA/infra executor (the named delegated executor): every class 1 and class 2 check (`d0-discovery`, `step-0b-doc-delta-capture`, checks 3 to 10 and `qa-closeout-deliverables`) and the `PARKED` records of `live-db-gate-readiness` and `live-db-reader-success` are executed by one authorized execution operator/session (Glow QA Guide §11.1), acting in the repository's QA/Verifier role (`AGENTS.md`), in that same checkout and outside the PO's Live QA time. The Product Owner delegates it, and the QA-90 task records its execution identity (Glow QA Guide §3.3: other bounded QA tasks may be assigned to an authorized repository-capable execution agent). It is neither the PO nor Kronos. Capability alone grants no authority. These checks are "Pre-flight / internal" and "Handled by QA/infra outside PO's Live QA time" (Glow QA Guide §3.5.6).
- If no QA/infra executor is recorded, the class 1 and class 2 checks are not run, and the PO does not run them in their place: class 2 "must not be scheduled as PO Live QA tasks" (Glow QA Guide §3.5.5).
- No automated agent executes a vendor call, handles a plaintext secret or connects to the shared database.
- Kronos designs the tasks through QA-90, reviews evidence at QA-110, where it also evaluates every [K] predicate (§12), and reports at QA-120. Kronos does not execute checks. Isis reviews this Plan at QA-70 and owns closure.

### 7.2 Evidence-only commit permission (bounded)

Evidence storage is not a QA check and is not part of any PASS predicate (PF19 §3.4.9, §10.8). After a QA-100 execution, the executor may commit and push only:

- the files this Plan names under `audit/qa/hde-epic040/` (primary logs, supplementary check files, the manifest, the path proofs, conditional rerun and Moon Loop files); and
- `audit/docdeltas/hde-epic040_doc_deltas.md` and its path proof,

on the evidence branch named in the QA-90 task, and open or update one evidence pull request. The commit message records the tested source commit from `d0-discovery`. Nothing else may be committed: no product, test, tool, schema, catalog, manifest, CI, Index, Mirror or PF file, and no file containing a secret value, a user UUID or a BodyGraph payload. No force-push, rebase or merge; Nathan merges. Any code or behavior fix goes through the normal PR route. Tracked files changed by test runs are recorded by `qa-closeout-deliverables` and are never committed.

### 7.3 Bounded ordinary-lane rerun

- Attempt 1 is the QA-90 task's first execution of a check.
- One rerun (attempt 2) of a check is available only when attempt 1 ended `FAIL_TOOLING` or `TOOLING_BLOCKED` from an execution or evidence fault (environment setup, operator error, a PO input later supplied, a transient service or network fault), the Plan is unchanged and valid, and Kronos's actual QA-110 decision routes QA-90 attempt 2 (PF19 §10.6).
- The rerun keeps the same `check_id`, evidence paths, deliverable family and rails; only the corrected fault changes. Before it starts, the executor copies the attempt-1 `primary.log` byte for byte to `attempt1_primary.log` in the same check directory and writes `rerun_note.md` there stating the failure signature, what changed and why. If attempt-1 bytes are unavailable, the note says so and nothing is reconstructed.
- A `FAIL_BEHAVIOR`, a second failure of the same check, an invalid Plan, or any scope, authority, code or Ops issue goes to ESC-10 through QA-110, not to another rerun. Renaming a check does not reset attempt lineage. A check whose prerequisite check is not PASS stays `TOOLING_BLOCKED` without consuming its rerun.
- Earlier attempts: checks 1 to 10 were executed under Plan v1.0 in commit `06b04a9` on branch `qa/hde-epic040-qa100-checks-1-10`. Kronos dispositions those attempts at QA-110 (QA-70 review v1.1 §6). This Plan neither counts nor discards them, and attempt numbers under it follow that disposition.

### 7.4 Moon Loop (bounded)

A Moon Loop may correct only QA-created evidence-assembly defects inside `audit/qa/hde-epic040/` or `audit/docdeltas/hde-epic040_doc_deltas.md` (header, manifest, path proof, doc-delta assembly, or a QA-created input file such as `tmp_goldens_altered.json`) when the proof target, rails, evidence identity and predicates are unchanged. It preserves the failure signature, records the change and why under `audit/qa/hde-epic040/00_meta/delta/` (PF27 Step-0B), and reruns the affected check in the same evidence stream. It never touches product, test, tool, generator, governed evidence outside the QA root or PF files, and never resets attempts.

### 7.5 Cleanup and recovery

- Stop the local server that `sec-reader-http-live` starts, and confirm port 8000 is closed before the next check.
- When `open-rails-showcompat-vendor` ends, unset `HD_API_KEY`, `GEO_API_KEY` and `HD_API_BASE_URL` from the shell and restore the closed posture before any other check (§5.2).
- Temporary files outside the repository (venv, comparator report before copy, the recording body file and argv list of §12) stay outside the repository and are not committed.
- A secret value found in any evidence file: quarantine the file outside the repository, do not commit it, classify the check `FAIL_TOOLING`, and route through §7.3.
- No check connects to a database or changes database state, so no database rollback exists.

## 8. Evidence posture and directory structure

- QA root: `audit/qa/hde-epic040/` (Canon-defined pattern, PF07 §2.8, PF19 §3.4.3). Absent at planning; `d0-discovery` records that before creating it.
- One current-state primary log per check, named `primary.log` in that check's own directory under `audit/qa/hde-epic040/checks/`; each check block states its concrete path. No run directories, no run identifiers, no pointer files.
- Manifest: `audit/qa/hde-epic040/qa_step_logs_manifest.json` (Canon-defined), a flat object keyed by `check_id` with `check_id`, `log_path` (full repository-relative path) and `status`, maintained by `record_check`. `TOOLING_BLOCKED` and `PARKED` checks are listed too.
- Path proofs (PF19 §3.4.3): `audit/qa/hde-epic040/qa_step_logs_manifest.json.path_proof.txt`, one `primary.log.path_proof.txt` beside each primary log, and one beside each doc-delta surface, written by `qa-closeout-deliverables`.
- Recording mechanism (Audit-proven L-41, L-42): `tools.qa.qa_harness.record_check` with `HarnessConfig("HDE-EPIC040", repo_root)` (the checkout root as a `pathlib.Path`) and one `CheckResult` carrying the fields listed in the QA Audit L-41. Pytest groups run directly (§12); `run_pytest_check` is not used, because its argument grammar does not admit `-rs`. Multi-command checks build one `CheckResult` whose `command` lists every executed argv in order.
- Step-log header: `pf27.step_log_header.v2`, fourteen keys, one contract across all checks. `status` from `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `PARKED` with PF27 causal precedence. `status_reason` empty only for PASS. `command_provenance` names this Plan's check block and any in-flight syntax normalization. `exit_code` is the exit code of the check's final decisive command, which each check names; every command's own exit code is written in the body. `captured_env` holds actual values of the admitted names (`LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`). `pf_refs` holds in-document PF titles; PF10 citations go in the body because `PF10-HDE-Build-Notes` does not match the harness pattern (QA50-F07). `intended_tokens` and `claimed_tokens` are `[]` for every check.
- Body sections follow PF19 §4.4.6: `=== CONTEXT ===` (tested source, interpreter, environment presence), `=== COMMANDS ===` (each command and exit code), `=== OUTPUT ===`, `=== PREDICATES ===` (each predicate with PASS or FAIL), `=== LIMITS ===`.
- Supplementary files named in a check block are bound by SHA-256 lines in that check's primary log.
- Index and Mirror publication is a follow-up for the evidence owner (QA Audit QA50-F01; PF09.3 HDE-SEPA005.5). This Plan does not claim the manifest is ledger-bound (PF19 §4.4.3).
- Tokens: none. No acceptance map, token matrix or viability ledger exists or is created.
- Pre-existing inputs (presence may be checked before a step; Audit-proven): `catalog/manifest.json`, `catalog/channels_v1.json`, `catalog/magic10_mechanics_v1.json`, `tests/fixtures/magic10/v1/goldens.json`, `audit/ops/hde-epic040/ops01/SHA256SUMS`, `audit/ops/hde-epic040/ops01/attestation.json`, `audit/ops/hde-epic030/ops-02/vendor_command.txt`, the 70 test files of the QA Audit §4.4, and the tools and scripts of the QA Audit §4.1. QA-run artifacts (created only by their producing check, never presence-gated in advance): every file under `audit/qa/hde-epic040/` and `audit/docdeltas/hde-epic040_doc_deltas.md` with its path proof.

## 9. Mandatory Step-0 artifacts

- Step-0A: not defined by PF27; none is invented.
- Step-0B: `step-0b-doc-delta-capture` (D1).
- Step-0C: not included. This Plan makes no Codespaces-to-production behavior claim.
- Discovery artifact (PF06 §0.4.1.1): `audit/qa/hde-epic040/checks/d0-discovery/primary.log`.

### 9.1 Step-0B doc-delta rows

Step-0B writes these rows mechanically, then appends any BLOCKER that `d0-discovery` records. BLOCKERS at plan time: none.

| ID | Class | Delta | Drain target (title) | Owner |
| --- | --- | --- | --- | --- |
| DD-01 | CAVEAT | QA Codespaces inventory lists retired `DB_BRIDGE_URL` (QA50-F14) | PF07-Canon-Glow-Infrastructure §2.4 | PF07 maintainer |
| DD-02 | CAVEAT | PF07 §2.8 forbids git operations and QA-time scripts; PF19 §3.4.9 and PF27 permit read-only observations and embedded harness calls (C040-09, `APPROVED_AS_CHANGED` by the QA-70 review v1.1) | PF07-Canon-Glow-Infrastructure §2.8 | PF07 maintainer |
| DD-03 | CAVEAT | PF19 §§3.4.3, 3.6, 10.8 and AGENTS.md name ChatGPT Library or Google Drive for authored plans and canon; D7 and the QA prompts use `docs/ephemeral/` and `docs/pfcanon/` (QA50-F13). Status: PF10 Addendum 2.29 now supersedes those PF19 passages, and PF19 wording drainage is pending; AGENTS.md is resolved at `bf6e8da` | PF19-Canon-Glow-QA-Guide §§3.4.3, 3.6, 10.8 | PF19 maintainer |
| DD-04 | CAVEAT | PF05 §7.1.11 `--allow-prod-vendor` is not implemented (QA50-B01) | PF05-Canon-HDE-CLI-API-Vendor-Ref §7.1.11 | PF05 and CLI owners |
| DD-05 | CAVEAT | AGENTS.md cited "PF10 §2.8" for the bounded PF-copy rule; its v13.3.9 home is PF19 §10.8 (QA50-F12). Status: resolved by a document update; AGENTS.md at `bf6e8da` no longer carries that citation, and PF10 Addendum 2.29 governs canon sources | AGENTS.md | Repository docs owner |
| DD-06 | CAVEAT | Guide §8 names `6e4b3a1` as the attestation candidate; the attestation binds `6f53d82` (QA50-F11) | None (ephemeral record) | Isis |
| DD-07 | CAVEAT, carried | C040-05 to C040-08 drainage pending (RA-18) | Per register, QA Audit §11 | Named maintainers |
| DD-08 | CAVEAT, carried | `showcompat` help says Reader v1 (O-P07-01) | Repository CLI help | Whole-change IA |
| DD-09 | CAVEAT, carried | `APP_ENV` asymmetry between dev `GET /reader` and conjunction routes (O-P07-04, RA-06) | O-P07-04 record | Whole-change IA |
| DD-10 | CAVEAT, carried | `ci/checks/check_mirror_schema.sh` is Python; AGENTS.md invocation (RA-13) | AGENTS.md | Repository docs owner |
| DD-11 | CAVEAT, carried | `docs/ADAPTER_009.md:174` says `body_not_allowed`; code emits `invalid_json` (FND-017) | `docs/ADAPTER_009.md` | Compat docs owner |
| DD-12 | CAVEAT, carried | PF10 v13.3.9 §2.28 line references to §2.19 and §2.20 are off by two | PF10-HDE-Build-Notes §2.28 | PF10 drain owner |

Every row states `Drives decision: No`. Documentation drainage is never a blocker, a check predicate or a deliverable of this Plan.

## 10. Runbook Check Matrix

Executor codes: Q = the QA/infra executor (§7.1); P = the Product Owner only. Class = the Glow QA Guide §3.5.6 class. All tokens: none (`[]`). The primary evidence column gives each concrete primary-log path. Evaluation marks [E] and [K] are defined in §12.

| # | check_id | check_name | D-goal | Class | PO Live QA | Rails | Commands and executor | Expected result | Primary evidence | Deliverables | Tokens | PF anchors |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` | Discovery and tooling bootstrap | D0 | 1, Pre-flight / internal | No | closed | Q: identity, venv, install, readiness, help, harness, admission | PASS when every prerequisite holds | `audit/qa/hde-epic040/checks/d0-discovery/primary.log` | primary log; manifest | none | PF06 §0.4.1.1; PF19 §3.6 |
| 2 | `step-0b-doc-delta-capture` | Step-0B doc-delta capture | D1 | 1, Pre-flight / internal | No | closed | Q: write both doc-delta surfaces | PASS when both surfaces exist and are byte-identical; content [K] | `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log` | two doc-delta files | none | PF27 Step-0B |
| 3 | `ac040-08-evidence-validators` | Owner evidence coherence and evidence tests | D2 | 2, local/offline (no vendor) | No | closed | Q: venue evidence, nine read-only validators, pytest group G | PASS when all exit 0 | `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log` | primary log | none | PF12 §8.3; PF19 §2.2.11, §14.1 |
| 4 | `ac040-02-03-catalog-config` | Catalog, configuration and schemas | D3 | 2, local/offline (no vendor) | No | closed | Q: catalog digests, pytest group A; structure [K] | PASS when pytest exits 0; structure at QA-110 | `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log` | primary log | none | PF09.3 HDE-SEPA005.1, .2 |
| 5 | `ac040-04-05-admission-identity` | Admission, pure core and release identity | D4 | 2, local/offline (no vendor) | No | closed | Q: manifest audit, OPS01 ledger, pytest group B; binding [K] | PASS when all exit 0; binding at QA-110 | `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log` | primary log | none | PF09.3 HDE-SEPA005.3, .4 |
| 6 | `ac040-06-golden-comparison` | Read-only golden comparison | D5 | 2, local/offline (no vendor) | No | closed | Q: compare twice, deliberate mismatch, tree digests, pytest group C; report contents [K] | PASS when exit codes, byte identity and digests hold; report contents at QA-110 | `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log` | four supplementary files | none | PF09.3 HDE-SEPA005.4 |
| 7 | `ac040-07-gate-ingress-offline` | Gate ingress and readiness, offline | D6 | 2, local/offline (no vendor) | No | closed | Q: three readiness refusals, pytest group D | PASS when refusals and tests hold | `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log` | primary log | none | PF09.3 HDE-SEPA005.3, .5 |
| 8 | `ac040-04-09-compat-cli-offline` | Compat and CLI, local/offline | D7 | 2, local/offline (no vendor) | No | closed | Q: pytest group E; skips recorded | PASS when rc 0; skips contribute no proof | `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log` | primary log | none | PF19 §3.3 |
| 9 | `ac040-09-reader-http-in-process` | Reader, HTTP and transport, in-process | D8 | 2, local/offline (no vendor), in-process | No | closed | Q: pytest group F | PASS when rc 0 | `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log` | primary log | none | PF05 §5 via PF10 2.23, 2.25 |
| 10 | `sec-reader-http-live` | Reader route security over loopback HTTP (closed posture) | D9 | 2, local/offline (no vendor), loopback HTTP | No | closed, `APP_ENV=dev` | Q: loopback server, 22 probes; probe predicates [K] | PASS when the server is ready and 22 probes are captured; probe predicates at QA-110 | `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log` | `http_probes.jsonl`; `gunicorn_server.log` | none | PF19 §3.2, §3.5.10 |
| 11 | `open-rails-showcompat-vendor` | Bounded open-rails vendor step | D10 | 3, vendor-focused | Yes: the whole PO Live QA subset | CLI-local vendor | P: two vendor-backed runs (AB, BA), byte identity, parse check, secret scan; output shape [K] | PASS per §12 block | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log` | five vendor files | none | PF05 §7.3.9; PF19 §3.3, §3.5.7 |
| 12 | `live-db-gate-readiness` | Live read-only Gate readiness | D11 | 2 (`PARKED`) | No | none; no command runs | Q: record `PARKED` only | `PARKED` before execution (Glow QA Guide §3.3) | `audit/qa/hde-epic040/checks/live-db-gate-readiness/primary.log` | primary log | none | PF19 §3.3; PF27 `PARKED` |
| 13 | removed | `live-db-reader-refusal` removed by QA-80 (RL-08) | D12 | none | No | none | none | Not in the collection; no evidence is expected | none | none | none | none |
| 14 | `live-db-reader-success` | Live DB Reader success path | D13 | 2 (`PARKED`) | No | none; no command runs | Q: record `PARKED` only | `PARKED` before execution (Glow QA Guide §3.3) | `audit/qa/hde-epic040/checks/live-db-reader-success/primary.log` | primary log | none | PF19 §3.3; PF27 `PARKED` |
| 15 | `qa-closeout-deliverables` | Close-out deliverables and coverage | D14 | 2, local/offline (no vendor) | No | closed | Q: manifest verification [K], append doc deltas, path proofs, updater checks | PASS per §12 block | `audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log` | path proofs | none | PF06 §0.4.1; PF19 §9.2.15.5 |

### 10.1 Classes and the PO Live QA subset

Glow QA Guide §3.5.6 requires a class label for every step and a statement of the PO subset.

- PO Live QA subset: check 11 only, the one vendor-focused class 3 step. The PO runs nothing else (§7.1).
- Class 1 (ops and identity): checks 1 and 2. They are "Pre-flight / internal" and "Handled by QA/infra outside PO's Live QA time". They are preconditions and cannot satisfy a behavior D-goal (Glow QA Guide §3.5.5).
- Class 2 (internal functional and determinism): checks 3 to 10 and 15, and the `PARKED` checks 12 and 14. Each executed class 2 check is "local/offline (no vendor)" (Glow QA Guide §3.3), "Pre-flight / internal" and "Handled by QA/infra outside PO's Live QA time". It proves the offline, in-process or loopback behavior of the tested source under the closed posture. It proves no live vendor, deployed-service or live-database behavior, and it satisfies no claim of live product behavior with vendor rails active.
- Closed-rails testing is the responsibility of CI and pre-merge QA (Glow QA Guide §3.4.8). §10.2 names that existing evidence for each closed-rails criterion. The class 2 checks re-execute the complete owner groups at the tested source alongside it.

### 10.2 Existing exact-head CI and PR evidence per closed-rails criterion

Glow QA Guide §3.4.14 binds the existing workflow records a Plan relies on. The work units per criterion come from the Implementation Plan v2.1 §8 acceptance table, with the PF10 Addendum 2.23 (Reader v2, PR06a) and 2.25 (Reader v1 errors, PR06b) overlays. Each run is the exact-head CI recorded in the named HDE Build Notes addendum for that PR's reviewed head.

| Work unit | PR | Exact-head CI run | Recorded in (HDE Build Notes addendum) |
| --- | --- | --- | --- |
| PR01 | amthorn78/glow-hdengine-v2#403 | 34393325625 | 2.6 "HDE-EPIC040-PR01 — Accept Source-Proven Catalog and Exact Contract Data", §5.2 |
| PR02 | amthorn78/glow-hdengine-v2#404 | 34784828890, attempt 2 | 2.11 "HDE-EPIC040-PR02 — PR Work-Unit Lineage Review v1.0" |
| PR03 | amthorn78/glow-hdengine-v2#405 | 34841280306 | 2.13 "HDE-EPIC040-PR03 — PR Work-Unit Lineage Review v1.0" |
| PR04 | amthorn78/glow-hdengine-v2#467 | 35777936856 (records the defined non-admitted interval of 2.15) | 2.19 "HDE-EPIC040-PR04-LINEAGE-001 — Bounded Application, Identity, and Consumer Integration" |
| PR05 | amthorn78/glow-hdengine-v2#492 | 36098781587 | 2.20 "HDE-EPIC040-PR05 — PR Work-Unit Lineage Review v1.0" |
| PR06 | amthorn78/glow-hdengine-v2#501 | 36210650937 | 2.22 "HDE-EPIC040-PR06 — PR Work-Unit Lineage Review v1.0" |
| PR06a | amthorn78/glow-hdengine-v2#508 | 36222478818 | 2.24 "HDE-EPIC040-PR06a — PR Work-Unit Lineage Review v1.0" |
| PR06b | amthorn78/glow-hdengine-v2#513 | 36257377433 | 2.26 "HDE-EPIC040-PR06b — PR Work-Unit Lineage Review v1.0" |
| OPS01 | not a PR | not applicable: accepted external release verification | 2.27 "HDE-EPIC040-OPS01 — OPS_EXECUTION_RESULT v1.4" |

| Criterion (closed-rails part) | Local class 2 run | Existing exact-head CI and PR evidence |
| --- | --- | --- |
| AC040-02 | check 4 | PR01, PR02 |
| AC040-03 | check 4 | PR01, PR03, PR04 |
| AC040-04 | checks 5 and 8 | PR02, PR03, PR04 |
| AC040-05 | check 5, with the `d0-discovery` admission probe | PR02, PR03, PR06; OPS01 |
| AC040-06 | check 6 | PR03, PR04, PR05, PR06 |
| AC040-07 (offline part) | check 7 | PR02, PR04, PR05 |
| AC040-08 | check 3 | every PR above; PR06 (convergence); OPS01 |
| AC040-09 (closed-rails part) | checks 8, 9 and 10 | PR01 to PR06; PR06a; PR06b; OPS01 |

Limits: each run is change-aware. Its lanes and tests were selected by that PR's diff (for PR01, "1,544 affected owner tests passed"), so it supports what those lanes executed at that head, not a full-suite run of the final tree. PR07 (amthorn78/glow-hdengine-v2#518, run 36272965542) changed documentation only and selected no test lane; it supports no criterion. AC040-01 is documentary (§2). The live part of AC040-07 and the live success path of AC040-09 have no local run; they are `PARKED` (§2).

## 11. Collection, dependencies and order

The collection is the 14 checks of §10 (numbers 1 to 12, 14 and 15; number 13 is removed), in the order listed. Counts: 14 checks; executor Q for 13 (11 executed checks and 2 `PARKED` records), executor P for 1; class 1: 2; class 2: 11 (9 executed, 2 `PARKED`); class 3: 1; conditional: 0; `PARKED` at plan time: 2 (`live-db-gate-readiness`, `live-db-reader-success`); all NOT RUN.

| Check | Depends on (must be PASS) | Notes |
| --- | --- | --- |
| `d0-discovery` | none | Gates every other executed check |
| `step-0b-doc-delta-capture` | `d0-discovery` executed (any status) | Records D0 blockers too |
| Checks 3 to 9 | `d0-discovery` | Independent of each other; run in the listed order |
| `sec-reader-http-live` | `d0-discovery`, `ac040-09-reader-http-in-process` | The in-process check carries CONNECT, QUERY, admission-refusal coverage and the production gating of the dev routes |
| `open-rails-showcompat-vendor` | `d0-discovery`, `ac040-04-09-compat-cli-offline` | Accepted local implementation proof (PF19 §3.3). The PO runs it after the QA/infra executor has recorded checks 1 to 10 |
| `live-db-gate-readiness` | none; `PARKED`, no execution | The QA/infra executor records it `PARKED` before `qa-closeout-deliverables` |
| `live-db-reader-success` | none; `PARKED`, no execution | As `live-db-gate-readiness` |
| `qa-closeout-deliverables` | every other check recorded (any status) | Runs last |

A dependency that is not PASS makes the dependent check `TOOLING_BLOCKED` with the dependency named, without executing its behavior commands. It is still recorded in the manifest. Dependencies read the step-log status, which is the execution layer of §12.

Reference counts from the QA Audit §4.4 (70 files, 2,090 tests, collected at the planning basis) are informational. A different count at the tested source is recorded and explained, not failed by itself.

## 12. Check Blocks

Common rules for every check:

- Executor: "PO command(s)" in a block is the Plan Templates field name. The executor is the one §7.1 assigns (Q or P in §10).
- Dependency posture: each check re-runs a step-local readiness line before its behavior commands: `python --version` reports 3.12, `python -c "import tools.qa.qa_harness, engine"` exits 0, and the posture of §5.2 is applied and recorded. If that readiness fails, the check is `TOOLING_BLOCKED` (or `FAIL_TOOLING` if the harness itself malfunctions after a good install).
- Syntax in this Plan is operational, not literal. The executor may normalize syntax without changing the proof target, rails, evidence identity or predicates, and records the exact command and the normalization in `command_provenance` (PF19 §3.4.10).
- Every command runs from the repository root. Exit codes are captured from the producer itself (`out=$(cmd); rc=$?` or the harness), never through a pipe that replaces the status.
- Decisive evaluation (RL-11; Glow QA Guide §3.4.8; C040-09 as approved as changed, §2.3). No evaluator program is written or composed at run time, and this Plan embeds no helper program, so no helper needs preapproval smoke validation. Each decisive predicate is evaluated in exactly one of two ways, and each block marks which:
  - [E], at execution: from the exit status or the printed value of a tracked, tested repository entrypoint (a repository test group, tool or validator, or the tracked harness `tools.qa.qa_harness`), or of a baseline command the block names (`test`, `cmp`, `sha256sum`, `wc -l`, `grep -c -F`, `stat`, `umask`, `python -m json.tool`, `curl`), compared with the literal expected value the block states. A predicate a block does not mark is [E].
  - [K], by Kronos at QA-110 from the captured artifacts the block names: structured-content predicates that no tracked entrypoint evaluates. The executor captures those artifacts, lists each [K] predicate in the body as `pending QA-110`, and does not evaluate it.
- Two result layers. The step-log `status` is the execution layer: every [E] predicate, every prerequisite, and the presence of every [K] capture, under the Plan Templates status predicates and causal precedence. A step-log `PASS` attests that layer only, and the body says so. Kronos's QA-110 per-task result adds the [K] layer (Glow QA Guide §3.1.2: Kronos reviews the evidence and retains per-task results). A false [K] predicate makes the per-task result `FAIL_BEHAVIOR`, or `FAIL_TOOLING` when the capture itself is malformed or untrustworthy, and routes the check under §7.3. The execution receipt stays unchanged as the pre-routing receipt. A check supports its criteria only when both layers pass, and QA-120 reports the per-task results.
- Pytest groups run directly, as `python -m pytest -q -p no:cacheprovider -rs` followed by the group's files as each block lists them, so that the skip report lists every skip with its reason. A pytest predicate's status follows the harness mapping of QA Audit L-41: rc 0 `PASS`; rc 5 `TOOLING_BLOCKED`; rc 2, 3, 4 or negative `FAIL_TOOLING`; any other rc `FAIL_BEHAVIOR`. `run_pytest_check` is not used: its argument grammar does not admit `-rs` (QA-80 inspection of `tools/qa/qa_harness.py` at `bf6e8da`).
- Recording: every primary log and its manifest entry are written through `record_check` (§8), invoked with `python -c` (C040-09 as approved as changed). The executor composes the `CheckResult` (QA Audit L-41) from what actually ran. That is recording, not evaluation.
- Recording by a hand operator (RL-11). For each PO-run check (in this Plan only `open-rails-showcompat-vendor`), the Product Owner produces the `pf27.step_log_header.v2` header and the manifest entry with the same tracked mechanism:
  1. Recording preflight, before the check's first behavior command: one `python -c` that imports `HarnessConfig`, `CheckResult`, `Status` and `record_check` from `tools.qa.qa_harness`, constructs `HarnessConfig("HDE-EPIC040", Path.cwd())` and one `CheckResult` for the check's `check_id` with status `TOOLING_BLOCKED`, a non-empty reason, no command, `exit_code` null and `command_provenance` `Not executed`, and prints the configured QA root. It writes nothing. Expected: exit 0 and a printed path ending in `audit/qa/hde-epic040`. If the preflight fails, the check is `TOOLING_BLOCKED` and no behavior command runs.
  2. During the check, the operator keeps outside the repository a body text file (the §8 body sections: each command with its exit code and output, and each [E] result) and the ordered list of executed argv.
  3. After the last command, one `python -c` invocation of `record_check` with `HarnessConfig("HDE-EPIC040", Path.cwd())` and one `CheckResult`: `check_id` and `check_name` as the block states; `status` and `status_reason` from the block's [E] predicates and prerequisites (the reason is empty only for `PASS`); `command` the ordered executed argv; `command_provenance` naming this Plan's block, the QA-90 task and any in-flight normalization; `exit_code` the final decisive command's exit code; `output` the body file's text; `evidence_artifacts` the block's deliverable paths; `intended_tokens` empty; `pf_refs` the block's in-document PF titles that the harness pattern admits (QA Audit L-42); and `captured_env` given explicitly with the values in force during the check's decisive commands, not the posture restored afterwards.
  4. `record_check` publishes the primary log and the manifest entry together and verifies both before it returns; on any error it rolls both back and writes nothing (QA-80 inspection at `bf6e8da`). Expected: exit 0. If it exits non-zero, the operator keeps the body file and the captures, stops, and reports the failure signature to Kronos. Kronos then records the check as `FAIL_TOOLING` at QA-110 (recording mechanism malfunction), and no status is inferred.
- `PARKED` records: the QA/infra executor records each `PARKED` check with `record_check`: status `PARKED`, no command, `exit_code` null, `command_provenance` `Not executed`, and a `status_reason` that states the reason, the controlling source, the affected acceptance claim and the reactivation condition given in its block (Plan Templates `PARKED` definition).
- A check that writes supplementary files creates its own check directory (`mkdir -p`) before its first write.
- Markers in primary-log bodies: a prerequisite gap found by `d0-discovery` is written as a line starting `BLOCKER:`; a documentation mismatch observed by any check is written as a line starting `DOC_DELTA:`. Step-0B and `qa-closeout-deliverables` collect those lines mechanically.
- Non-empty capture rule (PF27, PF19 §4.4.4): if a server log is empty when its server stops, the executor writes the single line `no server output` into it; no governed file is left empty.
- Nonclaims for every check: no QA PASS for the change, acceptance, closure, PF09 status change, deployment, token, new public route or flag, or PF edit follows from a check result.

### CHECK 1 `d0-discovery`: Discovery and tooling bootstrap

Surface / D-goal mapping: D0; all ACs (prerequisite).
Rails: closed posture (§5.2). Pins: `LC_ALL=C LANG=C TZ=UTC`.
Class: 1, ops and identity; Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF06-Canon-Change-Process-Guide §0.4.1.1; PF19-Canon-Glow-QA-Guide §3.6, §3.4.9.

Intent: establish and record, before any behavior check, the tested source, interpreter, dependencies, harness, CLI and tool entrypoints, rails, environment presence and admission of the actual checkout; record the initial absence of the QA root.

PO command(s), in order:

1. Initial absence: `test -e audit/qa/hde-epic040` (expected: absent at attempt 1). Capture the result before anything is written.
2. Environment presence: record SET or UNSET for `DATABASE_URL`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV`, `PORT`; values of `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`. Then apply the closed posture (§5.2).
3. Source identity (attribution only): `git rev-parse HEAD`; `git status --porcelain` line count.
4. Interpreter and install: a fresh venv outside the repository with Python 3.12; `python -m pip install -r requirements.txt -r requirements-dev.txt -e .`; `python -m pytest --version`.
5. Harness registration preflight: `python -c "from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check, run_pytest_check; from tools.evidence.update_evidence_index import _refresh_path_proof; print('harness_ready')"`.
6. CLI and tool help: `hdctl --help`; `hdctl showcompat --help`; `python tools/config/generate_config_artifacts.py --help`; `python tools/bodygraph/check_magic10_gate_readiness.py --help`; `python scripts/release_id_recompute.py --help`.
7. Admission: `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as f; b=f(); print(type(b).__name__, b.manifest.version, b.manifest.built_at_utc, len(b.manifest.files), b.release_id, b.mechanics['config_id'])"` and `sha256sum catalog/manifest.json`.
8. Ignore rules (informative): `git check-ignore -v` on the planned paths `audit/qa/hde-epic040/checks/d0-discovery/primary.log`, `audit/qa/hde-epic040/qa_step_logs_manifest.json`, `audit/docdeltas/hde-epic040_doc_deltas.md`.
9. Record the check with `record_check` (creates the QA root and manifest). Final decisive command: step 7's admission command.

Expected result:

PASS if:

- the QA root was absent at step 1 (or, on attempt 2, its presence is explained by `rerun_note.md`);
- Python is 3.12.x, install and `pytest --version` exit 0, and `harness_ready` prints;
- every help command exits 0; `showcompat` help lists `--source`, `--birthdate-a`, `--birthtime-a`, `--location-a`, `--birthdate-b`, `--birthtime-b`, `--location-b`, `--dump-reader`; comparator help lists `--compare-goldens`, `--goldens`, `--report`; readiness help lists `--user-id`, `--selection-file`; recompute help lists `--check-manifest-only`;
- admission prints `AdmittedMechanicsBundle 1.3.0 2026-08-24T18:04:49Z 45`, a `release_id` equal to the `catalog/manifest.json` SHA-256, and `m10-channel-state-v1.0.0`.

FAIL_BEHAVIOR if admission refuses, or its `release_id` differs from the manifest SHA-256, while `python scripts/release_id_recompute.py --check-manifest-only` exits 0 on the same checkout (unmodified members).

FAIL_TOOLING if the harness import fails after a successful install, or a tool crashes with a traceback during help.

TOOLING_BLOCKED if Python 3.12 is unavailable, install fails, an entrypoint or a Plan-used flag is missing (a Plan-to-repository mismatch; recorded as a Step-0B BLOCKER), the QA root pre-exists at attempt 1, or admission refuses because member bytes differ (`--check-manifest-only` exits 1: source contamination, not behavior).

Primary evidence: `audit/qa/hde-epic040/checks/d0-discovery/primary.log` (QA-created at the Canon-defined path). Also creates `audit/qa/hde-epic040/qa_step_logs_manifest.json` (Canon-defined; created by `record_check`). Tokens: `[]`, `[]`.

### CHECK 2 `step-0b-doc-delta-capture`: Step-0B doc-delta capture

Surface / D-goal mapping: D1; runbook self-honesty (PF27 Step-0B).
Rails: closed posture (§5.2). Pins as above.
Class: 1, ops and identity; Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF27-Canon-Plan-Templates (Mandatory Step-0 artifacts, Step-0B); PF19-Canon-Glow-QA-Guide §3.4.3.

Intent: mechanically record the doc deltas of §9.1 and any `d0-discovery` BLOCKER on both doc-delta surfaces.

PO command(s):

1. Preflight: `test -e audit/docdeltas/hde-epic040_doc_deltas.md` and `test -e audit/qa/hde-epic040/00_meta/doc_deltas.md` (expected: both absent). If either exists, do not overwrite it; record its SHA-256 and stop with `FAIL_TOOLING` for Moon Loop handling.
2. One embedded `python -c` writer that renders the §9.1 table rows, plus every `BLOCKER:` line read from the `d0-discovery` primary log, into UTF-8 Markdown without BOM, LF-terminated: a title line naming HDE-EPIC040 and this Plan, a `## BLOCKERS` section (IDs, or the line `none`), and a `## CAVEATS` section with one row per DD ID (ID, class, delta, drain target, owner, `Drives decision: No`). The same bytes are written to both paths, creating `audit/qa/hde-epic040/00_meta/` if needed.
3. Verification (final decisive command): `cmp audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md`, plus SHA-256 of both.

PASS if ([E]): both files exist and are non-empty (`test -s`), and `cmp` exits 0.

QA-110 predicates ([K], Kronos from the two doc-delta files): they are LF-terminated and without BOM; each of DD-01 to DD-12 appears exactly once; both sections are present; every `d0-discovery` BLOCKER appears under BLOCKERS.

FAIL_TOOLING if the files differ, are empty, or existing content would be overwritten; at QA-110, if a row, section, BLOCKER line or byte property is missing.

TOOLING_BLOCKED if `d0-discovery` produced no primary log.

Deliverables (QA-created): `audit/docdeltas/hde-epic040_doc_deltas.md` (draft or staging surface) and `audit/qa/hde-epic040/00_meta/doc_deltas.md` (authoritative epic capture), both Canon-defined surfaces of PF27 Step-0B. Primary evidence: `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log`. Tokens: `[]`, `[]`.

### CHECK 3 `ac040-08-evidence-validators`: Owner evidence coherence and evidence tests

Surface / D-goal mapping: D2; AC040-08; K040-REQ-012.
Rails: closed posture (§5.2). Pins as above.
Class: 2, local/offline (no vendor); Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF12-Canon-HDE-Schemas-and-Artifacts §8.3, §8.6; PF19-Canon-Glow-QA-Guide §2.2.7, §2.2.11, §14.1.

Intent: re-verify, read-only, that the owner-generated evidence graph and governed families are coherent at the tested source, and run the evidence and QA-tooling test group.

Venue evidence (RL-01; front matter), before command 1: `umask` and `stat -c '%a %n' docs/evidence/INDEX.sha256`, both recorded in the body. The mode printed for that file is the checkout mode against which group G's `tests/evidence/test_evidence_index_missing_state.py` compares a regenerated file, which the updater creates with mode 644.

PO command(s), each expected to exit 0 (Audit-proven L-13):

1. `python tools/evidence/update_evidence_index.py --check`
2. `python tools/evidence/orientation_demo.py --check`
3. `python tools/evidence/validate_evidence_paths.py`
4. `./ci/checks/check_mirror_schema.sh` (direct invocation; the file is a Python script)
5. `ci/checks/check_evidence_index_hash.sh`
6. `python tools/evidence/run_canonical_json_gate.py --check-only`
7. `python tools/evidence/check_lf_endings.py`
8. `ci/checks/check_env_pins.sh`
9. `python tools/config/generate_config_artifacts.py --check`
10. Pytest group G (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_cli_conformance_artifacts.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_dev_conjunction_identity.py tests/evidence/test_engine_core_evidence.py tests/evidence/test_epic030_pr05_category_framework_evidence.py tests/evidence/test_evidence_index_missing_state.py tests/evidence/test_evidence_tool_ownership.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_rails_ci_workflow_integration.py tests/evidence/test_sanity_pipeline.py tests/qa/test_qa_tool_ownership.py`

Supplementary, non-gating: a SHA-256 over the sorted file list and contents of `docs/evidence/`, `artifacts/` and `audit/gates/` before command 1 and after command 10, reported to Kronos if different.

PASS if all ten commands exit 0 and the pytest summary reports no failure or error; skips are listed with reasons.

FAIL_BEHAVIOR if a validator runs normally and reports incoherent delivered evidence (a governed error token), or a test asserts a contradiction. The RCA classifies an evidence-coherence failure as a documentation or evidence failure, not a runtime failure.

FAIL_TOOLING if a validator crashes (traceback), or pytest exits 2, 3, 4 or negative.

TOOLING_BLOCKED if `d0-discovery` is not PASS, an entrypoint is missing, or pytest collects no test (rc 5). Also `TOOLING_BLOCKED`, not `FAIL_BEHAVIOR` (venue rule of the front matter): group G exits 1, every failure it reports is in `tests/evidence/test_evidence_index_missing_state.py` at its file-mode equality assertion, and the recorded mode of `docs/evidence/INDEX.sha256` is not 644 or was not recorded. AC040-08 then relies for that test on the exact-head CI evidence of §10.2, and a rerun in a checkout whose modes are 644 is an execution-fault rerun under §7.3. Kronos confirms this attribution at QA-110 from the pytest output and the venue evidence.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log`. No other file. Tokens: `[]`, `[]`.

### CHECK 4 `ac040-02-03-catalog-config`: Catalog, configuration and schemas

Surface / D-goal mapping: D3; AC040-02, AC040-03; K040-REQ-003 to K040-REQ-006; PF09.3 HDE-SEPA005.1, HDE-SEPA005.2.
Rails: closed posture (§5.2). Pins as above.
Class: 2, local/offline (no vendor); Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.1, .2); PF10 Addendum 2.5 (Channel taxonomy).

Intent: prove the delivered catalog and mechanics configuration have the approved structure, and run the catalog, configuration and schema test group (mutation matrix, negative cases, bundle compatibility).

PO command(s):

1. Catalog digests: `sha256sum catalog/channels_v1.json catalog/magic10_mechanics_v1.json` (Audit-proven L-53, L-54). The digests bind the bytes Kronos evaluates at QA-110; no probe program runs.
2. Pytest group A (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/config/test_registry_catalog_contract.py tests/config/test_magic10_contracts.py tests/config/test_manifest_schema.py tests/config/test_typed_bundles.py tests/config/test_alias_policy_enforcement.py tests/config/test_config_loader_unknown_ids_fail_closed.py tests/config/test_registry_report.py tests/config/test_registry_report_determinism.py tests/config/test_registry_report_indexing.py tests/compare/test_arrays_as_sets.py tests/m10/test_defs_order.py tests/m10/test_thresholds_rounding.py`

PASS if ([E]): both digests are captured and the pytest run exits 0.

QA-110 predicates ([K], Kronos from the two catalog files at the tested source whose SHA-256 equals the captured digests):

- `catalog/channels_v1.json` has key `channels` with 36 rows; each row has exactly the keys `centers`, `circuit_primary`, `domains`, `flags`, `gates`, `id`, `primary_domain`, `substream`; every `gates` pair is ascending; the 36 pairs are unique; no value is null;
- `catalog/magic10_mechanics_v1.json` has `config_id` `m10-channel-state-v1.0.0`, `schema` `magic10_mechanics_config.v1`, 20 `signals` with unique `signal_id`, 3 `profiles` (`activation_bp_v1`, `coherence_bp_v1`, `expression_bp_v1`), 10 `category_weights`; `equilibrium_score` uses `twice_min_owner_mass_v1`, `counterweight_ratio` uses `companionship_em_mass_v1`, the other 18 use `weighted_state_sum_v1`.

FAIL_BEHAVIOR if a test fails; at QA-110, if a structural predicate is false.

FAIL_TOOLING if pytest malfunctions.

TOOLING_BLOCKED if `d0-discovery` is not PASS or a listed file is missing.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log`. Tokens: `[]`, `[]`.

### CHECK 5 `ac040-04-05-admission-identity`: Admission, pure core and release identity

Surface / D-goal mapping: D4; AC040-04, AC040-05; K040-REQ-007 to K040-REQ-009; PF09.3 HDE-SEPA005.3, HDE-SEPA005.4.
Rails: closed posture (§5.2). Pins as above.
Class: 2, local/offline (no vendor); Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.3, .4); PF10 Addenda 2.12, 2.22, 2.27.

Intent: prove that the complete release is intact and bound to the accepted OPS01 attestation, and run the admission, refusal-class, pure-core, determinism and identity test group.

PO command(s):

1. `python scripts/release_id_recompute.py --check-manifest-only` (expected rc 0; audits the bytes and size of all 45 members). Never run this script in any other mode.
2. `sha256sum catalog/manifest.json`.
3. `(cd audit/ops/hde-epic040/ops01 && sha256sum -c SHA256SUMS)` (expected 7 lines OK, rc 0; read-only).
4. Binding ([K]): no command and no probe program. Kronos reads `audit/ops/hde-epic040/ops01/attestation.json` at QA-110, whose bytes step 3 binds through `SHA256SUMS`, and compares it with the step-2 digest.
5. Pytest group B (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/config/test_production_admission.py tests/config/test_execution_coherence.py tests/core/test_engine_core_purity.py tests/core/test_engine_core_determinism.py tests/core/test_engine_core_abba.py tests/m10/test_m10_symmetry_identity.py tests/runtime/test_identity.py tests/scripts/test_cut_release_manifest.py tests/reader_v1/test_release_pack.py`

PASS if ([E]): steps 1, 3 and 5 exit 0 and step 2's digest is captured.

QA-110 predicates ([K], Kronos from `attestation.json` and the step-2 digest): the fields `release_id` and `manifest_sha256` both equal the step-2 digest; `validation_result` is `PASS` and `release_admission` is `PR06R_B_FINAL_PASS`; `source_commit`, `validation_result` and `release_admission` are recorded in the QA-110 result.

FAIL_BEHAVIOR if step 1 reports a `MANIFEST_ERROR` on the tested source or a test fails; at QA-110, if the binding fails.

FAIL_TOOLING if a command crashes or pytest exits 2, 3, 4 or negative.

TOOLING_BLOCKED if `d0-discovery` is not PASS or an OPS01 file is missing.

Limits: OPS01 evidence is corroboration, not QA evidence; the attestation is not rebuilt. Primary evidence: `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log`. Tokens: `[]`, `[]`.

### CHECK 6 `ac040-06-golden-comparison`: Read-only golden comparison

Surface / D-goal mapping: D5; AC040-06; K040-REQ-010; PF09.3 HDE-SEPA005.4.
Rails: closed posture (§5.2). Pins as above.
Class: 2, local/offline (no vendor); Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.4); PF10 Addendum 2.20; PF01-Canon-HDE-Math-Spec §9.5.

Intent: prove that the complete eight-case collection matches at the repository root through the canonical code, that the result repeats byte for byte, that a deliberate expected-value change is reported as a mismatch, and that nothing in the checkout changes.

PO command(s):

1. Before-digest: SHA-256 over the sorted list of `path` and file SHA-256 for every regular file under the repository root, excluding `.git/`, `audit/qa/hde-epic040/`, `__pycache__/` and `.pytest_cache/`.
2. Match run 1: `python tools/config/generate_config_artifacts.py --compare-goldens .` with stdout saved to `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json` (expected rc 0).
3. Match run 2: the same command, stdout to `compare_match_run2.json` in the same directory (expected rc 0).
4. Altered input (embedded `python -c`): load `tests/fixtures/magic10/v1/goldens.json`, change only case `M10-G001` `expected.signals[0].q` from `0` to `1`, and write `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json`. Record the SHA-256 of both files and the one changed leaf.
5. Mismatch run: `python tools/config/generate_config_artifacts.py --compare-goldens . --goldens audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json --report <a new path in a temporary directory outside the repository>` (expected rc 1, stderr `GOLDEN_COMPARISON_MISMATCH:<n>`). Copy the report to `compare_mismatch_report.json` in the check directory and record both SHA-256 values.
6. After-digest as in step 1, taken before any test runs so that only the comparator runs fall between the two digests.
7. Byte identity: `cmp` of `compare_match_run1.json` and `compare_match_run2.json` (expected rc 0).
8. Pytest group C (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/config/test_config_artifacts.py`.

Never run the comparator script without `--compare-goldens` or `--check` (write paths; QA Audit L-07).

PASS if ([E]):

- runs 1 and 2 exit 0, and the two report files are byte-identical (step 7);
- the mismatch run exits 1 and its stderr is `GOLDEN_COMPARISON_MISMATCH:<n>` with a printed n of at least 2;
- the pytest run exits 0;
- the before and after digests are equal.

QA-110 predicates ([K], Kronos from `compare_match_run1.json`, `compare_mismatch_report.json`, `tmp_goldens_altered.json`, the fixture at the tested source and the manifest SHA-256 recorded by `d0-discovery`):

- both match reports have `ok` true, empty `mismatches`, `cases` listing exactly `M10-G001` to `M10-G008` each with `outcome` `match`, `config_id` `m10-channel-state-v1.0.0` and `candidate_release_id` equal to the manifest SHA-256;
- the mismatch report has `ok` false; every mismatch row has `case_id` `M10-G001`; one row has `path` `transcription.expected`; cases `M10-G002` to `M10-G008` have `outcome` `match`;
- `tmp_goldens_altered.json` differs from `tests/fixtures/magic10/v1/goldens.json` only in case `M10-G001` `expected.signals[0].q`, changed from `0` to `1`.

FAIL_BEHAVIOR if the root comparison mismatches or refuses on the tested source, the altered collection is reported as a match, runs 1 and 2 differ, the digests differ, or a test fails; at QA-110, if a match-report predicate is false or the mismatch names another case.

FAIL_TOOLING if the altered file is refused with `GOLDENS_INVALID` (a QA input defect; Moon Loop eligible) or the report copy differs; at QA-110, if the altered file differs from the fixture in anything but the one leaf.

TOOLING_BLOCKED if `d0-discovery` is not PASS, or a run refuses with `RAILS_CLOSED_REQUIRED` (environment) or with an admission refusal that `--check-manifest-only` attributes to modified members.

Deliverables (QA-created, in `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/`): `compare_match_run1.json`, `compare_match_run2.json`, `tmp_goldens_altered.json`, `compare_mismatch_report.json`. Primary evidence: `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log`. Tokens: `[]`, `[]`.

### CHECK 7 `ac040-07-gate-ingress-offline`: Gate ingress and readiness, offline

Surface / D-goal mapping: D6; AC040-07 (offline part); K040-REQ-007, K040-REQ-011; PF09.3 HDE-SEPA005.3, HDE-SEPA005.5.
Rails: closed posture (§5.2; no `DATABASE_URL`). Pins as above.
Class: 2, local/offline (no vendor); Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.3, .5); PF10 Addendum 2.20.

Intent: run the Gate normalization and rejection corpus and the readiness tool's tests, and prove the readiness command's typed refusals at runtime without a database, including that an unavailable dataset is never reported ready.

PO command(s) (readiness command Audit-proven L-09):

1. Empty selection: `--selection-file` pointing to an empty file created outside the repository (expected rc 5, `READINESS_EMPTY_SELECTION`).
2. Invalid selection: `--user-id 00000000-0000-0000-0000-00000000000G` (expected rc 5, `READINESS_SELECTION_INVALID`).
3. Unavailable dataset: `--user-id 00000000-0000-0000-0000-000000000001` under the closed posture with `DATABASE_URL` unset (expected rc 5, `READINESS_UNAVAILABLE`; no report on stdout).
4. Pytest group D (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/bodygraph/test_gates.py tests/bodygraph/test_projection_gate_ingress.py tests/bodygraph/test_resolve_compat_chart.py tests/bodygraph/test_check_magic10_gate_readiness.py`

The open-rails refusal of the readiness command (`RAILS_CLOSED_REQUIRED` when `SAFE_MODE=0`) is not re-run here: group D's `tests/bodygraph/test_check_magic10_gate_readiness.py` already proves it (QA-70 review v1.1 FND-002, RL-07), and no command in this Plan changes rails inside a check.

PASS if commands 1 to 3 return the stated exit code and token with empty stdout, and the pytest run exits 0.

FAIL_BEHAVIOR if a refusal is missing or wrong, any command emits a READY report, or a test fails.

FAIL_TOOLING if a command crashes with a traceback or pytest malfunctions.

TOOLING_BLOCKED if `d0-discovery` is not PASS.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log`. Tokens: `[]`, `[]`.

### CHECK 8 `ac040-04-09-compat-cli-offline`: Compat and CLI, local/offline

Surface / D-goal mapping: D7; AC040-04 (application boundary), AC040-09; K040-REQ-004, K040-REQ-008.
Rails: closed posture (§5.2). Pins as above.
Class: 2, local/offline (no vendor); Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF19-Canon-Glow-QA-Guide §3.3 (local/offline label).

Intent: run the eligibility, no-user boundary, AB/BA identity, CLI source, error parity, canonical-bytes and file-input tests. Proof class: local/offline (no vendor); it does not prove live vendor behavior.

PO command(s): pytest group E (final decisive command), run directly (§12): `python -m pytest -q -p no:cacheprovider -rs tests/compat/test_evaluate_pair_eligibility.py tests/compat/test_conjunction_no_user_boundary.py tests/compat/test_compat_public_ab_ba_identity.py tests/compat/test_compat_public_lf_bom.py tests/compat/test_abba_parity.py tests/compat/test_hde_epic037_v2_adapter_to_compat.py tests/cli/test_showcompat_sources.py tests/cli/test_errors_parity.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_cli_file_inputs.py tests/cli/test_showcompat_parity_and_identity.py tests/artifacts/test_cli_text_artifacts_bom_lf.py tests/qa/test_cli_admin_dumps.py tests/qa/test_cli_admin_parity.py tests/runtime/test_emit_public_legacy_helper.py tests/epic003/test_meta_invocation_ok.py`

PASS if rc 0. FAIL_BEHAVIOR if rc 1. FAIL_TOOLING if rc 2, 3, 4 or negative. TOOLING_BLOCKED if rc 5, a file is missing, or `d0-discovery` is not PASS.

Skips (RL-12): the `-rs` summary lists every skipped test with its reason, and the executor copies each skip line, reason included, into the body's `=== PREDICATES ===` section. Skips contribute no proof and are not counted as passes. Under the closed posture the three tests of `tests/cli/test_showcompat_parity_and_identity.py` that skip with "showcompat vendor calls require open rails" (QA-70 review v1.1 FND-007) are not vendor coverage (Glow QA Guide §2.3). Vendor-backed behavior is carried by `open-rails-showcompat-vendor` (check 11) alone.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log`. Tokens: `[]`, `[]`.

### CHECK 9 `ac040-09-reader-http-in-process`: Reader, HTTP and transport, in-process

Surface / D-goal mapping: D8; AC040-09; Reader v1 and v2 contracts (PF10 Addenda 2.23, 2.25).
Rails: closed posture (§5.2). Pins as above.
Class: 2, local/offline (no vendor), in-process; Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF05-Canon-HDE-CLI-API-Vendor-Ref §5 as overridden by PF10 Addenda 2.23 and 2.25; PF19-Canon-Glow-QA-Guide §3.2.

Intent: run the Reader v1 and v2 route tests (success, eligibility, refusal classes, admission refusal as 503 `ERR_M10_MANIFEST_MISMATCH`, every non-POST method including CONNECT and QUERY on all three factories), the emitter and schema tests, transport proofs and keys-only logging tests. Proof class: in-process Flask test client with injected current rows; it is not live transport and not a live database. It also carries, in-process, the production gating of the dev routes that `sec-reader-http-live` no longer probes (RL-06 option (b)): `tests/http/test_reader_post_v1.py` (dev `GET /reader` refused with 403 `ERR_READER_FORBIDDEN` under a production `APP_ENV`) and `tests/http/test_dev_conjunction_http.py` (the three dev conjunction routes refused with 403 `ERR_WRITER_FORBIDDEN` under `APP_ENV=prod`) (QA-80 inspection at `bf6e8da`; routes Audit-proven L-25).

PO command(s): pytest group F (final decisive command), run directly (§12): `python -m pytest -q -p no:cacheprovider -rs tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py tests/http/test_compat_endpoint_contract.py tests/http/test_dev_conjunction_http.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py tests/adapter/test_compat_writer_transport.py tests/reader_v1/test_emitter.py tests/reader_v1/test_goldens.py tests/reader_v1/test_schema.py tests/transport/test_a7_transport_proofs.py tests/compliance/test_log_shape_snapshot.py tests/compliance/test_logging_filter_keys_only_and_redactions.py`

PASS if rc 0. FAIL_BEHAVIOR if rc 1. FAIL_TOOLING if rc 2, 3, 4 or negative. TOOLING_BLOCKED if rc 5, a file is missing, or `d0-discovery` is not PASS.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log`. Tokens: `[]`, `[]`.

### CHECK 10 `sec-reader-http-live`: Reader route security over loopback HTTP (closed posture)

Surface / D-goal mapping: D9; PO Q-1; AC040-09 (closed-rails part); K040-REQ-008, K040-REQ-013.
Rails: closed posture (§5.2) for the server and the client: `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`, `PORT=8000` for the server, no `DATABASE_URL`, no vendor keys. Pins as above.
Class: 2, local/offline (no vendor), loopback HTTP; Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF19-Canon-Glow-QA-Guide §3.2, §3.5.10, §14.4.2; PF10 Addenda 2.19, 2.23, 2.24, 2.25.

Intent: over real HTTP on the loopback interface, against the factory `adapter.factory:create_app()` started from the tested tree, prove that every request-shape, version, size and method refusal on `POST /api/reader` returns its governed envelope and headers, and that no public response carries a secret, stack trace, Gate payload or internal diagnostic. The production Reader route (L-20, L-21, L-23), `GET /internal/version` (L-28) and the factory's HTML 404 (L-24) do not read `APP_ENV`, so these probes are answered under `APP_ENV=dev` as they would be under a production `APP_ENV` (QA-80 inspection at `bf6e8da` of `adapter/http_reader.py`, `adapter/factory.py`, `engine/db/adapter.py` and `engine/http/compat_handler.py`: the only `APP_ENV` gates there cover the dev routes, namely dev `GET /reader`, `/internal/dev/sampler` and the three dev conjunction routes, and `/api/compat/v1`). This local process is not production, and the check proves nothing about the deployed service (Glow QA Guide §3.5.5, §14.4.2). Admission-refusal propagation and CONNECT/QUERY coverage come from check 9 (in-process) and are cited, not repeated.

Dev-route production gating (the former probes S-22 to S-25; RL-06 option (b)): not claimed over HTTP. The closed posture sets `APP_ENV=dev`, which enables those routes, and this Plan probes no deployed service. Their refusal under a production `APP_ENV` is covered in-process, class 2, by group F in check 9 (`tests/http/test_reader_post_v1.py`; `tests/http/test_dev_conjunction_http.py`).

Discovery step: none needed; routes and envelopes are Audit-proven (L-20 to L-28).

PO command(s):

1. Start the server (§5.2 declaration) in the background with stdout and stderr to `audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log`. Service readiness: poll `GET http://127.0.0.1:8000/internal/version` until HTTP 200, at most 30 seconds, and record each poll's HTTP code. No probe is sent before the first HTTP 200.
2. Send probes S-01 to S-21 and S-26 with `curl`, capturing for each the status, header lines (names lower-cased, values verbatim) and body separately from curl's stderr, and append one JSON object per probe to `audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl` with keys `probe_id`, `method`, `target`, `request_body_bytes`, `request_body_sha256`, `status`, `headers`, `body`.
3. Stop the server and confirm port 8000 is closed.
4. Capture check (final decisive command): `wc -l` of `http_probes.jsonl` (expected 22) and its `sha256sum`.

Probes (request bodies use the synthetic UUIDs `00000000-0000-0000-0000-000000000001` and `00000000-0000-0000-0000-000000000002`, Audit-proven L-50; `Content-Type: application/json; charset=utf-8`):

| Probe | Request | Expected |
| --- | --- | --- |
| S-01 | `GET /internal/version` | 200; `release_id` equals the manifest SHA-256 (`build_commit` is a static literal, not source identity) |
| S-02 | `POST /api/reader?v=1`, valid body | 503 `ERR_M10_RESOLVER_UNAVAILABLE` |
| S-03 | `POST /api/reader?v=2`, valid body | 503 `ERR_M10_RESOLVER_UNAVAILABLE` |
| S-04 | `POST /api/reader` (no `v`) | 400 `ERR_READER_INVALID_VERSION` |
| S-05 | `POST /api/reader?v=3` | 400 `ERR_READER_INVALID_VERSION` |
| S-06 | `POST /api/reader?v=1&v=2` | 400 `ERR_READER_INVALID_VERSION` |
| S-07 | `POST ?v=1`, body `{"a_id":` | 422 `ERR_READER_INVALID_INPUT` |
| S-08 | `POST ?v=1`, valid body preceded by a UTF-8 BOM | 422 `ERR_READER_INVALID_INPUT` |
| S-09 | `POST ?v=1`, valid body plus key `"c":1` | 422 `ERR_READER_INVALID_INPUT` |
| S-10 | `POST ?v=1`, `a_id` in upper case | 422 `ERR_READER_INVALID_INPUT` |
| S-11 | `POST ?v=1`, empty body | 422 `ERR_READER_INVALID_INPUT` |
| S-12 | `POST ?v=2`, 32,769-byte body with `Content-Length` | 422 `ERR_READER_INVALID_INPUT` |
| S-13 | `POST ?v=2`, 32,769-byte body sent chunked, no `Content-Length` | 422 `ERR_READER_INVALID_INPUT` |
| S-14 to S-21 | `GET`, `HEAD`, `OPTIONS`, `PUT`, `PATCH`, `DELETE`, `TRACE`, `PROPFIND` on `/api/reader?v=2` | 405; `Allow: POST`; body exactly `{"code":"ERR_NOT_FOUND","error":"not found","ok":false,"schema":"v1"}` plus LF (no body for HEAD) |
| S-26 | `GET /api/reader/missing` | 404 HTML (known limitation O-P06a-22; observed, not failed) |

Probe IDs S-22 to S-25 are retired, not reused.

PASS if ([E]): the server answered HTTP 200 on `GET /internal/version` within 30 seconds before any probe was sent; every probe ran and `http_probes.jsonl` has exactly 22 lines; the server stopped and port 8000 is closed.

QA-110 predicates ([K], Kronos from `http_probes.jsonl` and the manifest SHA-256 recorded by `d0-discovery`):

- each probe returns its expected status and code;
- every JSON response from S-02 to S-21 has `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store` and no `ETag`; every Reader error body from S-02 to S-21 (all except the bodiless HEAD probe) has exactly the keys `code`, `error`, `ok` (false) and `schema` (`"v1"`), is canonical and ends with exactly one LF;
- no response body or header from S-01 to S-21 and S-26 contains `Traceback`, `File "`, `psycopg`, `postgresql`, a `gates` key, or a JSON number in any Reader error body.

FAIL_BEHAVIOR at QA-110 if the server was reachable and a probe contradicts its expected status, code, envelope, header or leak predicate (PF19 §3.5.10).

FAIL_TOOLING if a capture is missing after its probe ran or `http_probes.jsonl` does not have 22 lines; at QA-110, if a capture is malformed.

TOOLING_BLOCKED if the server never becomes ready (connection refused, HTTP 000 or non-HTTP response), `PORT` is unavailable, or check 9 is not PASS.

Deliverables (QA-created, in `audit/qa/hde-epic040/checks/sec-reader-http-live/`): `http_probes.jsonl` (decisive captures); `gunicorn_server.log` (supplementary, non-gating; a server log that is empty is recorded as `no server output`). Primary evidence: `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log`. Tokens: `[]`, `[]`.

Nonclaims: no deployed-service, production-environment, live-DB or admission-refusal-over-live-HTTP claim; no HTTP claim about the dev routes.

### CHECK 11 `open-rails-showcompat-vendor`: Bounded open-rails vendor step

Surface / D-goal mapping: D10; PO Q-2; PF05 §7.3.9; AC040-04, AC040-09 (vendor-backed functional proof of the CLI, resolver, core and emitter).
Rails: CLI-local vendor posture (§5.2) for the whole check; the closed posture is restored when the check ends, before any other check. Pins as above.
Class: 3, vendor-focused; this check is the whole PO Live QA subset (§7.1, §10.1). PO-only and Kronos-guided.
PF anchors: PF05-Canon-HDE-CLI-API-Vendor-Ref §7.3.9; PF19-Canon-Glow-QA-Guide §3.3, §3.5.7; PF07-Canon-Glow-Infrastructure §2.7.

Proof class: vendor-backed no-user behavior (birth-only). Allowed inputs: `--source vendor` and the six birth flags. Forbidden: `--user-a`, `--user-b`, `--source db`, `--source auto`, any app user identifier or `person_uid` from the caller, DB-backed BodyGraphs as input, inline secret values, `--dump-admin-dir`, `--conjunction`.

Intent: prove, against HumanDesignAPI, that the delivered CLI resolves both birth tuples, evaluates the pair through the admitted release and emits canonical output, identically for AB and BA, with a bands-only Reader v1 dump.

PO command(s):

0. Readiness and recording preflight (§12): the step-local readiness line, then the recording preflight of §12 "Recording by a hand operator", item 1 (expected exit 0 and a printed QA root ending in `audit/qa/hde-epic040`).
1. Preflight matrix (recorded in the body): Plan and QA-90 task identity; PO authorization reference; CLI-local vendor posture applied; `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` SET; `HDAPI_BASE_URL`, `DATABASE_URL`, retired keys, `ENGINE_ENV` UNSET; check 8 PASS; tuple provenance (default L-51 or PO-named); the exact two commands below; and `sha256sum catalog/manifest.json` for the QA-110 release binding.
2. Create the check directory and write `vendor_request.txt` in it (commands with tuples, environment presence and rails values, time, executor, authorization reference; no secret value).
3. AB run: `hdctl showcompat --source vendor --birthdate-a <A date> --birthtime-a <A time> --location-a <A location> --birthdate-b <B date> --birthtime-b <B time> --location-b <B location> --dump-reader audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json`, stdout to `vendor_run_ab.json`, stderr captured separately.
4. BA run: the same with tuples A and B swapped, `--dump-reader` to `reader_v1_ba.json`, stdout to `vendor_run_ba.json`.
5. Byte identity: `cmp vendor_run_ab.json vendor_run_ba.json` and `cmp reader_v1_ab.json reader_v1_ba.json`, both in the check directory (expected rc 0 each).
6. Secret scan: count occurrences of the `HD_API_KEY` and `GEO_API_KEY` values in every file of the check directory, in both stderr captures and in the §12 body file as it stands, without printing any value (for example `grep -c -F` with the value taken from the environment, which is still set). Expected 0 everywhere. The stderr text of both runs is then added to the body.
7. Parse check: `python -m json.tool` over each of `vendor_run_ab.json`, `vendor_run_ba.json`, `reader_v1_ab.json` and `reader_v1_ba.json`, output discarded (expected rc 0 each). The final decisive command is its last invocation, on `reader_v1_ba.json`.
8. Record the check by the hand-operator mechanism of §12, items 2 to 4, with `captured_env` holding the CLI-local vendor values in force during commands 3 and 4.
9. Restore the closed posture and unset the vendor keys (§7.5). This ends the check.

PASS if ([E]): the readiness and recording preflights pass; every preflight row holds; both runs exit 0 with non-empty stdout; both stdout files are byte-identical and both dumps are byte-identical; the secret scan is zero; all four files parse.

QA-110 predicates ([K], Kronos from the four JSON files, the manifest digest recorded in command 1, and the body):

- each stdout is canonical JSON ending with exactly one LF and no CR, with exactly the keys `schema` (`magic10_compat_result.v1`), `config_id` (`m10-channel-state-v1.0.0`), `release_id` (equal to the manifest SHA-256), `pair_key`, `signals` (20), `categories` (10, in the order `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`);
- each Reader dump has exactly six keys, `reader_version` `v1`, `categories` of one `harmony` item or `[]`, no JSON number, and ends with one LF;
- the exercised-versus-inferred statement below matches the captured stderr.

FAIL_BEHAVIOR only if every prerequisite is proven, both commands ran, no tooling or secret fault occurred, and the output contradicts a predicate: an [E] predicate at execution, or a [K] predicate at QA-110. Before this status the cause is classified per PF19 §3.5.7 (vendor contract mismatch, request shaping, response mapping, product implementation defect, or QA expectation mismatch), in the body at execution or in the QA-110 result.

FAIL_TOOLING if a secret value appears in any file (quarantine it, do not commit), a forbidden input was used, an evidence file is missing after an attempted run, a command was changed by guesswork, or the recording invocation fails after its preflight passed (§12, item 4).

TOOLING_BLOCKED if a credential, input or authorization is missing, `HDAPI_BASE_URL` is set, the readiness or recording preflight fails, the CLI returns a typed provider refusal caused by rails, configuration, credentials, account or vendor availability, or check 8 is not PASS.

Deliverables (QA-created, in `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/`): `vendor_request.txt`, `vendor_run_ab.json`, `vendor_run_ba.json`, `reader_v1_ab.json`, `reader_v1_ba.json`. The birth tuples are recorded verbatim as PF19 §3.3's substituted birth-input record; they must be synthetic (QA Audit QA50-S01). Primary evidence: `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log`. Tokens: `[]`, `[]`.

Exercised versus inferred: exercised = both birth tuples resolved through HumanDesignAPI, pair evaluated, canonical output and Reader v1 dump emitted. Inferred, not exercised, unless the captured stderr shows it = the exact vendor resource path, auth-header family and adapter status. Not exercised = rate-limit and `Retry-After` handling, typed vendor error mapping, malformed-response handling, v1 legacy guard, mapped-cache persistence, Reader v2 and any deployed service.

### CHECK 12 `live-db-gate-readiness`: Live read-only Gate readiness (PARKED)

Surface / D-goal mapping: D11; AC040-07 (live part); K040-REQ-011; PF09.3 HDE-SEPA005.5.
Rails: none; no command runs. The `PARKED` record is written under the closed posture.
Class: 2 (`PARKED`; not executed). The QA/infra executor writes the `PARKED` record (§7.1).
PF anchors: PF19-Canon-Glow-QA-Guide §3.3; PF27-Canon-Plan-Templates ("Step-log header schema expectations (required; v2)", `PARKED`); PF10 Addendum 2.20.

Status: `PARKED` before execution, by this Plan (QA-80, 2026-09-27), under QA-70 review v1.1 RL-09. It is intentionally not attempted.

- Reason: the check needs current rows of `public.hde_body_graphs_current` keyed to app users, and a Product Owner list of their UUIDs. Before the App, no app-level user IDs and no persistent user-bound BodyGraphs exist that QA may rely on, and QA must not create them. A requirement that assumes existing users is blocked by environment, not failed acceptance.
- Authority and controlling source: Glow QA Guide §3.3 (such requirements "are treated as blocked by environment" and "must be explicitly called out in epic-level QA plans and deferred to a future epic"); decision reference: QA-70 review v1.1, FND-003 and RL-09.
- Affected acceptance claim: AC040-07, live part (read-only Gate readiness observed against current rows). The offline part stays with `ac040-07-gate-ingress-offline`, and no AC040-07 live claim is made.
- Reactivation condition: a future epic, under its approved Specification and the applicable phased HDE Build Checklist, defines user-bound QA surfaces once the Glow App user model exists (Glow QA Guide §3.3). The check is then re-planned in that epic's QA Plan.

No commands, inputs or probes. No PO input is requested (§6).

Recording: the QA/infra executor records the check with `record_check` as `PARKED` (§12, `PARKED` records), with a `status_reason` stating the four items above. Primary evidence: `audit/qa/hde-epic040/checks/live-db-gate-readiness/primary.log` (QA-created; the `PARKED` receipt). Tokens: `[]`, `[]`.

Nonclaims: no readiness observation, no database access, and no claim that the live dataset is or is not ready.

### CHECK 13 `live-db-reader-refusal`: removed

Removed by QA-80 under QA-70 review v1.1 RL-08 (its first option). The check is not in the collection, has no executor, produces no evidence and has no manifest entry. Under canon it had no valid live-behavior claim: DB-backed paths are not valid Live QA behavior acceptance before the App (Glow QA Guide §3.3; FND-004). Re-postured to the closed posture, it would leave only a secret-safety observation that needs the shared-database DSN in the console, and the class 1 and class 2 executor handles no plaintext secret and connects to no database (§7.1). Q-1 stays covered by checks 9 and 10: `POST /api/reader` with v=1 and v=2, the governed 405, the error envelopes and the admission refusal paths (PO disposition Q-1). The number 13 is kept so that check numbers match Plan v1.0 and the review.

### CHECK 14 `live-db-reader-success`: Live DB Reader success path (PARKED)

Surface / D-goal mapping: D13; AC040-09; Reader v1 and v2 over live HTTP with live rows (PF10 Addendum 2.23).
Rails: none; no command runs. The `PARKED` record is written under the closed posture.
Class: 2 (`PARKED`; not executed). The QA/infra executor writes the `PARKED` record (§7.1).
PF anchors: PF19-Canon-Glow-QA-Guide §3.3; PF27-Canon-Plan-Templates ("Step-log header schema expectations (required; v2)", `PARKED`); PF10 Addenda 2.23, 2.25.

Status: `PARKED` before execution, by this Plan (QA-80, 2026-09-27), under QA-70 review v1.1 RL-09. It is intentionally not attempted.

- Reason: the check needs two existing current rows keyed to app users, taken from a Product Owner selection. Before the App no such rows exist that QA may rely on, and QA must not create them. The requirement is blocked by environment, not failed acceptance.
- Authority and controlling source: Glow QA Guide §3.3 (as check 12); decision reference: QA-70 review v1.1, FND-003 and RL-09.
- Affected acceptance claim: AC040-09, live success path (Reader v1 and v2 success bytes over live HTTP on live current rows). The success bytes stay covered in-process with injected rows by check 9, and vendor-backed for Reader v1 by the dumps of check 11; no AC040-09 live-success claim is made.
- Reactivation condition: as check 12.

No commands, inputs or probes. No PO input is requested (§6).

Recording: the QA/infra executor records the check with `record_check` as `PARKED` (§12, `PARKED` records), with a `status_reason` stating the four items above. Primary evidence: `audit/qa/hde-epic040/checks/live-db-reader-success/primary.log` (QA-created; the `PARKED` receipt). Tokens: `[]`, `[]`.

Nonclaims: no live Reader success, no database access, and no claim about live rows.

### CHECK 15 `qa-closeout-deliverables`: Close-out deliverables and coverage

Surface / D-goal mapping: D14; AC040-01 and AC040-08 (evidence integrity of the QA run); PF06 §0.4.1.
Rails: closed posture (§5.2). Pins as above.
Class: 2, local/offline (no vendor); Pre-flight / internal; handled by QA/infra outside the PO's Live QA time (§7.1, §10.1).
PF anchors: PF06-Canon-Change-Process-Guide §0.4.1; PF19-Canon-Glow-QA-Guide §3.4.3, §4.4.3, §9.2.15.5.

Intent: verify the current-state QA evidence family, append QA-discovered doc deltas, write the path proofs, prove that the QA files do not disturb the governed evidence graph, and produce the coverage accounting that QA-120 uses.

PO command(s):

1. Manifest capture ([K]; no evaluator program runs): `sha256sum` of `audit/qa/hde-epic040/qa_step_logs_manifest.json`, of the primary log of every check recorded before this one, and of every supplementary file named in those primary logs, recorded in the body. Kronos verifies the manifest predicates below at QA-110.
2. Doc-delta append: append, below the existing content of both doc-delta surfaces, every `DOC_DELTA:` line recorded in the primary logs of the recorded checks from check 3 on (new IDs from DD-13), keeping both files byte-identical, then `cmp` the two files (expected rc 0). If there is no such line, append the line `No new deltas found during execution.`.
3. Path proofs (before-record set): `_refresh_path_proof(path, default_produced_at=<UTC now>, check=False)` then `check=True` for the primary log of every check recorded before this one, `audit/docdeltas/hde-epic040_doc_deltas.md` and `audit/qa/hde-epic040/00_meta/doc_deltas.md`.
4. Governed-graph non-interference: `python tools/evidence/update_evidence_index.py --check` and `python tools/evidence/validate_evidence_paths.py` (expected rc 0 with the QA files present).
5. Tracked-file observation (attribution only, non-gating): `git status --porcelain`; any tracked file outside the evidence paths of §7.2 that changed is listed for Kronos and is never committed.
6. Coverage accounting written into the body: every check in plan order with status, attempt, evidence pointers and, for non-PASS checks, the blocking precondition and required follow-up.
7. Record this check with `record_check`. Final decisive command: step 4's `validate_evidence_paths.py`.
8. After recording (finalization, outside this primary log): `_refresh_path_proof` with `check=False` then `check=True` for this check's `primary.log` and for `audit/qa/hde-epic040/qa_step_logs_manifest.json`. Kronos verifies at QA-110 that each proof's `sha256` and `size_bytes` match the file.

PASS if ([E]): the step-1 digests are captured; the two doc-delta surfaces are byte-identical after step 2; every path proof of step 3 passes check mode; both step-4 tools exit 0; and the coverage accounting is written.

QA-110 predicates ([K], Kronos from the manifest, the primary logs and supplementary files whose digests step 1 captured, and the body): the manifest holds exactly one entry for each check of §11 recorded before this one, including the two `PARKED` checks; each `log_path` is the concrete primary-log path that the check's block states; each primary log is non-empty, LF-terminated, and starts with a `pf27.step_log_header.v2` header whose `status` equals the manifest status; every supplementary file named in a primary log exists with the recorded SHA-256; the coverage accounting lists every check of §11.

FAIL_BEHAVIOR: not applicable; this check makes no product-behavior claim.

FAIL_TOOLING if a path proof fails check mode, a doc-delta surface differs from its twin, or step 4 fails because of the QA files (an evidence-integration defect for the evidence owner); at QA-110, if the manifest and a primary log disagree or a supplementary file is missing or changed.

TOOLING_BLOCKED if a primary log of a recorded check is missing.

Deliverables (QA-created): `.path_proof.txt` siblings of every recorded check's primary log (checks 1 to 12, 14 and 15), of `audit/qa/hde-epic040/qa_step_logs_manifest.json`, of `audit/docdeltas/hde-epic040_doc_deltas.md` and of `audit/qa/hde-epic040/00_meta/doc_deltas.md`, each at the file's path plus `.path_proof.txt`. Primary evidence: `audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log`. Tokens: `[]`, `[]`.

## 13. Close-out deliverables and final-report criteria

Discovery artifact: `audit/qa/hde-epic040/checks/d0-discovery/primary.log` with the Step-0B surfaces.

QA RCA & Doc Delta summary: produced by Kronos in QA-120 as part of the separate RCA (PF19 §3.1.2; PF06 §0.4.1.2), referencing the governed QA root. It states what ran, what each outcome means, which evidence proves it and whether canon updates are required, maps findings to PF titles as doc-delta intents, and records deferrals as deferrals.

The QA-120 final Report must:

- account for all 14 checks of §11 in plan order (number 13 is removed) with status, attempt lineage and evidence pointers under `audit/qa/hde-epic040/`; mark each COVERED, BLOCKED/UNEXECUTABLE (with blocking precondition, why, whether it blocks closeout, and whether a plan or implementation change is needed), `PARKED` (with its reason, controlling source, affected claim and reactivation condition) or NOT RUN; no step counts as COVERED without a step-scoped pointer (PF19 §9.2.15.5);
- report each check's QA-110 per-task result, including every [K] predicate (§12);
- conclude per criterion AC040-01 to AC040-09 as supported, not supported, or Unknown, with the evidence basis, including the exact-head CI and PR evidence of §10.2; label proof classes (local/offline, in-process, loopback HTTP under the closed posture, vendor-backed);
- report AC040-07's live part and AC040-09's live success path as not supported because they are blocked by environment and deferred (Glow QA Guide §3.3; checks 12 and 14 `PARKED`), not as failures (QA-70 review v1.1 §4);
- report Q-1 and Q-2 outcomes, including exercised versus inferred vendor behavior;
- keep repository-supported completion, canon-drain completion (no claim) and formal close-pack completion (no claim) separate;
- give the later-drain statement of §14 with values updated from the executed evidence;
- give a readiness and closeout recommendation for Isis's CL-E-10 decision, with Unknowns labelled.

The separate RCA must preserve actual failures, corrections, normalizations, Moon Loop and rerun lineage (failure signature, remediation note, rerun output), accepted deviations, causal limits and lessons, and must not invent a failure when all checks pass. Documentation drainage is never a blocker for a step verdict or the recommendation.

## 14. Later-drain statement and PF09 accountability

| Field | Value |
| --- | --- |
| Affected PF canon home(s) | `PF09.3-Canon-HDE-Build-Checklist-Separation` |
| Exact affected locator(s) | Task HDE-SEPA005 "Production Magic10 mechanics configuration contract"; subtasks HDE-SEPA005.1 to HDE-SEPA005.5 (status lines); the phase status summary line for HDE-SEPA005 |
| Current canon posture | HDE-SEPA005 Partial; HDE-SEPA005.1 and HDE-SEPA005.2 Partial; HDE-SEPA005.3 to HDE-SEPA005.5 Not done (as recorded) |
| Supported later-drain action | No status change recommended |
| Drain readiness classification | Not yet supportable from repo evidence |
| Evidence basis | None yet: this Plan's checks are NOT RUN. QA-120 re-evaluates from the executed evidence |
| Epic-close expectation | at epic close |

Check-to-PF09 mapping: HDE-SEPA005.1 and .2 → check 4; HDE-SEPA005.3 → checks 5, 7, 8; HDE-SEPA005.4 → checks 5, 6; HDE-SEPA005.5 → checks 3, 7, 15 and every pytest group. Checks 9, 10 and 11 verify delivered Reader v2, security and vendor behavior inside HDE-EPIC040 scope set by the PF10 Addendum 2.23 overlay; no PF09.3 subtask names Reader v2 exposure, so they map to the HDE-SEPA005 parent with that PF09 gap noted. The `PARKED` checks 12 (live Gate readiness, under HDE-SEPA005.5) and 14 (live Reader success) map to no current proof: they are blocked by environment and deferred (Glow QA Guide §3.3). Check 13 is removed and maps to nothing.

Task-like items this Plan creates, each with exactly one accountability:

| Item | Accountability |
| --- | --- |
| Index and Mirror registration of HDE-EPIC040 QA evidence (QA50-F01) | PF09.3 HDE-SEPA005.5; evidence owner through the whole-change IA PR route |
| `--allow-prod-vendor` gap (DD-04, QA50-B01) | PF09 gap; PF05 and CLI owners through change control; outside HDE-EPIC040 |
| DD-01, DD-02, DD-03, DD-05, DD-06 | Documentation or status drainage only |
| Carried items (DD-07 to DD-12 and QA-10 triage §2) | Their existing records and owners |
| Deferred live Gate readiness against current rows (AC040-07 live part; check 12 `PARKED`) | Out of the current epic, with exact phased PF09 mapping: `PF09.3-Canon-HDE-Build-Checklist-Separation`, Task HDE-SEPA005, Subtask HDE-SEPA005.5 "Separation implementation tests and governed artifacts". Blocked by environment (Glow QA Guide §3.3); reactivated by a future epic that defines user-bound QA surfaces once the App user model exists. No PF09 status claim |
| Deferred live Reader success over HTTP on live rows (AC040-09 live success path; check 14 `PARKED`) | PF09 gap: no PF09.3 subtask names live Reader behavior (the HDE-SEPA005 parent is noted, as for checks 9 to 11). Blocked by environment (Glow QA Guide §3.3); reactivated as the row above. No PF09 status claim |

## 15. Nonclaims

Approving or executing this Plan does not establish QA PASS for the change, acceptance, closure, PF09 status movement, PF-Canon drainage, a PF10 addendum, deployment, release activation, token satisfaction, broad HumanDesignAPI v2 conformance, deployed-service behavior, database population, mapped-cache persistence, a ledger-bound QA manifest or Index/Mirror publication. Check results establish only their stated predicates and proof classes.

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-80-20260927-01
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - prompt: QA-80 — Revise Whole-Change QA Plan — 091426.1; Notion 3db4590a05eb813ba9a9dbd9a641d36c; page as of 2026-09-24T15:55:48.777Z; release GCFPE-20260914.1
  - role_stage: continuing Kronos, QA-80
  - capture_time: 2026-09-27T21:37:48Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_PLAN v1.1, PLAN_PENDING_REVISED, routed to QA-70 (the same continuing Isis); REDLINE_APPLICATION_REPORT v1.0
  - task_and_attempt_mapping: none (QA-80 creates no task; attempt lineage per §7.3)
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md`; owner: the authorized repository writer under that procedure once it is installed)
- usage_id: GCFPE-USE-HDE-EPIC040-QA-50-20260927-01 (shared with the QA Audit; the v1.0 entry, preserved)
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - prompt: QA-50 — Create Whole-Change QA Audit and Plan — 091426.1; Notion 3db4590a05eb81a3ac91f602bad8cfa2; page as of 2026-09-24T15:54:17.481Z; release GCFPE-20260914.1
  - role_stage: continuing Kronos, QA-50
  - capture_time: 2026-09-27T09:26:32Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_PLAN v1.0, PLAN_PENDING, routed to QA-70 (continuing Isis)
  - task_and_attempt_mapping: none yet (QA-90 creates tasks after QA-70 approval)
  - repository_persistence: PENDING / NON_GATING (no installed docs/changes/GCFPE_PROMPT_PROVENANCE.md)
- Other earlier uses, each recorded in its own artifact: GCFPE-USE-HDE-EPIC040-QA-70-20260927-01 (QA Plan Review v1.0, rejected) and GCFPE-USE-HDE-EPIC040-QA-70-20260927-02 (QA Plan Review v1.1); GCFPE-USE-HDE-EPIC040-QA-90-20260927-01 (QA task collection v1.0, not carried forward).

ASK OK?
