# Evidence — recovery analysis, 2026-09-24

The raw returns behind `../RECOVERY-ANALYSIS-20260924.md`, committed as the agents returned them. One
workflow run, `wf_5818bab7-52e`, 2026-09-24: seven agents in one pass, 1.36M subagent tokens, 32 minutes.

| File | Agent | What it holds |
|---|---|---|
| `read_live.json` | reader | every live change the Alpha Feedback Modification made, by unit; what verified it and what did not; the freeze point; the pre-change baseline |
| `verify_live.json` | refute-by-default checker | its checks of `read_live.json`, with corrections |
| `read_defects.json` | reader | 48 known open defects: origin, significance, mechanism, comparison with 09-23, smallest fix |
| `verify_defects.json` | refute-by-default checker | its checks of `read_defects.json`. **Its corrected significance counts govern:** material 0, credible risk 5, low impact 31, no runtime effect 12 |
| `read_plan.json` | reader | the stopped plan split into content, normal path and machinery; §3 stability; salvage; a minimal execution design; per-round convergence |
| `verify_plan.json` | refute-by-default checker | its checks of `read_plan.json`, with the per-round counts recomputed from the RCA's CSV |
| `read_process.json` | reader | the governing rules behind the loops, every review loop of the day, model configuration, and stopping-rule candidates. Not separately checked; the analysis marks its inferences |
| `workflow-script.js` | — | the exact prompts and schemas the agents were given, committed so the briefs are on record |

**Constraints the agents ran under:** read-only; no git state changes; no prompt body fetched from Notion.
They quote skill and record text in short fragments only. Every agent's scratch files were outside the
repository.
