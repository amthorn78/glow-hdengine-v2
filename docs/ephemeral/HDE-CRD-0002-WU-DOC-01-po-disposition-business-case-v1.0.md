---
artifact_type: PRODUCT_OWNER_DISPOSITION
artifact_id: HDE-CRD-0002-WU-DOC-01-PO-DISPOSITION-BUSINESS-CASE
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
DOCUMENTATION_UNIT_ID: WU-DOC-01
decision_owner: Nathan / Product Owner
decided_at: 2026-10-22, in the whole-change Implementation Agent session below (recorded 2026-10-22T00:52:00Z)
recorded_by: the whole-change HDE-CRD-0002 Implementation Agent, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N); recorder and drafter of the adopted text; the decision is the Product Owner's
decides: the decision returned to the Product Owner by docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-work-unit-lineage-review-v1.0.md §10 (blob 0d841d3fd24e; landed by #688), recorded in PF10 addendum 2.20: WU-DOC-01's business case, due before DOC-10 (addendum 2.18, "Epic, task, and status effects")
approved_base_affected: none. The Specification, Implementation Plan v1.1 and Plan delta 01 v1.1 are unchanged; WU-DOC-01's scope is Plan v1.1 §7 as Plan delta 01 P-8 amends it
repository_head_read: origin/main aefb20c (PF10 v13.7.3)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.3.md (blob b39b6c0766a1; sha256 649602f3b1f391e4c7c6add3e978c361bc9cb49f3c311518fd9eaf50353f2f77). Read: the v13.7.1 → v13.7.3 diff (version lines, two index lines, addenda 2.19 and 2.20 appended), with 2.20 in full and 2.19 checked against its record; 2.18 in full earlier in this session
pf10_addendum_created: none
---

# HDE-CRD-0002 — Product Owner disposition: WU-DOC-01 business case (v1.0)

## 1. Product Owner's words (verbatim)

> "adopt the draft business case, give me the DOC-10 handoff"

"The draft business case" is the one in the WU-PR-08 lineage review §10, which PF10 addendum 2.20 restates under "Deferred obligations and unresolved work". It is reproduced in §2 without change.

## 2. Decision: the draft is adopted

### Business case for WU-DOC-01 (addendum 2.11 rule 1, as addendum 2.18 narrows it)

| Field | Content |
| :- | :- |
| Beneficiary | Agents and operators who take repository workflow from `AGENTS.md` and `README.md`. Every later PR session reads `AGENTS.md` |
| Evidence | Measured on `main` at `1a4c8ab` (lineage review §10): `README.md` does not mention `tools/ci/prepush_check.py`, the pre-push check WU-PR-06 delivered; `AGENTS.md` names only `schemas/epic_close_candidate_source.v1.json`, while WU-PR-07 delivered `schemas/close_candidate_source.v2.json`, which accepts CRD identities; `docs/EVIDENCE_INDEX.md` has no HDE-CRD-0002 entry; `CHANGELOG.md` has no HDE-CRD-0002 entry |
| Benefit | A session following `AGENTS.md` and `README.md` uses the tools HDE-CRD-0002 delivered (the pre-push check and the v2 close-pack source) rather than an outdated description |
| Measure | Each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20 |
| Cost ceiling | None (addendum 2.18 rule 1) |

The Product Owner's adoption answers the review's open question: whether this case meets addendum 2.11 rule 2 was his call, and he adopted it.

### Scope this business case covers

WU-DOC-01's scope is unchanged:
- Plan v1.1 §7 WU-DOC-01, with Plan delta 01 P-8's Bounded scope:
  - `README.md` (pre-push check usage; close-pack writer capability; test guidance);
  - `CHANGELOG.md`;
  - `AGENTS.md` operative passages;
  - `docs/EVIDENCE_INDEX.md`;
  - `docs/CLI_commands.md` final pass;
  - `docs/server/reader_v1.md`.
- The items earlier lineage reviews routed to WU-DOC-01, as the DOC-10 instruction resolves them (WU-PR-08 lineage review §8 and §10; addendum 2.20).

## 3. Effect

- **WU-DOC-01's prerequisite is met.** Its dependency ("Ninth; after WU-PR-08 merges") was met at #687. Its business case now exists. The next stage is DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, run by the whole-change Implementation Agent.
- **Unchanged:** WU-OPS-01's business case is still due before OPS-10 (addendum 2.18), owner the Product Owner.
- **Not decided here:** the instruction's content, the documentation wording, and any QA, Ops, acceptance or closure.

## 4. Open items and owners

| Item | Owner |
| :- | :- |
| WU-DOC-01's PR instruction | the whole-change Implementation Agent, DOC-10 |
| WU-OPS-01's business case, before OPS-10 | Product Owner |
| PR35-C1 and LR8-F1, later-change candidates (addendum 2.20) | Product Owner |
| The PF10 number of the Plan delta 01 approval addendum. Its record (`docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-PF10-build-notes-addendum-v1.0.md`) calls itself 2.19, but PF10 v13.7.3 gives 2.19 to the Specification delta 01 addendum and does not contain the Plan delta addendum. It is cited by title and record, so no decision here depends on its number | Product Owner |

## 5. TypeSafe reading for the receiving session (DOC-10, WU-DOC-01)

Action sent (v8.2): "Write, as the whole-change Implementation Agent, one new self-contained instruction for the final repository-documentation work unit of an approved change after its eight code units have been accepted: read the delivered code, tools and lineage reviews, and map each delivered requirement to the documentation change it needs across about six repository documents (README, CHANGELOG, the agent-instructions file's operative passages, an evidence-index guide, a CLI reference and a server note), plus about a dozen stale statements and carried items routed to this unit by earlier reviews, with its business case, scope, exclusions, baseline and acceptance. It is a Markdown record only: no code is written and no live run occurs; a detailed PR plan, a Product Owner Proceed, implementation, CI with an independent code review, a lineage review and a completion verification follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.95 (confidence 0.67); rung probabilities low 0.02, medium 0.23, high 0.53, extra high 0.20, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.57, Sonnet 5.5 0.42, Haiku 5.5 0.00 (confidence 0.43). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.005, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.011, Opus 5.5 at medium 0.131, Opus 5.5 at high 0.302, Opus 5.5 at extra high 0.114, Opus 5.5 at max 0.006, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.008, Sonnet 5.5 at medium 0.097, Sonnet 5.5 at high 0.223, Sonnet 5.5 at extra high 0.084, Sonnet 5.5 at max 0.004, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: model near tie between Opus 5.5 and Sonnet 5.5. Sent 2026-10-22T00:51:10Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T00:51:10Z; HTTP 200 in 0.77 s; 5508 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: model near tie between Opus 5.5 and Sonnet 5.5.
- **Which request.** The installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records.** The Notion row was not written. Nathan's pick for DOC-10 is not stated.

**Surface advice:** run DOC-10 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt, in the whole-change Implementation Agent role.
- **Reads from `main`:**
  - the lineage reviews of WU-PR-01 to WU-PR-08, for the items routed to WU-DOC-01;
  - Plan v1.1 with Plan delta 01;
  - the delivered tools and schemas (`tools/ci/prepush_check.py`, `tools/qa/generate_epic_close_pack.py`, `schemas/close_candidate_source.v2.json`, `tools/evidence/update_evidence_index.py`);
  - the six documents;
  - `docs/pfcanon/`.
- **Environment:** a Python 3.12 venv with CI's install, under closed rails (`env -i`), if the instruction measures tool help or behaviour.
- **Writes:** only the instruction under `docs/ephemeral/`.
- **Needs:** no live vendor, production or database access. This record's pull request should be merged first.

## Canon relied on

Read on `main` at `aefb20c`.

| Topic | Sources and sections |
| :- | :- |
| Business case fields and gates; no ceiling | PF10-HDE-Build-Notes v13.7.3 addendum 2.18, rules 1 to 3 and "Epic, task, and status effects" (WU-DOC-01's business case before DOC-10); addendum 2.11 rules 1 to 3 (rule 2: what is not a business case), read in full in this session |
| The decision returned and its draft | addendum 2.20, "Deferred obligations and unresolved work", read in full; the WU-PR-08 lineage review §10 (this session's own) |
| Next stage | PR-40 — Review PR Work-Unit Lineage — 100926.1, "Resolve the next approved Plan stage" (a final documentation unit without instructions goes to DOC-10); DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, read in full in this session ("Required inputs"; "Execute"; "Result routing"; handoff rules) |
| WU-DOC-01 scope and order | Implementation Plan v1.1 §7 WU-DOC-01; Plan delta 01 v1.1 P-8 (and its addendum record), read in full in this session |
| Prompt-use provenance | `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; usage recorded here only (DOC-10 "Native identity, source fidelity, and recovery") |
