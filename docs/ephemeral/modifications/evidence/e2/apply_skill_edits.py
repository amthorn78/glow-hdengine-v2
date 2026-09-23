"""E2 step 5 (spec v2 §8a, §8b, §5.8, §5.10): skill text, validator reversals, new checks, fixtures,
revision bumps. Scratch copy only. Pins (profile, byte pins, R1 digests, fixture pins, SKILL_TREE_SHA256)
are written afterwards by pin_e2.py, in §5.11 order.

usage: PYTHONDONTWRITEBYTECODE=1 python3 apply_skill_edits.py <skills-root>

Every edit is an exact substring replacement that must match exactly once (spec §8a.0/§8b.0).
Base edit lists are the v2 workers' tested scripts (evidence/v2-work: apply_skills.py b6683e6c...,
apply_8b.py 6988671a..., patch_fv.py 5d037231..., patch_fix_v2.py via section8b9_runner_scenarios.patch),
with the §12 addendum applied (U-6 order at relay :255; U-8b-9 comment) and the §5 R1 sites added.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from texts import SPEC, T, x  # noqa: E402

root = Path(sys.argv[1])
LOG = []


def apply(rel, edits):
    p = root / rel
    s = p.read_text(encoding="utf-8")
    for i, (old, new) in enumerate(edits):
        old, new = x(old), x(new)
        n = s.count(old)
        assert n == 1, (rel, i, n, old[:160])
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")
    LOG.append((rel, len(edits)))
    return s


LANDED, FB = T["LANDED"], T["FALLBACK"]

# ============================== §8a glow-hde-pr-development ==============================
apply("glow-hde-pr-development/SKILL.md", [
    ("Glow HDE PR work unit in its single dedicated development session across", "Glow HDE PR work unit, run in two dedicated sessions, across"),
    ("`GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5`", "`GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0`"),
    ("Keep the existing GCFPE actor, one dedicated PR-development session, one original Product Owner Proceed, scope, and manual-merge boundaries intact.",
     "Keep the existing GCFPE actor, one Proceed per approved per-PR plan, scope, and manual-merge boundaries intact."),
    ("detailed PR implementation Plan covered by the original Proceed, with", "detailed PR implementation Plan covered by the Proceed, with"),
    ("the complete `PR_CANDIDATE_PUBLISHED` result and same-session PR-35 handoff;", "the complete `PR_CANDIDATE_PUBLISHED` result and PR-35 handoff;"),
    (", the PR-35 handoff; in either case require the exact workspace/worktree, branch, open PR and remote-head lineage;", ", the PR-35 handoff;"),
    ("coherent initial publication followed in the same session by PR-35 review remediation", "coherent initial publication followed by PR-35 review remediation"),
    ("only for its explicit scope; continuation preserves the original Proceed and never requires or creates a second Proceed.", "only for its explicit scope. {C-PROCEED}"),
    ("3. Match prior work using evidence such as", "3. Match prior work of the current plan cycle using evidence such as"),
    ("Reconcile partial or ambiguous external effects before retrying them.", "Reconcile partial or ambiguous external effects before retrying them. {LANDED}"),
    ("Remain in the one dedicated PR-development session across both phases.", "{C-SESSION}"),
    ("followed by exactly one complete same-session `PR-35` handoff.", "followed by exactly one complete `PR-35` handoff to the dedicated PR-35 session."),
    ("The phase boundary adds no actor, session, work unit,", "The phase boundary adds no actor, work unit,"),
    ("Proceed, R1 row, or authority transfer.", "Proceed, R1 row, authority transfer, or any session beyond its own dedicated PR-35 session."),
    ("{TEN}.", "{NINE}."),
    ("The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`,", "The PR-35 result vocabulary is exactly `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,"),
    ("route a substantiated material boundary through the existing rescope path.", "route a substantiated material change (as defined below) through the existing rescope path."),
    ("Reuse an existing PR for the same branch/work unit instead of creating another.", "Reuse an existing PR for the same branch/work unit in the current plan cycle instead of creating another. {LANDED}"),
    ("- Bundle related implementation or review corrections into one locally verified push when practical.", "- Bundle related implementation changes into one locally verified push when practical."),
    ("that invokes the exact selected PR-35 in this same dedicated session with all repository, worktree, branch, PR, remote-head, artifact, test, constraint, unresolved-item, and original-Proceed lineage.",
     "that invokes the exact selected PR-35 in the dedicated PR-35 session."),
    ("or create another PR/session/Proceed.", "or create another PR/session/Proceed; one branch and one pull request per plan cycle."),
    ("Continue in the same dedicated PR session until all applicable predicates are true:", "Continue in this phase's own dedicated session until all applicable predicates are true:"),
    ("- the complete PR implementation result and handoff artifacts are saved and read back.",
     "- the complete PR implementation result (`PR_IMPLEMENTATION_RESULT`) and handoff artifacts are saved and read back; `PR_IMPLEMENTATION_RESULT` includes:\n  - {C-DEC}"),
    ("or keep polling for that manual action.\n", "or keep polling for that manual action. {C-DISPATCH}\n"),
    ("\nUse `REMOTE_EVIDENCE_PENDING` only in PR-35 when", "\n{C-SUB}\n\nUse `REMOTE_EVIDENCE_PENDING` only in PR-35 when"),
    ("- poll only when a pending remote result can change the next action;", "- where no subscription delivers it, poll only when a pending remote result can change the next action;"),
    ("## Route a real material boundary\n\nWhen repository evidence proves that the approved work unit cannot be completed without changing approved scope, architecture, requirements, or Plan authority:",
     "## Route a real material boundary\n\n{C-LAT}\n\nWhen repository evidence proves a material change, as defined above:"),
    ("repository/workspace/worktree/branch state, open PR and remote head only when they actually exist, ", ""),
    ("Resume the recorded phase in the same dedicated PR session, workspace/worktree, branch, open PR,", "Resume the recorded phase in the recorded phase's own dedicated session, workspace/worktree, branch, open PR,"),
    ("The work unit keeps exactly one branch and one pull request, which the ten-field continuity list requires;", "The work unit keeps exactly one branch and one pull request per plan cycle, which the nine-field continuity list requires;"),
    ("for artifacts. The Product Owner merges.\n\n", "for artifacts. The Product Owner merges.\n\n{C-ART}\n\n"),
    ("It must instruct the receiver to run the exact selected Notion prompt by full name, version, and direct Notion URL; identify the receiving role and exact continuing/dedicated session; identify the change/Epic and work unit; supply every required repository path and repository/PR reference; state current status, completed work, decisions, constraints, unresolved items, and preserved authority; and state the next required action and expected output.", "{C-HANDOFF}"),
    ("or unrecoverable work.\n", "or unrecoverable work. {C-PLACE}\n"),
    ("At PR-30 `PR_CANDIDATE_PUBLISHED`, return the exact same-session PR-35 continuation.", "At PR-30 `PR_CANDIDATE_PUBLISHED`, return the exact PR-35 continuation."),
    ("to use it only after Nathan has manually merged the identified PR;", "to use it only after Nathan has manually merged the identified PR and {FALLBACK};"),
    ("- Do not create hidden sessions or extra approval stages.", "- Do not create sessions or extra approval stages."),
])
REPLAN_CASE = ("\n## PR-40 rejection re-plan\n\n"
    "Given a PR-40 `REJECT` (`reject_replan`) for this `WORK_UNIT_ID`, whose pull request merged under the earlier plan cycle, "
    "PR-20 plans that work unit again in a new top-level session that Nathan creates, and the new plan receives its own Proceed. "
    "PR-30 starts only from the Proceed of its own plan. " + LANDED + " "
    "PR-30 creates a new branch and a new pull request for the new plan. "
    "The earlier Proceed is spent and is never reused.\n")
O16_CASES = ("\n## In-flight decisions\n\n"
    "Given a decision that is not material and is obvious, necessary to deliver the approved scope, and consistent with the Epic's objective and controlling constraints, PR-30 or PR-35 decides it, implements it, tests it, and records it under *In-flight decisions* in `PR_IMPLEMENTATION_RESULT`: what changed, why it was necessary to deliver the approved scope, and what was tested, by test identity and outcome. That holds even if the plan did not anticipate it; `NONE` is recorded when there were none.\n"
    "\n## Implementor latitude\n\n"
    "Given a planned approach found incomplete, impractical or inferior, that alone is not material. A change to the Epic-level commitment — its outcome or objective; approved acceptance criteria; a protected architectural, security, data-model or external-contract boundary; the scope of several planned work units; an accepted dependency or cross-team commitment; or budget, schedule or risk needing Product Owner direction — takes the formal rescope route. Anything that is neither material nor obvious and necessary is not done; it is recorded as a candidate for its owner.\n"
    "\n## Pull request subscription\n\n"
    "Given PR-35 entry, subscribe to the pull request's activity where the surface provides it, and record the subscription as active only when the tool result confirms that this session receives the pull request's events. Act on review, comment and check events as they arrive. Without an active subscription, `REMOTE_EVIDENCE_PENDING` and its re-entry handoff apply as before. The subscription creates no session.\n"
    "\n## Observed merge\n\n"
    "Given `MERGE_PENDING` returned with the conditional PR-40 block and an active subscription, when the subscription delivers the merge of the identified PR — a merge Nathan performs — PR-35 returns `MERGE_OBSERVED` with the paste-ready PR-40 handoff and returns control. Nathan creates the PR-40 session and pastes it; PR-40 still verifies the merged state and landed lineage independently. The conditional PR-40 block stays usable only after Nathan merges and " + FB + ". No agent merges or creates a session.\n")
# Cross-check the five appended cases against the spec's own §8a.2 insert block.
_ins = SPEC[SPEC.index("insert:\n\n## PR-40 rejection re-plan") + len("insert:\n"):]
_ins = x(_ins[:_ins.index("\n```")]) + "\n"
assert _ins == REPLAN_CASE + O16_CASES, "8a.2 insert block differs from the compiled cases"
apply("glow-hde-pr-development/references/behavior-cases.md", [
    ("with exactly one complete same-session PR-35 handoff.", "with exactly one complete PR-35 handoff."),
    ("The phase split creates no new role, session, Proceed,", "The phase split creates no new role, Proceed,"),
    ("R1 row, work unit, or PR.", "R1 row, work unit, PR, or any session beyond its own dedicated PR-35 session."),
    ("invokes the exact selected PR-35 in the same dedicated PR-development session with complete lineage.", "invokes the exact selected PR-35 in the dedicated PR-35 session."),
    ("The shared phase identity preserves the exact ordered ten-field GCF-17 continuity list: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree;",
     "The shared phase identity preserves the exact ordered nine-field GCF-17 continuity list: `WORK_UNIT_ID`; original Product Owner Proceed; workspace/worktree;"),
    ("Given the complete same-session PR-35 handoff,", "Given the complete PR-35 handoff,"),
    ("PR-35 returns only `MERGE_PENDING`, `RESCOPE_PENDING`,", "PR-35 returns only `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,"),
    ("Given evidence that implementation requires an approved-boundary change,", "Given evidence that implementation requires a material change to the Epic-level commitment,"),
    ("resume the recorded phase in the same PR session, workspace/worktree, branch, open PR and original Proceed.", "resume the recorded phase in the recorded phase's own dedicated session, workspace/worktree, branch, open PR and original Proceed."),
    ("The conditional prompt separately requires", "The conditional prompt, usable {FALLBACK}, separately requires"),
])
_bc = root / "glow-hde-pr-development/references/behavior-cases.md"
_t = _bc.read_text(encoding="utf-8")
assert _t.endswith("\n") and not _t.endswith("\n\n")
_bc.write_text(_t + REPLAN_CASE + O16_CASES, encoding="utf-8")
apply("glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py", [
    ('"GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5"', '"GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0"'),
    ('"single session": "one dedicated PR-development session",', '"single session": "run in two dedicated sessions",'),
    ('"PR-35 complete result vocabulary": "{V5}",', '"PR-35 complete result vocabulary": "{V6}",'),
    ('"PR-30 to PR-35": "same-session `PR-35` handoff",', '"PR-30 to PR-35": "exactly one complete `PR-35` handoff to the dedicated PR-35 session",'),
    ('"merge-ready ownership": "Continue in the same dedicated PR session until all applicable predicates are true",', '"merge-ready ownership": "Continue in this phase\'s own dedicated session until all applicable predicates are true",'),
    ('"exact GCF-17 continuity list": "{TEN}",', '"exact GCF-17 continuity list": "{NINE}",'),
    ('"same PR continuation": "same dedicated PR session, workspace/worktree, branch, open PR",', '"same PR continuation": "the recorded phase\'s own dedicated session, workspace/worktree, branch, open PR",'),
    ('        "specification change terminal":',
     '        "artifact holds results": "never carries the only copy",\n'
     '        "in-flight decisions": "An *In-flight decisions* section",\n'
     '        "material latitude": "Decide it during work",\n'
     '        "one Proceed per plan": "One Proceed per approved per-PR plan",\n'
     '        "top-level PR-35 session": "never as a subagent, forked agent or workflow agent of PR-30",\n'
     '        "subscription is not polling": "Subscribing is not polling",\n'
     '        "no agent-created session": "no session is created by an agent",\n'
     '        "handoff carries no branch": "It carries no branch and no commit",\n'
     '        "specification change terminal":'),
    ('        "[TODO",\n    ]',
     '        "[TODO",\n'
     '        "one dedicated PR-development session",\n'
     '        "same-session `PR-35` handoff",\n'
     '        "{V5}",\n'
     '        "Continue in the same dedicated PR session until all applicable predicates are true",\n'
     '        "{TEN}",\n'
     '        "same dedicated PR session, workspace/worktree, branch, open PR",\n'
     '        "followed in the same session by PR-35",\n'
     '        "`MERGE_PENDING`, `RESCOPE_PENDING`",\n'
     '        "ten-field",\n'
     '    ]'),
    ('        "## Not ready",\n    ]',
     '        "## Not ready",\n        "## PR-40 rejection re-plan",\n        "## In-flight decisions",\n        "## Implementor latitude",\n        "## Pull request subscription",\n        "## Observed merge",\n    ]'),
])

# ============================== §8a amthor-workspace-governance-audit ==============================
AM = "amthor-workspace-governance-audit/"
apply(AM + "SKILL.md", [
    ("**WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3", "**WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.12.0"),
    ("After authorized selection, verify each predecessor prompt moved intact", "After authorized selection, verify each predecessor prompt of a member that received a successor page moved intact"),
    ("It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the receiving role/session and work identifiers; carries every already-existing required artifact by exact identity/version and its repository path, or its direct Notion URL for a Notion-resident artifact; carries status, decisions, constraints, unresolved items, next action, and expected output; and contains no blanks, menus, or alternative destinations. Terminal results identify completion and the native Product Owner return.\n",
     "{C-HANDOFF} Terminal results identify completion and the native Product Owner return.\n"
     "- Every body whose registry row requires `NEXT_PROMPT_HANDOFF` carries, as the first sentence of its output section: {C-ART}\n"
     "- Every body whose registry row requires `NEXT_PROMPT_HANDOFF` carries, after its handoff rule: {C-PLACE}\n"),
    ("- GCFPE PR-30, same-session PR-35, interrupted PR recovery,", "- GCFPE PR-30, PR-35 in its own dedicated session, interrupted PR recovery,"),
    ("Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.\n- The exact ordered",
     "Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or any session beyond its own dedicated PR-35 session.\n- The exact ordered"),
    ("- {TEN}. Require PR-30", "- {NINE}. Require PR-30"),
    ("or unsupported platform limitation. PR-30 owns", "or unsupported platform limitation. {LANDED} PR-30 owns"),
    ("ends with `PR_CANDIDATE_PUBLISHED` plus one complete same-session PR-35 handoff.", "ends with `PR_CANDIDATE_PUBLISHED` plus one complete PR-35 handoff."),
    ("- One Product Owner `Proceed` authorizes the single PR-30/PR-35 work unit through genuine merge readiness, not merge.",
     "- One Product Owner `Proceed` per plan cycle authorizes the PR-30/PR-35 work unit through genuine merge readiness, not merge. " + T["C-PROCEED"].split(". ", 1)[1]),
    ("phase in the same session/workspace/worktree/branch/open PR/original Proceed.", "phase in the recorded phase's own session/workspace/worktree/branch/open PR/original Proceed."),
    ("- PR-35's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later invocation asserts only that Nathan manually merged the identified PR;",
     "- PR-35's `MERGE_PENDING` is historical pre-merge evidence. {C-DISPATCH} Nathan's later invocation, usable {FALLBACK}, asserts only that Nathan manually merged the identified PR;"),
    ("Never treat `MERGE_PENDING` as a current post-merge fact.\n", "Never treat `MERGE_PENDING` as a current post-merge fact.\n- {INVARIANT}\n"),
])
apply(AM + "references/interoperability-contracts.md", [
    ("implementation/publication, same-session PR-35 review/readiness,", "implementation/publication, PR-35 review/readiness,"),
    ("one selected PR-30 → PR-35 same-session phase continuation inside existing R1 row GCF-17; it adds no role, approval, authority transfer, Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.",
     "one selected PR-30 → PR-35 phase continuation inside existing R1 row GCF-17; it adds no role, approval, authority transfer, Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or any session beyond its own dedicated PR-35 session."),
    ("- The handoff begins with the exact selected destination prompt name, version, and direct Notion URL and carries the actual receiving role/session, work identifiers, every already-existing required artifact by exact identity/version and its repository path or its direct Notion URL for a Notion-resident artifact, state, decisions, constraints, unresolved items, next action, and expected output.", "- {C-HANDOFF}"),
    ("plus exactly one complete same-session PR-35 handoff.", "plus exactly one complete PR-35 handoff."),
    ("{TEN}.", "{NINE}."),
    ("PR-35's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later invocation asserts only a manual merge;",
     "PR-35's `MERGE_PENDING` is historical pre-merge evidence. {C-DISPATCH} Nathan's later invocation, usable {FALLBACK}, asserts only a manual merge;"),
    ("PR-30/PR-35 same-session skill/recovery", "PR-30/PR-35 skill/recovery"),
])
apply(AM + "references/behavioral-fixtures.md", [
    ("{TEN}.", "{NINE}."),
    ("with one complete same-session PR-35 handoff.", "with one complete PR-35 handoff."),
    ("separately require Nathan's later manual-merge assertion and PR-40's", "separately require Nathan's later manual-merge assertion, usable {FALLBACK}, and PR-40's"),
    ("- Require exact rescope return phase",
     "- Accept PR-40 entry on `MERGE_OBSERVED` only when the subscribed PR-35 session, or RS-40 resuming the PR-35 phase, observed through an active subscription the merge of the identified PR that Nathan performed, and Nathan pasted the handoff into a session he created; accept Nathan's manual-merge assertion {FALLBACK}. Reject an agent merge, automatic dispatch, an agent-created session, and PR-40 entry before any merge.\n"
     "- Accept a PR-40 `REJECT` for a precise in-scope defect in landed work only as a re-plan through PR-20 in a new top-level session Nathan creates, with a new plan and its own Proceed; a pull request merged under an earlier plan cycle is landed history. Reject that `REJECT` routed to PR-30, a second Proceed for the same plan, and a Proceed between PR-30 and PR-35.\n"
     "- Require exact rescope return phase"),
])
apply(AM + "references/project-prompt-registry-schema.md", [
    ("  session_class: DEDICATED_ONE_OFF | CHANGE_LIFETIME | ROLE_CONTINUING | ORCHESTRATOR_RUN\n",
     "  session_class: DEDICATED_ONE_OFF | CHANGE_LIFETIME | ROLE_CONTINUING | ORCHESTRATOR_RUN | DEDICATED_PR_REVIEW_SESSION\n"),
])
apply(AM + "scripts/run_fixture_suite.py", [
    ('EXACT_GCF17_CONTINUITY = "{TEN}"', 'EXACT_GCF17_CONTINUITY = "{NINE}"\nRETIRED_GCF17_CONTINUITY = "{TEN}"'),
    ('self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3", skill)', 'self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.12.0", skill)'),
    ("        self.assertIn(EXACT_GCF17_CONTINUITY, fixtures)\n",
     "        self.assertIn(EXACT_GCF17_CONTINUITY, fixtures)\n        for text in (skill, interoperability, fixtures):\n            self.assertNotIn(RETIRED_GCF17_CONTINUITY, text)\n"),
])

# ============================== §8b change-flow ==============================
CF_RETIRED = [
    "one dedicated PR-development session", T["TEN"],
    "same-session PR-30 → PR-35 phase continuation", "same-session PR-35 handoff", "same-session PR-35 review/readiness",
    "same-session second phase", T["V5"],
    "historical pre-merge evidence; Nathan's later invocation asserts that Nathan manually merged",
    "A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred",
    "One dedicated session per planned PR work unit; the same session performs both",
    "has only the manual-merge-assertion meaning",
    "The same dedicated PR session implements only that work unit",
    "Only after Nathan later asserts that the identified PR was manually merged may that invocation run",
    "GCF-14 — Create one dedicated PR session for one planned PR work unit",
]
apply("change-flow/SKILL.md", [
    ("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9", "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0"),
    ("R1_CONTRACT_PROFILE: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1", "R1_CONTRACT_PROFILE: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1"),
    ("or manual PF controls.\n\n### Runtime entry gate", "or manual PF controls.\n\n{OVERRIDE}\n\n### Runtime entry gate"),
    ("- The policy for one dedicated PR-development session per planned PR work unit, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, same-session PR-35 review/readiness,",
     "- The policy for each planned PR work unit, run in two dedicated sessions, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, PR-35 review/readiness,"),
    ("evidence destination, and cleanup/recovery owner in the handoff.", "evidence destination, and cleanup/recovery owner in the output artifact that the handoff names."),
    ("a selected PR-35 is lawful only as the same-session second phase of the existing GCF-17 PR work unit.", "a selected PR-35 is lawful only as the second phase of the existing GCF-17 PR work unit."),
    ("It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the actual receiving role/session and change/work identifiers; provides every required artifact repository path; and carries current status, decisions, constraints, unresolved items, next action, and expected output.", "{C-HANDOFF}"),
    ("Terminal results state completion and the native Product Owner return.", "Terminal results state completion and the native Product Owner return. {C-PLACE}"),
    ("PR-30 and PR-35 are two phases of that one work unit and retain one original Proceed, one dedicated PR-development session, one workspace/worktree, one branch, one pull request, one PR instruction and detailed Plan, one primary skill, and continuous recovery/artifact lineage.", "{C-SESSION}"),
    ("exactly one complete same-session PR-35 handoff;", "exactly one complete PR-35 handoff to the dedicated PR-35 session;"),
    ("coherent corrective commits and pushes, CI economy, remote-head proof, and genuine merge readiness.\n", "coherent corrective commits and pushes, CI economy, remote-head proof, and genuine merge readiness. {C-PROCEED}\n"),
    ("{TEN}", "{NINE}"),
    ("same-session continuation cannot add, omit,", "continuation cannot add, omit,"),
    ("{V5}", "{V6}"),
    ("permits this one selected same-session PR-30 → PR-35 phase continuation inside GCF-17. It permits no extra role, approval, authority transfer, Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.",
     "permits this one selected PR-30 → PR-35 phase continuation inside GCF-17. It permits no extra role, approval, authority transfer, Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, or R1 row."),
    ("it uses selected RS-40 to resume the recorded phase in the same session/workspace/worktree/branch/open PR under the original Proceed.",
     "it uses selected RS-40 to resume the recorded phase in that phase's own session, workspace/worktree, branch and open PR under the original Proceed."),
    ("PR-35's `MERGE_PENDING` is historical pre-merge evidence; Nathan's later invocation asserts that Nathan manually merged; PR-40 then independently verifies actual merged state and landed lineage read-only.",
     "PR-35's `MERGE_PENDING` is historical pre-merge evidence; {FALLBACK}, Nathan's later invocation asserts that Nathan manually merged; PR-40 then independently verifies actual merged state and landed lineage read-only. {C-DISPATCH}"),
    ("A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred; it is not a merge approval or merge instruction.",
     "Where the subscribed PR-35 session observed the merge, that event is the fact PR-40 is entered on; {FALLBACK}, Nathan's later PR-40 invocation asserts the manual merge; neither is a merge approval or instruction."),
    ("| Per-PR planning and implementation | One dedicated session per planned PR work unit; the same session performs both |",
     "| Per-PR planning and implementation | PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request. |"),
    ("has only the manual-merge-assertion meaning defined above;", "has only the meaning defined above;"),
    ("- GCF-14 — Create one dedicated PR session for one planned PR work unit.", "- GCF-14 — Nathan creates one dedicated top-level PR session for one planned PR work unit."),
    ("GCF-17 — The same dedicated PR session implements only that work unit across selected PR-30 and PR-35, validates it, and creates exactly one active branch and pull request.",
     "GCF-17 — The dedicated PR session (PR-30 phase) and the dedicated PR-35 session (PR-35 phase) implement only that work unit across selected PR-30 and PR-35, validate it, and create exactly one active branch and pull request. PR-35: its own dedicated top-level session for the same work unit and pull request, entered from PR-30's handoff; never a subagent of another session."),
    ("Only after Nathan later asserts that the identified PR was manually merged may that invocation run.",
     "Only after Nathan has manually merged the identified PR, and {FALLBACK}, may that invocation run; where the subscribed PR-35 session observed the merge, PR-35 returns `MERGE_OBSERVED` with the paste-ready PR-40 handoff."),
    ("This is the single authoritative work-unit acceptance route; an attribution bundle is evidence only.",
     "This is the single authoritative work-unit acceptance route; an attribution bundle is evidence only. A precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed (GCF-14)."),
    # :557 (§5.8; U-8b-4). The digest placeholder is written by pin_e2.py.
    ("load the complete [bundled 46-row runtime map](references/glow-hde-canonical-change-flow-r1-runtime-map.json), SHA-256 `5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e`, as immutable historical baseline evidence. Preserve its original rows and source digests.",
     "load the complete [bundled 46-row runtime map](references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json), SHA-256 `<SUCC_MAP>`, as the current runtime projection of the successor R1 oracle. Preserve its rows and source digests."),
    ("Load [GCFPE current direct-handoff contract](references/gcfpe-current-direct-handoff-contract.json) as the current specialization overlay.",
     "Load [GCFPE current direct-handoff contract](references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json) as the current specialization overlay."),
    ("The older integrated-readiness, final-scan,",
     "The historical 46-row runtime map `glow-hde-canonical-change-flow-r1-runtime-map.json` (SHA-256 `5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e`) remains immutable historical provenance, checked by its historical pins. The older integrated-readiness, final-scan,"),
    ("The bundled `gcfpe-20260913.1-091326.2`, `gcfpe-20260913.1`, and `gcfpe-20260912.2` direct-handoff contracts are superseded candidate records",
     "The bundled `gcfpe-current-direct-handoff-contract.json` alias (091326.2), `gcfpe-20260913.1-091326.2`, `gcfpe-20260913.1`, and `gcfpe-20260912.2` direct-handoff contracts are superseded candidate records"),
    ("Three of these files share `contract_id` `GCFPE-PF10-INTEGRITY-20260913.1` with the current contract above; that identifier resolves for current execution to `gcfpe-current-direct-handoff-contract.json` alone, which carries `status: SELECTED_PRODUCTION`.",
     "Three of these files share `contract_id` `GCFPE-PF10-INTEGRITY-20260913.1`; that identifier no longer names the current overlay. The current overlay is the 091426.1 contract above, `contract_id` `GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED`, which carries `status: SELECTED_PRODUCTION`."),
])
_retired = "    for text in (\n" + "".join("        " + json.dumps(p, ensure_ascii=False) + ",\n" for p in CF_RETIRED) + \
    "    ):\n        require(text.lower() not in skill.lower(), f\"retired skill clause present: {text}\")\n\n"
apply("change-flow/scripts/validate_gcfpe_20260914.py", [
    ('require("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9" in skill, "specialization revision")', 'require("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0" in skill, "specialization revision")'),
    ("        " + json.dumps(T["TEN"]) + ',\n        "one dedicated PR-development session",\n',
     "        " + json.dumps(T["NINE"]) + ',\n        "run in two dedicated sessions",\n        "never as a subagent, forked agent or workflow agent of PR-30",\n        "no session is created by an agent",\n        "One Proceed per approved per-PR plan",\n        "It carries no branch and no commit",\n'),
    ('        require(text in skill, f"missing skill clause: {text}")\n\n', '        require(text in skill, f"missing skill clause: {text}")\n\n' + _retired),
    # contract-side literals (§8b.3)
    ('require(contract["contract_revision"] == "4.0.6", "corrected-source contract revision")', 'require(contract["contract_revision"] == "4.1.0", "corrected-source contract revision")'),
    ('        len(graph["edges"]) == 227\n', '        len(graph["edges"]) == 229\n'),
    ('EXPECTED_ROUTING_SURFACE = "7380cd14430777675f1e8b2cdfa4a0da"\nEXPECTED_ROUTING_SURFACE_ROWS = 282',
     'EXPECTED_ROUTING_SURFACE = "fecc319bdd4ce7ee6201cb77d7231861"\nEXPECTED_ROUTING_SURFACE_ROWS = 284'),
    ('        == ["MERGE_PENDING", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"],\n        "PR-35 results",',
     '        == ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"],\n        "PR-35 results",'),
])
# The new clause block must equal the spec's §8b.3 block (token-expanded).
_s83 = SPEC[SPEC.index("The new block, in place of `:1020`"):]
_s83 = x(_s83[_s83.index("```\n") + 4:_s83.index("\n```")])
assert _s83 in (root / "change-flow/scripts/validate_gcfpe_20260914.py").read_text(encoding="utf-8"), "8b.3 block"

# ============================== §8b session-relay-flowmaster ==============================
rs = apply("session-relay-flowmaster/SKILL.md", [
    ("`SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.0.0`", "`SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0`"),
    # :255, W-9 scoping (U-8b-1), then the override paragraph and W-9's sentence, in the §12 addendum U-6 order.
    ("When a required participant does not exist or cannot be confirmed reachable, return `SESSION_PROVISIONING_REQUIRED` for Session Branch Flowmaster. Do not silently create a replacement.\n\n### Cross-skill contracts and shared state",
     "Outside a GCFPE main-ecosystem stage, when a required participant does not exist or cannot be confirmed reachable, return `SESSION_PROVISIONING_REQUIRED` for Session Branch Flowmaster. Do not silently create a replacement.\n\n{OVERRIDE}\n\n{W9}\n\n### Cross-skill contracts and shared state"),
    ("For every GCFPE reusable prompt and temporary repair/review/handoff prompt,", "For every GCFPE reusable prompt and temporary repair/review prompt,"),
    ("This prompt-locator rule does not ban API URLs, tool parameters or actual identity evidence outside prompt text.\n",
     "This prompt-locator rule does not ban API URLs, tool parameters or actual identity evidence outside prompt text. Runtime handoffs may name versioned files; reusable prompt text stays versionless.\n"),
    ("- Notion is the preferred live control plane for current task, assignment, dependency, decision, and handoff state.", "- {STEP2}."),
    ("cleanup/recovery owner in the existing handoff.", "cleanup/recovery owner in the output artifact that the handoff names."),
    ("Deliver every concrete routed handoff in the final user-facing response itself: target actor and session continuity, exact task-bound advice or limitation, named file references the recipient can resolve itself, and a populated copyable invocation with the selected prompt's native inputs and actual prerequisites. For a Notion prompt use its versionless name and verified directory; approved runtime versions remain input lineage.",
     "Deliver every concrete routed handoff in the final user-facing response itself. {C-HANDOFF} {C-PLACE}"),
    ("PR-30 finishes recovery, implementation, local testing and deliberate initial publication, returns PR_CANDIDATE_PUBLISHED with exactly one complete same-session PR-35 handoff,",
     "{C-SESSION} PR-30 finishes recovery, implementation, local testing and deliberate initial publication, returns PR_CANDIDATE_PUBLISHED with exactly one complete PR-35 handoff to the dedicated PR-35 session,"),
    ("PR-35 supplies the actual populated PR-40 handoff conditional on merge.", "{C-DISPATCH}"),
    ("The Product Owner's PR-40 invocation supplies merge approval without a separate confirmation or approval artifact; it never authorizes an agent merge,",
     "The Product Owner's PR-40 invocation is not a merge approval or merge instruction; it never authorizes an agent merge,"),
    ("Return a populated same-session resume of the recorded PR phase after the actual merge,", "Return a populated resume of the recorded PR phase in the recorded phase's own session after the actual merge,"),
    ("Bind `update_control_record` to `SHARED_STATE.CONTROL_PLANE: NOTION` and an exact Notion page URL in `LEDGER_DESTINATION`; version 1 cannot represent that binding and must migrate to version 2.",
     "Bind `update_control_record` to `SHARED_STATE.CONTROL_PLANE: NOTION` and an exact Notion page URL in `LEDGER_DESTINATION`; version 1 cannot represent that binding and must migrate to version 2. {S7}"),
    ("4. `NOTION_REFERENCE`: a versionless resource name plus its verified directory path, resolved by the recipient at execution under the prompt-locator rule above.",
     "4. `NOTION_REFERENCE`: a versionless resource name plus its verified directory path, resolved by the recipient at execution under the prompt-locator rule above. {S6}"),
    ("This specialization cannot create a session. When a required participant does not exist, return `SESSION_PROVISIONING_REQUIRED` and stop:",
     "This specialization cannot create a session. Outside a GCFPE main-ecosystem stage, when a required participant does not exist, return `SESSION_PROVISIONING_REQUIRED` and stop:"),
])

# ============================== §8b tw-flowmaster ==============================
rl = rs.split("\n")


def rline(prefix):
    c = [l for l in rl if l.startswith(prefix)]
    assert len(c) == 1, prefix
    return c[0]


twp = root / "tw-flowmaster/SKILL.md"
twl = twp.read_text(encoding="utf-8").split("\n")
assert twl[303].startswith("For every GCFPE reusable prompt") and twl[314].startswith("For GCFPE, assess or preserve advice")
assert twl[318].startswith("PR-30 finishes recovery") and twl[320].startswith("If later approved engineering")
twl[303] = rline("For every GCFPE reusable prompt")          # :304 := relay :259
twl[314] = rline("For GCFPE, assess or preserve advice")      # :315 := relay :279
twl[318] = rline(T["C-SESSION"][:40])                          # :319 := relay :283
twl[320] = rline("If later approved engineering")             # :321 := relay :285
twp.write_text("\n".join(twl), encoding="utf-8")
apply("tw-flowmaster/SKILL.md", [
    ("`TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.1.6`", "`TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0`"),
    ("### GCFPE binding\n\n", "### GCFPE binding\n\n{OVERRIDE}\n\n"),
    ("Add result artifact/PR/commit references when observed;", "Add result artifact/PR/commit references to the usage record when observed, never to the handoff;"),
])

# ============================== §8b flowmaster-validate: validate_flowmaster.py ==============================
FORB4 = ['"same-session PR-35 handoff",', '"preferred live control plane",', '"launched as a new session",',
         '"The Product Owner\'s PR-40 invocation supplies merge approval",']
NEW_CHECKS = '''

# A1-1 successor R1 oracle (spec v2 §5.7, N1-N10 and the R1-literal tie check). The historical oracle and
# historical runtime map stay byte-identical and are still verified; the successor changes exactly the
# three pinned rows, recorded in the successor source matrix.
HISTORICAL_ORACLE_RELATIVE = Path("references/glow-hde-canonical-change-flow-r1.json")
HISTORICAL_ORACLE_SHA256 = (
    "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"
)
HISTORICAL_CHANGE_RUNTIME_MAP_RELATIVE = Path(
    "references/glow-hde-canonical-change-flow-r1-runtime-map.json"
)
HISTORICAL_CHANGE_RUNTIME_MAP_SHA256 = (
    "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e"
)
SUCCESSOR_MATRIX_RELATIVE = Path("references/r1-successor-source-20260923.md")
SUCCESSOR_ROWS = ("GCF-14", "GCF-17", "GCF-17.LINEAGE")
R1_ROW_CONTENT_FIELDS = (
    "id", "partition", "name", "change_class", "actor", "session", "consumes",
    "produces", "next", "approval_contract", "failure_stop_condition",
)
# These four attest the ORIGINAL R1 matrix only; the successor rows are attested by the matrix digest.
HISTORICAL_R1_AUTHORITY = {
    "r1_source_manifest_library_id": "libfile_e66c0851b3d88191a6d3e39e34e987c6",
    "r1_contract_matrix_library_id": "libfile_9caa654f4a648191bb970b2f32970f22",
    "r1_frozen_snapshot_sha256": "5a6d89ed366f467ee75a5c71d23bf1a613dc79bb4d56791e812e20d53e53db67",
    "r1_verdict": "R1_CANONICAL_TRUTH_LOCK_PASS",
}
CANDIDATE_VALIDATOR_RELATIVE = Path("scripts/validate_gcfpe_20260914.py")
MATRIX_BLOCK_RE = re.compile(r"(?ms)^```json\\n(.*?)\\n```$")
R1_ORACLE_LITERAL_RE = re.compile(r'"r1_oracle_sha256":\\s*"([0-9a-f]{64})"')
R1_MAP_LITERAL_RE = re.compile(r'"r1_runtime_map_sha256":\\s*"([0-9a-f]{64})"')
R1_MAP_IDENTITY_RE = re.compile(
    r'runtime_map = change_skill_dir / "references" / "([^"]+)"\\n'
    r'\\s*if not runtime_map\\.is_file\\(\\) or sha256\\(runtime_map\\) != "([0-9a-f]{64})"'
)


def r1_row_digest(row: dict) -> str:
    content = {key: row.get(key) for key in R1_ROW_CONTENT_FIELDS}
    return hashlib.sha256(
        json.dumps(content, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def successor_oracle_findings(skill_dir: Path, oracle: dict[str, object]) -> list[dict[str, str]]:
    """N1 and N3-N10 (FMV-ORACLE-008 to -016) and the R1-literal tie check (FMV-ORACLE-017)."""

    results: list[dict[str, str]] = []
    oracle_path = skill_dir / ORACLE_RELATIVE
    history: dict[str, object] = {}
    history_path = skill_dir / HISTORICAL_ORACLE_RELATIVE
    if history_path.is_file():  # N1; absence is FMV-SKILL-STRUCTURE-001's to report
        history_bytes = history_path.read_bytes()
        history_sha256 = hashlib.sha256(history_bytes).hexdigest()
        if history_sha256 != HISTORICAL_ORACLE_SHA256:
            results.append(finding(
                "FMV-ORACLE-008", str(history_path),
                f"historical R1 oracle sha256={history_sha256}; expected={HISTORICAL_ORACLE_SHA256}",
            ))
        try:
            parsed = json.loads(history_bytes.decode("utf-8"))
            history = parsed if isinstance(parsed, dict) else {}
        except (UnicodeError, json.JSONDecodeError):
            history = {}
    authority = oracle.get("authority") if isinstance(oracle.get("authority"), dict) else {}
    rows = [row for row in oracle.get("runtime_rows", []) if isinstance(row, dict)]
    by_id = {row.get("id"): row for row in rows}
    history_rows = [row for row in history.get("runtime_rows", []) if isinstance(row, dict)]
    history_by_id = {row.get("id"): row for row in history_rows}
    blocks: dict[object, dict] = {}
    matrix_path = skill_dir / SUCCESSOR_MATRIX_RELATIVE
    if matrix_path.is_file():  # N3 and N5; absence is FMV-SKILL-STRUCTURE-001's to report
        matrix_bytes = matrix_path.read_bytes()
        matrix_sha256 = hashlib.sha256(matrix_bytes).hexdigest()
        if matrix_sha256 != authority.get("successor_source_matrix_sha256"):
            results.append(finding(
                "FMV-ORACLE-009", str(matrix_path),
                f"successor source matrix sha256={matrix_sha256}; "
                f"authority.successor_source_matrix_sha256={authority.get('successor_source_matrix_sha256')}",
            ))
        parsed_blocks: list[object] = []
        shape_ok = True
        try:
            for raw in MATRIX_BLOCK_RE.findall(matrix_bytes.decode("utf-8")):
                parsed_blocks.append(json.loads(raw))
        except (UnicodeError, json.JSONDecodeError):
            shape_ok = False
        block_keys = set(R1_ROW_CONTENT_FIELDS) | {"supersedes_source_row_sha256"}
        if (
            not shape_ok
            or len(parsed_blocks) != len(SUCCESSOR_ROWS)
            or any(not isinstance(block, dict) or set(block) != block_keys for block in parsed_blocks)
            or sorted(str(block.get("id")) for block in parsed_blocks if isinstance(block, dict)) != sorted(SUCCESSOR_ROWS)
        ):
            results.append(finding(
                "FMV-ORACLE-011", str(matrix_path),
                f"matrix must hold exactly {len(SUCCESSOR_ROWS)} JSON blocks for {list(SUCCESSOR_ROWS)}, "
                "each with the 11 row content fields and supersedes_source_row_sha256",
            ))
        else:
            blocks = {block["id"]: block for block in parsed_blocks}
    successor_rows = authority.get("successor_rows")
    if (
        not isinstance(successor_rows, list)
        or len(successor_rows) != len(set(map(str, successor_rows)))
        or set(successor_rows) != set(SUCCESSOR_ROWS)
    ):
        results.append(finding(
            "FMV-ORACLE-010", str(oracle_path),
            f"authority.successor_rows={successor_rows!r}; pinned set={sorted(SUCCESSOR_ROWS)}",
        ))
    for row_id in SUCCESSOR_ROWS:
        row = by_id.get(row_id)
        block = blocks.get(row_id)
        if row is None:
            continue
        if block is not None and any(row.get(key) != block.get(key) for key in R1_ROW_CONTENT_FIELDS):
            results.append(finding(
                "FMV-ORACLE-012", str(oracle_path),
                f"row={row_id}; successor row content differs from its successor source matrix block",
            ))
        if row.get("source_row_sha256") != r1_row_digest(row):
            results.append(finding(
                "FMV-ORACLE-013", str(oracle_path),
                f"row={row_id}; source_row_sha256 does not follow the successor row digest formula",
            ))
        if (
            block is not None and history_by_id
            and block.get("supersedes_source_row_sha256")
            != (history_by_id.get(row_id) or {}).get("source_row_sha256")
        ):
            results.append(finding(
                "FMV-ORACLE-014", str(matrix_path),
                f"row={row_id}; supersedes_source_row_sha256 is not the historical row digest",
            ))
    if history_rows:  # N9: the 43 unchanged rows, equal and in the historical order
        kept = [row for row in rows if row.get("id") not in SUCCESSOR_ROWS]
        history_kept = [row for row in history_rows if row.get("id") not in SUCCESSOR_ROWS]
        for row in kept:
            if row != history_by_id.get(row.get("id")):
                results.append(finding(
                    "FMV-ORACLE-015", str(oracle_path),
                    f"row={row.get('id')}; a row outside the successor set differs from the historical R1 row",
                ))
        if [row.get("id") for row in kept] != [row.get("id") for row in history_kept]:
            results.append(finding(
                "FMV-ORACLE-015", str(oracle_path),
                "rows outside the successor set are not the historical rows in the historical order",
            ))
    for key, value in HISTORICAL_R1_AUTHORITY.items():  # N10
        if authority.get(key) != value:
            results.append(finding(
                "FMV-ORACLE-016", str(oracle_path),
                f"authority.{key}={authority.get(key)!r}; it attests the original R1 matrix only and must "
                f"keep its historical value {value!r}",
            ))
    results.extend(r1_literal_tie_findings(skill_dir))
    return results


def r1_literal_tie_findings(skill_dir: Path) -> list[dict[str, str]]:
    """FMV-ORACLE-017: the candidate validator's R1 literals equal the successor files' digests."""

    results: list[dict[str, str]] = []
    validator_path = skill_dir / CANDIDATE_VALIDATOR_RELATIVE
    oracle_path = skill_dir / ORACLE_RELATIVE
    map_path = skill_dir.parent / "change-flow" / CHANGE_RUNTIME_MAP_RELATIVE
    if not validator_path.is_file() or not oracle_path.is_file():
        return results
    text = validator_path.read_text(encoding="utf-8")
    oracle_sha256 = hashlib.sha256(oracle_path.read_bytes()).hexdigest()
    oracle_literals = [(m.group(1), text.count("\\n", 0, m.start()) + 1) for m in R1_ORACLE_LITERAL_RE.finditer(text)]
    if len(oracle_literals) != 3:
        results.append(finding(
            "FMV-ORACLE-017", str(validator_path),
            f"expected 3 r1_oracle_sha256 literals; found {len(oracle_literals)}",
        ))
    for value, line in oracle_literals:
        if value != oracle_sha256:
            results.append(finding(
                "FMV-ORACLE-017", f"{validator_path}:{line}",
                f"r1_oracle_sha256 literal {value} is not the successor oracle digest {oracle_sha256}",
            ))
    map_literals = [(m.group(1), text.count("\\n", 0, m.start()) + 1) for m in R1_MAP_LITERAL_RE.finditer(text)]
    identity = [(m, text.count("\\n", 0, m.start()) + 1) for m in R1_MAP_IDENTITY_RE.finditer(text)]
    if len(map_literals) != 1 or len(identity) != 1:
        results.append(finding(
            "FMV-ORACLE-017", str(validator_path),
            f"expected 1 r1_runtime_map_sha256 literal and 1 runtime-map identity check; "
            f"found {len(map_literals)} and {len(identity)}",
        ))
    if map_path.is_file():
        map_sha256 = hashlib.sha256(map_path.read_bytes()).hexdigest()
        for value, line in map_literals + [(m.group(2), line) for m, line in identity]:
            if value != map_sha256:
                results.append(finding(
                    "FMV-ORACLE-017", f"{validator_path}:{line}",
                    f"runtime-map literal {value} is not the successor runtime map digest {map_sha256}",
                ))
        for m, line in identity:
            if m.group(1) != CHANGE_RUNTIME_MAP_RELATIVE.name:
                results.append(finding(
                    "FMV-ORACLE-017", f"{validator_path}:{line}",
                    f"runtime-map identity check reads {m.group(1)}, not {CHANGE_RUNTIME_MAP_RELATIVE.name}",
                ))
    return results
'''
apply("flowmaster-validate/scripts/validate_flowmaster.py", [
    ('ORACLE_RELATIVE = Path("references/glow-hde-canonical-change-flow-r1.json")\nCHANGE_RUNTIME_MAP_RELATIVE = Path(\n    "references/glow-hde-canonical-change-flow-r1-runtime-map.json"\n)',
     'ORACLE_RELATIVE = Path("references/glow-hde-canonical-change-flow-r1-20260923.json")\nCHANGE_RUNTIME_MAP_RELATIVE = Path(\n    "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"\n)'),
    ('EXPECTED_ORACLE_PROFILE = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1"', 'EXPECTED_ORACLE_PROFILE = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1"'),
    ('"TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.1.6",', '"TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0",\n        ' + json.dumps(T["OVERRIDE"], ensure_ascii=False) + ",\n        " + json.dumps(T["A18"], ensure_ascii=False) + ","),
    ('        "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9",\n        "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1",',
     '        "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0",\n        ' + json.dumps(T["OVERRIDE"], ensure_ascii=False) + ',\n        "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1",'),
    ('"SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.0.0",', '"SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0",\n        ' + json.dumps(T["OVERRIDE"], ensure_ascii=False) + ",\n        " + json.dumps(T["A18"], ensure_ascii=False) + ","),
    ('            "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9",\n', '            "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0",\n'),
    ('        "session_control_timeout_seconds = [[",\n    ),', '        "session_control_timeout_seconds = [[",\n' + "".join("        " + f + "\n" for f in FORB4) + "    ),"),
    ('        "attach the file to the message",\n    ),', '        "attach the file to the message",\n' + "".join("        " + f + "\n" for f in FORB4) + "    ),"),
    ('        "references/glow-hde-canonical-change-flow-r1.json",\n    ),',
     '        "references/glow-hde-canonical-change-flow-r1.json",\n        "references/glow-hde-canonical-change-flow-r1-20260923.json",\n        "references/r1-successor-source-20260923.md",\n    ),'),
    ('        "references/glow-hde-canonical-change-flow-r1-runtime-map.json",\n        "references/gcfpe-current-direct-handoff-contract.json",\n    },',
     '        "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json",\n        "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",\n    },'),
    ('            "validator_revision": "3.2.14",', '            "validator_revision": "3.3.0",'),
    ('                str(change_dir / "references" / "gcfpe-current-direct-handoff-contract.json"),',
     '                str(change_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"),'),
    # N1, N3-N10 and FMV-ORACLE-017 run with the oracle load (flowmaster-validate directory).
    ("def load_change_oracle(skill_dir: Path) -> tuple[dict[str, object], list[dict[str, str]]]:\n    oracle_path = skill_dir / ORACLE_RELATIVE\n",
     "def load_change_oracle(skill_dir: Path) -> tuple[dict[str, object], list[dict[str, str]]]:\n"
     "    oracle, findings = load_change_oracle_core(skill_dir)\n"
     "    if oracle:\n"
     "        findings.extend(successor_oracle_findings(skill_dir, oracle))\n"
     "    return oracle, findings\n\n\n"
     "def load_change_oracle_core(skill_dir: Path) -> tuple[dict[str, object], list[dict[str, str]]]:\n"
     "    oracle_path = skill_dir / ORACLE_RELATIVE\n"),
    ("\n\ndef extract_marked_json(", NEW_CHECKS + "\n\ndef extract_marked_json("),
    # N2 (FMV-GCF-MAP-007) runs with the change-flow contract (change-flow directory).
    ("    map_path = Path(subject).parent / CHANGE_RUNTIME_MAP_RELATIVE\n",
     "    historical_map_path = Path(subject).parent / HISTORICAL_CHANGE_RUNTIME_MAP_RELATIVE\n"
     "    try:\n"
     "        historical_map_sha256 = hashlib.sha256(historical_map_path.read_bytes()).hexdigest()\n"
     "    except OSError as exc:\n"
     "        historical_map_sha256 = f\"unreadable: {exc}\"\n"
     "    if historical_map_sha256 != HISTORICAL_CHANGE_RUNTIME_MAP_SHA256:\n"
     "        results.append(\n"
     "            finding(\n"
     "                \"FMV-GCF-MAP-007\",\n"
     "                str(historical_map_path),\n"
     "                f\"historical runtime map sha256={historical_map_sha256}; expected={HISTORICAL_CHANGE_RUNTIME_MAP_SHA256}\",\n"
     "            )\n"
     "        )\n"
     "    map_path = Path(subject).parent / CHANGE_RUNTIME_MAP_RELATIVE\n"),
])

# ============================== §8b flowmaster-validate: validate_gcfpe_current.py etc. ==============================
apply("flowmaster-validate/scripts/validate_gcfpe_current.py", [
    ('    contract_path = contract_path or change_skill_dir / "references" / "gcfpe-current-direct-handoff-contract.json"\n    if not contract_path.is_file():',
     '    contract_path = contract_path or change_skill_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"\n    if not contract_path.is_file():'),
    ('    if skill_text.count("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9") != 1:\n        errors.append("ACTIVE_CONTRACT_MISSING:CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9")',
     '    if skill_text.count("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0") != 1:\n        errors.append("ACTIVE_CONTRACT_MISSING:CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0")'),
    ('            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5",\n            "## Recover before creating work", "one dedicated PR-development session", "RS-40", "PR-50",',
     '            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0",\n            "## Recover before creating work", "run in two dedicated sessions", "RS-40", "PR-50",'),
    ('EXPECTED_RUNTIME_MAP_SHA256 = "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e"\n',
     'EXPECTED_RUNTIME_MAP_SHA256 = "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e"\n'
     '# The installed runtime map is the successor projection (A1-1); the two constants above stay the\n'
     '# 091326.2 alias\'s recorded historical values.\n'
     'EXPECTED_INSTALLED_RUNTIME_MAP_SHA256 = "<SUCC_MAP>"\n'),
    ('    runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map.json"\n    if not runtime_map.is_file() or sha256(runtime_map) != EXPECTED_RUNTIME_MAP_SHA256:',
     '    runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"\n    if not runtime_map.is_file() or sha256(runtime_map) != EXPECTED_INSTALLED_RUNTIME_MAP_SHA256:'),
])
apply("flowmaster-validate/scripts/run_gcfpe_current_fixtures.py", [
    ('    contract_path = contract_path or change_skill_dir / "references" / "gcfpe-current-direct-handoff-contract.json"\n    source = json.loads',
     '    contract_path = contract_path or change_skill_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"\n    source = json.loads'),
])
apply("flowmaster-validate/scripts/run_change_flow_fixtures.py", [
    ('ORACLE_PATH = SKILL_DIR / "references" / "glow-hde-canonical-change-flow-r1.json"', 'ORACLE_PATH = SKILL_DIR / "references" / "glow-hde-canonical-change-flow-r1-20260923.json"'),
])
# §5.10 R1 path fixture, inserted as text in the file's hand style; oracle_profile moves.
apply("flowmaster-validate/fixtures/change-flow/scenarios.json", [
    ('"oracle_profile": "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1",', '"oracle_profile": "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1",'),
    ('        {"row": "GCF-09"}\n      ]\n    }\n  ]\n}\n',
     '        {"row": "GCF-09"}\n      ]\n    },\n    {\n      "id": "GCF-LINEAGE-REPLAN-01",\n      "expected_pass": true,\n'
     '      "expected_rule_ids": [],\n      "coverage_mode": "COMPLETE",\n'
     '      "events": [{"row": "GCF-17.LINEAGE"}, {"row": "GCF-14"}]\n    }\n  ]\n}\n'),
])
_scen = json.loads((root / "flowmaster-validate/fixtures/change-flow/scenarios.json").read_text(encoding="utf-8"))
assert _scen["scenarios"][-1] == {"id": "GCF-LINEAGE-REPLAN-01", "expected_pass": True, "expected_rule_ids": [],
                                  "coverage_mode": "COMPLETE", "events": [{"row": "GCF-17.LINEAGE"}, {"row": "GCF-14"}]}

# ============================== §8b.7 validate_gcfpe_20260914.py reversals ==============================
S87 = SPEC[SPEC.index("### 8b.7 "):SPEC.index("### 8b.8 ")]
S87L = S87.split("\n")


def spec_def(first_line, last_line=None):
    """The spec's code, from a line equal to `first_line` to the first following line equal to `last_line`
    (default: the closing '}' or ']' at column 0)."""
    i = S87L.index(first_line)
    if last_line is None and not first_line.endswith(("{", "[")):
        return first_line
    end = last_line or ("}" if first_line.endswith("{") else "]")
    j = S87L.index(end, i + 1)
    return "\n".join(S87L[i:j + 1])


CONSTS = "\n".join([
    spec_def("EXPECTED_PR35_ADDED_BOUNDARIES = {"),
    spec_def("EXPECTED_TRANSITION_CONTRACT = {"),
    spec_def("EXPECTED_OBSERVED_MERGE_EDGES = ["),
    spec_def("EXPECTED_EVENT_2 = {"),
    spec_def("EXPECTED_RECEIVERS = {"),
    spec_def("EXPECTED_ROUTE_GRAPH_SEMANTICS = {"),
    spec_def('PR35_TOP_LEVEL_ROLE_PHRASE = "never as a subagent, forked agent or workflow agent of PR-30"'),
    spec_def("OBSERVED_MERGE_EDGE_CONDITIONS = {"),
]) + "\n\n\n" + spec_def("def observed_merge_edge_errors(edges) -> bool:", "    return False") + "\n\n\n"
_rel_block = spec_def('RELEASE_HEADER_KEYS = ("Prompt Version:", "Prompt version:", "Set:", "Ecosystem release:")')
_hdr_fn = spec_def("    return bool(", '    return any(line.startswith(key) for line in stripped for key in RELEASE_HEADER_KEYS)')
OLD_HDR_COMMENT = ("# The release carries two identity-header conventions, both accepted by the\n"
                   "# approved Project Prompt Contract Registry, whose per-row required regex is\n"
                   "# `Prompt [Vv]ersion: `?091426\\.1`?`: an unbackticked form using\n"
                   "# `Selection status:` and a backticked form using `Lifecycle:`.  Both are\n"
                   "# recognised here; neither is preferred.\n")
NEW_HDR_COMMENT = ("# D23-G: a body carries no release-bound header line (Prompt version, Set, Ecosystem release);\n"
                   "# prompt_body_release_header rejects one in the header window as PROMPT_BODY_RELEASE_HEADER.\n")
FV = "flowmaster-validate/scripts/validate_gcfpe_20260914.py"
apply(FV, [
    (OLD_HDR_COMMENT, NEW_HDR_COMMENT),
    ('EXPECTED_PR35_RESULTS = [\n    "MERGE_PENDING", "RESCOPE_PENDING",', 'EXPECTED_PR35_RESULTS = [\n    "MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING",'),
    ('    "WORK_UNIT_ID", "original Product Owner Proceed", "dedicated PR-development session",\n    "workspace/worktree",',
     '    "WORK_UNIT_ID", "original Product Owner Proceed",\n    "workspace/worktree",'),
    ('PROMPT_VERSION_HEADER_RE = re.compile(r"^Prompt [Vv]ersion: `?091426\\.1`?$")', _rel_block),
    ('    return bool(\n        len(nonblank) >= 7\n        and nonblank[0] == member.get("title")\n        and any(PROMPT_VERSION_HEADER_RE.match(line) for line in nonblank[:8])\n        and any(line in header_value_lines("Prompt ID:", prompt_id) for line in nonblank[:8])\n        and any(\n            line in header_value_lines("Ecosystem release:", "GCFPE-20260914.1")\n            for line in nonblank[:8]\n        )\n        and url_line_ok\n    )\n',
     _hdr_fn + "\n"),
    ('        if not prompt_identity_header_valid(nonblank, member, prompt_id):\n            errors.append(f"PROMPT_BODY_IDENTITY:{prompt_id}")\n',
     '        if not prompt_identity_header_valid(nonblank, member, prompt_id):\n            errors.append(f"PROMPT_BODY_IDENTITY:{prompt_id}")\n        if prompt_body_release_header(nonblank):\n            errors.append(f"PROMPT_BODY_RELEASE_HEADER:{prompt_id}")\n'),
    ('        "contract_revision": "4.0.6",', '        "contract_revision": "4.1.0",'),
    ('    errors += subset_errors(transition, {\n        "transport": "DIRECT_NATIVE_PROMPT_HANDOFF", "block": "NEXT_PROMPT_HANDOFF",\n        "fence_language": "text", "first_line": "NEXT_PROMPT_HANDOFF",\n        "exactly_one_per_nonterminal_result": True, "terminal_has_no_handoff": True,\n        "actual_branch_only": True, "actual_pasteable_complete_prompt": True,\n        "metadata_only_or_routing_summary_prohibited": True,\n        "blank_form_menu_or_reconstruction_prohibited": True,\n        "exact_destination_full_name_version_direct_notion_url": True,\n        "receiving_role_and_exact_session": True, "epic_change_and_work_unit": True,\n        "every_required_repository_and_pr_reference": True,\n        "status_completed_work_decisions_constraints_unresolved_authority": True,\n        "next_action_and_expected_output": True,\n    }, "HANDOFF_CONTRACT")\n',
     '    if (\n        not isinstance(transition, dict)\n        or set(transition) != set(EXPECTED_TRANSITION_CONTRACT) | {"prohibited_references"}\n        or any(transition.get(key) != value for key, value in EXPECTED_TRANSITION_CONTRACT.items())\n    ):\n        errors.append("HANDOFF_CONTRACT")\n'),
    ('        "model/strength/reasoning/eligibility/suitability/account/configuration route",\n    }:\n        errors.append("HANDOFF_PROHIBITED_REFERENCES")',
     '        "model/strength/reasoning/eligibility/suitability/account/configuration route",\n        "branch", "commit", "restated artifact content",\n        "menu", "metadata-only summary", "blank form", "placeholder after publication",\n    }:\n        errors.append("HANDOFF_PROHIBITED_REFERENCES")'),
    ('        "primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.2.5",',
     '        "primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.3.0",\n        "pr30_ownership": [\n            "recovery", "implementation", "local testing", "coherent commit creation",\n            "deliberate initial publication", "complete PR-35 handoff to the dedicated PR-35 session",\n        ],'),
    ('        "accepted_final_replay": False, "automatic_abort_route": False,\n    }, "RESCOPE_CONTRACT")',
     '        "accepted_final_replay": False, "automatic_abort_route": False,\n        "preserved_lineage": [\n            "PR_RETURN_PHASE", "PR_PHASE_SESSION", "WORKSPACE", "WORKTREE", "BRANCH",\n            "OPEN_PR_WHEN_ONE_EXISTS", "COMMIT", "ORIGINAL_PROCEED", "COMPLETED_WORK", "TESTS",\n            "REVIEWS", "CI_STATE", "DECISION", "ARTIFACTS", "UNRESOLVED_WORK",\n        ],\n    }, "RESCOPE_CONTRACT")'),
    ('    if not isinstance(development, dict) or any(value != 0 for value in development.get("added_boundaries", {}).values()):\n        errors.append("PR35_ADDED_BOUNDARY")\n    if not isinstance(development, dict) or development.get("shared_exactly_one") != EXPECTED_PHASE_CONTINUITY:\n        errors.append("PR_PHASE_CONTINUITY")',
     '    if not isinstance(development, dict) or development.get("added_boundaries") != EXPECTED_PR35_ADDED_BOUNDARIES:\n        errors.append("PR35_ADDED_BOUNDARY")\n    if not isinstance(development, dict) or development.get("shared_exactly_one") != EXPECTED_PHASE_CONTINUITY or "dedicated PR-development session" in development.get("shared_exactly_one", []):\n        errors.append("PR_PHASE_CONTINUITY")'),
    ("EXPECTED_MERGE_PENDING_REQUIREMENTS = {", CONSTS + "EXPECTED_MERGE_PENDING_REQUIREMENTS = {"),
    ('        "agent_merge_authorized": False, "direct_PR35_to_PR40_automatic_edge": False,\n    }, "POST_MERGE_CONTRACT")',
     '        "agent_merge_authorized": False, "direct_PR35_to_PR40_automatic_edge": False,\n        "observed_merge_edges": EXPECTED_OBSERVED_MERGE_EDGES,\n    }, "POST_MERGE_CONTRACT")'),
    ('        or (postmerge.get("event_2") or {}).get("actor") != "Nathan / Product Owner"\n        or (postmerge.get("event_2") or {}).get("fact") != "product_owner_manual_merge_assertion"\n',
     '        or postmerge.get("event_2") != EXPECTED_EVENT_2\n'),
    ('        "ordinary_pr_work_unit": [\n            "PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35",\n            "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40",\n        ],',
     '        "ordinary_pr_work_unit": ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "PR-40"],\n        "pr35_merge_pending_fallback": ["PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"],\n        "pr40_reject_replan": ["PR-40", "PR-20", "NATHAN_PROCEED", "PR-30"],'),
    ('    if contract.get("route_graph") != expected_route_graph:\n        errors.append("ROUTE_GRAPH_SHORTHAND")\n',
     '    if contract.get("route_graph") != expected_route_graph:\n        errors.append("ROUTE_GRAPH_SHORTHAND")\n    if contract.get("route_graph_semantics") != EXPECTED_ROUTE_GRAPH_SEMANTICS:\n        errors.append("ROUTE_GRAPH_SEMANTICS")\n    if PR35_TOP_LEVEL_ROLE_PHRASE not in str(((contract.get("member_registry") or {}).get("PR-35") or {}).get("receiving_role", "")):\n        errors.append("PR35_TOP_LEVEL_ROLE")\n'),
    ('        if any(edge.get("from") == "PR-35" and edge.get("to") == "PR-40" for edge in edges if isinstance(edge, dict)):\n            errors.append("DIRECT_PR35_PR40_EDGE")',
     '        if observed_merge_edge_errors(edges):\n            errors.append("DIRECT_PR35_PR40_EDGE")\n        replan = [e for e in edges if isinstance(e, dict) and e.get("from") == "PR-40" and any(isinstance(b, dict) and b.get("branch_id") in {"reject_replan", "reject_existing_pr_owner"} for b in e.get("route_branches", []))]\n        if len(replan) != 1 or replan[0].get("to") != "PR-20" or any(isinstance(e, dict) and e.get("from") == "PR-40" and e.get("to") == "PR-30" for e in edges):\n            errors.append("PR40_REJECT_REPLAN_ROUTE")'),
    ('        and edge.get("from") in {"PR-30", "PR-35"}\n        and edge.get("to") == "PR-40"\n        for edge in edges\n    ):\n        errors.append("GRAPH_DIRECT_PR40_EDGE")',
     '        and edge.get("from") in {"PR-30"}\n        and edge.get("to") == "PR-40"\n        for edge in edges\n    ) or observed_merge_edge_errors(edges):\n        errors.append("GRAPH_DIRECT_PR40_EDGE")'),
    ('        errors.append("GRAPH_HANDOFF_CONTRACT_MISMATCH")\n',
     '        errors.append("GRAPH_HANDOFF_CONTRACT_MISMATCH")\n    if not isinstance(graph_handoff, dict) or not isinstance(transition, dict) or not set(graph_handoff.get("prohibited", [])) <= set(transition.get("prohibited_references", [])):\n        errors.append("GRAPH_HANDOFF_PROHIBITED_REFERENCES")\n'),
    ('    recovery_pr40 = [edge for edge in inbound_pr40 if edge.get("from_kind") == "prompt"]',
     '    recovery_pr40 = [edge for edge in inbound_pr40 if edge.get("from_kind") == "prompt" and edge.get("from") not in OBSERVED_MERGE_EDGE_CONDITIONS]'),
    ('        "PR-35": ("REMOTE_EVIDENCE_PENDING", "PR_REMOTE_ACTION_LEDGER", "MERGE_PENDING"),',
     '        "PR-35": ("REMOTE_EVIDENCE_PENDING", "PR_REMOTE_ACTION_LEDGER", "MERGE_PENDING", "MERGE_OBSERVED"),'),
    ('        "RS-40": ("SOURCE_RESOLUTION_ERROR", *EXPECTED_RETURN_PHASES),',
     '        "RS-40": ("SOURCE_RESOLUTION_ERROR", *EXPECTED_RETURN_PHASES, "MERGE_OBSERVED"),'),
    ('        "r1_rows": 46, "flowmaster_primary_core_changed": False,\n        "r1_oracle_changed": False, "pr35_adds_r1_row": False,',
     '        "r1_rows": 46, "flowmaster_primary_core_changed": False,\n        "r1_oracle_changed": True, "pr35_adds_r1_row": False,'),
    ('        "automatic_pr50_edges": 0, "protected_primary_core_unchanged": True,\n        "protected_r1_46_rows_unchanged": True,',
     '        "automatic_pr50_edges": 0, "protected_primary_core_unchanged": True,\n        "protected_r1_46_rows_unchanged": False,'),
    ('    errors.extend(validate_artifact_timing_contract(contract))\n    return sorted(set(errors))\n\n\ndef find_skill(',
     '    receivers = contract.get("receiver_compatibility")\n    for receiver in sorted(set(EXPECTED_RECEIVERS) | set(receivers if isinstance(receivers, dict) else {})):\n        if not isinstance(receivers, dict) or receivers.get(receiver) != EXPECTED_RECEIVERS.get(receiver):\n            errors.append(f"RECEIVER_CONTRACT:{receiver}")\n    errors.extend(validate_artifact_timing_contract(contract))\n    return sorted(set(errors))\n\n\ndef find_skill('),
    ('        "edge_count": 227,', '        "edge_count": 229,'),
    ('        "schema_version": "gcfpe-scenarios/2.0", "count": 33,', '        "schema_version": "gcfpe-scenarios/2.0", "count": 37,'),
    ('EXPECTED_ROUTING_SURFACE = "7380cd14430777675f1e8b2cdfa4a0da"\nEXPECTED_ROUTING_SURFACE_ROWS = 282',
     'EXPECTED_ROUTING_SURFACE = "fecc319bdd4ce7ee6201cb77d7231861"\nEXPECTED_ROUTING_SURFACE_ROWS = 284'),
    ('        "validator_revision": "3.2.14",', '        "validator_revision": "3.3.0",'),
    ('            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5", "REMOTE_EVIDENCE_PENDING",', '            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0", "REMOTE_EVIDENCE_PENDING",'),
    ("            " + json.dumps(T["TEN"]) + ",\n", "            " + json.dumps(T["NINE"]) + ",\n"),
    ("    # option: a file would persist, and a persisted corpus is what the policy forbids.  Supply", "    # option: {C-D22}.  Supply"),
    # §5.8: the R1 runtime-map path at :2610 (its digest is written by pin_e2.py).
    ('    runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map.json"\n',
     '    runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"\n'),
])

# ============================== §8b.9 runner and scenarios ==============================
PATCH = HERE / "section8b9_runner_scenarios.patch"
r = subprocess.run(["patch", "-p1", "--no-backup-if-mismatch", "-i", str(PATCH)], cwd=root, capture_output=True, text=True)
assert r.returncode == 0, r.stdout + r.stderr
LOG.append(("section8b9_runner_scenarios.patch", r.stdout.strip().replace("\n", "; ")))
apply("flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py", [
    ("No path option: a file would persist.", "No path option: {C-D22}."),
    ('    ] + ["Purpose line."] * 0\n', "    ]\n"),   # no-op list padding left by the simulation; behaviour unchanged
])

# ============================== §8b.6 flowmaster-validate/SKILL.md (text; §5 R1 lines are pin_e2.py's) ==============================
apply("flowmaster-validate/SKILL.md", [
    ("FLOWMASTER_VALIDATE_REVISION: 3.2.16", "FLOWMASTER_VALIDATE_REVISION: 3.3.0"),
    ("deliberately with no path option, because a file persists --", "deliberately with no path option, because {C-D22} --"),
    ("The 20260914 candidate contract revision 4.0.6 binds", "The 20260914 candidate contract revision 4.1.0 binds"),
    ("The selected alias `references/gcfpe-current-direct-handoff-contract.json` must match that live binding.",
     "The current overlay `references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json` must match that live binding; the `gcfpe-current-direct-handoff-contract.json` alias is historical provenance and no longer a validation default."),
    ("- PR-30 and PR-35 are two phases of one GCF-17 PR work unit. {TEN}. Both phases share exactly one value for every field. PR-35 adds zero roles, sessions, approvals, gates, Proceeds, work units, R1 rows, merge authority, work vehicles, or cross-session routes.",
     "- {C-SESSION} {NINE}. Both phases share exactly one value for every field. PR-35 adds zero roles, approvals, gates, Proceeds, work units, R1 rows, merge authority, or work vehicles."),
    ("coherent commits, deliberate initial publication, and its same-session PR-35 handoff.", "coherent commits, deliberate initial publication, and its PR-35 handoff."),
    ("The exact PR-35 results are `MERGE_PENDING`, `RESCOPE_PENDING`,", "The exact PR-35 results are `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,"),
    ("PR-35 `MERGE_PENDING` is historical pre-merge evidence; Nathan's later invocation asserts the manual merge; PR-40 independently verifies actual merged state and landed lineage read-only.",
     "PR-35 `MERGE_PENDING` is historical pre-merge evidence; {FALLBACK}, Nathan's later invocation asserts the manual merge; PR-40 independently verifies actual merged state and landed lineage read-only. {C-DISPATCH}"),
    ("The versioned 33-case section-13 fixture suite", "The versioned 37-case section-13 fixture suite"),
    ("the TW specialization revision is 1.1.6 (including", "the TW specialization revision is 1.2.0 (including"),
    ("There is no path option and there will not be one: a file persists, and\na persisted corpus is what the policy forbids.", "There is no path option and there will not be one: {C-D22}."),
    ("12. One dedicated PR session plans and implements one work unit.", "12. PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request."),
    ("During candidate staging, the suite validates the selected 54-member `GCFPE-20260913.1 / 091326.2` alias and its predecessor fixtures first.",
     "By default the suite validates the 091426.1 current overlay and its schema-4 fixtures; the 54-member `GCFPE-20260913.1 / 091326.2` alias is validated only when passed explicitly."),
    ("and all 33 section-13 fixtures.", "and all 37 section-13 fixtures."),
    ("The fixture report separates 33 required fixture IDs,", "The fixture report separates 37 required fixture IDs,"),
    ("resumes the recorded phase in the same session/worktree/branch/open PR under the original Proceed.", "resumes the recorded phase in that phase's own session, worktree, branch and open PR under the original Proceed."),
])

for rel, n in LOG:
    print(f"{rel}: {n}")
print("skill edits applied")
