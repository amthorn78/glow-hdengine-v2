2 distinct confirmed REQUIRED findings.

# REVIEW-ANALYZE-1-B — ANALYZE of MODIFICATION-20261011-gcfpe-mb008-to-promotion, full review 1 of 2

Reviewer: REVIEWER-ANALYZE-1-B, fresh context, brief `BRIEF-ANALYZE-1-B.md` at commit `5fbfeede`. Reviewed: commit `978d233e228bc88c77bbc8148117da7c2613c02d`, the record's §A and frontmatter and its evidence directory. Date: 2026-10-11.

**Answer.** The analysis's measurements reproduce: closure, both builds, the contract probe, the 13 digests, the validator, and a fresh 11-page sample of the body scan. Two defects in the analysis's own text are required.

- **B-1 (R1).** The analysis treats PF10 addendum 2.1 as forbidding all of the parent's F07 advice. Rule 3 forbids only model, reasoning-level and effort recommendations. The addendum's superseded-passages table keeps "Advice on execution surface ... unchanged". PF04 §9.1.3 therefore still requires surface advice for every GCFPE downstream-session prompt. The record's scope silently drops that half of F07 and classifies the existing surface-advice bans as "compatible".
- **B-2 (R3).** Under the recommended DN-B option B2, sessions run the TypeSafe skill "as built". As built, the skill updates rows and pastes the reading into the prompt header. B2 pairs that with a destination rule allowing only row creation, and the analysis places the reading beside the block, not in it. Adopted as written, B2 directs writes and placements that its own rule and D23-B forbid, and nothing would catch them at runtime.

The other claims hold, with listed caveats. Neither required finding is in text a repair added, because this is round 1 and there has been no repair.

## REQUIRED findings

### B-1 — R1: the execution-surface half of F07 is dropped; surface-advice bans are classed "compatible"

- **Exact text.**
  - §A.6 A-1: "The parent's F07 redline, an agent-written 'suitable surface, model and reasoning setting', is now forbidden (rule 3)."
  - §A.3: "rule 3 forbids exactly that".
  - `scope-measurement.md` §2a:
    - change-flow `SKILL.md:301`, disposition "Keep the route/gate/AI-recommendation ban; require the reading". That line also bans "capability appraisal" and "eligibility/suitability/account check".
    - flowmaster-validate `validate_flowmaster.py:359–366`, forbidden phrase "surface/model/reasoning recommendation", disposition "Compatible (rule 3)".
    - governance audit `epic-reengineering-interoperability.md:54–56`, "surface/model/reasoning advice … rule 3 forbids the advice".
  - Claim C1: "PF10 addendum 2.1 governs F07 and supersedes the parent's F07 redline".
- **Evidence.**
  - PF10 v13.5.2, addendum 2.1, rule 3: "No agent gives its own recommendation, assessment or ranking of model, reasoning level or effort". Surface is not named.
  - Its superseded-passages table, against the PF04 §9.1.3 sentence: "For the GCFPE, advice on model and reasoning level is replaced by rules 2 to 4. Advice on execution surface is unchanged."
  - PF04 §9.1.3 on `main`: "Every downstream-session prompt must receive task-specific human advice for execution surface, model and reasoning level …".
  - The parent's `findings.md` F07 is about surface, model and reasoning advice together.
  - The record's own §2 table says "Surface advice is unchanged", but no item, decision, risk or disposition follows from it.
  - Nothing in ITEM-03, PART-02 or DN-A to DN-F carries a surface-advice requirement.
- **Path.** Normal path.
- **Likelihood.** High. PLAN takes its operations from these dispositions, and they say to keep the bans.
- **Consequence.**
  - The promoted release gives the reading but no execution-surface advice, which PF04 §9.1.3 still requires.
  - Repaired skills and the validator keep forbidding "surface … recommendation" and "capability appraisal".
  - F07 is reported closed while that canon conflict carries on, and nobody is told.
- **Smallest correction.**
  - In A-1, C1 and §2a, separate surface from model and reasoning. Rule 3 forbids the model, reasoning and effort parts of the parent's F07 redline. Its execution-surface part still stands under PF04 §9.1.3, as PF10 2.1 leaves it.
  - Measure where surface advice is suppressed: change-flow `:301`, `validate_flowmaster.py:364`, the bodies' and PE's exclusions.
  - Carry it in ITEM-03's scope as surface advice beside the handoff, separate from the reading, with no model or effort content. Canon answers this, so no Product Owner question is needed.
- **In text the last repair added?** No. This is round 1.

### B-2 — R3: DN-B option B2 ("runs the skill as built") requires writes and a placement that its own D28 and D23-B forbid

- **Exact text.** §A.7 DN-B: "**B2, recommended:** each handoff-emitting session runs the skill as built, including its uses-table row, and the row carries your pick when you give it. It needs a narrow destination rule, D28: GCFPE flow prompts may create rows in that one data source and nothing else, recorded before EXECUTE (`notion-write-boundary.md`)."
- **Evidence.** The installed `typesafe-scoring/SKILL.md` has freeze digest `3 088c77f3…`, which I reproduced.
  - Step 3: "Paste the printed header line into the prompt's header under **Model and reasoning setting**." In GCFPE the prompt is the `NEXT_PROMPT_HANDOFF` block.
  - Step 4: "Create or update the row … if they do not, correct the row".
  - Step 5: "When Nathan picks, set *Nathan's pick*".
  - Against those steps:
    - D28 as proposed allows only row creation, so the update, correction and pick-setting writes fall outside it.
    - `notion-write-boundary.md` allows Notion writes "Only on explicit task-level authorization, or an explicit established destination rule".
    - D25 records that destination rules "have no check that fires".
    - A-1 puts the reading beside the block, "not in it". D23-B limits what the block carries, and the 23 in-block prohibitions keep model and reasoning content out of it.
- **Path.**
  - Normal path: recording Nathan's pick, and re-scoring a re-entered session.
  - Failure path: a readback mismatch, which step 4 itself anticipates.
- **Likelihood.** Medium if B2 is adopted. B2 is the recommendation.
- **Consequence.** A runtime session can follow B2 to the letter in either of two ways, and neither is caught:
  - It updates rows beyond D28, a silent breach of the rule this option asks Nathan to make and of the write boundary.
  - It never records the pick, so PF10 2.1 rule 2 ("the pick is recorded with the reading") goes unmet without anyone seeing it.

  Following step 3 as built also puts the reading inside the handoff block, against D23-B and against the analysis's own placement.
- **Smallest correction.**
  - Reword B2 to state the GCFPE use exactly: run the script; print the header line beside the block, not at step 3's header position; create the row.
  - Name who sets Nathan's pick.
  - Word D28 to cover exactly the writes that follow: create; correct after a failed readback; set Nathan's pick. Or state that Nathan sets the pick himself, and D28 covers create and correct only.
- **In text the last repair added?** No. This is round 1.

## LISTED findings

Each line gives path, likelihood and consequence. None is in text a repair added.

- **L-B1.** `interoperability-contracts.md:96` in the governance audit (the 091426.1 profile, "absence of … model/strength assessment, Analyzer, or configuration routing") is missing from §2a's "6 conflicting lines". It is built like `:56` and flowmaster-validate `SKILL.md:161`, which §2a counts. Normal path, medium likelihood; it survives PART-02 unless PLAN's own D26-E sweep finds it, and the audit then flags the reading (loud).
- **L-B2.** PE's sentence "The separate AF-013 skill advice is outside this candidate's implementation; no replacement scoring or new workflow is introduced." (under *GCFPE 100926.1 authoring requirements*, flagged by W2) was classed T6 and is not carried into §5 or A-1. Normal path, medium likelihood; after PART-02, PE says no scoring is introduced while requiring the reading.
- **L-B3.** PE's three T1 sentences and the adjacent exclusion sit under *Authoring and validation exclusion*, which holds generic Glow clauses. The parent's PE-2 calls them "generic Glow clause", and the D23 successor says PE's general rules also govern GTWPE. PF10 2.1 does not extend to other ecosystems. The record names "PE's authoring rules" without that boundary. Normal path, low-to-medium likelihood; an unscoped PLAN edit silently changes the rules TW prompts are authored under.
- **L-B4.** "Beside the block" has no defined position. C-PLACE's second sentence limits the lines before the block to "naming what was produced and where". `session-working-rules.md` §2 puts the state line immediately before the block, and four bodies put `ASK OK?` there (RS-30, fresh read). None of these is named as a surface. Normal path, medium likelihood; bodies whose instructions disagree.
- **L-B5.** ITEM-09 (MB-003, S3) is in scope without an opt-in. MB-010 is also S3 and also sits in a PART-02 section, yet it is offered as DN-A2 with "no" recommended. PART-06 calls the reference "non-operative" (Tier 0, class C), while §2a says "rule 3 forbids the advice". The scope reasoning is inconsistent but not silent, because ITEM-09 is visible in the items list.
- **L-B6.** ITEM-04 takes MB-007's L-B1 "as it applies to GCFPE". MB-007's closing text asks for a Modification covering the affected ecosystems, and *Standards and preservation* is a generic PE section. The record does not say how a GCFPE-only edit is scoped, or that MB-007 stays open. Normal path, low likelihood.
- **L-B7.** PART-05 is classed B, but D20-B calls a MGMT-10 rewrite "Class A", and D20 says "It authorizes no implementation … the Class A prompt rewrite needs [its own authorization] most". DN-C supplies Nathan's authorization, so the label is wrong but nothing breaches silently.
- **L-B8.** DN-C's recommended option A goes further than PF10 2.1 needs; option B is the minimal application. A promotes the D20 redesign, which the parent's L01 calls "related existing work, not implicit runtime-candidate selection". The testing body's 2026-09-24 revision post-dates Nathan's 2026-09-22 testing approval. Nathan decides, so it is not silent.
- **L-B9.** D2's waiver of MGMT-10's "does not execute … promotion" has nowhere to be recorded. `promotion` is not in `modification_validate.py`'s `OVERRIDABLE` list, so an `override` naming it fails validation. The record does not say where the waiver goes. Loud.
- **L-B10.** F06 was measured at contract level only: §9 says "No validator ran over prompt bodies". Body-level profile expectations are therefore unmeasured, for example `PROMPT_ROUTE_SEMANTICS` and `PROMPT_BODY_IDENTITY`. A-3 names one value-table entry with "such as"; it does not enumerate them. Yet §8 says "No unmeasured scope … bounded by the value-table entries named there". Normal path, medium likelihood; PLAN finds more F06 work than estimated.
- **L-B11.** §2a does not disposition the contract's `prohibited_active_routing` (`MODEL_OR_STRENGTH_ASSESSMENT`, `REASONING_RECOMMENDATION`) or the validator's `EXPECTED_PROHIBITED_ROUTING` against PF10 2.1. They are probably compatible as routing bans, but the record does not say so. Low likelihood.
- **L-B12.** §8 says "Moving PART-02 … shares all five packages". session-relay-flowmaster is changed only by PART-02. The conclusion that no install is saved still holds.
- **L-B13.** `targets` lists `tool` (PART-01, PART-07) but names no repository tool. `modification_validate.py` defines `tool` as a repository script with its lock file and selftest. Cosmetic.
- **L-B14.** PART-03 is Tier 1. The redesign's §3.4 table puts "one rule reaching many prompts" at Tier 2, and here one rule reaches 14 bodies and PE, above D26-F's ten-body trigger. No consequence: the Modification is Tier 2, and PART-07 runs the full gate.
- **L-B15.** A-6 reports that the selected 091426.1 release conflicts with PF10 2.1, but asks Nathan nothing about the interim. PF04 §9.1.2 says to report and stop the affected work. Low likelihood; no harm while 091426.1 sessions give no model guidance at all.
- **L-B16.** Neither B3 nor B2 as worded says whether the reading is written to the producing session's output artifact (C-ART, D23-A). Under B3 the response carries the only copy. Low likelihood.
- **L-B17.** Nothing says whether rule 1 ("every … downstream-session prompt") or PF04 §9.1.3 asks anything for members entered without a handoff. Those are MGR-10, UTIL-10, PR-50 (Nathan's abort invocation) and GCFPE-MGMT-10, from the candidate parts. This is a question, not a defect.
- **L-B18.** `execution-and-delegation-model.md` pins "Model: Opus, for every parallel agent". §2a does not disposition this against PF10 2.1, though it is probably outside rule 1's scope because workers are not sessions. §9 says the workers inherited their model, a deviation from that control with no reason given. Low likelihood.

## Questions for PLAN, not findings

The brief places these outside ANALYZE: TypeSafe fit, the promotion transaction, package builds.

- The typesafe-scoring v6 request and action text are worded for "Glow app session" coding sessions. Its credential is attached by the Glow app environment. How GCFPE planning, QA-authoring and closure sessions get readings that are not routinely "not read" (A-8) is open.
- Under D2, which session executes PART-08, and how do D26-C post-merge checkpoints apply across the promotion pull request?

## Claims, in short

| Claim | Verdict |
|---|---|
| C1 | **Partly refuted.** The reach to 53 bodies, PE and the 5 skills is confirmed. "Supersedes the parent's F07 redline" holds for model and reasoning only (B-1). |
| C2 | Holds for D23-B and the in-block prohibitions. PR-50's exception holds. Placement is under-specified (L-B4). |
| C3 | Holds on the 11 pages I re-read fresh: no missed T1/T3/T4/N1 text, and every count and quote I checked matches. Surface-advice classification as in B-1. L-B2 omitted. |
| C4 | Defensible by "scope by rule" (ecosystem-change-management §1, D21-B) and by MB-003's own handling text. The reasoning is inconsistent (L-B5, L-B6). |
| C5 | Reproduced. The value-table claim holds: `VALUE_TABLE` and `EXPECTED_RECEIVERS` both pin `PR-20.accepted_inputs` to `["PR_INSTRUCTION", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"]`, while the candidate parts carry RS-20 → PR-20 (F09). L-B10 applies. |
| C6 | Cost 6+2+2+1+6+2 = 19 checks, range 22. Closure union reproduced. L-B7 and L-B14 apply. |
| C7 | **Refuted for B2** (B-2). D2 and DN-C as L-B8 and L-B9. |
| C8 | Holds. Minimal excerpts are kept, and the seven transient files are disclosed. |

## What I reproduced, in scratch outside the repository, with `PYTHONDONTWRITEBYTECODE=1`

- **Closure.** 55 `closure.py` calls over the candidate parts at `978d233e`, all exit 0. The union is upstream 52, downstream 51, state_sharers 44, equal to the frontmatter.
- **Builds.** Installed graph_parts.py, candidate parts: 55 nodes, 237 edges, 596,008 B, `ff296b1e…`. Selected parts: 229 edges, `ae2bd159…`.
- **Contract.** The recipe with `--contract-revision 4.1.1 --primary-skill-revision 1.3.1`:
  - selected: EQUAL against both bundled contracts;
  - candidate: 633,702 B, `8e1c169e…`.
- **Probe.** `validate_graph_contract` and `validate_contract` from flowmaster-validate 3.3.2:
  - control: 0 graph errors and 0 contract errors;
  - candidate: 4 graph errors (`GRAPH_BASELINE_PROFILE`, `GRAPH_CANDIDATE_PROFILE`, `GRAPH_IDENTITY`, `GRAPH_PROOFS`) and 58 contract errors (`MEMBER_BINDING` 55, `PF10_ADDENDUM_CONTRACT` 1, `PRODUCTION_SELECTION_EVIDENCE` 1, `ROUTING_SURFACE_CHANGED` 1).
- **Digests.** `freeze.py` over all 13 installed skills reproduces every digest in `source-identities.md`.
- **Validator.** `modification_validate.py`: 16/16 records pass.

## Reads, and D22

- **Repository.** Read with `git show` at `978d233e` and `origin/main` `9312add2`.
- **Notion, 14 pages, all one fetch each, all returned inline.**
  - The MGMT-10 testing body `3e34590a…`, last edited 2026-09-24T11:00:24.691Z.
  - The backlog `3e54590a…`, 2026-10-11T13:33:28.036Z.
  - The candidate catalog `3f44590a…9abc`, 2026-10-11T19:47:45.856Z.
  - Eleven candidate pages, each at the `page_last_edited_at` recorded in `body-scan.json`: UTIL-10, IA-60, QA-90, MGR-10, ESC-25, CF-PO-10, CL-E-30, DOC-20, RS-30, CL-20, CF-C-30.
- **D22.** No tool-results file was created. No prompt body was copied, hashed or byte-compared. The scratchpad held copies of three installed skills, the candidate graph parts, the built graphs, the contracts and a probe script. None of these is a prompt body.

**Canon relied on:**
- AGENTS.md
- PF10-HDE-Build-Notes v13.5.2, complete, addendum 2.1
- PF04-Canon-HDE-Governance v2.8.7 §9.1.2, §9.1.3, §9.1.6
- PF06-Canon-Change-Process-Guide v2.5.4 §0.1A
- PF27-Canon-Plan-Templates v2.0.5, *Canon precedence for template use*
- Repository controls:
  - `gcfpe.decision-record.md` D17, D20–D27
  - `ecosystem-change-management.md`, `modification-template.md`, `modification_validate.py`
  - `notion-write-boundary.md`, `prompt-corpus-policy.md`, `session-working-rules.md`, `execution-and-delegation-model.md`, `authoritative-surfaces.md`, `postflight-procedure.md`
  - the redesign analysis §3.4
- The C-PLACE and C-NOTION texts in `MODIFICATION-20260923-alpha-feedback-open-entries` §P
- The GCFPE-MGMT-10 testing body: the spine, `MODE = ANALYZE`, result routing

NOTHING NEEDED from Nathan yet. Under D26-A the author repairs B-1 and B-2, and one DIFF_CHECK follows.
