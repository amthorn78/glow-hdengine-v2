---
artifact_type: GCFPE_MODIFICATION_EVIDENCE
modification_id: MODIFICATION-20260923-alpha-feedback-open-entries
part: PART-01
item: ITEM-01
plan_step: 1
executed: 2026-09-23
result: CLEAN — 0 PROMPT_BODY_GOVERNANCE_STATE hits in 40 of 40 bodies; step 1a not triggered
---

# PART-01 — governance-line scan of the 40 unread `091426.1` bodies

This file holds ids, page ids, error codes and counts only. It holds no prompt-body text
(`prompt-corpus-policy.md`); an offending line would have been quoted here, and there were none.

## What was run

- **Validator.** The shipped `flowmaster-validate/scripts/validate_gcfpe_20260914.py`, installed
  tree, sha256 `747b1043c9cd5517b6e5bf0977b93584e5056474ad834b206554f8141a196100`.
- **Contract.** The bundled `change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json`,
  sha256 `2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b`. The validator reported
  `contract_status: SELECTED_PRODUCTION`, 55 selected members, frozen graph sha256
  `90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223`, 55 nodes and 227 edges.
- **Reading the bodies.** Each body was fetched from Notion once. A session-local extractor then read
  the fetch results out of the session's own transcript and tool-result files and piped
  `{PROMPT_ID: body}` straight into the validator:

  ```
  body_from_transcript.py <ID=PAGE ...> | PYTHONDONTWRITEBYTECODE=1 python3 \
    flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow \
    --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json \
    --bodies-stdin
  ```

  The extractor lives in the session scratchpad, outside the repository. No body was retyped or
  summarised, and no body was written to disk by the session.
- **Files the harness saved.** It saved five fetch results over its inline limit to its own
  tool-results folder: `QA-10`, `OPS-30`, `PR-40`, `PR-20` and `PR-10`. Under `D22` these are part
  of the read. They were not copied, hashed, or reopened except by the extractor, and they are left
  to harness teardown (`D22` condition 4).
- **How the run was split.** Four lanes of 10 bodies, each run by a separate worker. One cross-body
  check needs `QA-120`, `CL-E-10` and `CL-C-10` together, and those three fell in different lanes,
  so each lane reported `QA_PASS_CLASS_MAP_AND_INTAKES` under `prompt_body_checks_not_evaluated`. It
  was then run on the three bodies together (last row below), so no check went unevaluated.

## Result

| lane | bodies | `ok` | errors | `PROMPT_BODY_GOVERNANCE_STATE` hits | not evaluated |
|---|---|---|---|---|---|
| 0 | `QA-10`, `OPS-20`, `DOC-20`, `ESC-25`, `CL-E-20`, `QA-60`, `QA-20`, `IA-30`, `PR-50`, `IA-60` | true | 0 | 0 | `QA_PASS_CLASS_MAP_AND_INTAKES` (set-scoped) |
| 1 | `OPS-30`, `PR-30`, `CL-C-10`, `ESC-40`, `CL-E-40`, `RS-20`, `CL-E-30`, `RS-30`, `RS-40`, `IA-40` | true | 0 | 0 | same |
| 2 | `PR-40`, `OPS-10`, `CL-E-10`, `ESC-30`, `QA-50`, `QA-70`, `QA-100`, `RS-10`, `CF-E-40`, `IA-20` | true | 0 | 0 | same |
| 3 | `PR-20`, `PR-10`, `CL-40`, `DOC-10`, `ESC-10`, `QA-110`, `QA-120`, `QA-80`, `CF-E-30`, `IA-50` | true | 0 | 0 | same |
| trio | `QA-120`, `CL-E-10`, `CL-C-10` | true | 0 | 0 | none |

`prompt_bodies_validated` named all 40 ids, 10 per lane. The extractor found every page on its first
pass, and no id was reported `NOT FOUND`.

**Offending lines quoted:** none. There were no hits to quote.

## Completeness of what the validator saw

A truncated body could pass the validator by accident, so the extracted bodies were measured
against the sizes recorded when the bodies were first read at ANALYZE, without writing them
anywhere:

- 38 of 40 extracted bodies are exactly 48 bytes shorter than the recorded size.
- The 2 `CF-E-*` bodies are exactly 43 bytes shorter.

The offset is the same for bodies from 5.6 KB to 82 KB. That points to the two measurements framing
the page differently, not to truncation, which would shorten each body by a different amount.

## What this closes, and what it does not

- **Coverage.** With the 15 bodies confirmed clean in rounds 28–30, all 55 `091426.1` bodies have
  now been checked. The earlier 15 are `CF-C-10`, `CF-C-20`, `CF-C-30`, `CF-C-40`, `CF-E-10`,
  `CF-E-20`, `CF-PO-10`, `CL-20`, `CL-30`, `GCFPE-MGMT-10`, `IA-10`, `MGR-10`, `PR-35`, `QA-90` and
  `UTIL-10`; the list comes from `docs/ephemeral/gcfpe.round30/REPORT-r30-CORRECTIONS.md:155-157`.
  This scan did not re-read them.
- **No repair.** Nothing was found, so there is no leftover line to remove, no false positive to
  narrow, and no spawned Modification (step 1a).
- **Limit.** The scan shows the bodies are clean as of their Notion state on 2026-09-23, judged by
  the matcher shipped in the installed validator above. It does not cover later edits. The body
  edits this Modification makes later are covered by the step 46 gate, not by this scan.
