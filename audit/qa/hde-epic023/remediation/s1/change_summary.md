# HDE-EPIC023 remediation PR-01 (DEV lane) — change summary

## What changed
- D16/D17/D18 QA plan validators now target canonical emitted evidence surfaces and content checks.
- D17/D18 primary.log headers now include pf_refs, intended_tokens, and claimed_tokens for schema consistency.
- D16 step-logs manifest upsert now overwrites any existing entry, detects placeholder corruption, and forces FAIL_BEHAVIOR with a log finding when placeholders are present.

## Why
- Align determinism checks with canonical evidence outputs per PF10 and remove non-canonical expectations.
- Standardize step-log headers across D16–D18.
- Prevent placeholder corruption from persisting in the step-logs manifest.

## D16 orientation demo path adjustment
- Validator now targets the canonical output at audit/gates/topology/orientation_demo.txt (with sibling .path_proof.txt) emitted by tools/evidence/orientation_demo.py.
