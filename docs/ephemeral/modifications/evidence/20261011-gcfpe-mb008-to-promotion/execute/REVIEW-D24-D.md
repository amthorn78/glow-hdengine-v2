SKILL_REPAIR_REQUIRED — 1 REQUIRED finding.

# REVIEW-D24-D — D24 skill review, round 2, of the six MB-008 packages (X10)

**Reviewer:** REVIEWER-D24-D, fresh context. I did not author this change. I was not a round-1 reviewer, I took no part in its ANALYZE or PLAN reviews, and I did not read reviewer C's record.

**Brief:** `execute/BRIEF-D24-R2.md`, committed at `e45c573`. It is the only brief I had.

**Branch:** `claude/mb-008-modification-promotion-fdz2sn`, HEAD `99d14bc` at start and at end (local and remote agree). The one commit after the brief, `99d14bc`, adds only `execute/BRIEF-POSTFLIGHT.md`; it touches no package evidence. **Canon:** `main` at `9312add`. **Date:** 2026-10-12 (UTC).

## Answer

**Verdict: `SKILL_REPAIR_REQUIRED`.** It applies only to the six archives below, measured by me from the bytes I was given. It is void for any other bytes, including a repackaging of the same trees.

| Package | Files | Bytes | sha256 | Extracted freeze digest |
|---|---|---|---|---|
| change-flow.skill | 25 | 390,333 | `eea8dd2068fdce1e0b80c0c84f658745544ac3673663831e4bd9663602204bfd` | `25 c9b0927f327c31328c4b64a0408a946619c985a492702a70a2cd88e216cf22c2` |
| flowmaster-validate.skill | 37 | 507,685 | `1e8d413234cc4d388cb1d3ff7486de182639314bfbcb331889a4dfa0498d4e7c` | `37 02a69b8a99181e79e554299a51dcc31e8b6b629d4974d05c96b191cf948fa200` |
| glow-hde-pr-development.skill | 4 | 23,332 | `1aad2cf4f9ff0ad54dd8612aa78d1bedce7c45be5759163262effa5e847d2409` | `4 f0880ceb6c5d8104a79fb37260ce2cdd90cac110878eaabc2a12106f8b6bbaf0` |
| glow-graph-contract.skill | 9 | 58,371 | `2b6cc39637dc374d2ca3bfb4d2de1cccb90d30fcc1dc8ef46baa7589a5f3131e` | `9 d00c8d1705e3aa181b22c151f103edc9a0f9eccdcfe593fd3a92b90cb0fec6b9` |
| session-relay-flowmaster.skill | 5 | 56,563 | `6028346473f984519d78284efa8d295d257019c83f984ebacd3596427a13c1c4` | `5 33d8b9be98288b1ba698a403964409fb65f5cc53d81cbd94a348ff5b3ce4b52c` |
| amthor-workspace-governance-audit.skill | 15 | 57,190 | `6199c76d1cd607284d7760ec2f121cd665dc7eb152c9e53a3704899cd479fd96` | `15 f0f00820a1df24d20974dd3ad1a58bc4cb8d358d6e7b9a77ccd9ec26329e45f8` |

**Round-1 dispositions.**
- **R-1: fixed** in the governance audit, at both places it was stated (`SKILL.md:48`, `references/interoperability-contracts.md:42`). The new text matches PF06 §0.1A and the change-flow and PR-skill wording. **But the same retired F05 rule survives in flowmaster-validate**, which neither round-1 reviewer nor the author's D26-E search found. That is D-1 below, a new finding, not a defect the repair added.
- **R-2: fixed** at all three places (`SKILL.md:59`, `interoperability-contracts.md:29`, `project-prompt-registry-schema.md:80`). The new text matches D27 and the change-flow and flowmaster-validate wording. No other active text in the six packages gives QA execution to DevOps.
- **The repair added no defect.** It changed exactly the four files C11 names, and nothing else (proof under §8 c). The guard fires on the exact retired sentences; it is narrower than described (L-D2).

**Why the verdict is repair.** flowmaster-validate `SKILL.md:170`, inside *Validate these active GCFPE v2 contracts:* of the section that opens "The 100926.1 contract revision 4.2.0 …", still says: **"Producers never edit/number PF10 or claim adoption."** That is the prose of the 091426.1 contract's triple `producer_edits_pf10: false`, `producer_allocates_pf10_number: false`, `producer_claims_canonical_adoption: false`. This change flipped the middle value to `true` in the 100926.1 contract that the same package bundles, and its own `validate_gcfpe_20261009.py:1728` requires `true`. So the validator skill now tells its reader the opposite of the contract it enforces and of PF06 §0.1A. C11's claim that "no surviving active text in any of the six packages states the retired F02 or F05 rule" is refuted.

| ID | Class | Artifact | Defect |
|---|---|---|---|
| D-1 | REQUIRED | flowmaster-validate `SKILL.md:170` | The retired F05 rule survives as an active validation instruction: "Producers never edit/number PF10 or claim adoption." It contradicts the bundled 100926.1 contract, the package's own validator, PF06 §0.1A, PF27 and the redlined change-flow, PR-skill and audit text. |

There are 2 new LISTED findings (L-D1, L-D2). I re-classify no round-1 LISTED finding.

**This is the second consecutive `SKILL_REPAIR_REQUIRED` round for these packages,** so under D26-A rule 2 Nathan decides before anything more happens. The decision is at the end of this record.

## REQUIRED finding

### D-1 — flowmaster-validate still states the retired F05 rule as an active contract

- **Artifact:** flowmaster-validate, archive `1e8d4132…`, tree `37 02a69b8a…`, `SKILL.md:170`. The bytes are identical in the installed 3.3.2 tree and in round 1's archive. No approved redline and no repair op touches the line.
- **Exact text:** "The exact semantic addendum producers remain CF-C-30, CF-E-30, IA-30, QA-70, RS-20, and ESC-40. One qualifying approval creates exactly one standalone `PF10_BUILD_NOTES_ADDENDUM` with the complete required schema. Nonqualifying outcomes create none. **Producers never edit/number PF10 or claim adoption.**"
- **Where it sits:** the bullet list headed "Validate these active GCFPE v2 contracts:" (`SKILL.md:159`). It belongs to *GCFPE release-profile validation boundary*, whose first sentence is "The 100926.1 contract revision 4.2.0 is regenerated from the final candidate graph" (`:155`). That section also says "Validate the actual producer and both receiver bodies as well as graph/contract agreement". This change redlined the same section at `:155`, `:157` and `:161` (D-FV-1, D-FV-8 and the F07 sentence). `:170` was left as it was.
- **The defect:**
  - The sentence is the prose form of the contract's three flags. In the 091426.1 contract all three are `false`, and the sentence was true. In the 100926.1 contract this change ships (both bundled copies), `pf10_addendum_contract.producer_allocates_pf10_number` is `true`. `format_expectations.heading` is "exactly one H2 carrying the next continuous addendum number, resolved by the producer from current controlled PF10 at creation", and `number_carrier` is "the H2 heading".
  - flowmaster-validate's own `scripts/validate_gcfpe_20261009.py:1728` requires `producer_allocates_pf10_number: True`. Its fixture rule `pf10_numbering` and `PF10NUM-POS-01` project `PRODUCER_NUMBERS_ADDENDUM`. The documentation and the code of one package therefore disagree on the rule.
  - The sentence contradicts PF06-Canon-Change-Process-Guide §0.1A ("Resolve the current continuous addendum number and format before authoring. Each addendum has one H2 with the next number …").
  - It contradicts PF27-Canon-Plan-Templates, *Canon precedence for template use* ("the addendum uses the next continuous numbered H2 heading").
  - It contradicts the approved PLAN PART-01 F05 ("the producer resolves the next continuous number and the format at creation").
  - It contradicts change-flow `SKILL.md:10` and `:327`, glow-hde-pr-development `SKILL.md:147`, and the repaired audit `SKILL.md:48` and `interoperability-contracts.md:42`.
  - flowmaster-validate `SKILL.md` states the new F05 rule nowhere. A search for `H2`, `at creation`, `addendum number`, `0.1A` or `PF06` in it returns nothing.
  - PART-03 of the same PLAN removed the body-side form of this sentence ("The producer never edits PF10, allocates PF10 numbering, …") from the five CL pages for exactly this reason.
- **Why nobody found it:**
  - The approved package-side F05 search (`scope-measurement.md` §1) covered flowmaster-validate `*.md` with the regex `numbering`, `numbers the`, `allocat… (canon|pf10)`, `producer_allocates`. None of these matches "edit/number PF10". The body-side search in the same document (§4, "`number` together with `PF10` or `addendum`") would have matched it, but it was not applied to the packages.
  - Round-1 reviewer A's regex (`numbering|numbers the|allocat… (canon|pf10)|pastes and`) and the author's X10 `d26e_search` literals (`allocate canon numbering`, `pastes and numbers`, `select final PF10 numbering`, …) miss it for the same reason.
  - This is the failure D26-E names: the check tested for the known wording, not for the surviving rule.
- **Evidence (reproducible):**
  - `grep -rn -o -i -E '.{0,140}\bnumber[a-z]*\b.{0,140}' --include=*.md` over the six extracted trees, filtered for `pf10|addend|canon`, gives 9 hits. Seven state the new rule or are a nonproducer about itself (change-flow `:477` QA-10; audit `interoperability-contracts.md:38`, the auditor itself). One is under the *Historical and non-operative* banner (audit `epic-reengineering-interoperability.md:45`). The ninth is flowmaster-validate `SKILL.md:170`.
  - The contract values were read from both bundled copies.
  - The validator requirement: `validate_gcfpe_20261009.py:1728`.
  - No mechanical body check covers this rule. In the installed validator, a producer body is checked only for the literal `PF10_BUILD_NOTES_ADDENDUM` (`PROMPT_PRODUCER`, `validate_gcfpe_20261009.py:2548–2554`).
  - No fixture reads flowmaster-validate's own text.
- **Path, likelihood, consequence:**
  - *Path.* Every load of flowmaster-validate reads this section, including X18's production validation and any later GCFPE maintenance or semantic body review that uses the skill's active-contract list. The skill tells its reader to "Validate the actual producer and both receiver bodies".
  - *Likelihood.* Certain that the text is read; medium that it is applied to a body-level judgement.
  - *Consequence, either way.* An agent that applies the list either reports a conforming producer body (one that numbers its addendum, as PF06 §0.1A requires) as non-compliant, which is loud, or accepts a producer body that has gone back to "producers never number", which is silent.
  - The silent outcome is a silent breach of canon and of the F05 behaviour Nathan approved in the PLAN, and the installed scripts do not catch it.
  - It also leaves an interacting skill incompatible with the successor selection, which PF04-Canon-HDE-Governance §9.1.6 says makes the edited subgroup not ready.
- **Why REQUIRED under D26-A rule 3, and why this is not a restated LISTED finding:**
  - It is a defect on the normal path, with a plausible silent-breach outcome.
  - It is the same defect class as round 1's R-1, which the author accepted as REQUIRED and repaired.
  - It is worse than R-1 in one respect: this change itself made the sentence false, by flipping the contract value in a package whose bundled contract and validator now say the opposite. The audit's F04 text in round-1 L-13 was already wrong before this change.
  - Neither round-1 record mentions flowmaster-validate `SKILL.md:170` (A's R-1 and B's L-B1 cover the audit only), so this is new.
  - It also refutes C11's completion claim, which is D26-F trigger 1.
- **Smallest correction:**
  1. Add one count-checked op to `execute/d24-repair-redlines.json`, flowmaster-validate `SKILL.md`, count 1:
     - old: `Producers never edit/number PF10 or claim adoption.`
     - new, for example: `Producers never edit PF10 or claim adoption; each numbers its addendum at creation from the current controlled PF10 Markdown, in the addendum's H2 heading (`PF06-Canon-Change-Process-Guide` §0.1A).`
  2. Move `FLOWMASTER_VALIDATE_REVISION` from 3.4.0, which is now bound to two rounds' verdicts, to an unspent value, as DR-REV did for the audit (`skill-identity-and-freeze.md`, *Advertised identity must be unspent*).
  3. Recompute `SKILL_TREE_SHA256` last (V7). Nothing else pins `FLOWMASTER_VALIDATE_REVISION`: grep finds it in no script or JSON.
  4. Optionally add `edit/number PF10` to a flowmaster self-check, and widen the D26-E package regex to `\bnumber\w*\b` near `PF10|addendum`.
  5. Rebuild with `package_build.py`. Only flowmaster-validate changes. Rerun the §8 gates, then review the diff (D26-A rule 2) once Nathan has decided.

## LISTED findings (new in this round)

Both are non-blocking under D26-A rule 3: neither changes what the packages do on the promotion path, and each ends loud or needs a future edit.

- **L-D1 — flowmaster-validate `SKILL.md:176` still says "The versioned 37-case section-13 fixture suite".**
  - For the current 100926.1 profile, the suite has 54 cases. The same file's `:386`, D-FV-9, says "the 54 required fixture IDs".
  - The runner enforces 54, so nothing silent follows. The text is merely stale.
  - *Path:* a reader of the boundary section. *Likelihood:* certain to be read. *Consequence:* a reader may think 17 fixtures are extra. It can ride in a D-1 rebuild only if Nathan opts in (D26-A rule 4).
- **L-D2 — the DR-GUARD test is literal and audit-only; its description overstates it.**
  - `test_retired_mb008_role_and_numbering_rules_absent` checks three exact, case-sensitive phrases in the audit's `*.md`.
  - I confirmed it fires on each exact retired sentence restored in a scratch copy: R-1 in `interoperability-contracts.md`, R-2 in `project-prompt-registry-schema.md` and in `SKILL.md`. Each gives 38 tests, 1 failure.
  - Probe: replacing the repaired `SKILL.md:48` sentence with "Producers never edit/number PF10 or claim adoption. DevOps executes QA tasks." passes. That is 38 tests OK, although both retired rules have returned.
  - The record's "fails if either retired rule returns anywhere in the audit's *.md" (x10-packages.json, §E X10, brief §2) is therefore true only of those exact phrases.
  - The guard covers no other package, so it could not have caught D-1.
  - *Path:* a future edit that paraphrases a retired rule back into the audit. *Likelihood:* low. *Consequence:* a silent regression in a later round, which gets its own review. Correct the description, or broaden the guard when the audit is next maintained.

Also seen and **not** raised as findings:
- **A further site of a deferred finding.** The audit's `references/behavioral-fixtures.md:45` says "Initial, not-yet-approved Implementation Plan redlines alone use IA-40". It belongs to the same deferred F04 item as round-1 L-13 and L-B1. I do not re-classify that item. Both contracts already declared IA-40's `MATERIAL_PLAN_DELTA` mode before this change (10 occurrences in each), so round 1's "already wrong before this change" reasoning holds.
- **Old wording only in historical or unreached files.**
  - flowmaster-validate `scripts/validate_epic_alpha.py` maps QA-100 to `'Environment operator'`. Nothing in the suite, `REQUIRED_SCRIPTS` or `SKILL.md` references it; only `run_epic_alpha_fixtures.py` imports it.
  - change-flow's historical correction JSONs (`pre-guide-audit-correction.json`, `epic-alpha-repair-correction.json`) carry pre-D27 / pre-F05 wording, but `SKILL.md` does not link them.
  - The audit's `epic-reengineering-interoperability.md:45` ("Never mutate PF10 or choose final numbering") sits under its *Historical and non-operative* banner.
  - `validate_gcfpe_current.py:323` is the schema-3.1 historical profile, the permitted exception in `scope-measurement.md` §1.

## The claims (brief §5)

| Claim | Disposition |
|---|---|
| C1 | **Confirmed.** `diff -rq` from installed to extracted shows exactly the 26 paths of §8 c, and nothing else differs. `package_build.py --check` gives `equal: true`, `differing: []`, 95 files. |
| C2 | **Confirmed.** My production build's embedded JSON (593,569 B, `43f84f29…`) is byte-equal to both bundled graphs. Both bundled contracts are byte-equal to `execute/contracts/…-production-contract.json` and to my regenerated production contract (`cd291f17…`, 631,061 B). |
| C3 | **Confirmed.** The default run uses profile `GCFPE-20261009.1-100926.1-VALIDATION`. With the 091426.1 contract passed explicitly, the candidate coverage runs `GCFPE-20260914.1-091426.1-VALIDATION` and fails loudly, by design, on `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.1` and `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.1`. The default 100926.1 overlay stays `ok` in the same run. |
| C4 | **Confirmed.** V1: the tokens, the retired token in `CONTRACT_FORBIDDEN`, the `maintenance_metadata` mapping, and the R1 oracle files are unchanged by the diff. V2, V3, V4 (the two new change-flow fixtures; 34/34) and V6 (`CONTRACT_REQUIRED` for change-flow and relay; profile `required_skills` and the PR validator for glow-hde-pr-development) hold. V7: `SKILL_TREE_SHA256` `429eda21…` recomputes with the validator's own `skill_tree_digest`. |
| C5 | **Counts confirmed:** 37 + 17 (11 positive, 6 negative), 54 total, 31 positive and 23 negative. **The method statement is overstated**, as round-1 L-4 and L-B2 found. I confirmed independently that the six untested invariants (`WORK_UNIT_ID`, `added_boundaries.proceed`, `added_boundaries.work_unit`, `pf10_addendum_number` in `forbidden_fields`, `MODEL_OR_STRENGTH_ASSESSMENT`, `approval_artifact`) each turn their positive into `VALIDATION_FAILURE` when removed. With ESC-40's `result_states` stripped of `APPROVE_AS_CHANGED`, REM-POS-01 still projects `REMEDIATION_DECIDED`, which confirms L-B2 defect 1. |
| C6 | **Confirmed** as a description of the code (A2). |
| C7 | **Confirmed** from the validator diff. |
| C8 | **Confirmed.** Shipped 091426.1: 2 `EQUAL` (`dbae180b…`, 613,326 B). Candidate: `90593603…`, 634,423 B, byte-equal. Production: `cd291f17…`, 631,061 B, byte-equal. |
| C9 | **Confirmed, with one correction to the brief's wording.** change-flow 3.4.0, flowmaster-validate 3.4.0 and every live `validator_revision` 3.4.0, glow-hde-pr-development 1.4.0, relay 3.3.0, and glow-graph-contract advertises none. **The audit advertises 1.14.1, not the 1.14.0 that C9 states.** That is DR-REV, correctly described in brief §2. 1.14.1 appears nowhere in the repository outside this repair's own evidence, and nowhere on `main`. |
| C10 | **Confirmed and disclosed** (§E *Disclosed deviations (EXECUTE)*). M-A2's markers are present in the 100926.1 validator's `required_skills`. |
| C11 | **Partly refuted.** Confirmed: only the audit differs from round 1. Reverse-applying `d24-repair.patch` to my extracted audit reproduces round 1's tree digest `15 43e76519…`, so the delta is exactly the four named files, and the audit's other scripts are byte-identical to round 1. The other five archives carry round 1's sha256. **Refuted:** "no surviving active text in any of the six packages states the retired F02 or F05 rule". flowmaster-validate `SKILL.md:170` does (D-1). |

## Answers to the §6 questions

- **A0 — the repair.**
  - R-1 and R-2 are fixed at every place in the audit where the rule was stated. The new texts cite PF06 §0.1A and D27 and use the same wording as change-flow `:10`/`:327`/`:377`, glow-hde-pr-development `:147` and flowmaster-validate `:299`.
  - The guard tests the three exact phrases only (L-D2).
  - The repair added no defect; its diff is exactly `d24-repair.patch`.
  - My own broad matches over all six trees:
    - F05: `number*` near `PF10|addendum|canon`; `(edit|allocate|assign|select|choose)…number`; `numbering`.
    - F02: `devops…qa`, `operator…execut…qa`, `execut… qa`, `kronos (never|does not)…execut`, the retired tokens, `qa executor`, `qa execution remains`, `environment operator`.
  - One active survival remains: D-1. The contract's `support_skill_policy` sentence is round-1 L-1 (deferred), and the remaining hits are the historical exceptions listed above.
  - Canon note, not re-litigated: PF04 §9.1.1's table still names "Authorized environment/DevOps path" for QA task execution, while D27 and the approved PLAN give the Product Owner the choice. Round-1 L-12 already records this, and PF06's executor list (the syntax-normalization paragraph) already names Kronos among possible executors.
- **A1 — the 17 fixtures and six rules.**
  - The rules are faithful to the rulings on the facts they model. F01 matches D27 *Continuity*. F02 matches D27 *QA authorship and execution*: every QA execution needs the Product Owner's arrangement, Kronos never executes Ops, and execution claims no acceptance. F05 matches PF06 §0.1A and PF27. F07 matches PF10 2.1 rules 2–4 and PF04 §9.1.3. F08 matches ESC-40's three verdicts and ESC-25/ESC-30's inputs.
  - F09: my probe gives `PR20_PLANNING_RESUMED` for APPROVE, REJECT and IN_SCOPE_REPAIR, and `VALIDATION_FAILURE` for REVISION_REQUIRED and SPECIFICATION_CHANGE_REQUIRED, matching `receiver_compatibility.PR-20`.
  - Tautology and over-acceptance are as round 1 found: F07 reads only pre-F07 routing tokens, CONT-POS-02 depends on no invariant, `DENY` projects `REMEDIATION_DECIDED`, and any non-Kronos actor is accepted on the Ops lane. I did not re-classify these.
  - The text coupling (F01's sentence, F02's tokens, F08's sentence) is sound but brittle: a rewording fails loudly. F08's stated reason ("the contract carries no field") is wrong (L-B2).
  - The 13 dependency cases prove the 13 dependencies they remove. Six more invariants are real but untested (C5).
  - No fixture reads flowmaster-validate's own text, which is why D-1 is invisible to the suite.
- **A2 — change-flow's `validate_gcfpe_20261009.py`.**
  - Removing the URL-map and topology checks dropped nothing 100926.1 has.
  - Staged parents are still pinned: `EXPECTED_PARENT_BY_LANE` (16 lanes) equals `staged_parent_id` for all 55 members by exact lane.
  - Page bindings remain in flowmaster's validator. Member URLs are compared with the graph, which proves only derivation consistency (round-1 L-15).
  - Every pin is measured from the right artifact: graph `43f84f29…`/593,569, plan `4de47784…`/50,156 (equal to `PLAN-20261011.md` at HEAD), predecessor `dbae180b…` (equal to both bundled 091426.1 contracts), routing surface `d3a08833…`/290. The routing surface was computed by each validator's own `routing_surface()` on the bundled contract.
- **A3 — the X8 additions.** They are sound and disclosed. M-A2's three PR-skill markers (1.4.0 and V6's two phrases) are in `required_skills`, and C20/C21 are in change-flow's check. The dry-run gap (N6 measured before N8 moved the PR revision) is accurately disclosed. No finding.
- **A4 — V5.**
  - No default resolves 091426.1 as current: `validate_flowmaster.py`, `validate_gcfpe_current.py` and `run_gcfpe_current_fixtures.py` all default to 100926.1, and each dispatches 091426.1 only on its `target_release`.
  - The `gcfpe_20260914_candidate*` keys carry 100926.1 results in the explicit run, labelled by their own `profile` field. That is misleading to a human and harmless to a machine; round-1 L-6 already lists it.
- **A5 — the Kronos substring.** My probes in a scratch root:
  - The retired token replacing the active `KRONOS_NEVER_EXECUTES_OPS.` line: suite `FLOWMASTER_SUITE_FAIL` (`FMV-SKILL-STRUCTURE-001`), and change-flow's check fails ("missing skill clause").
  - Added beside the new token: suite FAIL, and change-flow fails ("retired skill clause present").
  - Inside the marked prohibition block: suite PASS, change-flow fails.
  - So the token cannot survive as active text without a loud failure. Inside the block it is caught only by change-flow's own gate (round-1 L-5). Outside the validators' own lists, it remains only in the two immutable R1 oracle files.
- **A6 — the redlines as landed.** `package_apply.py --check` on the extracted trees gives 44 `LANDED`. AU-REV and AU-REV-FX report `CONFLICT` (not landed) because DR-REV/DR-REV-FX supersede them. F01, F02, F04, F05, F07, F08 and MB-003 read as approved and agree with D27, PF06 §0.1A, PF27, PF10 2.1 and PF04 §9.1.3. SR-F07-1's "run" is as disclosed. The approved redline set left F05 un-reconciled in flowmaster-validate (D-1).
- **A7 — the docs.**
  - D-FV-1..9 match the code, with three exceptions: D-FV-1's "on `main`" (round-1 L-7/L-B3), D-FV-8's two-release dispatch (L-6), and the unredlined `:170` and `:176` in the same section (D-1, L-D1).
  - D-GG-1 matches the code except as round-1 L-10/L-B4 record. I confirmed that the filled release-values file also sets `receiver_compatibility.PR-20`, which D-GG-1's list omits.
- **A8 — fit with the 100926.1 candidate.** The contract has 55 members, equal to the graph's 55 node ids, and 235 edges. All 55 members are at `100926.1`, `SELECTED_PRODUCTION`. MGMT-10's page id, URL and parent equal `x1-successor.json`, with four result states. QA-100's receiving role states D27. The profile pins agree with the bundled contract, graph and fixtures. Bodies are X12's to check.
- **Q1 — false between build and X16?** Yes, and harmless while the X17 install order holds. The contract's selection fields, change-flow's "current overlay is 100926.1" and flowmaster-validate's 100926.1 default are all false until X16. One claim stays false after install: `REPOSITORY_FILE_ON_MAIN`. `git cat-file -e origin/main:…/PLAN-20261011.md` fails at `9312add`, so it stays false until PR #605 merges (X22). D-1's sentence is false from build onward and stays false after install.
- **Q2 — mark the 091426.1 change-flow check historical?** Yes, cheaply: a one-line docstring in `scripts/validate_gcfpe_20260914.py` (it still says "Deterministic checks for the GCFPE-20260914.1 Change Flow successor") or a mention in change-flow's paragraph on superseded 091426.1 records. Run, it prints a bare `FAIL: specialization revision`. It is not needed for these bytes: no document names it as a current gate.

## What I ran

I worked in `/tmp/d24d` with `PYTHONDONTWRITEBYTECODE=1` on every Python command. Helpers that read untrusted bytes ran with `-I`. I read every tool's top-level flag by name.

- **§8 a — archives.**
  - Sizes, sha256 and entry counts equal §1. Every entry sits under its skill root, with no absolute path, no `..` segment, no backslash, no directory entry and no symlink.
  - `name:` is unchanged in all six frontmatters.
  - Extracted freeze digests equal §1.
  - `quick_validate`: "Skill is valid!" for all six.
- **§3 — baseline.** All six installed freeze digests equal §3, measured both on copies and read-only on the synced directory. The baseline reproduced before anything else.
- **§8 b — gates from the extracted root.** The root held the six packages plus the seven L3 siblings copied from the installed tree.
  - `validate_flowmaster.py --skills-root`: exit 0. `FLOWMASTER_SUITE_PASS`, `suite_ok` true, all finding counts 0, `self_identity` OK. Current overlay: profile 100926.1, `ok` true, contract `cd291f17…`, graph `43f84f29…`, 55 nodes, 235 edges. Current fixtures: `fixture_suite_ok` true, 54/54, 55/55 variants, 283 cases, 13 dependency cases passing. `rows_exact` and `interfaces_closed` true. Change-flow fixtures 34/34.
  - The same run with the explicit 100926.1 contract and candidate root: exit 0, `FLOWMASTER_SUITE_PASS`.
  - flowmaster `validate_gcfpe_20261009.py`: exit 0, `ok` true, `errors` [].
  - `run_gcfpe_20261009_fixtures.py`: exit 0, `fixture_suite_ok` true, 54/54, 55 variants, 283 cases.
  - `run_change_flow_fixtures.py`: exit 0, 34 (14 positive, 20 negative), `fixture_suite_ok` true.
  - change-flow `validate_gcfpe_20261009.py`: exit 0, `PASS`. Its 091426.1 sibling: exit 1, `FAIL: specialization revision`, by design.
  - `validate_glow_hde_pr_development.py`: exit 0, `PASS`.
  - Audit `run_fixture_suite.py`: exit 0, 38 tests, `OK`.
  - `validate_relay_manifest.py --self-test`: exit 0, `status` PASS.
  - Regenerator, from the repository root: as in C8.
  - `package_build.py … --check`: as in C1. The graph argument was the embedded JSON of my production build plus its final LF.
- **§8 c.** The exact 26-path list. Reverse-applying `d24-repair.patch` gives round 1's audit tree.
- **§8 d.**
  - The profile's `candidate_contract`, `frozen_graph` and `fixtures` pins match the bundled files.
  - Fixtures: 54 (31 positive, 23 negative); `required_fixture_ids` is in row order.
  - `negative_rule_attribution` equals the runner's `EXPECTED_NEGATIVE_RULES` and covers exactly the negatives.
  - Parents, members and edges as in A2 and A8.
- **§8 e.** Every pin recomputed from its artifact:
  - flowmaster `EXPECTED_FROZEN_GRAPH_SHA256`/`BYTES`, `EXPECTED_CANDIDATE_CONTRACT_SHA256`/`BYTES`, `EXPECTED_FIXTURE_SHA256` (`e24c881d…`, 26,868 B), routing surface and rows, and the governing-plan literal;
  - change-flow `EXPECTED_GRAPH_SHA`, `EXPECTED_PLAN_SHA`/`BYTES`/`PATH`, predecessor, routing surface and rows;
  - the profile JSON and the contract's own `source_snapshot` pins;
  - `SKILL_TREE_SHA256`.
  All agree.
- **§8 f.** Every live revision site is 3.4.0, 1.4.0, 3.3.0 or 1.14.1. Old values remain only in the 091426.1 history files, the R1 oracle's `2.0.0` anchor (mapped) and dated narrative.
- **Beyond the brief:**
  - the broad matches in A0;
  - the guard probes (L-D2);
  - the Kronos-token placement probes (A5);
  - rule and invariant probes on `project_behavior` (A1, C5);
  - the suite with the explicit 091426.1 contract (C3).
- **Could not run, or did not run:**
  - No body-level check: under L1 and D22 no prompt body was read, copied, hashed or compared.
  - No live Notion state (L5).
  - I did not run `package_skill`, because archives do not reproduce by repackaging (L2), nor the author's `x8_gates.py`; I reran its gates myself.
  - I did not re-probe D-GG-1's refusal paths, which round-1 B probed.
- **Freeze:**
  - At the end, all 13 installed skills measure the same digests as at the start, for example `glow-merged-change-attribution-lock 10 c518ccb0…` and `typesafe-scoring 3 088c77f3…`.
  - The six source archives still hash to §1.
  - My working root measured the same before and after every gate, and no `__pycache__` appeared.
  - No skill was installed, and the tree did not move under me, so the review is not void.
- **Repository writes:** this record only. No commit, no push, no Notion write, nothing in the synced directory.

## Decision for Nathan

Round 1 was `SKILL_REPAIR_REQUIRED` (reviewer A). This full review 2 is `SKILL_REPAIR_REQUIRED` with one required defect, D-1. D26-A rule 2 says that "after two consecutive `SKILL_REPAIR_REQUIRED` rounds, Nathan decides before a third", and permits at most one check of a repair's diff.

D26-A rule 5's early-stop signals are not met: the required count halved from 2 to 1, and D-1 is not in text the last repair added.

Nathan's options:
1. **Authorise the one-line repair of D-1** described above (flowmaster-validate `SKILL.md:170`, an unspent `FLOWMASTER_VALIDATE_REVISION`, `SKILL_TREE_SHA256` last), followed by the single permitted diff check. L-D1 can ride along if he opts in.
2. **Accept D-1 as a risk in the promotion packet**, knowing the installed validator skill would state the retired F05 rule against its own contract.

**Canon relied on:**
- `AGENTS.md`.
- Read on `main` `9312add`:
  - PF10-HDE-Build-Notes v13.5.2, in full: precedence rules 1–9 and addendum 2.1.
  - PF06-Canon-Change-Process-Guide v2.5.4: §0.1A, read in full, and the QA-executor syntax-normalization paragraph (search hit read in context).
  - PF04-Canon-HDE-Governance v2.8.7: §9.1.1, §9.1.2, §9.1.3, §9.1.4 and §9.1.6, read in full.
  - PF27-Canon-Plan-Templates v2.0.5: *Canon precedence for template use*, read in full.
- Repository controls:
  - `gcfpe.decision-record.md` D24, D26 and D27, read in full; D22 and D23 by heading.
  - `skill-packaging-and-delivery.md`, *Skill packaging and installation*.
  - `skill-identity-and-freeze.md`, in full.
  - `freeze.py`.
- In-flight documents:
  - `MODIFICATION-20261011-gcfpe-mb008-to-promotion`: *Approval to enter EXECUTE*, §E and *Disclosed deviations (EXECUTE)*.
  - `PLAN-20261011.md`: PART-01, PART-03 and PART-04; the §7 X14–X22 rows.
  - `scope-measurement.md` §1 and §4.
  - `plan/package-redlines.json`, `plan/package_apply.py`.
  - `execute/package_build.py` (header and the revision substitutions).
  - `execute/d24-repair-redlines.json`, `d24-repair.patch`, `x10-packages.json`, `x10-repair-gates.json`, `contracts/release-values-100926.1.filled.json`, `x1-successor.json`.
  - `REVIEW-D24-A.md` and `REVIEW-D24-B.md`, in full.

DECISION NEEDED
