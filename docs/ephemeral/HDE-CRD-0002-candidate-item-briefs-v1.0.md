---
artifact_type: CRD_SOURCE_ITEM_BRIEFS
artifact_version: "1.0"
logical_id: HDE-CRD-0002-CANDIDATE-ITEM-BRIEFS
change_id: HDE-CRD-0002
proposed_change_class: CRD
author: Isis, Lead Developer (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
captured: 2026-10-11
source_register: Candidate CRD Items List, items 5 to 8 (https://app.notion.com/p/3e54590a05eb813c8d89d065026f694d)
repository_head_read: origin/main 1ea6a262
---

# HDE-CRD-0002 — Source item briefs (Candidate CRD Items List items 5 to 8)

## Product Owner decisions (2026-10-11)

These quotations are verbatim:
- "Move all items to accepted for CRD drafting."
- "You can create a handoff for this to begin the process for HDE-CRD0002"

They are recorded as follows:
- **Review status.** Candidate CRD Items List items 5, 6, 7 and 8 move to `Accepted for CRD Drafting`. That status is not Specification approval or implementation authorization.
- **Change class and identity.** The Product Owner selected the change class CRD and the identity HDE-CRD-0002, covering all four items as one change. The Product Owner wrote `HDE-CRD0002`. PF30.1 §3.1 fixes the canonical syntax as `HDE-CRD-<NNNN>` and says the unhyphenated `HDE-CRD0XX` form names the superseded epic-internal meaning. `HDE-CRD-0002` is therefore used, and it is the next ID after the highest entered, `HDE-CRD-0001` (PF30.1 v0.9, the only PF30 volume on `main`).
- **What this record does not do.** It does not register a PF30 record, draft a Specification, approve scope, or allocate work. Those belong to CF-PO-10, CF-C-10 to CF-C-30 and their owners.

## Common facts

- No code changed on `main` between the HDE-EPIC040 closure (`1fce7e74`, #560) and `1ea6a262`. Every defect below was re-checked at `1ea6a262`.
- The briefs use the intake fields of PF30.1 §4.1 and the §7 template, "Intake, analysis & bounded scope". The Lead Developer findings are intake findings. Bounded scope is approved only by the CRD Plan approval.

## Item 5 — HDE-EPIC040 carried defects

- **Observed need.** Four defects shipped with HDE-EPIC040 with no owning work unit:
  - **(a)** `pyproject.toml` package-data covers only `catalog/*.json` and `math/*.json`, so a wheel install omits release members and admission refuses outside a source checkout (O-12).
  - **(b)** The production app (`adapter.factory`, per the `Procfile`) returns Flask HTML 404s without `no-store` for unknown non-compat paths. Only `/api/compat/v1` (the scoped handler in `adapter/http_reader.py`) and `adapter.wsgi` return the governed `ERR_NOT_FOUND` (O-P06a-22).
  - **(c)** About 190 test files run in no CI lane. They hold 57 recorded failures and 13 collection errors, plus the `tests/reader_v1/test_cli_proof.py` baseline failure (RA-08, O-P06a-03).
  - **(d)** The attestation builder's wheel stage fails under Debian-patched setuptools (O-10).
- **Why warranted.**
  - (b) is live on the public production surface.
  - (c) leaves regressions in about a third of the test suite invisible to CI.
  - (d) breaks the next release attestation.
- **Affected surfaces:**
  - code: `pyproject.toml`, `adapter/factory.py`, `adapter/http_reader.py`, `tools/evidence/build_release_attestation.py`, the uncovered test files, `ci/checks/classify_ci_changes.py`;
  - data: none;
  - operations: release attestation;
  - documentation: as affected;
  - governance: none expected;
  - canon: none expected.
- **Constraints and risks.**
  - (a) or (b) may change release members, which forces a manifest re-cut and new admission pins (`ADMITTED_RELEASE_*` in `engine/config/registry_loader.py`).
  - (c) may expose real defects that enlarge the work.
- **Intake evidence:**
  - `docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md` (RA-04, RA-05, RA-08);
  - the PR06, PR06a and PR06b lineage reviews (#501, #508, #513);
  - `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md` §12.
- **Lead Developer finding:**
  - valid;
  - not already satisfied, re-checked at `1ea6a262`;
  - belongs in the CRD lane.
  - Part (c) is the largest and may justify its own phase block.
- **Proposed bounded scope.** Fix (a), (b) and (d). For (c), bring each uncovered file into a CI lane or retire it with a recorded reason.
- **Exclusions.** No Reader contract or payload change. No release re-cut beyond what (a) or (b) requires. No new evidence family.
- **Expected outcome.**
  - Wheel installs admit the release.
  - Every production 404 uses the governed envelope.
  - Every test file runs in CI or is retired.
  - Attestation builds on Debian.

## Item 6 — Open code PRs only after the implementation is pushed

- **Observed need.** Codex security review runs when a PR opens. Two PRs were opened holding only a plan, so their code got no security review: PR04 #467 and PR06 #501. PR05 and PR06a were reviewed on their first push only.
- **Why warranted.** Public HTTP routes merged without a security review of the code (RA-09).
- **Affected surfaces:**
  - code: none;
  - governance: the PR-30 prompt text (GCFPE);
  - canon: none.
- **Constraints and risks.** None material.
- **Intake evidence:**
  - PR04 lineage review N-05;
  - PR05 lineage review L-10;
  - `docs/ephemeral/HDE-EPIC040-QA10-change-audit-triage-v1.0.md` RA-09.
- **Lead Developer finding:**
  - valid;
  - not already satisfied: the 2026-10-09 GCFPE round (#598) did not include it;
  - **not naturally CRD lane.** It is a prompt change with no development target, and its native route is GCFPE-MGMT-10. It is carried here by Product Owner direction. The Specification should decide whether it is delivered inside the CRD or routed to GCFPE-MGMT-10 and tracked.
- **Proposed bounded scope.** PR-30 opens the code PR with the implementation commit, and plan successors go in a separate PR.
- **Exclusions.** No change to the review tooling.
- **Expected outcome.** Every code PR is security-reviewed on code.

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
  - not already satisfied: no such script exists at `1ea6a262`;
  - belongs in the CRD lane (tooling).
- **Proposed bounded scope.** One read-only script with its own test. It:
  - sets up a Python 3.12 venv;
  - prints the current PF10 path and hash;
  - shows CI lanes and release membership for given paths;
  - runs the uncovered-test sweep;
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
  - canon: Change Process Guide §3.5.2 and §0.7, the HDE Schemas & Artifacts close-pack rules, and Glow QA Guide close-pack truthfulness. All are unchanged on `main` at PF06 v2.5.4, PF12 v2.9.6 and PF19 v3.0.6, so an ADR is required (PF30.1 §4.1 "Canon posture").
- **Constraints and risks.**
  - HDE-EPIC039 made the generic writer neutral on purpose, so this reverses a design choice and must weigh that rationale.
  - The change touches the release-sanity and close-validation lanes.
- **Intake evidence:**
  - `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md` (B-1, B-2);
  - `docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md` (CC-1, CC-2);
  - `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` §5.
- **Lead Developer finding:**
  - valid;
  - not already satisfied: the schema is unchanged at `1ea6a262`;
  - belongs in the CRD lane (cross-change tooling with a canon ADR).
- **Proposed bounded scope.**
  - A governed, feedback-free writer that produces a canon-conforming close report and manifest from tracked inputs.
  - An admitted home for close-workflow run evidence that does not reopen an approved QA manifest.
- **Exclusions.** No new evidence families, no acceptance tokens, no retroactive close pack for HDE-EPIC040.
- **Expected outcome.** A closing change can pass the ordinary Close Gate.

## Canon relied on

Read on `main` at `1ea6a262`:
- PF30.1-Canon-HDE-CRD-Records v0.9: §3.1 (identifier governance); §4.1 (initial registration); §7 (record template, "Intake, analysis & bounded scope").
- PF06-Canon-Change-Process-Guide v2.5.4: §0.7; §3.5.1, including "Exceptional closure record."; §0.4.1.2 "Location".
- PF27-Canon-Plan-Templates v2.0.5: §10 scope rule (checked unchanged).
- PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.6: HDE-SEPA005 status (context only).
- PF10-HDE-Build-Notes v13.5.1 (HDE Build Notes): no current addenda.

In-flight documents: those listed under each item's intake evidence. Also the Candidate CRD Items List (Notion).
