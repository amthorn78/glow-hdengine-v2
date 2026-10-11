# Scope measurement — MB-008 ANALYZE — 2026-10-11

Method throughout: broad match over the whole surface, minus named permitted exceptions, with the remainder read in context (`SCOPE-001`, `D26-E`). Skill lines are from the installed trees in `source-identities.md`. Prompt-body results are from `body-scan.json`. Line numbers are 1-based.

## 1. Packages — F02, F04, F05 (package side)

Broad match over change-flow, flowmaster-validate and glow-hde-pr-development (`*.md`, `*.py`), excluding the bundled historical contracts (`references/gcfpe-2026091[23]*`) and the R1 runtime map.

| Finding | Regex | In-scope lines | Permitted exceptions |
|---|---|---|---|
| F02 executor | `kronos…(execut|operator)`, `different (operator|executor)`, `another authorized operator`, `not kronos` | change-flow `SKILL.md:385` `KRONOS_NEVER_EXECUTES_OPS_OR_QA`; `:554–555` `KRONOS_EXECUTES_OPS/QA is prohibited`; `:483` GCF-23 "authorized operator execution". flowmaster-validate `SKILL.md:299`, `:358–359`; `validate_flowmaster.py:155`, `:333–334`, `:1753–1759` (role findings) | `change-flow/SKILL.md:263` (manager substitution); fixture names in `validate_epic_alpha.py`, `run_strength_middleware_fixtures.py` |
| F02 contract value | `member_registry.QA-100.receiving_role` | regenerated from the candidate graph by the shipped recipe (§3); no hand edit | — |
| F04 IA-40 | `IA-40 (remains|only)`, `not IA-40` | change-flow `SKILL.md:379` ("through IA-40 only while the Plan is pending preapproval") | `:487` (bounded overlay; consistent) |
| F05 numbering | `numbering`, `numbers the`, `allocat… (canon|pf10)`, `producer_allocates` | change-flow `SKILL.md:323` ("The producer does not … allocate canon numbering … The Product Owner pastes and numbers the addendum"); glow-hde-pr-development `SKILL.md:147` ("select final PF10 numbering … the Product Owner pastes and numbers it"); flowmaster-validate `validate_gcfpe_20260914.py:1715` (asserts `producer_allocates_pf10_number: False`), `:1356` (graph/contract agreement) | change-flow `SKILL.md:471` (QA-10, a nonproducer, about itself); `validate_gcfpe_current.py:323` (historical profile); `:420`/`:551` key-name lists |

## 2. PF10 addendum 2.1 — the TypeSafe reading

### 2a. Skills

Broad match: `model|models|reasoning|effort|strength|advice|advise|advisory|recommend*|typesafe|Analyzer` over 13 installed skills. Raw counts: change-flow 28, flowmaster-validate 56, glow-hde-pr-development 10, session-relay-flowmaster 32, amthor-workspace-governance-audit 29, tw-flowmaster 34, flowmaster-primary 4, glow-po-reporting 6, session-branch-flowmaster 4, glow-graph-contract 5. Exceptions: data/state/fixture "model"; `ADVISORY` severity; "recommendation" for decisions, routes or relay outcomes; historical correction filenames (`strength-analyzer-middleware-correction.json`); code-comment "reasoning"; tw-flowmaster (GTWPE, outside 2.1's scope).

| Skill | Line | Text, shortened | Disposition under 2.1 |
|---|---|---|---|
| change-flow | `SKILL.md:301` | "Do not create, require, recommend, or route through a model/strength assessment, reasoning recommendation, eligibility/suitability/account check, capability appraisal, …" | **Conflicts**: forbids the reading, and its "capability appraisal" and "eligibility/suitability" terms also suppress the surface advice PF04 §9.1.3 still requires. Keep the bans on routes, gates and an agent's own model or reasoning recommendation; require the reading and the surface advice |
| flowmaster-validate | `SKILL.md:161` | "Direct continuation has no model/strength assessment, Analyzer, reasoning recommendation, …" | **Conflicts** the same way |
| flowmaster-validate | `validate_flowmaster.py:359–366` | forbidden phrases "surface/model/reasoning recommendation", "eligible human recommendation" | **Partly conflicts**: the phrase at `:364` also forbids surface advice, which PF04 §9.1.3 keeps. The model and reasoning half matches rule 3. A required guard for the reading is missing |
| glow-hde-pr-development | `SKILL.md:184` | "Do not introduce model, strength, configuration, or reasoning-level assessment or routing." | **Conflicts** (assessment) |
| glow-hde-pr-development | `validate_glow_hde_pr_development.py:106–107` | forbids "recommend a model", "reasoning-level recommendation" | Compatible (rule 3) |
| session-relay-flowmaster | `SKILL.md:283` | "For GCFPE, no handoff, relay message or ledger carries a model/strength assessment, reasoning recommendation, …" | **Conflicts**: a relay is in 2.1's scope by name |
| amthor-workspace-governance-audit | `SKILL.md:41`; `references/interoperability-contracts.md:56` | "No operative prompt, … skill, or validator requires a model/strength assessment, …" | **Conflicts**: the audit would report the reading rule as a violation |
| amthor-workspace-governance-audit | `references/epic-reengineering-interoperability.md:54–56` | Analyzer, `MODEL_HANDOFF`, surface/model/reasoning advice | Retired Analyzer handoff content (MB-003). Its model and reasoning advice is what rule 3 forbids. Surface advice is carried by PART-02's rule, not by this reference |
| change-flow, flowmaster-validate | bundled contracts, `prohibited_references` | "model/strength/reasoning/eligibility/suitability/account/configuration route" | Compatible: a route, and the reading is no route |
| typesafe-scoring | `SKILL.md` description | "Score a Glow app session prompt …"; records a row in the Notion uses table | The tool 2.1 names; no change established. Its recording step meets the write boundary (DN-B) |
| flowmaster-primary, glow-po-reporting, session-branch-flowmaster, glow-graph-contract | — | no GCFPE model-guidance rule | Unaffected |

### 2a-bis. Texts the placement must keep (R-A1, round 1)

D23's canonical wording, from `MODIFICATION-20260923-alpha-feedback-open-entries` §P, constrains where the reading and the surface advice go:

| Text | Where it is restated | Under DN-B options 1 and 2 | Under option 3 |
|---|---|---|---|
| **C-PLACE**: "The final response ends with the `NEXT_PROMPT_HANDOFF` block. Anything before it is at most a few lines naming what was produced and where; the artifact holds the rest." | 53 candidate bodies and PE (the "handoff preamble" in §2b); change-flow `SKILL.md:299`; glow-hde-pr-development `SKILL.md:174`; session-relay-flowmaster `SKILL.md:285`; governance audit pin `SKILL.md:40` | Kept: the line before the block names the reading's cell, its flags and the artifact path | Amended by a D23 successor in every place listed |
| **C-ART**: "Before emitting any handoff, write every result this prompt produces … into its output artifact … it never carries the only copy of a fact." | the nonterminal bodies; glow-hde-pr-development `SKILL.md:170`; governance audit pin `SKILL.md:39` | Kept: the printed reading and the surface advice are written into the artifact | Kept |
| **D23-B**: the block's five contents | the bodies' *Mandatory single-block handoff*; the four skills above | Kept | Kept |

### 2b. Prompt bodies

56 pages: the 54 candidate runtime members, the reused GCFPE-MGMT-10 at 091426.1, and the PE successor. The brief's classes: T1 forbids guidance in general; T2 forbids it inside the handoff block only; T3 gives AI guidance; T4 names TypeSafe; T5 operator decision; T6 another sense.

| Measure | Result |
|---|---|
| Pages carrying the handoff preamble ("Anything before it is at most a few lines …") and the `NEXT_PROMPT_HANDOFF` literal | 54: the 53 candidate members other than PR-50, and PE |
| Members with handoff branches in the candidate graph | 54 (218 of 291 branches); PR-50 has none |
| T4 TypeSafe, T3 AI guidance given | 0 and 0 on all 56 pages |
| T1 general prohibitions | PR-10, PR-20, PR-30, PR-40 (one shared sentence each); PR-35 (1); PR-50 (2); PE (3, plus the adjacent exclusion "These subjects are outside this metaprompt and outside every prompt or handoff it creates or revises.") |
| T2 in-block prohibitions | 23 pages: 8 PR/OPS/QA-10 pages, 10 CF/MGR pages, 5 CL pages. The CL sentence opens "Do not include …" without naming the block |
| GCFPE-MGMT-10 091426.1 | no handoff preamble, no `NEXT_PROMPT_HANDOFF` literal, no T1–T5 text; graph shows 2 handoff branches; its conditional handoff names `PR-10 — … — 091426.1` (the predecessor page) |

Reach of rule 1, by function: every member that emits a handoff needs the reading for its receiving session, so 53 candidate bodies plus GCFPE-MGMT-10 (DN-C) and PE's authoring rules. PF04 §9.1.3's surface advice reaches the same bodies, and the same general prohibitions suppress it. Exceptions: PR-50 emits no handoff, and its two prohibitions forbid its own assessment, which rule 3 also forbids. Of the 23 T2 sentences, 18 stay valid as written and the 5 CL ones gain "in the block", because nothing about the reading or the advice goes inside the block.

## 3. F06 — candidate contract and profile

Commands, in scratch, from the installed trees:

```
graph_parts.py build <candidate parts> cand-graph.md        -> 237 edges, ff296b1e…
contract_recipe.py cand-graph.md <4.0.6 template> <R1 oracle 20260923> <decision record> cand-contract.json \
    --contract-revision 4.1.1 --primary-skill-revision 1.3.1  -> exit 0, 633,702 B, 8e1c169e…
validate_gcfpe_20260914.validate_graph_contract / validate_contract  (flowmaster-validate 3.3.2)
```

Results in `contract-probe.json`. Control: the selected build with the shipped contract returns 0 and 0 errors. Candidate: 4 graph errors (`GRAPH_BASELINE_PROFILE`, `GRAPH_CANDIDATE_PROFILE`, `GRAPH_IDENTITY`, `GRAPH_PROOFS`) and 58 contract errors in 4 classes (`MEMBER_BINDING` ×55, `PF10_ADDENDUM_CONTRACT`, `PRODUCTION_SELECTION_EVIDENCE`, `ROUTING_SURFACE_CHANGED`). That is 62 091426.1-bound expectations in 8 classes. The revisions passed were the shipped ones, for the probe only.

Not covered by the probe: the regenerator's contract-only value table (`regenerate_contract.py`, `VALUE_TABLE`) holds 091426.1-era values, such as `receiver_compatibility["PR-20"].accepted_inputs` without F09's RS-20 pre-Proceed return. The validator pins those values exactly (`EXPECTED_RECEIVERS`). So glow-graph-contract probably changes too; PLAN confirms.

## 4. F05 surviving body text (`D26-E`)

Broad match over 56 pages for `numbering`, or `number` together with `PF10` or `addendum`. Exceptions: a nonproducer about itself (N2, 21 sentences); the producer rule (N3).

| Sentence | Pages |
|---|---|
| "No agent edits PF10, allocates PF10 numbering, or claims canonical adoption." | OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-40, PR-50, QA-10 |
| "The producer never edits PF10, allocates PF10 numbering, or claims canonical adoption." | CL-20, CL-30, CL-40, CL-C-10, CL-E-10 |
| "Preparing a standalone PF10 addendum does not authorize live PF10 inspection, numbering, insertion, canon adoption, or repository publication." | PE, *Standards and preservation* (MB-007's L-B1, as it applies to GCFPE) |

The parent's guard G-F05-A ran on seven producer rows and PE only, so these 14 member pages were never checked (the parent's listed risk P2-6).

## 5. Outside MB-008, recorded for the backlog

"Each handoff carries the complete native input package, exact artifact and version lineage, session identity, manual prerequisites, recovery context and result-specific terminal behavior." This is in PR-10, PR-20, PR-30 and PR-40, under *Managed entry, execution posture and continuing identity*. It contradicts `D23-B` and the same pages' *Mandatory single-block handoff* section, which governs the block. It is S3, and it is proposed as backlog entry MB-010.
