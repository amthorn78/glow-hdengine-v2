---
artifact_type: CRD_SOURCE_ITEM_BRIEFS
artifact_version: "1.2"
predecessor: docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.1.md (superseded; v1.2 adds seven items at the Product Owner's direction, corrects the uncovered-test count, and records production APP_ENV)
logical_id: HDE-CRD-0002-CANDIDATE-ITEM-BRIEFS
change_id: HDE-CRD-0002
proposed_change_class: CRD
author: Isis, Lead Developer (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
captured: 2026-10-11 (v1.0); revised 2026-10-11T13:15:38Z (v1.1); revised 2026-10-12T14:19:31Z (v1.2)
source_register: Candidate CRD Items List, items 5 to 8 (https://app.notion.com/p/3e54590a05eb813c8d89d065026f694d)
repository_head_read: origin/main d86b8850
---

# HDE-CRD-0002 — Source item briefs (Candidate CRD Items List items 5 to 8)

## Correction in v1.2

v1.0 and v1.1 said "about 190" test files run in no CI lane. No record supports that figure. The source records give **129**: observation O-11 in `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md` and the PR05 base-versus-head sweeps. Item 5(c) now uses 129, as counted at PR05. The Specification recounts on `main`.

## Product Owner decisions

These quotations are verbatim.

**2026-10-11:**
- "Move all items to accepted for CRD drafting."
- "You can create a handoff for this to begin the process for HDE-CRD0002"
- "Yes, add all seven to HDE-CRD-0002." This added the seven carried defects from the HDE-EPIC040 CL-40 scan (`docs/ephemeral/HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md` §4) as item 5 part (e).

**2026-10-12:**
- "Add the 7 items to the CRD". This adds the seven items the Lead Developer's completeness review found missing. They are recorded as item 5 parts (c-2), (c-3), (f), (g), (h) and (i), and item 6 part (b).
- "APP_ENV in railway is set to prod". This is the Product Owner's report of the production service's configuration. It was not observed by the Lead Developer.

They are recorded as follows:
- **Review status.** Candidate CRD Items List items 5, 6, 7 and 8 are `Accepted for CRD Drafting`. That status is not Specification approval or implementation authorization.
- **Change class and identity.** The Product Owner selected the change class CRD and the identity HDE-CRD-0002, covering all four items as one change. The Product Owner wrote `HDE-CRD0002`. PF30.1 §3.1 fixes the canonical syntax as `HDE-CRD-<NNNN>`, so `HDE-CRD-0002` is used. It is the next ID after `HDE-CRD-0001`, the highest entered.
- **What this record does not do.** It does not register a PF30 record, draft a Specification, approve scope, or allocate work. Those belong to CF-PO-10, CF-C-10 to CF-C-30 and their owners.

## Common facts

- No file outside `docs/` changed on `main` between `1ea6a262` and `d86b8850`. The v1.1 re-checks at `1ea6a262` therefore still hold, and every item added in v1.2 was re-checked at `d86b8850`.
- The briefs use the intake fields of PF30.1 §4.1 and the §7 template, "Intake, analysis & bounded scope". The Lead Developer findings are intake findings. Bounded scope is approved only by the CRD Plan approval.

## Item 5 — HDE-EPIC040 carried defects

- **Observed need.** Defects shipped with HDE-EPIC040, or carried through it, with no owning work unit:
  - **(a)** `pyproject.toml` package-data covers only `catalog/*.json` and `math/*.json`. A wheel install therefore omits release members, and admission refuses outside a source checkout (O-12).
  - **(b)** The production app (`adapter.factory`, per the `Procfile`) returns Flask HTML 404s without `no-store` for unknown non-compat paths. Only `/api/compat/v1` (the scoped handler in `adapter/http_reader.py`) and `adapter.wsgi` return the governed `ERR_NOT_FOUND` (O-P06a-22).
  - **(c)** CI coverage gaps:
    - **(c-1)** 129 test files run in no CI lane (O-11, counted at PR05). They hold 57 recorded failures and 13 collection errors, plus the `tests/reader_v1/test_cli_proof.py` baseline failure (RA-08, O-P06a-03). Some of them rewrite tracked evidence artifacts when run in the repository tree (O-11).
    - **(c-2)** The classifier gives an unregistered `tools/qa/*.sh` or `tools/qa/*.sql` file the `evidence` and `qa` lanes with no owner test (O-22). The fail-closed unknown-source check covers only `tools/bodygraph/` (`ci/checks/classify_ci_changes.py`, re-checked at `d86b8850`). *Added in v1.2.*
    - **(c-3)** `ci.yml`'s `paths-ignore` lists 4 documentation prefixes, while the classifier's `_DOCUMENTATION_PREFIXES` lists 8. A PR touching only `docs/crd/`, `docs/plans/`, `docs/qa/` or `docs/run/` still starts a CI run (RA-12, re-checked at `d86b8850`). *Added in v1.2.*
  - **(d)** The attestation builder's wheel stage fails under Debian-patched setuptools (O-10).
  - **(e)** Seven carried defects, added by the Product Owner on 2026-10-11:
    - **O-P07-01:** the `hdctl --help` showcompat summary says "Emit canonical Reader v1 bytes", but stdout is `magic10_compat_result.v1` (`engine/cli/main.py:79`). The file is a release member.
    - **O-P07-02:** `aux-preview --band` is not applied when the band comes from the pair file.
    - **O-P07-03:** `dev/reader_harness/app.py` raises `AttributeError` at import (`app.getattr`). `VERIFY.sh` and `docs/acceptance/reader_a7_crib.md` still name it.
    - **O-P07-04 (security-relevant):** dev `GET /reader` (`adapter/http_reader.py`) serves when `APP_ENV` is unset or exactly `dev`, and the production factory (`adapter/factory.py`, per the `Procfile`) mounts that blueprint. **Production status, 2026-10-12:** the Product Owner reports that the production service sets `APP_ENV=prod`. The route therefore refuses with 403 there today. The fail-open default remains: a deployment that loses the variable would serve the dev route.
    - **O-P06a-23:** the engine-core evidence currency test ignores `release_id`.
    - **O-P06b-17:** current-release captures carry origin-family Mirror labels.
    - **O-OPS01-01:** the isolated closure's admission probe depends on the ambient installed package.
  - **(f)** **`--allow-prod-vendor` is not implemented** (DD-04, QA50-B01). PF05 §7.1.11 states the production vendor override as a **Required-Now** contract: §7.1.11a the exact flag on `hdctl bg:resolve --source vendor`; §7.1.11b environment classification; §7.1.11c the rail and flag matrix; §7.1.11d evaluation order; §7.1.11e the error carrier; §7.1.11f the audit contract. No parser or resolver code implements it (re-checked at `d86b8850`). PF29 §16 tells users it is absent. *Added in v1.2.*
  - **(g)** **The endpoint catalog is incomplete** (RA-14). `AGENTS.md` names `docs/ENDPOINTS_CATALOG.json` as the source of truth, but 8 route strings registered in `adapter/` have no entry: `/api/aux/narrative`, `/aux/narrative`, `/internal/healthz`, `/internal/readyz`, `/ops/db/unavailable`, `/ops/probe/env`, `/ops/rails/refusal` and `/ops/writer/diagnostic` (re-checked at `d86b8850`). *Added in v1.2.*
  - **(h)** **`.env.example` has no `GEO_API_KEY` entry** (re-checked at `d86b8850`). PF20 §2.26.7 records it with the implementation lane. *Added in v1.2.*
  - **(i)** **Stale operator documentation** (re-checked at `d86b8850`). *Added in v1.2.*
    - **O-P07-05:** the "Readiness rules" in `docs/ADAPTER_009.md` describe a `compute_pair` smoke and typed 503s for `/internal/readyz`. `adapter/wsgi.py` returns 200 unconditionally, and no `compute_pair` exists in `engine/` or `adapter/`. The file's port statements are also stale.
    - **DD-11:** `docs/ADAPTER_009.md` (`COMPAT_GET_BODY_400_OK`) says `body_not_allowed`. The code emits `invalid_json` (FND-017). The code side is from the record and was not re-checked.
    - **O-P07-06:** `ARCHITECTURE.md` has stale statements: the `emit_compact_json` return type, and the "Routing (dev only)" heading, which now also covers the production mount.
- **Why warranted.**
  - (b) is live on the public production surface.
  - (c) leaves regressions in 129 test files invisible to CI. (c-3) also spends CI runs on documentation-only PRs.
  - (d) breaks the next release attestation.
  - (e) O-P07-04 is not exposed today but fails open. The other (e) defects are misleading CLI help, an ignored flag, a dead harness and evidence-tooling gaps.
  - (f) is a canon requirement with no implementation. Until it exists, no audited production vendor override is possible.
  - (g) makes the source-of-truth catalog wrong about which routes the service serves.
  - (h) and (i) mislead whoever configures or operates the service. (i) describes a readiness check that does not run.
- **Affected surfaces:**
  - code:
    - `pyproject.toml`, `adapter/factory.py`, `adapter/http_reader.py`, `tools/evidence/build_release_attestation.py`;
    - the uncovered test files, `ci/checks/classify_ci_changes.py` and `.github/workflows/ci.yml`;
    - for (e): `engine/cli/main.py`, the `aux-preview` CLI path, `dev/reader_harness/app.py`, `VERIFY.sh`, the engine-core evidence test, the Mirror provenance labels and the attestation closure probe;
    - for (f): the `hdctl bg:resolve` parser and the vendor resolver;
    - for (g): `docs/ENDPOINTS_CATALOG.json` and its audit mirror `artifacts/audit/ENDPOINTS_CATALOG.json`;
    - for (h): `.env.example`;
  - data: none;
  - operations: release attestation; for (f), the production override's audit trail;
  - documentation: `docs/ADAPTER_009.md`, `ARCHITECTURE.md`, and as affected;
  - governance: none expected;
  - canon: none expected. (f) implements existing canon (PF05 §7.1.11) and changes none.
- **Constraints and risks.**
  - (a) or (b) may change release members, which forces a manifest re-cut and new admission pins (`ADMITTED_RELEASE_*` in `engine/config/registry_loader.py`).
  - (e) O-P07-01 changes a release member, so it shares (a)'s re-cut. (f) may too, if the parser or resolver it changes is a release member.
  - (c-1) may expose real defects that enlarge the work. Running the uncovered files in the repository tree can rewrite tracked evidence, so the sweep must run in a throwaway copy.
  - O-P07-04's fix must not break dev, test or local use of `/reader`.
  - (f) must keep generic SAFE rails first. The override never opens a closed rail and never lets public Reader or Aux traffic call the vendor (PF05 §7.1.11).
  - (g)'s audit mirror must be produced by its owning tool, not hand-edited.
- **Intake evidence:**
  - `docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md` (RA-04, RA-05, RA-08, RA-12, RA-14);
  - the PR05 implementation result (O-11, O-22) and the PR06, PR06a and PR06b lineage reviews (#501, #508, #513);
  - `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md` §12;
  - for (e): `docs/ephemeral/HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md` §4, the PR07 lineage review and implementation result, and the OPS01 receipt v1.2;
  - for (f) to (i): PF20 §2.26.7 (DD-04 / QA50-B01, RA-14, `.env.example`, DD-11), PF05 §7.1.11, and the PR07 implementation result (O-P07-05, O-P07-06).
- **Lead Developer finding:**
  - valid;
  - not already satisfied: (a) to (e) re-checked at `1ea6a262`, and (c-2), (c-3) and (f) to (i) at `d86b8850`;
  - belongs in the CRD lane.
  - (c) is the largest part and may justify its own phase block. (f) is the largest new part.
- **Proposed bounded scope.**
  - Fix (a), (b), (d), (h) and (i).
  - For (c-1), bring each uncovered file into a CI lane or retire it with a recorded reason. Fix (c-2) and (c-3) in the same work.
  - For (e), fix each defect or retire it with a reason. O-P07-04 is fixed by refusing the dev route unless `APP_ENV` is explicitly `dev`, `test` or `local`.
  - For (f), implement PF05 §7.1.11 as written.
  - For (g), add every served route to the catalog, or remove the route, and regenerate the mirror through its owner.
- **Exclusions.** No Reader contract or payload change. No release re-cut beyond what (a), (b), (e) or (f) requires. No new evidence family. No canon change.
- **Expected outcome.**
  - Wheel installs admit the release.
  - Every production 404 uses the governed envelope.
  - Every test file runs in CI or is retired. The classifier fails closed on unregistered `tools/qa/` sources, and documentation-only PRs start no CI run.
  - Attestation builds on Debian.
  - The (e) defects are fixed or retired, and the dev `/reader` route is never served without an explicit dev, test or local `APP_ENV`.
  - `--allow-prod-vendor` works as PF05 §7.1.11 states.
  - The endpoint catalog lists every served route.
  - `.env.example`, `docs/ADAPTER_009.md` and `ARCHITECTURE.md` match the code.

## Item 6 — Open code PRs only after the implementation is pushed; review the code that missed it

- **Observed need.**
  - **(a)** Codex security review runs when a PR opens. Two PRs were opened holding only a plan, so their code got no security review: PR04 #467 and PR06 #501. PR05 #492 and PR06a #508 were reviewed on their first push only.
  - **(b)** No one has since reviewed the code those four PRs merged (RA-09). It includes the production Reader route and the compat HTTP handler. Item 6(a) prevents recurrence but does not cover that code. *Added in v1.2.*
- **Why warranted.** Public HTTP routes merged without a security review of the code (RA-09). The HDE Phased Epics record (PF20 §2.26.7) keeps this as a stated limitation, not a resolved one.
- **Affected surfaces:**
  - code: for (b), the code merged by #467, #492, #501 and #508, as review input; fixes only where a confirmed finding needs one;
  - governance: for (a), the PR-30 prompt text (GCFPE);
  - canon: none.
- **Constraints and risks.**
  - (a): none material.
  - (b): the review may find defects that enlarge the work. Findings in code a later PR already changed are reviewed against `main`.
- **Intake evidence:**
  - PR04 lineage review N-05;
  - PR05 lineage review L-10;
  - `docs/ephemeral/HDE-EPIC040-QA10-change-audit-triage-v1.0.md` RA-09;
  - PF20 §2.26.7, the "RA-09 / PR04/05/06/06a security coverage" row.
- **Lead Developer finding:**
  - valid;
  - not already satisfied: the 2026-10-09 GCFPE round (#598) did not include (a), and no review of the (b) code is recorded;
  - (a) is **not naturally CRD lane.** It is a prompt change with no development target, and its native route is GCFPE-MGMT-10. It is carried here by Product Owner direction. The Specification should decide whether it is delivered inside the CRD or routed to GCFPE-MGMT-10 and tracked.
  - (b) belongs in the CRD lane: it reviews and, where needed, fixes application code.
- **Proposed bounded scope.**
  - (a) PR-30 opens the code PR with the implementation commit, and plan successors go in a separate PR.
  - (b) One security review of the code merged by #467, #492, #501 and #508, read on `main`. Each confirmed finding is fixed in this CRD or routed with a reason.
- **Exclusions.** No change to the review tooling. No re-review of accepted PR lineages beyond security.
- **Expected outcome.** Every code PR is security-reviewed on code, and the HDE-EPIC040 code that missed review has had one.

## Item 7 — Read-only pre-push / pre-plan check script

- **Observed need.** Each PR session re-derives the same checks by hand or skips them: the base-versus-head sweep of tests that no lane runs, CI-lane impact, release membership, and the `ci.yml` replay. PR04 had 4 failed CI runs out of 19.
- **Why warranted.** It would reduce paid CI failures and the rescopes caused by unchecked lane or release impact.
- **Affected surfaces:**
  - code: a new script and its test (location to be set by the Specification);
  - canon: none.
- **Constraints and risks.** It duplicates CI logic and must track `ci.yml` changes. It overlaps item 5(c), so it should be sequenced after it.
- **Intake evidence.** PR history 2026-09-19 to 26: #467, #492, #501, #508.
- **Lead Developer finding:**
  - valid;
  - not already satisfied: no such script exists at `d86b8850`;
  - belongs in the CRD lane (tooling).
- **Proposed bounded scope.** One read-only script with its own test. It:
  - sets up a Python 3.12 venv;
  - prints the current PF10 path and hash;
  - shows CI lanes and release membership for given paths;
  - runs the uncovered-test sweep in a throwaway copy;
  - replays `ci.yml` in a throwaway worktree.
- **Exclusions.** No writes. No SessionStart hook.
- **Expected outcome.** One command gives a session its pre-push picture.

## Item 8 — Close-pack writer cannot produce a canon close report

- **Observed need.** `tools/qa/generate_epic_close_pack.py`, the only governed close-pack writer, is limited by `schemas/epic_close_candidate_source.v1.json` to four fixed headings, ten fixed sentences and five fixed nonclaims. It cannot write the close report that canon requires:
  - the acceptance section and `SATISFIED` / `NOT SATISFIED` (Change Process Guide §3.5.2.1);
  - the deferrals and later-drain statements (HDE Schemas & Artifacts, close-pack artifacts);
  - the QA RCA summary;
  - the heading `QA Rails — Open/Close (Final PR)` (Glow QA Guide).

  The close workflow's same-run evidence also has no admitted home once the QA manifest is final.
- **Why warranted.** No epic or CRD can complete the ordinary Close Gate. HDE-EPIC040 needed exceptional closure for this reason.
- **Affected surfaces:**
  - code: `tools/qa/generate_epic_close_pack.py`, its schema and `tests/qa/test_generate_epic_close_pack.py`, and possibly `tools/evidence/update_evidence_index.py`;
  - canon: Change Process Guide §3.5.2 and §0.7, the HDE Schemas & Artifacts close-pack rules, and Glow QA Guide close-pack truthfulness. All were unchanged on `main` at PF06 v2.5.4, PF12 v2.9.6 and PF19 v3.0.6 when v1.1 was written, so an ADR is required (PF30.1 §4.1 "Canon posture").
- **Constraints and risks.**
  - HDE-EPIC039 made the generic writer neutral on purpose, so this reverses a design choice and must weigh that rationale.
  - The change touches the release-sanity and close-validation lanes.
- **Intake evidence:**
  - `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md` (B-1, B-2);
  - `docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md` (CC-1, CC-2);
  - `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` §5.
- **Lead Developer finding:**
  - valid;
  - not already satisfied: the schema is unchanged at `d86b8850`;
  - belongs in the CRD lane (cross-change tooling with a canon ADR).
- **Proposed bounded scope.**
  - A governed, feedback-free writer that produces a canon-conforming close report and manifest from tracked inputs.
  - An admitted home for close-workflow run evidence that does not reopen an approved QA manifest.
- **Exclusions.** No new evidence families, no acceptance tokens, no retroactive close pack for HDE-EPIC040.
- **Expected outcome.** A closing change can pass the ordinary Close Gate.
- **Sequencing note.** Item 8 is needed before the next epic or CRD closes, not before one starts.

## Reviewed and left out (2026-10-12)

The Lead Developer's completeness review checked the HDE-EPIC040 carried register in PF20 §2.26.7 and PF09.3 HDE-SEPA005. These items were left out of this CRD:

| Item | Reason |
| --- | --- |
| O-P07-07 (`VERIFY.sh` imports the dead harness) | Already covered by O-P07-03 |
| O-P07-08 (PF10 storage defect) | Moot after the PF10 v13.5 rewrite |
| O-P07-09 (`AGENTS.md` cites PF10 by section) | Resolved: `AGENTS.md` at `d86b8850` cites no PF10 section |
| RA-11 (`bg:resolve` output skips the LF guard), RA-15 (serializer NaN and globals) | Recorded as information; no requirement established |
| RA-16 (repository root clutter) | Low value; repository owner |
| Final-check window atomicity | A disclosed limitation, not adopted as a promise |
| O-OPS01-02, CC-4 | Prompt or process work for GCFPE-MGMT-10 |
| CC-3, CC-5, CC-6 | Canon wording for their owners |
| Live Gate readiness and live Reader success | PF09.7 HDE-COAG003.8 and HDE-COAG003.9; a future App-era epic |

## Canon relied on

Read on `main` at `d86b8850` unless noted:
- PF30.1-Canon-HDE-CRD-Records v0.9: §3.1 (identifier governance); §4.1 (initial registration); §7 (record template, "Intake, analysis & bounded scope").
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3: §7.1.11 SAFE rails and production vendor override, §7.1.11a to §7.1.11f.
- PF29-Canon-HDE-Users-Guide v1.0.2: §16 Known limitations and nonclaims (`--allow-prod-vendor`).
- PF20-Reference-HDE-Phased-Epics v1.9.6: §2.26.7 Tracked Issues, Variances and Remaining Owners.
- PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.7: HDE-SEPA005 task notes (carried limitations owned by HDE-CRD-0002).
- PF06-Canon-Change-Process-Guide v2.5.4: §0.7; §3.5.1, including "Exceptional closure record."; §0.4.1.2 "Location" (read for v1.1 at `1ea6a262`).
- PF27-Canon-Plan-Templates v2.0.5: §10 scope rule (read for v1.1 at `1ea6a262`).
- PF10-HDE-Build-Notes v13.5.2 (HDE Build Notes): no rule on these items found.
- `AGENTS.md`: endpoint catalog as source of truth; code-review scope prefixes.

In-flight documents: those listed under each item's intake evidence; the Candidate CRD Items List (Notion).
