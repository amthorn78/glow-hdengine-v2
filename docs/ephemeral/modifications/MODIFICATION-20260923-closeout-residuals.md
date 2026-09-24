---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
modification_id: MODIFICATION-20260923-closeout-residuals
status: EXECUTING
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
item_count_at_approval: 40
interaction_cost_actual:
estimate:
  plan: "2 h and 2.5M tokens for this resume under D26 (the dry run, one diff check of the successor, two returns); set 2026-09-24 by the resumed PLAN, for the work still to come (D26 transition)"
  execute: "8 h of session time and 8M tokens (X0 to X7.7, one D24 round of two reviewers, the 50-body landing and two corpus gates in lanes); Nathan's merges and install sitting add wall-clock time on top"
reviews:
  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-24
    required_open: 1
    outcome: "Every normal-path gate read-only on fresh fetches and the manifest in order on main d179277: all pass except TRACK-STATUS-01..03, whose anchors stage 5 removed from the tracking page (X4.6 and X7.7 fail loudly). ESC-25 not rehearsed: the permission classifier refused the command. D26-F trigger 2: one bounded check, then back to Nathan (DN-8)"
  - mode: PLAN
    kind: DIFF_CHECK
    date: 2026-09-24
    required_open: 2
    outcome: "PLAN-DC-1 and PLAN-DC-2, independently: the same 2 required defects (a restart after a lost session re-runs a rejected D24 review unseen; X7.6's PR body waits for the withdrawn X7.7), plus 16 and 13 listed, all in the successor's own text. The cap is reached: returned to Nathan unrepaired"
  - mode: SKILL
    kind: FULL
    date: 2026-09-24
    required_open: 0
    outcome: "D24 round cr1 at X4.4: SFR-CR1-1 and SFR-CR1-2 both SKILL_FIT_CONFIRMED on the seven archives in EX/packages.json; the archives, brief and verdicts delivered to Nathan"
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
analyze_approved_by: Nathan
analyze_approved_date: 2026-09-23
plan_approved_by: Nathan
plan_approved_date: 2026-09-24
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

**ANALYZE approved** by Nathan, 2026-09-23 (*"yes"*, confirming that his "ok approved" also approved the analysis). Scope froze at 40 items in 17 parts.

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

## §P — Plan

*Written by MODE = PLAN, 2026-09-23; repaired 2026-09-24 after the second to seventh PLAN reviews. The analysis was approved by
Nathan on 2026-09-23 ("yes"). Scope stays frozen at 40 items in 17 parts.*

**The specification.** Every edit, literal, guard, package, command and check is in
`docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-closeout-residuals.md` (the spec, below). Its evidence
is in `evidence/closeout-residuals/plan/` (`EV`). The steps below cite the spec's sections, and §9 of the spec
orders them with an actor, a gate and a readback for each.

**How the plan was built and checked:**

1. **A first PLAN workflow** (`wf_73fca782-464`) drafted the rules, the edits to all 51 bodies (read completely),
   the registry and the seven skill packages. Its two reviewers returned 26 required findings.
2. **A repair round** (`wf_22dee43c-01f`) worked from one decision file (`EV/DECISIONS.md`). It drafted the
   repository texts and the control-page edits, cut the seven packages as one tree, and repaired the registry guards.
3. **The body edits became one engine** (`EV/engine/`). EXECUTE lands with the same code the dry runs used.
4. **Dry runs.** Pass 1 was rule level. Pass 2 was the complete check: 56 of 56 bodies passed (50 live, 5 untouched
   live, and the proposed MGMT-10 body).
5. **A second review** (`wf_045af16b-3ed`, three lenses) returned 7 required findings on order, paths, landing units
   and one guard. Repair round 2 (`wf_9c136682-f25`) answered them (P-55 to P-70; spec §2.4), and repair round 3
   settled the close order and the tokens (P-66 revised, P-71 to P-74; spec §2.5).
6. **A third review** (`wf_b886670d-753`, three lenses) returned 16 required findings, several shared between lenses.
   The main ones were that the readback could never pass on CL-40, that the rollback journal conflicted with `D22`,
   that the two landing units split parts, and that the failure paths were incomplete. Repair round 4 answered them
   (P-57 and P-58 revised again, P-75 to P-83; spec §2.6). **Pass 4 rehearsed `land.py` itself**, including the
   readback each landing will run, on every body (spec §8).
7. **A fourth review** (`wf_05b74ccf-d84`, three lenses, each followed by a verifier that tried to refute its
   findings) returned 11 required findings: the stop and resume procedures, the day D25 applies, evidence that a new
   session could not recover, forward repair the engine could not do, one Notion formatting trap, asynchronous
   writes and the manifest's removal commands. Repair round 5 answered them (P-84 to P-95; spec §2.7). **Pass 5**
   tried, on every body, each landing operation left out alone and each applied alone: none was repaired to anything
   but the landed page (spec §8.4). It found one engine defect on QA-10, fixed and re-run (P-88).
8. **A fifth review** (`wf_ad66aa45-00a`, three lenses, each with a verifier) returned 10 distinct required defects.
   A step resumed on a later day could not recognize its own landed edits. The stop's list of Notion writes could miss
   an earlier session's. A stop's record never reached `main`. The stop marked everything `BLOCKED` while landed bodies
   were still live. A resumed landing on a deletion-only body was refused. A lease push could be stale. The D24 brief
   was left to author. A new session after the install would re-patch the installed tree. A tracking line claimed a
   record before it existed. The verdict's binding reinterpreted the canonical template. Repair round 6 answered them
   (P-96 to P-102; spec §2.8). **Pass 6 ran `land.py`'s own refusal chain on every body**: all 51 landed texts refuse
   `ALREADY_LANDED`. Of 476 distinct partial landings, 410 are repaired to exactly the landed page, 66 are refused
   (which stops the unit) and none is repaired to anything else (spec §8.5). The new read-only helpers ran on today's
   pages: the control-page sequences, the anchor check, the Drive check, NAM-002 on the live hubs and the brief (spec
   §8.7).
9. **A sixth review** (`wf_bafe0805-392`, three lenses, each with a verifier) returned 10 distinct required defects.
   The step after the install could not be resumed in a new session. A stop could carry half-applied edits to `main`,
   and returned to Nathan before its tracking lines were written. A stop at the first Notion write, or on a changed
   tracking page, left a check that could never pass. The sweep could not read CL-40 before the page existed. Nothing
   recorded that the packages were delivered. A re-run could insert a text twice, in the repository or in Notion. The
   new page's readback had no tool. A resumed step could re-date its own writes. Repair round 7 answered them (P-103
   to P-111; spec §2.9): one branch rule for every start and resume, a stop record that returns only when complete,
   values recorded once, a delivery record, and tools for the new page. **Pass 7 re-ran every body** with operations
   that, sent a second time, match nothing: 0 of 262 could land twice (spec §8.5).
10. **A seventh review** (`wf_ca01df8d-ee0`, three lenses, each with a verifier) returned 7 distinct required defects.
   A control edit sent twice could survive a stop unlisted, and one the unit wrote could pass the restoration check.
   The new page's step could not be resumed. A resumed stop could not name its failure. After the execution PR's
   merge, a lost archive or a failure had no working route. One stale readback at the first Notion write recorded
   that nothing was written. The reviewer brief after the merge said the wrong thing. Repair round 8 answered them
   (P-112; spec §2.10): a committed list of the control edits the unit writes, a stop that commits its failure
   first, a page step that reads its stage from the page, readbacks that retry, and no re-cut after the merge. The
   proofs now include checks that must fail: a missed reversal, a doubled pointer, a stop line removed (spec §8.7).
11. **The skills.** Every suite passes on the patched tree, and every must-fail regression fires. The contract
   regenerates byte for byte. The suite gate is a script with its expected results built in.

### Rulings this plan applies

The Product Owner rulings in §A (1 to 5) are applied as recorded. The PLAN decisions P-01 to P-112 (spec §1) apply them
or settle a finding; none needs a new ruling. These settle something the analysis left to PLAN:

- **P-02:** R-OWN's sentence also covers the pull request that carries a prompt's outputs (D25-B credits it to the
  approved plan).
- **P-37:** a prompt's own intake list may name `CANON_CONFLICT_REGISTER`.
- **P-43:** the policy line and the repair-a4 note land after the install, in the close-out PR.
- **P-57, P-84 revised, P-88, P-98, P-99, P-107, P-108, P-112:** nothing leaves the branch before the freeze line,
  the first Notion write. A stop before that line is listed for writing reaches `main` by a record pull request, and
  Nathan ends the Modification or approves a plan change, after which EXECUTE starts again from `main`. From that
  listing all 17 parts land as one unit. A failed readback is repaired forward: the engine lands only the edits still
  missing. A failure it cannot repair stops the unit. EXECUTE then commits the failure, sweeps Notion for every
  landed write, reverses every control-page edit it listed or finds landed, moves the new page to trash, records the
  stop on `main` at `EXECUTING`, and writes the tracking page's stop lines before returning. Nathan restores the listed bodies, a restoration check verifies every page, and
  then he ends the Modification or approves a plan change.
- **No rollback journal (P-58 revised again, `D22`).** Nothing keeps a copy of a body, so restoring a landed body is
  Nathan's action, from Notion's page history. The sweep tells him exactly which pages to restore, and the check tells
  him when he is done.
- **P-96, P-103, P-104, P-106:** every value a Notion write carries, such as a date or the page URL, is recorded once
  in the evidence before the write, every Notion call is built so that sent twice it lands once, and every start or
  resume of EXECUTE follows one branch rule. So any step can be resumed in a new session, on any day, without landing
  anything twice.
- **P-100, P-109:** the reviewers' verdicts bind to the archives they read, and those archives are delivered to Nathan
  at the review's end, one per message, and the delivery is recorded; nothing is re-packaged after that. After the
  execution PR merges nothing is re-cut at all: an archive he no longer holds he saves again from its message
  (P-112 (d)).
- **P-86:** `D25` applies from the merge of the execution pull request; §E records that commit and its date.
- **P-66:** the freeze runs from before the first Notion write until Nathan lifts it after the post-install
  verification (an upstream finding against §A order 4).

### Steps

| # | part | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|---|
| 1 | all | the base | Preconditions (spec §9 X0): record PR merged; branch restarted from `main`, `$BASE` recorded in `EX/run.json`; base checks | template rule 2 | the registry, the 7 installed packages, the graph and the engine self-test equal the recorded base; the root digest is recorded (P-79) | stop: the stop record (P-84 revised, P-107) |
| 2 | PART-01, 02, 03, 04, 12, 17 | the 7 skill packages, in the scratchpad | Build `$PKG` (the installed root with the 7 diffs applied); run the `pre` gate (X1) | classes B and C; unspent identity | every patch exits 0; each package digest equals the manifest; `run_gate.py --set pre` exits 0 | discard the scratch copies |
| 3 | PART-06, 18 (class A); PART-05; PART-02; PART-03; PART-17 | `gcfpe.decision-record.md` and this record | Commit 1: `status: EXECUTING` and D25 (D25-A, D25-B), the D23-C, D23-G and D18 successors, the D14 note (spec §6, label `X2.2`; X2) | rulings 1, 2, 4, 5; §A order 2; P-81 | each anchor found once; `^## D25` = 1; no added line starts `> `; `canon.py` still reads two once-per-merge lines; `modification_validate.py` passes; the commit also carries `EX/run.json` and `EX/gate_pre.json` | before X5.0 nothing has left the branch: a stop reaches `main` by a record PR (P-107); Nathan ends the Modification or approves a plan change, and EXECUTE then starts again at step 1 (P-84 revised) |
| 4 | PART-10, 13–18 (the registry's guards and parent IDs) | `project-prompt-contract-registry.md` | `git apply EV/registry/registry.diff`, committed alone (spec §4; X3.1) | `D14`, `GUARD-001`; ITEM-22 | sha256 equals spec §4.1; `valid: true`; deriver drift `[]` | as step 3 |
| 5 | PART-04 | `docs/graph/parts` | Reindex with `$PKG`'s builder (ITEM-12; X3.2) | class C | the stripped `git diff` equals the recorded diff; the build is byte-identical (`ae2bd159…`); a second reindex rewrites 0 | as step 3 |
| 6 | PART-04 | `docs/graph/contract-template/` | `mkdir`; move the pre-E2 contract; add its README (ITEM-13; X3.3) | class C | sha256 `2b78f877…` and `469e2265…` at the new paths | as step 3 |
| 7 | PART-12 | `session-working-rules.md` | `P32-SWR` (spec §6; X3.4–X3.5) | ITEM-24; P-32 | anchor found once; the sentence found once afterwards and byte-equal to P-32; a re-run applies nothing (P-104) | as step 3 |
| 8 | PART-10 | the registry's parent IDs and titles | NAM-002 and the title and lane checks on a live snapshot of the hubs (the child list by `ctrl.py children`), committed to `EX/nam002/` (spec §4.4; X3.6) | ITEM-22; P-63, P-77 | 0 findings; exactly one on each injected fault; the old registry gives 55, exit 1 | as step 3 |
| 9 | PART-01 | the bundled 091426.1 contract | Regenerate 4.1.1 on the working tree (X4.1) | `D13`; Decision 1 | `6902924a…` EQUAL x2 from the kept template; `dbae180b…` in both copies | as step 3 |
| 10 | PART-01, 02, 03, 04, 12, 17 | `$PKG` and the working tree | `run_gate.py --set pkg` (spec §5.3; X4.2) | `CHK-001` | exit 0, 34 rows equal to their expected results | as step 3 |
| 11 | PART-01, 02, 03, 04, 12, 17 | the 7 packages | Package and extract (`execute.4b`, `EX/packages.json`); fill the PLAN-drafted brief (`fill_brief.py`) and commit it; two fresh reviewer subagents; commit each verdict as it returns; deliver the seven reviewed archives, one per message, then the brief and verdicts, and record the delivery in `EX/run.json` (X4.3–X4.4) | `D24` | `Skill is valid!` ×7; the extracted digests equal `expected_after_patch.txt` (`diff` exits 0); `SKILL_FIT_CONFIRMED` from both, bound to the archive and freeze digests in the brief's §1; each delivered file's sha256 equals `EX/packages.json`; `delivered_cr<k>` committed (P-100, P-109) | a rejection stops EXECUTE: the repair, or shipping without a part, is a plan change Nathan approves (P-84 revised) |
| 12 | all body parts; PART-06 | the 56 pages; the Drive file | Rehearsal: `land.py plan --no-ops` on a fresh fetch of each of the 51 bodies with edits, `check` on the 5 without (X4.5); then the read-only Drive and control-page anchor checks (X4.6) | P-76, P-77, P-88, P-95, P-102 | no refusal; `repair` `[]`; `reapply_unsafe` `[]`; `precheck` and `landed_check` pass on every page; the 5 exit 0; `drive_check.py` passes (bytes, fence, the nine M2 strings, no collision); `ctrl.py all --expect unlanded` passes | nothing written to Notion; a failure stops EXECUTE as step 11 does (P-84 revised) |
| 13 | all | the freeze | Nathan confirms it; the unit's date is recorded in `EX/run.json` and the line listed in `EX/ctrl/sent.txt`; `TRACK-FREEZE-START` (spec §7.3; X5.0) | P-66, P-96, P-104, P-112 | `ctrl.py edits` reads `LANDED`, a stale readback retried (P-112 (e)) | kept on a stop, beside `TRACK-UNIT-STOPPED` (P-98). A failure before the line is listed stops EXECUTE as before step 13; from the listing on it is a stop past X5.0, whose sweep finds whether the line landed (P-112 (e)) |
| 14 | PART-06 | Notion: the *Candidate CRD Items List* page | Create and migrate by method M2, with its self-links (spec §7.4; X5.1); the migration date is recorded before the create, and the page id and URL right after it | D25-A; P-47, P-96 | `drive_check.py` passes; `m2.py check` passes F1–F10 at both stages (P-105); no `{{`; a page this run already created is resumed from the stage it reads, not created again (P-95, P-112 (b)) | moved to trash if it exists (P-98) |
| 15 | PART-06 | `notion-write-boundary.md` | `P30-DEST` with the URL, and `P30-VERSION` (X5.2) | D25-A | anchors found once; no new `{{` | the branch stays unmerged (the landing-unit rule) |
| 16 | PART-06 | the Hub (×3), the four Checklist item rows (×2 each) | The eleven pointer edits (spec §7.4.5; X5.3) | P-46, P-67 | each edit applied once (P-90, P-96, P-103); readback | reversed in reverse order on the re-fetched text, a doubled pointer undoubled first; the restoration check tests every pointer the unit listed (P-98, P-112 (a)) |
| 17 | PART-05, 06, 07, 13, 14, 15, 16, 18 | the 50 live bodies | Land each page from the engine; re-fetch; `check`, CL-40 with the URL (spec §3; X5.4) | the parts' classes; `D23`, `D25` | every `plan` applied has `reapply_unsafe` `[]`; the first on each page has `repair` `[]`, or, on an X5.4 a session continued, its repair is applied once and checked (P-111 (a), P-112 (k)); `check` exits 0 on each page | repair forward: `plan` on a fresh fetch lands only what is missing (P-88); else the unit stops, and the sweep lists each landed body for Nathan's restoration (P-98, P-99) |
| 18 | PART-11 | the proposed MGMT-10 body | R-ITEM23 and its LOCAL preamble edit; the gates (X5.5) | ITEM-23, ITEM-40 | both gates read 0 on the readback | as step 17 |
| 19 | PART-11 | Notion: the D20 redesign tracking page | `PART-11-TRACK-01` (spec §7.3; X5.6) | Decision 11 | readback | reversed as step 16 (P-98) |
| 20 | PART-12 | Notion: Hub *Worker communication rules* §2 | `PART-12-HUB-01` (spec §7.1; X5.6) | ITEM-24 | readback | as step 19 |
| 21 | PART-18 | Notion: the Alpha feedback list, AF-009 | `PART-18-AF009-01`, a dated amendment (spec §7.2; X5.6). The PE Metaprompt and the skills state no placement; no edit | P-44 | readback | as step 19 |
| 22 | PART-08 | OPS-10, OPS-20 | No edit. ITEM-20 is `NOT_APPLICABLE`: the mention bans are correctly scoped (§A) | §A | §E records the disposition | — |
| 23 | gate | the corpus | The Tier 1 gate (X6.1–X6.3): `land.py check` on all 55 live bodies; `graph_check.py`; `closure.py` | Tier 1; P-64 | 55/55 exit 0; exit 0; the closure comparison's `diff` exits 0 | repair forward; else the unit stops (P-98) |
| 24 | record | this record's §E and `EX/` | Write §E; commit the evidence; open the execution PR (X6.4) | template rules 5, 6 | `modification_validate.py` passes; only the three open paths change, checked before the PR opens | the unit stops (P-98, P-99), as step 23 |
| 25 | the packages | the installed tree | After Nathan merges: Nathan installs the seven archives delivered at step 11 (X7.2–X7.3); digests, `run_gate.py --set post` and the corpus gate on the installed skills, and when all three pass the install date recorded (X7.4) | `D24` | X7.4 starts from `main` and resumes on its own branch (P-110); each installed digest equals its freeze digest in `EX/packages.json`; exit 0 (28 rows); 55/55; the summaries and the install date committed together | reinstall the delivered file, saved again from its message if needed; any other failure from the merge to X7.4: §E's row with the `D25 applies from:` line, and a record PR that merges before the step runs again; the freeze held; returned to Nathan (P-82, P-94, P-110, P-112 (d)) |
| 26 | close | the freeze; Notion: the D20 tracking page | After step 25 passes, Nathan lifts the freeze; the lift date recorded; `TRACK-FREEZE-LIFT` (X7.5) | P-66, P-96 | readback | — |
| 27 | close | the decision record, the policy, the repair-a4 record, this record | The close commit: the close date recorded; `CLOSE-D22`, `P31-POLICY`, `P33-A5NOTE` (`apply_texts.py`), §E's install record and actual cost, the `D25 applies from:` line unless present, the dispositions, `COMPLETE`; the close-out PR opened (X7.6), after reading back Nathan's Drive banner | P-43, P-72, P-83, P-86, P-102 | the banner is present; the `D25` line is found once; `modification_validate.py` passes on `COMPLETE`; the commit adds no `{{` | revert the commit |
| 28 | close | Notion: the D20 tracking page | `TRACK-STATUS-01` to `03`, dated by the close date step 27 recorded; their readback added to §E on the same PR (X7.7) | P-65, P-72 | readback; `modification_validate.py` passes | `new_str` → `old_str` |

**Order:** 1 to 12 in order, all before any Notion write. Then 13 to 21 in order: step 14 must pass before any body
lands (PART-15 is after PART-06). Then 22 to 24. Step 25 follows Nathan's merge, and 26, 27 and 28 follow in that
order. A stop before step 25 follows spec §9's stop procedure (P-98, P-99, P-107, P-108, P-112); a failure from
Nathan's merge to step 25 is recorded by P-110 and P-112 (d).

### Product Owner actions

- **Approve this plan.** Recorded as `plan_approved_by`.
- **Merge #478**, this record. Verified by `plan_approved_by` on `main`.
- **Receive the seven packages** at step 11, one per message, then the brief and both verdicts. Each caption leads
  with the archive's sha256, and each message says what changed, where it installs and the freeze line you should see
  after installing. **Install them only at step 25**, when EXECUTE asks, and keep the messages: an archive you no
  longer hold you can save again from its message. If you cannot, say so: EXECUTE re-sends it when its session still
  holds the same bytes, and otherwise records the failure for your ruling; nothing is re-cut after the execution PR's
  merge (P-112 (d)). Verified by step 25's digest comparison.
- **Confirm the freeze** at step 13 and **lift it** at step 26, once step 25's post-install verification passes. No
  flow session runs in between. Verified by the tracking page's two dated lines.
- **Banner the Drive file** `Candidate-CRD-Items-List.md` as superseded, pointing to the new page, once step 24 has
  passed and before step 27 (the page is permanent from then on). Verified at step 27 by reading the file's first
  lines.
- **Merge the execution PR** after step 24. Verified by the merge commit on `main`, which puts the reindex there
  before the install.
- **Install the seven `.skill` packages in one sitting**, after that merge, and give the date. Verified by step 25's
  digest comparison.
- **Merge the close-out PR** after step 28. Verified by the merge commit.
- **Rule on a stop, if one comes.** Every stop reaches you as a record PR, complete when you receive it (after a stop
  past the freeze line's listing at step 13, the tracking page's stop lines are already written and read back); merge
  it first (P-107).
  - Before the freeze line is listed at step 13 (P-84 revised, P-107, P-112 (e)): end the Modification, or approve
    the plan change a PLAN session writes. The freeze you confirmed at step 13 lapses with the stop.
  - From that listing to step 24 (P-99, P-108, P-112 (a)): restore each body and control-page edit the record lists,
    from Notion's page history, or say that a listed control edit stays as it is; then ask for the restoration check,
    which opens its own PR. Once it passes, end the Modification or approve a plan change, and lift the freeze when
    you choose.
  - From your merge of the execution PR to step 25 (P-110, P-112 (d)): rule a reinstall, or a plan change, which names
    its own steps and rejoins at step 25, not at step 1; no body is restored.
  Verified by §E and the record PRs.

### Explicitly not in scope

- The TW ecosystem, including tw-flowmaster's GCFPE binding and AF-012 for TW.
- The proposed MGMT-10 body's design-level contradictions: D20 stage 5 (recorded on the tracking page, step 19).
- The follow-ups in spec §10.2, recorded on the GCFPE Modification Backlog as MB-001 (S2), MB-002 (S3), MB-003 (S3) and
  MB-004 (S3). A later Modification takes each as an item.
- The kept NOT_REAL sentences in spec §10.3.
- The content of the Drive file after migration, which is Nathan's.
- Re-running any earlier Modification's gates, and editing any completed record (P-54).

### Findings on upstream sections

Recorded in spec §10.1 and not edited here (template rule 1):
- the census's RS-40 A5 row;
- the census summary for the proposed MGMT-10 body;
- `validator_revision`'s absence from §A's Decision 1;
- the merge count;
- the freeze window;
- the Notion targets §A omitted;
- ITEM-13's oracle input.

### Interaction cost, as planned

    interaction_cost = open rulings 3 + 2 + review cycles 1 + installs 1 + merges 3 + freeze 1 + Drive banner 1 = 12

§A predicted 11 with two merges. The install has to follow the execution PR's merge (§A order 3), so the
post-install record needs a third merge, the close-out PR. A D24 rejection would add 4: the stop record's merge, a
plan approval, a further review round and the plan-change merge (P-84 revised). A stop after step 13 adds the
restoration and the restoration check's pull request (P-99, P-108). An archive you can no longer save from its
message, when the session no longer holds its bytes either, becomes a recorded failure and a plan change
(P-112 (d)). `interaction_cost_predicted` keeps §A's 11, and §E compares the actual cost
against both.

### Successor, 2026-09-24 — the plan resumed under D26

*Written by MODE = PLAN, 2026-09-24, in a `GCFPE-MGMT-10` maintenance session running the proposed body
(Notion `3e34590a05eb811b93d2da9b4ef8106d`, last edited at 11:00Z and read in full at the start), started by Nathan with the kickoff in
`docs/ephemeral/pe37.stage5/RESUME-PROCEDURE.md`. It follows that file's step 3, in order. The plan above was stopped
before approval on 2026-09-24 at 08:28Z (`evidence/closeout-residuals/RCA-20260924-closeout-residuals.md` §8), and it is
not rewritten. **Where this section and the dated plan or the spec differ, this section governs.** Scope stays frozen
at 40 items in 17 parts. Nothing here is approved: `plan_approved_by` is empty.*

**Authority.** `D26` (its *Transition* names this Modification); the recovery analysis §4.3
(`docs/ephemeral/pe36.mgmt-redesign/RECOVERY-ANALYSIS-20260924.md`); `RESUME-PROCEDURE.md` step 3; `D20`–`D24` as
before.

**The eight PLAN rounds before D26** (2026-09-23 and 24) are cited from the RCA §2 and §8, not entered in the
`reviews` ledger (`D26` transition). The ledger starts with this resume.

**Where this stands.** The dry run failed on the normal path in one place, `TRACK-STATUS-01` to `03` (DN-8
below). Under `D26-F` trigger 2 that means one bounded executability check, then a return to Nathan. **So the diff check
(`RESUME-PROCEDURE.md` step 3.5) has not run.** It runs after Nathan rules on DN-1 to DN-8, on the successor as it then
stands. `status` is `PLANNING` until then.

#### What resumes, and what is withdrawn

| part of the plan | disposition | what that means for EXECUTE |
|---|---|---|
| **Content**: the 51 body edits (spec §3 and the engine), the 7 skill diffs, the registry diff and its guards, the graph reindex, the 11 repository texts, the Notion edits | **KEEP**, less `PART-11-TRACK-01` and (under DN-8's recommendation) `TRACK-STATUS-01` to `03` | Landed exactly as the spec and `EV/` state them. The re-derived text results are below |
| **`PART-11-TRACK-01`** (§P step 19) | **WITHDRAWN**, not rewritten | It would write a dated paragraph saying the proposed MGMT-10 body's contradictions are not resolved and wait for stage 5. Stage 5 resolved them (`docs/ephemeral/pe37.stage5/MGMT-10-REVISION.md`), so the paragraph would be false when written |
| **PART-11** (ITEM-23, ITEM-40) | **VERIFIED, not applied** | Stage 5 already applied `R-ITEM23` and the LOCAL preamble edit to the proposed body. The dry run: `land.py check` passes with `R-ITEM40` 0 and `R-ITEM23-gate` 0, `state` reads `LANDED`, and `plan` refuses `ALREADY_LANDED`. So X4.5 and X5.5 run `check` on `GCFPE-MGMT-10-PROPOSED`, never `plan`, and write nothing to it |
| **Normal-path tools**: `land.py` (`plan`, `check`, and `state` for the sweep), `ctrl.py` (`edits`, `all`, `op`, `children`), `run_gate.py`, `apply_texts.py`, `m2.py`, `drive_check.py`, `graph_check.py`, `runjson.py`, `nam002_live.py`, `packages_json.py`, `fill_brief.py` without `--prior-file`, and the first-round D24 brief | **KEEP**, with **R8-02 fixed** | X6.4's path check becomes the three-dot merge-base diff, and X7.6's check uses the same form (below) |
| **Machinery**: automated stop and reversal; the stop record and its `attempt-<n>` directories; the restoration check (`ctrl.py all --expect restored`, `--kept-from`, `--sent`, `--waived`); the lift and end routes after a stop; `TRACK-UNIT-STOPPED`, `TRACK-STATUS-STOP-01` to `03` and `TRACK-FREEZE-LIFT-STOP`; resuming in a new session at any step, and the branch rule that routes it; the lease pushes; the sent list `EX/ctrl/sent.txt`; post-merge routing by commit subjects; the D24 re-roll and plan-change brief variants (`fill_brief.py --prior-file`, `REVIEWER-PROMPT-prior.md`) | **WITHDRAWN** | Not run. The files stay in `EV/` as dated records. Round 8's R8-01, R8-03 and R8-04 go with this machinery, and so does the downgraded lift-after-stop finding |

The spec's §9 preamble keeps its definitions (`EV`, `EX`, `<record>`, `$SCRATCH`, `$INST`, `$PKG`, `$GATE`,
`$BASE`, `<URL>`, `<ROOT>`, the environment line), *Recorded values* (`runjson.py`; the keys `stop_date`,
`delivered_cr<k>` for any `k` but the first, and those of the withdrawn routes are not used), and *Notion writes*
(`allow_async: false`, the async poll, the apply-once test, and the control readback rule's three cycles). Everything
else in the preamble is superseded by the three subsections below. That includes the sent list, the commit-and-push
lease, *A failing gate*, *Sessions*, *The branch rule*, *The landing unit*, the stop record, the restoration check,
the lift and the end route. `AT` is not used.

#### The failure path (`D26-B`), replacing the stop procedure

**The first external write** is X5.0's `TRACK-FREEZE-START` Notion call. The RCA and the dated plan use the
term this way too. No Notion page is written before it.

- **Before it.** A failing gate stops EXECUTE. Nothing has left the execution branch, which stays unmerged, and
  `main` does not change. The session writes the failing step's row and the failed predicate into §E on the branch,
  commits and pushes, and returns `IMPLEMENTATION_BLOCKED` to Nathan. What follows is his ruling: end the
  Modification, or a plan change that a PLAN session writes. A D24 `SKILL_REPAIR_REQUIRED` verdict at X4.4 is such a
  stop. It is returned to Nathan and not re-rolled (`D26-A` rule 2). The parts share one registry diff, one engine
  and one package set, so no part carries on alone. That is an open finding (OF-3), not a design choice this plan
  makes silently.
- **From the first external write to X6.4's pull request**, a failure that forward repair within the session cannot
  clear takes these four steps and nothing more. Forward repair means `land.py plan` on a fresh fetch, which lands
  only the edits still missing, and the control readback rule's three cycles.
  1. **Failure record to `main`.** `git fetch origin main && git checkout -B docs/<yyyymmdd>-closeout-residuals-failure origin/main`;
     `mkdir -p docs/ephemeral/modifications/evidence/closeout-residuals/failure && git archive <execution branch> docs/ephemeral/modifications/evidence/closeout-residuals/execute | tar -x --strip-components=5 -C docs/ephemeral/modifications/evidence/closeout-residuals/failure`,
     which copies `EX` to `failure/execute/`. It never goes to `EX`'s own path, so `EX/run.json` reaches `main` only
     through the execution PR, and checkpoint 3's test stays true. In the record, set `status: EXECUTING` and write §E:
     a row for every step run, with its disposition; the failing step with its failed predicate and its output (counts and ids, no body text),
     copied from `$SCRATCH` into `failure/`; and every later step `NOT_RUN`, citing the failure. Run `modification_validate.py`; `git add` the record and `failure/` only, and `git diff --cached --name-only` lists
     nothing else; commit (`closeout-residuals record: failed at <step>`), push, and open a
     pull request against `main`. It carries no registry, graph, skill-text or rule change.
  2. **Sweep, read-only.** Fetch each of the 50 live bodies with edits and run `land.py state <PID> <PAGE>`
     (CL-40 with `--candidate-url <URL>` once `url` is recorded). Fetch the seven control pages and run
     `ctrl.py all --run docs/ephemeral/modifications/evidence/closeout-residuals/failure/execute/run.json --edits EV/resume-20260924/control-edits.json` without `--expect`. Fetch the Hub
     and run `ctrl.py children 3ce4590a05eb814f8892f88ff8539308`, which lists any *Candidate CRD Items List* child
     page by id. The states, ids and counts go to `failure/sweep.json`, one more commit on
     the same pull request. Lanes of workers may do the fetches.
  3. **Keep the freeze.** Nothing lifts it, and the tracking page keeps `TRACK-FREEZE-START`.
  4. **Return to Nathan** with `PRODUCT_OWNER_ACTION_PENDING`. It names every page the sweep reads `LANDED` or
     `PARTIAL`, every control edit that reads `LANDED`, and the new page if one exists; the record PR to merge; and the
     statement that the Modification stays `EXECUTING` until he has restored the bodies from Notion page history.
     Nothing further is automated: no reversal, no trashing, no stop lines, no restoration check. After his
     restoration, ending the Modification or a plan change is his ruling.
- **A lost session between the first external write and X6.4** is not a resume point (`D26-C`). The session
  Nathan starts next with `MODE = EXECUTE` finds `execute_date_X5.0` in `EX/run.json` on the pushed execution branch,
  and no execution PR merged. It then takes steps 1 to 4 above.
- **From X7.1 to X7.4** (post-merge, freeze held), a failure is recorded as spec §9 *A failing gate*'s third bullet
  already says: §E's row, the `D25 applies from:` line, one commit
  (`closeout-residuals record: X7.<s> failed`), a record PR, and a return to Nathan. The difference is that it is
  made on a branch opened from `origin/main`, as the next subsection says. "A plan change … rejoins at X7.2" is
  withdrawn: a plan change states its own steps.
- **From X7.5**, where Nathan has lifted the freeze, a failure is repaired forward by running the step again, or
  returned with the failing gate named. Nothing is reversed.

#### Checkpoints (`D26-C`)

1. **Mode boundary.** EXECUTE starts only when `main`'s record carries `plan_approved_by` (X0.1). X0.2 is:
   `git fetch origin main && git checkout -B docs/<yyyymmdd>-closeout-residuals-execute origin/main`, then
   `mkdir -p EX` and `runjson.py EX/run.json base "$(git rev-parse HEAD)"`. The gate is: `HEAD` equals `origin/main`
   and `git status --porcelain` prints nothing. Every push is `git push -u origin <that branch>`.
2. **Before the first external write, by restarting.** A session lost before X5.0's Notion call is
   followed by a new session that restarts EXECUTE at X0.2 on a new branch,
   `docs/<yyyymmdd>-closeout-residuals-execute-<n>` with `<n>` = 2, 3, and so on. The earlier branch stays unmerged,
   for Nathan to delete. X1 to X4 run again in full, including X4.3's packaging and a fresh D24 round. Archives
   delivered by an earlier attempt are void, because X7.2 names the archives to install by the sha256s in the
   `EX/packages.json` that reaches `main`. Before X0.2, `git fetch origin` and, for each
   `origin/docs/*-closeout-residuals-execute*` branch,
   `git grep -l SKILL_REPAIR_REQUIRED <branch> -- 'docs/ephemeral/modifications/evidence/closeout-residuals/SECTION-10-REVIEW-cr*'`;
   any output is the X4.4 stop, returned to Nathan, with no restart.
3. **Post-merge steps, started from `main`.** The execution PR's merge is detected by a file on `main`, never by a
   commit subject: `git fetch origin main && git cat-file -e origin/main:docs/ephemeral/modifications/evidence/closeout-residuals/execute/run.json`
   exits 0. That replaces R8-01's subject test. X7.2 runs once that holds. X7.4 runs once Nathan says his install
   sitting is done. It opens `docs/<yyyymmdd>-closeout-residuals-close` from `origin/main`. X7.4 to X7.7 commit
   there, and the close-out PR is opened from it. A session started after X7.1 begins at X7.2, or at X7.4 when
   Nathan says the install is done. After X7.4 has committed, it continues on the close branch.
4. **Within one session**, what keeps a step safe after compaction stays: values recorded once (`runjson.py`), the
   apply-once tests (`apply_texts.py`'s states, `land.py plan`'s edit states, `ctrl.py edits`), and operations that
   match nothing when sent twice (P-103). `m2.py check --stage auto` still reads X5.1's stage from the page, so a
   compacted session does not create the page twice.

#### Changes to the dated steps

The dated §P steps and spec §9 rows stand, with these changes. Nothing else in a step moves.

| dated step | spec row | change |
|---|---|---|
| 1 | X0.2 | Checkpoint 1's commands replace the branch rule. X0.3's recorded values hold on `main` `d179277` (dry run) |
| 3 | X2.1 | The applier's result on the new base: `gcfpe.decision-record.md` sha256 `c8cdfd5a46666173e2b634ef5793a7db11fbc23f4e9a3615a161fd2d2cb7a638`, 111 107 B, where it was `6742d593…`, 101 936 B. D25 lands between D24 and D26. The other gates are unchanged |
| 7 | X3.4 | `session-working-rules.md` after `P32-SWR`: sha256 `2501579e1f04a2f7d4855b965859407348b7c2dc2cbdf9c03b8dabd1a4eadf4b`, 16 113 B |
| 11 | X4.4 | `fill_brief.py EX/packages.json --write` only. It prints `k` = 1, because no `REVIEWER-PROMPT-cr*.md` exists yet in the closeout-residuals evidence directory on `main`. `--prior-file` and the new-session resume (P-109) are withdrawn. `SKILL_REPAIR_REQUIRED` from either reviewer stops EXECUTE (the failure path, before the first external write). `delivered_cr1` is still recorded once |
| 12 | X4.5 | `GCFPE-MGMT-10-PROPOSED` moves from `plan` to `check`: 50 `plan` runs and 6 `check` runs. X4.6's `ctrl.py all` takes `--edits EV/resume-20260924/control-edits.json` (sha256 `72889b248019c61dff47451bded0f22ea9785e203445117e7181306a0e978bbc`, 15 edits: `EV/notion/edits.json` less `PART-11-TRACK-01`, the five stop-path edits and, under DN-8 (A), `TRACK-STATUS-01` to `03`). Every later `ctrl.py` call takes the same `--edits` |
| 13 | X5.0 | Nathan confirms the freeze. `runjson.py EX/run.json execute_date_X5.0`, commit, push. Then `TRACK-FREEZE-START` by the apply-once test and `ctrl.py op`, with its readback. The sent-list append is withdrawn |
| 16 | X5.3 | As dated, without the sent-list append |
| 17 | X5.4 | As dated, except "on an X5.4 a session continued (the branch rule's rule 3)". A `repair` ≠ `[]` can now arise only within this session, after compaction or a lost response. It is the forward repair, applied once and checked. A refusal, or a non-empty `reapply_unsafe`, takes the failure path |
| 18 | X5.5 | `land.py check GCFPE-MGMT-10-PROPOSED 3e34590a05eb811b93d2da9b4ef8106d --skills $PKG` on a fresh fetch: exit 0, `R-ITEM40` 0, `R-ITEM23-gate` 0. No write. PART-11 lands as `VERIFIED` (stage 5 applied it) |
| 19 | X5.6 | **Withdrawn** (`PART-11-TRACK-01`) |
| 20, 21 | X5.6 | `PART-12-HUB-01` and `PART-18-AF009-01` only, without the sent-list append |
| 24 | X6.4 | **R8-02.** The path check is `git diff --name-only origin/main...HEAD`, a three-dot merge-base diff: it lists only paths under `docs/prompt_ecosystem_management/`, `docs/graph/` and `docs/ephemeral/`. A commit that reaches `main` outside those paths during EXECUTE no longer fails it |
| 25 | X7.2–X7.4 | Checkpoint 3 replaces the branch rule. X7.2's re-send and failure record stand. X7.4's failure is recorded on a branch from `origin/main` |
| 27 | X7.6 | The pull request's path check uses the same three-dot form on the close branch. The close texts' results depend on the install date and the installed freeze lines. With a stand-in date of 2026-01-01 and the expected lines, they were: decision record `b324490a…` (113 065 B), `prompt-body-content-policy.md` `c24061b8…` (7 125 B), `REVIEWER-PROMPT-a5.md` `9e2d822c…` (19 234 B), and each re-run of a label applied nothing. X7.6 opens the close-out PR without the X7.7 sentence, records step 28 in §E as withdrawn under DN-8 (A), and returns to Nathan for X7.8 |
| 28 | X7.7 | Under DN-8 (A), **withdrawn**. The tracking page's status lines belong to the D20 track, which already rewrote them. Under DN-8 (B), three re-anchored edits, drafted after the ruling |

The spec's stop-only material stays in the file as a dated record: §9's stop record, restoration check, lift and end
route, §7.3's stop and lift-stop edits, and P-98, P-99, P-107, P-108 and P-112's stop clauses.

#### The dry run (`D26-A` rule 1; the ledger's `DRY_RUN`)

2026-09-24, 11:05Z to 11:40Z. Every normal-path gate was run read-only against fresh fetches of the live pages, and
the manifest's commands were run in spec §9 order on a scratch clone of `main` `d179277`, with `$PKG` built from
`$INST`. Nothing was written to Notion, Drive or the repository. The evidence is
`evidence/closeout-residuals/plan/resume-20260924/dryrun-summary.json`: counts, ids and hashes, and no body text.

| gate | result |
|---|---|
| X0.3 (a)–(e) | registry `8b4e46ed…`; the 7 installed freeze lines equal the manifest; graph 575 074 B `ae2bd159…`, `a70a9326…`; `checks_matching_authored_or_canonical: []`; root `320 420705ec…` |
| X1.1, X1.3 | 7 patches exit 0; `expected_after_patch` diff exits 0; `$PKG` root `323 047ca742…`; the `pre` gate exits 0 with 12 of 12 rows |
| X2.1, X3.1–X3.4 | as the table above; the registry reaches `97bda1a0…`, `valid: true`, drift `[]`; reindex `cmp` exit 0, 27 files, a second reindex 0; the contract template and its README at their sha256s |
| X3.6 (NAM-002 on the six live hubs) | runs 1 to 3 `expectation_met` true, with 0, one ESC-10, and one title finding; run 4, the control, 55 / 16 / 6, exit 1; exactly spec §4.4's table |
| X4.1, X4.2, X4.3 | `6902924a…` and `dbae180b…` EQUAL ×2, with the two expected diff lines; the `pkg` gate exits 0 with 34 of 34 rows; `Skill is valid!` ×7; the extracted freeze digests equal `expected_after_patch.txt`; `$PKG` unchanged by packaging |
| X4.5 (rehearsal) | **49 of 50** live bodies with edits pass `plan --no-ops`: no refusal, `repair` `[]`, `reapply_unsafe` `[]`, precheck and landed check pass, 256 operations. The 5 untouched pass `check`. The proposed body passes `check` and is `ALREADY_LANDED` (PART-11). **ESC-25 was not rehearsed**: the harness's permission classifier refused the command twice, once in a worker and once in this session. The refusal was not worked around (OF-2) |
| X4.6 | `drive_check.py` passes: 31 923 B, sha256 and fence OK, each M2 `old` once, no Hub child with the title. `ctrl.py all --expect unlanded` on the dated 24 edits **fails**: `TRACK-STATUS-01` to `03`, and their three stop variants, have `old_count` 0 (DN-8). On the 15-edit successor set it passes, with every `old_str` once and none `LANDED` |
| X6.2 (`--simulate`), X6.3 | graph check `pass: true`; the closure `diff` exits 0 |
| texts (step 3.3) | every anchor occurs once on the new base. The results are in the table above, and a second run of each label applies nothing |

**The bounded executability check (`D26-F` trigger 2).** Only the three `TRACK-STATUS` edits fail, and they fail in
two places: X4.6's gate, before any Notion write, which would stop EXECUTE loudly, and X7.7. No other step uses them.
The rest of the normal path ran clean. The one gap is ESC-25, which pass 7 rehearsed clean on 2026-09-24 at 13:15Z to
13:25Z and which this dry run could not run.

**`D22` condition 5.** The workers' and this session's fetches left harness files in this session's store. Among
them, the QA-10 body and the Hub page were saved to `tool-results/` files. No worker or session opened those files by
hand; only the plan's tools read them, in memory. They are left to the harness's teardown.

#### Findings on upstream sections — DECISION NEEDED (template rule 1)

These seven were recorded in the dated plan and spec §10.1. Under rule 1, as `D26` amended it, each returns to Nathan.
None is an accepted risk, and the plan is not approved past them. **DN-8 is the dry run's.**

| # | the upstream text it contradicts | the plan's current handling | recommendation |
|---|---|---|---|
| DN-1 | `ANALYZE-anchor-census.md` A5 row: "REAL only in GCFPE-MGMT-10, PR-35, RS-40" | RS-40 does not carry the sentence; its runtime-artifact sentence already scopes to "explicitly authorized paths". R-A5 is `NOT_APPLICABLE` on RS-40 (P-04), and ITEM-32 is met by PR-35, GCFPE-MGMT-10 and RS-40's existing wording | Accept: the census row is wrong and the plan's handling is right |
| DN-2 | `ANALYZE-anchor-census.md` on the proposed MGMT-10 body: "Carries A1, A2, A3, A4, A5 and A8" | The per-body rows found only A8's two lines; R-ITEM23 removed them. **Answered by stage 5**: `MGMT-10-REVISION.md` removed those lines and resolved the census's contradictions, and the dry run reads both gates at 0 | Accept, and record PART-11 as `VERIFIED` (stage 5 applied it) |
| DN-3 | §A *Decisions*, item 1: the revision table lists flowmaster-validate 3.3.0 → 3.3.1 but not `validator_revision` | `validator_revision` moves 3.3.0 → 3.3.1 at its four sites, under the same rule: "Corrected bytes never reuse one" (P-22) | Accept: the same rule, applied to one more field |
| DN-4 | §A *Readiness*: "merges 2 … Merges count the record PR and the execution PR" | 3 in the dated plan: the close-out PR carries the post-install record. **4 now**: #478 (merged), this plan's record PR, the execution PR and the close-out PR | Accept 4 |
| DN-5 | §A *Order*, item 4: the freeze "lifts after full readback and the corpus gate" | It lifts at X7.5, after X7.4's post-install verification. The bodies land at X5, before the matching skills are installed at X7.3, and must not be used in between (P-66 revised) | Accept the longer window |
| DN-6 | §A per-part targets, PART-06 and PART-18: they name the new page, the destination rule and the eight bodies, but not the Hub and Checklist pointers to the Drive list, nor AF-009's placement statement | The plan includes them as consequences of ITEM-18 and ITEM-37 (P-67): eleven PART-06 pointer edits and `PART-18-AF009-01`. No item is added | Accept: these are the Notion surfaces of two frozen items. Reject only if you read them as new scope, in which case they go to the Backlog |
| DN-7 | ITEM-13: "regenerates byte for byte from repository sources" | One input, digest-pinned, is the R1 oracle bundled in flowmaster-validate, a skill rather than a repository file. ITEM-13's disposition records it, and nothing is widened (P-69) | Accept, with the disposition naming the oracle |
| DN-8 | The dry run: the tracking page (`3e34590a05eb81e7927efe0541258916`) no longer carries `TRACK-STATUS-01` to `03`'s anchors. Stage 5 rewrote the status lines, to `STAGE_5_PROCESS_FIX_IN_PROGRESS_PE37` and "`PLANNED`, not approved" (stage 5's review A L1) | X4.6's gate fails before any Notion write, and X7.7 cannot land | **(A) Recommended: withdraw the three edits.** The D20 track owns those status lines, rewrote them, and closes them at resume step 8. This Modification's own state is on its record. X4.6 then passes, as the dry run shows. **(B)** Re-anchor them to the current wording. That is new control-page text written by this plan, then a dry run of the three edits |

#### Open findings, accepted as risks (`D26-A` rule 4)

Approving the plan accepts these (`DISP-001`). None is repaired here.

| # | finding | path | likelihood | consequence | why listed |
|---|---|---|---|---|---|
| OF-1 | Round 8's 21 machinery findings: 1–7, 9, 13, 14, 16, 17 and 19–27 in `rca-20260924/round8-review-results.json`, plus the downgraded lift-after-stop finding | failure paths | — | — | **Withdrawn with the machinery**; none survives in a step that runs |
| OF-2 | ESC-25's rehearsal was refused by the harness's permission classifier ("Data Exfiltration" in the worker, "Auto-Mode Bypass" here) | normal, X4.5 | unknown; it happened twice today | if it recurs at X4.5, a loud stop before any Notion write; if it recurs at X5.4 or X6.1, the failure path | a harness permission, not a plan defect. Pass 7 rehearsed ESC-25 clean. Nathan can allow the command, or EXECUTE stops and asks |
| OF-3 | Before the first external write, one part's failure stops every part, where the MGMT-10 body says "carry on with every part not ordered after it" (`D21-B`) | failure, before X5.0 | low | a loud stop; nothing is written outside the unmerged branch | the parts share one registry diff, one engine and one package set, so landing a subset needs new machinery. The rule for that is Nathan's (`D26-B`: a fix that needs new machinery is a question first) |
| OF-4 | A session lost between the first external write and X6.4 cannot resume, so the next session takes the failure path, and Nathan restores the landed bodies by hand | failure | low to medium: X5 is the longest window | a manual restore of up to 50 bodies, and the freeze held for a PLAN cycle | `D26-C`: no resume is designed there |
| OF-5 | Restarting before X5.0 repeats X1 to X4 in full: a new package cut, a fresh D24 round and a new delivery | failure, before X5.0 | low | about 1.5 h and 1M tokens | `D26-C`: restart, not resume |
| OF-6 | Round 8 #10: every `m2.py` mode needs a Drive download from the last 30 minutes, and X5.1 is long | normal, X5.1 | medium | `m2.py` refuses loudly; downloading again and re-running clears it within the session | a loud refusal, repaired by re-running |
| OF-7 | Round 8 #11: `notion-create-pages` can return an async task with no page id | normal, X5.1 | low | a second create is caught by F1, loudly, which leads to the failure path, where Nathan trashes the duplicate | loud |
| OF-8 | Round 8 #12: X5.3's and X5.6's readbacks put several JSON documents in one file | normal, evidence | certain | an evidence file that is JSON Lines rather than one JSON document; no behaviour changes | no runtime effect |
| OF-9 | Round 8 #8, #15 and #18: stale counts and marks in the spec §0, spec §2.9 and `DECISIONS.md` | none | certain | documentation only | no runtime effect |

#### Product Owner actions (this successor)

- **Rule on DN-1 to DN-8.** The session records each answer in a successor note. Then it runs the one diff check
  (`RESUME-PROCEDURE.md` step 3.5) and returns the plan for approval.
- **Approve the plan.** The session writes `plan_approved_by` with your words (template rule 2), and you merge that
  record PR. X0.1 checks `main`'s record.
- **OF-2, if you want to prevent it:** allow the `land.py` command that the classifier refused on ESC-25, before
  X4.5.
- **The rest are as the dated plan says:** receive the seven archives at X4.4; confirm the freeze at X5.0; banner the
  Drive file after X6.4; merge the execution PR; install the seven in one sitting; lift the freeze at X7.5; merge the
  close-out PR.
- **On a failure after the first external write:** merge the failure-record PR; restore the bodies the sweep names
  from Notion page history; then rule on ending the Modification or a plan change.

#### Explicitly not in scope (additions)

- The tracking page's status lines, under DN-8 (A).
- Every change stage 5 made: `D26`, the template, the validator, the proposed MGMT-10 body. This plan verifies
  PART-11 against it and changes none of it.

#### Interaction cost, and the estimate against what has been spent

    interaction_cost = open rulings 4 + 2 + ANALYZE review rounds 3 + PLAN review rounds 9 + skill review cycles 1
                       + installs 1 + merges 4 + freeze 1 + Drive banner 1 = 26

- **Rulings (4):** §A's three, plus this return's DN-1 to DN-8, answered together.
- **PLAN review rounds (9):** the eight before D26, cited from the RCA, and the one diff check to come. The dry run is
  not a review round.
- **Merges (4):** #478, this record PR, the execution PR and the close-out PR.
- **Already spent (16):** 3 rulings, the ANALYZE approval, 3 ANALYZE rounds, 8 PLAN rounds and #478. **To come (10).**
- §A predicted 11 and the dated plan 12. The difference is the format 2.1 formula counting review rounds, which the
  earlier counts left out (`D26-D`), plus this plan's record PR.

**The estimate against what has been spent.** The estimate for this resume is 2 h and 2.5M tokens. Spent so far: the
dry run took about 40 minutes of this session. Its five read-only workers used 0.81M tokens, as measured by the
harness. This session's own tokens are not measured by the session. Still to come: the diff check, two reviewers at
about 0.5M, and the return. EXECUTE's estimate stands at 8 h and 8M tokens. Twice the estimate triggers a re-price to
Nathan (`D26-D`).

#### Product Owner rulings on DN-1 to DN-8, 2026-09-24

**Nathan, 2026-09-24**, answering the return above:

> My rulings on DN-1 to DN-8. I accept all eight as you recommended:
>
> DN-1: the A5 edit doesn't apply to RS-40.
> DN-2: stage 5 already made PART-11's edits. Record PART-11 as verified.
> DN-3: the validator revision moves from 3.3.0 to 3.3.1.
> DN-4: four merges: #478, #484, the execution PR and the close-out PR.
> DN-5: the freeze lifts after the post-install check, not at readback.
> DN-6: the missing Notion pointer edits and the AF-009 note belong to ITEM-18 and ITEM-37. No new items.
> DN-7: ITEM-13's disposition names the oracle that ships inside the skill.
> DN-8: option (A). Withdraw the three TRACK-STATUS edits.
> One correction to DN-8: stage 5 didn't remove those tracking-page lines. They were already gone before stage 5
> started. It doesn't change the ruling.

**What this settles.** The plan's handling of DN-1 to DN-7 stands as written. DN-8 (A) is the plan, so
`TRACK-STATUS-01` to `03` are withdrawn, X4.6 and every later `ctrl.py` call use
`EV/resume-20260924/control-edits.json` (15 edits), and dated step 28 does not run. "This record's plan PR" in DN-4 and
the interaction cost is #484. PART-11 is recorded as `VERIFIED` at §E, with stage 5 as the one that applied it.

**The correction.** Where this successor and the ledger's `DRY_RUN` outcome say stage 5 removed or rewrote the
tracking page's status lines, that is wrong. Nathan's correction above holds: the lines were gone before stage 5
started. The ruling does not change, and the text above is left as written (a dated record gets a successor, not an
edit).

**One change to the successor after the dry run**, made before the diff check so the check covers it: failure-path
step 1 copied `EX` to its own path on the failure-record branch. That would put `EX/run.json` on `main` through a
failure-record PR, and checkpoint 3 would then read that as the execution PR's merge. Step 1 now copies `EX` to
`failure/execute/`.

#### The diff check, and the plan returned for approval, 2026-09-24

The one diff check ran under the committed brief `EV/resume-20260924/REVIEW-BRIEF-diffcheck.md` (`217068c`). Two
fresh reviewers each wrote a record, committed unedited beside the brief: `REVIEW-diffcheck-PLAN-DC-1.md` and
`REVIEW-diffcheck-PLAN-DC-2.md`. They found **the same two required defects independently**. Both sit in this
successor's own text. **Neither is repaired here**: this was the last review the cap allows (`D26-A` rule 2), so the
plan goes to Nathan with both open. Each has a one-sentence correction, quoted from the records:

| # | defect | path, likelihood, consequence | the reviewers' smallest correction |
|---|---|---|---|
| DC-1 (PLAN-DC-1 REQ-1, PLAN-DC-2 DC2-01) | Checkpoint 2 restarts a session "lost or stopped" before X5.0 on a new branch from `main`. A `SKILL_REPAIR_REQUIRED` verdict pushed by a lost session is invisible there: `fill_brief.py` writes a first-round brief, and the rejected bytes are reviewed again as new. "Or stopped" also contradicts *Before it*, which sends a stop to Nathan | failure, then restart; low; **silent**: a rejected package set can be delivered and installed without Nathan seeing the rejection (`D24` condition 5, `D26-A` rule 2) | "lost" for "lost or stopped"; before X0.2, `git fetch origin` and, for each `origin/docs/*-closeout-residuals-execute*` branch, `git grep -l SKILL_REPAIR_REQUIRED <branch> -- 'docs/ephemeral/modifications/evidence/closeout-residuals/SECTION-10-REVIEW-cr*'`; any output is the X4.4 stop, returned to Nathan, with no restart |
| DC-2 (PLAN-DC-1 REQ-2, PLAN-DC-2 DC2-02) | Withdrawing X7.7 leaves spec X7.6 opening the close-out PR "its body saying not to merge it before X7.7's commit", with no final return to Nathan and no §E disposition for dated step 28 | normal; certain; the PR tells Nathan to wait for a commit that never comes; nothing is written wrong | X7.6 opens the close-out PR without the X7.7 sentence, records step 28 in §E as withdrawn under DN-8 (A), and returns to Nathan for X7.8 |

**Listed findings.** PLAN-DC-1 lists 16 and PLAN-DC-2 lists 13, each with its path, likelihood and consequence in its
record, and several overlap. Both reviewers list the same three failure-path gaps, each correctable in one clause:

- the sweep's `--run EX/run.json` names a file the failure branch no longer has
  (`--run docs/ephemeral/modifications/evidence/closeout-residuals/failure/execute/run.json` runs);
- step 1 names no staging scope and no staged-path check, which the dated stop record had;
- step 1's copy of the failing step's output lacks the dated limit "counts and ids, no body text" (`D22`).

Listed findings are not repaired unless Nathan opts in (`D26-A` rule 4).

**The trend.** There is no earlier round to halve from. Every finding sits in text the last repair added, which is
expected for a check of that repair's diff, and it is also `D26-A` rule 5's signal to return. The two DRY_RUN and
DIFF_CHECK rows are the ledger for this resumed PLAN.

**The estimate against what has been spent** (the estimate for this resume: 2 h and 2.5M tokens). Session time so
far: about 1.4 h of work, 11:00Z to 11:47Z and 12:47Z to 13:25Z. The hour between was spent waiting on Nathan's
rulings. Tokens measured by the harness: 0.81M for the five dry-run workers and 0.86M for the two reviewers (0.45M and
0.41M), 1.67M in all. This session's own tokens are not visible to the session, so the total is higher than 1.67M and
may be near the estimate. It has not passed twice the estimate on what can be measured.

#### Plan approved, 2026-09-24

**Nathan, 2026-09-24**, answering the return above:

> I approve the plan with option (A): apply the two required fixes and the three failure-path one-liners, each
> exactly as the reviewers worded them. No other edits and no further review.
>
> One correction: #484 already merged (07b47d8) before my rulings and your diff check were committed. Those commits
> are only on your branch, and main still shows the plan at PLANNING. Record my approval, apply the fixes, and put all
> of it in a new pull request from main. Tell me when it's ready to merge. Don't start EXECUTE until that PR is on
> main.
>
> When we get to lifting the freeze, it covers both freezes: the Alpha run's E6 freeze and this Modification's. Record
> the lift in both records' §E (resume procedure, step 6).

**The five corrections, applied in place in the successor above**, each in the wording the diff-check table quotes
from the reviewers' records. There was no further review, as Nathan ruled.

1. **DC-1**, checkpoint 2: "lost" for "lost or stopped", and the `git grep` for `SKILL_REPAIR_REQUIRED` across
   `origin/docs/*-closeout-residuals-execute*` before X0.2, where any output is the X4.4 stop returned to Nathan.
2. **DC-2**, the table's row 27: X7.6 opens the close-out PR without the X7.7 sentence, records step 28 in §E as
   withdrawn under DN-8 (A), and returns to Nathan for X7.8.
3. **Failure step 2**: the sweep's `--run` names `failure/execute/run.json`.
4. **Failure step 1**: stage the record and `failure/` only, with a `git diff --cached --name-only` check.
5. **Failure step 1**: the failing step's output is copied as counts and ids, with no body text.

**The freeze, as Nathan instructs.** X7.5's lift covers both freezes: the Alpha run's E6 freeze
(`MODIFICATION-20260923-alpha-feedback-open-entries`) and this Modification's. The lift, with its date and Nathan's
words, is recorded in both records' §E (`RESUME-PROCEDURE.md` step 6).

**Where the record stands.** #484 merged as `07b47d8` before the rulings and the diff check were committed. This
approval and everything after `07b47d8` reach `main` in a new pull request. **EXECUTE starts only once that pull request
is on `main`** (X0.1).

## §E — Execution

*Written by MODE = EXECUTE, 2026-09-24, on branch `docs/20260924-closeout-residuals-execute`, opened from `main`
`7028bea` (`EX/run.json` `base`). Evidence is under `EX` = `docs/ephemeral/modifications/evidence/closeout-residuals/execute/`.*

| dated step | spec rows | disposition | evidence |
|---|---|---|---|
| 1 | X0.1–X0.3 | VERIFIED | `main`'s record carries `plan_approved_by`; X0.2's gate passes (`HEAD` = `origin/main`, clean); X0.3 (a) to (d) equal the recorded values; `root_x0.3` recorded (`320 420705ec…`) |
| 2 | X1.1–X1.3 | VERIFIED | patches exit 0, `expected_after_patch` diff exit 0, `root_x1.1` `323 047ca742…`; `EX/gate_pre.json` 12/12 |
| 3 | X2.1–X2.2 | APPLIED, VERIFIED | commit `772c039`; the decision record is `c8cdfd5a…`, 111 107 B; `## D25` once, between D24 and D26; no added `> ` line; `canon.py` imports |
| 4 | X3.1 | APPLIED, VERIFIED | commit `1ef19bf`, the registry alone; `EX/x3.1.json`: `97bda1a0…`, `valid: true`, 55 rows, drift `[]` |
| 5 | X3.2 | APPLIED, VERIFIED | `EX/x3.2.txt`: `cmp` exit 0, 27 files, the build is `ae2bd159…`, and a second reindex rewrites 0 |
| 6 | X3.3 | APPLIED, VERIFIED | `EX/x3.3.txt`: the contract `2b78f877…` and the README `469e2265…` at `docs/graph/contract-template/` |
| 7 | X3.4–X3.5 | APPLIED, VERIFIED | `session-working-rules.md` `2501579e…`; commit `e0b186f` |
| 8 | X3.6 | VERIFIED | `EX/nam002/`: runs 1 to 4 as spec §4.4's table (0; one on ESC-10; one title; 55/16/6, exit 1) |
| 9 | X4.1 | VERIFIED | `EX/x4.1.txt`: `6902924a…` and `dbae180b…` each EQUAL ×2; two expected diff lines |
| 10 | X4.2 | VERIFIED | `EX/gate_pkg.json` 34/34 |
| 11 | X4.3–X4.4 | VERIFIED | `EX/packages.json`: 7 × "Skill is valid!", the extracted digests equal `expected_after_patch.txt`; brief `REVIEWER-PROMPT-cr1.md` committed before the reviewers started (`6a643d6`); SFR-CR1-1 and SFR-CR1-2 both `SKILL_FIT_CONFIRMED`, bound to the seven sha256s; the seven archives, the brief and both verdicts delivered to Nathan; `delivered_cr1` 2026-09-24T14:24:50Z |
| 12 | X4.5 | **BLOCKED** | `EX/rehearsal/`: 54 of 56 pages pass (49 `plan`, 5 `check` and the proposed MGMT-10 body's `check` with `R-ITEM40` 0 and `R-ITEM23-gate` 0; 246 operations; no tool refusal). **PR-30 and ESC-40 were not rehearsed**: the harness's permission classifier refused the rehearsal command ("Data Exfiltration") after each page's fetch. The refusal was not retried or worked around. ESC-25, refused in the dry run, ran this time with the plan's own command and passes (4 operations) |
| 12 | X4.6 | NOT_RUN | the stop at X4.5 |
| 13–28 | X5.0–X7.8 | NOT_RUN | the stop at X4.5 |

**The stop.** It comes before the first external write: nothing was written to Notion, the execution branch is
unmerged, and `main` is unchanged. It is returned to Nathan (`IMPLEMENTATION_BLOCKED`, the successor's *Before it*),
and what follows is his ruling. No item has a final disposition yet.
