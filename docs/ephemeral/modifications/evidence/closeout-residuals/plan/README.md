# PLAN evidence — MODIFICATION-20260923-closeout-residuals

Everything the execution specification
(`docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-closeout-residuals.md`) cites as `EV/`. Written by
`MODE = PLAN`, 2026-09-23; repaired 2026-09-24 (rounds 2 to 5). No prompt body is stored here: body clauses appear only as the engine's anchors and the
dry runs' readback notes, each at most 15 words (`D22`).

| path | what | how it was checked |
|---|---|---|
| `DECISIONS.md` | the PLAN decisions P-01 to P-95 | the spec's §2 maps every review finding to one |
| `engine/` | the body rules as one engine: `canon.py` (canonical texts from their repository homes), `closeout_rules.py` (rules, CHECKs, spans), `locals.json` (per-body LOCAL edits), `dryrun.py` (PLAN), `land.py` (EXECUTE: `plan`, `check`; each edit stated `NOT_LANDED`, `LANDED` or `MIXED`, and only the missing ones landed, P-88; no journal and no reverse mode, P-58), `graph_check.py` (the PART-16 gate), `pages.json` | self-test; five dry runs over every live body and a synthetic partial-landing test (`dryrun/`) |
| `registry/` | `registry.diff` (base `8b4e46ed…`, result `97bda1a0…`), `row_assertions.json` (the guards), `GUARDS.md`, `report.json`, `guard_tests.json`, `nam002_live.py`, `nam002_proof/`, and the PLAN-time builders `guards.py`, `apply_registry.py`, `guard_tests.py`, `summarize.py`, `build_guards_md.py` (P-74) | `ALL_CHECKS_OK`, `ALL_OK`; loader `valid: true`; deriver drift `[]` |
| `skills/` | `manifest.json` (every changed file's sha256, freeze digests before and after, EXECUTE commands), `run_gate.py` (the suite gate, sets `pre`, `pkg`, `post`), `diffs/` (7 packages), `expected_after_patch.txt` (each patched skill's file count and digest, which X4.3 diffs against), `contract-template-README.md`, `results/` | each diff round-trips with `patch`; every suite and regression recorded; `results/gate_proof_x.json`: the whole EXECUTE sequence run in spec §9 order (`results/run_proof_x.py`, full output kept; `results/build_gate_proof.py` builds the summary), every set passing |
| `texts/` | the exact repository texts (`edits.json`, one Markdown file each) | each anchor occurs exactly once at its turn |
| `notion/` | the control-page edits (`edits.json`), the Candidate CRD Items List migration (`M2.json`), the Notion worker's notes | each `old_str` occurs once on the page as fetched |
| `dryrun/pass1/` | the rule-level dry run, 7 batches | all 51 bodies passed after the data fixes now in the engine |
| `dryrun/pass2/` | the complete dry run, 6 batches: per-body engine output and batch reports | 56 of 56 pass (50 live, 5 untouched live, the proposed MGMT-10 body) |
| `dryrun/pass3/` | the landing rehearsal: `land.py plan --no-ops` on the 51 bodies with edits, `land.py check` on the 5 untouched, `graph_check.py --simulate`; `report.json`; `one.py`, the wrapper that ran each | 51/51 plan with no refusal, 5/5 check, graph check passes |
| `dryrun/pass4/` | the rehearsal after repair round 4, with the readback each landing will run (`landed_check`, P-76) and CL-40's URL filled in both modes (P-75); `report.json`; `one.py` | 51/51 plan with precheck and landed check passing, CL-40 included; 5/5 check; graph check passes; 0 refusals |
| `dryrun/pass5/` | the rehearsal after repair round 5: pass 4's runs plus, per plan body, the landing-state proof (P-88) on the same fetch; `report.json` (with the QA-10 finding and fix made during the pass); `one.py`, `run.sh` | 51/51 plan with `repair` `[]` and the state proof passing; 5/5 check; graph check passes; 0 refusals; 516 partial landings: 450 repaired exactly, 66 refused, 0 repaired wrongly |
| `dryrun/synthetic/` | `partial.py`, `partial.out.json`: every subset of CL-E-20's landing operations on synthetic text (no prompt body), planned and checked | every subset repaired exactly or refused; a doubled insertion fails `check` |

The builders in `registry/`, the skills' `results/` and `dryrun/pass3/one.py`, `dryrun/pass4/one.py`, `dryrun/pass5/one.py` and `dryrun/synthetic/partial.py` were run in the PLAN session's
scratchpad, and the paths they name are scratchpad paths. The files EXECUTE runs (`engine/`, `registry/nam002_live.py`) resolve the repository root
themselves.
