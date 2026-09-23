---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-closeout-residuals
status: ANALYZED
targets: [prompt, skill, rule, graph, registry, notion_control]
gate_tier: 1
closure:
  upstream: [CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CF-PO-10, CL-20, CL-30, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, GCFPE-MGMT-10, IA-10, IA-20, IA-30, IA-40, IA-50, MGR-10, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-10, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30, RS-40]
  downstream: [CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CF-PO-10, CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, ESC-10, ESC-25, ESC-30, ESC-40, IA-10, IA-20, IA-30, IA-40, IA-50, IA-60, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-10, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30, RS-40]
  state_sharers: [CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, DOC-10, DOC-20, ESC-25, ESC-30, ESC-40, IA-10, IA-20, IA-30, IA-40, IA-60, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-100, QA-110, QA-20, QA-50, QA-60, QA-70, QA-90, RS-10, RS-20, RS-30, RS-40, UTIL-10]
readiness: NEEDS_RULING
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 7
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
    statement: "The shared sentences in 34 bodies that keep mappings 'in … metadata or [the] handoff' (A1) and in 34 bodies that keep or carry the CANON_CONFLICT_REGISTER in the handoff (A2) keep them in the output artifact only; the handoff names that artifact (C-ART, C-HANDOFF)."
    source: "ANALYZE anchor census A1 and A2; one verdict per shared sentence"
    disposition: ""
  - id: ITEM-28
    statement: "A registry guard (D14) fails when any retired handoff-content phrasing, branch or commit carriage, or 'or the handoff' storage clause returns to a body, each proven by an injected must-fail regression."
    source: "The parent's E4 gate passed every body ITEM-26 names (0 of 1 484 assertions); a guard that never fired is not a guard (GUARD-001)"
    disposition: ""
  - id: ITEM-29
    statement: "Every one of the 21 bodies that describes PR-40 entry by Nathan's assertion alone (anchor A7) uses the parent's A1-5 wording and the D23 once-per-merge sentence verbatim: the MERGE_OBSERVED handoff from PR-35 or RS-40 first, Nathan's merge assertion only where no MERGE_OBSERVED result was returned for this merge, and PR-40 entered once per merge."
    source: "ANALYZE anchor census A7 (21 bodies)"
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
    statement: "The 13 bodies that call themselves read-only, or say they do not edit the repository, while committing their own outputs scope that claim to exclude those outputs; the shared 'Reviewers remain read-only' sentence is scoped to the reviewed work; and PR-35, RS-40 and GCFPE-MGMT-10, which write outside docs/ephemeral/ and docs/graph/, scope the storage sentence to their artifacts (ruling 2)."
    source: "ANALYZE anchor census A5 and A6 (evidence/closeout-residuals/ANALYZE-anchor-census.md)"
    disposition: ""
  - id: ITEM-33
    statement: "The 13 live bodies carrying author-directed text (anchor A3: 'Embed only applicable workflow contracts', 'reusable prompt policy', 'Do not copy those pins into reusable prompt text', 'historical example constants into this reusable contract') and the 5 carrying candidate-authoring text (anchor A4) lose it."
    source: "ANALYZE anchor census A3 and A4; one verdict per shared sentence"
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
  - id: ITEM-40
    statement: "The unpromoted GCFPE-MGMT-10 PROPOSED BODY carries none of the classes this Modification removes from live bodies (anchors A1-A5) and resolves the internal contradictions the census found in it, so it can be promoted without reintroducing them."
    source: "ANALYZE anchor census of page 3e34590a05eb811b93d2da9b4ef8106d (evidence/closeout-residuals/ANALYZE-anchor-census.md)"
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
    name: "The MGMT-10 proposed body is fixed before promotion"
    items: [ITEM-23, ITEM-40]
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

*Written by MODE = ANALYZE, 2026-09-23. A two-reviewer check found 11 required and 19 non-blocking
findings. This version repairs all of them; the repairs are listed at the end of §A. Evidence, all
under `evidence/closeout-residuals/`:*

- *`ANALYZE-body-evidence.md`: every sweep finding and its re-check verdict;*
- *`ANALYZE-anchor-census.md`: the exact census that gives each shared sentence one verdict;*
- *`ANALYZE-skill-evidence.md`: every skill item, as corrected by verification;*
- *`ANALYZE-closure.md`: `closure.py` output for each touched prompt.*

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
3. **This Modification is widened** to the stale body text left in place by D23's placements (Nathan,
   2026-09-23: *"yes. we may as well widen. This process seems to be working so far. I want this system
   tight"*). ANALYZE was not yet approved, so no override is needed.
   - **Measured classes:** a sweep of seven classes found handoff content lists, PR-40 entry without
     `MERGE_OBSERVED`, read-only claims beside commits, author-only leftovers and other contradictions.
     The undefined-reference and mention-ban classes came back empty.
   - **How scope was set:** an adversarial re-check judged every finding. An exact census then gave
     each shared sentence one verdict for all its carriers.
   - **C-LAT placement:** raised by the completeness critic, not by the sweep.
4. **ITEM-37: C-LAT in the eight bodies that implement nothing** (Nathan, 2026-09-23, on "decide it,
   implement it, test it" there: *"yes those words don't seem to mean anything do they"*).
   - **What the ruling was given:** the recommendation read "hand it to the implementing PR owner".
   - **Why that wording cannot stand:** review found it wrong for three roles.
     - PR-40 runs after the merge, when no PR owner remains, and its defects re-plan through PR-20
       (D23-F).
     - IA-30 and PR-10 run before any PR owner exists.
   - **What is applied:** the reading that matches the ruling. The *Decide it during work* block is
     removed from PR-10, PR-20, PR-40, RS-10, RS-20, DOC-10, DOC-20 and IA-30. The **Material**
     definition and each body's own routing stay.
   - **Record:** a `D23-C` successor note, entered before EXECUTE (class A gate). Nathan was told of
     this reading on 2026-09-23.

### Open question for the Product Owner

1. **PART-06: does CL-40 write the Candidate CRD Items List in Notion itself?**
   - **What CL-40 does:** it runs at the end of each change, scans for PF09 gaps and CRD candidates, and
     adds new candidates to the list. Ruling 1 moves the list to Notion.
   - **What breaks:** a flow prompt is read-only to Notion unless a destination rule names the page
     (`notion-write-boundary.md`). With no writer, the list goes stale, which is the failure that
     retired the D18 block.
   - **(A) Recommended.** A destination rule names the one page, so CL-40 becomes the first flow prompt
     with a Notion write, and CL-40's registry `mutations` row allows it. This costs one policy entry,
     and the list stays current.
   - **(B)** CL-40 records candidates only in its committed `CYCLE_GAP_SCAN`, and Nathan or a
     maintenance run copies them over. This needs no new write path, but it depends on someone
     remembering after every change.

### Items whose premise the verification refuted

- **ITEM-20, proposed `NOT_APPLICABLE`.**
  - The re-check found both OPS mention bans correctly scoped: they cover authored reusable text, and
    a runtime handoff URL is runtime data.
  - The census found them only in OPS-10 and OPS-20.
  - PART-08 therefore lands empty, and §E records the verdict.
- **ITEM-21 keeps its bodies and loses its premise.**
  - The "merge-approval effect … defined above" does point at the *Product Owner merge action* section
    above it, so the reference resolves.
  - What is wrong is that section: it describes PR-40 entry by assertion alone. That is anchor A7,
    fixed by ITEM-29 in the same four bodies.
  - ITEM-21 now covers only renaming "merge-approval" to what the section describes, an entry
    assertion that approves nothing.
- **ITEM-38 is reduced to PR-10's doubled word.**
  - `material change (D23-C)` is the parent's recorded STEP22-BEFORE settlement for routing lines that
    come before C-LAT (`evidence/e3/E3-E4-report.md:112`).
  - It moves to PART-15, so no ruling holds it.
- **ITEM-13 is half landed.** The pre-E2 contract it needs was kept at
  `evidence/pre-e2-contract/` in commit `245b21b`, during ANALYZE. PLAN moves it to `docs/graph/`,
  because it is a maintained input to a skill script and `docs/ephemeral/` is pruned by hand. PLAN
  then treats the regeneration as a verification step.

### Per part: closure, tier, class, targets and gates

| part | class | tier | targets | gates |
|---|---|---|---|---|
| PART-01 | B | 0 | skill: PR skill (ITEM-01), relay (02, 14: text, `validate_relay_manifest.py`, self-test, examples) | isolated readback; `CONTRACT_FORBIDDEN` literals and the PR validator's forbidden literal, each fired by an injected regression; D24 review; install |
| PART-02 | B | 0 | skill: flowmaster-validate, change-flow, relay, governance audit (text, code, fixture) | ITEM-16's guards fired by injected regressions; the governance-audit fixture; `core_sync` true; D24 review; install |
| PART-03 | C | 0 | skill: flowmaster-validate (03, 39), governance audit (07, 39), glow-graph-contract (09 including its description, 25), change-flow (10) | each control tested against an injected regression where it has a suite; the prose items are listed under *Unguarded*; D24 review; install |
| PART-04 | C | 0 | skill: flowmaster-validate (11, 15), glow-graph-contract (12, 13); graph: `docs/graph/parts` reindex; `docs/graph/` home for the pre-E2 contract; a dated correction note on the repair-a4 record (the claim-level half of 15) | build byte-identical (`ae2bd159…`); the builder rejects a count mismatch (injected); fixture cases for 11; the five a5 regressions; the contract regenerates to itself; D24 review; install |
| PART-05 | B | 0 | prompt: 15 bodies (A6: CL-20, CL-30, CL-40, CL-E-20, DOC-20, ESC-25, GCFPE-MGMT-10, OPS-10, OPS-30, PR-20, PR-40, PR-50, QA-10; A5 storage sentence: PR-35, RS-40, GCFPE-MGMT-10); registry guards | isolated readback; a registry forbidden pattern per retired phrasing, fired by an injected regression |
| PART-06 | A | 1 | prompt: CL-40; rule: `notion-write-boundary.md` destination rule (per the open question); notion_control: new *Candidate CRD Items List* page, migrated from Drive `1JPN7Wcq…`; registry: CL-40 `mutations`, guard; decision record: D-number for rulings 1 and 2 | D-number recorded before EXECUTE; Notion readback of the migrated list against the Drive source; registry guard fired by regression; corpus gate |
| PART-07 | D | 1 | prompt: CL-20; registry assertion | registry assertion added and fired by regression |
| PART-08 | B | 0 | prompt: OPS-10, OPS-20 | proposed `NOT_APPLICABLE` (above) |
| PART-10 | C | 0 | registry: 16 lane `notion_parent_id`, 55 row `expected_parent_id` (71 values over 6 IDs), with their 70 titles | the NAM-002 comparison run on a snapshot of actual parents, and failing on an injected wrong parent |
| PART-11 | B | 0 | notion_control: the unpromoted MGMT-10 proposed body (23, 40) | isolated readback; the body passes the widened release-line check (PART-17) and the new forbidden patterns, run against it before promotion |
| PART-12 | B | 0 | skill: `glow-po-reporting`; notion_control: Hub *Worker communication rules*; rule: `session-working-rules.md` | readback; D24 review; install |
| PART-13 | B | 1 | prompt: 48 bodies (46 with REAL routing findings under ITEM-26; every A1 and A2 carrier under ITEM-27); registry guards (ITEM-28) | ITEM-28's forbidden patterns, each fired by an injected regression; corpus gate |
| PART-14 | B | 1 | prompt: 21 bodies with A7 (CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10, QA-20), plus PR-35 and RS-40 (ITEM-30) and PR-40 (ITEM-31); registry guards | forbidden patterns for the assertion-only entry sentences; required A1-5 wording, fired by regression; corpus gate |
| PART-15 | D | 1 | prompt: 13 bodies with A3 or A4 (CL-20, CL-30, CL-40, CL-C-10, CL-E-10, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10), plus PR-10 for ITEM-38; registry assertions | assertions added and fired by regression. Tier 1 because removing CL-40's "This authoring candidate does not perform that update" changes whether CL-40 updates the list |
| PART-16 | D | 1 | prompt: QA-110, QA-80; registry assertions | assertions added and fired by regression; the body text matches the graph (`D13`) |
| PART-17 | B | 0 | registry: 55 rows' release-line guards; skill: flowmaster-validate `PROMPT_BODY_RELEASE_HEADER`; rule: `prompt-body-content-policy.md` ("in the header window" becomes "anywhere in the body") | the census measured 0 live label lines, so there are no false positives; a label line injected past line 8 fails |
| PART-18 | A | 1 | prompt: the 8 bodies of ITEM-37; registry: C-LAT guards on those 8 rows (the decide-block pattern becomes forbidden there); decision record: a `D23-C` successor; PE Metaprompt GCFPE overlay (its C-LAT placement); any skill copy that states C-LAT's placement | successor recorded before EXECUTE; forbidden pattern fired by regression; corpus gate |

- **PART-09 was dissolved.** Its only item, ITEM-21, moved to PART-14.
- **ITEM-14 moved from PART-03 to PART-01.** It applies D7, which makes it class B, not a control repair.
- **No graph part changes routing.** The graph already carries `MERGE_OBSERVED`, the REJECT re-plan and
  both QA-80 branches. PART-04 changes index bookkeeping only, and the build is byte-identical.
- **The Modification is Tier 1** (`gate_tier: 1`) because PARTs 06, 07, 13, 14, 15, 16 and 18 change
  what prompts produce.

**Closure.** The Modification touches 50 live prompts. Together with their upstream, downstream and
state-sharing prompts, the radius is **55 of 55**. The Tier 1 gate is therefore the full corpus: the
registry validator over all 55 live bodies, and every installed suite. Front matter holds the unions:
51 upstream, 50 downstream, 43 state sharers. Per prompt (full output in `ANALYZE-closure.md`):

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
| IA-10 | 3 | 5 | 19 | 24 |
| IA-20 | 2 | 4 | 19 | 22 |
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

- **Bodies.** Three passes, all under `D22`, with every body read completely.
  1. **Sweep:** seven classes, matched by effect. 335 findings.
  2. **Adversarial re-check:** 158 REAL, 177 NOT_REAL, plus 26 REAL findings added by the re-check.
  3. **Exact census:** nine anchors over the 55 live bodies and the proposed MGMT-10 body.

  The census is the authority for shared sentences. It gives each sentence one verdict that applies to
  every carrier and overrides a contradicting lane verdict. The re-check had judged, for example, the
  A1 sentence REAL in 9 bodies and NOT_REAL in 18. Measured part scopes:
  - PART-05: 15 bodies;
  - PART-13: 48;
  - PART-14: 21, plus PR-35 and RS-40;
  - PART-15: 13, plus PR-10;
  - PART-17: 0 live release-label lines;
  - touched overall: **50 of 55**.
- **Skills.** Every GCFPE-bound skill's `SKILL.md`, references and scripts were searched by broad
  regular-expression co-occurrence, then each hit was read and legitimate uses were removed. The
  classes searched:
  - D22 (a body noun with a copy or identity verb);
  - D23-B (handoff and carry);
  - D7 (`drive`);
  - counts.

  Two verifiers then reproduced or refuted each item (`ANALYZE-skill-evidence.md`). The baseline
  suites all pass.
- **Registry.** Each row's page was matched to the child pages of the six 091426.1 parent pages. All
  55 rows and 16 lanes name a superseded parent. The old-to-new mapping of the six IDs is in
  `ANALYZE-skill-evidence.md` and reproduced in PLAN.

### Decisions this analysis made

Each applies a ruling or rule already in force.

1. **Revisions move, per the unspent-identity rule** (`skill-identity-and-freeze.md`: "Corrected bytes
   never reuse one"):

   | skill | from | to |
   |---|---|---|
   | flowmaster-validate | 3.3.0 | 3.3.1 |
   | change-flow | 3.3.0 | 3.3.1 |
   | relay | 3.1.0 | 3.2.0 (new `REPOSITORY` plane) |
   | PR skill | 1.3.0 | 1.3.1 |
   | governance audit | 1.12.0 | 1.13.0 (code behaviour changes) |

   - The PR skill's revision sits inside the contract (`primary_skill_revision`), so the contract is
     regenerated with ITEM-13's regenerator, and its digest pins move with it.
   - glow-graph-contract and glow-po-reporting advertise no revision, so their identity is the freeze
     digest (`D19`).
2. **The relay's GCFPE model and reasoning advice is deleted (ITEM-02).** This applies the
   retired-assessment rule (`change-flow:299`, governance-audit interop `:56`).
3. **The governance audit changes its code as well as its text (ITEM-05).** D22 governs what a skill
   does.
4. **The relay keeps `GOOGLE_DRIVE` for non-GCFPE projects and adds `REPOSITORY` (ITEM-14).**
5. **Graph counts appear once, as a dated proof token (ITEM-09).** The unreproducible percentage is
   dropped from the text and from the description.
6. **The registry deriver imports the governance audit's `load_data` from a given root (ITEM-13).**
   That keeps one parser. It couples two packages, so they install together (see *Order*).
7. **CL-20's board stays a runtime-supplied reference (ITEM-19).** It is pending with its PF04 §9.1.1
   owner when none is supplied.
8. **QA-80 and QA-110 follow the graph (`D13`).**
9. **ITEM-11 is fixed in place,** not by retiring the historical alias path.
10. **Where a handoff block closes a message, the named state goes immediately before it (ITEM-24).**
11. **The proposed MGMT-10 body is edited (ITEMs 23 and 40).** These apply D23-G and this Modification's
    classes to a body approved for testing only. D20's promotion step is untouched.

### Order, cut-over and freeze

The parent found that no order of edits and installs stays green, and ran one cut-over under a freeze
(parent A1-4). The same applies here:

1. **One install event.** All seven packages are reviewed together (D24: two reviewer subagents, with
   the filled brief committed before either is spawned) and installed in one sitting. Two couplings
   force this:
   - flowmaster-validate pins change-flow's and relay's revisions;
   - glow-graph-contract imports the governance audit.
2. **The repository pull request lands before the install.** It carries:
   - the graph-parts reindex (ITEM-12);
   - the registry changes (PARTs 10 and 17, and the forbidden-pattern guards);
   - the management-document and decision-record entries;
   - the pre-E2 contract's move.

   The reindex must be on `main` before the stricter builder is installed.
3. **Bodies land under a freeze.** The freeze starts before EXECUTE's first Notion write and lifts
   after the full readback and the corpus gate. New guards that meet unedited bodies would fail; bodies
   landed without their guards would sit unguarded. So the guards are evaluated against the landed
   bodies in the same sitting, and only then is the pull request merged. PR05 planning waits on the
   freeze, which Nathan scheduled for after this run.
4. **This record and the close-out §6 commits** travel in one pull request from
   `claude/epic-tesla-17406z`. A merge preserves the record; it approves nothing (`D21-C`).

### Unguarded items, with the reason

- **ITEMs 03, 07, 09, 10, 25 and 39** are prose in skill text, with no suite that reads meaning. The
  D24 review holds them.
- **ITEM-24** is prose in `glow-po-reporting`, a prose skill with no validator.
- **ITEM-36** is itself a guard.

### Contradictions and risks

- **The parent's gate passed every one of these findings.** Its E4 check reported 0 of 1 484 assertions
  failing, because its guards tested that each canonical text was present, not that the text it
  replaced had gone. Every new class therefore gets a forbidden pattern fired by an injected regression
  (`GUARD-001`).
- **D22's prose guard is weaker than prototyped.** A keyword guard missed 30 of 30 paraphrases. ITEM-16
  now pins exact retired phrases, requires ITEM-08's sentence in change-flow and the relay, and tests
  the governance audit's code. The residual limit is prose paraphrase.
- **Notion storage.**
  - Today, a strikethrough across bold and code became literal tildes when a later edit re-stored the
    page.
  - At E6, a blank-line window on 10 bodies was exposed.

  So EXECUTE uses exact-anchor replacements, puts no strikethrough in bodies, and reads everything back
  in full. The migrated 32 KB list is read back against its Drive source.
- **D24 coupling.** PART-02 spans four packages and PART-03 spans five. One rejected edit blocks its
  part, re-cuts several packages, and needs fresh reviewers on the new bytes. The parent took five
  rounds.
- **Which MGMT-10 body governs this run.** This run is governed by the live 091426.1 MGMT-10 body as
  read when it began. PART-05 edits that body for later runs. PARTs 11 and 40 edit the proposed body,
  which does not govern this run.
- **Canonical texts are not edited, except by ruling 4.** PR-35's "as before" is canonical C-SUB wording
  and stays.
- **Not included (TW is out of scope).** tw-flowmaster's GCFPE binding keeps the core's content pin and
  an "optional digest" (`:306`), with no D22 override or guard. The same holds for its three
  model-advice lines (`:313`–`:317`). They are TW residuals, together with AF-012 for TW.
- **Defect classes matched:**
  - `DERIV-001`: handoffs restating artifacts;
  - `GUARD-001`: guards that never fired;
  - `SCOPE-001`: measured by effect;
  - `FUNC-001`: read-only claims judged by what the body does.
- **Findings on sections written upstream of ANALYZE** (template rule 1: recorded, not edited):
  - the opening sentence's "five prompt bodies" is now 50 live bodies plus the proposed MGMT-10 body;
  - the Intake's "none is ruled on in D1–D24" is false for ITEM-08 (the A1-6 precedent), ITEM-24 (a D23
    successor) and ITEM-29 (D23-E);
  - its part paragraph names PART-09, which no longer exists.

### Readiness and interaction cost

`readiness: NEEDS_RULING` (the PART-06 question).

    interaction_cost = open rulings 1 + 2 + review cycles 1 + installs 1 + merges 1 + freeze 1 = 7

- **Counting convention:** as the parent's, where one install event is 1 and the freeze start and lift
  is 1.
- **Already spent in ANALYZE:** five Product Owner answers (rulings 1–4, and the widening itself). The
  parent's final tally counted those as actual.
- **Calibration:** the parent predicted 11 and took 29, including four extra review rounds. Each extra
  round here adds 1.

### Repairs from the ANALYZE review

Two independent reviewers, run `wf_1ac3cdc2-156`, both returned NEEDS_REPAIR. Every finding is dealt
with above.

- **Required findings:**
  - lane verdicts that disagreed on a shared sentence, now reconciled by the census;
  - items whose premise was refuted (20, 21, 38);
  - three class errors (PART-08, PART-10, PART-15);
  - the missing class A decision-record gate;
  - Decision 1, where a skipped revision bump broke the unspent-identity rule;
  - ruling 4's receiver wording;
  - execution order, cut-over and freeze;
  - PART-06's policy step, now an open question;
  - ITEM-16 reaching tw-flowmaster.
- **Non-blocking findings:**
  - PART-18's body count;
  - PART-05's scope;
  - missing guard targets;
  - evidence gaps;
  - ITEM-13 half landed;
  - the front-matter closure shape;
  - Intake staleness;
  - PART-15's tier;
  - the install-counting convention;
  - the stale Alpha lines in skills (ITEM-39);
  - ITEM-36's measurement and its policy-document target;
  - D24 coupling;
  - the builder text;
  - the proposed body (ITEM-40);
  - ITEM-09's description;
  - ITEM-29's exact wording;
  - per-part gates.
