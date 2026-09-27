---
artifact_type: QA_PLAN
artifact_id: HDE-EPIC040-QA50-QA-PLAN
artifact_version: "1.0"
predecessor: none (first QA Plan for this change)
state: PLAN_PENDING
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-50 / whole change
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-50 — Create Whole-Change QA Audit and Plan — 091426.1 (Notion 3db4590a05eb81a3ac91f602bad8cfa2; page as of 2026-09-24T15:54:17.481Z)
ecosystem_release: GCFPE-20260914.1 (091426.1)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE)
live_qa_guide: docs/ephemeral/HDE-EPIC040-QA20-live-qa-guide-v1.0.md (GUIDE_READY)
qa_readiness: docs/ephemeral/HDE-EPIC040-QA10-qa-readiness-v1.0.md (READY_FOR_QA)
po_disposition: docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md (Q-1 yes, Q-2 yes)
pf10: docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md (SHA-256 54e660e364c29b9f0d91b6de28ca15efee4ae346f8ecd032833f2e47d8cebf0d; read in full)
planning_basis_revision: a6002d27cd955c814e90661ae2309dc74b190733 (planning basis only; not a PASS predicate)
review_route: QA-70 — Review Whole-Change QA Plan — 091426.1, continuing Isis
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-50
---

# HDE-EPIC040 — Whole-Change Live QA Plan v1.0 (QA-50)

Epic ID: HDE-EPIC040
Plan type: Live QA Plan / Runbook
Execution venue: Codespaces (preferred): GitHub Codespaces for `amthorn78/glow-hdengine-v2` (PF07-Canon-Glow-Infrastructure §2.6–§2.8). Other: a Product Owner-controlled Linux shell that satisfies every `d0-discovery` prerequisite.
Approval sentinel: `ASK OK?`
Venue-specific claim: NOT CLAIMED
Why venue can affect the result: NOT APPLICABLE. Interpreter, dependency and environment posture are fixed and recorded by `d0-discovery`, not by the venue.
Required venue evidence: NOT APPLICABLE
Effect of missing venue evidence: NOT APPLICABLE
Target environment: other: a local QA console running the tested source tree, a loopback HTTP server built from that tree, HumanDesignAPI through `HD_API_BASE_URL` for one PO-only step, and read-only access to the shared database instance for three PO-only steps. No deployed service is a target.
Plan revision: r1 (artifact v1.0)
Date (UTC): 2026-09-27
Operators (names-only): PO (Nathan), Kronos (QA author and evidence reviewer), optional execution agent delegated by the PO for closed-rails checks

"Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates."

No formally approved Product Owner rescope applies to QA. The PO dispositions Q-1 and Q-2 set required QA steps; they are not rescopes.

This Plan executes nothing. Every artifact it lists is NOT RUN until the producing check executes under an approved QA-90 task.

## 1. Canon set

Titles only; exact locators are in the QA Audit §2.

- PF10 — HDE Build Notes. Relevant addenda (v13.3.9 numbering, with headings): 2.2 "Canonize HDE-EPIC040 source-conflict ADR decisions"; 2.3 "Reconcile superseded core-test instructions"; 2.4 "Record in-flight resolution of C040-01 through C040-04"; 2.5 "Record the approved source-backed Channel taxonomy and existing-state conformance"; 2.12 "HDE-EPIC040-PR03-R02 — Bind Executing Mechanics to the Admitted Release"; 2.15 "HDE-EPIC040-PR04-F01 — Truthful Non-Admitted Gate Outcome for the PR04-to-PR06 Interval"; 2.16–2.18 (PR04-F03, F05, F07 Product Owner deferral decisions); 2.19 "HDE-EPIC040-PR04-LINEAGE-001"; 2.20 "HDE-EPIC040-PR05 — PR Work-Unit Lineage Review v1.0"; 2.21 "HDE-EPIC040-PR06-F01 — Frozen-capture identity source for the canonical JSON gate"; 2.22 "HDE-EPIC040-PR06 — PR Work-Unit Lineage Review v1.0"; 2.23 "HDE-EPIC040-PR07-F01 — Add PR06a for Reader v2 Full Magic-10 Exposure and the Deferred Reader Contract Work"; 2.24 "HDE-EPIC040-PR06a — PR Work-Unit Lineage Review v1.0"; 2.25 "HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08)"; 2.26 "HDE-EPIC040-PR06b — PR Work-Unit Lineage Review v1.0"; 2.27 "HDE-EPIC040-OPS01 — OPS_EXECUTION_RESULT v1.4"; 2.28 "HDE-EPIC040 — Change Audit Triage v1.0 (QA-10)".
- PF04 — HDE Governance, §2.0 (acceptance-token roster; this Plan is tokenless).
- PF06 — Change Process Guide, §0.4.1 (D0 Discovery artifact; QA RCA and Doc Delta summary).
- HDE Build Checklist phase document: `PF09.3-Canon-HDE-Build-Checklist-Separation`, Task HDE-SEPA005 "Production Magic10 mechanics configuration contract" and subtasks HDE-SEPA005.1 to HDE-SEPA005.5.
- PF12 — HDE Schemas & Artifacts, §8.3 and §8.6 (Machine Mirror and Evidence Index; follow-up publication only).
- PF19 — Glow QA Guide, §§3.1.2, 3.3, 3.4.3, 3.4.9, 3.4.10, 3.5.7, 3.5.10, 3.6, 4.4.3–4.4.6, 10.6, 10.7, 10.8.
- PF27 — Canon Plan Templates, §A.1 Live QA Plan and Review guardrails.
- PF05 — HDE CLI/API Vendor Ref, §7.1.11, §7.3.9, §7.4.
- PF07 — Glow Infrastructure, §§2.2, 2.4, 2.6–2.8, 7.0, 7.2.1, 8.1, 10.1–10.3.
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
- D9 Q-1 security of the live production Reader route on a loopback server: `sec-reader-http-live`
- D10 Q-2 PF05 §7.3.9 bounded open-rails vendor step: `open-rails-showcompat-vendor`
- D11 AC040-07 live, read-only Gate readiness against current rows: `live-db-gate-readiness`
- D12 AC040-09 live DB Reader refusal path: `live-db-reader-refusal`
- D13 AC040-09 live DB Reader success path (conditional): `live-db-reader-success`
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
| §4.2 security step (Q-1) | `sec-reader-http-live` (live transport), `ac040-09-reader-http-in-process` (admission refusal, CONNECT, QUERY), `live-db-reader-refusal` (real DSN) |
| §4.3 live Gate readiness with non-mutation proof | `live-db-gate-readiness` (before and after row digests) |
| §5 Python 3.12, fresh venv, editable install, closed rails, `DATABASE_URL` only, keys never printed, `adapter.factory:create_app()` | `d0-discovery`; §5.2 environment classes; checks 10, 13, 14 use the factory |
| §6 exact admission | `d0-discovery` admission probe with the manifest audit; tested source recorded |
| §6 wheel installs refuse (O-12) | Editable install from the source tree |
| §6 HTML 404 on the factory (O-P06a-22) | Probe S-26, observed as a known limitation |
| §6 `APP_ENV` asymmetry (O-P07-04) | Probes S-22 to S-25 in production posture; DD-09 |
| §6 `--band` ignored with `--pair-file` (O-P07-02) | Not used by any check |
| §6 `bg:resolve` bypasses the LF guard | `bg:resolve` excluded |
| §7 evidence root, per-step record, status vocabulary, redaction, Index/Mirror only through the updater | §8; Index/Mirror publication is the QA50-F01 follow-up |
| §8 baseline failures and out-of-lane files | `tests/reader_v1/test_cli_proof.py` and non-EPIC040 failures excluded; all 70 EPIC040 test files run in groups A to G |
| §9 permitted and forbidden actions | §2 exclusions; §7 executors and evidence storage |
| §10 recovery | §7.3 to §7.5 |

### 2.2 PF10 overrides and conflicts

- PF10 Addendum 2.23 (C040-07) → Reader v2 is an approved public surface on `POST /api/reader?v=2`, superseding the PF05 statement that the production Reader refuses `v=2` → PF05, PF01, PF04, PF12 (drainage pending).
- PF10 Addendum 2.25 and 2.26 (C040-08) → Reader v1 errors use the four-key `error_v1` envelope → PF01 §2.3, PF04 §8.1.2 (drainage pending).
- PF10 Addendum 2.20 → readiness was proven offline only; this runbook owes the live observation (D11) → PF09.3 HDE-SEPA005.5.
- PF10 Addendum 2.22 → a non-editable wheel refuses admission (O-12); installs are editable from the source tree → packaging.
- PF10 Addendum 2.24 → HTML 404 on unknown non-compat paths is a known limitation (O-P06a-22), observed, not failed; `tests/reader_v1/test_cli_proof.py` is a baseline failure outside scope → PF05 transport.
- PF10 Addenda 2.16–2.18 → the F03, F05 and F07 deferrals were later delivered or bounded by PR06a; dev conjunction evidence capture is not required here.
- PF10 Addendum 2.15 → the non-admitted interval is historical; release 1.3.0 is admitted, so `RELEASE_NOT_ADMITTED` is not an expected outcome at the tested source.
- PF10 Addenda 2.12 and 2.21 → admission and the canonical JSON gate bind to the admitted release and frozen-capture identity; D2 and D4 predicates follow them.
- PF10 Addendum 2.19 and 2.28 → security review did not cover four units (Q-1 → D9); RA-10 requires the open-rails step (Q-2 → D10).
- PF10 Addendum 2.27 → OPS01 is accepted; QA does not re-run it.
- Addenda 2.2–2.5 → C040-01 to C040-06 decisions govern source versions and the Channel taxonomy used by D3.

The single `CANON_CONFLICT_REGISTER` is in the QA Audit §11 (C040-01 to C040-08 carried; C040-09 PROPOSED). Interim treatment of C040-09 in this runbook: read-only git observations for attribution only, never as a PASS gate; no script file is created; existing harness APIs are invoked through embedded `python -c` calls (PF27 "Embedded harness checks").

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

### 5.2 Rails and environment classes

Default rails for this runbook: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`.

Presence of secret-bearing and drift keys is recorded as SET or UNSET only, before any change, in the body of the check's primary log. Values are never printed.

| Class | Used by | Rails and `APP_ENV` | Must be SET | Must be UNSET |
| --- | --- | --- | --- | --- |
| ENV-C (closed, no live services) | `d0-discovery`, `step-0b-doc-delta-capture`, `ac040-08-evidence-validators`, `ac040-02-03-catalog-config`, `ac040-04-05-admission-identity`, `ac040-06-golden-comparison`, `ac040-07-gate-ingress-offline`, `ac040-04-09-compat-cli-offline`, `ac040-09-reader-http-in-process`, `qa-closeout-deliverables` | `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev` | none | `DATABASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV` |
| ENV-S (security server) | `sec-reader-http-live` | server and client `SAFE_MODE=1 ALLOW_NETWORK=0`; server `APP_ENV=prod` (production posture) | `PORT=8000` for the server | as ENV-C |
| ENV-V (vendor step) | `open-rails-showcompat-vendor` | `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev` for this step only | `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` | `HDAPI_BASE_URL`, `DATABASE_URL`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV` |
| ENV-D (live DB, read-only) | `live-db-gate-readiness`, `live-db-reader-refusal`, `live-db-reader-success` | `SAFE_MODE=1 ALLOW_NETWORK=0`; `APP_ENV=dev` for the readiness tool and digest reads; server `APP_ENV=prod` | `DATABASE_URL`; `PORT=8000` for the server | `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV` |

Reasons: closed rails do not gate database access (QA Audit QA50-F03), so ENV-C and ENV-S unset `DATABASE_URL`; local writer routes can insert rows when a DB is reachable (QA50-F09); `HD_API_BASE_URL` is canonical and `HDAPI_BASE_URL` is a deprecated alias (PF07 §2.4, PF19 §3.5.7; QA50-F10); retired bridge keys are drift and are only reported by name (PF07 §7.0).

Pytest runs mirror the CI lane posture (`.github/workflows/ci.yml` L106): ENV-C plus `PYTHONDONTWRITEBYTECODE=1` and `python -m pytest -q -p no:cacheprovider -rs`.

Rails change inside a check (PF27 "Rails posture"): `ac040-07-gate-ingress-offline` command 1 sets `SAFE_MODE=0` for that one command, to prove the readiness tool's own closed-rails refusal; `ALLOW_NETWORK=0` stays and `DATABASE_URL` stays unset, so no live service is reachable; its evidence is the exit code and stderr token in that check's primary log.

Local servers use the PF07 §10.1 declaration with `PORT=8000`: `python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:8000 --workers 2 --threads 4 --timeout 30`. Clients use `http://127.0.0.1:8000` (PF07 §2.2).

### 5.3 VCS and source identity

No check performs a VCS mutation. `d0-discovery` records the tested source read-only (`git rev-parse HEAD`, `git status --porcelain` line count) for attribution only (PF19 §3.4.9). Neither value, a branch name nor working-tree noise is a PASS or FAIL predicate. The tested source is expected to be the planning basis or a later commit; Kronos assesses any substantive difference under PF19 §10.8. Evidence storage is a separate lane (§7).

## 6. PO inputs needed

Names only; no value is stored in this Plan.

| Input | Needed by | Source | If missing at runtime |
| --- | --- | --- | --- |
| `DATABASE_URL` | D11, D12, D13 | PF07 §8.1 QA (GitHub Codespaces) binding, supplied by the PO in the shell | Affected check `TOOLING_BLOCKED` |
| `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` | D10 | PF07 §2.4, §2.7 | D10 `TOOLING_BLOCKED` |
| Birth tuples A and B (synthetic, not a real person's data) | D10 | Default: A = (`1999-10-16`, `04:37`, `Santiago, Chile`), B = (`1978-06-17`, `02:35`, `Tallinn, Estonia`) from `audit/ops/hde-epic030/ops-02/vendor_command.txt` (Audit-proven L-51), unless the PO names other synthetic tuples in the QA-90 task | D10 `TOOLING_BLOCKED` |
| Readiness selection file: canonical lowercase UUIDs, one per line, of rows the PO expects in `public.hde_body_graphs_current`; kept outside the repository and never committed | D11, D13 | Product Owner | D11 and D13 `TOOLING_BLOCKED` |
| `PORT=8000` | D9, D12, D13 | PF07 §2.4 | Server not started; affected check `TOOLING_BLOCKED` |
| Delegation record naming an execution agent for the ENV-C and ENV-S checks (optional) | D0–D9, D14 | QA-90 task | The PO executes them |
| Evidence branch name | Evidence storage (§7) | QA-90 task | Evidence stays uncommitted until named |

## 7. Executors, authority, evidence storage, rerun and recovery

### 7.1 Authorized environment executor

- Nathan (Product Owner) is the authorized environment executor for every check, in one QA console checkout, so that one QA root and one manifest hold the complete current-state evidence.
- The PO may delegate the ENV-C and ENV-S checks (`d0-discovery` through `sec-reader-http-live`, and `qa-closeout-deliverables`) to one named repository-capable execution agent working in that same checkout, recorded in the QA-90 task (PF19 §3.3). Capability alone grants no authority.
- `open-rails-showcompat-vendor`, `live-db-gate-readiness`, `live-db-reader-refusal` and `live-db-reader-success` are PO-only and Kronos-guided (PF19 §3.3, §3.5.7). No automated agent executes a vendor call, handles a plaintext secret or connects to the shared database.
- Kronos designs the tasks through QA-90, reviews evidence at QA-110 and reports at QA-120. Kronos does not execute checks. Isis reviews this Plan at QA-70 and owns closure.

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

### 7.4 Moon Loop (bounded)

A Moon Loop may correct only QA-created evidence-assembly defects inside `audit/qa/hde-epic040/` or `audit/docdeltas/hde-epic040_doc_deltas.md` (header, manifest, path proof, doc-delta assembly, a QA-created input file such as `tmp_goldens_altered.json`, or evaluator code carried in the primary log) when the proof target, rails, evidence identity and predicates are unchanged. It preserves the failure signature, records the change and why under `audit/qa/hde-epic040/00_meta/delta/` (PF27 Step-0B), and reruns the affected check in the same evidence stream. It never touches product, test, tool, generator, governed evidence outside the QA root or PF files, and never resets attempts.

### 7.5 Cleanup and recovery

- Stop every local server a check starts, and confirm port 8000 is closed before the next server check.
- Unset `DATABASE_URL`, `HD_API_KEY`, `GEO_API_KEY` and `HD_API_BASE_URL` from the shell after each PO-only check.
- Temporary files outside the repository (venv, selection file, comparator report before copy) stay outside the repository and are not committed.
- A secret value found in any evidence file: quarantine the file outside the repository, do not commit it, classify the check `FAIL_TOOLING`, and route through §7.3.
- No database state is changed by this Plan, so no database rollback exists. If a live-DB non-mutation predicate fails, stop the live-DB checks and report to Kronos.

## 8. Evidence posture and directory structure

- QA root: `audit/qa/hde-epic040/` (Canon-defined pattern, PF07 §2.8, PF19 §3.4.3). Absent at planning; `d0-discovery` records that before creating it.
- One current-state primary log per check, named `primary.log` in that check's own directory under `audit/qa/hde-epic040/checks/`; each check block states its concrete path. No run directories, no run identifiers, no pointer files.
- Manifest: `audit/qa/hde-epic040/qa_step_logs_manifest.json` (Canon-defined), a flat object keyed by `check_id` with `check_id`, `log_path` (full repository-relative path) and `status`, maintained by `record_check`. `TOOLING_BLOCKED` and `PARKED` checks are listed too.
- Path proofs (PF19 §3.4.3): `audit/qa/hde-epic040/qa_step_logs_manifest.json.path_proof.txt`, one `primary.log.path_proof.txt` beside each primary log, and one beside each doc-delta surface, written by `qa-closeout-deliverables`.
- Recording mechanism (Audit-proven L-41, L-42): `tools.qa.qa_harness.record_check` with `HarnessConfig("HDE-EPIC040", repo_root)` (the checkout root as a `pathlib.Path`) and one `CheckResult` carrying the fields listed in the QA Audit L-41. Pytest-only checks may build their `CheckResult` with `run_pytest_check`. Multi-command checks build one `CheckResult` whose `command` lists every executed argv in order.
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
| DD-02 | CAVEAT | PF07 §2.8 forbids git operations and QA-time scripts; PF19 §3.4.9 and PF27 permit read-only observations and embedded harness calls (C040-09, PROPOSED) | PF07-Canon-Glow-Infrastructure §2.8 | PF07 maintainer |
| DD-03 | CAVEAT | PF19 §§3.4.3, 3.6, 10.8 and AGENTS.md name ChatGPT Library or Google Drive for authored plans and canon; D7 and the QA prompts use `docs/ephemeral/` and `docs/pfcanon/` (QA50-F13) | PF19-Canon-Glow-QA-Guide §§3.4.3, 3.6, 10.8; AGENTS.md | PF19 maintainer; repository docs owner |
| DD-04 | CAVEAT | PF05 §7.1.11 `--allow-prod-vendor` is not implemented (QA50-B01) | PF05-Canon-HDE-CLI-API-Vendor-Ref §7.1.11 | PF05 and CLI owners |
| DD-05 | CAVEAT | AGENTS.md cites "PF10 §2.8" for the bounded PF-copy rule; its v13.3.9 home is PF19 §10.8 (QA50-F12) | AGENTS.md | Repository docs owner |
| DD-06 | CAVEAT | Guide §8 names `6e4b3a1` as the attestation candidate; the attestation binds `6f53d82` (QA50-F11) | None (ephemeral record) | Isis |
| DD-07 | CAVEAT, carried | C040-05 to C040-08 drainage pending (RA-18) | Per register, QA Audit §11 | Named maintainers |
| DD-08 | CAVEAT, carried | `showcompat` help says Reader v1 (O-P07-01) | Repository CLI help | Whole-change IA |
| DD-09 | CAVEAT, carried | `APP_ENV` asymmetry between dev `GET /reader` and conjunction routes (O-P07-04, RA-06) | O-P07-04 record | Whole-change IA |
| DD-10 | CAVEAT, carried | `ci/checks/check_mirror_schema.sh` is Python; AGENTS.md invocation (RA-13) | AGENTS.md | Repository docs owner |
| DD-11 | CAVEAT, carried | `docs/ADAPTER_009.md:174` says `body_not_allowed`; code emits `invalid_json` (FND-017) | `docs/ADAPTER_009.md` | Compat docs owner |
| DD-12 | CAVEAT, carried | PF10 v13.3.9 §2.28 line references to §2.19 and §2.20 are off by two | PF10-HDE-Build-Notes §2.28 | PF10 drain owner |

Every row states `Drives decision: No`. Documentation drainage is never a blocker, a check predicate or a deliverable of this Plan.

## 10. Runbook Check Matrix

Executor codes: E = PO or a PO-delegated execution agent in the same checkout; P = PO only. All tokens: none (`[]`). The primary evidence column gives each concrete primary-log path.

| # | check_id | check_name | D-goal | Rails | Commands and executor | Expected result | Primary evidence | Deliverables | Tokens | PF anchors |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` | Discovery and tooling bootstrap | D0 | ENV-C | E: identity, venv, install, readiness, help, harness, admission | PASS when every prerequisite holds | `audit/qa/hde-epic040/checks/d0-discovery/primary.log` | primary log; manifest | none | PF06 §0.4.1.1; PF19 §3.6 |
| 2 | `step-0b-doc-delta-capture` | Step-0B doc-delta capture | D1 | ENV-C | E: write both doc-delta surfaces | PASS when both surfaces are identical and complete | `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log` | two doc-delta files | none | PF27 Step-0B |
| 3 | `ac040-08-evidence-validators` | Owner evidence coherence and evidence tests | D2 | ENV-C | E: nine read-only validators, pytest group G | PASS when all exit 0 | `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log` | primary log | none | PF12 §8.3; PF19 §2.2.11 |
| 4 | `ac040-02-03-catalog-config` | Catalog, configuration and schemas | D3 | ENV-C | E: structural probe, pytest group A | PASS when probe and tests pass | `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log` | primary log | none | PF09.3 HDE-SEPA005.1, .2 |
| 5 | `ac040-04-05-admission-identity` | Admission, pure core and release identity | D4 | ENV-C | E: manifest audit, OPS01 ledger, binding, pytest group B | PASS when all hold | `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log` | primary log | none | PF09.3 HDE-SEPA005.3, .4 |
| 6 | `ac040-06-golden-comparison` | Read-only golden comparison | D5 | ENV-C | E: compare twice, deliberate mismatch, tree digests, pytest group C | PASS when match, mismatch and non-mutation hold | `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log` | four supplementary files | none | PF09.3 HDE-SEPA005.4 |
| 7 | `ac040-07-gate-ingress-offline` | Gate ingress and readiness, offline | D6 | ENV-C | E: four readiness refusals, pytest group D | PASS when refusals and tests hold | `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log` | primary log | none | PF09.3 HDE-SEPA005.3, .5 |
| 8 | `ac040-04-09-compat-cli-offline` | Compat and CLI, local/offline | D7 | ENV-C | E: pytest group E | PASS when rc 0 | `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log` | primary log | none | PF19 §3.3 |
| 9 | `ac040-09-reader-http-in-process` | Reader, HTTP and transport, in-process | D8 | ENV-C | E: pytest group F | PASS when rc 0 | `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log` | primary log | none | PF05 §5 via PF10 2.23, 2.25 |
| 10 | `sec-reader-http-live` | Security of the live production Reader route | D9 | ENV-S | E: loopback server, 26 probes, evaluator | PASS when every probe predicate holds | `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log` | `http_probes.jsonl`; `gunicorn_server.log` | none | PF19 §3.2, §3.5.10 |
| 11 | `open-rails-showcompat-vendor` | Bounded open-rails vendor step | D10 | ENV-V | P: two vendor-backed runs (AB, BA), evaluator | PASS per §12 block | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log` | five vendor files | none | PF05 §7.3.9; PF19 §3.3, §3.5.7 |
| 12 | `live-db-gate-readiness` | Live read-only Gate readiness | D11 | ENV-D | P: digests, readiness tool, digests, evaluator | PASS per §12 block | `audit/qa/hde-epic040/checks/live-db-gate-readiness/primary.log` | `readiness_report.json` | none | PF10 2.20; PF09.3 HDE-SEPA005.5 |
| 13 | `live-db-reader-refusal` | Live DB Reader refusal path | D12 | ENV-D | P: loopback server, 3 probes, secret scan | PASS per §12 block | `audit/qa/hde-epic040/checks/live-db-reader-refusal/primary.log` | `http_probes.jsonl`; `gunicorn_server.log` | none | PF19 §3.5.10 |
| 14 | `live-db-reader-success` | Live DB Reader success path (conditional) | D13 | ENV-D | P: loopback server, 6 probes, digests | PASS per §12 block, or `TOOLING_BLOCKED` when its condition is unmet | `audit/qa/hde-epic040/checks/live-db-reader-success/primary.log` | `http_probes.jsonl`; `gunicorn_server.log` | none | PF10 2.23 |
| 15 | `qa-closeout-deliverables` | Close-out deliverables and coverage | D14 | ENV-C | E: verify manifest, append doc deltas, path proofs, updater checks | PASS per §12 block | `audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log` | path proofs | none | PF06 §0.4.1; PF19 §9.2.15.5 |

## 11. Collection, dependencies and order

The collection is exactly the 15 checks above, in the order listed. Counts: 15 checks; 11 executor class E, 4 executor class P; 1 conditional (`live-db-reader-success`); 0 PARKED at plan time; all NOT RUN.

| Check | Depends on (must be PASS) | Notes |
| --- | --- | --- |
| `d0-discovery` | none | Gates every other check |
| `step-0b-doc-delta-capture` | `d0-discovery` executed (any status) | Records D0 blockers too |
| Checks 3 to 9 | `d0-discovery` | Independent of each other; run in the listed order |
| `sec-reader-http-live` | `d0-discovery`, `ac040-09-reader-http-in-process` | The in-process check carries CONNECT, QUERY and admission-refusal coverage |
| `open-rails-showcompat-vendor` | `d0-discovery`, `ac040-04-09-compat-cli-offline` | Accepted local implementation proof (PF19 §3.3) |
| `live-db-gate-readiness` | `d0-discovery`, `ac040-07-gate-ingress-offline` | |
| `live-db-reader-refusal` | `d0-discovery`, `sec-reader-http-live` | |
| `live-db-reader-success` | `live-db-gate-readiness` PASS with `readiness` `READY` and `requested` at least 2; `live-db-reader-refusal` | Otherwise `TOOLING_BLOCKED` |
| `qa-closeout-deliverables` | every other check recorded (any status) | Runs last |

A dependency that is not PASS makes the dependent check `TOOLING_BLOCKED` with the dependency named, without executing its behavior commands. It is still recorded in the manifest.

Reference counts from the QA Audit §4.4 (70 files, 2,090 tests, collected at the planning basis) are informational. A different count at the tested source is recorded and explained, not failed by itself.

## 12. Check Blocks

Common rules for every check:

- Dependency posture: each check re-runs a step-local readiness line before its behavior commands: `python --version` reports 3.12, `python -c "import tools.qa.qa_harness, engine"` exits 0, and the environment class of §5.2 is applied and recorded. If that readiness fails, the check is `TOOLING_BLOCKED` (or `FAIL_TOOLING` if the harness itself malfunctions after a good install).
- Syntax in this Plan is operational, not literal. The executor may normalize syntax without changing the proof target, rails, evidence identity or predicates, and records the exact command and the normalization in `command_provenance` (PF19 §3.4.10).
- Every command runs from the repository root. Exit codes are captured from the producer itself (`out=$(cmd); rc=$?` or the harness), never through a pipe that replaces the status.
- Every primary log is written through `record_check` (§8). The evaluator code of a check, where one is used, is written verbatim into that check's primary log.
- A check that writes supplementary files creates its own check directory (`mkdir -p`) before its first write.
- Markers in primary-log bodies: a prerequisite gap found by `d0-discovery` is written as a line starting `BLOCKER:`; a documentation mismatch observed by any check is written as a line starting `DOC_DELTA:`. Step-0B and `qa-closeout-deliverables` collect those lines mechanically.
- Non-empty capture rule (PF27, PF19 §4.4.4): if a server log is empty when its server stops, the executor writes the single line `no server output` into it; no governed file is left empty.
- Nonclaims for every check: no QA PASS for the change, acceptance, closure, PF09 status change, deployment, token, new public route or flag, or PF edit follows from a check result.

### CHECK 1 `d0-discovery`: Discovery and tooling bootstrap

Surface / D-goal mapping: D0; all ACs (prerequisite).
Rails: ENV-C. Pins: `LC_ALL=C LANG=C TZ=UTC`.
PF anchors: PF06-Canon-Change-Process-Guide §0.4.1.1; PF19-Canon-Glow-QA-Guide §3.6, §3.4.9.

Intent: establish and record, before any behavior check, the tested source, interpreter, dependencies, harness, CLI and tool entrypoints, rails, environment presence and admission of the actual checkout; record the initial absence of the QA root.

PO command(s), in order:

1. Initial absence: `test -e audit/qa/hde-epic040` (expected: absent at attempt 1). Capture the result before anything is written.
2. Environment presence: record SET or UNSET for `DATABASE_URL`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV`, `PORT`; values of `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`. Then apply ENV-C.
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
Rails: ENV-C. Pins as above.
PF anchors: PF27-Canon-Plan-Templates (Mandatory Step-0 artifacts, Step-0B); PF19-Canon-Glow-QA-Guide §3.4.3.

Intent: mechanically record the doc deltas of §9.1 and any `d0-discovery` BLOCKER on both doc-delta surfaces.

PO command(s):

1. Preflight: `test -e audit/docdeltas/hde-epic040_doc_deltas.md` and `test -e audit/qa/hde-epic040/00_meta/doc_deltas.md` (expected: both absent). If either exists, do not overwrite it; record its SHA-256 and stop with `FAIL_TOOLING` for Moon Loop handling.
2. One embedded `python -c` writer that renders the §9.1 table rows, plus every `BLOCKER:` line read from the `d0-discovery` primary log, into UTF-8 Markdown without BOM, LF-terminated: a title line naming HDE-EPIC040 and this Plan, a `## BLOCKERS` section (IDs, or the line `none`), and a `## CAVEATS` section with one row per DD ID (ID, class, delta, drain target, owner, `Drives decision: No`). The same bytes are written to both paths, creating `audit/qa/hde-epic040/00_meta/` if needed.
3. Verification (final decisive command): `cmp audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md`, plus SHA-256 of both.

PASS if: both files exist, are non-empty, LF-terminated, without BOM and byte-identical; each of DD-01 to DD-12 appears exactly once; both sections are present; every `d0-discovery` BLOCKER appears under BLOCKERS.

FAIL_TOOLING if the files differ, are empty, miss a row, or existing content would be overwritten.

TOOLING_BLOCKED if `d0-discovery` produced no primary log.

Deliverables (QA-created): `audit/docdeltas/hde-epic040_doc_deltas.md` (draft or staging surface) and `audit/qa/hde-epic040/00_meta/doc_deltas.md` (authoritative epic capture), both Canon-defined surfaces of PF27 Step-0B. Primary evidence: `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log`. Tokens: `[]`, `[]`.

### CHECK 3 `ac040-08-evidence-validators`: Owner evidence coherence and evidence tests

Surface / D-goal mapping: D2; AC040-08; K040-REQ-012.
Rails: ENV-C. Pins as above.
PF anchors: PF12-Canon-HDE-Schemas-and-Artifacts §8.3, §8.6; PF19-Canon-Glow-QA-Guide §2.2.7, §2.2.11.

Intent: re-verify, read-only, that the owner-generated evidence graph and governed families are coherent at the tested source, and run the evidence and QA-tooling test group.

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

TOOLING_BLOCKED if `d0-discovery` is not PASS, an entrypoint is missing, or pytest collects no test (rc 5).

Primary evidence: `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log`. No other file. Tokens: `[]`, `[]`.

### CHECK 4 `ac040-02-03-catalog-config`: Catalog, configuration and schemas

Surface / D-goal mapping: D3; AC040-02, AC040-03; K040-REQ-003 to K040-REQ-006; PF09.3 HDE-SEPA005.1, HDE-SEPA005.2.
Rails: ENV-C. Pins as above.
PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.1, .2); PF10 Addendum 2.5 (Channel taxonomy).

Intent: prove the delivered catalog and mechanics configuration have the approved structure, and run the catalog, configuration and schema test group (mutation matrix, negative cases, bundle compatibility).

PO command(s):

1. Structural probe (embedded `python -c`, read-only JSON parse) over the actual files (Audit-proven L-53, L-54).
2. Pytest group A (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/config/test_registry_catalog_contract.py tests/config/test_magic10_contracts.py tests/config/test_manifest_schema.py tests/config/test_typed_bundles.py tests/config/test_alias_policy_enforcement.py tests/config/test_config_loader_unknown_ids_fail_closed.py tests/config/test_registry_report.py tests/config/test_registry_report_determinism.py tests/config/test_registry_report_indexing.py tests/compare/test_arrays_as_sets.py tests/m10/test_defs_order.py tests/m10/test_thresholds_rounding.py`

PASS if:

- `catalog/channels_v1.json` has key `channels` with 36 rows; each row has exactly the keys `centers`, `circuit_primary`, `domains`, `flags`, `gates`, `id`, `primary_domain`, `substream`; every `gates` pair is ascending; the 36 pairs are unique; no value is null;
- `catalog/magic10_mechanics_v1.json` has `config_id` `m10-channel-state-v1.0.0`, `schema` `magic10_mechanics_config.v1`, 20 `signals` with unique `signal_id`, 3 `profiles` (`activation_bp_v1`, `coherence_bp_v1`, `expression_bp_v1`), 10 `category_weights`; `equilibrium_score` uses `twice_min_owner_mass_v1`, `counterweight_ratio` uses `companionship_em_mass_v1`, the other 18 use `weighted_state_sum_v1`;
- the pytest run exits 0.

FAIL_BEHAVIOR if a structural predicate is false or a test fails.

FAIL_TOOLING if the probe or pytest malfunctions.

TOOLING_BLOCKED if `d0-discovery` is not PASS or a listed file is missing.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log`. Tokens: `[]`, `[]`.

### CHECK 5 `ac040-04-05-admission-identity`: Admission, pure core and release identity

Surface / D-goal mapping: D4; AC040-04, AC040-05; K040-REQ-007 to K040-REQ-009; PF09.3 HDE-SEPA005.3, HDE-SEPA005.4.
Rails: ENV-C. Pins as above.
PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.3, .4); PF10 Addenda 2.12, 2.22, 2.27.

Intent: prove that the complete release is intact and bound to the accepted OPS01 attestation, and run the admission, refusal-class, pure-core, determinism and identity test group.

PO command(s):

1. `python scripts/release_id_recompute.py --check-manifest-only` (expected rc 0; audits the bytes and size of all 45 members). Never run this script in any other mode.
2. `sha256sum catalog/manifest.json`.
3. `(cd audit/ops/hde-epic040/ops01 && sha256sum -c SHA256SUMS)` (expected 7 lines OK, rc 0; read-only).
4. Binding (embedded `python -c`): `attestation.json` fields `release_id` and `manifest_sha256` equal the step-2 digest; record `source_commit`, `validation_result`, `release_admission`.
5. Pytest group B (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/config/test_production_admission.py tests/config/test_execution_coherence.py tests/core/test_engine_core_purity.py tests/core/test_engine_core_determinism.py tests/core/test_engine_core_abba.py tests/m10/test_m10_symmetry_identity.py tests/runtime/test_identity.py tests/scripts/test_cut_release_manifest.py tests/reader_v1/test_release_pack.py`

PASS if steps 1, 3 and 5 exit 0, step 4 finds both equalities, and `validation_result` is `PASS` with `release_admission` `PR06R_B_FINAL_PASS`.

FAIL_BEHAVIOR if step 1 reports a `MANIFEST_ERROR` on the tested source, the binding fails, or a test fails.

FAIL_TOOLING if a command crashes or pytest exits 2, 3, 4 or negative.

TOOLING_BLOCKED if `d0-discovery` is not PASS or an OPS01 file is missing.

Limits: OPS01 evidence is corroboration, not QA evidence; the attestation is not rebuilt. Primary evidence: `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log`. Tokens: `[]`, `[]`.

### CHECK 6 `ac040-06-golden-comparison`: Read-only golden comparison

Surface / D-goal mapping: D5; AC040-06; K040-REQ-010; PF09.3 HDE-SEPA005.4.
Rails: ENV-C. Pins as above.
PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.4); PF10 Addendum 2.20; PF01-Canon-HDE-Math-Spec §9.5.

Intent: prove that the complete eight-case collection matches at the repository root through the canonical code, that the result repeats byte for byte, that a deliberate expected-value change is reported as a mismatch, and that nothing in the checkout changes.

PO command(s):

1. Before-digest: SHA-256 over the sorted list of `path` and file SHA-256 for every regular file under the repository root, excluding `.git/`, `audit/qa/hde-epic040/`, `__pycache__/` and `.pytest_cache/`.
2. Match run 1: `python tools/config/generate_config_artifacts.py --compare-goldens .` with stdout saved to `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json` (expected rc 0).
3. Match run 2: the same command, stdout to `compare_match_run2.json` in the same directory (expected rc 0).
4. Altered input (embedded `python -c`): load `tests/fixtures/magic10/v1/goldens.json`, change only case `M10-G001` `expected.signals[0].q` from `0` to `1`, and write `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json`. Record the SHA-256 of both files and the one changed leaf.
5. Mismatch run: `python tools/config/generate_config_artifacts.py --compare-goldens . --goldens audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json --report <a new path in a temporary directory outside the repository>` (expected rc 1, stderr `GOLDEN_COMPARISON_MISMATCH:<n>`). Copy the report to `compare_mismatch_report.json` in the check directory and record both SHA-256 values.
6. After-digest as in step 1, taken before any test runs so that only the comparator runs fall between the two digests.
7. Pytest group C: `python -m pytest -q -p no:cacheprovider -rs tests/config/test_config_artifacts.py`.
8. Evaluator (final decisive command, embedded `python -c`): checks every predicate below over the captured files and exits 0 only if all hold.

Never run the comparator script without `--compare-goldens` or `--check` (write paths; QA Audit L-07).

PASS if:

- runs 1 and 2 exit 0; both reports have `ok` true, empty `mismatches`, `cases` listing exactly `M10-G001` to `M10-G008` each with `outcome` `match`, `config_id` `m10-channel-state-v1.0.0` and `candidate_release_id` equal to the manifest SHA-256; the two report files are byte-identical;
- the mismatch run exits 1 with `GOLDEN_COMPARISON_MISMATCH:<n>` and n at least 2; its report has `ok` false; every mismatch row has `case_id` `M10-G001`; one row has `path` `transcription.expected`; cases `M10-G002` to `M10-G008` have `outcome` `match`;
- the pytest run exits 0;
- the before and after digests are equal.

FAIL_BEHAVIOR if the root comparison mismatches or refuses on the tested source, the altered collection is reported as a match, runs 1 and 2 differ, the mismatch names another case, the digests differ, or a test fails.

FAIL_TOOLING if the altered file is refused with `GOLDENS_INVALID` (a QA input defect; Moon Loop eligible), the report copy differs, or the evaluator malfunctions.

TOOLING_BLOCKED if `d0-discovery` is not PASS, or a run refuses with `RAILS_CLOSED_REQUIRED` (environment) or with an admission refusal that `--check-manifest-only` attributes to modified members.

Deliverables (QA-created, in `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/`): `compare_match_run1.json`, `compare_match_run2.json`, `tmp_goldens_altered.json`, `compare_mismatch_report.json`. Primary evidence: `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log`. Tokens: `[]`, `[]`.

### CHECK 7 `ac040-07-gate-ingress-offline`: Gate ingress and readiness, offline

Surface / D-goal mapping: D6; AC040-07 (offline part); K040-REQ-007, K040-REQ-011; PF09.3 HDE-SEPA005.3, HDE-SEPA005.5.
Rails: ENV-C (no `DATABASE_URL`). Pins as above.
PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.3, .5); PF10 Addendum 2.20.

Intent: run the Gate normalization and rejection corpus and the readiness tool's tests, and prove the readiness command's typed refusals at runtime without a database, including that an unavailable dataset is never reported ready.

PO command(s) (readiness command Audit-proven L-09):

1. Open-pin refusal: the readiness command with `--user-id 00000000-0000-0000-0000-000000000001` under `SAFE_MODE=0` for this command only (expected rc 5, stderr starts `RAILS_CLOSED_REQUIRED:`).
2. Empty selection: `--selection-file` pointing to an empty file created outside the repository (expected rc 5, `READINESS_EMPTY_SELECTION`).
3. Invalid selection: `--user-id 00000000-0000-0000-0000-00000000000G` (expected rc 5, `READINESS_SELECTION_INVALID`).
4. Unavailable dataset: `--user-id 00000000-0000-0000-0000-000000000001` under ENV-C with `DATABASE_URL` unset (expected rc 5, `READINESS_UNAVAILABLE`; no report on stdout).
5. Pytest group D (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/bodygraph/test_gates.py tests/bodygraph/test_projection_gate_ingress.py tests/bodygraph/test_resolve_compat_chart.py tests/bodygraph/test_check_magic10_gate_readiness.py`

PASS if commands 1 to 4 return the stated exit code and token with empty stdout, and the pytest run exits 0.

FAIL_BEHAVIOR if a refusal is missing or wrong, any command emits a READY report, or a test fails.

FAIL_TOOLING if a command crashes with a traceback or pytest malfunctions.

TOOLING_BLOCKED if `d0-discovery` is not PASS.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log`. Tokens: `[]`, `[]`.

### CHECK 8 `ac040-04-09-compat-cli-offline`: Compat and CLI, local/offline

Surface / D-goal mapping: D7; AC040-04 (application boundary), AC040-09; K040-REQ-004, K040-REQ-008.
Rails: ENV-C. Pins as above.
PF anchors: PF19-Canon-Glow-QA-Guide §3.3 (local/offline label).

Intent: run the eligibility, no-user boundary, AB/BA identity, CLI source, error parity, canonical-bytes and file-input tests. Proof class: local/offline (no vendor); it does not prove live vendor behavior.

PO command(s): pytest group E (final decisive command), recordable with `run_pytest_check`: `python -m pytest -q -p no:cacheprovider -rs tests/compat/test_evaluate_pair_eligibility.py tests/compat/test_conjunction_no_user_boundary.py tests/compat/test_compat_public_ab_ba_identity.py tests/compat/test_compat_public_lf_bom.py tests/compat/test_abba_parity.py tests/compat/test_hde_epic037_v2_adapter_to_compat.py tests/cli/test_showcompat_sources.py tests/cli/test_errors_parity.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_cli_file_inputs.py tests/cli/test_showcompat_parity_and_identity.py tests/artifacts/test_cli_text_artifacts_bom_lf.py tests/qa/test_cli_admin_dumps.py tests/qa/test_cli_admin_parity.py tests/runtime/test_emit_public_legacy_helper.py tests/epic003/test_meta_invocation_ok.py`

PASS if rc 0. FAIL_BEHAVIOR if rc 1. FAIL_TOOLING if rc 2, 3, 4 or negative. TOOLING_BLOCKED if rc 5, a file is missing, or `d0-discovery` is not PASS.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log`. Tokens: `[]`, `[]`.

### CHECK 9 `ac040-09-reader-http-in-process`: Reader, HTTP and transport, in-process

Surface / D-goal mapping: D8; AC040-09; Reader v1 and v2 contracts (PF10 Addenda 2.23, 2.25).
Rails: ENV-C. Pins as above.
PF anchors: PF05-Canon-HDE-CLI-API-Vendor-Ref §5 as overridden by PF10 Addenda 2.23 and 2.25; PF19-Canon-Glow-QA-Guide §3.2.

Intent: run the Reader v1 and v2 route tests (success, eligibility, refusal classes, admission refusal as 503 `ERR_M10_MANIFEST_MISMATCH`, every non-POST method including CONNECT and QUERY on all three factories), the emitter and schema tests, transport proofs and keys-only logging tests. Proof class: in-process Flask test client with injected current rows; it is not live transport and not a live database.

PO command(s): pytest group F (final decisive command), recordable with `run_pytest_check`: `python -m pytest -q -p no:cacheprovider -rs tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py tests/http/test_compat_endpoint_contract.py tests/http/test_dev_conjunction_http.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py tests/adapter/test_compat_writer_transport.py tests/reader_v1/test_emitter.py tests/reader_v1/test_goldens.py tests/reader_v1/test_schema.py tests/transport/test_a7_transport_proofs.py tests/compliance/test_log_shape_snapshot.py tests/compliance/test_logging_filter_keys_only_and_redactions.py`

PASS if rc 0. FAIL_BEHAVIOR if rc 1. FAIL_TOOLING if rc 2, 3, 4 or negative. TOOLING_BLOCKED if rc 5, a file is missing, or `d0-discovery` is not PASS.

Primary evidence: `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log`. Tokens: `[]`, `[]`.

### CHECK 10 `sec-reader-http-live`: Security of the live production Reader route

Surface / D-goal mapping: D9; PO Q-1; AC040-09; K040-REQ-008, K040-REQ-013.
Rails: ENV-S (server `APP_ENV=prod`, closed rails, no `DATABASE_URL`, no vendor keys). Pins as above.
PF anchors: PF19-Canon-Glow-QA-Guide §3.2, §3.5.10; PF10 Addenda 2.19, 2.23, 2.24, 2.25.

Intent: over real HTTP against the production factory `adapter.factory:create_app()`, prove that every request-shape, version, size and method refusal on `POST /api/reader` returns its governed envelope and headers, that dev routes refuse in production posture, and that no public response carries a secret, stack trace, Gate payload or internal diagnostic. Admission-refusal propagation and CONNECT/QUERY coverage come from check 9 (in-process) and are cited, not repeated.

Discovery step: none needed; routes and envelopes are Audit-proven (L-20 to L-28).

PO command(s):

1. Start the server (§5.2 declaration) in the background with stdout and stderr to `audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log`. Service readiness: poll `GET http://127.0.0.1:8000/internal/version` until HTTP 200, at most 30 seconds.
2. Send probes S-01 to S-26 with `curl`, capturing for each the status, header lines (names lower-cased, values verbatim) and body separately from curl's stderr, and append one JSON object per probe to `audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl` with keys `probe_id`, `method`, `target`, `request_body_bytes`, `request_body_sha256`, `status`, `headers`, `body`.
3. Stop the server and confirm port 8000 is closed.
4. Evaluator (final decisive command, embedded `python -c`) over `http_probes.jsonl`.

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
| S-22 | `GET /reader?v=1&a=x&b=y` | 403 `ERR_READER_FORBIDDEN` |
| S-23 | `GET /dev/reader/conjunction` | 403 `ERR_WRITER_FORBIDDEN` |
| S-24 | `GET /dev/sampler/conjunction` | 403 `ERR_WRITER_FORBIDDEN` |
| S-25 | `GET /dev/writer/conjunction` | 403 `ERR_WRITER_FORBIDDEN` |
| S-26 | `GET /api/reader/missing` | 404 HTML (known limitation O-P06a-22; observed, not failed) |

PASS if:

- the server became ready and every probe was captured;
- each probe returns its expected status and code;
- every JSON response from S-02 to S-25 has `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store` and no `ETag`; every Reader error body from S-02 to S-22 (all except the bodiless HEAD probe) has exactly the keys `code`, `error`, `ok` (false) and `schema` (`"v1"`), is canonical and ends with exactly one LF;
- no response body or header from S-01 to S-26 contains `Traceback`, `File "`, `psycopg`, `postgresql`, a `gates` key, or a JSON number in any Reader error body.

FAIL_BEHAVIOR if the server is reachable and a probe contradicts its expected status, code, envelope, header or leak predicate (PF19 §3.5.10).

FAIL_TOOLING if a capture is malformed or missing after the probe ran, or the evaluator malfunctions.

TOOLING_BLOCKED if the server never becomes ready (connection refused, HTTP 000 or non-HTTP response), `PORT` is unavailable, or check 9 is not PASS.

Deliverables (QA-created, in `audit/qa/hde-epic040/checks/sec-reader-http-live/`): `http_probes.jsonl` (decisive captures); `gunicorn_server.log` (supplementary, non-gating; a server log that is empty is recorded as `no server output`). Primary evidence: `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log`. Tokens: `[]`, `[]`.

Nonclaims: no deployed-service, live-DB or admission-refusal-over-live-HTTP claim.

### CHECK 11 `open-rails-showcompat-vendor`: Bounded open-rails vendor step

Surface / D-goal mapping: D10; PO Q-2; PF05 §7.3.9; AC040-04, AC040-09 (vendor-backed functional proof of the CLI, resolver, core and emitter).
Rails: ENV-V for this step only; restore ENV-C immediately after. Pins as above.
PF anchors: PF05-Canon-HDE-CLI-API-Vendor-Ref §7.3.9; PF19-Canon-Glow-QA-Guide §3.3, §3.5.7; PF07-Canon-Glow-Infrastructure §2.7.

Proof class: vendor-backed no-user behavior (birth-only). Allowed inputs: `--source vendor` and the six birth flags. Forbidden: `--user-a`, `--user-b`, `--source db`, `--source auto`, any app user identifier or `person_uid` from the caller, DB-backed BodyGraphs as input, inline secret values, `--dump-admin-dir`, `--conjunction`.

Intent: prove, against HumanDesignAPI, that the delivered CLI resolves both birth tuples, evaluates the pair through the admitted release and emits canonical output, identically for AB and BA, with a bands-only Reader v1 dump.

PO command(s):

1. Preflight matrix (recorded in the primary log): Plan and QA-90 task identity; PO authorization reference; ENV-V applied; `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` SET; `HDAPI_BASE_URL`, `DATABASE_URL`, retired keys, `ENGINE_ENV` UNSET; check 8 PASS; tuple provenance (default L-51 or PO-named); the exact two commands below.
2. Create the check directory and write `vendor_request.txt` in it (commands with tuples, environment presence and rails values, time, executor, authorization reference; no secret value).
3. AB run: `hdctl showcompat --source vendor --birthdate-a <A date> --birthtime-a <A time> --location-a <A location> --birthdate-b <B date> --birthtime-b <B time> --location-b <B location> --dump-reader audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json`, stdout to `vendor_run_ab.json`, stderr captured separately.
4. BA run: the same with tuples A and B swapped, `--dump-reader` to `reader_v1_ba.json`, stdout to `vendor_run_ba.json`.
5. Restore ENV-C and unset the vendor keys.
6. Secret scan: count occurrences of the `HD_API_KEY` and `GEO_API_KEY` values in every file of the check directory and in both stderr captures, without printing any value (for example `grep -c -F` with the value taken from the environment before it is unset). Expected 0 everywhere.
7. Evaluator (final decisive command, embedded `python -c`), then the stderr text of both runs is appended to the primary log.

PASS if every preflight row holds; both runs exit 0; each stdout is non-empty canonical JSON ending with exactly one LF and no CR, with exactly the keys `schema` (`magic10_compat_result.v1`), `config_id` (`m10-channel-state-v1.0.0`), `release_id` (equal to the manifest SHA-256), `pair_key`, `signals` (20), `categories` (10, in the order `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`); `vendor_run_ab.json` and `vendor_run_ba.json` are byte-identical; each Reader dump has exactly six keys, `reader_version` `v1`, `categories` of one `harmony` item or `[]`, no JSON number, and ends with one LF; the two dumps are byte-identical; the secret scan is zero.

FAIL_BEHAVIOR only if every prerequisite is proven, both commands ran, no tooling or secret fault occurred, and the output contradicts a predicate. Before this status the primary log classifies the cause per PF19 §3.5.7 (vendor contract mismatch, request shaping, response mapping, product implementation defect, or QA expectation mismatch).

FAIL_TOOLING if a secret value appears in any file (quarantine it, do not commit), a forbidden input was used, an evidence file is missing after an attempted run, or a command was changed by guesswork.

TOOLING_BLOCKED if a credential, input or authorization is missing, `HDAPI_BASE_URL` is set, the CLI returns a typed provider refusal caused by rails, configuration, credentials, account or vendor availability, or check 8 is not PASS.

Deliverables (QA-created, in `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/`): `vendor_request.txt`, `vendor_run_ab.json`, `vendor_run_ba.json`, `reader_v1_ab.json`, `reader_v1_ba.json`. The birth tuples are recorded verbatim as PF19 §3.3's substituted birth-input record; they must be synthetic (QA Audit QA50-S01). Primary evidence: `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log`. Tokens: `[]`, `[]`.

Exercised versus inferred: exercised = both birth tuples resolved through HumanDesignAPI, pair evaluated, canonical output and Reader v1 dump emitted. Inferred, not exercised, unless the captured stderr shows it = the exact vendor resource path, auth-header family and adapter status. Not exercised = rate-limit and `Retry-After` handling, typed vendor error mapping, malformed-response handling, v1 legacy guard, mapped-cache persistence, Reader v2 and any deployed service.

### CHECK 12 `live-db-gate-readiness`: Live read-only Gate readiness

Surface / D-goal mapping: D11; AC040-07 (live part); K040-REQ-011; PF09.3 HDE-SEPA005.5.
Rails: ENV-D (`APP_ENV=dev`; closed rails; real `DATABASE_URL`). Pins as above.
PF anchors: PF10 Addendum 2.20; PF09.3-Canon-HDE-Build-Checklist-Separation (HDE-SEPA005.5); PF19-Canon-Glow-QA-Guide §3.3; PF07-Canon-Glow-Infrastructure §7.0, §7.2.1.

Intent: observe, read-only, the actual Gate readiness of the PO-selected current rows in `public.hde_body_graphs_current`, and prove that the observation changed no selected row. No backfill, vendor fallback or row creation occurs (PF19 §3.3 forbids synthesizing users).

PO command(s):

1. Preflight: the selection file exists outside the repository and holds at least one canonical UUID, with no UUID repeated (the tool refuses repeats); `DATABASE_URL` SET; ENV-D applied; check 7 PASS.
2. Before-digests (embedded `python -c`, read-only): for each selected UUID in sorted order, run the product's own statement `CURRENT_ROW_SQL` (`engine/bodygraph/mapped_cache.py`, L-10) through `DBAccess.for_current_env().query(CURRENT_ROW_SQL, (uuid,))`; record the ordinal, the row count, and the SHA-256 of the canonical JSON of the returned rows (non-JSON scalars as strings). Never record a UUID or a payload.
3. Readiness run: `python tools/bodygraph/check_magic10_gate_readiness.py --selection-file <selection file>`, stdout to `audit/qa/hde-epic040/checks/live-db-gate-readiness/readiness_report.json`.
4. After-digests as in step 2.
5. Evaluator (final decisive command, embedded `python -c`).

PASS if:

- step 3 exits 0; the report has `schema` `magic10_gate_readiness.v1`, `read_only` true, `selection.requested` equal to the number of UUID lines and `selection.sha256` present;
- the six `counts` sum to `requested`; `counts.missing` equals the number of UUIDs with zero rows in step 2, `counts.duplicate` equals the number with more than one row, and the other four counts sum to the number with exactly one row;
- `readiness` is `READY` exactly when `counts.ready` equals `requested`;
- before and after digests are equal for every ordinal;
- at least one selected UUID has a current row, so the observation is against current rows.

`READY` or `NOT_READY` is the observation, not the verdict. `NOT_READY` is reported to Kronos as a data-readiness finding for the Product Owner; it is not a failure of this check.

FAIL_BEHAVIOR if the tool exits 0 but its report contradicts the digest cross-check, the counts do not sum, `read_only` is not true, or `readiness` disagrees with the counts.

FAIL_TOOLING if the before and after digests differ (non-mutation not established; concurrent writers cannot be excluded), a capture is malformed, or the evaluator malfunctions.

TOOLING_BLOCKED if no selection is supplied, `DATABASE_URL` is unavailable, the tool refuses `READINESS_UNAVAILABLE` or `RAILS_CLOSED_REQUIRED`, no selected UUID has a current row (PF19 §3.3 no-user environment; AC040-07 "unavailable live facts remain unavailable"), or check 7 is not PASS.

Deliverables (QA-created): `audit/qa/hde-epic040/checks/live-db-gate-readiness/readiness_report.json` (aggregate, identity-safe). Primary evidence: `audit/qa/hde-epic040/checks/live-db-gate-readiness/primary.log`. Tokens: `[]`, `[]`.

### CHECK 13 `live-db-reader-refusal`: Live DB Reader refusal path

Surface / D-goal mapping: D12; AC040-09; PO Q-1 (secret non-leakage with a real DSN in play).
Rails: ENV-D, server `APP_ENV=prod`. Pins as above.
PF anchors: PF19-Canon-Glow-QA-Guide §3.5.10; PF10 Addendum 2.23.

Intent: with the real `DATABASE_URL`, prove that the production Reader route resolves identities through the live read path, refuses unknown identities with the governed 404 on v1 and v2, and leaks no DSN.

PO command(s):

1. Preflight (embedded `python -c`, read-only): `read_current_mapped_bodygraph` returns no row for `00000000-0000-0000-0000-000000000001` and `00000000-0000-0000-0000-000000000002`. If either has a row, record it and stop with `TOOLING_BLOCKED` (input not valid for this run).
2. Start the server as in check 10 with ENV-D, stdout and stderr to `audit/qa/hde-epic040/checks/live-db-reader-refusal/gunicorn_server.log`; readiness via `GET /internal/version` (R-01).
3. Probes into `audit/qa/hde-epic040/checks/live-db-reader-refusal/http_probes.jsonl`: R-02 `POST /api/reader?v=1` and R-03 `POST /api/reader?v=2`, each with the two synthetic UUIDs.
4. Stop the server; confirm port 8000 is closed.
5. Secret scan: occurrences of the `DATABASE_URL` value in `http_probes.jsonl` and `gunicorn_server.log`, counted without printing it. Expected 0.
6. Evaluator (final decisive command).

PASS if R-01 is 200, R-02 and R-03 return 404 `ERR_M10_PERSON_UNRESOLVED` with the four-key envelope, `Cache-Control: no-store` and no `ETag`, no body contains `Traceback`, `File "`, `psycopg` or `postgresql`, and the secret scan is zero.

FAIL_BEHAVIOR if a probe contradicts these predicates or the DSN appears in a public response.

FAIL_TOOLING if the DSN appears only in the server log (quarantine it; record a keys-only logging finding for Kronos), or a capture is malformed.

TOOLING_BLOCKED if `DATABASE_URL` is unavailable, the server never becomes ready, the preflight finds a row, or check 10 is not PASS. A 503 `ERR_M10_RESOLVER_UNAVAILABLE` is `TOOLING_BLOCKED` (database not reachable), not a behavior failure.

Deliverables (QA-created): `http_probes.jsonl`; `gunicorn_server.log` (supplementary). Primary evidence: `audit/qa/hde-epic040/checks/live-db-reader-refusal/primary.log`. Tokens: `[]`, `[]`.

### CHECK 14 `live-db-reader-success`: Live DB Reader success path (conditional)

Surface / D-goal mapping: D13; AC040-09; Reader v1 and v2 over live HTTP with live rows (PF10 Addendum 2.23).
Rails: ENV-D, server `APP_ENV=prod`. Pins as above.
PF anchors: PF10 Addenda 2.23, 2.25; PF19-Canon-Glow-QA-Guide §3.2.

Condition: check 12 is PASS with `readiness` `READY` and `requested` at least 2. When the condition is unmet, record the check `TOOLING_BLOCKED` naming the unmet condition, execute no probe, and produce no supplementary file (conditional deliverables below are then not expected).

Intent: prove the public success bytes of Reader v1 and v2 on live current rows, their numeric-free contract, AB/BA and two-run identity, and non-mutation.

PO command(s):

1. Pair: the first two distinct UUIDs of the selection file in file order, u1 and u2. They are never written to evidence; request bodies are recorded by SHA-256 only.
2. Before-digests for u1 and u2 as in check 12 step 2.
3. Start the server as in check 13 with stdout and stderr to `audit/qa/hde-epic040/checks/live-db-reader-success/gunicorn_server.log`.
4. Probes into `audit/qa/hde-epic040/checks/live-db-reader-success/http_probes.jsonl`: W-01 `?v=1` (u1, u2); W-02 `?v=1` (u2, u1); W-03 `?v=1` (u1, u2) again; W-04 `?v=2` (u1, u2); W-05 `?v=2` (u2, u1); W-06 `?v=2` (u1, u2) again.
5. Stop the server; after-digests; secret scan as in check 13.
6. Evaluator (final decisive command).

PASS if every probe returns 200 with `Content-Type: application/json; charset=utf-8`, `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding` and no `ETag`; each body has exactly the six keys `categories`, `eligible`, `idempotence_hash`, `meta`, `reader_version`, `release_id`, no JSON number, `release_id` equal to the manifest SHA-256, bands in `Cool`, `Open`, `Warm`, `Glow`; v1 bodies carry one `harmony` item or `[]`; v2 bodies carry ten `{"band","id"}` items in canonical order or `[]`; W-01, W-02 and W-03 are byte-identical; W-04, W-05 and W-06 are byte-identical; v1 and v2 agree on `eligible` and on the `harmony` band; digests are unchanged; the secret scan is zero.

FAIL_BEHAVIOR if a probe contradicts a predicate.

FAIL_TOOLING if the digests differ, a capture is malformed, or the DSN appears only in the server log.

TOOLING_BLOCKED if the condition is unmet, the database or server is unavailable, or check 13 is not PASS.

Conditional deliverables (only when the condition holds; QA-created): `http_probes.jsonl`; `gunicorn_server.log` (supplementary). Primary evidence (always): `audit/qa/hde-epic040/checks/live-db-reader-success/primary.log`. Tokens: `[]`, `[]`.

### CHECK 15 `qa-closeout-deliverables`: Close-out deliverables and coverage

Surface / D-goal mapping: D14; AC040-01 and AC040-08 (evidence integrity of the QA run); PF06 §0.4.1.
Rails: ENV-C. Pins as above.
PF anchors: PF06-Canon-Change-Process-Guide §0.4.1; PF19-Canon-Glow-QA-Guide §3.4.3, §4.4.3, §9.2.15.5.

Intent: verify the current-state QA evidence family, append QA-discovered doc deltas, write the path proofs, prove that the QA files do not disturb the governed evidence graph, and produce the coverage accounting that QA-120 uses.

PO command(s):

1. Manifest verification (embedded `python -c`): the manifest holds exactly one entry for each of checks 1 to 14 that was recorded, each `log_path` is the concrete primary-log path that the check's block states, each primary log is non-empty, LF-terminated, starts with a `pf27.step_log_header.v2` header whose `status` equals the manifest status, and every supplementary file named in a primary log exists with the recorded SHA-256.
2. Doc-delta append: append, below the existing content of both doc-delta surfaces, every `DOC_DELTA:` line recorded in the primary logs of checks 3 to 14 (new IDs from DD-13), keeping both files byte-identical. If none, append the line `No new deltas found during execution.`.
3. Path proofs (before-record set): `_refresh_path_proof(path, default_produced_at=<UTC now>, check=False)` then `check=True` for the primary logs of checks 1 to 14, `audit/docdeltas/hde-epic040_doc_deltas.md` and `audit/qa/hde-epic040/00_meta/doc_deltas.md`.
4. Governed-graph non-interference: `python tools/evidence/update_evidence_index.py --check` and `python tools/evidence/validate_evidence_paths.py` (expected rc 0 with the QA files present).
5. Tracked-file observation (attribution only, non-gating): `git status --porcelain`; any tracked file outside the evidence paths of §7.2 that changed is listed for Kronos and is never committed.
6. Coverage accounting written into the body: every check in plan order with status, attempt, evidence pointers and, for non-PASS checks, the blocking precondition and required follow-up.
7. Record this check with `record_check`. Final decisive command: step 4's `validate_evidence_paths.py`.
8. After recording (finalization, outside this primary log): `_refresh_path_proof` with `check=False` then `check=True` for this check's `primary.log` and for `audit/qa/hde-epic040/qa_step_logs_manifest.json`. Kronos verifies at QA-110 that each proof's `sha256` and `size_bytes` match the file.

PASS if steps 1 to 4 succeed and the coverage accounting lists every check.

FAIL_BEHAVIOR: not applicable; this check makes no product-behavior claim.

FAIL_TOOLING if the manifest and a primary log disagree, a supplementary file is missing or changed, a path proof fails check mode, a doc-delta surface differs from its twin, or step 4 fails because of the QA files (an evidence-integration defect for the evidence owner).

TOOLING_BLOCKED if a primary log of a recorded check is missing.

Deliverables (QA-created): `.path_proof.txt` siblings of every primary log of checks 1 to 15, of `audit/qa/hde-epic040/qa_step_logs_manifest.json`, of `audit/docdeltas/hde-epic040_doc_deltas.md` and of `audit/qa/hde-epic040/00_meta/doc_deltas.md`, each at the file's path plus `.path_proof.txt`. Primary evidence: `audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log`. Tokens: `[]`, `[]`.

## 13. Close-out deliverables and final-report criteria

Discovery artifact: `audit/qa/hde-epic040/checks/d0-discovery/primary.log` with the Step-0B surfaces.

QA RCA & Doc Delta summary: produced by Kronos in QA-120 as part of the separate RCA (PF19 §3.1.2; PF06 §0.4.1.2), referencing the governed QA root. It states what ran, what each outcome means, which evidence proves it and whether canon updates are required, maps findings to PF titles as doc-delta intents, and records deferrals as deferrals.

The QA-120 final Report must:

- account for all 15 checks in plan order with status, attempt lineage and evidence pointers under `audit/qa/hde-epic040/`; mark each COVERED, BLOCKED/UNEXECUTABLE (with blocking precondition, why, whether it blocks closeout, and whether a plan or implementation change is needed) or NOT RUN; no step counts as COVERED without a step-scoped pointer (PF19 §9.2.15.5);
- conclude per criterion AC040-01 to AC040-09 as supported, not supported, or Unknown, with the evidence basis; label proof classes (local/offline, in-process, live loopback HTTP, live DB, vendor-backed);
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

Check-to-PF09 mapping: HDE-SEPA005.1 and .2 → check 4; HDE-SEPA005.3 → checks 5, 7, 8; HDE-SEPA005.4 → checks 5, 6; HDE-SEPA005.5 → checks 3, 7, 12, 15 and every pytest group. Checks 9, 10, 11, 13 and 14 verify delivered Reader v2, security and vendor behavior inside HDE-EPIC040 scope set by the PF10 Addendum 2.23 overlay; no PF09.3 subtask names Reader v2 exposure, so they map to the HDE-SEPA005 parent with that PF09 gap noted.

Task-like items this Plan creates, each with exactly one accountability:

| Item | Accountability |
| --- | --- |
| Index and Mirror registration of HDE-EPIC040 QA evidence (QA50-F01) | PF09.3 HDE-SEPA005.5; evidence owner through the whole-change IA PR route |
| `--allow-prod-vendor` gap (DD-04, QA50-B01) | PF09 gap; PF05 and CLI owners through change control; outside HDE-EPIC040 |
| DD-01, DD-02, DD-03, DD-05, DD-06 | Documentation or status drainage only |
| Carried items (DD-07 to DD-12 and QA-10 triage §2) | Their existing records and owners |

## 15. Nonclaims

Approving or executing this Plan does not establish QA PASS for the change, acceptance, closure, PF09 status movement, PF-Canon drainage, a PF10 addendum, deployment, release activation, token satisfaction, broad HumanDesignAPI v2 conformance, deployed-service behavior, database population, mapped-cache persistence, a ledger-bound QA manifest or Index/Mirror publication. Check results establish only their stated predicates and proof classes.

## Provenance

```text
GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-QA-50-20260927-01 (shared with the QA Audit)
  change: EPIC / HDE-EPIC040 (Specification v1.1)
  prompt: QA-50 — Create Whole-Change QA Audit and Plan — 091426.1; Notion 3db4590a05eb81a3ac91f602bad8cfa2; page as of 2026-09-24T15:54:17.481Z; release GCFPE-20260914.1
  role_stage: continuing Kronos, QA-50
  capture_time: 2026-09-27T09:26:32Z
  execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  result: QA_PLAN v1.0, PLAN_PENDING, routed to QA-70 (continuing Isis)
  task_and_attempt_mapping: none yet (QA-90 creates tasks after QA-70 approval)
  repository_persistence: PENDING / NON_GATING (no installed docs/changes/GCFPE_PROMPT_PROVENANCE.md)
```

ASK OK?
