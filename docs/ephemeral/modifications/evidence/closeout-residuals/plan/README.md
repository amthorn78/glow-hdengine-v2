# PLAN evidence — MODIFICATION-20260923-closeout-residuals

Everything the execution specification
(`docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-closeout-residuals.md`) cites as `EV/`. Written by
`MODE = PLAN`, 2026-09-23. No prompt body is stored here: body clauses appear only as the engine's anchors and the
dry runs' readback notes, each at most 15 words (`D22`).

| path | what | how it was checked |
|---|---|---|
| `DECISIONS.md` | the PLAN decisions P-01 to P-54 | the spec's §2 maps every review finding to one |
| `engine/` | the body rules as one engine: `canon.py` (canonical texts from their repository homes), `closeout_rules.py` (rules, CHECKs, spans), `locals.json` (per-body LOCAL edits), `dryrun.py` (PLAN), `land.py` (EXECUTE), `pages.json` | self-test; two dry runs over every live body (`dryrun/`) |
| `registry/` | `registry.diff` (base `8b4e46ed…`, result `4643741b…`), `row_assertions.json` (the guards), `GUARDS.md`, `report.json`, `guard_tests.json`, `nam002_live.py`, and the builders `guards.py`, `apply_registry.py`, `guard_tests.py` | `ALL_CHECKS_OK`, `ALL_OK`; loader `valid: true`; deriver drift `[]` |
| `skills/` | `manifest.json` (every changed file's sha256, freeze digests before and after, EXECUTE commands), `diffs/` (7 packages), `contract-template-README.md`, `results/` | each diff round-trips with `patch`; every suite and regression recorded |
| `texts/` | the exact repository texts (`edits.json`, one Markdown file each) | each anchor occurs exactly once at its turn |
| `notion/` | the control-page edits (`edits.json`), the Candidate CRD Items List migration (`M2.json`), the Notion worker's notes | each `old_str` occurs once on the page as fetched |
| `dryrun/pass1/` | the rule-level dry run, 7 batches | all 51 bodies passed after the data fixes now in the engine |
| `dryrun/pass2/` | the complete dry run, 6 batches: per-body engine output and batch reports | 56 of 56 pass (50 live, 5 untouched live, the proposed MGMT-10 body) |

The builders in `registry/` and the skills' `results/` were run in the PLAN session's scratchpad, and the paths they
print are scratchpad paths. The files EXECUTE runs (`engine/`, `registry/nam002_live.py`) resolve the repository root
themselves.
