---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-closeout-residuals
status: INTAKE
targets: []
gate_tier:
closure:
  upstream: []
  downstream: []
  state_sharers: []
readiness:
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted:
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
    statement: "GCFPE stage prompts are no longer pinned by prompt-body content hash, through a GCFPE override outside the byte-identical protected Flowmaster core (the core and tw-flowmaster are untouched)."
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
    statement: "validate_gcfpe_current.py runs with --bodies-stdin without a NameError."
    source: "CLOSE-OUT-20260923 §4.A (carried); validate_gcfpe_current.py:605"
    disposition: ""
  - id: ITEM-12
    statement: "The graph's edge_indices bookkeeping matches its edges."
    source: "CLOSE-OUT-20260923 §4.A (carried)"
    disposition: ""
  - id: ITEM-13
    statement: "The two graph derivation scripts live in glow-graph-contract rather than in run evidence."
    source: "CLOSE-OUT-20260923 §4.A (carried)"
    disposition: ""
  - id: ITEM-14
    statement: "session-relay-flowmaster no longer names Drive as the preferred artifact plane (D7)."
    source: "CLOSE-OUT-20260923 §4.A (carried); session-relay-flowmaster/SKILL.md:273, :358"
    disposition: ""
  - id: ITEM-15
    statement: "The five round-a5 non-blocking findings are repaired."
    source: "CLOSE-OUT-20260923 §4.A (carried); SECTION-10-REVIEW-a5-SFR-A5-1.md N1-N4, SECTION-10-REVIEW-a5-SFR-A5-2.md F1-F4"
    disposition: ""
  - id: ITEM-16
    statement: "D22 has a guard: a check that fails when an installed skill copies, snapshots or hashes a prompt body."
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
    statement: "CL-20's board update names its destination, or is removed."
    source: "CLOSE-OUT-20260923 §4.E"
    disposition: ""
  - id: ITEM-20
    statement: "OPS-10 and OPS-20 no longer both forbid and require page mentions."
    source: "CLOSE-OUT-20260923 §4.E"
    disposition: ""
  - id: ITEM-21
    statement: "The four CL-* bodies that cite a PR-40 merge-approval effect 'defined above' either define it or stop citing it."
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
parts:
  - id: PART-01
    name: "Skill handoff wording follows D23-B"
    items: [ITEM-01, ITEM-02]
    class:
    after: []
  - id: PART-02
    name: "Skills stop copying and hashing prompt bodies, and D22 gets its guard"
    items: [ITEM-04, ITEM-05, ITEM-06, ITEM-08, ITEM-16]
    class:
    after: []
  - id: PART-03
    name: "Stale statements in skill text"
    items: [ITEM-03, ITEM-07, ITEM-09, ITEM-10, ITEM-14, ITEM-25]
    class:
    after: []
  - id: PART-04
    name: "Validator and graph-tooling defects"
    items: [ITEM-11, ITEM-12, ITEM-13, ITEM-15]
    class:
    after: []
  - id: PART-05
    name: "QA-10 read-only claim"
    items: [ITEM-17]
    class:
    after: []
  - id: PART-06
    name: "CL-40 candidate-list store"
    items: [ITEM-18]
    class:
    after: []
  - id: PART-07
    name: "CL-20 board-update destination"
    items: [ITEM-19]
    class:
    after: []
  - id: PART-08
    name: "OPS-10 and OPS-20 page-mention rule"
    items: [ITEM-20]
    class:
    after: []
  - id: PART-09
    name: "CL-* PR-40 merge-approval reference"
    items: [ITEM-21]
    class:
    after: []
  - id: PART-10
    name: "Registry parent ids match the 091426.1 hubs"
    items: [ITEM-22]
    class:
    after: []
  - id: PART-11
    name: "MGMT-10 proposed body header"
    items: [ITEM-23]
    class:
    after: []
  - id: PART-12
    name: "Named state sits immediately before a handoff block"
    items: [ITEM-24]
    class:
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

*In progress. Written by MODE = ANALYZE; not yet approved.*

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

