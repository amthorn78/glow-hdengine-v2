# PO Instructions - HDE-EPIC036 - po-010

## Manifest Header

### Artifact Map

- HDE-EPIC: HDE-EPIC036 / Fermentation Pass 7
- Steps: po-010
- Approved QA Plan File: QA Plan HDE-EPIC036.md
- Approval Doc File: approval QA Plan HDE-EPIC036.md
- Previous Step Report File: PF10; addendum 2.7
- Repo root validated: amthorn78/glow-hdengine-v2, default branch main, current HEAD 5cd0162bf131e3277bd966d339997bdb28f6164d, compare main...main status identical.
- PF-Canon consulted: PF10 (current) + PF05 + PF02
- Output: PO Instructions - HDE-EPIC036 - po-010

## Step po-010 - PO-010

### Step intent excerpt (verbatim from Approved Plan)

> Produce one bounded live production-like QA proof for this epic unless a controlling exemption is supplied. This plan uses a PO-approved live v2 base value and expects route-policy refusal before legacy BodyGraph request construction.

### Step proof excerpt (verbatim from Approved Plan and/or Approval Doc)

> - PASS if the bounded live-target configuration check records `PROVIDER_ROUTE_UNSUPPORTED`.
> - PASS if the bounded live-target configuration check records `unsupported_runtime_nonclaim`.
> - PASS if the proof shows the PO-approved v2 base was redacted in evidence.

## Short recap - HDE-EPIC036 / Fermentation Pass 7 - po-010

This step exercises the bounded open-rails live-target route-policy proof for configured-v2 `bg:resolve --source vendor`. It is meant to prove the CLI records `PROVIDER_ROUTE_UNSUPPORTED` / `unsupported_runtime_nonclaim` before legacy BodyGraph request construction while redacting the PO-approved v2 base value. It matters because this is the approved live production-like proof boundary for the epic, without claiming full HumanDesignAPI v2 runtime conformance, BodyGraph-detail compatibility, OPS completion, PF09 status movement, or closeout.

## Canon Revalidation Notes

- PF10 current was consulted for HDE-EPIC036 addendum 2.7 as prior-step context only; it records the prior review scope `step-0b-doc-delta-capture / po-001 / po-002 / po-003 / po-004 / po-005 / po-006 / po-007 / po-008 / po-009` as PASS, but it was not used as current repo proof for `po-010`.
- PF05 command-safety posture applies: do not issue executable instructions when the repo-resident helper command is not currently validated for the selected check.
- PF02 architecture posture applies: do not invent a replacement route, runtime surface, public transport behavior, or vendor credential path to compensate for an unresolved QA helper locus.

## Live Repo Validation Notes

- Repo validation confirmed the repository root as `amthorn78/glow-hdengine-v2` on default branch `main`, with current HEAD `5cd0162bf131e3277bd966d339997bdb28f6164d`.
- Repo validation confirmed `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` exists on `main`.
- Repo validation found that current `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` registers checks only through `po-009` in its `CHECKS` map and does not register `po-010`.
- Repo validation found no `def check_po010` in the current HDE-EPIC036 helper; GitHub search for `def check_po010` returned matches only in other epic helper files, not in the HDE-EPIC036 helper.
- The Approved Plan's `po-010` command depends on `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-010`; current repo validation contradicts that executable helper locus for this selected step.

## Drift Inputs

- Captured from Approved Plan: check ID `po-010`.
- Captured from Approved Plan: `audit/qa/hde-epic036/checks/po-010/primary.log`.
- Captured from Approved Plan: `audit/qa/hde-epic036/checks/po-010/primary.log.path_proof.txt`.
- Captured from Approved Plan: `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`.
- Captured from Approved Plan: `audit/qa/hde-epic036/checks/po-010/live_route_policy.log.path_proof.txt`.
- Captured from Approved Plan: `HD_API_BASE_URL` must be PO-set as the PO-approved live v2 base value.
- Captured from Approved Plan: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
- Captured from Previous Step Report: PF10 addendum 2.7 records prior scope through `po-009` as PASS; this is dependency context only and not current repo proof for `po-010`.
- Captured from live repo validation: current HDE-EPIC036 QA helper is not currently executable for `po-010`.

## PO Inputs Needed

- Needed input: A current, source-grounded `po-010` executable helper path or an approved rerun/update of Step-0B that restores `po-010` support in `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py`.
- Why it is needed: The Approved Plan command for this step depends on `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-010`, but current repo validation shows the helper's `CHECKS` map does not include `po-010`; issuing the command as-is would rely on an unvalidated and currently contradicted repo-resident executable locus.
- Allowed source: Approved Plan, Approval Doc, live repo validation, or a PO-provided updated QA helper evidence state under `audit/qa/hde-epic036/00_meta/`.

## Planning Defect Disposition

- Disposition: Requiring re-confirmation of the `HD_API_BASE_URL` value for this step is a planning defect when the approved value is already supplied via Variable Import.
- Corrected rule for po-010: consume the pre-set Variable Import binding, log only presence/redaction posture in evidence, and do not request or print the raw base value in step instructions.
- Remaining blocker: only the executable-helper contradiction (`po-010` not registered in current `hde036_live_qa_harness.py`) remains a valid gating input for step execution.
