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
readiness: READY
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 11
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
    statement: "The contract regenerator and the registry deriver live in glow-graph-contract as maintained scripts, and the pre-E2 contract they need is kept in the repository, so the shipped 091426.1 contract 6902924a… regenerates byte for byte from repository sources."
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
    statement: "D22 has guards that fire on regression: CONTRACT_REQUIRED holds ITEM-08's override sentence in change-flow and session-relay-flowmaster; CONTRACT_FORBIDDEN, or the owning skill's own suite, forbids every retired body-copying or body-hashing phrase this Modification removes from change-flow, session-relay-flowmaster, flowmaster-validate and amthor-workspace-governance-audit; a governance-audit fixture proves prompt-kind sources carry no digest. tw-flowmaster is excluded (out of scope), and the residual limit, prose paraphrase, is recorded under D14."
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
    statement: "The four CL-* bodies' 'PR-40 merge-approval effect … defined above' names the PR-40 entry the section describes once ITEM-29 lands (MERGE_OBSERVED first, Nathan's assertion only as fallback), and states that entry approves nothing (Flow Index: a published page, a passing check or a historical receipt 'creates no runtime approval')."
    source: "CLOSE-OUT-20260923 §4.E"
    disposition: ""
  - id: ITEM-22
    statement: "The registry's 16 lane notion_parent_id and 55 row expected_parent_id values, and their 70 titles, name each prompt's actual 091426.1 parent page, so the governance audit's parent check (NAM-002) holds."
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
    statement: "No installed skill this Modification packages states the retired D18 Alpha state as current: change-flow/SKILL.md:335 ('the sole operative state is ALPHA_STOPPED…'), flowmaster-validate/SKILL.md:174, and the governance audit's interoperability-contracts.md:96 and behavioral-fixtures.md:59, with the validator markers that require change-flow's line (change-flow validate_gcfpe_20260914.py:1033, flowmaster-validate validate_gcfpe_20260914.py:2692) moved with it. The graph's and contracts' alpha_resumption_contract follows the Product Owner's answer (§A, Open questions 3)."
    source: "ANALYZE completeness review and broad match over the packaged skills, 2026-09-23 (ALPHA_STOPPED, PR04 not started, 'sole operative state')"
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
    statement: "The 10 live bodies carrying 'Embed only applicable workflow contracts' (A3a) lose it, with its trailing 'do not restate them as independent reusable prompt policy' clause (A3b) where the two form one sentence; the 5 carrying 'candidate URL tokens must be replaced' (A4a) lose it; CL-40's 'This authoring candidate does not perform that update' (A4c) is resolved to match the PART-06 answer. Correctly scoped prohibitions (A3c, A3d, A4b) stay."
    source: "ANALYZE anchor census A3 and A4, one verdict per sentence"
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
    statement: "C-LAT's 'Decide it during work' block in the eight bodies that implement nothing (PR-10, PR-20, PR-40, RS-10, RS-20, DOC-10, DOC-20, IA-30) is changed as the Product Owner rules on the re-asked question (§A, Open questions 2), recorded as a D23-C successor."
    source: "ANALYZE completeness critic; C-LAT is placed verbatim by the parent's step 22 (spec v2 §3), so this changes a canonical placement and needs a Product Owner ruling"
    disposition: ""
  - id: ITEM-38
    statement: "PR-10's 'material change (D23-C) change' loses its doubled word, as a rider on PR-10's PART-15 edit. The '(D23-C)' form itself stays: it is the parent's recorded STEP22-BEFORE settlement (evidence/e3/E3-E4-report.md:112)."
    source: "ANALYZE sweep: PR-10, PR-35, PR-40, DOC-10 read 'material change (D23-C)'; spec v2 step 22"
    disposition: ""
  - id: ITEM-40
    statement: "The unpromoted GCFPE-MGMT-10 PROPOSED BODY carries none of the classes the census measured on it and this Modification removes (anchors A1, A2, A3a with its A3b clause, A4a, A5 and A8; it has no handoff-content instruction), so its promotion cannot reintroduce them. Its read-only 'Must not: change anything' lines and its design-level contradictions are recorded for the D20 redesign's stage 5, not resolved here."
    source: "ANALYZE anchor census of page 3e34590a05eb811b93d2da9b4ef8106d (evidence/closeout-residuals/ANALYZE-anchor-census.md)"
    disposition: ""
parts:
  - id: PART-01
    name: "Skill text applies D23-B and D7; the PR skill's revision moves and the contract is regenerated"
    items: [ITEM-01, ITEM-02, ITEM-14]
    class: B
    after: [PART-04]
  - id: PART-02
    name: "Skills stop copying and hashing prompt bodies, and D22 gets its guards"
    items: [ITEM-04, ITEM-05, ITEM-06, ITEM-08, ITEM-16]
    class: B
    after: []
  - id: PART-03
    name: "Skill text states what rulings already settled"
    items: [ITEM-03, ITEM-07, ITEM-09, ITEM-10, ITEM-25, ITEM-39]
    class: B
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
    after: [PART-06]
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
    name: "C-LAT in the non-implementing bodies, as ruled on Open question 2"
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

*Written by MODE = ANALYZE, 2026-09-23. Two review rounds checked it:*

- *round one, `wf_1ac3cdc2-156`: 11 required findings;*
- *round two, `wf_4bf0baec-6cc`: 14 required findings, all against the repair;*
- *round three: a verifier's check of round two.*

*This version answers both rounds and a third verifier's check. The sub-points still open are named in the closing section.
Evidence, all under `evidence/closeout-residuals/`:*

- *`ANALYZE-body-evidence.md`: the sweep, its re-check verdicts, and the re-verification of ITEMs 17–21
  and 23;*
- *`ANALYZE-anchor-census.md`: one verdict per shared sentence;*
- *`ANALYZE-skill-evidence.md`: skill items, the registry mapping and the revision pins;*
- *`ANALYZE-closure.md`: `closure.py` output.*

### Product Owner rulings received during ANALYZE

1. **The Candidate CRD Items List lives in Notion** (Nathan, 2026-09-23: *"candidate CRD can live in
   notion, I don't think it is a huge doc"*). No Notion page for it exists yet. The only copy is the
   Drive file `Candidate-CRD-Items-List.md` (`1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`, 31 923 B, last
   modified 2026-09-08). ITEM-18 therefore needs a Notion page. Whether CL-40 itself writes it is *Open question 1*.
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
4. **ITEM-37, first answer.**
   - **What was put to Nathan:** option (b), "in those eight bodies step 2 reads 'hand it to the
     implementing PR owner, who decides, implements, tests and records it'. The test is unchanged."
   - **His reply:** *"yes those words don't seem to mean anything do they"*.
   - **Why it is asked again:** review showed (b)'s receiver wrong for PR-40, which runs after the merge
     and whose defects re-plan through PR-20 (D23-F), and for IA-30 and PR-10, which run before any PR
     owner exists. A different reading would change what he approved, so the question is re-asked
     below. It is not decided here.

5. **Open questions 1–3 answered** (Nathan, 2026-09-23: *"ok approved"*, to the three recommendations):
   - **Q1 (A):** CL-40 writes the Candidate CRD Items List in Notion, under a destination rule naming that
     one page.
   - **Q2 (a):** C-LAT's three-step *Decide it during work* block is removed from PR-10, PR-20, PR-40,
     RS-10, RS-20, DOC-10, DOC-20 and IA-30; the Material definition and each body's own routing stay.
   - **Q3 (A):** the graph's and contracts' `alpha_resumption_contract` stays as the promotion-time
     record; the two validator checks are renamed to promotion-record checks, and the graph does not
     change.

### Open questions for the Product Owner

All three were answered by ruling 5 and are kept as asked.

1. **PART-06: does CL-40 write the Candidate CRD Items List in Notion itself?**
   - **What CL-40 does:** it runs at the end of each change, scans for PF09 gaps and CRD candidates, and
     adds new candidates to the list.
   - **What breaks:** a flow prompt is read-only to Notion unless a destination rule names the page.
     With no writer, the list goes stale, which is the failure that retired the D18 block.
   - **(A) Recommended.** A destination rule names the one page, CL-40's registry `mutations` row
     allows the write, and CL-40's A4c sentence goes. The cost is one policy entry.
   - **(B)** CL-40 records candidates only in its committed `CYCLE_GAP_SCAN`, and Nathan or a
     maintenance run copies them over. Then CL-40's step 7 and its A4c sentence must change too, so it
     stops attempting the update.
   - **(B)'s cost:** no new write path in this run, and the same edit count. It adds one copying round
     trip after every change, indefinitely.
2. **ITEM-37, re-asked: C-LAT in the eight bodies that implement nothing.**
   - **What the bodies are:** PR-10 writes work-unit instructions; PR-20 plans; PR-40 reviews after
     the merge; RS-10 proposes a rescope; RS-20 reviews one; DOC-10 writes documentation instructions;
     DOC-20 verifies them; IA-30 reviews the whole-change plan.
   - **What breaks:** each carries C-LAT's three steps. Step 2 tells it to "decide it, implement it,
     test it", which none of them can do. PR-40, a read-only reviewer, is told to implement a fix, where
     D23-F sends it to REJECT and re-plan.
   - **(a) Recommended. Remove the three-step block and keep the Material definition.** Each body's
     own routing already sends a material change to rescope, and handles the rest by its role. The
     three steps are an implementor's procedure.
   - **(b′) Remove step 2 only, keeping steps 1 and 3.** PR-40 would still read "otherwise, do not do
     it; record it as a candidate", which contradicts its REJECT route for an in-scope defect.
   - **(c) Leave the text as placed.**
   - **Cost:** (a) and (b′) cost the same, 8 body edits and a registry pattern each; (c) costs nothing.
3. **ITEM-39: the retired Alpha state inside the graph and the contracts.**
   - **What it is:** the graph's `global.json` and both 091426.1 contracts carry an
     `alpha_resumption_contract` with `state: ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR` and
     `next_intended_unit: HDE-EPIC040-PR04`. flowmaster-validate requires those values
     (`validate_gcfpe_20260914.py:1901-1908`).
   - **What breaks:** a machine record, validated on every run, asserts an Alpha state that was
     discharged on 2026-09-21. Today no prompt reads it for routing.
   - **(A) Recommended. Keep it as the promotion-time record.** The fields describe the resumption
     contract at promotion. The skills' prose says so, the validator check is renamed from a state check
     to a promotion-record check, and nothing that moves the graph digest is touched.
   - **(A)'s cost:** two check renames inside PART-03, and nothing else.
   - **(B) Retire it** from the graph, both contracts and the validators, including change-flow's
     `:1017-1018` successor-trigger check. The graph digest moves off `ae2bd159…`, and every recorded
     proof token and pin moves with it: the Flow Index, the register, `authoritative-surfaces.md`,
     `ecosystem-change-management.md`, the v5.0.0 pointer, validators and profiles.
   - **(B)'s cost:** a new part, after PART-01, that edits `global.json`, rebuilds the graph and
     regenerates the contract a second time; about a dozen Notion and repository token updates; and a
     likely extra review cycle (+1). It would also replace Decision 1's "the graph is not regenerated"
     and PART-04's byte-identical gate, which would then apply only to the reindex, before the
     retirement.

### Items whose premise the verification refuted

- **ITEM-20, proposed `NOT_APPLICABLE`.**
  - The sweep and the re-check found OPS-10's and OPS-20's mention bans correctly scoped
    (`LINK_OR_MENTION_BAN`: 0 REAL, 6 NOT_REAL).
  - They are correctly scoped: OPS-10's ban governs the `OPS_TASK` text it authors, and OPS-20's governs
    reusable handoffs, not a runtime handoff's direct URL. The census rule keeps correctly scoped
    prohibitions, and the same rule keeps A3c, A3d and A4b.
  - PART-08 therefore lands empty, and §E records the verdict.
- **ITEM-21 keeps its four bodies and loses its premise.** The reference does resolve, to *Product Owner
  merge action*. ITEM-21 now makes that reference name the PR-40 entry the section will describe once
  ITEM-29 lands: `MERGE_OBSERVED` first, the assertion only as fallback. It also says that entry
  approves nothing.
- **ITEM-38 is reduced to PR-10's doubled word.** `material change (D23-C)` is the parent's recorded
  STEP22-BEFORE settlement (`evidence/e3/E3-E4-report.md:112`). The typo is fixed as a rider on PR-10's
  PART-15 edit and has no guard, since it has no behaviour.

### Already landed during ANALYZE

- **ITEM-13's input.** The pre-E2 contract `2b78f877…` was kept at `evidence/pre-e2-contract/` in
  commit `245b21b`. PART-04 moves it to `docs/graph/` (maintained source) and uses it only to prove the
  regenerator: regenerating from it must give the shipped `6902924a…` byte for byte.

### Per part: class, tier, targets and gates

| part | class | tier, and why | targets | gates |
|---|---|---|---|---|
| PART-01 | B | 0: skill text and the contract's revision fields; no prompt produces anything different | skill: PR skill (01), relay (02, 14: text, `validate_relay_manifest.py`, self-test, examples), flowmaster-validate (`CONTRACT_FORBIDDEN`). Contract: regenerated with `primary_skill_revision` 1.3.1 and `contract_revision` 4.1.0 → 4.1.1, both bundled copies (change-flow, flowmaster-validate), and every pin (`EXPECTED_CANDIDATE_CONTRACT_SHA256`, `validation-profile.json:8`, `validation-profile.json:27-28` `installed_skill_revisions`, the contract-revision pins at change-flow `:751` and flowmaster-validate `:1477`, and `primary_skill_revision` at flowmaster-validate `:1816`). After PART-04 (regenerator) | readback; forbidden literals fired by injected regressions; the regenerated contract passes both validators; D24 review; install |
| PART-02 | B | 0: skill text, code and guards; the core bytes do not move | skill: flowmaster-validate, change-flow, relay, governance audit (text, code, fixture); decision record: a `D14` note recording the prose-paraphrase limit of ITEM-16's guards | ITEM-16 guards fired by injected regressions; the governance-audit fixture; `core_sync` true; D24; install |
| PART-03 | B | 0: skill prose brought into line with settled rulings (D23-G, D23-D, D13, D18's successor, promotion) | skill: flowmaster-validate (03, 39), governance audit (07, 39), glow-graph-contract (09 including its description, 25), change-flow (09's `:802` comment, 10, 39 at `:335`), the two validator markers that require change-flow's `:335`; under Open question 3 (A), the checks at flowmaster-validate `:1901-1908` and change-flow `:1017-1018` renamed from Alpha-state checks to promotion-record checks, values unchanged | readback; the moved markers fire on the old text; D24; install |
| PART-04 | C | 0: validators and graph tooling are controls; the build stays byte-identical | skill: flowmaster-validate (11, 15), glow-graph-contract (12 with `reindex` and its documentation, 13); graph: `docs/graph/parts` reindex; `docs/graph/` home for the pre-E2 contract; a dated correction note on the repair-a4 record's C8 and §2 | build byte-identical (`ae2bd159…`); the builder rejects an injected count mismatch; fixture cases for 11; the five a5 regressions; the regenerator reproduces `6902924a…` from the kept input; D24; install |
| PART-05 | B | 0: wording aligned with what the bodies already do (ruling 2); nothing they produce changes | prompt: 15 bodies (CL-20, CL-30, CL-40, CL-E-20, DOC-20, ESC-25, GCFPE-MGMT-10, OPS-10, OPS-30, PR-20, PR-35, PR-40, PR-50, QA-10, RS-40); decision record: ruling 2's entry; registry patterns | readback; a forbidden pattern per retired phrasing, including A10, fired by regression |
| PART-06 | A | 1: changes what CL-40 writes and where | prompt: CL-40. Notion: a new *Candidate CRD Items List* page under the Glow Operations Hub, created by `GCFPE-MGMT-10` at EXECUTE and migrated from Drive `1JPN7Wcq…`. Rule: the destination rule (answer (A)). Registry: CL-40 `mutations`, guard. Decision record: ruling 1's entry. Product Owner action: banner the Drive file as superseded (Drive is his). The only repository mention of the Drive list (`docs/ephemeral/HDE-EPIC040-PR40-workspace-register.md:206`) is inside a dated 2026-09-09 snapshot of a Notion page and stays as written (`AUTH-001`) | decision-record entry committed before any EXECUTE edit; readback of the migrated list against the Drive source; guard fired by regression; corpus gate |
| PART-07 | D | 1: changes what the closure memo records when no board is supplied | prompt: CL-20; registry assertion | assertion added and fired by regression |
| PART-08 | B | 0: wording only, and proposed `NOT_APPLICABLE` | prompt: OPS-10, OPS-20 | none: proposed `NOT_APPLICABLE` |
| PART-10 | C | 0: registry data (a control) | registry: 71 parent IDs and 70 titles | NAM-002 run on a snapshot of actual parents, and failing on one injected wrong parent |
| PART-11 | B | 0: not a release member | Notion: the proposed MGMT-10 body (23, 40); the redesign tracking page records ITEM-40's deferred contradictions and read-only lines for stage 5 | readback; the gate runs directly, as PLAN's patterns for A1, A2, A3a, A4a, A5 and A8 plus the whole-body release-line pattern, against the body; it needs no other part to have landed |
| PART-12 | B | 0: reporting format | skill: `glow-po-reporting`; Notion: Hub *Worker communication rules*; rule: `session-working-rules.md` | readback; D24; install |
| PART-13 | B | 1: changes what handoffs carry | prompt: 48 bodies (46 with REAL routing findings, and every A1 and A2 carrier); registry patterns (ITEM-28) | patterns fired by injected regressions; corpus gate |
| PART-14 | B | 1: changes PR-35's and RS-40's lawful results and how PR-40 is entered | prompt: 21 bodies with A7 (CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10, QA-20), plus PR-35, RS-40 (30) and PR-40 (31); registry patterns | forbidden patterns for assertion-only entry and for "ordinary in-scope defect remains with the existing PR owner"; required A1-5 wording; required `MERGE_OBSERVED` in PR-35's and RS-40's result lists; each fired by regression; corpus gate |
| PART-15 | D | 1: CL-40's A4c changes whether CL-40 updates the list | prompt: 11 bodies (CL-20, CL-30, CL-40, CL-C-10, CL-E-10, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10); registry assertions. After PART-06 | assertions added and fired by regression |
| PART-16 | D | 1: changes result routing text | prompt: QA-110, QA-80; registry assertions | assertions fired by regression; text matches the graph (`D13`) |
| PART-17 | B | 0: guard widening | registry: the release-line guards on 55 rows; skill: flowmaster-validate `PROMPT_BODY_RELEASE_HEADER`; rule: `prompt-body-content-policy.md` | 0 live label lines, so no false positive; a label injected past line 8 fails |
| PART-18 | A | 1: changes a canonical placement | prompt: the 8 bodies (per Open question 2); registry: C-LAT patterns on those rows; decision record: `D23-C` successor; the PE Metaprompt GCFPE overlay and any skill copy stating C-LAT's placement | successor committed before any EXECUTE edit; pattern fired by regression; corpus gate |

Notes on the table:

- **PART-09 was dissolved.** ITEM-21 moved to PART-14.
- **ITEM-14 moved from PART-03 to PART-01.**
- **PART-17 is within D23-G.** `prompt-body-content-policy.md` already forbids "any field whose value
  changes because of a release event", with no header limit. The check's eight-line window was an
  implementation limit, not the rule.
- **No graph part changes routing.** The Modification is Tier 1 (`gate_tier: 1`) because PARTs 06, 07,
  13, 14, 15, 16 and 18 change what prompts produce.

**Closure.** 50 live prompts touched, radius **55 of 55**. The Tier 1 gate is the full corpus: the
registry validator over all 55 live bodies, and every installed suite. The front matter holds the
unions: 51 upstream, 50 downstream, 43 state sharers. Per prompt (full output in
`ANALYZE-closure.md`):

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
  3. **Exact census:** ten anchors over the 55 live bodies and the proposed MGMT-10 body.

  The census governs shared sentences: one verdict per sentence, applied to every carrier. One rule
  decides the author-directed rows and the mention bans alike: a positive instruction to the prompt's
  author, which an executor could act on, goes; a prohibition correctly scoped to what the executor
  actually writes stays. A3b goes with A3a where the two form one sentence (its "them" refers to A3a's
  contracts); PLAN confirms this per body. Measured part scopes:
  - PART-05: 15 bodies;
  - PART-13: 48;
  - PART-14: 21, plus PR-35 and RS-40;
  - PART-15: 11;
  - PART-17: 0 live label lines;
  - touched overall: **50 of 55**.
- **Skills.**
  - A broad paragraph scan of every GCFPE-bound skill's `SKILL.md`, references and scripts looked for
    a body noun with a copy or identity verb (D22), a handoff with a carry verb (D23-B), `drive` (D7),
    and numeric counts. It returned 31 candidate sites, each read in turn.
  - A second broad match looked for the retired Alpha state (ALPHA_STOPPED, "PR04 not started", "sole
    operative state"). It found 4 prose sites plus the machine records, which are Open question 3.
  - Two verifiers reproduced or refuted every surviving item (`ANALYZE-skill-evidence.md`).
- **Registry.** The six-ID mapping, measured from the parent pages' child lists, is in
  `ANALYZE-skill-evidence.md`.

### Decisions this analysis made

Each applies a ruling or rule already in force.

1. **Revisions move** (`skill-identity-and-freeze.md`: "Corrected bytes never reuse one"):

   | item | from | to |
   |---|---|---|
   | flowmaster-validate | 3.3.0 | 3.3.1 |
   | change-flow | 3.3.0 | 3.3.1 |
   | relay | 3.1.0 | 3.2.0 |
   | PR skill | 1.3.0 | 1.3.1 |
   | governance audit | 1.12.0 | 1.13.0 |
   | the 091426.1 contract | 4.1.0 | 4.1.1 |

   - The contract is regenerated because it carries the PR skill's revision. The graph is not
     regenerated.
   - glow-graph-contract and glow-po-reporting advertise no revision, so their identity is the freeze
     digest (`D19`).
2. **The relay's GCFPE model and reasoning advice is deleted (ITEM-02).** This applies the
   retired-assessment rule.
3. **The governance audit changes its code as well as its text (ITEM-05).**
4. **The relay keeps `GOOGLE_DRIVE` for non-GCFPE projects and adds `REPOSITORY` (ITEM-14).**
5. **Graph counts appear once, as a dated proof token (ITEM-09),** in the text and the description.
6. **The registry deriver imports the governance audit's `load_data` (ITEM-13).** That keeps one
   parser, and the two packages are installed together.
7. **CL-20's board stays a runtime reference (ITEM-19),** pending with its PF04 §9.1.1 owner when none
   is supplied.
8. **QA-80 and QA-110 follow the graph (`D13`).**
9. **ITEM-11 is fixed in place.**
10. **Where a handoff block closes a message, the named state goes immediately before it (ITEM-24).**
11. **ITEM-40 covers only the classes this Modification removes.** The census found design-level
    contradictions in the proposed MGMT-10 body: result codes, which session writes the approval fields,
    and artifact locations, among others. They go to the D20 redesign's stage 5, "fix what the pilot
    exposes". They are recorded on the redesign tracking page at EXECUTE and not resolved here, because
    each needs a design choice that the D20 track owns.

### Order, cut-over and freeze

1. **Record pull request.** This record, with its ANALYZE and PLAN, merges from
   `claude/epic-tesla-17406z` before EXECUTE (the parent's #474 pattern). The close-out §6 commits
   travel with it. A merge preserves the record and approves nothing (`D21-C`).
2. **Execution branch.** EXECUTE's first commit is the decision-record entries: ruling 1 and ruling 2
   (PART-06, PART-05), ruling 4 and Open question 2's answer as a `D23-C` successor (PART-18), and
   Open question 3's answer. `GCFPE-MGMT-10` commits them before any other edit, which meets the class
   A gate.
3. **One install event.** All seven packages are reviewed together: two D24 reviewer subagents, with
   the filled brief committed before either is spawned. They are installed in one sitting. Three
   couplings force this:
   - flowmaster-validate pins change-flow's and the relay's revisions and the contract digest;
   - glow-graph-contract imports the governance audit;
   - PART-01's regenerated contract ships in two packages.

   The graph-parts reindex reaches `main` in the execution pull request before the stricter builder
   is installed.
4. **Bodies land under a freeze.** It starts before EXECUTE's first Notion write and lifts after full
   readback and the corpus gate. The new registry patterns are evaluated against the landed bodies in
   the same sitting, and the execution pull request merges only after that. PR05 planning waits on
   the freeze, which Nathan scheduled for after this run.

### Unguarded items, with the reason

- **ITEMs 03, 07, 09, 10 and 25** are skill prose with no suite that reads meaning; the D24 review
  holds them.
- **ITEM-39** is guarded only at change-flow's `:335`, by the moved validator markers. Its other three
  prose sites have no guard: flowmaster-validate `SKILL.md:174`, and the governance audit's `:96` and
  `:59`.
- **ITEM-24** is prose in a prose skill.
- **ITEM-38** is a typo with no behaviour.
- **ITEM-36** is itself a guard.

### Contradictions and risks

- **The parent's gate passed every one of these findings,** with 0 of 1 484 assertions failing,
  because its guards tested presence, not removal. Every new class therefore gets forbidden patterns
  fired by injected regressions (`GUARD-001`).
- **D22's prose guard is weaker than prototyped.** It missed 30 of 30 paraphrases, so ITEM-16 now pins
  exact phrases. The residual limit is prose paraphrase.
- **Notion storage.** A strikethrough across bold and code turned into literal tildes today, and at E6
  a blank-line window was exposed on 10 bodies. So EXECUTE uses exact-anchor replacements, puts no
  strikethrough in bodies, reads everything back in full, and reads the migrated list back against
  Drive.
- **D24 coupling.** PART-01 spans 4 packages (the PR skill, relay, flowmaster-validate, and change-flow through the contract copy), PART-02 spans 4 and PART-03 spans 4. One rejected edit
  blocks its part, re-cuts several packages, and needs fresh reviewers. The parent took five rounds.
- **Which MGMT-10 body governs this run.** The live 091426.1 body, as read when the run began. PART-05's
  edit to it applies to later runs. PART-11 (ITEMs 23 and 40) edits the proposed body, which does not
  govern this run.
- **change-flow tells agents Alpha is stopped today** (`:335`). Any session that loads change-flow
  before this Modification installs reads a false Alpha state. PR05 planning is scheduled after this
  run, which is the reason not to plan PR05 earlier.
- **Canonical texts are not edited,** except by the Open question 2 answer. PR-35's "as before" is
  canonical C-SUB wording and stays.
- **Not included.**
  - **TW, which is out of scope.** tw-flowmaster's GCFPE binding keeps the core's content pin, an
    "optional digest" (`:306`) and three model-advice lines (`:313`–`:317`), with no D22 override or
    guard. AF-012 also stays open for TW.
  - **The proposed MGMT-10 body's design contradictions,** which go to D20 stage 5.
- **Defect classes matched:**
  - `DERIV-001`: handoffs restating artifacts;
  - `GUARD-001`: guards that never fired;
  - `SCOPE-001`: measured by effect;
  - `FUNC-001`: read-only claims judged by behaviour;
  - `NORM-001`: harmless prohibitions left alone.
- **Findings on upstream sections** (template rule 1, recorded rather than edited):
  - the opening sentence's "five prompt bodies" is now 50 live bodies plus the proposed MGMT-10 body;
  - the Intake's "none is ruled on in D1–D24" is false for ITEM-08 (the A1-6 precedent), ITEM-24 (a D23
    successor) and ITEM-29 (D23-E);
  - its part paragraph names PART-09, which no longer exists.

### Readiness and interaction cost

`readiness: READY`. Open questions 1–3 were answered by ruling 5.

    interaction_cost = open rulings 3 + 2 + review cycles 1 + installs 1 + merges 2 + freeze 1 + Drive banner 1 = 11

- **Counting convention:** the parent's. One install event counts 1. Merges count the record PR and
  the execution PR. The freeze start and lift counts 1. Nathan's Drive banner (PART-06) counts 1.
- **Already spent in ANALYZE:** four Product Owner answers (rulings 1–4). The widening is ruling 3.
- **What a split would save:**
  - Moving PART-06 or PART-18 to its own run saves one ruling here. It costs that run's own two
    approvals and a merge, and a second registry edit and readback. That is a net loss of 2 or more.
  - Moving Open question 3 to its own run saves 1 here and costs that run's 2 approvals and a merge, a
    net loss of 2.
- **Calibration:** the parent predicted 11 and took 29, four of them extra review rounds. Each extra
  round here adds 1.

### Repairs from the ANALYZE reviews

- **Round one** (11 required findings):
  - lane verdicts reconciled by the census;
  - ITEMs 20, 21 and 38 dispositioned;
  - class errors corrected;
  - class A gates;
  - revisions moved;
  - ruling 4 re-asked;
  - order, cut-over and freeze;
  - PART-06 as a question;
  - ITEM-16 without TW.
- **Round two** (14 required findings):
  - one rule for author-directed text and mention bans, with A3 and A4 split per sentence;
  - ITEM-37 re-asked, not decided;
  - `contract_revision` moved and the regeneration placed in PART-01, after PART-04;
  - the tier rationale restored and the split saving stated;
  - PART-06's page parent, creator and Drive action;
  - ITEM-39 measured, with change-flow `:335`, its validator markers, and the machine records as a
    question;
  - A10 counted;
  - ITEM-40 limited to this Modification's classes;
  - PART-15 ordered after PART-06;
  - ITEM-21 reworded;
  - the PART-40 typo removed;
  - package spans corrected;
  - ITEM-20 attributed to the sweep.
- **Round three** (a verifier's check of round two: 4 findings not yet resolved and 5 new):
  - the mention-ban premise restated as "correctly scoped";
  - `validation-profile.json:27-28` and flowmaster-validate `:1816` added to PART-01's pins;
  - ITEM-13 names `6902924a…`;
  - PART-08's tier;
  - the split-saving claim corrected;
  - the Drive mention recorded as a dated snapshot;
  - ITEM-39's three unguarded sites listed;
  - PART-01 spans 4 packages;
  - ITEM-40 and PART-11's gate limited to the classes measured on the proposed body;
  - Open question 3 carried by PART-03 (A) or a new part (B), with costs;
  - option costs added;
  - A3b goes with A3a where they form one sentence;
  - the skill-evidence table updated;
  - PART-18's name made neutral;
  - Decision 11's tracking-page record placed in PART-11;
  - ITEM-16's D14 note placed in PART-02.
- **Non-blocking sub-points still open:**
  - skill hit counts per class: only the 31-site total is recorded;
  - the merge count depends on Nathan merging the record PR separately (#478).
