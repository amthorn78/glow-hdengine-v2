# HDE-EPIC033 Doc Deltas

## BLOCKERS

None recorded for PR-01 contract-inventory evidence binding.

## CAVEATS

This PR binds HumanDesignAPI v2 and legacy v1 public documentation contract inventory only. It does not implement or claim runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader changes, a new HTTP home, or AI scope.

## PROCESS UPDATES

Recorded during PO-010 and PO-012 Moon Loop remediation on 2026-06-04.

- Future EPIC033 boundary-proof checks should not rely on case-sensitive exact `grep -F` matches against governed prose when the proof target is semantic posture rather than byte identity.
- Prefer regex-normalized or case-normalized QA checks under `audit/qa/hde-epic033/`, or promote a single canonical phrase constant that both the generator and the runbook consume.
- When semantic boundary language is present but prose-case drift breaks a receipt, classify the issue as a QA evidence-harness defect and keep any Moon Loop repair within the QA root.
