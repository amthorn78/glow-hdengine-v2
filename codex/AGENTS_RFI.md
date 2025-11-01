# AGENTS_RFI (for Codex)

You cannot see outside this repository. Before drafting `/AGENTS.md`, answer these three prompts using only repo files:

**A) Purpose & outline**
1) In one sentence: what will you use AGENTS.md for here?
2) List the section headings you want (≤ 10 lines, bullets).

**B) Repo-only inputs**
3) Which repo files/commands will you rely on (e.g., pyproject for hdctl, Makefile targets, scripts, presenter/emitter import path, audit/EVIDENCE_INDEX.jsonl)? List exact paths/commands.

**C) QA targeting**
4) What base-URL variable should AGENTS.md mention for smoke (name + default), and how will you select a JSON success endpoint for A7 using only files in this repo?

---

**Codex: put your answers below this line.**
A1) I will use AGENTS.md to brief future agents on Glow HD Engine-specific workflows, guardrails, and verification steps distilled from the repo’s internal docs and scripts.
A2)
- Repository scope & invariants
- Environment & configuration
- Service entrypoints & commands
- QA / acceptance expectations
- Evidence & artifact locations
- Coding patterns & style cues
- Support files & escalation

B3)
- README.md (project overview, environment variables, acceptance expectations)
- docs/server/reader_v1.md (route behavior & gating)
- docs/CLI_commands.md (API usage notes)
- docs/alpha_acceptance.md (card requirements)
- engine/http/compat_handler.py (compat endpoint behavior)
- scripts/architecture_capture.sh (smoke curl example & env defaults)
- VERIFY.sh (reader smoke command)
- requirements.txt & requirements-dev.txt (tooling context)
- pyproject.toml (package + tooling targets)
- artifacts/cards/ (evidence structure for QA references)

C4) Reference the `HDE_BASE_URL` variable defaulting to `http://127.0.0.1:5000` per scripts/architecture_capture.sh, and cite GET `/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo` as the JSON success smoke endpoint drawn from VERIFY.sh, with docs/server/reader_v1.md confirming the GET /api/reader contract in the APP_ENV=dev harness.

AGENTS.md Outline:
1. Repository scope & invariants
2. Environment & configuration
3. Service entrypoints & commands
4. QA / acceptance expectations
5. Evidence & artifact locations
6. Coding patterns & style cues
7. Support files & escalation
