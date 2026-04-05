# D1 - Binding Content Check

Source file checked:
- audit/ops/hde-epic028/ops-02/codespaces_harness_binding.md

Required linkage elements and exact quoted proof lines:

1. Exact governed QA artifact path being bound
- "- Primary artifact: audit/qa/hde-epic028/checks/po-010/final_summary.txt"

2. Exact Codespaces context being claimed
- "- codespaces_env.CODESPACES: SET"
- "- executed_at_utc: 2026-04-05T17:36:31Z"
- "- repo_root: /workspaces/glow-hdengine-v2"
- "- repo_head: b8f361b7b6e304bc3b34fabf85dca96a6b03f32d"

3. Exact command or command family producing the bound artifact
- "## Command Family Used To Produce The Bound Artifact In This Session"
- "- python -c write final_summary baseline lines"
- "- python -c append po_001..po_009 recorded/blocked/missing status lines"

4. Exact repo root and repo commit tied to that Codespaces session
- "- repo_root: /workspaces/glow-hdengine-v2"
- "- repo_head: b8f361b7b6e304bc3b34fabf85dca96a6b03f32d"

5. Explicit non-claim boundaries
- "- This record does not rerun or recompute the full EPIC028 QA suite."
- "- This record does not claim canon drain completion."
- "- This record does not claim merge provenance."

Result:
- PASS: binding file contains all required linkage elements for the rerun-based path.
