---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-closeout-residuals
status: ANALYZED
targets: [prompt, skill, rule, graph, registry, notion_control]
gate_tier: 1
closure:
  upstream: [CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CF-PO-10, CL-20, CL-30, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, GCFPE-MGMT-10, IA-10, IA-20, IA-30, IA-40, IA-50, MGR-10, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-10, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30, RS-40]
  downstream: [CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CF-PO-10, CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, ESC-10, ESC-25, ESC-30, ESC-40, IA-10, IA-40, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-10, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30, RS-40]
  state_sharers: "union over the 48 touched prompts: 43 prompts; radius with the touched set: 55 of 55 (§A)"
readiness: READY
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 12
interaction_cost_actual:
items:
  - id: ITEM-01
    statement: "The RS-20 package that glow-hde-pr-development describes carries no lineage or evidence that the named artifacts already hold (D23-B)."
    source: "CLOSE-OUT-20260923 §4.A; glow-hde-pr-development/SKILL.md:143"
    disposition: ""
  - id: ITEM-02
    statement: "session-relay-flowmaster no longer tells a handoff to carry advice and identity that the named artifacts hold (D23-B)."
    source: "CLOSE-OUT-20260923 §4.A; session-relay-flowmaster/SKILL.md:281"
    disposition: ""
  - id: ITEM-03
    statement: "flowmaster-validate's guidance no longer describes a `Selection status` body header, which its own validator rejects."
    source: "CLOSE-OUT-20260923 §4.A; flowmaster-validate/SKILL.md:178"
    disposition: ""
  - id: ITEM-04
    statement: "flowmaster-validate's guidance and profile staging_rule no longer presume a complete local copy of the prompt corpus (D22)."
    source: "CLOSE-OUT-20260923 §4.A; flowmaster-validate/SKILL.md:382, :398, :402; profile staging_rule"
    disposition: ""
  - id: ITEM-05
    statement: "amthor-workspace-governance-audit no longer snapshots or hashes prompt bodies (D22)."
    source: "CLOSE-OUT-20260923 §4.A; amthor-workspace-governance-audit/SKILL.md:109-113, its description, references/report-contracts.md:39"
    disposition: ""
  - id: ITEM-06
    statement: "session-relay-flowmaster no longer hashes prompt bodies (D22)."
    source: "CLOSE-OUT-20260923 §4.A; session-relay-flowmaster/SKILL.md:378"
    disposition: ""
  - id: ITEM-07
    statement: "The governance-audit behavioral fixture no longer rejects the cross-session PR-30 to PR-35 route that D23-D made lawful."
    source: "CLOSE-OUT-20260923 §4.A; amthor-workspace-governance-audit/references/behavioral-fixtures.md:49"
    disposition: ""
  - id: ITEM-08
    statement: "GCFPE stage prompts are no longer pinned by prompt-body content hash: one GCFPE override sentence outside the byte-identical protected core, in change-flow and session-relay-flowmaster, pins them by stable ID, version and direct Notion URL (A1-6 pattern). The core, flowmaster-primary, session-branch-flowmaster and tw-flowmaster are unchanged."
    source: "CLOSE-OUT-20260923 §4.A; protected core :72, :122 in change-flow and session-relay-flowmaster; Nathan 2026-09-23 accepted the override recommendation"
    disposition: ""
  - id: ITEM-09
    statement: "glow-graph-contract states the post-D23 graph counts."
    source: "CLOSE-OUT-20260923 §4.A; glow-graph-contract/SKILL.md:13, :133-134"
    disposition: ""
  - id: ITEM-10
    statement: "change-flow no longer calls 091426.1 the collision-checked reserved successor."
    source: "CLOSE-OUT-20260923 §4.A (carried); change-flow/SKILL.md:280"
    disposition: ""
  - id: ITEM-11
    statement: "flowmaster-validate/scripts/validate_gcfpe_current.py fails closed with a named result, not a NameError, when --bodies-stdin is used with the historical schema-3.1 alias contract."
    source: "CLOSE-OUT-20260923 §4.A (carried); located by the ANALYZE verification in flowmaster-validate/scripts/validate_gcfpe_current.py:605 (change-flow has no copy)"
    disposition: ""
  - id: ITEM-12
    statement: "The graph's edge_indices bookkeeping matches its edges."
    source: "CLOSE-OUT-20260923 §4.A (carried)"
    disposition: ""
  - id: ITEM-13
    statement: "The contract regenerator and the registry deriver live in glow-graph-contract as maintained scripts, and the pre-E2 contract they need is kept in the repository, so the shipped contract regenerates byte for byte from repository sources."
    source: "CLOSE-OUT-20260923 §4.A (carried)"
    disposition: ""
  - id: ITEM-14
    statement: "session-relay-flowmaster no longer names Drive as the GCFPE artifact plane (D7): its text, its ARTIFACT_PLANE enum (with REPOSITORY), validate_relay_manifest.py, a self-test case and the manifest examples agree."
    source: "CLOSE-OUT-20260923 §4.A (carried); session-relay-flowmaster/SKILL.md:273, :358"
    disposition: ""
  - id: ITEM-15
    statement: "The five round-a5 non-blocking findings are repaired."
    source: "CLOSE-OUT-20260923 §4.A (carried); SECTION-10-REVIEW-a5-SFR-A5-1.md N1-N4, SECTION-10-REVIEW-a5-SFR-A5-2.md F1-F4"
    disposition: ""
  - id: ITEM-16
    statement: "D22 has guards that fire on regression: CONTRACT_REQUIRED holds ITEM-08's override sentence in change-flow and session-relay-flowmaster; CONTRACT_FORBIDDEN, or the owning skill's own suite, forbids every retired body-copying or body-hashing phrase this Modification removes from change-flow, session-relay-flowmaster, glow-hde-pr-development, flowmaster-validate and amthor-workspace-governance-audit; a governance-audit fixture proves prompt-kind sources carry no digest. tw-flowmaster is excluded (out of scope), and the residual limit, prose paraphrase, is recorded under D14."
    source: "CLOSE-OUT-20260923 §4.A (carried); gcfpe.decision-record.md D22 (GUARD-001)"
    disposition: ""
  - id: ITEM-17
    statement: "QA-10 no longer calls itself read-only while it saves three artifacts."
    source: "CLOSE-OUT-20260923 §4.E"
    disposition: ""
  - id: ITEM-18
    statement: "CL-40 names the store of the CRD candidate list it updates."
    source: "CLOSE-OUT-20260923 §4.E"
    disposition: ""
  - id: ITEM-19
    statement: "CL-20's board-update instruction names the board reference supplied by the change context, and records the update as pending with its PF04 §9.1.1 owner (the authorized manual operator and the actual receiving owners) when none is supplied."
    source: "CLOSE-OUT-20260923 §4.E"
    disposition: ""
  - id: ITEM-20
    statement: "OPS-10's and OPS-20's ban on page and file mentions says that it covers authored reusable text only, so it no longer reads as contradicting their own Notion URL line and the direct URL a handoff must carry."
    source: "CLOSE-OUT-20260923 §4.E"
    disposition: ""
  - id: ITEM-21
    statement: "The four CL-* bodies that cite a 'PR-40 merge-approval effect' describe instead how PR-40 is entered (MERGE_OBSERVED first, the merge assertion as fallback), and approve nothing."
    source: "CLOSE-OUT-20260923 §4.E"
    disposition: ""
  - id: ITEM-22
    statement: "The registry's lane notion_parent_id and row expected_parent_id values name each prompt's actual 091426.1 parent page, so the governance audit's parent check (NAM-002) holds."
    source: "CLOSE-OUT-20260923 §4.D; ESC-10's page sits under the 091426.1 Escalation hub 3db4590a05eb81cd938de84cfffead9c while its row expects 3c74590a05eb8123bc55ca7f99ce176c"
    disposition: ""
  - id: ITEM-23
    statement: "The unpromoted GCFPE-MGMT-10 PROPOSED BODY (D20 redesign) reserves no release-bound header line (D23-G), so it can be promoted without one."
    source: "CLOSE-OUT-20260923 §4.D; Notion page 3e34590a05eb811b93d2da9b4ef8106d, a child of the redesign tracking page"
    disposition: ""
  - id: ITEM-24
    statement: "When a maintenance or repair session's message to the Product Owner carries a NEXT_PROMPT_HANDOFF block, the named state (DECISION NEEDED / NOTHING NEEDED / IN FLIGHT) is the line immediately before the block, so the handoff-last ruling and the named-state rule agree in glow-po-reporting, the Hub worker communication rules and session-working-rules.md."
    source: "Product Owner ruling 2026-09-23 (a maintenance session's handoff goes last; gcfpe.decision-record.md D23 successor) against glow-po-reporting 'end in one of exactly three named states' and Hub 'Worker communication rules' §2"
    disposition: ""
  - id: ITEM-25
    statement: "glow-graph-contract says that the graph copies bundled in skills are validator fixtures built from docs/graph/parts, not sources."
    source: "Parent Modification Amendment 1 'Noticed, not in scope' (spec S-3); glow-graph-contract/SKILL.md:59"
    disposition: ""
  - id: ITEM-39
    statement: "No installed skill this Modification packages still states the retired D18 Alpha state (PR04 not started, Alpha stopped): flowmaster-validate/SKILL.md:174, amthor-workspace-governance-audit references/interoperability-contracts.md:96 and behavioral-fixtures.md:59."
    source: "ANALYZE completeness review, 2026-09-23; close-out §6 retired the D18 block (PR04 merged in #467 and accepted)"
    disposition: ""
  - id: ITEM-26
    statement: "No body's routing, recovery or package sentence tells a handoff to carry lineage, decisions, completed work, evidence, a branch or commit, or other content its named artifacts hold; each such sentence names the artifacts instead (C-HANDOFF, D23-B)."
    source: "ANALYZE body sweep and adversarial re-check: HANDOFF_RESTATES_CONTENT, 123 REAL findings in 46 bodies (evidence/closeout-residuals/ANALYZE-body-evidence.md)"
    disposition: ""
  - id: ITEM-27
    statement: "The shared sentences that keep the CANON_CONFLICT_REGISTER, GCFPE_PROMPT_USES entries and usage mappings 'in the artifact … or the handoff' keep them in the output artifact only; the handoff names that artifact (C-ART)."
    source: "ANALYZE re-check, findings added by the verifiers in CL-*, OPS-*, PR-*, QA-10, QA-120 and the RS lane"
    disposition: ""
  - id: ITEM-28
    statement: "A registry guard (D14) fails when any retired handoff-content phrasing, branch or commit carriage, or 'or the handoff' storage clause returns to a body, each proven by an injected must-fail regression."
    source: "The parent's E4 gate passed every body ITEM-26 names (0 of 1 484 assertions); a guard that never fired is not a guard (GUARD-001)"
    disposition: ""
  - id: ITEM-29
    statement: "Every body that describes how PR-40 is entered uses the parent's A1-5 wording and the D23 once-per-merge sentence verbatim: the MERGE_OBSERVED handoff from PR-35 or RS-40 first, Nathan's merge assertion only where no MERGE_OBSERVED result was returned for this merge, and PR-40 entered once per merge."
    source: "ANALYZE re-check: PR40_ENTRY_PRE_D23E, 28 REAL in 17 bodies"
    disposition: ""
  - id: ITEM-30
    statement: "PR-35's and RS-40's closed result lists include MERGE_OBSERVED, so C-DISPATCH's result is not barred as a 'sixth result'."
    source: "ANALYZE re-check: PR-35 OTHER_CONTRADICTION (REAL); completeness critic for RS-40"
    disposition: ""
  - id: ITEM-31
    statement: "PR-40 no longer says that an ordinary in-scope defect stays with the existing PR owner; a REJECT re-plans through PR-20 (C-REPLAN, D23-F)."
    source: "ANALYZE re-check: PR-40 OTHER_CONTRADICTION (REAL)"
    disposition: ""
  - id: ITEM-32
    statement: "Every body that commits its own output artifacts scopes any read-only or no-repository-edit claim to exclude them, and PR-30, PR-35 and RS-40 scope the 'paths outside docs/ephemeral/ are not written' sentence to their artifacts, since they push code (Product Owner ruling 2)."
    source: "ANALYZE re-check: READ_ONLY_SELF_DESCRIPTION, 19 REAL in 12 bodies, plus PR-35 OTHER_CONTRADICTION (REAL)"
    disposition: ""
  - id: ITEM-33
    statement: "No live body carries instructions addressed to its author: 'candidate URL tokens must be replaced', 'Do not copy historical example constants into this reusable contract', and author-directed 'Embed only applicable workflow contracts' go."
    source: "ANALYZE re-check: CANDIDATE_AUTHORING_LEFTOVER, 9 REAL in 8 bodies"
    disposition: ""
  - id: ITEM-34
    statement: "QA-110 routes a completed failing run one way only, so ACCEPT and ESCALATION_REQUIRED no longer both claim it."
    source: "ANALYZE re-check: QA-110 OTHER_CONTRADICTION (REAL)"
    disposition: ""
  - id: ITEM-35
    statement: "QA-80 states WRONG_ROUTE_APPROVED_BASE once, with the graph's two branches as conditions (terminal without a complete delta; QA-70 with one), not as two opposing rules."
    source: "ANALYZE re-check: QA-80 OTHER_CONTRADICTION (REAL); docs/graph/parts/prompts/QA-80.json"
    disposition: ""
  - id: ITEM-36
    statement: "The D23-G release-line check rejects a Prompt version:, Set: or Ecosystem release: label line anywhere in a body, not only in the first 8 non-blank lines, in the registry's 55 rows and in flowmaster-validate's PROMPT_BODY_RELEASE_HEADER."
    source: "ANALYZE verification B4a-c: both checks see 8 non-blank lines only"
    disposition: ""
  - id: ITEM-37
    statement: "In the eight bodies that carry C-LAT but implement nothing (PR-10, PR-20, PR-40, RS-10, RS-20, DOC-10, DOC-20, IA-30), C-LAT's 'Decide it during work' three-step block is removed; the Material definition and each body's own routing stay (a D23-C successor, Product Owner ruling 4)."
    source: "ANALYZE completeness critic; C-LAT is placed verbatim by the parent's step 22 (spec v2 §3), so this changes a canonical placement and needs a Product Owner ruling"
    disposition: ""
  - id: ITEM-38
    statement: "PR-10's 'material change (D23-C) change' loses its doubled word. The '(D23-C)' form itself stays: it is the parent's recorded STEP22-BEFORE settlement for routing lines that come before C-LAT (evidence/e3/E3-E4-report.md:112)."
    source: "ANALYZE sweep: PR-10, PR-35, PR-40, DOC-10 read 'material change (D23-C)'; spec v2 step 22"
    disposition: ""
parts:
  - id: PART-01
    name: "Skill text applies D23-B and D7"
    items: [ITEM-01, ITEM-02, ITEM-14]
    class: B
    after: []
  - id: PART-02
    name: "Skills stop copying and hashing prompt bodies, and D22 gets its guards"
    items: [ITEM-04, ITEM-05, ITEM-06, ITEM-08, ITEM-16]
    class: B
    after: []
  - id: PART-03
    name: "Stale statements in skill text"
    items: [ITEM-03, ITEM-07, ITEM-09, ITEM-10, ITEM-25, ITEM-39]
    class: C
    after: []
  - id: PART-04
    name: "Validator and graph-tooling defects"
    items: [ITEM-11, ITEM-12, ITEM-13, ITEM-15]
    class: C
    after: []
  - id: PART-05
    name: "Read-only claims scoped to the body's own committed outputs"
    items: [ITEM-17, ITEM-32]
    class: B
    after: []
  - id: PART-06
    name: "CL-40's Candidate CRD Items List lives in Notion"
    items: [ITEM-18]
    class: A
    after: []
  - id: PART-07
    name: "CL-20 board-update destination"
    items: [ITEM-19]
    class: D
    after: []
  - id: PART-08
    name: "OPS-10 and OPS-20 page-mention rule scoped"
    items: [ITEM-20]
    class: B
    after: []
  - id: PART-10
    name: "Registry parent ids match the 091426.1 hubs"
    items: [ITEM-22]
    class: C
    after: []
  - id: PART-11
    name: "MGMT-10 proposed body carries no release header line"
    items: [ITEM-23]
    class: B
    after: []
  - id: PART-12
    name: "Named state sits immediately before a handoff block"
    items: [ITEM-24]
    class: B
    after: []
  - id: PART-13
    name: "Bodies' handoff sentences follow C-HANDOFF and C-ART"
    items: [ITEM-26, ITEM-27, ITEM-28]
    class: B
    after: []
  - id: PART-14
    name: "PR-40 entry and results follow D23-E and D23-F in every body"
    items: [ITEM-21, ITEM-29, ITEM-30, ITEM-31]
    class: B
    after: []
  - id: PART-15
    name: "Author-only leftovers removed from live bodies"
    items: [ITEM-33, ITEM-38]
    class: D
    after: []
  - id: PART-16
    name: "Two routing contradictions in QA-110 and QA-80"
    items: [ITEM-34, ITEM-35]
    class: D
    after: []
  - id: PART-17
    name: "D23-G release-line check covers the whole body"
    items: [ITEM-36]
    class: B
    after: []
  - id: PART-18
    name: "C-LAT's decide-during-work block leaves the non-implementing bodies"
    items: [ITEM-37]
    class: A
    after: []
request: |
  477 merged. yes, fix 1-4. The next action in Alph is planning for PR05. That will be done after this MGMT run is complete.
requested_by: Nathan
analyze_approved_by: ""
analyze_approved_date: ""
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: MODIFICATION-20260923-alpha-feedback-open-entries
shares_package_with: []
---

# MODIFICATION-20260923-closeout-residuals

Brings the installed skills and five prompt bodies into line with D23 and D22, closing the items
the previous Modification's close-out left for Nathan (`evidence/e6/CLOSE-OUT-20260923.md` §4.A
and §4.E).

## Intake

Spawned from `MODIFICATION-20260923-alpha-feedback-open-entries`, whose scope froze at ANALYZE
approval (`D20`). Nathan's "yes, fix 1-4" (2026-09-23) answers the close-out report's four
questions. Questions 1 and 2 are this Modification: 1 is the installed-skill text, with the
protected-core hash pin fixed by a GCFPE override outside the core, and 2 folds the body defects
into the same run. Questions 3 (the D18 Alpha-state block) and 4 (older stale lines on Notion
control pages) are maintenance edits made directly by `GCFPE-MGMT-10` and recorded in the close-out
file, not here, except the two §4.D items that change the registry or a prompt body (ITEM-22 and
ITEM-23), which need this Modification's gates.

Every item is `NEW`: none is ruled on in the decision record `D1`–`D24`, and none is an open
Alpha Feedback entry. Each item's source line is where it was found; ANALYZE re-verifies each
against the installed tree or the live body before planning an edit.

**Not included:** the four `tw-flowmaster` findings on its GCFPE binding (`:278`, `:311`–`:315`)
and AF-012 for TW. The TW ecosystem is out of scope (Nathan, 2026-09-23).

**Parts.** PART-01 to PART-03 each carry one rule across the skills that state it, so each lands
whole. PART-02 puts `D22`'s guard in the same part as the repairs, because a guard that lands before
them fails on the installed text and one that lands after leaves them unguarded. PART-04 groups the
tooling defects. Each body defect is its own part (PART-05 to PART-09, PART-11), since none depends on
another. PART-10 is a registry-only change. Whatever the grouping, template rule 7 still sends every change to the same skill through
one package, one review and one install.

## §A — Analysis

*Written by MODE = ANALYZE, 2026-09-23. Evidence: `evidence/closeout-residuals/ANALYZE-body-evidence.md`
(every body finding with its verdict), `ANALYZE-skill-evidence.md` (every skill item, as corrected by
verification) and `ANALYZE-closure.md` (`closure.py` output for each touched prompt).*

### Product Owner rulings received during ANALYZE

1. **The Candidate CRD Items List lives in Notion** (Nathan, 2026-09-23: *"candidate CRD can live in
   notion, I don't think it is a huge doc"*). No Notion page for it exists yet. The only copy is the
   Drive file `Candidate-CRD-Items-List.md` (`1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`, 31 923 B, last
   modified 2026-09-08). ITEM-18 therefore needs a Notion page, a destination rule in
   `notion-write-boundary.md` naming that page, and CL-40 naming it.
2. **Every prompt commits its output files** (Nathan, 2026-09-23: *"all output files are committed,
   that is the only way they are ever seen"*). A body that calls itself read-only, or says it does not
   edit the repository, while it commits its own output artifacts has the wording wrong, not the
   behaviour. The fix scopes the claim so that it excludes the prompt's own committed outputs (C-ART).
   The commit stays.
3. **This Modification is widened** to the stale body text that D23's placements left in place
   (Nathan, 2026-09-23: *"yes. we may as well widen. This process seems to be working so far. I want
   this system tight"*). ANALYZE was not yet approved, so no override is needed. The body sweep
   measured the classes: handoff content lists next to C-HANDOFF, PR-40 entry without
   `MERGE_OBSERVED`, read-only claims beside commits, author-only instructions, C-LAT in
   non-implementing roles, and other internal contradictions. An adversarial re-check of every
   finding sets the scope; the new items and parts follow it.

4. **ITEM-37: C-LAT in the eight non-implementing bodies takes option (b)** (Nathan, 2026-09-23, on
   "decide it, implement it, test it" in bodies that implement nothing: *"yes those words don't seem to
   mean anything do they"*). In PR-10, PR-20, PR-40, RS-10, RS-20, DOC-10, DOC-20 and IA-30, step 2
   hands an obvious, necessary, consistent change to the implementing PR owner, who decides,
   implements, tests and records it. The material test (step 1) and step 3 are unchanged. This is a
   `D23-C` successor and is recorded as one at EXECUTE.

### Per part: closure, tier, class and targets

| part | class | tier | targets | why this tier |
|---|---|---|---|---|
| PART-01 | B | 0 | skill (PR skill, relay) | skill text; no prompt produces anything different |
| PART-02 | B | 0 | skill (flowmaster-validate, change-flow, relay, governance audit) | skill text, code and guards; the core bytes do not move |
| PART-03 | C | 0 | skill (flowmaster-validate, governance audit, glow-graph-contract, change-flow, relay) | guidance corrected to match behaviour |
| PART-04 | C | 0 | skill (flowmaster-validate, glow-graph-contract); graph (`docs/graph/parts` indices) | the built graph stays byte-identical (`ae2bd159…`) |
| PART-05 | B | 0 | prompt (13 bodies, plus PR-30, PR-35 and RS-40's storage sentence); registry guards | wording only; every body already commits its outputs (ruling 2) |
| PART-06 | A | 1 | prompt (CL-40); rule (`notion-write-boundary.md`); notion_control (new list page); registry guard | changes what CL-40 writes and where (ruling 1) |
| PART-07 | D | 1 | prompt (CL-20); registry guard | changes what the closure memo says when no board reference is given |
| PART-08 | C | 0 | prompt (OPS-10, OPS-20) | wording scoped; nothing produced changes |
| PART-10 | D | 0 | registry (71 parent values, 70 titles) | data; the audit's NAM-002 comparison then holds |
| PART-11 | B | 0 | notion_control (the unpromoted MGMT-10 proposed body) | not a release member; two header lines and one sentence go |
| PART-12 | B | 0 | skill (`glow-po-reporting`); rule (Hub, `session-working-rules.md`) | reporting format |
| PART-13 | B | 1 | prompt (46 bodies with REAL findings, plus every carrier of the shared sentences); registry guards | changes what handoffs carry |
| PART-14 | B | 1 | prompt (17 bodies); registry guards | changes what PR-35 and RS-40 may return and how PR-40 is entered; the graph already carries `MERGE_OBSERVED` and the REJECT re-plan |
| PART-15 | C | 0 | prompt (8 bodies) | author-only text removed; runtime behaviour unchanged |
| PART-16 | D | 1 | prompt (QA-110, QA-80) | result routing text now matches the graph (`D13`) |
| PART-17 | B | 0 | registry (55 rows); skill (flowmaster-validate) | guard widening; applies to every body |
| PART-18 | A | 1 | prompt (8 C-LAT bodies; 4 with the step-22 literal) | changes a canonical placement (ITEM-37); ITEM-38 restores the approved literal |

**No graph part moves.** The graph already carries every route the bodies are brought into line with:
`MERGE_OBSERVED`, the REJECT re-plan, and both QA-80 branches. The only change under `docs/graph/parts` is
PART-04's index bookkeeping, which leaves the built graph byte-identical. So routing is provably
unaffected. The Modification is still **Tier 1** (`gate_tier: 1`), because PARTs 06, 07, 13, 14, 16 and 18
change what prompts produce.

**Closure.** This Modification touches 48 prompts. Taken together with their upstream, downstream and
state-sharing prompts, the radius is **55 of 55**. So the Tier 1 gate is the full corpus: the registry
validator over all 55 live bodies, and every installed suite. `closure.py` output for each of the 48
(full text in `ANALYZE-closure.md`):

| prompt | upstream | downstream | state sharers | radius |
|---|---|---|---|---|
| CF-C-10 | 4 | 4 | 19 | 22 |
| CF-C-20 | 1 | 2 | 21 | 22 |
| CF-C-30 | 2 | 2 | 2 | 5 |
| CF-C-40 | 1 | 1 | 3 | 4 |
| CF-E-10 | 4 | 4 | 19 | 22 |
| CF-E-20 | 1 | 2 | 21 | 22 |
| CF-E-30 | 2 | 2 | 2 | 5 |
| CF-E-40 | 1 | 1 | 3 | 4 |
| CL-20 | 2 | 5 | 0 | 7 |
| CL-30 | 1 | 1 | 0 | 2 |
| CL-40 | 4 | 1 | 7 | 12 |
| CL-C-10 | 1 | 2 | 1 | 4 |
| CL-E-10 | 1 | 3 | 1 | 5 |
| CL-E-20 | 4 | 2 | 21 | 26 |
| CL-E-30 | 2 | 2 | 5 | 8 |
| CL-E-40 | 2 | 2 | 0 | 4 |
| DOC-10 | 1 | 3 | 20 | 22 |
| DOC-20 | 0 | 4 | 23 | 25 |
| ESC-10 | 3 | 1 | 0 | 4 |
| ESC-25 | 4 | 1 | 21 | 22 |
| ESC-30 | 6 | 2 | 19 | 24 |
| ESC-40 | 1 | 3 | 3 | 6 |
| GCFPE-MGMT-10 | 0 | 1 | 0 | 1 |
| IA-30 | 4 | 2 | 6 | 10 |
| OPS-10 | 1 | 3 | 19 | 21 |
| OPS-20 | 1 | 3 | 22 | 24 |
| OPS-30 | 1 | 3 | 4 | 8 |
| PR-10 | 3 | 3 | 19 | 24 |
| PR-20 | 3 | 2 | 19 | 22 |
| PR-30 | 3 | 3 | 3 | 6 |
| PR-35 | 4 | 3 | 3 | 7 |
| PR-40 | 3 | 3 | 6 | 11 |
| PR-50 | 0 | 0 | 0 | 0 |
| QA-10 | 3 | 2 | 0 | 4 |
| QA-100 | 2 | 1 | 22 | 23 |
| QA-110 | 3 | 4 | 7 | 10 |
| QA-120 | 1 | 5 | 0 | 5 |
| QA-20 | 1 | 2 | 19 | 20 |
| QA-50 | 1 | 4 | 19 | 22 |
| QA-60 | 1 | 3 | 19 | 22 |
| QA-70 | 3 | 2 | 3 | 7 |
| QA-80 | 3 | 1 | 1 | 4 |
| QA-90 | 5 | 3 | 3 | 8 |
| RS-10 | 8 | 1 | 1 | 10 |
| RS-20 | 5 | 4 | 4 | 9 |
| RS-30 | 1 | 1 | 1 | 2 |
| RS-40 | 1 | 4 | 3 | 5 |
| UTIL-10 | 0 | 0 | 7 | 7 |

### Scope, and how it was measured

- **Bodies (PARTs 05, 13–16, 18).**
  - All 55 live bodies were read completely under `D22`. Seven classes were matched by effect, not by
    known phrasings: 335 findings.
  - Every finding was then re-judged adversarially, defaulting to `NOT_REAL`, with named exclusions:
    canonical text as placed; an artifact rather than the handoff; `complete` meaning a fully
    populated short handoff; labelled historical; the assertion fallback; correctly scoped.
  - Result: **184 REAL** (158 re-judged plus 26 found by the verifiers) and **177 NOT_REAL**.

  | class | REAL | NOT_REAL | bodies | part |
  |---|---|---|---|---|
  | handoff content | 123 | 99 | 46 | 13 |
  | PR-40 entry | 28 | 9 | 17 | 14 |
  | read-only claims | 19 | 5 | 12 | 05 |
  | author-only leftovers | 9 | 26 | 8 | 15 |
  | other contradictions | 5 | 11 | 4 | 16, 14, 05 |
  | undefined references | 0 | 21 | — | — |
  | mention bans | 0 | 6 | — | — |

  The shared sentences behind ITEM-27 recur in most bodies. PLAN anchors on each exact sentence, and
  EXECUTE's body script reports every body it edits, so a carrier the sweep did not list is still
  found.
- **Skills (PARTs 01–04, 12, 17).** Broad regular-expression co-occurrence across every GCFPE-bound
  skill's `SKILL.md`, references and scripts:
  - for D22, a body noun with a copy or identity verb;
  - for D23-B, a handoff noun with a carry or contain verb;
  - for D7, `drive`;
  - for counts, numeric patterns.

  Legitimate uses were then removed by reading each hit. The baseline suites all pass.
- **Registry (PART-10).** Every row's page ID was matched against the child pages of the six 091426.1
  parent pages. All 55 rows and all 16 lanes name a superseded parent: 71 values across 6 IDs.
- **Header window (PART-17).** Tested on synthetic bodies. Both the registry guards and
  `PROMPT_BODY_RELEASE_HEADER` see only the first 8 non-blank lines.

### Contradictions and risks

- **The parent's gate passed all of this.** The E4 check reported 55 of 55 bodies clean, with 0 of
  1 484 assertions failing, and every one of the 184 REAL findings survived it. The guards tested
  that each canonical text was present, not that older text contradicting it had gone. Each new class
  therefore gets forbidden-pattern guards with injected regressions (ITEM-28, and the guards in PARTs
  05, 14, 15, 16 and 17). This matches `GUARD-001`.
- **D22's prose guard is weaker than prototyped (ITEM-16).** A keyword guard missed 30 of 30
  paraphrases. The redesign pins exact retired phrases, requires the override sentence, and tests the
  governance audit's code. The residual limit, prose paraphrase, is recorded and left to review.
- **Notion storage.** Today a strikethrough across bold and code turned into literal tildes when a
  later edit re-stored the page. At E6, paragraph storage exposed a blank-line window on 10 bodies. So
  EXECUTE uses exact-anchor replacements, reads every body back in full, and puts no strikethrough in
  bodies.
- **Canonical texts are not edited**, except by ITEM-37 if you rule for it. The parts replace older text
  that sits next to the canonical texts. PR-35's "as before" is canonical C-SUB wording and stays.
- **Seven skill packages** go through one D24 review round, with two reviewer subagents. Given the
  parent's five rounds, more than one round is a real risk. The pins listed in the skill evidence file
  are what a round most often trips on.
- **The live MGMT-10 body will be replaced** by the D20 redesign, so PART-05 edits a body with a short
  remaining life. It is included because it is live today.
- **Defect classes matched:** `DERIV-001` (handoffs restating artifacts), `GUARD-001` (guards that never
  fired), `SCOPE-001` (measured by effect), `FUNC-001` (read-only judged by what the body does, not
  what it says).
- **This record's opening sentence** says "five prompt bodies". The widened scope is 48 bodies, plus
  the proposed MGMT-10 body.

### Decisions this analysis made

Each follows from a ruling already in force, so none waits on the Product Owner:

1. **The PR skill's revision is not bumped (ITEM-01).** The change is text-only, and a skill's identity
   is its freeze digest (`D19`). A bump would force regenerating the contract.
2. **The relay's GCFPE model and reasoning advice is deleted (ITEM-02).** This applies the
   retired-assessment rule already in `change-flow:299` and the governance audit's interop `:56`.
3. **The governance audit's code changes as well as its text (ITEM-05).** D22 governs what a skill
   does, not only what it says.
4. **The relay keeps `GOOGLE_DRIVE` for non-GCFPE projects and adds `REPOSITORY` (ITEM-14).** The relay
   is generic; D7 binds GCFPE.
5. **Graph counts appear once, as a dated proof token with its digest (ITEM-09).** The unreproducible
   94.3% is dropped.
6. **The registry deriver imports the governance audit's `load_data` from a root path it is given
   (ITEM-13).** That keeps one parser (`DERIV-001`).
7. **CL-20's board stays a runtime-supplied reference (ITEM-19),** with a pending state when none is
   supplied. PF04 §9.1.5 owns the board's identity.
8. **The proposed MGMT-10 body loses its two release header lines and the "stamped at promotion"
   sentence (ITEM-23).** This applies D23-G to a body you approved for testing; the change is
   mechanical. PART-17's whole-body check holds it at promotion.
9. **QA-80 and QA-110 follow the graph (ITEMs 34 and 35, `D13`).**
10. **ITEM-11 is fixed rather than retiring the historical alias path,** because the fix is four lines.
11. **Handoff-last against the named state (ITEM-24):** the state goes on the line immediately before
    the block.

### Open questions for the Product Owner

None open. The question below was answered by ruling 4 and is kept as asked.

1. **ITEM-37: C-LAT in the eight bodies that implement nothing** (PR-10, PR-20, PR-40, RS-10, RS-20,
   DOC-10, DOC-20, IA-30).
   - **Today:** its step 2 tells a planner, a reviewer or a documentation checker to "decide it,
     implement it, test it". The parent spec placed the text there so that these roles would use the
     three-step test to tell a material change from an ordinary one.
   - **(a) Leave it as placed:** the roles apply the test and ignore "implement", which does not fit
     them.
   - **(b) Recommended.** A D23-C successor: in those eight bodies step 2 reads "hand it to the
     implementing PR owner, who decides, implements, tests and records it". The test is unchanged, and
     no role is told to do what it cannot.

### Readiness and interaction cost

`readiness: READY`. The one open ruling (ITEM-37) was answered during ANALYZE (ruling 4).

    interaction_cost = open rulings 1 + 2 + review cycles 1 + installs 7 + merges 1 = 12

- **Installs:** one `.skill` each for `flowmaster-validate`, `change-flow`, `session-relay-flowmaster`,
  `glow-hde-pr-development`, `amthor-workspace-governance-audit`, `glow-graph-contract` and
  `glow-po-reporting`.
- **Merge:** one pull request carrying the repository changes.
- **Calibration:** the parent predicted 11 and took 29, 13 of them unplanned rulings and 4 extra review
  rounds. Each extra round here adds 1. Moving PART-18 to its own run would save its 1 ruling and cost a
  separate run.
