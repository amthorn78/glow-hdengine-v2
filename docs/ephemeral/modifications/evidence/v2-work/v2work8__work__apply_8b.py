"""v2 §8b skill-text and skill-side literal edits (contract-side literals excluded: they move with §6's contract)."""
import sys, json
sys.dont_write_bytecode = True
from common import apply
from texts import T
def x(s):
    for k, v in T.items():
        s = s.replace('{' + k + '}', v)
    return s
root = sys.argv[1]
def A(rel, edits):
    return apply(root + '/' + rel, [(x(o), x(n)) for o, n in edits], rel)
FB = T['FALLBACK']
CF_RETIRED = [
 "one dedicated PR-development session", T['TEN'],
 "same-session PR-30 → PR-35 phase continuation", "same-session PR-35 handoff", "same-session PR-35 review/readiness",
 "same-session second phase", T['V5'],
 "historical pre-merge evidence; Nathan's later invocation asserts that Nathan manually merged",
 "A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred",
 "One dedicated session per planned PR work unit; the same session performs both",
 "has only the manual-merge-assertion meaning",
 "The same dedicated PR session implements only that work unit",
 "Only after Nathan later asserts that the identified PR was manually merged may that invocation run",
 "GCF-14 — Create one dedicated PR session for one planned PR work unit",
]
CF = [
 ('CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9', 'CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0'),
 ('or manual PF controls.\n\n### Runtime entry gate', 'or manual PF controls.\n\n{OVERRIDE}\n\n### Runtime entry gate'),
 ('- The policy for one dedicated PR-development session per planned PR work unit, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, same-session PR-35 review/readiness,',
  '- The policy for each planned PR work unit, run in two dedicated sessions, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, PR-35 review/readiness,'),
 ('evidence destination, and cleanup/recovery owner in the handoff.', 'evidence destination, and cleanup/recovery owner in the output artifact that the handoff names.'),
 ('a selected PR-35 is lawful only as the same-session second phase of the existing GCF-17 PR work unit.', 'a selected PR-35 is lawful only as the second phase of the existing GCF-17 PR work unit.'),
 ('It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the actual receiving role/session and change/work identifiers; provides every required artifact repository path; and carries current status, decisions, constraints, unresolved items, next action, and expected output.', '{C-HANDOFF}'),
 ('Terminal results state completion and the native Product Owner return.', 'Terminal results state completion and the native Product Owner return. {C-PLACE}'),
 ('PR-30 and PR-35 are two phases of that one work unit and retain one original Proceed, one dedicated PR-development session, one workspace/worktree, one branch, one pull request, one PR instruction and detailed Plan, one primary skill, and continuous recovery/artifact lineage.', '{C-SESSION}'),
 ('exactly one complete same-session PR-35 handoff;', 'exactly one complete PR-35 handoff to the dedicated PR-35 session;'),
 ('coherent corrective commits and pushes, CI economy, remote-head proof, and genuine merge readiness.\n', 'coherent corrective commits and pushes, CI economy, remote-head proof, and genuine merge readiness. {C-PROCEED}\n'),
 ('{TEN}', '{NINE}'),
 ('same-session continuation cannot add, omit,', 'continuation cannot add, omit,'),
 ('{V5}', '{V6}'),
 ('permits this one selected same-session PR-30 → PR-35 phase continuation inside GCF-17. It permits no extra role, approval, authority transfer, Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.',
  'permits this one selected PR-30 → PR-35 phase continuation inside GCF-17. It permits no extra role, approval, authority transfer, Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, or R1 row.'),
 ('it uses selected RS-40 to resume the recorded phase in the same session/workspace/worktree/branch/open PR under the original Proceed.',
  "it uses selected RS-40 to resume the recorded phase in that phase's own session, workspace/worktree, branch and open PR under the original Proceed."),
 ("PR-35's `MERGE_PENDING` is historical pre-merge evidence; Nathan's later invocation asserts that Nathan manually merged; PR-40 then independently verifies actual merged state and landed lineage read-only.",
  "PR-35's `MERGE_PENDING` is historical pre-merge evidence; {FALLBACK}, Nathan's later invocation asserts that Nathan manually merged; PR-40 then independently verifies actual merged state and landed lineage read-only. {C-DISPATCH}"),
 ("A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred; it is not a merge approval or merge instruction.",
  "Where the subscribed PR-35 session observed the merge, that event is the fact PR-40 is entered on; {FALLBACK}, Nathan's later PR-40 invocation asserts the manual merge; neither is a merge approval or instruction."),
 ('| Per-PR planning and implementation | One dedicated session per planned PR work unit; the same session performs both |',
  "| Per-PR planning and implementation | PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request. |"),
 ('has only the manual-merge-assertion meaning defined above;', 'has only the meaning defined above;'),
 ('- GCF-14 — Create one dedicated PR session for one planned PR work unit.', '- GCF-14 — Nathan creates one dedicated top-level PR session for one planned PR work unit.'),
 ('GCF-17 — The same dedicated PR session implements only that work unit across selected PR-30 and PR-35, validates it, and creates exactly one active branch and pull request.',
  "GCF-17 — The dedicated PR session (PR-30 phase) and the dedicated PR-35 session (PR-35 phase) implement only that work unit across selected PR-30 and PR-35, validate it, and create exactly one active branch and pull request. PR-35: its own dedicated top-level session for the same work unit and pull request, entered from PR-30's handoff; never a subagent of another session."),
 ('Only after Nathan later asserts that the identified PR was manually merged may that invocation run.',
  'Only after Nathan has manually merged the identified PR, and {FALLBACK}, may that invocation run; where the subscribed PR-35 session observed the merge, PR-35 returns `MERGE_OBSERVED` with the paste-ready PR-40 handoff.'),
 ('This is the single authoritative work-unit acceptance route; an attribution bundle is evidence only.',
  'This is the single authoritative work-unit acceptance route; an attribution bundle is evidence only. A precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed (GCF-14).'),
 ('Load [GCFPE current direct-handoff contract](references/gcfpe-current-direct-handoff-contract.json) as the current specialization overlay.',
  'Load [GCFPE current direct-handoff contract](references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json) as the current specialization overlay.'),
 ('The bundled `gcfpe-20260913.1-091326.2`, `gcfpe-20260913.1`, and `gcfpe-20260912.2` direct-handoff contracts are superseded candidate records',
  'The bundled `gcfpe-current-direct-handoff-contract.json` alias (091326.2), `gcfpe-20260913.1-091326.2`, `gcfpe-20260913.1`, and `gcfpe-20260912.2` direct-handoff contracts are superseded candidate records'),
 ('Three of these files share `contract_id` `GCFPE-PF10-INTEGRITY-20260913.1` with the current contract above; that identifier resolves for current execution to `gcfpe-current-direct-handoff-contract.json` alone, which carries `status: SELECTED_PRODUCTION`.',
  'Three of these files share `contract_id` `GCFPE-PF10-INTEGRITY-20260913.1`; that identifier no longer names the current overlay. The current overlay is the 091426.1 contract above, `contract_id` `GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED`, which carries `status: SELECTED_PRODUCTION`.'),
]
CF.append(('The older integrated-readiness, final-scan,', 'The historical 46-row runtime map `glow-hde-canonical-change-flow-r1-runtime-map.json` (SHA-256 `5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e`) remains immutable historical provenance, checked by its historical pins. The older integrated-readiness, final-scan,'))
A('change-flow/SKILL.md', CF)
loop = "    for text in (\n" + "".join("        " + json.dumps(p, ensure_ascii=False) + ",\n" for p in CF_RETIRED) + \
       "    ):\n        require(text.lower() not in skill.lower(), f\"retired skill clause present: {text}\")\n\n"
A('change-flow/scripts/validate_gcfpe_20260914.py', [
 ('require("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9" in skill, "specialization revision")', 'require("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0" in skill, "specialization revision")'),
 ('        ' + json.dumps(T['TEN']) + ',\n        "one dedicated PR-development session",\n',
  '        ' + json.dumps(T['NINE']) + ',\n        "run in two dedicated sessions",\n        "never as a subagent, forked agent or workflow agent of PR-30",\n        "no session is created by an agent",\n        "One Proceed per approved per-PR plan",\n        "It carries no branch and no commit",\n'),
 ('        require(text in skill, f"missing skill clause: {text}")\n\n', '        require(text in skill, f"missing skill clause: {text}")\n\n' + loop),
])
# relay
RL = [
 ('`SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.0.0`', '`SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0`'),
 ('When a required participant does not exist or cannot be confirmed reachable, return `SESSION_PROVISIONING_REQUIRED` for Session Branch Flowmaster. Do not silently create a replacement.\n\n### Cross-skill contracts and shared state',
  'Outside a GCFPE main-ecosystem stage, when a required participant does not exist or cannot be confirmed reachable, return `SESSION_PROVISIONING_REQUIRED` for Session Branch Flowmaster. Do not silently create a replacement. {W9}\n\n{OVERRIDE}\n\n### Cross-skill contracts and shared state'),
 ('For every GCFPE reusable prompt and temporary repair/review/handoff prompt,', 'For every GCFPE reusable prompt and temporary repair/review prompt,'),
 ('This prompt-locator rule does not ban API URLs, tool parameters or actual identity evidence outside prompt text.\n',
  'This prompt-locator rule does not ban API URLs, tool parameters or actual identity evidence outside prompt text. Runtime handoffs may name versioned files; reusable prompt text stays versionless.\n'),
 ('- Notion is the preferred live control plane for current task, assignment, dependency, decision, and handoff state.', '- {STEP2}.'),
 ('cleanup/recovery owner in the existing handoff.', 'cleanup/recovery owner in the output artifact that the handoff names.'),
 ("Deliver every concrete routed handoff in the final user-facing response itself: target actor and session continuity, exact task-bound advice or limitation, named file references the recipient can resolve itself, and a populated copyable invocation with the selected prompt's native inputs and actual prerequisites. For a Notion prompt use its versionless name and verified directory; approved runtime versions remain input lineage.",
  'Deliver every concrete routed handoff in the final user-facing response itself. {C-HANDOFF} {C-PLACE}'),
 ('PR-30 finishes recovery, implementation, local testing and deliberate initial publication, returns PR_CANDIDATE_PUBLISHED with exactly one complete same-session PR-35 handoff,',
  '{C-SESSION} PR-30 finishes recovery, implementation, local testing and deliberate initial publication, returns PR_CANDIDATE_PUBLISHED with exactly one complete PR-35 handoff to the dedicated PR-35 session,'),
 ('PR-35 supplies the actual populated PR-40 handoff conditional on merge.', '{C-DISPATCH}'),
 ("The Product Owner's PR-40 invocation supplies merge approval without a separate confirmation or approval artifact; it never authorizes an agent merge,",
  "The Product Owner's PR-40 invocation is not a merge approval or merge instruction; it never authorizes an agent merge,"),
 ('Return a populated same-session resume of the recorded PR phase after the actual merge,', "Return a populated resume of the recorded PR phase in the recorded phase's own session after the actual merge,"),
 ('Bind `update_control_record` to `SHARED_STATE.CONTROL_PLANE: NOTION` and an exact Notion page URL in `LEDGER_DESTINATION`; version 1 cannot represent that binding and must migrate to version 2.',
  'Bind `update_control_record` to `SHARED_STATE.CONTROL_PLANE: NOTION` and an exact Notion page URL in `LEDGER_DESTINATION`; version 1 cannot represent that binding and must migrate to version 2. {S7}'),
 ('4. `NOTION_REFERENCE`: a versionless resource name plus its verified directory path, resolved by the recipient at execution under the prompt-locator rule above.',
  '4. `NOTION_REFERENCE`: a versionless resource name plus its verified directory path, resolved by the recipient at execution under the prompt-locator rule above. {S6}'),
 ('This specialization cannot create a session. When a required participant does not exist, return `SESSION_PROVISIONING_REQUIRED` and stop:',
  'This specialization cannot create a session. Outside a GCFPE main-ecosystem stage, when a required participant does not exist, return `SESSION_PROVISIONING_REQUIRED` and stop:'),
]
rs = A('session-relay-flowmaster/SKILL.md', RL)
rl = rs.split('\n')
def rline(prefix):
    c = [l for l in rl if l.startswith(prefix)]
    assert len(c) == 1, prefix; return c[0]
tw = open(root + '/tw-flowmaster/SKILL.md', encoding='utf-8').read()
twl = tw.split('\n')
assert twl[303].startswith('For every GCFPE reusable prompt') and twl[314].startswith('For GCFPE, assess or preserve advice')
assert twl[318].startswith('PR-30 finishes recovery') and twl[320].startswith('If later approved engineering')
twl[303] = rline('For every GCFPE reusable prompt'); twl[314] = rline('For GCFPE, assess or preserve advice')
twl[318] = rline(T['C-SESSION'][:40]); twl[320] = rline('If later approved engineering')
open(root + '/tw-flowmaster/SKILL.md', 'w', encoding='utf-8').write('\n'.join(twl))
A('tw-flowmaster/SKILL.md', [
 ('`TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.1.6`', '`TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0`'),
 ('### GCFPE binding\n\n', '### GCFPE binding\n\n{OVERRIDE}\n\n'),
 ('Add result artifact/PR/commit references when observed;', 'Add result artifact/PR/commit references to the usage record when observed, never to the handoff;'),
])
# flowmaster-validate
FORB4 = ['"same-session PR-35 handoff",', '"preferred live control plane",', '"launched as a new session",', '"The Product Owner\'s PR-40 invocation supplies merge approval",']
A('flowmaster-validate/scripts/validate_flowmaster.py', [
 ('"TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.1.6",', '"TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0",\n        ' + json.dumps(T['OVERRIDE']) + ',\n        ' + json.dumps(T['A18']) + ','),
 ('        "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9",\n        "GLOW_HDE_CANONICAL', '        "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0",\n        ' + json.dumps(T['OVERRIDE']) + ',\n        "GLOW_HDE_CANONICAL'),
 ('"SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.0.0",', '"SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0",\n        ' + json.dumps(T['OVERRIDE']) + ',\n        ' + json.dumps(T['A18']) + ','),
 ('            "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9",\n', '            "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0",\n'),
 ('        "session_control_timeout_seconds = [[",\n    ),', '        "session_control_timeout_seconds = [[",\n' + ''.join('        ' + f + '\n' for f in FORB4) + '    ),'),
 ('        "attach the file to the message",\n    ),', '        "attach the file to the message",\n' + ''.join('        ' + f + '\n' for f in FORB4) + '    ),'),
 ('        "references/gcfpe-current-direct-handoff-contract.json",\n    },', '        "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",\n    },'),
 ('            "validator_revision": "3.2.14",', '            "validator_revision": "3.3.0",'),
 ('                str(change_dir / "references" / "gcfpe-current-direct-handoff-contract.json"),', '                str(change_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"),'),
])
A('flowmaster-validate/scripts/validate_gcfpe_current.py', [
 ('    contract_path = contract_path or change_skill_dir / "references" / "gcfpe-current-direct-handoff-contract.json"\n    if not contract_path.is_file():',
  '    contract_path = contract_path or change_skill_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"\n    if not contract_path.is_file():'),
 ('    if skill_text.count("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9") != 1:\n        errors.append("ACTIVE_CONTRACT_MISSING:CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9")',
  '    if skill_text.count("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0") != 1:\n        errors.append("ACTIVE_CONTRACT_MISSING:CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0")'),
 ('            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5",\n            "## Recover before creating work", "one dedicated PR-development session", "RS-40", "PR-50",',
  '            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0",\n            "## Recover before creating work", "run in two dedicated sessions", "RS-40", "PR-50",'),
])
A('flowmaster-validate/scripts/run_gcfpe_current_fixtures.py', [
 ('    contract_path = contract_path or change_skill_dir / "references" / "gcfpe-current-direct-handoff-contract.json"\n    source = json.loads',
  '    contract_path = contract_path or change_skill_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"\n    source = json.loads'),
 ('        "validator_revision": "3.2.14",', '        "validator_revision": "3.3.0",') if False else ('', ''),
][:1])
A('flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json', [
 ('"change-flow": "3.2.9",', '"change-flow": "3.3.0",'),
 ('"glow-hde-pr-development": "1.2.5"', '"glow-hde-pr-development": "1.3.0"'),
 ('"validator_revision": "3.2.14"', '"validator_revision": "3.3.0"'),
])
A('flowmaster-validate/scripts/validate_gcfpe_20260914.py', [
 ('            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5", "REMOTE_EVIDENCE_PENDING",', '            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0", "REMOTE_EVIDENCE_PENDING",'),
 ('            ' + json.dumps(T['TEN']) + ',\n', '            ' + json.dumps(T['NINE']) + ',\n'),
 ('        "validator_revision": "3.2.14",', '        "validator_revision": "3.3.0",'),
 ('    # option: a file would persist, and a persisted corpus is what the policy forbids.  Supply', '    # option: {C-D22}.  Supply'),
])
A('flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py', [
 ('No path option: a file would persist.', 'No path option: {C-D22}.'),
 ('        "validator_revision": "3.2.14",', '        "validator_revision": "3.3.0",'),
])
FV = [
 ('FLOWMASTER_VALIDATE_REVISION: 3.2.16', 'FLOWMASTER_VALIDATE_REVISION: 3.3.0'),
 ('deliberately with no path option, because a file persists --', 'deliberately with no path option, because {C-D22} --'),
 ('The 20260914 candidate contract revision 4.0.6 binds', 'The 20260914 candidate contract revision 4.1.0 binds'),
 ('The selected alias `references/gcfpe-current-direct-handoff-contract.json` must match that live binding.',
  'The current overlay `references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json` must match that live binding; the `gcfpe-current-direct-handoff-contract.json` alias is historical provenance and no longer a validation default.'),
 ('- PR-30 and PR-35 are two phases of one GCF-17 PR work unit. {TEN}. Both phases share exactly one value for every field. PR-35 adds zero roles, sessions, approvals, gates, Proceeds, work units, R1 rows, merge authority, work vehicles, or cross-session routes.',
  '- {C-SESSION} {NINE}. Both phases share exactly one value for every field. PR-35 adds zero roles, approvals, gates, Proceeds, work units, R1 rows, merge authority, or work vehicles.'),
 ('coherent commits, deliberate initial publication, and its same-session PR-35 handoff.', 'coherent commits, deliberate initial publication, and its PR-35 handoff.'),
 ('The exact PR-35 results are `MERGE_PENDING`, `RESCOPE_PENDING`,', 'The exact PR-35 results are `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,'),
 ("PR-35 `MERGE_PENDING` is historical pre-merge evidence; Nathan's later invocation asserts the manual merge; PR-40 independently verifies actual merged state and landed lineage read-only.",
  "PR-35 `MERGE_PENDING` is historical pre-merge evidence; {FALLBACK}, Nathan's later invocation asserts the manual merge; PR-40 independently verifies actual merged state and landed lineage read-only. {C-DISPATCH}"),
 ('The versioned 33-case section-13 fixture suite', 'The versioned 37-case section-13 fixture suite'),
 ('the TW specialization revision is 1.1.6 (including', 'the TW specialization revision is 1.2.0 (including'),
 ('There is no path option and there will not be one: a file persists, and\na persisted corpus is what the policy forbids.', 'There is no path option and there will not be one: {C-D22}.'),
 ('12. One dedicated PR session plans and implements one work unit.', "12. PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request."),
 ('During candidate staging, the suite validates the selected 54-member `GCFPE-20260913.1 / 091326.2` alias and its predecessor fixtures first.',
  'By default the suite validates the 091426.1 current overlay and its schema-4 fixtures; the 54-member `GCFPE-20260913.1 / 091326.2` alias is validated only when passed explicitly.'),
 ('and all 33 section-13 fixtures.', 'and all 37 section-13 fixtures.'),
 ('The fixture report separates 33 required fixture IDs,', 'The fixture report separates 37 required fixture IDs,'),
 ('resumes the recorded phase in the same session/worktree/branch/open PR under the original Proceed.', "resumes the recorded phase in that phase's own session, worktree, branch and open PR under the original Proceed."),
]
A('flowmaster-validate/SKILL.md', FV)
print('8b applied')
