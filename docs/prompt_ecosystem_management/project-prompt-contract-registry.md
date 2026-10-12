# Project Prompt Contract Registry — GCFPE-20261009.1 / 100926.1

artifact_type: `PROJECT_PROMPT_CONTRACT_REGISTRY`  
status: `APPROVED`  
approved_by: `Nathan / Product Owner`  
approved_at: `2026-10-12`  
release: `GCFPE-20261009.1 / 100926.1 / 55`  
home: `docs/prompt_ecosystem_management/`  
supersedes: `GCFPE-PCR-20260914.1` (APPROVED, 091426.1 / 55), replaced in this file by MODIFICATION-20261011-gcfpe-mb008-to-promotion; its text stays in this file's history on `main`

```yaml
schema_version: project-prompt-contract-registry/1.0
registry_id: GCFPE-PCR-20261009.1
project_id: glow-hde
status: APPROVED
approved_by: Nathan / Product Owner
approved_at: '2026-10-12'
workspace_skill_registry_id: WSR-20260914.1-OBSERVATIONAL
workspace_skill_registry_disposition: Evidence only. That registry is DRAFT, unapproved, and self-classified
  INVENTORY_EVIDENCE_NOT_APPROVED_EXPECTED_STATE, observed from a checkout absent from this environment.
  It confers no skill lifecycle on this approved registry. Its glow-hde-devops row is a dated observation
  and is preserved unedited; that skill is retired by D16, which is the authority for its disposition,
  and the forbidden literal on all 55 rows below is correct.
authority_sources:
- type: SELECTED_RELEASE_REGISTER
  release: GCFPE-20261009.1
  url: https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1
- type: SELECTED_CATALOG
  version_family: '100926.1'
  member_count: 55
  url: https://app.notion.com/p/3f74590a05eb812db385c2544d7570f7
observation:
  release: GCFPE-20261009.1
  version_family: '100926.1'
  selected_member_count: 55
  complete_body_count: 55
  mutation_posture: READ_ONLY
lanes:
- lane: GCFPE-MGMT
  title: GCFPE management
  notion_parent_id: 3db4590a05eb81de9736ea69bac61016
  notion_parent_title: Glow HDE Prompt Flow Index — GCFPE-20261009.1 — 100926.1
  active: true
- lane: CF-PO
  title: Product Owner change-class selection
  notion_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  notion_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  active: true
- lane: CF-C
  title: CRD specification
  notion_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  notion_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  active: true
- lane: CF-E
  title: Epic specification
  notion_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  notion_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  active: true
- lane: CL-C
  title: CRD closure
  notion_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  notion_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  active: true
- lane: CL-E
  title: Epic closure and PF09 maintenance
  notion_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  notion_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  active: true
- lane: CL
  title: Shared closure administration
  notion_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  notion_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  active: true
- lane: DOC
  title: Repository documentation
  notion_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  notion_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  active: true
- lane: ESC
  title: Escalation and remediation
  notion_parent_id: 3db4590a05eb81cd938de84cfffead9c
  notion_parent_title: Escalation — GCFPE-20261009.1 — 100926.1
  active: true
- lane: IA
  title: Whole-change implementation audit and plan
  notion_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  notion_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  active: true
- lane: MGR
  title: Optional flow coordination
  notion_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  notion_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  active: true
- lane: OPS
  title: Bounded operations
  notion_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  notion_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  active: true
- lane: PR
  title: PR work-unit development
  notion_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  notion_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  active: true
- lane: QA
  title: Whole-change QA
  notion_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  notion_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  active: true
- lane: RS
  title: Bounded rescope
  notion_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  notion_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  active: true
- lane: UTIL
  title: Exact redline utility
  notion_parent_id: 3db4590a05eb811b9c14f2ae89c28df7
  notion_parent_title: HDE TW — GCFPE-20261009.1 — 100926.1
  active: true
prompts:
- prompt_key: CF-C-10
  notion_page_id: 3f44590a05eb810f83d4d539e5b0e588
  notion_url: https://app.notion.com/p/3f44590a05eb810f83d4d539e5b0e588
  expected_title: CF-C-10 — Prepare CRD Specification Kickoff Handoff — 100926.1
  lane: CF-C
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Prepare CRD Specification Kickoff Handoff for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are Master Scrum in the class-specific kickoff session.
  creator_role: Master Scrum in the class-specific kickoff session.
  reviewer_role: NONE
  inputs:
  - CLASS_SELECTION_REF
  - SOURCE_REF
  - PO_CONTEXT_REF
  outputs:
  - artifact: SPECIFICATION_KICKOFF
    states:
    - BLOCKED
    - KICKOFF_READY
    consumers: &id001
    - CF-C-20
    - CF-E-10
    - CF-PO-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id001
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb810f83d4d539e5b0e588?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8119a5a8e4d083fcf360?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb810f83d4d539e5b0e588?pvs=204
    page_last_edited_at: '2026-10-12T02:29:03.544Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: recovery package carries the original CLASS_SELECTION_REF|UNRESOLVED_CLASSIFICATION_CASE
        with the preserved source/change facts
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CF-C-20
  notion_page_id: 3f44590a05eb81a7a944f19bd9a2e3de
  notion_url: https://app.notion.com/p/3f44590a05eb81a7a944f19bd9a2e3de
  expected_title: CF-C-20 — Create CRD Specification — 100926.1
  lane: CF-C
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Create CRD Specification for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, the continuing Lead Developer and Specification author.
  creator_role: Isis, the continuing Lead Developer and Specification author.
  reviewer_role: Thoth / Head of Development
  inputs:
  - KICKOFF_HANDOFF_ID
  outputs:
  - artifact: CRD_SPECIFICATION
    states:
    - BLOCKED
    - SPECIFICATION_PENDING
    consumers: &id002
    - CF-C-10
    - CF-C-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id002
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81a7a944f19bd9a2e3de?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8173a73edc73f302a90a?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81a7a944f19bd9a2e3de?pvs=204
    page_last_edited_at: '2026-10-12T02:29:09.414Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: direct package contains the exact pending Specification, class/change lineage|recovery carries
        the original kickoff link, exact defect, class/change lineage
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CF-C-30
  notion_page_id: 3f44590a05eb8121af3bf2249c6d6ca8
  notion_url: https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8
  expected_title: CF-C-30 — Review and Approve CRD Specification — 100926.1
  lane: CF-C
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Review and Approve CRD Specification for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Thoth, Head of Development, in the same continuing review session for this change.
  creator_role: Thoth, Head of Development, in the same continuing review session for this change.
  reviewer_role: NONE
  inputs:
  - SPECIFICATION_ID
  outputs:
  - artifact: INITIAL_SPECIFICATION_REVIEW / SPECIFICATION_DELTA_REVIEW
    states:
    - CORRECTION_REDLINE
    - DELTA_APPROVE
    - DELTA_DENY
    - INITIAL_APPROVE
    - INITIAL_DENY
    consumers: &id003
    - CF-C-40
    - IA-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id003
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8149a8d2ed42c9c01ffd?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8?pvs=204
    page_last_edited_at: '2026-10-12T02:29:05.619Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: and approval lineage, the carried conflict register
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)^(?!.*(?i:\bnonterminal\b))(?=.*(?:DELTA_APPROVE))(?=.*(?i:\bterminal(ly)?\b|\bno (runnable
        )?continuation\b|\bemit no\b))
      guard: G-F03-A
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?i:Outside GCFPE\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-A
    - rule_id: CTR-001
      value: (?m)^(?=.*(?i:format recorded in the Glow Operations Hub|one `##` heading carrying its title|canonical
        PF10 build-notes addendum format))
      guard: G-F05-B
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)^(?=.*(?:DELTA_APPROVE))(?=.*(?i:\bnonterminal\b))(?=.*(?i:exactly one complete continuation
        block))(?=.*(?i:return (phase|point)))
      guard: G-F03-B
    - rule_id: CTR-002
      value: (?m)^(?=.*(?i:one H2 heading with the next continuous number))(?=.*(?:PF06-Canon-Change-Process-Guide))(?=.*(?:PF27-Canon-Plan-Templates))(?=.*(?i:only
        H3 or lower))
      guard: G-F05-C
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CF-C-40
  notion_page_id: 3f44590a05eb81458686cc39d8d98b2a
  notion_url: https://app.notion.com/p/3f44590a05eb81458686cc39d8d98b2a
  expected_title: CF-C-40 — Revise CRD Specification — 100926.1
  lane: CF-C
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Revise CRD Specification for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, the same continuing Specification author.
  creator_role: Isis, the same continuing Specification author.
  reviewer_role: Thoth / Head of Development
  inputs:
  - SPECIFICATION_DELTA
  outputs:
  - artifact: CRD_SPECIFICATION / SPECIFICATION_DELTA
    states:
    - SPECIFICATION_PENDING
    consumers: &id004
    - CF-C-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id004
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81458686cc39d8d98b2a?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81269931cee342ce8a0e?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81458686cc39d8d98b2a?pvs=204
    page_last_edited_at: '2026-10-12T02:29:18.974Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: actual mode, class/change/base lineage
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CF-E-10
  notion_page_id: 3f44590a05eb81129b09cddebcc18458
  notion_url: https://app.notion.com/p/3f44590a05eb81129b09cddebcc18458
  expected_title: CF-E-10 — Prepare Epic Specification Kickoff Handoff — 100926.1
  lane: CF-E
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Prepare Epic Specification Kickoff Handoff for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are Master Scrum in the class-specific kickoff session.
  creator_role: Master Scrum in the class-specific kickoff session.
  reviewer_role: NONE
  inputs:
  - CLASS_SELECTION_REF
  - SOURCE_REF
  - PO_CONTEXT_REF
  outputs:
  - artifact: SPECIFICATION_KICKOFF
    states:
    - BLOCKED
    - KICKOFF_READY
    consumers: &id005
    - CF-C-10
    - CF-E-20
    - CF-PO-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id005
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81129b09cddebcc18458?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb815b84a5c5a5ace85fe1?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81129b09cddebcc18458?pvs=204
    page_last_edited_at: '2026-10-12T02:29:06.412Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: recovery package carries the original CLASS_SELECTION_REF|UNRESOLVED_CLASSIFICATION_CASE
        with the preserved source/change facts
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CF-E-20
  notion_page_id: 3f44590a05eb813cb9cbc61c225b88e2
  notion_url: https://app.notion.com/p/3f44590a05eb813cb9cbc61c225b88e2
  expected_title: CF-E-20 — Create Epic Specification — 100926.1
  lane: CF-E
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Create Epic Specification for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, the continuing Lead Developer and Specification author.
  creator_role: Isis, the continuing Lead Developer and Specification author.
  reviewer_role: Thoth / Head of Development
  inputs:
  - KICKOFF_HANDOFF_ID
  outputs:
  - artifact: EPIC_SPECIFICATION
    states:
    - BLOCKED
    - SPECIFICATION_PENDING
    consumers: &id006
    - CF-E-10
    - CF-E-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id006
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb813cb9cbc61c225b88e2?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb810eb177f7dced41bc8f?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb813cb9cbc61c225b88e2?pvs=204
    page_last_edited_at: '2026-10-12T02:29:12.283Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: direct package contains the exact pending Specification, class/change lineage|recovery carries
        the original kickoff link, exact defect, class/change lineage
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CF-E-30
  notion_page_id: 3f44590a05eb8104824fe084354a0ef8
  notion_url: https://app.notion.com/p/3f44590a05eb8104824fe084354a0ef8
  expected_title: CF-E-30 — Review and Approve Epic Specification — 100926.1
  lane: CF-E
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Review and Approve Epic Specification for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Thoth, Head of Development, in the same continuing review session for this change.
  creator_role: Thoth, Head of Development, in the same continuing review session for this change.
  reviewer_role: NONE
  inputs:
  - SPECIFICATION_ID
  outputs:
  - artifact: INITIAL_SPECIFICATION_REVIEW / SPECIFICATION_DELTA_REVIEW
    states:
    - CORRECTION_REDLINE
    - DELTA_APPROVE
    - DELTA_DENY
    - INITIAL_APPROVE
    - INITIAL_DENY
    consumers: &id007
    - CF-E-40
    - IA-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id007
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8104824fe084354a0ef8?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81b4be79f405566da9a7?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8104824fe084354a0ef8?pvs=204
    page_last_edited_at: '2026-10-12T02:29:08.639Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: and approval lineage, the carried conflict register
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)^(?!.*(?i:\bnonterminal\b))(?=.*(?:DELTA_APPROVE))(?=.*(?i:\bterminal(ly)?\b|\bno (runnable
        )?continuation\b|\bemit no\b))
      guard: G-F03-A
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?i:Outside GCFPE\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-A
    - rule_id: CTR-001
      value: (?m)^(?=.*(?i:format recorded in the Glow Operations Hub|one `##` heading carrying its title|canonical
        PF10 build-notes addendum format))
      guard: G-F05-B
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)^(?=.*(?:DELTA_APPROVE))(?=.*(?i:\bnonterminal\b))(?=.*(?i:exactly one complete continuation
        block))(?=.*(?i:return (phase|point)))
      guard: G-F03-B
    - rule_id: CTR-002
      value: (?m)^(?=.*(?i:one H2 heading with the next continuous number))(?=.*(?:PF06-Canon-Change-Process-Guide))(?=.*(?:PF27-Canon-Plan-Templates))(?=.*(?i:only
        H3 or lower))
      guard: G-F05-C
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CF-E-40
  notion_page_id: 3f44590a05eb81f1994df5f6ab3a7f32
  notion_url: https://app.notion.com/p/3f44590a05eb81f1994df5f6ab3a7f32
  expected_title: CF-E-40 — Revise Epic Specification — 100926.1
  lane: CF-E
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Revise Epic Specification for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, the same continuing Specification author.
  creator_role: Isis, the same continuing Specification author.
  reviewer_role: Thoth / Head of Development
  inputs:
  - SPECIFICATION_DELTA
  outputs:
  - artifact: EPIC_SPECIFICATION / SPECIFICATION_DELTA
    states:
    - SPECIFICATION_PENDING
    consumers: &id008
    - CF-E-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id008
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81f1994df5f6ab3a7f32?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8101b655ed223b11a85e?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81f1994df5f6ab3a7f32?pvs=204
    page_last_edited_at: '2026-10-12T02:29:22.102Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: actual mode, class/change/base lineage
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CF-PO-10
  notion_page_id: 3f44590a05eb81f9bf84f4585d9f7a2c
  notion_url: https://app.notion.com/p/3f44590a05eb81f9bf84f4585d9f7a2c
  expected_title: CF-PO-10 — Record Product Owner Change-Class Selection — 100926.1
  lane: CF-PO
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Record Product Owner Change-Class Selection for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the recording assistant in the Product Owner context.
  creator_role: the recording assistant in the Product Owner context.
  reviewer_role: NONE
  inputs:
  - CHANGE_ID
  - CHANGE_CLASS
  - EPIC
  - CRD
  outputs:
  - artifact: CHANGE_CLASS_SELECTION
    states:
    - CLASS_SELECTED
    consumers: &id009
    - CF-C-10
    - CF-E-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id009
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81f9bf84f4585d9f7a2c?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8161b4d7cb6d07f5101c?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81f9bf84f4585d9f7a2c?pvs=204
    page_last_edited_at: '2026-10-12T02:29:09.502Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CL-20
  notion_page_id: 3f44590a05eb81739b57da57c285f45d
  notion_url: https://app.notion.com/p/3f44590a05eb81739b57da57c285f45d
  expected_title: CL-20 — Prepare Closure Memo and Post-Closure Record — 100926.1
  lane: CL
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Prepare Closure Memo and Post-Closure Record for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, after the positive terminal closure decision.
  creator_role: Isis, after the positive terminal closure decision.
  reviewer_role: NONE
  inputs:
  - CHANGE_CLOSURE_DECISION_ID
  - CLOSE
  outputs:
  - artifact: CLOSURE_MEMO / POST_CLOSURE_RECORD
    states:
    - POST_CLOSURE_PENDING
    consumers: &id010
    - CL-30
    - CL-40
    - CL-E-20
    - CL-E-30
    - CL-E-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - Carry existing closure canon basis and actual memo-source reads without a new closure decision.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id010
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81739b57da57c285f45d?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81f4812be61e8877c02c?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81739b57da57c285f45d?pvs=204
    page_last_edited_at: '2026-10-12T02:29:16.766Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: lineage into its result and handoff\b
    - rule_id: TOP-001
      value: Carry the positive closure decision, complete post-closure results
    - rule_id: TOP-001
      value: carrying the exact qualified condition, lineage, evidence
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Use only the read-only tools, stores, repository access[^.\n]*\.(?! Every statement in this
        prompt that it is read-only or does not change the repository excludes its own output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: CTR-001
      value: These candidate URL tokens must be replaced
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\bdo not include\b(?! in the block)))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:model/strength/reasoning))
      guard: G-CL-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: controlled Markdown
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: PF10/addendum lineage into its result artifact, which the handoff names
    - rule_id: CTR-002
      value: Name the positive closure decision and every post-closure result artifact by repository path
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: that entry creates no runtime approval
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: when none is supplied, record the board update as pending, owned under PF04 §9\.1\.1
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:The producer never edits PF10 or claims canonical adoption;
        it resolves the addendum's number from the current controlled PF10 at creation\.))
      guard: G-F05-F
- prompt_key: CL-30
  notion_page_id: 3f44590a05eb816ea12febba885940e8
  notion_url: https://app.notion.com/p/3f44590a05eb816ea12febba885940e8
  expected_title: CL-30 — Prepare Conditional Post-Change ADR Maintenance — 100926.1
  lane: CL
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Prepare Conditional Post-Change ADR Maintenance for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the explicitly assigned architecture documentation author.
  creator_role: the explicitly assigned architecture documentation author.
  reviewer_role: NONE
  inputs:
  - CHANGE_CLOSURE_DECISION_ID
  outputs:
  - artifact: ADR_CANDIDATE / NO_ADR_NEEDED
    states:
    - ADR_CANDIDATE
    - NO_ADR_NEEDED
    consumers: &id011
    - CL-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id011
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb816ea12febba885940e8?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8190a444d8818e445c1d?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb816ea12febba885940e8?pvs=204
    page_last_edited_at: '2026-10-12T02:29:13.172Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: lineage into its result and handoff\b
    - rule_id: TOP-001
      value: Carry the positive closure decision, complete post-closure results
    - rule_id: TOP-001
      value: Carry the complete candidate, positive closure and architecture-decision lineage
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Use only the read-only tools, stores, repository access[^.\n]*\.(?! Every statement in this
        prompt that it is read-only or does not change the repository excludes its own output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: CTR-001
      value: These candidate URL tokens must be replaced
    - rule_id: TOP-001
      value: decision lineage; existing ADR/conflict history
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\bdo not include\b(?! in the block)))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:model/strength/reasoning))
      guard: G-CL-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: controlled Markdown
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: PF10/addendum lineage into its result artifact, which the handoff names
    - rule_id: CTR-002
      value: Name the positive closure decision and every post-closure result artifact by repository path
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: that entry creates no runtime approval
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:The producer never edits PF10 or claims canonical adoption;
        it resolves the addendum's number from the current controlled PF10 at creation\.))
      guard: G-F05-F
- prompt_key: CL-40
  notion_page_id: 3f44590a05eb8155934dd1c4c2b5d1eb
  notion_url: https://app.notion.com/p/3f44590a05eb8155934dd1c4c2b5d1eb
  expected_title: CL-40 — Scan for PF09 Gaps and CRD Candidates — 100926.1
  lane: CL
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Scan for PF09 Gaps and CRD Candidates for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the same continuing Isis Lead Developer for the exact closed Epic or CRD change.
  creator_role: the same continuing Isis Lead Developer for the exact closed Epic or CRD change.
  reviewer_role: NONE
  inputs:
  - CHANGE_CLASS
  - CHANGE_ID
  - CHANGE_CLOSURE_DECISION_ID
  - POST_CLOSURE_CONTEXT_REFS
  - ADDITIONAL_CONTEXT_REFS
  - CYCLE_GAP_SCAN_ID
  - EXECUTION_POSTURE
  - MANUAL_PROMPT_EXECUTION
  - AUTOMATED_ORCHESTRATION
  outputs:
  - artifact: CYCLE_GAP_SCAN
    states:
    - COMPLETE
    - INCOMPLETE
    consumers: &id012 []
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    - Update the Notion page Candidate CRD Items List in place with this change's new CRD candidates,
      and no other Notion page; that page is the list's only store, named by a destination rule
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id012
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8155934dd1c4c2b5d1eb?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81db9c88cde6027e07bf?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8155934dd1c4c2b5d1eb?pvs=204
    page_last_edited_at: '2026-10-12T02:29:26.600Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: lineage into its result and handoff\b
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: It does not edit Canonical PF09, PF10, Canon, a board, registry, repository[^.\n]*\.(?! Every
        statement in this prompt that it is read-only or does not change the repository excludes its own
        output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: These candidate URL tokens must be replaced
    - rule_id: CTR-001
      value: This authoring candidate does not perform that update
    - rule_id: CTR-001
      value: \{\{CANDIDATE_CRD_LIST_URL\}\}
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\bdo not include\b(?! in the block)))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:model/strength/reasoning))
      guard: G-CL-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: PF10/addendum lineage into its result artifact, which the handoff names
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: Notion page `?Candidate CRD Items List`? \(`?https://app\.notion\.com/p/[0-9a-f]{32}(?:\?pvs=\d+)?`?\)
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:The producer never edits PF10 or claims canonical adoption;
        it resolves the addendum's number from the current controlled PF10 at creation\.))
      guard: G-F05-F
- prompt_key: CL-C-10
  notion_page_id: 3f44590a05eb819b8022f2a4cdd3b022
  notion_url: https://app.notion.com/p/3f44590a05eb819b8022f2a4cdd3b022
  expected_title: CL-C-10 — Perform CRD Retrospective and Decide Closure — 100926.1
  lane: CL-C
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Perform CRD Retrospective and Decide Closure for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, continuing Lead Developer and terminal closure authority.
  creator_role: Isis, continuing Lead Developer and terminal closure authority.
  reviewer_role: NONE
  inputs:
  - CRD
  - QA_REPORT_ID
  - QA_RCA_ID
  outputs:
  - artifact: CHANGE_CLOSURE_DECISION
    states:
    - CHANGE_CLOSED
    - DO_NOT_CLOSE
    consumers: &id013
    - CL-20
    - ESC-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id013
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb819b8022f2a4cdd3b022?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81ad8989faa77f441a64?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb819b8022f2a4cdd3b022?pvs=204
    page_last_edited_at: '2026-10-12T02:29:13.994Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: lineage into its result and handoff\b
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: Carry exact (?:CRD|Epic) Specification|Each runnable (?:direct-native )?package states
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: CTR-001
      value: These candidate URL tokens must be replaced
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\bdo not include\b(?! in the block)))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:model/strength/reasoning))
      guard: G-CL-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: PF10/addendum lineage into its result artifact, which the handoff names
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: that entry creates no runtime approval
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:The producer never edits PF10 or claims canonical adoption;
        it resolves the addendum's number from the current controlled PF10 at creation\.))
      guard: G-F05-F
- prompt_key: CL-E-10
  notion_page_id: 3f44590a05eb81248741f4679b050262
  notion_url: https://app.notion.com/p/3f44590a05eb81248741f4679b050262
  expected_title: CL-E-10 — Perform Epic Retrospective and Decide Closure — 100926.1
  lane: CL-E
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Perform Epic Retrospective and Decide Closure for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, continuing Lead Developer and terminal closure authority.
  creator_role: Isis, continuing Lead Developer and terminal closure authority.
  reviewer_role: NONE
  inputs:
  - QA_REPORT_ID
  - QA_RCA_ID
  outputs:
  - artifact: CHANGE_CLOSURE_DECISION
    states:
    - CHANGE_CLOSED
    - DO_NOT_CLOSE
    consumers: &id014
    - CL-20
    - CL-E-20
    - ESC-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id014
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81248741f4679b050262?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81248741f4679b050262?pvs=204
    page_last_edited_at: '2026-10-12T02:29:21.313Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: lineage into its result and handoff\b
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: Carry exact (?:CRD|Epic) Specification|Each runnable (?:direct-native )?package states
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: CTR-001
      value: These candidate URL tokens must be replaced
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\bdo not include\b(?! in the block)))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:model/strength/reasoning))
      guard: G-CL-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: PF10/addendum lineage into its result artifact, which the handoff names
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: that entry creates no runtime approval
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:The producer never edits PF10 or claims canonical adoption;
        it resolves the addendum's number from the current controlled PF10 at creation\.))
      guard: G-F05-F
- prompt_key: CL-E-20
  notion_page_id: 3f44590a05eb8186913fcb9f6b2a2f32
  notion_url: https://app.notion.com/p/3f44590a05eb8186913fcb9f6b2a2f32
  expected_title: CL-E-20 — Perform Bounded PF09 Epic Revalidation — 100926.1
  lane: CL-E
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Perform Bounded PF09 Epic Revalidation for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the explicitly assigned Lead Developer revalidation session, read-only.
  creator_role: the explicitly assigned Lead Developer revalidation session, read-only.
  reviewer_role: NONE
  inputs:
  - PF09_TARGET_REF
  - PF09_REVALIDATION_REVIEW_ID
  outputs:
  - artifact: PF09_REVALIDATION
    states:
    - BLOCKED
    - COMPLETE
    - PARTIAL
    consumers: &id015
    - CL-E-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id015
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8186913fcb9f6b2a2f32?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81c2b5d5ff46126f9e45?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8186913fcb9f6b2a2f32?pvs=204
    page_last_edited_at: '2026-10-12T02:29:16.227Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: revalidation session, read-only\.(?! Every statement in this prompt that it is read-only
        or does not change the repository excludes its own output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: controlled Markdown
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CL-E-30
  notion_page_id: 3f44590a05eb81be834efe3faf7abb6f
  notion_url: https://app.notion.com/p/3f44590a05eb81be834efe3faf7abb6f
  expected_title: CL-E-30 — Review Bounded PF09 Revalidation — 100926.1
  lane: CL-E
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Review Bounded PF09 Revalidation for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the assigned reviewer of the bounded revalidation deliverable.
  creator_role: the assigned reviewer of the bounded revalidation deliverable.
  reviewer_role: NONE
  inputs:
  - PF09_REVALIDATION_ID
  - PF09_REVALIDATION
  - CHANGE_CLOSURE_DECISION_ID
  outputs:
  - artifact: PF09_REVALIDATION_REVIEW
    states:
    - ACCEPT
    - DENY
    consumers: &id016
    - CL-E-20
    - CL-E-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id016
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81be834efe3faf7abb6f?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81b4a649fdcdb1903345?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81be834efe3faf7abb6f?pvs=204
    page_last_edited_at: '2026-10-12T02:29:29.629Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: controlled Markdown
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: CL-E-40
  notion_page_id: 3f44590a05eb8101a264f9fa702b8a6e
  notion_url: https://app.notion.com/p/3f44590a05eb8101a264f9fa702b8a6e
  expected_title: CL-E-40 — Prepare Post-Epic PF09 Maintenance — 100926.1
  lane: CL-E
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Prepare Post-Epic PF09 Maintenance for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the assigned Lead Developer maintenance author.
  creator_role: the assigned Lead Developer maintenance author.
  reviewer_role: NONE
  inputs:
  - PF09_REVALIDATION
  - PF09_REVALIDATION_REVIEW
  outputs:
  - artifact: PF09_MAINTENANCE_CANDIDATE
    states:
    - MAINTENANCE_PENDING
    consumers: &id017
    - CL-40
    - CL-E-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id017
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8101a264f9fa702b8a6e?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81e78e82f83a5f2e4b68?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8101a264f9fa702b8a6e?pvs=204
    page_last_edited_at: '2026-10-12T02:29:17.029Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: controlled Markdown
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: DOC-10
  notion_page_id: 3f44590a05eb81ce99b1d2ade30c572f
  notion_url: https://app.notion.com/p/3f44590a05eb81ce99b1d2ade30c572f
  expected_title: DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1
  lane: DOC
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Create Final Repository Documentation PR Instructions for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the same whole-change Implementation Agent (IA).
  creator_role: the same whole-change Implementation Agent (IA).
  reviewer_role: Dedicated PR engineering session
  inputs:
  - DOCUMENTATION_UNIT_ID
  - CHANGE_CLASS
  - CHANGE_ID
  - CANON_CONFLICT_REGISTER
  - PLAN_REVIEW_ID
  - REMEDIATION_REVIEW_ID
  - BLOCKED
  - PENDING
  - PARTIAL
  - FAILED
  outputs:
  - artifact: PR_INSTRUCTION
    states:
    - BLOCKED
    - DRAFT
    - INSTRUCTION_READY
    - PENDING
    consumers: &id018
    - PR-20
    - RS-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id018
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81ce99b1d2ade30c572f?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8193a9a8d7ddd751cd2d?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81ce99b1d2ade30c572f?pvs=204
    page_last_edited_at: '2026-10-12T02:29:24.131Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: 'only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual
        merge occurred|Nathan''s invocation supplies only the later manual-merge assertion|historical
        PR-35 `MERGE_PENDING` result, Nathan''s later manual-merge assertion|Nathan manual merge, PR-40
        read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|Nathan''s later merge assertion
        and PR-40''s independent|needed after Nathan''s assertion: continue to `?PR-40'
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Decide it during work
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: DOC-20
  notion_page_id: 3f44590a05eb81d8a582eec0e93e6ee7
  notion_url: https://app.notion.com/p/3f44590a05eb81d8a582eec0e93e6ee7
  expected_title: DOC-20 — Verify Final Repository Documentation Completion — 100926.1
  lane: DOC
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Verify Final Repository Documentation Completion for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the continuing whole-change Implementation Agent (IA), read-only.
  creator_role: the continuing whole-change Implementation Agent (IA), read-only.
  reviewer_role: NONE
  inputs:
  - PR_INSTRUCTION_ID
  - PR_WORK_UNIT_LINEAGE_REVIEW_ID
  - DOCUMENTATION_UNIT_ID
  - CHANGE_CLASS
  - CHANGE_ID
  - CANON_CONFLICT_REGISTER
  - COMPLETE
  - INCOMPLETE
  - PENDING
  - BLOCKED
  - PARTIAL
  - FAILED
  - PLAN_REVIEW_ID
  - REMEDIATION_REVIEW_ID
  outputs:
  - artifact: DOCUMENTATION_COMPLETION
    states:
    - BLOCKED
    - COMPLETE
    - INCOMPLETE
    - PENDING
    consumers: &id019
    - DOC-10
    - PR-40
    - QA-10
    - RS-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id019
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81d8a582eec0e93e6ee7?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8164ac09e722dc967f25?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81d8a582eec0e93e6ee7?pvs=204
    page_last_edited_at: '2026-10-12T02:29:19.255Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: 'only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual
        merge occurred|Nathan''s invocation supplies only the later manual-merge assertion|historical
        PR-35 `MERGE_PENDING` result, Nathan''s later manual-merge assertion|Nathan manual merge, PR-40
        read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|Nathan''s later merge assertion
        and PR-40''s independent|needed after Nathan''s assertion: continue to `?PR-40'
    - rule_id: CTR-001
      value: do not edit documentation, Canon, PF10, or repository state\.(?! Every statement in this
        prompt that it is read-only or does not change the repository excludes its own output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Decide it during work
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: ESC-10
  notion_page_id: 3f44590a05eb81f2af47fff48995f272
  notion_url: https://app.notion.com/p/3f44590a05eb81f2af47fff48995f272
  expected_title: ESC-10 — Create QA Escalation Report — 100926.1
  lane: ESC
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Create QA Escalation Report for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are the same continuing Kronos QA authority.
  creator_role: the same continuing Kronos QA authority.
  reviewer_role: NONE
  inputs:
  - QA_EVIDENCE_REVIEW_ID
  - QA_PREEXECUTION_FINDING_REF
  outputs:
  - artifact: QA_ESCALATION_REPORT
    states:
    - AWAITING_THOTH_REMEDIATION
    consumers: &id020
    - ESC-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id020
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81f2af47fff48995f272?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81cd938de84cfffead9c
  expected_parent_title: Escalation — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81d582b8d490e77f9f40?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81f2af47fff48995f272?pvs=204
    page_last_edited_at: '2026-10-12T02:29:32.722Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: ESC-25
  notion_page_id: 3f44590a05eb81949370e6d1b222b40b
  notion_url: https://app.notion.com/p/3f44590a05eb81949370e6d1b222b40b
  expected_title: ESC-25 — Execute Bounded Escalation Discovery — 100926.1
  lane: ESC
  sequence: 25
  lifecycle: ACTIVE
  function: Execute Execute Bounded Escalation Discovery for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the explicitly named read-only repository reviewer or authorized environment operator.
  creator_role: the explicitly named read-only repository reviewer or authorized environment operator.
  reviewer_role: NONE
  inputs:
  - REMEDIATION_PROPOSAL_ID
  - DISCOVERY_TASK_ID
  - TRIAGE_RECEIPT_ID
  outputs:
  - artifact: DISCOVERY_RESULT
    states:
    - BLOCKED
    - COMPLETE
    - PARTIAL
    consumers: &id021
    - ESC-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id021
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81949370e6d1b222b40b?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81cd938de84cfffead9c
  expected_parent_title: Escalation — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81bf9326e46a1017de38?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81949370e6d1b222b40b?pvs=204
    page_last_edited_at: '2026-10-12T02:29:20.067Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: read-only repository reviewer[^.\n]*\.(?! Every statement in this prompt that it is read-only
        or does not change the repository excludes its own output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: ESC-30
  notion_page_id: 3f44590a05eb81e385dbd4fe337ad9d9
  notion_url: https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9
  expected_title: ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1
  lane: ESC
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Diagnose and Propose Bounded Remediation for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Thoth, the continuing Head of Development and remediation proposal author for
    this change.
  creator_role: Thoth, the continuing Head of Development and remediation proposal author for this change.
  reviewer_role: NONE
  inputs:
  - ORIGINATING_FINDING_REF
  - QA_ESCALATION_REPORT_ID
  - CHANGE_CLASS
  - CHANGE_ID
  - REMEDIATION_PROPOSAL_ID
  - DISCOVERY_RESULT_IDS
  - REMEDIATION_REVIEW_ID
  outputs:
  - artifact: REMEDIATION_PROPOSAL
    states:
    - BLOCKED
    - DISCOVERY_REQUIRED
    - REMEDIATION_PENDING
    consumers: &id022
    - ESC-25
    - ESC-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id022
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81cd938de84cfffead9c
  expected_parent_title: Escalation — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb813e99b4e416bc7afdae?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9?pvs=204
    page_last_edited_at: '2026-10-12T02:29:51.552Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: ESC-40
  notion_page_id: 3f44590a05eb8173905cc6d17a40457b
  notion_url: https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b
  expected_title: ESC-40 — Review and Return Approved Remediation — 100926.1
  lane: ESC
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Review and Return Approved Remediation for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, the continuing Lead Developer and remediation decision owner.
  creator_role: Isis, the continuing Lead Developer and remediation decision owner.
  reviewer_role: NONE
  inputs:
  - REMEDIATION_PROPOSAL
  outputs:
  - artifact: REMEDIATION_REVIEW
    states:
    - APPROVE
    - APPROVE_AS_CHANGED
    - DENY
    consumers: &id023
    - ESC-30
    - PR-30
    - PR-35
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id023
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81cd938de84cfffead9c
  expected_parent_title: Escalation — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81efb6d4cd8d02ba9756?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b?pvs=204
    page_last_edited_at: '2026-10-12T02:29:22.274Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?i:Outside GCFPE\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-A
    - rule_id: CTR-001
      value: (?m)^(?=.*(?i:format recorded in the Glow Operations Hub|one `##` heading carrying its title|canonical
        PF10 build-notes addendum format))
      guard: G-F05-B
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)^(?=.*(?i:one H2 heading with the next continuous number))(?=.*(?:PF06-Canon-Change-Process-Guide))(?=.*(?:PF27-Canon-Plan-Templates))(?=.*(?i:only
        H3 or lower))
      guard: G-F05-C
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: GCFPE-MGMT-10
  notion_page_id: 3f74590a05eb81b69bd8c27106f7a59d
  notion_url: https://app.notion.com/p/3f74590a05eb81b69bd8c27106f7a59d
  expected_title: GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1
  lane: GCFPE-MGMT
  sequence: 10
  lifecycle: ACTIVE
  function: Manage one ecosystem Modification from request to applied result through three explicit modes,
    ANALYZE, PLAN and EXECUTE, stopping at merge and install, which are Nathan's.
  session_class: DEDICATED_ONE_OFF
  session_role: Act as the Managing Prompt Engineer for one ecosystem Modification.
  creator_role: Act as the Managing Prompt Engineer for one ecosystem Modification.
  reviewer_role: NONE
  inputs:
  - 'MODE: ANALYZE, PLAN or EXECUTE.'
  - 'The subject: for ANALYZE, the request in whatever form it arrives, or the Modification id when the
    invocation arrives as the intake and triage prompt''s NEXT_PROMPT_HANDOFF; for PLAN and EXECUTE, the
    Modification id.'
  outputs:
  - artifact: GCFPE_MODIFICATION_RECORD
    states:
    - ECOSYSTEM_CHANGE_COMPLETE
    - IMPLEMENTATION_BLOCKED
    - PRODUCT_OWNER_ACTION_PENDING
    - PROMOTION_CHECKPOINT_REQUIRED
    consumers: &id024 []
  mutations:
    allowed:
    - Write only to docs/ephemeral/, docs/graph/ and docs/prompt_ecosystem_management/, to Notion where
      a destination rule or explicit task authorization allows, and to installed skills
    forbidden:
    - 'Merge a pull request or install a skill: Nathan alone merges and installs'
    - Write docs/pfcanon/ or edit PF10 directly
    - Mirror, export, hash or byte-compare a prompt body to disk
    - Execute product Change Flow, implementation, QA, release selection, promotion or archival, or Alpha
      work
    - Emit a handoff to any prompt
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - The page is the duplicate of the approved testing body 3e34590a05eb811b93d2da9b4ef8106d with only
    M-HEAD and M-TS applied (MODIFICATION-20261011-gcfpe-mb008-to-promotion, PLAN PART-05); the testing
    page is unchanged and stays as the record.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return the truthful blocked or incomplete state to the exact owner, with the failed predicate and
    the recovery point; never invent missing evidence.
  - A source that cannot be uniquely resolved and read is a resolution error, not an assumed absence.
  - 'After the first external write, a failure takes D26-B''s path: a failure record that reaches main
    in a record pull request, a read-only sweep, the freeze kept, and a return to Nathan.'
  required_interfaces: *id024
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f74590a05eb81b69bd8c27106f7a59d?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81de9736ea69bac61016
  expected_parent_title: Glow HDE Prompt Flow Index — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81d1bb64ebcb3ca8eb54?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f74590a05eb81b69bd8c27106f7a59d?pvs=204
    page_last_edited_at: '2026-10-12T02:30:05.584Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: does not execute product Change Flow, implementation, repository work[^.\n]*\.(?! Every statement
        in this prompt that it is read-only or does not change the repository excludes its own output
        artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Repository paths outside `?docs/ephemeral/`? and `?docs/graph/`? are not written
    - rule_id: SRC-001
      value: '(?s)^Prompt ID:.*^Prompt ID:'
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)^(?=.*(?i:approved_for_testing|gcfpe_proposed_prompt_body|not_selected:|proposed replacement
        body))
      guard: G-MGMT-3
    required_literals: null
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: Every artifact is written under the path its kind belongs to — `docs/ephemeral/` for the
        Modification and its evidence, `docs/graph/` for graph parts, `docs/prompt_ecosystem_management/`
        for the controls this prompt maintains
    - rule_id: CTR-002
      value: Repository paths outside the writable set are not written, and `docs/pfcanon/` is read only\.
    - rule_id: CTR-002
      value: \*\*Nathan alone merges\. Nathan alone installs\.\*\*
    - rule_id: TOP-001
      value: \*\*This prompt hands off to no other prompt\.\*\* Every result returns to Nathan\.
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:record in the Modification the TypeSafe reading for that mode''s session and
        name it, with the record''s path, in the few lines of the return))(?=.*(?i:run the installed TypeSafe
        scoring skill''s script once, on an action text for that mode''s work written as the skill directs))(?=.*(?i:record
        the reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?:Do not write the skill''s Notion row\.))(?=.*(?i:When Nathan states
        the model and setting chosen for a session, record that pick in the Modification with a reference
        to the reading))'
      guard: G-TS-7
    - rule_id: CTR-002
      value: '(?m)^(?=(?:Prompt ID: ))'
      guard: G-MGMT-2
    - rule_id: CTR-002
      value: (?m)^(?=.*(?:In a fresh session, he invokes this prompt with that `MODE` and the Modification
        id\. Never without his approval\.))
      guard: G-MGMT-4
    - rule_id: CTR-002
      value: (?m)^(?=(?:GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926\.1$))
      guard: G-MGMT-5
- prompt_key: IA-10
  notion_page_id: 3f44590a05eb813aa0ccd709ebd134d0
  notion_url: https://app.notion.com/p/3f44590a05eb813aa0ccd709ebd134d0
  expected_title: IA-10 — Create Whole-Change Implementation Audit and Plan — 100926.1
  lane: IA
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Create Whole-Change Implementation Audit and Plan for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the dedicated Implementation Agent (IA) for this entire change.
  creator_role: the dedicated Implementation Agent (IA) for this entire change.
  reviewer_role: Isis / Lead Developer
  inputs:
  - SPECIFICATION_ID
  outputs:
  - artifact: IMPLEMENTATION_AUDIT / IMPLEMENTATION_PLAN
    states:
    - AUDIT_COMPLETE
    - BLOCKED
    - PLAN_PENDING
    consumers: &id025
    - IA-20
    - IA-30
    - IA-50
    - IA-60
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id025
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb813aa0ccd709ebd134d0?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb817aa191f1e822c30480?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb813aa0ccd709ebd134d0?pvs=204
    page_last_edited_at: '2026-10-12T02:29:35.733Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: IA-20
  notion_page_id: 3f44590a05eb81a8bf39f4b16cc61a5f
  notion_url: https://app.notion.com/p/3f44590a05eb81a8bf39f4b16cc61a5f
  expected_title: IA-20 — Create Whole-Change Implementation Plan — 100926.1
  lane: IA
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Create Whole-Change Implementation Plan for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the same whole-change Implementation Agent (IA).
  creator_role: the same whole-change Implementation Agent (IA).
  reviewer_role: Isis / Lead Developer
  inputs:
  - SPECIFICATION_ID
  - IMPLEMENTATION_AUDIT_ID
  outputs:
  - artifact: IMPLEMENTATION_PLAN
    states:
    - BLOCKED
    - PLAN_PENDING
    consumers: &id026
    - IA-30
    - IA-50
    - IA-60
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id026
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81a8bf39f4b16cc61a5f?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81c4825df2ad0dec4750?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81a8bf39f4b16cc61a5f?pvs=204
    page_last_edited_at: '2026-10-12T02:29:23.010Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: IA-30
  notion_page_id: 3f44590a05eb811db88dece791f1f60c
  notion_url: https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c
  expected_title: IA-30 — Review Whole-Change Implementation Plan — 100926.1
  lane: IA
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Review Whole-Change Implementation Plan for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, continuing Lead Developer for the approved change.
  creator_role: Isis, continuing Lead Developer for the approved change.
  reviewer_role: NONE
  inputs:
  - INITIAL_PLAN_REVIEW
  - MATERIAL_PLAN_DELTA_REVIEW
  outputs:
  - artifact: IMPLEMENTATION_PLAN_REVIEW / MATERIAL_PLAN_DELTA_REVIEW
    states:
    - CHANGE_NOT_SUBSTANTIATED
    - DELTA_APPROVE
    - DELTA_DENY
    - INITIAL_APPROVE
    - INITIAL_DENY
    - PLAN_DELTA_REDLINE
    - PRODUCT_OWNER_DECISION_REQUIRED
    - WRONG_NATIVE_LANE
    consumers: &id027
    - IA-40
    - PR-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id027
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81c6bfb5f36f7df8f464?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c?pvs=204
    page_last_edited_at: '2026-10-12T02:29:54.641Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: unresolved items/owners, next action, and expected (?:output|review state)
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Decide it during work
    - rule_id: CTR-001
      value: (?m)^(?!.*(?i:\bnonterminal\b))(?=.*(?:DELTA_APPROVE))(?=.*(?i:\bterminal(ly)?\b|\bno (runnable
        )?continuation\b|\bemit no\b))
      guard: G-F03-A
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?i:Outside GCFPE\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-A
    - rule_id: CTR-001
      value: (?m)^(?=.*(?i:format recorded in the Glow Operations Hub|one `##` heading carrying its title|canonical
        PF10 build-notes addendum format))
      guard: G-F05-B
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)^(?=.*(?:DELTA_APPROVE))(?=.*(?i:\bnonterminal\b))(?=.*(?i:exactly one complete continuation
        block))(?=.*(?i:return (phase|point)))
      guard: G-F03-B
    - rule_id: CTR-002
      value: (?m)^(?=.*(?i:one H2 heading with the next continuous number))(?=.*(?:PF06-Canon-Change-Process-Guide))(?=.*(?:PF27-Canon-Plan-Templates))(?=.*(?i:only
        H3 or lower))
      guard: G-F05-C
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: IA-40
  notion_page_id: 3f44590a05eb81ca83ecdac0960a6f16
  notion_url: https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16
  expected_title: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1
  lane: IA
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Prepare or Revise Whole-Change Implementation Plan for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the same Implementation Agent (IA) who authored the pending preapproval whole-change
    Plan.
  creator_role: the same Implementation Agent (IA) who authored the pending preapproval whole-change Plan.
  reviewer_role: Isis / Lead Developer
  inputs:
  - Require one complete pending initial Implementation Plan plus the exact IA-30 denial/redline for that
    version, or an interrupted preapproval recovery package with the same author/reviewer lineage.
  outputs:
  - artifact: IMPLEMENTATION_PLAN
    states:
    - PLAN_PENDING_REVISED
    - REDLINE_INCOMPLETE
    - WRONG_NATIVE_LANE
    consumers:
    - IA-30
  - artifact: MATERIAL_PLAN_DELTA
    states:
    - PLAN_DELTA_PENDING
    consumers:
    - IA-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces:
  - IA-30
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8197bb1bc8f52f896969?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16?pvs=204
    page_last_edited_at: '2026-10-12T02:29:25.413Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: IA-50
  notion_page_id: 3f44590a05eb810aa299fbb05a34dece
  notion_url: https://app.notion.com/p/3f44590a05eb810aa299fbb05a34dece
  expected_title: IA-50 — IA Answer Seeder — 100926.1
  lane: IA
  sequence: 50
  lifecycle: ACTIVE
  function: Execute IA Answer Seeder for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: Act as the IA Answer Seeder, a bounded resolution assistant.
  creator_role: Act as the IA Answer Seeder, a bounded resolution assistant.
  reviewer_role: NONE
  inputs:
  - 'RECOVERY_ENVELOPE: the complete exact paused-question/checkpoint envelope defined below.'
  outputs:
  - artifact: IA_RECOVERY_SEED
    states:
    - SEED_INCOMPLETE
    - SEED_READY
    consumers: &id028
    - IA-10
    - IA-20
    - IA-30
    - IA-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id028
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb810aa299fbb05a34dece?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81d78eeae384e93dd697?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb810aa299fbb05a34dece?pvs=204
    page_last_edited_at: '2026-10-12T02:29:38.746Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: IA-60
  notion_page_id: 3f44590a05eb81cdab15c7e7f7094a64
  notion_url: https://app.notion.com/p/3f44590a05eb81cdab15c7e7f7094a64
  expected_title: IA-60 — Thoth Planning Research — 100926.1
  lane: IA
  sequence: 60
  lifecycle: ACTIVE
  function: Execute Thoth Planning Research for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: Act as Thoth for one bounded advanced engineering planning inquiry before Plan approval.
  creator_role: Act as Thoth for one bounded advanced engineering planning inquiry before Plan approval.
  reviewer_role: NONE
  inputs:
  - 'PLANNING_INQUIRY: exact original question/identity; actual files/interfaces and repository evidence;
    constraints, alternatives, failure modes, decision criteria and specific requested finding.'
  outputs:
  - artifact: PLANNING_RESEARCH_FINDING
    states:
    - BLOCKED
    - PARTIAL
    - RESEARCH_COMPLETE
    consumers: &id029
    - IA-50
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id029
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81cdab15c7e7f7094a64?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8141b5b2c8fbf7b725e2?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81cdab15c7e7f7094a64?pvs=204
    page_last_edited_at: '2026-10-12T02:30:00.331Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: MGR-10
  notion_page_id: 3f44590a05eb813ea53ac959e7a4e597
  notion_url: https://app.notion.com/p/3f44590a05eb813ea53ac959e7a4e597
  expected_title: MGR-10 — Coordinate the Complete Change Flow within Current Authority — 100926.1
  lane: MGR
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Coordinate the Complete Change Flow within Current Authority for the exact supplied
    change.
  session_class: ORCHESTRATOR_RUN
  session_role: You are the Change Flow coordinator, without taking over any substantive actor or approval.
  creator_role: the Change Flow coordinator, without taking over any substantive actor or approval.
  reviewer_role: NONE
  inputs:
  - For a request only to prepare Product Owner cycle-entry launch guidance, accept known or unresolved
    classification and all actual intake without inventing change identity.
  outputs:
  - artifact: FLOW_PROGRESS
    states:
    - FLOW_PROGRESS
    - TERMINAL_RETURN
    consumers: &id030
    - CF-C-10
    - CF-E-10
    - CF-PO-10
    - CL-40
    - QA-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id030
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb813ea53ac959e7a4e597?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb81d59059eb6b95ed5fcf
  expected_parent_title: HDE Change Flow — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8108ad2dd4d0e20bd6c4?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb813ea53ac959e7a4e597?pvs=204
    page_last_edited_at: '2026-10-12T02:29:57.710Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion-resident artifact
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: OPS-10
  notion_page_id: 3f44590a05eb81509957c43992c03625
  notion_url: https://app.notion.com/p/3f44590a05eb81509957c43992c03625
  expected_title: OPS-10 — Create Bounded Ops Task — 100926.1
  lane: OPS
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Create Bounded Ops Task for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the same Implementation Agent (IA) and future task-acceptance owner.
  creator_role: the same Implementation Agent (IA) and future task-acceptance owner.
  reviewer_role: Same whole-change Implementation Agent
  inputs:
  - IMPLEMENTATION_PLAN_REF
  - PLAN_REVIEW_ID
  - REMEDIATION_REVIEW_ID
  outputs:
  - artifact: OPS_TASK
    states:
    - BLOCKED
    - READY
    consumers: &id031
    - ESC-25
    - OPS-20
    - RS-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - PF27 section 3 executable task, safe same-script rehearsal where supported, real authority/target/effects,
    stop/recovery and canonical audit/ops stored evidence; preserve permitted historical mappings.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing required stored evidence cannot support completion/ACCEPT; no verbatim approval formula required.
  required_interfaces: *id031
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81509957c43992c03625?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81db98cce3e30a62bce5?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81509957c43992c03625?pvs=204
    page_last_edited_at: '2026-10-12T02:29:29.013Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b|^(?:Complete return to ESC-30|RS-30 native revision):[^\n]*CANON_CONFLICT_REGISTER)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: must preserve in its execution result and return handoff
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: controlled Markdown
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: Then give the other fields the handoff rule above names; sections the artifact already holds
        are named, not repeated\.
    - rule_id: CTR-002
      value: Reviewers remain read-only toward the work they review
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: OPS-20
  notion_page_id: 3f44590a05eb8155aebacd56f469643e
  notion_url: https://app.notion.com/p/3f44590a05eb8155aebacd56f469643e
  expected_title: OPS-20 — Execute Bounded Ops Task — 100926.1
  lane: OPS
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Execute Bounded Ops Task for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the authorized DevOps or target-environment operator for the exact bounded operation
    supplied in OPS_TASK_ID.
  creator_role: the authorized DevOps or target-environment operator for the exact bounded operation supplied
    in OPS_TASK_ID.
  reviewer_role: NONE
  inputs:
  - OPS_TASK_ID
  outputs:
  - artifact: OPS_EXECUTION_RESULT
    states:
    - BLOCKED
    - COMPLETE
    - FAILED
    - NOT_EXECUTED
    - NOT_PRODUCED
    - PARTIAL
    consumers: &id032
    - ESC-25
    - OPS-30
    - RS-10
  mutations:
    allowed:
    - Execute only the bounded OPS_TASK mutations
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - PF27 section 3 executable task, safe same-script rehearsal where supported, real authority/target/effects,
    stop/recovery and canonical audit/ops stored evidence; preserve permitted historical mappings.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing required stored evidence cannot support completion/ACCEPT; no verbatim approval formula required.
  required_interfaces: *id032
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8155aebacd56f469643e?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81858a9dd361d3689ce8?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8155aebacd56f469643e?pvs=204
    page_last_edited_at: '2026-10-12T02:29:42.649Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b|^(?:Complete return to ESC-30|RS-30 native revision):[^\n]*CANON_CONFLICT_REGISTER)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: controlled Markdown
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: Then give the other fields the handoff rule above names; sections the artifact already holds
        are named, not repeated\.
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: OPS-30
  notion_page_id: 3f44590a05eb81ec8da3effc3b28cf97
  notion_url: https://app.notion.com/p/3f44590a05eb81ec8da3effc3b28cf97
  expected_title: OPS-30 — Review Ops Execution Receipt — 100926.1
  lane: OPS
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Review Ops Execution Receipt for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the same Implementation Agent (IA) who created the Ops Task.
  creator_role: the same Implementation Agent (IA) who created the Ops Task.
  reviewer_role: NONE
  inputs:
  - OPS_TASK_ID
  - OPS_EXECUTION_RESULT_ID
  - CHANGE_CLASS
  - CHANGE_ID
  - OPS_UNIT_ID
  - CANON_CONFLICT_REGISTER
  - COMPLETE
  - PARTIAL
  - BLOCKED
  - FAILED
  outputs:
  - artifact: OPS_TASK_RECEIPT
    states:
    - ACCEPT
    - REJECT
    consumers: &id033
    - ESC-25
    - OPS-10
    - RS-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  - PF27 section 3 executable task, safe same-script rehearsal where supported, real authority/target/effects,
    stop/recovery and canonical audit/ops stored evidence; preserve permitted historical mappings.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  - Missing required stored evidence cannot support completion/ACCEPT; no verbatim approval formula required.
  required_interfaces: *id033
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81ec8da3effc3b28cf97?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb816f91c9c394f9c9fa57?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81ec8da3effc3b28cf97?pvs=204
    page_last_edited_at: '2026-10-12T02:30:04.097Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: native inputs, lineage, current state, gates, risks and required action
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: TOP-001
      value: A saved attachment, link or scattered fields do not replace the handoff\.
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: Then give the other fields the handoff rule above names; sections the artifact already holds
        are named, not repeated\.
    - rule_id: CTR-002
      value: each input artifact by repository path; the artifacts hold the rest
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: Reviewers remain read-only toward the work they review
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: PR-10
  notion_page_id: 3f44590a05eb815d97d5f3930c7d3e8a
  notion_url: https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a
  expected_title: PR-10 — Create PR Work-Unit Instructions — 100926.1
  lane: PR
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Create PR Work-Unit Instructions for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the same Implementation Agent (IA).
  creator_role: the same Implementation Agent (IA).
  reviewer_role: Dedicated PR engineering session
  inputs:
  - IMPLEMENTATION_PLAN_ID
  - PLAN_REVIEW_ID
  - WORK_UNIT_ID
  - REMEDIATION_REVIEW_ID
  outputs:
  - artifact: PR_INSTRUCTION
    states:
    - BLOCKED
    - DRAFT
    - INSTRUCTION_READY
    consumers: &id034
    - PR-20
    - RS-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id034
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a?pvs=204
    page_last_edited_at: '2026-10-12T02:29:33.739Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: carry PR_INSTRUCTION_ID and its complete content|dependency and evidence history; read-only
        substantiation of the mismatch; completed work
    - rule_id: TOP-001
      value: (?i)\b(?:hands?|carry|carrying|carries)\s+(?:the\s+)?(?:one\s+|exact\s+|same\s+)?(?:original
        Proceed, dedicated PR session, )?workspace/worktree, branch\b|Carry the exact dedicated session,
        open PR|commit and remote-head references; completed work|branch and repository/reference baseline
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: 'only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual
        merge occurred|Nathan''s invocation supplies only the later manual-merge assertion|historical
        PR-35 `MERGE_PENDING` result, Nathan''s later manual-merge assertion|Nathan manual merge, PR-40
        read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|Nathan''s later merge assertion
        and PR-40''s independent|needed after Nathan''s assertion: continue to `?PR-40'
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: CTR-001
      value: Decide it during work
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(their|your|its) own (recommendation|assessment)\b))(?!(?i:Never
        infer external state or execution success\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(assess\w*|evaluat\w*|recommend\w*|apprais\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(runtime
        setting|model|reasoning|strength|suitability|eligibility)\b))
      guard: G-TS-4
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: Then give the other fields the handoff rule above names; sections the artifact already holds
        are named, not repeated\.
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:do not prescribe a runtime setting
        or give their own assessment of one))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:the TypeSafe reading and
        surface advice that \*Mandatory single-block handoff\* requires inform Nathan's choice and prescribe
        nothing))
      guard: G-TS-5
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: PR-20
  notion_page_id: 3f44590a05eb819fbea5dcd966a750ba
  notion_url: https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba
  expected_title: PR-20 — Create Detailed PR Implementation Plan — 100926.1
  lane: PR
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Create Detailed PR Implementation Plan for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the dedicated PR engineering session for this one work unit.
  creator_role: the dedicated PR engineering session for this one work unit.
  reviewer_role: Nathan / Product Owner
  inputs:
  - PR_INSTRUCTION_ID
  - PR_WORK_UNIT_LINEAGE_REVIEW with REJECT (reject_replan) and its in-scope finding, for a re-plan of
    the same WORK_UNIT_ID in a new dedicated session Nathan seeds
  outputs:
  - artifact: PR_IMPLEMENTATION_PLAN
    states:
    - AWAITING_PO_PROCEED
    - BLOCKED
    - DRAFT
    consumers: &id035
    - RS-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id035
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba?pvs=204
    page_last_edited_at: '2026-10-12T02:29:47.327Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: dependency/evidence history, completed work and unaffected obligations|all actual merge/commit/order/check
        evidence|current stage and suspended boundary, completed work, dependencies, evidence
    - rule_id: TOP-001
      value: (?i)\b(?:hands?|carry|carrying|carries)\s+(?:the\s+)?(?:one\s+|exact\s+|same\s+)?(?:original
        Proceed, dedicated PR session, )?workspace/worktree, branch\b|Carry the exact dedicated session,
        open PR|commit and remote-head references; completed work|branch and repository/reference baseline
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: 'only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual
        merge occurred|Nathan''s invocation supplies only the later manual-merge assertion|historical
        PR-35 `MERGE_PENDING` result, Nathan''s later manual-merge assertion|Nathan manual merge, PR-40
        read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|Nathan''s later merge assertion
        and PR-40''s independent|needed after Nathan''s assertion: continue to `?PR-40'
    - rule_id: CTR-001
      value: Do not mutate the repository in this authoring operation\.(?! Every statement in this prompt
        that it is read-only or does not change the repository excludes its own output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: CTR-001
      value: Decide it during work
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(their|your|its) own (recommendation|assessment)\b))(?!(?i:Never
        infer external state or execution success\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(assess\w*|evaluat\w*|recommend\w*|apprais\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(runtime
        setting|model|reasoning|strength|suitability|eligibility)\b))
      guard: G-TS-4
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: accepts\s+a\s+`?PR_WORK_UNIT_LINEAGE_REVIEW`?\s+whose\s+result\s+is\s+`?REJECT
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: Then give the other fields the handoff rule above names; sections the artifact already holds
        are named, not repeated\.
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:do not prescribe a runtime setting
        or give their own assessment of one))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:the TypeSafe reading and
        surface advice that \*Mandatory single-block handoff\* requires inform Nathan's choice and prescribe
        nothing))
      guard: G-TS-5
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: PR-30
  notion_page_id: 3f44590a05eb8148a538f5c80588db14
  notion_url: https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14
  expected_title: PR-30 — PR Implementation Proceed — 100926.1
  lane: PR
  sequence: 30
  lifecycle: ACTIVE
  function: Execute PR Implementation Proceed for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the same dedicated PR engineering session for one exact approved work unit.
  creator_role: the same dedicated PR engineering session for one exact approved work unit.
  reviewer_role: NONE
  inputs:
  - REMEDIATION_REVIEW
  - REMEDIATION_PLAN_REVIEW
  outputs:
  - artifact: PR_IMPLEMENTATION_RESULT
    states:
    - PRODUCT_OWNER_DECISION_REQUIRED
    - PR_CANDIDATE_PUBLISHED
    - RECOVERY_PENDING
    - RESCOPE_PENDING
    consumers: &id036
    - PR-35
    - RS-20
  mutations:
    allowed:
    - Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes
      on the published PR belong to PR-35
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id036
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14?pvs=204
    page_last_edited_at: '2026-10-12T02:30:08.672Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: (?i)\b(?:hands?|carry|carrying|carries)\s+(?:the\s+)?(?:one\s+|exact\s+|same\s+)?(?:original
        Proceed, dedicated PR session, )?workspace/worktree, branch\b|Carry the exact dedicated session,
        open PR|commit and remote-head references; completed work|branch and repository/reference baseline
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: TOP-001
      value: outside the approved Plan, return the metadata\b
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(their|your|its) own (recommendation|assessment)\b))(?!(?i:Never
        infer external state or execution success\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(assess\w*|evaluat\w*|recommend\w*|apprais\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(runtime
        setting|model|reasoning|strength|suitability|eligibility)\b))
      guard: G-TS-4
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: An\s+\*?In-flight decisions\*?\s+section
    - rule_id: CTR-002
      value: Decide it during work
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: they do not share a session
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: Then give the other fields the handoff rule above names; sections the artifact already holds
        are named, not repeated\.
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:do not prescribe a runtime setting
        or give their own assessment of one))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:the TypeSafe reading and
        surface advice that \*Mandatory single-block handoff\* requires inform Nathan's choice and prescribe
        nothing))
      guard: G-TS-5
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: PR-35
  notion_page_id: 3f44590a05eb811ebf72e949b7b1572e
  notion_url: https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e
  expected_title: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1
  lane: PR
  sequence: 35
  lifecycle: ACTIVE
  function: Execute the review-resolution and merge-readiness phase for one proceeded PR work unit.
  session_class: DEDICATED_PR_REVIEW_SESSION
  session_role: You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you
    continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's
    handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of
    any other session.
  creator_role: The dedicated PR-35 session; PR-30 and PR-35 are two phases of one work unit, run in two
    dedicated sessions.
  reviewer_role: NONE
  inputs:
  - WORK_UNIT_ID and exact change/Epic identity
  - selected PR-35 prompt identity and direct Notion URL
  - 'session_disposition: NEW_DEDICATED — the dedicated PR-35 session for this WORK_UNIT_ID'
  - original Product Owner Proceed for the exact detailed PR Plan
  - complete IA-issued PR instruction
  - immutable approved Specification and whole-change Implementation Plan with review and approved overlay
    lineage
  outputs:
  - artifact: PR_IMPLEMENTATION_RESULT
    states:
    - MERGE_OBSERVED
    - MERGE_PENDING
    - PRODUCT_OWNER_DECISION_REQUIRED
    - RECOVERY_PENDING
    - REMOTE_EVIDENCE_PENDING
    - RESCOPE_PENDING
    consumers: &id037
    - PR-40
    - RS-20
  mutations:
    allowed:
    - Resolve review findings on the existing pull request for the proceeded work unit
    - Record remote actions in the durable remote-action ledger and checkpoints
    - Produce the versioned same-lineage PR_IMPLEMENTATION_RESULT phase record
    forbidden:
    - Merge a pull request or enable automatic merge
    - Edit PF10 directly
    - Add an R1 row, actor, approval, Proceed or work unit, or any session beyond its own dedicated PR-35
      session
    - Produce a PF10_BUILD_NOTES_ADDENDUM
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e?pvs=204
    page_last_edited_at: '2026-10-12T02:30:15.569Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: CTR-001
      value: launched as a new session
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Carry original Proceed, dedicated PR session, workspace/worktree, branch|current head; completed
        work, commits/local changes|reviews/checks already observed, unresolved items|with each actual
        PR reference, commit identity, order
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: sixth top-level PR-35 result
    - rule_id: CTR-001
      value: The PR-40 handoff must say:|Nathan's later paste asserts
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Repository paths outside `?docs/ephemeral/`? and `?docs/graph/`? are not written
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(their|your|its) own (recommendation|assessment)\b))(?!(?i:Never
        infer external state or execution success\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(assess\w*|evaluat\w*|recommend\w*|apprais\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(runtime
        setting|model|reasoning|strength|suitability|eligibility)\b))
      guard: G-TS-4
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: An\s+\*?In-flight decisions\*?\s+section
    - rule_id: CTR-002
      value: Decide it during work
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: they do not share a session
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: '[Ss]ubscribe to the pull request'
    - rule_id: CTR-002
      value: stay subscribed and do not poll
    - rule_id: CTR-002
      value: The observed merge event is the fact PR-40 is entered on
    - rule_id: CTR-002
      value: verified at entry from the recorded vehicle and repository state; the handoff does not carry
        them
    - rule_id: CTR-002
      value: '`MERGE_OBSERVED`: [^\n]*?the subscribed PR-35 session observes the merge of the identified
        PR, performed by Nathan'
    - rule_id: CTR-002
      value: seventh top-level PR-35 result
    - rule_id: CTR-002
      value: for `MERGE_OBSERVED`, it is the same selected PR-40
    - rule_id: CTR-002
      value: This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:Do not give your own recommendation,
        assessment or ranking of model, reasoning level or effort, and do not inspect or route on model))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:the
        TypeSafe reading and surface advice follow \*Mandatory single-block handoff\*))
      guard: G-TS-6
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id037
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  registry_note: Added 2026-09-17. Present in the 091426.1 candidate and absent from the 091326.2 predecessor;
    this entry was derived from the candidate body, not carried over.
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204
- prompt_key: PR-40
  notion_page_id: 3f44590a05eb81088487e918fd642a7f
  notion_url: https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f
  expected_title: PR-40 — Review PR Work-Unit Lineage — 100926.1
  lane: PR
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Review PR Work-Unit Lineage for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the designated PR reviewer for the complete work unit, operating read-only.
  creator_role: the designated PR reviewer for the complete work unit, operating read-only.
  reviewer_role: NONE
  inputs:
  - PR_INSTRUCTION_ID and complete PR_INSTRUCTION
  - PR_IMPLEMENTATION_PLAN_ID and complete PR_IMPLEMENTATION_PLAN
  - The complete PR-30 result with PR_CANDIDATE_PUBLISHED
  - 'The complete PR-35 result: MERGE_OBSERVED with the observed merge event, or, only where no MERGE_OBSERVED
    result was returned for this merge, the earlier MERGE_PENDING, which is historical pre-merge evidence.'
  - The complete ordered PR_REFS for this work unit; PR-40 resolves each PR's commits, order, review/check
    state and merge evidence from repository evidence
  - CHANGE_CLASS, CHANGE_ID, WORK_UNIT_ID, approved Specification, Implementation Audit, Plan, Plan review,
    dependency and acceptance/evidence lineage
  - Existing PR reviewer/session lineage for a rereview, the PR-30 and PR-35 session identities, the whole-change
    IA context and exact return owner
  - CANON_CONFLICT_REGISTER, recovery state, truthful pending, NOT PRODUCED and NOT EXECUTED values, and
    all actual access limitations
  - The branch, head and commits are verified at entry from the recorded vehicle and repository state;
    the handoff does not carry them.
  - PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35
    session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on
    Nathan's assertion that he manually merged it.
  outputs:
  - artifact: PR_WORK_UNIT_LINEAGE_REVIEW
    states:
    - ACCEPT
    - PENDING
    - REJECT
    consumers: &id038
    - DOC-10
    - DOC-20
    - OPS-10
    - PR-10
    - PR-20
    - QA-10
    - RS-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id038
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f?pvs=204
    page_last_edited_at: '2026-10-12T02:29:38.234Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: CTR-001
      value: original Proceed and a suitable actual authorized implementation vehicle
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: PR instruction and implementation result; actual merged-state evidence|dependency, acceptance
        and evidence history; completed work|all completed review work; attempts; limitations
    - rule_id: TOP-001
      value: Carry original Proceed, dedicated PR session, workspace/worktree, branch|current head; completed
        work, commits/local changes|reviews/checks already observed, unresolved items|with each actual
        PR reference, commit identity, order
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: 'only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual
        merge occurred|Nathan''s invocation supplies only the later manual-merge assertion|historical
        PR-35 `MERGE_PENDING` result, Nathan''s later manual-merge assertion|Nathan manual merge, PR-40
        read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|Nathan''s later merge assertion
        and PR-40''s independent|needed after Nathan''s assertion: continue to `?PR-40'
    - rule_id: CTR-001
      value: ordinary in-scope defect remains with the existing PR owner
    - rule_id: CTR-001
      value: operating read-only\.(?! Every statement in this prompt that it is read-only or does not
        change the repository excludes its own output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: CTR-001
      value: Decide it during work
    - rule_id: TOP-001
      value: RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL\b
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(their|your|its) own (recommendation|assessment)\b))(?!(?i:Never
        infer external state or execution success\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(assess\w*|evaluat\w*|recommend\w*|apprais\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(runtime
        setting|model|reasoning|strength|suitability|eligibility)\b))
      guard: G-TS-4
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: every native return names those artifacts
    - rule_id: CTR-002
      value: Then give the other fields the handoff rule above names; sections the artifact already holds
        are named, not repeated\.
    - rule_id: CTR-002
      value: verified at entry from the recorded vehicle and repository state; the handoff does not carry
        them
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: re-plans through `?PR-20`?, as \*\*PRECISE IN-SCOPE DEFECT → re-plan\*\* states
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: Reviewers remain read-only toward the work they review
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:do not prescribe a runtime setting
        or give their own assessment of one))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:the TypeSafe reading and
        surface advice that \*Mandatory single-block handoff\* requires inform Nathan's choice and prescribe
        nothing))
      guard: G-TS-5
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: PR-50
  notion_page_id: 3f44590a05eb81d29748eb21df73b02c
  notion_url: https://app.notion.com/p/3f44590a05eb81d29748eb21df73b02c
  expected_title: PR-50 — Abort PR and Escalate — 100926.1
  lane: PR
  sequence: 50
  lifecycle: ACTIVE
  function: Execute Abort PR and Escalate for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are acting only on Nathan / Product Owner's direct manual invocation.
  creator_role: acting only on Nathan / Product Owner's direct manual invocation.
  reviewer_role: NONE
  inputs:
  - Require Nathan's direct manual invocation, exact change/work unit, PR/session/workspace/worktree/branch/head,
    original Proceed, immutable base and applicable overlays, failure/recovery evidence, completed work,
    reviews/CI, artifacts, constraints and the reason continuation is unrecoverable.
  outputs:
  - artifact: PR_ABORT_ESCALATION_RECORD
    states:
    - PR_ABORTED_ESCALATED
    consumers: &id039 []
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id039
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81d29748eb21df73b02c?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8138ac99c13cf6f2f282?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81d29748eb21df73b02c?pvs=204
    page_last_edited_at: '2026-10-12T02:29:48.607Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: otherwise mutating the workspace, worktree, branch, open PR, commits or evidence[^.\n]*\.(?!
        Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts)
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: controlled Markdown
    - rule_id: CTR-002
      value: PF10
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: QA-10
  notion_page_id: 3f44590a05eb8134af92e7c85a48e67c
  notion_url: https://app.notion.com/p/3f44590a05eb8134af92e7c85a48e67c
  expected_title: QA-10 — Audit Implementation and Establish QA Readiness — 100926.1
  lane: QA
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Audit Implementation and Establish QA Readiness for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, the continuing Lead Developer and whole-change readiness decision owner
    for the exact supplied change.
  creator_role: Isis, the continuing Lead Developer and whole-change readiness decision owner for the
    exact supplied change.
  reviewer_role: NONE
  inputs:
  - CHANGE_CLASS
  - CHANGE_ID
  - SPECIFICATION_ID
  - IMPLEMENTATION_PLAN_ID
  - PLAN_REVIEW_ID
  - PR_INSTRUCTION_ID
  - PR_IMPLEMENTATION_PLAN_ID
  - PR_IMPLEMENTATION_RESULT_ID
  - PR_WORK_UNIT_LINEAGE_REVIEW_ID
  - OPS_TASK_ID
  - OPS_EXECUTION_RESULT_ID
  - OPS_TASK_RECEIPT
  - DOCUMENTATION_COMPLETION_ID
  - REMEDIATION_PROPOSAL_ID
  - REMEDIATION_REVIEW_ID
  - ORIGINATING_FINDING_REF
  outputs:
  - artifact: REALITY_AUDIT / CHANGE_AUDIT_TRIAGE / QA_READINESS
    states:
    - ASSESSMENT_INCOMPLETE
    - NOT_READY
    - READY_FOR_QA
    consumers: &id040
    - ESC-30
    - QA-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  required_interfaces: *id040
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8134af92e7c85a48e67c?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb818bad2fcb4bc2610b29?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8134af92e7c85a48e67c?pvs=204
    page_last_edited_at: '2026-10-12T02:30:12.398Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: CTR-001
      value: Notion and repository persistence
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: '(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?:
        and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive
        input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete
        RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict
        register\b)'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Catalogs and runtime handoffs carry\b
    - rule_id: TOP-001
      value: native inputs, lineage, current state, gates, risks and required action
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: read-only audit and readiness role
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Embed only applicable workflow contracts
    - rule_id: TOP-001
      value: A saved attachment, link or scattered fields do not replace the handoff\.
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-D
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: unresolved facts in the output artifact, which each next or recovery handoff names
    - rule_id: CTR-002
      value: every return package names those artifacts
    - rule_id: CTR-002
      value: Then give the other fields the handoff rule above names; sections the artifact already holds
        are named, not repeated\.
    - rule_id: CTR-002
      value: each input artifact by repository path; the artifacts hold the rest
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: Every statement in this prompt that it is read-only or does not change the repository excludes
        its own output artifacts, which it writes, commits and pushes, and any pull request that carries
        them\.
    - rule_id: CTR-002
      value: Reviewers remain read-only toward the work they review
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?i:No agent edits PF10 or claims canonical adoption; only the
        qualifying producer resolves an addendum's number, from the current controlled PF10 at creation\.))
      guard: G-F05-E
- prompt_key: QA-100
  notion_page_id: 3f44590a05eb8182a201f0e177dad431
  notion_url: https://app.notion.com/p/3f44590a05eb8182a201f0e177dad431
  expected_title: QA-100 — Execute Bounded QA Task — 100926.1
  lane: QA
  sequence: 100
  lifecycle: ACTIVE
  function: Execute Execute Bounded QA Task for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: Executor under the Product Owner-chosen arrangement; no executor/session identity or venue
    prerequisite; QA-110 owns evidence review.
  creator_role: Product Owner-chosen executor
  reviewer_role: Kronos through QA-110
  inputs:
  - QA_TASK_IDS
  - QA_PLAN_ID
  - QA_PLAN_REVIEW_ID
  - QA_AUDIT_ID
  - QA_STEP_ID
  - QA_TASK_ID
  outputs:
  - artifact: QA_EXECUTION_RESULT
    states:
    - BLOCKED
    - COMPLETE
    - FAILED
    - NOT_EXECUTED
    - PARTIAL
    consumers: &id041
    - QA-110
  mutations:
    allowed:
    - Execute only the bounded QA_TASK actions
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  - No Kronos executor exclusion or actor/venue identity prerequisite. All five execution states return
    to QA-110 without acceptance authority.
  required_interfaces: *id041
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8182a201f0e177dad431?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb811a8d13c0bbbf77a848?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8182a201f0e177dad431?pvs=204
    page_last_edited_at: '2026-10-12T02:30:45.204Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: QA-110
  notion_page_id: 3f44590a05eb81ee9a09e00af51f33cb
  notion_url: https://app.notion.com/p/3f44590a05eb81ee9a09e00af51f33cb
  expected_title: QA-110 — Review QA Evidence and Route the Next Action — 100926.1
  lane: QA
  sequence: 110
  lifecycle: ACTIVE
  function: Execute Review QA Evidence and Route the Next Action for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are the same continuing Kronos QA authority.
  creator_role: the same continuing Kronos QA authority.
  reviewer_role: NONE
  inputs:
  - QA_TASK_IDS
  - QA_EXECUTION_RESULT_IDS
  - QA_PLAN_ID
  - QA_PLAN_REVIEW_ID
  - QA_AUDIT_ID
  - QA_TASK_ID
  - QA_EXECUTION_RESULT_ID
  outputs:
  - artifact: QA_EVIDENCE_REVIEW
    states:
    - ACCEPT
    - BOUNDED_RERUN_REQUIRED
    - ESCALATION_REQUIRED
    - INCOMPLETE
    consumers: &id042
    - ESC-10
    - QA-100
    - QA-120
    - QA-90
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id042
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81ee9a09e00af51f33cb?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb816984d1d34da0e08f40?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81ee9a09e00af51f33cb?pvs=204
    page_last_edited_at: '2026-10-12T02:29:41.377Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: code/Ops remediation\. Do not fix it here\.(?! This applies only before the whole approved
        run is complete)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: a completed failing run is `ACCEPT` and continues to QA-120
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: QA-120
  notion_page_id: 3f44590a05eb81a4a3fbc0fae65d153e
  notion_url: https://app.notion.com/p/3f44590a05eb81a4a3fbc0fae65d153e
  expected_title: QA-120 — Create Final QA Report and RCA — 100926.1
  lane: QA
  sequence: 120
  lifecycle: ACTIVE
  function: Execute Create Final QA Report and RCA for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Kronos, continuing QA authority for this Epic or CRD.
  creator_role: Kronos, continuing QA authority for this Epic or CRD.
  reviewer_role: NONE
  inputs:
  - QA_PLAN_ID
  - QA_TASK_ID
  - QA_EXECUTION_RESULT_ID
  - QA_EVIDENCE_REVIEW_ID
  - LIVE_QA_GUIDE_ID
  - QA_AUDIT_ID
  - REALITY_AUDIT_ID
  - CHANGE_AUDIT_TRIAGE_ID
  - QA_READINESS_ID
  outputs:
  - artifact: QA_REPORT / QA_RCA / QA_INTERIM_STATUS
    states:
    - FAIL
    - INTERIM
    - PASS
    consumers: &id043
    - CL-C-10
    - CL-E-10
    - ESC-10
    - QA-110
    - QA-90
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id043
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81a4a3fbc0fae65d153e?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81589d21e798cf38e8ba?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81a4a3fbc0fae65d153e?pvs=204
    page_last_edited_at: '2026-10-12T02:29:51.614Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: QA-20
  notion_page_id: 3f44590a05eb81289c7be77f66bac909
  notion_url: https://app.notion.com/p/3f44590a05eb81289c7be77f66bac909
  expected_title: QA-20 — Create Live QA Guide — 100926.1
  lane: QA
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Create Live QA Guide for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are the same Isis who established readiness.
  creator_role: the same Isis who established readiness.
  reviewer_role: NONE
  inputs:
  - QA_READINESS_ID
  - REALITY_AUDIT_ID
  - CHANGE_AUDIT_TRIAGE_ID
  outputs:
  - artifact: LIVE_QA_GUIDE
    states:
    - BLOCKED
    - GUIDE_READY
    consumers: &id044
    - QA-10
    - QA-50
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id044
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81289c7be77f66bac909?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb816daa3adff37283482b?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81289c7be77f66bac909?pvs=204
    page_last_edited_at: '2026-10-12T02:30:15.395Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: PR-40 is entered on the observed merge event for the identified PR
    - rule_id: CTR-002
      value: 'PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: QA-50
  notion_page_id: 3f44590a05eb815d89d3e602973d83ad
  notion_url: https://app.notion.com/p/3f44590a05eb815d89d3e602973d83ad
  expected_title: QA-50 — Create Whole-Change QA Audit and Plan — 100926.1
  lane: QA
  sequence: 50
  lifecycle: ACTIVE
  function: Execute Create Whole-Change QA Audit and Plan for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Kronos, the continuing QA authority for this entire change.
  creator_role: Kronos, the continuing QA authority for this entire change.
  reviewer_role: Isis / Lead Developer
  inputs:
  - LIVE_QA_GUIDE_ID
  - REALITY_AUDIT_ID
  - CHANGE_AUDIT_TRIAGE_ID
  - QA_READINESS_ID
  outputs:
  - artifact: QA_AUDIT / QA_PLAN
    states:
    - AUDIT_COMPLETE
    - BLOCKED
    - PLAN_PENDING
    consumers: &id045
    - QA-60
    - QA-70
    - QA-80
    - QA-90
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id045
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb815d89d3e602973d83ad?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81a3ac91f602bad8cfa2?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb815d89d3e602973d83ad?pvs=204
    page_last_edited_at: '2026-10-12T02:30:48.299Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:wide latitude))(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:do
        not require an executor name))(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:executor identity, session-inspection
        API))(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:record the execution arrangement))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(executor|operator)\b))
      guard: G-F02-A
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: (?m)^(?=.*(?i:record the execution arrangement the Product Owner chooses))(?=.*(?i:not categorically
        barred from execution))
      guard: G-F02-B
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: QA-60
  notion_page_id: 3f44590a05eb81489053f72637577807
  notion_url: https://app.notion.com/p/3f44590a05eb81489053f72637577807
  expected_title: QA-60 — Create Whole-Change QA Plan — 100926.1
  lane: QA
  sequence: 60
  lifecycle: ACTIVE
  function: Execute Create Whole-Change QA Plan for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are the same continuing Kronos QA authority.
  creator_role: the same continuing Kronos QA authority.
  reviewer_role: Isis / Lead Developer
  inputs:
  - QA_AUDIT_ID
  outputs:
  - artifact: QA_PLAN
    states:
    - BLOCKED
    - PLAN_PENDING
    consumers: &id046
    - QA-70
    - QA-80
    - QA-90
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id046
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81489053f72637577807?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb810b8aa3e1692830d4b8?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81489053f72637577807?pvs=204
    page_last_edited_at: '2026-10-12T02:29:44.410Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: CTR-002
      value: \bends? `ASK OK\?`
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: TOP-001
      value: '`ASK OK\?` is the line immediately before the block\.'
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: QA-70
  notion_page_id: 3f44590a05eb81209128ea7c82938faf
  notion_url: https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf
  expected_title: QA-70 — Review Whole-Change QA Plan — 100926.1
  lane: QA
  sequence: 70
  lifecycle: ACTIVE
  function: Execute Review Whole-Change QA Plan for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, continuing Lead Developer and QA Plan reviewer.
  creator_role: Isis, continuing Lead Developer and QA Plan reviewer.
  reviewer_role: NONE
  inputs:
  - QA_PLAN_ID
  outputs:
  - artifact: QA_PLAN_REVIEW / MATERIAL_QA_PLAN_DELTA_REVIEW
    states:
    - APPROVE
    - DENY
    consumers: &id047
    - QA-80
    - QA-90
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id047
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8143bf26d1459fbbcad7?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf?pvs=204
    page_last_edited_at: '2026-10-12T02:29:54.691Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?i:Outside GCFPE\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-A
    - rule_id: CTR-001
      value: (?m)^(?=.*(?i:format recorded in the Glow Operations Hub|one `##` heading carrying its title|canonical
        PF10 build-notes addendum format))
      guard: G-F05-B
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never a gate on later work
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: (?m)^(?=.*(?i:one H2 heading with the next continuous number))(?=.*(?:PF06-Canon-Change-Process-Guide))(?=.*(?:PF27-Canon-Plan-Templates))(?=.*(?i:only
        H3 or lower))
      guard: G-F05-C
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: QA-80
  notion_page_id: 3f44590a05eb818789e9ff3ffa9e06d8
  notion_url: https://app.notion.com/p/3f44590a05eb818789e9ff3ffa9e06d8
  expected_title: QA-80 — Revise Whole-Change QA Plan — 100926.1
  lane: QA
  sequence: 80
  lifecycle: ACTIVE
  function: Execute Revise Whole-Change QA Plan for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are the same Kronos who authored the Plan.
  creator_role: the same Kronos who authored the Plan.
  reviewer_role: Isis / Lead Developer
  inputs:
  - Require one complete pending initial QA Plan plus the exact QA-70 denial/redline for that version,
    or an interrupted preapproval recovery package with the same Kronos author and Isis reviewer.
  outputs:
  - artifact: QA_PLAN
    states:
    - PLAN_PENDING_REVISED
    - WRONG_ROUTE_APPROVED_BASE
    consumers: &id048
    - QA-70
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id048
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb818789e9ff3ffa9e06d8?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb813ba9a9dbd9a641d36c?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb818789e9ff3ffa9e06d8?pvs=204
    page_last_edited_at: '2026-10-12T02:30:18.516Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: CTR-002
      value: \bends? `ASK OK\?`
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: '`WRONG_ROUTE_APPROVED_BASE` terminally'
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: TOP-001
      value: '`ASK OK\?` is the line immediately before the block\.'
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: routed as \*Required result and routing\* states
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: QA-90
  notion_page_id: 3f44590a05eb81bea720f004a7e1a6d8
  notion_url: https://app.notion.com/p/3f44590a05eb81bea720f004a7e1a6d8
  expected_title: QA-90 — Create Bounded QA Execution Task — 100926.1
  lane: QA
  sequence: 90
  lifecycle: ACTIVE
  function: Execute Create Bounded QA Execution Task for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are the continuing Kronos QA authority.
  creator_role: the continuing Kronos QA authority.
  reviewer_role: NONE
  inputs:
  - QA_PLAN_ID
  - QA_PLAN_REVIEW_ID
  - QA_STEP_IDS
  - QA_STEP_ID
  - QA_TASK_IDS
  outputs:
  - artifact: QA_TASK / QA_PREEXECUTION_FINDING
    states:
    - ESCALATION_REQUIRED
    - NOT_EXECUTED
    - TASK_READY
    consumers: &id049
    - ESC-10
    - QA-100
    - QA-110
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - QA instructions and evidence review require actual output/destination/registration mapping, canonical
    writer or owned handoff, dependencies, read-only checks and QA-110 indexing proof; not conditional
    on a ledger-bound claim.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing required indexing remains incomplete/tooling work; no hand-edit of governed artifacts or rerun
    solely to index valid evidence.
  required_interfaces: *id049
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81bea720f004a7e1a6d8?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb814d96d3dcfa8835f96d
  expected_parent_title: HDE QA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb811e8582cf30238c5b9c?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81bea720f004a7e1a6d8?pvs=204
    page_last_edited_at: '2026-10-12T02:30:51.327Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-025-INDEX
      value: Required QA evidence indexing
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: RS-10
  notion_page_id: 3f44590a05eb81a588c9c82aa8a2d3f2
  notion_url: https://app.notion.com/p/3f44590a05eb81a588c9c82aa8a2d3f2
  expected_title: RS-10 — Create Bounded Work-Unit Rescope Proposal — 100926.1
  lane: RS
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Create Bounded Work-Unit Rescope Proposal for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: Originating PR implementation author; no rescope approval authority.
  creator_role: Originating PR implementation author
  reviewer_role: Independent whole-change IA through RS-20
  inputs:
  - Supply the exact CHANGE_CLASS, CHANGE_ID and work-unit/finding identity; approved Specification and
    immutable approved Plan/review; current PF10 Markdown and applicable addenda; actual originating stage,
    owner/session, suspended boundary and read-only finding evidence; existing draft/result and any prior
    proposal/review.
  outputs:
  - artifact: RESCOPE_PROPOSAL
    states:
    - RESCOPE_PROPOSAL_PENDING_REVIEW
    consumers: &id050
    - RS-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id050
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81a588c9c82aa8a2d3f2?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb811ca0cdc66e0d508ac4?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81a588c9c82aa8a2d3f2?pvs=204
    page_last_edited_at: '2026-10-12T02:29:47.386Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: CTR-002
      value: \bends? `ASK OK\?`
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Decide it during work
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: TOP-001
      value: '`ASK OK\?` is the line immediately before the block\.'
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: RS-20
  notion_page_id: 3f44590a05eb81be9566cd6397c9424c
  notion_url: https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c
  expected_title: RS-20 — Review Bounded Work-Unit Rescope — 100926.1
  lane: RS
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Review Bounded Work-Unit Rescope for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: Independent whole-change IA reviewer; never the proposal author; no Isis rescope role.
  creator_role: Originating PR implementation author
  reviewer_role: Independent whole-change IA
  inputs:
  - 'Supply exactly one complete read-back rescope artifact: a RESCOPE_REQUEST produced by PR-30 or revised
    by RS-30, or a RESCOPE_PROPOSAL produced by RS-10 or revised by RS-30.'
  outputs:
  - artifact: RESCOPE_REVIEW
    states:
    - APPROVE
    - IN_SCOPE_REPAIR
    - REJECT
    - REVISION_REQUIRED
    - SPECIFICATION_CHANGE_REQUIRED
    consumers: &id051
    - PR-20
    - PR-30
    - PR-35
    - RS-30
    - RS-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - 'Produce substantive Canon relied on: actual current PF titles/versions/sections read, PF10/addenda,
    approved in-flight path/version and decision-topic mapping or truthful searched silence.'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  - Missing, empty, unread, unrelated or topic-incomplete canon basis cannot support a positive decision.
  - Self-authored proposal cannot receive IA approval; Isis has no rescope role; preserve original PR
    return phase and actual Proceed/vehicle.
  required_interfaces: *id051
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c?pvs=204
    page_last_edited_at: '2026-10-12T02:29:57.795Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Carry original Proceed, dedicated PR session, workspace/worktree, branch|current head; completed
        work, commits/local changes|reviews/checks already observed, unresolved items|with each actual
        PR reference, commit identity, order
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Decide it during work
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?i:Outside GCFPE\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\ballocat\w*\b[^.\n]{0,40}\bnumber|\bnumber\w*\b[^.\n]{0,20}\ballocat))
      guard: G-F05-A
    - rule_id: CTR-001
      value: (?m)^(?=.*(?i:format recorded in the Glow Operations Hub|one `##` heading carrying its title|canonical
        PF10 build-notes addendum format))
      guard: G-F05-B
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    - rule_id: AF-024-CANON
      value: Canon relied on
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: \*{0,2}Material\*{0,2} means a change to the Epic-level commitment
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: verified at entry from the recorded vehicle and repository state; the handoff does not carry
        them
    - rule_id: CTR-002
      value: (?m)^(?=.*(?i:one H2 heading with the next continuous number))(?=.*(?:PF06-Canon-Change-Process-Guide))(?=.*(?:PF27-Canon-Plan-Templates))(?=.*(?i:only
        H3 or lower))
      guard: G-F05-C
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: RS-30
  notion_page_id: 3f44590a05eb8131bc61e346a46840e9
  notion_url: https://app.notion.com/p/3f44590a05eb8131bc61e346a46840e9
  expected_title: RS-30 — Revise Bounded Work-Unit Rescope Proposal — 100926.1
  lane: RS
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Revise Bounded Work-Unit Rescope Proposal for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: Same originating PR implementation author revising the proposal; no approval authority.
  creator_role: Originating PR implementation author
  reviewer_role: Independent whole-change IA through RS-20
  inputs:
  - 'Supply exactly one RESCOPE_REQUEST_ID or RESCOPE_PROPOSAL_ID and the actual correction authority:
    either its RS-20 REVISION_REQUIRED review or Nathan''s exact Product Owner correction.'
  outputs:
  - artifact: RESCOPE_REQUEST / RESCOPE_PROPOSAL
    states:
    - RESCOPE_PROPOSAL_PENDING_REVIEW
    consumers: &id052
    - RS-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id052
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb8131bc61e346a46840e9?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81ed9fd3d2ef439ceaaf?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb8131bc61e346a46840e9?pvs=204
    page_last_edited_at: '2026-10-12T02:30:23.555Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: CTR-002
      value: \bends? `ASK OK\?`
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: TOP-001
      value: '`ASK OK\?` is the line immediately before the block\.'
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: in the output artifact's (?:existing )?permitted metadata
    - rule_id: CTR-002
      value: '(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff
        names'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: RS-40
  notion_page_id: 3f44590a05eb813993beccaaf88523d4
  notion_url: https://app.notion.com/p/3f44590a05eb813993beccaaf88523d4
  expected_title: RS-40 — Approved Rescope — Resume PR Implementation — 100926.1
  lane: RS
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Approved Rescope — Resume PR Implementation for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: 'You resume the recorded phase in its own dedicated session: PR-30''s session for a PR-30
    phase, the PR-35 session for PR_RETURN_PHASE PR-35.'
  creator_role: the recorded phase's own dedicated session for the exact suspended work unit.
  reviewer_role: NONE
  inputs:
  - RESCOPE_REVIEW
  outputs:
  - artifact: PR_IMPLEMENTATION_RESULT
    states:
    - MERGE_OBSERVED
    - MERGE_PENDING
    - PRODUCT_OWNER_DECISION_REQUIRED
    - PR_CANDIDATE_PUBLISHED
    - RECOVERY_PENDING
    - REMOTE_EVIDENCE_PENDING
    - RESCOPE_PENDING
    - SOURCE_RESOLUTION_ERROR
    consumers: &id053
    - PR-30
    - PR-35
    - PR-40
    - RS-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  - Canon relied on required for resumed PR-35 review; no new approval gate in PR-30 continuation.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id053
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb813993beccaaf88523d4?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb8195a2ccf7c0959a8b6e
  expected_parent_title: HDE IA — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb8183b5ffdf4270133226?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb813993beccaaf88523d4?pvs=204
    page_last_edited_at: '2026-10-12T02:30:54.130Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: CTR-001
      value: launched as a new session
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: Carry original Proceed, dedicated PR session, workspace/worktree, branch|current head; completed
        work, commits/local changes|reviews/checks already observed, unresolved items|with each actual
        PR reference, commit identity, order
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: 'only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual
        merge occurred|Nathan''s invocation supplies only the later manual-merge assertion|historical
        PR-35 `MERGE_PENDING` result, Nathan''s later manual-merge assertion|Nathan manual merge, PR-40
        read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|Nathan''s later merge assertion
        and PR-40''s independent|needed after Nathan''s assertion: continue to `?PR-40'
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: Repository paths outside `?docs/ephemeral/`? and `?docs/graph/`? are not written
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never a gate on later work
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: An\s+\*?In-flight decisions\*?\s+section
    - rule_id: CTR-002
      value: they do not share a session
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: '[Ss]ubscribe to the pull request'
    - rule_id: CTR-002
      value: stay subscribed and do not poll
    - rule_id: CTR-002
      value: The observed merge event is the fact PR-40 is entered on
    - rule_id: CTR-002
      value: verified at entry from the recorded vehicle and repository state; the handoff does not carry
        them
    - rule_id: CTR-002
      value: '`MERGE_OBSERVED`: [^\n]*?the subscribed PR-35 session observes the merge of the identified
        PR, performed by Nathan'
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
- prompt_key: UTIL-10
  notion_page_id: 3f44590a05eb81d997d1fd2b8d1b5042
  notion_url: https://app.notion.com/p/3f44590a05eb81d997d1fd2b8d1b5042
  expected_title: UTIL-10 — Apply Exact Redline to a Complete Artifact — 100926.1
  lane: UTIL
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Apply Exact Redline to a Complete Artifact for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the original author or explicitly authorized editor of the exact target.
  creator_role: the original author or explicitly authorized editor of the exact target.
  reviewer_role: NONE
  inputs:
  - BASE_ARTIFACT_ID
  - REDLINE_ID
  outputs:
  - artifact: REVISED_TARGET_ARTIFACT / REDLINE_APPLICATION_REPORT
    states:
    - ALREADY_APPLIED
    - COMPLETE
    - INCOMPLETE
    consumers: &id054 []
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - Complete native Notion readback matches authored content, allowing native mention display normalization
    and stripped blank lines.
  - No body corpus, body checksum or shipped validator receipt is created.
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not
    invent missing evidence.
  - Missing persistent session/executor identity is not a blocker; require exact role/task/artifact lineage
    and preserve independent authority, explicit PO context choice and known provenance.
  required_interfaces: *id054
  controlling_sources:
  - GCFPE-20261009.1
  - '100926.1'
  - https://app.notion.com/p/3f44590a05eb81d997d1fd2b8d1b5042?pvs=204
  - AGENTS.md and current PF canon on main
  expected_parent_id: 3db4590a05eb811b9c14f2ae89c28df7
  expected_parent_title: HDE TW — GCFPE-20261009.1 — 100926.1
  supersedes:
  - https://app.notion.com/p/3db4590a05eb81b89fbaf4b31a3ed2a9?pvs=204
  superseded_by: null
  source_snapshot:
    completeness: COMPLETE
    notion_url: https://app.notion.com/p/3f44590a05eb81d997d1fd2b8d1b5042?pvs=204
    page_last_edited_at: '2026-10-12T02:29:50.321Z'
    representation: NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY
  audit_assertions:
    forbidden_literals: []
    forbidden_regex:
    - rule_id: CTR-001
      value: addendum_id[\s\S]{0,400}?artifact_version
    - rule_id: CTR-001
      value: Glow / Core Docs / PFCanon
    - rule_id: CTR-001
      value: Glow / Ephemeral Planning Files
    - rule_id: CTR-001
      value: drive\.google\.com
    - rule_id: CTR-001
      value: EPHEMERAL_DRIVE
    - rule_id: SRC-001
      value: off-repositor
    - rule_id: CTR-002
      value: state the mismatch
    - rule_id: CTR-002
      value: '[Cc]ompare the current PF10'
    - rule_id: INV-003
      value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
    - rule_id: SRC-001
      value: (?<![.\w/-])glow-hde-devops(?![\w-])
    - rule_id: CTR-001
      value: CONTROL_NOTION
    - rule_id: CTR-001
      value: (?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b
    - rule_id: TOP-001
      value: (?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n|[ \t]*#)){0,1500}?(?<!\bno
        )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit
        (?:SHA|hash|identity|id)\b|\bremote head\b)
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: INV-003
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: SRC-001
      value: '(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:'
    - rule_id: CTR-001
      value: Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked
        agent|workflow agent)\b
    - rule_id: CTR-001
      value: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this
        prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
    - rule_id: CTR-001
      value: (?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b
    - rule_id: TOP-001
      value: (?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|,
        in (?:the )?returned handoff\b
    - rule_id: TOP-001
      value: 'substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery
        packages|every next and recovery package)\b|review result and every native return\b|and every
        return package\b|receipt, review and handoff metadata|receipt and handoff when applicable'
    - rule_id: TOP-001
      value: current status and lineage; decisions already made|Carry complete native inputs rather than
        referring to
    - rule_id: TOP-001
      value: unresolved items/owners, next action, and expected (?:output|review state)
    - rule_id: CTR-001
      value: Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies
        the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval
        effect is defined above
    - rule_id: CTR-001
      value: Reviewers remain read-only(?! toward the work they review)
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?!(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(no|not|never|nothing|nor|without|neither)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(recommend\w*|advice|advis\w*|guidance|suggest\w*|rank\w*)\b))(?=(?:[^.!?\n]|[.!?](?!\s))*(?i:\b(model|models|reasoning|effort|strength)\b))
      guard: G-TS-3
    - rule_id: CTR-001
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:GCFPE-MGMT-10[^.\n]{0,80}\b(?!100926\.1)\d{6}\.\d|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION))
      guard: G-MGMT-1
    required_literals:
    - rule_id: CTR-002
      value: PF10
    - rule_id: TOP-001
      value: NEXT_PROMPT_HANDOFF
    - rule_id: AF-026
      value: Role and artifact continuity
    required_regex:
    - rule_id: CTR-002
      value: docs/pfcanon/
    - rule_id: CTR-002
      value: never\s+carries\s+the\s+only\s+copy
    - rule_id: TOP-001
      value: The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.
    - rule_id: CTR-002
      value: never\s+as\s+a\s+subagent\s+of\s+another\s+session
    - rule_id: CTR-002
      value: (?m)(?:^|(?<=[.!?])\s+)(?=(?:[^.!?\n]|[.!?](?!\s))*(?:No agent gives its own recommendation,
        assessment or ranking of model, reasoning level or effort\.))
      guard: G-TS-1
    - rule_id: CTR-002
      value: '(?m)^(?=.*(?i:name the TypeSafe reading and the surface advice for the receiving session,
        with the output artifact''s path))(?=.*(?i:run the installed TypeSafe scoring skill''s script
        once))(?=.*(?i:do not paste its line into the block or write its Notion row))(?=.*(?i:holds the
        reading as the skill prints it, with its cell, every probability and its flags))(?=.*(?:`TypeSafe:
        not read` with the reason))(?=.*(?i:advice on execution surface, with no model, reasoning-level
        or effort content))(?=.*(?i:When Nathan states the model and setting chosen for this session,
        record that pick in this session''s output artifact))'
      guard: G-TS-2
global_literals:
  approval_request: ASK OK?
  approved: ASK OK.
audit_contracts:
  selected_binding:
    release: GCFPE-20261009.1
    version_family: '100926.1'
    member_count: 55
  pfcanon_source:
    required_literal: select only the controlled Markdown lane
    failure_state: SOURCE_RESOLUTION_ERROR
  pf10_boundary:
    required_literal: PF10
    direct_edit_forbidden: true
  handoff:
    required_literal: NEXT_PROMPT_HANDOFF
    nonterminal_exact_block_count: 1
```
