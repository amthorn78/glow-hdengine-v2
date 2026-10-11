# PLAN verification specification — 2026-10-11

This distinguishes available commands from gates still awaiting their approved sources or implementation. It does not certify proposed repaired bytes. `plan-dry-run.json` contains actual receipts for available baseline commands. Source observations are in `plan-source-checks.json`. A blocked gate is not passed, waived or replaced by prose review.

All shell examples run from the repository root with `PYTHONDONTWRITEBYTECODE=1`. `INPUTS` below is `/workspace/scratch/fa82d6934864/skill-review-inputs`; `EVIDENCE` is `docs/ephemeral/modifications/evidence/20261010-gcfpe-candidate-skill-analysis`; `CANDIDATE_PARTS` is `docs/ephemeral/modifications/evidence/20261009-gcfpe-latest-alpha-analysis/execute/candidate-graph-parts`. These are source bindings, not placeholder authorization to select another tree. Final extracted package commands must point to the reviewed extraction, not these unchanged baseline inputs.

## Verification map

| ID | Gate / actual command or interface | Required interpretation |
|---|---|---|
| V01 | `python -B docs/prompt_ecosystem_management/modification_validate.py docs/ephemeral/modifications/MODIFICATION-20261010-gcfpe-candidate-skill-analysis.md`; `git diff --check` | Current document structure and approval fields. These checks do not approve a mode. |
| V02 | `git diff --name-only ff1f62e23597637c59f573cfd6e7e846d76cec2d`; review every diff against E0–E8 and frozen findings | Only this Modification's plan/evidence changes now. Future repairs cannot change PF canon, selection, historical evidence or listed optional scope. |
| V03 | Native Notion fetch by the recorded page IDs; inspect complete returned content and last-edited metadata | Read-only now. Before future writes, resolve changed revisions and unique anchors; read back the complete changed page. This is connector evidence, not body hashing. |
| V04 | `python -B docs/prompt_ecosystem_management/freeze.py "$INPUTS/change-flow"`, repeated per supplied skill; compare to source-identities.md | Baselines must reproduce. For future packages compare extracted and installed per-skill digests against the exact independent verdict. A printed digest alone is not a check. |
| V05 | **BLOCKED:** source-owned `python3 scripts/graph_parts.py build <candidate-parts> <scratch-graph.md>`; registry derivation command is not yet available | The build interface is documented in authoritative-surfaces.md, but its script is missing. Do not invent the derivation CLI. Recover it and record literal commands in the dated PLAN successor. Derived graph stays scratch; derived registry remains candidate-scoped. |
| V06 | Existing `python -B "$INPUTS/change-flow/scripts/validate_gcfpe_20260914.py"`; future active-contract repair fixtures for T02/T04/T05/T07 | Baseline static PASS is September-contract coverage only. New fixture implementation and exact commands are pending, not a current gate pass. |
| V07 | Native F03 checks plus candidate `CF-C-30.json`, `CF-E-30.json`, `IA-30.json`; current `closure.py --help` defines supported flags | Require one nonterminal dynamic handoff for qualifying approval, real-source failures terminal. Existing graph flags are already correct; T03 must catch a restored terminal body clause. |
| V08 | Native IA-30/IA-40 + PE/change-flow comparison; T04 positive and injected base-rewrite/QA80 cases | Separate approved base from pending delta. The PLAN successor must bind the implemented repair guard command before it can claim mechanical completeness. |
| V09 | Current profile command: `python -B "$INPUTS/flowmaster-validate/scripts/validate_gcfpe_20260914.py" "$INPUTS/change-flow" --contract "$INPUTS/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"` | Read `prompt_bodies_validated` and `prompt_body_checks_not_evaluated`, not just `ok`. Zero bodies is no native-body pass. Current repair expectations and T05 guards must be added before repaired-package qualification. |
| V10 | `python -B "$INPUTS/glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py"`; future T05 exception/regression cases | Structural baseline PASS does not certify new numbering or candidate continuity. Preserve unrelated portability and current phase gates. |
| V11 | Broad match minus interpreted exceptions on each affected native body and active skill text; T09 routing/absence tests on repaired graph and derived registry | Match numbering/allocation, terminal/continuation, preapproval/delta, executor and advice language, including templates/examples. Exact phrase guards cannot prove semantic absence; a reviewer must assess surviving old behavior. New command bindings pending. |
| V12 | `python -B "$INPUTS/flowmaster-validate/scripts/validate_flowmaster.py" --skills-root "$INPUTS" --strict-warnings`; historical fixture commands in checks.md | Missing companions are a suite failure. Reuse the already-passed unchanged historical fixtures during planning; rerun affected suites from final extracted bytes during execution. Do not retrofit historical R1 scenarios into current candidate certification. |
| V13 | **BLOCKED:** governed quick-validation, packaging, clean extraction, two D24 reviews and final install-digest comparison | Current quick_validate.py alone does not supply the repository's missing package_skill/SendUserFile route. Read/pin the approved supported mechanism, bind commands and delivery evidence, then review final bytes. No automatic install or Git save that evades Nathan's boundary. |
| V14 | Connected GitHub file fetches at the published commit plus git fetch/tree comparison; native Notion readback of catalog/Alpha updates | Read full published changed files. Confirm actual PR state and selected release; do not infer success from an attempted write. Nathan merges; do not infer a merge from its subject. |

Existing committed verification commands are quoted exactly. The explicitly pending guard and tool command bindings are a reason the PLAN is **not complete**. They are not executable pseudo-commands or deferred interpretation disguised as an approved normal path.

## Required behavior and injected-regression cases

These are specifications for E4, not test results. Each negative must fail the appropriate active repair guard and the clean/exception control must pass. Historical fixture behavior remains its own baseline. Store resulting receipts, counts, top-level flags, exact source coverage and final script paths in execution evidence.

| Case | Positive / preserved exception | Injected regression that must fail |
|---|---|---|
| T02a | PO chooses Kronos as executor; independent QA acceptance preserved | Require a different or named executor despite otherwise valid authority |
| T02b | Executor identity absent; exact task/target/actions/evidence and valid PO arrangement present | Reject solely for missing session, platform or DevOps venue |
| T02c | QA task authored but not run remains NOT_EXECUTED; all QA-100 states return to QA-110 | Treat preparation as execution or redirect a valid return away from QA-110 |
| T03a | Each of three qualifying delta approvals saves/reuses one addendum and emits one exact native handoff | Terminal DELTA_APPROVE, zero/two handoffs, generic/unresolved receiver or forced RS-40 |
| T03b | Missing required source/authority ends terminally with exact recovery owner | Guess receiver, run/create a receiving session, or introduce paste/presence verification |
| T04a | PLAN_DELTA_REDLINE enters IA-40 with immutable approved base and no pending delta; separate delta returns to IA-30 | Demand a nonexistent pending delta at first authoring or reject IA-40 categorically |
| T04b | DELTA_DENY revises the separate pending delta only | Replace approved base, self-approve, create addendum before approval, or copy this route to QA-80 |
| T04c | PR rescope and ESC remediation retain actual native owners | Route them through IA-40 as generic Plan-delta authoring |
| T05a | All six producers create exactly one next-continuous-numbered H2/descriptive title; H3+ children; substantive subject matter | Unnumbered/duplicate/gapped heading, H1 or sibling H2 child, role-addressed handling text replacing the substance |
| T05b | Current PF10 supplies creation-time numbering; Nathan alone inserts into PF10 | Require PO to supply the number, let producer edit PF10, or verify a later paste/presence/wording |
| T05c | Same valid approval reuses matching read-back addendum; initial/denied/revision/pending/editorial/in-scope outcomes emit none | Duplicate repeated approval, addendum for a nonqualifying outcome, or seventh producer |
| T05d | Canon destination and permanent-canon owner remain valid subject matter | Token-only `drain` rejection of a legitimate permanent-canon destination |
| T07a | Plain task-specific human surface/model/reasoning advice, outside runnable handoff | Blanket ban on that advice or mandatory score/Analyzer/configuration prerequisite |
| T07b | Tool/source/authority gap uses native recovery; no capability claim without evidence | Automatic switch/launch, provider mandate or TypeSafe API call |
| T09a | APPROVE/REJECT/IN_SCOPE_REPAIR before Proceed each returns to actual PR-20 planning origin; only APPROVE creates addendum | Missing PR-20 edge, dynamic branch restricted to non-PR, or substitution of PR-30_PREPUBLICATION |
| T09b | All three pre-Proceed cases omit future vehicle, Proceed and execution-phase fields | Require or invent any of those fields; add fourth execution-phase enum |
| T09c | Existing execution and lawful non-PR routes remain unchanged; independent IA reviews | Reuse PR-20 branch for executed PRs, erase original authority, or permit author self-review |

## Readback and rollback tests

Before writing, fetch current target and confirm intended revision/anchor. After each native edit, inspect the full returned page and the named behavior; repeated uncertain writes first inspect the page, never resend blind. Repository and package mutations must have a derived changed-file inventory and exact final identities. Readback failure after an external repair write invokes D26-B, not an improvised rollback script. No full prompt body backup is required or permitted.

For Notion restoration, Nathan selects the recorded pre-write page-history revision; the session then reads the restored page and confirms the relevant behavior and metadata. For repository changes, Nathan can preserve a failure record and separately merge the bounded revert. The session cannot guarantee a record reached main until those files are present there.
