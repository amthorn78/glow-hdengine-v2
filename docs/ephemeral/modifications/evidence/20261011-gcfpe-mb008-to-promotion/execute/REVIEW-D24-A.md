SKILL_REPAIR_REQUIRED — 2 REQUIRED findings.

# REVIEW-D24-A — D24 skill review of the six MB-008 packages, MODIFICATION-20261011-gcfpe-mb008-to-promotion (X10)

**Reviewer:** REVIEWER-D24-A, fresh context. I did not author this change. I took no part in its ANALYZE or PLAN reviews, and I did not read reviewer B's record.

**Brief:** `execute/BRIEF-D24.md`, committed at `894966c`. It is the only brief I had.

**Branch:** `claude/mb-008-modification-promotion-fdz2sn`. HEAD was `894966c` when I started and `081c217` when I finished. The author's commits in between (`517ac44`, `eba7599`, `081c217`) added X11, X12 and X13 evidence and reviewer B's record. None of them touched the package evidence: `package_build.py`, the redlines, the patch, `make_profile_20261009.py` and `execute/contracts/` are unchanged.

**Canon:** `main` at `9312add`. **Date:** 2026-10-12 (UTC).

## Answer

**Verdict: `SKILL_REPAIR_REQUIRED`.** It applies only to the six archives below. It is void for any other bytes.

| Package | Files | Bytes | sha256 | Extracted freeze digest |
|---|---|---|---|---|
| change-flow.skill | 25 | 390,333 | `eea8dd2068fdce1e0b80c0c84f658745544ac3673663831e4bd9663602204bfd` | `25 c9b0927f327c31328c4b64a0408a946619c985a492702a70a2cd88e216cf22c2` |
| flowmaster-validate.skill | 37 | 507,685 | `1e8d413234cc4d388cb1d3ff7486de182639314bfbcb331889a4dfa0498d4e7c` | `37 02a69b8a99181e79e554299a51dcc31e8b6b629d4974d05c96b191cf948fa200` |
| glow-hde-pr-development.skill | 4 | 23,332 | `1aad2cf4f9ff0ad54dd8612aa78d1bedce7c45be5759163262effa5e847d2409` | `4 f0880ceb6c5d8104a79fb37260ce2cdd90cac110878eaabc2a12106f8b6bbaf0` |
| glow-graph-contract.skill | 9 | 58,371 | `2b6cc39637dc374d2ca3bfb4d2de1cccb90d30fcc1dc8ef46baa7589a5f3131e` | `9 d00c8d1705e3aa181b22c151f103edc9a0f9eccdcfe593fd3a92b90cb0fec6b9` |
| session-relay-flowmaster.skill | 5 | 56,563 | `6028346473f984519d78284efa8d295d257019c83f984ebacd3596427a13c1c4` | `5 33d8b9be98288b1ba698a403964409fb65f5cc53d81cbd94a348ff5b3ce4b52c` |
| amthor-workspace-governance-audit.skill | 15 | 56,871 | `8c68ab082d614d9f1ddd4a2820d291b0de50849df2a8c9567157ab883a507931` | `15 43e765196bd73d9a484b9739aee78560ef856f48e92bff57e5124db60ed6a438` |

**What reproduced.** Every measurement above I took from the bytes I was given.

- The baseline reproduces: all six installed freeze digests match §3.
- Every gate in §8 passes from the extracted contents.
- `package_build.py --check` rebuilds the extracted trees exactly (95 files).
- The regenerator reproduces the shipped 091426.1 contract on both bundled copies, and both X7 contracts byte for byte.
- Every hash pin agrees with the artifact it pins.
- C1, C2, C8 and C9 hold as stated. C3 to C7 hold, with the limits listed below.

**Why the verdict is repair.** The change retires two rules, F05's "the producer does not number the addendum" and F02's "DevOps executes QA". It rewrites them in change-flow, flowmaster-validate and the PR skill. In the governance audit, it rewrites them on some lines and leaves the old rule standing on neighbouring lines. The audit is the read-only validator for the prompt ecosystem. Its `SKILL.md:146` tells the auditor to enforce the rules in `interoperability-contracts.md`. As shipped, it states both the old and the new rule for each.

ANALYZE searched for leftover F02 and F05 wording only in change-flow, flowmaster-validate and glow-hde-pr-development (`scope-measurement.md` §1). So the audit was never searched for those two rules, which D26-E requires. Each fix is a few lines of text.

| ID | Class | Artifact | Defect |
|---|---|---|---|
| R-1 | REQUIRED | amthor-workspace-governance-audit `SKILL.md:48`, `references/interoperability-contracts.md:42` | The retired F05 rule survives as a rule the auditor enforces: "The producer does not edit PF10, allocate canon numbering, or claim adoption." This contradicts PF06 §0.1A, the bundled 100926.1 contract and the redlined change-flow and PR-skill text. |
| R-2 | REQUIRED | the same package, `SKILL.md:59`, `references/interoperability-contracts.md:29`, `references/project-prompt-registry-schema.md:80` | The pre-D27 role rule survives: "DevOps owns bounded Ops and QA execution" / "DevOps executes bounded Ops and QA instructions/tasks". Each sits next to a line this change rewrote to say QA execution follows the arrangement the Product Owner chooses (`D27`). |

There are 15 LISTED findings, L-1 to L-15.

## REQUIRED findings

### R-1 — the governance audit still states the retired F05 numbering rule

- **Artifact:** amthor-workspace-governance-audit, in the archive `8c68ab08…` (tree `15 43e76519…`).
  - `SKILL.md:48`: "Every addendum carries the exact base, … The producer does not edit PF10, allocate canon numbering, or claim adoption."
  - `references/interoperability-contracts.md:42`: "Addendum production does not edit PF10, allocate canon numbering, or claim adoption."
  - Neither line is touched by any of the 46 redlines. Both are identical in the installed 1.13.0 tree.
- **Defect:** this is the sentence F05 retires, and the shipped audit enforces it. It contradicts:
  - **PF06-Canon-Change-Process-Guide §0.1A**: an agent-authored addendum's author resolves "the current continuous addendum number and format before authoring".
  - **The contract this release ships:** `pf10_addendum_contract.producer_allocates_pf10_number: true`, and `format_expectations.number_carrier` is "the H2 heading".
  - **change-flow `SKILL.md:327`** (redline CF-F05-1) and **glow-hde-pr-development `SKILL.md:147`** (PR-F05-1).
  - **change-flow's own `validate_gcfpe_20261009.py`** (C18), which now rejects the literal "allocate canon numbering" in change-flow.

  PF04 §9.1.6 requires interacting skills to be reconciled "in one coherent successor selection", and "an edited subgroup is not ready while an affected counterpart remains incompatible". ITEM-04 of this Modification exists to remove exactly these statements from the bodies and PE.
- **Evidence:**
  - Broad match `numbering|numbers the|allocat… (canon|pf10)|pastes and` over all six extracted trees, `*.md` and `*.py`.
  - The only hits that still say the producer does not number are these two audit lines. Every other hit is the new wording.
  - `SKILL.md:146` makes the `interoperability-contracts.md` rules enforced: "For Glow HDE, enforce the project-specific invariants in interoperability-contracts.md".
- **Path, likelihood, consequence:**
  - The audit is the read-only prompt-ecosystem validation mechanism (`authoritative-surfaces.md`, `ecosystem-change-management.md`).
  - The normal path is every GCFPE audit run with 1.14.0. The line is read on every run, so the likelihood is certain.
  - The auditor's rule says the six producers (CF-C-30, CF-E-30, IA-30, QA-70, RS-20, ESC-40) must not allocate numbering, yet their 100926.1 bodies must. So it either reports the canonical behaviour as non-compliant, or it accepts a body that has gone back to "no producer numbers". The second outcome is a silent breach of canon.
  - This is a defect on the normal path, so it is REQUIRED under D26-A rule 3.
- **Smallest correction:**
  1. Replace both sentences with change-flow's F05 wording. For example: "The producer does not edit PF10 or claim canonical adoption; it numbers the addendum at creation from the current controlled PF10 Markdown (PF06 §0.1A)."
  2. Ship it as two count-checked redlines, or as named substitutions in `package_build.py`. Optionally, add `assertNotIn("allocate canon numbering", …)` to the audit's `run_fixture_suite.py`.
  3. Rebuild, rerun the audit fixture suite and the flowmaster suite, and re-review the new bytes (D24 condition 5, within D26-A rule 2).

### R-2 — the governance audit still gives QA execution to DevOps, beside the D27 lines this change wrote

- **Artifact:** the same package, three lines.
  - `SKILL.md:59`: "Kronos is QA-only. DevOps owns bounded Ops and QA execution, not PR-development workflow control."
  - `references/interoperability-contracts.md:29`: "DevOps executes bounded Ops and QA instructions."
  - `references/project-prompt-registry-schema.md:80`: "… Kronos is QA-only; DevOps executes bounded Ops and QA tasks; …"
- **Defect:** `D27` (QA authorship and execution) gives the Product Owner wide latitude over execution, and no executor or session identity is required. The approved F02 text says Kronos may execute QA when the Product Owner chooses it. The package now states the old rule and the new one side by side:
  - `interoperability-contracts.md:29` keeps the old rule. The very next line, `:30`, was redlined by AU-F02-2 to "QA execution remains with the QA lane, under the execution arrangement the Product Owner chooses (`D27`)".
  - `SKILL.md:59` keeps "DevOps owns … QA execution". `SKILL.md:42` was redlined by AU-F02-1 to the D27 wording.

  change-flow `SKILL.md:377` and flowmaster-validate `SKILL.md:299` state D27. The audit's rule catalog makes the stale line enforceable: `ROL-001`, ERROR, "IA, Isis, Thoth, Kronos, PO, or DevOps duties are conflated".
- **Evidence:** I searched all six trees for `kronos|DevOps owns|DevOps executes|QA execution`. The only lines still giving QA execution to DevOps are these three audit lines. The redlined lines sit beside them.
- **Path, likelihood, consequence:**
  - The normal path is every GCFPE audit, so the likelihood is certain.
  - An auditor following `SKILL.md:59` either reports a QA execution by Kronos that the Product Owner chose as `ROL-001`, or accepts a body that restores DevOps-only execution. The second outcome is a silent breach of a Product Owner ruling.
  - Unlike the body-side F02 text accepted at PLAN round 1 as L-A12, this text is in a package this change edits for F02, and that package now contradicts itself. That makes it REQUIRED under D26-A rule 3.
- **Smallest correction:** three one-line redlines in the same rebuild as R-1.
  - `SKILL.md:59`: "DevOps owns bounded Ops execution; QA execution follows the arrangement the Product Owner chooses (`D27`); neither is PR-development workflow control."
  - `interoperability-contracts.md:29`: "DevOps executes bounded Ops instructions. …"
  - The registry schema line becomes "DevOps executes bounded Ops tasks; QA execution follows the Product Owner's chosen arrangement (`D27`)".

## LISTED findings

Each is non-blocking under D26-A rule 3: it ends in a loud failure, or it has no silent wrong outcome on the normal path.

- **L-1 — the 100926.1 contract carries the retired F02 sentence.**
  - **Where:** `pr_development_contract.support_skill_policy`, in both bundled copies, reads "…; QA execution remains with the authorized QA lane and its operator." It is the same sentence that CF-F02-5 and AU-F02-1 retire in change-flow and the audit.
  - **Where it comes from:** the 091426.1 contract template. No release-values op covers it, and no validator pins it.
  - **Why listed:** in context it denies support skills QA authority, and "its operator" can be read as the operator the Product Owner chooses.
  - **If a repair happens:** fold it in with a release-values `set` op. Both contracts then regenerate, and every pin moves.
- **L-2 — the F07 fixture rule never reads anything F07 changed.**
  - `typesafe_reading` projects its positives from `prohibited_active_routing ⊇ {MODEL_OR_STRENGTH_ASSESSMENT, REASONING_RECOMMENDATION}`. That set predates F07, and the rule never reads change-flow's reading rule.
  - Probe: TS-POS-01 and TS-POS-02 still project `TYPESAFE_READING_RECORDED` / `TYPESAFE_NOT_READ_RECORDED` with the 091426.1 contract and the installed 3.3.1 change-flow text, which forbade the reading.
  - `dependency-f07-prohibited-routing` therefore proves a dependency on the old routing ban, not on F07. F07 is enforced elsewhere: V6's required phrases, change-flow C17, and the profile's `PROMPT_TYPESAFE_READING` body check. So there is no silent path.
- **L-3 — the new rules work only on the facts they model.** With the current contract and text, each of these projects a pass although the ruling forbids it:
  - F01: a PR-35 recovery into the PR-30 session (`pr35_in_pr30_session`) projects `RECOVER_FROM_ROLE_AND_ARTIFACTS`. D27 keeps two dedicated phase sessions.
  - F02: any non-Kronos actor on the Ops lane projects `OPS_EXECUTION_BY_AUTHORIZED_OPERATOR`. I tried `Isis` and `PR-30`.
  - F07: a reading without its probabilities and flags, and a pick Nathan did not state, both project `TYPESAFE_READING_RECORDED`.
  - F08: `DENY` with an addendum, and `APPROVE` with two addenda, both project `REMEDIATION_DECIDED`, although the contract's `never_for` includes `DENIAL` and its `exactly_one_per_qualifying_approval` is true. A legacy id without exact lineage projects `REMEDIATION_INPUT_ACCEPTED`.
  - CONT-POS-02's `CONTINUE_RECORDED_SESSION` depends on no invariant at all.

  This matches the style of the existing rules. The suite is a fixture model, not runtime behaviour.
- **L-4 — C5 overstates the dependency cases.** "13 dependency cases remove each invariant once" is not literal. Six invariants the rules read are never removed:
  - `WORK_UNIT_ID` in `shared_exactly_one`;
  - `added_boundaries.proceed` and `added_boundaries.work_unit`;
  - `pf10_addendum_number` in `forbidden_fields`;
  - `MODEL_OR_STRENGTH_ASSESSMENT`;
  - `native_remediation_contract.approval_artifact`.

  I mutated each one, and each turns its positive into `VALIDATION_FAILURE`. So they are real dependencies, but untested. D-FV-9's "for each MB-008 rule, a case removing the invariant it projects from" is accurate as written.
- **L-5 (A5) — the suite allows the retired Kronos token inside the prohibition block.**
  - With `KRONOS_NEVER_EXECUTES_OPS_OR_QA.` added inside change-flow's marked prohibition block, the suite still returns `FLOWMASTER_SUITE_PASS`. Its forbidden-phrase check skips that block, and flowmaster-validate `SKILL.md` item 17 says so.
  - change-flow's own `validate_gcfpe_20261009.py` fails it: "retired skill clause present". So the catch is loud, but only at change-flow's own gate.
  - The F02 rule tests presence of `KRONOS_NEVER_EXECUTES_OPS` as a substring, which the old token satisfies. Old text fails only because `QA_EXECUTION_ARRANGEMENT = PRODUCT_OWNER_CHOICE` is required alongside it.
- **L-6 (V5, A4, D-FV-8) — "an explicit contract runs its own release's profile" holds for two releases only.**
  - The suite's `--gcfpe-contract` sends every contract whose `target_release` is not `GCFPE-20260914.1` to the 100926.1 profile.
  - Passing the 091326.2 alias explicitly therefore runs `GCFPE-20261009.1-100926.1-VALIDATION` against `GCFPE-20260913.1` and fails loudly with misleading errors (`ABORT_PROMPT`, `ALPHA_PROMOTION_RECORD`, …). D-FV-8's "each by its own release's profile" is inaccurate on that path.
  - The coverage keys `gcfpe_20260914_candidate*` carry 100926.1 results. That is misleading but harmless, because each report carries its `profile` field.
- **L-7 (Q1, D-FV-1) — the governing plan is called a file "on main" before it is.**
  - The contract's `governing_plan.representation` is `REPOSITORY_FILE_ON_MAIN`, and change-flow's validator requires that value. D-FV-1 says the contract "binds its governing plan as a repository file on `main`".
  - `PLAN-20261011.md` is not on `main` until PR #605 merges at X22, after the X17 install and the X18 production validation. If the PR never merges, the claim stays false.
  - A reader who looks for the plan on `main` finds nothing, which is loud. The value is the approved release value.
- **L-8 — dead staging code in the 100926.1 profile validator.** `validate_package` keeps the 091426.1-era staging block (around lines 2697–2712). For an `UNSELECTED_CANDIDATE` contract it pins the staging alias to the 091326.2 contract (54 members, hash `bf5140c9…`), while the profile says the staging release is GCFPE-20260914.1 with 55 members. It cannot be reached for 100926.1: any unselected contract fails `CONTRACT_HASH` first, because the pin is the production contract.
- **L-9 — a wrong comment in change-flow's validator.** Comment C14 in change-flow's `validate_gcfpe_20261009.py` says 229 edges become 235 because MGMT-10 drops two edges. In fact 235 is the parent candidate's 237 minus 2. The check itself is measured from the graph and the contract.
- **L-10 (A7) — the D-GG-1 documentation overstates what is derived from the graph.**
  - It says "the Notion page manifest" is derived from the graph. In fact `notion_page_manifest[*].parent_id` and `member_registry[*].staged_parent_id` are carried from the 091426.1 template; I confirmed this for all 55 members.
  - That is correct for 100926.1 only because its members sit under their predecessors' parents. For a future release whose members move parents, the values would be silently stale, and no release-values op covers parents.
  - Its list of release literals omits `receiver_compatibility.PR-20`, which `release-values-100926.1.filled.json` sets.
  - It says "five named prompt references", but the code derives six (the alpha trigger's PR-10 too).
  - `regenerate_contract.py`'s docstring still says the 091426.1 contract regenerates through `acceptance`, which P-L1 shows fails. `release_value_ops` guards with `assert`, which `python -O` skips.
- **L-11 — the alpha record is not "unchanged".** change-flow says the `alpha_resumption_contract` "in the graph and the current contract is the record made at the 091426.1 promotion, validated unchanged as that record". In the 100926.1 contract, `successor_trigger.prompt` was re-pointed to PR-10 100926.1 (new page id, URL and version) by the regenerator's named-prompt derivation. The state fields are unchanged and pinned. The prompt identity is not.
- **L-12 — the GCF-23 actor, and a possible canon tension.**
  - The immutable R1 oracle and the bundled runtime map still describe GCF-23 as "Kronos creates task; authorized DevOps/environment operator executes; Kronos reviews evidence". change-flow's prose overrides this for D27 without re-pinning the row, which D23-D did for GCF-17. The approved PLAN chose this ("the immutable R1 oracle stays byte-identical").
  - Canon note, not re-litigated here: PF04 §9.1.1 says "QA task execution | Authorized environment/DevOps path | Kronos independently reviews actual evidence", and PF19 says "Authorized operators execute … Kronos reviews their evidence".
  - When the Product Owner chooses Kronos as executor, Kronos reviewing its own execution sits uneasily with "independently". D27 decided the arrangement, and the packages add "execution confers no acceptance authority".
- **L-13 — older stale text in the audit, already wrong before this change.**
  - `references/interoperability-contracts.md:96`, under *Current-release validation*, still names "candidate/selected successor `GCFPE-20260914.1`" with "sole PR-35". `SKILL.md:30` makes it conditional on the register.
  - `references/project-prompt-registry-schema.md:80` says "IA-40 revises only an initial, not-yet-approved Implementation Plan". That contradicts IA-40's `MATERIAL_PLAN_DELTA` mode, which both the 091426.1 and 100926.1 contracts declare.
- **L-14 — leftover section-13 naming in the 100926.1 fixtures.** The fixture document keeps `governing_plan_section: "13"` and the suite id `…-SECTION-13`. The 100926.1 governing plan (`PLAN-20261011.md`) has 12 sections. The `mb008_cases` note explains where the cases come from.
- **L-15 (A2) — the 100926.1 URL check proves nothing independent.** "member Notion URLs are the graph's" only compares the contract with the graph it was derived from. Unlike the dropped URL-map and topology readback, it is not independent evidence. No Notion readback of member URLs or parents is bundled for 100926.1. That is acceptable because no staging move happened. Live verification happens at runtime, as change-flow requires, and at X4, X6 and X12.

## Answers to the §6 questions

- **A1 — the 17 fixtures and six rules.**
  - **Each ruling against its rule:**
    - F01 matches D27's continuity row.
    - F02 matches D27's QA row and the redlined tokens.
    - F05 matches PF06 §0.1A and PF27: the H2 carrier, numbering resolved at creation, no standalone number field.
    - F07 matches PF10 2.1 rules 2 to 4, PF04 §9.1.3's surface advice and DN-B option 2 (no Notion row).
    - F08 matches ESC-40's three verdicts and ESC-25/ESC-30's proposal or legacy id.
    - F09 matches PR-20's RS-20 return (APPROVE, REJECT, IN_SCOPE_REPAIR) only from the recorded planning origin, before Proceed.
  - **Tautology:** F07 is tautological with respect to the change (L-2), and CONT-POS-02 is tautological outright (L-3).
  - **Accepting what the ruling forbids:** yes, for facts the rules do not model (L-3).
  - **Reading change-flow's text:** the coupling is sound but brittle. A rewording of the exact sentence fails the suite loudly. A missing `SKILL.md` gives an empty text, which also fails loudly.
  - **Dependency cases:** the text-based ones prove dependency on the exact strings. Six contract dependencies are untested (L-4).
  - **Counts:** 54 fixtures (31 positive, 23 negative), 55 variants and 283 cases, with 13 of 13 dependency cases passing. The first 37 scenarios are byte-for-byte the 091426.1 ones; only header fields changed.
- **A2 — change-flow's `validate_gcfpe_20261009.py`.**
  - Removing the URL-map and topology checks dropped nothing 100926.1 has.
  - Kept: the staged parents (`EXPECTED_PARENT_BY_LANE`, equal to the contract's lane parents and to X1's MGMT-10 parent), the manifest parent parity, and the 55-member identity checks.
  - Added: the plan pin as a repository file, the predecessor-contract pin, F05's keys and requirement, and the F01/F02/F07/F08 clauses (required) and the retired F02/F05 clauses (forbidden).
  - The URL check proves only derivation consistency (L-15).
  - Every pin is measured from the right artifact: the graph `43f84f29…` (593,569 B), the plan `4de47784…` (50,156 B), the predecessor `dbae180b…`, and the routing surface `d3a08833…`/290, computed by both validators' own `routing_surface`.
- **A3 — the X8 additions.**
  - M-A1 (fixture count 54) and M-A2 (the PR skill's 1.4.0 marker and V6's two phrases) are needed. Without M-A2 the 100926.1 profile fails on the 1.4.0 PR skill.
  - C20 is needed because the contract carries `format_expectations` in a closed key set. C21 adds F05's requirement.
  - All four are named, count-checked substitutions, disclosed in §E's EXECUTE deviations and reproduced by `--check`. The disclosed gap in the dry run, that it ran before the redlines moved the PR revision, is accurately stated. No finding.
- **A4 — does anything still treat 091426.1 as current?**
  - No default treats the 091426.1 contract as current. `validate_gcfpe_current`, `run_gcfpe_current_fixtures` and the suite all default to 100926.1.
  - With the 091426.1 contract passed explicitly, the suite runs the 091426.1 profile and fails loudly, by design, on `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.1` and `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.1`.
  - The coverage key names are misleading but harmless (L-6). The audit's 091426.1-specific text is conditional (L-13).
- **A5 — can the retired Kronos token survive?** It can survive, as far as the suite is concerned, only inside change-flow's marked prohibition block, where a reader would read it as a prohibition entry. change-flow's own validator rejects it anywhere. It cannot survive outside the block without the suite failing on the forbidden phrase (L-5).
- **A6 — the redline texts against canon.**
  - F01 matches D27.
  - F02 matches D27 (canon note in L-12).
  - F04 matches the contract's IA-40 outputs, which are identical in both releases.
  - F05 matches PF06 §0.1A and PF27. The addendum's required `return_phase` field predates this change; set against PF06's "no routing instructions", that is an old tension, not introduced here.
  - F07 matches PF10 2.1 rules 1 to 5 and PF04 §9.1.3. Readings go only into the artifact, the lines before the block name them, the pick is recorded only when Nathan states it, and the reading is never a gate.
  - F08 matches the contract: ESC-40's result states and the remediation identity were already present in 091426.1. Emitting an addendum only for a material delta against an approved base is consistent with `immutable_base` being a required field.
  - MB-003: the banner is present and no model advice remains in the reference.
  - SR-F07-1's "run" is as approved. The suite and the profile require that exact phrase.
  - The retired text that survives elsewhere is R-1, R-2 and L-1.
- **A7 — are the docs accurate to the code?** D-FV-2 to D-FV-7 and D-FV-9 are accurate. D-FV-1 states the "on `main`" claim before it is true (L-7). D-FV-8 overstates "its own release's profile" (L-6). D-GG-1 overstates what is derived and undercounts (L-10).
- **A8 — fit with the 100926.1 candidate.**
  - Members: the contract has 55, the graph has 55 nodes and 235 edges, and the validator's expected-member set matches both.
  - Parents: every lane parent equals `EXPECTED_PARENT_BY_LANE`. The MGMT-10 successor's id, URL and parent equal `x1-successor.json`.
  - Roles: QA-100's receiving role states D27. MGMT-10 has four terminal results, one edge to `NATHAN_TERMINAL_RETURN`, and `GCFPE_MODIFICATION_RECORD` as its output. Its `predecessor_union_destinations` is the 091426.1 manager's history, which the field name says.
  - The only role misfit is L-1. Bodies are X12's to check.
- **Q1 — is anything in the packages false between their build and X16?**
  - Before X16: the contract's `status`, `selection_status`, `selection_claim` and `publication_evidence` say selected, and change-flow says 091426.1 is superseded. None of this is consumed before the X17 install. Receipts written before X16, at X12 and X13, nonetheless label runs `SELECTED_PRODUCTION`.
  - After X16: one claim stays false. `REPOSITORY_FILE_ON_MAIN` is false until X22 (L-7).
- **Q2 — should the 091426.1 change-flow check be marked as history in its own text?** Yes. Neither change-flow's `SKILL.md` nor the script says that `scripts/validate_gcfpe_20260914.py` is history. Run on the installed tree it prints a bare `FAIL: specialization revision`. The only marking is a code comment in flowmaster-validate's `REQUIRED_SCRIPTS`. The cheapest fix is to add it to change-flow's paragraph listing the superseded 091426.1 records.

## What I ran

I worked in `/tmp/d24a` with `PYTHONDONTWRITEBYTECODE=1`. I read every tool's top-level flag by name.

- **§8 a — the archives.**
  - Sizes, sha256 and entry counts match §1. No entry falls outside its skill root, and there are no traversal sequences, directory entries, duplicate names or symlinks.
  - `name:` is unchanged in all six frontmatters.
  - The baseline freeze digests match §3, measured both on copies and on the synced directory read-only.
  - The extracted freeze digests match §1.
  - `quick_validate` reports "Skill is valid!" for all six.
- **§8 b — gates from the extracted root**, which holds the six packages plus the seven siblings of L3:
  - `validate_flowmaster.py --skills-root`: `FLOWMASTER_SUITE_PASS`, `suite_ok: true`, 0 findings, `self_identity: OK`.
    - The current overlay is profile `GCFPE-20261009.1-100926.1-VALIDATION`, `ok: true`, contract `cd291f17…`, graph `43f84f29…`, 55 nodes and 235 edges.
    - Current fixtures: `fixture_suite_ok: true`, 54/54, 55/55 variants, 283 cases, 13 dependency cases passing.
    - Change contract: `rows_exact: true` and `interfaces_closed: true`.
  - The same suite with the explicit 100926.1 contract and candidate root: `FLOWMASTER_SUITE_PASS`.
  - `validate_gcfpe_20261009.py` (flowmaster-validate): `ok: true`, `errors: []`.
  - `run_gcfpe_20261009_fixtures.py`: `fixture_suite_ok: true`.
  - `run_change_flow_fixtures.py`: 34/34, `fixture_suite_ok: true`.
  - change-flow `validate_gcfpe_20261009.py`: `PASS`. Its 091426.1 sibling: `FAIL: specialization revision`, by design.
  - `validate_glow_hde_pr_development.py`: `PASS`.
  - Audit `run_fixture_suite.py`: 37 tests, `OK`.
  - `validate_relay_manifest.py --self-test`: `status: PASS`.
  - **Regenerator:** the shipped 091426.1 contract comes out `EQUAL` on both installed copies (`dbae180b…`, 613,326 B). The candidate build (593,625 B, `a58666e5…`) gives a contract byte-equal to `execute/contracts` (`90593603…`). The production build (593,569 B, `43f84f29…`) gives a contract byte-equal to `cd291f17…`.
  - **Reproduction:** `package_build.py … --check` gives `equal: true` over 95 files. The graph argument was the embedded JSON of my production build plus its final newline, which is byte-identical to both bundled graphs.
- **§8 c — the file list.** `diff -rq` from installed to extracted gives exactly the 25 listed files and nothing else. `package_apply.py --check` on the extracted trees shows 46 of 46 `LANDED`.
- **§8 d — counts and attribution.**
  - The profile's contract, graph and fixture pins match the bundled files.
  - Fixtures: 54 (31 positive, 23 negative); the required ids equal the scenario order.
  - The negative-rule attribution equals the runner's `EXPECTED_NEGATIVE_RULES` and covers exactly the 23 negatives.
  - `EXPECTED_PARENT_BY_LANE` equals the contract's staged parents. The contract has 55 members; the graph has 55 nodes and 235 edges.
- **§8 e — all 21 pin checks agree with their artifacts:**
  - flowmaster-validate's frozen-graph sha and bytes, candidate-contract sha and bytes, fixture sha, routing surface and rows, and the governing-plan literal;
  - change-flow's graph sha, plan sha and bytes, predecessor sha, and routing surface and rows;
  - the contract's own plan, graph and predecessor pins;
  - the profile JSON;
  - `SKILL_TREE_SHA256` = `429eda21…`, recomputed with the validator's own `skill_tree_digest`.
- **§8 f — revision sites.**
  - Every live site is 3.4.0, 1.4.0, 3.3.0 or 1.14.0. Old values remain only in the 091426.1 history files, the immutable R1 oracle's `2.0.0` anchor (mapped) and historical narrative.
  - None of the new values appears anywhere else in the repository, so none has been used before.
  - glow-graph-contract has no revision value to move.
- **Beyond the brief:**
  - broad-match searches for leftover wording (F02, F04, F05, F07 and F08 terms) over all six trees;
  - rule probes and invariant mutations on `project_behavior`;
  - the suite with the explicit 091426.1 contract (loud failure on the history path) and with the explicit 091326.2 alias (runs the 100926.1 profile; loud failure);
  - the suite and change-flow's validator on change-flow text with the retired token inside the prohibition block.
- **Could not run, or did not run:**
  - No body-level check. Under L1 and D22, no prompt body was read, copied or hashed.
  - No live Notion state.
  - I did not run the author's `x8_gates.py`. I reran its gates myself instead.
- **Disclosure:** one of my probe runs used `python3 -I`, which ignores `PYTHONDONTWRITEBYTECODE`, and it wrote a `__pycache__` into my scratch extraction of flowmaster-validate. I deleted it and re-measured: all six extracted freeze digests are unchanged, and `SKILL_TREE_SHA256` verifies.
- **Repository writes:** nothing outside this record. I made no commit and no push.

**Freeze.** Nothing moved during the review.

- At the end, all 13 installed skills measure the same digests, including the seven siblings, for example `glow-merged-change-attribution-lock 10 c518ccb0…`.
- The six source archives in the scratchpad still hash to §1.
- No skill was installed.

**Canon relied on:**
- `AGENTS.md`.
- PF10-HDE-Build-Notes v13.5.2, read in full on `main` `9312add`: precedence rules 1 to 9 and addendum 2.1.
- PF04-Canon-HDE-Governance v2.8.7: §9.1.1 (the authority table), §9.1.2, §9.1.3, §9.1.4 and §9.1.6, read in full.
- PF06-Canon-Change-Process-Guide v2.5.4: §0.1A, read in full, and the in-flight normalization paragraph at its QA-execution executor list.
- PF27-Canon-Plan-Templates v2.0.5: *Canon precedence for template use*, read in full.
- PF19-Canon-Glow-QA-Guide v3.0.6: the post-READY_FOR_QA paragraphs on executors and Kronos evidence review (search hits read in context; no complete-document read claimed).
- In-flight and controls: `MODIFICATION-20261011-gcfpe-mb008-to-promotion` (frontmatter, §A.1 to §A.12, §P, §E and EXECUTE deviations, at HEAD); `PLAN-20261011.md` (complete); `scope-measurement.md` §1 and §2a; `plan/package-redlines.json`; `plan/package_apply.py`; `plan/release-values-100926.1.json`; `execute/package_build.py` (complete); `execute/contracts/release-values-100926.1.filled.json`; `execute/x9-gates-extracted.json`.
- `gcfpe.decision-record.md` D22, D23, D24, D26 and D27; `skill-packaging-and-delivery.md`; `skill-identity-and-freeze.md`; `freeze.py`.

NOTHING NEEDED from Nathan yet. Under D24 condition 5 and D26-A rule 2, the author repairs R-1 and R-2 (L-1 can ride in the same rebuild), and fresh reviewers review the new bytes. If the author judges these audit lines outside the approved plan's redline set, the question goes back to Nathan as a decision.

NOTHING NEEDED
