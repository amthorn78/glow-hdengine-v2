---
artifact_type: PRODUCT_OWNER_DISPOSITION
artifact_id: HDE-CRD-0002-WU-DOC-01-PO-DISPOSITION-DOC20-CORRECTION
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
DOCUMENTATION_UNIT_ID: WU-DOC-01
decision_owner: Nathan / Product Owner
decided_at: 2026-10-22, in the whole-change Implementation Agent session below (recorded 2026-10-22T03:46:30Z)
recorded_by: the whole-change HDE-CRD-0002 Implementation Agent, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N). This IA records the decision; the decision is the Product Owner's
decides: the decision returned by docs/ephemeral/HDE-CRD-0002-WU-DOC-01-documentation-completion-v1.0.md §8 (DOC-20, INCOMPLETE; findings DC-1 and DC-2)
approved_base_affected: none. The Specification, Implementation Plan v1.1 and Plan delta 01 v1.1 are unchanged. WU-DOC-01's scope stays Plan v1.1 §7 as P-8 amends it
repository_head_read: origin/main 8187254 (#696)
pf10_addendum_created: none
---

# HDE-CRD-0002 WU-DOC-01 — Product Owner disposition: DOC-20 correction route (v1.0)

## 1. Product Owner's words (verbatim)

> "authorize DOC-10 for instruction v1.1, give me the handoff"

## 2. Decision

**DOC-10 issues WU-DOC-01's PR instruction v1.1.** That instruction is the start of one bounded corrective documentation pass, plan cycle 3, covering findings DC-1 and DC-2 of the DOC-20 record (§6, the "Correction (bounded)" rows):

| Finding | Sentences | Correction |
| :- | :- | :- |
| DC-1 | `README.md:13`, `AGENTS.md:143`, `CHANGELOG.md:7` | Scope the close-pack nonclaim to the HDE-CRD-0002 writer: no close pack, candidate source or close-run family has been produced with it or under schema v2. Legacy Epic close packs in `audit/` stay unmentioned or stay true |
| DC-2 | `docs/ADAPTER_009.md:48` | The HTTP adapter reads neither `ENGINE_TAG` nor `RELEASE_ID` from the environment. The vendor client reads `RELEASE_ID` from the environment for its `User-Agent` when no release identity is passed |

**Bounds:**
- nothing else in the ten documents reopens;
- the accepted lineage (#692, #695; review v2.0) stays accepted-final;
- instruction v1.0 is preserved, and v1.1 is a complete successor.

## 3. Effect

- **Next stage:** DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, run by the whole-change Implementation Agent. It produces `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.1.md`.
- **After DOC-10:** PR-20 (plan cycle 3) in a new dedicated session; the Product Owner's Proceed; PR-30; PR-35; Nathan's merge; PR-40; then DOC-20 again.
- **Unchanged:**
  - WU-OPS-01's business case is due before OPS-10 (Product Owner);
  - QA-10 waits for documentation `COMPLETE` and WU-OPS-01;
  - RF-11, RF-1 to RF-10 and the carried items keep their owners.
- **Not decided here:** the instruction's text, the documentation wording, QA, Ops, acceptance and closure.

## 4. TypeSafe reading for the receiving session (DOC-10, instruction v1.1)

Action sent (v8.2): "Write, as the whole-change implementation agent, version 1.1 of an existing final repository-documentation instruction, adding one bounded corrective pass after a completion verification found four inaccurate sentences on merged main: a close-pack nonclaim stated too broadly in three Markdown documents (README, CHANGELOG and the agent-instructions file) and one sentence in an operator document that says an environment variable is not read when a vendor client does read it. The verification record already gives each sentence's line, the controlling code and the bounded correction; the instruction re-measures them at its head, keeps everything else in the unit closed, and sets scope, exclusions, validation and the planning destination. It is a Markdown record only: no code and no live run; a detailed plan, a Product Owner Proceed, implementation, CI, a lineage review and a repeated completion verification follow."

- **TypeSafe v8.2: Opus 5.5 at medium.**
  - Effort score 1.43 (confidence 0.69). Rung probabilities: low 0.03, medium 0.56, high 0.38, extra high 0.03, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.85, Sonnet 5.5 0.14, Haiku 5.5 0.00 (confidence 0.80).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.006, Fable 5.1 at high 0.004, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.025, Opus 5.5 at medium 0.476, Opus 5.5 at high 0.323, Opus 5.5 at extra high 0.025, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.004, Sonnet 5.5 at medium 0.078, Sonnet 5.5 at high 0.053, Sonnet 5.5 at extra high 0.004, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Flags: boundary between high and medium.
  - Sent 2026-10-22T03:46:01Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T03:46:01Z; HTTP 200 in 0.63 s; 5518 input and 71 output tokens; jev-1.13.0. Rung by rule: medium (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for DOC-10 is not stated.

**Surface advice:** run DOC-10 in the continuing whole-change HDE-CRD-0002 Implementation Agent session on `amthorn78/glow-hdengine-v2` (this one, or a top-level session Nathan creates for that role), with Notion read access for the prompt.
- **Environment:** git and a read of `main`; a CPython 3.12 venv with CI's install only if the instruction re-measures tool behaviour; closed rails.
- **Access:** no live vendor, production or database access.
- **Order:** this record's pull request should be merged first.

## Canon relied on

Read on `main` at `8187254`; PF10 is v13.7.4.

| Topic | Sources and sections |
| :- | :- |
| The decision returned and its route | DOC-20 — Verify Final Repository Documentation Completion — 100926.1, "Result routing", read in full in this session; the DOC-20 record §8 |
| Accepted lineage stays final | PR-40 — Review PR Work-Unit Lineage — 100926.1, "Accepted-final lineage protection" |
| Next stage | DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, read in full in this session ("Role and native purpose": one final repository-documentation `PR_INSTRUCTION`) |
| Business case and measure unchanged | PF10 addendum 2.18; the disposition record `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md` §2 |
