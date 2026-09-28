---
artifact_type: GTWPE_ERROR_LEDGER
plan: GTWPE-IMPLEMENTATION-PLAN-v1.1.md, §7
kept_by: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
updated: 2026-09-28
---

# GTWPE error ledger

A phase does not close with a `REQUIRED` error open (plan §7).

| id | phase / step | class | severity | found by | finding | evidence | disposition |
|---|---|---|---|---|---|---|---|
| E-001 | P0 / sources | PLAN_DEFECT | LISTED | W1 (P0-1) | The plan's `status` still read `AWAITING_APPROVAL` after W1 was started | Plan v1.0 line 8 | FIXED in plan v1.1 (`status`, §15) |
| E-002 | P0 / skills | AUTHORITY | LISTED | W1 (P0-2) | T6's canon write is forbidden by `glow-write-boundary` until its exception is installed; P5 did not order the install first | `CHECKPOINT.md` §4.4; plan v1.0 §5 | FIXED in plan v1.1: P5 installs the skill package before T6. The install itself remains Nathan's |
| E-003 | P0 / plan | PLAN_DEFECT | LISTED | W1 (P0-3) | One records PR conflicted with S8's per-run canon PR | Kickoff; plan v1.0 §2.4 | FIXED in plan v1.1 per Nathan's ruling of 2026-09-28: PRs store and do not gate; the canon PR is separate and its merge adopts the change |
| E-004 | P0 / probes | TOOL_ACCESS | LISTED | W1 (P0-4) | The §2.3 readers' dependencies (pandoc, pypdf, openpyxl, HTML converters) are absent; PyPI is reachable | `CHECKPOINT.md` §4.5 | OPEN. P1 designs the pinned provisioning step; P2 builds and tests it |
| E-005 | P0 / Notion | SOURCE | LISTED | W1 (P0-5) | PE37's baseline said HDE TW has 21 direct children; it has 20 | `CHECKPOINT.md` §4.6 | FIXED: correction added to `TW-BASELINE-20260924.md` |
| E-006 | P0 / subagents | AUTHORITY | LISTED | W1 (§4.2) | A subagent's tools include Write, Edit, Bash, `merge_pull_request` and `create_session`; "writes nothing" rests on its brief and W1's check | `CHECKPOINT.md` §4.2 | OPEN. P1's design states the brief and the post-check (clean `git status`, Notion unchanged) |
| E-007 | P0 / PE Metaprompt | PROMPT_DEFECT | LISTED | PE test; W1 (§7.2) | PE test defects D5, D7, D8 and D10 have no workaround in the kickoff | `PE-METAPROMPT-TEST-20260924.md`; `CHECKPOINT.md` §7.2 | OPEN. P1 applies W1's proposed handling (one terminal return; no effort in bodies; old-text search in GTWPE-MGMT-10; a decision on Drive as a Path A origin). The PE repair itself goes to the MGMT-10 promotion Modification |
| E-008 | P0 / probes | SOURCE | LISTED | W1 (§4.1) | `AGENTS.md` line 27 says `rg` is absent; it is present | `CHECKPOINT.md` §4.1 | DECLINED for GTWPE: outside its scope, and `AGENTS.md` is written only on Nathan's instruction |
