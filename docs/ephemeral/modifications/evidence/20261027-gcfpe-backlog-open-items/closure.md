# Closure — MODIFICATION-20261027-gcfpe-backlog-open-items

`closure.py` run on 2026-10-27 over the 55 selected graph parts at `main` @ `44dba78` (`docs/graph/parts/`). All 55 calls exit 0. The graph rebuild reproduces the D29 proof token: `55 nodes · 235 edges · 55 state_routes · 593,569 bytes · sha256 43f84f29b9921c21f63ffbe21dd36a14bd846a89ae697ba3cf38746c2f887eb1`, validation PASS.

**Closure is undefined, not empty, for targets with no graph part:** the skills (glow-hde-pr-development, change-flow, flowmaster-validate, glow-graph-contract, glow-write-boundary), PE Metaprompt 100926.1, the Glow Operations Hub, the release register, the CL-05 candidate (no part until installed), the v5.0.0 procedure, `reviewer-prompt-template.md` and the skill-identity record.

## Per part: prompts and the union of their Tier 1 radii

| Part | Prompts it edits | Union radius | Radius members |
|---|---|---|---|
| PART-01 PR review findings on real inputs (MB-013, MB-014, MB-023) | PR-35, RS-40, PR-40, PR-20 | 32 | CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, CL-E-30, DOC-10, DOC-20, ESC-25, ESC-30, ESC-40, IA-10, IA-20, IA-30, IA-60, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-10, QA-100, QA-110, QA-20, QA-50, QA-60, RS-10, RS-20, RS-40 |
| PART-03 Business case per requirement and work unit (MB-015, MB-016, MB-017) | CF-C-30, CF-E-30, IA-30, PR-10, PR-20 | 33 | CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-30, IA-40, IA-50, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-30, PR-35, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10, RS-20, RS-40 |
| PART-04 Plan-side real inputs and no emulation (MB-016, MB-017, MB-018) | IA-30, PR-10, PR-20 | 31 | CF-C-10, CF-C-20, CF-C-30, CF-E-10, CF-E-20, CF-E-30, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-30, IA-40, IA-50, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-30, PR-35, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10, RS-20, RS-40 |
| PART-06 PR-20's description of a PR-40 REJECT (MB-002) | PR-20 | 23 | CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10, RS-20 |
| PART-07 Handoff package sentences, D23-B (MB-010) | CL-20, CL-30, CL-40, DOC-20, IA-10, IA-20, IA-30, MGR-10, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-10, QA-120, QA-20, QA-50, QA-60, QA-80, RS-10 | 50 | CF-C-10, CF-C-20, CF-C-30, CF-E-10, CF-E-20, CF-E-30, CF-PO-10, CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, IA-10, IA-20, IA-30, IA-40, IA-50, IA-60, MGR-10, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-10, QA-100, QA-110, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30, RS-40, UTIL-10 |
| PART-08 DOC-20's second PR-40 entry (MB-001) | DOC-20 | 25 | CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-10, QA-100, QA-110, QA-20, QA-50, QA-60, RS-10, UTIL-10 |
| PART-09 IA-40 redline return to IA-30 (MB-020) | IA-40, IA-30 | 12 | CF-C-30, CF-E-30, IA-10, IA-20, IA-30, IA-40, IA-50, PR-10, PR-30, PR-35, QA-80, RS-40 |
| PART-10 Approved QA Plan change route (MB-021) | QA-70, QA-80, QA-50, QA-60, QA-90, QA-110, ESC-40 | 36 | CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, CL-E-30, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, IA-10, IA-20, IA-40, IA-60, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-20, UTIL-10 |
| PART-11 QA-70 coherence, QA-80 reshape, QA-50 CI binding (MB-026) | QA-70, QA-80, QA-50 | 27 | CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, CL-E-30, DOC-10, DOC-20, ESC-25, ESC-30, ESC-40, IA-10, IA-20, IA-40, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-20 |
| PART-12 QA evidence persisted in the repository (MB-022) | QA-100, QA-90, QA-50 | 28 | CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, UTIL-10 |
| PART-13 Close-mutation-set stage, CL-05 (MB-030, MB-027) | QA-120, CL-C-10, CL-E-10 | 9 | CL-20, CL-C-10, CL-E-10, CL-E-20, ESC-10, ESC-30, QA-110, QA-120, QA-90 |
| PART-16 Concurrent addendum numbering (MB-009) | CF-C-30, CF-E-30, IA-30, QA-70, RS-20, ESC-40 | 29 | CF-C-20, CF-C-30, CF-C-40, CF-E-20, CF-E-30, CF-E-40, CL-E-30, ESC-30, ESC-40, IA-10, IA-20, IA-30, IA-40, IA-50, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30, RS-40 |

Parts with no prompt edit (PART-02, PART-05 until ruled, PART-14, PART-15, PART-17 to PART-25) have no closure of their own; their targets are listed in the record.

## `closure.py` output for every prompt in scope (35), pasted

```
CF-C-30  -- closure over 55 graph parts

  upstream                       2  CF-C-20, CF-C-40
  downstream                     2  CF-C-40, IA-10
  state_sharers                  2  CF-E-30, IA-30
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 5
  CF-C-20, CF-C-40, CF-E-30, IA-10, IA-30
```
```
CF-E-30  -- closure over 55 graph parts

  upstream                       2  CF-E-20, CF-E-40
  downstream                     2  CF-E-40, IA-10
  state_sharers                  2  CF-C-30, IA-30
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 5
  CF-C-30, CF-E-20, CF-E-40, IA-10, IA-30
```
```
CL-20  -- closure over 55 graph parts

  upstream                       2  CL-C-10, CL-E-10
  downstream                     5  CL-30, CL-40, CL-E-20, CL-E-30, CL-E-40
  state_sharers                  0  -
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 7
  CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40
```
```
CL-30  -- closure over 55 graph parts

  upstream                       1  CL-20
  downstream                     1  CL-40
  state_sharers                  0  -
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 2
  CL-20, CL-40
```
```
CL-40  -- closure over 55 graph parts

  upstream                       4  CL-20, CL-30, CL-E-40, MGR-10
  downstream                     1  CL-40
  state_sharers                  7  CL-E-20, DOC-20, ESC-25, OPS-20, QA-100, QA-110, UTIL-10
  boundaries (NOT consumers)     3  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 12
  CL-20, CL-30, CL-40, CL-E-20, CL-E-40, DOC-20, ESC-25, MGR-10, OPS-20, QA-100, QA-110, UTIL-10
```
```
CL-C-10  -- closure over 55 graph parts

  upstream                       1  QA-120
  downstream                     2  CL-20, ESC-30
  state_sharers                  1  CL-E-10
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 4
  CL-20, CL-E-10, ESC-30, QA-120
```
```
CL-E-10  -- closure over 55 graph parts

  upstream                       1  QA-120
  downstream                     3  CL-20, CL-E-20, ESC-30
  state_sharers                  1  CL-C-10
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 5
  CL-20, CL-C-10, CL-E-20, ESC-30, QA-120
```
```
DOC-20  -- closure over 55 graph parts

  upstream                       1  PR-40
  downstream                     4  DOC-10, PR-40, QA-10, RS-10
  state_sharers                 23  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-110, QA-20, QA-50, QA-60, UTIL-10
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 25
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-10, QA-100, QA-110, QA-20, QA-50, QA-60, RS-10, UTIL-10
```
```
ESC-40  -- closure over 55 graph parts

  upstream                       1  ESC-30
  downstream                     3  ESC-30, PR-30, PR-35
  state_sharers                  3  CL-E-30, QA-70, RS-20
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 6
  CL-E-30, ESC-30, PR-30, PR-35, QA-70, RS-20
```
```
IA-10  -- closure over 55 graph parts

  upstream                       3  CF-C-30, CF-E-30, IA-50
  downstream                     5  IA-10, IA-20, IA-30, IA-50, IA-60
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 24
  CF-C-10, CF-C-20, CF-C-30, CF-E-10, CF-E-20, CF-E-30, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-30, IA-50, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
```
```
IA-20  -- closure over 55 graph parts

  upstream                       2  IA-10, IA-50
  downstream                     4  IA-20, IA-30, IA-50, IA-60
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-30, IA-50, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
```
```
IA-30  -- closure over 55 graph parts

  upstream                       4  IA-10, IA-20, IA-40, IA-50
  downstream                     2  IA-40, PR-10
  state_sharers                  6  CF-C-30, CF-E-30, IA-40, PR-30, PR-35, RS-40
  boundaries (NOT consumers)     3  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 10
  CF-C-30, CF-E-30, IA-10, IA-20, IA-40, IA-50, PR-10, PR-30, PR-35, RS-40
```
```
IA-40  -- closure over 55 graph parts

  upstream                       2  IA-30, IA-50
  downstream                     1  IA-30
  state_sharers                  2  IA-30, QA-80
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 3
  IA-30, IA-50, QA-80
```
```
MGR-10  -- closure over 55 graph parts

  upstream                       0  -
  downstream                     5  CF-C-10, CF-E-10, CF-PO-10, CL-40, QA-10
  state_sharers                  0  -
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 5
  CF-C-10, CF-E-10, CF-PO-10, CL-40, QA-10
```
```
OPS-10  -- closure over 55 graph parts

  upstream                       2  OPS-30, PR-40
  downstream                     3  ESC-25, OPS-20, RS-10
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-20, OPS-30, PR-10, PR-20, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10
```
```
OPS-20  -- closure over 55 graph parts

  upstream                       1  OPS-10
  downstream                     3  ESC-25, OPS-30, RS-10
  state_sharers                 22  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, QA-90, UTIL-10
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 24
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-30, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, QA-90, RS-10, UTIL-10
```
```
OPS-30  -- closure over 55 graph parts

  upstream                       1  OPS-20
  downstream                     3  ESC-25, OPS-10, RS-10
  state_sharers                  4  CL-E-30, PR-40, QA-110, RS-20
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 8
  CL-E-30, ESC-25, OPS-10, OPS-20, PR-40, QA-110, RS-10, RS-20
```
```
PR-10  -- closure over 55 graph parts

  upstream                       2  IA-30, PR-40
  downstream                     3  PR-10, PR-20, RS-10
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 23
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-30, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10
```
```
PR-20  -- closure over 55 graph parts

  upstream                       4  DOC-10, PR-10, PR-40, RS-20
  downstream                     2  PR-20, RS-10
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     3  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_PROCEED, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 23
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10, RS-20
```
```
PR-30  -- closure over 55 graph parts

  upstream                       3  ESC-40, RS-20, RS-40
  downstream                     3  PR-30, PR-35, RS-20
  state_sharers                  3  IA-30, PR-35, RS-40
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 6
  ESC-40, IA-30, PR-30, PR-35, RS-20, RS-40
```
```
PR-35  -- closure over 55 graph parts

  upstream                       4  ESC-40, PR-30, RS-20, RS-40
  downstream                     3  PR-35, PR-40, RS-20
  state_sharers                  3  IA-30, PR-30, RS-40
  boundaries (NOT consumers)     2  NATHAN_MANUAL_MERGE_ASSERTION, NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 7
  ESC-40, IA-30, PR-30, PR-35, PR-40, RS-20, RS-40
```
```
PR-40  -- closure over 55 graph parts

  upstream                       3  DOC-20, PR-35, RS-40
  downstream                     7  DOC-10, DOC-20, OPS-10, PR-10, PR-20, QA-10, RS-10
  state_sharers                  6  CL-E-30, DOC-10, DOC-20, OPS-30, QA-110, RS-20
  boundaries (NOT consumers)     3  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 13
  CL-E-30, DOC-10, DOC-20, OPS-10, OPS-30, PR-10, PR-20, PR-35, QA-10, QA-110, RS-10, RS-20, RS-40
```
```
QA-10  -- closure over 55 graph parts

  upstream                       4  DOC-20, MGR-10, PR-40, QA-20
  downstream                     2  ESC-30, QA-20
  state_sharers                  0  -
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 5
  DOC-20, ESC-30, MGR-10, PR-40, QA-20
```
```
QA-100  -- closure over 55 graph parts

  upstream                       2  QA-110, QA-90
  downstream                     1  QA-110
  state_sharers                 22  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-20, QA-50, QA-60, QA-90, UTIL-10
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 23
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-110, QA-20, QA-50, QA-60, QA-90, UTIL-10
```
```
QA-110  -- closure over 55 graph parts

  upstream                       3  QA-100, QA-120, QA-90
  downstream                     4  ESC-10, QA-100, QA-120, QA-90
  state_sharers                  7  CL-40, CL-E-30, DOC-20, OPS-30, PR-40, QA-90, UTIL-10
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 10
  CL-40, CL-E-30, DOC-20, ESC-10, OPS-30, PR-40, QA-100, QA-120, QA-90, UTIL-10
```
```
QA-120  -- closure over 55 graph parts

  upstream                       1  QA-110
  downstream                     5  CL-C-10, CL-E-10, ESC-10, QA-110, QA-90
  state_sharers                  0  -
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 5
  CL-C-10, CL-E-10, ESC-10, QA-110, QA-90
```
```
QA-20  -- closure over 55 graph parts

  upstream                       1  QA-10
  downstream                     2  QA-10, QA-50
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 20
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-10, QA-100, QA-50, QA-60
```
```
QA-50  -- closure over 55 graph parts

  upstream                       1  QA-20
  downstream                     4  QA-60, QA-70, QA-80, QA-90
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-60, QA-70, QA-80, QA-90
```
```
QA-60  -- closure over 55 graph parts

  upstream                       1  QA-50
  downstream                     3  QA-70, QA-80, QA-90
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-70, QA-80, QA-90
```
```
QA-70  -- closure over 55 graph parts

  upstream                       3  QA-50, QA-60, QA-80
  downstream                     2  QA-80, QA-90
  state_sharers                  3  CL-E-30, ESC-40, RS-20
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 7
  CL-E-30, ESC-40, QA-50, QA-60, QA-80, QA-90, RS-20
```
```
QA-80  -- closure over 55 graph parts

  upstream                       3  QA-50, QA-60, QA-70
  downstream                     1  QA-70
  state_sharers                  1  IA-40
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 4
  IA-40, QA-50, QA-60, QA-70
```
```
QA-90  -- closure over 55 graph parts

  upstream                       5  QA-110, QA-120, QA-50, QA-60, QA-70
  downstream                     3  ESC-10, QA-100, QA-110
  state_sharers                  3  OPS-20, QA-100, QA-110
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 8
  ESC-10, OPS-20, QA-100, QA-110, QA-120, QA-50, QA-60, QA-70
```
```
RS-10  -- closure over 55 graph parts

  upstream                       8  DOC-10, DOC-20, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-40
  downstream                     1  RS-20
  state_sharers                  1  RS-30
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 10
  DOC-10, DOC-20, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-40, RS-20, RS-30
```
```
RS-20  -- closure over 55 graph parts

  upstream                       5  PR-30, PR-35, RS-10, RS-30, RS-40
  downstream                     5  PR-20, PR-30, PR-35, RS-30, RS-40
  state_sharers                  4  ESC-40, OPS-30, PR-40, QA-70
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 10
  ESC-40, OPS-30, PR-20, PR-30, PR-35, PR-40, QA-70, RS-10, RS-30, RS-40
```
```
RS-40  -- closure over 55 graph parts

  upstream                       1  RS-20
  downstream                     4  PR-30, PR-35, PR-40, RS-20
  state_sharers                  3  IA-30, PR-30, PR-35
  boundaries (NOT consumers)     2  NATHAN_MANUAL_MERGE_ASSERTION, NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 5
  IA-30, PR-30, PR-35, PR-40, RS-20
```
