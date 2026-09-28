---
artifact_type: GTWPE_ERROR_LEDGER
plan: GTWPE-IMPLEMENTATION-PLAN-v1.2.md, §7
kept_by: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
updated: 2026-09-28 (E-009 to E-023 from W1 P1, design §15 and CHECKPOINT §9)
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
| E-009 | P1 / sources | SOURCE | LISTED | W1 (P1-1) | `AGENTS.md` changed after P0; plan §1 and S5 quote an exception it no longer has | design §10.1 | OPEN. The design names every file at G3; plan wording in the next revision |
| E-010 | P1 / sources | SOURCE | LISTED | W1 (P1-2) | HDE Governance §9.1.1 conflicts with PF06 §1.0.3, §1.0.6 and PF27 §2A on PF30 and PF20 records | design §10.3 | OPEN, for Nathan. Canon is not edited; the record prompts follow §9.1.1 |
| E-011 | P1 / plan | PLAN_DEFECT | LISTED | W1 (P1-3) | Plan §2.2 gave every specification a PF30.1 record; Epics have none | design §10.4 | FIXED in the design |
| E-012 | P1 / plan | PLAN_DEFECT | LISTED | W1 (P1-4) | Plan §2.5 and Q1 predate Nathan's three target rulings of 2026-09-28 | design §10.2 | FIXED in the design |
| E-013 | P1 / sources | SOURCE | LISTED | W1 (P1-5) | PF text runs about 3.0 bytes a token, not 4; ten PFs are 300 KB or more | design §10.6 | FIXED: pricing uses the measured rate |
| E-014 | P1 / D22 | SOURCE | LISTED | W1 (P1-6) | P0's `D22` disclosure omitted the harness's session and subagent transcripts, which also hold fetched text | `CHECKPOINT.md` §5 | FIXED: disclosed |
| E-015 | P1 / authority | AUTHORITY | LISTED | W1 (P1-7) | The PE Metaprompt's "read-only" line and the register's PF rule are GCFPE controls outside GTWPE-MGMT-10 | design §14 D-9 | OPEN, D-9 at G1 |
| E-016 | P1 / post-check | VALIDATION | LISTED | W1 (P1-8) | The post-check does not watch the harness's `tool-results/` or `subagents/` directories | `CHECKPOINT.md` §9.6 | OPEN. Plan v1.2 §16.2: in the design, built in P4 |
| E-017 | P1 / change prompt | PLAN_DEFECT | LISTED | W1 (P1-9) | `modification_validate.py` has no target class for a tool, lock or selftest | validator line 81 | OPEN. Plan v1.2 P2(a): PE37 adds `tool` |
| E-018 | P1 / design | PLAN_DEFECT | LISTED | W1 (P1-10) | Design §16's `closure` risk is unfounded; no validator check reads `closure` | validator lines 401–405, 575 | OPEN. P1r removes it |
| E-019 | P1 / change prompt | PLAN_DEFECT | LISTED | W1 (P1-11) | GTWPE-MGMT-10's source, the GCFPE-MGMT-10 proposed body, can change without triggering it | `CHECKPOINT.md` §9.7 | OPEN. P1r pins the source and adds it to the triggers |
| E-020 | P1 / diff check | PLAN_DEFECT | REQUIRED | P1 reviewer (RQ-1, R1) | PF27 can change in a run with no specification | `design/REVIEW-P1-DIFFCHECK-R1.md` | OPEN. Proposed `ACCEPTED_RISK` (DISP-001), fixed in P4 with a failing selftest case; awaits Nathan |
| E-021 | P1 / diff check | PLAN_DEFECT | REQUIRED | P1 reviewer (RQ-2, R1) | A repository input's source record is built by no named command, and S2 cannot search it | same | OPEN. Proposed `ACCEPTED_RISK`, fixed in P3 (reader half) and P4; awaits Nathan |
| E-022 | P1 / diff check | PLAN_DEFECT | REQUIRED | P1 reviewer (RQ-3, R3) | A live read of a prompt-body input leaves an unreported transcript copy (`D22`) | same | OPEN. Proposed `ACCEPTED_RISK` with option (i): a Notion prompt body is `UNSUPPORTED_INPUT`; awaits Nathan |
| E-023 | P0 relay | PLAN_DEFECT | LISTED | W1 (§9.1) | PE37's relay text carried a `<paste Nathan's words>` slot; it reached W1 unfilled, so G0 is still unrecorded | `CHECKPOINT.md` §9.1 | FIXED in practice: relay texts carry no slot to fill. G0 asked for directly |
