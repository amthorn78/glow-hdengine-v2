---
artifact_type: ONE_TIME_TASK_PROMPT
artifact_version: "1.0"
logical_id: HDE-EPIC040-QAEV01-EVIDENCE-LANDING-TASK-PROMPT
work_unit_id: HDE-EPIC040-QAEV01
change_id: HDE-EPIC040
author: Isis, Lead Developer for HDE-EPIC040 (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
ordered_by: docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md (D-3)
standing: One-time prompt for this change only; not a GCFPE release member
---

# HDE-EPIC040-QAEV01 — Land the QA evidence of record on `main`

Paste everything below this line into a new top-level session on `amthorn78/glow-hdengine-v2`. Pasting it is the Product Owner's Proceed for this unit only.

## Task

Put HDE-EPIC040's accepted QA evidence on `main`, registered in the evidence index. Keep the change small; it is bookkeeping in support of development, not new evidence work.

The evidence is on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` at `787bb97`: 41 files, 39 under `audit/qa/hde-epic040/` plus `audit/docdeltas/hde-epic040_doc_deltas.md` and its path proof.
- Do not use branch `qa/hde-epic040-qa100-plan-v1.2`; it is Run A and non-canonical.
- The evidence branch merges cleanly into `main`.

## Do

Use closed rails throughout: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`.

1. Branch `qa/hde-epic040-evidence-landing` from `origin/main`. Merge the evidence branch with a merge commit.
2. Confirm that nothing changed in transit. This must print nothing:
   `git diff 787bb97 HEAD -- audit/qa/hde-epic040 audit/docdeltas/hde-epic040_doc_deltas.md audit/docdeltas/hde-epic040_doc_deltas.md.path_proof.txt`
3. Register the HDE-EPIC040 QA files in `tools/evidence/update_evidence_index.py`. Add one per-epic list the way `EPIC029_PRIMARY_ARTIFACTS` does, and extend the matching test in `tests/ops/test_evidence_index.py`. Register:
   - the QA step logs manifest;
   - the 12 check `primary.log` files;
   - the doc-delta file.
4. Run `python tools/evidence/update_evidence_index.py`. This canonical writer updates the Index, sentinel, Mirror and their companions.
5. Check:
   - `python tools/evidence/update_evidence_index.py --check`;
   - `python tools/evidence/orientation_demo.py --check`;
   - `python tools/evidence/validate_evidence_paths.py`;
   - `ci/checks/check_mirror_schema.sh`;
   - `ci/checks/check_evidence_index_hash.sh`;
   - `python -m pytest tests/ops/test_evidence_index.py`.

   Install `requirements-dev.txt` first.
6. Open one PR. Use the `.github/pull_request_template.md` headings. Under "What merging does", say: the HDE-EPIC040 QA evidence and its index registration become current on `main`; no QA was run; no closure, close pack, PF09 or canon change.
7. Get exact-head CI green. Never merge, and never use `[skip ci]`.

## Do not

- Run any QA check.
- Change any byte of the 41 evidence files.
- Hand-edit any Index, Mirror, sentinel or path proof.
- Touch anything outside the evidence files, the updater registration, its test and the updater's own outputs.

## If blocked

If the updater cannot admit the files by the existing pattern, or CI fails for a reason outside this change, stop:
- leave the branch as it is;
- tell the Product Owner the exact blocker in a few lines.

No workaround.

## When the PR is green

Reply with the PR number and its CI result. Then end with:

```text
NEXT_PROMPT_HANDOFF
Destination: CL-E-10 — Perform Epic Retrospective and Decide Closure — 091426.1
https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac?pvs=204
Receiving role and session: Isis, continuing Lead Developer and terminal closure authority for HDE-EPIC040 (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2).
Change: HDE-EPIC040 (Epic).
Manual prerequisites: the Product Owner has merged amthorn78/glow-hdengine-v2#<number>, and has authorized exceptional closure of HDE-EPIC040 (docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md §2).

Inputs:
- docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md — Lead Developer decisions D-1 to D-3
- docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md — DO_NOT_CLOSE decision being resolved
- docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md — retrospective and analysis that stand
- docs/ephemeral/HDE-EPIC040-QA120-qa-report-v1.0.md — final QA Report, verdict PASS
```

Replace `<number>` with the actual PR number.
