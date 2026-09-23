"""v2 §8a + §8b skill-text and skill-side literal edits, with every §12 decision applied. Scratch copy only."""
import sys, json, re
sys.dont_write_bytecode = True
from common import apply
from texts import T
def x(s):
    for k, v in T.items():
        s = s.replace('{' + k + '}', v)
    return s
root = sys.argv[1]
def A(rel, edits, label=None):
    return apply(root + '/' + rel, [(x(o), x(n)) for o, n in edits], label or rel)
LANDED, FB = T['LANDED'], T['FALLBACK']
# ---------------- §8a glow-hde-pr-development ----------------
A('glow-hde-pr-development/SKILL.md', [
 ('Glow HDE PR work unit in its single dedicated development session across', 'Glow HDE PR work unit, run in two dedicated sessions, across'),                 # :3
 ('`GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5`', '`GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0`'),                                                          # :8
 ('Keep the existing GCFPE actor, one dedicated PR-development session, one original Product Owner Proceed, scope, and manual-merge boundaries intact.',
  'Keep the existing GCFPE actor, one Proceed per approved per-PR plan, scope, and manual-merge boundaries intact.'),                                              # :10
 ('detailed PR implementation Plan covered by the original Proceed, with', 'detailed PR implementation Plan covered by the Proceed, with'),                       # :17 O3(a)
 ('the complete `PR_CANDIDATE_PUBLISHED` result and same-session PR-35 handoff;', 'the complete `PR_CANDIDATE_PUBLISHED` result and PR-35 handoff;'),          # :22
 (', the PR-35 handoff; in either case require the exact workspace/worktree, branch, open PR and remote-head lineage;', ', the PR-35 handoff;'),               # :22 O4(a)
 ('coherent initial publication followed in the same session by PR-35 review remediation', 'coherent initial publication followed by PR-35 review remediation'),# :27
 ('only for its explicit scope; continuation preserves the original Proceed and never requires or creates a second Proceed.', 'only for its explicit scope. {C-PROCEED}'), # :27
 ('3. Match prior work using evidence such as', '3. Match prior work of the current plan cycle using evidence such as'),                                         # :43 O5(a)
 ('Reconcile partial or ambiguous external effects before retrying them.', 'Reconcile partial or ambiguous external effects before retrying them. {LANDED}'),   # :44
 ('Remain in the one dedicated PR-development session across both phases.', '{C-SESSION}'),                                                                    # :53
 ('followed by exactly one complete same-session `PR-35` handoff.', 'followed by exactly one complete `PR-35` handoff to the dedicated PR-35 session.'),        # :53
 ('The phase boundary adds no actor, session, work unit,', 'The phase boundary adds no actor, work unit,'),                                                      # :53 O7(b)
 ('Proceed, R1 row, or authority transfer.', 'Proceed, R1 row, authority transfer, or any session beyond its own dedicated PR-35 session.'),                     # :53 O7(b)
 ('{TEN}.', '{NINE}.'),                                                                                                                                          # :55
 ('The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`,', 'The PR-35 result vocabulary is exactly `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,'), # :57
 ('route a substantiated material boundary through the existing rescope path.', 'route a substantiated material change (as defined below) through the existing rescope path.'), # :65 O2(a)
 ('Reuse an existing PR for the same branch/work unit instead of creating another.', 'Reuse an existing PR for the same branch/work unit in the current plan cycle instead of creating another. {LANDED}'), # :77 O6(b)
 ('- Bundle related implementation or review corrections into one locally verified push when practical.', '- Bundle related implementation changes into one locally verified push when practical.'), # :79
 ('that invokes the exact selected PR-35 in this same dedicated session with all repository, worktree, branch, PR, remote-head, artifact, test, constraint, unresolved-item, and original-Proceed lineage.',
  'that invokes the exact selected PR-35 in the dedicated PR-35 session.'),                                                                                    # :82
 ('or create another PR/session/Proceed.', 'or create another PR/session/Proceed; one branch and one pull request per plan cycle.'),                              # :82 O6(b)
 ('Continue in the same dedicated PR session until all applicable predicates are true:', "Continue in this phase's own dedicated session until all applicable predicates are true:"), # :100
 ('- the complete PR implementation result and handoff artifacts are saved and read back.',
  '- the complete PR implementation result (`PR_IMPLEMENTATION_RESULT`) and handoff artifacts are saved and read back; `PR_IMPLEMENTATION_RESULT` includes:\n  - {C-DEC}'), # :108
 ('or keep polling for that manual action.\n', 'or keep polling for that manual action. {C-DISPATCH}\n'),                                                      # :110
 ('\nUse `REMOTE_EVIDENCE_PENDING` only in PR-35 when', '\n{C-SUB}\n\nUse `REMOTE_EVIDENCE_PENDING` only in PR-35 when'),                                    # before :112
 ('- poll only when a pending remote result can change the next action;', '- where no subscription delivers it, poll only when a pending remote result can change the next action;'), # :121
 ('## Route a real material boundary\n\nWhen repository evidence proves that the approved work unit cannot be completed without changing approved scope, architecture, requirements, or Plan authority:',
  '## Route a real material boundary\n\n{C-LAT}\n\nWhen repository evidence proves a material change, as defined above:'),                                    # :126-:128 O2(a)
 ('repository/workspace/worktree/branch state, open PR and remote head only when they actually exist, ', ''),                                                   # :133 O8(b)
 ('Resume the recorded phase in the same dedicated PR session, workspace/worktree, branch, open PR,', "Resume the recorded phase in the recorded phase's own dedicated session, workspace/worktree, branch, open PR,"), # :141
 ('The work unit keeps exactly one branch and one pull request, which the ten-field continuity list requires;', 'The work unit keeps exactly one branch and one pull request per plan cycle, which the nine-field continuity list requires;'), # :158
 ('for artifacts. The Product Owner merges.\n\n', 'for artifacts. The Product Owner merges.\n\n{C-ART}\n\n'),                                                    # after :158 O1(a)
 ('It must instruct the receiver to run the exact selected Notion prompt by full name, version, and direct Notion URL; identify the receiving role and exact continuing/dedicated session; identify the change/Epic and work unit; supply every required repository path and repository/PR reference; state current status, completed work, decisions, constraints, unresolved items, and preserved authority; and state the next required action and expected output.', '{C-HANDOFF}'), # :162 O23(a)
 ('or unrecoverable work.\n', 'or unrecoverable work. {C-PLACE}\n'),                                                                                          # :162 (conflict 15)
 ('At PR-30 `PR_CANDIDATE_PUBLISHED`, return the exact same-session PR-35 continuation.', 'At PR-30 `PR_CANDIDATE_PUBLISHED`, return the exact PR-35 continuation.'), # :164
 ('to use it only after Nathan has manually merged the identified PR;', 'to use it only after Nathan has manually merged the identified PR and {FALLBACK};'),  # :164
 ('- Do not create hidden sessions or extra approval stages.', '- Do not create sessions or extra approval stages.'),                                          # :173 W-9
])
REPLAN_CASE = ('\n## PR-40 rejection re-plan\n\n'
  'Given a PR-40 `REJECT` (`reject_replan`) for this `WORK_UNIT_ID`, whose pull request merged under the earlier plan cycle, '
  'PR-20 plans that work unit again in a new top-level session that Nathan creates, and the new plan receives its own Proceed. '
  'PR-30 starts only from the Proceed of its own plan. ' + LANDED + ' '
  'PR-30 creates a new branch and a new pull request for the new plan. '
  'The earlier Proceed is spent and is never reused.\n')
O16_CASES = ('\n## In-flight decisions\n\n'
  "Given a decision that is not material and is obvious, necessary to deliver the approved scope, and consistent with the Epic's objective and controlling constraints, PR-30 or PR-35 decides it, implements it, tests it, and records it under *In-flight decisions* in `PR_IMPLEMENTATION_RESULT`: what changed, why it was necessary to deliver the approved scope, and what was tested, by test identity and outcome. That holds even if the plan did not anticipate it; `NONE` is recorded when there were none.\n"
  '\n## Implementor latitude\n\n'
  'Given a planned approach found incomplete, impractical or inferior, that alone is not material. A change to the Epic-level commitment — its outcome or objective; approved acceptance criteria; a protected architectural, security, data-model or external-contract boundary; the scope of several planned work units; an accepted dependency or cross-team commitment; or budget, schedule or risk needing Product Owner direction — takes the formal rescope route. Anything that is neither material nor obvious and necessary is not done; it is recorded as a candidate for its owner.\n'
  '\n## Pull request subscription\n\n'
  "Given PR-35 entry, subscribe to the pull request's activity where the surface provides it, and record the subscription as active only when the tool result confirms that this session receives the pull request's events. Act on review, comment and check events as they arrive. Without an active subscription, `REMOTE_EVIDENCE_PENDING` and its re-entry handoff apply as before. The subscription creates no session.\n"
  '\n## Observed merge\n\n'
  'Given `MERGE_PENDING` returned with the conditional PR-40 block and an active subscription, when the subscription delivers the merge of the identified PR — a merge Nathan performs — PR-35 returns `MERGE_OBSERVED` with the paste-ready PR-40 handoff and returns control. Nathan creates the PR-40 session and pastes it; PR-40 still verifies the merged state and landed lineage independently. The conditional PR-40 block stays usable only after Nathan merges and ' + FB + '. No agent merges or creates a session.\n')
A('glow-hde-pr-development/references/behavior-cases.md', [
 ('with exactly one complete same-session PR-35 handoff.', 'with exactly one complete PR-35 handoff.'),                                                          # :7
 ('The phase split creates no new role, session, Proceed,', 'The phase split creates no new role, Proceed,'),                                                    # :7 O7(b)
 ('R1 row, work unit, or PR.', 'R1 row, work unit, PR, or any session beyond its own dedicated PR-35 session.'),                                                  # :7 O7(b)
 ('invokes the exact selected PR-35 in the same dedicated PR-development session with complete lineage.', 'invokes the exact selected PR-35 in the dedicated PR-35 session.'), # :11
 ('The shared phase identity preserves the exact ordered ten-field GCF-17 continuity list: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree;',
  'The shared phase identity preserves the exact ordered nine-field GCF-17 continuity list: `WORK_UNIT_ID`; original Product Owner Proceed; workspace/worktree;'), # :13
 ('Given the complete same-session PR-35 handoff,', 'Given the complete PR-35 handoff,'),                                                                        # :17
 ('PR-35 returns only `MERGE_PENDING`, `RESCOPE_PENDING`,', 'PR-35 returns only `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,'),                        # :21
 ('Given evidence that implementation requires an approved-boundary change,', 'Given evidence that implementation requires a material change to the Epic-level commitment,'), # :49
 ('resume the recorded phase in the same PR session, workspace/worktree, branch, open PR and original Proceed.', "resume the recorded phase in the recorded phase's own dedicated session, workspace/worktree, branch, open PR and original Proceed."), # :57 O15(b)
 ('The conditional prompt separately requires', 'The conditional prompt, usable {FALLBACK}, separately requires'),                                             # :87
])
p = root + '/glow-hde-pr-development/references/behavior-cases.md'
open(p, 'a', encoding='utf-8').write(REPLAN_CASE + O16_CASES)
V5 = T['V5']; V6 = T['V6']
A('glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py', [
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
# ---------------- §8a amthor ----------------
AM = 'amthor-workspace-governance-audit/'
A(AM + 'SKILL.md', [
 ('**WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3', '**WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.12.0'),
 ('After authorized selection, verify each predecessor prompt moved intact', 'After authorized selection, verify each predecessor prompt of a member that received a successor page moved intact'),
 ('It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the receiving role/session and work identifiers; carries every already-existing required artifact by exact identity/version and its repository path, or its direct Notion URL for a Notion-resident artifact; carries status, decisions, constraints, unresolved items, next action, and expected output; and contains no blanks, menus, or alternative destinations. Terminal results identify completion and the native Product Owner return.\n',
  '{C-HANDOFF} Terminal results identify completion and the native Product Owner return.\n'
  '- Every body whose registry row requires `NEXT_PROMPT_HANDOFF` carries, as the first sentence of its output section: {C-ART}\n'
  '- Every body whose registry row requires `NEXT_PROMPT_HANDOFF` carries, after its handoff rule: {C-PLACE}\n'),
 ('- GCFPE PR-30, same-session PR-35, interrupted PR recovery,', '- GCFPE PR-30, PR-35 in its own dedicated session, interrupted PR recovery,'),
 ('Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.\n- The exact ordered',
  'Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or any session beyond its own dedicated PR-35 session.\n- The exact ordered'),
 ('- {TEN}. Require PR-30', '- {NINE}. Require PR-30'),
 ('or unsupported platform limitation. PR-30 owns', 'or unsupported platform limitation. {LANDED} PR-30 owns'),
 ('ends with `PR_CANDIDATE_PUBLISHED` plus one complete same-session PR-35 handoff.', 'ends with `PR_CANDIDATE_PUBLISHED` plus one complete PR-35 handoff.'),
 ('- One Product Owner `Proceed` authorizes the single PR-30/PR-35 work unit through genuine merge readiness, not merge.',
  '- One Product Owner `Proceed` per plan cycle authorizes the PR-30/PR-35 work unit through genuine merge readiness, not merge. ' + T['C-PROCEED'].split('. ', 1)[1]),
 ('phase in the same session/workspace/worktree/branch/open PR/original Proceed.', "phase in the recorded phase's own session/workspace/worktree/branch/open PR/original Proceed."),
 ("- PR-35's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later invocation asserts only that Nathan manually merged the identified PR;",
  "- PR-35's `MERGE_PENDING` is historical pre-merge evidence. {C-DISPATCH} Nathan's later invocation, usable {FALLBACK}, asserts only that Nathan manually merged the identified PR;"),
 ('Never treat `MERGE_PENDING` as a current post-merge fact.\n', 'Never treat `MERGE_PENDING` as a current post-merge fact.\n- {INVARIANT}\n'),
])
A(AM + 'references/interoperability-contracts.md', [
 ('implementation/publication, same-session PR-35 review/readiness,', 'implementation/publication, PR-35 review/readiness,'),
 ('one selected PR-30 → PR-35 same-session phase continuation inside existing R1 row GCF-17; it adds no role, approval, authority transfer, Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.',
  'one selected PR-30 → PR-35 phase continuation inside existing R1 row GCF-17; it adds no role, approval, authority transfer, Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or any session beyond its own dedicated PR-35 session.'),
 ('- The handoff begins with the exact selected destination prompt name, version, and direct Notion URL and carries the actual receiving role/session, work identifiers, every already-existing required artifact by exact identity/version and its repository path or its direct Notion URL for a Notion-resident artifact, state, decisions, constraints, unresolved items, next action, and expected output.', '- {C-HANDOFF}'),
 ('plus exactly one complete same-session PR-35 handoff.', 'plus exactly one complete PR-35 handoff.'),
 ('{TEN}.', '{NINE}.'),
 ("PR-35's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later invocation asserts only a manual merge;",
  "PR-35's `MERGE_PENDING` is historical pre-merge evidence. {C-DISPATCH} Nathan's later invocation, usable {FALLBACK}, asserts only a manual merge;"),
 ('PR-30/PR-35 same-session skill/recovery', 'PR-30/PR-35 skill/recovery'),
])
A(AM + 'references/behavioral-fixtures.md', [
 ('{TEN}.', '{NINE}.'),
 ('with one complete same-session PR-35 handoff.', 'with one complete PR-35 handoff.'),
 ("separately require Nathan's later manual-merge assertion and PR-40's", "separately require Nathan's later manual-merge assertion, usable {FALLBACK}, and PR-40's"),
 ('- Require exact rescope return phase', '- Accept PR-40 entry on `MERGE_OBSERVED` only when the subscribed PR-35 session, or RS-40 resuming the PR-35 phase, observed through an active subscription the merge of the identified PR that Nathan performed, and Nathan pasted the handoff into a session he created; accept Nathan\'s manual-merge assertion {FALLBACK}. Reject an agent merge, automatic dispatch, an agent-created session, and PR-40 entry before any merge.\n'
  '- Accept a PR-40 `REJECT` for a precise in-scope defect in landed work only as a re-plan through PR-20 in a new top-level session Nathan creates, with a new plan and its own Proceed; a pull request merged under an earlier plan cycle is landed history. Reject that `REJECT` routed to PR-30, a second Proceed for the same plan, and a Proceed between PR-30 and PR-35.\n'
  '- Require exact rescope return phase'),
])
A(AM + 'references/project-prompt-registry-schema.md', [
 ('  session_class: DEDICATED_ONE_OFF | CHANGE_LIFETIME | ROLE_CONTINUING | ORCHESTRATOR_RUN\n', '  session_class: DEDICATED_ONE_OFF | CHANGE_LIFETIME | ROLE_CONTINUING | ORCHESTRATOR_RUN | DEDICATED_PR_REVIEW_SESSION\n'),
])
A(AM + 'scripts/run_fixture_suite.py', [
 ('EXACT_GCF17_CONTINUITY = "{TEN}"', 'EXACT_GCF17_CONTINUITY = "{NINE}"\nRETIRED_GCF17_CONTINUITY = "{TEN}"'),
 ('self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3", skill)', 'self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.12.0", skill)'),
 ('        self.assertIn(EXACT_GCF17_CONTINUITY, fixtures)\n', '        self.assertIn(EXACT_GCF17_CONTINUITY, fixtures)\n        for text in (skill, interoperability, fixtures):\n            self.assertNotIn(RETIRED_GCF17_CONTINUITY, text)\n'),
])
print('8a applied')
